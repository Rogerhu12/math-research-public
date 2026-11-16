# WCTR. A clipped scalar trace, matrix normalizers, and complete two-direction paired circuits

**Proved here:** an exact reference theorem and a complete candidate specification on the already fixed actual spaces. This document reports no new numerical run and assigns no successful finite inverse. The first WVC calculation, its sources, and all its completed or running targets remain separate.

The point of this continuation is to retain a controlled part of the signed sum of the two modal diagonal entries. The existing WVC reference retains their difference. Adding their sum changes both propagation directions and makes the cell normalizer a matrix. Every one of those changes is included below; an old reference norm is never transferred by its name.

The topic prefix for the primary references is topics/visible-flex-exact-nearby/.

## WCTR1. Fixed actual problem and exact reference definition

Keep the WVC actual operator
$\mathcal A=\left(\begin{smallmatrix}A&B\\C&R\end{smallmatrix}\right)$,
its ordinary-$dr$ spaces, the original $153$ parents and their $160$ inherited children, the cell projections, the actual $S_i$, the root complement of dimension $97$, the prescribed root-even data of dimension $96$, and the outer chart of dimension $96$. The total finite dimension is still $193N+193$, with $N=24480$. The independent physical mean is one real coordinate.

In each nonzero mode the raw pair is $(\xi,\zeta)$ in the original normalized real sine/cosine basis. Its nonzero Fourier functions have the original $\sqrt2$ normalization. On one cell,

$$
 S=\operatorname{diag}(1,q),\qquad
 D_a=\begin{pmatrix}a&cq^2\\c&-a\end{pmatrix},
 \quad c=4j\widehat\eta,\quad 1\le j\le96 .
 \tag{WCTR.1}
$$

Use exactly the WVC definitions of $a,c,q$, including its rational diagonal clip:

$$
 c\ge0,\quad q\ge\tfrac18,\quad
 -\tfrac c{32}\le a\le\tfrac c{16}.
 \tag{WCTR.2}
$$

Let $d_o,d_e$ be the complete signed same-mode diagonal entries of the same frozen degree-$32$ reference packet used by WVC. They include the ordered primitive terms, the original repaired-centre scaling, and the real-basis normalization. Define

$$
 \widehat r=\tfrac12(d_o+d_e),\qquad
 r=\max\{-c/64,\min\{\widehat r,c/64\}\},
 \qquad D=rI+D_a .
 \tag{WCTR.3}
$$

These are exact rational reference definitions, not certified actual point values and not differences of independent norm bounds. On the root parent, set $a=c=r=0$. The physical-mean reference remains zero. Its actual row and all its couplings remain in the residual.

Every child inherits the exact parent $a,c,q,r$. This changes the finite reference and the associated trial maps, not the actual operator, the actual high space, or the projection. Raw states are matched across reference interfaces. If adjacent $S_i$ differ, transformed states have the corresponding complete $S_{i+1}S_i^{-1}$ matching; they are not silently identified.

The existing actual tail conclusion remains

$$
                         R^{-1}\text{ exists},\qquad \|R^{-1}\|\le3 .
 \tag{WCTR.4}
$$

This is the WIC result for the fixed actual tail. It does not assert the same actual contraction with a newly substituted tail preconditioner.

## WCTR2. Continuous impedance and the two distinct rates

Put $g=\xi+p\zeta$. For the reference equation $x'=Dx+f$, the backward impedance and the forward auxiliary function satisfy

$$
 \begin{split}
 p'&=cp^2+2ap-cq^2,\qquad p(R)=p_R=\tfrac{13}{80},\\
 H'&=c-2(a+cp)H,\qquad H(r_*)=0,\qquad K=1-pH .
 \end{split}
 \tag{WCTR.5}
$$

The scalar trace cancels from both equations. At $p_*=1/16$ the same inward barrier as WVC gives

