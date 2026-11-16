# R133 supplement: polynomial bounds for two-sided reflected waist normalization

2026-11-16, phase_inverse.

**Proved analytic corollary of WBN.** A second, explicitly different target coordinate can use the same positive primitive pairing as the source coordinate. Both coordinate inverses then have polynomial bounds in the already qualified coefficients. The complete algebraic error admits an exact collected form whose sign commutator contains only $v_i$, rather than two separately estimated functions involving $w$.

This proof does not revise WBN, the old CN/NPK normalizer, or any successful scalar record. It declares a new target operator. Every numerical bound below is symbolic; no exponential, cohomology, old norm, actual ball, or scientific target is evaluated. The true physical error, input density intertwiner and transported finite complement remain in the full formula.

## WBP1. The same functions and the same qualified spaces

Use WBN's selected real coefficients, physical frequencies $4j$, normalized circle, primitive $I=\partial_x^{-1}(Id-\Pi)$, and reflections
$$
 b=a+\Omega,\qquad
 Z_0=i\Pi_+-i\Pi_-,\qquad Z_{\rm full}=\Pi+Z_0,
 \qquad K_b=-Z_0R_b .
$$
The complete nonmean source and target are
$$
 X_b^s=\operatorname{Fix}(K_b)\cap H^s_0,\qquad
 Y_a^s=\operatorname{Fix}(R_a)\cap H^s_0,\qquad
 Q_a=(Id-\Pi)\frac{Id+R_a}{2}.
 \tag{WBP.1}
$$
No cutoff is inserted into this definition.

The complete WPL identities and the original cohomological solution give
$$
 c_i=\nu+v_i,\qquad c_o=-R_b c_i,\qquad
 \Pi v_i=0,\qquad \mu=-2\nu,
$$
$$
 (U_{-\Omega}-Id)w=-(v_i+R_bv_i),\qquad
 \Pi w=0,\qquad R_aw=-w ,
$$
$$
 \alpha=v_i-w,\qquad
 R_b\alpha=-\alpha,\qquad
 \Pi\alpha=0 .
 \tag{WBP.2}
$$
All of these are the same actual functions as WBN. In particular $w$ is not recomputed. The original regularities $v_i\in H^3$, $w\in H^2$ suffice for the two windows used below.

For any real function $f$ with the needed multiplication regularity define
$$
 \mathcal T_f
   =\Pi_+M_f\Pi_++\Pi_-M_f\Pi_-,
 \qquad F_f=M_fI-\mathcal T_fI .
 \tag{WBP.3}
$$
These definitions are linear in the coefficient. The two sign blocks are kept together as one complete operator.

Retain WBN's source normalizer and define the new target normalizer by
$$
 \boxed{\quad
 \mathcal A=Id-\mathcal T_\alpha I,\qquad
 \mathcal B=Id+\mathcal T_w I .
 \quad}
 \tag{WBP.4}
$$
The target $\mathcal B$ is not $N_\perp$ from WBN and is not the original full-circle $N=Id+M_wI$. The exact difference from that full-circle expression is $F_w$ on nonmean input. It will be kept before any target projection.

## WBP2. Both coordinate inverses are genuine, real and compatible

For the target reflection, $R_aw=-w$ implies
$$
 R_a\mathcal T_wR_a=-\mathcal T_w,\qquad
 [\mathcal B,R_a]=[\mathcal B,Z_0]=0 .
 \tag{WBP.5}
$$
The corresponding source identities are
$[\mathcal A,R_b]=[\mathcal A,Z_0]=[\mathcal A,K_b]=0$.
Both maps are real, preserve the nonmean carrier, and have the same commutations for their inverses.

In the exact WIT/WBN energy space
$$
 \mathscr H=\dot H^{-1/2}_0,\qquad
 G=IZ_0=|\partial_x|^{-1},
$$
the operator $\mathcal T_wI$ is skew-adjoint with respect to the $G$ pairing:
$$
 G^{1/2}(\mathcal T_wI)G^{-1/2}
       =-G^{1/2}\mathcal T_wG^{1/2}Z_0.
 \tag{WBP.6}
$$
The right side is bounded and skew-adjoint in ordinary $L^2_0$, because $\mathcal T_w$ is self-adjoint and commutes with $Z_0$. Thus both $\mathcal B=Id+\mathcal T_wI$ and its $G$ adjoint $Id-\mathcal T_wI$ have real quadratic form $\|u\|_{\mathscr H}^2$. The closed-range and adjoint-kernel argument of WBN applies with the sign reversed:
$$
 \mathcal B_{\mathscr H}^{-1}\text{ exists onto }\mathscr H,\qquad
 \|\mathcal B_{\mathscr H}^{-1}\|\le1.
 \tag{WBP.7}
