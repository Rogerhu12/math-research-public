#!/usr/bin/env python3
"""All ordinary scalar primitives and the true CM elliptic primitive charts.

The actual R194 differential is used.  Removable zeroes are divided using a
unit linear system, and true CM4 logarithmic poles are kept explicitly.
"""
import argparse
import gzip
import hashlib
import inspect
import json
from pathlib import Path
import random
import sys
import time
from p41_elliptic_coarse_atlas47 import Series, ClassicalInvariants, setup


def scalar_gm(A0, B0, vary_A, order):
    from p41_supersingular_atlas47 import ca, cm, ck, ci, cn
    from p41_actual_differentials47 import Q
    N = order+2
    def mul(x, y):
        out = [(0,0)]*N
        for i in range(N):
            for j in range(N-i):
                out[i+j] = ca(out[i+j], cm(x[i], y[j]))
        return out
    def add(x, y): return [ca(a,b) for a,b in zip(x,y)]
    def scale(x, n): return [ck(a,n) for a in x]
    def deriv(x): return [ck(x[i],i) for i in range(1,N)]+[(0,0)]
    def inverse(x):
        out=[ci(x[0])]
        for n in range(1,N):
            c=(0,0)
            for k in range(1,n+1): c=ca(c,cm(x[k],out[n-k]))
            out.append(cn(cm(c,out[0])))
        return out
    A=[A0,(1,0) if vary_A else (0,0)]+[(0,0)]*(N-2)
    B=[B0,(0,0) if vary_A else (1,0)]+[(0,0)]*(N-2)
    D=add(scale(mul(mul(A,A),A),4),scale(mul(B,B),27))
    ID=inverse(D)
    aa=scale(mul(deriv(D),ID),-pow(12,-1,Q))
    bb=scale(mul(add(scale(mul(B,deriv(A)),9),scale(mul(A,deriv(B)),-6)),ID),pow(2,-1,Q))
    return aa[:order],bb[:order]


