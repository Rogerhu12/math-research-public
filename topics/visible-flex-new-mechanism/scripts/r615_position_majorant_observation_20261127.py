#!/usr/bin/env python3
"""R615 same-field position-majorant accumulator for a future real scope.

Consume the coefficient/root arrays already formed by a R606 rho pass; do
not repeat that pass, call geometry, compute a seed, or start an optimizer.
All returned bounds assume the floating radial coefficients/point values
are exact. This assumption is explicit and is not a continuous certificate.
"""
import numpy as np


class PositionMajorant:
    def __init__(self,data,state,maximum_odd_mode=127):
        self.r=np.asarray(data["r"])
        self.nt=len(data["theta"])
        K=int(maximum_odd_mode)
        if self.nt%4 or K<1 or K%2!=1 or 2*K>=self.nt:
            raise ValueError("R615 requires 4|N and positive odd K<N/2")
        self.modes=np.arange(1,K+1,2,dtype=int)
        self.K=K
        theta=np.asarray(data["theta"])
        S=state["g"]["Wstar"]/np.sqrt(state["g"]["E"])[:,:,None]
        self.cx=2*(S[:,:,0]@np.cos(self.modes[:,None]*theta).T)/self.nt
        self.sy=2*(S[:,:,1]@np.sin(self.modes[:,None]*theta).T)/self.nt
        self.measured_sum=np.sum(np.maximum(abs(self.cx),abs(self.sy)),axis=1)
        # R504 §5.1, same real primitive with constant/Nyquist zero.
        # Floating evaluation remains conditional, not directed rounding.
        self.primitive_linf_bound=np.pi/np.sqrt(3.)
        self.best=np.full(len(self.r),np.inf)
        self.best_details=[None]*len(self.r)
        self.per_rho=[]
        self.counts={"same_actual_position_radial_angular_points":int(S.shape[0]*S.shape[1]),
            "same_actual_position_odd_coefficients":int(self.cx.size+self.sy.size),
            "consumed_existing_R606_rho_radial_points":0,
            "new_seed_ODE_geometry_or_original_gate_calls":0}

    def update(self,rho,valid,*,b_square_ratio_bound,N_norm,N_lower,
               shift_norm,e_lower,e_upper,root_radius,G_norm,G_e_norm,background_W):
        """Consume one existing R606 pass, without recomputing its inputs.

Every argument except rho is an array on the identical self.r. `valid`
must already contain the R606 tanh, denominator and turning-root checks.
All arrays have the actual model's already charged floating identity.
"""
        self.counts["consumed_existing_R606_rho_radial_points"]+=len(self.r)
        rho=float(rho)
        valid=np.asarray(valid,dtype=bool).copy()
        if rho<=0:
            raise ValueError("positive Wiener radius required")
        x,n,s=np.asarray(b_square_ratio_bound),np.asarray(N_norm),np.asarray(shift_norm)
        em,ep,d=np.asarray(e_lower),np.asarray(e_upper),np.asarray(root_radius)
        G,L=np.asarray(G_norm),np.asarray(G_e_norm)
        W=np.asarray(background_W)
        nlower=np.asarray(N_lower)
        gap=em-s
        valid&=(gap>0)&(x<1)&(x>=0)&(nlower>0)&(em+W*W>0)
        g=np.where(valid,gap,1.)
        xx=np.where(valid,x,0.)
        energy=np.where(valid,em+W*W,1.)
        with np.errstate(over="ignore",invalid="ignore",divide="ignore"):
            A=n/np.sqrt(g)
            omega=n/g**1.5
            wminus=nlower/(ep+s)**1.5
            B=self.r*(2-np.sqrt(1-xx))
            T=np.exp(rho+A/2)
            Rnorm=2*omega*G
            Qnorm=B*T*Rnorm/2
            Snorm=Qnorm/np.sqrt(energy)
            LS=(B*T/np.sqrt(energy)
                *(omega*L+3*omega*G/g+omega*omega*G/4)
                +Snorm/(2*energy))
            even_alias=(.5+2/self.nt)*np.exp(-self.nt*rho/2)
            odd_alias=(1+2/self.nt)*np.exp(-self.nt*rho/2)
            eps_mu=2*np.exp(-self.nt*rho)*omega*G/wminus
            eps_phi=even_alias*A
            eps_p=even_alias*Rnorm+self.primitive_linf_bound*omega*eps_mu
            eps_S=(odd_alias*Qnorm+self.primitive_linf_bound*self.r
                *(eps_p+(Rnorm/2)*eps_phi))/np.sqrt(energy)
            primitive_error=2*len(self.modes)*eps_S
            fourier_alias=Snorm*np.sum(np.exp(-(self.nt-self.modes)*rho))
            root_error=d*LS*np.sum(np.exp(-self.modes*rho))
            tail=Snorm*np.exp(-(self.K+2)*rho)
            delta=self.measured_sum+primitive_error+fourier_alias+root_error+tail
            eta=(1+np.sqrt(2))*delta+delta*delta
        valid&=np.isfinite(eta)&np.isfinite(Snorm)&np.isfinite(LS)&(eta>=0)
        indices=np.flatnonzero(valid)
        worst=None
        if len(indices):
            i=int(indices[np.argmax(eta[indices])])
            worst={"r":float(self.r[i]),"conditional_eta":float(eta[i])}
        self.per_rho.append({"rho":rho,"radial_points":len(self.r),
            "defined_radii":int(np.sum(valid)),"unresolved_radii":int(np.sum(~valid)),
            "worst_defined_conditional_eta":worst})
        for i in np.flatnonzero(valid&(eta<self.best)):
            self.best[i]=eta[i]
            self.best_details[i]={"r":float(self.r[i]),"rho":rho,
                "conditional_delta_S":float(delta[i]),"conditional_eta":float(eta[i]),
                "measured_sum_of_maximum_position_component_coefficients":float(self.measured_sum[i]),
                "both_discrete_primitives_and_weighted_mean_error":float(primitive_error[i]),
                "position_coefficient_Fourier_alias":float(fourier_alias[i]),
                "continuous_turning_root_shift":float(root_error[i]),
                "formal_position_Wiener_tail":float(tail[i]),
                "complex_position_Wiener_norm":float(Snorm[i]),
                "complex_position_root_derivative_Wiener_norm":float(LS[i]),
                "inner_and_outer_primitive_node_error":float(eps_S[i]),
                "discrete_weighted_mean_error":float(eps_mu[i]),
                "phase_node_error":float(eps_phi[i]),"radial_energy_lower":float(energy[i])}

    def finish(self):
        valid=np.isfinite(self.best)
        worst=None
        if np.any(valid):
            indices=np.flatnonzero(valid)
            i=int(indices[np.argmax(self.best[indices])])
            worst=self.best_details[i]
        missing=np.flatnonzero(~valid)
        return {"schema":"r615-same-field-floating-position-majorant-observation-v1",
            "radial_points":len(self.r),"angular_points":self.nt,
            "maximum_observed_odd_mode":self.K,"next_omitted_odd_mode":self.K+2,
            "primitive_matrix_linf_bound":float(self.primitive_linf_bound),
            "per_rho":self.per_rho,"unresolved_radius_count":int(len(missing)),
            "first_unresolved_radii":[float(self.r[i]) for i in missing[:12]],
            "defined_at_every_sampled_radius":bool(np.all(valid)),
            "worst_best_rho_conditional_majorant":worst,
            "same_actual_position_and_original_primitive_matrix":True,
            "consumes_R606_coefficients_without_repeating_its_pass":True,
            "both_finite_primitive_aliases_weighted_mean_and_root_shift_retained":True,
            "zero_point_value_DtN_ODE_core_integral_roundoff_errors_assumed":True,
            "continuous_radial_metric_or_reach_certificate":False,
            "not_an_extra_acceptance_gate_or_previous_run_probe":True,
            "counts":dict(self.counts)}
