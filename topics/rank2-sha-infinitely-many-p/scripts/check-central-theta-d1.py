#!/usr/bin/env python3
"""Finite certificates for the exact global value of the lowest central trace.

The accompanying proof supplies 4*d1 in Z[i] and the archimedean bound B.
This script checks the required high-precision residue, its uniqueness range,
and the canonical CM-unit orientation.  It makes no floating-point estimates.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import subprocess
import sys

HERE = Path(__file__).resolve().parent
B = 256 * 27 * (493*21777 + 1058969) // 8
M = 3**24
assert B == 10190905920
# 256*sqrt(2) < 512 is a sufficient integer bound.
assert 4*B + 512 < M

result = subprocess.run(
    [sys.executable, str(HERE/"check-central-theta-inert.py"), "3", "1", "24"],
    check=True, text=True, capture_output=True)
raw3 = json.loads(result.stdout)
assert raw3["ring_precision"] == 24 and raw3["orbit_size"] == 256
assert raw3["no_CLS_calibration"]
row1 = next(r for r in raw3["rows"] if r["m"] == 1)
assert row1["coefficient_denominator_loss"] == 0
assert row1["trace_scaled_coefficients_1_i"] == [64, 64]

# The p=13 point-orbit calibration is already audited independently.
with redirect_stdout(io.StringIO()):
    env = runpy.run_path(str(HERE/"check-central-theta-p13.py"))
R, ii = env["R"], env["i"]
total = R(0)
row = env["S0"]
for b in range(16):
    point = row
    for a in range(16):
        x, y, u = point
        total += -u*x-y
        point = env["gen_minus3"](point)
    row = env["gen_minus2_plus_i"](row, ii)
assert row == env["S0"]

# rotation = epsilon^(-1) for the actual point-orbit rotation epsilon.
# Weight 3 therefore needs rotation^3, not the factor used for weights 13,25.
calibrated = env["rotation"]**3 * total
assert calibrated == 64*(-1+ii)

print(json.dumps({
    "archimedean_bound_B": B,
    "clearing_denominator": 4,
    "high_precision_modulus": M,
    "uniqueness_integer_check": 4*B+512 < M,
    "raw_d1_coefficients_mod_3_power_24": [64,64],
    "raw_d1_mod_13_power_5": total.scalar(),
    "canonical_d1_mod_13_power_5": calibrated.scalar(),
    "canonical_d1_exact_coefficients_1_i": [-64,64],
    "canonical_norm": 2**13,
    "normalized_e1": "4/4913",
},indent=2))
