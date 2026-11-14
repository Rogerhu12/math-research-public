#!/usr/bin/env python3
"""Finite floating diagnostics of the original RHS on unchanged saved curves.

This does not solve, integrate, optimize, or export a candidate. Increasing the
projection order here changes only the evaluated velocity at one fixed curve,
not the curve or its angular metric. It supplies no continuous certificate.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np


HERE=Path(__file__).resolve().parent
TOPIC=HERE.parent


def require(condition,message):
    if not condition:raise ValueError(message)


def identity(path):
    path=Path(path).resolve();raw=path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def verify(row):
    actual=identity(row['path'])
    require(all(row.get(k)==v for k,v in actual.items()),'Changed bound file: '+row['path'])


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result


def lift(values,old_modes,new_modes):
    require(new_modes>=old_modes,'This fixed-state diagnostic only pads exact zero modes')
    out=np.zeros((3*new_modes+1,values.shape[1]),dtype=values.dtype)
    out[0]=values[0]
    for axis in range(3):
        out[axis*new_modes+1:axis*new_modes+old_modes+1]=values[axis*old_modes+1:(axis+1)*old_modes+1]
    return out


def diagnosis(rec,obj,sol,locations,modes,quadrature,audit_angular):
    flow=obj.Flow(obj.cfg,obj.port,modes,obj.q,quadrature,obj.base_mode,obj.bridge)
    require(flow.nt==quadrature,'Requested quadrature is below the original geometric minimum')
    Y=lift(sol.sol(locations),obj.M,modes)
    Yp=lift(sol.sol(locations,1),obj.M,modes)
    dy=flow.fun(locations,Y,sol.p)
    B,B1,B2=flow.basis(audit_angular)
    fr=flow.frame(locations,obj.q*Y,B1,B2)
    g=fr['geo'];rho=g['rho'];v=g['v'];aa=flow.profile(locations)[0][:,None]
    mean_vz=np.mean(fr['V'][:,:,2],axis=1)
    Ft=fr['d']/rho[:,:,None]
    G=np.sum(Ft*Ft,axis=2)
    common=g['s1']-v[:,:,None]*fr['d']
    common[:,:,2]+=mean_vz[:,None]
    result={'projection_modes':modes,'source_quadrature':quadrature,
            'audit_angular':audit_angular,'radial_points':len(locations),
            'fixed_state_exact_zero_padding':True,'new_candidate':False}
    def summarize(derivative):
        Fs=common+obj.q*flow.values(derivative,B)
        err=np.stack((np.sum(Fs*Fs,axis=2)-1,np.sum(Fs*Ft,axis=2)/aa,G/aa**2-1),axis=2)
        l1=np.sum(abs(np.fft.fft(err,axis=1)/audit_angular),axis=1)
        defect=np.linalg.norm(Fs-fr['Vnormal'],axis=2).max(axis=1)
        rows=[]
        ap=flow.profile(locations)[1]
        for i,s in enumerate(locations):
            rs=ap[i]+obj.q*(derivative[0,i]+sum(((-1)**j*derivative[j,i] for j in range(1,modes+1))))
            zs=mean_vz[i]+obj.q*sum(((-1)**j*derivative[2*modes+j,i] for j in range(1,modes+1)))
            rows.append({'s':float(s),'E_error_FFT_l1':float(l1[i,0]),
                         'F_over_a_error_FFT_l1':float(l1[i,1]),
                         'G_over_a2_error_FFT_l1':float(l1[i,2]),
                         'maximum_component_error_FFT_l1':float(np.max(l1[i])),
                         'velocity_defect_sampled':float(defect[i]),
                         'axis_pi_over_3_E_minus_1_float':float(rs*rs+zs*zs-1)})
        return {'max_E_FFT_l1':float(l1[:,0].max()),'max_F_FFT_l1':float(l1[:,1].max()),
                'max_G_FFT_l1':float(l1[:,2].max()),'max_metric_FFT_l1':float(l1.max()),
                'max_velocity_defect_sampled':float(defect.max()),'rows':rows}
    result['projected_source']=summarize(dy)
    result['saved_interpolant']=summarize(Yp)
    result['saved_vs_source_velocity_sampled']=float(np.linalg.norm(obj.q*flow.values(Yp-dy,B),axis=2).max())
    require(all(math.isfinite(float(x)) for row in result['projected_source']['rows'] for x in row.values()),
            'Nonfinite diagnostic')
    return result,dy


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint',type=Path,action='append',required=True)
    p.add_argument('--linear-port',type=Path,required=True)
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--bound-plan',type=Path,required=True)
    p.add_argument('--bound-plan-sha256',required=True)
    p.add_argument('--witness-report',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    require(not a.out.exists(),'Refuse existing diagnostic output')
    plan_id=identity(a.bound_plan)
    require(plan_id['sha256']==a.bound_plan_sha256,'Changed declared positive production plan')
    plan=json.loads(a.bound_plan.read_text())
    require(plan['plan_ready'] and plan['complete_final_audit_replayed'],'No bound successful source route')
    for row in plan['preexisting_bindings']:verify(row)
    witness=json.loads(a.witness_report.read_text())
    require(witness['schema']=='78718-prefix-nodal-axis-exact-lower-v1','Wrong actual point witness')
    from fractions import Fraction
    point=float(Fraction(witness['witness']['s']['exact']))
    # The actual witness plus fixed historical localization points.  These
    # samples do not claim coverage of the entire physical meridian.
    locations=np.unique(np.array([0.,.00196561545,.05,.11814752887,.2,point,.27483516074,.4,.7,1.]))
    loader_path=HERE/'db6f-prefix-flat-geometry-source.py'
    loader=load_module('fixed_state_original_flat_loader',loader_path)
    inputs=[plan_id,identity(a.witness_report),identity(a.linear_port)]
    all_results=[]
    previous=None
    fixed=('frozen_profile','chart','warp_reference_q','physical_port_sha256','physical_tail_parameters','physical_tail_cut','gauge_amplitude')
    for path in a.checkpoint:
        small=json.loads(gzip.decompress(path.read_bytes()))
        inputs.append(identity(path))
        for chunk in small['pp_coefficient_chunks']:
            row=identity(path.parent/chunk['file'])
            require(row['bytes']==chunk['bytes'] and row['sha256']==chunk['sha256'],'Saved PP chunk changed')
            inputs.append(row)
        if previous is not None:
            require(all(previous[k]==small[k] for k in fixed),'Fixed material definition differs')
        previous=small
        rec,obj,unused,sol=loader.source(path,a.linear_port,a.source_root)
        require(obj.fixed and obj.M==rec['config']['modes'],'Unexpected source class')
        require(locations[-1]<unused.end,'Diagnostic points lie outside source domain')
        rows=[];derivatives={}
        orders=[obj.M]
        if obj.M==14:orders.extend([15,16,18,22,26])
        quadratures=sorted(set([rec['config']['angular'],512,1024,2048]))
        for quadrature in quadratures:
            row,dy=diagnosis(rec,obj,sol,locations,obj.M,quadrature,2048)
            rows.append(row);derivatives[quadrature]=dy
        for modes in orders[1:]:
            row,_=diagnosis(rec,obj,sol,locations,modes,2048,2048)
            rows.append(row)
        differences=[]
        for q0,q1 in zip(quadratures[:-1],quadratures[1:]):
            differences.append({'left_quadrature':q0,'right_quadrature':q1,
                'physical_Fourier_RHS_coefficient_max_difference':float(obj.q*np.max(abs(derivatives[q1]-derivatives[q0])))})
        all_results.append({'checkpoint':identity(path),'modes':obj.M,
            'actual_support_amplitude':rec['actual_primary_amplitude'],
            'original_source_quadrature':rec['config']['angular'],
            'fixed_fields_same_as_other_inputs':True,
            'quadrature_comparisons_on_same_state':differences,'diagnostics':rows})
    # Record the original mathematical source files actually imported from
    # the repository/snapshot; no absent or inferred files are called bound.
    sources=[identity(__file__),identity(loader_path)]
    for module in list(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if not file:continue
        file=Path(file).resolve()
        if file.suffix=='.py' and file.is_relative_to(TOPIC):sources.append(identity(file))
    sources=list({x['path']:x for x in sources}.values())
    inputs=list({x['path']:x for x in inputs}.values())
    for row in [*sources,*inputs,*plan['preexisting_bindings']]:verify(row)
    out={'schema':'78718-prefix-fixed-state-source-projection-v1',
         'status':'COMPLETED_FLOATING_FIXED_STATE_DIAGNOSTIC',
         'scope':__doc__,'actual_witness_report':identity(a.witness_report),
         'sources':sources,'input_bindings':inputs,'checkpoints':all_results,
         'radial_locations':locations.tolist(),'continuous_bound':False,
         'new_candidate_or_reintegrated_curve':False,'BVP_calls':0,'tail_calls':0,
         'numerical_flow_integrations':0,'seconds':time.monotonic()-started}
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':out['status'],'output':identity(a.out),
                     'checkpoints':len(all_results),'radial_points':len(locations),
                     'BVP_calls':0,'tail_calls':0,'continuous_bound':False},sort_keys=True))


if __name__=='__main__':main()
