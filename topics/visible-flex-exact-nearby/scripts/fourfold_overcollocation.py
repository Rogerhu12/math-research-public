#!/usr/bin/env python3
"""Overcollocated actual-spline least squares; floating exploration only.

Uses Gauss points inside every radial spline interval. The requested waist
fourth-mode coefficient is an exact linear constraint, eliminated before the
optimizer. All output angular modes through 2M enter the objective by default.
No finite collocation minimum implies an exact, closed, fixed-cap surface.
"""
from __future__ import annotations
import argparse
import gc
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse import coo_matrix,csc_matrix,hstack,vstack,diags,eye
from scipy.sparse.linalg import splu
from types import SimpleNamespace
from scipy.optimize import least_squares
from fourfold_newton_refined import SplineNewton,parity_matrix
import poschl_teller_fourfold_series as ps


class Overcollocation(SplineNewton):
    def prepare(self,waist,gauss=2,all_modes=True,action=False,height_reference=None):
        self.objective_modes=2*self.modes if all_modes else self.modes
        self.action_constraint=action
        self.waist=waist
        self.greville=self.x.copy()
        self.collocation_rule=gauss
        breaks=np.unique(np.r_[0.,self.knots[self.knots>0]])
        q,w=leggauss(gauss)
        lo,hi=breaks[:-1,None],breaks[1:,None]
        self.x=((lo+hi)/2+(hi-lo)/2*q).ravel()
        self.quadrature_weights=((hi-lo)/2*w).ravel()
        self.even=[parity_matrix(self.knots,5,self.x,j,False) for j in range(3)]
        self.odd=[parity_matrix(self.knots,5,self.x,j,True) for j in range(3)]
        self.a=self.base_spline(self.x)[:,0]
        self.ap=self.base_spline(self.x,nu=1)[:,0]
        self.gamma=self.a**3
        self.base_x=np.broadcast_to(self.base_spline(self.x,nu=1)[:,None,:],
                                    (len(self.x),self.angles,3)).copy()
        self.base_t=np.zeros_like(self.base_x)
        self.base_t[:,:,1]=self.a[:,None]
        self.means_c=np.stack([s(self.x).T for s in self.mean_splines])
        self.means_d=np.stack([s(self.x,nu=1).T for s in self.mean_splines])
        sx=np.linalg.norm(self.base_x[:,0],axis=1)
        self.scale=np.stack([self.a**2,sx*self.a,sx**2],axis=1)*self.gamma[:,None]
        self.row_scale=np.tile(self.scale,(1,self.objective_modes))
        self.row_weight=np.repeat(np.sqrt(self.quadrature_weights),3*self.objective_modes)
        self.at_end=[parity_matrix(self.knots,5,np.array([self.length]),j,False) for j in range(2)]
        al=self.base_spline(np.array([self.length]))[0,0]
        apl=self.base_spline(np.array([self.length]),nu=1)[0,0]
        self.end_rate=self.mode*self.mu+3*apl/al
        self.waist_row=parity_matrix(self.knots,5,np.array([0.]),0,False).toarray().ravel()
        self.pivot=int(np.argmax(abs(self.waist_row)))
        size=3*self.modes*self.points+self.mean_count
        constraints=[]
        waistrow=np.zeros(size);waistrow[:self.points]=self.waist_row
        constraints.append((self.pivot,waistrow,waist))
        self.fixed_mean_height=height_reference
        if height_reference is not None:
            hrow=np.zeros(size)
            hrow[-self.mean_count:]=[sp(np.array([self.length]))[0,2] for sp in self.mean_splines]
            pivot=int(np.argmax(abs(hrow)))
            target=height_reference-self.base_spline(np.array([self.length]))[0,2]
            constraints.append((pivot,hrow,target))
        self.keep=np.delete(np.arange(size),[p for p,_,_ in constraints])
        freecol=np.full(size,-1,dtype=int);freecol[self.keep]=np.arange(len(self.keep))
        rows=self.keep.tolist();cols=list(range(len(self.keep)));vals=[1.]*(len(self.keep))
        self.offset=np.zeros(size)
        for pivot,row,target in constraints:
            self.offset[pivot]=target/row[pivot]
            for j in np.flatnonzero(row):
                if j==pivot:continue
                if freecol[j]<0:raise ValueError('constraint elimination requires disjoint pivots')
                rows.append(pivot);cols.append(int(freecol[j]));vals.append(float(-row[j]/row[pivot]))
        self.projector=coo_matrix((vals,(rows,cols)),shape=(size,len(self.keep))).tocsc()
        self.last_free=None;self.last_values=None;self.ncall=0

    def save(self,vector,path,epsilon):
        metadata=dict(kind='floating_actual_spline_finite_body_candidate_not_proof',
                      parameters=dict(modes=self.modes,points=self.points,length=self.length,
                                      mu_scale=self.mu/2**.5,means=self.mean_count,gauge=self.mean_gauge,
                                      profile_points=self.profile_points,mesh=self.mesh),epsilon=epsilon,
                      amplitude_gauge='exact fourth radial coefficient U4(0), not kernel projection',
                      radial_gauss_points_per_spline_interval=self.collocation_rule,
                      objective_positive_modes=self.objective_modes,
                      limitations=['Finite angular approximation','Finite Robin endpoint','No actual caps',
                                   'Floating arithmetic and sampled diagnostics only'])
        metadata['fixed_mean_height']=getattr(self,'fixed_mean_height',None)
        temporary=Path(str(path)+'.tmp.npz')
        np.savez_compressed(temporary,vector=vector,metadata=np.array(json.dumps(metadata)))
        temporary.replace(path)

    def expand(self,free):
        return self.offset+self.projector@free

    def extract(self,xx,xt,tt):
        fft=[np.fft.rfft(v,axis=1)/self.angles for v in [tt,xt,xx]]
        return np.stack([np.stack([2*fft[0][:,k].real,-2*fft[1][:,k].imag,2*fft[2][:,k].real])
                         for k in range(1,self.objective_modes+1)])

    def values(self,free):
        if self.last_free is not None and np.array_equal(free,self.last_free):return self.last_values
        vector=self.expand(free)
        coeff,alpha=self.unpack(vector)
        vx,vt=self.jets(self.pack(coeff,np.zeros(self.mean_count)))
        ax=self.base_x+np.tensordot(alpha,self.means_d,axes=(0,0)).T[:,None,:]
        at=self.base_t.copy();at[:,:,1]+=np.tensordot(alpha,self.means_c,axes=(0,0))[0,:,None]
        dxx=2*np.sum(ax*vx,axis=2)+np.sum(vx*vx,axis=2)
        dxt=np.sum(ax*vt+vx*at+vx*vt,axis=2)
        dtt=2*np.sum(at*vt,axis=2)+np.sum(vt*vt,axis=2)
        tensor=self.extract(dxx,dxt,dtt)
        base=(tensor.transpose(2,0,1).reshape(len(self.x),-1)/self.row_scale).ravel()
        boundary=np.array([float((self.at_end[1]@coeff[k,0])[0]+
                                 rate*(self.at_end[0]@coeff[k,0])[0])
                           for k,rate in enumerate(self.end_rate)])
        action_data=self.action(alpha) if self.action_constraint else None
        residual=np.r_[base*self.row_weight,boundary]
        if action_data is not None:residual=np.r_[residual,action_data[0]-self.reference_action]
        self.last_free=free.copy()
        self.last_values=(vector,tensor,residual,ax+vx,at+vt,action_data,base,boundary)
        return self.last_values

    def fun(self,free):
        vector,tensor,residual,fx,ft,action_data,base,boundary=self.values(free)
        self.ncall+=1
        rec=dict(call=self.ncall,cost=float(residual@residual/2),
                 maximum_weighted_tensor=float(abs(base).max()),
                 maximum_robin=float(abs(boundary).max()),
                 alpha=self.unpack(vector)[1].tolist())
        if action_data is not None:rec['action_error']=action_data[0]-self.reference_action
        self.history.append(rec)
        if hasattr(self,'snapshot_path') and rec['cost']<getattr(self,'best_cost',float('inf')):
            self.best_cost=rec['cost'];self.save(vector,self.snapshot_path,self.waist)
        print(json.dumps(rec),flush=True)
        return residual

    def normal_system(self,free):
        """Assemble J^T J and J^T r in radial blocks without a giant J.

        Local BLAS Gram products keep the quintic support bandwidth. This is
        the same sampled least-squares linearization, not another equation.
        """
        vector,tensor,residual,fx,ft,action_data,base,boundary=self.values(free)
        n,q,kout,kin=self.points,len(self.x),3*self.objective_modes,3*self.modes
        aa=np.zeros((q,kout,kin));bb=np.zeros_like(aa)
        for j in range(kin):
            k,c=divmod(j,3);m,co,si=self.mode[k],self.cos[k],self.sin[k]
            dxv=np.zeros_like(fx);dxd=np.zeros_like(fx);dtv=np.zeros_like(ft)
            p=4 if c<2 else 3;weight=self.a**p;derivative=p*self.ap/self.a*weight
            trig=si if c==1 else co
            dxv[:,:,c]=derivative[:,None]*trig;dxd[:,:,c]=weight[:,None]*trig
            if c==0:
                dtv[:,:,0]=-m*weight[:,None]*si;dtv[:,:,1]=weight[:,None]*co
            elif c==1:
                dtv[:,:,0]=-weight[:,None]*si;dtv[:,:,1]=m*weight[:,None]*co
            else:dtv[:,:,2]=-m*weight[:,None]*si
            aa[:,:,j]=self.cross(fx,ft,dxv,dtv).transpose(2,0,1).reshape(q,kout)
            bb[:,:,j]=self.cross(fx,ft,dxd,np.zeros_like(ft)).transpose(2,0,1).reshape(q,kout)
        aa/=self.row_scale[:,:,None];bb/=self.row_scale[:,:,None]
        aa*=np.sqrt(self.quadrature_weights)[:,None,None]
        bb*=np.sqrt(self.quadrature_weights)[:,None,None]
        coeff,alpha=self.unpack(vector)
        vx,vt=self.jets(self.pack(coeff,np.zeros(self.mean_count)))
        mean_columns=[]
        for i in range(self.mean_count):
            al=np.zeros(self.mean_count);al[i]=1.
            dx,dt=self.jets(self.pack(np.zeros_like(coeff),al))
            column=self.cross(vx,vt,dx,dt).transpose(2,0,1).reshape(q,kout)/self.row_scale
            mean_columns.append(column*np.sqrt(self.quadrature_weights)[:,None])
        mean_columns=np.stack(mean_columns,axis=2)
        matrices=[self.even[0].tocsr(),self.odd[0].tocsr(),self.even[1].tocsr(),self.odd[1].tocsr()]
        width=5
        bands=np.zeros((n,2*width+1,kin,kin))
        cross_mean=np.zeros((n,kin,self.mean_count))
        mean_gram=np.zeros((self.mean_count,self.mean_count))
        gradient=np.zeros((n,kin));mean_gradient=np.zeros(self.mean_count)
        rmat=residual[:q*kout].reshape(q,kout)
        for row in range(q):
            support=np.unique(np.concatenate([mat.getrow(row).indices for mat in matrices]))
            weights=[mat.getrow(row)[:,support].toarray().ravel() for mat in matrices]
            blocks=[]
            for j in range(len(support)):
                val=np.tile([weights[0][j],weights[0][j],weights[1][j]],self.modes)
                der=np.tile([weights[2][j],weights[2][j],weights[3][j]],self.modes)
                block=aa[row]*val[None,:]+bb[row]*der[None,:]
                block[abs(block)<1e-15]=0.
                blocks.append(block)
            local=np.concatenate(blocks,axis=1)
            gram=local.T@local
            local_gradient=local.T@rmat[row]
            mc=mean_columns[row]
            local_cross=local.T@mc
            mean_gram+=mc.T@mc;mean_gradient+=mc.T@rmat[row]
            for ii,node_i in enumerate(support):
                i=slice(ii*kin,(ii+1)*kin)
                gradient[node_i]+=local_gradient[i]
                cross_mean[node_i]+=local_cross[i]
                for jj,node_j in enumerate(support):
                    offset=int(node_j-node_i)
                    if abs(offset)>width:raise RuntimeError('unexpected spline support width')
                    j=slice(jj*kin,(jj+1)*kin)
                    bands[node_i,offset+width]+=gram[i,j]
        for k,rate in enumerate(self.end_rate):
            end=(self.at_end[1]+rate*self.at_end[0]).tocoo()
            c=3*k
            for node_i,value_i in zip(end.col,end.data):
                gradient[node_i,c]+=value_i*boundary[k]
                for node_j,value_j in zip(end.col,end.data):
                    bands[node_i,int(node_j-node_i)+width,c,c]+=value_i*value_j
        if action_data is not None:
            mean_gram+=np.outer(action_data[1],action_data[1])
            mean_gradient+=action_data[1]*(action_data[0]-self.reference_action)
        rows=[];cols=[];vals=[]
        cr,cc=np.indices((kin,kin))
        for i in range(n):
            for d in range(-width,width+1):
                j=i+d
                if not 0<=j<n:continue
                block=bands[i,d+width]
                mask=block!=0.
                rows.append((i*kin+cr[mask]).astype(np.int32))
                cols.append((j*kin+cc[mask]).astype(np.int32));vals.append(block[mask])
        cross=cross_mean.reshape(n*kin,self.mean_count)
        ir,ic=np.indices(cross.shape)
        rows.extend([ir.ravel().astype(np.int32),(n*kin+ic).ravel().astype(np.int32)])
        cols.extend([(n*kin+ic).ravel().astype(np.int32),ir.ravel().astype(np.int32)])
        vals.extend([cross.ravel(),cross.ravel()])
        ir,ic=np.indices(mean_gram.shape)
        rows.append((n*kin+ir).ravel().astype(np.int32));cols.append((n*kin+ic).ravel().astype(np.int32));vals.append(mean_gram.ravel())
        del aa,bb,bands,mean_columns,cross_mean
        full=coo_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),
                        shape=(n*kin+self.mean_count,n*kin+self.mean_count)).tocsc()
        full.eliminate_zeros()
        del rows,cols,vals
        radial_to_mode=np.r_[(np.arange(kin)[None,:]*n+np.arange(n)[:,None]).ravel(),
                             np.arange(n*kin,n*kin+self.mean_count)]
        transform=self.projector[radial_to_mode,:]
        reduced=(transform.T@full@transform).tocsc()
        reduced_gradient=np.asarray(transform.T@np.r_[gradient.ravel(),mean_gradient]).ravel()
        return reduced,reduced_gradient

    def jac(self,free):
        vector,tensor,residual,fx,ft,action_data,base,boundary=self.values(free)
        n,q,kout,kin=self.points,len(self.x),3*self.objective_modes,3*self.modes
        aa=np.zeros((q,kout,kin));bb=np.zeros_like(aa)
        for j in range(kin):
            k,c=divmod(j,3);m,co,si=self.mode[k],self.cos[k],self.sin[k]
            dxv=np.zeros_like(fx);dxd=np.zeros_like(fx);dtv=np.zeros_like(ft)
            p=4 if c<2 else 3;weight=self.a**p;derivative=p*self.ap/self.a*weight
            trig=si if c==1 else co
            dxv[:,:,c]=derivative[:,None]*trig;dxd[:,:,c]=weight[:,None]*trig
            if c==0:
                dtv[:,:,0]=-m*weight[:,None]*si;dtv[:,:,1]=weight[:,None]*co
            elif c==1:
                dtv[:,:,0]=-weight[:,None]*si;dtv[:,:,1]=m*weight[:,None]*co
            else:dtv[:,:,2]=-m*weight[:,None]*si
            aa[:,:,j]=self.cross(fx,ft,dxv,dtv).transpose(2,0,1).reshape(q,kout)
            bb[:,:,j]=self.cross(fx,ft,dxd,np.zeros_like(ft)).transpose(2,0,1).reshape(q,kout)
        aa/=self.row_scale[:,:,None];bb/=self.row_scale[:,:,None]
        aa*=np.sqrt(self.quadrature_weights)[:,None,None]
        bb*=np.sqrt(self.quadrature_weights)[:,None,None]
        rows=[];cols=[];vals=[];eqs=np.arange(kout,dtype=np.int32)
        for j in range(kin):
            basis=self.odd if j%3==2 else self.even
            for dense,mat in [(aa,basis[0]),(bb,basis[1])]:
                mm=mat.tocoo();rr=mm.row.astype(np.int32);cc=mm.col.astype(np.int32)
                values=dense[rr,:,j]*mm.data[:,None]
                # Ordinary-double Jacobian only: remove numerical FFT zeros
                # below 1e-15 after the fixed residual scaling. The nonlinear
                # residual itself is never truncated by this threshold.
                ir,ic=np.nonzero(abs(values)>1e-15)
                rows.append((rr[ir]*kout+ic).astype(np.int32))
                cols.append((j*n+cc[ir]).astype(np.int32))
                vals.append(values[ir,ic])
        coeff,alpha=self.unpack(vector)
        nonmean_x,nonmean_t=self.jets(self.pack(coeff,np.zeros(self.mean_count)))
        for i in range(self.mean_count):
            al=np.zeros(self.mean_count);al[i]=1.
            dx,dt=self.jets(self.pack(np.zeros_like(coeff),al))
            column=(self.cross(nonmean_x,nonmean_t,dx,dt).transpose(2,0,1).reshape(q,kout)/self.row_scale).ravel()*self.row_weight
            rows.append(np.arange(q*kout,dtype=np.int32))
            cols.append(np.full(q*kout,kin*n+i,dtype=np.int32))
            vals.append(column)
        for k,rate in enumerate(self.end_rate):
            end=(self.at_end[1]+rate*self.at_end[0]).tocoo()
            rows.append(np.full(end.nnz,q*kout+k,dtype=np.int32))
            cols.append(3*k*n+end.col.astype(np.int32));vals.append(end.data)
        count=q*kout+self.modes
        if action_data is not None:
            rows.append(np.full(self.mean_count,count,dtype=np.int32))
            cols.append(np.arange(kin*n,kin*n+self.mean_count,dtype=np.int32));vals.append(action_data[1])
            count+=1
        jac=coo_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(count,kin*n+self.mean_count)).tocsr()
        jac.eliminate_zeros()
        return (jac@self.projector).tocsr()


