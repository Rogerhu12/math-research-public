"""R776, two-lobed inward parallel tube and its exact circumferential-speed companion.
The source returns the actual six material derivatives on all nine curves/surface charts.
"""
from functools import lru_cache
from math import factorial
import numpy as np
import r772_coherent_developing_tube as g
from r742_tilted_disk_two_jets import J, unary, gather
from r767_preloaded_cap_atlas import root

P, L, SM, HALF_WIDTH = g.P, g.L, g.SM, .5
Q0, Q1, ELL, TAPER = .008, 1.13, 1/16, .025
offset, disk_world = g.offset, g.disk_world
end_limits, normal_to_disk_material = g.end_limits, g.normal_to_disk_material
profile_marks = g.profile_marks

def axial_marks():
    h = g.guard.ROUND*ELL
    quarter = np.array([0., h, ELL-h, ELL, .25-ELL, .25-ELL+h, .25-h, .25])
    return np.unique(np.concatenate([quarter+i/4-.5 for i in range(4)])).tolist()

def wave(x):
    phase = np.mod(x,.5)
    sign = np.where(phase<.25,1.,-1.)
    z = np.where(sign>0,phase,.5-phase)
    u,du,_ = g.guard.clock(z/ELL)
    v,dv,_ = g.guard.clock((.25-z)/ELL)
    return sign*u*v, (du*v-u*dv)/ELL

def delta_q(t):
    return (Q1-Q0)*np.sin(t)**2

@lru_cache(maxsize=192)
def quarter_table(t,order):
    h = g.guard.ROUND*ELL
    knots = np.array([0.,h,ELL-h,ELL,.25-ELL,.25-ELL+h,.25-h,.25])
    n,w = g.rule(order)
    ds = np.diff(knots)
    vals = rates(knots[:-1,None]+ds[:,None]*n,t)
    return knots,np.vstack((np.zeros(3),np.cumsum(ds[:,None]*(vals@w).T,axis=0)))

def rates(x,t):
    k,_ = wave(x)
    dq = delta_q(t)
    return np.stack([np.cos((Q0+dq)*k),np.sin(Q0*k),
                     2*np.sin(dq*k/2)*np.cos((Q0+dq/2)*k)],axis=0)

def axial(x,t,order):
    frac = np.mod(x.v,.5)
    z = np.minimum(frac,.5-frac)
    knots,tab = quarter_table(t,order)
    idx = np.clip(np.searchsorted(knots,z,side="right")-1,0,len(knots)-2)
    h = z-knots[idx]
    nodes,w = g.rule(order)
    val = tab[idx]+h[:,None]*(rates(knots[idx,None]+h[:,None]*nodes,t)@w).T
    upper = frac>.25
    count = 2*np.floor(x.v/.5)
    prim = np.where(upper,2*tab[-1,0]-val[:,0],val[:,0])+count*tab[-1,0]
    k,kp = wave(x.v)
    dq = delta_q(t)
    q = (Q0+dq)*k
    s0,c0 = np.sin(Q0*k),np.cos(Q0*k)
    sd = 2*np.sin(dq*k/2)*np.cos((Q0+dq/2)*k)
    cd = -2*np.sin(dq*k/2)*np.sin((Q0+dq/2)*k)
    a = unary(x,.5-4*tab[-1,0]+prim,np.cos(q),-(Q0+dq)*kp*np.sin(q))
    z0 = unary(x,val[:,1],s0,c0*Q0*kp)
    dz = unary(x,val[:,2],sd,(dq*np.cos(q)+Q0*cd)*kp)
    return a,z0,dz

def pulse(s):
    z = s/g.QUARTER
    d = np.minimum(z,1-z)
    def smooth(u):
        v = np.clip(u,0.,1.)
        return v**4*(35+v*(-84+v*(70-20*v)))
    p = smooth(d/TAPER)*smooth((.5-d)/TAPER)
    return np.where(z<.5,p,-p)

def pulse_derivative(s):
    z = s/g.QUARTER
    d = np.minimum(z,1-z)
    def both(u):
        v = np.clip(u,0.,1.)
        return v**4*(35+v*(-84+v*(70-20*v))),140*v**3*(1-v)**3
    p,dp = both(d/TAPER)
    q,dq = both((.5-d)/TAPER)
    return (dp*q-p*dq)/(TAPER*g.QUARTER)

@lru_cache(maxsize=16)
def quadrature(order):
    cuts = np.unique(np.r_[0.,g.SM,g.QUARTER-g.SM,g.QUARTER,
                    g.QUARTER*np.array([TAPER,.5-TAPER,.5,.5+TAPER,1-TAPER])])
    n,w = g.rule(order)
    d = np.diff(cuts)
    x = (cuts[:-1,None]+d[:,None]*n).ravel()
    weight = (d[:,None]*w).ravel()
    a,k,_ = bend(x)
    weight *= np.cos(a-np.pi/4)
    b = pulse(x)
    # Entire function (1-cos(sqrt(G)*b))/G, power series on G in [0, pi^2/4].
    m = np.array([np.array([np.sum(weight*b**(2*j)),np.sum(weight*k*b**(2*j))])
                   *((-1.)**(j+1)/factorial(2*j)) for j in range(1,17)])
    return cuts,m

