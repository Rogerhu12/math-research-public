# R133 supplement: exact leading root derivative and a complete stable-trace gate

2026-11-15, newton_source.

**Proved root identities and a conditional whole-operator coercivity criterion. No new numerical evaluation.** This computes the actual leading amplitude's first radial derivative from the moving fold and the original transport. It then retains every term in the stable trace of the normalized genuine terminal-Ai column. The conditional criterion concerns the original cutoff 97; it does not infer injectivity from a positive leading diagonal alone.

All derivatives below have the original outward physical orientation $r$. No derivative of a saved error ball is taken. The supplied head, physical means, low outputs, ordinary sources, jumps, second reference and actual exterior boundary conditions keep their original roles.

## RD1. Same root, reflection spaces and normalization

Use the actual repaired real family $|\delta|\le10^{-8}$, the original intrinsic $\eta_0$, and its analytic root piece. At the same actual root $r_*$, set
$$
 \tau=r-r_*,\qquad
 k_1=K_r(r_*)>0,\qquad k_2=K_{rr}(r_*),\qquad
 \eta_*=-\gamma_*m_*>0.
 \tag{RD.1}
$$
The symbols $k_1,k_2,\eta_*$ are independent of the angular variable. Let $P=1-\Pi$, $I=\partial_\phi^{-1}P$, with normalized measure on the circle of period $\pi/2$. Physical frequencies are $4j$; $P_H$ is the original high projection $|j|\ge97$, $N e_j=4|j|e_j$ there, and $N_*=388$. The independent physical means are not assigned an inverse power of $N$.

The original reflection spaces have first curvature row odd and second row even. The actual inverse
$$
 J=(\eta_*\partial_\phi+L)^{-1},\qquad
 L=PM_{\ell_*}P-2\beta_*P M_{v_\phi}I M_uP,\qquad
 \ell_*=-2\beta_*uv
 \tag{RD.2}
$$
acts from even mean-zero sources to odd states. Its original projections and its full primitive term remain. In particular there is no $J\Pi$.

Here and below all coefficient values in a root formula are evaluated at $r_*$, unless an argument is written. The scalar $\beta$ is the intrinsic coefficient called $b$ in O; it is distinct from the genuine Airy shear $\beta_n$.

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| I, old primitive and actual transport | ddc62b4539d640a950c2005505e08695f80910e7 | 14772 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| O, ordered scalarization | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |
| G, actual fold and genuine amplitudes | 8fa0d675d454a19451f946ed8f8a8eead7145089 | 22688 | c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e |
| A, normalized genuine terminal-Ai column | 62909c54de321da071a6bbc6e169e87b5888dde6 | 15528 | 0e56cf640b5c5f46c917699396e0ef6e5cce1fd5276cbddfc56ee1ed58d89c49 |
| P, first amplitude and actual stable root row | 11250cbb5f9921fdaa70791b6095c306e16bc5d7 | 35230 | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |
| SE, full natural stable operator | eb7b1bb1ea1fdf713fcf172428f68ed20afafdb2 | 20047 | 2220174707046248cbdf9f9f8c47bc13bc233b0ab65f5ed598ddcbf964e93ad4 |
| [N, actual global Riccati frame](R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md) | 6765382c0ea8af731b6593b687cbc84401a4f7ec | 15756 | 0f1383da8611aef931829876b49579f41c7a967435c795ef68a85d2a142cac23 |

The full-family qualification and exact natural weights are those of SE. A complex parameter disk may be used to bound coefficients, but the positivity and coercivity assertions below are for a real parameter and real intrinsic coefficients.

## RD2. The first nonconstant fold coefficient

Use the actual identities G.2:
$$
 D=\partial_r-d\partial_\phi,\qquad
 DT=QX_\phi,\qquad DX=-QT T_\phi,\qquad
 \eta^2K=Q^2T.
 \tag{RD.3}
$$
The scalar $Q$ in this section is the fold coefficient of G, not a background vector. The root normalization is $T(r_*,\phi)=0$, $X(r_*,\phi)=\phi$. Write
$$
 T=\lambda_*\tau+t_2(\phi)\tau^2+O(\tau^3),\qquad
 \lambda_*^3=\eta_*^2k_1,\quad\lambda_*>0.
 \tag{RD.4}
