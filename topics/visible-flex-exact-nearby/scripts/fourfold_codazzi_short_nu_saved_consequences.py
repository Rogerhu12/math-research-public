"""ASB exact rational consequences of whole completed SB, PA and PO balls.

No old carrier, norm, pairing, matrix, residual or scalar integral runs.
Square-root factors are replaced only by explicitly proved rational bounds.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json

TOPIC = "topics/visible-flex-exact-nearby"
INPUTS = {
    "SB":("notes/short_strict_nu_error_ci/run-45908403884-1/actual-short-strict-nu-error.json",
          "1983678692d346b7cf22e8baace984758657e23706be6b43a3c038eed62bd873",11),
    "PA":("notes/strict_nu_amplitude_border_ci/run-45906257068-1/actual-strict-nu-amplitude-border.json",
          "04d09519aeeaaf7d63d1efcc6ee38481a3cdbf25dfaa9868dd8558ecd4e35387",8),
    "PO":("notes/physical_nu_observation_inverse_ci/run-45903437912-1/actual-physical-nu-observation-inverse.json",
          "39060a8df22553647ad82d80348996e1ae1ae10e2c04582615b10127f590ccee",12),
}


def require(ok,message):
    if not ok:raise ValueError(message)


def interval(record):
    def text_ball(value):
        text = value.strip().strip("[]").strip();parts = text.split("+/-")
        centre = F(parts[0].strip()) if parts[0].strip() else F(0)
        radius = F(parts[1].strip()) if len(parts) == 2 else F(0)
        require(len(parts) <= 2 and radius >= 0,"complete finite rational display ball")
        return centre-radius,centre+radius
    pairs = [text_ball(record[key]) for key in ("ball","lower","upper") if key in record]
    require(pairs,"whole actual native ball")
    return min(x[0] for x in pairs),max(x[1] for x in pairs)


def consequences(root):
    root = Path(root);docs = {}
    for name,(path,digest,count) in INPUTS.items():
        raw = (root/TOPIC/path).read_bytes();doc = json.loads(raw)
        require(hashlib.sha256(raw).hexdigest() == digest,"whole completed original "+name)
        require(doc["complete"] is doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"] == 0 and doc["saved_record_count"] == count
            and len(doc["completed_targets"]) == count and set(doc["completed_targets"]) == set(doc["new_records"]),
            "entire actual completed conclusion")
        docs[name] = doc
    SB,PA,PO = (docs[name] for name in ("SB","PA","PO"))
    require(SB["reference_identity"] == PA["reference_identity"] == PO["reference_identity"]
        and SB["selected_member_identity"] == PA["selected_member_identity"] == PO["selected_member_identity"],
        "the same original implicit selected member and true strict particular")
    checks = []
    def upper(name,value,bound):
        require(value < F(bound),name+" strict rational upper")
        checks.append({"name":name,"strict_upper":bound,"passed":True})
    bounds = [".577270977",".577273187","1.478429e-7","4.253890","7.661355",
              "6.289073e-7","1.132677e-6","2.125887e-6","7.501268","1.594684e-5","6.765672e-6"]
    for name,bound in zip(SB["completed_targets"],bounds):upper(name,interval(SB["new_records"][name])[1],bound)
    D = interval(SB["new_records"][SB["completed_targets"][5]])[1]
    rows = PA["new_records"];names = PA["completed_targets"]
    a = interval(PA["new_amplitude_input_receipts"]["whole_waist_a"])[0]
    K = -interval(PA["new_amplitude_input_receipts"]["whole_waist_K"])[1]
    mean = interval(PA["copied_prior_scalar_records"]["selected_mean"])
    require(mean[1] < 0 and a > 0 and K > 0,"whole same-waist denominator inputs")
    n = a*a/((-mean[0])**2);denominator = F(24,25)
    require(n**4*K > denominator**4,"true n_g sqrt(q)>24/25 by exact positive fourth powers")
    checks.append({"name":"same_true_waist_ng_sqrtq","strict_lower":"24/25","passed":True})
    fee = interval(rows[names[4]])[1]+interval(rows[names[2]])[1]*D/denominator
    upper("new_complete_physical_amplitude_error",fee,"5.089e-6")
    signed = interval(rows[names[3]]);physical = (signed[0]-fee,signed[1]+fee)
    alpha = F(PA["parameters"]["exact_alpha"]);normalized = tuple(x/alpha for x in physical)
    for name,value,left,right in (("true_physical_amplitude",physical,"-.006275","-.006264"),
                                 ("true_original_alpha_normalized_amplitude",normalized,"-.008203","-.008188")):
        require(F(left) < value[0] <= value[1] < F(right),"entire signed enclosure: "+name)
        checks.append({"name":name,"strict_enclosure":[left,right],"passed":True})
    old = PO["copied_prior_scalar_records"]["original_bounds"];pn = PO["new_records"];order = PO["completed_targets"]
    BH,W0,W13,E = (interval(old[key])[1] for key in ("BH","W0","Wone_third","E"))
    N0 = interval(pn[order[3]])[1];leakage = interval(pn[order[6]])[1]
    halfroot = F(5,7);require(2*halfroot**2 > 1,"rational upper for 1/sqrt2")
    physical_error = BH*halfroot*D
    full = BH*(N0+halfroot*D);high = leakage+physical_error
    KB = 1+W0/4;high_fee = F(1,2**1536)*W13*F(13,32)*KB*full
    upper("true_physical_parameter_L2",full,".0016047")
    upper("true_physical_parameter_high97",high,"5.330e-5")
    upper("same_original_B_inverse_parameter_L2",KB*full,".1696")
    upper("same_original_B_inverse_high_tail_fee",high_fee,"1e-450")
    upper("same_original_B_inverse_parameter_high_at_2pow4608",high+high_fee,"5.330e-5")
    upper("true_physical_cosine96_joint_error",E*N0+physical_error,"6e-7")
    return {"kind":"ASB_exact_rational_consequences_of_whole_completed_outputs_v1",
        "input_sha256":{name:item[1] for name,item in INPUTS.items()},"checks":checks,
        "old_scientific_targets_evaluated":0,"original_B_same_sign_order_retained":True,
        "both_means_and_full_true_Fourier_error_retained":True,"full_phase_height_or_Schur_proved":False}


if __name__ == "__main__":
    print(json.dumps(consequences(Path(__file__).resolve().parents[3]),sort_keys=True))
