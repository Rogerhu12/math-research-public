#!/usr/bin/env python3
"""Fixed beta=1/4 continuous support boxes for the unchanged normalized pulse.

The raw common quintic is 26e53. Its actual normalization lambda/lambda_s is
consumed from the completed R648 certificates, never recomputed. Each one of
the 819 exact radial pieces is covered independently with Q8192 and four
closed radial subdivisions. The original last cell is restricted by exact
Fraction parameters; derivatives always use its original width. This is an
open-prefix support enclosure, not a closed-surface or reach certificate.
Default CLI execution only prepares bindings. --execute performs declared
pieces once and does not change grids after an unsuccessful enclosure.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time
import numpy as np

INPUT_SHA='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
INDEX_SHA='df41433b71147ac11d3f0193be31323d7e23a879cb2b05231d3a3e166b0d88fb'
INTERVAL_SHA='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
COMPONENT_SHA='459dc01e8e5a7fb2b1910c2f0fb028f196eb0921855386c3858c26ba13a33afc'
SCALING_SHA='d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882'
ORIGINAL_WORK=Path('/workspace/scratch/16f63c8bce6b')
Q=8192
RADIAL_SUBDIVISIONS=4
BETA=Fraction(1,4)
MIDPOINT=Fraction(1)-Fraction(5,2**60)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def ff(x):
    return Fraction.from_float(float(x))

def entry_key(text):
    cell,part=text.split(':',1)
    return int(cell),part

class Reader:
    def __init__(self,input_path,interval_source,gram_index,component_source):
        self.input=Path(input_path);self.interval_source=Path(interval_source)
        self.gram_index=Path(gram_index);self.component_source=Path(component_source)
        self.source_path=Path(__file__);self.source_sha=sha(self.source_path)
        self.bindings={str(self.input):INPUT_SHA,str(self.interval_source):INTERVAL_SHA,
                       str(self.gram_index):INDEX_SHA,str(self.component_source):COMPONENT_SHA,
                       str(self.source_path):self.source_sha}
        self.assert_bindings()
        self.I=load_module(self.interval_source,'weighted_support_interval_arithmetic')
        data=json.loads(gzip.decompress(self.input.read_bytes()))
        self.M=int(data['M']);self.x=np.asarray(data['mesh'],float)
        self.Y=np.asarray(data['states'],float);self.V=np.asarray(data['rhs'],float)
        self.A=np.asarray(data['d2'],float)
        shape=(819,962)
        if self.M!=320 or self.x.shape!=(819,) or self.x[0]!=0 or self.x[-1]!=1:
            raise ValueError('Different fixed common-quintic domain')
        if not np.isfinite(self.x).all() or not np.all(np.diff(self.x)>0):
            raise ValueError('Nonfinite or unordered original nodes')
        if any(v.shape!=shape or not np.isfinite(v).all() for v in (self.Y,self.V,self.A)):
            raise ValueError('Missing/nonfinite literal common jets')
        self.jet_sha=hashlib.sha256(b''.join(np.ascontiguousarray(v,dtype='<f8').tobytes()
                                           for v in (self.x,self.Y,self.V,self.A))).hexdigest()
        index=json.loads(self.gram_index.read_bytes())
        if index['input_sha256']!=INPUT_SHA or index['planned']!=819 or index['completed']!=819:
            raise ValueError('Different or incomplete R648 index')
        if index['failures'] or index['fatal'] is not None or not index['complete_scope_certified']:
            raise ValueError('R648 final index did not certify its fixed complete scope')
        if len(index['entries'])!=819:
            raise ValueError('Different piece count')
        self.scaling={};self.report_bindings={}
        for e in index['entries']:
            if e['status']!='certified':raise ValueError('Uncertified scaling source entry')
            original=Path(e['report_path']);path=original
            if not path.exists():
                path=self.input.resolve().parent/original.relative_to(ORIGINAL_WORK)
            digest=sha(path)
            if digest!=e['report_sha256']:raise ValueError('Scaling report changed: '+str(path))
            r=json.loads(path.read_bytes());key=(int(e['cell']),e['part'])
            if key in self.scaling or (r['cell'],r['part'])!=key:
                raise ValueError('Duplicate/misidentified scaling piece')
            if r['input_sha256']!=INPUT_SHA or r['source_sha256']!=SCALING_SHA:
                raise ValueError('Different scaling candidate or source')
            if INTERVAL_SHA not in r['dependencies'].values():
                raise ValueError('Different interval dependency')
            if (r['construction_angles'],r['audit_angles'],r['scalar_panels'])!=(4096,16384,4096):
                raise ValueError('Different original construction/certificate parameters')
            if not r['all_radius_and_angle_covered'] or not r['strict_under_stated_IEEE_arithmetic']:
                raise ValueError('Unpaid scaling interval')
            cell,part=key
            if not 0<=cell<818 or r['original_left']!=self.x[cell] or r['original_right']!=self.x[cell+1]:
                raise ValueError('Scaling report is not bound to this original cell')
            left,right=Fraction(r['left_exact']),Fraction(r['right_exact'])
            e0,e1=float(r['lambda_minus_one']),float(r['lambda_s'])
            if not all(math.isfinite(v) and v>=0 for v in (e0,e1)) or e0>=1:
                raise ValueError('Invalid certified normalization bounds')
            if not ff(self.x[cell])<=left<right<=ff(self.x[cell+1]):
                raise ValueError('Piece outside original cell')
            if r['whole_original_cell_covered']!=(left==ff(self.x[cell]) and right==ff(self.x[cell+1])):
                raise ValueError('Scaling whole-cell flag disagrees with exact endpoints')
            row=dict(cell=cell,part=part,left_exact=str(left),right_exact=str(right),
                     lambda_minus_one=e0,lambda_s=e1,report_path=str(path),report_sha256=digest)
            self.scaling[key]=row;self.report_bindings[str(path)]=digest
        expected={(i,'all')for i in range(817)}|{(817,'before'),(817,'after')}
        if set(self.scaling)!=expected:raise ValueError('Missing or extra fixed piece')
        for cell in range(818):
            rows=sorted((r for (i,_),r in self.scaling.items()if i==cell),key=lambda r:Fraction(r['left_exact']))
            edge=ff(self.x[cell])
            for row in rows:
                if Fraction(row['left_exact'])!=edge:raise ValueError('Gap or overlap in exact piece cover')
                edge=Fraction(row['right_exact'])
            if edge!=ff(self.x[cell+1]):raise ValueError('Uncovered cell endpoint')
        if Fraction(self.scaling[817,'before']['right_exact'])!=MIDPOINT:
            raise ValueError('Changed exact pulse switch')
        self.nu=2*np.arange(self.M+1);self.transform=None;self.visited=set()

    def assert_bindings(self,all_reports=False):
        for p,s in self.bindings.items():
            if sha(p)!=s:raise ValueError('Frozen input/source changed: '+p)
        if all_reports:
            for p,s in self.report_bindings.items():
                if sha(p)!=s:raise ValueError('Consumed scaling report changed: '+p)

    def metadata(self):
        return dict(scope=__doc__,source_sha256=self.source_sha,input_sha256=INPUT_SHA,
                    interval_source_sha256=INTERVAL_SHA,component_formula_source_sha256=COMPONENT_SHA,
                    scaling_source_sha256=SCALING_SHA,scaling_index_sha256=INDEX_SHA,
                    nodal_jets_little_endian_float64_sha256=self.jet_sha,M=self.M,
                    construction_angles=4096,angles=Q,radial_subdivisions=RADIAL_SUBDIVISIONS,
                    beta_exact=str(BETA),center=[0,0,0],normal_orientation='G_phi cross G_s',
                    original_cells=818,exact_pieces=819,exact_switch=str(MIDPOINT),
                    normalization_recomputed=False,closed_surface=False,reach_certified=False)

    def fraction_box(self,value):
        v=float(value);lo=hi=v
        if ff(v)>value:lo=np.nextafter(v,-np.inf)
        if ff(v)<value:hi=np.nextafter(v,np.inf)
        if not ff(lo)<=value<=ff(hi):raise ValueError('Rational parameter was not enclosed')
        return np.asarray(lo),np.asarray(hi)

    def split(self,b,value=Fraction(1,2)):
        I=self.I;degree=len(b[0])-1
        if value==0:return I.stack([I.at(b,0)]*(degree+1)),b
        if value==1:return b,I.stack([I.at(b,-1)]*(degree+1))
        if not 0<value<1:raise ValueError('Bad exact Bezier split parameter')
        u=self.fraction_box(value);one_minus_u=I.sub(I.exact(1.),u)
        work=b;left=[I.at(work,0)];right=[I.at(work,-1)]
        for _ in range(degree):
            work=I.add(I.mul(one_minus_u,I.at(work,slice(None,-1))),I.mul(u,I.at(work,slice(1,None))))
            left.append(I.at(work,0));right.append(I.at(work,-1))
        return I.stack(left),I.stack(list(reversed(right)))

    def restrict(self,b,u0,u1):
        if not 0<=u0<u1<=1:raise ValueError('Bad exact original-cell interval')
        if u0==0 and u1==1:return b
        right=self.split(b,u0)[1]
        return self.split(right,(u1-u0)/(1-u0))[0]

    def pieces(self,b):
        pieces=[b]
        for _ in range(2):pieces=[v for z in pieces for v in self.split(z)]
        return pieces

    def elevate(self,b,target):
        I=self.I
        while len(b[0])-1<target:
            d=len(b[0])-1;out=[I.at(b,0)]
            for j in range(1,d+1):
                out.append(I.div(I.add(I.scale(I.at(b,j-1),j),I.scale(I.at(b,j),d+1-j)),I.exact(d+1)))
            out.append(I.at(b,-1));b=I.stack(out)
        return b

    def original_jets(self,cell):
        I=self.I;h=I.sub(I.exact(self.x[cell+1]),I.exact(self.x[cell]));h2=I.square(h)
        y0=I.exact(self.Y[cell]);y1=I.exact(self.Y[cell+1])
        v0=I.mul(h,I.exact(self.V[cell]));v1=I.mul(h,I.exact(self.V[cell+1]))
        a0=I.mul(h2,I.exact(self.A[cell]));a1=I.mul(h2,I.exact(self.A[cell+1]))
        b=I.stack([y0,I.add(y0,I.div(v0,I.exact(5))),
            I.add(I.add(y0,I.div(I.scale(v0,2),I.exact(5))),I.div(a0,I.exact(20))),
            I.add(I.sub(y1,I.div(I.scale(v1,2),I.exact(5))),I.div(a1,I.exact(20))),
            I.sub(y1,I.div(v1,I.exact(5))),y1])
        db=I.div(I.scale(I.sub(I.at(b,slice(1,None)),I.at(b,slice(None,-1))),5),h)
        return b,self.elevate(db,5)

    def center_and_remainder(self,b):
        center=(np.zeros_like(b[0]),np.zeros_like(b[1]));rem=(b[0].copy(),b[1].copy())
        for k in (0,1):
            center[k][:,2*self.M+1]=b[k][:,2*self.M+1];rem[k][:,2*self.M+1]=0.
        return center,rem

    def normalized_jets(self,b,db,row):
        I=self.I;c,r=self.center_and_remainder(b);cs,rs=self.center_and_remainder(db)
        e0,e1=row['lambda_minus_one'],row['lambda_s']
        lam=I.add(I.exact(1.),(-e0,e0));lamp=(-e1,e1)
        G=I.add(c,I.mul(lam,r))
        Gs=I.add(cs,I.add(I.mul(lam,rs),I.mul(lamp,r)))
        return G,Gs

    def channels(self,b):
        I=self.I;M=self.M;nu=self.nu
        R=I.at(b,(slice(None),slice(0,M+1)))
        t=I.at(b,(slice(None),slice(M+1,2*M+1)))
        T=(np.pad(t[0],((0,0),(1,0))),np.pad(t[1],((0,0),(1,0))))
        Z=I.at(b,(slice(None),slice(2*M+1,None)))
        dr=I.neg(I.add(I.scale(R,nu),T));dt=I.add(R,I.scale(T,nu));dz=I.neg(I.scale(Z,nu))
        return list(zip((R,T,Z),('cos','sin','cos'))),list(zip((dr,dt,dz),('sin','cos','sin')))

    def angular(self,c,parity):
        I=self.I;tr=self.transform;nu=self.nu
        val=tr.cosine_sine(c,Q,parity)
        deriv=tr.cosine_sine(I.scale(c,-nu if parity=='cos'else nu),Q,'sin'if parity=='cos'else'cos')
        second=tr.cosine_sine(I.scale(c,-nu*nu),Q,parity)
        discount=I.sub(I.exact(1.),I.scale(self.halfstep2,(2*self.M)**2))[0]
        if discount<=0:raise ValueError('Nonpositive trigonometric Bernstein discount')
        B2=float(I.div(I.exact(float(I.absolute_upper(second).max())),I.exact(discount))[1])
        return self.pieces(val),self.pieces(deriv),B2

    def vector_boxes(self,data,subcell):
        I=self.I;out=[]
        for values,derivatives,B2 in data:
            p=values[subcell];dp=derivatives[subcell]
            lo=p[0].min(axis=0);hi=p[1].max(axis=0)
            Dp=I.absolute_upper(dp).max(axis=0)
            loss=I.add(I.mul(self.step,I.exact(Dp)),I.mul(self.halfstep2,I.exact(B2)))[1]
            out.append((I.down(lo-loss),I.up(hi+loss)))
        return out

    def cross(self,v,w):
        I=self.I
        return [I.sub(I.mul(v[(j+1)%3],w[(j+2)%3]),I.mul(v[(j+2)%3],w[(j+1)%3]))for j in range(3)]

    def dot(self,v,w):
        I=self.I
        return I.add(I.add(I.mul(v[0],w[0]),I.mul(v[1],w[1])),I.mul(v[2],w[2]))

    def certify(self,cell,part):
        key=(int(cell),part)
        if key not in self.scaling:raise ValueError('Unknown fixed piece')
        if key in self.visited:raise ValueError('This Reader already visited this piece; reuse its result')
        self.visited.add(key);begin=time.perf_counter();row=self.scaling[key]
        self.assert_bindings()
        if sha(row['report_path'])!=row['report_sha256']:raise ValueError('Scaling evidence changed')
        I=self.I
        np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
        if self.transform is None:
            self.transform=I.Transform(Q)
            self.step=I.div(I.exact(self.transform.pi_upper),I.exact(Q))
            self.halfstep2=I.scale(I.square(self.step),.5)
        b,db=self.original_jets(cell)
        left,right=Fraction(row['left_exact']),Fraction(row['right_exact'])
        original_left,original_right=ff(self.x[cell]),ff(self.x[cell+1]);width=original_right-original_left
        u0,u1=(left-original_left)/width,(right-original_left)/width
        b=self.restrict(b,u0,u1);db=self.restrict(db,u0,u1)
        G,Gs=self.normalized_jets(b,db,row)
        X,T=self.channels(G);V,_=self.channels(Gs)
        vectors={name:[self.angular(c,parity)for c,parity in values]
                 for name,values in (('position',X),('radial',V),('angular',T))}
        lower=float('inf');min_normal2=float('inf');min_numerator=float('inf')
        worst=None;normal_failures=0;support_failures=0;details=[]
        for sub in range(RADIAL_SUBDIVISIONS):
            xb,vb,tb=[self.vector_boxes(vectors[name],sub)for name in ('position','radial','angular')]
            normal=self.cross(tb,vb)
            normal2=I.add(I.add(I.square(normal[0]),I.square(normal[1])),I.square(normal[2]))
            weighted=[xb[0],xb[1],I.scale(xb[2],.25)]
            numerator=self.dot(weighted,normal)
            nlo=float(normal2[0].min());slo=float(numerator[0].min())
            min_normal2=min(min_normal2,nlo);min_numerator=min(min_numerator,slo)
            bad=int(np.count_nonzero(normal2[0]<=0));normal_failures+=bad
            if bad:
                details.append(dict(radial_subcell=sub,normal_squared_lower=nlo,numerator_lower=slo,
                                    support_lower=None,unpaid_normal_boxes=bad))
                continue
            norm=I.sqrt(normal2);support=I.div(numerator,norm)
            if not np.isfinite(support[0]).all()or not np.isfinite(support[1]).all():
                raise ValueError('Nonfinite support enclosure')
            idx=int(np.argmin(support[0]));value=float(support[0][idx])
            support_failures+=int(np.count_nonzero(support[0]<=0))
            details.append(dict(radial_subcell=sub,normal_squared_lower=nlo,numerator_lower=slo,
                                support_lower=value,worst_angle_grid_index=idx))
            if value<lower:
                lower=value
                worst=dict(radial_subcell=sub,angle_grid_index=idx,
                           numerator_interval=[float(numerator[k][idx])for k in (0,1)],
                           normal_length_interval=[float(norm[k][idx])for k in (0,1)],
                           support_interval=[float(support[k][idx])for k in (0,1)])
        valid_normal=normal_failures==0
        support_lower=lower if valid_normal and math.isfinite(lower)else None
        positive=valid_normal and support_lower is not None and support_lower>0
        self.assert_bindings()
        if sha(row['report_path'])!=row['report_sha256']:raise ValueError('Scaling evidence changed during piece')
        return dict(**self.metadata(),cell=cell,part=part,left_exact=str(left),right_exact=str(right),
                    original_left_exact=str(original_left),original_right_exact=str(original_right),
                    restriction_parameters=[str(u0),str(u1)],original_width_used_for_derivatives=True,
                    scaling_certificate=row,normal_squared_lower=min_normal2,numerator_lower=min_numerator,
                    support_lower=support_lower,normal_nonzero_certified=valid_normal,
                    positive_weighted_support_certified=bool(positive),
                    status='certified'if positive else'enclosure_did_not_certify_positive_support',
                    unpaid_normal_boxes=normal_failures,nonpositive_support_boxes=support_failures,
                    worst_address=worst,radial_subcells=details,
                    angular_second_bounds={name:[v[2]for v in values]for name,values in vectors.items()},
                    all_radius_and_angle_covered=True,strict_under_stated_IEEE_arithmetic=True,
                    seconds=time.perf_counter()-begin)

def main(args):
    reader=Reader(args.input,args.interval_source,args.gram_index,args.component_source)
    keys=[entry_key(text)for text in args.entries]
    if len(set(keys))!=len(keys)or any(key not in reader.scaling for key in keys):
        raise ValueError('Duplicate or unknown declared pieces')
    if args.out.exists():raise ValueError('Output already exists; consume it rather than overwrite')
    if not args.execute:
        result=dict(**reader.metadata(),mode='bindings_only_no_geometry',
                    requested=[reader.scaling[key]for key in keys],scientific_readout_executed=False)
    else:
        records=[]
        for key in keys:
            record=reader.certify(*key);records.append(record)
            print(json.dumps({k:record[k]for k in ('cell','part','status','support_lower','normal_squared_lower','seconds')}),flush=True)
        result=dict(**reader.metadata(),mode='declared_pieces_executed_once',records=records,
                    requested_count=len(keys),all_requested_positive=all(r['positive_weighted_support_certified']for r in records),
                    scientific_readout_executed=True)
    reader.assert_bindings(all_reports=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.out),sha256=sha(args.out))),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('input','interval-source','gram-index','component-source','out'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--entries',nargs='+',default=['0:all','390:all','498:all','817:before','817:after'])
    parser.add_argument('--execute',action='store_true')
    main(parser.parse_args())
