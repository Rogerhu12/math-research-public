#!/usr/bin/env python3
"""Exact continuous finite core references from the paid local input arrays.

The saved dyadic transfer centers are used as the exact joining matrices.
A finite affine correction of each rational local reference makes its two
endpoints exactly I and that saved center. Hence all radial joins are
mathematically continuous, without a floating-point jump convention.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb_mat
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_core_cell_flow import exact_matrix,identity
from fourfold_phase_core_flow_collect import validate,norm,read,sub

def zeros(rows,cols):return acb_mat(rows,cols)

class ExactCoreReference:
    def __init__(self,cover_root):
        self.cover_root=Path(cover_root)
        self.identity,self.local,self.manifests,self.leaves=validate(
            sorted(self.cover_root.glob('block_*/manifest.json')))
        self.N=self.identity['modes'];self.n=2*self.N+1;self.dimension=2*self.n
        self.scale=exact_arb(Fraction(self.identity['momentum_scale']))
        self.J=identity(self.dimension)
        for j in range(self.n,self.dimension):self.J[j,j]=-1
        self.prefix=[identity(self.dimension)]
        for transfer,error,metadata in self.local:
            self.prefix.append(transfer*self.prefix[-1])
        P=self.prefix[-1];n=self.n
        # The first n rows of J P J are P_height J.
        H=acb_mat(self.dimension,self.dimension)
        for i in range(n):
            for j in range(self.dimension):
                H[i,j]=P[i,j] if j<n else -P[i,j]
                H[n+i,j]=P[i,j]
        self.boundary_height_map=H
        self.boundary_to_waist=H.inv()
        self.boundary_to_waist_norm=norm(self.boundary_to_waist)
        self._cached_index=None;self._cached_reference=None

    def _local_reference(self,index):
        if self._cached_index==index:return self._cached_reference
        leaf=self.leaves[index];path=Path(leaf['arrays']['path'])
        with np.load(path,allow_pickle=False) as saved:
            raw=np.array(saved['exact_dyadic_generator_coefficients'],copy=True)
            center=exact_matrix(saved['exact_dyadic_local_transfer_center'])
        left,right=map(Fraction,leaf['exact_interval'])
        h=exact_arb((right-left)/2)
        polynomial=[exact_matrix(row) for row in raw]
        q=self.identity['flow_degree'];m=len(polynomial);d=self.dimension
        Z=[identity(d)]
        for k in range(q):
            value=zeros(d,d)
            for j in range(min(k,m-1)+1):value+=polynomial[j]*Z[k-j]
            Z.append(h*value/(k+1))
        minus=zeros(d,d);plus=zeros(d,d)
        for k,value in enumerate(Z):
            plus+=value;minus+=value if k%2==0 else -value
        inverse=minus.inv()
        R=[value*inverse for value in Z]
        # D is an exact rational expression. Its construction proves the
        # endpoint identities, even if evaluated interval sums have radii.
        correction=center-plus*inverse
        R[0]+=correction/2;R[1]+=correction/2
        result=dict(interval=(left,right),halfwidth=h,coefficients=R,
            endpoint_correction=correction,
            exact_definition='R(u)=Z(u)Z(-1)^{-1}+(u+1)(T_saved-Z(1)Z(-1)^{-1})/2')
        self._cached_index=index;self._cached_reference=result
        return result

    def coefficients(self,index,side=1):
        """Full physical (w,p) columns for endpoint heights, in positive u.

        side=-1 describes r=-s on the reflected negative interval. Both
        sides use u=(s-c)/h. Thus physical radial differentiation includes
        the factor side/h. The actual geometry coefficients on the negative
        side must use their exact radial parity, not unproved extrapolation.
        """
        if side not in (-1,1):raise ValueError('side must be exactly -1 or +1')
        local=self._local_reference(index)
        prior=self.prefix[index]
        if side==1:
            right=self.boundary_to_waist
            left=identity(self.dimension)
        else:
            right=self.J*self.boundary_to_waist
            left=self.J
        states=[left*value*prior*right for value in local['coefficients']]
        # Stored state had p/scale; return the physical raw flux p.
        for value in states:
            for i in range(self.n,self.dimension):
                for j in range(self.dimension):value[i,j]*=self.scale
        radial=[]
        for k in range(1,len(states)):
            radial.append((side*k/local['halfwidth'])*states[k])
        radial.append(zeros(self.dimension,self.dimension))
        actual_interval=local['interval'] if side==1 else tuple(-x for x in reversed(local['interval']))
        return dict(exact_physical_interval=list(map(str,actual_interval)),
            positive_parameter_interval=list(map(str,local['interval'])),
            radial_orientation=side,
            physical_state_coefficients=states,
            physical_radial_derivative_coefficients=radial,
            positive_halfwidth=local['halfwidth'],
            endpoint_selection_correction_norm=norm(local['endpoint_correction']),
            exact_endpoint_height_map=True,
            exact_continuity_at_all_radial_joins=True)

    def endpoint_raw_flux(self):
        """Exact finite reference DN, not the actual finite or infinite DN."""
        n=self.n;P=self.prefix[-1]
        positive=P*self.boundary_to_waist
        negative=self.J*P*self.J*self.boundary_to_waist
        out=zeros(self.dimension,self.dimension)
        for i in range(n):
            for j in range(self.dimension):
                out[i,j]=-self.scale*negative[n+i,j]
                out[n+i,j]=self.scale*positive[n+i,j]
        return out

def evaluate(coefficients,u):
    value=acb_mat(coefficients[0].nrows(),coefficients[0].ncols())
    for row in reversed(coefficients):value=value*u+row
    return value
