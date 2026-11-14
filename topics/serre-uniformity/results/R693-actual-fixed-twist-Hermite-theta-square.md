# R693 — The actual fixed-cubic-twist central values are explicit Hermite-theta squares

## 1. The theorem, including its limits

Keep the actual character $\xi_k$ and exact period normalization of
R615/R683, and the three-point theta identity R692.  Let $k\ge2$,
$k\equiv2\pmod3$, and write $m=k-1$.  Use the physicists' Hermite
polynomials, defined by

$$
e^{2Xs-s^2}=\sum_{m\ge0}H_m(X)\frac{s^m}{m!}.
\tag{1.1}
$$

Define a real, absolutely convergent sum

$$
U_m=\begin{cases}
\displaystyle\sum_{n\in\mathbf Z}(-1)^n
 H_m\!\left((n+1/3)\sqrt{6\pi\sqrt3}\right)
 e^{-3\pi\sqrt3(n+1/3)^2},&m\equiv1\pmod6,\\[4pt]
\displaystyle\sum_{n\in\mathbf Z}
 H_m\!\left((n+1/2)\sqrt{6\pi\sqrt3}\right)
 e^{-3\pi\sqrt3(n+1/2)^2},&m\equiv4\pmod6.
\end{cases}
\tag{1.2}
$$

Then

$$
\boxed{
L(\xi_k,k)=\frac{2\pi}{3^{1/4}2^m m!}
\begin{cases}
\sqrt{2+\sqrt3}\,U_m^2,&m\equiv1\pmod6,\\[2pt]
\dfrac34\sqrt{2-\sqrt3}\,U_m^2,&m\equiv4\pmod6.
\end{cases}}
\tag{1.3}
$$

In particular these actual central values are nonnegative, and their
vanishing is equivalent to vanishing of the explicitly displayed real
theta derivative.  The cubic character is retained throughout the proof;
the formula is not imported from an untwisted Hecke family.

Writing

$$
\mathcal P_k=\frac{\alpha\beta\Omega\mathcal A^m}{(-3)^m},
\qquad L(\xi_k,k)=\mathcal P_k C_k,
\tag{1.4}
$$

gives the corresponding fully normalized square formula for $C_k$.
Equation (1.3) does not prove that $U_m$ is nonzero, nor does it assert
that its algebraic normalization is a $p$-adic unit.  In particular the
actual all-prime condition $C_pC_{p-3}\ne0\pmod p$ remains open.

## 2. Theta and factorization conventions

Put

$$
\zeta=e^{2\pi i/3},\qquad z=1+\zeta=e^{\pi i/3},\qquad
y=\Im z=\sqrt3/2,\qquad T=-6\overline z=6\zeta.
\tag{2.1}
$$

For $t\in\mathfrak H$ and rational $\mu,\nu$ define

$$
\vartheta_m\!\begin{bmatrix}\mu\\\nu\end{bmatrix}(t)
=\frac{i^{-m}}{(2\pi\Im t)^{m/2}}
\sum_{n\in\mathbf Z+\mu}
H_m\!\left(n\sqrt{2\pi\Im t}\right)
e^{\pi in^2t+2\pi i\nu n}.
\tag{2.2}
$$

These are exactly the Hermite theta conventions in equation (23) of
Rodriguez--Villegas--Zagier, *Square roots of central values of Hecke
L-series*.  Only their general factorization identity is used; their
later Hecke-character square-root theorem has different hypotheses and
is not used.

Let

$$
Q_z(M,N)=\frac{|Mz-N|^2}{2y}
=\frac{M^2-MN+N^2}{\sqrt3}.
\tag{2.3}
$$

The $a=6$, $\alpha=0$ specialization of that factorization is

$$
\begin{aligned}
\mathfrak F_m(\mu,\nu)
:={}&\sum_{M,N\in\mathbf Z}e^{2\pi i(M\nu+N\mu)}
 L_m\!\left(\frac\pi3 Q_z(M,N)\right)
 e^{\frac\pi6(iMN-Q_z(M,N))}\\
={}&\frac{(-1)^m(\pi y)^m\sqrt{12y}}{m!}
\vartheta_m\!\begin{bmatrix}6\mu\\\nu\end{bmatrix}(z/6)
\vartheta_m\!\begin{bmatrix}\mu\\-6\nu\end{bmatrix}(T),
\end{aligned}
\tag{2.4}
$$

where $L_m$ is the ordinary Laguerre polynomial.  All sums in (2.4) are
absolutely convergent.  The cited identity is proved by Poisson summation
and comparison of two Taylor coefficients, and it allows these rational
characteristics without a restriction on the quadratic discriminant.

## 3. The actual cubic weights give a particular finite kernel

For the theta function $\Theta$ of R692 write

$$
F_m(t)=\sum_{N\ge0}a_N L_m(4\pi N\Im t)e^{-2\pi iN\overline t},
\qquad \Theta(t)=\sum_{N\ge0}a_Ne^{2\pi iNt}.
\tag{3.1}
$$

R692 gives, with the exact cubic directions,

