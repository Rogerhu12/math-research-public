# R150 appendix: the primitive reduced-H branch with original central source two is empty

AI-assisted GPT-6 Astra Pro; Astra-ISP-347c-20261126; 2026-11-26 UTC.

Sources: [finite phase classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md), [central-zero predecessor](R150-appendix-rank-three-reduced-degenerate-Gram-central-zero-exclusion.md), [self-contained original source](../notes/2026-11-26-reduced-H3-center-two-original-QQ-347c.py), and [actual execution receipt](../notes/2026-11-26-reduced-H3-center-two-execution-347c.json).

## Status and scope

**Status: proved original physical exclusion.** The original geometric reduction and all four residual exact rational source-fiber certificates were actually executed. The only leading-zero chart is paid separately before any monic change of variables.

Continue the reduced rank-three H, degenerate-Gram, Hp=0, essential-six branch. The preceding Gaussian reduction, phase classification and aligned-phase exclusion leave

$
F=1,\quad Hp=0,\quad H=\tfrac12(z_1^2+z_2^2+z_3^2),
\quad V=\tfrac12(u^3+v^3),
$
$
B_H=\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\quad gh\ne0,\quad g^2+h^2=-1,\quad 2e^3=-1,
$
$
(z_iKu)=(C_1,gr,-hr),\quad
(z_iKv)=(-\omega^2C_1,-\omega gr,\omega hr),
$
$
\omega^2+\omega+1=0,\quad
\delta=2g^2+1,\quad\delta^2=-e^2,\quad
2\delta C_1r=1,\quad C_1^2=\omega/(2e).
$

All displayed divisors are nonzero. The six support vectors \(y,z_1,z_2,z_3,u,v\) form a basis. Hence the five reduced H and V source points are distinct.

## 1. The actual original-center-two coordinate change

Let \(u(t)=(1,t,\ldots,t^5)^T\), \(u(\infty)=e_5\). The original bilinear form is

$
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$

Define \(M\) by \(M u(z)=z^5u(2+1/z)\). More explicitly, for \(0\le i,j\le5\),

$
M_{ij}=
\begin{cases}
\binom{i}{5-j}2^{i-5+j},&i\ge5-j,\\
0,&i<5-j.
\end{cases}
$

This homogeneous source change is invertible, with \((\det M)^2=1\). Express every original support vector and tensor in the new basis. The transformed pairing matrix is \(K_2=M^TKM\):

$
K_2=\begin{pmatrix}
0&0&0&0&-1&-3\\
0&0&0&5&15&5\\
0&0&-8&-12&16&16\\
0&5&-12&-42&-16&0\\
-1&15&16&-16&0&0\\
-3&5&16&0&0&0
\end{pmatrix}.
$

Transforming both tensors and the pairing preserves \(F\), \(Hp=0\), the original gradients and essential dimension. The source identity and congruence are verified in the frozen program. No projective invariance of the old matrix \(K\) is assumed.

The original central H source 2 becomes transformed infinity. An original source at infinity becomes transformed 0 and is retained. The other four physical source points become finite and pairwise distinct. Write

$
z_1=\lambda_1u(\infty),\quad
z_2=\lambda_2u(a),\quad z_3=\lambda_3u(b),\quad
u=\rho u(\alpha),\quad v=\sigma u(\beta)
$

in the new basis. All representative scales are nonzero.

The complete transformed original kernel is

$
k_2(s,t)=u(s)^TK_2u(t)=-(s-t)^2Q(s+t,st),
$
$
Q(x,z)=-16(x+1)z^2-(5x^2+18x+5)z+3x^3+x^2.
\tag{1.1}
$

Its central polar is

$
L(t)=k_2(t,\infty)=16t^2+5t-3.
\tag{1.2}
$

The nonzero Gram entries give

$
L(a)L(b)L(\alpha)L(\beta)\ne0.
\tag{1.3}
$

## 2. Original pairings, phase and norm

Define, at the V sources,

$
F_a(t)=\frac{k_2(a,t)}{L(a)L(t)},\qquad
F_b(t)=\frac{k_2(b,t)}{L(b)L(t)}.
$

All denominators are paid by (1.3). The original central and endpoint pairings give

$
F_a(\alpha)=T_0,\quad F_b(\alpha)=-T_0,\quad
F_a(\beta)=\omega^2T_0,\quad F_b(\beta)=-\omega^2T_0,
\qquad T_0=\lambda_1^2r/C_1\ne0.
\tag{2.1}
$

Put \(E_0=L(a)L(b)\), \(E_V=L(\alpha)L(\beta)\). As in the general primitive-phase pairing calculation,

