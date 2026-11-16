# R133 supplement: exact two-sided normalization of the reflected waist first coefficient

2026-11-16, phase_inverse.

**Proved analytic normalization with a complete conditional physical-error bound.** The true cohomological normalizer preserves the geometric reflected target after its full scalar mean row is retained. A different, explicitly compressed source normalizer preserves the ordinary-sign reflected input. Its inverse exists without a smallness assumption: the source correction is skew-adjoint in the positive primitive pairing. The two normalizers remove the variable first coefficient in their true order.

The source inverse and its two Sobolev-window bounds are proved here. All new bounds are symbolic positive expressions. No coefficient solve, exponential, old scalar budget, ray, native object, or scientific target is evaluated. Applying this reduction to the actual waist row retains its complete second-order waist term, scalar mean rank, physical state error, true input intertwiner, and transported finite complement.

## WBN1. The same selected coefficient and two different reflection spaces

Use the original selected real member and its true selected chart from RRF, WPL and WIT. The circle has length $\pi/2$ and normalized measure. Write
$$
 e_j(x)=e^{i4jx},\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 P=Id-\Pi,\qquad I=\partial_x^{-1}P,
$$
$$
 Z_0=i\Pi_+-i\Pi_-,\qquad Z_{\rm full}=\Pi+Z_0,\qquad
 R_cf(x)=f(c-x),\qquad b=a+\Omega .
 \tag{WBN.1}
$$
The phase $a$ is the actual RRF reflection phase; it is not set to zero. On the nonmean carrier, $Z=Z_0$ satisfies $Z^2=-Id$ and $R_cZ=-ZR_c$. Define
$$
 K_b=-ZR_b,\qquad
 X_b^s=\operatorname{Fix}(K_b)\cap H^s_0,\qquad
 Y_a^s=\operatorname{Fix}(R_a)\cap H^s_0,\qquad
 Q_a=P\frac{Id+R_a}{2}.
 \tag{WBN.2}
$$
Here $H^s_0=PH^s$. Both reflection projections have norm one in their inherited Bessel spaces. There is no Fourier cutoff in (WBN.2).

The exact complete-coefficient identity of WPL is used as an explicit premise:
$$
 c_i=\nu+v_i,\qquad \Pi v_i=0,\qquad
 c_o=-R_b c_i,\qquad
 \Pi c_o=-\nu,\qquad \mu=-2\nu .
 \tag{WBN.3}
$$
It comes from the complete PF/CT root coefficients, including their common odd finite root function, and the same selected density change. It is not inferred from nearly equal numerical norm bounds. The exact local metric parity and compact-support argument in WPL identifies $c_i$ as the first coefficient of the normalized physical primitive row: the first waist normalizer is zero, whereas the second normalizer remains.

The current lemma uses the actual real functions of that same identity. Their already qualified regularity gives $v_i\in H^3$, and the original real cohomological solution below has $w\in H^2$. These regularities suffice for all products and distributional mean pairings used here. The conclusions concern the two windows $s=0,-4/3$; no all-order tame estimate is assigned.

The two scalar means in (WBN.3) are not physical mean unknowns. The stored physical means, the actual even-mean equation, the amplitude row and all independently prescribed ports retain their existing realization.

## WBN2. Cohomology gives one odd function for each reflection

Let $U_{-\Omega}f(x)=f(x-\Omega)$ and set
$$
 v=(c_o-c_i)-\mu=-(v_i+R_bv_i).
$$
Use the same, already constructed CN/NW mean-zero solution
$$
 (U_{-\Omega}-Id)w=v,\qquad \Pi w=0.
 \tag{WBN.4}
$$
The original irrational rotation and its certified divisor bound give uniqueness of a mean-zero solution. No new cohomological solve is performed.

The exact operator identities are
$$
 R_bU_{-\Omega}=R_a,\qquad U_{-\Omega}R_a=R_b,\qquad R_bv=v.
 \tag{WBN.5}
$$
Consequently
$$
 (U_{-\Omega}-Id)(-R_aw)
       =R_aw-R_bw
       =R_b(U_{-\Omega}-Id)w=v.
