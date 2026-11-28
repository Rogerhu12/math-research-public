#!/usr/bin/env python3
"""Observe direct physical coordinates without the R289 spatial maps. Geometry and hard-shape certificates are separate."""
from pathlib import Path
import importlib.util
p=Path(__file__).with_name('2ecf-r289-cubic-meridian-physical-observe.py');sp=importlib.util.spec_from_file_location('r295_direct_obs',p);obs=importlib.util.module_from_spec(sp);sp.loader.exec_module(obs)
Original=obs.Field
class Direct(Original):
    def __init__(self,g,archive):
        super().__init__(g,archive);obs.G.F.k.slab=lambda j:(j,None);obs.G.F.k.ball=lambda j:j
if __name__=='__main__':obs.Field=Direct;obs.__file__=str(Path(__file__).resolve());obs.main()
