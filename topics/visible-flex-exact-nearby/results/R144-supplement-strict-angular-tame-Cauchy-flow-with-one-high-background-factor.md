# R144 NT: strict angular tame Cauchy flow with one high background factor

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all12 saved-rational comparisons pass.** On the actual strict
negative interval, the full-tail nearby Cauchy flow of
[NR](R144-supplement-actual-negative-and-root-propagation-in-a-full-tail-neighbourhood.md)
has a genuine one-derivative estimate and an explicit arbitrary-integer
angular tame recurrence. Only the stated low $A^3$ background ball is
small. The higher background norm occurs linearly, once, and is not
placed in an exponential or required small.

For the true raw equation, full means and original jumps, the first
increment is

$$
 \begin{array}{c|c}
 \text{orientation}&\displaystyle\sup_r\|h(r)\|_{H^1_\phi\oplus_2H^1_\phi}\\ \hline
 \text{reverse}&340\,\mathfrak D_1+1120000\,\mathfrak D_0\\
 \text{forward}&12\,\mathfrak D_1+44500\,\mathfrak D_0 .
 \end{array}
 \tag{NT.1}
$$

The actual source and trace norms $\mathfrak D_j$ are defined below.
This is a Cauchy inverse on the strict interval, not yet an angular
increment for the positive high boundary inverse or for the root
fold map. No trace of a generic radial $L^2$ head is inferred.

## NT1. Background, data and the actual differential

Use the same selected intrinsic metric as NR and the same domain

$$
 Q=\widetilde Q_\delta+e,\qquad
 |\delta|\le10^{-10},\qquad
 \sup_{[0,r_c]}\|e\|_{A^3,\oplus_1}\le10^{-6},
 \quad r_c={2333968743003\over10^{13}}<.234 .
 \tag{NT.2}
$$

The unknown $e$ may have infinitely many angular modes. For an
integer $n\ge1$ assume additionally that $\sup_r\|Q(r)\|_{A^{n+1}}$
is finite, without a smallness condition. The complete Cauchy problem is

$$
 h_r=A_Qh+f,\qquad h(r_i^+)-h(r_i^-)=j_i,
 \tag{NT.3}
$$

with its actual supplied datum at the chosen endpoint. In reverse
orientation the signs of the differential and impulses are changed
in the exact usual equation; the estimates use their full norms.
Write

$$
 \mathfrak D_j=
 \|h(r_{\rm in})\|_{H^j}
       +\int_{\rm actual\ interval}\|f(r)\|_{H^j}\,dr
       +\sum_i\|j_i\|_{H^j}.
 \tag{NT.4}
$$

All pair Sobolev norms in this note are Euclidean sums, with normalized
fourfold circle measure and physical frequencies $4\mathbb Z$.
For an ordinary $L^2_rH^j$ source the integral in (NT.4) is at most
the square root of its true support length times that norm.
Impulses have no radial length factor. Original coefficient jumps
are not extra state impulses.

The complete physical differential is

$$
 \begin{gathered}
 A_Qh=(dI_2+\gamma mJ)h_\phi+L_0h
       -2\beta Q_\phi I(Q^tDh)+\gamma\langle h_2\rangle JQ_\phi,\\
 d=-\beta I(Q^tDQ),\quad m=\langle Q_2\rangle,\quad
 D=\operatorname{diag}(1,K),\quad
 J=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\\
 L_0=\begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix},\qquad I=\partial_\phi^{-1}P_\perp .
 \end{gathered}
 \tag{NT.5}
$$

Every primitive has only its exact zero intermediate mode removed.
The equation is valid at the actual unsolved background; no nonlinear
equation for $m$ is used.

## NT2. Exact differentiated equation and the mean paths

Put $\partial=\partial_\phi$. For every smooth full direction,

$$
 \begin{aligned}
 [\partial,A_Q]h={}&d_\phi h_\phi+(L_0)_\phi h\\
 &-2\beta Q_{\phi\phi}I(Q^tDh)
       -2\beta Q_\phi I(Q_\phi^tDh)
       +\gamma\langle h_2\rangle JQ_{\phi\phi}.
 \end{aligned}
 \tag{NT.6}
$$

The angularly constant principal $\gamma mJ\partial$ commutes
exactly. The last term is the actual mean-input rank. It does
not vanish merely because $\partial h$ has zero mean.

More generally, for $n\ge1$ and $w_n=\partial^nh$,

$$
 (w_n)_r=(A_Q+n d_\phi I_2)w_n+\partial^nf+\mathcal R_n(Q,h),
 \qquad [w_n]_i=\partial^nj_i ,
 \tag{NT.7}
