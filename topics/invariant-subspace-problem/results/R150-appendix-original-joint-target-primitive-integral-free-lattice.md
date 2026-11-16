# R150: the primitive integral free lattice of the nine original targets

Author: Astra-ISP-789f / literature_audit, with GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Statement and the remaining extension

Put $p=31$, $D=\mathbb Z_{(31)}$, $R=D[s]$, and $x=s-2$. Keep the original primitive map with every source of multiplier degree at most three,
$$
A:R^{6188}\longrightarrow R^{4367},\qquad L=\operatorname{im}A.
$$
Let $N$ be its generic-image saturation, $C=N/L$, and $T=C[p^\infty]$. This $T$ is the **coefficient-prime torsion**, not the rational relative parameter module. Write
$$
M=\sum_{j=2}^{10}R[t_j]\subseteq C,\quad
S=M\cap T,\quad F_M=\operatorname{im}(M\longrightarrow C/T),
\qquad t_j=z_j^2,
$$
with the original binomial coordinates and ordinary squares. Set
$$
h_*=s^3F_+^2F_-^2E_8,\qquad h=\operatorname{mon}(h_*).
$$
The leading coefficient $3125$ is a unit of $D$, so $h\in R$, $\deg h=23$, and $h(0)=0$.

The new complete original-target calculation proves that $F_M$ is a saturated rank-25 submodule of the finite free $D$-module $C/T$, and
$$
\boxed{F_M\simeq R/(s)\oplus R/(s)\oplus R/(h).}
\tag{1.1}
$$
Moreover, the first two summands lift to actual $R$-direct summands of $M$:
$$
\boxed{M\simeq R/(s)\oplus R/(s)\oplus E,\qquad
0\longrightarrow S\longrightarrow E\longrightarrow R/(h)\longrightarrow0.}
\tag{1.2}
$$
These are noncanonical isomorphisms. The extension $E$, and the full integral structure of $S$, are not identified by this calculation.

As $D$-modules one also has $M\simeq D^{25}\oplus S$. The complete field image of $M$ has dimension 34; its image modulo the actual sixteen coefficient-torsion directions has dimension 25. The resulting nine-dimensional intersection with the reduction of $T$ is a residue image of $S$, not an assertion that $S$ has nine cyclic summands.

The minimum number of $R$-generators of $M$ remains in the proved interval
$$
8\le d_R(M)\le9.
\tag{1.3}
$$
The newly computed full field image has six polynomial generators, so that particular lower-bound test does not separate the two possibilities in (1.3).

## 2. Original inputs and the actual complete residue space

The [complete coefficient exponent-six theorem](R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md) gives a finite coefficient module $C$, its complete coefficient-torsion spectrum
$$
T\simeq_D D/(p)\oplus D/(p)\oplus
(D/(p^2))^5\oplus(D/(p^3))^2
\oplus(D/(p^4))^4\oplus(D/(p^5))^2\oplus D/(p^6),
\tag{2.1}
$$
and sixteen actual divided-source classes realizing this basis. Its $D$-length is 50. Their reduction is the actual $315\times16$ matrix $U_{16}$; it has rank 16 and is invariant under the original parameter action $J$.

The [rational relative-module theorem](R150-appendix-zero-relative-target-partition-three-one-one-and-global-invariant-factors.md) gives
$$
M_{\mathbb Q}\simeq
\mathbb Q[s]/(s)\oplus\mathbb Q[s]/(s)\oplus\mathbb Q[s]/(h).
\tag{2.2}
$$
The [complete integral annihilator theorem](R150-appendix-original-nine-targets-complete-integral-annihilator-and-parameter-denominator-law.md) gives
$$
\operatorname{Ann}_R(M)=h_*(p^5,p^2x,x^2).
\tag{2.3}
$$
In particular, the monic associate of $x^2h_*$, of degree 25, annihilates $M$. Hence the 225 **original** columns
$$
s^k[t_j],\qquad 0\le k\le24,\quad2\le j\le10,
\tag{2.4}
$$
generate $M$ over $D$; no higher parameter multiples are omitted.

