# R133 supplement: exact genuine root b jets with common radial cancellation

2026-11-16, visible-exact / phase_inverse.

**Proved ordered identities and a finite lower-order jet recipe; no new numerical bound.** The complete genuine first b amplitude and its root derivative can be written as two nonradial multipliers plus explicit input-labelled rational-frequency terms. The common radial fourth derivative of K cancels before taking any modulus. The same common radial third eta derivative cancels from the nonradial multiplier, while the original frequency-dependent third derivative terms remain with their exact factors.

The full reference solution still contains its nonzero terminal coefficient beta-n. Both Airy columns, both physical frequency signs, the original projections and complete mean rows remain. This result changes neither a reference solution nor its boundary conditions.

## RBG1. The same full reference, radial comparison and primary identities

Use the same root convention and analytic piece as [RBD](R133-supplement-complete-first-Airy-b-derivative-from-genuine-fourth-root-jets.md). All r derivatives are outward ordinary derivatives unless D is explicitly written. All root fields and frequency coefficients use the same repaired reference and physical parameters.

| Primary | Complete Git blob | Bytes | SHA256 |
|---|---|---:|---|
| G, complete signed forcing and radial difference | 8fa0d675d454a19451f946ed8f8a8eead7145089 | 22688 | c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e |
| F, genuine normalized first forcing | a1baaae718a0787712e1b76b8ddfa60a391196a1 | 14116 | 052a0b23535c42523bc25734ed6366fd01a765c6a309b8ca88731b3ffdd707d8 |
| C, common radial Langer reference | 5fe6c61c14db1bcc560f5361eceb13e59cae1a8c | 15993 | 8d4119cbd42577fc1ab498350f4a8fd77b2923f7e207db4c4519f7a345225392 |
| RBD, complete neighborhood derivative | 6688dd6a2f1110b8c2efd7709c924baa1962f33b | 17757 | 5d7c045fbda7a2db441620f742f1481d941823e69599e1167135e8409cebc63e |
| RD, complete projected root products | 24b3523585bdfe9f1d96b57e3ca2e4f0727fd2d4 | 17725 | 34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f |

The needed original formulas are G.24–33, F.11–13 and F.16–22, C.1–8, and RBD.25–31. In particular [C](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md) defines the actual finite rational functions; no large-frequency expansion replaces them.

Write
$$
 D=\partial_r-d\partial_\phi,\quad p=d_\phi,\quad
 S=u^2+Kv^2,\quad M=\beta\langle S\rangle,\quad
 \eta=-\gamma\langle v\rangle .
 \tag{RBG.1}
$$
Set
$$
 E_m=\langle-\beta(1+3u^2+Kv^2)\rangle,\qquad
 B_m=\langle\beta(1-u^2-3Kv^2)\rangle,
$$
$$
 a_c=\eta_r/\eta+E_m,\qquad
 \mathfrak t=a_c+B_m=\eta_r/\eta-4M,\qquad
 \mathfrak q=a_c-B_m,\qquad
 V_m=a_cB_m-(B_m)_r.
 \tag{RBG.2}
$$
All these means are the complete old-angle means of the actual reference, including its nonradial products. The radial comparison does not set u to zero or replace v by its mean.

Let bar-T be the original common radial fold, kappa its ordinary r derivative, and bar-G the original leading radial amplitude with the same full M integral. G.27–29 prove
$$
 \frac{\bar G_r}{\bar G}=\frac{\mathfrak t-\ell_\kappa}{2},
 \qquad
 (\partial_r^2-\mathfrak t\partial_r+V_m)\bar G
             =\kappa^2V_{\rm rad}(\bar T)\bar G,
 \qquad \ell_\kappa=\kappa_r/\kappa .
 \tag{RBG.3}
$$
The actual and radial folds share the same root and first derivative:
$$
 T|_*=\bar T|_*=0,\quad DT|_*=\bar T_r|_*=\lambda,\quad
 \lambda^3=\eta_*^2k_1,\quad k_1=K_r|_*>0.
 \tag{RBG.4}
