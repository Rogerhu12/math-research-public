#!/usr/bin/env python3
"""Run 55: two full-width central strip shootings plus both complete roll/cap physical fits and independent rereads."""
import argparse
from hashlib import sha256
import os
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.optimize import least_squares
import r792_full_width_rectifying_center_shooting as rib
from r792_rectifying_central_cylinder_and_complete_closed_shoulders import Sphere
import solve_r787_preloaded_long_wall_full_physical_families as parent
from r742_tilted_disk_two_jets import J,cap_s7

g=rib.g;fit=parent.fitbase
MODES=("signed-rolls-gram","signed-rolls-shape","open-whole-gram","open-whole-shape")
SHOOT=((160,9,70),(320,15,110),(640,23,160))

def whole_basis(ch,a,b,o,mode,na,nr,ref):
    t=parent.panel_basis(ch,a,b,o,mode,na,nr,ref)
    if mode!="rigid_caps":return t
    if ch=="cylinder" or ch.startswith("cap"):
        t.fill(0.);return t
    v=J(b,a=1.);u=v+g.E if ch.startswith("round") else v
    z=cap_s7(u/.07)*cap_s7((g.E+g.OLD_L-.022-u)/.07)
    for j in range(0,t.shape[-1],32):
        sl=slice(j,j+32);z0=J(*(np.broadcast_to(k,a.shape)[:,None] for k in z.parts()))
        new=z0*J(*(t[:,k,sl] for k in range(6)))
        for k,arr in enumerate(new.parts()):t[:,k,sl]=arr
    return t

def initial(level):
    return { "grid":level,"chart_columns":["count","nearly_singular","max_gram","max_abs_II","min_support",
                   "min_relative_area","frame11","frame12","frame22"]}

def words_id(x,path):
    body=np.asarray(x,dtype="<f8").tobytes();path.write_bytes(body);return [len(body),sha256(body).hexdigest()]

def diagnostics(arc,word,ph):
    A,d,J0=arc.integrate(word,True);s=arc.s;r=arc.r;c=arc.ctrl
    t=np.einsum("ijk,ik->ij",A,arc.t0);n=np.einsum("ijk,ik->ij",A,arc.n0)
    k,e,_,_=arc.curvatures(r,arc.k0,word);ep=c.db(r)@c.words(word)[1]
    cost=abs(k)*(1+e*e)/(1-g.B*abs(ep));j=int(np.argmax(cost))
    kword,eword,_=c.words(word);ce=c.b.c@eword;ck=c.b.c@kword
    K0=1/.1319
    K=(K0*(np.max(ck)+np.hypot(1.,np.max(ck))) if arc.keep_sign else K0+np.max(abs(ck)))
    curve_envelope=K*(1+np.max(abs(ce))**2)/(1-g.B*c.bound(word))
    tang=J0[3:].reshape(3,3,-1);w=np.stack([np.cross(A[-1,:,i],tang[:,i,:].T) for i in range(3)]).sum(axis=0).T/2
    sv=np.linalg.svd(np.vstack([J0[:3],w]),compute_uv=False)
    return {"side":"right" if not arc.side else "left","arc_original_material":[s[0],s[-1]],"true_initial_width":r[-1],
        "cells":len(r)-1,"goal":arc.goal(ph).tolist(),"endpoint_actual_delta":d[-1].tolist(),
        "orientation":A[-1].tolist(),"endpoint_chord_defect":np.linalg.norm(d[-1]-arc.goal(ph)),
        "orientation_frob":np.linalg.norm(A[-1]-rib.I),"six_endpoint_jac_singular":sv.tolist(),
        "full_width_derivative_hull":c.bound(word),"continuum_formula_K_envelope_from_coefficient_hulls":float(curve_envelope),"curve_formula_K_abs_sample_and_address":[cost[j],s[j],r[j]],
        "opposite_to_reference_section_curvature_nodes":int(np.sum(k*arc.k0<0))}

def arcs(sideflag,o,n,bases):
    return tuple(rib.Arc(j,o,n,bases,sideflag) for j in range(2))

def prolong(x,coarse,fine):
    if x is None:return np.zeros(2*fine.n)
    t=np.linspace(0,1,4*max(coarse.n,fine.n)+1)
    p=coarse.b(t*coarse.length);q=fine.b(t*fine.length)
    return np.linalg.lstsq(q,p@x.reshape(2,-1).T,rcond=1e-13)[0].T.ravel()

