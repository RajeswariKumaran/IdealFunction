from utils.db_helper import * 
import statsmodels.api as sm
import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn.metrics import root_mean_squared_error
from utils.data_utils import load_csv_to_df
global create_and_initial_load
create_and_initial_load = True

class Function():

    def get_rmse_from_function(self, train_df):
        '''
        Get the OLS function for the set of x and y values in function_data table
        Loads the function table with x co-eff and intercept for corresponding y_number of function
        '''
        if create_and_initial_load == True:
            from utils.db_helper import create_functions_table
            create_functions_table()


        functions_data = get_data_from_table("functionsdata")
        # functions_data_transposed = functions_data.T
        functions_data_transposed = [list(i) for i in zip(*functions_data)]
        # print(functions_data_transposed[1])
        x = functions_data_transposed[1]
        #add constant to predictor variables
        x = sm.add_constant(x)
        function_list = []
        for i, yvalue in enumerate(functions_data_transposed[2:]):
            y = yvalue
            #fit linear regression model
            model = sm.OLS(y, x).fit()
            train_x = train_df['x']
            train_x = sm.add_constant(train_x)
            if (i==0): print(train_x)
            y_pred = model.predict(train_x)
            # print('type in prevp pred')
            # print(type(train_x))
            y1_rmse = root_mean_squared_error(train_df['y1'], y_pred)
            y2_rmse = root_mean_squared_error(train_df['y2'], y_pred)
            y3_rmse = root_mean_squared_error(train_df['y3'], y_pred)
            y4_rmse = root_mean_squared_error(train_df['y4'], y_pred)
            current_function = ["y" + str(i+1), model.params[1], \
                                 model.params[0], y1_rmse, y2_rmse, y3_rmse, y4_rmse, False]
            function_list.append(current_function)

        df_function = pd.DataFrame(function_list, columns=["function_number","x_coeff",\
                                                           "intercept","y1_rmse","y2_rmse",\
                                                            "y3_rmse","y4_rmse","ideal"])
        delete_data_from_table("functions")
        load_data_table("functions", df_function)
        return df_function

    def get_ideal_functions(self, rmse_df):

        def append_ideal_function(ideal_function_list, df_ideal):
            ideal_function = [df_ideal["function_number"], df_ideal["x_coeff"],\
                            df_ideal["intercept"], df_ideal["y1_rmse"],\
                            df_ideal["y2_rmse"], df_ideal["y3_rmse"],\
                            df_ideal["y4_rmse"], True]
            ideal_function_list.append(ideal_function)
            print(df_ideal["function_number"].values[0])
            update_ideal_functions(df_ideal["function_number"].values[0])
            return ideal_function_list

        ideal_function_list = []
        df_ideal1 = rmse_df[rmse_df['y1_rmse']==rmse_df['y1_rmse'].min()]
        ideal_function_list = append_ideal_function(ideal_function_list, df_ideal1)
        
        df_ideal2 = rmse_df[rmse_df['y2_rmse']==rmse_df['y2_rmse'].min()]
        ideal_function_list = append_ideal_function(ideal_function_list, df_ideal2)
        df_ideal3 = rmse_df[rmse_df['y3_rmse']==rmse_df['y3_rmse'].min()]
        ideal_function_list = append_ideal_function(ideal_function_list, df_ideal3)
        df_ideal4 = rmse_df[rmse_df['y4_rmse']==rmse_df['y4_rmse'].min()]
        ideal_function_list = append_ideal_function(ideal_function_list, df_ideal4)
        df_ideal_functions = pd.DataFrame(ideal_function_list, columns=["function_number","x_coeff",\
                                                    "intercept","y1_rmse","y2_rmse",\
                                                    "y3_rmse","y4_rmse","ideal"])
        
        return df_ideal_functions

class IdealFunction(Function):
    def __init__(self, ideal_functions):
        self.ideal_functions = ideal_functions

 
    def get_rmse_from_function(self, test_data_df):
        '''
        test_data_df contains test data x and y values
        This function identifies the best function among the 4 ideal functions
        for each row of data_df 
        '''   
        # Overridden function from base class Function

        # get a list of ideal function numbers
        column_array = ['x']
        for i in range(0, len(self.ideal_functions)):
            column_array.append(list(self.ideal_functions['function_number'][i].values)[0])
        # column_array.append(list(self.ideal_functions['function_number'][1].values)[0])
        # column_array.append(list(self.ideal_functions['function_number'][2].values)[0])
        # column_array.append(list(self.ideal_functions['function_number'][3].values)[0])
        print(column_array)


        ideal_functions_data = get_ideal_functions_data(column_array)

        # transpose functions_data to get the data of x and y in rows instead of columns
        ideal_functions_data_transposed = [list(i) for i in zip(*ideal_functions_data)]
        print("ideal_functions_data_transposed:")
        print(ideal_functions_data_transposed[0])


        x = ideal_functions_data_transposed[0]
        #add constant to predictor variables
        x = sm.add_constant(x)
        for index, row in test_data_df.iterrows():
            print(index)

            for i, yvalue in enumerate(ideal_functions_data_transposed[1:]):
                y = yvalue
                #fit linear regression model
                model = sm.OLS(y, x).fit()
                test_x = pd.DataFrame(np.array([[1, row['x']]]), columns=["const","x"])
                y_pred = model.predict(test_x)
                print(y_pred)
                y_true = pd.DataFrame(np.array([[row['y']]]), columns=["y"])
                y_rmse = root_mean_squared_error(y_true, y_pred)
                print(y_rmse)
                if (i==0): 
                    min_rmse = y_rmse
                    min_rmse_function = column_array[1]
                else:
                    if (y_rmse < min_rmse):
                        min_rmse = y_rmse
                        min_rmse_function = column_array[i+1]
            print(min_rmse)
            update_test_data(index+1, min_rmse_function, min_rmse)


        



def main():
    if create_and_initial_load:


        # create table and load data to identify 50 functions
        functions_data_df = load_csv_to_df("./data/ideal.csv")
        create_functions_data_table()
        load_data_table("functionsdata", functions_data_df)
        print(len(functions_data_df))

        # create table and load training data
        training_data_df = load_csv_to_df("./data/train.csv")
        create_training_data_table()
        load_data_table("trainingdata", training_data_df)

        # create table and load testing data
        testing_data_df = load_csv_to_df("./data/test.csv")
        create_testing_data_table()
        load_data_table("testingdata", testing_data_df)

    olsfunction = Function()
    training_data_df = load_csv_to_df("./data/train.csv")
    rmse_values = olsfunction.get_rmse_from_function(training_data_df)
    print("rmse_values")
    ideal_functions = olsfunction.get_ideal_functions(rmse_values)
    print(type(ideal_functions))
    ideal_function = IdealFunction(ideal_functions)
    testing_data_df = load_csv_to_df("./data/test.csv")
    ideal_function.get_rmse_from_function(testing_data_df)


if __name__ == '__main__':
   main()