#!/usr/bin/env python3
"""R780 independent raw and arclength-normalized whole-sphere audits, with physical fitting on both entire rolls."""
import argparse
import os
from hashlib import sha256
from pathlib import Path
import numpy as np
import fit_r780_two_remaining_complete_roll_components as fitting
import solve_r774_shared_pose_complete_spheres as parent

ring=fitting.ring;geom=ring.geom
prior=parent.prior;old,m=geom.old,geom.m
B,E,L,T=geom.B,geom.E,geom.L,geom.T
PHASES=tuple(prior.PHASES)
ALL=tuple(sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])}))
COLS=("points","metric_op","frame11","frame12","frame22","principal_abs","support","relative_area")
ORDERS=(16,24,32)

def mesh(a,b):return np.meshgrid(a,np.unique(b),indexing="ij")

def atlas(idx,ph,order):
    n,k=((40,5),(64,8),(96,12))[idx];P=ring.period(order);st=geom.c.stations(order)
    bb=m.flat_material_s(np.array([-1.,-.85,-.65,-.50,-.35,-.15,.02,.15,.3]),order=order)
    s=np.mod(np.r_[np.arange(n)*P/n,st,P-st,bb,P-bb],P)
    s=np.unique(s);s=s[np.r_[True,np.diff(s)>1e-13]]
    z=np.linspace(0,1,k+1)
    pre=np.unique(np.r_[E*z,E/8,3*E/8,5*E/8,7*E/8,.012])
    rd=np.unique(np.r_[geom.OLD_L*z,m.END_E,geom.OLD_L-m.END_E,geom.OLD_L,
                        geom.OLD_L+geom.LIP/2,L])
    cap=np.unique(np.r_[np.linspace(.015,1,2*k+1),.82*(1-old.JOIN),.97*(1-old.JOIN),
                         1-old.WIDTH-old.ROUND,1-old.WIDTH,1-.0354,1-.0004])
    nr=np.unique(np.r_[old.WIDTH*z,.0004,.001,.0045,.0065]);nr=nr[nr<=old.WIDTH]
    a,r=mesh(np.arange(n)*2*np.pi/n,np.linspace(0,.999999,k+1))
    cart=(m.section_center(order)-old.OFFSET+old.EX*r*np.cos(a),old.EZ*r*np.sin(a))
    aa,rr=mesh(np.arange(n)*2*np.pi/n,np.r_[np.linspace(0,1,k+1),np.sqrt(1/7),.999,.1])
    ix=-.5+.09*rr*np.cos(aa);iz=.09*rr*np.sin(aa)
    out={"cylinder":mesh(s,np.r_[np.linspace(-B,B,2*k+1),-.78,-.70,0.,.33,.70,.78])}
    for sg in ("+","-"):
        for name,v in (("preband",pre),("round",rd),("cap",cap),("cap-normal",nr)):
            out[name+sg]=mesh(s,v)
        out["cap-cartesian"+sg]=cart
        out["cap-island"+sg]=(np.r_[ix.ravel(),ix.ravel()],np.r_[iz.ravel()+.40,iz.ravel()-.40])
    return out

def direction(ch):
    if ch=="cylinder":return 1
    end=1 if ch.endswith("+") else -1
    return -end if ch.startswith("cap") and not ch.startswith("cap-normal") else end

def cross_cost(A,B):
    tag,a,p,n=A;tag2,b,q,m=B
    d=q[None,:,:]-p[:,None,:];sq=np.einsum("ijk,ijk->ij",d,d)
    den=2*np.maximum(abs(np.einsum("ijk,ik->ij",d,n)),abs(np.einsum("ijk,jk->ij",d,m)))
    r=np.divide(sq,den,out=np.full_like(sq,np.inf),where=den>0)
    r[sq==0]=0.;i,j=np.unravel_index(np.argmin(r),r.shape)
    return [tag,tag2,int(sq.size),float(np.sqrt(sq.min())),float(r[i,j]) if np.isfinite(r[i,j]) else None,
            a[i].tolist(),b[j].tolist()]

