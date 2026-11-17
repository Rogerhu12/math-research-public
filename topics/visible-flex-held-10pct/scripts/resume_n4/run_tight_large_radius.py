#!/usr/bin/env python3
"""Run the unchanged large-radius BVP with a tighter coefficient certificate."""
import runpy
from pathlib import Path
from tight_moment_interval_bounds import install,PROVENANCE
install()
source=Path(__file__).with_name('run_large_radius_circle.py')
text=source.read_text()
needle="source_transforms=TRANSFORMS,rows=rows"
if text.count(needle)!=1:raise RuntimeError('Literal run provenance transformation mismatch')
text=text.replace(needle,'source_transforms=TRANSFORMS,coefficient_certificate=COEFFICIENT_CERTIFICATE,rows=rows')
exec(compile(text,str(source),'exec'),dict(__name__='__main__',__file__=str(source),COEFFICIENT_CERTIFICATE=PROVENANCE))
