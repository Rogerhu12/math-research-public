#!/usr/bin/env python3
"""The same full two-grid operator with point packets recomputed by block.

All source arrays remain literal memmaps. All original13/q2 rows, weights,
Fourier channels, physical S, and every normal covariance are unchanged.
Only the lifetime of derived PointLinearized packets changes.
"""
import numpy as np
from scipy.sparse.linalg import LinearOperator


def install(joint):
    original_class=joint.TwoGrid
    class StreamedTwoGrid(original_class):
        def __init__(self,stream,basis,caches,weights,coefficient,config,recipe):
            self.stream,self.basis=stream,basis
            self.names=('training','observer')
            allnodes=np.concatenate([caches[k].nodes for k in self.names])
            allweights=np.concatenate([weights[k]['metric'] for k in self.names])
            common=stream.BandedSobolev(basis,allnodes,allweights,recipe['preconditioner'])
            self.preconditioner=common;self.groups={}
            for key in self.names:
                g=stream.CompleteStreamingLinearized(basis,caches[key].nodes,weights[key],
                    caches[key],coefficient,len(caches[key].u),config,
                    block=recipe['radialBlock'],preconditioner=recipe['preconditioner'],
                    cache_point_blocks=False)
                g.preconditioner=common;self.groups[key]=g
            self.residual=np.concatenate([self.groups[k].residual for k in self.names])
            self.boundaries=np.cumsum([0]+[self.groups[k].shape[0] for k in self.names])
            self.shape=(len(self.residual),basis.dimension)
            self.operator=LinearOperator(self.shape,matvec=self.matvec,rmatvec=self.rmatvec,dtype=np.float64)
            self.group_values={k:self.groups[k].statistics for k in self.names}
            self.statistics=joint.combine(stream,self.group_values)
    joint.TwoGrid=StreamedTwoGrid
    return original_class
