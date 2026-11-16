# R150: the unique coefficient-127 torsion direction and exact integral sources for the nine squares

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Conclusion on the finite original carrier

Put
$$
p=127,\qquad D=\mathbb Z_{(127)},\qquad k=\mathbb F_{127}.
$$
Use the original primitive integer seventeen-equation matrix
$$
A:D[s]^{6188}\longrightarrow V=D[s]^{4367}
$$
and define
$$
L=\operatorname{im}A,\qquad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\qquad
C=N/L,\qquad T=C[p^\infty].
\tag{1.1}
$$
The finite carrier here is $C$, not the full cokernel $V/L$, which has thirteen free $\mathbb Q[s]$ directions.

The now completed original evidence implies
$$
\boxed{
T\simeq D/(127)\quad\text{as a }D\text{-module},\qquad
T\simeq k[s]/(s+64)\quad\text{as a }D[s]\text{-module}.
}
\tag{1.2}
$$
In particular, there is exactly one coefficient-127 torsion cyclic summand, and its exponent is exactly one. No coefficient-127 torsion summand of exponent two or higher remains.

For the original targets
$$
t_j=\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,\qquad 2\le j\le10,
$$
and the unchanged original polynomial
$$
h_*=s^3F_+^2F_-^2E_8,
$$
one obtains genuine integral-localized original sources
$$
\boxed{
Az^{(j)}=h_*t_j,\qquad z^{(j)}\in D[s]^{6188}
\quad(2\le j\le10).
}
\tag{1.3}
$$
The coefficients of these sources may have denominators prime to 127. This is not an assertion that they lie in $\mathbb Z[s]$, that their denominators are powers of 31, or that a corresponding statement holds over $\mathbb Z_{(31)}$.

Moreover every individual target has the exact same rational minimal annihilator:
$$
\boxed{
\operatorname{ann}_{\mathbb Q[s]}([t_j])
=\bigl(\operatorname{mon}(h_*)\bigr),
\qquad j=2,\ldots,10.
}
\tag{1.4}
$$
The proof below gives the stronger individual cyclic-module identification over $D$.

## 2. Finiteness and saturation are original-source statements

The [complete original infinity qualification at 127](R150-appendix-complete-original-infinity-prime127-spectrum66-and-affine-gauss-bound299.md) proves the same full rational and field infinity length 66. It supplies an original maximal minor $d(s)$ whose leading coefficient is a unit of $D$.

For any $v\in N$, the original adjugate identity on that minor gives $d\,v\in L$. The identity holds on all original output rows: the chosen output restriction is injective on the rational generic image. Thus $dC=0$. After dividing by its unit leading constant, $d$ is monic, so $C$ is a finite $D$-module.

The submodule $N$ is $p$-saturated in $V$:
$$
N\cap pV=pN.
\tag{2.1}
$$
Indeed, if $pv\in N$ and $v\in V$, then $pv$ belongs to the rational generic image. Division by the nonzero rational scalar $p$ keeps $v$ in that image, so $v\in N$.

After tensoring with $\mathbb Q$, $C\otimes_D\mathbb Q$ is the torsion part of the original rational polynomial cokernel. Consequently
$$
\operatorname{rank}_D C=\deg\Delta_{\rm aff}.
\tag{2.2}
$$
This is the original affine determinantal divisor, not the selected order-243 determinant.

The [completed rational divisor and source theorem](R150-appendix-exact-affine-divisor298-unmultiplied-nine-sources-and-rank-one-bell16.md) now gives
$$
\Delta_{\rm aff}=\operatorname{mon}(K_{178})\Omega,\qquad
\deg\Delta_{\rm aff}=298.
\tag{2.3}
$$
All these statements concern the same $A,N,L$.

## 3. One cyclic factor, then exponent exactly one

The [exact quotient-defect calculation](R150-appendix-exact-external-reduction127-and-zero-quotient-defect.md) proves $J_{127}=0$. Its precise role is to identify the reduction of the finite carrier:
$$
C/pC\simeq\operatorname{Tor}_{k[s]}(\operatorname{coker}\bar A).
$$
The [complete original affine computation](R150-appendix-original127-first-coefficient-torsion-at63-and-affine-degree298.md), §1, gives
$$
\dim_k C/pC=299
$$
and its full characteristic polynomial
$$
\chi_{299}
=s^{66}(s-2)^{12}(s+6)^{12}
\widehat F_+^8\widehat F_-^8\widehat E_8^5
(s+64)\Psi_{60}^2.
\tag{3.1}
$$
The $s+64$ primary has dimension one.

Let $F=C/T$. This is finite torsion-free over the DVR $D$, hence free. Reduction gives
$$
0\longrightarrow T/pT\longrightarrow C/pC
\longrightarrow F/pF\longrightarrow0.
\tag{3.2}
$$
By (2.2)–(2.3), $\dim_k F/pF=298$. Therefore
$$
\dim_k(T/pT)=299-298=1.
\tag{3.3}
$$

