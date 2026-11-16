# R133 supplement: the complete first Airy b derivative from genuine fourth root jets

2026-11-16, visible-exact / phase_inverse.

**Proved local analytic identities and a complete finite jet recipe; numerical bounds remain unpaid.** The derivative of the first free Airy b amplitude is obtained by differentiating its actual neighborhood forcing before restricting to the root. A fourth coefficient of the genuine fold supplies the missing third leading derivative. The construction uses finitely many actual background jets and retains the complete radial mean. It does not differentiate a root-only identity as though it held in a neighborhood.

The derivatives below use the original outward coordinate r. They hold on one original analytic root piece of the repaired family, with the original physical parameter fixed. Any uniform claim over a physical-parameter box or the selected delta family requires all input jets and positive gaps on that same box. The field eta below is the original coefficient eta = -gamma times the complete mean of v; it is not a newly varied metric parameter.

## RBD1. Complete primary identities and the common root piece

Use the following original proofs.

| Primary | Complete Git blob | Bytes | SHA256 |
|---|---|---:|---|
| L, the actual first Airy forcing | 2451ca1c639f04dd69de5c01ff25e59c65a6abb3 | 15780 | a798e93d73aa64115cb43313985054e0d682a41fd1393f4efea4704301699e3a |
| G, genuine fold identities | 8fa0d675d454a19451f946ed8f8a8eead7145089 | 22688 | c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e |
| I, the actual analytic forced transport | ddc62b4539d640a950c2005505e08695f80910e7 | 14772 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| RBJ, the leading second jet and first b value | ad1ac7c2ee965ddafca1bb4822fb3a03062b3c37 | 11617 | a19878f7e91cf1a9b7a62e935afa866e6e792cf5c48386f702335e7cde9dc0d8 |

The corresponding statements are L.4–6 and L.22, G.2, I.19–21, and RBJ.1–24. See [the first forcing](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md), [the original primitive and transport](R133-supplement-original-primitive-on-actual-Airy-amplitudes-and-exact-mean.md), and [the published second root jet](R133-supplement-exact-leading-second-root-jet-and-first-Airy-b-value.md).

Let
$$
 D=\partial_r-d\partial_\phi,\qquad
 \tau=r-r_*,\qquad k_j=\partial_r^jK\big|_*,
 \qquad \lambda^3=\eta_*^2k_1,\quad \eta_*>0,\quad k_1>0.
 \tag{RBD.1}
$$
All root values in one formula refer to the same repaired reference, same root and same analytic piece. No equation of motion for an unknown nonlinear solution is imposed on that reference. The genuine fold satisfies throughout this neighborhood
$$
 DT=QX_\phi,\quad DX=-QT T_\phi,\quad
 \eta^2K=Q^2T,\quad
 \mu=Q^2(X_\phi^2+TT_\phi^2),\quad
 T\big|_*=0,\quad X\big|_*=\phi.
 \tag{RBD.2}
$$
In particular lambda is the angle-independent root constant. It is kept fixed when forming Taylor coefficients in tau.

The complete mean and drift are
$$
 S=u^2+Kv^2,\qquad M=\beta\langle S\rangle,\qquad
 d=-\beta I S,\qquad p=d_\phi .
 \tag{RBD.3}
$$
Here I and the mean are the original normalized old-circle operators. The primitive keeps all nonzero Fourier inputs and its zero mean convention.

## RBD2. One more genuine fold coefficient

Use ordinary derivative ratios and ordinary Taylor coefficients
$$
 e_j=\frac{\partial_r^j\eta|_*}{\eta_*}\quad(j=1,2,3),
 \qquad
 c_2=\frac{k_2}{2k_1},\quad
 c_3=\frac{k_3}{6k_1},\quad
 c_4=\frac{k_4}{24k_1}.
 \tag{RBD.4}
$$
Thus e2 and e3 are not derivatives of log eta. Write the actual expansions
$$
 \begin{split}
 T&=\lambda\tau(1+t\tau+s\tau^2+t_4\tau^3)+O(\tau^5),\\
 X_\phi&=1+p\tau+x_2\tau^2+x_3\tau^3+O(\tau^4),\\
 Q&=\lambda(1+q_1\tau+q_2\tau^2+q_3\tau^3)+O(\tau^4).
 \end{split}
 \tag{RBD.5}
