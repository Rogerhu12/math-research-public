"""Explicit n-fold extension of original warped Cartesian Frenet code.
Only mode-dependent trigonometry and coordinate derivatives change. The
original residual, geometry guard, Newton solver and physical metric remain.
"""
import sys,types,hashlib
from pathlib import Path
TRANSFORMS={}
def module(name,path,replacements=()):
 source=Path(path).read_text();original=source;applied=[]
 for a,b in replacements:
  count=source.count(a)
  if not count:raise ValueError('Missing exact transformation: '+a)
  source=source.replace(a,b);applied.append([a,b,count])
 mod=types.ModuleType(name);mod.__file__=str(path);sys.modules[name]=mod
 exec(compile(source,str(path),'exec'),mod.__dict__)
 TRANSFORMS[str(path)]=dict(sha256=hashlib.sha256(original.encode()).hexdigest(),replacements=applied)
 return mod

def load(source_topic,n=4):
 if not isinstance(n,int)or n<2:raise ValueError('Integral n>=2 required')
 S=Path(source_topic)/'scripts';N=Path(source_topic)/'notes';R=Path(source_topic)/'repro/source-root'
 sys.path[:0]=[str(N),str(R/'topics/large-amplitude-twist-flex/scripts')]
 old=module('even_mode_warp',S/'950f-prefix-warped-bvp.py',[
  ('self.warp_e=8*float(warp_q)',f'self.warp_e={n*n-1}*float(warp_q)'),
  ('3*psi',f'{n}*psi'),('3*theta',f'{n}*theta'),
  (f'np.sin({n}*psi)/3',f'np.sin({n}*psi)/{n}'),
  ('rho1=3*e',f'rho1={n}*e'),
  ('cfg,port,q,M,angular,3,fixed',f'cfg,port,q,M,angular,{n},fixed'),
  ('self.pscale,3)',f'self.pscale,{n})'),
  ('*et/3',f'*et/{n}'),('obj.M*3+1',f'obj.M*{n}+1'),
  ('base_mode=3,core_kind=',f'base_mode={n},core_kind=')])
 pre="spec=importlib.util.spec_from_file_location('prefixwarp',HERE/'950f-prefix-warped-bvp.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)"
 ad=module('even_mode_adaptive',S/'950f-prefix-adaptive-chart-bvp-v2.py',[
  (pre,"old=sys.modules['even_mode_warp']"),
  ('3*psi',f'{n}*psi'),('3*theta',f'{n}*theta'),('3*np.arange',f'{n}*np.arange'),
  ('*sn/3',f'*sn/{n}'),('rho_p=3*e',f'rho_p={n}*e'),('rho_ps=3*ep',f'rho_ps={n}*ep'),
  ('*et/3',f'*et/{n}'),('max(64,self.nt),3,',f'max(64,self.nt),{n},'),
  ('psi)/3-target',f'psi)/{n}-target'),('obj.M*3+1',f'obj.M*{n}+1'),
  ('base_mode=3,core_kind=',f'base_mode={n},core_kind=')])
 patch=module('even_mode_flat',S/'db6f-prefix-flat-profile.py');patch.install(ad);ad.old.install_source(R)
 return ad
