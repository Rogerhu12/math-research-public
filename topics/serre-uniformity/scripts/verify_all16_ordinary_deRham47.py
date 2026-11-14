#!/usr/bin/env python3
"""Independent aggregate/input and endpoint-to-principal identity audit for all16 ordinary centers."""
import argparse,gzip,json,hashlib
from pathlib import Path
Q=47**4

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['aggregate','abel-dir','second-kind-dir','old-pure-j01','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();agg=read(args.aggregate);assert agg['complete_all16_ordinary_deRham_integrals'] and agg['completed_disk_count']==16 and agg['remaining_disk_ids']==[]
 wanted=['ORD_j'+str(j).zfill(2) for j in [1,5,7,11,12,15,19,24,27,28,30,32,41,43,45,46]];assert sorted(r['disk_id'] for r in agg['records'])==wanted
 inputs={str(args.aggregate):sha(args.aggregate),str(args.old_pure_j01):sha(args.old_pure_j01)};checks=[]
 for row in agg['records']:
  disk=row['disk_id'];apath=args.abel_dir/(disk+'_Abel47.json.gz');spath=args.second_kind_dir/(disk+'_second_kind_complete47.json.gz');ab=read(apath);se=read(spath);inputs[str(apath)]=sha(apath);inputs[str(spath)]=sha(spath)
  assert row['Abel_sha256']==sha(apath) and row['second_kind_certificate_sha256']==sha(spath)
  assert row['canonical_holomorphic_integrals_of_C_mod47four']==ab['canonical_log_C_mod47four'];assert row['cyclic_coordinates_of_C_mod47cubed']==ab['actual_center_C_cyclic_coordinates_mod47cubed'];assert row['second_kind_integrals_of_C_mod47four']==se['actual54_second_kind_integrals_of_C_mod47four'];assert row['complete_all108_actual_integrals']
  assert se['input_sha256'][apath.name]==sha(apath) and se['endpoint']['Abel_sha256']==sha(apath)
  e,p=se['endpoint'],se['principal_chain'];assert e['base_section_factor_v1_over_f0_retained'] and e['complete_actual_terminal_family1_transport'] and e['full820_by73_principal_ideal_transport_verified'];assert p['all455_principal_functions_unit_on_family2'] and p['complete_all454_actual_chain_norm_derivatives'];assert len(p['function_log_norm_derivatives'])==455
  tiny=e['actual_second_kind_tiny_integrals_at_family1_mod47four'][0];logshort=e['terminal_transport_log_norm_derivative_at_family2_mod47four'][0];dfinal=p['log_norm_derivative_f_final'][0];terminal=e['actual_second_kind_integrals_over_Dfinal_mod47four'][0];answer=se['actual54_second_kind_integrals_of_C_mod47four'][0]
  scale=ab['actual_multiple_sign']*ab['target_multiplier'];assert scale%47
  assert all(len(x)==54 for x in [tiny,logshort,dfinal,terminal,answer])
  for j in range(54):
   for k in range(2):
    assert (tiny[j][k]+logshort[j][k]-terminal[j][k])%Q==0
    assert (terminal[j][k]-dfinal[j][k]-scale*answer[j][k])%Q==0
  assert e['canonical_log_target_mod47four']==ab['canonical_log_signed_mC_mod47four']
  checks.append({'disk_id':disk,'all108_saved_integrals_and_all54_terminal_principal_identities_verified':True,'actual_chain_operations':454,'saved_function_norm_derivatives':455,'signed_scale_mod47four':scale%Q})
 old=read(args.old_pure_j01);new=read(args.abel_dir/'ORD_j01_Abel47.json.gz');keys=['canonical_log_C_mod47four','actual_center_C_cyclic_coordinates_mod47cubed','actual_multiple_point_sha256'];assert all(old[k]==new[k] for k in keys)
 out={'result':'R244','input_sha256':inputs,'completed_disk_ids':wanted,'completed_disk_count':16,'actual_saved_integral_scalar_count':16*108,'original454_operations_per_disk_total':16*454,'original457_principal_functions_per_disk_total':16*457,'checks':checks,'j01_original_pure_Abel_and_retained_function_replay_match_keys':keys,'j01_terminal_point_matches_exactly':True,'source_sha256':sha(__file__),'scope':'Independent exact aggregate, input SHA and all864 second-kind endpoint/principal identities; does not reexecute the long group chains or RR.'}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS all16 actual108 constants and j01 original/replay match',sha(args.output))
if __name__=='__main__':main()
