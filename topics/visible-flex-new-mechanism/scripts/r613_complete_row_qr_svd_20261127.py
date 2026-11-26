#!/usr/bin/env python3
"""Complete-row QR/SVD organization for a future declared height scope.

This module does not build a Jacobian, choose an input, evaluate geometry,
or start a solve. A caller supplies its already charged complete J and
residual. Every row is retained. The only SVD is of the small QR factor;
no normal equations, singular-value truncation or science probe is added.
"""
from collections import defaultdict
import numpy as np

COUNTS=defaultdict(int)


class CompleteRowFactor:
    def __init__(self,J,residual,*,batch_rows=4096,deadline_check=None):
        if J.ndim!=2 or residual.ndim!=1 or J.shape[0]!=len(residual):
            raise ValueError("complete Jacobian and residual shapes differ")
        m,n=J.shape
        if m<n+1 or batch_rows<n+1:
            raise ValueError("declared tall complete-row factorization required")
        self.shape=(m,n)
        self.batch_rows=int(batch_rows)
        check=(lambda:None) if deadline_check is None else deadline_check
        norms=np.zeros(n)
        for first in range(0,m,self.batch_rows):
            check()
            block=J[first:first+self.batch_rows]
            # No full-size squared-J temporary; hypot also avoids squaring
            # the accumulated norm outside this one small block.
            norms=np.hypot(norms,np.linalg.norm(block,axis=0))
            COUNTS["column_norm_rows"]+=len(block)
        if not np.all(np.isfinite(norms)):
            raise ArithmeticError("nonfinite complete column norm")
        self.column_norms=norms
        self.scales=np.maximum(norms,1e-12)
        reduced=None
        for first in range(0,m,self.batch_rows):
            check()
            last=min(m,first+self.batch_rows)
            previous=0 if reduced is None else reduced.shape[0]
            augmented=np.empty((previous+last-first,n+1))
            if previous:
                augmented[:previous]=reduced
            augmented[previous:,:n]=J[first:last]/self.scales
            augmented[previous:,n]=residual[first:last]
            reduced=np.linalg.qr(augmented,mode="r")
            COUNTS["complete_row_QR_blocks"]+=1
            COUNTS["new_original_rows_reduced"]+=last-first
            COUNTS["including_previous_R_rows_processed"]+=len(augmented)
        check()
        if reduced.shape!=(n+1,n+1) or not np.all(np.isfinite(reduced)):
            raise ArithmeticError("invalid full augmented QR factor")
        self.R=reduced[:n,:n].copy()
        self.c=reduced[:n,n].copy()
        self.orthogonal_residual_norm=abs(float(reduced[n,n]))
        self.U,self.s,self.Vt=np.linalg.svd(self.R,full_matrices=False)
        self.Utc=self.U.T@self.c
        self.scaled_gradient_inf=float(np.max(abs(self.R.T@self.c)))
        self.original_residual_norm=float(np.linalg.norm(residual))
        self.reduced_residual_norm=float(np.hypot(np.linalg.norm(self.c),
                                                 self.orthogonal_residual_norm))
        self.threshold=max(m,n)*np.finfo(float).eps*self.s[0]
        if not np.all(np.isfinite(self.s)):
            raise ArithmeticError("nonfinite complete small-factor spectrum")
        COUNTS["small_factor_SVDs"]+=1
        COUNTS["complete_J_factorizations"]+=1
        COUNTS["original_J_entries_consumed"]+=m*n

    def direction(self,damping):
        if not np.isfinite(damping) or damping<=0:
            raise ValueError("strictly positive declared damping required")
        COUNTS["complete_singular_direction_solves"]+=1
        return -(self.Vt.T@(self.s/(self.s*self.s+damping)*self.Utc))/self.scales

    def predicted_decrease(self,direction,fraction=1.):
        # The orthogonal residual cancels exactly in the model decrease.
        # This is the full-row quadratic form, evaluated without J@d or
        # subtraction of two large full residual norms.
        value=self.R@(self.scales*np.asarray(direction)*fraction)
        return float(-self.c@value-.5*(value@value))

    def spectrum(self):
        return {"singular_max":float(self.s[0]),"singular_min":float(self.s[-1]),
            "reported_rank":int(np.sum(self.s>self.threshold)),
            "rank_threshold":float(self.threshold),
            "column_norm_min":float(np.min(self.column_norms)),
            "column_norm_max":float(np.max(self.column_norms)),
            "columns_below_scale_floor":int(np.sum(self.column_norms<1e-12)),
            "scaled_gradient_inf":self.scaled_gradient_inf,
            "actual_output_rows":self.shape[0],"actual_columns":self.shape[1],
            "QR_batch_rows":self.batch_rows,
            "original_residual_norm":self.original_residual_norm,
            "reduced_residual_norm":self.reduced_residual_norm,
            "orthogonal_residual_norm":self.orthogonal_residual_norm,
            "full_augmented_rows_retained":True,
            "all_singular_directions_retained":True,
            "no_full_left_singular_matrix_formed":True,
            "normal_equations_not_formed":True,
            "floating_factorization_not_a_rigorous_inverse_certificate":True}
