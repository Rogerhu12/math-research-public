# R766: original T descent gives a forty-step ordinary exchange

Date: 2026-11-14. **Status: proved.** Keeping the same original
$X_t$, one can choose its R736 witness $Y$ so that
$N_TY=21A_\alpha$ and the unit
$H=R_{\Gamma S}(Y)/43$ is ordinary, has all three norms
zero, and belongs to $(t-1)^{40}E_M$. Consequently the
original common primitive satisfies
$\mathcal L_{\Gamma S}\in(t-1)^{41}E_M$.
The original real marking can be imposed while retaining
all these conclusions. The construction does not evaluate
$J_\ell$ or $b$ or delete either diagonal derivative in
the remaining dual descent problem.

## 1. Actual data and a general simultaneous norm input

Retain $p=43$, $\mathcal O=\mathbf Z_{43}[i]$, $k=\mathcal O/p$,
the original fields $M=LB$, $F_t=B^S$, $N=LF_t$, and
groups $\Gamma=\langle\gamma\rangle$, $S=\langle s\rangle$,
$T=\langle t\rangle$. Put $\pi=\gamma-1$ and $X=t-1$.
All ordinary units and full divisors are in the same completed
character component, with the original unaveraged $P_+$.

Fix the original $X_t$ throughout:

$$
\operatorname{div}_{F_t}X_t=P_+P_0,\qquad
N_TX_t=A_\alpha.
\tag{766.1}
$$

If $\mathfrak q=P_+Q_M$, its divisor in $M$ is
$\operatorname{div}_M X_t=p\mathfrak q$.
Both $\Gamma$ and $S$ fix the q primes, while $T$
permutes their $43$ original labels.

We use the following full ordinary form of R736's
simultaneous norm lemma. For any $d\in\mathcal O[T]$
with $d(1)\in p\mathcal O$, put $x=d(t)X_t$.
There is a genuine global q-unit $Y_d$ with

$$
\boxed{
\operatorname{div}_M Y_d=d(t)\mathfrak q,\qquad
N_\Gamma Y_d=N_SY_d=x.
}
\tag{766.2}
$$

To recall why this is a global ordinary assertion, the
actual class $e_q=[\mathfrak q]\in A_M$ is a nonzero
order-$p$ socle element fixed by $T$. Thus
$[d(t)\mathfrak q]=d(1)e_q=0$, giving a q-unit with
the exact full divisor. Its $\Gamma$-norm error is an
ordinary unit of $B$. The target $x$ is a field norm
from $M/B$: at q the unramified scalar degree-$p$
base change kills the original tame local norm obstruction;
at p and 2 the extension is split; at all other places
$x$ is a unit in an unramified extension. The cyclic
norm theorem and R731's equality of normic ordinary
units with ordinary unit norms remove the error by
an ordinary unit.

For a corrected element with $N_\Gamma Y_d=x$, the
remaining scalar error $N_SY_d-x$ belongs to
$K_N=\ker N_\Gamma E_N$. At every marked q place it
is $(N_S-N_\Gamma)Y_d$, with the full local uniformizer
part included. R736 proves that its residue obstruction
in the exact ordinary quotient

$$
K_N/N_S\ker N_\Gamma E_M
=R_\Gamma[T]c_t/(\pi,N_T)R_\Gamma[T]c_t
$$

is zero. The resulting ordinary kernel correction
removes this scalar error without changing the
$\Gamma$ norm or any divisor. This proves (766.2).
It is precisely the original lemma, applied with
the specified $d$; it does not choose a new prime
or replace a global unit by a local norm root.

For each fixed $d$ and $x$, the choices in (766.2)
form a torsor under
$K_{\Gamma S}=\ker N_\Gamma E_M\cap\ker N_SE_M$.

## 2. The ordinary Gamma-scalar exchange for every such d

Let $Y_d,x,d$ satisfy (766.2), and set $k_0=21$ and

$$
D_i=\sum_{a=0}^{42}ag_i^a,\qquad
B_i=D_i-k_0N_i\quad(i=\Gamma,S).
$$

Define

$$
R_\Gamma(d)=B_\Gamma Y_d,
\qquad R_S(d)=B_SY_d,
\qquad R(d)=B_\Gamma B_SY_d
          =D_\Gamma D_SY_d-pk_0^2x.
