# R133 supplement: exact waist flux, two primitive terminals, and complete endpoint reception

2026-11-16, phase_inverse.

**Proved analytic replacement; all 31 numerical targets below are new and unevaluated.** On the selected actual free waist, the nonmean density map has an exact four-block representation. Its first two blocks are the same leading and first coefficients already saved in FA/WZR. The remaining blocks use one and two original primitives. Their amplitudes separate into a frequency-independent function and the original bounded scalar $c_{B,n}$ times another such function. This permits complete negative-Sobolev multiplication bounds using only first and second angular derivatives.

The resulting two endpoint candidates retain the full scattering matrix, both free reference columns, the same output projection, the complete physical mean, WT, and the original ordered final receiver. No successful scalar target is recomputed, no old upper is reduced by a subtotal, and no numerical improvement or finite inverse is asserted here.

## WEX1. The identical selected waist and complete state

Use the same selected real member, fixed intrinsic $\eta_0$, original normalized circle
$\mathbb T_{\pi/2}$, physical frequencies $n=4|j|$, $n\ge N_0=388$, and $\epsilon=\operatorname{sgn}j$. Let
$$
 \Pi f=\frac2\pi\int_0^{\pi/2}f(\phi)\,d\phi,\qquad
 P=Id-\Pi,\qquad I=\partial_\phi^{-1}P.
 \tag{WEX.1}
$$
The full Bessel norm is
$$
 \|f\|_{H^s}^2=\sum_{j\in\mathbb Z}(1+16j^2)^s|\widehat f(j)|^2.
 \tag{WEX.2}
$$
In particular all auxiliary multiplication and profile estimates include zero and low output modes.

WES.5--9 proves for the entire selected waist circle and a true one-sided radial neighbourhood that
$$
 T<-L,\qquad L=\frac1{2000}.
 \tag{WEX.3}
$$
Thus the genuine potential vanishes there. The complete tail does not:
$$
 \Psi_{\rm ext}=F_n{\sf S}_n,\quad
 \|{\sf S}_n^{\pm1}\|<\frac65,\qquad
 {\cal B}_{\rm ext}=c_{B,n}t^{-1/2},\qquad t=-T.
 \tag{WEX.4}
$$
The old complete record $C_B$ bounds $|c_{B,n}|$. The scalar $c_{B,n}$ and the reference matrix ${\sf S}_n$ have no radial or angular derivatives in this free neighbourhood. They may depend on the original input frequency. The matrix is kept on the input side; it is not commuted through an arbitrary matrix amplitude.

At the actual waist $r=0$, WZR.3--8 gives
$$
 \beta=d=q_r=0,\qquad J_w=\eta_w^{-1}I.
 \tag{WEX.5}
$$
The actual parity inverse is used on the assembled original reflected class. The explicit primitive identity then permits a norm estimate on the containing complete nonmean Bessel carrier. It does not grant an unqualified signed realization of a different $J$.

Write $R_w=n_g(0)T(q_0)$ for the original radial primitive-density matrix, with the unchanged convention of WZR and the successful reconstruction record. It is independent of the angle. The complete endpoint state remains
$$
 {\cal Y}_0=L^2_{\ne0}(\mathbb T_{\pi/2};\mathbb C^2)\oplus\mathbb C^2.
 \tag{WEX.6}
$$
The uncompleted map ${\cal B}_F^V$ has zero raw means. Its independent completion remains $v_z z_{\rm ph}(0)$, with
$v_z=\mathfrak D_0(-u_w/m_w,1)$, both stored density means, and the actual initial condition $z_{\rm ph}(r_*)=0$. Neither the value of that mean nor its full propagation is changed in this note.

The point identities (5) are not radially differentiated. In particular $\beta_r,d_r,J_r$, the full second-order drift, and all original mean fees in the already saved forcing and negative receiver remain.

## WEX2. Exact free transport as a physical flux

All functions in this section are actual functions before norms. Put
$$
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},\quad
 x=X_\phi,\quad y=T_\phi,\quad
 H=i\epsilon x\,Id+yK_T,\quad A=H^{-1},\quad
 M=i\epsilon X_r\,Id+T_rK_T .
 \tag{WEX.7}
$$
The true phase gap gives
$\det H=-\Phi_{+,\phi}\Phi_{-,\phi}<0$.
Let $z=n^{-1}$, $w_1^V=w_1+c_{B,n}h$, and
$$
 h=t^{-1/2}K_Tw_0,\qquad W=w_0+zw_1^V.
 \tag{WEX.8}
$$
Here $w_1$ is the original complete free first transport; $w_1^V$ is the genuine extended amplitude. They are not identified with each other.

