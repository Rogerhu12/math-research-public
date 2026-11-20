# R994 — Certified original combined difference sets through 200000

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: the one bounded R993 execution is complete and accepted.** All 4008 newly requested original coefficients are nonzero. No old mathematical window was rerun. This is a finite result; the all-prime unit assertion, the original same-label criterion, and Serre uniformity remain open.

## 1. Public execution and actual termination

- Public run: [44760218207](https://github.com/Rogerhu12/math-research-public/actions/runs/44760218207).
- Public job: [136370438703](https://github.com/Rogerhu12/math-research-public/actions/runs/44760218207/job/136370438703), `exact_research`.
- Exact source commit: `248592d7fabd01b1b8c548237400767e9ecec001`.
- Run created at `2026-11-20T15:08:07Z`; successful terminal run metadata at `2026-11-20T15:17:09Z`.
- All job steps succeeded. The wrapper emitted `END_COMPUTATION` with name `original-balanced-combined-disjoint-window` and exit code `0`.
- The final budget receipt records **531.337922156 seconds**, `within_total_budget=true`, and `successful_contract_termination=true`. It is separate from the mathematical summary and was checked separately.

The method fixed a 620-second total budget, including source validation, the sieve, output, and scratch writing, with 15 seconds reserved for parent finalization. The mathematical summary has status `complete_nonzero_difference_sets`; no error, provisional zero, verified zero, or unverified zero occurred. The successful run and job, exit zero, complete summary, and final budget receipt all agree.

## 2. Exact new sets, with all old coverage excluded

Both rows require prime `p` with `p mod 9` in `{2,5}`. The row modulo twelve and lower endpoint are part of the original contract. The union was processed in strictly increasing prime order.

| Original row | New interval | Additional condition | Requested and completed | First two new primes | Last new prime | Zero values | Uncompleted |
|---|---|---|---:|---|---:|---:|---:|
| r=8 | 20000 < p ≤ 200000 | p mod 12 = 5 | 2622 | 20021, 20117 | 199877 | 0 | 0 |
| r=2 | 100000 < p ≤ 200000 | p mod 12 = 11 | 1386 | 100019, 100103 | 199967 | 0 | 0 |

R991 already completed the original row-eight interval through 20000; R963 already completed the original row-two interval through 100000. These and all earlier small-prime sources lie below the respective new lower endpoints. The contract records `old_primes_recomputed=[]`. The requested lists are disjoint, and the completed rows equal their entire increasing merged union, rather than merely matching a count.

The exact increasing requested list and completed list have the same canonical SHA256:

`f6dd903ee19ca46af465345cb4e0b752218b07edb1ae98dc40b8109241e75eeb`.

## 3. What each public row certifies

The main channel is the original R990 coefficient formula on the original plus model. For the actual row `r`, let `n=p-r`, `m=n/3`, and `k=floor(p/12)`. It forms the actual Jacobi polynomial `B`, the series `H=((1-z)B²)^−1`, the finite period quotient with coefficients `f_i=H_i/(1-3i)`, and `Q=4+12zB′/B-z/(1-z)`. It records

\[
J_{p,r}=[z^m]Qf^{-r},\qquad c_{p-r}^{+}=\frac{(-32)^m(r-1)!}{4}J_{p,r}.
\]

Every one of the 4008 rows records the original-model value, the opposite-model phase `c_minus=-c_plus`, the exact coefficient and scale, hashes of its finite polynomial inputs, and a successful first-resonance check `H_ell=B(1)^−2` at `ell=(p+1)/3`. The first-resonance unit is a source check; it is not used as a proof that the target coefficient is a unit.

All 4008 `c_plus` and `c_minus` entries are nonzero, and all recorded first-resonance checks passed. No individual prime beyond the four scheduled checks is claimed to have been evaluated by all three algorithms.

## 4. Independent original-source calibration

The exact first two new primes of each row received three source computations: the fixed-r hypergeometric main channel; the original Ramanujan/Chazy recurrence with the proved square-CDQ summation; and the original minus-model sigma single-carry contraction. The latter uses the fast independent Weierstrass recurrence and verifies its **entire defining ODE residual**, the sigma exponential differential identity, and the inverse identity. The sigma phase is exactly `g2=0,g3=4; sigma=z-z^7/210+...; no Gaussian`.

| p | r | n | J_(p,r) | Main scale | c_plus, all three channels | c_minus |
|---:|---:|---:|---:|---:|---:|---:|
| 20021 | 8 | 20013 | 12197 | 5571 | 18234 | 1787 |
| 20117 | 8 | 20109 | 17328 | 14163 | 9181 | 10936 |
| 100019 | 2 | 100017 | 53155 | 37011 | 45994 | 54025 |
| 100103 | 2 | 100101 | 81822 | 80559 | 16257 | 83846 |

The independent recurrences retain their own actual indices and normalization:

| p | Chazy M | a_M | Chazy scale | Sigma N | Sigma t | Original B | Low terms | Single-carry terms |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20021 | 6670 | 11770 | 420 | 3336 | 3335 | 2871 | 3337 | 3335 |
| 20117 | 6702 | 3231 | 420 | 3352 | 3351 | 13997 | 3353 | 3351 |
| 100019 | 33338 | 51833 | 8335 | 16669 | 16669 | 16684 | 16670 | 16670 |
| 100103 | 33366 | 94981 | 8342 | 16683 | 16683 | 8085 | 16684 | 16684 |

All four rows have `all_three_original_sources_agree=true`, `complete_original_wp_ODE_verified=true`, and `original_sigma_exponential_and_inverse_verified=true`. The four independently checked primes are exactly `[20021,20117,100019,100103]`, both in the contract and in the final summary. No zero was encountered, so the separately specified first-zero branch was not entered.

For an endpoint check on the received records, the last row-eight record is `p=199877, n=199869, J=196202, scale=146330, c_plus=106257, c_minus=93620`; the last row-two record is `p=199967, n=199965, J=138825, scale=137, c_plus=22160, c_minus=177807`. These are received public outputs, not local recomputations.

## 5. Complete chunk reconstruction and canonical receipts

The actual contract occupied eight physical chunk envelopes and the summary seven. Root required every zero-based index exactly once, consistent event metadata, and exact ASCII reconstruction. It checked the reconstructed byte length and SHA256 **before** decoding the original event. Neither a chunk envelope nor a truncated log line was accepted as a summary.

Canonical JSON is Python `json.dumps(value,sort_keys=True,separators=(",",":"))` with the original parsed numeric types. The complete payload is the object `{contract,rows,summary}` followed by one newline; the other objects below have no trailing newline.

| Object | Bytes | SHA256 |
|---|---:|---|
| contract | 29251 | `8e8b1a3bad495bd85989c716bfe37d2030ebf55bf28c26de2cbfa9d2a4ab23f3` |
| rows | 2808402 | `11a86f90fc1c0a9876efb602d8a3ac39d185d2854d10e8ac97ef43ddfe86182e` |
| summary | 27881 | `e5ee2a5ac073ccfee8f0619f9a9687cd064e1f69679d4663d9bea0ce630b3b12` |
| Payload plus newline | 2865567 | `e764dff838bb24b18c8fec7f7634c2044f403e59e23a349cc00d0554c000dc8d` |

The received full decoded log is 3006404 UTF-8 bytes with SHA256 `83344535ef1aa70775afe899a9dd0466ce9fcba0dcc3f29d908556a64b8f639a`. After reconstructing the two chunked events there are one contract, 4008 prime rows, one summary, one output receipt, and one final budget receipt. The complete payload was reconstructed in scratch and matched the public output receipt byte for byte.

Root verification was restricted to IO, schemas, equality of the requested/completed lists and source-check values, source hashes, chunk hashes, and public execution status. It did not run the sieve, recompute finite-field coefficients, rerun an old window, or execute any new mathematics locally.

## 6. Frozen sources

The execution request has SHA256 `f2a8c326dc535732259d5b4ffa6116746ef6e59747a398e5b7c624c2ce13f213`; the workflow at the source commit has SHA256 `19ab01312daa730c947ba3ae6c1c59610e6521ed692b324709965946ede36908`. All request sources, the self-reported consumer, and the source commit agree.

| Topic-relative source | SHA256 |
|---|---|
| `notes/R973-original-balanced-Kronecker-four-prime-execution-method.md` | `32d4c836cacbb0467c668a4a968be62fe759cd188a3365bdfb9da9583d076269` |
| `notes/R989-original-r8-sparse-heat-and-Kronecker-window-method.md` | `430459e1a80765b48efe83b1255a4f0a0bfbc7998dad5e8c3e039d2a8a76c4c0` |
| `notes/R993-original-combined-disjoint-window-method.md` | `c19133588a246f770f0a05820aff1d8046d87c83a898e1a6ec1cd240a00b6f06` |
| `results/R963-original-r2-moment-window-through-100000.md` | `8259c94ba3474395d47debe638bf776c696821df848e310c647d9027c561c826` |
| `results/R975-original-balanced-Kronecker-integral-heat-recurrence.md` | `56ab77273393f6db838daea1a3973e1d9da69525eb120e665dccea88f64de101` |
| `results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md` | `db82c7e799a7e54b7d91da329e4e6c113add5a98a519aab82df2a2e70de470a7` |
| `results/R990-original-hypergeometric-fixed-r-coefficient.md` | `5c35e72804eee83dde2c74af68232dea3a57c5d97ba39026a07329a7db25a7a1` |
| `results/R991-certified-original-r8-balanced-window-through-20000.md` | `1dfc30c1e246a778955c6470d7c668a83c017b6ee76055b16f548611c211d354` |
| `scripts/original_balanced_combined_disjoint_window.py` | `2e60046ffa0ea7cbf7534ad796bba8e4fd1086a5ef7198312089a73d96793f7e` |
| `scripts/original_r8_balanced_new_window.py` | `96b3bbf3ec77c3c75a3870adebd9f348e7849f52b17dcda245f56229682f7160` |

The two rule hashes were verified before execution: root README `581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102`, and topic README `35f82f3d96f1e07d1b7c3f0320398fdc0cd68d0c0e55ac17881c9f976299646d`. No raw arrays, full row tables, regenerable certificates, Actions artifacts, or Releases are added to Git by this receipt. The public stdout and exact compact receipts preserve the execution provenance.

## 7. Exact mathematical scope and continuation

R988 identifies the original complete trace unit condition with the original coefficient `c_(p-r)^+` being nonzero, with all original phases and unit scales retained. Therefore the **original complete trace is nonzero for every prime in the two new finite sets above**. Combined only with the already registered R991 and R963 coverage, these new sets extend the respective known finite ranges through 200000.

No all-prime nonvanishing statement follows from 4008 successful new points. The original same-label product remains a different condition; R945 already shows why full-trace nonvanishing cannot replace it. No height or rational-point exclusion is asserted. The R993 request is now complete and must not be triggered again. Continue the actual filtered-source and near-p pairing questions recorded in HANDOFF and open.md; do not treat a further routine scan as resolution of those gaps.