\tag{766.3}
$$

All three are ordinary units. The first two remove the
identical divisors $pk_0d(t)\mathfrak q$, and the
two terms in the last expression have divisor
$p^2k_0^2d(t)\mathfrak q$. The exact operator identity
$(g_i-1)D_i=p-N_i$ gives

$$
\begin{aligned}
\pi R_\Gamma(d)&=(s-1)R_S(d)=pY_d-x,\\
N_\Gamma R_S(d)&=N_SR_\Gamma(d)=0,\\
\pi R(d)&=pR_S(d),\qquad
(s-1)R(d)=pR_\Gamma(d),\\
N_\Gamma R(d)&=N_SR(d)=0.
\end{aligned}
\tag{766.4}
$$

We need the following general form of R761:

$$
\boxed{
R(d)=pH_d-\rho_d u,
\quad H_d\in E_M,\quad \rho_d\in\mathcal O,
}
\tag{766.5}
$$

where the same $H_d$ satisfies

$$
\boxed{
\pi H_d=R_S(d),\qquad
(s-1)H_d=R_\Gamma(d),\qquad
N_\Gamma H_d=N_SH_d=\rho_d u.
}
\tag{766.6}
$$

Here the residue of $\rho_d$ can depend on the chosen
witness. Formula (766.5) is not a claim that it has
already been normalized to zero.

### 2.1 The complete q-phase calculation, including arbitrary poles

At an actual q completion, the residue field of $M$
is $\mathbf F_{q^{2p}}$ and its entire p-primary
residue group is $\mu_{p^2}$. The actual marked
scalar action is $s=1+2p\pmod{p^2}$; $\Gamma$ is
inertia. Use the original real q-ray uniformizer
$\theta$, which is $S$-fixed and has positive
$\gamma\theta/\theta\equiv\zeta$.

At any marked translate, write
$Y_d=n\theta+V$, with its actual valuation
$n\in\mathcal O$ and a local unit $V$. No property
of $n$ other than its actual value is needed. The
two sums are

$$
\sum_{a=0}^{p-1}(a-k_0)=0,
\qquad
\sum_{a=0}^{p-1}a(a-k_0)
=\frac{p(p^2-1)}{12}\in p\mathbf Z.
\tag{766.7}
$$

For $B_S$, the first sum removes the uniformizer
part exactly, since $s\theta=\theta$. If the
$\mu_{p^2}$ phase of $V$ is $\xi^e$, its exponent
after applying $B_S$ is

$$
e\sum_a(a-k_0)(1+2p)^a
\equiv 2pe\sum_a a(a-k_0)=0\pmod{p^2}.
$$

For $B_\Gamma$, zero augmentation removes the
unit residue, because inertia fixes it. The
uniformizer power is also removed by zero
augmentation, while its residual $\mu_p$ exponent
is $n\sum_a a(a-k_0)=0\pmod p$.
Thus both $R_S(d)$ and $R_\Gamma(d)$ have zero
full p-primary phase at every q prime. This
calculation also applies to each T translate
and every Delta transport. All character
coefficients and the unaveraged $P_+$ are
retained linearly.

### 2.2 The ordinary primitive and its lower norm

R761's ordinary phase injection applies in the same
field $M/B$. Explicitly, a Hilbert 90 primitive
of the $\Gamma$ cocycle $R_S(d)$ has an invariant
full divisor. At q its valuations modulo $p$
are exactly the phases of $R_S(d)$; these are
zero. At every other prime, $M/B$ is unramified
or split, so its invariant divisor descends
integrally. Since the original character class
group $A_B$ is zero, subtracting a full principal
divisor from $B$ makes that primitive ordinary.
This gives $F_0\in E_M$ with $\pi F_0=R_S(d)$.

The error $(s-1)F_0-R_\Gamma(d)$ belongs to $E_B$
and has scalar norm zero, by (766.4). The actual
free lattice $E_B=\mathcal O[S,T]u_B$ gives an
ordinary scalar primitive of that error. Subtract
it to obtain $F\in E_M$ with

$$
\pi F=R_S(d),\qquad (s-1)F=R_\Gamma(d).
$$

It follows from (766.4) that
$e=pF-R(d)\in E_{F_t}$, and applying both norms
gives $N_\Gamma F=N_SF=e$.

