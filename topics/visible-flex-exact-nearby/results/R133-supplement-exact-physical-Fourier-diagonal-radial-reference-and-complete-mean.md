# R133 supplement: the exact physical Fourier diagonal radial reference and its complete mean

2026-11-15, visible-exact / phase_inverse.

**Proved:** an exact decomposition of the complete moving Jacobi generator into its physical Fourier diagonal and the remaining complete operator, including the primitive, independent even mean, two-state radial reference, and ordered residual and seam identities. The two-state reference is regular at the root and does not divide by the curvature.

This is an analytic identity and a conditional norm interface. It does not assert an evaluated reference Green operator, a small complete remainder, a new return coefficient, or a high-frequency inverse. All old actual source bounds, failed gates, finite numerator coefficients and physical seam ledgers remain intact. No new numerical computation is made here.

## 1. Exact object and Fourier convention

Use the fixed intrinsic parameter $\eta_0$ and the same explicit family
$Q_\delta=\bar Q+\delta Z$, $\nu_\delta=\nu_0+\delta$, with the exact repair and full direction of
[the complete moving scalarization](R133-supplement-complete-moving-root-scalarization.md).
Its immutable original text is Git blob
8a57ec851fc9029e4319650b87360b9867d22a97 (15539 bytes).
The formulas apply wherever that complete coefficient identity is defined, including its previously certified complex root family. They do not identify this explicit family with a nonlinear PDE solution.

Work in the old physical moving angle $\phi$, of period $\pi/2$, with normalized measure:
$$
 e_j(\phi)=e^{4ij\phi},\qquad
 \partial=\partial_\phi,\qquad
 \Pi f=\langle f\rangle,\qquad P=1-\Pi,\qquad
 I=\partial^{-1}P .
 \tag{R.1}
$$
The physical frequency is $4j$, and the multiplier of $I$ at $j=0$ is exactly zero. All Fourier coefficients below refer to this angle before a nonconstant ray or canonical pullback.

Use the original coefficients
$$
 m=\langle v\rangle,\quad \eta=-\gamma m,\quad
 S=u^2+Kv^2,\quad d=-bIS,\quad \ell=-2buv,
$$
$$
 e=-b(1+3u^2+Kv^2),\qquad B=b(1-u^2-3Kv^2).
 \tag{R.2}
$$
Here $b=a_{\rm phys}'/a_{\rm phys}$; the characteristic coefficient $\eta$ is not the intrinsic parameter $\eta_0$.
Products of background coefficients are bilinear, also for complex $\delta$.

The parity class is $u,h_1$ odd and $v,h_2$ even.
The exact repaired mean and the full direction mean belong to $m$.
The explicit background has angular degree at most 96; its repaired centre has degree at most 32. No finite support is imposed on the unknown variation.

## 2. The full generator before taking its diagonal

Writing $h=(h_1,h_2)^\mathsf T$, the original equation (N.3) is
$$
 \partial_rh=\mathcal Gh+g,
 \tag{R.3}
$$
where
$$
 \begin{split}
 \mathcal G_{11}&=M_d\partial+M_e-2bM_{u_\phi}IM_u,\\
 \mathcal G_{12}&=-\eta K\partial+KM_\ell
                    -2bKM_{u_\phi}IM_v+\gamma KM_{v_\phi}\Pi,\\
 \mathcal G_{21}&=\eta\partial+M_\ell-2bM_{v_\phi}IM_u,\\
 \mathcal G_{22}&=M_d\partial+M_B-2bKM_{v_\phi}IM_v
                                         -\gamma M_{u_\phi}\Pi.
 \end{split}
 \tag{R.4}
$$
Thus $D=\partial_r-d\partial_\phi$ was moved to the right with a plus sign. The two rank columns are retained.

These identities first act on smooth states on an actual radial piece, and extend to the original weak graph domain with the reconstructed flux. Piecewise identities use genuine one-sided traces. An ordinary source $g_2$ need not have a radial derivative.

