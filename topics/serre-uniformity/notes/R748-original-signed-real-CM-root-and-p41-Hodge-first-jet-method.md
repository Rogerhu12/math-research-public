# R748 — Exact recovery of the original signed real CM root at p = 41

**Status:** proved algorithm and normalization. Numerical outputs are to be
registered only after the public repository Actions run succeeds. This
method reuses the completed R717 integer traces and the R745 original
Hodge input. It does not rerun a toric fiber enumeration, an approximate
functional equation, or a discrete Fourier transform.

## 1. Original objects and the exact field identity

Set

$$
p=41,\quad n=42,\quad \eta=e^{2\pi i/42},\quad
\zeta=\eta^{14},\quad \beta=\eta+\eta^{-1},\quad
F_0=\mathbf Q(\beta),\quad A=\mathbf Q(\eta).
\tag{748.1}
$$

The positive real cube root is $\alpha=\sqrt[3]4$ and
$s_0=1+2\zeta=\sqrt{-3}$ with positive imaginary part. The six
positive primitive labels are

$$
\mathcal H=\{1,13,19,25,31,37\}.
\tag{748.2}
$$

They specify the actual six embeddings of $F_0$, with
$\beta_h=2\cos(2\pi h/42)$. The finite character has the retained
Teichmüller label $\eta\bmod41=(7,30)$ in the basis $(1,\zeta)$;
in particular $\eta^{14}\bmod41=\zeta$. None of these labels is
replaced by an arbitrary primitive generator.

Let $N$ be the original R588 norm of the averaged vector
$u=A_{\mathsf T_\zeta}e_0$, and let

$$
P=\frac{S_2S_3}{C_0^2}.
\tag{748.3}
$$

R717 already provides the exact polynomial $\mathcal P(X)$ with
integer coefficients such that

$$
\mathcal P(\eta)=42DP,\qquad
D=2^{37}3^{26}41^5.
\tag{748.4}
$$

The letter $\mathcal P$ here denotes that retained integer trace
polynomial. It is not the signed square root defined next. R745
provides $N$ itself as twelve integral coefficients in
$A=\mathbf Q[X]/(\Phi_{42})$, so no new finite torus calculation
is necessary.

R747 proves that the original flat derivative $M_2$ determines
the signed element

$$
T=\frac{42\alpha M_2}{144(1-\zeta^2)}
  =\frac{42}{432}\,\widehat M_2
  \in F_0,\qquad
\widehat M_2=\alpha s_0\zeta^2 M_2,
\qquad T^2=2NP.
\tag{748.5}
$$

The phase $\zeta^2$ in $\widehat M_2$ is applied once: it is the
actual $g_*$ transport to the marked point $c_1$. The raw
$M_2$ in (748.5) is still the absolutely normalized R588 value.
R747 also proves

$$
D_TT\in\mathcal O_{F_0},
\qquad D_T=2^{18}3^{13}41^2.
\tag{748.6}
$$

Thus both $R=2NP\in F_0$ and a sufficient integral denominator
are known exactly. A square-root routine alone would determine
only $\{T,-T\}$. Sections 4–6 determine the original sign.

## 2. Exact reconstruction without choosing an unproved integral basis

All polynomial arithmetic in this section is over $\mathbf Q$.
Compute $\Phi_{42}$, the powers of $\eta$, and
$\beta=\eta+\eta^{-1}$. Solve the exact linear system expressing
$\beta^6$ in the independent basis

$$
1,\beta,\ldots,\beta^5.
\tag{748.7}
$$

This constructs the monic minimal polynomial $f_\beta$ and
checks its degree six inside $A$. The same exact linear system
expresses $R$ in that basis. In particular no real floating point
recognition is used to move from $A$ to $F_0$.

Form the integral trace Gram matrix and its discriminant

$$
G_{ij}=\operatorname{Tr}_{F_0/\mathbf Q}(\beta^{i+j}),
\quad 0\le i,j\le5,\qquad
\Delta=\det G>0.
\tag{748.8}
$$

Every trace can be computed by summing the six exact
automorphisms $\eta\mapsto\eta^h$, $h\in\mathcal H$, and
checking that the result is a rational integer. The determinant
is computed exactly, with fraction-free divisions checked.

There is no need to assume that $\mathbf Z[\beta]$ is the full
ring of integers. If
$D_TT=\sum_{i=0}^5 z_i\beta^i$, then

