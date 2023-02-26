## Business Scenario
This project involves processing Canadian Climate data by using a data engineer approach to download data from the Canadian Climate website and outputting one file.

## Business Requirements
The project requires downloading data from the Canadian Climate website, concatenating the downloaded files into one final CSV file named `all_years.csv`, and uploading the scripts and the final output file to a GitHub repository.

- Shell script: `toronto-climate-data-de.sh` This is used to control all operations, including data downloading, log setting, and running the Python script.

- Python script: `scripts/concat.py` This script is used to concatenate all the downloaded data into one file.

- Output file:`output/all_years.csv` This is the output file containing all concatenated downloads.

## Shell Script Program Procedure
The program procedure involves the following steps:

1. Download data with a shell command.
2. Install the required python packages using `pipenv`
2. Concatenate data to one file with the Python script.
3. Save output file in the Python script, with both `exec 1` (STDOUT) and `exec 2` (STDERR) 
4. Print out SUCCESS with a shell command.
