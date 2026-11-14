#!/usr/bin/env python3
"""Actual coprime-kernel DAGs over (Z/47^4)[i], with quartic deformations.

Input prime kernels are the published exact source-curve kernels.  A new
coprime kernel is transported inside its own finite etale quotient algebra;
no compositum of individual torsion fields is used.  Every output is written
to disk.  This program computes isogeny models, not heights or QC roots.
"""
import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

from p41_etale_torsion_lift47 import QuadraticRing

Q = 47**4
R = QuadraticRing(Q)
INDICES = [1,2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30,31,
           33,34,35,37,38,39,42,46,4,51,53,55,57,58,59,61,62,65,66,
           67,69,70,71,73,74,77,78,79,83,85,86,87,89,91]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(obj, sort_keys=True, separators=(',', ':'))+'\n').encode()
    raw = gzip.compress(raw, mtime=0) if path.suffix == '.gz' else raw
    tmp = path.with_name(path.name+'.tmp')
    tmp.write_bytes(raw)
    tmp.replace(path)
    return digest(path)


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def factors(n):
    out = []
    for p in range(2, n+1):
        if n % p == 0:
            out.append(p)
            n //= p
            assert n % p, 'Only squarefree degrees are accepted here'
        if n == 1:
            break
    return out


def trim(a, B=R):
    a = list(a)
    while a and a[-1] == B.zero:
        a.pop()
    return a


def padd(a, b, B=R):
    out = list(a)+[B.zero]*max(0, len(b)-len(a))
    for j, x in enumerate(b):
        out[j] = B.add(out[j], x)
    return trim(out, B)


def pneg(a, B=R):
    return [B.neg(x) for x in a]


def psub(a, b, B=R):
    return padd(a, pneg(b, B), B)


def pscale(a, x, B=R):
    return trim([B.mul(v, x) for v in a], B)


def pmul(a, b, B=R):
    if not a or not b:
        return []
    out = [B.zero]*(len(a)+len(b)-1)
    for j, x in enumerate(a):
        if x != B.zero:
            for k, y in enumerate(b):
                if y != B.zero:
                    out[j+k] = B.add(out[j+k], B.mul(x, y))
    return trim(out, B)


def pdiv(a, b, B=R):
    a, b = trim(a, B), trim(b, B)
    assert b
    iv = B.inverse(b[-1])
    q = [B.zero]*max(0, len(a)-len(b)+1)
    while len(a) >= len(b):
        k = len(a)-len(b)
        v = B.mul(a[-1], iv)
        q[k] = v
        for j, x in enumerate(b):
            a[k+j] = B.sub(a[k+j], B.mul(v, x))
        a = trim(a, B)
    return trim(q, B), a


def derivative(a, B=R):
    return [B.scale(a[j], j) for j in range(1, len(a))]


def newton_sums(h, n, B=R):
    d = len(h)-1
    assert d and h[-1] == B.one
    out = [B.integer(d)]
    for k in range(1, n+1):
        total = B.zero
        for j in range(1, min(k, d)+1):
            if j == k:
                total = B.add(total, B.scale(h[d-j], k))
            else:
                total = B.add(total, B.mul(h[d-j], out[k-j]))
        out.append(B.neg(total))
    return out


