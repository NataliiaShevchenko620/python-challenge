# Python challenge
This repository contains Python scripts for performing financial and election analysis. The scripts read data from CSV files, analyze the data, and generate summary reports.


## Introduction
This project consists of two Python scripts:

- PyBank/main.py: This script analyzes financial data from a CSV file containing budget information. It calculates total months, total profits/losses, average change, and identifies the greatest increase and decrease in profits.
- PyPoll/main.py: This script analyzes election data from a CSV file containing voting information. It calculates the total number of votes, determines the winner of the election based on popular vote, and provides a breakdown of votes for each candidate.
Scripts

`PyBank/main.py`: Analyzes financial data and generates a summary report.

`PyPoll/main.py`: Analyzes election data and generates a summary report.


## Run the desired script:

```bash
PyBank/main.py
```
or

```bash
PyPoll/main.py
```

## Output:
For the script 1 we will get the file called `analysis_summary.txt` in the following directory:

`PyBank/analysis/analysis_summary.txt`


For the script 2 we will get the file called `election_results.txt` in the following directory:

`PyPoll/analysis/election_results.txt`

The script will generate a summary report both in the console and in a text file located in the analysis directory.

## Data Sources: 

`PyBank/Resources/budget_data.csv`: Contains financial data for budget analysis.

`PyPoll/Resources/election_data.csv`: Contains voting data for election analysis.

## Dependencies
These scripts require the `csv` and `os` modules, which are part of the Python standard library.

#License
This project is licensed under the MIT License.