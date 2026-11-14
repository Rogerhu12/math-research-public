# R46 supplement: the actual high density Volterra block in fixed ray labels

**Proved for the same complete old strict operator and whole real parameter
box.** The true principal transport can be removed exactly before estimating
its high-frequency ordinary-source correction. In each of the two separate
actual characteristic labels, retain the fixed projection
$P_H=1_{\{|n|\ge N\}}$. The complete high-to-high Volterra kernel has

$$
\int\|K_{HH}(r)\|_{L^2\to L^2}\,dr
\le {C_r Q_\kappa\over4N},\quad
C_r<14.983653,\quad Q_\kappa<113197.898280 .              \tag{H.1}
$$

At $N=2^{20}$ this is less than $0.405$, and the full two-direction high
Volterra resolvent is less than $1.498383$ at base order. The high space
contains every frequency $|n|\ge N$; there is no finite high truncation.

The **entire low-label histories and the two independent means remain
external inputs** to this high equation. Its finite spatial head and its
time evolution have not been solved here. Thus this result is neither a
complete high feedback inverse nor a new returned strong remainder. It
is a quantitatively usable interior high block with exact low/high and
source interfaces.

## 1. Exact variables and the two actual flows

Use the full R46 operator and physical momentum

$$
Pu=\partial_r(au_r+bu_\theta)
    +\partial_\theta(bu_r+cu_\theta)+du=f,\qquad
p=au_r+bu_\theta.
$$

Let $\mu=\sqrt{b^2-ac}$, $m=\mu^{-1/2}$,
$v=b/a$, $\nu=\mu/a$, and keep the full original shear $T$.
The already proved exact density equations use

$$
w=\sqrt\mu\,u,\quad
\zeta={p+Tu\over\sqrt\mu},\quad
y_\sigma={w_\theta+\sigma\zeta\over2},\quad
\kappa={\mathcal F\over\mu}.
$$

They are

$$
(y_\sigma)_r+
\partial_\theta[(v-\sigma\nu)y_\sigma]
={\sigma\over2}(mf-\kappa w),\qquad
w_r=\nu\zeta-vw_\theta .                                \tag{H.2}
$$

The potential is the complete
$\mathcal F=\mu^{1/2}P(\mu^{-1/2})$, including the original $d$.
In particular the native field named kappa in the earlier geometry file
means $-K_{\rm target}$ and is **not** the coupling $\kappa$ in (H.2).
The consumer reconstructs the latter bound explicitly as
$M_{\mathcal F}/\mu_-$ on every actual leaf.

Write $x=4\theta$ and regard each physical function as the function
$f(r,x/4)$. We keep its original scalar-density value and physical
$dr$; we do not redefine the divergence density when changing this
notation. The original normalized circle $L^2$ measure agrees with the
normalized $x$ measure.

Let $H_\sigma(r,\eta)$ be the exact normalized flow from the common left
strict cut $r_0=-r_c$:

$$
(H_\sigma)_r
=4(v-\sigma\nu)(r,H_\sigma/4),\qquad H_\sigma(r_0,\eta)=\eta ,
$$

and put $S_\sigma=H_\sigma^{-1}$.
Use the real natural lifts and the true density pullback