For clarity, (3.3) counts cyclic coefficient-prime torsion factors. It does not by itself give their $p$-adic length. In general,
$$
C\simeq D^{298}\oplus\bigoplus_{i=1}^{r}D/(p^{a_i})
\quad\Longrightarrow\quad
\dim_k C/pC=298+r.
$$
Here $r=1$, but the exponent would still be unknown without the next original certificate.

The [root63 global-source Bockstein](R150-appendix-original127-first-coefficient-torsion-at63-and-affine-degree298.md) constructs a genuine integer polynomial source $y(s)$ from the complete original source DAG such that $Ay$ is coefficientwise divisible by $p$. Its divided class
$$
[Ay/p]\in C[p]
$$
has nonzero image in $C/pC$ on the simple $s+64$ primary. The separately reconstructed original source and all 4367 original products modulo $p^2$ verify the detector value 40.

Define the exact first image
$$
I_1=\operatorname{im}\bigl(C[p]\longrightarrow C/pC\bigr).
$$
For one summand $D/(p^a)$ this reduction image is one-dimensional when $a=1$ and zero when $a\ge2$. The actual root63 result gives $\dim_k I_1\ge1$. Together with (3.3), it follows that the only cyclic factor has $a=1$.

Thus $pT=0$ and $I_1=T/pT=T$ has dimension one. Its $s$ action is the already detected action $s=63$; equivalently its monic annihilator over $k[s]$ is $s+64$. This proves (1.2).

The later generalized computations with zero first image on critical primaries are compatible with this conclusion. Taken alone, those zero-image computations would not exclude higher coefficient-prime exponents. Their exclusion here uses the independently completed rational degree equality (2.3) and the nonzero root63 certificate.

## 4. An optional original-parameter splitting

The monic polynomial $\Delta_{\rm aff}$ belongs to $D[s]$ by the already paid unit-leading Gauss argument. Multiplication by $s$ on the free module $F$ has characteristic polynomial $\Delta_{\rm aff}$, so
$$
\Delta_{\rm aff}(s)F=0.
$$
The root polynomial audit gives
$$
\overline{\Delta_{\rm aff}}(63)=\chi_{299}'(63)=79\ne0.
$$
Hence $u=\Delta_{\rm aff}(63)$ is a unit of $D$.

The $D[s]$-linear endomorphism
$$
e=u^{-1}\Delta_{\rm aff}(s):C\longrightarrow C
$$
takes values in $T$ and is the identity on $T$. Therefore $e^2=e$ and
$$
C=T\oplus\ker e
$$
as $D[s]$-modules, with $\ker e$ finite free of $D$-rank 298. The statement $C\simeq D^{298}\oplus D/(p)$ in §3 alone was only a $D$-module statement; this explicit projector explains the stronger parameter-stable splitting.

No matrix for this 298-dimensional summand is constructed by this appendix.

## 5. From rational and field sources to exact D-localized sources

The original nine squares belong to the rational generic image: they are in the normal-degree-at-least-two summand $W$, whose generic image inclusion was proved in the [original projection-divisor theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md). Thus their original integral vectors belong to $N$.

Fix $j$ and put $b=h_*t_j$. The new rational membership theorem gives
$$
b\in L\otimes_D\mathbb Q,
$$
so its class $[b]\in C$ belongs to $T$.

Independently, the [complete original target calculation at 127](R150-appendix-original127-nine-target-module-twentyfive-and-minimal-hstar.md) proves
$$
\bar b\in\operatorname{im}_{k[s]}\bar A.
\tag{5.1}
$$
It retains the original 6188 sources, the complete free-tail constraints, and the actual nine original target labels. In particular, (5.1) is not a point evaluation.

Choose any polynomial lift $x\in D[s]^{6188}$ of a source in (5.1). Then
$$
b-Ax=pv,\qquad v\in V.
$$
Both $b$ and $Ax$ lie in $N$, so (2.1) gives $v\in N$. Therefore
$$
[b]=p[v]\in pC.
$$
For every finite $D$-module with torsion part $T$ and free quotient $F$,
$$
T\cap pC=pT.
\tag{5.2}
$$
Indeed, if $pc\in T$, then $p(c+T)=0$ in the torsion-free module $F$, so $c\in T$.

Here $pT=0$ by (1.2). Thus $[b]\in T\cap pC=0$, proving (1.3). The same conclusion for $h_0t_j$ follows by multiplication by $s-2$.

This proof uses three distinct inputs: rational polynomial membership, full field polynomial membership, and the exact exponent-one coefficient-prime structure. A field zero without the other two inputs would not justify the conclusion.

## 6. Exact individual cyclic modules and minimality of h*

