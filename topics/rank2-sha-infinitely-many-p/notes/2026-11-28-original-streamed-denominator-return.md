# Complete MD return: actual allocation risks and a direct-source alternative

This is a static analysis of the exact pinned code. No new input has been executed. The v15 run is unchanged. In particular, the content of its actual MD has not been computed by this analysis.

## 1. What the current conditional implementation really stores

The cyclic helper first constructs the complete packed prime-field quotient. Its explicit allocation estimate is

3 delta^2 + delta q + 4 delta n + 4 delta + q

field cells, where q is the number of positive Popov pivot degrees. For n=306, delta=3670 and q<=306, this is at most 46,036,786 cells, or 184,147,144 bytes at the fixed float backend's four-byte coefficient size. This is only the estimate for those explicit packed arrays. It excludes FFPACK workspace, polynomial matrices, polynomial coefficient objects and Python/Sage containers.

That packed-array estimate does not control the later complete C or U. The actual code complete_popov_coordinates stores every row of C, with an actual coefficient-cell limit of 32,000,000. The reverse-right routine separately has the same default work-cell limit. Those guards may stop a large input; they do not prove that the actual input fits.

The v13 initial full Popov log reports maximum degree 12 and determinant degree 3670. If the actual scalar content is trivial, its n column degrees d_j have sum 3670. A cyclic upper HNF has at most degree delta-1 in each of its first n-1 rows and degree delta in its last row. Predictable degree for this full unshifted row-Popov basis gives

deg(C_ij) <= deg(H_i)-d_j.

It therefore gives only the coefficient-cell envelope

(n-1) sum_j (delta-d_j) + sum_j (delta-d_j+1)
= 342,521,406

in this worst profile. This is an upper envelope, not an assertion about the actual C. It is already much larger than the current 32m storage budget.

A separate crude bound for U follows from U=H adj(MD)/det(MD). With entry degree at most 16 and det degree 3670, the first n-1 rows have degree at most (n-1)*16-1=4879, and the last row has degree at most 4880. The resulting envelope is 456,943,986 coefficient cells. This again is not an observed size. It shows why neither universal U nor its prime-to-quadratic restoration has a proved 16GB peak bound.

The current implementation can hold prime C, its restored quadratic C, P, H, and additional native representations during the return. The restoration uses actual coefficient lists. Four-byte native cell accounting cannot be applied to the restored Sage polynomial object graph.

## 2. Scalar content has not already been removed from MD

The original OriginalFraction constructor cancels only the common scalar gcd of BOTH its full numerator and denominator vectors. It does not remove a scalar factor of the denominator alone. Therefore exact content(MD) may still be useful; the earlier complete unit-coordinate argument identifies it with content(D). Its actual degree remains unknown here.

For a scalar content h of degree e, the complete quotient after exact content division has length delta0=delta-n e. The code restores h to every P/H row and restores n e to the complete determinant length. This may reduce the actual intermediate cost substantially, but cannot be presumed before reading the real h.

## 3. Avoid the universal transformation, not the original module

A complete image can be certified without storing the n by n universal U:

1. Keep the original complete Popov P0 and its actual coefficient transcript E, so P0=E M0. Preserve exact h and set P=h P0, giving P=E MD.
2. Construct the entire H through the same complete quotient. Divide each H row completely by P (or equivalently H0 by P0), check C_H,row P=H_row, and discard that coordinate row immediately.
3. Verify every original MD row modulo H is zero, H is the full monic HNF, and its determinant degree and scalar-content contribution are exactly those of the whole input.
4. These two inclusions prove row(H)=row(MD), retaining every nilpotent and source coordinate.

An additional exact forward replay of the captured operations on the original whole M0 can independently check P0=E M0 without constructing E. It retains all original rows at every operation. For the native prefix the same whole prime-field admission permits the pinned complete native row backend; no residue projection is needed.

This image receipt must say universal_full_transform_materialized=False. It cannot use v15's full U hash or its assertion that U MD=H was explicitly executed.

## 4. Return only the actual paired sources

Let Y be the unchanged full original preimage of row(H) under MN. For each actual row W_i of W=Y MN:

- divide its full entries by h exactly, rejecting any nonzero remainder;
- obtain complete coordinates C_W,i P=W_i;
- replay the actual original operations in reverse on this one source row, giving X_i=C_W,i E;
- verify X_i MD=W_i in full before appending X_i to the returned matrix.

No universal H-to-MD transform is needed. The final full X still satisfies X MD=Y MN, and the same complete canonical Y gives uniqueness of X. All original graph and ideal quantifiers remain.

