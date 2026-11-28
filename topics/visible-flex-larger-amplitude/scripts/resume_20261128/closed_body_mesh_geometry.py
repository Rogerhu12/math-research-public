"""Complete finite triangle and ordered normal-chord comparisons on a closed material mesh."""
import numpy as np
from scipy.spatial import cKDTree


def rowdot(a,b):
    return np.einsum("...i,...i->...",a,b)


def box_tree(lo,hi,leaf=24):
    nodes=[]
    def build(ids):
        lower=lo[ids].min(axis=0);upper=hi[ids].max(axis=0)
        index=len(nodes);nodes.append(None)
        if len(ids)<=leaf:
            nodes[index]=(lower,upper,ids,-1,-1,len(ids))
        else:
            centers=(lo[ids]+hi[ids])*.5
            axis=int(np.argmax(np.ptp(centers,axis=0)))
            cut=len(ids)//2;order=np.argpartition(centers[:,axis],cut)
            left=build(ids[order[:cut]]);right=build(ids[order[cut:]])
            nodes[index]=(lower,upper,None,left,right,len(ids))
        return index
    build(np.arange(len(lo),dtype=np.int32))
    return nodes


def split_pair(nodes,i,j):
    x,y=nodes[i],nodes[j]
    if i==j:return [(x[3],x[3]),(x[3],x[4]),(x[4],x[4])]
    if y[2] is not None or (x[2] is None and x[5]>=y[5]):
        return [(x[3],j),(x[4],j)]
    return [(i,y[3]),(i,y[4])]


def diameter(points):
    ids=np.unique(np.r_[points.argmin(axis=0),points.argmax(axis=0)])
    delta=points[ids,None]-points[None,ids]
    w=rowdot(delta,delta);i,j=np.unravel_index(w.argmax(),w.shape)
    best=float(w[i,j]);witness=[int(ids[i]),int(ids[j])]
    nodes=box_tree(points,points,40);pending=[(0,0)]
    pad=256*np.finfo(float).eps*max(1.,float(np.ptp(points,axis=0).max())**2)
    leaves=0
    while pending:
        i,j=pending.pop();x,y=nodes[i],nodes[j]
        extent=np.maximum(x[1]-y[0],y[1]-x[0])
        if extent@extent+pad<best:continue
        if x[2] is None or y[2] is None:
            pending.extend(split_pair(nodes,i,j));continue
        leaves+=1;dd=points[x[2],None]-points[None,y[2]]
        d2=rowdot(dd,dd);p,q=np.unravel_index(d2.argmax(),d2.shape)
        if d2[p,q]>best:
            best=float(d2[p,q]);witness=[int(x[2][p]),int(y[2][q])]
    return {"value":float(np.sqrt(best)),"vertices":witness,"examined_leaf_pairs":leaves}


def ordered_chords(p,n,edges):
    best=0.;arg=None;zero_count=0;first_zero=None
    def compare(i,j,count_zero=False):
        nonlocal best,arg,zero_count,first_zero
        if not len(i):return
        v=p[j]-p[i];d2=rowdot(v,v);valid=d2>0.
        if count_zero and not np.all(valid):
            zero_count+=int((~valid).sum())
            if first_zero is None:
                k=int(np.argmax(~valid));first_zero=[int(i[k]),int(j[k])]
        ii,jj=i[valid],j[valid];v=v[valid];d2=d2[valid]
        if not len(ii):return
        for left,right,normals in ((ii,jj,n[ii]),(jj,ii,n[jj])):
            ratio=2*np.abs(rowdot(v,normals))/d2;k=int(np.argmax(ratio))
            if ratio[k]>best:best=float(ratio[k]);arg=[int(left[k]),int(right[k])]
    compare(edges[:,0],edges[:,1])
    # A witnessed lower bound L means all pairs farther than 2/L have
    # inverse chord <=L. The inflated radius is fixed before traversal.
    sigma=max(1.,float(np.linalg.norm(n,axis=1).max()))
    radius=(2*sigma/best) if best>0 else np.inf
    pad=256*np.finfo(float).eps*max(1.,float(np.max(np.abs(p))))
    if np.isfinite(radius):radius=np.nextafter(radius+pad,np.inf)
    tree=cKDTree(p)
    evaluated=0
    for first in range(0,len(p),20):
        stop=min(first+20,len(p));groups=tree.query_ball_point(p[first:stop],radius)
        js=[];is_=[]
        for i,other in enumerate(groups,first):
            others=np.asarray(other,dtype=int);others=others[others>i]
            if len(others):js.append(others);is_.append(np.full(len(others),i,dtype=int))
        if js:
            more=np.concatenate(js);evaluated+=len(more);compare(np.concatenate(is_),more,True)
    return {"maximum":best,"ordered_vertices":arg,"nonzero_witness_proxy":(1/best if best>0 else None),
            "finite_witness_search_radius":float(radius) if np.isfinite(radius) else None,
            "evaluated_unordered_pairs_after_radius_bound":evaluated,"all_unordered_pairs":len(p)*(len(p)-1)//2,
            "distinct_material_coincident_pairs":zero_count,"first_coincident_vertices":first_zero}


def unit(v):
    lengths=np.linalg.norm(v,axis=-1)
    return v/np.where(lengths>0,lengths,1.)[...,None]


