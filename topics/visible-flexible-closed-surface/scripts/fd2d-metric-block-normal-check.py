"""Tiny synthetic block evidence; no actual normal/F/J or sparse LU is run."""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace
import numpy as np
import fd2d_gc_block_normal_solve as solver


class SmallNormal(SimpleNamespace):
    def hff(self):raise AssertionError('Whole Hff construction is forbidden in this fixture')
    def scaled(self,*args,**kwargs):raise AssertionError('Whole normal.scaled is forbidden in this fixture')


def identity(path):
    p=Path(path);raw=p.read_bytes()
    return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def fingerprint(normal):
    h=hashlib.sha256()
    for a in normal.diagonal+normal.upper+[normal.Hfp,normal.Hpp,normal.gf,normal.gp,
            normal.field_norm_squared,normal.parameter_norm_squared]:
        h.update(str(a.shape).encode());h.update(a.dtype.str.encode());h.update(a.tobytes())
    return h.hexdigest()


def construct(widths,seed):
    P=54;widths=np.array(widths,int);offsets=np.r_[0,np.cumsum(widths)]
    N=len(widths);count=int(offsets[-1]);rng=np.random.default_rng(seed)
    n=SmallNormal(mapping=SimpleNamespace(N=N,P=P,count=count,widths=widths,offsets=offsets),
        diagonal=[np.zeros((w,w)) for w in widths],upper=[np.zeros((widths[j],widths[j+1])) for j in range(N-1)],
        Hfp=np.zeros((count,P)),Hpp=np.zeros((P,P)),gf=np.zeros(count),gp=np.zeros(P),
        field_norm_squared=np.zeros(count),parameter_norm_squared=np.zeros(P))
    independent_H=np.zeros((count,count));independent_Hfp=np.zeros((count,P));independent_gf=np.zeros(count)
    groups=[(j,) for j in range(N)]+[(j,j+1) for j in range(N-1)]
    for index,nodes in enumerate(groups):
        rows=7+(index%3);r=rng.normal(size=rows)
        B=rng.normal(size=(rows,P));B[:,-1]=0.
        global_A=np.zeros((rows,count));As=[]
        for j in nodes:
            A=rng.normal(size=(rows,int(widths[j])))
            if count and offsets[j]<=count-1<offsets[j+1]:
                A[:,count-1-offsets[j]]=0.
            As.append(A);global_A[:,offsets[j]:offsets[j+1]]=A
            n.diagonal[j]+=A.T@A
            n.Hfp[offsets[j]:offsets[j+1]]+=A.T@B
            n.gf[offsets[j]:offsets[j+1]]+=A.T@r
            n.field_norm_squared[offsets[j]:offsets[j+1]]+=np.sum(A*A,axis=0)
        if len(nodes)==2:n.upper[nodes[0]]+=As[0].T@As[1]
        n.Hpp+=B.T@B;n.gp+=B.T@r;n.parameter_norm_squared+=np.sum(B*B,axis=0)
        independent_H+=global_A.T@global_A
        independent_Hfp+=global_A.T@B;independent_gf+=global_A.T@r
    return n,independent_H,independent_Hfp,independent_gf


def run(prefix):
    started=time.monotonic();sources={k:identity(p) for k,p in dict(checker=__file__,solver=solver.__file__).items()}
    results=[]
    for label,widths,seed in [('central_and_cut_zeros',[0,0,5,3,4,0],2026111201),
                              ('interior_zero_disconnects',[0,2,0,0,3,0],2026111202),
                              ('all_field_nodes_fixed',[0,0,0],2026111203)]:
        normal,H,Hfp,gf=construct(widths,seed);before=fingerprint(normal);progress=[]
        def callback(*args):
            if not all(type(a) in (str,int,float,bool) for a in args):
                raise AssertionError('Progress includes a non-Python scalar')
            progress.append(list(args))
        answer=solver.solve_scaled_normal_field(normal,damping=1e-7,progress=callback)
        fs=1/np.maximum(np.sqrt(normal.field_norm_squared),1e-12)
        ps=1/np.maximum(np.sqrt(normal.parameter_norm_squared),1e-12)
        # Dense ONLY for this at-most 12 by 12 synthetic system; no inverse,
        # LU, sparse constructor, or whole physical matrix is used.
        dense=(fs[:,None]*H)*fs[None,:]+np.eye(len(fs))*1e-7
        rhs=np.column_stack((fs*gf,(fs[:,None]*Hfp)*ps[None,:]))
        residual=dense@answer['solved']-rhs
        magnitude=np.abs(dense)@np.abs(answer['solved'])+np.abs(rhs)
        backward=np.divide(np.abs(residual),magnitude,out=np.zeros_like(residual),where=magnitude>0)
        max_abs=float(np.max(np.abs(residual),initial=0.));max_backward=float(np.max(backward,initial=0.))
        expected=dict(field_scale=fs,parameter_scale=ps,hfp=(fs[:,None]*normal.Hfp)*ps[None,:],
            hpp=(ps[:,None]*normal.Hpp)*ps[None,:]+np.eye(len(ps))*1e-7,
            gf=fs*normal.gf,gp=ps*normal.gp)
        scaled_match={k:bool(np.array_equal(answer[k],v)) for k,v in expected.items()}
        zero_column=bool(not len(fs) or np.all(answer['solved'][-1]==0.))
        zero_parameter=bool(np.all(answer['solved'][:,-1]==0.))
        checks=dict(normal_payload_unchanged=fingerprint(normal)==before,
            original_global_scales_and_small_blocks_identical=all(scaled_match.values()),
            solution_shape=answer['solved'].shape==(len(fs),55),
            returned_solution_finite=bool(np.all(np.isfinite(answer['solved']))),
            deliberately_zero_field_column_stays_zero=zero_column,
            deliberately_zero_parameter_RHS_stays_zero=zero_parameter,
            independent_dense_backward_error_small=bool(max_backward<2e-12),
            all_progress_are_small_Python_scalars=len(progress)==len(widths))
        results.append(dict(case=label,seed=seed,node_widths=widths,field_dimension=len(fs),
            right_hand_sides=55,checks=checks,scaled_item_matches=scaled_match,
            independent_dense_absolute_residual_maximum=max_abs,
            independent_dense_componentwise_backward_maximum=max_backward,
            no_dense_inverse_or_LU=True,no_actual_normal_constructed=True,
            block_solver_info=answer['info']))
    unchanged={k:identity(v['path'])==v for k,v in sources.items()}
    report=dict(schema='fd2d-R159-tiny-block-Cholesky-check-v1',utc=datetime.now(timezone.utc).isoformat(),
        passed=all(all(case['checks'].values()) for case in results) and all(unchanged.values()),
        sources=sources,sources_unchanged=unchanged,cases=results,
        no_physical_F_J_or_BVP=True,no_whole_actual_normal_or_LU=True,
        scope='Three synthetic unscaled block Gram systems, at most twelve field variables and 55 RHS; direct dense residual only, no reference inverse',
        seconds=time.monotonic()-started,peak_rss_kib=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    target=Path(str(prefix)+'-report.json');target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(target),passed=report['passed'],seconds=report['seconds'],
        peak_rss_kib=report['peak_rss_kib'],cases=[dict(case=r['case'],checks=r['checks'],
            residual=r['independent_dense_absolute_residual_maximum'],backward=r['independent_dense_componentwise_backward_maximum']) for r in results]),ensure_ascii=False))
    return 0 if report['passed'] else 1


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out-prefix',required=True)
    args=parser.parse_args();sys.exit(run(args.out_prefix))