class EtaleKernel:
    """Constant finite etale algebra R[x]/h; h need not be irreducible."""
    def __init__(self, h):
        self.h = [tuple(v) for v in h]
        self.degree = len(h)-1
        assert self.degree >= 1 and self.h[-1] == R.one
        self.zero = (R.zero,)*self.degree
        self.one = (R.one,)+(R.zero,)*(self.degree-1)
        self.generator = self.reduce([R.zero, R.one])
        self.traces = newton_sums(self.h, self.degree-1)

    def constant(self, c):
        return (tuple(c),)+(R.zero,)*(self.degree-1)

    def integer(self, n):
        return self.constant(R.integer(n))

    def reduce(self, a):
        a = list(a)
        d = self.degree
        for k in range(len(a)-1, d-1, -1):
            v = a[k]
            if v != R.zero:
                for j in range(d):
                    a[k-d+j] = R.sub(a[k-d+j], R.mul(v, self.h[j]))
        return tuple(a[:d]+[R.zero]*max(0, d-len(a)))

    def add(self, a, b):
        return tuple(R.add(x,y) for x,y in zip(a,b))

    def sub(self, a, b):
        return tuple(R.sub(x,y) for x,y in zip(a,b))

    def neg(self, a):
        return tuple(R.neg(x) for x in a)

    def scale(self, a, n):
        return tuple(R.scale(x,n) for x in a)

    def mul(self, a, b):
        return self.reduce(pmul(a, b))

    power = QuadraticRing.power

    def inverse(self, a):
        F = QuadraticRing(47)
        h = [(x % 47,y % 47) for x,y in self.h]
        u = trim([(x % 47,y % 47) for x,y in a], F)
        r0,r1 = h,u
        t0,t1 = [],[F.one]
        while r1:
            q,r2 = pdiv(r0,r1,F)
            r0,r1 = r1,r2
            t0,t1 = t1,psub(t0,pmul(q,t1,F),F)
        assert len(r0) == 1, 'Denominator is not a unit in the etale algebra'
        t0 = pscale(t0,F.inverse(r0[0]),F)
        b = self.reduce(t0)
        for _ in range(2):
            b = self.mul(b,self.sub(self.integer(2),self.mul(a,b)))
        assert self.mul(a,b) == self.one
        return b

    def trace(self, a):
        s = R.zero
        for x,t in zip(a,self.traces):
            s = R.add(s,R.mul(x,t))
        return s

    def charpoly(self, a):
        power = self.one
        sums = [R.integer(self.degree)]
        coefficients = [R.one]
        for k in range(1,self.degree+1):
            power = self.mul(power,a)
            sums.append(self.trace(power))
            s = sums[k]
            for j in range(1,k):
                s = R.add(s,R.mul(coefficients[j],sums[k-j]))
            coefficients.append(R.scale(R.neg(s),pow(k,-1,Q)))
        h = list(reversed(coefficients))
        assert self.value(h,a) == self.zero
        return h

    def value(self, coefficients, x):
        out = self.zero
        for c in reversed(coefficients):
            out = self.add(self.mul(out,x),self.constant(c))
        return out


class Jets:
    def __init__(self, B, size=5):
        self.base,self.size = B,size
        self.zero = (B.zero,)*size
        self.one = (B.one,)+(B.zero,)*(size-1)

    def constant(self,a):
        return (a,)+(self.base.zero,)*(self.size-1)

    def integer(self,n):
        return self.constant(self.base.integer(n))

    def add(self,a,b):
        return tuple(self.base.add(x,y) for x,y in zip(a,b))

    def neg(self,a):
        return tuple(self.base.neg(x) for x in a)

    def sub(self,a,b):
        return self.add(a,self.neg(b))

    def mul(self,a,b):
        out = [self.base.zero]*self.size
        for n in range(self.size):
            for j in range(n+1):
                if a[j] != self.base.zero and b[n-j] != self.base.zero:
                    out[n] = self.base.add(out[n],self.base.mul(a[j],b[n-j]))
        return tuple(out)

    def scale(self,a,n):
        return tuple(self.base.scale(x,n) for x in a)

    def inverse(self,a):
        iv = self.base.inverse(a[0])
        out = [iv]+[self.base.zero]*(self.size-1)
        for n in range(1,self.size):
            s = self.base.zero
            for j in range(1,n+1):
                s = self.base.add(s,self.base.mul(a[j],out[n-j]))
            out[n] = self.base.neg(self.base.mul(iv,s))
        return tuple(out)

    power = QuadraticRing.power