$$
This does not require $w$ to be small or to have a pointwise sign.

Let complete positive inputs satisfy
$$
 W_0\ge\|w\|_\infty,\qquad
 W_{1/3}\ge W_{1/3}(w),\qquad
 C_I=\frac{\sqrt{17}}4,
$$
$$
 A_0\ge\|\alpha\|_\infty,\qquad
 A_{1/3}\ge W_{1/3}(\alpha).
 \tag{WBP.8}
$$
Here the function norm is
$W_{1/3}(f)=\sum_j(1+4|j|)^{1/3}|\widehat f_j|$.

The exact same two-step construction as WBN, now for $Id+\mathcal T_wI$, proves
$$
 \boxed{\begin{aligned}
 \|\mathcal B^{\pm1}\|_{L^2_0\to L^2_0}
     &\le K_{B,0}:=1+\frac{W_0}{4},\\
 \|\mathcal B^{\pm1}\|_{H^{-4/3}_0\to H^{-4/3}_0}
     &\le K_{B,-}:=1+C_IW_{1/3}.
 \end{aligned}}
 \tag{WBP.9}
$$
For the negative inverse one may write explicitly
$$
 \mathcal B^{-1}f
       =f-\mathcal B_{\mathscr H}^{-1}\mathcal T_wIf .
$$
The second term is in $\mathscr H$, because
$\mathcal T_wI:H^{-4/3}_0\to\mathscr H$
has norm at most $C_IW_{1/3}$. An arbitrary negative-window input is not first assumed to belong to $\mathscr H$. Kernel bootstrap proves the same two-sided inverse in both windows.

The source bounds remain exactly
$$
 \|\mathcal A^{\pm1}\|_0\le K_{A,0}:=1+\frac{A_0}{4},
 \qquad
 \|\mathcal A^{\pm1}\|_{-4/3}\le K_{A,-}:=1+C_IA_{1/3}.
 \tag{WBP.10}
$$
The target inverse restricts to $Y_a^s$, and the source inverse restricts to $X_b^s$. These are two distinct spaces. No full-circle inverse of $T_i$ is being restricted to an unproved same-space map.

Optional full scalar extensions are
$\Pi+\mathcal AP$ and $\Pi+\mathcal BP$.
Their auxiliary mean coordinate is explicitly the identity. They are not the old CN inverse with one of its weighted means removed. In particular the old identity
$N=\mathcal B+F_w$ on nonmean input still includes the full output-mean part of $F_w$.

## WBP3. The uncollected complete identity

Put
$$
 T_i=Id+M_{c_i}I,\qquad
 T_\nu=Id+\nu I,\qquad N=Id+M_wI .
$$
WBN gives the exact identity
$$
 T_i\mathcal A-N T_\nu
     =-M_{c_i}IM_\alpha I-\nu M_wI^2+T_iF_\alpha .
$$
Since $N-\mathcal B=F_w$ on nonmean input, the same complete operator can be written as
$$
 \boxed{\quad
 \mathcal R_{\rm ss}:=T_i\mathcal A-\mathcal BT_\nu
   =-M_{c_i}IM_\alpha I-\nu M_wI^2
          +T_iF_\alpha+F_wT_\nu .
 \quad}
 \tag{WBP.11}
$$
No factor in (WBP.11) has been commuted. Both $F$ terms initially include their complete output means.

For each coefficient the exact sign decomposition is
$$
 F_f=\Pi M_fI+\frac12Z_0[M_fI,Z_{\rm full}]
       \quad\hbox{on nonmean input}.
 \tag{WBP.12}
$$
The first row in (WBP.12) is real and generally nonzero. However, in this one normalized primitive target,
$$
 Q_aT_i1=Q_a1=0,\qquad Q_a1=0.
$$
Therefore only after applying the original $Q_a$ one obtains
$$
 \begin{aligned}
 Q_a\mathcal R_{\rm ss}
  =Q_a\bigl[
     &-M_{c_i}IM_\alpha I-\nu M_wI^2\\
     &+\tfrac12T_iZ_0[M_\alpha I,Z_{\rm full}]\\
     &+\tfrac12Z_0[M_wI,Z_{\rm full}]T_\nu
                         \bigr].
 \end{aligned}
 \tag{WBP.13}
