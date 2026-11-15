# Complete phase-row approximate inverse and its quadratic defect

2026-11-15.

**Proved one-step identities and conditional norm bounds.** This note supplies the off-constraint approximate-inverse calculation required by H.22 of [the complete strong-return criterion](R133-supplement-quantitative-strong-return-inverse-and-core-high-block-gates.md). It retains every original regular equation and the entire phase average. It gives no unproved numerical regular inverse, scalar Schur lower bound or convergent core iteration.

The primary identities are P.14--P.16 of [the complete phase counterterm](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md). The target used here is the selected quadratic target of [the selected-family first-phase theorem, Section 5](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md), rather than the different illustrative target in Section 6 of the former note. No new numerical evaluation is performed.

## 1. The full nonlinear residual and the raw phase row

Let the physical circle have period $p_0=\pi/2$, and fix
$$
 \rho_{15}=\frac{5831714953207175+\sqrt5}{21212218271020390},
 \qquad \Omega_\star=p_0\rho_{15},\qquad R(x)=x+\Omega_\star.
 \tag{PD.1}
$$
Use degree-one lifts throughout. At the current state let $g(x+p_0)=g(x)+p_0$, $g'>0$, and put
$$
 E(Q,\nu,g)=P(Q,\nu)\circ g-g\circ R,\qquad
 J=g'\circ R>0.
 \tag{PD.2}
$$
Here $Q$ denotes the full regular state, including any independent cap, boundary, height or matching variables in the chosen chart; $P$ depends on its actual physical field. The regular residual $\mathcal R(Q,\nu)$ contains the original complete body, boundary, waist, jump, physical fourth-mode Robin and independent mean rows. No row is exchanged for the phase equation. An independent geometric quantity which is already an output remains an output.

Write the full derivative at this current state as
$$
 D\mathcal R(Q,\nu)[h,\kappa]=A h-N_\nu\kappa,
 \qquad N_\nu=-\partial_\nu\mathcal R.
 \tag{PD.3}
$$
Thus $N_\nu$ includes the direct parameter derivative of every retained regular row. Its sign is fixed by (PD.3). The exact augmented map is
$$
 \mathcal F(Q,\nu,g)=(\mathcal R(Q,\nu),E(Q,\nu,g)).
 \tag{PD.4}
$$
The phase component in (PD.4) is the unnormalized residual $E$. Dividing its current linearized row by $J$ below is not a replacement of this nonlinear map by $E/J$.

All formulas are first identities on smooth states in an admissible common chart. The norm statements apply whenever their displayed quantities are finite and the complete underlying maps have the required derivatives. The current field is not assumed already to obey $E=0$.

## 2. An explicit approximate inverse with every regular defect retained

Let $G$ be a candidate regular right inverse and $z_\nu$ a candidate parameter response, at the same state and with every original row retained. Define their actual defects by
$$
 r_f=(A G-I)f,\qquad r_\nu=A z_\nu-N_\nu.
 \tag{PD.5}
$$
These definitions do not assume that either defect vanishes.

Use the current normalized phase functionals
$$
 Lh=\frac{D_QP[h]\circ g}{J},\qquad
 b_\nu=\frac{\partial_\nu P\circ g}{J},\qquad
 B=b_\nu+Lz_\nu,\qquad S=\langle B\rangle_x,
 \tag{PD.6}
$$
where $\langle\cdot\rangle_x$ is the full normalized average in the conjugacy variable $x$. Assume, for this one-step construction, an actually proved bound
$$
                         |S|\ge \sigma>0.                         \tag{PD.7}
$$
No such numerical bound is supplied by this note.

For an arbitrary regular target $f$ and an arbitrary **raw phase target** $b$, set
$$
 \begin{aligned}
 v&=b/J-LGf,\\
 \kappa&=\langle v\rangle_x/S,\\
 w&=v-B\kappa,\qquad \langle w\rangle_x=0,\\
 a-a\circ R&=w,\qquad \langle a\rangle_x=0,\\
 h&=Gf+z_\nu\kappa,\qquad \delta g=g'a.
 \end{aligned}                                                     \tag{PD.8}
$$
The zero mean of $a$ chooses the constant kernel for this linear solve. It does not assert a separately imposed nonlinear condition on $\langle g-x\rangle$.

