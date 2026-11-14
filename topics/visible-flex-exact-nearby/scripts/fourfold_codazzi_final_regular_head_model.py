#!/usr/bin/env python3
"""Same complete moving Jacobi body, with every regular outer row retained.

The fixed-nu inverse has waist u=0 and all physical outer mean/Robin rows.
The physical waist C4 amplitude is its scalar output.  No original row or
mean is removed from the full bordered problem; only its Schur pivot changes.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
from fourfold_codazzi_final_head_trial_model import (
    FinalHead as OriginalFinalHead, kernel_rows, exact_float, CANDIDATE,
    ALPHA, NU, RIGHT, sha)

DUAL_KIND='actual_final_physical_all_Robin_dual_regular_complement_v2'
DUAL_COORDINATES='all physical cosine Robin amplitudes including m=4; full outer mean independent'


class FinalHead(OriginalFinalHead):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.identity.update(
            Schur_complement='fixed_nu_complete_regular_outer_rows_waist_amplitude_output',
            regular_complement_source_sha256=sha(__file__),
            old_body_model_source_sha256=sha(Path(__file__).with_name(
                'fourfold_codazzi_final_head_trial_model.py')),
            original_fourth_Robin_row_retained=True,
            parameter_source_convention='D h = (+ partial_nu F) delta_nu + f')

    def regular_rows(self):
        old_left,old_right,fourth,description=super().physical_boundary()
        left=old_left[:self.m]
        amplitude=old_left[-1]
        right=np.vstack((old_right[0],fourth,old_right[1:]))
        if left.shape!=(self.m,self.n) or right.shape!=(self.m+1,self.n):
            raise RuntimeError('complete fixed-nu regular rows have wrong dimensions')
        return left,right,amplitude,dict(description,
            waist_inverse_rows='all u sine amplitudes only',
            outer_inverse_rows='physical C mean and every physical Robin amplitude j=1..N',
            scalar_output='physical C4 amplitude at the waist',
            original_fourth_Robin_row_retained=True,
            no_full_problem_row_removed=True)

    def boundary_problem(self,role):
        U,BR,amplitude,description=self.regular_rows()
        left=np.zeros((self.n+1,self.n));right=np.zeros_like(left)
        parameter=np.zeros((self.n+1,1));rhs=np.zeros(self.n+1)
        if role=='response':
            p=len(U)
            left[:p]=U
            right[p:p+len(BR)]=BR
            # A separate zero dummy keeps the existing n+1 QR protocol.
            parameter[-1,0]=1.
            return left,right,parameter,rhs,dict(description=description,
                artificial_parameter='identically zero dummy in its own right row',
                no_metric_parameter_unknown=True,
                full_regular_rows_kept_in_the_inverse=True)
        if role!='adjoint':raise ValueError('unknown complete regular role')
        # -W psi(0) = ell_amp - U^T lambda_U.  The complete v row,
        # including its mean with weight 1, is prescribed without an SVD.
        p=self.m+1
        left[:p,self.m:]=np.diag(self.weights[self.m:])
        rhs[:p]=-amplitude[self.m:]
        ZR,rank=kernel_rows(BR)
        if len(ZR)!=self.m:raise RuntimeError('the full regular right kernel lost rank')
        right[p:p+len(ZR)]=ZR*self.weights[None,:]
        parameter[-1,0]=1.
        return left,right,parameter,rhs,dict(description=description,
            artificial_parameter='identically zero dummy in its own right row',
            complete_L2_Gram=self.weights.tolist(),right_rank=rank,
            source_output_functional=amplitude.tolist(),
            left_adjoint_sign='W psi_v(0) = - ell_amp,v',
            right_adjoint_sign='W psi(R) = - BR_all^T lambda_R',
            exact_mean_initial_rule='psi2_mean(0) = - physical_amplitude_mean_derivative')

    def recover_dual(self,psi0,psiR):
        U,BR,amplitude,description=self.regular_rows()
        lhs0=self.weights*np.asarray(psi0)+amplitude
        lhsR=-self.weights*np.asarray(psiR)
        lambda0=lhs0[:self.m]
        lambdaR,_,rank,_=np.linalg.lstsq(BR.T,lhsR,rcond=None)
        if rank!=len(BR):raise RuntimeError('all physical regular multiplier rows must retain rank')
        return dict(kind=DUAL_KIND,coordinates=DUAL_COORDINATES,
            background_candidate_sha256=CANDIDATE,
            background_exact_alpha=str(ALPHA),background_exact_nu=str(NU),
            physical_frequency_factor=4,modes=self.m,
            original_fourth_retained_multiplier_is_free=True,
            no_physical_Robin_mode_omitted=True,
            cosine_amplitude_multipliers=[exact_float(x) for x in lambdaR[1:]],
            exact_amp_multiplier='-1',
            exact_model_mean_multiplier=exact_float(lambdaR[0]),
            exact_waist_Dirichlet_multipliers=[exact_float(x) for x in lambda0],
            recovery_residual_left=float(np.max(abs(U.T@lambda0-lhs0))),
            recovery_residual_right=float(np.max(abs(BR.T@lambdaR-lhsR))),
            output_functional='physical waist C4 amplitude',
            source_convention='D h = (+ partial_nu F) delta_nu + f',
            Green_identity='ell_amp[h(0)] = integral(psi D h) + lambda_U U h(0) + lambda_R BR_all h(R)',
            model_physical_boundary_only=True,
            true_mean_and_true_DN_reconstructed_by_complete_consumers=True,
            mathematical_certificate=False)

    def trial_metadata(self,role,*,projected):
        meta=super().trial_metadata(role,projected=projected)
        meta.update(Schur_complement='full_regular_waist_amplitude_output',
            scalar_output='physical waist C4 amplitude',
            original_fourth_Robin_row_retained=True,
            regular_complement_source_sha256=sha(__file__))
        return meta

    def diagnostic_actions(self):
        out=super().diagnostic_actions()
        U,BR,amp,_=self.regular_rows()
        for role in ('response','adjoint'):
            L,R,p,b,info=self.boundary_problem(role)
            if np.count_nonzero(p)!=1 or p[-1,0]!=1 or b[-1]!=0:
                raise RuntimeError('the artificial scalar is not an independent zero dummy')
            if np.any(L[-1]) or np.any(R[-1]):
                raise RuntimeError('the dummy must not change a physical boundary row')
        # A direct full boundary Green pairing, independent of the QR,
        # checks the changed endpoint signs and the complete mean Gram.
        j=np.arange(1,self.n+1,dtype=float)
        h0=np.sin(j/7)/(1+j);hR=np.cos(j/11)/(1+j)
        psi0=np.zeros(self.n);psi0[:self.m]=np.cos(j[:self.m]/13)
        psi0[self.m:]=-amp[self.m:]/self.weights[self.m:]
        lambdar=np.sin(np.arange(1,self.m+2,dtype=float)/17)
        psiR=-(BR.T@lambdar)/self.weights
        lambdau=(self.weights*psi0)[:self.m]
        green=(np.dot(self.weights*psiR,hR)-np.dot(self.weights*psi0,h0)
               +np.dot(lambdau,U@h0)+np.dot(lambdar,BR@hR)-np.dot(amp,h0))
        if abs(green)>5e-11:
            raise RuntimeError('the full regular/waist output boundary Green identity failed')
        dual=self.recover_dual(psi0,psiR)
        if max(dual['recovery_residual_left'],dual['recovery_residual_right'])>5e-11:
            raise RuntimeError('the complete all-mode regular multiplier recovery failed')
        out['regular_complement_boundary']=dict(
            all_waist_u_rows=len(U),all_outer_mean_and_Robin_rows=len(BR),
            scalar_output='waist physical C4',no_physical_row_deleted=True,
            original_fourth_Robin_row_retained=True,
            full_L2_Gram_and_adjoint_source_sign_kept=True,
            direct_full_boundary_Green_error=float(abs(green)),
            all_mode_multiplier_recovery_error=max(
                dual['recovery_residual_left'],dual['recovery_residual_right']))
        return out
