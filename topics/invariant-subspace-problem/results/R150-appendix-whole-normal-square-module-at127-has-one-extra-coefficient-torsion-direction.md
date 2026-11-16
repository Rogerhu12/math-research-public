# R150: the whole normal-square module at 127 has one extra coefficient-torsion direction

Author: Astra-ISP-789f / literature_audit, root.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Exact original-module conclusion

Put
$$
p=127,\qquad D=\mathbb Z_{(127)},\qquad R=D[s],\qquad k=\mathbb F_{127}.
$$
Retain the original primitive integer seventeen-equation matrix, all degree-at-most-three source multipliers, and all positive-degree-at-most-five outputs:
$$
A:R^{6188}\longrightarrow V=R^{4367},\qquad L=\operatorname{im}A.
$$
The original binomial coordinates are
$$
z_j=\sum_{a=0}^j\binom ja(-s)^{j-a}m_a,\qquad c=z_0,\quad d=z_1.
$$
Let $W\subset V$ be the coordinate summand spanned by all ordinary monomials of degree at most five with at least two factors among $z_2,\ldots,z_{10}$. Thus $\operatorname{rank}_R W=4212$. Write
$$
U=(W+L)/L\simeq W/(L\cap W),\qquad
M=\sum_{j=2}^{10}R[t_j],\qquad t_j=z_j^2.
$$
The original polynomial and its monic associate are
$$
h_*=s^3F_+^2F_-^2E_8,\qquad h=h_*/3125.
$$
The new complete original projection calculation proves
$$
\boxed{U=M\oplus T,\qquad T\simeq R/(127,s+64).}
\tag{1.1}
$$
Here $T$ is the unique coefficient-127 torsion submodule of the original finite carrier defined in §2. It is nonzero. The nine original squares generate $M$, a free $D$-module of rank 25, and miss exactly this additional direction of the whole $W$ image.

In particular,
$$
\boxed{\operatorname{Ann}_R U=h(127,s+64)=h_*(127,s+64).}
\tag{1.2}
$$
For every polynomial $q\in D[s]$ this gives the exact whole-source test
$$
\boxed{
h_*qW\subseteq L
\quad\Longleftrightarrow\quad
q(63)\equiv0\pmod{127}.
}
\tag{1.3}
$$
Consequently
$$
h_*W\nsubseteq L,\qquad
127h_*W\subseteq L,\qquad
(s+64)h_*W\subseteq L.
\tag{1.4}
$$
The least coefficient-prime exponent that clears $h_*W$ is exactly one. All nine individual $h_*t_j$ already have sources over $D[s]$; the nonzero direction in (1.4) is a property of the whole normal-square summand.

These are existence and exclusion statements for the unchanged original source module. No expanded family of 4212 sources or new source-degree bound is supplied by this calculation.

## 2. The previously established finite carrier and a true parameter projector

Define, inside the original rational generic output space,
$$
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,
\qquad C=N/L,
\qquad T=C[p^\infty].
$$
The [unique coefficient-127 torsion theorem](R150-appendix-unique-coefficient127-torsion-and-integral-nine-square-sources.md), §§2–4, proves all of the following for this same original matrix:

- $N\cap pV=pN$, and $C$ is finite over $D$;
- $T\simeq k[s]/(s+64)$ and $pT=0$;
- the free quotient has $D$-rank 298;
- the full monic rational affine divisor $\Delta\in D[s]$ has degree 298 and $\overline\Delta(63)=79$.

The full rational affine divisor is
$$
\Delta=\operatorname{mon}\!\left(s^{66}(s-2)^{12}(s+6)^{12}F_+^8F_-^8E_8^5\right)\Omega,
\qquad\deg\Omega=120.
$$
It annihilates the free quotient $C/T$. Since $a=\Delta(63)$ is a $D$-unit, the actual parameter endomorphism
$$
e=a^{-1}\Delta(s):C\longrightarrow C
$$
has image in $T$ and restricts to the identity on $T$. Therefore
$$
e^2=e,\qquad C=T\oplus F,\qquad F=\ker e,
\tag{2.1}
$$
as $R$-modules, where $F$ is finite free over $D$. This is a genuine polynomial-in-$s$ projector on the whole carrier, not a choice of a vector-space complement after reduction.

