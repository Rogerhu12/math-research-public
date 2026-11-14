# R46 supplement: first-derivative density energy with the full height and mean

**Status: proved for the original complete strict operator, uniformly on
its whole original real parameter box.** An exact change of two-row
variables avoids the large $\mathcal F/\mu$ coefficient in the base
energy. The resulting full strict Cauchy evolution, inverse and
ordinary source retain every angular mode and both mean components.

For the original $L^2$ amplitude frame, on every subinterval of the
actual full strict interval and in either direction,

$$
 \|\mathcal C_{\rm st}\|_0,\quad
 \|\mathcal C_{\rm st}^{-1}\|_0
 <1.594617252\,10^{24}.                                  \tag{HD.1}
$$

The prior complete bound was $6.329524\,10^{50}$. The ordinary
physical scalar source in $L^1(dr;H_{N_0}^{-1/2})$, for the original
$N_0=2^{20}$, has complete original-amplitude output bound

$$
 \|\mathcal S_{\rm st}f\|_0
 <6.784778349\,10^{19}\|f\|_{L^1(dr;H_{N_0}^{-1/2})}.       \tag{HD.2}
$$

These bounds are proved using all original 215 positive native
closed cells and their exact reflection. No geometry is recomputed.
They do not yet update the higher density bootstrap, strict strong
remainder, complete returned $R_*$ or final finite head.

## 1. The exact original Hamilton system

Write the original real scalar equation as

$$
 P u=\partial_r(a u_r+b u_\theta)
     +\partial_\theta(bu_r+c u_\theta)+d u=f.
$$

On the proved strict interval,
$a>0$, $\mu=(b^2-ac)^{1/2}>0$ and

$$
 p=a u_r+b u_\theta,\qquad
 \alpha=a^{-1},\quad v=b/a,\quad
 \nu=\mu/a,\quad\gamma=\mu^2/a.
$$

The exact first-order equations are

$$
 u_r=\alpha p-vu_\theta,\qquad
 p_r=\partial_\theta(\gamma u_\theta-vp)-d u+f.            \tag{HD.3}
$$

The coefficient $d$ is the original full
$\tau+\partial_\theta\sigma$, including its nonradial correction.
The named native field `kappa` is $-K_{\rm target}$; it is not used
as a substitute for any coefficient in (HD.3).

Put $\ell=\log\mu$ and introduce the unshifted states

$$
 z=\sqrt\mu\,u_\theta,\qquad t=p/\sqrt\mu,
 \qquad Y_\sigma=(z+\sigma t)/\sqrt2.                    \tag{HD.4}
$$

These use the original momentum $p$. No zero-order shear is put
inside (HD.4). Direct differentiation of (HD.3) gives

$$
 \begin{pmatrix}z\\t\end{pmatrix}_r
 =\begin{pmatrix}-v&\nu\\\nu&-v\end{pmatrix}
                  \begin{pmatrix}z\\t\end{pmatrix}_\theta
 +\begin{pmatrix}
  \ell_D/2-v_\theta&\nu_\theta-\nu\ell_\theta/2\\
  \nu_\theta+\nu\ell_\theta/2&-\ell_D/2-v_\theta
 \end{pmatrix}\begin{pmatrix}z\\t\end{pmatrix}
 +\binom0{(f-du)/\sqrt\mu},
                                                               \tag{HD.5}
$$

where $\ell_D=\ell_r+v\ell_\theta$. In deriving the off-diagonal
entries one uses exactly
$\mu\alpha_\theta=\nu_\theta-\nu\ell_\theta$ and
$\gamma_\theta/\mu=\nu_\theta+\nu\ell_\theta$.

Consequently the two true density transports are

$$
 \boxed{
 (Y_\sigma)_r+\partial_\theta[(v-\sigma\nu)Y_\sigma]
   =\tfrac12[\ell_r+(v+\sigma\nu)\ell_\theta]Y_{-\sigma}
      +\frac{\sigma(f-du)}{\sqrt{2\mu}}.}
                                                               \tag{HD.6}
$$

The accompanying exact height equation is

$$
 u_r+v u_\theta=\frac{\nu}{\sqrt{2\mu}}(Y_+-Y_-).         \tag{HD.7}
$$

Only first density derivatives occur. In particular no second
radial derivative of $\log\mu$ and no $\mathcal F/\mu$ occur.
This is an exact different state representation of the same PDE;
the original density potential is not set to zero.

## 2. The exact Hermitian cancellation

