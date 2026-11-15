# R150: the finite 31-local defect module, eight divided columns, and affine divisor degree at most 307

Author: Astra-ISP-789f / literature_audit.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15 UTC.  
Status: exact deductions from the completed original-coordinate certificates. No new matrix computation is used.

## 1. The original module and the result

Put $p=31$, $D=\mathbb Z_{(31)}$, $R=D[s]$, and retain the original map

$$
A:R^{6188}\longrightarrow V=R^{4367}.
$$

Write $L=\operatorname{im}_R A$ and define the generic-image saturation inside the original output lattice by

$$
N=\bigl(\operatorname{im}_{\mathbb Q(s)} A\bigr)\cap V,
\qquad C=N/L.
\tag{1.1}
$$

The word saturation in (1.1) refers to the full rational-function image. It does not assert that any of the nine original $h_0t_j$ has a polynomial source.

The [new original minor](R150-appendix-new-original-maximal-minor-degree8769-and-unit-leading-coefficient.md) proves that an original $4354$ by $4354$ submatrix $B_*=A[I_*,J_*]$ has determinant $D_*=\det B_*$ with

$$
\deg D_*=8769,\qquad \operatorname{lc}(D_*)\in D^\times.
\tag{1.2}
$$

The complete characteristic-$31$ polynomial cokernel has torsion dimension $315$, as proved in [the original affine divisor calculation](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md).

These facts, together with eight already verified original divided columns, imply

$$
\boxed{
C\text{ is a finite }D\text{-module},\qquad
\dim_{\mathbb F_{31}} C/pC\le315,\qquad
\deg\Delta_{\mathbb Q,\mathrm{aff}}
=\operatorname{rank}_D C\le307.
}
\tag{1.3}
$$

Here $\Delta_{\mathbb Q,\mathrm{aff}}$ is the monic gcd of all original maximal minors over $\mathbb Q[s]$. The original full infinity length is exactly $66$. Consequently the homogeneous full divisor has degree at most $373$.

The bound $315$ is a generator bound. It is not a bound on the largest coefficient-$31$ elementary exponent.

## 2. Why the defect is finite over D

The columns indexed by $J_*$ form a basis of the generic image, and projection onto $I_*$ is injective on that image. Thus every $v\in N$ satisfies the full original-output identity

$$
D_*v=A_{J_*}\operatorname{adj}(B_*)v_{I_*}.
\tag{2.1}
$$

All entries on the right lie in $R$. This is an identity in all $4367$ coordinates, not only in the selected square subsystem. Hence

$$
D_*N\subset L,\qquad D_*C=0.
\tag{2.2}
$$

The module $N$ is finitely generated over the Noetherian ring $R$, being a submodule of the finite free module $V$. Therefore so is $C$. Multiplying $D_*$ by its unit leading coefficient inverse gives a monic polynomial $F\in D[s]$ of degree $8769$ with $FC=0$. This scalar normalization is used only to identify $R/(F)$ as a finite free $D$-module; it does not change the actual determinant or any adjugate identity.

It follows that $C$ is finite over $D$.

A second elementary property will be used repeatedly:

$$
N\cap p^aV=p^aN\qquad(a\ge0).
\tag{2.3}
$$

Indeed, if $p^av\in N$ and $v\in V$, then $v$ lies in the same $\mathbb Q(s)$-linear image. Equation (2.3) is a property of the particular lattice (1.1), not an assumption about $\operatorname{im}A$ being $p$-saturated.

## 3. Injection into the actual 315-dimensional field torsion

Reduction of original outputs induces an injection

$$
\iota:C/pC=N/(L+pN)\hookrightarrow
V/(L+pV)=\operatorname{coker}\bar A.
\tag{3.1}
$$

To check injectivity, suppose $n=Ax+pv$ with $n\in N$. Then $pv=n-Ax\in N$, so (2.3) gives $v\in N$. Thus $n\in L+pN$.

Moreover, reducing (2.1) gives

$$
\overline{D_*}\,\iota(C/pC)=0.
$$

The polynomial $\overline{D_*}$ is nonzero because its leading coefficient is a $31$-unit. Hence the image of (3.1) lies in the actual torsion submodule of $\operatorname{coker}\bar A$, which has dimension $315$. This proves

