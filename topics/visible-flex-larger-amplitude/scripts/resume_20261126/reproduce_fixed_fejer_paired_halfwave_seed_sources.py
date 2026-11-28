#!/usr/bin/env python3
"""Reproduce four whole paired-halfwave sources from their complete fixed parents.

This program performs only UTF-8 source-byte operations. It does not import,
compile, parse or execute any scientific source, evaluate a field, or impose
a numerical admission step. Every complete output has its own final identity.
"""
import argparse
import hashlib
import json
from pathlib import Path

SPEC = json.loads(r'''{
  "schema": "complete-fixed-fejer-paired-halfwave-seed-four-source-construction-v1",
  "sources": [
    {
      "role": "seed",
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py",
        "name": "fixed_fejer_supported_meridian_reference.py",
        "bytes": 39771,
        "sha256": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
        "git_blob_sha": "ad7f2d9ea2e63df16d900cf12885d611fef5d823"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_reference.py",
        "name": "fixed_fejer_paired_halfwave_meridian_reference.py",
        "bytes": 43697,
        "sha256": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
        "git_blob_sha": "cc877246e546b8294826ad38d33b3eb2f7434f25"
      },
      "patches": [
        {
          "before": "The exact definition is R708/R709 with the independent R711 central profile: the original unit meridian outside two\nfixed supports, normalized boundary blends, and the twelve-piece smooth-triangle odd central\nprofile.  Three mean variables and one amplitude are determined at each",
          "after": "The exact definition retains the R708/R709 boundary mean and the R711 scalar\namplitude, with a positive halfwave on the first central interval and its\nnegative on the second equal central interval. The original unit meridian\noutside two fixed supports and every normalized boundary blend are retained.\nEach physical halfwave has six exact pieces; the auxiliary amplitude rule\nstill uses all twelve original R711 pieces. Three mean variables and one amplitude are determined at each",
          "count": 1
        },
        {
          "before": "SCHEMA = \"complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1\"",
          "after": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1\"",
          "count": 1
        },
        {
          "before": "Scientific supported-smooth-triangle reference evaluation requires public repository Actions",
          "after": "Scientific paired-halfwave reference evaluation requires public repository Actions",
          "count": 1
        },
        {
          "before": "        if any(not left < a < b < right\n               for (left, right), (a, b) in zip(support, central)):\n            raise ValueError(\"Every boundary layer and central interval must have positive exact length\")",
          "after": "        if any(not left < a < b < right\n               for (left, right), (a, b) in zip(support, central)):\n            raise ValueError(\"Every boundary layer and central interval must have positive exact length\")\n        if central[0][1]-central[0][0] != central[1][1]-central[1][0]:\n            raise ValueError(\"The two complete paired-halfwave central lengths must be exactly equal\")",
          "count": 1
        },
        {
          "before": "class SupportedUnitMeridianJet:\n",
          "after": "def paired_halfwave_definition(central, profile_delta):\n    \"\"\"Exact complete radial profile; no numerical mean or field evaluation.\"\"\"\n    central = tuple(tuple(F(v) for v in pair) for pair in central)\n    delta = F(profile_delta)\n    if (len(central) != 2 or any(len(pair) != 2 for pair in central)\n            or not F(0) < delta < F(1, 8)\n            or not F(0) < central[0][1]-central[0][0]\n            or central[0][1]-central[0][0] != central[1][1]-central[1][0]):\n        raise ValueError(\"The paired halfwaves require two complete equal positive central intervals\")\n    edges = (F(0), 2*delta, F(1,2)-2*delta, F(1,2),\n             F(1,2)+2*delta, F(1)-2*delta, F(1))\n    if any(a >= b for a, b in zip(edges, edges[1:])):\n        raise ValueError(\"Every one of the six exact halfwave pieces is required\")\n    return dict(schema=\"complete-equal-central-intervals-paired-halfwave-profile-v1\",\n        auxiliary_profile=\"the original complete R711 h_delta on [0,1]\",\n        auxiliary_mean_kernel_source_sha256=MEAN_KERNEL_SHA,\n        auxiliary_mean_rule_piece_count=12,\n        physical_central_interval_count=2, physical_piece_count_per_interval=6,\n        complete_physical_pair_piece_count=12,\n        exact_profile_delta=str(delta),\n        exact_normalized_piece_edges=[str(v) for v in edges],\n        exact_relative_central_intervals=[[str(v) for v in pair] for pair in central],\n        exact_relative_central_each_length=str(central[0][1]-central[0][0]),\n        exact_relative_physical_piece_edges=[\n            [str(a+(b-a)*v) for v in edges] for a,b in central],\n        signs_in_radial_discovery_order=[1,-1],\n        physical_profile=\"sign[index]*h_delta(t/2); t=(s-a)/(b-a)\",\n        radial_derivative_chain_factor=\"1/2\",\n        combined_cosine_mean=\"Lc*A_delta(lambda)*d\",\n        combined_transverse_mean=\"zero by equal complete central lengths and opposite signs\",\n        transverse_mean_zero_in_each_individual_interval=False,\n        old_per_interval_odd_physical_profile_inherited=False)\n\n\nclass SupportedUnitMeridianJet:\n",
          "count": 1
        },
        {
          "before": "        self.boundary, self.delta, self.profile_delta = boundary, delta, profile_delta\n",
          "after": "        self.boundary, self.delta, self.profile_delta = boundary, delta, profile_delta\n        self.physical_profile_definition = paired_halfwave_definition(central, profile_delta)\n        self.profile_breakpoints = tuple(F(v) for v in\n            self.physical_profile_definition[\"exact_normalized_piece_edges\"])\n",
          "count": 1
        },
        {
          "before": "schema=\"supported-smooth-triangle-reference-working-definition-v1\"",
          "after": "schema=\"paired-halfwave-reference-working-definition-v1\"",
          "count": 1
        },
        {
          "before": "radial_rule=\"all original exact-affine cells split at every support/boundary edge; positive Gauss on every outside and boundary piece\",",
          "after": "radial_rule=\"all original exact-affine cells split at every support/boundary edge and all six physical halfwave pieces per central interval; positive Gauss on every outside and boundary piece\",",
          "count": 1
        },
        {
          "before": "central_profile_rule=\"all twelve exact profile pieces, positive Gauss, no weight renormalization; odd transverse mean is a structural zero\",",
          "after": "central_profile_rule=\"the auxiliary A_delta and its two lambda derivatives retain all twelve original exact R711 pieces with positive Gauss and no weight renormalization; physical sine means cancel only across the two equal opposite halfwaves\",\n            physical_central_profile_definition=self.physical_profile_definition,\n            auxiliary_mean_metadata_describes_original_full_R711_rule=True,\n            physical_profile_is_not_the_auxiliary_full_period_on_each_interval=True,\n            actual_field_quadrature_or_closure_words_inherited_from_original_seed=False,",
          "count": 1
        },
        {
          "before": "mathematical_profile_piece_count=12,",
          "after": "mathematical_profile_piece_count=6,\n            mathematical_profile_piece_count_scope=\"one physical central interval\",\n            auxiliary_mean_profile_piece_count=12,\n            complete_physical_pair_piece_count=12,\n            paired_halfwave_definition=self.physical_profile_definition,",
          "count": 1
        },
        {
          "before": "accurate_definition=\"fixed original unit T0 outside U; N((1-chi)T0+chi*d) on boundary layers; cos(lambda*h)*d+sin(lambda*h)*w centrally\",",
          "after": "accurate_definition=\"fixed original unit T0 outside U; N((1-chi)T0+chi*d) on boundary layers; cos(lambda*h_delta(t/2))*d+sign[index]*sin(lambda*h_delta(t/2))*w on the two equal central intervals\",",
          "count": 1
        },
        {
          "before": "central_profile=\"R711 full C3 twelve-piece odd smooth-triangle h_delta; quarter primitive of S5-flat-S5 velocity\",",
          "after": "central_profile=\"paired opposite six-piece C3 halfwaves of the full R711 h_delta; first +h_delta(t/2), second -h_delta(t/2); all exact physical breakpoints retained\",",
          "count": 1
        },
        {
          "before": "        h, ht = _profile(np.array([t]), self.profile_delta, self.kernel)\n        return 1., 0., float(h[0]), float(ht[0]/self._width(a, b))",
          "after": "        h, ht = _profile(np.array([.5*t]), self.profile_delta, self.kernel)\n        sign = 1. if index == 0 else -1.\n        return 1., 0., float(sign*h[0]), float((.5*sign)*ht[0]/self._width(a, b))",
          "count": 1
        },
        {
          "before": "        for (left, right), (ca, cb) in zip(self.support, self.central):\n            cuts.update((v, F(0)) for v in (left, ca, cb, right))\n        ordered = sorted(cuts, key=cmp_to_key(self._compare))",
          "after": "        for (left, right), (ca, cb) in zip(self.support, self.central):\n            cuts.update((v, F(0)) for v in (left, ca, cb, right))\n            cuts.update((ca+(cb-ca)*v, F(0)) for v in self.profile_breakpoints)\n        ordered = sorted(cuts, key=cmp_to_key(self._compare))",
          "count": 1
        },
        {
          "before": "record = dict(schema=\"complete-supported-smooth-triangle-seed-radial-plan-v1\",",
          "after": "record = dict(schema=\"complete-paired-halfwave-seed-radial-plan-v1\",",
          "count": 1
        },
        {
          "before": "            central_profile_integral_is_separate=True,\n",
          "after": "            central_profile_integral_is_separate=True,\n            paired_halfwave_definition=self.physical_profile_definition,\n            every_physical_halfwave_breakpoint_in_complete_partition=True,\n            complete_physical_pair_piece_count=12,\n            auxiliary_mean_rule_piece_count=12,\n            physical_sine_cancellation_scope=\"both equal complete central intervals together\",\n",
          "count": 1
        }
      ]
    },
    {
      "role": "base",
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py",
        "name": "fixed_fejer_supported_so3_meridian_operator.py",
        "bytes": 40840,
        "sha256": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
        "git_blob_sha": "1d9e435bb68374b71c3d7361771c28f47838d59e"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_operator.py",
        "name": "fixed_fejer_paired_halfwave_meridian_operator.py",
        "bytes": 40803,
        "sha256": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
        "git_blob_sha": "350c2e057e6af15e663d0fdb463a518bebc36234"
      },
      "patches": [
        {
          "before": "complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",
          "after": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "before": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
          "after": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "count": 1
        },
        {
          "before": "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",
          "after": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
          "count": 1
        },
        {
          "before": "T0 is the explicitly bound supported-smooth-triangle seed, frozen from that",
          "after": "T0 is the explicitly bound paired-halfwave seed, frozen from that",
          "count": 1
        },
        {
          "before": "Bind the complete fixed supported-smooth-triangle world-meridian reference kernel",
          "after": "Bind the complete fixed paired-halfwave world-meridian reference kernel",
          "count": 1
        },
        {
          "before": "This entry uses a complete explicitly bound fixed supported-smooth-triangle seed",
          "after": "This entry uses a complete explicitly bound fixed paired-halfwave seed",
          "count": 1
        },
        {
          "before": "T0='complete fixed supported-smooth-triangle seed from original reference core/H; full complement, normalized boundary layers and odd central profile',",
          "after": "T0='complete fixed paired-halfwave seed from original reference core/H; full complement, normalized boundary layers and equal opposite six-piece central halfwaves',",
          "count": 1
        }
      ]
    },
    {
      "role": "Q",
      "parent": {
        "name": "fixed_fejer_literal_zero_moment_input.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_literal_zero_moment_input.py",
        "bytes": 31409,
        "sha256": "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",
        "git_blob_sha": "172d2b82eca6496058d2c73560de86bada50f12d"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "name": "fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "bytes": 34886,
        "sha256": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
        "git_blob_sha": "4625d2775b960a8859ddd88de215cc736a84363f"
      },
      "patches": [
        {
          "before": "SCHEMA = 'fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1'",
          "after": "SCHEMA = 'fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1'",
          "count": 1
        },
        {
          "before": "DEFINITION_SCHEMA = 'fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1'",
          "after": "DEFINITION_SCHEMA = 'fixed-fejer-paired-halfwave-reference-literal-two-bubble-endpoint-Q-v1'",
          "count": 1
        },
        {
          "before": "BASE_SCHEMA = 'complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1'",
          "after": "BASE_SCHEMA = 'complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1'",
          "count": 1
        },
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "SEED_SCHEMA = 'complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1'",
          "after": "SEED_SCHEMA = 'complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1'",
          "count": 1
        },
        {
          "before": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
          "after": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "count": 1
        },
        {
          "before": "\"\"\"Bind eighteen fixed Q words to one complete supported-smooth-triangle reference seed.",
          "after": "\"\"\"Bind eighteen fixed Q words to one complete paired-halfwave reference seed.",
          "count": 1
        },
        {
          "before": "fixed supported-smooth-triangle provider.",
          "after": "fixed paired-halfwave provider.",
          "count": 1
        },
        {
          "before": "def _supported_seed(seed_model, *, reference, reference_id,",
          "after": "def _paired_halfwave_definition(central, profile_delta):\n    \"\"\"Exact complete radial profile; no numerical mean or field evaluation.\"\"\"\n    central = tuple(tuple(Fraction(v) for v in pair) for pair in central)\n    delta = Fraction(profile_delta)\n    if (len(central) != 2 or any(len(pair) != 2 for pair in central)\n            or not Fraction(0) < delta < Fraction(1, 8)\n            or not Fraction(0) < central[0][1]-central[0][0]\n            or central[0][1]-central[0][0] != central[1][1]-central[1][0]):\n        raise ValueError(\"The paired halfwaves require two complete equal positive central intervals\")\n    edges = (Fraction(0), 2*delta, Fraction(1,2)-2*delta, Fraction(1,2),\n             Fraction(1,2)+2*delta, Fraction(1)-2*delta, Fraction(1))\n    if any(a >= b for a, b in zip(edges, edges[1:])):\n        raise ValueError(\"Every one of the six exact halfwave pieces is required\")\n    return dict(schema=\"complete-equal-central-intervals-paired-halfwave-profile-v1\",\n        auxiliary_profile=\"the original complete R711 h_delta on [0,1]\",\n        auxiliary_mean_kernel_source_sha256=SEED_MEAN_KERNEL_SOURCE_SHA,\n        auxiliary_mean_rule_piece_count=12,\n        physical_central_interval_count=2, physical_piece_count_per_interval=6,\n        complete_physical_pair_piece_count=12,\n        exact_profile_delta=str(delta),\n        exact_normalized_piece_edges=[str(v) for v in edges],\n        exact_relative_central_intervals=[[str(v) for v in pair] for pair in central],\n        exact_relative_central_each_length=str(central[0][1]-central[0][0]),\n        exact_relative_physical_piece_edges=[\n            [str(a+(b-a)*v) for v in edges] for a,b in central],\n        signs_in_radial_discovery_order=[1,-1],\n        physical_profile=\"sign[index]*h_delta(t/2); t=(s-a)/(b-a)\",\n        radial_derivative_chain_factor=\"1/2\",\n        combined_cosine_mean=\"Lc*A_delta(lambda)*d\",\n        combined_transverse_mean=\"zero by equal complete central lengths and opposite signs\",\n        transverse_mean_zero_in_each_individual_interval=False,\n        old_per_interval_odd_physical_profile_inherited=False)\n\n\ndef _supported_seed(seed_model, *, reference, reference_id,",
          "count": 1
        },
        {
          "before": "    _positive_exact_fraction(seed.get('exact_relative_boundary_total_length'),\n        'fixed seed boundary total length')\n    profile_delta = _positive_exact_fraction(seed.get('exact_profile_delta'), 'fixed seed smooth-triangle profile delta')\n    if (profile_delta >= Fraction(1, 8)\n            or seed.get('mathematical_profile_piece_count') != 12\n            or seed.get('mathematical_amplitude_interval') != '(0,pi)'\n            or seed.get('old_five_piece_working_cache_or_geometry_inherited') is not False):\n        raise ValueError('Bind the full independent R711 profile and its declared amplitude interval')\n    working = seed.get('working_definition')\n    if not isinstance(working, dict):\n        raise ValueError('Retain the complete actual fixed seed numerical rule definition')",
          "after": "    boundary = _positive_exact_fraction(seed.get('exact_relative_boundary_total_length'),\n        'fixed seed boundary total length')\n    support = tuple(tuple(Fraction(v) for v in pair) for pair in expected_support)\n    if boundary >= 2*min(b-a for a,b in support):\n        raise ValueError('Keep positive boundary layers and both complete central intervals')\n    end_width = boundary/4\n    central = tuple((a+end_width,b-end_width) for a,b in support)\n    profile_delta = _positive_exact_fraction(seed.get('exact_profile_delta'), 'fixed seed smooth-triangle profile delta')\n    paired = _paired_halfwave_definition(central, profile_delta)\n    if (profile_delta >= Fraction(1, 8)\n            or seed.get('mathematical_profile_piece_count') != 6\n            or seed.get('mathematical_profile_piece_count_scope') != 'one physical central interval'\n            or seed.get('auxiliary_mean_profile_piece_count') != 12\n            or seed.get('complete_physical_pair_piece_count') != 12\n            or seed.get('paired_halfwave_definition') != paired\n            or seed.get('exact_relative_central_intervals') != paired['exact_relative_central_intervals']\n            or seed.get('exact_relative_boundary_each_end_length') != str(end_width)\n            or seed.get('mathematical_amplitude_interval') != '(0,pi)'\n            or seed.get('old_five_piece_working_cache_or_geometry_inherited') is not False):\n        raise ValueError('Bind both complete opposite halfwaves and the original full R711 amplitude rule')\n    working = seed.get('working_definition')\n    if (not isinstance(working, dict)\n            or working.get('schema') != 'paired-halfwave-reference-working-definition-v1'\n            or working.get('physical_central_profile_definition') != paired\n            or working.get('auxiliary_mean_metadata_describes_original_full_R711_rule') is not True\n            or working.get('physical_profile_is_not_the_auxiliary_full_period_on_each_interval') is not True\n            or working.get('actual_field_quadrature_or_closure_words_inherited_from_original_seed') is not False):\n        raise ValueError('Retain the complete paired physical profile and distinct auxiliary mean rule')",
          "count": 1
        }
      ]
    },
    {
      "role": "calibration",
      "parent": {
        "name": "fixed_fejer_meridian_reference_calibration.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_reference_calibration.py",
        "bytes": 11872,
        "sha256": "aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3",
        "git_blob_sha": "2f816e1e3e617a1c8bf85bea8067f5aedd8e773e"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_reference_calibration.py",
        "name": "fixed_fejer_paired_halfwave_reference_calibration.py",
        "bytes": 11872,
        "sha256": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
        "git_blob_sha": "812e981a9e4a6302c6241129dd812c251bb92691"
      },
      "patches": [
        {
          "before": "\"\"\"Complete frozen-reference numerical calibration for the R715 R711 field.",
          "after": "\"\"\"Complete frozen-reference calibration for the R715 paired-halfwave field.",
          "count": 1
        },
        {
          "before": "ENDPOINT_SCHEMA = 'complete-fixed-fejer-detached-meridian-values-normal-layer-v1'",
          "after": "ENDPOINT_SCHEMA = 'complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1'",
          "count": 1
        },
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "BASE_SCHEMA = 'complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1'",
          "after": "BASE_SCHEMA = 'complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1'",
          "count": 1
        },
        {
          "before": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
          "after": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "count": 1
        }
      ]
    }
  ]
}''')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_parent(repo, record):
    path = repo/record["path"]
    data = path.read_bytes()
    if len(data) != record["bytes"] or digest(data) != record["sha256"]:
        raise ValueError("The complete declared parent source changed: "+str(path))
    return data.decode("utf-8")