$$
The independent mean equations and nonradial operator couplings have not been replaced by the scalar radial comparison.

## RBG2. Two low-order radial coefficients and their nonradial differences

Use the RBD notation
$$
 e_j=\eta^{(j)}|_*/\eta_*,\quad
 c_2=k_2/(2k_1),\quad c_3=k_3/(6k_1),\quad
 L=e_1+c_2/2 .
 \tag{RBG.5}
$$
Only j at most two is needed for the nonradial construction below. Define
$$
 \begin{split}
 \bar t&=(2e_1+c_2)/5,\\
 \bar s&=\frac27\left[
 \frac{e_2+c_3}{2}+\frac{e_1(c_2-\bar t)}2
 +\frac{3\bar t^2}{8}-\frac{c_2\bar t}{4}-\frac{c_2^2}{8}\right].
 \end{split}
 \tag{RBG.6}
$$
These are the coefficients of the actual common radial fold
$$
 \bar T=\lambda\tau(1+\bar t\tau+\bar s\tau^2+\bar t_4\tau^3)+O(\tau^5),
 \qquad \tau=r-r_* .
$$
No value or bound for bar-t4 will be required.

For the actual nonradial fold let t and s retain their RBD meaning. Their exact differences are
$$
 \delta t=t-\bar t=\frac25p,\qquad
 \boxed{\displaystyle
 \delta s=s-\bar s
   =\frac{18\bar t}{35}p+\frac{18}{175}p^2
                       +\frac{p_r}{7}+\frac9{35}d p_\phi .}
 \tag{RBG.7}
$$
The last two terms can equivalently be written Dp/7 plus 2d pphi/5. This is an identity of actual root functions derived from the neighborhood coefficient equations, not a differentiated bound.

For later use set
$$
 \begin{split}
 t&=\bar t+\delta t,\qquad s=\bar s+\delta s,\\
 x_2&=(p_r+p^2+d p_\phi)/2,\\
 x_3&=\frac13\partial_\phi(d x_2+d_rp+d_{rr}/2),\\
 q_1&=e_1+(c_2-t)/2,\\
 q_2&=(e_2+c_3-s)/2+e_1(c_2-t)/2
                      +3t^2/8-c_2t/4-c_2^2/8.
 \end{split}
 \tag{RBG.8}
$$
These require only the listed ordinary radial and angular jets.

## RBG3. The third logarithmic difference without k4 or e3

The fourth fold coefficients may be eliminated symbolically before any bounds are taken. Define factored exact differences
$$
 \Sigma_2=\delta t(t+\bar t),\quad
 \Sigma_3=\delta t(t^2+t\bar t+\bar t^2),\quad
 \Sigma_{ts}=\delta t\,s+\bar t\,\delta s.
 \tag{RBG.9}
$$
They equal t squared minus bar-t squared, t cubed minus bar-t cubed, and ts minus bar-t bar-s, respectively. Define
$$
 \begin{split}
 \delta R_1&=-\delta t/2,\\
 \delta R_2&=-\delta s/2+3\Sigma_2/8-c_2\delta t/4,\\
 \delta R_{3,0}&=3\Sigma_{ts}/4-5\Sigma_3/16-c_2\delta s/4
          +3c_2\Sigma_2/16-c_3\delta t/4+c_2^2\delta t/16 .
 \end{split}
 \tag{RBG.10}
$$
Subtracting the actual coefficient recurrences RBD.8–10 for the two genuine folds gives
$$
 \boxed{\displaystyle
 \delta t_4=t_4-\bar t_4
 =\frac29\left[
 d s_\phi+d_rt_\phi+\frac{e_2\delta R_1}{2}
 +e_1\delta R_2+\delta R_{3,0}
 +q_2p+q_1x_2+x_3\right].}
 \tag{RBG.11}
$$
The terms e3/6 and c4/2 in the two recurrences are exactly the same and cancel. Thus the right side of (RBG.11), as displayed, does not contain either eta-rrr or K-rrrr. This is a new finite identity for a difference, not a subtraction of two saved upper bounds.

