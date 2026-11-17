#!/usr/bin/env python3
"""Continuous geometry of the entire explicit finite m3 tail by Bernstein bounds.

All four elementary array operations round outward with nextafter. Every
sum of coefficient bounds is accumulated outward. Stored data are exact
binary constants; exact rational radial normalization is enclosed first.
The background theorem B<=8 is an explicit separate input. No metric-error
certificate or exact nonlinear solution is inferred from this geometry proof.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,math
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
for k in ['manifest','reader','background','prefix-audit','out']:p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();spec=importlib.util.spec_from_file_location('geometry_tail_reader',a.reader);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);f=m.IntegratedTail(a.manifest)
bg=json.loads(a.background.read_text());pre=json.loads(a.prefix_audit.read_text())
down=lambda x:np.nextafter(x,-np.inf);up=lambda x:np.nextafter(x,np.inf)
def exact(x):x=np.asarray(x,dtype=float);return x,x
def add(x,y):return down(x[0]+y[0]),up(x[1]+y[1])
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    z=np.stack([x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1]])
    return down(z.min(axis=0)),up(z.max(axis=0))
def div(x,y):
    assert np.all((y[0]>0)|(y[1]<0))
    return mul(x,(down(1/y[1]),up(1/y[0])))
def magnitude(x):return np.maximum(abs(x[0]),abs(x[1]))
def sum_up(x,axis=-1):
    x=np.moveaxis(x,axis,-1);out=np.zeros(x.shape[:-1])
    for i in range(x.shape[-1]):out=up(out+x[...,i])
    return out
def scalar_interval(q):
    z=float(q);lo,hi=math.nextafter(z,-math.inf),math.nextafter(z,math.inf)
    assert Q.from_float(lo)<=q<=Q.from_float(hi)
    return np.asarray(lo),np.asarray(hi)
L=mul(exact(f.unscaled_lengths[:,None]),scalar_interval(f.radial_scale))
u0,u1=exact(f.first[:-1]),exact(f.first[1:]);q0,q1=exact(f.second[:-1]),exact(f.second[1:])
b0=u0;b1=add(u0,div(mul(L,q0),exact(4)))
b4=u1;b3=sub(u1,div(mul(L,q1),exact(4)))
b2=div(sub(sub(sub(sub(mul(exact(16),exact(f.midpoint)),b0),mul(exact(4),b1)),mul(exact(4),b3)),b4),exact(6))
B=[b0,b1,b2,b3,b4]
Ubound=np.maximum.reduce([magnitude(x)for x in B])
Qbound=np.maximum.reduce([magnitude(div(mul(exact(4),sub(B[i+1],B[i])),L))for i in range(4)])
increments=mul(L,div(add(add(add(add(b0,b1),b2),b3),b4),exact(5)))
left0=np.empty_like(f.first[:-1]);left1=np.empty_like(left0)
v=exact(f.source_values[0])
for i in range(len(f.L)):
    left0[i],left1[i]=v
    v=add(v,(increments[0][i],increments[1][i]))
V=(left0,left1);Vbound=magnitude(V)
for bi in B:
    V=add(V,div(mul(L,bi),exact(5)))
    Vbound=np.maximum(Vbound,magnitude(V))
frequency=np.r_[abs(f.planar_modes),f.height_modes].astype(float)
norms={}
for name,values in [('V',Vbound),('Vr',Ubound),('Vrr',Qbound)]:
    for order in range(3):
        powers=frequency**order
        # Integer frequencies and squares are exactly represented.
        norms[name+('_theta'*order)]=float(np.max(sum_up(up(values*powers))))
def fq(x):return Q.from_float(float(x))
def sqrthi(q):
    z=fq(math.nextafter(math.sqrt(float(q)),math.inf))
    while z*z<q:z=fq(math.nextafter(float(z),math.inf))
    return z
def display(q):return dict(numerator=str(q.numerator),denominator=str(q.denominator),display_only=float(q))
aa=fq(f.meta['parameters']['rCuff']);Rcut=fq(f.meta['parameters']['rCut']);c=fq(f.meta['radialGeometry']['outerAnchor'])
delta=abs(c-Rcut);width=fq(.02)
warp_first=1+delta*Q(15,8)/width;warp_second=delta*20/width**2
V0=fq(norms['V']);Vt=fq(norms['V_theta']);Vtt=fq(norms['V_theta_theta'])
Vr=fq(norms['Vr'])*warp_first
Vrt=fq(norms['Vr_theta'])*warp_first
Vrr=fq(norms['Vrr'])*warp_first**2+fq(norms['Vr'])*warp_second
W=Q(41,100);Eroot=sqrthi(1+W*W)
eta=sqrthi(Vr*Vr+(Vt/aa)**2)
H00=Vrr+8*W*Eroot*Vr
H01=Vrt/aa+Vt/aa**2
H11=Vtt/aa**2+Vr/aa
eta2=sqrthi(H00*H00+2*H01*H01+H11*H11)
K=(8+eta2)/(1-eta)**2
zcut=fq(pre['zcut_mean']);mean=fq(pre['tail_mean_at_cut_approx'])
# The finite exact mean is enclosed by the outward coefficient integration.
meanlo=fq(v[0][f.P]);meanhi=fq(v[1][f.P])
# The geometric gauge uses the same mean coefficient as V(c), so this tiny
# mean interval suffices for position; no replacement of the true integral.
z0lo=zcut+meanlo
z0hi=zcut+meanhi+Q(bg['exact_background_height']['upper_exact'])
radius=sqrthi((Rcut+V0)**2+(z0hi+V0)**2)
base_radius=sqrthi(Rcut**2+z0hi**2)
cross_error=sqrthi(2*eta*eta)+eta*eta/2
normal_error=2*cross_error/(1-cross_error)
support=z0lo/Eroot-base_radius*normal_error-V0
Jlo=1-Vr-Vt/aa-Vr*Vt/aa
polar_Jlo=1-V0/aa-Vt/aa-V0*Vt/aa**2
assert eta<1 and cross_error<1 and Jlo>0 and polar_Jlo>0
assert K<Q(19,2) and support>Q(7,10) and radius<Q(87,100)
out=dict(scope=__doc__,inputs={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest()for p in [a.manifest,a.reader,a.background,a.prefix_audit]},
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    represented_spans=len(f.L),coefficient_count=f.C,bernstein_degrees=dict(value=5,first=4,second=3),
    complete_coefficient_bounds=norms,
    outer_ulp_reparametrization=dict(delta=display(delta),width=display(width),first_upper=display(warp_first),second_abs_upper=display(warp_second)),
    first_perturbation_g0_norm_upper=display(eta),covariant_second_perturbation_g0_norm_upper=display(eta2),
    curvature_upper=display(K),support_lower=display(support),radius_upper=display(radius),
    planar_jacobian_over_r_lower=display(Jlo),polar_angular_jacobian_over_r_squared_lower=display(polar_Jlo),
    finite_mean_at_cut_interval=[display(meanlo),display(meanhi)],
    strict_safe_bounds=dict(curvature=9.5,support=.7,radius=.87),
    geometric_statement='Every finite-tail point is regular, has upward normal, positive polar angular Jacobian, |kappa_i|<9.5, X.n>.7 and |X|<.87. Its union with the already proved collar/disk is an embedded graph over its planar image, since the planar perturbation has global derivative norm <1.',
    metric_error_certified=False,whole_closed_surface_certified=False)
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'curvature_upper':float(K),'support_lower':float(support),'radius_upper':float(radius),'eta1':float(eta),'eta2':float(eta2),'spans':len(f.L)}))
