#!/usr/bin/env python3
"""R787 full physical fits on one preloaded long-wall sphere, with four actual scopes and independent graph checks."""
import argparse
from hashlib import sha256
import os
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.optimize import least_squares
import r787_preloaded_two_complete_caps_and_four_returning_meridians as geom
from r787_complete_material_graph_paths import MaterialGraph
import solve_r780_exact_crowns_and_normalized_whole_rolls as previous
import solve_r764_corrugated_whole_sphere as fitbase
from r787_complete_cartesian_cap_basis_pullback import polar_basis
from r742_tilted_disk_two_jets import J,cap_s7

LEVELS=tuple(fitbase.LEVELS);PH=tuple(fitbase.PHASES);ALL=tuple(fitbase.ALL)
MODES=("panels-gram","panels-shape","open-gram","open-shape")
ORIG_BASIS=fitbase.basis
CHARTS=("cylinder",)+tuple(k+s for s in ("+","-") for k in
        ("preband","round","cap","cap-normal","cap-cartesian","cap-island"))

def win(z):
    return cap_s7((z+.99)/.035)*cap_s7((.29-z)/.035)

def panel_basis(ch,a,b,order,mode,na,nr,ref):
    if ch.startswith(("cap-cartesian","cap-island")):
        return polar_basis(ch,a,b,order,mode,na,nr,ref,ORIG_BASIS)
    t=ORIG_BASIS(ch,a,b,order,mode,na,nr,ref)
    if mode!="rigid_caps" or ch.startswith("cap"):
        return t
    # Pay the complete material flat plate, including its two physical terminal two-jets.
    sx=J(a,s=1.);q,n=geom.wall.parts(sx,order);xx=q[0]
    cut=1-cap_s7((xx+1.035)/.035)*cap_s7((.335-xx)/.035)
    for j in range(0,t.shape[-1],32):
        sl=slice(j,j+32);h=J(*(t[:,k,sl] for k in range(6)))
        gate=J(*(np.broadcast_to(z,a.shape)[:,None] for z in cut.parts()))
        p=gate*h
        for k,val in enumerate(p.parts()):t[:,k,sl]=val
    return t

def axes(level,ph,audit):
    idx=LEVELS.index(level);o=level[2];n,k=(level[-2],level[-1]) if audit else level[:2]
    P=2*geom.old.old.material(o,True)[-1];st=geom.old.c.stations(o);half=geom.m.LEFT_LENGTH/2
    wall_len,slack,_=geom.wall.spec(o);knots=np.unique(np.r_[0.,slack,slack+np.asarray(geom.wall.CLOCK),wall_len])
    left=[]
    for t in knots:
        lo,hi=0.,half
        for _ in range(56):
            a=(lo+hi)/2;v=a+(wall_len-half)*cap_s7(J(np.asarray(a/half))).v
            if v<wall_len-t:lo=a
            else:hi=a
        left.append((lo+hi)/2)
    extra=geom.m.flat_material_s(np.array([-1.,-.965,-.65,-.5,-.35,0.,.265,.30]),order=o)
    grip=np.array([geom.m.grip_s(x,o) for x in (.10,.18,.25,.55,.85,.96,1.05,np.pi/2)])
    if audit:st=np.unique(np.r_[st,(st[:-1]+st[1:])/2])
    a=np.r_[st,left,grip,extra];s=np.unique(np.mod(np.r_[a,P-a,np.arange(n)*P/n],P))
    s=s[np.r_[True,np.diff(s)>1e-12]]
    def mesh(v):
        return np.meshgrid(s,np.unique(v),indexing="ij")
    u=np.linspace(0,1,k+1)
    cart=previous.atlas(idx,ph,o)
    g={"cylinder":mesh(np.r_[np.linspace(-geom.B,geom.B,2*k+1),-.7,0.,.33,.7])}
    for sg in ("+","-"):
        g["preband"+sg]=mesh(np.r_[geom.E*u,.10,.132,.001,.131,.133,.439])
        g["round"+sg]=mesh(np.r_[geom.L*u,geom.OLD_L,geom.OLD_L+.003,geom.m.END_E,geom.OLD_L-geom.m.END_E])
        g["cap"+sg]=mesh(np.r_[np.linspace(.015,1,k+1),.998,.9992,.9996,.9998])
        g["cap-normal"+sg]=mesh(np.r_[.007*u,.0004,.0006,.0008])
        g["cap-cartesian"+sg]=cart["cap-cartesian"+sg]
        g["cap-island"+sg]=cart["cap-island"+sg]
    return [g[ch] for ch in CHARTS]