$$

where the complete lower remainder is

$$
 \begin{aligned}
 \mathcal R_n={}&
 \sum_{a=2}^n{n\choose a}d^{(a)}
                                  \partial^{\,n-a+1}h\\
 &+\sum_{a=1}^n{n\choose a}L_0^{(a)}
                                  \partial^{\,n-a}h\\
 &-2\beta
 \sum_{\substack{a+b+c=n\\a+b\ge1}}
 {n!\over a!b!c!}\,
 Q^{(a+1)}I((Q^{(b)})^tD\partial^ch)
       +\gamma\langle h_2\rangle JQ^{(n+1)} .
 \end{aligned}
 \tag{NT.8}
$$

Here $Q^{(a)}=\partial^aQ$, including $Q^{(0)}=Q$.
For $n=1$ the first sum is empty, and (NT.8) is exactly
(NT.6) without $d_\phi h_\phi$.
The primitive remains in its original order even when the
intermediate frequency is low.

The auxiliary derivative has $\Pi w_n=0$ identically.
This is an angular-derivative identity, not a restriction
that $\Pi h=0$. In particular the final term of (NT.8)
retains the original mean of $h$.
When deriving estimates one projects the auxiliary equation
to its nonmean subspace; its exact zero-mean compatibility
comes from differentiating (NT.3). The mean of
$\mathcal R_n$ is not separately discarded before that identity.
The original solution $h$ and its source retain the full
characteristic mean vector throughout.

## NT3. The highest derivative has a low-norm growth bound

Let $\kappa=\sqrt{-K}$ and use
$W_h=\operatorname{diag}(1,\kappa)h$.
The characteristic change is orthogonal after this weighting.
The complete low scalar conclusions are

$$
 .5338<\kappa<1.03,\quad b=|\beta|<2,\quad g=\gamma<7,
 \quad R<1.912002,\quad L<3.704003,\quad
                         \|d_\phi\|_\infty<.423 .
 \tag{NT.9}
$$

The last inequality is a new saved-scalar combination:
the original complete SP maximum is
$.4226268039375846785\ldots$; the entire NR difference
adds at most
$4\{2(1.912)\epsilon_R+\epsilon_R^2\}$, with
$\epsilon_R=5\,10^{-7}+1.03\,10^{-6}$.
No old angular coefficient is reevaluated.

The nonmean energy of $A_Q$ has rate at most
$b_*+c_\pm+bRL/2$, by NR2. Adding $n d_\phi$ costs
$n\|d_\phi\|_\infty$.
The actual SP comparison entry

$$
 \mathcal A_{11}
   =\max(0,b_*+D+(A_1+N_y)/4)
 \tag{NT.10}
$$

already dominates $b_*+D+bRL/2$. Therefore the auxiliary
nonmean flow in (NT.7) has energy kernel bounded by
the same actual scalar $11$ comparison kernel, times

$$
 \exp((n-1)(.423)(.234))
                  \le g_n:=(10/9)^{\,n-1}.
 \tag{NT.11}
$$

The inequality uses $.423(.234)<1/10$ and
$e^{1/10}<10/9$. Thus the highest derivative never
puts a high background norm in its exponential.
For $n=1$ there is no extra growth factor at all.

Convenient complete weak auxiliary and strong low-state
constants from NR are

$$
 \begin{array}{c|ccc}
 &U_1&U_0&k_1\\ \hline
 \text{reverse}&174&176&2.166\\
 \text{forward}&5.869&6&2.517 .
 \end{array}
 \tag{NT.12}
$$

Here $U_1$ bounds the full auxiliary comparison,
$U_0$ the full low $L^2$ flow, and $k_1$ the nonradial
auxiliary comparison. The latter is the NR weak
nonradial bound divided by its genuine new denominator.
All are uniform for every source insertion and subinterval.

## NT4. A complete single-high-background commutator estimate

For this section let
$x=(u,\kappa v)$, with the Euclidean-pair Wiener norm, and define

$$
 X_0=\sup_r\|x\|_{A^0}<6.6,\quad
 X_1=\sup_r\|x_\phi\|_{A^0}<5.602,\quad
 X_2=\sup_r\|x_{\phi\phi}\|_{A^0}<717,\quad
 B_{n+1}=\sup_r\|x\|_{A^{n+1}} .
 \tag{NT.13}
$$

The first three depend only on the low domain (NT.2).
For the centre alone one uses its degree32 and its already
proved first angular bound5.438; the unknown's first and
second derivatives each cost its actual $A^3$ norm.
Thus $X_2<1.03(128(5.438)+10^{-6})<717$.
No finite support is assigned to the unknown.

