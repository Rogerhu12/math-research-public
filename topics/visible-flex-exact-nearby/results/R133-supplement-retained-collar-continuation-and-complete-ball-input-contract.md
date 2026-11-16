# WPTVS. Exact retained-collar continuation and complete printed-ball input contract

## 1. Scope and immutable failure boundary

This note authorizes one remaining-body calculation for the same WPTV/WPTVR positive-head operator. It changes neither the admitted original family nor the physical head, mean, affine, outer-chart, and finite-Schur obligations. It gives no tail inverse and no finite signed inverse.

The original scientific attempt is run **43854566735/1**. Its complete scientific conclusion is

- `notes/frozen_cross_block_value_tail_ci/run-43854566735-1/actual-scientific-conclusion.json`,
  Git `e5721a0ecea7c3131401a8caa94839ad10e2e315`, 15,309 bytes,
  SHA256 `b8812b6b940b17532c7643555d3393da71c2190606082862ccf651fbff762274`;
- its complete execution is Git `fe4c3e274701d9237736809e7dd12b801ce8c79c`, 31,256 bytes,
  SHA256 `e7246476bc02fe196ec10186783bcda8892621ec1c105d4b99dc612647cd3eca`;
- the original current-input manifest is
  `notes/2026-11-16-R133-frozen-cross-block-current-inputs.json`,
  Git `c1228b9d5984a0a2d11de37b6dcd6e6eebbb5801`, 45,380 bytes,
  SHA256 `9b52fa3ceafb51d65d946bcdfbd58ce323f1fc9aa8b72432452b3729c975c3b4`.

The execution has one scientific child, return code 1, a complete successful readonly preflight, and zero old targets recomputed. All 24 original current-file receipts, 10 AST receipts, and 19 temporary-restoration receipts remain part of that original execution. The restoration object is exactly 13,771 bytes, SHA256 `4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac`.

The saved scientific prefix contains all 32 fields and all 11 completed gates. Its first whole-maxima target has started but has not finished. Parent 0, the original collar, is complete. Parent 1 is only marked `started`; it has no saved reference identity and there are zero completed body intersections. There are no completed whole targets, refinement comparisons, or resolvents.

The original reference chain is exactly

```json
{"count":1,"sha256":"947c13032e6e6dc6496e42d2a78b0178b41dbc4372069a321f3f501a07547df7"}
```

Its two nonzero running maxima remain the following complete original literals:

```text
A = [0.00142748996910073817525289994830054185572968290322097013280439797965555221499 +/- 2.15e-78]
L = [0.0383159795915786712631499980503846916080928356572902243927854214797407920020 +/- 3.14e-77]
E_b = 0
U_b = 0
B = 0
```

Their original witnesses, every progress counter, the interrupted-parent descriptor, and the complete original failure and runtime are retained verbatim. The full failed file and all its per-field canonical hashes remain pinned. This is stronger than a summary asserting that the collar once passed.

The old consumed marker is not removed or reused. The only new problem is `WPTV_remaining_body_after_43854566735_v1`. Its mathematical continuation starts at parent 1 and ends at parent 152. The original manifest remains at its old path and identity.

## 2. Exact cause established by the saved boundary

The original failure message is `original finite display centre`. The old scientific function stripped an opening bracket and then split only on the substring `" +/- "`. Consequently it did not implement the original producer's complete finite printed-ball grammar: a zero-centred form `[+/- radius]` and a bracketed exact form `[number]` were not accepted correctly.

The saved failure does not identify which of the four intrinsic records caused the rejection, or the precise offending text. This note does not invent that missing diagnostic. The boundary proves that no body reference bound or complete body intersection had been saved. The parser is corrected by its complete type contract, rather than by assuming a particular unseen numeric value.

