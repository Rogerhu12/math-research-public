# R133 supplement: the complete common root piece to the actual Airy port

2026-11-13, visible-exact / phase_inverse. **Proved, with 14 actual native
gates passed.** The object is the complete amplitude-$3/4$, M256 accepted
reciprocal centre, SHA
`45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`.
Its exact $\nu$, the whole $|\eta|\le10^{-9}$ box, every Fourier row,
both original mean states, and the primitive infinite remainder remain.

This fills the previously open interval **inside** the actual common
root candidate piece, from

$$r_c=\frac{8584986789675009}{36028797018963968}
 \quad\hbox{to}\quad r_*(\eta)-2^{-37},                              \tag{C.1}$$

then attaches the true, angle-dependent fixed-$r$ graph to the negative
canonical Airy section $T=-2^{-36}$. The propagation here is in the
original physical angle and the full original physical Jacobi equation.
It does not assume that the approximate centre solves the PDE.

At $r_c$, put $q=\sqrt{-K}$ and define three nonnegative quantities

$$E_0=\|(h_1,qh_2)\|_2,\quad
 E_1=\|(\partial_\theta h_1,q\partial_\theta h_2)\|_2,\quad
 Y_2=\|h_2\|_2.                                                       \tag{C.2}$$

The actual complete output contract is

$$
\boxed{\begin{aligned}
 \|U(-2^{-36})\|_{\mathcal E}
 <{}&3.177535 E_0(r_c)+1.092806 E_1(r_c)+2.232460 Y_2(r_c)\\
 &+0.069923777\|f\|_{H^1(\Omega_s)}
   +0.001045787\|f\|_{H^1(\Omega_g)} .
\end{aligned}}                                                       \tag{C.3}
$$

$\Omega_s$ is the true physical strict region in (C.1); $\Omega_g$ is
the exact physical between-graph domain from the preceding
[fixed radial port theorem](R133-supplement-actual-fixed-radial-to-Airy-ports.md).
The last source norm includes the physical radial derivative. The first
one may instead be replaced by the corresponding explicitly displayed
$L^1_rH^1_\theta$ source bound below.

There is no division by the terminal $q$, which is only about $2.1\cdot
10^{-5}$, in (C.3). The key exact cancellation is
$H_{\rm can}^{1/2}F^{-1}=\sqrt b\,H_{\rm phys}^{1/2}$ at the genuine
fixed-$r$ graph. Retaining $Y_2$ as the third comparison row avoids
converting the entire degenerate energy into an ordinary two-state
norm at that intermediate circle.

## 1. The whole actual interval is certified at once

The new native consumer reads the exact right-side candidate piece
1015 beginning at $r_c$, and the original scalar germ

$$
\left[\frac{8556839292003943}{36028797018963968},
      \frac{8636031980136455}{36028797018963968}\right].                 \tag{C.4}
$$

The whole closed real radial envelope $[r_c,r_*^+]$, including the
complete root enclosure, lies strictly inside the right end of that
same candidate piece. No PPoly join lies inside this theorem. The
preceding exterior strict bridge has already paid the jump *into*
piece 1015; its right-side initial trace is the trace required here.

The compact metric change is identically zero here because $r_c>.18$.
The consumer re-evaluates the original complete intrinsic primitive,
including the full affine parameter and its infinite remainder. The
energy is the bilinear zero convolution of the primitive derivatives,
with every arithmetic and omitted-tail fee retained. The candidate
$u=\alpha U$, $v=s+\alpha V$ is evaluated as the full exact dyadic cubic
PPoly and all 513 real sine/cosine/mean rows. Its real angular bounds
through order two are full Wiener sums, not a grid or a projection.

The true complete gates give

$$
 K'>59.40844045,\qquad |K'|<62.82318587,
 \qquad -v>0.5033188504.                                  \tag{C.5}
$$

For each actual parameter, the exact identity

$$-K(r)=(r_*-r)\int_0^1K'(r_*+t(r-r_*))\,dt                 \tag{C.6}$$

proves negativity all the way to the parameter-dependent terminal
circle in (C.1). Thus $q_{\rm terminal}>2.0790702\cdot10^{-5}$,
while on the whole interval $q^2<0.007263887$. Its length is at most
$\ell_*<0.000115624294$. This argument does not evaluate a broad
fixed radial interval containing the root and then incorrectly assert
that every parameter has negative curvature at its upper endpoint.

