# R133 supplement: local normalized-weight L1 kernels and a complete six-step mean-source bound

2026-11-16, phase_inverse.

**Proved here:** on the original real local root patch, the complete physical-mean forcing has a new positive bound using normalized angular $L^1$ derivatives of its exact common-weight kernels. The complete genuine radial derivative is retained. Four initial powers of inverse frequency, all six mean operations, and all ten terminal powers remain in the formula. There is no division by $T$ and no extension of the strict transport formula to the root.

The result is a new bound for the same trial and the same physical mean. It reads completed local geometry, physical-coefficient, extended-amplitude and profile records. It neither reruns the completed gamma bridge nor reevaluates the original local mean_N6 graph, the WMR propagator exponentials or the strict WMT graph. No scientific value has been evaluated for this note, and no numerical improvement or smallness gate is asserted.

## WML1. Original real patch and exact objects

Keep the original physical frequency and cutoff:
$$
 n=4|j|\ge N_0=388,\qquad \epsilon=\operatorname{sgn}j,\qquad z_n=n^{-1}.
 \tag{WML.1}
$$
The inverse-frequency symbol $z_n$ is distinct from the physical mean $z_{\rm ph}$. The physical local interval is
$$
 I_\ell=[r_c,r_*],\qquad
 r_c=\frac{76285779072683}{320000000000000},
 \qquad
 r_*\in
 \left[\frac{1191984371497}{5000000000000},
       \frac{2383968743003}{10000000000000}\right].
 \tag{WML.2}
$$
The upper enclosure in (WML.2) is denoted $r_+$. Both rational endpoints are the original root enclosure, without decimal conversion. All real local coefficient bounds are used only on their original $[r_c,r_+]$ in germ 2549, and the physical negative solution is restricted to $I_\ell$. Its initial condition remains $z_{\rm ph}(r_*)=0$. The enclosure endpoint $r_+$ is used only in the already qualified length bound.

Use the WUA/WEJ height and the original full genuine root matrix $C_n$, including its $\beta_n$:
$$
 f_n=P n^{7/6}{\cal U}_{n,\epsilon}^{\rm ext}
              (w_0+z_nw_1^{\rm ext}),
 \qquad
 w_0=(a_0,b_0^{\rm amp})^t,\quad
 w_1^{\rm ext}=(a_1^{\rm ext},b_1^{\rm ext})^t.
 \tag{WML.3}
$$
The notation $b_0^{\rm amp}$ distinguishes an amplitude component from the radial mean coefficient below. The extended first amplitude contains the complete $B_{\rm ext}K_Tw_0$ potential addition. Both original reference columns and both physical frequency signs retain their original roles.

Write
$$
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},\quad
 H=i\epsilon X_\phi Id+T_\phi K_T,\quad
 M_r=i\epsilon X_rId+T_rK_T,\quad
 {\cal A}_n=\partial_\phi-z_n V_{\rm ext}T_\phi E_{12}.
 \tag{WML.4}
$$
The complete genuine derivative identities are
$$
 \begin{split}
 \partial_\phi{\cal U}^{\rm ext}(a)
       &=n{\cal U}^{\rm ext}(Ha)+{\cal U}^{\rm ext}({\cal A}_na),\\
 \partial_r{\cal U}^{\rm ext}(a)
       &=n{\cal U}^{\rm ext}(M_ra)
          +{\cal U}^{\rm ext}(\partial_ra-z_nV_{\rm ext}T_rE_{12}a).
 \end{split}
 \tag{WML.5}
$$
They hold in the local analytic regular packet, including its real root limit. The saved local $H^{-1}$ is the inverse of this complete matrix. Its qualification uses the original nonvanishing regular determinant, not a lower bound for $-T$. The matrices $C_n$ depend on the input index and are not differentiated in $r$ or $\phi$.

All amplitudes and matrix coefficients used in angular integration are periodic. The phase itself is a degree-one lift, but the integer physical frequency makes the complete profile periodic. Only $X_r$ and qualified positive angular derivatives are used; no value of an omitted phase lift is invented.

## WML2. The same complete physical-mean functional

Let $m=\Pi v$, $\alpha=2\beta/\eta$ and
$$
 a_J=\exp(-\alpha I(uv)),\qquad
 w_J=1-\alpha uIv,\qquad
 D_J=\Pi(a_Jw_J),\qquad p_J=a_J/D_J.
 \tag{WML.6}
