# R133 supplement NIF: uniform common-input coordinates with one frozen selected chart

2026-11-16, newton_source.

**Proved analytic consequence and a minimal new scalar contract.** The accepted selected input chart can be frozen as a coordinate choice on the same original real reference family. The resulting common input spaces are fixed, and their incoming coordinate maps and inverses have uniform bounds in the two required windows. At the certified selected parameter the ambient operator is exactly the old MS normalization; its natural-root restriction uses the precise inverse-image reflected domain given below. This statement does not assert a family of KAM conjugacies or extend a selected principal/Cayley factorization to other parameters.

Only one new forward leading-scalar expression and a finite number of positive products are needed for explicit printed constants. Every coefficient, flow, mean, old exponential, root inverse and natural-window inverse used below has already been completed. No new scientific arithmetic is performed in this note.

## NIF1. Fixed family, reflected root space and selected carrier chart

Use the same continuous repaired reference and intrinsic family
$$
 Q_\delta=Q_0+\delta Z_{\rm can},\qquad
 \nu_\delta=\nu_0+\delta,\qquad
 \eta_{\rm intrinsic}=\eta_0,\qquad |\delta|\le10^{-8}.
 \tag{NIF.1}
$$
The centre and direction definition hashes are respectively
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47 and
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The strict cut is
$$
 r_c=\frac{76285779072683}{320000000000000},
 \qquad
 r_*\in\left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}
 \right].
 \tag{NIF.2}
$$
These are the same root piece and fixed-intrinsic family used in TF, KL, WX and the successful R97 recovery. B sections 2--3 already extend the genuine root construction and the regular positive given-head graph to this full real interval. The intrinsic bump vanishes on the root neighbourhood and the positive interval, and the original complete source columns remain separate. The moving coefficient
$\eta_*=-\gamma_*\langle v_*\rangle>0$ is distinct from $\eta_0$.

There are two different angular spaces here. The signed carrier space is
$\mathcal H_{\rm car}^s=P_{97}H^s$, containing both Fourier signs on the circle of period $\pi/2$ with normalized measure and Bessel weights
$\Lambda_j=(1+16j^2)^{1/2}$. The natural root space
$\mathcal H_{\rm nat}^s$ is the reflected scalar high domain denoted by $\mathcal H_H^s$ in SE/RNI. If
$\mathscr Rf(\phi)=f(-\phi)$, its complexified even realization has projector
$Q_{\rm nat}=P_{97}(1+\mathscr R)/2$. Its real form additionally retains the original Fourier conjugacy.

This is the actual moving convention: N.3 is followed by the explicit statement that $u,h_1$ are odd and $v,h_2$ are even; O.1--2 and SE1 retain it. In particular the old-circle inverse sends even mean-zero scalar data to odd data. It is not enlarged to another domain in this note. Both physical means, the original low complement, the whole radial head and other independent ports stay separate.

The actual strip theorem W.1--W.5 supplies the specific same-family pair $(\delta_*,\mathcal H_*)$ with
$$
 |\delta_*|<9.368259853002\,10^{-11}<10^{-10}<10^{-8}.
 \tag{NIF.3}
$$
It is the pair from public run 43588332723/1 and loss $1/250$, retained in AC and WX, not a parameter identified from another loss. It gives
$$
 \frac{31}{32}\le\mathcal H_*'\le\frac{33}{32},
 \qquad \|\mathcal H_*''\|_\infty\le4,
 \qquad
 \mathcal H_*\circ P_{\delta_*}=\mathcal H_*+\Omega_{15}.
 \tag{NIF.4}
$$
Only this equality at $\delta_*$ is used as a conjugacy statement.

For $U_\psi f=\psi'(f\circ\psi)$, freeze the one already qualified ambient carrier map
$$
 \mathcal S_*=
 U_{\mathcal H_*^{-1}}U_{X_{-,\delta_*}},
 \qquad
 \mathcal S_*^{-1}=
 U_{X_{-,\delta_*}^{-1}}U_{\mathcal H_*}.
 \tag{NIF.5}
$$
This is the original IC/MS order, with
$U_\alpha U_\beta=U_{\beta\circ\alpha}$. WX already supplies
$$
 \|\mathcal S_*\|_{H^s\to H^s}\le K_{\mathcal S,s},
 \qquad
 \|\mathcal S_*^{-1}\|_{H^s\to H^s}\le K_{\mathcal S^{-1},s},
 \quad s=0,-4/3.
 \tag{NIF.6}
$$
They concern this fixed actual map. No family of $\mathcal H_\delta$ is being asserted.

