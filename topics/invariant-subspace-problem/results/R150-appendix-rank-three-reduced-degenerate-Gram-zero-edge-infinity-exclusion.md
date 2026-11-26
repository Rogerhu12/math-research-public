# R150 appendix: the primitive-phase reduced-H branch with an infinite zero edge is empty

Date: 2026-11-26 UTC. Author: Astra-ISP-347c-20261126 / prior_results_map; AI-assisted GPT-6 Astra Pro.

## Status and exact scope

**Status: proved physical exclusion.** The two-variable necessary reduction below has actually been excluded by exact rational resultants whose extended gcd is one. The complete original physical source and scale argument is retained; no modular calculation is used.

Assume the original R150 critical point has rank H=3, rank V=2 and essential dimension six; H has three distinct sources, its Gram is degenerate, and Hp=0. The [complete Gaussian reduction](R150-appendix-rank-three-reduced-second-cumulant-degenerate-gram-essential-six-gaussian-reduction.md) and [finite-phase classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md) give, after the allowed weighted normalization,

$$
F=1,\quad H=\tfrac12(z_1^2+z_2^2+z_3^2),\quad
V=\tfrac12(u^3+v^3),
$$
$$
B_H=
\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\quad gh\ne0,\quad g^2+h^2=-1,\quad 2e^3=-1,
\quad e=uKv=p(u)=p(v).
$$

The [aligned phase has already been excluded](R150-appendix-rank-three-reduced-degenerate-Gram-aligned-phase-physical-exclusion.md) by the original highest-polynomial interpolation. For either remaining primitive cube root omega,

$$
c_1=C_1,\quad c_2=gr,\quad c_3=-hr,\qquad
d_1=-\omega^2C_1,\quad d_2=-\omega gr,\quad d_3=\omega hr,
$$
$$
\omega^2+\omega+1=0,\quad
\delta=2g^2+1,\quad \delta^2=-e^2,\quad
2\delta C_1r=1.
$$

Here c_i=z_iKu and d_i=z_iKv; every displayed divisor e,g,h,delta,C_1,r is nonzero.

This appendix handles exactly the case in which the unique zero H edge contains infinity. The other H point on that edge is forced to be -1, because the original kernel satisfies k(t,infinity)=-(t+1). Relabel the two equal-phase endpoints as

$$
z_2=\lambda_2u(-1),\qquad z_3=\lambda_3u(\infty),\qquad
z_1=\lambda_1u(s).
$$

All lambda_i are nonzero and s is finite, s!=-1. Essential dimension six forces the five H/V physical source points to be distinct, so

$$
u=\rho u(\alpha),\qquad v=\sigma u(\beta)
$$

have finite distinct alpha,beta, neither equal to -1 or s, and rho,sigma are nonzero. No remaining source-at-infinity case lies inside this particular chart.

## 1. The original zero-edge polar yields one cubic

The original kernel is

$$
k(s,t)=-(t-s)^2\bigl[
s^3-5s^2+(s^3-3s^2+22s)t
 -(3s^2+3s+5)t^2+(s+1)t^3\bigr].
$$

Put

$$
p(t)=5t^3+31t^2+32t+6.
$$

Directly from this kernel,

$$
k(-1,t)=(t+1)p(t),\qquad k(t,\infty)=-(t+1).
$$

The nonzero H edges are

$$
g=\lambda_1\lambda_2(s+1)p(s),\qquad
h=-\lambda_1\lambda_3(s+1).
$$

Thus both s+1 and p(s) are nonzero.

The two endpoint pairings of u give

$$
\rho(\alpha+1)=-\lambda_1(s+1)r,\qquad
\rho(\alpha+1)p(\alpha)=\lambda_1(s+1)p(s)r.
$$

The corresponding v pairings give

$$
\sigma(\beta+1)=\omega\lambda_1(s+1)r,\qquad
\sigma(\beta+1)p(\beta)=-\omega\lambda_1(s+1)p(s)r.
$$

All cancellations are among the already nonzero physical factors. Therefore

$$
\boxed{p(\alpha)=p(\beta)=-p(s).}\tag{1.1}
$$

Let x=alpha+beta, z=alpha beta and X=5x+31. The third root of p(t)+p(s), counted with its multiplicity, is -X/5. Vieta's identities give

