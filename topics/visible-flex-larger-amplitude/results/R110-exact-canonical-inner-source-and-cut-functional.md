# R110: Exact canonical correlations for a signed inner source

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

This proves exact changes of variables, bounds with fixed radial modal
masses, and a
signed cut functional for the same true auxiliary head as R39/R74.
It provides a concrete decomposition for evaluating the inner DN about
its true nonmean linear field. The complete auxiliary correction,
the full mean root, the inverse, the additional full-frequency head
correction and the true far boundary all remain present.

The background is the true source of
[R26](R26-real-head-source-interval-and-port-coordinates.md), and the
auxiliary solution and complete error radius are those of
[R39](R39-actual-strong-m20-node12-low46-head.md) or a separately
certified parameter extension such as
[R74](R74-actual-anisotropic-moving-centre-family.md).

No signed inner source integral or improved numerical cut bound is
claimed here. In particular the current sufficient T-head budget
cannot be reduced numerically just by applying these identities to
the names of old absolute-value fields. Actual signed column/source
enclosures must be supplied.

## 1. Same true coordinates and canonical variable

Fix the real R26 background on a true head cell, with its actual
constant $\mu_n>0$, outward physical radius $r$, $0<w\le1/2$ and $E=1+w^2$.
All Fourier coefficients use $e^{im\theta}$ and include both signs.
For a nonzero even mode m let
$$
h_{\perp,m}=r^4Q_m,\qquad
\Xi_{n,m}=\frac{r^4w}{\sqrt{12}\mu_n}
 \left((h_{\perp,m})_r-\frac{m^2}{r}h_{\perp,m}\right).
\tag{110.1}
$$
This is the height-derivative canonical variable. It is not a
stored nonlinear connection momentum called Pi, nor an independent
rounded metric/source field.

Introduce the positive coefficient functions
$$
\mathfrak a=\frac{r^3}{w},\qquad
\mathfrak d_n=\frac{\sqrt{12}\mu_n}{r^4w^2},\qquad z=w^2.
\tag{110.2}
$$
The letter $\mathfrak d_n$ here is a conversion coefficient, not the
normal discriminant D used in R75/R107.

Let $P=h_\theta/(rw)$ and $\overline K=(h_r-w)_\perp/w$
denote the relative physical nonmean variables of R33.
Equation (110.1) gives, exactly,
$$
\begin{aligned}
P_m&=im\,\mathfrak a Q_m,\\
\overline K_m&=m^2\mathfrak a Q_m+\mathfrak d_n\Xi_{n,m},\\
C_m:=(\overline K+P_\theta)_m&=\mathfrak d_n\Xi_{n,m},\\
U_m:=(\overline K_\theta-P)_m
 &=im\left[(m^2-1)\mathfrak a Q_m+\mathfrak d_n\Xi_{n,m}\right].
\end{aligned}
\tag{110.3}
$$
The physical fields on the two sides of a cell interface agree
under the original canonical change of scale. The factor mu_n
in (110.2) must not be replaced by mu_12 or by mu_11 at other
cells, and no additional interface ratio is inserted after
performing the same conversion once.

For real cosine amplitudes $Q_m$ and $\Xi_m$, write
$P=p_m\sin(m\theta)$ and $\overline K=k_m\cos(m\theta)$.
Then
$$
p_m=-m\mathfrak a Q_m,\quad
k_m=m^2\mathfrak a Q_m+\mathfrak d_n\Xi_m,\quad
C_m^{\cos}=\mathfrak d_n\Xi_m,\quad
U_m^{\sin}=-m[(m^2-1)\mathfrak a Q_m+\mathfrak d_n\Xi_m].
\tag{110.4}
$$
Thus the sine sign is fixed; it is not chosen from an absolute cap.
For complex reflection-symmetric parameter families the same
cosine/sine identities are complex algebraic identities. Their
two Fourier halves are related by parity, not by conjugation.