$$
The disappearance of these auxiliary constant output rows is an exact identity of this projected row. It is not a subtraction from a saved norm upper and is not a deletion from any independent mean or amplitude equation.

With
$$
 C_i^\infty\ge\|c_i\|_\infty,\qquad
 K_{i,0}^{\rm fwd}=1+\frac{C_i^\infty}{4},\qquad
 K_\nu=1+\frac{|\nu|}{4},\qquad
 a_I=\frac{17^{2/3}}{16},
 \tag{WBP.14}
$$
the complete MS bound for the full-sign commutator gives one positive candidate:
$$
 \boxed{\begin{aligned}
 \|Q_a\mathcal R_{\rm ss}:H^{-4/3}_0\to L^2\|
  &\le C_{\rm unc},\\
 C_{\rm unc}
  :=a_I\bigl(C_i^\infty A_{1/3}+|\nu|W_0\bigr)
    &+\frac{17}{16}
           \bigl(K_{i,0}^{\rm fwd}A_{1/3}
                         +K_\nu W_{1/3}\bigr).
 \end{aligned}}
 \tag{WBP.15}
$$
The factors $K_{i,0}^{\rm fwd}$ and $K_\nu$ are forward bounds on the indicated whole spaces. In particular $K_\nu$ uses the original physical minimum frequency four. The variable coordinate changes may produce modes below 97; no unproved high-input primitive improvement is used.

## WBP4. Exact collection leaves only the first coefficient's nonmean commutator

There is a more correlated identity before taking any norms. Linearity and the exact coefficient equality $\alpha+w=v_i$ give
$$
 \mathcal T_\alpha+\mathcal T_w=\mathcal T_{v_i},
 \qquad F_\alpha+F_w=F_{v_i}.
$$
Expanding the two products directly now yields
$$
 \boxed{\quad
 \mathcal R_{\rm ss}
     =F_{v_i}
       -M_{c_i}I\mathcal T_\alpha I
       -\nu\mathcal T_wI^2.
 \quad}
 \tag{WBP.16}
$$
For verification,
$$
 \begin{aligned}
 T_i\mathcal A
    &=Id+M_{c_i}I-\mathcal T_\alpha I
                         -M_{c_i}I\mathcal T_\alpha I,\\
 \mathcal BT_\nu
    &=Id+\nu I+\mathcal T_wI+\nu\mathcal T_wI^2,
 \end{aligned}
$$
and
$(M_{c_i}-\nu Id-\mathcal T_\alpha-\mathcal T_w)I
=(M_{v_i}-\mathcal T_{v_i})I=F_{v_i}$.
This proves equality with (WBP.11) as full output-valued operators, not merely after projection or up to a mean.

The full output-mean row of the common operator is, exactly,
$$
 \Pi\mathcal R_{\rm ss}
      =\Pi M_{v_i}I\mathcal A .
 \tag{WBP.17}
$$
Indeed $\mathcal A$ and $\mathcal BT_\nu$ have nonmean output, and
$\Pi T_i\mathcal A=\Pi M_{v_i}I\mathcal A$.
This row is retained if the full auxiliary equation is used.

In the actual primitive row, $Q_a$ kills the constant row of $F_{v_i}$ and leaves
$$
 \boxed{\quad
 Q_a\mathcal R_{\rm ss}
   =Q_a\left[
       \tfrac12 Z_0[M_{v_i}I,Z_{\rm full}]
       -M_{c_i}I\mathcal T_\alpha I
       -\nu\mathcal T_wI^2
        \right].
 \quad}
 \tag{WBP.18}
$$
Only the coefficient $v_i$ occurs in the remaining sign commutator. This is exact function-level collection. It does not estimate a difference of two previously bounded functions by subtracting their bounds.

Let $B_i\ge W_{1/3}(v_i)$. The same-sign multiplier has
$$
 \|\mathcal T_\alpha:H^{-1/3}\to H^{-1/3}\|
                         \le A_{1/3},\qquad
 \|\mathcal T_w:L^2\to L^2\|\le W_0 .
$$
The first follows from the complete Wiener multiplication bound and the two orthogonal sign blocks; the second is its complete $L^\infty$ estimate. Thus the two-primitive product and the compressed $I^2$ term have the same valid positive costs as before. The second full candidate is
$$
 \boxed{\begin{aligned}
 \|Q_a\mathcal R_{\rm ss}:H^{-4/3}_0\to L^2\|
     &\le C_{\rm col},\\
 C_{\rm col}
   :=a_I\bigl(C_i^\infty A_{1/3}+|\nu|W_0\bigr)
       &+\frac{17}{16}B_i .
 \end{aligned}}
 \tag{WBP.19}