$$
Both $w$ and $-R_aw$ have zero mean, so uniqueness gives
$$
 R_aw=-w,\qquad R_a(Iw)=Iw .
 \tag{WBN.6}
$$
Applying $R_b$ to (WBN.4), and using (WBN.6), also gives
$$
 w+R_bw=v_i+R_bv_i .
$$
To avoid confusing the source coefficient with the geometric phase $a$, denote it by
$$
 \boxed{\quad \alpha=v_i-w,\qquad R_b\alpha=-\alpha,\qquad \Pi\alpha=0.\quad}
 \tag{WBN.7}
$$
Thus $w$ is odd for the target reflection $R_a$, while $\alpha$ is odd for the source reflection $R_b$. Their roles are different even though they arise from the same complete cohomological equation.

## WBN3. The target normalizer and its complete mean row

Keep the original full-circle normalizer
$$
 N=Id+M_wI .
 \tag{WBN.8}
$$
Since $R_aIR_a=-I$ and $R_aw=-w$, it satisfies
$$
 [N,R_a]=[N^{-1},R_a]=0,\qquad N1=N^{-1}1=1 .
 \tag{WBN.9}
$$
The inverse is the same CN/NPK inverse, not an inverse newly inferred from the reflection identity.

For completeness its two weighted means remain explicit. With $p=Iw$ and $A_w=e^p$, the original formulas are
$$
 m_f=\frac{\langle A_wf\rangle}{\langle A_w\rangle},\qquad
 u=I\{A_w(f-m_f)\},\qquad
 \kappa_f=-\frac{\langle A_w^{-1}u\rangle}
                    {\langle A_w^{-1}\rangle},
$$
$$
 z=A_w^{-1}(u+\kappa_f),\qquad N^{-1}f=f-wz .
 \tag{WBN.10}
$$
The first mean gives $\Pi(N^{-1}f)=m_f$; the second gives $\Pi z=0$. These are distribution pairings at the negative index. Formula (WBN.10) is recalled as an exact identity; no exponential is evaluated here.

On $PH^s$ define
$$
 N_\perp=PNP,\qquad
 \boxed{\quad N_\perp^{-1}=PN^{-1}P.\quad}
 \tag{WBN.11}
$$
For example, if $f=Pf$, then
$PN(PN^{-1}f)=P\{f-(\Pi N^{-1}f)1\}=f$.
The other product uses $N^{-1}1=1$ in the same way. Hence (WBN.11) is a true two-sided inverse on each stated window, and both factors commute with $R_a$. They therefore restrict to the geometric target $Y_a^s$.

This compression does not delete the scalar mean row. In the order $PH^s\oplus\mathbb C$, write
$$
 \ell_w=\Pi M_wI|_{PH^s}.
$$
The full operators are exactly
$$
 N=\begin{pmatrix}N_\perp&0\\ \ell_w&1\end{pmatrix},
 \qquad
 N^{-1}=\begin{pmatrix}
 N_\perp^{-1}&0\\ -\ell_wN_\perp^{-1}&1
 \end{pmatrix}.
 \tag{WBN.12}
$$
The full-circle inverse can create an output mean from nonmean input. Any actual mean or amplitude row must be transported with this block, rather than replaced by its restriction to the upper-left entry.

Let $K_{N,0}$ and $K_{N,-}$ be complete evaluated bounds already available for the same $N^{-1}$ in $L^2$ and $H^{-4/3}$, respectively. The whole retained NPK bounds may be used. Orthogonal projections show
$$
 \|N_\perp^{-1}\|_0\le K_{N,0},\qquad
 \|N_\perp^{-1}\|_{-4/3}\le K_{N,-}.
 \tag{WBN.13}
$$
No logarithmic-only certificate is inserted into a product as though it were a norm. No inverse of the individual incoming factor is needed for (WBN.11)--(WBN.13).

## WBN4. An exact source operator preserving both signs and reflection