$$
X_\sigma=H_\sigma'(y_\sigma\circ H_\sigma),\qquad
\mathcal D_{H_\sigma}=M_{H_\sigma'}C_{H_\sigma}
=(C_{S_\sigma})^* .                                    \tag{H.3}
$$

The prime here is the label derivative. From (H.2),

$$
(X_\sigma)_r={\sigma\over2}\mathcal D_{H_\sigma}
                  (mf-\kappa w).                       \tag{H.4}
$$

This eliminates principal transport exactly. Neither a frozen ray
nor an averaged density appears.

The complete actual relative-flow certificates give, for both branches,
all strict times and every original parameter value,
$C_r^{-1}\le H_\sigma',S_\sigma'\le C_r$.
Their separately paid complex derivative bound is $C_c<36.730914$ on
normalized width $X=2.7952875\,10^{-5}$.
The complex width and $C_c$ are not replaced by the real bound $C_r$.

## 2. An exact primitive with both independent means

Set $D=-i\partial_x$ and let $D^{-1}$ be zero on the mean.
Density change of variables preserves the mean:
$\langle y_\sigma\rangle=\langle X_\sigma\rangle$.
The compatibility $w_\theta=y_++y_-$ gives

$$
\langle X_+\rangle=\alpha,\qquad
\langle X_-\rangle=-\alpha,\qquad
\langle\zeta\rangle=2\alpha.                             \tag{H.5}
$$

For the nonzero components $X_\sigma^\circ=X_\sigma-\langle X_\sigma\rangle$,
the complete periodic primitive is

$$
\boxed{
w=c+{\alpha\over4}(S_+-S_-)
   -{i\over4}\sum_{\sigma=\pm}C_{S_\sigma}D^{-1}X_\sigma^\circ .
}                                                       \tag{H.6}
$$

The scalar $c$ is a genuine independent height integration constant.
At $r_0$, both labels are the identity and it is exactly $\langle w\rangle$.
At later times

$$
\langle w\rangle
=c+{\alpha\over4}\langle S_+-S_-\rangle
 -{i\over4}\sum_\sigma
       \langle C_{S_\sigma}D^{-1}X_\sigma^\circ\rangle .
$$

Thus no claim that $c$ remains the physical angular mean is made.
The full high-to-physical-mean terms in this display remain present.
Differentiating (H.6) in $x$ proves
$4w_x=y_++y_-$ exactly. The factors $1/4$ come from
$w_\theta=4w_x$.

Here are the complete equations for the two independent scalar means.
Write $W=mf-\kappa w$. Equation (H.4) gives

$$
\alpha'={1\over2}\langle W\rangle.                       \tag{H.7}
$$

Use the zero-mean angular primitive
$\partial_x^{-1}\Pi_{\ne0}=-iD^{-1}$.
The exact height row is

$$
c'=-{\alpha'\over4}\langle S_+-S_-\rangle
 -{1\over4}\sum_\sigma
  \left\langle C_{S_\sigma}\partial_x^{-1}
                \Pi_{\ne0}(X_\sigma)_r\right\rangle .    \tag{H.8}
$$

To verify it without differentiating an unproved trace, take the primitive
$\phi_\sigma=\langle X_\sigma\rangle x+
\partial_x^{-1}X_\sigma^\circ$.
The identity
$(S_\sigma)_r=-4(v-\sigma\nu)(S_\sigma)_x$
shows that differentiating $\sum C_{S_\sigma}\phi_\sigma/4$
accounts exactly for $\nu\zeta-vw_\theta$ in (H.2).
The remaining sum $\sum C_{S_\sigma}(\phi_\sigma)_r$ is constant in $x$,
since its angular derivative is
$\sum_\sigma\sigma W/2=0$.
Taking its mean gives (H.8). All quantities there are bounded angular
integrals, not point evaluations of an $L^2$ function.

The true inverse-label displacements are finite. The current complete
field bounds give

$$
\|S_\sigma-x\|_\infty<11.686474,\qquad
\|S_+-S_-\|_\infty<23.372948=:D_\Delta .                  \tag{H.9}
$$

This is obtained by integrating
$4(\|v\|_\infty+\|\nu\|_\infty)$ over the full strict interval.
It also bounds the inverse displacement, since $x=H_\sigma(\eta)$.
For later use (H.7)--(H.8) imply

$$
|\alpha'|\le\|W\|_2/2,\qquad
|c'|\le(C_r/4+D_\Delta/8)\|W\|_2.                        \tag{H.10}
$$

## 3. Fixed projections and the exact high/low interfaces

In each of the two **separate fixed labels**, let

$$
P_H=1_{\{|n|\ge N\}},\qquad
P_L=1_{\{0<|n|<N\}},\qquad
X_\sigma^\circ=X_{\sigma,L}+X_{\sigma,H}.
$$

