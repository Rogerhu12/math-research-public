#!/usr/bin/env python3
"""Rebuild accurate B32 scalar packet and a minimal actual new-entry check.

No BVP, whole body, or whole-mesh Jacobian is run. Newly generated outputs
have new identities; unavailable earlier packet/source hashes are not used.
"""
from __future__ import annotations
import argparse,json,time,hashlib
from fractions import Fraction
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_r136_arb_profile import ends,bound_record,_encode,aq
from fd2d_gc_r181_b_arb_profile_recovery import R181BRecoveryArbProfile
from fd2d_gc_r181_b_round_raw_recovery import (
    R181BRecoveryRoundRawBumpDAE,checkpoint_arrays,DEFAULT_CANDIDATE)


def write_json(path,data):
    path=Path(path)
    if path.exists():raise FileExistsError(path)
    path.write_text(json.dumps(data,sort_keys=True,indent=2,allow_nan=False)+'\n')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--candidate',type=Path,default=DEFAULT_CANDIDATE)
    ap.add_argument('--modes',type=int,default=7)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--taylor-order',type=int,default=24)
    args=ap.parse_args();started=time.perf_counter()
    prefix=args.out_prefix;prefix.parent.mkdir(parents=True,exist_ok=True)
    paths={key:Path(str(prefix)+suffix) for key,suffix in (
        ('packet','-packet.json.gz'),('report','-report.json'),
        ('bumps','-bumps.json'),('definition','-entry-definition.json'),
        ('circle','-circle-zero-field.npz'))}
    if any(path.exists() for path in paths.values()):raise FileExistsError('Use a new actual output prefix')
    problem=R181BRecoveryRoundRawBumpDAE(args.candidate,modes=args.modes,gap=0.,gap_scale=.64)
    accurate=R181BRecoveryArbProfile(args.candidate,supports=problem.profile.supports,
        delta=np.zeros(7),precision=args.precision,taylor_order=args.taylor_order)
    endpoint=accurate.endpoint_jets()
    cut_a=ends(endpoint['a']);cut_v=ends(endpoint['a_s']);cut_acc=ends(endpoint['a_ss'])
    endpoint_ok=(cut_a[0]<=Fraction(4,5)<=cut_a[1]
        and cut_v==(Fraction(-1),Fraction(-1))
        and cut_acc==(Fraction(0),Fraction(0)))
    if not endpoint_ok:raise AssertionError('The declared exact cut interval was not enclosed')
    positive=all(p['L']>0 for p in accurate.pieces)
    if not positive or not all(row['exact_shared_two_jet'] for row in accurate.join_identities):
        raise AssertionError('Actual new phase resolution failed')
    packet_identity=accurate.save_packet(paths['packet'])
    again=R181BRecoveryArbProfile.from_packet(paths['packet'],expected_sha256=packet_identity['sha256'])
    if again.input_binding_sha256!=accurate.input_binding_sha256:
        raise AssertionError('New accurate packet transport changed identity')
    write_json(paths['bumps'],dict(schema='fd2d-R181-B32-recovery-new-physical-bumps-v1',
        source=identity(__file__),candidate=identity(args.candidate),
        supports=problem.profile.supports.tolist(),
        supports_exact=[[str(Fraction.from_float(float(v))) for v in row] for row in problem.profile.supports],
        delta=[0.]*7,old_supports_transferred=False))
    write_json(paths['definition'],problem.definition())
    np.savez_compressed(paths['circle'],**checkpoint_arrays(problem,problem.initial_vector()))
    # Three-point kernel only. The complete saved mesh is NOT assembled.
    view=problem.radial_view(np.array([0.,.65,problem.profile.end]))
    z=view.initial_vector();y,p=view.unpack(z)
    p[view.central_slice]=np.linspace(.002,.004,view.K)
    p[view.tail_slice]=np.linspace(.017,.023,16)
    p[view.profile_slice]=np.linspace(-1e-6,1e-6,7)
    rng=np.random.default_rng(18107)
    y[1]=rng.normal(size=view.q)*1e-4
    z=view.impose_linear_boundary_values(z)
    direction=rng.normal(size=view.size)*1e-3
    dy,dp=view.unpack(direction);dp[view.profile_slice]*=1e-3
    direction=view.impose_linear_boundary_values(direction)
    f,J,data=view.evaluate(z,jacobian=True)
    tangent=J@direction
    checks=[]
    for step in (2e-5,5e-6):
        fp=view.evaluate(z+step*direction,jacobian=False)[0]
        fm=view.evaluate(z-step*direction,jacobian=False)[0]
        finite=(fp-fm)/(2*step)
        error=float(np.max(abs(finite-tangent))/max(1.,float(np.max(abs(tangent)))))
        checks.append(dict(step=step,maximum_scaled_error=error))
    if min(row['maximum_scaled_error'] for row in checks)>2e-7:
        raise AssertionError('Actual three-point nonzero JVP discrepancy')
    zero=view.initial_vector();fz,dz=view.evaluate(zero,jacobian=False)
    # The reference and zero tail have zero cut values by definition.
    cut_zero=float(np.max(abs(dz['fields'][:,-1])))
    report=dict(schema='fd2d-R181-B32-recovery-computable-entry-check-v1',
        source=identity(__file__),candidate=identity(args.candidate),
        accurate_definition=accurate.definition(),packet=packet_identity,
        accurate_endpoint=_encode(endpoint),
        accurate_minus_numeric_end=bound_record(accurate.end-aq(Fraction.from_float(problem.profile.end))),
        resolved_positive_lengths=bool(positive),join_count=len(accurate.join_identities),
        packet_reload_same_binding=True,endpoint_contains_exact_symbolic_cut=endpoint_ok,
        finite_kernel=dict(physical_points=view.x.tolist(),nonzero_JVP=checks,
            circle_three_point_residual_max=float(np.max(abs(fz))),
            circle_cut_II_max=cut_zero,
            node_count_of_saved_definition=problem.N,
            point_count_actually_assembled=view.N,
            same_source_as_unavailable_87bde=False),
        physical_constraints=dict(central=view.core(p[view.central_slice])[0].definition(),
            tail=view.tail_control_box.certificate(p[view.tail_slice]),
            radius=view.profile_radius_domain_certificate(p[view.profile_slice])),
        outputs={k:identity(v) for k,v in paths.items() if k!='report'},
        seconds=time.perf_counter()-started,passed=True,
        BVP_started=False,whole_body_run=False,whole_saved_mesh_F_or_J=False,
        nonround_solution_claimed=False)
    write_json(paths['report'],report)
    print(json.dumps(dict(report=str(paths['report']),packet=str(paths['packet']),
        passed=True,seconds=report['seconds'],packet_sha256=packet_identity['sha256']),sort_keys=True))


if __name__=='__main__':main()