For $n\ge1$ define explicit positive constants

$$
 \begin{aligned}
 L_n&=2^n\,8bX_0X_1
                +{b\over2}\,3^n(X_0X_2+X_1^2),\\
 H_n&={17b\over4}\,4^nX_0
                +{b\over4}\,6^n(X_0+X_1)+g ,
 \qquad b=2,\quad g=7 .
 \end{aligned}
 \tag{NT.14}
$$

Then the complete remainder has the tame estimate

$$
 \|\operatorname{diag}(1,\kappa)\mathcal R_n(Q,h)\|_2
 \le L_n\|\partial^{n-1}W_h\|_2
                         +H_nB_{n+1}\|W_h\|_2 .
 \tag{NT.15}
$$

Here is a direct Fourier proof, including all intermediate
primitive frequencies. For the drift remainder, let
$\ell$ be the coefficient frequency and $k$ the input
frequency. Split only the inequality into
$|\ell|\le|k|$ and $|\ell|>|k|$.
For every $2\le a\le n$,

$$
 |\ell|^a|k|^{n-a+1}
       \le|\ell|^2|k|^{n-1}+|\ell|^{n+1}.
 \tag{NT.16}
$$

The sum of binomial coefficients is at most $2^n$.
Moreover
$\|d_{\phi\phi}\|_{A^0}\le2bX_0X_1$ and,
on nonzero fourfold modes,

$$
 \|d\|_{A^{n+1}}
 \le{5b\over4}\|x^t\operatorname{diag}(1,-1)x\|_{A^n}
 \le{5b\over4}\,2^nX_0B_{n+1}.
 \tag{NT.17}
$$

The factor $5/4$ is $(1+|k|)/|k|\le5/4$, not a
finite-input cutoff. The exact zero primitive mode is
excluded. For the local reaction commutator the analogous
split gives
$|\ell|^a|k|^{n-a}\le|\ell||k|^{n-1}+|\ell|^n$.
The actual quadratic matrix obeys
$\|(L_0)_\phi\|_{A^0}\le6bX_0X_1$ and its
nonconstant-in-$Q$ part has $A^n$ norm at most
$3b\,2^nX_0B_{n+1}$ in the weighted coordinates.
Its angularly constant linear matrix contributes nothing
to the commutator.
These are the first terms of $L_n,H_n$ in (NT.14).

For the ordered primitive let its two coefficient
frequencies be $\ell_1,\ell_2$ and put
$\ell=|\ell_1|+|\ell_2|$ in this estimate only.
For $a+b\ge1$ and $a+b+c=n$,

$$
 |\ell_1|^{a+1}|\ell_2|^b|k|^c
 \le|\ell_1|\ell|k|^{n-1}+|\ell_1|\ell^n .
 \tag{NT.18}
$$

The multinomial sum is at most $3^n$.
The first coefficient sum costs $X_2X_0+X_1^2$.
The second costs at most
$2^{n-1}(X_0+X_1)B_{n+1}$.
Use the actual bound $\|I\|\le1/4$ at every
nonzero intermediate frequency. This gives exactly
the primitive terms in (NT.14), since the original
prefactor is $2b$.
The final complete mean rank costs
$g B_{n+1}\|W_h\|_2$, proving (NT.15).
Every estimate is an ordinary $\ell^1$--$\ell^2$
convolution bound; no unknown Fourier tail has been
truncated.

Only one factor in each high term is $B_{n+1}$.
In particular (NT.15) contains no product of two
uncontrolled high background norms.

## NT5. Actual first increment with explicit constants

For $n=1$, the exact remainder (NT.6) gives a much
smaller pointwise bound than the general constants.
Using the weighted pointwise state, first derivative
and second derivative bounds,

$$
 \|\operatorname{diag}(1,\kappa)\mathcal R_1(Q,h)\|_2
 \le C_1\|W_h\|_2,\qquad
 C_1=6bRL+{b\over2}(RX_2+L^2)+gX_2<6500 .
 \tag{NT.19}
$$

The actual rational upper value is below
$6488.127477$.
The local derivative gives $6bRL$; the two ordered
primitive words give the two terms in the middle;
the last term is the full original mean-input rank.

A useful gain avoids paying the same radial scalar
factor twice. In a double Duhamel expression the
auxiliary kernel from $r$ to $\tau$ and the low-state
kernel from $\tau$ to $s$ have the same scalar
$c_\pm$. Their exponents add over disjoint intervals.
The full saved scalar budget therefore occurs once.
The nonradial factors are bounded by $k_1$ and by
the nonradial part already included in $U_0$.
Consequently the mixed two-kernel norm is at most
$k_1U_0$, for every ordered source insertion.

