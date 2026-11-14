# R133 supplement: the current moving body's true physical complex germ

2026-11-13, visible-exact / phase_inverse. **Proved and actually computed;
10 gates passed.** This theorem supplies the actual physical-angle
coefficient input for turning and strict operators at the new complete
amplitude-$0.765$, M32, full-$25/8$ moving-angle centre. It does not
transfer the old amplitude-$3/4$ centre's numerical coefficient bounds.

The new candidate manifest SHA is

`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.

The loader verifies every complete radial shard, its SHA, byte count,
interval order, exact double endpoint equality, and full state shape.
The exact centre parameters are

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \nu=-\frac{2572625729470897}{72057594037927936}.                       \tag{M.1}
$$

The source is reusable for a different complete moving candidate, but
it checks that candidate's actual piece and recomputes every domain,
inverse-angle, and coefficient gate. The numerical conclusion here is
only for the named manifest.

## 1. Joint domain and complete new centre

The actual intrinsic root enclosure remains

$$r_*(\eta)\in[0.2383968742994,0.2383968743003]                         \tag{M.2}$$

for the whole original $|\eta|\le10^{-9}$ interval. Reusing this
intrinsic fact is legitimate: the compact $\nu$ change is identically
zero after $.18$, including the entire present germ. The new $\nu$
lies in the previously certified intrinsic family
$[-1/25,-1/40]$. No old nonradial centre or old angle map is reused.

The new candidate's actual root piece is 2549, with exact endpoints

$$
 \left[\frac{2147184947341121}{9007199254740992},
       \frac{4295308144604611}{18014398509481984}\right].              \tag{M.3}
$$

It and the original scalar germ contain the full joint rectangle

$$
 \operatorname{Re}r\in[r_*^--10^{-5},r_*^++10^{-5}],\qquad
 |\operatorname{Im}r|\le10^{-5},\qquad
 |\operatorname{Im}\phi|\le1/1024 .                                  \tag{M.4}
$$

In particular (M.4) contains the complex disk of radius $10^{-5}$
about every actual parameter root. No PPoly or scalar seam is crossed.
The complete stored polynomial is interpreted as its exact dyadic
coefficients, rather than as an approximate evaluator whose radial
errors are assumed absent.

The moving fields are

$$
 u(r,\phi)=\alpha\sum_{j=1}^{32}U_j(r)\sin(4j\phi),\qquad
 v(r,\phi)=s(r)+\alpha\sum_{j=0}^{32}V_j(r)\cos(4j\phi),\qquad
 m(r)=s(r)+\alpha V_0(r).                                \tag{M.5}
$$

$m$ is the **moving-angle mean** of $v$. It is not declared to be the
physical-angle mean. The exact physical angle is

$$
 \theta=\phi+F(r,\phi),\qquad
 F=\frac1m\sum_{j=1}^{32}\frac{\alpha V_j(r)}{4j}\sin(4j\phi),
 \qquad \theta_\phi=v/m .                               \tag{M.6}
$$

The full finite series in (M.5)–(M.6) is evaluated on (M.4), including
its even mean. Its coefficients are not relabelled as physical Fourier
coefficients. The true physical functions below are the complete
implicit pullbacks by the inverse of (M.6); their generally infinite
physical Fourier tails remain inside the proved analytic bounds.

## 2. Intrinsic analytic input and radial derivative of the angle

The native calculation uses the same complete original primitive and
its explicit omitted remainder. For complex $r$, the energy is formed
by the **bilinear zero convolution** of the primitive first
derivatives. It is not formed using complex conjugation or a
`real_part` operation. The complete energy product error bounds are
saved, including all three ambient components. The analytic expressions
for $a,E,K,K',\gamma,\beta,s$ use their separated right-half-plane
denominators.

In particular $s=-a\sqrt{E/(E-a'^2)}$. Set $G=E-a'^2$; then the full
radial derivative used in the angle map is exactly

$$
 s'=s\left[\beta+\frac12\left(\frac{E'}E-\frac{E'-2a'a''}G\right)\right],
 \qquad m'=s'+\alpha V_0'.                              \tag{M.7}
$$

The finite radial coefficients in (M.5) are differentiated as their
complete saved cubic polynomials. Thus the full mean derivative in
(M.7) is not omitted.

Let $V_*^{\ne0}$ be the complete weighted Wiener sum of the nonmean
$v$ modes at strip $1/1024$, and let $m_->0$ bound $-\operatorname{Re}m$.
The following upper bounds are evaluated on the complete complex
radial rectangle:

$$
 \kappa=V_*^{\ne0}/m_-,\qquad
 I_0=\sum_{j\ge1}\frac{|\alpha V_j|}{4j},\qquad
 I_1=\sum_{j\ge1}\frac{|\alpha V_j'|}{4j},\qquad
 F_r^*=I_1/m_-+I_0|m'|/m_-^2 .                           \tag{M.8}
$$

$\kappa$ uses the complete complex angular strip. $F_r^*$ in (M.8)
is required only at real $\phi$; its radial argument is still complex.
These give

$$
\begin{gathered}
 m_->1.1197077044,\qquad |m|<1.119807069,\qquad
 -\operatorname{Re}v>0.4488872879,\\
 \kappa<0.599103154,\qquad F_r^*<0.696214995 .             \tag{M.9}
\end{gathered}
$$

The last gap is a complete complex product-domain inequality, not a
minimum over sampled real angles.

## 3. The actual physical-angle inverse exists jointly in complex $r$

Put $\sigma_\phi=1/1024$, $\sigma_\theta=1/8192$ and $R=10^{-5}$.
The native gate is

$$
 (1-\kappa)\sigma_\phi-RF_r^*-\sigma_\theta
       >0.0002624683644.                                 \tag{M.10}
$$

Here is the complete inverse argument. For fixed complex $r$ in (M.4)
and fixed $|\operatorname{Im}\theta|\le\sigma_\theta$, consider

$$\phi\longmapsto\theta-F(r,\phi).                       \tag{M.11}$$

On the closed horizontal strip $|\operatorname{Im}\phi|\le\sigma_\phi$,
$|F_\phi|\le\kappa<1$. Straight line integration inside this convex
strip proves that (M.11) is a global contraction in the usual complex
distance. For real $r$ and real $\phi$, $F$ is real. For complex $r$,
vertical integration in $r$ and (M.8) give

$$|\operatorname{Im}F(r,\phi)|\le RF_r^*+\kappa|\operatorname{Im}\phi|.
                                                                    \tag{M.12}$$

Therefore (M.10) proves that (M.11) maps the whole closed strip strictly
into itself. The strip is complete; its unbounded real direction is
irrelevant to the contraction theorem. Iteration produces the unique
fixed point $\phi=\Phi(r,\theta)$ for every point of the entire joint
product. Uniform convergence on interior compact sets and the analytic
implicit equation show that $\Phi$ is jointly holomorphic. Uniqueness
also gives the exact circle lift
$\Phi(r,\theta+\pi/2)=\Phi(r,\theta)+\pi/2$.

This proves both actual global injectivity on the relevant strip and
surjectivity onto the stated physical strip. It is not a merely formal
inverse series. Its complete first derivatives satisfy

$$
 |\Phi_\theta|\le(1-\kappa)^{-1}<2.494408,\qquad
 |\Phi_r|\le F_r^*/(1-\kappa)<1.736644 .                  \tag{M.13}
$$

The radial term in (M.13) is part of the source chain rule. A change
from the moving angle to the physical angle cannot discard it.

## 4. Full physical derivatives before forming the local Jacobi matrix

The actual physical centre is
$u^{\rm phys}(r,\theta)=u(r,\Phi(r,\theta))$,
$v^{\rm phys}(r,\theta)=v(r,\Phi(r,\theta))$.
It is holomorphic on the true physical product just proved. Its exact
angular differential operator is

$$\partial_\theta=(m/v)\partial_\phi.                    \tag{M.14}$$

For example

$$
\begin{aligned}
 u_\theta&=mu_\phi/v,&
 u_{\theta\theta}&=m^2(u_{\phi\phi}/v^2-u_\phi v_\phi/v^3),\\
 v_\theta&=mv_\phi/v,&
 v_{\theta\theta}&=m^2(v_{\phi\phi}/v^2-v_\phi^2/v^3).
\end{aligned}                                                       \tag{M.15}
$$

The third and fourth derivatives are obtained by applying (M.14)
again to these complete expressions. The source records all of them,
including every differentiated denominator, using the full gap (M.9).
Its `physical_*_derivative_sup` fields are **supremum derivative
bounds**, not claimed physical Wiener sums. The separate
`moving_*_derivative_Astrip` fields retain the actual finite moving
Wiener sums. These two permissions are not conflated.

The full original local physical Jacobi equation at this centre is,
after $R=\operatorname{diag}(-1,1)$,

$$
 y_r=(dI+aJ(K))y_\theta+Ly+Rf,\quad
 d=\gamma u^{\rm phys},\ a=-\gamma v^{\rm phys},\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.               \tag{M.16}
$$

The complete unreflected lower coupling and diagonal coefficients are

$$
\begin{aligned}
 g&=\gamma v_\theta-2\beta uv,\quad L_{12}=Kg,\quad L_{21}=g,\\
 L_{11}&=\gamma u_\theta-\beta(1+3u^2+Kv^2),\\
 L_{22}&=-\gamma u_\theta+\beta(1-u^2-3Kv^2).
\end{aligned}                                                       \tag{M.17}
$$

Reflection changes the two off-diagonal signs together, preserving
$L_{12}=K L_{21}$. All quantities in (M.17) are evaluated *after* the
physical inverse angle and its chain rule have been paid.

The true analytic simple-root quotient
$k(r)=K(r)/(r-r_*)=\int_0^1K'(r_*+t(r-r_*))dt$ lies in the same convex
complex $K'$ enclosure. The selected branch $p=a\sqrt k$ is therefore
actual and separated. Representative complete bounds are

| Physical coefficient on the joint product | Bound |
|---|---:|
| $\operatorname{Re}K'$ | $>59.74380437$ |
| $\operatorname{Re}a$ | $>0.5025436590$ |
| $\operatorname{Re}p$ | $>3.8318473892$ |
| $|d|,|a|$ | $<0.705336,\ 2.004892$ |
| $|d_\theta|,|a_\theta|$ | $<7.302797,\ 7.826659$ |
| $|p|,|p_\theta|$ | $<15.636321,\ 61.040795$ |
| $|g|$ | $<8.301670$ |
| $|L_{11}|,|L_{22}|$ | $<7.765019,\ 7.599912$ |
| Complete $\|L\|$ bound | $<23.678926$ |

The table and all higher physical angular derivative bounds retain the
entire affine parameter interval and every finite centre mode. The
physical inverse angle accounts for the infinite Fourier expansion
created by composition; there is no physical Fourier cutoff.

## 5. What this input authorizes

The theorem supplies the true new-centre physical coefficient germ
needed by an actual fold construction, including positive branches,
full angular derivative bounds, true local source coordinates, and
both means. The mathematical fold/energy formulas already proved for
general analytic physical coefficients can be instantiated with these
new numbers after their actual numerical gates are checked.

The moving-coordinate linearization also contains a nonlocal primitive
and a mean column. This theorem has not discarded those terms or
treated them as a local multiplication potential. Instead (M.16) is
the **original physical** operator at the reconstructed physical
centre, whose local formula is exact even at an approximate centre.
Connecting it to a moving variation operator still requires the
separate residual-sensitive variation bridge. The source $f$ in
(M.16) is the complete original ordinary two-component source,
including any fully supplied parameter columns.

No nonlinear existence, full turning inverse, positive regular graph,
or whole-body feedback inverse follows from a coefficient germ alone.
Those obligations remain explicitly separate in the report.

## 6. Source and native reproduction

Source:
`scripts/fourfold_codazzi_moving_turning_complex_germ.py`.
Complete native:
`notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz`.
The actual run completed in about 3.61 seconds with all 10 gates
passed. The report binds the complete candidate manifest, intrinsic
root, original object and source dependencies; every candidate shard
is verified by the loader before use.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/fourfold_codazzi_moving_turning_complex_germ.py --candidate /dev/shm/visible-exact-ac0d699811ad/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json --out notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz
```

The candidate is a command-line input, not a permanent hardcoded
location. Restore its complete SHA-bound manifest and shards through
the owning candidate checkpoint when using another workspace. The
producer refuses to overwrite an existing complete or failed report.
