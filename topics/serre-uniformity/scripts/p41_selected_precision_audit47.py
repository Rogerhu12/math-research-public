#!/usr/bin/env python3
"""Audit persisted selected precision data and aggregate the actual unit logs."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path

Q4=47**4
Q6=47**6


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def add(x,y):return ((x[0]+y[0])%Q4,(x[1]+y[1])%Q4)
def conjugate(x,q):return (x[0],-x[1]%q)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision-data',type=Path,required=True)
    ap.add_argument('--constant-dag',type=Path,required=True)
    ap.add_argument('--selection',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();p,d,s=map(read,[args.precision_data,args.constant_dag,args.selection])
    assert p['complete'] and p['precision']==6 and p['modulus']==Q6
    assert p['bindings']['constant_dag_sha256']==sha(args.constant_dag)
    assert p['bindings']['selection_sha256']==sha(args.selection)
    for key,node in p['nodes'].items():
        old=d['nodes'][key]
        for col in ['A','B']:
            assert [c%Q4 for c in node[col]]==old[col]
        if key!='1':
            assert [[c%Q4 for c in v] for v in node['kernel']]==old['kernel']
            parent=p['nodes'][node['parent']]
            assert node['source_A']==parent['A'] and node['source_B']==parent['B']
    assert len(p['near_CM4_logarithms'])==len(p['requested_nodes'])==200
    index_nodes={}
    for rec in s['near_CM4_node_inventory']:
        assert rec['near_CM4_row_count']==1
        for n in rec['indices']:index_nodes.setdefault(str(n),[]).append(rec['node'])
    for rec in s['near_CM4_rows_inventory']:
        node=p['nodes'][rec['node']];log=p['near_CM4_logarithms'][rec['node']]
        assert [c%Q4 for c in node['B']]==rec['B_mod47_to4']
        assert [c%Q4 for c in log['u_mod47_sixth']]==rec['u_mod47_to4']
    aggregates={}
    for n in d['indices']:
        keys=index_nodes.get(str(n),[]);models=Counter();us=Counter();logs=Counter()
        logu=logj=(0,0)
        for key in keys:
            node=p['nodes'][key];value=p['near_CM4_logarithms'][key]
            models[(tuple(node['A']),tuple(node['B']))]+=1
            us[tuple(value['u_mod47_sixth'])]+=1
            logs[(tuple(value['log_u_mod47_fourth']),tuple(value['log_j_minus1728_mod47_fourth']))]+=1
            logu=add(logu,value['log_u_mod47_fourth']);logj=add(logj,value['log_j_minus1728_mod47_fourth'])
        assert models==Counter({(conjugate(A,Q6),conjugate(B,Q6)):count for (A,B),count in models.items()})
        assert us==Counter({conjugate(u,Q6):count for u,count in us.items()})
        assert logs==Counter({(conjugate(u,Q4),conjugate(j,Q4)):count for (u,j),count in logs.items()})
        assert logu[1]==logj[1]==0
        aggregates[str(n)]={'near_CM4_rows':len(keys),'log_u_sum_mod47_fourth':logu,
                            'log_j_minus1728_sum_mod47_fourth':logj,
                            'full_models_u_and_logs_Frobenius_closed':True}
    out={'scope':'Persisted selected six-digit kernel data audit and near-CM4 unit-log sums',
         'source_sha256':sha(__file__),
         'input_sha256':{str(v.name):sha(v) for v in [args.precision_data,args.constant_dag,args.selection]},
         'all_saved_nodes_project_to_original_four_digit_DAG':True,
         'all_saved_parent_models_match':True,'all_54_Frobenius_checks':True,
         'target_count':200,'saved_node_count':len(p['nodes']),
         'lifted_source_kernel_count':len(p['lifted_source_kernels']),
         'lifted_source_kernels_by_prime':dict(sorted(Counter(k.split(':')[0] for k in p['lifted_source_kernels']).items(),key=lambda z:int(z[0]))),
         'aggregates':aggregates,
         'boundary':'These sums concern only the 200 near-CM4 rows; complete f_B unit norms and global heights are separate inputs'}
    raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
    args.output.write_bytes(gzip.compress(raw,mtime=0))
    print('audit complete',len(p['nodes']),'nodes',len(p['lifted_source_kernels']),'source kernels','SHA',sha(args.output))


if __name__=='__main__':main()
