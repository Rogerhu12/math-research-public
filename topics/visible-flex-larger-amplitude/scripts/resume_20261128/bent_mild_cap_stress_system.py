"""R786 full-time shape solve with a compressive second variation of the actual Gram rows."""
import numpy as np
from scipy.sparse.linalg import LinearOperator, cg
import bent_circular_free_ring_system as old
import bent_mild_cap_pullback_fields as field

fixed,transformed,clock,stats,dot=old.fixed,old.transformed,old.clock,old.stats,old.dot
far_constraints,objective=old.far_constraints,old.objective
ref=old.ref


def stress_at(tables,base,coeff,floor,par):
    # Half of the exact second derivative of ||g-I||_F^2 from the quadratic tensor diff.
    # The geometric displacement uses the current physical derivative of the axial floor map.
    # Its own second derivative and Hessians of the auxiliary nonsmooth penalties are omitted
    # from this trial model; every signed trial is evaluated in the original nonlinear objective.
    k=len(coeff)
    blocks=np.zeros((3,k,k));scores=[];saved=[]
    for (B,weight,_),f0 in zip(tables,base):
        F=field.apply(f0,B,coeff,floor,False)[0]
        va,vb=F[:,1],F[:,2]
        aa=dot(va,va)-1.;ab=dot(va,vb);bb=dot(vb,vb)-1.
        scores.append(aa*aa+2*ab*ab+bb*bb);saved.append((aa,ab,bb))
    losses=np.concatenate(scores);npeak=min(len(losses),par["gram_peak_count"])
    use=np.argpartition(losses,len(losses)-npeak)[-npeak:]
    extra=np.zeros(len(losses));extra[use]=par["gram_peak_weight"]**2/npeak
    start=0
    for ((B,w,pos),f0,(aa,ab,bb)) in zip(tables,base,saved):
        weights=2*(w*w+extra[start:start+len(B)]);start+=len(B)
        for j in range(0,len(B),par["jac_chunk"]):
            ix=slice(j,j+par["jac_chunk"])
            D=field.apply(f0[ix],B[ix],coeff,floor,True)[1]
            c11=weights[ix]*aa[ix];c12=weights[ix]*ab[ix];c22=weights[ix]*bb[ix]
            for a in range(3):
                P,Q=D[:,1,:,a],D[:,2,:,a]
                blocks[a]+=P.T@(c11[:,None]*P+c12[:,None]*Q)+Q.T@(c12[:,None]*P+c22[:,None]*Q)
    return .5*(blocks+blocks.transpose(0,2,1))


def ritz_model(total,stress,dimension,budget):
    # Deterministic bounded Krylov spaces for both the full Gram-curvature model and
    # the stress alone. All Rayleigh values are recomputed on the actual final vectors.
    x=np.arange(1,dimension+1,dtype=float);space=[]
    for j,mul in enumerate((stress,total)):
        q=np.sin((.119+.072*j)*x)+np.cos((.617-.21*j)*x)
        for _ in range(budget):
            for __ in range(2):
                for p in space:q-=np.dot(p,q)*p
            size=np.linalg.norm(q)
            if not np.isfinite(size) or size<1.e-12:break
            q=q/size;space.append(q.copy());q=mul(q)
    if not space:return []
    Q=np.column_stack(space);out=[]
    for name,mul in (("total",total),("compressive",stress)):
        M=np.column_stack([mul(q) for q in space]);A=Q.T@M
        vals,vec=np.linalg.eigh(.5*(A+A.T));direction=Q@vec[:,0]
        out.append((name,direction,float(np.dot(direction,total(direction))),
                    float(np.dot(direction,stress(direction))),len(space)))
    return out


