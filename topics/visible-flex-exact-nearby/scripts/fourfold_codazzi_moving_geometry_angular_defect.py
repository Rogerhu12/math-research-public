#!/usr/bin/env python3
"""Complete continuous-angle defect bounds for the original moving centre.

Reuse complete original residual and intrinsic/state coefficient covers.
No original primitive row is recomputed.  The single uncovered root box
is evaluated on its true common scalar/candidate germ.  Every original
candidate value jump, both means and the model anchor defect are paid.
This does not assert nonlinear existence or a true exterior world anchor.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_current_positive_complete_coefficients import (
    CURRENT_SHA,OBJECT_SHA,dyadic,polynomial_values,exact_polynomial_endpoint,
    literal_coordinates)
from fourfold_codazzi_moving_residual_checkpointed import ReciprocalFullTargetJets
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

STRICT_SHA='23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a'
POSITIVE_SHA='ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'


def load(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def hi(x):return abs(x).upper()
def norm(*values):return sum((x*x for x in values),arb(0)).sqrt().upper()
def value(x):return box_from_record(x)


def strict_coefficients(row):
    b=row['base'];z=row['actual_target'];s=row['scalar_mean']
    up=hi(value(b['full_u_phi_absolute']))
    dp=hi(value(b['actual_d_phi']))
    # Odd fourfold functions vanish at every multiple of pi/4.  Every
    # point is at distance at most pi/8 from such a zero.
    return dict(a=hi(value(s['actual_a'])),
        beta=hi(value(z['beta'])),gamma=hi(value(z['gamma'])),
        gamma_lower=value(z['gamma']).lower(),K=hi(value(z['K'])),
        m_lower=(-value(b['actual_m'])).lower(),
        u=(arb.pi()*up/8).upper(),v=hi(value(b['v_abs_upper'])),
        up=up,vp=hi(value(b['full_v_phi_absolute'])),
        d=(arb.pi()*dp/8).upper(),dp=dp)


def positive_coefficients(row):
    b=row['bounds'];z=row['intrinsic']
    return dict(a=hi(value(z['a'])),beta=hi(value(z['beta'])),
        gamma=hi(value(z['gamma'])),gamma_lower=value(z['gamma']).lower(),
        K=hi(value(z['K'])),m_lower=(-value(b['mean_v'])).lower(),
        u=hi(value(b['U_A0'])),v=hi(value(b['V_A0'])),
        up=hi(value(b['U_phi_A0'])),vp=hi(value(b['V_phi_A0'])),
        d=hi(value(b['drift_A0'])),dp=hi(value(b['drift_phi_A0'])))


def full_polynomial_coefficients(saved,nodes,left,right,alpha,target,nu):
    piece=bisect_right(nodes,left)-1
    if not nodes[piece]<=left<right<=nodes[piece+1]:
        raise ValueError('the root gap crossed a true candidate piece')
    z,germ=target.coefficients(left,right,nu)
    y=polynomial_values(saved,nodes,piece,left,right);M=32;al=exact_arb(alpha)
    u=[al*x for x in y[:M]];vc=[al*x for x in y[M:]]
    mean=z['s']+vc[0]
    u0=sum(map(abs,u),arb(0)).upper()
    v0=(abs(mean)+sum(map(abs,vc[1:]),arb(0))).upper()
    u1=sum((4*j*abs(x) for j,x in enumerate(u,1)),arb(0)).upper()
    v1=sum((4*j*abs(x) for j,x in enumerate(vc[1:],1)),arb(0)).upper()
    S=(u0*u0+hi(z['K'])*v0*v0).upper()
    c=dict(a=hi(z['a']),beta=hi(z['beta']),gamma=hi(z['gamma']),
        gamma_lower=z['gamma'].lower(),K=hi(z['K']),
        m_lower=(-mean).lower(),u=u0,v=v0,up=u1,vp=v1,
        d=(hi(z['beta'])*S/4).upper(),dp=(2*hi(z['beta'])*S).upper())
    return c,dict(candidate_piece=piece,actual_scalar_germ=list(map(str,germ)),
        full_65_real_coefficients_retained=True,
        complete_primitive_Wiener_bound='||I S||_A0 <= ||S||_A0/4',
        coefficients={k:record(x) for k,x in c.items()})


def connection_bounds(c,ru,rv,ru1,rv1):
    a,b,g,gl,k,m,u,v,up,vp,d,dp=[c[x] for x in (
        'a','beta','gamma','gamma_lower','K','m_lower','u','v',
        'up','vp','d','dp')]
    if not min(a,gl,m)>0:raise ValueError('a true model denominator is unresolved')
    tau=(d*v/m+g*u).upper()
    tau1=(dp*v/m+d*vp/m+g*up).upper()
    omega=norm(b*v/(gl*m),a*u/m,a/m)
    omega1=norm(b*vp/(gl*m),a*up/m)
    radial=norm(b*tau/gl,a*(g*k*v+d*u/m),a*d/m)
    radial1=norm(b*tau1/gl,a*(g*k*vp+(dp*u+d*up)/m),a*dp/m)
    f=norm(a*g,a*tau);f1=(a*tau1).upper()
    angular_f=(a*v/m).upper();angular_f1=(a*vp/m).upper()
    # The even source mean is bounded by rv and is never deleted.
    curvature=norm(b*(rv+v*rv/m)/(gl*m),a*(ru+u*rv/m)/m,a*rv/(m*m))
    curvature1=norm(b*(rv1+vp*rv/m)/(gl*m),a*(ru1+up*rv/m)/m)
    torsion=(a*(rv+v*rv/m)/m).upper()
    torsion1=(a*(rv1+vp*rv/m)/m).upper()
    return dict(omega=omega,omega_phi=omega1,radial_omega=radial,
        radial_omega_phi=radial1,radial_speed=f,radial_speed_phi=f1,
        angular_speed=angular_f,angular_speed_phi=angular_f1,
        curvature=curvature,curvature_phi=curvature1,
        torsion=torsion,torsion_phi=torsion1)


def advance(state,c,width):
    e,e1,p,p1=state;h=exact_arb(width)
    R,R1,T,T1,W,Ar1,f,f1=[c[x] for x in (
        'curvature','curvature_phi','torsion','torsion_phi','omega',
        'radial_omega_phi','radial_speed','radial_speed_phi')]
    aa=Ar1+R;bb=W*R+R1
    integral_e=h*e+h*h*R/2
    integral_e1=h*e1+h*h*(aa*e+bb)/2+h*h*h*aa*R/6
    return [(e+h*R).upper(),(e1+h*(aa*e+bb)+h*h*aa*R/2).upper(),
        (p+f*integral_e+h*T).upper(),
        (p1+f*integral_e1+(f1+T)*integral_e+h*(W*T+T1)).upper()]


def hull(c,d):
    return {k:(min(c[k],d[k]).lower() if k.endswith('_lower') else
               max(c[k],d[k]).upper()) for k in c}


def join_fees(c,ju,jv):
    a,b,gl,m,u,v,up,vp=[c[x] for x in (
        'a','beta','gamma_lower','m_lower','u','v','up','vp')]
    # Each source is the complete physical A0 jump.  Its largest actual
    # physical frequency is 128.  The mean jump is at most jv.
    dv=(jv/m+v*jv/(m*m)).upper()
    du=(ju/m+u*jv/(m*m)).upper()
    di=(jv/(m*m)).upper()
    dv1=(128*jv/m+vp*jv/(m*m)).upper()
    du1=(128*ju/m+up*jv/(m*m)).upper()
    return [norm(b*dv/gl,a*du,a*di),norm(b*dv1/gl,a*du1),
            (a*dv).upper(),(a*dv1).upper()]


def model_anchor(saved,nodes,alpha,target,nu):
    R=Fraction(25,8);z,_=target.coefficients(R,R,nu)
    y=exact_polynomial_endpoint(saved,nodes,6143,R);al=exact_arb(alpha)
    u=[al*exact_arb(x) for x in y[:32]]
    v=[al*exact_arb(x) for x in y[32:]]
    mean=z['s']+v[0];m=(-mean).lower()
    if not m>0:raise ValueError('the original model anchor mean is unresolved')
    u0=sum(map(abs,u),arb(0)).upper();v0=sum(map(abs,v),arb(0)).upper()
    u1=sum((4*j*abs(x) for j,x in enumerate(u,1)),arb(0)).upper()
    v1=sum((4*j*abs(x) for j,x in enumerate(v[1:],1)),arb(0)).upper()
    aa=hi(z['a']);cr=hi(z['Cref'])
    theta=((abs(mean)+sum(map(abs,v[1:]),arb(0)))/m).upper()
    e=norm(aa*u0/m,aa*cr*v0/m)
    e1=(theta*e+norm(aa*u1/m,aa*cr*v1/m)).upper()
    return [e,e1,arb(0),arb(0)],dict(
        radial='25/8',frame='X=(beta/gamma)e_r-a Cref e_z; Y=e_theta; N=-a Cref e_r-(beta/gamma)e_z',
        exact_orthogonality='(beta/gamma)^2+(a Cref)^2=1 outside the compact nu support',
        complete_angle_speed=record(theta),frame_defect=record(e),
        angular_frame_defect=record(e1),position_defect='exactly zero',
        angular_position_defect='exactly zero',
        actual_exterior_world_anchor_not_substituted=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--residual',type=Path,required=True)
    ap.add_argument('--strict',type=Path,required=True)
    ap.add_argument('--positive',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every complete geometry consumer')
    if sha(args.candidate)!=CURRENT_SHA or sha(args.object)!=OBJECT_SHA:
        raise ValueError('the original centre and true target are required')
    if sha(args.strict)!=STRICT_SHA or sha(args.positive)!=POSITIVE_SHA:
        raise ValueError('the actual complete strict and positive input bytes changed')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if meta['coordinates']!=literal_coordinates() or meta['object_sha256']!=OBJECT_SHA:
        raise ValueError('the complete moving centre changed')
    nodes=list(map(dyadic,saved['radial_nodes']))
    alpha=Fraction(meta['exact_float_amplitude']);nu=Fraction(meta['exact_float_nu'])
    res,strict,positive=[load(x) for x in (args.residual,args.strict,args.positive)]
    if (res['kind']!='complete_actual_moving_residual_all_closed_rows_and_interfaces' or
        not res['complete'] or res['failure'] is not None or
        res['candidate_sha256']!=CURRENT_SHA or res['object_sha256']!=OBJECT_SHA or
        res['exact_amplitude']!=str(alpha) or res['exact_nu']!=str(nu) or
        len(res['rows'])!=7296 or len(res['complete_interface_jumps'])!=6143):
        raise ValueError('complete same-object residual and every join are required')
    if (not strict['complete'] or strict['failure'] is not None or
        strict['object_sha256']!=OBJECT_SHA or strict['exact_nu']!=str(nu) or
        strict['exact_amplitude']!=str(alpha) or not strict['whole_requested_radial_interval'] or
        CURRENT_SHA not in strict['inputs'].values()):
        raise ValueError('the complete strict same-object cover is required')
    if (not positive['complete'] or not positive['coefficient_cover_complete'] or
        positive['failure'] is not None or
        positive['identity']['candidate_sha256']!=CURRENT_SHA or
        positive['identity']['object_sha256']!=OBJECT_SHA or
        positive['identity']['actual_nu']!=str(nu) or
        positive['identity']['actual_alpha']!=str(alpha)):
        raise ValueError('the complete positive same-centre cover is required')
    cover=[]
    for i,row in enumerate(strict['rows']):
        cover.append((tuple(map(Fraction,row['interval'])),strict_coefficients(row),['strict',i]))
    left=cover[-1][0][1];right=Fraction(positive['rows'][0]['interval'][0])
    target=ReciprocalFullTargetJets(args.object,Fraction(1,10**9),512)
    gap,root_native=full_polynomial_coefficients(saved,nodes,left,right,alpha,target,nu)
    cover.append(((left,right),gap,['new_true_root_box',0]))
    for i,row in enumerate(positive['rows']):
        cover.append((tuple(map(Fraction,row['interval'])),positive_coefficients(row),['positive',i]))
    for i,(interval,c,_) in enumerate(cover):
        if min(c['a'],c['gamma_lower'],c['m_lower'])<=0:
            raise ValueError('a complete coefficient box lost its true mean/metric gap')
        if i and interval[0]!=cover[i-1][0][1]:raise ValueError('coefficient cover has a gap or overlap')
    if cover[0][0][0]!=0 or cover[-1][0][1]!=Fraction(25,8):raise ValueError('full radial coverage is required')
    rintervals=[tuple(map(Fraction,x['interval'])) for x in res['rows']]
    for i,(l,r) in enumerate(rintervals):
        if l>=r or i and l!=rintervals[i-1][1]:raise ValueError('residual partition is not complete')
    cuts=sorted({x for interval,_,_ in cover for x in interval}|
                {x for interval in rintervals for x in interval})
    cleft=[x[0][0] for x in cover];rleft=[x[0] for x in rintervals]
    common=[];al=abs(exact_arb(alpha))
    for l,r in zip(cuts,cuts[1:]):
        ci=bisect_right(cleft,l)-1;ri=bisect_right(rleft,l)-1
        if r>cover[ci][0][1] or r>rintervals[ri][1]:raise ValueError('a common closed box crosses its source')
        rr=res['rows'][ri]
        ru,rv=[al*value(rr['complete_residual_A0'][k]).upper() for k in ('U','V')]
        ru1,rv1=[al*value(rr['complete_residual_A1'][k]).upper() for k in ('U','V')]
        common.append((l,r,ci,ri,connection_bounds(cover[ci][1],ru,rv,ru1,rv1)))
    jumps={Fraction(x['radius']):x for x in res['complete_interface_jumps']}
    state,anchor=model_anchor(saved,nodes,alpha,target,nu)
    initial=list(state);outputs=[];consumed=0
    maxima={k:arb(0) for k in ('frame_defect','frame_defect_phi','position_defect',
        'position_defect_phi','position_second_angular_derivative',
        'frame_second_angular_derivative')}
    for i in range(len(common)-1,-1,-1):
        l,r,ci,ri,c=common[i]
        state=advance(state,c,r-l);e,e1,p,p1=state
        F2=((c['omega']+e)*c['angular_speed']+c['angular_speed_phi']+p1).upper()
        Q2=(c['omega']**2+e*c['omega']+c['omega_phi']+e1).upper()
        vals=dict(zip(('frame_defect','frame_defect_phi','position_defect','position_defect_phi'),state))
        vals.update(position_second_angular_derivative=F2,frame_second_angular_derivative=Q2)
        for k,v in vals.items():maxima[k]=max(maxima[k],v).upper()
        out=dict(interval=[str(l),str(r)],coefficient_source=cover[ci][2],
            residual_row=ri,bounds={k:record(v) for k,v in vals.items()},
            model_coefficients={k:record(c[k]) for k in (
                'omega','radial_omega','radial_speed','angular_speed',
                'angular_speed_phi','curvature','curvature_phi','torsion','torsion_phi')})
        if l in jumps:
            if i==0:raise ValueError('a candidate join cannot be the waist')
            jc=hull(cover[ci][1],cover[common[i-1][2]][1])
            ju,jv=[al*value(z).upper() for z in jumps[l]['complete_A0']]
            jW,jW1,jf,jf1=join_fees(jc,ju,jv)
            qphi=c['omega']+e
            state=[(e+jW).upper(),(e1+qphi*jW+jW1).upper(),
                   (p+jf).upper(),(p1+qphi*jf+jf1).upper()]
            out['left_candidate_join']=dict(knot_index=jumps[l]['knot_index'],
                full_mean_included=True,fees=list(map(record,(jW,jW1,jf,jf1))),
                after_join_defects=list(map(record,state)))
            consumed+=1
        outputs.append(out)
        if len(outputs)%1024==0:print(dict(completed_common_boxes=len(outputs),total=len(common)),flush=True)
    if consumed!=6143:raise ValueError('not every actual candidate jump was consumed')
    factor=(arb.pi()/(2*512))**2/8
    doc=dict(kind='complete_original_moving_model_continuous_angular_defect_v1',
        complete=True,failure=None,source_sha256=sha(__file__),candidate_sha256=CURRENT_SHA,
        object_sha256=OBJECT_SHA,exact_amplitude=str(alpha),exact_nu=str(nu),
        common_parameter_half_width=res['common_parameter_half_width'],
        inputs={str(x):sha(x) for x in (args.candidate,args.residual,args.strict,args.positive,args.object)},
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_current_positive_complete_coefficients.py',
            'fourfold_codazzi_moving_residual_checkpointed.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        true_new_common_root_box=root_native,model_anchor=anchor,
        complete_original_7296_residual_boxes_reused=True,complete_original_6143_value_jumps_paid=True,
        full_real_angular_circle=True,even_source_and_interface_means_retained=True,
        normalized_residual_multiplied_by_exact_physical_alpha=True,
        original_centre_not_relabelled_as_continuous_repair=True,
        interval=['0','25/8'],common_closed_box_count=len(common),
        rows=list(reversed(outputs)),bounds={k:record(v) for k,v in maxima.items()},
        exact_angle_grid='phi_k=pi*k/(2*512), with true fourfold wrap',
        angular_linear_interpolation=dict(factor=record(factor.upper()),
            position=record((factor*maxima['position_second_angular_derivative']).upper()),
            frame=record((factor*maxima['frame_second_angular_derivative']).upper())),
        original_anchor_defects=list(map(record,initial)),waist_defects=list(map(record,state)),
        radial_floating_integration_error_included=False,
        actual_exterior_world_anchor_included=False,
        nonlinear_PDE_existence_proved=False,final_geometric_criteria_proved=False,
        wall_seconds=time.monotonic()-started)
    save(args.out,doc)
    print(json.dumps(dict(complete=True,boxes=len(common),jumps=consumed,
        bounds=doc['bounds'],interpolation=doc['angular_linear_interpolation'],
        seconds=doc['wall_seconds'])),flush=True)


if __name__=='__main__':main()
