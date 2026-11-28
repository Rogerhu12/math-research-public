#!/usr/bin/env sage-python
"""Independent scalar fraction test including a cubic ramified pole on both real charts."""
import os
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Run only in the named public research Actions.")
import hashlib
from types import SimpleNamespace
from sage.all import GF, PolynomialRing, PowerSeriesRing, matrix, vector
import numpy as np
from section_quotient_algebra import canonical, digest
from original_descended_pencil_sections import (original_m2, original_endpoint_germ, normalized_level_sections,
                                              pack_polys, require)
from original_descended_pencil_kernel import certify_g3, WholePencil, packed_rank
from original_descended_pencil_physical import PhysicalReturn, reciprocal, selected_physical_sections
from original_descended_pencil_returns import compress_rectangular, pencil_ideals
import original_descended_pencil_binding as binding


class ScalarEngine:
    def __init__(self, k, flag):
        self.k, self.dimension, self.infinity_chart = k, 1, flag
        self.R = PolynomialRing(k, "s" if flag else "t")
        self.unit = vector(self.R, [1])

    def element(self, row):
        return vector(self.R, row)

    def multiply(self, a, b):
        return vector(self.R, [a[0]*b[0]])

    def multiplication_matrix(self, a):
        return matrix(self.R, [[a[0]]])

    def progress(self, *args, **kwargs):
        pass


def reject(fn):
    try:
        fn()
    except (ValueError, ArithmeticError):
        return True
    raise ArithmeticError("An intentionally damaged source survived")


def level_four_source(fp, modular):
    """Use the actual PARI source on X0(4) and the actual unramified cusp branch on X0(12)."""
    size, work = 42, 44
    require(modular.nrows() == 2 and modular.ncols() >= work+2, "Missing true global level-four jets")
    power = PowerSeriesRing(fp, "q", default_prec=work+2)
    q = power.gen()
    normalized = modular[:, :2].inverse()*modular
    require(normalized[0,0] == normalized[1,1] == 1 and normalized[0,1] == normalized[1,0] == 0,
            "The full cusp section and its complementary level-four section changed")
    # A/B has exactly the unique simple pole at infinity. Scaling its residue and
    # fixing its constant identifies the marked u, whose q-leading term is -1/(8q).
    A = power(normalized.row(0).list()[:work]).add_bigoh(work)
    Bunit = power(normalized.row(1).list()[1:work+1]).add_bigoh(work)
    rho = A/Bunit
    qu = ((-rho+rho[1]*q)/8).add_bigoh(work)
    require(qu[0] == -fp.one()/8 and qu[1] == 0, "Wrong normalized actual u")
    def relation(z):
        return z**4 + 18*q**2*z**2-27*q**4-8*qu*z**3
    z = power(-1).add_bigoh(work)
    known = 1
    while known < work:
        derivative = 4*z**3+36*q**2*z-24*qu*z**2
        require(derivative[0] == -1, "The selected physical t branch is not simple")
        z = (z-relation(z)/derivative).add_bigoh(work)
        known = min(2*known, work)
        require(relation(z).add_bigoh(known) == 0, "The actual level-four cusp root failed")
    eta = ((q*qu.derivative()-qu)/(qu**2-q**2)).add_bigoh(size)
    require(eta.precision_absolute() >= size and eta[0] == 8, "Incorrect independent log differential")
    junit = (-eta/(4*z**3)).add_bigoh(size)
    desired = matrix(fp, [[(q*eta)[i] for i in range(size)], [(qu*eta)[i] for i in range(size)]])
    change = desired[:, :2]*modular[:, :2].inverse()
    physical_forms = change*modular[:, :size]
    require(change.is_invertible() and physical_forms == desired,
            "The entire eta,u*eta frames are not the claimed true level-four modular rows")
    src = normalized_level_sections(physical_forms,z,junit,1,0,size)
    one = pack_polys(src["one"], size)
    require(one[0,1] == 1 and np.count_nonzero(one[0]) == 1 and
            np.array_equal(one[1],pack_polys([src["qu"]],size)[0]), "The true global 1,u did not return")
    recipes, rows = {}, {}
    for w in (4,8):
        recipes[w] = [(0,j) for j in range(w+1)]
        entries = [q**(w-j)*z**j for j in range(w+1)]
        rows[w] = matrix(fp, [[v[i] for i in range(w+1)] for v in entries])
    from section_quotient_algebra import matrix_digest
    return src, dict(constants=fp, monomial_rows=rows, monomial_recipes=recipes), dict(
        true_modular_input_columns=int(modular.ncols()), true_complete_weight_two_rank=int(change.rank()),
        matched_both_global_frames_through_order=size-1, normalized_branch_coefficients=work,
        full_returned_weight_two_jets_sha256=matrix_digest(physical_forms),
        actual_basis_change_sha256=matrix_digest(change))


