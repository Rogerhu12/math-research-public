# R110. Constraint-preserving strict-core energy and complete weak-source budgets

Date: 2026-11-12.

## 110.1. Scope and exact operator

This result concerns the actual scalar operator used in R37, R88 and R107, at the same explicitly symmetrized affine family
$
p=p_5+\delta,\qquad
p_5=-7789843107295549/4611686018427387904,\qquad
|\delta|\le 10^{-9}.
$
All coefficients below are those of this actual operator. No radial background is substituted. Its physical angular variable is $\theta$, with period $\pi/2$ and Fourier frequencies $4k$.

Write $D=\partial_\theta$ and
$$
\mathcal P u
 =\partial_r(a u_r+bDu)+D(bu_r+cDu)+d u,
\qquad d=\tau+D\sigma.                                      \tag{110.1}
$$
On a **strict negative** radial interval $I=[r_-,r_+]$ assume
$$
\alpha=a^{-1}>0,\qquad v=b/a,\qquad
\gamma=bv-c=(b^2-ac)/a>0.                                 \tag{110.2}
$$
The existing finite quarter-core interval $[-1/4,1/4]$ contains positive collars. This theorem cannot be applied to that entire interval. Each strict interval must end before a turning root; the true root/Airy connections and positive caps remain separate operators.

The coefficient $d$ is not assumed positive. In particular, the option $\lambda=d$ is unavailable without an independent positive lower bound. The executable consumer uses either a prescribed positive constant $\lambda$, or the actual radial coefficient $\lambda=-K_0>0$ on a proved strict interval. It pays its full radial derivative.

This is an energy estimate for the complete physical PDE, constrained by $q=Du$. It does not replace the existing finite Galerkin propagation: multiplication by $\alpha$ is not the inverse of the finite projected matrix of $a$.

## 110.2. Weak sources and the exact shifted momentum

For the actual divergence-form load
$$
\mathcal P u=f_0+\partial_r f_r+D f_\theta,
$$
put
$$
q=Du,\qquad p=a u_r+bq-f_r.
$$
Then, in distributions,
$$
\begin{aligned}
u_r&=\alpha p-vq+\alpha f_r,\\
q_r&=D(\alpha p-vq)+D(\alpha f_r),\\
p_r&=-D(vp-\gamma q)-d u+
             f_0+D(f_\theta-vf_r).                       \tag{110.3}
\end{aligned}
$$
This identity does not differentiate $f_r$ in the radial variable. Piecewise radial sources, including their actual jumps, are allowed in the weak formulation.

For the saved even finite reference the exact residual convention is
$$
\begin{aligned}
R_r&=a u_{N,r}+bDu_N-p_N,\\
R_\theta&=P_H(bu_{N,r}+cDu_N+\sigma u_N),\\
R_0&=\sigma Du_N-\tau u_N-p_{N,r}
       -D P_N(bu_{N,r}+cDu_N+\sigma u_N).
\end{aligned}
$$
Thus
$$
\mathcal P u_N=-R_0+\partial_r R_r+D R_\theta,
\quad (f_0,f_r,f_\theta)=(-R_0,R_r,R_\theta),
\quad p=p_N.                                              \tag{110.4}
$$
The last equality is exact, including at adjacent radial reference segments. Correcting the reference to a homogeneous solution negates the entire load; the norm bounds below are unchanged. No unrecorded radial derivative of $R_r$ and no artificial momentum jump is introduced.

The low mean is retained. A zero angular frequency has weight one in every Sobolev norm below. The regular cap coordinate remains a separate sixth input of the retained even block; its direct core source column is zero, not deleted.

## 110.3. Exact base energy

Let $\lambda(r,\theta)>0$ be real and define, with normalized angular measure,
$$
E=\int_{\mathbb T_{\pi/2}}
       \lambda|u|^2+\gamma|q|^2+\alpha|p|^2.
