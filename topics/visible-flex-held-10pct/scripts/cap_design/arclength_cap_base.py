"""Use an existing candidate's unchanged image as a constant-mean-speed reference.

The intended inverse is defined by the exact positive one-dimensional integral.
Floating quadrature/Newton evaluations here are diagnostics, not interval bounds.
"""
import json
import numpy as np
from wide_round_cap_base import Model as Bounded
class Model(Bounded):
 def __init__(self,*args,reference,**kwargs):
  data=json.load(open(reference));p=data['parameters'];oldargs={k:p[k]for k in ['B','height','speed','rc','nc','m','bend']}
  self.old=Bounded(**oldargs);self.oldq=np.array(data['q']);self.source=reference
  super().__init__(*args,**kwargs)
  self.mean_u=np.arange(192)*2*np.pi/192;self.qx,self.qw=np.polynomial.legendre.leggauss(32);self.oldknots=self.old.intervals
  lengths=self.integrals(self.oldknots[:-1],self.oldknots[1:]);self.cumulative=np.r_[0.,np.cumsum(lengths)];self.speed=float(self.cumulative[-1]);self.reference_info={'source':reference,'length':self.speed,'angular_mean_nodes':192,'quadrature_nodes_per_old_interval':32,'inverse_residual_max':0.}
 def means(self,s,second=False):
  s=np.asarray(s);g=self.old.prepare(s,self.mean_u);jets=self.old.geometry(self.oldq,g,second);fs=jets[1];E=np.mean(np.sum(fs*fs,-1),axis=1)
  if second:return E,2*np.mean(np.sum(fs*jets[3],-1),axis=1)
  return E
 def integrals(self,left,right):
  left,right=np.asarray(left),np.asarray(right);half=(right-left)/2;points=left[:,None]+half[:,None]*(1+self.qx)
  values=np.sqrt(np.maximum(self.means(points.ravel()),1e-30)).reshape(len(left),len(self.qx));return half*(values@self.qw)
 def inverse(self,v):
  v=np.asarray(v);target=self.speed*v;idx=np.searchsorted(self.cumulative,target,side='right')-1;idx=np.clip(idx,0,len(self.oldknots)-2);a=self.oldknots[idx];b=self.oldknots[idx+1];local=target-self.cumulative[idx];lengths=self.cumulative[idx+1]-self.cumulative[idx]
  s=a+(b-a)*local/lengths;lo=a.copy();hi=b.copy()
  for _ in range(8):
   value=self.integrals(a,s);err=value-local;lo=np.where(err<0,s,lo);hi=np.where(err>=0,s,hi);snew=s-err/np.sqrt(self.means(s));s=np.where((snew<lo)|(snew>hi),(lo+hi)/2,snew)
  s=np.where(v==0,0,s);s=np.where(v==1,1,s);error=np.max(np.abs(self.integrals(a,s)-local));self.reference_info['inverse_residual_max']=max(self.reference_info['inverse_residual_max'],float(error))
  E,Ep=self.means(s,True);sp=self.speed/np.sqrt(E);spp=-self.speed**2*Ep/(2*E*E);return s,sp,spp
 def prepare(self,v,u):
  v,u=np.asarray(v),np.asarray(u);s,sp,spp=self.inverse(v);oldg=self.old.prepare(s,u);x,xs,xu,xss,xsu,xuu=self.old.geometry(self.oldq,oldg,True)
  geom=[x,xs*sp[:,None,None],xu,xss*sp[:,None,None]**2+xs*spp[:,None,None],xsu*sp[:,None,None],xuu]
  return dict(s=v,u=u,geom=geom,r=self.radial(v),ang=self.angles(u))
 def residual_jac(self,q,g,need_jac=False):
  base=super().residual_jac(q,g,need_jac);_,fs,_=self.geometry(q,g);e=np.sum(fs*fs,-1);n=len(g['s'])*len(g['u'])
  if not need_jac:
   base[:3*n].reshape(len(g['s']),len(g['u']),3)[:,:,0]=e/self.speed**2-1;return base
  Bs=g['r'][1][:,None,:,None,None]*g['ang'][0][None,:,None,:,:];de=2*np.sum(fs[:,:,None,None,:]*Bs,-1)
  base[:3*n].reshape(len(g['s']),len(g['u']),3,self.size)[:,:,0]=de.reshape(len(g['s']),len(g['u']),self.size)/self.speed**2;return base
 def audit(self,q,n=129,nu=128):
  report=super().audit(q,n,nu);g=self.prepare(np.linspace(0,1,n),np.arange(nu)*2*np.pi/nu);_,fs,fu=self.geometry(q,g);e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1);mg=gg.mean(1,keepdims=True);de=e/self.speed**2-1;df=f/(self.speed*np.sqrt(mg));dg=gg/mg-1;root=np.sqrt((de-dg)**2/4+df*df)
  report['constant_E_metric_max']=float(np.max(np.maximum(np.abs((de+dg)/2+root),np.abs((de+dg)/2-root))));report['constant_E_target']=self.speed**2;report['reference_info']=self.reference_info.copy();return report
