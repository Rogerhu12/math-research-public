#!/usr/bin/env python3
"""Measure and fit two complete R777 physical poses with both retained and independently restored caps."""
import argparse
from hashlib import sha256
import os
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.optimize import least_squares
import r777_bent_complete_caps_and_true_terminal_collars as geom
import r777_cartesian_original_cap_metric_restoration as cap
import solve_r774_shared_pose_complete_spheres as parent
from r742_tilted_disk_two_jets import J

prior=parent.prior;old,m,base=geom.old,geom.m,geom.base
E,L,B,T=geom.E,geom.L,geom.B,geom.T
PHASES,LEVELS=prior.PHASES,prior.LEVELS
BRANCHES=("pair-retained","balanced-retained","pair-restored","balanced-restored")

def axes(level,ph,audit):
    out=[]
    for name,(s,v) in zip(prior.CHARTS,parent.axes(level,ph,audit)):
        if name.startswith("round"):
            h=geom.EDGE;add=[L-.12,L-.10,L-.095,L-.001,L-h,L-h/2,L-.000075,L]
        elif name.startswith("cap-normal"):
            add=list(np.linspace(0,old.WIDTH,15 if audit else 8))
        elif name in ("cap+","cap-"):
            add=list(.82*(1-old.JOIN)*np.sqrt(1+np.linspace(-.04,.04,25 if audit else 13)))
        else:
            out.append((s,v));continue
        out.append(np.meshgrid(s[:,0],np.unique(np.r_[v[0],add]),indexing="ij"))
    return out

def configure(mode,free,index,corrections):
    shape=cap.LEVELS[index][:2]
    def jet(ch,a,b,ph,order,unused,rotate=False):
        z=corrections.get(float(ph))
        if free and z is not None:
            f=cap.weighted_jet(ch,a,b,ph,order,mode,shape,z)
        else:f=geom.chart_jet(ch,a,b,ph,order,mode,False)
        if rotate:
            ax=np.asarray(m.axis(order));p=f[...,:,[0,2]].copy();p[...,0,:]-=ax
            p=geom.c.oldgeom.parent.rot(p,ph);p[...,0,:]+=ax
            f[...,0]=p[...,0];f[...,2]=p[...,1]
        return f
    prior.geom=SimpleNamespace(chart_jet=jet,gate=lambda kind,s,v,o:geom.gate(kind,s,v,o,free))
    prior.axes=axes

def prices(level,ph,mode):
    order=level[2];h=old.material(order,True)[-1];grid=geom.c.stations(order)
    n=(128,256,512)[LEVELS.index(level)]
    s=np.unique(np.r_[grid,2*h-grid,np.arange(n+1)*2*h/n])
    last=geom.chart_jet("cap-normal+",s,np.zeros_like(s),ph,order,mode)
    first=geom.chart_jet("cylinder",s,np.full_like(s,B),ph,order,mode)
    gap=np.linalg.norm(last[:,0]-first[:,0],axis=1)-T
    p=geom.pose(order,ph,mode)
    co,si,Yl,C,b,tx,tz,span,dx,zl,zr,Zl,Zr,Xr,Zc=p[:15]
    lr=np.hypot(1+C,np.hypot(b,.71-Zl))-np.hypot(1.30,T)
    rr=np.hypot(Xr-C-span,np.hypot(b,Zc-Zr))-T
    oldbound=T+np.hypot(1.30,T)-1.30
    qr=old.data(np.asarray([geom.wall_label(order)]),0.,order,True)[0][0,0]
    db=m.terminal(order)[1]
    rows={"common_pose":p,"true_section_closure":geom.c.state(order,ph)[-1],
          "old_rigid_centroid_excess":Xr-qr+db-oldbound,
          "new_same_centroid_excess":Xr-qr+db-oldbound-(span-dx),
          "paired_actual_diagonal_and_meridian_excess":[lr,rr],
          "cap_pair_material_z_old":[zl,zr],"critical_span_before_after_gain":[dx,span,span-dx],
          "all_sampled_meridian_max_gap":[float(np.max(gap)),float(s[np.argmax(gap)])],
          "signed_rim_min_y":[float(np.min(last[:,0,1])),float(s[np.argmin(last[:,0,1])])],"seams":{}}
    for side,sg in ((1,"+"),(-1,"-")):
        vv=np.zeros_like(s);pick=lambda name,b:geom.chart_jet(name,s,b,ph,order,mode,False)
        central=pick("cylinder",vv+side*B);central[:,2]*=side;central[:,4]*=side
        rows["seams"][sg]=[np.max(abs(a-b),axis=(0,2)).tolist() for a,b in
             ((central,pick("preband"+sg,vv)),(pick("preband"+sg,vv+E),pick("round"+sg,vv)),
              (pick("round"+sg,vv+L),pick("cap-normal"+sg,vv)))]
    return rows

