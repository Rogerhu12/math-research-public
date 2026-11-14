"""Optional flat-acceleration meridian law; does not alter existing source files.
The profile configuration, including ramp_law and ramp_eta, identifies the metric.
Version2 additionally includes every polynomial-piece endpoint in the solver mesh.
"""
import importlib.util
from pathlib import Path
import numpy as np

def flat_piece_knots(flow):
 """All physical prefix knots, including eta and 1-eta inside each ramp."""
 if flow.cfg.get('ramp_law')!='flat':return np.asarray(flow.breakpoints)
 eta=float(flow.cfg.get('ramp_eta',.1));eps=flow.eps
 if not 0<eta<.5:raise ValueError('ramp_eta must lie in (0,.5)')
 u=np.array([0.,eps*eta,eps*(1-eta),eps,1-eps,
             1-eps*(1-eta),1-eps*eta,1.])
 first,second=(flow.Tu,flow.Td)if flow.direction=='outward'else(flow.Td,flow.Tu)
 return np.unique(np.concatenate([np.r_[j*flow.period+first*u,
                    j*flow.period+first+second*u]for j in range(flow.cycles)]))

def install(adaptive):
 original_install=adaptive.old.install_source
 def installer(root):
  original_install(root)
  from fixed_metric_mode3_flow import PlanarSymmetryFlow
  if getattr(PlanarSymmetryFlow,'db6f_flat_installed',False)==2:return
  file=Path(__file__).with_name('950f-prefix-flat-accel-screen.py')
  spec=importlib.util.spec_from_file_location('db6f_flat_law',file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  Flat,_=m.build_flow();original=PlanarSymmetryFlow.prefix_profile;original_init=PlanarSymmetryFlow.__init__
  def prefix_profile(self,s):
   if self.cfg.get('ramp_law')=='flat':return Flat.prefix_profile(self,s)
   return original(self,s)
  def flow_init(self,*args,**kwargs):
   original_init(self,*args,**kwargs)
   if self.cfg.get('ramp_law')=='flat':
    self.breakpoints=flat_piece_knots(self)
    self.breaks=np.unique(np.r_[self.breakpoints,self.end])
  PlanarSymmetryFlow.prefix_profile=prefix_profile
  PlanarSymmetryFlow.__init__=flow_init
  PlanarSymmetryFlow.db6f_flat_installed=2
 adaptive.old.install_source=installer
