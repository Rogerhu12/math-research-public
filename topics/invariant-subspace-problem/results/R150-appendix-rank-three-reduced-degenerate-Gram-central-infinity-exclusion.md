# R150 appendix: the primitive reduced-H branch with central source infinity is empty

Date: 2026-11-26 UTC. Author: Astra-ISP-347c-20261126 / prior_results_map; AI-assisted GPT-6 Astra Pro.

## Status and scope

**Status: proved physical exclusion.** The original source reduction below has actually passed exact rational elimination and all four remaining source-fiber certificates. Every original physical exception is retained; no characteristic-positive computation is used.

Continue the reduced rank-three H, degenerate-Gram, Hp=0, essential-six branch. The [Gaussian reduction](R150-appendix-rank-three-reduced-second-cumulant-degenerate-gram-essential-six-gaussian-reduction.md), [finite-phase classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md) and [aligned-phase exclusion](R150-appendix-rank-three-reduced-degenerate-Gram-aligned-phase-physical-exclusion.md) leave

$
F=1,\quad H=\tfrac12(z_1^2+z_2^2+z_3^2),\quad
V=\tfrac12(u^3+v^3),
$
$
B_H=\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\quad gh\ne0,\quad g^2+h^2=-1,\quad 2e^3=-1,
$
$
c_1=C_1,\ c_2=gr,\ c_3=-hr,\qquad
d_1=-\omega^2C_1,\ d_2=-\omega gr,\ d_3=\omega hr,
$
$
\omega^2+\omega+1=0,\quad
\delta=2g^2+1,\quad \delta^2=-e^2,\quad
2\delta C_1r=1,\quad C_1^2=\frac{\omega}{2e}.
$

All displayed scale divisors are nonzero.

The present chart has the central H source at infinity and the zero-edge endpoints finite:

$
z_1=\lambda_1u(\infty),\quad
z_2=\lambda_2u(a),\quad z_3=\lambda_3u(b).
$

The endpoints a,b are distinct and neither is -1, because
g=-lambda_1 lambda_2(a+1) and h=-lambda_1 lambda_3(b+1) are nonzero. The reduced V sources alpha,beta are finite and distinct from one another and from both H endpoints; otherwise the six original support columns would be dependent. They are also not -1, because c_1,d_1 are nonzero and k(t,infinity)=-(t+1).

Write u=rho u(alpha), v=sigma u(beta), with all representative scales nonzero.

## 1. Original pairings and rational endpoint polars

Define

$
F_a(t)=\frac{k(a,t)}{(a+1)(t+1)},\qquad
F_b(t)=\frac{k(b,t)}{(b+1)(t+1)}.
$

These rational functions are used only at alpha,beta, where all denominators have just been paid.

The central pairings give

$
\rho(\alpha+1)=-C_1/\lambda_1,\qquad
\sigma(\beta+1)=\omega^2C_1/\lambda_1.
$

Using the two endpoint pairings and setting T_0=lambda_1^2 r/C_1 gives

$
\boxed{
F_a(\alpha)=T_0,\quad F_b(\alpha)=-T_0,\quad
F_a(\beta)=\omega^2T_0,\quad F_b(\beta)=-\omega^2T_0.
}\tag{1.1}
$

The quantity T_0 is nonzero.

Put E_0=(a+1)(b+1) and E_V=(alpha+1)(beta+1). From e=rho sigma k(alpha,beta), C_1^2=omega/(2e), and r/C_1=omega^2 e/delta, one obtains

$
\lambda_1^2=-\frac{k(\alpha,\beta)}{2e^2E_V},\qquad
T_0=-\frac{\omega^2k(\alpha,\beta)}{2e\delta E_V}.
$

Squaring and using delta^2=-e^2 and 2e^3=-1 gives the necessary original norm relation

$
\boxed{
2eE_V^2F_a(\alpha)F_a(\beta)=k(\alpha,\beta)^2.
}\tag{1.2}
$

The later symmetric equations are necessary only. Squaring never licenses an inverse reconstruction claim.

