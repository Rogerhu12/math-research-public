#!/usr/bin/env python3
"""True Γ95 and R205 endpoint defects against the proxy Fourier controls in the HF64 field."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import time
from fractions import Fraction as Q
from pathlib import Path
for s in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[s]='1'
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def absI(I,x):return I.raw(x.absupper(),x.absupper())


def convert(K,vals):
    def bounds(v):return float(v.lower()),float(v.upper())
    arr=np.array([bounds(v) for v in vals])
    return K.I(np.nextafter(arr[:,0],-np.inf),np.nextafter(arr[:,1],np.inf))


def ulp_vec(K,rows):
    sh=np.asarray(rows,dtype=object).shape
    return convert(K,np.asarray(rows,dtype=object).ravel()).reshape(*sh)


def run(args):
    tic=time.monotonic();s=args.scripts
    cf=s/'6a65-m12-r137-continuous-domain.py';ff=s/'6a65-geometry-final-ramp-port-certificate.py'
    kf=s/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py';bf=s/'2ecf-strong-accurate-polar-port-budgets.py'
    c=load(cf,'edge_c');p=load(ff,'edge_f');k=load(kf,'edge_k');b=load(bf,'edge_b')
    if sha(args.coast)!=p.COAST_SHA or sha(args.ramp)!=p.RAMP_SHA:raise ValueError('Incorrect actual Γ95')
    I=c.I;N=args.cells;J=p.Series(c);pi=c.pi_interval();half=pi/N
    arc=I(p.ARC_LO,p.ARC_HI);eps=Q('2.453e-17');scale=I(1-eps,1+eps);a=arc*scale
    with np.load(args.ramp) as inp:A,B=[I(Q(float(inp[v]))) for v in ('centralA','centralB')]
    with np.load(args.coast) as inp:
        co,si=p.real_curve(inp['curve_modes'],inp['curve_coefficients'])
        v,L=[I(Q(float(inp[key]))) for key in ('v','length')]
    C0=[I(x) for x in co[0]];r0=a/v;delta=L*(2*r0+L)
    curve=p.Fourier(co,si,c,8);rf=b.RightPort(c,args.integral_panels);trig={}
    def phase(index,n):
        index%=2*n
        key=(index,n)
        if key not in trig:trig[key]=c.sincos(pi*Q(index if index<=n else index-2*n,n))
        return trig[key]
    # Composite Simpson on every half-bin. All centres are cumulative endpoints.
    def ell(sn,cs):return ((A*sn).square()+(B*cs).square()).sqrt()
    M=[A.upper()**2/(2*B.lower())]
    M.append((2*A.upper()**2+2*M[0]**2)/(2*B.lower()))
    M.append((4*A.upper()**2+6*M[0]*M[1])/(2*B.lower()))
    M.append((8*A.upper()**2+8*M[0]*M[2]+6*M[1]**2)/(2*B.lower()))
    cum=[I(0)];err=absI(I,half)**5*I(M[3])/2880
    for j in range(2*N):
        y0=ell(*phase(j, N));ym=ell(*phase(2*j+1,2*N));y1=ell(*phase(j+1,N))
        q=half*(y0+4*ym+y1)/6
        cum.append(cum[-1]+q+I.raw(-err.hi,err.hi))
    ae=cum[-1]/(2*pi)
    H={w:{side:[] for side in ('left','right')} for w in ('center','box','u','width')}
    for j in range(N):
        pt=curve.point(j,N,phase,order=7);box=curve.box(pt,half,order=6)
        for tag,vals in [('center',pt),('box',box)]:
            port=b.left_port(c,J,curve.series(vals,6),arc,a,scale,v,L,C0)
            geo=c.geometry(vals[:5],arc,a,v,L,C0)
            if tag=='center':
                ratio=geo['ratio']
                w=delta/(r0+(r0.square()+(1+ratio.square())*delta).sqrt())
                x=ratio*w/(r0+w)
                if x.absupper()>c.SCALE//4:raise ValueError('Small phase expansion failed')
                # atan x = x-x³/3+x⁵/5 + O(|x|^7/7), both signs.
                errx=(absI(I,x)**7/7).hi
                bet=x-x**3/3+x**5/5+I.raw(-errx,errx)
                # R233 gives |η−θ|<1.075e-14 and U'_ellipse≤A/aellipse.
                errangle=(I(Q('1.075e-14'))*A/ae).hi
                uc=cum[2*j+1]/ae+I.raw(-errangle,errangle)-bet/v
                H['u']['left'].append(uc);H['u']['right'].append(pi*Q(2*j+1,N))
                sj,cj=phase(2*j+1,N)
                sn,cs=absI(I,sj),absI(I,cj)
                # Do not replace a narrow rigorous centre by its absolute upper alone.
                def abst(x):return I.raw(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),x.absupper())
                sn,cs=abst(sj),abst(cj)
            else:
                q=c.norm2(vals[1]).sqrt()
                H['width']['left'].append(half*q*geo['material_derivative']/arc)
                H['width']['right'].append(half)
                qj=j%(N//2);jj=qj if qj<N//4 else N//2-qj-1
                sn0,cs0=phase(2*jj,N);sn1,cs1=phase(2*jj+2,N)
                sn=I.raw(max(0,sn0.lo),min(c.SCALE,sn1.hi));cs=I.raw(max(0,cs1.lo),min(c.SCALE,cs0.hi))
            H[tag]['left'].append(port)
            right=rf.port(sn,cs);sx=1 if j<N//4 or j>=3*N//4 else -1;sy=1 if j<N//2 else -1
            for key,value in right.items():
                factor=sx*sy if key in ('U','SU','AU') else 1
                right[key]=[factor*sx*value[0],factor*sy*value[1],factor*value[2]]
            H[tag]['right'].append(right)
    with np.load(args.field) as inp:proxy=inp['endpointProxy']
    bounds={}
    for side,cs in zip(('left','right'),proxy):
        uc=ulp_vec(k,H['u'][side]);dw=ulp_vec(k,H['width'][side]);m=np.arange(cs.shape[1])
        sn,co=k.sincos(uc[:,None]*k.I(m[None,:]));res={}
        # Complete closed-cell u enclosures around exact centres; speed conversion
        # uses the terminal native derivative, not the inlet derivative alone.
        for portname,ukey,z in zip(('P','V','A'),('U','SU','AU'),cs):
            real=k.I(z.real);imag=k.I(z.imag)
            C=(co[:,:,None]*real[None,:,:]-sn[:,:,None]*imag[None,:,:]).sum(1)
            Cp=-(sn[:,:,None]*real[None,:,:]+co[:,:,None]*imag[None,:,:])
            Cp=(Cp*k.I(m[None,:,None])).sum(1)
            Cpp=((k.I(real.abs_upper())+k.I(imag.abs_upper()))*k.I(m[:,None])**2).sum(0)
            true=ulp_vec(k,[x[portname] for x in H['center'][side]])
            truep=ulp_vec(k,[x[ukey] for x in H['center'][side]])
            truepbox=ulp_vec(k,[x[ukey] for x in H['box'][side]])
            e0=k.I((true-C).abs_upper());e1=k.I((truep-Cp).abs_upper())
            d=k.I(dw.abs_upper())[:,None]
            e1box=k.I((truepbox-Cp).abs_upper())+Cpp[None,:]*d
            ebox=e0+e1box*d
            if portname=='P':
                M2=ulp_vec(k,[x['UU'] for x in H['box'][side]])
                sec=k.I(M2.abs_upper())+Cpp[None,:]
                ebox2=e0+e1*d+sec*d.square()/2
                ebox=k.I(np.minimum(ebox.hi,ebox2.hi))
                e1box=k.I(np.minimum(e1box.hi,(e1+sec*d).hi))
            res[portname]=np.nextafter(np.max(ebox.hi,axis=0).astype(float),np.inf).tolist()
            res[ukey]=np.nextafter(np.max(e1box.hi,axis=0).astype(float),np.inf).tolist()
        bounds[side]=res
    out=dict(schema='HF64-actual-Gamma95-R205-edge-Fourier-proxy-certified-defects-v1',
        fieldSHA256=sha(args.field),sourceSHA256=sha(__file__),dependencies={p.name:sha(p) for p in (cf,ff,kf,bf)},
        nativeAngleCells=N,rightIntegralPanels=args.integral_panels,
        bounds=bounds,ellipseMean=ae.display(),simpsonFourthDerivativeExactUpper=str(M[-1]),seconds=time.monotonic()-tic)
    with args.output.open('x') as handle:json.dump(out,handle,indent=2);handle.write('\n')
    print(json.dumps(bounds),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for n in ('scripts','field','ramp','coast','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--cells',type=int,default=1024);ap.add_argument('--integral-panels',type=int,default=4096)
    a=ap.parse_args()
    if a.cells%4:raise ValueError('Right quadrants require aligned cells')
    run(a)