For any angular coefficients $p,q$, direct Fourier multiplication gives
$$
 (M_{p_\phi}IM_q)_{mn}
   =\sum_{k\ne0}\frac{m-k}{k}\,p_{m-k}q_{k-n}.
 \tag{R.5}
$$
The factor $4i(m-k)$ from the first multiplier cancels the $4ik$ of the primitive. Define its diagonal entry by
$$
 D_j(p,q)=\sum_{\ell\ne j}\frac{\ell}{j-\ell}\,
                                    p_\ell q_{-\ell}.
 \tag{R.6}
$$
Here $k=j-\ell$. The term $\ell=j$ is omitted because the intermediate primitive mode is the mean. It must not be restored as a singular or limiting term. With the current background this is a finite sum for every integer $j$, while $j$ itself is unrestricted.

## 3. The exact complete physical Fourier diagonal

Let $\mathcal R$ be the Fourier diagonal of $\mathcal G$, so
$(\mathcal Rh)_j=R_jh_j$. Set
$$
 E_j=\langle e\rangle-2bD_j(u,u),\qquad
 B_j=\langle B\rangle-2bKD_j(v,v),\qquad
 A_j=4ij\eta+2bD_j(u,v).
 \tag{R.7}
$$
Then
$$
 \boxed{\quad
 R_j=\begin{pmatrix}E_j&-KA_j\\A_j&B_j\end{pmatrix},
 \qquad \mathcal G=\mathcal R+\Delta\mathcal G .
 \quad}
 \tag{R.8}
$$
The difference contains every off-diagonal physical Fourier entry.

Indeed $\langle d\rangle=0$ by definition and
$\langle\ell\rangle=-2b\langle uv\rangle=0$ by parity.
Each derivative-rank column has zero diagonal: a nonzero input label has zero mean, and the output derivative at input label zero has zero mean. Finally
$$
 D_j(v,u)=-D_j(u,v),\qquad
 D_{-j}(p,p)=D_j(p,p),\qquad
 D_{-j}(u,v)=-D_j(u,v)
 \tag{R.9}
$$
for $p=u$ or $v$. Replace $\ell$ by $-\ell$ and use
$u_{-\ell}=-u_\ell$, $v_{-\ell}=v_\ell$ to prove these equalities.
They are parity identities for the full complex family, not conjugation identities. In particular
$$
 R_{-j}=\mathfrak D R_j\mathfrak D,\qquad
                 \mathfrak D=\operatorname{diag}(-1,1).
 \tag{R.10}
$$
Both label signs and both state columns remain.

For background degree at most 96, $\mathcal G$ and $\Delta\mathcal G$
have bandwidth at most 192. Their derivative-rank columns have input label zero and output labels of size at most 96. These are generator statements; neither the inverse nor the propagator is claimed to have finite bandwidth.

## 4. The independent even mean agrees exactly

At $j=0$ one has
$$
 D_0(u,u)=-\langle u^2\rangle,\qquad
 D_0(v,v)=-\langle v^2\rangle+m^2,\qquad
 D_0(u,v)=0.
$$
Consequently
$$
 A_0=0,\qquad E_0=-b(1+\langle S\rangle),\qquad
 \boxed{\ B_0=b(1-\langle S\rangle)-2bKm^2.\ }
 \tag{R.11}
$$
The first zero mode is absent in the physical odd class. The second is the actual independent even mean.

Let $f=Ph_2$, $z=\langle h_2\rangle$. The full mean equation is exactly
$$
 \boxed{\quad
 z_r=B_0z-2bm\langle uh_1+K(v-m)f\rangle+\langle g_2\rangle .
 \quad}
 \tag{R.12}
$$
This is the original (N.7), with precisely the coefficient (R.11).
It can also be recovered by taking the mean of (R.4), integrating by parts, and using $d_\phi=-bPS$.

The nonmean functional in (R.12) belongs to $\Delta\mathcal G$ and remains a source of mean coupling. For a state supported strictly in $|j|\ge97$, this one functional vanishes by background support. The actual Airy reconstruction, physical source, seam correction, or evolved state cannot be assumed to retain that support. Its independent source $\langle g_2\rangle$ is never dropped.