Let $\lambda>0$ be a **constant** height weight and set

$$
 \mathcal E_\lambda(u,p)^2
  =\int\left(\lambda|u|^2+\mu|u_\theta|^2+|p|^2/\mu\right)
  =\|\sqrt\lambda u\|_2^2+\|Y_+\|_2^2+\|Y_-\|_2^2.        \tag{HD.8}
$$

The positive height term controls the independent mean height;
the momentum term controls mean flux. Neither is reconstructed
by a zero-mean antiderivative or discarded.

For $X=(\sqrt\lambda u,Y_+,Y_-)^t$, integration by parts in the
periodic physical angle gives the exact homogeneous derivative
$\partial_r\mathcal E_\lambda^2=\int X^*\mathsf H X$, with

$$
 \mathsf H=
 \begin{pmatrix}
 v_\theta & h &-h\\
 h&-v_\theta+\nu_\theta&\ell_D\\
 -h&\ell_D&-v_\theta-\nu_\theta
 \end{pmatrix},\qquad
 h=\frac{\lambda\nu-d}{\sqrt{2\lambda\mu}}.               \tag{HD.9}
$$

The $+\nu\ell_\theta$ and $-\nu\ell_\theta$ terms in (HD.6)
cancel in the Hermitian cross entry. Keeping them separately by
absolute values would lose this identity. The norm of the remaining
height-to-wave off-diagonal block is
$|\lambda\nu-d|/\sqrt{\lambda\mu}$.

The two stored true real characteristic rates on a native cell bound
$\max(0,-v_\theta+|\nu_\theta|)$ and
$\max(0,v_\theta+|\nu_\theta|)$ respectively. Their maximum
$\chi$ therefore bounds the absolute value of each diagonal entry
in (HD.9), in both time directions. Hence

$$
 \|\mathsf H\|\le
 \chi+|\ell_r+v\ell_\theta|
       +\frac{|\lambda\nu-d|}{\sqrt{\lambda\mu}}.          \tag{HD.10}
$$

For the source, (HD.6) adds a vector of length $|f|/\sqrt\mu$.
Writing $g$ for the right side of (HD.10) gives the full estimate

$$
 \frac d{dr}\mathcal E_\lambda
 \le\tfrac12g\mathcal E_\lambda+\|f/\sqrt\mu\|_2,         \tag{HD.11}
$$

with the corresponding reversed inequality for evolution in the
other direction. This contains the whole ordinary scalar source.
No weak divergence load is renamed as that scalar input.

The identities first hold for smooth consistent data. The augmented
three-state system has real diagonal transport principal part in
$(u,Y_+,Y_-)$ and a bounded zero-order matrix on every closed strict
interval. Its usual energy completion gives a full propagator.
The constraint $u_\theta=(Y_++Y_-)/\sqrt{2\mu}$ is preserved by
(HD.6)–(HD.7), so consistent completed data give exactly (HD.3).
The original scalar-germ joins use continuous actual coefficients
and states; no new jump or radial derivative across an unpaid knot
is inserted in this argument.

## 3. Pay (HD.10) from the existing complete native fields

On each original positive closed cell $I_i$, let $M_f$ be its
proved complete field modulus and $\mu_{i,-}>0$ its proved density
lower bound. We use

$$
 |\ell_D|\le M_{L_r}+M_vM_{L_\theta},\qquad
 \frac{|\lambda\nu-d|}{\sqrt{\lambda\mu}}
 \le\frac{\sqrt\lambda M_\nu+M_d/\sqrt\lambda}
          {\sqrt{\mu_{i,-}}}.                            \tag{HD.12}
$$

Here $L_r,L_\theta$ are precisely the full first derivatives of
$\log\mu$ evaluated in the original native field proof. The exact
reflection pays both halves by doubling their positive-cell lengths.
All real parameter and closed angle errors of those certificates
remain in (HD.12).

The directed complete integrals on $[-r_c,r_c]$ are

$$
 \int\chi<39.445296981,\qquad
 \int|\ell_D|<10.847484872,
$$
$$
 \int\frac{|\nu|}{\sqrt\mu}<2.791938217,
 \qquad
 \int\frac{|d|}{\sqrt\mu}<25.783406674.                  \tag{HD.13}
$$

Choose the exact constant $\lambda=9$. Equations (HD.10)–(HD.13)
give

$$
 L_E=\tfrac12\left(\int\chi+\int|\ell_D|
        +3\int|\nu|/\sqrt\mu+\tfrac13\int|d|/\sqrt\mu\right)
 <33.631532697,