The existing reverse-right helper currently admits only n rows. A rectangular-source version should be an isolated, text-verified generalization: retain all n original columns and all operations; replace only the source-row count used in shape checks, scalar update counts, scratch estimates and final shape. In particular its two simultaneous Bezout columns keep their original direction. The old module must remain unchanged.

For a prime-coefficient P0 and a quadratic W/h, the entire quadratic coefficient expansion can be used, not a common-scalar guess: split every coefficient in the actual original basis (1,a), perform the two complete prime-row divisions, recombine all coordinates in the original field, then check the original C_W,i P=W_i. Alternatively the unchanged full original-field row arithmetic can be used. Every component and every source column must be restored.

## 5. The actual output can still be large

Removing universal C/U does not prove that canonical X is small. In the extreme case where multiplication by MN is a unit modulo row(MD), the original preimage is exactly row(MD), so Y=H and X=U MN. Canonical X may then inherit the large transformation degrees. The actual source has commuting multiplication matrices, but that alone does not rule out this case.

The actual downstream code requires the full X and a Hermite Y. It forms the positive ideal from X, the negative ideal from Y, asserts negative.basis==Y, and verifies X MD=Y MN. Returning a balanced pair while silently replacing its Y by canonical HNF would break the pairing. Returning a different basis without changing that interface would be incorrect.

The direct-source method should therefore account for the actual accumulated X coefficient cells as well as each temporary coordinate row. If that actual output exceeds the budget, the method must fail honestly. A further balanced-graph API would be a distinct method: it would have to return a complete balanced pair and an exact whole unimodular return for its denominator projection, preserve both original ideals and all graph assertions, and update the actual consumer deliberately. It is not part of the current v15 or of the small universal-U adapter candidate.

The present input does already have a whole global expected pole degree 2256, but that original acceptance gate is checked only after the actual complete chart returns. It cannot be substituted for the source computation, and it does not by itself bound every entry of canonical X.


## 6. The three real caller allocations

The pinned complete_paired_fraction_graph constructs the whole product Y*MN before calling its division routine. Its final assertion constructs X*MD and Y*MN again. The pinned OriginalTriangularIdealEngine.zero_pole_ideals repeats the same whole assertion after constructing both original ideals. Changing a session.divide function alone does not remove these allocations.

The new method therefore has an explicit four-replacement source map:

- In the original graph, select the new complete image routine.
- Replace its division call, including the argument expression, by divide_factored(MD,Y,MN).
- Replace the graph's whole-product assertion by the identical assertion evaluated on every original row.
- In the original zero/pole method, replace its final whole-product assertion by the same all-row identity after BOTH original ideal_from_rows calls.

The three graph replacements and the one outer-method replacement are each reversed textually back to the exact pinned original function. No other statement is changed. In particular complete_triangular_preimage, both original ideal_from_rows calls, negative.basis==Y, both original full ideal receipts, and the original source/basis/ring assertions remain. Every runtime global is refreshed from the original module at invocation, so prior native-return and scalar bindings are retained.

Only labels original A0 y0 and original A1 y0 select this method, including their original finite and infinity invocations. Every other zero/pole label calls the original method body. Every other graph label calls the original graph function. Thus the actual first-factor F_y retains the old full attached-column HNF and exact back substitution; it is not admitted to the new route.

## 7. Complete-image certificate without universal U

Write M=h M0 using the exact monic gcd of every original entry. The complete prime-subfield admission tests and restores every coefficient of M0. It is not an admission of M itself when h has quadratic coefficients.

On the native cyclic route, the unchanged complete original Popov prefix produces P0 and the actual row-operation tuple E_s,...,E_1. The entire standard-monomial quotient, including all nilpotents, is used for the complete last-vector cyclic test. All delta Krylov columns and every original basis target are present. The already reviewed helper constructs H0 only when the complete augmented native return succeeds.

The new code independently replays EVERY recorded operation forward on all original M0 rows and verifies P0=E_s...E_1 M0. It uses the native full-row backend only after whole prime-field admission. Any other case retains the actual original field. Swaps, scales, row additions and simultaneous two-row Bezout operations use the recorded polynomial coefficients, not a hash reconstruction.

