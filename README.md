# Pricing Sensitivity Model

This repository includes a simple Python script that estimates the price
elasticity of demand using a log-log linear regression model.

## Files

- `pricing_sensitivity.py` — command-line tool for computing price elasticity.
- `example_data.csv` — example dataset containing `price` and `quantity` columns.

## Usage

1. Install the dependencies:

```bash
pip install pandas numpy scipy
```

2. Run the script with a CSV file that has `price` and `quantity` columns:

```bash
python pricing_sensitivity.py example_data.csv
```

The script will output an estimate of the price elasticity of demand for the
given data.
