"""R752/R753 true material atlas and hard geometry plus nested C2 roll directions."""
from collections import OrderedDict
import numpy as np
from bent_body_atlas import profile_nodes
from bent_end_phase_fields import scalar,unary,mul,cheb,metric
from r742_tilted_disk_two_jets import J,gather,cap_s7

HARD=19
def hshape(src,d,q):
    z=np.tanh(q)
    def fan(i,plus):
        first=(d["upper_cubic"]+.028*(1+z[i])) if plus else d["lower_cubic"]+.055*z[i]
        return (first,.12*z[i+1],.065*z[i+2])
    def pose(i,side):
        val=np.r_[.85*z[i:i+3],.35*z[i+3:i+6]]
        val[4]+=side*d["cap_y"]
        return tuple(val)
    return src.Shape(d["middle"]+(2.**-21-abs(d["middle"]))*z[0],
                     fan(1,True),fan(4,False),pose(7,1),pose(13,-1))

def posjet(a,i):
    return J(*a[:,:,i].T)

class Mesh:
    def __init__(self,src,n,off):
        self.src=src;self.delay=src.delay;self.ar=src.ar;self.g=src.OLD
        g=self.g;r=self.delay;U=profile_nodes(g,n[0],off)
        def levels(lo,hi,m):
            x=np.linspace(lo,hi,m)
            return np.r_[lo,.63*x[:-1]+.37*x[1:],hi] if off else x
        Y=np.unique(np.r_[levels(-r.HALF_WIDTH,r.HALF_WIDTH,n[1]),0.,-.36,.36])
        v0=levels(0,g.END_LENGTH,n[2]);b=r.SMALL_ANGLE
        # Include the small old v0 ramp and both sides of the true change of variable.
        fine=r.clock_at(np.array([0.,.000025,.00005,.00010,.000125,.00015,.000175,
                                 .0002,.00025,.00035,.0005,.0008,.001,g.END_LENGTH-.0005]))
        V=np.unique(np.r_[levels(0,r.END_LENGTH,n[2]),r.clock_at(v0),fine,r.END_LENGTH])
        W=np.unique(np.r_[levels(0,1,n[3])[1:],.007,.035,.25,.5,.75,.99925,.9995,.99975,.9999])
        self.cases=[];self.center=np.array([g.CENTER_X,0.,0.]);self.polar=U
        F=[];lab=[];loc=[];sign=[];weight=[];start=0
        for label,z,sg in (("cylinder",Y,1),("end+",V,1),("end-",V,-1),("cap+",W,-1),
                           ("cap-",W,1),("cap-cartesian+",[0],-1),("cap-cartesian-",[0],1)):
            if "cartesian" in label:
                u=np.array([g.CENTER_X,g.CENTER_X-.012,g.CENTER_X+.012,g.CENTER_X,g.CENTER_X])
                v=np.array([0.,-.001,.001,-.00002,.00002])
            else:
                u,v=np.meshgrid(U,z,indexing="ij");u=u.ravel();v=v.ravel()
            ff=r.chart_jet(label,u,v,0.,bend=0.,rotate=False)
            stop=start+len(u);self.cases.append((label,u,v,slice(start,stop)));start=stop
            F.append(ff);loc.append(np.c_[u,v]);lab.extend([label]*len(u));sign.extend([sg]*len(u))
            weight.extend([np.sqrt((.008 if "cartesian" in label else 1.)/len(u))]*len(u))
        self.f0=np.concatenate(F);self.xy=np.concatenate(loc);self.g0=metric(self.f0);self.lab=np.array(lab)
        self.sign=np.array(sign);self.weight=np.array(weight);self.cache=OrderedDict()
        self.fan_cache=OrderedDict();self.pose_cache=OrderedDict()
        self.roll=[next(j for label,u,v,j in self.cases if label=="end"+side) for side in ("+","-")]
    def name(self,i):
        return {"chart":str(self.lab[i]),"u":float(self.xy[i,0]),"v":float(self.xy[i,1]),"index":int(i)}
    def entry(self,d,t):
        key=(d["method"],float(t))
        if key in self.cache:
            self.cache.move_to_end(key);return self.cache[key]
        src=self.src;r=self.delay;data=[];raw=[]
        for label,u,v,ind in self.cases:
            a,b=J(u,s=1.),J(v,a=1.);ph=np.full(len(u),t);sg=1 if label.endswith("+") else -1
            if label=="cylinder":
                S=a+src.R*t;y=b;q,n=self.g.profile(S,32);x,z=q;w=J(0.)
            elif label.startswith("end"):
                w=cap_s7(b/r.END_LENGTH);gate=src.transport_weight(b,d["method"])
                p,D=r.end_offsets(b,32);y=sg*(r.HALF_WIDTH+p)
                S=a+src.R*t*gate if d["method"]=="legacy" else self.ar.angular_shift(a,D,ph,gate,32)
                q,n=self.g.profile(S,32);x,z=[q[k]-D*n[k] for k in range(2)]
            else:
                w=J(1.);S=None;q=None
                x,y,z=[posjet(self.f0[ind],k) for k in range(3)]
            raw.append(gather((x,y,z),len(u)))
            data.append((label,ind,S,q,y,x,z,w,ph,sg))
        out=(np.concatenate(raw),data);self.cache[key]=out
        if len(self.cache)>2:self.cache.popitem(last=False)
        return out
    def fan_part(self,d,t,shape,sg,data):
        coeff=shape.plus if sg==1 else shape.minus
        pose=shape.plus_pose if sg==1 else shape.minus_pose
        key=(d["method"],float(t),sg);fk=(key,tuple(coeff))
        if key not in self.pose_cache:
            terms=[]
            for label,ind,S,q,y,x,z,w,ph,side in data:
                if label=="cylinder" or side!=sg:continue
                wp=np.stack(np.broadcast_arrays(*w.parts(),ph)[:6],axis=1)
                base=gather((w*(x-self.g.CENTER_X),w*0.,w*z),len(ph))
                terms.append((ind,wp,base,x,z,w,ph))
            self.pose_cache[key]=terms
            if len(self.pose_cache)>4:self.pose_cache.popitem(last=False)
        terms=self.pose_cache[key]
        if fk not in self.fan_cache:
            fans=[]
            for ind,wp,base,x,z,w,ph in terms:
                delta=self.src.fan_delta(x,z,coeff,ph,32)
                fans.append(gather(tuple(w*j for j in delta),len(ph)))
            self.fan_cache[fk]=fans
            if len(self.fan_cache)>10:self.fan_cache.popitem(last=False)
        self.fan_cache.move_to_end(fk)
        a=np.asarray(pose[:3]);mag=np.linalg.norm(a);time=np.sin(t);rot=np.eye(3)
        if mag:
            i,j,k=a/mag;K=np.array([[0.,-k,j],[k,0.,-i],[-j,i,0.]])
            rot+=np.sin(time*mag)*K+2*np.sin(time*mag/2)**2*(K@K)
        out=np.zeros_like(self.f0)
        for (ind,wp,base,x,z,w,ph),fan in zip(terms,self.fan_cache[fk]):
            out[ind]=fan@rot.T+base@(rot-np.eye(3)).T+wp[:,:,None]*(time*np.asarray(pose[3:]))
        return out
    def part(self,d,t,h,part):
        src=self.src;shape=hshape(src,d,h);raw,data=self.entry(d,t)
        if part!="central":return self.fan_part(d,t,shape,part,data)
        out=np.zeros_like(raw)
        for label,ind,S,q,y,x,z,w,ph,sg in data:
            if S is None:continue
            amp=shape.middle*np.sin(t);xx=q[0].v
            live=(xx>src.LEFT)&(xx<src.RIGHT);left=xx<=src.LEFT
            if np.any(left):
                nodes,weights=src.gauss(32);delta=src.LEFT-src.RIGHT
                bs=src.bend(src.RIGHT+delta*(nodes+1)/2,amp)[0]
                dx=-delta*np.dot(np.sin(bs/2)**2,weights);dy=.5*delta*np.dot(np.sin(bs),weights)
                fade=1-w
                for j,z0 in enumerate([dx,dy,0.]):
                    jet=fade*z0
                    vals=np.broadcast_arrays(*jet.parts(),ph)[0:6]
                    out[ind][left,:,j]=np.stack(vals,axis=-1)[left]
            if np.any(live):
                cut=lambda f:src.OLD.slice_j(f,live)
                c=src.cylinder(cut(S),cut(y),np.full(live.sum(),amp),32)
                out[ind][live]=gather(tuple((1-cut(w))*(u-cut(v)) for u,v in zip(c,(q[0],y,q[1]))),int(live.sum()))
        return out
    def at(self,d,t,h=None):
        if h is None:h=np.zeros(HARD)
        raw,_=self.entry(d,t)
        if not t:return raw.copy()
        return raw+sum(self.part(d,t,h,i) for i in ("central",1,-1))

