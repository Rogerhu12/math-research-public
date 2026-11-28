"""R763 complete true R757 initial metric, with either R761 tube-safe moving caps
or independently moved exact original caps. Both rims have open shared physical jets.
"""
import numpy as np
import r759_paired_curvature_tracks as paired
import r761_paired_tube_safe_nonflat_caps as tube
from r742_tilted_disk_two_jets import J,cap_s7,gather
g=paired.g
delay=paired.delay

def chart_jet(chart,u,v,phase=0.,design=None,order=32):
    p={} if design is None else design
    amp=p.get("angle",.78);nr=p.get("ramp_cells",2);kind=p.get("cap","translated")
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    s=aa.ravel();v=bb.ravel();t=float(phase)
    if not t:return delay.chart_jet(chart,s,v,0.,order,bend=0.,rotate=False).reshape(sh+(6,3))
    if kind=="tube":
        # On the rim itself the R761 velocity flow is identically the parallel
        # normal-label trace in an open collar; bypass an unnecessary ODE.
        if chart.startswith("cap") and "cartesian" not in chart:
            w=v if "normal" in chart else 1-v
            direct=w<=1.e-8
            if np.any(direct):
                out=np.empty((len(s),6,3))
                a=J(s[direct],s=1.);b=J(v[direct],a=1.)
                w=b if "normal" in chart else 1-b
                theta=amp*np.sin(t);P=tube.normal(a,w,theta,nr,order)
                sg=1 if chart.endswith("+") else -1
                y=sg*(delay.HALF_WIDTH+delay.end_limits(order)[0]+tube.crown(P,theta,nr,order))
                out[direct]=gather((P[0],y,P[1]),direct.sum())
                if np.any(~direct):out[~direct]=tube.chart_jet(chart,s[~direct],v[~direct],t,amp,nr,order)
                return out.reshape(sh+(6,3))
        return tube.chart_jet(chart,s,v,t,amp,nr,order).reshape(sh+(6,3))
    if kind not in ("translated","developed"):raise ValueError("unknown R763 cap mechanism")
    if chart=="cylinder":
        return paired.field(chart,s,v,t,amp,nr,(0.,)*6,order).reshape(sh+(6,3))
    a=J(s,s=1.);b=J(v,a=1.);time=np.sin(t);theta=amp*time
    total=paired.integration(theta,nr,order)[1][-1]
    shift=-.5*total;sg=1 if chart.endswith("+") else -1
    dy=-sg*p.get("shorten",.23)*time;pb,db=delay.end_limits(order)
    if chart.startswith("end"):
        q0,n0=g.profile(a,order);qt,nt=paired.profile(a,theta,nr,order)
        pp,dd=delay.end_offsets(b,order);yc=sg*(delay.HALF_WIDTH+pp);fade=cap_s7(b/delay.END_LENGTH)
        X0,Z0=[q0[i]-dd*n0[i] for i in range(2)]
        X,Z=[qt[i]-dd*nt[i] for i in range(2)];height=J(0.)
    else:
        X0,y0,Z0=delay.sphere_chart(chart,a,b,np.zeros(len(s)),order,"legacy")
        yc=y0;X,Z=X0,Z0;fade=J(1.);height=y0-sg*(delay.HALF_WIDTH+pb)
    ddx=J(0.);ddy=J(0.)
    if kind=="developed":
        # A true unit-speed development along X. Curvature is confined to a
        # compact hinge disjoint from the radius-.04 R757 raised disk.
        lo=-.83;span=.20
        xx=X0.v;w=np.clip((xx-lo)/span,0.,1.)
        coeff=sg*p.get("development",.22)*time
        ss=np.sin(np.pi*w);cc=np.cos(np.pi*w)
        beta=coeff*ss**4;bp=4*np.pi/span*coeff*ss**3*cc
        nodes,weights=g.disk.rule(order);at=w[:,None]*nodes
        al=coeff*np.sin(np.pi*at)**4
        dx=span*w*((np.cos(al)-1)@weights)
        yy=span*w*(np.sin(al)@weights)
        co=np.cos(beta);si=np.sin(beta)
        ddx=unary1(X0,dx,co-1,-si*bp)
        ddy=unary1(X0,yy,si,co*bp)
        # Normal extension of the actual initial graph height.
        sn=unary1(X0,si,co*bp,-si*bp*bp+co*angle2(w,coeff,span))
        cs=unary1(X0,co,-si*bp,-co*bp*bp-si*angle2(w,coeff,span))
        ddx=ddx-height*sn;ddy=ddy+height*(cs-1)
    x=X+fade*(X0-X+shift[0]+ddx);z=Z+fade*(Z0-Z+shift[1])
    y=yc+fade*(dy+ddy)
    return gather((x,y,z),len(s)).reshape(sh+(6,3))

def unary1(x,v,p,q):
    from r742_tilted_disk_two_jets import unary
    return unary(x,v,p,q)

def angle2(w,coeff,span):
    si=np.sin(np.pi*w);co=np.cos(np.pi*w)
    return 4*coeff*(np.pi/span)**2*(3*si*si*co*co-si**4)
