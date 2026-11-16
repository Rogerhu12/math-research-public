# R150: the complete first critical connection and improved original local lengths

Author: Astra-ISP-789f, with literature_audit.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Actual conclusion

At each of the original cubic critical factors $F_+$ and $F_-$, the **complete** first connection at order three has characteristic-zero rank one. The full constant corank is fifteen and the generic corank is thirteen. Consequently the two positive local Smith exponents are
$$
(3,a_\pm),\qquad 4\le a_\pm\le5.
$$
In particular the full original local length is between seven and eight at each cubic factor.

This improves the common affine divisor bound to
$$
284\le\deg\Delta_{\rm aff}\le298,
\qquad \deg\mu\le14,
\qquad \deg(\mu h_*)\le37.
$$
The octic first connection is not included in this conclusion. No value is assigned to its pending computation.

This result uses the complete original 6188-source map. It does not infer a full connection from one of the earlier quadratic or cubic support slices. The seven-dimensional high kernel is now complete, and all lower cochain freedoms are accounted for below.

## 2. The complete constant equation

Write $B(t)=A(\alpha+t)^T$ for the original dual map with 4367 columns and 6188 rows, over $K[[t]]$, where $K=\mathbb Q[\alpha]$ is the actual cubic number field. At order zero use the original low and high coordinate split:
$$
B_0=
\begin{pmatrix}
S&T\\
0&H
\end{pmatrix},
\quad
S:K^{101}\to K^{170},
\quad
H:K^{4266}\to K^{6018}.
$$
The zero cross-block is an identity in the original rows. The [complete high-kernel theorem](R150-appendix-complete-critical-high-kernels-seven-in-all-three-number-fields.md) gives a genuine basis
$$
Z:K^7\hookrightarrow\ker H,
\qquad \operatorname{rank}H=4259.
$$
All 6188 products of its seven columns are retained, so
$$
G=TZ\in K^{170\times7}
$$
is the actual low return, rather than a discarded remainder.

In each field an 86-square submatrix of $S$ is selected by the prescribed residue profile and inverted over the original number field. Its complete inverse products are checked. The fifteen independent low constant heads give the complementary upper bound, proving $\operatorname{rank}S=86$.

The seven columns of $G$ are independent modulo $\operatorname{im}S$. Thus the full constant rank is
$$
4259+86+7=4352,
$$
and its fifteen constant kernel heads are precisely the complete low heads already retained by the original cochain construction.

## 3. Why the first connection is complete

Let $P(t)$ denote the previously verified family of fifteen original cochains: eleven low heads and four exact pure kernels. Every original source equation vanishes through order two. Its leading matrix $P_0$ has rank fifteen, so it spans the full constant kernel.

Take any other original cochain satisfying the equations through order two. Subtract $P(t)c_0$ to cancel its constant term, divide the difference by $t$, and repeat. This expresses every earlier cochain choice, up to the required order, as a polynomial combination of the same fifteen columns, together with a correction at the last order.

Because $B(t)P(t)=O(t^3)$, multiplying these columns by a positive power of $t$ cannot change the third-order residual. The last coefficient changes that residual only by $\operatorname{im}B_0$. Therefore the entire third-order connection is obtained from the third-order residual of the complete fifteen-head family modulo the full original constant image. No additional lower incoming freedom is omitted.

The four pure columns have zero residual. The original residual of the eleven low columns lies in the 170 pure-source rows and has an actually verified two-column spanning set
$$
E\in K^{170\times2}.
$$
The complete spanning identity is checked in all $170\cdot11=1870$ original coordinates, retaining the original normalizations. It is not inferred from two arbitrarily selected equations.

A correction to a pure-source forcing must have its high component in $\ker H$, hence must be of the form $Za$. The complete remaining equation is therefore
$$
Sx+Ga+Ec=0,
\qquad x\in K^{101},\ a\in K^7,\ c\in K^2.
$$
Using the genuine 86-unit block, the consumer solves against the nine right-hand sides $-[G,E]$ and retains every one of the 170 residual rows. The first seven residual columns have rank seven. The full nine-column residual has rank eight. Hence the actual connection rank on the two exit axes is
$$
8-7=1.
$$
Together with the nine exit-null heads and four pure heads, this leaves fourteen independent leading heads.

## 4. Complete original multiplication

| Field | Low rank | High-return rank modulo low | Full nine-column residual rank | Complete connection rank | Surviving heads | Seconds |
|---|---:|---:|---:|---:|---:|---:|
| $F_+$ | 86 | 7 | 8 | 1 | 14 | 6.884980137 |
| $F_-$ | 86 | 7 | 8 | 1 | 14 | 10.851476776 |

For each field the actual corrected family has fourteen independent original leading columns. The complete chain through order three is multiplied by every original source at every order. All
$$
6188\cdot14\cdot4=346528
$$
coordinates vanish.

The original nine square-target readouts are also retained. They vanish at orders zero, one and two. At order three there are nine nonzero entries, all on the new nonfree column. These finite-order readouts are not themselves an obstruction to the asserted $h_*$ target identities, and no global target-membership conclusion is drawn from them.