$$
 -p'\big|_{p_*}=c(q^2-p_*^2)-2ap_*\ge c/256 .
 \tag{WCTR.6}
$$

The upper Riccati barrier is also finite on a finite collection of constant cells: on each such cell take the positive zero
$-a/c+\sqrt{(a/c)^2+q^2}$ when $c>0$, together with the incoming value; backward propagation stays between them. When $c=0$, (2)--(3) give $a=r=0$ and $p$ is constant. This proves a complete finite positive impedance without a Riccati blow-up. Raw identity interfaces preserve the same $p$.

As before,

$$
 p\ge\tfrac1{16},\qquad
 K'=\frac{cq^2}{p}-c\left(p+\frac{q^2}{p}\right)K,\qquad
 0\le K\le1,\qquad 0\le H\le1/p\le16 .
 \tag{WCTR.7}
$$

Write $\kappa=a+cp$. The two homogeneous scalar equations are now different:

$$
 g'=(\kappa+r)g,\qquad
 y'=-(\kappa-r)y,\qquad y=\zeta-Hg .
 \tag{WCTR.8}
$$

Both directions have a nonnegative lower rate, with their complete signs retained:

$$
 \kappa\ge c/32,\qquad
 \kappa+r\ge c/64,\qquad
 \kappa-r\ge c/64 .
 \tag{WCTR.9}
$$

The backward $g$ factor uses $\kappa+r$; the forward $y$ factor uses $\kappa-r$. One factor is not copied to the other. The root cell has zero rate and the exact constant propagation limit.

No assertion of coercivity for the actual operator follows. All actual lower-order, mean, off-mode, and high-feedback terms remain.

## WCTR3. Complete signed continuous Green kernel

Define the signed columns and rows

$$
 F=\binom{-p}{1},\qquad U=\binom{K}{H},\qquad
 L=(1,p),\qquad J=(-H,K).
 \tag{WCTR.10}
$$

They satisfy the exact local identity $FJ+UL=I$. For $s\le t$ set

$$
 E_-(s,t)=\exp\!\left(-\int_s^t(\kappa-r)\,du\right),\qquad
 E_+(s,t)=\exp\!\left(-\int_s^t(\kappa+r)\,du\right).
 \tag{WCTR.11}
$$

For homogeneous root-even and outer Robin data the full Green kernel is

$$
 G_D(t,s)=
 \begin{cases}
 F(t)E_-(s,t)J(s),&s<t,\\
 -U(t)E_+(t,s)L(s),&s>t.
 \end{cases}
 \tag{WCTR.12}
$$

For general reference endpoint data $\zeta(r_*)=z_*$ and
$g(R)=g_R$, the two additional terms are

$$
 F(t)E_-(r_*,t)z_*+U(t)E_+(t,R)g_R .
 \tag{WCTR.13}
$$

Indeed the full inhomogeneous scalar equations are
$g'=(\kappa+r)g+Lf$ and $y'=-(\kappa-r)y+Jf$.
Integrating them in their respective directions gives (12)--(13).
The jump of the kernel across its diagonal is exactly $FJ+UL=I$.
No part of the multiplication identity is estimated separately before it has been formed.

Across a piecewise-constant reference seam, $p,H$, the raw Green state, and the accumulated propagators are transmitted without a reset. A seam of the actual system is still subject to its original matching. All independent affine jumps and all original boundary data remain in the actual residual statement.

The complete source and target weights are the same as WPS/WVC: actual $S$, the ordinary-$dr$ normalization, the declared angular Sobolev weights, the root odd row, and the outer factor
$\theta_j=(1+16j^2)^{-5/12}$. The physical mean has its separate scalar branch and no additional $\sqrt2$.

The adjoint computation is the transpose of this same weighted two-triangle kernel, including both endpoint atoms and all direct local terms. It is not obtained by reversing one of the two rates while retaining the other's coefficients.

## WCTR4. The already paid spectral range

