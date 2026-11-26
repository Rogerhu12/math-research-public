#!/usr/bin/env sage-python
"""R955: all original Miller-line units from one complete thick product solve.

This is an optional process-local replacement for exactly one original
consumer method.  Every original line factor, constant special case, chain
square and complete quotient return is retained.  No reduced support,
point sample, saved coefficient table, alternative Miller function or
prime-field norm is used.  Mathematical execution is public Actions only.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import vector
import original_ys_artinian_shadow_consumer as original_consumer
from original_ys_artinian_shadow_consumer import (
    _WholeQuotient, _ideal_reference, _evaluate_miller, legacy,
    SOURCE_DEPENDENCIES as CONSUMER_DEPENDENCIES)
from original_ys_divisor_ideal_tools import (
    digest, element_digest, finite_field_coordinates)

ORIGINAL_MILLER_METHOD = original_consumer.OriginalArtinianShadowConsumer._miller_component_norm
SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_miller_batch_units.py",
) + CONSUMER_DEPENDENCIES))


def _complete_batch_inverses(consumer, quotient, factors, labels, label):
    """Invert every supplied actual factor in ONE unchanged full A/I."""
    q = quotient
    I = q.I
    assert q.tools is consumer.tools and q.engine is consumer.engine
    assert not I.is_unit() and not q.unit.is_zero()
    assert len(factors) == len(labels)
    reduced = [q.element(value) for value in factors]
    assert all(value == supplied for value, supplied in zip(reduced, factors))
    assert all(not value.is_zero() for value in reduced), (
        "An original nonconstant Miller line is zero on the entire component.")
    prefixes = [vector(q.R, q.unit)]
    for value in reduced:
        prefixes.append(q.multiply(prefixes[-1], value))
    if reduced:
        total_inverse, unit_solve = consumer.tools.inverse_unit(
            I, prefixes[-1], label+": sole complete original product inverse")
        total_inverse = q.element(total_inverse)
        assert q.multiply(prefixes[-1], total_inverse) == q.unit
        current_inverse = total_inverse
        inverses = [None]*len(reduced)
        for index in range(len(reduced)-1, -1, -1):
            inverse = q.multiply(prefixes[index], current_inverse)
            # Every original factor, not only the accumulated product, returns.
            assert q.multiply(reduced[index], inverse) == q.unit
            inverses[index] = inverse
            current_inverse = q.multiply(current_inverse, reduced[index])
            assert q.multiply(prefixes[index], current_inverse) == q.unit
        assert current_inverse == q.unit
        solves = 1
    else:
        inverses, unit_solve, solves = [], None, 0
        assert prefixes == [q.unit]
    collective = dict(
        operation="all_original_nonconstant_line_units_on_one_complete_thick_component",
        label=label, complete_ideal=_ideal_reference(I),
        ordered_original_factor_count=len(reduced),
        ordered_original_factor_labels=list(labels),
        ordered_original_factor_sha256=[element_digest(value) for value in reduced],
        complete_product_sha256=element_digest(prefixes[-1]),
        complete_product_unit_solve=unit_solve,
        complete_polynomial_unit_solve_count=solves,
        every_original_factor_and_inverse_returned_mod_entire_ideal=True,
        every_reverse_prefix_inverse_returned_mod_entire_ideal=True,
        entire_nonreduced_ideal_and_coefficient_field_unchanged=True,
        membership_or_nonzero_at_reduced_points_used=False,
        different_component_or_fraction_cache_used=False)
    collective_hash = digest(collective)
    records = []
    for index, (value, inverse, factor_label) in enumerate(zip(reduced, inverses, labels)):
        records.append(dict(
            operation="complete_thick_algebra_unit_inverse_from_verified_full_product",
            label=factor_label, complete_ideal=_ideal_reference(I),
            full_quotient_length=I.length,
            original_factor_index=index,
            value_sha256=element_digest(value),
            inverse_sha256=element_digest(inverse),
            collective_complete_product_unit_gate_sha256=collective_hash,
            exact_product_one_mod_whole_ideal_verified=True,
            separate_polynomial_unit_solve_falsely_claimed=False))
    return inverses, records, collective


def original_miller_component_norm_with_complete_batch_units(
        self, ideal, zx, zy, index, auxiliary, label):
    """The original Miller function; all line units share one full product solve."""
    assert isinstance(self, original_consumer.OriginalArtinianShadowConsumer)
    q = _WholeQuotient(self.tools, ideal)
    assert q.tools is self.tools and q.engine is self.engine
    assert not ideal.is_unit()
    zx, zy = q.element(zx), q.element(zy)
    q.curve_gate(zx, zy)
    chain = self.reader.chains[index]
    assert self.ell in (5, 7) and self.reader.ell == self.ell
    assert len(chain) == (3 if self.ell == 5 else 4)
    prepared, nonconstant, factor_labels, factor_slots = [], [], [], []
    constant_factor_count, vertical_line_count = 0, 0
    for line_index, (square, coefficients) in enumerate(chain):
        assert len(coefficients) == 5
        assert all(c.parent() is self.k for c in coefficients)
        ax, ay, a0, bx, b0 = coefficients
        numerator = q.add(
            q.add(q.scale(ax, zx), q.scale(ay, zy)), q.constant(a0))
        denominator = q.add(q.scale(bx, zx), q.constant(b0))
        constants = (a0 if ax == 0 and ay == 0 else None,
                     b0 if bx == 0 else None)
        entry = dict(square=square, coefficients=coefficients,
                     factors=(numerator, denominator),
                     inverses=[None, None], unit_records=[None, None])
        prepared.append(entry)
        # A vertical numerator still uses its actual ax*zx+a0; it is never
        # changed to a generic secant formula or discarded as a special point.
        if ay == 0 and ax != 0:
            vertical_line_count += 1
        for side, (name, value, constant) in enumerate(zip(
                ("numerator", "denominator"), entry["factors"], constants)):
            factor_label = "%s: original line %s %s" % (label, line_index, name)
            if constant is not None:
                inverse, record = self._line_inverse(
                    ideal, value, constant, factor_label)
                inverse = q.element(inverse)
                assert q.multiply(value, inverse) == q.unit
                entry["inverses"][side] = inverse
                entry["unit_records"][side] = record
                constant_factor_count += 1
            else:
                assert not value.is_zero(), (
                    "The actual original Miller %s at line %s is zero on this component."
                    % (name, line_index))
                nonconstant.append(value)
                factor_labels.append(factor_label)
                factor_slots.append((line_index, side))
    inverses, records, collective = _complete_batch_inverses(
        self, q, nonconstant, factor_labels, label)
    for (line_index, side), inverse, record in zip(factor_slots, inverses, records):
        prepared[line_index]["inverses"][side] = inverse
        prepared[line_index]["unit_records"][side] = record
    assert len(factor_slots) == len(inverses) == len(records)
    assert 2*len(prepared) == constant_factor_count+len(nonconstant)
    # For the unchanged binary chains at ell=5/7, the final vertical line
    # has constant denominator 1 and every other factor is nonconstant.
    assert constant_factor_count == vertical_line_count == 1
    assert len(nonconstant) == self.ell
    assert self.reader.chains[index] is chain

    value = vector(self.R, q.unit)
    chain_numerator, chain_denominator = vector(self.R, q.unit), vector(self.R, q.unit)
    line_records = []
    for line_index, ((square, coefficients), entry) in enumerate(zip(chain, prepared)):
        assert entry["square"] == square and entry["coefficients"] == coefficients
        numerator, denominator = entry["factors"]
        numerator_inverse, denominator_inverse = entry["inverses"]
        numerator_unit, denominator_unit = entry["unit_records"]
        assert numerator_inverse is not None and denominator_inverse is not None
        assert numerator_unit is not None and denominator_unit is not None
        # These are the original separate numerator/denominator unit gates.
        assert q.multiply(numerator, numerator_inverse) == q.unit
        assert q.multiply(denominator, denominator_inverse) == q.unit
        if square:
            value = q.square(value)
            chain_numerator = q.square(chain_numerator)
            chain_denominator = q.square(chain_denominator)
        factor = q.multiply(numerator, denominator_inverse)
        assert q.multiply(factor, denominator) == numerator
        value = q.multiply(value, factor)
        chain_numerator = q.multiply(chain_numerator, numerator)
        chain_denominator = q.multiply(chain_denominator, denominator)
        # Complete quotient identity for EACH original chain prefix.
        assert q.multiply(value, chain_denominator) == chain_numerator
        line_records.append({
            "line_index": line_index, "square_previous_value": bool(square),
            "same_original_five_line_coefficients": [
                finite_field_coordinates(c, self.k) for c in coefficients],
            "whole_numerator_unit": numerator_unit,
            "whole_denominator_unit": denominator_unit,
            "full_accumulator_sha256": element_digest(value),
            "complete_original_chain_prefix_numerator_sha256": element_digest(chain_numerator),
            "complete_original_chain_prefix_denominator_sha256": element_digest(chain_denominator),
            "whole_original_chain_prefix_identity_returned": True,
        })
        self.progress(
            "whole original Artinian Miller line certified",
            label=label, basis_index=index, line_index=line_index,
            full_component_length=ideal.length,
            numerator_and_denominator_entire_units=True)
    assert len(line_records) == len(prepared) == len(chain)
    assert self.reader.chains[index] is chain
    denominator_constant = _evaluate_miller(
        chain, auxiliary, lambda c: self.k(c), self.k)
    assert denominator_constant.parent() is self.k and denominator_constant != 0
    ratio = q.scale(denominator_constant**-1, value)
    assert q.scale(denominator_constant, ratio) == value
    norm, norm_record = self.tools.norm_unit(
        ideal, ratio, label+": full original k norm of shifted Miller ratio")
    assert norm.parent() is self.k and norm != 0
    batch_gate = dict(
        full_nonconstant_product_unit_gate=collective,
        actual_original_line_count=len(prepared),
        exact_constant_special_case_count=constant_factor_count,
        exact_nonconstant_original_factor_count=len(nonconstant),
        actual_original_vertical_line_count=vertical_line_count,
        complete_polynomial_unit_solve_count=collective["complete_polynomial_unit_solve_count"],
        original_five_coefficients_and_chain_order_preserved=True,
        actual_original_chain_object_retained=True,
        every_original_line_numerator_and_denominator_unit_verified=True,
        every_original_chain_prefix_identity_returned_on_full_quotient=True,
        same_complete_thick_norm_method_called=True,
        original_constant_auxiliary_divided_before_norm=True,
        direct_per_line_polynomial_solves_not_falsely_claimed=True,
        helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return norm, {
        "basis_index": index,
        "full_component": _ideal_reference(ideal),
        "auxiliary": legacy.point_coordinates(auxiliary),
        "all_original_miller_lines": line_records,
        "complete_original_batch_unit_gate": batch_gate,
        "miller_at_actual_original_auxiliary": finite_field_coordinates(
            denominator_constant, self.k),
        "auxiliary_constant_divided_before_full_thick_norm": True,
        "auxiliary_constant_automatically_has_entire_length_exponent": True,
        "full_ratio_sha256": element_digest(ratio),
        "complete_pi_layer_norm": norm_record,
        "norm_in_actual_original_k": finite_field_coordinates(norm, self.k),
        "no_degree_or_multiplicity_reduced_before_norm": True,
    }
