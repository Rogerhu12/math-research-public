#!/usr/bin/env python3
"""Independent actual Velu maps, Weil roots and all820 Hecke evaluations."""
import argparse
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import sys


def velu_identity(r,A,B,root,t,u,ell):
    def add(a,b):return [r.add(a[j] if j<len(a) else r.zero,b[j] if j<len(b) else r.zero) for j in range(max(len(a),len(b)))]
    def scale(a,c):return [r.mul(x,c) for x in a]
    def sub(a,b):return add(a,scale(b,r.element(-1)))
    def mul(a,b):
        c=[r.zero]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]=r.add(c[i+j],r.mul(x,y))
        return c
    def power(a,n):
        out=[r.one]
        for _ in range(n):out=mul(out,a)
        return out
    d=[r.scale(root,-1),r.one];x=[r.zero,r.one]
    X=add(add(mul(x,power(d,2)),scale(d,t)),[u])
    Y=sub(sub(power(d,3),scale(d,t)),[r.scale(u,2)])
    targetA=r.sub(A,r.scale(t,5));targetB=r.sub(B,r.scale(r.add(u,r.mul(root,t)),7))
    F=[B,A,r.zero,r.one]
    residual=sub(sub(sub(mul(F,power(Y,2)),power(X,3)),scale(mul(X,power(d,4)),targetA)),scale(power(d,6),targetB))
    assert all(c==r.zero for c in residual)
    derivative=[r.scale(X[j],j) for j in range(1,len(X))]
    assert all(c==r.zero for c in sub(sub(mul(derivative,d),scale(X,r.element(2))),Y))
    assert any(c%47 for c in (t if ell==2 else u))


def weight_one(r,C,P,Q,index):
    Ps,Qs=[P],[Q]
    for _ in range(39):Ps.append(C.add(Ps[-1],P));Qs.append(C.add(Qs[-1],Q))
    num,den=[],[]
    for base,multiples in ((P,Ps),(Q,Qs)):
        for k in range(39):
            if k==0:num.append(r.add(r.scale(r.mul(base[0],base[0]),3),C.A));den.append(r.scale(base[1],2))
            else:num.append(r.sub(multiples[k][1],base[1]));den.append(r.sub(multiples[k][0],base[0]))
    for x,y in Ps:
        for xx,yy in Qs:num.append(r.sub(yy,y));den.append(r.sub(xx,x))
    pref=[];prod=r.one
    for d in den:assert any(x%47 for x in d);pref.append(prod);prod=r.mul(prod,d)
    vi=r.inverse(prod);slopes=[None]*len(den)
    for k in range(len(den)-1,-1,-1):slopes[k]=r.mul(num[k],r.mul(vi,pref[k]));vi=r.mul(vi,den[k])
    assert vi==r.one
    def total(a):
        out=r.zero
        for x in a:out=r.add(out,x)
        return out
    ep=r.scale(total(slopes[:39]),pow(41,-1,r.q));eq=r.scale(total(slopes[39:78]),pow(41,-1,r.q))
    pe,qe=[ep],[eq]
    for k in range(39):pe.append(r.sub(r.add(pe[-1],ep),slopes[k]));qe.append(r.sub(r.add(qe[-1],eq),slopes[k+39]))
    out=[r.zero]*1681
    for a in range(1,41):out[index(a,0)]=pe[a-1];out[index(0,a)]=qe[a-1]
    for a in range(1,41):
        for b in range(1,41):out[index(a,b)]=r.sub(r.add(pe[a-1],qe[b-1]),slopes[78+40*(a-1)+b-1])
    for a in range(41):
        for b in range(41):assert out[index(-a,-b)]==r.scale(out[index(a,b)],-1)
    return out


