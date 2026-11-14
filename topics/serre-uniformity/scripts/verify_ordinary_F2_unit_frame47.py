#!/usr/bin/env python3
"""Independent exact scalar, mixed-frame residue, tangent and QC audit for ORD_j28."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith(".gz") else raw)


def flat(x):
    if isinstance(x, list):
        return [z for y in x for z in flat(y)]
    return [x]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--disk-id", required=True)
    ap.add_argument("--qc-dir", type=Path, required=True)
    ap.add_argument("--root-dir", type=Path, required=True)
    ap.add_argument("--script-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    qc, root, d = args.qc_dir.resolve(), args.root_dir.resolve(), args.disk_id
    scripts=args.script_dir.resolve()
    def locate(primary, fallback):
        return primary if primary.exists() else fallback
    names = {
        "generic_center_source": qc/"p41_ordinary_F2_unit_frame_connection47.py",
        "generic_disk_source": qc/"p41_ordinary_F2_unit_frame_polynomial47.py",
        "frozen_R259_source": root/"p41_ordinary_F2_connection47.py",
        "frozen_R262_source": root/"p41_ordinary_F2_local_polynomial47.py",
        "center": qc/(d+"_actual_canonical_F2_height47.json.gz"),
        "polynomial": qc/(d+"_actual_canonical_F2_polynomial47.json.gz"),
        "full_norm": qc/(d+"_actual_F2_first_variable_norm47.json.gz"),
        "Abel": qc/"ordinary-abel-with-transports"/(d+"_Abel47.json.gz"),
        "multiply": qc/"ordinary-abel-with-transports"/(d+"_multiply47.json.gz"),
        "second": qc/"ordinary-second-kind"/(d+"_second_kind_complete47.json.gz"),
        "principal": qc/"ordinary-F2-norms"/(d+"_actual_principal_function47.json.gz"),
        "T2_support": qc/"ordinary-F2-norms"/(d+"_actual_T2_support47.json.gz"),
        "T2_norm": qc/"ordinary-F2-norms"/(d+"_actual_T2_principal_norm47.json.gz"),
        "based": qc/"p41_all19_based_points47.json.gz",
    }
    for key,path in names.items():
        fallback=scripts/path.name if path.suffix==".py" else scripts/"data"/path.name
        names[key]=locate(path,fallback)
    data = {k: read(p) for k, p in names.items() if k not in [
        "generic_center_source", "generic_disk_source", "frozen_R259_source", "frozen_R262_source"]}
    center, poly, fullnorm = [data[k] for k in ["center", "polynomial", "full_norm"]]
    assert center["source_sha256"] == sha(names["generic_center_source"])
    assert poly["source_sha256"] == sha(names["generic_disk_source"])
    assert all(data[k]["disk_id"] == d for k in ["center", "polynomial", "full_norm", "Abel",
        "multiply", "second", "principal", "T2_norm"])
    assert data["T2_support"]["source_disk_id"] == d
    checks = []
    def edge(source, target):
        h = data[source]["input_sha256"]
        matches = [v for k, v in h.items() if Path(k).name == names[target].name]
        assert matches and set(matches) == {sha(names[target])}, (source, target)
        checks.append([source, target])
    for s, t in [("center", "second"), ("center", "principal"), ("center", "T2_support"),
        ("center", "full_norm"), ("polynomial", "center"), ("polynomial", "Abel"),
        ("polynomial", "multiply"), ("Abel", "multiply"), ("second", "Abel"),
        ("second", "multiply"), ("second", "based"), ("principal", "second"),
        ("T2_norm", "principal"), ("T2_norm", "T2_support"), ("full_norm", "T2_norm"),
        ("full_norm", "principal"), ("full_norm", "second"), ("full_norm", "multiply"),
        ("full_norm", "based")]:
        edge(s, t)
    assert data["multiply"]["input_sha256"] == sha(names["based"])
    assert data["multiply"]["bits_done"] == data["multiply"]["target_bits"] == 304
    assert data["multiply"]["point_sha256"] == data["Abel"]["actual_multiple_point_sha256"]
    Q, q = 47**4, 47**3
    # Every tangent value below was independently retained by the fixed-norm executor.
    rows = {x["label"]: x for x in fullnorm["fixed_and_collision_part"]["rows"]}
    ab, apoint = [rows[k]["j_tangent"]["g1_differential_over_dj"] for k in ["P_minus3", d]]
    assert ab[1] == apoint[1] == 0 and ab[0] % 47 and apoint[0] % 47
    assert [ab[0], apoint[0]] == center["actual_g1_over_dj_at_base_and_center"]
    sigma = pow(ab[0] * pow(apoint[0], -1, Q) % Q, 4, Q)
    z = (pow(sigma, 46, Q) - 1) % Q
    assert z % 47 == 0
    log_sigma = (z-z*z*pow(2,-1,Q)+z*z*z*pow(3,-1,Q))*pow(46,-1,Q) % Q
    assert sigma == center["canonical_sigma_fibre_coordinate_mod47four"]
    assert log_sigma == center["canonical_sigma_coordinate_log_mod47four"]
    m = fullnorm["actual_integer_scale"]
    assert m == center["actual_integer_scale"] == data["Abel"]["target_multiplier"]
    assert m % 47 == 9
    normlog = fullnorm["actual_log_norm_Phi_on_F2_second_divisor_mod47four"]
    assert normlog == center["first_variable_principal_log_norm_mod47four"]
    t = center["all_actual_tiny_integrals_mod47four"]
    weights = {"T2C":27,"C":4,"u_minus_b":162,"Z8_minus20b":-27,
               "c7_minus_b":-54,"K_g1_minus106b":4}
    tiny = sum(weights[k]*t[k] for k in weights) % Q
    assert tiny == center["second_divisor_tiny_integral_mod47four"]
    actual_height = (log_sigma + pow(m,-1,Q)*(normlog+tiny)) % Q
    assert actual_height == center["actual_local_sigma_F2_height_mod47four"]
    actual_nu = flat(data["second"]["actual54_second_kind_integrals_of_C_mod47four"])
    center_nu = flat(center["actual_gradients_original_nu_mod47cubed"]["C"])
    assert [x%q for x in actual_nu] == center_nu
    ph = data["principal"]["combined_function_to_actual_A1_t"]["actual_A1_physical_parameters"]
    assert flat(ph) == flat(center["physical_family1_parameters"])
    height_poly = poly["canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four"]
    assert height_poly[0] == actual_height
    global_poly = poly["global_F2_coefficients_0to4_in_y_mod47four"]
    qc_poly = [(global_poly[k]-800*(height_poly[k] if k<4 else 0))%Q for k in range(5)]
    assert qc_poly == poly["actual_QC_F2_coefficients_0to4_in_y_mod47four"]
    assert all(x%47==0 for x in qc_poly)
    red = [(x//47)%47 for x in qc_poly]
    assert red == poly["QC_divided_by47_reduction_coefficients_mod47"]
    values = [sum(c*pow(y,k,47) for k,c in enumerate(red))%47 for y in range(47)]
    roots = [y for y,v in enumerate(values) if v==0]
    assert values == poly["all47_residual_QC_values"] and roots == poly["residual_QC_roots"]
    assert poly["entire_disk_excluded_for_all_four_bad_components"] == (roots==[])
    discriminant = (red[1]**2-4*red[0]*red[2])%47
    assert discriminant == poly["residual_quadratic_discriminant"]
    divided = [x//47 for x in qc_poly]
    lifted = []
    for y0 in roots:
        y = y0
        derivative = sum(k*c*pow(y0,k-1,47) for k,c in enumerate(divided) if k)%47
        assert derivative
        digits = [y0]
        modulus = 47
        for _ in range(2):
            next_modulus = 47*modulus
            value = sum(c*pow(y,k,next_modulus) for k,c in enumerate(divided))%next_modulus
            assert value%modulus == 0
            digit = -(value//modulus)*pow(derivative,-1,47)%47
            digits.append(digit)
            y += digit*modulus
            modulus = next_modulus
        assert sum(c*pow(y,k,q) for k,c in enumerate(divided))%q == 0
        lifted.append({"y_mod47cubed":y,"z_mod47four":47*y,
                       "y_base47_digits":digits,"derivative_mod47":derivative})
    # Independently check the new frame-sensitive residue and scale at P.
    assert d == "ORD_j28"
    source_dir = args.script_dir / "data"
    atlas_path = source_dir / "p41_ordinary_rational_atlas47.json.gz"
    cusp_path = source_dir / "p41_cusp_divisors47_certificate.json.gz"
    atlas, cusp = read(atlas_path), read(cusp_path)
    chart = next(x for x in atlas["charts"] if d in x["disk_ids"])
    row = chart["disk_ids"].index(d)
    W0 = chart["W_coefficients_0to3"][0][row]
    W1 = chart["W_coefficients_0to3"][1][row]
    C = center["actual_connections"]["C"]
    assert C["finite_pole_coordinates_unit_normalized"][0] == W0
    assert C["finite_pole_unit_frames"][0] == chart["frame"] == center["ordinary_center_frame"]
    assert poly["actual_projective_frame"] == chart["frame"]
    assert poly["actual_projective_coordinate"] == chart["coordinate"]
    def cm(x,y,modulus=Q):
        return ((x[0]*y[0]-x[1]*y[1])%modulus,(x[0]*y[1]+x[1]*y[0])%modulus)
    def dot(x,y,modulus=Q):
        terms=[cm(u,v,modulus) for u,v in zip(x,y)]
        return (sum(v[0] for v in terms)%modulus,sum(v[1] for v in terms)%modulus)
    def inv(x):
        n=pow((x[0]*x[0]+x[1]*x[1])%Q,-1,Q)
        return (x[0]*n%Q,-x[1]*n%Q)
    H0=C["finite_pole_Hv_values"][0]
    coord=[x[0] for x in chart["coordinate"]]
    frame=[x[0] for x in chart["frame"]]
    hc=dot(H0,coord)
    assert dot(W0,frame)==(1,0) and dot(H0,frame)==(0,0)
    assert all(list(cm(x,hc))==y for x,y in zip(W1,H0))
    assert (hc[0]*hc[0]+hc[1]*hc[1])%47
    # Evaluate the actual quadratic numerator from the published monomial basis.
    monomials=cusp["square_basis_monomials_1based"]
    inverse=cusp["square_basis_inverse"]
    qcoef=[x[0] for x in C["denominator_linear_coefficients_mod47four"]]
    scoef=[x[0] for x in C["numerator_quadratic_coefficients_mod47cubed"]]
    for i,W in enumerate(C["finite_pole_coordinates_unit_normalized"]):
        products=[cm(W[u-1],W[v-1]) for u,v in monomials]
        V2=[dot(products,[inverse[k][j] for k in range(199)]) for j in range(199)]
        assert dot(W,qcoef)==(0,0)
        value=dot(V2,scoef,q)
        derivative=dot(C["finite_pole_Hv_values"][i],qcoef,q)
        residue=C["finite_residues"][i]
        assert value==tuple(residue*x%q for x in derivative)
    gcoef=[x[0] for x in fullnorm["g1_actual73_coefficients"]]
    jp=poly["actual_j_coefficients_0to4_mod47four"][1][0][0]
    actual_ap=cm(dot(W0,gcoef),inv(cm(hc,jp)))
    assert actual_ap==tuple(apoint)
    targetrow=rows[d]
    assert not targetrow["actual_frame_is_fc"]
    fcW=targetrow["fixed_Weierstrass"]["fc"]
    assert len(fcW)>1 and fcW[-1]==[1,0]
    assert all(x%47==0 for pair in fcW[:-1] for x in pair)
    assert data["principal"]["combined_function_to_actual_A1_t"]["f0_integer_exponent"]==0
    assert targetrow["fc_distinguished_cancelled_with_exact_zero_final_exponent"]
    assert fullnorm["all_unit_frames_allowed_with_exact_fc_cancellation"]
    normsource=locate(qc/"p41_ordinary_F2_unit_frame_norm47.py",scripts/"p41_ordinary_F2_unit_frame_norm47.py")
    assert fullnorm["source_sha256"]==sha(normsource)
    names.update(unit_frame_norm_source=normsource,ordinary_atlas=atlas_path,cusp_basis=cusp_path)
    # Re-evaluate the removable eta_B quotient from the independently saved
    # fixed-Norm chart.  Only exact Python integers and the published R2
    # coefficient lists are used here; no matrix/helper import is made.
    eta_path=source_dir/"p41_eta_calibration47_complete.json.gz"
    jets_name="p41_ORD_j28_F2_fixed_chart2_jets27.json.gz"
    jets_path=locate(qc/"ordinary-norm-cache"/jets_name,locate(qc/"norm-cache"/jets_name,source_dir/jets_name))
    eta,jets=read(eta_path),read(jets_path)
    assert jets["frame"]==chart["frame"] and jets["coordinate"]==chart["coordinate"]
    assert jets["W"][0][0]==W0 and jets["order"]==27
    eta_div=poly["eta_B_auxiliary_denominator_removable_division"]
    assert not eta_div["auxiliary_denominator_is_a_unit_at_center"]
    e=eta_div["actual_denominator_reduction_order"]
    length=eta_div["toeplitz_size"]
    assert e==1 and length==3*e+3
    qs=[x[0][0] for x in eta_div["denominator_coefficients_mod47cubed"]]
    ss=[x[0][0] for x in eta_div["numerator_coefficients_mod47cubed"]]
    qB=[x[0] for x in eta["denominator_coefficients"]]
    sB=[x[0] for x in eta["numerator_coefficients"]]
    for k in range(e+length):
        assert dot(jets["V2"][k][0],qB,q)==tuple(qs[k])
        assert dot(jets["V3"][k][0],sB,q)==tuple(ss[k])
    assert all(all(z%47==0 for z in x) for x in qs[:e]+ss[:e])
    assert (qs[e][0]**2+qs[e][1]**2)%47
    matrix=eta_div["unit_toeplitz_matrix_mod47cubed"]
    quotient=[x[0] for x in eta_div["quotient_coefficients_through_size_minus_one_mod47cubed"]]
    for i in range(length):
        for j in range(length):
            k=e+i-j
            assert matrix[i][j]==(qs[k] if k>=0 else [0,0])
        assert dot(matrix[i],quotient,q)==tuple(ss[e+i])
    for k in range(e):
        assert dot(qs[:k+1],list(reversed(quotient[:k+1])),q)==tuple(ss[k])
    bounds=[(length-k+e-1)//e for k in range(3)]
    assert bounds==eta_div["first_three_tail_error_valuation_bounds"] and min(bounds)>=4
    assert eta_div["quotient_coefficients_0to2_mod47cubed"]==[[[x]] for x in quotient[:3]]
    hseries=[tuple(x[0][0][part]%q for part in range(2)) for x in jets["Hc"][:3]]
    assert hseries[0]==tuple(x%q for x in hc)
    hnorm=pow((hseries[0][0]**2+hseries[0][1]**2)%q,-1,q)
    hi=[(hseries[0][0]*hnorm%q,-hseries[0][1]*hnorm%q)]
    for k in range(1,3):
        total=dot(hseries[1:k+1],list(reversed(hi[:k])),q)
        product=cm(hi[0],total,q)
        hi.append(tuple(-x%q for x in product))
    eta_piece=[]
    for k in range(3):
        val=dot(quotient[:k+1],list(reversed(hi[:k+1])),q)
        eta_piece.append([[[(-2*z)%q for z in val]]])
    assert eta_piece==poly["differential_pieces_coefficients_mod47cubed"]["minus2_eta_B"]
    pieces=poly["differential_pieces_coefficients_mod47cubed"]
    derivative_coefficients=[]
    for k in range(3):
        coefficient=[sum(v[k][0][0][part] for v in pieces.values())%q for part in range(2)]
        assert coefficient[1]==0
        derivative_coefficients.append(coefficient[0])
        assert [[coefficient]]==poly["local_differential_coefficients_0to2_in_z_mod47cubed"][k]
    assert height_poly[1:]==[x*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(derivative_coefficients)]
    names.update(eta_B_calibration=eta_path,fixed_norm_same_chart_jets=jets_path)
    out = {
        "disk_id":d,"input_sha256":{str(p):sha(p) for p in names.values()},
        "all19_nested_input_hash_edges_checked":checks,
        "based_point_and_terminal_point_hashes_match":True,
        "fixed_norm_j_tangent_and_sigma_values_match_independently":True,
        "mixed_frame_C_residues_recomputed_from_actual_quadratic_basis":True,
        "all73_Hv_coordinates_match_published_R231_tangent":True,
        "Hv_scale_matches_independent_physical_g1_over_dj":True,
        "nonunit_fc_Weierstrass":fcW,
        "exact_final_fc_exponent_zero":True,
        "eta_B_removable_numerator_denominator_recomputed_from_fixed_Norm_jets":True,
        "eta_B_all_unit_Toeplitz_and_omitted_low_equations_independently_verified":True,
        "eta_B_first_three_tail_error_valuation_bounds":bounds,
        "eta_B_actual_differential_recomputed_with_same_Hv_coordinate":True,
        "all_local_differential_pieces_and_integrated_height_coefficients_recomputed":True,
        "actual_g1_over_dj_base_center":[ab[0],apoint[0]],
        "canonical_sigma":sigma,"canonical_sigma_log":log_sigma,
        "signed_actual_scale":m,"second_divisor_tiny":tiny,"full_first_norm_log":normlog,
        "actual_center_height":actual_height,"local_polynomial":height_poly,
        "global_polynomial":global_poly,"QC_polynomial":qc_poly,
        "QC_div47_reduction":red,"residual_roots":roots,
        "residual_discriminant":discriminant,
        "simple_single_F2_root_candidates_to_available_precision":lifted,
        "scope":"Independent exact scalar arithmetic and input identity checks, plus source-diff review recorded separately; no duplicate RR, T2 or group-chain reexecution.",
        "source_sha256":sha(__file__),
    }
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print("PASS generic",d,"nested19hashes,physical parameters,nu,canonical tangent,center and QC scalars",sha(args.output))


if __name__=="__main__":
    main()

