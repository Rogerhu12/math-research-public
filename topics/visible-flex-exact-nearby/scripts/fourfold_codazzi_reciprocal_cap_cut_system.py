#!/usr/bin/env python3
"""Complete finite reciprocal system at the actual r=3/2 cap cut.

Every retained physical Robin row uses its own propagated q_(4j), and its
full quotient derivative and parameter column are retained. The actual
nonlinear cap remainder and mean correction are still separate obligations.
"""
from __future__ import annotations
from fractions import Fraction
import json
from pathlib import Path
import numpy as np
from fourfold_codazzi_reciprocal_polynomial_system import ReciprocalPolynomial
from fourfold_codazzi_reciprocal_candidate_tools import diagnostic as full_interior_diagnostic
from fourfold_phase_local_correction_probe import sha


class ReciprocalCapCut(ReciprocalPolynomial):
    def __init__(self,geometry,modes,angles,body,graft,*,q_path,mean_boundary='outer'):
        super().__init__(geometry,modes,angles,body,graft,mean_boundary=mean_boundary,right=1.5)
        self.q_path=Path(q_path);data=json.loads(self.q_path.read_text())
        if Fraction(str(data['left']))!=Fraction(3,2) or Fraction(str(data['right']))!=Fraction(25,8):
            raise ValueError('q vector must refer to the actual complete cap segment')
        frequencies=np.asarray(data['physical_frequencies'],dtype=int)
        values=np.asarray(data['q_values'],dtype=float)
        if len(values)<modes or len(values)!=len(frequencies) or not np.all(frequencies==4*np.arange(1,len(values)+1)):
            raise ValueError('a complete consecutively ordered physical q vector is required')
        if not np.all(np.isfinite(values)) or np.any(values<=0):raise ValueError('invalid propagated q vector')
        self.q_vector=values[:modes].copy();self.q_data=data
        bound=data.get('all_nonmean_q_abs_upper')
        self.q_tail_bound=None if bound is None else float(bound)
        if self.q_tail_bound is not None and self.q_tail_bound<np.max(self.q_vector):
            raise ValueError('the reported all-mode q bound does not cover its finite vector')

    def boundary(self,left,right,p):
        bl,cl,*_=self.boundary_jet(0.,left,p)
        br,cr,*_=self.boundary_jet(self.right_boundary,right,p)
        m=self.modes;mean=cl[0] if self.mean_boundary=='waist' else cr[0]
        return np.r_[left[:m],mean,cl[1]+1,br+self.q_vector*cr[1:]]

    def boundary_jac(self,left,right,p):
        bl,cl,jbl,jcl,pbl,pcl=self.boundary_jet(0.,left,p)
        br,cr,jbr,jcr,pbr,pcr=self.boundary_jet(self.right_boundary,right,p)
        m=self.modes;n=2*m+1;jl=np.zeros((n+1,n));jr=np.zeros_like(jl);jp=np.zeros((n+1,1))
        jl[np.arange(m),np.arange(m)]=1
        if self.mean_boundary=='waist':jl[m]=jcl[0];jp[m,0]=pcl[0]
        else:jr[m]=jcr[0];jp[m,0]=pcr[0]
        jl[m+1]=jcl[1];jp[m+1,0]=pcl[1]
        jr[m+2:]=jbr+self.q_vector[:,None]*jcr[1:]
        jp[m+2:,0]=pbr+self.q_vector*pcr[1:]
        return jl,jr,jp


def diagnostic(system,result):
    # All interior equations are the identical reciprocal polynomial system.
    # Replace every outer scalar-Robin diagnostic below by the actual vector.
    out=full_interior_diagnostic(system,result)
    if not out.get('valid'):return out
    m=system.modes;N=2*system.angular_grid
    fine=ReciprocalPolynomial(system.geometry,m,N,system.body,system.graft,
        mean_boundary=system.mean_boundary,right=system.right_boundary)
    fine.alpha=system.alpha;fine.all_base_cache=system.all_base_cache
    br,cr=fine.physical_normalized_fields([system.right_boundary],result.sol(system.right_boundary),result.p)
    fb=np.fft.fft(br[:,0])/N;fc=np.fft.fft(cr[:,0])/N
    signed=np.fft.fftfreq(N,1/N);indices=np.abs(signed).astype(int)
    retained=(indices>0)&(indices<=m);tail=indices>m
    robin=1j*np.sign(signed[retained])*fb[retained]+system.q_vector[indices[retained]-1]*fc[retained]
    boundary=out['full_physical_boundary']
    for name in ('normalized_all_sampled_nonmean_Robin_l1','normalized_retained_Robin_l1',
        'normalized_unretained_Robin_tail_l1','normalized_Robin_high_grid_tail_l1',
        'right_Robin_remains_the_stated_linear_reference'):
        boundary.pop(name,None)
    btail=float(np.sum(abs(fb[tail])));ctail=float(np.sum(abs(fc[tail])))
    tail_bound=None if system.q_tail_bound is None else btail+system.q_tail_bound*ctail
    boundary.update(actual_cap_cut='3/2',normalized_retained_mode_dependent_Robin_l1=float(np.sum(abs(robin))),
        normalized_unretained_physical_b_sampled_tail_l1=btail,
        normalized_unretained_physical_c_sampled_tail_l1=ctail,
        supplied_all_nonmean_q_abs_upper=system.q_tail_bound,
        normalized_unretained_mode_dependent_Robin_sampled_tail_upper=tail_bound,
        q_vector_source=str(system.q_path),q_vector_source_sha256=sha(system.q_path),
        actual_mode_dependent_linear_cap_rows=True,
        true_nonlinear_cap_nonmean_remainder_and_mean_correction_not_claimed=True,
        rational_boundary_tail_is_sampled_not_continuously_certified=True)
    return out