$$
The commutator factor is not multiplied by $K_{i,0}^{\rm fwd}$ in this expression: (WBP.16), not a triangle estimate for (WBP.11), is being used.

Both (WBP.15) and (WBP.19) bound the very same complete projected operator. They may be retained as two whole candidates. A later directed consumer must save each full candidate before selecting a whole record. It must not splice favorable summands from unrelated decompositions into a new unproved bound.

## WBP5. The density mean rank and the true input map remain

Use the exact WPL physical row in its already declared units:
$$
 \mathcal B_\partial
       =\frac{\mathfrak W_\partial}{2\kappa}
       =Q_aT_i|_{X^{\rm fr}}+E_\partial^{\rm fr}.
 \tag{WBP.20}
$$
The whole physical strong error is
$$
 E_\partial^{\rm fr}
  =Q_aV_wT_i-(h_H-1)\otimes\rho_i
       +Q_a(Id+V_w)(Id-h_H\Pi)E_i^{\rm fr}.
 \tag{WBP.21}
$$
The exact second waist normalizer is in $V_w$; the first normalizer's zero endpoint value does not set $V_w$ to zero.

In particular the genuine density mean rank in (WBP.21) does not disappear in the cancellations above. RRF gives $\Pi h_H=1$ and $R_ah_H=h_H$, so
$$
 Q_a(h_H-1)=h_H-1 .
$$
Its output vector is mean-zero, not a constant. The cancellation of a constant row in (WBP.13) or (WBP.18) therefore cannot remove $(h_H-1)\otimes\rho_i$. All WRA state, PC/ST4, strict source, interface, root/finite and primitive-rank contributions inside $E_i^{\rm fr}$ remain in (WBP.21).

Suppose a complete bound $C_\partial$ for (WBP.21) on
$X_{-4/3}^{\rm fr}\to Y_a^0$ has been admitted. It remains a symbolic whole-input hypothesis here.

Retain WIT's exact density intertwiner $\mathcal W$:
$$
 K_W=1+\frac{C_\Delta}{2},\qquad
 \|\mathcal W^{\pm1}\|_{0},\
 \|\mathcal W^{\pm1}\|_{-4/3}\le K_W,
$$
$$
 \|\mathcal W^{-1}-Id:H^{-4/3}_0\to L^2_0\|
          \le C_{W-Id}:=K_W C_\Delta/2 .
 \tag{WBP.22}
$$
The original complete $C_\Delta$ includes its independent mean rank. It is not replaced by an outgoing subtotal or recomputed.

The exact new normalized physical row is
$$
 \widetilde{\mathcal B}_{\rm ss}
       =\mathcal B^{-1}\mathcal B_\partial
                                 \mathcal W^{-1}\mathcal A.
$$
It obeys
$$
 \boxed{\quad
 \widetilde{\mathcal B}_{\rm ss}
    =\Pi_a^+T_\nu+\widetilde E_{\rm ss},
 \quad}
$$
$$
 \begin{aligned}
 \widetilde E_{\rm ss}
   =\mathcal B^{-1}\bigl[
       &Q_a\mathcal R_{\rm ss}\\
       &+Q_aT_i(\mathcal W^{-1}-Id)\mathcal A\\
       &+E_\partial^{\rm fr}\mathcal W^{-1}\mathcal A
                                  \bigr].
 \end{aligned}
 \tag{WBP.23}
$$
Here $\mathcal B^{-1}$ commutes with $Q_a$ on the nonmean carrier, and
$Q_a\mathcal BT_\nu=\mathcal B\Pi_a^+T_\nu$.
Every factor stays on its original side. In particular the leading and the physical error were both right-transformed by $\mathcal W^{-1}\mathcal A$.

For $r\in\{\mathrm{unc},\mathrm{col}\}$, the corresponding whole positive bound is
$$
 \boxed{\quad
 C_{{\rm ss},r}
   :=K_{B,0}\left[
       C_r
       +K_{i,0}^{\rm fwd} C_{W-Id}K_{A,-}
       +C_\partial K_W K_{A,-}
            \right]
 \ \ge\|\widetilde E_{\rm ss}\|_{H^{-4/3}\to L^2}.
 \quad}
 \tag{WBP.24}
$$
The left inverse is paid on $L^2$, the source forward map on $H^{-4/3}$, and the whole physical input is in its actual source subspace. No NPK exponential or old complete N inverse is used in this coordinate choice.

