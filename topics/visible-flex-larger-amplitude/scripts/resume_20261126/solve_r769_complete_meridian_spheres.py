#!/usr/bin/env python3
"""Joint all-chart physical fits starting at two normalized-roll and two actual unit-meridian spheres."""
import argparse
from hashlib import sha256
from pathlib import Path
import os
from types import SimpleNamespace
import numpy as np
from scipy.optimize import least_squares
import r769_closed_turn_redistribution_and_complete_rolls as norm
import r769_full_unit_meridian_shooting as shooting
import solve_r764_corrugated_whole_sphere as prior

base,old,m=norm.base,norm.old,norm.m
E,L,B=norm.E,norm.L,norm.B
PHASES=prior.PHASES
LEVELS=prior.LEVELS
original_axes=prior.axes

def axes(level,ph,audit):
    original=original_axes(level,ph,audit);order=level[2]
    half=old.material(order,True)[-1];grid=norm.stations(order)[0]
    if audit:
        grid=np.unique(np.r_[grid,(grid[1:]+grid[:-1])/2])
    grid=np.r_[grid,2*half-grid]
    out=[]
    for name,(ss,vv) in zip(prior.CHARTS,original):
        if name.startswith("cap-cartesian"):
            out.append((ss,vv))
        else:
            s=np.unique(np.r_[ss[:,0],grid])
            s=s[np.r_[True,np.diff(s)>1e-13]]
            out.append(np.meshgrid(s,vv[0],indexing="ij"))
    return out

def configure(mode):
    selected=norm.chart_jet if mode=="normalized" else shooting.chart_jet
    # Each natural process owns its adapter. The complete zero-phase reference always
    # returns the original full R764 function before either moving response is used.
    prior.geom=SimpleNamespace(chart_jet=selected,gate=base.gate)
    prior.axes=axes

def diagnosis(level,ph,mode,e):
    order=level[2];half=old.material(order,True)[-1]
    s0=norm.stations(order)[0];n={16:128,24:256,32:512}[order]
    s=np.unique(np.r_[np.arange(n+1)*2*half/n,s0,2*half-s0,(s0[:-1]+s0[1:])/2])
    w=np.zeros_like(s);pick=prior.geom.chart_jet
    q,t,nn,k,kp,r,rs,rss=norm.curve(s,ph,order)
    rec={"closure_lambda_and_three_integrals":[float(norm.state(order,ph)[2]),*norm.state(order,ph)[4]],
         "ratio_min_max":[float(r.min()),float(r.max())],"max_abs_curvature":float(np.max(np.abs(k))),
         "max_abs_ratio_s":float(np.max(np.abs(rs))),"whole_period_addresses":len(s),"seams":{}}
    sm=float(m.flat_material_s(np.asarray([.30]),order=order)[0]);labels=np.asarray([sm,2*half-sm])
    init=base.chart_jet("cap-normal+",labels,np.zeros(2),0.,order,.14,False)[:,0]
    rigid_chord=np.linalg.norm(init[1]-init[0])
    mer=pick("preband+",labels,np.full(2,E),ph,order,e,False)[:,0]
    rec["symmetric_rigid_cap_test"]=[float(np.linalg.norm(mer[1]-mer[0])),float(rigid_chord),float(2*L),
        float(np.linalg.norm(mer[1]-mer[0])-rigid_chord-2*L)]
    for side,suffix in ((-1,"-"),(1,"+")):
        cyl=pick("cylinder",s,w+side*B,ph,order,e,False)
        cyl[:,2]*=side;cyl[:,4]*=side
        pre0=pick("preband"+suffix,s,w,ph,order,e,False)
        pre1=pick("preband"+suffix,s,w+E,ph,order,e,False)
        rd0=pick("round"+suffix,s,w,ph,order,e,False)
        rd1=pick("round"+suffix,s,w+L,ph,order,e,False)
        cap=pick("cap-normal"+suffix,s,w,ph,order,e,False)
        rec["seams"][suffix]=[np.max(np.abs(a-b),axis=(0,2)).tolist()
                               for a,b in ((cyl,pre0),(pre1,rd0),(rd1,cap))]
        rec["seams"][suffix].append(float(np.max(np.linalg.norm(rd1[:,0]-pre0[:,0],axis=1))-(E+L)))
    if mode=="shoot":
        rec["real_spherical_flow"]=shooting.controls(order,ph,e)[2]
    else:
        k0=old.data(s,0.,order,True)[3]
        from r742_tilted_disk_two_jets import J
        _,d=norm.travel(J(1+e*(r-1)),J(np.full_like(s,L)),True,order)
        rec["terminal_projected_angular_factor_min"]=float(np.min(1-k*d.v))
        rec["initial_angular_factor_min"]=float(np.min(1-k0*m.terminal(order)[1]))
    return rec

def fitted_chart_jet(chart,s,v,phase,level,mode,response,folder,rotate=True):
    configure(mode)
    return prior.field(chart,s,v,phase,LEVELS[level],response,"fully_free",prior.interpolated(folder,level,phase),rotate)

def lengths(x):
    return np.linalg.norm(x,axis=1)