$
\lambda_1^2=-\frac{k_2(\alpha,\beta)}{2e^2E_V},
\quad T_0=-\frac{\omega^2k_2(\alpha,\beta)}{2e\delta E_V},
$
$
2eE_V^2F_a(\alpha)F_a(\beta)=k_2(\alpha,\beta)^2.
\tag{2.2}
$

For completeness, these identities use
\(\rho L(\alpha)=C_1/\lambda_1\),
\(\sigma L(\beta)=-\omega^2C_1/\lambda_1\),
\(e=\rho\sigma k_2(\alpha,\beta)\),
\(r/C_1=\omega^2e/\delta\),
\(\delta^2=-e^2\), and \(2e^3=-1\).

Let

$
J(t)=k_2(a,t)k_2(b,t),\qquad
T=J(\alpha)L(\beta)^2+J(\beta)L(\alpha)^2.
$

Because \(F_b=-F_a\) at both V sources,
\(F_a(t)^2=-J(t)/(E_0L(t)^2)\).
The primitive ratio in (2.1) implies

$
T^2-E_V^2J(\alpha)J(\beta)=0,\qquad
F_a(\alpha)F_a(\beta)=T/(E_0E_V^2).
$

Then (2.2), cubed with \(2e^3=-1\), gives

$
\boxed{T^2-E_V^2J(\alpha)J(\beta)=0,}
$
$
\boxed{E_0^3 k_2(\alpha,\beta)^6+4T^3=0.}
\tag{2.3}
$

These are necessary equations only. No inverse claim from their squares or cubes is used, and neither primitive phase is lost.

## 3. The complete zero leading coefficient boundary

Write \(A=a+b\), \(p=ab\). The distinct H endpoints satisfy \(Q(A,p)=0\), namely

$
\ell(A)p^2+b_1(A)p+b_0(A)=0,
$
$
\ell(A)=-16(A+1),\quad b_1=-5A^2-18A-5,\quad b_0=3A^3+A^2.
\tag{3.1}
$

There is exactly one zero of the leading coefficient: \(A=-1\). Substituting it into the original equation (3.1) gives \(8p-2=0\), hence \(p=1/4\). Then

$
A^2-4p=0,
$

so the two H endpoints coincide. This contradicts reduced rank three. The frozen source actually checked this complete leading-zero boundary before making any rescaling.

We may therefore assume \(\ell(A)\ne0\) for the remaining original points.

## 4. Monic rank-six coordinates and every scale

Put \(B=\ell(A)p\). Multiplication of (3.1) by \(\ell(A)\) gives the monic equation

$
Q_B=B^2+b_1(A)B+\ell(A)b_0(A)=0.
\tag{4.1}
$

This transformation is equivalent on the paid open set \(\ell\ne0\). Define

$
E=\ell^2E_0.
$

It is an integer polynomial. A direct formula, requiring no endpoint square root, is

$
d=-3\ell-16B,\qquad v=5+16A,\qquad
E=d^2+A\ell dv+\ell Bv^2.
\tag{4.2}
$

Indeed \(L(t)\) modulo \(t^2-At+B/\ell\) is \(d/\ell+vt\).

By (2.1), both V sources annihilate

$
N_H(t)=-\{L(b)k_2(a,t)+L(a)k_2(b,t)\}.
$

On \(Q_B=0\), this polynomial is divisible by
\(H_q(t)=t^2-At+B/\ell\).
The V sources are distinct from the H endpoints, so they are zeros of the remaining cubic.

Here is a self-contained definition of all cubic coefficients used in the source. Divide \(N_H\) by the monic \(H_q\) as polynomials in \(t\). Multiply the quotient by \(\ell^3\), then reduce each coefficient modulo the monic \(Q_B\) in \(B\). Write the result as

$
-q t^3+c_2t^2+c_1t+c_0.
\tag{4.3}
$

Every coefficient is integral in \(A,B\). The source constructs the quotient from the displayed original matrix and checks

$
\ell^3N_H(t)\equiv H_q(t)(-q t^3+c_2t^2+c_1t+c_0)
\pmod{Q_B},
$
$
q\equiv2\ell E\pmod{Q_B}.
\tag{4.4}
$

For the first identity it multiplies by the paid \(\ell\) and checks the entire polynomial identity without a denominator. Thus \(q\ne0\) at every original point. These definitions and checks specify the cubic exactly without an external coefficient array.

Let \(x=\alpha+\beta\), \(z=\alpha\beta\), \(X=qx-c_2\). Reducing (4.3) modulo \(t^2-xt+z\) gives