On the complete nonmean carrier define the two same-sign multiplication blocks
$$
 \mathcal T_\alpha
   =\Pi_+M_\alpha\Pi_++\Pi_-M_\alpha\Pi_-,
 \qquad
 B_\alpha=\mathcal T_\alpha I,\qquad
 \mathcal A=Id-B_\alpha .
 \tag{WBN.14}
$$
The output of each block stays in its own nonzero sign. Real $\alpha$ makes $\mathcal T_\alpha$ self-adjoint in ordinary $L^2$, and
$$
 \|\mathcal T_\alpha\|_{L^2\to L^2}\le\|\alpha\|_\infty,\qquad
 [\mathcal T_\alpha,Z]=0,\qquad
 R_b\mathcal T_\alpha R_b=-\mathcal T_\alpha .
 \tag{WBN.15}
$$
The norm has no extra factor for two signs: the input and output sign spaces are mutually orthogonal.

Because $R_bIR_b=-I$, (WBN.15) implies
$$
 [\mathcal A,Z]=[\mathcal A,R_b]=[\mathcal A,K_b]=0.
 \tag{WBN.16}
$$
The operator also commutes with complex conjugation. Thus it preserves the real form and the nonmean source reflection space $X_b^s$. Its inverse, once constructed below, has the same exact commutations. It is not a high-frequency compression, and no smallness of $\alpha$ is required.

## WBN5. A bounded skew correction in the positive primitive pairing

Use exactly the positive pairing of WIT:
$$
 G=IZ=|\partial_x|^{-1},\qquad
 \mathscr H=\dot H^{-1/2}_0,\qquad
 \|f\|_{\mathscr H}^2
       =\sum_{j\ne0}(4|j|)^{-1}|\widehat f_j|^2.
 \tag{WBN.17}
$$
In particular $I=-GZ$. The map $G^{1/2}$ is an isometry from $\mathscr H$ to $L^2_0$. On smooth nonmean data,
$$
 G^{1/2}B_\alpha G^{-1/2}
      =-G^{1/2}\mathcal T_\alpha G^{1/2}Z.
 \tag{WBN.18}
$$
The expression on the right is a bounded $L^2_0$ operator. Its norm is at most $\|\alpha\|_\infty/4$, since
$\|G^{1/2}\|_{L^2_0\to L^2_0}=1/2$.
The middle self-adjoint operator commutes with the skew-adjoint $Z$. Hence (WBN.18) is skew-adjoint, and it extends the same $B_\alpha$ boundedly to $\mathscr H$.

Equivalently, with dagger denoting the $\mathscr H$ adjoint,
$$
 B_\alpha^\dagger=-B_\alpha,\qquad
 \mathcal A^\dagger=Id+B_\alpha,\qquad
 \operatorname{Re}(u,\mathcal Au)_{\mathscr H}
       =\|u\|_{\mathscr H}^2 .
 \tag{WBN.19}
$$
No claim of ordinary $L^2$ skew-adjointness is made for $B_\alpha$ itself. The weighting in (WBN.18) is essential.

Both $\mathcal A$ and its $\mathscr H$ adjoint are bounded below by one. Thus $\mathcal A$ has closed range, and its range has zero orthogonal complement because its adjoint has zero kernel. This proves a genuine onto statement and
$$
 \boxed{\quad
 \mathcal A_{\mathscr H}^{-1}:\mathscr H\to\mathscr H
 \text{ exists},\qquad
 \|\mathcal A_{\mathscr H}^{-1}\|\le1.
 \quad}
 \tag{WBN.20}
$$
This is an accretive inverse for an arbitrary size of the real coefficient. It is not a Neumann-series claim.

## WBN6. The same source inverse in the two required windows

Set
$$
 C_I=\frac{\sqrt{17}}4,\qquad
 A_0\ge\|\alpha\|_\infty,\qquad
 A_{1/3}\ge W_{1/3}(\alpha),
$$
$$
 W_{1/3}(f)=\sum_{j\in\mathbb Z}
                       (1+4|j|)^{1/3}|\widehat f_j|.
 \tag{WBN.21}
$$
All three quantities in (WBN.21) are symbolic upper inputs here. The existing complete bounds for $v_i$ and $w$ can give $A_0$ and $A_{1/3}$ by positive sums, without subtracting their upper bounds.