The fixed incoming Maslov phase and the correct frozen natural input space are
$$
 \begin{split}
 D_+&=e^{-i\pi/4}\Pi_+ + e^{i\pi/4}\Pi_-,\\
 \mathcal X_s^{\rm fr}&=\mathcal S_*D_+\mathcal H_{\rm nat}^s,\\
 Q_{\rm nat}^{\rm fr}
   &=\mathcal S_*D_+Q_{\rm nat}D_+^{-1}\mathcal S_*^{-1}.
 \end{split}
 \tag{NIF.7}
$$
The norm is the inherited ambient $H^s$ norm, not a renormalization that removes the costs (NIF.6). The phase $D_+$ is an isometry on every signed high Sobolev space and preserves real Fourier conjugacy, but generally does not preserve the even-reflection subspace.

All uses of $D_+^{-1}$ in (NIF.7) are on the nonmean carrier. The ambient carrier projector is separately
$P_{\rm car}^{\rm fr}=\mathcal S_*P_{97}\mathcal S_*^{-1}$.
Its range is larger than the reflected space in (NIF.7). Neither transported projector is asserted to be orthogonal or a Fourier projector in the final angle. In particular the complement of $Q_{\rm nat}$ in the full signed carrier space is not a finite head.

Below we prove that (NIF.7) is precisely the inverse image of the natural root domain under the old selected ambient $N_{i,\delta_*}$, and also under every new $N_{i,\delta}^{\rm fr}$. At $\delta_*$ the operator formula is exactly the old MS formula with its properly transported physical-reflection constraint. It is not the old literal space $\mathcal S_*\mathcal H_{\rm nat}^s$; that shorthand in SE8 needs the narrow correction stated in NIF9. The fixed spaces in (NIF.7) are identified across $\delta$ by the identity.

## NIF2. Two full-family factors already available

For every real parameter in (NIF.1), retain the actual TF root normalizer
$$
 T_{F,\delta}=1+P_{1024}M_{F_{*,\delta}}IP_{1024},
 \qquad
 F_{*,\delta}=\frac{\beta_*u_*v_*}{\eta_*},
 \qquad \deg F_{*,\delta}\le192.
 \tag{NIF.8}
$$
The full mean of $v_*$ and of $F_{*,\delta}$ is retained. The TFA receipt explicitly covers (NIF.1), including the off-support domain bridge used for its original positive coefficient bounds. It supplies
$$
 \|T_{F,\delta}\|_{H^s\to H^s}\le K_{F,s}^+,\qquad
 \|T_{F,\delta}^{-1}\|_{H^s\to H^s}\le K_{F,s}^-,
 \quad s=0,-4/3 .
 \tag{NIF.9}
$$
The inverse is the same on the common distributional core. The cutoff 1024 is the root normalizer cutoff, not a replacement of the input cutoff 97 or the moving normalizer cutoff.

Both high projections and the degree192 support give the exact commutators of MS.10--12:
$$
 [T_{F,\delta}^{\pm1},P_{97}]
 =[T_{F,\delta}^{\pm1},\Pi_\pm]
 =[T_{F,\delta}^{\pm1},\Lambda_{\sigma,\delta}]=0.
 \tag{NIF.10}
$$
This support argument justifies restriction to the full high carrier. The further natural reflection restriction needs its own fact. In the actual moving convention, $u_*$ is odd, $v_*$ is even and $\beta_*,\eta_*$ are radial, so $F_{*,\delta}$ is odd. Thus
$$
 \mathscr RI\mathscr R=-I,\qquad
 \mathscr RM_{F_{*,\delta}}\mathscr R=-M_{F_{*,\delta}},
 \qquad
 \mathscr RT_{F,\delta}^{\pm1}\mathscr R=T_{F,\delta}^{\pm1}.
 \tag{NIF.10a}
$$
The two sign reversals cancel, and $P_{1024}$ commutes with reflection. Consequently $T_{F,\delta}$ and its same inverse are isomorphisms of $\mathcal H_{\rm nat}^s$. This parity argument neither drops the full mean of $v_*$ nor alters any previously paid complete norm. The original finite difference between the compressed normalizer and its uncompressed first symbol remains separate.

Here $\Lambda_{\sigma,\delta}$ is the original terminal-Ai leading scalar diagonal
$$
 \Lambda_{\sigma,\delta}
 =\ell_{\sigma,+,\delta}\Pi_+
       +\ell_{\sigma,-,\delta}\Pi_-.
 \tag{NIF.11}
