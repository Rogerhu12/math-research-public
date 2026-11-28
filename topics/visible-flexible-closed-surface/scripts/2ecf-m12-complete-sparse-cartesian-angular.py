#!/usr/bin/env python3
"""M12 coupled-planar/cosine-height full angular Gram via sparse Cartesian slots.

Exact distributivity replaces contraction over structurally zero Cartesian
coefficients. All signed Fourier terms, Cartesian cross terms and discrete
aliases remain. Floating summation grouping changes and must be audited.
"""
import numpy as np

def contract(spectrum,frequency,coefficient,N):
 spectrum=np.asarray(spectrum);frequency=np.asarray(frequency);coefficient=np.asarray(coefficient)
 nc=frequency.shape[1];nr=spectrum.shape[0]
 if spectrum.shape!=(nr,N//2+1,2,3,2,3) or frequency.shape!=(2,nc) or coefficient.shape!=(2,nc,3):raise ValueError('Complete actual M12 two-first-jet Cartesian spectrum required')
 Q=np.zeros((nr,nc,nc,2,2),complex);aliases=0;peak=Q.nbytes
 for left in range(2):
  fa=frequency[left]
  for right in range(2):
   fb=frequency[right];freq=fa[:,None]+fb[None,:];wrapped=np.mod(freq,N)
   index=np.minimum(wrapped,N-wrapped);conjugate=wrapped<=N//2
   za0=coefficient[left]*(1j*fa[:,None]);zb0=coefficient[right]*(1j*fb[:,None])
   live=np.any(za0!=0,axis=1)[:,None]&np.any(zb0!=0,axis=1)[None,:]
   aliases+=int(np.count_nonzero((abs(freq)>N//2)&live))
   for d,da in enumerate((1,0)):
    za=coefficient[left]*(1j*fa[:,None])**da
    for e,db in enumerate((1,0)):
     zb=coefficient[right]*(1j*fb[:,None])**db
     for ca in range(3):
      ia=np.flatnonzero(za[:,ca])
      if not len(ia):continue
      for cb in range(3):
       ib=np.flatnonzero(zb[:,cb])
       if not len(ib):continue
       ids=index[ia[:,None],ib[None,:]];sign=conjugate[ia[:,None],ib[None,:]]
       values=spectrum[:,:,d,ca,e,cb][:,ids]
       moment=np.where(sign[None],values.conj(),values)
       term=moment*za[ia,ca][None,:,None];term*=zb[ib,cb][None,None,:]
       Q[:,ia[:,None],ib[None,:],d,e]+=term
       peak=max(peak,Q.nbytes+freq.nbytes+wrapped.nbytes+index.nbytes+conjugate.nbytes+values.nbytes+moment.nbytes+term.nbytes)
 return Q,{'all_original_cartesian_cross_terms_and_signed_slots':True,'structural_zero_coefficients_only_omitted':True,
   'discrete_alias_frequency_pairs':aliases,'largest_explicit_kernel_bytes':peak,'floating_sum_grouping_changed':True}
