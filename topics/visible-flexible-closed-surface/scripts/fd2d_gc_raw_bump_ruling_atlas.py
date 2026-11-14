"""Explicit whole-domain ruling atlas on the same physical bump target.

Only the finite angular representation and one added computational knot
change here. The exact known lifting is pulled back at the actual material
u. On its coast support its label is already known, so no material inverse
is needed. All physical-profile and tail parameter columns stay analytic.
"""
from __future__ import annotations
import json
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_raw_bump_coast_reference import CoastReferenceRawBumpDAE
from fd2d_gc_frozen_ruling_atlas import FrozenRulingAtlas,invert_original_chart_on_grid


class DirectLabelCoastReference:
    """Same fixed R139 functions, evaluated at the caller's known label."""
    def __init__(self,original,atlas,maximum_points=64):
        self.original=original;self.atlas=atlas;self.maximum_points=int(maximum_points)
        if self.maximum_points<1:raise ValueError('Positive bounded cache size required')
        if original.candidate_sha256!=atlas.ruling.base.candidate_sha256:
            raise ValueError('Reference and atlas use different physical inputs')
        self._points=[];self.hits=self.misses=0
        self.maximum_composition_residual=0.;self.maximum_native_residual=0.
    def __getattr__(self,key):
        original=self.__dict__.get('original')
        if original is None:raise AttributeError(key)
        return getattr(original,key)
    def __copy__(self):return self
    def __deepcopy__(self,memo):memo[id(self)]=self;return self
    def _point(self,s,label,material):
        s=float(s);label=np.asarray(label,np.longdouble);material=np.asarray(material,np.longdouble)
        if label.ndim!=1 or material.shape!=label.shape:raise ValueError('Expected paired label/material columns')
        point=None
        for i,(ss,xi,row) in enumerate(self._points):
            if ss==s and np.array_equal(xi,label):
                point=row;self.hits+=1
                if i:self._points.insert(0,self._points.pop(i))
                break
        if point is None:
            q=self.atlas.ruling_jet(s,label,include_native=True);native=q['native']
            n,m,ns,ms=(np.asarray(native[k],np.longdouble) for k in ('n','m','n_s','m_s'))
            if np.any(n<=0) or np.any(native['D']<=0):raise FloatingPointError('Fixed positive reference failed')
            ls=(2*m*ms*n-m*m*ns)/(n*n)
            point=dict(material_u=np.asarray(native['material_u'],np.longdouble),
                values=np.asarray(np.stack((n,m,native['l']),axis=-1),float),
                physical_s=np.asarray(np.stack((ns,ms,ls),axis=-1),float),
                physical_u=np.asarray(np.stack((native['n_u'],native['m_u'],native['l_u']),axis=-1),float))
            if not all(np.all(np.isfinite(v)) for v in point.values()):raise FloatingPointError('Nonfinite direct reference jets')
            self.maximum_native_residual=max(self.maximum_native_residual,
                *[float(np.max(abs(native[k]),initial=0.)) for k in ('gauss_residual','codazzi_n','codazzi_m')])
            for value in point.values():value.flags.writeable=False
            self._points.insert(0,(s,label.copy(),point));del self._points[self.maximum_points:];self.misses+=1
        error=float(np.max(abs(point['material_u']-material),initial=0.))
        self.maximum_composition_residual=max(self.maximum_composition_residual,error)
        if error>2e-13:raise ValueError('Direct label does not match the actual requested material coordinate')
        return point
    def jet_on_grid(self,x,coords,active_mask=None):
        x=np.asarray(x,float);u=np.asarray(coords['u']);labels=np.asarray(coords['frozen_ruling_label'])
        us,ux=(np.asarray(coords[k],float) for k in ('u_s','u_xi'))
        if u.ndim!=2 or u.shape[1]!=len(x) or any(v.shape!=u.shape for v in (labels,us,ux)):
            raise ValueError('Expected full paired label/material chart arrays')
        active=(x>=self.entry_s)&(x<=self.exit_s) if active_mask is None else np.asarray(active_mask,bool)
        if active.shape!=x.shape or np.any(active&((x<self.entry_s)|(x>self.exit_s))):
            raise ValueError('Active direct reference outside its physical coast')
        values=np.zeros(u.shape+(3,));dx=np.zeros_like(values);dxi=np.zeros_like(values)
        for j in np.flatnonzero(active):
            row=self._point(x[j],labels[:,j],u[:,j]);values[:,j]=row['values']
            dx[:,j]=row['physical_s']+us[:,j,None]*row['physical_u']
            dxi[:,j]=ux[:,j,None]*row['physical_u']
        return dict(values=values,x=dx,xi=dxi)
    def evaluation_definition(self):
        return dict(schema='fd2d-known-ruling-label-fixed-reference-evaluation-v1',
            source_sha256=identity(__file__)['sha256'],physical_reference_binding_sha256=self.binding_sha256,
            angular_atlas_source_sha256=self.atlas.chart_definition()['source_sha256'],
            method='R139 native_from_inlet at known frozen inlet label; no material inverse',
            physical_component_order=['n','m','l'],physical_l_s='(2*m*m_s*n-m*m*n_s)/n^2 of the positive frozen reference',
            computational_x='physical_s+U_s*physical_u',computational_xi='U_xi*physical_u',
            composition_tolerance=2e-13,stored_jets_dtype='binary64',
            cache='bounded recent 64 scalar-s/full-label pairs, actual label equality and requested material composition checked',
            physical_function_changed=False,unknown_raw_n_divided=False)
    def cache_statistics(self):
        return dict(entries=len(self._points),maximum_entries=self.maximum_points,hits=self.hits,misses=self.misses,
            maximum_material_composition_residual=self.maximum_composition_residual,
            maximum_numerical_native_GC_residual=self.maximum_native_residual,
            evaluation='known ruling label',loaded_old_mixed_cache_used=False)
    def definition(self):
        out=self.original.definition();out['direct_label_evaluation']=self.evaluation_definition()
        out['direct_label_cache_statistics']=self.cache_statistics();return out


