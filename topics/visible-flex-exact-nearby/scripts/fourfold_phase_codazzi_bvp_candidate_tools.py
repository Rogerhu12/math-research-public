#!/usr/bin/env python3
"""Construct or diagnose finite Codazzi BVP candidates without changing them.

The initial-guess command interpolates old-geometry curvature only. The
waist command records the retained mean, total turning, and the exact rule
for a fourfold closed initial curve, plus floating geometric differences.
No cap regularity or exact PDE solution is asserted.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline,PPoly
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_core_low_block import uniform_fields
from fourfold_phase_codazzi_two_end_probe import save_npz_gz,load_candidate
from fourfold_phase_codazzi_two_end_homotopy_probe import ChunkedTwoEnded
from fourfold_phase_local_correction_probe import sha,scalar_target,source_and_geometry,correction_norms,angular_derivative


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=['old-guess','waist'])
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--modes',type=int,default=32);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--radial-nodes',type=int,default=251);p.add_argument('--right',type=float,default=.25)
    p.add_argument('--candidate',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();geometry,definition=load_exact_object(args.object,512)
    if args.command=='old-guess':
        system=ChunkedTwoEnded(geometry,args.modes,args.angles)
        r=np.linspace(0.,args.right,args.radial_nodes)
        values=np.column_stack([system.old_fields(x) for x in r]);poly=CubicSpline(r,values.T)
        metadata=dict(kind='old_actual_geometry_curvature_initial_guess_only',object_sha256=sha(args.object),
            source_sha256=sha(__file__),modes=args.modes,boundary_amplitude=1.,physical_frequency_factor=4,
            state_order='B sine k=1..M, C cosine k=0..M')
        save_npz_gz(args.candidate,radial_nodes=r,piece_coefficients=poly.c,initial_state=values[:,0],
            right_boundary_C_nonmean=values[args.modes+1:,-1],metadata=np.array(json.dumps(metadata)))
        doc=dict(**metadata,certified=False,angular_grid=args.angles,radial_nodes=args.radial_nodes,
            right=args.right,candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
            limitations=['A floating interpolatory INITIAL GUESS, not a solution of either the finite or full Codazzi PDE.'])
    else:
        saved=load_candidate(args.candidate);metadata=json.loads(str(saved['metadata']));m=int(metadata['modes'])
        if metadata['object_sha256']!=sha(args.object):raise ValueError('different target object')
        poly=PPoly(saved['piece_coefficients'],saved['radial_nodes']);initial=poly(0.)
        t=scalar_target(geometry,0.);a=t['a'];c=initial[m:].copy();grid=args.angles
        theta=np.arange(grid)*np.pi/(2*grid);freq=4*np.arange(1,m+1)
        cosine=np.cos(freq[:,None]*theta);sine=np.sin(freq[:,None]*theta)
        phase=-(a*c[1:]/freq)@sine
        C=-1/a+c[1:]@cosine
        Y=np.column_stack([-np.sin(phase),np.cos(phase),np.zeros(grid)])
        normal=np.column_stack([np.cos(phase),np.sin(phase),np.zeros(grid)])
        tangent_phase=np.exp(1j*phase);k=4*np.fft.fftfreq(grid,1/grid)
        planar=grid*np.fft.ifft(a*np.fft.fft(tangent_phase)/grid/(k+1))
        F=np.column_stack([planar.real,planar.imag,np.zeros(grid)])
        P=np.zeros_like(F);P[:,2]=np.sqrt(t['E'])
        fields=(F,P,a*Y,(t['E']*t['K']/C)[:,None]*normal,np.zeros_like(F),(a*a*C)[:,None]*normal)
        old=uniform_fields(geometry,0.,grid);old_geom=source_and_geometry(old,t)
        new_geom=source_and_geometry(fields,t);V=tuple(v-o for v,o in zip(fields,old))
        end=poly(float(saved['radial_nodes'][-1]));boundary=saved['right_boundary_C_nonmean']
        doc=dict(kind='floating_BVP_waist_mean_turning_and_fourfold_closure_diagnostic',certified=False,
            source_sha256=sha(__file__),object_sha256=sha(args.object),input_candidate_path=str(args.candidate),
            input_candidate_sha256=sha(args.candidate),input_metadata=metadata,angular_grid=grid,
            original_target_fixed=True,initial_waist_curve_changed=True,
            floating_target_a0=a,initial_B_coefficient_l1=float(np.sum(abs(initial[:m]))),
            initial_C_mean=float(c[0]),required_initial_C_mean=-1/a,
            initial_mean_gap=float(c[0]+1/a),raw_initial_total_turn=float(-2*np.pi*a*c[0]),
            raw_initial_turn_number=float(-a*c[0]),
            exact_mean_repair_rule='C(0,theta)=-1/a_true(0)+sum_{k=1}^M c_k cos(4k theta)',
            exact_phase_rule='beta(theta)=-a_true(0)*sum_{k=1}^M c_k*sin(4k theta)/(4k)',
            exact_closure_identity='The repaired tangent is i*exp(i theta+i beta(theta)); beta is pi/2-periodic. The four quarter integrals sum by 1+i-1-i=0. Its turn is exactly 2pi, and X0=ez gives identity frame holonomy.',
            sampled_repaired_C_range=[float(np.min(C)),float(np.max(C))],
            sampled_waist_support_min=float(np.min(np.sum(F*normal,axis=1))),
            sampled_primitive_tangent_mismatch=float(np.max(np.linalg.norm(angular_derivative(F)-a*Y,axis=1))),
            sampled_repaired_metric_defect=float(np.max(new_geom['metric_norm'])),
            sampled_repaired_source=float(np.max(abs(new_geom['q']))),
            correction_vs_old_waist=correction_norms(V,old_geom),
            free_outer_C_mean=float(end[m]),outer_nonmean_C_boundary_difference_l1=float(np.sum(abs(end[m+1:]-boundary))),
            true_outer_condition_identity=metadata.get('right_boundary','initial guess, no imposed true cap condition'),
            regular_port=None,outer_mean_was_not_prescribed=True,
            limitations=['All displayed numerical gaps and geometric norms are floating samples, not certified.',
                'The exact mean/phase rules describe a legitimate new initial curve; they do not turn the input finite BVP into an exact PDE solution.',
                'Only nonmean outer C was specified. No full cap DN, regular-port response or global closure is imposed.'])
    doc['exact_center_parameter']=definition['delta_fraction']
    doc['dependency_sha256']={s:sha(Path(__file__).with_name(s)) for s in
        ('fourfold_phase_codazzi_two_end_probe.py','fourfold_phase_codazzi_two_end_homotopy_probe.py',
         'fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py',
         'fourfold_phase_local_correction_probe.py')}
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print({k:doc[k] for k in ('kind','initial_mean_gap','raw_initial_turn_number','sampled_repaired_C_range',
        'correction_vs_old_waist') if k in doc})


if __name__=='__main__':main()