## 2. The actual local linearization and its full cancellation

Write $y=Rh$, $R=\operatorname{diag}(-1,1)$. The exact physical
linearization has the form

$$
 y_r=(dI+aJ(K))y_\theta+L y+Rf,
 \quad d=\gamma u,\ a=-\gamma v>0,\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.               \tag{C.7}
$$

In the reflected frame $L_{12}=K L_{21}$ exactly. The absolute bounds
are those of the unreflected coefficients

$$
\begin{aligned}
 g&=\gamma v_\theta-2\beta uv,\\
 L_{11}&=\gamma u_\theta-\beta(1+3u^2+Kv^2),\\
 L_{22}&=-\gamma u_\theta+\beta(1-u^2-3Kv^2).
\end{aligned}                                                        \tag{C.8}
$$

The reflection only changes the signs of the two off-diagonal entries.
Set $Q=-K$, $H=\operatorname{diag}(1,Q)$ and
$A=dI+aJ(K)$. Then $HA$ is real symmetric and the off-diagonal part
of $HL+L^*H$ vanishes exactly. The energy identity is

$$
 (\|H^{1/2}y\|_2^2)'=
 \langle y,[H_r-(HA)_\theta+HL+L^*H]y\rangle
 +2\operatorname{Re}\langle Hy,Rf\rangle.                \tag{C.9}
$$

The additional lower diagonal term is $Q_r/Q=-K'/Q<0$.
We discard it only in the **forward**, increasing-$r$ estimate.
We do not turn this assertion into a reverse Cauchy estimate.
The remaining conjugated matrix has diagonal entries
$2L_{ii}-d_\theta$ and off-diagonal entry $q a_\theta$.

Let a star denote a full upper bound over the complete interval and
all physical angles. Define

$$
\begin{aligned}
 \rho_0&=\max(L_{11}^*,L_{22}^*)+\tfrac12(d_\theta^*+q^*a_\theta^*),\\
 \rho_1&=\rho_0+d_\theta^*+q^*a_\theta^*,\\
 \lambda&=\max(L_{11,\theta}^*,L_{22,\theta}^*)+q^*g_\theta^*,\\
 \rho_2&=L_{22}^*+d_\theta^*/2 .
\end{aligned}                                                        \tag{C.10}
$$

The exact differentiated equation adds $A_\theta y_\theta$ to the
first-order term and $L_\theta y$ to the source. Since
$\|H^{1/2}A_\theta H^{-1/2}\|\le d_\theta^*+q^*a_\theta^*$,
the complete first two comparison inequalities are

$$E_0'\le\rho_0E_0+\|f\|_2,\qquad
 E_1'\le\lambda E_0+\rho_1E_1+\|f_\theta\|_2.            \tag{C.11}$$

Here $q<1$, so the full physical source controls its weighted version.
All coefficient derivative costs in $\lambda$ are explicit:

$$
\begin{aligned}
 g_\theta^*&\le\gamma^*V_2+2\beta^*(U_1V_0+U_0V_1),\\
 L_{11,\theta}^*&\le\gamma^*U_2+\beta^*(6U_0U_1+2Q^*V_0V_1),\\
 L_{22,\theta}^*&\le\gamma^*U_2+\beta^*(2U_0U_1+6Q^*V_0V_1),
\end{aligned}                                                        \tag{C.12}
$$

where $U_j,V_j$ are the complete candidate Wiener derivative bounds.
Thus (C.11) does not require an uncomputed higher angular tail.

## 3. The third row is the ordinary second component

The actual second row is

$$ (y_2)_r=d(y_2)_\theta-a(y_1)_\theta+L_{21}y_1+L_{22}y_2+(Rf)_2.
                                                                    \tag{C.13}$$

Using its real scalar transport, rather than a conversion by $q^{-1}$,
gives

$$Y_2'\le g^*E_0+a^*E_1+\rho_2Y_2+\|f_2\|_2.           \tag{C.14}$$

This includes the complete mean of $y_2$. No inverse angular derivative
or mean-zero hypothesis occurs. The comparison state
$Z=(E_0,E_1,Y_2)^{\mathsf T}$ therefore obeys

