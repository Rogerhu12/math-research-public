#!/usr/bin/env python3
"""Resumable prefix value consumer with radial ranges and immutable trig cache.

The finite-polynomial formulas and interval backend are imported without
alteration. Only Fourier columns whose entire native polynomial is exactly
zero in BOTH interval endpoints are omitted. Actual field modes are never
discarded. Per-cell results are persisted while the consumer runs, so an
external termination cannot turn a completed prefix into unrecorded work.
Only a report with complete_prefix_domain=true covers the whole prefix.
"""
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('fd2d_prefix_linear_checked_backend',HERE/'fd2d-metric-c2-field-linear-continuous.py')
B=importlib.util.module_from_spec(sp);sys.modules[sp.name]=B;sp.loader.exec_module(B)
sp=importlib.util.spec_from_file_location('fd2d_prefix_normal_arithmetic',HERE/'fd2d-metric-normal-interval-arithmetic.py')
normal=importlib.util.module_from_spec(sp);sys.modules[sp.name]=normal;sp.loader.exec_module(normal)
NORMAL_POLICY=normal.install(B.poly,narrow_owner=B)
sp=importlib.util.spec_from_file_location('fd2d_prefix_radial_range',HERE/'fd2d-metric-radial-range-remainder.py')
radial_range=importlib.util.module_from_spec(sp);sys.modules[sp.name]=radial_range;sp.loader.exec_module(radial_range)
RADIAL_RANGE_POLICY=radial_range.install(B.poly,degree=12)
sp=importlib.util.spec_from_file_location('fd2d_prefix_trig_cache',HERE/'fd2d-metric-cached-trig-range.py')
trig_cache=importlib.util.module_from_spec(sp);sys.modules[sp.name]=trig_cache;sp.loader.exec_module(trig_cache)
TRIG_CACHE_POLICY=trig_cache.install(B)
sp=importlib.util.spec_from_file_location('fd2d_prefix_linear_light_tail',HERE/'fd2d-light-tail-definition-reader.py')
light=importlib.util.module_from_spec(sp);sys.modules[sp.name]=light;sp.loader.exec_module(light)


class CommonCutTailData(light.CheckedTailDefinition):
    """Original common-cut code only uses len(L), besides checked raw bits.

    Supply exact rational lengths rather than any approximate cumulative
    values. The original common-cut interval integral still runs unchanged.
    """
    def __init__(self,path):
        super().__init__(path)
        if self.unscaled_lengths is None:
            self.L=[Q(float(b))-Q(float(a)) for a,b in zip(self.nodes[:-1,0],self.nodes[1:,0])]
        else:self.L=[Q(float(x))*self.radial_scale for x in self.unscaled_lengths]


class SparsePrefix(B.Prefix):
    def polynomials(self,left,right):
        key=(left,right)
        if getattr(self,'_last_polynomial_key',None)==key:return self._last_polynomials
        full=self.geom
        i=min(bisect.bisect_right(full.exact_mesh,left)-1,len(full.x)-2)
        raw=full.power[i];M=full.M
        active=B.np.any((raw.lo!=0)|(raw.hi!=0),axis=0)
        present=[j for j in range(1,M+1) if active[j] or active[M+j] or active[2*M+j]]
        keep=max(present,default=0)
        indices=[0]+[axis*M+j for axis in range(3) for j in range(1,keep+1)]+[3*M+1]
        omitted=B.np.ones(3*M+2,dtype=bool);omitted[indices]=False
        if B.np.any(raw.lo[:,omitted]!=0) or B.np.any(raw.hi[:,omitted]!=0):
            raise AssertionError('Attempt to discard a nonzero actual geometry coefficient')
        self.geom=SimpleNamespace(exact_mesh=full.exact_mesh,x=full.x,M=keep,
            power={i:B.I(raw.lo[:,indices],raw.hi[:,indices])})
        try:data=super().polynomials(left,right)
        finally:self.geom=full
        self._last_polynomial_key=key;self._last_polynomials=data
        self._last_active_geometry_modes=keep
        return data


def rss():return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024


