"""Qualify the actual three-step full physical multiple-shooting result."""
import re

KIND="complete_R149_full_physical_multiple_shooting_and_four_maps_v1"
TARGETS=["complete_MSS_two_boundary_1424_cell_signed_defects","complete_MSS_physical_low193_inverse",
         "complete_MSS_four_source_HS_and_operator_maps"]
ROLES=("ordinary_raw_low_source","transformed_low_source","low_second_kind_correction","centre_high0_return_source")


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def ball(rec):
    require(rec["kind"]=="complete_decimal_ball_v1" and int(rec["radius_integer"])>=0
        and abs(int(rec["decimal_exponent"]))<300000,"complete outward scalar")
    m,r=int(rec["midpoint_integer"]),int(rec["radius_integer"])
    return m-r,m+r


def h(s):
    return isinstance(s,str) and re.fullmatch("[0-9a-f]{64}",s)


def validate(a,op,ref,triples):
    require(a["kind"]==op["scientific_kind"]==KIND and a["complete"] and a["proved"]
        and a["actual_returncode"]==0 and a["current_target"] is None and a["failure"] is None
        and a["completed_targets"]==op["ordered_targets"]==TARGETS
        and a["scientific_modules"]==op["scientific_module_binding"] and a["reference_identity"]==ref and ref
        and a["gates"]==[dict(name=k,passed=True) for k in op["complete_gate_names"]],"genuine complete physical MSS")
    c=a["certificate"]
    require(c["original_failed_GDC_scope"]==[{k:s[k] for k in ("path","bytes","sha256","git_blob_sha")} for s in triples]
        and c["whole_original81_matched"]["original_accepted_pivots_copied"]==81
        and c["whole_original81_matched"]["new_old_target_records"]==0,"actual antecedent and original TF carriers")
    last=c["whole_original_GDC_packets_matched"]
    require(last["original_GG89"]["restored_packets"]==89 and last["original_GG89"]["original_89_receipt_chain"]==
        "61e66e72eecdf989305547f10bdec90b0f97ec078cc7d7228cec470ce6bda9f4"
        and last["GDC_graph_or_source_targets_recomputed"]==0 and last["original_GDC_count"]>=89
        and h(last["original_GDC_index"]),"precise required prior whole packet recovery")
    r=c["full_local_rows"];m=c["true_model"];p=c["packet_carriers"];store=c["joint_matrices"]
    products=sum(1424//2**i for i in range(11))
    require(r["original_cells"]==1424 and r["original_nodes"]==1425 and r["all_local_angular_block_bounds"]==11392
        and r["original_boundary_block_bounds"]==4 and r["diagonal_signed_product_counts"]==[products]*2
        and r["complete_private_row_bytes"]>0 and h(r["complete_private_row_sha256"])
        and r["complete_dyadic_definition"]==store and store["whole_live_matrices"]==1425*2+1424*3+2
        and h(store["whole_live_matrix_index_sha256"]) and h(store["whole_write_journal_sha256"])
        and c["complete_row_prefix"]["count"]==1424 and h(c["complete_row_prefix"]["ordered_chain"])
        and m["complete_true_inverse"] and m["dimension"]==193*1425
        and m["exact_original_boundary_dimensions"]==[96,97] and m["independent_physical_mean_retained"]
        and m["true_ordinary_lengths"] and m["original_cells"]==1424
        and m["complete_left_and_right_weights"]["nodes"]==1425 and h(m["complete_left_and_right_weights"]["sha256"])
        and ball(m["strict_contraction_margin"])[0]>0 and c["actual_low_hybrid_inverse_proved"]
        and not c["actual_full_positive_inverse_proved"],"all original block evidence with one strict global inverse")
    require(p["whole_cell_indices"]==list(range(1424)) and p["whole_cell_count"]==1424
        and p["whole_frame_count"]==0 and h(p["whole_cell_carrier_index_sha256"])
        and p["four_roles_and_five_moments_present_in_every_whole_packet"] and not p["old_scientific_targets_reissued"]
        and a["actual_progress"]["actual_source_cells_complete"]==1424
        and a["actual_progress"]["old_completed_targets_recomputed"]==0,"complete actual physical input and source maps")
    sources=c["sources"]
    require(set(sources)==set(ROLES),"all four original sources")
    for j,role in enumerate(ROLES):
        v=sources[role]
        require(v["kind"]=="R149_actual_multiple_shooting_four_source_map_v1"
            and v["source_columns"]==(128 if j==3 else 193) and v["source_role"]==role
            and v["complete_true_cells"]==1424 and v["ordinary_dr"] and v["actual_low_BVP_proved"]
            and v["same_cell_triangles_charged_via_positive_whole_X_J"]
            and v["all193_original_mean_and_boundary_observations_retained"]
            and not v["full_CFB_or_positive_family_inverse_inferred"],"true same source and physical observations")
        for k in ("body_HS2_upper","root97_HS2_upper","outer96_HS2_upper","root97_operator_upper","outer96_operator_upper",
                  "body_norm_upper","atoms193_norm_upper","complete_norm_upper"):
            require(ball(v[k])[1]>0,"actual finite positive source upper")
        for k,l in (("body_norm_upper","actual_body_norm_upper"),("atoms193_norm_upper","actual_atoms193_norm_upper"),
                    ("complete_norm_upper","actual_complete_source_norm_upper")):
            require(v[k]==v[l],"original four source receiver aliases")
        if j==2:
            require(v["all193_independent_atom_inputs_keep_their_identity"]
                    and ball(v["actual_low_second_kind_inverse_upper"])[1]>0,"all full physical square inputs")
    return sources
