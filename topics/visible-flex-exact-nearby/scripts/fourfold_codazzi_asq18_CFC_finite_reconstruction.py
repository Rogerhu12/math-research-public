"""ASQ18 whole global slot and certified low recovery on all original CFC columns."""
import hashlib
import json
from fractions import Fraction


TOPIC = "topics/visible-flex-exact-nearby"
PROOF = TOPIC + "/results/R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md"
PROOF_SHA = "82d2beb80d2023c0747c6c0927f0c98dd3fcebcb9376333496e05e55b38ce0f4"
RECOVERY_PROOF = TOPIC + "/results/R149-supplement-actual-low-coordinate-recovery-on-complete-physical-columns.md"
RECOVERY_PROOF_SHA = "a2dd99637667471a5bdc5fa2a2f4c509bf6c6aca0795afa1840cbe23c84dceef"
UACT_PATH = TOPIC + "/notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/actual-unit-disk-operator-Theta-low-square.json"
UACT_SHA = "17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc"
DCP_SHA = "2f90550a3c44e3b2a6c434179992dec191da149d08cfdc7876d379d4522c5e5b"
TRIAL_INVERSE_SHA = "982b6c5fe1d92dd9f42c8866963455c6d7a526353bf87605f70295f7565cae90"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def admit(root, proof_raw, dcp):
    recovery=(root/RECOVERY_PROOF).read_bytes()
    require(len(recovery)==4782 and sha(recovery)==RECOVERY_PROOF_SHA, "the full ASQ20 reconstruction proof")
    require(len(proof_raw) == 7319 and sha(proof_raw) == PROOF_SHA,
            "the whole proved ASQ18 global, low-error and finite-inverse scopes")
    require(dcp["execution"]["scientific_files"][0]["sha256"] == DCP_SHA
            and dcp["actual"]["completed_targets"] == dcp["manifest"]["target_order"]
            and len(dcp["actual"]["completed_targets"]) == 18,
            "the complete original DCP actual and execution as admitted by CFC")
    specs = [s for s in dcp["specs"].values() if s["path"] == UACT_PATH]
    require(len(specs) == 1 and specs[0]["sha256"] == UACT_SHA and specs[0]["bytes"] == 42477,
            "the same original full UACT ancestor inside DCP")
    raw = (root / UACT_PATH).read_bytes()
    require(len(raw) == 42477 and sha(raw) == UACT_SHA, "whole original UACT signed coordinate receipt")
    u = json.loads(raw)
    inv = u["private_trial_inverse_receipt"]
    require(u["complete"] is u["proved"] is True and len(u["completed_targets"]) == u["saved_record_count"] == 21
            and u["complete_coordinate_inverse"]["finite_coordinate_inverse_proved"] is True
            and u["private_square_receipt"]["sha256"] == "59407fb83861bdedd4694fef870012eba106944376fcca2d8add4f0a5bedd323"
            and u["private_square_receipt"]["shape"] == [96,96] and u["private_square_receipt"]["bytes"] == 73728
            and inv["bytes"] == 73728 and inv["shape"] == [96, 96] and inv["sha256"] == TRIAL_INVERSE_SHA
            and inv["dtype"] == "<f8" and inv["order"] == "C" and inv["exact_dyadic_trial"] is True,
            "the single genuine original low96 dyadic inverse")
    d = dcp["actual"]
    legacy = d["new_records"][d["completed_targets"][17]]["whole_global_Theta_error"]
    require(legacy == d["copied_complete_input_records"]["complete_WMT14_global_error"],
            "the earlier full WMA global fee in the same CFC slot")
    return {"proof_sha256": PROOF_SHA, "finite_recovery_proof_sha256": RECOVERY_PROOF_SHA, "original_DCP_sha256": DCP_SHA, "original_UACT_sha256": UACT_SHA,
            "original_global_Theta_slot": legacy, "original_low_inverse_slot": u["complete_coordinate_inverse"],
            "original_low_dyadic_inverse": inv, "original_low_square":u["private_square_receipt"]}


