"""Complete Fourier rows, actual material shells and local-support columns."""
import numpy as np
from scipy.interpolate import BSpline
from r703_material_geometry_observer import cones,relmetric,ActualPose,barrier
from r683_proper_phase_metric_transport_20261128 import shell,shell_ok
from r726_closed_spinor_fourier import ClosedSpinor
from r726_paid_half_projection import AnchoredSpaces


class Grid:
    def __init__(self,spans,order,split=1):
        self.a,self.b,self.theta=.075,.22,np.arcsin(.27)
        edges=np.linspace(self.a,self.b,spans*split+1)
        t,gw=np.polynomial.legendre.leggauss(order)
        h=np.diff(edges)/2
        rr=(edges[1:]+edges[:-1])[:,None]/2+h[:,None]*t
        self.r=np.sort(np.r_[edges,rr.ravel()])
        self.w=np.zeros(len(self.r))
        for i,width in enumerate(h):
            j=i*(order+1)
            self.w[j+1:j+1+order]=width*gw
        widths=np.diff(self.r)
        self.guard=(np.r_[0.,widths]+np.r_[widths,0.])/2


class Layout:
    def __init__(self,spans,K):
        self.space=AnchoredSpaces(.075,.22,spans,np.arcsin(.27))
        self.K=K;self.spans=spans;self.nd=2*K+1
        bs,bc=self.space.basis(np.array([.075,.22]),0)
        self.shapes=((bs.shape[1],self.nd),(bs.shape[1],self.nd),(bc.shape[1],2))
        self.offset=np.r_[0,np.cumsum([int(np.prod(a)) for a in self.shapes])]
        self.size=int(self.offset[-1])
    def pack(self,cs):
        return np.concatenate([c.ravel() for c in cs])
    def split(self,x):
        return tuple(x[a:b].reshape(sh) for a,b,sh in zip(self.offset[:-1],self.offset[1:],self.shapes))
    def masks(self,r):
        base=[self.space.basis(r,j) for j in range(3)]
        masks=[]
        for block,(nr,ncol) in enumerate(self.shapes):
            use=int(block==2)
            active=np.logical_or.reduce([q[use]!=0 for q in base])
            for i in range(nr):
                ids=np.flatnonzero(active[:,i])
                masks.extend([ids]*ncol)
        return masks
    def prolong(self,old,x):
        if self.spans%old.spans or self.K<old.K:raise ValueError('Nested spinor spaces required.')
        result=[]
        for block,(oldc,sh) in enumerate(zip(old.split(x),self.shapes)):
            dest=np.zeros(sh)
            if block==2:
                full=np.vstack((np.repeat(oldc[:1],3,axis=0),oldc[1:],np.zeros((3,2))))
            else:
                full=np.pad(oldc,((3,3),(0,0)))
            curve=BSpline(old.space.spline.t,full,5)
            for i,pos in enumerate(np.linspace(.075,.22,self.spans+1)[1:-1],1):
                if i%(self.spans//old.spans):curve=curve.insert_knot(pos)
            fitted=np.vstack((curve.c[0:1],curve.c[3:-3])) if block==2 else curve.c[3:-3]
            dest[:,:fitted.shape[1]]=fitted
            result.append(dest)
        return self.pack(result)


def native(core,s,r,center):
    def evals(a):
        k=core.degree;z,c,h=core.modes(a,k)
        freq=np.arange(1,k+1).reshape((1,k)+(1,)*(a.ndim-2))
        def mix(x,y):
            return np.einsum('mn,rm...->rn...',core.cos[:k],x)+np.einsum('mn,rm...->rn...',core.sin[:k],y)
        return z[:,None,...]+mix(c,h),mix(h*freq,-c*freq),mix(-c*freq**2,-h*freq**2)
    (u,up,upp),(ur,urp,_),(urr,_,_)=map(evals,s['auxiliary_position_jets'])
    (_,su,suu),(pr,jr,_),(prr,_,_)=map(evals,s['auxiliary_shift_jets'])
    p=pr-pr[:,0:1];pp=prr-prr[:,0:1];J=1+su
    if np.any(J.real<=.02):raise FloatingPointError('Native material interpolation lost positive speed.')
    g=p/J;gp=(jr-g*suu)/J;gr=(pp-g*jr)/J
    t=up/J[...,None];tp=(upp-suu[...,None]*t)/J[...,None]
    tr=(urp-jr[...,None]*t)/J[...,None]-g[...,None]*tp
    du=ur-g[...,None]*up
    ddu=urr-2*g[...,None]*urp+g[...,None]**2*upp+(g*gp-gr)[...,None]*up
    rd=r[:,None,None];c,cr,crr=(z[:,None,:] for z in center)
    return c+rd*u,cr+u+rd*du,t,crr+2*du+rd*ddu,t/rd+tr,tp/(rd*J[...,None])


def state(layout,core,x,r,ref=None):
    za,zb,c=layout.space.actual_jets(r,layout.split(x))
    s=core.state(r,za,zb,c,ref)
    if any(np.any(y[:,1]!=0) for y in c):raise ArithmeticError('Reflection center leaves its fixed plane.')
    sh=(s['physical_six_jets'],native(core,s,r,c))
    return s,c,sh


def length_rows(S,C,count,weight):
    theta=np.arcsin(.27);a,b,T=.075,.22,.03
    ang=np.linspace(-np.pi,np.pi,count,endpoint=False)
    A=np.abs(np.angle(np.exp(1j*(ang+theta))));B=abs(ang)
    if S.real<=T*np.max(abs(A-B)):raise FloatingPointError('Terminal tangent cones do not meet.')
    merge=(A+B-S/T)/2
    U=np.where(merge.real>0,T*(np.sin(A)+np.sin(B)-2*np.sin(np.where(merge.real>0,merge,0))),
               S-T*(A-np.sin(A)+B-np.sin(B)))
    tests=np.stack((np.cos(ang),np.sin(ang)),axis=1)
    delta=np.array([b-a*np.cos(theta),a*np.sin(theta)])
    z=((tests@delta)[None,:]+np.array([[-1.],[1.]])*(tests@C)[None,:]-U)/(b-a)
    return (weight*barrier(z+.0002/(b-a),.0005)/np.sqrt(z.size)).ravel(),-z.real.max()*(b-a)


def local_rows(st,sh,weights,opt):
    E=st['E'][:,None];m=np.sqrt(E);span=.22-.075
    w=np.sqrt(weights[:,None]/span)
    out=[];masks=[]
    def put(a,mask=None):
        out.append(a);masks.append(np.ones(a.shape,bool) if mask is None else mask)
    a0,ac,_=st['complete_RA'];_,_,bs=st['complete_RB']
    put(w*(a0[:,None]/E));put(w*ac/(np.sqrt(2.)*E));put(w*bs/(np.sqrt(2.)*m))
    angular=w*np.sqrt(st['J']/st['J'].shape[1])
    for geometry,coef in zip(sh,(1.,.45)):
        vals,ten=cones(geometry,np.arcsin(.27));ar,br,cr=ten[:3]
        rel=(ar/E-1,np.sqrt(2.)*br/m,cr-1)
        emph=1+sum(y*y for y in rel)/opt['peak_scale']**2
        for y in rel:put(angular*coef*opt['metric_weight']*emph*y)
        for j,g in enumerate(vals):
            target=opt['axis_guard'] if j>=4 else opt['cone_guard']
            put(angular*coef*opt['geometry_weight']*barrier(target-g,.004),g.real<target)
    return np.column_stack(out),np.column_stack(masks)


def read_curve(g,curve,c,E,material_angles):
    vals,ten=cones(curve,g.theta)
    a,b,d,det,L,M,K=ten
    mean=(d*L-2*b*M+a*K)/(2*det);gauss=(L*K-M*M)/det
    curv=abs(mean)+np.sqrt(np.maximum(0.,mean**2-gauss))
    rel=relmetric(ten,np.sqrt(E)[:,None])
    u=(curve[0]-c[0][:,None,:])/g.r[:,None,None]
    info=shell(ActualPose(g,c[0]),None,dict(r=g.r,q=np.zeros_like(g.r)),dict(U=u),
               dict(actual_center=c[0][0,[0,2]],min_outer_normal=float(vals[4].min()),
                    min_inner_normal=float(vals[5].min()),max_abs_curvature=float(curv.max())))
    i,j=np.unravel_index(rel.argmax(),rel.shape);k,l=np.unravel_index(curv.argmax(),curv.shape)
    neg=[max(0.,-float(v)) for name,v in info.items() if
         name in ('sampled_curvature_margin','sampled_outer_normal_min','sampled_inner_normal_min',
                  'sampled_side_margin','sampled_cylinder_margin','peg_outer_tube_cylinder_margin',
                  'sampled_whole_support_dominance')]
    neg.append(max(0.,info['sampled_whole_D_upper_estimate']-1))
    return dict(shell=info,eta=float(rel[i,j]),eta_attainer=[float(g.r[i]),float(material_angles[i,j])],
                curvature=float(curv[k,l]),curvature_attainer=[float(g.r[k]),float(material_angles[k,l])],
                shell_pass=shell_ok(info),violation=sum(neg))


def actual_read(g,st,c,sh,nbeta):
    pair=[read_curve(g,z,c,st['E'],st['material_angle']) for z in sh]
    S=float(g.w@np.sqrt(st['E']));_,lm=length_rows(S,c[0][0,[0,2]],nbeta,1.)
    identities={}
    for name,val in st['spectral_identity_reads'].items():
        if name=='certified_continuous':continue
        identities[name]=[float(np.max(abs(a))) for a in val] if isinstance(val,tuple) else float(np.max(abs(val)))
    rim={}
    theta=g.theta
    for ix,angle,label in ((0,theta,'inner'),(-1,0.,'outer')):
        phi=st['material_angle'][ix];co,si=np.cos(phi),np.sin(phi)
        ca,sa=np.cos(angle),np.sin(angle)
        er=np.stack((ca*co,si,-sa*co),axis=1);et=np.stack((-ca*si,co,sa*si),axis=1)
        known=(c[0][ix]+g.r[ix]*er,er,et,np.zeros_like(er),et/g.r[ix],-er/g.r[ix])
        rim[label]=[[float(np.linalg.norm(v[ix]-u,axis=-1).max()) for v,u in zip(curve,known)] for curve in sh]
    return dict(paired=pair,rim_material_six=rim,eta=max(p['eta'] for p in pair),curvature=max(p['curvature'] for p in pair),
              shell_pass=all(p['shell_pass'] for p in pair),shell_violation=sum(p['violation'] for p in pair),
              actual_center=c[0][0].tolist(),target_radial_integral=S,target_length_margin=float(lm),
              sampled_J_minimum=float(st['J'].min()),angular_J_lower_estimate=float(st['ordinary_angular_J_lower'].min()),
              finite_identity_disagreements=identities,
              all_parity_disagreement=[float(np.max(abs(v))) for v in st['parity_read']],
              angular_certified=False,radial_certified=False)
