"""Unprojected complete physical atlas and material fields of R744/R745."""
import numpy as np

def dot(a,b):
    return np.einsum("...i,...i->...",a,b)

def info(gid,src,gap):
    if gid=="equal":
        g=src;gamma=g.chosen();c=np.array([g.CX,0.,0.]);h=g.H
    else:
        g=src.parent;gamma=0.;c=np.array([g.CENTER_X,0.,0.]);h=g.HEIGHT
    cc,ss=np.cos(gamma),np.sin(gamma)
    frame=np.array([[cc,0.,-ss],[0.,1.,0.],[ss,0.,cc]])
    return g,c,frame,h

def profile_nodes(g,n,shift):
    lh,l,r,top,half,*_=g.profile_constants(32)
    edges=[0.,lh,l,l+1.,r,top,half]
    for a in [.001,.02,.04,.15,.26,.28]:
        if lh<l-a<l:edges.append(l-a)
        if r<r+a<top:edges.append(r+a)
    for a in [.3,.3325,.5275,.56]:
        edges.append(l+1+a)
    for a in [lh+.001,top-.001]:edges.append(a)
    edges=np.unique(np.r_[edges,2*half-np.array(edges)])
    raw=[(np.arange(n)+shift)*2*half/n,edges[:-1]]
    if shift:raw.append((edges[:-1]+edges[1:])/2)
    return np.unique(np.round(np.concatenate(raw),13))%(2*half)

def y_nodes(n,shift):
    a=np.linspace(-1.,1.,n)
    if shift:a=np.r_[a[0],a[:-1]+(a[1:]-a[:-1])*.413,a[-1]]
    positive=np.array([0,1/4096,1/1024,2/1024,.01,.13,.3,.55,.8,.96,.99])
    return np.unique(np.r_[a,positive,-positive])

def transition(x,y,width):
    """C3 scalar mask and its two physical chart derivatives before sign changes."""
    rho=np.hypot(x,y);t=np.clip((rho-1.)/width,0,1)
    p=t*(1-t);h=t**4*(35+t*(-84+t*(70-20*t)))
    hr=140*p**3/width;hrr=420*p*p*(1-2*t)/width**2
    den=np.where(rho>.25,rho,1.);rx=x/den;ry=y/den
    return np.stack([h,hr*rx,hr*ry,hrr*rx*rx+hr*(1-rx*rx)/den,
                 hrr*rx*ry-hr*rx*ry/den,hrr*ry*ry+hr*(1-ry*ry)/den],axis=1)

def material(g,s,v,chart,width,fieldwidth):
    n=len(s); chi=np.zeros((n,6));chi[:,0]=1.;x0=np.zeros((n,3,2))
    if chart.startswith("cap"):return chi,x0
    _,m0,_,_,half,*_=g.profile_constants(32)
    lo=s>half
    sx=np.where(lo,-1.,1.)
    sy=-1. if chart=="end-" else 1.
    x=np.where(lo,2*half-s,s)-m0-1.
    y=v if chart=="cylinder" else sy*(1+v)
    chi=transition(x,y,width);chi[:,1]*=sx;chi[:,2]*=sy;chi[:,4]*=sx*sy
    q=transition(x,y,fieldwidth);q0=1-q[:,0];qx=-q[:,1];qy=-q[:,2]
    x0[:,0,0]=-sx*y*q0;x0[:,0,1]=sy*x*q0
    x0[:,1,0]=-y*qx;x0[:,1,1]=sy*sx*(q0+x*qx)
    x0[:,2,0]=-sx*sy*(q0+y*qy);x0[:,2,1]=x*qy
    return chi,x0

