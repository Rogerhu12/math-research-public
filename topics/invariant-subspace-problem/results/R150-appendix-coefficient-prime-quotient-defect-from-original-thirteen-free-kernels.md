# R150 appendix: the coefficient-prime quotient defect from the original thirteen free kernels

Author: AI (ChatGPT / literature_audit), 2026-11-15 UTC.

## 1. The original module and the exact object to compute

Put $D=\mathbb Z_{(31)}$, $p=31$, $R=D[s]$, and $k=\mathbb F_{31}$. Let $A$ be the original $4367$ by $6188$ seventeen-equation source matrix, let $V=R^{4367}$, and put

$$
L=\operatorname{im}_R A,\qquad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\qquad
C=N/L,\qquad G=V/N.
$$

The intersection defining $N$ is taken in $\mathbb Q(s)^{4367}$. We use the already proved full generic rank $4354$; therefore $G$ has rank $13$ over $R$. The finite-$D$ carrier theorem and its completed root-$2$ refinement give

$$
0\longrightarrow C/pC\longrightarrow\operatorname{coker}\overline A
 \longrightarrow G/pG\longrightarrow0.
\tag{1.1}
$$

The additional finite $k[s]$-module in that theorem is

$$
J=\operatorname{Tor}_{k[s]}(G/pG).
$$

This appendix identifies a much smaller exact presentation that determines the characteristic polynomial of $J$. It does not assign a numerical length to $J$ before the computation.

References: [the finite carrier](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md), [the root-$2$ coefficient spectrum and three-term budget](R150-appendix-root2-coefficient31-spectrum-through-five-and-affine-degree300.md), and [the original projection and its complete polynomial free kernels](R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md).

## 2. Why these are the full original free kernels

Use the original binomial change from the eleven physical moments to the co-moving coordinates $(c,d,n_2,\ldots,n_{10})$. On each bounded moment degree this change is triangular with diagonal $1$, so both directions are defined over $R$. Let

$$
\pi:V\longrightarrow R^{155}
$$

be the coordinate projection onto the twenty pure tangent and $135$ one-normal target coordinates. In particular, $\pi$ is surjective over $R$, without division by a parameter polynomial.

The paid original projection $P$ has $224$ rows: the $170$ pure-multiplier original rows and the $54$ actual $g(s)$ rows representing all $918$ one-normal sources. Those rows retain $g(s)$ itself. The other $5100$ original sources project to zero by exact support. The paid polynomial kernel matrix

$$
Q\in\mathbb Q[s]^{155\times13}
$$

satisfies all $224\cdot13=2912$ original projected equations. Its thirteen specified pure-coordinate rows form

$$
D_{\rm lin}(s)^2 I_{13},
\qquad
D_{\rm lin}
=s^8(s-2)^2(s+6)^2F_+^3F_-^3E_8^2.
\tag{2.1}
$$

The theorem below uses the additional input condition that every coefficient denominator of this saved $Q$ is a unit at $31$. The consumer checks this condition entry by entry before reporting any defect conclusion. After that check, $Q\in D[s]^{155\times13}$, and all following assertions over $D$ apply to this actual input. This is a direct coefficient check, not an operation that divides rows by their $31$-contents.

Since (2.1) has nonzero determinant, these thirteen columns are independent over $\mathbb Q(s)$. They annihilate all original sources after $\pi$, and the full original left nullity is exactly thirteen. Consequently

$$
\ker_{\mathbb Q(s)}(Q^T\pi)
=\operatorname{im}_{\mathbb Q(s)}A.
$$

Intersecting with $V$ gives the exact identity

$$
N=\ker_R(Q^T\pi).
\tag{2.2}
$$

Thus this argument uses the complete original generic image. It does not infer that image merely from the rank of an unrelated projected system. Surjectivity of $\pi$ and (2.2) imply

$$
G\cong\operatorname{im}_R Q^T.
\tag{2.3}
$$

## 3. A finite-$D$ cokernel detects exactly $J$

Set

$$
H=\operatorname{coker}_R(Q^T:R^{155}\longrightarrow R^{13}).
$$

