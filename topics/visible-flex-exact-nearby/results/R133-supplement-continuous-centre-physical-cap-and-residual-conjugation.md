# R133 supplement: the continuous physical cap and its exact residual conjugation

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved.** The distinct, exactly continuous repair of the final moving
centre has the complete physical Codazzi cap inverse on
$[9/10,25/8]$. Its actual feedback is less than $0.820523$ and its
resolvent is less than $5.571744$. This statement includes every Fourier
mode, the physical mean rows, the true nonlinear exterior derivative,
ordinary sources, angular-divergence sources and independent jumps.
The original centre is not relabelled as the repaired centre.

For the complete moving Jacobi operator at a centre with nonzero
residual, the exact conjugation below leaves just one differentiated
unknown term: a **common real transport**. We put that term into the
already paid angular-divergence source column of the cap Green operator.
Everything else uses the actual centre residual and its first angular
derivative. A quantitative contraction criterion is given in (C.31).
It is a cap criterion, not a whole mixed-body inverse or a negative
return estimate. The companion consumer rejects an incomplete residual
cover before it can assert the additional moving-cap inverse.

## 1. The two distinct centres and the complete norms

The original complete candidate has SHA256

```
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413
```

Its exact continuous repair is (V.1)--(V.3) of
[the exact repair theorem](R133-supplement-exact-continuous-repair-of-final-centre.md),
with definition SHA256

```
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
```

Write the repaired moving state as $Q=(u,v)$, its mean as
$m=\langle v\rangle_\phi$, and

$$
 \theta=\phi+\frac1m I_\phi(v-m),\qquad
 \theta_\phi=v/m>0,\qquad
 W=(B,C)=(u/v,1/v)\circ\phi(\theta).
 \tag{C.1}
$$

Here $I=\partial^{-1}P_{\ne0}$ has multiplier $1/(ik)$ on
$k\in4\mathbb Z\setminus\{0\}$ and is zero on the mean. The actual
reflection class is $u$ odd, $v$ even. Its even mean is arbitrary; it
is never discarded. The physical cap Green theorem is stated on the
larger two-mean space. Its restriction to this reflection class has
$B_0=0$ by parity and retains the complete $C_0$ row.

For coefficient fields on the whole cap, use the joint Wiener norm

$$
 \|a\|_{\mathscr A_\sigma}
   =\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_r|a_k(r)|.
 \tag{C.2}
$$

For physical unknowns use the exact module from
[the original all-mode physical cap theorem](R133-supplement-actual-final-all-mode-physical-cap-Green.md):

$$
 \|x\|_{\mathfrak M}
 =\left(\sum_k\sup_r|x_{B,k}(r)|^2\right)^{1/2}
  +\left(\sum_k\sup_r|x_{C,k}(r)|^2\right)^{1/2}.
 \tag{C.3}
$$

In particular $\sup_r\|x(r)\|_{L^2\oplus_1 L^2}\le\|x\|_{\mathfrak M}$.
The complete convolution inequality is
$\|ax\|_{\mathfrak M}\le\|a\|_{\mathscr A_0}\|x\|_{\mathfrak M}$.
We do not interchange the coefficientwise radial supremum and its sum.
We also do not claim that an arbitrary moving-angle composition has a
small same-order operator difference from the identity.

## 2. Actual transfer of the background and the physical inverse

Put $w=(v-m)/m$. The original native retains every coefficientwise
supremum of $u$, $w=\psi_\phi$, and $\psi=I_\phi w$.
For the repair, its full cumulative correction satisfies

$$
 \|e\|_{\mathscr A_{1/32}}<4.832\,10^{-18},\qquad
 \|e_\phi\|_{\mathscr A_{1/32}}<2.026\,10^{-17},\qquad
 |e_0|<5.842\,10^{-21}.
 \tag{C.4}
$$

These are the complete pair norms and contain the even mean. If
$m_*>0$ is the old mean gap and $\bar m_*=m_*-|e_0|$, then

