# R150 appendix: the aligned phase of the reduced rank-three, degenerate-Gram, zero-Hp branch is impossible

Date: 2026-11-26 UTC. Author: Astra-ISP-347c-20261126 / prior_results_map; AI-assisted GPT-6 Astra Pro.

**Status: proved physical exclusion.** Under rank H=3, rank V=2 and essential dimension six, suppose H has three distinct physical sources and degenerate Gram, and Hp=0. The all-opposite pairing phase d_i=-c_i at all three H sources is impossible. Combined with the [finite-phase classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md), only the two nontrivial cube-root phases remain; this does not yet exclude those phases.

## 1. Original normalization and nonzero quantities

The [complete reduced-H degenerate-Gram reduction](R150-appendix-rank-three-reduced-second-cumulant-degenerate-gram-essential-six-gaussian-reduction.md) pays the normalization

$$
F=1,\qquad H=\tfrac12(z_1^2+z_2^2+z_3^2),
\qquad V=\tfrac12(u^3+v^3),
$$
$$
Hp=0,\quad p=Ky,\quad p(u)=p(v)=e,\quad 2e^3=-1.
$$

The physical H Gram is

$$
B_H=
\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\quad gh\ne0,\quad g^2+h^2=-1.
$$

Write m_i=(B_H^2)_{ii}, so (m_1,m_2,m_3)=(-1,g^2,h^2), all nonzero.

Assume the aligned phase

$$
c_i=K(z_i,u),\qquad d_i=K(z_i,v)=-c_i
\quad (i=1,2,3).
$$

The original polar equation at z_i is 2e(c_i^2+d_i^2)=m_i; hence

$$
c_i^2=\frac{m_i}{4e}. \tag{1.1}
$$

All divisions by e,m_i below are legitimate. No jet or restricted-parameter replacement of the original polar equation is used.

## 2. Homogeneous physical polars and their common divisor

To cover finite and infinite source points in one argument, use the homogeneous rational normal curve

$$
u_5(X,Y)=(X^5,X^4Y,X^3Y^2,X^2Y^3,XY^4,Y^5)^T.
$$

Define binary quintics and the binary decic

$$
P(X,Y)=K(y,u_5(X,Y)),\quad
U(X,Y)=K(u,u_5(X,Y)),\quad
W(X,Y)=K(v,u_5(X,Y)),
$$
$$
S=U+W,\qquad
\mathcal H(X,Y)=u_5(X,Y)^{\mathsf T}KHK\,u_5(X,Y).
$$

Let the three distinct H sources be t_i in P^1 and write z_i=lambda_i u_5(t_i) with lambda_i nonzero. By Hp=0 and the aligned phase, P(t_i)=0 and S(t_i)=0 for all three i.

Let D be the product of their three distinct homogeneous linear factors. It has degree three, including an X factor when one source is infinity. There are homogeneous binary quadratics A and C such that

$$
P=DA,\qquad S=DC. \tag{2.1}
$$

This is ordinary divisibility by a squarefree divisor, so neither a special affine chart nor a generic-root assumption is used.

The complete original highest polar identity is

$$
P^3-6P\mathcal H+2(U^3+W^3)=0.
$$

Since U^3+W^3=S^3-3UWS, substitute (2.1) and cancel the nonzero polynomial D in the polynomial integral domain:

$$
D^2(A^3+2C^3)-6(A\mathcal H+CUW)=0. \tag{2.2}
$$

All terms, in particular the mixed product UW, are retained.

## 3. Three actual source values force the quadratic identity

At t_i, the scaled original pairings give

$$
\mathcal H(t_i)=\frac{m_i}{2\lambda_i^2},
\qquad
U(t_i)W(t_i)=\frac{c_id_i}{\lambda_i^2}
=-\frac{m_i}{4e\lambda_i^2}. \tag{3.1}
$$

Evaluate (2.2) at t_i. Its D^2 term vanishes, and (3.1), with m_i and lambda_i nonzero, gives

$$
A(t_i)-\frac{C(t_i)}{2e}=0\qquad (i=1,2,3).
$$

A homogeneous binary quadratic vanishing at three distinct projective points is the zero polynomial. Consequently

$$
A=\frac{C}{2e},\qquad
P=\frac{U+W}{2e}. \tag{3.2}
$$

This interpolation includes the infinity source and every possible drop in affine degree. No derivative or quotient value was guessed: A and C were genuine homogeneous quotients before evaluating at the roots of D.

The coefficient map z -> K(z,u_5(X,Y)) is injective because the six degree-five monomials form a basis and K is invertible. Thus (3.2) also gives the vector identity

$$
y=\frac{u+v}{2e}.
$$

Pair with u. The original physical vector u is isotropic, K(u,u)=0, and K(v,u)=e. Therefore

$$
e=p(u)=K(y,u)=\frac{e}{2e}=\frac12.
$$

This contradicts 2e^3=-1. Equivalently, the displayed vector identity would already place T_3 in Ran H+Ran V, of dimension at most five, contrary to the essential-six hypothesis.

The aligned phase is therefore excluded on every physical source chart.

## 4. Updated remaining branch

The [finite-phase classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md) proves that the only possible phase pattern was

$$
(\omega_1,\omega_2,\omega_3)=(\omega^2,\omega,\omega),
\qquad d_i=-\omega_i c_i.
$$

This appendix removes omega=1. The remaining two nontrivial values satisfy

$$
\omega^2+\omega+1=0,\qquad
2e^3=-1,\qquad
(2g^2+1)^2=-e^2,\qquad g^2+h^2=-1.
$$

Up to the already paid column signs, the earlier upper bound of eighteen normalized Grams drops to twelve. These mixed-phase forms still require the full original physical equations; no characteristic-zero computation or modular test has been used or asserted here.