The projections commute with $D^{-1}$ in that label. They do not commute
with a density pullback, a scalar pullback, a coefficient, or each other
after physical-coordinate identification.
Set

$$
w_L=c+{\alpha\over4}(S_+-S_-)
 -{i\over4}\sum_\tau C_{S_\tau}D^{-1}X_{\tau,L},
\qquad
w_H=-{i\over4}\sum_\tau C_{S_\tau}D^{-1}X_{\tau,H}.        \tag{H.11}
$$

The exact high equation is

$$
(X_{\sigma,H})_r
=\sum_\tau K_{\sigma\tau}(r)X_{\tau,H}+F_{\sigma,H},
$$

$$
\boxed{
K_{\sigma\tau}
={i\sigma\over8}P_H(C_{S_\sigma})^*
       M_\kappa C_{S_\tau}D^{-1}P_H ,
}                                                       \tag{H.12}
$$

$$
F_{\sigma,H}
={\sigma\over2}P_H(C_{S_\sigma})^*(mf-\kappa w_L).         \tag{H.13}
$$

Every projection is in its actual position. In particular the gain
$1/N$ is supplied by the **rightmost label primitive**, before the
scalar pullback. It is not a fictitious Eulerian high projection.

The nonzero head rows remain

$$
(X_{\sigma,L})_r
={\sigma\over2}P_L(C_{S_\sigma})^*
       [mf-\kappa(w_L+w_H)] .                           \tag{H.14}
$$

Equations (H.7)--(H.8), with the full $w=w_L+w_H$, retain the other
two low rows. Thus all high-to-low and low-to-high paths are explicit.
The theorem below solves (H.12) for any given complete low history
$(X_{+,L},X_{-,L},\alpha,c)$; it does not assert that this given history
solves (H.7), (H.8), and (H.14).

## 4. The complete base high Volterra estimate

Ordinary change of variables gives the exact base bounds

$$
\|C_{S_\sigma}\|_2,\ 
\|(C_{S_\sigma})^*\|_2\le\sqrt{C_r}.
$$

The row map
$(X_+,X_-)\mapsto\sum C_{S_\tau}D^{-1}P_HX_\tau$
has norm at most $\sqrt{2C_r}/N$.
The column map
$z\mapsto(\sigma(C_{S_\sigma})^*z)_\sigma$
has norm at most $\sqrt{2C_r}$.
With the factor $1/8$ in (H.12),

$$
\|K_{HH}(r)\|_2
\le{C_r\over4N}\sup_\theta|\kappa(r,\theta)|.             \tag{H.15}
$$

The entire 215-cell actual positive cover and its exact reflection give

$$
Q_\kappa
 =\sum_{\text{positive leaves }I}
       2|I|\,{M_{\mathcal F,I}\over\mu_{-,I}}
 <113197.898280 .                                        \tag{H.16}
$$

This includes the complete actual density, mean and ordinary potential.
It is not the tiny integral of $-K_{\rm target}$.

Picard's Volterra series is bounded by
$\sum_{j\ge0}(\int\|K\|)^j/j!$.
Hence for the same entire high-space operator,

$$
\|X_H\|_{L^\infty_rL^2}
\le e^{k_0}
\left(\|X_H(r_0)\|_2+\|F_H\|_{L^1_rL^2}\right),
\qquad k_0={C_rQ_\kappa\over4N}.                         \tag{H.17}
$$

The same proof in reversed time gives the exact backward high Cauchy and
source bound. Smallness of $k_0$ is not needed for existence of this
Volterra solution; its value below one at the selected high cutoff
is a useful quantitative fact.

## 5. Higher orders by a finite lower-order bootstrap

No differentiated principal transport remains in (H.12).
The rightmost true inverse derivative gains one order. This lets us
obtain higher regularity from the preceding level, instead of placing
a new high-order diagonal term into Gronwall's inequality.

Use $H_N^j$ with the same $N$ as the high cutoff.
For every relevant actual $H_\sigma$ or $S_\sigma$, take

