# Original critical square targets: exact local exponents from a nonfree dual chain

Author: Astra-ISP-789f / literature_audit, with GPT-6 Astra Pro.
Date: 2026-11-16.

All three actual gates have now completed and have been read independently.
For every one of the original nine square targets, the exact local
annihilator exponents at $(F_+,F_-,E_8)$ are $(2,2,1)$. At each critical
place, every one of these nine classes generates the entire cyclic
difference module between the full original map and its projection.

| Original factor | Full positive Smith exponents | Projected exponents | Difference module | Exponent for each of the nine targets |
| --- | --- | --- | --- | --- |
| $F_+$ | $(3,5)$ | $(3,3)$ | $R/(t^2)$ | $2$ |
| $F_-$ | $(3,5)$ | $(3,3)$ | $R/(t^2)$ | $2$ |
| $E_8$ | $(2,3)$ | $(2,2)$ | $R/(t)$ | $1$ |

The actual source-level gates and small receipt identities are recorded in
Section 5. The earlier failed octic output is retained as historical
evidence; its mathematical completion was established by a new read-only
replay, not by relabeling the failed receipt.

Let $\Phi$ be one of the original irreducible polynomials $F_+,F_-,E_8$,
let $k=\mathbb Q[\alpha]$ with $\Phi(\alpha)=0$, and use the original
co-moving parameter $t=s-\alpha$. Work over $R=k[[t]]$.

The original nine targets are
$$
t_j(s,m)=
\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,
\qquad j=2,\ldots,10.
$$
Under the exact original binomial moment transformation they are precisely
$n_j^2$. No scalar arising from a source-equation normalization is inserted
into a target. Since $\Phi'(\alpha)\ne0$, the factors $\Phi$ and $t$ differ
by a unit in this local ring.

Use the original full map $A$, its image $L$, the target submodule $W$ of
normal degree at least two, and the original projection $P$ to the quotient
by $W$. The already proved generic inclusion $W\subseteq L\otimes k((t))$
makes
$$
T=W/(W\cap L)
$$
a finite-length module. The exact source-level projection sequence gives
$$
0\longrightarrow T\longrightarrow
\operatorname{Tor}(\operatorname{coker}A)
\longrightarrow
\operatorname{Tor}(\operatorname{coker}P)
\longrightarrow0.
$$
Here torsion surjectivity is part of the original projection argument:
the induced surjection on the two free rank-thirteen quotients is an
isomorphism. Equal rank by itself would not justify this assertion.

## 1. Exact exponent two at both cubic fields

The actual positive-prolongation receipts verify the following gates in both cubic fields:

1. The full first critical connection has rank one at order three.
2. The chosen surviving leading head is outside the thirteen-dimensional
   reduction of the full formal kernel.
3. A genuine original cochain through order four satisfies
   $A(t)^T\lambda(t)\in t^5R^{6188}$ with that unchanged head.
4. The full local length upper bound eight applies to these same original
   equations and parameter.

The formal-free-head argument in the
[preceding appendix](R150-appendix-critical-formal-free-heads-and-single-nonfree-prolongation.md)
then gives the exact full positive Smith exponents $(3,5)$.

At this stage only a lower bound for the complete original projection is
used. The [two cubic low-jet proofs, Sections 2--4](R150-appendix-both-cubic-fields-low-smith33-and-original-nine-target-local-membership.md)
prove the complete original low spectrum $(3,3)$ and the source-preserving
injection
$$
\ker(S\bmod t^N)\oplus(R/t^N)^4
\hookrightarrow\ker(P\bmod t^N).
$$
They retain all 224 projected source rows, including the 54 true $g$ rows.
The four additional pure coordinates are exact original kernel columns,
and the generic kernel ranks are nine and thirteen. Thus
$\delta_P\ge6$; this does not assert that every complete projected
correction is low.

The [original projection length-gap theorem, Section 2](R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)
therefore gives
$$
\ell_R(T)=8-\delta_P\le2.
$$
A finite module of length at most two over the DVR $R$ is killed by $t^2$.
In particular every original square target is killed by $t^2$ in the
original full cokernel. No exact projected spectrum has been assumed.

Write the actual original square readout as
$$
\lambda(t)^Tn_j^2=c_jt^3+O(t^4).
$$
If $c_j\ne0$, then
$$
\lambda(t)^T(tn_j^2)=c_jt^4+O(t^5)\ne0\pmod{t^5}.
$$
Every element of the original image pairs to zero modulo $t^5$ with this
same cochain. Hence $tn_j^2\notin L$. Together with $t^2n_j^2\in L$ this
proves that the target's exact local annihilator exponent is two.

Equivalently, if $\Phi(s)n_j^2$ were in the original image, the coefficient
of $t^4$ in its pairing would be $\Phi'(\alpha)c_j$, still nonzero. Thus
the statement is about the original factor $\Phi$, not a different
normalization of the local parameter.