## 2. The complete inverse also has an exact correlation

The nonmean part of the complete leading denominator is
$$
\Lambda=\overline K+EP_\theta.
$$
Using E=1+z in (110.3) yields
$$
\boxed{\Lambda_m=\mathfrak d_n\Xi_{n,m}
                   -z\,m^2\mathfrak a Q_m.}
\tag{110.5}
$$
In particular one should not enclose the two large terms
$\overline K_m$ and $E(P_\theta)_m$ independently and then infer that
their resulting wide interval is the actual size of $\Lambda_m$.
Equation (110.5) evaluates the same exact function directly.

Set $Z_a=(a^2-1)\mathfrak a Q_a+\mathfrak d_n\Xi_a$.
Here the italic indices $a,b$ are signed frequencies; $\mathfrak a$
is the positive coefficient in (110.2).
For the outward source coordinate $x$, put
$s=r_x/r>0$, $\ell=w_x/w$, and $c_{\rm bg}=s+|\ell|$.
[R106](R106-physical-correlation-and-complete-mean-remainder.md)
writes the nonmean source using the full Laurent numerator
$$
\begin{aligned}
\mathscr Q&=EsU^2+\ell[E C^2-z(\overline K^2+P^2)],\\
\mathscr A(c)&=\ell(2c\Lambda+c^2),\\
\mathcal N_x&=\Pi_\perp
 \frac{\mathscr Q+\mathscr A(c)}{1+c+\Lambda},
\end{aligned}
\tag{110.6}
$$
where $c$ is the complete
[R33](R33-full-head-forcing-on-a-variable-analytic-strip.md) mean root of the nonmean input.
Throughout this result, $\overline K$, $C$, $U$ and $\Lambda$ contain
only nonzero modes. The full mean is supplied separately by $c$;
the bound on $C$ below is not a bound on $c+C$.

The two quadratic materials have the following exact signed
coefficients for every integer output m, including m=0:
$$
\mathscr Q^{(s)}_m
=-Es\sum_{a+b=m}ab\,Z_aZ_b,
\tag{110.7}
$$
$$
\boxed{
\mathscr Q^{(\ell)}_m
=\ell\sum_{a+b=m}\left[
 \mathfrak d_n^2\Xi_a\Xi_b
 -z\mathfrak a\mathfrak d_n
       (a^2Q_a\Xi_b+b^2\Xi_aQ_b)
 -z\,ab(ab-1)\mathfrak a^2Q_aQ_b
\right].}
\tag{110.8}
$$

**Proof.** The radial term follows from $U_a=iaZ_a$.
For the second material, expand $\overline K_a\overline K_b+P_aP_b$
using (110.3). Its $Q_aQ_b$ coefficient is
$(a^2b^2-ab)\mathfrak a^2$, its two cross coefficients are
$a^2\mathfrak a\mathfrak d_n$ and $b^2\mathfrak a\mathfrak d_n$,
and its $\Xi_a\Xi_b$ coefficient is $\mathfrak d_n^2$.
Since $C_a=\mathfrak d_n\Xi_a$ and $E-z=1$, subtracting
$z(\overline K_a\overline K_b+P_aP_b)$ from $EC_aC_b$
gives (110.8). QED.

These formulas preserve all signed products before interval
absolute values. They do not discard the zero mode of
$\mathscr Q$, the $c^2$ term, or any term in the full inverse.
Projection in (110.6) occurs after the product with that inverse.

For one cosine/sine mode, the signed mean quadratic term of
[R107](R107-signed-quadratic-complete-mean-centre.md) becomes
$$
\begin{aligned}
(c_2)_m={}&
\frac{m^2}{4}\big[(m^2-1)-z(m^2+1)\big]\,
                \mathfrak a^2 Q_m^2\\
