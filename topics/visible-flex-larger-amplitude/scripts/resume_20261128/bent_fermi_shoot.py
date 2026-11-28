"""Differentiable full-circle surface-geodesic and Jacobi shooting in the actual roll chart."""
import jax
jax.config.update("jax_enable_x64",True)
import jax.numpy as j
from jax import lax
from jax.scipy.special import logsumexp
import numpy as np
from r742_tilted_disk_two_jets import J
from bent_body_atlas import profile_nodes

def dot(a,b):return j.sum(a*b,axis=-1)
def positive(x):return j.maximum(x,0.)
def penalty(x):return 2*(j.sqrt(1+x*x)-1)

def geometry(F):
    a,b=F[...,1,:],F[...,2,:]
    e,c,g=dot(a,a),dot(a,b),dot(b,b)
    n=j.cross(a,b);det=dot(n,n);safe=j.maximum(det,1.e-16)
    unit=n/j.sqrt(safe)[...,None]
    s=F[...,3:6,:]
    da=j.sum(a[...,None,:]*s,axis=-1);db=j.sum(b[...,None,:]*s,axis=-1)
    pa=(g[...,None]*da-c[...,None]*db)/safe[...,None]
    pb=(e[...,None]*db-c[...,None]*da)/safe[...,None]
    ii=j.sum(s*unit[...,None,:],axis=-1)
    K=(ii[...,0]*ii[...,2]-ii[...,1]**2)/safe
    H=(g*ii[...,0]-2*c*ii[...,1]+e*ii[...,2])/(2*safe)
    princ=j.sqrt(H*H+1.e-20)+j.sqrt(j.maximum(1.e-20,H**2-K))
    data=j.concatenate([j.stack([e,c,g],axis=-1),pa,pb,K[...,None]],axis=-1)
    return data,princ,unit,det