class ScalarPrimitiveAtlas:
    def __init__(self, at, coarse_path):
        self.at,self.a,self.r,self.np=at,at.a,at.r,at.np
        self.inv=ClassicalInvariants(at)
        self.eta=self.a.read('p41_eta_calibration47_complete.json.gz')
        from p41_actual_differentials47 import Q3
        self.sc=self.r.from_json(self.eta['numerator_coefficients'],Q3)
        self.qc=self.r.from_json(self.eta['denominator_coefficients'],Q3)
        raw=Path(coarse_path).read_bytes()
        self.coarse=json.loads(gzip.decompress(raw))
        self.coarse_sha=hashlib.sha256(raw).hexdigest()
        self.ordinary={}
        self.cm={}

    def ordinary_jets(self,j,order=5):
        at,a,r,np=self.at,self.a,self.r,self.np
        from p41_actual_differentials47 import Q,digest
        from p41_supersingular_atlas47 import ck
        ref=at.refs[j]
        raw0=ref['W']
        ordinary=np.flatnonzero(np.any(r.units(raw0),axis=1)).tolist()
        expected=800 if j==36 else 819 if j==0 else 820
        assert len(ordinary)==expected
        aa,bb=scalar_gm(ref['A'],ref['B'],j==0,order)
        assert (bb[0][0]**2+bb[0][1]**2)%47
        output=[raw0]+[r.zeros(820,73) for _ in range(order)]
        uncovered=set(ordinary);patches=[]
        rng=random.Random(2160041+j)
        for attempt in range(30):
            if attempt==0: v,G=at.v,at.G
            else:
                seed=r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(52)])
                vv=r.mm(at.K,seed)
                v=r.add(vv,r.mm(a.M['A1'],r.conjugate(vv)))
                values=r.mul(r.mm(a.M['W'],v),at.delta)
                G=r.rows(values,a.M['P3'])
                assert r.equal(r.mm(a.M['V3'],G),values)
            units=r.units(r.mm(raw0,v))[:,0]
            I=[i for i in sorted(uncovered) if units[i]]
            if not I:continue
            W=[r.rows(raw0,I)]
            for n in range(order):
                V3=self.inv.section_series(W)[1]
                vv=[r.mm(w,v) for w in W]
                iv=Series(a,n+1).inverse(vv)
                GG=[r.mm(v,G) for v in V3]
                rhs=r.zeros(len(I),73)
                for k in range(n+1):
                    for h in range(n-k+1):
                        rhs=r.add(rhs,at.matrix_scale(r.mul(GG[k],iv[h]),bb[n-k-h]))
                    rhs=r.sub(rhs,at.matrix_scale(W[n-k],ck(aa[k],2)))
                nxt=a.scale(rhs,pow(n+1,-1,Q))
                W.append(nxt)
                for k in range(2):output[n+1][k][I]=nxt[k]
            patches.append({'ordinary_points_1based':[i+1 for i in I],
                            'clearing_section_sha256':digest(r.to_json(v)),
                            'cleared_matrix_sha256':digest(r.to_json(G))})
            uncovered.difference_update(I)
            if not uncovered:break
        assert not uncovered
        return output,ordinary,patches,bb

    def ordinary_chart(self,j):
        at,a,r,np=self.at,self.a,self.r,self.np
        from p41_actual_differentials47 import Q,Q3,digest
        W,I,patches,beta=self.ordinary_jets(j,order=5)
        WI=[r.rows(w,I) for w in W]
        V2,V3=self.inv.section_series(WI)
        q=[r.mm(a.reduce(v,Q3),self.qc,Q3) for v in V2]
        s=[r.mm(a.reduce(v,Q3),self.sc,Q3) for v in V3]
        good=np.flatnonzero(r.units(q[0])[:,0]).tolist()
        bad=np.flatnonzero(~r.units(q[0])[:,0]).tolist()
        ratios=[r.zeros(len(I),1) for _ in range(3)]
        if good:
            qq=[r.rows(v,good) for v in q[:3]]
            ss=[r.rows(v,good) for v in s[:3]]
            v=Series(a,3).mul(ss,Series(a,3).inverse(qq))
            for n in range(3):
                for k in range(2):ratios[n][k][good]=v[n][k]%Q3
        removable=[]
        for row in bad:
            assert not r.units(s[0])[row,0], 'Denominator zero is not removable'
            assert r.units(q[1])[row,0], 'A higher-order Weierstrass chart is required'
            N=5
            mat=r.zeros(N,N)
            for i in range(N):
                for k in range(N):
                    d=i+1-k
                    if 0<=d<len(q):
                        for c in range(2):mat[c][i,k]=q[d][c][row,0]
            rhs=(np.stack([x[0][row] for x in s[1:N+1]]),
                 np.stack([x[1][row] for x in s[1:N+1]]))
            sol=r.mm(r.inverse_matrix(mat,Q3),rhs,Q3)
            assert r.equal(r.mm(mat,sol,Q3),rhs)
            assert r.equal(r.mul(r.rows(q[0],[row]),r.rows(sol,[0]),Q3),r.rows(s[0],[row]))
            for n in range(3):
                for c in range(2):ratios[n][c][row,0]=sol[c][n,0]
            removable.append({'necklace_index_1based':I[row]+1,
                              'q_mod47_zero':True,'s_mod47_zero':True,'q_prime_mod47_unit':True,
                              'division_matrix_size':5,'constant_equation_mod47_cubed':True,
                              'quotient_coefficients_mod47_cubed':r.to_json(sol)})
        eta=[]
        for n in range(3):
            val=r.zeros(len(I),1)
            for k in range(n+1):val=r.add(val,at.matrix_scale(ratios[k],beta[n-k]),Q3)
            eta.append(a.reduce(val,Q3))
        primitive=[a.scale(eta[n],pow(n+1,-1,Q3),Q3) for n in range(3)]
        record={'reference_j':j,'reference_label':at.refs[j]['label'],
                'A':at.refs[j]['A'],'B':at.refs[j]['B'],
                'parameter':'A-A_reference' if j==0 else 'B-B_reference',
                'ordinary_necklace_indices_1based':[i+1 for i in I],
                'excluded_elliptic_necklace_indices_1based':[i+1 for i in range(820) if i not in set(I)],
                'integrand_coefficients_mod47_cubed':[r.to_json(v) for v in eta],
                'primitive_coefficients_degrees1_to3_mod47_cubed':[r.to_json(v) for v in primitive],
                'unit_denominators':len(good),'removable_denominators':removable,
                'clearing_patches':patches,
                'all_generated_raw_jet_sha256':[digest(r.to_json(w)) for w in W],
                'precision_argument':'five unit equations imply c0,c1,c2 correct modulo47^3; integral primitive to47^4 on47R2'}
        self.ordinary[j]={'record':record,'position':{k:n for n,k in enumerate(I)},'primitive':primitive}
        print('ordinary',j,'points',len(I),'removable',len(bad),'patches',[len(x['ordinary_points_1based']) for x in patches],flush=True)
        return record

    def elliptic_charts(self):
        a,r,np=self.a,self.r,self.np
        from p41_actual_differentials47 import Q,Q3
        out=[]
        for record in self.coarse['elliptic_charts']:
            W=[r.from_json(v) for v in record['coarse_values']]
            V2,V3=self.inv.section_series(W)
            q=[r.mm(a.reduce(v,Q3),self.qc,Q3) for v in V2]
            s=[r.mm(a.reduce(v,Q3),self.sc,Q3) for v in V3]
            is_pole=record['kind']=='CM4'
            if is_pole:
                assert r.iszero(q[0]) and np.all(r.units(q[1]))
                den=q[1:4]
                beta0=-3*pow(8,-1,Q3)%Q3
                factor=-27*pow(4,-1,Q3)%Q3
            else:
                assert np.all(r.units(q[0]))
                den=q[:3]
                beta0=pow(18,-1,Q3)
                factor=-4*pow(27,-1,Q3)%Q3
            ratio=Series(a,3).mul(s[:3],Series(a,3).inverse(den))
            coeff=[]
            for n in range(3):
                val=r.zeros(W[0][0].shape[0],1)
                for k in range(n+1):val=r.add(val,a.scale(ratio[k],beta0*pow(factor,n-k,Q3),Q3),Q3)
                coeff.append(a.reduce(val,Q3))
            if is_pole:
                assert r.equal(coeff[0],r.column([[1,0]]*20,Q3))
                tau=[i-1 for i in a.cm4['elliptic_frobenius_permutation_1based']]
            else:tau=[0]
            for val in coeff:assert r.equal(r.conjugate(val,Q3),r.rows(val,tau))
            item={'kind':record['kind'],'A':record['curve_A'],'B':record['curve_B'],
                  'indices_1based':record['indices_1based'],'parameter':record['parameter'],
                  'true_logarithmic_pole':is_pole,'residue':1 if is_pole else 0,
                  'integrand_exponents':[-1,0,1] if is_pole else [0,1,2],
                  'integrand_coefficients_mod47_cubed':[r.to_json(v) for v in coeff],
                  'Frobenius':True,
                  'precision_boundary':'CM4 log(uY/uX) requires the actual unit part; no inversion of positive-valuation u at precision47^4'}
            out.append(item)
            self.cm[record['kind']]=item
            print('elliptic',record['kind'],'points',len(record['indices_1based']),'residue',item['residue'],flush=True)
        return out

    def evaluate_ordinary_difference(self,j,index,t0,t1):
        from p41_supersingular_atlas47 import ca,cs,cm
        from p41_actual_differentials47 import Q
        assert all(x%47==0 for x in t0+t1)
        obj=self.ordinary[j];row=obj['position'][index]
        p0,p1=(1,0),(1,0);out=(0,0)
        for coeff in obj['primitive']:
            p0=cm(p0,t0);p1=cm(p1,t1)
            c=tuple(int(v[row,0]) for v in coeff)
            out=ca(out,cm(c,cs(p1,p0)))
        return out

    def previous_three_tiny(self):
        """True degree2/3 torsion at endpoints, without target height inputs."""
        from p41_supersingular_atlas47 import ca,cs,cm,ck,ci,cp
        from p41_actual_differentials47 import Q
        a,r,at=self.a,self.r,self.at
        frame=a.read('p41_hecke3_formal_height47_compact.json.gz')
        fam=frame['families'][0]
        I=[x-1 for x in fam['points_1based']]
        pars=[tuple(x) for x in fam['actual_parameters'][0]]
        assert len(I)==len(pars)==54
        total={1:(0,0),2:(0,0),3:(0,0)}
        for idx,t in zip(I,pars):
            total[1]=ca(total[1],self.evaluate_ordinary_difference(9,idx,(0,0),t))
        details=[]
        for ell in (2,3):
            D=at.permute([[1,0],[0,ell]],I)
            for branch,target in enumerate(at.raw['operators'][str(ell)]['targets']):
                A0,B0=at.curve_coordinates(target)
                if len(target['kernel_x'])==2:
                    root=tuple(target['kernel_x'])
                else:
                    kc=a.field_coordinates([target['kernel_x']])
                    assert not a.np.any(kc[0][1:]) and not a.np.any(kc[1][1:])
                    root=tuple(int(v[0,0]) for v in kc)
                j,ref,c,t0=at.match(A0,B0)
                g=at.transport(ref,c,target['P'],target['Q'])
                indices=at.permute(g,D)
                subtotal=(0,0)
                for idx,ds in zip(indices,pars):
                    B=ca((32,0),ds);x=root
                    for _ in range(2):
                        if ell==2:
                            f=ca(ca(cp(x,3),x),B)
                            df=ca(ck(cp(x,2),3),(1,0))
                        else:
                            f=cs(ca(ca(ck(cp(x,4),3),ck(cp(x,2),6)),ck(cm(B,x),12)),(1,0))
                            df=ca(ca(ck(cp(x,3),12),ck(x,12)),ck(B,12))
                        x=cs(x,cm(f,ci(df)))
                    if ell==2:
                        assert ca(ca(cp(x,3),x),B)==(0,0)
                        AA=cs((-4%Q,0),ck(cp(x,2),15))
                        BB=cs(ck(x,-8),ck(cp(x,3),22))
                    else:
                        assert cs(ca(ca(ck(cp(x,4),3),ck(cp(x,2),6)),ck(cm(B,x),12)),(1,0))==(0,0)
                        AA=cs((-9%Q,0),ck(cp(x,2),30))
                        BB=cs(cs(ck(B,-27),ck(x,42)),ck(cp(x,3),70))
                    jj,rr,cc,t1=at.match(AA,BB)
                    assert jj==j and tuple(v%47 for v in c)==tuple(v%47 for v in cc)
                    value=self.evaluate_ordinary_difference(j,idx,t0,t1)
                    subtotal=ca(subtotal,value)
                total[ell]=ca(total[ell],subtotal)
                details.append({'ell':ell,'branch':branch,'reference_j':j,
                                'subtotal':subtotal,'actual_torsion_endpoint_equations':True})
        expected={1:(890368,0),2:(463561,0),3:(924161,0)}
        assert total==expected,(total,expected)
        print('independent tiny endpoint primitives',total,flush=True)
        return {'actual_tiny_integrals':{str(k):v for k,v in total.items()},
                'all_first_three_previous_values_match':True,'branches':details,
                'normalization':'Physical R145 source t; actual isogeny endpoints; true level transport; no extra1/ell after integration'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--coarse',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    at=setup(args.script_dir.resolve())
    obj=ScalarPrimitiveAtlas(at,args.coarse)
    from p41_actual_differentials47 import save,Q
    generation_sha=hashlib.sha256((inspect.getsource(scalar_gm)+
        inspect.getsource(ScalarPrimitiveAtlas.ordinary_jets)+
        inspect.getsource(ScalarPrimitiveAtlas.ordinary_chart)+
        inspect.getsource(ScalarPrimitiveAtlas.elliptic_charts)).encode()+
        Path(__file__).with_name('p41_elliptic_coarse_atlas47.py').read_bytes()).hexdigest()
    cache=args.output.with_name(args.output.name.replace('.json.gz','_partial.json.gz'))
    cached=None
    if cache.exists():
        cached=json.loads(gzip.decompress(cache.read_bytes()))
        assert cached['generation_sha256']==generation_sha
        assert cached['coarse_sha256']==obj.coarse_sha
        for name,wanted in cached['input_sha256'].items():
            at.a.read(name)
            assert at.a.inputs[name]==wanted
    records=[]
    for j in [9,10,44,0,36]:
        found=next((v for v in cached['ordinary_charts'] if v['reference_j']==j),None) if cached else None
        if found:
            obj.ordinary[j]={'record':found,
                'position':{k-1:n for n,k in enumerate(found['ordinary_necklace_indices_1based'])},
                'primitive':[obj.r.from_json(v) for v in found['primitive_coefficients_degrees1_to3_mod47_cubed']]}
            records.append(found)
            print('restored ordinary chart',j,flush=True)
        else:records.append(obj.ordinary_chart(j))
        save(cache,{'generation_sha256':generation_sha,'coarse_sha256':obj.coarse_sha,
                    'ordinary_charts':records,'input_sha256':at.a.inputs})
    cm=obj.elliptic_charts()
    save(cache,{'generation_sha256':generation_sha,'coarse_sha256':obj.coarse_sha,
                'ordinary_charts':records,'elliptic_charts':cm,'input_sha256':at.a.inputs})
    previous=obj.previous_three_tiny()
    out={'scope':'All4079 ordinary reference labels and21 true elliptic primitive charts; actual CM4 logs retained',
         'level':41,'auxiliary_prime':47,'modulus':Q,'coefficient_precision':3,
         'ordinary_charts':records,'elliptic_charts':cm,'independent_tiny_check':previous,
         'coarse_certificate_sha256':obj.coarse_sha,'derivative_certificate_sha256':at.derivative_sha,
         'input_sha256':at.a.inputs,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'coarse_source_sha256':hashlib.sha256(Path(__file__).with_name('p41_elliptic_coarse_atlas47.py').read_bytes()).hexdigest(),
         'remaining':'Full Hecke endpoints, static CM norms at sufficient precision, remaining51 global heights, all QC common roots'}
    h=save(args.output,out)
    print('COMPLETE',h,'seconds',round(time.monotonic()-start,3),flush=True)


if __name__=='__main__':
    main()