$$
\frac{3\sqrt3}{\pi}L(\xi_k,k)
=F_m(2\zeta)-\frac{\zeta^{-1}}2F_m(\zeta/2)
                 -\frac{\zeta^{-2}}2F_m((1+\zeta)/2).
\tag{3.2}
$$

Each $F_m$ can also be written as a sum over the norm form
$r^2-rs+s^2$.  In the common summand on the first line of (2.4),
substitute $M=3r,N=3s$.  The Gaussian and Laguerre argument are exactly
those of the latter two terms of (3.2); its phase is
$e^{3\pi irs/2}$.  The phase ratios needed to obtain the two terms are

$$
f_1(r,s)=i^{r^2+s^2},\qquad
f_2(r,s)=e^{-\pi i(r+s)^2/2}.
\tag{3.3}
$$

The first term of (3.2) is the restriction $M,N\equiv0\pmod6$.
It follows that the right side of (3.2) equals the common sum in (2.4)
weighted by a function $K(M,N)$ of period six.  It is zero unless
$M,N\equiv0\pmod3$, and its four possibly nonzero values are

$$
\begin{array}{c|cc}
K(M,N)&N=0&N=3\\ \hline
M=0&3/2&-\sqrt3/2\\
M=3&-\sqrt3/2&-i\sqrt3/2.
\end{array}
\tag{3.4}
$$

Indeed at each parity of $r,s$ the coefficient is
$\mathbf1_{r,s\text{ even}}-	frac12(\zeta^{-1}f_1+\zeta^{-2}f_2)$.
This derives (3.4) directly from the actual character; no cubic weight
is replaced by one.

Its finite Fourier expansion is

$$
K(M,N)=\sum_{r,s=0}^5\kappa_{rs}e^{2\pi i(Ms+Nr)/6},
\tag{3.5}
$$

where

$$
\kappa_{rs}=
\frac{3-\sqrt3\bigl((-1)^r+(-1)^s\bigr)
                    -i\sqrt3(-1)^{r+s}}{72}.
\tag{3.6}
$$

## 4. The S transformation turns the factorization into a quadratic form

The Hermite theta convention (2.2) satisfies

$$
\vartheta_m\!\begin{bmatrix}\mu\\\nu\end{bmatrix}(-1/t)
=t^m\sqrt{-it}\,e^{2\pi i\mu\nu}
\vartheta_m\!\begin{bmatrix}\nu\\-\mu\end{bmatrix}(t).
\tag{4.1}
$$

The square root is the usual holomorphic one on the upper half-plane.
One direct proof uses the generating series

$$
\sum_{m\ge0}\vartheta_m\!\begin{bmatrix}\mu\\\nu\end{bmatrix}(t)
\frac{U^m}{m!}
=e^{U^2/(2\pi\Im t)}
 \sum_{n\in\mathbf Z+\mu}e^{\pi in^2t+2\pi i\nu n-2inU}
\tag{4.2}
$$

and the usual Gaussian Poisson formula, replacing $U$ by $U/t$ on the
transformed side.  The Gaussian completion in (4.2) cancels the Jacobi
exponential, leaving exactly (4.1).

Since $|z|=1$, $z/6=-1/T$.  Put

$$
v_r=\vartheta_m\!\begin{bmatrix}r/6\\0\end{bmatrix}(T),
\qquad
\mathsf M_{rs}=\kappa_{rs}e^{-2\pi irs/6}.
\tag{4.3}
$$

Take $\mu=r/6,\nu=s/6$ in (2.4).  The factor
$e^{2\pi irs/6}$ from (4.1) cancels the integral-characteristic shift
in its first theta factor.  The second factor contributes
$e^{-2\pi irs/6}$.  Thus (3.2), (3.5), and (2.4) give

$$
L(\xi_k,k)=\frac\pi{3\sqrt3}
\frac{(-1)^m(\pi y)^m\sqrt{12y}}{m!}
T^m\sqrt{-iT}\,v^{\mathsf t}\mathsf Mv.
\tag{4.4}
$$

This step retains every characteristic shift and its phase.

## 5. The CM fixed point leaves exactly one theta direction

For varying $t$ set
$V_r(t)=\vartheta_m\bigl[\begin{smallmatrix}r/6\\0\end{smallmatrix}\bigr](6t)$.
Poisson summation and direct translation give

$$
\begin{aligned}
V_r(-1/t)&=\frac{t^m\sqrt{-it}}{\sqrt6}
              \sum_{s=0}^5e^{-2\pi irs/6}V_s(t),\\
V_r(t+1)&=e^{\pi ir^2/6}V_r(t).
\end{aligned}
\tag{5.1}
$$

Let $\mathsf F_{rs}=e^{-2\pi irs/6}$ and
$\mathsf D_{ss}=e^{\pi is^2/6}$.  Since
$\zeta=-1/(\zeta+1)$, equation (5.1) implies

$$
\mathsf F\mathsf Dv=\lambda_m v,
\qquad
\lambda_m=\begin{cases}
\sqrt3(1-i),&m\equiv1\pmod6,\\
-\sqrt3(1-i),&m\equiv4\pmod6.
\end{cases}
\tag{5.2}
$$