$$
G(z_i)_{i=0}^5
 =\bigl(\operatorname{Tr}(D_TT\beta^j)\bigr)_{j=0}^5
 \in\mathbf Z^6,
\tag{748.9}
$$

because both $D_TT$ and $\beta$ are integral. Multiplication by
the adjugate gives

$$
W:=\Delta D_TT\in\mathbf Z[\beta].
\tag{748.10}
$$

For each of the six real embeddings, interval arithmetic
encloses $\beta_h$ and $R_h=R(\beta_h)>0$. Positivity is
certified by strict ball comparisons. The program computes the
six positive square roots $\sqrt{R_h}$, constructs the Lagrange
polynomials

$$
L_h(X)=\prod_{\substack{k\in\mathcal H\\k\ne h}}
       \frac{X-\beta_k}{\beta_h-\beta_k},
\tag{748.11}
$$

and considers the $2^5$ sign patterns with the first sign
positive. For one such pattern, the six coefficient balls of

$$
\sum_{h\in\mathcal H}
 \varepsilon_h\,\Delta D_T\sqrt{R_h}\,L_h(X)
\tag{748.12}
$$

enclose the integer coefficients of the root with positive
first embedding. A candidate is accepted only when every
coefficient ball contains a unique integer and the exact
identity

$$
W(X)^2=(\Delta D_T)^2R(X)\pmod{f_\beta(X)}
\tag{748.13}
$$

holds. Thus ball rounding merely proposes an exact identity;
it is not the proof of that identity. Conversely, (748.6)–(748.10)
prove that increasing precision must eventually reveal the
actual coefficient vector. Because $F_0$ is a field and
$R\ne0$, there are exactly two roots, which are negatives of
one another. After one exact nonzero root has been found,
enumerating the other sign patterns supplies no further
mathematical information.

The recovered polynomial is initially named $T_+$, where
$T_+(\beta_1)>0$. No assertion that $T_+$ is the original
$T$ is made until the analytic sign test below succeeds.

## 3. Retained absolute Fourier coordinates

R745 supplies the original gauge $c_0=0$ and integral
polynomials $c_r(\eta)$, $1\le r\le40$, with

$$
u=\sum_{r=1}^{40}\frac{c_r(\eta)}{1722}e_r,
\qquad 1722=41\cdot42.
\tag{748.14}
$$

The raw functions and the original full parameter are

$$
H_0^\circ(\tau)=f_\theta(\tau/246),\quad
H_2^\circ(\tau)=f_\theta(4\tau/246),\quad
F^\circ=A_{\mathsf T_\zeta}
       (H_0^\circ-4\zeta^2H_2^\circ),\quad
Q=e^{2\pi i\tau/246}.
\tag{748.15}
$$

Write $\xi=e^{2\pi i/41}$, and let $v=6^{-1}\bmod41$.
The integral CRT translation is $k_r=6(rv\bmod41)$; it
satisfies $k_r\equiv0\bmod6$ and $k_r\equiv r\bmod41$.
Consequently

$$
B_\nu=\frac1{1722}\sum_{r=1}^{40}
 c_r(\eta)\xi^{-\nu rv},
\qquad
F^\circ(\tau)=\sum_{\nu\ge1}a_\nu B_\nu t_\nu Q^\nu,
\tag{748.16}
$$

where

$$
t_\nu=
\begin{cases}
1,&\nu\text{ odd},\\
-s_0,&4\mid\nu,\\
0,&\nu\equiv2\pmod4.
\end{cases}
\tag{748.17}
$$

To verify the even coefficient, use the actual inert-two
relation $a_{4m}=-2a_m$. The second summand in (748.15)
contributes $-4\zeta^2a_mB_{4m}$ at $Q^{4m}$, so together
the coefficient is
$(1+2\zeta^2)a_{4m}B_{4m}=-s_0a_{4m}B_{4m}$.
There is no additional factor of $246$ in the raw form.
That factor appears only on converting the actual differential
$2\pi iF^\circ\,d\tau$ to the $Q$ parameter.

The character coefficients already supplied by R745 through
$\nu=800$ are reused verbatim. If a larger cutoff is required,
only the additional coefficients are formed:

$$
a_\nu=
\sum_{\substack{a^2-ab+b^2=\nu\\
                 a\equiv1,\ b\equiv0\ (3)}}
 (a+b\zeta)\,
 \eta^{-\log_\gamma(\overline y/y)},