def shape_step(tables,values,W,Z,par):
    nt,k,_=Z.shape;K=3*k;H=[];g=[];C=[];loss=peak=0.;nnormal=nfar=0
    chord=maxfar=0.
    for i,(t,rows,floor) in enumerate(values):
        x=np.tensordot(W[i],Z,axes=1)
        score,pk,HH,gg,nn,rd,nf,rf=old.system_at(tables,rows,x,floor,par,True)
        H.append(HH);g.append(gg);C.append(stress_at(tables,rows,x,floor,par))
        loss+=score;peak=max(peak,pk);nnormal+=nn;nfar+=nf;chord=max(chord,rd);maxfar=max(maxfar,rf)
    H=np.asarray(H);C=np.asarray(C);G=W.T@np.asarray(g)
    diag=np.einsum("tp,ti->pi",W*W,np.diagonal(H,axis1=1,axis2=2))
    penalty=par["damping"]*max(np.mean(diag),1.e-7)
    denom=diag.ravel()+penalty;scale=1/np.sqrt(denom)
    def gn_model(x):
        b=W@x.reshape(nt,K)
        return (W.T@np.einsum("tij,tj->ti",H,b)).ravel()
    def stress_model(x):
        b=(W@x.reshape(nt,K)).reshape(-1,k,3)
        c=np.einsum("taij,tja->tia",C,b)
        return (W.T@c.reshape(-1,K)).ravel()
    A=LinearOperator((nt*K,nt*K),matvec=lambda x:gn_model(x)+penalty*x)
    M=LinearOperator(A.shape,matvec=lambda x:x/denom)
    count=[0]
    def hit(_):count[0]+=1
    step,st=cg(A,-G.ravel(),M=M,rtol=par["cg_tol"],atol=0.,maxiter=par["cg_max"],callback=hit)
    eig=ritz_model(lambda x:scale*(gn_model(scale*x)+stress_model(scale*x)),
                   lambda x:scale*stress_model(scale*x),len(step),par["stress_krylov_per_operator"])
    names=["gauss-newton"];directions=[step.reshape(Z.shape)]
    eiglog=[]
    for tag,vec,full,compression,nsub in eig:
        eiglog.append(dict(label=tag,total_rayleigh=full,stress_rayleigh=compression,subspace=nsub))
        if (full if tag=="total" else compression)<0.:
            names.append(tag);directions.append((scale*vec).reshape(Z.shape))
    motions=np.zeros(len(directions));slopes=np.zeros(len(directions))
    for i,(t,rows,floor) in enumerate(values):
        x=np.tensordot(W[i],Z,axes=1);dsteps=[np.tensordot(W[i],v,axes=1) for v in directions]
        for (B,_,_),f0 in zip(tables,rows):
            for j in range(0,len(B),par["jac_chunk"]):
                ix=slice(j,j+par["jac_chunk"])
                D=field.apply(f0[ix],B[ix],x,floor,True)[1]
                for ii,d in enumerate(dsteps):
                    qr=np.einsum("nrkd,kd->nrd",D,d)
                    motions[ii]=max(motions[ii],np.linalg.norm(qr[:,0],axis=-1).max())
                    slopes[ii]=max(slopes[ii],np.linalg.norm(qr[:,1:3],axis=-1).max())
    output=[];sizing=[]
    for j,(tag,v) in enumerate(zip(names,directions)):
        f=min(par["step_displacement"]/max(motions[j],1.e-15),par["step_tangent"]/max(slopes[j],1.e-15))
        if not j:f=min(1.,f)
        output.append((tag,f*v))
        sizing.append(dict(label=tag,unscaled_position=float(motions[j]),unscaled_tangent=float(slopes[j]),
                           scale=float(f),raw_coordinate_norm=float(np.linalg.norm(v))))
    return output,dict(current_objective=loss,raw_max_gram=peak,cg_status=int(st),cg_iterations=count[0],
       stress_ritz=eiglog,physical_step_scales=sizing,active_global_ordered_pairs=nnormal,worst_pair_residual=chord,
       active_metric_reach_pairs=nfar,worst_metric_reach_pair=maxfar)
