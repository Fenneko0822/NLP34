# NLP34

## Data Preprocessing Steps

This section describes how to preprocess the dataset before training or analysis.

### Step 1: Download the Data
Download the .tar.gz files from the [PMC Open Access XML Repository](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/).

### Step 2: Extract the Files
After downloading, extract the .tar.gz archive to obtain a folder containing .xml files.

### Step 3: Convert XML to CSV
Run [`xml_to_csv.py`](https://github.com/Fenneko0822/NLP34/blob/main/xml_to_csv.py) to convert all .xml files in the folder into a structured CSV file.

### Step 4: Check for Empty Rows
Use [`double_check.py`](github.com/Fenneko0822/NLP34/blob/main/double_check.py) to verify that the resulting CSV file contains no rows with empty columns.
