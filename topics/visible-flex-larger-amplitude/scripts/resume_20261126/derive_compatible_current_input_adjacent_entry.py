#!/usr/bin/env python3
"""Regenerate six complete current-input-compatible adjacent-frame sources.

Only full text, SHA, AST and byte compilation are used; no numerical module is
imported. The immutable parent sources and complete replacement producer remain
required. The full original numerical solver suffix is retained byte-for-byte.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import py_compile

MANIFEST = json.loads(r'''{
  "schema": "complete-compatible-current-input-adjacent-source-derivation-v1",
  "parents": {
    "so3_reference_centred_adjacent_frame_material_envelope_geometry.py": "c253ef1559d00a2da2a961df10f47843e9f82b2c8dd17071a064b56042c5ac4e",
    "transfer_material_envelope_memory_to_adjacent_frames.py": "eb22d711122da4e9db99a032f84560a32358f11a543b91757d9e83cc149bc2ee",
    "fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py": "91c86a4fed296cda92a9ac522dace21fb7e0ab603c288226b5cc8e7c3b8f44b6",
    "launch_reference_centred_adjacent_frame_material_envelope_so3_actions.py": "90423119843e0d4e4ab584c9476785b8b4bc3bd8fac50776571fc14711844ffa",
    "read_reference_centred_adjacent_frame_material_envelope_so3_report.py": "c0cc0011498154a171e401d9874d34f060242180d341d6d2ea2b85eb963455dd",
    "complete_material_envelope_memory_current_restorer.py": "5f22ad999b33a657d5e59721f3d6459b3411faabb180a475cd3fd989b662fba0"
  },
  "renames": {
    "so3_reference_centred_adjacent_frame_material_envelope_geometry.py": "so3_reference_centred_compatible_frame_material_envelope_geometry.py",
    "transfer_material_envelope_memory_to_adjacent_frames.py": "transfer_material_envelope_memory_to_compatible_frames.py",
    "fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py": "fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py",
    "launch_reference_centred_adjacent_frame_material_envelope_so3_actions.py": "launch_reference_centred_compatible_frame_material_envelope_so3_actions.py",
    "read_reference_centred_adjacent_frame_material_envelope_so3_report.py": "read_reference_centred_compatible_frame_material_envelope_so3_report.py",
    "complete_material_envelope_memory_current_restorer.py": "complete_material_envelope_memory_compatible_current.py"
  },
  "patches": {
    "so3_reference_centred_adjacent_frame_material_envelope_geometry.py": [
      [
        "5f22ad999b33a657d5e59721f3d6459b3411faabb180a475cd3fd989b662fba0",
        "1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9"
      ]
    ],
    "transfer_material_envelope_memory_to_adjacent_frames.py": [
      [
        "5f22ad999b33a657d5e59721f3d6459b3411faabb180a475cd3fd989b662fba0",
        "1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9"
      ]
    ],
    "fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py": [
      [
        "so3_reference_centred_adjacent_frame_material_envelope_geometry.py",
        "so3_reference_centred_compatible_frame_material_envelope_geometry.py"
      ],
      [
        "c253ef1559d00a2da2a961df10f47843e9f82b2c8dd17071a064b56042c5ac4e",
        "ba98027d88f2949e902af90bc9fe19cb0e18c0e758512c18382798e1a050425b"
      ],
      [
        "transfer_material_envelope_memory_to_adjacent_frames.py",
        "transfer_material_envelope_memory_to_compatible_frames.py"
      ],
      [
        "eb22d711122da4e9db99a032f84560a32358f11a543b91757d9e83cc149bc2ee",
        "f3264400100cabbf717c4e07cae70d7cabca8403bc6c8b4c46c726da3eb6f10a"
      ],
      [
        "complete_material_envelope_memory_current_restorer.py",
        "complete_material_envelope_memory_compatible_current.py"
      ],
      [
        "5f22ad999b33a657d5e59721f3d6459b3411faabb180a475cd3fd989b662fba0",
        "1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9"
      ],
      [
        "                                 '1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9')}",
        "                                 '1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9'),\n 'independent_input_projection_producer': ('scripts/resume_20261126/restore_actual_run05_carrier_for_compatible_current_run08.py',\n                                           '6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19')}"
      ]
    ],
    "launch_reference_centred_adjacent_frame_material_envelope_so3_actions.py": [
      [
        "fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py",
        "fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py"
      ],
      [
        "91c86a4fed296cda92a9ac522dace21fb7e0ab603c288226b5cc8e7c3b8f44b6",
        "5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191"
      ]
    ],
    "read_reference_centred_adjacent_frame_material_envelope_so3_report.py": [
      [
        "fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py",
        "fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py"
      ],
      [
        "91c86a4fed296cda92a9ac522dace21fb7e0ab603c288226b5cc8e7c3b8f44b6",
        "5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191"
      ]
    ],
    "complete_material_envelope_memory_current_restorer.py": [
      [
        "import hashlib\n",
        "import hashlib\nimport importlib.util\n"
      ],
      [
        "import struct\n",
        "import struct\nimport sys\n"
      ],
      [
        "RESTORER_SHA = '8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449'",
        "RESTORER_SHA = '6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19'\nCURRENT_COMPATIBILITY_PRODUCER_NAME = 'restore_actual_run05_carrier_for_compatible_current_run08.py'"
      ],
      [
        "def _point_key(",
        "\ndef _validate_actual_current_binding(binding, *, actual_model=None, current_carrier=None,\n        current_preparation_report=None, current_reference_bundle=None,\n        current_node_report=None, current_scalar_input=None):\n    \"\"\"Verify the entire actual current projection with the whole pinned producer.\"\"\"\n    if not isinstance(binding,dict):\n        raise ValueError('The complete actual current path binding is required')\n    value=binding.get('current_input_compatibility')\n    if (not isinstance(value,dict)\n            or binding.get('current_input_compatibility_identity_sha256')!=canonical(value)\n            or value.get('producer_source_sha256')!=RESTORER_SHA\n            or binding.get('origin_carrier')!=value.get('historical_carrier')\n            or binding.get('current_carrier')!=value.get('current_carrier')):\n        raise ValueError('Current projection and whole old/current carrier evidence disagree')\n    records=dict(current_carrier=current_carrier,\n        current_preparation_report=current_preparation_report,\n        current_reference_bundle=current_reference_bundle,current_node_report=current_node_report,\n        current_scalar_input=current_scalar_input)\n    for key,actual in list(records.items()):\n        declared=value.get(key)\n        if not isinstance(declared,dict):\n            raise ValueError('Missing full current projection file record '+key)\n        if actual is None:\n            records[key]=copy.deepcopy(declared)\n        elif actual!=declared:\n            raise ValueError('The actual caller input differs from its full producer '+key)\n    preparation=_read_bound_json(records['current_preparation_report'])\n    model=preparation.get('reference_definition')\n    if (not isinstance(model,dict) or preparation.get('source_sha256')!=PREPARATION_SHA\n            or preparation.get('schema')!='R690-independent-axisymmetric-SO3-preparation-v1'\n            or preparation.get('complete') is not True\n            or preparation.get('reference_model_identity_sha256')!=canonical(model)\n            or (actual_model is not None and actual_model!=model)):\n        raise ValueError('Bind the same actual complete frozen reference model')\n    path=Path(__file__).with_name(CURRENT_COMPATIBILITY_PRODUCER_NAME)\n    if sha(path)!=RESTORER_SHA:\n        raise ValueError('Use the complete current projection producer source')\n    module_name='_complete_run08_current_projection_'+RESTORER_SHA[:16]\n    spec=importlib.util.spec_from_file_location(module_name,path)\n    if spec is None or spec.loader is None:\n        raise ValueError('The full current projection source cannot be loaded')\n    module=importlib.util.module_from_spec(spec)\n    sys.modules[module_name]=module\n    spec.loader.exec_module(module)\n    if (sha(module.__file__)!=RESTORER_SHA\n            or sha(module.validate_current_input_compatibility.__code__.co_filename)!=RESTORER_SHA):\n        raise ValueError('The actual complete projection validator source differs')\n    result=module.validate_current_input_compatibility(value,actual_model=model,**records)\n    if (result.get('producer_source_sha256')!=RESTORER_SHA\n            or result.get('compatibility_identity_sha256')!=canonical(value)\n            or result.get('actual_current_model_identity_sha256')!=canonical(model)\n            or result.get('whole_old_carrier_and_full_current_input_bytes_rechecked') is not True\n            or result.get('same_complete_scalar_formula_and_fixed_chart') is not True\n            or result.get('scientific_certificates_inherited') is not False):\n        raise ValueError('The full actual projection validator did not return its binding')\n    return result\n\ndef _point_key("
      ],
      [
        "            or actual_model.get('original_warm_bundle_sha256') != ORIGIN_WARM_SHA\n",
        ""
      ],
      [
        "    if binding_path is None:\n        if current['record']['sha256'] != ORIGIN_CARRIER_SHA:\n",
        "    current_projection_validation = None\n    if binding_path is None:\n        if (current['record']['sha256'] != ORIGIN_CARRIER_SHA\n                or actual_model.get('original_warm_bundle_sha256') != ORIGIN_WARM_SHA):\n"
      ],
      [
        "        binding = dict(binding, binding_file=binding_record)\n",
        "        binding = dict(binding, binding_file=binding_record)\n        current_projection_validation = _validate_actual_current_binding(binding,\n            actual_model=actual_model,current_carrier=current['record'],\n            current_preparation_report=file_record(args.preparation_report),\n            current_reference_bundle=file_record(args.reference_bundle),\n            current_node_report=file_record(args.node_report),current_scalar_input=file_record(args.scalar_input))\n"
      ],
      [
        "        legacy_angle_reinterpretation='literal historical angles retained as material phi0; no same physical point assertion')",
        "        legacy_angle_reinterpretation='literal historical angles retained as material phi0; no same physical point assertion',\n        current_input_compatibility_validation=current_projection_validation)"
      ],
      [
        "    memory = value.get('actual_separation_memory',{})\n",
        "    path_binding=bound.get('actual_path_binding',{})\n    current_projection_validation=None\n    if path_binding.get('identical_whole_file_directly_read') is not True:\n        verified_path_binding=validate_public_binding(path_binding,current_input=current)\n        current_projection_validation=_validate_actual_current_binding(\n            verified_path_binding,current_carrier=current)\n    elif (current.get('sha256')!=ORIGIN_CARRIER_SHA\n            or origin!=current or path_binding.get('origin_carrier')!=origin\n            or path_binding.get('current_carrier')!=current):\n        raise ValueError('A direct historical whole-file case cannot represent different current input')\n    memory = value.get('actual_separation_memory',{})\n"
      ],
      [
        "        actual_separation_memory_count=len(rows),actual_separation_memory_sha256=canonical(rows),\n",
        "        actual_separation_memory_count=len(rows),actual_separation_memory_sha256=canonical(rows),\n        current_input_compatibility_validation=current_projection_validation,\n"
      ]
    ]
  },
  "outputs": {
    "so3_reference_centred_compatible_frame_material_envelope_geometry.py": {
      "bytes": 68275,
      "sha256": "ba98027d88f2949e902af90bc9fe19cb0e18c0e758512c18382798e1a050425b",
      "blob": "8cf309bff99484e0e495aedfcb73203de512f9e1"
    },
    "transfer_material_envelope_memory_to_compatible_frames.py": {
      "bytes": 55758,
      "sha256": "f3264400100cabbf717c4e07cae70d7cabca8403bc6c8b4c46c726da3eb6f10a",
      "blob": "9a455377464e30e257accf52ca6bdbd2ad06129c"
    },
    "fullclosed_reference_centred_compatible_frame_material_envelope_so3_qp.py": {
      "bytes": 74542,
      "sha256": "5c5c2c944c030682bc85470089590a4d3f1536049942d6a3de6cf79e38ed2191",
      "blob": "d1465a44df2f6db6a3df89302f3d32fa83167a91"
    },
    "launch_reference_centred_compatible_frame_material_envelope_so3_actions.py": {
      "bytes": 20745,
      "sha256": "a52e4b54d7785b226a255c5d938892198164858907795e93337c529a8b2c625e",
      "blob": "10da3889d88f0476a45867c7f65b7afab039586d"
    },
    "read_reference_centred_compatible_frame_material_envelope_so3_report.py": {
      "bytes": 95632,
      "sha256": "475fa6d8505611d8198debc97f5bb4101fb18c10312835178d486e3c366a927e",
      "blob": "0eb931055c4f52acff1e77bb27757cf48c058308"
    },
    "complete_material_envelope_memory_compatible_current.py": {
      "bytes": 45188,
      "sha256": "1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9",
      "blob": "2055669a80513243f5644129def4185bc48d63c7"
    }
  },
  "restorer": {
    "name": "restore_actual_run05_carrier_for_compatible_current_run08.py",
    "sha256": "6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19"
  },
  "science_suffix_sha256": "3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5"
}''')

def sha(data):
    return hashlib.sha256(data if isinstance(data,bytes) else data.encode()).hexdigest()

def derive(parent):
    outputs={}
    for name,digest in MANIFEST['parents'].items():
        source=parent[name]
        if sha(source)!=digest:
            raise ValueError('Entire parent source differs: '+name)
        for old,new in MANIFEST['patches'][name]:
            if source.count(old)!=1:
                raise ValueError('Complete source anchor changed: '+name)
            source=source.replace(old,new,1)
        target=MANIFEST['renames'][name]
        if sha(source)!=MANIFEST['outputs'][target]['sha256']:
            raise ValueError('Complete regenerated source differs: '+target)
        ast.parse(source,filename=target)
        outputs[target]=source
    original='fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py'
    marker='    def save_report():\n'
    old=parent[original]
    new=outputs[MANIFEST['renames'][original]]
    old=old[old.index(marker):]
    new=new[new.index(marker):]
    if old!=new or sha(new)!=MANIFEST['science_suffix_sha256']:
        raise ValueError('Full original scientific solver suffix changed')
    return outputs

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent-directory',required=True,type=Path)
    p.add_argument('--restorer-source',required=True,type=Path)
    p.add_argument('--outdir',required=True,type=Path)
    p.add_argument('--verify-existing',action='store_true')
    args=p.parse_args()
    if sha(args.restorer_source.read_bytes())!=MANIFEST['restorer']['sha256']:
        raise ValueError('Require the entire actual current-projection producer')
    parent={name:(args.parent_directory/name).read_text()
        for name in MANIFEST['parents']}
    outputs=derive(parent)
    args.outdir.mkdir(parents=True,exist_ok=True)
    records=[]
    for name,source in outputs.items():
        target=args.outdir/name
        if args.verify_existing:
            if target.read_bytes()!=source.encode():
                raise ValueError('The existing whole source differs: '+name)
        else:
            target.write_text(source)
        py_compile.compile(str(target),doraise=True)
        records.append(dict(name=name,bytes=len(source.encode()),sha256=sha(source)))
    print(json.dumps(dict(science_executed=False,complete_sources=records),indent=2))

if __name__=='__main__':
    main()
