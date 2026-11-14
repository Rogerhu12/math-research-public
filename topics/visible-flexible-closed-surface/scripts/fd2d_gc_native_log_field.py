#!/usr/bin/env python3
"""Actual shared C1 native eta/zeta field from a saved design BVP.

The defining radial coordinate is computational x, not physical s. Shared
binary node values and true first-x jets define exact cubic Hermite fields;
n=n_reference*exp(eta), m=n_reference*zeta is not Fourier truncated here.
"""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
from fd2d_gc_shared_hermite_field import SharedHermiteGCField

LD=np.longdouble
SCHEMA='fd2d-gc-native-log-shared-c1-field-v1'


def identity(path):
    path=Path(path)
    return dict(file=str(path.resolve()),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def locate_near(owner,row):
    owner=Path(owner);old=Path(row.get('file',row.get('path','')))
    local=owner.parent/old.name
    path=local if local.exists() else old
    if not path.exists() or identity(path)['sha256']!=row['sha256']:
        raise ValueError(f'Actual input missing or changed: {old.name}')
    return path


def write_native_definition(report_path,out):
    report_path,out=Path(report_path),Path(out)
    if out.exists():raise FileExistsError('Use a new actual native field definition')
    report=json.loads(report_path.read_text());raw=locate_near(report_path,report['field'])
    with np.load(raw,allow_pickle=False) as data:
        nodes=data['mesh'];values=data['values'];first=data['first']
        if values.shape!=first.shape or values.shape[1]!=len(nodes) or values.shape[0]%2!=1:
            raise ValueError('Unexpected native shared field dimensions')
        if np.any(np.diff(nodes)<=0) or not all(np.all(np.isfinite(a)) for a in (nodes,values,first)):
            raise ValueError('Invalid defining shared values or first-x jets')
        dimension=values.shape[0]
    angular=dict(report['angular_chart'])
    angular['radial_variable']='computational x, not physical s=S(x,T)'
    angular['U']='(1-beta(x))*U_seed(xi)+beta(x)*xi'
    angular['beta']='10*t^3-15*t^4+6*t^5; t=clip((x-left)/(right-left),0,1)'
    central=report['actual_central_definition']
    definition=dict(schema=SCHEMA,source=identity(__file__),source_report=identity(report_path),
        actual_arrays=dict(file=str(raw.relative_to(out.parent)) if raw.parent==out.parent else str(raw.resolve()),**{k:v for k,v in identity(raw).items() if k!='file'}),
        polynomial_source=report['polynomial'],
        definition='exact shared binary64 node/value/first-x cubic Hermite for eta,zeta',
        node_count=len(nodes),dimension=dimension,mode_count=(dimension-1)//2,
        state_order='[eta_0,eta_2,...,eta_(2K),zeta_2,...,zeta_(2K)]; real cosine/sine, no sqrt(2)',
        radial_domain_exact=[str(Fraction(float(nodes[0]))),str(Fraction(float(nodes[-1])))],
        true_first_source='saved sol.sol(mesh,1); rhs stored separately and not used as defining first-x jets',
        physical_fields='n=sqrt(1-a_s^2)/a*exp(eta), m=sqrt(1-a_s^2)/a*zeta; full exponential, no angular truncation',
        angular_chart=angular,radial_chart=report['final_radial_chart'],
        target_input=report['candidate_input'],designed_target=report['designed_candidate'],
        initial_geometry=central,source_inputs=report['sources'],
        actual_T=report['parameters']['T'],physical_metric_frozen_for_this_consumer=True,
        same_g_refinement_evidence_claimed=False,complete_target_prefix=True,exact_C1_definition=True,
        continuous_residual_bounded_here=False,nonlinear_tail_solved=report['nonlinear_tail_solved'],closed_surface=False)
    out.write_text(json.dumps(definition,indent=2,allow_nan=False)+'\n')
    return out


class NativeLogField:
    def __init__(self,path):
        self.path=Path(path);self.meta=json.loads(self.path.read_text())
        if self.meta['schema']!=SCHEMA:raise ValueError('Wrong actual native field schema')
        row=self.meta['actual_arrays'];raw_path=Path(row['file'])
        if not raw_path.is_absolute():raw_path=self.path.parent/raw_path
        if identity(raw_path)['sha256']!=row['sha256']:raise ValueError('Defining native arrays changed')
        with np.load(raw_path,allow_pickle=False) as data:
            self.nodes=data['mesh'].copy();self.values=data['values'].T.copy();self.first_s=data['first'].T.copy()
        if np.any(np.diff(self.nodes)<=0) or not all(np.all(np.isfinite(a)) and a.dtype==np.float64 for a in (self.nodes,self.values,self.first_s)):
            raise ValueError('Invalid exact native binary data')
        self.dimension=self.meta['dimension'];self.K=(self.dimension-1)//2
        if self.values.shape!=(len(self.nodes),self.dimension) or self.first_s.shape!=self.values.shape:
            raise ValueError('Native field dimension mismatch')
        self.frequencies=2*np.arange(1,self.K+1,dtype=LD)

    # These two methods are coordinate-neutral Hermite algebra. first_s is
    # only the inherited internal attribute name: it stores FIRST-X jets.
    normalized_power=SharedHermiteGCField.normalized_power
    state=SharedHermiteGCField.state

    def evaluate(self,x,xi):
        xi=np.atleast_1d(np.asarray(xi,dtype=LD));y,yx=self.state(x),self.state(x,1)
        phase=self.frequencies[:,None]*xi[None,:];co,si=np.cos(phase),np.sin(phase)
        k=self.frequencies[:,None];eta0,ec,zs=y[:,0:1],y[:,1:self.K+1],y[:,self.K+1:]
        ex0,exc,zxs=yx[:,0:1],yx[:,1:self.K+1],yx[:,self.K+1:]
        return dict(eta=eta0+ec@co,zeta=zs@si,eta_x=ex0+exc@co,zeta_x=zxs@si,
            eta_xi=ec@(-k*si),zeta_xi=zs@(k*co),
            eta_xixi=ec@(-k*k*co),zeta_xixi=zs@(-k*k*si))


def log_codazzi_numerators(a,ap,app,J,q,Ux,eta,zeta,eta_x,zeta_x,eta_xi,zeta_xi,exp_minus_eta,exp_minus_2eta,expm1_minus_2eta):
    """Coefficient-first actual numerator identities, retaining background cancellation.

    a/ap/app are physical-s target jets. J=S_x>0, q=U_xi>0.
    Rn=exp(eta)*Pn/(J*a^2*q*sqrt(1-ap^2));
    Rm=Pm/(J*a^2*q*sqrt(1-ap^2)). All radial native derivatives are fixed xi.
    """
    v2=1-ap*ap
    Pn=(a*q*v2*eta_x-a*v2*Ux*eta_xi-J*v2*exp_minus_eta*zeta_xi
        -J*ap*q*(v2*exp_minus_2eta*zeta*zeta-a*app*expm1_minus_2eta))
    Pm=(a*q*v2*zeta_x-a*v2*Ux*zeta_xi
        -J*exp_minus_eta*(2*v2*zeta*zeta_xi-(v2*zeta*zeta-a*app)*eta_xi)
        +J*ap*q*(v2-a*app)*zeta)
    return dict(Pn=Pn,Pm=Pm,denominator_without_sqrt=J*a*a*q,v2=v2)
