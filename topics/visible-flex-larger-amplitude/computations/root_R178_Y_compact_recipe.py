#!/usr/bin/env python3
"""Store original binary second jets and reconstruct every rational Y coefficient.

The large polynomial is cheap derived data. This compact archive preserves
the ACTUAL binary coefficients without rerunning floating quadrature/libm.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw)if p.suffix=='.gz'else raw)
def qr(q):return [str(q.numerator),str(q.denominator)]
def fq(q):return F(*map(int,q))
def hermite(y0,y1,d0,d1,dd0,dd1):return [y0,y0+d0/5,y0+2*d0/5+dd0/20,y1-2*d1/5+dd1/20,y1-d1/5,y1]
def encode(v):return (json.dumps(v,separators=(',',':'))+'\n').encode()
def save(p,v):
    if p.exists():raise FileExistsError(p)
    raw=encode(v);p.write_bytes(gzip.compress(raw,mtime=0)if p.suffix=='.gz'else raw)
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--definition',type=Path,required=True);ap.add_argument('--jets',type=Path,required=True)
    ap.add_argument('--polynomials',type=Path);ap.add_argument('--out-prefix',type=Path);ap.add_argument('--compact',type=Path);ap.add_argument('--restore-to',type=Path)
    a=ap.parse_args();started=time.monotonic();counts={}
    def gate(k,v):
        counts[k]=counts.get(k,0)+1
        if not v:raise ArithmeticError(k)
    definition=load(a.definition);jets=load(a.jets)
    gate('same_original_first_jets',definition['all_gates'] and jets['all_gates'] and definition['original_jets']['sha256']==sha(a.jets))
    nodes={v['saved_node']:v for v in definition['canonical_nodes']};jp={(r['raw_cell'],r['raw_segment'],r['part']):r for r in jets['pieces']}
    def values(row,side):
        j=jp[row['cell'],row['segment'],row['part']];node=j['inner_node' if side==0 else 'outer_node'];nr=nodes[node];df=fq(nr['binary_factor']);Y=list(map(fq,nr['exact_Y']));ep=j['endpoint_jets'][side]
        cf=(F.from_float(ep['s'])+3*F.from_float(ep['l']))/2
        first=list(map(F.from_float,j['dP'+str(side)]+j['dK'+str(side)]));DY=[df*v+cf*y for v,y in zip(first,Y)]
        return Y,DY
    if a.compact is None:
        gate('fresh_compact_arguments',a.polynomials is not None and a.out_prefix is not None and a.restore_to is None)
        poly=load(a.polynomials);gate('original_full_polynomial_identity',sha(a.polynomials)==definition['polynomial_file']['sha256'])
        rows=[]
        for row in poly['rows']:
            coeff=[list(map(fq,p))for p in row['exact_YP_Bernstein']+row['exact_YK_Bernstein']]
            Y0,D0=values(row,0);Y1,D1=values(row,1);dd0=[];dd1=[]
            for i,p in enumerate(coeff):
                gate('exact_original_values_and_first_jets',p[0]==Y0[i] and p[5]==Y1[i] and 5*(p[1]-p[0])==D0[i] and 5*(p[5]-p[4])==D1[i])
                a0=20*(p[2]-2*p[1]+p[0]);a1=20*(p[3]-2*p[4]+p[5]);f0,f1=float(a0),float(a1)
                gate('actual_binary_second_jet_exact_recovery',F.from_float(f0)==a0 and F.from_float(f1)==a1)
                dd0.append(f0.hex());dd1.append(f1.hex())
            rows.append(dict(cell=row['cell'],segment=row['segment'],part=row['part'],stage_index=row['stage_index'],ddY0_binary64_hex=dd0,ddY1_binary64_hex=dd1,endpoint_definition_diagnostics=row['endpoint_definition_diagnostics']))
        compact=dict(schema='R178-exact-actual-binary-second-jet-reconstruction-v1',polynomial_schema=poly['schema'],
            definition_sha256=sha(a.definition),jets_sha256=sha(a.jets),original_polynomial_sha256=sha(a.polynomials),
            original_polynomial_uncompressed_sha256=hashlib.sha256(gzip.decompress(a.polynomials.read_bytes())).hexdigest(),rows=rows)
    else:
        gate('restore_arguments',a.restore_to is not None and a.polynomials is None and a.out_prefix is None)
        compact=load(a.compact)
    gate('frozen_definition_and_jets',compact['definition_sha256']==sha(a.definition) and compact['jets_sha256']==sha(a.jets))
    reconstructed=[]
    for row in compact['rows']:
        Y0,D0=values(row,0);Y1,D1=values(row,1);DD0=[F.from_float(float.fromhex(v))for v in row['ddY0_binary64_hex']];DD1=[F.from_float(float.fromhex(v))for v in row['ddY1_binary64_hex']]
        coeff=[hermite(*v)for v in zip(Y0,Y1,D0,D1,DD0,DD1)]
        reconstructed.append(dict(cell=row['cell'],segment=row['segment'],part=row['part'],stage_index=row['stage_index'],exact_YP_Bernstein=[[qr(v)for v in p]for p in coeff[:20]],exact_YK_Bernstein=[[qr(v)for v in p]for p in coeff[20:]],endpoint_definition_diagnostics=row['endpoint_definition_diagnostics']))
    gate('complete216_original_pieces',len(reconstructed)==216 and len(jp)==216)
    raw=encode(dict(schema=compact['polynomial_schema'],rows=reconstructed));compressed=gzip.compress(raw,mtime=0)
    gate('every_uncompressed_byte_reconstructed',hashlib.sha256(raw).hexdigest()==compact['original_polynomial_uncompressed_sha256'])
    gate('every_original_gzip_byte_reconstructed',hashlib.sha256(compressed).hexdigest()==compact['original_polynomial_sha256'])
    if a.compact is None:
        ref=save(Path(str(a.out_prefix)+'-compact.json.gz'),compact)
        result=dict(schema='R178-lossless-compact-candidate-storage-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
            definition=dict(path=str(a.definition),sha256=sha(a.definition)),jets=dict(path=str(a.jets),sha256=sha(a.jets)),
            original_polynomials=dict(path=str(a.polynomials),sha256=sha(a.polynomials),bytes=a.polynomials.stat().st_size),compact=ref,
            all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,no_numerical_jet_recomputation=True,
            restore_command=['python',str(Path(__file__).resolve()),'--definition',str(a.definition),'--jets',str(a.jets),'--compact',ref['path'],'--restore-to','FRESH_OUTPUT_PATH'],
            actual_source_polynomial_remains_available=True,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        report=save(Path(str(a.out_prefix)+'-certificate.json'),result);print(json.dumps(dict(compact=ref,report=report,gate_count=result['gate_count'],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
    else:
        if a.restore_to.exists():raise FileExistsError(a.restore_to)
        a.restore_to.write_bytes(compressed);print(json.dumps(dict(restored=str(a.restore_to),sha256=sha(a.restore_to),bytes=len(compressed))),flush=True)

if __name__=='__main__':main()
