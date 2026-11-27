# R144 RPT: all-angular tame derivatives of the actual principal return

2026-11-27, visible-exact-astra-fb31ed6-20261127.

This proves the value, first derivative and full Hessian of the same
two-ray return P at every integer angular order. Both legs, the true
fixed root, all state means, the actual parameter direction and all
original radial joins are retained. The constants are explicit rational
recurrences. A high background norm occurs only linearly; it never
enters a transport exponent or an inverse denominator.

The map is defined away from the solved Gauss--Codazzi and conjugacy
constraints. The sharper low-norm estimates of
[RP](R144-supplement-full-off-constraint-principal-return-Hessian.md)
remain in force. This higher-order result does not replace them, infer a
regular inverse, or identify a candidate phase pivot with a full Schur
complement. Composing with the actual gauge and physical waist chart
still requires their complete chain rules and nonzero residual terms.

## RPT1. Same compact domain, norms and fixed low budgets

Use the compact full-tail domain of RP.3 and TH.1: fixed $\eta_0$,
$|\nu-\nu_0|\le10^{-10}$, and
$Q=\widetilde Q_\nu+q$ with $\sup_r\|q\|_{A^3,\oplus_1}\le10^{-6}$.
The root $r_*$ is unchanged by the metric control, which is supported
in $[1/20,9/50]$. Put $T=2r_*<478/1000$ and use the normalized original
circle, with genuine frequencies $4\mathbb Z$. Set

$$
 B_s=1+\sup_{0\le r\le r_*}\|Q(r)\|_{A^s,\oplus_1},\qquad
 N_s(h,\kappa)=\|h\|_{L^2_r(H^s\oplus_1H^s)}+100|\kappa|,
 \quad s=0,1,2,\ldots .                                  \tag{RPT.1}
$$

$A^s$ has the original weight $(1+|k|)^s$, while $H^s$ is the Bessel
norm. All actual even means are included. A component-sum radial norm
can always be enlarged to the sum of the component $L^2_rH^s$ norms.
The suprema include both one-sided values at each original join.

RP and TH give $\|Q\|_{A^0,1}<10$ and
$\|Q_\phi\|_{A^0,1}<10$. Only the known compact centre has degree32,
as TH.1 explicitly records. Therefore a convenient fixed low bound is

$$
 B_0<11,\qquad B_1<21,\qquad
 B_3\le1+10\cdot129^3+10^{-6}<S:=2^{25}.                 \tag{RPT.2}
$$

No support assertion is made for q or a direction. The high norms
$B_s$, $s>3$, can be arbitrarily large and remain outside all constants.
Hölder interpolation shows $B_j\le B_0^{1-j/n}B_n^{j/n}$, and the
same property holds for the $N_j$ ladder. Ordinary monotonicity will
suffice for most of the estimates below.

Keep precisely RP.5:

$$
 F_\sigma=\beta I(u^2+Kv^2)-\sigma cm,
 \quad m=\Pi v,\quad c=\gamma\sqrt{-K}.                  \tag{RPT.3}
$$

Here I removes only its own intermediate zero mode. The original
mean m and its variations are never removed. Write V for RP.6's
chronological forward-plus-reverse field on $[0,T]$. The completed
uniform bounds on every shorter chronological interval are

$$
 \int_0^T\|V_\phi\|_\infty<.074,\qquad
 \int_0^T\|V_{\phi\phi}\|_\infty<19,\qquad
 J:=27/25,\qquad J^{-1}<X_\phi<J .                       \tag{RPT.4}
$$

These are read from RP, not recomputed. The corresponding second
derivative of every subinterval flow, or its inverse, is below24.

## RPT2. Exact transported-label equation for the forward return

Define the reversed chronological coefficient

$$
                    W(t,\phi)=-V(T-t,\phi).              \tag{RPT.5}
$$

If $X_V(T,0)$ is the original forward flow, the flow of W at T
is exactly $X_V(T,0)^{-1}$. Its transported label p thus solves

$$
 p_t+Wp_\phi=0,\qquad p(0,\phi)=\phi,\qquad p(T,\phi)=P(\phi).
 \tag{RPT.6}
$$

The last equality is an identity of the original lifts. It does not
reset a phase or discard an inverse-endpoint derivative. The periodic
displacement $U=p-\phi$ satisfies

