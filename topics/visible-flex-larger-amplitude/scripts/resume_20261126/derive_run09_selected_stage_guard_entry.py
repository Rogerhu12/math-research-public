#!/usr/bin/env python3
"""Reproduce four complete run09 sources after the actual selected-stage guard failure.

Pure source/text construction only.  No runtime module is imported and no
scientific field, root, matrix, fixture or numerical example is evaluated.
Every complete public parent and every complete output is bound by bytes and
SHA256. Old filenames are retained; each result has an independent v2 basename.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

SCHEMA = 'complete-run09-selected-stage-guard-source-reproducer-v1'
PARENT_PUBLIC_COMMIT = '53e8565c7688e1cd2b7c3d4055832ce3ebe86bb5'
EXACT_SCIENTIFIC_SUFFIX_SHA256 = 'd4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376'
EXACT_SCIENTIFIC_SUFFIX_BYTES = 19574
SPECS = json.loads(r'''[
  {
    "role": "geometry",
    "name": "so3_run09_public_reference_analytic_frame_geometry_v2.py",
    "bytes": 68903,
    "sha256": "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13",
    "git_blob_sha": "6d3ddb2f52fc19b60566a567a3b5e2e747887b8a",
    "parent_name": "so3_run09_public_reference_analytic_frame_geometry.py",
    "parent_sha256": "ef121193668791c9c7bc10e8e72314c74ab3c32eff530a4a39dc2ec61d17d409",
    "parent_bytes": 68903,
    "replacements": [
      [
        "all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained",
        "all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained"
      ]
    ]
  },
  {
    "role": "driver",
    "name": "fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py",
    "bytes": 80726,
    "sha256": "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
    "git_blob_sha": "eab240470226ff883e618281c3d23be6ccc3b686",
    "parent_name": "fullclosed_run09_public_reference_analytic_frame_so3_qp.py",
    "parent_sha256": "e3cb0f5a0d4b6e0c4771514470a4729a7042505691e5bba02a79fba789a2e141",
    "parent_bytes": 80723,
    "replacements": [
      [
        "so3_run09_public_reference_analytic_frame_geometry.py",
        "so3_run09_public_reference_analytic_frame_geometry_v2.py"
      ],
      [
        "ef121193668791c9c7bc10e8e72314c74ab3c32eff530a4a39dc2ec61d17d409",
        "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"
      ]
    ]
  },
  {
    "role": "launcher",
    "name": "launch_run09_public_reference_analytic_frame_actions_v2.py",
    "bytes": 21359,
    "sha256": "c1888457b67c85185aebe6c91d2bd4942ccc2d2074407e17f7f54a2825927d23",
    "git_blob_sha": "029e86780126fdbfb19daf42bc63f6191465e432",
    "parent_name": "launch_run09_public_reference_analytic_frame_actions.py",
    "parent_sha256": "84d453f5dbade82fd10fcbf390d49eb190c063c89cd174dc599c6004f9b46ccd",
    "parent_bytes": 21356,
    "replacements": [
      [
        "fullclosed_run09_public_reference_analytic_frame_so3_qp.py",
        "fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py"
      ],
      [
        "e3cb0f5a0d4b6e0c4771514470a4729a7042505691e5bba02a79fba789a2e141",
        "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
      ]
    ]
  },
  {
    "role": "reader",
    "name": "read_run09_public_reference_analytic_frame_so3_report_v2.py",
    "bytes": 97351,
    "sha256": "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32",
    "git_blob_sha": "ee2e71bddb759a659c683cdb4871d06cbb39aa4b",
    "parent_name": "read_run09_public_reference_analytic_frame_so3_report.py",
    "parent_sha256": "47409b634fe48ffd79738d2456494fdf97db50b1ce00b3553b72f164f263b5aa",
    "parent_bytes": 97348,
    "replacements": [
      [
        "fullclosed_run09_public_reference_analytic_frame_so3_qp.py",
        "fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py"
      ],
      [
        "e3cb0f5a0d4b6e0c4771514470a4729a7042505691e5bba02a79fba789a2e141",
        "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
      ]
    ]
  }
]''')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def functions(tree):
    answer = {}
    def visit(nodes, prefix=''):
        for node in nodes:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                answer[prefix+node.name] = ast.dump(node, include_attributes=False)
            elif isinstance(node, ast.ClassDef):
                visit(node.body, prefix+node.name+'.')
    visit(tree.body)
    return answer


def literal(tree, name):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(v,ast.Name) and v.id==name for v in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError('Missing complete literal '+name)


def reproduce(source_directory, output_directory):
    source_directory = Path(source_directory).resolve()
    output_directory = Path(output_directory).resolve()
    if source_directory == output_directory:
        raise ValueError('Use a distinct source-only output directory; keep every old source')
    prepared = []
    parent_driver = new_driver = None
    for spec in SPECS:
        source_path = source_directory/spec['parent_name']
        raw = source_path.read_bytes()
        if len(raw)!=spec['parent_bytes'] or digest(raw)!=spec['parent_sha256']:
            raise ValueError('The whole published parent changed: '+spec['parent_name'])
        text = raw.decode('utf-8')
        old_text = text
        for before, after in spec['replacements']:
            if text.count(before)!=1:
                raise ValueError('A declared exact replacement is not unique in '+spec['parent_name'])
            text=text.replace(before,after)
        result=text.encode('utf-8')
        if len(result)!=spec['bytes'] or digest(result)!=spec['sha256'] or len(result)>=100000:
            raise ValueError('The whole declared output differs: '+spec['name'])
        old_tree=ast.parse(old_text,filename=spec['parent_name'])
        tree=ast.parse(text,filename=spec['name'])
        compile(text,spec['name'],'exec',dont_inherit=True)
        if any(line.rstrip()!=line for line in text.splitlines()):
            raise ValueError('Unexpected trailing whitespace')
        old_functions,new_functions=functions(old_tree),functions(tree)
        if set(old_functions)!=set(new_functions):
            raise ValueError('Do not add or remove a complete runtime function')
        changed=[key for key in old_functions if old_functions[key]!=new_functions[key]]
        expected={'geometry':['GeometryScreen.__init__'],'driver':[],
            'launcher':['main'],'reader':['read_report']}[spec['role']]
        if changed!=expected:
            raise ValueError('The exact function-change scope differs: '+spec['role']+' '+repr(changed))
        for node in ast.walk(tree):
            if isinstance(node,ast.Dict):
                keys=[key.value for key in node.keys if isinstance(key,ast.Constant)]
                if len(keys)!=len(set(keys)):
                    raise ValueError('A literal dict contains duplicate keys')
        if spec['role']=='driver':
            marker='    def save_report():'
            old_suffix=old_text[old_text.index(marker):].encode()
            suffix=text[text.index(marker):].encode()
            if (old_suffix!=suffix or len(suffix)!=EXACT_SCIENTIFIC_SUFFIX_BYTES
                    or digest(suffix)!=EXACT_SCIENTIFIC_SUFFIX_SHA256):
                raise ValueError('The original complete scientific loop/packet hooks changed')
            old_pins,new_pins=literal(old_tree,'SOURCE_PINS'),literal(tree,'SOURCE_PINS')
            if len(new_pins)!=58 or set(old_pins)!=set(new_pins):
                raise ValueError('Preserve the complete 58-role source closure')
            if [key for key in old_pins if old_pins[key]!=new_pins[key]]!=['geometry']:
                raise ValueError('Only the geometry source role changes')
            if new_pins['geometry']!=('scripts/resume_20261126/'+SPECS[0]['name'],SPECS[0]['sha256']):
                raise ValueError('Bind the exact new complete geometry body')
            parent_driver,new_driver=old_text,text
        prepared.append((spec,result,changed,len(new_functions)))
    output_directory.mkdir(parents=True,exist_ok=True)
    records=[]
    for spec,raw,changed,count in prepared:
        path=output_directory/spec['name']
        if path.exists() and path.read_bytes()!=raw:
            raise FileExistsError('Do not overwrite an independently different source: '+str(path))
        if not path.exists():
            with path.open('xb') as stream:
                stream.write(raw)
        records.append(dict(name=spec['name'],bytes=len(raw),sha256=digest(raw),
            parent_name=spec['parent_name'],parent_bytes=spec['parent_bytes'],
            parent_sha256=spec['parent_sha256'],exact_replacement_count=len(spec['replacements']),
            complete_functions=count,changed_functions=changed))
    report=dict(schema=SCHEMA,parent_public_commit=PARENT_PUBLIC_COMMIT,
        source_sha256=digest(Path(__file__).read_bytes()),outputs=records,
        scientific_suffix_bytes=EXACT_SCIENTIFIC_SUFFIX_BYTES,
        scientific_suffix_sha256=EXACT_SCIENTIFIC_SUFFIX_SHA256,
        complete_runtime_source_role_count=58,
        complete_parent_and_output_bytes_checked=True,stdlib_AST_and_compile_only=True,
        runtime_modules_imported=False,scientific_or_fixture_execution=False,
        old_sources_modified=False)
    report_path=output_directory/'source-only-reproduction.json'
    report_raw=(json.dumps(report,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    if report_path.exists() and report_path.read_bytes()!=report_raw:
        raise FileExistsError('A previous source-only reproduction record differs')
    if not report_path.exists():
        with report_path.open('xb') as stream:
            stream.write(report_raw)
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-directory',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    report=reproduce(args.source_directory,args.out)
    print(json.dumps(report,sort_keys=True,separators=(',',':'),allow_nan=False))


if __name__=='__main__':
    main()