class Dual:
    """Differentiate before reducing the x variable by h."""
    def __init__(self,B):
        self.base=B
        self.zero=(B.zero,B.zero)
        self.one=(B.one,B.zero)

    def integer(self,n):
        return self.base.integer(n),self.base.zero

    def add(self,a,b):
        return self.base.add(a[0],b[0]),self.base.add(a[1],b[1])

    def neg(self,a):
        return self.base.neg(a[0]),self.base.neg(a[1])

    def sub(self,a,b):
        return self.add(a,self.neg(b))

    def mul(self,a,b):
        B=self.base
        return B.mul(a[0],b[0]),B.add(B.mul(a[0],b[1]),B.mul(a[1],b[0]))

    def scale(self,a,n):
        return self.base.scale(a[0],n),self.base.scale(a[1],n)

    power = QuadraticRing.power


def division_polynomial(ell,x,A,B,F):
    """psi_ell for odd ell, or the cubic for ell=2, over an arbitrary ring."""
    x2=F.mul(x,x)
    f=F.add(F.add(F.mul(x2,x),F.mul(A,x)),B)
    if ell == 2:
        return f
    x3=F.mul(x2,x)
    x4=F.mul(x2,x2)
    A2=F.mul(A,A)
    p3=F.sub(F.add(F.add(F.scale(x4,3),F.scale(F.mul(A,x2),6)),F.scale(F.mul(B,x),12)),A2)
    p4=F.sub(F.add(F.add(F.mul(x3,x3),F.scale(F.mul(A,x4),5)),F.scale(F.mul(B,x3),20)),F.scale(F.mul(A2,x2),5))
    p4=F.sub(F.sub(F.sub(p4,F.scale(F.mul(F.mul(A,B),x),4)),F.scale(F.mul(B,B),8)),F.mul(A2,A))
    p4=F.scale(p4,2)
    cache={0:F.zero,1:F.one,2:F.one,3:p3,4:p4}
    f16=F.scale(F.mul(f,f),16)
    def rec(n):
        if n in cache:
            return cache[n]
        m=n//2
        if n % 2:
            u=F.mul(rec(m+2),F.power(rec(m),3))
            v=F.mul(rec(m-1),F.power(rec(m+1),3))
            if m % 2:
                v=F.mul(v,f16)
            else:
                u=F.mul(u,f16)
            out=F.sub(u,v)
        else:
            out=F.mul(rec(m),F.sub(F.mul(rec(m+2),F.power(rec(m-1),2)),F.mul(rec(m-2),F.power(rec(m+1),2))))
        cache[n]=out
        return out
    return rec(ell)


def velu_model(ell,h,A,B):
    sums=newton_sums(h,3)
    d=len(h)-1
    t=R.add(R.scale(sums[2],3),R.scale(A,d))
    w=R.add(R.add(R.scale(sums[3],5),R.scale(R.mul(A,sums[1]),3)),R.scale(B,2*d))
    if ell == 2:
        assert d == 1
        At,Bt=R.sub(A,R.scale(t,5)),R.sub(B,R.scale(w,7))
    else:
        assert d == (ell-1)//2
        At,Bt=R.sub(A,R.scale(t,10)),R.sub(B,R.scale(w,14))
    delta=R.add(R.scale(R.power(At,3),4),R.scale(R.power(Bt,2),27))
    assert R.is_unit(delta)
    return At,Bt