Let
$$
 \delta L_3=\delta t_4-\Sigma_{ts}+\Sigma_3/3
$$
and define
$$
 \begin{split}
 \Delta\Lambda_3={}&6\delta L_3
    -6d(s_\phi-t t_\phi)
    -3(d_r-dp)t_\phi+3d^2t_{\phi\phi},\\
 \delta_1={}&21p/10,\\
 \delta_2={}&4Lp/175+2p^2/175+29Dp/14,\\
 \boxed{\displaystyle
 \delta_3=\Delta\Lambda_3/4+2D^2p.}
 \end{split}
 \tag{RBG.12}
$$
These are precisely the first three D derivatives at the root of log(a0/bar-G). Indeed the common radial mean integral cancels from log(a0) minus log(bar-G), and RBD.13–17 supply the full variable-coefficient D derivatives. The term TTphi squared in a0 remains of order tau to the fifth and does not contribute to these three root jets.

The explicit second formula in (RBG.12) follows by subtracting the quadratic logarithmic coefficients. It also reproduces F.18. This second-order agreement is an audit of the actual derivative convention; it is not a replacement for the third-order neighborhood derivation.

Put
$$
 \bar A=\bar G_r|_*=(\bar t-c_2)/4-2M_*,
$$
$$
 \bar C=\bar G_{rr}|_*
   =\bar A^2+\frac{2\bar s-\bar t^2-2c_3+c_2^2}{4}-2M_r .
 \tag{RBG.13}
$$
Then define the complete leading differences
$$
 \begin{split}
 \Delta A&=\delta_1,\\
 \Delta C&=2\bar A\delta_1+\delta_1^2+\delta_2,\\
 \boxed{\displaystyle
 \Delta C_3
 =3\bar C\delta_1+3\bar A(\delta_1^2+\delta_2)
                     +\delta_1^3+3\delta_1\delta_2+\delta_3.}
 \end{split}
 \tag{RBG.14}
$$
They are Da0 minus bar-Gr, D2a0 minus bar-Grr, and D3a0 minus bar-Grrr at the root. In particular the common Mrr cancels from the last difference as well. Set
$$
 A_0=\bar A+\Delta A,\qquad C_0=\bar C+\Delta C .
 \tag{RBG.15}
$$
The quantities on the right sides of (RBG.6)–(RBG.15) use beta through order one for the mean, eta through order two, K through order three, and the displayed drift jets through radial order two. They do not require a bound for either individual fourth fold coefficient or either individual third leading derivative.

## RBG4. The complete local potential difference and its derivative

Use the original full scalar coefficient V0 from L.4 and put
$$
 Z=2\beta K P(v^2),\qquad
 W_{AC}=\ell^2-4\beta\eta vu_\phi,\qquad
 \ell=-2\beta uv,\qquad P=1-\Pi .
 \tag{RBG.16}
$$
G.26 is the full neighborhood identity
$$
 \Delta V:=V_0-V_m
   =(a_c+4B_m)p+(B_m-a_c)Z+4p^2-3pZ-Z^2-Dp+DZ-KW_{AC}.
 \tag{RBG.17}
$$
Differentiate this identity before restricting to the root. Define
$$
 \begin{split}
 Z_D&=2\beta k_1P(v^2),\\
 Z_{DD}&=(4\beta_rk_1+2\beta k_2)P(v^2)
       +4\beta k_1\{P(2vv_r)-2dvv_\phi\}.
 \end{split}
 \tag{RBG.18}
$$
These are DZ and D2Z at the root. In particular
$$
 D(P(v^2))=P(2vv_r)-2dvv_\phi
$$
there; D and P have not been interchanged. The old mean subtracted inside P and the additional mean that may arise from multiplication by d both remain.

The complete root difference and derivative are
$$
 \boxed{\displaystyle
 \Delta V_*=(a_c+4B_m)p+4p^2-Dp+Z_D,}
 \tag{RBG.19}