$$
RBJ already gives
$$
 \begin{split}
 x_2&=\frac{d_{r\phi}+p^2+d\,p_\phi}{2},\\
 t&=\frac{2e_1+c_2+2p}{5},\qquad t_\phi=\frac25p_\phi,\\
 q_1&=e_1+(c_2-t)/2,\\
 q_2&=(e_2+c_3-s)/2+e_1(c_2-t)/2
                  +3t^2/8-c_2t/4-c_2^2/8,\\
 s&=\frac27\left[
 d t_\phi+\frac{e_2+c_3}{2}+\frac{e_1(c_2-t)}2
 +\frac{3t^2}{8}-\frac{c_2t}{4}-\frac{c_2^2}{8}
 +q_1p+x_2\right].
 \end{split}
 \tag{RBD.6}
$$
All angular derivatives of these root functions are their actual angular derivatives. They may be computed from these identities because the identities hold on the entire root circle.

Since Tphi is of order tau squared, DX is of order tau cubed. The first three coefficients of Xphi therefore satisfy the same coefficient equations as Xr = d Xphi. In particular
$$
 \boxed{\displaystyle
 x_3=\frac13\partial_\phi
                  \left(d x_2+d_r p+\frac{d_{rr}}2\right).}
 \tag{RBD.7}
$$
The order tau cubed term in DX first affects the next coefficient of Xphi, not x3. The dr and drr in (RBD.7) are genuine ordinary radial derivatives; they are not derivatives of p as a root-only function.

For a compact explicit formula define
$$
 \begin{split}
 R_1&=(c_2-t)/2,\\
 R_2&=(c_3-s)/2+3t^2/8-c_2t/4-c_2^2/8,\\
 R_{3,0}&=\frac{c_4}{2}+\frac{3ts}{4}-\frac{5t^3}{16}
   -\frac{c_2s}{4}+\frac{3c_2t^2}{16}
   -\frac{c_3t}{4}+\frac{c_2^2t}{16}
   -\frac{c_2c_3}{4}+\frac{c_2^3}{16}.
 \end{split}
 \tag{RBD.8}
$$
The exact positive branch of the third identity in (RBD.2) is
$$
 \frac Q\lambda
 =\frac{\eta}{\eta_*}
  \left(\frac{1+c_2\tau+c_3\tau^2+c_4\tau^3+O(\tau^4)}
              {1+t\tau+s\tau^2+t_4\tau^3+O(\tau^4)}\right)^{1/2}.
$$
Multiplying its Taylor coefficients gives
$$
 q_3=\frac{e_3}{6}+\frac{e_2R_1}{2}+e_1R_2+R_{3,0}-\frac{t_4}{2}.
 \tag{RBD.9}
$$
The coefficient of tau cubed in DT = Q Xphi is
$$
 4t_4-ds_\phi-d_rt_\phi=q_3+q_2p+q_1x_2+x_3.
$$
Consequently the fourth fold coefficient is the following finite expression:
$$
 \boxed{\displaystyle
 t_4=\frac29\left[
 ds_\phi+d_rt_\phi+\frac{e_3}{6}+\frac{e_2R_1}{2}
 +e_1R_2+R_{3,0}+q_2p+q_1x_2+x_3\right].}
 \tag{RBD.10}
$$
This is a coefficient of the genuine fold defined by (RBD.2). No ray solve, new coordinate choice or approximate local model has been introduced.

## RBD3. The complete third leading derivative

The original leading amplitudes satisfy
$$
 a_0=G(X_\phi^2-TT_\phi^2),\qquad
 b_{0,\epsilon}=-2i\epsilon G X_\phi T_\phi,
$$
$$
 \log G=\mathrm{constant}+\frac14\log(T/K)
                         -2\int_{r_*}^r M(q)\,dq,\qquad G|_*=1.
 \tag{RBD.11}
$$
The quotient T/K is its analytic nonzero extension on the original branch. Its root logarithm is angle independent.

Set
$$
 \begin{split}
 L_1&=t-c_2,\\
 L_2&=s-t^2/2-c_3+c_2^2/2,\\
 L_3&=t_4-ts+t^3/3-c_4+c_2c_3-c_2^3/3.
 \end{split}
 \tag{RBD.12}
$$
These are the first three actual coefficients of log(T/K). Applying the full variable-coefficient operator D three times to its neighborhood expansion gives
$$
 \begin{split}
 \Lambda_1&=L_1,\\
 \Lambda_2&=2L_2-2d(L_1)_\phi,\\
 \boxed{\displaystyle
 \Lambda_3
 =6L_3-6d(L_2)_\phi
       -3(d_r-dp)(L_1)_\phi+3d^2(L_1)_{\phi\phi}.}
 \end{split}
 \tag{RBD.13}