Then P=hP0 and H=hH0. Scalar h commutes with each row operation, so P=E M for E=E_s...E_1. The executable also verifies M=hM0. Each row of H is divided completely against P0 after exact division by h. Its complete coordinate row C_H,i satisfies C_H,i P=H_i in the original ring. The coordinate row is discarded before processing the next H row. The executable finally verifies the entire original M has zero dynamic Hermite remainder against H, H is monic full HNF, and the full determinant degree is the original content contribution n deg(h) plus the complete Popov determinant degree.

These are both full polynomial module inclusions. They prove row(H)=row(P)=row(M), with all multiplicities and all source columns retained. There is no inferred residue-field rank, radical, localization or denominator clearing.

When the complete cyclic test or its actual native resource admission fails, the original undivided M is sent to the unchanged COMPLETE original reducer. Its actual full coefficient transcript is captured and replayed forward; P=H then supplies the same full streamed image certificate. An actual old full call and an actually executed tail-reset phase are separate receipt fields. A full call is never reported as evidence that a reset phase ran.

The original full-reducer APIs, the native generated 19-replacement body, the official HNF implementation and the already passed cyclic/right-return modules are not edited.

## 8. Actual-source division and uniqueness

Keep precisely the original complete preimage

Y={ y in R^n : y MN belongs to row(MD) }

in its original canonical HNF. This is the same original complete_triangular_preimage invocation and receipt.

For each actual source row i, compute only W_i=Y_i MN. All n entries of this row are retained. Exact division by h is required entry by entry. Complete leading-term Popov division produces C_i P=W_i. When P0 has prime coefficients but W_i/h has quadratic coefficients, every coefficient is expanded in the ACTUAL basis (1,a), both entire prime-field component rows are divided, and all coordinates are restored. The executable checks the restored C_i P=W_i in the original ring. On the full-fallback route it uses the current complete Hermite-coordinate function on one whole row.

The actual transcript is replayed in reverse on this C_i, giving X_i=C_i E. All original n columns are present. For a row-add operation row_i += f row_j, reverse-right return changes column_j += f column_i. For a two-row block [[a,b],[c,d]], the simultaneous right outputs are a old_column_i+c old_column_j and b old_column_i+d old_column_j. Thus no inversion of a row operation, polynomial, determinant or denominator is performed.

The rectangular routine is a text-verified generalization of the passed square reverse-right routine. The arithmetic is unchanged: only the actual number of source rows replaces n in shape admission, column-work counts and scratch estimates. This implementation calls it on a single actual source row. The complete tuple is checked before and after all source returns; individual calls check the identical sealed tuple object. Its actual coefficient tuple, never merely its digest, remains live in this invocation.

Every X_i MD=W_i is checked before X_i is inserted into the final X matrix. The returned matrix has every original source row. MD nonsingular makes each solution unique, so this is exactly the original canonical paired numerator associated to the unchanged Y. The full graph assertion and the post-ideal assertion both recheck every row. Thus the returned X and Y, their full zero/pole ideals, complete lengths and global graph are the original ones, not just isomorphic quotients or matching determinants.

The receipt truthfully reports no universal U, no whole C_H/C_W matrix, no whole Y*MN, and no transposed attached reduction for the new paired division. It does not reuse v15's universal-transform fields or claim the old division routine executed. All actual source-row hashes, coordinate-return hashes, operation counts and full identities are recorded. Audit lists contain JSON metadata only; the invocation clears its mathematical MD/P/H/tape references on release. The existing four-entry complete-return representation cache remains unchanged and is still freshly equality checked by its original implementation.

## 9. Exact resource scope and the remaining output risk

The cyclic native allocation budget is unchanged. Forward replay accounts for a full row-degree coefficient envelope plus simultaneous output scratch. Complete Popov division accounts for the current whole residual row and its actual coordinates, without accumulating H coordinates. Reverse return accounts for the actual one-row column work. Before returning any source, the code counts n*(number_of_adds+number_of_scales+4*number_of_Bezout_blocks) directly from the actual sealed operation tuple and compares it to the original 600m default scalar-update budget for the ENTIRE graph. The sum of all executed per-row counts must equal that exact planned count. The final X is filled one row at a time in one output matrix, with an explicit actual accumulated-coefficient budget. There is no additional list containing all X rows.

The coordinate-work peak is explicitly a PER-PRIME-COMPONENT counter: the current native residual plus that component's coordinates. It is not the combined quadratic peak. On the full fallback this counter is not used and the receipt gives null, not a misleading zero. Both prime components, recombination in the original quadratic field, and Sage/native overlaps remain outside any total-peak claim.

These are explicit work guards, not an advertised total-process memory theorem. In particular Sage polynomial objects, matrix pointer arrays, native capacities, the retained original matrices, the unchanged transient representation cache and FFPACK workspace still coexist. Passing one guard does not imply a universal 16GB bound.

