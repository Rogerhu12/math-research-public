"""Freeze one actual trajectory's curvature load for a new physical warp."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    p.add_argument('--cells',type=int,default=3)
    p.add_argument('--blend',type=float,default=.95)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    cfg=json.loads(a.config.read_text());r=json.loads(a.report.read_text())
    if not r.get('completed') or r['config_sha256']!=sha(a.config):
        raise ValueError('Completed same-config actual finite trajectory required')
    path=a.report.parent/r['trajectory']['file']
    if sha(path)!=r['trajectory']['sha256']:raise ValueError('Trajectory binding changed')
    samples={}
    with gzip.open(path,'rt') as stream:
        for line in stream:
            q=json.loads(line);n=q['cell'];j=q['segment']
            if n<a.cells:samples.setdefault((n,j),{})[q['x']]=abs(q['delta_l'])
    cells=[]
    for n in range(a.cells):
        segments=[]
        for j in range(max(j for k,j in samples if k==n)+1):
            v=samples[n,j];xs=sorted(v)
            segments.append(dict(segment=j,x=xs,absoluteDeltaL=[v[x] for x in xs]))
        cells.append(dict(cell=n,segments=segments))
    definition=dict(changedCells=a.cells,referenceConfigSHA256=sha(a.config),
        referenceReport=dict(file=a.report.name,sha256=sha(a.report)),
        referenceTrajectory=r['trajectory'],cells=cells,
        scope='Frozen actual finite samples are design weights; no claim that they solve the new metric equation')
    out=dict(cfg,schema='fd2d-load-balanced-tail-v1',baseConfig=cfg,frozenLinearLoad=definition,
             loadBlend=a.blend,generator_sha256=sha(__file__),
             design_label='New finite free-warp distribution, same endpoints and exact old deep metric')
    a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(config=str(a.output),sha256=sha(a.output),changed_cells=a.cells,blend=a.blend)))


if __name__=='__main__':main()
