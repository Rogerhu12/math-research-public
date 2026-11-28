"""R772 full translation shell with physical directors and genuine transverse/axial material changes."""
import numpy as np
import r772_coherent_developing_tube as geom
from r742_tilted_disk_two_jets import J,unary,trig
from r767_preloaded_cap_atlas import root
from r767_negative_track_profile import clock

def arctan(x):return unary(x,np.arctan(x.v),1/(1+x.v*x.v),-2*x.v/(1+x.v*x.v)**2)

def heading(x,t):
    u=unary(x,*clock(x.v));co,si=trig(2*np.pi*u)
    return arctan((geom.X0+(geom.X1-geom.X0)*np.sin(t))*si*(1.5-.5*si*si))

def section_tz(s):
    v=np.mod(s.v,geom.P);b=np.floor(v/geom.BLOCK).astype(int);x=v-b*geom.BLOCK
    d=np.clip(x-geom.FLAT,0.,geom.QUARTER)
    al=geom.softened_angle(d,geom.QUARTER,geom.SM,1/geom.R)+np.pi*b/2
    h=np.clip(np.minimum(d,geom.QUARTER-d)/geom.SM,0.,1.)
    k=geom.s5(h)/geom.R
    kp=30*h**2*(1-h)**2*np.where(d<geom.QUARTER/2,1.,-1.)/(geom.SM*geom.R)
    return unary(s,-np.sin(al),-np.cos(al)*k,np.sin(al)*k*k-np.cos(al)*kp)

def base(chart,u,v,t,order,d):
    if chart!="cylinder" or not t:return geom.chart_jet(chart,u,v,t,order)
    a,b,slip=d
    e=J(np.asarray(u),s=1.);x=J(np.asarray(v)+.5,a=1.)
    C,n=geom.section(e,order)
    A,z=geom.path(x,t,order);q=heading(x,t);q0=heading(x,0.)
    # Tangential moves are honest material compositions. Both and all their two-jets
    # vanish at either seam. The cross clock has derivative >1-.18/.27>0.
    dz=geom.path(x,0.,order)[1]-z
    shift=b*dz/root(1+(dz/.18)*(dz/.18))
    ep=e+shift*section_tz(e)
    # Limit axial displacement to a fraction of both distances to the closest rim.
    F=x*(1-x);wave=(q-q0)*F*F*C[1]
    xp=x+slip*wave/root(1+(wave/.037)*(wave/.037))
    cp,n=geom.section(ep,order);A,z=geom.path(xp,t,order)
    ang=a*(heading(xp,t)-heading(xp,0.));co,si=trig(ang)
    # Paired axial material y, section plane X,Z, positive tangent (cos q,sin q).
    # At a=1, b=slip=0 the two mixed and ring rows are EXACT.
    return geom.gather((cp[0],A-si*cp[1],z+co*cp[1]),len(u))

def grid(ns,nv,order,independent=False):
    a=.417 if independent else 0.;b=.283 if independent else 0.
    s=np.unique(np.r_[geom.profile_marks(),np.mod(geom.P*(np.arange(ns)+a)/ns,geom.P)])
    x=np.unique(np.r_[geom.axial_marks(),geom.P*0.+(np.arange(nv)+b)/nv-.5,.5])
    h=np.unique(np.r_[0.,geom.SM,geom.L/2,geom.L-geom.SM,geom.L,
                        geom.L*(np.arange(max(5,nv//2))+b)/max(5,nv//2)])
    rad=np.unique(np.r_[.02,(np.arange(1,max(nv//2,4)+1)-b)/max(nv//2,4),1.])
    def mesh(x,y):
        xx,yy=np.meshgrid(x,y,indexing="ij");return xx.ravel(),yy.ravel()
    out=[("cylinder",*mesh(s,x))]
    ang=2*np.pi*(np.arange(16)+a)/16
    X=np.r_[0.,.02*np.cos(ang),.12*np.cos(ang)];Z=np.r_[0.,.02*np.sin(ang),.12*np.sin(ang)]
    for side in "+-":
        out.extend([("end"+side,*mesh(s,h)),("cap"+side,*mesh(s,rad)),
                     ("cap-normal"+side,*mesh(s,[0.,.003,.01])),("cap-cartesian"+side,X,Z)])
    return out

def cheb(x,n):
    y=[J(0.*x.v+1.),x]
    for _ in range(2,n+1):y.append(2*x*y[-1]-y[-2])
    return y

def names(lev):
    n=lev+1
    out=[("world",i,j,h) for i in range(n+2) for j in range(n+2-i) for h in range(n+2-i-j)]
    out += [("rim",i,j,h) for i in range(n+1) for j in range(n+1-i) for h in range(3)]
    out += [("tube",m,tr,j) for m in range(n+3) for tr in ((0,) if not m else (0,1))
            for j in range(n+2) if m+j<=n+3]
    out += [("corner",i,j,h) for i in range(4) for j in range(n+1) for h in (0,1)]
    return out

def basis(chart,u,v,F,keys):
    from r742_tilted_disk_two_jets import cap_s7
    X,Y,Z=[J(*F[:,:,i].T) for i in range(3)];dep=.5-Y
    k=np.maximum(dep.v,0.);d3=unary(dep,k**3,3*k*k,6*k)
    gate=d3/(d3+.018);degree=max(6,max(c[1] for c in keys)+2)
    ax=cheb(1.8*dep-.95,degree);xx=cheb(2.6*X,degree);zz=cheb(2.6*Z,degree)
    edge=dep-geom.path_table(0.,24)[1][-1,0]
    wave=unary(edge,np.exp(-32*edge.v**2),-64*edge.v*np.exp(-32*edge.v**2),
               (4096*edge.v**2-64)*np.exp(-32*edge.v**2))
    rim=[wave,wave*edge,wave*edge*edge]
    if chart=="cylinder":
        e=J(u,s=1.);x=J(v+.5,a=1.);A=2*np.pi*e/geom.P;tt=[trig(m*A) for m in range(degree+1)]
        h=x*(1-x);bell=64*h*h*h
        cx=cheb(2*x-1.,degree);windows=[]
        # The section coordinate is periodic. Localized columns resolve BOTH
        # true vertical tangencies and all four physical curvature sectors.
        for i in range(4):
            mid=i*geom.BLOCK+geom.FLAT+geom.QUARTER/2
            windows.append(cap_s7((trig(A-2*np.pi*mid/geom.P)[0]-.22)/.66))
    rows=[]
    for typ,i,j,h in keys:
        if typ=="world":b=gate*ax[i]*xx[j]*zz[h]
        elif typ=="rim":b=gate*rim[h]*xx[i]*zz[j]
        elif chart!="cylinder":b=J(np.zeros(len(u)))
        elif typ=="tube":b=bell*tt[i][j]*cx[h]
        else:b=bell*windows[i]*cx[j]*tt[1][h]
        rows.append(np.stack(np.broadcast_arrays(*b.parts(),u)[:6],axis=1))
    return np.stack(rows,axis=2)

def target(chart,u,v,order):return geom.chart_jet(chart,u,v,0.,order)

def image(chart,u,v,t,d,order,keys,co):
    f=base(chart,u,v,t,order,d)
    if not t or chart.endswith("+"):return f
    B=basis(chart,u,v,target(chart,u,v,order),keys)
    return f+B@co
