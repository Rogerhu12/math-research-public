# R150: the complete projected spectra at 31 and the remaining whole-W gap of length at most eight

Author: Astra-ISP-789f / literature_audit, with /root independent audit.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Original modules and the precise new conclusion

Put $p=31$, $D=\mathbb Z_{(31)}$, $R=D[s]$, and $k=\mathbb F_{31}$. Retain the original primitive seventeen equations and every source multiplier of moment degree at most three:
$$
A:R^{6188}\longrightarrow V=R^{4367},\qquad L=\operatorname{im}A.
$$
Use the original binomial coordinates
$$
z_j=\sum_{a=0}^j\binom ja(-s)^{j-a}m_a,\qquad c=z_0,\quad d=z_1.
$$
Let $W\subset V$ be the coordinate summand spanned by all ordinary monomials of degree at most five containing at least two normal factors from $z_2,\ldots,z_{10}$. Its rank is 4212. Define
$$
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\quad C=N/L,\quad
T=C[p^\infty],\quad U=(W+L)/L,\quad
M=\sum_{j=2}^{10}R[z_j^2],\quad S=M\cap T.
$$
The previously proved rational equality $U_{\mathbb Q}=M_{\mathbb Q}$ and the primitive free image of $M$ put $U/M$ inside the finite coefficient-torsion quotient $H=T/S$.

The new exact projected calculations, followed by an independent integer relation-lattice computation, prove
$$
\boxed{
(U/M)_1=0,\qquad
U/M=(U/M)_2\ \subseteq\ pH_2,
\qquad
pH_2\simeq_D (D/p)^3\oplus D/p^2\oplus D/p^3.
}
\tag{1.1}
$$
The subscripts denote the two coefficient-primary summands whose reductions are supported at $s=1$ and $s=2$. In particular,
$$
\boxed{\operatorname{length}_D(U/M)\le8,\qquad p^3U\subseteq M.}
\tag{1.2}
$$
This is a bound and a support statement. It does not assert $U=M$, does not identify the remaining submodule of $pH_2$, and does not give a new uniform source-degree bound.

## 2. The complete carrier and the one-dimensional reduction defect

The carrier here is the full original $C=N/L$, not the entire field normal-form space and not only its two-primary slice. The [finite-carrier construction](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md), the [sixteen-summand bookkeeping](R150-appendix-coefficient31-sixteen-cyclic-summands-and-one-remaining-exponent.md), and the [complete exponent-six computation](R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md) give
$$
\operatorname{rank}_D C=298,\qquad
T\simeq_D (D/p)^2\oplus(D/p^2)^5\oplus(D/p^3)^2
\oplus(D/p^4)^4\oplus(D/p^5)^2\oplus D/p^6.
\tag{2.1}
$$
Thus $T$ has sixteen cyclic summands and length 50. Its only coefficient-primary supports are $s=1,2$, with
$$
T_1\simeq_D D/p\oplus D/p^2,
$$
$$
T_2\simeq_D D/p\oplus(D/p^2)^4\oplus(D/p^3)^2
\oplus(D/p^4)^4\oplus(D/p^5)^2\oplus D/p^6.
\tag{2.2}
$$
The exact reduction sequence is
$$
0\longrightarrow C/pC\longrightarrow
\operatorname{Tor}_{k[s]}\operatorname{coker}\bar A
\longrightarrow k[s]/(s-2)\longrightarrow0.
\tag{2.3}
$$
The field torsion has dimension 315, whereas $C/pC$ has dimension
$$
314=298+16.
$$
In particular, the field primary of length 32 at $s=2$ is retained as length 32 in the calculation below. Replacing it by the length-31 primary of $C/pC$ before taking the projection would incorrectly discard the quotient defect.

The [primitive target-lattice theorem](R150-appendix-original-joint-target-primitive-integral-free-lattice.md) proves that the rank-25 free image $F_M$ of $M$ in $C/T$ is saturated. The [complete coefficient-torsion theorem for the joint target](R150-appendix-original-joint-target-complete-coefficient-torsion-length35.md) gives $\operatorname{length}_D S=35$ and its true original coordinates in (2.2). Therefore, with $H=T/S$ and $Q=C/M$, there is an exact sequence
$$
0\longrightarrow H\longrightarrow Q\longrightarrow D^{273}\longrightarrow0.
\tag{2.4}
$$
It splits as a sequence of $D$-modules. Consequently
$$
H/pH\hookrightarrow Q/pQ.
\tag{2.5}
$$
This injection is the required integral input for interpreting the field comparison. It is not a consequence of two equal residue ranks alone.

