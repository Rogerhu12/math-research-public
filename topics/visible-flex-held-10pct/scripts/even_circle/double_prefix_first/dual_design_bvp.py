"""Two physical design parameters, unchanged Frenet residual and core gates.

p[0] changes delta; p[1] changes vd. The core ignores its first correction
slot, and the remaining slots control support modes >=12. Physical profile
knots are fixed in a separate monotone C2 numerical chart.
"""
import numpy as np


def install(Flow,BaseBVP,eta):
    class DualDesignBVP(BaseBVP):
        def __init__(self,*args,**kwargs):
            self._reference_cfg=dict(args[0]if args else kwargs['cfg'])
            self._design_second=0.;self._dual_flow_key=None
            super().__init__(*args,**kwargs)
            if self.fixed:raise ValueError('This prototype is design-only; frozen-metric refinement needs its own coordinate declaration')
            reference=self.flow(0.)
            self._dual_reference_breaks=reference.breaks.copy()
            self._dual_reference_end=reference.end
            self._dual_chart_nodes=self._dual_reference_breaks/reference.end
            self.chart_breaks=self._dual_chart_nodes.copy()
            self._dual_chart_key=None;self.bimodal_eta=float(eta)

        def flow(self,p0):
            p0=float(p0);p1=float(self._design_second);key=(p0,p1)
            if self._dual_flow_key!=key or getattr(self,'_flow',None)is None:
                delta=self._reference_cfg['delta']+p0;vd=self._reference_cfg['vd']+p1
                if not .002<delta<2:raise FloatingPointError('Excursion outside original design domain')
                if not 0<vd<1:raise FloatingPointError('Return speed outside original positive meridian domain')
                self._flow=self.Flow({**self.cfg,'delta':delta,'vd':vd},self.port,self.M,self.q,self.nt,self.base_mode,self.bridge)
                self._dual_flow_key=key;self._flow_key=p0
            return self._flow

        def initial(self,p):
            self._design_second=float(p[1])
            current_vd=self._reference_cfg['vd']+self._design_second
            if self.cfg['vd']!=current_vd:
                self.cfg['vd']=current_vd;self._flow_key=None;self._dual_flow_key=None;self._flow=None
            ans=super().initial(p)
            # LiftBVP.initial deliberately calls super().flow, so both the
            # inherited one-parameter cache and this two-parameter cache must
            # name the same fully lifted object after every parameter change.
            self._flow_key=float(p[0]);self._dual_flow_key=(float(p[0]),self._design_second)
            return ans

        def _chart_data(self,p0):
            f=self.flow(p0);key=self._dual_flow_key
            if key!=self._dual_chart_key:
                target=f.breaks
                if len(target)!=len(self._dual_reference_breaks):raise FloatingPointError('Physical knot count changed')
                # Retain the inherited profile-range guard. Its role is
                # numerical chart admissibility, not a physical theorem.
                if not 0<f.prefix_end/self.chart_reference_prefix<2:raise FloatingPointError('Design excursion left the original chart range')
                dx=np.diff(self._dual_chart_nodes);dy=np.diff(target)
                if min(dx)<=0 or min(dy)<=0:raise FloatingPointError('Nonpositive physical chart interval')
                slope=dy/dx
                # Smooth soft minimum: d/min(slope)<=N^(1/16)<15/7 for
                # this finite chart, so every quintic has positive derivative.
                vmin=float(slope.min());d=vmin*(float(np.mean((vmin/slope)**16)))**(-1/16)
                lower=float(np.min((15*slope-7*d)/8))
                if lower<=0:raise FloatingPointError('C2 physical chart derivative cannot be certified positive')
                self._dual_chart_data=(target.copy(),slope,d,lower)
                self._dual_chart_key=key
            return self._dual_chart_data

        def chart(self,t,p0):
            target,slope,d,_=self._chart_data(p0);t=np.asarray(t,float)
            nodes=self._dual_chart_nodes
            i=np.clip(np.searchsorted(nodes,t,side='right')-1,0,len(nodes)-2)
            h=nodes[i+1]-nodes[i];u=np.clip((t-nodes[i])/h,0.,1.)
            S=u**3*(10-15*u+6*u*u);Sp=30*u*u*(1-u)**2
            s=target[i]+d*h*u+(slope[i]-d)*h*S
            ds=d+(slope[i]-d)*Sp
            return s,ds

        def inverse_chart(self,s,p0):
            target,slope,d,_=self._chart_data(p0);s=np.asarray(s,float)
            i=np.clip(np.searchsorted(target,s,side='right')-1,0,len(target)-2)
            nodes=self._dual_chart_nodes;h=nodes[i+1]-nodes[i]
            z=(s-target[i])/h;u=np.clip(z/slope[i],0.,1.);lo=np.zeros_like(u);hi=np.ones_like(u)
            for _ in range(48):
                S=u**3*(10-15*u+6*u*u);Sp=30*u*u*(1-u)**2
                residual=d*u+(slope[i]-d)*S-z
                if np.max(abs(residual*h))<2e-14:break
                lo=np.where(residual<0,u,lo);hi=np.where(residual>0,u,hi)
                trial=u-residual/(d+(slope[i]-d)*Sp)
                bad=(trial<lo)|(trial>hi)|~np.isfinite(trial)
                u=np.where(bad,(lo+hi)/2,trial)
            out=nodes[i]+h*u
            if np.max(abs(self.chart(out,p0)[0]-s))>2e-13:raise FloatingPointError('C2 chart inverse residual')
            return out

        def fun_jac(self,t,y,p):
            J,P=super().fun_jac(t,y,p)
            step=2e-6*max(.1,self._reference_cfg['vd']+p[1]);plus=p.copy();minus=p.copy();plus[1]+=step;minus[1]-=step
            P[:,1,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
            self.initial(p)
            return J,P

        def bc_jac(self,ya,yb,p):
            A,B,P=super().bc_jac(ya,yb,p)
            for j,name in ((0,'delta'),(1,'vd')):
                step=2e-6*max(.1,self._reference_cfg[name]+p[j]);plus=p.copy();minus=p.copy();plus[j]+=step;minus[j]-=step
                P[:,j]=(self.bc(ya,yb,plus)-self.bc(ya,yb,minus))/(2*step)
            self.initial(p)
            return A,B,P

        def seed(self,nodes):
            from fixed_metric_mode3_bvp import merge_profile_mesh
            p=np.zeros(self.M);self.initial(p);flow=self.flow(0.)
            t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks);s,_=self.chart(t,0.)
            N=max(2048,64*self.M);g=flow.geo(s,N);theta=g['theta']
            er=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
            et=np.stack((-np.sin(theta),np.cos(theta),np.zeros_like(theta)),axis=-1)
            shape=np.zeros_like(er)
            weights=(1+self.bimodal_eta,-(self.base_mode**2-1)*self.bimodal_eta/(4*self.base_mode**2-1))
            for j,weight in enumerate(weights):
                line=flow.backward_line(j);fg=np.empty((2,len(s)))
                for k,(lo,hi,solution,scale)in enumerate(line.segments):
                    mask=(s>=lo)&((s<hi)if k+1<len(line.segments)else(s<=hi))
                    if np.any(mask):fg[:,mask]=solution(s[mask])*np.exp(scale-line.logscale)/line.core[0]
                mode=self.base_mode*(j+1)
                shape+=weight*fg[0,:,None,None]*(np.cos(mode*theta)[:,:,None]*er-np.sin(mode*theta)[:,:,None]*et/mode)
                shape[:,:,2]+=weight*fg[1,:,None]*np.cos(mode*theta)
            # Remove only the explicitly present reference lift from the
            # perturbation seed; the actual nonlinear residual is unchanged.
            ar=flow.profile(s)[0];shape-=(g['pos']-ar[:,None,None]*er)/self.q
            B,_,_=flow.basis(N);y=flow.project(shape,B)
            difference=self.initial(p)-y[:,0]
            u=np.clip((s-.5*flow.prefix_end)/(.4*flow.prefix_end),0.,1.)
            taper=ar*(1-u**3*(10-15*u+6*u*u))
            y+=difference[:,None]*taper[None,:]
            return t,y,p

    return DualDesignBVP
