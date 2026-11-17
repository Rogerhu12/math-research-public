#!/usr/bin/env python3
"""Radial geometric reconstruction of the same integral-K height candidate.

The exact candidate is defined by radial integral equations for alpha and XY,
with a literal angular-primitive initial curve.  Quadrature approximates these
integrals; actual radial jets use their analytic derivatives, not a sampled
surface interpolant or the old P/K PDE.  Angular jets are independent FFT
derivatives of the reconstructed positions.  The model note proves C2 under
the stated positive-branch hypotheses.  All numerical extrema below remain
sampling evidence on an open small-amplitude tail, not a closed/reach result.
"""

from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np


def import_file(path, name):
    raw = path.read_bytes()
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if path.read_bytes() != raw:
        raise RuntimeError('A reconstruction dependency changed while importing')
    return module, hashlib.sha256(raw).hexdigest()


def integration_matrix(order):
    nodes, weights = np.polynomial.legendre.leggauss(order)
    basis = np.polynomial.legendre.legvander(nodes, order-1)
    integrals = np.empty_like(basis)
    for k in range(order):
        coefficient = np.zeros(order); coefficient[k] = 1
        primitive = np.polynomial.legendre.legint(coefficient)
        integrals[:, k] = (np.polynomial.legendre.legval(nodes, primitive)
                            - np.polynomial.legendre.legval(-1., primitive))/2
    return (nodes+1)/2, weights/2, np.linalg.solve(basis.T, integrals.T).T