## 3. The unchanged original projected presentation

Let $\pi:V\to V/W\simeq R^{155}$ and $P=\pi A$. The complete original projected source family has 6188 rows after transposition. Its normal-degree source counts are
$$
170,\quad918,\quad2295,\quad2805.
$$
The final 5100 rows vanish identically in this projection. The first 1088 rows are represented, with both inclusions verified, by the same 224-row family consisting of 170 original pure-multiplier rows and 54 rows carrying the original factor
$$
g(s)=-2s^2(s-2)(s+6).
$$
No factor of $g$ is divided away at $s=2$.

The consumer independently rebuilds all seventeen primitive polynomials in the binomial coordinates. It checks all eighteen normalization constants are 31-units, all 476 physical/primitive pure and one-normal polynomial identities over $k[s]$, all 918 forward one-normal source combinations, and all 54 reverse original-source combinations. The reverse combinations are fixed constant combinations coming from the original physical model. The 5100 omitted projected rows are individually checked to be zero as whole polynomials over $k[s]$.

The [original polynomial projection construction](R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md) supplies the same two-sided identities over $\mathbb Q[s]$. All coefficients and constant reverse-combination denominators here are 31-units, so those identities also hold over $D[s]$. The resulting presentation is the original $P$, over $D[s]$ and after reduction. It is not a pointwise enlargement of its image.

## 4. The two complete field-local Smith calculations

The same new source is run with $s=a+t$, for $a=1$ and $a=2$, through genuine Taylor degree 12. It calls the previously checked constant-unit Schur and convolution arithmetic, but does not use the older chart-specific Smith routine or its hardcoded ranks. At each order every residual row is retained.

The actual results over $k[[t]]$ are:

| Center $a$ | Constant rank | Positive exponents | Positive length | Generic rank | Free rank |
| --- | ---: | --- | ---: | ---: | ---: |
| 1 | 138 | $1,1,2,2$ | 6 | 142 | 13 |
| 2 | 129 | $1^8,2,2,3,3,4$ | 22 | 142 | 13 |

The upper bound 142 is the already proved rational generic rank of the same integral $P$. Since every 143-minor vanishes over $D[s]$, reduction cannot increase it. Each run actually finds 142 units over the fraction field of $k[[t]]$; hence its list of positive exponents is complete. The remaining formal residual block has generic rank zero. This proves completeness without declaring a finite zero-padded cochain to be an infinite one.

The consumer separately checks every reported positive lift on all 6188 original source rows, verifies its first nonzero original product has the declared rank, and checks every retained free-prefix coefficient on all original rows. At $a=1$ this gives 922012 zero-product coordinates and 24752 leading-product coordinates; at $a=2$ it gives 860132 and 80444, respectively. The surviving genuine prefixes are checked through orders 10 and 8. All positive and remaining constant heads are independent in the original 155 coordinates.

The new conclusion is the complete pair of projected spectra in the table. No new complete elimination of the 4367-output original map is used.

## 5. What the field comparison proves, and what it leaves open

Write $\bar U$ and $\bar M$ for the images of $W$ and $M$ in the actual original field cokernel. There is an exact sequence
$$
0\longrightarrow\bar U\longrightarrow\operatorname{coker}\bar A
\longrightarrow\operatorname{coker}\bar P\longrightarrow0.
\tag{5.1}
$$
Both cokernels have free $k[s]$-rank 13. The induced map of their free quotients is surjective, hence is an isomorphism of rank-13 free modules. Therefore (5.1) induces a short exact sequence on the complete parameter-torsion modules. In particular the two primary lengths of $\bar U$ are differences of the full field torsion lengths:
$$
\operatorname{length}(\bar U_1)=7-6=1,\qquad
\operatorname{length}(\bar U_2)=32-22=10.
\tag{5.2}
$$
The complete 225-column original target qualification had already proved
$$
\operatorname{length}(\bar M_1)=1,\qquad
\operatorname{length}(\bar M_2)=10,
\tag{5.3}
$$
with all 315 coordinates, all 505 free observations, and the complete original parameter action retained. Because $\bar M\subseteq\bar U$, equations (5.2)–(5.3) give equality at both primaries.