$$
                 U_t+WU_\phi=-W,\qquad U(0)=0.           \tag{RPT.7}
$$

In particular the mean of -W is a genuine forcing in this equation.
The root-leg velocity jump is permitted; p is continuously transmitted
there, with no state impulse. The same convention applies at every
original radial interface. Since T is fixed throughout the parameter
domain, no moving endpoint has been differentiated as if it were fixed.

For later use (RPT.4) on the actual shorter intervals gives

$$
       \|p_\phi\|_\infty<J,\quad
       \|p_{\phi\phi}\|_\infty<24,\quad
       \|p_\phi\|_{A^0}<50.                              \tag{RPT.8}
$$

For the last inequality use the complete embedding
$A^0\le2H^1$ and $J^2+24^2<25^2$. This pays the constant part of
$p_\phi$ as well as its nonconstant modes.

## RPT3. All-order scalar transport estimate on the full circle

The actual angular derivative of W has no contribution from cm.
The quadratic drift and (RPT.2), using
$|\beta|\max(1,|K|)<6$, give the new complete coefficient bounds

$$
 \int_0^T\|W_{\phi\phi}\|_{A^0}\,dt<2^{10},\qquad
 \int_0^T\|\partial_\phi^{n+1}W\|_{A^0}\,dt
                      \le2^{n+7}B_n\quad(n\ge1).         \tag{RPT.9}
$$

Indeed the first integrand is below $2\cdot6\cdot10\cdot10=1200$,
and $1200(478/1000)<2^{10}$. For the second, the primitive removes
one angular derivative exactly. The two-factor Fourier moment bound
gives $60\,2^nB_n$ pointwise, which is more than paid by (RPT.9)
after the full folded length. This concerns the complete unknown
tail, not a trigonometric Bernstein bound on it.

Consider arbitrary real periodic data and the exact transport equation

$$
 z_t+Wz_\phi=f,\qquad z(0)=z_0,\qquad
 {\cal D}_n=\|z_0\|_{H^n}+\int_0^T\|f(t)\|_{H^n}\,dt.    \tag{RPT.10}
$$

Define constants

$$
 K_0=K_1=4,\qquad
 K_n=2^{n+2}J^{n+1}
       [1+2^{n+10}K_{n-1}+2^{2n+10}],\quad n\ge2.       \tag{RPT.11}
$$

Then the full solution, including its mean, obeys

$$
 \sup_t\|z(t)\|_2\le2{\cal D}_0,\qquad
 \sup_t\|z(t)\|_{H^1}\le4{\cal D}_1,
$$
$$
 \sup_t\|z(t)\|_{H^n}\le
       K_n({\cal D}_n+B_n{\cal D}_1)\quad(n\ge2).        \tag{RPT.12}
$$

The last weaker formula with $K_0,K_1$ is also valid at orders0 and1
when $\mathcal D_1$ is finite.

Here is the complete commutator argument. The nth derivative solves

$$
 (\partial_t+W\partial_\phi+nW_\phi)\partial_\phi^nz
 =\partial_\phi^nf-
       \sum_{j=2}^n{n\choose j}W^{(j)}z^{(n+1-j)}.       \tag{RPT.13}
$$

The exact skew part of $W\partial_\phi$ is retained. Its energy
growth together with $nW_\phi$ costs at most $J^{n+1}$, by (RPT.4).
For any two signed frequencies and $2\le j\le n$,

$$
 |\ell|^j|k|^{n+1-j}
       \le|\ell|^2|k|^{n-1}+|\ell|^{n+1}.               \tag{RPT.14}
$$

Split at $|k|\ge|\ell|$ to prove it. The complete lower commutator
therefore has L2 norm at most

$$
 2^n\{\|W''\|_{A^0}\|z\|_{H^{n-1}}
                 +\|W^{(n+1)}\|_{A^0}\|z\|_2\}.        \tag{RPT.15}
$$

