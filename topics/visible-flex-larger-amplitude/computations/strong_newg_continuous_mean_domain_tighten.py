#!/usr/bin/env python3
"""Tighten only actual q106 domain boxes with D below 1/1024.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The complete already proved 3152-box domain is the input. Positive boxes
above the declared quality target are retained verbatim. Only the actual
small-denominator boxes exposed by the complete mean consumer are split.
The quality target is not a mathematical assumption: if it is not reached,
an actually positive final box remains valid and is explicitly reported.
All physical states are restricted from their original binary quintics;
no ODE, numerical solution or original metric is changed.
"""
import ast
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE/'strong_newg_continuous_mean_domain_refine_v2.py'
PARENT_SHA = 'ea1720a356695d7f868b2a2ae38898c460e929a0307bad640f65aeba114fabdf'
PRIOR_SHA = 'a7342234eb1ce94569f7de40f1fa084701da35b87dbf4bdcec82be1e84cde39d'


def unique(source, before, after):
    if source.count(before) != 1:
        raise ValueError('Frozen tightening edit site is not unique: '+before[:100])
    result = source.replace(before, after, 1)
    if result.count(after) != 1 or result.replace(after, before, 1) != source:
        raise ValueError('Exact tightening reversal failed')
    return result


def additional_edits(edit):
    edit(" if len(prior_rows)!=len(prior['rows']):raise ValueError('Duplicate original domain atoms')\n",
         " if len(prior_rows)!=len(prior['rows']):raise ValueError('Duplicate original domain atoms')\n"
         " if not prior['all_domain_gates'] or prior['failed_atoms'] or len(prior_rows)!=3152:raise ValueError('Complete actual positive prior required')\n"
         " prior_right_by_start={(r['original_interval'],r['s_interval'][0]):F(r['s_interval'][1]) for r in prior['rows']}\n"
         " if len(prior_right_by_start)!=len(prior_rows):raise ValueError('Prior start coverage is not unique')\n")
    edit("    piece=pieces[piece_index];right=min(s1,piece['right'])\n",
         "    piece=pieces[piece_index];right=min(s1,piece['right'],prior_right_by_start[(intervals,str(left))])\n")
    edit("    if old['positive_domain']:\n",
         "    if old['positive_domain'] and binary(old['normalized_D_lower'])>=F(1,1024):\n")
    before = """ def refine_atom(index,pindex,left,right,depth):
  nonlocal atoms,refined_leaves
  yy=refined_state_box(index,left,right);radius,ap=background_box(pieces[pindex],left,right);N=max(1024,a.angular_start)
  passed,bounds=domain(yy,radius,ap,left,right,N)
  if not passed and depth<a.max_radial_depth:
   middle=(left+right)/2;refine_atom(index,pindex,left,middle,depth+1);refine_atom(index,pindex,middle,right,depth+1);return
  while not passed and N<a.angular_max:
   N*=2;passed,bounds=domain(yy,radius,ap,left,right,N)
  item=dict(original_interval=index,background_piece=pindex,s_interval=[str(left),str(right)],angular_intervals=N,radial_subdivision_depth=depth,original_binary_quintic_exact_Bernstein_restricted=True,whole_radial_angular_and_repair_homotopy_enclosed=True,positive_domain=passed,**bounds)
  rows.append(item);atoms+=1;refined_leaves+=1
  if not passed:failures.append(item)
"""
    after = """ def refine_atom(index,pindex,left,right,depth):
  nonlocal atoms,refined_leaves
  yy=refined_state_box(index,left,right);radius,ap=background_box(pieces[pindex],left,right);N=max(1024,a.angular_start)
  passed,bounds=domain(yy,radius,ap,left,right,N)
  adequate=passed and binary(bounds['normalized_D_lower'])>=F(1,1024)
  if not adequate and depth<a.max_radial_depth:
   middle=(left+right)/2;refine_atom(index,pindex,left,middle,depth+1);refine_atom(index,pindex,middle,right,depth+1);return
  while not adequate and N<a.angular_max:
   N*=2;passed,bounds=domain(yy,radius,ap,left,right,N);adequate=passed and binary(bounds['normalized_D_lower'])>=F(1,1024)
  item=dict(original_interval=index,background_piece=pindex,s_interval=[str(left),str(right)],angular_intervals=N,radial_subdivision_depth=depth,original_binary_quintic_exact_Bernstein_restricted=True,whole_radial_angular_and_repair_homotopy_enclosed=True,positive_domain=passed,declared_D_floor_quality_target_met=adequate,**bounds)
  rows.append(item);atoms+=1;refined_leaves+=1
  if not passed:failures.append(item)
"""
    edit(before, after)
    edit("unpaid_original_atoms_refined=refined_original_atoms,refined_leaves=refined_leaves",
         "prior_atoms_below_quality_target_refined=refined_original_atoms,refined_leaves=refined_leaves")
    edit("  normalized_definitions={'u':'X_psi/a'",
         "  denominator_tightening=dict(prior_complete_domain_sha256=sha(a.prior),target_D_lower=['1',-10],target_is_not_a_mathematical_assumption=True,quality_target_failures=sum(binary(r['normalized_D_lower'])<F(1,1024) for r in rows),retained_prior_boxes_above_target_only=True),\n"
         "  normalized_definitions={'u':'X_psi/a'")


def main():
    original = PARENT.read_text()
    if hashlib.sha256(original.encode()).hexdigest() != PARENT_SHA:
        raise ValueError('Frozen exact-refinement parent changed')
    replacements = [
        ("PRIOR_SHA='e8eb6d474b9f8d4a9d03100b038e3c4d8757341e3941cc12a12d9afaa322ce76'", "PRIOR_SHA='"+PRIOR_SHA+"'"),
        ("prior['source_sha256']!=REFINE_ORIGINAL_SHA", "prior['source_sha256']!='"+PARENT_SHA+"'"),
        ('    ast.parse(source)\n', '    APPLY_DENOMINATOR_TIGHTENING(edit)\n    ast.parse(source)\n'),
    ]
    changed = original
    for before, after in replacements:
        changed = unique(changed, before, after)
    ast.parse(changed)
    reverse = changed
    for before, after in reversed(replacements):
        reverse = unique(reverse, after, before)
    if reverse != original:
        raise ValueError('Unlisted refinement source change')
    namespace = dict(__file__=str(Path(__file__).resolve()), __name__='q106_actual_domain_denominator_tightening',
                     APPLY_DENOMINATOR_TIGHTENING=additional_edits)
    exec(compile(changed, '<frozen-refinement-with-actual-denominator-target>', 'exec'), namespace)
    namespace['main']()


if __name__ == '__main__':
    main()
