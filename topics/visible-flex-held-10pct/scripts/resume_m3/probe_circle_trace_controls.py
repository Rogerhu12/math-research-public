#!/usr/bin/env python3
"""Finite implementation checks for the new two-column circle trace definition.

No original core or solver is replaced.  Full-circle sums are finite numerical
checks; the exact zero moments and direct-sum assertion are proved in R44.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from circle_trace_controls import CircleTraceControls


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--halfwidth',type=float,default=.21)
    p.add_argument('--transition',type=float,default=.4)
    p.add_argument('--precision',type=int,default=80)
    p.add_argument('--angular',type=int,default=12288)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    basis=CircleTraceControls(a.halfwidth,a.transition,a.precision)
    phi=2*np.pi*np.arange(a.angular)/a.angular
    jets=basis.support_jets(phi,4)
    values=jets[0]
    moments=np.stack((np.mean(values,axis=1),np.mean(values*np.cos(3*phi)[None,:],axis=1)))
    arc=basis.center+np.linspace(-basis.a,basis.a,257)
    arc_jets=basis.support_jets(arc,4);arc_rho=basis.rho_jets(arc)
    radius=basis.position_increment(arc,[1.,0.])
    centre=basis.position_increment(arc,[0.,1.])
    er=np.stack((np.cos(arc),np.sin(arc)),axis=1)
    nu0=np.array([np.cos(basis.center),np.sin(basis.center)])
    periodic=basis.support_jets(phi+basis.T,0)[0]
    reflected=basis.support_jets(2*basis.center-phi,0)[0]
    library=Path(__file__).with_name('round_raw_lib')
    sys.path.insert(0,str(library))
    from complementary_moment_basis import _constants
    old=_constants(3,16,basis.a,basis.b,1,a.precision,True)
    oldG=old['gram'][:2,:2]
    raw_file=library/'complementary_moment_basis.py'
    new_file=Path(__file__).with_name('circle_trace_controls.py')
    result=dict(scope=__doc__,command=sys.argv,definition=basis.summary(),
        source_sha256={str(Path(__file__).resolve()):sha(__file__),str(new_file.resolve()):sha(new_file),
            str(raw_file.resolve()):sha(raw_file)},
        finite_full_circle_nodes=a.angular,finite_arc_nodes=len(arc),
        finite_low_moments= moments.tolist(),
        finite_low_moment_max=float(np.max(abs(moments))),
        finite_even_value_error=float(np.max(abs(values-reflected))),
        finite_C3_value_error=float(np.max(abs(values-periodic))),
        arc_support_trace_errors=dict(radius=float(np.max(abs(arc_jets[0][0]-1))),
            centre=float(np.max(abs(arc_jets[0][1]-np.cos(arc-basis.center))))),
        arc_rho_trace_errors=dict(radius=float(np.max(abs(arc_rho[0][0]-1))),
            centre=float(np.max(abs(arc_rho[0][1])))),
        actual_position_increment_errors=dict(radius_column_vs_er=float(np.max(abs(radius-er))),
            centre_column_vs_plus_nu0=float(np.max(abs(centre-nu0)))),
        current_raw_low_gram=dict(modes_used_only_for_identity=16,halfwidth=basis.a,
            transition=basis.b,new_low_gram=basis.constants['low_gram'].tolist(),
            original_low_gram=oldG.tolist(),
            binary64_max_difference=float(np.max(abs(basis.constants['low_gram']-oldG))),
            binary64_bytes_equal=basis.constants['low_gram'].tobytes()==oldG.tobytes()),
        finite_column_support_peaks=np.max(abs(values),axis=1).tolist(),
        finite_column_rho_peaks=np.max(abs(jets[0]+jets[2]),axis=1).tolist(),
        geometry_scope='The centre column moves the actual planar circle centre in +nu0. '
            'If the project writes that centre as -c*nu0, its scalar c changes by -B. '
            'No positivity, held ratio, metric, BVP existence or previous geometric constants '
            'are transferred to a modified core by these finite checks.')
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),sha256=sha(a.out),
        moment_error=result['finite_low_moment_max'],
        geometry_errors=result['actual_position_increment_errors'],
        old_low_gram_difference=result['current_raw_low_gram']['binary64_max_difference'])),flush=True)


if __name__=='__main__':main()
