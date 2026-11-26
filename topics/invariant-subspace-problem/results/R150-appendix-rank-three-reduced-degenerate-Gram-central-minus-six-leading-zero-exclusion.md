# R150 appendix: the complete zero-leading endpoint fiber at original central H source minus six

AI-assisted GPT-6 Astra Pro; Astra-ISP-347c-20261126; 2026-11-26 UTC.

**Status: this original boundary is proved empty.** The generic original central-source-minus-six chart is still unresolved. The successful boundary calculation preceded a timeout of the separate generic norm calculation; the overall job's failure is not relabeled success.

Dependencies: [primitive phase and Gram classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md), the pairing derivation in the [central-two proof](R150-appendix-rank-three-reduced-degenerate-Gram-central-two-exclusion.md), the [actual self-contained source](../notes/2026-11-26-reduced-H3-center-minus-six-original-QQ-347c.py), and the [partial execution receipt](../notes/2026-11-26-reduced-H3-center-minus-six-partial-execution-347c.json).

## 1. Actual kernel and the complete leading-zero condition

Work in the primitive reduced-H, degenerate-Gram, Hp=0, essential-six branch. The five H/V source points are distinct, and all central/endpoint, central/V, endpoint/V and V/V pairings used below are nonzero by the preceding full Gram classification.

Apply the exact invertible source change

$$
t_{\rm original}=-6+1/t,\qquad
M u(t)=t^5u(-6+1/t),\qquad K_{-6}=M^{\mathsf T}KM.
$$

The original central source becomes transformed infinity. All four other sources are finite; transformed zero retains an original source at infinity. Both the tensors and pairing are transformed; no invariance of the original K under this source map is assumed.

The frozen source directly verifies the entire changed kernel

$$
k(s,t)=-(s-t)^2Q(s+t,st),
$$

$$
Q(x,z)=(144x-112)z^2+(-5x^2+30x-5)z-5x^3+x^2,
\qquad L(t)=k(t,\infty)=-144t^2+5t+5.
\tag{1}
$$

Write the two finite H endpoints as a,b, with $A=a+b$, $p=ab$. Their zero Gram edge and distinctness give $Q(A,p)=0$. Its leading coefficient in p is $\ell(A)=144A-112$. The entire zero-leading fiber is therefore

$$
A=\frac79,\qquad
\frac{1240}{81}p-\frac{1274}{729}=0,\qquad
\boxed{p=\frac{637}{5580}.}
\tag{2}
$$

There is no other leading-zero A. The endpoint discriminant and polar norm are

$$
\delta_H=A^2-4p=\frac{1862}{12555}\ne0,\qquad
E_0=L(a)L(b)=-\frac{1688209}{96100}\ne0.
\tag{3}
$$

Thus this boundary is not discarded as a repeated-root or zero-pairing chart. It requires, and receives, a separate original calculation.

## 2. Necessary original phase and norm

Let the finite V sources be $\alpha,\beta$, and write $E_V=L(\alpha)L(\beta)$ and $k_V=k(\alpha,\beta)$. The primitive Gram phase gives, for
$F_a(t)=k(a,t)/(L(a)L(t))$ and similarly $F_b$,

$$
F_b(\alpha)=-F_a(\alpha),\quad
F_b(\beta)=-F_a(\beta),\quad
F_a(\beta)=\omega^2F_a(\alpha),
$$

$$
2eE_V^2F_a(\alpha)F_a(\beta)=k_V^2,\qquad
2e^3=-1,\quad \omega^2+\omega+1=0.
$$

The same pairing derivation as in the cited central-two proof uses only these original pairings and nonzero divisors; it applies to (1) without a new geometric assumption.

Set

$$
J(t)=k(a,t)k(b,t),\qquad
T=J(\alpha)L(\beta)^2+J(\beta)L(\alpha)^2.
$$

The displayed phase and $2e^3=-1$ imply the two necessary rational equations

$$
T^2-E_V^2J(\alpha)J(\beta)=0,\qquad
E_0^3k_V^6+4T^3=0.
\tag{4}
$$

Both primitive phases are retained. Only necessity is used.

## 3. A full three-dimensional rational source algebra

Define the symmetric endpoint sum

$$
N_H(t)=-\{L(b)k(a,t)+L(a)k(b,t)\}.
$$

At (2), the source exactly divides it by the monic $t^2-At+p$ and checks zero remainder. Choose s to be the least common multiple of the rational coefficient denominators of the resulting cubic, and write

$$
s\,\frac{N_H(t)}{t^2-At+p}=-q t^3+c_2t^2+c_1t+c_0.
\tag{5}
$$

All coefficients in (5) are exact rational numbers (in fact integral after scaling). The program checks $q=2sE_0\ne0$. The two V sources annihilate this cubic, because they annihilate $N_H$ and are distinct from the H endpoints.