def original_germ_checks(k):
    fp = k.prime_subfield()
    r = PolynomialRing(k, "omega"); omega = (r.gen()**2+r.gen()+1).roots(multiplicities=False)[0]
    r0 = PolynomialRing(fp, "q_high"); Q = r0.gen()
    records = []
    hi = {}
    for i,m in ((0,3),(2,612)):
        hi[i] = dict(A=(Q**(m-1)*(1+Q**1100), Q**(m+16) if i==2 else r0.zero()),
                     B=(Q**m*(1+Q**4), r0.zero()))
    scale = k(2)
    context = dict(constants=k, omega=omega, A=[dict(original_embedding=i,artin_index=j) for j,i in enumerate((0,2))],
                   artin_constants=dict(rows=[dict(embedding=i,artin_index=j,vnew=scale,dnew=k.one())
                                              for j,i in enumerate((0,2))]))
    context["cube_context"] = dict(constants=k, original_omega_codec=SimpleNamespace(field=k,omega=omega),
             extended_q_precision=6941,sigma_a_index=(2,0,1),selected_RP_high_sections=hi,
             map_context=dict(P={i:dict(vnew=scale) for i in (0,2)}))
    for j in (0,1):
        qf, rec = original_endpoint_germ(context, j, 1483)
        q = qf.parent().gen()
        correction = omega*q**17 if j else 0
        require(((qf-q)*(1+q**4)-1-q**1100-correction).add_bigoh(1483) == 0,
                "The two independent high-section components or the shift at 612 changed")
        records.append(rec)
    context["A"][1]["original_embedding"] = 1
    rejected = reject(lambda: original_endpoint_germ(context,1,1483))
    return dict(actual_sources=records, wrong_original_embedding_rejected=rejected)


def physical_case(k, lam, sections, apery):
    finite, infinity = ScalarEngine(k,False), ScalarEngine(k,True)
    poly = sections["ring"]
    small = PowerSeriesRing(k,"q",default_prec=20)
    q = small.gen()
    qu = small([k(sections["qu"][j]) for j in range(20)]).add_bigoh(20)
    qf = qu+lam*q**2/(qu-q)
    field, K, graph = certify_g3(sections,qf,1,0,2)
    require(graph["actual_complete_kernel_dimension"] == 2 and graph["true_equation_coefficients"] == 6,
            "Wrong genus-zero complete G3 rank")
    pencil = WholePencil(field, sections, 1,0,2)
    pairs, proof = pencil.select(K)
    a = pencil.multiplier_rows(pairs[0])
    repeated_rank = packed_rank(field,np.concatenate((a,a),axis=1))
    require(repeated_rank == proof["actual_independent_multiplier_rank"]-1,
            "A repeated section failed to expose its full common point")
    lift4 = PhysicalReturn(apery,finite,4)
    jet4 = pack_polys([(sections["z"]**3*b).truncate(5) for b in sections["one"]],5)
    one, u = lift4.read_planes(jet4[None,:,:],[k.one()])
    t = finite.R.gen()
    A = t**4+18*t**2-27
    B = 8*t**3
    require(one[0] == t**3 and u[0] == k.one()/8*A, "Physical W1 did not equal t^3 or t^3 u")
    H, receipt = selected_physical_sections(field, sections, pairs, PhysicalReturn(apery,finite,8))
    expected_N = vector(finite.R,[A*(A-B)+lam*B**2])
    expected_D = vector(finite.R,[B*(A-B)])
    N0, D0 = expected_N[0], expected_D[0]
    require(N0.gcd(D0).degree()==0 and (D0 % (t-3)**3)==0 and (D0 % (t-3)**4)!=0,
            "Independent scalar chart failed the actual cubic branch")
    objects = {False:H, True:[tuple(reciprocal(row,finite,infinity,[0],12) for row in pair) for pair in H]}
    short = reject(lambda: certify_g3(sections,qf.add_bigoh(5),1,0,2))
    require(short, "Short graph sample incorrectly survived")
    result = []
    for flag, E in ((False,finite),(True,infinity)):
        N,D = (reciprocal(expected_N,finite,infinity,[0],8),reciprocal(expected_D,finite,infinity,[0],8)) if flag else (expected_N,expected_D)
        pos, neg, rec = pencil_ideals(E,N,D,objects[flag],"whole aperture test",8,[0],
                        dict(actual_original_function_id=id(qf),actual_original_endpoint=0,G3=graph),(8,5 if flag else 7))
        require(pos.basis[0,0] == N[0].monic() and neg.basis[0,0] == D[0].monic(),
                "The actual canonical physical ideals disagree with the independent coprime rational fraction")
        source = objects[flag][0][0]
        altered = E.element(objects[flag][0][1])+E.unit
        rejected = reject(lambda: pencil_ideals(E,N,D,[(source,altered),objects[flag][1]],"bad physical row",
                8,[0],dict(actual_original_function_id=id(qf),actual_original_endpoint=0,G3=graph)))
        result.append(dict(positive=int(pos.length),negative=int(neg.length),wrong_physical_paired_image_rejected=rejected,
                   post_ideal_identity=rec["post_ideal_outer"]["complete_X_sha256"]))
    return dict(physical_charts=result,field_degree=int(k.degree()),complete_g3=graph,
                real_pencil=proof,actual_original_coordinate_receipt=receipt, short_germ_rejected=short,
                actual_repeated_pencil_rank=repeated_rank, actual_ramified_pole_order=3)


