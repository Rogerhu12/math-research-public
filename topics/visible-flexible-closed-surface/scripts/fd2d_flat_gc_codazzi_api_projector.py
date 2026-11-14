"""Fixed-parameter nearest Codazzi projection, recovered as text after executor loss.

This is the same finite linear construction used in the historical
25%/75% initialization experiment. It does not solve Gauss or alter
central, tail, physical-T or exact endpoint values.
"""
from __future__ import annotations
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu


class FixedCodazziProjector:
    def __init__(self, model, parameters, *, l_weight=.5,
                 preserve_before=None, preservation_multiplier=10.):
        self.model = model
        self.parameters = np.asarray(parameters, float).copy()
        self.T = float(self.parameters[-1])
        ops = model.operators(self.T)
        rr, cc, vv = [], [], []
        def block(row, col, value):
            ii,jj = np.nonzero(value)
            rr.extend((row+ii).tolist())
            cc.extend((col+jj).tolist())
            vv.extend(value[ii,jj].tolist())
        for j in range(model.N-1):
            block(j*model.d, j*model.q,
                  -model.select/model.h[j]-.5*ops['op'][j])
            block(j*model.d, (j+1)*model.q,
                  model.select/model.h[j]-.5*ops['op'][j+1])
        full = sparse.coo_matrix((vv,(rr,cc)),
            shape=((model.N-1)*model.d, model.N*model.q)).tocsr()
        self.free = np.arange(model.q, (model.N-1)*model.q)
        self.C = full[:,self.free].tocsc()
        radial = .5*np.r_[model.h[0],model.h[:-1]+model.h[1:],model.h[-1]]
        weights = np.ones((model.N-2,model.q))
        weights[:,model.d:] *= l_weight
        if preserve_before is not None:
            weights[model.x[1:-1]<=preserve_before] *= preservation_multiplier
        weights[:,0] *= np.sqrt(2.)
        weights[:,model.d] *= np.sqrt(2.)
        weights *= np.sqrt(radial[1:-1,None])
        self.inverse_weight = 1/weights.ravel()
        weighted = self.C@sparse.diags(self.inverse_weight)
        norms = np.sqrt(np.asarray(weighted.multiply(weighted).sum(axis=1)).ravel())
        self.row_scale = 1/norms
        self.A = sparse.diags(self.row_scale)@weighted
        normal = (self.A@self.A.T).tocsc()
        self.factor = splu(normal)
        self.definition = dict(
            physical_T=self.T, l_weight=float(l_weight),
            preserve_before=preserve_before,
            preservation_multiplier=float(preservation_multiplier),
            number_of_free_coefficients=len(self.free),
            number_of_equations=self.C.shape[0], C_nnz=int(self.C.nnz),
            normal_nnz=int(normal.nnz),
            lu_nnz=int(self.factor.L.nnz+self.factor.U.nnz),
            norm='radial L2 of real Fourier coefficients; constants sqrt(2); selected l weight',
            state_endpoints_fixed=True, all_parameters_fixed=True,
            gauss_not_solved=True)

    def direction(self, vector):
        y,p = self.model.unpack(vector)
        if not np.array_equal(p,self.parameters):
            raise ValueError('The projector binds fixed central/tail/T parameters')
        unused,data = self.model.evaluate(vector)
        cod = data['codazzi_cells'].ravel()
        multiplier = self.factor.solve(-self.row_scale*cod)
        delta = self.inverse_weight*np.asarray(self.A.T@multiplier).ravel()
        for unused in range(2):
            residual = cod+self.C@delta
            multiplier = self.factor.solve(-self.row_scale*residual)
            delta += self.inverse_weight*np.asarray(self.A.T@multiplier).ravel()
        return delta, dict(initial_codazzi_maximum=float(np.max(np.abs(cod))),
            full_linear_residual=float(np.max(np.abs(cod+self.C@delta))),
            correction_norm=float(np.linalg.norm(delta)))

    def project(self, vector, *, amount=1.):
        result = np.asarray(vector,float).copy()
        delta,diagnostic = self.direction(result)
        result[self.free] += float(amount)*delta
        diagnostic['amount'] = float(amount)
        return result,diagnostic