$$
z=\frac{X^2-31X+160}{25},
$$
$$
\boxed{
\mathcal C(s,X)=X^3-31X^2+160X
 -125s^3-775s^2-800s-300=0.
}\tag{1.2}
$$

The third cubic root is allowed to equal alpha or beta. No cubic discriminant has been divided out; this multiple-root fiber is retained.

Write

$$
Z=X^2-31X+160,\quad E=X^2-26X+30,\quad
D=-3X^2+62X+321.
$$

Then

$$
(\alpha+1)(\beta+1)=E/25,\qquad
(\alpha-\beta)^2=D/25.
$$

Both E and D are nonzero in the physical chart.

## 2. The central H pairings and a small quadratic polar

For a root t of p(t)+p(s), define F_s(t)=k(s,t)/(t+1). The division is legitimate because p(-1)=0 and p(s)!=0 exclude t=-1.

The actual central pairings are

$$
C_1=-\lambda_1^2(s+1)rF_s(\alpha),\qquad
-\omega^2C_1=\omega\lambda_1^2(s+1)rF_s(\beta).
$$

Consequently

$$
\boxed{F_s(\beta)=\omega F_s(\alpha),}\tag{2.1}
$$

with both sides nonzero.

Define integer polynomials

$$
a=100s^2+400s+1003,
$$
$$
b=-75s^3-65s^2-480s+1196,
$$
$$
c=75s^4+465s^3+1483s^2+1376s+516,
\qquad \Phi_s(t)=at^2+bt+c.
$$

Direct exact division gives

$$
\boxed{
25k(s,t)+2(s+1)(t+1)\Phi_s(t)
\equiv0\pmod{p(t)+p(s)}.
}\tag{2.2}
$$

Thus F_s(t)=-2(s+1)Phi_s(t)/25 on every root, including a multiple cubic root. In particular Phi_s(alpha) and Phi_s(beta) are nonzero, and their ratio is omega.

To express their sum and product symmetrically set

$$
A=25c-aZ,\qquad B=5b+a(X-31),
$$
$$
S=2A+B(X-31),
$$
$$
P=A^2+AB(X-31)+B^2Z.
$$

Reduction modulo t^2-xt+z gives

$$
25\,[\Phi_s(\alpha)+\Phi_s(\beta)]=S,\qquad
625\,\Phi_s(\alpha)\Phi_s(\beta)=P.
$$

Since omega is a primitive cube root, equation (2.1) implies

$$
\boxed{\mathcal R(s,X)=S^2-P=0.}\tag{2.3}
$$

This symmetric equation retains both primitive phases. It is a necessary condition; no inverse reconstruction from it is asserted.

## 3. The original V pairing eliminates e over QQ

Let k_ab=k(alpha,beta) and E_ab=(alpha+1)(beta+1). From the nonzero scales above and the identity 2delta C_1r=1,

$$
e=\rho\sigma k_{ab}
 =\frac{\omega(s+1)k_{ab}}
        {2\delta E_{ab}F_s(\alpha)}.
$$

Equivalently,

$$
2e\delta E_{ab}F_s(\alpha)=\omega(s+1)k_{ab}.
$$

Square this equality, multiply by omega, and use
F_s(alpha)F_s(beta)=omega F_s(alpha)^2,
delta^2=-e^2, and 2e^3=-1. The exact consequence is

$$
2eE_{ab}^2F_s(\alpha)F_s(\beta)
 =(s+1)^2k_{ab}^2. \tag{3.1}
$$

No square-root sign is discarded as an exclusion: (3.1) is deliberately only a necessary equation and therefore retains any extra squared solutions.

The original pair kernel factors particularly simply after (1.2). With

$$
q(x,z)=x^3-5x^2+x^2z-6xz+32z-5z^2
$$

one has

$$
625q(x,z)=-4(X-31)(X+9)E,
$$
$$
k_{ab}=-(x^2-4z)q(x,z)
 =\frac{4D(X-31)(X+9)E}{15625}.
$$

Put K_*=D(X-31)(X+9). Substituting this factorization, E_ab=E/25 and (2.2) into (3.1), with all nonzero factors explicitly paid above, gives

$$
\boxed{eP=2K_*^2.}\tag{3.2}
$$

The nonzero V pairing e=rho sigma k_ab shows that X-31 and X+9 are nonzero. Cubing (3.2) and using 2e^3=-1 gives P^3+16K_*^6=0. Finally (2.3) gives the equivalent necessary polynomial