## 2. The zero H edge and the V source cubic

Let

$
A=a+b,\qquad B=5ab,\qquad E=5A+B+5=5E_0.
$

The original kernel has k(a,b)=-(a-b)^2q_H(a,b). Since a!=b, the zero H edge is exactly the monic quadratic equation

$
\boxed{
Q_B=B^2-(A^2-6A+32)B-5A^3+25A^2=0.
}\tag{2.1}
$

The physical endpoint discriminant is A^2-4B/5, so 5A^2-4B is nonzero. Also E is nonzero.

By (1.1), both alpha and beta annihilate

$
N_H(t)=(b+1)k(a,t)+(a+1)k(b,t).
$

On the zero-edge equation N_H(t) is divisible by
t^2-At+B/5. The two V sources are not a or b, so they are roots of the remaining cubic. An exact original-kernel identity, modulo Q_B, is

$
25N_H(t)\equiv
(t^2-At+B/5)(-q t^3+c_2t^2+c_1t+c_0), \tag{2.2}
$

where

$
q=10E=50E_0,
$
$
c_2=15AB+75A^2+200A+250,
$
$
c_1=(-7A^2+2A+306)B-35A^3-350A^2-550A,
$
$
c_0=(-7A^2-88A-14)B+90A^3+350A^2.
$

The source verifies (2.2) directly from the original kernel. Its only nonconstant leading divisor would be q, already a physical unit.

Let x=alpha+beta and z=alpha beta, and introduce X=qx-c_2. Reducing the cubic in (2.2) modulo t^2-xt+z gives

$
Y=X+c_2,\qquad Z=X^2+c_2X-qc_1,
$
$
x=Y/q,\qquad z=Z/q^2,
$
$
\boxed{
C_X=X^3+c_2X^2-qc_1X+q^2c_0=0.
}\tag{2.3}
$

No distinctness of the third cubic root is required. The source cubic may have a multiple root, and no cubic discriminant is inverted.

The two equations Q_B,C_X are monic in B and X respectively. Reducing the coefficients of C_X modulo Q_B preserves its monic X-leading term. Consequently

$
\mathcal T=\mathbb Q[A,B,X]/(Q_B,C_X)
$

is a free algebra of rank six over Q[A], with representatives of B-degree at most one and X-degree at most two. This remains true at every A and at every repeated-root fiber.

## 3. Symmetric phase and norm equations over QQ

Let

$
J(t)=k(a,t)k(b,t),
$
$
T=J(\alpha)(\beta+1)^2+J(\beta)(\alpha+1)^2.
$

At alpha,beta, equation (1.1) gives

$
F_a(t)^2=-\frac{J(t)}{E_0(t+1)^2}.
$

The ratio of these two squares is a primitive cube root. Their sum and product are therefore constrained by (sum)^2-product=0. Moreover,

$
F_a(\alpha)F_a(\beta)
=-\{F_a(\alpha)^2+F_a(\beta)^2\}
=\frac{T}{E_0E_V^2}.
$

The complete necessary phase and original norm consequences are

$
\boxed{
T^2-E_V^2J(\alpha)J(\beta)=0,
}\tag{3.1}
$
$
\boxed{
E_0^3k(\alpha,\beta)^6+4T^3=0.
}\tag{3.2}
$

For (3.2), equation (1.2) says 2eT=E_0k(alpha,beta)^2. Cubing and using 2e^3=-1 proves (3.2) directly, without division by T.

These equations have rational coefficients and cover both primitive phases and both signs of delta.

## 4. Exact integer representatives in the rank-six source algebra

The symmetric polynomial J_0(t)=3125J(t) has integer coefficients in A,B,t. One self-contained construction is to reduce k(r,t) modulo r^2-Ar+B/5 as F(t)+G(t)r and use

$
J_0(t)=3125\{F(t)^2+AF(t)G(t)+(B/5)G(t)^2\}.
$

This is the exact quadratic norm; no endpoint square root is selected.

