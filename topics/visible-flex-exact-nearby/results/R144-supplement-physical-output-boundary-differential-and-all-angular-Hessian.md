# R144 OX: the physical-output boundary differential and all-angular Hessian

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all8 new saved-rational comparisons pass.** The actual
physical boundary residual of
[DH](R144-supplement-full-physical-outer-curvature-residual-Hessian.md)
has a tame first derivative and Hessian at every integer angular
order on the admitted full-tail endpoint domain. One higher endpoint
norm occurs, linearly, at $A^{n+2}$. The displayed safe direction
scale has three angular derivatives of buffer. Both physical means,
the complete long graph and its independent height input are included.

This also identifies the precise off-shell derivative consumed by
[PX](R144-supplement-all-angular-positive-high-inverse-with-the-actual-exterior.md).
DH fixes the **output** physical angle before differentiation.
PX's pullback of that physical tangent is consequently the actual
Fréchet differential, even when the background residual is nonzero.
If the nonlinear residual value is instead first pulled into the
state-dependent moving angle, its additional residual transport is
retained explicitly below. No new residual-smallness test is needed
for the original physical-output convention.

The exact good-tangent identities U.19/U.22 and DH's low-order
Hessian are existing results, not new claims here. The new content
is their complete interface with the actual high graph and a
quantitative all-order tame estimate for the full nonlinear residual.

## OX1. The same nonlinear map and all its scalar rows

Use precisely DH.2--DH.5, including the same intrinsic metric,
$R=25/8$, the whole original parameter range and the independent
endpoint condition

$$
 Q=Q_*+q,\qquad \|q\|_{A^3,\oplus_1}\le10^{-9},\qquad
 g=|D_\theta|^2f_B,\quad
 \|g\|_{A^0_\sigma}\le2^{-60},\quad \sigma\ge1/16 .
 \tag{OX.1}
$$

The unknown $q$ can have infinitely many modes and has no assumed
positive spatial strip. Only the stated height **background** has
the original analytic bound. Directions below need not be analytic.
All means use the original normalized circle measure.

Write

$$
 \begin{gathered}
 m=\langle v\rangle_\phi,\quad j=v/m,\quad
 \Theta=\mathrm{id}+I_\phi(j-1),\quad \Phi=\Theta^{-1},\\
 (B_Q,C_Q)=\Psi(Q)=(u/v,1/v)\circ\Phi,\quad
 Z=P_{\perp,\theta}(C_Q-C_{\rm ref}),\\
 \Gamma(Z,g)=(d(Z,|D_\theta|^{-2}g),
                     c_0(Z,|D_\theta|^{-2}g)).
 \end{gathered}
 \tag{OX.2}
$$

The original full physical map is

$$
 \mathscr R(Q,g)=
 \begin{pmatrix}
 J_\theta B_Q+Q_\theta Z-d(Z,|D_\theta|^{-2}g)\\
 \langle C_Q\rangle_\theta-C_{\rm ref}
                         -c_0(Z,|D_\theta|^{-2}g)\\
 \langle B_Q\rangle_\theta
 \end{pmatrix}.
 \tag{OX.3}
$$

The symbol of the actual $J_\theta$ is $i\operatorname{sgn}k$;
the complete $Q_\theta$ has the original $q_k(R)$, with
$0<q_k(R)<1$. Neither operator is replaced by its leading
part. The output space at order $n$ is

$$
 \mathcal O_n=H^n_{\perp,\theta}\oplus_1\mathbb R\oplus_1\mathbb R.
 \tag{OX.4}
$$

A scalar row has its ordinary absolute value at every order.
The independent overall height translation is separate from
$g$. The long holonomy small root, actual finite interval,
both endpoint lifts and mean-height recovery are the ones
inside the genuine $\Gamma$; none is removed by (OX.3).

## OX2. Exact off-shell identification of the differential

For a moving direction $h$, held fixed in $\phi$, put

$$
 \mu_h=\langle h_2\rangle,\qquad
 \ell_h=D\Theta[h]=m^{-1}I_\phi(h_2-j\mu_h),\qquad
 b_h=\ell_h/j .
 \tag{OX.5}
$$

The primitive input has exactly zero moving mean. Thus this
is the original normalized phase, including the full mean
variation; it is not a newly chosen angular constant.