$$
Here $\beta$ is the metric logarithmic derivative, $\eta$ is the positive characteristic coefficient, and neither is the fixed intrinsic parameter named $\eta_0$. The signed physical mean $m$ is not assumed positive.

The same original angular inverse and the complete mean equation give the exact WMF kernels
$$
 \begin{split}
 e&=-\alpha m I(p_Ju),\\
 b_{\rm m}&=\beta(1-\Pi S),\\
 e_\kappa&=-b_{\rm m}e
           +2\beta mP\left[p_J\left(Kv-\frac{du}{\eta}\right)\right],\\
 F_{{\rm mean},n}
       &=\Pi(e\,\partial_rf_n+e_\kappa f_n),\\
 (z_{\rm ph})_r&=a_{\rm eff}z_{\rm ph}-F_{{\rm mean},n},
                     \qquad z_{\rm ph}(r_*)=0 .
 \end{split}
 \tag{WML.7}
$$
The formula for $e_\kappa$ is the full identity
$-H_2^*e+2\beta mK(v-m)$ after the two exact common-weight cancellations of WMF. It is not a bound for a selected part of that adjoint. In particular the material drift is $\partial_r-d\partial_\phi$, with its original sign.

Both $e$ and $e_\kappa$ have zero angular mean. Thus the $P$ in (WML.3) is removed only inside these two pairings. This does not remove $P$ from the physical trial or from a different operator.

On the same real local patch the completed WMR qualification gives
$$
 |\alpha|<\tfrac12,\qquad
 \|u\|_\infty<1,\qquad
 \|Iv\|_\infty<\tfrac12,\qquad
 w_J\ge\tfrac34 .
 \tag{WML.8}
$$
The exact weight is positive, and
$$
 \Pi(p_Jw_J)=1,\qquad
 p_J>0,\qquad
 \|p_J\|_1=\Pi p_J\le\tfrac43,\qquad
 (p_J)_\phi=-\alpha uvp_J .
 \tag{WML.9}
$$
It is $p_Jw_J\,d\phi/L$, not $p_J\,d\phi/L$, that has total mass one. These statements concern real coefficients. No positivity on the old complex coefficient disk is inferred.

The original angular reflection has $u$ odd and $v$ even. Consequently $p_J$ is even and $\Pi(p_Ju)=0$. The identity
$e_\phi=-\alpha mp_Ju$ therefore contains no omitted mean term. This proof does not use a radial derivative of $e$ because the functional in (WML.7) is $e\,f_r$, not $(ef)_r$. Any later radial integration by parts would have to restore $e_r$ and every endpoint and interface term.

## WML3. Complete normalized L1 kernels through order six

Use normalized angular measure on the circle of length $L=\pi/2$. Define
$$
 [a]_{j,\infty}=\|\partial_\phi^ja\|_\infty/j!,
 \qquad [a]_{j,1}=\|\partial_\phi^ja\|_1/j!.
 \tag{WML.10}
$$
Vector norms are sums of component norms and matrix norms are sums of entry norms. If $(a*b)_j=\sum_{i=0}^ja_i b_{j-i}$, products of normalized derivative bounds use this convolution without an extra binomial coefficient. Differentiation sends a bound array $a_j$ to $(j+1)a_{j+1}$.

Let $U_j,V_j,d_j$ bound the original $u,v,d$ in the first norm of (WML.10), for $0\le j\le6$. They are read from the completed local physical-coefficient A0 graph. The embedding from that complete Fourier-Wiener norm to the pointwise norm has constant one. In particular, the old raw coefficient arrays with angular columns zero through four are not mislabeled as already containing angular orders five and six.

Read complete same-patch bounds
$$
 A\ge|\alpha|,\quad M\ge|m|,\quad
 B\ge|\beta|,\quad K^+\ge|K|,\quad b^+\ge|b_{\rm m}|,
 \qquad 0<\eta_-\le\eta .
 \tag{WML.11}
$$
The existing WMR local qualification record supplies $A$; the existing local_V bound supplies $M$. The fixed rational bounds in (WML.8) justify (WML.9) but do not replace those smaller completed records in the positive recipe.

Put $h_j=A(U*V)_j$ and define
$$
 \begin{split}
 {\mathsf p}_0&=\tfrac43,\\
 {\mathsf p}_{j+1}
       &=\frac1{j+1}\sum_{i=0}^j h_i{\mathsf p}_{j-i},
                         &&0\le j\le5 .
 \end{split}
 \tag{WML.12}