def disjoint_faces(a,b,tol):
    # Each supplied axis is a separating-axis opportunity. Edge-plane
    # axes cover flat coplanar triangles as well as the nonparallel case.
    ea=np.roll(a,-1,axis=1)-a;eb=np.roll(b,-1,axis=1)-b
    na=np.cross(ea[:,0],ea[:,1]);nb=np.cross(eb[:,0],eb[:,1])
    axes=[na,nb]
    for i in range(3):
        axes.extend([np.cross(na,ea[:,i]),np.cross(nb,eb[:,i])])
        for j in range(3):axes.append(np.cross(ea[:,i],eb[:,j]))
    # Center both triangles at one physical vertex before projection.
    a,b=a-a[:,:1],b-a[:,:1]
    keep=np.ones(len(a),dtype=bool)
    for ax in axes:
        d=unit(ax)
        x=np.einsum("nki,ni->nk",a,d);y=np.einsum("nki,ni->nk",b,d)
        keep&=np.maximum(x.min(axis=1)-y.max(axis=1),y.min(axis=1)-x.max(axis=1))<=tol
    return keep


def triangle_contacts(p,faces):
    tri=p[faces];lo=tri.min(axis=1);hi=tri.max(axis=1)
    tol=512*np.finfo(float).eps*max(1.,float(np.abs(p).max()))
    nodes=box_tree(lo,hi);pending=[(0,0)]
    buckets={0:[],1:[],2:[]};counts=[0,0,0];tested=[0,0,0];witness=[None,None,None]
    # Batch the exact candidate tests to avoid invoking vector geometry
    # separately for every leaf or edge of a regular measured mesh.
    def flush(shared):
        if not buckets[shared]:return
        ij=np.concatenate(buckets[shared]);buckets[shared].clear()
        ii,jj=ij.T;tested[shared]+=len(ij)
        if shared==0:
            hit=disjoint_faces(tri[ii],tri[jj],tol)
        elif shared==2:
            A,B=faces[ii],faces[jj];same=(A[:,:,None]==B[:,None,:])
            ca=np.argmax(~same.any(axis=2),axis=1);cb=np.argmax(~same.any(axis=1),axis=1)
            t=np.arange(len(ii));u=p[A[t,(ca+1)%3]];v=p[A[t,(ca+2)%3]];d=unit(v-u)
            x=p[A[t,ca]]-u;y=p[B[t,cb]]-u
            x=unit(x-d*rowdot(x,d)[:,None]);y=unit(y-d*rowdot(y,d)[:,None])
            hit=(np.linalg.norm(np.cross(x,y),axis=1)<=2e-10)&(rowdot(x,y)>0)
        else:
            A,B=faces[ii],faces[jj];same=A[:,:,None]==B[:,None,:]
            ia=np.argmax(same.any(axis=2),axis=1);ib=np.argmax(same.any(axis=1),axis=1)
            t=np.arange(len(ii));u=p[A[t,ia]]
            a,b=unit(p[A[t,(ia+1)%3]]-u),unit(p[A[t,(ia+2)%3]]-u)
            c,d=unit(p[B[t,(ib+1)%3]]-u),unit(p[B[t,(ib+2)%3]]-u)
            h,k=unit(np.cross(a,b)),unit(np.cross(c,d));cross=np.cross(h,k);dr=unit(cross)
            def member(x,y,n,v):
                return ((np.abs(rowdot(v,n))<=2e-10)&(rowdot(np.cross(x,v),n)>=-2e-10)&
                        (rowdot(np.cross(v,y),n)>=-2e-10))
            hit=np.where(np.linalg.norm(cross,axis=1)>2e-10,
                (member(a,b,h,dr)&member(c,d,k,dr))|(member(a,b,h,-dr)&member(c,d,k,-dr)),
                member(a,b,h,c)|member(a,b,h,d)|member(c,d,k,a)|member(c,d,k,b))
        counts[shared]+=int(np.count_nonzero(hit))
        if np.any(hit) and witness[shared] is None:
            w=int(np.argmax(hit));witness[shared]=[int(ii[w]),int(jj[w])]
    while pending:
        i,j=pending.pop();x,y=nodes[i],nodes[j]
        if np.any(x[0]>y[1]+tol) or np.any(y[0]>x[1]+tol):continue
        if x[2] is None or y[2] is None:
            pending.extend(split_pair(nodes,i,j));continue
        ix,jx=x[2],y[2]
        use=np.all((lo[ix,None]<=hi[None,jx]+tol)&(lo[None,jx]<=hi[ix,None]+tol),axis=2)
        if i==j:use&=ix[:,None]<jx[None,:]
        a,b=np.nonzero(use)
        if not len(a):continue
        aa,bb=ix[a],jx[b];shared=(faces[aa,:,None]==faces[bb,None,:]).sum(axis=(1,2))
        for common in (0,1,2):
            sel=shared==common
            if np.any(sel):buckets[common].append(np.column_stack((aa[sel],bb[sel])))
            if len(buckets[common])>=40:flush(common)
    for common in (0,1,2):flush(common)
    return {"scope":"floating-point triangle contact incl. extra overlap beyond a shared edge or vertex",
            "candidate_pairs_by_shared_vertex_count":tested,"possible_contacts_by_shared_vertex_count":counts,
            "first_triangle_pair_by_shared_vertex_count":witness,"spatial_tolerance":tol,"angular_tolerance":2e-10}
