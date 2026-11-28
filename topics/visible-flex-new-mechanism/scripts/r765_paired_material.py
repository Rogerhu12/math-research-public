"""Two equal physical arclength windows. The same ambient rotation fixes their vector sum."""
from math import factorial

import numpy as np
from scipy.sparse import csr_matrix, hstack

import r763_material_twist as twist

model=twist.material
SUM=.811
OUTER=(.060,.080)
INNER=(.731,.751)
ACTIVE=(.062,.078)


def tags(degree):
    if degree not in (3,5):raise ValueError('R765 uses the original two material degrees')
    return [('paired_U',side,radial,angular) for side in (1,3)
            for radial in range(1 if degree==3 else 3) for angular in range(2 if degree==3 else 4)]


def polynomial(t,n):
    x=2.*t-1.
    if n==0:return np.ones_like(x),np.zeros_like(x)
    if n==1:return x,2.*np.ones_like(x)
    if n==2:return (3.*x*x-1.)/2.,6.*x
    if n==3:return (5.*x**3-3.*x)/2.,15.*x*x-3.
    raise ValueError('unexpected material polynomial')


def enveloped(t,n):
    p,dp=polynomial(t,n);b,db=twist.bump(t)
    return b*p,db*p+b*dp


def new_basis(build,degree,u,s):
    u,s=np.broadcast_arrays(np.asarray(u,float),np.asarray(s,float))
    u,s=u.ravel(),s.ravel()
    d,kind,_=build.ring.label(s)
    lu,per=build.ring.LU,build.ring.length
    width=ACTIVE[1]-ACTIVE[0]
    t=np.clip((u-ACTIVE[0])/width,0.,1.)
    radial={i:enveloped(t,i) for i in range(1 if degree==3 else 3)}
    angular={}
    for side,offset in ((1,2.),(3,4.+lu)):
        v=(d-offset)/lu
        z=np.where(kind==side,np.clip((v-.10)/.80,0.,1.),0.)
        for j in range(2 if degree==3 else 4):
            val,der=enveloped(z,j);angular[side,j]=val,der*per/(.80*lu)
    controls=tags(degree);a,au,az=(np.zeros((len(u),len(controls))) for _ in range(3))
    for k,(_,side,i,j) in enumerate(controls):
        f,fd=radial[i];g,gd=angular[side,j]
        a[:,k]=f*g;au[:,k]=fd*g/width;az[:,k]=f*gd
    return a,au,az


def initial(phase,degree,side_signs,factor=.20):
    return np.asarray([factor*phase**.25*side_signs[0 if side==1 else 1]
        if i==0 and j==0 else 0. for _,side,i,j in tags(degree)])


def skew(v):
    out=np.zeros((len(v),3,3),dtype=v.dtype)
    x,y,z=v.T
    out[:,0,1]=-z;out[:,0,2]=y;out[:,1,0]=z
    out[:,1,2]=-x;out[:,2,0]=-y;out[:,2,1]=x
    return out


def polynomial_and_derivative(z,coeff):
    val=np.full_like(z,coeff[-1]);der=np.zeros_like(z)
    for c in coeff[-2::-1]:
        der=der*z+val;val=val*z+c
    return val,der


def exponential_jet(v,vu,vs):
    """Return H-I and the two derivatives; entire in the rotation vector, including at S=0."""
    norm2=np.einsum('ij,ij->i',v,v)
    small=abs(norm2)<.01
    f,fd,g,gd=(np.empty_like(norm2) for _ in range(4))
    z=norm2[small]
    coeff=lambda j:[(-1.)**k/factorial(2*k+j) for k in range(9)]
    f[small],fd[small]=polynomial_and_derivative(z,coeff(1))
    g[small],gd[small]=polynomial_and_derivative(z,coeff(2))
    if np.any(~small):
        z=norm2[~small];w=np.sqrt(z)
        sv=np.sin(w)/w;cv=.5*(np.sin(w/2.)/(w/2.))**2
        f[~small],g[~small]=sv,cv
        fd[~small]=(np.cos(w)-sv)/(2.*z);gd[~small]=(.5*sv-cv)/z
    A=skew(v);A2=A@A
    col=lambda t:t[:,None,None]
    delta=col(f)*A+col(g)*A2
    def differentiated(vq):
        B=skew(vq);zz=2.*np.einsum('ij,ij->i',v,vq)
        return col(f)*B+col(g)*(B@A+A@B)+col(zz)*(col(fd)*A+col(gd)*A2)
    return delta,differentiated(vu),differentiated(vs)


def unit_radial(jets,er,err):
    _,br,_,brs,brr,_=jets
    L=br/er[:,None]
    return L,(brr-err[:,None]*L)/(er[:,None]**2),brs/er[:,None]


