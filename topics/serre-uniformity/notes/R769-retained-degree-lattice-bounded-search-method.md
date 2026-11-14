# R769 — A bounded exact search in the retained original degree lattice

Date: 2026-11-14. **Status: method and executable certificate interface; no search result is asserted before the public run.**

This task reuses the complete R759 output from public run 43625474728, source commit 4728e6868e2509556e5c60e138fd97c9b4120d8e. It searches the already computed twelve-dimensional integral map lattice for a nonzero map of degree at most $693$. It does not repeat a period, HNF, LLL, intersection, finite-field, or CM field computation.

The target remains the actual R735 curve $C:y^2=x^3+b$, with differential $dx/(2y)$, and the maps retain the original $c_0$ normalization and $c_1$ marking. A search failure at its time budget is not a proof of nonexistence.

## 1. The three exact retained inputs

The producer artifact is serre-global-R759-original-integral-period-lattice-and-map-degrees-43625474728-1. Its full output manifest has SHA-256 fb61ded80deb7f6904de7e0aa2e7a3f3b161a0ecd2f5f0c329e96935c4e9f1aa.

| File | SHA-256 |
|---|---|
| p41-original-integral-period-lattice-and-degree-certificate.json | 7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0 |
| R759-exact-degree-LLL.json.gz | 5a1b6d44694389ac3fe48686a00c1745976726fefd8ff5196e2f60d4ef063825 |
| R759-original-integral-maps-and-bounded-recovery-input.json.gz | 037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc |

The producer core SHA-256 is 17403f45f74e03e5a138376068e64e54c9bf6b2622a7b91bb178747d407708e0.

The wrapper verifies the original manifest, successful producer receipt, source commit, run ID, and these three file hashes. The core independently requires the original certificate's full rank $12$, use of all $1600$ integral-period conditions, exact HNF and LLL assertions, and positive degree form. It requires the LLL and map files to have exactly the same configuration as the certificate.

Write $G$ for the retained twice_degree_Gram_matrix. It is in the same ordered LLL basis as the twelve maps. The core checks equality of the two retained copies of $G$ and the diagonal degrees in the old certificate. In particular the already published least basis degree is $1206$; this is not a claim about arbitrary integer combinations.

The old LLL row transformation is denoted $U$. If $w\in\mathbb Z^{12}$ is a coefficient column in the retained LLL basis, its column in the original saturated basis is $U^{\mathsf t}w$. No new reduction of a basis takes place.

## 2. The exact quadratic form and the cutoff

R759 proves for the retained integral-period lattice that

$$
d(w)=\frac12 w^{\mathsf t}G w
     =-a(w)^{\mathsf t}\Omega^{-1}b(w).
\tag{769.1}
$$

The second equality is recalled only to identify the original degree and sign. This task never solves for $\Omega^{-1}$, reconstructs the periods, or changes the differential normalization.

The search condition is exactly

$$
w\ne0,\qquad w^{\mathsf t}G w\le1386.
\tag{769.2}
$$

The matrix is symmetric with even diagonal. Its quadratic form is therefore even on integer vectors, and its positive definiteness makes every nonzero degree positive.

Why $693$ is useful is specific to the retained original quotient $Y=X_1/\mu_3$. It has genus $127$ and the fixed function $t=a^3$ has degree $820$. For a map of degree $d\le693$,

$$
820-d\ge127.
\tag{769.3}
$$

Thus the single divisor $D=(t)_0$ suffices in the R762 recovery argument: $L(D-(y)_\infty)\ne0$. Its dimension is

$$
h^0(Y,\mathcal O(D))=820+1-127=694.
\tag{769.4}
$$

In the R767 low-weight description, put $L=K_Y+D_{\rm cusps}$ and let $P,Q$ be the two order-three elliptic points. Then

$$
M_6(\Gamma_Y)=H^0(Y,3L+2P+2Q),\qquad \dim M_6=694.
$$

The genuine weight-six form $\eta_{\rm Ded}^{12}$ has zero divisor $41D_{\rm cusps}$ in this bundle, while $(t)_\infty=41D_{\rm cusps}$. Consequently

