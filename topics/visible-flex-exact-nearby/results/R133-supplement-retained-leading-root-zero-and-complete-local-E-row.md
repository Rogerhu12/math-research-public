# R133 supplement: retained leading root zero in the complete first-local E row

2026-11-15, visible-exact / phase_inverse.

**Proved reduction and conditional scalar-consumer contract.** The successful [direct mixed-jet local result](R133-supplement-actual-direct-genuine-first-local-mixed-jet-bounds.md) bounds the whole genuine first local numerator. Its largest summand budget is the leading $E_{12}$ row. The present refinement retains the exact second-order root zero of its second leading component before taking the canonical derivative. It computes only a new complete bound for that same row and recombines already completed full summand bounds. It does not reevaluate any of the ten successful mixed derivatives, any first-correction coefficient, or an old source integral.

## 1. The exact row and the fixed reference branch

Use the same physical piece2549, fixed intrinsic parameter $\eta_0$, actual common coordinates $(T,X)$, full allowed complex delta square and full scalar-potential square in $z=j^{-2}$. The final operators have real input labels $|j|\ge97$, physical frequency $n=4|j|$, and both carrier signs $\epsilon$.

The exact first-local vector is M.3 and M.20 of [the mixed-jet contract](R133-supplement-direct-genuine-first-local-residual-from-negative-mixed-jets.md). With $w_0=(a_0,b_0)^t$, its leading row is
$$
 E_0=-\mu E_{12}\{2Vw_{0,T}+(V_T+c_TV)w_0\}
 =-\mu\{2Vb_{0,T}+(V_T+c_TV)b_0\}e_1 .
 \tag{ER.1}
$$
The $T$ derivative is taken at fixed canonical $X$, on the same analytic reference branch. It is not an old physical radial derivative. The second component of (ER.1) is exactly zero. The original $V=V_j(T)$, $\mu$, radial leading gauge and all means are retained.

The original leading formula is
$$
 a_0=G(x^2-Ty^2),\qquad b_0=-2i\epsilon Gxy,\qquad
 x=X_\phi,\quad y=T_\phi .
 \tag{ER.2}
$$
In the fixed branch,
$$
 T=-\rho A^{2/3},\qquad
 y=-\frac23\rho A^{-1/3}A_\phi,\qquad
 A_\phi=O(\rho).
 \tag{ER.3}
$$
Here $A$ is the divided fold phase, not a normalized first-transport component. The original $A$ gap and root branch imply the exact analytic factorization
$$
 b_0(T,X)=T^2b_2(T,X).
 \tag{ER.4}
$$
This is the same factorization used in P.17, P.21 and P.24 of [the original regular-transport local contract](R133-supplement-exact-first-local-vector-reduction-through-regular-transport.md). No new zero or zero-mode projection is asserted.

## 2. Why the saved B2 bounds the canonical analytic factor

The original full physical fold product has
$$
 R_G=\frac3{8000},\qquad \Sigma_G=\frac3{128}.
$$
Its frozen producer stores the complete numbers
$$
 |G|\le G_*,\quad |x|\le E_*,\quad |A|\ge A_->0,\quad
 |A_\phi|\le B_A .
$$
The function $A_\phi/\rho$ is removable and has the complete bound $B_A/R_G$ on the same product, by the original first radial zero. Dividing (ER.2)--(ER.3) by $T^2$ as an identity of analytic functions gives
$$
 \left|\frac{b_0}{T^2}\right|
 \le\frac43G_*E_*\,\frac{B_A}{R_G}\,A_-^{-5/3}.
 \tag{ER.5}
$$
The frozen original algorithm uses
$$
 B_A=\frac35a_+D_2R_G\,e^{4D_1R_G},
 \qquad
 B_2=\frac45G_*E_*a_+D_2A_-^{-5/3}e^{4D_1R_G}.
 \tag{ER.6}
$$
Thus its saved field named `B2` is precisely a complete modulus for the analytic factor in (ER.4), not merely a pointwise root estimate. The new consumer reads that saved numerical bound; it does not recompute either formula in (ER.6).

The same original fold proof supplies an analytic inverse into this physical product for
$$
 |T|<R_C=\frac{27}{32000}=\frac{\Lambda R_G}{2},
 \qquad |\operatorname{Im}X|<\Sigma_C=\frac1{64},
 \qquad \Lambda=\frac92 .
 \tag{ER.7}