The physical frequency convention gives
$$
 \|f\|_{\mathscr H}\le\tfrac12\|f\|_2,\qquad
 \|If\|_2\le\tfrac12\|f\|_{\mathscr H},\qquad
 \|g\|_{H^{-4/3}}\le\|g\|_{\mathscr H}.
 \tag{WBN.22}
$$
For $f\in L^2_0$, first take $u=\mathcal A_{\mathscr H}^{-1}f$. Then
$\|u\|_{\mathscr H}\le\|f\|_2/2$ and
$u=f+B_\alpha u$. The last term is in $L^2$, and
$$
 \|B_\alpha u\|_2
       \le \frac{A_0}{2}\|u\|_{\mathscr H}
       \le \frac{A_0}{4}\|f\|_2 .
$$
It follows that the same inverse is onto $L^2_0$ and
$$
 \|\mathcal A^{-1}\|_{L^2_0\to L^2_0}
          \le K_{A,0}:=1+\frac{A_0}{4}.
 \tag{WBN.23}
$$

For the negative window, same-sign compression has multiplier norm at most $W_{1/3}(\alpha)$ on $H^{-1/3}$. The exact primitive norm is
$\|I:H^{-4/3}\to H^{-1/3}\|=C_I$, and
$H^{-1/3}_0\hookrightarrow\mathscr H$ has norm at most one. Therefore
$$
 \|B_\alpha:H^{-4/3}_0\to\mathscr H\|
                 \le C_I A_{1/3}.
 \tag{WBN.24}
$$
One must not start by treating an arbitrary $H^{-4/3}$ input as an element of $\mathscr H$. Instead define, for such $f$,
$$
 \boxed{\quad
 \mathcal A^{-1}f
      :=f+\mathcal A_{\mathscr H}^{-1}B_\alpha f.
 \quad}
 \tag{WBN.25}
$$
The second term is in $\mathscr H$, so (WBN.19)--(WBN.20) give
$\mathcal A(\mathcal A^{-1}f)=f$ distributionally.
If $\mathcal Au=0$ in $H^{-4/3}_0$, then $u=B_\alpha u\in\mathscr H$, where injectivity has already been proved. This also proves the other inverse identity and compatibility with (WBN.23). Thus
$$
 \|\mathcal A^{-1}\|_{H^{-4/3}_0\to H^{-4/3}_0}
          \le K_{A,-}:=1+C_IA_{1/3}.
 \tag{WBN.26}
$$
The forward bounds are valid with the same majorants:
$$
 \|\mathcal A\|_0\le K_{A,0},\qquad
 \|\mathcal A\|_{-4/3}\le K_{A,-}.
 \tag{WBN.27}
$$
For the first, use $\|I\|_{L^2\to L^2}=1/4$. For the second, use (WBN.24) and $\mathscr H\hookrightarrow H^{-4/3}_0$. These estimates concern one distributional inverse and retain the real subspaces and all commutations in (WBN.16).

An optional full scalar extension is $\widehat{\mathcal A}=\Pi+\mathcal AP$, with inverse $\Pi+\mathcal A^{-1}P$. It is a declared identity on the auxiliary scalar mean; the proof on $\mathscr H$ never assigns a positive primitive norm to a constant. Neither physical mean port is eliminated by this extension.

## WBN7. The exact discarded sign blocks include a real output-mean rank

The relation between the same-sign source operator and full multiplication is
$$
 F_\alpha=M_\alpha I-\mathcal T_\alpha I.
$$
On nonmean input there is the exact identity
$$
 \boxed{\quad
 F_\alpha
    =\Pi M_\alpha I+
        \frac12 Z_0[M_\alpha I,Z_{\rm full}].
 \quad}
 \tag{WBN.28}
$$
For nonzero input index $k$ and nonzero output index $j$, the second term has multiplier factor
$\tfrac12 z_j(z_k-z_j)$, equal to zero on equal signs and one on opposite signs. At output index zero, $Z_0$ vanishes and the first term supplies the full missing row. The constant input column is zero because $I1=0$.