$$
\operatorname{div}(t\eta_{\rm Ded}^{12})=(t)_0,\qquad
L((t)_0)=M_6(\Gamma_Y)/(t\eta_{\rm Ded}^{12}).
\tag{769.5}
$$

These identities explain the cutoff. They do not assume that the bounded search will find such a vector. The existing degree-$1206$ route continues independently.

## 3. Rational LDL and exact integer intervals

The core computes a rational factorization of this small retained matrix,

$$
G=\mu\,\operatorname{diag}(r_0,\ldots,r_{11})\,\mu^{\mathsf t},
\tag{769.6}
$$

where $\mu$ is lower triangular with diagonal one and $r_i>0$. It reconstructs every entry of $G$ from (769.6) using exact rational arithmetic. This is an LDL factorization for enumeration, not a new LLL calculation.

For an integer coefficient column $w$,

$$
w^{\mathsf t}G w
=\sum_{i=0}^{11}r_i
 \left(w_i+\sum_{j>i}\mu_{ji}w_j\right)^2.
\tag{769.7}
$$

The depth-first search fixes $w_{11},w_{10},\ldots,w_0$, in that order. Suppose the suffix $w_{i+1},\ldots,w_{11}$ is fixed and its contribution to (769.7) is $S_i$. Set

$$
c_i=-\sum_{j>i}\mu_{ji}w_j,\qquad
R_i=\frac{1386-S_i}{r_i}.
\tag{769.8}
$$

A branch with $S_i\le1386$ has exactly the following allowed next integers:

$$
(w_i-c_i)^2\le R_i.
\tag{769.9}
$$

There is no floating-point interval estimate. Write $c_i=a/b$ and $R_i=r/s$ in reduced form, with $b,s>0$. Define

$$
K=\left\lfloor\sqrt{\left\lfloor b^2r/s\right\rfloor}\right\rfloor.
$$

Since $bw_i-a$ is an integer, (769.9) is equivalent to

$$
-K\le bw_i-a\le K.
$$

Thus the exact endpoints are

$$
\boxed{
\left\lceil\frac{a-K}{b}\right\rceil
 \le w_i\le
\left\lfloor\frac{a+K}{b}\right\rfloor.
}
\tag{769.10}
$$

Python's unbounded integers, Fraction, and integer isqrt implement these formulas. No precision parameter enters the mathematical test.

Within each interval, the order is nearest integer to $c_i$, then offsets $+1,-1,+2,-2,\ldots$, skipping integers outside the interval. The nearest-integer tie convention is $\lfloor c_i+1/2\rfloor$. This changes only search order. Every integer in the closed interval occurs exactly once.

## 4. Completeness, stopping, and a found map

Every vector satisfying (769.2) has a suffix whose contribution is at most $1386$, because all terms in (769.7) are nonnegative. At each level its next coordinate therefore lies in (769.10). Induction on the depth shows that it occurs in the search.

Conversely, every accepted leaf satisfies the quadratic bound. At a leaf the implementation also recomputes $w^{\mathsf t}Gw$ directly from the retained integer matrix and checks equality with the sum of LDL terms and evenness. The zero vector is recorded and excluded as a witness.

No quotient by a sign, by the $\zeta$ action, or by any other symmetry is used. Thus there is no orbit-representative condition that could discard a candidate.

There are three distinct outcomes.

1. **Found:** a nonzero vector has been certified. The search may stop immediately; it does not claim to have found a shortest vector.
2. **Exhausted:** the DFS stack is empty. The entered and finished frame counts agree at every depth, and the only accepted leaf was the zero vector. The exact bounded region contains no nonzero vector.
3. **Searching:** the time budget or an external stop request was reached. The exact stack and audit data are preserved. No assertion of nonexistence is made.

Positive definiteness gives finiteness of the bounded region and hence finiteness of a complete traversal. Budget termination is deliberately separate from that mathematical fact.

For a witness, the implementation divides the coordinate gcd, if necessary, and fixes the sign by making the last nonzero coordinate positive. This remains an integer vector in the same full lattice; it can only reduce the degree. The reduced vector's degree is checked again by (769.1).

