# CSV Analyzer

A simple command-line CSV analysis tool built with Python and pandas.

## Requirements

- Python 3.10+
- pandas

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the project folder:

```bash
python main.py
```

Then enter the path to a CSV file when prompted.

The menu supports:

1. Size of the file
2. Columns and datatype
3. Missing values
4. Statistics
5. Description of table
6. Data cleaning
7. Show correlation matrix
8. Save file
9. Exit

## Sample CSV

Use `sample.csv` as a starting dataset or replace it with your own CSV file.

## Notes

- The script expects a valid CSV path.
- `data_cleaning` fills numeric missing values with mean or median, and non-numeric missing values with `Unknown`.
- The statistics menu will automatically compute sales statistics if a `Sales` column exists.
