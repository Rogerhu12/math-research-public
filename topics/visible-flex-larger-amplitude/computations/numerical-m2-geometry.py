#!/usr/bin/env python3
"""Sample the actual saved mode-two prefix and its reflected image.

No tail/cap closure is added. Finite point-cloud Hausdorff values are only
screening numbers, with no continuous covering-error certificate. The
reported centred diameter is an exact identity for a centrally symmetric
compact set, evaluated here on the sampled reflected prefix only.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
from types import SimpleNamespace
sys.dont_write_bytecode=True
import numpy as np
from scipy.interpolate import PPoly
from scipy.spatial import cKDTree


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','checkpoint','port','out'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--radial',type=int,default=301);p.add_argument('--angular',type=int,default=512)
    p.add_argument('--phases',type=int,default=9)
    a=p.parse_args();start=time.time()
    file=Path(__file__).with_name('numerical-m2-prefix.py')
    spec=importlib.util.spec_from_file_location('numerical_mode2_wrapper',file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    ad=m.load(a.source_topic)
    from curve_stable_prefix_bvp import load_checkpoint
    rec=load_checkpoint(a.checkpoint)
    port=json.loads(a.port.read_text());_,BVP=ad.build_classes(rec['chart'])
    obj=BVP(rec['frozen_profile'],port,rec['gauge_amplitude'],rec['config']['modes'],max(128,a.angular),True,rec['warp_reference_q'])
    par=np.array(rec['parameters']);par[0]=math.log(rec['actual_primary_amplitude']/obj.q)
    obj.initial(par);flow=obj.flow(par[0]);x=np.array(rec['mesh']);pp=PPoly.construct_fast(np.array(rec['pp_coefficients']),x,extrapolate=True,axis=1)
    sol=SimpleNamespace(x=x,y=pp(x),p=par,sol=pp)
    s=np.unique(np.r_[np.linspace(0,flow.end,a.radial),flow.breaks])
    heights=flow.height_integral(sol,s,a.angular,6);B,B1,B2=flow.basis(a.angular)
    clouds=[];maxk=0.;minmargin=1.;margin_at=None;minsupport=math.inf;maxnorm=0.;max_at=None;metric=0.
    witness=np.array([0.,obj._core.summary()['radius_max_sample'],0.]);near=math.inf;nearwhere=None
    for first in range(0,len(s),32):
        ss=s[first:first+32];Y=pp(ss);Yp=pp(ss,1);Ypp=pp(ss,2);fr,Fsp,dW=flow.velocity_s(ss,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']
        pos=g['pos']+obj.q*flow.values(Y,B);pos[:,:,2]+=heights[first:first+len(ss),None]
        Fc=g['s1']+obj.q*flow.values(Yp,B);Fc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fcc=g['s2']+obj.q*flow.values(Ypp,B);Fcc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
        Fs=Fc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
        Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
        Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
        Fss=Fcc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
        nn=np.cross(Ft,Fs);nn/=np.linalg.norm(nn,axis=2)[:,:,None]
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        L=np.sum(Fss*nn,axis=2);M=np.sum(Fst*nn,axis=2);N=np.sum(Ftt*nn,axis=2)
        det=E*G-F*F;tr=(L*G-2*M*F+N*E)/det;det2=(L*N-M*M)/det
        kap=(abs(tr)+np.sqrt(np.maximum(0.,tr*tr-4*det2)))/2
        aa=flow.profile(ss)[0][:,None]
        metric=max(metric,float(np.max(abs(E-1))),float(np.max(abs(F/aa))),float(np.max(abs(G/aa**2-1))))
        maxk=max(maxk,float(kap.max()))
        if fr['margin'].min()<minmargin:
            minmargin=float(fr['margin'].min());mi=np.unravel_index(np.argmin(fr['margin']),fr['margin'].shape)
            margin_at={'s':float(ss[mi[0]]),'psi':float(2*np.pi*mi[1]/a.angular),'a':float(fr['a'][mi[0]]),'ap':float(fr['ap'][mi[0]]),'curve_curvature':float(fr['kap'][mi]),'xyz':pos[mi].tolist()}
        minsupport=min(minsupport,float(np.sum(pos*nn,axis=2).min()))
        norms=np.linalg.norm(pos,axis=2);ii=np.unravel_index(np.argmax(norms),norms.shape)
        if norms[ii]>maxnorm:maxnorm=float(norms[ii]);max_at={'s':float(ss[ii[0]]),'psi':2*np.pi*ii[1]/a.angular,'xyz':pos[ii].tolist()}
        dist=np.linalg.norm(pos-witness,axis=2);ii=np.unravel_index(np.argmin(dist),dist.shape)
        if dist[ii]<near:near=float(dist[ii]);nearwhere={'s':float(ss[ii[0]]),'psi':2*np.pi*ii[1]/a.angular,'xyz':pos[ii].tolist()}
        clouds.append(pos.reshape(-1,3))
    up=np.concatenate(clouds);down=up.copy();down[:,2]*=-1;points=np.r_[up,down];tree=cKDTree(points)
    rows=[]
    for alpha in np.linspace(0,np.pi/2,a.phases):
        c,si=math.cos(alpha),math.sin(alpha);rot=points.copy();rot[:,0]=c*points[:,0]-si*points[:,1];rot[:,1]=si*points[:,0]+c*points[:,1]
        other=cKDTree(rot);to_base,ib=tree.query(rot,workers=1);to_rot,ir=other.query(points,workers=1);d=float(max(to_base.max(),to_rot.max()))
        if to_base.max()>=to_rot.max():
            iw=int(np.argmax(to_base));witness_at={'direction':'rotated to base','point':rot[iw].tolist(),'nearest':points[ib[iw]].tolist(),'s':float(s[(iw%(len(s)*a.angular))//a.angular]),'psi':float(2*np.pi*(iw%a.angular)/a.angular)}
        else:
            iw=int(np.argmax(to_rot));witness_at={'direction':'base to rotated','point':points[iw].tolist(),'nearest':rot[ir[iw]].tolist(),'s':float(s[(iw%(len(s)*a.angular))//a.angular]),'psi':float(2*np.pi*(iw%a.angular)/a.angular)}
        row={'angle':float(alpha),'point_cloud_Hausdorff':d,'prefix_only_ratio':d/(2*maxnorm),'maximum_witness_sample':witness_at};rows.append(row);print(json.dumps(row),flush=True)
    report=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),solver_success=rec['solver_success'],profile=rec['frozen_profile'],q=rec['actual_primary_amplitude'],modes=obj.M,
        samples=dict(radial=len(s),angular=a.angular,phases=a.phases),D_reflected_prefix_sample=2*maxnorm,max_norm_at=max_at,max_principal_curvature_sample=maxk,
        curvature_radius_to_prefix_D=1/(2*maxnorm*maxk),minimum_Frenet_margin=minmargin,minimum_Frenet_margin_location=margin_at,minimum_outward_support_sample=minsupport,
        prefix_metric_sample=metric,core=obj._core.summary(),inward_core_witness_distance_to_prefix_sample=float(tree.query(np.array([obj._core.summary()['radius_min_sample'],0.,0.]))[0]),rotated_core_witness_distance_to_prefix_sample=near,witness_nearest_sample=nearwhere,phase_rows=rows,
        seconds=time.time()-start,source_transforms=m.TRANSFORMS)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k in ['D_reflected_prefix_sample','max_principal_curvature_sample','curvature_radius_to_prefix_D','minimum_Frenet_margin','minimum_outward_support_sample','rotated_core_witness_distance_to_prefix_sample','seconds']}),flush=True)

if __name__=='__main__':main()
