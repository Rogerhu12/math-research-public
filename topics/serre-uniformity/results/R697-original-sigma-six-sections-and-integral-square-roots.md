# R697 — Original sigma-six sections and arithmetic square roots of the actual central values

Date: 2026-11-14. Status: **proved** (arithmetic square-root identity and integrality away from 6). The all-prime unit assertion and the main Serre-uniformity problem remain open.

## 1. Exact statement

Use the original curve and period of R615/R683,

$$
E_0:y^2=x^3-1,\qquad dz=dx/(2y),\qquad
\Lambda=\Omega\mathbf Z[\zeta],\qquad \Omega>0.
\tag{697.1}
$$

Let $\sigma(z)=z+O(z^7)$ be its Weierstrass sigma function, and write
$x(z)=\wp_\Lambda(z)$ and $y(z)=\wp_\Lambda'(z)/2$.
For $k\ge2$, $k\equiv2\pmod3$, put $m=k-1$ and define

$$
\boxed{
A_k=\begin{cases}
\displaystyle 2^{-(m-1)/2}m![z^m]\bigl(-x(z)y(z)\sigma(z)^6\bigr),
&m\equiv1\pmod6,\$$3pt]
\displaystyle 2^{-m/2}m![z^m]\bigl(x(z)\sigma(z)^6\bigr),
&m\equiv4\pmod6.
\end{cases}}
\tag{697.2}
$$

These are rational numbers.  Their exact connection with the *actual*
full six-torsion Kronecker numbers is

$$
\boxed{
-2(k-1)!C_k=A_k^2\quad(k\equiv2\pmod6),\qquad
\frac{(k-1)!C_k}{3}=A_k^2\quad(k\equiv5\pmod6).
}
\tag{697.3}
$$

Moreover

$$
\boxed{A_k\in\mathbf Z[1/6].}
\tag{697.4}
$$

This last assertion does not silently remove the factorial: the $m!$ in
(697.2) is essential, and is incorporated as an ordinary derivative in
the integrality proof below.  No integrality at the primes $2$ and $3$ is
asserted.

In particular, for every prime $p\ge41$, $p\equiv5\pmod6$,

$$
\boxed{
C_p\equiv-3A_p^2,\qquad C_{p-3}\equiv-3A_{p-3}^2\pmod p.
}
\tag{697.5}
$$

Thus the actual first-term condition is equivalent to
$A_pA_{p-3}\ne0\pmod p$.  Neither (697.3) nor (697.4) proves this
nonvanishing.  The result gives exact arithmetic square roots and a
characteristic-$p$ Bell recursion with no division by $p$.

## 2. The six Jacobi functions are sections of the original degree-six line bundle

Put $y_0=\Im\zeta=\sqrt3/2$.  For $r\in\mathbf Z/6\mathbf Z$ define
the entire function

$$
\mathcal F_r(z)=
\exp\!\left(\frac{3\pi z^2}{y_0\Omega^2}\right)
\sum_{n\in\mathbf Z+r/6}
\exp\!\left(6\pi in^2\zeta+\frac{12\pi inz}{\Omega}\right).
\tag{697.6}
$$

This includes the Gaussian factor and the actual characteristic $r/6$;
neither is omitted.  For the Hermite theta of R693 it satisfies

$$
\mathcal F_r^{(m)}(0)=(-6\pi/\Omega)^m
\vartheta_m\!\begin{bmatrix}r/6\\0\end{bmatrix}(6\zeta).
\tag{697.7}
$$

Indeed substitute $U=-6\pi z/\Omega$ in the exact Hermite generating
identity (R693(4.2)).

The equianharmonic lattice has completed weight-two constant zero.
Equivalently its quasiperiods satisfy

$$
\eta_\lambda=\overline\lambda/\mathcal A,
\qquad \mathcal A=\Omega^2y_0/\pi.
\tag{697.8}
$$