&-z m^2\mathfrak a\mathfrak d_n Q_m\Xi_m
-\frac{1+3z}{4}\mathfrak d_n^2\Xi_m^2.
\end{aligned}
\tag{110.9}
$$
The sum over positive modes gives c_2. For complex cosine
amplitudes these are squares and products, not absolute squares.
The complete root is still enclosed by the R107 Cauchy tail
$128R^3/(1-32R)$ and the original R33 disk $|c|\le4R^2$,
using the actual joint relative strong norm $R<1/32$.
The quantitative remainder estimates below use $R\le1/64$. Formula (110.9) is an evaluation
centre, not a replacement mean equation.

## 3. Exact canonical columns of the quadratic derivative

For a centre mode a=m-b, define
$$
Z_a=(a^2-1)\mathfrak a Q_a+\mathfrak d_n\Xi_a,\qquad
\Lambda_a=\mathfrak d_n\Xi_a-z a^2\mathfrak a Q_a.
$$
Differentiating the quadratic source gives
$$
(D\mathscr Q[X]e)_m
 =\sum_b\left(J^Q_{m,b}e_{Q,b}
                       +J^\Xi_{m,b}e_{\Xi,b}\right),
\tag{110.10}
$$
where
$$
\begin{aligned}
J^Q_{m,b}
=2\mathfrak a\big[
 &-Es\,ab(b^2-1)Z_a\\
 &-z\ell\{ab(ab-1)\mathfrak a Q_a
                         +b^2\mathfrak d_n\Xi_a\}\big],
\\
J^\Xi_{m,b}
=2\mathfrak d_n\big[-Es\,abZ_a+\ell\Lambda_a\big].
\end{aligned}
\tag{110.11}
$$
A centre mode outside the true centre support contributes zero.
Both factors of two in (110.11) are the differentiation of the
symmetric quadratic form; no additional factor two is attached
when these columns are used.

A $Q$ input has $\delta C=0$, so its $\ell$ material in (110.11)
has an explicit factor $z=w^2$. The $\Xi$ input in that material
depends on the exact $\Lambda_a$, not on unrelated absolute caps
of $\overline K$ and $P_\theta$.
This distinction is lost by replacing the two canonical input
components with one common physical mass before differentiation.

For completeness the derivative of the full source, not just
its quadratic part, is
$$
D\mathcal N_x[e]=\Pi_\perp
 \frac{D\mathscr Q[e]
       +2\ell[(\Lambda+c)Dc[e]+c\,D\Lambda[e]]
       -F\,[Dc[e]+D\Lambda[e]]}
      {1+c+\Lambda},
\tag{110.12}
$$
where $F=(\mathscr Q+\mathscr A(c))/(1+c+\Lambda)$ is the
unprojected full Laurent function and
$$
(D\Lambda[e])_b=\mathfrak d_n e_{\Xi,b}
                           -z b^2\mathfrak a e_{Q,b}.
$$
The exact $Dc$ is the derivative of the same complete R33 root,
for example in the
[R75](R75-complete-mean-transport-and-shear-constraint.md) implicit formula. Setting $Dc=0$ or
replacing $F$ by its nonmean projection in (110.12) would
change the derivative.

## 4. Canonical error bounds in the relative physical norm

Let the true nonmean canonical error e on one cell have fixed
modal masses
$$
\begin{aligned}
q_m&=(1+|m|)^3\sup e^{\tau_{\rm ref}|m|}|e_{Q,m}|,\\
\xi_m&=(1+|m|)\sup e^{\tau_{\rm ref}|m|}|e_{\Xi,m}|,\qquad
\sum_m(q_m+\xi_m)\le\rho.
\end{aligned}
\tag{110.13}
$$
The suprema in (110.13) are over the whole cell at its fixed
reference strip $\tau_{\rm ref}\ge0$. All input sums are signed
sums. The physical strong norm takes the radial supremum separately
for each mode and each component before summation, with weight
$1+|m|$.

For R39 the radius $\rho$ is the complete certified
$(U_n-1)x_n$, including the actual nonlinear far lift.
For a parameter family it must be the corresponding
already-proved family radius, not an old displayed centre
radius silently reused on the new family.