WVC5 uses the exact definition of the completed original record
complete_reference_Z_squared_upper, not merely its interpretation as an operator norm. That record dominates every
$\min\{x_0^2/12,x_0/2\}$ and is strictly below $1/3$, where $x_0=hcq$. Consequently $x_0<2$.

Let $\Omega^2=a^2+c^2q^2$. WVC10 gives

$$
 h^2\Omega^2\le\tfrac54h^2c^2q^2<5 .
 \tag{WCTR.14}
$$

For $c>0$, $\Omega\ge cq\ge c/8$, so the new trace clip implies

$$
 |r|\le\Omega/8,\qquad
 \lambda_\pm=r\pm\Omega,\qquad
 h^2\lambda_\pm^2<\frac{405}{64}<7 .
 \tag{WCTR.15}
$$

The eigenvalues have opposite signs. At $c=0$ all of $a,r,\Omega,\lambda_\pm$ vanish, and every subsequent expression is read through its stated exact zero limit.

These are consequences of a completed producer and exact inequalities. They do not evaluate a new numerical target, repeat either old $m=1,2$ test, or infer a spectral range from an arbitrary inverse-norm upper bound.

## WCTR5. Matrix normalizer and its physical-coordinate inverse

The selfadjoint representative of the raw modal reference is

$$
 SDS^{-1}=rI+\begin{pmatrix}a&cq\\cq&-a\end{pmatrix}.
 \tag{WCTR.16}
$$

Its quadratic Padé normalizer is a matrix:

$$
 \begin{split}
 P&=I+\frac{h^2D^2}{12}=\alpha I+\beta D_a,\\
 \alpha&=1+\frac{h^2(r^2+\Omega^2)}{12},\qquad
 \beta=\frac{h^2r}{6},\\
 \det P&=\alpha^2-\beta^2\Omega^2
       =\left(1+\frac{h^2(r+\Omega)^2}{12}\right)
        \left(1+\frac{h^2(r-\Omega)^2}{12}\right)\ge1,\\
 P^{-1}&=\frac{\alpha I-\beta D_a}{\alpha^2-\beta^2\Omega^2}.
 \end{split}
 \tag{WCTR.17}
$$

Thus $SP^{-1}S^{-1}$ is positive definite and has operator norm at most one. Its off-diagonal entries are signed; they are not replaced by a scalar division. The actual body output factor is

$$
 \sqrt h\,SP^{-1},
 \quad\hbox{acting after the complete raw local sum};
 \qquad
 r_f^{\rm finite}=S^{-1}u_f/\sqrt h
 \tag{WCTR.18}
$$

for the finite input coordinate $u_f$. In particular neither $S$ nor $P^{-1}$ is moved through an unrelated angular multiplication or through an interface.

The mean coordinate has $D=0$, $P=1$, and the same independent old scalar shear. Formula (17) is exact rational arithmetic for the reference definitions; no eigensystem is required for its implementation.

## WCTR6. Positive Padé transfer and both discrete propagation factors

Set

$$
 T=(P-\tfrac h2D)^{-1}(P+\tfrac h2D).
 \tag{WCTR.19}
$$

For every real $z$,
$1-z/2+z^2/12=(z-3)^2/12+1/4>0$.
Hence (19) has no singular real spectral denominator. Its scalar eigenvalue function is

$$
 R_2(z)=\frac{1+z/2+z^2/12}{1-z/2+z^2/12}>0 .
 \tag{WCTR.20}
$$

For $\Omega>0$ write $T=A I+B D_a$, with

$$
 A=\frac{R_2(h\lambda_+)+R_2(h\lambda_-)}2,\qquad
 B=\frac{R_2(h\lambda_+)-R_2(h\lambda_-)}{2\Omega}>0 .
 \tag{WCTR.21}
$$

