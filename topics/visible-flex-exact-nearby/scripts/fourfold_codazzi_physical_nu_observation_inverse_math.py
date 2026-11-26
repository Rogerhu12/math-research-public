"""PO: a new full96 observation inverse and the same physical nu high column.

No IO or numerical imports.  The public owner restores only necessary exact
old RW definitions.  Observations are NP's whole uninflated signed balls;
neither the NP trial nor any old pairing/norm/error target runs again.
"""

OUTPUT_ORDER = (
    "complete_RW_even96_inverse_identity_defect_upper",
    "complete_RW_even96_inverse_L2_upper",
    "complete_NP_even_physical_trial_reconstruction_radius_upper",
    "complete_NP_even_physical_trial_L2_upper",
    "complete_NP_even_physical_trial_angle_derivative_L2_upper",
    "same_true_H_mean_translation_removed_displacement_upper",
    "complete_NP_physical_trial_true_angle_high97_upper",
    "complete_true_NP_physical_primitive_L2_upper",
    "complete_true_NP_physical_high97_upper",
    "complete_true_NP_target_normalized_physical_L2_upper",
    "complete_true_NP_target_normalized_physical_highJ_upper",
    "complete_true_NP_physical_cosine96_error_upper",
)


def require(ok,message):
    if not ok:
        raise ValueError(message)


def magnitude(value):
    require(value.is_finite(),"finite whole real matrix coefficient or observation")
    return abs(value).upper()


def nonnegative(value):
    require(value.is_finite() and value.lower() >= 0,"whole nonnegative bound")
    return value.upper()


def minimum(*values):
    candidates = [nonnegative(x) for x in values]
    selected = candidates[0]
    for value in candidates[1:]:
        if value < selected:
            selected = value
    return selected


def frobenius(api,matrix):
    total = api.arb(0)
    for i in range(matrix.nrows()):
        for j in range(matrix.ncols()):
            value = magnitude(matrix[i,j])
            total += value*value
    return total.upper().sqrt().upper()


def complete_observation_inverse(api,rows,observations,saved,nh,publish,retain):
    """PO.1--21.  All96 columns, both Fourier signs, full true-error fee.

    retain(matrix,inverse,coefficients) stores/readbacks the complete private
    enclosures and returns all96 restored coefficient balls.  Public output
    consists only of twelve new scalar conclusions and private receipts.
    """
    names = ["row_%03d"%j for j in range(1,97)]
    require(list(rows) == list(observations) == names
            and all(len(rows[name]) == 1025 for name in names),
            "every original complete RW row and every raw physical observation")
    require(set(saved) == {"H1","m","E","BH","KW","D","H","W0","Wone_third"},
            "all whole original scalar receivers and same target normalizer")
    def save(index,value):
        return nonnegative(publish(OUTPUT_ORDER[index],value,"upper"))
    arb = api.arb
    root2 = arb(2).sqrt()
    matrix = api.arb_mat([[root2*rows[name][k] for k in range(1,97)] for name in names])
    inverse = matrix.inv()
    # A dyadic point preconditioner and BOTH complete products prove actual
    # nonsingularity.  The interval inverse then encloses the same exact M^-1.
    point_inverse = api.arb_mat([[inverse[i,j].mid() for j in range(96)] for i in range(96)])
    identity = api.arb_mat([[arb(int(i == j)) for j in range(96)] for i in range(96)])
    left,right = (frobenius(api,identity-point_inverse*matrix),
                  frobenius(api,identity-matrix*point_inverse))
    defect = save(0,left if left >= right else right)
    require(defect < 1,"the complete new96 observation matrix is actually invertible")
    save(1,frobenius(api,point_inverse)/(1-defect))
    observation_column = api.arb_mat([[observations[name]] for name in names])
    coefficients = inverse*observation_column
    values = retain(matrix,inverse,coefficients)
    require(len(values) == 96 and all(value.is_finite() for value in values),
            "whole private recovered column, no selected subset or midpoint data")
    radius2,norm2,derivative2 = arb(0),arb(0),arb(0)
    for k,value in enumerate(values,1):
        radius,absolute = magnitude(value-value.mid()),magnitude(value)
        radius2 += radius*radius
        norm2 += absolute*absolute
        derivative2 += (4*k)**2*absolute*absolute
    save(2,radius2.upper().sqrt())
    H1,BH,KW,E,D,H,W0,W13 = (nonnegative(saved[key]) for key in
        ("H1","BH","KW","E","D","H","W0","Wone_third"))
    m = saved["m"].lower()
    require(H1 >= 1 and BH >= 1 and KW >= 1 and m.is_finite() and m > 0,
            "full constant-one derivative Wiener bound and the same true H Jacobian")
    halfroot = (arb(1)/2).sqrt()
    N0 = save(3,minimum(norm2.upper().sqrt(),halfroot*H))
    N1 = save(4,derivative2.upper().sqrt())
    eta = H1-1
    displacement = save(5,eta/4)
    leakage = save(6,(displacement*H1.sqrt()*N1+eta*N0)/m)
    physical_error = (BH*halfroot*D).upper()
    full = save(7,minimum(BH*(N0+halfroot*D),
        halfroot*nh["complete_true_strict_nu_paired_L2_norm_upper"]))
    high = save(8,minimum(leakage+physical_error,full,
        halfroot*nh["complete_true_strict_nu_paired_high97_norm_upper"]))
    # This is the ORIGINAL same-sign B, with no source W^-1 A on an
    # independent physical nu column.  All Fourier modes and means survive.
    KB = (1+W0/4).upper()
    save(9,KB*full)
    # J=2^4608: Lambda_J^(-1/3) <= 2^-1536.  The exact rational 13/32
    # strictly bounds ||I||_{L2 -> H^(1/3)}=17^(1/6)/4.
    highJ_fee = (arb(1)/arb(2**1536))*W13*(arb(13)/32)*KB*full
    save(10,high+highJ_fee)
    save(11,minimum(E*N0+physical_error,
        nh["complete_true_strict_nu_physical_cosine96_error_upper"]))

