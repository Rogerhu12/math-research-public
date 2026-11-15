# R133 supplement: finite angular jets for the true long DN and Poisson ports

2026-11-15, visible-exact-astra-0df9.

**A complete finite-regularity outer estimate.** The true nonlinear long graph
and its full curvature feedback can be used without an analytic unknown
background. This note proves that assertion on an explicit finite-jet
domain, with every Fourier mode, the holonomy slope, both curvature means,
and the original physical source units retained. The argument uses
holomorphy in finitely many Banach-valued parameters. It never evaluates
an unknown finite-Sobolev function at a complex angle.

The complete physical equations and constants are
[N.3--N.25](R119-supplement-actual-long-screening-complete-Sobolev-DN-and-cap-facing-port.md),
abbreviated N. The original nonlinear weighted Green proof is
[S.1--S.34](R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md).
The real coordinate interface is
[D.1--D.17](R133-supplement-real-angle-full-weak-DN-and-good-density.md).
The good tangent and all physical curvature means are
[U.1--U.25](R133-supplement-exact-unknown-outer-angle-good-tangent-and-full-means.md).

All statements first use the actual physical angle at B and R. The
intrinsic parameters and the true finite length L are fixed. Their
independent derivatives remain separate source columns.

## 1. Zero-width algebra and the actual finite-jet domain

Let A_0 be the complete Wiener algebra on 4Z, with norm
$\sum_{m\in4\mathbb Z}|f_m|$. Nonmean dot A^k norms are
$\sum_{m\ne0}|m|^k|f_m|$. The mean slope output has the sum norm
$\dot A^1_0\oplus\mathbb C$. All signed modes are present.

Put
$$
 Q_*=8192,\qquad z_*=2^{-36},\qquad
 \epsilon=e^{-7L/4}<2^{-33554432},\qquad s_B=a_Bw_B .
 \tag{J.1}
$$
The true cap curvature input is
$Z=(C_R-C_r)_\perp$, and the left nonmean height is $f=f_B$.
Assume they are real and have the finite translation jets
$$
 \|\partial_\theta^qZ\|_{A_0}\le q!128^q z_*,
 \qquad
 \|\partial_\theta^qf\|_{\dot A^2_0}\le q!128^q F,
 \quad 0\le q\le Q_*,\quad 0\le F\le2^{-62}.
 \tag{J.2}
$$
These are finitely many inequalities. No claim is made about derivatives
above 8192 or about an analytic strip.

The original complete Fourier-algebra proof of N.6 is valid at width
zero. Indeed convolution has the same norm-one product estimate;
the mean and nonmean projections, the zero-mean primitive, all diagonal
Dirichlet Green multipliers and the radial weighted modules in S use
the same absolute coefficient estimates. Deleting the exponential
angular weight introduces no new factor in any of those inequalities.
The holonomy small root and the actual C_R inverse use precisely those
operations. Thus one repeats the same contraction proof in A_0:
$$
 f_*=\Phi_R(Z,f),\quad
 \|\Phi_R\|_{\dot A^2_0}\le r_f=10^{-8},\quad
 \|D_f\Phi_R\|<2^{35},\quad
 \|D_Z\Phi_R:A_0\to\dot A^2_0\|<10 .
 \tag{J.3}
$$
The larger original complex parameter domain remains
$\|Z\|_{A_0}\le z_a=3.3\,10^{-10}$ and
$\|f\|_{\dot A^2_0}\le r_B=2^{-60}$, with the same ball-image
and contraction inequalities
$$
 9z_a+2^{-512}r_B+9\,2^{12}(r_f+r_B)^2<r_f,\qquad
 36\,2^{12}(r_f+r_B)<1/512 .
$$
This is a new instantiation of the complete proof, not an assertion
that an arbitrary finite-Sobolev input already belonged to its positive
analytic-width domain.

The long solution, the holonomy slope and Phi_R are holomorphic in these
complex Banach parameters, by the uniformly contracting holomorphic
iterations. Their actual curvature means and the one constant-height
gauge are retained. Real translations commute with all the physical
equations and their normalizations, so uniqueness gives real translation
covariance of the complete solution and its derivatives.

At width zero N.7--N.11 consequently give the same complete slope error
$$
 T_{Z,f}=D_f\mathscr K_Z(f)+\mathsf C_L,\qquad
 \|T_{Z,f}:\dot A^2_0\to\dot A^1_0\oplus\mathbb C\|
 <2^{25}\|f\|_{\dot A^2_0}+2^{41}\epsilon ,
 \tag{J.4}