$$
Differentiating the last identity in (WML.9) proves
$[p_J]_{j,1}\le{\mathsf p}_j$ through order six. No separate exponential norm of $a_J$ or inverse-denominator derivative is evaluated.

For the complete zero-mean primitive, the normalized convolution kernel is
$K_I(t)=L/2-t$ on $0<t<L$. Therefore
$$
 \|I\|_{L^1\to L^1}\le\pi/8<11/28 .
 \tag{WML.13}
$$
The rational inequality follows, for example, from
$\int_0^1 x^4(1-x)^4/(1+x^2)\,dx=22/7-\pi>0$.
The rational $11/28$ is an outward bound, not an asserted value of $\pi/8$. The $L^2$ or Fourier-Wiener primitive bound $1/4$ is not substituted here.

Define
$$
 \begin{split}
 {\mathsf e}_0&=AM(11/28){\mathsf p}_0U_0,\\
 {\mathsf e}_j&=\frac{AM}{j}({\mathsf p}*U)_{j-1},
                                  &&1\le j\le6,\\
 \zeta_j&=K^+V_j+\eta_-^{-1}(d*U)_j,\qquad
 \rho_j=({\mathsf p}*\zeta)_j,\\
 {\mathsf k}_0&=b^+{\mathsf e}_0+4BM\rho_0,\\
 {\mathsf k}_j&=b^+{\mathsf e}_j+2BM\rho_j,
                                  &&1\le j\le6 .
 \end{split}
 \tag{WML.14}
$$
Then $[e]_{j,1}\le{\mathsf e}_j$ and
$[e_\kappa]_{j,1}\le{\mathsf k}_j$ for every $j=0,\ldots,6$.
Only the degree-zero projected term pays $\|P\|_{L^1\to L^1}\le2$. Positive angular derivatives annihilate its constant output. All six positive derivative orders of $e_\kappa$ are retained.

This first new graph has exactly 21 scalar records: seven $\mathsf p$, seven $\mathsf e$ and seven $\mathsf k$ records. It has no gamma, $D_J$, $a_J$ or old WMR recomputation.

## WML4. Four complete local forcing amplitudes

The genuine radial identity (WML.5) and the exact pairings (WML.7) give
$$
 F_{{\rm mean},n}
     =n^{13/6}\Pi{\cal U}^{\rm ext}
          (A_0+z_nA_1+z_n^2A_2+z_n^3A_3),
 \tag{WML.15}
$$
where
$$
 \begin{split}
 A_0&=eM_rw_0,\\
 A_1&=eM_rw_1^{\rm ext}+e\,\partial_rw_0+e_\kappa w_0,\\
 A_2&=e\,\partial_rw_1^{\rm ext}+e_\kappa w_1^{\rm ext}
                              -eV_{\rm ext}T_rE_{12}w_0,\\
 A_3&=-eV_{\rm ext}T_rE_{12}w_1^{\rm ext}.
 \end{split}
 \tag{WML.16}
$$
In particular, the complete $w_{1,r}^{\rm ext}$ remains in $A_2$. The potential term is present in both $A_2$ and $A_3$, including the entire extended cutoff and tail. No strict formula involving $1/T$ has been used, and no positive-frequency term has been dropped.

Here is a complete positive recipe. Let $t,x^{(r)},t^{(r)},v^e$ be the normalized pointwise arrays for $T,X_r,T_r,V_{\rm ext}$. Let $a_0,b_0^{\rm amp},a_1^{\rm ext},b_1^{\rm ext}$ and their first radial derivatives have their complete saved normalized pointwise arrays. Put
$$
 \begin{split}
 W_0&=a_0+b_0^{\rm amp},&
 W_1&=a_1^{\rm ext}+b_1^{\rm ext},\\
 W_{0r}&=a_{0,r}+b_{0,r}^{\rm amp},&
 W_{1r}&=a_{1,r}^{\rm ext}+b_{1,r}^{\rm ext},\\
 R_j&=2x^{(r)}_j+
          \{t^{(r)}*(\mathbf1+t)\}_j,\qquad0\le j\le6 .
 \end{split}
 \tag{WML.17}
$$
The array $\mathbf1$ is one at degree zero and zero elsewhere. The factor two in $R$ is the entry-sum norm of the scalar identity matrix in $M_r$.