In particular the output-mean row $\Pi M_\alpha I$ cannot be removed merely because $\Pi\alpha=0$. By duality and the same physical primitive norm,
$$
 \|\Pi M_\alpha I:H^{-4/3}\to\mathbb C\|
   =\|I\alpha\|_{H^{4/3}}
   \le C_I\|\alpha\|_{H^{1/3}}
   \le C_IA_{1/3}.
 \tag{WBN.29}
$$
The complete MS.25 commutator, including its nonzero-to-mean row, gives
$$
 \|[M_\alpha I,Z_{\rm full}]:H^{-4/3}\to L^2\|
                    \le\frac{17}{8}A_{1/3}.
$$
Combining these two full bounds yields
$$
 \boxed{\quad
 \|F_\alpha:H^{-4/3}\to L^2\|
       \le C_F:=
          \left(C_I+\frac{17}{16}\right)A_{1/3}.
 \quad}
 \tag{WBN.30}
$$
This is a positive whole bound, not a cancellation between independently evaluated upper estimates.

## WBN8. The variable first coefficient cancels in the actual order

Put
$$
 T_i=Id+M_{c_i}I,\qquad T_\nu=Id+\nu I .
$$
Since $c_i-\alpha=\nu+w$, expansion without commuting a multiplier through a primitive gives
$$
 \boxed{\quad
 T_i\mathcal A=N T_\nu+\mathcal R_{\rm alg},
 \quad}
$$
$$
 \mathcal R_{\rm alg}
   =-M_{c_i}IM_\alpha I-\nu M_wI^2+T_iF_\alpha .
 \tag{WBN.31}
$$
Every term displayed is retained. In particular (WBN.28)'s output-mean row passes through the full $T_i$; no zero-mode simplification is inserted into (WBN.31).

Let
$$
 C_i^\infty\ge\|c_i\|_\infty,\qquad
 W_0\ge\|w\|_\infty,\qquad
 K_{i,0}^{\rm fwd}=1+\frac{C_i^\infty}{4},\qquad
 a_I=\frac{17^{2/3}}{16}.
 \tag{WBN.32}
$$
The quantity $K_{i,0}^{\rm fwd}$ bounds the forward $T_i$ on $L^2$; it is not its inverse. The two ordered primitive norms are
$$
 \|I:H^{-4/3}\to H^{-1/3}\|\,
 \|I:H^{-1/3}\to L^2\|
 =\frac{\sqrt{17}}4\frac{17^{1/6}}4
 =a_I=\|I^2:H^{-4/3}\to L^2\|.
$$
Therefore the complete new algebraic error has the symbolic bound
$$
 \boxed{\quad
 \|\mathcal R_{\rm alg}:H^{-4/3}_0\to L^2\|
 \le C_{\rm alg}
 :=a_I\bigl(C_i^\infty A_{1/3}+|\nu|W_0\bigr)
                   +K_{i,0}^{\rm fwd}C_F .
 \quad}
 \tag{WBN.33}
$$
The first product pays the $\alpha$ multiplier on $H^{-1/3}$, between the two primitives. The second uses the complete $I^2$ norm. The third pays $T_i$ on the output $L^2$ window. Mean terms created by the intermediate multiplier remain included.

Since $N_\perp$ commutes with the target reflection, (WBN.31) also gives the exact two-space identity
$$
 N_\perp^{-1}Q_aT_i\mathcal A
       =\left.\Pi_a^+T_\nu\right|_{H^s_0}
          +N_\perp^{-1}Q_a\mathcal R_{\rm alg},
 \qquad \Pi_a^+=\frac{Id+R_a}{2}.
 \tag{WBN.34}
$$
Here $PN T_\nu=N_\perp T_\nu$ on nonmean input. Thus the target inverse acts after the exact projection in its correct space. Formula (WBN.34) does not restrict $T_i$ or its full-circle inverse to an unproved same-source endomorphism.

## WBN9. The true input intertwiner and the complete physical row