$$
 \left\|\frac{v+e_v-(m+e_0)}{m+e_0}\right\|_{\mathscr A_{1/32}}
 \le\left(1+\frac{|e_0|}{\bar m_*}\right)
                   \|w\|_{\mathscr A_{1/32}}
              +\frac{\|e_v\|_{\mathscr A_{1/32}}}{\bar m_*}.
 \tag{C.5}
$$

The same formula applies after one angular derivative. For the
primitive, the last term has the additional factor $1/4$.
Thus the actual inverse angle remains the Banach-algebra fixed point
$h=-\psi(\operatorname{id}+h)$ in $\mathscr A_{1/64}$. No inverse is
obtained by sampling the real angle.

The complete native transfer gives the following strict bounds. Every
displayed field is in the actual repaired physical angle unless a
moving derivative is explicitly indicated.

| Quantity | Strict bound |
| --- | ---: |
| $|m|$ from below / above | $3.1914104290$ / $5.8639401366$ |
| $\|w\|_{\mathscr A_{1/32}}$ | $.015211829$ |
| $\|w_\phi\|_{\mathscr A_{1/32}}$ | $.061779810$ |
| $\|\phi(\theta)-\theta\|_{\mathscr A_{1/64}}$ | $.003774146$ |
| $\|u\|_{\mathscr A_{1/64}}$ | $.019598032$ |
| moving $\|u_\phi\|_{\mathscr A_{1/32}}$ | $.079576107$ |
| $\|v\|_{\mathscr A_{1/64}}$ | $5.953141388$ |
| $\|C\|_{\mathscr A_{1/64}}$ | $.318181201$ |
| $\|C_\theta\|_{\mathscr A_{1/64}}$ | $.020269146$ |
| $\|B\|_{\mathscr A_{1/64}}$ | $.006235726$ |
| $\|B_\theta\|_{\mathscr A_{1/64}}$ | $.026107964$ |
| $\|W_\theta\|_{\mathscr A_{1/64},\mathrm{pair}}$ | $.046377109$ |
| $\phi_\theta$ / $\theta_\phi$ from above | $1.015446803$ / $1.015211829$ |

For example the bounds for $C$ and its physical derivative follow
directly from

$$
 C=\frac1{m(1+w)},\qquad
 C_\theta=-\frac{w_\phi}{m(1+w)^3}.
 \tag{C.6}
$$

The actual nonlinear physical coefficients are still exactly

$$
 Q_B=2u,\qquad Q_C=\ell-u^2-Kv^2.
 \tag{C.7}
$$

The consumer uses the finite moving expression
$Q_C=-u^2-K(2s\alpha V+\alpha^2V^2)$ and the complete repair
differences; it does not subtract poorly conditioned floating numbers.
The repaired complete physical bounds are

$$
 \|Q_B\|_{\mathscr A_{1/64}}<.039196064,
 \qquad \|Q_C\|_{\mathscr A_{1/64}}<.051432066.
 \tag{C.8}
$$

The intrinsic target and the rotational reference Green have not
changed. The original comparison between the historical rotational
outer line and the actual installed exterior is still explicitly
retained in its source column. Moreover, along the entire straight
repair path, (C.6) and the first differential below give

$$
 \|\Delta C(R)\|_{\mathscr A_{1/64}}
   <4.970\,10^{-19},\qquad
 |\Delta C_0(R)|<7.898\,10^{-23}.
 \tag{C.9}
$$

The second inequality also follows from the exact right mean offset
and $C_0=1/m$. The original bound $\|Z(R)\|_{A^0}<2.533\,10^{-13}$
therefore becomes $\|\bar Z(R)\|_{A^0}<2.533005\,10^{-13}<10^{-12}$.
The actual uniform exterior derivative on that entire ball applies.
The changed mean is paid, not declared zero.

Using exactly the original reference Green kernels and (C.8), the
new complete feedback is

$$
 \chi_{\rm phys}<.820522971,
 \qquad (1-\chi_{\rm phys})^{-1}<5.571744.
 \tag{C.10}
$$

The closed ordinary $L^2_rL^2_\theta$ source gains remain below
$12.725633$ and $22.179140$ for the $B$ and $C$ equations. The closed
angular-divergence module gains remain below $18.407084$ and
$41.065564$. All original independent inner $C_{\ne0}$, right Robin,
right mean, and physical jump gains are retained individually in the
native. Their construction is all-frequency and is not an inverse
of a finite radial or Fourier collocation matrix.

