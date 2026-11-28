"""Transport already integrated R750 rows on exactly equal physical Gauss nodes and weights."""
import numpy as np
from scipy.sparse import csr_matrix

import r750_relative_boundary as original
import r760_relative_material_rows as rows


def pair(old,new,oldrule,newrule,oldq,q):
    if old['ns']!=1 or new['ns']!=1 or not np.array_equal(old['ss'],new['ss']):
        raise ValueError('quadrature response transfer needs one identical material label')
    newidx,oldidx=rows.matched_rows(oldrule,newrule)
    n0=len(oldq)//3
    good=(new['weights'][newidx]==old['weights'][oldidx])
    good&=np.all(new['matrix'][newidx]==old['matrix'][oldidx],axis=(1,2))
    good&=np.all(new['pr'][newidx]==old['pr'][oldidx],axis=1)
    bn,bo=original.controls(new),original.controls(old)
    # Reuse only when the right Euler field agrees as well. Equal old physical
    # coefficients on transported radial nodes were copied when making new.
    prefix=bn[newidx,:n0]-bo[oldidx]
    for i in np.flatnonzero(np.diff(prefix.indptr)):
        if np.any(prefix.data[prefix.indptr[i]:prefix.indptr[i+1]]!=0):good[i]=False
    if np.any(q[3*n0:]):
        good&=np.all(bn[newidx,n0:]@q[3*n0:].reshape(-1,3)==0,axis=1)
    return (np.setdiff1d(np.arange(len(old['weights'])),oldidx[good],assume_unique=True),
            np.setdiff1d(np.arange(len(new['weights'])),newidx[good],assume_unique=True),int(np.sum(good)))


def integral(piece,q,ix,cols=None):
    width=0 if cols is None else 3*(cols[1]-cols[0])
    if not len(ix):return np.zeros(3) if cols is None else np.zeros((3,width))
    b=original.controls(piece)[ix]
    ang=b@q.reshape(-1,3);wt=piece['weights'][ix]
    (x,dx),(y,dy),(z,dz)=[original.weak.fields.rotation(ang[:,j],j) for j in range(3)]
    m=piece['matrix'][ix];pr=piece['pr'][ix]
    apply=original.weak.fields.apply
    mx=m@x;zp=apply(z,pr);yp=apply(y,zp)
    if cols is None:return wt@(apply(mx,yp)-pr)
    bt=b[:,cols[0]:cols[1]].T.tocsr()
    out=np.empty((3,width//3,3))
    d=(apply(m@dx,yp),apply(mx@dy,zp),apply(mx@y@dz,pr))
    for i,v in enumerate(d):out[:,:,i]=(bt@(wt[:,None]*v)).T
    return out.reshape(3,width)


def adopt(old,new,oldrule,newrule,oldq,q,parent_value,derivative):
    oi,ni,number=pair(old,new,oldrule,newrule,oldq,q);n0=len(oldq)//3
    if derivative:
        prefix=parent_value+integral(new,q,ni,(0,n0))-integral(old,oldq,oi,(0,n0))
        tail=integral(new,q,np.arange(len(new['weights'])),(n0,new['nterm']))
        val=np.column_stack((prefix,tail))
    else:
        if not np.array_equal(new['goals'],old['goals']):
            raise ValueError('relative target changed for the same R750 physical label')
        val=parent_value+integral(new,q,ni)-integral(old,oldq,oi)
    return val,dict(unchanged_original_Gauss_rows=number,subtracted_original_rows=len(oi),
                    charged_new_or_changed_rows=len(ni),full_new_columns=3*(new['nterm']-n0))