For any actual physical output $F(Q,g)(\theta)$ and direction
$x=(h,p)$, where $p=|D_\theta|^2\dot f_B$, the chain rule gives

$$
 D(F\circ\Theta)[x]-b_h\partial_\phi(F\circ\Theta)
                         =(DF[x])\circ\Theta .
 \tag{OX.6}
$$

This is an identity at every admitted background, regardless
of whether $F$ is zero. It is exactly U.19/U.22 in the original
moving angle.
The weighted mean satisfies the accompanying full identity

$$
 D\langle jF^\flat\rangle[x]
       =\langle j(D F^\flat[x]-b_h F^\flat_\phi)\rangle.
 \tag{OX.7}
$$

The signed term $Dj[h]=\ell_{h,\phi}$ is included in (OX.7).

For clarity let $r=P_{\perp,\phi}(\mathscr R_1\circ\Theta)$.
Since $\mathscr R_1$ has physical mean zero,
$\mathscr R_1\circ\Theta=J_jr$, with
$J_jf=f-\langle jf\rangle$. Its derivative in $\phi$ equals
$r_\phi$. Applying the ordinary projection only after (OX.6)
therefore gives the exact ordinary-chart equation

$$
 Dr[x]-P_{\perp,\phi}(b_hr_\phi)
       =P_{\perp,\phi}\{(D\mathscr R_1[x])\circ\Theta\}.
 \tag{OX.8}
$$

In particular the Newton equation for the fixed physical map,
$D\mathscr R_1[x]=-\mathscr R_1$, becomes
$Dr[x]-P_{\perp,\phi}(b_hr_\phi)=-r$.
Deleting the transport while differentiating this moving
output would give a different equation.
Using the original fixed physical output (OX.3) requires no
such deletion or residual perturbation argument.

Here is the complete physical differential itself. Put

$$
 (b,c)=D\Psi_Q[h],\quad
 \zeta=P_{\perp,\theta}c,\qquad
 T=D_Zd,\ C=D_Zc_0,\ U=D_gd,\ V=D_gc_0 .
$$

Then, with the actual $m<0$,

$$
 D\mathscr R(Q,g)[h,p]=
 \begin{pmatrix}
 J_\theta b+(Q_\theta-T)\zeta-Up\\
 -\mu_h/m^2-C\zeta-Vp\\
 \langle h_1\rangle/m-\langle u\rangle\mu_h/m^2
 \end{pmatrix}.
 \tag{OX.9}
$$

Thus the scalar curvature-mean equation is not a frozen
constant, and the physical $B$ mean vanishes only for its
actual reflection directions.
The independent Robin datum $r_B$ is the right side of the
first row of (OX.9). For example its nonmean curvature tangent
obeys

$$
 b_\perp=-J_\theta r_B
                +J_\theta(Q_\theta-T)\zeta-J_\theta Up .
 \tag{OX.10}
$$

The mean of $c$ is $C\zeta+Vp+r_C$, with the full independent
$r_C$. Substitution into the exact cap inverse gauge U.24
is precisely QN.34--QN.37 and the full affine family FX.33.
Its normalization, true low endpoint input and all source
charges are those already used in PX.
The supplied head's moving mean and its physical $B$-mean
compatibility still have to satisfy the last two rows;
the high graph does not solve them automatically.

Consequently PX applies to the actual high block of
$D\mathscr R$ with the physical sources just stated.
It is not necessary to regard $P_{\perp,\phi}(b_hr_\phi)$
as a discarded term or an unproved small perturbation.
The distinct moving-output derivative is exactly (OX.8).

### A quantitative norm for the retained transport

The existing FX domain gives
$|m|>5.84$, $\|j-1\|_{A^1}<\epsilon_j=2^{-18}$.
The original primitive satisfies
$\|I:L^2_\perp\to L^\infty\|<1/2$ and
$\|I:L^2_\perp\to H^1\|\le\sqrt{17}/4<33/32$.
Using $h_2-j\mu_h=P_\perp h_2-(j-1)\mu_h$ gives