def angular_derivative(values, order=1):
    n = values.shape[1]
    multiplier = (1j*np.fft.fftfreq(n, d=1/n))**order
    if order % 2 == 1:
        multiplier[n//2] = 0
    shape = (1, n)+(1,)*(values.ndim-2)
    return np.fft.ifft(np.fft.fft(values, axis=1)*multiplier.reshape(shape), axis=1).real


def compensated_add(value, correction, increment):
    adjusted = increment-correction
    updated = value+adjusted
    return updated, (updated-value)-adjusted


def radial_coefficients(data, rho):
    r, w, wr = (data[name][:, None] for name in ('r', 'w', 'wr'))
    hr, hrr, hp, hrp = (data[name] for name in ('hr', 'hrr', 'h_phi', 'hr_phi'))
    z, zr, E = w*w, 2*w*wr, 1+w*w
    density = rho[None, :]
    P, y = hp/(r*density*w), hr/w
    K = y-1
    Pr = hrp/(r*density*w)-(1/r+wr/w)*P
    Kr = hrr/w-y*wr/w
    A = 2*K+K*K+E*P*P
    Ar_aux = 2*y*Kr+zr*P*P+2*E*P*Pr
    S, D = 1-z*P*P, 1-z*A
    Sr, Dr = -zr*P*P-2*z*P*Pr, -zr*A-z*Ar_aux
    if np.min(S) <= 0 or np.min(D) <= 0:
        raise FloatingPointError('Radial construction leaves the positive branch')
    a = np.sqrt(D/S)
    b = -z*y*P/np.sqrt(S)
    ar = a*(Dr/D-Sr/S)/2
    br = -(zr*y*P+z*Kr*P+z*y*Pr)/np.sqrt(S)+z*y*P*Sr/(2*S**1.5)
    U = hrp/(w*density)-P
    connection = z*y*U/(r*S*np.sqrt(D))
    return dict(a=a, b=b, ar=ar, br=br, connection=connection,
                q=r*density*np.sqrt(S), S=S, D=D)


def read_geometry(alpha, xy, mean_height, data, coefficients, rho):
    tangent = np.stack((np.cos(alpha), np.sin(alpha)), axis=2)
    normal = np.stack((np.sin(alpha), -np.cos(alpha)), axis=2)
    a, b, ar, br, connection = (coefficients[name] for name in ('a', 'b', 'ar', 'br', 'connection'))
    V = b[:, :, None]*tangent+a[:, :, None]*normal
    Vr = ((br+a*connection)[:, :, None]*tangent
          +(ar-b*connection)[:, :, None]*normal)
    F = np.concatenate((xy, (data['hperp']+mean_height[:, None])[:, :, None]), axis=2)
    Fr = np.concatenate((V, data['hr'][:, :, None]), axis=2)
    Frr = np.concatenate((Vr, data['hrr'][:, :, None]), axis=2)
    Fphi = np.concatenate((angular_derivative(xy), data['h_phi'][:, :, None]), axis=2)
    Fphiphi = np.concatenate((angular_derivative(xy, 2), data['h_phiphi'][:, :, None]), axis=2)
    Frphi = angular_derivative(Fr)
    E = np.sum(Fr*Fr, axis=2); mixed = np.sum(Fr*Fphi, axis=2); G = np.sum(Fphi*Fphi, axis=2)
    targetE, targetG = 1+data['w'][:, None]**2, (data['r'][:, None]*rho[None, :])**2
    er, gr, fr = E/targetE-1, G/targetG-1, mixed/np.sqrt(targetE*targetG)
    op = (abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2
    cross = np.cross(Fr, Fphi)
    determinant = np.sum(cross*cross, axis=2)
    unit = cross/np.sqrt(determinant)[:, :, None]
    ee, ff, gg = (np.sum(jet*unit, axis=2) for jet in (Frr, Frphi, Fphiphi))
    tr = (ee*G+gg*E-2*ff*mixed)/determinant
    kd = (ee*gg-ff*ff)/determinant
    curvature = (abs(tr)+np.sqrt(np.maximum(0, tr*tr-4*kd)))/2
    angular_error = Fphi[:, :, :2]-coefficients['q'][:, :, None]*tangent
    return dict(F=F, Fr=Fr, Frr=Frr, er=er, gr=gr, fr=fr, op=op,
                curvature=curvature, determinant=determinant,
                angular_error=angular_error,
                radial_outward=np.sum(V*normal, axis=2))


def run(args):
    started = time.perf_counter()
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    height_module, height_sha = import_file(args.height_reader, 'same_height_reader')
    helper_module, helper_sha = import_file(args.angular_helper, 'same_angular_helper')
    reader = height_module.HeightReader(args.input, args.background, args.angles,
                                        'k-integral', args.height_gauss, args.height_anchor)
    rho = getattr(reader, 'rho', np.ones(reader.N))
    rho_phi = getattr(reader, 'rho_phi', np.zeros(reader.N))
    direction = 1 if reader.height_anchor == 'left' else -1
    start = reader.breaks[0] if direction == 1 else reader.breaks[-1]
    start_reference = reader.breaks[0] if direction == 1 else reader.breaks[-2]
    anchor = reader.evaluate(np.array([start]), np.array([start_reference]))
    initial = helper_module.reconstruct_slice(
        h=anchor['hperp'][0]+args.anchor_mean_height,
        rho=rho, rho_phi=rho_phi,
        **{name: anchor[name][0] for name in ('r', 'w', 'wr', 'hr', 'hrr', 'h_phi',
                                             'h_phiphi', 'hr_phi', 'hr_phiphi')})
    alpha = initial['alpha'].copy(); xy = initial['F'][:, :2].copy()
    mean_height = args.anchor_mean_height
    alpha_correction = np.zeros_like(alpha); xy_correction = np.zeros_like(xy)
    height_correction = 0.
    phi = reader.angle
    initial_turn_error = 1+angular_derivative((alpha-phi)[None, :])[0]-initial['omega_phi']
    initial_angular_error = initial['Fphi'][:, :2] - np.sqrt((anchor['r'][0]*rho)**2-anchor['h_phi'][0]**2)[:, None]*np.column_stack((np.cos(alpha), np.sin(alpha)))
    nodes, weights, matrix = integration_matrix(args.radial_gauss)
    cell_order = np.arange(len(reader.breaks)-1)
    if direction < 0:
        cell_order = cell_order[::-1]
    maxima = {name: 0. for name in ('relative_gram_operator', 'relative_rr', 'relative_rphi',
                  'relative_phiphi', 'principal_curvature', 'angular_compatibility',
                  'join_Fr_jump', 'join_Frr_jump', 'sampled_mean')}
    minima = {name: float('inf') for name in ('gram_determinant', 'radial_outward_speed', 'S', 'D', 'L')}
    position_min, position_max = np.full(3, np.inf), np.full(3, -np.inf)
    worst = {}; worst_curvature = {}; count = 0; previous_end = None
    max_reference_curvature = 0.
    height_total = 0.
    for batch_start in range(0, len(cell_order), args.batch_cells):
        selected = cell_order[batch_start:batch_start+args.batch_cells]
        low, high = reader.breaks[selected], reader.breaks[selected+1]
        left, right = (low, high) if direction > 0 else (high, low)
        fractions = np.r_[0., nodes, 1.]
        points = (left[:, None]+(right-left)[:, None]*fractions).ravel()
        reference = np.repeat(low, len(fractions))
        all_data = reader.evaluate(points, reference)
        all_coefficients = radial_coefficients(all_data, rho)
        for local, cell in enumerate(selected):
            offset = local*len(fractions); sl = slice(offset, offset+len(fractions))
            data = {name: value[sl] for name, value in all_data.items()
                    if isinstance(value, np.ndarray) and value.shape[0] == len(points)}
            coefficients = {name: value[sl] for name, value in all_coefficients.items()}
            width = right[local]-left[local]
            alpha_velocity = data['rx'][1:-1, None]*coefficients['connection'][1:-1]
            alpha_nodes = alpha+width*(matrix@alpha_velocity)
            alpha_end, alpha_correction = compensated_add(
                alpha, alpha_correction, width*(weights@alpha_velocity))
            tangent = np.stack((np.cos(alpha_nodes), np.sin(alpha_nodes)), axis=2)
            normal = np.stack((np.sin(alpha_nodes), -np.cos(alpha_nodes)), axis=2)
            spatial_velocity = data['rx'][1:-1, None, None]*(
                coefficients['b'][1:-1, :, None]*tangent+coefficients['a'][1:-1, :, None]*normal)
            xy_nodes = xy+width*np.einsum('ij,jkl->ikl', matrix, spatial_velocity)
            xy_end, xy_correction = compensated_add(
                xy, xy_correction, width*np.einsum('j,jkl->kl', weights, spatial_velocity))
            height_velocity = data['height_mean_x'][1:-1]
            height_nodes = mean_height+width*(matrix@height_velocity)
            height_end, height_correction = compensated_add(
                mean_height, height_correction, width*float(weights@height_velocity))
            alpha_all = np.vstack((alpha, alpha_nodes, alpha_end))
            xy_all = np.concatenate((xy[None, :, :], xy_nodes, xy_end[None, :, :]), axis=0)
            heights_all = np.r_[mean_height, height_nodes, height_end]
            geometry = read_geometry(alpha_all, xy_all, heights_all, data, coefficients, rho)
            value = float(np.max(geometry['op']))
            if value > maxima['relative_gram_operator']:
                i, j = np.unravel_index(np.argmax(geometry['op']), geometry['op'].shape)
                worst = dict(value=value, cell=int(cell), x=float(points[offset+i]),
                             r=float(data['r'][i]), phi=float(phi[j]),
                             relative_rr=float(geometry['er'][i, j]),
                             relative_rphi=float(geometry['fr'][i, j]),
                             relative_phiphi=float(geometry['gr'][i, j]))
                maxima['relative_gram_operator'] = value
            for name, key in [('relative_rr', 'er'), ('relative_rphi', 'fr'), ('relative_phiphi', 'gr')]:
                maxima[name] = max(maxima[name], float(np.max(abs(geometry[key]))))
            reference_radial = abs(data['wr'])/(1+data['w']**2)**1.5
            reference_angular = abs(data['w'])/(data['r']*np.sqrt(1+data['w']**2))
            max_reference_curvature = max(max_reference_curvature,
                float(np.max(np.maximum(reference_radial, reference_angular))))
            if np.max(geometry['curvature']) > maxima['principal_curvature']:
                i, j = np.unravel_index(np.argmax(geometry['curvature']), geometry['curvature'].shape)
                maxima['principal_curvature'] = float(geometry['curvature'][i, j])
                worst_curvature = dict(value=maxima['principal_curvature'], cell=int(cell),
                    x=float(points[offset+i]), r=float(data['r'][i]), phi=float(phi[j]),
                    background_radial_curvature=float(reference_radial[i]),
                    background_angular_curvature=float(reference_angular[i]),
                    w=float(data['w'][i]), wr=float(data['wr'][i]))
            maxima['angular_compatibility'] = max(maxima['angular_compatibility'], float(np.max(np.linalg.norm(geometry['angular_error'], axis=2))))
            maxima['sampled_mean'] = max(maxima['sampled_mean'], float(np.max(abs(data['literal_mean']))))
            minima['gram_determinant'] = min(minima['gram_determinant'], float(np.min(geometry['determinant'])))
            minima['radial_outward_speed'] = min(minima['radial_outward_speed'], float(np.min(geometry['radial_outward'])))
            for key in ('S', 'D'):
                minima[key] = min(minima[key], float(np.min(coefficients[key])))
            minima['L'] = min(minima['L'], float(np.min(all_data['fields']['L'][sl])))
            position_min = np.minimum(position_min, geometry['F'].min(axis=(0, 1)))
            position_max = np.maximum(position_max, geometry['F'].max(axis=(0, 1)))
            if previous_end is not None:
                maxima['join_Fr_jump'] = max(maxima['join_Fr_jump'], float(np.max(np.linalg.norm(geometry['Fr'][0]-previous_end[0], axis=1))))
                maxima['join_Frr_jump'] = max(maxima['join_Frr_jump'], float(np.max(np.linalg.norm(geometry['Frr'][0]-previous_end[1], axis=1))))
            previous_end = (geometry['Fr'][-1], geometry['Frr'][-1])
            height_total += height_end-mean_height
            alpha, xy, mean_height = alpha_end, xy_end, height_end
            count += len(fractions)*reader.N
    result = dict(scope=__doc__, source_sha256=source_sha, height_reader_sha256=height_sha,
                  angular_helper_sha256=helper_sha, input_sha256=hashlib.sha256(reader.raw).hexdigest(),
                  background_sha256=reader.bg.sha256, M=reader.M, N=reader.N,
                  sampled_rho_min=float(np.min(rho)), sampled_rho_max=float(np.max(rho)),
                  rho_mode_count=len(getattr(reader, 'rho_coefficients', [])),
                  height_anchor=reader.height_anchor, radial_gauss=args.radial_gauss,
                  height_coefficient_quadrature=reader.height_quadrature,
                  atomic_cells=len(cell_order), full_radial_domain=True,
                  sampled_angle_radial_points=count, one_sided_endpoints=True,
                  initial_turn_density_error=float(np.max(abs(initial_turn_error))),
                  initial_angular_compatibility=float(np.max(np.linalg.norm(initial_angular_error, axis=1))),
                  maxima=maxima, minima=minima, worst_metric=worst,
                  worst_curvature=worst_curvature, max_reference_curvature=max_reference_curvature,
                  radial_accumulation='Kahan compensated alpha, XY and mean-height increments',
                  sampled_position_min=position_min.tolist(), sampled_position_max=position_max.tolist(),
                  anchor_mean_height=args.anchor_mean_height, terminal_mean_height=float(mean_height),
                  oriented_mean_height_increment=float(height_total),
                  seconds=time.perf_counter()-started, closed_surface=False, reach_certificate=False,
                  regularity='Exact radial integral candidate is C2 on a uniformly positive branch; quadrature/branch extrema here are numerical evidence')
    if args.out:
        args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    folder = Path(__file__).parent
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--background', type=Path, required=True)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--height-reader', type=Path, default=folder/'2026-11-17-parallel-geometry-tail-readout.py')
    parser.add_argument('--angular-helper', type=Path, default=folder/'2026-11-17-parallel-model-angular-reconstruct.py')
    parser.add_argument('--angles', type=int, default=512)
    parser.add_argument('--radial-gauss', type=int, default=8)
    parser.add_argument('--height-gauss', type=int, default=8)
    parser.add_argument('--height-anchor', choices=('left', 'right'))
    parser.add_argument('--anchor-mean-height', type=float, default=0.)
    parser.add_argument('--batch-cells', type=int, default=8)
    run(parser.parse_args())
