"""Full physical Gauss-Newton for a shared spatial section field and finite ordered normal-ball constraints."""
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse.linalg import LinearOperator,cg
import bent_preloaded_bridge_system as ref
import bent_spatial_ring_fields as field
fixed,transformed,clock,stats,dot=ref.fixed,ref.transformed,ref.clock,ref.stats,ref.dot

def residual(F,B,w,par,linear=True):
    npts=len(F);k=B.shape[2] if linear else 0;a,b=F[:,1],F[:,2];P,Q=B[:,1:3].transpose(1,0,2,3) if linear else (None,None)
    ncr=np.cross(a,b);area=np.linalg.norm(ncr,axis=1)
    nn=ncr/np.maximum(area,1.e-14)[:,None];ab=dot(a,b)
    aa=dot(a,a);bb=dot(b,b);r=[];jac=[]
    def add(value,j,wgt):
        weight=w*wgt;r.append(value*weight)
        if linear:jac.append(j*weight[:,None,None])
    if linear:
        ja=2*P*a[:,None,:];jb=2*Q*b[:,None,:]
        jab=P*b[:,None,:]+Q*a[:,None,:]
    else:ja=jb=jab=None
    add(aa-1,ja,1.);add(ab,jab,2**.5);add(bb-1,jb,1.)
    # Relative area barrier. delta |a cross b|=delta a.(b cross n)+delta b.(n cross a).
    dm=np.maximum(np.log(par["area_floor"]/np.maximum(area,1.e-12)),0)
    jj=None
    if linear:
        jj=-(P*np.cross(b,nn)[:,None,:]+Q*np.cross(nn,a)[:,None,:])*((dm>0)/np.maximum(area,1.e-12))[:,None,None]
    add(dm,jj,par["area_weight"])
    worst=np.zeros(npts)
    for co,si in ((1.,0.),(0.,1.),(2**-.5,2**-.5),(2**-.5,-2**-.5)):
        v=co*a+si*b;vv=dot(v,v)
        H=co*co*F[:,3]+2*co*si*F[:,4]+si*si*F[:,5]
        h=dot(nn,H);active=np.maximum(abs(h)-par["curvature_bound"]*vv,0.)
        worst=np.maximum(worst,abs(h)/np.maximum(vv,1.e-15))
        j=None
        if linear:
            hp=(H-h[:,None]*nn)/np.maximum(area[:,None],1.e-14)
            # delta n.H = delta a.(b cross Hperp)/area + delta b.(Hperp cross a)/area.
            ah=np.cross(b,hp);bh=np.cross(hp,a)
            BH=co*co*B[:,3]+2*co*si*B[:,4]+si*si*B[:,5]
            hj=P*ah[:,None,:]+Q*bh[:,None,:]+BH*nn[:,None,:]
            j=np.sign(h)[:,None,None]*hj-2*par["curvature_bound"]*(co*P+si*Q)*v[:,None,:]
            j*=(active>0)[:,None,None]
        add(active,j,par["curvature_weight"])
    e=.5*(aa+bb)-1;d=np.hypot(.5*(aa-bb),ab);op=np.maximum(abs(e+d),abs(e-d))
    return np.concatenate(r),(np.concatenate(jac,axis=0).reshape(-1,3*k) if linear else None),op,area,worst


def pairs(F,material,par):
    a,b=F[:,1],F[:,2];cr=np.cross(a,b);ar=np.linalg.norm(cr,axis=1);n=cr/np.maximum(ar[:,None],1.e-14)
    pts=F[:,0];ids=cKDTree(pts).query(pts,k=par["neighbor_ranks"])[1]
    ii=np.broadcast_to(np.arange(len(pts))[:,None],ids.shape).ravel();jj=ids.ravel()
    use=(ii!=jj)&(np.linalg.norm(material[jj]-material[ii],axis=1)>par["distinct_material_distance"])
    ii,jj=ii[use],jj[use];ch=pts[jj]-pts[ii]
    length=np.sqrt(dot(ch,ch)+par["chord_smoothing"]**2);sc=dot(n[ii],ch)
    r=np.maximum(2*abs(sc)/length-length/par["radius"],0.)
    idx=np.flatnonzero(r>0.)
    if len(idx)>par["worst_pairs"]:
        idx=idx[np.argpartition(r[idx],-par["worst_pairs"])[-par["worst_pairs"]:]]
    return ii[idx],jj[idx],r[idx],n,ar

