#!/usr/bin/env python3
"""Candidate direct-metric representation with an independent radial height.

Only --check-only is exposed. This file neither evaluates research candidates
nor chooses an optimizer, objective weight, step size or solve budget. The
reference b0 is the exact angular mean of one immutable natural-cap c0 field;
its finite GH/angular/radial rules are evaluation settings, not its identity.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np

from frame_collar_bvp import (RadialBasis,periodic_operator,radial_quadrature,
    smooth_positive,atomic_save,FrameCollarProblem,EllipticCylinderPort,NegativeKRadialSeed)
from frame_collar_bent_tail import artificial_enriched_report,load_enriched_report
from frame_collar_enriched import make_enriched
from frame_collar_natural_body_audit import NaturalBodyProblem,implementation_hashes as natural_hashes
from frame_collar_residual_audit import digest,exact_binary64


class HeightBasis:
    """Quintic B splines with cubic endpoint zeros and one global primitive."""
    def __init__(self,seed,count=9):
        self.count=int(count)
        if self.count<1:raise ValueError('positive radial height dimension required')
        self.left_exact=seed.length_exact*seed.core_fraction_exact
        self.right_exact=seed.length_exact*(1-seed.flat_fraction_exact)
        self.left=float(self.left_exact);self.right=float(self.right_exact)
        self.basis=RadialBasis(self.count,self.left,self.right)
        self.antiderivative=self.basis.full.antiderivative()
        self.primitive_at_left=self.antiderivative(self.left)[3:-3]
        interior=[self.left_exact+(self.right_exact-self.left_exact)*Q(j,self.count+1)
                  for j in range(1,self.count+1)]
        self.identity={'schema':'independent-center-speed-quintic-basis-v1',
            'interval_exact':[str(self.left_exact),str(self.right_exact)],
            'degree':5,'free_count':self.count,
            'clamped_knots_exact':[str(self.left_exact)]*6+[str(x) for x in interior]+[str(self.right_exact)]*6,
            'retained_columns':'3 through count+2 inclusive; discard first and last three',
            'zero_extension_of_speed_basis_outside_interval':True,
            'cubic_zero_at_both_ends_preserves_speed_value_first_and_second_derivatives':True,
            'primitive':'I_j(t)=integral_0^t C_j(s) ds; one constant continuation after the interval',
            'no_fifth_order_endpoint_weight_added':True}
        self.identity_sha256=digest(self.identity)

    def evaluate(self,radial,order=0):
        return self.basis.evaluate(np.asarray(radial,float),order)

    def integral(self,radial):
        t=np.asarray(radial,float)
        return self.antiderivative(np.clip(t,self.left,self.right))[...,3:-3]-self.primitive_at_left


def tangent_parameter_jets(grid,fields,frame,name,order=2):
    """Analytic parameter columns for T, T_s, T_theta and optionally T_ss."""
    B=grid.basis_jacobian(name);Bs=grid.basis_jacobian(name,'s');Bt=grid.basis_jacobian(name,'theta')
    part=frame['Tpart'][name]
    result={'T':part[...,None]*B[:,:,None,:],
        'Ts':frame['Ts_value_part'][name][...,None]*B[:,:,None,:]+part[...,None]*Bs[:,:,None,:]}
    v=fields['v']['value'];psi=fields['_theta']+fields['u']['value']
    H=np.stack((-np.sin(psi),np.cos(psi),np.zeros_like(v)),axis=-1)
    N=np.stack((np.cos(psi),np.sin(psi),np.zeros_like(v)),axis=-1)
    ez=np.zeros_like(H);ez[...,2]=1.
    c=1/np.sqrt(1+v*v);cv=-v*c**3;cvv=(2*v*v-1)*c**5
    dv=c**3;dvv=-3*v*c**5
    Tuu=-c[...,None]*H;Tuv=-cv[...,None]*N
    Tvv=cvv[...,None]*H+dvv[...,None]*ez
    pt=1+fields['u']['theta'];vt=fields['v']['theta']
    value_theta=(pt[...,None]*Tuu+vt[...,None]*Tuv) if name=='u' else (pt[...,None]*Tuv+vt[...,None]*Tvv)
    result['Ttheta']=value_theta[...,None]*B[:,:,None,:]+part[...,None]*Bt[:,:,None,:]
    if order<2:return result
    us,vs,uss,vss=(fields[a][b] for a,b in [('u','s'),('v','s'),('u','ss'),('v','ss')])
    A=-c*us*us+cvv*vs*vs+cv*vss
    Bn=-2*cv*us*vs-c*uss
    if name=='u':
        value=Bn[...,None]*H-A[...,None]*N
        first=(-2*c*us)[...,None]*H+(-2*cv*vs)[...,None]*N
    else:
        cvvv=3*v*(3-2*v*v)*c**7;dvvv=3*(4*v*v-1)*c**7
        value=((-cv*us*us+cvvv*vs*vs+cvv*vss)[...,None]*H+
               (-2*cvv*us*vs-cv*uss)[...,None]*N+
               (dvvv*vs*vs+dvv*vss)[...,None]*ez)
        first=(2*cvv*vs)[...,None]*H+(-2*cv*us)[...,None]*N+(2*dvv*vs)[...,None]*ez
    Bss=np.einsum('ri,tk->rtik',grid.bases[2],grid.angular[name]).reshape(len(grid.radial),len(grid.theta),-1)
    result['Tss']=value[...,None]*B[:,:,None,:]+first[...,None]*Bs[:,:,None,:]+part[...,None]*Bss[:,:,None,:]
    return result


class IndependentHeightProblem:
    """Natural T(u,v), immutable mean-height base, independent b controls.

    The source NaturalBodyProblem is only a scalar-field/basis provider. Its
    evolving auxiliary V and its old center integral are never used here.
    """
    def __init__(self,source,height_free=9,*,height_angular_nodes=384,
                 frozen_metric_definition=None):
        self.source=source;self.port=source.port;self.seed=source.seed;self.tail=source.tail
        self.height_basis=HeightBasis(self.seed,height_free);self.height_free=self.height_basis.count
        self.height_angular_nodes=int(height_angular_nodes)
        if self.height_angular_nodes<4 or self.height_angular_nodes%4:
            raise ValueError('height mean grid must have a positive multiple-of-four size')
        self.height_theta=np.arange(self.height_angular_nodes)*2*np.pi/self.height_angular_nodes
        self.height_cache={};self.body_metric=source.body_metric
        self.metric_free=self.body_metric.count if frozen_metric_definition is None else 0
        self.fixed_metric=None if frozen_metric_definition is None else self.body_metric.replay_coefficients(frozen_metric_definition)
        self._reset_layout()
        self.anchor_latent=np.zeros(source.nunknown)
        self.anchor_latent[:source.field_count]=source.source_state
        self.anchor_latent.setflags(write=False)
        self.height_base_definition={'schema':'immutable-natural-c0-angular-mean-height-v1',
            'source_model_definition':source.model_definition(),
            'source_model_definition_sha256':digest(source.model_definition()),
            'source_c0_exact':[str(Q.from_float(float(x))) for x in source.source_state],
            'height_speed':'b0(t)=angular_mean[-sin(beta0(t,theta))/sqrt(1+v0(t,theta)^2)]',
            'source_fields':'the immutable natural-cap field at original c0, with zero body metric controls',
            'angular_mean_is_the_exact_full_circle_integral':True,
            'heat_source_is_the_same_infinite_Gaussian_definition':True,
            'current_u_v_height_and_metric_parameters_do_not_change_b0':True}
        self.ball_radius=source.ball_radius;self.strip_half_width=source.strip_half_width
        self.shape_weight=source.shape_weight

    def _reset_layout(self):
        self.slices={};offset=0
        for name in ['u','v']:
            count=self.source.slices[name].stop-self.source.slices[name].start
            self.slices[name]=slice(offset,offset+count);offset+=count
        self.tangent_count=offset
        self.slices['height']=slice(offset,offset+self.height_free);offset+=self.height_free
        self.slices['metric']=slice(offset,offset+self.metric_free);self.nunknown=offset+self.metric_free

    def initial_state(self):
        return np.r_[self.source.source_state[self.source.slices['u']],
                     self.source.source_state[self.source.slices['v']],
                     np.zeros(self.height_free+self.metric_free)]

    def latent_state(self,state):
        state=np.asarray(state,float)
        if state.shape!=(self.nunknown,) or not np.all(np.isfinite(state)):
            raise ValueError('finite independent-height coefficient vector required')
        latent=self.anchor_latent.copy()
        for name in ['u','v']:latent[self.source.slices[name]]=state[self.slices[name]]
        return latent

    def metric_coefficients(self,state):
        return np.asarray(state[self.slices['metric']],float) if self.metric_free else self.fixed_metric

    def metric(self,state,radial,jacobian=False):
        answer=self.body_metric.evaluate(self.metric_coefficients(state),radial,jacobian)
        if jacobian and not self.metric_free:
            for name in ['jac_a','jac_as','jac_ass','jac_K']:answer[name]=np.zeros((len(radial),0))
        return answer

    def metric_model(self,state):
        return self.body_metric.frozen_definition(self.metric_coefficients(state),designed=bool(self.metric_free))

    def frozen_metric_copy(self,state):
        result=copy.copy(self)
        result.fixed_metric=self.body_metric.replay_coefficients(self.metric_model(state))
        result.metric_free=0;result._reset_layout()
        coefficient=np.r_[state[self.slices['u']],state[self.slices['v']],state[self.slices['height']]]
        if result.metric_model(coefficient)['mathematical_definition_sha256']!=self.metric_model(state)['mathematical_definition_sha256']:
            raise ArithmeticError('freezing the metric changed its exact definition')
        return result,coefficient

    def height_baseline(self,radial):
        t=np.asarray(radial,float)
        if t.ndim!=1:raise ValueError('one-dimensional radial samples required')
        key=t.tobytes()
        if key in self.height_cache:return self.height_cache[key]
        grid=self.source.grid_for(t,self.height_theta);fields=grid.fields(self.anchor_latent)
        v,beta=(fields[name]['value'] for name in ['v','beta'])
        vs,bs=(fields[name]['s'] for name in ['v','beta'])
        vss,bss=(fields[name]['ss'] for name in ['v','beta'])
        c=1/np.sqrt(1+v*v);cs=-v*c**3*vs
        css=(2*v*v-1)*c**5*vs*vs-v*c**3*vss
        S,C=np.sin(beta),np.cos(beta)
        b=-S*c;first=-C*bs*c-S*cs
        second=S*bs*bs*c-C*bss*c-2*C*bs*cs-S*css
        answer={'b0':b.mean(axis=1),'b0_s':first.mean(axis=1),'b0_ss':second.mean(axis=1)}
        self.height_cache[key]=answer
        return answer

    def height_jets(self,state,radial):
        base=self.height_baseline(radial);coefficient=state[self.slices['height']]
        return {'b':base['b0']+self.height_basis.evaluate(radial)@coefficient,
                'b_s':base['b0_s']+self.height_basis.evaluate(radial,1)@coefficient,
                'b_ss':base['b0_ss']+self.height_basis.evaluate(radial,2)@coefficient}

    def identity(self,state):
        return {'schema':'independent-center-speed-direct-metric-frame-v1',
            'source_T_scalar_family':self.source.space_definition(),
            'current_tangent_free_columns':'only original u and v; no variable auxiliary beta',
            'reference_beta_used_only_inside_the_immutable_height_base':True,
            'height_base_definition':self.height_base_definition,
            'height_basis_definition':self.height_basis.identity,
            'body_metric_definition':self.metric_model(state)['mathematical_definition'],
            'core_identity':self.port.identity,'port_identity':self.port.port_identity,
            'tail_identity':self.tail.identity,
            'height_anchor':{'z0':'side*core_half_width','one_global_integral':True,
                'tail_height':'side*z(L), no radial-row refitting'},
            'exact_coefficients':{name:[str(Q.from_float(float(x))) for x in state[self.slices[name]]]
                                  for name in ['u','v','height']},
            'evaluation_rules_do_not_enter_this_identity':True,
            'not_asserted_to_contain_all_old_finite_beta_height_functions':True,
            'no_isometry_embedding_or_reach_claim':True}

    def evaluation_definition(self):
        return {'source_GH_order':self.source.heat_order,
            'height_mean_angular_nodes':self.height_angular_nodes,
            'height_mean_angles':'fixed uniform [0,2pi) grid independent of query theta',
            'height_control_integral':'same clamped BSpline antiderivative evaluated in binary64',
            'reference_height_integral':'radial Gauss rule anchored at t=0; order specified per geometry call',
            'no_continuous_quadrature_error_bound':True}

    def evaluation_variant(self,state,*,heat_order=None,height_angular_nodes=None):
        source=self.source if heat_order is None else self.source.evaluation_variant(heat_order,self.anchor_latent)
        frozen=None if self.metric_free else self.metric_model(state)
        variant=IndependentHeightProblem(source,self.height_free,
            height_angular_nodes=self.height_angular_nodes if height_angular_nodes is None else height_angular_nodes,
            frozen_metric_definition=frozen)
        if variant.identity(state)!=self.identity(state):raise ArithmeticError('evaluation refinement changed the physical state')
        return variant

    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,full_two_jet_jacobian=False):
        t=np.asarray(radial,float);theta=np.asarray(theta,float);state=np.asarray(state,float)
        if t.ndim!=1 or len(t)<2 or t[0]!=0 or np.any(np.diff(t)<=0):
            raise ValueError('one global position chart must start at zero with strictly increasing radial nodes')
        if theta.ndim!=1 or len(theta)<4 or len(theta)%4:
            raise ValueError('full-period angular grid with a positive multiple-of-four size required')
        expected=theta[0]+np.arange(len(theta))*2*np.pi/len(theta)
        if not np.allclose(theta,expected,rtol=0,atol=128*np.finfo(float).eps*max(1.,np.max(abs(theta)))):
            raise ValueError('FFT primitive evaluation requires a uniform full-period angular grid')
        grid=self.source.grid_for(t,theta);latent=self.latent_state(state)
        fields=grid.fields(latent);fields['_theta']=theta[None,:]
        frame=self.source.frame(latent,grid);metric=self.metric(state,t,jacobian)
        a,ap,app=(metric[key] for key in ['a','a_s','a_ss'])
        P,Ps,Pss=(periodic_operator(frame[key],-1) for key in ['T','Ts','Tss'])
        height=self.height_jets(state,t);nodes,weights=radial_quadrature(t,int(quadrature_order))
        base_q=self.height_baseline(nodes)['b0']
        increments=np.sum(base_q.reshape(len(t)-1,int(quadrature_order))*weights,axis=1)
        primitive=self.height_basis.integral(t)
        center=self.port.initial_center_z+np.r_[0.,np.cumsum(increments)]+primitive@state[self.slices['height']]
        X=a[:,None,None]*P;X[...,2]+=center[:,None]
        Xs=ap[:,None,None]*P+a[:,None,None]*Ps;Xs[...,2]+=height['b'][:,None]
        Xss=app[:,None,None]*P+2*ap[:,None,None]*Ps+a[:,None,None]*Pss
        Xss[...,2]+=height['b_s'][:,None]
        Xt=a[:,None,None]*frame['T'];Xst=ap[:,None,None]*frame['T']+a[:,None,None]*frame['Ts']
        Xtt=a[:,None,None]*frame['Ttheta']
        answer={'X':X,'Xs':Xs,'Xt':Xt,'Xss':Xss,'Xst':Xst,'Xtt':Xtt,
            'T':frame['T'],'Ts':frame['Ts'],'Tss':frame['Tss'],'Ttheta':frame['Ttheta'],
            'metric':metric,'height':height,'center':center,'primitive':P,
            'radial':t,'theta':theta,'auxiliary_R_not_used_as_metric_residual':True}
        if not jacobian:return answer
        names=['X','Xs','Xt','T']+(['Xss','Xst','Xtt'] if full_two_jet_jacobian else [])
        blocks={name:[] for name in names}
        for name in ['u','v']:
            jets=tangent_parameter_jets(grid,fields,frame,name,2 if full_two_jet_jacobian else 1)
            dP,dPs=(periodic_operator(jets[key],-1) for key in ['T','Ts'])
            blocks['X'].append(a[:,None,None,None]*dP)
            blocks['Xs'].append(ap[:,None,None,None]*dP+a[:,None,None,None]*dPs)
            blocks['Xt'].append(a[:,None,None,None]*jets['T']);blocks['T'].append(jets['T'])
            if full_two_jet_jacobian:
                dPss=periodic_operator(jets['Tss'],-1)
                blocks['Xss'].append(app[:,None,None,None]*dP+2*ap[:,None,None,None]*dPs+a[:,None,None,None]*dPss)
                blocks['Xst'].append(ap[:,None,None,None]*jets['T']+a[:,None,None,None]*jets['Ts'])
                blocks['Xtt'].append(a[:,None,None,None]*jets['Ttheta'])
        def vertical(values):
            out=np.zeros(X.shape+(self.height_free,));out[:,:,2,:]=values[:,None,:];return out
        zero=np.zeros(X.shape+(self.height_free,))
        blocks['X'].append(vertical(primitive));blocks['Xs'].append(vertical(self.height_basis.evaluate(t)))
        blocks['Xt'].append(zero);blocks['T'].append(zero)
        if full_two_jet_jacobian:
            blocks['Xss'].append(vertical(self.height_basis.evaluate(t,1)));blocks['Xst'].append(zero);blocks['Xtt'].append(zero)
        if self.metric_free:
            ja,jap,japp=(metric[key][:,None,None,:] for key in ['jac_a','jac_as','jac_ass'])
            blocks['X'].append(P[...,None]*ja)
            blocks['Xs'].append(P[...,None]*jap+Ps[...,None]*ja)
            blocks['Xt'].append(frame['T'][...,None]*ja)
            blocks['T'].append(np.zeros(X.shape+(self.metric_free,)))
            if full_two_jet_jacobian:
                blocks['Xss'].append(P[...,None]*japp+2*Ps[...,None]*jap+Pss[...,None]*ja)
                blocks['Xst'].append(frame['T'][...,None]*jap+frame['Ts'][...,None]*ja)
                blocks['Xtt'].append(frame['Ttheta'][...,None]*ja)
        for name in names:answer['jac_'+name]=np.concatenate(blocks[name],axis=-1)
        answer['parameter_Jacobian_contains_complete_position_two_jets']=bool(full_two_jet_jacobian)
        return answer

    def direct_residual_and_jacobian(self,state,radial,theta,quadrature_order=4,*,jacobian=True):
        data=self.geometry(state,radial,theta,quadrature_order,jacobian=jacobian)
        X,U,T=data['X'],data['Xs'],data['T'];count=len(radial)*len(theta)
        e=np.sum(U*U,axis=-1)-1;q=np.sum(U*T,axis=-1)
        values=[np.stack((e,np.sqrt(2)*q),axis=-1).ravel()/np.sqrt(count)]
        jac=[]
        if jacobian:
            de=2*np.sum(U[...,None]*data['jac_Xs'],axis=2)
            dq=np.sum(T[...,None]*data['jac_Xs']+U[...,None]*data['jac_T'],axis=2)
            jac.append(np.stack((de,np.sqrt(2)*dq),axis=2).reshape(-1,self.nunknown)/np.sqrt(count))
        if self.shape_weight>0:
            constraints=[np.sum(X*X,axis=-1)/self.ball_radius**2-1,X[...,1]/self.strip_half_width-1,-X[...,1]/self.strip_half_width-1]
            if jacobian:
                derivatives=[2*np.sum(X[...,None]*data['jac_X'],axis=2)/self.ball_radius**2,
                             data['jac_X'][:,:,1,:]/self.strip_half_width,-data['jac_X'][:,:,1,:]/self.strip_half_width]
            for k,value in enumerate(constraints):
                positive,slope=smooth_positive(value);weight=self.shape_weight/np.sqrt(count)
                values.append(weight*positive.ravel())
                if jacobian:jac.append(weight*(slope[...,None]*derivatives[k]).reshape(-1,self.nunknown))
        return np.concatenate(values),np.vstack(jac) if jacobian else None,data


def developer_check():
    rows=[]
    for side in [1,-1]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
        baseline=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
            ellipse_envelope=(port.major,port.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
        old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5')
        c0=.009*np.sin(np.arange(old.nunknown)+.2)
        old,c0,_=load_enriched_report(artificial_enriched_report(old,c0,baseline,.006*np.cos(np.arange(baseline.nunknown))))
        natural=NaturalBodyProblem(old,c0,metric_free=3,ball_radius='91/100',strip_half_width='1/3',
            amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9'],radial_nodes=9,angular_nodes=24,quadrature_order=3,heat_order=16)
        problem=IndependentHeightProblem(natural,3,height_angular_nodes=48)
        initial=problem.initial_state();rng=np.random.default_rng(6803+side)
        state=initial+.006*rng.standard_normal(problem.nunknown)
        t=natural.radial;theta=natural.theta;step=2e-7
        data=problem.geometry(state,t,theta,3,jacobian=True,full_two_jet_jacobian=True)
        direction=rng.standard_normal(problem.nunknown);direction/=np.linalg.norm(direction)
        plus=problem.geometry(state+step*direction,t,theta,3)
        minus=problem.geometry(state-step*direction,t,theta,3)
        jet_errors={}
        for key in ['X','Xs','Xt','Xss','Xst','Xtt']:
            fd=(plus[key]-minus[key])/(2*step);analytic=np.einsum('rtcn,n->rtc',data['jac_'+key],direction)
            jet_errors[key]=float(np.linalg.norm(fd-analytic)/max(1e-30,np.linalg.norm(fd)))
        rr,J,_=problem.direct_residual_and_jacobian(state,t,theta,3)
        rplus=problem.direct_residual_and_jacobian(state+step*direction,t,theta,3,jacobian=False)[0]
        rminus=problem.direct_residual_and_jacobian(state-step*direction,t,theta,3,jacobian=False)[0]
        fd=(rplus-rminus)/(2*step)
        objective_error=float(np.linalg.norm(fd-J@direction)/max(1e-30,np.linalg.norm(fd)))
        frozen,fc=problem.frozen_metric_copy(state);replay=frozen.geometry(fc,t,theta,3)
        freeze_error=max(float(np.max(abs(data[key]-replay[key]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt'])
        tf=problem.height_basis.right;tc=problem.height_basis.left
        endpoints=np.array([tc,tf]);Bjets=[problem.height_basis.evaluate(endpoints,j) for j in range(3)]
        # Different query-angle sets must not alter b0 or b0_s.
        before={key:value.copy() for key,value in problem.height_baseline(t).items()}
        problem.geometry(state,t,theta+.017,3)
        after=problem.height_baseline(t)
        query_independent=all(np.array_equal(before[key],after[key]) for key in before)
        # With equal mean quadrature, zero new controls reproduce the accurate
        # mathematical natural-c0 construction at the same numerical settings.
        matched=IndependentHeightProblem(natural,3,height_angular_nodes=len(theta))
        md=matched.geometry(matched.initial_state(),t,theta,3)
        original=natural.geometry(np.r_[c0,np.zeros(natural.metric_free)],natural.grid,quadrature_order=3)
        initial_replay=max(float(np.max(abs(md[key]-original[key]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt'])
        variants={'GH_only':problem.evaluation_variant(state,heat_order=32),
                  'height_angle_only':problem.evaluation_variant(state,height_angular_nodes=96)}
        uniform_identity=all(variant.identity(state)==problem.identity(state) for variant in variants.values())
        refinements={name:{key:float(np.max(abs(variant.height_baseline(t)[key]-before[key]))) for key in before}
                     for name,variant in variants.items()}
        noheight=state.copy();noheight[problem.slices['height']]=0
        unshifted=problem.geometry(noheight,t,theta,3)
        expected_shift=problem.height_basis.integral(t)@state[problem.slices['height']]
        difference=data['X']-unshifted['X'];difference[:,:,2]-=expected_shift[:,None]
        common_shift_error=float(np.max(abs(difference)))
        after=t>=tf;tail_derivative_error=max(float(np.max(abs(data[key][after]-unshifted[key][after])))
                                             for key in ['Xs','Xt','Xss','Xst','Xtt'])
        sample=np.array([tc+.013,.31,.63,tf-.017]);ds=1e-6
        hb=problem.height_baseline(sample);hp=problem.height_baseline(sample+ds);hm=problem.height_baseline(sample-ds)
        height_errors={key:float(np.max(abs((hp[source]-hm[source])/(2*ds)-hb[key]))) / max(1.,float(np.max(abs(hb[key]))))
                       for key,source in [('b0_s','b0'),('b0_ss','b0_s')]}
        sample_B=problem.height_basis.evaluate(sample)
        int_fd=(problem.height_basis.integral(sample+ds)-problem.height_basis.integral(sample-ds))/(2*ds)
        integral_error=float(np.max(abs(int_fd-sample_B)))
        rows.append({'side':side,'unknown_count':problem.nunknown,
            'tangent_count':problem.tangent_count,'height_count':problem.height_free,'metric_count':problem.metric_free,
            'complete_position_two_jet_parameter_Jacobian_relative_errors':jet_errors,
            'direct_metric_and_shape_Jacobian_relative_error':objective_error,
            'height_base_analytic_radial_jet_relative_errors':height_errors,
            'height_basis_primitive_derivative_error':integral_error,
            'height_endpoint_value_first_second_derivative_error':max(float(np.max(abs(x))) for x in Bjets),
            'height_mean_independent_of_query_angles':query_independent,
            'global_height_control_primitive_position_difference_error':common_shift_error,
            'height_control_open_tail_position_derivatives_unchanged_error':tail_derivative_error,
            'artificial_height_reference_evaluation_refinement_differences':refinements,
            'zero_controls_original_natural_c0_same_evaluator_position_two_jet_error':initial_replay,
            'frozen_metric_position_two_jet_replay_error':freeze_error,
            'same_physical_identity_under_heat_and_height_mean_refinement':uniform_identity,
            'fixed_height_base_exact_identity_sha256':digest(problem.height_base_definition),
            'independent_state_identity_sha256':digest(problem.identity(state))})
    passed=all(max(row['complete_position_two_jet_parameter_Jacobian_relative_errors'].values())<3e-5
        and row['direct_metric_and_shape_Jacobian_relative_error']<3e-5
        and max(row['height_base_analytic_radial_jet_relative_errors'].values())<3e-5
        and row['height_basis_primitive_derivative_error']<1e-8
        and row['height_endpoint_value_first_second_derivative_error']==0
        and row['height_mean_independent_of_query_angles']
        and row['global_height_control_primitive_position_difference_error']<1e-10
        and row['height_control_open_tail_position_derivatives_unchanged_error']==0
        and row['zero_controls_original_natural_c0_same_evaluator_position_two_jet_error']<1e-10
        and row['frozen_metric_position_two_jet_replay_error']==0
        and row['same_physical_identity_under_heat_and_height_mean_refinement'] for row in rows)
    return {'schema':'independent-height-frame-development-v1','passed':bool(passed),'checks':rows,
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False,
        'passed_does_not_certify_isometry_embedding_reach_or_quadrature_accuracy':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    answer=developer_check();hashes=natural_hashes()
    hashes[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    answer['source_files_sha256']=hashes;atomic_save(args.out,answer)
    print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