The homogeneous radial mean propagator is therefore
$$
 Y_{\rm mean}(r,s)=\exp\!\left(\int_s^r B_0(t)\,dt\right),
 \tag{R.13}
$$
while the second and third terms of (R.12) remain in the true equation. No transport mean has replaced the physical mean.

## 5. Exact high-label formulas

For background degree at most $M$ and $|j|>M$, pair $\ell$ and $-\ell$ in (R.6):
$$
 \begin{split}
 D_j(p,p)&=\sum_{\ell=1}^M
        \frac{2\ell^2}{j^2-\ell^2}\,p_\ell p_{-\ell},\\
 D_j(u,v)&=\sum_{\ell=1}^M
        \frac{2j\ell}{j^2-\ell^2}\,u_\ell v_{-\ell}.
 \end{split}
 \tag{R.14}
$$
The numerator at $\ell=0$ is zero. In the second formula the paired products have opposite parity. All displayed denominators are nonzero and positive for these real integer labels.

Ordinary normalized $L^2$ gives the complete bounds
$$
 \begin{split}
 |D_j(u,u)|&\le
       {M^2\over j^2-M^2}\|u\|_2^2,\\
 |D_j(v,v)|&\le
       {M^2\over j^2-M^2}\|v-m\|_2^2,\\
 |D_j(u,v)|&\le
       {|j|M\over j^2-M^2}\|u\|_2\|v-m\|_2.
 \end{split}
 \tag{R.15}
$$
For example $2\sum_{\ell>0}|u_\ell v_{-\ell}|
\le\|u\|_2\|v-m\|_2$ by Cauchy--Schwarz and parity.
These inequalities also hold for complex parameters, with modulus norms.

Thus the corrections to $E_j,B_j$ are $O(j^{-2})$ and that to
$A_j$ is $O(j^{-1})$, with exactly the stated constants.
This does not assert smallness at $j=97$.
When $\eta\ne0$, a sufficient condition for $A_j\ne0$ is
$$
 {\,|b|M\,\over2|\eta|(j^2-M^2)}
                       \|u\|_2\|v-m\|_2<1.
 \tag{R.16}
$$
It gives the lower bound $4|j\eta|$ times one minus its left side.
Condition (R.16) has not been numerically executed here.
The following two-state reference does not require it.

## 6. The two-state radial reference and ordinary sources

On each actual radial piece define
$$
 \partial_rY_j(r,s)=R_j(r)Y_j(r,s),\qquad Y_j(s,s)=I_2 .
 \tag{R.17}
$$
For fixed $j$ the coefficients are locally integrable and regular at the simple root. The finite-dimensional linear ODE therefore has a unique matrix, with
$$
 \det Y_j(r,s)=
       \exp\!\left(\int_s^r(E_j+B_j)(t)\,dt\right)\ne0 .
 \tag{R.18}
$$
No division by $K$, $\sqrt{-K}$, $j$, or $A_j$ occurs.
Both columns are part of the reference.
For an ordinary integrable source,
$$
 h_j(r)=Y_j(r,s)h_j(s)+\int_s^rY_j(r,t)g_j(t)\,dt .
 \tag{R.19}
$$
The integral is oriented, so the same formula fixes the reverse sign when $r<s$.

An actual additive jump at a seam contributes its ordered propagated vector. If the physical trace convention uses a nonidentity matrix, that exact matrix must be inserted between adjacent propagators. It cannot be replaced by continuity.

The notation $\mathcal E(r,s)=\operatorname{diag}_jY_j(r,s)$ is initially componentwise or on finite physical Fourier data.
The ODE identity alone does not prove a bounded infinite Sobolev or analytic propagator. In a positive-curvature interval its unrestricted two-column Cauchy map generally has an exponentially growing column. The genuine positive graph, two-port source contract and their norm must be imposed and paid separately.

## 7. Scalar factorization when its denominator is paid