$
Y=X+c_2,\quad Z=X^2+c_2X-qc_1,\qquad
x=Y/q,\quad z=Z/q^2,
$
$
C_X=X^3+c_2X^2-qc_1X+q^2c_0=0.
\tag{4.5}
$

Only the paid \(q\) is divided. No source-cubic discriminant is inverted; the third cubic root may coincide with a V source.

The algebra

$
\mathcal T=\mathbb Q[A,B,X]/(Q_B,C_X)
$

is free of rank six over \(\mathbb Q[A]\), with \(B\)-degree at most one and \(X\)-degree at most two. This remains true even at artificial \(\ell=0\) fibers of the monic completion and at repeated roots.

## 5. Integer phase and norm in the source algebra

The exact quadratic norm

$
J_0(t)=\ell^5J(t)
$

is integral in \(A,B,t\). To construct it, reduce \(k_2(r,t)\) modulo
\(r^2-Ar+B/\ell\) as \(F(t)+G(t)r\), and use

$
J_0(t)=\ell^5\{F^2+AFG+(B/\ell)G^2\}.
$

The program checks integrality and its leading coefficient \(\ell^3E\).

Let the scaled V roots be \(\lambda=q\alpha,\mu=q\beta\), with sum \(Y\) and product \(Z\). Reduce

$
q^{10}J_0(T_{\rm v}/q)
$

modulo \(T_{\rm v}^2-YT_{\rm v}+Z\), writing the remainder \(J_A+J_BT_{\rm v}\). The scaled original central polar has remainder

$
q^2L(T_{\rm v}/q)\equiv L_A+L_BT_{\rm v},
\qquad
L_A=-3q^2-16Z,\quad L_B=5q+16Y.
$

Define

$
\mathscr P=J_A^2+YJ_AJ_B+ZJ_B^2,
\quad \mathscr E=L_A^2+YL_AL_B+ZL_B^2,
\quad \mathscr D=Y^2-4Z,
$
$
\mathscr T=
J_A\{2L_A^2+2YL_AL_B+(Y^2-2Z)L_B^2\}
+J_B\{YL_A^2+4ZL_AL_B+ZYL_B^2\},
$
$
\mathscr Q=q^5Q(Y/q,Z/q^2)
=-16(Y+q)Z^2-(5qY^2+18q^2Y+5q^3)Z
 +3q^2Y^3+q^3Y^2.
\tag{5.1}
$

The trace formula is checked independently as a scalar identity in the two scaled V roots. Its actual polar coefficients are rebuilt from \(L\); no different-chart formula is reused.

The complete scales are

$
\mathscr E=q^4E_V,\quad
\mathscr D=q^2(\alpha-\beta)^2,\quad
k_2(\alpha,\beta)=-\mathscr D\mathscr Q/q^7,
$
$
\mathscr P=q^{20}\ell^{10}J(\alpha)J(\beta),\qquad
\mathscr T=q^{14}\ell^5T.
$

Consequently (2.3) gives

$
\boxed{\mathcal R=\mathscr T^2-\mathscr E^2\mathscr P=0,}
$
$
\boxed{\mathcal N=\ell^9E^3(\mathscr D\mathscr Q)^6
 +4\mathscr T^3=0.}
\tag{5.2}
$

The factor \(\ell^9\) is required: \(E_0=E/\ell^2\), while \(J_0=\ell^5J\). Multiplication of the original norm equation by \(q^{42}\ell^{15}\) gives exactly (5.2).

Every multiplication in the source is reduced in the displayed monic algebra, with quotient-remainder identities checked.

## 6. All original physical units

At every original point in the generic chart,

$
\boxed{
\mathcal U=\ell E(\ell A^2-4B)
 \mathscr E\,\mathscr D\,\mathscr Q\,\mathscr P\ne0.
}
\tag{6.1}
$

The factors \(\ell,E\) and \(\ell A^2-4B\) express the paid leading coefficient, nonzero central/endpoint pairings, and distinct H endpoints. The factors \(\mathscr E,\mathscr D\) express nonzero central/V pairings and distinct V sources. The nonzero V pairing \(e=\rho\sigma k_2(\alpha,\beta)\) implies \(\mathscr Q\ne0\). All four endpoint/V pairings are nonzero, hence \(J(\alpha)J(\beta)\ne0\) and \(\mathscr P\ne0\).

No other parameter or discriminant is removed. Transformed source 0, representing an original source at infinity, remains allowed.

## 7. Actual exact QQ elimination and all four fibers

The frozen source is Git blob

6ff96bb73f9d7901557877bff8626f7a9ebedf74.

After the original identities and leading-zero boundary, it actually computed

