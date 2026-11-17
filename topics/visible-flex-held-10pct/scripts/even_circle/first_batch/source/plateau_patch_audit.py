"""Sampled full-map two-jet comparison with the exact circular local model.
The characteristic window is numerical; no continuous enclosure is claimed.
"""
import numpy as np
from scipy.integrate import cumulative_trapezoid


def patch_audit(obj,sol,N=384,points=101):
    f=obj.flow(sol.p[0]);obj.initial(sol.p);core=obj._core
    B,B1,B2=f.basis(N);s=np.array([0.]);Y=sol.sol(s);fr=f.frame(s,obj.q*Y,B1,B2);g=fr['geo'];actual=g['pos']+obj.q*f.values(Y,B);exact=core.evaluate(g['theta'][0]);rho=g['rho']
    first=fr['d']/rho[:,:,None];second=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
    inlet=dict(position=float(np.linalg.norm(actual[0]-exact['F'],axis=1).max()),first=float(np.linalg.norm(first[0]-exact['Ft'],axis=1).max()),second=float(np.linalg.norm(second[0]-exact['Ftt'],axis=1).max()),metric=float(np.max(abs(np.sum(first*first,axis=2)-1))))
    out=dict(scope=__doc__,actual_inlet=inlet)
    if core.lam!=1:return out
    R=1+core.sign*core.factor*core.q;k=1/R;u0=float(core.arc(np.array([core.center]))[0]);center=core.normal_geometry(np.array([core.center]))['F'][0]-R*np.array([np.cos(core.center),np.sin(core.center),0.])
    end=(1-f.eps)*f.Tu;s=np.unique(np.r_[np.linspace(0,end,points),f.breaks[(f.breaks>=0)&(f.breaks<=end)]]);a,ap,app=f.profile(s)
    if np.min(k*k-ap*ap)<=0:return dict(**out,patch_error='local root domain')
    speed=np.sqrt(np.maximum(app,0)/(a*(k*k-ap*ap)));chi=cumulative_trapezoid(speed,s,initial=0);heightlocal=cumulative_trapezoid(np.sqrt(1-(ap/k)**2),s,initial=0);height=f.height_integral(sol,s,N,6)
    half=(float(core.arc(np.array([core.center+core.a]))[0])-float(core.arc(np.array([core.center-core.a]))[0]))/2
    errors={name:0. for name in ['X','Xs','Xu','Xss','Xsu','Xuu']};count=0;maxs=0.
    for st in range(0,len(s),24):
        sl=slice(st,st+24);ss=s[sl];Y=sol.sol(ss);Yp=sol.sol(ss,1);Ypp=sol.sol(ss,2);fr,Fsp,dW=f.velocity_s(ss,Y,Yp,B1,B2);g=fr['geo'];rh=g['rho'];v=g['v'];aa=fr['a'][:,None];av=fr['ap'][:,None];acc=fr['app'][:,None]
        Fsc=g['s1']+obj.q*f.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fssc=g['s2']+obj.q*f.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
        actual={'X':g['pos']+obj.q*f.values(Y,B),'Xs':Fsc-v[:,:,None]*fr['d'],'Xu':fr['d']/rh[:,:,None],'Xuu':fr['dd']/rh[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rh[:,:,None]**3,'Xsu':(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rh[:,:,None],'Xss':Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']}
        actual['X'][:,:,2]+=height[sl,None]
        u=(g['theta']-u0+np.pi)%(2*np.pi)-np.pi;angle=core.center+k*u;n=np.stack((np.cos(angle),np.sin(angle),np.zeros_like(angle)),axis=-1);t=np.stack((-np.sin(angle),np.cos(angle),np.zeros_like(angle)),axis=-1);bb=np.sqrt(1-(av/k)**2)
        target={'X':center[None,None,:]+(aa/k)[:,:,None]*n,'Xs':(av/k)[:,:,None]*n,'Xu':aa[:,:,None]*t,'Xss':(acc/k)[:,:,None]*n,'Xsu':av[:,:,None]*t,'Xuu':(-aa*k)[:,:,None]*n}
        target['X'][:,:,2]+=heightlocal[sl,None];target['Xs'][:,:,2]=bb;target['Xss'][:,:,2]=-av*acc/(k*k*bb)
        mask=abs(u)<(half-chi[sl,None]-.01)
        if np.any(mask):
            count+=int(mask.sum());maxs=max(maxs,float(np.max(np.broadcast_to(ss[:,None],u.shape)[mask])))
            for name in errors:errors[name]=max(errors[name],float(np.max(np.linalg.norm(actual[name]-target[name],axis=2)[mask])))
    out.update(radius=R,normal_width=2*core.a,circle_center=center.tolist(),characteristic_loss_at_end=float(chi[-1]),sampled_patch_end=maxs,sampled_points=count,patch_twojet_errors=errors,local_height_quadrature='trapezoid on recorded s grid; this contributes to X error only')
    return out
