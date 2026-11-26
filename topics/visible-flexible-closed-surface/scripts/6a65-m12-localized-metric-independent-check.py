#!/usr/bin/env python3
"""Reproduce independent algebra checks and an explicitly artificial field.

This is not a reconstruction of any previous CI checkpoint. All temporary
arrays and logs remain under the required fresh --out directory.
"""
from __future__ import annotations
import argparse,importlib.util,json,math,os,subprocess,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def algebra(m,cert):
    rng=np.random.default_rng(519023);mesh=[Q(0),Q(1,11),Q(2,7),Q(3,5),Q(1)]
    knots=[Q(0)]*6+mesh[1:-1]+[Q(1)]*6
    C=[[Q(int(v),2**25) for v in row] for row in rng.integers(-100,101,size=(len(knots)-12,8))]
    full=[[Q(0)]*8]*3+C+[[Q(0)]*8]*3
    sp=BSpline(np.array(list(map(float,knots))),np.asarray([[float(v) for v in row] for row in full]),5)
    errors=[0.,0.]
    for lo,hi,b in m.extract_bezier(knots,C):
        for x in (Q(1,9),Q(2,5),Q(7,8)):
            z=lo+(hi-lo)*x
            for order,cs in ((0,b),(1,m.elevated_derivative(b,hi-lo))):
                v=np.array([float(sum(Q(math.comb(5,i))*x**i*(1-x)**(5-i)*row[j] for i,row in enumerate(cs))) for j in range(8)])
                errors[order]=max(errors[order],float(np.max(abs(v-sp(float(z),nu=order)))))
    if max(errors)>=1e-16:raise ArithmeticError('Independent BSpline comparison failed')
    pm=np.arange(-2,3)*3+1;zm=np.arange(3)*3
    row=[Q(int(v),2**38) for v in rng.integers(-100,101,size=8)]
    rounded,_=m.rounded_coefficients(row);angles=np.linspace(0,2*np.pi,2001)
    angular=m.AngularBoxes(cert,32,8,max_mode=4);polar=[]
    for order in (0,1):
        p=m.norm_cosine_integers(rounded,pm,zm,order)
        numeric=sum(float(Q(v,4*m.SCALE*m.SCALE))*np.cos(3*k*angles) for k,v in p.items())
        a=np.array(list(map(float,row)));plane=np.exp(1j*angles[:,None]*pm)@((1j*pm)**order*a[:5])
        height=(np.cos(angles[:,None]*zm) if order==0 else -np.sin(angles[:,None]*zm)*zm)@a[5:]
        polar.append(float(max(abs(numeric-abs(plane)**2-height**2))))
        for j,(lo,hi) in enumerate(angular.enclose(p,4*m.SCALE*m.SCALE)):
            x=np.linspace(j*np.pi/32,(j+1)*np.pi/32,101)
            v=sum(float(Q(c,4*m.SCALE*m.SCALE))*np.cos(k*x) for k,c in p.items())
            if min(v)<float(Q(lo,m.SCALE))-1e-30 or max(v)>float(Q(hi,m.SCALE))+1e-30:
                raise ArithmeticError('Independent angular evaluation left a strict box')
    return {'scipy_BSpline_max_abs_value_and_derivative_errors':errors,
            'autocorrelation_vs_direct_Cartesian_max_abs_errors':polar,
            'all_independent_angular_samples_in_integer_Taylor_boxes':True}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','checker','grid','data','out'):ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=False);began=time.monotonic()
    m=load('independent_localized_checker',args.checker)
    cert=load('independent_localized_interval',args.scripts/'6a65-m12-r137-continuous-domain.py')
    checked=algebra(m,cert);g=json.loads(args.grid.read_text());mesh=np.asarray(g['unit_mesh']);M=g['order']
    if M!=32 or len(mesh)!=363:raise ValueError('This fixed artificial regression recipe uses the original 362-element/order32 grid')
    knots=np.r_[np.repeat(mesh[0],6),mesh[1:-1],np.repeat(mesh[-1],6)]
    c=np.zeros((len(mesh)-2,3*M+2));c[12:18,2*M//3]=[1,-2,3,-3,2,-1];c*=1e-8
    c[12:18,2*M+2]=[1,1,-2,-2,1,1];c[12:18,2*M+2]*=1e-9
    field=args.out/'synthetic-field.npz'
    np.savez_compressed(field,coefficients=c,unit_knots=knots,planar_modes=np.arange(-M,M+1)*3+1,vertical_modes=np.arange(M+1)*3)
    old=args.out/'synthetic-R226.json';new=args.out/'synthetic-sharp.json'
    common=['--scripts',str(args.scripts),'--data',str(args.data),'--field',str(field),'--grid',str(args.grid)]
    commands=[[sys.executable,str(args.scripts/'6a65-m12-entire-half-continuous-correction-bounds.py'),*common,'--out',str(old)],
              [sys.executable,str(args.checker),*common,'--correction-bounds',str(old),'--out',str(new)]]
    env={k:v for k,v in os.environ.items() if k not in ('M12_RECOVERY_TOKEN','GITHUB_TOKEN','GH_TOKEN')};exits=[]
    for i,cmd in enumerate(commands):
        with (args.out/f'stage-{i}.stdout').open('w') as out,(args.out/f'stage-{i}.stderr').open('w') as err:
            result=subprocess.run(cmd,stdout=out,stderr=err,env=env)
        exits.append(result.returncode)
        if result.returncode:raise RuntimeError(f'Actual artificial regression stage {i} exited {result.returncode}')
    a=json.loads(old.read_text());b=json.loads(new.read_text())
    receipt={'schema':'localized-M12-metric-independent-check-v1','verification_source_sha256':m.sha(__file__),
             'checker_source_sha256':m.sha(args.checker),'original_CI_field_consumed':False,
             'all_arrays_are_explicitly_artificial':True,'independent_algebra':checked,'stage_exit_codes':exits,
             'field_sha256':m.sha(field),'grid_sha256':m.sha(args.grid),'data_sha256':m.sha(args.data),
             'R226_report_sha256':m.sha(old),'localized_report_sha256':m.sha(new),
             'old_differential_upper_exact':a['target_orthonormal_differential_l1_upper'],
             'new_differential_upper':b['target_orthonormal_differential_Frobenius_upper'],
             'new_metric_upper':b['metric_triangle_upper'],'metric_gate_pass':b['continuous_metric_below_1e_6'],
             'accepted_subpieces':b['accepted_subpieces'],'radial_subdivisions':b['radial_subdivisions'],
             'angular_refined_rows':b['angular_refined_rows'],'checker_seconds':b['seconds'],
             'total_seconds':time.monotonic()-began,'new_isometry_proved':False}
    p=args.out/'independent-check-receipt.json';p.write_text(json.dumps(receipt,indent=2,allow_nan=False)+'\n')
    print(json.dumps(receipt,indent=2,allow_nan=False))

if __name__=='__main__':main()
