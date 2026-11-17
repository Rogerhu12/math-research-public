#!/usr/bin/env python3
"""Direct geometry optimization around a literal accepted weak height.

The accepted integral-K height is used as a function, without a B-spline fit.
A new reference metric and C2 height patch are defined only beyond its finite
end. Cut-fraction zero uses the same weak field's initial curve; one uses the
true original prefix Cartesian 0/1/2 jets. Intermediate cuts are local
compatible optimization data, not accepted prefix surfaces. Five logw design
variables may change the reference metric and must be frozen before refinement.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,time
import numpy as np

HERE=Path(__file__).parent

def module(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out

direct=module('accepted_base_direct','2026-11-17-parallel-model-direct-height-autodiff.py')
mode_api=module('accepted_base_modes','2026-11-17-parallel-geometry-height-mode-api.py')
flat=module('accepted_base_flat','2026-11-17-parallel-geometry-flat-cuff.py')

class AcceptedBase(direct.Design):
    def reference_metric(self,r):
        r=np.asarray(r);inner=np.minimum(r,self.deep_r)
        w=np.exp(self.bg.spline(inner));wr=w*self.bg.spline(inner,1)
        outside=r>self.deep_r
        if np.any(outside):
            u=(r[outside]-self.deep_r)/self.cap_width
            B=self.deep_w*(1+2*u)+self.cap_width*self.deep_wr*u+self.args.cap_lift*u*u
            Bp=2*self.deep_w+self.cap_width*self.deep_wr+2*self.args.cap_lift*u
            w[outside]=(1-u)**2*B
            wr[outside]=(-2*(1-u)*B+(1-u)**2*Bp)/self.cap_width
        return w,wr

    def __init__(self,args):
        started=time.perf_counter();raw=json.loads(args.background.read_text());last=raw['rows'][-1]
        self.deep_r=last['r'];self.cap_width=args.cuff_radius-self.deep_r
        if self.cap_width<=0:raise ValueError('The new flat cuff must lie outside the finite accepted field')
        self.deep_w=np.exp(last['logw']);self.deep_wr=self.deep_w*last['dlogwdr']
        w0,w1,d,A=self.deep_w,self.deep_wr,self.cap_width,args.cap_lift
        self.wpolynomial=np.array([w0,d*w1,-3*w0-2*d*w1+A,2*w0+d*w1-2*A,A])
        args.end_radius=args.cuff_radius;args.amplitude=1.
        if getattr(args,'cap_metric_modes',False):
            r0=json.loads(args.trace.read_text())['r']
            knots=json.loads(args.metric_knots)
            knots.extend((self.deep_r-r0+self.cap_width*np.array([.25,.5,.75])).tolist())
            args.metric_knots=json.dumps(sorted(set(knots)));args.metric_modes=100
        if args.height_knots=='segments':
            r0=json.loads(args.trace.read_text())['r']
            ks=[v['r']-r0 for v in raw['rows'] if v['x'] in (0,1)]
            ks.extend(json.loads(args.metric_knots));ks.extend([.001,.003])
            ks.extend(self.deep_r-r0+self.cap_width*np.linspace(0,1,5))
            args.height_knots=json.dumps(sorted(set(ks)))
        super().__init__(args)
        self.optimizer_source_sha=self.source_sha
        self.source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        truejets=self.hjets+self.h0mean[:,None];truealpha=self.alpha0.copy();truexy=self.xy0.copy()
        true_phi=self.hpj.copy();true_pp=self.hppj.copy()
        trueFr=self.true_Fr0.copy();trueFrr=self.true_Frr0.copy()
        hm=mode_api.HeightModes(args.accepted_state,args.background,mean_anchor=args.accepted_mean_anchor)
        self.accepted_source_sha=hashlib.sha256(args.accepted_state.read_bytes()).hexdigest()
        self.height_api_sha=hm.source_sha256
        self.finite_frequency=hm.frequency
        f=hm.frequency;co=np.cos(self.theta[:,None]*f);si=np.sin(self.theta[:,None]*f)
        rf=2*np.arange(1,len(self.trace['rho_cos_coefficients'])+1)
        rhop=-np.sin(self.phi[:,None]*rf)@(rf*np.array(self.trace['rho_cos_coefficients']))
        def values(v):
            H=v['h0'][:,None]+v['C']@co.T;Hr=v['h0r'][:,None]+v['Cr']@co.T
            Hrr=v['h0rr'][:,None]+v['Crr']@co.T
            Hp=-self.rho[None,:]*((v['C']*f)@si.T)
            Hrp=-self.rho[None,:]*((v['Cr']*f)@si.T)
            Hpp=-self.rho[None,:]**2*((v['C']*f*f)@co.T)-rhop[None,:]*((v['C']*f)@si.T)
            return H,Hr,Hrr,Hp,Hrp,Hpp
        inside=self.flat_r<=self.deep_r
        cut_coeff=hm.at_r([self.r0]);end_coeff=hm.at_r([self.deep_r])
        val=values(hm.at_r(self.flat_r[inside]));cut=values(cut_coeff);end=values(end_coeff)
        # The arbitrary vertical origin is chosen to match the true cut mean.
        shift=truejets[0].mean()-cut[0][0].mean()
        for target in (val,cut,end):target[0][:]+=shift
        self.vertical_shift=float(shift)
        arrays=[np.empty((len(self.flat_r),self.N)) for _ in range(6)]
        for target,source in zip(arrays,val):target[inside]=source
        u=(self.flat_r[~inside]-self.deep_r)/self.cap_width
        deep_mean=float(hm.at_r([self.deep_r])['h0'][0]+shift)
        ext=flat.height_jets(u,width=self.cap_width,w0=w0,w1=w1,mean_height=deep_mean,
            hb=end[0][0],hrb=end[1][0],hrrb=end[2][0],lift=A)
        for index,key in enumerate(('h','hr','hrr')):arrays[index][~inside]=ext[key]
        def mode_first(c):return -self.rho*(si@(f*c))
        def mode_second(c):return -self.rho**2*(co@(f*f*c))-rhop*(si@(f*c))
        deep_angular=[end[3][0],end[4][0],mode_first(end_coeff['Crr'][0])]
        deep_second=[end[5][0],mode_second(end_coeff['Cr'][0]),mode_second(end_coeff['Crr'][0])]
        # Each angular derivative is of the same finite height formula.
        arrays[3][~inside]=0.;arrays[4][~inside]=0.;arrays[5][~inside]=0.
        for j in range(3):
            p=np.polynomial.polynomial.polyval(u,flat.P[j])*d**j
            pr=np.polynomial.polynomial.polyval(u,np.polynomial.polynomial.polyder(flat.P[j]))*d**(j-1)
            arrays[3][~inside]+=p[:,None]*deep_angular[j]
            arrays[4][~inside]+=pr[:,None]*deep_angular[j]
            arrays[5][~inside]+=p[:,None]*deep_second[j]
        weak=np.array([v[0] for v in cut[:3]])
        tau=args.cut_fraction
        if not 0<=tau<=1:raise ValueError('cut_fraction must be in [0,1]')
        weak_phi=np.array([cut[3][0],cut[4][0],mode_first(cut_coeff['Crr'][0])])
        weak_pp=np.array([cut[5][0],mode_second(cut_coeff['Cr'][0]),mode_second(cut_coeff['Crr'][0])])
        target=(1-tau)*weak+tau*truejets
        target_phi=(1-tau)*weak_phi+tau*true_phi;target_pp=(1-tau)*weak_pp+tau*true_pp
        mean_residual=None
        if 0<tau<1:
            target[1],target[2],mean_residual=self.compatible_cut(target[0],target[1],target_phi[0],target_pp[0])
            target_phi[2]=direct.base.derivative(target[2],axis=0)
            target_pp[2]=direct.base.derivative(target_phi[2],axis=0)
        delta=target-weak;dphi=target_phi-weak_phi;dpp=target_pp-weak_pp
        self.base_H=arrays[0]+self.base[0]@delta
        self.base_hr=arrays[1]+self.base[1]@delta
        self.base_hrr=arrays[2]+self.base[2]@delta
        self.base_hp=arrays[3]+self.base[0]@dphi
        self.base_hrp=arrays[4]+self.base[1]@dphi
        self.base_hpp=arrays[5]+self.base[0]@dpp
        self.h0mean=target.mean(axis=1);self.hjets=target-self.h0mean[:,None]
        self.hpj=target_phi;self.hppj=target_pp
        # This offset makes the reported final height belong to this base field.
        cap_end=flat.height_jets(np.array([1.]),width=d,w0=w0,w1=w1,mean_height=deep_mean,
            hb=end[0][0],hrb=end[1][0],hrrb=end[2][0],lift=A)
        self.base_increment_offset=float(cap_end['h'].mean()-self.h0mean[0]-np.sum(self.width[:,None]*self.gw*self.w.reshape(self.r.shape)))
        initial=direct.angular.reconstruct_slice(r=self.r0,w=self.trace['w'],wr=self.trace['w_r'],
            h=target[0],hr=target[1],hrr=target[2],h_phi=self.hpj[0],h_phiphi=self.hppj[0],
            hr_phi=self.hpj[1],hr_phiphi=self.hppj[1],rho=self.rho,rho_phi=rhop)
        self.alpha0=initial['alpha'];self.xy0=initial['F'][:,:2]
        fake=[]
        for row in target:
            vector=np.zeros((self.N,3));vector[:,2]=row;fake.append((vector,None,None))
        if tau==1:
            self.alpha0=truealpha;self.xy0=truexy;self.true_Fr0=trueFr;self.true_Frr0=trueFrr
        self._initial_correction(fake)
        if tau!=1:
            self.true_Fr0=self.constructed_Fr0;self.true_Frr0=self.constructed_Frr0;self._initial_correction(fake)
        u=np.clip(self.x/self.join_width,0,1);mask=self.x<self.join_width
        ch=(1-10*u**3+15*u**4-6*u**5)*mask
        cp=(-30*u*u+60*u**3-30*u**4)/self.join_width*mask
        cpp=(-60*u+180*u*u-120*u**3)/self.join_width**2*mask
        self.correct_Frr=(2*cp+self.x*cpp)[:,None,None]*self.delta_Fr+(ch+2*self.x*cp+.5*self.x*self.x*cpp)[:,None,None]*self.delta_Frr
        self.homotopy=dict(cut_fraction=tau,accepted_source_scale=args.accepted_scale,
            mean_turn_residual=float(initial['mean_turn_error']),compatible_cut_mean=mean_residual,
            original_prefix_jets=(tau==1),initial_Fr_correction=float(abs(self.delta_Fr).max()),
            initial_Frr_correction=float(abs(self.delta_Frr).max()),
            scope='Only cut_fraction=1 has the true prefix jets; intermediate cuts are optimization data')
        self.actual_modes=hm;self.material_cos=co;self.material_sin=si;self.rho_phi=rhop
        self.cut_delta=delta;self.cut_delta_phi=dphi;self.cut_delta_phiphi=dpp
        self.deep_height_arrays=[v[0].copy() for v in end[:3]]
        self.deep_height_phi=np.array(deep_angular);self.deep_height_phiphi=np.array(deep_second)
        self.deep_reference_mean=deep_mean;self._primitive_cache=None
        deepA=direct.base.boundary_fundamentals(np.array([self.deep_r-self.r0]),self.L,args.decay_length)
        self.deep_base_height=end[0][0]+(deepA[0]@delta)[0]
        self.deep_B=self.spline(self.deep_r-self.r0)[self.free]
        self.deep_Bend=float(self.spline(self.deep_r-self.r0)[-3:].sum())
        self.cut_height=target[0].copy()
        print(json.dumps(dict(event='literal-accepted-base',seconds=time.perf_counter()-started,
            cut_fraction=tau,panels=self.nc,variables=self.n,vertical_shift=self.vertical_shift,
            initial_turn=self.homotopy['mean_turn_residual'])),flush=True)

    def compatible_cut(self,h,hr_guess,hp,hpp):
        r=self.r0;w=self.trace['w'];wr=self.trace['w_r'];z=w*w;E=1+z
        rp=direct.base.derivative(self.rho,axis=0)
        P=hp/(r*w*self.rho);T=hpp/(r*w*self.rho**2)-hp*rp/(r*w*self.rho**3)
        perpendicular=hr_guess-hr_guess.mean();Kbar=perpendicular/w;c=hr_guess.mean()/w-1
        for iteration in range(40):
            K=Kbar+c;S=1-z*P*P;A=2*K+K*K+E*P*P;D=1-z*A;L=1+K+E*T
            if min(S.min(),D.min(),L.min())<=0:raise ValueError('The chosen intermediate cut leaves the local root chart')
            B=A/(np.sqrt(D)*(1+np.sqrt(D)))+(1+K)*T/(S*np.sqrt(D))
            mean=np.mean(self.rho*B);mu=np.mean(self.rho*L/D**1.5)
            if abs(mean)<2e-14:break
            step=-mean/mu
            for shrink in range(35):
                K2=Kbar+c+step;D2=1-z*(2*K2+K2*K2+E*P*P);L2=1+K2+E*T
                if min(D2.min(),L2.min())>0:break
                step*=.5
            c+=step
        K=Kbar+c;V=direct.base.derivative(K,axis=0)/self.rho
        kr=-(wr/w)*(2*K+T)+(E/r*(V-P)**2+(wr/w)*((K+T)**2+z*(2*K*T+T*T-P*P)))/L
        return w*(1+K),wr*(1+K)+w*kr,float(mean)

    def save_design(self,x,cost,finished,optimizer=None):
        super().save_design(x,cost,finished,optimizer)
        report=json.loads(self.args.out.read_text());report['accepted_base']=dict(
            optimizer_source_sha256=self.optimizer_source_sha,height_api_sha256=self.height_api_sha,
            accepted_source_sha256=self.accepted_source_sha,deep_radius=self.deep_r,cap_width=self.cap_width,
            cap_w_coefficients=self.wpolynomial.tolist(),vertical_shift=self.vertical_shift,
            flat_helper_sha256=hashlib.sha256((HERE/'2026-11-17-parallel-geometry-flat-cuff.py').read_bytes()).hexdigest())
        self.args.out.write_text(json.dumps(report,indent=2)+'\n')

    def diagnostics(self,z):
        out=super().diagnostics(z)
        deep_index=int(np.argmin(abs(self.edges-self.deep_r)))
        if abs(self.edges[deep_index]-self.deep_r)>1e-13:raise ValueError('The finite endpoint must be a quadrature edge')
        radial_need=float(np.max(self.r1-np.linalg.norm(z['xy_nodes'][deep_index],axis=1)))
        each_radial=self.r1-np.linalg.norm(z['xy_nodes'][deep_index],axis=1)
        chord_need=float(np.max(np.hypot(each_radial,out['terminal_mean_height']-z['deep_height'])))
        ww=z['w'].reshape(self.r.shape)[deep_index:]
        width=self.width[deep_index:]
        extra=float(np.sum(width[:,None]*self.gw*ww*ww/(np.sqrt(1+ww*ww)+1)))
        available=self.cap_width+extra
        whole_available=float(np.sum(self.width[:,None]*self.gw*np.sqrt(1+z['w'].reshape(self.r.shape)**2)))
        whole_needed=float(np.max(np.hypot(self.r1-np.linalg.norm(self.xy0,axis=1),out['terminal_mean_height']-self.cut_height)))
        out.update(cap_reference_length_extra=extra,cap_maximum_radial_need_extra=radial_need-self.cap_width,
            cap_radial_length_necessary_error=max(0.,(radial_need/available)**2-1),
            cap_maximum_chord_need_extra=chord_need-self.cap_width,
            cap_chord_length_necessary_error=max(0.,(chord_need/available)**2-1),
            whole_reference_length=whole_available,whole_maximum_chord_need=whole_needed,
            whole_chord_length_necessary_error=max(0.,(whole_needed/whole_available)**2-1))
        return out

    def prepare_initial(self,coefficients):
        """Pay the fixed-center chord-height interval using the free end mean.

        This is a geometric feasibility initializer, not an isometry solve.
        The last mean-height basis vanishes before the cap's first quarter, so
        it changes neither the finite-tail endpoint nor its height jets.
        """
        x=np.asarray(coefficients).copy();z=self.reconstruct(x)
        i=int(np.argmin(abs(self.edges-self.deep_r)))
        radial=self.r1-np.linalg.norm(z['xy_nodes'][i],axis=1)
        ww=z['w'].reshape(self.r.shape)
        length=float(np.sum(self.width[i:,None]*self.gw*np.sqrt(1+ww[i:]**2)))
        square=length*length-radial*radial
        if np.min(square)<0:
            print(json.dumps(dict(event='end-height-feasibility',changed=False,reason='Radial length is insufficient')),flush=True);return x
        allowance=np.sqrt(square);lo=float(np.max(z['deep_height']-allowance));hi=float(np.min(z['deep_height']+allowance))
        whole=float(np.sum(self.width[:,None]*self.gw*np.sqrt(1+ww*ww)))
        radial0=self.r1-np.linalg.norm(self.xy0,axis=1);sq0=whole*whole-radial0*radial0
        if np.min(sq0)<0:
            print(json.dumps(dict(event='end-height-feasibility',changed=False,reason='Whole-tail radial length is insufficient')),flush=True);return x
        allow0=np.sqrt(sq0);lo=max(lo,float(np.max(self.cut_height-allow0)));hi=min(hi,float(np.min(self.cut_height+allow0)))
        current=float(self.h0mean[0]+z['height_increment'])
        if lo>hi:
            print(json.dumps(dict(event='end-height-feasibility',changed=False,reason='Chord-height intervals do not intersect',lower=lo,upper=hi)),flush=True);return x
        margin=.05*(hi-lo);desired=float(np.clip(current,lo+margin,hi-margin))
        step=(desired-current)/self.height_scale
        for shrink in range(30):
            trial=x.copy();trial[self.nheight-1]+=step;test=self.reconstruct(trial)
            if np.min(test['D'])>self.args.branch_margin:x=trial;break
            step*=.5
        print(json.dumps(dict(event='end-height-feasibility',changed=bool(step),old_height=current,new_height=current+step*self.height_scale,
            lower=lo,upper=hi,minimum_D=float(test['D'].min()))),flush=True)
        return x

    def atomic_radii(self):
        """All actual base breakpoints plus the new height/metric spline knots."""
        rd=self.actual_modes.reader
        rr=rd.bg.radial(rd.breaks)[0]
        return direct.base.distinct_knots(np.r_[rr,self.r0+self.spline.t,
            self.r0+self.metric_spline.t,self.deep_r,self.r1,self.r0+self.join_width])

    def _base_height_at(self,radii):
        r=np.atleast_1d(np.asarray(radii,dtype=float));inside=r<=self.deep_r
        shape=(len(r),self.N);H,Hr,Hrr,Hp,Hrp,Hpp=(np.empty(shape) for _ in range(6))
        f=self.finite_frequency;co=self.material_cos;si=self.material_sin
        if np.any(inside):
            v=self.actual_modes.at_r(r[inside]);C,Cr,Crr=(v[k] for k in ('C','Cr','Crr'))
            H[inside]=v['h0'][:,None]+C@co.T+self.vertical_shift
            Hr[inside]=v['h0r'][:,None]+Cr@co.T
            Hrr[inside]=v['h0rr'][:,None]+Crr@co.T
            Hp[inside]=-self.rho[None,:]*((C*f)@si.T)
            Hrp[inside]=-self.rho[None,:]*((Cr*f)@si.T)
            Hpp[inside]=-self.rho[None,:]**2*((C*f*f)@co.T)-self.rho_phi[None,:]*((C*f)@si.T)
        if np.any(~inside):
            u=(r[~inside]-self.deep_r)/self.cap_width;d=self.cap_width
            ext=flat.height_jets(u,width=d,w0=self.deep_w,w1=self.deep_wr,
                mean_height=self.deep_reference_mean,hb=self.deep_height_arrays[0],
                hrb=self.deep_height_arrays[1],hrrb=self.deep_height_arrays[2],lift=self.args.cap_lift)
            H[~inside]=ext['h'];Hr[~inside]=ext['hr'];Hrr[~inside]=ext['hrr']
            Hp[~inside]=0.;Hrp[~inside]=0.;Hpp[~inside]=0.
            for j in range(3):
                p=np.polynomial.polynomial.polyval(u,flat.P[j])*d**j
                pr=np.polynomial.polynomial.polyval(u,np.polynomial.polynomial.polyder(flat.P[j]))*d**(j-1)
                Hp[~inside]+=p[:,None]*self.deep_height_phi[j]
                Hrp[~inside]+=pr[:,None]*self.deep_height_phi[j]
                Hpp[~inside]+=p[:,None]*self.deep_height_phiphi[j]
        A=direct.base.boundary_fundamentals(r-self.r0,self.L,self.args.decay_length)
        H+=A[0]@self.cut_delta;Hr+=A[1]@self.cut_delta;Hrr+=A[2]@self.cut_delta
        Hp+=A[0]@self.cut_delta_phi;Hrp+=A[1]@self.cut_delta_phi;Hpp+=A[0]@self.cut_delta_phiphi
        return H,Hr,Hrr,Hp,Hrp,Hpp

    def _metric_at(self,radii,metric):
        r=np.asarray(radii);w0,wr0=self.reference_metric(r)
        B=self.metric_spline(r-self.r0)[:,self.metric_free]
        Br=self.metric_spline(r-self.r0,1)[:,self.metric_free]
        p=B@metric;pr=Br@metric;ep=np.exp(p)
        return w0*ep,ep*(wr0+w0*pr),w0*np.expm1(p),w0,wr0

    def _mean_metric_primitive(self,radii,metric,order=12):
        r=np.atleast_1d(np.asarray(radii));key=(order,np.asarray(metric).tobytes())
        if self._primitive_cache is None or self._primitive_cache[0]!=key:
            edges=direct.base.distinct_knots(np.r_[self.bg.r,self.r0+self.metric_spline.t,self.r1])
            gx,gw=np.polynomial.legendre.leggauss(order);gx=(gx+1)/2;gw=gw/2
            rr=edges[:-1,None]+np.diff(edges)[:,None]*gx
            diff=self._metric_at(rr.ravel(),metric)[2].reshape(rr.shape)
            cell=np.diff(edges)*(diff@gw);prefix=np.r_[0,np.cumsum(cell)]
            self._primitive_cache=(key,edges,gx,gw,prefix)
        _,edges,gx,gw,prefix=self._primitive_cache
        idx=np.clip(np.searchsorted(edges,r,side='right')-1,0,len(edges)-2)
        lo=edges[idx];width=r-lo;rr=lo[:,None]+width[:,None]*gx
        diff=self._metric_at(rr.ravel(),metric)[2].reshape(rr.shape)
        return prefix[idx]+width*(diff@gw)

    def evaluate_height(self,radii,coefficients,*,mean_gauss=12):
        """Literal C2 height and scalar metric at arbitrary physical radii.

        The only numerical primitive here is the scalar integral of the metric
        change. Its derivatives are the exact declared integrand and derivative.
        An independent caller can compare mean_gauss=8/12 without changing h_r.
        No derivatives of a sampled radial interpolation are substituted.
        """
        r=np.atleast_1d(np.asarray(radii,dtype=float))
        if r.min()<self.r0 or r.max()>self.r1:raise ValueError('Radius outside the declared height interval')
        x=np.asarray(coefficients);c=x[:self.nheight-1].reshape(self.M+1,self.nf)*self.height_scale
        end=x[self.nheight-1]*self.height_scale;metric=x[self.nheight:]
        H,Hr,Hrr,Hp,Hrp,Hpp=self._base_height_at(r)
        B=[self.spline(r-self.r0,j)[:,self.free] for j in range(3)]
        Be=[self.spline(r-self.r0,j)[:,-3:].sum(axis=1) for j in range(3)]
        w,wr,dw,w0,wr0=self._metric_at(r,metric)
        coupling=float(self.args.metric_height_coupling)
        primitive=self._mean_metric_primitive(r,metric,mean_gauss) if coupling else np.zeros(len(r))
        H+=(primitive+B[0]@c[0]+Be[0]*end)[:,None]+(B[0]@c[1:].T)@self.C.T
        Hr+=(coupling*dw+B[1]@c[0]+Be[1]*end)[:,None]+(B[1]@c[1:].T)@self.C.T
        Hrr+=(coupling*(wr-wr0)+B[2]@c[0]+Be[2]*end)[:,None]+(B[2]@c[1:].T)@self.C.T
        Hp+=(B[0]@c[1:].T)@self.Cp.T;Hrp+=(B[1]@c[1:].T)@self.Cp.T
        Hpp+=(B[0]@c[1:].T)@self.Cpp.T
        return dict(r=r,w=w,wr=wr,h=H,hr=Hr,hrr=Hrr,h_phi=Hp,hr_phi=Hrp,h_phiphi=Hpp)

    def cartesian_join_correction(self,radii):
        r=np.atleast_1d(np.asarray(radii));x=r-self.r0
        u=np.clip(x/self.join_width,0,1);mask=(x<self.join_width)&(x>=0)
        ch=(1-10*u**3+15*u**4-6*u**5)*mask
        cp=(-30*u*u+60*u**3-30*u**4)/self.join_width*mask
        cpp=(-60*u+180*u*u-120*u**3)/self.join_width**2*mask
        value=(x*ch)[:,None,None]*self.delta_Fr+.5*(x*x*ch)[:,None,None]*self.delta_Frr
        first=(ch+x*cp)[:,None,None]*self.delta_Fr+(x*ch+.5*x*x*cp)[:,None,None]*self.delta_Frr
        second=(2*cp+x*cpp)[:,None,None]*self.delta_Fr+(ch+2*x*cp+.5*x*x*cpp)[:,None,None]*self.delta_Frr
        return dict(value=value,first=first,second=second)

def main(args):
    old=json.loads(args.template.read_text());params=old['parameters']
    for key in ('trace','background','out','input'):
        if params.get(key):params[key]=Path(params[key])
    params.update(accepted_state=args.state,accepted_mean_anchor=args.mean_anchor,accepted_scale=args.accepted_scale,
        cuff_radius=args.cuff_radius,cap_lift=args.cap_lift,cut_fraction=args.cut_fraction,
        out=args.out,input=args.input,modes=args.modes,angles=args.angles,height_knots='segments',
        max_nfev=args.max_nfev,metric_modes=args.metric_modes,gauss=args.gauss,
        actual_curvature_weight=args.actual_curvature_weight,scaling='heuristic',method=args.method,
        log_every=20,freeze_metric=args.freeze_metric,cap_metric_modes=args.cap_metric_modes,
        function_tolerance=args.function_tolerance,cap_length_weight=args.cap_length_weight,
        metric_height_coupling=args.coupled_metric_height)
    params['template']=str(args.template)
    direct.Design=AcceptedBase;direct.main(argparse.Namespace(**params))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--template',type=Path,required=True)
    p.add_argument('--state',type=Path,required=True);p.add_argument('--mean-anchor',type=float,default=.9196724087226285)
    p.add_argument('--accepted-scale',type=float,default=.0014);p.add_argument('--cuff-radius',type=float,default=1.767318285443017)
    p.add_argument('--cap-lift',type=float,default=.048856939517352364);p.add_argument('--cut-fraction',type=float,default=0.)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--input',type=Path)
    p.add_argument('--modes',type=int,default=32);p.add_argument('--angles',type=int,default=512);p.add_argument('--gauss',type=int,default=8)
    p.add_argument('--max-nfev',type=int,default=300);p.add_argument('--metric-modes',type=int,default=5)
    p.add_argument('--actual-curvature-weight',type=float,default=0.);p.add_argument('--freeze-metric',action='store_true')
    p.add_argument('--cap-metric-modes',action='store_true');p.add_argument('--function-tolerance',type=float,default=1e-20)
    p.add_argument('--cap-length-weight',type=float,default=10.)
    p.add_argument('--method',choices=['lbfgs','armijo'],default='armijo')
    p.add_argument('--coupled-metric-height',action='store_true')
    main(p.parse_args())