def relative(cur,ref,sign,center):
    a,b=ref[:,1],ref[:,2];l=lengths(a);e1=a/l[:,None]
    proj=np.einsum("ij,ij->i",b,e1);perp=lengths(b-proj[:,None]*e1)
    pa=1/l[:,None];pc=1/perp[:,None];pb=-proj[:,None]*pa*pc
    ff=prior.linjet(cur,pa,pb,pc);f,ta,tb,aa,ab,bb=np.moveaxis(ff,1,0)
    cr=np.cross(ta,tb);area=lengths(cr);nor=sign*cr/np.maximum(area[:,None],1e-18)
    dot=lambda p,q:np.einsum("ni,ni->n",p,q)
    g11,g12,g22=dot(ta,ta),dot(ta,tb),dot(tb,tb)
    gram=np.stack((g11-1,g12,g12,g22-1),axis=1).reshape(-1,2,2)
    l,mix,n=dot(nor,aa),dot(nor,ab),dot(nor,bb)
    ii=np.stack((l,mix,mix,n),axis=1).reshape(-1,2,2)
    _,sv,vt=np.linalg.svd(np.swapaxes(ff[:,1:3],1,2),full_matrices=False)
    ks=np.linalg.eigvalsh((vt@ii@np.swapaxes(vt,1,2))/np.maximum(sv[:,:,None]*sv[:,None,:],1e-24))
    return [float(np.max(np.abs(np.linalg.eigvalsh(gram)))),float(np.max(np.abs(g11-1))),
            float(np.max(np.abs(g12))),float(np.max(np.abs(g22-1))),float(np.max(np.abs(ks))),
            float(np.min(dot(f-center,nor))),float(np.min(area))]



def guide_experiment(level,ph,mode,e):
    order=level[2];out={};center=np.array([m.section_center(order),0.,0.])
    witness=base.chart_jet("cylinder",0.,0.,0.,order,.14,False)[0].copy()
    ax=np.array(m.axis(order));witness[[0,2]]=norm.parent.rot(witness[[0,2]]-ax,-ph)+ax
    held=np.inf
    for name,(ss,vv) in zip(prior.CHARTS,axes(level,ph,True)):
        s,v=ss.ravel(),vv.ravel();side=1 if name.endswith("+") else -1
        sign=1 if name=="cylinder" else side*(-1 if name.startswith("cap") and not name.startswith("cap-normal") else 1)
        blocks=[]
        for i in range(0,len(s),384):
            sl=slice(i,i+384);x,y=s[sl],v[sl]
            cur=prior.geom.chart_jet(name,x,y,ph,order,e,False)
            ref=base.chart_jet(name,x,y,0.,order,.14,False)
            blocks.append(relative(cur,ref,sign,center))
            held=min(held,float(np.min(lengths(cur[:,0]-witness))))
        ar=np.asarray(blocks)
        out[name]=[len(s),*ar[:,:5].max(axis=0).tolist(),*ar[:,5:].min(axis=0).tolist()]
    return {"phase":ph,"all_charts":out,"held_witness_min_sample":held,"construction":diagnosis(level,ph,mode,e)}


def solve(mode,e,folder):
    previous={}
    configure(mode)
    for idx,level in enumerate(LEVELS):
        whole=sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])})
        actual=[guide_experiment(level,ph,mode,e) for ph in whole]
        guides={"schema":"R769-raw-physical-construction-complete-resolution-v1","level":idx,"mode":mode,
            "response":e,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
            "source_commit":os.environ["R769_SOURCE_COMMIT"],"rows":actual,
            "columns":["points","relative_gram_op","abs_11","abs_12","abs_22","abs_principal","min_support","min_area"],
            "seam_order":["cylinder-preband","preband-round","round-cap-normal","complete_meridian_chord_minus_length"],
            "shoot_angular_prices":["raw_rigid_chord_minus_length","registered_chord_minus_length","pointwise_cap_displacement"]}
        identity=prior.write(folder/f"geometry-{idx}.json",guides)
        print("R769 full uncorrected geometry",idx,identity,flush=True)
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
            print("R769 physical whole sphere",mode,e,idx,ph,status,flush=True)
        for j,(l,r) in enumerate(zip(PHASES[:-1],PHASES[1:])):
            ph=(l+r)/2;x=(coeff[j]+coeff[j+1])/2
            a=prior.Data(level,ph,e,"fully_free",True);res=a.result(x.ravel());del a
            mid.append([ph,res,prior.volumes(level,idx,ph,e,"fully_free",x)])
        report={"schema":"R769-complete-single-resolution-whole-sphere-physical-fit-v1","mode":mode,
             "e":e,"level":idx,"grid":level,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R769_SOURCE_COMMIT"],"rules_read_commit":os.environ["R769_RULES_COMMIT"],
             "fitted":rows,"intermediate":mid,"fiducial_material":"whole R764 zero-phase 11-chart sphere",
             "chart_columns":["points","nearly_singular","relative_metric_op","max_abs_principal",
             "min_support","min_relative_area","max_abs_frame11","max_abs_frame12","max_abs_frame22"],
             "volume_columns":["uncorrected_signed_flux","fitted_signed_flux"],
             "volume_angular_radial_order":[(48,72,112)[idx],(6,9,12)[idx]]}
        meta=prior.write(folder/f"stage-{idx}.json",report);print("R769 complete resolution",idx,meta,flush=True)
        previous=coeff


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode",choices=("normalized","shoot"),required=True)
    parser.add_argument("--response",type=float,required=True)
    parser.add_argument("--folder",type=Path,required=True)
    a=parser.parse_args()
    if a.response not in (norm.PITCH if a.mode=="normalized" else shooting.RETREATS):
        raise ValueError("unregistered complete physical branch")
    m.old.disk._public();a.folder.mkdir(exist_ok=True,parents=True)
    solve(a.mode,a.response,a.folder)
