# R150 appendix: the primitive reduced-H branch with original central source zero is empty

AI-assisted GPT-6 Astra Pro; Astra-ISP-347c-20261126; 2026-11-26 UTC.

Predecessors: [finite phase classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md), [aligned phase exclusion](R150-appendix-rank-three-reduced-degenerate-Gram-aligned-phase-physical-exclusion.md), and [original central infinity exclusion](R150-appendix-rank-three-reduced-degenerate-Gram-central-infinity-exclusion.md). The [corrected executable source](../notes/2026-11-26-reduced-H3-center-zero-corrected-original-QQ-347c.py) and [actual compact receipt](../notes/2026-11-26-reduced-H3-center-zero-corrected-execution-347c.json) are part of this proof.

## Scope and status

**Status: proved original physical exclusion.** The corrected exact rational gate has actually completed the original geometric reduction and all four residual source-fiber identities. This document uses the original central H source 0 and retains every original source at infinity through the exact reciprocal coordinates. No finite-field statement is used.

The earlier reduced rank-three H degenerate-Gram reduction, finite-phase classification, and aligned-phase exclusion leave, under the essential-six hypothesis,

$$
F=1,\quad Hp=0,\quad H=\tfrac12(z_1^2+z_2^2+z_3^2),
\qquad V=\tfrac12(u^3+v^3),
$$
$$
B_H=\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\quad gh\ne0,\quad g^2+h^2=-1,\quad 2e^3=-1.
$$

For one primitive cube root \(\omega\),

$$
(z_iKu)_{i=1}^3=(C_1,gr,-hr),\qquad
(z_iKv)_{i=1}^3=(-\omega^2C_1,-\omega gr,\omega hr),
$$
$$
\delta=2g^2+1,\quad \delta^2=-e^2,\quad
2\delta C_1r=1,\quad C_1^2=\frac{\omega}{2e}.
$$

Every displayed denominator is nonzero. The six vectors \(y,z_1,z_2,z_3,u,v\) form a basis, so the five reduced H and V source points are distinct.

## 1. Reciprocal coordinates change the kernel as well as the curve

Write \(u(t)=(1,t,\ldots,t^5)^T\), \(u(\infty)=e_5\), and let \(R\) reverse the six coordinates. Make the exact invertible change

$$
\widetilde y=Ry,\quad \widetilde H=RHR,\quad
\widetilde V=R^{\otimes3}V,\qquad K_0=RKR.
$$

Pairings, \(F\), the original gradient equations, \(Hp=0\), and essential dimension are preserved after transforming both the tensors and the bilinear form. In homogeneous source coordinates the identity is simply

$$
R\,u_5(S,T)=u_5(T,S).
$$

Thus the original central H source 0 becomes the transformed source infinity. For a nonzero finite original source \(t\), \(Ru(t)=t^5u(1/t)\); the nonzero scalar is absorbed in its representative. Original source infinity becomes transformed source 0 and is retained. This is a change of basis with the changed kernel \(K_0\), not an assertion that the original \(K\) is invariant under a projective transformation.

The actual transformed matrix is

$$
K_0=\begin{pmatrix}
0&0&0&0&-1&-1\\
0&0&0&5&5&5\\
0&0&-8&-4&-32&0\\
0&5&-4&54&0&0\\
-1&5&-32&0&0&0\\
-1&5&0&0&0&0
\end{pmatrix}.
$$

Suppress tildes from now on. Its entire physical polar is

$$
k_0(s,t)=u(s)^TK_0u(t)=-(s-t)^2q_0(s+t,st),
$$
$$
q_0(x,z)=32z^2-(5x^2+6x+5)z+x^3+x^2,
\qquad L(t)=k_0(t,\infty)=5t-1.
\tag{1.1}
$$

The frozen source verifies both identities directly from the displayed reversed original matrix.

Represent the transformed sources as

$$
z_1=\lambda_1u(\infty),\quad
z_2=\lambda_2u(a),\quad z_3=\lambda_3u(b),\quad
u=\rho u(\alpha),\quad v=\sigma u(\beta).
$$

All five representative scales are nonzero. All four remaining sources \(a,b,\alpha,\beta\) are finite and pairwise distinct, because they are distinct from the central source infinity. Moreover

$$
L(a)L(b)L(\alpha)L(\beta)\ne0,
\tag{1.2}
$$

by the nonzero original pairings \(g,h,C_1,-\omega^2C_1\). No assumption excludes transformed source 0.

## 2. Original Gram pairings give the rational phase and norm

At the two V sources define

$$
F_a(t)=\frac{k_0(a,t)}{L(a)L(t)},\qquad
F_b(t)=\frac{k_0(b,t)}{L(b)L(t)}.
$$

Their denominators are paid by (1.2). From the central pairings,