The thirteen free-coordinate columns of $Q^T$ include $D_{\rm lin}^2I_{13}$. The leading coefficient of $D_{\rm lin}$ is a power of $5$, hence a unit of $D$. Therefore $H$ is a quotient of $(R/(D_{\rm lin}^2))^{13}$ and is finite as a $D$-module.

Using (2.3), tensor the exact sequence

$$
0\longrightarrow G\longrightarrow R^{13}\longrightarrow H\longrightarrow0
$$

with $D/pD$. Its leftmost term is $\operatorname{Tor}_1^D(H,k)=H[p]$, and it gives

$$
0\longrightarrow H[p]\longrightarrow G/pG
 \longrightarrow k[s]^{13}\longrightarrow H/pH\longrightarrow0.
\tag{3.1}
$$

The quotient of $G/pG$ by $H[p]$ is a submodule of the torsion-free module $k[s]^{13}$. Also $H[p]$ is finite dimensional over $k$. It follows that

$$
J\cong H[p].
\tag{3.2}
$$

This identifies the exact missing quotient defect, rather than a subspace of it.

## 4. The characteristic-polynomial difference, including residue collisions

For a finite-dimensional module over a one-variable polynomial PID, write $\chi$ for its monic characteristic polynomial, equivalently the product of all nonzero Smith factors. Let

$$
\Delta_{H,\mathbb Q}=\chi(H\otimes_D\mathbb Q),\qquad
\Delta_{H,k}=\chi(H/pH).
$$

Let $T=H[p^\infty]$ and $F=H/T$. The module $F$ is finite free over the DVR $D$, and multiplication by $s$ is a $D$-linear endomorphism of $F$. Hence

$$
\Delta_{H,\mathbb Q}\in D[s]
$$

is monic, and its reduction has the same degree. Reduction of $0\to T\to H\to F\to0$ gives

$$
0\longrightarrow T/pT\longrightarrow H/pH
 \longrightarrow F/pF\longrightarrow0.
\tag{4.1}
$$

The modules $T[p]$ and $T/pT$ need not be isomorphic as $k[s]$-modules. Their characteristic polynomials are equal. One direct proof filters $T$ by its powers of $p$: multiplication by $p$ maps $p^{a-1}T/p^aT$ onto $p^aT/p^{a+1}T$, and its kernel is the corresponding subquotient of the socle filtration on $T[p]$. Multiplicativity of characteristic polynomials in these finite exact sequences telescopes to

$$
\chi(T[p])=\chi(T/pT).
$$

Combining this fact with (3.2) and (4.1) proves

$$
\boxed{\displaystyle
\chi_J=\frac{\Delta_{H,k}}{\overline{\Delta_{H,\mathbb Q}}}.}
\tag{4.2}
$$

The division in (4.2) is exact in $k[s]$. In particular,

$$
\dim_k J=\deg\Delta_{H,k}-\deg\Delta_{H,\mathbb Q}.
\tag{4.3}
$$

At any irreducible $f\in k[s]$, the multiplicity of $f$ in (4.2) is the length over $k[s]_{(f)}$; its contribution to $k$-dimension is that multiplicity times $\deg f$.

The denominator in (4.2) must be reduced as a complete monic polynomial. A rational local length at $s=2$ alone is insufficient. For example,

$$
\overline {E_8}=5(s-1)(s-2)E_6
$$

so rational $E_8$ factors contribute to both linear residue primes. The consumer checks this identity and all resulting primary contributions explicitly.

## 5. Exact separation of ten axes and the three-row matrix

Write $d=D_{\rm lin}^2$. In the actual original coordinate order, the first ten columns of $Q$ have only one nonzero entry each, namely $d$ on their respective pure coordinates. The last three columns vanish on all these ten coordinates. This is stronger than merely knowing one free-coordinate minor.

The actual support therefore gives a direct sum

$$
H\cong (R/(d))^{10}\oplus H_3.
\tag{5.1}
$$

The first summand is $D$-free and contributes no $p$-torsion. The remaining presentation is the three-row, thirty-column matrix

