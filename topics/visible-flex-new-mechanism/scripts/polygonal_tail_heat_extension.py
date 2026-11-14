#!/usr/bin/env python3
"""Infinite Gaussian heat extension; Gauss-Hermite is only an evaluator.

The exact periodic heat operator is applied to the C2 reflected scalar cap.
For each positive delta its mathematical angular field is analytic. A finite
Gauss-Hermite sum is only C4 and is never the physical definition. The CLI
checks artificial interfaces and does not evaluate a research candidate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite_e import hermegauss

from bent_flat_tail_port import Jet22,digest,exact
from polygonal_flat_tail_port import PolygonalFlatTail


JET_KEYS=('value','s','ss','theta','st','tt','ss_theta','ss_thetatheta')


@lru_cache(maxsize=16)
def gaussian_rule(order):
    """Positive probabilists' GH rule for standard normal expectation."""
    order=int(order)
    if order<4 or order>256:raise ValueError('Gaussian evaluation order must lie in [4,256]')
    nodes,weights=hermegauss(order)
    weights=weights/np.sum(weights)
    if not np.all(np.isfinite(nodes)) or not np.all(np.isfinite(weights)) or not np.all(weights>0):
        raise ArithmeticError('invalid finite Gaussian rule')
    nodes.setflags(write=False);weights.setflags(write=False)
    return nodes,weights


def coordinate_jet(value,s=0.,ss=0.,theta=0.):
    answer=Jet22.constant(value)
    answer.c[1,0]=s;answer.c[2,0]=np.asarray(ss)/2;answer.c[0,1]=theta
    return answer


def exact_metric_definition(seed):
    source=seed.frozen_definition
    source=source() if callable(source) else source
    answer={key:value for key,value in source.items() if key!='numerical_evaluation'}
    if 'a0_source' in answer:
        answer['a0_source']={key:value for key,value in answer['a0_source'].items()
            if key!='numerical_a0_for_evaluation'}
    return answer


def cap_increment_composition(tail,radius,angle):
    """Evaluate the same exact source cap with arbitrary Jet22 coordinates.

    This is composition, not a new exterior cap formula. Only radius values in
    the disjoint closed source disk are read. beta is its real-lift increment.
    """
    tail._domain(radius.c[0,0])
    cosine,sine=angle.cos(),angle.sin()
    zero=np.zeros_like(radius.c[0,0]);u=Jet22.constant(zero);v=Jet22.constant(zero)
    beta_delta=Jet22.constant(zero)
    for j,normal in enumerate(tail.normals):
        a=cosine*normal[0]+sine*normal[1];b=-sine*normal[0]+cosine*normal[1]
        excess=radius*a-tail.offset
        if not np.any(excess.c[0,0]>0):continue
        alpha=excess.compose(tail.alpha_jets(j,excess.c[0,0],4));C,S=alpha.cos(),alpha.sin()
        u=u+((1-C)*a*b/(1-(1-C)*b*b)).atan()
        v=v-tail.side*b*S/(1-b*b*S*S).sqrt()
        beta_delta=beta_delta+tail.side*(a*S/C).atan()
    return {'u':u,'v':v,'beta':beta_delta}


def gaussian_jet_expectation(callback,order,shape):
    """Stream one GH node at a time, keeping arrays independent of GH order."""
    nodes,weights=gaussian_rule(order)
    accumulated={name:np.zeros((3,3)+tuple(shape)) for name in ['u','v','beta']}
    for node,weight in zip(nodes,weights):
        values=callback(float(node))
        for name in accumulated:accumulated[name]+=float(weight)*values[name].c
    return {name:Jet22(value) for name,value in accumulated.items()}


