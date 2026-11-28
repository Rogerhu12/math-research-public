#!/usr/bin/env python3
"""Complete R715-method frozen-reference calibration for the R730 length field.

This helper never changes a current free point, the seed, the fixed metric or
a root. It reads the same bound reference nodes and the same Torch endpoint
formula at the original reference point, retains their actual defects, and
records the complete physical-lift readouts. All scientific calls are Actions
only. Ordinary values are not outward errors or continuous certificates.
"""
from pathlib import Path
import hashlib
import json
import math
import os

import numpy as np
import torch

SCHEMA = 'complete-R730-frozen-reference-working-calibration-v1'
ENDPOINT_SCHEMA = 'complete-fixed-fejer-r730-detached-meridian-normal-layer-v1'
BASE_SOURCE = 'b9c787340021b5736f2796f2b84a1c25cb4b0ce96333eb98f543b1e8923ce267'
BASE_SCHEMA = 'complete-fixed-fejer-r730-so3-meridian-with-core-lift-v1'
SEED_SOURCE = '53ebce095394a833d95a65b834ae889b4cb9554e06ef839fcb626bddcb8864b8'
LENGTH_KERNEL_SOURCE = '87be2efa7381f50bd419c0d91a3b0c5b1a762f9f1eb7d1f2f7a053f8bc93cfc2'
ORIGINAL_NORMAL_SOURCE = '66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific frozen-reference calibration requires public Actions')


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20),b''):
            value.update(block)
    return value.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    result = hashlib.sha256(str(value.dtype).encode())
    result.update(json.dumps(list(value.shape)).encode())
    result.update(value.tobytes())
    return result.hexdigest()


def tensor(value):
    return torch.as_tensor(np.array(value,dtype=np.float64,copy=True),
        dtype=torch.float64,device='cpu')


