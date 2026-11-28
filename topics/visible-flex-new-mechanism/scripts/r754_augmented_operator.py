"""All native R754 columns; import the unchanged R746 operator rows exactly."""
from types import SimpleNamespace
import numpy as np
from scipy.sparse import coo_matrix,csr_matrix,hstack,vstack
import r754_nested_rotation as model


def raw(c):
    c=c.tocsr();return dict(data=c.data,indices=c.indices,indptr=c.indptr,shape=c.shape)


def matrix(r):
    return csr_matrix((r['data'],r['indices'],r['indptr']),shape=r['shape'])


def rowids(nodes):
    return (3*np.asarray(nodes,dtype=int)[:,None]+np.arange(3)).ravel()


def expand_rows(part,nodes,nrow):
    co=part.tocoo();ids=rowids(nodes)
    return coo_matrix((co.data,(ids[co.row],co.col)),shape=(3*nrow,part.shape[1])).tocsr()


def overwrite_rows(original,part,nodes):
    # An actual partition of the row set. Avoid subtract/add cancellation or
    # rounding old values, including when an imported singular direction is small.
    support=np.zeros(original.shape[0]//3,dtype=bool);support[nodes]=True
    complement=np.flatnonzero(~support)
    stack=vstack((original[rowids(complement)],part),format='csr')
    ordering=np.concatenate((complement,nodes));inverse=np.argsort(ordering)
    return stack[rowids(inverse)]


def angular_channels(frame,q):
    args,base=frame.arguments(q)
    proxy=SimpleNamespace(base=base[0],br=base[1],bs=base[2],det=frame.det,j0=frame.j0)
    ans=np.empty((3,3,len(frame.r),3))
    for slot in range(3):
        for axis in range(3):
            z=[a.astype(complex) if j==slot else a for j,a in enumerate(args)]
            z[slot][:,axis]+=1.e-24j
            ans[slot,axis]=model.space.angular_curl(proxy,*z).imag/1.e-24
    if not np.isfinite(ans).all():
        raise ArithmeticError('nonfinite R754 independent angular/radial/angular-derivative channels')
    return ans


def standard_columns(b,br,bs,ch):
    cols=b.shape[1];blocks=[]
    for lo in range(0,len(b),96):
        s=slice(lo,lo+96);n=len(b[s]);values=np.empty((n,3,cols,3))
        for j in range(3):
            values[:,:,:,j]=sum(ch[k,j,s,:,None]*a[s,None,:] for k,a in enumerate((b,br,bs)))
        blocks.append(csr_matrix(values.reshape(3*n,3*cols)))
    return vstack(blocks,format='csr') if blocks else csr_matrix((0,3*cols))


def restrict_field(frame,q,parent_values):
    _,p,c=model.split(q,frame.degree)
    original=np.asarray(parent_values)
    if original.shape!=frame.shape+(3,) or not np.isfinite(original).all():
        raise ValueError('old paid field has a different native mesh or nonfinite data')
    if not np.any(p) and not np.any(c):
        return original
    ids=np.flatnonzero(frame.changed_mask(p,c))
    ans=original.reshape(-1,3).copy()
    if len(ids):ans[ids]=frame.subset(ids).curl(q)
    return ans.reshape(original.shape)


def add_operator(frame,q,previous_raw,previous_ch,previous_ch_on_region,stage):
    """stage(kind,compute) runs outside any other paid operation."""
    _,p,c=model.split(q,frame.degree)
    n=len(frame.r);ix=np.flatnonzero(frame.support(c))
    ic=np.flatnonzero(frame.changed_mask(p,c));changed=bool(len(ic))
    at=np.searchsorted(ix,ic)
    previous=matrix(previous_raw) if previous_raw is not None else None
    if previous is not None and previous.shape!=(3*n,3*frame.B.shape[1]):
        raise ValueError('original CSR shape differs from the R746 mesh/control prefix')
    if previous is None:
        if previous_ch is None:
            ch=stage('angular_all',lambda:angular_channels(frame,q))
        elif not changed:
            ch=previous_ch
        else:
            ch=previous_ch.copy()
            ch[:,:,ic]=stage('angular_changed',lambda:angular_channels(frame.subset(ic),q))
        oldmat=matrix(stage('old_columns_unpaid',lambda:raw(standard_columns(frame.B,frame.Br,frame.Bs,ch))))
        chpart=ch[:,:,ix]
    else:
        if len(ix):
            if previous_ch_on_region is not None or previous_ch is not None:
                chpart=(previous_ch_on_region if previous_ch_on_region is not None else previous_ch[:,:,ix])
                if changed:
                    chpart=chpart.copy()
                    chpart[:,:,at]=stage('angular_changed',lambda:angular_channels(frame.subset(ic),q))
            else:
                chpart=stage('angular_released',lambda:angular_channels(frame.subset(ix),q))
        else:
            chpart=np.empty((3,3,0,3))
        if changed:
            revised=matrix(stage('old_columns_changed_rows',lambda:raw(
                standard_columns(frame.B[ic],frame.Br[ic],frame.Bs[ic],chpart[:,:,at]))))
            oldmat=overwrite_rows(previous,revised,ic)
        else:
            oldmat=previous
    pi=frame.plus_nodes;p_at=np.searchsorted(ix,pi)
    plus=matrix(stage('appended_euler_columns',lambda:raw(expand_rows(standard_columns(
        frame.plus,frame.plus_r,frame.plus_s,chpart[:,:,p_at]),pi,n))))
    def carrier():
        take=frame.carrier_rows(c)
        if not len(take):return raw(csr_matrix((3*n,3)))
        block=frame.subset(take);col=[]
        for j in range(3):
            z=np.array(q,dtype=complex);z[-3+j]+=1.e-24j
            col.append(block.curl(z).imag.ravel()/1.e-24)
        return raw(expand_rows(csr_matrix(np.column_stack(col)),take,n))
    tri=matrix(stage('left_meridian_columns',carrier))
    result=hstack((oldmat,plus,tri),format='csr')
    # Independently re-differentiate only genuinely changed/new rows when the
    # old CSR was already checked. Preserve the parent's original check data.
    sample=ix if previous is not None else np.arange(n)
    if len(sample)>96:sample=sample[np.linspace(0,len(sample)-1,96,dtype=int)]
    test=frame.subset(sample)
    oldn=3*frame.B.shape[1];m=result.shape[1]
    ids=np.unique(np.r_[0,1,2,oldn-1,oldn,oldn+1,np.linspace(0,m-1,12,dtype=int),m-3,m-2,m-1])
    def checks():
        if not len(sample):return np.zeros(len(ids))
        vals=[];reference=result[rowids(sample)]
        for j in ids:
            z=np.array(q,dtype=complex);z[j]+=1.e-24j
            exact=test.curl(z).imag.ravel()/1.e-24
            vals.append(np.max(abs(exact-reference.getcol(j).toarray().ravel()))/max(1.,np.max(abs(exact))))
        if not np.isfinite(vals).all() or max(vals)>2.e-10:
            raise ArithmeticError('actual augmented columns disagree with the new complex-step checks')
        return np.asarray(vals)
    defects=stage('augmented_checks',checks)
    return {**raw(result),'sampled_columns':ids,'scaled_check_defects':defects,
        'old_prefix_columns':oldn,'new_columns':m-oldn,'unchanged_parent_rows':
        (3*(n-len(ic)) if changed else 3*n) if previous is not None else 0,
        'old_coefficient_rows_newly_differentiated':3*(n if previous is None else len(ic)),
        'new_complex_checked_nodes':sample,
        'parent_independent_columns':None if previous_raw is None else previous_raw['sampled_columns'],
        'parent_independent_defects':None if previous_raw is None else previous_raw['scaled_check_defects']}