Retain WIT's exact operator $\mathcal W$ and actual source projection:
$$
 \widehat P_{97}
       =\mathcal W\mathcal S P_{97}\mathcal S^{-1}\mathcal W^{-1},
 \qquad
 \mathcal W X_s^{\rm fr}
       =\operatorname{ran}(\widehat P_{97})\cap X_b^s.
 \tag{WBN.35}
$$
Let $C_\Delta$ be the already certified complete DZA bound for
$\Delta_{\rm full}=\mathcal S Z_{\rm full}\mathcal S^{-1}-Z_{\rm full}$.
It includes its independent input-mean rank. WIT gives
$$
 K_W=1+\frac{C_\Delta}{2},\qquad
 \|\mathcal W^{\pm1}\|_{0},\
 \|\mathcal W^{\pm1}\|_{-4/3}\le K_W,
$$
$$
 \|\mathcal W^{-1}-Id:H^{-4/3}_0\to L^2_0\|
          \le C_{W-Id}:=K_W\frac{C_\Delta}{2}.
 \tag{WBN.36}
$$
The old $C_\Delta$ is read as a complete bound, not extracted from a smaller outgoing subtotal. No product in (WBN.36) is numerically evaluated here.

For the actual homogeneous terminal-Ai column, WPL identifies the normalized physical primitive row as
$$
 \mathcal B_\partial
   :=\frac{\mathfrak W_\partial}{2\kappa}
   =\left.Q_aT_i\right|_{X^{\rm fr}}
                        +E_\partial^{\rm fr}.
 \tag{WBN.37}
$$
Its complete strong error is explicitly
$$
 E_\partial^{\rm fr}
   =Q_aV_wT_i-(h_H-1)\otimes\rho_i
             +Q_a(Id+V_w)P_{h_H}E_i^{\rm fr},
$$
$$
 h_H=U_{\mathcal H^{-1}}1,\qquad
 P_{h_H}=Id-h_H\Pi,\qquad
 \rho_i=\Pi T_i|_{X^{\rm fr}}.
 \tag{WBN.38}
$$
The exact $V_w$ contains the true second waist normalizer and both density changes. Its input cutoff is the original $J_s$, not 97. The coefficient identity $\mathbf S(0)=0$ removes only the first waist normalizer. It does not remove $V_w$, $\rho_i$, or the complete WRA error $E_i^{\rm fr}$.

Suppose a complete admitted bound is supplied for this exact operator:
$$
 \|E_\partial^{\rm fr}:
       X_{-4/3}^{\rm fr}\to Y_a^0\|\le C_\partial .
 \tag{WBN.39}
$$
This is a whole physical-row hypothesis. An old state subtotal or incoming subtotal alone is not $C_\partial$. WPL supplies the explicit three-term positive expression that can be used when all of its factors are admitted. This lemma does not assign a numerical value to it.

Use the exact new source and target changes
$$
 x=\mathcal W^{-1}\mathcal A\xi,\qquad
 \widetilde{\mathcal B}
       =N_\perp^{-1}\mathcal B_\partial\mathcal W^{-1}\mathcal A .
$$
On its true source subspace, the complete identity is
$$
 \boxed{\quad
 \widetilde{\mathcal B}
       =\Pi_a^+T_\nu+\widetilde E,
 \quad}
$$
$$
 \begin{aligned}
 \widetilde E=N_\perp^{-1}\bigl[
   &Q_a\mathcal R_{\rm alg}\\
   &+Q_aT_i(\mathcal W^{-1}-Id)\mathcal A\\
   &+E_\partial^{\rm fr}\mathcal W^{-1}\mathcal A
                         \bigr].
 \end{aligned}
 \tag{WBN.40}
$$
The leading and the complete physical error have both been transformed. In particular $\mathcal W^{-1}$ was not silently commuted through $T_i$ or dropped from its leading term; its entire strong difference is the second line.