One can see this directly: write the quasiperiod map as
$a\lambda+\overline\lambda/\mathcal A$ using Legendre's relation.
The CM relation $\eta_{\zeta\lambda}=\zeta^{-1}\eta_\lambda$ forces
$a=0$.

Translation by $\Omega$ in (697.6) leaves the theta sum unchanged.
Translation by $\Omega\zeta$ is evaluated by replacing $n$ with $n+1$.
The resulting multipliers, including the Gaussian, are exactly

$$
\mathcal F_r(z+\lambda)
=\exp\!\left(6\eta_\lambda(z+\lambda/2)\right)\mathcal F_r(z)
\qquad(\lambda\in\Lambda).
\tag{697.9}
$$

They are the multipliers of $\sigma(z)^6$; the sigma sign has sixth
power one.  Consequently $\mathcal F_r/\sigma^6$ is an elliptic
function with its only pole at $O$, of order at most six.  The six
functions in (697.6) are linearly independent: after removing the
common Gaussian, their Fourier exponents $6n$ lie in six disjoint
residue classes modulo six.  Riemann--Roch gives $h^0(E_0,6O)=6$, so
they form a basis of $H^0(E_0,\mathcal O(6O))$ in this trivialization.

A rational basis is

$$
\sigma^6,\quad x\sigma^6,\quad y\sigma^6,\quad
x^2\sigma^6,\quad xy\sigma^6,\quad x^3\sigma^6.
\tag{697.10}
$$

Under $z\mapsto uz$, $u\in\mu_6$, one has
$\sigma(uz)=u\sigma(z)$, $x(uz)=u^{-2}x(z)$ and
$y(uz)=u^{-3}y(z)$.  The corresponding degree classes in (697.10)
are $0,4,3,2,1,0$.  Thus the class zero has dimension two, class five
is absent, and the two classes actually needed here, one and four,
each have dimension one.  In particular the projections of
$\mathcal F_r$ to those classes are multiples of

$$
G(z)=-xy\sigma^6=z+O(z^7),\qquad
F(z)=x\sigma^6=z^4+O(z^{10}).
\tag{697.11}
$$

It follows exactly, whenever the indicated base derivative is nonzero,
that