On an interval where $A_j\ne0$, put $f_j=h_{2,j}$,
$q_j=E_j+A_j'/A_j$, and $t_j=q_j+B_j$.
The exact weak elimination is
$$
 (\partial_r-E_j)A_j^{-1}
       \{(\partial_r-B_j)f_j-g_{2,j}\}
                         +KA_jf_j=g_{1,j},
 \tag{R.20}
$$
with $h_{1,j}=A_j^{-1}\{(\partial_r-B_j)f_j-g_{2,j}\}$.
For smooth sources it expands to
$$
 f_j''-t_jf_j'
       +(q_jB_j-B_j'+KA_j^2)f_j
          =A_jg_{1,j}+g_{2,j}'-q_jg_{2,j}.
 \tag{R.21}
$$
The derivative on the right is the weak flux of (R.20), not a new assumption for ordinary data.

For the homogeneous equation, use
$f_j=\exp(\frac12\int t_j)\,y_j$. Then
$$
 y_j''+
 \left\{KA_j^2+\frac12(q_j-B_j)'
                       -\frac14(q_j-B_j)^2\right\}y_j=0 .
 \tag{R.22}
$$
Indeed $q_jB_j-B_j'+t_j'/2-t_j^2/4
=(q_j-B_j)'/2-(q_j-B_j)^2/4$.
This retains the entire radial potential and finite primitive diagonal; it does not replace the equation by pure Airy.

For real parameters one may write $A_j=4ij a_j$, $j\ne0$.
If $a_j$ has a nonzero analytic branch, a subsequent radial Langer coordinate may be defined from $T_j(T_j')^2=Ka_j^2$ on the simple-root germ. Its domain, derivative gaps, complete source transform and numerical remainder are additional obligations. No such gate is claimed here.

## 8. Exact interface with the old Airy trial

Let $V^{\rm tr}(r)$ be any already constructed full physical trial column, with the original input normalization, signed carrier and all output modes.
The physical reconstruction is still the original (N.9):
$$
 h_1=J\{(D_0-B_{\rm op})f-zb_2-Pg_2\},\qquad h_2=f+z .
 \tag{R.23}
$$
The old-circle $J$ and $B_{\rm op}$ are the complete original operators.
$B_{\rm op}$ is distinct from the coefficient $B$ and the diagonal scalar $B_j$.
Replacing $J$ by a radial inverse would change the trial and is not done.

The Airy construction uses $f=P\mathcal U(w_0+n^{-1}w_1)$ with its original density normalization.
Taking its trial $z=0$ leaves the mean residual from (R.12); it does not remove the mean equation.
All original terms from
[the exact old-circle remainder](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md)
and
[the compressed mean](R133-supplement-exact-old-mean-compression-and-first-correction-nonlocal-budgets.md)
remain.

Define the complete residuals
$$
 R^{\rm tr}=(\partial_r-\mathcal G)V^{\rm tr},\qquad
 E^{\rm tr}=(\partial_r-\mathcal R)V^{\rm tr}.
$$
Then, before taking any absolute bounds,
$$
 \boxed{\ E^{\rm tr}=R^{\rm tr}+\Delta\mathcal G\,V^{\rm tr}.\ }
 \tag{R.24}
$$
A difference of unrelated upper bounds may not replace either signed expression.

Take the complete actual root trace $C_*=V^{\rm tr}(r_*)$ and define, componentwise,
$$
 (V^{\rm rad})_m(r)=Y_m(r,r_*)(C_*)_m .
 \tag{R.25}
$$
The index $m$ is the **physical output** label, not the input carrier of the original column.
A nonconstant ray generally supplies infinitely many output modes.
The finite trace approximation, full trace enclosure and its omitted tail must all be retained. No diagonal projection of $C_*$ follows from this reference.

Where the sums belong to a proved common space, or componentwise before that extension,
$$
 V^{\rm rad}(r)-V^{\rm tr}(r)
       =-\int_{r_*}^r\mathcal E(r,t)E^{\rm tr}(t)\,dt .
 \tag{R.26}
$$
For unequal reference and trial root traces, add the exactly propagated initial difference.
This is a genuine reference correction, not deletion of a residual by changing its name.

## 9. Physical seams and the complete remaining coupling

In increasing radial orientation suppose the original trial jump is
$J_c=V^{\rm tr}(c+)-V^{\rm tr}(c-)$, while the reference jump is $a_c$.
With identity physical trace convention, for $r\ge s$,
$$
 \begin{split}
 V^{\rm rad}(r)-V^{\rm tr}(r)
 ={}&\mathcal E(r,s)(V^{\rm rad}(s)-V^{\rm tr}(s))\\
    &-\int_s^r\mathcal E(r,t)E^{\rm tr}(t)\,dt
      +\sum_{s<c\le r}\mathcal E(r,c)(a_c-J_c).
 \end{split}
 \tag{R.27}
$$
The reverse formula reverses the seam order and jump sign.
For nonidentity trace matrices, use their exact ordered form in the propagator and the jumps.

A continuous reference gives correction jump $-J_c$, not an assertion $J_c=0$.
The original 1079 physical seams and 653 inherited seam-ledger entries remain.
The single physical root piece 2549 has no artificial internal seam, but its original two endpoint seams are not moved or removed.

For the homogeneous radial reference,
$$
 (\partial_r-\mathcal G)V^{\rm rad}
                          =-\Delta\mathcal G\,V^{\rm rad}.
 \tag{R.28}
$$
A true solution consequently satisfies the ordered Duhamel formula
$$
 h(r)=\mathcal E(r,s)h(s)
     +\int_s^r\mathcal E(r,t)
                 \{\Delta\mathcal G h(t)+g(t)\}\,dt
     +\hbox{the genuine ordered physical jump ports}.
 \tag{R.29}
$$
This formula requires the actual mapping norms and boundary selection, or is read componentwise on an already defined solution. It is not a contraction theorem by itself.

In particular $\Delta\mathcal G$ still contains $M_d\partial$, generally an angular first-order term. Zero Fourier diagonal does not make it an order-zero small operator. A true principal transport or a paid Green gain must deal with it before a same-order norm estimate is used.
The derivative-rank columns and the full mean functional (R.12) also remain.

## 10. The finite numerator constant stays in the problem

The actual correlated local numerator is $N_{\rm raw}=\mu L_0w_1$.
A degree-zero coefficient of its **amplitude** is not the zero physical output after multiplication by the carrier and complete angle map.
Neither $\Pi$ nor the independent even-mean equation licenses deletion of that coefficient.

The reference (R.8) is instead defined from the complete physical generator before any Airy amplitude is inserted.
Its radial coefficients contain the finite primitive sums and the exact physical mean. The only permitted comparison is (R.24)--(R.29), with full physical residual, root trace and seam ports.
Any smaller numerical bound must follow from a newly certified reference solve or a rigorously evaluated complete signed difference.

All prior signed finite $N_{\rm raw}$ coefficients stay unchanged, together with the complete nine old-circle words, five independent-mean source rows, positive two-port conditions and true mean/head feedback. An upper bound from an earlier successful native does not become signed data in this comparison.

## 11. The minimal new numerical interface

A public consumer can form (R.6)--(R.8) from the already pinned original 65/193 coefficient pieces and exact repairs, or from a complete signed coefficient stage with the same object identity.
It must retain all background modes and the exact missing intermediate primitive mean.
The infinite labels in (R.14) are represented by a finite rational formula; its evaluation requires no repeated target, FFT, completed Taylor coefficient or old source norm.

What remains new is the enclosure of the selected radial evolution or boundary Green map, its parameter and frequency windows, and the full physical source and seam maps in the actual norm used.
Whole-piece coefficients and radial jets must remain in their pinned domains.
An auxiliary analytic extension agrees with the physical family only on their already proved overlap; it cannot be used across a physical seam.

The principal nonradial transport, full positive boundary selection, low/high and mean feedback, return arithmetic including any reference-phase change, and genuine PDE-background transfer remain explicit obligations.
This theorem supplies their exact radial reference interface. It grants no numerical cutoff, no $j\ge97$ inverse, and no final completion of the topic.