$$
For the homogeneous equation, direct differentiation and one angular integration by parts give
$$
\begin{aligned}
E'=\int&
 [\lambda_r+v\lambda_\theta+\lambda v_\theta]|u|^2\\
 &+[\gamma_r+v\gamma_\theta-\gamma v_\theta]|q|^2\\
 &+[\alpha_r+v\alpha_\theta-\alpha v_\theta]|p|^2\\
 &+2\alpha(\lambda-d)\operatorname{Re}(\overline u p).
                                                               \tag{110.5}
\end{aligned}
$$
Here the mixed $p,q$ terms cancel because
$$
\gamma\alpha_\theta+\alpha\gamma_\theta-(\alpha\gamma)_\theta=0.
$$
The $u,q$ term is integrated using the actual constraint $q=Du$:
$$
-2\operatorname{Re}\int\lambda v\overline u\,Du
   =\int(\lambda v)_\theta |u|^2.
$$
These two cancellations are responsible for the absence of a highest angular frequency in (110.5).

Define
$$
\begin{aligned}
r_u&=(\lambda_r+v\lambda_\theta)/\lambda+v_\theta,\\
r_q&=(\gamma_r+v\gamma_\theta)/\gamma-v_\theta,\\
r_p&=(\alpha_r+v\alpha_\theta)/\alpha-v_\theta,\\
c_*&=(\lambda-d)\sqrt{\alpha/\lambda}.
\end{aligned}
$$
The normalized energy matrix is the real symmetric matrix
$$
\mathcal H=
\begin{pmatrix}
r_u&0&c_*\\
0&r_q&0\\
c_*&0&r_p
\end{pmatrix}.                                               \tag{110.6}
$$
Any uniform upper bounds
$$
g_+\ge\sup_{r,\theta,\delta}\lambda_{\max}(\mathcal H),
\qquad
g_-\ge\sup_{r,\theta,\delta}\lambda_{\max}(-\mathcal H)
                                                               \tag{110.7}
$$
give forward and backward base energy rates.

For the radial weight used by the program, $\lambda_\theta=0$. The two-by-two eigenvalue is evaluated by
$$
\frac{r_u+r_p+
 \sqrt{(r_u-r_p)^2+4c_*^2}}2,
$$
and the trace is formed as
$$
r_u+r_p=\lambda_r/\lambda+
              (\alpha_r+v\alpha_\theta)/\alpha.              \tag{110.8}
$$
The two $v_\theta$ terms cancel before interval evaluation. Bounds for the difference and cross term are squared with their complete absolute upper bounds. The backward rate uses $-(r_u+r_p)$ and the same discriminant; $r_q$ is separately retained.

No absolute-value estimate of $d$ is added as an independent exponential loss: its actual correlation with $\lambda$ is retained in $c_*$. If $d$ itself were positive and chosen as $\lambda$, that cross term would vanish, but this is not an assumption made here.

## 110.4. A physical half-derivative commutator without a cutoff

For $0\le s\le1$ define
$$
w_s(k)=\max(1,|4k|)^s,\qquad
\Lambda_s e^{4ik\theta}=w_s(k)e^{4ik\theta}.
$$
The coefficient multiplier norm used here is
$$
M_s(f)=\sum_{m\in\mathbb Z}(1+|4m|)^s|\widehat f_m|.
$$
It obeys
$$
\|fz\|_{H^s}\le M_s(f)\|z\|_{H^s}.                           \tag{110.9}
$$
For a frequency difference $m=k-l$, the two exact scalar inequalities
$$
\begin{aligned}
\frac{|w_s(k)-w_s(l)|}{w_s(l)}
   &\le (1+|4m|)^s-1,\\
\frac{|4k|\,|w_s(k)-w_s(l)|}{w_s(l)}
   &\le |4m|(1+|4m|)^s                                    \tag{110.10}
