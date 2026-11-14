"""R180 exact full-function endpoint primitive for the actual current field.

v=(-a*n,a*m,0), q=v-L_v with L_v the endpoint affine interpolant at
fixed native xi.  The native/physical drift is retained algebraically:

  E=(v_right-v_left)/L + T - (U_s/U_xi)*(L_v)_xi + q cross alpha,
  T=(m_u+a_s*l, -l_u+a_s*m, -a*G).

This is an exact nonpolynomial primitive; no fit, Fourier truncation or
radial differentiation of a numerical interpolant defines q or E.
"""
from __future__ import annotations

from fractions import Fraction as F

from flint import arb

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import (
    rational,interval,square,require_positive,UnresolvedInterval)
from fd2d_gc_current_accurate_domain_arb import digest
from fd2d_gc_current_primitive_interval_v2 import cross,norm_upper

SCHEMA='fd2d-R180-exact-full-function-connection-endpoint-primitive-v1'


def _v(fields,profile):
    n,m,unused=fields
    return (-profile.a*n.value,profile.a*m.value,arb(0))


def _v_xi(fields,profile):
    n,m,unused=fields
    if n.xi is None or m.xi is None:
        raise UnresolvedInterval('Exact angular first jets are required')
    return (-profile.a*n.xi,profile.a*m.xi,arb(0))


def _gauss(fields,profile,evaluated,field,cell):
    """Use only exact defining algebra, otherwise retain the full G box."""
    if int(cell)==field.last_cell:
        # Both supported accurate-domain constructors bind the whole
        # completed cell to the exact trace platform. Their cut bypass is
        # the exact PSD tail, not a numerical projection.
        return arb(0),'accurate completed cell: R155 trace platform; exact PSD tail at endpoint'
    weights=evaluated.get('weights')
    if weights is not None:
        terminal=weights['terminal'].value
        coast=weights['coast'].value
        if terminal==arb(1):
            return arb(0),'complete terminal trace weight identically one'
        if coast==arb(1) and terminal.is_zero():
            return arb(0),'complete R153 weight identically one; terminal weight zero'
    n,m,l=fields
    return n.value*l.value-square(m.value)+profile.a_ss/profile.a,'actual full Gauss interval'


