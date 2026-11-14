#!/usr/bin/env python3
"""Natural single-cap scalar continuations with endpoint-flat angular heat.

For r>R the six cylindrical maps overlap.  Their scalar increments are added
only to define a target orthonormal frame; their position sum is not asserted
to be an isometric surface.  Infinite Gaussian averaging is the definition,
and finite Gauss-Hermite rules are only evaluators of that same definition.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np

from bent_flat_tail_port import Jet22,digest,exact
from polygonal_flat_tail_port import PolygonalFlatTail,s9_derivative
from polygonal_tail_heat_extension import (coordinate_jet,exact_metric_definition,
    gaussian_rule,_ArtificialSeed,JET_KEYS,_maximum_difference)


def natural_cap_scalar_sum(tail,radius,angle):
    """Sum six globally defined cylindrical scalar increments, not positions."""
    if np.any(radius.c[0,0]<0):raise ValueError('nonnegative source radius required')
    cosine,sine=angle.cos(),angle.sin();zero=np.zeros_like(radius.c[0,0])
    result={name:Jet22.constant(zero) for name in ['u','v','beta']}
    for j,normal in enumerate(tail.normals):
        a=cosine*normal[0]+sine*normal[1]
        b=-sine*normal[0]+cosine*normal[1]
        excess=radius*a-tail.offset
        if not np.any(excess.c[0,0]>0):continue
        # Keep the exact clamped S9 definition. Polynomial continuation past
        # its saturation point would be a different and unbounded angle law.
        alpha=excess.compose(tail.alpha_jets(j,excess.c[0,0],4))
        C,S=alpha.cos(),alpha.sin()
        result['u']=result['u']+((1-C)*a*b/(1-(1-C)*b*b)).atan()
        result['v']=result['v']-tail.side*b*S/(1-b*b*S*S).sqrt()
        result['beta']=result['beta']+tail.side*(a*S/C).atan()
    return result


def flat_gaussian_scale(delta,support,sigma0):
    """sigma=sigma0*exp(1-(h/delta)^2), with its t,tt jets (delta=tf-t).

    Logarithmic evaluation avoids 0 times overflow near the endpoint. Any
    binary64 underflow is an evaluation effect, not a cutoff in the model.
    """
    delta=np.asarray(delta,float);x=delta/float(support)
    sigma=np.zeros_like(x);first=np.zeros_like(x);second=np.zeros_like(x)
    mask=x>0
    if np.any(mask):
        z=x[mask];logx=np.log(z)
        with np.errstate(over='ignore',under='ignore',divide='ignore',invalid='raise'):
            logvalue=np.log(float(sigma0))+1-1/(z*z)
            sigma[mask]=np.exp(logvalue)
            first[mask]=-np.exp(logvalue+np.log(2/float(support))-3*logx)
            second[mask]=(np.exp(logvalue+np.log(4/float(support)**2)-6*logx)
                          -np.exp(logvalue+np.log(6/float(support)**2)-4*logx))
    return sigma,first,second


def plateau_cutoff(radial,tail_start,support,plateau_fraction=Q(1,3)):
    """chi=1 near the end; a clamped S9 transition on the outer support part."""
    fraction=float(plateau_fraction)
    if not 0<fraction<1:raise ValueError('a strict interior plateau fraction is required')
    width=float(support)*(1-fraction)
    y=((float(tail_start)-np.asarray(radial,float))-float(support)*fraction)/width
    return (1-s9_derivative(y),s9_derivative(y,1)/width,-s9_derivative(y,2)/width**2)


class NaturalGaussianPolygonalExtension:
    def __init__(self,tail,seed,support_width='1/10',tau0='1/128'):
        self.tail=tail;self.seed=seed
        self.support_exact=exact(support_width);self.tau0_exact=exact(tau0)
        if self.support_exact<=0 or self.tau0_exact<=0:raise ValueError('positive support and heat scale required')
        self.support_width=float(self.support_exact);self.tau0=float(self.tau0_exact)
        self.tail_start_exact=seed.length_exact*(1-seed.flat_fraction_exact)
        self.tail_start=float(self.tail_start_exact);self.sigma0=float(np.sqrt(2*self.tau0))
        if self.tau0_exact==Q(1,128):self.sigma0=1/8
        self.identity={'schema':'natural-single-cap-sum-flat-Gaussian-extension-v1',
            'tail_physical_identity':tail.identity,'tail_physical_identity_sha256':tail.identity_sha256,
            'patch_seed_metric_definition':exact_metric_definition(seed),
            'support_width_exact':str(self.support_exact),'tail_start_exact':str(self.tail_start_exact),
            'tau0_exact':str(self.tau0_exact),
            'source_radius':'a_seed(t), independent of body metric control coefficients',
            'source_scalar_definition':'flat+sum_j(single_cap_u_j,single_cap_v_j,single_cap_beta_j-flat)',
            'single_cap_angle_law':'the original globally clamped S9 law, including u>=w saturation',
            'source_maps_overlap_outside_R':True,
            'source_scalar_sum_is_only_a_target_frame_base_not_a_position_sum_isometry':True,
            'Gaussian_standard_deviation':'sqrt(2*tau0)*exp(1-(support_width/delta)^2) for delta>0; zero at delta=0',
            'heat_time':'tau0*exp(2-2*(support_width/delta)^2) for delta>0; zero at delta=0',
            'exact_operator':'expectation over Z~N(0,1) of the source scalar increment at theta+sigma(t)*Z',
            'beta_constant_lift':'-side*pi, added after the periodic increment expectation',
            'fixed_single_cap_all_radial_jet_scope':'fixed nondegenerate open angles with 0<excess<w and b!=0, away from vertices and cap centers',
            'no_all_order_joint_jet_claim_at_vertices_or_cap_centers':True,
            'source_joint_regularities':'globally C4 scalar increments; smooth within each single-cap branch',
            'heat_scale_flat_at_tail_endpoint':True,
            'finite_GH_order_not_part_of_physical_identity':True,
            'finite_exponential_underflow_is_not_a_physical_cutoff':True,
            'infinite_operator_is_angular_analytic_for_delta_positive':True,
            'domain':'tail_start-support_width<=t<=tail_start; source radius may exceed R',
            'no_isometry_embedding_or_existence_claim':True}
        self.identity_sha256=digest(self.identity)

    def radial_data(self,radial):
        radial=np.asarray(radial,float)
        if radial.ndim!=1:raise ValueError('one-dimensional radial samples required')
        delta=self.tail_start-radial
        slack=128*np.finfo(float).eps*max(1.,abs(self.tail_start),self.tail.outer)
        if np.any(delta<-slack) or np.any(delta>self.support_width+slack):
            raise ValueError('natural heat extension queried outside its support')
        delta=np.clip(delta,0,self.support_width)
        metric=self.seed.evaluate(radial)
        if np.any(metric['a']<self.tail.outer-slack):raise ValueError('the exterior patch requires a_seed>=R')
        sigma,first,second=flat_gaussian_scale(delta,self.support_width,self.sigma0)
        return {'delta':delta,'source_radius':metric['a'],'source_radius_s':metric['a_s'],
            'source_radius_ss':metric['a_ss'],'sigma':sigma,'sigma_s':first,'sigma_ss':second}

    def composition_at_nodes(self,data,theta,nodes):
        theta=np.asarray(theta,float);nodes=np.atleast_1d(np.asarray(nodes,float))
        if theta.ndim!=1:raise ValueError('one-dimensional angular samples required')
        shape=(len(data['delta']),len(theta),len(nodes))
        def broad(value):return np.broadcast_to(np.asarray(value)[:,None,None],shape)
        radius=coordinate_jet(broad(data['source_radius']),broad(data['source_radius_s']),broad(data['source_radius_ss']))
        angle=coordinate_jet(theta[None,:,None]+broad(data['sigma'])*nodes,
            broad(data['sigma_s'])*nodes,broad(data['sigma_ss'])*nodes,1.)
        return natural_cap_scalar_sum(self.tail,radius,angle)

    def evaluate(self,radial,theta,order=32):
        radial=np.asarray(radial,float);theta=np.asarray(theta,float)
        data=self.radial_data(radial);shape=(len(radial),len(theta))
        nodes,weights=gaussian_rule(order);batch_size=8
        accumulated={name:np.zeros((3,3)+shape) for name in ['u','v','beta']}
        for start in range(0,len(nodes),batch_size):
            values=self.composition_at_nodes(data,theta,nodes[start:start+batch_size])
            for name in accumulated:
                accumulated[name]+=np.sum(values[name].c*weights[start:start+batch_size],axis=-1)
        endpoint=data['delta']==0
        if np.any(endpoint):
            direct=self.composition_at_nodes(data,theta,[0.])
            for name in accumulated:
                value=direct[name].c[...,0]
                accumulated[name][:,:,endpoint,:]=value[:,:,endpoint,:]
        jets={name:Jet22(value) for name,value in accumulated.items()}
        jets['beta']=jets['beta']-self.tail.side*np.pi
        answer={name:value.result() for name,value in jets.items()}
        answer.update(heat_extension_identity_sha256=self.identity_sha256,
            evaluation={'method':'standard-normal GH, fixed nodes in eight-node batches','order':int(order),
                'same_nodes_for_every_query_angle_and_radius':True,'finite_quadrature_is_only_an_evaluator':True,
                'finite_GH_does_not_make_the_exact_field_piecewise_C4':True,
                'quadrature_error_not_certified':True,'endpoint_uses_the_zero_heat_direct_composition':True},
            delta=data['delta'],sigma=data['sigma'],source_radius=data['source_radius'],
            source_sum_outside_R_not_an_isometric_cap=True)
        return answer


def developer_check():
    rows=[];angles=np.array([.11,.43,.69,1.19,1.71,2.25,3.42,4.88,5.81])
    radial=np.array([.917,.943,.976,.993]);step=1e-6
    for side in [1,-1]:
        tail=PolygonalFlatTail('9/10','3/5',['1/7','1/9','1/9','1/7','1/9','1/9'],side)
        extension=NaturalGaussianPolygonalExtension(tail,_ArtificialSeed(tail.outer_exact))
        data=extension.radial_data(radial);dp=extension.radial_data(radial+step);dm=extension.radial_data(radial-step)
        scale_errors={
            'sigma_s':float(np.max(abs((dp['sigma']-dm['sigma'])/(2*step)-data['sigma_s']))),
            'sigma_ss':float(np.max(abs((dp['sigma_s']-dm['sigma_s'])/(2*step)-data['sigma_ss'])))}
        field=extension.evaluate(radial,angles,32)
        plus=extension.evaluate(radial+step,angles,32);minus=extension.evaluate(radial-step,angles,32)
        ap=extension.evaluate(radial,angles+step,32);am=extension.evaluate(radial,angles-step,32)
        errors={}
        for name in ['u','v','beta']:
            for target,source,pa,ma in [('s','value',plus,minus),('ss','s',plus,minus),
                ('theta','value',ap,am),('st','s',ap,am),('ss_theta','ss',ap,am),
                ('ss_thetatheta','ss_theta',ap,am)]:
                fd=(pa[name][source]-ma[name][source])/(2*step)
                errors[name+'_'+target]=float(np.max(abs(fd-field[name][target])))/max(1.,float(np.max(abs(field[name][target]))))
        endpoint=extension.evaluate(np.array([1.]),angles,32);correct=tail.scalar_jets(tail.outer,angles)
        end_error=max(float(np.max(abs(endpoint[name][key][0]-correct[name][key])))
            for name in ['u','v','beta'] for key in JET_KEYS)
        # At a radius below R the independent original disjoint-cap evaluator
        # and the new scalar-sum composition are exactly the same formulas.
        rr=coordinate_jet(np.full_like(angles,.86),-1.);tt=coordinate_jet(angles,theta=1.)
        direct=natural_cap_scalar_sum(tail,rr,tt);direct['beta']=direct['beta']-side*np.pi
        old=tail.scalar_jets(.86,angles)
        inside_error=max(float(np.max(abs(direct[name].result()[key]-old[name][key])))
            for name in direct for key in JET_KEYS)
        period=extension.evaluate(radial,angles+np.pi,32);reflection=extension.evaluate(radial,-angles,32)
        symmetry=max(float(np.max(abs(period[name]['value']-field[name]['value']))) for name in ['u','v','beta'])
        symmetry=max(symmetry,max(float(np.max(abs(reflection[name]['value']-(-1 if name!='beta' else 1)*field[name]['value']))) for name in ['u','v','beta']))
        endpoint_scale=flat_gaussian_scale(np.array([0.,1e-3,1e-100]),.1,.125)
        chi=plateau_cutoff(np.array([.9,.94,.98,1.]),1.,.1)
        points=np.array([.91,.945,.98,1.]);grid_angles=np.arange(24)*2*np.pi/24+.007
        refined={n:extension.evaluate(points,grid_angles,n) for n in [16,32,64]}
        rows.append({'side':side,'heat_scale_finite_difference_errors':scale_errors,
            'scalar_spatial_jet_relative_errors':errors,'accurate_port_full_Jet22_error':end_error,
            'inside_R_independent_old_port_error':inside_error,'twofold_and_reflection_error':symmetry,
            'endpoint_and_small_delta_scale_evaluation':[x.tolist() for x in endpoint_scale],
            'plateau_cutoff_value_s_ss':[x.tolist() for x in chi],
            'fixed_model_GH_differences':{str(n)+'_to_'+str(2*n):_maximum_difference(refined[n],refined[2*n]) for n in [16,32]},
            'same_identity_under_GH_refinement':all(x['heat_extension_identity_sha256']==extension.identity_sha256 for x in refined.values()),
            'physical_identity_sha256':extension.identity_sha256})
    passed=all(max(row['heat_scale_finite_difference_errors'].values())<2e-5
        and max(row['scalar_spatial_jet_relative_errors'].values())<3e-5
        and max(row['accurate_port_full_Jet22_error'],row['inside_R_independent_old_port_error'],row['twofold_and_reflection_error'])<2e-8
        and row['same_identity_under_GH_refinement'] for row in rows)
    return {'schema':'natural-single-cap-flat-heat-development-v1','passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False,
        'checks':rows,'passed_does_not_certify_GH_error_isometry_or_a_connector':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();answer=developer_check()
    names=[Path(__file__).name,'polygonal_tail_heat_extension.py','polygonal_flat_tail_port.py','bent_flat_tail_port.py']
    answer['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(answer,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