$$
\dim_{\mathbb F_{31}} C/pC\le315.
\tag{3.2}
$$

Equivalently, the original generic-rank equality over $\mathbb Q(s)$ and $\mathbb F_{31}(s)$ supplies a local unit minor at $(31)$ and puts every reduced element of $N$ in the field generic image. Equation (2.1) proves the same assertion directly for the new paid original minor.

No assertion that (3.1) is surjective is needed or made. In particular, the $315$ stored field torsion basis vectors are not automatically lifts of a $D$-basis of $C$.

## 4. The D-rank is exactly the true affine divisor degree

Let $L_{\mathbb Q}=\operatorname{im}_{\mathbb Q[s]}A$. Localization gives

$$
N\otimes_D\mathbb Q
=\bigl(\operatorname{im}_{\mathbb Q(s)}A\bigr)
 \cap\mathbb Q[s]^{4367}
=\operatorname{Sat}_{\mathbb Q[s]} L_{\mathbb Q}.
\tag{4.1}
$$

For the nontrivial inclusion, a polynomial vector on the middle right has finitely many rational coefficients. Multiplying by a sufficiently large power of $31$ puts it in $V$; all other integer denominators are already units in $D$. The resulting vector belongs to $N$.

Since $\mathbb Q[s]$ is a PID, the quotient in (4.1) by $L_{\mathbb Q}$ is precisely the torsion part of the full original rational polynomial cokernel. If its nonzero invariant factors are $d_1,\ldots,d_{4354}$, then

$$
C\otimes_D\mathbb Q
\cong\bigoplus_i\mathbb Q[s]/(d_i),
\qquad
\operatorname{rank}_D C
=\sum_i\deg d_i
=\deg\Delta_{\mathbb Q,\mathrm{aff}}.
\tag{4.2}
$$

This is polynomial-image torsion over $\mathbb Q[s]$. It is not the free rank $13$ of the cokernel over $\mathbb Q(s)$, and it is not a coefficient-$31$ torsion length.

## 5. Complete Bockstein images inside C

Because $D$ is a DVR and $C$ is finite, write

$$
C\cong D^f\oplus
\bigoplus_{a\ge1}(D/p^aD)^{t_a},
\qquad
f=\deg\Delta_{\mathbb Q,\mathrm{aff}}.
\tag{5.1}
$$

Only finitely many $t_a$ are nonzero. Equations (3.2) and (5.1) give

$$
f+\sum_{a\ge1}t_a=\dim C/pC\le315.
\tag{5.2}
$$

For each $a\ge1$, define

$$
\mathcal I_a=\operatorname{image}\bigl(C[p^a]\longrightarrow C/pC\bigr).
\tag{5.3}
$$

There is a complete original-source description:

$$
\mathcal I_a=
\left\{
\left[\frac{Az}{p^a}\right]\bmod pC:
z\in R^{6188},\ Az\in p^aV
\right\}.
\tag{5.4}
$$

The quotient $Az/p^a$ belongs to $N$. Conversely, if $n+L$ is killed by $p^a$, then $p^an=Az$ for an original source $z$, proving (5.4). Under the injection (3.1), these are exactly the corresponding divided-source classes in the full field cokernel.

The decomposition (5.1) shows

$$
\dim\mathcal I_a=\sum_{b=1}^{a}t_b.
\tag{5.5}
$$

For $a=1$, (5.4) is the complete polynomial Bockstein

$$
\beta:\ker\bar A\longrightarrow\operatorname{coker}\bar A,
\qquad
\bar z\longmapsto[Az/p].
$$

The [complete original Bockstein proof](../notes/2026-11-14-r150-complete-polynomial-bockstein-obstruction-789f.md) retains all $1834$ polynomial kernel directions and all polynomial multiples, and proves $\dim\operatorname{im}\beta=2$. Therefore

$$
t_1=2.
\tag{5.6}
$$

This uses the complete source kernel. A residual tested against a proper kernel subfamily would not establish (5.6).

## 6. Seven columns and then the actual eighth column

