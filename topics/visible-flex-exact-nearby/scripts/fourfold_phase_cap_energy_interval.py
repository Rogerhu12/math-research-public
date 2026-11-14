#!/usr/bin/env python3
"""True native positive-cap trial/flux energy on a closed scalar span.

The trial functions are the exact binary coefficients saved by the finite
space runner, not asserted solutions. Infinite primitive errors, complete
angular trapezoidal aliases, and the full radial Gauss tail are paid. The
radial analytic extension is that of the selected common scalar germ only.
This initial entry certifies listed body intervals; it does not certify an
entire cap merely because one interval passes.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from flint import arb, acb, ctx

from fourfold_phase_beta_affine import AffineFastBulkTarget
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_bulk_box import (CBox, Box, cstack, complex_sincos,
    arb_box, reduce_box, zeros)
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_positive_family_outer import StablePositiveFamily
from fourfold_phase_actual_positive_cap import complex_separation
from fourfold_phase_core_low_coefficients import extend_half
from fourfold_phase_cap_moment_space import shapes


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def conjugate(z):
    return CBox(z.real, -z.imag)


def matrix_product(a, b):
    return (a.reshape(a.real.lo.shape[0], a.real.lo.shape[1], 1)
            *b.reshape(1, b.real.lo.shape[0], b.real.lo.shape[1])).sum(1)


def constant_array(values):
    values = np.asarray(values, dtype=complex)
    return CBox(Box(values.real), Box(values.imag))


def norm_upper(matrix):
    values = matrix.magnitude_upper()
    total = arb(0)
    for value in values.ravel():
        total += arb(float(value))**2
    return total.sqrt().upper()


def complex_record(value):
    return dict(real=ball_record(value.real), imag=ball_record(value.imag))


def hermitian_midpoint(matrix):
    lo, hi = matrix.real.lo, matrix.real.hi
    ilo, ihi = matrix.imag.lo, matrix.imag.hi
    middle = (lo+hi)/2+1j*(ilo+ihi)/2
    middle = (middle+middle.conj().T)/2
    # This selected binary matrix is exact data. Its rounding is paid by the
    # following difference from the complete directed integral enclosure.
    difference = matrix-constant_array(middle)
    return middle, norm_upper(difference)


def polynomial(coefficients, x):
    value = CBox(0.)
    for coefficient in coefficients[::-1]:
        value = value*x+CBox(float(coefficient))
    return value


def gauss_rule(degree):
    """Legendre roots certified by signs and interval Newton, true weights."""
    p0, p1 = [Fraction(1)], [Fraction(0), Fraction(1)]
    if degree == 0:
        raise ValueError('a positive Gauss order is required')
    for n in range(1, degree):
        shifted = [Fraction(0)]+p1
        old = p0+[Fraction(0)]*(len(shifted)-len(p0))
        p0, p1 = p1, [((2*n+1)*a-n*b)/(n+1) for a,b in zip(shifted,old)]
    coefficients = [exact_arb(x) for x in p1]
    derivative = [j*coefficients[j] for j in range(1,len(coefficients))]
    def evaluate(poly,x):
        result = arb(0)
        for c in poly[::-1]:
            result = result*x+c
        return result
    nodes, weights = [], []
    seeds, _ = leggauss(degree)
    for seed in seeds:
        root = arb(float(seed))+arb(0,arb(2)**-40)
        if not evaluate(coefficients,root.lower())*evaluate(coefficients,root.upper()) < 0:
            raise ValueError('the proposed Gauss root bracket lacks a sign change')
        if evaluate(derivative,root).contains(0):
            raise ValueError('the proposed Gauss root is not simple on its bracket')
        for _ in range(6):
            root = root.intersection(root.mid()-evaluate(coefficients,root.mid())/evaluate(derivative,root))
        if nodes and not nodes[-1].upper() < root.lower():
            raise ValueError('Gauss root intervals are not disjoint')
        weight = 2/((1-root*root)*evaluate(derivative,root)**2)
        if not weight > 0:
            raise ValueError('the actual Gauss weight is not positive')
        nodes.append(root);weights.append(weight)
    if not sum(weights,arb(0)).contains(2):
        raise ValueError('the true Gauss weights do not enclose their constant moment')
    return nodes, weights


class BodyForm(AffineFastBulkTarget):
    finite_data = StablePositiveFamily.finite_data
    tail_errors = StablePositiveFamily.tail_errors
    complete_fast_data = StablePositiveFamily.complete_fast_data

    def form_parts(self, radial, sigma=None):
        coefficient,K,_,errors,real = self.complete_fast_data(radial)
        fields = self.fast_fields(radial,coefficient,errors,real,sigma)
        if real and (sigma is None or sigma == 0):
            fields = {key:CBox(value.real) for key,value in fields.items()}
        F, X = fields[0,0], fields[1,0]
        beta,gamma,_,_ = self.last_scalar
        ss,cc = (self.angle_sines,self.angle_cosines) if sigma is None else self.angle_shift_cache[sigma.str(35)]
        frequency = CBox((4*np.arange(1,self.modes+1)).reshape(-1,1))
        phase = lambda v,j:(v[j].reshape(-1,1)*ss).sum()
        angular = lambda v:(v[0].reshape(-1,1)*frequency*cc).sum()
        b,g,br,gr,bt,gt = phase(beta,0),phase(gamma,0),phase(beta,1),phase(gamma,1),angular(beta),angular(gamma)
        sb,cb=complex_sincos(b);sg,cg=complex_sincos(g)
        h=-sb*X[:,0]+cb*X[:,1]
        v=-cb*X[:,0]-sb*X[:,1]
        Q=cg*X[:,2]-sg*h
        D=(1+bt)*cg*Q-gt*v
        M=br*cg*Q-gr*v
        W=Q*Q+v*v
        fh=-sb*F[:,0]+cb*F[:,1]
        fv=-cb*F[:,0]-sb*F[:,1]
        fq=cg*F[:,2]-sg*fh
        H=fq*v-fv*Q
        return dict(D=D,M=M,W=W,H=H,Z=F[:,2],K=K,primitive_errors=errors,real=real)

    def form_values(self, radial):
        p=self.form_parts(radial)
        D,M,W,H,Z,K=[p[key] for key in ('D','M','W','H','Z','K')]
        iH,iD,iZ,iW,iK=1/H,1/D,1/Z,1/W,1/K
        alpha=Z*Z*D*iH*iH
        drift=-M*iD
        kappa=Z*Z*W*W*K*iD*iH*iH
        inverse_alpha=H*H*iZ*iZ*iD
        inverse_kappa=D*H*H*iZ*iZ*iW*iW*iK
        values=[alpha,alpha*drift,alpha*drift*drift+kappa,
                inverse_alpha+drift*drift*inverse_kappa,-drift*inverse_kappa,inverse_kappa]
        if any(not np.all(np.isfinite(value.magnitude_upper())) for value in values):
            raise ValueError('a genuine body form or inverse denominator meets zero in its box')
        if p['real']:
            if not min(float(np.min(alpha.real.lo)),float(np.min(kappa.real.lo))) > 0:
                raise ValueError('the actual real grounded form did not retain positivity')
            values=[CBox(value.real) for value in values]
        return values

    def coefficient_strip_moduli(self, left, right, sigma):
        p=self.form_parts(acb(real_interval(left,right)),sigma)
        D,M,W,H,Z,K=[p[key] for key in ('D','M','W','H','Z','K')]
        upper=lambda value:arb(float(np.max(value.magnitude_upper())))
        dl,wl,hl,zl=[complex_separation(value,name) for value,name in
                     ((D,'D'),(W,'W'),(H,'H'),(Z,'Fz'))]
        klo=arb(float(np.min(K.real.lo)))
        if not klo>0:
            raise ValueError('angular inverse-form strip needs the true positive radial curvature')
        du,mu,wu,hu,zu,ku=map(upper,(D,M,W,H,Z,K))
        a=zu*zu*du/(hl*hl);v=mu/dl
        k=zu*zu*wu*wu*ku/(dl*hl*hl)
        ia=hu*hu/(zl*zl*dl)
        ik=du*hu*hu/(zl*zl*wl*wl*klo)
        return [x.upper() for x in (a,a*v,a*v*v+k,ia+v*v*ik,v*ik,ik)]


class FiniteTrial:
    def __init__(self,path):
        self.report=json.loads(Path(path).read_text())
        binary=Path(self.report['arrays']['path'])
        if not self.report['complete'] or sha(binary)!=self.report['arrays']['sha256']:
            raise ValueError('the completed finite primal/dual trial arrays changed')
        with np.load(binary,allow_pickle=False) as saved:
            self.mesh=saved['mesh'].copy();self.frequency=saved['frequencies'].copy()
            self.V=saved['primal_trial'].copy();self.flux=saved['dual_flux'].copy()
        self.M=self.report['interior_modes'];self.B=self.report['boundary_modes']
        self.degree=self.report['radial_polynomial_degree'];self.basis=shapes(self.degree)
        self.n=len(self.frequency);self.d=2*self.B+2
        self.cells=len(self.mesh)-1;self.nodes=self.degree*self.cells+1
        self.nonzero=np.flatnonzero(self.frequency);self.nn=len(self.nonzero)
        if self.V.shape!=(self.nodes*self.n,self.d):
            raise ValueError('wrong exact finite primal trial shape')
        if self.flux.shape!=(self.nodes*self.nn+1+self.degree*self.cells,self.d):
            raise ValueError('wrong exact finite flux trial shape')
        self.cache=json.loads(Path(self.report['cache_report_path']).read_text())
        if sha(self.report['cache_report_path'])!=self.report['cache_report_sha256']:
            raise ValueError('the saved finite trial changed its moment input')
        self.object_path=Path(self.cache['object_path'])
        if sha(self.object_path)!=self.report['object_sha256']:
            raise ValueError('the finite trial and actual graph differ')

    def coefficients(self,element,radial):
        left,right=map(lambda x:Fraction(float(x)),self.mesh[element:element+2])
        h=exact_arb(right-left)
        t=(CBox.from_acb(radial)-CBox.from_acb(acb(exact_arb(left))))/CBox.from_acb(acb(h))
        U,R,P,Q=[zeros((self.n,self.d)) for _ in range(4)]
        for local,poly in enumerate(self.basis):
            basis=polynomial(poly.coef,t)
            derivative=polynomial(poly.deriv().coef,t)/CBox.from_acb(acb(h))
            nodal=constant_array(self.V[(element*self.degree+local)*self.n:
                                       (element*self.degree+local+1)*self.n])
            U+=basis*nodal;R+=derivative*nodal
            part=constant_array(self.flux[(element*self.degree+local)*self.nn:
                                          (element*self.degree+local+1)*self.nn])
            P[self.nonzero]=P[self.nonzero]+basis*part
            Q[self.nonzero]=Q[self.nonzero]-derivative*part/CBox(0.,Box(self.frequency[self.nonzero,None]))
        pmean=self.nodes*self.nn
        P[self.M]=constant_array(self.flux[pmean])
        power=CBox(1.)
        for j in range(self.degree):
            Q[self.M]=Q[self.M]+power*constant_array(self.flux[pmean+1+element*self.degree+j])
            power*=t
        T=U*CBox(0.,Box(self.frequency[:,None]))
        return R,T,P,Q

    @staticmethod
    def coefficient_l1_columns(value):
        # The Euclidean norm in the finite input columns, after l1 angular
        # summation, bounds the Frobenius norm at every real physical angle.
        sums=reduce_box(Box(value.magnitude_upper()),0)
        return sum((arb(float(x))**2 for x in sums.hi.ravel()),arb(0)).sqrt().upper()


def sampled_energy(target,trial,element,radial):
    values=target.form_values(radial)
    full=cstack([extend_half(value,-1 if j in (1,4) else 1) for j,value in enumerate(values)],1)
    transformed=target.fast_fourier.fft(full)/target.angles
    modes=np.arange(-trial.M,trial.M+1)
    lag=(modes[:,None]-modes[None,:])%target.angles
    matrices=[transformed[lag,j] for j in range(6)]
    R,T,P,Q=trial.coefficients(element,radial)
    answer=[]
    for A,B,C,X,Y in ((matrices[0],matrices[1],matrices[2],R,T),
                       (matrices[3],matrices[4],matrices[5],P,Q)):
        left=matrix_product(A,X)+matrix_product(B,Y)
        right=matrix_product(B,X)+matrix_product(C,Y)
        answer.append(matrix_product(conjugate(X).transpose(1,0),left)
                      +matrix_product(conjugate(Y).transpose(1,0),right))
    return answer


def analytic_radial_moduli(target,trial,element,center,radius):
    radial=acb(center+arb(0,radius),arb(0,radius))
    values=target.form_values(radial)
    bounds=[arb(float(np.max(value.magnitude_upper()))) for value in values]
    columns=list(map(trial.coefficient_l1_columns,trial.coefficients(element,radial)))
    result=[]
    for offset,(x,y) in zip((0,3),(columns[:2],columns[2:])):
        # The coefficient-conjugated radial polynomials have the same bound
        # on this conjugation-symmetric disk. This is an analytic energy
        # extension, not conjugation of the complex radial argument.
        result.append((bounds[offset]*x*x+2*bounds[offset+1]*x*y+bounds[offset+2]*y*y).upper())
    return result


def angular_alias_fees(target,trial,element,left,right,sigma):
    moduli=target.coefficient_strip_moduli(left,right,sigma)
    lag=2*trial.M
    factor=((-(target.angles-lag)*sigma).exp()+(-(target.angles+lag)*sigma).exp())/(1-(-target.angles*sigma).exp())
    coefficients=trial.coefficients(element,acb(real_interval(left,right)))
    columns=list(map(trial.coefficient_l1_columns,coefficients))
    fees=[]
    for offset,(x,y) in zip((0,3),(columns[:2],columns[2:])):
        fees.append((factor*(moduli[offset]*x*x+2*moduli[offset+1]*x*y+moduli[offset+2]*y*y)).upper())
    return fees,moduli


def certify_interval(target,trial,element,left,right,nodes,weights,radius_factor,sigma):
    left,right=Fraction(left),Fraction(right)
    center=exact_arb((left+right)/2);h=exact_arb((right-left)/2)
    outer=radius_factor*h
    if not radius_factor>1:
        raise ValueError('Gauss tail needs a strictly larger analytic radial disk')
    radial_moduli=analytic_radial_moduli(target,trial,element,center,outer)
    aliases,angular_moduli=angular_alias_fees(target,trial,element,left,right,sigma)
    integrals=[zeros((trial.d,trial.d)),zeros((trial.d,trial.d))]
    for node,weight in zip(nodes,weights):
        values=sampled_energy(target,trial,element,acb(center+h*node))
        for j,value in enumerate(values):
            integrals[j]+=value*CBox.from_acb(acb(h*weight))
    ratio=1/radius_factor
    # True Gaussian quadrature integrates all radial polynomials through
    # degree 2n-1. Integral and positive-weight quadrature each pay the full
    # analytic tail; no fitted finite tail replaces the infinite one.
    gauss=[(4*h*M*ratio**(2*len(nodes))/(1-ratio)).upper() for M in radial_moduli]
    alias=[(2*h*fee).upper() for fee in aliases]
    results=[]
    for j,value in enumerate(integrals):
        middle,roundoff=hermitian_midpoint(value)
        results.append(dict(matrix_middle=[[[float(z.real),float(z.imag)] for z in row] for row in middle],
            full_operator_error=ball_record((roundoff+gauss[j]+alias[j]).upper()),
            directed_node_and_weight_error=ball_record(roundoff),
            radial_Gauss_full_tail=ball_record(gauss[j]),
            complete_angular_alias=ball_record(alias[j]),
            analytic_radial_matrix_modulus=ball_record(radial_moduli[j])))
    return dict(exact_radial_interval=[str(left),str(right)],finite_element=element,
        normalized_angular_strip=str(Fraction(str(sigma.fmpq()))) if sigma.is_exact() else sigma.str(35),
        radial_outer_factor=ball_record(radius_factor),
        true_form_Fourier_strip_moduli=list(map(ball_record,angular_moduli)),
        primal_energy=results[0],dual_energy=results[1])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    parser.add_argument('--element',type=int,default=0)
    parser.add_argument('--span',type=int,default=0)
    parser.add_argument('--angles',type=int,default=1024)
    parser.add_argument('--primitive-nodes',type=int,default=512)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--gauss-order',type=int,default=8)
    parser.add_argument('--max-depth',type=int,default=6)
    parser.add_argument('--radial-factor',type=Fraction,default=Fraction(4))
    parser.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,32))
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();ctx.prec,ctx.cap=args.bits,4
    trial=FiniteTrial(args.trial)
    target=BodyForm(trial.object_path,args.primitive_nodes,args.angles,arb('.003'),arb('.0025'),arb('.32'))
    left,right=map(lambda x:Fraction(float(x)),trial.mesh[args.element:args.element+2])
    if not Fraction(1,4)<=left<right<=3:
        raise ValueError('this entry certifies actual body cells; natural graft is a separate analytic object')
    allcuts={Fraction(0),Fraction(3)}
    for key,values in target.frozen.items():
        if key.endswith('_knots'):
            for x in values:
                q=Fraction(float(x))
                allcuts.update((q,-q))
    cuts=sorted({left,right}|{q for q in allcuts if left<q<right})
    a,b=cuts[args.span:args.span+2]
    common=sorted(allcuts);k=bisect_right(common,(a+b)/2)-1
    target.set_cell(common[k],common[k+1])
    nodes,weights=gauss_rule(args.gauss_order)
    wall,cpu=time.monotonic(),time.process_time()
    rows,failures,subdivisions=[],[],[]
    pending=[(a,b,0)]
    while pending:
        left,right,depth=pending.pop()
        try:
            row=certify_interval(target,trial,args.element,left,right,nodes,weights,
                                 exact_arb(args.radial_factor),exact_arb(args.normalized_strip))
            row['subdivision_depth']=depth
            rows.append(row)
            print(json.dumps(dict(accepted=row['exact_radial_interval'],depth=depth,
                primal_error=row['primal_energy']['full_operator_error']['ball'],
                dual_error=row['dual_energy']['full_operator_error']['ball'])),flush=True)
        except (ValueError,ZeroDivisionError) as exc:
            record=dict(exact_radial_interval=[str(left),str(right)],depth=depth,reason=str(exc))
            if depth==args.max_depth:
                failures.append(record)
            else:
                subdivisions.append(record)
                midpoint=(left+right)/2
                pending.extend([(midpoint,right,depth+1),(left,midpoint,depth+1)])
    rows.sort(key=lambda row:Fraction(row['exact_radial_interval'][0]))
    cursor=a
    for row in rows:
        left,right=map(Fraction,row['exact_radial_interval'])
        if left!=cursor:
            break
        cursor=right
    complete=not failures and cursor==b
    report=dict(kind='true_native_closed_body_interval_cap_trial_energy_matrices',complete=complete,
        full_positive_cap_complete=False,source_sha256=sha(__file__),
        trial_report_path=str(args.trial),trial_report_sha256=sha(args.trial),
        object_sha256=trial.report['object_sha256'],exact_delta_fraction=trial.report['exact_delta_fraction'],
        modes=dict(boundary=trial.B,interior=trial.M),radial_trial_degree=trial.degree,
        primitive_nodes=args.primitive_nodes,angular_nodes=args.angles,bits=args.bits,
        gauss_order=args.gauss_order,gauss_nodes=list(map(ball_record,nodes)),
        gauss_weights=list(map(ball_record,weights)),selected_true_common_span=list(map(str,target.cell)),
        requested_exact_radial_interval=[str(a),str(b)],intervals=rows,
        rejected_parent_boxes=subdivisions,unresolved_intervals=failures,
        CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_positive_family_outer.py','fourfold_phase_cap_moment_space.py',
            'fourfold_phase_core_low_coefficients.py')},
        scope='Only this explicitly listed common body span is paid. Infinite primitive, finite quadrature node/weight uncertainty, full analytic Gauss tail and full angular Fourier aliases are included; a whole cap inverse is not asserted.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(complete=complete,covered_intervals=len(rows),failures=failures,
        CPU_seconds=report['CPU_seconds'],wall_seconds=report['wall_seconds']),indent=2),flush=True)
    if not complete:
        raise SystemExit('the requested actual body span has not been fully certified')


if __name__=='__main__':
    main()