$$
H_1=C_r,\qquad
H_l={(l-1)!\,C_c\over(X/2)^{l-1}},\quad 2\le l\le J+1 .
                                                               \tag{H.18}
$$

Let $B_{jk}$ be the full exponential partial Bell polynomials evaluated
at these positive derivative bounds.
The complete scalar comparison matrix is

$$
P_{jk}=N^{k-j}B_{jk}\quad(k\le j).
$$

For the density pullback,

$$
\partial_x^j[H'(f\circ H)]
 =\sum_{k=0}^jB_{j+1,k+1}(H',H'',\ldots)
                  (\partial_x^k f)\circ H .
$$

Divide the coefficient by the actual positive $H'$ before applying
its density $L^2$ Jacobian. The leading quotient is exactly $(H')^j$;
the lower quotients are at most $C_r B_{j+1,k+1}$.
Thus use the finite matrix

$$
\mathsf D_{jk}=
\begin{cases}
C_r^j,& k=j,\\
C_r N^{k-j}B_{j+1,k+1},& k<j .
\end{cases}                                              \tag{H.19}
$$

With $W_j=\operatorname{diag}_{0\le k\le j}\sqrt{\binom jk}$,
set

$$
p_j=\sqrt{C_r}\|W_jP^{[j]}W_j^{-1}\|_2,\qquad
d_j=\sqrt{C_r}\|W_j\mathsf D^{[j]}W_j^{-1}\|_2.           \tag{H.20}
$$

These are true scalar and density operator norms.
In particular $p_0=d_0=\sqrt{C_r}$ exactly; no extra Jacobian is inserted.
The matrix norms in the consumer are full directed Schur/Frobenius bounds.

Let $M_{j,N}(1,s_f)$ be the complete multiplier bound for a function
of analytic modulus one on normalized field width $s_f=1/160$.
The high primitive satisfies

$$
\|D^{-1}P_H:H_N^{j-1}\to H_N^j\|
 =\sup_{|n|\ge N}{J_N(n)\over|n|}
 \le{\sqrt2\over N}.                                    \tag{H.21}
$$

Combining the row and column maps of Section 4 at order $j$ gives

$$
\int\|K_{HH}(r):H_N^{j-1}\to H_N^j\|\,dr
\le k_j:={\sqrt2\,d_jp_jM_{j,N}(1,s_f)Q_\kappa\over4N},
\qquad j\ge1.                                           \tag{H.22}
$$

Define the complete finite recurrence

$$
G_0=e^{k_0},\qquad G_j=1+k_jG_{j-1}.                     \tag{H.23}
$$

The same mild equation now proves, inductively,

$$
\|X_H\|_{L^\infty H_N^j}
\le G_j\left(\|X_H(r_0)\|_{H_N^j}
                  +\|F_H\|_{L^1H_N^j}\right).           \tag{H.24}
$$

At level $j$ the integral term is bounded using level $j-1$; the
stronger input norm dominates its lower counterpart.
There is no further exponential. Smooth Fourier tests justify the
induction, and the original $L^2$ Volterra solution is recovered by
completion. Thus this is a bound on the full infinite operator.
The backward argument is identical.
Interpolation gives the corresponding noninteger finite orders.

The executed values include

| $N$ | $G_0$ | $G_1$ | $G_2$ |
|---:|---:|---:|---:|
| $4096$ | $9.107340\,10^{44}$ | $1.995702\,10^{52}$ | $7.113574\,10^{62}$ |
| $16384$ | $1.737193\,10^{11}$ | $2.312165\,10^{17}$ | $1.714677\,10^{26}$ |
| $65536$ | $645.597695$ | $53330835.236$ | $2.128210\,10^{15}$ |
| $1048576$ | $1.498383$ | $520.375872$ | $81436320.914$ |

The report also contains levels three and four, the exact matrices,
and the interpolated orders $1/2,5/6,4/3,3/2,2$.
In particular every stated higher-order factor is a saved finite number.

## 6. Complete ordinary source, head drive and feedback columns

For the original ordinary scalar source $f$,
(H.13) and (H.20) give

$$
\|F_H^{\,f}\|_{L^1H_N^j}
\le{d_j\over\sqrt2}M_{j,N}(m)\,
                         \|f\|_{L^1(dr;H_N^j)}.          \tag{H.25}
$$

The output high-state gain is this number times $G_j$.
The physical $dr$, unchanged scalar-density convention and actual
$m=\mu^{-1/2}$ are retained.
A divergence source, a weak load and an ordinary $f$ are not interchanged.

For the complete low-height history,

$$
\|X_H^{\,L}\|_{L^\infty H_N^j}
\le {G_jd_jM_{j,N}(1,s_f)Q_\kappa\over\sqrt2}
                              \|w_L\|_{L^\infty H_N^j}.  \tag{H.26}
$$

The low height in (H.11) has the actual bound

$$
\|w_L\|_{H_N^j}
\le |c|+{\Delta_j\over4}|\alpha|
               +{p_j\over2\sqrt2}\|X_L\|_{(H_N^j)^2},
$$

$$
\Delta_j^2=
D_\Delta^2+
\sum_{l=1}^j\binom jl N^{-2l}(2H_l)^2.                  \tag{H.27}
$$

This keeps all nonzero head modes and the two independent scalar rows.

The reverse high-to-head columns can also be paid directly.
Since
$\|w_H\|_2\le\sqrt{2C_r}\|X_H\|_2/(4N)$,
the complete integrated base bounds for the nonzero head, mean flux
and mean height rows are respectively

$$
{C_rQ_\kappa\over4N},\qquad
{Q_\kappa\sqrt{2C_r}\over8N},\qquad
(C_r/4+D_\Delta/8){Q_\kappa\sqrt{2C_r}\over4N}.           \tag{H.28}
$$

These are actual columns of (H.7), (H.8), and (H.14).
They are not set to zero, and a small high-to-high kernel alone
does not close their feedback through the low time problem.

## 7. Exact physical reconstruction and scope

After obtaining the high state and a low history, use (H.6) for $w$ and

$$
y_\sigma=(S_\sigma')\,X_\sigma\circ S_\sigma,\qquad
z=y_++y_-,\quad \zeta=y_+-y_-,
$$

$$
\boxed{u=mw,\qquad p=\sqrt\mu\,\zeta-Tu.}                 \tag{H.29}
$$

The full physical shear and original momentum direction are unchanged.
For the high contribution alone,

$$
\|w_H\|_{H_N^j}\le{p_j\over2\sqrt2\,N}\|X_H\|_{(H_N^j)^2},
\qquad
\|(z_H,\zeta_H)\|_{(H_N^j)^2}\le\sqrt2\,d_j\|X_H\| .
$$

The consumer saves the base physical $u,p$ bounds using the complete
actual moduli of $m,\sqrt\mu,T$.
The low contribution is (H.27), including its two means.
No assertion that physical high Fourier support equals label high
Fourier support is made.

The new proof and consumer close the actual interior high Volterra block
for prescribed complete low history, for all original parameters and all
high frequencies. Three subsequent responsibilities remain distinct:
the full returned high remainder after coupling through that head,
the finite head and mean time/port problem itself, and any positive
fixed angular-weight estimate needed for a nonlinear inverse.
Neither a root/Airy estimate nor a complete feedback inverse follows
from this interior statement alone.

## 8. Reproduction

The producer is scripts/fourfold_actual_label_high_density_volterra.py.
It reads the original 215 native cells, complete density identity and
whole-flow derivative report through the frozen requested-window
consumer. It recomputes no native geometry. All common object and
parameter hashes and the entire continuous cover are checked.

The report is
notes/2026-11-13-actual-fixed-label-high-density-Volterra.json.
It includes all integer/fractional levels, both complete means, every
source and head column and the exact reconstruction scope.

~~~bash
python3 scripts/fourfold_actual_label_high_density_volterra.py \
  --out notes/2026-11-13-actual-fixed-label-high-density-Volterra.json
~~~

The producer requires a fresh output path; displayed decimal bounds
are outward rounded from its complete Arb enclosures.
