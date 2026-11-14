#!/usr/bin/env python3
"""Evaluate descended kernel polynomials on the actual level-41 residue basis.

The prime-to-47 torsion itself may require degree82, but its kernel polynomial
lies in R2 and is evaluated directly in the published F47^80 level model.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time
from p41_supersingular_atlas47 import Atlas, Q, cp, cm, ck
from p41_actual_differentials47 import digest, save


class KernelBridge:
    def __init__(self, atlas):
        self.atlas=atlas
        self.F=atlas.F

    def source_basis(self, name):
        F,a=self.F,self.atlas.a
        if name=='source_j9':
            ref=self.atlas.refs[9]
            P0,Q0=F.point(ref['P']),F.point(ref['Q'])
            A,B=(1,0),(32,0)
            c=(1,0)
        elif name=='CM4':
            data=a.read('p41_cm4_divisor47_certificate.json')
            assert data['curve_A']==1 and data['curve_B']==0
            P0=F.point([v[0] for v in data['P_jets']])
            Q0=F.point([v[0] for v in data['Q_jets']])
            root=7
            for _ in range(2):root=(root-(root*root-2)*pow(2*root,-1,Q))%Q
            assert root*root%Q==2
            c=ck((1,1),pow(root,-1,Q))
            assert cp(c,4)==(Q-1,0)
            c2,c3=F.embed(cp(c,2)),F.embed(cp(c,3))
            P0=F.mul(P0[0],c2),F.mul(P0[1],c3)
            Q0=F.mul(Q0[0],c2),F.mul(Q0[1],c3)
            A,B=(Q-1,0),(0,0)
        else:raise ValueError(name)
        Af,Bf=F.embed(A),F.embed(B)
        assert F.on_curve(P0,Af,Bf) and F.on_curve(Q0,Af,Bf)
        for T in [P0,Q0]:assert not F.np.any(F.scalar(F.jac(T),41,Af)[2])
        return A,B,P0,Q0,c

    def polynomial_derivatives(self, coefficients, x):
        F=self.F
        # Divided derivatives: the four entries are h^(j)/j! at x.
        out=[F.zero.copy() for _ in range(4)]
        for coefficient in reversed(coefficients):
            for j in range(3,0,-1):out[j]=F.add(F.mul(x,out[j]),out[j-1])
            out[0]=F.add(F.mul(x,out[0]),F.embed(coefficient))
        return out

    def velu_pair(self, ell, kernel, A, B, P0, Q0):
        F=self.F
        h=[tuple(x) for x in kernel['kernel_polynomial_ascending']]
        assert len(h)==(ell+1)//2 and h[-1]==(1,0)
        s1=F.neg(F.embed(h[-2]));Af,Bf=F.embed(A),F.embed(B)
        values=[self.polynomial_derivatives(h,T[0]) for T in [P0,Q0]]
        product=F.mul(values[0][0],values[1][0]);inverse=F.inverse(product)
        inverses=[F.mul(inverse,values[1][0]),F.mul(inverse,values[0][0])]
        images=[]
        At,Bt=tuple(kernel['velu_A']),tuple(kernel['velu_B'])
        Atf,Btf=F.embed(At),F.embed(Bt)
        for T,V,iv in zip([P0,Q0],values,inverses):
            assert F.eq(F.mul(V[0],iv),F.one)
            S1=F.mul(V[1],iv)
            H2=F.mul(V[2],iv)
            S2=F.sub(F.mul(S1,S1),F.scale(H2,2))
            S3=F.add(F.sub(F.mul(F.mul(S1,S1),S1),F.scale(F.mul(S1,H2),3)),F.scale(F.mul(V[3],iv),3))
            x,y=T;x2=F.mul(x,x)
            f=F.add(F.add(F.mul(x2,x),F.mul(Af,x)),Bf)
            fp=F.add(F.scale(x2,3),Af)
            xx=F.add(F.sub(F.sub(F.scale(x,ell),F.scale(s1,2)),F.scale(F.mul(fp,S1),2)),F.scale(F.mul(f,S2),4))
            derivative=F.sub(F.add(F.sub(F.scale(F.one,ell),F.scale(F.mul(x,S1),12)),F.scale(F.mul(fp,S2),6)),F.scale(F.mul(f,S3),8))
            yy=F.mul(y,derivative)
            U=xx,yy
            assert F.on_curve(U,Atf,Btf)
            assert not F.np.any(F.scalar(F.jac(U),41,Atf)[2])
            images.append(U)
        Pplus=images[0]
        Qplus=F.affine_batch([F.scalar(F.jac(images[1]),pow(ell,-1,41),Atf)])[0]
        return Pplus,Qplus,images

    def target(self, curve, ell, kernel, indices):
        A,B,P0,Q0,c=self.source_basis(curve)
        PP,QQ,raw=self.velu_pair(ell,kernel,A,B,P0,Q0)
        target_indices=self.atlas.permute([[1,0],[0,ell%41]],indices)
        return PP,QQ,target_indices,{'source_curve':curve,'source_homothety':c,
             'kernel_line':kernel['line'],'ell':ell,'target_necklace_indices_1based':[i+1 for i in target_indices]}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    atlas=Atlas(args.script_dir,args.script_dir/'data/p41_cleared_serre_derivative47_complete.json.gz')
    bridge=KernelBridge(atlas);F=atlas.F;r=atlas.r
    path=args.script_dir/'data/p41_prime3_source_j9_kernels47.json.gz'
    data=json.loads(gzip.decompress(path.read_bytes()))
    A,B,P0,Q0,c=bridge.source_basis('source_j9')
    checks=[]
    for kernel in data['kernels']:
        At,Bt=tuple(kernel['velu_A']),tuple(kernel['velu_B'])
        matches=[]
        for b,t in enumerate(atlas.raw['operators']['3']['targets']):
            if atlas.curve_coordinates(t)==(At,Bt):matches.append((b,t))
        assert len(matches)==1
        branch,target=matches[0]
        PP,QQ,images=bridge.velu_pair(3,kernel,A,B,P0,Q0)
        assert F.key(PP)==F.key(F.point(target['P']))
        assert F.key(QQ)==F.key(F.point(target['Q']))
        rec={'kernel_line':kernel['line'],'matched_R131_branch':branch,
             'A':At,'B':Bt,'P_plus_matches':True,'Q_plus_matches':True,
             'P_plus':[v.tolist() for v in PP],'Q_plus':[v.tolist() for v in QQ]}
        j=atlas.j(At,Bt)[0]
        if j in [9,10,44]:
            W,metadata=atlas.evaluate(At,Bt,PP,QQ,list(range(820)))
            assert r.equal(W,r.from_json(target['evaluation_matrix']))
            rec.update(actual_weight2_values_match=True,matched_value_count=820*73,atlas=metadata)
        checks.append(rec)
        print('matched source_j9 degree3 branch',branch,'j',j,flush=True)
    D=atlas.permute([[1,0],[0,3]],list(range(820)))
    assert [i+1 for i in D]==atlas.raw['operators']['3']['necklace_transport_1based']
    # Explicitly exercise the CM4 source-model isomorphism and all four images.
    path2=args.script_dir/'data/p41_prime3_CM4_kernels47.json.gz'
    data2=json.loads(gzip.decompress(path2.read_bytes()))
    A,B,P0,Q0,c=bridge.source_basis('CM4')
    cmchecks=[]
    for kernel in data2['kernels']:
        PP,QQ,_=bridge.velu_pair(3,kernel,A,B,P0,Q0)
        cmchecks.append({'line':kernel['line'],'A':kernel['velu_A'],'B':kernel['velu_B'],
                         'P_plus':[v.tolist() for v in PP],'Q_plus':[v.tolist() for v in QQ],
                         'target_curve_and_41_torsion_checks':True})
    out={'scope':'Actual kernel-polynomial Velu bridge, all four independent R131 degree3 bases and CM4 source homothety; not a complete height evaluation',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'kernel_certificate_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [path,path2]},
         'atlas_source_sha256':hashlib.sha256((args.script_dir/'p41_supersingular_atlas47.py').read_bytes()).hexdigest(),
         'source_j9_checks':checks,'CM4_source_homothety':c,'CM4_checks':cmchecks,
         'necklace_D_action_matches_independent_R131':True,'input_sha256':atlas.a.inputs}
    sha=save(args.output,out)
    print('COMPLETE',sha,'seconds',round(time.monotonic()-started,3),flush=True)


if __name__=='__main__':main()
