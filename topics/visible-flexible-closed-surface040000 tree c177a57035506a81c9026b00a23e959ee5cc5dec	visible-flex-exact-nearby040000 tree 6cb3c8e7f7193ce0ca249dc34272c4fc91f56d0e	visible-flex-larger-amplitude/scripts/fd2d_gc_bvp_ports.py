#!/usr/bin/env python3
"""Explicitly labelled tail starters and actual-jet adapters for GC BVPs.

FiniteLinearTailStarter supplies only a finite LINEAR selected tail graph.
Applying the nonlinear Hessian-to-II formula to those jets does not make it
a nonlinear DN response.  Every consumer must retain this scope and replace
the starter with genuine nonlinear responses before claiming tail matching.
"""
from __future__ import annotations
import numpy as np
from fd2d_metric_tail_gc_port import TailGCJetPort


class FiniteLinearTailStarter:
    def __init__(self, report, modes):
        if report.get('completed') is False:
            raise ValueError('The selected linear graph is incomplete')
        self.M = int(modes)
        self.spacing = int(report.get('spacing', report.get('config', {}).get('spacing', 2)))
        rows = {int(row['mode']): row for row in report['rows']}
        self.frequency = self.spacing*np.arange(1, self.M+1, dtype=float)
        self.D = np.array([rows[int(k)]['slope'] for k in self.frequency])
        cut = report['cut']
        self.r, self.w, self.wr = float(cut['r']), float(cut['w']), float(cut['wr'])
        self.E = 1+self.w*self.w
        self.Ep = 2*self.w*self.wr
        self.D2 = -(self.wr/self.w)*(self.D-self.frequency**2/self.r)
        self.J = np.zeros((3*self.M+2, self.M))
        self.J[np.arange(self.M), np.arange(self.M)] = self.D
        self.J[self.M+np.arange(self.M), np.arange(self.M)] = self.D2
        self.J[2*self.M+2+np.arange(self.M), np.arange(self.M)] = 1
        self.height_scale = abs(-1/np.sqrt(self.E))*self.r*self.r/(self.frequency**2+abs(self.r*self.D))
        self.scope = 'Finite linear selected graph, initializer only; no actual nonlinear tail solve.'
        self.nonlinear = False

    def packet(self, worker_height):
        h = np.asarray(worker_height, dtype=float)
        if h.shape != (self.M,):
            raise ValueError('Incorrect physical worker-height dimension')
        jets = dict(radius=self.r, E=self.E, Ep=self.Ep,
                    backgroundSlope=self.w, backgroundSecond=self.wr,
                    height=h.tolist(), slope=(self.D*h).tolist(), second=(self.D2*h).tolist(),
                    meanSlope=self.w, meanSecond=self.wr,
                    meanSlopeCorrection=0., meanSecondCorrection=0.)
        return dict(jets=jets, heightJetJacobian=self.J.ravel().tolist(),
                    config=dict(spacing=self.spacing, modes=self.M), scope=self.scope,
                    nonlinear_tail_solved=False)

    def port(self, worker_height, target_jet=None):
        packet = self.packet(worker_height)
        return TailGCJetPort(packet['jets'], spacing=self.spacing,
                             height_jacobian=packet['heightJetJacobian'], target_jet=target_jet)


class ProjectedTailPort:
    """Compose scalar II fields with the SAME material angle at the cut."""
    def __init__(self, flow, provider):
        self.flow, self.provider = flow, provider
        self.M = provider.M
        self.scope = provider.scope
        self.height_scale = provider.height_scale
        self.cached_height = self.cached_values = self.cached_jacobian = self.cached_diagnostics = None

    def material_coordinate(self):
        if hasattr(self.flow, 'coordinates'):
            return np.asarray(self.flow.coordinates(self.flow.candidate.end)['u']).reshape(self.flow.work)
        return self.flow.u

    def evaluate(self, height, jacobian=False):
        height = np.asarray(height, dtype=float)
        if self.cached_height is None or not np.array_equal(self.cached_height, height):
            aa, ap, app = self.flow.profile(self.flow.candidate.end)
            port = self.provider.port(height, target_jet=(aa[0], ap[0], app[0]))
            material = self.material_coordinate()
            values = port.evaluate(material)
            nm = np.column_stack((values['n'], values['m']))
            projected = self.flow.encode(nm)
            self.cached_height, self.cached_values = height.copy(), projected
            self.cached_jacobian = None
            self.cached_port = port
            self.cached_diagnostics = dict(scope=self.scope,
                minimum_n=float(np.min(values['n'])), minimum_vertical_normal_squared=float(np.min(values['normal_projection_squared'])),
                gauss_defect=float(np.max(abs(values['gauss_defect']))),
                Fourier_projection_maximum_difference=float(np.max(abs(self.flow.decode(projected)-nm))))
        if jacobian and self.cached_jacobian is None:
            material = self.material_coordinate()
            directions = []
            for k in range(self.M):
                direction = np.zeros(self.M)
                direction[k] = 1
                tangent = self.cached_port.jvp(material, direction)
                directions.append(self.flow.encode(np.column_stack((tangent['n'], tangent['m']))))
            self.cached_jacobian = np.column_stack(directions)
        return self.cached_values, self.cached_jacobian if jacobian else None, self.cached_diagnostics
