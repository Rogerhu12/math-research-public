#!/usr/bin/env python3
"""Complete M12 three-Gram normal bands for the coupled planar Fourier basis.

This is a new consumer of the general band/triangular utilities in R244.
The real planar coefficient multiplies (cos(m u),sin(m u),0), so both xy
cross covariances are retained. All actual discrete angular moments are
used, including aliases. eta*S belongs only to the invertible right
preconditioner; the physical least-squares objective has lambda=0.
"""
from __future__ import annotations
import hashlib,importlib.util,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import cholesky_banded
from scipy.linalg.blas import dtbsv
from scipy.sparse.linalg import LinearOperator

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load_helper(path):
    spec=importlib.util.spec_from_file_location('m12_complete_normal_generic',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def coupled_terms(basis):
    """Exact complex-vector coefficients of every real M12 angular column."""
    pm=np.asarray(basis.pm,dtype=int);zm=np.asarray(basis.zm,dtype=int)
    if len(pm)+len(zm)!=basis.na or not np.array_equal(basis.modes,np.r_[pm,zm]):
        raise ValueError('Full coupled M12 planar/cosine-height layout required')
    if np.any(pm==0) or not len(zm) or zm[0]!=0 or np.any(zm[1:]<=0):
        raise ValueError('Expected nonzero signed planar modes and the true height constant')
    frequency=np.zeros((2,basis.na),dtype=int)
    coefficient=np.zeros((2,basis.na,3),dtype=complex)
    for j,m in enumerate(pm):
        frequency[:,j]=m,-m
        coefficient[0,j,:2]=.5,-.5j
        coefficient[1,j,:2]=.5,.5j
    for j,k in enumerate(zm,start=len(pm)):
        if k==0:coefficient[0,j,2]=1.
        else:
            frequency[:,j]=k,-k
            coefficient[:,j,2]=.5
    return frequency,coefficient

def point_covariance(xs,xt,bb,weight):
    """[Wt,Ws] physical first-jet covariance, including all xy/xz/yz terms.

    Result axes: radial, angle, radial-basis derivative, Cartesian,
    radial-basis derivative, Cartesian. B0 multiplies Wt's beta-prime;
    B1 multiplies Ws's beta. The existing actual quadrature is included.
    """
    outer=lambda a,b:np.einsum('...c,...d->...cd',a,b)
    ss,tt,st=outer(xs,xs),outer(xt,xt),outer(xs,xt)
    b2=bb**2;w2=weight**2
    cov=np.empty((*bb.shape,2,3,2,3))
    cov[:,:,0,:,0,:]=(2*ss/b2[...,None,None]+4*tt/(b2*b2)[...,None,None])*w2[...,None,None]
    cov[:,:,1,:,1,:]=(4*ss+2*tt/b2[...,None,None])*w2[...,None,None]
    cov[:,:,0,:,1,:]=2*st*w2[...,None,None]/b2[...,None,None]
    cov[:,:,1,:,0,:]=np.swapaxes(cov[:,:,0,:,1,:],-1,-2)
    return cov

class CompleteGramNormal:
    def __init__(self,linear,eta=1e-6,helper_path=None,assembly_block=8):
        began=time.monotonic();self.linear=linear;self.basis=linear.basis
        self.eta=float(eta);self.block=int(assembly_block)
        if not math.isfinite(self.eta) or self.eta<=0 or self.block<1:
            raise ValueError('Positive finite preconditioner eta and block size required')
        if helper_path is None:helper_path=Path(__file__).with_name('6a65-cartesian-complete-radial-normal.py')
        self.helper_path=Path(helper_path);self.helper=load_helper(self.helper_path)
        basis=self.basis;nb,nc,N=basis.nb,basis.na,linear.N;n=nb*nc
        if linear.shape!=(len(linear.nodes)*N*3,n) or linear.bandwidth!=5:
            raise ValueError('Exactly the original three Gram rows and quintic radial columns required')
        if N%2 or N<=2*max(np.max(np.abs(basis.pm)),np.max(basis.zm)):
            raise ValueError('Every actual angular column must be represented')
        self.dimension=n;self.half_bandwidth=min(6*nc-1,n-1)
        self.normal_band=np.zeros((self.half_bandwidth+1,n))
        self.old_groups=[];coverage=np.zeros(nc,dtype=int)
        for k,(lower,upper) in linear.factors.items():
            columns=np.flatnonzero(np.abs(basis.modes)==int(k))
            if len(columns):self.old_groups.append((lower.copy(),columns));coverage[columns]+=1
        if np.any(coverage!=1):raise ValueError('Every original H1 channel must appear once')
        frequency,coefficient=coupled_terms(basis)
        angular_derivative=(1,0) # B0 beta-prime, B1 beta
        maximum_imaginary=maximum_real=maximum_asymmetry=0.
        covariance_points=alias_pairs=largest_temporary=0
        timing={'covariance':0.,'angular':0.,'radial':0.,'equilibration':0.,'cholesky':0.}
        triangles={}
        for left in range(0,len(linear.nodes),self.block):
            sl=slice(left,min(left+self.block,len(linear.nodes)))
            B=np.stack((linear.B0[sl].toarray(),linear.B1[sl].toarray()))
            live=np.any(B!=0,axis=0)
            if not np.any(live):continue
            t0=time.monotonic()
            cov=point_covariance(linear.Xs[sl],linear.Xt[sl],linear.bb[sl],linear.weight[sl])
            spectrum=np.fft.rfft(cov,axis=1)
            largest_temporary=max(largest_temporary,cov.nbytes+spectrum.nbytes+B.nbytes)
            covariance_points+=len(B[0])*N;del cov
            timing['covariance']+=time.monotonic()-t0;t0=time.monotonic()
            Q=np.zeros((len(B[0]),nc,nc,2,2),dtype=complex)
            for d in range(2):
                for e in range(2):
                    sector=spectrum[:,:,d,:,e,:]
                    for ls in range(2):
                        fa=frequency[ls];za=coefficient[ls]*(1j*fa[:,None])**angular_derivative[d]
                        for rs in range(2):
                            fb=frequency[rs];zb=coefficient[rs]*(1j*fb[:,None])**angular_derivative[e]
                            freq=fa[:,None]+fb[None,:]
                            F=self.helper.positive_exponential_moment(sector,freq,N)
                            Q[:,:,:,d,e]+=np.einsum('ic,sijcd,jd->sij',za,F,zb,optimize=True)
                            if d==e==0:
                                live_pair=np.any(za!=0,axis=1)[:,None]&np.any(zb!=0,axis=1)[None,:]
                                alias_pairs+=int(np.count_nonzero((np.abs(freq)>N//2)&live_pair))
                            largest_temporary=max(largest_temporary,spectrum.nbytes+Q.nbytes+F.nbytes+B.nbytes)
                            del F
            maximum_imaginary=max(maximum_imaginary,float(np.max(abs(Q.imag))))
            maximum_real=max(maximum_real,float(np.max(abs(Q.real))))
            Q=Q.real.copy();opposite=Q.transpose(0,2,1,4,3)
            maximum_asymmetry=max(maximum_asymmetry,float(np.max(abs(Q-opposite))))
            Q=.5*(Q+opposite);del opposite,spectrum
            timing['angular']+=time.monotonic()-t0;t0=time.monotonic()
            for row,mask in enumerate(live):
                active=np.flatnonzero(mask)
                if not len(active):continue
                if len(active)>6 or np.any(np.diff(active)!=1):
                    raise ValueError('Contiguous quintic support of at most six columns required')
                width=len(active)*nc
                if width not in triangles:
                    rr,cc=np.tril_indices(width);triangles[width]=(rr,cc,rr-cc)
                rr,cc,dist=triangles[width]
                weights=B[:,row,active]
                local=np.einsum('di,mnde,ej->imjn',weights,Q[row],weights,optimize=True).reshape(width,width)
                columns=int(active[0])*nc+cc
                self.normal_band[dist,columns]+=local[rr,cc]
                largest_temporary=max(largest_temporary,Q.nbytes+B.nbytes+local.nbytes+rr.nbytes+cc.nbytes+dist.nbytes+columns.nbytes)
            timing['radial']+=time.monotonic()-t0
        if not np.all(np.isfinite(self.normal_band)):raise ArithmeticError('Nonfinite full normal band')
        t0=time.monotonic();packed=np.array(self.normal_band,order='F')
        for lower,columns in self.old_groups:
            old=self.helper.lower_product_band(lower)
            for offset in range(min(5,nb-1)+1):
                count=nb-offset;indices=(np.arange(count)[:,None]*nc+columns[None,:]).ravel()
                packed[offset*nc,indices]+=self.eta*np.broadcast_to(old[offset,:count,None],(count,len(columns))).ravel()
        diagonal=packed[0].copy()
        if np.any(diagonal<=0) or not np.all(np.isfinite(diagonal)):
            raise ArithmeticError('Positive full physical preconditioner diagonal required')
        self.diagonal_scale=1/np.sqrt(diagonal)
        for offset in range(self.half_bandwidth+1):
            count=n-offset;packed[offset,:count]*=self.diagonal_scale[offset:]*self.diagonal_scale[:count]
        timing['equilibration']=time.monotonic()-t0;t0=time.monotonic()
        self.factor=np.asfortranarray(cholesky_banded(packed,lower=True,overwrite_ab=True,check_finite=True))
        timing['cholesky']=time.monotonic()-t0
        self.receipt={'schema':'6a65-M12-complete-three-Gram-normal-band-v1',
            'script_sha256':sha(__file__),'generic_R244_helper_sha256':sha(self.helper_path),
            'columns':n,'physical_rows':linear.shape[0],'radial_blocks':nb,'angular_channels':nc,
            'angular_nodes':N,'radial_block_half_bandwidth':5,'scalar_half_bandwidth':self.half_bandwidth,
            'preconditioner_eta':self.eta,'physical_objective_lambda':0.,'required_LSMR_damp':0.,
            'normal_band_bytes':self.normal_band.nbytes,'factor_bytes':self.factor.nbytes,
            'all_three_Gram_rows_and_all_cross_channels_retained':True,
            'coupled_planar_xy_terms_retained':True,'discrete_angular_moments_without_truncation':True,
            'alias_frequency_pairs':alias_pairs,'assembled_points':covariance_points,
            'maximum_imaginary_roundoff':maximum_imaginary,
            'relative_imaginary_roundoff':maximum_imaginary/max(np.finfo(float).tiny,maximum_real),
            'maximum_Q_asymmetry_before_roundoff_symmetrization':maximum_asymmetry,
            'diagonal_equilibration_changes_physical_P':False,
            'largest_explicit_temporary_bytes':largest_temporary,'temporary_bytes_are_process_RSS':False,
            'timings_seconds':timing,'seconds':time.monotonic()-began,
            'lambda_zero_positive_spectral_lower_bound_claimed':False,
            'new_M12_field_or_refinement_improvement_claimed':False}

    def unpack(self,vector):
        vector=np.asarray(vector,dtype=float).ravel()
        if vector.size!=self.dimension:raise ValueError('All actual physical coefficient columns required')
        value=dtbsv(self.half_bandwidth,self.factor,vector,lower=1,trans=1)
        return (self.diagonal_scale*value).reshape(self.basis.nb,self.basis.na)

    def transpose(self,gradient):
        gradient=np.asarray(gradient,dtype=float).ravel()
        if gradient.size!=self.dimension:raise ValueError('All actual physical gradient columns required')
        return dtbsv(self.half_bandwidth,self.factor,self.diagonal_scale*gradient,lower=1,trans=0)

    def physical_gradient(self,coordinate_gradient):
        """Recover g from q=T^T g: g=D^-1 L q, not the old H1 transform."""
        q=np.asarray(coordinate_gradient,dtype=float).ravel()
        if q.size!=self.dimension:raise ValueError('Full preconditioned gradient required')
        result=np.zeros_like(q)
        for offset in range(self.half_bandwidth+1):
            count=self.dimension-offset;result[offset:]+=self.factor[offset,:count]*q[:count]
        return (result/self.diagonal_scale).reshape(self.basis.nb,self.basis.na)

class CompleteGramRightPreconditioned:
    """The unchanged physical operator J T. No regularizer rows or LSMR damp."""
    def __init__(self,linear,eta=1e-6,helper_path=None,assembly_block=8):
        self.linear=linear;self.basis=linear.basis;self.shape=linear.shape
        self.blocks=CompleteGramNormal(linear,eta,helper_path,assembly_block)
        self.operator=LinearOperator(self.shape,matvec=self.matvec,rmatvec=self.rmatvec,dtype=float)
        self.receipt={'schema':'6a65-M12-unregularized-complete-Gram-right-preconditioner-v1',
            'physical_objective_lambda':0.,'required_LSMR_damp':0.,'shape':list(self.shape),
            'all_original_rows_columns_metric_and_field_preserved':True,'assembly':self.blocks.receipt}

    def raw_matvec(self,coefficients):
        linear=self.linear;coeff=np.asarray(coefficients,dtype=float).reshape(self.basis.nb,self.basis.na)
        out=np.empty((len(linear.nodes),linear.N,3))
        for left in range(0,len(linear.nodes),linear.block):
            sl=slice(left,min(left+linear.block,len(linear.nodes)))
            Ws=self.basis.angular(linear.B1[sl]@coeff,linear.N)
            Wt=self.basis.angular(linear.B0[sl]@coeff,linear.N,1)
            xs,xt,bb=linear.Xs[sl],linear.Xt[sl],linear.bb[sl]
            out[sl,:,0]=2*np.sum(xs*Ws,axis=-1)
            out[sl,:,1]=np.sqrt(2)*np.sum(xs*Wt+xt*Ws,axis=-1)/bb
            out[sl,:,2]=2*np.sum(xt*Wt,axis=-1)/(bb*bb)
            out[sl]*=linear.weight[sl,:,None]
        return out.ravel()

    def raw_transpose(self,vector):
        linear=self.linear;x=np.asarray(vector,dtype=float).reshape(len(linear.nodes),linear.N,3)
        gradient=np.zeros((self.basis.nb,self.basis.na))
        for left in range(0,len(linear.nodes),linear.block):
            sl=slice(left,min(left+linear.block,len(linear.nodes)))
            z=x[sl]*linear.weight[sl,:,None];e,f,g=z[...,0],z[...,1],z[...,2]
            xs,xt,bb=linear.Xs[sl],linear.Xt[sl],linear.bb[sl]
            V=2*e[...,None]*xs+(np.sqrt(2)*f/bb)[...,None]*xt
            W=(np.sqrt(2)*f/bb)[...,None]*xs+(2*g/(bb*bb))[...,None]*xt
            gradient+=linear.B1[sl].T@self.basis.angular_adjoint(V)+linear.B0[sl].T@self.basis.angular_adjoint(W,1)
        return gradient

    def unpack(self,vector):return self.blocks.unpack(vector)
    def matvec(self,vector):return self.raw_matvec(self.unpack(vector))
    def rmatvec(self,vector):return self.blocks.transpose(self.raw_transpose(vector))
    def physical_normal_residual(self,direction):
        return self.raw_transpose(self.raw_matvec(direction)+self.linear.residual.ravel())