The exact derivative identity is
$$
 \boxed{\quad
 D\mathcal F(Q,\nu,g)[h,\kappa,g'a]
   =\bigl(f+r_f+r_\nu\kappa,\ b+E'a\bigr).
 \quad}                                                           \tag{PD.9}
$$
In particular the phase defect is $E'a$ in the raw target units.

To prove it, differentiation of (PD.2) in $x$ gives
$$
 P'(Q,\nu;g)\,g'=J+E'.
$$
The phase variation at fixed $\Omega_\star$ is consequently
$$
 \begin{aligned}
 \delta E
 &=D_QP[h]\circ g+(\partial_\nu P\circ g)\kappa
          +P'(g)g'a-(g'a)\circ R\\
 &=J\{Lh+b_\nu\kappa+a-a\circ R\}+E'a.
 \end{aligned}                                                     \tag{PD.10}
$$
Substituting (PD.8) makes the brace exactly $b/J$. Substitution in (PD.3) gives the first component of (PD.9). No derivative of the algorithm $G,z_\nu,S$ is needed to evaluate the linearized map on this one direction.

The phase mean of the omitted term is generally
$$
                         \langle E'a\rangle_x.                   \tag{PD.11}
$$
It remains in (PD.9). Neither $\langle E'\rangle_x=0$ nor $\langle a\rangle_x=0$ makes (PD.11) zero. No phase average is identified with the independent physical even mean in $\mathcal R$.

## 3. The principal small divisor and its exact derivative loss

For $p_0$-periodic functions use
$$
 u(x)=\sum_{j\in\mathbb Z}\widehat u_j e^{4ijx},\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 \|u\|_{H^s}^2=\sum_j\Lambda_j^{2s}|\widehat u_j|^2.
 \tag{PD.12}
$$
The already proved principal arithmetic of $\rho_{15}$ gives
$$
       |1-e^{2\pi i j\rho_{15}}|>\frac1{68|j|}
                   \quad(j\ne0).                                \tag{PD.13}
$$
This is the principal conjugacy gap. It is distinct from the first-phase strong-return gap involving $\beta_\star/j$, the fourth roots of unity, and the restriction $|j|\ge97$.

The unique zero-mean solution in (PD.8) is
$$
 \widehat a_0=0,\qquad
 \widehat a_j=\frac{\widehat w_j}{1-e^{2\pi i j\rho_{15}}}
                         \quad(j\ne0).
 \tag{PD.14}
$$
It preserves reality. Since $68|j|\le17\Lambda_j$, for every real $s$,
$$
                     \|a\|_{H^s}\le17\|w\|_{H^{s+1}}.             \tag{PD.15}
$$
This is a loss of one derivative. It does not give a bounded inverse from $H^s$ to the same $H^s$.

For the Wiener strip norm
$$
 \|u\|_{\mathcal A_\alpha}
      =\sum_j|\widehat u_j|e^{4|j|\alpha},
$$
and $0<\tau<\alpha$, (PD.14) also gives
$$
       \|a\|_{\mathcal A_{\alpha-\tau}}
                   \le\frac{17}{\tau}\|w\|_{\mathcal A_\alpha}.
 \tag{PD.16}
$$
Indeed $68|j|e^{-4|j|\tau}\le17/\tau$. This analytic statement requires actual strip norms for $w$ and the maps forming it; a real Sobolev estimate does not supply them.

## 4. A tame product estimate and the complete phase defect

For $s\ge1$ put
$$
                         C_s=\frac98\,2^{s-1}.
$$
The normalized Fourier norms in (PD.12) obey
$$
 \|uv\|_{H^s}\le C_s\bigl(
      \|u\|_{H^s}\|v\|_{H^1}
          +\|u\|_{H^1}\|v\|_{H^s}\bigr).                         \tag{PD.17}
$$
For completeness, $\Lambda_{k+\ell}\le\Lambda_k+\Lambda_\ell$ implies
$\Lambda_{k+\ell}^s\le2^{s-1}(\Lambda_k^s+\Lambda_\ell^s)$.
Young's convolution inequality then bounds each term by one weighted $\ell^2$ norm and one unweighted $\ell^1$ norm. Finally
$$
 \sum_j\Lambda_j^{-2}
  \le1+\frac1{16}\sum_{j\ne0}j^{-2}
  =1+\frac{\pi^2}{48}<\left(\frac98\right)^2
$$
proves the required $\ell^1$ bound by Cauchy--Schwarz. This argument includes the zero Fourier coefficient.

Combining (PD.15) and (PD.17) proves the explicit quadratic-defect estimate
$$
 \boxed{\quad
 \|E'a\|_{H^s}
 \le17 C_s\bigl(
       \|E\|_{H^{s+1}}\|w\|_{H^2}
          +\|E\|_{H^2}\|w\|_{H^{s+1}}\bigr),\qquad s\ge1 .
 \quad}                                                           \tag{PD.18}
$$
It is bilinear in the current phase residual and the normalized target produced by (PD.8). Its loss is stated explicitly. One may not place this term into a same-order Neumann series just from the smallness of a low norm of $E'$.

If $E,w$ both have the actual analytic norm at width $\alpha$, the algebra property of $\mathcal A_{\alpha-\tau}$ and the derivative multiplier give
$$
 \|E'a\|_{\mathcal A_{\alpha-\tau}}
       \le\frac{17}{\tau^2}
                   \|E\|_{\mathcal A_\alpha}
                   \|w\|_{\mathcal A_\alpha}.                    \tag{PD.19}
$$
Both factors are estimated on the same target strip: one uses
$\|E'\|_{\mathcal A_{\alpha-\tau}}\le\tau^{-1}\|E\|_{\mathcal A_\alpha}$
and (PD.16) separately. This proof does not assume an analytic unknown core merely because its coefficients were enclosed on a complex product.

## 5. Bounds for the direction and preservation of orientation

The scalar counterterm is bounded by its complete mean:
$$
 |\kappa|
 \le \sigma^{-1}\bigl(
           \|b/J\|_{L^2}+\|LGf\|_{L^2}\bigr).
 \tag{PD.20}
$$
For $s\ge0$, define the explicit expression
$$
 \begin{split}
 W_s(f,b)={}&\|b/J\|_{H^s}+\|LGf\|_{H^s}\\
 &+\sigma^{-1}\|B\|_{H^s}
          \bigl(\|b/J\|_{L^2}+\|LGf\|_{L^2}\bigr).
 \end{split}                                                       \tag{PD.21}
$$
Then $\|w\|_{H^s}\le W_s(f,b)$ and
$\|a\|_{H^s}\le17W_{s+1}(f,b)$. The regular direction satisfies, in any applicable normed state space $X_s$,
$$
                    \|h\|_{X_s}
              \le\|Gf\|_{X_s}+\|z_\nu\|_{X_s}|\kappa|.             \tag{PD.22}
$$
For $s\ge1$ the actual embedding direction obeys
$$
 \|g'a\|_{H^s}
 \le C_s\bigl(\|g'\|_{H^s}\|a\|_{H^1}
                   +\|g'\|_{H^1}\|a\|_{H^s}\bigr).               \tag{PD.23}
$$
The constants for $J^{-1}$, $L$, $G$, $z_\nu$, $B$ and the full regular source and state spaces must still be paid at the same background. They are not covered by the divisor constant 17.

Since $g'a$ is periodic, adding it preserves degree one. If $c=\inf g'>0$ and
$$
                         \|(g'a)'\|_\infty\le c/2,                \tag{PD.24}
$$
then the new embedding has derivative at least $c/2$. Every separate domain constraint on the physical state, parameter, cap inputs, matching charts and composition maps must also hold on the whole line segment used below. Orientation alone does not supply those domain constraints.

## 6. A full Newton residual identity with smoothing allowed

Let $\mathcal S_N$ be any declared linear smoothing operator on the **output data** of $\mathcal F$. On scalar regular rows it acts as the identity. On the phase row it includes the constant coefficient; deleting that coefficient would remove the actual scalar counterterm equation. Angular smoothing in a physical regular row uses that row's physical chart. Phase smoothing uses $x$. No commutation or identification of these projectors is assumed.

Choose the targets in (PD.8) to be
$$
             (f,b)=-\mathcal S_N\mathcal F(Q,\nu,g)
$$
and write $\Delta=(h,\kappa,g'a)$. If the full map is twice differentiable along the admissible segment, its exact Taylor remainder is
$$
 \mathcal Q_2
  =\int_0^1(1-t)\,
     D^2\mathcal F((Q,\nu,g)+t\Delta)[\Delta,\Delta]\,dt.
 \tag{PD.25}
$$
Equations (PD.9) and (PD.25) give
$$
 \boxed{\quad
 \mathcal F((Q,\nu,g)+\Delta)
    =(I-\mathcal S_N)\mathcal F(Q,\nu,g)
       +(r_f+r_\nu\kappa,\ E'a)+\mathcal Q_2 .
 \quad}                                                           \tag{PD.26}
$$
The formula contains the complete regular and phase rows, including both kinds of mean. Smoothing acts on the chosen targets only; no expression such as $AG\mathcal S_N=\mathcal S_N AG$ is used.

For example, the phase component satisfies
$$
 \begin{split}
 \|E_{\rm new}\|_{H^s}\le{}&
       \|(I-\mathcal S_N^{\rm phase})E\|_{H^s}\\
 &+17C_s\{\|E\|_{H^{s+1}}\|w\|_{H^2}
                  +\|E\|_{H^2}\|w\|_{H^{s+1}}\}\\
 &+\frac12\sup_{0\le t\le1}
   \|D^2E((Q,\nu,g)+t\Delta)[\Delta,\Delta]\|_{H^s},
 \qquad s\ge1 .
 \end{split}                                                       \tag{PD.27}
$$
In a regular output space $Y_s$ its companion is
$$
 \begin{split}
 \|\mathcal R_{\rm new}\|_{Y_s}\le{}&
  \|(I-\mathcal S_N^{\rm reg})\mathcal R\|_{Y_s}
       +\|r_f\|_{Y_s}+\|r_\nu\|_{Y_s}|\kappa|\\
 &+\frac12\sup_{0\le t\le1}
    \|D^2\mathcal R((Q,\nu)+t(h,\kappa))
                        [(h,\kappa),(h,\kappa)]\|_{Y_s}.
 \end{split}                                                       \tag{PD.28}
$$

If $G$ and $z_\nu$ are exact for the full current regular derivative, then $r_f=r_\nu=0$. If they are approximate, the additional term $r_f+r_\nu\kappa$ must be controlled. A fixed small response defect $r_\nu$ times $\kappa$ is not automatically quadratic in the old residual. Bounds for the true parameter response, its approximation error and every regular boundary row remain necessary.

At a fixed background the construction (PD.8) is linear in $(f,b)$. Thus (PD.18) is a genuine residual-times-direction term for the Newton choice, whenever the same-state tame bounds in (PD.20)--(PD.23) are supplied. It does not by itself prove that the smoothing tails, derivative losses and $D^2\mathcal F$ can be summed over an iteration.

## 7. Phase normalization, full means and the remaining core task

At an exact conjugacy $E=0$, the change of variables $y=g(x)$ in the invariant-measure formula P.13 identifies
$\langle(D_QP[h]\circ g)/J\rangle_x$
with the full state contribution $L_\Omega h$, and similarly identifies the direct parameter term. If $z_\nu$ is the true full regular response, $S$ is therefore the P.16 scalar Schur coefficient. At a general iterate, (PD.6) defines the explicit scalar used in this approximate inverse; no differentiable rotation-number function on an interval of arbitrary circle maps is assumed.

The denominator $J$ in (PD.8) is frozen only as a coefficient of the current linear solve. If one instead chose the nonlinear residual $E/J$, its derivative would contain the additional term $-E\,\delta J/J^2$. Equations (PD.9) and (PD.26) use the raw residual (PD.2), so this additional normalized-map term is not being omitted.

The new proved statements are the exact complete approximate-inverse identity (PD.9), the one-derivative divisor bound (PD.15), the explicit tame and strip defect bounds (PD.18)--(PD.19), and the full smoothed Newton identity (PD.26). They close the one-step off-constraint bookkeeping required by H.22.

The actual remaining inputs are the same-object full regular inverse or a suitable quantitative approximate inverse, the complete parameter response and a positive lower bound for $|S|$, uniform tame bounds for the full second derivative and compositions, a smoothing schedule with summable losses, and verified state and trace domains throughout that iteration. The selected-family first scalar $\beta_\star$ still requires its own comparison at the true background if it is used for the strong return. The physical finite border, the two true core cuts, all cap and waist matching, and the low/high physical curvature gates remain independent obligations.

None of these missing quantities is supplied by a finite-volume source upper bound, a conditional tail solution or this one-step algebra. All successful numerical inputs remain immutable and are read only.
