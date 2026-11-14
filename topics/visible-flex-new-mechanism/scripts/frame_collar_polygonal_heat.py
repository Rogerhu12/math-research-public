#!/usr/bin/env python3
"""Fixed-g six-cap pilot with an infinite-Gaussian compact base definition.

All research evaluation and optimization runs only in the public Actions.
Gauss-Hermite order is an evaluation choice, never part of the physical field.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.optimize import least_squares

from polygonal_flat_tail_port import PolygonalFlatTail,s9_derivative
from polygonal_tail_heat_extension import GaussianPolygonalExtension
from frame_collar_polygonal import (CompactPolygonalGrid,CompactPolygonalProblem,reflected_tail_jets,
    source_prefix_comparison,current_audit,implementation_hashes as compact_hashes)
from frame_collar_bent_tail import (load_enriched_report,readonly_old_replay,artificial_enriched_report,ball_strip_values)
from frame_collar_enriched import make_enriched
from frame_collar_bvp import (EllipticCylinderPort,NegativeKRadialSeed,FrameCollarProblem,radial_quadrature,
    primitive_gauss_audit,atomic_save,smooth_positive,periodic_operator)
from frame_collar_residual_audit import digest,distribution,extremum


def implementation_hashes(extra_source_files=()):
    out=compact_hashes()
    for name in ['polygonal_tail_heat_extension.py',Path(__file__).name,*extra_source_files]:
        out[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return out


def heat_rows(extension,radial,theta,order,maximum_base_points=16384):
    """Bound temporary GH arrays without changing the quadrature at any point."""
    radial=np.asarray(radial,float);theta=np.asarray(theta,float)
    if not len(radial) or not len(theta):raise ValueError('nonempty heat sample arrays required')
    row_count=max(1,int(maximum_base_points)//len(theta));pieces=[]
    for start in range(0,len(radial),row_count):
        pieces.append(extension.evaluate(radial[start:start+row_count],theta,order))
    return {name:{key:np.concatenate([part[name][key] for part in pieces],axis=0)
        for key in ['value','s','ss','theta','st','ss_theta']} for name in ['u','v','beta']}


class GaussianPolygonalGrid(CompactPolygonalGrid):
    def __init__(self,problem,radial,theta):
        super().__init__(problem,radial,theta)
        selected=(self.radial>problem.support_start)&(self.radial<problem.active_end)
        if not np.any(selected):return
        radius=self.radial[selected]
        old=reflected_tail_jets(problem,radius,self.theta)
        heat=heat_rows(problem.heat_extension,radius,self.theta,problem.heat_order)
        x=(problem.active_end-radius)/problem.support_width
        chi=1-s9_derivative(x);cp=s9_derivative(x,1)/problem.support_width
        cpp=-s9_derivative(x,2)/problem.support_width**2
        for name in ['u','v','beta']:
            difference={key:heat[name][key]-old[name][key] for key in ['value','s','ss','theta','st','ss_theta']}
            self.base[name]['value'][selected]+=chi[:,None]*difference['value']
            self.base[name]['s'][selected]+=cp[:,None]*difference['value']+chi[:,None]*difference['s']
            self.base[name]['ss'][selected]+=cpp[:,None]*difference['value']+2*cp[:,None]*difference['s']+chi[:,None]*difference['ss']
            self.base[name]['theta'][selected]+=chi[:,None]*difference['theta']
            self.base_cross[name]['st'][selected]+=cp[:,None]*difference['theta']+chi[:,None]*difference['st']
            self.base_cross[name]['ss_theta'][selected]+=cpp[:,None]*difference['theta']+2*cp[:,None]*difference['st']+chi[:,None]*difference['ss_theta']


class GaussianPolygonalProblem(CompactPolygonalProblem):
    def __init__(self,old,source_state,support_width='1/10',ball_radius='101/100',strip_half_width='19/50',
                 amplitudes=('3/16','1/8','1/8','3/16','1/8','1/8'),
                 radial_nodes=61,angular_nodes=192,quadrature_order=4,heat_order=32,tau0='1/128',
                 extension_factory=GaussianPolygonalExtension):
        self.heat_order=int(heat_order)
        if not 4<=self.heat_order<=128:raise ValueError('primary GH order must lie in [4,128] to permit doubling')
        outer=old.seed.cut_radius_exact+old.seed.length_exact*old.seed.flat_fraction_exact
        tail=PolygonalFlatTail(outer,old.seed.cut_radius_exact,amplitudes,old.port.side)
        self.heat_extension=extension_factory(tail,old.seed,support_width,tau0)
        # The inherited initializer builds intermediate old grids. Do not pay
        # heat quadrature for them; only the final exact nonuniform grid is used.
        self._heat_live=False
        super().__init__(old,source_state,support_width,ball_radius,strip_half_width,amplitudes,
            radial_nodes,angular_nodes,quadrature_order)
        if self.heat_extension.tail.identity!=self.tail.identity:raise ArithmeticError('two tail identities disagree')
        self._heat_live=True;self._rebuild_evaluation_grids()

    def _rebuild_evaluation_grids(self):
        self._grids={};self._cache=None;self.grid=self.grid_for(self.radial,self.theta)
        qnodes,self.quad_weights=radial_quadrature(self.radial,self.radial_quadrature_order)
        self.quad_grid=self.grid_for(qnodes,self.theta)

    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:
            cls=GaussianPolygonalGrid if self._heat_live else CompactPolygonalGrid
            self._grids[key]=cls(self,radial,theta)
        return self._grids[key]

    def space_definition(self):
        out=CompactPolygonalProblem.space_definition(self)
        out.update(schema='infinite-Gaussian-six-cap-frame-space-v1',
            compact_correction='chi*(flat+infinite_Gaussian_heat(E)(t,theta)-f_old(c0))',
            reflected_extension='the source E of the complete infinite Gaussian heat operator',
            heat_extension_identity_sha256=self.heat_extension.identity_sha256,
            finite_GH_order_not_part_of_the_exact_space=True)
        return out

    def model_definition(self):
        out=CompactPolygonalProblem.model_definition(self)
        out.update(schema='infinite-Gaussian-six-cap-connector-model-v1',
            heat_extension_identity=self.heat_extension.identity,
            heat_extension_identity_sha256=self.heat_extension.identity_sha256,
            angle_analyticity_refers_to_infinite_operator_not_finite_GH=True,
            original_reflection_model_is_not_this_continuous_model=True)
        return out

    def evaluation_definition(self):
        return {'schema':'Gaussian-six-cap-evaluation-v1','GH_order':self.heat_order,
            'Gaussian_nodes':'standard-normal probabilists GH; eight-node batches',
            'maximum_base_radial_angle_points_per_heat_call':16384,
            'radial_row_chunking_changes_neither_nodes_nor_pointwise_formula':True,
            'finite_GH_is_only_an_approximation':True,
            'radial_center_quadrature_order':self.radial_quadrature_order,
            'collocation_radial_count':len(self.radial),'collocation_angle_count':len(self.theta),
            'GH_refinement_and_Pi_angle_refinement_are_separate':True}

    def identity_bundle(self,state):
        return {'model':self.model_definition(),'space':self.space_definition(),
            'anchor':self.anchor_definition,'heat':self.heat_extension.identity,
            'metric':self.metric_model(state),'tail':self.tail.identity,
            'core':self.port.identity,'port':self.port.port_identity,
            'exact_coefficients':[str(Q.from_float(float(x))) for x in state]}

    def evaluation_variant(self,order,state):
        if not 4<=int(order)<=256:raise ValueError('GH comparison order outside [4,256]')
        variant=copy.copy(self);variant.heat_order=int(order);variant._rebuild_evaluation_grids()
        if self.identity_bundle(state)!=variant.identity_bundle(state):
            raise ArithmeticError('GH evaluation refinement changed the mathematical model or coefficients')
        return variant


def cost_from_geometry(problem,grid,data):
    count=len(grid.radial)*len(grid.theta)
    cost=float(np.sum(data['R']**2)/(2*count))
    X=data['X']
    if problem.shape_weight>0:
        for value in [np.sum(X*X,axis=-1)/problem.ball_radius**2-1,
            X[...,1]/problem.strip_half_width-1,-X[...,1]/problem.strip_half_width-1]:
            positive=smooth_positive(value)[0]
            cost+=float(problem.shape_weight**2*np.sum(positive*positive)/(2*count))
    return cost


def compare_heat_evaluation(problem,state,variant,radial=None,theta=None,quadrature_order=None):
    radial=problem.radial if radial is None else np.asarray(radial,float)
    theta=problem.theta if theta is None else np.asarray(theta,float)
    quadrature_order=problem.radial_quadrature_order if quadrature_order is None else quadrature_order
    if problem.identity_bundle(state)!=variant.identity_bundle(state):
        raise ArithmeticError('GH comparison lacks identical full physical identities')
    grids=[p.grid_for(radial,theta) for p in [problem,variant]]
    data=[p.geometry(state,g,quadrature_order=quadrature_order) for p,g in zip([problem,variant],grids)]
    fields=[g.full_scalar_jets(state) for g in grids]
    patch=(radial>=problem.support_start)&(radial<=problem.active_end)
    keys=['value','s','ss','theta','st','ss_theta']
    differences={key:max(float(np.max(abs(fields[0][name][key][patch]-fields[1][name][key][patch])))
        for name in ['u','v','beta']) for key in keys}
    positions={key:float(np.max(np.linalg.norm(data[0][key]-data[1][key],axis=-1)))
        for key in ['X','Xs','Xt','Xss','Xst','Xtt','R']}
    rows=[]
    for i in np.flatnonzero(patch):
        rows.append({'t':float(radial[i]),'delta':float(problem.active_end-radial[i]),
            'first_scalar_jet_difference':max(float(np.max(abs(fields[0][name][key][i]-fields[1][name][key][i])))
                for name in ['u','v','beta'] for key in ['value','s','theta']),
            'ss_scalar_difference':max(float(np.max(abs(fields[0][name]['ss'][i]-fields[1][name]['ss'][i]))) for name in ['u','v','beta']),
            'R_difference':float(np.max(np.linalg.norm(data[0]['R'][i]-data[1]['R'][i],axis=-1)))})
    return {'GH_orders':[problem.heat_order,variant.heat_order],
        'all_full_physical_identities_and_exact_coefficients_equal':True,
        'identity_bundle_sha256':digest(problem.identity_bundle(state)),
        'radial_nodes':len(radial),'angular_nodes':len(theta),'radial_center_quadrature_order':quadrature_order,
        'only_GH_evaluation_order_changed':True,
        'objective_costs_at_the_same_fixed_coefficients_and_grid':[
            cost_from_geometry(p,g,d) for p,g,d in zip([problem,variant],grids,data)],
        'patch_scalar_jet_max_differences':differences,'whole_grid_position_jet_and_R_differences':positions,
        'patch_rows':rows,'differences_are_not_continuous_error_bounds':True,
        'GH_cost_difference_is_not_optimization_improvement':True}


def developer_check(extension_factory=GaussianPolygonalExtension):
    rows=[]
    for side in [1,-1]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
        baseline=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
            ellipse_envelope=(port.major,port.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
        bs=.006*np.cos(np.arange(baseline.nunknown));old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5')
        c0=.009*np.sin(np.arange(old.nunknown)+.2)
        old,c0,_=load_enriched_report(artificial_enriched_report(old,c0,baseline,bs))
        problem=GaussianPolygonalProblem(old,c0,ball_radius='91/100',strip_half_width='1/3',
            amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9'],radial_nodes=9,angular_nodes=24,quadrature_order=3,heat_order=16,
            extension_factory=extension_factory)
        rng=np.random.default_rng(831+side);state=c0+.003*rng.standard_normal(problem.nunknown)
        direction=rng.standard_normal(problem.nunknown);direction/=np.linalg.norm(direction);h=2e-7
        rr,jj,data=problem.residual_and_jacobian(state)
        fd=(problem.residual(state+h*direction)-problem.residual(state-h*direction))/(2*h)
        jac_error=float(np.linalg.norm(fd-jj@direction)/max(1e-30,np.linalg.norm(fd)))
        prefix=source_prefix_comparison(old,c0,problem,c0)
        independent_cost=cost_from_geometry(problem,problem.grid,data)
        cost_error=abs(independent_cost-float(np.dot(rr,rr)/2))
        variant=problem.evaluation_variant(32,state)
        comparison=compare_heat_evaluation(problem,state,variant)
        patch=problem.radial[(problem.radial>problem.support_start)&(problem.radial<problem.active_end)]
        full=heat_rows(problem.heat_extension,patch,problem.theta,16)
        chunked=heat_rows(problem.heat_extension,patch,problem.theta,16,maximum_base_points=len(problem.theta))
        chunk_error=max(float(np.max(abs(full[name][key]-chunked[name][key])))
            for name in ['u','v','beta'] for key in full[name])
        audit=current_audit(problem,state,problem.grid,data,3)
        core_refinement=[]
        for count in [24,48,96]:
            angles=np.arange(count)*2*np.pi/count;core_grid=problem.grid_for(np.array([0.]),angles)
            frame=problem.frame(state,core_grid)
            reconstructed=problem.port.a0*periodic_operator(frame['T'],-1)[0]
            reconstructed[:,2]+=problem.port.initial_center_z
            target=problem.port.position_jets(0.,angles)['X']
            core_refinement.append({'angular_nodes':count,
                'core_X_error':float(np.max(np.linalg.norm(reconstructed-target,axis=-1))),
                'same_core_same_field_coefficients_no_reoptimization':True,
                'no_heat_extension_evaluated_at_the_core':True})
        rows.append({'side':side,'unknowns':problem.nunknown,'full_parameter_Jacobian_relative_error':jac_error,
            'independent_objective_cost_difference':cost_error,'same_prefix_replay':prefix,
            'GH_evaluation_comparison':comparison,
            'row_chunking_fixed_query_difference':chunk_error,
            'position_two_jet_endpoint_errors':audit['position_two_jet_endpoint_errors'],
            'core_Pi_angle_refinement':core_refinement,
            'tail_R_max_sample':audit['exact_cap_comparison']['tail_R_max_sample'],
            'model_hash_independent_of_GH_order':digest(problem.model_definition())==digest(variant.model_definition())})
    passed=all(row['full_parameter_Jacobian_relative_error']<3e-5 and row['independent_objective_cost_difference']<1e-10
        and max(row['same_prefix_replay']['prefix_position_jet_and_R_differences'].values())<1e-10
        and row['same_prefix_replay']['metric_full_identity_equal'] and row['same_prefix_replay']['metric_evaluation_bitwise']
        and row['model_hash_independent_of_GH_order']
        and row['row_chunking_fixed_query_difference']<1e-10
        and max(x for end,part in row['position_two_jet_endpoint_errors'].items() for jet,x in part.items()
                if (end,jet)!=('core','X'))<1e-8
        and row['core_Pi_angle_refinement'][-1]['core_X_error']<1e-8
        and row['core_Pi_angle_refinement'][-1]['core_X_error']<row['core_Pi_angle_refinement'][0]['core_X_error']
        and row['tail_R_max_sample']<1e-10 for row in rows)
    return {'schema':'Gaussian-six-cap-frame-development-v1','checks':rows,'passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False,
        'passed_does_not_certify_GH_accuracy_or_geometric_feasibility':True}


def main(*,extension_factory=GaussianPolygonalExtension,extra_source_files=(),model_label='raw-reflection-Gaussian'):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--support-width',default='1/10');parser.add_argument('--tau0',default='1/128')
    parser.add_argument('--heat-order',type=int,choices=[32],default=32,
        help='this pilot starts at 32 and may deterministically select 64 after a 128 comparison')
    parser.add_argument('--initial-cost-limit',default='1')
    parser.add_argument('--initial-heat-first-jet-limit',default='1/10000')
    parser.add_argument('--radial-nodes',type=int,default=61);parser.add_argument('--angular-nodes',type=int,default=192)
    parser.add_argument('--quadrature-order',type=int,default=4)
    parser.add_argument('--audit-radial-nodes',type=int,default=121);parser.add_argument('--audit-angular-nodes',type=int,default=384)
    parser.add_argument('--ball-radius',default='101/100');parser.add_argument('--strip-half-width',default='19/50')
    parser.add_argument('--field-bound',type=float,default=8.);parser.add_argument('--max-nfev',type=int,default=250)
    parser.add_argument('--checkpoint-every',type=int,default=10);parser.add_argument('--checkpoint-seconds',type=float,default=60.)
    parser.add_argument('--check-only',action='store_true');args=parser.parse_args()
    started=time.monotonic();hashes=implementation_hashes(extra_source_files)
    if args.check_only:
        output=developer_check(extension_factory);output['source_files_sha256']=hashes
        output['model_variant_label']=model_label;atomic_save(args.out,output)
        print(json.dumps({'out':str(args.out),'passed':output['passed']}),flush=True)
        if not output['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        parser.error('research replay, quadrature comparison and optimization require this public repository Actions')
    if not args.input:parser.error('--input is required')
    repo=Path(__file__).resolve().parents[3];allowed=[repo/'topics'/'visible-flex-new-mechanism'/'notes']
    if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']))
    if not any(args.input.resolve().is_relative_to(root.resolve()) for root in allowed):parser.error('input must be a public note or Actions temporary output')
    if min(args.radial_nodes-8,args.quadrature_order,args.max_nfev,args.field_bound,args.checkpoint_every)<=0:
        parser.error('invalid positive dimensions')
    if min(args.angular_nodes,args.audit_angular_nodes)<4 or args.angular_nodes%4 or args.audit_angular_nodes%4 or args.audit_radial_nodes<args.radial_nodes or args.audit_angular_nodes<args.angular_nodes:
        parser.error('invalid twofold grid or audit resolution')
    cost_limit=Q(args.initial_cost_limit);heat_limit=Q(args.initial_heat_first_jet_limit)
    if min(cost_limit,heat_limit)<=0:parser.error('positive engineering budget limits required')
    raw=args.input.read_bytes();report=json.loads(raw);old,initial,input_identity=load_enriched_report(report)
    problem=GaussianPolygonalProblem(old,initial,args.support_width,args.ball_radius,args.strip_half_width,
        radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes,quadrature_order=args.quadrature_order,
        heat_order=args.heat_order,tau0=args.tau0,extension_factory=extension_factory)
    if np.max(abs(initial))>=args.field_bound:parser.error('source coefficients meet the bound; no clipping is allowed')
    prefix=source_prefix_comparison(old,initial,problem,initial)
    if max(prefix['prefix_position_jet_and_R_differences'].values())>1e-8 or not prefix['metric_evaluation_bitwise'] or not prefix['metric_full_identity_equal']:
        raise ArithmeticError('heat base altered the supposedly fixed prefix or metric')
    fine_radial=np.linspace(0,problem.seed.length,args.audit_radial_nodes)
    double_theta=np.arange(2*args.audit_angular_nodes)*np.pi/args.audit_angular_nodes
    old_replay=readonly_old_replay(old,initial,report,problem,fine_radial,double_theta)
    old_replay.update(source_path=str(args.input),source_sha256=hashlib.sha256(raw).hexdigest(),source_identity=input_identity)
    atomic_save(args.out.with_name(args.out.stem+'-old-ball-replay.json'),old_replay)
    higher=problem.evaluation_variant(64,initial)
    first_pair=compare_heat_evaluation(problem,initial,higher)
    first_difference=max(first_pair['patch_scalar_jet_max_differences'][key] for key in ['value','s','theta'])
    comparisons=[first_pair];heat_accepted=bool(first_difference<=float(heat_limit))
    if not heat_accepted:
        third=problem.evaluation_variant(128,initial)
        second_pair=compare_heat_evaluation(higher,initial,third)
        comparisons.append(second_pair)
        first_difference=max(second_pair['patch_scalar_jet_max_differences'][key] for key in ['value','s','theta'])
        heat_accepted=bool(first_difference<=float(heat_limit))
        # At most one additional refinement. If it fails, retain the 64/128
        # fixed-parameter diagnostics and never start a nonlinear solve.
        problem,higher=higher,third
    initial_heat={'schema':'deterministic-initial-GH-evaluation-selection-v1',
        'rule':'32/64 first jets <= limit selects 32; otherwise compare 64/128 and select 64 if passed; otherwise no optimization',
        'first_jet_limit_exact':str(heat_limit),'comparisons':comparisons,
        'selected_order_for_optimization':problem.heat_order if heat_accepted else None,
        'order_for_saved_diagnostics':problem.heat_order,
        'heat_evaluation_accepted':heat_accepted,
        'all_comparisons_hold_exact_model_space_metric_anchor_heat_and_coefficients_fixed':True,
        'second_jet_differences_saved_without_claiming_a_curvature_certificate':True}
    atomic_save(args.out.with_name(args.out.stem+'-initial-heat-comparison.json'),initial_heat)
    residual,jac,initial_data=problem.residual_and_jacobian(initial)
    initial_cost=float(np.dot(residual,residual)/2)
    initial_audit=current_audit(problem,initial,problem.grid,initial_data,args.quadrature_order)
    gate={'cost_limit_exact':str(cost_limit),'initial_cost':initial_cost,
        'heat_first_jet_limit_exact':str(heat_limit),'heat_first_jet_difference':first_difference,
        'cost_accepted':bool(initial_cost<=float(cost_limit)),
        'heat_evaluation_accepted':heat_accepted,
        'selected_GH_order_for_optimization':problem.heat_order if heat_accepted else None,
        'accepted':bool(initial_cost<=float(cost_limit) and heat_accepted),
        'engineering_budget_not_a_mathematical_infeasibility_test':True,
        'failure_saves_fixed_parameter_diagnostics_and_skips_optimization':True}
    model=problem.model_definition();space=problem.space_definition();model_hash=digest(model)
    config={key:str(value) if isinstance(value,Path) else value for key,value in vars(args).items()}
    config['model_variant_label']=model_label
    best={'cost':initial_cost,'state':np.array(initial,copy=True)};history=[];evaluation_count=[0];last_save=[0.]
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    source_record={key:report[key] for key in ['schema','source_files_sha256','configuration','space_definition',
        'space_definition_sha256','core_physical_identity','core_physical_identity_sha256','port_identity','port_identity_sha256',
        'metric_model','metric_is_frozen','exact_field_coefficients','field_coefficients_binary64','field_unknown_count','angular_counts',
        'original_model_record','shape_budget','shape_budget_sha256','mathematical_state','mathematical_state_sha256']}

    def payload(state,status,final=False):
        data=problem.residual_and_jacobian(state)[2]
        coefficients=[str(Q.from_float(float(x))) for x in state]
        mathematical={'model_definition_sha256':model_hash,'exact_field_coefficients':coefficients}
        out={'schema':'Gaussian-six-cap-frame-collar-v1','status':status,'configuration':config,
            'model_variant_label':model_label,
            'full_model_definition':model,'full_model_definition_sha256':model_hash,
            'space_definition':space,'space_definition_sha256':digest(space),
            'heat_extension_identity':problem.heat_extension.identity,'heat_extension_identity_sha256':problem.heat_extension.identity_sha256,
            'evaluation_definition':problem.evaluation_definition(),
            'sampling_definition':problem.sampling_definition,'sampling_definition_sha256':digest(problem.sampling_definition),
            'tail_physical_identity':problem.tail.identity,'tail_physical_identity_sha256':problem.tail.identity_sha256,
            'core_physical_identity':problem.port.identity,'core_physical_identity_sha256':problem.port.identity_sha256,
            'port_identity':problem.port.port_identity,'port_identity_sha256':problem.port.port_identity_sha256,
            'metric_model':problem.metric_model(state),'metric_is_frozen':True,
            'base_anchor_definition':problem.anchor_definition,'base_anchor_definition_sha256':digest(problem.anchor_definition),
            'exact_field_coefficients':coefficients,'field_coefficients_binary64':state.tolist(),
            'mathematical_state':mathematical,'mathematical_state_sha256':digest(mathematical),
            'field_unknown_count':problem.nunknown,'angular_counts':problem.angular_counts,
            'original_enriched_model_record':source_record,
            'warm_source':{'path':str(args.input),'sha256':hashlib.sha256(raw).hexdigest(),'identity':input_identity,
                'github_sha':report.get('github_sha'),'github_run_id':report.get('github_run_id')},
            'same_grid_untouched_prefix_replay':prefix,'read_only_old_ball_replay':old_replay,
            'initial_new_collocation_audit':initial_audit,'initial_new_objective_cost':initial_cost,
            'initial_fixed_parameter_heat_comparison':initial_heat,'initial_engineering_gate':gate,
            'shape_budget':problem.shape_definition(),'shape_budget_sha256':digest(problem.shape_definition()),
            'collocation_audit':current_audit(problem,state,problem.grid,data,args.quadrature_order),
            'objective_decrease_only_compares_the_same_fixed_GH_evaluator':True,
            'source_and_new_objective_costs_not_directly_comparable':True,
            'evaluations_seen':evaluation_count[0],'history':history,'elapsed_seconds':time.monotonic()-started,
            'source_files_sha256':hashes,'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'peak_rss_kib_linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None,
            'source_c0_is_original_enriched_not_failed_bent_state':True,
            'finite_GH_is_not_the_physical_field_definition':True,
            'same_fixed_metric':True,'different_physical_tail_and_heat_base':True,
            'continuous_heat_evaluation_error_certified':False,'continuous_metric_certificate':False,
            'embedding_proved':False,'whole_surface_reach_proved':False,'closed_surface_constructed':False,'task_complete':False}
        if final:
            theta=np.arange(args.audit_angular_nodes)*2*np.pi/args.audit_angular_nodes
            grid=problem.grid_for(fine_radial,theta);d0=problem.geometry(state,grid,quadrature_order=8)
            doubled=problem.grid_for(fine_radial,double_theta);d1=problem.geometry(state,doubled,quadrature_order=8)
            out['fixed_parameter_audit']=current_audit(problem,state,grid,d0,8)
            out['fixed_parameter_double_angle_audit']=current_audit(problem,state,doubled,d1,8)
            out['Pi_angle_refinement_position_difference_max']=float(np.max(np.linalg.norm(d0['X']-d1['X'][:,::2],axis=-1)))
            out['Pi_angle_refinement_holds_GH_order_fixed']=problem.heat_order
            out['final_fixed_parameter_GH_comparison']=compare_heat_evaluation(problem,state,higher,fine_radial,theta,8)
            extra=np.unique(np.r_[fine_radial,problem.support_start,problem.active_start,problem.active_end,
                np.linspace(problem.support_start,problem.active_end,13),problem.seed.length*problem.seed.edges])
            eg=problem.grid_for(extra,double_theta);ed=problem.geometry(state,eg,quadrature_order=8)
            out['patch_and_breakpoint_audit']={'radial_nodes':len(extra),'angular_nodes':len(double_theta),
                'audit':current_audit(problem,state,eg,ed,8),'fixed_field_not_reoptimized':True}
            out['primitive_gauss_crosscheck']=primitive_gauss_audit(problem,state,args.audit_angular_nodes)
            dist=distribution(problem,state,fine_radial,theta,quadrature_order=8,spectrum_modes=16)
            dist['active_shape_budget']=problem.shape_definition()
            values=ball_strip_values(d0,problem.ball_radius,problem.strip_half_width)
            dist['current_shape_global_extrema']={key:extremum(value,grid) for key,value in values.items()}
            dist['legacy_ellipse_and_height_not_active_constraints']=True;out['residual_distribution']=dist
        return out

    atomic_save(checkpoint,payload(initial,'initial_heat_candidate_before_budget_decision'))
    print(json.dumps({'initial_engineering_gate':gate,'initial_GH_comparison':initial_heat}),flush=True)
    if not gate['accepted']:
        output=payload(initial,'initial_heat_engineering_gate_rejected',True)
        output['optimization_skipped']=True;output['solver']=None
        atomic_save(args.out,output);atomic_save(checkpoint,output)
        print(json.dumps({'out':str(args.out),'optimization_skipped':True,'task_complete':False}),flush=True);return

    def objective(state):
        rr,_,_=problem.residual_and_jacobian(state);evaluation_count[0]+=1
        cost=float(np.dot(rr,rr)/2)
        if cost<best['cost']:best.update(cost=cost,state=np.array(state,copy=True))
        now=time.monotonic()
        if evaluation_count[0]==1 or evaluation_count[0]%args.checkpoint_every==0 or now-last_save[0]>=args.checkpoint_seconds:
            selected=best['state'];audit=current_audit(problem,selected,problem.grid,
                problem.residual_and_jacobian(selected)[2],args.quadrature_order)
            row={'evaluation':evaluation_count[0],'selected_cost_same_GH_order':best['cost'],'GH_order':problem.heat_order,
                'R_max_sample':audit['integrability_residual_max_sample'],'metric_error_sample':audit['metric_relative_operator_error_max_sample'],
                'area_min_sample':audit['minimum_area_sample'],'curvature_max_sample':audit['principal_curvature_absolute_max_sample'],
                'ball_violation_sample':audit['ball_radius_squared_normalized_positive_violation_sample'],
                'strip_violation_sample':audit['strip_abs_normalized_positive_violation_sample'],'seconds':now-started}
            history.append(row);atomic_save(checkpoint,payload(selected,'checkpoint_Gaussian_six_cap_candidate'))
            print(json.dumps(row),flush=True);last_save[0]=now
        return rr

    result=least_squares(objective,initial,jac=problem.jacobian,bounds=(-args.field_bound,args.field_bound),
        x_scale='jac',max_nfev=args.max_nfev,ftol=1e-11,xtol=1e-11,gtol=1e-11,method='trf')
    objective(result.x);output=payload(best['state'],'finite_Gaussian_six_cap_candidate',True)
    output['optimization_skipped']=False
    output['solver']={'success':bool(result.success),'message':str(result.message),'status':int(result.status),
        'nfev':int(result.nfev),'njev':int(result.njev) if result.njev is not None else None,
        'cost':float(result.cost),'selected_cost':best['cost'],'optimality':float(result.optimality),
        'termination_success_is_not_geometric_feasibility':True}
    output['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform.startswith('linux') else None
    atomic_save(args.out,output);atomic_save(checkpoint,output)
    print(json.dumps({'out':str(args.out),'audit':output['fixed_parameter_double_angle_audit'],'task_complete':False}),flush=True)


if __name__=='__main__':main()