def measure(field,idx,ph,order,mode,all_cross):
    charts={};group={};center=np.array([m.section_center(order),0.,0.])
    ax=np.asarray(m.axis(order))
    witness=geom.chart_jet("cylinder",0.,0.,0.,order,mode,False)[0].copy()
    witness[[0,2]]=geom.c.oldgeom.parent.rot(witness[[0,2]]-ax,-ph)+ax
    held=np.inf
    for name,(aa,bb) in atlas(idx,ph,order).items():
        s,v=aa.ravel(),bb.ravel();new=field(name,s,v)
        original=geom.chart_jet(name,s,v,0.,order,mode,False)
        charges=parent.previous_solver.relative(new,original,direction(name),center)
        charts[name]=[len(s),*charges]
        held=min(held,float(np.linalg.norm(new[:,0]-witness,axis=1).min()))
        if all_cross and name in ("cylinder","cap+","cap-","round+","round-","preband+","preband-"):
            # Distinct chart interiors avoid shared seam labels in distance and ball probes.
            lo,hi={"cylinder":(-B,B),"cap":(.015,1.),"round":(0.,L),"preband":(0.,E)}[name.rstrip("+-")]
            ok=np.flatnonzero((v>lo+1e-9)&(v<hi-1e-9))
            ids=ok[np.unique(np.linspace(0,len(ok)-1,min((80,144,216)[idx],len(ok))).astype(int))]
            f=new[ids];cr=np.cross(f[:,1],f[:,2]);n=cr/np.maximum(np.linalg.norm(cr,axis=1)[:,None],1e-300)
            group[name]=(name,np.stack((s[ids],v[ids]),axis=1),f[:,0],n)
    ans={"phase":ph,"charts":charts,"initial_witness_sampled_distance":held,
         "max_metric":max(v[1] for v in charts.values()),"max_principal":max(v[5] for v in charts.values()),
         "min_support":min(v[6] for v in charts.values()),"min_relative_area":min(v[7] for v in charts.values())}
    if all_cross:
        groups=list(group.values())
        ans["distinct_chart_pairs"]=[cross_cost(g,h) for i,g in enumerate(groups) for h in groups[i+1:]]
    return ans

def seams(field,idx,order):
    n=(64,96,144)[idx];P=ring.period(order)
    s=np.arange(n)*P/n;zero=np.zeros_like(s);out={}
    for side,sg in ((1,"+"),(-1,"-")):
        center=field("cylinder",s,zero+side*B).copy();center[:,2]*=side;center[:,4]*=side
        stages=((center,field("preband"+sg,s,zero)),(field("preband"+sg,s,zero+E),field("round"+sg,s,zero)),
                (field("round"+sg,s,zero+L),field("cap-normal"+sg,s,zero)))
        out[sg]=[np.max(abs(l-r),axis=(0,2)).tolist() for l,r in stages]
    return out

def chords(field,idx,order):
    P=ring.period(order);st=geom.c.stations(order)
    s=np.unique(np.r_[np.arange((160,320,640)[idx])*P/(160,320,640)[idx],st,P-st]);zero=np.zeros_like(s)
    q=[];result={}
    for side,sg in ((1,"+"),(-1,"-")):
        a=field("cylinder",s,zero+side*B)[:,0];b=field("cap-normal"+sg,s,zero)[:,0];q.append(b)
        g=np.linalg.norm(a-b,axis=1)-T;i=int(np.argmax(g));result[sg]=[float(g[i]),float(s[i])]
    g=np.linalg.norm(q[0]-q[1],axis=1)-2*(B+T);i=int(np.argmax(g))
    result["cap_cap_own_label"]=[float(g[i]),float(s[i])];return result

