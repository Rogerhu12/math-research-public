#!/usr/bin/env python3
"""Four independent whole-sphere R764 physical fits on the one initial corrugated pre-roll metric."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix,vstack
from scipy.sparse.linalg import LinearOperator
from r742_tilted_disk_two_jets import J,unary,cap_s7
import r764_corrugated_pre_roll_and_movable_complete_caps as geom

m=geom.m;old=geom.old;B=geom.HALF;E=geom.E;L=geom.L
PHASES=(0.,.15,.30,.45,.60,.75,.90)
ALL=tuple(sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])}))
LEVELS=((24,6,16,6,3,12,12,64,12),(40,9,24,12,6,20,16,96,18),(64,12,32,24,12,30,20,144,26))
CHARTS=("cylinder",)+tuple(k+s for s in ("+","-") for k in ("preband","round","cap","cap-normal","cap-cartesian"))
KMAX=1/.132;RMIN=.132
CENTERS=tuple((x,y,z) for x in (-.95,-.48,.04,.46,.74) for y in (-1.24,-.73,0.,.73,1.24) for z in (-.70,0.,.70))
FEATURES=len(CENTERS)+4


def axes(level,ph,audit):
    n,k,order,na,nr,_,_,an,ak=level
    n,k=(an,ak) if audit else (n,k)
    cut,ext,half=old.material(order,True);elbows=np.asarray(old.clock_spec(True)[1])
    main=m.flat_material_s(np.array([-.5,.30,.30+.26*.125,.56-.26*.125,.56,1.]),order=order)
    s0=m.LEFT_LENGTH/2+m.constants(order)[9]-.05
    basic=np.r_[0.,half,s0,cut+elbows,cut-.30,cut-.20,cut-.10,main,main-.15*ph,
                [m.grip_s(a,order) for a in (.10,.18,.25,.55,.85,.96,1.05)]]
    if audit:
        basic=np.r_[basic,cut+(elbows[1:]+elbows[:-1])/2,
              [m.grip_s(a,order)+b*r for a,_,r in m.MARKS for b in (-1.,-.7,0.,.7,1.)]]
    s=np.unique(np.r_[np.arange(n)*2*half/n,basic,2*half-basic])
    vcap=np.unique(np.r_[np.linspace(.02,1,k+1),(1-old.JOIN)*np.array([.82,.84,.86,.87,.92,.97,.98]),
              1-old.WIDTH,1-old.WIDTH-old.ROUND])
    ys=np.unique(np.r_[np.linspace(-B,B,2*k+1),-.78,-.70,0.,.33,.70,.78,B,-B])
    pre=E*np.unique(np.r_[np.linspace(0,1,k+1),.125,.25,.375,.5,.625,.75,.875])
    roll=np.unique(np.r_[np.linspace(0,L,k+1),m.END_E,L-m.END_E])
    normal=np.unique(np.r_[np.linspace(0,old.WIDTH,k+1),.0065])
    aa,rr=np.meshgrid(np.arange(n)*2*np.pi/n,np.linspace(0,.999999,max(3,k//2)),indexing="ij")
    cart=(m.section_center(order)-old.OFFSET+old.EX*rr*np.cos(aa),old.EZ*rr*np.sin(aa))
    out=[]
    for chart in CHARTS:
        kind=chart if chart=="cylinder" else chart[:-1]
        if kind=="cap-cartesian":
            out.append(cart)
        else:
            v={"cylinder":ys,"preband":pre,"round":roll,"cap":vcap,"cap-normal":normal}[kind]
            out.append(np.meshgrid(s,v,indexing="ij"))
    return out


def cardinal(x):
    a=np.abs(x.v);q=np.maximum(2-a,0.);sig=np.sign(x.v);inner=a<1
    val=np.where(inner,(4-6*a*a+3*a**3)/6,q**3/6)
    der=np.where(inner,(-12*a+9*a*a)/6,-q*q/2)*sig
    sec=np.where(inner,-2+3*a,q)
    return unary(x,val,der,sec)


def tensor_coords(x,y,period,na,nr):
    ax=x*(na/period)
    av=np.mod(ax.v[:,None]-np.arange(na)[None,:]+na/2,na)-na/2
    def shaped(j):
        return [np.broadcast_to(t,j.v.shape)[:,None] for t in j.parts()[1:]]
    aa=cardinal(J(av,*shaped(ax)))
    ry=y*nr;rv=ry.v[:,None]-np.arange(-1,nr+2)[None,:]
    rr=cardinal(J(rv,*shaped(ry)))
    a=J(*(t[:,:,None] for t in np.broadcast_arrays(*aa.parts())))
    b=J(*(t[:,None,:] for t in np.broadcast_arrays(*rr.parts())))
    return a*b


def basis(chart,a,b,order,mode,na,nr,ref):
    n=len(a);s=J(a,s=1.);v=J(b,a=1.);one=J(np.ones(n))
    side=1 if chart.endswith("+") else -1
    kind=chart if chart=="cylinder" else chart[:-1]
    pole=kind=="cap-cartesian"
    guard=geom.gate(kind,s,v,order)
    if kind=="cylinder":
        lane=v
    elif kind=="preband":
        lane=side*(B+v)
    elif kind=="round":
        lane=side*(B+E+v)
    elif kind=="cap":
        lane=side*(B+E+L+1-v)
    elif kind=="cap-normal":
        lane=side*(B+E+L+v)
    else:
        lane=J(np.full(n,side*(B+E+L+.25)))
    if mode=="rigid_caps":
        guard=guard*cap_s7((B+E+L-lane)/.12)*cap_s7((B+E+L+lane)/.12)
    x,y,z=(J(*ref[:,:,i].T) for i in range(3))
    loc=na*(nr+3);block=np.zeros((n,6,FEATURES+3*loc))
    def add(col,j):
        for k,val in enumerate(j.parts()):
            block[:,k,col]=val
    for i,j in enumerate((one,x,y,z)):
        add(i,guard*j)
    for i,(cx,cy,cz) in enumerate(CENTERS):
        dx=(x-cx)/.43;dy=(y-cy)/.48;dz=(z-cz)/.58
        add(i+4,guard*old.expj(-(dx*dx+dy*dy+dz*dz)))
    if pole:
        return block
    limit=B+E+L+.145
    wins=((-B-.16,B+.16),(B-.25,limit),(-limit,-B+.25))
    period=2*old.material(order,True)[-1]
    for j,(left,right) in enumerate(wins):
        t=(lane-left)/(right-left)
        env=guard*cap_s7(t/.13)*cap_s7((1-t)/.13)
        sel=np.flatnonzero(env.v!=0.)
        if not len(sel):
            continue
        def choose(z):
            return J(*(np.broadcast_to(q,(n,))[sel] for q in z.parts()))
        cols=tensor_coords(choose(s),choose(t),period,na,nr)
        cgate=J(*(q[:,None,None] for q in choose(env).parts()))
        start=FEATURES+j*loc
        for k,val in enumerate((cgate*cols).parts()):
            block[sel,k,start:start+loc]=val.reshape(len(sel),loc)
    return block


def linjet(mat,pa,pb,pc):
    # Initial orthonormal frame: e1=pa*u, e2=pb*u+pc*v, with positive determinant.
    # The Hessian terms from spatial differentiation of frame coefficients are
    # tangent and vanish against the normal, so the same transform applies to II.
    a,b=mat[:,1],mat[:,2]
    aa,ab,bb=mat[:,3],mat[:,4],mat[:,5]
    return np.stack((mat[:,0],pa*a,pb*a+pc*b,pa*pa*aa,pa*pb*aa+pa*pc*ab,
                     pb*pb*aa+2*pb*pc*ab+pc*pc*bb),axis=1)


class Data:
    def __init__(self,level,ph,e,mode,audit=False):
        _,_,order,na,nr,*_=level
        raw=[];ref_rows=[];bases=[];weights=[];orient=[];blocks=[];pairs=[];nx=0
        self.center=np.array([m.section_center(order),0.,0.])
        for chart,(ss,vv) in zip(CHARTS,axes(level,ph,audit)):
            kind=chart if chart=="cylinder" else chart[:-1]
            side=1 if chart.endswith("+") else -1
            shape=ss.shape;s,v=ss.ravel(),vv.ravel()
            cur=geom.chart_jet(chart,s,v,ph,order,e,False)
            ref=geom.chart_jet(chart,s,v,0.,order,e,False)
            a,b=ref[:,1],ref[:,2];l=np.linalg.norm(a,axis=1);t=a/l[:,None]
            proj=np.einsum("ij,ij->i",b,t);perp=np.linalg.norm(b-proj[:,None]*t,axis=1)
            if np.any((l<=0)|(perp<=0)):
                raise ArithmeticError("singular original material chart")
            pa=1/l[:,None];pc=1/perp[:,None];pb=-proj[:,None]*pa*pc
            raw.append(linjet(cur,pa,pb,pc));ref_rows.append(linjet(ref,pa,pb,pc))
            for lo in range(0,len(s),144):
                sl=slice(lo,lo+144);h=basis(chart,s[sl],v[sl],order,mode,na,nr,ref[sl])
                h=linjet(h,pa[sl],pb[sl],pc[sl]);bases.append(csr_matrix(h.reshape(-1,h.shape[-1])))
            sign=1 if kind=="cylinder" else side*(-1 if kind in ("cap","cap-cartesian") else 1)
            orient.append(np.full(len(s),sign));weights.append(np.full(len(s),1/np.sqrt(len(s))))
            blocks.append((chart,nx,nx+len(s)))
            if kind=="preband":
                ids=nx+np.arange(len(s)).reshape(shape);pairs.extend(zip(ids[:,0],ids[:,-1]))
            nx+=len(s)
        self.base=np.concatenate(raw);self.h=vstack(bases,format="csr");self.ref=np.concatenate(ref_rows)
        self.w=np.concatenate(weights);self.ori=np.concatenate(orient);self.blocks=blocks
        self.p=self.h.shape[-1];self.cache_key=None;self.saved=None
        self.i,self.j=np.asarray(pairs).T
        point=geom.chart_jet("cylinder",0.,0.,0.,order,e,False)[0]
        ox,oz=m.axis(order);c,h=np.cos(ph),np.sin(ph);dx,dz=point[0]-ox,point[2]-oz
        self.witness=np.array([ox+c*dx+h*dz,point[1],oz-h*dx+c*dz]);self.held=.878*(ph/.90)**2

    def state(self,x):
        key=x.tobytes()
        if key==self.cache_key:
            return self.saved
        field=self.base+(self.h@x.reshape(self.p,3)).reshape(-1,6,3)
        f,a,b,h11,h12,h22=np.moveaxis(field,1,0)
        dot=lambda x,y:np.einsum("ni,ni->n",x,y)
        cr=np.cross(a,b);area=np.linalg.norm(cr,axis=1)
        normal=self.ori[:,None]*cr/np.maximum(area,1e-14)[:,None]
        aa,ab,bb=dot(a,a),dot(a,b),dot(b,b)
        g=np.stack((aa,ab,ab,bb),axis=-1).reshape(-1,2,2)
        n11,n12,n22=(dot(z,normal) for z in (h11,h12,h22))
        ii=np.stack((n11,n12,n12,n22),axis=-1).reshape(-1,2,2)
        middle=f-self.center;support=dot(middle,normal)
        res=np.zeros((len(f),7));der=np.zeros((len(f),7,6,3))
        res[:,:3]=np.stack((aa-1,np.sqrt(2)*ab,bb-1),axis=-1)
        der[:,0,1]=2*a;der[:,1,1]=np.sqrt(2)*b;der[:,1,2]=np.sqrt(2)*a;der[:,2,2]=2*b
        def normder(val):
            tang=(val-dot(val,normal)[:,None]*normal)*(self.ori/np.maximum(area,1e-14))[:,None]
            return np.cross(b,tang),np.cross(tang,a)
        for ix,sgn in ((3,1.),(4,-1.)):
            values,vec=np.linalg.eigh(KMAX*g+sgn*ii)
            u=vec[:,0,0];v=vec[:,1,0]
            active=(values[:,0]<0)*(.18/KMAX)
            res[:,ix]=np.maximum(0.,-values[:,0])*(.18/KMAX)
            u,v=u[:,None],v[:,None]
            tangent=u*a+v*b;curv=u*u*h11+2*u*v*h12+v*v*h22
            na,nb=normder(curv);mult=-active[:,None]
            der[:,ix,1]=mult*(2*KMAX*u*tangent+sgn*na)
            der[:,ix,2]=mult*(2*KMAX*v*tangent+sgn*nb)
            der[:,ix,3]=mult*sgn*u*u*normal;der[:,ix,4]=mult*sgn*2*u*v*normal
            der[:,ix,5]=mult*sgn*v*v*normal
        active=(support<RMIN)*.30
        res[:,5]=.30*np.maximum(0.,RMIN-support);na,nb=normder(middle)
        der[:,5,0]=-active[:,None]*normal;der[:,5,1]=-active[:,None]*na;der[:,5,2]=-active[:,None]*nb
        diff=f-self.witness;length=np.linalg.norm(diff,axis=1)
        res[:,6]=.45*np.maximum(self.held-length,0.)
        der[:,6,0]=-.45*(length<self.held)[:,None]*diff/np.maximum(length,1e-14)[:,None]
        self.cache_key=key;self.saved=(field,g,ii,support,area,res,der)
        return self.saved

    def fun(self,x):
        field,_,_,_,_,res,_=self.state(x)
        excess=np.maximum(0.,np.linalg.norm(field[self.j,0]-field[self.i,0],axis=1)-E)
        return np.r_[(self.w[:,None]*res).ravel(),excess/np.sqrt(len(self.i)),.0002*x]

    def jac(self,x):
        field,*_,der=self.state(x);der=der*self.w[:,None,None,None]
        d=field[self.j,0]-field[self.i,0];dd=np.linalg.norm(d,axis=1)
        unit=(dd>E)[:,None]*d/(np.sqrt(len(d))*np.maximum(dd,1e-14)[:,None])
        p=self.p;h=self.h
        def mv(y):
            col=np.asarray(y).ravel()
            df=(h@col.reshape(p,3)).reshape(-1,6,3)
            chords=np.einsum("ij,ij->i",unit,df[self.j,0]-df[self.i,0])
            return np.r_[np.einsum("nkac,nac->nk",der,df).ravel(),chords,.0002*col]
        def rv(y):
            row=np.asarray(y).ravel();cnt=7*len(self.base);body=row[:cnt].reshape(-1,7)
            normal=np.einsum("nk,nkac->nac",body,der)
            dq=unit*row[cnt:cnt+len(self.i),None]
            np.add.at(normal[:,0],self.i,-dq);np.add.at(normal[:,0],self.j,dq)
            force=h.T@normal.reshape(-1,3)
            return force.ravel()+.0002*row[-3*p:]
        return LinearOperator((len(self.base)*7+len(self.i)+3*p,3*p),matvec=mv,rmatvec=rv,dtype=np.float64)

    def result(self,x):
        field,g,ii,support,area,_,_=self.state(x)
        sig=np.linalg.svd(field[:,1:3,:],compute_uv=False)
        _,s,vt=np.linalg.svd(np.swapaxes(field[:,1:3],1,2),full_matrices=False)
        den=s[:,:,None]*s[:,None,:]
        cost=np.linalg.eigvalsh((vt@ii@np.swapaxes(vt,1,2))/np.maximum(den,1e-24))
        metric=np.max(np.abs(np.linalg.eigvalsh(g-np.eye(2))),axis=1)
        kk=np.max(np.abs(cost),axis=1)
        values={}
        for key,i,j in self.blocks:
            values[key]=[j-i,int(np.count_nonzero(sig[i:j,1]<=1e-12*sig[i:j,0])),
                float(np.max(metric[i:j])),float(np.max(kk[i:j])),float(np.min(support[i:j])),
                float(np.min(area[i:j])),*[float(np.max(np.abs(v[i:j]))) for v in (g[:,0,0]-1,g[:,0,1],g[:,1,1]-1)]]
        return {"charts":values,"held_witness_min_sample":float(np.min(np.linalg.norm(field[:,0]-self.witness,axis=1))),
            "max_preband_endpoint_chord_minus_initial_path":float(np.max(np.linalg.norm(field[self.j,0]-field[self.i,0],axis=1))-E)}



def prolong(x,old_dims,dims):
    na,nr=dims;ans=np.zeros((FEATURES+3*na*(nr+3),3))
    if x is None:
        return ans
    a,r=old_dims;ans[:FEATURES]=x[:FEATURES]
    coarse=x[FEATURES:].reshape(3,a,r+3,3);fine=ans[FEATURES:].reshape(3,na,nr+3,3)
    mask=np.array([1,4,6,4,1])/8
    for i in range(a):
        for j in range(-1,r+2):
            for di,wi in zip(range(-2,3),mask):
                for dj,wj in zip(range(-2,3),mask):
                    jj=2*j+dj
                    if -1<=jj<=nr+1:
                        fine[:,(2*i+di)%na,jj+1]+=wi*wj*coarse[:,i,j+1]
    return ans


def field(chart,s,v,ph,level,e,mode,coeff,rotate=False):
    order,na,nr=level[2:5]
    s,v=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float));shape=s.shape;s,v=s.ravel(),v.ravel()
    cur=geom.chart_jet(chart,s,v,ph,order,e,False)
    if coeff is not None:
        for lo in range(0,len(s),128):
            sl=slice(lo,lo+128);ref=geom.chart_jet(chart,s[sl],v[sl],0.,order,e,False)
            h=basis(chart,s[sl],v[sl],order,mode,na,nr,ref)
            cur[sl]+=h@coeff
    if rotate:
        ox,oz=m.axis(order);c,h=np.cos(ph),np.sin(ph)
        x,z=cur[:,:,0].copy(),cur[:,:,2].copy();x[:,0]-=ox;z[:,0]-=oz
        cur[:,:,0]=c*x-h*z;cur[:,:,2]=h*x+c*z;cur[:,0,0]+=ox;cur[:,0,2]+=oz
    return cur.reshape(shape+(6,3))


def interpolated(folder,idx,ph):
    ip=max(0,min(len(PHASES)-2,np.searchsorted(PHASES,ph,side="right")-1))
    t=(ph-PHASES[ip])/(PHASES[ip+1]-PHASES[ip]);w=t**3*(10+t*(-15+6*t))
    get=lambda j:np.fromfile(Path(folder)/f"level{idx}-phase{j}.f64",dtype="<f8").reshape(-1,3)
    return (1-w)*get(ip)+w*get(ip+1)


def fitted_chart_jet(chart,s,v,phase,level,retreat,mode,folder,rotate=True):
    return field(chart,s,v,phase,LEVELS[level],retreat,mode,interpolated(folder,level,phase),rotate)


def volumes(level,idx,ph,e,mode,x):
    order=level[2];n=(48,72,112)[idx];degree=(6,9,12)[idx]
    half=old.material(order,True)[-1];s=(np.arange(n)+.5)*2*half/n
    nodes,weights=np.polynomial.legendre.leggauss(degree)
    costs=np.zeros(2)
    for chart in ("cylinder","preband+","round+","cap+","preband-","round-","cap-"):
        kind=chart if chart=="cylinder" else chart[:-1]
        side=1 if chart.endswith("+") else -1
        cuts={"cylinder":(-B,-.7,0.,.33,.70,B),"preband":(0.,E/4,E/2,3*E/4,E),
              "round":(0.,m.END_E,L/2,L-m.END_E,L),"cap":(0.,.82*(1-old.JOIN),.86*(1-old.JOIN),
              .87*(1-old.JOIN),.97*(1-old.JOIN),1-old.WIDTH-old.ROUND,1-old.WIDTH,1.)}[kind]
        sign=1 if kind=="cylinder" else side*(-1 if kind=="cap" else 1)
        vv=np.concatenate([(a+b+(b-a)*nodes)/2 for a,b in zip(cuts[:-1],cuts[1:])])
        ww=np.concatenate([(b-a)*weights/2 for a,b in zip(cuts[:-1],cuts[1:])])
        ss,v=np.meshgrid(s,vv,indexing="ij")
        for j,coef in enumerate((None,x)):
            f=field(chart,ss,v,ph,level,e,mode,coef)
            integrand=f[...,0,1]*np.cross(f[...,1,:],f[...,2,:])[...,1]
            costs[j]+=sign*(2*half/n)*np.sum(integrand@ww)
    return costs.tolist()


def write(path,rec):
    data=(json.dumps(rec,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
    path.write_bytes(data)
    return [len(data),sha256(data).hexdigest()]


def solve(mode,e,folder):
    previous={}
    for idx,level in enumerate(LEVELS):
        na,nr=level[3:5];nfev,it=level[5:7];coeff={};rows=[];mid=[]
        for ip,ph in enumerate(PHASES):
            d=Data(level,ph,e,mode)
            seed=prolong(previous.get(ip),LEVELS[idx-1][3:5] if idx else None,(na,nr))
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
            a=Data(level,ph,e,mode,True);audit=a.result(x.ravel());del a
            raw=np.asarray(x,dtype="<f8").tobytes()
            (folder/f"level{idx}-phase{ip}.f64").write_bytes(raw);coeff[ip]=x
            rows.append({"phase":ph,"seed":before,"fit":fit,"independent":audit,"status":status,
                        "coeff":[len(raw),sha256(raw).hexdigest()],"volumes":volumes(level,idx,ph,e,mode,x)})
            print("R764 physical whole sphere",mode,e,idx,ph,status,flush=True)
        for j,(l,r) in enumerate(zip(PHASES[:-1],PHASES[1:])):
            ph=(l+r)/2;x=(coeff[j]+coeff[j+1])/2
            a=Data(level,ph,e,mode,True);res=a.result(x.ravel());del a
            mid.append([ph,res,volumes(level,idx,ph,e,mode,x)])
        report={"schema":"R764-complete-single-resolution-whole-sphere-physical-fit-v1","mode":mode,
             "e":e,"level":idx,"grid":level,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R764_SOURCE_COMMIT"],"rules_read_commit":os.environ["R764_RULES_COMMIT"],
             "fitted":rows,"intermediate":mid,"legacy_fixed_metric_prices":geom.legacy_prices(level[2]),
             "chart_columns":["points","nearly_singular","relative_metric_op","max_abs_principal",
             "min_support","min_relative_area","max_abs_frame11","max_abs_frame12","max_abs_frame22"],
             "volume_columns":["uncorrected_signed_flux","fitted_signed_flux"],
             "volume_angular_radial_order":[(48,72,112)[idx],(6,9,12)[idx]]}
        meta=write(folder/f"stage-{idx}.json",report);print("R764 complete resolution",idx,meta,flush=True)
        previous=coeff


if __name__=="__main__":
    arg=argparse.ArgumentParser(description=__doc__)
    arg.add_argument("--mode",choices=("rigid_caps","fully_free"),required=True)
    arg.add_argument("--retreat",type=float,choices=geom.ENDS,required=True)
    arg.add_argument("--folder",type=Path,required=True);v=arg.parse_args()
    m.old.disk._public();v.folder.mkdir(exist_ok=True,parents=True);solve(v.mode,v.retreat,v.folder)
