#!/usr/bin/env python3
"""Stable forward m2 screen for shallower final contraction and a free coast.

All v4 data before the matching shallow coast remain unchanged. The deep
phase is selected in (atan2(1,.1), pi/2), and T is adjusted to the existing
finite linear cut direction. Full-span eta/zeta amplification, height and
rotational curvature are compared; a small terminal height is not sufficient.
No nonlinear branch or continuous error certificate is asserted by this scan.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,copy,importlib.util,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sp=importlib.util.spec_from_file_location('fd2d_moderate_linear',HERE/'fd2d_m2_linear_trajectory.py')
lin=importlib.util.module_from_spec(sp);sp.loader.exec_module(lin);fm=lin.fm


def subset(candidate,lo,hi=None):
    out=copy.copy(candidate);out.segments=candidate.segments[lo:hi]
    out.end=out.segments[-1]['s1'];out.breaks=np.array([out.segments[0]['s0']]+[p['s1'] for p in out.segments])
    return out


class ModerateFamily:
    def __init__(self,path):
        self.path=Path(path);self.source=json.loads(self.path.read_text());base=fm.Candidate(self.source)
        self.raw_indices={p.get('label'):i for i,p in enumerate(self.source['segments'])}
        self.shallow=self.raw_indices['partial_return_matching_coast']
        self.down=self.raw_indices['redeepen_after_partial_return']
        self.deep=self.raw_indices['final_deep_coast'];self.brake=self.raw_indices['cut_second_jet_brake']
        self.T0=self.source['segments'][self.shallow]['L'];self.vm=math.sin(base.segments[self.shallow]['p0'])
        self.target=np.array(self.source['finite_linear_screen']['terminal_direction'])
        self.prefix_count=self.shallow
        self.prefix=subset(base,0,self.prefix_count)
        self.prefix_trace=lin.LinearTrace(self.prefix,rtol=3e-14,atol=3e-16,max_step=.02)
        self.prefix_fg=self.prefix_trace.endpoint()

    def bundle(self,pdeep,T):
        if pdeep<=math.atan2(1.,self.source['cut_reference']['w']):
            raise ValueError('Deep phase must lie beyond the fixed cut phase')
        if T<0:raise ValueError('The shallow coast cannot have negative length')
        out=copy.deepcopy(self.source);pieces=out['segments']
        pieces[self.shallow]['L']=float(T);pieces[self.down]['p1']=-float(pdeep)
        pieces[self.deep]['p0']=pieces[self.deep]['p1']=-float(pdeep)
        pieces[self.brake]['p0']=-float(pdeep)
        for key in ('finite_linear_screen','metric_diagnostics'):out.pop(key,None)
        out['partial_return_design_parameters']['coast_length']=float(T)
        out['partial_return_design_parameters']['epsilon']=math.pi/2-float(pdeep)
        out['moderate_deep_design']=dict(pdeep=float(pdeep),T=float(T),source_file=self.path.name,
            source_sha256=fm.digest(self.path),source_generator=Path(__file__).name,source_generator_sha256=fm.digest(__file__),
            objective='finite full-span relative second-form gain, plus height and curvature')
        out['status']=dict(metric_frozen=False,nonlinear_prefix_solved=False,nonlinear_tail_matched=False,
            closed_surface=False,reach_certified=False,strong_target_complete=False)
        return out

    def Tmax(self,pdeep):
        candidate=fm.Candidate(self.bundle(pdeep,self.T0))
        deep=next(p for p in candidate.segments if p.get('label')=='final_deep_coast')
        vd=math.sin(deep['p0'])
        return self.T0+deep['L']*vd/self.vm

    def shoot(self,pdeep,T):
        candidate=fm.Candidate(self.bundle(pdeep,T))
        suffix=subset(candidate,self.prefix_count)
        trace=lin.LinearTrace(suffix,self.prefix_fg,rtol=3e-14,atol=3e-16,max_step=.025)
        y=trace.endpoint()
        residual=(y[0]*self.target[1]-y[1]*self.target[0])/(np.linalg.norm(y)*np.linalg.norm(self.target))
        return float(residual),y

    def root_record(self,pdeep,T):
        bundle=self.bundle(pdeep,T);candidate=fm.Candidate(bundle)
        trace,analysis=lin.analyse(candidate,self.target,full_checks=False)
        metric=candidate.metric_diagnostics();metric['background_height_with_tail']=metric['background_height']+self.source['cut']['tail_height_span']
        metric['maximum_meridian_curvature']=max(p['maximum_rotational_meridian_curvature'] for p in analysis['extrema']['pieces'])
        row=dict(pdeep=float(pdeep),T=float(T),Tmax=self.Tmax(pdeep),
            normalized_terminal_residual=analysis['normalized_terminal_direction_residual'],
            terminal_fg=analysis['final_fg'],max_eta=analysis['extrema']['global_extrema']['eta'],
            max_zeta=analysis['extrema']['global_extrema']['zeta'],minimum_b=analysis['minimum_b'],
            minimum_n_reference=analysis['minimum_n_reference'],metric=metric,
            suggested_initial_amplitudes=analysis['suggested_initial_amplitudes'])
        bundle['finite_linear_screen']=dict(normalized_direction_residual=row['normalized_terminal_residual'],
            terminal_height_gain_at_exact_direction_match=row['terminal_fg'][1],terminal_direction=self.target.tolist(),
            prefix_line=self.prefix_fg.tolist(),scope='Stable f,q forward finite linear mode only; nonlinear tail remains unmatched.')
        bundle['full_m2_amplification']={k:row[k] for k in ('max_eta','max_zeta','minimum_b','minimum_n_reference','suggested_initial_amplitudes')}
        bundle['metric_diagnostics']=metric
        bundle['partial_return_design_parameters']['fraction']=T/row['Tmax']
        return row,bundle,trace


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v4.json')
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--pdeep',type=float,nargs='+',default=[1.48,1.49,1.50,1.51,1.52,1.53,1.54])
    args=p.parse_args();start=time.monotonic();family=ModerateFamily(args.source)
    out=dict(scope=__doc__,source_sha256=fm.digest(__file__),candidate_source_sha256=fm.digest(args.source),
        linear_provider_sha256=fm.digest(HERE/'fd2d_m2_linear_trajectory.py'),prefix_count=family.prefix_count,
        prefix_fg=family.prefix_fg.tolist(),rows=[],roots=[])
    report_path=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    bundles=[]
    for deep in args.pdeep:
        Tmax=family.Tmax(deep);previous=None
        for fraction in (0.,.05,.15,.3,.5,.75,.95):
            T=fraction*Tmax
            try:
                residual,y=family.shoot(deep,T)
                row=dict(pdeep=deep,T=T,fraction=fraction,Tmax=Tmax,residual=residual,terminal_fg=y.tolist())
                if previous is not None and previous[1]*residual<0:
                    root=brentq(lambda value:family.shoot(deep,value)[0],previous[0],T,xtol=5e-13,rtol=1e-14)
                    record,bundle,trace=family.root_record(deep,root);out['roots'].append(record);bundles.append(bundle)
                    print(json.dumps(dict(event='root',**record)),flush=True)
                previous=T,residual
            except Exception as exc:
                row=dict(pdeep=deep,T=T,fraction=fraction,error=repr(exc));previous=None
            out['rows'].append(row);report_path.write_text(json.dumps(out,indent=2)+'\n')
            print(json.dumps(row),flush=True)
    accepted=[(r,b) for r,b in zip(out['roots'],bundles) if abs(r['normalized_terminal_residual'])<1e-7
        and r['metric']['background_height_with_tail']<1.3786410585615192
        and r['metric']['maximum_meridian_curvature']<1/.136]
    if accepted:
        record,bundle=min(accepted,key=lambda pair:max(pair[0]['max_eta']['absolute'],pair[0]['max_zeta']['absolute']))
        bundle['status']['metric_frozen']=True
        path=args.out_prefix.with_name(args.out_prefix.name+'-selected.json');path.write_text(json.dumps(bundle,indent=2)+'\n')
        out['selected']=dict(file=path.name,sha256=fm.digest(path),root=record)
    out.update(accepted_finite_roots=len(accepted),seconds=time.monotonic()-start,
               all_root_candidates=bundles,nonlinear_solution=False,continuous_interval_certificate=False)
    report_path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(event='complete',roots=len(out['roots']),accepted=len(accepted),selected=out.get('selected'),seconds=out['seconds'])),flush=True)


if __name__=='__main__':main()
