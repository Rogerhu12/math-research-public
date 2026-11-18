#!/usr/bin/env python3
"""One primary-matched-q, full-centre-twojet initializer in the R44 space.

The uniquely matched q is imported from the frozen defining-moment result.
Keep the first thirteen old physical controls, replace the last two with the
natural complete centre-twojet trace, then reproject the actual old full map
against the new reference and use the reviewed shared C2 inlet repair.
No old q-power restart predictor is called. The original actual full H is
re-encoded in the new numerical gauge; its actual binary64 product is recorded
without claiming equality unless observed. The original saved DN response is
an affine anchor only for this no-solver initial residual diagnostic.
"""
import hashlib
from pathlib import Path

SOURCE=Path(__file__).with_name('probe_circle_trace_replacement_initializer.py')
SOURCE_SHA='240019c426ee50983c1cd7b38d75147abeddb7a019774ba82b045bd73e356dce'
MAPPING_SHA='5cdba7238986b51cc6be26dba4782ef0dbe66eed167b3824fdf7ee3290910e35'
CONSTRUCTOR_SHA='fe2c656ea8163683eba7cead6f18b34e26904a6865cf6a7f07f426c6ddbecc0d'
INTERFACE_SHA='409d398f7e78f67fbce4ccc6e2402c66de70be72aaa201701c4f50e8e08f2df3'
text=SOURCE.read_text()
if hashlib.sha256(text.encode()).hexdigest()!=SOURCE_SHA:
    raise ValueError('The frozen full-twojet initializer source changed')


def replace_once(old,new):
    global text
    if text.count(old)!=1:raise ValueError('The primary-matched source boundary is not unique: '+old[:90])
    text=text.replace(old,new)


replace_once("    p.add_argument('--reference-run',type=Path,required=True)",
    "    p.add_argument('--reference-run',type=Path,required=True)\n"
    "    p.add_argument('--primary-mapping',type=Path,required=True)\n"
    "    p.add_argument('--constructor-check',type=Path,required=True)\n"
    "    p.add_argument('--interface-probe',type=Path,required=True)")
replace_once("    M=16;N=int(arg('angular'));q=float(arg('amplitude'));warp=float(arg('warp-reference'))\n"
             "    if q!=rec['actual_primary_amplitude'] or warp!=rec['warp_reference_q']:\n"
             "        raise ValueError('The declared actual q and old sine chart must be retained')",
'''    M=16;N=int(arg('angular'));warp=float(arg('warp-reference'))
    mapping_record=json.loads(args.primary_mapping.read_text())
    constructor_record=json.loads(args.constructor_check.read_text())
    if sha(args.primary_mapping)!=MAPPING_SHA or sha(args.constructor_check)!=CONSTRUCTOR_SHA:
        raise ValueError('The frozen unique primary mapping or actual constructor check changed')
    for entry in [mapping_record,constructor_record]:
        for path,digest in entry['source_sha256'].items():
            if sha(path)!=digest:raise ValueError('A primary/source identity changed: '+path)
    if (mapping_record['checkpoint']['sha256']!=sha(checkpoint) or
        mapping_record['new_settings']!=settings or
        constructor_record['mapping']['sha256']!=MAPPING_SHA or
        constructor_record['old_constructor']['actual_core_q']!=rec['actual_primary_amplitude'] or
        warp!=rec['warp_reference_q']):
        raise ValueError('The unique mapping does not bind this complete old anchor and endpoint')
    q=float(mapping_record['matched_q']['binary64'])
    if q.hex()!=mapping_record['matched_q']['binary64_hex']:
        raise ValueError('The uniquely rounded physical amplitude changed')
    if settings['center']!=math.pi/3:
        raise ValueError('The new trace space requires the literal reflection centre pi/3')''')
start=text.index('    install_record=args.out.with_name(')
end=text.index('    # Reconstruct the actual old full represented map',start)
replace_once(text[start:end],'''    H0=np.asarray(tail['request']['height'],float)
    # Do not call the original restart: for a new q it would apply ratio**j
    # to controls and scale the cut height. Both physical data are explicit.
''')
replace_once('mapping=dict(old_q_gauge=rec[\'gauge_amplitude\'],new_q_gauge=q,actual_q=rec[\'actual_primary_amplitude\'],',
    "mapping=dict(old_q_gauge=rec['gauge_amplitude'],new_q_gauge=q,old_actual_q=rec['actual_primary_amplitude'],actual_q=q,")
replace_once("rule='Keep the first 13 raw physical coefficients; t=old rho-new base rho, u=old h-new base h. No parameter scan.',",
    "rule='Set q to the unique primary-moment match. Keep the first 13 old physical coefficients; choose the complete centre-twojet t=old rho-new base rho, u=old h-new base h. No amplitude or trace-step scan.',")
