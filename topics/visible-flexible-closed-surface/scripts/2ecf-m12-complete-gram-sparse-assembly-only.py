#!/usr/bin/env python3
"""Assemble the unchanged complete M12 J^T J without an unused H1 factor.

The original three-Gram covariance, every Fourier cross term, aliases and
radial accumulation are retained. The only matrix uses Fortran layout so
its caller can consume it in place for the actual H2 step. No preconditioner
factor or duplicate physical band is allocated by this consumer.
"""
from __future__ import annotations
import hashlib,importlib.util,json,math,resource,time
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

ORIGINAL_SOURCE_SHA='f19a09b0d4efbb9f6f8122de446f371306d291dfa47cf0dfeb7727fe0e0b18f9'

def resident():
    out={'peak_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    for line in Path('/proc/self/status').read_text().splitlines():
        if line.startswith('VmRSS:'):out['current_KiB']=int(line.split()[1])
    return out

ANGULAR_SOURCE_SHA='a5c2715adaf7653f4e79f90c475c88f122bd0d08bbe0a9e901c006dbef606a64'

class CompleteGramNormalAssemblyOnly:
    def __init__(self,linear,eta=1e-6,helper_path=None,assembly_block=8):
        began=time.monotonic();self.linear=linear;self.basis=linear.basis
        self.eta=float(eta);self.block=int(assembly_block)
        if not math.isfinite(self.eta) or self.eta<=0 or self.block<1:
            raise ValueError('Positive finite preconditioner eta and block size required')
        if helper_path is None:helper_path=Path(__file__).with_name('6a65-cartesian-complete-radial-normal.py')
        self.helper_path=Path(helper_path);self.helper=load_helper(self.helper_path)
        if sha(self.helper_path.with_name('6a65-m12-complete-gram-normal-preconditioner.py'))!=ORIGINAL_SOURCE_SHA:raise ValueError('The compared complete-Gram source changed')
        basis=self.basis;nb,nc,N=basis.nb,basis.na,linear.N;n=nb*nc
        if linear.shape!=(len(linear.nodes)*N*3,n) or linear.bandwidth!=5:
            raise ValueError('Exactly the original three Gram rows and quintic radial columns required')
        if N%2 or N<=2*max(np.max(np.abs(basis.pm)),np.max(basis.zm)):
            raise ValueError('Every actual angular column must be represented')
        self.dimension=n;self.half_bandwidth=min(6*nc-1,n-1)
        self.normal_band=np.zeros((self.half_bandwidth+1,n),order='F')
        self.old_groups=[];coverage=np.zeros(nc,dtype=int)
        for k,(lower,upper) in linear.factors.items():
            columns=np.flatnonzero(np.abs(basis.modes)==int(k))
            if len(columns):self.old_groups.append((lower.copy(),columns));coverage[columns]+=1
        if np.any(coverage!=1):raise ValueError('Every original H1 channel must appear once')
        angular_path=Path(__file__).with_name('2ecf-m12-complete-sparse-cartesian-angular.py')
        if sha(angular_path)!=ANGULAR_SOURCE_SHA:raise ValueError('Audited M12 sparse Cartesian angular source changed')
        angular=load_helper(angular_path)
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
            Q,angular_receipt=angular.contract(spectrum,frequency,coefficient,N)
            alias_pairs+=angular_receipt['discrete_alias_frequency_pairs']
            largest_temporary=max(largest_temporary,spectrum.nbytes+B.nbytes+angular_receipt['largest_explicit_kernel_bytes'])
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
            if left%(self.block*16)==0 or left+self.block>=len(linear.nodes):
                print(json.dumps({'stage':'complete-Gram-only-assembly','radial_rows_completed':left+len(B[0]),'radial_rows_total':len(linear.nodes),'normal_band_bytes':self.normal_band.nbytes,'resident':resident(),'seconds':time.monotonic()-began}),flush=True)
        if not np.all(np.isfinite(self.normal_band)):raise ArithmeticError('Nonfinite full normal band')
        self.receipt={'schema':'2ecf-M12-complete-three-Gram-sparse-cartesian-assembly-only-v1',
            'script_sha256':sha(__file__),'angular_kernel_sha256':ANGULAR_SOURCE_SHA,'same_complete_point_covariance_and_radial_accumulation':True,'floating_angular_sum_grouping_changed':True,'generic_R244_helper_sha256':sha(self.helper_path),
            'columns':n,'physical_rows':linear.shape[0],'radial_blocks':nb,'angular_channels':nc,
            'angular_nodes':N,'radial_block_half_bandwidth':5,'scalar_half_bandwidth':self.half_bandwidth,
            'unused_H1_factor_constructed':False,'original_complete_Gram_source_sha256':ORIGINAL_SOURCE_SHA,'normal_band_layout':'Fortran contiguous','physical_objective_lambda':0.,
            'normal_band_bytes':self.normal_band.nbytes,'factor_bytes':0,
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