class GaussianPolygonalExtension:
    def __init__(self,tail,seed,support_width='1/10',tau0='1/128'):
        self.tail=tail;self.seed=seed
        self.support_exact=exact(support_width);self.tau0_exact=exact(tau0)
        if self.support_exact<=0 or self.tau0_exact<=0:raise ValueError('positive support and heat time required')
        self.support_width=float(self.support_exact);self.tau0=float(self.tau0_exact)
        self.tail_start_exact=seed.length_exact*(1-seed.flat_fraction_exact)
        self.tail_start=float(self.tail_start_exact)
        self.sigma0=float(np.sqrt(2*self.tau0))
        if self.tau0_exact==Q(1,128):self.sigma0=1/8
        self.identity={'schema':'infinite-Gaussian-S9-cap-extension-v1',
            'tail_physical_identity':tail.identity,'tail_physical_identity_sha256':tail.identity_sha256,
            'radial_metric_definition':exact_metric_definition(seed),
            'support_width_exact':str(self.support_exact),'tail_start_exact':str(self.tail_start_exact),
            'tau0_exact':str(self.tau0_exact),
            'heat_time':'tau0*((tail_start-t)/support_width)^6',
            'Gaussian_standard_deviation':'sqrt(2*tau0)*((tail_start-t)/support_width)^3',
            'exact_operator':'expectation over Z~N(0,1) of E(t,theta+Gaussian_standard_deviation*Z)',
            'equivalent_periodic_operator':'exp(heat_time*d_theta^2)',
            'reflected_increment':'3*g(R)-3*g(R-epsilon)+g(R-2*epsilon); epsilon=a(t)-R',
            'beta_constant_lift':'-side*pi; heat only the periodic real increment',
            'domain':'tail_start-support_width<=t<=tail_start; all source radii in [0,R]',
            'finite_Gauss_Hermite_order_not_part_of_physical_identity':True,
            'infinite_operator_is_angular_analytic_for_positive_heat_time':True,
            'no_isometry_embedding_or_existence_claim':True}
        self.identity_sha256=digest(self.identity)

    def radial_data(self,radial):
        radial=np.asarray(radial,float)
        if radial.ndim!=1:raise ValueError('one-dimensional radial samples required')
        delta=self.tail_start-radial
        slack=128*np.finfo(float).eps*max(1.,abs(self.tail_start),self.tail.outer)
        if np.any(delta<-slack) or np.any(delta>self.support_width+slack):
            raise ValueError('heat extension queried outside its compact interval')
        delta=np.clip(delta,0,self.support_width);x=delta/self.support_width
        metric=self.seed.evaluate(radial);epsilon=metric['a']-self.tail.outer
        if np.any(epsilon<-slack) or np.any(2*epsilon>self.tail.outer+slack):
            raise ValueError('reflected source radii require 0<=2*(a-R)<=R')
        epsilon=np.maximum(epsilon,0.)
        return {'delta':delta,'epsilon':epsilon,'a_s':metric['a_s'],'a_ss':metric['a_ss'],
            'sigma':self.sigma0*x**3,
            'sigma_s':-3*self.sigma0*x**2/self.support_width,
            'sigma_ss':6*self.sigma0*x/self.support_width**2}

    def composition_at_nodes(self,data,theta,nodes):
        theta=np.asarray(theta,float)
        if theta.ndim!=1:raise ValueError('one-dimensional angular samples required')
        nodes=np.atleast_1d(np.asarray(nodes,float));shape=(len(data['delta']),len(theta),len(nodes))
        def broad(value):return np.broadcast_to(np.asarray(value)[:,None,None],shape)
        angle=coordinate_jet(theta[None,:,None]+broad(data['sigma'])*nodes,
            broad(data['sigma_s'])*nodes,broad(data['sigma_ss'])*nodes,1.)
        r0=coordinate_jet(np.full(shape,self.tail.outer))
        r1=coordinate_jet(broad(self.tail.outer-data['epsilon']),-broad(data['a_s']),-broad(data['a_ss']))
        r2=coordinate_jet(broad(self.tail.outer-2*data['epsilon']),-2*broad(data['a_s']),-2*broad(data['a_ss']))
        f0=cap_increment_composition(self.tail,r0,angle)
        f1=cap_increment_composition(self.tail,r1,angle)
        f2=cap_increment_composition(self.tail,r2,angle)
        return {name:3*f0[name]-3*f1[name]+f2[name] for name in ['u','v','beta']}

    def evaluate(self,radial,theta,order=32):
        radial=np.asarray(radial,float);theta=np.asarray(theta,float)
        data=self.radial_data(radial);shape=(len(radial),len(theta))
        nodes,weights=gaussian_rule(order);batch_size=8
        accumulated={name:np.zeros((3,3)+shape) for name in ['u','v','beta']}
        for start in range(0,len(nodes),batch_size):
            values=self.composition_at_nodes(data,theta,nodes[start:start+batch_size])
            for name in accumulated:
                accumulated[name]+=np.sum(values[name].c*weights[start:start+batch_size],axis=-1)
        jets={name:Jet22(value) for name,value in accumulated.items()}
        jets['beta']=jets['beta']-self.tail.side*np.pi
        out={name:value.result() for name,value in jets.items()}
        out.update(heat_extension_identity_sha256=self.identity_sha256,
            evaluation={'method':'standard-normal Gauss-Hermite, streamed in bounded small batches',
                'order':int(order),'node_batch_size':batch_size,'weight_sum_numerically_normalized':True,
                'same_nodes_for_every_query_angle_and_radius':True,
                'no_finite_Fourier_source_model':True,
                'finite_quadrature_is_C4_and_is_not_the_analytic_physical_field':True,
                'quadrature_error_not_certified':True},
            delta=data['delta'],sigma=data['sigma'],minimum_source_radius=self.tail.outer-2*data['epsilon'])
        return out