The strict positivity of $B$ follows already from
$h\lambda_+>0>h\lambda_-$: $R_2(z)>1$ for $z>0$ and is below one for $z<0$.
The diagonal entries of $T$ are convex combinations of its positive eigenvalues, since $|a|\le\Omega$.
Its off-diagonal entries are nonnegative and its determinant $\delta_T$ is positive. The determinant generally differs from one.

For the next impedance $p_+\ge p_*$ put

$$
 d=t_{11}+p_+t_{21},\quad
 p=\frac{t_{12}+p_+t_{22}}d,\quad
 \tau_b=\frac1d,\quad
 \tau_f=\frac{\delta_T}{d},\quad
 \sigma=\frac{t_{21}}d .
 \tag{WCTR.22}
$$

The Möbius derivative is $\delta_T/d^2>0$, and at $p_*$,

$$
 t_{12}+p_*t_{22}-p_*(t_{11}+p_*t_{21})
       =B(cq^2-2ap_*-cp_*^2)\ge Bc/256 .
 \tag{WCTR.23}
$$

This proves the same positive lower impedance at every discrete cell.

Both propagation factors in (22) are at most one. Here is the complete spectral proof, which is not a determinant-one argument. Let
$\varphi(z)=\log R_2(z)$. On $z^2\le7$,

$$
 \varphi'(z)=\frac{1-z^2/12}{1-z^2/12+z^4/144},
 \qquad \frac12\le\varphi'(z)\le1 .
 \tag{WCTR.24}
$$

For the lower inequality, with $u=z^2\le7$,
$u^2+12u\le133<144$.
Write

$$
 s=\tfrac12[\varphi(h\lambda_+)+\varphi(h\lambda_-)],
 \qquad
 t=\tfrac12[\varphi(h\lambda_+)-\varphi(h\lambda_-)]>0 .
 \tag{WCTR.25}
$$

Oddness of $\varphi$ and (24) give $|s|\le h|r|$ and $t\ge h\Omega/2$.
Thus for $\mu=(a+cp_+)/\Omega\ge0$,

$$
 \frac{|s|}{t}\le\frac{2|r|}{\Omega}\le\mu .
 \tag{WCTR.26}
$$

Also $|s|<t$, since the two eigenvalues have opposite signs.
Now
$d=e^s(\cosh t+\mu\sinh t)$ and $\delta_T=e^{2s}$.
If $0\le\mu\le1$, Jensen's inequality applied to the two positive weights
$(1+\mu)/2$ and $(1-\mu)/2$ yields
$\cosh t+\mu\sinh t\ge e^{\mu t}\ge e^{|s|}$.
If $\mu>1$, the left side is at least $e^t\ge e^{|s|}$.
Consequently

$$
 d\ge\max\{1,\delta_T\},\qquad
                  0<\tau_b\le1,\quad0<\tau_f\le1 .
 \tag{WCTR.27}
$$

The logarithms in this proof establish inequalities. A numerical implementation of (19), (22) and (17) needs only exact rational matrix expressions and directed arithmetic; it need not evaluate (25).

The correct forward recurrence is

$$
 H_+=\tau_f\tau_b H+\sigma .
 \tag{WCTR.28}
$$

Its invariant obeys the exact formula

$$
 K_+=1-p_+H_+
     =\frac{t_{12}}{dp}
       +\frac{p_+\delta_T}{d^2p}K .
 \tag{WCTR.29}
$$

All coefficients are nonnegative and their sum is
$1-p_+t_{21}/d\le1$. Therefore $H\ge0$ and $0\le K\le1$ are retained.
At the root $T=P=I$, $\tau_b=\tau_f=1$, and $\sigma=0$.
There is no division by either propagation factor.

## WCTR7. Complete finite action and ordinary-source pair

For an ordinary source $f$ on a child, keep both complete moments

$$
 G=\int_0^h f(s)\,ds,\qquad
 m_f=\int_0^h(1/2-s/h)f(s)\,ds .
 \tag{WCTR.30}
$$