The source forward $\mathcal A$ is paid on $H^{-4/3}$, the target inverse on $L^2$. Equations (WBN.13), (WBN.26)--(WBN.27), (WBN.33) and (WBN.36) give
$$
 \boxed{\quad
 \|\widetilde E\|_{H^{-4/3}\to L^2}
 \le C_{\rm two}
 :=K_{N,0}
   \left[
    C_{\rm alg}
    +K_{i,0}^{\rm fwd}C_{W-Id}K_{A,-}
    +C_\partial K_W K_{A,-}
   \right].
 \quad}
 \tag{WBN.41}
$$
Each term is a complete positive majorant for the corresponding ordered operator in (WBN.40). The domain of $E_\partial^{\rm fr}$ in its last line is respected by the source condition below; an arbitrary full-circle extension of that error is not needed or asserted.

The identities hold first on qualified smooth inputs and then distributionally in the stated windows. The leading $\Pi_a^+T_\nu$ is an order-zero map. The fact that $\widetilde E$ lands in $L^2$ does not assert that the entire row sends every $H^{-4/3}$ input to $L^2$.

## WBN10. The actual cutoff is transported again

The exact source of (WBN.40) is
$$
 \widetilde X_s
  =\{\xi\in X_b^s:
           \mathcal W^{-1}\mathcal A\xi\in X_s^{\rm fr}\}
  =\operatorname{ran}(\widetilde P_{97})\cap X_b^s,
$$
$$
 \boxed{\quad
 \widetilde P_{97}
       =\mathcal A^{-1}\widehat P_{97}\mathcal A .
 \quad}
 \tag{WBN.42}
$$
The equality uses the exact invariance of $X_b^s$ under $\mathcal A^{\pm1}$, proved above. It is not a Fourier-band claim.

With $C=\mathcal W\mathcal S$, the complete complement on the nonmean carrier is
$$
 Id-\widetilde P_{97}
       =\mathcal A^{-1}C(Id-P_{97})C^{-1}\mathcal A .
 \tag{WBN.43}
$$
It has rank 192 on the full complex nonmean carrier and rank 96 on the reflected complex subspace; the corresponding real forms have the same respective real dimensions. This is a statement of finite rank under actual bounded coordinate changes, not a computation of the finite matrix or its inverse.

The projection is idempotent and compatible with both stated Sobolev windows, but is not declared orthogonal. It commutes with $Z$, $R_b$ and $K_b$ because $\widehat P_{97}$ and $\mathcal A^{\pm1}$ do. The corresponding property of $\widehat P_{97}$ follows from WIT's exact intertwining by $C$, not from a false assertion that $C$ commutes with $R_b$. Neither $\mathcal A$ nor $C$ is asserted to commute with ordinary $P_{97}$ or another Fourier cutoff. Thus $\widetilde P_{97}$ must not be replaced by an ordinary projector in an actual high test.

An endpoint finite map remains finite after these bounded changes. Its actual columns, dual rows and inherited weights remain required. A radially varying family of finite-rank maps already inside the whole physical error is not moved into a single finite block by this result.

Likewise, although $N_\perp$ preserves the reflected target, it need not commute with an ordinary Fourier cutoff. Any later source/target high-low decomposition retains the genuine cross maps produced by the chosen projections. No old finite row is set to zero.

## WBN11. What is now reduced to the constant model

On ordinary model spaces $P_JX_b^s$ and $P_JY_a^s$, the leading $\Pi_a^+T_\nu$ has the exact reflection-line blocks of WCS. For the actual identified $\nu=\nu_i$, its one-derivative-loss inverse can use the already completed Cayley certificate. That scalar result is not an inverse of an arbitrary same-order reflected square.

To combine it with (WBN.40), one must first realize the actual finite complement (WBN.43), the true ordinary high cross maps, and a complete error bound on the exact proposed source and target. The appropriate $L^2$ graph domain and right-preconditioned target operator are the ones in WCS. A same-order inverse is not inferred from the present two-window bounds for the coordinate changes.

All independent source columns are left-transformed by the target inverse in this same normalized physical-row realization. Returning to the original physical row also retains its nonunit factor $2\kappa$ and every preceding row conversion. Every independently retained input row is right-transformed by $\mathcal W^{-1}\mathcal A$, with its actual dual norm. The original scalar mean row of $N$, its two weighted mean conditions, the full $K_H=R_a-2h_H\Pi$ relation, the actual physical mean entries and independent mean/amplitude/outer/metric-parameter equations remain present. The present normalization solves none of those equations.

