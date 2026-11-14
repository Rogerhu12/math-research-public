#!/usr/bin/env python3
"""Original native/body consumer, with transparent gzip transport for NPZ bytes.

Only the native module's array-file reader is wrapped. All array values,
source identities, Hermite definitions, physical equations and body ODEs
remain those of the supplied actual report. No new BVP is solved.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,importlib.util,io,json,sys
from pathlib import Path
import numpy as np
import fd2d_gc_native_log_field as native


class CompressedArchiveReader:
    def __getattr__(self,key):return getattr(np,key)
    def load(self,file,*args,**kwargs):
        if isinstance(file,(str,Path)) and str(file).endswith('.gz'):
            return np.load(io.BytesIO(gzip.decompress(Path(file).read_bytes())),*args,**kwargs)
        return np.load(file,*args,**kwargs)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--angles',type=int,default=32);p.add_argument('--rtol',type=float,default=2e-10)
    p.add_argument('--atol',type=float,default=2e-12);a=p.parse_args()
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    manifest=a.out_prefix.with_name(a.out_prefix.name+'-native-field.json')
    native.np=CompressedArchiveReader()
    native.write_native_definition(a.report,manifest)
    record=json.loads(manifest.read_text())
    record['lossless_npz_transport']=dict(source=native.identity(__file__),
        operation='gzip.decompress to original NPZ bytes; numpy.load(allow_pickle=False)',
        all_numerical_array_values_unchanged=True,original_native_source_unchanged=True)
    manifest.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    source=Path(__file__).with_name('fd2d-gc-body-actual-prefix.py')
    spec=importlib.util.spec_from_file_location('actual_body_compressed_transport',source)
    body=importlib.util.module_from_spec(spec);spec.loader.exec_module(body)
    sys.argv=[str(source),'--field',str(manifest),'--out-prefix',str(a.out_prefix),
              '--angles',str(a.angles),'--rtol',str(a.rtol),'--atol',str(a.atol)]
    body.main()


if __name__=='__main__':main()
