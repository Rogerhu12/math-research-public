# R133 supplement: a single complete root first-symbol trial and its ordered waist error

2026-11-16, visible-exact / tail_connector.

**A new analytic candidate, with a current-only scalar recipe.** This note replaces the product of the cut first symbol and the strict transported first symbol by their single complete root coefficient. It retains the actual second normalizer, all three finite primitive defects, both physical means, every interface, and both endpoint corrections. The new trial agrees exactly with the existing FA first-order map at the strict cut. No new numerical bound is asserted here. All successful SF/SJ, FA, WX, CG, WT, WE and UT calculations remain frozen.

The final comparison is between complete paid strong-error bounds for the same individually normalized branch operators. Two different trial errors are not compared directly. The six retained rows of WE/UT remain unpaid in their original exact form; no complete incoming inverse, finite Schur inverse, nonlinear state or full return is obtained.

## 1. Fixed objects and the complete first coefficient

Use exactly the real repaired family, intrinsic parameter and strict interval of [SF](R133-supplement-complete-strict-first-symbol-propagation-defect.md):
$$
Q_\delta=\bar Q+\delta Z_{\rm can},\qquad |\delta|\le10^{-8},\qquad
0\le r\le r_c=\frac{76285779072683}{320000000000000}.
\tag{SW.1}
$$
The circle has period $\pi/2$, physical frequencies $4j$, normalized measure, and
$I=\partial_\phi^{-1}P$, $P=1-\Pi$. The original root input is
$\mathcal X_{97}^s=P_{97}H^s$, with $P_{97}$ selecting $|j|\ge97$.
It contains both Fourier signs. All two-wave spaces use the Hilbert component norm. The two independent physical mean coordinates are additional coordinates of
$\mathcal Y=L^2_{\ne0}(\mathbb T;\mathbb C^2)\oplus\mathbb C^2$.

Keep SF.4--18 verbatim. In particular
$$
L_0=M_{C_{\rm vel}}\partial_\phi+M_{(C_{\rm vel})_\phi}
                 +\ell_0,\quad
L_d=L_0+M_aI,\quad
T=T_1T_2=(1+SI)(1+ZI^2),
\tag{SW.2}
$$
where $a=\operatorname{diag}(a_+,a_-)$ is the complete S.12 / SF.15 diagonal coefficient, $C_{\rm vel}=\operatorname{diag}(d+\sigma\eta q)$, and $Z=S_2$. The symbol $\mathscr A$ below is a leading evolution, not the coefficient called $A$ in SF.4.

Use the actual root-label phases $\Phi_\sigma(r)$ and their inverses $H_\sigma(r)$ from PF/CT/WY. On the strict interval,
$$
\Phi_\sigma(r)=\Phi_{\sigma,c}\circ\psi_\sigma(r),\qquad
H_\sigma(r)=\chi_\sigma(r)\circ H_{\sigma,c},\qquad
\chi_\sigma=\psi_\sigma^{-1}.
\tag{SW.3}
$$
Density pullback is $U_\alpha f=\alpha'(f\circ\alpha)$, so
$U_\alpha U_\beta=U_{\beta\circ\alpha}$.
Let $\mathcal C=\operatorname{diag}(C_+,C_-)$ be the full root coefficient of
[CT.4](R133-supplement-regular-density-transport-for-complete-first-coefficient.md) and
[WY.39--46](R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md). Then
$$
\partial_r C_\sigma=U_{H_\sigma(r)}a_\sigma,\qquad
C_\sigma(r_c)=C_{\sigma,c}.
\tag{SW.4}
$$
It contains the original common root function $F_*$ and its scalar mean.
It is neither the SN nonmean $q_\sigma$ nor $C_\sigma-F_*$.
WY.42--44 proves that the two input signs give the same real $C_\sigma$, using the complete root normalization, rather than equality of upper bounds. The Airy sign constants remain on the right.

## 2. The exact leading map and the unchanged cut input