$$
For example the third identity follows from the actual differential operator
$$
 D^2f=f_{rr}-2df_{r\phi}+d^2f_{\phi\phi}
                         -(d_r-dp)f_\phi.
 \tag{RBD.14}
$$
When the root value of f is angle independent, the terms in D3f containing only angular derivatives of that root value vanish, leaving
frrr minus 3d times frrphi plus 3d squared times frphiphi minus 3Dd times frphi. Substitution of (RBD.12) gives (RBD.13).

The exact commutator [D,partial-phi] = p partial-phi and the second identity in (RBD.2) imply
$$
 D\log X_\phi
   =p-\frac{\partial_\phi(QTT_\phi)}{X_\phi}
   =p+O(\tau^3).
 \tag{RBD.15}
$$
Also TTphi squared is of order tau to the fifth. Therefore, through the third D derivative at the root, log a0 has exactly the jets of log G plus twice log Xphi. Define
$$
 \begin{split}
 A_0&=\Lambda_1/4+2p-2M_*,\\
 H_2&=\Lambda_2/4+2Dp-2M_r,\\
 H_3&=\Lambda_3/4+2D^2p-2M_{rr}.
 \end{split}
 \tag{RBD.16}
$$
Then the complete leading derivatives are
$$
 \boxed{\displaystyle
 Da_0|_*=A_0,\qquad
 D^2a_0|_*=C_0=A_0^2+H_2,\qquad
 D^3a_0|_*=C_3=A_0^3+3A_0H_2+H_3.}
 \tag{RBD.17}
$$
This reproduces RBJ for the first two derivatives. For implementation the last drift term can be written entirely in ordinary jets:
$$
 Dp=p_r-dp_\phi,\qquad
 D^2p=p_{rr}-2dp_{r\phi}+d^2p_{\phi\phi}
                         -(d_r-dp)p_\phi.
 \tag{RBD.18}
$$
No radial derivative of the root-only formulas for A0 or C0 is used.

## RBD4. Full means and differentiated local coefficients

Ordinary radial differentiation commutes with the fixed old-circle normalized mean. At the root, the full mean jets in (RBD.16) are
$$
 \begin{split}
 M_*={}&\beta\langle u^2\rangle,\\
 M_r={}&\beta_r\langle u^2\rangle
       +\beta\{2\langle u u_r\rangle+k_1\langle v^2\rangle\},\\
 M_{rr}={}&\beta_{rr}\langle u^2\rangle
       +2\beta_r\{2\langle u u_r\rangle+k_1\langle v^2\rangle\}\\
 &+\beta\{2\langle u_r^2+u u_{rr}\rangle
                     +k_2\langle v^2\rangle+4k_1\langle v v_r\rangle\}.
 \end{split}
 \tag{RBD.19}
$$
The k1 and k2 terms remain even though K vanishes at the root. These are complete products and means of the reference, not means removed by a high projection.

To avoid ambiguity with Airy amplitudes, write
$$
 b_{\rm op}=\beta(1-u^2-3Kv^2),\quad
 e=-\beta(1+3u^2+Kv^2),\quad
 \ell=-2\beta uv,
$$
$$
 t_Q=\eta_r/\eta+p+e,\quad
 T_0=\eta_r/\eta-4M+5p,\quad
 V_0=t_Qb_{\rm op}-Db_{\rm op}
                         -K(\ell^2-4\beta\eta vu_\phi).
 \tag{RBD.20}
$$
These are the full neighborhood definitions from L.4, with no root substitution made before differentiation.

For ordinary-to-D conversion put
$$
 U_D=u_r-du_\phi,\quad V_D=v_r-dv_\phi,
$$
$$
 U_{DD}=u_{rr}-2du_{r\phi}+d^2u_{\phi\phi}
                                 -(d_r-dp)u_\phi.
 \tag{RBD.21}
$$
The actual root coefficient derivatives are
$$
 \begin{split}
 b_*={}&\beta(1-u^2),\\
 b_D:=(Db_{\rm op})_*={}&\beta_r(1-u^2)-2\beta uU_D-3\beta k_1v^2,\\
 b_{DD}:=(D^2b_{\rm op})_*={}&
 \beta_{rr}(1-u^2)-4\beta_r uU_D
                -2\beta(U_D^2+uU_{DD})\\
 &-6\beta_rk_1v^2-3\beta k_2v^2-12\beta k_1vV_D .
 \end{split}
 \tag{RBD.22}
