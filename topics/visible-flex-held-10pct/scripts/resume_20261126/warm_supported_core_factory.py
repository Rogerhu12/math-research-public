"""Warm R53 baseline plus R52 supported material-phase controls.

The baseline's complete support vector is fixed.  The old positive q input
is ONLY a coordinate carrier: d1 = scale*log(q_aux/gauge_q).  Remaining
legacy support inputs map to d_j=scale*c_input/legacy_pscale.  None is a new
support Fourier coefficient.  The fixed BVP still uses its original
p0=log(q_aux/q_seed); the numerical gauge multiplying Y remains unchanged.

At zero phase controls this object delegates the complete baseline F/Ft/Ftt
literally.  Its position increment is integrated through expm1, hence no
refit or separate approximate baseline reconstruction defines the handoff.
This is a new core family preserving one anchor, not a reversible change
of the old finite support parameter span.  No BVP success is claimed here.
"""
from pathlib import Path
import sys
import math
import numpy as np


def _xyz(value):
    value=np.asarray(value)
    return np.stack((value.real,value.imag,np.zeros_like(value.real)),axis=-1)


class SupportedIncrementCore:
    def __init__(self,baseline,controls,*,input_chain,q_aux,gauge_q):
        self.baseline=baseline
        self.base_mode=baseline.base_mode
        self.period=baseline.period
        self.halfperiod=baseline.halfperiod
        self.halfwidth=baseline.halfwidth
        self.transition=baseline.transition
        self.homotopy=baseline.homotopy
        self.target_curvature=baseline.target_curvature
        self.controls=np.asarray(controls,float)
        self.input_chain=np.asarray(input_chain,float)
        self.coefficients=self.controls.copy()
        self.corrections=tuple(float(v) for v in self.controls[1:])
        self.q=float(q_aux)
        self.support_amplitude=float(q_aux)  # legacy interface label, not support Q
        self.gauge_q=float(gauge_q)
        self.frequencies=self.base_mode*np.arange(1,len(self.controls)+1)
        self.omega=self.frequencies.astype(float)
        self.norms=1.+630./(256.*self.transition*self.omega)
        self._zero=bool(np.all(self.controls==0.))
        self.quadrature_order=baseline.quadrature_order
        self.integration_cells=baseline.integration_cells
        self._gx,self._gw=baseline._gx,baseline._gw
        self._integration_grid=baseline._integration_grid.copy()
        self._last_theta=None
        self._last_value=None
        self._last_jets=None
        self._set_guard()
        increments=self._integrate(self._integration_grid[:-1],self._integration_grid[1:])
        self._cumulative=np.vstack((np.zeros((1,len(self.controls)+1),complex),
                                    np.cumsum(increments,axis=0)))
        origins=self._cumulative[-1]/np.expm1(1j*self.period)
        self.reflection_roundoff=float(np.max(abs(origins.imag)))
        self._origins=origins.real.astype(complex)

    def _basis(self,local):
        local=np.asarray(local,float).reshape(-1)
        _,W,W1,W2,_=self.baseline._window(local)
        t=np.clip((abs(local-self.halfperiod)-self.halfwidth)/self.transition,0.,1.)
        W3=(7560*t*t*(1-t)**2*(1-2*t)**2-5040*t**3*(1-t)**3)
        W3*=np.sign(local-self.halfperiod)/self.transition**3
        w=self.omega[:,None]
        sine,cosine=np.sin(w*local[None,:]),np.cos(w*local[None,:])
        norm=self.norms[:,None]
        phase=W[None,:]*sine/w/norm
        first=(W[None,:]*cosine+W1[None,:]*sine/w)/norm
        second=(2*W1[None,:]*cosine+(W2[None,:]/w-W[None,:]*w)*sine)/norm
        third=((3*W2[None,:]-W[None,:]*w*w)*cosine+
               (W3[None,:]/w-3*W1[None,:]*w)*sine)/norm
        return phase,first,second,third

    def _set_guard(self):
        size=float(np.sum(abs(self.controls)))
        base=self.baseline
        low=base.curvature_lower_bound-size
        high=base.curvature_upper_bound+size
        method="original-baseline-plus-unit-curvature-control-triangle"
        nodes=0
        if low<=1e-5:
            # Same original curvature floor. This is the recorded numerical
            # interpolation guard, not a formal outward interval enclosure.
            if base._bound_provider is None:
                raise FloatingPointError("Warm supported core lacks baseline curvature derivative bounds")
            K1,K2=map(float,base._bound_provider(base.original))
            a,b=1./base.original.rho_upper,1./base.original.rho_lower
            D1=630./(256.*self.transition)
            D2=2520./(64.*self.transition**2)
            D3=(7560./16.+5040./64.)/self.transition**3
            gap=max(abs(a-base.k+base.beta),abs(b-base.k+base.beta))
            bound=K2+2*base.homotopy*D1*K1+base.homotopy*D2*gap
            columns=(3*D2+self.omega**2+D3/self.omega+3*self.omega*D1)/self.norms
            bound+=float(abs(self.controls)@columns)
            allowance=1e-12*(1+base.curvature_upper_bound+size)
            for nodes in (512,1024,2048,4096,8192,16384,32768):
                u=self.period*np.arange(nodes)/nodes
                values=base._phase_fields(u)["kappa"]+self.controls@self._basis(u)[1]
                if float(values.min())<=1e-5:
                    raise FloatingPointError("Warm supported core curvature sample crossed original floor")
                slack=bound*(self.period/nodes)**2/8+allowance
                candidate=max(low,float(values.min())-slack)
                if candidate>1e-5:
                    low,high=candidate,min(high,float(values.max())+slack)
                    method="original-floor-periodic-interpolation"
                    break
            else:
                raise FloatingPointError("Warm supported core curvature positivity unresolved at original ceiling")
        self.curvature_lower_bound=float(low)
        self.curvature_upper_bound=float(high)
        self.rho_lower,self.rho_upper=1./high,1./low
        self.curvature_guard=dict(method=method,lower=low,upper=high,nodes=nodes,
                                  formal_outward_interval_certificate=False)

    def _integrate(self,a,b):
        a,b=np.asarray(a,float).reshape(-1),np.asarray(b,float).reshape(-1)
        u=(a[:,None]+b[:,None])/2+(b-a)[:,None]*self._gx[None,:]/2
        phase=self._basis(u.reshape(-1))[0]
        original=self.baseline._phase_fields(u.reshape(-1))
        old_normal=np.exp(1j*original["phi"])
        change=self.controls@phase
        normal=old_normal*np.exp(1j*change)
        tangent_change=1j*old_normal*np.expm1(1j*change)
        values=np.column_stack((tangent_change,(-normal[None,:]*phase).T))
        values=values.reshape(len(a),self.quadrature_order,len(self.controls)+1)
        return np.einsum("q,nqp->np",self._gw,values)*(b-a)[:,None]/2

    def evaluate(self,theta):
        theta=np.asarray(theta,float)
        if self._last_theta is not None and np.array_equal(theta,self._last_theta):
            return self._last_value
        flat=theta.reshape(-1)
        sector=np.floor(flat/self.period)
        local=flat-sector*self.period
        base=self.baseline.evaluate(flat)
        phase,k,k1,k2=self._basis(local)
        change=self.controls@phase
        kappa=base["kappa"]+self.controls@k
        normal=np.exp(1j*base["phi"])*np.exp(1j*change)
        index=np.clip(np.searchsorted(self._integration_grid,local,side="right")-1,
                      0,len(self._integration_grid)-2)
        integral=self._cumulative[index]+self._integrate(self._integration_grid[index],local)
        increment=(self._origins[None,:]+integral)*np.exp(1j*sector*self.period)[:,None]
        if self._zero:
            # Literal full geometry identity at the real saved anchor.
            F,Ft,Ftt=(base[name].copy() for name in ("F","Ft","Ftt"))
        else:
            F=base["F"]+_xyz(increment[:,0])
            Ft=_xyz(1j*normal)
            Ftt=_xyz(-kappa*normal)
        value=dict(F=F.reshape(theta.shape+(3,)),Ft=Ft.reshape(theta.shape+(3,)),
            Ftt=Ftt.reshape(theta.shape+(3,)),phi=(base["phi"]+change).reshape(theta.shape),
            kappa=kappa.reshape(theta.shape),
            kappa_u=(base["kappa_u"]+self.controls@k1).reshape(theta.shape),
            kappa_uu=(base["kappa_uu"]+self.controls@k2).reshape(theta.shape),
            arc_residual=np.zeros_like(theta),arc_iterations=0)
        d0=_xyz(increment[:,1:].T)
        d1=_xyz(-normal[None,:]*phase)
        d2=_xyz(-normal[None,:]*(k+1j*kappa[None,:]*phase))
        self._last_jets=tuple(v*self.input_chain[:,None,None] for v in (d0,d1,d2))
        self._last_theta=theta.copy();self._last_value=value
        return value

    def parameter_derivatives(self,theta):
        self.evaluate(theta)
        return self._last_jets[0]

    def jet_parameter_derivatives(self,theta):
        self.evaluate(theta)
        return self._last_jets

    def rho_material_jets(self,theta):
        values=self.evaluate(theta)
        k,k1,k2=(values[name] for name in ("kappa","kappa_u","kappa_uu"))
        return 1/k,-k1/k**2,2*k1*k1/k**3-k2/k**2

    def summary(self):
        return dict(core_kind="warm-supported-material-phase",base_mode=self.base_mode,
            homotopy=self.homotopy,halfwidth=self.halfwidth,transition=self.transition,
            target_curvature=self.target_curvature,exact_arc_reached=self.homotopy==1.,
            physical_phase_controls=self.controls.tolist(),
            baseline_support_coefficients=self.baseline.original.coefficients.tolist(),
            baseline_core_settings=self.baseline.summary(),
            gauge_q=self.gauge_q,q_aux=self.q,
            phase_control_scale=self.phase_control_scale,
            inherited_auxiliary_q_domain=[1e-7,.124],
            q_aux_meaning="positive numerical coordinate only; d1=scale*log(q_aux/gauge_q)",
            correction_meaning="supported material phase controls d2...dM; not support Fourier coefficients",
            input_parameter_chain=self.input_chain.tolist(),
            zero_controls_literal_geometry_identity=self._zero,
            curvature_guard=self.curvature_guard,exact_perimeter=2*math.pi,
            scope="New family anchored at actual R53 geometry; not the old finite span or an accepted BVP")