## 3. The complete first differential and its inverse

Let $\Psi:Q\mapsto W$ be (C.1), and pull a moving direction $h$ to
the physical angle when it occurs in the following formulas. Define

$$
 P=\begin{pmatrix}C&-BC\\0&-C^2\end{pmatrix},\qquad
 e_h=I_\theta(C h_2),\qquad
 x=D\Psi(Q)h=P h-W_\theta e_h.
 \tag{C.11}
$$

Indeed $\delta\theta_\theta=C h_2-z_h/m$, where
$z_h=\langle h_2\rangle_\phi$ and
$\langle C h_2\rangle_\theta=z_h/m$. Reflection makes
$\delta\theta$ odd and fixes its integration constant to zero.
This proves (C.11), including the even mean.

Conversely put $x=(b,c)$ and

$$
 p_c=I_\theta\{c-mC\langle c\rangle_\theta\},\qquad
 S'=\begin{pmatrix}v&-uv\\0&-v^2\end{pmatrix}.
 \tag{C.12}
$$

Then the exact inverse differential, expressed at the same physical
angle before returning to $\phi$, is

$$
 \boxed{\quad h=S'\{x-vW_\theta p_c\}.\quad}
 \tag{C.13}
$$

To verify it, differentiate
$\phi=\theta+mI_\theta(C-C_0)$ with $m=1/C_0$.
The angle variation is
$mI_\theta(c-mC\langle c\rangle)$; its inverse variation at fixed
$\phi$ is $-v p_c$. Applying the reciprocal derivative $S'$ gives
(C.13). In particular

$$
 \langle x_C\rangle_\theta=-z_h/m^2.
 \tag{C.14}
$$

Thus the mean map is an actual invertible scalar, not a discarded
row. The full reconstruction is not obtained by setting
$h_2=\partial_\phi^{-1}(h_2)_\phi$.

Hereafter write $C_*,B_*,V_*,W_1$ for the upper coefficient bounds
in the table and $J_*=(1-\|w\|)^{-1}$. The elementary operator bounds
$\|I\|_{L^2\to L^2}=1/4$ and $\|mC\|_\infty\le J_*$ give

$$
 \|p_c\|_2\le I_*\|c\|_2,
 \quad I_*=(1+J_*)/4.
 \tag{C.15}
$$

Put

$$
 \begin{aligned}
 S_*&=\max\{V_*,V_*(U_*+V_*)\},\\
 H&=S_*(1+V_*W_1I_*),\\
 H_2&=V_*^2(1+V_*C_{\theta,*}I_*).
 \end{aligned}
 \tag{C.16}
$$

Then $\|h\|_{L^2\oplus_1L^2}\le H\|x\|_{L^2\oplus_1L^2}$ and
$\|h_2\|_2\le H_2\|x_C\|_2$ at the same physical angle.
The actual values satisfy

$$
 H<40.502869,\quad H_2<37.594586,\quad
 \|h\|_{L^\infty_r(L^2_\phi\oplus_1L^2_\phi)}
      <40.814490\|x\|_{\mathfrak M}.
 \tag{C.17}
$$

The last factor contains the genuine measure conversion
$d\phi=\phi_\theta d\theta$.

For an arbitrary ordinary moving source $f$, (C.11) similarly yields

$$
 \|D\Psi f\|_{L^2_rL^2_\theta,\mathrm{pair}}
       <.324309160\|f\|_{L^2_rL^2_\phi,\mathrm{pair}}.
 \tag{C.18}
$$

No finite-mode assumption is made on $x,h$, or $f$ in these estimates.

## 4. Exact second differential at a centre with nonzero residual

Let $F$ denote the full moving nonlinear vector field and
$R=Q_r-F(Q)$ its **actual** residual. In formulas with physical
derivatives, pull $R$ to the physical angle. Set

$$
 t=P R,\qquad e=I_\theta(C R_2),\qquad
 \mu_h=\langle C h_2\rangle_\theta.
 \tag{C.19}
$$

The complete second differential has the following cancellation:

$$
 \boxed{\begin{aligned}
 D^2\Psi(Q)[R,h]
 ={}&-e x_\theta+DP[t]h-t_\theta e_h\\
 &+W_\theta\{(CR_2)e_h+e\mu_h
                         -\langle C e h_2\rangle_\theta\}.
 \end{aligned}}
 \tag{C.20}
$$

Here

$$
 DP[t]=\begin{pmatrix}
 t_C&-Ct_B-Bt_C\\0&-2Ct_C
 \end{pmatrix}.
 \tag{C.21}
$$

The retained last mean in (C.20) vanishes for the exact even/odd
inputs, but is not used as a reason to omit any mean estimate.

For completeness, differentiating (C.11) at fixed physical angle
gives $\delta h=-e h_\theta$ and
$\delta W=t-W_\theta e$. Since
$e_\theta=CR_2-\langle CR_2\rangle$, integration of the exact derivative
of $e_h$ gives

$$
 \delta e_h=-\langle CR_2\rangle e_h-e C h_2
                              +\langle e C h_2\rangle.
 \tag{C.22}
$$

Substituting this in $\delta(P h-W_\theta e_h)$ cancels both
$W_{\theta\theta}e e_h$ terms and leaves (C.20).
No second angular derivative of the centre and no derivative of $R$
beyond $R_\theta$ is required. As a separate check on its full mean,
differentiating $C_0=1/m$ twice gives exactly

$$
 \left\langle(D^2\Psi[R,h])_C\right\rangle_\theta
       =2z_Rz_h/m^3,
 \quad z_R=\langle R_2\rangle_\phi.
 \tag{C.23}
$$

This term is generally nonzero.

Let $\mathcal D_{\rm mov}=\partial_r-DF(Q)$ and let
$\mathcal D_{\rm phys}$ be the actual physical Codazzi linearization
at $W=\Psi(Q)$. The nonlinear residual covariance and the chain rule
give

$$
 \boxed{\quad
 \mathcal D_{\rm phys}(D\Psi h)
   =D\Psi(\mathcal D_{\rm mov}h)+D^2\Psi[R,h].
 \quad}
 \tag{C.24}
$$

In particular it is not legitimate to omit the last term merely
because the centre is a good approximate solution.

## 5. Full source budget and the moving-cap contraction

Suppose $r_{U,0},r_{V,0}$ are complete moving $A^0$ residual bounds
and $r_{U,1},r_{V,1}$ are complete inhomogeneous $A^1$ bounds, with
the physical normalization $R=(\alpha R_U,\alpha R_V)$ already applied.
Their correction for the continuous repair is described in Section 6.
The actual centre and its repaired residual have exact moving Fourier
degree at most 96. This finite statement applies to the **coefficients
of the operator**, not to an unknown direction or source.

If $h_*$ is the actual inverse-angle displacement bound in the table,
the full joint physical residual coefficient bound is

$$
 R_{V,\rm joint}\le r_{V,0}+
   \sum_{j=1}^{96}\min\left\{r_{V,0},\frac{r_{V,1}}{1+4j}\right\}
                  e^{4j h_*}.
 \tag{C.25}
$$

For a real cosine pair the sum of its two Fourier moduli is bounded
by the full $A^0$ norm, so the summation in (C.25) has no missing
factor two. This bound takes a supremum for each coefficient before
summing, and includes the genuine mean. Actual inverse-angle
composition in $\mathscr A_0$ costs precisely the displayed exponential;
we do not charge the unnecessarily larger $e^{|k|/32}$.

Let

$$
 \begin{aligned}
 E_A&=C_*R_{V,\rm joint}/4,&
 E_\infty&=(\pi/8)C_*r_{V,0},&
 E_1&=2C_*r_{V,0},\\
 T_B&=C_*r_{U,0}+B_*C_*r_{V,0},&
 T_C&=C_*^2r_{V,0},\\
 P_*&=\max\{C_*,B_*C_*+C_*^2\},\\
 P_{1,*}&=\max\{C_{\theta,*},
    B_{\theta,*}C_*+B_*C_{\theta,*}+2C_*C_{\theta,*}\},\\
 T_1&=P_{1,*}(r_{U,0}+r_{V,0})
            +P_*J_*(r_{U,1}+r_{V,1}),\\
 D_P&=C_*T_B+(1+B_*+2C_*)T_C.
 \end{aligned}
 \tag{C.26}
$$

Then $\|e\|_{\mathscr A_0}\le E_A$,
$\|e\|_\infty\le E_\infty$ and
$\|e_\theta\|_\infty\le E_1$.
The factor $\pi/8$ is the actual $L^\infty$ norm of the zero-mean
primitive on a circle of period $\pi/2$; it is not replaced by its
smaller $L^2$ norm $1/4$. The factor two in $E_1$ pays mean removal
in $L^\infty$.

Writing (C.20) as $-e x_\theta+Zx$, the complete zero-order budget is

$$
 Z_*=D_PH+\frac14T_1C_*H_2
        +W_1\left(\frac14C_*^2r_{V,0}+2C_*E_\infty\right)H_2.
 \tag{C.27}
$$

This follows term by term from (C.15)--(C.22), using the full $h_2$
norm and the actual mean pairing. It is an $L^2$ operator estimate;
no unknown Fourier cutoff appears.

Most importantly, put the differentiated term in the exact form

$$
 -e x_\theta=\partial_\theta(-e x)+e_\theta x.
 \tag{C.28}
$$

The first source belongs to the complete module by (C.2)--(C.3),
with norm at most $E_A\|x\|_{\mathfrak M}$. The remaining source
belongs to $L^2_rL^2_\theta$ with norm at most
$\sqrt{25/8-9/10}(E_1+Z_*)\|x\|_{\mathfrak M}$.

Let $G_o$ be the larger of the two **closed** ordinary-source gains
from Section 2 and let $G_d$ be the larger of its two closed
divergence-source gains. Thus

$$ G_o<22.179140,\qquad G_d<41.065564. \tag{C.29} $$

The actual physical Green already includes the background coefficient
feedback and the full exterior derivative. They are not applied again
to (C.20). Its additional complete moving-to-physical feedback is

$$
 \varepsilon_{\rm bridge}
   =G_dE_A+G_o\sqrt{25/8-9/10}\,(E_1+Z_*).
 \tag{C.30}
$$

Consequently, if the actual complete residual cover verifies

$$ \boxed{\quad\varepsilon_{\rm bridge}<1,\quad} \tag{C.31}
$$

the full moving cap BVP has inverse in the space
$D\Psi^{-1}\mathfrak M$, with the original physical inner
$C_{\ne0}$ port and all genuine outer regular ports. Every closed
physical gain is multiplied by $(1-\varepsilon_{\rm bridge})^{-1}$.
For ordinary moving sources there is additionally the source factor
$.324309160$ from (C.18); to measure the output in
$L^\infty_rL^2_\phi$ there is the reconstruction factor $40.814490$.

This is a Banach contraction of the complete Green equation. It does
not identify a large discrete QR inverse with a continuous inverse,
does not assume a zero centre residual, and does not claim that its
right stable graph alone closes the negative-body return.

## 6. Repair residual, parameter columns and genuine interfaces

On every original open piece the repair offset is independent of $r$.
Thus

$$
 \bar R=R-\{F(Q+e)-F(Q)\}.
 \tag{C.32}
$$

For $j=0,1$ use the complete inhomogeneous Wiener norms $Q_j,E_j$
of the old state and the repair. Put $K_*=\max(1,|K|)$,
$S_j=K_*Q_j^2$ and
$\Delta S_j=K_*(2Q_jE_j+E_j^2)$. From the full moving field

$$
 F(Q)=dQ_\phi+\gamma mJ(K)Q_\phi
       +\beta(-u,v)-\beta(u^2+Kv^2)Q,
 \qquad d=-\beta I(u^2+Kv^2),
 \tag{C.33}
$$

the following explicit bound is valid:

$$
 \begin{aligned}
 \|F(Q+e)-F(Q)\|_{A^j,\rm pair}
 \le{}&\frac{|\beta|}{4}
   \{\Delta S_jQ_{j+1}+(S_j+\Delta S_j)E_{j+1}\}\\
 &+\gamma K_*\{|e_0|Q_{j+1}+(|m|+|e_0|)E_{j+1}\}\\
 &+|\beta|\{E_j+\Delta S_jQ_j+(S_j+\Delta S_j)E_j\}.
 \end{aligned}
 \tag{C.34}
$$

The complete same-object positive cache supplies $Q_0,Q_1$, and
$Q_2\le129Q_1$ follows from the actual degree 32 of the centre.
The small correction itself is paid with its exact $A^0,A^1,A^2$
native bounds. The actual additional pair residuals are

$$
 \|\bar R-R\|_{A^0}<4.285\,10^{-15},\qquad
 \|\bar R-R\|_{A^1}<2.902\,10^{-13}.
 \tag{C.35}
$$

In particular (C.25)--(C.31) use $\alpha$ times the normalized
original residual plus (C.35), not the original residual without a
centre-change fee. The cap lies beyond the support of the compact
$\nu$ perturbation, so its intrinsic direct $\nu$ source is zero;
all incoming $\nu$-response traces at $9/10$ remain independent inputs.
On the rest of the body the exact parameter-column change remains
$\int_0^1D_Q\partial_\nu F(Q+te)e\,dt$ and is not set to zero by
this local result.

The repaired value and every angular derivative agree exactly at
each interface. Hence its angle map and the full first differential
(C.11) agree there too. A homogeneous continuous moving direction
has a homogeneous continuous physical direction in the **same**
physical angle. There is no uncompensated composition jump. The
centre radial derivative and its residual may have ordinary one-sided
jumps; (C.20) contains no radial derivative of those residuals and
does not create a radial delta source from them.

If independent affine direction jumps $j$ are prescribed instead,
their physical jumps are exactly $D\Psi j$. They are paid by the two
physical jump columns, including their means, with the same pointwise
source-map factor in (C.18). This supplies complete interface data;
it does not delete jumps of an arbitrary trial or adjoint.

## 7. Native input and scope of each report

The consumer is
`scripts/fourfold_codazzi_continuous_cap_residual_conjugation.py`.
It binds the complete original physical-cap native, the complete
4,650-row positive coefficient cache, and the exact repair native by
SHA256. It reuses their proved closed-box inequalities without running
the original target primitive again. It evaluates all new analytic,
mean, product, source and exterior-ball inequalities in Arb.

The completed background native is
`notes/2026-11-14-R133-continuous-repair-physical-cap-background-v2-native.json.gz`.
All six actual gates passed. Its exact command, from the topic directory,
was

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python \
  scripts/fourfold_codazzi_continuous_cap_residual_conjugation.py \
  --positive-cache /workspace/scratch/ac0d699811ad/phase-native-restored-20261114/current-positive-complete-ac1-native.json.gz \
  --out notes/2026-11-14-R133-continuous-repair-physical-cap-background-v2-native.json.gz
```

The large positive input is the original exact native restored from its
published lossless parts; its SHA256 is
`ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`.
A replay must choose a fresh output filename. No binary input is
re-encoded into a mathematical surrogate and no primitive is rerun.

The background-only report proves Sections 1--3 and the numerical
transfer bounds in Sections 2 and 6. It deliberately has
`full_residual_sensitive_bridge_proved=false`. Supplying one or more
`--residual` inputs causes the consumer to verify the true complete
cap cover, its exact degree-96 residual support, target identity and
parameter domain before evaluating (C.30). A report with a full bridge
uses the **intersection** of those residual parameter domains; an
$\eta=\eta_0$ residual computation is never promoted to the entire
original $\eta$ interval.

The complete background transfer does retain the whole original
$\eta\in[\eta_0-10^{-9},\eta_0+10^{-9}]$ and every primitive tail.
Neither report proves the negative return inverse, the full finite
head Schur complement, a nonzero $\nu$ scalar determinant, or nonlinear
existence. Those remain genuinely separate global obligations.