def whole_global(api, admitted):
    require(admitted["proof_sha256"] == PROOF_SHA and admitted["original_DCP_sha256"] == DCP_SHA,
            "the whole qualified CFC target row")
    return api.rational(13, 50)


def checked_private(path, spec):
    raw = path.read_bytes()
    require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"],
            "the entire original carrier: "+path.name)
    return raw


def restore_low_inverse(api, np, source, old, private, choose_ir, source_b):
    # The already restored whole grid is read without rerunning its construction.
    ir = old["IR"]["actual"]
    grid = json.loads(checked_private(private/"complete-original-IR-grid.json", ir["private_grid_receipt"]))
    points = [api.arb(v) for v in grid["all_balls"]]
    require(len(points) == 4096 and grid["complete_count"] == 4096,
            "one complete originally rounded inverse-lift grid")
    ir_raw = choose_ir(np,points)
    original = old["IR"]["actual"]["private_trial_receipt"]
    require(len(ir_raw) == original["bytes"] == 192*96*2*8 and sha(ir_raw) == original["sha256"],
            "whole original IR independent two-sign trial before the low square")
    ir_file = private/"ASQ18-same-original-IR-trial.f64"
    ir_file.write_bytes(ir_raw)
    z = np.frombuffer(checked_private(ir_file, original), dtype="<f8").reshape(192,96,2)
    alpha_file = private/"same-original-alpha-only"/"complete-original-AS-alpha-trial.json"
    ar = old["AS"]["actual"]["private_alpha_trial_receipt"]
    alpha_body = json.loads(checked_private(alpha_file, ar))
    require(len(alpha_body["all_positive_exact_pairs"]) == 2048
            and alpha_body["exact_mean"] == "0" and alpha_body["negative_modes_are_exact_conjugates"] is True,
            "both signs and the true original trial alpha")
    alpha = {0:api.acb(0)}
    for ell,(x,y) in enumerate(alpha_body["all_positive_exact_pairs"],1):
        a,b = api.rational(Fraction(x)),api.rational(Fraction(y))
        alpha[ell],alpha[-ell] = api.acb(a,b),api.acb(a,-b)
    root2=api.rational(2).sqrt()
    phases=[2*k*source_b+api.arb.pi()/4 for k in range(1,97)]
    trigs=[(x.cos(),x.sin()) for x in phases]
    low=np.empty((96,96),dtype="<f8")
    for j in range(96):
        primitive=[api.acb(api.rational(Fraction.from_float(float(x))),api.rational(Fraction.from_float(float(y))))/(4*n)
                   for n,(x,y) in enumerate(z[:,j,:],1)]
        for k,(cosine,sine) in enumerate(trigs,1):
            # Each retained output gets exactly the original increasing-input summation.
            v=api.acb(0)
            for n,p in enumerate(primitive,1):
                v=v+alpha[k-n]*p
            coeff=primitive[k-1]+v/api.acb(0,4*k)
            # The old DT and OT owners each saved/read its own formal 90-digit balls.
            c=api.acb(api.arb(coeff.real.str(90)),api.arb(coeff.imag.str(90)))
            entry=api.one*(root2*(c.real*cosine-c.imag*sine))
            low[j,k-1]=float(api.arb(entry.str(90)).mid())
    square_path=private/"ASQ18-same-original-low-square.f64"
    square_path.write_bytes(low.tobytes(order="C"))
    square=np.frombuffer(checked_private(square_path,source["original_low_square"]),dtype="<f8").reshape(96,96)
    inverse=np.ascontiguousarray(np.linalg.inv(square),dtype="<f8")
    inverse_file=private/"ASQ18-same-original-low-inverse.f64"
    inverse_file.write_bytes(inverse.tobytes(order="C"))
    inverse=np.frombuffer(checked_private(inverse_file,source["original_low_dyadic_inverse"]),dtype="<f8").reshape(96,96)
    return inverse, {"complete_original_IR_grid":ir["private_grid_receipt"],"complete_original_IR_trial":original,
                     "complete_original_alpha":ar,"original_low_square":source["original_low_square"],
                     "original_UACT_inverse":source["original_low_dyadic_inverse"],
                     "old_scientific_targets_called":0}


