#!/usr/bin/env python3
"""The same complete reciprocal cap-cut equations, batched by radial columns.

No angular Fourier coefficient, physical field, mean or parameter column is
removed. Only independent radial point evaluations are split into batches.
"""
from __future__ import annotations
import numpy as np
from fourfold_codazzi_reciprocal_cap_cut_system import ReciprocalCapCut


class ReciprocalCapCutBatched(ReciprocalCapCut):
    radial_batch=16

    def evaluate(self,r,y,p):
        r=np.atleast_1d(np.asarray(r,dtype=float));y=np.asarray(y,dtype=float)
        if y.ndim==1:y=y[:,None]
        if y.shape!=(2*self.modes+1,len(r)):raise ValueError('incomplete batched nonlinear state')
        out=np.empty_like(y)
        for start in range(0,len(r),self.radial_batch):
            stop=min(start+self.radial_batch,len(r))
            out[:,start:stop]=super().evaluate(r[start:stop],y[:,start:stop],p)
        return out

    def actual_fields(self,r,y,p):
        r=np.atleast_1d(np.asarray(r,dtype=float));y=np.asarray(y,dtype=float)
        if y.ndim==1:y=y[:,None]
        if y.shape!=(2*self.modes+1,len(r)):raise ValueError('incomplete batched physical state')
        B=np.empty((self.angular_grid,len(r)));C=np.empty_like(B)
        for start in range(0,len(r),self.radial_batch):
            stop=min(start+self.radial_batch,len(r))
            B[:,start:stop],C[:,start:stop]=super().actual_fields(r[start:stop],y[:,start:stop],p)
        return B,C