$$
Similarly,
$$
 \begin{split}
 t_{Q,*}&=e_1+p-\beta(1+3u^2),\\
 (Dt_Q)_*&=e_2-e_1^2+Dp-\beta_r(1+3u^2)
                               -6\beta uU_D-\beta k_1v^2,\\
 T_*:=T_{0,*}&=e_1-4M_*+5p,\\
 T_D:=(DT_0)_*&=e_2-e_1^2-4M_r+5Dp.
 \end{split}
 \tag{RBD.23}
$$
Define the complete two local potential jets
$$
 \boxed{\displaystyle
 \begin{aligned}
 {\cal V}_0&=t_{Q,*}b_*-b_D,\\
 {\cal V}_1&=(Dt_Q)_*b_*+t_{Q,*}b_D-b_{DD}
                            -k_1(\ell^2-4\beta\eta_*vu_\phi).
 \end{aligned}}
 \tag{RBD.24}
$$
They are V0 and DV0 at the root, respectively. In particular the last line retains the derivative of the factor K in the original AC contribution. It cannot be recovered by differentiating only the root value of V0.

## RBD5. Differentiate the actual forcing, then restrict

G.2 gives the neighborhood identity
$$
 H^{-1}H_D=-i\epsilon Q
                   \begin{pmatrix}0&T\\1&0\end{pmatrix}.
$$
Thus the first component of L.5–6, throughout the common neighborhood, is
$$
 \boxed{\displaystyle
 F_b=-\mu^{-1}\left[
 D^2a_0+\eta^2K(a_0)_{\phi\phi}-T_0Da_0+V_0a_0
                         +i\epsilon\vartheta QT b_{0,\epsilon}\right].}
 \tag{RBD.25}
$$
The coefficient vartheta is exactly the full L.4 coefficient, including its one-gain radial contribution and original means. It has not been deleted from this neighborhood formula.

Three exact root facts now simplify its first D derivative.

First, a0 equals one on the entire root circle, so its angular derivatives there vanish. Differentiating the angular second-order term before restricting therefore gives
$$
 D\{\eta^2K(a_0)_{\phi\phi}\}\big|_*
                =\eta_*^2 k_1(a_0)_{\phi\phi}\big|_*=0.
 \tag{RBD.26}
$$
Second, b0 is of order tau squared and T of order tau, so the entire last term of (RBD.25) is of order tau cubed. Its value and first D derivative at the root vanish. This component-specific fact does not remove vartheta from the second forcing component or any original operator remainder.

Third, the actual mu in (RBD.2) satisfies
$$
 \frac{D\mu}{\mu}\Big|_*
       =2q_1+2p=4t,\qquad \mu_*=\lambda^2.
 \tag{RBD.27}
$$
This derivative comes from the full G.2 identity, not from differentiating the root constant lambda squared.

Set
$$
 R_*:=C_0-T_*A_0+{\cal V}_0,\qquad
 R_{D,*}:=C_3-T_*C_0+({\cal V}_0-T_D)A_0+{\cal V}_1.
 \tag{RBD.28}
$$
The neighborhood differentiation of (RBD.25), using (RBD.26)–(RBD.27), gives
$$
 \boxed{\displaystyle
 b_1\big|_*=-\lambda^{-2}R_*,
 \qquad DF_b\big|_*=-4t\,b_1\big|_*-\lambda^{-2}R_{D,*}.}
 \tag{RBD.29}
$$
The analytic first transport equation I.19 has the genuine root derivative
$$
 3(b_1)_T+l_*b_1=(F_b)_T,\qquad
 D|_*=\lambda\partial_T,\qquad
 \lambda l_*=2t-T_* .
$$
Its common normalization gives (a1)X at the root equal to zero. Consequently
$$
 \boxed{\displaystyle
 Db_1\big|_*=
 \frac{(T_*-6t)b_1\big|_*-\lambda^{-2}R_{D,*}}{3}.}
 \tag{RBD.30}
$$
Equations (RBD.4)–(RBD.24), followed by (RBD.28)–(RBD.30), are a finite complete root jet formula. Every radial differentiation was performed on an actual neighborhood identity.

