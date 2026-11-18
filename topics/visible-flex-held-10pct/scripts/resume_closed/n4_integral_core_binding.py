#!/usr/bin/env python3
"""Bind the complete native n4 raw core without importing m3 conventions.

This reader handles core parameters and the material-angle chain only. It
does not decode the prefix polynomial, solve a BVP, certify an integral
error, or upgrade a linear-tail prefix to an actual nonlinear-tail result.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import gzip
import hashlib
import importlib
import json
import math
from pathlib import Path
import sys

import numpy as np


CORE_FILES = (
    'moment_interval_bounds.py', 'complementary_moment_basis.py',
    'plateau_core.py', 'large_radius_local_core.py',
    'second_order_large_radius_core.py', 'fixed_large_radius_core.py',
    'raw_n4_complementary.py', 'raw_n4_free_complementary.py',
    'raw_fixed_core.py',
)


def sha(file):
    return hashlib.sha256(Path(file).read_bytes()).hexdigest()


def payload_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def exact_binary64(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError('Finite binary64 physical parameters are required')
    return dict(value=value, hexadecimal=value.hex(), rational=str(Fraction.from_float(value)))


@dataclass(frozen=True)
class N4IntegralCoreBinding:
    checkpoint: Path
    checkpoint_sha256: str
    execution_record: Path
    source_root: Path
    record: dict
    source_sha256: dict
    q_actual: float
    controls: tuple

    def native_arguments(self):
        """Exactly the arguments for the original raw_fixed_core factory."""
        settings = dict(self.record['plateau_settings'])
        return dict(q=self.q_actual, corrections=self.controls, base_mode=4,
                    lock_fundamental=False, **settings)

    def native_core(self):
        """Construct the original integral evaluator; no BVP or prefix audit.

        Its Gauss quadrature, inverse tolerance and rho guard retain their
        original numerical meaning. Construction supplies no new rigorous
        integration or inverse error bound.
        """
        for file, digest in self.source_sha256.items():
            if sha(file) != digest:
                raise ValueError('Bound core source changed: '+file)
        root = str(self.source_root)
        modules = {}
        sys.path.insert(0, root)
        try:
            for filename in CORE_FILES:
                name = Path(filename).stem
                loaded = sys.modules.get(name)
                if loaded is not None and sha(loaded.__file__) != self.source_sha256[str(self.source_root/filename)]:
                    raise ValueError('Another core convention already owns module '+name)
                module = importlib.import_module(name)
                if sha(module.__file__) != self.source_sha256[str(self.source_root/filename)]:
                    raise ValueError('Imported core dependency differs: '+name)
                modules[name] = module
            Core = modules['raw_fixed_core'].make_core_class(
                modules['plateau_core'].PlateauSupportCore, self.record['raw_control_anchor_modes'])
            core = Core(**self.native_arguments())
        finally:
            sys.path.remove(root)
        if (core.base_mode != 4 or core.basis.M != self.record['config']['modes'] or
                core.basis.anchor_modes != self.record['raw_control_anchor_modes'] or
                float(core.q).hex() != self.q_actual.hex() or
                tuple(float(v).hex() for v in core.c) != tuple(float(v).hex() for v in self.controls)):
            raise AssertionError('Native constructor lost the full physical core input')
        return core

    def angle_jets(self, psi, e, ep, epp):
        """Original n4 material angle and physical-s derivatives.

        e, ep, epp are supplied from the unchanged radial profile; this
        function neither chooses them nor changes the meridian atlas.
        """
        psi = np.asarray(psi, float)
        eta = float(self.record['angular_chart_eta'])
        S = (1+eta)*np.sin(4*psi)/4-eta*np.sin(8*psi)/8
        C = (1+eta)*np.cos(4*psi)-eta*np.cos(8*psi)
        minus_Cp = 4*(1+eta)*np.sin(4*psi)-8*eta*np.sin(8*psi)
        return dict(theta=psi-e*S, theta_psi=1-e*C,
                    theta_psipsi=e*minus_Cp, theta_s=-ep*S,
                    theta_ss=-epp*S, theta_spsi=-ep*C)

    def descriptor(self):
        r = self.record
        native = self.native_arguments()
        return dict(
            scope=__doc__, checkpoint=dict(path=str(self.checkpoint), sha256=self.checkpoint_sha256),
            execution_record=dict(path=str(self.execution_record), sha256=sha(self.execution_record)),
            source_sha256=self.source_sha256,
            kind='n4_fixed_raw_mean_circle', control_path='raw-mean-free-c8-with-frozen-canonical-low-start-v1',
            modes=r['config']['modes'], raw_control_anchor_modes=r['raw_control_anchor_modes'],
            q_gauge=exact_binary64(r['gauge_amplitude']), q_actual=exact_binary64(self.q_actual),
            q_expression='float(q_gauge * numpy.exp(parameters[0])) in the original constructor convention',
            parameters=r['parameters'], central_correction_scales=r['central_correction_scales'],
            complete_controls=[exact_binary64(v) for v in self.controls],
            control_expression='binary64 numpy multiplication: parameters[1:] * central_correction_scales; index 0 is retained',
            free_c8=True, lock_fundamental=False,
            native_arguments={k:v for k,v in native.items() if k!='corrections'},
            angular_chart_eta=exact_binary64(r['angular_chart_eta']),
            meridian_length_binary64=exact_binary64(r['meridian_length']),
            physical_profile=r['physical_profile'], physical_profile_payload_sha256=payload_sha(r['physical_profile']),
            physical_port_payload_sha256=payload_sha(r['physical_port']),
            recorded_physical_port_file_sha256=r['physical_port_sha256'],
            parameter_count=len(r['parameters']), control_count=len(self.controls),
            checkpoint_solver_success=r.get('solver_success'),
            actual_nonlinear_tail_flag=bool(r['config'].get('actual_nonlinear_tail', False)),
            complete_metric_pass_flag=r.get('complete_metric_pass'),
            exact_circle_parameter_condition=r['plateau_settings']['homotopy']==1.,
            source_rounding_scope='The supplied native constructor q/c are the literal binary64 numbers above. An exact analytic integral uses the declared mean-zero primary/control definitions; quadrature, coefficient, center/period and inverse errors still require separate enclosures.',
            core_summary_used_as_definition=False, prefix_coefficients_decoded=False,
            bvp_solved=False, continuous_error_certified=False,
            mathematical_definition=dict(
                primary='s(phi)=-15*((1+eta)*cos(4phi)-eta*cos(8phi)); C=15*(1+2eta)',
                primary_mean='beta=-integral(chi_p*(C-s))/(T-integral(chi_p)), T=pi/2',
                primary_homotopy='s+lambda*(chi_p*(C-s)+beta*(1-chi_p))',
                raw_first_column='W*(cos(8phi)-<W*cos(8phi)>/<W>)',
                raw_other_columns='W*(cos(4*j*phi)-weighted_projection_onto_{1,cos(8phi)}), j=3..M',
                low_start='cos(4*j*phi)+ell_j*cos(4phi); ell_j comes from the frozen J canonical basis for j<=J, and is zero for j>J',
                full_control='(1-lambda)*low_start+lambda*raw_column; all j=2..M retained',
                rho='1+q_actual*primary_homotopy+sum_j c_j*(b_j+b_j_second)',
                curve='Gamma=n+q_actual*V+b*n+b_prime*t, b=sum_j c_j*b_j; V_prime=primary_homotopy*t',
                origin='(R_T-I)*V(0)=integral_0^T primary_homotopy(phi)*t(phi) dphi',
                material='u(phi)=integral_0^phi rho; u(0)=0; Gamma_u=t; Gamma_uu=-n/rho',
                angle='u=theta(s,psi)=psi-e(s)*((1+eta_chart)*sin(4psi)/4-eta_chart*sin(8psi)/8)',
                rho_material='rho_u=rho_phi/rho; rho_uu=(rho_phiphi*rho-rho_phi^2)/rho^3'),
        )


def load_binding(checkpoint, execution_record, source_root):
    checkpoint, execution_record, root = map(lambda p:Path(p).resolve(),
                                              (checkpoint, execution_record, source_root))
    record = json.loads(gzip.decompress(checkpoint.read_bytes()))
    execution = json.loads(execution_record.read_text())
    digest = sha(checkpoint)
    if execution['output_checkpoint']['sha256'] != digest:
        raise ValueError('Execution provenance belongs to another complete checkpoint')
    cfg = record['config']
    if (cfg.get('core_kind') != 'n4_fixed_raw_mean_circle' or cfg.get('base_mode') != 4 or
            record.get('fixed_metric') is not True or record.get('solver_success') is not True):
        raise ValueError('An explicitly successful native fixed-metric raw n4 prefix is required')
    M, J = cfg['modes'], record['raw_control_anchor_modes']
    if not isinstance(M,int) or not isinstance(J,int) or not 3 <= J <= M:
        raise ValueError('The full M and frozen canonical J must be explicit')
    provenance = record['raw_control_provenance']
    if provenance['anchor_modes'] != J or record['core_projection_order'] != J:
        raise ValueError('Frozen canonical low-start order changed')
    settings = record['plateau_settings']
    if set(settings) != {'halfwidth','transition','control_transition','homotopy','center','bimodal_eta'}:
        raise ValueError('Explicit n4 plateau settings required; no defaults or silent new fields')
    if (float(settings['center']).hex() != float(np.pi/4).hex() or
            not 0 <= settings['bimodal_eta'] <= 1 or not 0 <= settings['homotopy'] <= 1 or
            not 0 < settings['halfwidth'] < settings['halfwidth']+settings['transition'] < np.pi/4 or
            not 0 < settings['halfwidth'] < settings['halfwidth']+settings['control_transition'] < np.pi/4):
        raise ValueError('The stated pi/4 reflection-centered n4 windows are required')
    parameters = np.asarray(record['parameters'],float)
    scales = np.asarray(record['central_correction_scales'],float)
    if parameters.shape != (M,) or scales.shape != (M-1,) or not np.all(np.isfinite(parameters)) or not np.all(np.isfinite(scales)):
        raise ValueError('All physical parameters and all M-1 control scales must be present')
    gauge = float(record['gauge_amplitude'])
    q = float(gauge*np.exp(parameters[0]))
    controls = tuple(float(v) for v in parameters[1:]*scales)
    if not math.isfinite(q) or q <= 0 or not all(math.isfinite(c) for c in controls):
        raise ValueError('Invalid complete physical core')
    sources = {}
    for filename in CORE_FILES:
        file = root/filename
        expected = execution['source_sha256'][filename]
        if sha(file) != expected:
            raise ValueError('Original executed core dependency changed: '+str(file))
        if filename in provenance['source_sha256'] and provenance['source_sha256'][filename] != expected:
            raise ValueError('Checkpoint and execution core provenance disagree: '+filename)
        sources[str(file)] = expected
    if set(provenance['source_sha256'])-set(CORE_FILES):
        raise ValueError('Unbound core sources need an explicit reader update')
    return N4IntegralCoreBinding(checkpoint,digest,execution_record,root,record,sources,q,controls)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--execution-record',type=Path,required=True)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--construct-native',action='store_true')
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('Use a fresh output')
    bound = load_binding(args.checkpoint,args.execution_record,args.source_root)
    result = bound.descriptor()
    result['reader_sha256'] = sha(__file__)
    result['command'] = [sys.executable,*sys.argv]
    result['native_constructed'] = False
    if args.construct_native:
        core = bound.native_core()
        result['native_constructed'] = True
        result['native_constructor_identity'] = dict(
            all_controls_retained=True,actual_q_retained=True,first_control=core.c[0],
            modes=core.basis.M,anchor_modes=core.basis.anchor_modes,
            guard_lower_numerical_only=core.rho_lower)
    with args.output.open('x') as stream:
        json.dump(result,stream,indent=2,allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(output=str(args.output),sha256=sha(args.output),
                          native_constructed=result['native_constructed'],q_actual=bound.q_actual,
                          controls=len(bound.controls),prefix_solved=False)))


if __name__ == '__main__':
    main()