The original coefficient producer
`scripts/fourfold_codazzi_current_positive_complete_coefficients.py`
(Git `45ce0d7171ad35aa3175ea03fdac22f5158fa855`, 21,756 bytes,
SHA256 `1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c`)
imports `record` from `fourfold_phase_metric_defect`. That helper
(Git `cc1c1e0b271e69e7415712c5bb82678c94c3e5f8`, 13,046 bytes,
SHA256 `c4196dddcbfab15116c06a9be8a2120916c05d77fe3d7cb152f842f16b80a7de`)
returns `ball_record(arb(value))`. The defining
`fourfold_phase_beta_interval.ball_record`
(Git `6a0713f931680adfd04e87949087189aa1d75e02`, 30,343 bytes,
SHA256 `ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f`)
saves exactly

```python
{"ball": value.str(digits),
 "lower": value.lower().str(digits),
 "upper": value.upper().str(digits),
 "mid_float": float(value.mid()),
 "radius_upper_float": float(value.rad().upper())}
```

with default `digits=35`. The last two fields are display metadata. They are preserved and checked for finite JSON numeric type, but are never used as mathematical bounds or reference values.

The original other three row groups still use their exact three-field records. The already-corrected admission keeps the exact group key sets: intrinsic 7; repaired bounds 21; full-delta bounds 21; full-delta fees 10. No unknown field or non-ball metadata is silently skipped.

## 3. Complete finite display grammar and original interval semantics

Let $\mathrm{DEC}$ denote the finite ASCII token

```text
[+-]?(digits("."digits*)? | "."digits+)([eE][+-]?digits+)?
```

The readonly parser accepts precisely a bare DEC, $[{\rm DEC}]$, $[{\rm DEC}\ +/-\ {\rm DEC}]$, or $[+/-\ {\rm DEC}]$, with optional surrounding spaces. A printed radius must be finite and nonnegative. The last form has the exact reference centre zero. It rejects nonfinite tokens, condensed output, incomplete brackets, extra radius separators, and a common exponent outside the closing bracket.

These rules agree with the default finite printing branch of FLINT `arb_get_str` and the uncondensed `python-flint 0.9.0` string interface. The bracket-exact form is also a legal original `arb_set_str` input. In this calculation the original records already have an ASCII qualification; Unicode display conversion is not introduced.

For source audit, the official default-printing implementation is
`flint/v3.3.1/src/arb/get_str.c`,
Git `4e6f92753986478f76d4c478f92b30249f720c54`, 12,409 bytes,
SHA256 `61a3e820e061b3ba6d678709d053660dc7ef384b703563bf840240a3ed1d1915`.
The Python wrapper is `python-flint/0.9.0/src/flint/types/arb.pyx`,
Git `56b9ba07e5a37e63902498a4c7361023b09f82fd`, 88,632 bytes,
SHA256 `eb8f165e638756ffc19f2a7e72a478edc71e53ea866345f4cfcad05cb154882d`.
These source reads are format evidence, not numerical evaluations.

A second correction restores the original native consumer's exact interval convention. In the fully read original
`scripts/fourfold_codazzi_repaired_positive_high_Volterra.py`
(Git `538ca4f6c9f25f669daf2ce1a175fd0bfbacb40a`, 21,932 bytes,
SHA256 `8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d`),
the consumer is

```python
def interval(value):
    return arb(value["lower"]).lower().union(arb(value["upper"]).upper())
```

The actual full-delta body producer
`scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py`
(Git `f4dd9ad8b324e39fed478183b88095c949d5c09a`, 19,660 bytes,
SHA256 `0df3ae7181d5ac8808928e9b0ed4bcf225fa3f80ae5df944b2a96a5e4d3ae117`)
imports that same function as `interval=base.interval`.

Accordingly, for a complete original three- or five-field record $r$, the continuation uses

$$
\mathcal I(r)=
\operatorname{hull}\!\left(
 \operatorname{lower}(\operatorname{arb}(r_{\rm lower})),
 \operatorname{upper}(\operatorname{arb}(r_{\rm upper}))
\right).
\tag{WPTVS.1}
$$