For the original genuine potential correction, RBJ.25–26 remain in their original order:
$$
 b_1^{V_n}\big|_*=b_1+V_n(0),\qquad
 Db_1^{V_n}\big|_*=Db_1+\lambda V_n'(0)/3+V_n(0)A_0.
 \tag{RBD.31}
$$
These are input-labelled potential diagonals. They are not commuted through multiplication, projection or the complete old inverse.

## RBD6. Minimal actual inputs and a complete positive budget

The algebra above needs the following true inputs on the same root piece.

| Input | Required ordinary radial and angular information |
|---|---|
| Intrinsic K | Root zero, k1 positive, k2, k3, and the new fourth derivative k4 |
| eta field | Positive eta-star and its first, second and third ordinary radial derivatives |
| Intrinsic beta | Orders zero, one and two in r |
| Repaired u and v | Full values and radial derivatives through order two; the angular derivatives occurring in (RBD.19)–(RBD.24) |
| Drift d | Radial derivatives through order two and the angular derivatives in x3, sphi, D2p; maximal angular order three |
| Complete radial mean | The full products and ordinary derivatives in (RBD.19), without a nonmean projection |

One direct rectangular input inventory is dr-jets of d through order two and phi-jets through order three, plus dr-jets of u,v through order two and phi-jets through order two. This is sufficient and may be reduced entry by entry using the displayed formulas. The independent mean needed for eta through radial order three is retained separately:
$$
 \eta_{rrr}
 =-\gamma_{rrr}m-3\gamma_{rr}m_r
                  -3\gamma_rm_{rr}-\gamma m_{rrr},\qquad m=\langle v\rangle .
 \tag{RBD.32}
$$
In the original root piece the repaired polynomial offsets are constant in r. This permits their positive radial derivatives to vanish inside that piece; it does not permit removal of the true rotational background or of radial derivative jumps between pieces. The root must remain inside one verified analytic germ. No seam-crossing derivative is granted by this lemma.

The only newly increased intrinsic order is k4. A saved real third derivative bound does not itself give k4. It must be obtained from a separately justified actual metric derivative identity, an already saved fourth derivative, or a new Cauchy bound on a verified complex root disk. For example, if the complete same-parameter analytic K is already bounded by MK on a complex disk of radius R centered at the true root, then
$$
 |k_4|\le 4! M_K/R^4
 \tag{RBD.33}
$$
is an eligible new scalar bound. A disk centered at a different point must use its verified remaining radius to the true root. No real interval or unrelated potential disk is silently used as that analytic K disk.

For any same-domain complete upper bounds denoted by a superscript sharp, and a true positive lambda lower bound, define
$$
 \begin{split}
 B_b&=\lambda_-^{-2}
        (C_0^\sharp+T_*^\sharp A_0^\sharp+{\cal V}_0^\sharp),\\
 B_R&=C_3^\sharp+T_*^\sharp C_0^\sharp
        +({\cal V}_0^\sharp+T_D^\sharp)A_0^\sharp+{\cal V}_1^\sharp,\\
 B_{DF}&=4t^\sharp B_b+\lambda_-^{-2}B_R,\\
 \boxed{\displaystyle
 B_{Db}=\frac{(T_*^\sharp+6t^\sharp)B_b+\lambda_-^{-2}B_R}{3}.}
 \end{split}
 \tag{RBD.34}
$$
These bound the complete b1, neighborhood forcing derivative and Db1. The quantities preceding (RBD.34) are bounded by finite absolute-coefficient product rules applied to the exact formulas, with true lower endpoints for all denominators. Signed cancellations may be retained before taking a modulus; independently rounded upper bounds are never subtracted.

The common real b1 and Db1 are independent of the physical input sign, by RBJ.20–21. Their complete ordinary circle suprema therefore pay the whole L2 multiplication operators on the high input projection without an extra sign sum. This does not give a negative Sobolev multiplier bound without the corresponding angular derivatives. The original physical output projection, low intermediate outputs, full mean-rank source, both physical mean coordinates and all input potential diagonals remain.

A future public Actions consumer may read already completed exact inputs and evaluate only these new coefficient combinations and any explicitly new required derivative gate. It must not rerun an old fold, ray, Airy amplitude, completed forcing or potential target. All old scientific successes remain frozen.

This result pays the analytic formula for the remaining root derivative. It asserts no new numerical multiplier bound, stable-trace coercivity pass, incoming inverse, finite Schur inverse, nonlinear solution or final surface.