$
P_A=\operatorname{Res}_B
(Q_B,\operatorname{Res}_X(C_X,\mathcal R)),\quad
N_A=\operatorname{Res}_B
(Q_B,\operatorname{Res}_X(C_X,\mathcal N)).
$

The inner resultants were reduced modulo monic \(Q_B\). Their values at every zero of \(Q_B\) are unchanged. Every original point therefore annihilates both univariate norms.

Their actual degrees were 864 and 1296. The serialization SHA-256 values were

- \(P_A\): 235ee0377235d9535959d07c22eacd88955feeda8f4f54a236f6521f47ba1b79;
- \(N_A\): e080be6b626577f5b172f29f9969b5807e03955750ee42dc4f9a39d9e4b61486.

The exact rational extended gcd was explicitly remultiplied. Its degree was 652, and its complete factorization, up to a nonzero rational scalar, was

$
\boxed{
G(A)=A^{24}(4A+1)^6
(7808A^4+568A^3-8713A^2+1380A+549)^{58}(A+1)^{390}.
}
$

The full factorization including multiplicities was actually remultiplied. The gcd serialization SHA-256 was

274c31e1e64ea13b9a4634d0f7e588814ac6c55981098e4104e35f8c6476e741.

For each distinct factor \(f\), made monic, the source worked in

$
\mathcal A_f=\mathbb Q[A,B,X]/(f(A),Q_B,C_X),
\qquad D=6\deg f.
$

The actual certificates were:

| Factor \(f\) | Multiplicity | Dimension \(D\) | Rational matrix rank | Nonzero cofactor coefficients | Verified identity |
|---|---:|---:|---:|---:|---|
| \(A\) | 24 | 6 | 3 | 3 | \(\mathcal U^6=A_f\mathcal R+B_f\mathcal N\) |
| \(4A+1\) | 6 | 6 | 4 | 3 | \(\mathcal U^6=A_f\mathcal R+B_f\mathcal N\) |
| \(7808A^4+568A^3-8713A^2+1380A+549\) | 58 | 24 | 12 | 12 | \(\mathcal U^{24}=A_f\mathcal R+B_f\mathcal N\) |
| \(A+1\) | 390 | 6 | 0 | 0 | \(\mathcal U^6=0\) |

The cofactor symbols denote actual rational elements, not the source parameter. Each identity was verified by exact rational matrix multiplication and again by reconstructing the two cofactor elements and multiplying in the full monic algebra.

The certificate-vector SHA-256 values, in table order, were

- 950a37882dd16a17160f105c0b7005f421598561b778805e6195c36cfe7aeeaf;
- 360a560da12afc1848a2921446edbec21669ede862d0f22cf652ae38a1b218f7;
- fd020fb800df66a794ecbfc556a73f2b15f2203034926f7ab01572078e2d7507;
- ff3268db72f34cee59ecc7c8856b5c41f9c51e5f29fba3783cb762b589067a60.

At the monic completion's artificial \(A=-1\) fiber, \(\ell=0\), so \(\mathcal U^6=0\) itself. This does not replace the original boundary proof in §3; that proof already excluded the genuine unscaled physical fiber before using \(B=\ell ab\).

Using \(f\) instead of \(f^m\) is a pointwise argument only, since they have the same complex roots. No primary-ideal equivalence is claimed. All repeated \(B,X\) roots are retained in the full monic algebra, of dimension \(6\deg f\).

Every possible source value \(A\) belongs to one displayed factor. Evaluation of its verified identity forces \(\mathcal U^D=0\), contradicting (6.1). This excludes the entire \(\ell\ne0\) chart, and §3 excludes its complete original complement.

## 8. Frozen execution and remaining scope

The actual public run was 45823574259, job 139921814732, from source commit

a8213d2429c498852dde5602ccb9019251f01ff6.

The source SHA-256 was

8fd5e5b31e92bd0ffaf181c8cb96100ea55ad61ab1724652e3eff17ab497cd9a.

The source completed in 229.449772332 seconds; the driver completed in 229.770566081 seconds, with maximum child RSS 562040 KiB and source exit code 0. The compact actual receipt is Git blob

078c9e1fa715add6a2d8457e48bdc60443518f45.

The driver actually pulled main to a39e5a6f88c9695ae43abcc6358679a422c4d5e8 and verified both governing README blobs were unchanged. Every rational norm, Bézout identity, factorization and finite-fiber product reported above was actually executed. No finite-field unit was extrapolated.

This excludes original central H source 2 in the primitive reduced-H, degenerate-Gram, Hp=0, essential-six branch, including any other original source at infinity. General remaining finite central sources, other H Gram types, lower essential dimensions, the Bell natural-power problem and ordinary invariant-subspace problem remain outside this conclusion.
