"""Release the first complementary control for the frozen-metric BVP.

The local-circle definition, integral geometry, derivatives and all rho
guards are unchanged. Only c8 and its parameter jets become unknowns.
"""
import hashlib,types
from pathlib import Path

SOURCE=Path(__file__).with_name('large_radius_local_core.py')
TRANSFORMS=[
 ('if len(actual):actual[0]=0.','if len(actual):pass  # c8 is free at fixed metric'),
 ('for v in value:v[0]=0. # Ignored c8 slot: all parameter jets must vanish.','# All complementary parameter jets are retained.'),
 ('C4 complementary controls with fixed c8=0 and two-harmonic primary','C4 complementary controls with free c8 and two-harmonic primary'),
 ('ignored_correction_index=0','ignored_correction_index=None')]
text=SOURCE.read_text();SOURCE_SHA256=hashlib.sha256(text.encode()).hexdigest()
for a,b in TRANSFORMS:
    if text.count(a)!=1:raise RuntimeError('Fixed local core transform mismatch: '+a)
    text=text.replace(a,b)
mod=types.ModuleType('fixed_large_radius_core_literal');mod.__file__=str(SOURCE)
exec(compile(text,str(SOURCE),'exec'),mod.__dict__)
make_core_class=mod.make_core_class
