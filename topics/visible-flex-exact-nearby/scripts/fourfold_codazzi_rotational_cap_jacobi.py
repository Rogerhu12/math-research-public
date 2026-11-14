#!/usr/bin/env python3
"""True fixed-target rotational cap and all-channel Codazzi Jacobi comparison.

The complete body primitive/alias tail and the actual natural graft are
retained. Positive scalar Riccati comparison runs backwards from the true
R74 regular line, including its exponentially small fee. Selected physical
modes are enclosed separately; an invariant interval covers every m in 4N.
This is a linear cap reference, not a nonlinear match for the waist branch.
"""
from __future__ import annotations
import argparse,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_metric_defect import MetricDefectTarget,record,save,sha
from fourfold_phase_cap_scaled_body import common_cells,magnitude
from fourfold_phase_beta_bulk_box import Box,CBox,arb_box,cdot,reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_natural_exterior_graft import NaturalGraft,real_coefficient
from fourfold_phase_beta_affine import load_definition


def real(x,name):
    z=x.to_acb() if hasattr(x,'to_acb') else acb(x)
    if not z.imag.contains(0):raise ValueError('real enclosure lost: '+name)
    return z.real


def box_from_record(x):return arb(x['lower']).lower().union(arb(x['upper']).upper())


class RotationalPositiveCap:
    def __init__(self,object_path,half_width,nodes):
        self.body=MetricDefectTarget(object_path,half_width,nodes)
        self.cuts=common_cells(self.body)
        self.graft=NaturalGraft(object_path,half_width,Fraction(1,8))

    def body_values(self,left,right):
        j=bisect_right(self.cuts,left)-1
        if left==3:j-=1
        gl,gr=self.cuts[j:j+2]
        if not gl<=left<=right<=gr:raise ValueError('body box crosses a true scalar germ')
        t=self.body;t.set_cell(gl,gr);radial=acb(real_interval(left,right))
        primitive,radius=t.unit_finite_data(radial);errors=t.unit_tail_errors(radial)
        L,Lp,H,Hp,ia=t.scalar_ratios(radial,radius)
        rev=(-np.arange(t.nodes))%t.nodes
        u=L*primitive[0]+primitive[1]
        ur=Lp*primitive[0]+L*primitive[1]+primitive[2]
        ebar=2*L*u[0,0]+cdot(u,u[rev]).sum()
        ebar_r=2*Lp*u[0,0]+2*L*ur[0,0]+2*cdot(u,ur[rev]).sum()
        eps=[arb_box(math.factorial(j)*errors[0]/t.tail_radius**j) for j in range(3)]
        La,Lpa=magnitude(L),magnitude(Lp)
        eu=La*eps[0]+eps[1];eur=Lpa*eps[0]+La*eps[1]+eps[2]
        Mu=Box(np.max(reduce_box(Box(u.magnitude_upper())).hi))
        Mur=Box(np.max(reduce_box(Box(ur.magnitude_upper())).hi))
        fee0=2*La*eu+3*(2*Mu*eu+eu*eu)
        fee1=2*Lpa*eu+2*La*eur+6*(Mu*eur+Mur*eu+eu*eur)
        ebar=ebar.pad(fee0,True);ebar_r=ebar_r.pad(fee1,True)
        aa=radius[0];Ebar=L*L+aa*aa*H*H+ebar
        R=H*H+ebar*ia*ia
        K=(H*H*(L*L-Lp)+L*H*Hp+(L*ebar_r-2*Lp*ebar)*ia*ia/2)/(Ebar*Ebar)
        values={name:real(value,name) for name,value in dict(a=aa,beta=L,Ebar=Ebar,R=R,K=K).items()}
        values['primitive_error_0']=arb(float(fee0.hi)).upper()
        values['primitive_error_1']=arb(float(fee1.hi)).upper()
        return values,(gl,gr),'body'

    def graft_values(self,left,right):
        if not Fraction(3)<=left<=right<=Fraction(25,8):raise ValueError('outside actual graft')
        jets=self.graft.jets(left-3,right-3);maj=self.graft.majorants(jets,arb(0))
        aa=real_coefficient(jets['radius'],0)
        L=real_coefficient(jets['log_radius'],1);Lp=2*real_coefficient(jets['log_radius'],2)
        H=real_coefficient(jets['slope_ratio'],0);Hp=real_coefficient(jets['slope_ratio'],1)
        e0=arb(0,maj['mean_energy'][0]);e1=arb(0,maj['mean_energy'][1])
        Ebar=L*L+aa*aa*H*H+e0;R=H*H+e0/(aa*aa)
        K=(H*H*(L*L-Lp)+L*H*Hp+(L*e1-2*Lp*e0)/(2*aa*aa))/(Ebar*Ebar)
        return dict(a=aa,beta=L,Ebar=Ebar,R=R,K=K,
            primitive_error_0=maj['mean_energy'][0],primitive_error_1=maj['mean_energy'][1]),(Fraction(3),Fraction(25,8)),'graft'

    def values(self,left,right):
        values,germ,part=(self.body_values(left,right) if right<=3 else self.graft_values(left,right))
        if not all(values[x]>0 for x in ('a','Ebar','R','K')):
            raise ValueError('rotational positive chart unresolved')
        values.update(gamma=values['Ebar'].sqrt(),
            Cref=-(values['R']/values['Ebar']).sqrt(),
            lambda_ref=values['K']*values['Ebar']/values['R'],
            radial_slope=values['beta']/values['Ebar'].sqrt())
        if not all(x.is_finite() for x in values.values()):raise ValueError('nonfinite true cap coefficient')
        return values,germ,part