def witness(order):
    P=2*geom.old.old.material(order,True)[-1]
    s=P-geom.m.grip_s(np.pi/2,order)
    return geom.chart_jet("cylinder",s,0.,0.,order)[0]

def configure():
    fitbase.L=geom.L
    fitbase.CHARTS=CHARTS;fitbase.basis=panel_basis;fitbase.axes=axes
    fitbase.geom=SimpleNamespace(chart_jet=geom.chart_jet,gate=geom.old.base.gate)

class Study(fitbase.Data):
    def __init__(self,level,ph,mode,charges,audit=False):
        super().__init__(level,ph,0.,mode,audit)
        self.witness=witness(level[2]);self.held=.878*(ph/.90)**2
        d,c,s=geom.axial_clock(ph);pg,dg,pb,db,dy,dz,zl=geom.pose(ph,level[2])
        self.center=np.array([geom.m.section_center(level[2]),dy/2,dz/2])
        for name,i,j in self.blocks:
            if name.startswith("cap-island"):self.ori[i:j]=-1 if name.endswith("+") else 1
        self.weights7=np.array([1.,1.,1.,charges,charges,charges,charges])
    def state(self,x):
        f,g,i,s,a,r,d=super().state(x)
        return f,g,i,s,a,r*self.weights7[None,:],d*self.weights7[None,:,None,None]

def all_pairs(field,idx,order):
    P=2*geom.old.old.material(order,True)[-1];n=(24,40,64)[idx];s=(np.arange(n)+.3)*P/n
    groups=[]
    for ch in ("cylinder","preband+","preband-","round+","round-","cap+","cap-"):
        typ=ch.rstrip("+-");a,b={"cylinder":(-geom.B,geom.B),"preband":(0.,geom.E),
                              "round":(0.,geom.L),"cap":(0.,1.)}[typ]
        ss,yy=np.meshgrid(s,np.linspace(a,b,(5,7,9)[idx]+2)[1:-1],indexing="ij")
        uv=np.column_stack((ss.ravel(),yy.ravel()));f=field(ch,*uv.T);cr=np.cross(f[:,1],f[:,2])
        norm=cr/np.maximum(np.linalg.norm(cr,axis=1)[:,None],1e-20)
        groups.append((ch,uv,f[:,0],norm))
    return [previous.cross_cost(a,b) for i,a in enumerate(groups) for b in groups[i+1:]]

def seams(field,idx,order):
    n=(64,96,144)[idx];P=2*geom.old.old.material(order,True)[-1];s=np.arange(n)*P/n;z=np.zeros(n)
    result={}
    for sign,sg in ((1,"+"),(-1,"-")):
        cent=field("cylinder",s,z+sign*geom.B).copy();cent[:,2]*=sign;cent[:,4]*=sign
        result[sg]=[np.max(abs(a-b),axis=(0,2)).tolist() for a,b in (
            (cent,field("preband"+sg,s,z)),(field("preband"+sg,s,z+geom.E),field("round"+sg,s,z)),
            (field("round"+sg,s,z+geom.L),field("cap-normal"+sg,s,z)))]
    return result

def stage(field,graph,idx,ph,level,mode,res):
    o=level[2];r=res["charts"];row={"phase":ph,"charts":r,"max_metric":max(x[2] for x in r.values()),
         "max_principal":max(x[3] for x in r.values()),"min_support":min(x[4] for x in r.values()),
         "min_relative_area":min(x[5] for x in r.values()),"initial_witness_sampled_distance":res["held_witness_min_sample"],
         "volume":previous.signed_volume(field,idx,o),"seams":seams(field,idx,o),
         "chords":graph.audit(field),"maximum_pre_meridian_chord_minus_path":res["max_preband_endpoint_chord_minus_initial_path"]}
    if ph in (0.,.90):row["distinct_chart_pairs"]=all_pairs(field,idx,o)
    return row