The complete original finite-field normal-form state has 820 state coordinates, 505 independent free observations, and a 315-dimensional parameter-torsion space. Its stored maps satisfy
$$
K\Xi=\mathrm{Targets},\qquad A_{\mathrm{state}}K=KJ,\qquad
OK=0,\qquad O\,\mathrm{Targets}=0.
\tag{2.5}
$$
The consumer repeats all these products, rank $K=315$, the full original-target action, and the $J$-closure of all 225 columns.

There is an injection $C/pC$ into this whole 315-dimensional space. It is essential that the full space is not simply renamed $C/pC$: the previously established quotient defect has dimension one. After quotienting by the actual $U_{16}=T/pT$, the reduction of $C/T$ still injects into the resulting 299-dimensional field space. All free-lattice ranks below are computed in this ambient quotient, with the injection retained.

## 3. The paid-parent reuse and the exact qualification

The local calculation reads the surviving completed full210 parent under its original binding. It does **not** claim that the subsequently frozen selected $p^9$, precision-35 parent was rerun.

It checks the complete parent's raw receipt and result bytes, the original driver, its canonical semantic binding, all thirty recorded original carry stages, all three complete $L_3,L_4,L_5$ class files, and the complete $L_6$ result. The current basis is reconstructed exactly as
$$
U_{16}=[\,U_{13},\ (L_5)_{10},\ (L_5)_{11},\ (L_6)_{12}\,],
\tag{3.1}
$$
where indices are zero-based original indices. In particular, it does not substitute the recipe's differently normalized fifteen-column incoming basis for the true original divided-source basis.

Both established logical identities are reproduced:
$$
\mathrm{SHA256}(U_{16})=
\texttt{679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9},
$$
$$
\mathrm{SHA256}(J_{16})=
\texttt{59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8}.
$$
The complete original identity $JU_{16}=U_{16}J_{16}$, with all 5040 coordinates, is checked anew.

The 225-column target matrix has rank 34. Its quotient by $U_{16}$ has rank 25. The chosen 25 independent columns are actual members of (2.4), and their rational span has dimension 25 by (2.2).

Here is the integral implication. If $v_1,\ldots,v_{25}$ in the free $D$-module $C/T$ have independent reductions, then $D v_1+\cdots+D v_{25}$ is a saturated direct summand: one of its coordinate minors is a $D$-unit. Every other original target multiple lies in its rational span, so saturation puts that multiple in this same integral span. Therefore it is exactly $F_M$, proving the rank-25 saturation statement.

The computed action $J_F$ on its reduction has
$$
\chi_{J_F}=s^2\bar h,\qquad \mu_{J_F}=\bar h.
\tag{3.2}
$$
Both assertions are exact complete characteristic/minimal-polynomial computations, followed by the full action identities. Their degrees are 25 and 23 respectively.

## 4. Lifting the integral free $R$-structure

Because $hM_{\mathbb Q}=0$ and $F_M$ is $D$-torsion-free, $hF_M=0$ integrally.

By (3.2), the field module $F_M/pF_M$ contains a cyclic vector with a 23-dimensional Krylov span. Lift that vector to $v\in F_M$. The 23 columns
$$
v,\ sv,\ldots,s^{22}v
$$
have a unit minor modulo $p$, and therefore generate a saturated free rank-23 $D$-submodule $U\subseteq F_M$. Since $hv=0$, they give
$$
U\simeq R/(h).
\tag{4.1}
$$
The quotient $F_M/U$ is free of $D$-rank two.

