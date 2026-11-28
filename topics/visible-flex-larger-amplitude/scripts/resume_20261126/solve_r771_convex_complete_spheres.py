#!/usr/bin/env python3
"""Two R771 fixed-metric whole-sphere fits after the endpoint-preserving feasible angular solve."""
import argparse
import os
from pathlib import Path
from hashlib import sha256
from types import SimpleNamespace
import numpy as np
from scipy.optimize import least_squares
import solve_r769_complete_meridian_spheres as previous
import r771_convex_complete_meridian_coordinates as convex
import r771_feasible_two_gram_angular_shapes as angular

prior,norm,base,old,m=previous.prior,previous.norm,previous.base,previous.old,previous.m
LEVELS,PHASES=prior.LEVELS,prior.PHASES
E,L,B=norm.E,norm.L,norm.B

def configure(mode):
    prior.geom=SimpleNamespace(chart_jet=convex.chart_jet,gate=base.gate)
    prior.axes=previous.axes

def diagnosis(level,ph,mode,e):
    idx=LEVELS.index(level);order=level[2];n=(128,256,512)[idx]
    half=old.material(order,True)[-1];q=norm.stations(order)[0]
    s=np.unique(np.r_[np.arange(n)*2*half/n,q,2*half-q,(q[1:]+q[:-1])/2])
    # The shared chart/seam test below reads the actually selected convex chart.
    rec=previous.diagnosis(level,ph,"normalized",e)
    rec.pop("terminal_projected_angular_factor_min",None);rec.pop("initial_angular_factor_min",None)
    D,prices=convex.predecessor.target(s,ph,order,e)
    p,ps,pss,stats=convex.jets_at(s,ph,order,e)
    record={"samples":len(s),"max_abs_endpoint_root_with_address":[float(stats[:,0].max()),float(s[np.argmax(stats[:,0])])],
            "root_function_evaluations":int(stats[:,1].sum()),"fallback_nodes":int(stats[:,2].sum()),
            "minimum_positive_axial_parameter":float(p[:,1].min()),"min_hessian_eigenvalue":float(stats[:,4].min()),
            "max_hessian_eigenvalue":float(stats[:,5].max()),"max_abs_implicit_control_derivatives":
            [float(np.max(np.abs(ps))),float(np.max(np.abs(pss)))],"max_raw_clipped_chord_excess_and_cap_motion":prices.max(axis=0).tolist()}
    v=np.linspace(0,convex.T,43)
    ay=np.inf;two_jet=np.zeros(3);quad_max=0.
    for j in range(0,len(s),64):
        a=s[j:j+64];z,zs,zss=convex.sampled(a,order,ph,e)
        co,ds,dds=p[j:j+len(a)],ps[j:j+len(a)],pss[j:j+len(a)]
        u=np.broadcast_to(v,(len(a),len(v)))
        U,Us,Uss,Uv=convex.virtual(u,co,ds,dds,z,zs,zss)
        ay=min(ay,float(U[:,:,1].min()))
        two_jet=np.maximum(two_jet,[np.max(abs(np.linalg.norm(U,axis=2)-1)),
                       np.max(abs(np.einsum("nvi,nvi->nv",U,Us))),
                       np.max(abs(np.einsum("nvi,nvi->nv",U,Uv)))])
        uq,wq=convex.quadrature(order+8)
        V=convex.evaluate(co,z,uq)[0]
        quad_max=max(quad_max,float(np.max(np.linalg.norm(np.einsum("q,nqj->nj",wq,V)-D[j:j+len(a)],axis=1))))
    record["minimum_sampled_outward_axial_velocity_including_end"]=ay
    record["unit_and_orthogonal_derivatives"]=two_jet.tolist()
    record["higher_quadrature_independent_endpoint_max"]=quad_max
    rec["true_convex_controls"]=record
    return rec

