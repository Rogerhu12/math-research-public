"""Tighten the rational moment certificate without changing its exact core.

The old Taylor remainder at degree 100 is too broad for the M24 complementary
Gram inverse. Only the remainder-generating expansion degree becomes 180.
The same exact rational moments, Neumann inverse test, unique coefficients,
physical core and original positivity floor/grid ceiling are retained.
"""
import hashlib,types
from pathlib import Path
SOURCE=Path(__file__).with_name('moment_interval_bounds.py')
SOURCE_SHA256=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
TRANSFORMS=[('def beta_characteristic(z,degree=100):','def beta_characteristic(z,degree=180):')]
text=SOURCE.read_text()
for before,after in TRANSFORMS:
    if text.count(before)!=1:raise RuntimeError('Moment certificate literal transform mismatch')
    text=text.replace(before,after)
mod=types.ModuleType('tight_moment_interval_literal');mod.__file__=str(SOURCE)
exec(compile(text,str(SOURCE),'exec'),mod.__dict__)
coefficient_enclosures=mod.coefficient_enclosures
PROVENANCE=dict(source_sha256=SOURCE_SHA256,replacements=TRANSFORMS,
    scope='Tighter exact rational interval proof of the same unique canonical coefficients; no core or equation change')
def install():
    import complementary_moment_basis as basis
    basis.coefficient_enclosures=coefficient_enclosures