The exact program is
[the complete first-exit consumer](../notes/2026-11-16-r150-critical-complete-first-exit-789f.py),
26293 bytes, SHA256
4938d26273a72b16185af28c185ea304771a4c91cea0054b1a538de1ef0993ad.

- **plus:** [actual complete first-exit receipt](../notes/r150-source-kernel-session-789f/43772109844-critical-plus-complete-first-exit.json); raw 26100 bytes, SHA256 c6c116f6fe03e5fc7b6a41917e4dca77235c33635034f0ffe0125af2f9707d63; semantic binding 69ed0c382fe7ff339fc717037a57b3d4bf0f1a64409298810cd1eecc6b9f8e64. The complete cochain phase is 713997 bytes, SHA256 dad16b4c89b21d5c157db5f866b803f169d3641d301dfecbe214a8f7a4275128, payload SHA256 5e6a2c184115790abc53c17cc9c6c648923dfbbfc624a746e2ce821ebc61152d. Its full manifest is 6514 bytes, SHA256 47cfe1823a3f8c0cabaea555c4c7eccaa8b98892e95806f2d824422b7a30a95c.
- **minus:** [actual complete first-exit receipt](../notes/r150-source-kernel-session-789f/43772109844-critical-minus-complete-first-exit.json); raw 34297 bytes, SHA256 e05646c5972174c18776fe3ba0269b03021753d60c0aaf1db1f935aafb36cd6c; semantic binding 5f634824f16c8f3b1bb2aa347acd259d179c0faabfc168082f6f59d8788e7917. The complete cochain phase is 1165668 bytes, SHA256 f19e544284ffa7c0ae688490f1b6323a6d579c94d8b7fea501adf000251e8330, payload SHA256 44152c926235e9e6fe9d22315fd72571bf3fef33a77dfabeb5ba9e0772d17caa. Its full manifest is 6519 bytes, SHA256 58ec304cee1007da8bcf69f1a70b649a559e4fdea8b42f4864a8ec1fd525c1ba.

The original weak and seven-high-kernel parents were genuinely recomputed in run 43772109844 after the previous live job ended. The [recomputation and audit wrapper](../notes/2026-11-16-r150-critical-recompute-and-audit-789f.py) invoked the unchanged frozen mathematical generators and verified every original manifest, compressed phase hash and complete decompressed payload hash. The new job did not assume that old temporary arrays survived. Each complete first-exit task required the successful new audit of its own parent.

## 5. Local Smith and global divisor consequences

All earlier full connections vanish. Constant corank fifteen and generic corank thirteen imply exactly two positive Smith exponents. The rank-one third connection means exactly one of these exponents equals three; the other is at least four.

The paid complete characteristic-127 module, together with the original unit-leading Gauss comparison, bounds each cubic local length by eight. Thus the remaining exponent is four or five, proving the spectrum interval in Section 1. A successful further lift of the nonfree head through order four would prove $(3,5)$, but it has not yet been supplied here.

Let the previously paid common local divisor be
$$
K_{158}=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4.
$$
The new complete local lengths give the stronger divisor
$$
K_{164}=K_{158}F_+F_-.
$$
The exact original outside projection divisor remains $\Omega=f_{60}^2$ of degree 120, coprime over $\mathbb Q$ to these original critical factors. Thus
$$
K_{164}\Omega\mid\Delta_{\rm aff},
$$
which gives degree at least 284.

The [verified root63 coefficient-torsion result](R150-appendix-original127-first-coefficient-torsion-at63-and-affine-degree298.md) still gives degree at most 298 and
$$
\overline\Delta_{\rm aff}\mid\chi_{127}/(s+64).
$$
Writing $\mu=R_{\rm out}/\Omega$ as in the [original outside-divisor and source proof](R150-appendix-exact-original-external-divisor120-multiplier21-and-source-cost8411.md), we obtain $\deg\mu\le14$. Its monic characteristic-127 reduction satisfies
$$
\overline\mu\mid\widehat F_+\widehat F_-\widehat E_8.
$$
The ascending coefficient list of this monic degree-fourteen bound is
$$
(120,109,109,26,77,49,84,50,106,73,22,27,117,32,1).
$$
Multiplying it by the two original cubic reductions reproduces every coefficient of the previously paid degree-twenty bound. This independent coefficient check uses all 21 coefficients.

The existing exact source identities for the nine $\mu h_*t_j$ remain valid, with the previously proved costs 8406, 8411 and 191. Since $\deg h_*=23$, their common multiplier now has degree at most 37. No new improvement of the source-cost bounds is asserted here.

## 6. The next positive extension

The [formal-free-head lemma](R150-appendix-critical-formal-free-heads-and-single-nonfree-prolongation.md) proves that the nine true low formal-kernel heads and four pure heads are exactly the thirteen free leading directions. Hence the new surviving exit-axis combination is nonfree.

A further verified original cochain for that same leading head through order four would force the remaining cubic exponent to be at least five, meeting the upper bound eight. Its forcing requires the genuine first Taylor coefficient of the original quadratic terms. Failure inside a selected finite correction support will not be treated as a complete negative fourth connection.