def bend(d):
    alpha = g.softened_angle(d,g.QUARTER,g.SM,1/g.R)
    z = np.clip(np.minimum(d,g.QUARTER-d)/g.SM,0.,1.)
    k = g.s5(z)/g.R
    kp = 30*z*z*(1-z)*(1-z)*np.where(d<g.QUARTER/2,1.,-1.)/(g.SM*g.R)
    return alpha,k,kp

def root_eq(h,z0,dz,m):
    g2 = h*dz
    total = m[-1,0]-z0*m[-1,1]
    for c,ck in m[-2::-1]:
        total = total*g2+(c-z0*ck)
    return h*total-np.sqrt(2.)

def amplitude(z0,dz,order):
    _,m = quadrature(order)
    lo,hi = np.zeros_like(z0.v),np.full_like(z0.v,20.)
    for _ in range(52):
        mid = (lo+hi)*.5
        pos = root_eq(mid,z0.v,dz.v,m)>0
        hi,lo = np.where(pos,mid,hi),np.where(pos,lo,mid)
    hv = (lo+hi)*.5
    eq = root_eq(J(hv,s=1.),z0,dz,m)
    hx = -eq.a/eq.s
    hxx = -(eq.aa+2*eq.sa*hx+eq.ss*hx*hx)/eq.s
    h = J(hv,a=hx,aa=hxx)
    # The smooth positive branch sqrt(delta z) is C^2 at each axial lobe edge.
    valid = dz.v>0
    sv = np.sqrt(np.where(valid,dz.v,1.))
    dx = np.where(valid,dz.a/(2*sv),0.)
    dxx = np.where(valid,(.5*dz.aa-dx*dx)/sv,0.)
    return root(h)*J(np.where(valid,sv,0.),a=dx,aa=dxx)

def perturb(s,phase,z0,dz,angle):
    # Local quadrant tangent data and its full first jet; only the primitive is added to the short base.
    alpha,k,kp = bend(s.v)
    c,ss = np.cos(alpha+phase),np.sin(alpha+phase)
    tx = unary(s,c,-k*ss,-kp*ss-k*k*c)
    tz = unary(s,-ss,-k*c,-kp*c+k*k*ss)
    off = np.clip(np.minimum(s.v,g.QUARTER-s.v)/g.SM,0.,1.)
    kpp = 60*off*(1-off)*(1-2*off)/(g.SM*g.SM*g.R)
    kk = unary(s,k,kp,kpp)
    b = unary(s,pulse(s.v),pulse_derivative(s.v),np.zeros_like(s.v))
    arg = b*angle
    co,si = g.trig(arg)
    a0 = 1-kk*z0
    tangent = a0*(co-1)+kk*dz
    return [tangent*tx,a0*si,tangent*tz]

def correction(e,z0,dz,ang,order):
    pos = np.mod(e.v,P)
    quad = np.floor(pos/g.BLOCK).astype(int)
    reach = np.clip(pos-quad*g.BLOCK-g.FLAT,0.,g.QUARTER)
    cuts,_ = quadrature(order)
    nodes,w = g.rule(order)
    def col(j):
        return J(j.v[:,None],a=np.broadcast_to(j.a,j.v.shape)[:,None],
                 aa=np.broadcast_to(j.aa,j.v.shape)[:,None])
    a0,dd,aa = col(z0),col(dz),col(ang)
    sums = np.zeros((3,3,len(pos)))
    for left,right in zip(cuts[:-1],cuts[1:]):
        h = np.clip(reach-left,0.,right-left)
        vals = perturb(J(left+h[:,None]*nodes),quad[:,None]*np.pi/2,a0,dd,aa)
        for i,f in enumerate(vals):
            for row,part in enumerate((f.v,f.a,f.aa)):
                sums[i,row] += h*(np.broadcast_to(part,(len(pos),order))@w)
    edge = perturb(J(reach,s=1.),quad*np.pi/2,z0,dz,ang)
    result = []
    for i,h in enumerate(edge):
        base,x,xx = sums[i]
        result.append(J(base,h.v,x,h.s,h.a,xx))
    return result

def chart_jet(chart,u,v,phase=0.,order=24,kind="short"):
    aa,bb = np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float))
    sh = aa.shape
    t = float(phase)
    if kind not in ("short","arclength"):
        raise ValueError(kind)
    if chart!="cylinder":
        f = g.chart_jet(chart,aa,bb,0.,order)
        if chart.endswith("-"):
            old = g.path_table(0.,order)[1][-1,0]
            f[...,0,1] += old-4*quarter_table(t,order)[1][-1,0]
        return f
    ua,xb = aa.ravel(),bb.ravel()+.5
    out = np.empty((len(ua),6,3))
    for idx in range(0,len(ua),192):
        sl = slice(idx,idx+192)
        e,x = J(ua[sl],s=1.),J(xb[sl],a=1.)
        a,z0,dz = axial(x,t,order)
        pt,n = g.section(e,order)
        z = z0+dz
        f = [pt[0]-z*n[0],a,pt[1]-z*n[1]]
        if kind=="arclength" and t!=0.:
            fix = correction(e,z0,dz,amplitude(z0,dz,order),order)
            f = [p+h for p,h in zip(f,fix)]
        out[sl] = gather(f,len(e.v))
    return out.reshape(sh+(6,3))