At every T translate, $(s-1)F=R_\Gamma(d)$ has
zero full $\mu_{p^2}$ phase. Hence the phase
of $F$ lies in $\mu_p$, and its $\Gamma$ norm
$e$ has zero phase. Since
$E_{F_t}=\mathcal O[T]u_t$ and the original
phase polynomial $A_u$ has annihilator $kN_T$,
this full vanishing vector gives

$$
e=ph_t+\rho_d u\qquad(h_t\in E_{F_t}).
$$

Taking $H_d=F-h_t$ proves (766.5)--(766.6).
This proof includes all ordinary divisor and
phase steps; it does not assume that the special
coefficient polynomial is $D_T$.

## 3. The first exact T descent already achieves all three zero norms

For clarity, one step can be stated without any long
iteration. Set

$$
d_0(T)=D_T(T)=\sum_{a=0}^{42}aT^a,
\qquad c_0=d_0(1)=pk_0,
\qquad d_1(T)=\frac{d_0(T)-c_0}{T-1}.
\tag{766.8}
$$

This is an integral polynomial and

$$
d_1(1)=d_0'(1)=\sum_{a=0}^{p-1}a^2
=\frac{p(p-1)(2p-1)}6\in p\mathbf Z.
$$

Apply (766.2) to $d_1$ and let $Y_1$ be the resulting
q-unit. Define

$$
Y_0=k_0X_t+(t-1)Y_1.
\tag{766.9}
$$

Its divisor and its $\Gamma,S$ norms are exactly
those of the original R736 witness. For instance
$p k_0+(t-1)d_1=d_0$ as an integral group-ring
identity. It also satisfies

$$
N_TY_0=k_0A_\alpha.
\tag{766.10}
$$

The balanced operators kill $X_t$, since it is
fixed by both $\Gamma$ and $S$. Therefore

$$
R(d_0)=(t-1)R(d_1)
      =(t-1)(pH_{d_1}-\rho_{d_1}u)
      =p(t-1)H_{d_1}.
$$

The last equality uses the actual equality
$(t-1)u=0$. Thus $R(d_0)/p$ is ordinary and is
the ordinary T boundary $(t-1)H_{d_1}$.
Both its $\Gamma$ and $S$ norms are zero by
(766.6), and its $T$ norm is zero because it is
a T boundary.

This construction simultaneously imposes the
T norm in (766.10) and removes the residual
coefficient in (766.5) for $Y_0$. It does not
assume that two arbitrary torsor adjustments
can be made independently.

## 4. The exact Taylor coefficients and the forty permitted steps

Use a uniform index for the whole construction. Write

$$
D_T(1+X)=\sum_{r=0}^{42}c_rX^r,
\qquad
d_r(T)=X^{-r}\left(D_T(T)-\sum_{j<r}c_jX^j\right).
\tag{766.11}
$$

Here $X=T-1$ in polynomial expressions, and the
displayed quotient is an actual integral polynomial.
Thus $d_r(1)=c_r$ and

$$
d_r=c_r+Xd_{r+1}.
\tag{766.12}
$$

Since

$$
N_T(1+X)=\frac{(1+X)^p-1}{X}
=\sum_{r=0}^{42}\binom p{r+1}X^r,
\qquad D_T=T\frac{dN_T}{dT},
$$

the exact coefficients are

$$
c_r=(r+1)\binom p{r+2}
       +r\binom p{r+1},
\tag{766.13}
$$

with a binomial coefficient outside its range equal
to zero. For $0\le r\le40$, both occurring
nonzero binomial coefficients have lower index
strictly between $0$ and $p$. Therefore

$$
c_r\in p\mathbf Z\quad(0\le r\le40).
\tag{766.14}
$$

The last three exact coefficients are

$$
\begin{aligned}
c_{40}&=41\cdot43+40\binom{43}{41}
       =37883=43\cdot881,\\
c_{41}&=42+41\cdot43=1805\equiv-1\pmod{43},\\
c_{42}&=42\equiv-1\pmod{43}.
\end{aligned}
\tag{766.15}
$$

In particular the top input that is actually needed is
the small-degree integral polynomial

$$
\boxed{d_{40}(T)=37883+1805X+42X^2.}
\tag{766.16}
$$

Its augmentation is $43\cdot881$, so the original
global lemma (766.2) applies to it.