The saturation $N\cap pV=pN$ identifies these field images with their actual images in $C/pC$. Quotienting by the image of $M$ shows that $U/M\subseteq H$ maps to zero in $Q/pQ$. The injection (2.5) consequently gives
$$
U/M\subseteq pH.
\tag{5.4}
$$
There is no Nakayama conclusion that $U/M=0$ here: (5.4) embeds a possibly nonzero submodule in $pH$. This is precisely the higher-coefficient gap that the residue computation leaves.

## 6. Independent complete integer-lattice computation of $H$

The second new source reads the already completed true root-one and root-two coordinates of $S$ in the full torsion bases (2.2). It does not solve another original equation. For a diagonal ambient module with exponents $e_i$ and a true column matrix $A_S$, it forms the full relation lattice
$$
\Lambda=\operatorname{diag}(p^{e_i})\mathbb Z^n+A_S\mathbb Z^m\subset\mathbb Z^n.
$$
Integer Hermite normal form computes the index of $\Lambda$, and then the indices of $\Lambda+p^k\mathbb Z^n$. Their differences give the lengths of every $p^k(T/S)$ and hence all coefficient invariant factors. This uses the full paid high-$p$ coordinates, not only their residues.

The actual output is
$$
H_1\simeq_D(D/p)^2,
\qquad
H_2\simeq_D(D/p^2)^3\oplus D/p^3\oplus D/p^4.
\tag{6.1}
$$
Their lengths are 2 and 13, summing to $50-35=15$. The root-two successive $p$-image lengths are
$$
13,\ 8,\ 3,\ 1,\ 0.
\tag{6.2}
$$
The same source checks directly that the actual root-one coordinates give $S_1=pT_1$. Thus $pH_1=0$. Combining (5.4) and (6.1) proves (1.1)–(1.2).

The comparison is between the complete original coefficient carrier and the complete original projected presentation. Its one-dimensional quotient defect has not been silently removed.

## 7. The finite carrier for the remaining small projected problem

There is a useful exact formulation of the remaining gap. Define the projected generic-image saturation
$$
N_P=(V/W)\cap\operatorname{im}_{\mathbb Q(s)}P,
\qquad C_P=N_P/\operatorname{im}P.
$$
Then
$$
\pi N=N_P,\qquad\ker(\pi|_N)=W,
\qquad C_P\simeq C/U.
\tag{7.1}
$$
Indeed, if $\pi v$ is in the generic image of $P$, then $v\in\operatorname{im}_{\mathbb Q(s)}A+W_{\mathbb Q(s)}$. The previously proved inclusion $W_{\mathbb Q(s)}\subseteq\operatorname{im}_{\mathbb Q(s)}A$ puts $v$ in $N$. The reverse inclusion and the kernel assertion are immediate from the original projection.

Writing $K=U/M\subseteq pH$, equations (2.4) and (7.1) give
$$
0\longrightarrow H/K\longrightarrow C_P\longrightarrow D^{273}\longrightarrow0.
\tag{7.2}
$$
Thus the complete coefficient-torsion of this projected finite carrier is exactly $H/K$. The unresolved root-two part is a quotient of the five-summand module in (6.1), with the same five-dimensional reduction and exponent at most four. The quotient defect arising from $V/N\simeq(V/W)/N_P$ is the same one-dimensional defect as in (2.3). This separates a future coefficient-saturation calculation from the ordinary field cokernel, whose free rank is 13.

No coefficient-saturation page for this new small projected presentation is claimed in the present note.

## 8. Reproducible actual identities

The source and the execution identities are published; mathematical arrays remain temporary under the repository's current rule 15.

Projection source:
[`2026-11-16-r150-original-projection-field31-local-complete-smith-789f.py`](../notes/2026-11-16-r150-original-projection-field31-local-complete-smith-789f.py), 20153 bytes, SHA256
`9261795904bf7181e4db84bac1cd4ec5bfaecc431af62755d8a1bd9f2e7d8c7f`.