def evaluations(values,r,ew,ii,model,index,mm2,power_traces,qmatmul):
    reps=[];signed=[0]*1681
    for k in range(1,1681):
        neg=index(-(k%41),-(k//41))
        if k<neg:reps.append(k);signed[k]=len(reps);signed[neg]=-len(reps)
    E=[values[k] for k in reps];tr=[x%r.q for x in power_traces(r.f,237)];ewi=r.mul(ew,ii);quarter=pow(4,-1,r.q)
    hs=[[sum(e[j]*tr[k+j] for j in range(80))*quarter%r.q for k in range(159)] for e in (ew,r.scale(ewi,-1))]
    transforms=[[[sum(e[k]*h[j+k] for k in range(80))%r.q for j in range(80)] for e in E] for h in hs]
    @lru_cache(maxsize=None)
    def pair(a,b):return tuple(sum(x*y for x,y in zip(T[a],E[b]))%r.q for T in transforms)
    raw=[]
    for n in range(820):
        gh=[mm2(model['sl2_representatives'][n],h) for h in model['sl2_normalizer_mod_signs']];row=[]
        for v,w in model['basis_pairs']:
            answer=[0,0]
            for g in gh:
                iv=signed[index(g[0][0]*v[0]+g[0][1]*v[1],g[1][0]*v[0]+g[1][1]*v[1])]
                iw=signed[index(g[0][0]*w[0]+g[0][1]*w[1],g[1][0]*w[0]+g[1][1]*w[1])]
                a,b=sorted((abs(iv)-1,abs(iw)-1));value=pair(a,b);sign=1 if iv*iw>0 else -1
                answer[0]+=sign*value[0];answer[1]+=sign*value[1]
            row.append([x%r.q for x in answer])
        raw.append(row)
    return qmatmul(raw,model['basis_inverse'],r.q)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--certificate',type=Path)
    parser.add_argument('--isogeny-only',action='store_true')
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from verify_p41_local47_torsion import Curve
    from verify_p41_cm3_makdisi47 import FastRing
    from verify_p41_makdisi47 import index,mm2,power_traces,qmatmul
    import p41_r2_matrix as mat
    from p41_cm4_divisor47 import kernel
    path=args.certificate or folder/'data'/'p41_hecke47_compact.json.gz';raw=path.read_bytes();data=json.loads(gzip.decompress(raw))
    sources={}
    for name,digest in data['source_sha256'].items():
        b=(folder/'data'/name).read_bytes();assert hashlib.sha256(b).hexdigest()==digest
        sources[name]=json.loads(gzip.decompress(b) if name.endswith('.gz') else b)
    torsion=sources['p41_local47_torsion_certificate.json'];model=sources['p41_makdisi47_certificate.json.gz'];divs=sources['p41_cusp_divisors47_certificate.json.gz']
    reference=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    r=FastRing(torsion['field_polynomial_ascending'],47**4);ii=r.element(model['sqrt_minus_one_lift']);ew=r.element(reference['weil_pairing'])
    P0,Q0=[tuple(r.element(x) for x in reference[k]) for k in ('P','Q')]
    class ActualCurve(Curve):
        def on_curve(self,P):
            if P is None:return True
            x,y=P
            return r.mul(y,y)==r.add(r.add(r.power(x,3),r.mul(self.A,x)),self.B)
    def velu(P,root,t,u):
        d=r.inverse(r.sub(P[0],root));d2=r.mul(d,d);d3=r.mul(d2,d)
        return r.add(r.add(P[0],r.mul(t,d)),r.mul(u,d2)),r.mul(P[1],r.sub(r.sub(r.one,r.mul(t,d2)),r.scale(r.mul(u,d3),2)))
    W=mat.from_json(model['evaluation_matrix']);A1=mat.from_json(model['frobenius_basis_matrix'])
    K=mat.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    free=[i-1 for i in divs['cusp_free_columns_1based']];piv=[i-1 for i in model['pivot_rows_1based']];lookup={tuple(x):i for i,x in enumerate(model['necklaces'])}
    operators=[]
    for ell in (2,3):
        record=data['operators'][str(ell)];targets=record['targets'];assert len(targets)==ell+1
        seen=set();values=mat.zeros(820,73);iv=pow(ell,-1,41)
        permutation=[lookup[a*iv%41,e*iv*iv%41] for a,e in model['necklaces']]
        assert [i+1 for i in permutation]==record['necklace_transport_1based']
        for n,entry in enumerate(targets):
            residue=tuple(x%47 for x in entry['kernel_x']);assert residue not in seen;seen.add(residue)
            root=r.add(r.element(entry['kernel_x'][0]),r.scale(ii,entry['kernel_x'][1]))
            root2=r.mul(root,root);root3=r.mul(root2,root)
            if ell==2:assert r.add(r.add(root3,root),r.element(32))==r.zero
            else:assert r.sub(r.add(r.add(r.scale(r.mul(root2,root2),3),r.scale(root2,6)),r.scale(root,384)),r.one)==r.zero
            t=r.add(r.scale(root2,3),r.one);u=r.zero
            if ell==3:t=r.scale(t,2);u=r.scale(r.add(r.add(root3,root),r.element(32)),4)
            velu_identity(r,r.one,r.element(32),root,t,u,ell)
            w=r.add(u,r.mul(root,t));A=r.sub(r.one,r.scale(t,5));B=r.sub(r.element(32),r.scale(w,7))
            assert A==r.element(entry['A']) and B==r.element(entry['B']);C=ActualCurve(r,A,B)
            P=velu(P0,root,t,u);Q=C.mul(velu(Q0,root,t,u),iv)
            assert P==tuple(r.element(x) for x in entry['P']) and Q==tuple(r.element(x) for x in entry['Q'])
            assert C.on_curve(P) and C.on_curve(Q) and C.mul(P,41) is None and C.mul(Q,41) is None
            direct=r.scale(r.mul(C.miller(P,Q,41),r.inverse(C.miller(Q,P,41))),-1)
            assert direct==ew
            print('Independent T',ell,'target',n+1,'actual isogeny/torsion/Weil root PASS.',flush=True)
            if args.isogeny_only:
                computed=entry.get('evaluation_matrix')
            else:
                computed=evaluations(weight_one(r,C,P,Q,index),r,ew,ii,model,index,mm2,power_traces,qmatmul)
                if 'evaluation_matrix' in entry:
                    assert computed==entry['evaluation_matrix']
                else:
                    encoded=json.dumps(computed,separators=(',',':')).encode()
                    assert hashlib.sha256(encoded).hexdigest()==entry['evaluation_matrix_sha256']
                print('Independent T',ell,'target',n+1,'all820x73 values PASS.',flush=True)
            if computed is not None:
                values=mat.add(values,mat.rows(mat.from_json(computed),permutation))
        if args.isogeny_only and 'evaluation_matrix' not in targets[0]:
            T=mat.from_json(record['weight2_operator'])
        else:
            values=tuple(x*pow(ell,-1,mat.Q)%mat.Q for x in values);T=mat.rows(values,piv)
            assert mat.to_json(T)==record['weight2_operator'] and mat.equal(mat.mm(W,T),values)
        assert mat.equal(mat.mm(A1,mat.conjugate(T)),mat.mm(T,A1))
        TK=mat.rows(mat.mm(T,K),free);assert mat.to_json(TK)==record['canonical_operator']
        assert mat.equal(mat.mm(K,TK),mat.mm(T,K));operators.append(TK)
    H=mat.add(operators[0],tuple(2*x%mat.Q for x in operators[1]));poly=[1]
    for f in sources['p41_jacobi_cm_certificate.json']['fields']:
        factor=f['factor_descending'];out=[0]*(len(poly)+len(factor)-1)
        for i,a in enumerate(poly):
            for j,b in enumerate(factor):out[i+j]+=a*b
        poly=out
    assert poly==data['primitive_polynomial_descending'];value=mat.zeros(54,54)
    for c in poly:value=mat.add(mat.mm(value,H),tuple((c%mat.Q)*x%mat.Q for x in mat.eye(54)))
    assert mat.iszero(value);cyclic=mat.from_json(data['canonical_cyclic_matrix'])
    assert mat.equal(mat.mm(H,mat.cols(cyclic,list(range(53)))),mat.cols(cyclic,list(range(1,54))))
    mat.inverse_matrix(cyclic)
    if args.isogeny_only:print('All seven whole-curve identities,normalized differentials,torsion and Weil roots PASS; evaluation recomputation skipped.',flush=True)
    else:print('All actual T2/T3 targets,820 rows,canonical actions and54-dimensional spectrum PASS.',flush=True)
    print('SHA256',hashlib.sha256(raw).hexdigest(),flush=True)


if __name__=='__main__':main()
