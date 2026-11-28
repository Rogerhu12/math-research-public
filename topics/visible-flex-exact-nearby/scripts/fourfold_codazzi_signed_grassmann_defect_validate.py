"""Read an actual GDC result, with separate natural prefix and complete-model qualifications."""
from hashlib import sha256
import json
import re

KIND="complete_R149_signed_chronological_grassmann_and_four_maps_v1"
TARGETS=["signed_GDC_positive_physical_cell_82","complete_GDC_true_low193_inverse","complete_GDC_four_physical_source_maps"]


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def positive_lower(ball):
    require(ball["kind"]=="complete_decimal_ball_v1" and int(ball["radius_integer"])>=0
            and int(ball["midpoint_integer"])-int(ball["radius_integer"])>0,"strict directed decimal lower")


def validate(a,op,reference,gg,failed):
    require(a["kind"]==KIND==op["scientific_kind"] and a["complete"] and a["proved"]
            and a["failure"] is None and a["actual_returncode"]==0 and a["reference_identity"]==reference and reference
            and a["scientific_modules"]==op["scientific_module_binding"] and a["completed_targets"]==TARGETS==op["ordered_targets"]
            and a["gates"]==[dict(name=n,passed=True) for n in op["complete_gate_names"]],"complete new GDC actual and qualifications")
    c=a["certificate"]
    require(all(c["restored_original81"].get(k)==v for k,v in gg.OLD.items())
            and c["restored_original81"]["original_accepted_pivots_copied"]==81
            and c["restored_original81"]["new_old_target_records"]==0,"admitted original TF81")
    past=c["original_failed_GG"]
    rec=past["old_packets"]
    require(rec["actual"]==failed.ACTUAL[1] and rec["execution"]==failed.EXECUTION[1]
            and rec["manifest"]==failed.MANIFEST[1] and rec["restored_packets"]==89
            and rec["whole_original_packet_bytes"]==185822772 and rec["original_89_receipt_chain"]==failed.PACKET_CHAIN
            and rec["original_81_graph_scalar_record_chain"]==failed.OLD_SCALAR_CHAIN
            and sorted(rec["original_8_arrival_order"])==list(range(81,89))
            and rec["original_8_arrival_order"][-1]==88 and rec["old_failed_graph_gate_calls"]==0
            and past["old_graphs"]==dict(whole_packets=failed.PACKETS_INDEX,whole_frames=failed.FRAMES_INDEX,
                whole_matrices=failed.MATRICES_INDEX,whole_write_journal=failed.MATRIX_JOURNAL,
                whole_graph_scalar_journal=failed.OLD_SCALAR_CHAIN,old_failed_denominator_calls=0,old_scientific_targets_reissued=0),
            "all separate complete original failed GG carrier, journal and packet identities")
    first=c["first_new_cell82"]
    positive_lower(first["complete_new_denominator_lower"])
    require(first["used_original_denominator_witness"] is False and not first["old_Grassmann_scalar_gate_recomputed"],
            "independent positive witness over complete physical cell 81")
    model=c["true_model"]
    require(model["true_hybrid_BVP_verified"] and model["new_chronological_method"] and model["complete_refined_cells"]==1424
            and model["ordinary_dr_and_true_root_lengths_retained"] and model["exact_rational_householder_frames"]
            and model["all193_original_mean_and_boundary_coordinates_retained"] and not model["physical_S_replaced_by_internal_balance"],
            "complete original low193 physical inverse")
    cuts=model["accepted_subbox_counts"]
    require(len(cuts)==1424 and cuts[:81]==[4]*81 and all(type(i)is int and 4<=i<=64 for i in cuts),"complete signed Peano partitions")
    ledger=gg.unpack_powers(c["joint_inclusions"])
    require(all(len(ledger[s])==1424 and all(len(row)==2 and all(type(i)is int for i in row) for row in ledger[s]) for s in ("left","right"))
            and len(ledger["nodes"])==1425 and all(type(x)is int for x in ledger["nodes"])
            and re.fullmatch(r"[0-9a-f]{64}",ledger["whole_ordered_record_chain_sha256"]),"ordered full witnesses")
    for side in ("left","right"):
        cp=c["history_checkpoints"][side]["complete_history"]
        require(cp["completed_chronological_cells"]==sum(cp["complete_blocks"])==1424 and cp["bytes"]>0
                and re.fullmatch(r"[0-9a-f]{64}",cp["sha256"]),"last whole private chronological history")
    packets=c["packet_carriers"]
    require(packets["whole_cell_indices"]==list(range(1424)) and packets["whole_cell_count"]==packets["whole_frame_count"]==1424
            and 1<=packets["maximum_submitted_unreceived_cells"]<=8 and packets["old_scientific_targets_reissued"]==0
            and packets["four_roles_and_five_moments_present_in_every_whole_packet"] and c["joint_matrices"]["each_whole_matrix_readback_hash_checked"],
            "complete final cell, frame and joint-matrix carrier index")
    require(c["actual_low_hybrid_inverse_proved"] and not c["actual_full_positive_inverse_proved"]
            and set(c["sources"])==set(gg.ROLES) and a["actual_progress"]["actual_source_cells_complete"]==1424,
            "same actual inverse and all four source maps")
    for idx,role in enumerate(gg.ROLES):
        rec=c["sources"][role]
        require(rec["kind"]=="R149_actual_low193_joint_complete_source_map_v1" and rec["source_role"]==role
                and rec["source_columns"]==(128 if idx==3 else 193) and rec["complete_true_cells"]==1424 and rec["ordinary_dr"]
                and rec["all193_original_mean_and_boundary_observations_retained"] and rec["same_cell_triangles_bounded_by_two_complete_positive_squares"]
                and rec["actual_low_BVP_proved"] and not rec["full_CFB_or_positive_family_inverse_inferred"],"original whole source map")
        for k in ("body_HS2_upper","root97_HS2_upper","outer96_HS2_upper","body_norm_upper","atoms193_norm_upper","complete_norm_upper"):
            gg.positive_upper(rec[k])
        if idx==2:
            gg.positive_upper(rec["actual_low_second_kind_inverse_upper"])
            require(rec["all193_independent_atom_inputs_keep_their_identity"],"square physical second-kind identity")
    return c["sources"]
