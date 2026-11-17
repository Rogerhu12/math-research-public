"""Chiral half-turn-symmetric trial space; full angular-mean metric allowed."""
import numpy as np
from half_cap_homotopy_base import Model as Base
class Model(Base):
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs);self.shape=(self.nc-6,6*self.m-1);self.size=np.prod(self.shape)
 def angles(self,u):
  odd,even=self.odd,self.even;n=6*self.m-1
  vals=[np.zeros((len(u),n,3))for _ in range(3)];k=0
  for dim,frequencies in [(0,odd),(1,odd),(2,even)]:
   for f in frequencies:
    vals[0][:,k,dim]=np.cos(f*u);vals[1][:,k,dim]=-f*np.sin(f*u);vals[2][:,k,dim]=-f*f*np.cos(f*u);k+=1
    if f:
     vals[0][:,k,dim]=np.sin(f*u);vals[1][:,k,dim]=f*np.cos(f*u);vals[2][:,k,dim]=-f*f*np.sin(f*u);k+=1
  return vals
 def residual_jac(self,q,g,need_jac=False):
  base=super().residual_jac(q,g,need_jac);_,fs,fu=self.geometry(q,g)
  e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1);me=e.mean(1,keepdims=True);mf=f.mean(1,keepdims=True);mg=gg.mean(1,keepdims=True)
  me=np.maximum(me,1e-15);mg=np.maximum(mg,1e-15);n=len(g['s'])*len(g['u']);schur=me-mf*mf/mg
  if not need_jac:
   view=base[:3*n].reshape(len(g['s']),len(g['u']),3);view[:,:,0]=e/self.speed**2-1;view[:,:,1]=np.sqrt(2)*(f-mf)/np.sqrt(me*mg)
   return np.r_[base,10*np.sqrt(len(g['u']))*np.maximum(.04-schur[:,0],0)]
  Bs=g['r'][1][:,None,:,None,None]*g['ang'][0][None,:,None,:,:];Bu=g['r'][0][:,None,:,None,None]*g['ang'][1][None,:,None,:,:]
  de=2*np.sum(fs[:,:,None,None,:]*Bs,-1);df=np.sum(fu[:,:,None,None,:]*Bs+fs[:,:,None,None,:]*Bu,-1);dg=2*np.sum(fu[:,:,None,None,:]*Bu,-1)
  dme=de.mean(1,keepdims=True);dmf=df.mean(1,keepdims=True);dmg=dg.mean(1,keepdims=True)
  ME=me[:,:,None,None];MF=mf[:,:,None,None];MG=mg[:,:,None,None]
  jf=np.sqrt(2)*(df-dmf)/np.sqrt(ME*MG)-np.sqrt(2)*(f-mf)[:,:,None,None]/np.sqrt(ME*MG)*.5*(dme/ME+dmg/MG)
  view=base[:3*n].reshape(len(g['s']),len(g['u']),3,self.size);view[:,:,0]=de.reshape(len(g['s']),len(g['u']),self.size)/self.speed**2;view[:,:,1]=jf.reshape(len(g['s']),len(g['u']),self.size)
  ds=dme-2*MF/MG*dmf+MF**2/MG**2*dmg;js=-10*np.sqrt(len(g['u']))*ds[:,0]*(schur[:,0]<.04)[:,None,None]
  return np.r_[base,js.reshape(-1,self.size)]
 def audit(self,q,n=129,nu=128):
  report=super().audit(q,n,nu);g=self.prepare(np.linspace(0,1,n),np.arange(nu)*2*np.pi/nu);_,fs,fu=self.geometry(q,g)
  e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1);me=np.full((n,1),self.speed**2);mf=f.mean(1,keepdims=True);mg=gg.mean(1,keepdims=True)
  de=e-me;df=f-mf;dg=gg-mg;det=me*mg-mf*mf;tr=(mg*de+me*dg-2*mf*df)/det;deld=(de*dg-df*df)/det;root=np.sqrt(np.maximum(tr*tr-4*deld,0))
  report['full_mean_metric_max']=float(np.max(np.maximum(np.abs((tr+root)/2),np.abs((tr-root)/2))));report['Fmean_range']=[float(mf.min()),float(mf.max())];report['schur_min']=float(np.min(me-mf*mf/mg));report['constant_E_target']=self.speed**2
  return report
