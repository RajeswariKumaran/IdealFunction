There are 4 training datasets and one test dataset, as well as datasets for 50 ideal functions. All data respectively consists of x-y-pairs of values.

This is a Python-program that uses training data to choose the four ideal functions which are the best fit out of the fifty provided *.

After identification of the ideal functions, the test data provided is used to determine for each and every x-ypair of values whether or not they can be assigned to the four chosen ideal functions. 
If so, the program also needs to execute the mapping and save it together with the deviation at hand

All data is  visualized logically
Where possible, suitable unit-tests are created

* The criterion for choosing the ideal functions for the training function is how they minimize the sum of all ydeviations squared (Least-Square)
** The criterion for mapping the individual test case to the four ideal functions is that the existing maximum deviation of the calculated regression does not exceed the largest deviation between
  training dataset (A) and the ideal function (C) chosen for it by more than factor sqrt(2)

Additional criteria:
- Its design is sensibly object-oriented
− It includes at least one inheritance
− It includes standard- und user-defined exception handlings
− For logical reasons, it makes use of Pandas’ packages as well as data visualization via Bokeh, sqlalchemy, as well as others
− Write unit-tests for all useful elements
− Your code needs to be documented in its entirety and also include Documentation Strings, known as ”docstrings“
