#!/usr/bin/env python3
"""Generate explicit new storage adapters by complete unique textual replay.

This generator only reads/compiles source text.  It imports no mathematical
backend and does not execute a producer, reader, solver, or certificate.
Every original file is pinned.  Existing output files are never overwritten.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ORIGINAL = {
 '950f-root-fullxyz-hermite.py':'4f60dbd1735268e2f4953748d12c4a87099d49ddf69dcb34d40b9f26986d0bd9',
 'db6f-root-mirror-hermite.py':'ddb785a7e5199f1488fa50937668fc5236a1dee7b24679f75b39a4f15cb7f4b6',
 'db6f-audit-continuous-hermite.py':'e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d',
 'db6f-audit-metric-polynomial.py':'02f9da4d86c7514bf90a3cfd185be85274c7ad0b9b34d3d20ede342d6b8adea4',
 'db6f-audit-metric-supplier.py':'de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0',
 'db6f-root-volume-moment.py':'502a3d8c9439ee0b707e6be7b367e356ef44d1942aa6a0615330b1005fe10913',
 'db6f-root-common-cut-v2.py':'317e519fda8d78fb70b53f8a8c80d51599dec1ac46e92741cd9b2576a3f4fa7d',
 'db6f-audit-tail-metric-curvature.py':'ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670',
 'db6f-audit-prefix-metric-budget.py':'dc5c0a569f291fdd19e77272c4d565c43a2d976d2534dc13cc47d0fb13bb451f',
 'db6f-audit-closed-budget-transfer-v3.py':'5ef8d229e0a19bc83381a2cdcaef8b24309e00a1fdc6b9409b20d7ca34092e49',
 'db6f-prefix-angular-metric-storage.py':'2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c',
 'db6f-prefix-export-closed-mesh-storage.py':'d776e41ef75741be0d5d44a8156d2c71a70ad016ef3678605d718a32ba7684d1',
 'db6f-prefix-review-closed-mesh-storage.py':'698e8b0528ffa7b1bbe1bc84c574079f60261156f1d3a6ddae048af0f9c0c479',
 'db6f-prefix-terminal-error-storage-v3.py':'8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7',
}
NEW = {
 'fullxyz':'78718-prefix-fullxyz-hermite-storage-v1.py',
 'mirror':'78718-prefix-mirror-hermite-storage-v1.py',
 'continuous':'78718-prefix-continuous-hermite-storage-v1.py',
 'polynomial':'78718-prefix-metric-polynomial-storage-v1.py',
 'supplier':'78718-prefix-metric-supplier-storage-v1.py',
 'moment':'78718-prefix-volume-moment-storage-v1.py',
 'common':'78718-prefix-common-cut-storage-v1.py',
 'arithmetic':'78718-prefix-angular-arithmetic-storage-v1.py',
 'metric_budget':'78718-prefix-metric-budget-storage-v1.py',
 'closed_budget':'78718-prefix-closed-budget-storage-v1.py',
 'angular':'78718-prefix-angular-metric-storage-v1.py',
 'export':'78718-prefix-export-closed-mesh-storage-v1.py',
 'review':'78718-prefix-review-closed-mesh-storage-v1.py',
 'terminal':'78718-prefix-terminal-error-storage-v1.py',
 'codec':'78718-prefix-byte-shards-v1.py',
 'helper':'78718-prefix-storage-v1.py',
}
CORE = {
 NEW['codec']:'e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39',
 NEW['helper']:'83cf59cfe5ab373421e53d0c0d8d2274edfc6a6b266fc2ab6161274b474a4329',
}
C_PREFIX = {
 'db6f-prefix-shared-jet-byte-shards-v2.py':('codec','b894107ca47773b259f589d0231244e3dbdf86d2285f3c3789f07e318d868c50'),
 'db6f-prefix-shared-jet-storage.py':('helper','c9d6f89b0dd3e8bca744b679ed92ef3176899c8ae30be46f8080b9e6a4b7b9c2'),
 'db6f-prefix-fullxyz-hermite-storage.py':('fullxyz','f7b3659a98d70941377a6e054fd9900a1de45518e65899da862987aae75f9ccc'),
 'db6f-prefix-mirror-hermite-storage.py':('mirror','163d3ce9b11036c4ff9effce52d02dece2f09e57f582e24ce26e9ae4162eee94'),
 'db6f-prefix-continuous-hermite-storage.py':('continuous','511b107519652feeda8f2beb3f1935a6f3078d297c3639824c0dabe75bff150c'),
 'db6f-prefix-metric-polynomial-storage.py':('polynomial','70bf1b39e23074069cd11cb5cbe180f40fb7df77b59a1c1622c274665444233d'),
 'db6f-prefix-metric-supplier-storage.py':('supplier','cf0981bcb2426c9db4dc35523e46ced805da4a90c37e47eae8a1247ccbd4aa2f'),
 'db6f-prefix-volume-moment-storage.py':('moment','fd81fd2b1ebee77bd95ce9065e4898d5ef03b8bf72e99e3d0858f401b16818c1'),
 'db6f-prefix-common-cut-storage.py':('common','b994ce2e777eb24f744489ea2a6be96a74764fc75a0b3cea2e6d2d387efc4d3b'),
 'db6f-prefix-angular-arithmetic-storage.py':('arithmetic','d27282a9820d35023b74171bad3cc208429e5b0451d47d3175b7b001caa591c9'),
 'db6f-prefix-metric-budget-storage.py':('metric_budget','0009368a049809d3d5864a6ca1adc8e52fbbade1f7b3e184b024b1093408f0c1'),
 'db6f-prefix-closed-budget-storage.py':('closed_budget','dc07d80f74a1cb880132e91ef0296f972e7e550a278eac057975fb8b032a09e9'),
 'db6f-prefix-angular-metric-storage.py':('angular','2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c'),
}
BANNER = '# New 78718 explicit storage adaptation; original mathematical source is retained below.\n'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def function_nodes(text):
    found = {}
    def walk(node, prefix=''):
        for item in ast.iter_child_nodes(node):
            if isinstance(item, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                name = prefix+item.name
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    found[name] = ast.dump(item, include_attributes=False)
                walk(item, name+'.')
            else:
                walk(item, prefix)
    walk(ast.parse(text))
    return found


class Transform:
    def __init__(self, old, new):
        self.old, self.new = old, new
        self.original = (HERE/old).read_bytes()
        require(sha(self.original) == ORIGINAL[old], 'Original source changed: '+old)
        self.text = self.original.decode('utf-8')
        self.steps = []
        first = self.text.splitlines(keepends=True)[0]
        self.replace(first, first+BANNER, 'Explicit new source identity; comment only')

    def replace(self, old, new, reason):
        require(old != new and self.text.count(old) == 1,
                'Replacement is not unique in '+self.old+': '+repr(old[:100]))
        self.text = self.text.replace(old, new, 1)
        self.steps.append({'old': old, 'new': new, 'reason': reason})

    def rename(self, old, new, reason='Explicit source filename/hash binding'):
        """Use a unique complete-line context for every occurrence, in order."""
        while old in self.text:
            pos = self.text.index(old)
            start = self.text.rfind('\n', 0, pos)+1
            end = self.text.find('\n', pos)
            end = len(self.text) if end < 0 else end+1
            while self.text.count(self.text[start:end]) != 1:
                require(start > 0 or end < len(self.text), 'No unique replacement context')
                if start > 0:
                    start = self.text.rfind('\n', 0, start-1)+1
                if end < len(self.text):
                    nxt = self.text.find('\n', end)
                    end = len(self.text) if nxt < 0 else nxt+1
            fragment = self.text[start:end]
            self.replace(fragment, fragment.replace(old, new, 1), reason)

    def storage_import(self):
        if self.old == 'db6f-audit-continuous-hermite.py':
            self.replace('import numpy as np\n\n\ndef down(x):',
                         'import numpy as np\nimport importlib.util\n\n'
                         'HERE = Path(__file__).resolve().parent\n\n\ndef down(x):',
                         'Add only the explicit storage loader imports/path to a reader with no original HERE')
        matches = re.findall(r'^HERE\s*=\s*Path\(__file__\)\.resolve\(\)\.parent$', self.text, re.M)
        require(len(matches) == 1, 'Missing unique HERE assignment')
        old = matches[0]+'\n'
        new = old+"\n_storage_spec = importlib.util.spec_from_file_location(\n    'prefix_78718_explicit_storage', HERE/'78718-prefix-storage-v1.py')\nstorage = importlib.util.module_from_spec(_storage_spec)\n_storage_spec.loader.exec_module(storage)\n"
        self.replace(old, new, 'Explicit new storage helper import; no numerical callback change')

    def close(self):
        compile(self.text, self.new, 'exec', dont_inherit=True)
        oldnodes, newnodes = function_nodes(self.original.decode()), function_nodes(self.text)
        require(set(oldnodes) == set(newnodes), 'Mathematical function set unexpectedly changed')
        identical = sorted(k for k in oldnodes if oldnodes[k] == newnodes[k])
        changed = sorted(set(oldnodes)-set(identical))
        replay = self.original.decode()
        for step in self.steps:
            require(replay.count(step['old']) == 1, 'Replay lost unique source fragment')
            replay = replay.replace(step['old'], step['new'], 1)
        require(replay == self.text, 'Full-source replay differs')
        return self.text.encode(), {'old': self.old, 'old_bytes': len(self.original),
            'old_sha256': sha(self.original), 'new': self.new,
            'new_bytes': len(self.text.encode()), 'new_sha256': sha(self.text.encode()),
            'replacements': self.steps, 'unchanged_ast_functions': identical,
            'changed_ast_functions_requiring_storage_diff_review': changed}


def build_all():
    output, transformations = {}, []
    for name, expected in CORE.items():
        raw = (HERE/name).read_bytes()
        require(sha(raw) == expected, 'Tested core source changed: '+name)
        output[name] = raw

    def add(t):
        raw, row = t.close(); output[t.new] = raw; transformations.append(row)

    t = Transform('950f-root-fullxyz-hermite.py', NEW['fullxyz']); t.storage_import()
    t.replace("    out_data = args.out_prefix.with_name(args.out_prefix.name+'-data.npz.gz')\n    out_data.write_bytes(gzip.compress(payload.getvalue(), mtime=0))\n    if out_data.stat().st_size >= 5_000_000:\n        raise ValueError('Checkpoint exceeds the repository file-size limit')\n",
              "    logical_payload = gzip.compress(payload.getvalue(), mtime=0)\n    storage_record = storage.write_payload(args.out_prefix, logical_payload,\n                                           nodes=len(mesh), modes=M)\n",
              'Only physical storage after the unchanged original NPZ serialization')
    t.replace('        data_file=out_data.name, data_sha256=sha(out_data),\n',
              "        data_storage=storage_record, data_sha256=storage_record['logical_sha256'],\n",
              'Explicit storage reference; data SHA still identifies the original logical gzip/NPZ')
    t.replace("    print(json.dumps({'data_bytes': out_data.stat().st_size}))\n",
              "    print(json.dumps({'logical_data_bytes': len(logical_payload),\n                      'storage_descriptor': storage_record['descriptor_file']}))\n",
              'Storage-only console summary')
    t.replace("        data_path = Path(meta_path).parent/self.meta['data_file']\n        if sha(data_path) != self.meta['data_sha256']:\n            raise ValueError('Geometry data hash mismatch')\n        raw = np.load(io.BytesIO(gzip.decompress(data_path.read_bytes())),\n                      allow_pickle=False)\n",
              "        stored_meta, payload, self.storage_bindings = storage.read_payload(meta_path, verify_arrays=True)\n        if stored_meta != self.meta:\n            raise ValueError('Geometry metadata changed during storage read')\n        raw = np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False)\n",
              'Only logical-container acquisition; all original SharedHermite arithmetic follows unchanged')
    add(t)

    t = Transform('db6f-root-mirror-hermite.py', NEW['mirror']); t.storage_import()
    t.rename('950f-root-fullxyz-hermite.py', NEW['fullxyz'])
    t.replace("    data_path = meta_path.parent / meta['data_file']\n    saved = np.load(io.BytesIO(gzip.decompress(data_path.read_bytes())),\n                    allow_pickle=False)\n",
              "    stored_meta, payload, _storage_bindings = storage.read_payload(meta_path, verify_arrays=True)\n    if stored_meta != meta:\n        raise ValueError('Base metadata changed during storage read')\n    saved = np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False)\n",
              'Read the original logical payload before unchanged mirror parity statements')
    t.replace("    data_path.write_bytes(gzip.compress(stream.getvalue(), mtime=0))\n    if data_path.stat().st_size >= 5_000_000:\n        raise RuntimeError('Data exceeds the repository size limit')\n",
              "    logical_payload = gzip.compress(stream.getvalue(), mtime=0)\n    storage_record = storage.write_payload(args.out_prefix, logical_payload,\n                                           nodes=meta['nodes'], modes=meta['modes'])\n",
              'Only physical storage after the unchanged mirror NPZ serialization')
    t.replace('        data_sha256=sha(data_path), wrapper_sha256=sha(__file__),\n',
              "        data_storage=storage_record, data_sha256=storage_record['logical_sha256'],\n        wrapper_sha256=sha(__file__),\n",
              'Bind the modified logical payload and the explicit new wrapper identity')
    add(t)

    t = Transform('db6f-audit-continuous-hermite.py', NEW['continuous']); t.storage_import()
    t.replace("        data=self.path.parent/self.meta['data_file']\n        if sha(data)!=self.meta['data_sha256']:raise ValueError('Data hash mismatch')\n        raw=np.load(io.BytesIO(gzip.decompress(data.read_bytes())),allow_pickle=False)\n",
              "        stored_meta,payload,self.storage_bindings=storage.read_payload(self.path,verify_arrays=True)\n        if stored_meta!=self.meta:raise ValueError('Geometry metadata changed during storage read')\n        raw=np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False)\n",
              'Only logical-container acquisition before unchanged exact/interval arithmetic')
    t.replace("             data_sha256=geom.meta['data_sha256'],script_sha256=sha(__file__),\n",
              "             data_sha256=geom.meta['data_sha256'],script_sha256=sha(__file__),\n             storage_bindings=geom.storage_bindings,\n",
              'Certificate provenance adds the actual prefix storage closure')
    add(t)

    t = Transform('db6f-audit-metric-polynomial.py', NEW['polynomial'])
    t.rename('db6f-audit-continuous-hermite.py', NEW['continuous'])
    t.replace("             supplier_claim=target.get('analytic_definition'),\n",
              "             storage_bindings=geom.storage_bindings,\n             supplier_claim=target.get('analytic_definition'),\n",
              'Report provenance only; target bytes and all metric arithmetic unchanged')
    add(t)

    t = Transform('db6f-audit-metric-supplier.py', NEW['supplier'])
    t.rename('db6f-audit-metric-polynomial.py', NEW['polynomial'])
    t.replace('    output=dict(scope=__doc__,geometry_file=str(args.geometry),geometry_sha256=sha(args.geometry),\n',
              '    output=dict(scope=__doc__,geometry_file=str(args.geometry),geometry_sha256=sha(args.geometry),\n        geometry_storage_bindings=geom.storage_bindings,\n',
              'Report provenance only; original target construction and storage unchanged')
    add(t)

    t = Transform('db6f-root-volume-moment.py', NEW['moment'])
    t.rename('db6f-audit-continuous-hermite.py', NEW['continuous'])
    t.replace("        'geometry_sha256':iv.sha(args.geometry),'data_sha256':geom.meta['data_sha256'],\n",
              "        'geometry_sha256':iv.sha(args.geometry),'data_sha256':geom.meta['data_sha256'],\n        'storage_bindings':geom.storage_bindings,\n",
              'Report provenance only; original moment arithmetic unchanged')
    add(t)

    t = Transform('db6f-root-common-cut-v2.py', NEW['common']); t.storage_import()
    for old, new in [('db6f-audit-continuous-hermite.py',NEW['continuous']),
                     ('db6f-audit-metric-polynomial.py',NEW['polynomial']),
                     ('db6f-root-volume-moment.py',NEW['moment'])]: t.rename(old,new)
    t.replace("            rawpath=oldpath.parent/self.meta['data_file']\n            raw=np.load(io.BytesIO(gzip.decompress(rawpath.read_bytes())),allow_pickle=False)\n",
              "            stored_meta,payload,bindings=storage.read_payload(oldpath,verify_arrays=True)\n            if stored_meta!=self.meta or bindings!=self.storage_bindings:\n                raise ValueError('Defining base changed during common-cut storage read')\n            raw=np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False)\n",
              'Second read uses the same defining base and its original mode count; correction math unchanged')
    t.replace("    raw=np.load(io.BytesIO(gzip.decompress((args.geometry.parent/old['data_file']).read_bytes())),allow_pickle=False)\n",
              "    stored_meta,payload,_storage_bindings=storage.read_payload(args.geometry,verify_arrays=True)\n    if stored_meta!=old:raise ValueError('Defining base changed during common-cut make')\n    raw=np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False)\n",
              'Common-cut make reads the defining base bytes; all node/mode/width formulas unchanged')
    add(t)

    t = Transform('db6f-audit-tail-metric-curvature.py', NEW['arithmetic'])
    t.rename('db6f-audit-metric-polynomial.py',NEW['polynomial'])
    add(t)
    t = Transform('db6f-audit-prefix-metric-budget.py', NEW['metric_budget'])
    t.rename('db6f-audit-tail-metric-curvature.py',NEW['arithmetic'])
    t.rename('db6f-root-common-cut-v2.py',NEW['common'])
    add(t)
    t = Transform('db6f-audit-closed-budget-transfer-v3.py', NEW['closed_budget'])
    t.replace("    implementations=[HERE/'db6f-root-common-cut.py',HERE/'db6f-root-common-cut-v2.py']\n",
              "    implementations=[HERE/'78718-prefix-common-cut-storage-v1.py']\n",
              'Explicit new prefix implementation family; no widening of old tail/transfer identities')
    t.rename('db6f-audit-continuous-hermite.py',NEW['continuous'])
    t.replace("      'same_background_transfer':transfer_binding,\n",
              "      'same_background_transfer':transfer_binding,\n      'prefix_storage_bindings':shape.storage_bindings,\n",
              'Report actual prefix storage closure; all original scalar inequalities unchanged')
    add(t)

    def migrate_C(oldfile, newkey):
        t = Transform(oldfile, NEW[newkey])
        for oldname, (key, oldhash) in C_PREFIX.items():
            if key == newkey:
                continue
            if oldname in t.text or oldhash in t.text:
                require(NEW[key] in output, 'New dependency not yet generated: '+key)
                t.rename(oldname,NEW[key])
                t.rename(oldhash,sha(output[NEW[key]]), 'Bind explicit new prefix source bytes; original tail source table retained')
        return t

    add(migrate_C('db6f-prefix-angular-metric-storage.py','angular'))
    add(migrate_C('db6f-prefix-export-closed-mesh-storage.py','export'))
    t = migrate_C('db6f-prefix-review-closed-mesh-storage.py','review')
    t.rename('db6f-prefix-export-closed-mesh-storage.py',NEW['export'])
    t.rename(ORIGINAL['db6f-prefix-export-closed-mesh-storage.py'],sha(output[NEW['export']]),
             'Reviewer binds exact new exporter bytes')
    t.replace('"reviewer": "/root/coupled_prefix explicit storage-interface adaptation",',
              '"reviewer": "78718 new storage interface; actual independent runner recorded separately",',
              'Honest new implementation provenance, without claiming independent execution')
    add(t)
    add(migrate_C('db6f-prefix-terminal-error-storage-v3.py','terminal'))
    return output, transformations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-dir',type=Path,required=True)
    parser.add_argument('--ledger',type=Path,required=True)
    args=parser.parse_args()
    require(not args.ledger.exists(),'Refusing to replace an existing ledger')
    output,rows=build_all()
    args.out_dir.mkdir(parents=True,exist_ok=True)
    for name,raw in output.items():
        path=args.out_dir/name
        require(not path.exists() or path.read_bytes()==raw,
                'Refusing to overwrite an existing output: '+str(path))
    ledger={'schema':'78718-complete-storage-source-transformations-v1',
        'status':'PURE_SOURCE_GENERATION_NOT_PRODUCTION_ACCEPTANCE',
        'builder_sha256':sha(Path(__file__).read_bytes()),
        'core_sources':CORE,'new_source_names':NEW,'transformations':rows,
        'mathematical_backend_calls':0,'solver_calls':0,
        'scope':'Complete unique textual replay and compile only. Changed function bodies require semantic storage review; no blanket unchanged-math claim is inferred from AST counts.'}
    raw=(json.dumps(ledger,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
    require(len(raw)<1_000_000,'Source ledger unexpectedly exceeds small-JSON budget')
    for name,blob in output.items():
        path=args.out_dir/name
        if not path.exists():
            with path.open('xb')as stream:stream.write(blob)
    with args.ledger.open('xb')as stream:stream.write(raw)
    print(json.dumps({'status':ledger['status'],'generated_adapters':len(rows),
        'core_files':len(CORE),'replacement_steps':sum(len(r['replacements'])for r in rows),
        'unchanged_function_instances':sum(len(r['unchanged_ast_functions'])for r in rows),
        'ledger_bytes':len(raw),'ledger_sha256':sha(raw),'solver_calls':0}))


if __name__=='__main__':main()