All low modes satisfy $2\le|m|\le M$, with $M=92$. Define
$$
a_M=\frac{M}{M+1},\qquad
b_M=\frac{M(M-1)}{(M+1)^2}.
$$
The following positive pointwise profiles bound the indicated
relative physical norms at any common strip $0\le\tau\le\tau_{\rm ref}$:
$$
\begin{array}{c|c}
\text{output}&\text{profile}\\ \hline
(P_e,\overline K_e)\text{ joint strong}
 &\rho\max(a_M\mathfrak a,\mathfrak d_n)\\
P_e\text{ weak}&(2/27)\rho\mathfrak a\\
\overline K_e\text{ weak}
 &\rho\max((4/27)\mathfrak a,\mathfrak d_n/3)\\
C_e\text{ weak}&\rho\mathfrak d_n/3\\
U_e\text{ weak}
 &\rho\max(b_M\mathfrak a,a_M\mathfrak d_n).
\end{array}
\tag{110.14}
$$
Here strong means weight $1+|m|$ and weak means no such extra
weight. More precisely, dividing each output coefficient by
its indicated profile gives the corresponding sum of
radial suprema at most one; for the joint strong row the
two component suprema are kept separate. At $\rho=0$ the
field is identically zero and no division is needed.

**Proof.** For a Q-input of frequency magnitude t, its
combined strong P and K contribution relative to its
canonical mass has coefficient
$$
\frac{t+t^2}{(1+t)^2}\mathfrak a
 =\frac{t}{1+t}\mathfrak a\le a_M\mathfrak a.
$$
The $\Xi$ contribution to that row is exactly $\mathfrak d_n$.
The two $Q$ component suprema share the same positive
factor $\mathfrak a$ divided by the profile, so their
coefficients can be added before this last bound.
The remaining coefficient maxima for $2\le t\le M$ are
$$
\frac{t}{(1+t)^3}\le\frac2{27},\quad
\frac{t^2}{(1+t)^3}\le\frac4{27},\quad
\frac1{1+t}\le\frac13,
$$
$$
\frac{t(t^2-1)}{(1+t)^3}
 =\frac{t(t-1)}{(1+t)^2}\le b_M,\qquad
\frac{t}{1+t}\le a_M.
\tag{110.15}
$$
Apply them to (110.3), then sum the fixed masses (110.13).
This establishes the radial-first statement; it is not
deduced by commuting a sum and a supremum. QED.

For $M=92$, $a_M=92/93$ and $b_M=8372/8649$.
For a nonmean linear centre supported through mode $40$,
$M=40$ may be used in its own profile. An error still
containing all $46$ low modes retains $M=92$.
These strict finite-window factors are not assigned to unbounded
frequencies: the limiting factors for the joint $Q$ term and the
two $U$ terms are $1$.

The [R82](R82-complete-low-cut-source-and-reference-strip.md)
balanced envelope is
$V/w=\overline X(a_n\mathfrak a+\overline{\mathfrak d}_n)$, with
$a_n\ge1$ and $\overline{\mathfrak d}_n\ge\mathfrak d_n$.
Consequently
$$
\overline X\max(a_M\mathfrak a,\mathfrak d_n)\le V/w.
\tag{110.16}
$$
Thus the new relative physical profile fits the old complete
mean small-root domain. This is a sharper source/mean
evaluation profile, not a free change of the Green
propagation norm. Any change of propagation norm would
still require its own radial and interface costs.

## 5. True auxiliary source about its signed linear field

Let $L$ be the exact nonmean linear head in the original homogeneous
linear far subspace, with the same
shallow low heights as the certified auxiliary solution
$C_{\rm aux}$. Let $e=C_{\rm aux}-L$, with its complete radius from
(110.13). Evaluating $\mathcal N_x(L)$ always completes the mean
by the same R33 root $c(L)$; it does not insert zero mean.