$$
$$
 G_E=e^{L_E}<4.036352328\,10^{14}.                        \tag{HD.14}
$$

For comparison the prior base-energy exponent was
$79.478945657$. The actual field identities and finite-height
weight, rather than an omission of any mode, produce the smaller
exponent. The new argument never estimates its energy using the
old integrated density-potential modulus $113197.898279$.

The full density range used is
$\mu_->.1113999328238585$ and $\mu_+<1.787992986267$.
Every subinterval and both directions consequently have homogeneous
energy gain $G_E$ and ordinary $L^1L^2$ source-to-energy gain

$$
 G_E/\sqrt{\mu_-}<1.209334949\,10^{15}.                  \tag{HD.15}
$$

## 4. Full physical Sobolev states and their flux duals

Use the normalized angle $x=4\theta$ and any auxiliary integer
$N\ge1$. Put
$\mathcal P_N^s=H_N^{s+1/2}\oplus H_N^{s-1/2}$ for $(u,p)$.
The full positive-half energy comparison is

$$
 h_-\|(u,p)\|_{\mathcal P_N^{1/2}}^2
 \le\mathcal E_9^2
 \le h_+\|(u,p)\|_{\mathcal P_N^{1/2}}^2,
$$
$$
 h_- =\min(9,16N^2\mu_-,1/\mu_+),\qquad
 h_+=\max(9,16N^2\mu_+,1/\mu_-).                         \tag{HD.16}
$$

The factor $16N^2$ is required since
$\partial_\theta=4\partial_x$. It has not been removed by
calling the norm scaled. Thus the true positive-half Cauchy norm
is bounded by

$$
 C_N=G_E\sqrt{h_+/h_-}.                                  \tag{HD.17}
$$

The same bound holds in reverse time. The exact original Green
flux $\int(u\bar p'-p\bar u')$ identifies the dual of the
positive-half state with $\mathcal P_N^{-1/2}$. Applying the
reverse propagator and taking its actual flux adjoint therefore
pays the negative-half bound with the same constant. Interpolation
gives every $-1/2\le s\le1/2$, including $s=0$.

At $N=1$, $C_1<2.886787861\,10^{15}$. At $N=2^{20}$ it is
$<3.027016468\,10^{21}$. The source injection $(0,f)$ has norm
one from $H_N^{-1/2}$ to $\mathcal P_N^0$, so Duhamel bounds the
whole $L^1(dr;H_N^{-1/2})\to\mathcal P_N^0$ source by $C_N$.
The sharper positive-half $L^1L^2$ source constant is separately
$G_E/\sqrt{\mu_-h_-}$; it is not substituted at a different index.

## 5. Recover the original full amplitude frame with actual first jets

Let $m=\mu^{-1/2}$ and keep the original full normal shear $T$.
After a constant unitary Hadamard change in the amplitudes the
exact frame is

$$
 (r,t)\longmapsto
 \binom{m\Lambda^{-1/2}r}
 {-Tm\Lambda^{-1/2}r+i\sqrt\mu\Lambda^{1/2}t},
 \qquad\Lambda_n=\max(1,4|n|).                           \tag{HD.18}
$$

Its inverse is
$r=\Lambda^{1/2}\sqrt\mu\,u$ and
$t=-i\Lambda^{-1/2}(mp+Tm\,u)$. These formulas include the
original mean matrices. The large radial shear is recovered exactly;
it was not dropped when using the energy (HD.8).

For a real multiplier $f$ with complete real bounds
$\|f\|_\infty\le M$ and $\|f_x\|_\infty\le D$, the normalized
derivative pair at order one has comparison matrix

$$
 \begin{pmatrix}M&0\\D/N&M\end{pmatrix}.
$$

Its exact norm is
$m_1=(\sqrt{(D/N)^2+4M^2}+D/N)/2$. Duality and interpolation
therefore bound multiplication at both half indices by

$$
 m_{1/2}=\sqrt{M m_1}.                                   \tag{HD.19}
$$

The native first jets pay the three multipliers in (HD.18)
without a generic strip derivative loss:

$$
 |m_x|\le m|L_\theta|/8,\quad
 |(\sqrt\mu)_x|\le\sqrt\mu|L_\theta|/8,
$$
$$
 |(Tm)_x|\le m|T_\theta|/4+Tm|L_\theta|/8.                \tag{HD.20}
$$