$$
The original inverse self-map, two contraction rows, phase gap and leading branch gaps remain mandatory. Pulling (ER.5) back by that already paid inverse yields
$$
 |b_2(T,X)|\le B_2
 \quad\hbox{throughout (ER.7)} .
 \tag{ER.8}
$$
This is an analytic continuation of the same leading branch. It is not a complex-angle bound for the full genuine oscillatory column operator.

## 3. A new physical-angle subproduct inside the original canonical product

Keep the exact original negative interval
$$
 I_-=\left[\frac{2147184947341121}{9007199254740992},
               \frac{2383968743003}{10^{13}}\right],
$$
$$
 h=\frac{125978014066294748203}{10995116277760000000000000},
 \qquad
 H=\frac{893368603925465506687}{21990232555520000000000000},
 \qquad 0<h<H<R_G .
 \tag{ER.9}
$$
The root remains in its accepted bracket; all six original negative intersections and the uncertain-root charge remain unchanged.

Read RV's completed bound $T_h$ for $|T|$ on $|\rho|\le h$ and the full physical angle strip $\Sigma_G$. Read its completed positive canonical margin
$$
 d_T=R_C-T_h>0.
 \tag{ER.10}
$$
These are the exact saved `new_complete_negative_T_image_upper` and `complete_leading_T_margin_lower` fields. A consumer uses the stored directed lower endpoint of the latter rather than recreating a different margin.

Choose the new physical output strip
$$
 \Sigma_E=\frac3{256}<\Sigma_G.
 \tag{ER.11}
$$
Let $X_r^*$ be the original full-product saved field `Xr`, which bounds the true physical derivative of the same $X$. The original root anchor is $X(0,\phi)=\phi$. Integration along the radial segment, with $\partial_r=-\partial_\rho$, gives
$$
 |X(\rho,\phi)-\phi|\le hX_r^* .
 \tag{ER.12}
$$
Only its absolute bound is used; there is no change of derivative convention. A new consumer must verify the strict image gate
$$
 \Sigma_E+hX_r^*<\Sigma_C,\qquad T_h<R_C .
 \tag{ER.13}
$$
Consequently every point of the new physical product lies in (ER.7). For fixed such $X$, the $T$ disk needed for Cauchy also lies in the same canonical product. If (ER.13) fails, no new row bound is asserted.

The original scalar-potential image disk must also contain $T_h$. The full delta and $z$ products, input labels, leading normalization and root branch are exactly those of the accepted potential, RV, AJ and M receipts. In particular no bound for $V_j$ at an old radius is substituted for the actual value at $T(\rho,\phi)$.

## 4. Keep the root factor before the canonical derivative

At fixed $X$, differentiate the exact factorization (ER.4):
$$
 2b_{0,T}+c_Tb_0
 =4Tb_2+2T^2b_{2,T}+c_TT^2b_2 .
 \tag{ER.14}
$$
Cauchy on the $T$ disk in (ER.7) gives
$$
 |b_{2,T}|\le\frac{B_2}{d_T},\qquad
 |b_0|\le B_2T_h^2,\qquad
 |2b_{0,T}+c_Tb_0|
 \le B_2\left(4T_h+\frac{2T_h^2}{d_T}+C_TT_h^2\right).
 \tag{ER.15}
$$
All terms vanish to their actual order at the root. In particular the leading derivative is paid as $O(T_h)$ before any old-angle Cauchy estimate.

Here $C_T$ is the complete holomorphic $c_T$ modulus in the accepted AJ domain conclusion. Its original construction used the full physical strip $\Sigma_G$ for $Q,x,y,DQ,d_\phi,T_0,\mu^{-1}$; the smaller $1/256$ strip in that old consumer was needed for its separate regular quotient. The frozen G producer explicitly applies $c_T$'s angular Cauchy bound with $\Sigma_G$. A new consumer pins that source identity and reads AJ's complete holomorphic modulus. A real-circle jet is not substituted for it.

Let $M_\mu$ be M's complete holomorphic $\mu$ modulus on the original $\Sigma_G$ product. Let $M_V,M_{V_T}$ be the complete potential moduli from the accepted $R_0=1/6000$ case. The full potential image gate and (ER.13) imply the complete new first-component bound
$$
 \boxed{\quad
 E_*^{\rm root}
 =M_\mu B_2\left[
 M_V\left(4T_h+\frac{2T_h^2}{d_T}+C_TT_h^2\right)
                  +M_{V_T}T_h^2\right].
 \quad}
 \tag{ER.16}
$$
Its second component remains exactly zero. This bounds the same entire (ER.1); it is not a bound for only its root value or for one term after dropping a radial scalar.

