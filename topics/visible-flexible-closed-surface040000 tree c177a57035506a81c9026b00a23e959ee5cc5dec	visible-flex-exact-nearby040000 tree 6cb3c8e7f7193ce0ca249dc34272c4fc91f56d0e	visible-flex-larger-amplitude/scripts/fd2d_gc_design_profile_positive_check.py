#!/usr/bin/env python3
"""Finite execution/JVP checks of the R131 exact positive clock."""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from fd2d_gc_design_profile import CoastDesignProfile as OldProfile
from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile,positive_coast_clock


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use an unused actual-check report')
    profile=PositiveCoastDesignProfile(args.candidate)
    tau=np.array([0.,.01,.1,.25,.5,.75,.9,.99,1.])
    x=np.unique(np.concatenate([p['s0']+p['L']*tau for p in profile.base.segments]))
    rows=[]
    for T in (.001,.02,.129,.15,.20,.22):
        if not T<profile.model.Tmax:continue
        profile.set_parameter(T);reference={key:np.array(value,copy=True) for key,value in profile.jet(x).items()}
        actual=profile.current.profile(reference['s'])
        step=min(2e-7,T/1000.,(profile.model.Tmax-T)/1000.)
        profile.set_parameter(T+step);plus={key:np.array(value,copy=True) for key,value in profile.jet(x).items()}
        profile.set_parameter(T-step);minus={key:np.array(value,copy=True) for key,value in profile.jet(x).items()}
        profile.set_parameter(T)
        errors={}
        for value,tangent in [('a','a_T'),('a_s','a_s_T'),('a_ss','a_ss_T'),('s','s_T'),('radial_scale','radial_scale_T'),('K','K_T'),('c','c_T')]:
            finite=(plus[value]-minus[value])/(2*step);target=reference[tangent]
            errors[value]=dict(max_absolute=float(abs(finite-target).max()),
                max_scaled=float((abs(finite-target)/(1.+abs(target))).max()))
        row=dict(T=T,step=step,definition=profile.definition(),
            physical_scalar_composition_error={key:float(abs(reference[key]-target).max()) for key,target in zip(('a','a_s','a_ss'),actual)},
            actual_minimum_radial_scale_sample=float(reference['radial_scale'].min()),
            JVP_errors=errors,
            cut_jet=[float(profile.jet([profile.end])[key][0]) for key in ('a','a_s','a_ss')])
        try:
            old=OldProfile(args.candidate);old.set_parameter(T)
            row['old_quintic_chart_accepted']=True
        except FloatingPointError as error:
            row['old_quintic_chart_accepted']=False;row['old_quintic_chart_message']=str(error)
        rows.append(row)
    profile.set_parameter(profile.reference_T)
    old=OldProfile(args.candidate);newref=profile.jet(x);oldref=old.jet(x)
    reference_error={key:float(abs(newref[key]-oldref[key]).max()) for key in ('a','a_s','a_ss','s','radial_scale')}
    endpoint=[]
    for q in (.0001,.01,.2,1.,5.,10000.):
        J,Jq,scale,scaleq=positive_coast_clock(np.array([0.,.5,1.]),q)
        endpoint.append(dict(ratio=q,J=J.tolist(),J_q=Jq.tolist(),scale=scale.tolist(),scale_q=scaleq.tolist()))
    out=dict(schema='fd2d-positive-coast-clock-actual-check-v1',
        candidate=args.candidate.name,candidate_sha256=digest(args.candidate),
        reader_sha256=digest(Path(__file__).with_name('fd2d_gc_design_profile_positive.py')),
        check_source_sha256=digest(__file__),point_count=len(x),parameter_checks=rows,
        same_reference_chart_errors=reference_error,analytic_endpoint_evaluations=endpoint,
        scope='Exact definition/proof is R131; these are actual finite composition and centered-JVP checks, not an interval surface certificate.',
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(out=args.out.name,seconds=out['seconds'],point_count=len(x),
        reference_errors=reference_error,
        T_rows=[dict(T=row['T'],minimum_scale=row['actual_minimum_radial_scale_sample'],
            old_chart_accepted=row['old_quintic_chart_accepted'],max_scaled_JVP=max(v['max_scaled'] for v in row['JVP_errors'].values())) for row in rows])))


if __name__=='__main__':main()
