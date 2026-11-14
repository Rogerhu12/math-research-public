# R46 supplement: the actual high density phase and a two-window order-two remainder

**Proved for the original complete strict operator, all its real parameter
values, and the same two separate fixed characteristic labels.**
Let \(T_H(t,s)\) denote the full infinite-dimensional high Volterra
propagator constructed in
[the fixed-label density theorem](R46-supplement-actual-fixed-label-high-density-Volterra.md).
For every pair of strict times, in either direction,

$$
T_H(t,s)
=I+\operatorname{diag}_{\sigma=\pm}
 \left(iP_HM_{A_\sigma(t,s)}D^{-1}P_H\right)+R_H(t,s),
\qquad
A_\sigma(t,s)={\sigma\over8}
 \int_s^t H_\sigma'(\kappa\circ H_\sigma)\,dr .             \tag{P.1}
$$

Each \(A_\sigma\) is the actual real, nonconstant phase function. No angular
average or frozen ray is substituted. The complete remainder has both
windows

$$
R_H:H_N^0\longrightarrow H_N^2,\qquad
R_H:H_N^{-2}\longrightarrow H_N^0 .                       \tag{P.2}
$$

The displayed spaces are two-component high label spaces, with
\(P_H=1_{\{|n|\ge N\}}\), \(D=-i\partial_x\), and
\(\|u\|_{H_N^s}=\|(1+D^2/N^2)^{s/2}u\|_2\).
All frequencies in this infinite high space are included.
The low-label time histories and the two independent scalar means
remain external inputs. This theorem does **not** identify a new complete
returned remainder after their feedback, nor replace the independently
proved final circle phase.

## 1. Exact high generator and its actual diagonal phase

Retain the original density variables, physical \(dr\), source \(f\),
and \(x=4\theta\) from the preceding theorem:

$$
\kappa={\mathcal F\over\mu},\quad
\nu={\mu\over a},\quad v={b\over a},\quad
\mathcal D_{H_\sigma}=H_\sigma'C_{H_\sigma}=(C_{S_\sigma})^*,
\quad S_\sigma=H_\sigma^{-1}.
$$

For prescribed complete low history the high equation is

$$
X_H'=KX_H+F_H,\qquad
K_{\sigma\tau}={i\sigma\over8}
 P_H\mathcal D_{H_\sigma}M_\kappa C_{S_\tau}D^{-1}P_H .
                                                               \tag{P.3}
$$

The projection on the right is in the actual \(\tau\)-label and the
projection on the left is in the actual \(\sigma\)-label. In particular,
neither projection is moved through a pullback.
On the same branch,