The angular constant in z has not been projected out. The formula
still holds at k=0. Integrate (RPT.13), use (RPT.9), and use the
integer Bessel conversion, bounded by $2^n$ times the largest relevant
derivative norm. Induction and $B_{n-1}\le B_n$,
$\mathcal D_{n-1}\le\mathcal D_n$ give (RPT.12); the generous recurrence
(RPT.11) dominates precisely these terms. Only J, $2^{10}$ and fixed
numerical constants enter the recurrence. The high Bn is a single
additive factor.

## RPT4. Complete true-parameter coefficient variations

Write $x=(h,\kappa)$, $y=(k,\rho)$ and put
$\mu=\Pi h_2$, $\lambda=\Pi k_2$. On either original leg the exact
variations, before the chronological sign, are

$$
\begin{aligned}
 (F_\sigma)_x={}&2\beta I(uh_1+Kvh_2)-\sigma c\mu\\
 &+\kappa[\beta K_\nu I(v^2)-\sigma c_\nu m],\\
 (F_\sigma)_{xy}={}&2\beta I(h_1k_1+Kh_2k_2)\\
 &+2\beta K_\nu I(v(\kappa k_2+\rho h_2))
       -\sigma c_\nu(\kappa\lambda+\rho\mu)\\
 &+\kappa\rho[\beta K_{\nu\nu}I(v^2)-\sigma c_{\nu\nu}m].
 \tag{RPT.16}
\end{aligned}
$$

The true intrinsic bounds from RP/TH are
$$
 |\beta K_\nu|<4,\quad |\beta K_{\nu\nu}|<8,\quad
 |c_\nu|<47,\quad |c_{\nu\nu}|<4418.                    \tag{RPT.17}
$$
These derivatives vanish off the original control
support, but no support is used to delete a nonlocal output.
The actual relation $c_{\nu\nu}=-c_\nu^2/c$ and its root-domain
qualification are exactly those proved in RP.

For all integers $n\ge0$, write $Q_n=2^{n+32}$. The full coefficient
jets obey

$$
\begin{aligned}
 \int_0^T\|W_x\|_{H^n}\,dt
 &\le Q_n[N_n(x)+B_nN_1(x)],\\
 \int_0^T\|W_{xy}\|_{H^n}\,dt
 &\le Q_n[N_n(x)N_1(y)+N_1(x)N_n(y)+B_nN_1(x)N_1(y)].
 \tag{RPT.18}
\end{aligned}
$$

Here x and y include their actual metric increments. The complete
angular product estimate is

$$
 \|ab\|_{H^n}\le2^n
       (\|a\|_{H^n}\|b\|_{A^0}+\|a\|_{A^0}\|b\|_{H^n}),
 \qquad \|a\|_{A^0}\le2\|a\|_{H^1}.                    \tag{RPT.19}
$$

Apply it to the literal terms of (RPT.16). I is used in its
original order and has norm at most1 here. The two-leg radial
one-direction conversion has factor $2\sqrt{r_*}<1$; a two-direction
product has factor2 after radial Cauchy--Schwarz. Direct parameter
terms have the true finite support and are also bounded by the larger
whole folded interval. A deliberately generous coefficient ledger is

$$
       24\cdot2^{13}\cdot10^2\cdot8
                          =157286400<2^{32}.            \tag{RPT.20}
$$

It includes every term, at most two background factors, both direction
embeddings, the radial product factor, and the largest true intrinsic
derivative. The $2^n$ in (RPT.18) pays the full angular product moment.
The genuine means in (RPT.16) are angular constants bounded by the
corresponding L2 norm; they are not set to zero. Thus (RPT.18) pays
all Fourier signs and all unknown tail modes.

## RPT5. Explicit recurrences for the nonlinear return map

The complete velocity has a convenient whole Wiener bound
$\|W\|_{A^0}<256$: its quadratic part costs at most
$(6/4)10^2$, and its constant speed at most $7(103/100)7$.
The mean is included in this count. Combining this and (RPT.9) with
the integer Bessel conversion gives

$$
 \int_0^T\|W\|_{H^n}\,dt\le2^{2n+8}B_n,\qquad n\ge0,
 \qquad \int_0^T\|W\|_{H^1}\,dt<2^{10}.
 \tag{RPT.21}
$$

For the last, separately use $\|W_\phi\|_{A^0}\le600$ and
$(256+600)(478/1000)<2^{10}$. Thus this low source bound is a
fixed number; it does not introduce a second high background factor.
Apply the complete transport estimate (RPT.12) to (RPT.7). Define