def run(mode,out):
    parent.configure();fit.basis=whole_basis
    lock=mode.startswith("signed");shape=mode.endswith("shape");bm="rigid_caps" if lock else "fully_free"
    old_arcs=None;old_word={};prev={}
    for idx,level in enumerate(parent.LEVELS):
        o,na,nr,nfev,it=level[2:7];n,nb,its=SHOOT[idx];aa=arcs(lock,o,n,nb);check=arcs(lock,o,2*n,nb)
        wc={};hist={};phys={};srow=[];regular=[];fitted=[]
        base={"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R792_SOURCE_COMMIT"],"rules_read_commit":os.environ["R792_RULES_COMMIT"],
             "branch":mode,"level":idx,**initial(level)}
        graph=parent.MaterialGraph(idx,o)
        for ip,ph in enumerate(parent.PH):
            wc[ph]=[];hist[ph]=[]
            for j,a in enumerate(aa):
                x=prolong(old_word.get((ip,j)),old_arcs[j].ctrl if old_arcs is not None else None,a.ctrl)
                if ip:
                    last=wc[parent.PH[ip-1]][j]
                    def price(z):
                        R,d=a.integrate(z);return np.linalg.norm(d[-1]-a.goal(ph))+np.linalg.norm(R[-1]-rib.I)
                    if price(last)<price(x):x=last
                y,stat=a.shoot(ph,x,its,shape);wc[ph].append(y)
                hist[ph].append([stat,words_id(y,out/f"strip-{idx}-{ip}-{j}.f64")])
            print("R792 actual two-end shootings",mode,idx,ph,hist[ph],flush=True)
        old_arcs=aa;old_word={(ip,j):x for ip,p in enumerate(parent.PH) for j,x in enumerate(wc[p])}
        for p,q in zip(parent.PH[:-1],parent.PH[1:]):wc[(p+q)/2]=[(x+y)/2 for x,y in zip(wc[p],wc[q])]
        for ph in parent.ALL:
            m=Sphere(check,wc[ph],ph,o);phys[ph]=m
            srow.append({"phase":ph,"solver_word_identity":hist.get(ph),"fit_grid":[diagnostics(a,x,ph) for a,x in zip(aa,wc[ph])],
                 "independent":[diagnostics(a,x,ph) for a,x in zip(check,wc[ph])],"closed_field":[z.prices for z in m.strips]})
        print("R792 entire central-end results",fit.write(out/f"shoot-{idx}.json",{**base,"schema":"R792-full-width-both-ends-v1","rows":srow}),flush=True)
        def use(grid):
            def field(ch,s,y,ph,order,e=None,rotate=False):
                if ph==0.:return g.chart_jet(ch,s,y,0.,order)
                return grid[ph].evaluate(ch,s,y)
            fit.geom=SimpleNamespace(chart_jet=field,gate=g.old.base.gate)
        use(phys)
        for ph in parent.ALL:
            data=parent.Study(level,ph,bm,1.,True);raw=data.result(np.zeros(3*data.p));del data
            field=lambda c,a,b:phys[ph].evaluate(c,a,b)
            regular.append(parent.stage(field,graph,idx,ph,level,mode,raw))
        print("R792 independent complete guide",fit.write(out/f"geometry-{idx}.json",
            {**base,"schema":"R792-rejoined-closed-spheres-v1","rows":regular}),flush=True)
        low={ph:Sphere(aa,wc[ph],ph,o) for ph in parent.PH};use(low)
        coef={};status={}
        for ip,ph in enumerate(parent.PH):
            data=parent.Study(level,ph,bm,float(shape));x=fit.prolong(prev.get(ip),parent.LEVELS[idx-1][3:5] if idx else None,(na,nr))
            if ip and np.linalg.norm(data.fun(coef[parent.PH[ip-1]].ravel()))<np.linalg.norm(data.fun(x.ravel())):x=coef[parent.PH[ip-1]]
            if ph:
                z=least_squares(data.fun,x.ravel(),jac=data.jac,method="trf",tr_solver="lsmr",tr_options={
                    "maxiter":it,"atol":.0002,"btol":.0002},max_nfev=nfev,ftol=1e-9,xtol=1e-9,gtol=1e-9,x_scale=1.)
                w=z.x.reshape(-1,3);st=[int(z.status),int(z.nfev),float(z.cost),float(z.optimality)]
            else:w=x*0.;st=[0,0,float(np.linalg.norm(data.fun(w.ravel()))**2/2),0.]
            coef[ph]=w;status[ph]=[st,words_id(w,out/f"whole-{idx}-{ip}.f64")];del data
            print("R792 independent original refinement",mode,idx,ph,st,flush=True)
        prev={i:coef[p] for i,p in enumerate(parent.PH)}
        for p,q in zip(parent.PH[:-1],parent.PH[1:]):coef[(p+q)/2]=(coef[p]+coef[q])/2
        use(phys)
        for ph in parent.ALL:
            x=coef[ph];d=parent.Study(level,ph,bm,1.,True);res=d.result(x.ravel());del d
            field=lambda c,a,b:fit.field(c,a,b,ph,level,0.,bm,x)
            r=parent.stage(field,graph,idx,ph,level,mode,res);r["solver_word_identity"]=status.get(ph);fitted.append(r)
        print("R792 all thirteen charts and phases",fit.write(out/f"stage-{idx}.json",
            {**base,"schema":"R792-complete-three-channel-end-solves-v1","rows":fitted}),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--mode",choices=MODES,required=True)
    ap.add_argument("--folder",type=Path,required=True);op=ap.parse_args();op.folder.mkdir(exist_ok=True,parents=True)
    g.m.old.disk._public();run(op.mode,op.folder)
