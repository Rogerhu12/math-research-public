"""One-time paid material-only R755 observation using the completed R738 calibration and pose."""
import argparse
import base64
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import time
import numpy as np
from r726_closed_spinor_fourier import public
from r734_true_dyadic_tail import I,D,ZERO,ONE
from r755_harmonic_area_bounds import exact,material_cell,test_matrix,selector,quadratic,cap_cell

SOURCE_SHA='4a271c0f8df58456a66a71a59e003c5d887c07d54b8bb53290e7269625f3ff7e'
CAL_SHA='bf12e73ac01668167581f3a4037d115a226984555ca1c80dc146ee7239f14b73'
CUTS=('.075','.085','.09','.145','.15','.205','.21','.22')


def digest(v):return hashlib.sha256(v).hexdigest()
def plain(y):return json.dumps(y,sort_keys=True,allow_nan=False,separators=(',',':'))
class Pause(Exception):pass


def main():
    public();p=argparse.ArgumentParser();p.add_argument('--geometry',required=True)
    p.add_argument('--max-seconds',required=True,type=float);args=p.parse_args()
    admin_start=time.monotonic()
    opt=json.loads(Path(args.geometry).read_bytes());req=json.loads(Path(os.environ['R755_REQUEST']).read_bytes())
    tmp=Path(os.environ['RUNNER_TEMP']);roots=tmp/'r745-sources'
    bind=req['completed_source']
    if (str(bind['source_run'])!='46171769763' or str(bind['source_job'])!='141061557951' or
        bind['source_head']!='ebd6fb99d537edc6500baf8ccd33bc53cab63d01' or bind['source_run_conclusion']!='success'):
        raise ValueError('This is not the frozen completed R738 source.')
    packed=bind.get('terminal_gzip_base64')
    raw=gzip.decompress(base64.b64decode(packed,validate=True)) if packed else (roots/'r738-final.json').read_bytes()
    if len(raw)!=64333 or digest(raw)!=SOURCE_SHA:raise ValueError('Incorrect complete R738 FINAL literal.')
    wide=json.loads(raw)
    meta=bind.get('angular_calibration_64')
    cal=base64.b64decode(meta['base64'],validate=True) if meta else (roots/'r738/r738_angular_calibration_64.npz').read_bytes()
    if len(cal)!=610 or digest(cal)!=CAL_SHA:raise ValueError('Different paid R738 angular calibration.')
    with np.load(io.BytesIO(cal),allow_pickle=False) as zz:calibration=json.loads(zz['meta'].tobytes())['M']
    M=exact(calibration);C=[exact(v) for v in wide['full_independent_cross']['both']['actual_center_for_all_sectors']]
    if wide['kind']!='terminal' or wide['accepted']!=14 or wide['actual_space']!=[32,6,2]:raise ValueError('Wrong actual posture.')
    admin_seconds=time.monotonic()-admin_start
    start=time.monotonic();root=tmp/'r755-paid';root.mkdir(exist_ok=True);fp=root/'units.jsonl'
    fid=digest(plain(dict(schema='r755-v1',geo=opt,sources={k:v for k,v in req['source_sha256'].items() if k.endswith('.py')},
                         initial=SOURCE_SHA,calibration=CAL_SHA,numpy=np.__version__)).encode())
    records={}
    if fp.is_file():
        for line in fp.read_bytes().splitlines():
            q=json.loads(line)
            if q['fingerprint']!=fid or q['key'] in records:raise ValueError('Different or duplicate paid R755 unit.')
            records[q['key']]=q
    initial=len(records);duration=sum(q['scientific_seconds'] for q in records.values())
    def once(key,fn):
        if key in records:return records[key]['value']
        if time.monotonic()-start+opt['reserve_seconds']+2>args.max_seconds:raise Pause(key)
        begin=time.monotonic();v=fn()
        row=dict(fingerprint=fid,key=key,value=v,scientific_seconds=time.monotonic()-begin)
        with fp.open('a') as out:out.write(plain(row)+'\n');out.flush();os.fsync(out.fileno())
        records[key]=row;return v
    edges=[]
    splits=opt['subdivisions']
    for a,b,n in zip(CUTS,CUTS[1:],splits):
        a,b=I(a),I(b)
        edges.extend(a+(b-a)*k/n for k in range(n))
    edges.append(I(CUTS[-1]))
    data=[]
    try:
        def weights():
            if np.__version__!='2.3.5':raise ValueError('Reproducing the original Base64 rule requires its recorded NumPy 2.3.5.')
            nodes,w=np.polynomial.legendre.leggauss(64)
            total=sum((exact(z) for z in w),ZERO)
            if np.any(abs(nodes)>=1) or np.any(w<=0) or total.hi>D('2.00000000001'):
                raise ArithmeticError('Unverified positive normalized source rule.')
            return dict(nodes=64,weight_sum=total.bounds(),new_quadrature_weight_verification=True)
        once('actual_64_positive_weights',weights)
        for i,(l,h) in enumerate(zip(edges,edges[1:])):
            z=once(f'material_{i}',lambda:material_cell(l,h,M))
            data.append(tuple(I(*v) for v in z))
        A,L,S=[sum((q[i] for q in data),ZERO) for i in range(3)]
        cells=[];x=dist=ZERO
        for l,h,(area,dx,dd) in zip(edges,edges[1:],data):
            xr=I(x.lo,(x+dx).hi);d=I(dist.lo,(dist+dd).hi)
            e=S-d;e=I(max(D(0),e.lo),e.hi)
            cells.append((I(l.lo,h.hi),area,xr,d,e));x+=dx;dist+=dd
        poses={'all_centers_lower':(ZERO,ZERO,ZERO),'actual_terminal':C}
        for i,d in enumerate(('-.0115','.0115')):
            for j,h in enumerate(('-.0426','.0426')):poses[f'corner_{i}_{j}']=(I(d),ZERO,I(h))
        reports={};Mc=100*ONE/3
        for name,xyz in poses.items():
            def observe():
                report,gap,B,Di,Do=test_matrix(A,L,xyz)
                directions=[selector(gap,False)]+[[ONE if i==j else ZERO for i in range(3)] for j in range(3)]
                return dict(matrix=report,directions=[[z.bounds() for z in v] for v in directions],
                       gap=[[z.bounds() for z in row] for row in gap],area_vector=[z.bounds() for z in B],
                       D_i=[[z.bounds() for z in row] for row in Di],D_o=[[z.bounds() for z in row] for row in Do])
            obs=once('matrix_'+name,observe);report=dict(obs['matrix'])
            if name in ('actual_terminal','all_centers_lower'):
                gap,Di,Do=([[I(*z) for z in row] for row in obs[k]] for k in ('gap','D_i','D_o'))
                B=[I(*z) for z in obs['area_vector']]
                witness=[]
                for j,rawv in enumerate(obs['directions']):
                    v=[I(*z) for z in rawv];lower=ZERO
                    for first in range(0,len(cells),opt['cap_chunk']):
                        stop=min(first+opt['cap_chunk'],len(cells))
                        def batch():return sum((cap_cell(c,A,L,xyz,B,Di,Do,v,Mc) for c in cells[first:stop]),ZERO).bounds()
                        lower+=I(*once(f'curvature_{name}_{j}_{first}',batch))
                    slack=quadratic(gap,v)-I(lower.lo)
                    witness.append(dict(test=rawv,directed_lower_budget=str(lower.lo),slack_upper=str(slack.hi),
                         excluded_at_this_center_with_absolute_T003=bool(slack.hi<0)))
                report['exact_curvature_witnesses']=witness
            reports[name]=report
        final=dict(kind='terminal',A_over_pi=A.bounds(),L=L.bounds(),S=S.bounds(),raw_center=[z.bounds() for z in C],
               poses=reports,whole_center_rectangle_strict_basic_gate=all(v['strict_PSD_gate_passed'] for k,v in reports.items() if k.startswith('corner_')),
               all_centers_excluded_by_basic_gate=reports['all_centers_lower']['strictly_excluded'],
               all_centers_excluded_with_absolute_T003=any(z['excluded_at_this_center_with_absolute_T003'] for z in reports['all_centers_lower']['exact_curvature_witnesses']),
               positive_solution_or_continuous_path_granted=False)
    except Pause as exc:final=dict(kind='paid_partial',next_unit=str(exc))
    final.update(fingerprint=fid,original_R738_cumulative_science=wide['cumulative_seconds'],original_R738_counts=wide['counts'],
           exact_source_scalar_M=calibration,source_sha256=SOURCE_SHA,original_calibration_sha256=CAL_SHA,
           remaining_old_J_or_RHS_repeated=0,administrative_source_seconds=admin_seconds,
           prior_retained_unit_seconds=duration,new_units=len(records)-initial,retained_units=len(records),
           cumulative_unit_seconds=sum(q['scientific_seconds'] for q in records.values()),new_job_elapsed_seconds=time.monotonic()-start)
    print('R755_FINAL',plain(final),flush=True)


if __name__=='__main__':main()