class RulingAtlasRawBumpDAE(CoastReferenceRawBumpDAE):
    def __init__(self,*args,reference_inlet,atlas_entry_start=.55,atlas_exit_stop=1.4,**kwargs):
        super().__init__(*args,reference_inlet=reference_inlet,**kwargs)
        self.original_chart=self.chart;old_nodes=self.x.copy()
        if atlas_entry_start<float(self.seed_weight_definition['end']):
            raise ValueError('The new chart must begin only after the exact seed lifting vanishes')
        self.chart=FrozenRulingAtlas(self.original_chart,reference_inlet,
            entry_start=atlas_entry_start,exit_stop=atlas_exit_stop)
        self.x=np.unique(np.r_[old_nodes,self.chart.entry_start,self.chart.entry_s,self.chart.exit_s,self.chart.exit_stop])
        # The first three interface knots already occur in the declared
        # physical mesh. A scale-near duplicate is rejected rather than
        # silently changing the already stored mathematical representation.
        if np.min(np.diff(self.x))<1e-12*max(1.,self.profile.end):
            raise ValueError('Atlas interface and physical knots need explicit near-duplicate reconciliation')
        self.N=len(self.x);self.h=np.diff(self.x);self.size=self.N*self.q+self.parameter_count
        self.residual_size=self.N*self.q+2*self.K+2
        self.coords={k:np.asarray(v,float) for k,v in self.chart.coordinates(self.x).items()}
        self._operator_cache={};self._cell_gauss_view_cache=None;self._chunked_gauss_codazzi_views=None
        self.fixed_central_nodes=np.flatnonzero(self.x<=self.profile.central_end)
        self.central_field_definition=dict(self.central_field_definition,fixed_node_indices=self.fixed_central_nodes.tolist())
        self.angular_atlas_definition=self.chart.chart_definition()
        self.atlas_mesh_definition=dict(schema='fd2d-explicit-ruling-atlas-computational-mesh-v1',
            old_nodes=old_nodes.tolist(),actual_nodes=self.x.tolist(),
            added_nodes=self.x[~np.isin(self.x,old_nodes)].tolist(),
            old_node_count=len(old_nodes),actual_node_count=self.N,minimum_cell=float(self.h.min()),
            all_old_nodes_retained=bool(np.all(np.isin(old_nodes,self.x))),
            physical_metric_changed=False,finite_representation_changed=True)
        self.coast_reference=DirectLabelCoastReference(self.coast_reference,self.chart)
        self.reference_evaluation_definition=self.coast_reference.evaluation_definition()
        self.representation_kind='targeted_turn_mesh_exact_cylinder_frozen_coast_global_ruling_atlas_v1'
    def parameter_layout(self):
        out=super().parameter_layout();out.update(angular_atlas_definition=self.angular_atlas_definition,
            atlas_mesh_definition=self.atlas_mesh_definition,reference_evaluation_definition=self.reference_evaluation_definition)
        return out
    def warm_from_old_coast(self,mesh,corrections,parameters):
        mesh=np.asarray(mesh,float);y=np.asarray(corrections,float);p=np.asarray(parameters,float)
        if y.shape!=(len(mesh),self.q) or p.shape!=(self.parameter_count,):raise ValueError('Wrong warm dimensions')
        if mesh[0]!=self.x[0] or mesh[-1]!=self.x[-1] or np.any(np.diff(mesh)<=0):raise ValueError('Different old physical domain')
        if not np.all(np.isin(mesh,self.x)):raise ValueError('Keep every old physical node explicitly')
        interpolated=np.column_stack([np.interp(self.x,mesh,y[:,j]) for j in range(self.q)])
        roundtrip=interpolated[np.searchsorted(self.x,mesh)]-y
        yy=interpolated.copy();changed=(self.x>self.chart.entry_start)&(self.x<self.chart.exit_stop)
        x=self.x[changed];u=self.coords['u'][:,changed]
        oldxi,inverse=invert_original_chart_on_grid(self.original_chart,x,u)
        freq=2*np.arange(self.K+1);target=np.empty((self.work,len(x),3))
        projection_rows=[]
        for local,j in enumerate(np.flatnonzero(changed)):
            cosine=np.cos(np.asarray(oldxi[:,local],float)[:,None]*freq)
            sine=np.sin(np.asarray(oldxi[:,local],float)[:,None]*freq[1:])
            old=interpolated[j]
            target[:,local,0]=cosine@old[:self.e];target[:,local,1]=sine@old[self.e:self.d]
            target[:,local,2]=cosine@old[self.d:]
            yy[j,:self.e]=self.PE@target[:,local,0];yy[j,self.e:self.d]=self.PO@target[:,local,1]
            yy[j,self.d:]=self.PE@target[:,local,2]
            restored=np.stack((self.E@yy[j,:self.e],self.O@yy[j,self.e:self.d],self.E@yy[j,self.d:]),axis=-1)
            projection_rows.append(dict(node=int(j),s=float(self.x[j]),
                component_maximum_errors=np.max(abs(restored-target[:,local]),axis=0).tolist()))
        before=np.r_[yy.ravel(),p.copy()];vector=self.impose_linear_boundary_values(before)
        err=np.asarray([r['component_maximum_errors'] for r in projection_rows])
        return vector,dict(schema='fd2d-explicit-old-mixed-to-global-ruling-warm-v1',
            old_node_count=len(mesh),new_node_count=self.N,unchanged_coordinate_nodes=int(np.count_nonzero(~changed)),
            changed_coordinate_nodes=int(np.count_nonzero(changed)),
            original_node_P1_roundtrip_error=float(np.max(abs(roundtrip))),
            unchanged_coordinate_coefficients_copied_exactly=bool(np.array_equal(yy[~changed],interpolated[~changed])),
            original_material_inverse=inverse,
            correction_projection_component_maximum_errors=np.max(err,axis=0).tolist(),projection_rows=projection_rows,
            boundary_projection_change_maximum=float(np.max(abs(vector-before))),
            parameters_unchanged=bool(np.array_equal(self.unpack(vector)[1],p)),
            physical_metric_changed=False,nonlinear_solve_performed=False,
            lifting_transfer='new L(s,xi)=old L(s,oldXi(s,Unew)) as whole functions: changed region has zero seed lifting, remaining tail/reference are physical-u compositions',
            continuous_old_field_preserved=False,
            scope='Retained Fourier projection at same physical material points, then actual new radial P1 interpolation; recompute complete finite residual')