Their scalar norms are $\sqrt h$ and $\sqrt{h/12}$ and their kernels are orthogonal in ordinary $L^2$. The physical mean uses the same two scalar moments.

For finite residual datum $b_f$, the exact raw cell equations are

$$
 x_+-x=hDv+G,\qquad
 Pv=\tfrac12(x+x_+)+b_f+m_f .
 \tag{WCTR.31}
$$

They imply

$$
 x_+=Tx+u,\qquad
 u=(T-I)(b_f+m_f)+\tfrac12(T+I)G .
 \tag{WCTR.32}
$$

This follows by multiplying (31) by $P-hD/2$; $P$ commutes with $D$ because it is its polynomial. No arbitrary ordinary source is replaced by a cellconstant source.

Put

$$
 u_g=-\frac{u_o+p_+u_e}{d},\qquad
 u_y=\frac{t_{11}u_e-t_{21}u_o}{d}.
 \tag{WCTR.33}
$$

The complete recurrences are

$$
 \begin{split}
 g&=\tau_b g_++u_g,\\
 y_+&=\tau_f y+\tau_f H u_g+u_y,\qquad
 x=Ug+Fy .
 \end{split}
 \tag{WCTR.34}
$$

The two factors have different locations and must not be interchanged.
For the finite action set $G=m_f=0$, and form the signed rows
$u_g=b_i b_f$ and $\tau_f H u_g+u_y=f_i b_f$.
Before multiplication by $P^{-1}$ the three complete local output blocks are

$$
 \begin{split}
 F_i^{\rm out}&=\tfrac12(F_i+\tau_{f,i}F_{i+1}),\\
 U_i^{\rm out}&=\tfrac12(\tau_{b,i}U_i+U_{i+1}),\\
 D_i^{\rm out}&=I+\tfrac12(U_i b_i+F_{i+1}f_i).
 \end{split}
 \tag{WCTR.35}
$$

After this full signed sum, apply the exact output factor (18). The input factors remain $S_i^{-1}/\sqrt{h_i}$. The terminal datum is still
$g_N=g_o+p_Rg_e$, the root-even datum is supplied through the original right side, the root odd output is $g_0$ when that prescribed datum is zero, and the weighted outer output is
$\theta_j(y_N+H_Ng_N-g_e)$.
Both direct terminal paths are present. The complete physical-mean shear is unchanged.

The independent endpoint input is not removed by the paired $-\int f$ term. That term cancels only in the exact same ordinary-source pair for which (30)--(32) were derived.

Equations (17), (19), (22), (28), and (32)--(35) give a streaming action with one backward and one forward scalar channel per mode. Each off-diagonal radial block still has rank at most one. Local blocks are full signed two-by-two matrices, or full two-by-four blocks for the two ordinary-source moments.

The transpose reverses this entire weighted graph. It includes $P^{-T}$ in the correct raw dual position, both endpoint paths, and the actual $S_i$ and $\sqrt h$ factors. It is not the old scalar-$\rho$ transpose with a diagonal replacement.

## WCTR8. New whole norm and normalizer targets

Form a positive majorant only after each full signed local block in (35) and (18) has been multiplied and combined. For positive input and output comparison weights $\upsilon,\varpi$, compute the whole row and column quantities on that same graph:

$$
 R_w=\sup \frac{M\upsilon}{\varpi},\qquad
 C_w=\sup \frac{M^T\varpi}{\upsilon},\qquad
                      \|Q_D\|\le\sqrt{R_wC_w}.
 \tag{WCTR.36}
$$

The finite endpoint coordinates belong to both computations. The modes form an orthogonal direct sum in the actual Hilbert coordinates, so the complete modal bound is a maximum over modes, not that maximum multiplied by $\sqrt{96}$. The independent mean is combined using its unchanged exact complete norm.

For the continuous kernels (12)--(13), use the same weighted Schur construction on ordinary $dr$ together with the actual finite endpoint atoms. Both triangles have their respective rates. Multiplication terms are included before the row and column bounds are combined. The reverse sweep is the transpose of the same full positive kernel and atoms, not a different comparison equation.

