"""New exact D boundary-lift Gram targets in the original WVC coordinates.

Pure definitions, no numerical import, file access or import-time work.
The original reference-definition hashes are reidentified; no old norm,
Green action, actual centre packet, or successful source target is called.
"""
from fractions import Fraction
import hashlib

MODES = tuple(range(1, 97))
N, ROOT_ATOMS, OUTER_ATOMS = 193, 97, 96
PARTS_PER_PANEL = 16
RECORD_NAMES = [
    "reference_weighted_right97_body_upper",
    "reference_weighted_right97_root97_upper",
    "reference_weighted_right97_outer96_upper",
    "reference_weighted_right97_atoms193_upper",
    "reference_weighted_right97_complete_upper",
    "reference_joint193_boundary_body_upper",
    "reference_joint193_boundary_root97_upper",
    "reference_joint193_boundary_outer96_upper",
    "reference_joint193_boundary_atoms193_upper",
    "reference_joint193_boundary_complete_upper",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite(), "whole finite directed boundary-lift value")
    point = value.upper()
    require(api.lower(point) >= 0, "nonnegative mathematical upper")
    return point


def maximum(api, values):
    require(values, "nonempty complete modal family")
    return upper(api, api.hull([upper(api, value) for value in values]))


def sqrt_upper(api, value):
    return upper(api, api.sqrt(upper(api, value)))


def two_by_two_gram_eigen_upper(api, a, b, d):
    """Largest eigenvalue upper of an enclosed symmetric PSD 2x2 Gram.

    The signed off-diagonal is integrated first. Only here is its complete
    magnitude taken. Entrywise absolute domination gives the Perron bound.
    """
    aa, dd = upper(api, a), upper(api, d)
    bb = upper(api, api.magnitude(b))
    difference = upper(api, api.magnitude(aa-dd))
    disc = sqrt_upper(api, difference*difference+4*bb*bb)
    return upper(api, (aa+dd+disc)/2)


def prepare_same_reference(api, km, reference, assembly, admitted, provider,
                           display, progress):
    """Materialize only the original153 D/S definitions and low96 profiles.

    This is the exact reference-definition prefix of the accepted assembly,
    with both recorded hash chains checked. There is no actual-centre/family
    coefficient assembly and no high reference or Green bound preparation.
    """
    require(admitted["collar_inputs_verified"] is True and len(admitted["rows"]) == 4650,
            "complete original readonly admission")
    literals, rows, cubic = admitted["literals"], admitted["rows"], admitted["cubic"]
    parents = assembly._same_parent_mesh(literals)
    root_interval = tuple(map(Fraction, literals["rstar_interval"]))
    cut, outer = Fraction(literals["c_body"]), Fraction(literals["R"])
    require(len(parents) == 153 and outer == Fraction(25, 8), "same original radial definition")
    definitions = [None]
    selected = [{j: Fraction(0) for j in MODES}]
    chain = "947c13032e6e6dc6496e42d2a78b0178b41dbc4372069a321f3f501a07547df7"
    diagonal_chain = hashlib.sha256(b"complete_WVC_root_diagonal_is_zero_v1").hexdigest()
    for i, parent in enumerate(parents[1:], 1):
        definition = assembly._same_reference_definition(cubic, rows,
            (parent["left"]+parent["right"])/2, api, display)
        packet = assembly._same_exact_reference_coefficients(definition)
        values = {j: assembly._same_exact_tracefree_diagonal(packet, j,
                    4*j*abs(definition["eta_exact"]), Fraction(0))["selected"] for j in MODES}
        definitions.append(definition)
        selected.append(values)
        chain = hashlib.sha256(bytes.fromhex(chain)+bytes.fromhex(definition["reference_hash"])).hexdigest()
        raw = assembly._canonical_exact({str(j): str(values[j]) for j in MODES})
        diagonal_chain = hashlib.sha256(bytes.fromhex(diagonal_chain)+hashlib.sha256(raw).digest()).hexdigest()
        progress("same_exact_reference_definition", {"parents_verified": i+1,
            "reference_chain": chain, "selected_diagonal_chain": diagonal_chain,
            "old_bound_targets_recomputed": 0})
    require({"count": 153, "sha256": chain} == reference.REFERENCE_CHAIN == provider["reference_chain"]
            and {"count": 153, "sha256": diagonal_chain} == reference.DIAGONAL_CHAIN ==
                provider["reference_selection"]["selected_diagonal_chain"],
            "both complete original exact reference chains")
    panels, parent_indices = [], []
    split_points = (cut+Fraction(1, 16), outer-Fraction(1, 16))
    for i, parent in enumerate(parents):
        if i == 0:
            pieces = [(None, cut)]
        else:
            points = [parent["left"]]+[x for x in split_points
                if parent["left"] < x < parent["right"]]+[parent["right"]]
            pieces = list(zip(points, points[1:]))
        for left, right in pieces:
            panels.append({"left": left, "right": right, "parent_index": i})
            parent_indices.append(i)
    require(len(panels) == 155 and set(parent_indices) == set(range(153)),
            "complete original155 comparison cover")
    domain = km.RadialDomain(api, panels, root_interval, Fraction(0), Fraction(1))

    def exact(value):
        return api.rational(value.numerator, value.denominator)

    etas = [api.zero if i == 0 else exact(abs(definitions[i]["eta_exact"])) for i in parent_indices]
    qs = [api.one if i == 0 else exact(definitions[i]["q_exact"]) for i in parent_indices]
    diagonals = [{j: exact(selected[i][j]) for j in MODES} for i in parent_indices]
    identity = {"kind": "complete_fixed_WVC_signed_reference_identity_v1",
        "complete_original_WVC_file": dict(reference.WVC_ACTUAL_FILE),
        "original_reference_chain": dict(reference.REFERENCE_CHAIN),
        "selected_diagonal_chain": dict(reference.DIAGONAL_CHAIN),
        "same_original_D_S_and_true_root": True, "all_original_parent_definitions_verified": True,
        "no_completed_bound_target_recomputed": True, "scalar_trace_identically_zero": True,
        "reference_outer_impedance": "13/80", "fine_refinement": 160, "fine_cell_count": 24480,
        "finite_normalizer_rule": "rho2=1+h^2*(a^2+c^2*q^2)/12"}
    profiles = reference.prepare_signed_reference_profiles(api, domain, etas, qs,
        diagonals, parent_indices, identity, modes=MODES)
    theta = {j: api.rational(1+16*j*j)**api.rational(-5, 12) for j in MODES}
    require(all(api.lower(value) > 0 for value in theta.values()),
            "the exact original outer Hminus5over6 Riesz weights")
    return {"domain": domain, "profiles": profiles, "qs": qs, "theta": theta,
            "reference_identity": identity, "parent_indices": parent_indices,
            "only_original_D_definitions_materialized": True,
            "actual_centre_or_family_packets_materialized": False,
            "high_reference_or_Green_action_prepared": False}