For $0\le j\le6$ define
$$
 \begin{split}
 {\mathsf A}_{j,0}
    &=({\mathsf e}*R*W_0)_j,\\
 {\mathsf A}_{j,1}
    &=({\mathsf e}*R*W_1)_j
         +({\mathsf e}*W_{0r})_j+({\mathsf k}*W_0)_j,\\
 {\mathsf A}_{j,2}
    &=({\mathsf e}*W_{1r})_j+({\mathsf k}*W_1)_j
         +({\mathsf e}*v^e*t^{(r)}*b_0^{\rm amp})_j,\\
 {\mathsf A}_{j,3}
    &=({\mathsf e}*v^e*t^{(r)}*b_1^{\rm ext})_j .
 \end{split}
 \tag{WML.18}
$$
Each line bounds the whole corresponding vector in (WML.16) in normalized angular $L^1$. The $E_{12}$ terms use the actual second component. Multiplication of a scalar $e_\kappa$ by a vector is bounded directly and is not replaced by an unnecessary two-entry matrix norm.

This second graph contains seven $R_j$ records and all $7\times4=28$ amplitude records, for 35 new records. Working products in (WML.17)--18 are parts of these declared whole formulas; they are not substituted for earlier saved target objects.

## WML5. Six exact angular means and every terminal degree

Let $A(z)=\sum_{k=0}^3z^kA_k$. Define the finite exact sequence
$$
 v_0=H^{-1}A,\qquad
 v_{\ell+1}=-H^{-1}{\cal A}_n v_\ell,\qquad0\le\ell\le4 .
 \tag{WML.19}
$$
Periodicity and the first identity of (WML.5) give
$$
 \Pi{\cal U}^{\rm ext}(A)
       =-n^{-6}\Pi{\cal U}^{\rm ext}({\cal A}_nv_5).
 \tag{WML.20}
$$
No radial integration by parts occurs in this argument. The sixth operation is the displayed terminal, and is not replaced by a zero remainder.

Let $H_j^+$ bound the entry-sum normalized derivatives of $H^{-1}$ through order six, and let
$c_j=(v^e*y)_j$, where $y_j$ bounds
$[\partial_\phi T]_{j,\infty}$. Complete positive recurrences are
$$
 {\mathsf V}^{[0]}_{j,k}
      =\sum_{a=0}^j H_a^+{\mathsf A}_{j-a,k},
       \qquad 0\le j\le6,\quad0\le k\le3 .
 \tag{WML.21}
$$
For $\ell=0,\ldots,4$ use
$$
 \begin{split}
 {\mathsf D}^{[\ell]}_{j,k}
      &=(j+1){\mathsf V}^{[\ell]}_{j+1,k}
           +\sum_{a=0}^j c_a{\mathsf V}^{[\ell]}_{j-a,k-1},\\
 {\mathsf V}^{[\ell+1]}_{j,k}
      &=\sum_{a=0}^jH_a^+{\mathsf D}^{[\ell]}_{j-a,k},
       \qquad
       0\le j\le5-\ell,\quad0\le k\le4+\ell .
 \end{split}
 \tag{WML.22}
$$
Only polynomial coefficients outside their actual degree range are exact zero. Missing geometric derivative entries are not filled with zero. Every product is an $L^\infty$ matrix or coefficient bound times an $L^1$ vector bound.

The complete terminal is
$$
 {\mathsf T}_k={\mathsf V}^{[5]}_{1,k}
                +c_0{\mathsf V}^{[5]}_{0,k-1},
           \qquad0\le k\le9 .
 \tag{WML.23}
$$
The level counts are
$$
 7\!\times\!4,\quad6\!\times\!5,\quad5\!\times\!6,\quad
 4\!\times\!7,\quad3\!\times\!8,\quad2\!\times\!9,
 \tag{WML.24}
$$
followed by ten terminal records. These are 168 records before the final complete source record.

Read the original complete pointwise constant $P_{\star,\ell}$ for one signed genuine reference column from the saved local profile node. The new source candidate is
$$
 \boxed{\;
 C_{F,\ell}^{\,L^1}
      =2P_{\star,\ell}\sum_{k=0}^9 N_0^{-k}{\mathsf T}_k,\qquad
 |F_{{\rm mean},n}(r)|
       \le C_{F,\ell}^{\,L^1}n^{-23/6}\quad(r\in I_\ell).
 \;}
 \tag{WML.25}
$$
The reflected assembly factor two is exactly the factor in the original local mean_N6 node. It does not eliminate an independent second reference or source port. The exponent is $13/6-6=-23/6$. The frequency in the terminal weights is $388$, not the Fourier label $97$.

