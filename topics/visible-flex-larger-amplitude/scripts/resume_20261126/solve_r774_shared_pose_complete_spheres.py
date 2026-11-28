#!/usr/bin/env python3
"""R774 true 11-chart guide, general rigid-cap midpoint inequality and full Cartesian refinements."""
from hashlib import sha256
import os
from pathlib import Path
import argparse
from types import SimpleNamespace
import numpy as np
from scipy.optimize import least_squares
import solve_r769_complete_meridian_spheres as previous_solver
import r774_common_left_body_and_complete_caps as geom
from r742_tilted_disk_two_jets import J

prior=previous_solver.prior;base,old,m=geom.base,geom.old,geom.m
E,L,B,T=geom.E,geom.L,geom.B,geom.T
PHASES,LEVELS=prior.PHASES,prior.LEVELS
base_axes=previous_solver.original_axes

def axes(level,ph,audit):
    original=base_axes(level,ph,audit);order=level[2]
    half=old.material(order,True)[-1];s=geom.stations(order)
    if audit:s=np.unique(np.r_[s,(s[:-1]+s[1:])/2])
    out=[]
    for name,(q,v) in zip(prior.CHARTS,original):
        if name.startswith("cap-cartesian"):
            out.append((q,v))
        else:
            a=np.unique(np.r_[q[:,0],s,2*half-s]);a=a[np.r_[True,np.diff(a)>1e-13]]
            out.append(np.meshgrid(a,v[0],indexing="ij"))
    return out

def configure(mode):
    def chart(ch,a,b,ph,order,unused,rotate=False):
        return geom.chart_jet(ch,a,b,ph,order,mode,rotate)
    prior.geom=SimpleNamespace(chart_jet=chart,gate=base.gate);prior.axes=axes

def prices(level,ph,mode):
    order=level[2];half=old.material(order,True)[-1];n=(128,256,512)[LEVELS.index(level)]
    st=geom.stations(order);s=np.unique(np.r_[np.arange(n+1)*2*half/n,st,2*half-st])
    _,_,_,_,_,info=geom.state(order,ph)
    q,t,norm,k,kp=geom.curve(s,ph,order);p0=old.data(s,0.,order,True)[0]
    cap,ret=geom.cap_shift(order,ph,mode);pb,db=m.terminal(order)
    D=geom.target(J(s,s=1.),ph,order,mode,True)
    ss=old.material(order,True)[0]+sum(old.clock_spec(True)[0][1][:2])
    qr=geom.curve(np.array([ss]),ph,order)[0][0]
    qo=old.data(np.array([ss]),0.,order,True)[0][0]
    shift=geom.state(order,ph)[3] if ph else np.zeros(2)
    dx=qr[0]-shift[0]-qo[0]
    tr=geom.BRANCHES[mode][0]*ph/.90
    rec={"wall_amplitudes_loss_requested_recovered_and_closure":info,
        "true_full_section_max_abs_signed_curvature":float(np.max(abs(k))),
        "rigid_chord_registered_guard_max":[[float(v.max()),float(s[np.argmax(v)])] for v in D.T],
        "general_rigid_cap_centroid":[float(ss),float(dx),float(dx+db),float(T+np.hypot(1.30,T)-1.30),
                 float(dx+db-T-np.hypot(1.30,T)+1.30)],
        "flat_diagonal_squared_excess":float(2*1.30*abs(tr)+tr*tr+db*db+(base.axial(order)+pb-ret)**2-T*T),
        "convex_root_and_hessian":[float(np.max(geom.params(s,ph,order,mode)[3][:,0])),
                 float(np.min(geom.params(s,ph,order,mode)[3][:,1]))],
        "seams":{}}
    a=J(s,s=1.);need=geom.target(a,ph,order,mode)[:,:,0]
    roots=geom.params(s,ph,order,mode)[0];u,w=geom.convex.quadrature(order+8);worst=0.
    for i in range(0,len(s),96):
        v=roots[i:i+96];z=np.zeros((len(v),1,2));U=geom.convex.evaluate(v,z,u)[0]
        worst=max(worst,float(np.max(np.linalg.norm(np.einsum("q,nqj->nj",w,U)-need[i:i+96],axis=1))))
    rec["fine_independent_meridian_chord_residual"]=worst
    for side,sg in ((1,"+"),(-1,"-")):
        vv=np.zeros_like(s);pick=lambda name,v:geom.chart_jet(name,s,v,ph,order,mode,False)
        c=pick("cylinder",vv+side*B);c[:,2]*=side;c[:,4]*=side
        rec["seams"][sg]=[np.max(abs(a-b),axis=(0,2)).tolist() for a,b in
              ((c,pick("preband"+sg,vv)),(pick("preband"+sg,vv+E),pick("round"+sg,vv)),
               (pick("round"+sg,vv+L),pick("cap-normal"+sg,vv)))]
    return rec