Write $\Pi_\perp$ for the contraction which removes only the zero
Fourier coefficient. It is applied after every product with the
complete pointwise inverse. The exact source decomposition is
$$
\mathcal N_x(C_{\rm aux})
=\mathcal N_x(L)
 +\Pi_\perp\big(D\mathscr Q[L]e+\mathscr Q(e)\big)
 +\{\mathcal R(L+e)-\mathcal R(L)\},
\tag{110.17}
$$
where $\mathcal R=\mathcal N_x-\Pi_\perp\mathscr Q$ is the complete
mean/inverse remainder of R106. On the right, the
quadratic terms are projected to the required nonzero
output after they are formed. The definition of
$\mathcal R$ retains every interaction of a quadratic
zero mode with the inverse.

If $R_L$ and $R_e$ are the actual strong relative physical
norm bounds in one fixed radial Wiener space and
$R_L+R_e\le1/64$, R106 gives
$$
\left\|\frac{\mathcal R(L+e)-\mathcal R(L)}
                  {c_{\rm bg}}\right\|_{0,*}
\le60\left(R_L^2R_e+R_LR_e^2+\frac13R_e^3\right).
\tag{110.18}
$$
Indeed, integrate its complete derivative bound
$60(R_L+tR_e)^2R_e$ over $0\le t\le1$. Also
$$
\|\mathscr Q(e)/c_{\rm bg}\|_{0,*}
 \le(23/18)R_e^2.
\tag{110.19}
$$
These estimates use complete complex mean roots along
the entire connecting segment. The input is the
certified auxiliary error, not a finite stored trajectory.

At a fixed radial point, the same formulas hold in
its angular Wiener space using local upper profiles.
Such a pointwise bound may be integrated for a chosen
output coefficient. It must not be relabelled a
sum-of-radial-suprema source bound without paying that
stronger quantifier. Alternatively use whole-cell
suprema of (110.14) in (110.18), or retain the fixed
modal masses as below.

For the main term $D\mathscr Q[L]e$, (110.11) gives
actual frequency-resolved canonical columns. For a signed output
$m\ne0$, let $H^Q_{m,b,n}$ and $H^\Xi_{m,b,n}$ be the integrals
of the absolute values of those columns times the absolute value
of the true output cut kernel and the respective weights
$$
\frac{e^{-\tau_{\rm ref}|b|}}{(1+|b|)^3},
\qquad
\frac{e^{-\tau_{\rm ref}|b|}}{1+|b|},
\tag{110.20}
$$
respectively, its one-mode cut error is bounded by
$$
\sum_n\rho_n\max_{b,\text{component}}H_{m,b,n}.
\tag{110.21}
$$
For the complete output Wiener norm with
$\omega_m=(1+|m|)e^{\sigma|m|}$, a valid stronger organization is
$$
\sum_n\rho_n
 \max_{b,\text{component}}\sum_{\substack{m\in2\mathbb Z\\0<|m|\le92}}
                  \omega_m H_{m,b,n}.
\tag{110.22}
$$
The unknown modal masses in (110.13) are fixed before
integration. Formula (110.22) sums output rows before
maximizing the input column. It does not assign an
entire independent $\rho_n$ to every output and then
claim that the total still costs just $\rho_n$.
Equivalently sum over positive outputs using the paired kernel
$H_{m,b,n}+H_{-m,b,n}$. Both Fourier halves are then accounted for
without an unrecorded factor of two.

The $\mathscr Q(e)$ term can likewise retain its two fixed
input modal masses and ordered quadratic columns,
or use the complete bound (110.19).
The remainder (110.18), the mean error in a signed
evaluation of $\mathcal N_x(L)$, and the far contribution below
must all still be paid.

## 6. Exact physical cut functional and cancellation of scales

