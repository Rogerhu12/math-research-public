#!/usr/bin/env python3
"""Produce only the missing tail C2 field, retaining an existing actual prefix.

This avoids loading/fitting the prefix again. The prefix manifest is bound
by its actual hash; all tail fitting and saved-field checks are real new
computations. The final report does not promote sampled residuals to a
continuous or nonlinear metric certificate.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('fd2d_c2_tail_recovery_producer',HERE/'fd2d-metric-c2-material-field-candidate.py')
source=importlib.util.module_from_spec(sp);sys.modules[sp.name]=source;sp.loader.exec_module(source)
np=source.np


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix-field',type=Path,required=True);p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--target',type=Path,required=True);p.add_argument('--tail',type=Path,required=True)
    p.add_argument('--tail-packet',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True)
    p.add_argument('--cells',type=int,default=1024);p.add_argument('--modes',type=int,default=192)
    p.add_argument('--angular',type=int,default=512);p.add_argument('--quadrature',type=int,default=6)
    p.add_argument('--iterations',type=int,default=4);p.add_argument('--tail-start',type=float,default=.4)
    p.add_argument('--cut-zero-width',type=float,default=.01);p.add_argument('--inner-zero-width',type=float,default=.002)
    args=p.parse_args();started=time.monotonic()
    if args.out_dir.exists():raise FileExistsError('Use a new directory')
    meta=json.loads(args.geometry.read_text());pf=json.loads(args.prefix_field.read_text())
    if pf['region']!='prefix' or meta['tail_manifest_sha256']!=source.screen.r105.sha(args.tail):
        raise ValueError('Wrong prefix definition or own tail')
    for shard in pf['shards']:
        path=Path(shard['file'])
        if not path.exists():path=args.prefix_field.parent/path.name
        if source.screen.identity(path)['sha256']!=shard['sha256']:raise ValueError('Existing prefix bytes changed')
    args.out_dir.mkdir(parents=True);producer=source.screen.identity(__file__)
    tail=source.screen.Tail(args.tail,args.tail_packet,args.angular)
    knots=np.linspace(args.tail_start,float(tail.reader.r[-1]),args.cells+1)
    region=source.Region('tail',tail,knots,args.angular,args.quadrature)
    fixed=region.fixed(args.cut_zero_width,args.inner_zero_width);weights=np.ones(len(region.h));iterations=[]
    for it in range(args.iterations):
        jets,stats,radial=region.fit(args.modes,weights,fixed)
        entry=dict(iteration=it+1,**stats,seconds=time.monotonic()-started);iterations.append(entry)
        print(json.dumps(dict(stage='fit_tail',**entry)),flush=True)
        floor=max(float(np.median(radial)),1e-13)
        weights*=np.sqrt(np.maximum(1,radial/floor));weights/=np.mean(weights);weights=np.clip(weights,1e-4,1e4)
    actual=jets[:,:,:,:args.modes+1].copy();actual[:,:,1]/=region.scale;actual[:,:,2]/=region.scale**2
    for i,f,j in zip(*np.nonzero(fixed.reshape(-1,2,3))):actual[i,f,j]=0
    field,real=source.write_field(args.out_dir,'tail',region,actual,producer)
    observed=source.screen_saved(region,real,args.angular)
    report=dict(schema='fd2d-recovered-tail-c2-field-production-v1',status='ACTUAL_FIELDS_DEFINED__METRIC_UNVERIFIED',
        scope=__doc__,script=producer,shared_producer=source.screen.identity(HERE/'fd2d-metric-c2-material-field-candidate.py'),
        geometry=source.screen.identity(args.geometry),target=source.screen.identity(args.target),
        tail=source.screen.identity(args.tail),tail_packet=source.screen.identity(args.tail_packet),
        fields=[source.screen.identity(args.prefix_field),field],old_tail_sampled_metric=region.old_max,
        fit_iterations=iterations,actual_saved_tail_sampled_linear_residual=observed,
        prefix_recomputed=False,prefix_source_session=34070,prefix_source_session_final_exit_code=137,
        prefix_field_was_saved_before_that_exit=True,
        finite_field_definitions_present=True,continuous_linear_residual_certified=False,
        nonlinear_pullback_certified=False,README_complete=False,seconds=time.monotonic()-started)
    out=args.out_dir/'production.json';out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(out),actual_saved_tail=observed,seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
