# R133 supplement: fixed-base conservative source transport and nearby cap linearization

2026-11-15, visible-exact-astra-0df9.

**Proved exact identities and a quantitative fixed-port cap perturbation criterion.**
The reference remains the continuous repaired centre
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47,
at fixed intrinsic eta0 and delta=0. The coordinate map in this note is
frozen at that reference. Its already paid radial derivative and residual
Hessian remain in the base inverse. A nearby coefficient field is never
differentiated radially in the new perturbation estimate.

The result concerns the complete original moving field in its actual
odd/even reflection sector. The angular source identity itself holds on
all of 4Z, with both genuine means. Actual changed boundary graphs, the
negative body, the full parameter Schur and a nonlinear same-space
iteration still require their own estimates.

Dependencies are the [complete normalized gauge](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md),
the [exact moving flux](R133-supplement-complete-moving-nonlinear-flux-and-metric-remainder.md),
the [continuous repaired cap](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md),
the [shifted Sobolev cap](R133-supplement-shifted-Sobolev-complete-gauge-Hessian-and-cap-tail-Schur.md),
and the [actual reflection bridge](R133-supplement-exact-reflection-sector-and-original-moving-cap-tail-bridge.md).
All operators and means below use their original normalization.

## 1. Freeze the physical angle once

Write the reference as Q0=(u,v), with signed m=<v>_phi.
Let Theta, Phi, W=(B,C)=Psi(Q0), and I_theta be exactly G.1--G.5.
A hat always means composition with this fixed Phi. In displayed
physical-coordinate products u and v also denote their hatted values.
In particular
$$
 \Phi_\theta=mC,\qquad \langle C\rangle_\theta=1/m,\qquad
 P=\begin{pmatrix}C&-BC\\0&-C^2\end{pmatrix}.
 \tag{P.1}
$$
The actual m,v,C are negative. The following identities use these signed
values.

For a moving source f the complete derivative is
$$
 D\Psi_0 f=P\widehat f-W_\theta E_f,\qquad
 E_f=I_\theta(C\widehat f_2)
           -m\langle C I_\theta(C\widehat f_2)\rangle_\theta .
 \tag{P.2}
$$
For x=(b,c) the inverse, expressed in the same physical angle, is
$$
 \mathcal Hx=
 \begin{pmatrix}v&-uv\\0&-v^2\end{pmatrix}
       (x-vW_\theta p_c),\qquad
 p_c=I_\theta(c-mC\langle c\rangle_\theta).
 \tag{P.3}
$$
Thus the moving direction h is defined by hat h=H x. This is the
complete inverse differential, including the independent even mean.

## 2. Exact divergence-source cancellation, including its rank mean

Let a=(a1,a2) be an arbitrary periodic angular flux. The actual
derivative is the old moving derivative partial_phi, not partial_theta.
The chain rule gives
$$
 \widehat{\partial_\phi a}={v\over m}\partial_\theta\widehat a,
 \qquad C\widehat{\partial_\phi a_2}
                       ={1\over m}\partial_\theta\widehat a_2 .
$$
Since I_theta partial_theta removes the true physical mean, (P.2) and
<C>=1/m give exactly
$$
 E_{\partial_\phi a}
           =\widehat a_2/m-\langle C\widehat a_2\rangle_\theta .
 \tag{P.4}
$$
Define
$$
 M={Pv\over m}={1\over m}
             \begin{pmatrix}1&-B\\0&-C\end{pmatrix}.
$$
Its derivative satisfies
M_theta=-(1/m)W_theta e2^t. Therefore the two multiplication terms
cancel in the precise order
$$
 \boxed{\quad
 D\Psi_0(\partial_\phi a)
       =\partial_\theta(M\widehat a)
            +W_\theta\langle C\widehat a_2\rangle_\theta .
 \quad}                                                   \tag{P.5}
$$
The last term has a plus sign. It is a genuine complete rank-one
ordinary source. The true measure also gives
<C hat a2>_theta=<a2>_phi/m.
Adding a constant to a2 makes the two changes on the right of (P.5)
cancel, as required for a divergence source.

Consequently, for an ordinary remainder b,
$$
 D\Psi_0(\partial_\phi a+b)
  =\partial_\theta(M\widehat a)
   +W_\theta\langle C\widehat a_2\rangle_\theta
   +P\widehat b-W_\theta E_b .                             \tag{P.6}