class Mesh:
    def __init__(self,p,design,src,counts,offset):
        self.design=design;self.src=src;g,c,Q,h=info(design["geometry"],src,design["gap"])
        self.g,self.center,self.frame,self.H=g,c,Q,h
        self.hr=src.parent
        u=profile_nodes(g,counts[0],offset)
        y=y_nodes(counts[1],offset);le=self.hr.END_LENGTH
        a=np.linspace(0.,1.,counts[2]);v=np.unique(np.r_[le*a,.00025,.0005,le-.0005,le-.00025])
        lam=np.linspace(0.,1.,counts[3])[1:];lam=np.unique(np.r_[.009,.042,lam])
        parts=[];mask=[];xx=[];norm=[];weight=[];labs=[];aa=[];bb=[]
        cases=[("cylinder",y,1),("end+",v,1),("end-",v,-1),("cap+",lam,-1),("cap-",lam,1),
                  ("cap-center+",[0.],-1),("cap-center-",[0.],1)]
        for chart,rad,sign in cases:
            if "center" in chart:
                us=np.array([c[0]]);vs=np.array([c[-1]])
                z=g.cap_cartesian(us,vs,1 if chart.endswith("+") else -1.)
            else:
                us,vs=np.meshgrid(u,rad,indexing="ij");us=us.ravel();vs=vs.ravel()
                if design["geometry"]=="equal":
                    z=g.chart_jet(chart,us,vs,markers=False,jacobi=bool(design["gap"]))
                else:
                    z=g.chart_jet(chart,us,vs,markers=False,gap_amplitude=design["gap"])
            ch,x=material(g,us,vs,chart,p["shape_mask_width"],design["field_width"])
            z=z@Q;z[:,0,:]-=c@Q
            parts.append(z);mask.append(ch);xx.append(x);norm.append(np.full(len(us),sign))
            # Full chart budget, keeping the two regular cap centers as finite sample points.
            wt=(.002 if "center" in chart else 1.)/len(us)
            weight.append(np.full(len(us),np.sqrt(wt)))
            labs.append(np.full(len(us),chart));aa.append(us);bb.append(vs)
        self.f=np.concatenate(parts);self.chi=np.concatenate(mask);self.X0=np.concatenate(xx)
        self.sign=np.concatenate(norm);self.weight=np.concatenate(weight);self.lab=np.concatenate(labs)
        self.a=np.concatenate(aa);self.b=np.concatenate(bb)
    def point(self,i):
        tag=str(self.lab[i])
        half=self.g.profile_constants(32)[4]
        side=("upper_profile" if self.a[i]<half else "lower_profile") if "center" not in tag else "regular_center"
        return {"chart":tag,"coordinate_1":float(self.a[i]),"coordinate_2":float(self.b[i]),
                "side":side,"physical_grid_index":int(i)}
    def phase_cloud(self,f,p):
        # Each active phase is the same physical image rigidly rotated, plus fixed upper marks.
        from scipy.spatial import cKDTree
        pts0=f[:,0]@self.frame.T+self.center
        raw=np.cross(f[:,1],f[:,2])*self.sign[:,None];raw/=np.maximum(np.linalg.norm(raw,axis=1,keepdims=True),1e-15)
        nn0=raw@self.frame.T
        g=self.g;_,m0,_,_,half,*_=g.profile_constants(32)
        top=(self.lab=="cylinder")&(self.a<half)&(np.hypot(self.a-m0-1.,self.b)<1.)
        if self.design["geometry"]=="equal":marks=g.MARKS;heights=[g.HEIGHT]*len(marks)
        else:marks=g.disk.MARKERS;heights=[1e-4*d**2 for _,_,d in marks]
        ex=[]
        for x,y,r in marks:
            a=np.arange(16)*2*np.pi/16;rr=r*np.linspace(0,1,5)[:,None]
            px=(x+rr*np.cos(a)).ravel();py=(y+rr*np.sin(a)).ravel()
            ex.append(np.column_stack([px,py,np.full(len(px),self.H)]))
        ex=np.vstack(ex)
        out=[];first=None
        for ph in p["phases"]:
            c,s=np.cos(ph),np.sin(ph);rot=np.array([[c,s,0.],[-s,c,0.],[0.,0.,1.]])
            pts=np.vstack([pts0@rot,ex]);norm=np.vstack([nn0@rot,np.tile([0.,0.,1.],(len(ex),1))])
            ids=np.r_[np.where(top)[0],np.arange(len(pts0),len(pts))]
            for (x,y,r),h in zip(marks,heights):
                dx,dy=pts[ids,0]-x,pts[ids,1]-y
                q=1-(dx**2+dy**2)/r**2;use=q>0;ix=ids[use];t=q[use]
                pts[ix,2]+=h*t**3
                ng=np.column_stack([6*h*dx[use]*t*t/r**2,6*h*dy[use]*t*t/r**2,np.ones(len(ix))])
                norm[ix]=ng/np.linalg.norm(ng,axis=1,keepdims=True)
            tree=cKDTree(pts)
            if first is None:first=(pts,tree)
            diameter=inv=0.;ij=[0,0]
            for j in range(0,len(pts),32):
                d=pts[None,:,:]-pts[j:j+32,None,:];dd=np.einsum("bni,bni->bn",d,d)
                ratio=2*np.abs(np.einsum("bni,bi->bn",d,norm[j:j+32]))/np.where(dd>1e-16,dd,np.inf)
                diameter=max(diameter,float(dd.max()))
                if ratio.max()>inv:
                    h,k=np.unravel_index(ratio.argmax(),ratio.shape);ij=[int(j+h),int(k)];inv=float(ratio[h,k])
            out.append({"phase":ph,"ordered_inverse_reach":inv,"arg_pair_cloud_indices":ij,
                        "sample_diameter":float(np.sqrt(diameter)),"sample_held":float(max(tree.query(first[0])[0].max(),first[1].query(pts)[0].max())),
                        "size":len(pts)})
        return out
