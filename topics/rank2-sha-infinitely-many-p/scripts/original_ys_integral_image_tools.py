#!/usr/bin/env sage-python
"""Exact full-source integral images in the SAME original affine chart.

This optional helper replaces a graph-kernel construction ONLY when taking
the image of an already complete ideal under a fixed nonzero fraction.
Every one of the 306 source basis rows is divided exactly by the full
denominator multiplication matrix.  A nonzero polynomial remainder is an
error, never an instruction to clear a denominator or to keep a submodule.

No running engine or consumer is modified.  Complete denominator HNF and
image HNF may themselves be expensive; no performance result is assumed.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from original_ys_artinian_norm_tools import (
    OriginalArtinianNormTools, _whole_hermite_coordinates,
    SOURCE_DEPENDENCIES as NORM_SOURCE_DEPENDENCIES)
from original_ys_divisor_ideal_tools import (
    canonical, digest, field_description, finite_field_coordinates,
    polynomial_matrix_digest, element_digest, _hermite_remainder_rows,
    POLYNOMIAL_MATRIX_REFERENCE)


SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_ys_integral_image_tools.py",
) + NORM_SOURCE_DEPENDENCIES))


def _default_progress(stage, **data):
    print("RANK2_ORIGINAL_INTEGRAL_IMAGE_STAGE " +
          canonical(dict(stage=stage, **data)), flush=True)


class OriginalIntegralImageTools:
    """Optional whole-ideal image algorithm using an authenticated R931 object.

The input object retains the actual original ring, ordered basis, chart,
constant field, omega and multiplication table.  No method on that object
or its engine is overwritten.  integral_fraction_multiple returns the SAME
OriginalAffineIdeal type as the existing engine method.
"""
    def __init__(self, original_tools, progress=None):
        assert isinstance(original_tools, OriginalArtinianNormTools)
        self.tools = original_tools
        self.engine = original_tools.engine
        self.R, self.k, self.n = (
            original_tools.R, original_tools.k, original_tools.n)
        self.identity = original_tools.identity
        self.omega = original_tools.omega
        self.progress = progress or _default_progress
        self.receipts = []
        assert self.n == 306 and self.R.base_ring() is self.k
        assert self.engine.R is self.R and self.engine.k is self.k
        assert self.engine.identity is self.identity
        assert self.omega.parent() is self.k
        self.source_receipt = {
            "kind": "rank2_original_complete_integral_image_tools",
            "original_norm_tools": dict(original_tools.source_receipt),
            "original_constants": field_description(self.k),
            "original_normalization_signature_sha256": original_tools.signature,
            "actual_original_omega_coordinates": finite_field_coordinates(
                self.omega, self.k),
            "source_dependencies": list(SOURCE_DEPENDENCIES),
            "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "existing_engine_or_consumer_modified": False,
            "performance_or_original_shadow_claimed": False,
        }

    def integral_fraction_multiple(self, ideal, numerator, denominator,
                                   label="same original complete integral image"):
        """Return exactly (N/D)*I after proving EVERY source row maps integrally.

        H=U*MD is a complete polynomial row Hermite factorization.  Exact
        triangular coordinates give C*H=HI*MN; then V=C*U is the unique full
        image matrix and V*MD=HI*MN.  Its full row HNF is exactly (N/D)*I.
        No fraction-field kernel, row rescaling or partial source is used.
        """
        assert self.tools.engine is self.engine
        assert self.tools.R is self.R and self.tools.k is self.k
        assert self.tools.identity is self.identity
        assert self.tools.omega is self.omega
        I = self.tools._ideal(ideal)
        N, D = self.tools._element(numerator), self.tools._element(denominator)
        assert not N.is_zero() and not D.is_zero()
        MD = self.engine.multiplication_matrix(D)
        assert MD.base_ring() is self.R
        assert MD.nrows() == MD.ncols() == self.n
        self.progress("complete denominator Hermite image start", label=label,
                      rows=self.n, columns=self.n, original_source_length=I.length)
        started = time.monotonic()
        H, U = MD.hermite_form(include_zero_rows=False, transformation=True)
        assert H.base_ring() is self.R and U.base_ring() is self.R
        assert H.nrows() == H.ncols() == U.nrows() == U.ncols() == self.n
        assert H.is_hermite()
        assert all(H[j, j] and H[j, j].leading_coefficient() == 1
                   for j in range(self.n))
        assert all(not H[i, j] for i in range(self.n) for j in range(i))
        assert U*MD == H
        assert _hermite_remainder_rows(MD, H).is_zero()
        denominator_elapsed = time.monotonic()-started
        MN = self.engine.multiplication_matrix(N)
        assert MN.base_ring() is self.R and MN.nrows() == MN.ncols() == self.n
        W = I.basis*MN
        C = _whole_hermite_coordinates(H, W)
        assert C.base_ring() is self.R
        assert C.nrows() == C.ncols() == self.n and C*H == W
        V = C*U
        assert V.base_ring() is self.R and V.nrows() == V.ncols() == self.n
        assert V*MD == W
        image_certificate = {
            "label": label,
            "source_ideal_hnf_sha256": polynomial_matrix_digest(I.basis),
            "numerator_sha256": element_digest(N),
            "denominator_sha256": element_digest(D),
            "denominator_full_HNF_sha256": polynomial_matrix_digest(H),
            "denominator_full_transform_sha256": polynomial_matrix_digest(U),
            "denominator_HNF_both_complete_inclusions_verified": True,
            "complete_source_times_numerator_sha256": polynomial_matrix_digest(W),
            "complete_polynomial_division_coordinates_sha256": polynomial_matrix_digest(C),
            "complete_integral_image_rows_sha256": polynomial_matrix_digest(V),
            "all_306_original_source_basis_rows_divided_exactly": True,
            "every_image_row_times_original_denominator_returned": True,
            "entire_source_coefficient_module_equals_unit_module": True,
            "full_source_basis_preserved_without_rescaling": True,
            "fraction_field_rank_kernel_or_denominator_clearing_used": False,
            "polynomial_graph_kernel_computed": False,
            "denominator_full_HNF_elapsed_seconds": denominator_elapsed,
            "official_algorithm_reference": POLYNOMIAL_MATRIX_REFERENCE,
        }
        image = self.engine.ideal_from_rows(V, label, provenance=image_certificate)
        assert image.engine is self.engine
        self.tools._ideal(image)
        # This is equality of the WHOLE source image, not a norm/degree guess.
        image.receipt["entire_source_module_maps_integrally"] = True
        image.receipt["complete_original_integral_image"] = image_certificate
        record = {
            "operation": "same_original_fraction_times_complete_ideal",
            "original_normalization_signature_sha256": self.tools.signature,
            "original_ordered_integral_basis_sha256": digest(self.tools.basis_identity),
            "original_constants": field_description(self.k),
            "infinity_chart": bool(self.engine.infinity_chart),
            "source": image_certificate,
            "result": image.receipt,
            "same_original_engines_and_objects": True,
            "complete_nonreduced_image_ideal_certified": True,
            "complete_intersection_or_shadow_claimed": False,
        }
        self.receipts.append(record)
        self.progress("complete original integral image certified", label=label,
                      image_length=image.length, all_source_rows=self.n)
        return image

    def receipt_summary(self):
        return {
            "source": dict(self.source_receipt),
            "completed_operations": len(self.receipts),
            "operation_receipts_sha256": digest(self.receipts),
            "same_original_complete_nonreduced_ideals_only": True,
            "original_shadow_computed": False,
        }