$$
No derivative of an unknown or of a nearby background occurs in the
ordinary part of this formula. No reflection assumption was needed.

Both physical component means in (P.5) vanish. In (P.6) the ordinary
source retains, exactly,
$$
 \langle(D\Psi_0 b)_C\rangle_\theta
                 =-\langle b_2\rangle_\phi/m^2,
$$
$$
 \langle(D\Psi_0 b)_B\rangle_\theta
       =\langle b_1\rangle_\phi/m
            -\langle u\rangle_\phi\langle b_2\rangle_\phi/m^2 .
 \tag{P.7}
$$
The actual reference has <u>_phi=0; its even mean remains independent.
The identities first hold for smooth complete functions and extend by
the paid divergence-potential and ordinary-source norms. They do not
replace a radial weak source by an angular one.

## 3. The old primitive in the fixed physical angle

A composition operator on an arbitrary unknown Hilbert module need not
be close to the identity. None is used here.

For a physical scalar g define the true old-angle mean and primitive
by
$$
 \Pi_0g=m\langle Cg\rangle_\theta,\qquad
 \mathcal I_0g=
 T_g-m\langle CT_g\rangle_\theta,\quad
 T_g=I_\theta\{mC(g-\Pi_0g)\}.
 \tag{P.8}
$$
Their exact meanings are
$$
 \Pi_0\widehat f=\langle f\rangle_\phi,\qquad
                \mathcal I_0\widehat f=\widehat{I_\phi f}.
 \tag{P.9}
$$
To prove the second identity, differentiate in theta and impose its
original zero mean in phi. Both operations agree with (P.8), which
determines the unique primitive.

Use the physical coefficientwise radial-supremum Wiener algebra A0
and Hilbert module M of the continuous cap theorem, with the pair norm
equal to the sum of the component norms. Put J=||mC||_A0.
The paid complete coefficients give J<33/32. The Fourier multiplier
I_theta has norm 1/4. Ordinary multiplication and the weighted mean
therefore give
$$
 \|\Pi_0\|\le J<2,\qquad
 \|\mathcal I_0\|\le J(1+J)^2/4<2.                         \tag{P.10}
$$
These bounds hold both on A0 and on M. In particular the latter is
sum_k sup_r of coefficients in its stated squared order; no
sup_r sum_k interchange is made. Every occurrence of the moving
primitive below is transported by (P.8), including its mean constant.

## 4. The full Jacobian difference is an angular divergence plus an ordinary mean source

At fixed intrinsic coefficients put
$$
 S(Q)=u^2+Kv^2,\quad
 \mathcal B(Q,h)=uh_1+Kvh_2,\quad
 J_K=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
$$
Let Y be a continuous nearby moving field and h a full moving
direction. The exact conservative equation N.2 gives
$$
 [DF(Q_0+Y)-DF(Q_0)]h
                     =\partial_\phi a_Y(h)+b_Y(h),        \tag{P.11}
$$
where
$$
\begin{split}
a_Y(h)={}&-\beta\{2I_\phi\mathcal B(Y,h)Q_0
 +2I_\phi\mathcal B(Q_0,h)Y
 +2I_\phi\mathcal B(Y,h)Y\\
 &\hspace{33mm}
 +I_\phi[2\mathcal B(Q_0,Y)+S(Y)]h\}\\
 &+\gamma\{\langle h_2\rangle_\phi J_KY
                         +\langle Y_2\rangle_\phi J_Kh\},
\end{split}                                               \tag{P.12}
$$
$$
\begin{split}
b_Y(h)=-\beta\{&
 \langle2\mathcal B(Q_0,Y)+S(Y)\rangle_\phi h
 +2\langle\mathcal B(Y,h)\rangle_\phi Q_0\\
 &+2\langle\mathcal B(Q_0,h)\rangle_\phi Y
 +2\langle\mathcal B(Y,h)\rangle_\phi Y\}.
\end{split}                                               \tag{P.13}
$$
All means in these formulas are moving means. In physical products
they are Pi0, and every I_phi is I0. Neither is replaced by an
unweighted physical mean.