On a constant comparison cell, directed scalar comparison may bound the endpoint propagation and the complete within-cell supremum for each rate in (11). A nonnegative source envelope yields a monotone constant-source comparison solution, whose supremum is attained at one of its two endpoints. This does not claim that the actual variable-source solution is monotone. The zero-rate branch uses its exact integral length. Lower endpoints are used for decay rates and upper endpoints for interval lengths where required. Both rate legs and all actual weights are paid.

The exact principal mean-zero cell elimination has spectral normalizer
$\rho_*(z)=(z/2)\coth(z/2)$, continuously equal to one at zero.
Since the reference is selfadjoint in the fixed cell $S$ coordinates, the WIC scalar spectral inequalities apply to its two real eigenvalues:

$$
 \begin{split}
 0&\preceq_S P-\rho_*(hD),\\
 \|P-\rho_*(hD)\|_S
   &\le \min\{\bar x^2/12,\bar x^4/720\},\qquad
     \bar x^2=\tfrac{81}{64}h^2\Omega^2,\\
 \|Z_D\|^2&<\frac{135}{256},\qquad
       \|(I,-Z_D)\|<\sqrt{\frac{391}{256}}<\frac54 .
 \end{split}
 \tag{WCTR.37}
$$

The matrix difference is not evaluated by subtracting independent upper bounds. Its exact definition or the complete spectral enclosure is used. If a scalar envelope $d_i$ from (37) is used, write the whole block difference as $d_i V_i$ with $\|V_i\|_S\le1$. This justifies bounding $Q_D\operatorname{diag}(d_i I,0_{\rm endpoints})$ by its own complete circuit and transpose. It does not justify inserting only a diagonal entry of the matrix difference.

The new whole normalizer target is
$\|Q_D(P-\rho_*(hD))\|$.
The old reference inverse near $61.96$, the old defect near $0.071$, and any later WVC result are not new values for it. The new odd-endpoint receiver is likewise computed on the new full action. The physical-mean receiver is unchanged and may be copied with its exact original scope.

## WCTR9. Actual residual and complete reception

Use the same continuous repaired-centre high trial as WVC,

$$
 \widehat{\mathcal P}_c=\chi G_{D_H}\chi B_{HL,c}.
 \tag{WCTR.38}
$$

The high principal $D_H$ is unchanged. The complete high residual remains exactly