$$
 \begin{aligned}
 \|b_h\|_\infty
 &\le{1+\epsilon_j\over2(5.84)(1-\epsilon_j)}
                                  \|h_2\|_2<\tfrac1{10}\|h_2\|_2,\\
 \|b_h\|_{H^1}
 &\le{1+\epsilon_j\over5.84}
   \left\{{33/32\over1-\epsilon_j}
               +{\epsilon_j\over4(1-\epsilon_j)^2}\right\}
                                  \|h_2\|_2<\tfrac15\|h_2\|_2,\\
 \|b_h\|_{A^0}&<\tfrac14\|h_2\|_2 .
 \end{aligned}
 \tag{OX.11}
$$

The last estimate uses DH.15, including the possible ordinary
mean of $b_h$. In particular the exact discarded-if-omitted
row in (OX.8) obeys

$$
 \|P_\perp(b_hr_\phi)\|_{L^2_\phi}
       <\tfrac1{10}\|r_\phi\|_2\|h_2\|_2 .
 \tag{OX.12}
$$

This is a norm for the genuine residual transport in its
displayed units. It is not silently inserted into a different
fractional boundary norm or claimed to supply another inverse.

## OX3. All-order constants and a complete real chart estimate

For $s\ge0$ and $x=(h,p)$ define

$$
 B_s=1+\|Q(R)\|_{A^s,\oplus_1},\qquad
 E_s(x)=\|h_1\|_{H^s_\phi}+\|h_2\|_{H^s_\phi}
                                      +\|p\|_{H^s_\theta}.
 \tag{OX.13}
$$

All direction norms refer to the actual endpoint, supplied
independently when the interior direction has only radial
$L^2$ regularity. The height direction has its two true
physical derivatives in $p$.

Only $B_3$ is required bounded a priori. In fact $B_3<10$ on
the actual domain. To check that qualification from completed
endpoint bounds, use $|m|<8$ and
$U_\sigma=1.643190\,10^{-9}$,
$V_\sigma=9.603792\,10^{-9}$ at width $1/8$.
The three derivative factors $8,128,3072$ give

$$
 \|Q(R)\|_{A^3,\oplus_1}
 \le8+3481(U_\sigma+V_\sigma)+10^{-9}<9 .
 \tag{OX.14}
$$

Only the known centre uses its saved strip. The unknown uses
exactly its full $A^3$ norm.

The following large explicit constants are convenient:

$$
 \begin{gathered}
 P_n=2^{80(n+40)}((n+40)!)^{12},\\
 J_n=2^{2n+4}(n+1)!,\qquad
 K_n=2^{2n+44}(n+1)!,\\
 C_n=P_n(2+5J_n+5K_n),\qquad n=0,1,2,\ldots .
 \end{gathered}
 \tag{OX.15}
$$

They depend only on the stated order and low domain.
No high background norm is hidden in them.

We record the real chart estimates needed below:

$$
 \begin{aligned}
 \|D\Psi_Q[h]\|_{H^n_\theta,\oplus_1}
       +\|P_\perp DC_Q[h]\|_{A^n_\theta}
 &\le P_n\{E_{n+3}(h,0)+B_{n+2}E_3(h,0)\},\\
 \|D^2\Psi_Q[h,k]\|_{H^n_\theta,\oplus_1}
 &\le P_n\{E_{n+3}(h,0)E_3(k,0)
                    +E_3(h,0)E_{n+3}(k,0)\\
 &\hspace{32mm}+B_{n+2}E_3(h,0)E_3(k,0)\}.
 \end{aligned}
 \tag{OX.16}
$$

Here is an explicit majorant proof, including the high-factor
qualification. Let $a=(u/v,1/v)$ and use the exact raw
differentials $a_h,a_{hk}$ of UH.14. With
$\beta_h=-\ell_h/j$ and