Let the scaled V roots be lambda=q alpha and mu=q beta. They satisfy

$
\lambda+\mu=Y,\quad \lambda\mu=Z,\quad
T_{\mathrm v}^2-YT_{\mathrm v}+Z=0.
$

Write the remainder of

$
\widehat J(T_{\mathrm v})=q^{10}J_0(T_{\mathrm v}/q)
$

modulo this monic quadratic as J_A+J_B T_v. All coefficient operations may be performed exactly in T. Define

$
\mathscr P=J_A^2+YJ_AJ_B+ZJ_B^2,
$
$
\mathscr T=
J_A(Y^2-2Z+2qY+2q^2)
+J_B(ZY+4qZ+q^2Y),
$
$
\mathscr E=q^2+qY+Z,\qquad
\mathscr D=Y^2-4Z,
$
$
\mathscr Q=qY^3-5q^2Y^2+Y^2Z-6qYZ+32q^2Z-5Z^2.
$

These definitions retain the exact scales

$
\mathscr E=q^2E_V,\quad
\mathscr D=q^2(\alpha-\beta)^2,\quad
k(\alpha,\beta)=-\mathscr D\mathscr Q/q^6,
$
$
\mathscr P=q^{20}3125^2J(\alpha)J(\beta),\qquad
\mathscr T=q^{12}3125\,T.
$

Equations (3.1)--(3.2), after multiplication by paid powers of q and numerical constants, become

$
\boxed{\mathcal R=\mathscr T^2-\mathscr E^2\mathscr P=0,}\tag{4.1}
$
$
\boxed{
\mathcal N=5^{12}E^3(\mathscr D\mathscr Q)^6
 +4\mathscr T^3=0.
}\tag{4.2}
$

The coefficient 5^12 is required: it is 3125^3/5^3, because E_0=E/5. Every product in the source is reduced by the displayed monic triangular equations, with exact quotient identities checked. No number-field specialization is used.

## 5. All original physical units

The following product is nonzero at every original point in the chart:

$
\boxed{
\mathcal U=
E(5A^2-4B)\,
\mathscr E\,\mathscr D\,\mathscr Q\,\mathscr P\ne0.
}\tag{5.1}
$

Here E records the nonzero pairings of the two endpoints with the central infinity source. The H endpoint discriminant is nonzero because a!=b. The V factors mathscr E and mathscr D record alpha,beta!=-1 and alpha!=beta. The nonzero V pairing e gives k(alpha,beta)!=0, and hence mathscr Q!=0. Finally all four endpoint/V pairings c_2,c_3,d_2,d_3 are nonzero, so J(alpha)J(beta)!=0 and mathscr P!=0.

There is no unproved generic assumption in (5.1). It does not remove a multiple root of either monic defining polynomial, and it contains no unspecified leading coefficient.

## 6. The actually executed rational elimination and all four fibers

The [frozen self-contained source](../notes/2026-11-26-reduced-H3-center-infinity-original-QQ-347c.py) is Git blob `f67005f96502947b66af3ee9789622e92992b48c`.

It constructs the original kernel identities and integer endpoint norm J_0, checks the displayed scales, and forms the canonical representatives of R,N,U in T. The actual iterated integer resultants were

$
P_A=\operatorname{Res}_B
\bigl(Q_B,\operatorname{Res}_X(C_X,\mathcal R)\bigr),
$
$
N_A=\operatorname{Res}_B
\bigl(Q_B,\operatorname{Res}_X(C_X,\mathcal N)\bigr).
$

The inner resultants are first reduced modulo the monic Q_B; their values on Q_B=0 are unchanged. A common original point must therefore make both univariate polynomials vanish at its A.

The actual degrees were 284 and 426. Their exact FLINT-serialization SHA-256 values were

- P_A: d8bb446b6df5227457f042218ec04f30b0b0ec09e76c57d59768e61d40d003ac;
- N_A: 2a3c622766abdedd9e32698b76130caec0cf750cca965000a0705940b261b262.