def signed_volume(field,idx,order):
    na=(36,52,80)[idx];deg=(3,5,7)[idx];P=ring.period(order)
    s=(np.arange(na)+.5)*P/na;node,wt=np.polynomial.legendre.leggauss(deg);total=0.
    for name in ("cylinder","preband+","round+","cap+","preband-","round-","cap-"):
        kind=name.rstrip("+-")
        cuts={"cylinder":(-B,-.7,0.,.33,.70,B),"preband":(0.,E/4,E/2,3*E/4,E),
              "round":(0.,m.END_E,geom.OLD_L/2,geom.OLD_L-m.END_E,geom.OLD_L,L),
              "cap":(0.,.82*(1-old.JOIN),.97*(1-old.JOIN),1-old.WIDTH-old.ROUND,
                     1-old.WIDTH,1-.0004,1.)}[kind]
        cuts=np.unique(cuts)
        vs=np.concatenate([(a+b+(b-a)*node)/2 for a,b in zip(cuts[:-1],cuts[1:])])
        ws=np.concatenate([(b-a)*wt/2 for a,b in zip(cuts[:-1],cuts[1:])])
        ss,v=np.meshgrid(s,vs,indexing="ij");f=field(name,ss,v)
        value=f[...,0,1]*np.cross(f[...,1,:],f[...,2,:])[...,1]
        total+=direction(name)*P/na*np.sum(value@ws)
    return float(total)

def run(mode,folder):
    for idx,order in enumerate(ORDERS):
        common={"branch":mode,"level":idx,"order":order,"run":os.environ["GITHUB_RUN_ID"],
                "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"source_commit":os.environ["R780_SOURCE_COMMIT"],
                "rules_read_commit":os.environ["R780_RULES_COMMIT"],"columns":COLS}
        rawrows=[]
        for ph in ALL:
            field=lambda c,s,v:geom.chart_jet(c,s,v,ph,order,mode,False)
            row=measure(field,idx,ph,order,mode,ph in (0.,.90))
            row.update(pose=list(geom.pose(ph,order,mode)),seams=seams(field,idx,order),
                       chords=chords(field,idx,order),volume=signed_volume(field,idx,order))
            rawrows.append(row)
        print("R780 raw independent",mode,idx,prior.write(folder/f"geometry-{idx}.json",
            {**common,"schema":"R780-raw-sphere-v1","rows":rawrows}),flush=True)
        stages=[];coefs={};fits={}
        for ip,ph in enumerate(PHASES):
            ends={};meta={}
            for side in (1,-1):
                prev=coefs[PHASES[ip-1]][side] if ip else None
                ends[side],meta[side]=fitting.fit(idx,ph,order,mode,side,prev)
                raw=np.asarray(ends[side],dtype="<f8").tobytes()
                (folder/f"coef-{idx}-{ip}-{side}.f64").write_bytes(raw)
                meta[side]["coefficient_bytes_sha256"]=[len(raw),sha256(raw).hexdigest()]
            coefs[ph]=ends;fits[ph]=meta
            print("R780 both complete native fits",mode,idx,ph,flush=True)
        for ip,(a,b) in enumerate(zip(PHASES[:-1],PHASES[1:])):
            coefs[(a+b)/2]={k:(coefs[a][k]+coefs[b][k])/2 for k in (-1,1)}
        for ph in ALL:
            field=ring.PhysicalRoll(ph,order,mode,idx,coefs[ph])
            row=measure(field.jet,idx,ph,order,mode,ph in (0.,.90))
            row.update(seams=seams(field.jet,idx,order),chords=chords(field.jet,idx,order),
                       volume=signed_volume(field.jet,idx,order))
            vals=list(field.diagnostics.values())
            row["ring_stats"]=None if not vals else {"count":len(vals),"inverse_residual_max":max(d[0] for d in vals),
                 "minimum_native_speed":min(d[1] for d in vals),"scale_range":[min(d[4] for d in vals),max(d[4] for d in vals)]}
            row["two_fits"]=fits.get(ph)
            stages.append(row)
            print("R780 independent complete normalized",mode,idx,ph,row["max_metric"],flush=True)
        complete={**common,"schema":"R780-normalized-physical-whole-sphere-v1","fit_limits":fitting.LEVELS[idx],
             "shape":ring.SHAPES[idx],"rows":stages}
        print("R780 full normalized resolution",mode,idx,prior.write(folder/f"stage-{idx}.json",complete),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--mode",choices=tuple(geom.MODES),required=True)
    ap.add_argument("--folder",type=Path,required=True);opt=ap.parse_args()
    geom.m.old.disk._public();opt.folder.mkdir(parents=True,exist_ok=True);run(opt.mode,opt.folder)
