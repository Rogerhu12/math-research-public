# R147 WRA: the actual-anchor-sensitive weak physical height receiver

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**Proved:** the complete original-negative weak receiver for the physical
mean-height row now includes an arbitrary genuine $C^1$ change of its
world anchors. The anchor dependence is explicit and linear in the
three actual seminorms below. No actual anchor is identified with the
old reference by declaration, and no $C^1$ error is inferred from a
$C^0$ error.

This supplies a missing interface between
[WRC's fixed-reference receiver](R147-supplement-complete-reference-world-height-and-original-negative-receiver.md)
and the original complete root/strict source spaces used by TC and
the full inverse. It does not assert the uncompleted TC source arrays
or the full finite/high/parameter Schur to be complete.

## WRA1. Same state, actual anchors and the three genuine errors

Fix the original selected $Q_{\delta_*},\nu_{\delta_*},\eta_0$ on
$[0,b]$, $b=9/50$. Retain its entire relative $A,x$ from RH and RHI.
The actual $A$ is in $SO(3)$; the original absolute frame has
determinant $-1$. Both actual and reference world frames use that
same absolute convention.

Let $(\mathsf Q_b,F_b)$ be the actual independent anchors at $b$.
Let $(\mathsf Q_b^{\rm ref},F_b^{\rm ref})$ be WRC's fixed original
raw anchors at $b$. Define the actual vertical functions

$$
 q_b=e_z^T\mathsf Q_b,\quad f_b=e_z^TF_b,\qquad
 \Delta q_b=q_b-q_b^{\rm ref},\quad
 \Delta f_b=f_b-f_b^{\rm ref}.                         \tag{WRA.1}
$$

Only the following actual quantities are used:

$$
 a_0=\|\Delta q_b\|_\infty,\qquad
 a_1=\|\partial_\phi\Delta q_b\|_\infty,\qquad
 b_1=\|\partial_\phi\Delta f_b\|_\infty.               \tag{WRA.2}
$$

The first two use the Euclidean row norm. Full matrix bounds on
$\mathsf Q_b-\mathsf Q_b^{\rm ref}$ and its derivative may dominate
them, but neither a full matrix derivative nor $a_1$ is supplied by
an undifferentiated frame bound. The physical angle labels and
normalized fourfold measure are the original ones. The vertical
projections are $C^1$ functions on that original angle circle; the
full horizontal world anchors retain their original quarter-turn
equivariance. An unmatched angular world seam would supply an additional
independent boundary functional and is not silently admitted as periodic.

The zero-order value of $\Delta f_b$ is not required for this weak
mean-height difference: its constant component has an exact
annihilator, proved below. This fact does not delete the independent
varying vertical-position port.

For a complete fixed-metric curvature correction $h$, retain both means
and set

$$
 J=v/m,\quad
 g_h={h_2\over m}-{v\Pi h_2\over m^2}
         =\partial_\phi\dot\Theta_h .
                                                               \tag{WRA.3}
$$

Let $y_h$ be the full relative position variation with its independent
$b$-ports fixed. The body part of the actual physical mean-height row is

$$
 \mathcal L_b(h)=\Pi J q_b y_h(0)+
                  \Pi g_h\{f_b+q_bx(0)\}.               \tag{WRA.4}
$$

There is no replacement of this row by an unweighted relative mean.
All products are in the original order; in particular the full
mean-containing rank-one part of $g_h$ is present.

Subtract the same exact row with the reference anchors. This gives

$$
 \boxed{\quad
 \Delta\mathcal L_b(h)=
       \Pi J\Delta q_b\,y_h(0)
       +\Pi g_h\{\Delta f_b+\Delta q_bx(0)\}.
 \quad}                                                    \tag{WRA.5}
$$

This is an operator identity, not a difference of two numerical upper
bounds.

## WRA2. Complete angular position and weighted adjoint bounds

The original selected short bounds from
[RRM](R149-supplement-relative-frame-position-means-in-original-negative-source-windows.md)
give

$$
 |c|\le C_0=19/5,\quad |c_\phi|\le C_1=25/2,\quad
 |A_\phi(r)|_{\rm op}\le12(b-r).
$$

Since $x(0)=-\int_0^b A(r)c(r)\,dr$, the complete pointwise estimates are

$$
 \boxed{\quad
 |x(0)|\le X_0=C_0b={171\over250},\qquad
 |x_\phi(0)|\le X_1=6C_0b^2+C_1b={37359\over12500}.
 \quad}                                                    \tag{WRA.6}
$$

The $A_\phi c$ contribution is included. These are bounds for the exact
relative solution over the whole angle circle, not numerical endpoint
interpolation claims.

For $w(\phi)=J(0,\phi)\Delta q_b(\phi)^T$,

$$
 \|w\|_\infty\le{27\over8}a_0,\qquad
 \|w_\phi\|_\infty\le{165\over32}a_0+{27\over8}a_1 .
                                                               \tag{WRA.7}
$$

Here $27/8=V/M$ and $165/32=(11/2)/(16/15)$ use the whole
$v,v_\phi$ and true mean bounds. The weight is not commuted through
a nonlocal primitive.

RRM's exact Fubini adjoint for relative position is
$L_m^*z_m+L_c^*z_c$ with

$$
 z_m(r)=A(r)^T(X(r)\times w),\quad
 z_c(r)=-A(r)^Tw,\quad X(r)=\int_0^r A(s)c(s)\,ds .
$$

Its full $H^1$ norm for a constant unit test is below26. The genuine
full $L^2$ norms of both $L_m,L_c$ are below5/2. Their derivative
commutators, including every primitive and moving-mean coefficient,
are already paid in RRM. The additional derivative of a variable
test therefore gives

$$
 \|L_m^*z_m+L_c^*z_c\|_{H^1}
 \le26\|w\|_\infty+
        {5\over2}(C_0b+1)\|w_\phi\|_\infty.              \tag{WRA.8}
$$

Substitution into this entire joint bound yields

$$
 \boxed{\quad
 C_Y={70053\over640}a_0+{11367\over800}a_1,\qquad
 |\Pi J\Delta q_b\,y_h(0)|
 \le C_Y\int_0^b\|h(r)\|_{H^{-1}\oplus H^{-1}}\,dr .
 \quad}                                                    \tag{WRA.9}
$$

These constants include the actual derivative of the outer vertical
covector. The estimate uses full Euclidean vector norms, not three
separate rows with an undeclared dimension loss.

## WRA3. Complete coordinate term and the endpoint port

For the second term of (WRA.5), integration by parts gives exactly

$$
 \Pi g_h(\Delta f_b+\Delta q_bx)
 =-\Pi\dot\Theta_h\{
      (\Delta f_b)_\phi+(\Delta q_b)_\phi x
                         +\Delta q_bx_\phi\}.            \tag{WRA.10}
$$

All three derivatives are retained. In particular the middle term
cannot be omitted when a world anchor depends on angle.

The already proved RH complete angle map gives

$$
 \|\dot\Theta_h\|_2\le{5\over4} Z_h(0),\qquad
 Z_h(r)=\|(Ih,\Pi h)(r)\|.
$$

This estimate includes the full moving mean. Equations (WRA.6),(WRA.10)
therefore prove

$$
 \boxed{\quad
 C_\theta={37359\over10000}a_0+{171\over200}a_1+{5\over4}b_1,
 \qquad
 |\Pi g_h(\Delta f_b+\Delta q_bx)|
                 \le C_\theta Z_h(0).
 \quad}                                                    \tag{WRA.11}
$$

The endpoint norm is supplied by the true original SP propagation;
it is not obtained as a trace of an ordinary radial $L^2$ norm.

Since $\Pi g_h=0$ exactly, a constant vertical difference between
the two fixed base anchors drops from (WRA.10). A constant independent
phase shift also drops from this mean-height row, because only
$\partial_\phi\dot\Theta_h$ occurs. These two identities apply to the
physical mean test; nonconstant height tests and the original phase
constraint retain their respective independent columns.

## WRA4. Actual root/strict source units and the complete table

Use the unchanged original source variables of WRC/RRM:
$D_*$ is true-root data in $H^{-2/3}\oplus H^{-1}$;
$F_-,J_-$ are the complete ordinary $L^2(dr)$ root source and
unweighted affine-jump sum in those units.
$F_{\rm st},J_{\rm st}$ are the complete strict counterparts in
$H^{-1}\oplus H^{-1}$. The root/strict interface impulse belongs to
the root list once. Every original piece and both means remain.

With

$$
 U=173.872,\quad N_I=11.272695,\quad J_{\rm in}=1.060693,\quad
 q_0=2669/5000,\quad R=1/200,\quad
 r_c={2333968743003\over10^{13}},
$$

the same full SP/root products used in WRC give, for any nonnegative
$C,c$,

$$
\begin{aligned}
 \mathcal R(C,c)
 ={}&{UN_I\over q_0}(bC+c)(D_*+J_-+\sqrt R\,F_-)\\
 &+{UJ_{\rm in}\over q_0}
       \{bC\sqrt{r_c-2b/3}+c\sqrt{r_c}\}\,F_{\rm st}\\
 &+{UJ_{\rm in}\over q_0}(bC+c)J_{\rm st}.              \tag{WRA.12}
\end{aligned}
$$

Inserting (WRA.9),(WRA.11) gives
$|\Delta\mathcal L_b(h)|\le\mathcal R(C_Y,C_\theta)$.
The integration weights include sources on $[b,r_c]$ and all shorter
ordered products. A geometric or state impulse is never multiplied
by a fictitious radial length.

Twelve new exact rational comparisons use the already paid
$\sqrt R<.070711$, $\sqrt{r_c-2b/3}<.337$ and
$\sqrt{r_c}<.484$. All twelve were evaluated once and passed:

| Original complete source | Coefficient of $a_0$ | Coefficient of $a_1$ | Coefficient of $b_1$ |
|---|---:|---:|---:|
|$D_*+J_-$|86061|12531|4590|
|$F_-$|6086|887|325|
|$F_{\rm st}$|2919|441|210|
|$J_{\rm st}$|8098|1180|432|

Adding the already paid fixed-reference WRC row proves the complete
actual-anchor body estimate

$$
\boxed{\begin{aligned}
 |\mathcal L_b(h)|\le{}&
 (94000+86061a_0+12531a_1+4590b_1)(D_*+J_-)\\
 &+(6650+6086a_0+887a_1+325b_1)F_-\\
 &+(3000+2919a_0+441a_1+210b_1)F_{\rm st}\\
 &+(8850+8098a_0+1180a_1+432b_1)J_{\rm st}.
\end{aligned}}                                              \tag{WRA.13}
$$

The coefficients are in precisely the old source units. No false
conversion of the selected degree288 parameter source or an infinite
PDE correction into a finite $L^2_\phi$ residual occurs.

## WRA5. Actual varying frame and position ports

The base-anchor comparison in WRA1 is distinct from variation of
the actual anchor along a correction. For those independent ports put

$$
 Y_b=\dot F_b,\qquad K_b=\dot{\mathsf Q}_b\mathsf Q_b^T,\qquad
                      k_b=\operatorname{ax}K_b .
$$

The complete physical mean row includes

$$
 P_b=\Pi J e_z^T(Y_b+K_b\mathsf Q_bx(0)).                \tag{WRA.14}
$$

Real orthogonality and (WRA.6) give the direct complete bound

$$
 \boxed{\quad
 |P_b|\le{27\over8}\|e_z^TY_b\|_2+
                   {4617\over2000}\|k_b\|_2 .
 \quad}                                                    \tag{WRA.15}
$$

The axial vector here is that of the actual world skew matrix $K_b$.
There is no incorrect determinant-$-1$ conversion through
$\mathsf Q_b$. In particular a varying vertical translation in $Y_b$
has its genuine nonzero column. Its norm is an independent endpoint
input, not a body norm trace.

For the original identity passive transmissions, (WRA.13) plus
(WRA.15) is the full row estimate. Any additional prescribed affine
passive frame or position transmission must remain as its own
propagated geometric port; WRA does not turn it into one of the
ordinary curvature-source terms.

## WRA6. Use and limits

The companion
[saved-bound consumer](../scripts/fourfold_codazzi_actual_anchor_weak_height_saved_bounds.py)
records the twelve new exact comparisons and the resulting full
four-source/three-anchor table. No old scientific norm, phase,
geometry, RHI, TC or WMR target is evaluated by this derivation.

For a genuinely completed TC column, use its complete original
weak source records in (WRA.13), and append its actual independent
ports in (WRA.14). For a complete finite row, the entire resulting
column-error vector gives its joint error in the original finite
coordinates. Incomplete TC prefixes cannot supply those whole norms.

The actual $a_0,a_1,b_1$ must come from the same world anchors and
same angular chart. The theorem does not assign them numbers.
The separate compact-centre, tail-selection and full Schur problems
retain their own transfer and closure obligations.
