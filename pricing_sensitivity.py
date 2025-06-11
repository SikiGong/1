#!/usr/bin/env python3
"""Pricing Sensitivity Model

This script estimates the price elasticity of demand using a log-log linear
regression model. It only relies on Python's standard library.

Usage:
    python pricing_sensitivity.py data.csv

The CSV file must contain two columns named ``price`` and ``quantity``.
The script prints the estimated price elasticity of demand.
"""

import csv
import math
import sys
from pathlib import Path


def compute_price_elasticity(prices: list[float], quantities: list[float]) -> float:
    """Compute price elasticity via simple linear regression on log values."""
    if len(prices) != len(quantities):
        raise ValueError("Price and quantity lists must have the same length")
    logs_p = [math.log(p) for p in prices]
    logs_q = [math.log(q) for q in quantities]
    n = len(logs_p)
    mean_p = sum(logs_p) / n
    mean_q = sum(logs_q) / n
    numerator = sum((x - mean_p) * (y - mean_q) for x, y in zip(logs_p, logs_q))
    denominator = sum((x - mean_p) ** 2 for x in logs_p)
    return numerator / denominator


def read_csv(path: Path) -> tuple[list[float], list[float]]:
    """Read price and quantity columns from ``path``."""
    with path.open(newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        if not {"price", "quantity"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain 'price' and 'quantity' columns")
        prices = []
        quantities = []
        for row in reader:
            prices.append(float(row["price"]))
            quantities.append(float(row["quantity"]))
    if not prices:
        raise ValueError("CSV contains no rows")
    return prices, quantities


def main(csv_path: str) -> None:
    path = Path(csv_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    prices, quantities = read_csv(path)
    elasticity = compute_price_elasticity(prices, quantities)
    print(f"Estimated price elasticity: {elasticity:.3f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1])