\end{aligned}
$$
yield, by the $\ell^1*\ell^2$ convolution inequality,
$$
\begin{aligned}
\|[\Lambda_s,f]z\|_2&\le A_s(f)\|z\|_{H^s},\\
\|D[\Lambda_s,f]z\|_2&\le B_s(f)\|z\|_{H^s},\\
A_s(f)&=\sum_m((1+|4m|)^s-1)|\widehat f_m|,\\
B_s(f)&=\sum_m|4m|(1+|4m|)^s|\widehat f_m|.                 \tag{110.11}
\end{aligned}
$$

For completeness, put $L_k=\max(1,|4k|)$. If $L_k\ge L_l$, set $R=L_k/L_l$. Then $R\le1+|4m|$ and, for $0\le s\le1$,
$$
R(R^s-1)\le(R-1)R^s.
$$
Multiplication by $L_l$ proves the second inequality. If $L_k<L_l$, use $1-R^s\le1-R$ for $R=L_k/L_l\in(0,1)$. The first inequality follows from the same cases. This proof includes the zero mode and every physical frequency; no finite $N$ is used.

Apply $\Lambda_s$ to (110.3). The commutator source is
$$
\begin{aligned}
h_u&=[\Lambda_s,\alpha]p-[\Lambda_s,v]q,\\
h_q&=D h_u,\\
h_p&=-D([\Lambda_s,v]p-[\Lambda_s,\gamma]q)
                         -[\Lambda_s,d]u.                 \tag{110.12}
\end{aligned}
$$
The commuted state still satisfies $\Lambda_s q=D\Lambda_s u$, so (110.5) remains applicable to its principal part.

Let positive constants $\lambda_\pm,\gamma_\pm,\alpha_\pm$ bound the corresponding exact coefficients throughout the same strict interval and parameter box. Put
$$
\begin{aligned}
c_u&=A_s(\alpha)/\sqrt{\alpha_-}
                      +A_s(v)/\sqrt{\gamma_-},\\
c_q&=B_s(\alpha)/\sqrt{\alpha_-}
                      +B_s(v)/\sqrt{\gamma_-},\\
c_p&=B_s(v)/\sqrt{\alpha_-}
       +B_s(\gamma)/\sqrt{\gamma_-}+A_s(d)/\sqrt{\lambda_-},\\
C_s&=\sqrt{\lambda_+c_u^2+\gamma_+c_q^2+\alpha_+c_p^2}.
                                                               \tag{110.13}
\end{aligned}
$$
All Fourier norms in this formula are uniform in $r,\delta$. Weighted Cauchy-Schwarz in (110.12) bounds the commutator forcing by $C_s\sqrt{E_s}$, where
$$
E_s=\int\lambda|\Lambda_su|^2+
            \gamma|\Lambda_sq|^2+\alpha|\Lambda_sp|^2.
$$
Consequently the homogeneous square-root rates are
$$
\beta_+=g_+/2+C_s,\qquad \beta_-=g_-/2+C_s.                 \tag{110.14}
$$

The implemented case is $s=1/2$. It uses
$$
A_{1/2}(d)\le A_{1/2}(\tau)
 +\sum_m |4m|(\sqrt{1+|4m|}-1)|\widehat\sigma_m|.            \tag{110.15}
$$
This avoids replacing a complete coefficient norm by a pointwise bound.

## 110.5. Exact strong-source wiring and Duhamel constants

Use the physical source product space
$$
\mathcal S
 =H^{1/2}\oplus H^{3/2}\oplus H^{3/2}
\quad\hbox{for }(f_0,f_r,f_\theta).
$$
The commuted inhomogeneous source from (110.3) has energy norm at most
$$
\mathcal L
\begin{pmatrix}
\|f_0\|_{H^{1/2}}\\
\|f_r\|_{H^{3/2}}\\
\|f_\theta\|_{H^{3/2}}
\end{pmatrix}
\quad\hbox{in Euclidean norm},\qquad
\mathcal L=
\begin{pmatrix}
0&\sqrt{\lambda_+}M_{1/2}(\alpha)&0\\
0&\sqrt{\gamma_+}M_{3/2}(\alpha)&0\\
\sqrt{\alpha_+}&\sqrt{\alpha_+}M_{3/2}(v)&\sqrt{\alpha_+}
\end{pmatrix}.                                               \tag{110.16}
$$
Indeed $\|Dh\|_{H^{1/2}}\le\|h\|_{H^{3/2}}$ with the stipulated physical weights. Products are controlled by (110.9). Let $L_*=\|\mathcal L\|_2$ with an outward upper bound.