$$
 \gamma_{hk}=-j^{-1}
 \{\Theta_{hk}+\ell_h'\beta_k+\ell_k'\beta_h
                                      +j'\beta_h\beta_k\},\qquad
 \Theta_{hk}=-m^{-1}(\mu_k\ell_h+\mu_h\ell_k),
$$

the full real formulas are

$$
 \begin{aligned}
 D\Psi_Q[h]&=(a_h+a'\beta_h)\circ\Phi,\\
 D^2\Psi_Q[h,k]
   &=(a_{hk}+a_h'\beta_k+a_k'\beta_h
                    +a''\beta_h\beta_k+a'\gamma_{hk})\circ\Phi .
 \end{aligned}
 \tag{OX.17}
$$

The first formula has at most one pre-existing angular
derivative; the second has at most two. Direction means
and the exact primitive occur explicitly in these expressions.
No equation for the background was used.

At a real point, angular differentiation after composition
is exactly $D_j=j^{-1}\partial_\phi$ before composition:

$$
       \{\partial_\theta^r(F\circ\Phi)\}\circ\Theta=D_j^rF.
 \tag{OX.18}
$$

This avoids any appeal to bounded complex composition.
Expand the displayed algebraic formulas before estimating.
There are fewer than256 signed monomials, with at most32
factors before differentiation, if repeated factors are
counted separately. This count follows directly by expanding
the two terms in each $\ell$, the five terms in $\gamma$
(the first of them has two terms), and the three ratio
components of $a_h,a_{hk}$. Counting their absolute integer
coefficients is also below256.

After $r\le n+1$ applications of $D_j$, the number of factors
and the total power of the reciprocal $j$ are at most
$2n+36$. The total absolute coefficient mass is bounded by
$2^{4p}(p!)^2$, $p=n+40$: each differentiation has fewer than
$4(r+32)$ possible factor/reciprocal charges, and introduces
only the additional factor $j^{-1}$.
The largest total angular frequency degree is $n+2$:
for the first derivative in an $A^n$ norm use one additional
Sobolev derivative, while (OX.17) then has only one
pre-existing derivative. All other uses of (OX.17) require
at most $n$ derivatives and its two pre-existing derivatives.

For completeness the elementary Fourier estimate assigning
this degree is

$$
 \left(\sum_{\alpha=1}^N|\lambda_\alpha|\right)^d
       \le N^{d-1}\sum_{\alpha=1}^N|\lambda_\alpha|^d
             \quad(d\ge1).
 \tag{OX.19}
$$

Apply it to the complete signed convolution kernel of each
monomial. It places the higher moment on exactly one
background or one direction. All other factors retain their
low norms, bounded by10 for the background and by $2E_3$ for
a direction. A direction with moment $n+2$ costs at most
$2^{n+3}E_{n+3}$ by the full fourfold Cauchy--Schwarz
embedding; a background with that moment costs $B_{n+2}$.
The original primitives have their exact zero coefficient
and all other signed frequencies, with divisor at least4.
Scalar direction means are zero-frequency factors in this
same count.

Reciprocals are summed as their genuine convergent series in
$e=j-1$, $\|e\|_{A^0}<2^{-18}$. A power at most $2n+36$
has coefficients bounded by
$\binom{q+2n+35}{2n+35}$. With the frequency degree $n+2$,
its total series is bounded by a constant times

$$
 \sum_{q\ge0}(q+2n+36)^{3n+38}(2^{-18})^q .
 \tag{OX.20}
$$

When the high moment is on a reciprocal factor, shift the
index by one and use the corresponding
$(2^{-18})^{q-1}$ series. There is no division by an
unknown parameter norm or missing zero-parameter case.
Both bounds follow from
$\sum_{q\ge0}(q+1)^r\epsilon^q
\le r!/(1-\epsilon)^{r+1}$.

With $p=n+40$, the complete series, coefficient and low
factor charges are dominated by

$$
 2^{8p}\,2^{4p}(p!)^2\,
          (2p)^{3p}(3p)!\,2^{3p+1}\,2^{3p}
       <2^{40p}(p!)^8<P_n .
 \tag{OX.21}
$$

One may use $p^p<3^pp!$ and
$(3p)!\le3^{3p}(p!)^3$ for the last comparison.
The last $2^{3p}$ also covers the real change of measure,
the Bessel sum and the one extra Cauchy--Schwarz derivative
when an $A^n$ norm is requested.
This proves (OX.16). In particular a product of two high
background norms was never introduced and subsequently
ignored.

The same proof for $C_Q=(1/v)\circ\Phi$, together with the
known height background, gives for $n\ge1$

$$
 \Gamma_n:={\|\partial_\theta^n Z\|_{A^0}\over5\,10^{-10}}
              +{\|\partial_\theta^n g\|_{A^0}\over10^{-11}}
                         \le P_nB_{n+2}.
 \tag{OX.22}
$$

The parameter normalizers cost less than $2^{37}$.
The analytic height contribution is at most
$10^{11}n!16^n2^{-60}$ and fits in the same displayed
majorant. Set $\Gamma_0=1$ in estimates at order zero.
This convention is an enlargement, not a missing constant
mode in $Z$ or $g$.

## OX4. The full function-parameter second derivative of the long graph

Use the complete physical-angle operator family
[DT.2--DT.13](R144-supplement-all-angular-exterior-DN-tame-inverse-in-real-function-spaces.md).
Its actual background mass is $t<.081$, hence $3t<.243<1/4$.
Its two genuine $L^2$ module column bounds are
$M_Z=.0035$, $M_B=.00039$, including their scalar output
rows. They are holomorphic on the zero-width function ball
with radii $5\,10^{-10}$ and $10^{-11}$.

For a pair $X=(\zeta,p)$ write
$|X|_{A^s}=\|\zeta\|_{A^s}+\|p\|_{A^s}$ and similarly
for Sobolev norms. The full Taylor-kernel estimates imply

$$
 \|D\Gamma[Y]\|_{H^n\oplus_1\mathbb R}
       \le J_n\{|Y|_{H^n}+\Gamma_n|Y|_{L^2}\},
 \tag{OX.23}
$$

and

$$
 \begin{aligned}
 \|D^2\Gamma[X,Y]\|_{H^n\oplus_1\mathbb R}
 \le K_n\{&
 |X|_{A^0}|Y|_{H^n}+|X|_{A^n}|Y|_{L^2}\\
                    &+\Gamma_n|X|_{A^0}|Y|_{L^2}\}.
 \end{aligned}
 \tag{OX.24}
$$

These bounds concern the actual infinite Fourier module.
Here is the complete second-derivative summation, rather
than a formal assertion of smooth dependence.
Write one derivative column as
$A(Y_0)=\sum_{q\ge0}A_q(Y_0^q)$, with
$\|A_q\|\le3^qM$ as in DT.11. Differentiating in $X$
gives $qA_q(X,Y_0^{q-1})$.
For an input frequency $k$, the frequency of $X$, and
the remaining background lags, the exact output is their
signed sum. A Bessel weight of order $n$ is bounded by
$3^n$ times the sum of its three corresponding weights.

Put $x_0=1/4$. The terms with the high derivative on $X$
or on the module input sum to

$$
            3^n\,{3M\over(1-x_0)^2}
                         <6\,3^nM .
 \tag{OX.25}
$$

For the high background moment use, with $q\ge2$,
the full sum
$q\,3^q(q-1)^nt^{q-2}\Gamma_n$.
Writing $r=q-1$ and using $r+1\le2r$ gives its bound

$$
 3^n\,{18M(n+1)!\over(1-x_0)^{n+2}}\Gamma_n
                      =32\,4^nM(n+1)!\Gamma_n .
 \tag{OX.26}
$$

The normalized parameter direction costs less than
$2^{37}|X|_{A^s}$. Equations (OX.25)--(OX.26), with
the complete column sum retained, are dominated by the
stated $K_n$. The analogous undifferentiated series gives
$J_n$ in (OX.23).
At order zero the elementary direct geometric bounds are
smaller than these constants with $\Gamma_0=1$.

For scalar output a kernel is supported on exact total
frequency zero. Its scalar norm is still included in the
same summation; no row is suppressed by angular
differentiation. Symmetry gives (OX.24) with $X,Y$
interchanged as well. Smooth directions are dense in
the displayed norms, so this is the genuine mixed
extension to the stated nonanalytic directions.

## OX5. The complete physical residual is tame at every order

For $x=(h,p)$ and $y=(k,t)$ define

$$
 \mathcal T_n(x,y)=
 E_{n+3}(x)E_3(y)+E_3(x)E_{n+3}(y)
                         +B_{n+2}E_3(x)E_3(y).
 \tag{OX.27}
$$

The all-order conclusions are

$$
 \boxed{\displaystyle
 \begin{aligned}
 \|D\mathscr R(Q,g)[x]\|_{\mathcal O_n}
       &\le C_n\{E_{n+3}(x)+B_{n+2}E_3(x)\},\\
 \|D^2\mathscr R(Q,g)[x,y]\|_{\mathcal O_n}
       &\le C_n\,\mathcal T_n(x,y).
 \end{aligned}}
 \tag{OX.28}
$$

The original DH bound with constant10000 remains the
sharper low-order estimate. The constants (OX.15) pay
arbitrary orders, rather than a new small contraction
test.

To prove the complete chain rule, let
$X=(P_\perp DC_Q[h],p)$ and
$Y=(P_\perp DC_Q[k],t)$.
The already paid DH.14--DH.16 give

$$
 |X|_{L^2}\le E_3(x),\qquad |X|_{A^0}\le2E_3(x).
 \tag{OX.29}
$$

The stronger bounds in (OX.16), including the elementary
height embeddings, give

$$
 |X|_{H^n},\ |X|_{A^n}
       \le P_n\{E_{n+3}(x)+B_{n+2}E_3(x)\}.
 \tag{OX.30}
$$

Using (OX.22) and (OX.24) now bounds
$D^2\Gamma[X,Y]$ by $5K_nP_n\mathcal T_n(x,y)$.
The factor5 includes the two terms carrying a higher
input and all three single-background contributions.
There is no multiplication of two high bounds in this
substitution: the low terms always use (OX.29).

The full chain rule also contains
$D_Z\Gamma\,P_\perp D^2C_Q[h,k]$.
Its $H^n$ term is controlled by (OX.16).
For the $L^2$ term use UH.1, giving
$\|D^2C_Q[h,k]\|_2\le4E_3(x)E_3(y)$ independently
of the high background. Equation (OX.23) therefore
bounds this additional whole row by
$5J_nP_n\mathcal T_n(x,y)$.

Finally the linear map of the two curvatures into
the three rows of (OX.3) has norm at most2 at every
order: its genuine Fourier multipliers have norm at
most1, and both constant observations are retained.
Its Hessian contribution is at most
$2P_n\mathcal T_n(x,y)$.
These three bounds add to exactly the chosen $C_n$.
The first derivative in (OX.28) follows in the same
way from (OX.16), (OX.22)--(OX.23), with the smaller
coefficient $P_n(2+2J_n)$.

All identities are off shell. In particular
$\langle C_Q\rangle=1/m$ and
$\langle B_Q\rangle=\langle u\rangle/m$ have their
actual first and second derivatives, and the long
$c_0$ output remains in both chain-rule terms.
The nonzero original curvature residual is not
assumed away.

## OX6. Actual tame remainders and the scope of the result

Let all required real segments stay in (OX.1), and put

$$
 N(x)=\mathscr R((Q,g)+x)-\mathscr R(Q,g)
                                      -D\mathscr R(Q,g)x .
$$

If $B^*_{n+2}$ is the maximum of the single high
endpoint norm on that segment, the integral Taylor
formula gives the complete remainder

$$
 \|N(x)\|_{\mathcal O_n}
 \le C_n\{E_{n+3}(x)E_3(x)
                         +\tfrac12B^*_{n+2}E_3(x)^2\}.
 \tag{OX.31}
$$

For two increments, suppose their connecting and
base segments stay in the same domain, and their
low and high direction norms are at most
$\rho_3$ and $\rho_{n+3}$. Then

$$
 \begin{aligned}
 \|N(x)-N(y)\|_{\mathcal O_n}\le C_n\{&
 \rho_3E_{n+3}(x-y)+\rho_{n+3}E_3(x-y)\\
                    &+B^*_{n+2}\rho_3E_3(x-y)\}.
 \end{aligned}
 \tag{OX.32}
$$

These follow by integrating the same genuine
Hessian, retaining both means throughout.
They do not extend nonlinear background paths
beyond the independent height domain in (OX.1).
The linear and bilinear derivatives themselves
extend to the displayed rough directions by the
module argument.

Together with PX this supplies the high inverse
and full nonlinear curvature boundary tame estimates
in one consistent fixed-physical-output convention.
The actual world-height and phase equations, the
original finite/mean/parameter inverse, and a
convergent global iteration still have their own
obligations.
No generic radial trace is inferred here.

The companion
[rational combination](../scripts/fourfold_codazzi_physical_boundary_tame_saved_bounds.py)
evaluates only8 new elementary combinations of the
saved endpoint and function-parameter bounds.
It restores no native array, evaluates no long
solution or reference equation, and repeats no
completed scientific target.