Both endpoints must be finite and ordered. Their full original text remains unchanged. Equation (WPTVS.1) is the original saved enclosure read with its two directed endpoints; it neither recomputes the original coefficient nor subtracts an upper bound. A saved new one-field $\{\texttt{ball}\}$ record keeps its former parsing and upper-endpoint read unchanged.

The completed collar used only its original rational collar constants and the saved new one-field $\pi$ record. It did not invoke this native three-/five-field interval path or any body reference. Therefore both corrections leave its complete saved qualification unchanged.

## 4. Signed reference selection does not change the actual operator

The actual body interval must first satisfy

$$
\inf\mathcal I(K)>0,\qquad
\inf\mathcal I(\gamma)>0,\qquad
\sup\mathcal I(C_{\rm ref})<0.
\tag{WPTVS.2}
$$

Failure of (WPTVS.2) stops this new calculation with its complete prefix. It is not repaired by changing the actual family.

For a reference only, the printed centre of $\beta$ is retained. For each of $K,\gamma,C_{\rm ref}$, the first rational value having the required strict sign is selected from the fixed list:

1. the parsed centre of the original `ball`;
2. the mean of the parsed centres of its two endpoint displays;
3. the lower-display centre;
4. the upper-display centre;
5. the fixed signed reference $K^0=1/64,\ \gamma^0=1,\ C_{\rm ref}^0=-1$, respectively.

The exact selected values and their selection labels are saved in the current reference identity. The original printed centres are saved separately. The identity explicitly states that these are reference values, not certified actual point values.

The same exact degree-32 candidate polynomial, physical amplitude, and midpoint are used. The reference repair is zero; the complete actual repair enclosure remains in the actual coefficient. The original strictly positive rational $q_i$ floor and dyadic selection remain unchanged. Thus the fixed cell symmetrizer $S_i$ is invertible, and the reference principal block is self-adjoint after the same scaling. WPT's principal inverse proof needs self-adjointness, not equality of the reference parameters to actual point values.

For the complete cross block, the algebra remains the ordered identity

$$
a I b-a^0 I b^0
  =(a-a^0)I b+a^0 I(b-b^0).
\tag{WPTVS.3}
$$

The local coefficient and drift differences are also formed as complete signed interval differences. The full repaired centre-to-reference difference is followed by the original full degree-96 delta fee. The actual intrinsic principal difference, all reaction and primitive terms, the physical mean rank in the low block, the true 193-component input, and the complete $C_A,C_B,C_{LH,1}$ factors remain those of the already-reviewed WPTV calculation.

No old upper is subtracted. Changing an arbitrary reference changes both the reference block and its explicitly charged full difference. It therefore leaves the true operator and the validity of each complete candidate unchanged. It may make a sufficient bound worse; it promises no successful tail gate.

## 5. Precisely permitted continuation

The new readonly admission reads the full three prior files in §1 and verifies:

- all 32 original scientific fields by individual canonical hashes and the complete raw file identity;
- the full original execution, original 24 receipts, all 10 AST receipts, the 19-restoration object, the successful complete preflight, and source/manifest/checkout bindings;
- all old success and failure qualifications, the original scope and complete candidate/repair dictionaries;
- the five saved maxima and witnesses, chain count 1, completed-parent count 1, zero body intersections, and the interrupted body-parent descriptor without a reference;
- the unchanged 153-parent mesh and the fixed refinements $m=1,2$, giving 153 and 306 cells.

The new manifest has 27 current text files: the former 24 roles with the two corrected source versions, plus the complete prior scientific conclusion, execution, and manifest. The historical list remains the same 19 objects. No old binary is obtained through a chat connector; the identical objects are restored temporarily by the same public Actions worker. The original 4,650 rows in each order and all 3,594 interfaces are admitted before new science.