start=text.index('    # A zero-trace identity checks the changed interface, not another initializer.\n')
end=text.index('    output=dict(',start)
replace_once(text[start:end],'''    previous=json.loads(args.interface_probe.read_text())
    if sha(args.interface_probe)!=INTERFACE_SHA or previous['new_core_settings']!=settings:
        raise ValueError('The unchanged trace-basis interface evidence changed')
    for path,digest in previous['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('The frozen trace interface source changed: '+path)
    interface=previous['interface_checks']
    reused_interface=dict(path=str(args.interface_probe.resolve()),sha256=sha(args.interface_probe),
        original_q=previous['initialization_mapping']['actual_q'],
        scope='The completed trace-basis primitive/retained-column checks are reused for the same basis. The old 17-point zero-trace core comparison was at its recorded old q; no new-q numerical equality is inferred from that finite check.')
''')
replace_once("'probe_circle_trace_replacement_initializer.py','circle_trace_replacement_basis.py',",
    "'probe_circle_trace_replacement_initializer.py','probe_circle_trace_primary_matched_initializer.py','circle_trace_replacement_basis.py',")
replace_once("        original_gauge_seed_record=dict(path=str(install_record),sha256=sha(install_record),source_transform=install_metadata),\n"
             "        initialization_mapping=mapping,interface_checks=interface,modes=M,angular=N,",
'''        unique_primary_mapping=dict(path=str(args.primary_mapping.resolve()),sha256=MAPPING_SHA),
        old_constructor_check=dict(path=str(args.constructor_check.resolve()),sha256=CONSTRUCTOR_SHA),
        original_restart_predictor_called=False,
        initialization_mapping=mapping,interface_checks=interface,reused_interface_checks=reused_interface,modes=M,angular=N,''')
replace_once("        prior_cut=y[obj.iz:,-1].copy();y[obj.iz:,-1]=gauge_y[obj.iz:,-1]",
'''        prior_cut=y[obj.iz:,-1].copy()
        # This is the physical old-H value expressed in the new gauge; any
        # last-bit product difference is measured below, not silently erased.
        y[obj.iz:,-1]=H0/(obj.bridge.sigma*obj.q)''')
replace_once("        if H.tobytes()!=H0.tobytes():raise ValueError('The new complete initial H differs from the actual affine anchor')",
'''        full_H_equal=H.tobytes()==H0.tobytes()
        height_delta=H-H0''')
replace_once('full_H_binary64_equal=True,full_H_binary64_sha256=binary_sha(H),',
'''full_H_binary64_equal=full_H_equal,full_H_binary64_sha256=binary_sha(H),
            original_H_binary64_sha256=binary_sha(H0),full_H=H.tolist(),original_H=H0.tolist(),
            full_H_minus_original_max=float(np.max(abs(height_delta))),
            changed_H_components=np.flatnonzero(H.view(np.uint64)!=H0.view(np.uint64)).tolist(),
            affine_anchor_scope='The saved original actual H0/response/Jac is used only as an affine residual anchor; a rounded candidate H is not claimed to have a newly accepted actual tail.', ''')
replace_once("    args.out.write_text(json.dumps(output,indent=2)+'\\n')",
    "    output['primary_match_initializer_source_transform']=PRIMARY_MATCH_PROVENANCE\n"
    "    args.out.write_text(json.dumps(output,indent=2)+'\\n')")
doc_start=text.index('"""');doc_end=text.index('"""',doc_start+3)+3
text=text[:doc_start]+repr(__doc__)+text[doc_end:]
PROVENANCE=dict(parent_source=str(SOURCE.resolve()),parent_source_sha256=SOURCE_SHA,
    mapping_sha256=MAPPING_SHA,constructor_check_sha256=CONSTRUCTOR_SHA,
    transformed_program_sha256=hashlib.sha256(text.encode()).hexdigest(),
    changes='Unique defining-primary-matched q; original physical first13 controls and complete twojet trace mapping; no q-power restart; old full H explicitly re-encoded in new gauge and compared; basis checks reused with their original scope.',
    no_BVP_or_actual_tail_solve=True)
namespace=dict(__name__='__main__',__file__=str(Path(__file__).resolve()),
    MAPPING_SHA=MAPPING_SHA,CONSTRUCTOR_SHA=CONSTRUCTOR_SHA,INTERFACE_SHA=INTERFACE_SHA,
    PRIMARY_MATCH_PROVENANCE=PROVENANCE)
exec(compile(text,str(Path(__file__).resolve())+'::primary_matched_initializer','exec'),namespace)
