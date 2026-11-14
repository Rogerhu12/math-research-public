#!/usr/bin/env python3
"""Checkpointed entry point for the unchanged actual-prefix linear consumer.

The finite-polynomial formulas and interval backend are imported without
alteration. Per-cell results are persisted while the consumer runs, so an
external termination cannot turn a completed prefix into unrecorded work.
Only a report with complete_prefix_domain=true covers the whole prefix.
"""
import argparse
from fractions import Fraction as Q
import gzip
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('fd2d_prefix_linear_checked_backend',HERE/'fd2d-metric-c2-field-linear-continuous.py')
B=importlib.util.module_from_spec(sp);sys.modules[sp.name]=B;sp.loader.exec_module(B)
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


def rss():return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True);p.add_argument('--target',type=Path,required=True)
    p.add_argument('--field',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rows',type=Path,required=True);p.add_argument('--start',type=int,default=0)
    p.add_argument('--stop',type=int);p.add_argument('--angular',type=int,default=256)
    p.add_argument('--threshold',type=float,default=1.9e-9);p.add_argument('--radial-subdivisions',type=int,default=1)
    p.add_argument('--progress-every',type=int,default=25)
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
    model=B.Prefix(args.geometry,args.target,field);total=len(model.mesh)-1
    stop=total if args.stop is None else min(total,args.stop)
    if not 0<=args.start<stop or min(args.angular,args.radial_subdivisions,args.progress_every)<1:
        raise ValueError('Invalid coverage or subdivision')
    print(json.dumps(dict(stage='geometry_loaded',peak_rss_bytes=rss(),total_cells=total,seconds=time.monotonic()-started)),flush=True)
    maximum=0.;worst=None;done=0
    with gzip.open(args.rows,'wt',encoding='utf8') as sink:
        for cell in range(args.start,stop):
            a,b=model.mesh[cell:cell+2]
            for sub in range(args.radial_subdivisions):
                left=a+(b-a)*Q(sub,args.radial_subdivisions);right=a+(b-a)*Q(sub+1,args.radial_subdivisions)
                bound=model.bound(left,right,args.angular)
                row=dict(cell=cell,subdivision=sub,left_exact=str(left),right_exact=str(right),linear_operator_upper=bound)
                sink.write(json.dumps(row,separators=(',',':'))+'\n');sink.flush()
                if bound>maximum:maximum=bound;worst=row
            done+=1
            state=dict(schema='fd2d-prefix-linear-progress-v1',complete_prefix_domain=False,
                field=B.diff.identity(args.field),start=args.start,next_cell=cell+1,total_radial_cells=total,
                angular=args.angular,radial_subdivisions=args.radial_subdivisions,
                completed_cells=done,maximum=maximum,worst_interval=worst,peak_rss_bytes=rss(),seconds=time.monotonic()-started)
            progress.write_text(json.dumps(state,indent=2)+'\n')
            if done==1 or done%args.progress_every==0:
                print(json.dumps(dict(stage='bounded',cells=done,maximum=maximum,peak_rss_bytes=rss(),seconds=state['seconds'])),flush=True)
    complete=args.start==0 and stop==total
    report=dict(schema='fd2d-continuous-prefix-linear-material-residual-v1',scope=__doc__,script=B.diff.identity(__file__),
        polynomial_consumer=B.diff.identity(HERE/'fd2d-metric-c2-field-linear-continuous.py'),
        tail_storage_adapter=B.diff.identity(HERE/'fd2d-light-tail-definition-reader.py'),
        tail_adapter_scope='Exact checked raw arrays; original common-cut interval accumulation and map definition unchanged',
        geometry=B.diff.identity(args.geometry),target=B.diff.identity(args.target),target_data=model.target_data,
        field=B.diff.identity(args.field),field_bindings=field.bindings,geometry_bindings=model.bindings,
        total_radial_cells=total,selected_radial_cells=stop-args.start,radial_subdivisions=args.radial_subdivisions,
        angular_arcs_covering_one_threefold_period=args.angular,all_finite_angular_modes_covered=True,
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
