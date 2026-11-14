#!/usr/bin/env python3
"""Saturated source displacement for the same infinite Gaussian cap operator.

e=c*tanh((a-R)/c), c=(R-d)/4, preserves the physical end two-jet and keeps
every inner source circle strictly outside the cap-birth radius d. This is a
new fixed base, with unchanged metric and unchanged accurate physical cap.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from bent_flat_tail_port import digest
from polygonal_flat_tail_port import PolygonalFlatTail,algebraic
from polygonal_tail_heat_extension import GaussianPolygonalExtension,_ArtificialSeed,JET_KEYS,_maximum_difference


class SaturatedGaussianPolygonalExtension(GaussianPolygonalExtension):
    def __init__(self,tail,seed,support_width='1/10',tau0='1/128'):
        super().__init__(tail,seed,support_width,tau0)
        self.saturation_scale=tail.bend_width/4
        self.identity.update(schema='infinite-Gaussian-S9-cap-saturated-reflection-v1',
            raw_epsilon='a(t)-R',
            source_displacement='e=c*tanh(raw_epsilon/c)',
            saturation_scale_Q_sqrt3=algebraic(tail.outer_exact/4,-tail.outer_exact/8),
            saturation_scale_definition='c=(R-chord_offset)/4=(R-d)/4',
            reflected_increment='3*g(R)-3*g(R-e)+g(R-2*e)',
            inner_source_radius_strict_lower_Q_sqrt3=algebraic(tail.outer_exact/2,tail.outer_exact/4),
            strict_lower_exceeds_chord_offset=True,
            raw_epsilon_endpoint_jets=['e(0)=0','de/depsilon(0)=1','d2e/depsilon2(0)=0'],
            all_inner_source_radii_remain_above_cap_birth_radius=True,
            source_coordinate_changed_from_raw_reflection=True,
            accurate_metric_and_physical_cap_unchanged=True)
        self.identity_sha256=digest(self.identity)

    def radial_data(self,radial):
        radial=np.asarray(radial,float)
        if radial.ndim!=1:raise ValueError('one-dimensional radial samples required')
        delta=self.tail_start-radial
        slack=128*np.finfo(float).eps*max(1.,abs(self.tail_start),self.tail.outer)
        if np.any(delta<-slack) or np.any(delta>self.support_width+slack):
            raise ValueError('heat extension queried outside its compact interval')
        delta=np.clip(delta,0,self.support_width);x=delta/self.support_width
        metric=self.seed.evaluate(radial);raw=metric['a']-self.tail.outer
        if np.any(raw<-slack):raise ValueError('saturated reflection needs a(t)>=R')
        raw=np.maximum(raw,0.);tangent=np.tanh(raw/self.saturation_scale)
        first=1-tangent*tangent;second=-2*tangent*first/self.saturation_scale
        displacement=self.saturation_scale*tangent
        derivative=first*metric['a_s']
        second_derivative=second*metric['a_s']**2+first*metric['a_ss']
        # The inherited coordinate composer consumes these two legacy keys as
        # derivatives of its source displacement. They are e_t,e_tt here,
        # not a new value of the physical metric derivatives.
        return {'delta':delta,'epsilon':displacement,'a_s':derivative,'a_ss':second_derivative,
            'raw_epsilon':raw,'source_e_s':derivative,'source_e_ss':second_derivative,
            'metric_a_s_unchanged':metric['a_s'],'metric_a_ss_unchanged':metric['a_ss'],
            'sigma':self.sigma0*x**3,
            'sigma_s':-3*self.sigma0*x**2/self.support_width,
            'sigma_ss':6*self.sigma0*x/self.support_width**2}


def developer_check():
    rows=[];amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9']
    for side in [1,-1]:
        tail=PolygonalFlatTail('9/10','3/5',amplitudes,side)
        seed=_ArtificialSeed(tail.outer_exact);extension=SaturatedGaussianPolygonalExtension(tail,seed)
        radial=np.array([.917,.943,.976,.993]);theta=np.array([.11,.43,.69,1.19,1.71,2.25,3.42,4.88,5.81])
        step=1e-6;data=extension.radial_data(radial)
        dp=extension.radial_data(radial+step);dm=extension.radial_data(radial-step)
        coordinate_errors={
            'e_s':float(np.max(abs((dp['epsilon']-dm['epsilon'])/(2*step)-data['source_e_s']))),
            'e_ss':float(np.max(abs((dp['source_e_s']-dm['source_e_s'])/(2*step)-data['source_e_ss'])))}
        field=extension.evaluate(radial,theta,32)
        plus=extension.evaluate(radial+step,theta,32);minus=extension.evaluate(radial-step,theta,32)
        ap=extension.evaluate(radial,theta+step,32);am=extension.evaluate(radial,theta-step,32)
        errors={}
        for name in ['u','v','beta']:
            for target,source,pa,ma in [('s','value',plus,minus),('ss','s',plus,minus),
                ('theta','value',ap,am),('st','s',ap,am),('ss_theta','ss',ap,am),
                ('ss_thetatheta','ss_theta',ap,am)]:
                fd=(pa[name][source]-ma[name][source])/(2*step)
                errors[name+'_'+target]=float(np.max(abs(fd-field[name][target])))/max(1.,float(np.max(abs(field[name][target]))))
        endpoint=extension.evaluate(np.array([1.]),theta,32);exact=tail.scalar_jets(tail.outer,theta)
        end_error=max(float(np.max(abs(endpoint[name][key][0]-exact[name][key])))
            for name in ['u','v','beta'] for key in JET_KEYS)
        points=np.array([.9,.94,.98,1.]);angles=np.arange(24)*2*np.pi/24+.007
        refinement={n:extension.evaluate(points,angles,n) for n in [16,32,64]}
        differences={str(n)+'_to_'+str(2*n):_maximum_difference(refinement[n],refinement[2*n]) for n in [16,32]}
        raw=GaussianPolygonalExtension(tail,seed)
        rows.append({'side':side,'source_coordinate_finite_difference_errors':coordinate_errors,
            'scalar_spatial_jet_relative_errors':errors,'accurate_port_full_Jet22_error':end_error,
            'minimum_sampled_inner_source_radius_minus_d':float(np.min(tail.outer-2*data['epsilon']-tail.offset)),
            'exact_strict_source_gap_lower_formula':'(R-d)/2',
            'physical_cap_identity_unchanged':raw.tail.identity==extension.tail.identity,
            'exact_metric_identity_unchanged':raw.identity['radial_metric_definition']==extension.identity['radial_metric_definition'],
            'base_identity_differs_from_raw':raw.identity_sha256!=extension.identity_sha256,
            'same_heat_identity_at_all_quadrature_orders':all(value['heat_extension_identity_sha256']==extension.identity_sha256 for value in refinement.values()),
            'fixed_parameter_GH_refinement':differences,'identity_sha256':extension.identity_sha256})
    passed=all(max(row['source_coordinate_finite_difference_errors'].values())<1e-5
        and max(row['scalar_spatial_jet_relative_errors'].values())<3e-5
        and row['accurate_port_full_Jet22_error']<2e-8 and row['minimum_sampled_inner_source_radius_minus_d']>0
        and row['physical_cap_identity_unchanged'] and row['exact_metric_identity_unchanged']
        and row['base_identity_differs_from_raw'] and row['same_heat_identity_at_all_quadrature_orders'] for row in rows)
    return {'schema':'saturated-Gaussian-six-cap-extension-development-v1','checks':rows,'passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False,
        'passed_does_not_certify_GH_error_or_geometric_feasibility':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=developer_check()
    result['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in [Path(__file__).name,'polygonal_tail_heat_extension.py','polygonal_flat_tail_port.py','bent_flat_tail_port.py']}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