$$
 Z'\le MZ+F,\quad
 M=\begin{pmatrix}\rho_0&0&0\\\lambda&\rho_1&0\\g^*&a^*&\rho_2\end{pmatrix},
 \quad F\le\|f\|_{H^1_\theta}(1,1,1)^{\mathsf T}.         \tag{C.15}
$$

The actual matrix has the following safe upper entries:

$$
 M<\begin{pmatrix}
 9.408909&0&0\\
 69.795128&15.566637&0\\
 6.180341&2.339375&8.909061
 \end{pmatrix}.                                                       \tag{C.16}
$$

Since $M$ has nonnegative entries, $e^{M\ell_*}$ bounds all forward
subintervals and all source insertion times. The complete native
comparison is

$$
 P_s\le
 \begin{pmatrix}
 1.001088491&0&0\\
 0.008081674&1.001801503&0\\
 0.000716448&0.000270872&1.001030635
 \end{pmatrix}+10^{-74}{\bf1}_{3\times3}.                 \tag{C.17}
$$

The last harmless matrix retains the native exponential tail at every
entry. Specifically the source sums terms through degree 24; if
$s=\|M\ell_*\|_\infty$, the omitted operator norm is at most
$s^{25}/[25!(1-s/26)]<4.649\cdot10^{-76}$. This is a complete
matrix exponential, with no frequency or time truncation.

For smooth data the actual hyperbolic system has real characteristic
curves and a coupled zero-order Volterra representation. Iteration
converges on compact strict subintervals, and (C.11)–(C.14) give the
uniform $H^1$ and ordinary second-row bounds up to the terminal circle.
The latter still has $q>0$ by (C.6). Approximation extends the result
to the displayed source and input spaces. This supplies both existence
and the stated comparison, not only a conditional energy calculation.

## 4. Exact curvature-weight cancellation at the true graph

At the terminal fixed-$r$ circle, the actual fold has
$q_{\rm can}=\sqrt{-T}=bq_{\rm phys}$ and
$F=\operatorname{diag}(b^{-1/2},b^{1/2})$. Therefore

$$
 H_{\rm can}^{1/2}F^{-1}
 =\sqrt b\,H_{\rm phys}^{1/2},\qquad
 H_{\rm can}=\operatorname{diag}(1,-T),\quad
 H_{\rm phys}=\operatorname{diag}(1,-K).                  \tag{C.18}
$$

The fixed physical radius has the actual angular Jacobian
$x_\theta=X_\theta(r_*-2^{-37},\theta)>0$. It follows exactly from
$U=F^{-1}Rh$ and the product rule that

$$
\begin{pmatrix}E_{0,\rm can}\\E_{1,\rm can}\\\|U_2\|_2\end{pmatrix}
\le W_g\begin{pmatrix}E_{0,\rm phys}\\E_{1,\rm phys}\\Y_{2,\rm phys}\end{pmatrix},
\quad
W_g=\begin{pmatrix}
 \sqrt{b_+x_+}&0&0\\
 \sqrt{b_+/x_-}\,\ell_\theta^*/2&\sqrt{b_+/x_-}&0\\
 0&0&F_*\sqrt{x_+}
\end{pmatrix},                                                       \tag{C.19}
$$

where $\ell_\theta^*=|(\log b)_\theta|^*$ and $x_\pm$ are the
previously proved fixed-$r$ angular bounds. Numerically

$$
 W_g<\begin{pmatrix}
 .583785020&0&0\\1.005147053&.583785020&0\\0&0&2.190537114
 \end{pmatrix}.                                                       \tag{C.20}
$$

In particular no $q_{\rm terminal}^{-1}$ has been inserted into this
port conversion. Both derivative and angular measure are paid.

The complete reverse graph propagation proved in Sections 4–5 of the
fixed-radial theorem acts on these same three quantities. Its matrix is

$$
 P_g<\begin{pmatrix}
 1.862681437&0&0\\
 .335380438&1.862681437&0\\
 2.146724\cdot10^{-9}&6.693911\cdot10^{-11}&1.000002915
 \end{pmatrix}.                                                       \tag{C.21}
$$

It includes all angle-dependent graph effects, and its independent
ordinary physical source column is preserved separately.

## 5. Full padded Airy output and complete source assembly