$$
$$
 \boxed{\displaystyle
 \begin{aligned}
 \Delta V_D:=(D\Delta V)_*
 ={}&(a_c'+4B_m')p+(a_c+4B_m+8p)Dp\\
   &+(B_m-a_c-3p)Z_D-D^2p+Z_{DD}-k_1W_{AC}.
 \end{aligned}}
 \tag{RBG.20}
$$
The primes on the radial quantities ac and Bm are ordinary r derivatives. The final term in (RBG.20) is the full differentiated AC coefficient. It is not removed by substituting K equal to zero before differentiation.

All radial means used here retain their full reference values. In particular
$$
 \begin{split}
 E_m'|_*&=-\beta_r(1+3\langle u^2\rangle)
                    -\beta\{6\langle uu_r\rangle+k_1\langle v^2\rangle\},\\
 B_m'|_*&=\beta_r(1-\langle u^2\rangle)
                    -\beta\{2\langle uu_r\rangle+3k_1\langle v^2\rangle\},\\
 a_c'|_*&=e_2-e_1^2+E_m',\\
 \mathfrak t'|_*&=e_2-e_1^2-4M_r .
 \end{split}
 \tag{RBG.21}
$$
The M and Mr are exactly those in RBD.19. No nonlocal mean is discarded.

The radial potential value itself is already determined by the complete second-order radial identity (RBG.3):
$$
 V_r:=V_{\rm rad}(0)
           =\lambda^{-2}(\bar C-\mathfrak t\bar A+V_m).
 \tag{RBG.22}
$$
This uses no derivative of Vrad and no fourth derivative of K.

## RBG5. Two complete nonradial amplitude multipliers

