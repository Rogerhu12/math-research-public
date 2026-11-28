#!/usr/bin/env python3
"""Build an independent predictor-only cached literal-JVP library.

The original C++ file and production binary are never modified. New methods
are inserted before diagnostics, and independent C handle exports are appended.
All original root, RHS, full-J, flow, protocol and acceptance code is retained.
The candidate is not a replacement production kernel or an accepted tail.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time


def ref(p):
    p = Path(p).resolve()
    return dict(path=str(p), sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    a = p.parse_args(); own = Path(__file__).resolve().parent
    old = a.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended'
    cpp = old/'frozen_flow_production.cpp'
    if ref(cpp)['sha256'] != 'e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf':
        raise ValueError('Review the changed original kernel before deriving a new candidate')
    out = a.outdir.resolve(); out.mkdir(parents=True, exist_ok=False)
    methods = own/'native_cached_direction_methods.inc'; exports = own/'native_cached_direction_exports.inc'
    source = cpp.read_text(); anchor = '    void diagnostics(VFDiagnostics &d) const {'
    if source.count(anchor) != 1 or source.count('#include <vector>') != 1:
        raise ValueError('Original class source anchor changed')
    derived = source.replace('#include <vector>', '#include <vector>\n#include <memory>', 1)
    derived = derived.replace(anchor, methods.read_text()+'\n'+anchor, 1)
    derived += '\n'+exports.read_text()
    dest = out/'frozen_flow_cached_directions.cpp'; dest.write_text(derived)
    shutil.copy2(old/'frozen_flow.h', out/'frozen_flow.h')
    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('The declared original compiler is unavailable')
    library = out/'libcached_directions.so'
    command = [compiler, '-std=c++17', '-O2', '-fno-fast-math', '-ffp-contract=off',
               '-fexcess-precision=standard', '-frounding-math', '-fPIC', '-shared',
               str(dest), '-o', str(library), '-lm']
    begin = time.monotonic(); process = subprocess.run(command, capture_output=True)
    (out/'compiler.stdout').write_bytes(process.stdout); (out/'compiler.stderr').write_bytes(process.stderr)
    report = dict(scope=__doc__, source=ref(__file__), original_cpp=ref(cpp),
        original_header=ref(old/'frozen_flow.h'), methods=ref(methods), exports=ref(exports),
        derived_cpp=ref(dest), compiler=ref(compiler), command=command,
        returncode=process.returncode, wall_seconds=time.monotonic()-begin,
        stdout=ref(out/'compiler.stdout'), stderr=ref(out/'compiler.stderr'),
        library=ref(library) if library.exists() else None, production_source_changed=False,
        new_library_loaded=False, new_native_JVP_executed=False, nonlinear_tail_accepted=False)
    (out/'build.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)
    if process.returncode:
        raise SystemExit(process.returncode)


if __name__ == '__main__':
    main()