Choose one actual $Y_{40}$ from that lemma. For
$r=39,38,\ldots,0$, define successively

$$
\boxed{Y_r=\frac{c_r}{p}X_t+(t-1)Y_{r+1}.}
\tag{766.17}
$$

The coefficients $c_r/p$ are integral by (766.14).
An induction using (766.12) proves

$$
\operatorname{div}_M Y_r=d_r(t)\mathfrak q,
\qquad N_\Gamma Y_r=N_SY_r=d_r(t)X_t.
\tag{766.18}
$$

For every $r<40$ the construction also gives
$N_TY_r=(c_r/p)A_\alpha$. In particular
$Y_0$ is an original witness with
$N_TY_0=21A_\alpha$, while the top $Y_{40}$ is
not assigned an unproved T norm.

## 5. The actual depth of the ordinary common primitive

Let $R_r=B_\Gamma B_SY_r$. Since the two balanced
operators kill the base term in (766.17),

$$
R_r=(t-1)R_{r+1},\qquad R_0=(t-1)^{40}R_{40}.
\tag{766.19}
$$

Apply the proved general exchange (766.5) to the
single top witness:

$$
R_{40}=pH_{40}-\rho_{40}u,
\qquad
N_\Gamma H_{40}=N_SH_{40}=\rho_{40}u.
$$

Because $(t-1)u=0$, (766.19) becomes

$$
R_0=p(t-1)^{40}H_{40}.
$$

Thus the actual ordinary unit

$$
\boxed{H=R_0/p=(t-1)^{40}H_{40}\in E_M}
\tag{766.20}
$$

has

$$
\boxed{N_\Gamma H=N_SH=N_TH=0.}
\tag{766.21}
$$

The first two follow by applying $(t-1)^{40}$
to $\rho_{40}u$; the last follows from the exact
group-ring equality $N_T(t-1)=0$.
There is no claim that $\rho_{40}$ is known or
that it had to be set to zero.

For the associated original cube based on this
$Y_0$, R761 gives

$$
\boxed{
\mathcal L_{\Gamma S}
=-\mathcal W_{\Gamma S}/p
=(t-1)H=(t-1)^{41}H_{40}.
}
\tag{766.22}
$$

It is a genuine ordinary unit with all three norms
zero, and its exact derivatives remain

$$
\pi\mathcal L_{\Gamma S}=\mathcal V_S,
\qquad
(s-1)\mathcal L_{\Gamma S}=\mathcal V_\Gamma,
\qquad
\pi(s-1)\mathcal L_{\Gamma S}=\mathcal U.
\tag{766.23}
$$

Consequently the same ordinary cube also has

$$
\mathcal V_S,\mathcal V_\Gamma,\mathcal U
\in(t-1)^{41}E_M.
\tag{766.24}
$$

These are exact statements in the integral ordinary
lattice, not only in its local image or modulo $p$.

## 6. The real average preserves the whole construction's conclusions

Fix the original real $X_t$ as in R763 and the
reconstructed first-moment note. Throughout the
preceding construction this same $X_t$ has been
kept fixed. Let $C_X=(N_T-1)X_t$ and replace
the constructed $Y_0$ by

$$
Y_0^{\rm real}=(Y_0+C_X-\tau Y_0)/2.
\tag{766.25}
$$

R763 proves that this is an allowed ordinary torsor
change and imposes
$Y_0^{\rm real}+\tau Y_0^{\rm real}=C_X$.
Its T norm remains $21A_\alpha$: indeed
$N_TC_X=42A_\alpha$, and both $N_TY_0$ and
its conjugate equal $21A_\alpha$.

The exact semilinear operator identities are

$$
\tau B_\Gamma=-\gamma B_\Gamma\tau,
\qquad \tau B_S=B_S\tau,
\qquad \tau(t-1)=-t^{-1}(t-1)\tau.
$$

Since $B_\Gamma B_SC_X=0$, its new exchange unit is

$$
R_0^{\rm real}=(R_0+\gamma^{-1}\tau R_0)/2.
$$

Hence

$$
H^{\rm real}=R_0^{\rm real}/p
             =(H+\gamma^{-1}\tau H)/2
\tag{766.26}
$$