On the real old circle the complete jets satisfy
$$
 e_q^{\rm root}=\frac{q!}{\Sigma_E^q}E_*^{\rm root},
 \qquad q=0,1,2 .
 \tag{ER.17}
$$
For each order one may retain the minimum with M's already successful complete bound of the identical derivative. Both candidates are complete; no differences of upper bounds are used.

Equivalently, the exact physical inverse Jacobian gives
$$
 \mu b_{0,T}=Q(xb_{0,r}-X_rb_{0,\phi}),
 \qquad T_rx-T_\phi X_r=\mu/Q .
 \tag{ER.18}
$$
This verifies that (ER.14)--(ER.17) preserve the physical/canonical derivative distinction. The new consumer does not also evaluate (ER.18) or regenerate the old leading mixed jets.

## 5. Recombine completed full summands, without a subtraction

M's successful output contains eight complete scalar operator bounds for the eight physical summands of M.20. Let $K_\ell$ be the seven saved bounds other than its `leading_E_row`. Their full vectors, signs, means and genuine columns were already paid. They are read byte for byte.

Let $\mathcal A^V$ be the original18-coefficient nonnegative genuine-column functional, including all three profile branches, both input signs and all output means. Insert only
$$
 (e_0^{\rm root},e_1^{\rm root},e_2^{\rm root},0,0,0)
$$
to obtain a complete new $E$-row coefficient $K_E^{\rm root}$. The whole raw first-local operator has the complete new bound
$$
 K_1^{\rm new}
   =\sum_{\ell\ne E}K_\ell+K_E^{\rm root}.
 \tag{ER.19}
$$
Each summand already refers to the same common envelope $|\rho|^{-1/4}$ and the same operator from $H^{-4/3}_{|j|\ge97}$ to $H^{-5/3}$. Therefore ordinary triangle inequality proves (ER.19). There is no need to subtract M's saved $E$ upper bound from M's saved total. There is no lower bound for the true amplitude, residual or operator in this step.

The seven saved diagnostic bounds are used as complete operator bounds, not as an assumed exact decomposition of the previous rounded total. Recombining them is new scalar bookkeeping; their original vectors or positive-functional calculations are not reevaluated.

## 6. The same positive-budget source comparison

Read the original complete numerical local1 coefficient from C and its original whole-term $L^2$ bound from D. As in D.6--D.9 and M.23--M.24, a directed positive lower endpoint $\beta_{\rm old}$ for that actual numerical budget gives
$$
 q=\min\{1,K_1^{\rm new}/\beta_{\rm old}\},\qquad
 L_{1,\rm candidate}=q\,L_{1,\rm original}.
 \tag{ER.20}
$$
The lower endpoint is a lower bound for an original positive algorithm parameter; it is not a function lower bound. The exact outer $J$, six intersections, full physical $dr$, common squared envelope and one-sided uncertain-root charge are unchanged.

Take a minimum only against the latest successful complete bound for the same `local_raw_1` term. Copy the other20 first-row terms and all10 independent physical-mean terms from that latest ledger. If a later complete density-zero SV result is the baseline, its three complete improvements must be retained; reverting them to the older M ledger is not permitted.

Only the local, first and pair aggregates require new scalar recombination. The entire nonlocal and mean aggregates are read unchanged. Physical and reference seams, ordinary source rows, both density windows, input-label powers and all independent means remain in their original places.

## 7. Minimal execution and scope

A new public consumer must check the completed M, RV, AJ, potential, C, D and current-baseline source/manifest/run/runtime/child0 identities; the original fold stage/header/publication; the original canonical inverse product and saved $B_2$; the full $\Sigma_G$ meaning of $C_T,M_\mu$; and the strict new physical image (ER.13). The entire allowed complex coefficient family is preserved.

The only new mathematical quantities are the new physical $X$ image and positive margin, (ER.15)--(ER.17), one complete positive-functional evaluation for $E$, (ER.19), one same-term comparison and three scalar aggregate recombinations. The old fold, intrinsic target, signed Taylor coefficients, all successful mixed derivatives, full leading inverse, potential, transport, column profiles, source rows and radial integrals have recomputation count zero.

Persist only code, parameters, exact identities, run, hashes, actual status/gates and bounded final conclusions. Temporary native and intermediate arrays are not published. An actual strict improvement is claimed only after the public arithmetic and every gate succeed.

This refinement does not change the physical-to-wave readout and does not supply the two-ended high inverse, positive growing-column/source ports, strong-return estimate, unknown core trace or final parameter Schur gate.