Equations (P.3), (P.6), and (P.11)--(P.13) express the complete
conjugated nearby-body perturbation as
$$
 \mathcal V_Yx
       =\partial_\theta\{M\widehat{a_Y(\mathcal Hx)}\}
                    +\mathcal O_Yx,                      \tag{P.14}
$$
$$
 \mathcal O_Yx=
 W_\theta\langle C\widehat{a_Y(\mathcal Hx)}_2\rangle_\theta
       +P\widehat{b_Y(\mathcal Hx)}
                    -W_\theta E_{b_Y(\mathcal Hx)} .
$$
Here a_Y(Hx) means that the moving h has the physical pullback Hx.
This notation never composes an arbitrary x with a changing angle.
There is no Y_r or h_r in VY.

## 5. A fully stated fixed-port perturbation criterion

Let Go,Gd be the fixed-centre moving-body cap inverse, written in
physical x variables, for ordinary sources and divergence potentials.
Its exterior rows are the same fixed complete linear rows as in the
base theorem. The reference radial gauge and its true residual
Hessian are already part of this inverse.

The actual all-mode gains, the long B0 closure and the Hessian
resolvent imply the conservative inequalities
$$
 \|G_o\|<64,\qquad \|G_d\|<128 .                           \tag{P.15}
$$
Indeed the original closed gains are less than 23 and 42; the product
of the additional factors (1-2^-46)^-1 and (1-1/64)^-1 is less than 2.
The actual reflection bridge identifies this inverse with the
original moving equation on its odd/even sector.

All coefficient norms in the rest of this section are the same
fixed-angle joint Wiener norms on the entire cap. The paid table gives
$$
 \|Q_0\|<6,\quad \|\mathcal H\|<64,\quad
 \|P\|<1/3,\quad \|M\|<1/3,\quad
 \|W_\theta\|<1/16,\quad \|C\|<1/3,\quad \|E_f\|<\| \widehat f_2\|/8.
 \tag{P.16}
$$
For the last bound use the zero unweighted mean of I_theta(C f2).
The normalization gives mean(mC)=1 and the paid G.23 bound gives
||mC-1||<1/32. Thus the rank term in (P.2) is bounded using
(mC-1), and ||E_f||< (33/32)||C|| ||hat f2||/4 <||hat f2||/8.
Thus ||D Psi0 f||<||hat f||/2 in these physical coordinates.
The bound for H is obtained from the same complete multiplier formula
(P.3), not by converting a moving l2(sup_r) norm. Explicitly,
||S'||<36+6/32, ||pc||<(65/128)||c||, and
||vW_theta||<3/8, whose complete product gives the displayed bound.

Write
$$
 b_*=\sup_I|\beta|,\quad g_*=\sup_I|\gamma|,\quad
 k_*=\max(1,\sup_I|K|),\qquad
 \varepsilon=\|\widehat Y\|_{\mathscr A_0,\mathrm{pair}}\le1 .
$$
No numerical full-cap values for b*,g*,k* are inferred from a root
germ. They are the displayed finite actual-coefficient suprema.
From (P.10)--(P.13), with h expressed physically, one has
$$
 \|\widehat{a_Y(h)}\|_{\mathfrak M}
    \le k_*\{b_*(72\varepsilon+6\varepsilon^2)
                                +4g_*\varepsilon\}\|\widehat h\|_{\mathfrak M},
$$
$$
 \|\widehat{b_Y(h)}\|_{\mathfrak M}
    \le b_*k_*(72\varepsilon+6\varepsilon^2)
                                      \|\widehat h\|_{\mathfrak M}.
 \tag{P.17}
$$
For example the four primitive terms cost, in their displayed order,
24 eps, 24 eps, 4 eps^2, and 24 eps+2 eps^2, times b*k*.
The mean terms have the same complete upper sum. Both mean-rank
gamma terms are included.

The exact body length is 89/40, with square root less than 3/2.
If A and B denote the two right sides in (P.17), (P.6) yields a
divergence potential of norm at most A/3 and an ordinary L2_r L2_theta
source of norm at most A/32+3B/4.
Consequently
$$
 \|\mathcal K_Yx\|_{\mathfrak M}
 :=\|(G_d,G_o)\mathcal V_Yx\|_{\mathfrak M}
 <64(A+B)
 \le 2^{20}k_*(b_*+g_*)\varepsilon\|x\|_{\mathfrak M}.
 \tag{P.18}