Let $k(r_c)=1$, $k_r=\ell_0 k$, and define the diagonal root-to-moving evolution
$$
\mathscr A(r)=k(r)\operatorname{diag}_\sigma U_{\Phi_\sigma(r)}.
\tag{SW.5}
$$
The true phase equation $\partial_r\Phi_\sigma=c_\sigma\partial_\phi\Phi_\sigma$ gives
$\partial_r U_{\Phi_\sigma}=\partial_\phi M_{c_\sigma}U_{\Phi_\sigma}$.
Consequently
$$
\mathscr A_r=L_0\mathscr A,\qquad
\mathscr A(r)=V_0(r,r_c)\operatorname{diag}_\sigma U_{\Phi_{\sigma,c}}.
\tag{SW.6}
$$
There is no missing Jacobian or mean-residual term. In PF's notation
$E_r=-2R_0E/m$ and
$(\log n_g)_r=-\ell_0-2R_0/m$, hence
$E(r)/n_g(r)=[E(r_c)/n_g(r_c)]k(r)$ exactly. The reference mean residual $R_0$ is not set to zero.

Keep the scalar leading constants on the original input:
$$
(\mathscr L_ca)_\sigma
 =\sum_{\epsilon=\pm1}
   \frac{\ell_{\sigma,\epsilon}^*E(r_c)}{n_g(r_c)}\Pi_\epsilon a,
 \qquad a\in\mathcal X_{97}.
\tag{SW.7}
$$
Here $\Pi_\epsilon$ are the original root Fourier sign projectors.
For either Sobolev window,
$$
\|\mathscr L_c\|
 =\max_\epsilon
  \left(\sum_{\sigma=\pm1}
   \left|\frac{\ell_{\sigma,\epsilon}^*E(r_c)}{n_g(r_c)}\right|^2
  \right)^{1/2}.
\tag{SW.8}
$$
The two input signs are orthogonal at this step; the two physical output waves require the displayed component norm. These constants do not commute through a coefficient, the selected chart, or the subsequent common-root input change.

Define the single first-symbol map
$$
W(r)=\mathscr A(r)(1+M_{\mathcal C(r)}I)\mathscr L_c.
\tag{SW.9}
$$
WY.40--41 is an exact input-primitive identity on each original Fourier basis vector. Thus
$$
W(r_c)=n_g(r_c)^{-1}B_{\rm free}^{[1]}=\mathcal B_c.
\tag{SW.10}
$$
The equality concerns the same terminal-Ai reference and the original $|j|\ge97$ input. The original output-primitive mean/tail, finite cut corrections and actual cut error remain in their FA/WY ledger. This does not construct a different free basis or infer an inverse leading norm from an upper bound.

## 3. Full primitive conjugation and the new defect

Put $b_\sigma^{\rm root}=U_{H_\sigma}a_\sigma$ and
$p_\sigma=H_\sigma-\operatorname{id}-\langle H_\sigma-\operatorname{id}\rangle$.
The exact full-circle primitive identity gives
$$
\mathscr A^{-1}M_aI\mathscr A=M_{b^{\rm root}}I+\mathcal F_{\rm root},
\quad
(\mathcal F_{\rm root})_\sigma
 =b_\sigma^{\rm root}\otimes p_\sigma
       -(b_\sigma^{\rm root}p_\sigma)\otimes1.
\tag{SW.11}
$$
The tensor functional is the complete normalized integral. The radial $k$ cancels only within this conjugation. In particular the second, scalar-mean functional is retained.

Using (SW.4) and (SW.6), with every product in its displayed order,
$$
\mathcal D_W:=(\partial_r-L_d)W
 =-\mathscr A
   \left\{
     M_{b^{\rm root}}I M_{\mathcal C}I+
     \mathcal F_{\rm root}(1+M_{\mathcal C}I)
   \right\}\mathscr L_c .
\tag{SW.12}
$$
The differentiation contributes $\mathscr A M_{b^{\rm root}}I\mathscr L_c$, which cancels exactly the corresponding linear term from $M_aIW$. It does not commute $I$ past $\mathcal C$.

The defect $\mathcal F_{\rm root}$ in (SW.11) is only the primitive-conjugation pair. In particular it is not the complete normalization remainder. That remainder is still the whole SF.18:
$$
\begin{split}
\mathcal Q={}&\mathcal R_2T_1T_2
 +(K_{-1}ISI-SIaI+\mathcal F_1)T_2
 +OIZI^2-SIOI\\
