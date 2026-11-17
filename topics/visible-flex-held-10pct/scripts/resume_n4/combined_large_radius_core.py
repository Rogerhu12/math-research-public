"""Sharpen the sufficient rho guard for the same complete local-circle core.

All core values, derivatives and equations remain identical. The actual
complementary coefficient vector is combined before taking absolute bounds,
including the original exact coefficient intervals and dot-product allowance.
The same rho floor, positivity grid ceiling and value allowance remain.
"""
import hashlib,types
from pathlib import Path
SOURCE=Path(__file__).with_name('large_radius_local_core.py')
SOURCE_SHA256=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
TRANSFORMS=[
 ('from complementary_moment_basis import ComplementaryMomentBasis',
  'from complementary_moment_basis import ComplementaryMomentBasis\nfrom combined_control_bounds import bounds as _combined_control_bounds'),
 ('triangle=float(np.sum(abs(self.c)*rb))',
  'combined_bounds=_combined_control_bounds(self.basis,self.c,self.lam) if self.basis is not None else (0.,0.)\n            triangle=combined_bounds[0]'),
 ('base_prime+float(np.sum(abs(self.c)*db))','base_prime+combined_bounds[1]')]
text=SOURCE.read_text()
for before,after in TRANSFORMS:
    if text.count(before)!=1:raise RuntimeError('Combined core guard literal transform mismatch: '+before)
    text=text.replace(before,after)
mod=types.ModuleType('combined_large_radius_core_literal');mod.__file__=str(SOURCE)
exec(compile(text,str(SOURCE),'exec'),mod.__dict__)
make_core_class=mod.make_core_class
PROVENANCE=dict(source_sha256=SOURCE_SHA256,replacements=TRANSFORMS,scope=__doc__)