The witness records:

- its twelve integer coordinates in the retained LLL basis;
- the twelve original saturated-basis coordinates $U^{\mathsf t}w$;
- the twelve rational coefficients in the original $h_0,\ldots,h_5,\zeta h_0,\ldots,\zeta h_5$ directions;
- the six exact coefficients of the original $\omega_0,\ldots,\omega_5$, each as the retained pair $A(b)+\zeta B(b)$ with degree at most six in $b$;
- the degree, the original target and base-point normalization, and the unchanged $c_1$ coset.

The six coefficients are direct integer linear combinations of the twelve retained map vectors. In particular no period reconstruction, numerical recognition, or arbitrary Manin/KS unit is involved. The new rational functions and the point $\beta$ are still to be recovered after a witness is found.

An exhausted result concerns precisely the full retained R759 lattice in the original factor. It is not a minimum-degree theorem for unrelated elliptic quotients.

## 5. Checkpoints and an inspectable traversal

The exact checkpoint contains the full active DFS stack. A frame records its suffix-dependent rational center and partial norm, its integer endpoints, the next center-out cursor, and the number of accepted integers already visited.

The cursor is advanced before descending into a child. Therefore a saved active child and its parent cursor describe disjoint completed and pending work. Continuation restores these cursors; it does not repeat the committed traversal prefix.

Each event is also appended to a hash-chained audit stream:

- enter a frame, with the full suffix, exact partial norm, center, and bounds;
- try an integer and its new exact partial norm;
- finish a frame, with its accepted-integer count;
- accept a leaf, with its exact vector and direct quadratic value.

A frame is finished only after its accepted count equals the length of its exact integer interval. Audit events are saved in numbered gzip blocks of at most $4096$ events. The checkpoint binds their names, SHA-256 hashes, chain endpoints, and counters. The separate audit manifest and the final certificate bind the same chain.

On continuation, the source SHA, retained input hashes, cutoff, configuration, every committed block hash, and the hash chain are checked. The active suffix centers and partial norms are checked again from the small exact LDL data. Completed branches are not enumerated again. An orphan block that was written after the last atomic checkpoint is left in the old artifact and is not copied over a new continuation.

A final completed certificate is reused only with the identical configuration and exact bound. Its saved checkpoint, LDL data, audit manifest and, when present, witness must match the saved hashes.

The core's soft budget is $720$ seconds. The wrapper allows $15$ minutes for the core and requests a clean stop before a forced termination. The core checks for a stop between DFS transitions and saves an atomic checkpoint. A clock only decides when to pause; it is not used in any numerical inequality.

## 6. Public execution and publication

The request explicitly identifies this public repository and the successful R759 artifact. The mathematical core has an Actions/repository guard. This task needs only Python's exact standard-library integers and rationals; it does not install a numerical or lattice package.

The wrapper creates the initial source and failure receipts before downloading or validating a producer artifact. It archives the exact core, wrapper, request, workflow, method, dependencies and both READMEs. Its sparse checkout includes the workflow itself.

All output, including failed or partial attempts, exact audit blocks, the original source archive, and any witness, is uploaded to an Actions artifact. Small receipts, the certificate and the small LDL record are published using the existing public recovery helper. That helper checks README differences and retries non-fast-forward pushes by pulling with rebase. No new private workflow or external compute service is used.

The final verification accepts only a certified witness or a genuinely exhausted traversal. A budget checkpoint makes the job incomplete while preserving all work needed to continue. Neither outcome is promoted to a result before its actual public receipt is inspected.

## Dependencies

- The actual R759 producer certificate and the three exact files in section 1.
- [R759 method](R759-original-integral-period-lattice-and-map-degree-method.md): the full integral lattice and exact original degree form.
- [R762](../results/R762-original-mu3-quotient-and-single-function-map-recovery.md): the same original quotient, base point, and finite function-recovery argument.
- R767's low-weight description is used only to explain the potential $694$-dimensional downstream computation; it is not a hypothesis in the enumeration proof.

The enumeration and interval proof above are elementary and complete. No empirical LLL quality estimate or floating-point exclusion is used.