&+T_1\{H_ZI^2+ZIC_\phi I+aIZI^2-ZI^2aI+\mathcal F_2\}.
\end{split}
\tag{SW.13}
$$
Here $C=C_{\rm vel}$, $H_Z=CZ_\phi+C_\phi Z-Z_r$, and
$$
\begin{split}
\mathcal R_2&=IM_{D_\phi}I+\beta IM_{\mathbf r_\phi}IM_{\mathbf a_\phi}
                         +\mathcal F_0,\\
\mathcal F_0&=-\Pi M_B-M_{ID}\Pi+\Pi M_DI
                           +\beta M_{I\mathbf r_\phi}\Pi M_{\mathbf a},\\
\mathcal F_1&=-CS\Pi+S\Pi C,\qquad
\mathcal F_2=-Z(IC)\Pi+Z\Pi CI.
\end{split}
\tag{SW.14}
$$
The second normalizer $T_2$ and the entire $T_1\mathcal F_2$ term remain. All matrix/row meanings are exactly SF.9--18. The new recipe below uses the complete saved $\mathcal Q$ bound, without subtracting any of its positive terms.

## 4. The complete source, interfaces and two endpoints

The new full-normalizer trial is
$$
\mathbb Y_{W,T}=\binom{PTW}{0}.
\tag{SW.15}
$$
Its displayed mean is a trial choice. Since $[G_y,P]=0$ and $Z_yP=Z_y$,
its exact source in the complete SP system is
$$
\mathbb F_{W,T}
 =\binom{P\{T\mathcal D_W-\mathcal QW\}}{-Z_yTW}.
\tag{SW.16}
$$
All actual evolving means and all mean couplings in the error equation remain. In particular the second row is generally nonzero.

At every original qualified interface, $S$, the actual leading evolution and the complete first coefficient are continuous; radial derivatives of the reference need not be. The new jump is therefore
$$
[\mathbb Y_{W,T}]_\ell=\binom{PT_1[Z]_\ell I^2W(r_\ell)}0.
\tag{SW.17}
$$
The bracket is right trace minus left trace in increasing $r$. The comparison error has the negative of this jump and the negative of (SW.16), as in SF.42--44. All 3070 certified interface locations are retained, including conservative artificial refinement locations. A jump receives no radial length factor. No old whole jump bound is transferred merely because the cut values agree.

Let $J_s=268435456$, retain the exact double-high $T_J$, and set $F_T=T-T_J$ as in UT. The new compressed trial is
$\mathbb Y_{W,J}=(PT_JW,0)$.
By (SW.10), the complete cut discrepancy from the successful UT calculation is the same object:
$$
E_{c,T}^{\rm dens}
 =\mathfrak D_{r_c}{\sf H}^{0,c}
       -n_g(r_c)\binom{PT(r_c)\mathcal B_c}0 .
\tag{SW.18}
$$
Read its complete UT upper bound verbatim. It already contains the original FA cut error and the full $F_T(r_c)B_{\rm free}^{[1]}$ correction, with their original normalization.

At the waist the return to the new compressed trial is
$$
\mathfrak D_0{\sf H}^{0,c}-n_g(0)\mathbb Y_{W,J}(0)
 =\mathfrak D_0{\sf H}^{0,c}-n_g(0)\mathbb Y_{W,T}(0)
     +n_g(0)\binom{PF_T(0)W(0)}0.
\tag{SW.19}
$$
Thus both endpoint corrections remain. The actual inverse used later is the same WT $T_J(0)^{-1}$; no inverse of full $T$ is assumed.

## 5. Previously completed fields which bound every shorter interval

All bounds in this section refer to exactly (SW.1), the original physical circle and the same terminal-Ai column. The analytic identities hold throughout that real family. The selected common angle enters only in Section 8.

The complete SJ derivative integrals in SJ.45 were sums of positive bounds with true ordinary radial lengths. They bound
$\partial_\phi^k\int_{r_c}^rU_{\chi_\sigma}a_\sigma\,ds$ for **every**
$r\in[0,r_c]$, for $k=0,1,2$.
CG.15 then applies the fixed $H_{\sigma,c}$ density chain rule to precisely those same positive integrals. Its complete derivative sums and both complete multiplier candidates therefore hold uniformly for the full $C_\sigma(r)$, not only at the waist. This conclusion uses the actual positive construction; it would not follow from an arbitrary terminal norm.

