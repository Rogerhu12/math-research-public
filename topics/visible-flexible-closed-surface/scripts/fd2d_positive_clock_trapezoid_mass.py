#!/usr/bin/env python3
"""Read-only mass diagnostic for the R131 clock on an actual saved mesh.

No GC state, ODE, BVP or physical profile is solved or modified.  The exact
clock integral over a reference coast is its actual physical length; this
compares that identity with the endpoint trapezoid used on the saved mesh.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    root=Path(__file__).resolve().parent.parent
    ap.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    ap.add_argument('--state',type=Path,default=root/'notes/2026-11-12-fd2d-local-recovery01-k15.npz')
    ap.add_argument('--upper-gap',type=float,default=2.25e-13)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();data=np.load(args.state,allow_pickle=False)
    mesh=np.asarray(data['mesh'],dtype=float)
    if np.any(np.diff(mesh)<=0):raise ValueError('Saved mesh is not strictly ordered')
    expected=str(np.asarray(data['candidate_sha256']).item())
    if digest(args.candidate)!=expected:raise ValueError('Saved mesh candidate identity differs')
    profile=PositiveCoastDesignProfile(args.candidate)
    points=[('reference_T',profile.reference_T),('near_physical_upper',profile.model.Tmax-args.upper_gap)]
    runs=[]
    for label,T in points:
        profile.set_parameter(T);jets=profile.jet(mesh);coasts=[]
        for index in (profile.model.shallow,profile.model.deep):
            old,new=profile.base.segments[index],profile.current.segments[index]
            left,right=old['s0'],old['s1']
            il=int(np.argmin(abs(mesh-left)));ir=int(np.argmin(abs(mesh-right)))
            if abs(mesh[il]-left)>5e-14 or abs(mesh[ir]-right)>5e-14 or ir<=il:
                raise ValueError('Actual saved mesh does not contain both coast endpoints')
            x=mesh[il:ir+1];J=jets['radial_scale'][il:ir+1];s=jets['s'][il:ir+1]
            widths=np.diff(x);trap=widths*(J[:-1]+J[1:])/2
            exact_cell=np.diff(s);total=float(np.sum(trap));true=float(new['L'])
            floor=float((widths[0]+widths[-1])/2)
            coasts.append(dict(label=old.get('label'),piece_index=int(index),
                reference_x_interval=[left,right],saved_mesh_indices=[il,ir],
                saved_node_count=len(x),saved_cell_count=len(widths),
                endpoint_x_errors=[float(x[0]-left),float(x[-1]-right)],
                reference_length=float(old['L']),actual_physical_length=true,
                actual_ratio=float(new['L']/old['L']),
                trapezoid_clock_mass=total,absolute_mass_error=total-true,
                relative_mass_error=(total-true)/true,
                exact_clock_map_mass_from_nodes=float(np.sum(exact_cell)),
                exact_map_mass_roundoff=float(np.sum(exact_cell)-true),
                shrinking_coast_trapezoid_limit_on_fixed_mesh=floor,
                nodes=x.tolist(),radial_scale_nodes=J.tolist(),
                physical_s_nodes=s.tolist(),trapezoid_cell_masses=trap.tolist(),
                exact_map_cell_masses=exact_cell.tolist(),
                note='The exact integral is L(T), not the finite trapezoid value. The shrink-limit formula holds for fixed interior nodes as q tends to zero.'))
        runs.append(dict(label=label,T=T,actual_distance_from_Tmax=float(profile.model.Tmax-T),coasts=coasts))
    report=dict(schema='fd2d-positive-clock-trapezoid-mass-v1',actual_execution=True,
        source_sha256=digest(__file__),candidate=dict(file=args.candidate.name,sha256=digest(args.candidate)),
        saved_state=dict(file=args.state.name,sha256=digest(args.state),mesh_nodes=len(mesh),
            modes=int(np.asarray(data['modes']).item())),
        profile_source_sha256=digest(root/'scripts/fd2d_gc_design_profile_positive.py'),
        profile_base_source_sha256=digest(root/'scripts/fd2d_gc_design_profile.py'),
        physical_Tmax=profile.model.Tmax,requested_upper_gap=args.upper_gap,runs=runs,
        exact_identity='Integral of s_x over each reference coast equals its current physical length.',
        scope='Only a finite quadrature/coordinate diagnostic on an actual saved mesh. No ODE/BVP solved, no geometry or nonexistence conclusion.',
        seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),seconds=report['seconds'],
        runs=[dict(label=r['label'],T=r['T'],coasts=[{k:c[k] for k in ('label','saved_cell_count','actual_physical_length','trapezoid_clock_mass','absolute_mass_error','relative_mass_error','shrinking_coast_trapezoid_limit_on_fixed_mesh')} for c in r['coasts']]) for r in runs]),allow_nan=False))


if __name__=='__main__':main()