Writing $\mathfrak D_j$ for (NT.4), the actual complete
energy bound for the first derivative and the value is

$$
 \sup_r\|h(r)\|_{H^1}
 \le {1.03\over.5338}
       \{U_1\mathfrak D_1+
             [U_0+6500(.234)k_1U_0]\mathfrak D_0\}.
 \tag{NT.20}
$$

The factor $1.03/.5338$ is the full raw input/output
conversion; $H^1$ is bounded by the value plus first
derivative norm. Formula (NT.20) includes original
impulses by the same ordered mixed-kernel argument.
The exact rational comparisons give respectively

$$
 \begin{array}{c|rr}
 &\mathfrak D_1\text{ coefficient}&\mathfrak D_0\text{ coefficient}\\ \hline
 \text{reverse}&<335.743725&<1119156.429525\\
 \text{forward}&<11.324598&<44333.882091 .
 \end{array}
 \tag{NT.21}
$$

This proves (NT.1). All constants concern this same
full-tail nearby background and same physical
operator. A first-order coefficient change was
never inserted as a bounded ordinary $L^2$ source.

## NT6. Explicit arbitrary-integer tame recurrence

For completeness the general estimate can be given
without optimizing its constants. Define the derivative-sum
data norm $\mathfrak E_n$ by replacing each $H^n$ norm
in (NT.4) with
$\sum_{j=0}^n\|\partial^j\operatorname{diag}(1,\kappa)\,\cdot\|_2$,
using the actual radial $\kappa$ at each source or impulse.
Let

$$
 S_n=\sum_{j=0}^n\sup_r\|\partial^jW_h(r)\|_2,\quad
 C_0=U_0,\quad \ell=.234,\quad g_n=(10/9)^{n-1},
 \tag{NT.22}
$$

and recursively set

$$
 C_n=(1+U_1g_n\ell L_n)C_{n-1}
                         +U_1g_n(1+\ell H_nU_0).
 \tag{NT.23}
$$

Use the upper constants in (NT.12)--(NT.14), so every
$C_n$ is an explicit positive rational number depending
only on $n$ and the fixed low background domain.
The full high norm $B_{n+1}$ is absent from (NT.23).

The actual auxiliary Cauchy estimate (NT.11),(NT.15)
gives

$$
 S_n\le
 (1+U_1g_n\ell L_n)S_{n-1}
       +U_1g_n\mathfrak E_n
       +U_1g_n\ell H_nB_{n+1}U_0\mathfrak E_0 .
 \tag{NT.24}
$$

Starting with $S_0\le U_0\mathfrak E_0$ and using
$B_n\le B_{n+1}$ proves

$$
 S_n\le C_n\{\mathfrak E_n+
                              (1+B_{n+1})\mathfrak E_0\}.
 \tag{NT.25}
$$

The high norm is carried through the induction linearly:
the term with $S_{n-1}$ is multiplied only by the fixed
low constant $L_n$.
Converting derivative sums to ordinary Bessel Sobolev
norms gives the convenient explicit version

$$
 \boxed{\quad
 \sup_r\|h(r)\|_{H^n}
 \le 2^{n+1}(n+1)C_n
       \{\mathfrak D_n+(1+B_{n+1})\mathfrak D_0\},
 \qquad n\ge1 .
 \quad}
 \tag{NT.26}
$$

Indeed $1.03/.5338<2$,
$\|W_h\|_{H^n}\le2^{n/2}S_n$, and
$\mathfrak E_n\le1.03(n+1)\mathfrak D_n$.
The larger displayed integer factor covers all these
conversions. It is not multiplied into the high
background norm at each derivative step.

Smooth full Fourier data first give the identities.
Finite Fourier approximation of the coefficients and
data preserves the uniform low margins and the stated
higher norms. The estimates, the original characteristic
existence construction and uniqueness of the NR low flow
then give the same actual $H^n$ Cauchy solution.
The proof takes no radial derivative of an unknown
background, a radial enclosure or an approximate mean.

The input in (NT.4) is an actual prescribed endpoint
datum or the trace of an already propagated Cauchy
solution. A merely radial $L^2$ low193 head has no
fixed-cut trace by this theorem. When a source is
formed from such a head, its actual ordinary source
norm must first be supplied, and its resulting trace
is then read through the Cauchy map. The original
physical means, phase, height, point inputs and
normalizer charges remain separate ports.

The next root and positive-high angular increments
must retain their own anisotropic root source units
and complete physical outer trace regularity.
Equation (NT.26) supplies the strict tame part without
requiring all high background norms small; it does
not grant those remaining increments for free.