class _ArtificialSeed:
    """Only a polynomial radial coordinate for interface development."""
    def __init__(self,radius):
        self.radius=float(exact(radius));self.length_exact=Q(10,9);self.flat_fraction_exact=Q(1,10)
        self.frozen_definition={'schema':'artificial-heat-interface-radius-v1','R':str(exact(radius)),
            'a(t)':'R+(1-t)+(1-t)^3/5','not_a_research_metric':True}
    def evaluate(self,radial):
        d=1-np.asarray(radial,float)
        return {'a':self.radius+d+d**3/5,'a_s':-1-3*d*d/5,'a_ss':6*d/5}


def _maximum_difference(left,right):
    return {key:max(float(np.max(abs(left[name][key]-right[name][key])))
                    for name in ['u','v','beta']) for key in JET_KEYS}


def _cutoff_applied(result,radial,tf=1.,support=.1):
    from polygonal_flat_tail_port import s9_derivative
    x=(tf-np.asarray(radial))/support;chi=1-s9_derivative(x)
    cp=s9_derivative(x,1)/support;cpp=-s9_derivative(x,2)/support**2
    out={}
    for name in ['u','v','beta']:
        f=result[name];out[name]={}
        for key in ['value','theta','tt']:out[name][key]=chi[:,None]*f[key]
        out[name]['s']=cp[:,None]*f['value']+chi[:,None]*f['s']
        out[name]['ss']=cpp[:,None]*f['value']+2*cp[:,None]*f['s']+chi[:,None]*f['ss']
        out[name]['st']=cp[:,None]*f['theta']+chi[:,None]*f['st']
        out[name]['ss_theta']=cpp[:,None]*f['theta']+2*cp[:,None]*f['st']+chi[:,None]*f['ss_theta']
        # Full t² theta² includes the source s theta² jet; it is not needed by
        # the solver and is excluded from this auxiliary weighted comparison.
        out[name]['ss_thetatheta']=np.zeros_like(f['ss_thetatheta'])
    return out