is still ordinary and has all three norms zero.
The submodule $(t-1)^{40}E_M$ is stable under
$\tau$, because conjugation multiplies this
operator by the unit $t^{-40}$ and the exponent
$40$ is even. Therefore

$$
H^{\rm real}\in(t-1)^{40}E_M,
\qquad
\mathcal L_{\Gamma S}^{\rm real}
=(t-1)H^{\rm real}\in(t-1)^{41}E_M.
\tag{766.27}
$$

The exact real laws are
$\tau H^{\rm real}=\gamma H^{\rm real}$ and
$\tau\mathcal L_{\Gamma S}^{\rm real}
=-\gamma t^{-1}\mathcal L_{\Gamma S}^{\rm real}$.
Thus imposing the real marking does not lose a
norm equation, the integral p-division, or the
proved T depth.

Every constructed and averaged $Y_0$ lies in the
same original torsor. R763's ordinary coboundary
calculation preserves $\eta_\alpha$ and its entire
phase vector, so the same $J_\ell$ has been retained.

## 7. The next polynomial principalization has a genuine obstruction

The next formal polynomial would be

$$
d_{41}(T)=1805+42X.
$$

Its q divisor has actual class

$$
[d_{41}(t)\mathfrak q]
=c_{41}e_q=-e_q\ne0
\quad\hbox{in }A_M.
\tag{766.28}
$$

Thus there is no global completed multiplicative
element with that exact divisor. This is stronger
than merely failing to meet a convenient hypothesis
of (766.2). Adding a multiple of $N_T$ to a
group-ring antiderivative changes its augmentation
by a multiple of $p$ and cannot remove (766.28).

Accordingly the same exact-divisor recursion has
$40$ permitted peeling steps and then stops at
the original nonzero q socle. This is consistent
with R756/R758, where the fixed marked class has
nonzero leading coefficient $19X^{40}$ in
$H^1(S,K_\Gamma)=k[X]/X^{42}$.
No assertion is made that every other conceivable
construction or every different ordinary unit
has the same maximal depth.

## 8. The remaining dual equation is compressed, not discarded

For the chosen representative write
$\mathcal L_{\Gamma S}=(t-1)^{41}H_{40}^*$,
where $H_{40}^*$ is ordinary; after the real average
it is the corresponding averaged top unit.
Then the two actual diagonal residuals are exactly

$$
\pi^2\mathcal L_{\Gamma S}
=(t-1)^{41}\pi^2H_{40}^*,\qquad
(s-1)^2\mathcal L_{\Gamma S}
=(t-1)^{41}(s-1)^2H_{40}^*.
\tag{766.29}
$$

For example the ordinary candidate
$e_*=2\mathcal V_S-2i\mathcal V_\Gamma$
for the required restricted dual class has

$$
\begin{aligned}
\pi e_*&=-2i\mathcal U
             +2\pi^2\mathcal L_{\Gamma S},\\
(s-1)e_*&=2\mathcal U
             -2i(s-1)^2\mathcal L_{\Gamma S}.
\end{aligned}
\tag{766.30}
$$

Thus the diagonal terms really occur even after
the ordinary T descent. Equations (766.29)--(766.30)
place them in the proved deep submodule; they do
not show that they vanish modulo $p$ or supply
the full $T$ invariance and rational supported
descent required in R755. Those are the remaining
conditions on the original dual primitive.

The actual $J_\ell,b,\sigma_2,I_\alpha$ are still
not evaluated, and no abstract identification of
socles or choice of a local norm root is used.

## Dependencies

- [R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md):
  the actual $u_t$, full ordinary lattice, and residue derivative.
- [R731](R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md):
  the nonzero q socle and genuine ordinary Gamma corrections.
- [R736](R736-original-three-norm-exchange-and-minus-four-moment-phase.md), §5:
  the original arbitrary-$d$ simultaneous norm lemma.
- [R756](R756-original-three-norm-ordinary-lattice-and-exact-scalar-cohomology.md):
  the ordinary cube and exact leading coefficient $19$.
- [R761](R761-original-Gamma-scalar-ordinary-exchange-and-integral-p-division.md):
  the ordinary phase injection and full two-direction exchange.
- [R763](R763-ordinary-torsor-normalization-with-fixed-moment-and-real-marking.md):
  the exact ordinary torsor, fixed moment, and real normalization.
