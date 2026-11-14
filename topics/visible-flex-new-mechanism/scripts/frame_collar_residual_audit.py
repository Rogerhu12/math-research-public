#!/usr/bin/env python3
"""Read-only, identity-bound residual locations for a frozen frame collar.

Research evaluations run only in the public repository Actions. The developer
check uses a mild artificial ellipse and does not optimize. Every diagnostic
here is sampled; neither a maximum nor a refinement is a continuous bound.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import (EllipticCylinderPort, NegativeKRadialSeed,
    FrameCollarProblem, audit_geometry, atomic_save, dot)


DEPENDENCIES=('frame_collar_bvp.py','ellipse_frame_port.py',
              'cosine_connector_radial_seed.py')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def source_hashes():
    return {name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in DEPENDENCIES}


def exact_binary64(values):
    result=[]
    for text in values:
        if not isinstance(text,str):raise ValueError('exact coefficients must be rational strings')
        rational=Q(text);value=float(rational)
        if not np.isfinite(value) or Q.from_float(value)!=rational:
            raise ValueError('a frozen coefficient is not the recorded exact binary64 value')
        result.append(value)
    return np.asarray(result,float)


def load_frozen_report(report):
    """No fitted field or replacement metric: rebuild the recorded definition."""
    if report.get('schema')!='orthonormal-frame-collar-design-v1':
        raise ValueError('unsupported frame report schema')
    recorded=report.get('source_files_sha256',{})
    current=source_hashes()
    for name in DEPENDENCIES:
        if recorded.get(name)!=current[name]:
            raise ValueError('solver implementation differs from the report: '+name)
    identity=report['core_physical_identity'];port_identity=report['port_identity']
    if (digest(identity)!=report['core_physical_identity_sha256'] or
        digest(port_identity)!=report['port_identity_sha256']):
        raise ValueError('core or port identity hash mismatch')
    if identity.get('kind')!='exact-elliptic-cylinder-v1':
        raise ValueError('this audit currently accepts the accurate ellipse port only')
    port=EllipticCylinderPort(identity['major'],identity['minor'],identity['half_width'],
                             side=int(port_identity['side']))
    if port.identity!=identity or port.port_identity!=port_identity:
        raise ValueError('port reconstruction changed its mathematical identity')
    definition=report['definition']
    for key,expected in [('major',port.A_exact),('minor',port.B_exact),('half_width',port.width_exact)]:
        if Q(str(definition[key]))!=expected:raise ValueError('CLI and core identity disagree: '+key)
    if int(definition['side'])!=port.side:raise ValueError('CLI and port side disagree')
    metric=report['metric_model'];seed_definition=metric['seed']
    config={key:seed_definition[key] for key in ['core_fraction','flat_fraction',
        'active_fractions','negative_curvature_drop','tail_smoothstep_order']}
    seed=NegativeKRadialSeed.from_core(port,seed_definition['length'],seed_definition['cut_radius'],config)
    if seed.frozen_definition()['definition_sha256']!=seed_definition['definition_sha256']:
        raise ValueError('seed reconstruction changed the exact metric definition')
    for key in ['length','cut_radius','core_fraction','flat_fraction','negative_curvature_drop']:
        if Q(str(definition[key]))!=Q(seed_definition[key]):
            raise ValueError('CLI and exact seed disagree: '+key)
    mathematical=metric['mathematical_definition']
    if digest(mathematical)!=metric['mathematical_definition_sha256']:
        raise ValueError('metric identity hash mismatch')
    fixed=exact_binary64(mathematical['log_basis_coefficients_exact'])
    state=exact_binary64(report['exact_field_coefficients'])
    if not np.array_equal(state,np.asarray(report['field_coefficients_binary64'],float)):
        raise ValueError('exact field coefficients and binary64 array disagree')
    problem=FrameCollarProblem(port,seed,radial_free=int(definition['radial_free']),
        angular_modes=int(definition['angular_modes']),metric_free=0,
        fixed_metric_coefficients=fixed,ellipse_envelope=(port.major,port.minor),
        height_limit=float(definition['height_limit']),shape_weight=float(definition['shape_weight']),
        radial_nodes=int(definition['radial_nodes']),angular_nodes=int(definition['angular_nodes']),
        radial_quadrature_order=int(definition['quadrature_order']))
    if len(state)!=problem.field_count or len(state)!=int(report['field_unknown_count']):
        raise ValueError('field coefficient count or basis dimensions disagree')
    replay=problem.metric_model(state)
    if replay['mathematical_definition']!=mathematical:
        raise ValueError('frozen metric basis, exact coefficients, or seed changed on replay')
    if (int(report['fold'])!=problem.fold or
        report['tail_beta_multiple_of_pi']!=-port.side or
        not np.allclose(report['active_interval'],[problem.active_start,problem.active_end],rtol=0,atol=1e-14)):
        raise ValueError('symmetry, lift branch, or active interval mismatch')
    exact_state={'port_identity_sha256':port.port_identity_sha256,
        'field_definition':{'radial_free':problem.radial_free,'angular_modes':problem.angular_modes,
            'field_basis':report['field_basis'],'base_blending':report['base_blending'],
            'exact_field_coefficients':report['exact_field_coefficients']},
        'metric_mathematical_definition_sha256':metric['mathematical_definition_sha256'],
        'solver_implementation':current}
    return problem,state,{'reconstructed_frozen_state_sha256':digest(exact_state),
        'metric_mathematical_definition_sha256':metric['mathematical_definition_sha256'],
        'all_recorded_dependency_hashes_match_current':True,
        'exact_field_binary64_roundtrip':True,'metric_is_frozen_for_this_audit':True,
        'source_was_metric_design':bool(metric.get('metric_is_being_designed')),
        'source_files_sha256':current}


def segments(problem):
    edges=problem.seed.length*problem.seed.edges
    return [('open_core',0.,float(edges[0])),
            ('first_S5',float(edges[0]),float(edges[1])),
            ('negative_K_S5',float(edges[1]),float(edges[2])),
            ('last_S'+str(problem.seed.tail_smoothstep_order),float(edges[2]),float(edges[3])),
            ('open_flat_tail',float(edges[3]),problem.seed.length)]


def segment_name(problem,t):
    bounds=segments(problem)
    for name,left,right in bounds:
        if t<right:return name
    return bounds[-1][0]


def point_arrays(problem,data):
    X,Xs,Xt=(data[key] for key in ['X','Xs','Xt'])
    a=data['metric']['a'][:,None];E=dot(Xs,Xs);F=dot(Xs,Xt);G=dot(Xt,Xt)
    aa=E-1;dd=G/a**2-1;off=F/a
    op=(abs(aa+dd)+np.hypot(aa-dd,2*off))/2
    cross=np.cross(Xs,Xt);area=np.linalg.norm(cross,axis=-1)
    normal=np.full_like(cross,np.nan)
    valid=np.isfinite(area)&(area>0)
    normal[valid]=cross[valid]/area[valid,None]
    with np.errstate(divide='ignore',invalid='ignore',over='ignore'):
        l=dot(normal,data['Xss']);m=dot(normal,data['Xst']);n=dot(normal,data['Xtt'])
        K=(l*n-m*m)/area**2;H=(E*n-2*F*m+G*l)/(2*area**2)
        disc=H*H-K;principal=abs(H)+np.sqrt(np.maximum(disc,0))
    T,V=data['frame']['T'],data['frame']['V'];W=np.cross(T,V);R=data['R']
    return {'R_norm':np.linalg.norm(R,axis=-1),'R_T':dot(R,T),'R_V':dot(R,V),'R_W':dot(R,W),
        'metric_operator_error':op,'E_minus_one':aa,'F_over_a':off,'G_over_a_squared_minus_one':dd,
        'area':area,'principal_curvature_abs':principal,'induced_K':K,'curvature_discriminant':disc,
        'ellipse_radius_squared':(X[...,0]/problem.port.major)**2+(X[...,1]/problem.port.minor)**2,
        'signed_height_minus_width':problem.port.side*X[...,2]-problem.port.width,
        'height_abs':abs(X[...,2]),'actual_radial_target_difference':np.linalg.norm(Xs-V,axis=-1)}


def finite_number(value):
    return float(value) if np.isfinite(value) else None


def extremum(values,grid,kind='max',mask=None):
    values=np.asarray(values,float)
    include=np.isfinite(values)
    if mask is not None:include&=np.broadcast_to(mask[:,None],values.shape)
    if not np.any(include):return None
    score=abs(values) if kind=='abs' else values
    selected=np.where(include,score,np.inf if kind=='min' else -np.inf)
    ij=np.unravel_index(np.argmin(selected) if kind=='min' else np.argmax(selected),values.shape)
    i,j=map(int,ij)
    return {'value':float(values[i,j]),'absolute_value':float(abs(values[i,j])),
            't':float(grid.radial[i]),'theta':float(grid.theta[j]),
            'radial_index':i,'angular_index':j}


EXTREMA={'R_norm':'max','R_T':'abs','R_V':'abs','R_W':'abs',
    'metric_operator_error':'max','E_minus_one':'abs','F_over_a':'abs',
    'G_over_a_squared_minus_one':'abs','area':'min','principal_curvature_abs':'max',
    'ellipse_radius_squared':'max','signed_height_minus_width':'min','height_abs':'max',
    'actual_radial_target_difference':'max'}


def distribution(problem,state,radial,theta,quadrature_order=8,spectrum_modes=16):
    grid=problem.grid_for(radial,theta)
    data=problem.geometry(state,grid,quadrature_order=quadrature_order)
    values=point_arrays(problem,data)
    global_extrema={key:extremum(values[key],grid,kind) for key,kind in EXTREMA.items()}
    for entry in global_extrema.values():
        if entry is not None:
            i,j=entry['radial_index'],entry['angular_index']
            entry['segment']=segment_name(problem,entry['t'])
            entry['position']=data['X'][i,j].tolist()
            entry['R_frame_components']=[float(values[k][i,j]) for k in ['R_T','R_V','R_W']]
    rows=[]
    spectrum_modes=min(int(spectrum_modes),len(theta)//2)
    fourier={key:np.fft.rfft(values[key],axis=1)/len(theta) for key in ['R_T','R_V','R_W']}
    for i,t in enumerate(radial):
        one=np.zeros(len(radial),bool);one[i]=True
        row={'t':float(t),'t_over_L':float(t/problem.seed.length),'segment':segment_name(problem,t),
            'a':float(data['metric']['a'][i]),'a_prime':float(data['metric']['a_s'][i]),
            'target_K':float(data['metric']['K'][i]),'center_z':float(data['center'][i]),
            'position_min':np.min(data['X'][i],axis=0).tolist(),
            'position_max':np.max(data['X'][i],axis=0).tolist(),
            'R_component_means':{key:float(np.mean(values[key][i])) for key in ['R_T','R_V','R_W']},
            'R_norm_rms':float(np.sqrt(np.mean(values['R_norm'][i]**2))),
            'undefined_curvature_sample_count':int(np.sum(~np.isfinite(values['principal_curvature_abs'][i]))),
            'extrema':{key:extremum(values[key],grid,kind,one) for key,kind in EXTREMA.items()}}
        row['residual_fourier_complex_modulus']={key:abs(coeff[i,:spectrum_modes+1]).tolist()
                                                for key,coeff in fourier.items()}
        rows.append(row)
    per_segment=[]
    for name,left,right in segments(problem):
        mask=(radial>=left)&(radial<=right)
        mean_extreme=extremum(np.mean(values['R_T'],axis=1)[:,None],
            problem.grid_for(radial,np.array([0.])),kind='abs',mask=mask)
        if mean_extreme is not None:
            mean_extreme['theta']=None;mean_extreme['angular_index']=None
            mean_extreme['is_full_angle_mean']=True
        per_segment.append({'name':name,'closed_interval':[left,right],
            'sampled_radial_rows':int(np.sum(mask)),
            'extrema':{key:extremum(values[key],grid,kind,mask) for key,kind in EXTREMA.items()},
            'R_T_mean_extreme':mean_extreme})
    summary=audit_geometry(problem,state,grid,data,quadrature_order)
    return {'grid':{'radial_nodes':len(radial),'angular_nodes':len(theta),
                   'center_quadrature_order':quadrature_order,
                   'radial_coordinates':radial.tolist(),'angular_grid':'2*pi*j/angular_nodes',
                   'fourier_modulus_definition':'abs(FFT(R_component)[k])/angular_nodes; no doubling',
                   'fourier_modes':list(range(spectrum_modes+1))},
            'summary':summary,'global_extrema':global_extrema,'segments':per_segment,'radial_rows':rows,
            'undefined_curvature_sample_count':int(np.sum(~np.isfinite(values['principal_curvature_abs']))),
            'minimum_curvature_discriminant_before_roundoff_clip':finite_number(np.nanmin(values['curvature_discriminant'])),
            'sampled_only':True,'continuous_residual_bound_proved':False,
            'continuous_metric_certificate':False,'embedding_proved':False,
            'whole_surface_reach_proved':False,'task_complete':False}


def summary_comparison(actual,published):
    keys=['integrability_residual_max_sample','metric_relative_operator_error_max_sample',
          'minimum_area_sample','principal_curvature_absolute_max_sample',
          'height_positive_violation_sample','signed_side_height_minus_core_width_min_sample']
    result={}
    for key in keys:
        left,right=actual.get(key),published.get(key)
        result[key]={'current':left,'published':right,
                     'difference':float(left-right) if left is not None and right is not None else None}
    return result


def artificial_report(problem,state):
    port=problem.port;seed=problem.seed;seed_def=seed.frozen_definition()
    return {'schema':'orthonormal-frame-collar-design-v1',
        'source_files_sha256':source_hashes(),'core_physical_identity':port.identity,
        'core_physical_identity_sha256':port.identity_sha256,'port_identity':port.port_identity,
        'port_identity_sha256':port.port_identity_sha256,'fold':port.fold,
        'tail_beta_multiple_of_pi':-port.side,'active_interval':[problem.active_start,problem.active_end],
        'field_unknown_count':problem.field_count,'metric_model':problem.metric_model(state),
        'exact_field_coefficients':[str(Q.from_float(float(x))) for x in state[:problem.field_count]],
        'field_coefficients_binary64':state[:problem.field_count].tolist(),
        'field_basis':'clamped degree-five B splines with first/last three coefficients omitted; sin/cos(fold*k*theta)',
        'base_blending':'degree-nine Hermite with third/fourth radial jets zero, plus compact necessary ellipse Cauchy leading terms',
        'definition':{'major':str(port.A_exact),'minor':str(port.B_exact),'half_width':str(port.width_exact),
            'side':port.side,'length':seed_def['length'],'cut_radius':seed_def['cut_radius'],
            'core_fraction':seed_def['core_fraction'],'flat_fraction':seed_def['flat_fraction'],
            'negative_curvature_drop':seed_def['negative_curvature_drop'],
            'radial_free':problem.radial_free,'angular_modes':problem.angular_modes,
            'height_limit':problem.height_limit,'shape_weight':problem.shape_weight,
            'radial_nodes':len(problem.radial),'angular_nodes':len(problem.theta),
            'quadrature_order':problem.radial_quadrature_order}}


def developer_check():
    checks=[]
    for side in [1,-1]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
        problem=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
            metric_free=1 if side==1 else 0,ellipse_envelope=(port.major,port.minor),
            radial_nodes=13,angular_nodes=32)
        state=.012*np.sin(np.arange(problem.nunknown)+.3)
        report=artificial_report(problem,state);frozen,fs,identity=load_frozen_report(report)
        radial=np.linspace(0,seed.length,19);theta=np.arange(48)*2*np.pi/48
        direct=problem.geometry(state,problem.grid_for(radial,theta),quadrature_order=6)
        replay=frozen.geometry(fs,frozen.grid_for(radial,theta),quadrature_order=6)
        difference=max(float(np.max(abs(direct[k]-replay[k]))) for k in ['X','Xs','Xss','R'])
        result=distribution(frozen,fs,radial,theta,quadrature_order=6,spectrum_modes=8)
        maxima_match=(result['global_extrema']['R_norm']['value']==result['summary']['integrability_residual_max_sample']
            and result['global_extrema']['metric_operator_error']['value']==result['summary']['metric_relative_operator_error_max_sample']
            and result['global_extrema']['area']['value']==result['summary']['minimum_area_sample'])
        rows_cover=all(any(s['closed_interval'][0]<=t<=s['closed_interval'][1] for s in result['segments']) for t in radial)
        checks.append({'side':side,'frozen_geometry_exact_evaluation_difference':difference,
            'global_maxima_agree_with_solver_summary':bool(maxima_match),'segments_cover_every_row':rows_cover,
            'source_hashes_match':identity['all_recorded_dependency_hashes_match_current']})
    rejected={}
    for name in ['source_hash','coefficient_float','coefficient_not_binary64','metric_identity','core_identity']:
        bad=copy.deepcopy(report)
        if name=='source_hash':bad['source_files_sha256']['frame_collar_bvp.py']='0'*64
        elif name=='coefficient_float':bad['field_coefficients_binary64'][0]+=1e-5
        elif name=='coefficient_not_binary64':bad['exact_field_coefficients'][0]='1/3'
        elif name=='metric_identity':bad['metric_model']['mathematical_definition']['log_basis_degree']=4
        else:bad['core_physical_identity']['major']='1'
        try:load_frozen_report(bad)
        except ValueError:rejected[name]=True
        else:rejected[name]=False
    passed=all(c['frozen_geometry_exact_evaluation_difference']==0 and c['global_maxima_agree_with_solver_summary']
        and c['segments_cover_every_row'] and c['source_hashes_match'] for c in checks) and all(rejected.values())
    return {'schema':'frame-collar-residual-audit-development-v1','passed':passed,'checks':checks,
        'rejected_mismatches':rejected,'artificial_inputs_only':True,
        'research_geometry_evaluated':False,'nonlinear_optimization_performed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--radial-nodes',type=int);parser.add_argument('--angular-nodes',type=int)
    parser.add_argument('--quadrature-order',type=int,default=8)
    parser.add_argument('--include-breakpoints',action='store_true')
    parser.add_argument('--spectrum-modes',type=int,default=16)
    parser.add_argument('--check-only',action='store_true');args=parser.parse_args()
    started=time.monotonic();hashes=source_hashes()
    hashes[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.check_only:
        output=developer_check();output['source_files_sha256']=hashes
        atomic_save(args.out,output);print(json.dumps({'out':str(args.out),'passed':output['passed']}),flush=True)
        if not output['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        parser.error('research residual evaluation runs only in the public repository Actions')
    if not args.input:parser.error('--input is required')
    repo=Path(__file__).resolve().parents[3]
    allowed=[repo/'topics'/'visible-flex-new-mechanism'/'notes']
    if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']))
    if not any(args.input.resolve().is_relative_to(root.resolve()) for root in allowed):
        parser.error('input must be a public topic note or current Actions temporary output')
    raw=args.input.read_bytes();report=json.loads(raw)
    problem,state,identity=load_frozen_report(report)
    published_key=('fixed_parameter_double_angle_audit' if 'fixed_parameter_double_angle_audit' in report
        else 'fixed_parameter_audit' if 'fixed_parameter_audit' in report else 'collocation_audit')
    published=report[published_key]
    nr=args.radial_nodes or int(published['radial_nodes']);nt=args.angular_nodes or int(published['angular_nodes'])
    if nr<3 or nt<8 or nt%(2*problem.fold) or args.quadrature_order<1 or args.spectrum_modes<0:
        parser.error('invalid radial/angular grid, quadrature or spectrum dimensions')
    radial=np.linspace(0,problem.seed.length,nr)
    if args.include_breakpoints:
        radial=np.unique(np.r_[radial,problem.seed.length*problem.seed.edges,
                               problem.active_start+problem.entry_length])
    theta=np.arange(nt)*2*np.pi/nt
    result=distribution(problem,state,radial,theta,args.quadrature_order,args.spectrum_modes)
    same_grid=(len(radial)==int(published['radial_nodes']) and nt==int(published['angular_nodes'])
        and not args.include_breakpoints and args.quadrature_order==int(published['radial_center_quadrature_order']))
    output={'schema':'frame-collar-residual-distribution-v1','input_path':str(args.input),
        'input_sha256':hashlib.sha256(raw).hexdigest(),'input_github_sha':report.get('github_sha'),
        'input_github_run_id':report.get('github_run_id'),'identity':identity,
        'evaluation':result,'same_published_grid_and_quadrature':same_grid,
        'published_summary_key':published_key,
        'published_summary_comparison':summary_comparison(result['summary'],published) if same_grid else None,
        'source_files_sha256':hashes,'github_sha':os.environ.get('GITHUB_SHA'),
        'github_run_id':os.environ.get('GITHUB_RUN_ID'),'elapsed_seconds':time.monotonic()-started,
        'optimization_performed':False,'field_parameters_changed':False,'metric_changed':False,
        'all_geometry_claims_are_sampled_only':True,'task_complete':False}
    atomic_save(args.out,output)
    print(json.dumps({'out':str(args.out),'R_argmax':result['global_extrema']['R_norm'],
        'metric_argmax':result['global_extrema']['metric_operator_error'],'task_complete':False}),flush=True)


if __name__=='__main__':main()
