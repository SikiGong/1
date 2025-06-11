#!/usr/bin/env python3
"""Pricing Sensitivity Model

This script estimates the price elasticity of demand using a log-log linear
regression model. Provide a CSV file containing 'price' and 'quantity'
columns.

Usage:
    python pricing_sensitivity.py data.csv

Example CSV structure:
    price,quantity
    10,100
    20,80

The output is an estimate of the price elasticity of demand.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import linregress


def compute_price_elasticity(price: np.ndarray, quantity: np.ndarray) -> float:
    """Compute price elasticity via log-log linear regression."""
    log_price = np.log(price)
    log_quantity = np.log(quantity)
    slope, _intercept, _r, _p, _stderr = linregress(log_price, log_quantity)
    return slope


def main(csv_path: str) -> None:
    path = Path(csv_path)
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    df = pd.read_csv(path)
    required = {'price', 'quantity'}
    if not required.issubset(df.columns):
        raise ValueError("CSV must contain 'price' and 'quantity' columns")
    elasticity = compute_price_elasticity(df['price'].values, df['quantity'].values)
    print(f"Estimated price elasticity: {elasticity:.3f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1])
