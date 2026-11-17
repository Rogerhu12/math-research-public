"""Explicit fixed-metric coordinate change: release the c8 core control.

The design core source stays frozen. The five literal transformations below
only release its first control and label that choice; all radius, positivity,
derivative and integral definitions are inherited unchanged.
"""
import hashlib,types
from pathlib import Path

SOURCE=Path(__file__).with_name('bimodal_core.py')
TRANSFORMS=[
    ('if len(actual):actual[0]=0.','if len(actual):pass  # c8 is free at fixed metric'),
    ('for v in value:v[0]=0. # Ignored c8 slot: all parameter jets must vanish.',
     '# All core controls are free in this fixed-metric coordinate system.'),
    ('C4 complementary controls with fixed c8=0 and two-harmonic primary',
     'C4 complementary controls with free c8 and two-harmonic primary'),
    ('ignored_correction_index=0','ignored_correction_index=None')]
text=SOURCE.read_text();SOURCE_SHA256=hashlib.sha256(text.encode()).hexdigest()
for old,new in TRANSFORMS:
    if text.count(old)!=1:raise RuntimeError('Fixed-core literal transformation mismatch: '+old)
    text=text.replace(old,new)
mod=types.ModuleType('fixed_bimodal_core_literal');mod.__file__=str(SOURCE)
exec(compile(text,str(SOURCE),'exec'),mod.__dict__)
make_core_class=mod.make_core_class

