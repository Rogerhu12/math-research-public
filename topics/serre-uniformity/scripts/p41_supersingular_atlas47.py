#!/usr/bin/env python3
"""Actual residue-level transport and integral analytic atlas at good prime47.

This module uses the five R131 reference curves.  Implemented evaluation charts
are the non-elliptic references j=9,10,44; elliptic marked points are explicitly
excluded until their coarse-frame conversion is supplied.
"""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import random
import time
from p41_actual_differentials47 import ActualModel, P, Q, digest, report, save


def ca(x,y,q=Q):return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def cn(x,q=Q):return (-x[0]%q,-x[1]%q)
def cs(x,y,q=Q):return ca(x,cn(y,q),q)
def cm(x,y,q=Q):return ((x[0]*y[0]-x[1]*y[1])%q,(x[0]*y[1]+x[1]*y[0])%q)
def ck(x,k,q=Q):return (x[0]*k%q,x[1]*k%q)
def ci(x,q=Q):
    n=pow((x[0]*x[0]+x[1]*x[1])%q,-1,q)
    return (x[0]*n%q,-x[1]*n%q)
def cp(x,n,q=Q):
    out=(1,0)
    while n:
        if n&1:out=cm(out,x,q)
        x=cm(x,x,q);n//=2
    return out


class ResidueField:
    """Published F47^80 model; exact bounded NumPy integer convolution."""
    def __init__(self,poly,ii,np):
        self.np=np
        self.f=np.asarray(poly,dtype=np.int64)%P
        self.ii=np.asarray(ii,dtype=np.int64)%P
        self.zero=np.zeros(80,dtype=np.int64)
        self.one=self.zero.copy();self.one[0]=1
        assert len(self.f)==81 and self.f[-1]==1
        assert self.eq(self.mul(self.ii,self.ii),self.neg(self.one))
    def add(self,a,b):return (a+b)%P
    def sub(self,a,b):return (a-b)%P
    def neg(self,a):return -a%P
    def scale(self,a,n):return a*n%P
    def eq(self,a,b):return self.np.array_equal(a,b)
    def mul(self,a,b):
        v=self.np.convolve(a,b)%P
        for k in range(158,79,-1):
            c=int(v[k])
            if c:v[k-80:k]=(v[k-80:k]-c*self.f[:-1])%P
        return v[:80]
    def power(self,a,n):
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def inverse(self,a):
        assert self.np.any(a)
        out=self.power(a,P**80-2)
        assert self.eq(self.mul(a,out),self.one)
        return out
    def embed(self,c):return self.add(self.scale(self.one,c[0]),self.scale(self.ii,c[1]))
    def decode(self,a):return self.np.asarray(a,dtype=self.np.int64)%P
    def point(self,P0):return tuple(self.decode(z) for z in P0)
    def on_curve(self,T,A,B):
        return self.eq(self.mul(T[1],T[1]),self.add(self.add(self.mul(self.mul(T[0],T[0]),T[0]),self.mul(A,T[0])),B))
    def jac(self,T):return (T[0],T[1],self.one) if T is not None else (self.zero,self.one,self.zero)
    def jneg(self,T):return T[0],self.neg(T[1]),T[2]
    def double(self,T,A):
        X,Y,Z=T
        if not self.np.any(Z) or not self.np.any(Y):return self.jac(None)
        XX=self.mul(X,X);YY=self.mul(Y,Y);YYYY=self.mul(YY,YY);ZZ=self.mul(Z,Z)
        S=self.scale(self.mul(X,YY),4)
        M=self.add(self.scale(XX,3),self.mul(A,self.mul(ZZ,ZZ)))
        T3=self.sub(self.mul(M,M),self.scale(S,2))
        return T3,self.sub(self.mul(M,self.sub(S,T3)),self.scale(YYYY,8)),self.scale(self.mul(Y,Z),2)
    def jadd(self,T,U,A):
        X1,Y1,Z1=T;X2,Y2,Z2=U
        if not self.np.any(Z1):return U
        if not self.np.any(Z2):return T
        Z11=self.mul(Z1,Z1);Z22=self.mul(Z2,Z2)
        U1=self.mul(X1,Z22);U2=self.mul(X2,Z11)
        S1=self.mul(Y1,self.mul(Z2,Z22));S2=self.mul(Y2,self.mul(Z1,Z11))
        if self.eq(U1,U2):return self.double(T,A) if self.eq(S1,S2) else self.jac(None)
        H=self.sub(U2,U1);I=self.mul(self.scale(H,2),self.scale(H,2));J=self.mul(H,I)
        R=self.scale(self.sub(S2,S1),2);V=self.mul(U1,I)
        X3=self.sub(self.sub(self.mul(R,R),J),self.scale(V,2))
        Y3=self.sub(self.mul(R,self.sub(V,X3)),self.scale(self.mul(S1,J),2))
        Z3=self.mul(self.sub(self.sub(self.mul(self.add(Z1,Z2),self.add(Z1,Z2)),Z11),Z22),H)
        return X3,Y3,Z3
    def scalar(self,T,n,A):
        out=self.jac(None)
        while n:
            if n&1:out=self.jadd(out,T,A)
            T=self.double(T,A);n//=2
        return out
    def affine_batch(self,points):
        prefix=[];p=self.one
        for T in points:
            prefix.append(p)
            if self.np.any(T[2]):p=self.mul(p,T[2])
        inv=self.inverse(p);out=[None]*len(points)
        for k in range(len(points)-1,-1,-1):
            X,Y,Z=points[k]
            if not self.np.any(Z):continue
            iz=self.mul(inv,prefix[k]);inv=self.mul(inv,Z);iz2=self.mul(iz,iz)
            out[k]=self.mul(X,iz2),self.mul(Y,self.mul(iz,iz2))
        assert self.eq(inv,self.one)
        return out
    def key(self,T):
        if T is None:return b''
        return T[0].astype(self.np.uint8).tobytes()+T[1].astype(self.np.uint8).tobytes()


