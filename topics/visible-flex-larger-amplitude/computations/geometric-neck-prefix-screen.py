#!/usr/bin/env python3
"""Cylindrical and nonlocal image screen of an actual saved finite neck prefix.

Restores every coefficient chunk through SavedPrefix and retains its mean
height antiderivative and derivatives. Uses the exact recorded finite metric
provider, not a surface of revolution substituted for the saved map. All
extrema, point-cloud Hausdorff distances and pair searches are numerical
diagnostics on a double-mirror annulus with boundary, not certificates of
continuous embedding, a complete cap, or reach.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import cKDTree
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj;spec.loader.exec_module(obj)
    return obj


pb=module('geometric_neck_pullback',HERE/'geometric-checkpoint-core-pullback.py')
curv=module('geometric_neck_curvature',HERE/'alternative-neck-curvature-map.py')


def merged(*arrays):
    x=np.sort(np.concatenate([np.ravel(a)for a in arrays]));tol=64*np.finfo(float).eps*max(1.,abs(x).max())
    out=[x[0]]
    for y in x[1:]:
        if y-out[-1]>tol:out.append(y)
    return np.asarray(out)


def indices(values,grid):
    hi=np.minimum(np.searchsorted(grid,values),len(grid)-1);lo=np.maximum(hi-1,0)
    ans=np.where(abs(grid[lo]-values)<abs(grid[hi]-values),lo,hi)
    if np.max(abs(grid[ans]-values))>2e-12*max(1.,grid[-1]):raise ValueError('Lost requested radial samples')
    return np.unique(ans)


def segment_table(f):
    pre=f._alternative_neck;rows=[]
    for seg in pre.segments:
        rows.append(dict(index=len(rows),label=curv.label(seg,pre.loop_begin),kind=seg['kind'],lo=seg['s0'],hi=seg['s1']))
    for seg in f.bridge.segments:
        rows.append(dict(index=len(rows),label=curv.label(seg,pre.loop_begin,True),kind=seg['kind'],lo=pre.end+seg['s0'],hi=pre.end+seg['s1']))
    return rows


def segment_at(segments,s):
    return next((row for row in segments if row['lo']-2e-12<=abs(s)<=row['hi']+2e-12),segments[-1])


def extreme(value,s,psi,position,minimum):
    i,j=np.unravel_index(int(np.argmin(value)if minimum else np.argmax(value)),value.shape)
    return dict(value=float(value[i,j]),s=float(s[i]),psi=float(psi[j]),point=position[i,j].tolist())


def geometry_screen(saved,args):
    started=time.time();f=saved.flow;segments=segment_table(f)
    breaks=merged(f.breaks,[0.,f.end],[v for row in segments for v in (row['lo'],row['hi'])])
    coarse=np.linspace(0.,f.end,args.radial)
    phase_s=merged(np.linspace(0.,f.end,args.phase_radial),breaks)
    pair_s=merged(np.linspace(0.,f.end,args.pair_radial),breaks)
    fractions=np.array([.5,(3-np.sqrt(3))/6,(3+np.sqrt(3))/6])
    inside=(saved.sol.x[:-1,None]+np.diff(saved.sol.x)[:,None]*fractions).ravel()
    ss=merged(coarse,saved.sol.x,inside,breaks,phase_s,pair_s)
    ss[0]=0.;ss[-1]=f.end
    phase_idx=indices(phase_s,ss);pair_idx=indices(pair_s,ss)
    phase_s=ss[phase_idx];pair_s=ss[pair_idx]
    phase_lookup={int(i):j for j,i in enumerate(phase_idx)};pair_lookup={int(i):j for j,i in enumerate(pair_idx)}
    if args.angular%args.pair_angular:raise ValueError('Pair angular count must divide dense angular count')
    stride=args.angular//args.pair_angular
    phase_points=np.empty((len(phase_idx),args.angular,3));pair_points=np.empty((len(pair_idx),args.pair_angular,3));pair_normals=pair_points.copy()
    psi=2*np.pi*np.arange(args.angular)/args.angular;beta_grid=2*np.pi*np.arange(256)/256
    height=saved.height_jets(ss,args.height_angular,6)
    print(json.dumps(dict(event='height_restored',radial=len(ss),height_angular=args.height_angular,seconds=time.time()-started)),flush=True)
    lo={k:None for k in ('R','beta_psi','beta_theta','J_psi','J_theta','z_s_at_fixed_beta','star_support')}
    hi={k:None for k in ('kappa','metric','ball_radius')};zbeta=0.;wlo=math.inf;whi=-math.inf;bstep=0.;angle_monotone=True
    heights=np.empty((len(ss),len(beta_grid)));segment_best={}
    for first in range(0,len(ss),16):
        sl=slice(first,first+16);s=ss[sl];eta=np.broadcast_to(psi,(len(s),len(psi)))
        jet=saved.jets(s,eta,tuple(h[sl]for h in height));X=jet['pos'];A=jet['s1'];B=jet['p1'];ang=saved.angle(s,eta)
        R=np.linalg.norm(X[:,:,:2],axis=2);beta=np.arctan2(X[:,:,1],X[:,:,0])
        bs=(X[:,:,0]*A[:,:,1]-X[:,:,1]*A[:,:,0])/R**2
        bp=(X[:,:,0]*B[:,:,1]-X[:,:,1]*B[:,:,0])/R**2
        J=bp*A[:,:,2]-bs*B[:,:,2];normal=np.cross(B,A);normal/=np.linalg.norm(normal,axis=2)[:,:,None]
        kap=curv.principal(A,B,jet['s2'],jet['sp'],jet['p2'])[0]
        physical_A=A-(ang['theta_s']/ang['rho'])[:,:,None]*B;physical_B=B/ang['rho'][:,:,None]
        aa=f.profile(s)[0][:,None];E=np.sum(physical_A**2,axis=2);F=np.sum(physical_A*physical_B,axis=2);G=np.sum(physical_B**2,axis=2)
        metric=np.maximum.reduce((abs(E-1),abs(F)/aa,abs(G/aa**2-1)))
        values=dict(R=R,beta_psi=bp,beta_theta=bp/ang['rho'],J_psi=J,J_theta=J/ang['rho'],z_s_at_fixed_beta=J/bp,
                    star_support=np.sum(X*normal,axis=2),kappa=kap,metric=metric,ball_radius=np.linalg.norm(X,axis=2))
        for key in lo:
            r=extreme(values[key],s,psi,X,True)
            if lo[key]is None or r['value']<lo[key]['value']:lo[key]=r
        for key in hi:
            r=extreme(values[key],s,psi,X,False)
            if hi[key]is None or r['value']>hi[key]['value']:hi[key]=r
        zbeta=max(zbeta,float(np.max(abs(B[:,:,2]/bp))))
        for j,sv in enumerate(s):
            seg=segment_at(segments,float(sv));k=int(np.argmax(kap[j]));row=dict(segment=seg['index'],label=seg['label'],s=float(sv),psi=float(psi[k]),kappa=float(kap[j,k]),point=X[j,k].tolist())
            if seg['index']not in segment_best or row['kappa']>segment_best[seg['index']]['kappa']:segment_best[seg['index']]=row
            i=first+j
            if i in phase_lookup:phase_points[phase_lookup[i]]=X[j]
            if i in pair_lookup:pair_points[pair_lookup[i]]=X[j,::stride];pair_normals[pair_lookup[i]]=normal[j,::stride]
            db=np.angle(np.exp(1j*(np.roll(beta[j],-1)-beta[j])));w=float(db.sum()/(2*np.pi));wlo=min(wlo,w);whi=max(whi,w);bstep=max(bstep,float(abs(db).max()))
            lift=np.r_[beta[j,0],beta[j,0]+np.cumsum(db)]
            if np.any(np.diff(lift)<=0):angle_monotone=False;heights[i]=np.nan
            else:
                target=lift[0]+np.mod(beta_grid-lift[0],2*np.pi);heights[i]=np.interp(target,lift,np.r_[X[j,:,2],X[j,0,2]])
    dz=np.diff(heights,axis=0)/np.diff(ss)[:,None]
    report=dict(radial_samples=len(ss),angular_samples=args.angular,minimum_radial_spacing=float(np.diff(ss).min()),height_angular=args.height_angular,height_quadrature_order=6,
        interior_interval_fractions=fractions.tolist(),
        minima=lo,maxima=hi,winding_min=wlo,winding_max=whi,maximum_cyclic_beta_step=bstep,all_sampled_angles_strictly_increasing=angle_monotone,
        fixed_beta_count=len(beta_grid),fixed_beta_height_difference_quotient_min=float(np.nanmin(dz)),fixed_beta_nonpositive_step_count=int(np.sum(dz<=0)),
        top_height_min=float(np.nanmin(heights[-1])),top_height_max=float(np.nanmax(heights[-1])),top_bottom_height_gap_min=float(2*np.nanmin(heights[-1])),maximum_abs_z_beta=zbeta,
        diameter_dense_sample=2*hi['ball_radius']['value'],segment_curvature_samples=list(segment_best.values()),seconds=time.time()-started)
    for key in ('minima','maxima'):
        for row in report[key].values():row['segment']=segment_at(segments,row['s'])['label']
    if lo['R']['value']>0 and lo['z_s_at_fixed_beta']['value']>0:
        r=lo['R']['value'];m=lo['z_s_at_fixed_beta']['value']
        report['conditional_inverse_Lipschitz_C']=float(np.linalg.norm([[1/m,math.pi*zbeta/(2*m*r)],[0,math.pi/2]],2))
    return report,segments,(phase_s,phase_points),(pair_s,pair_points,pair_normals)


def curvature_polish(saved,segments,rows,angular,top=3):
    f=saved.flow;_,B1,B2=f.basis(angular);answer=[]
    def value(x):
        s=np.array([float(x[0])]);eta=np.array([[float(x[1])]]);Y=saved.sol.sol(s);Yp=saved.sol.sol(s,1)
        fr,_,dW=f.velocity_s(s,Y,Yp,B1,B2);hp=np.mean(fr['V'][:,:,2],axis=1);hpp=np.mean(dW[:,:,2],axis=1)
        j=saved.jets(s,eta,(np.zeros(1),hp,hpp))
        vals=curv.principal(j['s1'],j['p1'],j['s2'],j['sp'],j['p2'])
        return np.array([float(v[0,0])for v in vals])
    for row in sorted(rows,key=lambda x:-x['kappa'])[:top]:
        row=dict(row);seg=segments[row['segment']];x=np.array([row['s'],row['psi']]);half=max((seg['hi']-seg['lo'])/10,2e-5)
        bounds=[(max(seg['lo'],x[0]-half),min(seg['hi'],x[0]+half)),(x[1]-.08,x[1]+.08)]
        result=minimize(lambda y:-value(y)[0],x,method='Nelder-Mead',bounds=bounds,options=dict(xatol=2e-10,fatol=2e-10,maxiter=180))
        if -result.fun>row['kappa']:row.update(s=float(result.x[0]),psi=float(result.x[1]),kappa=float(-result.fun))
        vals=value([row['s'],row['psi']]);row.update(principal_signed=vals[1:3].tolist(),meridian_normal_curvature=float(vals[3]),mixed_normal_curvature=float(vals[4]),latitude_normal_curvature=float(vals[5]),optimization_success=bool(result.success))
        aa,v,acc=f.profile([row['s']]);row.update(a=float(aa[0]),ap=float(v[0]),app=float(acc[0]),background_meridian_curvature=float(abs(acc[0])/math.sqrt(1-v[0]**2)))
        answer.append(row)
    answer.sort(key=lambda x:-x['kappa'])
    s=np.array([row['s']for row in answer]);h=saved.height_jets(s,angular=angular);eta=np.array([[row['psi']]for row in answer]);j=saved.jets(s,eta,h)
    for i,row in enumerate(answer):row['point']=j['pos'][i,0].tolist()
    return answer


def mirrored(s,X,normal=None):
    lower=X[:0:-1].copy();lower[:,:,2]*=-1;points=np.concatenate((lower,X));signed_s=np.r_[-s[:0:-1],s]
    if normal is None:return signed_s,points
    lower_n=normal[:0:-1].copy();lower_n[:,:,2]*=-1
    return signed_s,points,np.concatenate((lower_n,normal))


def phase_screen(saved,data,phases,D):
    start=time.time();s,upper=data;S,cloud3=mirrored(s,upper);cloud=cloud3.reshape(-1,3);tree=cKDTree(cloud);rows=[]
    for phase in np.linspace(0,math.pi/2,phases+1)[1:]:
        c=math.cos(phase);sn=math.sin(phase);R=np.array([[c,-sn,0.],[sn,c,0.],[0.,0.,1.]]);turned=cloud@R.T
        forward,ind=tree.query(turned,workers=1);backward,ib=cKDTree(turned).query(cloud,workers=1);i=int(np.argmax(forward));j=int(np.argmax(backward));distance=float(max(forward[i],backward[j]))
        rows.append(dict(phase=float(phase),hausdorff_point_cloud=distance,held_over_dense_D_sample=distance/D,forward=float(forward[i]),backward=float(backward[j]),
            forward_witness=turned[i].tolist(),forward_nearest=cloud[ind[i]].tolist(),backward_witness=cloud[j].tolist(),backward_nearest=turned[ib[j]].tolist()))
    core=np.asarray(saved.rec['core']['coefficients']);witness=np.array([0.,1+core.sum(),0.]);d,idx=tree.query(witness)
    return dict(radial_samples_per_half=len(s),angular=len(upper[0]),points=len(cloud),diameter_this_cloud=2*float(np.linalg.norm(cloud,axis=1).max()),
        rows=rows,best=max(rows,key=lambda x:x['hausdorff_point_cloud']),core_axis_witness=dict(point=witness.tolist(),distance_point_cloud=float(d),nearest=cloud[idx].tolist()),seconds=time.time()-start)


def near_pair_screen(data,segments,r0,D,query_radial=65,query_angular=32):
    start=time.time();s,upper,normal=data;S0,X0,N0=mirrored(s,upper,normal);Nang=len(upper[0]);X=X0.reshape(-1,3);normal=N0.reshape(-1,3)
    S=np.repeat(S0,Nang);psi=np.tile(2*np.pi*np.arange(Nang)/Nang,len(S0));beta=np.arctan2(X[:,1],X[:,0]);tree=cKDTree(X)
    segment_ids=np.repeat([segment_at(segments,si)['index']for si in S0],Nang)
    is_loop=np.repeat([segment_at(segments,si)['label'].startswith('loop ')for si in S0],Nang)
    rows=np.unique(np.round(np.linspace(0,len(S0)-1,query_radial)).astype(int));angles=np.unique(np.round(np.arange(query_angular)*Nang/query_angular).astype(int)%Nang)
    query=np.array([i*Nang+j for i in rows for j in angles]);radius=.06*D;thresholds=[0.,.1,.25,.5];best_q={str(v):None for v in thresholds};best_d={str(v):None for v in thresholds};counts={str(v):0 for v in thresholds};violations=0
    groups={key:dict(pair_count=0,minimum_quotient=None,minimum_distance=None)for key in ('loop_involved','loop_involved_d0_ge_025','loop_nonadjacent_pieces_d0_ge_025')}
    def record(i,j,d,d0,Q):
        def point(k):return dict(s=float(S[k]),psi=float(psi[k]),beta=float(beta[k]),point=X[k].tolist(),segment=segment_at(segments,S[k])['label'])
        return dict(distance=float(d),product_separation=float(d0),minimum_ordered_normal_chord_quotient=float(Q),first=point(i),second=point(j))
    for done,ii in enumerate(query):
        ids=np.asarray(tree.query_ball_point(X[ii],radius),int);delta=X[ids]-X[ii];dd=np.sum(delta*delta,axis=1)
        db=abs((beta[ids]-beta[ii]+np.pi)%(2*np.pi)-np.pi);d0=np.sqrt((S[ids]-S[ii])**2+(r0*db)**2)
        den=2*np.maximum(abs(delta@normal[ii]),abs(np.sum(delta*normal[ids],axis=1)));Q=np.divide(dd,den,out=np.full_like(dd,np.inf),where=den>1e-18)
        nonzero=dd>1e-16;violations+=int(np.sum(nonzero&(Q<.03*D)))
        for eta in thresholds:
            mask=nonzero&(d0>=eta);counts[str(eta)]+=int(np.sum(mask))
            if not np.any(mask):continue
            allowed=np.flatnonzero(mask);kq=int(allowed[np.argmin(Q[mask])]);kd=int(allowed[np.argmin(dd[mask])])
            if best_q[str(eta)]is None or Q[kq]<best_q[str(eta)]['minimum_ordered_normal_chord_quotient']:best_q[str(eta)]=record(ii,int(ids[kq]),math.sqrt(dd[kq]),d0[kq],Q[kq])
            if best_d[str(eta)]is None or dd[kd]<best_d[str(eta)]['distance']**2:best_d[str(eta)]=record(ii,int(ids[kd]),math.sqrt(dd[kd]),d0[kd],Q[kd])
        loop=nonzero&(is_loop[ii]|is_loop[ids]);masks=(loop,loop&(d0>=.25),loop&(d0>=.25)&(abs(segment_ids[ii]-segment_ids[ids])>=2))
        for group,mask in zip(groups.values(),masks):
            group['pair_count']+=int(np.sum(mask))
            if not np.any(mask):continue
            allowed=np.flatnonzero(mask);kq=int(allowed[np.argmin(Q[mask])]);kd=int(allowed[np.argmin(dd[mask])])
            if group['minimum_quotient']is None or Q[kq]<group['minimum_quotient']['minimum_ordered_normal_chord_quotient']:
                group['minimum_quotient']=record(ii,int(ids[kq]),math.sqrt(dd[kq]),d0[kq],Q[kq])
            if group['minimum_distance']is None or dd[kd]<group['minimum_distance']['distance']**2:
                group['minimum_distance']=record(ii,int(ids[kd]),math.sqrt(dd[kd]),d0[kd],Q[kd])
        if done and done%512==0:print(json.dumps(dict(event='near_pairs',done=done,total=len(query))),flush=True)
    return dict(target_points=len(X),source_queries=len(query),target_signed_radial=len(S0),target_angular=Nang,query_radial=len(rows),query_angular=len(angles),
        target_radius=.03*D,chord_search_radius=radius,counts=counts,normal_chord_quotient_below_target_count=violations,minima_quotient=best_q,minima_distance=best_d,
        loop_groups=groups,
        seconds=time.time()-start,scope='All finite target points within the stated chord radius of the selected source subset. A null entry means no such pair, not a continuum exclusion. Ordinary normals do not cover the annulus boundary normal cone.')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('input','source-topic','port','out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--angular',type=int,default=512);p.add_argument('--radial',type=int,default=801);p.add_argument('--height-angular',type=int,default=512)
    p.add_argument('--phase-radial',type=int,default=401);p.add_argument('--phases',type=int,default=8)
    p.add_argument('--pair-radial',type=int,default=181);p.add_argument('--pair-angular',type=int,default=128);p.add_argument('--skip-pairs',action='store_true')
    p.add_argument('--equivalent-default-angle-hook',action='store_true',help='Allow only the recorded inert angle hook for an old cubic profile, with exact old-source and helper hash checks')
    args=p.parse_args();start=time.time();saved,_=pb.load_saved(args.input,args.source_topic,args.port,angular=args.height_angular)
    if not saved.rec['solver_success']:raise ValueError('Checkpoint did not solve successfully')
    if saved.mode!=2:raise ValueError('This diameter identity uses the saved m2 central symmetry')
    if saved.rec['frozen_profile'].get('ramp_law')!='hermite_boost_neck':raise ValueError('Not a complete saved neck profile')
    port_hash=hashlib.sha256(args.port.read_bytes()).hexdigest()
    if port_hash!=saved.rec['physical_port_sha256']:raise ValueError('Requested port bytes differ from recorded physical port')
    checks={}
    for name,expected in saved.rec.get('interface_hashes',{}).items():
        if name=='root_dual_core_bvp.py':continue
        path=HERE/name;actual=hashlib.sha256(path.read_bytes()).hexdigest();checks[name]=dict(expected=expected,current=actual,match=actual==expected)
        if actual!=expected and name=='alternative-neck-provider.py' and args.equivalent_default_angle_hook:
            if saved.rec['frozen_profile'].get('boost_law','cubic')!='cubic':
                raise ValueError('Default-hook equivalence is only for the unchanged cubic profile')
            source=path.read_text();begin=source.index('# Optional local design extension.');end=source.index("if __name__=='__main__':main()",begin)
            stripped=hashlib.sha256((source[:begin]+source[end:]).encode()).hexdigest()
            helper=hashlib.sha256((HERE/'strong_angle_boost.py').read_bytes()).hexdigest()
            known='ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be'
            if stripped!=expected or helper!=known:
                raise ValueError('Unrecognized provider or helper change; equivalence not established')
            checks[name].update(match=True,exact_old_source_without_hook_sha256=stripped,helper_sha256=helper,
                equivalence='Recorded helper delegates cubic profile arithmetic to the exact old provider; default segments, jets, knots and height were separately checked in 2026-11-12-strong-angle-provider-check.json.')
    if not all(row['match']for row in checks.values()):raise ValueError('Saved finite-map interface source changed: '+json.dumps(checks))
    result=dict(scope=__doc__,input=str(args.input),input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),coefficient_chunks=saved.rec.get('pp_coefficient_chunks'),
        source_revision=saved.rec.get('source_git_head'),source_topic=str(args.source_topic),physical_port_sha256=port_hash,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        pullback_sha256=hashlib.sha256((HERE/'geometric-checkpoint-core-pullback.py').read_bytes()).hexdigest(),interface_hash_checks=checks,
        frozen_profile=saved.rec['frozen_profile'],modes=saved.M,gauge=saved.q,meridian_length=saved.flow.end,actual_core=saved.rec['core'])
    result['cylindrical'],result['segments'],phase,pairs=geometry_screen(saved,args);args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='cylindrical',result=result['cylindrical'])),flush=True)
    result['curvature_polished']=curvature_polish(saved,result['segments'],result['cylindrical']['segment_curvature_samples'],args.height_angular)
    D=result['cylindrical']['diameter_dense_sample'];result['curvature_radius_over_D']=1/(D*result['curvature_polished'][0]['kappa'])
    args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(event='curvature',top=result['curvature_polished'][0],radius_over_D=result['curvature_radius_over_D'])),flush=True)
    result['phase_images']=phase_screen(saved,phase,args.phases,D);args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='phase_images',best=result['phase_images']['best'])),flush=True)
    if not args.skip_pairs:result['near_pairs']=near_pair_screen(pairs,result['segments'],result['cylindrical']['minima']['R']['value'],D)
    result['seconds']=time.time()-start;result['caveats']=['No continuous-domain or interpolation-error enclosure.','Finite linear-tail-DN prefix only; no actual tail or cap is added.','The double-mirror annulus has two boundary circles.','Point-cloud Hausdorff, diameter and normal-chord quotients are samples, not certified continuous bounds.']
    args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(event='complete',seconds=result['seconds'],near_pairs=result.get('near_pairs'))),flush=True)


if __name__=='__main__':main()