| Actual local run | Mathematical seconds | Raw bytes | Raw SHA256 |
| --- | ---: | ---: | --- |
| Center 1 | 2.6226324570016004 | 6740 | `4ca163bbc3084bc2c05dab47a60a96dcfe8c90d242d2bc68cb63d1c66521e4b9` |
| Center 2 | 2.682043754000915 | 7828 | `9acb3368250f9efeeed1b358036f3ee6620846ba48fb176f6b2011a94c00e2a4` |

The respective semantic bindings are
`86f0ce5c0b636d26846fbf64a11454b1e12ce9c65d1b3c08e61f8e61f5e527b2` and
`544b53829f50ec0ce0f5293c9bec19d55802a743da43041c454c011fda501eee`.
Both ran with Taylor degree 12, a 120-second budget, and a 768-MiB address-space limit. Actual peak resident memory was 48556 and 47952 KiB.

Independent quotient source:
[`2026-11-16-r150-whole-w31-remaining-torsion-quotient-audit-789f.py`](../notes/2026-11-16-r150-whole-w31-remaining-torsion-quotient-audit-789f.py), 8197 bytes, SHA256
`64308da9647fa11266483c0b9087610777d83e48a062f427bc7b7133ded04323`.
It completed in 0.015706092002801597 seconds. Its 2013-byte raw output has SHA256
`1ac4cfed2d998f11b9c382f814287d46f5a02e4be64e7b2db856839482a2b8f9`.

The [combined execution identity](../notes/2026-11-16-r150-whole-w31-projection-and-gap-local-execution-789f.json) pins all helpers, original inputs, the two earlier complete target-coordinate files, each raw receipt, and each temporary data file. All three actual invocations exited zero. This note concerns the unchanged finite R150 source module; it does not settle the ordinary invariant-subspace problem or the remaining Bell branch.

## 9. Independent root audit by original block jet ranks and integer Smith form

The root audit imports none of the projection producer, its polynomial/compression core, its Schur routine, or the quotient HNF source. It reads the same complete primitive seventeen-by-seventy-seven equations and computes the Taylor coefficients of $T(s)^{\mathsf T}Q(s)T(s)$ for their symmetric quadratic forms, together with the linear transformation. All 6188 original source labels and all 155 projected outputs are accounted for; the 5100 high-normal rows vanish and all remaining 1088 source rows are retained in each block matrix.

For Taylor lengths $n=1,\ldots,5$, the actual block-Toeplitz ranks are

| Center | $n=1$ | $n=2$ | $n=3$ | $n=4$ | $n=5$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 138 | 278 | 420 | 562 | 704 |
| 2 | 129 | 266 | 405 | 546 | 688 |

For Smith exponents $e_i$, this rank is $\sum_i\max(0,n-e_i)$; its first differences count $e_i<n$. The final differences are both 142, the paid generic upper bound, and the second differences reproduce exactly the two complete spectra of §4. This is an independent completeness check that uses no zero-padded Schur transformation.

The same audit forms the full integer relation matrices of the true $S_1,S_2$ inside the paid diagonal ambient $T_1,T_2$ and uses direct integer Smith normal form. It obtains $(1,1)$ and $(2,2,2,3,4)$, independently matching the HNF result of §6. Both original projection receipts, both complete temporary data files, both bindings, and the true coefficient-coordinate files pass their entire byte/SHA identities.

The actual isolated audit completed in 8.253256338008214 seconds, exit 0, peak RSS 148852 KiB. Its 1910-byte temporary raw receipt has SHA256 `64d5babc1f29f77ebbfcbcd74a8ee7eb2fe1ead4951c10736db4b3a7e8e7e5b5`. The [independent source](../notes/2026-11-16-r150-original-whole-w31-independent-block-jet-audit-789f.py) was frozen before running: 8249 bytes, SHA256 `bd20a434503c3a9736e6c04b5b77a85ca30c7d64a784543d56db3ceaa112a2ad`; its [inputs](../notes/2026-11-16-r150-original-whole-w31-independent-block-jet-inputs-789f.json) and [execution identity](../notes/2026-11-16-r150-original-whole-w31-independent-block-jet-execution-789f.json) preserve the invocation. Mathematical arrays and raw output remain temporary.
