# R144 GGB: actual principal-gauge budget with the full phase constant

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** The completed PCT and PSC tame estimates admit a low
budget based only on the nonconstant displacement of the gauge.
This is a norm refinement, not a phase normalization.
The actual original principal gauge has this budget below6406.
Its declared H3-radius-one neighbourhood has budget below6410,
so one can use the explicit common value $L=8192$.

The complete phase constant, phase residual and constant direction
remain in every map and derivative. This supplies an actual
nonempty gauge domain for PCT/PSC and its intersection with CP.
It does not infer H3 control from a C1 neighbourhood.

## GGB1. Same original selected conjugacy

Use the exact selected pair $(\delta_*,\mathcal H)$ of
[AC](R133-supplement-actual-conjugacy-density-transfer-for-complete-first-coefficient.md),
not a fitted rotation or a nearby unknown conjugacy.
The completed whole bounds AC.2/AC.9, also recorded in
[ZD.15--16](R133-supplement-strong-sign-density-conjugation-and-global-Cayley-return.md),
are
$$
 31/32\le\mathcal H'\le33/32,\qquad
 \|\mathcal H''\|_\infty\le4,\qquad
 \|\mathcal H'''\|_\infty\le1024.                         \tag{GGB.1}
$$
Both signs and the complete true analytic tail are included.
No KAM calculation or old derivative target is repeated.

Let $g_0=\mathcal H^{-1}$ with its same original degree-one
lift and phase constant, and write $u_0=g_0-\operatorname{Id}$.
The already stated inverse derivative formulas give, with $r=32/31$,
$$
 \begin{split}
 32/33&\le g_0'\le32/31,\\
 \|u_0'\|_\infty&\le1/31,\\
 \|u_0''\|_\infty&\le4r^3<9/2,\\
 \|u_0'''\|_\infty&\le48r^5+1024r^4<1280.
 \end{split}                                                \tag{GGB.2}
$$
The numerical comparisons after those complete formulas are new
exact rational combinations of completed bounds.

Parseval in the original normalized period-pi/2 circle gives
$$
 \|u_0'\|_{H^2}^2
 =\|u_0'\|_2^2+2\|u_0''\|_2^2+\|u_0'''\|_2^2
 \le(1/31)^2+2(9/2)^2+1280^2<1281^2.                    \tag{GGB.3}
$$
No bound on the lift's additive constant was used in this
derivative norm.

## GGB2. Actual complete Wiener budget

For a periodic u define
$$
 u^\circ=u-\langle u\rangle,\qquad
             G_s^\circ=1+\|u^\circ\|_{A^s}.              \tag{GGB.4}
$$
The original signed frequencies are $4\mathbb Z$.
For every nonzero such frequency k,
$$
 \frac{(1+|k|)^2}{|k|}
 \le\frac54(1+|k|).
$$
The complete Fourier embedding $A^1\le4H^2$ therefore gives
$$
 \|u^\circ\|_{A^2}
 \le\frac54\|u'\|_{A^1}\le5\|u'\|_{H^2}.                \tag{GGB.5}
$$
This uses $u^\circ=Iu'$ as an exact identity of norms,
while the actual map still uses the unchanged u.
The coefficient 4 in the embedding follows from
$(1+|k|)^2\le2(1+k^2)$ and the completed $A^0\le2H^1$.

Applying (GGB.3) gives the actual selected-centre budget
$$
                1+\|u_0^\circ\|_{A^2}<1+5(1281)=6406.
                                                               \tag{GGB.6}
$$
It controls the whole true function, not its finite Fourier
model.

For any real periodic perturbation z with $\|z\|_{H^3}\le1$,
put $g=g_0+z$ and $u=g-\operatorname{Id}$.
Projection away from the mean is a contraction on A2,
and the complete embedding $A^2\le4H^3$ gives
$$
 G_2^\circ\le6406+4\|z\|_{H^3}\le6410<8192.              \tag{GGB.7}
$$
The original constant in $g_0$ and the full constant in z
remain in g. The bound on z here includes its constant
coefficient; no phase condition has been imposed.

## GGB3. Refinement of PCT without deleting the phase equation

All
[PCT](R144-supplement-all-angular-moving-phase-and-current-normalized-row.md)
estimates remain valid with
$$
 G_s\ \hbox{replaced by }G_s^\circ,\quad
 G_2^\circ\le L,\quad
 Z_n^\circ=B_{n+2}+G_{n+1}^\circ.                         \tag{GGB.8}
$$
Their explicit cn, dn, Tn and Cn are unchanged functions
of the declared L.

Here is the full reason for that refinement.
Every derivative of g of positive order is unchanged by
subtracting the constant from u.
In particular
$$
 \|g'\|_{A^{n-1}}\le1+\|u^\circ\|_{A^n}=G_n^\circ
 \quad(n\ge1).