The [complete relative-module theorem](R150-appendix-zero-projection61-and-complete-relative-nine-target-module25.md), §§5–6, proves
$$
h_*M=0,\qquad M\cap T=0,\qquad
\operatorname{rank}_D M=25,
$$
and the actual reduction map $M/pM\to C/pC$ has image dimension 25 and is injective. Its rationalization is the whole rational relative module:
$$
M\otimes_D\mathbb Q=U\otimes_D\mathbb Q.
\tag{2.2}
$$
The integer evaluation $h_*(63)\equiv44\pmod{127}$ makes $h_*$ invertible on $T$. Since $h_*$ kills $M$ and $e$ commutes with it, $eM=0$. Thus $M\subset F$.

## 3. Why only the one torsion direction could be missing

Injectivity of $M/pM\to C/pC$ gives
$$
M\cap pC=pM.
$$
Hence $M$ is saturated in the free $D$-module $F$: if $pf\in M$ for $f\in F$, write $pf=pm$ with $m\in M$ and cancel $p$ in $F$. Iterating this argument yields
$$
F\cap(M\otimes_D\mathbb Q)=M.
\tag{3.1}
$$

The original generic-image theorem gives $W\subset N$, so $M\subset U\subset C$. For $u\in U$, equations (2.2) and (3.1) imply
$$
(1-e)u\in M.
$$
Therefore $eu=u-(1-e)u\in U\cap T$. The two summands intersect trivially and both belong to $U$, proving the exact reduction
$$
\boxed{U=M\oplus(U\cap T).}
\tag{3.2}
$$
Since $T$ is simple, the remaining question is whether $U\cap T$ is zero or all of $T$. No unproved lifting of a field-generated lattice is used in this reduction.

## 4. The small matrix retains all original sources

Let
$$
\pi:V\longrightarrow V/W\simeq R^{155},\qquad P=\pi A.
$$
The 155 projected outputs are the 20 pure $c,d$ monomials and 135 monomials containing exactly one $z_j$, $2\le j\le10$. The binomial change and its induced changes in every source degree are polynomial units: the eleven-coordinate matrix is lower triangular with diagonal one and has inverse obtained by replacing $s$ by $-s$.

The new source reconstructs the original whole-polynomial physical equations using the pinned polynomial core. Separately, it reads the original primitive integer equations, with all seventeen rows and all 77 ordinary linear/quadratic moment monomials, evaluates their 4382 stored integer coefficients at $s=63$ modulo 127, and applies the binomial change directly.

The fixed denominator and all seventeen primitive contents are verified to be units modulo 127. Every one of the 476 physical pure/one-normal coefficient polynomials has a unit denominator, and all 476 physical/primitive coefficient comparisons pass with the actual row scales. Ordinary quadratic diagonal terms and off-diagonal terms are expanded by ordinary polynomial multiplication; no divided-power convention is substituted.

Every one of the 364 multiplier monomials of degree at most three is then applied to each of the seventeen equations. The source counts by normal degree are
$$
(170,918,2295,2805),\qquad 170+918+2295+2805=6188.
$$
The entire resulting $6188\times155$ projected matrix is constructed. In particular, all 5100 rows of source normal degree at least two are actually checked to have zero projection.

The independent 224-row compression has the 170 original pure-multiplier rows and 54 rows with the genuine factor
$$
g(s)=-2s^2(s-2)(s+6).
$$
At the present point its value is $g(63)=118$ in $k$. The source checks both inclusions of row modules:

- all 170 pure rows agree with their original primitive rows after the fixed unit row scale;
- every one of the 918 original one-normal rows is the computed multiple of its retained $g$ row;
- each of the 54 retained $g$ rows is reconstructed as the actual original constant linear combination supplied by $J_2^{-1}/4$.

Thus no source is omitted and no true $g$ row is replaced by a bare unit without an original-source identity. The full and compressed ranks are subsequently computed independently.

## 5. Actual rank 142 and the original local exact sequence

The actual field calculation gives
$$
\boxed{\operatorname{rank}_k P(63)=142.}
\tag{5.1}
$$
Both the full $6188\times155$ projected matrix and its $224\times155$ compression have this rank. A selected $142\times142$ minor of the binomially transported original-source rows and projected output columns has determinant 97 in $k$. Each source row is an original equation times a comoving monomial; the full source-basis change is the degree-preserving polynomial unit described in §4. The claim does not identify these transported row labels with the untransformed raw moment-monomial labels.

