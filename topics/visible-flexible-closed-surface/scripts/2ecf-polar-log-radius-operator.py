#!/usr/bin/env python3
"""Complete Cartesian plus log-radius design derivative and physical normal.

X=X_source+W_z is independent of alpha; a=a_base*exp(B alpha).
All original 13 rows and q=2 area rows remain. The finite weights, physical
nodes, point guides and increment H2 form are explicitly independent of
alpha. This is metric DESIGN, never same-g continuation while alpha moves.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import gc
import importlib.util
from pathlib import Path
import sys
import time
import types
import numpy as np
from scipy.linalg import cholesky_banded
from scipy.linalg.blas import dtbsv


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    sys.modules[name] = out
    spec.loader.exec_module(out)
    return out


def dependencies(scripts):
    names = dict(joint="6a65-geometry-gap-window-two-grid-cartesian.py",
        area="6a65-geometry-area-ratio-power-two.py",
        normal="6a65-cartesian-complete-radial-normal-two-grid-area.py")
    return {key:module(scripts/name, "log_radius_"+key) for key,name in names.items()}


class ArrayCache:
    """Declared exact finite source subset, for the small derivative audit."""
    def __init__(self, nodes, angles, jets, radius):
        self.nodes, self.u = np.asarray(nodes), np.asarray(angles)
        self.jets, self.radius = np.asarray(jets), np.asarray(radius)

    def __call__(self, nodes, angles):
        index = np.searchsorted(self.nodes, nodes)
        if (angles != len(self.u) or np.any(index >= len(self.nodes))
                or not np.array_equal(self.nodes[index], nodes)):
            raise ValueError("Only actual declared source samples may be consumed")
        return self.jets[index], np.broadcast_to(self.radius[index, 0, None], (len(index), angles))


class LogRadiusCache(ArrayCache):
    """The complete base position remains literal; only the target g changes."""
    def __init__(self, basis, parent, alpha):
        alpha = np.asarray(alpha, float)
        if alpha.shape != (basis.nb,) or not np.all(np.isfinite(alpha)):
            raise ValueError("Every declared finite log-radius coefficient is required")
        self.parent, self.basis, self.alpha = parent, basis, alpha.copy()
        self.matrices = basis.matrices(parent.nodes)
        h, hs, hss = (matrix@alpha for matrix in self.matrices)
        exp = np.exp(h)
        a, first, second = parent.radius.T
        radius = np.column_stack((a*exp, (first+a*hs)*exp,
            (second+2*first*hs+a*(hss+hs*hs))*exp))
        if not np.all(np.isfinite(radius)) or np.any(radius[:, 0] <= 0):
            raise ArithmeticError("Finite strictly positive actual designed radius required")
        self.log_values = h
        super().__init__(parent.nodes, parent.u, parent.jets, radius)


def radius_columns(point, area_packet, metric_weights, strength, target):
    """Derivative of all weighted point rows with respect to log(a)."""
    base = np.zeros_like(point.metric)
    base[..., 1] = -point.metric[..., 1]
    base[..., 2] = -2*(point.metric[..., 2]+1)
    column13 = np.zeros_like(point.residual)
    # Retain the full quartic amplification derivative, including cross terms
    # into the E residual. Only the three raw Gram coordinates have simple
    # radius derivatives; the final weighted rows do not.
    column13[..., :3] = point.sqrt_weights["metric"][..., None]*point.metric_apply(base)
    sigma = area_packet.sigma
    root = np.sqrt(strength*metric_weights)
    area_column = np.where(sigma < target, 2*root*(target/sigma)**2, 0.)
    if not np.all(np.isfinite(column13)) or not np.all(np.isfinite(area_column)):
        raise ArithmeticError("Nonfinite complete designed-radius derivative")
    return column13, area_column


class FullDesignLinear:
    def __init__(self, deps, stream, basis, source_caches, weights, z, alpha, config, recipe, area):
        self.deps, self.stream, self.basis = deps, stream, basis
        self.weights, self.recipe, self.config, self.area_definition = weights, recipe, config, area
        self.z, self.alpha = np.asarray(z, float), np.asarray(alpha, float)
        self.caches = {key:LogRadiusCache(basis, cache, alpha) for key,cache in source_caches.items()}
        self.position = deps["area"].CompleteAreaTwoGrid(deps["joint"], stream, basis,
            self.caches, weights, self.z, config, recipe, area)
        self.proxy = types.SimpleNamespace(linear=self.position)
        self.residual, self.statistics = self.position.residual, self.position.statistics
        self.group_values = self.position.group_values
        self.columns_per_radial_row = basis.na+1
        self.shape = (len(self.residual), basis.nb*self.columns_per_radial_row)
        self.radius_packets = {}
        for name in self.position.names:
            original = self.position.parent.groups[name]
            packets = []
            for index,sl in enumerate(original.slices):
                part = original._get_block(index, sl)
                area_packet = self.position.groups[name].packets[index]
                packets.append(radius_columns(part, area_packet,
                    np.asarray(weights[name]["metric"])[sl,None]/original.N,
                    area["strength"], area["targetAreaRatio"]))
            self.radius_packets[name] = packets

    def pack(self, z, alpha):
        return np.column_stack((np.asarray(z).reshape(self.basis.nb,self.basis.na),
            np.asarray(alpha).reshape(self.basis.nb))).ravel()

    def split(self, vector):
        value = np.asarray(vector, float).reshape(self.basis.nb, self.columns_per_radial_row)
        return value[:, :self.basis.na], value[:, self.basis.na]

    def matvec(self, vector):
        dz, da = self.split(vector)
        result = self.deps["normal"].SameSobolevAreaFullBandAugmented.raw_matvec(self.proxy, dz)
        for grid,name in enumerate(self.position.names):
            original = self.position.parent.groups[name]
            begin,end = self.position.parent.boundaries[grid:grid+2]
            out = result[begin:end].reshape(len(original.nodes), original.N, 13)
            begin,end = self.position.boundaries[grid+1:grid+3]
            outarea = result[begin:end].reshape(len(original.nodes), original.N)
            for sl,(k13,ka) in zip(original.slices,self.radius_packets[name]):
                change = original.matrices[0][sl]@da
                out[sl] += k13*change[:,None,None]
                outarea[sl] += ka*change[:,None]
        return result

    def transpose(self, vector):
        vector = np.asarray(vector, float)
        if vector.shape != (self.shape[0],):
            raise ValueError("All full original13 and q2 cotangent rows required")
        z = self.deps["normal"].SameSobolevAreaFullBandAugmented.raw_transpose(self.proxy, vector)
        alpha = np.zeros(self.basis.nb)
        for grid,name in enumerate(self.position.names):
            original = self.position.parent.groups[name]
            begin,end = self.position.parent.boundaries[grid:grid+2]
            cot = vector[begin:end].reshape(len(original.nodes), original.N, 13)
            begin,end = self.position.boundaries[grid+1:grid+3]
            cotarea = vector[begin:end].reshape(len(original.nodes), original.N)
            for sl,(k13,ka) in zip(original.slices,self.radius_packets[name]):
                alpha += original.matrices[0][sl].T@(
                    np.sum(k13*cot[sl],axis=(1,2))+np.sum(ka*cotarea[sl],axis=1))
        return self.pack(z, alpha)

    def sobolev_apply(self, vector):
        z, alpha = self.split(vector)
        normal = self.deps["normal"]
        out = np.empty_like(z)
        for lower,upper,columns in self.position.preconditioner.factors.values():
            out[:,columns] = normal.triangular_apply(lower,
                normal.triangular_apply(lower,z[:,columns],True),False)
        lower = self.position.preconditioner.factors[0][0]
        aout = normal.triangular_apply(lower,
            normal.triangular_apply(lower,alpha[:,None],True),False)[:,0]
        return self.pack(out,aout)

    def cross_normal(self):
        """Complete J_X^T J_alpha and J_alpha^T J_alpha, with no row dropping."""
        basis = self.basis
        cross = np.zeros((basis.dimension,basis.nb))
        gram = np.zeros((basis.nb,basis.nb))
        for name in self.position.names:
            original = self.position.parent.groups[name]
            for index,(sl,(k13,ka)) in enumerate(zip(original.slices,self.radius_packets[name])):
                part = original._get_block(index, sl)
                area = self.position.groups[name].packets[index]
                packet = part.vjp(k13)
                packet[:,:,1] += area.gs*ka[...,None]
                packet[:,:,2] += area.gu*ka[...,None]
                angular = (
                    basis.angular_adjoint(packet[:,:,0])+basis.angular_adjoint(packet[:,:,2],1)
                        +basis.angular_adjoint(packet[:,:,5],2),
                    basis.angular_adjoint(packet[:,:,1])+basis.angular_adjoint(packet[:,:,4],1),
                    basis.angular_adjoint(packet[:,:,3]))
                B = np.stack([b[sl].toarray() for b in original.matrices])
                square = np.sum(k13*k13,axis=(1,2))+np.sum(ka*ka,axis=1)
                for row in range(B.shape[1]):
                    active = np.flatnonzero(np.any(B[:,row] != 0.,axis=0))
                    if not len(active):
                        continue
                    if len(active)>6 or np.any(np.diff(active)!=1):
                        raise ArithmeticError("Full local quintic support structure changed")
                    gradient = sum((B[d,row,active,None]*angular[d][row,None,:]
                        for d in range(3)),np.zeros((len(active),basis.na)))
                    columns = (active[:,None]*basis.na+np.arange(basis.na)[None,:]).ravel()
                    local = gradient[:,:,None]*B[0,row,active][None,None,:]
                    cross[columns[:,None],active[None,:]] += local.reshape(len(columns),len(active))
                    gram[active[:,None],active[None,:]] += square[row]*np.outer(B[0,row,active],B[0,row,active])
        return cross,gram


class FullDesignNormal:
    def __init__(self, linear, damping):
        start = time.monotonic()
        self.linear, self.damping = linear, float(damping)
        if not np.isfinite(damping) or damping<=0:
            raise ValueError("Positive explicit joint design LM damping required")
        basis,normal = linear.basis,linear.deps["normal"]
        old = normal.CompleteAreaRadialNormal(linear.position,eta=damping)
        old_receipt = old.receipt
        nc,na,nb = linear.columns_per_radial_row,basis.na,basis.nb
        self.dimension = nb*nc
        self.half_bandwidth = min(6*nc-1,self.dimension-1)
        band = np.zeros((self.half_bandwidth+1,self.dimension))
        for offset in range(old.half_bandwidth+1):
            columns = np.arange(basis.dimension-offset)
            rows = columns+offset
            newcolumns = columns+columns//na
            newdistance = offset+rows//na-columns//na
            band[newdistance,newcolumns] = old.normal_band[offset,:len(columns)]
        for lower,channels in old.old_groups:
            oldband = normal.lower_product_band(lower)
            for offset in range(min(6,nb)):
                count = nb-offset
                columns = (np.arange(count)[:,None]*nc+channels[None,:]).ravel()
                band[offset*nc,columns] += damping*np.broadcast_to(
                    oldband[offset,:count,None],(count,len(channels))).ravel()
        del old
        gc.collect()
        cross,gram = linear.cross_normal()
        ii,jj = np.nonzero(cross)
        ci,ai = ii+ii//na,jj*nc+na
        rows,columns = np.maximum(ci,ai),np.minimum(ci,ai)
        distance = rows-columns
        if np.any(distance>self.half_bandwidth):
            raise ArithmeticError("Nonlocal Cartesian-radius covariance was omitted")
        band[distance,columns] += cross[ii,jj]
        radius_S = normal.lower_product_band(linear.position.preconditioner.factors[0][0])
        for offset in range(min(6,nb)):
            columns = np.arange(nb-offset)*nc+na
            band[offset*nc,columns] += np.diag(gram,k=-offset)+damping*radius_S[offset,:nb-offset]
        exterior = np.abs(np.arange(nb)[:,None]-np.arange(nb)[None,:])>5
        if np.any(gram[exterior] != 0.):
            raise ArithmeticError("Nonlocal radius covariance was omitted")
        self.unscaled_band = band.copy()
        diagonal = band[0]
        if np.any(diagonal<=0) or not np.all(np.isfinite(band)):
            raise ArithmeticError("The full physical joint normal is not finite positive diagonal")
        self.scale = 1/np.sqrt(diagonal)
        for offset in range(self.half_bandwidth+1):
            count = self.dimension-offset
            band[offset,:count] *= self.scale[offset:]*self.scale[:count]
        self.factor = cholesky_banded(band,lower=True,check_finite=True)
        self.receipt = dict(schema="2ecf-full-Cartesian-plus-log-radius-physical-normal-v1",
            actualRows=linear.shape[0], actualColumns=self.dimension,
            CartesianColumns=basis.dimension, logRadiusColumns=nb,
            CartesianRadiusCrossBlockFrobenius=float(np.linalg.norm(cross)),
            radiusNormalFrobenius=float(np.linalg.norm(gram)),
            fullOriginalCartesianAssembly=old_receipt,
            allOriginal13AndQ2RowsRetained=True, allCartesianRadiusCrossTermsRetained=True,
            metricQuarticAmplificationDerivativeIncluded=True,
            sameFixedWeightsNoParameterDerivativeRequired=True,
            targetMetricChangesWithAlpha=True, sameMetricConvergenceClaim=False,
            scalarHalfBandwidth=self.half_bandwidth,
            damping=damping, radiusIncrementSobolev="same physical k=0 radial H2 form",
            absoluteFieldPenaltyAdded=False, seconds=time.monotonic()-start)

    def solve(self, gradient):
        y = dtbsv(self.half_bandwidth,self.factor,self.scale*np.asarray(gradient),lower=1,trans=0)
        return self.scale*dtbsv(self.half_bandwidth,self.factor,y,lower=1,trans=1)

    def physical_normal(self, vector):
        return self.linear.transpose(self.linear.matvec(vector))+self.damping*self.linear.sobolev_apply(vector)

    def residual(self, direction):
        return self.physical_normal(direction)+self.linear.transpose(self.linear.residual)
