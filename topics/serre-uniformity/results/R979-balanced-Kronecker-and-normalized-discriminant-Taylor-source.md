# R979 — The actual balanced Kronecker coefficient as a normalized discriminant Taylor coefficient

Date: 2026-11-20. Author: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: exact characteristic-zero source comparison; the local Kummer-coordinate comparison is not proved.**
This result applies R975 to the actual discriminant in R977. It retains the
Cayley coordinate, the complex period, the sign of the original curve, and
the normalized differential on the isogeny quotient. No arithmetic
calculation is executed.

## 1. The universal Ramanujan flow and its logarithmic discriminant

Retain R975's polynomial derivation
\[
\mathcal R=\frac{E^2-X}{12}\partial_E+
 \frac{EX-Y}{3}\partial_X+\frac{EY-X^2}{2}\partial_Y,
\qquad
\mathcal F_n(X,Y)=\left.\mathcal R^{n-1}E\right|_{E=0}.
\tag{979.1}
\]
The discriminant polynomial satisfies the exact identity
\[
\mathcal R(X^3-Y^2)=E(X^3-Y^2).
\tag{979.2}
\]
For the formal solution with initial point \((E,X,Y)=(0,0,Y_0)\),
\(Y_0\ne0\), it follows that
\[
\log\frac{X(T)^3-Y(T)^2}{-Y_0^2}
 =\sum_{n\ge1}\mathcal F_n(0,Y_0)\frac{T^n}{n!}.
\tag{979.3}
\]
There is no ambiguity of additive constant: the argument of the formal
logarithm has constant term one. This is a formal identity over
\(\mathbf Q[Y_0,Y_0^{-1}]\), obtained by differentiating and using (979.1).

## 2. The exact analytic flat coordinate

Let \(\tau_0=\zeta=(-1+\sqrt{-3})/2\), \(y_0=\operatorname{Im}\tau_0\), and
\[
u=\frac{\tau-\tau_0}{\tau-\bar\tau_0},\qquad
\tau(u)=\frac{\tau_0-\bar\tau_0u}{1-u}.
\tag{979.4}
\]
Write \(s_0=-4\pi y_0\) and \(t=s_0u\). The following holomorphic functions
of \(u\), not almost-holomorphic functions of both \(u\) and \(\bar u\),
satisfy exactly the Ramanujan equations with respect to \(t\):
\[
\begin{aligned}
\widetilde E&=\frac{E_2(\tau(u))}{(1-u)^2}
 -\frac{3}{\pi y_0(1-u)},\\
\widetilde X&=\frac{E_4(\tau(u))}{(1-u)^4},\\
\widetilde Y&=\frac{E_6(\tau(u))}{(1-u)^6}.
\end{aligned}
\tag{979.5}
\]
For example \(2\pi i\,d\tau/du=s_0/(1-u)^2\). Thus
\[
\frac{d\widetilde X}{dt}
=\frac{4E_4}{s_0(1-u)^5}
 +\frac{E_2E_4-E_6}{3(1-u)^6}
=\frac{\widetilde E\widetilde X-\widetilde Y}{3},
\]
because \(12/s_0=-3/(\pi y_0)\). To check the other two equations
explicitly, put \(v=1-u\) and \(a_0=12/s_0\). Then
\[
\frac{d\widetilde E}{dt}
=\frac{E_2^2-E_4}{12v^4}
 +\frac{2E_2}{s_0v^3}+\frac{a_0}{s_0v^2}
=\frac{(E_2/v^2+a_0/v)^2-E_4/v^4}{12}
=\frac{\widetilde E^2-\widetilde X}{12},
\]
and
\[
\frac{d\widetilde Y}{dt}
=\frac{6E_6}{s_0v^7}+
 \frac{E_2E_6-E_4^2}{2v^8}
=\frac{\widetilde E\widetilde Y-\widetilde X^2}{2}.
\]
All \(E_k\) in these derivative checks are evaluated at \(\tau(u)\).
At \(u=0\) one has \(\widetilde E=0\), since
\(E_2^*(\tau_0)=0\), and \(\widetilde X=0\). In particular this construction
does not assert that the holomorphic value \(E_2(\tau_0)\) is zero.