The complete thirteen-dimensional point kernel is retained in the original 155 output coordinates, with its free-coordinate block equal to $I_{13}$. All
$$
6188\cdot13=80444
$$
original source/kernel products are verified to be zero. The unit minor gives the lower rank bound; the full kernel gives the matching upper bound.

Now localize $R$ at
$$
\mathfrak m=(127,s-63).
$$
The actual minor is a unit in $R_{\mathfrak m}$. The independently paid rational generic rank of this same original $P$ is 142. Eliminating the unit block leaves a Schur block which is zero over $\mathbb Q(s)$ and therefore zero over the domain $R_{\mathfrak m}$. Consequently
$$
\operatorname{coker}P_{\mathfrak m}\simeq R_{\mathfrak m}^{13}.
\tag{5.2}
$$

The original projection, before and after localization, has the exact sequence
$$
0\longrightarrow U\longrightarrow V/L
\longrightarrow (V/W)/\pi L\longrightarrow0.
\tag{5.3}
$$
Because $\Delta(63)$ is a unit, equation (2.1) gives
$$
C_{\mathfrak m}=T_{\mathfrak m}=T.
$$
Its image in the free module (5.2) must vanish: $T$ is killed by 127, while $R_{\mathfrak m}^{13}$ has no such torsion. Exactness of (5.3) therefore gives
$$
T\subseteq U_{\mathfrak m}.
$$
The submodule $U\cap T$ is either zero or the simple module $T$, which is entirely supported at $\mathfrak m$. Its localization is nonzero, hence $U\cap T=T$. Together with (3.2), this proves (1.1).

As a separate pointwise consistency check, the complete original field cokernel has a unique simple $s+64$ primary and generic free rank thirteen. Thus $\operatorname{rank}\bar A(63)=4353$. In the very same original output decomposition,
$$
\dim_k\frac{W(63)+\operatorname{im}\bar A(63)}{\operatorname{im}\bar A(63)}
=4212+\operatorname{rank}\bar P(63)-4353=1.
$$
The local-unit argument above, including $\Delta(63)$ being a unit, is what identifies this point direction with the whole coefficient torsion. A specialization of an intersection of images is not being assumed.

## 6. Exact annihilator and source multipliers

Every individual original target has exact annihilator $(h)$ over $D[s]$, by the original integral cyclic-module theorem. Therefore $\operatorname{Ann}_R M=(h)$. Equation (1.1) gives
$$
\operatorname{Ann}_R U=(h)\cap(127,s+64).
$$
The image of $h$ in $R/(127,s+64)$ is $55\ne0$. Hence the two ideals are comaximal, and
$$
(h)\cap(127,s+64)=h(127,s+64).
$$
This proves (1.2). Since $3125$ is a unit, using $h_*$ instead of $h$ gives the same ideal.

More directly, $h_*U=h_*T=T$. Thus $h_*q$ kills the full relative image exactly when $q$ kills $T$. The latter condition is $q(63)=0$ in $k$, proving (1.3) and (1.4).

In particular, there is at least one ordinary basis monomial $w$ of $W$ for which $h_*w$ has no original source over $D[s]$. Otherwise all its basis monomials would be killed and $h_*U$ would be zero. No specific basis monomial is selected by the present positive-rank calculation.

## 7. Full integral parameter structure and generator count

The [exact rational invariant-factor theorem](R150-appendix-zero-relative-target-partition-three-one-one-and-global-invariant-factors.md) gives
$$
M\otimes_D\mathbb Q\simeq
\mathbb Q[s]/(s)\oplus\mathbb Q[s]/(s)\oplus\mathbb Q[s]/(h).
$$
This also gives an integral splitting in the present 127 lattice. Indeed, choose the original cyclic module $M_2=R[t_2]\simeq R/(h)$. Its reduction has its complete dimension 23 in $C/pC$, so it is saturated in $M$. Hence $M/M_2$ is free of $D$-rank two.

The rational dimensions of $sM$ and $sM_2$ are both 22, and the latter is contained in the former. Thus their rationalizations agree. Moreover
$$
M_2/sM_2\simeq D,
$$
because $h(0)=0$. Saturation first gives $sv\in M_2$ for every $v\in M$, and then gives $sv\in sM_2$. Each of two $D$-basis lifts of $M/M_2$ can therefore be changed by an element of $M_2$ to become exactly killed by $s$. This proves
$$
M\simeq R/(s)\oplus R/(s)\oplus R/(h).
$$
Consequently the whole relative module has the exact, noncanonical structure
$$
\boxed{
U\simeq R/(s)\oplus R/(s)\oplus R/(h)\oplus R/(127,s+64).
}
\tag{7.1}
$$
Its $D$-module structure is $D^{25}\oplus D/(127)$, so its least number of $D$ generators is 26. Its least number of $R$ generators is three: reduction at $(127,s)$ requires three, while the comaximal last two summands in (7.1) combine into the cyclic module $R/(h(127,s+64))$.

