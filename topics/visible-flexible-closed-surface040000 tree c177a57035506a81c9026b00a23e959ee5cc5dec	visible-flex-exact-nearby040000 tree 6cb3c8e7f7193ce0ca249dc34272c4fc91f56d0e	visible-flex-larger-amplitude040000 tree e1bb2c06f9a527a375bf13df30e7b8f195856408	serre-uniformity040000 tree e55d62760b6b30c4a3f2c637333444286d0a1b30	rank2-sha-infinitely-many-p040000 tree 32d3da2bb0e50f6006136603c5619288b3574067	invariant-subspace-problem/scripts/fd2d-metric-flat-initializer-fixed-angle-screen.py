#!/usr/bin/env python3
"""Compare the same finite initial function in fixed seed normal angle.

This recovered diagnostic makes no physical metric change. It retains the
original radial mesh (including previous blend knots), sets U=U_seed(xi), and
projects only the unknown correction in that coordinate. Saved arrays have
this explicit chart and must not be passed to a moving-chart reader.
No BVP, ODE, or full-surface certificate is produced.
"""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fd2d_recovered_angular_base',
    HERE/'fd2d-metric-flat-initializer-angular-screen.py')
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
OriginalProblem=base.RawLiftedDAE


class FixedSeedAngle:
    def __init__(self,theta,geometry):
        self.theta=np.asarray(theta,float);self.geometry=geometry

    def coordinates(self,x,coordinate=None):
        x=np.atleast_1d(np.asarray(x,float))
        xi=self.theta if coordinate is None else np.atleast_1d(np.asarray(coordinate,float))
        seed=self.geometry.material_coordinate(xi)
        def repeat(key):
            return np.broadcast_to(np.asarray(seed[key],float)[:,None],(len(xi),len(x))).copy()
        u,ux,uxx=repeat('u'),repeat('u_phi'),repeat('u_phi_phi')
        zero=np.zeros_like(u);radial=np.zeros_like(x)
        return dict(u=u,u_xi=ux,u_xixi=uxx,u_s=zero.copy(),u_sxi=zero.copy(),
            u_ss=zero.copy(),advection=zero.copy(),beta=radial.copy(),
            beta_s=radial.copy(),beta_ss=radial.copy())


class FixedSeedProblem(OriginalProblem):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.chart=FixedSeedAngle(self.chart.theta,self.geometry)
        self.coords=self.chart.coordinates(self.x)
        self._operator_cache={}


def main():
    parser=base.parser()
    parser.description=__doc__
    parser.set_defaults(out_prefix=base.TOP/'notes/2026-11-12-fd2d-metric-flat-initializer-fixed-angle-screen-recovery01')
    args=parser.parse_args()
    base.RawLiftedDAE=FixedSeedProblem
    reports=[]
    for K in args.modes:
        row=base.screen_one(K,args)
        row['angular_chart']='fixed balanced-seed normal xi; material u=U_seed(xi) at every x'
        row['blend_interval_active']=False
        row['retained_old_blend_knots_in_radial_mesh']=list(row['blend_interval'])
        row['coordinate_override_source']=base.identity(__file__)
        row['must_not_be_read_as_moving_chart']=True
        if row.get('reference_K7') is not None:
            row['reference_K7']['interpretation']='Different angular charts: coefficient differences are not a reconstruction failure'
        out=Path(str(args.out_prefix)+f'-k{K}.json')
        out.write_text(json.dumps(row,indent=2)+'\n')
        reports.append(row)
    output=Path(str(args.out_prefix)+'-report.json')
    output.write_text(json.dumps(dict(schema='fd2d-flat-initializer-fixed-normal-screens-recovery-v1',
        source=base.identity(__file__),base_source=base.identity(base.__file__),
        reports=reports,continuous_certificate=False,
        stored_array_chart='fixed seed normal, never the radially moving chart'),indent=2)+'\n')
    print(json.dumps(dict(complete=True,report=str(output))),flush=True)


if __name__=='__main__':main()
