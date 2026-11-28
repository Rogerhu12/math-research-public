#!/usr/bin/env python3
"""Compute the new Gamma95 terminal port with its own arc and 2048 proved angular cells."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def load(p,name):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

# The published primitive imports the full-port producer for these two arithmetic classes.
# Both CLIs provide --scripts-dir, so the import remains portable when run from W.
def helpers():
    root=Path(sys.argv[sys.argv.index('--scripts-dir')+1]) if '--scripts-dir' in sys.argv else Path(__file__).parent
    return load(root/'6a65-geometry-final-ramp-port-certificate.py','original_exact_port_calculus')

def real_curve(*args):return helpers().real_curve(*args)

def Fourier(*args,**kw):return helpers().Fourier(*args,**kw)


def main():
    ap=argparse.ArgumentParser()
    for name in ('scripts-dir','master','coast-master','master-report','gram-report','output'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--angular-cells',type=int,default=2048)
    a=ap.parse_args();t0=time.monotonic();root=a.scripts_dir
    if a.output.exists():raise FileExistsError(a.output)
    original=root/'6a65-geometry-final-ramp-port-certificate.py';port=helpers()
    gram=load(root/'6a65-geometry-ramp-native-gram-certificate.py','newgap_gram')
    cert=load(root/'6a65-m12-r137-continuous-domain.py','newgap_integer')
    model=gram.ActualRamp(a.master);g=json.loads(a.gram_report.read_text());master=json.loads(a.master_report.read_text())
    if g['source']['masterSHA256']!=sha(a.master) or master['coastSHA256']!=sha(a.coast_master) or g['source']['physicalMasterSHA256']!=master['rampSHA256']:
        raise ValueError('New source and endpoint slice must coincide')
    abox=tuple(map(Q,g['exactEllipticArcRadiusInterval']));I=cert.I
    f0=I(*abox)+I(model.v*model.ramp/2);alg=port.Series(cert)
    with np.load(a.coast_master) as rd:
        co,si=port.real_curve(rd['curve_modes'],rd['curve_coefficients']);ell=Q(float(rd['length']))
    e,pbox=port.spectral_speed_residual(co,si,model,abox,gram)
    qmin=I((pbox[0]*model.B)**2-e[0]).sqrt().lower()
    if qmin<=0:raise ArithmeticError('Squared-speed enclosure nonpositive')
    difference=port.upq(e[0]/(qmin+pbox[0]*model.B))
    # Integral of (1+vr/(2a))*ellipse speed equals f0 exactly.
    arc=f0+I(-difference,difference)
    curve=port.Fourier(co,si,cert)
    old={};tails={}
    for i,name in [(1,'V'),(2,'A')]:
        o1,o2,ot=port.old_port_fourier(model,16,i)
        old[name]=port.Fourier(o1,o2,cert);tails[name]=ot
    pi=cert.pi_interval();N=a.angular_cells;half=pi/N;halfq=half.upper();trig={}
    if N<256:raise ValueError('At least 256 closed cells required')
    def phase(index,count):
        k=index%(2*count);key=(k,count)
        if key not in trig:trig[key]=cert.sincos(pi*Q(k if k<=count else k-2*count,count))
        return trig[key]
    same={n:[Q(0)]*3 for n in old};ds={n:[Q(0)]*4 for n in old};bounds={};diag=hashlib.sha256()
    center=[I(x) for x in co[0]]
    for j in range(N):
        cp=curve.point(j,N,phase);cb=curve.box(cp,half)
        inlet=alg.inlet(curve.series(cp),arc,f0,I(model.v));whole=alg.inlet(curve.series(cb),arc,f0,I(model.v))
        for name,obj in old.items():
            op=obj.point(j,N,phase);oq=obj.series(op);ob=obj.series(obj.box(op,half))
            for r in range(3):
                val=port.taylor_difference(inlet[name],oq,whole[name],ob,halfq,r,cert)+tails[name][r]
                same[name][r]=max(same[name][r],val)
            for r in range(4):ds[name][r]=max(ds[name][r],port.upq(port.vector_bound(whole[name],r,cert)))
        geo=cert.geometry(cb[:5],arc,f0,I(model.v),I(ell),center)
        if geo['D'].lo<=0 or geo['material_derivative'].lo<=0:raise ArithmeticError('Nonpositive coast clock')
        for k,val in geo.items():bounds[k]=val if k not in bounds else cert.hull(bounds[k],val)
        diag.update(str([(n,[str(x) for x in v]) for n,v in same.items()]).encode())
        if (j+1)%256==0:print('closed boxes',j+1,'of',N,flush=True)
    out=dict(schema='new-central-gap-H65-exact-terminal-derivative-enclosure-v1',source=dict(masterSHA256=sha(a.master),
        coastMasterSHA256=sha(a.coast_master),fullPhysicalMasterSHA256=master['rampSHA256'],
        gramReportSHA256=sha(a.gram_report),entrySHA256=sha(__file__),originalPortCalculusSHA256=sha(original),
        curvatureArithmeticSHA256=sha(root/'6a65-m12-r137-continuous-domain.py'),gramArithmeticSHA256=sha(root/'6a65-geometry-ramp-native-gram-certificate.py')),
        exactTargetDefinition='a0 is true ellipse mean for the two storage dyadics; add v*ramp/2',
        globalSquaredSpeedResidual=str(e[0]),rigorousPointSpeedDifference=str(difference),sharpenedAccurateRawArc=arc.display(),
        sameNativeAnglePortDerivativeBounds={k:[gram.upper(x) for x in v] for k,v in same.items()},
        actualCoastPortGlobalNativeDerivativeBounds={k:[gram.upper(x) for x in v] for k,v in ds.items()},
        allCoastGeometry={k:x.display() for k,x in bounds.items()},fullAngularDomainCertified=True,completeClosedCells=N,
        incrementalMaximumSHA256=diag.hexdigest(),seconds=time.monotonic()-t0)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('complete',N,'D',out['allCoastGeometry']['D'],'K',out['allCoastGeometry']['nonzero_principal_curvature'],flush=True)
if __name__=='__main__':main()
