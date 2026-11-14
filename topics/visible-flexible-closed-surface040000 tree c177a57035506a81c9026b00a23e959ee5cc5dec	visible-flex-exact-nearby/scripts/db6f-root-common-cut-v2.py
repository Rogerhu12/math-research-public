#!/usr/bin/env python3
"""Exact common-cut Hermite correction and interval verification adapter, v2.

V2 preserves the v1 map formula, uses independent interval endpoint arrays,
and checks exact increment anchors and the full threefold Fourier basis.

The corrected prefix is the saved finite map plus one Fourier/quintic
correction vanishing with its first two jets at the beginning of a short
end interval. At the cut it has the full jets of the reflected explicit
tail in the exact bridge arclength. Coefficients are defined by exact
saved binary data, rational integration, and the certified bridge root;
the interval arrays below enclose that definition, not a fitted model.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
from db6f_tail_integrated import IntegratedTail

HERE=Path(__file__).resolve().parent


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def module(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    z=importlib.util.module_from_spec(spec);sys.modules[name]=z;spec.loader.exec_module(z)
    return z


def resolve(meta_path,name):
    p=Path(name)
    if p.exists():return p
    p=Path(meta_path).parent/p.name
    if not p.exists():raise FileNotFoundError(name)
    return p


def validate_tail(tail):
    """Validate the exact radial chart and the threefold Fourier conversion."""
    fmt = tail.meta['format']
    pm, hm = fmt['planarModes'], fmt['heightModes']
    if (not pm or not hm or
        any(not isinstance(k, int) or isinstance(k, bool) for k in pm+hm) or
        len(set(pm)) != len(pm) or len(set(hm)) != len(hm) or
        any((k-1) % 3 != 0 for k in pm) or
        any(k < 0 or k % 3 != 0 for k in hm)):
        raise ValueError('Tail modes do not define the full threefold basis')
    if tail.unscaled_lengths is None:
        inner, outer = Q(float(tail.nodes[0,0])), Q(float(tail.nodes[-1,0]))
        if any(Q(float(b)) <= Q(float(a)) for a,b in zip(tail.nodes[:-1,0], tail.nodes[1:,0])):
            raise ValueError('Nonpositive exact absolute radial interval')
    else:
        radial = tail.meta['radialGeometry']
        inner, outer = Q(radial['innerAnchor']), Q(radial['outerAnchor'])
        if tail.radial_scale <= 0 or any(x <= 0 for x in tail.unscaled_lengths):
            raise ValueError('Nonpositive exact radial increment or scale')
        total = sum((Q(float(x)) for x in tail.unscaled_lengths), Q(0))
        if inner+tail.radial_scale*total != outer:
            raise ValueError('Exact radial increment sum misses the outer anchor')
    if not 0 < Q(tail.meta['parameters']['rCuff']) < inner < outer:
        raise ValueError('Tail and collar do not form the prescribed annulus')
    if outer != Q(tail.meta['parameters']['rCut']):
        raise ValueError('Tail outer anchor differs from the physical cut')
    return inner, outer


def install(base):
    original=base.ExactHermite
    I,qb=base.I,base.qbounds

    class CommonCutPrefix(original):
        def __init__(self,path):
            meta=json.loads(Path(path).read_text())
            if meta.get('representation')!='exact-common-cut-prefix':
                super().__init__(path);return
            if meta['common_cut_implementation_sha256']!=sha(__file__):raise ValueError('Common-cut implementation changed')
            oldpath=resolve(path,meta['base_geometry']);tailpath=resolve(path,meta['tail_manifest']);bridgepath=resolve(path,meta['bridge_parameter_certificate'])
            for p,k in [(oldpath,'base_geometry_sha256'),(tailpath,'tail_manifest_sha256'),(bridgepath,'bridge_parameter_certificate_sha256')]:
                if sha(p)!=meta[k]:raise ValueError('Changed common-cut input '+k)
            if sha(HERE/'db6f_tail_integrated.py')!=meta['tail_reader_sha256']:raise ValueError('Changed tail reader')
            super().__init__(oldpath)
            oldM=self.M
            rawpath=oldpath.parent/self.meta['data_file']
            raw=np.load(io.BytesIO(gzip.decompress(rawpath.read_bytes())),allow_pickle=False)
            tail=IntegratedTail(tailpath);bridge=json.loads(bridgepath.read_text())
            if bridge['geometry_sha256']!=sha(oldpath) or not bridge['unique_root_in_box']:
                raise ValueError('Bridge certificate is not bound to this original prefix')
            if self.meta.get('ell',0.)!=0.:
                raise ValueError('This closed mirror construction requires ell=0')
            inner,outer=validate_tail(tail)
            if outer!=Q(bridge['physical_cut_radius_exact']):
                raise ValueError('Tail outer radius is not the exact common cut')
            M=int(meta['modes']);C=tail.C;P=tail.P
            if M<max(oldM,max(abs((tail.planar_modes-1)//3)),max(tail.height_modes//3)):
                raise ValueError('Common basis omits a tail mode')
            # Exact polynomial endpoint value from the integrated derivative
            # definition, with every operation rounded outwards.
            if tail.unscaled_lengths is None:
                lengths=I(tail.nodes[1:,0])-I(tail.nodes[:-1,0])
            else:lengths=I(tail.unscaled_lengths)*qb(tail.radial_scale)
            if np.any(lengths.lo<=0):raise ValueError('Unproved positive radial lengths')
            L=I(lengths.lo[:,None],lengths.hi[:,None])
            inc=L*(qb(Q(7,30))*(I(tail.first[:-1])+I(tail.first[1:]))+
                   qb(Q(8,15))*I(tail.midpoint)+L*(I(tail.second[:-1])-I(tail.second[1:]))*qb(Q(1,60)))
            endpoint=I(tail.source_values[0])
            for j in range(len(tail.L)):endpoint=endpoint+inc[j]
            source=[endpoint,I(tail.first[-1]),I(tail.second[-1])]
            tl=np.zeros((3,3*M+2));th=tl.copy()
            def put(order,index,value):tl[order,index]=value.lo;th[order,index]=value.hi
            indices={int(k):j for j,k in enumerate(tail.planar_modes)}
            for order,v in enumerate(source):
                get=lambda m:v[indices[m]] if m in indices else I(0.)
                put(order,0,get(1))
                for j in range(1,M+1):
                    a,b=get(1+3*j),get(1-3*j)
                    put(order,j,a+b);put(order,M+j,a-b)
                for index,k in enumerate(tail.height_modes):
                    put(order,-1 if k==0 else 2*M+k//3,-v[P+index])
            T=I(tl,th)
            # Convert the original prefix's exact endpoint jets to this basis.
            old=np.zeros((3,3*M+2));stored=raw['jets'][:,-1,:]
            old[:,0]=stored[:,0];old[:,-1]=stored[:,-1]
            for axis in range(3):old[:,axis*M+1:axis*M+oldM+1]=stored[:,axis*oldM+1:(axis+1)*oldM+1]
            Y=I(old.copy(),old.copy())
            mean=sum((Q.from_float(float(v))for v in raw['mean_increments']),Q(0))
            exact_mean=qb(mean);Y.lo[0,-1]=exact_mean.lo;Y.hi[0,-1]=exact_mean.hi
            c=Q(bridge['physical_cut_radius_exact']);w=Q(bridge['physical_cut_slope_exact']);wr=-7*w/c
            E=1+w*w
            lam_data=bridge['arclength_rescale'];lam=I(qb(Q(lam_data['lo'])).lo,qb(Q(lam_data['hi'])).hi)
            k=-I(1.)/qb(E).sqrt();k2=qb(-w*wr/(E*E))
            T.lo[0,0],T.hi[0,0]=(T[0,0]+qb(c)).lo,(T[0,0]+qb(c)).hi
            T.lo[1,0],T.hi[1,0]=(T[1,0]+1).lo,(T[1,0]+1).hi
            self.background_cut_height=exact_mean-T[0,-1]
            T.lo[0,-1]=exact_mean.lo;T.hi[0,-1]=exact_mean.hi
            T.lo[1,-1],T.hi[1,-1]=(T[1,-1]-qb(w)).lo,(T[1,-1]-qb(w)).hi
            T.lo[2,-1],T.hi[2,-1]=(T[2,-1]-qb(wr)).lo,(T[2,-1]-qb(wr)).hi
            target=[T[0],(k/lam)*T[1],(k.square()*T[2]+k2*T[1])/lam.square()]
            delta=base.stack(target,0)-Y
            # The gauge was chosen by this exact equality, so do not lose it
            # by subtracting two independent enclosures of the same mean.
            delta.lo[0,-1]=delta.hi[0,-1]=0.
            start=int(meta['correction_start_index'])
            if not 0<start<len(self.x)-1:raise ValueError('Invalid correction start')
            b=Q.from_float(float(self.x[start]));end=Q.from_float(float(self.x[-1]));width=end-b
            W=qb(width);d0,d1,d2=delta[0],delta[1],delta[2]
            correction=[10*d0-4*W*d1+W.square()*d2/2,
                        -15*d0+7*W*d1-W.square()*d2,
                        6*d0-3*W*d1+W.square()*d2/2]
            shape=(len(self.x)-1,6,3*M+2)
            lo=np.zeros(shape);hi=lo.copy()
            lo[:,:,0]=self.power.lo[:,:,0];hi[:,:,0]=self.power.hi[:,:,0]
            lo[:,:,-1]=self.power.lo[:,:,-1];hi[:,:,-1]=self.power.hi[:,:,-1]
            for axis in range(3):
                lo[:,:,axis*M+1:axis*M+oldM+1]=self.power.lo[:,:,axis*oldM+1:(axis+1)*oldM+1]
                hi[:,:,axis*M+1:axis*M+oldM+1]=self.power.hi[:,:,axis*oldM+1:(axis+1)*oldM+1]
            power=I(lo,hi)
            for index in range(start,len(self.x)-1):
                a=(Q.from_float(float(self.x[index]))-b)/width
                h=(Q.from_float(float(self.x[index+1]))-Q.from_float(float(self.x[index])))/width
                for j in range(6):
                    term=I(np.zeros(3*M+2))
                    for degree,coeff in zip((3,4,5),correction):
                        if degree>=j:term=term+qb(math.comb(degree,j)*a**(degree-j)*h**j)*coeff
                    z=power[index,j]+term;power.lo[index,j]=z.lo;power.hi[index,j]=z.hi
            self.power=power;self.M=M;self.path=Path(path);self.meta=meta
            self.cut_delta=delta;self.cut_correction=correction;self.correction_width=width
            self.exact_common_cut_definition=True

    base.ExactHermite=CommonCutPrefix
    return CommonCutPrefix


def make(args):
    old=json.loads(args.geometry.read_text());t=IntegratedTail(args.tail)
    validate_tail(t)
    raw=np.load(io.BytesIO(gzip.decompress((args.geometry.parent/old['data_file']).read_bytes())),allow_pickle=False)
    start=int(np.searchsorted(raw['mesh'],raw['mesh'][-1]-args.width))
    if not 0<start<len(raw['mesh'])-1:raise ValueError('Invalid correction width')
    M=max(old['modes'],max(abs((t.planar_modes-1)//3)),max(t.height_modes//3))
    meta={**old,'representation':'exact-common-cut-prefix','modes':int(M),
          'base_geometry':str(args.geometry),'base_geometry_sha256':sha(args.geometry),
          'tail_manifest':str(args.tail),'tail_manifest_sha256':sha(args.tail),
          'bridge_parameter_certificate':str(args.bridge),'bridge_parameter_certificate_sha256':sha(args.bridge),
          'tail_reader_sha256':sha(HERE/'db6f_tail_integrated.py'),
          'common_cut_implementation_sha256':sha(__file__),'correction_start_index':start,
          'correction_width_requested':args.width,
          'mathematical_definition':__doc__,
          'cut_height_gauge':'Reflect the entire exported tail height; choose H(c) so the cut mean height equals the exact prefix mean.',
          'exact_common_cut_C2_by_definition':True,
          'continuous_bounds_certified':False,'complete_closed_surface':False}
    args.out.write_text(json.dumps(meta,indent=2)+'\n')
    b=module('common_cut_initial_enclosure','db6f-audit-continuous-hermite.py');install(b)
    z=b.ExactHermite(args.out)
    print(json.dumps({'modes':int(M),'corrected_spans':len(z.x)-1-start,
          'width':float(z.correction_width),
          'cut_height_interval':[float(z.background_cut_height.lo),float(z.background_cut_height.hi)],
          'cut_jet_coefficient_max_upper':[float(z.cut_delta[j].abs().hi.max())for j in range(3)],
          'exact_C2_definition':True},indent=2))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('task',choices=['make','geometry','metric','moment'])
    p.add_argument('--geometry',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--tail',type=Path);p.add_argument('--bridge',type=Path);p.add_argument('--target',type=Path)
    p.add_argument('--width',type=float,default=.15);p.add_argument('--angular',type=int,default=256)
    p.add_argument('--radial',type=int,default=1);args=p.parse_args()
    if args.task=='make':return make(args)
    if args.task=='geometry':
        mod=module('common_cut_geometry','db6f-audit-continuous-hermite.py');install(mod)
        mod.certify(SimpleNamespace(geometry=args.geometry,out=args.out,angular=args.angular,radial=args.radial,
                                   batch=16,start=0,stop=None,ell=0.,witness=True))
    elif args.task=='metric':
        mod=module('common_cut_metric','db6f-audit-metric-polynomial.py');install(mod.base)
        mod.run(SimpleNamespace(geometry=args.geometry,target=args.target,out=args.out,limit=None))
    else:
        mod=module('common_cut_moment','db6f-root-volume-moment.py');install(mod.iv)
        mod.integrate(SimpleNamespace(geometry=args.geometry,out=args.out,angular=args.angular,
                                      radial=args.radial,batch=16))


if __name__=='__main__':main()