$$
It is not the Bessel weight $\Lambda_j$. MS.6--8 and KL.9--11 give, on the original nonmean high carrier,
$$
 \Lambda_{+,\delta}=a_\delta D_+,\qquad
 a_\delta=\frac{n_g(0)}{\sqrt{2\pi}}
       \left(\frac{k_*}{\eta_*}\right)^{1/6}k_{\rm root}(0)>0.
 \tag{NIF.11a}
$$
Indeed $\kappa_{+,\epsilon}=e^{i\epsilon\pi/4}/(2\sqrt\pi)$ and multiplication by $\sqrt2/(i\epsilon)$ gives the fixed phase $e^{-i\epsilon\pi/4}$. Only the common positive modulus varies with $\delta$. All four sign/wave moduli coincide. These statements are restricted to the actual nonmean high carrier: a full-circle auxiliary convention setting the mean multiplier to one does not satisfy the same global scalar-ratio identity.

The successful KL receipt proves, on (NIF.1),
$$
 \|\Lambda_{\sigma,\delta}^{-1}\|_{H^s\to H^s}
       \le K_\Lambda^-,
 \qquad s=0,-4/3.
 \tag{NIF.12}
$$
This is one nonzero carrier diagonal and the same inverse on both windows. Its action on the natural reflected domain has the phase-transported range in (NIF.7); it is not claimed to preserve even functions by itself. It does not cover a second Bi column or another reference normalization.

Thus neither (NIF.9) nor (NIF.12) needs a new enclosure or a new inverse test. What has not yet been printed as a scalar is a complete upper bound for the forward diagonal $\Lambda_{\sigma,\delta}$.

## NIF3. The missing forward leading scalar uses five saved bounds

Keep the exact KL identity, with its complete mean residual,
$$
 |\ell_{\sigma,\epsilon,\delta}|
 =\frac{n_g(0)}{\sqrt{2\pi}}
       \left(\frac{k_*}{\eta_*}\right)^{1/6}
       k_{\rm root}(0),\qquad
 k_*=K_r(r_*),\qquad
 k_{\rm root}(r)=
       \exp\!\left(\int_{r_*}^{r}\ell_0(t)\,dt\right).
 \tag{NIF.13}
$$
Here $n_g=a_{\rm phys}^2/\langle v\rangle^2$ and
$\ell_0=-2\beta\langle u^2+Kv^2\rangle$ are exactly KL.4. No mean is removed. The correlation identity
$E(r)=n_g(r)k_{\rm root}(r)/n_g(r_*)$ was used before taking absolute values; the mean residual was not set to zero.

Use the following already retained bounds:
$$
 n_g(0)\le n_+,\qquad
 0<k_*\le k_+,\qquad
 \eta_*\ge\eta_->0,\qquad
 k_{\rm SF}(0)\le P_{\rm rev},
 \qquad E_{\rm sh}\ge
     \exp\!\left(2B_*M_*^2(r_+-r_c)\right).
 \tag{NIF.14}
$$
The exact saved field locations are in NIF7. In particular $P_{\rm rev}$ is the WX reverse radial exponential bound, while the old KL inverse used the forward bound. Their roles cannot be interchanged by taking reciprocals of upper bounds.

The name of the retained $E_{\rm sh}$ field refers to the inverse root-to-cut factor. Its original derivation, KL.17--18, bounded the absolute integrand:
$|\ell_0|\le2B_*M_*^2$ on the entire short interval. Consequently that same already evaluated positive exponential also bounds the other orientation:
$$
 k_{\rm root}(r_c)\le E_{\rm sh},\qquad
 k_{\rm root}(0)=k_{\rm root}(r_c)k_{\rm SF}(0)
       \le E_{\rm sh}P_{\rm rev}.
 \tag{NIF.15}
$$
This is a new use of the original absolute-rate inequality. It does not recompute its exponential or infer a forward bound from an inverse norm.

It follows that the one new sufficient scalar
$$
 \boxed{\displaystyle
 K_\Lambda^+
 =\frac{n_+\,P_{\rm rev}\,E_{\rm sh}}{\sqrt{2\pi}}
          \left(\frac{k_+}{\eta_-}\right)^{1/6}
 }
 \tag{NIF.16}
$$
bounds $\|\Lambda_{\sigma,\delta}\|_{H^s\to H^s}$ for both waves, both input signs and both windows, uniformly in (NIF.1). No sum or extra $\sqrt2$ is incurred by the sign diagonal. The upper $k_+$ is from the complete body germ containing the short interval, while $\eta_-$ is the original full root coefficient-domain lower bound; neither is a cut-only endpoint substituted at the root.