Accordingly read, without recomputation,
$$
m_{13}=\text{CG.complete.Hminus1\_3},\qquad
m_{43}=\text{CG.complete.Hminus4\_3},
\tag{SW.20}
$$
which bound the diagonal $M_{\mathcal C(r)}$ on the two stated windows.
Each CG bound is common to either branch, so its maximum controls the Hilbert diagonal operator. A sum over equal input-sign coefficients is not added. The scalar mean is already in each multiplier.

Read also:
- $a_0$: the zeroth FA complete own-sign/branch $A_0$ derivative supremum;
- $z_0$: the zeroth FA bound for $\kappa^{-1}$, where $\kappa=\partial_\phi\Phi_{\sigma,c}$;
- $n_{c,-}$: the same-cut positive lower bound for $n_g$;
- $e$: the complete CG bound for $|\kappa-1|$;
- $u_c^-$: the actual FA forward $U_{\Phi_{\sigma,c}}$ bound on $H^{-4/3}$;
- $v_0,v_-$: WX's reverse ungauged leading bounds on $L^2,H^{-4/3}$, valid on every shorter interval;
- $M_\chi,F_\chi$: WX's complete first and second derivatives of the inverse flow on every shorter interval;
- $h_{c,2}$: CG's complete $H_{\sigma,c}''$ bound;
- $b_{c,0}$: SJ's zeroth complete maximum for $U_{\chi_\sigma}a_\sigma$;
- $C_{I^2}$: the completed CG norm of $I^2:L^2\to H^{4/3}$.

The true Jacobian is positive by the original cut gate. An upper $e$ is used only for
$\kappa\le1+e$; no new $e<1$ assumption or reciprocal is needed.
For each branch,
$\|U_{\Phi_{\sigma,c}}\|_{L^2\to L^2}\le\sqrt{1+e}$.
The exact leading identity in WY.40 and the positive lower $n_{c,-}$ give a new **forward** bound
$$
L_c^\#=\sqrt2\,a_0z_0/n_{c,-},\qquad
A_0^\#=v_0\sqrt{1+e},\qquad
A_-^\#=v_-u_c^- .
\tag{SW.21}
$$
The only $\sqrt2$ here combines the two physical wave components of (SW.8).
The sign projectors are orthogonal before multiplication. No KL inverse upper is inverted, no $K_c^-$ containing a first coefficient is multiplied in again, and no extra characteristic factor is appended to the complete WX leading norm.

From (SW.3) and the complete density composition,
$$
b_0^\#=z_0b_{c,0},\qquad
h_2^\#=F_\chi z_0^2+M_\chi h_{c,2}.
\tag{SW.22}
$$
These bound $b_\sigma^{\rm root}$ in $L^\infty$ and $H_\sigma''$ in $L^\infty$ for either branch and every shorter interval.
Since $p_\sigma=I^2H_\sigma''$ and the full two-sign Fourier sum
$\sum_{j\ne0}(4j)^{-4}<1/64$,
$$
P_H^\#=C_{I^2}h_2^\#,\qquad
P_\infty^\#=h_2^\#/8,\qquad
f_{\rm root}^\#=b_0^\#(P_H^\#+P_\infty^\#).
\tag{SW.23}
$$
This pays both root primitive ranks, including the constant functional.
The diagonal two-wave operator is controlled by the common per-branch bound, with no unproved component-sum identification. A composition does not acquire finite Fourier support from these estimates.

## 6. A finite current-only strong recipe