For either direction, let $\beta$ be the corresponding value in (110.14) and $\ell=r_+-r_-$. Then
$$
\sqrt{E_s(r_+)}
 \le e^{\beta\ell}\sqrt{E_s(r_-)}
   +L_*\int_{r_-}^{r_+}e^{\beta(r_+-r)}
              \|(f_0,f_r,f_\theta)(r)\|_{\mathcal S}\,dr.
                                                               \tag{110.17}
$$
For zero incoming state this implies
$$
\sqrt{E_s(r_+)}
 \le L_*\sqrt{J(\beta,\ell)}
       \|(f_0,f_r,f_\theta)\|_{L^2(I;\mathcal S)},\qquad
J(\beta,\ell)=
\begin{cases}
\ell\,\dfrac{e^{2\beta\ell}-1}{2\beta\ell},&\beta\ne0,\\
\ell,&\beta=0.
\end{cases}                                                   \tag{110.18}
$$
The formula is valid for negative $\beta$ as well. If a ball for $2\beta\ell$ contains zero, the executable fallback $\ell e^{\max(0,2\beta\ell)}$ is a proved upper bound, not a division by a ball containing zero.

The energy controls the actual strong Cauchy state:
$$
E_{1/2}\ge
 \min(\lambda_-,\gamma_-)\|u\|_{H^{3/2}}^2
                   +\alpha_-\|p\|_{H^{1/2}}^2.             \tag{110.19}
$$
The zero mode is supplied by $\lambda_-$, while each nonzero physical frequency is supplied by $\gamma_-|4k|^2$. The reverse bound with coefficients $\lambda_++\gamma_+$ and $\alpha_+$ is immediate. This conversion is not the separately needed canonical/shear/label frame conversion of R107.

## 110.6. Adjacent spans and the complete five-column source Gram

Suppose adjacent strict intervals use the same exact energy weight definition. The actual $\alpha,\gamma,\lambda$ are continuous at their common spline interfaces. Hence the physical energy is the same limit from both sides. Joining local estimates costs no additional coefficient-equivalence factor at every small interval.

For interval $I_j$ write $\beta_j,L_j,\ell_j$ for its actual forward inputs. Its load-to-final-endpoint coefficient is
$$
c_j=\exp\!\left(\sum_{k>j}\beta_k\ell_k\right)
            L_j\sqrt{J(\beta_j,\ell_j)}.                    \tag{110.20}
$$
Let $G_j$ be any rigorous positive semidefinite five-input majorant with
$$
\int_{I_j}\!\!
 \big(\|R_0 z\|_{H^{1/2}}^2+
      \|R_r z\|_{H^{3/2}}^2+
      \|R_\theta z\|_{H^{3/2}}^2\big)\,dr
 \le z^*G_jz
$$
for every complex five-vector $z$. Each $G_j$ must include the complete selected-coefficient and infinite Fourier/Taylor errors, not only the finite rectangular polynomial.

For arbitrary positive real numbers $a_j$,
$$
\|\text{final forced state}(z)\|_{E_s}^2
 \le \left(\sum_j a_j\right)
     z^*\!\left(\sum_j\frac{c_j^2}{a_j}G_j\right)z.           \tag{110.21}
$$
This is weighted Cauchy-Schwarz applied to $\sum_jc_j\sqrt{z^*G_jz}$. Thus one may retain the full finite-column correlations instead of substituting a scalar sum of local transfer errors. A usable scalar choice is $a_j=c_j\sqrt{\|G_j\|}$; zero contributions can be omitted only when rigorously zero.