class FrozenReferenceCalibration:
    def __init__(self, base, core_cap_method, total_method, *, endpoint_source_sha256):
        require_actions()
        if torch.__version__.split('+')[0] != '2.5.1':
            raise ValueError('Keep the declared complete CPU Torch source path')
        if (base.model.get('schema') != BASE_SCHEMA
                or base.model.get('source_sha256') != BASE_SOURCE
                or canonical(base.model) != base.identity):
            raise ValueError('Calibrate only the complete fixed R730 base')
        seed = base.model['fixed_safe_cone_unit_seed_model']
        if (seed != base.parent_jet.model or canonical(seed) != base.parent_jet.model_identity
                or seed.get('source_sha256') != SEED_SOURCE
                or seed.get('length_kernel_source_sha256') != LENGTH_KERNEL_SOURCE):
            raise ValueError('The complete fixed R730 length/inverse reference changed')
        owner = getattr(core_cap_method,'__self__',None)
        if owner is None or getattr(total_method,'__self__',None) is not owner or owner.base is not base:
            raise ValueError('Use the actual same complete endpoint operator for both methods')
        for function in (core_cap_method,total_method):
            actual = function.__func__
            if (sha(actual.__code__.co_filename) != endpoint_source_sha256
                    or actual.__globals__.get('SCHEMA') != ENDPOINT_SCHEMA
                    or actual.__globals__.get('REFERENCE_CENTERING_SOURCE_SHA256') != sha(__file__)):
                raise ValueError('The actual endpoint method does not bind this full calibration source')
        for name in ('initial','unpack','_unpack_torch','_parent_tensor'):
            if sha(getattr(base,name).__func__.__code__.co_filename) != BASE_SOURCE:
                raise ValueError('Changed complete reference evaluation path: '+name)
        self.base,self.core_cap,self.total = base,core_cap_method,total_method
        self.endpoint_source_sha256 = endpoint_source_sha256
        self.reference_point = np.array(base.initial(),dtype=np.float64,copy=True)
        core,jets,height = base.unpack(self.reference_point)
        if (not np.array_equal(core,base.parent_core) or np.any(jets != 0)
                or float(height).hex() != seed['initial_height_hex']):
            raise ValueError('The baseline is the original core/H with all outer omega zero')
        self.reference_point.setflags(write=False)
        self.reference_point_sha256 = array_sha(self.reference_point)
        self.definition = dict(schema='R730-fixed-length-reference-centred-working-normal-definition-v1',
            source_sha256=sha(__file__),endpoint_source_sha256=endpoint_source_sha256,
            original_complete_normal_source_sha256=ORIGINAL_NORMAL_SOURCE,
            original_reference_point_sha256=self.reference_point_sha256,
            original_height_hex=seed['initial_height_hex'],base_model_identity_sha256=base.identity,
            fixed_safe_cone_reference_identity_sha256=base.parent_jet.model_identity,
            fixed_endpoint_path='same complete Torch core/cap method at original base.initial()',
            fixed_integration_reference_path='same bound base._parent_tensor integration query',
            integration_order=int(base.integration_order),mesh_sha256=array_sha(base.mesh),
            gauss_nodes_sha256=array_sha(base.gauss_u),gauss_weights_sha256=array_sha(base.gauss_w),
            nodewise_difference_before_original_complete_cumsum=True,
            exact_equality_to_original_closure_requires_exact_reference_closure=True,
            all_normal_stages_and_full_upstream_parameter_jets_retained=True,
            physical_lift='ell=S5(s/S)=1-base_query_h; complete delta_ref-Ecenter and ALL derivatives',
            numerical_current_raw_closure_defect_omitted=False,
            numerical_radial_Gram_error_identically_zero=False)
        self.field_identity = None
        self.cache = {}
        self.current_point = None
        self.raw = [None,None,None]
        self.centered = [None,None,None]

    def bind_field(self, model, identity):
        if (self.field_identity is not None or canonical(model) != identity
                or model.get('schema') != ENDPOINT_SCHEMA
                or model.get('source_sha256') != self.endpoint_source_sha256
                or model.get('reference_centering_definition') != self.definition
                or model.get('base_complete_model') != self.base.model):
            raise ValueError('Bind once to the complete actual centred field model')
        self.field_identity = identity

    def select_point(self, identity):
        if identity != self.current_point:
            self.current_point = identity
            self.raw,self.centered = [None,None,None],[None,None,None]

    def reference_data(self, phi):
        require_actions()
        if self.field_identity is None:
            raise ValueError('The complete centred field must be bound before any evaluation')
        phi = np.asarray(phi,dtype=np.float64)
        if phi.ndim != 1 or not len(phi) or not np.isfinite(phi).all():
            raise ValueError('Use every finite literal material angle')
        keys = tuple(float(v).hex() for v in phi)
        parent = self.base._parent_tensor(self.base.integration_query,phi,'integration')
        reference = {name:parent[key].detach() for name,key in
            (('T','T0'),('Tp','T0_phi'),('Tpp','T0_phiphi'))}
        expected = ((self.base.J-1)*self.base.integration_order,len(phi),3)
        if any(tuple(v.shape) != expected or not bool(torch.isfinite(v).all()) for v in reference.values()):
            raise ValueError('The complete fixed reference three-jet is unavailable')
        if keys not in self.cache:
            with torch.no_grad():
                core,_,height = self.base._unpack_torch(tensor(self.reference_point))
                Gamma,P,_ = self.core_cap(core,height,phi)
                Gamma = tuple(v.detach().clone() for v in Gamma)
                P = tuple(v.detach().clone() for v in P)
                delta = torch.stack(tuple(P[j]-Gamma[j]-self.total(reference[name])
                    for j,name in enumerate(('T','Tp','Tpp'))),dim=1)
                if not bool(torch.isfinite(delta).all()):
                    raise ValueError('Nonfinite actual reference defect; no defect is set to zero')
                norms = torch.linalg.vector_norm(delta,dim=-1).amax(0).cpu().numpy()
            arrays = dict(phi=phi,core=np.stack([v.cpu().numpy() for v in Gamma]),
                cap=np.stack([v.cpu().numpy() for v in P]),delta=delta.cpu().numpy())
            name = canonical(dict(field=self.field_identity,angles=keys))
            path = self.base.cache_directory/('reference-centred-'+name+'.npz')
            temporary = path.with_suffix('.partial.npz')
            np.savez(temporary,**arrays,model_identity=np.array(self.field_identity),
                reference_point_sha256=np.array(self.reference_point_sha256))
            temporary.replace(path)
            record = dict(angle_list_sha256=canonical(keys),angle_count=len(keys),
                path=str(path),bytes=path.stat().st_size,sha256=sha(path),
                arrays_sha256={k:array_sha(v) for k,v in arrays.items()},
                maximum_defect_norms=[float(v) for v in norms])
            self.cache[keys] = (Gamma,P,record)
        Gamma,P,_ = self.cache[keys]
        return reference,Gamma,P

    def observe_field(self, defects, centered):
        require_actions()
        if len(defects) != len(centered) or len(defects) not in (2,3):
            raise ValueError('Retain every requested angular closure jet')
        for j in range(len(defects)):
            raw = float(torch.linalg.vector_norm(defects[j].detach(),dim=-1).max())
            ctr = float(torch.linalg.vector_norm(centered[j].detach(),dim=-1).max())
            if not math.isfinite(raw) or not math.isfinite(ctr):
                raise ValueError('Nonfinite actual raw or centred closure readout')
            self.raw[j] = raw if self.raw[j] is None else max(self.raw[j],raw)
            self.centered[j] = ctr if self.centered[j] is None else max(self.centered[j],ctr)

    def current_record(self):
        return dict(reference_point_sha256=self.reference_point_sha256,
            current_full_point_sha256=self.current_point,
            raw_value_max=self.raw[0],raw_phi_max=self.raw[1],raw_phiphi_max=self.raw[2],
            centered_value_max=self.centered[0],centered_phi_max=self.centered[1],
            centered_phiphi_max=self.centered[2],
            working_radial_identity=False,complete_raw_defect_lift=True,
            equation_scope='reference-centred complete equation; distinct raw quadrature defect')

    def metadata(self):
        records = [v[2] for v in self.cache.values()]
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            model_identity_sha256=self.field_identity,
            reference_point_sha256=self.reference_point_sha256,
            fixed_endpoint_angle_batches=len(records),actual_reference_records=records,
            maximum_fixed_reference_defect_norms=[
                max((r['maximum_defect_norms'][j] for r in records),default=None) for j in range(3)],
            current=self.current_record(),
            physical_field_uses_complete_current_raw_defect_lift=True,
            lift_includes_all_current_parameter_and_angular_derivatives=True,
            baseline_reselected_from_current_outer_point=False,
            raw_reference_defect_forced_to_zero=False,
            numerical_radial_Gram_identity_claimed=False,
            accurate_reference_or_quadrature_or_geometry_certified=False)