The new positive consumer modifies the paid chain only by explicit
$t$-shifts of canonical low chains and by a new top coefficient at order
four. Every shifted canonical coefficient has normal degree at most one.
Consequently all two-normal square readouts of orders zero through three
are unchanged. The paid first-exit data for both cubic fields have zero
square readouts in orders zero, one and two; their selected nonfree column
has all nine order-three readouts nonzero. The new actual positive receipts themselves report nine nonzero entries in
this nine-by-one order-three readout, with orders zero through two zero.
Thus the argument applies separately to every $j=2,\ldots,10$.

For each target the preceding nonzero pairing gives a cyclic submodule
of $T$ with length at least two. Since $\ell_R(T)\le2$, that cyclic
submodule is all of $T$, and its length is exactly two. Hence
$$
T\simeq R/(t^2),\qquad \ell_R(T)=2,\qquad \delta_P=6.
$$
Each of the nine original square classes generates this same module.
The exact projected length is a consequence of the actual target
pairings and the length bound, not an input inferred from the low slice.

## 2. Exact exponent one at the octic field

The completed and independently replayed original first exit at order two
has rank one. With the previously paid full length upper bound five, the two full
positive exponents are then exactly $(2,3)$. The
[original low-projection proof, Sections 7 and 9](R150-appendix-original-low-projection-double-linear-divisor-and-E8-local-target-membership.md)
gives the low spectrum $(2,2)$ and the same complete 224-row jet
injection, hence only the needed lower bound $\delta_P\ge4$.
The exact projection sequence yields
$$
\ell_R(T)=5-\delta_P\le1.
$$
In particular $tT=0$. No equivalence between the complete projection
and its low submatrix is assumed.

The actual original cochain through order two satisfies
$A(t)^T\lambda(t)\in t^3R^{6188}$ and
$$
\lambda(t)^Tn_j^2=c_jt^2+O(t^3),\qquad c_j\ne0.
$$
Then $n_j^2\notin L$, while $tn_j^2\in L$. This target has exact local
annihilator exponent one. Its nonzero class spans a length-one cyclic
submodule of $T$, so
$$
T\simeq R/(t),\qquad \ell_R(T)=1,\qquad \delta_P=4.
$$
Every one of the nine classes generates $T$.

The original first-exit construction places its two-normal coefficient
at this order in the block
$$
[\,0_{450\times9},\ H_{450\times(2-b)},\ 0_{450\times4}\,].
$$
Here the actual complete connection rank is $b=1$. Therefore the
nine-by-fourteen square readout can be nonzero only in zero-based column
nine. The actual recovered receipt reports exactly nine nonzero entries.
Since there are only nine rows, each row has a nonzero entry in that
column. This proves the separate nonzero assertion for each target;
neither a matrix hash nor a total count alone was used without the
original support argument.

The read-only recovery reran the unmodified original compute function
against its completed phase files. It verified 259896 original products,
the complete first-exit gates, and byte preservation of every phase.
New RREF and phase writes were forbidden. The original log confirmed
that the initial failure was the 90000-byte small-receipt limit.

## 3. The complete projected spectra follow afterwards

For clarity, the projected spectra in the initial table are conclusions,
not replacements for the original low-jet lower bound.

Let $e=3$ in the two cubic fields and $e=2$ in the octic field.
The already verified injection of the complete low matrix plus the four
pure exact columns gives, for every $N\ge1$,
$$
\sum_i\min(a_i(P),N)\ge2\min(e,N).
$$
At $N=1$ this requires at least two positive projected exponents.
The torsion surjection from the complete full cokernel, whose torsion
has two cyclic summands, permits at most two. Thus exactly two positive
projected exponents occur.

At $N=e$, each of those two exponents must be at least $e$. Sections
1 and 2 have independently established $\delta_P=2e$ by the actual
target pairings. Their sum is therefore $2e$, which forces both
exponents to equal $e$.

Only now may one also identify the inclusion inside the full cokernel:
the complete projected torsion is killed by $t^e$, so
$$
t^e\operatorname{Tor}(\operatorname{coker}A)\subseteq T.
$$
Both sides have length two in the cubic fields and length one in the
octic field. Consequently this inclusion is an equality. This recovers
$T=t^3\operatorname{Tor}(\operatorname{coker}A)$ or
$T=t^2\operatorname{Tor}(\operatorname{coker}A)$, respectively, after
all their inputs have been proved for the complete original map.

## 4. Completion and global scope

The finite modules come from the original localized polynomial
presentation over $\mathbb Q[s]_{(\Phi)}$. Completion is faithfully flat,
so these local membership and exact-exponent assertions descend from
$k[[t]]$ to that localized presentation. No new source-degree family has
been introduced: the matrix still uses all and only the original
degree-at-most-three multipliers.

