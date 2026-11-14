"""R180 on an exact subinterval of one original physical P1 cell.

Only the verification interval changes. Original mesh indices, complete
field, metric and terminal-domain identity remain unchanged. In particular
a one-cell verification view is never relabelled as a terminal field cell.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from flint import arb

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import (
    rational,rational_pair,aq,interval,require_positive,UnresolvedInterval)
from fd2d_gc_current_primitive_interval_v2 import cross,norm_upper
from fd2d_gc_connection_endpoint_primitive import (
    ExactConnectionEndpointPrimitive,_v,_v_xi,_gauss)

PARENT_SHA256='2a5f3e966751f787ce53bb7ee420cfc3480be78e925fe16ab203965a15f3931b'
SCHEMA='fd2d-R180-exact-full-function-subcell-primitive-v1'


class RestrictedConnectionEndpointPrimitive(ExactConnectionEndpointPrimitive):
    """ta/tb are exact normalized labels in the original physical cell."""
    def __init__(self,field,cell,ta=F(0),tb=F(1)):
        self.ta,self.tb=map(rational,(ta,tb))
        if not 0<=self.ta<self.tb<=1:
            raise ValueError('Use a nonempty exact subinterval of the saved physical cell')
        self.parent_source=identity(Path(__file__).with_name(
            'fd2d_gc_connection_endpoint_primitive.py'))
        if self.parent_source['sha256']!=PARENT_SHA256:
            raise ValueError('The inherited exact primitive algebra changed')
        super().__init__(field,cell)

    def definition(self,include_hash=True):
        result=super().definition(include_hash=False)
        result.update(schema=SCHEMA,source=identity(__file__),
            parent_formula_source=self.parent_source,
            subinterval_original_normalized=[rational_pair(self.ta),rational_pair(self.tb)],
            local_label='r in [0,1]; original t=ta+(tb-ta)*r',
            physical_length='(tb-ta) times the original exact physical cell length',
            original_field_cell_index_retained=True,
            complete_field_mesh_or_functions_changed=False,
            endpoints='full exact angular functions at original labels ta,tb and fixed native xi')
        if include_hash:result['packet_sha256']=self.packet_sha256
        return result

    def _endpoints(self,field,alo,ahi,angle_unit):
        key=(rational(alo),rational(ahi),angle_unit)
        if key not in self._endpoint_cache:
            rows=[]
            for t,side in ((self.ta,'right'),(self.tb,'left')):
                q=field.cell_box(self.cell,t,t,alo,ahi,
                    angle_unit=angle_unit,side=side,connection=False)
                rows.append(dict(v=_v(q['fields'],q['profile']),
                    v_xi=_v_xi(q['fields'],q['profile'])))
            if len(self._endpoint_cache)>=8:
                self._endpoint_cache.pop(next(iter(self._endpoint_cache)))
            self._endpoint_cache[key]=tuple(rows)
        return self._endpoint_cache[key]

    def box(self,field,rlo,rhi,alo,ahi,*,angle_unit='pi',side='both'):
        self._validate(field)
        rlo,rhi=map(rational,(rlo,rhi))
        if not 0<=rlo<=rhi<=1:
            raise ValueError('Use normalized subcell labels in [0,1]')
        span=self.tb-self.ta
        tlo,thi=self.ta+span*rlo,self.ta+span*rhi
        actual=field.cell_box(self.cell,tlo,thi,alo,ahi,
            angle_unit=angle_unit,side=side,connection=False)
        left,right=self._endpoints(field,alo,ahi,angle_unit)
        length=field.cell_length(self.cell)*aq(span)
        require_positive(length,'accurate physical subcell length')
        r=interval(rlo,rhi)
        linear=tuple((1-r)*a+r*b for a,b in zip(left['v'],right['v']))
        linear_xi=tuple((1-r)*a+r*b for a,b in zip(left['v_xi'],right['v_xi']))
        mean=tuple((b-a)/length for a,b in zip(left['v'],right['v']))
        v,vxi=_v(actual['fields'],actual['profile']),_v_xi(actual['fields'],actual['profile'])
        if rlo==rhi and rlo in (0,1):
            q=qxi=(arb(0),arb(0),arb(0))
        else:
            q=tuple(a-b for a,b in zip(v,linear))
            qxi=tuple(a-b for a,b in zip(vxi,linear_xi))
        p,chart=actual['profile'],actual['chart'];n,m,l=actual['fields']
        require_positive(p.a,'actual physical radius')
        require_positive(chart.U_xi,'actual angular Jacobian')
        if m.xi is None or l.xi is None:
            raise UnresolvedInterval('Full first angular jets are required')
        G,Gscope=_gauss(actual['fields'],p,actual,field,self.cell)
        T=(m.xi/chart.U_xi+p.a_s*l.value,
           -l.xi/chart.U_xi+p.a_s*m.value,-p.a*G)
        drift=chart.drift();alpha=(m.value,-l.value,arb(0));comm=cross(q,alpha)
        E=tuple(b+c-drift*dx+z for b,c,dx,z in zip(mean,T,linear_xi,comm))
        return dict(E=E,E_norm_upper=norm_upper(E),
            q=q,q_xi=qxi,Q_norm_upper=norm_upper(q),Q_e1_norm_upper=norm_upper(q[1:]),
            v=v,v_xi=vxi,endpoint_linear=linear,endpoint_linear_xi=linear_xi,
            endpoint_slope=mean,T=T,physical_drift=drift,alpha=alpha,
            Gauss=G,Gauss_scope=Gscope,actual=actual,
            physical_subcell_length=length,
            original_normalized_query=[rational_pair(tlo),rational_pair(thi)],
            subcell_normalized_query=[rational_pair(rlo),rational_pair(rhi)],
            field_binding_sha256=self.field_binding_sha256,
            primitive_sha256=self.packet_sha256,source_cell=self.cell,
            exact_endpoint_identity_used=(rlo==rhi and rlo in (0,1)),
            physical_drift_sign='minus (U_s/U_xi)*(L_v)_xi',
            radial_derivatives_n_s_m_s_used_by_E=False,
            complete_actual_endpoint_functions_used=True,
            no_polynomial_fit_error_or_aliasing_assumed=True,
            original_field_mesh_changed=False,
            initial_compatibility_supplied=False,whole_surface_certificate=False)


__all__=['RestrictedConnectionEndpointPrimitive']