The normalized analytic discriminant is
\[
\mathscr D(u)=
\frac{\Delta(\tau(u))}{(1-u)^{12}\Delta(\tau_0)},\qquad
\Delta=(E_4^3-E_6^2)/1728.
\tag{979.6}
\]
It has constant term one and no zero for \(|u|<1\). Directly,
\[
\frac{d}{dt}\log\mathscr D(u)=\widetilde E(t).
\tag{979.7}
\]

Now let \(\Lambda=\Omega(\mathbf Z+\tau_0\mathbf Z)\) be the lattice of a
specified elliptic curve with its specified invariant differential. Put
\[
\lambda_\Omega=\left(\frac{\Omega}{2\pi i}\right)^2,\qquad
T=\lambda_\Omega t=\frac{\Omega^2y_0}{\pi}u.
\tag{979.8}
\]
The period is squared in (979.8); it is not replaced by its absolute square.
The algebraic variables
\[
E=\widetilde E/\lambda_\Omega,\qquad
X=\widetilde X/\lambda_\Omega^2,\qquad
Y=\widetilde Y/\lambda_\Omega^3
\]
again satisfy (979.1), now with respect to \(T\). Their initial invariants are
\[
X(0)=12g_2,\qquad Y(0)=-216g_3.
\tag{979.9}
\]
For the original \(E_-:y^2=x^3-1\), \(dz=dx/(2y)\), one has
\((g_2,g_3)=(0,4)\), so \(Y(0)=-864\). The original positive real
generator \(\Omega_-\) may be used, and then the multiplier in (979.8)
equals the actual lattice area divided by \(\pi\):
\[
T=\mathcal A u,\qquad
\mathcal A=\Omega_-^2y_0/\pi.
\]
In the old note on the original Schwarz frame, (PL6) uses the parameter
\(t_{\rm PL}=-\mathcal A u/3\). Thus the exact relation is
\(T=-3t_{\rm PL}\); the two parameters are not silently identified.

Combining (979.3), (979.6)–(979.9), and R975.15 gives the complete generating
identity
\[
\boxed{\quad
\log\frac{\Delta(\tau(u))}{(1-u)^{12}\Delta(\tau_0)}
 =\sum_{n\ge1}\mathcal F_n(0,-864)\frac{T^n}{n!}
 =12\sum_{n\ge1}(n-1)!\,c_n^-T^n,
\quad T=\mathcal A u.
\quad}
\tag{979.10}
\]
Here \(c_n^-=[z^nw^{n-1}]\sigma(z+w;0,4)/
(\sigma(z;0,4)\sigma(w;0,4))\) is the precise coefficient of
R973–R975. At degree three, the logarithm has coefficient
\(\mathcal F_3(0,-864)/3!=-4\), consistently with \(c_3^-=-1/6\).
This is a consequence of the proved source normalization, not an
additional numerical check.

## 3. The \(E_+\) model used in R977

For \(E_+:y^2=x^3+1\) with \(dz=dx/(2y)\), the invariants are
\((g_2,g_3)=(0,-4)\), and the initial Ramanujan value in (979.9) is \(+864\).
Choose \(\epsilon=e^{\pi i/6}\) and \(\Omega_+=\epsilon\Omega_-\).
Then \(\epsilon^6=-1\), as required by the invariants. Set
\(\xi=\epsilon^2=-\zeta^2\in\mu_6\). Consequently
\[
T_+=\xi T_-,\qquad
c_n^+=\epsilon^{-2n}c_n^-.
\tag{979.11}
\]
By homogeneity, a nonzero term has \(3\mid n\); the two actual rows have
\(n\equiv3\pmod6\). For them (979.11) is simply \(c_n^+=-c_n^-\).
The product \(c_n^+T_+^n=c_n^-T_-^n\) retains the same analytic
discriminant in (979.10). These are exact equalities in the chosen frames,
not merely assertions about valuations. In particular the zero/nonzero
status at \(p\ge41\) is unchanged by this model transport.

The exact coarse formal coordinate is \(W=T^3\). In that coordinate the
same normalized logarithm is
\[
\mathscr G_\pm(W)=12\sum_{j\ge1}(3j-1)!\,c_{3j}^\pm W^j.
\tag{979.12}
\]
For the original \(n=p-r=3(m-b)\), its coefficient at degree \(m-b\) is
therefore \(12(n-1)!c_n^\pm\). The multiplier is a \(p\)-unit because
\(n<p\). Thus R975 and R977 really single out the same numerical degree
in two different coarse coordinates; the unresolved issue is the
specified arithmetic transport from \(W\) to \(\rho\), not a mismatch
of degrees. This statement alone does not assert that transport is
linear, integral, or diagonal in those degrees.