Let $C_I=\sqrt{17}/4$. The two ordered primitives in (SW.12) use
$H^{-4/3}\xrightarrow I H^{-1/3}
\xrightarrow{M_{\mathcal C}}H^{-1/3}
\xrightarrow I H^{2/3}\hookrightarrow L^2$.
Put
$$
\begin{split}
c_-^\#&=1+m_{43}/4,\\
W_-^\#&=A_-^\#c_-^\#L_c^\#,\\
D_W^\#&=A_0^\#
 \{(17/16)b_0^\#m_{13}+f_{\rm root}^\#c_-^\#\}L_c^\# .
\end{split}
\tag{SW.24}
$$
Then $W_-^\#$ bounds the entire $W:\mathcal X_{97}^{-4/3}\to H^{-4/3}(\mathbb C^2)$ and $D_W^\#$ bounds the complete strong defect.

Read SJ's uniform complete maxima $t_0,t_-,q_*,z_*,t_{1,0},Z_0$.
They respectively bound $T$ on $L^2,H^{-4/3}$, the whole
$\mathcal Q:H^{-4/3}\to L^2$, the complete
$Z_y:H^{-4/3}\to\mathbb C^2$, $T_1$ on $L^2$, and $Z$ in operator supremum norm. The saved entry-sum bounds are safe for these operator norms. A new sufficient complete source and interface bound is
$$
\begin{split}
F_W^\#&=r_c\{t_0D_W^\#+(q_*+z_*t_-)W_-^\#\},\\
J_W^\#&=3070\,t_{1,0}(17/16)(2Z_0)W_-^\# .
\end{split}
\tag{SW.25}
$$
The first uses the actual length once. The second uses the one-sided inequality
$|[Z]|\le2Z_0$, retains the complete certified interface count, and has no length.
Both formulas are new scalar products of completed global maxima; no old enclosure, ray, positive source integral or interface sum is recomputed. The use of a global maximum can be coarse and does not predict an improvement.

Read UT's completed $\mathcal E_T^\#\ge\|F_T:H^{-4/3}\to L^2\|$ and its whole cut upper $E_{c,T}^\#$, the actual waist $n_{g,0}^+$, and the two existing SF/ST gains $G_{\rm cut},G_{\rm src}$.
Then
$$
e_{0,W}^\#=n_{g,0}^+\mathcal E_T^\#W_-^\#,
\qquad
C_{{\rm SF},W}^\#
 =G_{\rm cut}E_{c,T}^\#
   +G_{\rm src}(F_W^\#+J_W^\#)+e_{0,W}^\# .
\tag{SW.26}
$$
The source gain consumes the ordinary $L^1(dr;\mathcal Y)$ source (SW.16) and the ungauged state impulses, by the exact positive-algorithm argument in SF.39--41. Its waist density factor is already included; no further $n_g(0)$ multiplies that middle term.
The final term is a different endpoint correction and does require the displayed $n_g(0)$ once.

The exact identities first hold on finite original Fourier sums. The strong source, jump and endpoint bounds then extend their complete difference to $\mathcal X_{97}^{-4/3}$, exactly as in SF.44. They do not assert that the full oscillatory trial itself is $L^2$ on that input space.

## 7. Exact waist normalization and the remaining independent projection rank

Let $\Lambda_\sigma$ be the original root sign-diagonal waist leading factor.
From (SW.7), the mean-residual identity in Section 2, and $\Phi_\sigma(0)=X_{-\sigma}$,
$$
n_g(0)W_\sigma(0)
 =U_{X_{-\sigma}}(1+M_{C_\sigma(0)}I)\Lambda_\sigma
\quad\hbox{on }\mathcal X_{97}.
\tag{SW.27}
$$
The factor $\Lambda_\sigma$ remains on the right. Applying the original same-$J_s$ WT inverse after returning to $\mathbb Y_{W,J}$, taking the actual row, applying the full inverse density, and then the original right $\Lambda_\sigma^{-1}$ gives
$$
U_{X_{-\sigma}}^{-1}PU_{X_{-\sigma}}(1+M_{C_\sigma(0)}I)
 =(1-v_\sigma\otimes\Pi)(1+M_{C_\sigma(0)}I),
\quad v_\sigma=U_{X_{-\sigma}}^{-1}1.
\tag{SW.28}
$$
The scalar mean is preserved by density pullback. On the original high input,
$\Pi a=0$ and $\Pi(C_\sigma Ia)=-\Pi((IC_\sigma)a)$.
Thus the independent waist projection fee is at most
$$
C_{{\rm proj},W}^\#=B_{X^{-1},0}\|IC_\sigma(0)\|_{H^{4/3}}.
\tag{SW.29}
$$
It is not zero, and it is not the cut primitive rank or either rank in (SW.11).
On low/mean input, the omitted simplification $\Pi a=0$ is unavailable; the complete old finite and physical mean rows stay in the retained register.

The old WY product trial instead gives
$(1-v_\sigma\otimes\Pi)(1+M_{C_\sigma}I+R_{\sigma,\rm alg})$.
Their difference is exactly
$(1-v_\sigma\otimes\Pi)R_{\sigma,\rm alg}$.
Writing the actual row as $B_\sigma$, the two state discrepancies satisfy the exact relation
$$
\begin{split}
E_{\sigma,W}^{\rm state}
 &=E_{\sigma,\rm old}^{\rm state}
        +(1-v_\sigma\otimes\Pi)R_{\sigma,\rm alg},\\
E_{\sigma,W}^{\rm state}
   -v_\sigma\otimes\Pi(1+M_{C_\sigma}I)
 &=E_{\sigma,\rm old}^{\rm state}
        +R_{\sigma,\rm alg}
        -v_\sigma\otimes\Pi(1+M_{C_\sigma}I+R_{\sigma,\rm alg}).
\end{split}
\tag{SW.29a}
$$
Thus the actual normalized operator minus its principal coefficient is unchanged. The old algebra term is not subtracted from an upper bound.

## 8. Reuse the complete CG positive fee; compare only the whole paid object

The successful CG positive construction explicitly used
$$
C_{\rm proj,CG}^\#
 =(1+B_{X^{-1},0})R_{\rm alg}^\#
       +B_{X^{-1},0}P_C,\qquad
P_C\ge\|IC_\sigma(0)\|_{H^{4/3}},\quad R_{\rm alg}^\#\ge0.
\tag{SW.30}
$$
Therefore its whole projection budget also bounds (SW.29).
All other CG terms concern the same full coefficient $C_\sigma$, the same common-root $T_F^{-1}$, and the same selected chart $\mathcal S$.
The successful complete CG coefficient-only fee can consequently be copied as a conservative upper for the new trial's entire coefficient contribution. This is forward domination by identified nonnegative budget terms; it is not recovery of a summand from an arbitrary norm.

Read UT's already completed state factor
$A_{\rm state}=B_{H^{-1},0}K_{W,0}K_\Lambda K_{F,-4/3}K_{\mathcal S^{-1},-4/3}$,
its complete independent $C_{\rm PC}$ and $C_{\rm ST4}$, and $C_{\rm CG}$.
A new sufficient paid bound is
$$
C_{*,W}^\#=C_{\rm PC}+C_{\rm ST4}+C_{{\rm SF},W}^\#,\qquad
C_{{\rm paid},W}^\#=A_{\rm state}C_{*,W}^\#+C_{\rm CG}.
\tag{SW.31}
$$
Only the state error uses the exact left-angle cancellation of WY/WE. The original input order remains
$E_{*,W}P_{97}\Lambda_\sigma^{-1}T_F^{-1}\mathcal S^{-1}$.
No $\Lambda_\sigma$, root projector or sign projector moves through $\mathcal S$.
The complete CG fee is added once and is not multiplied by $A_{\rm state}$ or a second $K_F$.

This is the same individually $\Lambda_\sigma$-normalized paid branch object as UT, with both original input signs already included. It does not remove the exact Maslov factor of the common physical outgoing map: the MS/ZD ordered global map remains separate.

The allowed comparison is
$$
C_{\rm paid,new}^\#
 =\min\{C_{\rm paid,UT}^\#,\,C_{{\rm paid},W}^\#\}.
\tag{SW.32}
$$
Both candidates, their full records, and their scopes must be retained.
Select using upper endpoints of the final serialized outward records, keeping the old candidate on a tie. Do not take entrywise minima.
In particular $C_{{\rm SF},W}^\#$ and the UT original-trial SF error bound compare different trials and are not substituted for one another without their exact difference.

The WE/UT six retained rows stay verbatim with unknown numerical fees. Full $E_i/E_o$, actual incoming invertibility, the finite Schur inverse, common physical return and $R_0$ remain unproved by this scalar recipe. Two independent physical means, transported root head/low input, all finite cross blocks, stable/reference ports and infinite other-sign contributions retain their existing classifications.

## 9. Exact small inputs and a future numerical target

The following are all already completed small texts. Paths have prefix
`topics/visible-flex-exact-nearby/`. Embedded scientific objects are read from their original execution field without changing their byte provenance.

| Role | Repository path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| FA2 science | `notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/actual-scientific-conclusion.json` | `2001f4e2eeece1cda56b18b90dccab04b7f6d336` | 35718 | `2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2` |
| WX execution | `notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json` | `5121a599896025d90e2861450756a256aaba659d` | 43753 | `e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12` |
| SJ execution | `notes/strict_radial_first_symbol_defect_ci/run-43768006977-1/execution.json` | `7dac244799016d9cae317a61f6c5dbe47ca0a013` | 46318 | `2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88` |
| CG science | `notes/separate_cut_propagated_coefficients_ci/run-43768992861-1/actual-scientific-conclusion.json` | `bb4ed26f5aef5e84dd3a055ce54e40df0cdc0963` | 18985 | `a68095bb38c38d62a4b1af256c84c96e7f1f7f1c2663d5fdb5ffc814b73e57fc` |
| UT science | `notes/full_normalizer_endpoint_replacement_ci/run-43776528869-1/actual-scientific-conclusion.json` | `ae319d395f13b645d33a02a6922b7506cb88cf26` | 22856 | `3817fbeca91e87e63298cc3e52161af6167465eef62b9af3d3b4da3940ce139e` |

Exact scalar paths, relative to each original scientific object:

| Symbols | Exact original fields |
|---|---|
| $a_0,z_0,n_{c,-},u_c^-$ | FA `complete_new_first_frame_and_leading_conclusion`: `complete_common_each_sign_each_branch_A0_angular_jets[0]`, `complete_phase_reciprocal_angular_jets[0]`, `same_cut_ng_lower_read_verbatim`, `complete_U_Phi_Hminus4_3_upper_read_verbatim` |
| $v_0,v_-$ | WX `complete_ungauged_leading_flow_conclusion.complete_reverse_L2_upper` and `complete_reverse_Hminus4_3_upper` |
| $M_\chi,F_\chi$ | WX `complete_shorter_flow_derivative_conclusion.complete_shorter_flow_derivative_upper` and `complete_shorter_flow_second_derivative_upper` |
| $m_{13},m_{43}$ | CG `complete_new_multiplier_conclusion.complete.Hminus1_3` and `Hminus4_3` |
| $e,h_{c,2},C_{I^2}$ | CG `complete_new_dual_row_conclusion.phase_derivative_deviation`, `inverse_second_derivative_upper`, `C_I2_L2_to_H4_3_upper` |
| $b_{c,0}$ | SJ `complete_new_transported_coefficient_conclusion.common_both_branch_b_0_2_maxima[0]` |
| $t_0,t_-,q_*,z_*,t_{1,0}$ | SJ `complete_new_radial_coefficient_conclusion.complete_finite_and_two_primitive_scalar_maxima`: `t0`, `tm`, `qstar`, `zstar`, `t10` |
| $Z_0$ and the complete join count | SJ `complete_new_radial_coefficient_conclusion.complete_matrix_row_column_A0_maxima.Z`; `complete_new_interface_conclusion.complete_interface_count` |
| $\mathcal E_T^\#,E_{c,T}^\#$ | UT `complete_new_endpoint_strong_conclusion.complete_FT_Hminus4_3_to_L2_upper`; `complete_new_full_trial_bound_conclusion.complete_new_physical_cut_error_upper` |
| $n_{g,0}^+,G_{\rm cut},G_{\rm src},A_{\rm state},C_{\rm PC},C_{\rm ST4},C_{\rm CG}$ | UT `copied_complete_scalar_inputs_read_verbatim`: `ng0_upper`, `Gcut`, `Gsource`, `Astate`, `C_PC`, `C_ST4`, `CGwhole` |
| Old complete paid candidate | UT `complete_new_ordered_paid_conclusion.complete_paid_Hminus4_3_to_L2_upper` |
| Unpaid exact rows | UT `retained_row_register`, copied completely |

The only new scientific work proposed is evaluation of the positive combinations (SW.21)--(SW.26), (SW.31)--(SW.32). No new ray, original norm enclosure, source grid, Gram, signed first-coefficient integral or successful target is called. Original sources may be read only to verify the positive-construction identities; they are not imported or executed.

A future consumer must first verify every original success, gate count, runtime/source/manifest identity, same cut, full family, moving $J_s$, original high input and selected-chart scope. It must preserve all read balls, the new full source/jump/endpoint terms, the old and new complete paid candidates, and all retained rows. A failed validation or a non-improving whole candidate is retained honestly. The formulas in this note do not by themselves provide a numerical value or an incoming gate.