For the original fold scalar $Q=Q_f$, WUA.14--15 and the same ordinary-radial transport give at this waist
$$
 C=-i\epsilon QK_T,\qquad
 L_w=\frac Q4
 \begin{pmatrix}x/T&-i\epsilon y\\ i\epsilon y/T&-x/T\end{pmatrix},
 \tag{WEX.9}
$$
$$
 q_f=\frac Q2
 \begin{pmatrix}x&i\epsilon y\\ i\epsilon y&x/T\end{pmatrix}
 \binom{F_a}{F_b}.
 \tag{WEX.10}
$$
The pair $F_a,F_b$ is the entire original WUA forcing, including $\vartheta$, the radial drift coefficients, both physical components and all original means. In particular $d_r$ is not made zero in that forcing by $d_w=0$.

For completeness, before the waist specialization the reaction has the additional term
$-H_c Id/2$, where
$H_c=q_r/q+4\beta\Pi S-4d_\phi=q_r/q+4\beta S$.
All of this term vanishes at the waist by (5). Also $Q_\phi=-Qy/(2T)$; hence
$$
 \Delta:=L_w-C_\phi
 =\frac Q4
 \begin{pmatrix}x/T&i\epsilon y\\-i\epsilon y/T&-x/T\end{pmatrix}.
 \tag{WEX.11}
$$
For example the upper-right entry of $C_\phi$ is
$-i\epsilon(Q_\phi T+Qy)=-i\epsilon Qy/2$; subtracting it gives the upper-right sign in (11). The lower-left sign follows from $Q_\phi$ in the same way.

The exact transport equations are
$$
 (w_0)_r=C(w_0)_\phi+L_ww_0,\qquad
 (w_1^V)_r=C(w_1^V)_\phi+L_ww_1^V+q_f .
 \tag{WEX.12}
$$
Although $V_{\rm ext}=0$ here, (8) and its derivatives remain in (12). The complete tail is a homogeneous addition in this neighbourhood.

Let ${\cal U}={\cal U}^{F}_{n,\epsilon}$ use either of the two free reference columns, with the original scaled derivative and normalization. Its exact free derivative rules and $HC=M$ give
$$
 \partial_r{\cal U}(W)
 =\partial_\phi{\cal U}(CW)+{\cal U}(\Delta W+zq_f).
 \tag{WEX.13}
$$
Thus (5), the original outer primitive, and $IP=I$ give the complete nonmean density identity
$$
 {\cal B}_F^V
 =R_w n^{7/6}
 \begin{pmatrix}
 \eta_w^{-1}\{I{\cal U}(CW)+I^2{\cal U}(\Delta W+zq_f)\}\\
 I{\cal U}(W)
 \end{pmatrix}.
 \tag{WEX.14}
$$
This is an evaluation identity at the waist. No radial integration by parts has introduced or suppressed an endpoint, seam or physical mean.

## WEX3. Two exact primitive identities and four full blocks

Define the ordered amplitude differential operator
$$
 {\mathscr D}v=\partial_\phi(Av).
 \tag{WEX.15}
$$
Since $\partial_\phi{\cal U}(v)={\cal U}(nHv+v_\phi)$, the identities $I\partial_\phi=P$ and $IP=I$ give
$$
 I{\cal U}(v)=zP{\cal U}(Av)-zI{\cal U}({\mathscr D}v).
 \tag{WEX.16}
$$
For any $a_0,a_1,b_0,b_1$, applying (16) a finite number of times yields
$$
 \begin{aligned}
 I{\cal U}(a_0+za_1)
 ={}&zP{\cal U}(Aa_0)
   +z^2P{\cal U}(Aa_1-A{\mathscr D}a_0)\\
 &+z^2I{\cal U}({\mathscr D}^2a_0-{\mathscr D}a_1),
 \end{aligned}
 \tag{WEX.17}
$$
$$
 \begin{aligned}
 I^2{\cal U}(b_0+zb_1)
 ={}&z^2P{\cal U}(A^2b_0)
   -z^2I{\cal U}({\mathscr D}(Ab_0))\\
 &+zI^2{\cal U}(b_1-{\mathscr D}b_0).
 \end{aligned}
 \tag{WEX.18}
$$
In particular the order ${\mathscr D}(Ab_0)$ in (18) cannot be changed to
$A{\mathscr D}b_0$.

Use (17) on $CW$ and $W$, and (18) on
$\Delta w_0+z(\Delta w_1^V+q_f)$.
For a pair of row amplitudes, ${\cal U}$ acts on each physical row. Define
$$
 V_0=
 \begin{pmatrix}\eta_w^{-1}ACw_0\\Aw_0\end{pmatrix},
 \tag{WEX.19}
$$
$$
 V_1=
 \begin{pmatrix}
 \eta_w^{-1}\{ACw_1^V-A{\mathscr D}(Cw_0)+A^2\Delta w_0\}\\
 Aw_1^V-A{\mathscr D}w_0
 \end{pmatrix},
 \tag{WEX.20}