At either cubic field, the other factors of $h^*$ are units, and its
$\Phi$-valuation is two. At the octic field its valuation is one. The
conclusions above therefore prove both sufficiency and necessity of
these exponents for the stated original targets at these critical places.

This does not alone prove global membership, remove a residual outside
these places, give a coefficient-prime denominator bound, or settle the
ordinary invariant-subspace problem. Those statements require their
separate original-module arguments.

## 5. Actual executable gates and exact small receipts

All three actual steps ran in research run43772109844. Each completed
successfully with the gates described above.

| Field | Actual step | Mathematical seconds | Original product coordinates rechecked |
| --- | --- | ---: | ---: |
| $F_+$ | critical-plus-one-nonfree-positive-prolongation | 6.853180992 | 30940 |
| $F_-$ | critical-minus-one-nonfree-positive-prolongation | 9.306006032 | 30940 |
| $E_8$ | critical-e8-first-exit-readonly-completion | 8.444090138 | 259896 |

The two positive consumers also verify the original physical quadratic
first coefficient using the same formula modulo $\Phi^2$, including all
765 quadratic constants and every pure/linear first derivative.
Their selected head has actual rank fourteen together with the thirteen
formal-free heads. Their complete high correction is multiplied through
all 6018 original high source rows.

For the octic step, the actual fields
mathematicalCompletionRecovered=true,
allOriginal6188ProductsZero=true,
completeConnectionRank=1,
completeLeadingHeads=14 and fullLengthExact=5 are all present.
The failed raw receipt was not promoted. The original mathematical
binding and every original phase remain unchanged.

### Cubic plus

- [Actual small receipt](../notes/r150-source-kernel-session-789f/43772109844-critical-plus-one-nonfree-positive-prolongation.json).
- Outer: 16948 bytes; SHA256
  `6a097cd559546d7d6a8da6794a3f5965be807b64ce27ce787f5c6ae12a807b85`.
- Original temporary raw: 11447 bytes; SHA256
  `a1d6f0ea815c691152b89617a0882507aabd89217a80db6676fb933f41bf11a0`.
- Binding:
  `8acd244b1249a26bf10828bed703e6045c473ef33acf00d510de9cc7547bb61e`.
- The actual nine-by-one order-three square readout has nine nonzero
  entries and SHA256
  `69e581153c446234abce7a90c124d126b00815f927d04e90de8be39a6d1098c5`.

### Cubic minus

- [Actual small receipt](../notes/r150-source-kernel-session-789f/43772109844-critical-minus-one-nonfree-positive-prolongation.json).
- Outer: 19566 bytes; SHA256
  `40088c16cdfdf6f714513fea38da96e610f034c83ed48ff8b721034ec9bed455`.
- Original temporary raw: 14056 bytes; SHA256
  `1477c986e0a551a965b71470447d64a391bf978692df7ab37eaeb45eec196dca`.
- Binding:
  `97b453a49020af3fb05758604fa629fd94cd55738c85f91ec1726e2a9af26978`.
- The actual nine-by-one order-three square readout has nine nonzero
  entries and SHA256
  `aacedd0e3d52cbf0ee7adefd9f4779b6af7ee2d30be4722a15bd3c9dbd0d226f`.

### Octic field

- [Actual recovered small receipt](../notes/r150-source-kernel-session-789f/43772109844-critical-e8-first-exit-readonly-completion.json).
- Outer: 17541 bytes; SHA256
  `38459deb4f522b0c23f31ef97ae0ff5d110fcdb0302bbbda243540a50ab8422e`.
- Original temporary recovered raw: 9456 bytes; SHA256
  `15349fa57fdcae012ffc16fb65fe357258def3f45aeaf9563e39fa31cb395081`.
- Recovery binding:
  `9e283e5d5d0d7bd3c68236aeb905c61ee09d118c920a45267c7f2f868043dd0f`.
- The actual nine-by-fourteen order-two square readout has exactly nine
  nonzero entries, all in zero-based column nine by the proved support,
  and SHA256
  `2d7986105751a49c38b7558b3353b7279506b99b7579e2c58c535bfedcfc9053`.

### Frozen algorithms

The positive source is
[the one-nonfree original prolongation consumer](../notes/2026-11-16-r150-critical-one-nonfree-positive-prolongation-789f.py),
SHA256
`cbc594785576322260e051d41417b03367eae8ab9047f856e457db614beaeb59`.

The first-exit source is
[the complete original critical consumer](../notes/2026-11-16-r150-critical-complete-first-exit-789f.py).
Its exact mathematical code was rerun by
[the read-only complete-pack recovery](../notes/2026-11-16-r150-critical-e8-readonly-completion-recovery-789f.py),
SHA256
`00be5668fe1ea288869ff799421033b5b209d0c7577087dfa285955ac12fb0cf`.

The full target values and complete cochains remain in the verified
temporary phases. The published receipts preserve exact matrix hashes,
original product counts and all mathematical acceptance gates. No new
large certificate or matrix was uploaded.