$$
\rho L(\alpha)=C_1/\lambda_1,\qquad
\sigma L(\beta)=-\omega^2C_1/\lambda_1.
$$

The endpoint pairings then give, with \(T_0=\lambda_1^2r/C_1\ne0\),

$$
F_a(\alpha)=T_0,\quad F_b(\alpha)=-T_0,\qquad
F_a(\beta)=\omega^2T_0,\quad F_b(\beta)=-\omega^2T_0.
\tag{2.1}
$$

Put

$$
E_0=L(a)L(b),\qquad E_V=L(\alpha)L(\beta).
$$

Using \(e=\rho\sigma k_0(\alpha,\beta)\) and the displayed Gram normalization,

$$
\lambda_1^2=-\frac{k_0(\alpha,\beta)}{2e^2E_V},\qquad
T_0=-\frac{\omega^2k_0(\alpha,\beta)}{2e\delta E_V}.
$$

The identities \(\delta^2=-e^2\), \(2e^3=-1\) imply

$$
2eE_V^2F_a(\alpha)F_a(\beta)=k_0(\alpha,\beta)^2.
\tag{2.2}
$$

Only necessary consequences will be used; no inverse reconstruction from their squares is asserted.

## 3. A monic rank-six source algebra with no omitted endpoint fiber

Set

$$
A=a+b,\qquad B=32ab,\qquad
E=25B-160A+32=32E_0.
$$

The zero H edge and the distinctness \(a\ne b\) give

$$
Q_B=B^2-(5A^2+6A+5)B+32A^3+32A^2=0.
\tag{3.1}
$$

The physical factors \(E\) and \(32A^2-4B\) are nonzero.

By (2.1), both V sources vanish on

$$
N_H(t)=-\{L(b)k_0(a,t)+L(a)k_0(b,t)\}.
$$

On (3.1), the polynomial \(N_H\) is divisible by \(t^2-At+B/32\). Its remaining cubic has nonzero leading coefficient because \(E_0\ne0\). A direct original-kernel calculation gives

$$
512N_H(t)\equiv
(t^2-At+B/32)(-q t^3+c_2t^2+c_1t+c_0)
\pmod{Q_B},
\tag{3.2}
$$
where
$$
q=32E,
$$
$$
c_2=(1760A+224)B-11264A^2+4096A-1024,
$$
$$
c_1=(-1085A^2-438A+835)B+6944A^3-7392A^2+1536A,
$$
$$
c_0=(217A^2-290A-7)B+1888A^3-672A^2.
$$

The source derives the quotient from the original matrix, clears its exact rational coefficient denominators, and verifies the entire identity (3.2), rather than treating these coefficients as unchecked input.

Write \(x=\alpha+\beta\), \(z=\alpha\beta\), \(X=qx-c_2\). The two distinct V sources are not H endpoints. Reducing the cubic in (3.2) modulo \(t^2-xt+z\) gives

$$
Y=X+c_2,\quad Z=X^2+c_2X-qc_1,\qquad
x=Y/q,\quad z=Z/q^2,
$$
$$
C_X=X^3+c_2X^2-qc_1X+q^2c_0=0.
\tag{3.3}
$$

Only the already paid unit \(q=32E\) is divided out. The unselected third cubic root may coincide with a V source; no cubic discriminant is inverted.

The two equations \(Q_B,C_X\), after reducing coefficients modulo \(Q_B\), are monic of degrees two in \(B\) and three in \(X\). Thus

$$
\mathcal T=\mathbb Q[A,B,X]/(Q_B,C_X)
$$

is free of rank six over \(\mathbb Q[A]\), even at every repeated-root fiber. Canonical representatives have \(B\)-degree at most one and \(X\)-degree at most two.

## 4. Symmetric phase and original norm

Let

$$
J(t)=k_0(a,t)k_0(b,t),\qquad
T=J(\alpha)L(\beta)^2+J(\beta)L(\alpha)^2.
$$

At the V sources, \(F_b=-F_a\), so

$$
F_a(t)^2=-\frac{J(t)}{E_0L(t)^2}.
$$

Equation (2.1) gives \(F_a(\beta)=\omega^2F_a(\alpha)\). Therefore

$$
T^2-E_V^2J(\alpha)J(\beta)=0,
\tag{4.1}
$$
$$
F_a(\alpha)F_a(\beta)
=-\{F_a(\alpha)^2+F_a(\beta)^2\}
=\frac{T}{E_0E_V^2}.
$$

Equation (2.2) becomes \(2eT=E_0k_0(\alpha,\beta)^2\). Cube this identity and use \(2e^3=-1\):

$$
E_0^3k_0(\alpha,\beta)^6+4T^3=0.
\tag{4.2}
$$

No division by \(T\) is needed. Both primitive phases and both signs of \(\delta\) are covered by these rational necessary equations.

