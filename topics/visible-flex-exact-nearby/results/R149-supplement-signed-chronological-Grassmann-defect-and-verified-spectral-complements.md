# R149. Signed chronological Grassmann defects for the physical low193 inverse

**Scope.** Use GG.1–GG.7's original WVC reference, the entire coefficient family, 155 parents and 1424 true-root cells, physical lengths and ordinary differential, all 193 coordinates, 97 freely propagated initial coordinates including the mean, 96 complementary coordinates, terminal impedance 13/80 and its independent mean equation. The 193,193,193,128 source columns have the original observation norms. A failure of a sufficient chart estimate leaves these data and the prior computation intact.

## GDC.1. Authenticated initial objects

The actual scientific result of public run 46135063788/1, 61622 bytes, has SHA256
`183e1b223c015b2c591133bebb5741ca9eec0d02c74b7055192d1c2c59f575cd`.
Its final execution, 68240 bytes, has digest
`f3de409e81db324211cb2c66f6bbff14811ed3542a3c72099ec20de87915cc15`.
Its 72126-byte manifest has digest
`e5f106998e4456d951183c05ace1cd2930d67fb7b8ffe207749dba6136799c19`.
It stopped on left cell 81 with the scalar test applied after the frame for node 82 had been defined. No complete BVP or source map was obtained. The 81 ordered scalar records have chain
`df33217279c5fc9d2717b0a3815e44d8aa507ade1f5186cc63195747f8f73434`.
Their definitions and errors are distinct from the underlying native objects.

| Whole native data | Bytes | SHA256 of the ordered index |
| --- | ---: | --- |
| 89 whole forward/reverse/physical moment packets | 185822772 | `a64b34280dc6adad784589085ba6039c7f8cc19077be988aee15a35ad26c8e52` |
| 82 exact Householder frame definitions | 12283518 | `bb0c87191792f278615889be4cfa95413845c60bb031a749bfac817ee5990574` |
| 245 private graph, inverse and frame matrices | 36669520 | `9fd5ef9f1ca8b8b5331b1cff704b0d6af1d7b6b08b1064c1693fba3d629fd292` |

Verify the original TF81 three whole objects, all three GG indices, the complete matrix write journal `108f895c53394560171651408584a00aa21e370846c64dc69dfcffd843c53aa3`, and the packet arrival chain `61e66e72eecdf989305547f10bdec90b0f97ec078cc7d7228cec470ce6bda9f4`. The actual last received was packet 88. Enumerating the seven preceding packet receipts recovers the original order even if a different worker finishes first today. Read back every private byte before a new graph proof. The original scalar failed predicate at index 81 is never necessary for matching any of these data.

## GDC.2. Verified spectral bound

For any real matrix enclosed entry by entry in a finite interval matrix M, evaluate G=MᵀM with directed arithmetic. One may transpose M first to use the smaller Gram matrix. For any single real rectangular S of compatible shape, G+SᵀS dominates G as quadratic forms. The largest eigenvalue is bounded above by the largest Gershgorin right endpoint of this latter symmetric matrix. The code proposes S from a floating eigendecomposition of the midpoint Gram using the square roots of the gaps between the largest proposed eigenvalue and the other proposed eigenvalues. The proof uses only the actual proposed finite dyadic entries of S and directed bounds on all entries of G+SᵀS. It also takes the minimum with the direct Gram Gershgorin bound and the square root of the product of the one- and infinity-norm bounds, and restores any exact power-of-two scaling. This applies to signed products as well as to a single coefficient.

## GDC.3. One true fractional step

Write the exact transfer as a nominal four-block dyadic matrix T₀ with blocks A,B,C,D, plus a single operator error of norm at most t. Let Z and Y be chosen dyadic centres of the graphs at consecutive nodes. The incoming true graph is Z+E with norm of E at most R. Let P be a dyadic proposed right inverse of A+BZ. Write L₀ for the dyadic centre of D−YB, and let l cover the rounding in that difference. For vertical and horizontal stacks set z=(1+‖Z‖²)¹ᐟ² and y=(1+‖Y‖²)¹ᐟ². Use the following directed upper bounds, with all intermediate roundoff included.

- c bounds ‖(C+DZ−Y(A+BZ))P‖ + t z y ‖P‖.
- α bounds (l+t y)‖P‖.
- d bounds ‖I−(A+BZ)P‖ + t z ‖P‖.
- β bounds ‖BEP‖ + t R ‖P‖, with its first term evaluated on the entire preceding signed history.
- k bounds ‖L₀ E P‖ on the same history.

The exact upper graph coordinate U is the upper block of T acting on [I;Z+E]. Thus ‖I−UP‖≤h=d+β. When h<1, U is invertible, ‖U⁻¹‖≤‖P‖/(1−h) and ‖U⁻¹−P‖≤‖P‖h/(1−h). Define E′ to be the exact outgoing graph minus Y. Multiplication of its fractional graph identity by UP on the right gives

```math
E'=L_0 E P+F,\qquad
\|F\|\le c+\alpha R+h\|E'\|,\qquad
\|E'\|\le(c+\alpha R+k)/(1-h).
```

Indeed the transfer perturbation acts on [I;Z] and [0;E] and is observed by [−Y,I]. Their operator norms give precisely the two t terms of c and α. Observing the same input in the top block gives the t terms of d and β. The preconditioner and transfer perturbation are never assumed independent of the true graph. In the first 81 cells alone the old complete graph ball and inverse in the same centres give independent enclosures. One can intersect radii when both proofs work, or retain the old validated denominator and graph when only its archived witness is positive. In both cases the bound on F uses the effective graph radius and the actual new h even if h≥1. A positive *new* bound is required at index 81 and every later unqualified step.

## GDC.4. Chronological defect propagation

For a contiguous block let (L,P,f) mean E_out=L E_in P+Δ with ‖Δ‖≤f. Two consecutive blocks 1 and 2 yield the exact signed nominal products L₂L₁ and P₁P₂, with outgoing error at most f₂+‖L₂‖‖P₂‖f₁. Maintain the dyadic partition of the full time history by concatenating adjacent equal-length blocks. For a current observation (M,N), traverse the blocks in reverse order. Charge each block's f after bounding the norm of the full products M L_last ... and ... P_last N from all later blocks. Then charge the initial radius after the complete product. The minimum with ‖M‖R‖N‖ is valid. Use observations (L₀,P) and (B,P) separately. Every cell and defect enters the maintained representation. Whole private checkpoints enclose each entry of every retained signed product and each nonnegative envelope by outward decimal balls. Subsequent nominal products use the reloaded enclosures.

For the left pass use the old 82 authenticated frame definitions, then select each subsequent full rational Householder frame from the propagated nominal columns. The coordinate centre can be zero in each newly proposed moving frame. Its complete residual is still paid by c. The right pass starts with the full original physical terminal matrix, including the independent mean, and uses a floating fractional-map proposal as its next centre. Each inverse proposal M⁻¹ in the terminal and the complementary node equations has its entire directed defect ‖I−MP‖ validated before use. The complete vectors and duals of GG.5 then follow. This gives the actual low BVP only after 1424 left inclusions, 1424 right inclusions, the true terminal solve and all 1425 complementary nodes. The four physical maps require the subsequent full signed GG.6 covariance calculation on that same private model and every original atom.

There are three ordered public targets. The first records the genuinely new positive denominator and graph at the previously failed physical cell. The second establishes the whole inverse. The third establishes all four source maps. Each completed target is saved before the next starts. Global height, infinite complements, waist returns, both nonlinear right-hand sides and the physical family still require their own equations after this low-dimensional calculation.
