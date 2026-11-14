#!/usr/bin/env python3
"""Construct an actual shared-two-jet Fourier material-field candidate.

The linear fit is performed in physical angular coordinates. Prefix nodal
jets are then converted numerically to the saved psi chart and truncated
to a finite Fourier series; THOSE saved binary jets, with exact shared
quintic Hermite interpolation, define the actual C2 field. The conversion
is not asserted exact. Its actual resulting linear residual is screened
again. Tail jets use physical radius, while the radial displacement
component is in the physical meridian-arclength direction.

The field is exactly zero on both sides of the common cut, and on an inner
tail neighbourhood. Mirror conditions are exact coefficient identities.
No uniform metric claim, nonlinear pullback, or successful surface is
inferred from the finite samples in this producer.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy import fft
from scipy.interpolate import CubicSpline
from scipy.linalg import solveh_banded

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sp=importlib.util.spec_from_file_location('fd2d_c2_field_screen_source',HERE/'fd2d-metric-noncircle-gauge-screen.py')
screen=importlib.util.module_from_spec(sp);sys.modules[sp.name]=screen;sp.loader.exec_module(screen)

# Columns: value, first, second at left; value, first, second at right.
HC=np.array([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,.5,0,0,0],
    [-10,-6,-1.5,10,-4,.5],[15,8,1.5,-15,7,-1],[-6,-3,-.5,6,-3,.5]],dtype=float)


def hermite_basis(t,h,scale):
    v=np.polynomial.polynomial.polyval(t,HC)
    d=np.polynomial.polynomial.polyval(t,HC[1:]*np.arange(1,6)[:,None])/h
    factors=np.array([1,h/scale,(h/scale)**2,1,h/scale,(h/scale)**2])
    return v*factors,d*factors


def own_target(prefix,s):
    raw=prefix.raw;j=min(max(int(np.searchsorted(raw['left'],s,side='right')-1),0),len(raw['left'])-1)
    h=screen.LD(raw['right'][j])-screen.LD(raw['left'][j]);t=(screen.LD(s)-screen.LD(raw['left'][j]))/h
    v,_=screen.r105.target_point(raw,j,t)
    c=screen.r105.midpoint(raw['e_lo'][j],raw['e_hi'][j])
    v['epp']=screen.horner(c[2:]*np.arange(2,len(c),dtype=screen.LD)*np.arange(1,len(c)-1,dtype=screen.LD),t)/(h*h)
    return {k:float(x) for k,x in v.items()}


def tail_at(tail,r):
    r=screen.LD(r)
    if r<tail.reader.r[0]:return tail.point(-1,(r-tail.cuff)/tail.length)
    i=min(max(int(np.searchsorted(tail.reader.r,r,side='right')-1),0),len(tail.reader.L)-1)
    t=(r-tail.reader.r[i])/tail.reader.L[i]
    return tail.point(i,min(screen.LD(1),max(screen.LD(0),t)))


class Region:
    def __init__(self,kind,reader,knots,count,gauss):
        self.kind,self.reader,self.knots=kind,reader,np.asarray(knots,dtype=float)
        self.h=np.diff(self.knots);self.scale=float(np.median(self.h));self.count=count
        z,w=np.polynomial.legendre.leggauss(gauss);self.t=(z+1)/2;self.gw=w/2
        nc=len(self.h);self.a=np.empty((nc,gauss));self.ap=self.a.copy();self.k=self.a.copy()
        self.error=np.empty((nc,gauss,3,count//2+1),dtype=complex)
        self.target_e=np.empty((nc,gauss));self.target_ep=self.target_e.copy()
        self.old_max=0.
        self.v=np.empty((nc,gauss,6));self.d=self.v.copy()
        for i,(left,h) in enumerate(zip(self.knots[:-1],self.h)):
            for j,t in enumerate(self.t):
                x=left+h*t
                if kind=='prefix':
                    point=reader.point(screen.LD(x));target=own_target(reader,x)
                    k=1.;self.target_e[i,j]=target['e'];self.target_ep[i,j]=target['ep']
                else:point=tail_at(reader,x);k=point['ap'];self.target_e[i,j]=self.target_ep[i,j]=0.
                self.a[i,j]=point['a'];self.ap[i,j]=point['ap'];self.k[i,j]=k
                self.old_max=max(self.old_max,float(np.max(screen.r105.symmetric_norm(*point['errors']))))
                self.error[i,j]=fft.rfft(point['errors'],axis=-1,norm='forward')
                self.v[i,j],self.d[i,j]=hermite_basis(t,h,self.scale)
            if (i+1)%256==0:print(json.dumps(dict(stage='sample_'+kind,cells=i+1)),flush=True)

    def fixed(self,cut_width,inner_width):
        f=np.zeros(6*len(self.knots),dtype=bool)
        if self.kind=='prefix':
            # Native radial p is odd and q is even at the central mirror.
            f[[0,2,4]]=True
            nodes=np.nonzero(self.knots>=self.knots[-1]-cut_width)[0]
        else:
            nodes=np.nonzero((self.knots<=self.knots[0]+inner_width)|
                             (self.knots>=self.knots[-1]-cut_width))[0]
        for j in nodes:f[6*j:6*j+6]=True
        return f

    def fit(self,modes,weights,fixed):
        nc=len(self.h);dim=6*(nc+1);jets=np.zeros((nc+1,2,3,self.error.shape[-1]),dtype=complex)
        residual=self.error.copy();base=6*np.arange(nc)
        pc=np.array([0,1,2,6,7,8]);qc=np.array([3,4,5,9,10,11])
        ww=(self.h[:,None]*self.gw[None,:]*self.a/abs(self.k)*weights[:,None])[:,:,None]*np.array([1,2,1])[None,None,:]
        for n in range(modes+1):
            omega=3j*n;C=np.zeros((*self.a.shape,3,12),dtype=complex)
            C[:,:,0,pc]=2*self.k[:,:,None]*self.d
            C[:,:,1,pc]=(omega/self.a)[:,:,None]*self.v
            C[:,:,1,qc]=(self.a*self.k)[:,:,None]*self.d
            C[:,:,2,pc]=(2*self.ap/self.a)[:,:,None]*self.v
            C[:,:,2,qc]=2*omega*self.v
            H=np.einsum('cqri,cqrj,cqr->cij',C.conj(),C,ww,optimize=True)
            b=-np.einsum('cqri,cqr,cqr->ci',C.conj(),self.error[:,:,:,n],ww,optimize=True)
            ab=np.zeros((12,dim),dtype=complex);rhs=np.zeros(dim,dtype=complex)
            for i in range(12):
                np.add.at(rhs,base+i,b[:,i])
                for j in range(i+1):np.add.at(ab[i-j],base+j,H[:,i,j])
            for offset in range(12):
                starts=np.arange(dim-offset);forbidden=fixed[starts]|fixed[starts+offset]
                ab[offset,starts[forbidden]]=0
            ab[0,fixed]=1;rhs[fixed]=0
            sol=solveh_banded(ab,rhs,lower=True,overwrite_ab=True,overwrite_b=True,check_finite=False)
            unpacked=sol.reshape(nc+1,2,3);jets[:,:,:,n]=unpacked
            pair=np.concatenate((sol.reshape(nc+1,6)[:-1],sol.reshape(nc+1,6)[1:]),axis=1)
            residual[:,:,:,n]+=np.einsum('cqri,ci->cqr',C,pair,optimize=True)
        values=fft.irfft(residual,n=self.count,axis=-1,norm='forward')
        op=screen.r105.symmetric_norm(values[:,:,0],values[:,:,1],values[:,:,2])
        stats=dict(metric=float(np.max(op)),E=float(np.max(abs(values[:,:,0]))),
                   F=float(np.max(abs(values[:,:,1]))),G=float(np.max(abs(values[:,:,2]))))
        where=np.unravel_index(int(np.argmax(op)),op.shape)
        stats['worst_cell']=int(where[0]);stats['worst_quadrature']=int(where[1]);stats['worst_angle']=int(where[2])
        stats['worst_coordinate']=float(self.knots[where[0]]+self.h[where[0]]*self.t[where[1]])
        return jets,stats,op.max(axis=(1,2))


def convert_prefix(region,jets,psi_modes,material_grid=8192,psi_grid=4096):
    """Numerical conversion only; saved finite psi jets define the new field."""
    prefix=region.reader;knots=region.knots
    u=np.arange(material_grid)*2*np.pi/(3*material_grid)
    psi=np.arange(psi_grid)*2*np.pi/(3*psi_grid)
    omega=3j*np.arange(jets.shape[-1]);out=np.zeros((len(knots),2,3,psi_modes+1),dtype=complex)
    for i,s in enumerate(knots):
        target=own_target(prefix,s);e,ep,epp=target['e'],target['ep'],target['epp']
        theta=psi-e*np.sin(3*psi)/3;nu=-ep*np.sin(3*psi)/3;nus=-epp*np.sin(3*psi)/3
        for field in range(2):
            c=jets[i,field].copy();c[1]/=region.scale;c[2]/=region.scale**2
            series=np.stack((c[0],c[1],c[2],omega*c[0],omega*c[1],omega*omega*c[0]))
            values=fft.irfft(series,n=material_grid,axis=-1,norm='forward').T
            spline=CubicSpline(np.r_[u,2*np.pi/3],np.vstack((values,values[0])),axis=0,bc_type='periodic')
            v=spline(theta)
            composed=np.array((v[:,0],v[:,1]+nu*v[:,3],
                v[:,2]+2*nu*v[:,4]+nu*nu*v[:,5]+nus*v[:,3]))
            out[i,field]=fft.rfft(composed,axis=-1,norm='forward')[:,:psi_modes+1]
        if (i+1)%256==0:print(json.dumps(dict(stage='prefix_psi_conversion',nodes=i+1)),flush=True)
    # These exact equalities define the actual mirror interface, regardless
    # of tiny floating conversion noise in the preceding numerical proposal.
    out[0,0,0]=0;out[0,0,2]=0;out[0,1,1]=0
    return out


def real_coefficients(c):
    a=np.empty((*c.shape,2),dtype=float);a[...,0]=2*c.real;a[...,1]=-2*c.imag
    a[...,0,0]=c[...,0].real;a[...,0,1]=0
    return a


def complex_coefficients(a):
    c=(a[...,0]-1j*a[...,1])/2;c[...,0]=a[...,0,0]
    return c


def write_field(directory,name,region,coefficients,producer):
    out=directory/(name+'-field.json');a=real_coefficients(coefficients);parts=[]
    # Small independently hashed defining shards, each below repository limits.
    for start in range(0,len(region.knots),64):
        stop=min(len(region.knots),start+64);buffer=io.BytesIO()
        np.savez(buffer,mesh=region.knots[start:stop],jets=a[start:stop])
        payload=gzip.compress(buffer.getvalue(),mtime=0)
        if len(payload)>=5_000_000:raise ValueError('Field shard exceeds repository limit')
        path=directory/(name+f'-nodes-{start:06d}-{stop:06d}.npz.gz');path.write_bytes(payload)
        parts.append(dict(first_node=start,node_count=stop-start,**screen.identity(path)))
    meta=dict(schema='fd2d-shared-twojet-finite-fourier-material-field-v1',region=name,
        modes=coefficients.shape[-1]-1,nodes=len(region.knots),producer=producer,shards=parts,
        coordinates=('native prefix s, saved psi; material u=psi-e(s)sin(3psi)/3' if name=='prefix'
                     else 'physical radius r, physical/material theta=u'),
        components=('p is native meridian displacement; q is physical angular displacement' if name=='prefix'
                    else 'p is physical meridian-arclength displacement; q is physical angular displacement'),
        basis='sum cosine[n] cos(3n angle)+sine[n] sin(3n angle); n=0 sine is exactly zero',
        jets='exact saved binary value, native first derivative, native second derivative',
        interpolation='exact quintic Hermite from shared nodal two-jets; coefficient arithmetic interpreted over rationals',
        outside_radial_interval='field and both native derivatives are identically zero where an endpoint zero two-jet permits this extension',
        field_is_actual_saved_finite_definition=True,uniform_metric_bound_certified=False,
        inverse_material_map_certified=False,full_surface_success=False)
    out.write_text(json.dumps(meta,indent=2)+'\n');return screen.identity(out),a


def screen_saved(region,real_jets,psi_count):
    """Evaluate the ACTUAL saved field at the fit quadrature points."""
    c=complex_coefficients(real_jets);count=region.count;maximum=dict(metric=0.,E=0.,F=0.,G=0.)
    for i,h in enumerate(region.h):
        pair=np.concatenate((c[i],c[i+1]),axis=1)
        for j,t in enumerate(region.t):
            # Stored jets are actual native derivatives, so Hermite scale=1.
            v,d=hermite_basis(t,h,1.)
            values=np.einsum('j,fjn->fn',v,pair);radial=np.einsum('j,fjn->fn',d,pair)
            omega=3j*np.arange(c.shape[-1])
            if region.kind=='prefix':
                psi=np.arange(psi_count)*2*np.pi/(3*psi_count);e=region.target_e[i,j];ep=region.target_ep[i,j]
                rho=1-e*np.cos(3*psi);nu=-ep*np.sin(3*psi)/3
                f=fft.irfft(values,n=psi_count,axis=-1,norm='forward')
                fs=fft.irfft(radial,n=psi_count,axis=-1,norm='forward')
                fp=fft.irfft(values*omega,n=psi_count,axis=-1,norm='forward')
                ps=fs[0]-nu*fp[0]/rho;qs=fs[1]-nu*fp[1]/rho
                pu=fp[0]/rho;qu=fp[1]/rho
                correction=np.array((2*ps,pu/region.a[i,j]+region.a[i,j]*qs,
                                     2*region.ap[i,j]*f[0]/region.a[i,j]+2*qu))
                theta=psi-e*np.sin(3*psi)/3
                spline=CubicSpline(np.r_[theta,2*np.pi/3],np.c_[correction,correction[:,0]].T,axis=0,bc_type='periodic')
                correction=spline(region.reader.u).T
            else:
                f=fft.irfft(values,n=count,axis=-1,norm='forward')
                fs=fft.irfft(radial,n=count,axis=-1,norm='forward')*region.k[i,j]
                fu=fft.irfft(values*omega,n=count,axis=-1,norm='forward')
                correction=np.array((2*fs[0],fu[0]/region.a[i,j]+region.a[i,j]*fs[1],
                                     2*region.ap[i,j]*f[0]/region.a[i,j]+2*fu[1]))
            error=fft.irfft(region.error[i,j],n=count,axis=-1,norm='forward')+correction
            stats=dict(metric=float(np.max(screen.r105.symmetric_norm(*error))),
                       E=float(np.max(abs(error[0]))),F=float(np.max(abs(error[1]))),G=float(np.max(abs(error[2]))))
            for k in maximum:maximum[k]=max(maximum[k],stats[k])
    return maximum


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True);p.add_argument('--target',type=Path,required=True)
    p.add_argument('--tail',type=Path,required=True);p.add_argument('--tail-packet',type=Path,required=True)
    p.add_argument('--out-dir',type=Path,required=True);p.add_argument('--prefix-cells',type=int,default=1024)
    p.add_argument('--tail-cells',type=int,default=1024);p.add_argument('--modes',type=int,default=192)
    p.add_argument('--prefix-psi-modes',type=int,default=512);p.add_argument('--angular',type=int,default=512)
    p.add_argument('--psi-angular',type=int,default=2048);p.add_argument('--quadrature',type=int,default=6)
    p.add_argument('--iterations',type=int,default=4);p.add_argument('--tail-start',type=float,default=.4)
    p.add_argument('--cut-zero-width',type=float,default=.01);p.add_argument('--inner-zero-width',type=float,default=.002)
    args=p.parse_args();started=time.monotonic()
    if args.out_dir.exists():raise FileExistsError('Use a new directory')
    if not 0<=args.modes<args.angular//2:raise ValueError('Fit modes must exclude Nyquist')
    args.out_dir.mkdir(parents=True)
    producer=screen.identity(__file__)
    prefix=screen.Prefix(args.geometry,args.target,args.angular,args.psi_angular)
    tail=screen.Tail(args.tail,args.tail_packet,args.angular)
    if prefix.meta.get('tail_manifest_sha256')!=screen.r105.sha(args.tail):raise ValueError('Wrong common own tail')
    history=[];fields=[]
    for kind,reader,knots in [('prefix',prefix,np.linspace(0,float(prefix.geom.x[-1]),args.prefix_cells+1)),
                             ('tail',tail,np.linspace(args.tail_start,float(tail.reader.r[-1]),args.tail_cells+1))]:
        region=Region(kind,reader,knots,args.angular,args.quadrature)
        fixed=region.fixed(args.cut_zero_width,args.inner_zero_width);weights=np.ones(len(region.h));iterations=[]
        for it in range(args.iterations):
            jets,stats,radial=region.fit(args.modes,weights,fixed)
            entry=dict(iteration=it+1,**stats,seconds=time.monotonic()-started);iterations.append(entry)
            print(json.dumps(dict(stage='fit_'+kind,**entry)),flush=True)
            floor=max(float(np.median(radial)),1e-13)
            weights*=np.sqrt(np.maximum(1,radial/floor));weights/=np.mean(weights);weights=np.clip(weights,1e-4,1e4)
        if kind=='prefix':actual=convert_prefix(region,jets[:,:,:,:args.modes+1],args.prefix_psi_modes)
        else:
            actual=jets[:,:,:,:args.modes+1].copy();actual[:,:,1]/=region.scale;actual[:,:,2]/=region.scale**2
        # Every fully prescribed-zero node stays exactly zero after conversion.
        nodal_fixed=fixed.reshape(-1,2,3)
        for i,f,j in zip(*np.nonzero(nodal_fixed)):actual[i,f,j]=0
        record,real=write_field(args.out_dir,kind,region,actual,producer)
        actual_screen=screen_saved(region,real,max(args.psi_angular,4*(args.prefix_psi_modes+1)))
        fields.append(record);history.append(dict(region=kind,old_sampled_metric=region.old_max,
            fit_iterations=iterations,actual_saved_field_sampled_linear_residual=actual_screen,
            native_domain=[float(knots[0]),float(knots[-1])],fixed_nodal_jet_count=int(np.sum(fixed))))
        print(json.dumps(dict(stage='actual_saved_'+kind,**actual_screen,seconds=time.monotonic()-started)),flush=True)
    report=dict(schema='fd2d-c2-material-field-candidate-production-v1',status='ACTUAL_C2_FIELD_DEFINED__METRIC_UNVERIFIED',
        scope=__doc__,script=producer,sampler=screen.identity(HERE/'fd2d-metric-noncircle-gauge-screen.py'),
        geometry=screen.identity(args.geometry),target=screen.identity(args.target),tail=screen.identity(args.tail),
        tail_packet=screen.identity(args.tail_packet),fields=fields,regions=history,arguments=vars(args)|{'out_dir':str(args.out_dir)},
        native_shared_two_jets=True,finite_periodic_angular_series=True,
        mirror_coefficient_identities_enforced=True,zero_field_near_cut_enforced=True,
        zero_field_near_cuff_enforced=True,field_material_C2_requires_original_chart_C2=True,
        inverse_material_map_certified=False,continuous_linear_residual_certified=False,
        nonlinear_metric_certified=False,README_complete=False,seconds=time.monotonic()-started)
    report['arguments']={k:str(v) if isinstance(v,Path) else v for k,v in report['arguments'].items()}
    out=args.out_dir/'production.json';out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(out),regions=history,status=report['status'])),flush=True)


if __name__=='__main__':main()