def transport_kernel(h,edge):
    S=EtaleKernel(h)
    x=S.generator
    A,B=tuple(edge['source_A']),tuple(edge['source_B'])
    kernel=[tuple(v) for v in edge['kernel']]
    ell=edge['ell']
    if ell == 2:
        r=R.neg(kernel[0])
        inv=S.inverse(S.sub(x,S.constant(r)))
        phi=S.add(x,S.mul(S.constant(R.add(R.scale(R.mul(r,r),3),A)),inv))
    else:
        hh=S.value(kernel,x)
        inv=S.inverse(hh)
        h1=S.value(derivative(kernel),x)
        h2=S.value(derivative(derivative(kernel)),x)
        S1=S.mul(h1,inv)
        S2=S.sub(S.mul(S1,S1),S.mul(h2,inv))
        f=S.add(S.add(S.power(x,3),S.mul(S.constant(A),x)),S.constant(B))
        fp=S.add(S.scale(S.mul(x,x),3),S.constant(A))
        s1=R.neg(kernel[-2])
        phi=S.add(S.sub(S.sub(S.scale(x,ell),S.constant(R.scale(s1,2))),S.scale(S.mul(fp,S1),2)),S.scale(S.mul(f,S2),4))
    out=S.charpoly(phi)
    # The transported point remains of the intended prime order on the target.
    return out


def roots_cubic(A,B):
    F=QuadraticRing(47)
    roots=[]
    for u in range(47):
        for v in range(47):
            x=(u,v)
            if F.add(F.add(F.power(x,3),F.mul(tuple(t%47 for t in A),x)),tuple(t%47 for t in B)) != F.zero:
                continue
            for _ in range(2):
                err=R.add(R.add(R.power(x,3),R.mul(A,x)),B)
                dx=R.add(R.scale(R.mul(x,x),3),A)
                x=R.sub(x,R.mul(err,R.inverse(dx)))
            assert R.add(R.add(R.power(x,3),R.mul(A,x)),B) == R.zero
            roots.append(x)
    assert len(roots) == 3
    return roots


def load_primes(script_dir,curve):
    A,B={'source_j9':(R.integer(1),R.integer(32)),'CM4':(R.integer(-1),R.zero)}[curve]
    primes=sorted(set(q for n in INDICES if n != 4 for q in factors(n)))
    allkernels={}
    inputs={}
    for ell in primes:
        if ell == 2:
            kernels=[]
            for line,r in enumerate(roots_cubic(A,B)):
                h=[R.neg(r),R.one]
                At,Bt=velu_model(2,h,A,B)
                kernels.append({'line':line,'kernel_polynomial_ascending':h,'velu_A':At,'velu_B':Bt})
        else:
            path=Path(script_dir)/f'data/p41_prime{ell}_{curve}_kernels47.json.gz'
            data=read(path)
            assert data['modulus']==Q and data['base_A']%Q==A[0] and data['base_B']%Q==B[0]
            inputs[str(path.name)]=digest(path)
            kernels=data['kernels']
        allkernels[ell]=kernels
        for k in kernels:
            h=[tuple(x) for x in k['kernel_polynomial_ascending']]
            assert velu_model(ell,h,A,B) == (tuple(k['velu_A']),tuple(k['velu_B']))
    return A,B,allkernels,inputs


def nodekey(pairs):
    return '/'.join(f'{ell}:{line}' for ell,line in pairs) or '1'


