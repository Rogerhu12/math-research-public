"""New experiment: constant meridian speed removes radial reparameterization."""
import numpy as np
from half_cap_homotopy_base import Model as BoundedModel
class Model(BoundedModel):
 def residual_jac(self,q,g,need_jac=False):
  base=super().residual_jac(q,g,need_jac)
  _,fs,_=self.geometry(q,g)
  e=np.sum(fs*fs,axis=-1);n=len(g['s'])*len(g['u'])
  if not need_jac:
   base[:3*n].reshape(len(g['s']),len(g['u']),3)[:,:,0]=e/self.speed**2-1
   return base
  Bs=g['r'][1][:,None,:,None,None]*g['ang'][0][None,:,None,:,:]
  de=2*np.sum(fs[:,:,None,None,:]*Bs,axis=-1)
  base[:3*n].reshape(len(g['s']),len(g['u']),3,self.size)[:,:,0,:]=de.reshape(len(g['s']),len(g['u']),self.size)/self.speed**2
  return base
 def audit(self,q,n=129,nu=128):
  report=super().audit(q,n,nu)
  g=self.prepare(np.linspace(0,1,n),np.arange(nu)*2*np.pi/nu)
  _,fs,fu=self.geometry(q,g)
  e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1);mg=gg.mean(1,keepdims=True)
  de=e/self.speed**2-1;df=f/np.sqrt(self.speed**2*mg);dg=gg/mg-1
  root=np.sqrt((de-dg)**2/4+df*df)
  report['constant_E_metric_max']=float(np.max(np.maximum(np.abs((de+dg)/2+root),np.abs((de+dg)/2-root))))
  report['constant_E_target']=self.speed**2
  return report