def normal_gauss_newton(s,initial,iterations=15,damping=1e-9):
    """Column-equilibrated damped normal solves, with actual-residual search.

    Normal equations lose conditioning; their use here is exploratory only.
    The accepted candidate is always checked using the original residual.
    """
    free=initial.copy();nfev=0;njev=0;message='iteration limit'
    residual=s.fun(free);nfev+=1;cost=float(residual@residual/2)
    components=getattr(s,'components',3)
    physical=components*s.modes*s.points
    keys=np.where(s.keep<physical,(s.keep%s.points)*(components*s.modes)+s.keep//s.points,s.keep)
    permutation=np.argsort(keys)
    for it in range(iterations):
        raw_normal,raw_gradient=s.normal_system(free);njev+=1
        norm=np.sqrt(np.maximum(0.,raw_normal.diagonal()))
        scale=1/np.maximum(norm,1e-12)
        normal=(diags(scale)@raw_normal@diags(scale)).tocsc()
        del raw_normal
        gradient=scale*raw_gradient
        identity=eye(len(free),format='csc')
        ordered_normal=normal[permutation,:][:,permutation].tocsc()
        accepted=False
        for attempt in range(7):
            lu=splu(ordered_normal+damping*identity,permc_spec='NATURAL',
                     diag_pivot_thresh=0.,options={'SymmetricMode':True})
            scaled_step=np.empty_like(gradient)
            scaled_step[permutation]=lu.solve(-gradient[permutation])
            # SuperLU retains substantial native storage. Release each factor
            # before line search or a new regularization attempt; otherwise the
            # next factorization transiently coexists with the previous one.
            del lu
            delta=scale*scaled_step
            lin=float(np.max(abs((normal+damping*identity)@scaled_step+gradient)))
            for power in range(12):
                fraction=2.**(-power)
                trial=free+fraction*delta
                try:rr=s.fun(trial)
                except ValueError:continue
                nfev+=1;newcost=float(rr@rr/2)
                if newcost<cost:
                    free,residual=trial,rr;oldcost,cost=cost,newcost;accepted=True
                    print(json.dumps(dict(normal_iteration=it,regularization=damping,
                                          fraction=fraction,linear_normal_residual=lin,
                                          relative_improvement=(oldcost-cost)/oldcost,
                                          scaled_gradient=float(abs(gradient).max()))),flush=True)
                    damping=max(1e-13,damping/3) if fraction==1 else damping
                    break
            if accepted:break
            damping*=10
        # Do not retain three previous normal matrices during the next local
        # Gram assembly (or the final optimality calculation). The M24 probe
        # measured 579 MB before release and 131 MB after this cleanup.
        del normal,ordered_normal,identity
        gc.collect()
        if not accepted:message='no actual-residual decrease';break
        if cost<1e-26:message='small sampled least-squares cost';break
    raw_normal,raw_gradient=s.normal_system(free);njev+=1
    optimality=float(np.max(abs(raw_gradient)))
    return SimpleNamespace(x=free,cost=cost,status=0,message=message,nfev=nfev,njev=njev,optimality=optimality)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--modes',type=int,default=16)
    ap.add_argument('--points',type=int,default=151)
    ap.add_argument('--mesh',choices=['uniform','graded'],default='uniform')
    ap.add_argument('--gauss',type=int,default=2)
    ap.add_argument('--mu-scale',type=float,default=4.)
    ap.add_argument('--means',type=int,default=3)
    ap.add_argument('--waist',type=float,default=.06)
    ap.add_argument('--action',action='store_true')
    ap.add_argument('--retained-only',action='store_true')
    ap.add_argument('--fix-mean-height',action='store_true')
    ap.add_argument('--start-old',type=Path)
    ap.add_argument('--start-cache',type=Path)
    ap.add_argument('--max-evaluations',type=int,default=30)
    ap.add_argument('--lsmr-iterations',type=int,default=250)
    ap.add_argument('--linear-method',choices=['lsmr','normal'],default='lsmr')
    ap.add_argument('--regularization',type=float,default=1e-9)
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    s=Overcollocation(modes=args.modes,points=args.points,mu_scale=args.mu_scale,means=args.means,gauge='none',mesh=args.mesh)
    initial=s.seed(args.waist)
    if args.start_old:initial=s.from_old(ps.load_series(args.start_old))
    if args.start_cache:
        with np.load(args.start_cache,allow_pickle=False) as f:
            meta=json.loads(str(f['metadata']));oldvector=f['vector']
        old=SplineNewton(**meta['parameters']);candidate=old.candidate(oldvector,meta['epsilon'])
        coeff=np.zeros((s.modes,3,s.points))
        for k,m in enumerate(s.mode):
            if int(m) not in candidate['splines']:continue
            val=candidate['splines'][int(m)](s.x).T
            for j in range(3):coeff[k,j]=s.value_lu[int(j==2)].solve(val[j]/s.a**(3 if j==2 else 4))
        alpha=old.unpack(oldvector)[1]
        if len(alpha)<s.mean_count:alpha=np.r_[alpha,np.zeros(s.mean_count-len(alpha))]
        initial=s.pack(coeff,alpha)
    height_reference=None
    if args.fix_mean_height:
        alpha=s.unpack(initial)[1]
        height_reference=float(s.base_spline(np.array([s.length]))[0,2]+
                               sum(al*sp(np.array([s.length]))[0,2] for al,sp in zip(alpha,s.mean_splines)))
    s.prepare(args.waist,args.gauss,not args.retained_only,args.action,height_reference)
    free=initial[s.keep]
    args.cache.parent.mkdir(parents=True,exist_ok=True)
    s.snapshot_path=args.cache
    if args.linear_method=='normal':
        result=normal_gauss_newton(s,free,args.max_evaluations,args.regularization)
    else:
        result=least_squares(s.fun,free,jac=s.jac,method='trf',tr_solver='lsmr',x_scale='jac',
                             ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=args.max_evaluations,
                             tr_options=dict(atol=1e-10,btol=1e-10,maxiter=args.lsmr_iterations,regularize=True),verbose=2)
    vector=s.expand(result.x)
    diagnostic=s.diagnostic(vector,args.waist)
    args.cache.parent.mkdir(parents=True,exist_ok=True)
    s.save(vector,args.cache,args.waist)
    report=dict(kind='floating_actual_spline_overcollocation_not_proof',
                parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
                status=int(result.status),message=result.message,nfev=int(result.nfev),njev=int(result.njev),
                cost=float(result.cost),optimality=float(result.optimality),
                exact_waist_coefficient=float(s.waist_row@s.unpack(vector)[0][0,0]),
                diagnostic=diagnostic,history=s.history,
                limitations=['Finite angular approximation','Finite Robin endpoint','Floating arithmetic',
                             'Sampled residuals only','No closed fixed-cap surface or certified reach'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(diagnostic=diagnostic,cost=float(result.cost))),flush=True)

if __name__=='__main__':main()
