#!/usr/bin/env python3
"""Streaming-reader one-step tail fit with immediate actual-field checkpoint.

The exact existing prefix is retained. After the tail sample table is made,
the defining raw-tail arrays are released. Unfitted floating Fourier terms
are charged by their full coefficient sum in the sampled diagnostic. Each
invocation performs ONE linear fit, saves its actual C2 field immediately,
and saves the next radial weights for a later invocation if needed.
"""
import argparse
import gc
import hashlib
from fractions import Fraction
import resource
import gzip
import importlib.util
import io
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('fd2d_c2_tail_lowmem_source',HERE/'fd2d-metric-c2-material-field-candidate.py')
source=importlib.util.module_from_spec(sp);sys.modules[sp.name]=source;sp.loader.exec_module(source)
np=source.np

# This adapter is used only to propose actual field coefficients. The final
# continuous consumer still reads the exact original map independently.
import db6f_tail_integrated as tail_reader_module
OriginalIntegratedTail=tail_reader_module.IntegratedTail


class ThinIntegratedTail(OriginalIntegratedTail):
    """Read validated raw shards into only the arrays used by point()."""
    def __init__(self,manifest):
        self.manifest_path=Path(manifest);self.meta=json.loads(self.manifest_path.read_text())
        if self.meta['status'] not in ['finite-C2-integrated-explicit-tail-with-sampled-audit',
                'finite-C2-increment-integrated-explicit-tail-with-sampled-audit'] or not self.meta.get('finished'):
            raise ValueError('Incomplete or unsupported actual tail')
        fmt=self.meta['format'];self.planar_modes=np.array(fmt['planarModes'],dtype=int)
        self.height_modes=np.array(fmt['heightModes'],dtype=int);self.P=len(self.planar_modes)
        self.C=fmt['coefficientCount'];n=sum(x['rows'] for x in self.meta['files'])-len(self.meta['files'])+1
        self.first=np.empty((n,self.C));self.second=np.empty_like(self.first)
        mids=np.empty_like(self.first);rdisplay=np.empty(n);increments=np.empty(n)
        firstnode=None;last=None;cursor=0
        for part in self.meta['files']:
            path=Path(part['path'])
            if not path.exists():path=self.manifest_path.parent/path.name
            payload=path.read_bytes()
            if hashlib.sha256(payload).hexdigest()!=part['sha256']:raise ValueError('Changed actual raw shard')
            raw=gzip.decompress(payload);del payload
            a=np.frombuffer(raw,dtype='<f8').reshape(part['rows'],part['columns'])
            if not np.isfinite(a).all():raise ValueError('Nonfinite actual raw input')
            if last is not None:
                if not np.array_equal(a[0],last):raise ValueError('Different raw interface rows')
                b=a[1:]
            else:b=a;firstnode=a[0,2:2+self.C].copy()
            last=a[-1].copy();end=cursor+len(b)
            v=b[:,2:2+4*self.C].reshape(len(b),4,self.C)
            self.first[cursor:end]=v[:,1];self.second[cursor:end]=v[:,2];mids[cursor:end]=v[:,3]
            rdisplay[cursor:end]=b[:,0];increments[cursor:end]=b[:,-1]
            cursor=end;del a,b,v,raw
        if cursor!=n:raise ValueError('Raw row coverage mismatch')
        self.source_values=firstnode[None,:];self.midpoint=mids[1:]
        if 'radialGeometry' in self.meta:
            radial=self.meta['radialGeometry'];self.unscaled_lengths=increments[1:]
            self.radial_scale=Fraction(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
            scale=np.longdouble(self.radial_scale.numerator)/np.longdouble(self.radial_scale.denominator)
            self.L=self.unscaled_lengths.astype(np.longdouble)*scale
            self.r=np.concatenate([np.array([radial['innerAnchor']],dtype=np.longdouble),
                    np.longdouble(radial['innerAnchor'])+np.cumsum(self.L)])
            self.r[-1]=np.longdouble(radial['outerAnchor'])
        else:
            self.unscaled_lengths=None;self.radial_scale=Fraction(1);self.r=rdisplay;self.L=np.diff(self.r)
        if not np.all(self.L>0):raise ValueError('Nonpositive actual tail span')
        self.value_nodes=np.empty((n,self.C),dtype=np.longdouble);self.value_nodes[0]=firstnode
        running=np.zeros(self.C,dtype=np.longdouble);anchor=firstnode.astype(np.longdouble)
        for start in range(0,n-1,64):
            stop=min(n-1,start+64);L=self.L[start:stop,None]
            inc=L*((np.longdouble(7)/30)*(self.first[start:stop].astype(np.longdouble)+self.first[start+1:stop+1])+
                    (np.longdouble(8)/15)*self.midpoint[start:stop]+
                    L*(self.second[start:stop].astype(np.longdouble)-self.second[start+1:stop+1])/60)
            for j,x in enumerate(inc):
                running=running+x;self.value_nodes[start+j+1]=anchor+running
        print(json.dumps(dict(stage='streaming_sample_reader_loaded',nodes=n,modes=self.C,
                peak_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024)),flush=True)


tail_reader_module.IntegratedTail=ThinIntegratedTail


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix-field',type=Path,required=True);p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--target',type=Path,required=True);p.add_argument('--tail',type=Path,required=True)
    p.add_argument('--tail-packet',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True)
    p.add_argument('--weights-from',type=Path);p.add_argument('--cells',type=int,default=1024)
    p.add_argument('--modes',type=int,default=192);p.add_argument('--angular',type=int,default=512)
    p.add_argument('--quadrature',type=int,default=6);p.add_argument('--tail-start',type=float,default=.4)
    p.add_argument('--cut-zero-width',type=float,default=.01);p.add_argument('--inner-zero-width',type=float,default=.002)
    args=p.parse_args();started=time.monotonic()
    if args.out_dir.exists():raise FileExistsError('Use a new directory')
    meta=json.loads(args.geometry.read_text());pf=json.loads(args.prefix_field.read_text())
    if pf['region']!='prefix' or meta['tail_manifest_sha256']!=source.screen.r105.sha(args.tail):raise ValueError('Wrong own input')
    for shard in pf['shards']:
        path=Path(shard['file'])
        if not path.exists():path=args.prefix_field.parent/path.name
        if source.screen.identity(path)['sha256']!=shard['sha256']:raise ValueError('Existing prefix bytes changed')
    args.out_dir.mkdir(parents=True);producer=source.screen.identity(__file__)
    tail=source.screen.Tail(args.tail,args.tail_packet,args.angular)
    knots=np.linspace(args.tail_start,float(tail.reader.r[-1]),args.cells+1)
    region=source.Region('tail',tail,knots,args.angular,args.quadrature)
    region.reader=None;del tail;gc.collect()
    omitted=2*np.sum(abs(region.error[:,:,:,args.modes+1:]),axis=-1)
    omitted_metric=float(np.max(np.maximum(omitted[:,:,0]+omitted[:,:,1],omitted[:,:,1]+omitted[:,:,2])))
    region.error=np.ascontiguousarray(region.error[:,:,:,:args.modes+1]);gc.collect()
    fixed=region.fixed(args.cut_zero_width,args.inner_zero_width)
    weights=np.ones(len(region.h))
    if args.weights_from:
        with np.load(io.BytesIO(gzip.decompress(args.weights_from.read_bytes())),allow_pickle=False) as raw:
            if not np.array_equal(raw['mesh'],region.knots):raise ValueError('Weights belong to a different radial field mesh')
            weights=raw['weights'].copy()
        if weights.shape!=(len(region.h),) or np.any(weights<=0):raise ValueError('Invalid previous weights')
    print(json.dumps(dict(stage='raw_arrays_released',unfitted_sampled_fourier_metric_bound=omitted_metric,
                         seconds=time.monotonic()-started)),flush=True)
    jets,stats,radial=region.fit(args.modes,weights,fixed)
    actual=jets.copy();actual[:,:,1]/=region.scale;actual[:,:,2]/=region.scale**2
    for i,f,j in zip(*np.nonzero(fixed.reshape(-1,2,3))):actual[i,f,j]=0
    field,real=source.write_field(args.out_dir,'tail',region,actual,producer)
    print(json.dumps(dict(stage='actual_field_saved',field=field,fit_sampled=stats,seconds=time.monotonic()-started)),flush=True)
    floor=max(float(np.median(radial)),1e-13)
    weights*=np.sqrt(np.maximum(1,radial/floor));weights/=np.mean(weights);weights=np.clip(weights,1e-4,1e4)
    buffer=io.BytesIO();np.savez(buffer,mesh=region.knots,weights=weights)
    wp=args.out_dir/'weights-next.npz.gz';wp.write_bytes(gzip.compress(buffer.getvalue(),mtime=0))
    del jets,actual;gc.collect()
    observed=source.screen_saved(region,real,args.angular)
    observed['metric_plus_unfitted_fourier_bound']=observed['metric']+omitted_metric
    report=dict(schema='fd2d-lowmem-tail-c2-field-production-v1',status='ACTUAL_FIELDS_DEFINED__METRIC_UNVERIFIED',
        scope=__doc__,script=producer,shared_producer=source.screen.identity(HERE/'fd2d-metric-c2-material-field-candidate.py'),
        geometry=source.screen.identity(args.geometry),target=source.screen.identity(args.target),
        tail=source.screen.identity(args.tail),tail_packet=source.screen.identity(args.tail_packet),
        fields=[source.screen.identity(args.prefix_field),field],old_tail_sampled_metric=region.old_max,
        fit_sampled=stats,actual_saved_tail_sampled_linear_residual=observed,
        unfitted_sampled_fourier_metric_bound=omitted_metric,next_weights=source.screen.identity(wp),
        prior_weights=None if args.weights_from is None else source.screen.identity(args.weights_from),
        prefix_recomputed=False,continuous_linear_residual_certified=False,nonlinear_pullback_certified=False,
        README_complete=False,seconds=time.monotonic()-started)
    report['streaming_sampler_original_reader']=source.screen.identity(HERE/'db6f_tail_integrated.py')
    report['peak_rss_bytes']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
    out=args.out_dir/'production.json';out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(out),actual_saved_tail=observed,seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
