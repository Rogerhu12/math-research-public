#!/usr/bin/env python3
"""Actual single-turn positive component for one exact affine R33 graph.

The physical radial coordinate is kept unchanged.  The real angular flow
Theta_x=-mraw/nraw removes the cross term of Yz^2 Ahat.  Complete closed
scalar spans, all angular gaps, and the infinite primitive are included.
This certifies a finite root-to-regular-cut component, not an exterior flat
tail or a fixed open holding region.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_affine import AffineFastBulkTarget, sha, provenance
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_bulk_box import CBox, cstack, cdot, ccross, complex_sincos
from fourfold_phase_beta_interval import ball_record


def rotation(v):
    return cstack([-v[:, 1], v[:, 0], CBox(np.zeros(v.real.lo.shape[0]))], -1)


def cmod_upper(v):
    return arb(float(np.max(v.magnitude_upper())))


def real_range(v):
    # This function is only called for the mathematically real r/theta
    # formulas.  A directed complex reciprocal can leave subnormal imaginary
    # rounding intervals about zero; intersection with the real axis is valid.
    if np.any(v.imag.lo>0) or np.any(v.imag.hi<0):
        raise ValueError('a real cap quantity lost real structure')
    return [float(np.min(v.real.lo)), float(np.max(v.real.hi))]


def positive_real_range(v, name):
    value = real_range(v)
    if not value[0] > 0:
        raise ValueError(name+' has no positive continuous lower bound')
    return value


def complex_separation(v, name):
    lower = []
    for index in np.ndindex(v.real.lo.shape):
        box = acb(arb(float(v.real.lo[index])).union(arb(float(v.real.hi[index]))),
                  arb(float(v.imag.lo[index])).union(arb(float(v.imag.hi[index]))))
        lower.append(box.abs_lower())
    result = min(lower)
    if not result > 0:
        raise ValueError(name+' vanishes in the paid complex rectangle')
    return result


class PositiveCapTarget(AffineFastBulkTarget):
    def geometry(self, radial, coefficient, errors, sigma):
        fields = self.fast_fields(radial, coefficient, errors, True, sigma=sigma)
        if sigma == 0:
            fields = {key:CBox(value.real) for key,value in fields.items()}
        beta, gamma, radius, _ = self.last_scalar
        ss, cc = self.angle_shift_cache[sigma.str(35)]
        frequency = CBox((4*np.arange(1, self.modes+1)).reshape(-1, 1))
        def phase(values, radial_order=0, angular_order=0):
            v = values[radial_order].reshape(-1, 1)
            if angular_order == 0:
                return (v*ss).sum()
            if angular_order == 1:
                return (v*frequency*cc).sum()
            if angular_order == 2:
                return -(v*frequency*frequency*ss).sum()
            raise ValueError('unsupported phase derivative')
        b,g,br,gr,bt,gt,btt,gtt,brt,grt = [
            phase(v,r,t) for v,r,t in ((beta,0,0),(gamma,0,0),
                (beta,1,0),(gamma,1,0),(beta,0,1),(gamma,0,1),
                (beta,0,2),(gamma,0,2),(beta,1,1),(gamma,1,1))]
        sb,cb = complex_sincos(b);sg,cg = complex_sincos(g)
        aa, ar = radius[0], radius[1]
        F, X = fields[(0,0)], fields[(1,0)]
        # Exact orthonormal moving-frame identities.  Keeping these scalar
        # combinations avoids re-expanding a determinant into wide boxes.
        h = -sb*X[:,0]+cb*X[:,1]
        v = -cb*X[:,0]-sb*X[:,1]
        Q,R = cg*X[:,2]-sg*h,cg*h+sg*X[:,2]
        P=1+bt
        Q1=aa*gr-P*sg*v-gt*R
        v1=aa*cg*br-P*h
        D,M,W=P*cg*Q-gt*v,br*cg*Q-gr*v,Q*Q+v*v
        D1=btt*cg*Q-P*sg*gt*Q+P*cg*Q1-gtt*v-gt*v1
        M1=brt*cg*Q-br*sg*gt*Q+br*cg*Q1-grt*v-gr*v1
        fh=-sb*F[:,0]+cb*F[:,1]
        fv=-cb*F[:,0]-sb*F[:,1]
        fq=cg*F[:,2]-sg*fh
        H=fq*v-fv*Q
        area,norm,support=aa*aa*W,cdot(F,F),aa*H
        n=-aa*aa*D
        height = F[:,2]
        if sigma != 0:
            dl=complex_separation(D,'D')
            hl=complex_separation(H,'H')
            separations = {key:ball_record(complex_separation(value,key)) for key,value in
                           [('support',support),('nraw',n),('norm2',norm)]}
            # Modulus inequalities avoid a second rectangular reciprocal
            # overestimate while retaining the same exact analytic formulas.
            alpha_bound=cmod_upper(height)**2*cmod_upper(D)/hl**2
            eta_bound=cmod_upper(height)**2*cmod_upper(W)**2/(dl*hl**2)
            derivative_bound=cmod_upper(M1)/dl+cmod_upper(M)*cmod_upper(D1)/dl**2
            return dict(separations=separations,
                alpha_modulus=ball_record(alpha_bound.upper()),
                eta_modulus=ball_record(eta_bound.upper()),
                drift_theta_modulus=ball_record(derivative_bound.upper()))
        drift=-M/D
        drift_theta=-(M1+drift*D1)/D
        iH,iD=1/H,1/D
        alpha=height*height*D*iH*iH
        eta=height*height*W*W*iD*iH*iH
        if sigma == 0:
            ranges = {key:positive_real_range(value,key) for key,value in
                [('area2',area),('norm2',norm),('support',support),
                 ('minus_nraw',-n),('Fz',height),('alpha',alpha),('eta',eta)]}
            ranges['drift'] = real_range(drift)
            ranges['drift_theta'] = real_range(drift_theta)
            Ylo = arb(ranges['Fz'][0])/arb(ranges['norm2'][1]).sqrt()
            Yhi = arb(ranges['Fz'][1])/arb(ranges['norm2'][0]).sqrt()
            ranges['Yz'] = [float(Ylo.lower()),float(Yhi.upper())]
            # The enclosing binary64 display must itself be outward.
            ranges['Yz'][0] = float(np.nextafter(ranges['Yz'][0],-np.inf))
            ranges['Yz'][1] = float(np.nextafter(ranges['Yz'][1],np.inf))
            return ranges

    def evaluate_cap(self,left,right,sigma,root_interval,monotone_cut):
        radial = acb(real_interval(left,right))
        coefficient,K,Kp,errors,real = self.complete_fast_data(radial)
        if not real:
            raise ValueError('this component uses real physical r')
        kp=real_range(Kp)
        if right<=monotone_cut:
            if not kp[0]>0:raise ValueError('target K radial derivative is not positive on the root collar')
            distance_bound=kp
            distance_kind='derivative on the initial collar; aggregate over the whole collar'
        elif left>=monotone_cut:
            if not real_range(K)[0]>0:raise ValueError('target K is not positive on the strict positive collar')
            distance=real_interval(left-root_interval[1],right-root_interval[0])
            ratio=K.to_acb().real/distance
            distance_bound=[float(np.nextafter(float(ratio.lower()),-np.inf)),
                            float(np.nextafter(float(ratio.upper()),np.inf))]
            distance_kind='direct true K divided by r minus the certified true root'
        else:raise ValueError('cell crosses the prescribed monotone-collar boundary')
        real_geometry = self.geometry(radial,coefficient,errors,arb(0))
        complex_geometry = self.geometry(radial,coefficient,errors,sigma)
        return dict(radial_interval=[str(left),str(right)],K=real_range(K),Kprime=kp,
            K_over_distance_input=distance_bound,K_over_distance_kind=distance_kind,
            real_geometry=real_geometry,complex_geometry=complex_geometry,
            primitive_errors=[ball_record(x) for x in errors])


def stored_upper(record):
    return arb(record['upper']).upper()


def aggregate(rows,root_interval,cut,sigma):
    lower,upper = map(exact_arb,root_interval)
    Llo,Lhi = exact_arb(cut)-upper,exact_arb(cut)-lower
    kmin = min(arb(row['K_over_distance_input'][0]) for row in rows)
    kmax = max(arb(row['K_over_distance_input'][1]) for row in rows)
    amin = min(arb(row['real_geometry']['alpha'][0]) for row in rows)
    amax = max(arb(row['real_geometry']['alpha'][1]) for row in rows)
    emin = min(arb(row['real_geometry']['eta'][0]) for row in rows)
    emax = max(arb(row['real_geometry']['eta'][1]) for row in rows)
    Vr = max(arb(max(abs(x) for x in row['real_geometry']['drift_theta'])) for row in rows)
    Vc = max(stored_upper(row['complex_geometry']['drift_theta_modulus']) for row in rows)
    ac = max(stored_upper(row['complex_geometry']['alpha_modulus']) for row in rows)
    ec = max(stored_upper(row['complex_geometry']['eta_modulus']) for row in rows)
    Jr,Jc = (Vr*Lhi).exp(),(Vc*Lhi).exp()
    m = min(amin,emin*kmin)/Jr
    M = max(amax,emax*kmax)*Jr
    # sigma is the normalized 4theta width.  Start with half the physical
    # strip, then pay the complete real-time angular-flow amplification.
    physical_strip = sigma/4
    flow_strip = physical_strip/(2*Jc)
    Ccomplex = max(ac,ec*kmax)*Jc
    elllo,ellhi = Llo/4,Lhi/4
    Ctr = max(2*ellhi+4/elllo+16/elllo**2,
              2*ellhi+4/elllo+32/(3*Llo*elllo))
    CE = max(1/elllo+ellhi/3+ellhi**2/12,
             1/elllo+ellhi/3+Lhi*ellhi/3)
    g = (1+Lhi**2/arb.pi()**2)/m
    poisson = CE.sqrt()*(1+M*g)
    DN = M*CE
    qrho = (-flow_strip/2).exp()
    gap = -(-flow_strip/2).expm1()
    NC = 2*Ccomplex*qrho/gap**2
    CL = CE*(1+2*g*(M+1))**2
    if not NC.is_finite() or not CL.is_finite() or not NC>0 or not CL>0:
        raise ValueError('nonfinite or nonpositive analytic coefficient budget')
    # Real shear zero in the actual ground-state flux frame, gamma=1.
    sigma_star = min(flow_strip/2,arb(1)/NC,1/(2*g*NC),1/(2*CL*NC))
    Ymin = min(arb(row['real_geometry']['Yz'][0]) for row in rows)
    Ymax = max(arb(row['real_geometry']['Yz'][1]) for row in rows)
    interior_gain=(1+max(arb(3),4/Llo**2)).sqrt()
    values = dict(length_lower=Llo,length_upper=Lhi,K_over_distance_lower=kmin,
        K_over_distance_upper=kmax,angular_drift_theta_real=Vr,
        angular_drift_theta_complex=Vc,J_upper=Jr,J_inverse_upper=Jr,
        m_lower=m,M_upper=M,trace_constant=Ctr,extension_constant=CE,
        dirichlet_inverse=g,poisson_and_full_source_contact=poisson,DN=DN,
        interior_two_thirds_gain=interior_gain,
        ordinary_source_to_full_contact=interior_gain*poisson,
        Yz_lower=Ymin,Yz_upper=Ymax,ordinary_physical_source_to_new_L2=Jr.sqrt()*Ymax,
        physical_coefficient_strip=physical_strip,flow_coefficient_strip=flow_strip,
        C_complex_modulus=Ccomplex,coefficient_first_Fourier_moment=NC,
        DN_weight_perturbation_constant=CL,positive_analytic_weight=sigma_star,
        weighted_Robin_inverse=arb(2),weighted_Cayley=arb(5))
    if not Llo>0 or not m>0 or not sigma_star>0:
        raise ValueError('actual aggregate gate failed')
    if any(not value.is_finite() for value in values.values()):
        raise ValueError('a nonfinite aggregate constant cannot be certified')
    return {key:ball_record(value) for key,value in values.items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,required=True)
    ap.add_argument('--root-certificate',type=Path,required=True)
    ap.add_argument('--cut',default='1/4')
    ap.add_argument('--normalized-strip',default='1/128')
    ap.add_argument('--quarter-nodes',type=int,default=256)
    ap.add_argument('--angles',type=int,default=512)
    ap.add_argument('--bits',type=int,default=160)
    ap.add_argument('--max-depth',type=int,default=12)
    ap.add_argument('--max-cell-width',default='1/4096')
    ap.add_argument('--max-attempts',type=int,default=1000)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=4
    started=time.monotonic()
    target=PositiveCapTarget(args.object,args.quarter_nodes,args.angles,
        arb('.003'),arb('.0025'),arb('.32'))
    root=json.loads(args.root_certificate.read_text())
    if (not root.get('proved') or Fraction(root['exact_delta_fraction'])!=target.affine_delta
        or root['origin_inputs_sha256']!=target.affine_definition['origin_inputs']['sha256']
        or root['frozen_direction_sha256']!=target.affine_definition['direction']['sha256']):
        raise ValueError('root certificate belongs to a different exact graph')
    roots=[Fraction.from_float(float(x)) for x in root['root_interval']]
    cut=Fraction(args.cut);sigma=exact_arb(Fraction(args.normalized_strip))
    if not 0<roots[0]<=roots[1]<cut<=3 or not sigma>0:
        raise ValueError('invalid physical cap interval or angle strip')
    monotone_cut=roots[1]+Fraction(1,4096)
    if not monotone_cut<cut:monotone_cut=cut
    knots={roots[0],cut,monotone_cut}
    for key,values in target.frozen.items():
        if key.endswith('_knots'):
            knots.update(q for q in (abs(Fraction.from_float(float(x))) for x in values) if roots[0]<q<cut)
    points=sorted(knots)
    initial=list(zip(points,points[1:]))
    width=Fraction(args.max_cell_width)
    if not width>0:raise ValueError('positive initial cell width required')
    queue=deque()
    for a,b in initial:
        count=max(1,-(-(b-a)//width))
        queue.extend((a+(b-a)*j/count,a+(b-a)*(j+1)/count,0) for j in range(count))
    rows=[];failures=[];attempts=0
    identity=provenance(target,args.object)
    identity.pop('dependency_sha256')
    report=dict(kind='actual_exact_affine_single_turn_positive_cap_and_full_DN',complete=False,
        **identity,root_certificate_sha256=sha(args.root_certificate),
        root_interval=list(map(str,roots)),physical_regular_cut=str(cut),
        monotone_root_collar_cut=str(monotone_cut),
        initial_original_spans=len(initial),normalized_angle_strip=str(Fraction(args.normalized_strip)),
        maximum_initial_cell_width=str(width),
        quarter_nodes=args.quarter_nodes,angular_boxes=args.angles,bits=args.bits,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_beta_affine.py','fourfold_phase_beta_interval.py',
             'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_bulk_box.py',
             'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        cells=rows,failed_cells=failures,
        scope=['The physical r coordinate is unchanged; only an actual angular flow is used.',
            'The operator is the R37 fixed-target determinant operator with its global ell ground state.',
            'Both full ports, every angular mode and the mean, and full ordinary source contact remain.',
            'No exterior flat tail, fixed H, full global inverse, or exact isometric family is asserted.'])
    report['source_sha256']=sha(__file__)
    def save():
        report['attempts']=attempts;report['pending']=[[str(a),str(b),d] for a,b,d in queue]
        report['elapsed_seconds']=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        temporary=args.out.with_suffix(args.out.suffix+'.tmp')
        temporary.write_text(json.dumps(report,indent=2)+'\n');temporary.replace(args.out)
    while queue and attempts<args.max_attempts:
        left,right,depth=queue.popleft();attempts+=1
        target.set_cell(left,right)
        try:
            row=target.evaluate_cap(left,right,sigma,roots,monotone_cut);rows.append(row)
            print(json.dumps(dict(attempt=attempts,accepted=len(rows),pending=len(queue),
                interval=[float(left),float(right)],Kprime=row['Kprime'],
                elapsed_seconds=time.monotonic()-started)),flush=True)
        except (ValueError,ZeroDivisionError) as exc:
            if depth<args.max_depth:
                mid=(left+right)/2
                queue.appendleft((mid,right,depth+1));queue.appendleft((left,mid,depth+1))
            else:
                failures.append(dict(interval=[str(left),str(right)],reason=str(exc)))
            print(json.dumps(dict(attempt=attempts,refinement=depth,reason=str(exc))),flush=True)
        save()
    rows.sort(key=lambda row:Fraction(row['radial_interval'][0]))
    cursor=roots[0]
    for row in rows:
        left,right=map(Fraction,row['radial_interval'])
        if left!=cursor:break
        cursor=right
    report['exact_radial_cover']=bool(cursor==cut and not queue and not failures)
    if report['exact_radial_cover']:
        report['operator_constants']=aggregate(rows,roots,cut,sigma)
        report['complete']=True
    save()
    print(json.dumps(dict(complete=report['complete'],accepted=len(rows),failed=len(failures),
        elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)
    if not report['complete']:raise SystemExit('actual positive cap is not yet completely certified')


if __name__=='__main__':main()