For $x=\alpha+\beta$, $z=\alpha\beta$, put

$$
X=qx-c_2,\quad Y=X+c_2,\quad Z=X^2+c_2X-qc_1.
$$

Division of (5) by the V quadratic gives

$$
x=Y/q,\qquad z=Z/q^2,\qquad
C_X=X^3+c_2X^2-qc_1X+q^2c_0=0.
\tag{6}
$$

The entire algebra $\mathcal B=\mathbb Q[X]/(C_X)$ has dimension three. No cubic root, discriminant or coefficient is deleted. The unused third cubic root may coincide with a selected V root.

These formulas specify the exact input without a large external coefficient table: (1)–(3) determine (5) by rational monic division and denominator lcm, and (6) determines its source algebra.

## 4. Exact scales and the original physical unit

The symmetric product J is computed as the norm of $k(r,t)$ in
$\mathbb Q[r]/(r^2-Ar+p)$. If its remainder is $F(t)+G(t)r$, then
$J=F^2+AFG+pG^2$. Let j be the denominator lcm of J and set $J_0=jJ$.

Reduce $q^{10}J_0(T_{\rm v}/q)$ modulo $T_{\rm v}^2-YT_{\rm v}+Z$, obtaining $J_A+J_BT_{\rm v}$. In $\mathcal B$ put

$$
L_A=5q^2+144Z,\qquad L_B=5q-144Y,
$$

$$
\mathscr E=L_A^2+YL_AL_B+ZL_B^2,\quad
\mathscr D=Y^2-4Z,\quad
\mathscr Q=q^5Q(Y/q,Z/q^2),
$$

$$
\mathscr P=J_A^2+YJ_AJ_B+ZJ_B^2,
$$

$$
\mathscr T=
J_A\{2L_A^2+2YL_AL_B+(Y^2-2Z)L_B^2\}
+J_B\{YL_A^2+4ZL_AL_B+ZYL_B^2\}.
$$

These use the actual L of (1). Direct symmetric-product identities give

$$
\mathscr E=q^4E_V,\quad
\mathscr D=q^2(\alpha-\beta)^2,\quad
k_V=-\mathscr D\mathscr Q/q^7,
$$

$$
\mathscr P=q^{20}j^2J(\alpha)J(\beta),\qquad
\mathscr T=q^{14}jT.
$$

Hence the original equations (4) imply

$$
\mathcal R=\mathscr T^2-\mathscr E^2\mathscr P=0,\qquad
\mathcal N=j^3E_0^3(\mathscr D\mathscr Q)^6+4\mathscr T^3=0.
\tag{7}
$$

Every original physical point in the boundary also has

$$
\boxed{\mathcal U=E_0\delta_H\mathscr E\mathscr D\mathscr Q\mathscr P\ne0.}
\tag{8}
$$

Indeed (3) supplies the first factors; the others express the nonzero central/V and endpoint/V pairings, distinct V sources, and nonzero V/V pairing. No additional unit is assumed.

## 5. The actual rational identity and its scope

On the basis $1,X,X^2$, the frozen program forms the six columns
$\mathcal R X^i,\mathcal N X^i$ for $i=0,1,2$, reduced modulo the entire monic $C_X$. Exact rational RREF constructs cofactor elements a,b. It then actually verifies, first as a rational matrix product and then by full polynomial remultiplication,

$$
\boxed{\mathcal U^3=a\mathcal R+b\mathcal N\pmod{C_X}.}
\tag{9}
$$

The reported matrix rank is three. The actual cofactor-vector serialization SHA-256 is

f490ac74c415442e13b88970b892098f415d042496be9fbd71e4a94f8b043473.

No claimed inverse depends on selecting a root of $C_X$. At every original point, (7) and (9) force $\mathcal U^3=0$, contradicting (8). This proves the entire original boundary (2) empty.

The verified boundary stage completed in 0.160614919 seconds in Actions run
45823574259 / job 139921814446, from source commit
a8213d2429c498852dde5602ccb9019251f01ff6.

The source Git blob is 91171f618666a743f37d1958408eab22a28ea5c7, SHA-256
524def82887ca5f082561ec6ee8c3939b470f49fc3892408829928269a958635.

The same job subsequently entered a different, generic $\ell(A)\ne0$ norm calculation and did not finish it. Its 600-second alarm was delivered after the native calculation returned; the observed driver duration was 662.582268362 seconds, maximum child RSS 263492 KiB, source exit code 1. No generic norms, gcd, factorization or exclusion are claimed. The actual pull before the run reached a39e5a6f88c9695ae43abcc6358679a422c4d5e8 with both governing README blobs unchanged.

This lemma closes only the genuine zero-leading endpoint fiber at original central H source minus six. The rest of that center is included in the new general finite-center original-N equations; the failed generic norm input is not rerun. Other Gram types, the global Bell power task and ordinary ISP remain open.