Let $\Phi_m$ be the true homogeneous column normalized by
$\Phi_{Q,m}(b)=1$ at the actual node12 cut $b$. In the
ungauged canonical variables the source equation is
$$
(Q_m,\Xi_{n,m})_r^t
 =A_{n,m}(r)(Q_m,\Xi_{n,m})^t
    +(0,F_{\Xi,n,m})^t,
$$
and the complete relative source obeys
$$
F_{\Xi,n,m}
=\frac{r^4w^2}{\sqrt{12}\mu_n}\mathcal N_{r,m}.
\tag{110.23}
$$
To check the units, the physical-height second source is
$f_H=w\mathcal N_r$, and the canonical coefficient
for $f_H$ is $r^4w/(\sqrt{12}\mu_n)$.
For an outward source coordinate $x$,
$\mathcal N_x=r_x\mathcal N_r$ and $dr=r_x\,dx$.

The [R63](R63-actual-auxiliary-cut-momentum-functional.md)
Wronskian source functional, followed by the
actual cut conversion from Xi_12 to Kbar, therefore
simplifies exactly to
$$
\boxed{
\mathfrak F_m(f)
=\frac1{b^4w_b^2}
 \sum_{n=12}^{224}\int_{I_n}
       r(x)^4w(x)^2\,\Phi_{Q,m}(x) f_m(x)\,dx.}
\tag{110.24}
$$
Here $f=\mathcal N_x$ when evaluating the complete physical source.

**Proof.** In the continuous $(Q,\mu_n\Xi_n)$ coordinates
the true linear flow has zero trace. For a zero-shallow-Q
source response sharing the linear far stable subspace
with $\Phi$, differentiation of their determinant gives
$$
(e_S)_{\Xi_{12},m}(b)
=\sum_n\frac{\mu_n}{\mu_{12}}
        \int\Phi_{Q,m}(r)F_{\Xi,n,m}(r)\,dr.
$$
Its relative physical $\overline K$ at the cut is
$\sqrt{12}\mu_{12}/(b^4w_b^2)$ times that expression.
Substitute (110.23). The exact $\mu_n$, $\mu_{12}$ and $\sqrt{12}$
cancel. Finally $\mathcal N_r\,dr=\mathcal N_x\,dx$ gives (110.24). QED.

The orientation in this proof is outward $r$ and outward $x$.
Reversing an integration parameter changes its signed
Jacobian; it cannot be hidden behind an absolute R63
bound. Formula (110.24) has no second $r_x$ and no remaining
$\mu$ ratio. These cancellations do not authorize using the
wrong cell $\mu$ when reconstructing $C$ or $\Lambda$ in
(110.3)--(110.5). Gauge powers such as $(r/r_c)^{m^2-4}$
must also be undone once when reading a gauged column.

For the auxiliary solution the nonlinear far lift is separate:
$$
(\overline K_{\rm aux}-\overline K_{\rm lin})_m(b)
=\mathfrak F_m(\mathcal N_x(C_{\rm aux}))
       +(\mathcal B_{\rm cut}\mathcal D(z_{\rm aux}))_m.
\tag{110.25}
$$
Replacing its source using (110.17) does not eliminate
the second term. The auxiliary error e inside
(110.17) already includes the influence of the actual
far lift on the field; this is distinct from the
direct boundary contribution in (110.25).

If the exact full head Y is being compared with its
certified auxiliary centre, use the already-proved
[R83](R83-complete-head-difference-at-true-cut.md) or
[R100](R100-hybrid46-parameter-chart-and-source-transfer.md) source
difference and combine the direct
far boundary exactly:
$$
\begin{aligned}
\beta^{\rm true}_m={}&
 \mathfrak F_m(\mathcal N_x(L))
 +\mathfrak F_m(\mathcal N_x(C_{\rm aux})
                           -\mathcal N_x(L))\\
&+\mathfrak F_m(\mathcal N_x(Y)
                           -\mathcal N_x(C_{\rm aux}))
 +(\mathcal B_{\rm cut}\mathcal D(z_Y))_m.