$$
where $\mathsf C_L=|D_\theta|\coth(L|D_\theta|)P_\perp$.
In particular the true term
$D_{f_*}\mathcal K_B\,D_f\Phi_R$ is still present.
The case F=0 uses the quadratic zero of N.7; there is no zero-radius
Cauchy estimate.

## 2. Finite polynomial parameter curves and real commutators

For complex a define the finite, Banach-valued polynomials
$$
 Z^{[Q_*]}(a)=\sum_{q=0}^{Q_*}{a^q\over q!}\partial_\theta^qZ,
 \qquad
 f^{[Q_*]}(a)=\sum_{q=0}^{Q_*}{a^q\over q!}\partial_\theta^qf .
 \tag{J.5}
$$
For $|a|\le1/512$ their norms are at most $(4/3)z_*$ and
$(4/3)F$, respectively. They lie strictly in the original domain
of (J.3), with f in its half ball. Thus the operator-valued
holomorphic function obtained from (J.4) satisfies
$$
 \|T_{Z^{[Q_*]}(a),f^{[Q_*]}(a)}\|
                   <2^{43}(F+\epsilon).
 \tag{J.6}
$$

Here is the finite-jet identification used below. For any real
translation a, the true real curve is
$(C_aZ,C_af)$, $C_a=e^{a\partial_\theta}$.
Through order Q_* at a=0 it has exactly the same Banach derivatives
as (J.5). The finite chain rule for the holomorphic solution and operator
maps therefore gives identical derivatives through that order.
Real covariance identifies those derivatives, on finite Fourier vectors,
with the commutators of the actual operator:
$$
 \|\operatorname{ad}_{\partial_\theta}^{\,q}T_{Z,f}\|
 _{\dot A^2_0\to\dot A^1_0\oplus\mathbb C}
 \le q!512^q\,2^{43}(F+\epsilon),\qquad q\le Q_* .
 \tag{J.7}
$$
Coefficient maps have the same finite-jet identification with their
ordinary angular derivatives. This argument is valid even if the
unknown functions have no nonzero analytic width. The polynomials in
(J.5) are auxiliary parameter curves; they are not declared equal to
complex-angle translates of those functions.

The same proof yields all finite angular jets of the actual solution
in its original long strong space and of Phi_R in dot A^2_0.
For example the latter are bounded by $q!512^q r_f$.
No radial bootstrap or new radial regularity of an arbitrary source
is inferred from this angular statement.

## 3. The complete Sobolev matrix, including output mean

For $n\ne0$, $m\in4\mathbb Z$, let $a_m=\max(1,|m|)$.
The q=0 and q=4 estimates in (J.7) imply
$$
 |(T_{Z,f})_{mn}|
 \le B\,{|n|^2\over a_m}(1+|m-n|)^{-4},
 \qquad B<2^{88}(F+\epsilon).
 \tag{J.8}
$$
Indeed one first takes the smaller of the bounds with factors
$1$ and $|m-n|^{-4}$, and then uses
$(1+|k|)^4\le16\max(1,|k|^4)$.
The inequality $4!512^4\,2^{43}<2^{84}$ pays the displayed constant.

The actual $H^{1/2}\to H^{-1/2}$ weighted matrix entry is at most
$$
             2B(1+|m-n|)^{-5/2}.                         \tag{J.9}
$$
This follows from $|n|\le a_m(1+|m-n|)$.
Both full signed row and column sums of this lag kernel are less
than 4, even if the sum is enlarged from 4Z to Z.
The Schur estimate therefore gives
$$
 \|T_{Z,f}:H^{1/2}_\perp\to H^{-1/2}\|
                         <2^{96}(F+\epsilon).
 \tag{J.10}
$$
The row m=0 was included throughout. The column n=0 is exactly zero
only because the input of this slope map is nonmean height.

For a higher commutator one applies the same argument to the q and
q+4 bounds in (J.7). For $q\le2176$ these use at most 2180
translation jets. The simple integer bound
$2180!<2^{12\cdot2180}$ shows that
$$
 (2180)!512^{2180}\,2^{43}<2^{45823}.
$$
Thus the complete finite-lag proof has ample room inside a
$2^{65536}(F+\epsilon)$ bound. No finite-window count, principal
symbol replacement or assumption of analytic Fourier decay occurs.

## 4. Actual coefficients and the physical DN

