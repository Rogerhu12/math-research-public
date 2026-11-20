#!/usr/bin/env python3
"""Cheap outward full-image C0 difference for two same-carrier closed fields.

No angular grid and no radial sampling. Exact Hermite differences are
elevated to degree six; Delta q_Z0 + chi Delta H is combined at controls.
Finite angular coefficients use l1 bounds. The complete analytic circle
lift uses its exact unit-vector Lipschitz bound, with all core modes kept.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


GEOMETRY_SHA = '2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377'
INTERVAL_SHA = 'f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module; spec.loader.exec_module(module)
    return module


class Difference:
    def __init__(self, base, candidate, node_report, geometry_source, interval_source):
        if sha(geometry_source) != GEOMETRY_SHA or sha(interval_source) != INTERVAL_SHA:
            raise ValueError('Use the stated complete radial model and outward arithmetic')
        self.paths = dict(base=Path(base), candidate=Path(candidate), node_report=Path(node_report),
                          geometry_source=Path(geometry_source), interval_source=Path(interval_source))
        geometry = load('C0_difference_radial_geometry', geometry_source)
        self.I = load('C0_difference_outward_arithmetic', interval_source)
        # Instantiate only the documented radial formulas. Reader.__init__
        # also builds angle transforms, which this l1 proof does not use.
        self.r = geometry.Reader.__new__(geometry.Reader)
        r, I = self.r, self.I
        r.I = I
        with np.load(base, allow_pickle=False) as z:
            self.base = {k: np.array(z[k]) for k in z.files}
        with np.load(candidate, allow_pickle=False) as z:
            self.candidate = {k: np.array(z[k]) for k in z.files}
        for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
            if not np.array_equal(self.base[key], self.candidate[key]):
                raise ValueError('Same exact carrier required: '+key)
        report = json.loads(Path(node_report).read_text())
        r.mesh = self.base['mesh']; r.J = len(r.mesh)
        r.M = (self.base['qjets'].shape[-1]-2)//3; r.n = 3*r.M+2
        r.width = F(float(self.base['width'])); r.W = r.fraction(r.width)
        r.nodes = [(F(d['S_coefficient']), F(d['constant'])) for d in report['true_scalar_nodes']]
        r.S_exact = tuple(F(report['scalar']['S'][k]) for k in ('lower_exact', 'upper_exact'))
        r.R_exact = tuple(F(report['scalar']['R'][k]) for k in ('lower_exact', 'upper_exact'))
        r.S, r.R = r.bounds(*r.S_exact), r.bounds(*r.R_exact)
        if (len(r.nodes) != r.J or report['S_carrier'] != float(r.mesh[-1])
                or report['radius_carrier'] != float(self.base['radius'])
                or r.nodes[0] != (F(0), F(0)) or r.nodes[-1] != (F(1), F(0))):
            raise ValueError('The exact same-Hold symbolic mesh must match both members')
        self.scalar_identity = report['scalar']
        self.validate_member(self.base); self.validate_member(self.candidate)
        old, new = self.base['qjets'], self.candidate['qjets']
        difference = I.sub(I.exact(new), I.exact(old))
        same = new == old
        self.jets = np.where(same, 0., difference[0]), np.where(same, 0., difference[1])
        self.core_difference = I.at(self.jets, (0, 0, slice(1, r.M+1)))
        nu = 2*np.arange(1, r.M+1)
        # This is the accurate real affine difference, not a subtraction
        # of the two separately rounded derived endpoint T arrays.
        exact_t_difference = I.scale(self.core_difference, -nu)
        self.jets[0][0, 0, r.M+1:2*r.M+1] = exact_t_difference[0]
        self.jets[1][0, 0, r.M+1:2*r.M+1] = exact_t_difference[1]
        self.height_difference_exact = F(float(self.candidate['Hcap']))-F(float(self.base['Hcap']))
        self.height_difference = r.fraction(self.height_difference_exact)
        phase_coefficients = I.div(I.scale(self.core_difference, 1-nu*nu), I.exact(nu))
        self.phase_difference_upper = float(I.sum_upper(I.absolute_upper(phase_coefficients)))
        self.rho_difference_upper = float(I.sum_upper(I.absolute_upper(I.scale(self.core_difference, 1-nu*nu))))
        c0, c1 = old[0, 0, 1:r.M+1], new[0, 0, 1:r.M+1]
        self.witness_displacement_exact = abs(sum((F(float(b))-F(float(a)) for a, b in zip(c0, c1)), F(0)))
        self.witness_displacement_upper = float(r.fraction(self.witness_displacement_exact)[1])

    def validate_member(self, data):
        r = self.r; y = data['qjets']; core = y[0, 0, 1:r.M+1]
        if y.shape != (r.J, 3, r.n) or not np.isfinite(y).all() or float(data['Hcap']) <= 0:
            raise ValueError('Incomplete finite closed member')
        expected = y.copy(); expected[0, 0] = 0.; expected[0, 0, 0] = 1.
        expected[0, 0, 1:r.M+1] = core
        expected[0, 0, r.M+1:2*r.M+1] = -2*np.arange(1, r.M+1)*core
        expected[0, 1] = 0.; expected[0, 1, 2*r.M+1] = 1.
        expected[0, 2, 2*r.M+1:] = 0.; expected[-1] = 0.
        if not np.array_equal(expected, y) or not np.array_equal(core[:len(data['fixed_core_first3'])], data['fixed_core_first3']):
            raise ValueError('Member must belong to the original literal affine interface')

    def cell(self, cell):
        r, I = self.r, self.I
        h = r.width_box(r.nodes[cell], r.nodes[cell+1])
        if float(h[0]) <= 0:
            raise ValueError('The exact original cell width must be positive')
        controls = r.hermite(I.at(self.jets, cell), I.at(self.jets, cell+1), h)
        best = dict(cell=cell, uniform_difference_upper=0., pieces=[])
        for index, piece in enumerate(r._cell_pieces(cell)):
            left, right, u0, u1, active = piece
            co = r.elevate(r.restrict(controls, u0, u1))
            lift = r.lift_controls(left, right, active)
            z0 = I.add(I.at(co, (slice(None), 2*r.M+1)), I.mul(lift['chi'], self.height_difference))
            co[0][:, 2*r.M+1], co[1][:, 2*r.M+1] = z0
            R = I.sum_upper(I.absolute_upper(I.at(co, (slice(None), slice(0, r.M+1)))), axis=-1)
            T = I.sum_upper(I.absolute_upper(I.at(co, (slice(None), slice(r.M+1, 2*r.M+1)))), axis=-1)
            Z = I.sum_upper(I.absolute_upper(I.at(co, (slice(None), slice(2*r.M+1, None)))), axis=-1)
            square = I.add(I.add(I.square(I.exact(R)), I.square(I.exact(T))), I.square(I.exact(Z)))
            norms = I.sqrt(square)[1]
            control = int(np.argmax(norms)); polynomial_bound = float(norms[control])
            fmax = float(I.absolute_upper(lift['f']).max())
            analytic_bound = float(I.mul(I.exact(fmax), I.exact(self.phase_difference_upper))[1])
            total = float(I.add(I.exact(polynomial_bound), I.exact(analytic_bound))[1])
            detail = dict(piece=index, active_lift=bool(active),
                symbolic_left=[str(v) for v in left], symbolic_right=[str(v) for v in right],
                combined_q_and_height_upper=polynomial_bound, worst_Bernstein_control=control,
                component_l1_at_worst_control=[float(v[control]) for v in (R, T, Z)],
                f_absolute_upper=fmax, full_analytic_phase_difference_upper=analytic_bound,
                uniform_difference_upper=total)
            best['pieces'].append(detail)
            best['uniform_difference_upper'] = max(best['uniform_difference_upper'], total)
        return best

    def transfer(self, epsilon, diameter='4.106819', witness_distance='.943143', marker_height='.001'):
        I, r = self.I, self.r
        ep = I.exact(epsilon); eta = r.fraction(self.witness_displacement_exact)
        D = I.add(r.fraction(F(diameter)), I.scale(ep, 2))
        L = I.sub(I.sub(r.fraction(F(witness_distance)), ep), eta)
        held_ratio = I.div(L, D)
        grip_ratio = I.div(r.fraction(F(9, 10)), D)
        h = F(marker_height)
        marked_D = I.add(D, r.fraction(2*h))
        height_lower = F(float(self.candidate['Hcap']))-h
        marked_distance = float(L[0]) if r.fraction(height_lower)[0] > L[1] else min(float(L[0]), float(r.fraction(height_lower)[0]))
        return dict(base_certified_diameter_exact=diameter,
            base_certified_witness_distance_exact=witness_distance,
            Hausdorff_distance_upper=epsilon, witness_displacement_upper=float(eta[1]),
            new_diameter_upper=float(D[1]), new_full_witness_distance_lower=float(L[0]),
            new_held_amplitude_over_diameter_lower=float(held_ratio[0]),
            radius_0_45_fixed_grip_over_diameter_lower=float(grip_ratio[0]),
            marker_height_exact=str(h), conditional_marked_diameter_upper=float(marked_D[1]),
            conditional_marked_witness_distance_lower=marked_distance,
            conditional_marked_held_ratio_lower=float(I.div(I.exact(marked_distance), marked_D)[0]),
            conditional_marked_grip_ratio_lower=float(I.div(r.fraction(F(9, 10)), marked_D)[0]),
            new_core_rho_lower_from_base=float(I.sub(r.fraction(F('0.1657734')), I.exact(self.rho_difference_upper))[0]),
            geometric_embedding_curvature_reach_or_metric_claimed=False)

    def run(self):
        records = [self.cell(cell) for cell in range(self.r.J-1)]
        if [r['cell'] for r in records] != list(range(self.r.J-1)):
            raise ValueError('Full cell coverage was not returned')
        cap_bound = float(self.r.fraction(abs(self.height_difference_exact))[1])
        side_bound = max(item['uniform_difference_upper'] for item in records)
        epsilon = max(side_bound, cap_bound)
        return dict(schema='same-carrier-fullclosed-C0-difference-outward-v1',
            source_sha256=sha(__file__), source_inputs={name:dict(path=str(path.resolve()), sha256=sha(path)) for name, path in self.paths.items()},
            exact_S_box=[str(v) for v in self.r.S_exact], exact_R_box=[str(v) for v in self.r.R_exact],
            exact_width=str(self.r.width), J=self.r.J, M=self.r.M,
            height_difference_exact=str(self.height_difference_exact),
            core_phase_difference_l1_upper=self.phase_difference_upper,
            core_rho_difference_l1_upper=self.rho_difference_upper,
            witness_displacement_exact=str(self.witness_displacement_exact),
            caps_difference_upper=cap_bound, side_difference_upper=side_bound,
            complete_image_Hausdorff_upper=epsilon, covered_original_cells=len(records),
            angular_grid_created=False, radial_samples_or_subdivisions=0,
            all_modes_and_complete_analytic_lift_retained=True,
            delta_q_Z0_plus_chi_delta_H_combined_before_bounds=True,
            derived_core_T_difference_reconstructed_exactly=True,
            same_angle_band_pairing_and_same_Cartesian_cap_pairing=True,
            cap_pairing_need_not_agree_with_band_pairing_at_seam=True,
            strict_under_stated_IEEE_arithmetic=True,
            arithmetic='f512 IEEE binary64 operations each outward; exact rational S/R/mesh widths; coefficient l1 and Bernstein convexity',
            top_cells=sorted(records, key=lambda z:z['uniform_difference_upper'], reverse=True)[:8],
            records=records, transferred_components=self.transfer(epsilon))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('base', 'candidate', 'node-report', 'geometry-source', 'interval-source', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    args = p.parse_args()
    if args.out.exists(): raise FileExistsError('Keep prior complete difference reports')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    start = time.monotonic()
    reader = Difference(args.base, args.candidate, args.node_report, args.geometry_source, args.interval_source)
    report = reader.run(); report['seconds'] = time.monotonic()-start
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'records'}), flush=True)
    print(json.dumps(dict(event='complete_C0_difference_returned', report_sha256=sha(args.out))), flush=True)


if __name__ == '__main__': main()