$$
M_3=
[d e_1,\ d e_2,\ d e_3,\
 v_1,\ldots,v_9,\
 a_1e_2,\ldots,a_9e_2,\
 a_1e_3,\ldots,a_9e_3],
\tag{5.2}
$$

where $v_i=(a_i,b_i,c_i)^T$. These are the actual saved entries of $Q$: the three coefficients at $n_i$ give $v_i$, and the coefficients at $cn_i,dn_i$ are respectively $a_i e_2,a_i e_3$. All other entries of the $155$ by $13$ matrix must match this exact structure.

The common contribution $\chi(R/(d))^{10}$ cancels from (4.2). Thus one may compute $\chi_J$ using only the complete maximal-minor gcds of (5.2), once over $\mathbb Q[s]$ and once over $k[s]$.

## 6. A complete 211-expression gcd, with no large matrix elimination

Work over either of these two fields, independently, and put

$$
q=\gcd(d,a_1,\ldots,a_9)
$$

with monic normalization. Bezout's identity shows that the axial columns $d e_2,a_i e_2$ generate exactly $q e_2$, and the same statement holds in direction $e_3$. Hence the column module of (5.2) equals that of

$$
[d e_1,\ q e_2,\ q e_3,\ v_1,\ldots,v_9].
\tag{6.1}
$$

Every three-column determinant of (6.1) is in one of the following groups:

$$
dq^2,\quad q^2a_i,\quad dq b_i,\quad dq c_i,
$$

$$
d(b_ic_j-b_jc_i),\quad
q(a_ib_j-a_jb_i),\quad
q(a_ic_j-a_jc_i),\qquad i<j,
$$

$$
\det(v_i,v_j,v_\ell),\qquad i<j<\ell.
$$

The gcd of $dq^2$ together with the nine $q^2a_i$ is exactly $q^3$. The complete maximal-minor gcd is therefore the gcd of

$$
q^3;\quad
18\text{ axial expressions};\quad
36+72\text{ two-vector expressions};\quad
84\text{ three-vector determinants}.
\tag{6.2}
$$

There are $1+18+36+72+84=211$ expressions. This is an exact replacement of the entire maximal-minor ideal over each field, not a sufficient upper bound obtained by sampling a few minors. The two computations use their own gcd $q$; they do not assume that reduction commutes with taking the rational gcd.

Each presentation contains $dI_3$, so its generic rank is exactly three. The gcd in (6.2) is nonzero and is its full characteristic polynomial.

## 7. Reproducible input and scope of the computation

The paid source is the polynomial-core script with SHA256

    727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb

and semantic binding

    ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba.

The immutable temporary phase is

    free-thirteen-kernel-70b27882aced10d9de363b30056d93491860db2b102d3750c949659a7ad11fc0.json.gz

with $157898$ bytes and SHA256

    b4cd026450d301328d4273ca7256dd9d8ee645576fcc5a5118aecd99a4fc2c51.

Its uncompressed payload SHA256 is

    70b27882aced10d9de363b30056d93491860db2b102d3750c949659a7ad11fc0,

and its canonical polynomial-matrix SHA256 is

    0094105c15f99860016767a662e27b7b60ddfb04b085f044f50bacfe694aabe6.

The paid actual receipt is
[the original core run](../notes/r150-source-kernel-session-789f/43756208221-original-global-projection-polynomial-core.json).
It records the complete original products, $58$ nonzero polynomial entries, and maximum degree $116$.

A consumer must verify the immutable identity, all $2015$ matrix entries against (5.1)--(5.2), every coefficient's $31$-integrality, both complete gcds, the monic rational gcd's $31$-integrality and degree-preserving reduction, and the exact division (4.2). All primary lengths are then outputs. None of $22$, a root-$2$ length, or a proposed global membership conclusion is supplied as an expected answer.

The computation of $J$ does not by itself determine every coefficient-$p$ Smith exponent of $C$. It supplies the missing term in the exact finite-field dimension and characteristic-polynomial budget, which can then be combined with independently proved divided-source submodules and an independently proved external projection divisor.
