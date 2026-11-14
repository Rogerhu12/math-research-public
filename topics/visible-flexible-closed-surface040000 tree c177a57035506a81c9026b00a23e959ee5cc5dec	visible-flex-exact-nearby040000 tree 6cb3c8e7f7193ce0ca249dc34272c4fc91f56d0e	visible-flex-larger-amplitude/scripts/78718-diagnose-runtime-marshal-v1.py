#!/usr/bin/env python3
"""Read-only diagnostic of recorded/imported/recompiled code serialization.

This does not replace, relax, or invoke a success gate.  No mathematical
callback, BVP, DN, Jacobian constructor, or factory is executed.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import marshal
from pathlib import Path
import sys
from types import CodeType


FIELDS = ('co_argcount','co_posonlyargcount','co_kwonlyargcount','co_nlocals',
          'co_stacksize','co_flags','co_code','co_consts','co_names','co_varnames',
          'co_filename','co_name','co_qualname','co_firstlineno','co_linetable',
          'co_exceptiontable','co_freevars','co_cellvars')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def deep_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, CodeType):
        return all(deep_equal(getattr(a,k),getattr(b,k)) for k in FIELDS)
    if isinstance(a, tuple):
        return len(a)==len(b) and all(deep_equal(x,y) for x,y in zip(a,b))
    return a == b


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reproduction',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    rep=json.loads(args.reproduction.read_text())
    launch_path=Path(rep['launch']['path']);launch=json.loads(launch_path.read_text())
    if sys.executable!=launch['command'][0]:raise ValueError('Interpreter differs from launch')
    expected='59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2'
    bvp=importlib.import_module('scipy.integrate._bvp');path=Path(bvp.__file__)
    if sha(path.read_bytes())!=expected:raise ValueError('Original SciPy source differs')
    rows=[]
    for name,row in rep['csc_selection']['original_runtime'].items():
        if Path(row['filename']).resolve()!=path.resolve():raise ValueError('Runtime filename differs')
        tree=compile(path.read_bytes(),row['filename'],'exec',dont_inherit=True)
        found=[x for x in tree.co_consts if isinstance(x,CodeType) and x.co_name==name]
        if len(found)!=1:raise ValueError('Ambiguous compiled function')
        live=getattr(bvp,name).__code__;rebuilt=found[0]
        versions={}
        for version in range(5):
            a,b=marshal.dumps(live,version),marshal.dumps(rebuilt,version)
            first=next((i for i,(x,y)in enumerate(zip(a,b))if x!=y),None)
            if first is None and len(a)!=len(b):first=min(len(a),len(b))
            versions[str(version)]={'equal':a==b,'imported_bytes':len(a),'recompiled_bytes':len(b),
                'imported_sha256':sha(a),'recompiled_sha256':sha(b),
                'first_different_offset':first,
                'first_imported_octet':a[first]if first is not None and first<len(a)else None,
                'first_recompiled_octet':b[first]if first is not None and first<len(b)else None}
        rows.append({'function':name,'recorded_digest':row['code_sha256'],
            'fresh_imported_digest_matches_recorded':sha(marshal.dumps(live))==row['code_sha256'],
            'code_objects_compare_equal':live==rebuilt,
            'all_listed_code_fields_equal_recursively':deep_equal(live,rebuilt),
            'code_field_equalities':{k:deep_equal(getattr(live,k),getattr(rebuilt,k))for k in FIELDS},
            'versions':versions})
    result={'schema':'78718-runtime-marshal-read-only-diagnostic-v1',
        'status':'RECORDED_SERIALIZATION_DIAGNOSTIC_NOT_GATE_REPLACEMENT',
        'sys_executable':sys.executable,'sys_version':sys.version,'sys_flags':repr(sys.flags),
        'marshal_version':marshal.version,'compiler_dont_inherit':True,
        'compiler_filename':'exact row filename retained','source_file':str(path),
        'source_sha256':expected,'reproduction_sha256':sha(args.reproduction.read_bytes()),
        'launch_sha256':sha(launch_path.read_bytes()),'diagnostic_script_sha256':sha(Path(__file__).read_bytes()),
        'rows':rows,'all_fresh_imports_match_recorded':all(x['fresh_imported_digest_matches_recorded']for x in rows),
        'all_code_fields_equal':all(x['all_listed_code_fields_equal_recursively']for x in rows),
        'v4_mismatch_functions':[x['function']for x in rows if not x['versions']['4']['equal']],
        'scope':'Observed serialization differences for these four pinned functions in this runtime. No general claim of marshal canonicality or complete recorded selected-function audit is made. The frozen gate remains unchanged and run02 remains failed.',
        'old_gate_modified':False,'solver_calls':0,'callback_calls':0,'run02_success':False}
    raw=(json.dumps(result,indent=2,allow_nan=False)+'\n').encode()
    if len(raw)>=100_000:raise ValueError('Unexpectedly large diagnostic report')
    with args.out.open('xb')as f:f.write(raw)
    print(json.dumps({'status':result['status'],'all_fresh_imports_match_recorded':result['all_fresh_imports_match_recorded'],
        'all_code_fields_equal':result['all_code_fields_equal'],'v4_mismatch_functions':result['v4_mismatch_functions'],
        'v0_all_equal':all(x['versions']['0']['equal']for x in rows),
        'report_bytes':len(raw),'report_sha256':sha(raw),'solver_calls':0}))


if __name__=='__main__':main()
