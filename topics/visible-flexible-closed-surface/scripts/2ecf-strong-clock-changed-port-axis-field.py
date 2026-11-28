#!/usr/bin/env python3
"""Finite full-geometry lift of two bounded-curvature meridians for the actually changed outer port."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import numpy as np
def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec);sys.modules[n]=m;spec.loader.exec_module(m);return m
axis=load(Path(__file__).with_name("2ecf-strong-clock-axis-field.py"),"actual_2D_axial_field")
cut=axis.cut;c=cut.c
def main(args):
    original=cut.setup
    selection=json.loads(args.selection.read_text())
    short=json.loads(args.short_axis.read_text())
    if (short["selection"]!=c.sha(args.selection) or short["portIndex"]!=args.port_index
        or selection["prepared"]!=c.sha(args.prepared) or selection["parent"]!=c.sha(args.parent)
        or selection["clock"]!=c.sha(args.clock)):
        raise ValueError("Actual short curve and reconstructed outer port differ")
    row=selection["rows"][args.port_index]
    if row["betaPi"]!=0:raise ValueError("Using the original long-axis curve requires the same port along y=0")
    maxlong=0.
    def setup(a):
        nonlocal maxlong
        saved,d,basis,seed,mods,warm,clock,oldA,Z=original(a)
        for name,value in seed.items():
            cache=value["cache"]
            raw,err=cut.changed(warm,cache,value["rawbase"],oldA,row["Afraction"]*oldA,Z,basis.c,basis.end,row["startFraction"],0.)
            if name=="training":
                maxlong=float(np.max(abs(raw[:,[0,1,3],0]-value["rawbase"][:,[0,1,3],0])))
                if maxlong>1e-8:raise ArithmeticError("Long axis no longer matches the genuine old-curve source")
            value["rawbase"]=raw
        return saved,d,basis,seed,mods,warm,clock,row["Afraction"]*oldA,Z
    cut.setup=setup
    dest=args.output
    with tempfile.TemporaryDirectory(dir=dest.parent) as tmp:
        args.output=Path(tmp)/"field.json"
        axis.main(args)
        obj=json.loads(args.output.read_text())
    obj.update(selectedPort=selection["rows"][args.port_index],portSelection=c.sha(args.selection),portIndex=args.port_index,
        wrapperEntry=c.sha(__file__),unchangedLongActualRadialJets=maxlong)
    print(json.dumps(dict(SHA256=c.save(dest,obj),best=obj["chosenNonzeroTrainingIndex"],G11=obj["actualIndependent"]["metric"],
        curvature=obj["actualIndependent"]["curvature"],held=obj["actualIndependent"]["held"])),flush=True)
if __name__=="__main__":
    ap=argparse.ArgumentParser();c.common_args(ap)
    for k in ("clock","observer","long-axis","short-axis","selection","output"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--port-index",type=int,required=True)
    main(ap.parse_args())
