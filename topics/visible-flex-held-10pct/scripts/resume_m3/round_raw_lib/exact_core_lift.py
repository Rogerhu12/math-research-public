"""Exact planar core retained as a reference lift in the Frenet collocation.
Only the correction to this reference is Fourier represented. The full
unprojected Frenet and metric residual remain necessary diagnostics.
"""
import types
import numpy as np


def install_core_lift(Flow,BaseBVP,window=(.5,.9)):
    original_geo=Flow.geo
    def geo(self,s,N):
        g=original_geo(self,s,N)
        core=getattr(self,'exact_lift_core',None)
        if core is None:return g
        cached=self.exact_lift_cache.get(N)
        if cached is None:
            ang=self.angular(N);B,B1,B2=self.basis(N);z=core.evaluate(ang[1]);c=self.q*self.exact_lift_initial[:,None]
            H=z['F']-ang[4]-self.values(c,B)[0]
            H1=z['Ft']*ang[2][:,None]-ang[5]-self.values(c,B1)[0]
            H2=z['Ftt']*ang[2][:,None]**2+z['Ft']*ang[3][:,None]-ang[6]-self.values(c,B2)[0]
            cached=(H,H1,H2);self.exact_lift_cache[N]=cached
        H,H1,H2=cached;s=np.atleast_1d(s);aa,av,acc=self.profile(s)
        lo,hi=window;span=(hi-lo)*self.prefix_end;x=np.clip((s-lo*self.prefix_end)/span,0.,1.)
        chi=1-x**3*(10-15*x+6*x*x);chip=-30*x*x*(1-x)**2/span;chipp=-60*x*(1-x)*(1-2*x)/span**2
        h=aa*chi;hp=av*chi+aa*chip;hpp=acc*chi+2*av*chip+aa*chipp
        for name,factor,Hj in [('pos',h,H),('p1',h,H1),('p2',h,H2),('s1',hp,H),('s2',hpp,H),('sp',hp,H1),('spp',hp,H2)]:
            g[name]=g[name]+factor[:,None,None]*Hj[None,:,:]
        return g
    Flow.geo=geo
    class LiftBVP(BaseBVP):
        def initial(self,p):
            ans=super().initial(p)
            if not hasattr(self,'unlifted_projection') or self._core_key!=getattr(self,'_lift_inlet_key',None):
                self.unlifted_projection=dict(self._inlet_metrics);self._lift_inlet_key=self._core_key
            self._inlet_metrics=dict(position=0.,first=0.,second=0.,metric_l1=0.,scope='The analytical reference lift retains the exact core and its two angular jets; quadrature/inversion roundoff is audited separately.',unlifted_projection=self.unlifted_projection)
            f=super().flow(p[0])
            if getattr(f,'exact_lift_key',None)!=self._core_key:
                f.exact_lift_core=self._core;f.exact_lift_initial=ans.copy();f.exact_lift_cache={};f.exact_lift_key=self._core_key
            return ans
        def fun(self,t,y,p):
            self.initial(p)
            return super().fun(t,y,p)
        def fun_jac(self,t,y,p):
            self.initial(p);f=self.flow(p[0]);s,ds=self.chart(t,p[0]);J,_=f.fun_jac(s,y,p);PJ=np.empty((self.n,len(p),len(t)))
            for j in range(len(p)):
                step=(2e-6*max(.1,self.cfg['delta']+p[0]) if j==0 else 2e-5*max(1.,abs(p[j])))
                plus=p.copy();minus=p.copy();plus[j]+=step;minus[j]-=step
                PJ[:,j,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
            self.initial(p)
            return ds[None,None,:]*J,PJ
        def terminal(self,y,p):
            self.initial(p)
            return super().terminal(y,p)
    return LiftBVP