## 4. The actual \(p\)-isogeny discriminant and the remaining coordinate problem

Retain precisely R977's normalization
\[
\phi:E_+\longrightarrow E_+/C,\qquad
\phi^*\omega_C=\omega,\qquad
D_C=\frac{\Delta(E_+/C,\omega_C)}{\Delta(E_+,\omega)}.
\tag{979.13}
\]
The quotient differential \(\omega_C\) here is not generally the
primitive differential of a good integral model. If
\(C=\langle\Omega_+/p\rangle\), its quotient lattice is
\((\Omega_+/p)(\mathbf Z+p\tau_0\mathbf Z)\), so
\[
D_C=p^{12}\frac{\Delta(p\tau_0)}{\Delta(\tau_0)}.
\tag{979.14}
\]
This is R977.5, with its essential factor \(p^{12}\).

Define, for this complex representative,
\[
u_p=\frac{(p-1)\tau_0}{p\tau_0-\bar\tau_0},\qquad
T_p=\frac{\Omega_+^2y_0}{\pi}u_p.
\tag{979.15}
\]
Since \(p\tau_0\) is in the upper half-plane, \(|u_p|<1\).
The analytic identity (979.10) on the \(E_+\) frame gives the exact
multiplicative formula
\[
\boxed{\quad
D_C=[p(1-u_p)]^{12}
\exp\left(12\sum_{n\ge1}(n-1)!\,c_n^+T_p^n\right).
\quad}
\tag{979.16}
\]
Writing it multiplicatively avoids an arbitrary branch of a complex
logarithm of \(D_C\).

Independently of (979.16), logarithmic differentiation of the modular
function in (979.14), before evaluating at the CM point, gives
\[
\Theta\log\!\left(p^{12}\frac{\Delta(p\tau)}{\Delta(\tau)}\right)
=pE_2(p\tau)-E_2(\tau)
=pE_2^*(p\tau)-E_2^*(\tau).
\tag{979.17}
\]
The nonholomorphic corrections cancel because
\(\operatorname{Im}(p\tau)=p\operatorname{Im}\tau\). Thus at \(\tau_0\)
this derivative is \(pE_2^*(p\tau_0)\), not a low derivative at \(\tau_0\).

R977 uses the tame Kummer coordinate
\[
\rho^m=-p,\qquad m=(p+1)/3,\qquad
\delta_p=D_C/\rho^4,
\]
and asks for \([\rho^{m-b}]\log\langle\delta_p\rangle\bmod p\), where
\(b=1\) or \(3\). Formula (979.16) does not identify this coefficient
with a coefficient of (979.10). In particular:

- \(T\) is the explicitly normalized Gauss–Manin/Cayley parameter;
  \(\rho\) is an arithmetic tame uniformizer.
- The factor \([p(1-u_p)]^{12}\) in (979.16) and the normalization
  \(\rho^4\) of R977 both have to be retained.
- The complex expression \(T_p\) contains the squared CM period. No
  \(p\)-adic period or integral comparison is supplied by replacing it
  formally with \(\rho\) or with a parameter of the target \(j\)-invariant.
- The complex series (979.16) is not asserted to be a convergent \(p\)-adic
  series at a substituted arithmetic point.

Thus the two routes now have an exact common characteristic-zero
discriminant source. The additional arithmetic statement needed to
identify their finite local coefficients is a comparison of the actual
isogeny period frame with the specified Kummer coordinate. No such
comparison, all-prime unit, or completion of the original problem is
claimed here.

## References

- [R975](R975-original-balanced-Kronecker-integral-heat-recurrence.md):
  the actual balanced coefficient, the universal Ramanujan polynomial, and
  the factor \(12n!(n-1)!\).
- [R977](R977-original-Robert-norm-and-normalized-isogeny-discriminant.md):
  the specified isogeny differential, \(p^{12}\) in the analytic ratio,
  \(\delta_p=D_C/\rho^4\), and the two local logarithm coordinates.
- [Original Schwarz frame note](../notes/2026-11-15-sigma-original-Schwarz-frame-and-critical-Lagrange-source.md),
  (PL5)–(PL6): the original Cayley period and the separate parameter
  \(t_{\rm PL}\). Its old eighteen-point convolution is not repeated here.