All five inputs in (NIF.14) are saved complete scalar records. The first, second, fourth and fifth use upward endpoints. The third is a strictly positive lower bound and must use a downward endpoint. A division by its upper endpoint would be invalid. The factor $(2\pi)^{-1/2}$ and the positive sixth root in (NIF.16) are new elementary scalar operations only; the old $E_{\rm sh}$ is read verbatim. Evaluate the negative half power directly with an upper endpoint, or divide by a strictly positive lower endpoint for $\sqrt{2\pi}$; do not divide by its upper bound. The positive one-sixth power is taken on the complete ratio before its upward endpoint is selected.

## NIF4. Uniform coordinate isomorphisms on a fixed space

For every $\delta$ in (NIF.1), define
$$
 \boxed{\displaystyle
 N_{i,\delta}^{\rm fr}
   =\Lambda_{+,\delta}^{-1}T_{F,\delta}^{-1}\mathcal S_*^{-1}
       :\mathcal X_s^{\rm fr}\longrightarrow\mathcal H_{\rm nat}^s ,
 \qquad s=0,-4/3 .
 }
 \tag{NIF.17}
$$
Its two-sided inverse is, in the reverse order,
$$
 \boxed{\displaystyle
 (N_{i,\delta}^{\rm fr})^{-1}
       =\mathcal S_*T_{F,\delta}\Lambda_{+,\delta}.
 }
 \tag{NIF.18}
$$
For $f\in\mathcal H_{\rm nat}^s$, the exact phase cancellation gives
$$
 N_{i,\delta}^{\rm fr}(\mathcal S_*D_+f)
       =a_\delta^{-1}T_{F,\delta}^{-1}f,\qquad
 (N_{i,\delta}^{\rm fr})^{-1}\mathcal H_{\rm nat}^s
       =\mathcal S_*D_+\mathcal H_{\rm nat}^s.
 \tag{NIF.18a}
$$
Here only the proved commutation of $T_{F,\delta}$ with $D_+$ and its genuine reflection invariance are used. Equivalently,
$\mathcal S_*T_{F,\delta}\Lambda_{+,\delta}\mathcal H_{\rm nat}^s
 =\mathcal S_*\Lambda_{+,\delta}\mathcal H_{\rm nat}^s
 =\mathcal S_*D_+\mathcal H_{\rm nat}^s$.
This proves the domain and both inverse identities. No factor is moved through $\mathcal S_*$. The maps are compatible on the common distributional core.

Define the complete positive products
$$
 A_s=K_\Lambda^-K_{F,s}^-K_{\mathcal S^{-1},s},
 \qquad
 B_s=K_{\mathcal S,s}K_{F,s}^+K_\Lambda^+.
 \tag{NIF.19}
$$
Then uniformly over the full real family,
$$
 \|N_{i,\delta}^{\rm fr}\|_{\mathcal X_s^{\rm fr}\to\mathcal H_{\rm nat}^s}
     \le A_s,\qquad
 \|(N_{i,\delta}^{\rm fr})^{-1}\|_{\mathcal H_{\rm nat}^s\to\mathcal X_s^{\rm fr}}
     \le B_s.
 \tag{NIF.20}
$$
At $\delta=\delta_*$, the ambient operator formula (NIF.17) is exactly MS.13 and its admissible natural-root restriction is the inverse-image space (NIF.7). This corrects, rather than repeats, SE8's old unqualified space shorthand. At other parameters it is a newly specified frozen-chart realization. Nothing here asserts
$\mathcal H_*\circ P_\delta=\mathcal H_*+\Omega_{15}$ for $\delta\ne\delta_*$.

The high construction extends to all independently declared ports by the block map
$\operatorname{diag}(N_{i,\delta}^{\rm fr},1_{\rm rest})$ in the appropriate direction. The rest can contain an infinite-dimensional radial source space. It includes both physical means, the original low columns and any genuinely independent second reference datum; it is not silently treated as a finite vector.

