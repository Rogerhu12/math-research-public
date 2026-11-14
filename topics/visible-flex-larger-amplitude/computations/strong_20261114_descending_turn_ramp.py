"""An optional physical ramp fraction for the first outward-to-inward turn.

Only the first genuine turn from positive to negative radial slope changes.
The accepted value eps=0.08 leaves every original segment byte-for-byte
unchanged. Other values define a new prefix scalar metric; the loop, finite
terminal bridge, physical tail cut and tail metric are unchanged. No numerical
state, spectral coefficient, tail equation or acceptance criterion changes.
"""
from __future__ import annotations
import math
import numpy as np

DEFAULT=0.08
FIELD='descending_turn_ramp'


def install(provider):
 if getattr(provider,'_strong_descending_turn_ramp_installed',False):return
 original=provider.NeckPrefix
 class DescendingTurnRampPrefix(original):
  def append(self,segment):
   if (segment['kind']=='turn' and segment['p0']>0>segment['p1'] and not getattr(self,'_strong_descending_turn_seen',False)):
    self._strong_descending_turn_seen=True
    eps=float(self.cfg.get(FIELD,DEFAULT))
    if not math.isfinite(eps) or not 0<eps<.5:raise ValueError('The first-turn ramp fraction must lie strictly between zero and one half')
    if eps!=float(segment['turn_ramp']):
     p0,p1,K=segment['p0'],segment['p1'],segment['K'];L=abs(p1-p0)/(K*(1-eps));segment=dict(segment,length=L,turn_ramp=eps)
     segment['dr']=L*float(provider.fl.integral(segment,1.));segment['dh']=L*float(provider.fl.integral(segment,1.,'cos'))
     u=np.linspace(0,1,301);r=L*provider.fl.integral(segment,u);segment['dr_min']=float(r.min());segment['dr_max']=float(r.max())
   return super().append(segment)
 provider.NeckPrefix=DescendingTurnRampPrefix;provider._strong_descending_turn_ramp_installed=True
