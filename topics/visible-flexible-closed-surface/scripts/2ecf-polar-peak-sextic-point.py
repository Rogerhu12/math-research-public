"""Augment the existing weighted metric loss by a positive sextic Frobenius term."""
import numpy as np


def install(stream,beta):
    base=stream.point.PointLinearized
    if not np.isfinite(beta) or beta<=0:
        raise ValueError("A positive finite sextic coefficient is required")

    class SexticPoint(base):
        def __init__(self,jets,target_radius,config,weights):
            super().__init__(jets,target_radius,config,weights)
            self.metric_q=np.einsum("...i,...i->...",self.metric,self.metric)/(config.metric_tau**2)
            self.metric_h=np.sqrt(1+self.metric_q+beta*self.metric_q**2)
            self.residual[...,:3]=(self.sqrt_weights["metric"]*self.metric_h)[...,None]*self.metric

        def metric_apply(self,direction):
            projection=np.einsum("...i,...i->...",self.metric,direction)
            factor=(1+2*beta*self.metric_q)/(self.config.metric_tau**2*self.metric_h)
            return self.metric_h[...,None]*direction+self.metric*(factor*projection)[...,None]

    stream.point.PointLinearized=SexticPoint
    return base,SexticPoint