class Atlas:
    def __init__(self,script_dir,derivative):
        self.a=ActualModel(script_dir)
        self.r,self.np,self.M=self.a.r,self.a.np,self.a.M
        self.a.field_setup()
        self.F=ResidueField(self.a.field_polynomial,self.a.ii,self.np)
        b=Path(derivative).read_bytes();self.derivative_sha=hashlib.sha256(b).hexdigest()
        d=json.loads(gzip.decompress(b))
        self.K=self.r.from_json(d['elliptic_kernel_coefficients'])
        self.v=self.r.from_json(d['chosen_clearing_section'])
        self.G=self.r.from_json(d['cleared_derivative_coefficients'])
        jets=self.a.read('p41_evaluation_jets47_checkpoint.json.gz')
        self.delta=self.r.add(self.a.scale(self.r.from_json(jets['evaluation_derivatives']),-27652*pow(3,-1,Q)),self.a.scale(self.M['W'],96))
        self.raw=self.a.read('p41_hecke47_full_saved.json.gz')
        compact=self.a.read('p41_hecke47_compact.json.gz')
        assert self.a.inputs['p41_hecke47_full_saved.json.gz']==compact['full_raw_sha256']
        torsion=self.a.read('p41_local47_torsion_certificate.json')
        source=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
        self.refs={9:{'label':'source','A':(1,0),'B':(32,0),'P':source['P'],'Q':source['Q'],'W':self.M['W']}}
        for j,ell,n in [(10,2,2),(44,3,0),(0,3,2),(36,3,3)]:
            t=self.raw['operators'][str(ell)]['targets'][n]
            AB=self.a.field_coordinates([t['A'],t['B']])
            assert not self.np.any(AB[0][1:]) and not self.np.any(AB[1][1:])
            A=tuple(int(x[0,0]) for x in AB);B=tuple(int(x[0,1]) for x in AB)
            assert self.j(A,B)==(j,0)
            self.refs[j]={'label':'T'+str(ell)+'_branch'+str(n),'A':A,'B':B,'P':t['P'],'Q':t['Q'],'W':self.r.from_json(t['evaluation_matrix'])}
        self.source=[self.a.model,self.a.cusp,self.a.cm4,self.a.group]
        self.lookup={tuple(pair):k for k,pair in enumerate(self.a.model['necklaces'])}
        self.rng=random.Random(205206)

    @staticmethod
    def j(A,B):
        n=ck(cp(A,3,P),4,P);d=ca(n,ck(cp(B,2,P),27,P),P)
        return ck(cm(n,ci(d,P),P),1728,P)

    def curve_coordinates(self,target):
        AB=self.a.field_coordinates([target['A'],target['B']])
        assert not self.np.any(AB[0][1:]) and not self.np.any(AB[1][1:])
        return tuple(int(x[0,0]) for x in AB),tuple(int(x[0,1]) for x in AB)

    def match(self,A,B):
        j=self.j(A,B)
        assert j[1]==0 and j[0] in self.refs
        ref=self.refs[j[0]]
        exponent=6 if j[0]==0 else 4
        ratio=cm(B,ci(ref['B'])) if exponent==6 else cm(A,ci(ref['A']))
        choices=[(x,y) for x in range(P) for y in range(P) if cp((x,y),exponent,P)==tuple(v%P for v in ratio)]
        assert len(choices)==exponent
        for c in choices:
            for _ in range(2):
                c=cs(c,cm(cs(cp(c,exponent),ratio),ci(ck(cp(c,exponent-1),exponent))))
            assert cp(c,exponent)==ratio
            An=cm(A,ci(cp(c,4)));Bn=cm(B,ci(cp(c,6)))
            if tuple(x%P for x in An)!=tuple(x%P for x in ref['A']) or tuple(x%P for x in Bn)!=tuple(x%P for x in ref['B']):continue
            t=cs(An,ref['A']) if exponent==6 else cs(Bn,ref['B'])
            assert all(x%P==0 for x in t)
            return j[0],ref,c,t
        raise AssertionError('No actual isomorphism of residue curves')

    def prepare_basis(self,ref):
        if 'Ptable' in ref:return
        F=self.F;A=F.embed(ref['A']);B=F.embed(ref['B'])
        PP,QQ=F.point(ref['P']),F.point(ref['Q'])
        assert F.on_curve(PP,A,B) and F.on_curve(QQ,A,B)
        Pj,Qj=F.jac(PP),F.jac(QQ)
        assert not self.np.any(F.scalar(Pj,41,A)[2]) and not self.np.any(F.scalar(Qj,41,A)[2])
        Ptable=[F.jac(None)];Qtable=[F.jac(None)]
        for k in range(1,41):
            Ptable.append(F.jadd(Ptable[-1],Pj,A));Qtable.append(F.jadd(Qtable[-1],Qj,A))
        points=F.affine_batch(Ptable)
        lookup={F.key(T):k for k,T in enumerate(points)}
        assert len(lookup)==41
        ref.update(Ptable=Ptable,Qtable=Qtable,Plookup=lookup,residueA=A)

    def transport(self,ref,c,P0,Q0):
        self.prepare_basis(ref)
        F=self.F;A=ref['residueA'];ic=ci(c,P);ic2=F.embed(cp(ic,2,P));ic3=F.embed(cp(ic,3,P))
        normalized=[]
        for T in (P0,Q0):
            T=F.point(T);T=F.mul(T[0],ic2),F.mul(T[1],ic3)
            assert F.on_curve(T,A,F.embed(ref['B']))
            normalized.append(T)
        differences=[]
        for T in normalized:
            T=F.jac(T)
            differences.extend(F.jadd(T,F.jneg(U),A) for U in ref['Qtable'])
        aff=F.affine_batch(differences)
        columns=[]
        for k,T in enumerate(normalized):
            found=[]
            for b in range(41):
                key=F.key(aff[41*k+b])
                if key in ref['Plookup']:found.append((ref['Plookup'][key],b))
            assert len(found)==1
            aa,bb=found[0]
            test=F.affine_batch([F.jadd(ref['Ptable'][aa],ref['Qtable'][bb],A)])[0]
            assert F.key(test)==F.key(T)
            columns.append((aa,bb))
        g=[[columns[0][0],columns[1][0]],[columns[0][1],columns[1][1]]]
        assert (g[0][0]*g[1][1]-g[0][1]*g[1][0])%41==1
        return g

    def permute(self,g,indices):
        def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2))%41 for j in range(2)] for i in range(2)]
        det=(g[0][0]*g[1][1]-g[0][1]*g[1][0])%41;iv=pow(det,-1,41)
        gi=[[g[1][1]*iv%41,-g[0][1]*iv%41],[-g[1][0]*iv%41,g[0][0]*iv%41]]
        out=[]
        for idx in indices:
            x,e=self.a.model['necklaces'][idx]
            R=[[x,(e-x*x)%41],[1,-x%41]]
            T=mm(mm(g,R),gi);t=pow(T[1][0],-1,41)
            x=T[0][0]*t%41;e=(x*x+T[0][1]*t)%41
            out.append(self.lookup[(x,e)])
        assert len(set(out))==len(indices)
        return out

    @staticmethod
    def pmul(A,B):
        out=[(0,0)]*4
        for i,x in enumerate(A):
            for j,y in enumerate(B):
                if i+j<4:out[i+j]=ca(out[i+j],cm(x,y))
        return out
    @staticmethod
    def padd(A,B):return [ca(x,y) for x,y in zip(A,B)]
    @staticmethod
    def pscale(A,n):return [ck(x,n) for x in A]
    @staticmethod
    def pderiv(A):return [ck(A[i],i) for i in range(1,4)]+[(0,0)]
    def pinv(self,A):
        out=[ci(A[0])]
        for n in range(1,4):
            t=(0,0)
            for k in range(1,n+1):t=ca(t,cm(A[k],out[n-k]))
            out.append(cn(cm(t,out[0])))
        return out
    def gm(self,A,B):
        D=self.padd(self.pscale(self.pmul(self.pmul(A,A),A),4),self.pscale(self.pmul(B,B),27))
        ID=self.pinv(D)
        aa=self.pscale(self.pmul(self.pderiv(D),ID),-pow(12,-1,Q))[:3]
        bb=self.pscale(self.pmul(self.padd(self.pscale(self.pmul(B,self.pderiv(A)),9),self.pscale(self.pmul(A,self.pderiv(B)),-6)),ID),pow(2,-1,Q))[:3]
        return aa,bb
    def matrix_scale(self,M,c):
        return ((M[0]*c[0]-M[1]*c[1])%Q,(M[0]*c[1]+M[1]*c[0])%Q)

    def prepare_jets(self,j,ref):
        if 'jets' in ref:return
        assert j not in (0,36),'elliptic marked coarse charts must be supplied explicitly'
        from p41_hecke3_hessian47 import section_jets
        a,r,np=self.a,self.r,self.np
        A=[ref['A'],(0,0),(0,0),(0,0)];B=[ref['B'],(1,0),(0,0),(0,0)]
        aa,bb=self.gm(A,B)
        assert (bb[0][0]**2+bb[0][1]**2)%P
        output=[ref['W']]+[r.zeros(820,73) for _ in range(3)]
        uncovered=set(range(820));patches=[]
        for attempt in range(30):
            if attempt==0:v,G=self.v,self.G
            else:
                seed=r.column([[self.rng.randrange(P),self.rng.randrange(P)] for _ in range(52)])
                vv=r.mm(self.K,seed);v=r.add(vv,r.mm(self.M['A1'],r.conjugate(vv)))
                val=r.mul(r.mm(self.M['W'],v),self.delta);G=r.rows(val,self.M['P3'])
                assert r.equal(r.mm(self.M['V3'],G),val)
            unit=r.units(r.mm(ref['W'],v))[:,0]
            I=[i for i in sorted(uncovered) if unit[i]]
            if not I:continue
            W=[r.rows(ref['W'],I)]
            for n in range(3):
                V3=section_jets(W,self.source,self.M,r)[1]
                vv=[r.mm(w,v) for w in W];iv=[r.inverse_values(vv[0])]
                for k in range(1,n+1):
                    t=r.zeros(len(I),1)
                    for u in range(1,k+1):t=r.add(t,r.mul(vv[u],iv[k-u]))
                    iv.append(r.neg(r.mul(t,iv[0])))
                GG=[r.mm(w,G) for w in V3];rhs=r.zeros(len(I),73)
                for u in range(n+1):
                    for vj in range(n-u+1):rhs=r.add(rhs,self.matrix_scale(r.mul(GG[u],iv[vj]),bb[n-u-vj]))
                    rhs=r.sub(rhs,self.matrix_scale(W[n-u],ck(aa[u],2)))
                nxt=a.scale(rhs,pow(n+1,-1,Q));W.append(nxt)
                for k in range(2):output[n+1][k][I]=nxt[k]
            patches.append({'points':len(I),'section_sha256':digest(r.to_json(v))})
            uncovered.difference_update(I)
            if not uncovered:break
        assert not uncovered
        ref['jets']=output;ref['patches']=patches
        report('Atlas reference j='+str(j)+' actual cubic jets ready')

    def evaluate(self,A,B,P0,Q0,indices):
        j,ref,c,t=self.match(A,B)
        self.prepare_jets(j,ref)
        g=self.transport(ref,c,P0,Q0)
        permutation=self.permute(g,indices)
        answer=self.r.zeros(len(indices),73);power=(1,0)
        for W in ref['jets']:
            answer=self.r.add(answer,self.matrix_scale(self.r.rows(W,permutation),power));power=cm(power,t)
        assert power==(0,0)
        answer=self.matrix_scale(answer,cp(c,2))
        return answer,{'reference_j':j,'reference_label':ref['label'],'homothety':c,'parameter':t,
                       'level_basis_matrix_mod41':g,'reference_necklace_indices_1based':[i+1 for i in permutation],
                       'output_sha256':digest(self.r.to_json(answer))}