The actual extended gcd was computed over QQ and explicitly remultiplied. Its monic gcd has degree 128 and, up to its nonzero rational normalization, is

$
\boxed{
G(A)=A^{24}(A-4)^6(A+12)^6(5A^2+36A+37)^{46}.
}
$

The program also remultiplied the complete exact factorization, including all four multiplicities. Thus every possible complex source value A lies on one of exactly these four displayed factors.

For each distinct factor f, make it monic and work in

$
\mathcal A_f=\mathbb Q[A,B,X]/(f(A),Q_B,C_X).
$

The actual source verified the following table:

| Factor f | Multiplicity in G | Dimension D of A_f | Rational matrix rank | Nonzero certificate coefficients | Verified identity |
|---|---:|---:|---:|---:|---|
| A | 24 | 6 | 3 | 3 | U^6=A_f R+B_f N |
| A-4 | 6 | 6 | 4 | 3 | U^6=A_f R+B_f N |
| A+12 | 6 | 6 | 4 | 3 | U^6=A_f R+B_f N |
| 5A^2+36A+37 | 46 | 12 | 6 | 6 | U^12=A_f R+B_f N |

Here A_f,B_f in the last column denote actual rational cofactor elements, not the source parameter A. Each identity was checked twice: by exact rational matrix remultiplication and by reconstructing the elements in the full monic triangular algebra and multiplying there again.

The actual certificate-vector SHA-256 values, in the same factor order, are

- 48ab0d395cab638b7d6f7be47812301e13d7bcb0ba48d1fa9a7667bd0651f540;
- 7bdfedf441e73c25b029d3808f738de56125df309e97af78896a4437923e89b9;
- c1a04860961f205442ac8be3c01273beb421e9825e3432fee44da84fab5e421f;
- 45fb6aceefbfd64312970a11ce1c468444b6e7a40c0d8bd93878762ea1e34815.

The source reconstructs these rational vectors by an exact RREF solve from the original displayed generators. No large coefficient array is needed as an independent unverified input.

Using f in place of f^k is a pointwise argument only: every complex root of f^k is a root of f. No claim is made that the corresponding primary quotient ideals agree. All repeated B and X fibers are retained in the monic algebra A_f, whose dimension is 6deg f independently of separability.

At any original critical point belonging to a factor f, evaluation of the verified identity gives U^D=0. This contradicts the fully paid physical unit (5.1). The four factors exhaust every possible A, so the entire present chart is empty.

## 7. Frozen execution identity and remaining scope

The actual public run was 45818497162, job 139904312131, from source commit

3707eea2a0c64cdbd32b9966de2ed97fddcd11e8.

The source SHA-256 was

fd594e1340b0a63b8c50ced8c52bca31ce75b0e2d843f66fd1cbd1d135b7f1e0.

The source completed in 18.036312604 seconds; the driver completed in 18.355596398 seconds, with maximum child RSS 190212 KiB and source exit code 0. The [compact actual receipt](../notes/2026-11-26-reduced-H3-center-infinity-execution-347c.json) is Git blob `b9594fc76a180aad489b4355db6015321b61fccf`.

The driver actually pulled main to abb271537c66e5cd38a75ee7305befd52adb4a2e before executing and verified that both governing README blobs were unchanged. The exact rational norm, gcd, factorization and four cofactor identities were all actually executed. No modular unit ideal was used as an exclusion certificate.

This excludes every primitive-phase essential-six point with the central H source at infinity and its two zero-edge endpoints finite. The [zero-edge-infinity theorem](R150-appendix-rank-three-reduced-degenerate-Gram-zero-edge-infinity-exclusion.md) already excludes either zero-edge endpoint being infinity, and the aligned phase was excluded on every source chart. Hence, within the reduced-H degenerate-Gram branch, any remaining essential-six point must have all three H sources finite; the V sources may still include infinity. These remaining charts, other H Gram types, lower essential dimensions, the Bell natural-power problem and the ordinary invariant-subspace problem remain outside the present conclusion.
