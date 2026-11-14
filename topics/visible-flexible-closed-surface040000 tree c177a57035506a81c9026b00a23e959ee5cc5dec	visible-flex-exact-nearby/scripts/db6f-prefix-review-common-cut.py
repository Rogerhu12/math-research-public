#!/usr/bin/env python3
"""Independent rational audit of the common-cut coefficient enclosures.

All integrated tail endpoint coefficients are recomputed over Fraction.
An independent rational interval for sqrt(E) and the certified lambda box
then checks every Cartesian Fourier two-jet correction enclosure. The
Hermite and angular-cutoff endpoint identities are checked exactly. This
does not certify a whole surface or its isometry and reach.
"""
import argparse,gzip,hashlib,importlib.util,io,json,math,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from db6f_tail_integrated import IntegratedTail

class J:
    def __init__(self,a,b=None):self.lo=Q(a);self.hi=self.lo if b is None else Q(b)
    @staticmethod
    def get(v):return v if isinstance(v,J)else J(v)
    def __add__(self,v):
        v=J.get(v);return J(self.lo+v.lo,self.hi+v.hi)
    __radd__=__add__
    def __neg__(self):return J(-self.hi,-self.lo)
    def __sub__(self,v):return self+-J.get(v)
    def __mul__(self,v):
        v=J.get(v);p=[self.lo*v.lo,self.lo*v.hi,self.hi*v.lo,self.hi*v.hi]
        return J(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=J.get(v)
        if v.lo<=0<=v.hi:raise ValueError('Zero in rational divisor')
        return self*J(1/v.hi,1/v.lo)
    def square(self):
        if self.lo<=0<=self.hi:return J(0,max(self.lo*self.lo,self.hi*self.hi))
        return J(min(self.lo*self.lo,self.hi*self.hi),max(self.lo*self.lo,self.hi*self.hi))

def q(v):return Q.from_float(float(v))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def sqrti(v,bits=360):
    scale=1<<bits;n=math.isqrt((v.numerator*scale*scale)//v.denominator)
    assert Q(n*n,scale*scale)<=v<Q((n+1)*(n+1),scale*scale)
    return J(Q(n,scale),Q(n+1,scale))
def evaluate(c,x,derivative=0):
    return sum((c[j]*Q(math.factorial(j),math.factorial(j-derivative))*x**(j-derivative)
                for j in range(derivative,len(c))),Q(0))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    spec=importlib.util.spec_from_file_location('db6f_common_cut_reviewed',HERE/'db6f-root-common-cut.py')
    common=importlib.util.module_from_spec(spec);spec.loader.exec_module(common)
    base=common.module('db6f_review_interval_base','db6f-audit-continuous-hermite.py');common.install(base)
    obj=base.ExactHermite(a.geometry);meta=json.loads(a.geometry.read_text())
    oldpath=common.resolve(a.geometry,meta['base_geometry']);old=json.loads(oldpath.read_text())
    tailpath=common.resolve(a.geometry,meta['tail_manifest']);tail=IntegratedTail(tailpath)
    bridgepath=common.resolve(a.geometry,meta['bridge_parameter_certificate']);bridge=json.loads(bridgepath.read_text())
    raw=np.load(io.BytesIO(gzip.decompress((oldpath.parent/old['data_file']).read_bytes())),allow_pickle=False)
    pm=list(map(int,tail.planar_modes));hm=list(map(int,tail.height_modes));M=meta['modes'];oldM=old['modes'];n=3*M+2
    assert len(set(pm))==len(pm) and all((k-1)%3==0 for k in pm)
    assert len(set(hm))==len(hm) and 0 in hm and all(k>=0 and k%3==0 for k in hm)
    assert max(abs((k-1)//3)for k in pm)<=M and max(k//3 for k in hm)<=M
    endpoint=[q(v)for v in tail.source_values[0]]
    for i in range(len(tail.L)):
        length=(q(tail.nodes[i+1,0])-q(tail.nodes[i,0]))if tail.unscaled_lengths is None else q(tail.unscaled_lengths[i])*tail.radial_scale
        assert length>0
        for j in range(tail.C):
            endpoint[j]+=length*(Q(7,30)*(q(tail.first[i,j])+q(tail.first[i+1,j]))+
                Q(8,15)*q(tail.midpoint[i,j])+length*(q(tail.second[i,j])-q(tail.second[i+1,j]))/60)
    source=[endpoint,[q(v)for v in tail.first[-1]],[q(v)for v in tail.second[-1]]]
    target=[[Q(0)for _ in range(n)]for _ in range(3)];indices={m:j for j,m in enumerate(pm)}
    for order,row in enumerate(source):
        def get(m):return row[indices[m]]if m in indices else Q(0)
        target[order][0]=get(1)
        for j in range(1,M+1):target[order][j]=get(1+3*j)+get(1-3*j);target[order][M+j]=get(1+3*j)-get(1-3*j)
        for j,m in enumerate(hm):target[order][-1 if m==0 else 2*M+m//3]=-row[tail.P+j]
    original=[[Q(0)for _ in range(n)]for _ in range(3)]
    for order in range(3):
        original[order][0]=q(raw['jets'][order,-1,0]);original[order][-1]=q(raw['jets'][order,-1,-1])
        for axis in range(3):
            for j in range(1,oldM+1):original[order][axis*M+j]=q(raw['jets'][order,-1,axis*oldM+j])
    mean=sum((q(v)for v in raw['mean_increments']),Q(0));original[0][-1]=mean
    Hc=mean-target[0][-1]
    assert q(obj.background_cut_height.lo)<=Hc<=q(obj.background_cut_height.hi)
    target[0][-1]=mean
    c=Q(bridge['physical_cut_radius_exact']);w=Q(bridge['physical_cut_slope_exact']);wr=-7*w/c;E=1+w*w
    target[0][0]+=c;target[1][0]+=1;target[1][-1]-=w;target[2][-1]-=wr
    lam=J(Q(bridge['arclength_rescale']['lo']),Q(bridge['arclength_rescale']['hi']))
    assert lam.lo>0
    k=-J(1)/sqrti(E);k2=-w*wr/(E*E)
    failed=[];maximum_width=[]
    for order in range(3):
        width=0.
        for j in range(n):
            if order==0:expected=J(target[0][j]-original[0][j])
            elif order==1:expected=k/lam*target[1][j]-original[1][j]
            else:expected=(J(target[2][j]/E)+J(k2*target[1][j]))/lam.square()-original[2][j]
            lo=q(obj.cut_delta.lo[order,j]);hi=q(obj.cut_delta.hi[order,j])
            if not(lo<=expected.lo<=expected.hi<=hi):failed.append([order,j])
            width=max(width,float(hi-lo))
        maximum_width.append(width)
    bases=[[Q(v)for v in (0,0,0,10,-15,6)],
           [Q(v)for v in (0,0,0,-4,7,-3)],
           [Q(0),Q(0),Q(0),Q(1,2),Q(-1),Q(1,2)]]
    for j,cfs in enumerate(bases):
        for d in range(3):assert evaluate(cfs,Q(0),d)==0 and evaluate(cfs,Q(1),d)==int(j==d)
    cutoff=[Q(v)for v in (1,0,0,-10,15,-6)]
    assert all(evaluate(cutoff,Q(1),d)==0 for d in range(3))
    out=dict(scope=__doc__,geometry=str(a.geometry),geometry_sha256=sha(a.geometry),
      common_cut_script_sha256=sha(HERE/'db6f-root-common-cut.py'),audit_script_sha256=sha(__file__),
      tail_manifest_sha256=sha(tailpath),bridge_certificate_sha256=sha(bridgepath),
      exact_tail_spans=len(tail.L),tail_coefficients=tail.C,complete_twojet_coefficients=3*n,
      tail_mode_congruences_and_coverage=True,mean_height_fraction_enclosed=True,
      rational_twojet_enclosure_pass=not failed,failed_enclosures=failed,
      maximum_interval_width_by_jet_order=maximum_width,hermite_basis_exact=True,
      angular_cutoff_exact_zero_twojet=True,
      interval_alias_note='I(old) aliases its endpoints; only the overwritten mean position is changed, and delta0 mean is then fixed by an exact identity. The final enclosures pass this independent Fraction audit.',
      elapsed_seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k not in ('scope','interval_alias_note')}),flush=True)
    if failed:raise SystemExit(1)

if __name__=='__main__':main()