By (2.2), multiplication by $s$ has rational rank 22 on $F_M$. It also has rank 22 on $U_{\mathbb Q}$, because $h(0)=0$ and $\deg h=23$. Consequently
$$
s(F_M)_{\mathbb Q}=sU_{\mathbb Q}.
\tag{4.2}
$$
Saturation first implies $sF_M\subseteq U$. Also $U/sU\simeq D$, again because $h(0)=0$; hence $sU$ is saturated in $U$. Equation (4.2) therefore improves the inclusion to
$$
sF_M\subseteq sU.
$$
Choose two $D$-basis lifts of $F_M/U$. Subtract suitable elements of $U$ to make both lifts annihilated by $s$. This proves (1.1) without assuming that rational direct summands lift automatically.

Next, $s$ acts invertibly on the finite coefficient torsion $T$: its reduction is supported only at $s=1,2$, so $sT+pT=T$, and finite-module Nakayama gives $sT=T$. Its inverse preserves every $R$-submodule. For example, a polynomial inverse modulo $p$, followed by the finite geometric series for the remaining nilpotent $p$-error, expresses that inverse as a polynomial in the action of $s$. Thus $sS=S$.

The free resolution of $R/(s)$ gives
$$
\operatorname{Ext}^1_R(R/(s),S)=S/sS=0.
$$
The two $R/(s)$ factors in (1.1) consequently lift to $R$-sections of $M\to F_M$. Removing them leaves exactly the extension in (1.2). This does not split the remaining $R/(h)$ extension.

## 5. Complete primary residue information

The consumer forms primary idempotents from the **whole** original characteristic polynomial, evaluates them on the full span of $U_{16}$ and (2.4), and checks idempotence, pairwise orthogonality, commutation, and their sum. All transports back into the original 315 coordinates are multiplied through.

The complete field target image has the following actual primary data. Cubic factors are monic reductions of $F_+,F_-$, and $E_6$ is the degree-six factor of $\bar E_8$.

| Primary | Field target dimension | Free-target dimension | Image of $S$ in $T/pT$ | Field polynomial generators |
|---|---:|---:|---:|---:|
| $s$ | 5 | 5 | 0 | 3 |
| $s-1$ | 1 | 1 | 0 | 1 |
| $s-2$ | 10 | 1 | 9 | 6 |
| $\bar F_+$, degree 3 | 6 | 6 | 0 | 1 |
| $\bar F_-$, degree 3 | 6 | 6 | 0 | 1 |
| $E_6$, degree 6 | 6 | 6 | 0 | 1 |
| Total | 34 | 25 | 9 | Maximum 6 |

At each of $s=1,2$, the original target $t_2$ has nonzero free residue and qualifies as a primitive generator of the corresponding one-dimensional free Hensel line. The exact original $h_*$ values and derivative checks show simple Hensel factors at both roots.

To justify the intersection column of this table, suppose an element of $M$ reduces into $T/pT$. Its free image belongs to $p(C/T)$. Saturation of $F_M$ makes that free image $p$ times a free image already represented in $M$. Subtracting the corresponding $p$-multiple leaves an element of $S$ with the same reduction. Thus the computed intersection is exactly the image of $S$ in $T/pT$.

This image need not be $S/pS$. In particular, the zero root-one entry only gives
$$
S_1\subseteq pT_1,\qquad T_1\simeq D/(p)\oplus D/(p^2)
$$
after completion and primary decomposition. It leaves at most one hidden root-one $p$-socle. The root-two image of dimension nine does not fill the fourteen-dimensional reduction of $T_2$, and gives no equality $S_2=T_2$.

For each field primary $f$, the reported generator count is computed as
$$
\frac{\dim\ker f(J_M|_{V_f})}{\deg f}.
$$
The maximum is six. Since $M$ surjects onto its field image, this gives a lower bound of six, which is weaker than the already established bound eight. The [complete joint-$B$ theorem](R150-appendix-original-joint-nine-target-coefficient-module-length24-and-eight-generators.md) proves $d_R(B)=8$, and $M\xrightarrow{\ h_*\ }B$ is onto. Together with the nine original generators this proves exactly the interval (1.3).