$$
Here the factor H<64 has been included in the last inequality.

In particular, the explicit sufficient condition
$$
 \|\widehat Y\|_{\mathscr A_0,\mathrm{pair}}
       \le {2^{-22}\over k_*(1+b_*+g_*)}                  \tag{P.19}
$$
gives ||KY||<1/4. The original fixed-port linear cap then has the
complete nearby-body inverse (I-KY)^-1 G0, with factor at most 4/3.
All Fourier modes, independent source columns, original jumps and
both mean equations remain.

This assertion freezes the linear boundary rows. If a genuine changed
boundary operator contributes a further solved lift KB,Y, its exact
same-space norm must be added to (P.18). The sufficient condition
||KY||+||KB,Y||<1 is the full boundary criterion. Uniform bounds on
two separate boundary operators do not alone bound their difference.

## 6. Why a new residual or a radial derivative of Y is unnecessary here

Put L0=partial_r-DF(Q0) and
LY=partial_r-DF(Q0+Y), on the actual reflection sector.
For x=D Psi0 h, the reference covariance is
$$
 L_{\rm phys,0}x=D\Psi_0(L_0h)+H_{R_0}x .
$$
Thus LYh=f gives exactly
$$
 L_{\rm phys,0}x
       =D\Psi_0 f+H_{R_0}x+D\Psi_0([DF(Q_0+Y)-DF(Q_0)]h).
 \tag{P.20}
$$
The reference Hessian term is the already paid H_R0, and the last
term is (P.14). One never changes the gauge to Psi(Q0+Y), so no
R_Y=Q0,r+Y_r-F(Q0+Y) is introduced into this argument.
This is an identity at a nonsolution centre, not an assumption that
either centre solves the PDE.

Q0 and D Psi0 are continuous at the accepted repaired interfaces.
Hence the same transformed affine jumps are retained, with both mean
components. Piecewise coefficient derivatives are not replaced by
zero jumps. A changed nonlinear boundary or material port is still a
separate true row, as in (P.19).

## 7. Exact metric columns and nonlinear use

For completeness, the exact compact metric change in N.15--N.16 is
affine in Delta K, Delta gamma and Delta p, with p=gamma K.
At a complete Q=(u,v), define
$$
 J_\Delta=\begin{pmatrix}0&\Delta p\\-\Delta\gamma&0\end{pmatrix}.
$$
Its full Jacobian change is partial_phi a_nu+b_nu, where
$$
 a_\nu(h)=
 -\beta\Delta K\{2I_\phi(vh_2)Q+I_\phi(v^2)h\}
       +\langle h_2\rangle_\phi J_\Delta Q
                          +\langle v\rangle_\phi J_\Delta h,
$$
$$
 b_\nu(h)=
 -\beta\Delta K\{2\langle vh_2\rangle_\phi Q
                               +\langle v^2\rangle_\phi h\}.
 \tag{P.21}
$$
The change in p is the actual one; it is not K Delta gamma alone.
Formula (P.6) applies without a new radial differentiation. On this
cap the original nu bump is identically zero, so (P.21) is exactly zero.
On its negative-body support the identities remain true, but the
positive-cap bounds (P.15) are not transferred there.

The complete nonlinear state remainder N.4--N.6 likewise has the
same source form partial_phi a+b and therefore obeys (P.6).
Polarization of (P.12)--(P.13) gives its full local Lipschitz budget
when its coefficients are controlled in the displayed joint Wiener
ball. This is a useful source-domain criterion; it does not assert
that an arbitrary M output lies in that coefficient algebra.

The supplied full-real-delta positive result bounds delta Z in its
stated row norms. To instantiate (P.19) on a specific interval one
must pay the corresponding joint coefficientwise suprema and the
fixed-angle composition on that actual interval. A finite polynomial
degree does not permit replacing sup_r sum_k by sum_k sup_r.
The whole |delta|<=1e-8 interval is not granted by (P.19) without that
consumption.

The completed item is the exact conservative source transport,
the full nearby Jacobian representation and a fully specified
fixed-port cap inverse criterion. It leaves a concrete coefficient
budget, changed true boundary rows and the global nonlinear domain
for the continuing proof.