def cross_probes(level,ph,mode,field):
    idx=LEVELS.index(level);nt=(24,36,48)[idx];nr=(3,4,5)[idx];order=level[2]
    half=old.material(order,True)[-1];s=(np.arange(nt)+.375)*2*half/nt
    def points(chart,radii):
        x,y=np.meshgrid(s,np.asarray(radii),indexing="ij");uv=np.column_stack((x.ravel(),y.ravel()))
        f=field(chart,uv[:,0],uv[:,1]);n=np.cross(f[:,1],f[:,2]);area=np.linalg.norm(n,axis=1)
        n/=np.maximum(area,1e-300)[:,None]
        return chart,uv,f[:,0],n
    central=points("cylinder",np.unique(np.r_[np.linspace(-B,B,2*nr+1),-.33,.33]))
    caps=[];sleeves=[]
    for sign in ("+","-"):
        caps.append(points("cap"+sign,np.unique(np.r_[np.linspace(.05,.95,nr+2),.82*(1-old.JOIN),.995,1.])))
        sleeves.append(points("round"+sign,np.unique(np.r_[np.linspace(.005,L-.0003,nr+2),L-geom.EDGE/2])))
    def price(left,right):
        # All pairs in the listed two disjoint material sets, ordered in both directions.
        d=right[2][None,:,:]-left[2][:,None,:];sq=np.einsum("ijk,ijk->ij",d,d)
        nl=abs(np.einsum("ijk,ik->ij",d,left[3]));nn=abs(np.einsum("ijk,jk->ij",d,right[3]))
        den=2*np.maximum(nl,nn);v=np.divide(sq,den,out=np.full_like(sq,np.inf),where=den>0)
        v[sq==0]=0.;i,j=np.unravel_index(np.argmin(v),v.shape)
        return [left[0],right[0],len(left[1])*len(right[1]),float(np.sqrt(sq.min())),
                (float(v[i,j]) if np.isfinite(v[i,j]) else None),left[1][i].tolist(),right[1][j].tolist()]
    return [price(central,q) for q in caps+sleeves]+[price(caps[0],caps[1]),price(sleeves[0],sleeves[1])]+[
        price(q,t) for q in caps for t in sleeves]

def guide(level,ph,mode):
    order=level[2];out={};center=np.array([m.section_center(order),0.,0.])
    witness=base.chart_jet("cylinder",0.,0.,0.,order,.14,False)[0].copy()
    ax=np.asarray(m.axis(order));witness[[0,2]]=geom.c.oldgeom.parent.rot(witness[[0,2]]-ax,-ph)+ax
    held=np.inf
    for name,(ss,vv) in zip(prior.CHARTS,axes(level,ph,True)):
        s,v=ss.ravel(),vv.ravel();side=1 if name.endswith("+") else -1
        sign=1 if name=="cylinder" else side*(-1 if name.startswith("cap") and not name.startswith("cap-normal") else 1)
        rows=[]
        for i in range(0,len(s),384):
            sl=slice(i,i+384);x,y=s[sl],v[sl]
            new=geom.chart_jet(name,x,y,ph,order,mode,False);oldj=base.chart_jet(name,x,y,0.,order,.14,False)
            rows.append(parent.previous_solver.relative(new,oldj,sign,center))
            held=min(held,float(np.min(np.linalg.norm(new[:,0]-witness,axis=1))))
        a=np.asarray(rows);out[name]=[len(s),*a[:,:5].max(axis=0).tolist(),*a[:,5:].min(axis=0).tolist()]
    return {"phase":ph,"all_charts":out,"sampled_held":held,"construction":prices(level,ph,mode),
            "cross_surface_pairs":cross_probes(level,ph,mode,lambda name,s,v:geom.chart_jet(name,s,v,ph,order,mode,False))}