class Shoot:
    def __init__(self,m,cfg,verify=False):
        self.m=m;self.cfg=cfg;P=2*m.g.profile_constants(32)[4];L=m.delay.END_LENGTH
        self.P,self.L=P,L
        U=np.asarray(m.polar);V=np.unique(m.xy[m.roll[0],1]);self.U,self.V=U,V
        if np.any(np.diff(U)<=0):raise ValueError("angular field table must increase")
        angles=profile_nodes(m.g,cfg["check_rays"] if verify else cfg["rays"],.319 if verify else 0.)
        angles=np.unique(np.r_[0.,angles]);self.launch=angles
        nsteps=cfg["check_steps"] if verify else cfg["steps"]
        bb=np.unique(np.r_[V,np.linspace(0,L,nsteps+1)])
        self.clock=bb
        def locations(x):
            lo=np.clip(np.searchsorted(V,x,side="right")-1,0,len(V)-2)
            return lo,(x-V[lo])/(V[lo+1]-V[lo])
        il,wl=locations(bb[:-1]);im,wm=locations(.5*(bb[1:]+bb[:-1]));ir,wr=locations(bb[1:])
        schedule=j.asarray(np.column_stack([il,wl,im,wm,ir,wr,np.diff(bb)]))
        old=m.g
        dgrid=np.unique(np.r_[np.linspace(0,L,2049),V]);djet=m.delay.end_offsets(J(dgrid,s=1.),32)[1];dtab=djet.v
        ac=np.unique(np.r_[np.linspace(0,P,4097),U,P])
        av=m.ar.angular_data(ac,32)[0];db=m.delay.end_limits(32)[1]
        k0=j.asarray(old.profile_coordinates(angles)[3]);a0=j.asarray(angles)
        ug=j.asarray(U);ugext=j.asarray(np.r_[U,U[0]+P]);ag=j.asarray(ac);tg=j.asarray(av)
        dg=j.asarray(dgrid);dt=j.asarray(dtab);dp=j.asarray(djet.s);ddp=j.asarray(djet.ss)
        index=[(sl.start,sl.stop) for sl in m.roll]
        center=j.asarray(m.center);sign=j.asarray(m.sign);weights=j.asarray(m.weight**2)
        ginit=m.g0;dd0=j.asarray(np.maximum(ginit[0]*ginit[2]-ginit[1]**2,1.e-16))
        n=len(angles);dom=float(cfg["slope_guard"]);vbound=float(cfg["acceleration_guard"])
        cap_j=float(cfg["jacobi_guard"]);cap_q=cap_j*4
        def angular(table,grid,a,iv,w):
            def each(data,q):
                def layer(i):
                    lo=grid[:,i];ext=j.concatenate((lo,lo[:1]+P));x=j.mod(q-lo[0],P)+lo[0]
                    id=j.clip(j.searchsorted(ext,x,side="right")-1,0,len(U)-1)
                    vd=(x-ext[id])/(ext[id+1]-ext[id]);up=(id+1)%len(U)
                    return (1-vd[:,None])*data[id,i]+vd[:,None]*data[up,i]
                return (1-w)*layer(iv)+w*layer(iv+1)
            return jax.vmap(each)(table,a)
        def rhs(table,grid,x,iv,w):
            c=angular(table,grid,x[:,:,0],iv,w)
            raw=x[:,:,1];p=j.clip(raw,-dom,dom)
            e,h,g=c[:,:,0],c[:,:,1],c[:,:,2]
            dotp=p*(c[:,:,6]*p*p+2*c[:,:,7]*p+c[:,:,8])-(c[:,:,3]*p*p+2*c[:,:,4]*p+c[:,:,5])
            vel=j.sqrt(j.maximum(e*p*p+2*h*p+g,1.e-16))
            jj=j.clip(x[:,:,3],-cap_j,cap_j);qq=j.clip(x[:,:,4],-cap_q,cap_q)
            guard=j.maximum(j.maximum(abs(raw)/dom,abs(dotp)/vbound),
                            j.maximum(abs(x[:,:,3])/cap_j,abs(x[:,:,4])/cap_q))
            return j.stack((p,j.clip(dotp,-vbound,vbound),vel,vel*qq,-vel*c[:,:,9]*jj),axis=-1),guard
        def run(F,xi,advance):
            geom,princ,nrm,det=geometry(F)
            grid=xi[:,:,0];su,sv,suu,suv,svv=[xi[:,:,i][None,:,:,None] for i in range(1,6)]
            au=1/su;av=-sv/su;auu=-suu*au**2/su
            auv=-(suu*au*av+suv*au)/su;avv=-(suu*av**2+2*suv*av+svv)/su
            jet=j.stack([F[i:k].reshape(len(U),len(V),6,3) for i,k in index])
            f,fa,fb,faa,fab,fbb=[jet[:,:,:,i] for i in range(6)]
            Q=j.stack([f,fa*au,fa*av+fb,faa*au**2+fa*auu,
                faa*au*av+fab*au+fa*auv,faa*av**2+2*fab*av+fbb+fa*avv],axis=-2)
            table=geometry(Q)[0]
            zero=j.zeros((2,n));angs=j.broadcast_to(a0+advance,(2,n))
            ic=angular(table,grid,angs,0,0.)
            initial=j.stack((angs,-ic[:,:,1]/j.maximum(ic[:,:,0],1.e-14),zero,zero+1,zero),axis=-1)
            def step(x,s):
                il,wl,im,wm,ir,wr,h=s
                k1,r1=rhs(table,grid,x,il.astype(int),wl)
                k2,r2=rhs(table,grid,x+.5*h*k1,im.astype(int),wm)
                if verify:
                    k3,r3=rhs(table,grid,x+.5*h*k2,im.astype(int),wm)
                    k4,r4=rhs(table,grid,x+h*k3,ir.astype(int),wr)
                    nxt=x+h*(k1+2*k2+2*k3+k4)/6
                    guard=j.maximum(j.maximum(r1,r2),j.maximum(r3,r4))
                else:
                    nxt=x+h*k2;guard=j.maximum(r1,r2)
                return nxt,(nxt,guard)
            last,(track,guard)=lax.scan(step,initial,schedule)
            track=j.concatenate((initial[None],track),axis=0)
            T=last[:,:,2];land=last[:,:,0]
            normalized=L*track[:,:,:,2]/j.maximum(T,1.e-12)
            desired=1-j.interp(normalized,dg,dt)*k0[None,None,:]
            jrel=track[:,:,:,3]/j.maximum(desired,.1)-1
            qerr=(T/L)[None,:,:]*track[:,:,:,4]+k0[None,None,:]*j.interp(normalized,dg,dp)
            ki=j.concatenate((j.asarray([il[0]]),j.asarray(ir)));kw=j.concatenate((j.asarray([wl[0]]),j.asarray(wr)))
            rayK=jax.vmap(lambda st,ip,bw:angular(table,grid,st[:,:,0],ip,bw)[:,:,9])(track,ki,kw)
            kerr=(T/L)[None,:,:]**2*rayK*track[:,:,:,3]-k0[None,None,:]*j.interp(normalized,dg,ddp)
            def omega(a):
                lap=j.floor(a/P);v=a-lap*P
                return a-db*(2*j.pi*lap+j.interp(v,ag,tg))
            shift=omega(land)-omega(a0)[None,:]
            shift=shift-(P-2*j.pi*db)*j.round(shift/(P-2*j.pi*db))
            # A periodic lift has strictly positive successive angular increments
            # at each b if these finite sampled neighbors have not crossed.
            lifted=track[:,:,:,0]
            spacing=j.diff(j.concatenate((a0,a0[:1]+P)))
            ratio=j.diff(j.concatenate((lifted,lifted[:,:,:1]+P),axis=2),axis=2)/spacing
            sup=sign*dot(F[:,0]-center,nrm)
            return track,guard,jrel,T,shift,ratio,princ,sup,det/dd0,qerr,kerr
        def loss(F,xi,advance):
            tr,guard,jr,T,shift,ratio,k,sup,area,qr,kr=run(F,xi,advance)
            # Angular errors are counted on both full circles. The anchor is also
            # given its own row. Integration guard proposals incur a separate cost.
            temporal=j.asarray(np.r_[np.diff(bb)/2,0]+np.r_[0,np.diff(bb)/2])/L
            jl=j.sum(temporal*j.mean(penalty(jr),axis=(1,2)))
            geom=j.sum(weights*(cfg["bend_weight"]*penalty(positive(k/cfg["curvature_cap"]-1))+
                cfg["support_weight"]*penalty(positive(cfg["support_goal"]-sup))+
                cfg["area_weight"]*penalty(positive(.55-area))))/j.sum(weights)
            def tail(x,rho):
                return (logsumexp(rho*x)-j.log(x.size))/rho
            geom+=cfg["geometry_peak_weight"]*(penalty(tail(positive(k/cfg["curvature_cap"]-1),3.))+
                         penalty(tail(positive((cfg["support_goal"]-sup)/.055),4.)))
            jl+=cfg["angular_peak_weight"]*penalty(tail(j.sqrt(jr*jr+1.e-20),3.))
            return (jl+cfg["jacobi_derivative_weight"]*j.sum(temporal*j.mean(penalty(qr/3),axis=(1,2)))+
                cfg["curvature_density_weight"]*j.sum(temporal*j.mean(penalty(kr/24),axis=(1,2)))+cfg["length_weight"]*j.mean(penalty(T/L-1))+
                cfg["landing_weight"]*j.mean(penalty(shift/.3))+
                .18*j.mean(penalty(shift[:,0]/.3))+geom+
                4*j.mean(penalty(positive(.12-ratio)))+8*j.mean(penalty(positive(.12-tr[:,:,:,3])))+
                8*j.mean(penalty(positive(guard-.85))))
        self._forward=jax.jit(run)
        self._value_grad=jax.jit(jax.value_and_grad(loss,argnums=0))
        self.bound=None
    def bind(self,d,t):
        key=(d["method"],float(t))
        if key==self.bound:return
        self.bound=key;data=self.m.entry(d,float(t))[1]
        S=next(row[2] for row in data if row[0]=="end+")
        self.xi=np.stack(np.broadcast_arrays(*S.parts()),axis=-1).reshape(len(self.U),len(self.V),6)
        self.advance=.15*float(t)
    def forward(self,F):
        return self._forward(F,self.xi,self.advance)
    def value_grad(self,F):
        return self._value_grad(F,self.xi,self.advance)
    def raw_track(self,tr):
        # Convert shooting coordinates back to the actual raw material label,
        # with the exact R747 lifted inverse on each ray and b, for the closed fit.
        m=self.m;method,t=self.bound;B=np.asarray(self.clock)
        g=m.src.transport_weight(J(B),method).v[:,None,None]
        S=tr[:,:,:,0];out=tr.copy()
        if method=="legacy":out[:,:,:,0]=S-.15*t*g;return out
        d=m.delay.end_offsets(J(B),32)[1].v[:,None,None]
        shift=t*(.15-d)*g;theta=m.ar.angular_data(S.ravel(),32)[0].reshape(S.shape)
        target=S-d*theta-shift;lo=S-shift/.26;hi=S.copy();a=np.maximum(lo,np.minimum(hi,S-shift))
        for _ in range(50):
            ang,k,_=m.ar.angular_data(a.ravel(),32)
            err=a-d*ang.reshape(a.shape)-target;ok=abs(err)<8.e-14*(1+abs(a))
            if np.all(ok):break
            lo=np.where((err<0)&~ok,a,lo);hi=np.where((err>0)&~ok,a,hi)
            nr=a-err/(1-d*k.reshape(a.shape));nr=np.where((nr>lo)&(nr<hi),nr,(lo+hi)/2)
            a=np.where(ok,a,nr)
        out[:,:,:,0]=a;return out
    def read(self,f,return_paths=False):
        tr,guard,jr,T,sh,rat,k,su,ar,qr,kr=[np.asarray(x) for x in self.forward(f)]
        def at(q,low=False):
            ii=np.unravel_index((np.argmin(q) if low else np.argmax(q)),q.shape)
            return {"value":float(q[ii]),"b":float(self.clock[ii[0]]),"side":1 if ii[1]==0 else -1,
                    "start_s":float(self.launch[ii[2]])}
        z={"max_relative_J":at(abs(jr)),"minimum_J":at(tr[:,:,:,3],True),"minimum_angular_increment_ratio":at(rat,True),
           "max_Jacobi_derivative_error":at(abs(qr)),"max_Gaussian_density_error":at(abs(kr)),
           "min_T":float(T.min()),"max_T":float(T.max()),"max_abs_T_minus_L":float(abs(T-self.L).max()),
           "max_rim_arclength_mismatch":float(abs(sh).max()),"two_anchor_offsets":sh[:,0].tolist(),
           "guard_ratio_max":float(guard.max()),"guarded_stage_ray_entries":int((guard>1.).sum()),
           "ray_count_per_end":len(self.launch),"radial_nodes":len(self.clock),
           "max_raw_K":float(k.max()),"min_raw_support":float(su.min()),"min_raw_relative_area_squared":float(ar.min())}
        return (z,self.raw_track(tr)) if return_paths else z

    def baseline_test(self,d,t):
        self.bind(d,t)
        raw=self.m.entry(d,t)[0]
        tr,guard,*_=[np.asarray(x) for x in self.forward(raw)]
        offset=self.m.delay.end_offsets(J(self.clock,s=1.),32)[1]
        k=self.m.g.profile_coordinates(self.launch+.15*t)[3]
        J0=1-offset.v[:,None]*k[None,:];Q0=-offset.s[:,None]*k[None,:]
        final=tr[-1,:,:,0]-self.launch[None,:]-.15*t
        final-=self.P*np.round(final/self.P)
        return {"phase":float(t),"max_true_length_error":float(abs(tr[:,:,:,2]-self.clock[:,None,None]).max()),
                "max_true_J_error":float(abs(tr[:,:,:,3]-J0[:,None,:]).max()),
                "max_true_Q_error":float(abs(tr[:,:,:,4]-Q0[:,None,:]).max()),
                "max_true_landing_label_error":float(abs(final).max()),
                "guard_max":float(guard.max())}
