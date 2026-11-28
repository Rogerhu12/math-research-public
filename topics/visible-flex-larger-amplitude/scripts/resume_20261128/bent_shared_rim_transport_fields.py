"""Run53 uses the complete Run44 physical coefficient spaces and the R790 base evaluator."""
from types import SimpleNamespace

import numpy as np

import bent_shared_rim_fields as original
import r790_multiphase_tube_transport as physical

prior = original.prior
layout = original.layout


class Model(original.Model):
    def base(self, design, phase):
        if not phase:
            return self.mesh.f0.copy()
        return np.concatenate([physical.chart_jet(chart, u, v, phase, design)
                               for chart, u, v, _ in self.mesh.cases])


def evaluate(d,cfg,z,chart,u,v,t):
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=a.shape
    u=a.ravel();v=b.ravel();out=[]
    rr,cc,jj=original.layout(cfg);coeff=z.reshape(2,rr+cc+jj,3)[0 if chart.endswith("+") else 1]
    if chart=="cylinder":return physical.chart_jet(chart,a,b,t,d)
    for first in range(0,len(u),384):
        sl=slice(first,first+384);a=u[sl];b=v[sl]
        f=physical.chart_jet(chart,a,b,t,d);f0=physical.delay.chart_jet(chart,a,b,0.,bend=0.,rotate=False)
        if chart.startswith("end"):
            fake=SimpleNamespace(xy=np.c_[a,b],delay=physical.delay,g=physical.g,roll=[slice(None)])
            B=prior.Basis(fake,cfg).B;c=coeff[:rr]
        else:B=prior.cap_matrix(chart,b,f0,cfg);c=coeff[rr:rr+cc]
        f=f+(B@c).transpose(1,0,2)
        js=original.rim(chart,a,b,f0,cfg)[1]
        out.append(f+(js@coeff[rr+cc:]).transpose(1,0,2))
    return np.concatenate(out).reshape(sh+(6,3))