def construct(text, item):
    old = text
    for patch in item["patches"]:
        if text.count(patch["before"]) != patch["count"]:
            raise ValueError("An exact complete source replacement has the wrong multiplicity")
        text = text.replace(patch["before"], patch["after"])
    data = text.encode("utf-8")
    record = item["output"]
    if len(data) != record["bytes"] or digest(data) != record["sha256"]:
        raise ValueError("A complete paired-halfwave source has the wrong identity")
    restored = text
    for patch in reversed(item["patches"]):
        if restored.count(patch["after"]) != patch["count"]:
            raise ValueError("An exact reverse source replacement has the wrong multiplicity")
        restored = restored.replace(patch["after"], patch["before"])
    if restored != old:
        raise ValueError("The complete original source cannot be restored byte for byte")
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--output-directory", type=Path, required=True)
    args = p.parse_args()
    outputs = [(item, construct(read_parent(args.repo, item["parent"]), item))
               for item in SPEC["sources"]]
    args.output_directory.mkdir(parents=True, exist_ok=True)
    records = []
    for item, data in outputs:
        path = args.output_directory/item["output"]["name"]
        if path.exists():
            raise FileExistsError("Preserve an already written complete source: "+str(path))
        path.write_bytes(data)
        records.append(dict(role=item["role"], path=str(path.resolve()),
                            bytes=len(data), sha256=digest(data)))
    print(json.dumps(dict(schema=SPEC["schema"], complete_sources=records,
        all_complete_parent_bytes_used=True, complete_inverse_source_replacements=True,
        numerical_or_AST_or_compile_evaluation_performed=False), indent=2))


if __name__ == "__main__":
    main()