Write
$$
m_*=\operatorname{mon}(h_*)=h_*/3125\in D[s].
$$
It is monic of degree 23 because 3125 is a unit in $D$.

The original integer evaluations at 63 are
$$
\overline F_+(63)=112,\qquad
\overline F_-(63)=100,\qquad
\overline E_8(63)=77,\qquad
\overline h_*(63)=44\ne0.
\tag{6.1}
$$
The [independent exact-integer cross-audit](../notes/2026-11-16-r150-original-hstar-at63-exact-integer-cross-audit-789f.json) reconstructs all 24 integer coefficients from the three original factor arrays and matches the paid coefficient file byte-for-byte at the coefficient level. Integer Horner evaluation and the factored evaluation both give
$$
h_*(63)=1630159488059100357895588625989620223385900352.
$$
Its reduction is 44. The original leading coefficient has residue $3125\bmod127=77$, whose inverse is 33; the monic normalization is therefore a $D$-unit normalization.

Thus multiplication by $h_*$ is a unit on the one-dimensional module $T$.

For each individual original target define
$$
M_j=D[s]\,[t_j]\subset C.
$$
Equation (1.3) makes $M_j$ a quotient of the finite free $D$-module $D[s]/(m_*)$, of rank 23. Its torsion is contained in $T$, while $h_*$ kills it. By (6.1), $M_j\cap T=0$. Hence $M_j$ is itself finite free over $D$, with rank at most 23.

Its image in $C/pC$ is exactly the cyclic module generated by the original field target. The actual [single-target Krylov checks](R150-appendix-original127-nine-target-module-twentyfive-and-minimal-hstar.md), §4, give dimension 23 for each of the nine original labels. Therefore
$$
23\le\dim_k M_j/pM_j=\operatorname{rank}_D M_j\le23.
$$
The natural surjection
$$
D[s]/(m_*)\longrightarrow M_j
$$
is now between free $D$-modules of the same finite rank. Its kernel is a submodule of a free module and has rank zero, so it is zero. Consequently
$$
\boxed{M_j\simeq D[s]/(m_*),\qquad j=2,\ldots,10.}
\tag{6.2}
$$
Reduction also shows that each individual cyclic module embeds with its complete 23-dimensional reduction in $C/pC$.

Tensoring (6.2) with $\mathbb Q$ proves (1.4). The common rational annihilator of all nine targets is therefore also exactly $m_*$. In particular, the exact rational local exponents of every individual target are three at $s=0$, two at $F_+$ and $F_-$, one at $E_8$, and zero at the other finite factors.

The complete field joint module has dimension 25, but this appendix does not infer a rational joint dimension merely by copying that number. The individual cyclic identifications and the common annihilator suffice for the present conclusion.

## 7. Evidence and source-cost boundaries

The root63 positive source has the following actual pins:

| Object | Actual value |
|---|---|
| Run and step | 43772109844 / original127-root63-global-source-bockstein180 |
| Global source node | 26969742 |
| Original input raw ID | 3463 |
| Nonzero divided detector | 40 |
| Original source support at 63 | 4324 |
| Full original output product | all 4367 coordinates modulo $127^2$ |
| Raw receipt | 12445 bytes |
| Raw SHA256 | 2a7dd4da8014b5f0e5d29e5566b90ebe667c82243f435755ef65cdf317eed4a8 |

The completed nine-target calculation has:

| Object | Actual value |
|---|---|
| Run and step | 43772109844 / original127-complete-nine-target-cyclic60 |
| Complete original joint field module | dimension 25 |
| Every original individual cyclic module | dimension 23 |
| Common field annihilator | $\operatorname{mon}(\bar h_*)$ |
| All nine original $h_*$ actions | zero |
| Raw receipt | 20892 bytes |
| Raw SHA256 | 60229e78fc6cc18fb873d17fc974f9a4c9a20b0eca6ca060901891da6bfce7c0 |

Its original target-coordinate and action gates include all 7245 finite-window products, 7475 intertwining products, and 2691 target-span coordinates. The [published actual receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-nine-target-cyclic60.json) and its source/parameter hashes retain those original identities.

The new [rational source bound 8391](R150-appendix-exact-affine-divisor298-unmultiplied-nine-sources-and-rank-one-bell16.md), §§5–6, applies over $\mathbb Q[s]$. The uniform bound 8515 there concerns already existing solutions over $\mathbb Z_{(31)}$ or its finite quotients. Neither number is newly asserted as a bounded-denominator $\mathbb Z_{(127)}$ source bound here. Equation (1.3) is an exact polynomial-source existence result; its expanded coefficients and an integral-localized degree-reduction implementation have not been computed.

The remaining coefficient-31 torsion and the unrestricted non-rank-one Jacobian problem are separate. This coefficient-127 closure does not alter their primes, source lattices, or unresolved hypotheses.