$$
$$
 T_1=
 \begin{pmatrix}
 \eta_w^{-1}\{{\mathscr D}^2(Cw_0)-{\mathscr D}(Cw_1^V)
                      -{\mathscr D}(A\Delta w_0)\}\\
 {\mathscr D}^2w_0-{\mathscr D}w_1^V
 \end{pmatrix},
 \tag{WEX.21}
$$
$$
 T_2=
 \begin{pmatrix}
 \eta_w^{-1}\{\Delta w_1^V+q_f-{\mathscr D}(\Delta w_0)\}\\0
 \end{pmatrix}.
 \tag{WEX.22}
$$
The exact full map is
$$
 \boxed{
 {\cal B}_F^V
 =R_wn^{7/6}
 \{zP{\cal U}(V_0)+z^2P{\cal U}(V_1)
                  +z^2I{\cal U}(T_1)+zI^2{\cal U}(T_2)\}.}
 \tag{WEX.23}
$$
Here the factor $R_w$ is understood outside the row amplitudes in (19)--(22); it appears once. The separate mean vector in (6) is added later.

All four blocks are exact. Neither $T_1$ nor $T_2$ is declared zero. The full $P$ in both retained blocks is retained.

## WEX4. Exact agreement with the saved FA coefficients

The original waist reconstruction satisfies
$$
 g_0=(\eta_wH)^{-1}Mw_0=\eta_w^{-1}Cw_0.
 \tag{WEX.24}
$$
Using (12) for $w_0$ in the actual FA definition of $g_1$,
$$
 \begin{aligned}
 g_1&=(\eta_wH)^{-1}
       (Mw_1^V+(w_0)_r-\eta_w(g_0)_\phi)\\
 &=\eta_w^{-1}\{Cw_1^V+A\Delta w_0\}.
 \end{aligned}
 \tag{WEX.25}
$$
The leading and first outer primitive amplitudes in FA.18 are therefore exactly
$$
 {\cal B}_0=R_wV_0,\qquad {\cal B}_1=R_wV_1.
 \tag{WEX.26}
$$
This identity is at the function level, before any bound or choice. It uses the same free reference matrix and extended first amplitude as the successful free-waist receipt.

Let ${\cal L}^V$ be the complete two-phase leading-plus-first map of FA.21--22 constructed from these two coefficients. The retained part of (23) is compared to **$P{\cal L}^V$**. The exact first endpoint ${\cal P}_1$ in WES.3 already has this same $P$. Consequently the WES.24--26 leading and first cancellation occurs under the same original projection.

There is no step replacing $P{\cal L}^V$ by ${\cal L}^V$ and then estimating an additional auxiliary $\Pi{\cal L}^V$. Conversely this observation does not set that auxiliary mean to zero as a function, and does not change the independent $v_z z_{\rm ph}$. The old outer-mean record is an immutable valid estimate for the old reconstruction; the new exact decomposition simply does not introduce that separate comparison error.

The already saved records
$$
 K_{\rm sym},\quad C_{\rm A,1},\quad C_{\rm A,2},\quad A_{\rm Bi,1}
 \tag{WEX.27}
$$
are respectively the complete eight-component symbol bound, first Airy cross bound, second Airy remainder bound, and complete Bi first-coefficient sum over both signs and both phases. Their ${\cal B}_0,{\cal B}_1$ are (26), including $R_w$. They are copied exactly, without recalculating a Schur sum, an Airy constant or a coefficient jet.

Put
$$
 C_{\rm A}=C_{\rm A,1}+C_{\rm A,2}.
 \tag{WEX.28}
$$
This is a new complete Airy remainder for the retained degree-zero/one polynomial in (23). It is not the old full polynomial remainder with its higher terms subtracted. The old higher polynomial and old $J$/outer terminals are not used as inputs to a subtraction; the exact alternatives (21)--(23) account for the entire difference.

## WEX5. Fixed angular multiplication with the complete tail separated

Equation (8) gives, exactly for each fixed sign,
$$
 T_i=T_i^{(0)}+c_{B,n}T_i^{(1)},\qquad i=1,2.
 \tag{WEX.29}
$$
The coefficient matrices $T_i^{(0)},T_i^{(1)}$ are independent of the magnitude of the input frequency. In particular
$$
 T_1^{(1)}=
 \begin{pmatrix}-\eta_w^{-1}{\mathscr D}(Ch)\\-{\mathscr D}h\end{pmatrix},
 \qquad
 T_2^{(1)}=\begin{pmatrix}\eta_w^{-1}\Delta h\\0\end{pmatrix}.
 \tag{WEX.30}
$$
The zeroth parts are (21)--(22) with $w_1$ in place of $w_1^V$. The full $q_f$ remains in $T_2^{(0)}$.