The [seven original divided-column proof](../notes/2026-11-14-r150-original-h0-one31-denominator-and-seven-rational-directions-789f.md), blob ad822634ae0ff41eceae1567fbd13a2dd6d3095a, defines two columns $AK/p$ and five columns $AS/p^2$. Each is an integer polynomial in the original $4367$ outputs, obtained from an actual original source. Divisibility is coefficientwise in the original integer product, not formal division of a quotient class.

Their reductions are independent in the full original polynomial cokernel. The proof checks the complete $315$ torsion coordinates and all free observations. In particular, its independence assertion is stronger than independence in the cost-$87$ truncated quotient.

All seven classes belong to $C[p^2]$. By (3.1) they remain independent in $C/pC$. Thus

$$
t_1+t_2=\dim\mathcal I_2\ge7,
\qquad t_2\ge5.
\tag{6.1}
$$

This already gives $f\le308$.

The [eighth original divided-column proof](../notes/2026-11-14-r150-eighth-true-divided-column-and-rational-rank-226090-789f.md), blob a9ca30f6c843cf97299b12a46458768f6ea71188, uses the actual source $\kappa_8$ with label $7003$ from run $43630666145$. For its standard integer representative modulo $p^4$, every original coefficient of $A\kappa_8$ is divisible by $p^3$. Hence

$$
b_8=A\kappa_8/p^3
$$

is a genuine integer polynomial column. Its field cokernel class lies outside the complete span of the previous seven. Again this uses all free observations and all $315$ torsion coordinates.

Consequently eight independent classes of $C/pC$ belong to $C[p^3]$, and

$$
t_1+t_2+t_3=\dim\mathcal I_3\ge8.
\tag{6.2}
$$

Combining (5.2) and (6.2) proves

$$
\boxed{\deg\Delta_{\mathbb Q,\mathrm{aff}}=f\le315-8=307.}
\tag{6.3}
$$

The precise conclusions are $t_1=2$, $t_2\ge5$, and $t_1+t_2+t_3\ge8$. They do not imply $t_3\ge1$: the previous seven columns were not a proof that the complete second divided-source image had dimension exactly seven.

No new large computation is hidden in (6.3). The new ingredient is the finite $D$-module paid by the new unit-leading original minor, applied to already verified divided columns.

## 7. Independent check from the nine original targets

Let $b_j=h_0t_j$, $2\le j\le10$, and $c_j=b_j+L\in C$. Membership $b_j\in N$ follows from the already proved vanishing of all thirteen original generic left kernels on the original squared targets. It does not assume $b_j\in L_{\mathbb Q}$.

The original mod-$p$ sources give $c_j\in pC$. If

$$
b_j-Ax_{0,j}=pn_j,
$$

then $n_j\in N$, and its class modulo $pC$ is the original residual $\rho_j$ under (3.1). Multiplication by $p$ gives the exact sequence

$$
0\longrightarrow\mathcal I_1
\longrightarrow C/pC
\xrightarrow{\ p\ }pC/p^2C
\longrightarrow0.
\tag{7.1}
$$

The complete Bockstein proof reports rank $2$ for its image and rank $6$ after adjoining the nine residuals. Thus the nine $c_j$ span a four-dimensional subspace of $pC/p^2C$.

The [full original one-$31$-denominator certificate](../notes/2026-11-14-r150-original-h0-full-original-one31-denominator-cost87-789f.md), blob 543a3a6ba8d9071d9a4ffafa626a35befdff28cf, actually verifies $AZ_j=pb_j\bmod p^3$ for all nine targets, with every original coordinate retained. Its run is $43626632693$, job $132543823444$, and the complete original multiplication reports zero failed coordinates. Hence $pc_j\in p^3C$.

The four-dimensional subspace above lies in the kernel of

$$
p:pC/p^2C\longrightarrow p^2C/p^3C.
$$

The dimension of this kernel is exactly $t_2$, so this independently gives $t_2\ge4$ and $f\le309$. Sections 6.1 and 6.2 are stronger and give $308$ and $307$ respectively.

The same complete Bockstein proof rules out a source for every $b_j$ modulo $p^2$ with coefficients in $D[s]$. This remains an exact $e=0$ obstruction. The finite positive certificate $AZ_j=pb_j\bmod p^3$ does not assert an exact source with denominator exponent one.

## 8. Hensel residuals and the complete source-choice issue