The new scientific document begins as a deep copy of the complete failed document. It adds one `continuation` field containing the exact prior identities, all 32 field hashes, original failure/runtime, the complete saved prefix, and the no-recomputation restrictions. The new source, manifest, checkout, current admission, and runtime are then bound to the new attempt. The old values remain available through that complete continuation object and their immutable full-file pins.

There is no second call to start the first whole-maxima target. The original count of one started, unfinished target is retained. The body loop is exactly

```python
for parent_index in range(1, 153):
    # every selected cell is body; no collar branch exists
```

The five initial running maxima are read from the saved records. Their witnesses are copied. The original reference chain is the chain input. The old collar bound is not evaluated again.

For each new body parent, the source first saves its started descriptor. After forming the new exact reference it saves the complete bounded identity. It consumes every intersecting original row, forms the same five complete parent candidates, and only after the entire parent is covered saves the five running maxima, all their witnesses, the chain update, the full cumulative counters, and the completed-parent descriptor. That complete prefix is atomically persisted and printed before any next parent. Downstream bounds are read back from that persisted document.

A later exception preserves the whole latest completed prefix and the incomplete current-parent descriptor. It does not authorize an automatic restart. A further continuation would require a separately stated remaining-work contract.

## 6. Whole targets, gate semantics, and output limits

After all 152 remaining body parents are complete, the cumulative count is 153. All 4,650 original body rows must have appeared in the complete cover. Only then are the five whole maxima finalized for the first time. The original WPTVR formulas are unchanged:

$$
Q_m=
\sqrt{(C_cE_c)^2+
       \bigl[C_b(E_b+U_b/m)\bigr]^2},
\qquad
\delta_m=
A/m+LQ_m/m+B/m^2,\qquad m\in\{1,2\}.
\tag{WPTVS.4}
$$

Both whole candidates are saved separately. The first passing predeclared mesh is selected, coarse first. A resolvent bound is computed only after its actual saved strict comparison $\delta_m<1$. A false comparison is a complete valid outcome, not an operational failure and not a proof of singularity.

The completed suffix document has 33 root fields and 18 structural gates: the original 11 gates retained verbatim, one new preserved-prefix admission gate, and the original six remaining gates. There are still four complete targets when neither mesh passes, or five when a conditional resolvent is actually admissible. The scalar count is 11 or 12; the original incomplete whole-maxima target is being finished, not recomputed. No finite matrix is allocated and no new array is published.

A pure JSON structural model includes the actual complete candidate/repair metadata and the entire 6,376-byte continuation object. It gives 30,314 bytes for a complete passing branch, 29,478 for two false comparisons, and a deliberately dominating 45,435-byte partial model. The latter superposes all completed branches, an 8,192-byte reference identity, every maximum witness, all gate names, and the maximum fully escaped diagnostic even though no legal ordered prefix contains all those branches simultaneously.

The scientific cap is therefore 50,000 bytes. Full output is saved and printed before a byte-limit error can be raised. The 80,000-byte execution cap and 8,000-byte report cap give a 138,000-byte publication budget; the separate pre-science reserve remains 120,000 bytes. These are static storage models, not computed scientific bounds.

The unchanged worker has dynamic kind, fieldset, gate, target-count, and current-input contracts. It can use the new problem-specific marker and output directory without modifying the old worker or old marker. It must retain the complete preflight stderr if readonly admission fails. Every previously completed scientific target remains frozen.

## 7. Scientific scope left open

This continuation pays only the remaining original WPTV whole-tail candidates. All genuine finite signed Schur blocks, both full right-hand sides, physical root-96 normalization, radial-head compatibility, independent means, $\nu$, $\Theta$, outer functions, affine sources, and cokernel obligations remain.

Until an actual new strict tail gate has passed, the WDS finite-Schur residual certificate cannot use a tail inverse. Even a successful tail gate would not by itself prove the finite signed inverse.