The new unconditional results are the cohomological parities, the exact target compression with its retained mean block, and the bounded real source isomorphism with no smallness condition. The complete physical conclusion is the ordered identity (WBN.40) and the conditional positive bound (WBN.41), subject to (WBN.39) and the exact retained source. No actual high cutoff or finite matching inverse is certified here.

## WBN12. Exact inputs and the boundary of any later scalar readout

The proof needs no new scientific execution. A later authorized scalar consumer may read complete already saved bounds for $v_i,w,\nu$, the same NPK inverse, the complete DZA $C_\Delta$, and every factor of the actual WPL physical error. It must distinguish a bound for the full $c_i$ from a bound for its zero-mean part.

For instance, with $V_i\ge\|v_i\|_\infty$ and
$B_i\ge W_{1/3}(v_i)$, one may define the complete positive majorants
$$
 A_0:=V_i+W_0,\qquad
 A_{1/3}:=B_i+W_{1/3},\qquad
 C_i^\infty:=|\nu|+V_i .
$$
These are full-function estimates; no subtraction of upper bounds is allowed. Any sharper complete candidate must have the same coefficient, window and scope.

Only the new positive products of (WBN.23), (WBN.26), (WBN.30), (WBN.33), (WBN.36) and (WBN.41) would be new scalar targets. Old Fourier budgets, cohomology, exponential, two-window N inverses, full sign differences and physical source budgets are frozen. Every complete candidate must be saved before any whole-candidate comparison. There is no numerical value, new gate verdict, or source invocation in this document.

The mathematical primary identities are:

| Primary and role | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WPL: complete coefficient reflection and actual physical primitive row | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |
| RRF: true target and transported source reflections | cdb4b957f6976c7b72e974fcccc8f2a15afbee74 | 15266 | 803302f2924da51022e2aa16a36c928ee0789fde93277f5ea9fd9c2ae2a3630f |
| WIT: the positive density intertwiner and its same two-window inverse | 68737e28209551cab5b45aa251869892bc51b380 | 21308 | 13c5972c82dd1af1ded73ccdfdd6b8ba69da3c3a84bb278aea602d3dd90ba437 |
| CN: the original complete normalizer, cohomology and both weighted means | df47da70f4831a651f99628b914e4be99d88da12 | 15615 | 427387a2f3836d95b5f79546f0c6d41e8d6307abbb76611073d2801364fda9db |
| NW: same actual coefficients and complete norm/log distinction | dbe97d3caa9e61b557ef22ac2b0f4606f6cfc27f | 19754 | 1469fdd05417284743e7857aabe0324ee67ccb1b7dbaa003461364d8c9447938 |
| NPK: complete inverse refinement and whole-window selection | 0cfdef792fbaf5eff1b6e3d49d404aab9bb0c135 | 11251 | 1ab985bcc97d40c63ab7ea0163746256cf9edc3d79233d990ca0189fa39b57b9 |
| MS.25--27: the complete sign commutator including mean output | 10fdaddc0114e25ad349f1f411e80baf4f98fe26 | 19522 | 44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161 |
| DZA actual complete $Z^{\mathcal S}-Z$ scalar conclusion | 67b41ac717207f8696b637c667fb210088fca638 | 26909 | 05036749a28c55499e2ed6fe47019cd31f4438652e3e6ab1319e6f9f2f2c4dba |
| WCS: exact constant-mean model, graph domain and ordered high gate | 4215c33aaec529176b1f8021904fd5f1e173e2fa | 12818 | 4998ef8208e3dc9e5474fe456bed53ebf4e7d987f7684d888f6705c9f1f55d0a |

WPL and WCS are the independently reviewed immutable manuscripts named in this table; their publication identity may be recorded separately without changing these formulas. The DZA scalar source is the complete small scientific conclusion from its unique successful run. No binary, old producer, numerical function, or actual input ball has been reevaluated to establish this lemma.
