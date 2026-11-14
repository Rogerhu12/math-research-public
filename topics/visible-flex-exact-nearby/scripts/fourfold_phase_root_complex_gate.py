#!/usr/bin/env python3
"""Local complex denominator gates at an already certified symmetric root.

The real collar lies inside one common polynomial span. Complete polynomial
Taylor bounds cover complex radial arguments; multivariate Bell majorants
cover the true unit-tangent formula on a complex angular strip. The infinite
primitive is bounded directly by its periodic convolution norm. No finite
FFT is substituted in this calculation, and no global radial analyticity is
asserted across spline knots.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import ceiling_float, interval_exp
from fourfold_phase_root_interval import Box, stack
from fourfold_phase_core_interval import CoreTarget
from fourfold_phase_uniform_tail import (
    up, down, add_up, mul_up, exact_iv, endpoint_up, exp_up, weighted_sum_up,
)


def positive_sum(values):
    answer = 0.
    for value in values:
        answer = add_up(answer, value)
    return answer


def product(*values):
    answer = 1.
    for value in values:
        answer = mul_up(answer, value)
    return answer


def pad_jet(value, degree):
    count = value.lo.shape[0]
    shape = (degree+1-count,)+value.lo.shape[1:]
    return Box(np.concatenate([value.lo,np.zeros(shape)]),
               np.concatenate([value.hi,np.zeros(shape)]))


def polynomial_product(left, right):
    order = len(left.lo)-1
    return stack([sum((math.comb(n,j)*left[j]*right[n-j] for j in range(n+1)),Box(0.))
                  for n in range(order+1)])


def physical_polynomial_jets(target, x):
    """All derivatives of the physical phase polynomials, not just raw ones."""
    def one_side(value):
        base = target.base.jets(value,order=5)
        base20 = pad_jet(base,20).reshape(21,1)
        raw = pad_jet(target.phase.jets(value,order=5),20)
        beta, gamma = raw[:,:,0],raw[:,:,1]
        for _ in range(3): beta = polynomial_product(beta,base20)
        for _ in range(2): gamma = polynomial_product(gamma,base20)
        radius = base+target.shift.jets(value,order=5)
        for alpha,sp in zip(target.alpha,target.means): radius += alpha*sp.jets(value,order=5)
        height = target.height_primitive.jets(value,order=6)
        return beta,gamma,radius,height
    plus,minus = one_side(x),one_side(-x)
    signs = (-1.)**np.arange(21)
    beta = (plus[0]+minus[0]*signs[:,None])*.5
    gamma = (plus[1]-minus[1]*signs[:,None])*.5
    radius = (plus[2]+minus[2]*signs[:6])*.5
    height = (plus[3]-minus[3]*signs[:7])*.5
    return beta,gamma,radius,height


def imaginary_taylor(real_jets, width, order=5):
    """The exact finite polynomial Taylor expansion in i Im(x)."""
    bounds = real_jets.abs_upper()
    result = []
    for j in range(order+1):
        total = np.zeros(bounds.shape[1:])
        power = 1.
        for k in range(j,len(bounds)):
            reciprocal = ceiling_float(Fraction(1,math.factorial(k-j)))
            total = add_up(total,product(bounds[k],power,reciprocal))
            power = mul_up(power,width)
        result.append(total)
    return np.asarray(result)


def phase_moments(coefficients,width,theta_order=2):
    frequencies = 4*np.arange(1,coefficients.shape[1]+1)
    weights = []
    for n in frequencies:
        arg = exact_iv(width)*int(n)
        weights.append(endpoint_up((interval_exp(arg)+interval_exp(-arg))/2))
    result = np.zeros((len(coefficients),theta_order+1))
    for j,row in enumerate(coefficients):
        for k in range(theta_order+1):
            result[j,k] = weighted_sum_up(row,mul_up(weights,frequencies**k))
    return result


def bell_majorant(derivatives):
    """Mixed derivatives of exp(f)/exp(f), in absolute-value majorants."""
    rx,st = np.array(derivatives.shape)-1
    result = np.zeros_like(derivatives);result[0,0]=1.
    for s in range(1,st+1):
        result[0,s] = positive_sum(product(math.comb(s-1,k-1),derivatives[0,k],result[0,s-k])
                                  for k in range(1,s+1))
    for r in range(1,rx+1):
        for s in range(st+1):
            result[r,s] = positive_sum(product(math.comb(r-1,i),math.comb(s,j),
                derivatives[i+1,j],result[r-1-i,s-j])
                for i in range(r) for j in range(s+1))
    return result


def tangent_majorants(beta,gamma,theta_width):
    total = add_up(beta,gamma)
    total[0,1] = add_up(total[0,1],1.) # theta in phi=theta+pi/2+beta.
    horizontal = product(2.,exp_up(add_up(theta_width,add_up(beta[0,0],gamma[0,0]))))
    vertical = exp_up(gamma[0,0])
    return add_up(mul_up(horizontal,bell_majorant(total)),mul_up(vertical,bell_majorant(gamma)))


def real_tangent_majorants(beta,gamma):
    # Every real mixed phase partial of the spherical unit-vector map has
    # Euclidean norm <=1. The same positive Bell polynomial therefore
    # bounds real jets without the complex exponential prefactors.
    total = add_up(beta,gamma);total[0,1]=add_up(total[0,1],1.)
    return bell_majorant(total)


def position_majorants(radius,height,tangent):
    p = up(11/7) # pi/2 < 11/7, valid also on each translated complex circle.
    result = []
    for r in range(len(radius)):
        result.append(add_up(height[r],positive_sum(product(math.comb(r,j),radius[j],p,tangent[r-j,0])
                                                     for j in range(r+1))))
    return np.asarray(result)


def square_root_upper(value):
    candidate = math.sqrt(float(value));exact = Fraction.from_float(float(value))
    while Fraction.from_float(candidate)**2 < exact:
        candidate = math.nextafter(candidate,math.inf)
    return candidate


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--root-certificate',type=Path,required=True)
    ap.add_argument('--scalar-certificate',type=Path,required=True)
    ap.add_argument('--core-certificate',type=Path,required=True)
    ap.add_argument('--radial-width',type=float,default=1e-6)
    ap.add_argument('--angular-width',type=float,default=1e-4)
    ap.add_argument('--out',type=Path,required=True)
    args = ap.parse_args()
    sx,st = args.radial_width,args.angular_width
    if not 0 < sx < .01 or not 0 < st < .1:
        raise ValueError('positive modest local complex widths required')
    with np.load(args.inputs,allow_pickle=False) as saved:
        frozen={key:saved[key].copy() for key in saved.files}
    root=json.loads(args.root_certificate.read_text())
    scalar=json.loads(args.scalar_certificate.read_text())
    core=json.loads(args.core_certificate.read_text())
    sha=hashlib.sha256(args.inputs.read_bytes()).hexdigest()
    if not (root['inputs_sha256']==scalar['inputs_sha256']==core['configuration']['inputs_sha256']==sha):
        raise ValueError('all real certificates must describe these same scalar inputs')
    if not root['sign_and_simple_root_gate'] or not scalar['gate_passed'] or not core['complete']:
        raise ValueError('complete real gates required')
    if scalar['radial_core'] != core['radial_core']:
        raise ValueError('scalar and geometric real core coverage must match')
    collar=root['optional_collar_evaluation']
    if collar is None: raise ValueError('a certified real root collar is required')
    left,right=collar['x']
    root_left,root_right=root['isolating_interval']
    if not left <= root_left <= root_right <= right:
        raise ValueError('the real collar must contain the certified exact root')
    cell=root['common_spline_cell']
    if not cell[0] < left < right < cell[1]: raise ValueError('collar must stay inside one common span')
    if not 0 < left < right < core['radial_core'][1]: raise ValueError('collar outside the real geometry proof')
    target=CoreTarget(frozen,256,512)
    beta,gamma,aa,zz=physical_polynomial_jets(target,Box(left,right))
    bc,gc=imaginary_taylor(beta,sx),imaginary_taylor(gamma,sx)
    ac,zc=imaginary_taylor(aa,sx),imaginary_taylor(zz,sx)
    bcomplex,gcomplex=phase_moments(bc,st),phase_moments(gc,st)
    breal,greal=phase_moments(beta.abs_upper()[:6],0.),phase_moments(gamma.abs_upper()[:6],0.)
    tc=tangent_majorants(bcomplex,gcomplex,st)
    tr=real_tangent_majorants(breal,greal)
    ar,zr=aa.abs_upper(),zz.abs_upper()[:6]
    fc=position_majorants(ac,zc,tc)
    fr=position_majorants(ar,zr,tr)
    fr[0]=min(fr[0],max(row['F_norm_upper'] for row in core['cells']))
    fr[1]=min(fr[1],max(row['Fx_norm_upper'] for row in core['cells']))
    ftheta=np.asarray([positive_sum(product(math.comb(r,j),ac[j],tc[r-j,0])
                                      for j in range(r+1)) for r in range(6)])
    # Move first vertically in x, then vertically in theta; all derivative
    # majorants cover the entire closed product domain.
    tf=tc.copy()
    for r in range(5):
        for s in range(2):
            tf[r,s]=min(tc[r,s],positive_sum([tr[r,s],mul_up(sx,tc[r+1,s]),mul_up(st,tc[r,s+1])]))
    ff=fc.copy()
    for r in range(5):
        ff[r]=min(fc[r],positive_sum([fr[r],mul_up(sx,fc[r+1]),mul_up(st,ftheta[r])]))
    F,X,X2,X3,X4=ff[:5]
    T,Tx,Tt,Txt,Ttt=tf[0,0],tf[1,0],tf[0,1],tf[1,1],tf[0,2]
    a,ap=ac[:2]
    W=mul_up(T,X)
    Wx=add_up(mul_up(Tx,X),mul_up(T,X2))
    Wt=add_up(mul_up(Tt,X),product(a,T,Tx))
    Nx=add_up(product(2,a,ap,X,T,Tt),product(a,a,
        positive_sum([product(X2,T,Tt),product(X,Tx,Tt),product(X,T,Txt)])))
    Nt=product(a,a,T,add_up(product(a,Tx,Tt),mul_up(X,Ttt)))
    A2x=add_up(product(2,a,ap,W,W),product(2,a,a,W,Wx))
    A2t=product(2,a,a,W,Wt)
    H2x,H2t=product(2,F,X),product(2,F,a,T)
    Jx=add_up(product(ap,F,W),product(a,F,Wx)) # X dot (T cross X)=0.
    Jt=product(a,F,Wt)
    Zx,Zt=X,product(a,exp_up(gcomplex[0,0]))
    derivatives={'Nraw':(Nx,Nt),'area_squared':(A2x,A2t),'F_squared':(H2x,H2t),
                 'J':(Jx,Jt),'Fz':(Zx,Zt)}
    losses={key:float(add_up(mul_up(sx,x),mul_up(st,t))) for key,(x,t) in derivatives.items()}
    hmin=core['support_lower'];amin=scalar['area_lower']
    real_lower={'minus_Nraw':-core['raw_N_upper'],
        'area_squared':float(down(amin*amin)),
        'F_squared':float(down(hmin*hmin)),
        'J':float(down(hmin*amin)),
        'Fz':float(down(scalar['Fz_over_x_lower']*left))}
    lower={key:float(down(value-losses['Nraw' if key=='minus_Nraw' else key]))
           for key,value in real_lower.items()}
    E1=product(2,X,X2)
    E_loss=float(mul_up(sx,E1))
    Eabs_upper=float(up(collar['E'][1]+E_loss))
    Eabs_lower=float(down(collar['E'][0]-E_loss))
    a_loss=float(mul_up(sx,ap))
    a_abs_upper=float(up(collar['a'][1]+a_loss))
    a_abs_lower=float(down(collar['a'][0]-a_loss))
    E3=add_up(product(2,X,X4),product(6,X2,X3))
    Csecond=positive_sum([mul_up(ac[1],E3),product(3,ac[3],E1),product(2,ac[4],Eabs_upper)])
    Cprime_loss=float(mul_up(sx,Csecond))
    Cprime_lower=float(down(collar['Cprime'][0]-Cprime_loss))
    Cprime_abs_upper=float(up(max(abs(v) for v in collar['Cprime'])+Cprime_loss))
    lower.update(a=a_abs_lower,E=Eabs_lower,real_part_Cprime=Cprime_lower)
    gate=all(value>0 for value in lower.values())
    quantities={}
    if gate:
        kappalow=float((Box(Cprime_lower)/(2*Box(a_abs_upper)*Eabs_upper*Eabs_upper)).lo)
        kappahigh=float((Box(Cprime_abs_upper)/(2*Box(a_abs_lower)*Eabs_lower*Eabs_lower)).hi)
        area_real_upper=max(row['area_upper'] for row in core['cells'])
        position_real_upper=max(row['F_norm_upper'] for row in core['cells'])
        A2upper=float(add_up(mul_up(area_real_upper,area_real_upper),losses['area_squared']))
        H2upper=float(add_up(mul_up(position_real_upper,position_real_upper),losses['F_squared']))
        zeta_denominator=square_root_upper(float(mul_up(A2upper,H2upper)))
        zetalow=float((Box(lower['J'])/zeta_denominator).lo)
        ellupper=float((Box(Zt)/lower['Fz']+Box(product(F,a,T))/lower['F_squared']).hi)
        quantities=dict(kappa_modulus_lower=kappalow,kappa_modulus_upper=kappahigh,
            zeta_modulus_lower=zetalow,ell_modulus_upper=ellupper,
            area_squared_modulus_upper=A2upper,F_squared_modulus_upper=H2upper)
    report=dict(kind='local_complex_radial_angular_denominator_gate_for_exact_symmetric_infinite_R33_root',
        inputs_sha256=sha,source_checkpoint_sha256=core['source_checkpoint_sha256'],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        certificates_sha256={str(path):hashlib.sha256(path.read_bytes()).hexdigest()
            for path in [args.root_certificate,args.scalar_certificate,args.core_certificate]},
        dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['fourfold_phase_core_interval.py','fourfold_phase_root_interval.py',
                         'fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        real_radial_collar=[left,right],common_real_polynomial_span=cell,
        imaginary_radial_width=sx,imaginary_angular_width=st,
        all_real_angles=True,gate_passed=gate,
        positive_real_part_lower=lower,real_baseline_lower=real_lower,
        complex_displacement_allowances=losses,
        complex_derivative_majorants={key:list(map(float,value)) for key,value in derivatives.items()},
        E_radial_derivative_upper=float(E1),E_displacement_allowance=E_loss,
        Csecond_modulus_upper=float(Csecond),Cprime_displacement_allowance=Cprime_loss,
        radius_complex_jet_majorants=ac.tolist(),height_complex_jet_majorants=zc.tolist(),
        phase_beta_complex_mixed_majorants=bcomplex.tolist(),phase_gamma_complex_mixed_majorants=gcomplex.tolist(),
        tangent_complex_mixed_majorants=tf.tolist(),position_complex_radial_majorants=ff.tolist(),
        **quantities,
        analytic_definitions='Bilinear dot products in complex variables; A²=a²(T cross Fx) dot (T cross Fx); H²=F dot F; J=a F dot (T cross Fx); zeta=J/(sqrt(A²) sqrt(H²)), each square root is the principal branch on the proved right half-plane',
        kappa_identity='K0(z)/(z-t) = integral_0^1 Cprime(t+s(z-t)) ds / (2 a(z) E(z)^2); t is the already certified exact real root',
        limitations=['Only this root collar and its exact radial reflection, not the entire piecewise-polynomial core, is complexified in x',
            'No parameter tube, canonical coordinate univalence, beta coefficient enclosure, or PDE inverse is asserted',
            'The complete infinite primitive is bounded directly; there is no uncharged finite FFT remainder'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)
    if not gate: raise SystemExit('complex gate failed; inspect explicit losses or decrease a stated width')


if __name__=='__main__':main()
