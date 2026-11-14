#!/usr/bin/env python3
"""Consume a saved full native log-Codazzi cubic, including off-collocation points.

This finite screen preserves true first-x jets and the moving angular/radial
charts. It is not a continuous residual certificate. No ODE/BVP is re-solved.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_native_log_field import NativeLogField,write_native_definition,identity,locate_near,log_codazzi_numerators
from fd2d_balanced_curvature_core import FixedBalancedGeometry,BalancedCurvatureCore,LD,PI,PERIOD
from fd2d_gc_design_profile import CoastDesignProfile

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',type=Path,required=True)
    parser.add_argument('--definition',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--angular',type=int,default=512)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError('Use a new native-field residual report')
    started=time.monotonic();report=json.loads(args.report.read_text())
    if not args.definition.exists():write_native_definition(args.report,args.definition)
    field=NativeLogField(args.definition)
    if field.meta['source_report']['sha256']!=identity(args.report)['sha256']:
        raise ValueError('Native field binds another actual run')
    used=[]
    for row in report['sources']:
        name=Path(row.get('path',row.get('file'))).name
        if name in ('fd2d_gc_design_profile.py','fd2d_partial_return_parameter.py','fd2d_frozen_ellipse_candidate.py'):
            path=HERE/name
            if identity(path)['sha256']!=row['sha256']:raise ValueError('A target definition source changed')
            used.append(identity(path))
    source=locate_near(args.report,report['candidate_input'])
    profile=CoastDesignProfile(source,reference_T=report['radial_chart']['reference_T'])
    profile.set_parameter(report['parameters']['T'])
    geometry=FixedBalancedGeometry()
    central=BalancedCurvatureCore(report['parameters']['central_c'],base_kind='circle',geometry=geometry)
    if central.definition()['coefficients_exact']!=field.meta['initial_geometry']['coefficients_exact']:
        raise ValueError('Actual central parameters do not match their exact geometry definition')
    xi=np.arange(args.angular,dtype=LD)*PERIOD/args.angular
    initial_coordinates=geometry.material_coordinate(xi)
    displacement=initial_coordinates['u']-xi;qseed=initial_coordinates['u_phi']
    blend_left,blend_right=map(LD,field.meta['angular_chart']['blend_interval'])

    def values_at(x):
        x=np.asarray(x,dtype=LD)
        f=field.evaluate(x,xi);p=profile.jet(np.asarray(x,dtype=float))
        a,ap,app,J=(np.asarray(p[key],dtype=LD)[:,None] for key in ('a','a_s','a_ss','radial_scale'))
        t=np.clip((x-blend_left)/(blend_right-blend_left),0,1)
        beta=t**3*(10-15*t+6*t*t);betax=30*t*t*(1-t)**2/(blend_right-blend_left)
        q=1+(1-beta[:,None])*(qseed[None,:]-1);Ux=-betax[:,None]*displacement[None,:]
        eta,zeta,ex,zx,eu,zu=(f[key] for key in ('eta','zeta','eta_x','zeta_x','eta_xi','zeta_xi'))
        v2=1-ap*ap;v=np.sqrt(v2);nr=v/a;chi=-a*app/v2;c=ap/a
        positive=np.exp(eta);inverse=np.exp(-eta);inverse2=np.exp(-2*eta);em2=np.expm1(-2*eta)
        material_eta=(ex-(Ux/q)*eu)/J;material_zeta=(zx-(Ux/q)*zu)/J
        Eeta=material_eta-inverse*zu/(a*q)-c*(inverse2*zeta*zeta+chi*em2)
        Ezeta=material_zeta-inverse*(2*zeta*zu-(zeta*zeta+chi)*eu)/(a*q)+c*(1+chi)*zeta
        n,m=nr*positive,nr*zeta;Rn=n*Eeta;Rm=nr*Ezeta
        numerators=log_codazzi_numerators(a,ap,app,J,q,Ux,eta,zeta,ex,zx,eu,zu,inverse,inverse2,em2)
        den=numerators['denominator_without_sqrt']*v
        pn=positive*numerators['Pn']/den;pm=numerators['Pm']/den
        dlognr=c*(chi-1);l=nr*inverse*(zeta*zeta+chi)
        direct_n=n*(material_eta+dlognr)-nr*zu/(a*q)-c*(l-n)
        direct_m=nr*(material_zeta+dlognr*zeta)-nr*inverse*(2*zeta*zu-(zeta*zeta+chi)*eu)/(a*q)+2*c*m
        return dict(Rn=Rn,Rm=Rm,n=n,m=m,a=a[:,0],physical_s=np.asarray(p['s'],dtype=LD),
            J=J,q=q,v2=v2,eta=eta,zeta=zeta,
            numerator_difference=max(np.max(abs(Rn-pn)),np.max(abs(Rm-pm))),
            direct_difference=max(np.max(abs(Rn-direct_n)),np.max(abs(Rm-direct_m))))

    f0=values_at(field.nodes[:1]);true_n=central.curvature(xi)['n']
    initial_D0=float(geometry.a0*np.max(np.sqrt((f0['n'][0]-true_n)**2+f0['m'][0]**2)))
    fractions=np.array([0,LD('.5')-np.sqrt(LD(15))/10,LD('.25'),LD('.5'),LD('.75'),LD('.5')+np.sqrt(LD(15))/10,1],dtype=LD)
    rows=[];worst_n=worst_m=0.;minimum_n=np.inf;eta_max=zeta_max=0.;ndiff=ddiff=0.
    D=LD(initial_D0);C=LD(0);metric_surrogate=LD(0);worst_location=None
    for cell in range(len(field.nodes)-1):
        left,right=map(LD,field.nodes[cell:cell+2]);x=left+(right-left)*fractions
        result=values_at(x);rn,rm=result['Rn'],result['Rm'];r=np.sqrt(rn*rn+rm*rm)
        i,j=np.unravel_index(np.argmax(r),r.shape);maximum=float(r[i,j])
        if worst_location is None or maximum>worst_location['residual']:
            worst_location=dict(cell=cell,x=float(x[i]),material_s=float(result['physical_s'][i]),xi=float(xi[j]),residual=maximum)
        worst_n=max(worst_n,float(abs(rn).max()));worst_m=max(worst_m,float(abs(rm).max()))
        minimum_n=min(minimum_n,float(result['n'].min()));eta_max=max(eta_max,float(abs(result['eta']).max()));zeta_max=max(zeta_max,float(abs(result['zeta']).max()))
        ndiff=max(ndiff,float(result['numerator_difference']));ddiff=max(ddiff,float(result['direct_difference']))
        h=result['physical_s'][-1]-result['physical_s'][0];ar=max(result['a'])*LD(maximum)
        C+=h*D+h*h*ar/2;D+=h*ar
        eta=C/result['a'][-1];metric_surrogate=max(metric_surrogate,2*eta+eta*eta)
        rows.append(dict(cell=cell,x_left=float(left),x_right=float(right),physical_s_left=float(result['physical_s'][0]),physical_s_right=float(result['physical_s'][-1]),
            sampled_Rn_max=float(abs(rn).max()),sampled_Rm_max=float(abs(rm).max()),sampled_residual_max=maximum,
            sampled_n_min=float(result['n'].min()),sampled_a_max=float(max(result['a']))))
    output=dict(schema='fd2d-gc-native-design-off-collocation-screen-v1',scope=__doc__,source=identity(__file__),
        native_reader=identity(HERE/'fd2d_gc_native_log_field.py'),shared_hermite_algebra=identity(HERE/'fd2d_gc_shared_hermite_field.py'),
        definition=identity(args.definition),source_report=identity(args.report),target_source=identity(source),target_providers=used,
        exact_central_provider=identity(HERE/'fd2d_balanced_curvature_core.py'),
        radial_cells=len(rows),radial_fractions=[float(v) for v in fractions],angular_samples=args.angular,
        minimum_n=minimum_n,maximum_native_eta=eta_max,maximum_native_zeta=zeta_max,
        Rn_maximum=worst_n,Rm_maximum=worst_m,worst_location=worst_location,
        coefficient_numerator_identity_floating_max=ndiff,original_n_m_identity_floating_max=ddiff,
        initial_frame_defect_sample_max=initial_D0,initial_position_tangency_defect_exact=0,
        R119_sampled_cell_maximum_surrogate=dict(final_frame_defect=float(D),final_position_tangency_defect=float(C),
            metric_relative_maximum=float(metric_surrogate),is_upper_bound=False,
            explanation='Cell sampled maxima replace continuous suprema only for a diagnostic; no bound or completed metric certificate is claimed.'),
        source_node_midpoint_screen=report['residual_screen'],rows=rows,
        complete_radial_cell_sampling=True,continuous_residual_certificate=False,
        actual_n_m_preserve_full_native_exponential=True,physical_material_reconstruction='fixed u; (d_x-U_x/U_xi*d_xi)/S_x',
        source_cut_mean_defect=report['final']['omitted_n_mean'],nonlinear_tail_solved=False,closed_surface=False,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:output[key] for key in ('Rn_maximum','Rm_maximum','worst_location','minimum_n','initial_frame_defect_sample_max','R119_sampled_cell_maximum_surrogate','seconds')}),flush=True)


if __name__=='__main__':main()
