#!/usr/bin/env sage-python
"""One full scalar-preimage kernel on the SAME original integral Y chart.

This optional helper returns exactly I:(I+qA)=I:qA using the complete
polynomial left kernel [q Id; -H_I].  It preserves the actual R, k, original
ordered 306 basis, whole kernel and full quotient-times-common return.
No current consumer is changed and no mathematical computation runs locally.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from original_ys_artinian_norm_tools import (
    OriginalArtinianNormTools, SOURCE_DEPENDENCIES as NORM_SOURCE_DEPENDENCIES)
from original_ys_divisor_ideal_tools import (
    canonical, digest, polynomial_digest, polynomial_matrix_digest,
    _hermite_remainder_rows)

SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_ys_scalar_colon_tools.py",
) + NORM_SOURCE_DEPENDENCIES))


def _progress(stage, **data):
    print("RANK2_ORIGINAL_SCALAR_COLON_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


class OriginalScalarColonTools:
    """Optional complete I:qA using the caller's actual original norm tools."""
    def __init__(self, original_tools, progress=None):
        assert isinstance(original_tools, OriginalArtinianNormTools)
        self.tools, self.engine = original_tools, original_tools.engine
        self.R, self.k, self.n = original_tools.R, original_tools.k, original_tools.n
        self.identity = original_tools.identity
        self.progress = progress or _progress
        self.receipts = []
        assert self.n == 306 and self.R.base_ring() is self.k
        assert self.identity is self.engine.identity
        self.source_receipt = dict(
            kind="rank2_original_complete_scalar_colon_tools",
            original_norm_tools=dict(original_tools.source_receipt),
            source_dependencies=list(SOURCE_DEPENDENCIES),
            helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            existing_engine_or_consumer_modified=False,
            original_intersections_or_shadow_claimed=False)

    def effective_scalar_preimage(self, ideal, scalar, common_ideal=None,
                                  label="same original complete scalar preimage"):
        """Return I:qA and verify J*(I+qA)=I on the complete original chart."""
        assert self.tools.engine is self.engine
        assert self.tools.R is self.R and self.tools.k is self.k
        assert self.tools.identity is self.identity
        I = self.tools._ideal(ideal)
        assert scalar.parent() is self.R and scalar
        q = scalar
        scalar_ideal = self.engine.ideal_from_rows(
            q*self.identity, label+": entire scalar ideal")
        calculated, common_record = self.tools.ideal_sum(
            I, scalar_ideal, label+": actual I plus qA")
        C = calculated if common_ideal is None else self.tools._ideal(common_ideal)
        assert C.basis == calculated.basis
        assert _hermite_remainder_rows(I.basis, C.basis).is_zero()
        self.progress("complete original scalar preimage kernel start", label=label,
                      rows=2*self.n, columns=self.n,
                      scalar_degree=int(q.degree()), original_ideal_length=I.length)
        full_input = (q*self.identity).stack(-I.basis)
        K, kernel_record = self.engine.complete_kernel(
            full_input, expected_rank=self.n, label=label+": whole scalar preimage")
        assert K.base_ring() is self.R
        assert K.nrows() == self.n and K.ncols() == 2*self.n
        assert (K*full_input).is_zero()
        U, V = K[:, :self.n], K[:, self.n:]
        assert q*U == V*I.basis
        J = self.engine.ideal_from_rows(
            U, label, provenance=dict(
                entire_scalar_preimage_kernel=kernel_record,
                all_original_projected_source_rows_retained=True,
                fraction_field_kernel_or_denominator_clearing_used=False))
        assert _hermite_remainder_rows(q*J.basis, I.basis).is_zero()
        required, residual = I.determinant.quo_rem(C.determinant)
        assert not residual and required and required.leading_coefficient() == 1
        assert J.determinant == required
        product = self.engine.ideal_product(
            J, C, label+": full quotient times common ideal return")
        assert product.basis == I.basis and product.determinant == I.determinant
        assert J.length+C.length == I.length
        receipt = dict(
            operation="complete_original_scalar_effective_quotient", label=label,
            original_normalization_signature_sha256=self.tools.signature,
            original_ordered_integral_basis_sha256=digest(self.tools.basis_identity),
            infinity_chart=bool(self.engine.infinity_chart),
            original_scalar_sha256=polynomial_digest(q),
            scalar_multiplication_is_exactly_q_times_original_identity=True,
            original_unit_vector_not_replaced_by_a_basis_vector=True,
            entire_common_ideal_sum=common_record,
            common_ideal_equals_I_plus_qA_verified=True,
            full_dividend_in_divisor_inclusion_verified=True,
            entire_original_kernel=kernel_record,
            whole_kernel_sha256=polynomial_matrix_digest(K),
            whole_projected_module_sha256=polynomial_matrix_digest(U),
            every_original_kernel_coordinate_returned=True,
            entire_projected_module_equals_I_colon_qA=True,
            required_monic_determinant_sha256=polynomial_digest(required),
            complete_norm_equality_used_only_with_proved_containment=True,
            full_quotient_times_divisor_hnf_equals_dividend=True,
            complete_product_return=product.receipt,
            quotient=J.receipt,
            full_lengths=[I.length, C.length, J.length],
            complete_polynomial_kernel_count=1,
            reduced_support_or_closed_point_decomposition_used=False)
        self.receipts.append(receipt)
        self.progress("complete original scalar preimage certified", label=label,
                      full_length=J.length, whole_kernel_count=1)
        return J, receipt

    def receipt_summary(self):
        return dict(source=self.source_receipt, completed_operations=len(self.receipts),
                    operation_receipts_sha256=digest(self.receipts),
                    same_original_complete_nonreduced_ideals_only=True,
                    original_shadow_computed=False)