Define
$$
 \begin{split}
 \Delta R_*={}&\Delta C-\mathfrak t\,\Delta A-5pA_0+\Delta V_*,\\
 \Delta R_{D,*}={}&
 \Delta C_3-\mathfrak t\,\Delta C-5pC_0
 +(V_m-\mathfrak t')\Delta A\\
 &+(\Delta V_*-5Dp)A_0+\Delta V_D.
 \end{split}
 \tag{RBG.23}
$$
These are exact differences between the full numerators of the neighborhood forcing and its radial comparison. The second identity follows by subtracting RBD.28 from its true radial counterpart; the high common radial derivative has already cancelled in (RBG.14).

Set
$$
 {\cal E}_0=-\lambda^{-2}\Delta R_*.
 \tag{RBG.24}
$$
For comparison, F.20 gives the equivalent signed low-order expression
$$
 {\cal E}_0=-\lambda^{-2}\left[
 \left(\frac{12}{35}L-\frac32\mathfrak q\right)p
 -\frac{291}{140}p^2+\frac{15}{14}Dp
                         +2\beta k_1P(v^2)\right].
 \tag{RBG.25}
$$
This is the complete b1 plus Vr, including its old scalar mean. It is not a nonmean projection of that coefficient.

Define the second complete multiplier
$$
 \boxed{\displaystyle
 {\cal E}_1=
 \frac{2A_0-4t}{3}{\cal E}_0+\frac{37}{30}pV_r
                            -\frac{\Delta R_{D,*}}{3\lambda^2}.}
 \tag{RBG.26}
$$
Both E0 and E1 are independent of the Fourier input label and physical frequency sign. They depend on the full actual reference, not on a radialized replacement.

To prove (RBG.26) from neighborhood identities, let f_b be the original normalized first forcing, F.11–12. Since the off-diagonal first row of M0 inverse is of order tau cubed,
$$
 f_b|_*=b_1,\qquad Df_b|_*=DF_b|_*-A_0b_1 .
 \tag{RBG.27}
$$
The radial comparison has normalized forcing exactly minus Vrad(bar-T), by (RBG.3). RBD.29 therefore gives
$$
 Df_b|_*+\lambda V_{\rm rad}'(0)
   =-(4t+A_0){\cal E}_0
        +\frac{37}{10}pV_r-\lambda^{-2}\Delta R_{D,*}.
 \tag{RBG.28}
$$
Here
$$
 (4t+A_0)-(4\bar t+\bar A)
       =4(2p/5)+21p/10=37p/10
$$
is an exact root identity. The common fourth and third radial jets have cancelled symbolically in (RBG.28); neither side is formed by subtracting numerical upper bounds.

Finally the analytic transport gives
$$
 Db_1=A_0b_1+\tfrac13Df_b
$$
at the root. It is equivalent to RBD.30 because
A0 equals (T0-star minus 2t)/2. Adding the exact original genuine potential correction proves the formulas in the next section.

## RBG6. Every finite-frequency term, including its nonzero root derivative

Use the original rational parameter
$$
 z=j^{-2},\qquad n=4|j|,\qquad |j|\ge97 .
$$
For the actual degree M at most 96, C.1 defines
$$
 \begin{split}
 U(z)&=\sum_{\ell=1}^M\frac{2\ell^2}{1-\ell^2z}u_\ell u_{-\ell},\\
 W(z)&=\sum_{\ell=1}^M\frac{2\ell^2}{1-\ell^2z}v_\ell v_{-\ell},\\
 \alpha(z)&=\frac{\beta}{i}
       \sum_{\ell=1}^M\frac{\ell}{1-\ell^2z}u_\ell v_{-\ell},\\
 h(z)&=\alpha(z)/\eta,\qquad
 Q_1(z)=-2\beta U(z)+2\beta K W(z)
                                  +\frac{h_r(z)}{1+zh(z)}.
 \end{split}
 \tag{RBG.29}
$$
All products remain bilinear on complex parameter families. The complete original means enter eta and the scalar coefficients in (RBG.2). The denominators in (RBG.29), including the full 1+zh gap, have their original domains. A numerical bound must verify those same gaps.

At fixed z, the full G.32 identity is
$$
 V_j(\bar T)-V_{\rm rad}(\bar T)
   =\kappa^{-2}\left[
 \frac z2(Q_1)_r-\frac z2\mathfrak q Q_1-\frac{z^2}{4}Q_1^2
                       -16K(2\eta\alpha+z\alpha^2)\right].
 \tag{RBG.30}
$$
Set
$$
 U_*(z)=\left[\frac z2(Q_1)_r
                 -\frac z2\mathfrak qQ_1-\frac{z^2}{4}Q_1^2\right]_*,
 \qquad
 \Delta_0(z)=\lambda^{-2}U_*(z).
 \tag{RBG.31}
$$
It is exactly Vj(0) minus Vr, with every finite-frequency term retained.

Differentiate (RBG.30) before setting K equal to zero. Since kappa-r over kappa equals 2bar-t at the root, the complete derivative difference is
$$
 \boxed{\displaystyle
 \begin{aligned}
 \Delta_1(z)&:=\lambda\{V_j'(0)-V_{\rm rad}'(0)\}\\
 &=\lambda^{-2}\left[
 \frac z2(Q_1)_{rr}
 -\frac z2\{\mathfrak q_rQ_1+\mathfrak q(Q_1)_r\}
 -\frac{z^2}{2}Q_1(Q_1)_r\\
 &\hspace{23mm}
 -16k_1(2\eta_*\alpha+z\alpha^2)-4\bar t\,U_*(z)\right]_* .
 \end{aligned}}
 \tag{RBG.32}
$$
The primes on Vj and Vrad are derivatives in their common canonical radial coordinate. Equality of the first true derivatives DT and bar-Tr at the root makes (RBG.32) the same derivative difference needed for Vj at the actual nonradial T. No equality of the two folds away from the root is assumed.

The curvature term in (RBG.32) survives at z equal to zero:
$$
 \Delta_1(0)=-32k_1\eta_*\alpha(0)/\lambda^2 .
 \tag{RBG.33}
$$
Thus the factor z in the value difference (RBG.31) cannot be assigned to its entire derivative difference. In particular no nonzero finite-frequency or limiting diagonal has been silently dropped.

The original derivatives of Q1 can be evaluated without any K4 input. At the root,
$$
 \begin{split}
 Q_1={}&-2\beta U+\frac{h_r}{1+zh},\\
 (Q_1)_r={}&-2\beta_rU-2\beta U_r+2\beta k_1W
           +\frac{h_{rr}}{1+zh}-\frac{z h_r^2}{(1+zh)^2},\\
 (Q_1)_{rr}={}&-2\beta_{rr}U-4\beta_rU_r-2\beta U_{rr}
        +(4\beta_rk_1+2\beta k_2)W+4\beta k_1W_r\\
 &+\frac{h_{rrr}}{1+zh}
       -\frac{3zh_rh_{rr}}{(1+zh)^2}
       +\frac{2z^2h_r^3}{(1+zh)^3}.
 \end{split}
 \tag{RBG.34}
$$
The hrrr term remains. It uses the actual third derivative of alpha over eta, with the full quotient rule. It can contain eta-rrr and actual third reference derivatives, and occurs in (RBG.32) with the original factor z/2. The cancellation of the common radial third eta jet does not permit removing this genuine frequency-dependent term.

Combining (RBG.24)–(RBG.32) with F.12–13 and RBD.31 gives the complete root jets
$$
 \boxed{\displaystyle
 b_1^{V_j}\big|_*={\cal E}_0+\Delta_0(j^{-2}),}
$$
$$
 \boxed{\displaystyle
 Db_1^{V_j}\big|_*=
 {\cal E}_1+A_0\Delta_0(j^{-2})+\frac{\Delta_1(j^{-2})}{3}.}
 \tag{RBG.35}
$$
These formulas are exact for each original input label. No upper bound for free b1 or Vj has been subtracted to produce them.

## RBG7. Ordered operator use, actual inputs and scope

For the original high input projection PH, let the diagonal operators D-Delta0 and D-Delta1 act on the input frequency label j. Then (RBG.35) reads
$$
 {\mathsf B}^{V}
   =M_{{\cal E}_0}P_H+D_{\Delta_0}P_H,
$$
$$
 {\mathsf B}^{V}_r
   =M_{{\cal E}_1}P_H+M_{A_0}D_{\Delta_0}P_H
                                      +\tfrac13D_{\Delta_1}P_H .
 \tag{RBG.36}
$$
An external physical output projection stays external. The input-labelled diagonal in the mixed term is to the right of multiplication by A0; it has not been reassigned to an output frequency.

The nonradial functions in (RBG.24) and (RBG.26) require only K through order three, eta through order two, beta through order two, the full means, and drift/reference jets through the finite orders explicitly displayed. Their common K4, eta3 and Mrr contributions have cancelled before any modulus.

The frequency terms additionally require the complete derivatives of the finite functions U, W and alpha in (RBG.34). In particular alpha over eta has to be differentiated three times on the same original root piece. These are finite sums of the actual original Fourier coefficients and their ordinary derivatives, with every Leibniz and quotient term. They do not require a new ray or fold computation. They are new numerical obligations if not already saved; a first- or second-derivative enclosure is not promoted to a third derivative.

If complete same-domain suprema e0, e1, a0, d0 and d1 bound E0, E1, A0, Delta0 and Delta1, respectively, then
$$
 \|{\mathsf B}^{V}\|_{L^2\to L^2}\le e_0+d_0,\qquad
 \|{\mathsf B}^{V}_r\|_{L^2\to L^2}\le e_1+a_0d_0+d_1/3.
 \tag{RBG.37}
$$
The two physical input signs share the same b coefficients and the same absolute-frequency diagonals, so they introduce no additional sign sum. These ordinary L2 statements do not grant a negative Sobolev multiplier bound without the necessary angular derivatives.

In the complete RD stable trace, the actual root profile diagonals still contain
$$
 A_n=\operatorname{Ai}(0)+\beta_n\operatorname{Bi}(0),\qquad
 D_n=\operatorname{Ai}'(0)+\beta_n\operatorname{Bi}'(0).
$$
Their true nonzero beta-n and same terminal normalization are unchanged. All potential diagonals, explicit input powers, full J, original primitive, independent physical means, complete projection-generated mean term, low intermediate outputs, finite rows and second-reference ports remain in their original order.

A new public Actions consumer may evaluate these signed combinations from original immutable inputs or read already completed bounds. It must not rerun old reference, potential, fold, forcing or amplitude targets, nor obtain a cancellation by subtracting unrelated norm upper bounds. Every new rational-frequency domain and positive denominator must be recorded before a numerical use.

This supplement supplies no numerical coercivity pass, actual incoming inverse, finite Schur inverse, nonlinear state or final surface. It identifies an exact complete way to avoid the common fourth root derivative while retaining all remaining finite-frequency data.

## RBG8. Exact substitution in the complete RD root products

This section records the operator substitution explicitly so that the genuine potential correction is not charged twice. Let
$$
 a_*=A_0-b_{\rm op},\qquad
 {\cal H}={\mathsf B}^{V}_r-M_{b_{\rm op}}{\mathsf B}^{V}.
$$
Using (RBG.36), its complete ordered form is
$$
 \boxed{\displaystyle
 {\cal H}=M_{{\cal E}_1-b_{\rm op}{\cal E}_0}P_H
           +M_{a_*}D_{\Delta_0}P_H+\tfrac13D_{\Delta_1}P_H.}
 \tag{RBG.38}
$$
It is exactly the bracket
$$
 {\mathsf B}_r-M_{b_{\rm op}}{\mathsf B}
       +M_{a_*}D_{\mathcal B}+\lambda D_{\mathcal B'}
$$
in RD.19, because
$$
 D_{\mathcal B}=D_{V(0)},\qquad
 D_{\mathcal B'}=\tfrac13D_{V'(0)},\qquad
 {\mathsf B}^{V}={\mathsf B}+D_{\mathcal B}.
$$
No separate second copy of the B correction or its derivative is added after this substitution.

The complete RD.17–19 products can therefore be written
$$
 \begin{split}
 E_2={}&P{\mathsf B}^{V}D_DN^{-4/3},\\
 R_0={}&PM_{a_*}D_A+P{\mathsf A}_rD_AN^{-1}
       +P{\cal H}D_DN^{-4/3}\\
 &-\lambda P{\mathsf B}^{V}D_VD_AN^{-2}
       +PM_{b_{\rm op}}\Pi{\mathsf B}^{V}D_DN^{-4/3}.
 \end{split}
 \tag{RBG.39}
$$
The input diagonals DA, DD and DV are exactly RD's true reference values, including its nonzero beta-n. The last positive term is the complete projection-generated mean rank. The genuine correction does not change the complete Da1 operator in the second term.

If BV and HV are complete ordinary L2 bounds for the two unprojected operators $\mathsf B^V$ and $\mathcal H$, then, with the original RD constants and N-star equal to 388,
$$
 \begin{split}
 e_{\rm amp}&=B_VD_*N_*^{-4/3},\qquad e_2\le e_{\rm amp},\\
 r_0&\le a^\sharp A_*+A_{1r}A_*N_*^{-1}
      +H_VD_*N_*^{-4/3}
      +\lambda_+B_VV_*A_*N_*^{-2}
      +b_{\rm op}^\sharp e_{\rm amp}.
 \end{split}
 \tag{RBG.40}
$$
The final mean term uses the complete unprojected correction, not a potentially smaller post-projection norm. For instance
$$
 B_V\le e_0+d_0,\qquad
 H_V\le\|{\cal E}_1-b_{\rm op}{\cal E}_0\|_\infty
                                      +a^\sharp d_0+d_1/3
$$
follows directly from (RBG.36) and (RBG.38). A further triangle bound for the displayed correlated multiplier is allowed but is not required by the identity.

The source and target spaces, original J and L, every low intermediate output and all independent supplied means remain those of RD. These new expressions can enter its same sufficient stable-trace gate only after their numerical bounds and common domains have actually been paid.