\qquad y=(a+b\zeta)\bmod41,\quad41\nmid\nu.
\tag{748.18}
$$

For $41\mid\nu$ the coefficient is zero. The $42$ powers of
the already fixed $\gamma=(7,30)$ suffice to label the new
terms. Formula (748.18) never repeats the R745 torus fiber
calculation. A checkpoint records every completed new range;
the retained first $801$ coefficient arrays are checked to be
unchanged.

## 4. Strict full tails for the original form and its derivatives

The original positive finite Hermitian form has matrix
$41I-J$ in the gauge $c_0=0$, with eigenvalues $1$ and $41$.
The torus average is an orthogonal projection, so

$$
G(u,u)\le G(e_0,e_0)=40,\qquad
\sum_{r=1}^{40}\left|\frac{c_r}{1722}\right|^2\le40,
\qquad
\sum_{r=1}^{40}\left|\frac{c_r}{1722}\right|\le40.
\tag{748.19}
$$

These are bounds in the specified positive complex embedding;
the same proof works in every other embedding. Each ideal of
norm $\nu$ contributes a complex number of absolute value
$\sqrt\nu$ to the normalized CM newform, and there are at most
$d(\nu)$ such ideals. Pairing divisors around $\sqrt\nu$ gives
$d(\nu)\le2\sqrt\nu$. Hence

$$
|a_\nu|\le d(\nu)\sqrt\nu\le2\nu,\qquad
|a_\nu B_\nu t_\nu|\le80\sqrt3\,\nu.
\tag{748.20}
$$

At $\tau=\zeta$ the actual parameter is

$$
Q=e^{-\pi i/246}r,\qquad
r=e^{-\pi\sqrt3/246}\in(0,1).
\tag{748.21}
$$

For $D=q\,d/dq=(2\pi i)^{-1}d/d\tau$, a term $Q^\nu$
has derivative multiplier $\nu/246$. Therefore truncation at
$B$ gives, for $k=0,1,2$, the rigorous bounds

$$
\left|D^kF^\circ(\zeta)
 -\sum_{\nu=1}^B
   a_\nu B_\nu t_\nu(\nu/246)^kQ^\nu\right|
\le\frac{80\sqrt3}{246^k}
          \sum_{\nu>B}\nu^{k+1}r^\nu.
\tag{748.22}
$$

The tails are evaluated as finite rational functions of $r$
with nonnegative coefficients. Explicitly, if $b=B+1$,

$$
\sum_{\nu>B}\nu^k r^\nu
=r^b\sum_{j=0}^k\binom kj b^{k-j}
 \sum_{\ell=0}^j
 \left\{\begin{matrix}j\\\ell\end{matrix}\right\}
 \frac{\ell!\,r^\ell}{(1-r)^{\ell+1}}.
\tag{748.23}
$$

Here the braces are the Stirling numbers of the second kind,
with the usual value $\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=1$.
This identity follows by expanding $(b+m)^k$ and then writing
$m^j$ in falling factorials. Its positive form avoids
cancellation in the error bound.

All radii include floating point enclosure errors as well as
the analytic tail (748.22). Root of unity phases are each
evaluated directly from an exact rational argument, rather
than by a long sequence of rectangular complex-ball rotations.
Positive real powers of $r$ cause no such rotation.

The program also evaluates

$$
E_6(\zeta)=1-504\sum_{\nu\ge1}\sigma_5(\nu)q^\nu,
\qquad q=-e^{-\pi\sqrt3}.
\tag{748.24}
$$

Since $\sigma_5(\nu)\le\zeta(5)\nu^5<2\nu^5$, cutoff $B_6$
has error at most

$$
1008\sum_{\nu>B_6}\nu^5|q|^\nu,
\tag{748.25}
$$

again evaluated by (748.23). Nonvanishing of the resulting
$E_6$ ball is checked before division.

## 5. The original sign

R592's original $c_1$ deck selection implies
$F^\circ(\zeta)=DF^\circ(\zeta)=0$. This is an exact
transformation-law statement, not a numerical guess. Thus the
ordinary second derivative equals the raised derivative:

$$
\partial_4\partial_2F^\circ(\zeta)
 =\delta_4\delta_2F^\circ(\zeta)
 =D^2F^\circ(\zeta).
\tag{748.26}
$$

