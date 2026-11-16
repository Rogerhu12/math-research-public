#!/usr/bin/env python3
"""R880(A3)-(A5): coefficient arithmetic for actual original shadow traces.

This is a consumer helper, not a producer of intersection points.  The caller
must supply the complete divisor multiplicities and residue-field traces for
all eighteen original point-factor Artin labels and all nine endpoint pairs.
Each input vector is the coordinates of [6] times that complete trace in one
fixed, verified E_0[ell] basis.  Geometry and character coefficients never share
a finite-field Frobenius.  The two original characteristic-zero certificates
must have succeeded before this helper is used by the geometric consumer.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

ORIGINAL_PAIRS = ((0, 1), (1, 2), (2, 0))
ORIGINAL_FORM_LABELS = ("g10", "g16", "g4")


def _certificate_sources(first_certificate, packet_certificate):
    if first_certificate.get("certified_original_first_factor") is not True:
        raise ValueError("The original F certificate has not succeeded.")
    if packet_certificate.get("certified_original_map") is not True:
        raise ValueError("The original rational-Hecke P certificate has not succeeded.")
    return {
        "first_source": first_certificate.get("source"),
        "first_run": first_certificate.get("run_id"),
        "packet_source": packet_certificate.get("source"),
        "packet_run": packet_certificate.get("run_id"),
    }


def original_two_axis_shadow_readout(
        *, prime, ell, coefficient_field, zeta9, cm_matrix_omega,
        artin_labels, complete_trace_vectors, character_values_by_pair,
        first_certificate, packet_certificate, identity_index=0):
    """Return the three original CM-sign readouts, each equal to [6]S in (A5).

    coefficient_field is the character field in characteristic ell, not the
    geometric field in characteristic prime.  zeta9 represents the fixed b/alpha
    of R880, so the coefficient omega is zeta9**6.

    cm_matrix_omega is the actual action of the geometric automorphism
    (x,y)->(omega_geometry*x,y) on the supplied E_0[ell] basis.  It is a 2 by 2
    matrix over F_ell, with columns recording images of the two basis points.

    artin_labels lists all 18 point-factor elements in the exact order used by
    complete_trace_vectors.  The latter has shape 18 x 3 x 3 x 2.  It contains
    coordinates of
        [6] Alb F^sigma_* (A_b^sigma q2 - phi_prime A_a^sigma q0)^*[O].
    At every place use the original normalizations and full closed-point trace.

    character_values_by_pair[(j,k)] is chi(sigma), in the same label order,
    for the required original finite character.  These characters are supplied
    by the original Artin model; their identity and labels are not reconstructed
    from finite-field Frobenius or from the point vectors.

    The helper certifies coefficient arithmetic conditional on these actual
    geometric inputs.  It does not claim that arbitrary vectors are cycle data.
    """
    prime, ell = int(prime), int(ell)
    if (prime, ell) not in ((29, 5), (41, 7)):
        raise ValueError("Use the original r=29/ell=5 or r=41/ell=7 detector.")
    sources = _certificate_sources(first_certificate, packet_certificate)
    F = coefficient_field
    zero, one = F(0), F(1)
    if one == zero or F(ell) != zero:
        raise ValueError("Incorrect character-field characteristic.")
    zeta = F(zeta9)
    if zeta**9 != one or zeta**3 == one:
        raise ValueError("The supplied b/alpha must be the original primitive ninth root.")
    omega = zeta**6
    if omega**2 + omega + one != zero:
        raise ValueError("Inconsistent coefficient CM embedding.")

    labels = tuple(str(x) for x in artin_labels)
    if len(labels) != 18 or len(set(labels)) != 18:
        raise ValueError("All eighteen original point-factor Artin labels are required.")
    identity_index = int(identity_index)
    if not 0 <= identity_index < 18:
        raise ValueError("Invalid original identity label.")
    if len(complete_trace_vectors) != 18:
        raise ValueError("Missing an original Artin row.")
    for row in complete_trace_vectors:
        if len(row) != 3 or any(len(v) != 3 for v in row):
            raise ValueError("Every Artin row requires all nine original endpoint traces.")
        if any(len(row[a][b]) != 2 for a in range(3) for b in range(3)):
            raise ValueError("Use the same two coordinates of the verified torsion basis.")

    if len(cm_matrix_omega) != 2 or any(len(row) != 2 for row in cm_matrix_omega):
        raise ValueError("A complete two by two geometric CM matrix is required.")
    M = [[int(cm_matrix_omega[i][j]) % ell for j in range(2)] for i in range(2)]
    if ((M[0][0] + M[1][1] + 1) % ell != 0 or
            (M[0][0]*M[1][1] - M[0][1]*M[1][0] - 1) % ell != 0):
        raise ValueError("The matrix is not the faithful rank-two action of the original omega.")
    for i in range(2):
        for j in range(2):
            value = sum(M[i][k]*M[k][j] for k in range(2)) + M[i][j] + int(i == j)
            if value % ell:
                raise ValueError("The supplied geometric CM action does not satisfy Phi_3.")

    def project_cm(v):
        mv = [sum((F(M[i][j])*v[j] for j in range(2)), zero) for i in range(2)]
        return tuple((mv[i] - omega**2*v[i])/(omega-omega**2) for i in range(2))

    projected = {}
    normalization = one/F(162)
    zetas = tuple(omega**j*zeta for j in range(3))
    if set(character_values_by_pair) != set(ORIGINAL_PAIRS):
        raise ValueError("Keep exactly the original three ordered newform pairs.")
    for pair in ORIGINAL_PAIRS:
        j, k = pair
        chars = tuple(F(c) for c in character_values_by_pair[pair])
        if len(chars) != 18 or chars[identity_index] != one:
            raise ValueError("Original character and identity labels are inconsistent.")
        if any(c**18 != one for c in chars):
            raise ValueError("An original order-eighteen character value is missing.")
        value = [zero, zero]
        for sigma_index in range(18):
            row = complete_trace_vectors[sigma_index]
            chi_inverse = one/chars[sigma_index]
            for a in range(3):
                for b in range(3):
                    coefficient = chi_inverse * zetas[j]**a * zetas[k]**b * normalization
                    for component in range(2):
                        value[component] += coefficient*F(int(row[a][b][component]) % ell)
        projected[pair] = project_cm(value)

    nonzero = tuple(pair for pair in ORIGINAL_PAIRS if any(x != zero for x in projected[pair]))
    return {
        "prime": prime,
        "ell": ell,
        "point_multiplier": 6,
        "cm_sign": "omega under the original coefficient embedding",
        "zeta_label": "b/alpha from R880",
        "original_form_labels": ORIGINAL_FORM_LABELS,
        "artin_labels": labels,
        "cm_matrix_omega": tuple(tuple(x for x in row) for row in M),
        "readouts": projected,
        "nonzero_original_pairs": nonzero,
        "certificate_sources": sources,
        "interpretation": (
            "Each vector is the actual [6] multiple of the corresponding original "
            "CM-sign, two-axis, full-Artin shadow, conditional on the supplied "
            "complete geometric divisor traces.  Nonzero implies the original "
            "rational ell-adic AJ is nonzero by R880(A4) and R859 torsion-freeness."
        ),
    }
