#!/usr/bin/env python3
"""Outward full-angle bounds for the actual shared Cartesian end correction.

Only finite defining coefficients are consumed. The exact integrated-tail
position is enclosed by outward quadrature identities, not by stored samples.
No angular sampling or FFT is used in these correction bounds.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,math
from fractions import Fraction as Q
import numpy as np
from interval_geometry_kernel import exact,add,sub,mul,div,sqrt,scale,dn,up

p=argparse.ArgumentParser(description=__doc__)
for k in ['prefix-data','tail-manifest','tail-reader','out']:p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--width',type=float,default=.04);a=p.parse_args()
d=np.load(a.prefix_data);pm=d['planar_modes'];hm=d['height_modes'];P=len(pm)
old=d['jets'][:,:,-1]
spec=importlib.util.spec_from_file_location('bound_cut_reader',a.tail_reader);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);f=m.IntegratedTail(a.tail_manifest)
def qi(x):
    v=float(x);l,h=dn(v),up(v);assert Q.from_float(float(l))<=x<=Q.from_float(float(h));return l,h
def row(x,i):return x[0][i],x[1][i]
L=mul(exact(f.unscaled_lengths[:,None]),qi(f.radial_scale))
u0,u1=exact(f.first[:-1]),exact(f.first[1:]);q0,q1=exact(f.second[:-1]),exact(f.second[1:])
# The integral of the quartic derivative is L[7(u0+u1)/30+8um/15+L(q0-q1)/60].
increment=mul(L,add(add(mul(qi(Q(7,30)),add(u0,u1)),mul(qi(Q(8,15)),exact(f.midpoint))),div(mul(L,sub(q0,q1)),exact(60))))
A0=exact(f.source_values[0])
for i in range(len(f.L)):A0=add(A0,row(increment,i))
A=[A0,exact(f.first[-1]),exact(f.second[-1])]
R=exact(f.meta['parameters']['rCut']);w=exact(f.meta['parameters']['wCut'])
E=add(exact(1),mul(w,w));wr=scale(div(w,R),-7)
ap=scale(div(exact(1),sqrt(E)),-1);app=scale(div(mul(w,wr),mul(E,E)),-1)
tail_p={int(k):j for j,k in enumerate(f.planar_modes)};tail_h={int(k):f.P+j for j,k in enumerate(f.height_modes)}
co=[[],[],[]]
for j,k in enumerate(pm):
    ta=[row(z,tail_p[int(k)])if int(k)in tail_p else exact(0)for z in A]
    b=exact(1 if k==1 else 0)
    target=[add(ta[0],mul(R,b)),mul(ap,add(ta[1],b)),add(mul(mul(ap,ap),ta[2]),mul(app,add(ta[1],b)))]
    for v in range(3):co[v].append(sub(target[v],exact(old[v,j])))
for j,k in enumerate(hm):
    ta=[row(z,tail_h[int(k)])if int(k)in tail_h else exact(0)for z in A]
    ismean=1 if k==0 else 0
    target=[scale(ta[0],-1),scale(mul(ap,add(ta[1],scale(w,ismean))),-1),
            scale(add(mul(mul(ap,ap),add(ta[2],scale(wr,ismean))),mul(app,add(ta[1],scale(w,ismean)))),-1)]
    for v in range(3):
        # The one gauge is chosen from this same exact mean coefficient;
        # mean position at the cut is identically the prefix mean.
        co[v].append(exact(0)if v==0 and ismean else sub(target[v],exact(old[v,P+j])))
freq=np.r_[abs(pm),hm]
norm=np.zeros((3,3))
for angular in range(3):
    for radial in range(3):
        total=0.
        for k,c in zip(freq,co[radial]):
            term=up(max(abs(float(c[0])),abs(float(c[1])))*int(k)**angular)
            total=float(up(total+term))
        norm[angular,radial]=total
H=[[Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)],
   [Q(0),Q(1),Q(0),Q(-6),Q(8),Q(-3)],
   [Q(0),Q(0),Q(1,2),Q(-3,2),Q(3,2),Q(-1,2)]]
width=Q.from_float(a.width);weight=np.empty((3,3))
for deriv in range(3):
    for jet in range(3):
        c=[H[jet][k]*math.factorial(k)//math.factorial(k-deriv)for k in range(deriv,6)]
        # Avoid Fraction floor division: factorial ratio is an integer.
        c=[H[jet][k]*(math.factorial(k)//math.factorial(k-deriv))for k in range(deriv,6)]
        degree=len(c)-1
        bern=[sum((c[j]*Q(math.comb(k,j),math.comb(degree,j))for j in range(k+1)),Q(0))for k in range(degree+1)]
        bound=max(abs(z)for z in bern)*width**(jet-deriv)
        weight[deriv,jet]=float(qi(bound)[1])
cost=np.zeros((3,3))
for radial in range(3):
    for angular in range(3):
        total=0.
        for jet in range(3):total=float(up(total+up(weight[radial,jet]*norm[angular,jet])))
        cost[radial,angular]=total
out=dict(scope=__doc__,inputs={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest()for p in [a.prefix_data,a.tail_manifest,a.tail_reader]},
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),width=a.width,
    all_angle_delta_bounds_angular_then_radial_jet=norm.tolist(),
    hermite_weight_bounds_derivative_then_endpoint_jet=weight.tolist(),
    correction_bounds_radial_then_angular_derivative=cost.tolist(),
    c2_reason='One right-end complete Cartesian two-jet function, zero two-jet at the fixed strip interior endpoint; exact Hermite identities.',
    angular_sampling_used=False,exact_tail_position_integral_enclosed=True)
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'delta':norm.tolist(),'correction_bounds':cost.tolist()}))
