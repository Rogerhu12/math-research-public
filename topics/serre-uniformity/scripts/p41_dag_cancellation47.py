#!/usr/bin/env python3
"""Match all actual D0 linear factors and inventory true-CM4 near poles."""
import argparse
from collections import Counter,defaultdict
import gzip
import hashlib
import json
from math import gcd,isqrt
from pathlib import Path


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def valuation(x):
    return next((v for v in range(4) if any(c%47**(v+1) for c in x)),4)


def rho(n):
    bound=isqrt(n)
    count=sum(a*a+b*b==n and gcd(a,b)==1
              for a in range(-bound,bound+1) for b in range(-bound,bound+1))
    assert count%4==0
    return count//4


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cm-dag',type=Path,required=True)
    ap.add_argument('--cm-level',type=Path,required=True)
    ap.add_argument('--source-dag',type=Path,required=True)
    ap.add_argument('--endpoints',type=Path,required=True)
    ap.add_argument('--primitives',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    d,l,s,e,a=map(read,[args.cm_dag,args.cm_level,args.source_dag,args.endpoints,args.primitives])
    assert l['complete'] and e['complete_regular_parts']
    assert l['constant_dag_sha256']==sha(args.cm_dag)
    assert e['constant_dag_sha256']==sha(args.source_dag)
    I=e['source_necklace_indices_1based'];source_set=set(I)
    ell={r['kind']:set(r['indices_1based']) for r in a['elliptic_charts']}
    near=[];exact=[];per_index={};matches={};near_nodes=defaultdict(list)
    all_actual=all_expected=cm3=0
    for n,targets in d['targets'].items():
        actual=defaultdict(list);expected=defaultdict(list);horizontal=[]
        for target in targets:
            k=target['node'];rec=l['nodes'][k];node=d['nodes'][k]
            if rec['reference_key']=='9':
                for row,label in enumerate(rec['image_indices_1based']):
                    if label in source_set:
                        actual[(label,tuple(rec['reference_parameter']))].append(
                            {'CM4_node':k,'CM4_source_row_0based':row})
            coarse=rec.get('coarse')
            if not coarse:continue
            if coarse['reference_key']=='CM3':
                cm3+=sum(label in ell['CM3'] for label in coarse['image_indices_1based'])
                continue
            hit=[(row,label) for row,label in enumerate(coarse['image_indices_1based']) if label in ell['CM4']]
            if not hit:continue
            B=node['B'];v=valuation(B)
            if B==[0,0]:
                assert len(hit)==20
                horizontal.append(k)
                exact.append({'index':int(n),'node':k,'CM4_rows':20})
            else:
                assert v==1
                for row,label in hit:
                    entry={'index':int(n),'node':k,'CM4_source_row_0based':row,
                           'coarse_necklace_index_1based':label,'B_valuation':v,
                           'B_mod47_to4':B,'stack_parameter_mod47_to4':coarse['stack_parameter'],
                           'u_mod47_to4':coarse['invariant_parameter'],
                           'required_B_precision_exponent':5}
                    near.append(entry);near_nodes[k].append(entry)
        assert len(horizontal)==rho(int(n)),(n,len(horizontal),rho(int(n)))
        for target in s['targets'][n]:
            k=target['node']
            for pole in e['nodes'][k]['CM4_log_factors']:
                key=(I[pole['source_row_0based']],tuple(pole['weierstrass_root_alpha']))
                expected[key].append({'source_node':k,'source_row_0based':pole['source_row_0based'],
                                      'source_tY':pole['source_tY'],'multiplicity':2})
        actual_count=Counter({k:len(v) for k,v in actual.items()})
        expected_count=Counter({k:2*len(v) for k,v in expected.items()})
        assert actual_count==expected_count,(n,actual_count-expected_count,expected_count-actual_count)
        all_actual+=sum(actual_count.values());all_expected+=sum(expected_count.values())
        match=[]
        for (label,alpha),left in sorted(actual.items()):
            right=expected[(label,alpha)]
            match.append({'source_necklace_index_1based':label,'physical_root_alpha':alpha,
                          'CM4_norm_rows':left,'endpoint_poles':right,
                          'multiplicity':len(left),'exact_counter_equality':True})
        matches[n]=match
        per_index[n]={'horizontal_CM4_nodes':len(horizontal),'rho_cyclic':rho(int(n)),
                      'D0_collision_norm_rows':sum(actual_count.values()),
                      'endpoint_poles':sum(expected_count.values())//2,
                      'D0_linear_factors_match':True}
    nodes=[]
    for key,rows in sorted(near_nodes.items()):
        node=d['nodes'][key]
        nodes.append({'node':key,'indices':sorted(set(r['index'] for r in rows)),
                      'near_CM4_row_count':len(rows),'source_rows_0based':[r['CM4_source_row_0based'] for r in rows],
                      'coarse_labels_1based':[r['coarse_necklace_index_1based'] for r in rows],
                      'kernel_path':node['path']})
    out={'scope':'Actual D0 factor matching plus selective static-CM4 precision inventory',
         'modulus':47**4,'source_sha256':sha(__file__),
         'input_sha256':{str(p.name):sha(p) for p in [args.cm_dag,args.cm_level,args.source_dag,args.endpoints,args.primitives]},
         'all_54_D0_counters_match':True,'D0_norm_rows':all_actual,'endpoint_poles_doubled':all_expected,
         'near_CM4_rows':len(near),'near_CM4_distinct_nodes':len(nodes),
         'exact_CM4_rows':20*len(exact),'exact_CM4_horizontal_nodes':len(exact),
         'all_horizontal_counts_match_Gaussian_cyclic_rho':True,'CM3_rows':cm3,
         'per_index':per_index,'D0_matches':matches,
         'near_CM4_node_inventory':nodes,'near_CM4_rows_inventory':near,'horizontal_CM4_nodes':exact,
         'precision_boundary':'u mod47^4 equality alone is not enough to merge static true-pole logarithms; lift every listed kernel path, or independently certify equality at the needed precision',
         'cancellation':'For D0=Y-X, the f_B factor alpha/(alpha-tY) cancels the endpoint factor (tY-alpha)/(-alpha), with actual multiplicity2; true static m*log(j-1728) remains'}
    args.output.write_bytes(gzip.compress(json.dumps(out,sort_keys=True,separators=(',',':')).encode(),mtime=0))
    print('matched',all_actual,'D0 rows; static near-CM4',len(near),'rows',len(nodes),'nodes; exact',20*len(exact),'rows; SHA',sha(args.output))


if __name__=='__main__':main()
