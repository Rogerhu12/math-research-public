"""R736 continuous material endpoint screening. The interval margins are specified in the accompanying proof."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from r688_actual_r664_window_collars import require_public

# Explicit pi enclosure follows from the alternating arctangent series in
# pi/4=4 atan(1/5)-atan(1/239). Binary64 evaluation of these terms is padded in the proof.
PI=3.141592653589793
BETA0=.100
INC=.920
W=.27
A=.52
FILLET=.174
SHIFT=.320
T0=.25*2/PI
QPAD=.000045


def trig(x,cosine):
    """Taylor with |x|<=pi, analytic remainder <2e-15 and an absolute 5e-13 evaluation allowance."""
    x=np.asarray(x,dtype=float)
    z=x*x
    m=0 if cosine else 1
    term=np.ones_like(x) if cosine else x.copy()
    v=term.copy()
    for j in range(1,15):
        term*= -z/((m+2*j)*(m+2*j-1))
        v+=term
    return v


def sin(x):return trig(x,False)
def cos(x):return trig(x,True)


def linear_step(u):
    return np.clip((u-.001)/.998,0.,1.)


def angle(v,c,w):
    return linear_step((abs(v)-c)/w)


def alphas(v):
    a=.1*(angle(v,.205,.102)-angle(v,.846,.102))
    a1=a+.92*(angle(v,.206,.100)-angle(v,.847,.100))
    return a,a1


def integral(values):
    return np.r_[0.,np.cumsum(values,dtype=float)/len(values)]


def odd_at(v,grid,values,x_extension):
    y=abs(v)
    return np.sign(v)*(np.interp(np.minimum(y,1.),grid,values)+x_extension*np.maximum(0.,y-1))


class Curves:
    def __init__(self,nq,nline,nu):
        if nq<65536 or nline<96 or nu<32:raise ValueError('input too coarse for declared quadrature padding')
        self.N=nq;self.vgrid=np.linspace(0,1,nq+1)
        self.mid=(np.arange(nq)+.5)/nq
        self.a,self.a1=alphas(self.mid);self.ca=cos(self.a);self.sa=sin(self.a)
        self.Y0=integral(self.ca);self.Z0=integral(self.sa)
        turn=PI*linear_step(self.mid)
        uy=integral(cos(turn));uz=integral(sin(turn))
        self.lu=.40/uz[-1]
        self.ub=FILLET*integral(sin(.5*turn))[-1]
        self.endx=W+A+FILLET*integral(cos(.5*turn))[-1]
        # Every cell that can have k'_0 != 0 is separately marked and split.
        sk=np.array([.0005,.0015,.9985,.9995])
        ramps=np.r_[.205+.102*sk,.846+.102*sk]
        slope_knots=np.r_[.206+.1*sk,.847+.1*sk]
        v=np.unique(np.r_[np.linspace(-1,1,nline+1),ramps,-ramps,slope_knots,-slope_knots,-.6,0,.6])
        u=np.unique(np.r_[np.linspace(0,1,nu+1),sk])
        # For a half-loop, omit its endpoint and the duplicated line/U join.
        self.v=np.r_[v[:-1],np.ones(len(u)-1)]
        self.uf=np.r_[np.zeros(len(v)-1),u[:-1]]
        self.on=np.r_[np.zeros(len(v)-1,dtype=bool),np.ones(len(u)-1,dtype=bool)]
        self.hlen=len(self.v)
        loc=np.r_[v[:-1]+1,2+self.lu*u[:-1]]
        self.sigma=np.r_[loc,loc+2+self.lu,4+2*self.lu]
        self.ds=np.diff(self.sigma)+2.e-7
        # A true U-material cell scales by the true U length, which differs by <.00002.
        self.ds*=1.00004
        halfmid=(np.r_[loc,2+self.lu][1:]+loc)/2
        vhalf=halfmid-1
        uhalf=(halfmid-2)/self.lu
        is_sharp=np.zeros(len(halfmid),dtype=bool)
        for c in (.205,.846):
            y=(abs(vhalf)-c)/.102
            for k in (.001,.999):is_sharp|=(halfmid<2)&(abs(y-k)<.0005001)
        for k in (.001,.999):is_sharp|=(halfmid>=2)&(abs(uhalf-k)<.0005001)
        self.dk=np.tile(np.where(is_sharp,35000.,0.),2)
        self.uy=self.lu*np.interp(self.uf,self.vgrid,uy)
        self.uz=.20-self.lu*np.interp(self.uf,self.vgrid,uz)
        a,_=alphas(self.v);turn=PI*linear_step(self.uf)
        normal=np.column_stack((np.where(self.on,sin(turn),-sin(a)),np.where(self.on,cos(turn),cos(a))))
        self.outer0=self.circle(self.Y0,self.Z0)
        self.inner0=self.outer0-self.ub*self.double(normal)
        zm=np.select([self.v<=-.6,self.v<=0,self.v<=.6],[0.,.1-a,.1],default=.2-a)
        neg=np.where(self.on,.2+turn,zm);e=loc-self.ub*neg
        self.ehalf=2+self.lu-self.ub*(.2+PI)
        self.eta=np.r_[e,e+self.ehalf,2*self.ehalf]
        qy=self.inner0[:,0]
        self.w=np.sign(qy)*(np.interp(np.minimum(abs(qy),self.Y0[-1]),self.Y0,self.vgrid)
                            +np.maximum(0.,abs(qy)-self.Y0[-1]))
        self.qz=self.inner0[:,1]
        arc=abs(self.eta[:,None]-self.eta[None,:])
        arc=np.minimum(arc,2*self.ehalf-arc)
        self.product=(A+FILLET-QPAD)**2+arc**2
        d=self.inner0[None,:,:]-self.outer0[:,None,:]
        self.ambient=(self.endx-W)**2+np.sum(d*d,axis=-1)
        self.tetrads=len(self.sigma)-1

    def double(self,p):
        return np.concatenate((p,-p,p[:1]),axis=0)

    def circle(self,y,z):
        P=np.column_stack((odd_at(self.v,self.vgrid,y,1),odd_at(self.v,self.vgrid,z,0)))
        P[:,1]+=.20
        P[self.on,0]=y[-1]+self.uy[self.on]
        P[self.on,1]=z[-1]+self.uz[self.on]
        return self.double(P)

    def terminal_points(self,t):
        phase=t**4;th=(PI/2)*t;st=sin(th);ct=cos(th)
        aa=self.a+phase*(self.a1-self.a);beta=phase*self.a1
        P=self.circle(integral(cos(aa)),integral(sin(aa)))
        y=odd_at(self.w,self.vgrid,integral(self.ca*cos(beta)),1.)
        h=odd_at(self.w,self.vgrid,integral(self.ca*sin(beta)),0.)
        x=self.endx-SHIFT*st+ct*h-self.qz*st
        z=st*h+self.qz*ct
        return P,np.column_stack((x,y,z))


def cell_max(a):
    return np.maximum(np.maximum(a[:-1,:-1],a[:-1,1:]),np.maximum(a[1:,:-1],a[1:,1:]))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def put_record(path,**fields):
    tmp=path.with_suffix('.pending')
    with tmp.open('wb') as f:np.savez_compressed(f,**fields)
    os.replace(tmp,path)


def prepare(args,root):
    identity=dict(source_sha=sha(Path(__file__).read_bytes()),shift=SHIFT,quad=args.quad,line=args.line,usub=args.u,
                  time=args.time,numpy=np.__version__,float64=np.finfo(float).bits,pose_clock='lambda=t^4')
    meta=root/'input.json';expected=json.dumps(identity,sort_keys=True)
    if meta.exists() and json.loads(meta.read_text())!=identity:raise ValueError('R736 incompatible paid grid/input')
    meta.write_text(expected+'\n')
    page=root/'source-state';page.mkdir(exist_ok=True)
    index=page/'index.json'
    if index.exists():
        ids=json.loads(index.read_text());c=Curves.__new__(Curves)
        for key,h in ids.items():
            path=page/(key+'.npz')
            if sha(path.read_bytes())!=h:raise ValueError('mismatched R736 paid source '+key)
            with np.load(path,allow_pickle=False) as part:z=part['value']
            setattr(c,key,z.item() if z.ndim==0 else z)
        return c
    c=Curves(args.quad,args.line,args.u);ids={}
    for key,value in vars(c).items():
        path=page/(key+'.npz');put_record(path,value=value);ids[key]=sha(path.read_bytes())
    index.write_text(json.dumps(ids,sort_keys=True)+'\n')
    return c


def distances(curves,t,root):
    key=sha(np.asarray(t,dtype='<f8').tobytes())[:20]
    path=root/('physical-'+key+'.npz')
    if path.exists():
        with np.load(path,allow_pickle=False) as data:
            if data['time'].item()!=t:raise ValueError('R736 paid phase mismatch')
            P,G=data['outer'],data['core']
    else:
        P,G=curves.terminal_points(t)
        put_record(path,time=t,outer=P,core=G)
    return (G[None,:,0]-W)**2+(G[None,:,1]-P[:,0,None])**2+(G[None,:,2]-P[:,1,None])**2


def screen(curves,nt,stop,root):
    st=time.monotonic();tt=np.linspace(T0,1.,nt+1)
    # Pure second derivatives of the scalar squared tests in each variable.
    outer=(108.+2.4*curves.dk)*curves.ds**2/8
    inner=(172.+3.2*curves.dk)*curves.ds**2/8
    err=outer[:,None]+inner[None,:]+500.*(tt[1]-tt[0])**2/8
    ca=curves.ambient;cp=curves.product
    last=None;unclosed=0;cells=0;worst=-np.inf
    where=None;ranges=[];seen=0;left=np.zeros((curves.tetrads,curves.tetrads),dtype=bool)
    for i in range(nt):
        if time.monotonic()-st>stop:break
        receipt=root/f'boxes-{i:04d}.npz'
        if receipt.exists():
            with np.load(receipt,allow_pickle=False) as rr:
                if rr['begin']!=tt[i] or rr['end']!=tt[i+1]:raise ValueError('R736 paid interval mismatch')
                bad=np.unpackbits(rr['packed'],count=curves.tetrads**2).reshape(left.shape).astype(bool)
                peak=float(rr['max']);ij=rr['ij']
            last=None
        else:
            if last is None:last=distances(curves,tt[i],root)
            now=distances(curves,tt[i+1],root)
            # The additional ambient source length surplus is left unused in the large-phase screen.
            amb=cell_max(np.maximum(last-ca,now-ca))+.0057+err
            prod=cell_max(np.maximum(last-cp,now-cp))+.0094+err
            top=np.minimum(amb,prod)+.00065 # complete physical endpoint bands
            bad=top>=0;peak=float(np.max(top));ij=np.unravel_index(np.argmax(top),top.shape)
            put_record(receipt,begin=tt[i],end=tt[i+1],packed=np.packbits(bad),max=peak,ij=ij)
            last=now
        if peak>worst:
            worst=peak;where=[i,int(ij[0]),int(ij[1])]
        cnt=int(np.count_nonzero(bad))
        if cnt:ranges.append([i,cnt,peak])
        unclosed+=cnt;left|=bad;cells+=bad.size;seen+=1
    return dict(finished_time_cells=seen,total_time_cells=nt,continuous_material_time_boxes=cells,
                unclosed_boxes=unclosed,unclosed_material_boxes=int(np.sum(left)),worst_upper_excess=worst,
                worst_box=where,unclosed_by_time=ranges,all_cross_pairs=bool(seen==nt and not unclosed),
                changes_source_or_target=False,elapsed=time.monotonic()-st),left


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--line',type=int,default=256);ap.add_argument('--u',type=int,default=64)
    ap.add_argument('--time',type=int,default=128);ap.add_argument('--quad',type=int,default=65536)
    ap.add_argument('--seconds',type=float,default=300.);ap.add_argument('--out',default='r736-cross')
    a=ap.parse_args();require_public()
    dest=Path(a.out);dest.mkdir(parents=True,exist_ok=True)
    curves=prepare(a,dest);info,left=screen(curves,a.time,a.seconds,dest)
    np.savez_compressed(dest/'unclosed-material.npz',unclosed_material_mask=left,sigma_centres=curves.sigma,
                        signed_weighted_labels=curves.eta)
    info.update(line=a.line,usub=a.u,time=a.time,quad=a.quad,pose_shift=SHIFT,small_phase_analytic='theta <= .25',
                note='unclosed boxes are inconclusive, not violations',input_geometry='R732 unchanged source, explicit R736 assigned inner core')
    (dest/'summary.json').write_text(json.dumps(info,indent=2,allow_nan=False)+'\n')
    print('R736_CROSS',json.dumps(info,sort_keys=True),flush=True)


if __name__=='__main__':main()