## 5. Integer representatives and the changed \(L\)-scales

The exact quadratic norm

$$
J_0(t)=32^5J(t)
$$

has integer coefficients in \(A,B,t\). For example, reduce \(k_0(r,t)\) modulo \(r^2-Ar+B/32\) as \(F(t)+G(t)r\). Then

$$
J_0(t)=32^5\{F(t)^2+AF(t)G(t)+(B/32)G(t)^2\}.
$$

The source checks coefficient integrality and the leading coefficient \(32^4E\).

Let \(\lambda=q\alpha\), \(\mu=q\beta\), so that \(\lambda+\mu=Y\), \(\lambda\mu=Z\). Reduce

$$
q^{10}J_0(T_{\rm v}/q)
$$

modulo the monic \(T_{\rm v}^2-YT_{\rm v}+Z\), obtaining \(J_A+J_BT_{\rm v}\). Define

$$
\mathscr P=J_A^2+YJ_AJ_B+ZJ_B^2,
$$
$$
\mathscr T=
J_A\{25(Y^2-2Z)-10qY+2q^2\}
+J_B\{25ZY-20qZ+q^2Y\},
$$
$$
\boxed{\mathscr E=q^2-5qY+25Z=q^2E_V,}
\qquad
\mathscr D=Y^2-4Z,
$$
$$
\mathscr Q=
32Z^2-(5Y^2+6qY+5q^2)Z+qY^3+q^2Y^2.
$$

The changed coefficients in \(\mathscr E\) and \(\mathscr T\) come from the actual transformed polar \(L(t)=5t-1\). In particular,

$$
(5\lambda-q)(5\mu-q)=q^2-5qY+25Z.
$$

The source independently checks this scalar identity and the analogous identity for \(\mathscr T\), before forming any elimination input.

The complete exact scales are

$$
\mathscr D=q^2(\alpha-\beta)^2,\quad
k_0(\alpha,\beta)=-\mathscr D\mathscr Q/q^6,
$$
$$
\mathscr P=q^{20}32^{10}J(\alpha)J(\beta),\qquad
\mathscr T=q^{12}32^5T.
$$

Thus (4.1)--(4.2) imply the two rational equations

$$
\mathcal R=\mathscr T^2-\mathscr E^2\mathscr P=0,
\tag{5.1}
$$
$$
\mathcal N=32^{12}E^3(\mathscr D\mathscr Q)^6
 +4\mathscr T^3=0.
\tag{5.2}
$$

The factor \(32^{12}=32^{15}/32^3\) pays the exact scales \(J_0=32^5J\) and \(E_0=E/32\). Every operation is performed in the displayed monic source algebra, with exact quotient-remainder identities checked.

## 6. Every physical factor used by the gate

At an original point in the present chart,

$$
\mathcal U=
E(32A^2-4B)\,\mathscr E\,\mathscr D\,\mathscr Q\,\mathscr P
\ne0.
\tag{6.1}
$$

The first two factors express nonzero central/endpoint pairings and distinct H endpoints. The factors \(\mathscr E,\mathscr D\) express nonzero central/V pairings and distinct V sources. The identity \(e=\rho\sigma k_0(\alpha,\beta)\ne0\) forces \(\mathscr Q\ne0\). Finally all four endpoint/V pairings are nonzero in the preceding full Gram classification, hence \(J(\alpha)J(\beta)\ne0\) and \(\mathscr P\ne0\).

No vanishing value of an unlisted leading coefficient, source cubic discriminant, or source parameter is removed. In particular the transformed source 0, which represents an original source at infinity, is retained.

## 7. Actually executed exact QQ gate and all four source fibers

The corrected self-contained source is Git blob

6110026f5aeee5d257bba5fb409d6828fda55b31.

It actually constructed and checked nine original matrix, polar, source-cubic, endpoint-norm and changed-scale identities. It then formed the exact nested integer resultants

$$
P_A=\operatorname{Res}_B
(Q_B,\operatorname{Res}_X(C_X,\mathcal R)),\qquad
N_A=\operatorname{Res}_B
(Q_B,\operatorname{Res}_X(C_X,\mathcal N)).
$$

The inner norms were reduced modulo the monic \(Q_B\) before the outer norms. This does not change their values at a zero of \(Q_B\). Hence a common original point must annihilate both resulting univariate polynomials.

The actual degrees were respectively 284 and 426. Their exact FLINT-serialization SHA-256 values were

- \(P_A\): 6ab7f77c089f56a0f3c0bfd02cca10a4bf50151a134e3549529857ee6970d65d;
- \(N_A\): 3451ece1aa210115f6b5a0ab7b03225bf37f35f6c012772dc7620f19a58c13e4.

The program computed the actual extended gcd over \(\mathbb Q\) and explicitly remultiplied its Bézout identity. Its gcd has degree 128 and, up to a nonzero rational scalar, is