def paired_jet(primary,partner,primary_ell,companion_ell,first,ax):
    """The argument first identifies the side of each actual native row; the sample's s is normalized."""
    _,er,err=primary_ell
    _,ger,gerr=companion_ell
    l,l_ell,l_s=unit_radial(primary,er,err)
    m,m_ell,m_s=unit_radial(partner,ger,gerr)
    side=np.where(first,1.,-1.)[:,None]
    L1=np.where(first[:,None],l,m)
    L1u=np.where(first[:,None],l_ell,m_ell)
    L1s=np.where(first[:,None],l_s,m_s)
    a,au,az=(v[:,None] for v in ax)
    total=l+m
    v=a*total
    vu=au*total+a*side*(l_ell-m_ell)
    vs=az*total+a*(l_s+m_s)
    diff,du,dz=exponential_jet(v,vu,vs)
    apply=model.weak.fields.apply
    W=apply(diff,L1)
    Wu=apply(du,L1)+apply(diff,L1u)
    Ws=apply(dz,L1)+apply(diff,L1s)
    dr=er[:,None,None]*side[:,:,None]*du
    kr,br,bs,brs,brr,bss=primary
    result=(kr+apply(diff,kr)+apply(dr,bs)-apply(dz,br),
            br+er[:,None]*side*W,bs+apply(diff,bs),
            brs+er[:,None]*side*Ws,brr+err[:,None]*side*W+(er[:,None]**2)*Wu,
            bss+apply(diff,bss)+apply(dz,bs))
    return result,dict(E=W,E_u=Wu,E_s=Ws,H_minus_I=diff,H_u=du,H_s=dz)


def physical_parts(frame,q):
    c=np.asarray(q).reshape(-1,3)
    return [a@c for a in (frame.B,frame.Br,frame.Bs)]


def source_companion(build,phase,frame):
    ell,_,_=model.space.ell_data(frame.r)
    u=np.minimum(ell,SUM-ell)
    p=new_basis(build,frame.degree,u,frame.s)
    active=np.any(p[0]!=0,axis=1)|np.any(p[1]!=0,axis=1)|np.any(p[2]!=0,axis=1)
    ids=np.flatnonzero(active)
    if not len(ids):return None
    other=build.radius_at(SUM-ell[ids])
    companion=model.R760Frame(build,phase,other,frame.s[ids],frame.degree)
    actual=model.space.ell_data(other)[0]
    if np.max(abs(actual+ell[ids]-SUM))>5.e-14:
        raise ArithmeticError('paired native points did not return to the required equal arclengths')
    return dict(ids=ids,companion=companion,first=ell[ids]<.40,
                pair_basis=tuple(a[ids] for a in p))


def all_local(primary,partner,original_parts,other_parts,a_old,a_pair,
              first,el0,el1):
    base=twist.original_from_local(primary,*original_parts)
    other=twist.original_from_local(partner,*other_parts)
    if a_old is not None:
        base=twist.turn_jets(base,twist.source_direction(primary.j0),*a_old)
    return paired_jet(base,other,el0,el1,first,a_pair)


def physical(primary,partner,q,z,y,old_basis,pair_basis,first):
    el0,el1=model.space.ell_data(primary.r),model.space.ell_data(partner.r)
    return all_local(primary,partner,physical_parts(primary,q),physical_parts(partner,q),
        [m@z for m in old_basis],[m@y for m in pair_basis],first,el0,el1)


def local_operator(primary,partner,q,z,y,old_basis,pair_basis,first):
    """Complete complex local differential, including old Euler controls at the companion label."""
    data=[physical_parts(primary,q),physical_parts(partner,q),
          [v@z for v in old_basis],[v@y for v in pair_basis]]
    el0,el1=model.space.ell_data(primary.r),model.space.ell_data(partner.r)
    def curl(parts):
        jets,_=all_local(primary,partner,*parts,first,el0,el1)
        return jets[0]/primary.det[:,None]
    n=len(primary.r);new=np.zeros((n,3,len(y)))
    original=np.zeros((n,3,len(q)//3,3));aux=np.zeros((n,3,len(z)))
    step=1.e-24;channels=[]
    for group,grids in enumerate(((primary.B,primary.Br,primary.Bs),(partner.B,partner.Br,partner.Bs),
                                  old_basis[:2],pair_basis)):
        for j,grid in enumerate(grids):
            for axis in range(3 if group<2 else 1):
                parts=[list(row) for row in data]
                value=parts[group][j].astype(complex)
                if group<2:value[:,axis]+=step*1j
                else:value+=step*1j
                parts[group][j]=value
                ch=curl(parts).imag/step;channels.append(ch)
                addition=ch[:,:,None]*grid[:,None,:]
                if group<2:original[:,:,:,axis]+=addition
                elif group==2:aux+=addition
                else:new+=addition
    blocks=[csr_matrix(v.reshape(n*3,-1)) for v in (original,aux,new)]
    return hstack(blocks,format='csr'),np.asarray(channels)