def checkpoint_arrays(problem,vector,candidate_sha256):
    y,p=problem.unpack(vector)
    return dict(mesh=problem.x,corrections=y,parameters=p,modes=np.array(problem.K),
        profile_supports=problem.profile.supports,profile_count=np.array(problem.J),
        fixed_base_T=np.array(problem.fixed_base_T),profile_kind=np.array(problem.profile_kind),
        tail_kind=np.array(problem.tail_kind),base_kind=np.array(problem.base_kind),
        candidate_sha256=np.array(candidate_sha256),blend=np.array(problem.blend),
        seed_weight_definition=np.array(json.dumps(problem.seed_weight_definition,sort_keys=True)),
        representation_kind=np.array(problem.representation_kind),
        central_field_definition=np.array(json.dumps(problem.central_field_definition,sort_keys=True)),
        targeted_mesh_definition=np.array(json.dumps(problem.targeted_mesh_definition,sort_keys=True)),
        coast_reference_definition=np.array(json.dumps(problem.coast_reference_definition,sort_keys=True)),
        angular_atlas_definition=np.array(json.dumps(problem.angular_atlas_definition,sort_keys=True)),
        atlas_mesh_definition=np.array(json.dumps(problem.atlas_mesh_definition,sort_keys=True)),
        reference_evaluation_definition=np.array(json.dumps(problem.reference_evaluation_definition,sort_keys=True)),
        finite_radial_scheme=np.array('Exact full lifting endpoint difference plus Gauss-Legendre2 physical PDE cell averages'))