$$
Since $DX=0$ at the root, $X_r=d_*$ there. Thus
$$
 X_\phi=1+d_\phi\tau+O(\tau^2),\qquad
 Q=\lambda_*\left[
  1+\left(\frac{\eta_r}{\eta_*}+\frac{k_2}{4k_1}
                     -\frac{t_2}{2\lambda_*}\right)\tau
 \right]+O(\tau^2).
 \tag{RD.5}
$$
The second identity follows by expanding the exact ratio
$\eta^2K/T$ in $Q^2=\eta^2K/T$; the common root factor is canceled analytically, not divided as an interval containing zero. Comparing the coefficient of $\tau$ in $DT=QX_\phi$ gives
$$
 \boxed{
 \frac{t_2}{\lambda_*}
   =\frac15\left(\frac{k_2}{2k_1}
                  +2\frac{\eta_r}{\eta_*}+2d_\phi\right),\qquad
 \frac{D^2T}{\lambda_*}
   =\frac{k_2}{5k_1}
                  +\frac{4\eta_r}{5\eta_*}+\frac45d_\phi .}
 \tag{RD.6}
$$
For the last expression $D^2T=2t_2$ at the root: $DT$ has constant root value $\lambda_*$, so its angular derivative at that circle vanishes. This is an outward-$r$ formula. Replacing $r$ by $\rho=r_*-r$ without changing the derivatives would reverse terms incorrectly.

## RD3. Exact leading-amplitude derivative, with the complete mean

The normalized local operator of I.18 is
$\partial_T^2+T\partial_X^2+l\partial_T+T^2m\partial_X+v$.
Here $l,m,v$ are the local fold coefficients; they do not replace the nonlocal or independent mean operators of O.

The homogeneous amplitude $w_0=(a_0,b_0)^t$ has
$a_0(0,X)=1$, $b_0=O(T^2)$. The second equation of I.19 at $T=0$ gives
$$
 (a_0)_T(0,X)=-\frac12l(0,X).
 \tag{RD.7}
$$
At the root the coefficient of $\partial_T$ is exactly
$$
 l_*=\frac{D^2T-T_0DT}{\lambda_*^2},\qquad
 T_{0,*}=\frac{\eta_r}{\eta_*}
               -4\beta_*\langle u^2\rangle+5d_\phi .
 \tag{RD.8}
$$
Indeed $K=0$, $DT=Q=\lambda_*$, $X_\phi=1$, and the principal normalization factor is $\mu=\lambda_*^2$; the term $\eta^2K T_{\phi\phi}$ in G.4 is zero at this value before any radial differentiation. O.19 supplies the full mean in $T_0$. The one-gain radial operator of O.18 is not inserted into $T_0$.

Since $DX=0$ at the root, (RD.6)--(RD.8) imply
$$
 \boxed{
 Da_0=\frac{\eta_r}{10\eta_*}-\frac{k_2}{10k_1}
                  -2\beta_*\langle u^2\rangle+\frac{21}{10}d_\phi .}
 \tag{RD.9}
$$
At this root $d_\phi=-\beta_*(u^2-\langle u^2\rangle)$, while the local coefficient of $B_{\rm op}$ is $b_{\rm op}=\beta_*(1-u^2)$. Therefore
$$
 \boxed{
 a_*:=Da_0-b_{\rm op}
 =\frac{\eta_r}{10\eta_*}-\frac{k_2}{10k_1}
       -\beta_*(1+\langle u^2\rangle)+\frac{11}{10}d_\phi .}
 \tag{RD.10}
$$
These identities depend on the actual fold and background coefficients. They do not assume that the repaired reference solves the nonlinear PDE. In particular the complete mean $\langle u^2\rangle$ is retained.

Formula (RD.10) may supply a new bound for this exact coefficient without a generic radial Cauchy bound for $a_0$. It does not supply a bound for $Da_1$, omit the original nonlocal first forcing, or authorize subtracting two existing upper bounds.

## RD4. Genuine root values and an exact positive diagonal

Use $Y_n=\widehat f_n=f_n/a_n$ from A.19, with its actual terminal boundary choice and root normalization. Define real diagonal sequences
$$
 A_n=\operatorname{Ai}(0)+\beta_n\operatorname{Bi}(0),\qquad
 D_n=\operatorname{Ai}'(0)+\beta_n\operatorname{Bi}'(0).
 \tag{RD.11}
$$
For real parameters these sequences are real: the potential and terminal Airy data are real, and ODE uniqueness preserves that reality. Then
$$
 Y_n(0)=A_n,\qquad Y_n'(0)=n^{2/3}D_n,\qquad
 Y_n''(0)=-V_n(0)A_n,\qquad |\beta_n|<1/19 .
 \tag{RD.12}
