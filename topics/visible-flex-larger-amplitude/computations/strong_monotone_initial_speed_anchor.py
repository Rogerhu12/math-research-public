#!/usr/bin/env python3
"""Fresh first-append anchor fix for the frozen monotone speed provider.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original first Hermite append receives kind/length/k0/v1 only. Its a0 is
inserted later by Pieces.append from self.aend. This adapter changes exactly
that early physical_piece argument to the same current self.aend. All
physical formulas, domains, controls, zero-weight delegation and installation
order remain the frozen implementation. No frozen source is edited.
Install this module instead of the original frontload module, after the
original angle and pulse hooks; an already installed unfixed hook is refused.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent
ORIGINAL_SHA='12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7'
ORIGINAL_PATH=HERE/'strong_monotone_initial_speed.py'
source=ORIGINAL_PATH.read_text()
if hashlib.sha256(source.encode()).hexdigest()!=ORIGINAL_SHA:
    raise ValueError('Frozen original monotone provider changed')
before='data = physical_piece(segment["a0"], float(self.cfg["delta"]),'
after='data = physical_piece(self.aend, float(self.cfg["delta"]),'
if source.count(before)!=1:
    raise ValueError('Original early-anchor call is not unique')
changed=source.replace(before,after,1)
if changed.count(after)!=1 or changed.replace(after,before,1)!=source:
    raise ValueError('Anchor replacement changed another frozen source site')
ast.parse(changed)
_namespace=dict(__file__=str(ORIGINAL_PATH),__name__='frozen_monotone_provider_correct_append_anchor')
exec(compile(changed,'<frozen-monotone-correct-first-append-anchor>','exec'),_namespace)
elevated_cubic_controls=_namespace['elevated_cubic_controls']
bernstein=_namespace['bernstein']
physical_piece=_namespace['physical_piece']


def source_identity():
    return dict(original_source_sha256=ORIGINAL_SHA,
        adapter_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_original_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        exact_reverse_recovers_original_source=True,
        only_changed_expression='first nonzero Hermite physical_piece a0 argument: segment[a0] -> self.aend')


def install(provider):
    if getattr(provider,'_strong_initial_speed_frontload_anchor_installed',False):return
    if getattr(provider,'_strong_initial_speed_frontload_installed',False):
        raise ValueError('Install the fresh anchor provider instead of the unfixed frontload hook')
    _namespace['install'](provider)
    provider._strong_initial_speed_frontload_anchor_installed=True


def install_globals(namespace):
    proxy=SimpleNamespace(**namespace);install(proxy)
    for name in ('velocity','piece_jet','NeckPrefix','_strong_initial_speed_frontload_installed',
                 '_strong_initial_speed_frontload_anchor_installed'):
        namespace[name]=getattr(proxy,name)