def guide_experiment(level,ph,mode,e):
    order=level[2];out={};center=np.array([m.section_center(order),0.,0.])
    witness=base.chart_jet("cylinder",0.,0.,0.,order,.14,False)[0].copy()
    ax=np.array(m.axis(order));witness[[0,2]]=norm.parent.rot(witness[[0,2]]-ax,-ph)+ax
    held=np.inf
    for name,(ss,vv) in zip(prior.CHARTS,previous.axes(level,ph,True)):
        s,v=ss.ravel(),vv.ravel();side=1 if name.endswith("+") else -1
        sign=1 if name=="cylinder" else side*(-1 if name.startswith("cap") and not name.startswith("cap-normal") else 1)
        blocks=[]
        for i in range(0,len(s),384):
            sl=slice(i,i+384);x,y=s[sl],v[sl]
            cur=prior.geom.chart_jet(name,x,y,ph,order,e,False)
            ref=base.chart_jet(name,x,y,0.,order,.14,False)
            blocks.append(previous.relative(cur,ref,sign,center))
            held=min(held,float(np.min(previous.lengths(cur[:,0]-witness))))
        ar=np.asarray(blocks)
        out[name]=[len(s),*ar[:,:5].max(axis=0).tolist(),*ar[:,5:].min(axis=0).tolist()]
    return {"phase":ph,"all_charts":out,"held_witness_min_sample":held,"construction":diagnosis(level,ph,mode,e)}


def solve(mode,e,folder):
    previous={}
    configure(mode)
    for idx,level in enumerate(LEVELS):
        whole=sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])})
        actual=[guide_experiment(level,ph,mode,e) for ph in whole]
        guides={"schema":"R771-raw-physical-construction-complete-resolution-v1","level":idx,"mode":mode,
            "response":e,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
            "source_commit":os.environ["R771_SOURCE_COMMIT"],"rows":actual,
            "columns":["points","relative_gram_op","abs_11","abs_12","abs_22","abs_principal","min_support","min_area"],
            "seam_order":["cylinder-preband","preband-round","round-cap-normal","complete_meridian_chord_minus_length"],
            "endpoint_angular_prices":["raw_rigid_chord_minus_length","registered_chord_minus_length","pointwise_cap_displacement"]}
        identity=prior.write(folder/f"geometry-{idx}.json",guides)
        print("R771 full uncorrected geometry",idx,identity,flush=True)
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
            print("R771 physical whole sphere",mode,e,idx,ph,status,flush=True)
        for j,(l,r) in enumerate(zip(PHASES[:-1],PHASES[1:])):
            ph=(l+r)/2;x=(coeff[j]+coeff[j+1])/2
            a=prior.Data(level,ph,e,"fully_free",True);res=a.result(x.ravel());del a
            mid.append([ph,res,prior.volumes(level,idx,ph,e,"fully_free",x)])
        report={"schema":"R771-complete-single-resolution-whole-sphere-physical-fit-v1","mode":mode,
             "e":e,"level":idx,"grid":level,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R771_SOURCE_COMMIT"],"rules_read_commit":os.environ["R771_RULES_COMMIT"],
             "fitted":rows,"intermediate":mid,"fiducial_material":"whole R764 zero-phase 11-chart sphere",
             "chart_columns":["points","nearly_singular","relative_metric_op","max_abs_principal",
             "min_support","min_relative_area","max_abs_frame11","max_abs_frame12","max_abs_frame22"],
             "volume_columns":["uncorrected_signed_flux","fitted_signed_flux"],
             "volume_angular_radial_order":[(48,72,112)[idx],(6,9,12)[idx]]}
        meta=prior.write(folder/f"stage-{idx}.json",report);print("R771 complete resolution",idx,meta,flush=True)
        previous=coeff


def fitted_chart_jet(chart,s,v,phase,level,e,folder,rotate=True):
    idx=level;lev=angular.LEVELS[idx];order=LEVELS[idx][2]
    n,k=lev[:2];P=2*old.material(order,True)[-1];sn=np.arange(n)*P/n
    j=max(0,min(len(PHASES)-2,np.searchsorted(PHASES,phase,side="right")-1))
    t=(phase-PHASES[j])/(PHASES[j+1]-PHASES[j]);w=t**3*(10-15*t+6*t*t)
    def at(i):
        return np.fromfile(Path(folder)/f"convex-{idx}-{i}.f64",dtype="<f8").reshape(n,k,2)
    convex.install(order,phase,e,sn,(1-w)*at(j)+w*at(j+1))
    configure("convex")
    return prior.field(chart,s,v,phase,LEVELS[idx],e,"fully_free",prior.interpolated(folder,idx,phase),rotate)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response",type=float,choices=convex.RETREATS,required=True)
    parser.add_argument("--folder",type=Path,required=True);a=parser.parse_args()
    m.old.disk._public();a.folder.mkdir(exist_ok=True,parents=True)
    angular.solve_all(a.response,a.folder)
    solve("convex",a.response,a.folder)