At B let
$$
 \mu=\mu_0JD^{-3/2},\quad d=E(V-P)/J,\quad
 \mu_0=(4\omega)^{-1}\in(1/6,1/4),\quad E=1+w_B^2 .
$$
The width-zero versions of N.19--N.20 apply to every curve in (J.5).
They imply, for either coefficient
$c=\mu/\mu_0-1$ or $c=d$,
$$
 \|\partial_\theta^q c\|_{A_0}
       \le q!512^q\,2^{18}(F+\epsilon),\qquad q\le Q_* .
 \tag{J.11}
$$
The complex curve is used only for its A_0 coefficient bound.
One does not assign an unproved A^1 norm to the last synthetic jet.

At the actual real background the standard full convolution bound is
$$
 \|M_c:H^{\pm1/2}\to H^{\pm1/2}\|
       \le2\{\|c\|_{A_0}+\|\partial_\theta c\|_{A_0}\}.
 \tag{J.12}
$$
It follows directly by inserting the Sobolev weights in the full
multiplication matrix. Hence (J.11) with q=0,1 pays these real
multipliers; in particular the actual multiplier M_mu has norm below 2.
For a commutator of order q, (J.12) uses coefficient jets only through
q+1. There is still a large finite buffer.

The exact physical height normalization and total conormal are
$$
 \delta f_B=P_\perp g/s_B,\qquad
 \mathcal N_{B,Z}g
 =-\mu\{D_f\mathscr K_Z(f)P_\perp g-d\,\partial_\theta g\}.
 \tag{J.13}
$$
The s_B factor cancels in the homogeneous slope column, exactly as
in N.16. Subtract the true radial reference
$\mathcal N_{B,0}=\mu_0\mathsf C_L$:
$$
 \Delta\mathcal N_B
 =(\mu-\mu_0)\mathsf C_L-\mu T_{Z,f}P_\perp
                             +\mu d\,\partial_\theta .
 \tag{J.14}
$$
Since $\|\mathsf C_L:H^{1/2}\to H^{-1/2}\|<2$,
(J.10)--(J.12) prove
$$
 \boxed{\ \|\Delta\mathcal N_B:H^{1/2}\to H^{-1/2}\|
                            <2^{128}(F+\epsilon).\ }       \tag{J.15}
$$
For the higher commutators use the exact Leibniz expansion in
(J.14), with (J.7)--(J.12). In each product the total differentiated
order, including the four lag derivatives and the coefficient
multiplier derivative, is at most q+5. Its factorial products are
bounded by $(q+5)!$, up to the displayed binomial sums.
For $q+5\le2181<4096$, the bound $r!<2^{12r}$, the factors
$512^r=2^{9r}$, the at most $2^{12}$ terms, and the fixed constants
all fit below 65536 bits. Consequently
$$
 \boxed{\ \max_{0\le q\le2176}
 \|\operatorname{ad}_{\partial_\theta}^{\,q}\Delta\mathcal N_B:
                     H^{1/2}\to H^{-1/2}\|
                        <2^{65536}(F+\epsilon).\ }         \tag{J.16}
$$
A generous bound is used deliberately; it is a proved finite derivative
budget, not a numerically estimated seminorm.

Constant height is annihilated. The homogeneous total conormal mean
is zero only after the complete holonomy slope in (J.13) has been
included. This follows by differentiating the true M=1 equation,
as in N.21. It is not obtained by projecting the output mean away.
The actual two curvature means are different rows and remain independent.

## 5. The independent cap Poisson column and all physical charges

First remove the multiplication by mu and define
$$
 \mathcal B_{\rm bare}
       =-s_BD_{f_*}\mathcal K_B\,D_Z\Phi_R .
 \tag{J.17}
$$
The width-zero Green and curvature inverse bounds give
$\|\mathcal B_{\rm bare}:A_0\to\dot A^1_0\oplus\mathbb C\|
<2^{10}s_B\epsilon$ throughout (J.5).
Apply the finite-jet argument to this bare operator. Its
$H^{-1/2}\to H^{1/2}$ weighted matrix has lag factor at most
$2(1+|m-n|)^{1/2}$; four commutators therefore suffice for both
full signed Schur sums. Multiplying afterwards by the actual
real M_mu, already paid in (J.12), proves
$$
 \boxed{\ \|\mathcal B_Z:H^{-1/2}_\perp\to H^{1/2}\|
                                     <2^{128}s_B\epsilon,\ }
