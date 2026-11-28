#!/usr/bin/env python3
"""All-angle anisotropic-ray boundary graph certificate for the new-gap H65 accurate exit."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(sp);sys.modules[name]=mod;sp.loader.exec_module(mod)
    return mod
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args):
    tick=time.monotonic()
    root=args.scripts
    cp=root/'6a65-m12-r137-continuous-domain.py'
    fp=root/'6a65-geometry-final-ramp-port-certificate.py'
    cert=load(cp,'exit_graph_int');port=load(fp,'exit_graph_fourier')
    tr=json.loads(args.trace.read_text());endpoint=json.loads(args.endpoint_input.read_text())
    if (sha(args.coast)!=tr['source']['coastMasterSHA256'] or sha(args.ramp)!=endpoint['source']['physicalMasterSHA256']
        or sha(args.endpoint_input)!=tr['source']['gramReportSHA256'] or not tr['fullAngularDomainCertified']):
        raise ValueError('Independent new accurate terminal trace and source required')
    I=cert.I
    arc=I(Q(tr['accurateRawArc']['lo']),Q(tr['accurateRawArc']['hi']))
    f0=I(Q(tr['exactTargetRadius']['lo']),Q(tr['exactTargetRadius']['hi']))
    scale=f0/arc
    with np.load(args.ramp) as r:
        A,B,c=[I(Q.from_float(float(r[k]))) for k in ('centralA','centralB','centralLength')]
    with np.load(args.coast) as z:
        co,si=port.real_curve(z['curve_modes'],z['curve_coefficients'])
        L,v=[I(Q.from_float(float(z[k]))) for k in ('length','v')]
    curve=port.Fourier(co,si,cert,max_order=6)
    pi=cert.pi_interval();trig={}
    def phase(index,count):
        m=index%(2*count)
        if m not in trig:trig[m]=cert.sincos(pi*Q(m if m<=count else m-2*count,count))
        return trig[m]
    center=[I(x) for x in co[0]]
    minimum={}; maximum={}; ids={}; rows=hashlib.sha256()
    for j in range(args.cells):
        val=curve.box(curve.point(j,args.cells,phase,order=5),pi/args.cells,order=4)
        gamma,p,q=val[:3]
        geo=cert.geometry(val,arc,f0,v,L,center)
        k=geo['ratio'];K=geo['Tu']
        energy=cert.norm2(p);vel=energy.sqrt()
        cross=cert.cross(p,q);crossnorm=cert.norm2(cross).sqrt()
        curvature=crossnorm/(energy*vel)
        T=cert.scale(1/vel,p)
        NF=cert.scale(1/(energy*curvature),cert.sub(q,cert.scale(cert.dot(p,q)/energy,p)))
        BF=cert.scale(1/crossnorm,cross)
        d=cert.add(cert.scale(-v/K,NF),cert.scale((1-(v/K).square()).sqrt(),BF))
        r0=f0/v;delta=L*(2*r0+L)
        w=delta/(r0+(r0.square()+(1+k.square())*delta).sqrt())
        start=cert.add(center,cert.scale(scale,cert.sub(gamma,center)))
        x=cert.add(start,cert.scale(w,cert.sub(d,cert.scale(k,T))))
        tangent=cert.scale(1/(r0+L),cert.add(cert.scale(k*w,d),cert.scale(r0+w,T)))
        det=x[0]*tangent[1]/A.square()-x[1]*tangent[0]/B.square()
        current=dict(transverse=det,height=x[2],aboveCentral=x[2]-c,materialAngleDerivative=geo['material_derivative'])
        for name,val in current.items():
            if name not in minimum or val.lo<minimum[name]:minimum[name]=val.lo;ids[name]=j
            if name not in maximum or val.hi>maximum[name]:maximum[name]=val.hi
        rows.update(str([(a,b.lo,b.hi) for a,b in current.items()]).encode()+b'\n')
    out=dict(schema='new-central-gap-complete-exit-anisotropic-ray-graph-v1',
             exactLower={n:str(Q(v,cert.SCALE)) for n,v in minimum.items()},
             exactUpper={n:str(Q(v,cert.SCALE)) for n,v in maximum.items()},minimumCells=ids,
             cells=args.cells,integerBits=cert.BITS,allRowsSHA256=rows.hexdigest(),arc=[str(arc.lower()),str(arc.upper())],
             accurateScale=scale.display(),terminalPrimitiveSHA256=sha(args.trace),endpointInputSHA256=sha(args.endpoint_input),entrySHA256=sha(__file__),integerSHA256=sha(cp),fourierSHA256=sha(fp),
             rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),
             boundaryGraphAndPositiveHeight=all(v>0 for v in minimum.values()),seconds=time.monotonic()-tick)
    with args.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(dict(lower={k:float(Q(v,cert.SCALE)) for k,v in minimum.items()},upper={k:float(Q(v,cert.SCALE)) for k,v in maximum.items()},seconds=out['seconds'])))
    if not out['boundaryGraphAndPositiveHeight']:raise ArithmeticError('Boundary graph/height proof did not close')


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for name in ('scripts','ramp','coast','trace','endpoint-input','output'):ap.add_argument('--'+name,required=True,type=Path)
    ap.add_argument('--cells',type=int,default=1024)
    args=ap.parse_args()
    if args.cells<256:raise ValueError('At least 256 complete angle cells required')
    run(args)