$$
\frac{\mathcal F_r^{(m)}(0)}{\mathcal F_r'(0)}
=m![z^m]G\quad(m\equiv1\pmod6),
\tag{697.12}
$$

and

$$
\frac{\mathcal F_r^{(m)}(0)}{\mathcal F_r^{(4)}(0)}
=\frac{m!}{24}[z^m]F\quad(m\equiv4\pmod6).
\tag{697.13}
$$

This identifies the entire subsequences, not a finite list of matching
Taylor coefficients.

## 3. Calibrating the original sigma coefficients against the actual central values

In the odd-$m$ case use $r=2$; in the even-$m$ case use $r=3$, as in
R693.  Their base derivatives are nonzero because R683 gives
$C_2=-1/2$ and R615 gives $C_5=9/2$, and the R693 square scalars are
nonzero.

For two indices $m,m_0$ in the same one of these residue classes,
R693(4.4)--(5.6), followed by (697.7), gives

$$
\frac{L(\xi_{m+1},m+1)}{L(\xi_{m_0+1},m_0+1)}
=\left(\frac{\mathcal A}{6}\right)^{m-m_0}
\frac{m_0!}{m!}
\left(\frac{\mathcal F_r^{(m)}(0)}
           {\mathcal F_r^{(m_0)}(0)}\right)^2.
\tag{697.14}
$$

Here $m-m_0$ is divisible by six, so the factors $(-1)^{m-m_0}$ and
$\zeta^{m-m_0}$ are one.  Dividing by the unchanged R615 period
normalization gives

$$
\frac{m!C_{m+1}}{m_0!C_{m_0+1}}
=2^{m_0-m}
\left(\frac{\mathcal F_r^{(m)}(0)}
           {\mathcal F_r^{(m_0)}(0)}\right)^2.
\tag{697.15}
$$

Take $m_0=1$ and $m_0=4$ respectively and use (697.12)--(697.13).
The two base values $C_2=-1/2$, $24C_5=108$ yield exactly
(697.2)--(697.3).  The Laurent coefficients of $x,y$ and the Taylor
coefficients of $\sigma$ are rational for the rational invariants
$g_2=0,g_3=4$.  This proves $A_k\in\mathbf Q$ directly, without an
unproved Galois descent for a theta constant.

For example the first terms give $A_2=1$, $A_5=6$, $A_8=-108$ and
$A_{11}=12960$.  Their signs are fixed by (697.2), not chosen after
squaring.

## 4. A fixed tame six-isogeny supplies integral ordinary derivatives

To prove the denominator assertion, put $r=\alpha=\sqrt[3]4$ and
$b=\beta=\sqrt3$, with their positive real embeddings.  The real
point $Q=\Omega/6$ on $E_0$ has

$$
x(Q)=X=2+r+r^2,
\qquad x(2Q)=r,\qquad x(3Q)=1.
\tag{697.16}
$$

The cyclic quotient by $\langle Q\rangle$ has period lattice

$$
\Lambda'=\Lambda+\mathbf Z\Omega/6
     =(\Omega/6)(\mathbf Z+6\zeta\mathbf Z).
\tag{697.17}
$$

Thus its real period is $\Omega'=\Omega/6$, and its modular parameter
is $6\zeta$, exactly the one in (697.6).  The quotient is taken in
this direction, with invariant differential $dz$ preserved.

Writing the quotient as $y'^2=x'^3+a x'+c$, its coefficients and
completed weight-two constant are

$$
\begin{aligned}
a&=-180r^2-240r-375,\\
c&=-2100r^2-3360r-5566,\\
s&=2r^2+4r+5.
\end{aligned}
\tag{697.18}
$$

These can be obtained directly from the lattice addition formula:

$$
x'(z)=x(z)+\sum_{0\ne T\in\langle Q\rangle}
                  (x(z+T)-x(T)).
\tag{697.19}
$$

Equivalently the finite sums are
$a=-15\sum x(T)^2$ and $c=69-35\sum x(T)^3$, with the five nonzero
points.  For the zeta function, integrating (697.19) gives an additional
linear term $z\sum x(T)$.  The quasiperiod and covolume terms both
scale by six, so the completed weight-two constant is
$s=\sum x(T)=2X+2r+1$.  This proves (697.18), including the sign of $s$.

More precisely, let $\sigma'$ be the sigma function for $\Lambda'$ and
let $Q_j=\Omega'((j/6-1/2)6\zeta-1/2)$.  The ratio in question is

$$
\frac{\mathcal F_j(z)}{\mathcal F_j(0)}
=e^{-sz^2/2}\frac{\sigma'(z+Q_j)}{\sigma'(Q_j)}
  e^{-(sQ_j+\overline Q_j/\mathcal A')z},
\qquad \mathcal A'=\mathcal A/6.
\tag{697.19a}
$$

Both sides have their simple zero at $-Q_j$, the same two theta
multipliers for $\Lambda'$, and value one at zero.  Their quotient is
therefore a constant elliptic function, proving the identity.  Its
logarithmic derivative is
$\zeta_{\Lambda'}(z+Q_j)-s(z+Q_j)-\overline Q_j/\mathcal A'$.
Hence, if its ordinary derivatives are denoted by
$f_n=f^{(n)}(0)$, they are given by the polynomial differential system

$$
Dx=2y,\qquad Dy=3x^2+a,\qquad De=-x-s,
\qquad Df=ef,
\tag{697.20}
$$

with $f(0)=1$.  The Gaussian in (697.6) is what produces the term
$-s$ in $De$; omitting it would change the square roots.

## 5. The two initial points and the only denominators

For $j=3$, the theta characteristic is $[1/2,0]$ and the corresponding
point is the real half-period $\Omega'/2$.  Its initial data are

$$
x_+=5+2r^2+2b(r^2+2r+3),\qquad y_+=0,\qquad e_+=0.
\tag{697.21}
$$

For $j=2$, the characteristic is $[1/3,0]$.  Relative to the odd
theta characteristic $[1/2,1/2]$, its point is

$$
Q_2=-\Omega'\zeta-\Omega'/2
    =-\Omega\zeta/6-\Omega/12.
\tag{697.22}
$$

Its initial data are

$$
\begin{aligned}
x_2&=(b-4)r^2+(2b-6)r-6b-1,\\
y_2&=i\bigl((12-9b)r^2+(12b-24)r+6b+12\bigr),\\
e_2&=i\bigl((b-1)r^2/2+r+b+1\bigr).
\end{aligned}
\tag{697.23}
$$

Here the completed zeta uses the same $s$ as (697.18).  One explicit
derivation of (697.23) is as follows.  Let $D_0=\Omega\zeta/6$ on
$E'$, and let $R=2D_0=\Omega\zeta/3$.  Applying (697.19) and its
derivative to the original point $(r\zeta,-b)$ gives

$$
x_R=-3r^2-6r-3,\qquad
y_R=-i(3r^2-6r+2),\qquad e_R=-i(r+1).
\tag{697.24}
$$

The three half-period abscissae on $E'$ are

$$
-10-4r^2,\qquad 5+2r^2\pm2b(r^2+2r+3).
\tag{697.25}
$$

The first is the image of the original nonreal two-torsion under the
six-isogeny.  If $T_-$ has the minus abscissa in (697.25), then
$Q_2=R+T_-$.  This follows directly from their periods: both sides
have twice the point equal to $-R$ and three times the point equal to
$T_-$.  Using the addition formula for $x,y$ and
$e(P+T_-)=e(P)+y(P)/(x(P)-x(T_-))$ gives (697.23).

All entries of (697.18), (697.21), and (697.23) belong to
$\mathbf Z[1/2,r,b,i]$.  System (697.20), when used for **ordinary
derivatives**, only takes additions and multiplications and integral
binomial coefficients.  Therefore every $f_n$ is integral at every
prime above a rational prime $p\ge5$.

For the even-$m$ branch the base derivative is

$$
f_4^+=192b+(96b+168)r^2+(144b+240)r+384,
\tag{697.26}
$$

and its norm from $\mathbf Q(r,b)$ is

$$
N(f_4^+)=2^{26}3^{10}.
\tag{697.27}
$$

For the odd-$m$ branch write $f_1=e_2=iE_2$.  Then

$$
N_{\mathbf Q(r,b)/\mathbf Q}(E_2)=-648=-2^3 3^4.
\tag{697.28}
$$

For example the intermediate norms over $\mathbf Q(r)$ are

$$
f_4^+(b)f_4^+(-b)=6912(2r^2+3r+4),\qquad
E_2(b)E_2(-b)=-3r^2-6.
\tag{697.29}
$$

These identities, the curve equations for the initial points, and the
finite additions above can all be checked in the six-dimensional
algebra $\mathbf Q[r,b]/(r^3-4,b^2-3)$.  In particular the base
derivatives are units above every $p\ge5$.

Since normalization by $\mathcal F_j(0)$ cancels in derivative ratios,
(697.12)--(697.15) give the equivalent root formulas

$$
A_k=\begin{cases}
2^{-(m-1)/2}\,f_m/f_1,&m\equiv1\pmod6,\$$2pt]
6\,2^{-(m-4)/2}\,f_m^+/f_4^+,&m\equiv4\pmod6.
\end{cases}
\tag{697.30}
$$

Every factor in (697.30) is integral at every $p\ge5$, and each
denominator is a unit there by (697.27)--(697.28).  Together with the
already proved rationality of $A_k$, this proves (697.4).

## 6. Characteristic-p Bell recursion and actual residues

For $p\ge41$, $p\equiv5\pmod6$, use the unique $r\in\mathbf F_p$
with $r^3=4$ and the quadratic algebra
$\mathbf F_p[b]/(b^2-3)$.  This algebra is allowed to split; inversion
of a base derivative is still valid because its norm is a unit.

For the even-$m$ branch take (697.21), (697.18), and the ordinary
derivative recurrence

$$
\begin{aligned}
X_{n+1}&=2Y_n,\\
Y_{n+1}&=3\sum_{j=0}^n\binom nj X_jX_{n-j}+a\,\mathbf1_{n=0},\\
E_{n+1}&=-X_n-s\,\mathbf1_{n=0},\\
F_{n+1}&=\sum_{j=0}^n\binom nj E_jF_{n-j}.
\end{aligned}
\tag{697.31}
$$

For the odd-$m$ branch one can avoid adjoining $i$.  Put
$X_n=i^{-n}D^nx$, $Y_n=i^{-n-1}D^ny$,
$E_n=i^{-n-1}D^ne$, and $F_n=i^{-n}D^nf$.
Start from $x_2,y_2/i,e_2/i,1$ in (697.23).  The first and last
recurrences in (697.31) stay unchanged, while the middle two become

$$
Y_{n+1}=-3\sum_{j=0}^n\binom nj X_jX_{n-j}-a\,\mathbf1_{n=0},
\qquad
E_{n+1}=X_n+s\,\mathbf1_{n=0}.
\tag{697.32}
$$

The ordinary derivative ratio in (697.30) is then
$f_m/f_1=i^{m-1}F_m/F_1=(-1)^{(m-1)/2}F_m/F_1$.
All operations are additions, multiplications, and divisions by the
two already proved units; there is no division by $p$ or by an unknown
factorial.  The outputs for (697.30) have zero $b$ coefficient, because
they are reductions of the rational $A_k$ of (697.2).

Finally Wilson's theorem gives $(p-1)!\equiv-1$ and
$(p-4)!\equiv1/6\pmod p$.  Applying (697.3) proves (697.5).
This recovers the actual R658/R683 residues through arithmetic square
roots, without the two-digit division of R685.

The standalone implementation is `R697_Bell_square_roots.py`, with
interface `--prime P --output FILE`.  It uses only Python's standard
library.  The separate exact checker `R697_verify_tame_initial_data.py`
checks the fixed algebraic data and norms over
$\mathbf Q[r,b]/(r^3-4,b^2-3)$.

Two targeted normalization executions were made, one with $3$ a
nonsquare modulo $p$ and one with the quadratic algebra split:

| $p$ | $A_p$ | $A_{p-3}$ | $C_p$ | $C_{p-3}$ |
| ---: | ---: | ---: | ---: | ---: |
| 41 | 10 | 24 | 28 | 35 |
| 47 | 2 | 30 | 35 | 26 |

The $C$ residues agree with the independently retained Kronecker and
direct-coefficient values.  Each new Bell calculation took less than
0.004 seconds on the development machine.  No new prime window was run.
The exact fixed-algebra certificate also records
$A_2=1,A_5=6,A_8=-108,A_{11}=12960,A_{14}=-4152384,
A_{17}=-177759360$.

The recursion uses $O(p^2)$ field operations and $O(p)$ storage for
each of the two weights.  It supplies a new exact representation of
the remaining nonvanishing problem; it does not solve that problem.

## Dependencies

- R615/R683: definition of $C_k$, actual character and exact period
  normalization, including $C_2=-1/2$ and $C_5=9/2$.
- R693: actual Hermite theta square, with the full cubic weights and
  finite $S,ST$ phases.  No ordinary-prime interpolation is used.
- Standard sigma and addition identities, here with their multipliers,
  linear terms, and six-isogeny direction explicitly fixed.