$$
\boxed{\mathcal N(s,X)=S^6+16K_*^6=0.}\tag{3.3}
$$

The universal identity

$$
(P^3+16K_*^6)-\mathcal N
 =-\mathcal R(P^2+PS^2+S^4)
$$

checks this last reduction without any extra division.

## 4. Complete original physical open set for the QQ gate

Every actual point in the present branch therefore satisfies the three rational equations

$$
\mathcal C=\mathcal R=\mathcal N=0
$$

and the nonzero product

$$
\boxed{
\mathcal U=(s+1)p(s)\,E\,D\,(X-31)(X+9)\ne0.
}\tag{4.1}
$$

Each factor has been proved nonzero from an actual original physical pairing or source distinction. Neither a cubic discriminant nor an unspecified resultant leading coefficient has been inverted. The reduction covers both primitive phases, both signs of delta and every nonzero H/V representative scale.

The remaining central-H-at-infinity case, and the case where both zero-edge endpoints are finite, are outside this chart and are not claimed here.

## 5. The actually executed rational unit identity

The [frozen self-contained source](../notes/2026-11-26-reduced-H3-zero-edge-infinity-original-QQ-347c.py) is blob `f32425c6b3fc96a38a550cd10ce3145e501d00e8`.

It verifies (2.2) and the kernel factorizations over QQ directly from the original k, and checks the universal norm reduction. It then reduces R and N by the monic X-cubic C, retaining exact quotient identities. Their remainders R_rem,N_rem have X-degree at most two.

The actual integer resultants are

$$
P_0(s)=\operatorname{Res}_X(\mathcal C,\mathcal R_{\rm rem}),
\qquad
Q_0(s)=\operatorname{Res}_X(\mathcal C,\mathcal N_{\rm rem}).
$$

The actual execution obtained

$$
\deg P_0=23,\qquad \deg Q_0=72,\qquad
\boxed{\gcd_{\mathbb Q[s]}(P_0,Q_0)=1.}
$$

The source computed the extended gcd and explicitly remultiplied its rational polynomials to verify

$$
L_P(s)P_0(s)+L_Q(s)Q_0(s)=1.
$$

The integer-resultant SHA-256 values, computed from their exact FLINT polynomial serialization, are

- P_0: 58cdb616103ff9ea147f0fdeb5573a6dafc5585ffcce87b67b0fd8abfeaf8a7b;
- Q_0: 4bfea033370b46761fce0bb62dc17aa1bea3c7d3f9bef54b4a352b4c46fc15bc.

A common complex root (s,X) of C,R,N would make both resultants vanish at that s. Evaluating the verified extended-gcd identity would then give 0=1. Hence the necessary two-variable system has no common complex root at all. This conclusion is stronger than an exclusion after localization by U; every original physical boundary already retained by the reduction is covered.

No candidate factors were removed: the actual primary-deletion stage recorded zero layers and remaining gcd 1. The source's unused finite-algebra fallback was not entered, and no finite-algebra matrix certificate is claimed as executed.

## 6. Frozen execution identity and conclusion

The actual public execution was run 45815953727, job 139895617025, from source commit

bafa9883e0cf79eac8a9b82a14f15d2615c43bcd.

The source SHA-256 was

0352492a375cc035bc2c23aaace58a677542cb79370b5eb32a405e0a2e0f0786.

The source completed in 0.075555984 seconds; the driver completed in 0.347030920 seconds, with maximum child RSS 75088 KiB and source exit code 0. The [compact actual receipt](../notes/2026-11-26-reduced-H3-zero-edge-infinity-execution-347c.json) is independently stored as Git blob `f455b224ae4261beb67d755cb89ebae48e45c87d`.

Before execution the driver actually pulled main to 3a751a836c60a4f33efa9e0ddd3060a188621adc and verified that the two governing README blobs were unchanged. The complete arithmetic was over QQ; the source did not perform a modular test or extrapolate a modular unit ideal.

Therefore every primitive-phase reduced-H, degenerate-Gram, Hp=0, essential-six critical point whose zero H edge contains infinity is impossible. The aligned phase had already been excluded on all charts. What remains in this reduced-H branch is a finite zero edge, with the central H source either finite or infinity. No assertion is made here about those remaining charts, the nondegenerate H Gram, lower essential dimensions, the Bell natural-power problem, or the ordinary invariant-subspace problem.
