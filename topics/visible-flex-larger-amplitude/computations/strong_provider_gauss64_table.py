#!/usr/bin/env python3
"""Read the exact binary64 Gauss64 table used by the provider's construction.

This is a new local table observation. It does not claim bitwise identity to an
earlier CI executor. It neither imports a physical Flow nor starts a tail worker.
"""
import argparse
import hashlib
import inspect
import json
import os
import platform
from pathlib import Path

for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import numpy as np

HERE=Path(__file__).resolve().parent
PROVIDER_SHA="f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational(value):
    n,d=float(value).as_integer_ratio()
    return str(n)+"/"+str(d)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--expected-numpy",default="2.3.5")
    parser.add_argument("--expected-python",default="3.12.14")
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh table output")
    if np.__version__!=args.expected_numpy or platform.python_version()!=args.expected_python:
        raise ValueError("Numerical runtime differs from the requested table observation")
    provider=HERE/"alternative-neck-excursion.py"
    if sha(provider)!=PROVIDER_SHA:
        raise ValueError("Original Gauss64 provider source differs")
    # Exactly the source construction; no weight normalization is added.
    gx,gw=np.polynomial.legendre.leggauss(64)
    gu=(gx+1)/2
    normalized_weights=gw/2
    if gx.shape!=(64,) or gw.shape!=(64,) or not np.all(np.isfinite(gu)) or not np.all(np.isfinite(gw)):
        raise ValueError("The complete finite original table is required")
    if not np.all(np.diff(gu)>0) or not np.all((gu>0)&(gu<1)) or not np.all(gw>0):
        raise ValueError("The original positive ordered rule is invalid")
    legendre_file=Path(inspect.getsourcefile(np.polynomial.legendre.leggauss))
    result=dict(schema="strong-provider-gauss64-binary-table-v1",
        identity=dict(source_sha256=sha(__file__),provider_source_sha256=PROVIDER_SHA,
            numpy_version=np.__version__,python_version=platform.python_version(),
            architecture=platform.machine(),numpy_legendre_file_sha256=sha(legendre_file)),
        normalized_nodes=[rational(x) for x in gu],
        normalized_weights=[rational(x) for x in normalized_weights],
        normalized_nodes_float64_le_sha256=hashlib.sha256(np.asarray(gu,dtype="<f8").tobytes()).hexdigest(),
        normalized_weights_float64_le_sha256=hashlib.sha256(np.asarray(normalized_weights,dtype="<f8").tobytes()).hexdigest(),
        source_rule="gx,gw=np.polynomial.legendre.leggauss(64); gu=(gx+1)/2",
        weight_normalization="gw/2 exactly, without renormalizing the rounded weight sum",
        original_runtime_claim="Only this observed local runtime; not the old accepted CI table",
        physical_profile_loaded=False,prior_accepted_field_loaded=False,
        original_numpy_evaluation_roundoff_paid=False,physical_RHS_calls=0,tail_workers=0,newton_solves=0)
    payload=(json.dumps(result,indent=2,allow_nan=False)+"\n").encode()
    if len(payload)>=100000:
        raise ValueError("Unexpected table size")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    temporary=args.out.with_name(args.out.name+".tmp-"+str(os.getpid()))
    try:
        with temporary.open("xb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.link(temporary,args.out)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(json.dumps(dict(event="gauss64_binary_table_observed",out=str(args.out),
        sha256=sha(args.out),physical_RHS_calls=0,tail_workers=0,newton_solves=0)),flush=True)


if __name__=="__main__":
    main()