def complete_boundary_lifts(api, context, progress):
    """Two new complete boundary targets, ten scalar observations in total.

    Inputs are either weighted right97 alone, or raw left96 plus that right97.
    Their output is always S-body, root odd96+mean, and weighted outer even96.
    The exact independent mean is retained. Both columns of each joint2x2
    Gram are integrated together before any norm or absolute cross term.
    """
    domain, profiles = context["domain"], context["profiles"]
    qs, theta = context["qs"], context["theta"]
    require(len(domain.cells) == 155 and profiles.modes == MODES
            and context["only_original_D_definitions_materialized"] is True,
            "complete original reference-only low193 boundary problem")
    body_grams = {j: [api.zero, api.zero, api.zero] for j in MODES}
    mean_body_squared = api.zero
    invparts = api.rational(1, PARTS_PER_PANEL)
    for i in range(155):
        q = qs[i]
        require(api.lower(q) > 0, "whole positive original body weight")
        h = domain.full_length(i)
        mean_body_squared += h*q*q
        width = h*invparts
        for j in MODES:
            inverse_theta = api.one/theta[j]
            for part in range(PARTS_PER_PANEL):
                box = (i, Fraction(part, PARTS_PER_PANEL), Fraction(part+1, PARTS_PER_PANEL))
                value = profiles.at(j, box)
                tail = profiles.to_right(j, box)
                # Exact homogeneous raw columns are (-p*g,g) and tail*(K,H).
                # The right Robin input is multiplied once by Theta^{-1}.
                x0, y0 = -value["p"]*value["g"], q*value["g"]
                x1, y1 = tail*value["K"]*inverse_theta, q*tail*value["H"]*inverse_theta
                gram = body_grams[j]
                gram[0] += width*(x0*x0+y0*y0)
                gram[1] += width*(x0*x1+y0*y1)
                gram[2] += width*(x1*x1+y1*y1)
        # Only complete scalar integrals persist. Node profiles are already
        # stored by the original reference; whole-box cache stays one-panel.
        profiles.cache.clear()
        if i % 8 == 7 or i == 154:
            progress("complete_reference_boundary_gram_panels", {"panels_complete": i+1,
                "complete_original_panels": 155, "modes": 96,
                "whole_subboxes_per_panel_mode": PARTS_PER_PANEL,
                "old_bound_targets_recomputed": 0, "new_boundary_targets": 2})
    mean_body_squared = upper(api, mean_body_squared)
    right = {name: [] for name in ("body", "root", "outer", "atoms", "complete")}
    joint = {name: [] for name in right}
    # Mean input is the original independent moving-even terminal value.
    # Its D solution is constant, root mean is one, outer even slot is zero.
    for result in (right, joint):
        result["body"].append(mean_body_squared)
        result["root"].append(api.one)
        result["outer"].append(api.zero)
        result["atoms"].append(api.one)
        result["complete"].append(upper(api, mean_body_squared+api.one))
    for j in MODES:
        data = profiles.mode[j]
        pa, gr, hr = data["p"][0], data["g"][-1], data["H"][-1]
        th = theta[j]
        root0, root1 = -pa, gr/th
        outer0, outer1 = th*gr, hr
        aa = root0*root0+outer0*outer0
        ab = root0*root1+outer0*outer1
        ad = root1*root1+outer1*outer1
        ba, bb, bd = body_grams[j]
        right["body"].append(upper(api, bd))
        right["root"].append(upper(api, root1*root1))
        right["outer"].append(upper(api, outer1*outer1))
        right["atoms"].append(upper(api, ad))
        right["complete"].append(upper(api, bd+ad))
        joint["body"].append(two_by_two_gram_eigen_upper(api, ba, bb, bd))
        joint["root"].append(upper(api, root0*root0+root1*root1))
        joint["outer"].append(upper(api, outer0*outer0+outer1*outer1))
        joint["atoms"].append(two_by_two_gram_eigen_upper(api, aa, ab, ad))
        joint["complete"].append(two_by_two_gram_eigen_upper(api, ba+aa, bb+ab, bd+ad))
    values = [sqrt_upper(api, maximum(api, result[name])) for result in (right, joint)
              for name in ("body", "root", "outer", "atoms", "complete")]
    require(len(values) == len(RECORD_NAMES) == 10, "all complete boundary observations")
    return values
