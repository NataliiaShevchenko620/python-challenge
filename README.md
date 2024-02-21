# Python challenge
This repository contains Python scripts for performing financial and election analysis. The scripts read data from CSV files, analyze the data, and generate summary reports.


## Introduction
This project consists of two Python scripts:

- budget_analysis.py: This script analyzes financial data from a CSV file containing budget information. It calculates total months, total profits/losses, average change, and identifies the greatest increase and decrease in profits.
- election_results.py: This script analyzes election data from a CSV file containing voting information. It calculates the total number of votes, determines the winner of the election based on popular vote, and provides a breakdown of votes for each candidate.
Scripts

`budget_analysis.py`: Analyzes financial data and generates a summary report.

`election_results.py`: Analyzes election data and generates a summary report.


## Run the desired script:

```bash
budget_analysis.py
```
or

```bash
election_results.py
```

## Output:
For the script 1 we will get the file called `PyBank_analysis.txt` in the following directory:

`analysis/PyBank_analysis.txt`


For the script 2 we will get the file called `election_results.txt` in the following directory:

`analysis/election_results.txt`

The script will generate a summary report both in the console and in a text file located in the analysis directory.

## Data Sources: 

`budget_data.csv`: Contains financial data for budget analysis.

`election_data.csv`: Contains voting data for election analysis.
These files are located in directory called: `Resources/`

## Dependencies
These scripts require the `csv` and `os` modules, which are part of the Python standard library.

#License
This project is licensed under the MIT License.