class Basis:
    def __init__(self,m,cfg):
        u,v=m.xy[m.roll[0]].T
        a=scalar(u);a[:,1]=1.;b=scalar(v);b[:,2]=1.
        L=m.delay.END_LENGTH;w=b/L;one=scalar(np.ones(len(v)))
        s0=m.delay.original_parameter(v)
        ang,k,kp,*_=m.g.turn(s0,np.pi/2,m.g.END_TURN,m.g.END_BLEND,32)
        z=np.maximum(1-ang/m.delay.SMALL_ANGLE,0.)
        c1=4*z**3/m.delay.SMALL_ANGLE;c2=-12*z**2/m.delay.SMALL_ANGLE**2
        dv=1+m.delay.EXTRA*c1*k
        d2=m.delay.EXTRA*(c2*k*k+c1*kp)
        v_old=unary(b,s0,1/dv,-d2/dv**3)/m.g.END_LENGTH
        radial=[];angular=[]
        def family(x,tag,depth):
            l=x[:,0];f=l**3*(1-l)**3
            # C2-clamped endpoint envelope; normalized to one at the midpoint.
            e=64*unary(x,f,3*l*l*(1-l)**2*(1-2*l),
                6*l*(1-l)*(1-2*l)**2-6*l*l*(1-l)**2)
            for j,q in enumerate(cheb(2*x-one,depth)):
                radial.append(((tag,"poly",j),mul(e,q)))
        family(w,"physical-v",cfg["radial_degree"])
        family(v_old,"old-v",cfg["turn_degree"])
        for side in (0,1):
            x=w if side==0 else one-w;l=x[:,0];p=2.5
            f=l**p*(1-l)**4
            f1=p*l**(p-1)*(1-l)**4-4*l**p*(1-l)**3
            f2=p*(p-1)*l**(p-2)*(1-l)**4-8*p*l**(p-1)*(1-l)**3+12*l**p*(1-l)**2
            radial.append((("fractional",side),32*unary(x,f,f1,f2)))
        P=2*m.g.profile_constants(32)[4]
        for j in range(cfg["roll_modes"]+1):
            k=2*np.pi*j/P
            for ph in ([0.] if j==0 else [0.,np.pi/2]):
                p=k*u+ph
                angular.append((("circ",j,int(ph>0)),unary(a,np.cos(p),-k*np.sin(p),-k*k*np.cos(p))))
        _,T,N,K,Ks=m.g.profile_coordinates(u)
        for i in (0,1):
            angular.append((("T",i),unary(a,T[:,i],-K*N[:,i],-Ks*N[:,i]-K*K*T[:,i])))
        self.names=[];self.m=len(radial)*len(angular);self.B=np.empty((6,len(u),self.m))
        for ri,(rn,q) in enumerate(radial):
            for ai,(an,g) in enumerate(angular):
                j=ri*len(angular)+ai;self.B[:,:,j]=mul(q,g).T;self.names.append((rn,an))
        self.n=HARD+6*self.m;self.mesh=m
    def val(self,z):
        out=np.zeros_like(self.mesh.f0)
        for sl,q in zip(self.mesh.roll,z[HARD:].reshape(2,self.m,3)):
            out[sl]=(self.B@q).transpose(1,0,2)
        return out
    def adj(self,v):
        return np.concatenate([(self.B.reshape(-1,self.m).T@np.ascontiguousarray(v[i].transpose(1,0,2)).reshape(-1,3)).ravel()
             for i in self.mesh.roll])
    def project(self,names,z):
        out=np.zeros(self.n);out[:HARD]=z[:HARD]
        orig={k:i for i,k in enumerate(names)};old=z[HARD:].reshape(2,len(names),3);new=out[HARD:].reshape(2,self.m,3)
        for i,k in enumerate(self.names):
            if k in orig:new[:,i]=old[:,orig[k]]
        return out

def seams(m,f):
    P=len(m.polar);ends=[];caps=[]
    for name,u,v,sl in m.cases:
        if name=="cylinder":
            central=f[sl].reshape(P,-1,6,3)
        elif name.startswith("end"):
            ends.append(f[sl].reshape(P,-1,6,3))
        elif name in ("cap+","cap-"):
            caps.append(f[sl].reshape(P,-1,6,3))
    ret=[]
    for i,sg in enumerate([1,-1]):
        inside=central[:,-1 if sg==1 else 0].copy();inside[:,[2,4]]*=sg
        outside=caps[i][:,-1].copy();outside[:,[2,4]]*=-1
        ret.append([float(abs(inside-ends[i][:,0]).max()),float(abs(outside-ends[i][:,-1]).max())])
    return ret