def build_dag(script_dir,curve,order):
    A,B,primes,inputs=load_primes(script_dir,curve)
    nodes={'1':{'key':'1','degree':1,'A':A,'B':B,'path':[]}}
    targets={}
    def getpath(pairs):
        key=nodekey(pairs)
        if key in nodes:
            return nodes[key]
        parent=getpath(pairs[:-1])
        ell,line=pairs[-1]
        h=[tuple(v) for v in primes[ell][line]['kernel_polynomial_ascending']]
        for edgekey in parent['path']:
            h=transport_kernel(h,nodes[edgekey])
        At,Bt=velu_model(ell,h,tuple(parent['A']),tuple(parent['B']))
        # Coprime etale subgroup transport is proved algebraically in R209.
        # Unit inverses and the complete characteristic polynomial are checked
        # by transport_kernel.  Published prime inputs already certify exact
        # order; do not repeat their large division-polynomial computations.
        nodes[key]={'key':key,'parent':parent['key'],'degree':parent['degree']*ell,
                    'ell':ell,'line':line,'source_A':parent['A'],'source_B':parent['B'],
                    'kernel':h,'A':At,'B':Bt,'path':parent['path']+[key]}
        return nodes[key]
    for n in INDICES:
        if n == 4:
            rows=[]
            for line in range(3):
                parent=getpath([(2,line)])
                r=R.neg(tuple(parent['kernel'][0]))
                dual=R.scale(r,-2)
                for k,s in enumerate(roots_cubic(tuple(parent['A']),tuple(parent['B']))):
                    h=[R.neg(s),R.one]
                    At,Bt=velu_model(2,h,tuple(parent['A']),tuple(parent['B']))
                    if s == dual:
                        assert At == R.scale(A,16) and Bt == R.scale(B,64)
                        continue
                    key=f'2:{line}/2target:{k}'
                    nodes[key]={'key':key,'parent':parent['key'],'degree':4,'ell':2,
                                'line_on_target':k,'source_A':parent['A'],'source_B':parent['B'],
                                'kernel':h,'A':At,'B':Bt,'path':parent['path']+[key],
                                'nondual_cyclic_order_four':True}
                    rows.append({'source_lines':[[2,line],[2,k]],'node':key})
            assert len(rows)==6
        else:
            ff=sorted(factors(n),reverse=order=='descending')
            rows=[]
            for lines in itertools.product(*(range(q+1) for q in ff)):
                pairs=list(zip(ff,lines))
                node=getpath(pairs)
                rows.append({'source_lines':sorted(pairs),'node':node['key']})
        targets[str(n)]=rows
        print(curve,order,'degree',n,'kernels',len(rows),'nodes',len(nodes),flush=True)
    assert sum(map(len,targets.values())) == 3282
    return {'scope':'All 54 stated cyclic Hecke target models; no heights',
            'curve':curve,'order':order,'modulus':Q,'indices':INDICES,
            'input_sha256':inputs,'nodes':nodes,'targets':targets,
            'source_sha256':digest(__file__)}


def check_orders(a,b):
    assert a['curve']==b['curve']
    checked=0
    for n in INDICES:
        if n in [1,4] or len(factors(n))<=1:
            continue
        look={tuple(map(tuple,r['source_lines'])):b['nodes'][r['node']] for r in b['targets'][str(n)]}
        for r in a['targets'][str(n)]:
            x=a['nodes'][r['node']]
            y=look[tuple(map(tuple,r['source_lines']))]
            assert tuple(x['A'])==tuple(y['A']) and tuple(x['B'])==tuple(y['B'])
            checked+=1
    assert checked==2422
    return checked


def lift_edge_quartic(node,A,B):
    S=EtaleKernel(node['kernel'])
    J=Jets(S)
    aj=tuple(S.constant(v) for v in A)
    bj=tuple(S.constant(v) for v in B)
    x=J.constant(S.generator)
    DJ=Dual(J)
    for _ in range(3):
        err,der=division_polynomial(node['ell'],(x,J.one),(aj,J.zero),(bj,J.zero),DJ)
        assert err[0]==S.zero
        x=J.sub(x,J.mul(err,J.inverse(der)))
    assert division_polynomial(node['ell'],x,aj,bj,J)==J.zero
    sums=[]
    power=J.one
    for _ in range(3):
        power=J.mul(power,x)
        sums.append(tuple(S.trace(v) for v in power))
    V=Jets(R)
    s1,s2,s3=sums
    t=V.add(V.scale(s2,3),V.scale(A,S.degree))
    w=V.add(V.add(V.scale(s3,5),V.scale(V.mul(A,s1),3)),V.scale(B,2*S.degree))
    u,v=(5,7) if node['ell']==2 else (10,14)
    At,Bt=V.sub(A,V.scale(t,u)),V.sub(B,V.scale(w,v))
    assert At[0]==tuple(node['A']) and Bt[0]==tuple(node['B'])
    return At,Bt