Equation (WML.25) uses a pointwise genuine profile multiplied by an angular $L^1$ amplitude. It does not turn WGS component-sup jets into Fourier-Wiener norms, use a single-column estimate as a full output operator theorem, or alter a Hilbert-Schmidt threshold. The third new graph has 169 records, and the complete local core has $21+35+169=225$ new records.

## WML6. Typed use of the completed local records

The local derivative requirements are finite and already covered by the complete saved objects. The following table specifies the actual quantities used, not new values inferred from an unqualified raw array.

| Exact input object | Required derivatives and interpretation |
|---|---|
| physical_coefficients_local.complete_A0_jets.U, V, d | Pure angular orders 0 through 6; complete A0 bounds imply pointwise bounds with constant one |
| WGS complete_local_regular_packet_conclusion.complete_jets.T | Pure angular orders 0 through 6, and ordinary radial order one with angular orders 0 through 6 |
| The same local X_minus_phi | Radial order one with angular orders 0 through 6; this is exactly $X_r$, with no identity correction |
| The same local a0, b0 | Pure angular orders 0 through 6 and radial-one/angular-zero-through-six |
| The same local H_inverse_entry_sum | Pure angular orders 0 through 6, with its complete regular determinant qualification |
| extended_amplitude_local.complete_jets.a1_ext, b1_ext | Pure angular orders 0 through 6 and radial-one/angular-zero-through-six; complete potential correction retained |
| extended_amplitude_local.complete_jets.Vext | Pure angular orders 0 through 6, from the full fixed cutoff and potential |
| profile_block_local.new_complete_records.single_signed_point_profile_upper | One complete signed genuine reference-column pointwise bound |
| WMR local_V, local_beta, local_Kabs, local_base, local_eta_lower | Complete same-patch scalar bounds in (WML.11); only eta_lower supplies a positive lower endpoint |
| WMR qualification_local_alpha, qualification_local_U, qualification_local_Iv | Complete original records establishing the same real positive-weight domain |
| The completed mean_gamma_bridge.interval_length_upper | The already saved outward upper for $r_+-r_c$; no gamma-bridge target is repeated |

The actual group convention is a bound for
$\|\partial_r^a\partial_\phi^b q\|/(a!\,b!)$, using the fixed groups
$$
 [0,0],[1,1],[2,2],[3,3],[4,4],[5,6],[7,9],[10,12],[13,15].
 \tag{WML.26}
$$
A pure angular coefficient of degree $j$ therefore reads the group containing $j$ directly. A radial-one coefficient normalized only by $j!$ reads the group containing $1+j$, again directly because $1!=1$. If one instead displays an ordinary derivative, the factor $j!$ must be restored. An angular differentiation such as $y_j=[T_\phi]_{j,\infty}$ uses $(j+1)t_{j+1}$.

The radial-one maximum here has total degree seven. The saved WGS leading shapes [14,3], geometry [15,3] and regular inverse [13,2], together with the extended-amplitude shape [12,2], cover all requests. No request for $(0,0)$ of an omitted phase lift is made. If the derivative $X_\phi$ is used in another implementation, the exact identity contribution must be added to the derivative of X_minus_phi; it is absent from $X_r$.

The original c.U and c.V tables have shape 4 by 5, and c.D has only its original six angular entries. This proof does not obtain orders five and six by relabeling those raw tables. It reads the already completed physical_coefficients_local graph, whose full A0 shape is [14,1]. Thus the original strip-based continuation costs have already been paid and saved. That complete graph is not run again.

For reference, the complete immutable predecessors already checked for this note are:

| Object and repository-relative path below the topic | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/physical_coefficients_local.json | 8e04fca88d61b2f38152302cac8527ab8326d5df | 15904 | ee16b343c4dff938c0d56ce29f906b55a4fff250ff68c98c49e47d138b4c614a |
| notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extended_amplitude_local.json | 7a749edb97b3181581157ff60d37cbaec0586ef7 | 9416 | bdcce134a6db6b1fd3de738d4eccfd2f404fb7316f1df8cf008390fd7331d4f5 |
| notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/profile_block_local.json | 4b10ca03cb4f5a419f1e30f4ba3d8ab1a997ccbb | 9096 | b1ceba8254efd75ca500a0c26e47f7440bdf61b252eecaf5aa8c68a4c5102676 |
| notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/mean_gamma_bridge.json | 679a1d15e5814c3f3a88b1b786d279212189de3f | 3497 | 00e1566b0a0641f5f92e04c6b5fe20b108f4e314be181afa39e17614d748ba48 |
| notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/actual-scientific-conclusion.json | 5fdb01ed62008489bca34a4b6231519af4f60793 | 51030 | 39a2d96accdbe1b4a8073674cabeda97878876f11fc24a055b910ed61567b432 |