The full Airy norm is
$\mathcal E=\|\langle D_X\rangle^{1/6}
\operatorname{diag}(W,W^{-1})U\|_2$, with
$W_m=(2^{-36}+|m|^{-2/3})^{-1/4}$ at $m\ne0$ and identity at the
two independent means. The previous exact inequality gives

$$\|U\|_{\mathcal E}^2\le H_*^2+q_-^{2/3}Y_*^{5/3}H_*^{1/3}
                                      +c_*Y_*^2,                       \tag{C.22}$$

where $H_*=(E_0^2+E_1^2)^{1/2}$, $q_-=2^{-18}$ and
$c_*=(\sqrt{17}/4)^{1/3}$. The ordinary weighted AM–GM inequality
$Y^{5/6}H^{1/6}\le5Y/6+H/6$ therefore gives the complete linear row

$$
 \|U\|_{\mathcal E}
 \le A_H(E_0+E_1)+A_Y Y_2,
 \quad A_H=1+q_-^{1/3}/6,
 \quad A_Y=\sqrt{c_*}+5q_-^{1/3}/6.                      \tag{C.23}
$$

The whole assembly, in its actual order, is

$$ (A_H,A_H,A_Y)\,P_g\,W_g\,P_s .                         \tag{C.24}$$

The directed result is

$$ (C.24)<(3.177535,\ 1.092806,\ 2.232460).                \tag{C.25}$$

There is no interchange of these matrices and no scalarization of
the mean before (C.24). Every actual mode, all mean transitions, and
the complete local zero-order matrix have been retained throughout.

For a strict source, positivity of $P_s$ bounds every insertion by
$P_s(1,1,1)^{\mathsf T}$. Thus its complete $L^1_rH^1_\theta$ cost
is at most the sum of the three unrounded entries in (C.24), less than
$6.502800$. Cauchy–Schwarz in the true radial interval then gives
the coefficient $0.069923777$ in (C.3) for the physical full $H^1$
norm. For the local graph source, the previously proved columns
$sE_0,sE_1,sY_2$ give

$$A_H(sE_0+sE_1)+A_YsY_2<0.001045787,                     \tag{C.26}$$

with the same exact physical source domain and density as before.

## 6. Permissions of this conclusion

The ordinary $H^1$ data at $r_c$ supply (C.2); retaining its three
entries is preferable to prematurely absorbing $Y_2$ into
$E_0/q(r_c)$. If that last simplification is desired, the external
strict certificate proves $q(r_c)^{-1}<11.896$, and it is paid only
at this nondegenerate outer circle. No such division is used at the
near-root circle.

The output is a genuine full negative Airy port for the original
physical operator at the specified approximate centre. When the input
is obtained from a moving-coordinate linearization, the separate
residual-sensitive variation bridge must still be supplied. This
theorem does not silently set that residual to zero. It also makes no
reverse-common-piece, positive regular graph, full feedback inverse,
or nonlinear body existence assertion.

The coefficient inequalities and the ordered three-state assembly
apply to any centre for which their hypotheses have actually been
paid. The numerical values above are certified only for the named
complete amplitude-$3/4$ centre. A later moving or reciprocal centre
requires its own actual coefficient, inverse-angle, and germ inputs.

## 7. Reproduction and saved attempt

Source:
`scripts/fourfold_codazzi_common_root_piece_strict_ports.py`.
Complete native:
`notes/2026-11-13-R133-actual-alpha075-common-root-piece-strict-ports-native.json.gz`.
The complete calculation takes approximately 1.6 seconds and passes
14 gates. All input and source dependency SHAs are retained. The
large exact candidate is supplied explicitly from its existing
reconstruction manifest, without another repository copy.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/fourfold_codazzi_common_root_piece_strict_ports.py --candidate /workspace/scratch/ac0d699811ad/reciprocal-m256-alpha075-accepted000-candidate.json --out notes/2026-11-13-R133-actual-alpha075-common-root-piece-strict-ports-native.json.gz
```

The first attempt reached report serialization but failed because the
primitive-tail Arb value was not converted to its standard record.
No native conclusion was saved from that attempt. The small record
`notes/2026-11-13-R133-common-root-piece-strict-attempt01-serialization.json`
preserves that source SHA and the exception. The corrected source
recomputed the whole result before publishing the complete report.