class ExactConnectionEndpointPrimitive:
    """One full actual cell, including its exact endpoint angular functions."""
    def __init__(self,field,cell):
        self.cell=int(cell)
        self.cell_definition=field.cell_definition(self.cell)
        self.field_binding_sha256=field.binding_sha256
        # This is a current-field consumer, not a duck-typed assertion that
        # any arbitrary last cell is on the R155 platform.
        schema=field.definition()['schema']
        if schema not in (
                'fd2d-current-complete-accurate-domain-Arb-v1',
                'fd2d-R170-current-complete-accurate-domain-Arb-v1'):
            raise ValueError('Bind an explicit complete accurate-domain field')
        self.field_schema=schema
        self._endpoint_cache={}
        self.packet_sha256=digest(self.definition(include_hash=False))

    def definition(self,include_hash=True):
        result=dict(schema=SCHEMA,source=identity(__file__),
            field_schema=self.field_schema,
            field_binding_sha256=self.field_binding_sha256,
            cell_definition=self.cell_definition,
            v='(-a*n,a*m,0), using the complete actual physical target and fields',
            endpoints='same fixed native xi, full exact angular functions at normalized t=0 and t=1',
            L_v='(1-t)*v_left+t*v_right, t normalized by the true physical cell length',
            q='v-L_v',
            exact_identities=dict(q_left_zero=True,q_right_zero=True,
                q_xi_left_zero=True,q_xi_right_zero=True),
            physical_radial_operator='partial_s_at_fixed_xi-(U_s/U_xi)*partial_xi',
            E='(v_right-v_left)/L + (m_u+a_s*l,-l_u+a_s*m,-a*G) - (U_s/U_xi)*(L_v)_xi + q cross alpha',
            alpha='(m,-l,0)',
            all_endpoint_angular_modes_retained=True,
            finite_fit_or_sampled_integral_used=False,
            n_s_or_m_s_needed_by_E=False,
            whole_surface_certificate=False)
        if include_hash:result['packet_sha256']=self.packet_sha256
        return result

    def _validate(self,field):
        if (field.binding_sha256!=self.field_binding_sha256 or
                field.cell_definition(self.cell)!=self.cell_definition):
            raise ValueError('The endpoint primitive is bound to another exact field or cell')

    def _endpoints(self,field,alo,ahi,angle_unit):
        key=(rational(alo),rational(ahi),angle_unit)
        if key not in self._endpoint_cache:
            rows=[]
            for t,side in ((F(0),'right'),(F(1),'left')):
                q=field.cell_box(self.cell,t,t,alo,ahi,
                    angle_unit=angle_unit,side=side,connection=False)
                rows.append(dict(v=_v(q['fields'],q['profile']),
                    v_xi=_v_xi(q['fields'],q['profile'])))
            if len(self._endpoint_cache)>=8:
                self._endpoint_cache.pop(next(iter(self._endpoint_cache)))
            self._endpoint_cache[key]=tuple(rows)
        return self._endpoint_cache[key]

    def box(self,field,tlo,thi,alo,ahi,*,angle_unit='pi',side='both'):
        self._validate(field)
        tlo,thi=map(rational,(tlo,thi))
        if not 0<=tlo<=thi<=1:
            raise ValueError('Use normalized actual physical cell labels')
        evaluated=field.cell_box(self.cell,tlo,thi,alo,ahi,
            angle_unit=angle_unit,side=side,connection=False)
        left,right=self._endpoints(field,alo,ahi,angle_unit)
        length=field.cell_length(self.cell)
        require_positive(length,'actual physical cell length')
        t=interval(tlo,thi)
        linear=tuple((1-t)*a+t*b for a,b in zip(left['v'],right['v']))
        linear_xi=tuple((1-t)*a+t*b for a,b in zip(left['v_xi'],right['v_xi']))
        mean=tuple((b-a)/length for a,b in zip(left['v'],right['v']))
        v=_v(evaluated['fields'],evaluated['profile'])
        vxi=_v_xi(evaluated['fields'],evaluated['profile'])
        if tlo==thi and tlo in (0,1):
            # Exact function identity, not numerical small-value clipping.
            q=qxi=(arb(0),arb(0),arb(0))
        else:
            q=tuple(a-b for a,b in zip(v,linear))
            qxi=tuple(a-b for a,b in zip(vxi,linear_xi))
        profile,chart=evaluated['profile'],evaluated['chart']
        n,m,l=evaluated['fields']
        require_positive(profile.a,'actual physical radius')
        require_positive(chart.U_xi,'actual material-angle Jacobian')
        if m.xi is None or l.xi is None:
            raise UnresolvedInterval('Complete actual first angular jets are required')
        G,Gscope=_gauss(evaluated['fields'],profile,evaluated,field,self.cell)
        T=(m.xi/chart.U_xi+profile.a_s*l.value,
           -l.xi/chart.U_xi+profile.a_s*m.value,
           -profile.a*G)
        drift=chart.drift()
        alpha=(m.value,-l.value,arb(0))
        product=cross(q,alpha)
        E=tuple(b+c-drift*dx+comm for b,c,dx,comm in
                zip(mean,T,linear_xi,product))
        return dict(E=E,E_norm_upper=norm_upper(E),
            q=q,q_xi=qxi,Q_norm_upper=norm_upper(q),
            Q_e1_norm_upper=norm_upper(q[1:]),
            v=v,v_xi=vxi,endpoint_linear=linear,
            endpoint_linear_xi=linear_xi,endpoint_slope=mean,T=T,
            physical_drift=drift,alpha=alpha,Gauss=G,Gauss_scope=Gscope,
            actual=evaluated,field_binding_sha256=self.field_binding_sha256,
            primitive_sha256=self.packet_sha256,source_cell=self.cell,
            exact_endpoint_identity_used=(tlo==thi and tlo in (0,1)),
            physical_drift_sign='minus (U_s/U_xi)*(L_v)_xi',
            radial_derivatives_n_s_m_s_used_by_E=False,
            complete_actual_endpoint_functions_used=True,
            no_polynomial_fit_error_or_aliasing_assumed=True,
            initial_compatibility_supplied=False,whole_surface_certificate=False)


__all__=['ExactConnectionEndpointPrimitive']
