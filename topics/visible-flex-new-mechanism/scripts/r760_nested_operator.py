"""Reuse compatible original R750 rows, columns, responses and Householder subtrees."""
from types import SimpleNamespace

import numpy as np
from scipy.sparse import coo_matrix,csr_matrix,hstack,vstack
import r760_full_annulus_frame as material
from r754_tsqr_reuse import tsqr_factor


def csr(data):return csr_matrix((data['data'],data['indices'],data['indptr']),shape=data['shape'])

def raw(mat):return {k:getattr(mat,k) for k in ('data','indices','indptr','shape')}

def vector_rows(ix):return (3*np.asarray(ix,dtype=int)[:,None]+np.arange(3)).ravel()


def native_parent(frame,q,phase,prior,old_nodes):
    nold=3*len(material.old.tags(frame.degree));oldq=q[:nold]
    ro,so=old_nodes;r=frame.r.reshape(frame.shape)[:,0];s=frame.s.reshape(frame.shape)[0]
    rr=np.searchsorted(r,ro);ss=np.searchsorted(s,so)
    if (np.any(rr>=len(r)) or np.any(ss>=len(s)) or not np.array_equal(r[rr],ro)
            or not np.array_equal(s[ss],so)):raise ValueError('old native row ordering lost')
    rows=(rr[:,None]*len(s)+ss).ravel()
    ell=material.space.ell_data(frame.r[rows])[0]
    safe=np.ones(len(rows),dtype=bool) if phase==0 else (ell<=material.moments.START)|(ell>=material.old.FLAT_START)
    ext=q[nold:].reshape(-1,3)
    if np.any(ext):
        for b in (frame.B,frame.Br,frame.Bs):
            safe&=~np.any((b[rows,nold//3:]@ext)!=0,axis=1)
    return dict(nold=nold,old_q=oldq,rows=rows,old_angular=ss,safe=safe,prior=prior)


def thin(frame,ix):
    return SimpleNamespace(base=frame.base[ix],br=frame.br[ix],bs=frame.bs[ix],
        B=frame.B[ix],Br=frame.Br[ix],Bs=frame.Bs[ix],j0=tuple(v[ix] for v in frame.j0),
        det=frame.det[ix],r=frame.r[ix])


def channels(frame,q,link,paid):
    prior=link['prior'];ids=link['rows'][link['safe']]
    if not len(ids) or not paid.parent.has('nine_angular_derivatives',prior):
        return material.space.channels(frame,q)
    original=paid.acquire('nine_angular_derivatives',prior)
    result=np.empty((3,3,len(frame.r),3))
    result[:,:,ids]=original[:,:,link['safe']]
    if len(ids)<len(frame.r):
        extra=np.setdiff1d(np.arange(len(frame.r)),ids,assume_unique=True)
        for lo in range(0,len(extra),256):
            select=extra[lo:lo+256]
            result[:,:,select]=material.space.channels(thin(frame,select),q)
    return result


def standard(frame,ch,ids,first,last):
    blocks=[]
    for lo in range(0,len(ids),96):
        ix=ids[lo:lo+96]
        shape=(len(ix),3,last-first,3)
        data=np.empty(shape)
        for axis in range(3):
            data[:,:,:,axis]=sum(ch[k,axis,ix,:,None]*a[ix,None,first:last]
                                 for k,a in enumerate((frame.B,frame.Br,frame.Bs)))
        blocks.append(csr_matrix(data.reshape(len(ix)*3,3*(last-first))))
    return vstack(blocks,format='csr') if blocks else csr_matrix((0,3*(last-first)))


def physical_csr(frame,q,ch,link,paid):
    prior=link['prior'];safe=link['safe'];oldcols=link['nold']//3
    if not np.any(safe) or not paid.parent.has('r750_complete_curl_csr',prior):
        return material.space.sparse_jac(frame,q,ch)
    prev=paid.acquire('r750_complete_curl_csr',prior)
    ids=link['rows'][safe];fresh=np.setdiff1d(np.arange(len(frame.r)),ids,assume_unique=True)
    left=vstack((csr(prev)[vector_rows(np.flatnonzero(safe))],standard(frame,ch,fresh,0,oldcols)),format='csr')
    left=left[vector_rows(np.argsort(np.r_[ids,fresh]))]
    active=np.zeros(len(frame.r),dtype=bool)
    for b in (frame.B,frame.Br,frame.Bs):active|=np.any(b[:,oldcols:]!=0,axis=1)
    active=np.flatnonzero(active)
    ext=standard(frame,ch,active,oldcols,frame.B.shape[1]).tocoo()
    rhs=coo_matrix((ext.data,(vector_rows(active)[ext.row],ext.col)),
                   shape=(3*len(frame.r),3*(frame.B.shape[1]-oldcols))).tocsr()
    full=hstack((left,rhs),format='csr')
    test=np.unique(np.r_[0,1,3*oldcols-1,3*oldcols,np.linspace(0,len(q)-1,15,dtype=int),len(q)-1])
    errors=[]
    for j in test:
        z=q.astype(complex);z[j]+=1.e-24j
        actual=frame.curl(z).imag.ravel()/1.e-24
        errors.append(float(np.max(abs(actual-full.getcol(j).toarray().ravel()))/max(1.,np.max(abs(actual)))))
    if not np.isfinite(errors).all() or max(errors)>2.e-10:
        raise ArithmeticError('new R760 complete native CSR check failed')
    return {**raw(full),'sampled_columns':test,'scaled_check_defects':np.asarray(errors),
            'adopted_R750_curl_rows':3*len(ids),'adopted_original_columns':3*oldcols,
            'new_curl_rows':3*len(fresh),'actual_w_shoulder_rows':len(active)}


def original_first(raw_j,residual,identity,stage,frame,link,paid):
    prior=link['prior']
    old_curl=[prior[0],prior[1],'train',prior[2],prior[3]]
    if not (paid.parent.has('full_sparse_jacobian',prior) and paid.parent.has('tsqr_scale',prior+['columns'])
            and paid.parent.has('r750_complete_curl_csr',prior) and paid.parent.has('curl',old_curl)):
        return tsqr_factor(raw_j,residual,identity,stage)
    n=len(frame.r);ns=frame.shape[-1];r=link['rows'];s=link['old_angular']
    old=np.r_[r,n+s]
    extra=np.setdiff1d(np.arange(n+ns),old,assume_unique=True)
    order=np.r_[old,extra]
    def reorder():
        return {**raw_j,**raw(csr(raw_j)[vector_rows(order)])}
    full=stage('r760_reordered_all_rows',['original_material_first'],reorder)
    support=~link['safe'].copy()
    first=link['nold']//3
    for a in (frame.B,frame.Br,frame.Bs):support|=np.any(a[r,first:]!=0,axis=1)
    # Old integrated rows use their own radial panels and original joint weight.
    # The genuinely refined relative integrated operator is new even at source.
    support=np.r_[support,np.ones(len(s),dtype=bool)]
    donor=dict(columns=link['nold'],support=support,
               has=lambda kind,sub:paid.parent.has(kind,prior+sub),
               load=lambda kind,sub:paid.acquire(kind,prior+sub))
    return tsqr_factor(full,np.asarray(residual).reshape(-1,3)[order],identity,stage,donor)