Backward estimates use the reverse interval order and $\beta_-$. For the explicit radial symmetry, $\alpha,\gamma,d,\lambda$ are even and $v$ is odd. The energy matrix at $-r$ is unitarily conjugate to the negative matrix at $r$: on the $(u,p)$ block use $\operatorname{diag}(1,-1)$. Consequently positive-half backward rates pay negative-half forward rates. The coefficient and source symmetries, including the momentum sign, must still be applied exactly.

Equation (110.21) provides a strong-source interface to the high problem. It does not declare that the full high inverse is bounded, does not invert a potentially singular infinite core DN, and does not replace the Airy or cap contributions in the joint Schur residual.

## 110.7. Actual nine-field producer and complete radial error

The new source is `scripts/fourfold_phase_core_energy_fields.py`. It extends the same whole-real-parameter, center-first radial Taylor geometry as the already saved seven-field producer. Its exact fields are
$$
a,b,c,\tau,\sigma,\alpha,v,\gamma,\kappa,\qquad \kappa=-K_0.
$$
Writing
$$
X=F_r,\quad Y=F_\theta,\quad C=Y\times X,\quad
R^2=F\cdot F,\quad S=C\cdot F,\quad
m=C\cdot F_{r\theta},\quad n=C\cdot F_{\theta\theta},\quad
G=C\cdot C,
$$
the extra fields use the exact algebra
$$
\alpha=-\frac{S^2}{nR^2},\qquad
v=-\frac mn,\qquad
\gamma=\frac{K_0G^2R^2}{nS^2}.                              \tag{110.22}
$$
The inherited actual geometry proves nonvanishing of $n,R^2,S$ on the full complex radial disk times angular strip. Its bound for $n$ uses the true moving-frame factorization. A rectangular raw enclosure wrapping zero is not treated as a nonvanishing proof. The native primitive's full infinite tails and exact real-parameter interval are retained.

On the normalized radial disk $|u|\le R>1$, let the complete coefficient modulus be $M$ and the normalized angular strip width be $S_\theta$. The source saves every selected exact dyadic coefficient in the finite rectangle
$$
\sum_{i=0}^{m-1}\sum_{|k|\le K} g_{ik}u^ie^{4ik\theta},
$$
with complete node, angular alias, time alias and selected-midpoint fees. Its existing full complement is separated into high angular modes and retained angular modes with $i\ge m$.

For physical $r=c+hu$ it additionally pays:

1. Each selected coefficient fee is multiplied by $i/h$.
2. The complete high-angular error at derivative order $j$ is divided by $h(R-1)$, using the radial Cauchy estimate on the true full disk for every high Fourier coefficient.
3. The retained-angle high-time derivative is bounded by
$$
\frac{M}{h}R^{-m}
 \left(\frac{m}{1-R^{-1}}+
       \frac{R^{-1}}{(1-R^{-1})^2}\right)
 \sum_{|k|\le K}|4k|^j e^{-|k|S_\theta},                    \tag{110.23}
$$
where the $k=0,j=0$ term is one and the $k=0,j>0$ term is zero.

This is the derivative of the entire infinite time tail. It does not differentiate only the finite saved polynomial. The angularly constant identity of $\kappa$ is enforced exactly, with no invented nonzero angular tail.

For either the value or radial derivative, let $E_0,E_1,E_2$ be its complete absolute Fourier error moments. The multiplier and commutator error budgets are
$$
\begin{aligned}
\Delta M_{1/2}&\le E_0+\sqrt{E_0E_1},\\
\Delta M_{3/2}&\le\sqrt{(E_0+E_1)(E_0+2E_1+E_2)},\\
\Delta A_{1/2}&\le\min(E_1/2,\sqrt{E_0E_1}),\\
\Delta B_{1/2}&\le\sqrt{E_1(E_1+E_2)},\\
\Delta A_{1/2}(D\cdot)&\le
                    \min(E_2/2,\sqrt{E_1E_2}).
                                                               \tag{110.24}
