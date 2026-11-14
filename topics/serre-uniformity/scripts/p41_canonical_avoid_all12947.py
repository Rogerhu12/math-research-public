#!/usr/bin/env python3
"""Construct an actual canonical divisor avoiding all 129 rational disks."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import runpy
import sys

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode()
    p.write_bytes(gzip.compress(raw,mtime=0) if str(p).endswith('.gz') else raw)
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ['script-dir','build-dir','raw-output','compact-output','output']:
        ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--candidate-start',type=int,default=2)
    args=ap.parse_args();s=args.script_dir.resolve();sys.path.insert(0,str(s))
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_native_r2_linear47 import install
    install_exact_float_mm(r);native=install(r,args.build_dir)
    a=ActualModel(s,derivatives=False);np=a.np
    atlas=a.read('p41_rational_SS_residue_atlas47_complete.json.gz')
    ordinary=a.read('p41_ordinary_point_lifts47.json.gz')
    points=[];labels=[]
    for chart in atlas['charts']:
        points.extend(chart['W_coefficients_0to3'][0]);labels.extend(chart['disk_ids'])
    assert len(points)==110 and len(set(labels))==110
    for point in ordinary['points']:
        points.append(point['W_mod47four']);labels.append('ORD_j'+str(point['j_mod47']).zfill(2))
    assert len(points)==129 and len(set(labels))==129
    W=r.from_json(points);A=r.from_json(a.cusp['canonical_frobenius_matrix'])
    rejected=[]
    for candidate in range(args.candidate_start,args.candidate_start+10000):
        seed,gc=r.rational_trace(A,random.Random(4104715400+candidate))
        g=r.mm(a.K1,gc)
        assert r.equal(r.mm(a.M['A1'],r.conjugate(g)),g)
        values=r.mm(W,g);source_values=r.mm(a.M['W'],g)
        bad=np.flatnonzero(~r.units(values)[:,0]).tolist()
        badsource=np.flatnonzero(~r.units(source_values)[:,0]).tolist()
        if not bad and not badsource:break
        rejected.append({'candidate':candidate,'bad_rational_disks':[labels[i] for i in bad],
                         'bad_faithful_source_rows':len(badsource)})
    else:raise AssertionError('No canonical form disjoint from the actual disks')
    print('CHOSEN actual canonical candidate',candidate,'all129 disks and820 source rows unit',flush=True)
    original=s/'p41_canonical_restriction47.py'
    sys.argv=[str(original),'--script-dir',str(s),'--canonical-candidate',str(candidate),
              '--raw-output',str(args.raw_output),'--compact-output',str(args.compact_output)]
    runpy.run_path(str(original),run_name='__main__')
    algebra=read(args.raw_output)
    assert algebra['canonical_candidate']==candidate
    assert algebra['canonical_coefficients']==r.to_json(gc)
    assert algebra['etale_mod47']
    assert all(degree>1 and mult==1 for degree,mult in algebra['factor_degrees_mod47'])
    out={'level':41,'auxiliary_prime':47,'precision':4,'canonical_candidate':candidate,
         'actual_canonical73_coefficients':r.to_json(g),
         'all129_actual_rational_disks_unit':True,'all820_faithful_source_rows_unit':True,
         'actual_disk_values':[{'disk_id':label,'value_mod47four':value[0]}
                              for label,value in zip(labels,r.to_json(values))],
         'actual_source_values_mod47four':r.to_json(source_values),
         'canonical_degree':106,'canonical_algebra_etale':True,
         'irreducible_factor_degrees_mod47':algebra['factor_degrees_mod47'],
         'canonical_algebra_sha256':sha(args.raw_output),'compact_sha256':sha(args.compact_output),
         'rejected_candidates':rejected,'input_sha256':a.inputs,
         'original_generator_sha256':sha(original),'exact_native_engine':native,
         'source_sha256':sha(__file__)}
    save(args.output,out)
    print('PASS actual canonical divisor avoiding all129 disks',sha(args.output),flush=True)

if __name__=='__main__':main()
