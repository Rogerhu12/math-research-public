#!/usr/bin/env python3
"""Actual raw level-41 transport through every edge of a constant isogeny DAG.

Raw phi(P),phi(Q) are retained: their matrix determinant is the total degree.
The program never rescales Q by the degree.  Full1681-point lookup tables make
every basis identification an equality of actual elliptic-curve points.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def source_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def initialize(folder):
    sys.path.insert(0,str(folder))
    from p41_supersingular_atlas47 import Atlas
    return Atlas(folder,folder/'data/p41_cleared_serre_derivative47_complete.json.gz')


class FullLevelTransport:
    def __init__(self,at):
        from p41_supersingular_atlas47 import ResidueField,cp,ci,cm
        from p41_kernel_level_bridge47 import KernelBridge
        self.at,self.a,self.r,self.np=at,at.a,at.r,at.np
        old=at.F
        np=at.np
        reduction=np.zeros((159,80),dtype=np.int64)
        reduction[:80]=np.eye(80,dtype=np.int64)
        for n in range(80,159):
            last=int(reduction[n-1,-1])
            reduction[n]=np.concatenate([np.zeros(1,dtype=np.int64),reduction[n-1,:-1]])
            reduction[n]=(reduction[n]-last*old.f[:-1])%47
        assert 80*46**2<2**63 and 159*46**2<2**63
        class FastResidueField(ResidueField):
            def __init__(self,old,reduction):
                self.__dict__.update(old.__dict__)
                self.reduction=reduction
            def mul(self,a,b):
                return (self.np.convolve(a,b)%47)@self.reduction%47
        self.F=FastResidueField(old,reduction)
        for a,b in [(old.ii,old.ii),(old.f[:80],old.ii),
                    (np.arange(80,dtype=np.int64)%47,np.arange(79,-1,-1,dtype=np.int64)%47)]:
            assert old.eq(self.F.mul(a,b),old.mul(a,b))
        at.F=self.F
        self.bridge=KernelBridge(at)
        self.reduction_sha=hashlib.sha256(reduction.astype('<i8').tobytes()).hexdigest()
        self.roots={4:{},6:{}}
        for d in (4,6):
            for x in range(47):
                for y in range(47):
                    if x==0 and y==0:continue
                    self.roots[d].setdefault(cp((x,y),d,47),[]).append((x,y))
        self.refs={str(j):v for j,v in at.refs.items()}
        c4=at.a.cm4
        c3=at.a.read('p41_cm3_makdisi47_certificate.json')
        self.refs['CM4']={'label':'CM4_exact_A1_B0','A':(1,0),'B':(0,0),
                         'P':[v[0] for v in c4['P_jets']],'Q':[v[0] for v in c4['Q_jets']]}
        self.refs['CM3']={'label':'CM3_exact_A0_B1','A':(0,0),'B':(1,0),
                         'P':[v[0] for v in c3['P_jets']],'Q':[v[0] for v in c3['Q_jets']]}
        self.lookup_tables={}
        self.inverse_reference={k:{'A':ci(v['A']) if k not in ['0','CM3'] else None,
                                   'B':ci(v['B']) if k in ['0','CM3'] else None}
                                for k,v in self.refs.items()}

    def prepare_table(self,key):
        if key in self.lookup_tables:return self.lookup_tables[key]
        from p41_actual_differentials47 import digest
        ref=self.refs[key];F=self.F;np=self.np
        A,B=F.embed(ref['A']),F.embed(ref['B'])
        P,Q=F.point(ref['P']),F.point(ref['Q'])
        assert F.on_curve(P,A,B) and F.on_curve(Q,A,B)
        pj,qj=F.jac(P),F.jac(Q)
        assert not np.any(F.scalar(pj,41,A)[2]) and not np.any(F.scalar(qj,41,A)[2])
        PP,QQ=[F.jac(None)],[F.jac(None)]
        for _ in range(40):
            PP.append(F.jadd(PP[-1],pj,A));QQ.append(F.jadd(QQ[-1],qj,A))
        points=F.affine_batch([F.jadd(PP[a],QQ[b],A) for a in range(41) for b in range(41)])
        lookup={F.key(T):divmod(k,41) for k,T in enumerate(points)}
        assert len(lookup)==1681 and lookup[b'']==(0,0)
        for T in points:
            assert T is None or F.on_curve(T,A,B)
        cert={'points':1681,'all_on_curve':True,'actual_basis_41_torsion':True,
              'ordered_point_table_sha256':hashlib.sha256(b''.join(F.key(v) for v in points)).hexdigest()}
        self.lookup_tables[key]={'points':points,'lookup':lookup,'certificate':cert}
        print('actual1681 table',key,cert['ordered_point_table_sha256'],flush=True)
        return self.lookup_tables[key]

    def match(self,A,B,key=None):
        from p41_supersingular_atlas47 import cp,ci,ca,cs,cm,ck
        j=self.at.j(A,B)
        assert j[1]==0 and j[0] in self.at.refs
        key=key or str(j[0]);ref=self.refs[key]
        d=6 if key in ['0','CM3'] else 4
        ratio=cm(B,self.inverse_reference[key]['B']) if d==6 else cm(A,self.inverse_reference[key]['A'])
        candidates=self.roots[d].get(tuple(x%47 for x in ratio),[])
        assert len(candidates)==d
        for cbar in candidates:
            An=cm(A,ci(cp(cbar,4,47),47),47)
            Bn=cm(B,ci(cp(cbar,6,47),47),47)
            if An!=tuple(x%47 for x in ref['A']) or Bn!=tuple(x%47 for x in ref['B']):continue
            c=cbar
            for _ in range(2):c=cs(c,cm(cs(cp(c,d),ratio),ci(ck(cp(c,d-1),d))))
            assert cp(c,d)==ratio
            An=cm(A,ci(cp(c,4)));Bn=cm(B,ci(cp(c,6)))
            t=cs(An,ref['A']) if d==6 else cs(Bn,ref['B'])
            assert all(x%47==0 for x in t)
            return key,c,t
        raise ArithmeticError('No actual reference isomorphism')

    def matrix(self,key,c,P,Q,degree):
        from p41_supersingular_atlas47 import cp,ci
        F=self.F;ref=self.refs[key];tab=self.prepare_table(key)
        ic=ci(c,47);ic2,ic3=F.embed(cp(ic,2,47)),F.embed(cp(ic,3,47))
        columns=[]
        for T in [P,Q]:
            U=F.mul(T[0],ic2),F.mul(T[1],ic3)
            assert F.on_curve(U,F.embed(ref['A']),F.embed(ref['B']))
            ab=tab['lookup'][F.key(U)]
            assert ab!=(0,0)
            assert F.key(tab['points'][41*ab[0]+ab[1]])==F.key(U)
            columns.append(ab)
        g=[[columns[0][0],columns[1][0]],[columns[0][1],columns[1][1]]]
        assert (g[0][0]*g[1][1]-g[0][1]*g[1][0])%41==degree%41
        return g

    def recover_pair(self,record):
        from p41_supersingular_atlas47 import cp
        key=record['reference_key'];tab=self.prepare_table(key)
        F=self.F;c=tuple(record['homothety']);g=record['raw_level_matrix_mod41']
        c2,c3=F.embed(cp(c,2,47)),F.embed(cp(c,3,47))
        out=[]
        for k in range(2):
            P=tab['points'][41*g[0][k]+g[1][k]]
            out.append((F.mul(P[0],c2),F.mul(P[1],c3)))
        return out

    def raw_pair(self,node,P,Q):
        F=self.F
        ell=node['ell'];A,B=tuple(node['source_A']),tuple(node['source_B'])
        At,Bt=tuple(node['A']),tuple(node['B'])
        Af,Bf=F.embed(A),F.embed(B);Atf,Btf=F.embed(At),F.embed(Bt)
        h=[tuple(x) for x in node['kernel']]
        for T in (P,Q):assert F.on_curve(T,Af,Bf)
        if ell==2:
            r=F.neg(F.embed(h[0]));t=F.add(F.scale(F.mul(r,r),3),Af)
            denominators=[F.sub(T[0],r) for T in (P,Q)]
            iv=F.inverse(F.mul(*denominators))
            inverses=[F.mul(iv,denominators[1]),F.mul(iv,denominators[0])]
            out=[]
            for T,iv in zip((P,Q),inverses):
                xx=F.add(T[0],F.mul(t,iv))
                yy=F.mul(T[1],F.sub(F.one,F.mul(t,F.mul(iv,iv))))
                U=xx,yy
                assert F.on_curve(U,Atf,Btf)
                out.append(U)
            return out
        vals=[self.bridge.polynomial_derivatives(h,T[0]) for T in (P,Q)]
        iv=F.inverse(F.mul(vals[0][0],vals[1][0]))
        inverses=[F.mul(iv,vals[1][0]),F.mul(iv,vals[0][0])]
        s1=F.neg(F.embed(h[-2]));out=[]
        for T,V,iv in zip((P,Q),vals,inverses):
            S1=F.mul(V[1],iv);H2=F.mul(V[2],iv)
            S2=F.sub(F.mul(S1,S1),F.scale(H2,2))
            S3=F.add(F.sub(F.mul(F.mul(S1,S1),S1),F.scale(F.mul(S1,H2),3)),F.scale(F.mul(V[3],iv),3))
            x,y=T;x2=F.mul(x,x)
            f=F.add(F.add(F.mul(x2,x),F.mul(Af,x)),Bf)
            fp=F.add(F.scale(x2,3),Af)
            xx=F.add(F.sub(F.sub(F.scale(x,ell),F.scale(s1,2)),F.scale(F.mul(fp,S1),2)),F.scale(F.mul(f,S2),4))
            dx=F.sub(F.add(F.sub(F.scale(F.one,ell),F.scale(F.mul(x,S1),12)),F.scale(F.mul(fp,S2),6)),F.scale(F.mul(f,S3),8))
            U=xx,F.mul(y,dx)
            assert F.on_curve(U,Atf,Btf)
            out.append(U)
        return out

    def record(self,A,B,P,Q,degree,source_indices):
        from p41_supersingular_atlas47 import cp,ci,cm
        key,c,t=self.match(A,B)
        g=self.matrix(key,c,P,Q,degree)
        out={'degree':degree,'reference_key':key,'homothety':c,'reference_parameter':t,
             'raw_level_matrix_mod41':g,'determinant_mod41':degree%41,
             'image_indices_1based':[i+1 for i in self.at.permute(g,source_indices)]}
        if key in ['0','36']:
            ckey='CM3' if key=='0' else 'CM4'
            _,cc,tt=self.match(A,B,ckey)
            gg=self.matrix(ckey,cc,P,Q,degree)
            uu=cm(cp(A,3),ci(cp(B,2))) if ckey=='CM3' else cm(cp(B,2),ci(cp(A,3)))
            assert uu==cp(tt,3 if ckey=='CM3' else 2)
            out['coarse']={'reference_key':ckey,'homothety':cc,'stack_parameter':tt,
                           'invariant_parameter':uu,'raw_level_matrix_mod41':gg,
                           'image_indices_1based':[i+1 for i in self.at.permute(gg,source_indices)]}
        return out

    def run_dag(self,data,outpath,dag_sha,checkpoint=100,limit=None):
        from p41_actual_differentials47 import save
        curve=data['curve'];nodes=data['nodes']
        if curve=='source_j9':
            frame=self.a.read('p41_hecke3_formal_height47_compact.json.gz')
            I=[i-1 for i in frame['families'][0]['points_1based']]
        else:I=[i-1 for i in self.a.cm4['elliptic_necklace_indices_1based']]
        records={}
        if Path(outpath).exists():
            previous=read(outpath)
            assert previous['constant_dag_sha256']==dag_sha
            assert previous['source_sha256']==source_digest(__file__)
            records=previous['nodes']
        A,B,P,Q,c=self.bridge.source_basis(curve)
        if '1' not in records:records['1']=self.record(A,B,P,Q,1,I)
        start=time.monotonic()
        def obj():
            return {'scope':'Actual raw41-torsion transport; determinant equals total isogeny degree',
                    'curve':curve,'order':data['order'],'constant_dag_sha256':dag_sha,
                    'source_necklace_indices_1based':[i+1 for i in I],
                    'node_count':len(nodes),'completed_count':len(records),'complete':len(records)==len(nodes),
                    'nodes':records,'source_sha256':source_digest(__file__),
                    'residue_multiplication_reduction_sha256':self.reduction_sha,
                    'reference_tables':{k:v['certificate'] for k,v in self.lookup_tables.items()},
                    'input_sha256':self.a.inputs}
        keys=sorted(nodes,key=lambda key:(len(nodes[key]['path']),key))
        for key in keys:
            if key in records:continue
            node=nodes[key]
            P,Q=self.recover_pair(records[node['parent']])
            P,Q=self.raw_pair(node,P,Q)
            records[key]=self.record(tuple(node['A']),tuple(node['B']),P,Q,node['degree'],I)
            if len(records)%checkpoint==0:
                save(outpath,obj())
                print('rawlevel',curve,len(records),'/',len(nodes),'seconds',round(time.monotonic()-start,2),flush=True)
            if limit and len(records)>=limit:break
        result=obj();sha=save(outpath,result)
        print('level saved',curve,len(records),sha,flush=True)
        return result


def small_data(at,curve):
    from p41_supersingular_atlas47 import cp,ck,cs
    from p41_actual_differentials47 import Q
    A,B=((1,0),(32,0)) if curve=='source_j9' else ((Q-1,0),(0,0))
    nodes={'1':{'key':'1','degree':1,'A':A,'B':B,'path':[]}}
    for ell in (2,3):
        if ell==3:
            d=read(at.a.folder/f'data/p41_prime3_{curve}_kernels47.json.gz')
            kernels=d['kernels']
        else:
            if curve=='source_j9':roots=[tuple(t['kernel_x']) for t in at.raw['operators']['2']['targets']]
            else:roots=[(0,0),(1,0),(Q-1,0)]
            kernels=[]
            from p41_supersingular_atlas47 import cm
            for k,t in enumerate(roots):
                At=cs(ck(A,-4),ck(cp(t,2),15))
                Bt=cs(ck(cm(A,t),-8),ck(cp(t,3),22))
                kernels.append({'line':k,'kernel_polynomial_ascending':[ck(t,-1),(1,0)],'velu_A':At,'velu_B':Bt})
        for k in kernels:
            key=str(ell)+':'+str(k['line'])
            nodes[key]={'key':key,'parent':'1','degree':ell,'ell':ell,'source_A':A,'source_B':B,
                        'kernel':k['kernel_polynomial_ascending'],'A':k['velu_A'],'B':k['velu_B'],'path':[key]}
    return {'curve':curve,'order':'small-independent','nodes':nodes}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--dag',type=Path)
    ap.add_argument('--curve',choices=['source_j9','CM4'],default='source_j9')
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--limit',type=int)
    args=ap.parse_args();start=time.monotonic()
    at=initialize(args.script_dir.resolve());transport=FullLevelTransport(at)
    if args.dag:
        data=read(args.dag);sha=source_digest(args.dag)
    else:
        data=small_data(at,args.curve)
        sha=hashlib.sha256(json.dumps(data,sort_keys=True).encode()).hexdigest()
    result=transport.run_dag(data,args.output,sha,limit=args.limit)
    print('elapsed',round(time.monotonic()-start,3),flush=True)


if __name__=='__main__':
    main()