def solve(branch,folder):
    mode,freedom=branch.split("-");free=freedom=="restored";previous={}
    whole=sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])})
    for idx,level in enumerate(LEVELS):
        norms={};configure(mode,free,idx,norms)
        common={"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
                "source_commit":os.environ["R777_SOURCE_COMMIT"],"level":idx,"branch":branch}
        rep={**common,"schema":"R777-original-guide-all-angles-two-cap-pose-v1",
             "rows":[guide(level,ph,mode) for ph in whole],
             "columns":["points","relative_metric_op","abs_11","abs_12","abs_22","max_abs_principal","minimum_support","minimum_area"]}
        print("R777 complete guide",idx,prior.write(folder/f"geometry-{idx}.json",rep),flush=True)
        if free:
            independent=[];seed=None
            for ip,ph in enumerate(PHASES):
                z,r=cap.restore(axes,level,idx,ph,mode,True,seed)
                norms[float(ph)]=z;seed=z
                raw=np.asarray(z,dtype="<f8").tobytes();r["coefficient_bytes_sha256"]=[len(raw),sha256(raw).hexdigest()]
                (folder/f"cap{idx}-phase{ip}.f64").write_bytes(raw);independent.append(r)
            for left,right in zip(PHASES[:-1],PHASES[1:]):
                ph=(left+right)/2;z=(norms[left]+norms[right])/2;norms[ph]=z
                _,r=cap.restore(axes,level,idx,ph,mode,False,z)
                independent.append(r)
            rep={**common,"schema":"R777-three-channel-original-cap-Gram-restoration-v1",
                 "grid":cap.LEVELS[idx],"rows":independent,"chart_columns":["points","orthonormal_operator","index","abs11","abs12","abs22"]}
            print("R777 direct original cap restoration",idx,prior.write(folder/f"cap-{idx}.json",rep),flush=True)
        na,nr=level[3:5];nfev,it=level[5:7];coeff={};rows=[];mid=[]
        for ip,ph in enumerate(PHASES):
            d=prior.Data(level,ph,0.,"fully_free")
            seed=prior.prolong(previous.get(ip),LEVELS[idx-1][3:5] if idx else None,(na,nr))
            if ip>1 and np.linalg.norm(d.fun(coeff[ip-1].ravel()))<np.linalg.norm(d.fun(seed.ravel())):
                seed=coeff[ip-1].copy()
            before=d.result(seed.ravel())
            if ph:
                opt=least_squares(d.fun,seed.ravel(),jac=d.jac,method="trf",tr_solver="lsmr",
                    tr_options={"maxiter":it,"atol":.0002,"btol":.0002},max_nfev=nfev,
                    ftol=1e-9,xtol=1e-9,gtol=1e-9,x_scale=1.)
                x=opt.x.reshape(-1,3);status=[int(opt.status),int(opt.nfev),float(opt.cost),float(opt.optimality)]
            else:
                x=seed;status=[0,0,float(np.linalg.norm(d.fun(x.ravel()))**2/2),0.]
            fit=d.result(x.ravel());del d
            a=prior.Data(level,ph,0.,"fully_free",True);audit=a.result(x.ravel());del a
            raw=np.asarray(x,dtype="<f8").tobytes()
            (folder/f"level{idx}-phase{ip}.f64").write_bytes(raw);coeff[ip]=x
            rows.append({"phase":ph,"seed":before,"fit":fit,"independent":audit,"status":status,
                        "coeff":[len(raw),sha256(raw).hexdigest()],"volumes":prior.volumes(level,idx,ph,0.,"fully_free",x)})
            print("R777 physical whole sphere",mode,free,idx,ph,status,flush=True)
        for j,(l,r) in enumerate(zip(PHASES[:-1],PHASES[1:])):
            ph=(l+r)/2;x=(coeff[j]+coeff[j+1])/2
            a=prior.Data(level,ph,0.,"fully_free",True);res=a.result(x.ravel());del a
            mid.append([ph,res,prior.volumes(level,idx,ph,0.,"fully_free",x)])
        report={"schema":"R777-complete-single-resolution-whole-sphere-physical-fit-v1","mode":mode,
             "cap_free":free,"level":idx,"grid":level,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R777_SOURCE_COMMIT"],"rules_read_commit":os.environ["R777_RULES_COMMIT"],
             "fitted":rows,"intermediate":mid,"fiducial_material":"whole R764 zero-phase 11-chart sphere",
             "chart_columns":["points","nearly_singular","relative_metric_op","max_abs_principal",
             "min_support","min_relative_area","max_abs_frame11","max_abs_frame12","max_abs_frame22"],
             "volume_columns":["uncorrected_signed_flux","fitted_signed_flux"],
             "volume_angular_radial_order":[(48,72,112)[idx],(6,9,12)[idx]]}
        def final_field(name,s,v):
            return prior.field(name,s,v,PHASES[-1],level,0.,"fully_free",coeff[len(PHASES)-1])
        report["last_independent_cross_surface_pairs"]=cross_probes(level,PHASES[-1],mode,final_field)
        meta=prior.write(folder/f"stage-{idx}.json",report);print("R777 complete resolution",idx,meta,flush=True)
        previous=coeff



if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode",choices=BRANCHES,required=True)
    parser.add_argument("--folder",type=Path,required=True)
    args=parser.parse_args();geom.m.old.disk._public();args.folder.mkdir(parents=True,exist_ok=True)
    solve(args.mode,args.folder)
