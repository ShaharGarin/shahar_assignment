This program  (["xl_calcs.py"](xl_calcs.py)) is designed to go over a folder with results of an smFISH experiment. In the results files you can find counts for mRNA spots, their designation as localized to different cellular compartments and data concerning the coverage of a specific compartment in each z-plane imaged in the experiment. Each row in the file represents a single cell and each file represents a specific sample tested.

To identify each file, the program asks the user for the amount of files, the name of each file and an identifier string from the file's name.
First, the program removes any cells with 0 mRNA signals. Then, for each cell, the program calculates the ratio of mRNAs designated to each compartment and the average compartment coverage. The resulting table (without the 0 mRNA rows and the calculated new columns) is saved in a new folder, under the original folder given. The files are named according to the user's input from the beginning of the run.

After doing this for each file in a folder given by the user, the program calculates the average ratio of localization for each compartment, the average number of total signals and the average compartment coverage for each sample. It creates a new file called "Stats Table.scv". For each average, a standard error of the mean is also calculated and presented in the table.

In the future, other statistics could be added to this file. For example, a t test between the samples for each of the ratios calculated, or a correlation between the ratios and the compartment coverage.

A testing file (["test_xl_test_fun.py"](test_xl_test_fun.py)) and a file with the tested functions (["xl_test_fun.py"](xl_test_fun.py)), as well as sample csv files ("DEL" and "WT") are also provided.
