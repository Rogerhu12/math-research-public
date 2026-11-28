"""Finite angular corrugations on the R776 fixed metric; complete material two-jets on the closed sphere."""
from functools import lru_cache
from math import factorial
import numpy as np
import r776_short_inward_tube_and_spatial_corners as a
from r742_tilted_disk_two_jets import J,unary,trig,gather
from r767_preloaded_cap_atlas import root

g=a.g
P,L,SM,HALF_WIDTH=a.P,a.L,a.SM,a.HALF_WIDTH
offset,end_limits=a.offset,a.end_limits
disk_world,normal_to_disk_material=a.disk_world,a.normal_to_disk_material
profile_marks,axial_marks=a.profile_marks,a.axial_marks
NTERMS=16
POWERS=np.arange(1,2*NTERMS+2)

def pulse(u):
    return a.pulse(u*g.QUARTER),g.QUARTER*a.pulse_derivative(u*g.QUARTER)

@lru_cache(maxsize=12)
def moment_table(order):
    # Split all compact pulse joins. These are ordinary integrals of integer powers.
    cuts=np.array([0.,a.TAPER,.5-a.TAPER,.5,.5+a.TAPER,1-a.TAPER,1.])
    nodes,w=g.rule(order);h=np.diff(cuts)
    raw=pulse(cuts[:-1,None]+h[:,None]*nodes)[0]
    vals=(raw[:,:,None]**POWERS[None,None,:]).transpose(0,2,1)@w
    tab=np.vstack((np.zeros(len(POWERS)),np.cumsum(h[:,None]*vals,axis=0)))
    # Use exact opposite signs of the two matching pulse halves for the full odd moments.
    tab[-1,::2]=0.
    return cuts,tab

def partial_moments(y,order):
    cuts,tab=moment_table(order)
    idx=np.clip(np.searchsorted(cuts,y.v,side="right")-1,0,len(cuts)-2)
    h=y.v-cuts[idx];nodes,w=g.rule(order)
    p=pulse(cuts[idx,None]+h[:,None]*nodes)[0]
    B=tab[idx]+h[:,None]*((p[:,:,None]**POWERS[None,None,:]).transpose(0,2,1)@w)
    py,dy=pulse(y.v)
    return [unary(y,B[:,i],py**j,j*py**(j-1)*dy) for i,j in enumerate(POWERS)]

def series(z,coeff):
    h=coeff[-1]
    for c in coeff[-2::-1]:
        h=h*z+c
    return h

def positive_root(j):
    mask=j.v>0
    v=np.sqrt(np.where(mask,j.v,1.))
    return unary(j,np.where(mask,v,0.),np.where(mask,.5/v,0.),np.where(mask,-.25/v**3,0.))

def angle_parameters(d,dk,zeta,speed0,order):
    full=moment_table(order)[1][-1]
    coeff=[(-1.)**(j+1)*full[2*j-1]/factorial(2*j) for j in range(1,NTERMS+1)]
    def fun(h,v):return h*series(h*v,coeff)-1
    lo,hi=np.full(d.v.shape,1.9),np.full(d.v.shape,4.)
    for _ in range(52):
        mid=(lo+hi)/2
        mask=fun(mid,d.v)>0
        lo,hi=np.where(mask,lo,mid),np.where(mask,mid,hi)
    val=(lo+hi)/2
    eq=fun(J(val,s=1.),J(d.v,a=1.))
    c=-eq.a/eq.s
    c2=-(eq.aa+2*eq.sa*c+eq.ss*c*c)/eq.s
    h=unary(d,val,c,c2)
    # Factor sqrt(k*DeltaZ/a0) to preserve both axial edge limits and high-order phase zeros.
    ang=positive_root(dk)*positive_root(zeta)*root(h/speed0)
    return ang,h*d

def wave_jet(x,theta):
    k,kp=a.wave(x.v)
    frac=np.mod(x.v,.5);positive=frac<.25;z=np.where(positive,frac,.5-frac)
    u,du,ddu=g.guard.clock(z/a.ELL)
    v,dv,ddv=g.guard.clock((.25-z)/a.ELL)
    kpp=np.where(positive,1.,-1.)*(ddu*v-2*du*dv+u*ddv)/a.ELL**2
    return (a.Q0+a.delta_q(theta))*unary(x,k,kp,kpp)

def core(e,x,t,harmonics,order):
    ax,z0,dz=a.axial(x,t,order)
    c,n=g.section(e,order)
    z=z0+dz
    f=[c[0]-z*n[0],ax,c[1]-z*n[1]]
    pos=np.mod(e.v,P)
    block=np.floor(pos/g.BLOCK).astype(int)
    local=pos-block*g.BLOCK-g.FLAT
    dc=np.clip(local,0.,g.QUARTER)
    turn,k,kp=a.bend(dc)
    w=np.clip(np.minimum(dc,g.QUARTER-dc)/g.SM,0.,1.)
    kpp=60*w*(1-w)*(1-2*w)/(g.R*g.SM**2)
    curvature=unary(e,k,kp,kpp)
    co,si=trig(unary(e,turn+block*np.pi/2,k,kp))
    cq,sq=trig(wave_jet(x,t))
    tang=[co,0.,-si]
    norm=[cq*n[0],sq,cq*n[1]]
    a0=1-curvature*z0
    deficit=curvature*dz/a0
    ang,G=angle_parameters(deficit,curvature,dz,a0,order)
    eps=g.QUARTER/harmonics
    y=J(np.mod(dc/eps,1.),s=1/eps)
    moment=partial_moments(y,order)
    even=[(-1.)**(j+1)*moment[2*j-1]/factorial(2*j) for j in range(1,NTERMS+1)]
    odd=[(-1.)**j*moment[2*j]/factorial(2*j+1) for j in range(NTERMS+1)]
    along=a0*(deficit*y-G*series(G,even))
    outward=a0*ang*series(G,odd)
    return [p+eps*(along*T+outward*N) for p,T,N in zip(f,tang,norm)]

def chart_jet(chart,u,v,phase=0.,order=24,harmonics=1):
    if int(harmonics)!=harmonics or harmonics<1:
        raise ValueError("harmonics must be a positive integer")
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float))
    if chart!="cylinder" or float(phase)==0.:
        return a.chart_jet(chart,aa,bb,phase,order,"short")
    out=np.empty((aa.size,6,3))
    for i in range(0,aa.size,128):
        sl=slice(i,i+128)
        e=J(aa.ravel()[sl],s=1.);x=J(bb.ravel()[sl]+.5,a=1.)
        out[sl]=gather(core(e,x,float(phase),int(harmonics),order),len(e.v))
    return out.reshape(aa.shape+(6,3))
