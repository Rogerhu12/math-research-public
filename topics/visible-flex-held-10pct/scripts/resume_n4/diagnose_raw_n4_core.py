#!/usr/bin/env python3
"""Check the independent original core and the nested raw n4 definition."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from tight_moment_interval_bounds import install,PROVENANCE as INTERVAL_PROVENANCE
install()
import large_radius_local_core
from plateau_core import PlateauSupportCore
from raw_n4_complementary import make_raw_basis,provenance


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scalar_summary(core):
    value=core.summary()
    out={k:v for k,v in value.items()if not isinstance(v,(dict,list))}
    out['control_certificate']={k:v for k,v in value['control_certificate'].items()if not isinstance(v,(dict,list))}
    return out


def identity(first,second):
    theta=2*np.pi*np.arange(4097)/4097
    ga,gb=first.evaluate(theta),second.evaluate(theta)
    out={key:float(abs(ga[key]-gb[key]).max())for key in ('F','Ft','Ftt')}
    if max(out.values())>2e-10:
        raise ArithmeticError('Complete core identity failed')
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    rec=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    J=rec['config']['modes'];q=rec['gauge_amplitude']
    if rec.get('fixed_metric') or rec['plateau_settings']['homotopy']!=0:
        raise ValueError('This check needs an original lambda=0 design checkpoint')
    corrections=np.array(rec['parameters'][1:])*np.array(rec['central_correction_scales'])
    corrections[0]=0.
    settings=rec['plateau_settings']
    Original=large_radius_local_core.make_core_class(PlateauSupportCore)
    # Instantiate the independent original before changing its module globals.
    original=Original(q,corrections,4,arc_nodes=1024,**settings)
    original_basis_type=type(original.basis).__name__
    RawBasis=make_raw_basis(J)
    large_radius_local_core.ComplementaryMomentBasis=RawBasis
    Raw=large_radius_local_core.make_core_class(PlateauSupportCore)
    new=Raw(q,corrections,4,arc_nodes=1024,**settings)
    assert type(original.basis) is not type(new.basis)
    results=dict(
        scope='Exact defining constraints plus independent floating evaluation checks. No BVP is solved by this diagnostic.',
        input_checkpoint_sha256=sha(args.checkpoint),script_sha256=sha(__file__),
        source_provenance=provenance(J),interval_provenance=INTERVAL_PROVENANCE,
        original_basis_type=original_basis_type,raw_basis_type=type(new.basis).__name__,
        q=q,eta=settings['bimodal_eta'],J=J,
        lambda_zero_complete_identity=identity(original,new),
        rows={})
    gx,gw=np.polynomial.legendre.leggauss(128)
    basis=new.basis
    marks=np.unique(np.mod([0.,basis.T,basis.center,basis.center-basis.a-basis.eps,
                           basis.center-basis.a,basis.center+basis.a,basis.center+basis.a+basis.eps],basis.T))
    marks=np.r_[marks,basis.T]
    mean=np.zeros(J-1);c8=np.zeros(J-1)
    for lo,hi in zip(marks[:-1],marks[1:]):
        phi=(lo+hi)/2+(hi-lo)/2*gx
        values=basis.support_jets(phi,0,1.)[0]
        mean+=(hi-lo)/2*(values@gw)/basis.T
        c8+=(hi-lo)/basis.T*(values@(gw*np.cos(8*phi)))
    results['independent_low_moment_quadrature']=dict(
        gaussian_order=128,mean_max_abs=float(abs(mean).max()),
        c8_max_abs=float(abs(c8).max()))
    if max(abs(mean).max(),abs(c8).max())>2e-12:
        raise ArithmeticError('Raw low-moment implementation audit failed')
    for lam in (0.,.001,.02,.1,1.):
        kw={**settings,'homotopy':lam}
        small=Raw(q,corrections,4,arc_nodes=1024,**kw)
        large=Raw(q,np.pad(corrections,(0,4)),4,arc_nodes=1024,**kw)
        row=scalar_summary(small)
        row['nested_M_plus_4_complete_identity']=identity(small,large)
        if lam==1.:
            phi=small.center+np.linspace(-small.a,small.a,257)
            rho=small.normal_geometry(phi)['rho']
            jets=small.basis.primitive_jets(phi,5,1.)
            row['protected_control_jets_max']=max(float(abs(v).max())for v in jets)
            row['protected_rho_constant_error']=float(abs(rho-(1+q*small._circle_constant)).max())
        results['rows'][str(lam)]=row
    args.out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(sha256=sha(args.out),bytes=args.out.stat().st_size,
                          initial_identity=results['lambda_zero_complete_identity'],
                          low_moments=results['independent_low_moment_quadrature'],
                          nested_identity_max=max(max(r['nested_M_plus_4_complete_identity'].values())for r in results['rows'].values()))))


if __name__=='__main__':main()