$$
The Airy primes in (RD.11) are argument derivatives; the $Y_n$ primes in (RD.12) are $T$ derivatives. These are exact initial values, not a large-$n$ expansion.

The official [DLMF 9.2.3](https://dlmf.nist.gov/9.2.E3),
[9.2.4](https://dlmf.nist.gov/9.2.E4),
[9.2.5](https://dlmf.nist.gov/9.2.E5), and
[9.2.6](https://dlmf.nist.gov/9.2.E6) give
$\operatorname{Bi}(0)=\sqrt3\operatorname{Ai}(0)$ and
$\operatorname{Bi}'(0)=-\sqrt3\operatorname{Ai}'(0)$.
Using the already proved P.20 bounds
$\operatorname{Ai}(0)>1/3$, $\operatorname{Ai}'(0)<0$, and $\sqrt3<2$, the complete genuine diagonal satisfies
$$
 \begin{split}
 g_n&:=A_n-\frac{\lambda_*}{\eta_*}D_n\\
 &=\operatorname{Ai}(0)(1+\sqrt3\beta_n)
   +\frac{\lambda_*}{\eta_*}|\operatorname{Ai}'(0)|
                                     (1-\sqrt3\beta_n)\\
 &>\frac{17}{19}
   \left(\operatorname{Ai}(0)
               +\frac{\lambda_*}{\eta_*}|\operatorname{Ai}'(0)|\right)
 >\frac{17}{57}.
 \end{split}
 \tag{RD.13}
$$
Thus $D_g$ is positive on both signed high sectors. The shear has not been replaced by zero. The displayed rational lower bound alone says nothing about the complete remainder.

## RD5. Complete root products, including the projected mean term

Work first with the unweighted high amplitudes of SE.11, before its actual density input factor $N_{\rm in}^{7/6}$:
$$
 F_j=e^{i\epsilon nX}
 \left[(a_0+n^{-1}a_1^V)Y_n
           +(n^{-1}b_0+n^{-2}b_1^V)Y_n'\right],
 \quad
 h_2=PF,\quad h_1=JR,\quad R=(D_0-B_{\rm op})PF .
 \tag{RD.14}
$$
Here $\epsilon=\operatorname{sgn}j$, $D_0=\partial_r-PM_d\partial_\phi P$. At the root $D_0PF=P\,DF$. The genuine amplitudes have their original ordered form
$$
 a_1^V=a_1+\mathcal B_n T b_0,\qquad
 b_1^V=b_1+\mathcal B_n a_0,\qquad
 2T\mathcal B_n'+\mathcal B_n=V_n .
 \tag{RD.15}
$$
Because $a_1(0,X)=0$, $b_0=Db_0=0$, their root derivatives obey
$Da_1^V=Da_1$ and
$Db_1^V=Db_1+\lambda_*\mathcal B_n'(0)+\mathcal B_n(0)Da_0$.

For compact operator notation let
$$
 \mathsf B=\sum_{\epsilon=\pm1}M_{b_{1,\epsilon}(0,\cdot)}P_\epsilon,\quad
 \mathsf B_r=\sum_{\epsilon=\pm1}M_{Db_{1,\epsilon}(0,\cdot)}P_\epsilon,\quad
 \mathsf A_r=\sum_{\epsilon=\pm1}M_{Da_{1,\epsilon}(0,\cdot)}P_\epsilon ,
 \tag{RD.16}
$$
where $P_\epsilon$ are the two original signed high input projections.
Let $D_A,D_D,D_V,D_{\mathcal B},D_{\mathcal B'}$ be the input diagonal sequences $A_n,D_n,V_n(0),\mathcal B_n(0),\mathcal B_n'(0)$.
All right factors in the following formulas act on the original high input. In particular an input diagonal is not commuted through $\mathsf B$ or a multiplier.

Exact differentiation of (RD.14), followed by the original projected $B_{\rm op}$, gives
$$
 H_2:=h_2(r_*)=D_A+E_2,\qquad
 E_2=P(\mathsf B+D_{\mathcal B})D_DN^{-4/3},
 \tag{RD.17}
$$
$$
 R=\lambda_*D_DN^{2/3}+R_0,
 \tag{RD.18}
$$
where the complete bounded root operator is
$$
 \begin{split}
 R_0={}&PM_{a_*}D_A+P\mathsf A_rD_AN^{-1}\\
 &+P\{\mathsf B_r-M_{b_{\rm op}}\mathsf B
               +M_{a_*}D_{\mathcal B}
               +\lambda_*D_{\mathcal B'}\}D_DN^{-4/3}\\
 &-\lambda_*P(\mathsf B+D_{\mathcal B})D_VD_AN^{-2}\\
 &+PM_{b_{\rm op}}\Pi(\mathsf B+D_{\mathcal B})D_DN^{-4/3}.
 \end{split}
 \tag{RD.19}
$$
At $K=0$ the original nonlocal term
$-2\beta K P M_{v_\phi}I M_vP$ in $B_{\rm op}$ vanishes as a value.
No radial derivative of that term has been set to zero.
The last line of (RD.19) is precisely the rank term produced by
$B_{\rm op}=PM_{b_{\rm op}}P$ acting on the root height correction.
It cannot be discarded merely because the reconstructed $h_2$ is mean-zero.
The full nonlocal operator $L$ still remains inside $J$.

For verification, the four terms in $DF_j$ surviving at the root are
$$
 e^{4ij\phi}\left[
  (Da_0+n^{-1}Da_1^V)A_n+\lambda_*n^{2/3}D_n
    +n^{-4/3}(Db_1^V)D_n
    -n^{-2}\lambda_*b_1^VV_n(0)A_n\right].
 \tag{RD.20}
$$
There is no $nDX$ term because $DX=0$ exactly. Subtracting
$PM_{b_{\rm op}}P F$ gives (RD.19), with its displayed positive mean-rank term. The true independent mean source of the trial and its positive correction are retained in their original ports; (RD.19) is not a convention that sets those sources to zero.

## RD6. The exact stable row and its complete error

Let $\mathcal Z e_j=i\,\operatorname{sgn}(j)e_j$ on nonzero modes, zero on the mean. Thus $\mathcal ZI=N^{-1}P$. The original global Riccati frame has $g_n(r_*)=n^{-1/3}$ and $p_n(r_*)=n^{-1/3}\widetilde p_n$, with $0<\widetilde p_n<66$. Direct inversion of the N.1 frame gives its first root row
$$
 (1+\widetilde p_n)^{-1/2}
                  [h_{2,n}-i\epsilon n^{1/3}h_{1,n}].
 \tag{RD.21}
$$
This is the true global reference, not a local Airy impedance.

Removing the positive bounded output diagonal in (RD.21) defines
$$
 \widehat S=P_H[H_2-\mathcal ZN_{\rm out}^{1/3}JR].
 \tag{RD.22}
$$
It is the corresponding normalized stable trace of the actual PC/IN corrected high family: its correction has zero stable root input, as in SE6. The other true boundary and source columns have not been replaced.

From the exact old-circle identity
$$
 J=\eta_*^{-1}I-JL\eta_*^{-1}I
 \tag{RD.23}
$$
one obtains, without interchanging input and output weights,
$$
 \boxed{
 \widehat S=D_g+E,\quad
 E=P_HE_2-\eta_*^{-1}P_HN_{\rm out}^{-2/3}R_0
       +P_H\mathcal ZN_{\rm out}^{1/3}
                               JL\eta_*^{-1}IR.}
 \tag{RD.24}
$$
All terms are complete original-angle operators on the original reflected high input. The $P_H$ in (RD.24) selects the stable high output of the actual graph; removed low outputs remain separate physical equations.

Suppose complete same-domain bounds have been established:
$$
 \|E_2\|_{L^2_H\to L^2}\le e_2,\quad
 \|R_0\|_{L^2_H\to L^2_{\rm even,0}}\le r_0,\quad
 \|\partial_\phi J\|_{L^2\to L^2}\le J_1,\quad
 \|L\|_{L^2\to L^2}\le L_0,\quad
 \sup_n|D_n|\le D_* .
 \tag{RD.25}
$$
The spaces of each $J,L,I$ in a product are those in RD1. Then
$$
 \boxed{
 \|E\|_{L^2_H\to L^2_H}\le
 e:=e_2+\frac{N_*^{-2/3}}{\eta_*}
       \left[r_0+J_1L_0
          \left(\lambda_*D_*N_*^{-1/3}+\frac{r_0}{4}\right)\right].}
 \tag{RD.26}
$$
Indeed
$\|P_HN_{\rm out}^{1/3}J\|\le N_*^{-2/3}\|\partial_\phi J\|$.
On the input,
$\|I\lambda_*D_DN_{\rm in}^{2/3}\|
 \le\lambda_*D_*N_*^{-1/3}$,
whereas the full $R_0$ may generate low nonzero frequencies, so its primitive costs $r_0/4$, not $r_0/N_*$.
This distinction retains every intermediate frequency.

If an outward evaluation establishes
$$
 e<g_-\le\inf_{|j|\ge97}g_n
 \qquad\text{(for example $g_-=17/57$)},
 \tag{RD.27}
$$
then
$\|\widehat Sf\|_2\ge(g_--e)\|f\|_2$.
Thus its kernel and the true $S_{\rm nat}$ kernel vanish.
Alternatively a direct Neumann series around $D_g$ proves the same $L^2$ isomorphism. In that case
$
 \|\widehat S^{-1}\|_{L^2\to L^2}\le(g_--e)^{-1},\qquad
 \|S_{\rm nat}^{-1}\|_{L^2\to L^2}
            \le\sqrt{67}\,(g_--e)^{-1}.
$
SE's same-domain Fredholm index zero and smooth-kernel bootstrap then give the same inverse on every fixed natural Sobolev window, including $-7/6$ and $-5/2$. This last statement supplies qualitative fixed-window boundedness; the displayed $L^2$ inverse bound is not silently used as the norm in a negative window.

## RD7. One finite recipe for the whole-operator inputs

A bound for a complete signed multiplier
$\sum_\epsilon M_{f_\epsilon}P_\epsilon$ is, for example,
$\sum_\epsilon\|f_\epsilon\|_\infty$.
This is a whole $L^2$ operator bound with all output frequencies, not a sum of unrelated scalar column bounds. Sharper proved bounds may replace it.

Let $B_1,B_{1r},A_{1r}$ bound respectively the three operators in (RD.16), and let
$a^\#,b^\#,A_*,D_*,V_*,\mathcal B_*,\mathcal B'_*$
denote nonnegative bounds for the sup norm of the coefficient in (RD.10), $\|b_{\rm op}\|_\infty$, and the five input diagonals in RD5. The exact expressions imply the valid complete choices
$$
 e_{\rm amp}=(B_1+\mathcal B_*)D_*N_*^{-4/3},\qquad e_2=e_{\rm amp},
 \tag{RD.28}
$$
$$
 \begin{split}
 r_0={}& A_*(a^\#+A_{1r}/N_*)\\
 &+D_*N_*^{-4/3}
      \{B_{1r}+b^\#B_1+a^\#\mathcal B_*+\lambda_*\mathcal B'_*\}\\
 &+\lambda_*V_*A_*(B_1+\mathcal B_*)N_*^{-2}
      +b^\#e_{\rm amp} .
 \end{split}
 \tag{RD.29}
$$
The quantity $e_{\rm amp}$ bounds the whole unprojected root amplitude correction as well as $E_2$. This is why the final $b^\#e_{\rm amp}$ safely charges the complete mean term. A smaller bound known only after applying $P$ cannot replace $e_{\rm amp}$ in that last term. A complete same-root bound for $L$ can likewise be obtained directly from (RD.2), keeping both its multiplier and primitive terms. Previously certified stronger $J_1,L_0$ may instead be read with their exact root-family domain.

Only the precise low-order quantities in (RD.25), (RD.28)--(RD.29) are needed for this sufficient gate. The values of free $b_1,Db_1,Da_1$, the genuine potential and its $\mathcal B$ correction must be read from successful original conclusions or paid as genuinely new smaller-root expressions. A component-sum budget must not be interpreted as a componentwise signed identity. Input-dependent coefficients require their actual complete operator bounds; the analytic weighted-Schur theorem SE2 is one available route if a scalar-multiplier representation is unavailable.

## RD8. Scope of the new gate

Equations (RD.6), (RD.9), (RD.10), (RD.17)--(RD.24) are exact identities. Equation (RD.13) is a genuine positive diagonal statement, with both Airy signs and the nonzero shear. Equation (RD.27) remains a separate numerical obligation; no existing successful computation is repeated here, and no actual $e$ or pass verdict is asserted.

A coarse upper bound failing (RD.27) would not prove a kernel or failure of the actual operator. The finite Fredholm completion FC remains a distinct exact way to parametrize the same regular graph. Conversely, passing (RD.27) would prove faithfulness of these original high Ai parameters; it would still not prove the complete waist incoming inverse, a finite bordered inverse, the coupled source/mean equations, or the nonlinear boundary problem. No selfadjointness, conserved same-solution flux, or true-PDE property of the repaired centre has been assumed.
