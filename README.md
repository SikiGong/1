# Pricing Sensitivity Model

This repository provides a lightweight Python script for estimating the price
elasticity of demand using a log-log regression. The implementation relies only
on the Python standard library so no additional packages are required.

## Files

- `pricing_sensitivity.py` — command-line tool for computing price elasticity.
- `example_data.csv` — example dataset containing `price` and `quantity` columns.

## Usage

1. Run the script with a CSV file that has `price` and `quantity` columns. If the
   file path contains spaces, wrap it in quotes:

```bash
python pricing_sensitivity.py "~/Desktop/Doogooda/EDA/2024_long_ver2 (1).csv"
```

2. The script will output an estimate of the price elasticity for the provided
   data.
