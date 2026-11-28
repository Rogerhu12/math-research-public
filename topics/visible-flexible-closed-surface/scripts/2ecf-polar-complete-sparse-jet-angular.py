#!/usr/bin/env python3
"""Complete signed Fourier contraction using the six nonzero jet slots.

This rearranges only the angular algebra of the full weighted point Gram.
All 3x3 Cartesian, 6x6 jet, real Fourier +/- and discrete aliases remain.
It does not approximate the Gram, discard point rows, or change weights.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np


def contract(spectrum, channels, N):
    spectrum=np.asarray(spectrum)
    if spectrum.ndim!=6 or spectrum.shape[1:]!=(N//2+1,3,3,6,6):
        raise ValueError('Full actual Cartesian-by-jet rFFT Gram required')
    nc=len(channels);nr=spectrum.shape[0]
    components=np.array([c for c,k,kind in channels],int)
    frequency=np.zeros((2,nc),int);coefficient=np.zeros((2,nc),complex)
    for j,(component,k,kind) in enumerate(channels):
        if k==0:
            if kind!='cos':raise ValueError('Only cosine has a constant channel')
            coefficient[0,j]=1.
        elif k>0 and kind in ('cos','sin'):
            frequency[:,j]=(k,-k)
            coefficient[:,j]=(.5,.5) if kind=='cos' else (-.5j,.5j)
        else:raise ValueError('Every declared real periodic channel is required')
    # Each tuple is (jet slot, angular derivative order), per radial order.
    radial=(((0,0),(2,1),(5,2)),((1,0),(4,1)),((3,0),))
    Q=np.zeros((nr,nc,nc,3,3))
    maximag=maxreal=0.;aliases=0
    for ca in range(3):
        ia=np.flatnonzero(components==ca)
        for cb in range(3):
            ib=np.flatnonzero(components==cb)
            if not len(ia) or not len(ib):continue
            local=np.zeros((nr,len(ia),len(ib),3,3),complex)
            for sa in range(2):
                fa=frequency[sa,ia][:,None];za=coefficient[sa,ia][:,None]
                for sb in range(2):
                    fb=frequency[sb,ib][None,:];zb=coefficient[sb,ib][None,:]
                    weight=za*zb
                    if not np.any(weight):continue
                    freq=fa+fb;wrapped=np.mod(freq,N);index=np.minimum(wrapped,N-wrapped)
                    conjugate=wrapped<=N//2
                    aliases+=int(np.count_nonzero((abs(freq)>N//2)&(weight!=0)))
                    afactors=[(1j*fa)**k for k in range(3)]
                    bfactors=[(1j*fb)**k for k in range(3)]
                    for d,left in enumerate(radial):
                        for e,right in enumerate(radial):
                            for ji,pa in left:
                                for jj,pb in right:
                                    values=spectrum[:,:,ca,cb,ji,jj][:,index]
                                    positive=np.where(conjugate[None],values.conj(),values)
                                    local[:,:,:,d,e]+=positive*(weight*afactors[pa]*bfactors[pb])[None]
            maximag=max(maximag,float(np.max(abs(local.imag))))
            maxreal=max(maxreal,float(np.max(abs(local.real))))
            Q[:,ia[:,None],ib[None,:],:,:]=local.real
    return Q,dict(maximumImaginaryFinalContraction=maximag,maximumRealFinalContraction=maxreal,
        discreteAliasedFrequencyPairs=aliases,allSixJetSlotsAndCartesianCrossTermsRetained=True,
        allSignedRealFourierSlotsRetained=True)
