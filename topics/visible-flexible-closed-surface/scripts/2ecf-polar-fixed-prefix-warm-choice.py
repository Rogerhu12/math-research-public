"""Pay four full fixed-prefix baselines and continue the lowest complete residual."""
import argparse,json,subprocess
from pathlib import Path


def main():
    ap=argparse.ArgumentParser()
    for key in ('work','scripts','warm-state','prepared','normal-audit','prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();w=args.work
    common=['--scripts',str(args.scripts),'--prepare-entry',str(w/'2ecf-polar-c2-g10-split-prepare.py'),
            '--prepared',str(args.prepared),'--normal-audit',str(args.normal_audit),'--initial-damping','0.001']
    def run(tag,args):
        p=Path(str(prefix)+'-'+tag)
        subprocess.run(['python3',str(w/'2ecf-polar-natural-process-receipt.py'),'--prefix',str(p),'--',
            'python3','-u',str(w/'2ecf-polar-fixed-prefix-position-solve.py'),*common,'--prefix',str(p),*args],check=True)
        return p
    prefix=args.prefix
    rows=[]
    for tag,taper in [('copy',0),('short',.06),('long',.18),('zero',None)]:
        start=['--zero'] if taper is None else ['--warm-state',str(args.warm_state),'--taper',str(taper)]
        p=run(tag,start+['--steps','0']);state=Path(str(p)+'-initial.json')
        d=json.loads(state.read_text()); e=d['evaluation']
        rows.append(dict(tag=tag,state=str(state),R2=e['squaredNorm'],metric=e['maxRelativeMetric'],
                         curvature=e['maxCurvature'],held=e['minHeldDistance']))
    best=min(rows,key=lambda r:r['R2'])
    with Path(str(prefix)+'-selection.json').open('x') as o:
        json.dump(dict(rule='minimum unchanged complete weighted residual squared',rows=rows,selected=best),o,indent=2)
    print(json.dumps(dict(baselines=rows,selected=best)),flush=True)
    run('step01',['--state',best['state'],'--steps','1'])


if __name__=='__main__':main()
