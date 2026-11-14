#!/usr/bin/env python3
"""Query-independent evaluation of the existing exact center-height integral.

This is an evaluator correction, not a change to b0, its source anchor, or g.
Only artificial --check-only inputs are evaluated by this module's CLI.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from frame_independent_height import IndependentHeightProblem
from frame_collar_residual_audit import digest


def fixed_partition(problem, uniform_panels=120):
    """Exact rational partition derived from the immutable height source."""
    count=int(uniform_panels)
    if count<4:raise ValueError('at least four fixed uniform panels required')
    seed=problem.seed;L=seed.length_exact
    tc=L*seed.core_fraction_exact;tf=L*(1-seed.flat_fraction_exact)
    active=tf-tc
    sources={}
    def add(name,values):
        sources[name]=[str(Q(v)) for v in values]
    add('uniform',[L*Q(j,count) for j in range(count+1)])
    edges=[tc];running=tc
    for fraction in seed.fractions_exact:
        running+=active*fraction;edges.append(running)
    add('seed_piece_boundaries',[Q(0),*edges,L])
    radial_free=int(problem.source.radial_free)
    add('immutable_anchor_spline_knots',
        [tc+active*Q(j,radial_free+1) for j in range(radial_free+2)])
    # Published entry correction uses one quarter of the first seed segment.
    add('published_entry_cutoff',[tc+active*seed.fractions_exact[0]/4])
    source=problem.source
    if hasattr(source,'support_exact'):
        h=source.support_exact
        add('natural_patch_cutoff',[tf-h,tf-h*source.plateau_fraction,tf])
    points=sorted({Q(s) for values in sources.values() for s in values})
    if points[0]!=0 or points[-1]!=L or any(x<0 or x>L for x in points):
        raise ValueError('all physical partition nodes must lie in [0,L]')
    return {'schema':'query-independent-height-physical-partition-v1',
        'uniform_panel_count':count,'construction_sources_exact':sources,
        'nodes_exact':[str(x) for x in points],
        'source_height_base_definition_sha256':digest(problem.height_base_definition),
        'partition_is_only_an_evaluation_choice':True,
        'all_queries_use_this_same_prefix_partition':True,
        'query_nodes_do_not_modify_full_panel_integrals':True}


class FixedHeightPrimitive:
    """Prefix panel quadrature plus one partial panel per requested point."""
    def __init__(self,evaluate_b0,partition,order=8):
        self.evaluate_b0=evaluate_b0;self.partition=dict(partition);self.order=int(order)
        if self.order<2:raise ValueError('Gauss order at least two required')
        self.points=np.array([float(Q(x)) for x in partition['nodes_exact']])
        if len(self.points)<2 or self.points[0]!=0 or np.any(np.diff(self.points)<=0):
            raise ValueError('strictly increasing fixed partition anchored at zero required')
        self.gx,self.gw=leggauss(self.order)
        self.prefix=None;self.partial_cache={}

    def _integrals(self,left,right):
        left=np.asarray(left,float);right=np.asarray(right,float)
        middle=(left+right)/2;half=(right-left)/2
        nodes=middle[:,None]+half[:,None]*self.gx[None,:]
        values=np.asarray(self.evaluate_b0(nodes.ravel()),float).reshape(nodes.shape)
        if not np.all(np.isfinite(values)):raise FloatingPointError('nonfinite b0 in fixed primitive')
        return half*np.sum(values*self.gw[None,:],axis=1)

    def _prepare(self):
        if self.prefix is None:
            increments=self._integrals(self.points[:-1],self.points[1:])
            self.prefix=np.r_[0.,np.cumsum(increments)]

    def __call__(self,query):
        t=np.asarray(query,float)
        if np.any(~np.isfinite(t)) or np.any(t<0) or np.any(t>self.points[-1]):
            raise ValueError('finite query points in the physical [0,L] interval required')
        self._prepare();flat=t.ravel();out=np.empty_like(flat)
        missing={}
        for value in np.unique(flat):
            key=float(value).hex()
            if key not in self.partial_cache:
                index=int(np.searchsorted(self.points,value,side='right')-1)
                if index==len(self.points)-1 or value==self.points[index]:
                    self.partial_cache[key]=float(self.prefix[index])
                else:missing[key]=(index,float(value))
        if missing:
            keys=list(missing)
            left=np.array([self.points[missing[key][0]] for key in keys])
            right=np.array([missing[key][1] for key in keys])
            partial=self._integrals(left,right)
            for key,value in zip(keys,partial):
                self.partial_cache[key]=float(self.prefix[missing[key][0]]+value)
        for i,value in enumerate(flat):out[i]=self.partial_cache[float(value).hex()]
        return out.reshape(t.shape)

    def evaluation_definition(self):
        return {'schema':'fixed-prefix-plus-local-height-quadrature-v1',
            'partition':self.partition,'gauss_order_per_full_or_partial_panel':self.order,
            'prefix_anchor':0,'partial_rule':'same fixed panel left endpoint to the individual query',
            'reference_b0_is_not_modified':True,
            'finite_quadrature_not_a_continuous_error_certificate':True}


class FixedPrimitiveProblem:
    """Transparent wrapper: replace only the evaluated common z primitive.

    The old evaluator is retained for comparison. The correction has no free
    parameter dependence, so all six position parameter Jacobians are kept.
    """
    def __init__(self,problem,uniform_panels=120,primitive_order=8):
        self.problem=problem;self.uniform_panels=int(uniform_panels)
        self.primitive_order=int(primitive_order)
        self.partition=fixed_partition(problem,self.uniform_panels)
        self.fixed_primitive=FixedHeightPrimitive(
            lambda t:problem.height_baseline(t)['b0'],self.partition,self.primitive_order)

    def __getattr__(self,name):
        return getattr(self.problem,name)

    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,
                 full_two_jet_jacobian=False):
        data=self.problem.geometry(state,radial,theta,quadrature_order,jacobian=jacobian,
            full_two_jet_jacobian=full_two_jet_jacobian)
        t=np.asarray(radial,float)
        center=(self.port.initial_center_z+self.fixed_primitive(t)+
                self.height_basis.integral(t)@np.asarray(state)[self.slices['height']])
        old_center=data['center'].copy();shift=center-old_center
        data['X']=data['X'].copy()
        data['X'][...,2]=data['metric']['a'][:,None]*data['primitive'][...,2]+center[:,None]
        data['center']=center
        data['height_primitive_evaluation']={
            'old_query_partition_center':old_center,
            'new_fixed_partition_center':center.copy(),
            'new_minus_old_common_vertical_shift':shift,
            'Xs_and_all_other_position_derivatives_unchanged':True,
            'free_parameter_Jacobians_unchanged':True,
            'physical_height_definition_unchanged':True}
        return data

    def direct_residual_and_jacobian(self,state,radial,theta,quadrature_order=4,*,jacobian=True):
        # Call the unmodified formula with this wrapper's geometry dispatch.
        return IndependentHeightProblem.direct_residual_and_jacobian(
            self,state,radial,theta,quadrature_order,jacobian=jacobian)

    def identity(self,state):
        return self.problem.identity(state)

    def evaluation_definition(self):
        result=dict(self.problem.evaluation_definition())
        result['reference_height_integral']='fixed physical partition prefix plus individual local panel integral'
        result['query_independent_height_primitive']=self.fixed_primitive.evaluation_definition()
        return result

    def evaluation_variant(self,state,*,heat_order=None,height_angular_nodes=None,
                           uniform_panels=None,primitive_order=None):
        variant=self.problem.evaluation_variant(state,heat_order=heat_order,
            height_angular_nodes=height_angular_nodes)
        result=FixedPrimitiveProblem(variant,
            self.uniform_panels if uniform_panels is None else uniform_panels,
            self.primitive_order if primitive_order is None else primitive_order)
        if result.identity(state)!=self.identity(state):
            raise ArithmeticError('primitive evaluation refinement changed the physical state')
        return result

    def frozen_metric_copy(self,state):
        frozen,coefficient=self.problem.frozen_metric_copy(state)
        result=FixedPrimitiveProblem(frozen,self.uniform_panels,self.primitive_order)
        if result.identity(coefficient)!=self.identity(state):
            raise ArithmeticError('freezing the metric changed the fixed primitive physical state')
        return result,coefficient


def developer_check():
    # Independent primitive test: a smooth artificial, explicitly integrable b.
    partition={'nodes_exact':[str(Q(j,32)) for j in range(33)],'artificial':True}
    f=lambda t:1+2*t+3*t*t+.2*np.cos(13*t)
    ant=lambda t:t+t*t+t**3+.2*np.sin(13*t)/13
    primitive=FixedHeightPrimitive(f,partition,8)
    sparse=np.array([0.,.17,.63,1.]);dense=np.unique(np.r_[np.linspace(0,1,101),sparse])
    first=primitive(sparse);whole=primitive(dense)
    sparse_dense=float(np.max(abs(first-whole[np.searchsorted(dense,sparse)])))
    shuffled=FixedHeightPrimitive(f,partition,8)
    reversed_values=shuffled(sparse[::-1])[::-1]
    exact_error=float(np.max(abs(whole-ant(dense))))
    h=2e-6;points=np.array([.11,.31,.61,.91])
    derivative_error=float(np.max(abs((primitive(points+h)-primitive(points-h))/(2*h)-f(points))))
    # Full wrapper uses an artificial mild ellipse, never a research report.
    from frame_collar_bvp import FrameCollarProblem,EllipticCylinderPort,NegativeKRadialSeed
    from frame_collar_enriched import make_enriched
    from frame_collar_natural_body_audit import NaturalBodyProblem
    core=EllipticCylinderPort('9/10','18/25','1/50',1)
    seed=NegativeKRadialSeed.from_core(core,'11/10','11/50')
    baseline=FrameCollarProblem(core,seed,radial_free=2,angular_modes=2,
        ellipse_envelope=(core.major,core.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,
        radial_quadrature_order=3)
    old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5')
    c0=.004*np.sin(np.arange(old.nunknown)+.3)
    natural=NaturalBodyProblem(old,c0,metric_free=2,ball_radius='91/100',strip_half_width='1/3',
        amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9'],radial_nodes=9,
        angular_nodes=24,quadrature_order=3,heat_order=8)
    base=IndependentHeightProblem(natural,3,height_angular_nodes=24)
    state=base.initial_state();state[base.slices['height']]=[.003,-.002,.001]
    state[base.slices['metric']]=[.003,-.004]
    wrapped=FixedPrimitiveProblem(base,16,4)
    tc,tf=base.height_basis.left,base.height_basis.right
    coarse=np.array([0.,tc,tf,seed.length]);fine=np.unique(np.r_[np.linspace(0,seed.length,17),coarse])
    theta=np.arange(24)*2*np.pi/24
    a=wrapped.geometry(state,coarse,theta,3,jacobian=True,full_two_jet_jacobian=True)
    b=wrapped.geometry(state,fine,theta,3,jacobian=True,full_two_jet_jacobian=True)
    indices=np.searchsorted(fine,coarse)
    query_jet_errors={key:float(np.max(abs(a[key]-b[key][indices])))
                      for key in ['X','Xs','Xt','Xss','Xst','Xtt']}
    old_a=base.geometry(state,coarse,theta,3,jacobian=True,full_two_jet_jacobian=True)
    derivative_unchanged={key:float(np.max(abs(a[key]-old_a[key])))
                          for key in ['Xs','Xt','Xss','Xst','Xtt']}
    jac_unchanged=max(float(np.max(abs(a['jac_'+key]-old_a['jac_'+key])))
                      for key in ['X','Xs','Xt','Xss','Xst','Xtt'])
    direction=np.sin(np.arange(base.nunknown)+.7);direction/=np.linalg.norm(direction)
    step=2e-7
    rr,J,_=wrapped.direct_residual_and_jacobian(state,fine,theta,3)
    plus=wrapped.direct_residual_and_jacobian(state+step*direction,fine,theta,3,jacobian=False)[0]
    minus=wrapped.direct_residual_and_jacobian(state-step*direction,fine,theta,3,jacobian=False)[0]
    fd=(plus-minus)/(2*step)
    jac_error=float(np.linalg.norm(fd-J@direction)/max(1e-30,np.linalg.norm(fd)))
    frozen,fc=wrapped.frozen_metric_copy(state);replay=frozen.geometry(fc,fine,theta,3)
    freeze=max(float(np.max(abs(replay[key]-b[key]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt'])
    refined=wrapped.evaluation_variant(state,uniform_panels=32,primitive_order=6)
    same_identity=base.identity(state)==wrapped.identity(state)==refined.identity(state)==frozen.identity(fc)
    result={'schema':'fixed-height-primitive-artificial-check-v1',
        'artificial_inputs_only':True,'research_geometry_evaluated':False,
        'primitive_sparse_dense_difference':sparse_dense,
        'primitive_query_order_difference':float(np.max(abs(first-reversed_values))),
        'primitive_exact_function_error':exact_error,'primitive_derivative_error':derivative_error,
        'full_wrapper_sparse_dense_position_two_jet_errors':query_jet_errors,
        'unchanged_nonposition_derivatives':derivative_unchanged,
        'unchanged_position_parameter_Jacobians_error':jac_unchanged,
        'direct_metric_shape_directional_Jacobian_error':jac_error,
        'same_physical_identity_under_evaluator_change_and_metric_freeze':same_identity,
        'frozen_metric_position_two_jet_replay_error':freeze,
        'artificial_old_new_sparse_common_height_difference':float(a['center'][-1]-old_a['center'][-1]),
        'finite_checks_are_not_continuous_error_certificates':True}
    result['passed']=bool(sparse_dense==0 and result['primitive_query_order_difference']==0
        and exact_error<1e-13 and derivative_error<1e-8 and max(query_jet_errors.values())<1e-12
        and max(derivative_unchanged.values())==0 and jac_unchanged==0 and jac_error<3e-5
        and same_identity and freeze<1e-12)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true',required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    result=developer_check();result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