The three complete local posterior nodes have their original problem-id suffixes, twelve-original-input map, five-module map and direct-dependency receipts. They are successful nodes within the original failed attempt; that attempt is not relabeled successful. Their original parameter hash is
0940b91abbfb830015c5111c86896e6e92030c7de4c83974dad964245a34f65a.
The actual WGS main and companion are paired by the complete three-key filename/byte-count/SHA256 reference and their original run, source, module, manifest and commit identities.

The local source qualification continues to distinguish the exact complete coefficient radius 3/8000, its angular strip 1/32 and the original auxiliary-input radius 1/2000. The functional identities are used only on the original germ intersection. The gamma bridge uses row 790's mean lower at the cut and its own saved Lipschitz argument; it does not extend that row's other norms or complex domain.

## WML7. Complete physical propagation and unchanged receivers

Let $C_s$ denote one fixed, already completed whole strict forcing bound with the original power $n^{-23/6}$. It can be the original WMR strict_CF. If the strict WMT consumer has completed before a new WML numerical package is frozen, its complete strict flux record can instead be pinned and read verbatim. The latter is not a numerical input until that actual record exists. No value is filled from the analytic WMT recipe and no WMT target is recomputed.

Write $C_\ell=C_{F,\ell}^{\,L^1}$. Read the saved WMR complete backward factors $G_\ell,G_s$, absolute coefficients $A_\ell,A_s$, complete residual-action bounds $T k_\ell,T k_s$, and the original $k_{0,p}$ and $I k_p$ bounds. Read the already completed bridge length $h_\ell^+$ for $r_+-r_c$. Then the same scalar equation in (WML.7) gives the complete candidates
$$
 \begin{split}
 Z_\ell&=G_\ell h_\ell^+ C_\ell,&
 Z_\ell'&=A_\ell Z_\ell+C_\ell,\\
 Z_s&=G_s(r_c C_s+Z_\ell),&
 Z_s'&=A_sZ_s+C_s .
 \end{split}
 \tag{WML.27}
$$
The prime on $Z_p'$ denotes a bound for the absolute ordinary radial derivative of the same physical mean. It is not a derivative of the positive scalar bound $Z_p$. The absolute coefficient $A_p$, not the one-sided backward coefficient, is used in the derivative line.

The original factors $G_\ell,G_s$ are read as complete saved records. Neither of their two exponentials is evaluated again. The real initial condition remains at $r_*$; the enclosing length is used only to dominate the actual integral.

The complete mean-dependent raw and primitive sources are
$$
 M_p=k_{0,p}Z_p'+(Tk_p)Z_p,\qquad
 \widetilde M_p=(Ik_p)Z_p'+\tfrac14(Tk_p)Z_p,
                      \qquad p\in\{\ell,s\}.
 \tag{WML.28}
$$
These are the whole WMR affine terms for the same $g_1$ residual. The terms involving $k_r$, drift, reaction and $b_1$ remain inside the already completed $Tk_p$. The factor $1/4$ in this equation is used only for the original odd L2 primitive. It is independent of the L1 constant in (WML.13).

For completeness, the remaining source/reception formulas are stated with the exact existing-record aliases. Let old(q) mean the upper endpoint of the complete saved record with that alias in WMR.copied_original_scalar_records. Put $M_c=\max(M_s,M_\ell)$. The complete ordinary source quantities are
$$
 \begin{split}
 S_c={}&\operatorname{old}(\texttt{sqrt\_two\_upper})\,
        \operatorname{old}(\texttt{ell\_plus\_one\_fourth\_upper})\\
      &\quad\cdot\bigl[
         \operatorname{old}(\texttt{collar\_B\_union})
           +\operatorname{old}(\texttt{collar\_T\_union})
                    \operatorname{old}(\texttt{N\_minus5\_6\_upper})\bigr]\\
      &+\operatorname{old}(\texttt{sqrt\_ell\_plus\_upper})\,M_c\,
                       \operatorname{old}(\texttt{N\_minus5\_3\_upper}),\\
 S_s={}&c_{\rm PW}\bigl[
        \operatorname{old}(\texttt{ell\_minus\_negative\_fourth\_upper})
         \{\operatorname{old}(\texttt{strict\_B\_t})
           +\operatorname{old}(\texttt{strict\_T\_t})
                   \operatorname{old}(\texttt{N\_minus1\_2\_upper})\}\\
      &\hspace{35mm}
         +\widetilde M_s\operatorname{old}(\texttt{N\_minus4\_3\_upper})\bigr],
 \qquad
 c_{\rm PW}=\frac{2333968743003}{10000000000000}.
 \end{split}
 \tag{WML.29}