def system_at(tables,rows,coef,level_floor,par,linear):
    K=coef.size;H=np.zeros((K,K)) if linear else None;G=np.zeros(K) if linear else None
    obj=0.;peak=0.;fs=[];mat=[];chunk=par["jac_chunk"];move_basis=0.
    for (B,w,pos0),f0 in zip(tables,rows):
        arr=[]
        for i in range(0,len(f0),chunk):
            ix=slice(i,i+chunk);F,D=field.apply(f0[ix],B[ix],coef,level_floor,linear)
            r,J,op,ar,pk=residual(F,D,w[ix],par,linear);arr.append(F)
            obj+=float(r@r);peak=max(peak,float(op.max()))
            if linear:H+=J.T@J;G+=J.T@r
        fs.append(np.concatenate(arr));mat.append(pos0)
    F=np.concatenate(fs);coords=np.concatenate(mat)
    ii,jj,r,n,ar=pairs(F,coords,par);w=par["pair_weight"]/np.sqrt(par["worst_pairs"])
    obj+=float(w*w*(r@r))
    if len(ii) and linear:
        chosen,inv=np.unique(np.r_[ii,jj],return_inverse=True);i0,j0=np.split(inv,2)
        D=np.empty((len(chosen),6,K//3,3));start=0
        for (B,ww,pos),f0 in zip(tables,rows):
            loc=np.flatnonzero((chosen>=start)&(chosen<start+len(B)))
            if len(loc):
                idx=chosen[loc]-start
                D[loc]=field.apply(f0[idx],B[idx],coef,level_floor,True)[1]
            start+=len(B)
        delta=F[jj,0]-F[ii,0];length=np.sqrt(dot(delta,delta)+par["chord_smoothing"]**2)
        sc=dot(n[ii],delta);sg=np.sign(sc)
        v=2*sg[:,None]*n[ii]/length[:,None]-(2*abs(sc)/length**3+1/(par["radius"]*length))[:,None]*delta
        hp=(delta-sc[:,None]*n[ii])*(2*sg/(length*np.maximum(ar[ii],1.e-14)))[:,None]
        j=(D[j0,0]-D[i0,0])*v[:,None,:]+D[i0,1]*np.cross(F[ii,2],hp)[:,None,:]+D[i0,2]*np.cross(hp,F[ii,1])[:,None,:]
        j=j.reshape(len(r),K)*w;H+=j.T@j;G+=j.T@(r*w)
    return obj,peak,H,G,len(r),float(r.max(initial=0.))

def shape_step(tables,base,W,Z,par):
    K=Z[0].size;nt=len(Z);H=[];g=[];value=0.;peak=0.;npair=0;pairpeak=0.
    for i,(t,rows,floor) in enumerate(base):
        c=np.tensordot(W[i],Z,axes=1);v,k,HH,gg,n,r=system_at(tables,rows,c,floor,par,True)
        H.append(HH);g.append(gg);value+=v;peak=max(peak,k);npair+=n;pairpeak=max(pairpeak,r)
    H=np.array(H);g=np.array(g);G=W.T@g
    diag=np.einsum("tp,ti->pi",W*W,np.diagonal(H,axis1=1,axis2=2))
    reg=par["damping"]*max(np.mean(diag),1.e-7)
    def mul(x):
        b=W@x.reshape(nt,K)
        return (W.T@np.einsum("tij,tj->ti",H,b)+reg*x.reshape(nt,K)).ravel()
    A=LinearOperator((nt*K,nt*K),matvec=mul);M=LinearOperator(A.shape,matvec=lambda x:x/(diag.ravel()+reg))
    its=[0]
    def count(_):its[0]+=1
    update,info=cg(A,-G.ravel(),M=M,rtol=par["cg_tol"],atol=0.,maxiter=par["cg_max"],callback=count)
    out=update.reshape(Z.shape);move=0.;slope=0.
    for i,(t,rows,floor) in enumerate(base):
        c=np.tensordot(W[i],Z,axes=1);dx=np.tensordot(W[i],out,axes=1)
        for (B,w,pos),f0 in zip(tables,rows):
            for j in range(0,len(B),par["jac_chunk"]):
                ix=slice(j,j+par["jac_chunk"]);_,D=field.apply(f0[ix],B[ix],c,floor,True)
                d=np.einsum("nrkd,kd->nrd",D,dx)
                move=max(move,float(np.linalg.norm(d[:,0],axis=-1).max()))
                slope=max(slope,float(np.linalg.norm(d[:,1:3],axis=-1).max()))
    fac=min(1.,par["step_displacement"]/max(move,1.e-15),par["step_tangent"]/max(slope,1.e-15))
    return fac*out,dict(current_objective=value,raw_max_gram=peak,cg_status=int(info),cg_iterations=its[0],
           raw_update_norm=float(np.linalg.norm(out)),raw_physical_move=move,
           raw_orthonormal_tangent_move=slope,trust_factor=fac,active_global_ordered_pairs=npair,worst_pair_residual=pairpeak)

def objective(tables,base,W,Z,par):
    value=0.;peak=0.
    for i,(t,rows,floor) in enumerate(base):
        c=np.tensordot(W[i],Z,axes=1);v,k,_,_,_,_=system_at(tables,rows,c,floor,par,False)
        value+=v;peak=max(peak,k)
    return value,peak
