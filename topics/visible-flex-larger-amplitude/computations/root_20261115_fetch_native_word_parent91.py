#!/usr/bin/env python3
"""Fetch the complete actual91 artifact for the independent word-first run.

Only the literal pin and local adapter provenance wrap the frozen512247
transport kernel. Network/auth/redirect, full ZIP size/SHA, every member's
path/type/CRC/size/SHA, receipt-last publication and cleanup remain original.
All CLI pins must be explicit. No scientific module or arithmetic is used.
"""
from __future__ import annotations
import hashlib,importlib.util,os
from pathlib import Path

REPOSITORY='Rogerhu12/math-research-public'
KERNEL_NAME='exact_20261114_fetch_pinned_public_artifact.py'
KERNEL_SHA='51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859'
PIN=dict(run_id=43672150224,artifact_id=14145200674,
 artifact_name='visible-mainline-modelresponse-43672150224-1',expected_size=10267458,
 expected_sha256='78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6')
SOURCE='b78f0dd1471a118d2ed21467602509d188c2ab67'
SCHEMA='pinned-complete-actual91-word-first-parent-fetch-v1'

def main():
 if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY:
  raise RuntimeError('This transport belongs only to the exact public repository Actions')
 here=Path(__file__).resolve().parent;p=here/KERNEL_NAME
 if hashlib.sha256(p.read_bytes()).hexdigest()!=KERNEL_SHA:raise ValueError('Frozen complete transport source changed')
 spec=importlib.util.spec_from_file_location('native_word_parent91_pinned_transport',p)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 if module.REPOSITORY!=REPOSITORY or module.SCHEMA!='pinned-public-actions-artifact-fetch-v3':
  raise ValueError('Frozen public transport contract changed')
 original_metadata=module.read_metadata;original_public=module.public_metadata
 adapter=dict(source_file=Path(__file__).name,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  kernel_source_file=KERNEL_NAME,kernel_source_sha256=KERNEL_SHA,pinned_source_commit=SOURCE,
  original_network_redirect_full_ZIP_and_all_member_validation_unchanged=True,
  complete_artifact_payload_retained=True,scientific_computation_performed=False)
 def metadata(opener,token):
  value,canonical=original_metadata(opener,token)
  if value['workflow_run']['head_sha']!=SOURCE:
   module.fail('SOURCE_COMMIT','The fixed actual91 source commit differs.')
  return value,canonical
 def public_metadata(value):
  output=original_public(value)
  output['local_pin_adapter_identity_not_GitHub_metadata']=adapter
  return output
 module.PIN=dict(PIN);module.SCHEMA=SCHEMA
 module.read_metadata=metadata;module.public_metadata=public_metadata
 return module.main()

if __name__=='__main__':raise SystemExit(main())