def integer_matrix(value):
    ratios=[[float(x).as_integer_ratio() for x in row] for row in value]
    power=max(den.bit_length()-1 for row in ratios for _,den in row)
    return [[num << (power-(den.bit_length()-1)) for num,den in row] for row in ratios],power


def exact_product(inverse, center, source, center_receipt, io):
    left,lp=integer_matrix(inverse)
    right,rp=integer_matrix(center)
    columns=list(zip(*right))
    entries=[[sum(x*y for x,y in zip(row,col)) for col in columns] for row in left]
    name="complete_ASQ18_recovered_signed_physical_columns"
    body={"kind":"CFC_complete_ASQ18_exact_recovered_low96_by_physical96_v1",
          "shape":[96,96],"common_binary_exponent":-lp-rp,"all_signed_integer_numerators":entries,
          "left_factor":source["original_low_dyadic_inverse"],"right_factor":center_receipt}
    require(io.json(name,body)==body,"all 9216 exact signed products read back before publication")
    return io.receipts[name]


def recovered_columns(api, np, source, theta, center_receipt, scalar, old, private, choose_ir, source_b, io):
    """The exact center is the ordered dyadic product X_UACT D_CFC, in root row/TC-column order."""
    center = theta["centers"]
    require(center.lo.shape == center.hi.shape == (96, 96)
            and (center.lo == center.hi).all() and center_receipt["shape"] == [96,96],
            "all9216 exact signed CFC center values")
    inverse, restored = restore_low_inverse(api,np,source,old,private,choose_ir,source_b)
    product = exact_product(inverse,center.lo,source,center_receipt,io)
    rows = [Fraction(0)] * 96
    columns = [Fraction(0)] * 96
    square = Fraction(0)
    for i in range(96):
        for j in range(96):
            x = Fraction.from_float(float(center.lo[i,j]))
            rows[i] += abs(x)
            columns[j] += abs(x)
            square += x*x
    hs = api.rational(square).sqrt().upper()
    schur = api.rational(max(rows)*max(columns)).sqrt().upper()
    norm = min(hs, schur)
    # ASQ18 gives rho <= 10^-15+2.523*.025 for Id-X T.
    # Hence ||T^-1-X|| <= 2.523*rho/(1-rho) < .170.
    radius = (api.rational(1347,500)*theta["true_joint"].upper()+api.rational(17,100)*norm).upper()
    return {"whole_ASQ18_inputs": source, "scope": "T_inverse_times_Theta_times_original_physical_X96",
            "exact_center_order": ["original_UACT_trial_inverse", "complete_CFC_signed_Theta_center"],
            "original_UACT_trial_inverse": source["original_low_dyadic_inverse"],
            "complete_CFC_signed_Theta_center": center_receipt, "complete_rows":96, "complete_columns":96,
            "signed_center_representation": "all9216 signed integer numerators with one common binary exponent",
            "exact_signed_product_carrier":product,"necessary_original_carrier_restoration":restored,
            "complete_CFC_center_Frobenius_upper": scalar(hs), "complete_CFC_center_Schur_upper": scalar(schur),
            "complete_CFC_true_Theta_joint_error": scalar(theta["true_joint"]),
            "T_inverse_norm_upper": "1347/500", "T_inverse_minus_original_dyadic_upper": "17/100",
            "T_low_block_error_upper": "1/40", "whole_Theta_global_error_upper": "13/50",
            "certified_joint_recovered_matrix_radius": scalar(radius),
            "independent_physical_mean_phase_height_and_other_high_responses_retained": True,
            "full_physical_Schur_inverse_proved": False}