$$
\mathcal D_{H_\sigma}M_\kappa C_{S_\sigma}
=M_{H_\sigma'(\kappa\circ H_\sigma)}.                    \tag{P.4}
$$

Thus the time integral of the diagonal part of \(K\) is exactly the
first-order term in (P.1), including its real nonconstant coefficient.
This is an exact fixed-label identity before any approximation.

The previously proved all-time bounds are

$$
C_r^{-1}\le H_\sigma',S_\sigma'\le C_r,\qquad
C_r<14.983653,
$$

with a separate complex derivative bound \(C_c<36.730914\) on
normalized width \(X=2.7952875\,10^{-5}\).
These real and complex permissions are kept distinct.
The complete density integral is

$$
Q_\kappa=\sum_{I>0}2|I|\,{M_{\mathcal F,I}\over\mu_{-,I}}
<113197.898280.                                          \tag{P.5}
$$

It follows in particular that
\(\|A_\sigma(t,s)\|_\infty\le C_rQ_\kappa/8\).
This is a bound on the full actual function, not a value for its mean.

## 2. The cross-branch oscillation and its two exact endpoint columns

For \(\tau=-\sigma\), put

$$
F_{\sigma\tau}=S_\tau\circ H_\sigma,\qquad J_\sigma=H_\sigma'.
$$

Since \(H_{\sigma,r}=4(v-\sigma\nu)\circ H_\sigma\), the actual relative
phase has

$$
(F_{\sigma\tau})_r
=-8\sigma\,{\nu\circ H_\sigma\over J_\tau\circ F_{\sigma\tau}} .
                                                               \tag{P.6}
$$

The real \(\nu=\mu/a\) is strictly positive in the original strict chart.
There is consequently no stationary cross-branch phase.
Its reciprocal is bounded directly by
\(C_r\sup(a/\mu)/8\); the consumer records this full finite bound.
No unproved complex gap for a relative inverse flow is needed below.

Define the exact cleared coefficient and the material derivative

$$
R={\kappa\over\nu}={a\mathcal F\over\mu^2},\qquad
Q_\sigma=R_r+(v-\sigma\nu)R_\theta+2v_\theta R .            \tag{P.7}
$$

The \(\theta\)-derivatives in this formula are physical angular
derivatives. The factors of four have already cancelled against
\(\partial_x=\partial_\theta/4\).
The equality \(R=a\mathcal F/\mu^2\) makes its entire complex
coefficient domain explicit.

Consider the two actual order-two endpoint operators

$$
L_{\sigma\tau}(r)
=-{1\over64}P_H\mathcal D_{H_\sigma}
 M_R C_{S_\tau}M_{J_\tau}D^{-2}P_H ,\qquad \tau=-\sigma .
                                                               \tag{P.8}
$$

The last multiplier \(J_\tau\) is in the original fixed \(\tau\)-label.
It is not the Eulerian Jacobian at the other end.
Both cross branches have the same minus sign in (P.8).
Define also

$$
\begin{split}
Z_{\sigma\tau}(r)
={}&-{1\over64}P_H\mathcal D_{H_\sigma}
 M_{Q_\sigma}C_{S_\tau}M_{J_\tau}D^{-2}P_H\\
&+{\sigma\over8}P_H\mathcal D_{H_\sigma}
 M_\kappa C_{S_\tau}M_{J_\tau'/J_\tau}D^{-2}P_H .
\end{split}                                               \tag{P.9}
$$

The prime on \(J_\tau\) in the last line is a label derivative.
Then

$$
\boxed{\quad K_{\sigma\tau}=\partial_rL_{\sigma\tau}
                    -Z_{\sigma\tau},\qquad \tau=-\sigma.\quad} \tag{P.10}
$$

Here is a direct verification, including the density terms.
In the \(\sigma\)-label the coefficient before
\(C_FD^{-2}\) in (P.8) is

$$
B=-{1\over64}J_\sigma(J_\tau\circ F)(R\circ H_\sigma).
$$

Using \(\partial_r(C_FD^{-2})=iM_{F_r}C_FD^{-1}\), equation
(P.6) gives \(iBF_r=i\sigma J_\sigma(\kappa\circ H_\sigma)/8\),
the complete cross generator (P.3).
For its coefficient derivative,

$$
(J_\sigma)_r=(v_\theta-\sigma\nu_\theta)\circ H_\sigma\,J_\sigma,
$$

$$
\partial_r[J_\tau(r,F)]
=(v_\theta-\tau\nu_\theta)\circ H_\sigma\,(J_\tau\circ F)
 +(J_\tau'\circ F)F_r.
$$

The two first terms add to \(2v_\theta\), while the last term uses
\(R\nu=\kappa\) and produces the second line of (P.9).
The derivative of \(R(r,H_\sigma)\) is
\([R_r+(v-\sigma\nu)R_\theta]\circ H_\sigma\).
This proves (P.9)--(P.10) with all signs and all scalar-density factors.

The original coefficient regularity gives absolute continuity across
the common scalar germs; the piecewise first derivatives are integrable.
There is no jump term when the original 215-cell cover is joined.
For every subinterval,

$$
\int_s^tK_{\rm cross}(r)\,dr
=L_{\rm cross}(t)-L_{\rm cross}(s)-\int_s^tZ_{\rm cross}(r)\,dr .
                                                               \tag{P.11}
$$

Thus both endpoints, not only the entering one, remain in the model error.
Equation (P.11) integrates the first Born operator against a fixed test
input. Higher interactions, including what would be an \(LX'\) term
if one integrated the full equation by parts, are kept by the exact
Duhamel treatment in Section 5.

## 3. All coefficients are paid from the complete existing native fields

On each original continuous cell use its full complex moduli,
its first \(r,\theta\) derivatives, and its positive \(\mu_-\).
With \(M_F=M_{\mathcal F}\), one may take

$$
M_R={M_aM_F\over\mu_-^2},
$$

$$
M_{R_\ell}
={M_{a_\ell}M_F+M_aM_{F_\ell}\over\mu_-^2}
 +{2M_aM_FM_{\mu_\ell}\over\mu_-^3},
\quad \ell=r,\theta,
$$

$$
M_Q=M_{R_r}+(M_v+M_\nu)M_{R_\theta}+2M_{v_\theta}M_R .
                                                               \tag{P.12}
$$

These are bounds on the entire original normalized field strip
\(s_f=1/160\), before Cauchy differentiation.
The full new consumer obtains

$$
\sup M_R<6311285327.05,\qquad
Q_Q:=\sum_{I>0}2|I|M_{Q,I}<38440031743.8 .                 \tag{P.13}
$$

No new native coefficient computation is performed.
The identity and SHA checks require the same complete 215 cells,
their exact reflection, the same affine parameter interval and
the same density Volterra report.
The geometry field named kappa, which means \(-K_{\rm target}\),
is again not used in place of \(\mathcal F/\mu\).

For the real label Jacobian and its logarithmic derivative set

$$
h_2={C_c\over X/2},\quad h_3={2C_c\over(X/2)^2},\quad
h_4={6C_c\over(X/2)^3}.
$$

The following complete real derivative bounds are sufficient:

$$
(J,J',J'')\preceq(C_r,h_2,h_3),
$$

$$
\left({J'\over J},
 \partial_x{J'\over J},
 \partial_x^2{J'\over J}\right)
\preceq
\left(C_rh_2,\ C_rh_3+C_r^2h_2^2,\
 C_rh_4+3C_r^2h_3h_2+2C_r^3h_2^3\right).                 \tag{P.14}
$$

This uses the true real lower bound for \(J\) and Cauchy bounds for
its higher derivatives. It does not assert a stronger complex
lower bound for \(J\).
For a function with known derivative moduli \(f_0,\ldots,f_j\),
the complete scaled multiplication matrix is

$$
\mathsf M^{[j]}_{ab}
=\binom ab\,{f_{a-b}\over N^{a-b}}\quad(0\le b\le a\le j).
                                                               \tag{P.15}
$$

Conjugate it by
\(W_j=\operatorname{diag}\sqrt{\binom j0},\ldots,\sqrt{\binom jj}\)
and take the full directed matrix bound.
Let \(m_{J,j}\) and \(m_{\log J,j}\) denote the bounds obtained from
(P.14). Let \(p_j,d_j\) be the already paid scalar and density pullback
bounds from (H.20), and let \(u_j=M_{j,N}(1,s_f)\) be the complete
analytic multiplier bound. In particular \(p_0=d_0=\sqrt{C_r}\),
\(u_0=1\), \(m_{J,0}=C_r\).

For later use define finite constants

$$
E_j={d_jp_ju_jm_{J,j}\over64}\sup M_R,
\qquad
Z_j=d_jp_ju_j
 \left({m_{J,j}Q_Q\over64}+{m_{\log J,j}Q_\kappa\over8}\right).
                                                               \tag{P.16}
$$

No scalar coefficient was commuted past a Fourier multiplier to obtain
these product bounds.
The off-diagonal two-by-two operator norm is the maximum of its two
cross entries, so there is no gratuitous extra factor two here.

## 4. Both strong windows of the first cross integral

In the high label,

$$
\|D^{-2}P_H\|_{L^2\to L^2}\le N^{-2},\qquad
\|D^{-2}P_H\|_{L^2\to H_N^2}\le2N^{-2}.
$$

For the forward window, apply the full \(H_N^2\) bounds to all factors
to the left of this rightmost primitive in (P.8)--(P.9).
For the opposite window, take the adjoint: its primitive is leftmost,
so all the factors to its right need only their base bounds.
Consequently the complete cross integral \(C(t,s)=\int_s^tK_{\rm cross}\)
satisfies

$$
\|C\|_0\le c_0:=
\min\left\{{k_0\over2},{2E_0+Z_0\over N^2}\right\},
$$

$$
\|C\|_{0\to2}\le c_+:={2(2E_2+Z_2)\over N^2},\qquad
\|C\|_{-2\to0}\le c_-:={2(2E_0+Z_0)\over N^2},
\quad k_0={C_rQ_\kappa\over4N}.                           \tag{P.17}
$$

The alternative \(k_0/2\) follows by bounding just the two cross
entries of (P.3), not its full four-entry matrix.
These inequalities hold uniformly for all subintervals and both
orientations. In particular they can be used inside the ordinary
source integral.

## 5. The entire higher Born series without a high-order Cauchy exponential

Write \(G_0=e^{k_0}\), the already paid complete base propagator bound.
The one-order gains of the actual generator are bounded by

$$
k_j^+={\sqrt2\,d_jp_ju_jQ_\kappa\over4N},\qquad
k_j^-={\sqrt2\,d_{j-1}p_{j-1}u_{j-1}Q_\kappa\over4N},
\quad j=1,2 .                                           \tag{P.18}
$$

The plus bound applies to \(K:H_N^{j-1}\to H_N^j\), since the
primitive is rightmost. The minus bound applies to
\(K^*:H_N^{j-1}\to H_N^j\), since its primitive is leftmost.
The latter is the reason the opposite window is much cheaper.
Both are estimates of the complete matrix, including its diagonal.

Let
\(B_{\ge2}(t,s)=T_H(t,s)-I-\int_s^tK\).
There are two exact Duhamel expansions:

$$
B_{\ge2}
=\int_{s\le u\le v\le t}
       K(v)K(u)T_H(u,s)\,du\,dv ,
$$

$$
B_{\ge2}
=\int_{s\le u\le v\le t}
       T_H(t,v)K(v)K(u)\,du\,dv .                         \tag{P.19}
$$

The first puts the base propagator on the right for the forward window;
the adjoint of the second puts its adjoint on the right for the opposite
window. Hence no \(H_N^2\) Cauchy norm is silently inserted.
The two ordered coefficient integrals give the actual factor \(1/2\):

$$
b_0=e^{k_0}-1-k_0\le{k_0^2e^{k_0}\over2},\qquad
b_+={k_2^+k_1^+G_0\over2},\qquad
b_-={k_2^-k_1^-G_0\over2}.                              \tag{P.20}
$$

The proof remains valid in reversed time after reversing the ordered
simplex. The consumer uses the minimum of the two rigorous positive
base formulas in (P.20).

Combining (P.4), (P.11), and (P.19) proves (P.1) with

$$
\boxed{\quad
\|R_H\|_0\le r_0=c_0+b_0,\quad
\|R_H\|_{0\to2}\le r_+=c_++b_+,\quad
\|R_H\|_{-2\to0}\le r_-=c_-+b_- .
\quad}                                                  \tag{P.21}
$$

Interpolation gives, for the same complete remainder,

$$
\|R_H\|_{0\to4/3}\le r_0^{1/3}r_+^{2/3},\qquad
\|R_H\|_{-4/3\to0}\le r_0^{1/3}r_-^{2/3}.                 \tag{P.22}
$$

This is an actual two-window strong estimate for this high interior
operator. It is not inferred from a small truncated matrix.

## 6. Numerical bounds and complete affine source columns

Selected directed bounds from the consumer are:

| High label cutoff \(N\) | \(r_0\) | \(r_+\), \(0\to2\) | \(r_-\), \(-2\to0\) |
|---:|---:|---:|---:|
| \(2^{20}\) | \(0.296190\) | \(1.183021\,10^{10}\) | \(164.024500\) |
| \(2^{30}\) | \(7.474699\,10^{-6}\) | \(2.559053\) | \(4.986298\,10^{-5}\) |
| \(2^{40}\) | \(7.128419\,10^{-12}\) | \(2.394215\,10^{-6}\) | \(4.749905\,10^{-11}\) |

The large forward constant at \(2^{20}\) is an explicit cost of the
current higher real flow-jet bounds. It is not replaced by the much
smaller opposite constant.
These displayed cutoffs are for the present conditional interior
statement; they are not claimed to be final return cutoffs.

For the same prescribed complete low history the affine solution is
exactly

$$
X_H(t)=T_H(t,s)X_H(s)
        +\int_s^tT_H(t,r)F_H(r)\,dr,                     \tag{P.23}
$$

$$
(F_H)_\sigma={\sigma\over2}
 P_H\mathcal D_{H_\sigma}(mf-\kappa w_L).
$$

Inserting (P.1) in both places of (P.23) retains the identity source
term, its full actual phase term, and the complete remainder source
term. The high projections stay in exactly the positions in (P.3).
No independent mean or low path is discarded.

For the \(0\to2\) error source column, the ordinary physical
\(L^1(dr;L^2)\) source and the full
\(L^\infty(dr;L^2)\) low height history have bounds

$$
r_+{\sqrt{C_r}M_m\over\sqrt2},\qquad
r_+{\sqrt{C_r}Q_\kappa\over\sqrt2}.                       \tag{P.24}
$$

For the \(-2\to0\) column the corresponding source spaces are
\(L^1(dr;H_N^{-2})\) and \(L^\infty(dr;H_N^{-2})\).
Since \(\mathcal D_H^*=C_S\), their bounds are

$$
r_-{p_2M_{2,N}(M_m,s_f)\over\sqrt2},\qquad
r_-{p_2u_2Q_\kappa\over\sqrt2}.                          \tag{P.25}
$$

This uses the scalar positive-window bound \(p_2\), not an unjustified
positive-window density bound in the negative source space.
The actual \(m\), full scalar source \(f\), physical radial measure
and whole parameter interval are unchanged.
The two mean equations, all high-to-low columns and the exact
\(u=mw,\ p=\sqrt\mu\,\zeta-Tu\) reconstruction remain those
of (H.6)--(H.14), (H.28)--(H.29).

## 7. Scope and reproduction

The producer is scripts/fourfold_actual_high_density_first_phase.py,
and the complete output is
notes/2026-11-13-actual-high-density-first-phase-two-window.json.
It checks its complete native inputs and dependencies, pays (P.12)
on every original closed cell, and records every coefficient, matrix,
source column and both strong windows.

~~~bash
python3 scripts/fourfold_actual_high_density_first_phase.py \
  --out notes/2026-11-13-actual-high-density-first-phase-two-window.json
~~~

The output path must be fresh.
The native cells, true flows, primitive tails and full parameter
interval have not been recomputed or changed.
What remains before this can improve the full return certificate is
the actual low-history feedback, all physical root/cap port maps in
the same high-label split, and the complete final circle reconstruction.
Those obligations are not supplied by the present high-only
propagator or by a small number in its base column.