The combined coefficient $Tm$ is treated before taking its norm.
No derivative of a product is omitted. For all $N\ge1$ and every
mode, including zero, $J_N\le\Lambda\le4NJ_N$. Thus if
$M_m,M_r,M_{Tm}$ are the half-multiplier bounds, both the full
frame and its inverse are bounded by the same exact matrix norm

$$
 F_N=\left\|\begin{pmatrix}M_m&0\\M_{Tm}&\sqrt{4N}M_r\end{pmatrix}\right\|_2.
                                                               \tag{HD.21}
$$

The inverse interchanges the two diagonal entries; the trace and
determinant of its squared singular-value matrix are unchanged.
The original amplitude norm at index zero is independent of the
auxiliary $N$. Hence every $F_N^2C_N$ is a bound for the same
complete amplitude propagator. The executed choices include
$N=1,4,16,64,256,1024,4096,65536,2^{20}$, and $N=1$ gives

$$
 F_1<23502.864350,
 \quad F_1^2C_1<1.594617252\,10^{24},
 \quad F_1C_1<6.784778349\,10^{19}.                       \tag{HD.22}
$$

This proves (HD.1). The final bound is the source map to the
original amplitude from $L^1H_1^{-1/2}$. Since $M\le N$ implies
$H_N^{-1/2}\hookrightarrow H_M^{-1/2}$ with norm one, it also
proves (HD.2) for $N_0=2^{20}$ and every larger declared input
norm scale. The original output amplitude is unchanged.

## 6. Keep the former density bootstrap as an available exact interface

The higher-order scalar-density representation remains useful
because its antiderivative gains one angular order. The present
base estimate supplies it without charging the large second
density derivative in a new exponential.

For the original variables
$w=\sqrt\mu u$, $\zeta=(p+Tu)/\sqrt\mu$ and
$y_\sigma=(w_\theta+\sigma\zeta)/2$, exact comparison with (HD.8)
gives

$$
 |\langle w\rangle|\le W_E\mathcal E_9,
 \qquad \|(y_+,y_-)\|_2\le Y_E\mathcal E_9,
$$
$$
 W_E=\sup\sqrt\mu/3<.445719516471,
$$
$$
 Y_E=\sup\left[\frac12\left(1+
      \frac{\mu L_\theta^2/4+T^2/\mu}{9}\right)\right]^{1/2}
 <2809.927411.                                          \tag{HD.23}
$$

For the second inequality the matrix to $(w_\theta,\zeta)$ is
the identity on $(z,t)$ plus the single height column
$(\sqrt\mu L_\theta/2,T/\sqrt\mu)/3$; its largest squared
singular value is one plus the squared length of that column.
The extra factor $1/\sqrt2$ converts to the original $y$ pair.

For initial data in $\mathcal P_N^{1/2}$ the full initial
mean/density columns are therefore $W_EG_E\sqrt{h_+}$ and
$Y_EG_E\sqrt{h_+}$. For ordinary $L^1L^2$ source they are
$W_EG_E/\sqrt{\mu_-}$ and $Y_EG_E/\sqrt{\mu_-}$.
All four are explicitly saved at each comparison scale. The mean
height and mean flux are genuine parts of these estimates; the
actual high/low paths are not compressed.

## 7. Native execution and scope

The new light consumer is
`scripts/fourfold_strict_unshifted_half_density_energy.py`.
It uses the existing complete field, old density and original
strong-word reports, checking their source/dependency/input hashes
and the exact whole-family identity. Its source SHA256 is
`c3cbe27ced54bb5ab707694177ed97f76840bbe52914841df9fac6a29eb34794`.

All four gates passed. The completed report is
`notes/2026-11-13-R46-unshifted-half-density-energy.json`, SHA256
`ebe435c41b5337b3f92aeadfc132ae173e459c54d2cfd9befaeaadf5afad384e`.
It contains each of the 215 true closed-cell contributions, all
global integrals, the exact fixed height weight, complete half-jet
multiplier bounds, both frame directions, physical/source estimates
at every scale, and the four full original-density interface columns.

```sh
python3 scripts/fourfold_strict_unshifted_half_density_energy.py \
  --out /tmp/unshifted-half-density-energy.json
```

This conclusion changes the actual base Cauchy estimate through a
proved energy identity and recovers the complete original frame.
It does not by itself update the higher-density staircase or strong
WKB residual, solve the returned finite head, or transfer these
numerical constants to the new nonlinear body or deep-tail object.