The two bounds in (WBP.24) apply to one and the same $\widetilde E_{\rm ss}$ and may be compared as whole records. By contrast, WBN uses $N_\perp^{-1}$ as its left coordinate and therefore defines a different normalized operator. Its remainder bound and (WBP.24) are not automatically two bounds for the same remainder. One may choose either complete coordinate construction, with its own exact leading/error identity; a numerical minimum between different left-normalized operators is not asserted.

## WBP6. The retained finite complement and the later scalar graph problem

The new true input subspace is exactly the one in WBN:
$$
 \widetilde X_s
    =\{\xi\in X_b^s:
             \mathcal W^{-1}\mathcal A\xi\in X_s^{\rm fr}\}
    =\operatorname{ran}(\widetilde P_{97})\cap X_b^s,
$$
$$
 \widetilde P_{97}
    =\mathcal A^{-1}\widehat P_{97}\mathcal A,\qquad
 \widehat P_{97}
    =\mathcal W\mathcal S P_{97}\mathcal S^{-1}\mathcal W^{-1}.
 \tag{WBP.25}
$$
The actual complement is
$$
 Id-\widetilde P_{97}
   =\mathcal A^{-1}(\mathcal W\mathcal S)
       (Id-P_{97})(\mathcal W\mathcal S)^{-1}\mathcal A .
 \tag{WBP.26}
$$
Its full nonmean rank 192 and reflected rank 96 are retained, with their genuine columns, dual rows and weights. These are coordinate ranks, not a computed or solved finite system.

The new target map preserves the complete geometric target $Y_a^s$ and the two signs, but it need not preserve any ordinary Fourier cutoff. The same is true of the source normalizer. Every later ordinary high/low decomposition must keep the actual cross maps and finite rows generated by these choices.

On ordinary model source and target spaces, the leading $\Pi_a^+T_\nu$ is the WCS scalar model at the same $\nu=\nu_i$. Its inverse loses one derivative, and the right-preconditioned error belongs on the target. This corollary does not change that graph domain, prove a physical high test, or supply a finite-border inverse.

The normalization of the physical row still includes its original factor $2\kappa$. Independent mean/amplitude/outer/metric-parameter and radial/source equations must retain their actual row and column conversions. An auxiliary identity extension on a Fourier constant is not an identification with the physical even mean. No radially varying family of finite-rank sources is promoted to a single finite block.

## WBP7. Inputs, original evidence and scope of a later readout

All new coefficient inputs are complete positive majorants for the existing functions. For example, already admitted
$V_i\ge\|v_i\|_\infty$ and $B_i\ge W_{1/3}(v_i)$ permit
$$
 A_0:=V_i+W_0,\qquad
 A_{1/3}:=B_i+W_{1/3},\qquad
 C_i^\infty:=|\nu|+V_i .
$$
These choices do not recompute $v_i,w$ or their original norm budgets. They do not infer a signed field from a modulus or subtract one upper estimate from another.

A later authorized scalar readout could evaluate the new positive products in (WBP.9), (WBP.10), (WBP.15), (WBP.19) and (WBP.24) after every old input and complete physical factor has been admitted. It would save both whole candidates and the exact coordinate choice before comparison. The only inverse existence statements proved here are for the declared coordinate maps $\mathcal A$ and $\mathcal B$, not for the full waist matching problem.

| Primary and exact role | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WBN: cohomological parities, source inverse and complete uncollected ledger | 9507d853e18de92840abda11cb895a5989df1fc8 | 26506 | f6783549a2b29c5eebd4b31b6b604a89ba31345595cd3f03b86f6080927bde95 |
| WPL: complete coefficient reflection and actual physical waist row | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |
| WIT: true input intertwiner, complete sign error and transported finite complement | 68737e28209551cab5b45aa251869892bc51b380 | 21308 | 13c5972c82dd1af1ded73ccdfdd6b8ba69da3c3a84bb278aea602d3dd90ba437 |
| MS.25--27: the complete full-sign commutator | 10fdaddc0114e25ad349f1f411e80baf4f98fe26 | 19522 | 44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161 |
| WCS: same constant-mean scalar model and its graph-domain inverse | 4215c33aaec529176b1f8021904fd5f1e173e2fa | 12818 | 4998ef8208e3dc9e5474fe456bed53ebf4e7d987f7684d888f6705c9f1f55d0a |

The exact immutable manuscripts are identified so the operator identities can be checked independently. Their publication records do not trigger a mathematical execution. No native array, ball arithmetic, old successful target, new exponential or numerical comparison is called by this proof.