The same primitivity argument shows that $U/pU\to C/pC$ is injective. Thus the complete parameter-stable field image of the whole $W$ has dimension 26 and characteristic polynomial
$$
s^2\operatorname{mon}(\bar h_*)(s+64).
$$
The already paid field image of the nine squares has dimension 25. The additional factor is exactly the original coefficient-prime direction proved in §5.

## 8. Execution identity and scope

The new original projection source is
[2026-11-16-r150-original-whole-w-prime127-root63-projection-789f.py](../notes/2026-11-16-r150-original-whole-w-prime127-root63-projection-789f.py),
18570 bytes, SHA256
$\texttt{6a80e5a873320a4794ce8c61572b0b828c53fdf6a92b51b11265bd7f23d82ae5}$.

It was actually executed in an isolated local directory on 2026-11-16, with a 90-second and 768-MiB bound. It exited zero after 0.884472256 seconds; peak resident memory was 45440 KiB. The [execution-completion identity](../notes/2026-11-16-r150-original-whole-w-prime127-root63-local-execution-789f.json) records the complete CLI, all input pins and temporary-output identities without storing mathematical arrays in the repository.

| Item | Actual identity or result |
|---|---|
| Raw receipt | 3208 bytes |
| Raw SHA256 | 041d65424636c7db5539bc7b0b3b1b4003642f07e82af55266505ea4edf3de2b |
| Semantic binding | 44668fb72622a562436ea84dad1c82d9a6cbd78db08b2def3ae85ce77947822b |
| Temporary point data | 125275 bytes |
| Temporary data SHA256 | 0795447edab5684100db0d3b82a08446b2059737a5a4c8ba8a55b204642114ad |
| Whole projected matrix logical SHA256 | 1cbf98064363de984e41040e2495acb8bc2355d9177e4712227789b57f56dac7 |
| Complete projected ranks | 142 on both source representations |
| Actual original minor determinant | 97 modulo 127 |
| All original point-kernel products | 80444, all zero |

The two old helpers are used with their unchanged paid bytes: the whole-polynomial core has SHA256 $\texttt{727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb}$, and the original physical generator has SHA256 $\texttt{2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186}$. The primitive compressed file and its entire decoded payload are independently hashed before any arithmetic.

The result closes the whole-$W$ integral qualification at the coefficient prime 127. It does not change the coefficient prime in the separate 31-integral source-cost theorems, nor remove the normalized rank-one family from the original unrestricted Bell or invariant-subspace problem.

## 9. Independent reconstruction of every original projected row

The [root quadratic-form audit](../notes/2026-11-16-r150-original-whole-w127-independent-quadratic-form-audit-789f.py) does not import the producer's polynomial core, row compression, or custom elimination. It starts from the complete primitive integer equations and represents each ordinary quadratic polynomial by a symmetric matrix, using one half of each off-diagonal coefficient. The congruence $T^{\mathsf T}QT$, together with the independent linear transformation, reconstructs the original binomial coefficients. It then constructs every one of the 6188 projected source rows. Both complete dictionaries and every projected matrix coefficient have exactly the original logical SHA256.

An independent FLINT calculation gives rank 142 for both the full and compressed matrices, rank 13 for the complete kernel, and zero for all full and compressed kernel products. The selected actual source-row minor is rebuilt from the primitive equations and has determinant 97. This small verification completed in 0.509557548 seconds. Its source is 5315 bytes, SHA256 `21b6335ba1441635f5f4ca4c14a9aee3ec9caba0fa40145e0da9e0c4b73193b5`; its temporary receipt is 1012 bytes, SHA256 `82db385e50f4a3300aafd7d629762ede4fc490f541f4b7dd0f87ae5440c37648`. The [execution identity](../notes/2026-11-16-r150-original-whole-w127-independent-quadratic-form-execution-789f.json) preserves those pins without storing mathematical arrays. It does not repeat the full original $4367\times6188$ elimination.