$$
$$
 \boxed{\ \max_{0\le q\le2176}
 \|\operatorname{ad}_{\partial_\theta}^{\,q}\mathcal B_Z:
                       H^{-1/2}_\perp\to H^{1/2}\|
                                  <2^{65536}s_B\epsilon.\ }
 \tag{J.18}
$$
Here $\mathcal B_Z=\mu\mathcal B_{\rm bare}$ is precisely the
independent physical N.23 column. Factoring it as in (J.17)
is necessary: an A_0 bound on mu alone is not an A^1 multiplier
bound at zero analytic width.

The full right variation is still
$$
 \delta f_*=
 D_f\Phi_R\,P_\perp g/s_B+D_Z\Phi_R\,\delta Z+f_*^{\rm src}.
 \tag{J.19}
$$
The other incoming source uses its original dot A^2 norm;
(J.18) does not freely give it the curvature-source norm.
The exact B_R and C_R formulas, their two means and the nonmean
Robin output N.23b remain output rows. There is one independent
constant height gauge.

Likewise all ordinary, weak and total-flux charges obey the original
ordered N.24 formula, with the actual unmatched scalar slope c_B.
In particular
$$
 q_L=q_A-\int g_0,\qquad
 \pi_T=P_{\mu_T}\pi_{\rm tmp}
            +{\mu_T\over\langle\mu_T\rangle}q_T,\qquad
 c_B={q_T-\langle\pi_{\rm tmp}\rangle\over\langle\mu_T\rangle}
 \tag{J.20}
$$
are not set to zero. The mean-height span is the true integral
$\int_0^L aw\,D\mu_t(h)\delta h\,dt$; the original remote input
bound is $aw(L)/165$, with no additional epsilon factor.
Metric and parameter columns still differentiate s_B, mu_0,
C_L and the explicit parameters of Phi_R. This theorem concerns
the fixed-metric unknown height and the stated independent curvature port.

## 6. The actual unmatched interface at finite regularity

The boundary correction E_B is part of the actual problem. It cannot
be dropped when the connector and the long background are not matched.

Assume, in the same physical angle and original four-state units at B,
that the short-side complete states obey
$$
 \sum_{A\in\{P_T,U_T,K_T,V_T\}}
       \|\partial_\theta^q A\|_{A_0}
              \le q!128^q n,\qquad 0\le q\le8192 .
 \tag{J.21}
$$
K_T includes its true holonomy mean. The nonmean height at B is the
same f as the long input; its independent scalar height and all source
charges are retained. For the following uniform small-form corollary
assume the stronger, sufficient condition
$$
                  A_*=n+F+\epsilon\le2^{-262144}.           \tag{J.22}
$$
This extra smallness is stated explicitly; it does not follow for every
F allowed by the larger graph domain (J.2).

At B define the exact coefficients and projection
$$
 r_\mu={\mu_T\over\mu_L},\qquad
 b_\mu=\mu_T(d_L-d_T),\qquad
 P_{\mu_T}v=v-{\mu_T\over\langle\mu_T\rangle}\langle v\rangle .
$$
The actual complete interface error is
$$
 \mathcal E_B
   =P_{\mu_T}\{-M_{r_\mu-1}\mathcal N_{B,Z}P_\perp
                                      +M_{b_\mu}\partial_\theta\}.
 \tag{J.23}
$$
Both $\mathcal E_B1=0$ and $\langle\mathcal E_Bv\rangle=0$
are exact properties of this formula. The affine flux formula (J.20)
is separate and need not have zero mean.

Here is a finite-jet estimate which does not borrow the analytic strip
used in the older N.26 bound. Adjoin the finite polynomials for the four
short-side states to (J.5). Their norms are at most 4n/3.
On this parameter disk the actual long boundary state norm is bounded
by $2^8(4F/3)+2^6\epsilon r_f$, by N.19 at width zero.
For a state of norm N less than 1/64 one has
$\|J-1\|\le3N$, $\|D-1\|\le5N$, and the complete convergent
binomial/reciprocal series give
$\|\mu/\mu_0-1\|<32N$, $\|d\|<8N$.
All statements use the full A_0 product norm.

Taking the actual ratios and their true mean denominators therefore gives,
for each of $r_\mu-1$, $b_\mu$, and
$c_T=\mu_T/\langle\mu_T\rangle-1$, the safe complete estimate
$$
 \|\partial_\theta^q c\|_{A_0}
            \le q!512^q\,2^{24}A_*,
                \qquad 0\le q\le8192 .                    \tag{J.24}
