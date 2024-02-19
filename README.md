# Code Repository for Data Generation Process of A Robust Optimization Framework for Two-Echelon Vehicle and UAV Routing for Post-Disaster Humanitarian Logistics Operations
This code repository is for the data generation process of A Robust Optimization Framework for Two-Echelon Vehicle and UAV Routing for Post-Disaster Humanitarian Logistics Operations. All the data and code for the data generation used in the paper will be provided in both Jupiter Notebook and Python format. Users may be able to reproduce all the data presented in the paper and perform further testing by following the instructions. 

The Jupiter Notebook file for all methods described in the paper is available in the Jupiter_Code subfolder of this repository. 

*Jupiter Notebook version used:*
- Jupiter Notebook version 6.5.2 in Anaconda Distribution version 2.3.1

The Python file for all methods described in the paper is available in the Python_Code subfolder of this repository. 

*Python version used:*
- Python version 3.12.0
  
*Python packages required to run the code:*
- NumPy
- pandas
- struct
- os

**Before trying to run any of the files in your environment please make sure that all the paths point to the correct folders, paste the data under the corresponding relative path, and go over the function comments in the code.**


## To reproduce the Data Sampling Process
* Run: instance_gene.py/instance_gene.ipynb
* Note:
  * Input file name, output file name, and output file path could be user-specified.
  * Output data size/the amount of data sampled must be specified by the user in the code files.
  * Please keep the file "PR_DATA.xlsx" in the same folder as the code file.


## To reproduce the Data Instance for the Optimization Problem
* To produce input data for the optimization problem involving Two-Echelon Vehicle and UAV Routing for Post-Disaster Humanitarian Logistics Operations, several steps need to be undertaken.
* Please complete the following steps:
  * Choose any CSV file from the instance folder in the repository.
  * Begin by copying the community name, longitude, and altitude data from the output file generated during the data sampling process. Paste this information into the first tab, 'N', starting from line 30 in the selected CSV file.
  * Next, copy the community name and demand data from the output file obtained during the data sampling process. Paste these details into the fourth tab, 'T', of the chosen CSV file.
* Note:
  * Ensure the provided instructions are carried out upon completing the Data Sampling Process.
  * Retain all other elements except those explicitly addressed in the instructions.