def developer_check():
    from cosine_connector_radial_seed import NegativeKRadialSeed
    src={'kind':'artificial-exact-perimeter-interface','definition':'4/5','numerical_a0_for_evaluation':.8}
    real_seed=NegativeKRadialSeed('4/5','11/10','11/50',a0_source=src)
    src2=dict(src,numerical_a0_for_evaluation=float(np.nextafter(.8,1.)))
    refined_seed=NegativeKRadialSeed(np.nextafter(.8,1.),'11/10','11/50',a0_source=src2)
    outer=real_seed.cut_radius_exact+real_seed.length_exact*real_seed.flat_fraction_exact
    interface_tail=PolygonalFlatTail(outer,'11/50',['1/7','1/9','1/9','1/7','1/9','1/9'])
    interface=GaussianPolygonalExtension(interface_tail,real_seed)
    refined_interface=GaussianPolygonalExtension(interface_tail,refined_seed)
    actual_class_identity_check={'NegativeKRadialSeed_callable_definition_accepted':True,
        'numerical_perimeter_refinement_preserves_heat_identity':interface.identity_sha256==refined_interface.identity_sha256,
        'numerical_evaluation_absent_from_heat_metric': 'numerical_evaluation' not in interface.identity['radial_metric_definition'],
        'definition_sha256_preserved':interface.identity['radial_metric_definition']['definition_sha256']==real_seed.frozen_definition()['definition_sha256'],
        'artificial_parameters_only_no_geometry_evaluated':True}
    # This finite Fourier source has an independent closed Gaussian expectation.
    radial=np.array([.9,.94,.985,1.]);theta=np.array([.13,.47,1.08,1.91])
    delta=1-radial;shape=(len(radial),len(theta));x=delta/.1
    sigma=.125*x**3;sp=-3*.125*x*x/.1;spp=6*.125*x/.1**2
    A=1+.3*radial+.2*radial**2;Ap=.3+.4*radial;App=np.full_like(radial,.4)
    aj=coordinate_jet(np.broadcast_to(A[:,None],shape),Ap[:,None],App[:,None])
    k=7
    def Fourier_node(z):
        angle=coordinate_jet(theta[None,:]+sigma[:,None]*z,sp[:,None]*z,spp[:,None]*z,1.)
        value=aj*(k*angle).cos()
        return {'u':value,'v':2*value,'beta':-value}
    approximate=gaussian_jet_expectation(Fourier_node,32,shape)
    tau=sigma*sigma/2;tp=sigma*sp;tpp=sp*sp+sigma*spp
    exponent=coordinate_jet(np.broadcast_to(-k*k*tau[:,None],shape),-k*k*tp[:,None],-k*k*tpp[:,None])
    decay=exponent.compose([np.exp(exponent.c[0,0])]*5)
    angle=coordinate_jet(np.broadcast_to(theta[None,:],shape),theta=1.)
    independent=aj*decay*(k*angle).cos()
    exacts={'u':independent.result(),'v':(2*independent).result(),'beta':(-independent).result()}
    errors=_maximum_difference({name:value.result() for name,value in approximate.items()},exacts)

    rows=[];amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9']
    for side in [1,-1]:
        tail=PolygonalFlatTail('9/10','3/5',amplitudes,side)
        extension=GaussianPolygonalExtension(tail,_ArtificialSeed(tail.outer_exact))
        t=np.array([.927,.954,.982,.995]);th=np.array([.11,.43,.69,1.19,1.71,2.25,3.42,4.88,5.81])
        h=1e-6;base=extension.evaluate(t,th,32)
        plus=extension.evaluate(t+h,th,32);minus=extension.evaluate(t-h,th,32)
        angular_plus=extension.evaluate(t,th+h,32);angular_minus=extension.evaluate(t,th-h,32)
        checks={}
        for name in ['u','v','beta']:
            for target,source,pa,ma in [('s','value',plus,minus),('ss','s',plus,minus),
                ('theta','value',angular_plus,angular_minus),('st','s',angular_plus,angular_minus),
                ('ss_theta','ss',angular_plus,angular_minus),('ss_thetatheta','ss_theta',angular_plus,angular_minus)]:
                fd=(pa[name][source]-ma[name][source])/(2*h)
                checks[name+'_'+target]=float(np.max(abs(fd-base[name][target])))/max(1.,float(np.max(abs(base[name][target]))))
        endpoint=extension.evaluate(np.array([1.]),th,32);port=tail.scalar_jets(tail.outer,th)
        endpoint_error=max(float(np.max(abs(endpoint[name][key][0]-port[name][key]))) for name in ['u','v','beta'] for key in JET_KEYS)
        separate=extension.evaluate(t,np.array([th[3]]),32)
        query_error=max(float(np.max(abs(separate[name][key][:,0]-base[name][key][:,3]))) for name in ['u','v','beta'] for key in JET_KEYS)
        period=extension.evaluate(t,th+np.pi,32);reflection=extension.evaluate(t,-th,32)
        period_error=max(float(np.max(abs(period[name][key]-base[name][key]))) for name in ['u','v','beta'] for key in JET_KEYS)
        symmetry=[]
        for name in ['u','v','beta']:
            for key in JET_KEYS:
                theta_order={'value':0,'s':0,'ss':0,'theta':1,'st':1,'tt':2,'ss_theta':1,'ss_thetatheta':2}[key]
                parity=(-1 if name in ['u','v'] else 1)*(-1)**theta_order
                symmetry.append(float(np.max(abs(reflection[name][key]-parity*base[name][key]))))
        # Same artificial source and same heat identity at every evaluation order.
        tr=np.array([.9,.92,.94,.96,.98,.995,.9995,1.]);angles=np.arange(48)*2*np.pi/48+.007
        refinements={n:extension.evaluate(tr,angles,n) for n in [16,32,64,128]}
        differences={str(n)+'_to_'+str(2*n):_maximum_difference(refinements[n],refinements[2*n]) for n in [16,32,64]}
        weighted={n:_cutoff_applied(value,tr) for n,value in refinements.items()}
        weighted_differences={str(n)+'_to_'+str(2*n):{key:value for key,value in _maximum_difference(weighted[n],weighted[2*n]).items()
            if key!='ss_thetatheta'} for n in [16,32,64]}
        by_radius=[]
        for i,t0 in enumerate(tr):
            by_radius.append({'t':float(t0),'delta':float(1-t0),
                'difference_32_to_128':{key:max(float(np.max(abs(refinements[32][name][key][i]-refinements[128][name][key][i])))
                    for name in ['u','v','beta']) for key in JET_KEYS}})
        rows.append({'side':side,'spatial_jet_finite_difference_relative_errors':checks,
            'exact_port_full_Jet22_error':endpoint_error,'query_set_invariance_error':query_error,
            'period_error':period_error,'reflection_error':max(symmetry),
            'fixed_identity_quadrature_refinement':differences,'refinement_by_radius':by_radius,
            'cutoff_applied_quadrature_refinement':weighted_differences,
            'heat_extension_identity_sha256':extension.identity_sha256,
            'all_orders_have_identical_physical_identity':all(v['heat_extension_identity_sha256']==extension.identity_sha256 for v in refinements.values())})
    passed=all(actual_class_identity_check.values()) and max(errors.values())<1e-7 and all(max(row['spatial_jet_finite_difference_relative_errors'].values())<3e-5
        and row['exact_port_full_Jet22_error']<2e-8 and row['query_set_invariance_error']<1e-10
        and row['period_error']<2e-8 and row['reflection_error']<2e-8 and row['all_orders_have_identical_physical_identity'] for row in rows)
    return {'schema':'Gaussian-six-cap-extension-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'optimization_performed':False,
        'real_seed_class_artificial_identity_check':actual_class_identity_check,
        'Fourier_source_exact_Gaussian_comparison':errors,'checks':rows,'passed':bool(passed),
        'quadrature_refinement_differences_are_diagnostics_not_continuous_bounds':True,
        'passed_does_not_assert_default_order_sufficient_for_research':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=developer_check()
    result['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in [Path(__file__).name,'polygonal_flat_tail_port.py','bent_flat_tail_port.py']}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