$$
\boxed{
G(A)=A^{24}(A-1)^6(3A+1)^6(800A^2-795A+157)^{46}.
}
\tag{7.1}
$$

The entire exact factorization, including all multiplicities, was also remultiplied.

For each distinct factor \(f\), make it monic and form

$$
\mathcal A_f=\mathbb Q[A,B,X]/(f(A),Q_B,C_X),
\qquad D=6\deg f.
$$

The actual finite-algebra identities were:

| Factor \(f\) | Multiplicity in \(G\) | Dimension \(D\) | Rational matrix rank | Nonzero cofactor coefficients | Verified identity |
|---|---:|---:|---:|---:|---|
| \(A\) | 24 | 6 | 3 | 3 | \(\mathcal U^6=A_f\mathcal R+B_f\mathcal N\) |
| \(A-1\) | 6 | 6 | 2 | 0 | \(\mathcal U^6=0\) |
| \(3A+1\) | 6 | 6 | 4 | 3 | \(\mathcal U^6=A_f\mathcal R+B_f\mathcal N\) |
| \(800A^2-795A+157\) | 46 | 12 | 6 | 6 | \(\mathcal U^{12}=A_f\mathcal R+B_f\mathcal N\) |

The symbols \(A_f,B_f\) denote actual rational cofactor elements, not the source parameter \(A\). Each displayed identity was actually checked twice: first by exact rational matrix multiplication, then by reconstructing the elements and multiplying in the full monic finite algebra. In the \(A=1\) fiber the target \(\mathcal U^6\) itself is zero before using \(\mathcal R,\mathcal N\); the zero cofactor vector is an actual successful exclusion certificate, not an omitted calculation.

The cofactor-vector SHA-256 values, in table order, were

- 8da69ea07607715d9af31e4faf047f577a73eaed1177997af148e4f6b20b6582;
- ff3268db72f34cee59ecc7c8856b5c41f9c51e5f29fba3783cb762b589067a60;
- 18a8a5289e5066b0730c410e9811fb45b17fc4444f20da65d2faabba72796e4d;
- 38069029e64e8c4003433c48f0f4d657ab1afb39592e67f259000f77b7bab8e1.

The source reconstructs every vector by exact RREF directly from the displayed original generators, so a large external coefficient array is not part of the trust boundary.

Replacing \(f^k\) by \(f\) is solely a pointwise argument: every complex root of \(f^k\) is a root of \(f\). No equality of the corresponding primary ideals is claimed. Every repeated \(B,X\) fiber remains in the monic algebra, whose dimension is \(6\deg f\) independently of separability.

At any original critical point, (7.1) places \(A\) on a factor in the table. Evaluating that factor's verified identity gives \(\mathcal U^D=0\), contradicting the original physical unit (6.1). All four factors are covered. The entire original central-zero chart is therefore empty.

## 8. Corrected input identity and actual execution

The actual corrected public run was 45821311603, job 139913975096, from source commit

85f8c05de49cde33e3cf78fe29c0657cc38a36c3.

The exact source SHA-256 was

fff102d169d13c4afc75047fd9f5531a257550c6902fa934d42f19e3360efc32.

The source completed in 30.726057836 seconds; the driver completed in 31.128928186 seconds, with maximum child RSS 201372 KiB and source exit code 0. The compact actual receipt is Git blob

98611c2e20592e2ca4b1d7d0e9932638b6cbefa6.

The driver actually pulled main to 85f8c05de49cde33e3cf78fe29c0657cc38a36c3 and verified that both governing README blobs were unchanged. The actual source ran the rational norm/gcd, complete factorization, and all four cofactor identities. No modular unit ideal was used.

An earlier new-chart source, blob b34d4894e6848c2dd54512340c26a035797cd96f, had erroneously retained \(\mathscr E=q^2+qY+Z\) from the different original central-infinity kernel. Its run 45820227879, job 139910286959, exited 0, but that raw output does not exclude any original point. Its input-defect receipt is blob 10f95889e56a45664e7f82914dd7867fe708fbbe. All exclusion language in that defective output is withdrawn. The corrected source used here has the required \(\mathscr E=q^2-5qY+25Z\) and independent original polar-product and trace checks.

The existing theorem for original central H source infinity used its own correct kernel and source, so it was unaffected by this new-chart input defect.

## Remaining scope

This excludes original central H source 0 throughout the primitive reduced-H, degenerate-Gram, \(Hp=0\), essential-six branch, including any other original source at infinity. Together with the previously proved aligned-phase and H-infinity exclusions, a surviving point in this branch must have all three H sources finite and nonzero central source.

General finite nonzero central H sources, other H Gram types, lower essential dimensions, the Bell natural-power task, and the ordinary invariant-subspace problem remain outside this conclusion.