def prior_rows(path,args,model):
    if path is None:return {},None
    meta=json.loads(path.read_text())
    if meta['schema']!='fd2d-prefix-linear-closed-checkpoint-v1':raise ValueError('Unsupported closed checkpoint')
    for key in ('geometry','target','field'):
        if B.diff.identity(getattr(args,key))['sha256']!=meta['inputs'][key]['sha256']:
            raise ValueError('Prior checkpoint has different '+key)
    for key in ('old_consumer','input_identity_reference','row_data'):
        p=Path(meta[key]['file'])
        if not p.exists():p=(HERE if key=='old_consumer' else path.parent)/p.name
        if B.diff.identity(p)['sha256']!=meta[key]['sha256']:raise ValueError('Changed checkpoint binding '+key)
        if key=='row_data':rows_path=p
    if meta['total_radial_cells']!=len(model.mesh)-1 or meta['radial_subdivisions']!=args.radial_subdivisions:
        raise ValueError('Prior radial partition dimensions differ')
    rows={}
    for line in gzip.decompress(rows_path.read_bytes()).decode().splitlines():
        row=json.loads(line);cell,sub=row['cell'],row['subdivision'];key=(cell,sub)
        if key in rows or not 0<=cell<len(model.mesh)-1 or not 0<=sub<args.radial_subdivisions:
            raise ValueError('Invalid or repeated prior exact cell')
        a,b=model.mesh[cell:cell+2]
        left=a+(b-a)*Q(sub,args.radial_subdivisions);right=a+(b-a)*Q(sub+1,args.radial_subdivisions)
        if Q(row['left_exact'])!=left or Q(row['right_exact'])!=right:
            raise ValueError('Prior exact endpoints differ from reconstructed partition')
        if not (math.isfinite(row['linear_operator_upper']) and row['linear_operator_upper']>=0):
            raise ValueError('Invalid prior continuous upper bound')
        rows[key]=row
    expected={(i,j) for i in range(meta['start'],meta['stop']) for j in range(args.radial_subdivisions)}
    if set(rows)!=expected:raise ValueError('Closed checkpoint does not cover its claimed exact cells')
    return rows,B.diff.identity(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True);p.add_argument('--target',type=Path,required=True)
    p.add_argument('--field',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rows',type=Path,required=True);p.add_argument('--start',type=int,default=0)
    p.add_argument('--stop',type=int);p.add_argument('--angular',type=int,default=1024)
    p.add_argument('--maximum-angular',type=int,default=4096)
    p.add_argument('--threshold',type=float,default=1.9e-9);p.add_argument('--radial-subdivisions',type=int,default=1)
    p.add_argument('--progress-every',type=int,default=25)
    p.add_argument('--reuse-checkpoint',type=Path);p.add_argument('--stop-file',type=Path)
    args=p.parse_args();started=time.monotonic()
    progress=args.out.with_name(args.out.stem+'-progress.json')
    if any(x.exists() for x in (args.out,args.rows,progress)):raise FileExistsError('Use new output paths')
    if args.rows.suffix!='.gz':raise ValueError('Use a gzip JSON-lines row stream')
    print(json.dumps(dict(stage='before_field',peak_rss_bytes=rss())),flush=True)
    field=B.Field(args.field)
    if field.meta['region']!='prefix':raise ValueError('Not a prefix field')
    print(json.dumps(dict(stage='field_loaded',peak_rss_bytes=rss(),seconds=time.monotonic()-started)),flush=True)
    import db6f_tail_integrated
    db6f_tail_integrated.IntegratedTail=CommonCutTailData
    model=SparsePrefix(args.geometry,args.target,field);total=len(model.mesh)-1
    stop=total if args.stop is None else min(total,args.stop)
    if not 0<=args.start<stop or min(args.angular,args.radial_subdivisions,args.progress_every)<1:
        raise ValueError('Invalid coverage or subdivision')
    print(json.dumps(dict(stage='geometry_loaded',peak_rss_bytes=rss(),total_cells=total,seconds=time.monotonic()-started)),flush=True)
    prior,prior_binding=prior_rows(args.reuse_checkpoint,args,model)
    maximum=0.;worst=None;done=0;reused=0;computed=0;stopped=False
    with gzip.open(args.rows,'wt',encoding='utf8') as sink:
        for cell in range(args.start,stop):
            a,b=model.mesh[cell:cell+2]
            for sub in range(args.radial_subdivisions):
                left=a+(b-a)*Q(sub,args.radial_subdivisions);right=a+(b-a)*Q(sub+1,args.radial_subdivisions)
                old=prior.get((cell,sub))
                if old is not None and old['linear_operator_upper']<=args.threshold:
                    row={**old,'reused_closed_checkpoint':True};bound=row['linear_operator_upper'];reused+=1
                else:
                    angular=args.angular;bound=model.bound(left,right,angular);attempts=[dict(angular=angular,bound=bound)]
                    while bound>args.threshold and 2*angular<=args.maximum_angular:
                        angular*=2;newbound=model.bound(left,right,angular)
                        attempts.append(dict(angular=angular,bound=newbound));bound=min(bound,newbound)
                    row=dict(cell=cell,subdivision=sub,left_exact=str(left),right_exact=str(right),linear_operator_upper=bound,
                        all_angle_attempts=attempts,exact_nonzero_geometry_modes=model._last_active_geometry_modes,
                        prior_upper_if_refined=None if old is None else old['linear_operator_upper'])
                    computed+=1
                sink.write(json.dumps(row,separators=(',',':'))+'\n');sink.flush()
                if bound>maximum:maximum=bound;worst=row
            done+=1
            state=dict(schema='fd2d-prefix-linear-progress-v1',complete_prefix_domain=False,
                field=B.diff.identity(args.field),start=args.start,next_cell=cell+1,total_radial_cells=total,
                angular=args.angular,radial_subdivisions=args.radial_subdivisions,
                completed_cells=done,maximum=maximum,worst_interval=worst,peak_rss_bytes=rss(),seconds=time.monotonic()-started)
            state.update(reused_intervals=reused,newly_computed_intervals=computed,prior_checkpoint=prior_binding)
            progress.write_text(json.dumps(state,indent=2)+'\n')
            if done==1 or done%args.progress_every==0:
                print(json.dumps(dict(stage='bounded',cells=done,maximum=maximum,peak_rss_bytes=rss(),seconds=state['seconds'])),flush=True)
            if args.stop_file is not None and args.stop_file.exists():
                stop=cell+1;stopped=True;break
    complete=args.start==0 and stop==total
    report=dict(schema='fd2d-continuous-prefix-linear-material-residual-v1',scope=__doc__,script=B.diff.identity(__file__),
        polynomial_consumer=B.diff.identity(HERE/'fd2d-metric-c2-field-linear-continuous.py'),
        interval_arithmetic_adapter=B.diff.identity(HERE/'fd2d-metric-normal-interval-arithmetic.py'),
        interval_arithmetic_policy=NORMAL_POLICY,
        radial_range_adapter=B.diff.identity(HERE/'fd2d-metric-radial-range-remainder.py'),
        radial_range_policy=RADIAL_RANGE_POLICY,
        trigonometry_cache_adapter=B.diff.identity(HERE/'fd2d-metric-cached-trig-range.py'),
        trigonometry_cache_policy=TRIG_CACHE_POLICY,
        tail_storage_adapter=B.diff.identity(HERE/'fd2d-light-tail-definition-reader.py'),
        tail_adapter_scope='Exact checked raw arrays; original common-cut interval accumulation and map definition unchanged',
        geometry_zero_column_rule='Discard only native polynomial columns with both interval endpoints exactly zero; no actual field mode discarded',
        prior_checkpoint=prior_binding,reused_intervals=reused,newly_computed_intervals=computed,
        stopped_at_complete_cell=stopped,
        geometry=B.diff.identity(args.geometry),target=B.diff.identity(args.target),target_data=model.target_data,
        field=B.diff.identity(args.field),field_bindings=field.bindings,geometry_bindings=model.bindings,
        total_radial_cells=total,selected_radial_cells=stop-args.start,radial_subdivisions=args.radial_subdivisions,
        angular_arcs_covering_one_threefold_period=args.angular,all_finite_angular_modes_covered=True,
        maximum_angular_arcs=args.maximum_angular,angular_refinement='Each attempted arc partition covers the complete threefold period; use the minimum of valid whole-period upper bounds',
        complete_prefix_domain=complete,linear_operator_upper=maximum,worst_interval=worst,
        threshold=args.threshold,threshold_met=complete and maximum<=args.threshold,
        target_kind='own frozen analytic metric; exact common bridge transfer is separate',
        physical_radius_derivative_bound=1.,nonlinear_pullback_certified=False,whole_surface_certified=False,
        row_data=B.diff.identity(args.rows),row_format='gzip JSON lines, one exact radial interval per line',
        peak_rss_bytes=rss(),seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),linear_operator_upper=maximum,complete=complete,
        threshold_met=report['threshold_met'],seconds=report['seconds'],peak_rss_bytes=rss())),flush=True)


if __name__=='__main__':main()