def logistic_flow(q,A,B,C,h):
    """Exact positive solution of q'=A+Bq-Cq^2 for constant A,C>0."""
    if not min(q,A,C)>0 or not h>=0:raise ValueError('invalid Riccati comparison initial data')
    D=(B*B+4*A*C).sqrt()
    positive=2*A/(D-B);negative=-(D-B)/(2*C)
    ratio=(q-positive)/(q-negative)*(-D*h).exp()
    denominator=1-ratio
    if not denominator>0:raise ValueError('Riccati comparison denominator unresolved')
    result=(positive-ratio*negative)/denominator
    if not result>0 or not result.is_finite():raise ValueError('positive comparison flow failed')
    return result


def propagate(rows,entry,modes):
    aa=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    if not (aa>0 and aa<arb(7)/10**6 and omega>arb(7)/5 and omega<arb(3)/2):
        raise ValueError('R74 actual entrance domain failed')
    E=1+(aa/(4*omega))**2;base=1/E.sqrt();length=Fraction(2**24)-Fraction(25,8)
    common_fee=(arb(2)**42*(-8*omega.lower()*exact_arb(length)).exp()).upper()
    if not common_fee<arb(2)**-100:raise ValueError('true infinite regular-tail fee exceeds the paid bound')
    answers=[]
    for j in range(1,modes+1):
        m=4*j;fee=arb(0) if j==1 else (arb(2)**42*(-2*m*omega.lower()*exact_arb(length)).exp()).upper()
        low=(base.lower()-fee).lower();high=(base.upper()+fee).upper();initial=[record(low),record(high)]
        trajectory=[]
        for row in reversed(rows):
            left,right=map(Fraction,row['interval']);h=exact_arb(right-left)
            c={name:box_from_record(row['coefficients'][name]) for name in ('gamma','beta','lambda_ref')}
            gamma,lam,beta=c['gamma'],c['lambda_ref'],c['beta'];linear=-beta*(lam-1)
            lower_flow=logistic_flow(low,(m*gamma.lower()*lam.lower()).lower(),linear.lower(),
                (m*gamma.upper()).upper(),h)
            upper_flow=logistic_flow(high,(m*gamma.upper()*lam.upper()).upper(),linear.upper(),
                (m*gamma.lower()).lower(),h)
            low,high=lower_flow.lower(),upper_flow.upper()
            if not 0<low<=high:raise ValueError('actual Jacobi ratio enclosure failed')
            # Decimal ball strings still enclose the directed endpoints;
            # consumers must take .lower()/.upper() again after parsing.
            trajectory.append([*row['interval'],low.str(40),high.str(40)])
        answers.append(dict(physical_frequency=m,initial_q_bounds=initial,true_tail_fee=record(fee),
            final_q_lower=record(low),final_q_upper=record(high),
            final_B_sine_over_C_cosine_lower=record(-high),final_B_sine_over_C_cosine_upper=record(-low),
            trajectory_columns=['left','right','q_lower_outer_ball','q_upper_outer_ball'],trajectory=trajectory))
    gl=min(box_from_record(r['coefficients']['gamma']).lower() for r in rows).lower()
    gu=max(box_from_record(r['coefficients']['gamma']).upper() for r in rows).upper()
    ll=min(box_from_record(r['coefficients']['lambda_ref']).lower() for r in rows).lower()
    lu=max(box_from_record(r['coefficients']['lambda_ref']).upper() for r in rows).upper()
    linear=max(abs(-box_from_record(r['coefficients']['beta'])*(box_from_record(r['coefficients']['lambda_ref'])-1)).upper() for r in rows).upper()/4
    qlo=2*gl*ll/((linear*linear+4*gu*gl*ll).sqrt()+linear)
    qhi=((linear*linear+4*gl*gu*lu).sqrt()+linear)/(2*gl)
    lower=min((base.lower()-common_fee).lower(),qlo.lower()).lower()
    upper=max((base.upper()+common_fee).upper(),qhi.upper()).upper()
    if not 0<lower<upper:raise ValueError('full-frequency invariant positive interval failed')
    return dict(finite_mode_entries=answers,full_frequency_interval=dict(
        physical_frequencies='every m=4j, j>=1; negative modes by real conjugacy',
        q_lower=record(lower),q_upper=record(upper),
        gamma_lower=record(gl),gamma_upper=record(gu),lambda_lower=record(ll),lambda_upper=record(lu),
        linear_over_minimum_frequency=record(linear),
        exact_boundary_identity='B_sine/C_cosine=lambda_R74/(m omega sqrt(1+w^2)); q is its negative',
        complete_true_tail_fee=record(common_fee)))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9));ap.add_argument('--nodes',type=int,default=512)
    ap.add_argument('--left',type=Fraction,default=Fraction(239,1000));ap.add_argument('--right',type=Fraction,default=Fraction(25,8))
    ap.add_argument('--bits',type=int,default=256);ap.add_argument('--modes',type=int,default=16)
    ap.add_argument('--maximum-coefficient-ratio',type=Fraction,default=Fraction(3,2));ap.add_argument('--max-depth',type=int,default=20)
    ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();ctx.prec=a.bits;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('refusing to overwrite a completed cap Jacobi certificate')
    if not 0<a.left<3 or a.right!=Fraction(25,8) or a.half_width<=0 or a.modes<1:raise ValueError('invalid true cap domain')
    target=RotationalPositiveCap(a.object,a.half_width,a.nodes)
    definition,_,_,center=load_definition(a.object)
    r74_center=Fraction(-7789866024620307,4611686018427387904);r74_half=Fraction(1,2000000)
    if not r74_center-r74_half<=center-a.half_width<center+a.half_width<=r74_center+r74_half:
        raise ValueError('requested exact parameter interval exceeds the true R74 tail theorem')
    if (definition['origin_inputs']['sha256']!='0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b'
        or definition['direction']['sha256']!='8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab'):
        raise ValueError('the actual R74 family input identity changed')
    cuts=sorted({a.left,Fraction(3),a.right}|{x for x in target.cuts if a.left<x<3})
    pending=[(l,r,0) for l,r in reversed(list(zip(cuts[:-1],cuts[1:])))]
    rows=[];subdivisions=[];failure=None;last_progress=started
    while pending:
        left,right,depth=pending.pop()
        try:
            values,germ,part=target.values(left,right)
            ratio=max((values[k].upper()/values[k].lower()).upper() for k in ('gamma','lambda_ref','R'))
            if not ratio<exact_arb(a.maximum_coefficient_ratio):raise ValueError('coefficient ratio requests subdivision')
            rows.append(dict(interval=[str(left),str(right)],actual_scalar_germ=list(map(str,germ)),part=part,
                coefficients={k:record(v) for k,v in values.items()},maximum_ratio=record(ratio),depth=depth))
        except (ValueError,ZeroDivisionError) as e:
            subdivisions.append(dict(interval=[str(left),str(right)],depth=depth,reason=str(e)))
            if depth>=a.max_depth:failure=subdivisions[-1];break
            mid=(left+right)/2;pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
        if time.monotonic()-last_progress>20:
            print(dict(completed_boxes=len(rows),pending=len(pending),last_right=str(right),wall=time.monotonic()-started),flush=True)
            last_progress=time.monotonic()
    endpoint=a.left
    for row in rows:
        left,right=map(Fraction,row['interval'])
        if left!=endpoint:raise ValueError('true cap cover gap')
        endpoint=right
    complete=failure is None and not pending and endpoint==a.right
    report=dict(kind='actual_fixed_target_rotational_cap_complete_Codazzi_Jacobi',complete=complete,
        source_sha256=sha(__file__),object_sha256=sha(a.object),origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],exact_center_parameter=str(center),parameter_half_width=str(a.half_width),
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        exact_requested_interval=[str(a.left),str(a.right)],covered_interval=[str(a.left),str(endpoint)],
        nodes=a.nodes,bits=a.bits,requested_finite_modes=a.modes,maximum_coefficient_ratio=str(a.maximum_coefficient_ratio),
        rows=rows,subdivisions=subdivisions,failure=failure,cap_linear_reference_certified=False,
        nonlinear_waist_branch_matched=False,closed_surface_complete=False,
        actual_R74_parameter_interval=[str(r74_center-r74_half),str(r74_center+r74_half)],
        mean_channel=dict(curvature_mean_not_used_as_a_regular_height_port=True,
            formal_curvature_transfer='b0_r=-2 beta b0; c0_r=-beta(lambda_ref+1)c0',
            actual_periodic_homogeneous_mean='On the rotational chart, periodic axisymmetric infinitesimal isometries are axial translation and axial rotation; their curvature variation is zero.',
            retained_position_port='Axial translation / regular mean height xi remains a separate rigid slot; this curvature graph does not supply a forced mean-flux inverse.'),
        input_theorem_sha256={name:sha(Path('results')/name) for name in (
            'R74-actual-full-tail-robin-and-augmented-positive-cap.md',
            'R126-exact-Codazzi-reconstruction-and-continuation.md')},
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_metric_defect.py','fourfold_phase_cap_scaled_body.py',
            'fourfold_phase_cap_parameter_comparison.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_natural_exterior_graft.py',
            'fourfold_phase_exterior_entry_jet.py','fourfold_phase_beta_parameter_germ.py','fourfold_phase_beta_affine.py')})
    if complete:
        entry=target.graft.exact_radial_entrance();report['true_R74_entrance']=entry
        # Preserve the completed expensive coefficient cover even if a
        # later finite comparison arithmetic gate fails.
        report['wall_seconds']=time.monotonic()-started;save(a.out,report)
        try:
            report['Jacobi']=propagate(rows,entry,a.modes);report['cap_linear_reference_certified']=True
        except (ValueError,ZeroDivisionError) as e:
            report['Jacobi_failure']=str(e)
    report['wall_seconds']=time.monotonic()-started;save(a.out,report)
    print(dict(complete=complete,cap_linear_reference_certified=report['cap_linear_reference_certified'],
        boxes=len(rows),failure=failure,wall_seconds=report['wall_seconds'],out=str(a.out)),flush=True)
    if report['cap_linear_reference_certified']:
        print([dict(m=x['physical_frequency'],q_lower=x['final_q_lower']['lower'],q_upper=x['final_q_upper']['upper'])
            for x in report['Jacobi']['finite_mode_entries']],flush=True)


if __name__=='__main__':main()