$$
 R_n=1+2^{2n+12}K_n.                                    \tag{RPT.22}
$$

Then uniformly at every intermediate time,

$$
 \|p-\phi\|_{H^n}\le(R_n-1)B_n,\qquad
 \|p_\phi\|_{H^n}\le R_{n+1}B_{n+1}.                    \tag{RPT.23}
$$

The constant1 in the second estimate is included in the definition
of Rn. These are bounds for the full displacement and its actual
degree-one derivative, including their respective means.

For two input directions let $z_x=D p[x]$ and $z_{xy}=D^2p[x,y]$.
Their exact equations have zero initial values:

$$
\begin{aligned}
 (\partial_t+W\partial_\phi)z_x&=-W_xp_\phi,\\
 (\partial_t+W\partial_\phi)z_{xy}
      &=-W_{xy}p_\phi-W_x(z_y)_\phi-W_y(z_x)_\phi .
 \tag{RPT.24}
\end{aligned}
$$

In particular the mixed parameter and mean terms in (RPT.16) enter
the second equation without modification. There is no solved-PDE
hypothesis in (RPT.24).

The following rational constants specify the complete bounds at all
orders; they are not asymptotic notation:

$$
\begin{aligned}
 D_n&=2^{2n+44}S(1+R_{n+1}),\\
 A_n&=K_n[D_n+(1+S)D_1],\\
 F_n&=4D_n+2^{2n+44}S(1+S)(1+A_2+A_{n+1}),\\
 H_n&=K_n[F_n+(S+2)F_1].
 \tag{RPT.25}
\end{aligned}
$$

This is a well-founded recurrence: first determine all required Kn,
then Rn and Dn, then An, then Fn and Hn. A finite requested order
needs only finitely many of these constants. No background norm
above the fixed S in (RPT.2) enters their definitions.

To see the first source estimate, use the complete product rule
(RPT.19), $\|p_\phi\|_{A^0}<50$, (RPT.18) and (RPT.23).
Also
$\int\|W_x\|_{A^0}\le2\int\|W_x\|_{H^1}
 \le2^{35}SN_1(x)$.
It follows that

$$
 \int_0^T\|W_xp_\phi\|_{H^n}\,dt
       \le D_n[N_n(x)+B_{n+1}N_1(x)].                  \tag{RPT.26}
$$

The factors50 and the two product sums fit well inside the stated
$2^{2n+44}$. At order1 the right side is at most
$D_1(1+S)N_1(x)$. Apply (RPT.12), using
$B_n\le B_{n+1}$, to obtain the complete first derivative estimate

$$
             \sup_t\|z_x\|_{H^n}
                 \le A_n[N_n(x)+B_{n+1}N_1(x)].
 \tag{RPT.27}
$$

For the second source define its temporary bilinear data expression

$$
 \Xi_n(x,y)=N_{n+2}(x)N_2(y)+N_2(x)N_{n+2}(y)
                         +B_{n+2}N_2(x)N_2(y).
 \tag{RPT.28}
$$

The complete $W_{xy}p_\phi$ term is bounded by
$D_n\Xi_n$, using (RPT.18),(RPT.23) exactly as before.
For the other terms, the full product inequality gives

$$
\begin{aligned}
 \|W_x(z_y)_\phi\|_{H^n}\le2^n
 \{&\|W_x\|_{H^n}\|(z_y)_\phi\|_{A^0}\\
   &+\|W_x\|_{A^0}\|(z_y)_\phi\|_{H^n}\}.
 \tag{RPT.29}
\end{aligned}
$$

Here both factors are actual full functions. The low factor obeys

$$
 \|(z_y)_\phi\|_{A^0}\le2\|z_y\|_{H^2}
                        \le2A_2(1+S)N_2(y),
 \tag{RPT.30}
$$

and its high factor obeys
$\|(z_y)_\phi\|_{H^n}
 \le A_{n+1}[N_{n+1}(y)+B_{n+2}N_1(y)]$.