def ks(A,B):
    J=Jets(R,4)
    da=tuple(R.scale(A[k+1],k+1) for k in range(4))
    db=tuple(R.scale(B[k+1],k+1) for k in range(4))
    a,b=A[:4],B[:4]
    delta=J.add(J.scale(J.power(a,3),4),J.scale(J.power(b,2),27))
    numerator=J.sub(J.scale(J.mul(a,db),2),J.scale(J.mul(b,da),3))
    return J.mul(numerator,J.inverse(delta))


def lift_dag(data,outpath,checkpoint_every=100):
    V=Jets(R)
    source=data['nodes']['1']
    A=V.constant(tuple(source['A']))
    B=(tuple(source['B']),R.one,R.zero,R.zero,R.zero)
    baseks=ks(A,B)
    jets={'1':{'A':A,'B':B}}
    if Path(outpath).exists():
        old=read(outpath)
        if old.get('constant_dag_sha256')==data['certificate_sha256'] and old.get('source_sha256')==digest(__file__):
            jets={k:{'A':tuple(map(tuple,v['A'])),'B':tuple(map(tuple,v['B']))} for k,v in old['jets'].items()}
    # The stored JSON is key sorted, so reconstruct a topological order explicitly.
    keys=sorted(data['nodes'],key=lambda k:(len(data['nodes'][k]['path']),k))
    def output():
        return {'scope':'Quartic target A/B; KS checked only through t^3; not a height or full level-map certificate',
                'curve':data['curve'],'order':data['order'],'modulus':Q,'series_modulus':'t^5',
                'source_A':A,'source_B':B,'constant_dag_sha256':data['certificate_sha256'],
                'source_sha256':digest(__file__),'node_count':len(data['nodes']),
                'completed_count':len(jets),'complete':len(jets)==len(data['nodes']),
                'ks_relation':'degree * beta_target = beta_source, coefficients t^0 through t^3',
                'jets':jets}
    started=time.monotonic()
    for key in keys:
        if key in jets:
            continue
        node=data['nodes'][key]
        parent=jets[node['parent']]
        At,Bt=lift_edge_quartic(node,parent['A'],parent['B'])
        assert tuple(R.scale(v,node['degree']) for v in ks(At,Bt))==baseks
        jets[key]={'A':At,'B':Bt}
        if len(jets)%checkpoint_every==0:
            save(outpath,output())
            print('quartic',data['curve'],len(jets),'/',len(data['nodes']),'seconds',round(time.monotonic()-started,2),flush=True)
    result=output()
    sha=save(outpath,result)
    print('quartic COMPLETE',data['curve'],len(jets),sha,flush=True)
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--output-dir',type=Path,required=True)
    ap.add_argument('--curve',choices=['source_j9','CM4'],required=True)
    ap.add_argument('--quartic',action='store_true')
    ap.add_argument('--reuse-constants',action='store_true')
    args=ap.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    dags={}
    for order in ['descending','ascending']:
        path=args.output_dir/f'p41_{args.curve}_{order}_kernel_dag47.json.gz'
        if args.reuse_constants and path.exists():
            data=read(path)
            assert data['source_sha256']==digest(__file__)
        else:
            data=build_dag(args.script_dir,args.curve,order)
            save(path,data)
        data['certificate_sha256']=digest(path)
        dags[order]=data
    count=check_orders(dags['descending'],dags['ascending'])
    manifest={'curve':args.curve,'target_count':3282,'coprime_order_comparisons':count,
              'dag_sha256':{k:v['certificate_sha256'] for k,v in dags.items()},
              'node_counts':{k:len(v['nodes']) for k,v in dags.items()},'source_sha256':digest(__file__)}
    save(args.output_dir/f'p41_{args.curve}_kernel_dag47_manifest.json',manifest)
    print('constants COMPLETE',manifest,flush=True)
    if args.quartic:
        lift_dag(dags['descending'],args.output_dir/f'p41_{args.curve}_descending_quartic_dag47.json.gz')


if __name__=='__main__':
    main()