Also $v_{6-r}=(-1)^mv_r$ by $n\mapsto-n$ in (2.2).
Solving these finite equations gives

$$
v=v_2\left(0,a,1,0,-1,-a\right)^{\mathsf t},
\qquad a=\frac{(1+\sqrt3)(1+i)}2,
\quad m\equiv1\pmod6,
\tag{5.3}
$$

and

$$
v=v_3(b,c,d,1,d,c)^{\mathsf t},\qquad
\begin{cases}
b=(1-\sqrt3)(1-i)/2,\\
c=(1-i\sqrt3)/4,\\
d=(2-\sqrt3+i)/4,
\end{cases}
\quad m\equiv4\pmod6.
\tag{5.4}
$$

These are exact one-dimensional spaces, not a numerical rank claim.
Here is a short rank certificate.  In the odd parity basis
$(v_1,v_2)$, row $1$ of $\mathsf F\mathsf D-\lambda_m I$ has first
entry $-3i/2-\sqrt3(1-2i)/2\ne0$, while (5.3) is an explicit kernel
vector.  In the even parity basis $(v_0,v_1,v_2,v_3)$, the submatrix
using rows $0,1,2$ and columns $0,1,2$ has determinant

$$
-6\sqrt3-12i\sqrt3-18i\ne0,
\tag{5.5}
$$

while (5.4) is an explicit kernel vector.  Hence the ranks are precisely
one and three respectively.  All entries belong to
$\mathbf Q(i,\sqrt3)$.

Substitution in the explicit quadratic form (4.3) gives

$$
v^{\mathsf t}\mathsf Mv=
\begin{cases}
\dfrac{2+\sqrt3-i}{2}\,v_2^2,&m\equiv1\pmod6,\\[3pt]
\dfrac{3(1-\sqrt3)(1-i)}8\,v_3^2,&m\equiv4\pmod6.
\end{cases}
\tag{5.6}
$$

Equations (5.2)--(5.6) can be checked by direct multiplication of the
displayed six-by-six matrices.  The accompanying exact finite-algebra
checker `R693_verify_theta_matrices.py` verifies all 36 finite Fourier
identities, both kernel vectors, the nonzero minors, and both quadratic
scalars in $\mathbf Q(i,\sqrt3)$.  It uses only Python's standard library.
It was actually executed and produced `R693-matrix-certificate.json`.

## 6. Removing the phases and completing the proof

At $T=6\zeta$ the real parts of the quadratic exponent have constant
phase on each of the two relevant arithmetic progressions.  With
$U_m$ defined in (1.2), one obtains directly from (2.2)

$$
v_2=i^{-m}e^{-\pi i/3}(12\pi y)^{-m/2}U_m,
\quad m\equiv1\pmod6,
\tag{6.1}
$$

and

$$
v_3=i^{-m}e^{-3\pi i/4}(12\pi y)^{-m/2}U_m,
\quad m\equiv4\pmod6.
\tag{6.2}
$$

For (6.1), use
$e^{-3\pi i(n+1/3)^2}=(-1)^n e^{-\pi i/3}$.
For (6.2), $n(n+1)$ is even, so
$e^{-3\pi i(n+1/2)^2}=e^{-3\pi i/4}$.

The common scalar in (4.4) simplifies using

$$
\sqrt{12y}\sqrt{-iT}=6\,3^{1/4}e^{\pi i/12},
\qquad \zeta^m=\zeta.
\tag{6.3}
$$

Substitute (5.6) and (6.1)--(6.3) into (4.4).  The phases cancel.
The remaining real factors are respectively
$\sqrt{2+\sqrt3}$ and $\tfrac34\sqrt{2-\sqrt3}$, and
$(6\pi y)^m(12\pi y)^{-m}=2^{-m}$.  This proves (1.3).

## 7. Executed normalization diagnostics

A small diagnostic using 60-digit arithmetic and $-12\le n\le12$
in (1.2) gave the following values after dividing by the *unchanged*
period factor (1.4):

| $k$ | $C_k$ from the square expression |
| ---: | ---: |
| 2 | $-0.5$ |
| 5 | $4.5$ |
| 8 | $-1.157142857142857142857143$ |
| 11 | $138.8571428571428571428571$ |

They match the exact Kronecker outputs $-1/2,9/2,-81/70,972/7$.
These floating-point values only check the normalization; equations
(2.4)--(6.3) supply the proof.  They do not establish an infinite
nonvanishing statement, and no prime scan was used for this derivation.

## Primary source and dependency boundary

- R692 supplies the actual three-point weight-one theta expression.
- R615/R683 supply only the exact period normalization and the actual
  fixed-cubic-twist character.
- Rodriguez--Villegas--Zagier, *Square roots of central values of Hecke
  L-series*, equation (23), printed page 7:
  <https://people.mpim-bonn.mpg.de/zagier/files/mpim/92-68/fulltext.pdf>.
  Its general Poisson factorization is used.  Its final special
  Hecke-character theorem, ordinary interpolation, and any unproved
  nonvanishing assertion are not used.