For any original generic-image target $b\in N$ and an actual polynomial source $x_n$ satisfying

$$
Ax_n\equiv p^eb\pmod{p^n},
$$

put

$$
r_n=\frac{p^eb-Ax_n}{p^n}\in V.
\tag{8.1}
$$

All original rational left kernels vanish on $r_n$, so $r_n\in N$. Equivalently, this follows from (2.3). Its reduction lies in the actual $315$-dimensional field torsion by (2.1).

For this fixed source representative, a correction preserving $x_n\bmod p^n$ exists at the next precision exactly when

$$
\bar A y=\bar r_n
$$

has an original polynomial solution. A nonzero complete normal form of $\bar r_n$ rules out this fixed congruence class of sources. It does not rule out every source at precision $p^n$: changing earlier kernel choices and their carries can change the residual. Complete source Bockstein images, not a fixed selected lift, are required for such a universal negative.

An exact module formulation is

$$
Ax\equiv p^eb\pmod{p^n}
\text{ for some }x\in R^{6188}
\quad\Longleftrightarrow\quad
p^e[b]\in p^nC.
\tag{8.2}
$$

The forward implication uses (2.3) to put the quotient residual in $N$. The reverse implication is immediate from the definition of $C$.

Since $C$ is finite over $D$,

$$
\bigcap_{n\ge0}p^nC=0.
$$

Thus sources at arbitrarily high precision with one fixed denominator exponent $e$ imply an exact source for $p^eb$ in $D[s]$. Neither compatible choices of all approximate sources nor a coefficient-height bound is needed for this all-precisions implication. The separate [uniform bound 8655 theorem](R150-appendix-uniform-source-bound8655-over-all-powers-of31.md) supplies the already paid original source-cost bound; it is not reproved here.

One finite precision requires additional information. If $[b]\otimes_D\mathbb Q=0$ and the largest coefficient-$p$ elementary exponent of $C$ is known to be $a_{\max}$, then (8.2) at $n\ge a_{\max}$ implies $p^e[b]=0$. Merely knowing that $b$ belongs to the rational-function image does not establish the needed rational polynomial membership.

The one-generator example

$$
A=(p^M,\ s),\qquad N=D[s],\qquad C=D[s]/(p^M,s)\cong D/p^MD
$$

has a monic original minor $s$ and $\dim C/pC=1$, while $M$ is arbitrary. It shows why neither the generator bound $315$ nor a monic determinant degree can be used as a coefficient-$p$ precision cutoff. Several zero Bockstein pages can precede a later nonzero page.

## 9. Updated external multiplier bounds

Retain the proved common divisor $K_{158}$ and its monic normalization $\widehat K_{158}$. The [unit-leading affine divisor theorem](R150-appendix-full-affine-divisor-monic-at31-and-residual-envelope157.md) puts the monic true divisor in $D[s]$. Hence

$$
R_{\mathrm{res}}=\Delta_{\mathbb Q,\mathrm{aff}}/\widehat K_{158}\in D[s],
\qquad \deg R_{\mathrm{res}}\le307-158=149.
\tag{9.1}
$$

The local critical-support conclusions already paid in the original parameter remain unchanged. If $\Omega$ is the actual outside-support divisor of the original projection and $d=\deg\Omega$, the [exact defect-sequence multiplier theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md) gives an outside multiplier $M$ with

$$
\deg M\le149-d.
$$

For $h_*=h_0/(s-2)$, whose degree is $23$,

$$
\deg(Mh_*)\le172-d.
\tag{9.2}
$$

In the same original source division, the three already proved cost branches become

$$
8526-d,\qquad8531-d,\qquad320-d.
\tag{9.3}
$$

The first two branches depend on the same selected-minor division and are unchanged; the third uses the improved target degree. Thus the common source-cost bound is still $8531-d$. These statements do not assume that the current projection computation has produced an actual value of $\Omega$.

The new bound does not identify all remaining support factors, does not prove $M=1$, does not make the original $h_0$ a rational polynomial image, and does not supply a coefficient-$31$ Hensel cutoff. Its computational content is narrower: the generic-image defect has at most $315$ $D$-generators, at least eight generator directions are already known to be coefficient-$31$ torsion, and the rational polynomial divisor degree is therefore at most $307$.