$$
The scalar denominator is nonzero on the same whole parameter disk,
because it is the common nonzero mu_0 times 1 plus a norm-small term.
No endpoint upper bound is used as a denominator lower bound.

At the real background (J.12) pays each coefficient multiplier.
Under (J.22), $\|\mathcal N_{B,Z}\|<3$ by (J.15) and
$\|P_{\mu_T}:H^{-1/2}\to H^{-1/2}\|<3$.
The exact product in (J.23) consequently yields the generous bound
$$
 \|\mathcal E_B:H^{1/2}\to H^{-1/2}\|<2^{144}A_* .          \tag{J.25}
$$
For its q-th angular commutator use the same Leibniz formula, retaining
the derivative of the rank-one projection. The coefficient factors
need at most q+1 jets, and the DN factors use (J.16).
Terms with two small factors are absorbed using (J.22).
The complete finite factorial bound, with at most q+5 differentiated
orders, is smaller than the following uniform allowance:
$$
 \max_{0\le q\le2176}
 \|\operatorname{ad}_{\partial_\theta}^{\,q}\mathcal E_B:
                      H^{1/2}\to H^{-1/2}\|
                           <2^{131072}A_* .               \tag{J.26}
$$
There is no derivative of an unrecorded angular analytic width in
(J.24)--(J.26). In particular an old dot A^1 slope mismatch alone
has not been used as a free multiplier bound for its differentiated
drift; the four-state finite jets pay that derivative.

## 7. Complete energy, its adjoint, and the real coordinate

The true radial boundary form obeys
$\mathcal N_{B,0}\ge(1/6)|D_\theta|P_\perp$.
Using the zero constant input and zero homogeneous total flux,
the nonmean half-order conversions give the relative boundary
form bounds
$$
 |\langle\Delta\mathcal N_B f,g\rangle|
 \le2^{133}(F+\epsilon)\,
       \|f\|_{\mathcal N_{B,0}}\|g\|_{\mathcal N_{B,0}},
$$
$$
 |\langle\mathcal E_B f,g\rangle|
 \le2^{149}A_*\,
       \|f\|_{\mathcal N_{B,0}}\|g\|_{\mathcal N_{B,0}} .
 \tag{J.27}
$$
The constant trace is not estimated by a nonmean seminorm; it is
annihilated by the actual two operators.

Let a_0 be the complete radial connector form plus this radial
boundary form, on the original zero-root-trace energy space.
Suppose the actual short connector, in its genuine Piola coordinates,
has already paid a relative coefficient form error eta_C.
The complete actual form is the short form plus the true N_B form
minus the actual E_B form. By (J.27) its full relative perturbation
is bounded by
$$
                  \eta_{\rm all}=\eta_C+2^{150}A_* .
 \tag{J.28}
$$
For $\eta_{\rm all}<1/2$, the entire zero-boundary form and its true
adjoint have bounded inverses, with factor less than 2 relative to
a_0. This is the bounded-form Neumann proof; it does not require the
actual C_R feedback or E_B to be self-adjoint.

For the reference Poisson lift H_f^0 the actual correction is
$$
 w_f=-(A_{00}^0+E_{00})^{-1}E H_f^0,\qquad
 \|w_f\|_{\mathfrak a_0}
 \le{\eta_{\rm all}\over1-\eta_{\rm all}}
                                      \|H_f^0\|_{\mathfrak a_0}.
 \tag{J.29}
$$
Thus elimination to the actual root DN is the Schur complement of
this entire form, with its true primal and adjoint Poisson/contact
operators. No factor L is introduced by this argument, and no
extra Dirichlet condition is imposed at a root-collar endpoint.
The two mean frames and the root mean shear retain the original
geometric normalizations. Their separate short-side estimates
remain part of eta_C and the original root reconstruction.

All angular commutators of the new B-boundary terms through order
2176 have been supplied in (J.16), (J.26). The complete resolvent
commutator expansion can therefore be used with these polynomial
lag bounds in a finite-Sobolev positive-region proof. An analytic
translation family of the new background is unnecessary. A claimed
global tail constant must still include its own short coefficients,
root graph, source windows and all-layer sums; this note supplies
the complete outer-boundary contribution.