def make_factory(settings,reference_class=None,anchor_baseline=None):
    settings=dict(settings)
    gauge=float(settings["gauge_q"])
    scale=float(settings.get("phase_control_scale",1.))
    if not 0<gauge<.124 or not math.isfinite(scale) or scale<=0:
        raise ValueError("Valid original gauge and positive phase coordinate scale required")
    old_parameters=np.asarray(settings["anchor_support_coefficients"],float)
    options=dict(settings["anchor_core_settings"])
    if options.get("curvature_blend")!=1. or not 0<float(options.get("homotopy",0))<=1:
        raise ValueError("The warm baseline must be a positive-lambda R53 fixed-target core")
    if reference_class is None:
        reference_class=__import__("fixed_metric_mode3_core").PlanarSupportCore
        if not hasattr(reference_class,"normal_geometry"):
            raise ValueError("Supply the genuine original support reference, not a stacked factory")
    if anchor_baseline is None:
        sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"resume_transfer"))
        from material_flattened_support_core import make_factory as original_factory
        anchor_baseline=original_factory(reference_class,options)(old_parameters[0],old_parameters[1:],3)
    else:
        if not np.array_equal(anchor_baseline.original.coefficients,old_parameters):
            raise ValueError("Live anchor support coefficients differ")
        if anchor_baseline.homotopy!=options["homotopy"]:
            raise ValueError("Live anchor lambda differs")

    class ConfiguredCore(SupportedIncrementCore):
        def __init__(self,q,corrections=(),base_mode=3):
            if base_mode!=3:
                raise ValueError("This first warm handoff is the original mode3 core")
            legacy=np.asarray(corrections,float)
            if not np.isfinite(q) or q<=0:
                raise FloatingPointError("Positive auxiliary coordinate required")
            legacy_scales=np.maximum(gauge**np.arange(2,len(legacy)+2),1e-10)
            physical=np.r_[scale*math.log(float(q)/gauge),scale*legacy/legacy_scales]
            chain=np.r_[scale/float(q),scale/legacy_scales]
            super().__init__(anchor_baseline,physical,input_chain=chain,q_aux=q,gauge_q=gauge)
            self.phase_control_scale=scale

    ConfiguredCore.anchor_definition=settings
    ConfiguredCore.baseline=anchor_baseline
    return ConfiguredCore