$$
The real composition proof PCT.5--7 uses only this bound,
the actual derivative of g, and real change of variables.
It makes no assumption on the actual additive phase.
The same is true of the reciprocal proof for
$j=g'\circ R$ and its powers.

In the raw value formula, the only uncomposed u term is
$u-u\circ R=u^\circ-u^\circ\circ R$.
Its constant cancels in that exact difference.
The other part $(P-\operatorname{Id})\circ g-\Omega_\star$
is still evaluated at the actual full g and can have a
nonzero mean. Thus the value estimate has not projected
the phase residual to its nonconstant part.

All first and second derivative formulas PCT.13, and all
seven terms in PCT.19, use those same actual compositions
and derivative/reciprocal factors.
Their direction norms still include the entire directions,
including constant ones. Thus their same full product
argument proves (GGB.8) without a new low-smallness gate.

For example a constant additive direction $\xi=c$ has
$$
 D_gE[c]=c(P'\circ g-1),
$$
which is generally nonzero. A constant abstract PD direction
$\alpha=c$, whose actual direction is $g'c$, instead gives
$$
 \mathscr L(0,c)=cE'/j .
$$
That whole current-residual term is retained too.
These identities illustrate that a norm independent of
an arbitrary lift constant does not erase its direction
from the actual equation.

## GGB4. The complete physical secant has the same refinement

The estimates in
[PSC](R144-supplement-complete-physical-phase-secant-and-tame-Hessian.md)
also hold with the replacement (GGB.8), and
$$
 \widehat Z_n^\circ
       =B_{n+2}+G_{n+1}^\circ+W_{n+1}.                  \tag{GGB.9}
$$
Keep every waist trace and mean exactly as there.

The low derivative budget $L_A$ in PSC.17 already uses
only $g'$ and the true $P'\circ g$.
For the high real-composition proof at $A=P\circ g$ and
$B=g\circ R$, use
$$
 \|A'\|_{A^{n-1}}
       \le1+\|(A-\operatorname{Id})^\circ\|_{A^n}.
$$
The nonconstant part of $A-\operatorname{Id}$ is
$$
 u^\circ+
 \big((P-\operatorname{Id})\circ g
               -\langle(P-\operatorname{Id})\circ g\rangle\big).
$$
Projection is a contraction in the complete Fourier norm.
The same PCT composition bound pays the second term with
one high background and the actual evaluation at g.
For B the nonconstant displacement is simply
$u^\circ\circ R$.
Thus PSC.19 and its full composition proof use
$G_{n+1}^\circ$ with the same constants.

The physical map itself remains exactly
$\Theta(A)-\Theta(B)$.
All nine Hessian terms, the full secant, the actual waist
mean and the independent trace directions are unchanged.
Its low derivative bound23 and mixed Hessian bound3000
remain the previously completed ones.

## GGB5. Explicit intersection with the actual positive pivot domain

Use the same actual $g_0$ as
[CP](R147-supplement-uniform-positive-phase-pivot-near-the-mean-exact-centre.md).
In addition to CP's complete Q/nu conditions, require
$$
 \|g-g_0\|_\infty\le10^{-8},\qquad
 \|g'-g_0'\|_\infty\le10^{-8},\qquad
                        \|g-g_0\|_{H^3}\le1.             \tag{GGB.10}
$$
This is an explicit nonempty intersection: the actual g0
is included. The last inequality is an independent strong
budget, not a consequence of the first two.
The complete constants in (GGB.2) give
$$
 1/2<32/33-10^{-8}\le g'
       \le32/31+10^{-8}<2.
$$
Hence this actual gauge domain satisfies the refined
PCT/PSC hypotheses with the concrete choice
$$
                               L=8192.                  \tag{GGB.11}
$$
The candidate scalar $1/60<S<3/50$ of CP continues to
hold on this intersection, with all its regular candidate
defects retained. Its positivity still does not turn
that candidate into a full regular response.

For Taylor remainders and operator differences, the whole
line segment must satisfy the stated domains.
The constraints in (GGB.10) are convex in the additive
gauge coordinate, and all phase constants are retained.
Preserving them in an actual iteration still requires its
real increment estimates.

This result supplies a concrete low gauge budget for the
completed all-angular phase interfaces.
It supplies no missing finite matrix, no full parameter
Schur inverse and no nonlinear fixed-metric family.
The original true conjugacy is used only as the actual
centre, not declared to conjugate an unconstructed exact
nearby PDE solution.

The companion reader performs only the new rational
combinations in (GGB.2)--7 and the actual orientation
comparisons. It recomputes no old conjugacy, angle norm,
phase transport or scientific target.

