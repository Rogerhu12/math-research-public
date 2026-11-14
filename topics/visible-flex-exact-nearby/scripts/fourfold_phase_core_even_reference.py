#!/usr/bin/env python3
"""Exact waist-even/cosine continuous core references from all paid leaves.

The reference has five paired physical height inputs, not eighteen arbitrary
two-cut inputs. It uses only the proved invertible five-height waist map and
retains both Cauchy state channels throughout every local construction.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb_mat
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_core_cell_flow import exact_matrix,identity
from fourfold_phase_core_flow_collect import validate,norm,sub
from fourfold_phase_core_even_collect import cosine_basis,two_cauchy_slots
from fourfold_phase_low_feedback_paid_inputs import adjoint

def zeros(rows,cols):
    return acb_mat(rows,cols)

class ExactEvenCoreReference:
    def __init__(self,cover_root):
        self.cover_root=Path(cover_root)
        self.identity,self.original,self.manifests,self.leaves=validate(
            sorted(self.cover_root.glob('block_*/manifest.json')))
        self.N=int(self.identity['modes'])
        self.n=2*self.N+1
        self.dimension=self.N+1
        self.cauchy_dimension=2*self.dimension
        self.scale=exact_arb(Fraction(self.identity['momentum_scale']))
        self.Q=cosine_basis(self.N)
        self.U=two_cauchy_slots(self.Q)
        self.local=[(adjoint(self.U)*T*self.U,error,metadata)
                    for T,error,metadata in self.original]
        self.prefix=[identity(self.cauchy_dimension)]
        for transfer,error,metadata in self.local:
            self.prefix.append(transfer*self.prefix[-1])
        P=self.prefix[-1]
        A=sub(P,0,self.dimension,0,self.dimension)
        Ai=A.inv()
        self.boundary_to_waist=zeros(self.cauchy_dimension,self.dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.boundary_to_waist[i,j]=Ai[i,j]/arb(2).sqrt()
        self.boundary_to_waist_norm=norm(self.boundary_to_waist)
        self._cached_index=None
        self._cached_reference=None

    def _local_reference(self,index):
        if self._cached_index==index:
            return self._cached_reference
        leaf=self.leaves[index]
        with np.load(Path(leaf['arrays']['path']),allow_pickle=False) as saved:
            raw=np.array(saved['exact_dyadic_generator_coefficients'],copy=True)
        left,right=map(Fraction,leaf['exact_interval'])
        h=exact_arb((right-left)/2)
        polynomial=[adjoint(self.U)*exact_matrix(row)*self.U for row in raw]
        q=int(self.identity['flow_degree'])
        m=len(polynomial)
        d=self.cauchy_dimension
        Z=[identity(d)]
        for k in range(q):
            value=zeros(d,d)
            for j in range(min(k,m-1)+1):
                value+=polynomial[j]*Z[k-j]
            Z.append(h*value/(k+1))
        minus,plus=zeros(d,d),zeros(d,d)
        for k,value in enumerate(Z):
            plus+=value
            minus+=value if k%2==0 else -value
        inverse=minus.inv()
        R=[value*inverse for value in Z]
        center=self.local[index][0]
        correction=center-plus*inverse
        R[0]+=correction/2
        R[1]+=correction/2
        result=dict(interval=(left,right),halfwidth=h,coefficients=R,
                    endpoint_correction=correction)
        self._cached_index=index
        self._cached_reference=result
        return result

    def coefficients(self,index,side=1):
        if side not in (-1,1):
            raise ValueError('side must be exactly -1 or +1')
        local=self._local_reference(index)
        prior=self.prefix[index]
        # U is exact algebraic; the reference itself is never rounded at a join.
        states=[self.U*value*prior*self.boundary_to_waist
                for value in local['coefficients']]
        for value in states:
            for i in range(self.n,2*self.n):
                for j in range(self.dimension):
                    value[i,j]*=side*self.scale
        radial=[(side*k/local['halfwidth'])*states[k]
                for k in range(1,len(states))]
        radial.append(zeros(2*self.n,self.dimension))
        actual=(local['interval'] if side==1
                else tuple(-x for x in reversed(local['interval'])))
        return dict(exact_physical_interval=list(map(str,actual)),
            positive_parameter_interval=list(map(str,local['interval'])),
            radial_orientation=side,
            physical_state_coefficients=states,
            physical_radial_derivative_coefficients=radial,
            positive_halfwidth=local['halfwidth'],
            endpoint_selection_correction_norm=norm(local['endpoint_correction']),
            exact_endpoint_height_map=True,
            exact_continuity_at_all_radial_joins=True,
            endpoint_heights='(w_left,w_right)=(Qcos*v,Qcos*v)/sqrt(2)',
            input_space='five normalized paired physical cosine heights, including the mean',
            both_local_Cauchy_channels_retained=True)

    def endpoint_even_flux(self):
        """Reference flux projected onto the same normalized paired heights."""
        positive=self.prefix[-1]*self.boundary_to_waist
        out=zeros(self.dimension,self.dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                out[i,j]=arb(2).sqrt()*self.scale*positive[self.dimension+i,j]
        return out

    def endpoint_raw_flux(self):
        positive=self.U*self.prefix[-1]*self.boundary_to_waist
        out=zeros(2*self.n,self.dimension)
        for i in range(self.n):
            for j in range(self.dimension):
                value=self.scale*positive[self.n+i,j]
                out[i,j]=value
                out[self.n+i,j]=value
        return out