def verify_hasse():
    def mul(A,B):
        C=[0]*(len(A)+len(B)-1)
        for i,a in enumerate(A):
            for j,b in enumerate(B):C[i+j]=(C[i+j]+a*b)%P
        return C
    def monic(A):return [a*pow(A[-1],-1,P)%P for a in A]
    q=[1,-1%P,1]
    F=mul(q,mul([1,1],mul([-2%P,1],[-pow(2,-1,P)%P,1])))
    for j in (9,10,44):
        C=[256*x%P for x in mul(mul(q,q),q)]
        for k,v in enumerate([0,0,1,-2,1]):C[k]=(C[k]-j*v)%P
        F=mul(F,monic(C))
    H=[math.comb(23,k)**2%P for k in range(24)]
    assert F==H
    return {'Hasse_polynomial_ascending':H,'supersingular_j':[0,9,10,36,44],'exact_degree23_factor_identity':True}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--derivative',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    atlas=Atlas(args.script_dir,args.derivative);r=atlas.r
    checks=[]
    for ell,branch in [(2,0),(2,1),(3,1)]:
        target=atlas.raw['operators'][str(ell)]['targets'][branch]
        A,B=atlas.curve_coordinates(target)
        W,rec=atlas.evaluate(A,B,target['P'],target['Q'],list(range(820)))
        assert r.equal(W,r.from_json(target['evaluation_matrix']))
        rec.update(label='R131_T'+str(ell)+'_branch'+str(branch),points=820,all_actual_values_match=True)
        checks.append(rec);report(rec['label']+' all820x73 values matched through residue transport')
    cm16=atlas.a.read('p41_cm16_hecke47_verified.json.gz')
    cm36=atlas.a.read('p41_cm36_hecke47_raw.json.gz')
    for label,record in [('CM16',cm16)]+[('CM36_'+str(k+1),v) for k,v in enumerate(cm36['records'])]:
        A=(record['curve_A']%Q,0);B=(record['curve_B']%Q,0)
        I=[i-1 for i in record['target_necklace_indices_1based']]
        W,rec=atlas.evaluate(A,B,record['P_plus'],record['Q_plus'],I)
        assert r.equal(W,r.from_json(record['weight2_values']))
        rec.update(label=label,points=20,all_actual_values_match=True)
        checks.append(rec);report(label+' all20x73 values matched through residue transport')
    out={'status':'actual nonelliptic supersingular atlas transport verified against six independent evaluations',
         'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'hasse':verify_hasse(),'checks':checks,
         'references':{str(j):{'label':v['label'],'A':v['A'],'B':v['B'],'patches':v.get('patches'),
                                'jet_sha256':[digest(r.to_json(w)) for w in v.get('jets',[])]} for j,v in atlas.refs.items()},
         'input_sha256':atlas.a.inputs,'derivative_certificate_sha256':atlas.derivative_sha,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'engine_sha256':hashlib.sha256(Path(__file__).with_name('p41_actual_differentials47.py').read_bytes()).hexdigest(),
         'scope':'j9/10/44 unit charts; all 60 CM16/36 and three full820 target fibres; elliptic marked j0/1728 charts not yet evaluated'}
    h=save(args.output,out);report('Actual atlas checks complete; seconds='+str(round(time.monotonic()-started,3)))
    print(str(args.output)+' SHA256 '+h,flush=True)


if __name__=='__main__':main()