$$
All nonmean block and terminal quantities in (WML.29) are unchanged. The two original cuts $c_{\rm PW}$ and $r_c$ are not identified with one another.

The complete received error is
$$
 \begin{split}
 R_c&=\operatorname{old}(\texttt{C\_O})S_c
                  +\operatorname{old}(\texttt{C\_R})
                     \operatorname{old}(\texttt{jump\_collar}),\\
 R_s&=\operatorname{old}(\texttt{C\_1})
                    [S_s+\operatorname{old}(\texttt{jump\_strict})],\\
 C_{\rm neg}&=\operatorname{old}(\texttt{Bessel\_prefactor})
       [R_c\operatorname{old}(\texttt{dyadic\_one\_third})
         +R_s\operatorname{old}(\texttt{dyadic\_two\_thirds})].
 \end{split}
 \tag{WML.30}
$$
The old full jump records retain every original true seam. No change of trial, radial cutoff or radial integration by parts has occurred, so these jumps are exactly the same objects. The old exponents, Bessel conversion, ordinary radial lengths and full receiver windows are preserved.

Only the physical-mean part of the waist endpoint changes:
$$
 \begin{split}
 E_{\rm mean}
       &=\operatorname{old}(\texttt{endpoint\_Vz})\,Z_s\,
                               \operatorname{old}(\texttt{Xi23\_6}),\\
 E_{\rm end}
       &=\operatorname{old}(\texttt{endpoint\_scattering})
         +\operatorname{old}(\texttt{endpoint\_second\_order})
         +\operatorname{old}(\texttt{endpoint\_WT})+E_{\rm mean}.
 \end{split}
 \tag{WML.31}
$$
The $q$ contribution to the original endpoint_Vz norm retains both stored physical mean entries. Neither of those entries, the full physical $z_{\rm ph}$, nor an external mean equation is discarded.

Finally use the two existing operator realizations, with their original left readout once:
$$
 \begin{split}
 S_{\rm nonroot}&=\operatorname{old}(\texttt{Rplus})+C_{\rm neg}+E_{\rm end},\\
 S_{\rm all}&=S_{\rm nonroot}+\operatorname{old}(\texttt{RF}),\\
 R_{\rm whole}&=\operatorname{old}(\texttt{Lrec})S_{\rm all},&
 C_{\rm whole}^{\rm new}
       &=\operatorname{old}(\texttt{Calg})+R_{\rm whole},\\
 R_{\rm reduced}&=\operatorname{old}(\texttt{Lrec})S_{\rm nonroot},&
 C_{\rm reduced}^{\rm new}
       &=\operatorname{old}(\texttt{D\_infinity})+R_{\rm reduced}.
 \end{split}
 \tag{WML.32}
$$
RF and the independently separated coefficient finite factor remain in their exact realization. D_infinity is not relabeled as whole Calg. Every $n_g$, NIF coordinate, inverse factor, endpoint norm and source reception is used only where its original saved complete formula places it.

The numerical design, if later frozen, uses one fixed new local branch throughout (WML.27)--32. It may compare only the completed new whole bound with a previous complete bound for the same whole operator, and only the completed new reduced bound with the previous bound for that same reduced operator. All candidates remain stored, the old candidate wins a tie, and no individual positive term is selected from different decompositions. An old winner is copied, not recomputed.

## WML8. New targets, old targets and retained open work

A fixed complete numerical shape for the local branch and full reassembly has seven graphs:

| Ordered graph | Complete record content | New scalar records |
|---|---|---:|
| local_normalized_weight_L1_kernels | p[0..6], e[0..6], e_kappa[0..6] | 21 |
| local_complete_radial_forcing_amplitudes | Mr entry-sum[0..6] and four full amplitude arrays, each [0..6] | 35 |
| local_complete_six_mean_steps | All six inverse levels in (WML.24), all ten terminal coefficients, one whole CF record | 169 |
| complete_two_patch_physical_mean | Both Z/Zr and both raw/primitive mean-source terms in (WML.27)--28 | 8 |
| complete_negative_receiver | M_c, S_c, S_s, R_c, R_s and C_neg | 6 |
| complete_waist_endpoint | Complete physical-mean endpoint and sum of all four endpoints | 2 |
| complete_whole_and_reduced | The six complete records of (WML.32) | 6 |
| **Total** | **225 local-core records plus 22 complete reassembly records** | **247** |

No new exponential, logarithm, gamma bridge, fixed genuine root matrix, WMR propagator, original strict CF, strict WMT target, original negative nonmean target or original endpoint constant is among these 247 targets. The full scalar objects read from the previous actual results retain their original strings and types. The same applies to all consumed scope objects and all array positions in their non-ball qualifications.

A publication model must include all 247 new records, the complete consumed old records, full qualifying scopes and original input identities. If a complete single-file model exceeds its cap, a natural companion containing all complete original records and scopes may be used only with a full filename/bytes/SHA256 binding and a validator that requires both files. No scope, terminal, old record or computed partial prefix may be removed to fit a cap.

The same physical object is preserved throughout: the real mean initial condition at the true root, both stored means, original root matrix and beta_n, all ordinary radial pieces and 3070 true interfaces, original local gamma bridge, and the unchanged positive/root/waist decomposition. The independent parameter nu, waist amplitude, external mean, radial head functions, complete matching rows and actual 96 physical columns with their still uncomputed signed normalization remain separate.

The result supplies neither a signed finite inverse, a physical Poisson onto theorem, a completed head inverse, a finite determinant certificate nor a nonlinear background solution. The WMR and WMT values remain frozen. A new local source bound becomes numerical evidence only after its own complete current-input qualification and single authorized scientific execution.

## WML9. Primary proof chain and independent checks

The exact identities and types used above are from the following complete source objects:

| Source | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WMF: exact normalized-weight physical-mean forcing | 2c4a1789195a1ea400ef7c547b319ea3f4f7329f | 15111 | 14900631ba2d793977336fd5f7e8870e4313cbda50a8a8c3e02fa11b53054356 |
| WUA: same global genuine trial and derivative rules | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WEJ: complete original local N6 and physical source | da9d8461ca406a1c6f4b829a91147a860133567f | 59644 | 6b7644a978915550b5835b3492eda3bffde872b8e92f16c2db6c4538e405be8f |
| WMR: same complete propagation and error reassembly | a7b23dea9a96dfab74475d382ca2d1df8edd5b8e | 31643 | 550866c05d9a07d3e4b037e5840a4f75b66a7f3a9304c5cd0d52e4f2b7e729a6 |
| WMT: strict flux bound, whose strict reciprocal is not used here | c8049ef93eca8f84f135ab4338d6485081fb8424 | 31256 | 51eb08d0b110b8a5b171538c3be023efb94df587fdab880ebddac518665f73ce |
| GMR: completed local bridge and exact reuse | bb72e319a7143c098ac0b4747928552da55b6384 | 12615 | f03b79bc5577a4f6e8bd5fe333916b7b5abad7f93250ac008a5e8ccaa0faa7e2 |
| Original posterior support source, read as text only | d4f887d637a709331977ef24cd48d930ea396b40 | 73459 | c42b14e13c7357bb3aa60447ee8679592e0948fffe11f7ecdd846fc554bafdf4 |

The author read the complete small actual objects in WML6 and returned to the complete_local_regular_packet, complete_mean_kernel_patch and complete_mean_N6_patch definitions as text. The old complete local polynomial indeed has four initial degrees and retains terminal degrees zero through nine. The new proof changes the full kernel norm before that same exact mean identity; it does not subtract an old subtotal from a saved upper.

Tail independently checked the real local p mass bound, normalized L1 derivative recurrence, primitive constant, full projected e_kappa through order six and the actual mixed-group convention. The initially available raw c tables alone would not have supplied angular orders five and six; the completed physical_coefficients_local graph was then identified and checked as their read-only full A0 predecessor. These checks were symbolic and textual.

No scientific Python, Arb operation, old producer, restoration, old target evaluation or new numerical target evaluation was performed to prepare this proof. Exact JSON comparisons and byte/hash checks of complete existing files are distinct from mathematical execution.
