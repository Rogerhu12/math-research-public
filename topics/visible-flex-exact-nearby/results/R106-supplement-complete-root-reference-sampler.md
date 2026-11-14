# R106 supplement: complete finite root one-form on the saved reference

The source [fourfold_subprincipal_root_reference.py](../scripts/fourfold_subprincipal_root_reference.py)
is an executable adapter for the complete finite seven-field report. No native
run or whole-root integral is asserted by this note. It closes the finite
representation and normalization between that report and the already saved
retarget reference; it does not bypass either report's true error budget.

## 1. Actual root and branch coordinates

Let $\epsilon\in\{-1,+1\}$ be the physical root side, with root
$r=\epsilon t(p)$. On the common physical sine branch
$-\pi/2\le\tau\le\pi/2$ put

$$
 \eta={\pi\over2}-\epsilon\tau,\qquad
 s=\sqrt{2t(p)}\sin(\eta/2),\qquad
 \rho=s^2=t(p)(1-\epsilon\sin\tau).
$$

For a reference subsegment $\tau=c+hu$, $h>0$, this gives

$$
 {ds\over du}=-\epsilon h\sqrt{t(p)/2}\cos(\eta/2).
$$

The root-to-cut orientation is $-\epsilon$ relative to increasing forward
$\tau$. At an exact saved root endpoint, its rational-plus-$\pi$ identity is
checked before $\eta=0$ is imposed. No approximate endpoint is identified with
the root.

The frozen actual scalar sampler uses

$$
 f_\tau=-r_\tau\,{M+\varsigma\,\mathrm{wave}\,W\over D}.
$$

Since $b/a=-M/D$ and $\nu=\mathrm{wave}\,W/D$, the physical characteristic
velocity is $b/a-\varsigma\nu$. Changing to inward $s$ therefore gives

$$
 \sigma_{\rm inward}=-\epsilon\varsigma.
$$

This sign is checked against the actual finite root-source report. For the
forward branch $\varsigma=-1$, the negative root uses inward $\sigma=-1$ and
the positive root inward $\sigma=+1$.

Under the exact radial reflection, $F(-r)=S F(r)$,
$F_r(-r)=-S F_r(r)$ and $\det S=-1$.
Thus $C=F_\theta\times F_r$ transforms to $SC$,
$G_{\rm area},H,F\cdot F,a_0,c_0$ are even and $b_0$ is odd.
The positive-root inward seven functions therefore give the negative-root
functions with the inward sign just specified.
The ratios involving the ground solution, including
$F_{\theta,z}/F_z$, are unchanged; the sign of $F_z$ is never used to redefine
the ground-state operator or drop its constant term.

## 2. Complete finite composition

Let $H_\sigma(s,\theta)=R_\sigma(s,\theta)+\partial_\theta S_{\rm reg}(s^2,\theta)$.
The finite source report keeps its complete representation

$$
 \widehat H_\sigma(s,\theta)
 =\sum_n w^n E_n(\theta)+s\sum_n w^n O_n(\theta),
 \qquad w=\rho/\mathrm{scale}.
$$

Every finite Laurent coefficient and every product frequency is loaded from
SHA-checked shards. Horner evaluation at complex $\rho$ retains the complete
polynomials. Finite angular evaluation uses the existing full Taylor-table
evaluator, which charges input balls, all finite arithmetic and its complete
Taylor tail. It does not project the result to the angular node count.

The saved reference is physical angle $Y(u,x)$ with
$Y(u,x+2\pi)=Y(u,x)+\pi/2$. The adapter returns the complete finite one-form
coefficient

$$
 \widehat B(u,x)
 =-\epsilon\,{ds\over du}\,
   \widehat H_\sigma(s,Y(u,x))\,Y_x(u,x).
$$

This is the coefficient of $dx$, where $x$ is the normalized label and $Y$ is
the physical angle. It is an ordinary one-form pullback; no numerical endpoint
factor is borrowed. Any final R46/R104 amplitude, Fourier-index or physical-cut
conversion remains the separately specified complete frame map, including
$K_{\rm wire}$. This adapter alone does not assert that its output is the final
normalized R104 multiplier.

All means are retained before composition. A nonzero physical mean multiplies
the nonconstant $Y_x$ and may create nonzero label frequencies; deleting that
mean before the pullback would change the result.

## 3. Interior true errors and finite outer bounds

The complete finite root report previously charged errors at its original
physical cut. A full saved time segment containing that cut may extend slightly
past it. The adapter does not transfer the cut-specific fee to that larger
segment. Instead it recomputes the regularized source error at the actual
segment radial upper bound, using the same larger paid error disk. It also
reweights every saved finite arithmetic error row by
$(r/\mathrm{scale})^n$. The enlarged smaller disk must still be strictly inside
the original actual error disk.

The exact monotonicity of $\sin\tau$ on the physical branch supplies the radial
upper bound. The complete real-time reference image certificate, including all
eight Bernstein controls and every retained product frequency, must lie inside
the actual physical angular error strip. Only then is the true source fee
multiplied by the reference $Y_x$ bound and $|ds/du|$.

For the finite composition alone, an outer complex time disk can be used without
extending the actual geometry domain. Set
$z_0=(\pi/2-\epsilon c)/2$ and $w_*=|h|R_u/2$. The identities for
$\sin(z_0+w)$ and $\cos(z_0+w)$ imply

$$
\begin{aligned}
 |s|&\le\sqrt{2t}\bigl(|\sin z_0|\cosh w_*+
                            |\cos z_0|\sinh w_*\bigr),\\
 |s_u|&\le |h|\sqrt{t/2}\bigl(|\cos z_0|\cosh w_*+
                            |\sin z_0|\sinh w_*\bigr).
\end{aligned}
$$

These bounds, the full finite reference image, and the exact finite Laurent
norm yield a complete outer modulus of $\widehat B$.
It is explicitly a bound for the finite polynomial composition. The true
geometry approximation fee is paid only on the stated real-time region.
This is the same separation used by the completed zero-order density pipeline.

## 4. The actual cut and root terms

At the fixed physical cut $r=\epsilon r_c$, use the actual parameter-dependent
time and inward radius

$$
 \tau_c(p)=\epsilon\arcsin(r_c/t(p)),\qquad
 s_c(p)=\sqrt{t(p)-r_c}.
$$

The whole certified parameter-time interval must lie in one saved reference
segment; otherwise the current endpoint method rejects it and requires an
explicit common subdivision. It does not substitute the time midpoint.
The complete finite cut field is evaluated as

$$
 s_c^{-3}\widehat C_{-3}(s_c^2,Y_c)
 +s_c^{-1}\widehat C_{-1}(s_c^2,Y_c)
 +\widehat C_0(s_c^2,Y_c),
$$

then multiplied by the same actual reference $Y_x$.
The separate root term is
$\sigma\,\widehat L_\theta(0,Y_0)Y_x(0)/4$ at the exact saved root endpoint.
Their stored complete approximation errors include the finite coefficient
choices. The caller must still pay the reference angular-image and $Y_x$
multipliers. No endpoint, mean or ground-solution term has been removed.

The remaining assembly is an actual finite time/Fourier integration, plus
the already proved second-order true-flow pullback and complete strict-region
phase. The present source reports only a sample and its real-time geometric
fee. It deliberately does not set a whole-phase, R104-cutoff or PDE-inverse
completion flag.
