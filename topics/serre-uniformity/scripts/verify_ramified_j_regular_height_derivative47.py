#!/usr/bin/env python3
"""Independent integer ODE and scalar-series audit for the R435 interface."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

Q = 47**4
Z, O = (0, 0), (1, 0)

def read(p):
    b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def add(x,y):return ((x[0]+y[0])%Q,(x[1]+y[1])%Q)
def neg(x):return (-x[0]%Q,-x[1]%Q)
def sub(x,y):return add(x,neg(y))
def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%Q,(x[0]*y[1]+x[1]*y[0])%Q)
def scale(x,n):return (x[0]*n%Q,x[1]*n%Q)
def unit(x):return bool(x[0]%47 or x[1]%47)
def inverse(x):
    assert unit(x);n=pow((x[0]*x[0]+x[1]*x[1])%Q,-1,Q);return (x[0]*n%Q,-x[1]*n%Q)
def dot(xs,ys):
    return (sum(x[0]*y[0]-x[1]*y[1] for x,y in zip(xs,ys))%Q,
            sum(x[0]*y[1]+x[1]*y[0] for x,y in zip(xs,ys))%Q)
def product(x,y,n):
    return [tuple(sum(mul(x[k],y[i-k])[j] for k in range(i+1) if k<len(x) and i-k<len(y))%Q for j in range(2)) for i in range(n)]
def invseries(x,n):
    out=[inverse(x[0])]
    for i in range(1,n):
        v=Z
        for k in range(1,min(i,len(x)-1)+1):v=add(v,mul(x[k],out[i-k]))
        out.append(neg(mul(out[0],v)))
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['script-dir','certificate','generator','derivative','output']:ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();S=args.script_dir.resolve();x=read(args.certificate);frame=read(args.derivative)
    assert x['result']==frame['result']=='R435' and x['source_sha256']==sha(args.generator)
    assert any(Path(k).name==args.derivative.name and h==sha(args.derivative) for k,h in x['input_sha256'].items())
    sys.path.insert(0,str(S))
    from p41_actual_differentials47 import ActualModel
    # This reconstruction uses its original bounded integer multiplication.
    a=ActualModel(S);H=a.r.to_json(a.H);Hcols=list(zip(*H));atlas=read(S/'data/p41_rational_SS_residue_atlas47_complete.json.gz')
    v=[z[0] for z in frame['chosen_clearing_section']]
    records=[];ode_entries=0
    for cert in x['charts']:
        ch=next(c for c in atlas['charts'] if c['reference_key']==cert['reference_key'])
        assert cert['disk_ids']==ch['disk_ids'] and cert['coordinate']==ch['coordinate'] and cert['frame']==ch['frame']
        assert cert['W_coefficients_0to4'][:4]==ch['W_coefficients_0to3']
        coordinate=[z[0] for z in ch['coordinate']]
        for i,disk in enumerate(ch['disk_ids']):
            W=[n[i] for n in cert['W_coefficients_0to4']]
            h=[[dot(ch['V3_coefficients_0to3'][n][i],col) for col in Hcols] for n in range(4)]
            hc=[dot(hn,coordinate) for hn in h]
            assert hc==[tuple(n[i][0]) for n in cert['Hc_coefficients_0to3']]
            assert unit(hc[0])
            for n in range(4):
                for col in range(73):
                    lhs=Z
                    for k in range(n+1):lhs=add(lhs,mul(hc[k],scale(W[n-k+1][col],n-k+1)))
                    assert lhs==h[n][col],(disk,n,col);ode_entries+=1
            vals=lambda k:[tuple(n[i][0]) for n in cert[k]]
            vv,aa,bb=[vals(k+'_coefficients_0to4') for k in ['v','Av','Bv3']]
            assert vv==[dot(wn,v) for wn in W] and unit(vv[0])
            vi=invseries(vv,5);A=product(aa,vi,5);B=product(bb,product(product(vi,vi,5),vi,5),5)
            assert A==vals('A_coefficients_0to4') and B==vals('B_coefficients_0to4')
            dlt=[add(scale(x,4),scale(y,27)) for x,y in zip(product(product(A,A,5),A,5),product(B,B,5))]
            Ap=[scale(A[n+1],n+1) for n in range(4)];Bp=[scale(B[n+1],n+1) for n in range(4)]
            K=[sub(scale(x,3),scale(y,2)) for x,y in zip(product(B,Ap,4),product(A,Bp,4))]
            assert dlt==vals('delta_coefficients_0to4') and K==vals('K_coefficients_0to3')
            assert unit(dlt[0]) and unit(K[0])
            dl=product([scale(dlt[n+1],n+1) for n in range(3)],invseries(dlt,3),3)
            kl=product([scale(K[n+1],n+1) for n in range(3)],invseries(K,3),3)
            C=[sub(scale(x,10*pow(3,-1,Q)),scale(y,4)) for x,y in zip(dl,kl)]
            assert C==vals('regular_combined_differential_coefficients_0to2')
            j=[scale(t,6912) for t in product(product(product(A,A,5),A,5),invseries(dlt,5),5)]
            assert j==vals('j_coefficients_0to4')
            e=cert['ramification_index'];ram=list(j)
            if e==2:ram[0]=sub(ram[0],(1728,0))
            assert all(t[0]%47==t[1]%47==0 for t in ram[:e]) and unit(ram[e])
            records.append({'disk_id':disk,'ramification_index':e,'v_delta_K_units':[vv[0],dlt[0],K[0]],'regular_coefficients':C})
    assert len(records)==41 and ode_entries==41*4*73
    out={'result':'R435','certificate_sha256':sha(args.certificate),'generator_sha256':sha(args.generator),
         'source_sha256':sha(__file__),'all11972_projective_ODE_entries_independently_replayed':True,
         'all41_v_delta_K_units_and_scalar_series_replayed':True,'all41_residual_j_ramification_orders_verified':True,
         'records':records,'scope':'Independent Python integer pair arithmetic replays the recorded projective ODE through degree4 and all scalar-series combinations; the published model reconstruction supplies H and the existing atlas supplies the first four V3 coefficients. No height or Norm is claimed.',
         'model_input_sha256':a.inputs,'actual_height_or_Norm_computed':False}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS R435 independent integer ODE and scalar series',sha(args.output),flush=True)

if __name__=='__main__':main()