The program checks that the separately enclosed zeroth and
first derivatives contain zero as a normalization check; the
proof of (748.26) is the deck selection. R742's absolute
period identity is

$$
M_2=-864\,
\frac{D^2F^\circ(\zeta)}{E_6(\zeta)}.
\tag{748.27}
$$

Combining (748.5) and (748.27) gives the exact complex
expression for the original real root:

$$
T_{\rm CM}
 =-\frac{6\alpha\cdot42}{1-\zeta^2}\,
       \frac{D^2F^\circ(\zeta)}{E_6(\zeta)}.
\tag{748.28}
$$

The complete ball for (748.28) must have imaginary interval
containing zero and real interval strictly separated from
zero. If either check fails, no sign is certified; the retained
stages remain available for a further range or precision.
The working cutoff or precision is not itself a proof of
separation. Once separation succeeds, it selects exactly one
of $T_+$ and $-T_+$. The selected algebraic embedding must
overlap the real CM ball, and its square is checked exactly
again using (748.13). These checks keep the original phase,
Fourier direction, period, and average-versus-trace
normalization visible in the certificate.

Only the first embedding needs this analytic sign test.
R747 proves that the other five original signed values are the
coefficient conjugates of this single element $T\in F_0$.
They are not chosen independently from six positive square
roots.

## 6. Six exact first jets in the actual rational Hodge basis

Use precisely the R745 global basis

$$
\omega_j=2\pi i\,\alpha s_0
 \operatorname{Tr}_{F_0/\mathbf Q}
 \bigl(\beta^jF^\circ\bigr)\,d\tau,
\qquad 0\le j\le5.
\tag{748.29}
$$

At the original marked $c_1$, slash by $g_*$ once supplies
$\zeta^2$. Equation (748.5) therefore gives its canonical
flat second derivative

$$
\widehat M_{2,j}
 =\frac{432}{42}
     \operatorname{Tr}_{F_0/\mathbf Q}(\beta^jT)
 \in\mathbf Q.
\tag{748.30}
$$

R592 gives $z_{\rm flat}^3=(3/8)(a-1)+O((a-1)^2)$.
The flat primitive starts as
$\widehat M_{2,j}z_{\rm flat}^3/6$. Consequently the actual
coarse Abel integral in the parameter $s=a-1$ has first
coefficient

$$
[s]\int_{c_1}^{x(s)}\omega_j
 =\frac{\widehat M_{2,j}}{16}
 =\boxed{\frac9{14}
        \operatorname{Tr}_{F_0/\mathbf Q}(\beta^jT)}.
\tag{748.31}
$$

Every trace in (748.30)–(748.31) is computed exactly from the
signed polynomial and the exact trace matrix. These are
coordinates in the actual rational Hodge basis defined in
R745. The statement neither identifies a Néron basis nor
declares any quotient comparison scalar to be a unit.

## 7. Public computation contract and scope

The request fixes the R717 integer-polynomial and completed
receipt hashes, the successful R745 run and input hashes, the
new source hash, precision, cutoff, and method hash. The core
refuses to execute the actual arithmetic outside the public
repository Actions environment. Completed exact-field,
new-coefficient, square-root, and CM-sign stages are retained
with compatible configuration and input hashes. A successful
final receipt is reused rather than recomputed.

The exact field identity, all coefficient-rounding balls, all
tail bounds, the direct CM ball, the selected original sign,
and all six rational traces are saved. Failure also preserves
the completed stages and an explicit incomplete receipt.
Neither finite fibers nor old R717 traces are regenerated.

The outcome is an exact signed original first Hodge jet at the
specified prime. It is not a computation of an abelian
quotient map, the point $\beta=q[c_1-c_0]$, a height, or a
Serre-uniformity exclusion.

## References and dependencies

- R588: original torus average, absolute norm, and CM period
  normalization.
- R592: actual raw tame vector, complete integral flat
  coordinates, and the coarse change of variable.
- R717: previously certified original integer trace
  polynomial; its existing public artifact is reused.
- R742: exact Serre derivative and the $-864$ period identity.
- R745: original finite vector and rational Hodge basis,
  Fourier labels, and the first $800$ newform coefficients.
- R747: the original signed real square root, its coherent
  Galois conjugates, and its full denominator bound.
- Python-FLINT 0.9.0, official Arb and Acb API documentation:
  https://python-flint.readthedocs.io/en/latest/arb.html and
  https://python-flint.readthedocs.io/en/latest/acb.html.