def solve(mode,out):
    configure();sco=mode.endswith("shape");base_mode="rigid_caps" if mode.startswith("panels") else "fully_free"
    prev={}
    for idx,level in enumerate(LEVELS):
        order,na,nr,nfev,it=level[2:7];graph=MaterialGraph(idx,order)
        common={"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R787_SOURCE_COMMIT"],"rules_read_commit":os.environ["R787_RULES_COMMIT"],
             "branch":mode,"level":idx,"grid":level,"chart_columns":["count","nearly_singular","max_gram","max_abs_II",
             "min_support","min_relative_area","frame11","frame12","frame22"]}
        natural=[];fitted=[];coeff={};history={}
        for ph in ALL:
            ad=Study(level,ph,base_mode,1.,True);zero=np.zeros(3*ad.p);raw=ad.result(zero);del ad
            fld=lambda c,x,v:geom.chart_jet(c,x,v,ph,order)
            rr=stage(fld,graph,idx,ph,level,mode,raw)
            rr["two_signed_clocks_and_lower_translation"]=geom.pose(ph,order);natural.append(rr)
        print("R787 raw whole",mode,idx,fitbase.write(out/f"geometry-{idx}.json",
            {**common,"schema":"R787-preloaded-complete-reference-and-physical-guide-v1","rows":natural}),flush=True)
        for ip,ph in enumerate(PH):
            data=Study(level,ph,base_mode,float(sco))
            x0=fitbase.prolong(prev.get(ip),LEVELS[idx-1][3:5] if idx else None,(na,nr))
            if ip and np.linalg.norm(data.fun(coeff[PH[ip-1]].ravel()))<np.linalg.norm(data.fun(x0.ravel())):
                x0=coeff[PH[ip-1]]
            if ph:
                opt=least_squares(data.fun,x0.ravel(),jac=data.jac,method="trf",tr_solver="lsmr",
                    tr_options={"maxiter":it,"atol":.0002,"btol":.0002},max_nfev=nfev,
                    ftol=1e-9,xtol=1e-9,gtol=1e-9,x_scale=1.)
                z=opt.x.reshape(-1,3);status=[int(opt.status),int(opt.nfev),float(opt.cost),float(opt.optimality)]
            else:z=x0*0.;status=[0,0,float(np.linalg.norm(data.fun(z.ravel()))**2/2),0.]
            fit=data.result(z.ravel());del data
            body=np.asarray(z,dtype="<f8").tobytes();(out/f"coef-{idx}-{ip}.f64").write_bytes(body)
            coeff[ph]=z;history[ph]=[status,len(body),sha256(body).hexdigest(),max(x[2] for x in fit["charts"].values())]
            print("R787 fitted",mode,idx,ph,status,flush=True)
        prev={i:coeff[t] for i,t in enumerate(PH)}
        for a,b in zip(PH[:-1],PH[1:]):coeff[(a+b)/2]=(coeff[a]+coeff[b])/2
        for ph in ALL:
            z=coeff[ph];ad=Study(level,ph,base_mode,1.,True);res=ad.result(z.ravel());del ad
            fld=lambda c,x,v:fitbase.field(c,x,v,ph,level,0.,base_mode,z)
            rr=stage(fld,graph,idx,ph,level,mode,res);rr["natural_solver_word_identity"]=history.get(ph)
            fitted.append(rr)
        print("R787 independent physical whole",mode,idx,fitbase.write(out/f"stage-{idx}.json",
            {**common,"schema":"R787-complete-nonseparable-physical-refinements-v1","rows":fitted}),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--mode",choices=MODES,required=True)
    ap.add_argument("--folder",type=Path,required=True);op=ap.parse_args();op.folder.mkdir(parents=True,exist_ok=True)
    geom.m.old.disk._public();solve(op.mode,op.folder)