\end{aligned}
$$
These follow from $\sqrt{1+t}-1\le\min(t/2,\sqrt t)$ and Cauchy-Schwarz with respect to the positive error masses. They apply to the complete error, not only a finite spectral tail.

## 110.8. Continuous executable energy gate

The consumer is `scripts/fourfold_phase_strict_core_energy.py`. It requires a completed nine-field report, its exact arrays and matching actual source/dependency hashes. It may restrict to a closed radial subinterval of the already proved leaf; it cannot extend beyond that leaf or change its actual polynomial germ.

At every angular grid point it evaluates the **whole radial interval** by ball Horner, both for the value and physical radial derivative, then adds their complete errors. Exact native DFT evaluation is permitted only with an even number of nodes exceeding $2K$. The finite Fourier coefficient reality and the structural angular zero of $\kappa$ are checked.

With angular mesh halfwidth $h_\theta=\pi/(4N)$, the continuous angular cell bounds are
$$
\begin{aligned}
f(\theta_j+t)&\in f(\theta_j)+t f_\theta(\theta_j)
                      +[-h_\theta^2M_{\theta\theta}/2,
                          h_\theta^2M_{\theta\theta}/2],\\
f_\theta(\theta_j+t)&\in f_\theta(\theta_j)
                       +[-h_\theta M_{\theta\theta},
                           h_\theta M_{\theta\theta}],\\
f_r(\theta_j+t)&\in f_r(\theta_j)+t f_{r\theta}(\theta_j)
                      +[-h_\theta^2M_{r\theta\theta}/2,
                          h_\theta^2M_{r\theta\theta}/2],
\end{aligned}                                                 \tag{110.25}
$$
for every $|t|\le h_\theta$. The two second-derivative moduli include the complete infinite-field error. These closed cells cover the full physical angular circle.

Only after these continuous enclosures does the program require strict positivity of $\alpha,\gamma,\kappa$, and compute (110.6)--(110.18). A failed positivity or denominator test is saved as a failed report, never skipped as if covered.

The output records the exact family/germ/real interval, all actual Fourier multiplier and commutator constants, full potential range, positive lower bounds, forward/backward energy rates, and Duhamel constants. No pointwise inverse lower bound is substituted for a Wiener multiplier norm.

## 110.9. Status and replay

The proof above is complete as a coefficient-input theorem. The two new sources were written while the native executor was unavailable. They have **not** produced an actual continuous energy certificate yet. No numerical full-core propagation, whole-source inverse or completed feedback bound is asserted by this result.

A native replay, from the topic directory and using one of the saved completed whole-family strict-core leaf reports, is:

```sh
python scripts/fourfold_phase_core_energy_fields.py \
  --leaf-report "$STRICT_LEAF" \
  --angles 2048 --keep 768 --time-nodes 64 --time-terms 40 \
  --outer-radius 3 --sample-radius 5/4 --normalized-strip 1/16 \
  --bits 192 --out notes/strict_core_energy_fields.json

python scripts/fourfold_phase_strict_core_energy.py \
  --field-report notes/strict_core_energy_fields.json \
  --angles 4096 --bits 256 \
  --out notes/strict_core_energy_gate.json
```

Here `STRICT_LEAF` is an exact path to one completed leaf under `data/core_uniform_flow_ci/43307149760/`. A root-containing or positive-collar leaf must not be relabeled strict. It can instead be restricted by the consumer's `--left` and `--right` only when that closed subinterval is actually proved positive in all required quantities. The optional `--lambda-constant` selects an exact positive rational; joining intervals requires the same weight definition.

The already observed native 175-leaf finite product, six-dimensional retained inverse and whole-family quarter-cut strong multiplier Grams remain separate results. Their complete reports and binary arrays must be recovered or rerun after the executor outage; the small observed receipt is not replaced by this energy proof.
