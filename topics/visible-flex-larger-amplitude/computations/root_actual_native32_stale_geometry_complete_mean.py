#!/usr/bin/env python3
"""Complete actual-current geometry using an explicitly old native-M32 increment.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The unchanged accepted-current transport and current-grid construction now
bind the genuine full nine-control M32-to-M32 constructor. All 97 state
channels and 32 core directions remain present. Geometry keeps all old grid
points, all actually accepted current raw nodes and the current fixed-view
quintic witness, with the complete 1552-point mean and 768 angular samples.
No derivative at a future current point, future acceptance, new solution or
new full field is implied by preparation. Control arguments are increments
from the actually accepted current point, not totals from the old origin.
"""
import ast
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PARENT=HERE/'root_actual_stale_increment_geometry_complete_mean.py'
PARENT_SHA='8d333f7fdbe8b422db87193c825be3a7a9f5c863b44cab333874061535f011df'
NATIVE_SHA='6fe16047d4a3c4e069166157ba414232c36b36d22140b4e18cd8d972f03aa6c2'

def main():
    original=PARENT.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=PARENT_SHA:
        raise ValueError('Frozen original accepted-current fullmean geometry changed')
    doc=ast.get_docstring(ast.parse(original),clean=False)
    edits=[
      ('"""'+doc+'"""',json.dumps(__doc__)),
      ("STALE_SHA = 'e21809f94b1b702481ff30181fc936c5ea9e43d9436b4fe69586efadef10bbd0'",
       "STALE_SHA = '"+NATIVE_SHA+"'"),
      ("    source = before.replace(anchor, replacement, 1)\n"
       "    if source.replace(replacement, anchor, 1) != before:\n",
       "    source = before.replace(anchor, replacement, 1)\n"
       "    scope_before = 'Complete accepted M32 field plus an explicitly embedded M28 response increment, with the original complete M32 mean; unsolved warm geometry only.'\n"
       "    scope_after = 'Complete actually accepted current M32 field plus a declared old M32 full-nine-control increment; original complete mean, unsolved warm geometry only.'\n"
       "    if source.count(scope_before) != 1:\n"
       "        raise ValueError('Frozen warm scope label changed')\n"
       "    source = source.replace(scope_before, scope_after, 1)\n"
       "    if source.replace(scope_after, scope_before, 1).replace(replacement, anchor, 1) != before:\n"),
      ("        only_parser_arguments_and_declared_constructor_grid_callbacks_changed=True,\n",
       "        only_parser_arguments_declared_constructor_grid_callbacks_and_scope_label_changed=True,\n"
       "        full_97_state_rows_and_32_modes_required_by_native_constructor=True,\n"
       "        complete_old_nine_control_response_required=True,\n"
       "        native32_geometry_parent_sha256=NATIVE_GEOMETRY_PARENT_SHA,\n"),
      ("    record['source_and_input_sha256'][str(original_path)] = ORIGINAL_FINE_SHA\n",
       "    record['source_and_input_sha256'][str(original_path)] = ORIGINAL_FINE_SHA\n"
       "    record['source_and_input_sha256'][str(NATIVE_GEOMETRY_PARENT_PATH)] = NATIVE_GEOMETRY_PARENT_SHA\n"),
    ]
    source=original
    for before,after in edits:
        if source.count(before)!=1:raise ValueError('A frozen native geometry adaptation site changed')
        source=source.replace(before,after,1)
    reverse=source
    for before,after in reversed(edits):
        if reverse.count(after)!=1:raise ValueError('Native fullmean adaptation cannot be reversed')
        reverse=reverse.replace(after,before,1)
    if reverse!=original:raise ValueError('Unlisted native fullmean geometry change')
    ast.parse(source)
    namespace=dict(__file__=str(Path(__file__).resolve()),__name__='actual_native32_stale_fullmean_geometry',
        NATIVE_GEOMETRY_PARENT_SHA=PARENT_SHA,NATIVE_GEOMETRY_PARENT_PATH=PARENT)
    exec(compile(source,'<actual-native32-stale-fullmean-geometry>','exec'),namespace)
    namespace['main']()

if __name__=='__main__':main()
