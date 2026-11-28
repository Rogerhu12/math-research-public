#!/usr/bin/env python3
"""Reproduce the complete R725 seed source from its complete published parent.

This is a stdlib source-text constructor. It imports no scientific source and
does not run AST, compile, a scientific fixture, or any numerical calculation.
It is not a required scientific preflight stage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PARENT_NAME = "fixed_fejer_paired_halfwave_meridian_reference.py"
PARENT_BYTES = 43697
PARENT_SHA256 = "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0"
PARENT_GIT_BLOB_SHA = "cc877246e546b8294826ad38d33b3eb2f7434f25"
OUTPUT_NAME = "fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py"
OUTPUT_BYTES = 51540
OUTPUT_SHA256 = "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f"
PATCHES = json.loads(r'''[
  {
    "label": "source_description",
    "expected_count": 1,
    "old": "The exact definition retains the R708/R709 boundary mean and the R711 scalar\namplitude, with a positive halfwave on the first central interval and its\nnegative on the second equal central interval. The original unit meridian\noutside two fixed supports and every normalized boundary blend are retained.",
    "new": "The exact definition retains the R708/R709 normalized boundary mean and the R711\nscalar amplitude, with the same opposite paired halfwaves. Only the boundary\ncutoff is changed to the complete fixed-epsilon R725 three-piece C3 law.\nThe original unit meridian outside two fixed supports is unchanged."
  },
  {
    "label": "current_seed_schema",
    "expected_count": 1,
    "old": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1\"",
    "new": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1\""
  },
  {
    "label": "fixed_cutoff_constant_and_complete_pure_functions",
    "expected_count": 1,
    "old": "DEFAULT_SUPPORT = ((\"1/32\", \"15/32\"), (\"17/32\", \"31/32\"))\n",
    "new": "DEFAULT_SUPPORT = ((\"1/32\", \"15/32\"), (\"17/32\", \"31/32\"))\n\nBOUNDARY_CUTOFF_EPSILON = \"1/8\"\nBOUNDARY_CUTOFF_SCHEMA = \"complete-fixed-width-three-piece-C3-boundary-cutoff-v1\"\n\n\ndef _flat_cutoff_polynomial_jets(t, epsilon):\n    \"\"\"Exact arithmetic for Fraction inputs; working arithmetic for float inputs.\"\"\"\n    zero, one = t*0, t*0+1\n    if t <= zero:\n        return zero, zero, zero, zero\n    if t >= one:\n        return one, zero, zero, zero\n    denominator = one-epsilon\n    if epsilon <= t <= one-epsilon:\n        return (t-epsilon/2)/denominator, one/denominator, zero, zero\n    reflected = t > one-epsilon\n    u = (one-t)/epsilon if reflected else t/epsilon\n    G = (u*u*u*u)*(5+u*(-6+2*u))/2\n    S = u*u*u*(10+u*(-15+6*u))\n    S1 = 30*u*u*(one-u)*(one-u)\n    S2 = 60*u*(one-u)*(one-2*u)\n    value = epsilon*G/denominator\n    first = S/denominator\n    second = S1/(epsilon*denominator)\n    third = S2/(epsilon*epsilon*denominator)\n    if reflected:\n        return one-value, first, -second, third\n    return value, first, second, third\n\n\ndef boundary_cutoff_exact_jets(t):\n    \"\"\"R725 value and first three normalized-coordinate derivatives, all exact.\"\"\"\n    t = exact_fraction(t, \"boundary cutoff coordinate\")\n    return _flat_cutoff_polynomial_jets(t, F(BOUNDARY_CUTOFF_EPSILON))\n\n\ndef boundary_cutoff_working_jets(t):\n    \"\"\"The same complete three pieces, with explicit working float arithmetic.\"\"\"\n    t = float(t)\n    if not math.isfinite(t) or not 0. <= t <= 1.:\n        raise ValueError(\"Use a finite complete boundary cutoff coordinate in [0,1]\")\n    result = _flat_cutoff_polynomial_jets(t, float(F(BOUNDARY_CUTOFF_EPSILON)))\n    if (len(result) != 4 or any(not math.isfinite(v) for v in result)\n            or not 0. <= result[0] <= 1. or result[1] < 0):\n        raise ValueError(\"A complete boundary cutoff jet is nonfinite or outside its working range\")\n    return tuple(float(v) for v in result)\n\n\ndef boundary_cutoff_definition(support, central):\n    \"\"\"Complete fixed-rational three-piece law and every exact physical cut.\"\"\"\n    epsilon = F(BOUNDARY_CUTOFF_EPSILON)\n    support = tuple(tuple(F(v) for v in pair) for pair in support)\n    central = tuple(tuple(F(v) for v in pair) for pair in central)\n    if (epsilon != F(1,8) or len(support) != 2 or len(central) != 2\n            or any(len(pair) != 2 for pair in support+central)):\n        raise ValueError(\"This source fixes the complete R725 cutoff at epsilon=1/8\")\n    edges = (F(0), epsilon, F(1)-epsilon, F(1))\n    layers = []\n    for index, ((left, right), (ca, cb)) in enumerate(zip(support, central)):\n        if not left < ca < cb < right:\n            raise ValueError(\"Every complete original boundary and central interval is required\")\n        for side, a, b, orientation in ((\"left\", left, ca, 1), (\"right\", cb, right, -1)):\n            physical = tuple(a+(b-a)*v for v in edges)\n            layers.append(dict(support_index=index, side=side,\n                exact_relative_interval=[str(a),str(b)],\n                exact_relative_piece_edges=[str(v) for v in physical],\n                exact_relative_internal_cuts=[str(v) for v in physical[1:-1]],\n                original_interval_normalized_piece_edges=[str(v) for v in edges],\n                cutoff_coordinate=\"t\" if orientation == 1 else \"1-t\",\n                odd_material_derivative_orientation=orientation,\n                physical_piece_count=3,\n                branches_in_increasing_material_order=(\n                    [\"left-polynomial\",\"affine\",\"right-reflection\"] if orientation == 1 else\n                    [\"right-reflection\",\"affine\",\"left-polynomial\"])))\n    return dict(schema=BOUNDARY_CUTOFF_SCHEMA, proof_result=\"R725\",\n        exact_epsilon=str(epsilon), epsilon_is_a_fixed_source_parameter=True,\n        epsilon_depends_on_angle_mean_direction_or_outer_point=False,\n        accurate_law=\"C=epsilon*G(t/epsilon)/(1-epsilon); (t-epsilon/2)/(1-epsilon); 1-epsilon*G((1-t)/epsilon)/(1-epsilon)\",\n        exact_G_ascending_coefficients=[\"0\",\"0\",\"0\",\"0\",\"5/2\",\"-3\",\"1\"],\n        exact_velocity_S5_ascending_coefficients=[\"0\",\"0\",\"0\",\"10\",\"-15\",\"6\"],\n        exact_normalized_piece_edges=[str(v) for v in edges],\n        constant_extension_outside_unit_interval=True,\n        piecewise_polynomial_degree=[6,1,6],\n        matching_material_derivative_order=3,\n        fourth_material_derivative_continuity_claimed=False,\n        exact_cut_values_and_first_three_normalized_jets=[\n            [str(v) for v in boundary_cutoff_exact_jets(t)] for t in edges],\n        exact_first_derivative_peak=str(F(1)/(1-epsilon)),\n        exact_derivative_integral=\"1\", exact_value_integral=\"1/2\",\n        four_boundary_layers=layers, complete_physical_boundary_piece_count=12,\n        complete_new_internal_boundary_cut_count=8,\n        original_central_halfwave_profile_changed=False,\n        original_bubble_gamma_and_raw_defect_lift_changed=False,\n        working_arithmetic=\"binary64 evaluation of this complete exact-rational law\",\n        working_rounding_or_integration_error_enclosed=False)\n"
  },
  {
    "label": "append_fixed_cutoff_parameter",
    "expected_count": 1,
    "old": "    mean_armijo: float = 1.e-4\n",
    "new": "    mean_armijo: float = 1.e-4\n    boundary_cutoff_epsilon: str = BOUNDARY_CUTOFF_EPSILON\n"
  },
  {
    "label": "validate_fixed_rational_epsilon",
    "expected_count": 1,
    "old": "        boundary = exact_fraction(self.relative_boundary_total_length, \"boundary total length\")\n",
    "new": "        cutoff_epsilon = exact_fraction(self.boundary_cutoff_epsilon, \"boundary cutoff epsilon\")\n        if cutoff_epsilon != F(BOUNDARY_CUTOFF_EPSILON):\n            raise ValueError(\"This complete source fixes boundary cutoff epsilon=1/8\")\n        boundary = exact_fraction(self.relative_boundary_total_length, \"boundary total length\")\n"
  },
  {
    "label": "bind_complete_cutoff_definition",
    "expected_count": 1,
    "old": "        self.physical_profile_definition = paired_halfwave_definition(central, profile_delta)\n",
    "new": "        self.physical_profile_definition = paired_halfwave_definition(central, profile_delta)\n        self.boundary_cutoff_definition = boundary_cutoff_definition(support, central)\n        self.boundary_cutoff_epsilon = F(seed_parameters.boundary_cutoff_epsilon)\n        self.boundary_cutoff_breakpoints = tuple(F(v) for v in\n            self.boundary_cutoff_definition[\"exact_normalized_piece_edges\"])\n"
  },
  {
    "label": "working_definition_schema",
    "expected_count": 1,
    "old": "            schema=\"paired-halfwave-reference-working-definition-v1\",",
    "new": "            schema=\"paired-halfwave-flat-cutoff-reference-working-definition-v1\","
  },
  {
    "label": "working_rule_complete_cuts",
    "expected_count": 1,
    "old": "            radial_rule=\"all original exact-affine cells split at every support/boundary edge and all six physical halfwave pieces per central interval; positive Gauss on every outside and boundary piece\",",
    "new": "            radial_rule=\"all original exact-affine cells split at every support/boundary edge, both internal cuts in every R725 boundary layer and all six physical halfwave pieces per central interval; complete positive Gauss on every outside and boundary piece\",\n            physical_boundary_cutoff_definition=self.boundary_cutoff_definition,\n            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),\n            old_boundary_quadrature_mean_root_or_cache_inherited=False,\n            original_outer_whole_cell_Gauss_and_partial_rule_is_separate=True,"
  },
  {
    "label": "model_fixed_cutoff_identity",
    "expected_count": 1,
    "old": "            exact_profile_delta=str(profile_delta),\n",
    "new": "            exact_profile_delta=str(profile_delta),\n            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),\n            boundary_cutoff_definition=self.boundary_cutoff_definition,\n"
  },
  {
    "label": "model_boundary_law",
    "expected_count": 1,
    "old": "            boundary_cutoff=\"S5 from original T0 to d at each support end; first two endpoint jets zero\",",
    "new": "            boundary_cutoff=\"R725 fixed epsilon=1/8 three-piece C3 cutoff from original T0 to d at each support end; first three endpoint jets zero; two exact internal cuts per boundary layer\","
  },
  {
    "label": "working_left_boundary_only",
    "expected_count": 1,
    "old": "            return float(_S5(t)), float(_S5_prime(t)/self._width(a, b)), 0., 0.",
    "new": "            cutoff = boundary_cutoff_working_jets(t)\n            return cutoff[0], float(cutoff[1]/self._width(a, b)), 0., 0."
  },
  {
    "label": "working_right_boundary_only",
    "expected_count": 1,
    "old": "            return float(_S5(1.-t)), float(-_S5_prime(1.-t)/self._width(a, b)), 0., 0.",
    "new": "            cutoff = boundary_cutoff_working_jets(1.-t)\n            return cutoff[0], float(-cutoff[1]/self._width(a, b)), 0., 0."
  },
  {
    "label": "full_seed_mean_partition_includes_all_eight_new_cuts",
    "expected_count": 1,
    "old": "            cuts.update((ca+(cb-ca)*v, F(0)) for v in self.profile_breakpoints)\n",
    "new": "            cuts.update((ca+(cb-ca)*v, F(0)) for v in self.profile_breakpoints)\n            cuts.update((left+(ca-left)*v, F(0)) for v in self.boundary_cutoff_breakpoints)\n            cuts.update((cb+(right-cb)*v, F(0)) for v in self.boundary_cutoff_breakpoints)\n"
  },
  {
    "label": "record_actual_boundary_subpiece",
    "expected_count": 1,
    "old": "                width_carrier_hex=width.hex(), node_count=0)\n            if kind != \"central\":",
    "new": "                width_carrier_hex=width.hex(), node_count=0)\n            if kind in (\"left\", \"right\"):\n                layer = self.boundary_cutoff_definition[\"four_boundary_layers\"][\n                    2*region+(1 if kind == \"right\" else 0)]\n                layer_edges = [F(v) for v in layer[\"exact_relative_piece_edges\"]]\n                cutoff_piece = next((j for j in range(3)\n                    if self._compare(midpoint, (layer_edges[j+1], F(0))) < 0), None)\n                if (cutoff_piece is None\n                        or self._compare(left, (layer_edges[cutoff_piece], F(0))) < 0\n                        or self._compare(right, (layer_edges[cutoff_piece+1], F(0))) > 0):\n                    self._fail(\"boundary_cutoff_partition\", \"A boundary piece crosses an exact R725 internal cut\")\n                record.update(boundary_cutoff_piece_index=cutoff_piece,\n                    boundary_cutoff_branch=layer[\"branches_in_increasing_material_order\"][cutoff_piece],\n                    odd_material_derivative_orientation=layer[\"odd_material_derivative_orientation\"])\n            if kind != \"central\":"
  },
  {
    "label": "new_complete_radial_plan_schema",
    "expected_count": 1,
    "old": "        record = dict(schema=\"complete-paired-halfwave-seed-radial-plan-v1\",",
    "new": "        record = dict(schema=\"complete-paired-halfwave-flat-cutoff-seed-radial-plan-v1\","
  },
  {
    "label": "plan_complete_boundary_definition",
    "expected_count": 1,
    "old": "            paired_halfwave_definition=self.physical_profile_definition,\n            every_physical_halfwave_breakpoint_in_complete_partition=True,",
    "new": "            paired_halfwave_definition=self.physical_profile_definition,\n            boundary_cutoff_definition=self.boundary_cutoff_definition,\n            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),\n            every_internal_boundary_cut_in_complete_partition=True,\n            complete_physical_boundary_piece_count=12,\n            complete_internal_boundary_cut_count=8,\n            every_physical_halfwave_breakpoint_in_complete_partition=True,"
  }
]''')

def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def replace_exact(text, old, new, count, label):
    actual = text.count(old)
    if not old or actual != count:
        raise ValueError("Complete exact source patch count differs: "+label+
                         "; expected="+str(count)+"; actual="+str(actual))
    return text.replace(old, new)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-source", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    parent_path = args.parent_source.resolve()
    raw = parent_path.read_bytes()
    if len(raw) != PARENT_BYTES or digest(raw) != PARENT_SHA256:
        raise ValueError("Use every byte of the complete pinned paired-halfwave parent")
    text = raw.decode("utf-8")
    for patch in PATCHES:
        text = replace_exact(text, patch["old"], patch["new"],
                             patch["expected_count"], patch["label"])
    output = text.encode("utf-8")
    if len(output) != OUTPUT_BYTES or digest(output) != OUTPUT_SHA256:
        raise ValueError("The complete resulting source differs from its published identity")
    reversed_text = text
    for patch in reversed(PATCHES):
        reversed_text = replace_exact(reversed_text, patch["new"], patch["old"],
                                      patch["expected_count"], patch["label"]+" reverse")
    if reversed_text.encode("utf-8") != raw:
        raise ValueError("Complete inverse text construction did not recover the full parent")
    output_directory = args.output_directory.resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    destination = output_directory/OUTPUT_NAME
    if destination.resolve() == parent_path:
        raise ValueError("Preserve the complete original source at its original path")
    if destination.exists():
        if destination.read_bytes() != output:
            raise ValueError("Do not overwrite a different existing source")
    else:
        temporary = destination.with_name(destination.name+".partial")
        temporary.write_bytes(output)
        temporary.replace(destination)
    print(json.dumps(dict(
        schema="complete-r725-fixed-boundary-cutoff-seed-source-construction-v1",
        complete=True,
        parent=dict(path=str(parent_path), bytes=len(raw), sha256=digest(raw),
                    git_blob_sha=PARENT_GIT_BLOB_SHA),
        output=dict(path=str(destination), bytes=len(output), sha256=digest(output)),
        complete_exact_patch_count=len(PATCHES),
        complete_parent_recovered_by_inverse_text_patches=True,
        scientific_imports_or_calls=False,
        AST_or_compile_or_fixture_executed=False,
        extra_scientific_admission_stage_required=False), indent=2)+"\n")


if __name__ == "__main__":
    main()