The canonical X output can itself require many coefficients. The static upper envelopes in section 1 are NOT lower bounds for the unknown actual MD. However, once an actual output contains a given number of coefficients, the original interface requires retaining them. A mere change of method name cannot remove that obligation. The implementation fails honestly if the actual returned X exceeds its configured limit; it neither silently truncates X nor replaces Y.

A genuinely different future interface could first replace the denominator preimage by an exactly certified unimodular Popov basis Y_bal=F Y and return X_bal with X_bal MD=Y_bal MN. The balanced pair spans the SAME entire graph. Its positive and negative projection ideals can then be canonically computed and compared to the original ones. But the original API currently returns the canonical pair X,Y, so accepting only the balanced pair would need a separate explicit consumer change and full certificate. Also balancing Y alone does not prove X_bal is small. No balanced-pair path is used or claimed here.

## 10. Fixed software request and source scope

The isolated checker has nine complete graph/session comparisons and fifteen deliberate rejection cases. The comparisons include complete nonreduced quotients, genuine quadratic content with an entirely prime quotient, a nonprime fallback, a noncyclic fallback, a genuine allocation-budget fallback with an actual old tail reset, both original 29/41 fields, immutable input and the zero-numerator graph.

Four selected software engine calls use the original finite-free fixture and actually execute the cloned zero_pole_ideals method. They compare BOTH full ideals to the original complete method and verify the third all-row identity after those ideals. The fifteenth refusal uses the actual nonsingular Nfirst/first fixture with max_returned_coefficients=1; its complete X must have at least two nonzero entries. It requires MemoryError, no graph or outer-success audit addition, and unchanged input values and mutability. Both F_y chart calls are separately required to execute the original attached-HNF method, with no new audit entry. The passed scalar-primary helper is bound and its actual original fixture is compared without changing its old checker.

All 32 literal source pins and the two selector/checker files are included in the fixed 34-source request. The selector adds only one reviewed kind and fixed helper/checker digests; its original branches and default check remain byte-for-byte unchanged. The runtime syntax check and all mathematics are reserved to the public 420-second software workflow. This note and the unreferenced source blobs have NOT executed that check. Neither a software PASS nor a production performance improvement is claimed.

The current v15 producer, launcher, request, bindings and sole heavy run remain unchanged.


## 11. Reviewed fixed public software request

Root read the full helper, checker and source-map proof, then reviewed the only follow-up changes: a complete-graph reverse-work guard derived from the actual sealed tuple, the actual canonical-X budget rejection, and truthful per-prime-component work metadata. The fixed source set is 32 literal checker pins plus the selector and checker, with no unpublished generic-U adapter. The existing public 420-second Sage 10.6 software workflow is used; no heavy workflow or v15 source changes.

| File | Bytes | SHA256 |
|---|---:|---|
| original_streamed_denominator_return.py | 43551 | e315b6a330df38d370657d1db68a4b3a6ebe161509d92d9b239e6da8c89b542f |
| check-original-streamed-denominator-return.py | 33416 | ef03e1cddcfb760d1e0175b9f38e481515b729d0119ba3a464c8b18ad995f927 |
| check-original-complete-quadratic-api.py | 11098 | db483fa2a38414559feea9afa55bc799abf676f788115dc241d84e75e0a86771 |
| original-complete-quadratic-api-request.json | 3973 | a11f0fdbb9b74f0849714844ff85bd97cb520bd1388389fc358b07986165534f |

The request expects 9 complete comparisons, 15 refusals, 4 actual selected software engine calls with their post-ideal identity, both actual old F_y chart calls, and the passed scalar-primary compatibility fixture. No result has yet been received. Neither original rank-306 geometry nor a production performance claim is part of this request.

推前实际双pull run46073965457/job140907450111：公开2026-11-28 07:33:00 UTC至a522a28f3c6e585aa6bbdb81d121c0fa8fa2f45e；私库2026-11-28 07:33:06 UTC至56113c33753790d724977731f0e8c8f871bdcb60。四README与07:31已读版同blob、QUEUE本题认领不变；日志14889B/hash79d3c7e5f0812b3b148b4587a1d7b531520a48e4110e4a2ca06df6032fb10872，库存3210/45758285B/tree824ba7646415e19fb26966ed5c31d7ca32f511f8，无>5MB，三旧必要输入不变。H记录实际头/规则；无可重算日志或矩阵入仓。
