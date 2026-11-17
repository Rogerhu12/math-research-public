#!/usr/bin/env python3
"""Inspect actual m3 protected-arc defects without solving the BVP again.

R35 gives a literal finite trigonometric formula on the protected arc.
The center and the conservative global upper bound below use exact rational
arithmetic on the input binary64 parameters. The angular maxima are samples.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np

SIBLING=Path(__file__).resolve().parent.parent/'resume_m3'
sys.path.insert(0,str(SIBLING))
from couple_m3_smallcut_secant import accepted_anchor


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact(value):
    return dict(numerator=str(value.numerator),denominator=str(value.denominator))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint',type=Path,action='append',required=True)
    p.add_argument('--halfwidth',type=float,default=.21)
    p.add_argument('--samples',type=int,default=8193)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if not a.samples>=2 or not 0<a.halfwidth<math.pi/3:raise ValueError('Invalid arc grid')
    rows=[]
    for path in a.checkpoint:
        r=json.loads(gzip.decompress(path.read_bytes()));accepted_anchor(r,path)
        if r['config']['base_mode']!=3:raise ValueError('Expected the actual m3 family')
        kind=r['config']['core_kind'];settings=r.get('core_round_settings')
        if kind=='adaptive_warped_support' and settings is None:
            lam=0.;scope='Original analytic support core, evaluated on the subsequently declared protected arc'
        elif kind=='exact_m3_raw_local_circle_integral_lift' and r.get('core_control_path')=='raw-mean-primary-compact-v1':
            if settings['bimodal_eta']!=0 or not settings['lock_fundamental']:
                raise ValueError('The R35 eta=0, mean/primary-locked identity is required')
            if settings['halfwidth']!=a.halfwidth:raise ValueError('Do not compare different protected arcs')
            lam=settings['homotopy'];scope='Actual raw mean/primary compact path'
        else:raise ValueError('This formula does not cover the input core definition')
        if not 0<=lam<=1:raise ValueError('Invalid homotopy parameter')
        q=float(r['actual_primary_amplitude']);M=r['config']['modes']
        coeff=np.asarray(r['parameters'][1:],float)*np.asarray(r['central_correction_scales'],float)
        if len(coeff)!=M-1:raise ValueError('Missing actual physical control coefficients')
        c=[Q.from_float(float(v))for v in coeff];l=Q.from_float(float(lam));qq=Q.from_float(q);aa=Q.from_float(a.halfwidth)
        frequency=list(range(2,M+1));weighted=[(1-9*j*j)*v for j,v in zip(frequency,c)]
        center=(1-l)*sum(((-1)**j)*v for j,v in zip(frequency,weighted))
        control_upper=sum(abs(v)for v in weighted)
        upper=(1-l)*(36*abs(qq)*aa*aa+control_upper)
        norm2=sum(v*v for v in c)/2
        z=np.linspace(0.,a.halfwidth,a.samples)
        control=sum(float(v)*((-1)**j)*np.cos(3*j*z)for j,v in zip(frequency,weighted))
        defect=(1-lam)*(8*q*(np.cos(3*z)-1)+control)
        index=int(np.argmax(abs(defect)))
        rows.append(dict(input=str(path.resolve()),input_sha256=sha(path),scope=scope,
            modes=M,q=q,homotopy=lam,halfwidth=a.halfwidth,
            physical_control_coefficients=coeff.tolist(),physical_profile=r['frozen_profile'],
            coefficient_definition='The original binary64 multiplication parameters[1:]*central_correction_scales; the resulting finite values are treated as exact real coefficients in the R35 identity.',
            center_defect=float(center),center_defect_exact=exact(center),
            center_abs_lower=math.nextafter(float(abs(center)),-math.inf)if center else 0.,
            complete_arc_defect_upper=math.nextafter(float(upper),math.inf),complete_arc_defect_upper_exact=exact(upper),
            input_control_curvature_l1_upper=math.nextafter(float(control_upper),math.inf),
            input_control_l2_squared=float(norm2),input_control_l2_squared_exact=exact(norm2),
            sampled_arc_defect_max=float(abs(defect[index])),sampled_peak_offset=float(z[index]),
            sampled_input_control_curvature_max=float(abs(control).max()),
            interpretation='No endpoint convergence follows from lambda alone. These design states may have different full physical metrics; sample maxima are not continuous certificates.'))
    result=dict(scope=__doc__,arguments={k:[str(x)for x in v]if isinstance(v,list)else str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},
        source_sha256={str(x.resolve()):sha(x)for x in [Path(__file__),SIBLING/'couple_m3_smallcut_secant.py']},rows=rows)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    for row in rows:print(json.dumps({k:row[k]for k in ['modes','q','homotopy','center_defect','center_abs_lower','complete_arc_defect_upper','sampled_arc_defect_max','sampled_peak_offset','input_control_curvature_l1_upper']}),flush=True)


if __name__=='__main__':main()
