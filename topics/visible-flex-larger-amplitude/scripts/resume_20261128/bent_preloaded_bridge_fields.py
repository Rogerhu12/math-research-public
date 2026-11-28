"""Material dictionaries and finite training/validation charts for both R770 closed bridges."""
import numpy as np
from r742_tilted_disk_two_jets import J,trig,unary,cap_s7
import r767_negative_track_profile as g
import r767_preloaded_cap_atlas as cap
import r770_compensated_negative_bridge_two_jets as ref

def profile_marks():
    cuts=[0.,g.RAMP*g.ROUND,g.RAMP*(1-g.ROUND),g.RAMP,.5,1-g.RAMP,
          1-g.RAMP*(1-g.ROUND),1-g.RAMP*g.ROUND,1.,1+g.HEAD_BLEND,
          1+g.HEAD_L/2,1+g.HEAD_L-g.HEAD_BLEND]
    return sorted(set([*cuts,*[g.P/2+x for x in cuts]]))

def end_marks():
    return sorted(set([*(ref.L*x for x in ref.abscissae()),ref.L,
              ref.L+cap.OUTER_BLEND,ref.L+cap.OUTER_L-cap.OUTER_BLEND,ref.L+cap.OUTER_L]))

def grid(ns,nv,order,independent=False):
    a=(.418 if independent else .0);b=(.314 if independent else 0.)
    s=np.unique(np.r_[profile_marks(),np.mod(g.P*(np.arange(ns)+a)/ns,g.P)])
    u=np.unique(np.r_[end_marks(),(cap.OUTER_L+ref.L)*(np.arange(nv)+b)/nv])
    rad=np.unique(np.r_[.018,(np.arange(1,max(nv//2,4)+1)-b)/max(nv//2,4),1.])
    def mesh(x,y):
        xx,yy=np.meshgrid(x,y,indexing="ij");return xx.ravel(),yy.ravel()
    out=[("cylinder",*mesh(s,[-ref.Y,-.5*ref.Y,0.,.5*ref.Y,ref.Y]))]
    # The Cartesian chart is world x,z, including the actual tiny nonplanar crown.
    center=cap.disk_world(J(np.array([0.])),J(np.array([0.])),order)
    cp=np.array([z.v[0] for z in center]);q,tt,n,_,_=g.coordinates(np.array([cap.RIGHT]),0.,order)
    crown=q[0]-.127*n[0];az=2*np.pi*(np.arange(18)+a)/18.
    X=np.r_[cp[0],crown[0],*(crown[0]+d*np.cos(az) for d in (.003,.006,.009,.011,.012))]
    Z=np.r_[cp[1],crown[1],*(crown[1]+d*np.sin(az) for d in (.003,.006,.009,.011,.012))]
    for side in "+-":
        out.extend([("end"+side,*mesh(s,u)),("end-outer"+side,s,np.full_like(s,ref.L)),
                  ("cap"+side,*mesh(s,rad)),("cap-normal"+side,*mesh(s,[0.,.003,.01])),
                  ("cap-cartesian"+side,X,Z)])
    return out

def cheb(x,n):
    vals=[J(1.+0.*x.v),x]
    for _ in range(2,n+1):vals.append(2*x*vals[-1]-vals[-2])
    return vals[:n+1]

def b3(x):
    h=np.maximum(x.v,0.)
    return unary(x,h**3,3*h*h,6*h)

def names(level):
    # Hierarchical enumeration: every old physical coefficient has precisely the same column.
    n=level+1
    out=[("body",i,j,k) for i in range(n+2) for j in range(n+2-i)
         for k in range(min(3,n+2)+1) if i+j+k<=n+2]
    out += [("rim",i,j,k) for i in range(n+1) for j in range(n+1-i) for k in (0,1,2)]
    out += [("bridge",m,tr,j) for m in range(1,n+2) for tr in (0,1)
            for j in range(n+1) if m+j<=n+1]
    out += [("head",h,j,tr) for h in (0,1) for j in range(n+1) for tr in (0,1)]
    out += [("fraction",e,m,tr) for e in (0,1) for m in range(n+1)
            for tr in ((0,) if m==0 else (0,1))]
    return out

def basis(chart,u,v,F0,ns):
    # Shared body/rim fields are functions of the SAME frozen world F0 across all charts.
    shape=np.shape(u);N=len(u)
    if chart=="cylinder":return np.zeros((N,6,len(ns)))
    side=1 if chart.endswith("+") else -1
    X,Y,Z=[J(*(F0[:,:,i].T)) for i in range(3)]
    dep=(side*Y-ref.Y)/ref.L
    gate=b3(dep)/(1+b3(dep))
    dx=X+.50;dz=(Z+.025)*1.6
    degree=max(3,max(int(n[1]) for n in ns if n[0]=="body")+2)
    px=cheb(dx,degree);pz=cheb(dz,degree);pv=cheb(dep-0.60,degree)
    # local shell wave functions include true first and second normal data at the rim in world coordinates
    d=dep-ref.old.axial0(20)/ref.L
    from r742_tilted_disk_two_jets import unary
    h0=unary(d,np.exp(-16*d.v*d.v),-32*d.v*np.exp(-16*d.v*d.v),
             (1024*d.v*d.v-32)*np.exp(-16*d.v*d.v))
    rim=[h0,h0*d,h0*d*d]
    S=J(u,s=1.);V=J(v/ref.L,a=1/ref.L)
    isend=chart.startswith("end") and "outer" not in chart
    if isend:
        left=b3(V);right=b3(1-V);br=64*left*right;local=cheb(2*V-1,degree+1)
        ang=2*np.pi*S/g.P;tt=[trig(i*ang) for i in range(degree+2)]
        def pow52(q):
            y=np.maximum(q.v,0.)
            return unary(q,y**2.5,2.5*y**1.5,3.75*np.sqrt(y))
        frac=[30*pow52(V)*right,30*left*pow52(1-V)]
        gates=[]
        for c in (1+g.HEAD_L*.5,2+1.5*g.HEAD_L):
            z=trig(ang-2*np.pi*c/g.P)[0]
            gates.append(cap_s7((z-.30)/.60))
    result=[]
    for typ,i,j,k in ns:
        if typ=="body":val=gate*px[i]*pz[j]*pv[k]
        elif typ=="rim":val=gate*px[i]*pz[j]*rim[k]
        elif not isend:val=J(np.zeros(N))
        elif typ=="bridge":val=br*tt[i][j]*local[k]
        elif typ=="head":val=br*gates[i]*local[j]*(tt[1][k])
        else:val=frac[i]*tt[j][k]
        result.append(np.stack(np.broadcast_arrays(*val.parts(),u)[:6],axis=1))
    return np.stack(result,axis=2)

def target(chart,u,v,order):return ref.chart_jet(chart,u,v,0.,order)

def image(chart,u,v,t,design,order,ns,coeff):
    f=ref.chart_jet(chart,u,v,t,order,design)
    if chart=="cylinder" or not t:return f
    zero=target(chart,u,v,order);B=basis(chart,u,v,zero,ns)
    return f+B@coeff[0 if chart.endswith("+") else 1]