Let $F_{i,\ell,j}$ bound the complete entry-sum supremum of the ordinary derivative $\partial_\phi^j T_i^{(\ell)}$, uniformly for both signs. Require
$$
 \begin{array}{c|c|c}
 i&\ell&j\\ \hline
 1&0,1&0,1\\
 2&0,1&0,1,2 .
 \end{array}
 \tag{WEX.31}
$$
These are ten new scalar targets. A component-dependent sign is not bounded by subtracting upper endpoints.

For a scalar $f$ with ordinary derivative bounds $F_j$, the full Bessel multiplication estimates are
$$
 \|M_f:H^{\pm1}\to H^{\pm1}\|\le F_0+F_1,
 \qquad
 \|M_f:H^{\pm2}\to H^{\pm2}\|
       \le F_0+\sqrt2F_1+F_2.
 \tag{WEX.32}
$$
For the positive windows, the $H^1$ and $H^2$ Leibniz comparison matrices have diagonal $F_0$. In $H^2$, use
$(\|g\|_2,\sqrt2\|g'\|_2,\|g''\|_2)$; the $F_1$ off-diagonal shift has norm $\sqrt2F_1$, and the $F_2$ entry has norm $F_2$. This proves (32) by the triangle inequality for these complete matrices. The negative windows follow by duality, including the mean. Summing over matrix entries gives the same safe entry-sum bounds.

Define the two complete new multiplier fees
$$
 M_1=F_{1,0,0}+F_{1,0,1}
                 +C_B(F_{1,1,0}+F_{1,1,1}),
 \tag{WEX.33}
$$
$$
 M_2=F_{2,0,0}+\sqrt2F_{2,0,1}+F_{2,0,2}
       +C_B(F_{2,1,0}+\sqrt2F_{2,1,1}+F_{2,1,2}).
 \tag{WEX.34}
$$
The old saved upper for $\sqrt2$ is read once as that target. The scalar $c_{B,n}$ acts as an input diagonal with norm at most $C_B$. No derivative of an arbitrary frequency-dependent amplitude family is being ignored: (29) has first separated every such dependence into that explicit scalar input multiplier.

The necessary ordinary angular orders are $w_0$ through 3, free $w_1$ through 2, $q_f$ through 2, and the displayed geometry through 4. No radial first-amplitude jet is needed. In particular the complete old $F_a,F_b$ have not been replaced by a principal part.

## WEX6. Complete profile, primitive and input-frequency reception

Copy from the successful WRP receipt the complete weights
$W_{0,0}$ and $W_{2,0}$ of the same genuine profile operator. They include the full near term and both far terms, the actual genuine normalization, all signed Fourier inputs, and zero, low and high outputs. For each constant amplitude basis vector, interpolation of this same operator on the same output Bessel scale gives the new bound
$$
 W_{1,0}=\sqrt{W_{0,0}W_{2,0}}.
 \tag{WEX.35}
$$
The inputs at both endpoints are the same $\ell^2$ space. The common decay factors interpolate to the same
$(1+N^{2/3}\rho)^{-1/4}$. There is no interpolation between different reference maps or differently projected outputs.

The old normalized reflection restriction is isometric. To handle both independent reference inputs and both signs, one may decompose into at most four orthogonal input pieces and use Cauchy--Schwarz, giving the conservative factor 2. Convert free reference inputs to the genuine matrix on their correct right side using $\|{\sf S}_n^{-1}\|<6/5$. This gives $12/5$. No extra factor for the two far phases is added: they are already in each complete $W_{d,0}$.

The original primitive has the full-window bounds
$$
 \|I:H^{-1}\to L^2\|\le\frac{\sqrt{17}}4<\frac{17}{16},
 \qquad
 \|I^2:H^{-2}\to L^2\|\le\frac{17}{16}.
 \tag{WEX.36}
$$
Indeed their nonzero multipliers are $(4ij)^{-1}$ and $-(4j)^{-2}$, and the worst ratios to the full Bessel weights occur at $|j|=1$. Their zero multipliers impose the original output mean projection; no low nonzero output is discarded.

At the waist $\rho=r_*$. The original actual root bracket gives $r_*>c>1/8$, so
$$
 (1+N^{2/3}r_*)^{-1/4}\le 2N^{-1/6}.
 \tag{WEX.37}
$$
The rational 2 is only a safe outward bound for $r_*^{-1/4}$. It is not a newly evaluated root or fractional-power target.

Let $R_*$ be the copied complete operator upper for $R_w$, and let $a_{1/6}$ be the copied complete upper for $2^{1/6}$. Define
$$
 K_1=\frac{51}{10}R_*W_{1,0}M_1,\qquad
 K_2=\frac{51}{10}R_*a_{1/6}W_{2,0}M_2,\qquad
 K_{\rm term}=K_1+K_2.
 \tag{WEX.38}
$$
The coefficient $51/10=2\cdot(12/5)\cdot(17/16)$ records, respectively, (37), the reference/sign assembly and inverse reference conversion, and the primitive norm.

On the physical dyadic band $N\le n<2N$, the first terminal has the factors
$n^{7/6}n^{-2}$, $N^{-1}$, and $N^{-1/6}$; their total is $N^{-2}$. The second has
$n^{7/6}n^{-1}\le2^{1/6}N^{1/6}$, $N^{-2}$, and $N^{-1/6}$, again $N^{-2}$. Hence the complete two-terminal map satisfies
$$
 \|{\cal T}_{[N,2N)}:\ell^2\to{\cal Y}_0\|\le K_{\rm term}N^{-2}.
 \tag{WEX.39}
$$
This bound is for the full row pair. The two stored mean components of this uncompleted terminal map are zero by its explicit primitives; the independent physical completion remains outside it.

For the complete $L^2$ input, triangle summation gives the safe new target
$$
 E_{T,0}=\frac4{3N_0^2}K_{\rm term}.
 \tag{WEX.40}
$$
For the full original $H^{-4/3}$ input, $\Lambda_j=\sqrt{1+n^2}<3N$ on the band. Read the old complete $C_{\rm Bessel}$ and $S_{2/3}$, which pay
$3^{4/3}$ and
$\big(\sum_{\nu\ge0}(N_02^\nu)^{-4/3}\big)^{1/2}$.
Input Cauchy--Schwarz, without output orthogonality, gives
$$
 E_{T,-4/3}=C_{\rm Bessel}S_{2/3}K_{\rm term}.
 \tag{WEX.41}
$$
No new Hilbert--Schmidt sum is applied to the root scattering matrix. No old terminal decay is relabeled.

## WEX7. Two complete endpoint candidates and the unchanged whole receiver

Read the old complete $\Xi_0,\Xi_2$. Their original qualifications retain the four reference/sign columns for $\Xi_0$, the two original input signs for $\Xi_2$, the physical frequency 4, the complete Bessel weights and every output mode.

Equations (23), (26)--(28), and FA's real Airy remainder give
$$
 K_F^{\rm flux}=K_{\rm sym}+E_{T,0}+C_{\rm A}\Xi_0.
 \tag{WEX.42}
$$
The density factor in $K_{\rm sym},C_{\rm A,1},C_{\rm A,2}$ is already present and is not inserted again. Only the new terminal uses $R_*$ in (38).

Let $C_s$ be the old complete bound for
${\sf S}_n(D_n^{\rm root}+J_{n,\infty}):H^{-4/3}\to L^2$.
The new whole scattering endpoint is
$$
 E_{\rm sc}^{\rm flux}=K_F^{\rm flux}C_s.
 \tag{WEX.43}
$$
The matrix remains on the original input side, with its original $4/3$ order, both reference roles and all root normalization terms.

For the other endpoint write
$N_\infty=Id+zc_{B,n}J_{\rm rot}$.
The old complete leading and first cancellation under $P$ gives
$$
 P{\cal L}^V N_\infty\iota_{\rm Ai}-{\cal P}_1
       =z^2c_{B,n}P({\cal L}_1^V\iota_{\rm Bi}).
 \tag{WEX.44}
$$
Here ${\cal L}_1^V$ denotes the complete first coefficient, with its original phase exponentials. Its old bound $A_{\rm Bi,1}$ includes the complete extended amplitude and first Airy correction. In particular its $c_{B,n}$ dependence retains the $c_{B,n}^2$ and first-Airy cross terms after (44).

Define the two complete new positive terms and their sum:
$$
 E_{2,a}=(1+C_B/N_0)(E_{T,-4/3}+C_{\rm A}\Xi_2),\qquad
 E_{2,b}=C_BA_{\rm Bi,1}\Xi_2,
$$
$$
 E_2^{\rm flux}=E_{2,a}+E_{2,b}.
 \tag{WEX.45}
$$
These bound the entire same operator
${\cal B}_F^VN_\infty\iota_{\rm Ai}-{\cal P}_1$.
Neither an old mean upper nor an old remainder upper is subtracted.

Copy the whole WT endpoint and the complete physical mean endpoint from the current successful WSMF provider. Set
$$
 E_{\rm end}^{\rm flux}
   =E_{\rm sc}^{\rm flux}+E_2^{\rm flux}
                    +E_{\rm WT}^{\rm old}+E_{\rm mean}^{\rm current}.
 \tag{WEX.46}
$$
There are exactly four original endpoint contributions. WT uses the same strong whole remainder, same $J_s=268435456$, and exactly one $n_g$ in its already saved product. The physical mean keeps its full feedback, $J_r,T_k$, true root condition, both stored means and original receiver.

Read the complete current negative response $E_-^{\rm current}$, positive response $R_+$, root finite fee $R_F$, ordered readout $L_{\rm rec}$, and separate $C_{\rm alg},D_\infty$. Then
$$
 S_{\rm nr}=R_++E_-^{\rm current}+E_{\rm end}^{\rm flux},\qquad
 S_{\rm all}=S_{\rm nr}+R_F,
 \tag{WEX.47}
$$
$$
 C_{\rm whole}^{\rm flux}=C_{\rm alg}+L_{\rm rec}S_{\rm all},\qquad
 C_{\rm red}^{\rm flux}=D_\infty+L_{\rm rec}S_{\rm nr}.
 \tag{WEX.48}
$$
Whole and reduced are compared only against their own complete currently selected provider records, preserving both candidates and letting the old record win equal saved upper endpoints.

The old negative receiver is copied as a whole. Thus its ordinary-$dr$ factors, all 3070 true jumps, the complete terminal and all original PW windows are unchanged. The exact 96 physical columns and their still uncomputed signed normalization, both means, $\Theta,\nu$, radial head, all seven independent function/endpoint ports, finite factors, cokernel and signed finite inverse obligations retain their current status. A smaller partial error would not itself discharge any of them.

## WEX8. A first executable coefficient recipe using only saved low jets

No new global transport or phase flow is needed for a first candidate. The successful WGS main file already supplies complete normalized low angular bounds for $A,Q,t,x,y,F_a,F_b,a_1,b_1$. The companion file is read in full to retain its exact binding and original qualifications. The successful waist reconstruction separately supplies $w_0$ through order 3 and the exact same $R_*,|\eta_w|^{-1}$ budgets.

The WGS group convention is derivative divided by $r!j!$. For the pure angular entries used here, total orders 0,1,2,3 each have their own saved group. No mixed-group maximum is treated as an actual signed coefficient. A saved scalar supremum/entry sum is not relabeled as a Wiener bound.

For a normalized positive jet $v$, write
$$
 (u*v)_j=\sum_{a=0}^j u_av_{j-a},\qquad
 (\partial^\#v)_j=(j+1)v_{j+1},\qquad
 {\mathscr D}^\#v=\partial^\#(A^\#*v).
 \tag{WEX.49}
$$
All products here are positive majorants for the complete ordered matrix/vector products, not commutations of the actual matrices.

Use the exact real lower $\tau=1/2000$ from (3). For $a=1$ or $a=1/2$, a finite positive jet for $t^{-a}$ is
$$
 h^{[a]}_j=\tau^{-1}
 [s^j]\sum_{k=0}^{j}
   \left|\binom{-a}{k}\right|
   \left(\tau^{-1}\sum_{\ell=1}^{j}t_\ell s^\ell\right)^k.
 \tag{WEX.50}
$$
The zeroth bound $\tau^{-1}$ is exact for the reciprocal majorant and is an outward bound for $t^{-1/2}$, because $0<\tau<1$. Formula (50) is finite Faà di Bruno algebra for real derivatives. It assumes no Taylor-series convergence or complex domain enlargement and requires no new square root or noninteger numerical power.

Let $k^\#=1+t^\#$, with 1 only at degree zero. Complete safe entry-sum jets are
$$
 C^\#=Q^\#*k^\#,\qquad
 \Delta^\#=\tfrac14Q^\#*
     (2x^\#*h^{[1]}+y^\#+y^\#*h^{[1]}),
$$
$$
 h^\#=h^{[1/2]}*k^\#*w_0^\#,\qquad
 w_1^\#=a_1^\#+b_1^\#,
$$
$$
 q_f^\#=\tfrac12Q^\#*
  (x^\#+x^\#*h^{[1]}+2y^\#)*(F_a^\#+F_b^\#).
 \tag{WEX.51}
$$
The two $a_1,b_1$ tables are the saved **free** transport tables. The tail in $h^\#$ is subsequently retained through (29); the genuine amplitude is never substituted for those free tables.

With $\eta_*=|\eta_w|^{-1}$ read from its old complete record, define
$$
 \begin{aligned}
 T_{1,0}^\#={}&\eta_*\{
 ({\mathscr D}^\#)^2(C^\#*w_0^\#)
 +{\mathscr D}^\#(C^\#*w_1^\#)
 +{\mathscr D}^\#(A^\#*\Delta^\#*w_0^\#)\}\\
 &+({\mathscr D}^\#)^2w_0^\#+{\mathscr D}^\#w_1^\#,\\
 T_{1,1}^\#={}&\eta_*{\mathscr D}^\#(C^\#*h^\#)
                                    +{\mathscr D}^\#h^\#,\\
 T_{2,0}^\#={}&\eta_*(\Delta^\#*w_1^\#+q_f^\#
                              +{\mathscr D}^\#(\Delta^\#*w_0^\#)),\\
 T_{2,1}^\#={}&\eta_*\Delta^\#*h^\# .
 \end{aligned}
 \tag{WEX.52}
$$
These preserve every signed term of (21), (22), (30) by a complete positive triangle. They do not subtract norm bounds. The ten outputs in (31) are $j!(T_{i,\ell}^\#)_j$, converting to ordinary derivatives once.

Only orders 0--3 of $A,Q,t,x,y$, 0--2 of $F_a,F_b,a_1,b_1$, and 0--3 of $w_0$ are used. The $y$ table is already the qualified $T_\phi$ table; its order 3 represents the required fourth angular derivative of $T$. All coefficients are evaluated on a domain containing the actual waist. No old producer, old finite reconstruction target, WSM152, WMR42, WMT195, WRT42, WRP40, WSMF52 or W4M30 target is invoked or regenerated.

Sharper same-function coefficient inputs can later supply another complete candidate, but they are not assumed by this first recipe. A candidate's whole set of coefficient and terminal choices must remain internally complete.

## WEX9. Exactly 31 new saved targets and 62 original scalar records

The first standalone consumer has four complete graphs:

| Graph | New targets, in order | Count |
|---|---|---:|
| Fixed terminal coefficients | $F_{1,0,0},F_{1,0,1},F_{1,1,0},F_{1,1,1}$; $F_{2,0,0},F_{2,0,1},F_{2,0,2},F_{2,1,0},F_{2,1,1},F_{2,1,2}$; $M_1,M_2$ | 12 |
| Complete primitive reception | $W_{1,0},K_1,K_2,K_{\rm term},E_{T,0},E_{T,-4/3}$ | 6 |
| Free map and two endpoints | $C_{\rm A},K_F^{\rm flux},E_{\rm sc}^{\rm flux},E_{2,a},E_{2,b},E_2^{\rm flux}$ | 6 |
| Four endpoints and complete errors | $E_{\rm end}^{\rm flux},S_{\rm nr},S_{\rm all},L_{\rm rec}S_{\rm all},C_{\rm whole}^{\rm flux},L_{\rm rec}S_{\rm nr},C_{\rm red}^{\rm flux}$ | 7 |

There are no old-record copies disguised as new targets. The only new square root is (35); all other new operations are rational combinations, finite integer powers, sums and products. No new exponential, logarithm, ODE, quadrature, intrinsic continuation, reference solve or old scientific call is required.

The 62 consumed scalar objects are copied verbatim, together with exact path aliases and complete retained qualifications:

| Source role | Exact scalar paths relative to that original JSON | Count |
|---|---|---:|
| wgs_main | complete_strict_geometry_conclusion.complete_jets.$A,Q,t,x,y$.group_upper[0..3], with $A$ spelled H_inverse_entry_sum | 20 |
| wgs_main | complete_strict_forcing_conclusion.complete_forcing_jets.$F_a,F_b$.group_upper[0..2], spelled Fa/Fb | 6 |
| wgs_main | complete_free_first_transport_conclusion.complete_jets.$a1,b1$.group_upper[0..2] | 6 |
| reconstruction | conclusion.complete_amplitude_ports.w0.normalized_angular_coefficients[0..3] | 4 |
| reconstruction | conclusion.new_complete_constants.complete_density_pair_operator_upper; complete_waist_eta_inverse_upper | 2 |
| free | conclusion.complete_reconstruction_and_map_records.complete_all_eight_symbol_components_upper; complete_Airy_first_cross_upper; complete_Airy_second_remainder_upper; complete_Bi_first_coefficients_two_sign_two_phase_sum_upper | 4 |
| free | conclusion.complete_tail_weights.new_complete_records.complete_Xi0_upper; complete_Xi2_upper | 2 |
| endpoints | conclusion.complete_new_constants.complete_root_scattering_Hminus4_3_to_L2_upper | 1 |
| extension | conclusion.constants.complete_cB_upper | 1 |
| wrp | complete_new_graphs.complete_new_full_output_profile_weights_conclusion.new_records.zero.angle_0; two.angle_0 | 2 |
| wrp | copied_original_scalar_records.Bessel_prefactor; dyadic_two_thirds; two_one_sixth_upper; sqrt_two_upper | 4 |
| current | complete_new_graphs.complete_current_negative_and_whole_receiver.new_records.complete_same_negative_error_upper | 1 |
| current | complete_new_graphs.complete_physical_mean_and_four_waist_endpoints.new_records.complete_physical_mean_endpoint_upper; copied_original_records.old_endpoint_WT | 2 |
| current | complete_new_graphs.complete_current_negative_and_whole_receiver.copied_original_records.provider_Rplus; provider_RF; provider_Calg; provider_D_infinity; provider_Lrec | 5 |
| current | whole_candidate_choices.whole.selected_record; reduced.selected_record | 2 |

The compact math notation in the first two rows is resolved to the literal keys listed there; the implementation contract uses explicit JSON path arrays, not a path pattern.

The companion WGS file supplies no additional scalar target here. It is still read and bound in full, preserving the successful mathematical stage, its separate old formatter status, the original local coefficient object and scope, and its exact same-run/source/manifest relationship. No local complex domain is moved into this real-waist argument.

The reconstruction and extension nodes were complete successes before their original parent run failed at a later, different node. Their complete status, saved count and original binding are retained as such; they are not relabeled as success of that parent's entire run. The later complete free-map/endpoint run and the current WSMF success are admitted independently.

Every new target is atomically persisted with the entire completed/pending graph prefix and printed before a cap check or successor use. Its saved decimal record is then parsed back, and downstream arithmetic reads the directed upper endpoint. Original scalar objects are copied without upper-plus-zero rewriting. Complete graphs, all 31 records and every failure prefix remain available; only operational diagnostic text may be bounded, after the full exception is sent to the job log. Complete whole choices occur after all four graphs have been saved.

This analytic document executes none of these operations. A manifest binds the exact complete source, worker, proof and eight original small JSON files before the first scientific child. A previous successful or mathematical partial attempt locks its targets against automatic rerun.

## WEX10. Complete immutable evidence

The following eight complete original JSON files are the numerical input closure for the first recipe. Each body is smaller than 100000 bytes. Full source paths, byte counts and hashes are retained in the separate explicit consumer contract; they are not replaced by display titles.

| Role | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| wgs_main | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| wgs_copies | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| reconstruction | 7a473349764e3499eb9eec4a1fd95730603229ab | 22953 | 113a03c9beae72e12ac163a0c43d5bc3e057a477b9ba0cfc847f1f52b5b89640 |
| free | d2aa61e0dc1502181a9e86549e81311e8fdacdaf | 14394 | 5f48bdc934047c86ed2fd2d79cb94c593c619cffefb3ac52510fd3c4bfe4b413 |
| endpoints | 13b5b9809e2ba649511613eb5e58ef78f51908dd | 7974 | 7fbee7f580c01944e585f5a763ce5a87717db8c8f59ea789b48f850fe6a75df3 |
| wrp | 146904d030cca0887fae921084396bf4008d0281 | 82508 | 4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee |
| extension | c5d9166b914a17136c5058b3d213afc4dffad5c0 | 12958 | 5816db201af6f0da0f7412c1a1fe0f1521d5425debf37693ab652f152e7fec00 |
| current | c20713f51366ef6c838147232994424bf3e633de | 61398 | 3243348d6dddc11c8baf1f6eb559d929a37c509a464165b7042d1ce47bb2e290 |

Paths are relative to topics/visible-flex-exact-nearby:

- **wgs_main:** `notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json`
- **wgs_copies:** `notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json`
- **reconstruction:** `notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/complete_exact_waist_finite_reconstruction.json`
- **free:** `notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/complete_free_waist_Airy_and_Schur_map.json`
- **endpoints:** `notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/complete_four_waist_endpoint_contributions.json`
- **wrp:** `notes/relative_phase_pullback_receiver_ci/run-43881690924-1/actual-scientific-conclusion.json`
- **extension:** `notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extension_scalars.json`
- **current:** `notes/per_index_strict_flux_complete_mean_ci/run-43886938106-1/actual-scientific-conclusion.json`

The relevant primary proofs are:

| Primary exact role | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WUA.13--15, 18, 21--23: same full forcing, true transport, genuine/free reference and nonzero tail | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WES.1--4, 9--12, 22--32, 36--39: exact free waist and four complete endpoint terms | 02ca30d6e063e9bdfd158d8401361db74e92ce77 | 31293 | 8aa7eb5d210ed73b3e3e2b3c166432292725a603c23dda4d4d9c0a8292d72b00 |
| WZR.3--11: identical waist zeros, full primitive inverse and retained physical mean | 65a382de44ea8f1cff334289865e74fa71ed086d | 14044 | f5e690908c07ebcd121852c3a2b2efdc2c4e0b1bd3d40398c242fa8201a9d249 |
| FA.9, 13, 18--23: exact finite primitive algebra and same first two Airy coefficients | acfb0cfd9a2598c00a6b29c2db05041d0340cba9 | 27814 | 24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af |
| WRP.3--17, 20--22: full mean Bessel measure, complete profile weights and unchanged whole receiver | 9f55708ca3a0a6018279628342fb8715a48ab830 | 16951 | 95be269fc011c756fff2f882a32828ad7293bbaa140c28f0cf6eb5474e674f36 |

The old scattering and second-order values remain saved in the endpoint input. Their large size motivates this new exact decomposition but is not an input to a subtraction. The new coefficients, terminal norms, endpoint bounds and whole candidates are all presently unpaid. The complete current physical mean and WT are retained as original successful objects.