$$
 \begin{split}
 L_H\widehat{\mathcal P}_c-B_{HL}
 ={}&(\chi^2-I)B_{HL,c}-\Delta B_{HL}\\
 &+[\chi'I-\chi(A_{HH,c}-D_H)]G_{D_H}\chi B_{HL,c}\\
 &-\chi\Delta A_{HH}G_{D_H}\chi B_{HL,c}.
 \end{split}
 \tag{WCTR.39}
$$

This identity uses the source equation for $G_{D_H}$ before taking norms and does not require $B_{HL,c}'$. Full degree-$96$ differences retain their complete output norm; they are not projected into the degree-$32$ centre trial band.

The low centre residual changes to

$$
 \widehat\Gamma_D=(A_{L,c}-D)a+B_{LH,c}\widehat{\mathcal P}_c a .
 \tag{WCTR.40}
$$

Its diagonal difference is formed from signed coefficient enclosures and the exact reference (3). One does not subtract the new trace from an old positive norm bound.

Let $G_{f,D}=P_fG_D$. The complete family and actual high-error reception is the same ordered expression as WVC40, with every low receiver replaced by this same $G_{f,D}$:

$$
 \begin{split}
 \varepsilon_H\ge{}&
 \|G_{f,D}\Delta A_LS^{-1}\|
 +\|G_{f,D}\Delta B_{LH}\|\,\|\widehat{\mathcal P}_cS^{-1}\|\\
 &+\|G_{f,D}B_{LH}\|
                  \|(\mathcal P_a-\widehat{\mathcal P}_c)S^{-1}\|,\\
 \varepsilon_b\ge{}&\|G_{f,D}B_{LH}\|\,\|\mathcal P_b\|.
 \end{split}
 \tag{WCTR.41}
$$

The original actual collar/body receivers and all their source, endpoint, jump, mean, and exterior qualifications are unchanged. In particular $\chi=0$ at a trial endpoint kills only that trial endpoint; it does not cancel an actual independent exterior function or a physical mean.

With the new $q_o,e_\rho,Q_D$, unchanged same-operator $q_m$, complete outer errors, and the proved $w_0=5/4$, set

$$
 \begin{split}
 q_R&=q_oE_-+q_m\mu_-,&
 o_H&=q_RY_a^{\rm err},\\
 o_b&=(3/80+E_-)q_o+\mu_-q_m+q_RY_b^0,\\
 e&=e_\rho+(1+e_\rho)
       \sqrt{w_0^2(K_H+\varepsilon_H)^2+\varepsilon_b^2}
                  +\sqrt{w_0^2o_H^2+o_b^2},\\
 d&=(1+e_\rho)(K_H+\varepsilon_H)+o_H,&
 t&=\sqrt{w_0^2t_H^2+t_b^2}.
 \end{split}
 \tag{WCTR.42}
$$

Here $K_H$ and $t_H,t_b$ have the same complete WVC meanings with (40) and the unchanged actual tail coordinates. Every term belongs to one candidate and one reference. The actual comparison remains

$$
                                  e+3dt<1 .
 \tag{WCTR.43}
$$

The old actual tail inverse (4) is used. If WPN is used instead, its lower preconditioner keeps the original proved tail principal inverse. A trace-modified finite reference is not silently made into a new proved actual tail contraction.

Only a true complete comparison (43) activates the actual finite inverse and the WPN reconstruction. Both original right-side rows are transformed and retained. The root-even normalization $I_{96}$ then follows from the actual imposed trace equations for those same $96$ columns, not from the reference circuit by itself. Other readouts retain their actual conversion.

## WCTR10. Minimal read-only boundary and complete future graph

This is a precise prospective dependency specification, not a declaration that a future WVC output already exists.

First admit one complete finished WVC candidate, if it is used as an old input: full scientific file, execution file, source and manifest identities, actual success or failure qualifications, all completed graph records and all prefixes. A failed unfinished graph cannot be treated as a complete supplier. All old WPS targets and old WVC targets remain frozen.

The original native/repair/cubic closure, exact centre coefficients, all physical scaling, original intrinsic intervals, complete full-degree96 error packets, complete source windows and immutable restoration identities remain the ones fixed by WVC. No degree96 shard is regenerated merely to replace a signed centre-plus-full-difference enclosure.

For a completed WVC candidate with at least one nonzero new trace clip, the following old/new boundary follows directly from the exact maps, not from record names:

| WVC graph | Unchanged complete part | New complete part for the trace candidate |
| --- | --- | --- |
| Reference receivers, 7 records | Mean receiver outside these seven; same-mode restrictions only when that mode has $r_i=0$ on every cell | Whole inverse row/column, whole normalizer row/column, inverse norm, defect, odd-endpoint receiver |
| High trial/source, 12 records | All 12: (38)--(39), input $S$, high principal, centre packet, full-family error, actual receiver and chosen comparison weights are exactly unchanged | None |
| Actual paired receivers, 22 records | 7: centre tail-LH row/column/norm, full-difference tail-LH, actual tail-LH, tail-$\Delta A_L$, raw tail-$\Delta B_{LH}$ | The other 15, all involving the new continuous low receiver |
| Local signed remainder, 8 records | 1: the complete outer-data tail source $t_b$ | 7: complete low paired and tail signed-centre source bounds and the assembled $t_H$ |
| Endpoint correction, 3 records | Unchanged scalar constituents may be copied only as original constituents | All three complete expressions with the new $q_o$ |
| Complete actual comparison, 4 records | No previous whole comparison is altered or overwritten | New $e,d,t,e+3dt$; add its positive gap and inverse fee only after the actual true comparison |

Thus this declared graph has $36$ new records and $20$ complete copied records before a possible two-record true-gate suffix. These are static counts, not numerical results. The exact row/column records of the unchanged parts are copied whole; their old calculation is not rerun.

If all trace clips vanish, the reference and the whole trial are exactly the existing WVC candidate. In that branch no new reference or residual norm is evaluated: copy the complete same candidate, retaining its own $w_0$ and true/false scope. It is not necessary to replace its old proved $6/5$ lift choice by the weaker $5/4$ of this theorem.

For a mixed set of modes, an old global modal upper bound may bound a restriction to an exactly unchanged mode. Its witness states that restriction and the original complete record. It is not an actual maximizing mode certificate and is never used for a changed mode. New changed-mode bounds are assembled with those valid restrictions before taking one complete direct-sum maximum.

The new scalar trace identity must bind the full signed diagonal recipe and every parent, root cell, mode, and child inheritance. The original reference chain is retained, and no old maximum or repair is recomputed. Definition-only materialization is distinguished from an already completed numerical bound. An identity of continuous $p,H$ equations alone does not claim that their per-cell saved enclosures are exposed in an old receipt.

The exact normalizer inverse, full signed local transfer/action blocks, two distinct continuous rates, discrete $\tau_b,\tau_f$, physical mean, root and outer atoms, and all source moments are required inputs to any implementation. All completed new whole targets and mode-prefix records must be saved before readback; an exception preserves the complete already computed prefix. An operation cap limits resources and does not discard a scientific prefix.

A future consumer must declare and verify its complete success, unchanged, true-gate and failure shapes, source/input identities, operation count and memory model before its first numerical target. This theorem does not assign those runtime observations. The finite action remains streaming and does not require a dense $4724833$ square matrix. Every actual finite inverse or actual $96$-column conclusion remains conditional on (43).

## Primary immutable references

| Primary | Git blob | Bytes | SHA256 |
| --- | --- | --- | --- |
| [WVC](R133-supplement-continuous-repaired-centre-trials-and-clipped-tracefree-reference.md) | e377cb2e0578fc66ba8a7bc32e339fadcb0a242c | 29128 | fade78e696506af0ef2c1e304e824ff7415c63df53b31f0ed299d8ff548845a8 |
| [WPS](R133-supplement-paired-source-circuits-and-complete-finite-residual-candidate.md) | e830f7df4643fe77b941478dbde06ebf9378ebef | 43851 | ffd000ff15f705ffaaf3c33dddcd0c09c997c0c92d5110bab5be5ea9c114fa72 |
| [WIC](R133-supplement-analytic-inherited-tail-and-weighted-impedance-circuit.md) | 019b1136ebe81e44e98399dff5fb895aafb4362e | 29026 | 527fc35e48f8bb8807e2dc7e7a4b8726e381d35183f31bf8977b252dbb66e59f |
| [WPN](R133-supplement-complete-paired-Neumann-reconstruction-and-root96-normalization.md) | 3c4b712c05b5c9fd392be2d9b65bbd8e727bd2ac | 17666 | dc553f11d578e00b2c2dd0abc7e4f3c78c852a519e1f06073962706e4d8c749d |
| [WPSA](R133-supplement-actual-complete-paired-finite-residual-and-false-gate.md) | 6bcd4484f596e39f94cb6adc870dec3b937ad984 | 50464 | 470d2547de70dea45468103bc3518e6ed5bcc757c348543896df4edda65a2f92 |

No independent physical mean, affine jump, exterior function, negative head, metric, nonlinear, $\nu$, $\Theta$, or cokernel obligation is erased by changing this reference.
