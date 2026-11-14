#!/usr/bin/env python3
"""Non-input cubic-jet verification of R205 at the source and a true 2-isogeny.

The published target cubic jets are used only after the ODE reconstruction.
All 820 rows are reconstructed through integral unit charts; no GP is run.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import time
from p41_actual_differentials47 import ActualModel, P, Q, digest, report, save


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--derivative',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    started=time.monotonic()
    raw=args.derivative.read_bytes()
    cert=json.loads(gzip.decompress(raw))
    a=ActualModel(args.script_dir)
    r,np,M=a.r,a.np,a.M
    from p41_hecke3_hessian47 import section_jets
    sources=[a.model,a.cusp,a.cm4,a.group]
    chosen=r.from_json(cert['chosen_clearing_section'])
    chosenG=r.from_json(cert['cleared_derivative_coefficients'])
    K=r.from_json(cert['elliptic_kernel_coefficients'])
    jets=a.read('p41_evaluation_jets47_checkpoint.json.gz')
    delta=r.add(a.scale(r.from_json(jets['evaluation_derivatives']),-27652*pow(3,-1,Q)),a.scale(M['W'],96))
    def padd(a,b):return [(x+y)%Q for x,y in zip(a,b)]
    def scale(a,c):return [x*c%Q for x in a]
    def pmul(a,b):
        out=[0]*4
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if i+j<4:out[i+j]=(out[i+j]+x*y)%Q
        return out
    def deriv(a):return [i*a[i]%Q for i in range(1,4)]+[0]
    def pinv(a):
        assert a[0]%P
        out=[pow(a[0],-1,Q)]
        for n in range(1,4):out.append(-sum(a[k]*out[n-k] for k in range(1,n+1))*out[0]%Q)
        return out
    def gm(A,B):
        D=padd(scale(pmul(pmul(A,A),A),4),scale(pmul(B,B),27))
        iD=pinv(D)
        aa=scale(pmul(deriv(D),iD),-pow(12,-1,Q))[:3]
        bb=scale(pmul(padd(scale(pmul(B,deriv(A)),9),scale(pmul(A,deriv(B)),-6)),iD),pow(2,-1,Q))[:3]
        return aa,bb
    def reconstruct(W0,A,B):
        aa,bb=gm(A,B)
        assert bb[0]%P
        output=[W0]+[r.zeros(820,73) for _ in range(3)]
        uncovered=set(range(820));patches=[]
        rng=random.Random(205194)
        for patch in range(20):
            if patch==0:v,G=chosen,chosenG
            else:
                seed=r.column([[rng.randrange(P),rng.randrange(P)] for _ in range(K[0].shape[1])])
                vv=r.mm(K,seed);v=r.add(vv,r.mm(M['A1'],r.conjugate(vv)))
                val=r.mul(r.mm(M['W'],v),delta)
                G=r.rows(val,M['P3'])
                assert r.equal(r.mm(M['V3'],G),val)
            basev=r.mm(W0,v)
            I=[j for j in sorted(uncovered) if r.units(basev)[j,0]]
            if not I:continue
            Ws=[r.rows(W0,I)]
            for n in range(3):
                V3=section_jets(Ws,sources,M,r)[1]
                vv=[r.mm(w,v) for w in Ws]
                iv=[r.inverse_values(vv[0])]
                for k in range(1,n+1):
                    t=r.zeros(len(I),1)
                    for j in range(1,k+1):t=r.add(t,r.mul(vv[j],iv[k-j]))
                    iv.append(r.neg(r.mul(t,iv[0])))
                GG=[r.mm(w,G) for w in V3]
                rhs=r.zeros(len(I),73)
                for i in range(n+1):
                    for j in range(n-i+1):
                        rhs=r.add(rhs,a.scale(r.mul(GG[i],iv[j]),bb[n-i-j]))
                    rhs=r.sub(rhs,a.scale(Ws[n-i],2*aa[i]))
                nextW=a.scale(rhs,pow(n+1,-1,Q))
                Ws.append(nextW)
                for component in range(2):output[n+1][component][I]=nextW[component]
            patches.append({'points_1based':[j+1 for j in I],'clearing_section':r.to_json(v),'cleared_matrix_sha256':digest(r.to_json(G))})
            uncovered.difference_update(I)
            if not uncovered:break
        assert not uncovered
        return output,{'A_coefficients':A,'B_coefficients':B,'Gauss_Manin_a':aa,'Kodaira_Spencer_b':bb,'patches':patches}
    # Source cubic coefficients are not fed to reconstruct except the constant.
    source=a.read('p41_source_cubic47_full_saved.json.gz')
    assert a.inputs['p41_source_cubic47_full_saved.json.gz']=='2eda1b699c8e556ab4d161868cb7152106520dd30a84008b2972e21e9a9312f4'
    expected=[r.from_json(c) for c in source['evaluation_coefficients']]
    del source
    assert r.equal(expected[0],M['W'])
    predicted,source_record=reconstruct(M['W'],[1,0,0,0],[32,1,0,0])
    for x,y in zip(predicted,expected):assert r.equal(x,y)
    source_record['all_820_by73_by4_entries_match']=True
    source_record['coefficient_sha256']=[digest(r.to_json(w)) for w in predicted]
    del predicted,expected
    report('Source cubic ODE reconstruction matches every published coefficient')
    target=a.read('p41_hecke2_target2_cubic47_saved.json.gz')
    assert a.inputs['p41_hecke2_target2_cubic47_saved.json.gz']=='8e622cd069ba399fa6239eaf879177bb7266403df4dc09a256b608eabdbfa225'
    assert target['target_index_0based']==2
    target=target['target']
    for z in target['kernel_jets']:assert len(z)==80 and all(v==0 for v in z[1:])
    kernel=[z[0] for z in target['kernel_jets']]
    sourceA,sourceB=[1,0,0,0],[32,1,0,0]
    assert padd(padd(pmul(pmul(kernel,kernel),kernel),kernel),sourceB)==[0,0,0,0]
    A=padd(scale(sourceA,-4),scale(pmul(kernel,kernel),-15))
    B=padd(scale(pmul(sourceA,kernel),-8),scale(pmul(pmul(kernel,kernel),kernel),-22))
    expected=[r.from_json(c) for c in target['evaluation_coefficients']]
    del target
    predicted,target_record=reconstruct(expected[0],A,B)
    for x,y in zip(predicted,expected):assert r.equal(x,y)
    assert target_record['Kodaira_Spencer_b']==scale(source_record['Kodaira_Spencer_b'],pow(2,-1,Q))
    target_record['kernel_x_coefficients']=kernel
    target_record['all_820_by73_by4_entries_match']=True
    target_record['coefficient_sha256']=[digest(r.to_json(w)) for w in predicted]
    out={'status':'source and genuine degree2 target cubic jets completely reconstructed without input higher jets',
         'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'source':source_record,'degree2_target':target_record,
         'entries_checked_in_each_family':4*820*73,'true_target_KS_ratio':'1/2',
         'derivative_certificate_sha256':hashlib.sha256(raw).hexdigest(),'input_sha256':a.inputs,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'engine_sha256':hashlib.sha256(Path(__file__).with_name('p41_actual_differentials47.py').read_bytes()).hexdigest(),
         'scope':'unit-chart ODE verified at all820 source and all820 target points; elliptic stack parameter conversion remains explicit'}
    h=save(args.output,out)
    report('True target cubic ODE reconstruction passed; seconds='+str(round(time.monotonic()-started,3)))
    print(str(args.output)+' SHA256 '+h,flush=True)


if __name__=='__main__':main()