## 6. Completed execution identities and next finite problem

This is an independently bound local reuse, with parent mode $\texttt{paidFull210/localReuse}$. The new qualification exited zero after 3.9234747430018615 mathematical seconds. Its 225-column/CRT/Nakayama/generator-count mathematical body is unchanged from the separately frozen selected-parent qualifier. Only the admitted-parent reader, its binding, and explicit reuse metadata differ.

| Item | Exact identity |
|---|---|
| New source | 25415 bytes; SHA256 $\texttt{2da1bbb101274730333af6bafb32595cc892351d42766d653d56fbc873fe9e30}$ |
| Original paid full210 binding | $\texttt{712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093}$ |
| Paid parent receipt | 42372 bytes; SHA256 $\texttt{dd867cfbbefcce2d7a846016807b1da6f56c73fd82ea9a364036348467bdc5b9}$ |
| Paid complete result | 141288 bytes; SHA256 $\texttt{30d9c04e68e337e2ac5019e527e97e211104b1e9276ff7caf24619a804fde8b9}$ |
| New semantic binding | $\texttt{f03f4892d70cdf39aceaebf8d8e9dc979196904e8ca75afbfc3d080230cb365f}$ |
| Completed raw receipt | 20106 bytes; SHA256 $\texttt{9b8c104b8cbd9d7fbe17c7e6fbddd1067c66d6a6a17252ed9c8f854b7cd2a2a7}$ |
| Temporary complete data | 2112889 bytes; SHA256 $\texttt{a7a21b4c00e306ee0278451217491aedf88c6bcb59c3ca23668198516a74a29d}$ |

The [source](../notes/2026-11-16-r150-original-joint-m-paid-full210-local-qualification-789f.py), [interface](../notes/2026-11-16-r150-original-joint-m-paid-full210-local-qualification-interface-789f.md), and [completed execution identity](../notes/2026-11-16-r150-original-joint-m-paid-full210-local-execution-789f.json) contain the precise helper pins, original-parent checks, and command line. Mathematical arrays and raw mathematical output remain temporary.

A separate actual GitHub Actions execution, run 43849025211 / job 133246502238, subsequently completed all five restore/qualification steps. Its selected original $p^9$, precision-35 parent was genuinely rebuilt in 307.279067481 wall seconds; the qualifier exited zero in 2.1683791209999868 wall seconds (2.0609094359999744 mathematical seconds). This is independent of the local full210 reuse above.

The selected-parent receipt is 27333 bytes, SHA256 `b9033b2b7c34d046f5ddda79c8a9e2e0817645167362041f284306ecda16a2e7`, with binding `0a0b38c3107add8f719b0fac0d99ec75f44c48d842b830dadb1ed1e7b1f84ce1`. The qualification receipt is 19407 bytes, SHA256 `2c72291642a379d7f01e12f9cb5d0ed5aa9ad5b0f78d6a87dea81f66499832b4`, with binding `caa18c20cf67b7314f7909f9762ea5a21ae4a1aecb205d20f9a044fb6edfbc05`.

The root's [read-only whole-log audit](../notes/2026-11-16-r150-original-joint-m-independent-log-audit-789f.js) independently reconstructs both raw receipts without float-rounding their numeric tokens, verifies both semantic bindings and every recorded original parent gate, and checks all six primary results. Removing only the temporary-data descriptor and the three explicitly local reuse fields, the complete final mathematical summaries from the two independent parents are byte-for-byte identical under sorted compact JSON with a final newline: 16834 bytes, SHA256 `c1ad1438a58e6e1dae59d90df81a6f4df160b5091fbaf7ea7710b7ade67141ff`. No mathematical arrays are added to the repository.

The remaining finite problem is to recover the coefficient torsion $S=M\cap T$, together with the parameter action and the extension $E$ in (1.2). The two actual primitive local targets now justify separate root-one and root-two carry calculations. No old complete210 computation needs to be repeated merely to establish this qualification.