def guide_experiment(level,ph,mode,e):
    order=level[2];out={};center=np.array([m.section_center(order),0.,0.])
    witness=base.chart_jet("cylinder",0.,0.,0.,order,.14,False)[0].copy()
    ax=np.asarray(m.axis(order));witness[[0,2]]=geom.oldgeom.parent.rot(witness[[0,2]]-ax,-ph)+ax
    held=np.inf
    for name,(ss,vv) in zip(prior.CHARTS,axes(level,ph,True)):
        s,v=ss.ravel(),vv.ravel();side=1 if name.endswith("+") else -1
        sign=1 if name=="cylinder" else side*(-1 if name.startswith("cap") and not name.startswith("cap-normal") else 1)
        blocks=[]
        for i in range(0,len(s),384):
            sl=slice(i,i+384);x,y=s[sl],v[sl]
            cur=geom.chart_jet(name,x,y,ph,order,mode,False);ref=base.chart_jet(name,x,y,0.,order,.14,False)
            blocks.append(previous_solver.relative(cur,ref,sign,center));held=min(held,float(np.min(previous_solver.lengths(cur[:,0]-witness))))
        ar=np.asarray(blocks);out[name]=[len(s),*ar[:,:5].max(axis=0).tolist(),*ar[:,5:].min(axis=0).tolist()]
    return {"phase":ph,"all_charts":out,"held_witness_min_sample":held,"construction":prices(level,ph,mode)}

def solve(mode,e,folder):
    previous={}
    configure(mode)
    for idx,level in enumerate(LEVELS):
        whole=sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])})
        actual=[guide_experiment(level,ph,mode,e) for ph in whole]
        guides={"schema":"R774-raw-physical-construction-complete-resolution-v1","level":idx,"mode":mode,
            "response":e,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
            "source_commit":os.environ["R774_SOURCE_COMMIT"],"rows":actual,
            "columns":["points","relative_gram_op","abs_11","abs_12","abs_22","abs_principal","min_support","min_area"],
            "seam_order":["cylinder-preband","preband-round","round-cap-normal","complete_meridian_chord_minus_length"],
            "rigid_input_prices":["raw_common_cap_3D_chord_minus_length","planar_raw_chord_minus_guard"]}
        identity=prior.write(folder/f"geometry-{idx}.json",guides)
        print("R774 full uncorrected geometry",idx,identity,flush=True)
        na,nr=level[3:5];nfev,it=level[5:7];coeff={};rows=[];mid=[]
        for ip,ph in enumerate(PHASES):
            d=prior.Data(level,ph,e,"fully_free")
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
            a=prior.Data(level,ph,e,"fully_free",True);audit=a.result(x.ravel());del a
            raw=np.asarray(x,dtype="<f8").tobytes()
            (folder/f"level{idx}-phase{ip}.f64").write_bytes(raw);coeff[ip]=x
            rows.append({"phase":ph,"seed":before,"fit":fit,"independent":audit,"status":status,
                        "coeff":[len(raw),sha256(raw).hexdigest()],"volumes":prior.volumes(level,idx,ph,e,"fully_free",x)})
            print("R774 physical whole sphere",mode,e,idx,ph,status,flush=True)
        for j,(l,r) in enumerate(zip(PHASES[:-1],PHASES[1:])):
            ph=(l+r)/2;x=(coeff[j]+coeff[j+1])/2
            a=prior.Data(level,ph,e,"fully_free",True);res=a.result(x.ravel());del a
            mid.append([ph,res,prior.volumes(level,idx,ph,e,"fully_free",x)])
        report={"schema":"R774-complete-single-resolution-whole-sphere-physical-fit-v1","mode":mode,
             "e":e,"level":idx,"grid":level,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R774_SOURCE_COMMIT"],"rules_read_commit":os.environ["R774_RULES_COMMIT"],
             "fitted":rows,"intermediate":mid,"fiducial_material":"whole R764 zero-phase 11-chart sphere",
             "chart_columns":["points","nearly_singular","relative_metric_op","max_abs_principal",
             "min_support","min_relative_area","max_abs_frame11","max_abs_frame12","max_abs_frame22"],
             "volume_columns":["uncorrected_signed_flux","fitted_signed_flux"],
             "volume_angular_radial_order":[(48,72,112)[idx],(6,9,12)[idx]]}
        meta=prior.write(folder/f"stage-{idx}.json",report);print("R774 complete resolution",idx,meta,flush=True)
        previous=coeff


def fitted_chart_jet(chart,s,v,ph,level,mode,folder,rotate=True):
    configure(mode)
    return prior.field(chart,s,v,ph,LEVELS[level],geom.BRANCHES[mode][1],"fully_free",prior.interpolated(folder,level,ph),rotate)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode",choices=tuple(geom.BRANCHES),required=True)
    parser.add_argument("--folder",type=Path,required=True);a=parser.parse_args()
    m.old.disk._public();a.folder.mkdir(exist_ok=True,parents=True)
    solve(a.mode,geom.BRANCHES[a.mode][1],a.folder)