For a real degree-one $\theta=\tau(x)$ with $1/2\le j=\tau_x\le2$,
use the scalar height pullback T_tau and the density pullback D_tau.
The exact fixed-x DN is
$$
 \widetilde{\mathcal N}=D_\tau\mathcal N T_\tau^{-1},
 \qquad
 \widetilde{\mathcal N}_0=D_\tau\mathcal N_0T_\tau^{-1}.
 \tag{J.30}
$$
By D.8--D.12 the DN norm bound changes by less than 25, whereas
every relative form bound in (J.27)--(J.29) is exactly unchanged
in this common pulled reference energy. The reference is not
replaced by a bare Fourier multiplier in x.

The stronger positive-half-order Poisson output in (J.18), and a
negative-half-order scalar curvature input, require their own
Jacobian multiplier factors if both are expressed in fixed x.
For example put
$$
 K_x=2(\|j\|_{A_{0,x}}+\|j_x\|_{A_{0,x}}),\qquad
 K_\theta=2(\|j\circ\tau^{-1}\|_{A_{0,\theta}}
       +\|\partial_\theta(j\circ\tau^{-1})\|_{A_{0,\theta}}).
$$
Then D_tau on H^{1/2} has norm below 5K_x, while
$T_\tau^{-1}=M_{j\circ\tau^{-1}}D_\tau^{-1}$
on H^{-1/2} has norm below 5K_theta.
The fixed-x density version of the Poisson column therefore costs
at most $25K_xK_\theta$ times (J.18).
These are actual finite-regularity coefficient norms. The
H^{-1/2} density bound by itself does not pay a scalar curvature
conversion or a positive-order density conversion.

When the angle also varies, the U good tangent and the D.16 good
density derivative are mandatory:
$\dot\lambda-\partial_x(\eta n^\flat)=j(\dot n^\flat-bn^\flat_x)$.
At an unmatched boundary their residual transport remains.
No same-space differentiability claim is made for raw composition.

## 8. Entry from the nearby domains and the remaining coupled equations

For the true B input of the finite-Sobolev tail background,
$f_\theta=P_B$ and $f_{\theta\theta}=U_B$.
Its complete H^{8196} state bound gives directly
$$
 \|\partial_\theta^qf\|_{\dot A^2_0}
 =\|\partial_\theta^qU_B\|_{A_0}
 \le2\|U_B\|_{H^{q+1}}\le2^{-438}\mathscr R,
                   \qquad 0\le q\le8192 .                \tag{J.31}
$$
The last step is the original connector normalization and actual
w/w_0 comparison, not a fixed-x composition assertion.
Consequently this finite background supplies (J.2) with
$F=2^{-438}\mathscr R$. The same actual B-trace contract gives the complete short-state
condition (J.21) with
$$
                         n=2^{-432}\mathscr R .
 \tag{J.32}
$$
For completeness, the physical metric ratio costs less than 2,
each full Fourier A_0 readout costs at most 2 from H^{q+1},
and summing the four states costs at most 4. The holonomy
correction to K is angularly constant; its positive angular jets
vanish and its zeroth jet is the already paid quadratic small
root. These costs fit below $2^6\,2^{-440}\mathscr R$.
This reads the original H^{8196} B trace directly and does not
upgrade a general Y_64 correction. For
$\mathscr R\le2^{-8192000}$, (J.22) follows.
The quantity n is this true short-side bound, not the coarse
entire-long bound $2^{-18}$.

The cap input is the actual physical curvature
$Z=(C_R-C_r)_\perp$ after its true mean-normalized angle.
[F.1--F.24](R133-supplement-cap-finite-Sobolev-ball-to-physical-curvature-jets.md)
prove exactly (J.2) for this Z from the complete cap ball
$\widehat Y=\mathcal H z$, $\|z\|_{\mathfrak M_{8212}}\le2^{-8388608}$.
They use finite real reciprocal/phase/composition identities and
keep both curvature means. Thus the stated cap and tail background
domains supply the actual finite-jet inputs of the present theorem.
This is not a bound for a raw reciprocal in a different coordinate
and is not inferred from a low-order state norm.

For any actual inputs satisfying the stated conditions the complete
nonlinear long graph exists, its physical DN, independent curvature
Poisson port and actual unmatched interface have the proved finite
jet bounds, and the full positive form/adjoint follows under (J.28).
The full cap head/high equations, both curvature means, the
independent metric and nu columns, the constant-height and total-flux
conditions, and the remaining nonlinear global matching are still
the equations to be solved together. No finite-window nu estimate,
proxy tail inverse, or standalone energy estimate is identified
with that final coupled solution.