\end{aligned}
\tag{110.26}
$$
Any additional prescribed low homogeneous height lift
is part of the linear DN subtracted in $\beta^{\rm true}$.
Its nonlinear effect remains in the actual difference
$Y-C_{\rm aux}$, as paid by the relevant certificate.
The auxiliary and full far terms are not both added
after this exact combination.

## 7. What a new signed computation must actually consume

The old R63/R82 files contain positive source caps.
Their names and values do not encode the sign of $\mathcal N_x(L)$.
A new evaluation must retain the following actual data:

1. The true signed homogeneous columns and the complete
   signed `Q_gain` used to normalize them, not only
   `abs(Q_gain)` or its positive lower bound.
2. The complete specified linear height vector, with
   all of its actual 20 modes and any explicitly
   included family lift. No higher reference mode is
   silently replaced by a generic m2 remainder.
3. True same-$g$ $r,w,\mu_n$ and the outward source
   coordinate on each source panel.
4. The full mean and pointwise inverse in (110.6),
   for example $c_2$ plus the complete R107 enclosure.
5. The actual canonical auxiliary error certificate,
   the complete full-head difference, and the direct
   true far contribution in (110.26).

A common projective amplitude should be retained while
forming the signed canonical linear forms. If a stored
interval column is represented as a signed common
scale times $(1,t)$ or $(t,1)$, form the needed linear
combination in that unit vector before multiplication
by its common scale. This avoids unnecessarily
splitting a shared amplitude into unrelated boxes.

A true signed whole-panel enclosure is still required.
One valid replay of the existing positive Peano--Baker
mechanism uses, for every prefix of a subpiece with
$A_{\rm int}\le A$, $B_{\rm int}\le B$, and $p=AB<1$,
$$
e=\frac{p^2}{4(1-p)},\quad o=\frac{p^2}{12(1-p)}
$$
and the entrywise enclosure
$$
T_{\rm prefix}\in
\begin{pmatrix}
[1-p-e,1+e]&[-A(p/2+o),A(1+o)]\\
[-B(1+o),B(p/2+o)]&[1-p-e,1+e]
\end{pmatrix}.
\tag{110.27}
$$
This is the original ordered series bound with prefix
integrals between zero and their complete positive
upper bounds. It preserves possible internal zeros;
it never divides by a field value that might vanish.
The full endpoint flow and projective advance remain
the original signed ones. Further subdivision or a
more accurate signed tube may be needed for a useful
numerical interval; that is an execution question,
not supplied by an absolute endpoint chart alone.

The R101 outer projected-solution spectrum is not an
input to this argument. In particular it cannot be
used as a spectrum of the inner auxiliary solution
or of its nonmean linear field.

## 8. Exact coefficient ledger and present scope

[closure_inner_canonical_correlation_constants.js](../computations/closure_inner_canonical_correlation_constants.js)
was actually evaluated in V8 with BigInt arithmetic.
Its ledger is
[2026-11-13-closure-inner-canonical-correlation-constants.json](../notes/2026-11-13-closure-inner-canonical-correlation-constants.json).

All fifteen gates passed. They include all 46 positive
modes, all 92 signed modes, all 8464 ordered signed pairs,
the complete quadratic and quadratic-Jacobian identities,
the exact canonical coefficient maxima, the 92
zero-output pairs, and the monomial cancellation of
both $\mu$ factors and $\sqrt{12}$ in (110.24).
These are universal algebraic checks. No floating
scientific field or new source integral was evaluated.

All proofs above are pointwise algebra or estimates on the fixed
radial modal masses. They do not assume that stored rounded states
solve the true real-source equation.

The result changes neither the true auxiliary solution
nor any existing certificate. It supplies signed
algebra and a complete error accounting interface for
a subsequent rigorous evaluation. The current numeric
T-head budget, the uncomputed signed centre functionals,
the remaining middle window, low/high feedback and the
full outer/cut closure are not claimed to have passed.
