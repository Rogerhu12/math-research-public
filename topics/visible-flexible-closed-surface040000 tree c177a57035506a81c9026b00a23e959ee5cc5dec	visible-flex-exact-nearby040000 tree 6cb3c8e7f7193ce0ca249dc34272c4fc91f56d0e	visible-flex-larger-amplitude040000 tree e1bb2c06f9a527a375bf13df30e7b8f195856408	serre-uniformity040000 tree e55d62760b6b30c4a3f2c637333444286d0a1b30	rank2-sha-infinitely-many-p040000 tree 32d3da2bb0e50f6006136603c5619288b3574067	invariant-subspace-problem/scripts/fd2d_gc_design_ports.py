#!/usr/bin/env python3
"""Exact first-order curvature column of a selected finite linear tail.

This is deliberately a LINEAR initializer. The actual nonlinear tail is
later consumed through TailGCJetPort, not inferred from these columns.
The parameter is the old worker's physical height h=-g on the upper half.
"""
import numpy as np
from fd2d_gc_intrinsic import LD


class LinearCurvatureTail:
    def __init__(self,flow,report):
        self.flow,self.M=flow,flow.K
        rows={int(row['mode']):row for row in report['rows']}
        self.frequencies=2*np.arange(1,self.M+1,dtype=LD)
        self.D=np.array([rows[int(k)]['slope'] for k in self.frequencies],dtype=LD)
        a,v,app=flow.profile(flow.candidate.end)
        self.r,self.v,self.app=LD(a[0]),LD(v[0]),LD(app[0])
        self.nr=np.sqrt(1-self.v*self.v)/self.r
        self.n_column=(self.frequencies**2-self.r*self.D)/(self.r*self.r*self.v)
        self.m_column=self.frequencies*(self.r*self.D-1)/(self.r*self.r)
        self.u=np.asarray(flow.coordinates(flow.candidate.end)['u'][:,0],dtype=LD)
        self.N=np.cos(self.u[:,None]*self.frequencies)*self.n_column
        self.Mat=np.sin(self.u[:,None]*self.frequencies)*self.m_column
        self.height_scale=np.asarray(abs(self.v)*self.r*self.r/(self.frequencies**2+abs(self.r*self.D)),dtype=float)
        self.scope='Finite LINEAR tail curvature graph at the actual frozen cut; nonlinear tail not solved.'
        self._height=self._values=self._jacobian=None

    def evaluate(self,height,jacobian=False):
        height=np.asarray(height,dtype=float)
        if self._height is None or not np.array_equal(height,self._height):
            dn=self.N@np.asarray(height,dtype=LD);m=self.Mat@np.asarray(height,dtype=LD);n=self.nr+dn
            if np.any(n<=0):raise FloatingPointError('Linear tail initializer left the positive n chart')
            native=np.column_stack((np.log1p(dn/self.nr),m/self.nr))
            self._values=self.flow.encode(native);self._height=height.copy();self._jacobian=None
            self.n,self.m=n,m
        if jacobian and self._jacobian is None:
            point=np.stack((self.N/self.n[:,None],self.Mat/self.nr),axis=1)
            self._jacobian=self.flow.encode(point)
        return self._values,self._jacobian if jacobian else None

    def diagnostics(self):
        return dict(scope=self.scope,minimum_n=float(self.n.min()),
                    maximum_m=float(abs(self.m).max()),nonlinear_tail_solved=False,
                    height_to_curvature='worker h=-g; dn=(k^2-rD)/(r^2*v)*h*cos(k*u), dm=k*(rD-1)/r^2*h*sin(k*u)')
