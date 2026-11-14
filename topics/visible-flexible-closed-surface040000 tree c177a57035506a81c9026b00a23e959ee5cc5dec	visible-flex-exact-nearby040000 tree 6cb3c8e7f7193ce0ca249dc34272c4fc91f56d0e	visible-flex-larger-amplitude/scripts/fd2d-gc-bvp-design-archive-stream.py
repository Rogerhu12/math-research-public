#!/usr/bin/env python3
"""Original variable-T design equations with streaming CSC and lossless parts.

This changes storage only. T remains an outer physical design variable and
the prescribed central gap remains a boundary equation. It is not same-g
refinement. Every native defining coefficient and all auxiliary arrays are
saved losslessly, with files below the repository size limit.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import importlib.util, json, resource, sys, time
from pathlib import Path
import fd2d_gc_archive_arrays as archive
import fd2d_gc_stream_csc as streaming

HERE=Path(__file__).resolve().parent


def main():
    source=HERE/'fd2d-gc-bvp-design-warm.py'
    spec=importlib.util.spec_from_file_location('fd2d_archive_design_target',source)
    warm=importlib.util.module_from_spec(spec); spec.loader.exec_module(warm)
    warm.save_npz=archive.save_npz
    warm.__doc__=__doc__; warm.__file__=__file__
    args=sys.argv[1:]; stem=Path(args[args.index('--out-prefix')+1])
    record=stem.parent/'stream-resources'/(stem.name+'.jsonl')
    if record.exists(): raise FileExistsError(record)
    record.parent.mkdir(parents=True,exist_ok=True); started=time.monotonic()
    def state(event):
        return dict(event=event,utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            seconds=time.monotonic()-started,maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            streaming=dict(streaming.STATUS),newton=dict(warm.newton.STATS))
    first=state('start'); first.update(source=archive.identity(__file__),
        parent_frontend=archive.identity(source),archive_source=archive.identity(archive.__file__),
        original_design_equations_unchanged=True,physical_metric_is_fixed=False)
    record.write_text(json.dumps(first)+'\n'); streaming.install()
    try:
        warm.main()
    finally:
        with record.open('a') as f: f.write(json.dumps(state('wrapper_exit'))+'\n')
        path=stem.with_name(stem.name+'-report.json')
        if path.exists():
            report=json.loads(path.read_text()); report.update(parent_frontend=archive.identity(source),
                archive_source=archive.identity(archive.__file__),streaming_source=archive.identity(streaming.__file__),
                original_design_equations_unchanged=True)
            path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(state('design_archive_wrapper_done')),flush=True)


if __name__=='__main__': main()