def rectangular_case(k):
    R = PolynomialRing(k,"b")
    t = R.gen()
    Y = matrix(R,[[1,t],[0,1],[1,t+1],[t,t**2]])
    X = t*Y
    B,C,rec = compress_rectangular(Y,X,[0,1],1)
    require(C == t*B and B.determinant().degree() == 0 and len(rec["actual_zero_rows"])==2,
            "Independent complete rectangular module did not return")
    altered = matrix(R, X)
    altered[3,0] += 1
    rejected_image = reject(lambda: compress_rectangular(Y,altered,[0,1],1))
    cap = matrix(R, X)
    cap[1,0] = t**40
    rejected_cap = reject(lambda: compress_rectangular(Y,cap,[0,1],1))
    return dict(full_source_rows=4, returned_rank=2, actual_deleted_zero_rows=len(rec["actual_zero_rows"]),
                changed_syzygy_rejected=rejected_image, excessive_attached_degree_rejected=rejected_cap,
                original_row_comparison=rec["all_original_rows_roundtripped"])


def main():
    fp = GF(29)
    ring = PolynomialRing(fp,"m")
    mod = ring.gen()**2-ring.gen()-fp.one()/4
    require(mod.is_irreducible(), "Wrong prescribed field for the genuine quadratic fixture")
    extension = GF(29**2,"a_pencil",modulus=mod)
    modular, small = original_m2(4,1,2,29,48)
    sections, apery, modular_frames = level_four_source(fp, modular)
    cases = [physical_case(fp,fp.one(),sections,apery),
             physical_case(extension,extension.gen(),sections,apery)]
    registered = binding.bind_original_endpoint_graphs()
    require(registered["reversible_new_call_sites"] == 1 and registered["mathematical_instances_by_binding"] == 0 and
            not binding.SESSIONS, "The real original source selection performed unexpected geometry")
    # Inspect the actual per-call object without running principal divisor geometry.
    _, scalar_session = binding.scalar._new_geometry_runner()
    require(scalar_session is not None and len(binding.SESSIONS) == 1 and not binding.SESSIONS[0].entries,
            "Changed per-call binding or original fallback")
    payload = dict(source_binding=registered, actual_selector_sessions=len(binding.SESSIONS),
           actual_selected_original_endpoint_calls=len(binding.SESSIONS[0].entries), status="all_descended_pencil_small_software_checks_completed",
           actual_small_modular_lattice=small, physical_modular_frames=modular_frames, actual_high_source_fixtures=original_germ_checks(extension),
           scalar_cases=cases, rectangular_cases=[rectangular_case(k) for k in (fp,extension)],
           physical_rank306_geometry_executed=False, original_level1156_lattice_executed=False)
    raw = canonical(payload)
    print("RANK2_DESCENDED_PENCIL_SOFTWARE_RESULT "+raw,flush=True)
    print("RANK2_DESCENDED_PENCIL_SOFTWARE_SHA256 "+hashlib.sha256(raw.encode()).hexdigest(),flush=True)


if __name__ == "__main__":
    main()