A full density pullback preserves the mean functional, but need not fix the constant function. Thus if a comparison is written on a full scalar circle with a mean-identity realization, the exact differences
$U_\psi-(\psi'-1)\Pi$ and their inverse counterparts from WX.20 remain. No such finite-rank correction is deleted by (NIF.17).

## NIF5. Two natural stable windows, with the original weights

The successful R97 recovery and RNE give the same true natural stable inverse on the fixed original root spaces, uniformly for (NIF.1). Write its already printed bounds as
$$
 K_{{\rm nat},t}\ge
 \|S_{{\rm nat},\delta}^{-1}:\mathcal H_{\rm nat}^t\to\mathcal H_{\rm nat}^t\|,
 \qquad t=-7/6,-5/2.
 \tag{NIF.21}
$$
Their retained exact inverse order is
$(1+D_g^{-1}E)^{-1}D_g^{-1}\mathcal M^{-1}$.
They are independent negative-window constants, not the L2 margin bound reused in a negative norm.

Define the new frozen-coordinate stable map by the original SE weight order:
$$
 C_{s,\delta}^{\rm fr}
 =N_{\rm out}^{-1}S_{{\rm nat},\delta}N_{\rm in}^{7/6}
           N_{i,\delta}^{\rm fr}
 :\mathcal X_s^{\rm fr}\longrightarrow\mathcal H_{\rm nat}^{s-1/6}.
 \tag{NIF.22}
$$
The physical input and output frequency weights act only on their original high spaces. No inverse frequency is applied to either independent mean. Since $t=s-7/6$, its exact inverse is
$$
 \boxed{\displaystyle
 (C_{s,\delta}^{\rm fr})^{-1}
 =(N_{i,\delta}^{\rm fr})^{-1}N_{\rm in}^{-7/6}
       S_{{\rm nat},\delta}^{-1}N_{\rm out}.
 }
 \tag{NIF.23}
$$
The two cases are
$$
 \begin{array}{c|c|c}
 s & t=s-7/6 & \text{stable output exponent }s-1/6\\ \hline
 0 & -7/6 & -1/6\\
 -4/3 & -5/2 & -3/2 .
 \end{array}
 \tag{NIF.24}
$$
They use one compatible inverse.

As in RNE.30, $N_{\rm out}$ has norm at most one between the displayed windows, and
$$
 \|N_{\rm in}^{-7/6}\|
 \le\left(\frac{\sqrt{1+388^2}}{388}\right)^{7/6}
 =\left(1+\frac1{388^2}\right)^{7/12}
 \le\Gamma_{97}:=\frac{150545}{150544}.
 \tag{NIF.25}
$$
The final rational bound is deliberately retained as a harmless complete upper bound; it does not reevaluate a previous geometric scalar. Therefore
$$
 \boxed{\displaystyle
 \|(C_{s,\delta}^{\rm fr})^{-1}\|
       \le \Gamma_{97}\,B_s\,K_{{\rm nat},s-7/6},
       \qquad s=0,-4/3 .
 }
 \tag{NIF.26}
$$
These are two new positive products of the old natural inverse bounds and the coordinate factors in (NIF.19). No RNE polynomial or R97 strict comparison is rerun.

For completeness the forward maps are also uniformly bounded. RNI.1--4 and RNE give a finite common $g_+$ and complete gains
$\|E_\delta:H^t\to H^{t+2/3}\|\le e_t$ at these two exponents. Since $\|\mathcal M_\delta\|\le1$, the unit-norm embedding gives
$\|S_{{\rm nat},\delta}\|_{H^t\to H^t}\le g_++e_t$. The positive input weight has norm at most one, while the negative output weight costs at most $\Gamma_{97}$. Thus
$$
 \|C_{s,\delta}^{\rm fr}\|
       \le\Gamma_{97}(g_++e_{s-7/6})A_s .
 \tag{NIF.27}
$$
This finite symbolic bound suffices for the asserted uniform isomorphism. Printing the optional forward constants is a separate new scalar product; it is not included silently in the minimal output list below.

The coordinate qualification in RNI5 is consequently met for this explicitly frozen realization. It is not a proof that a previously unspecified family of selected-angle realizations existed. On smooth compatible data, B sections 2--3 already supply the same regular positive given-head graph over the full real interval, with its actual regular endpoint and complete independent source columns. The smooth graph consequence therefore uses this existing PC/IN realization, not a new hypothesis of a selected KAM family. Its bulk, outer and source domains and boundary conditions are unchanged. On rough spaces the present theorem asserts the bounded trace maps of (NIF.22)--26 and retains SE/FC's trace-extension qualification.

## NIF6. Relation to a frozen-H true-flow chart, and precise limits

If retaining the varying true waist labels is useful, WX also supplies whole-family two-sided bounds for $U_{X_{-,\delta}}$. One may define
$$
 \mathcal S_\delta^{H{\rm fr}}
   =U_{\mathcal H_*^{-1}}U_{X_{-,\delta}},\qquad
 \mathcal X_{s,\delta}^{H{\rm fr}}
   =\mathcal S_\delta^{H{\rm fr}}D_+\mathcal H_{\rm nat}^s,\qquad
 J_\delta=\mathcal S_\delta^{H{\rm fr}}\mathcal S_*^{-1}.
 \tag{NIF.28}
$$
Both $J_\delta$ and its inverse have complete uniform bounds from WX's two directions. Here only $\mathcal H_*$ is frozen. Its old bounds apply to the same fixed map, and WX's full-family bounds apply to the actual varying $X_{-,\delta}$.

For
$N_{i,\delta}^{H{\rm fr}}
 =\Lambda_{+,\delta}^{-1}T_{F,\delta}^{-1}
                 (\mathcal S_\delta^{H{\rm fr}})^{-1}$,
the cancellation is exact:
$$
 N_{i,\delta}^{H{\rm fr}}J_\delta=N_{i,\delta}^{\rm fr}.
 \tag{NIF.29}
$$
The natural reflected projector is
$\mathcal S_\delta^{H{\rm fr}}D_+Q_{\rm nat}D_+^{-1}
(\mathcal S_\delta^{H{\rm fr}})^{-1}$, whereas the ambient carrier projector is
$\mathcal S_\delta^{H{\rm fr}}P_{97}
(\mathcal S_\delta^{H{\rm fr}})^{-1}$.
They are not interchanged or identified with an orthogonal final-angle Fourier projector.

This optional construction is unnecessary for the fixed-space contract (NIF.17). It also does not require operator-norm continuity of varying composition or density pullbacks on a fixed Sobolev space. Smoothness of their defining diffeomorphisms alone would not justify that assertion. No operator-norm continuity of the true global Riccati diagonal $\mathcal M_\delta$ is assumed either.

The following limitations remain explicit.

- At $\delta_*$ the old MS ambient incoming normalization is recovered exactly, with the corrected physical-reflection restriction. At other parameters, the old selected KAM rotation, cohomological solution, principal first coefficients, Cayley gap and strong-return decomposition do not transfer without their own identities and fees.
- Even at $\delta_*$, restricting an already certified full-circle principal or Cayley inverse to the physically reflected input space requires a separate compatible domain-and-range statement. NIF does not supply that restriction theorem; the original full-circle successful bounds remain unchanged.
- The root-stable inverse and the coordinate isomorphisms do not prove a complete physical incoming inverse or the remaining finite Schur system.
- The FC completion already vanishes on the qualified R97 root family. This coordinate construction removes no further physical mean equation, radial head, actual low column, sign factor, independent second input or retained strong error.
- A common right coordinate change of a fully specified incoming/outgoing realization is exact. Cancellation in a physical return still requires the complete incoming inverse first.
- No parameter derivative of an unspecified selected chart, affine base point or physical boundary map is asserted. In particular this note supplies neither a family of selected KAM maps nor a true nonlinear background.

## NIF7. Exact saved inputs and the minimal new consumer

The scientific content comes from four current complete small objects. Paths in this table are relative to topics/visible-flex-exact-nearby.

| Role | Exact path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| TF science | notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json | 3766aea85aba59230be3813b4b7634d318316e49 | 18206 | a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720 |
| KL science | notes/correlated_terminal_Ai_leading_scalar_ci/run-43766439345-1/actual-scientific-conclusion.json | d24a1ecdd9b4397184a3ab932a503e8eb79d0c24 | 20537 | 1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee |
| WX execution | notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json | 5121a599896025d90e2861450756a256aaba659d | 43753 | e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12 |
| RNE science | notes/root_natural_negative_window_explicit_constants_ci/run-43792291190-1/actual-scientific-conclusion.json | 6f4ddebe683c0a22cb726d8ff7f8e7269146e46d | 57079 | 579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086 |

For WX, the mathematical object is its embedded actual_scientific_receipt. The other three are standalone science objects. Their successful gate counts are respectively 14, 16, 20 and 16, and every child return code is zero. Their source/manifest hashes and original runtime schemas must be checked as given; WX's lowercase python/numpy/scipy runtime is not replaced by another producer's schema.

For brevity in the field table, KL.copied denotes copied_complete_input_objects; TF.root denotes complete_new_root_coefficient_conclusion; TF.norm denotes complete_new_root_normalizer_conclusion; WX.common denotes actual_scientific_receipt.complete_selected_common_input_conclusion.

| Symbol | Exact complete field |
|---|---|
| $n_+$ | KL.copied.WT_complete_SP_waist_factors.density_radial_factor_upper.ball |
| $k_+$ | KL.copied.FA_complete_root_mean_value_q_bounds.complete_Kr_upper.ball |
| $\eta_-$ | TF.root.complete_original_eta_lower_used_verbatim.ball |
| $P_{\rm rev}$ | KL.copied.WX_complete_ungauged_leading_flow_conclusion.complete_reverse_radial_exponential_upper.ball |
| $E_{\rm sh}$ | KL.complete_new_root_short_conclusion.complete_inverse_root_to_cut_radial_factor_upper.ball |
| $K_\Lambda^-$ | KL.complete_new_leading_scalar_conclusion.complete_inverse_leading_scalar_upper.ball |
| $K_{F,0}^+,K_{F,-4/3}^+$ | TF.norm.complete_forward_L2_upper.ball, complete_forward_Hminus4_3_upper.ball |
| $K_{F,0}^-,K_{F,-4/3}^-$ | TF.norm.complete_inverse_L2_upper.ball, complete_inverse_Hminus4_3_upper.ball |
| $K_{\mathcal S,0},K_{\mathcal S,-4/3}$ | WX.common.complete_common_input_L2_upper.ball, complete_common_input_Hminus4_3_upper.ball |
| $K_{\mathcal S^{-1},0},K_{\mathcal S^{-1},-4/3}$ | WX.common.complete_common_input_inverse_L2_upper.ball, complete_common_input_inverse_Hminus4_3_upper.ball |
| $K_{{\rm nat},-7/6},K_{{\rm nat},-5/2}$ | RNE.complete_natural_inverse_conclusion.windows at keys -7/6 and -5/2, then complete_Snat_inverse_upper |

These are sixteen original scalar records. All complete records and the accepted scope objects must be copied before new combinations. The WX selected scope remains verbatim; the new output explains why a fixed one-time map supplies a uniform constant in a newly frozen realization. It must not rewrite that original scope as a claim of selected conjugacies for every parameter.

A minimal consumer may produce precisely the following new scalar conclusions:

1. The forward leading bound $K_\Lambda^+$ of (NIF.16), including its five original inputs and endpoint roles.
2. The two $A_s$ and two $B_s$ products of (NIF.19).
3. The two frozen-coordinate stable inverse bounds of (NIF.26), with the exact rational $\Gamma_{97}$ retained.
4. Exact coordinate/domain/mean statements and the original-order identities (NIF.17), (NIF.18), (NIF.22), (NIF.23).

This is seven new principal scalar outputs, plus the elementary intermediate factors needed to audit the first expression. The optional forward $C_s$ constants and varying-chart identification products are not part of this minimal target. If added later they must be named and counted as new scalar work.

No old exponential, flow, mean integral, root finder, native restore, R97 graph, strict e/g comparison, RNE finite inverse polynomial or old scientific producer may be called. No per-mode or radial array is needed. A false optional formatting or downstream condition cannot justify repeating completed scientific work. All copied literals, the new complete conclusions and their scope must be saved before display or publication formatting.

## NIF8. Primary identity audit

The following complete small texts were read for this statement. Source text is identity evidence, not authorization to execute an old producer.

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| Actual physical strip theorem W | a79a7ad7c147076b044389e98a15ab2f341d0d0c | 6138 | 1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3 |
| AC actual selected conjugacy | 30591d2714e45dcad6ae2de1774a9b7e333466de | 8974 | 6527fa46ddc21ed3d3e8c6ce4bb1f39f2db816d9fff5684e6daf4f30951c46f4 |
| WX whole-family true waist coordinates | ef394649b79b06e27d7d3a36bdf98a7fcd801039 | 20033 | c5157bbb14b300c1a418642e96917b49f0f90c1ebc3571a124a26b863adc9ae1 |
| WX original scalar source | 6c889bfa4e6bd0f64e1b161bce36eafdebb9c4c6 | 32330 | 63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424 |
| KL correlated leading scalar | cf3e435f21bbce03ad051a19676428504d490dcd | 13896 | dc48bdb46fde624f5e6f3820a7f37e326cb3b84274f34d46e1538f6166285b9a |
| MS exact common-input normalization | 10fdaddc0114e25ad349f1f411e80baf4f98fe26 | 19522 | 44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161 |
| N actual moving scalarization and reflection | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| O ordered moving parity operators | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |
| B full-real-family root and positive graph | e561b822673bbce15c1391ee851fb93d4143d43e | 15703 | f5f980a1fb085103f548d7bbdf6fe0124dda176276fa1b8bac6783b6b22a150c |
| SE natural stable port, original before the NIF9 domain clarification | eb7b1bb1ea1fdf713fcf172428f68ed20afafdb2 | 20047 | 2220174707046248cbdf9f9f8c47bc13bc233b0ab65f5ed598ddcbf964e93ad4 |
| RNI common-input inverse qualification | ce0a46c75360850479333534cf096fd61f412168 | 19405 | d771cf43faa0d5351851168f9f1567e21f8b7e0be27480b6bd67880a4eb69a81 |
| RNE explicit natural-window theorem | d6cb8f723584a5f893a01324033d059995d1ee79 | 17890 | 030e434ed31632c0c5330318251486d37424deba78f3fe35bf8b738960425120 |

The actual R97 result is already carried by the complete accepted RNE object and its copied original objects. No new root claim is derived from a prefix or a planned count. The present result pays only the explicitly frozen coordinate realization and the displayed same-window products.


## NIF9. The narrow SE8 domain correction and dependency boundary

The original SE blob eb7b1bb1ea1fdf713fcf172428f68ed20afafdb2, 20047 bytes, SHA256 2220174707046248cbdf9f9f8c47bc13bc233b0ab65f5ed598ddcbf964e93ad4, states in SE8 that the MS map
$N_i=\Lambda_+^{-1}T_F^{-1}\mathcal S^{-1}$ has
$\mathcal X_s=\mathcal S\mathcal H_H^s$ as its actual transported high space. With $\mathcal H_H^s$ retaining SE1's natural reflected meaning, that domain equality is not justified: the two phases of $\Lambda_+$ differ. Preserving positive and negative frequency sectors, or real Fourier conjugacy, does not prove preservation of the even-reflection space.

The corrected domain statement is the following.

> Let $\mathcal H_{\rm nat}^s$ retain the original reflected natural root domain and let $\mathcal H_{\rm car}^s=P_{97}H^s$ denote the full signed carrier. The ordered MS formula is first an ambient carrier map. Its natural-root restriction has domain
> $$
> \mathcal X_s=N_i^{-1}\mathcal H_{\rm nat}^s
>   =\mathcal S T_F\Lambda_+\mathcal H_{\rm nat}^s
>   =\mathcal S D_+\mathcal H_{\rm nat}^s.
> $$
> Here $D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_-$ is fixed and unitary. The last range equality uses the actual odd coefficient $F_*$, the reflection-preserving isomorphism $T_F$ and its commutation with $D_+$, as proved in NIF.10a and NIF.11a. The transported natural-reflection projector and the transported ambient Fourier high projector are distinct. The physical means and original low complement remain separate.

At the original selected member use its actual $\mathcal S$; the full-family frozen realization is exactly (NIF.7), (NIF.17). This correction does not enlarge $J$ or $S_{\rm nat}$ to an unproved opposite-reflection domain.

| Existing statement | Effect of the correction |
|---|---|
| MS ambient signed-carrier factorization, phase ratio, sign ordering and exact $T_F$ commutators | Unchanged; these are full signed-carrier statements. Their bounds remain valid after the properly typed restriction. |
| SE1--7, RNI root argument, actual R97 strict gate, and RNE natural-window inverse | Unchanged. They remain on the same original reflected natural root space, with the same complete error and actual saved constants. |
| SE8 natural weights, SE.21--23 and Fredholm consequence | Their weight order and theorem stay unchanged; the concrete domain sentence is replaced by the inverse-image definition above. |
| RNI5, FC4 and RNS2 formula for $C_s$ and its inverse | Each was explicitly conditional on an actual bounded isomorphism $N_i:\mathcal X_s\to\mathcal H_{\rm nat}^s$. The corrected inverse-image domain now supplies that type. No formula or factor is reordered. |
| FC finite completion and RNS graph/right-factor identities | Their abstract natural-root arguments are unchanged. On the admitted R97 family the completion is already zero. Any application to common input coordinates uses the corrected domain, with all independent rest ports retained. |
| BF/BT/RNS finite angular-head formulas using $P_{97}$ or its complement | They remain formulas on the original signed carrier. $Q_{\rm nat}$ is not substituted for that Fourier projector; its opposite-reflection complement is infinite dimensional and is not a finite head. |
| R97A and RNE's conditional selected-coordinate consequences | Their qualification clauses remain. NIF supplies a concrete frozen-domain realization, not an unproved varying selected KAM family. |
| Existing numerical receipts | No scalar, gap, error, finite bootstrap, norm, array or native is recalculated or changed. |

For a bounded physical realization that separately retains another reflection/phase direction, that direction retains its original port space. The present natural reflected statement neither manufactures nor deletes such a port. Complete incoming invertibility and the actual finite Schur problem remain independent.

This is a genuine domain correction to a shorthand in SE8. It is not a numerical repair and does not change the seven new scalar combinations specified in NIF7.
