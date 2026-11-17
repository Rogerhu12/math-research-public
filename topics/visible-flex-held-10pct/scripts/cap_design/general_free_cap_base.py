"""No imposed angular reflection or half-turn symmetry; full mean metric."""
import numpy as np
from negative_entry_cap_base import Model as Base
class Model(Base):
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs);self.nangular=2*self.m+1;self.shape=(self.nc-6,3*self.nangular);self.size=np.prod(self.shape)
 def angles(self,u):
  values=[np.zeros((len(u),3*self.nangular,3))for _ in range(3)]
  for dim in range(3):
   offset=dim*self.nangular;values[0][:,offset,dim]=1
   for f in range(1,self.m+1):
    c,s=offset+2*f-1,offset+2*f
    values[0][:,c,dim]=np.cos(f*u);values[1][:,c,dim]=-f*np.sin(f*u);values[2][:,c,dim]=-f*f*np.cos(f*u)
    values[0][:,s,dim]=np.sin(f*u);values[1][:,s,dim]=f*np.cos(f*u);values[2][:,s,dim]=-f*f*np.sin(f*u)
  return values
 def residual_jac(self,q,g,need_jac=False):
  base=super().residual_jac(q,g,need_jac);_,fs,fu=self.geometry(q,g)
  e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1);me=np.maximum(e.mean(1,keepdims=True),1e-15);mf=f.mean(1,keepdims=True);mg=np.maximum(gg.mean(1,keepdims=True),1e-15);n=len(g['s'])*len(g['u']);schur=me-mf*mf/mg
  if not need_jac:
   base[:3*n].reshape(len(g['s']),len(g['u']),3)[:,:,1]=np.sqrt(2)*(f-mf)/np.sqrt(me*mg)
   return np.r_[base,10*np.sqrt(len(g['u']))*np.maximum(.15-schur[:,0],0)]
  Bs=g['r'][1][:,None,:,None,None]*g['ang'][0][None,:,None,:,:];Bu=g['r'][0][:,None,:,None,None]*g['ang'][1][None,:,None,:,:]
  de=2*np.sum(fs[:,:,None,None,:]*Bs,-1);df=np.sum(fu[:,:,None,None,:]*Bs+fs[:,:,None,None,:]*Bu,-1);dg=2*np.sum(fu[:,:,None,None,:]*Bu,-1);dme=de.mean(1,keepdims=True);dmf=df.mean(1,keepdims=True);dmg=dg.mean(1,keepdims=True);ME=me[:,:,None,None];MF=mf[:,:,None,None];MG=mg[:,:,None,None]
  jf=np.sqrt(2)*(df-dmf)/np.sqrt(ME*MG)-np.sqrt(2)*(f-mf)[:,:,None,None]/np.sqrt(ME*MG)*.5*(dme/ME+dmg/MG)
  base[:3*n].reshape(len(g['s']),len(g['u']),3,self.size)[:,:,1]=jf.reshape(len(g['s']),len(g['u']),self.size)
  ds=dme-2*MF/MG*dmf+MF**2/MG**2*dmg;js=-10*np.sqrt(len(g['u']))*ds[:,0]*(schur[:,0]<.15)[:,None,None]
  return np.r_[base,js.reshape(-1,self.size)]
 def audit(self,q,n=129,nu=128):
  report=super().audit(q,n,nu);g=self.prepare(np.linspace(0,1,n),np.arange(nu)*2*np.pi/nu);_,fs,fu=self.geometry(q,g);e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1);me=e.mean(1,keepdims=True);mf=f.mean(1,keepdims=True);mg=gg.mean(1,keepdims=True)
  de=e-me;df=f-mf;dg=gg-mg;det=me*mg-mf*mf;tr=(mg*de+me*dg-2*mf*df)/det;deld=(de*dg-df*df)/det;root=np.sqrt(np.maximum(tr*tr-4*deld,0))
  report['full_mean_metric_max']=float(np.max(np.maximum(np.abs((tr+root)/2),np.abs((tr-root)/2))));report['Fmean_range']=[float(mf.min()),float(mf.max())];report['schur_min']=float(np.min(me-mf*mf/mg));return report
