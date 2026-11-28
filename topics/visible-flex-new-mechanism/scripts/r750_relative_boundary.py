"""Genuine endpoint displacement and its all-column derivative on the physical annulus."""
import numpy as np
from scipy.sparse import csr_matrix

import r750_rigid_annulus as material


weak=material.weak


def ray_grid(build,physics,order):
    anchor=float(build.radius_at(np.array([material.CLOSE_ELL]))[0])
    cuts=physics.true_breaks(build,np.array([anchor,1.]))
    cuts=np.unique(np.r_[anchor,cuts[(cuts>anchor)&(cuts<1.)],1.])
    z,w=weak.physical.quadrature(order)
    half=np.diff(cuts)/2
    radius=(cuts[:-1,None]+half[:,None]*(1+z)).ravel()
    weights=(half[:,None]*w).ravel()
    return dict(anchor=anchor,radius=radius,weights=weights,cuts=cuts,order=order)


def kernel(build,phase,degree,ss,grid):
    rs=grid['radius'];nr=len(rs);ns=len(ss)
    base=[];pr=[];ind=[];ptr=[0];data=[]
    # The integral needs just beta_r, its control values and the true source
    # radial differential. Expensive source frames are generated in real panels.
    for lo in range(0,nr,96):
        f=material.R750Frame(build,phase,rs[lo:lo+96,None],ss[None,:],degree)
        base.append(f.base);pr.append(f.j0[1]);sparse=csr_matrix(f.B)
        offset=ptr[-1]
        ptr.extend((sparse.indptr[1:]+offset).tolist())
        ind.append(sparse.indices);data.append(sparse.data)
    ri=np.full_like(ss,grid['anchor'])
    pi=build.geometry(ri,ss)[0][0]
    # A rigid interior entire open band gives this non-asymptotic anchor.
    # Compute its displacement from the genuine material source, separately
    # from the integrated correction. The outer endpoints are true ring data.
    goal=build.boundary_jets(phase,ss)[0]-build.boundary_jets(0.,ss)[0]
    shift=material.core_shift(build,phase)
    origin=np.r_[build.profile.endx,build.ring.origin]
    inside=shift+(pi-origin)@(material.turn(phase)-np.eye(3)).T
    goal-=inside
    return dict(shape=(nr,ns),ns=ns,ss=ss,weights=grid['weights'],goals=goal,
                physical_source_inner=pi,inner_displacement=inside,
                matrix=np.concatenate(base),pr=np.concatenate(pr),nterm=len(material.tags(degree)),
                data=np.concatenate(data),indices=np.concatenate(ind),indptr=np.asarray(ptr,dtype=np.int64))


def controls(piece):
    nr,ns=piece['shape']
    return csr_matrix((piece['data'],piece['indices'],piece['indptr']),shape=(nr*ns,piece['nterm']))


def evaluate(piece,q,derivatives=False):
    B=controls(piece)
    angles=B@np.asarray(q).reshape(-1,3)
    matrices=[weak.fields.rotation(angles[:,i],i) for i in range(3)]
    base=piece['matrix'];pr=piece['pr']
    (x,dx),(y,dy),(z,dz)=matrices
    left=base@x
    right=weak.fields.apply(z,pr)
    ypr=weak.fields.apply(y,right)
    nr,ns=piece['shape'];wt=piece['weights']
    if not derivatives:
        beta=weak.fields.apply(left,ypr)
        residual=np.einsum('i,ijk->jk',wt,(beta-pr).reshape(nr,ns,3))-piece['goals']
        if not np.isfinite(residual).all():
            raise ArithmeticError('nonfinite R750 physical endpoint displacement')
        return residual
    channels=(weak.fields.apply(base@dx,ypr),weak.fields.apply(left@dy,right),
              weak.fields.apply(left@y@dz,pr))
    out=np.empty((ns,3,B.shape[1],3))
    for j in range(ns):
        rows=np.arange(j,nr*ns,ns)
        bt=B[rows].T.tocsr()
        for axis,ch in enumerate(channels):
            out[j,:,:,axis]=(bt@(wt[:,None]*ch[rows])).T
    return out.reshape(ns*3,B.shape[1]*3)


def derivative(piece,q,ids):
    block=evaluate(piece,q,derivatives=True)
    defects=[]
    for j in ids:
        z=np.asarray(q,dtype=complex).copy();z[j]+=1.e-24j
        exact=evaluate(piece,z).imag.ravel()/1.e-24
        defects.append(float(np.max(abs(exact-block[:,j]))/max(1.,np.max(abs(exact)))))
    if not np.isfinite(defects).all() or max(defects)>2.e-10:
        raise ArithmeticError('R750 integrated all-column endpoint derivative failed the original complex-step check')
    return dict(block=block,independent_columns=ids,scaled_check_defects=defects)