Insert these and (RPT.18) into (RPT.29), integrate, and include the
same complete term with x and y exchanged. The whole second
source in (RPT.24) is bounded by $F_n\Xi_n$.
The term $2^{2n+44}S(1+S)(1+A_2+A_{n+1})$ in (RPT.25)
dominates both product sums; the additional $4D_n$ includes
$W_{xy}p_\phi$ and the harmless monotone enlargements.

At order1 specifically,
$\Xi_1\le(S+2)N_3(x)N_3(y)$. Consequently (RPT.12) gives

$$
\begin{aligned}
 \sup_t\|z_{xy}\|_{H^n}\le H_n\{&
 N_{n+3}(x)N_3(y)+N_3(x)N_{n+3}(y)\\
 &+B_{n+2}N_3(x)N_3(y)\}.
 \tag{RPT.31}
\end{aligned}
$$

The single high background factor in this estimate is genuine.
In (RPT.26),(RPT.29) the high coefficient is always multiplied by a
low solution norm. The transport coefficient $B_n\mathcal D_1$
only encounters the fixed low bound $B_3<S$. At no point is a
high $B_n$ multiplied by another unknown high background norm.
All products of two input directions are integrated using the
stated radial Cauchy--Schwarz bounds, not an artificial radial
L2 trace or pointwise bound for an arbitrary direction.

## RPT6. The actual return, remainder and remaining phase interfaces

Evaluating (RPT.23),(RPT.27),(RPT.31) at T proves, for every integer
$n\ge0$,

$$
 \|P-\operatorname{Id}\|_{H^n}\le R_nB_n,\qquad
 \|DP[x]\|_{H^n}\le A_n[N_n(x)+B_{n+1}N_1(x)],
 \tag{RPT.32}
$$
$$
 \boxed{\ \|D^2P[x,y]\|_{H^n}\le H_n
 \{N_{n+3}(x)N_3(y)+N_3(x)N_{n+3}(y)
                   +B_{n+2}N_3(x)N_3(y)\}.\ }          \tag{RPT.33}
$$

This is a complete tame Hessian with an explicit three-derivative
direction buffer. That buffer is a sufficient norm convention, not
a claim of a sharp loss. It includes the actual metric direction,
the even mean, every Fourier mode and every original characteristic
interface. RP's sharper $530N_0(x)N_0(y)$ and angular-first estimate
continue to be the preferred bounds when their weaker norms suffice.

For an admitted line segment, let $B_s^*$ be its whole supremum.
Taylor's integral formula gives

$$
 \|P(Q+z)-P(Q)-DP(Q)z\|_{H^n}
 \le H_n\{N_{n+3}(z)N_3(z)
                    +B_{n+2}^*N_3(z)^2\}.             \tag{RPT.34}
$$

The notation Q+z here includes the actual increment in nu.
The derivative-difference bound is (RPT.33) with directions z and h
and the same complete segment supremum. No residual is presumed zero.

One can first prove the equations for smooth real fields. Convolve
the full-tail perturbation by positive angular kernels, retaining
the original finite centre, actual means and radial interfaces.
The fixed low domain is preserved and high moments have the same
limits. The exact real transport flows and their first two
variational equations then converge. The estimates above extend the
derivatives by density to their displayed direction norms.
This is differentiability at the declared strong backgrounds,
not existence of a nonlinear value on an unrestricted rough
radial L2 ball. Genuine extra phase impulses, if prescribed in
another problem, would have to be included as independent ports.

For the original moving phase equation
$E=P\circ g-g\circ R_\star$, its full first and second chain rules
remain RP.25--27, with the phase constant retained. PD divides the
current linearized row by $g'\circ R_\star$; this does not replace
the nonlinear map E by their quotient. Higher derivatives of that
operator family must pay the current denominator derivatives, while
the raw $E'a$ term remains in the complete row. The physical residual
is likewise the entire secant in RP.28.
None of these terms, nor a waist trace fee, is deleted by the
present return estimate. Their explicit all-order composition
is the next interface to attach.

The regular finite and high response, complete parameter Schur,
all geometric matching, and a summable same-metric iteration
remain independent obligations. The parameter neighbourhood is
not itself a flex with varying intrinsic metric.

The companion saved-rational calculation uses only the complete
cited conclusions and the new recurrences. It restores no
characteristic carrier and evaluates no old phase integral,
PDE residual, Riccati equation, Fourier norm or signed target.



