# R133 supplement: the exact good tangent for an unknown outer angle

2026-11-15, visible-exact-astra-0df9.

**Proved identities, including both curvature means and the boundary gauge.**
This note varies the real degree-one outer angle itself. The variation is
handled by an exact good tangent, not by assigning a bounded derivative to
a raw composition operator on one Sobolev space. There is no new numerical
calculation or new inverse theorem here.

The background is a genuine sufficiently regular real field in the stated
neighborhood of the explicit family, with the same intrinsic parameters.
The long coordinate change is independent of its radial variable. The
complete moving equations, the two curvature means, holonomy, and the
constant height gauge remain separate. In particular a raw pulled height
tangent need not have the regularity of its good tangent.

The fixed-angle objects and the true long graph are those of
[T.1--T.25](R133-supplement-full-delta-fixed-angle-regular-graph-analytic-translation.md).
The complete gauge is
[G.1--G.5](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md);
the frozen old-angle mean and primitive are
[P.8--P.9](R133-supplement-fixed-base-conservative-source-transport-and-nearby-cap-linearization.md).
All formulas below use the same normalized circle measure and the full
fourfold Fourier space. Reflection can be imposed afterwards.

## 1. The actual angle, its phase, and its admissible variation

Write the fixed reference physical angle as $x=\theta_0$ and its inverse
moving-angle map as $\varphi=\Phi_0(x)$. Set
$$
 \omega_0=\Phi_{0,x}>0,\qquad
 \Pi_0 f=\langle\omega_0 f\rangle_x,\qquad
 \mathcal I_0f=(I_\varphi(f\circ\Theta_0))\circ\Phi_0 .
 \tag{U.1}
$$
Thus $\langle\omega_0\rangle_x=1$, $\Pi_0\mathcal I_0=0$, and
$\partial_x\mathcal I_0f=\omega_0(f-\Pi_0f)$.
These are the complete fixed operators of P.8; in particular $\Pi_0$
is not an ordinary $x$ mean.

Let $\widehat Q=(\widehat u,\widehat v)=Q\circ\Phi_0$ at the actual outer
endpoint, and put
$$
 m=\Pi_0\widehat v<0,\qquad
 \tau=\Theta_Q\circ\Phi_0,\qquad
 j=\tau_x={\omega_0\widehat v\over m}>0,\qquad
 \langle j\rangle_x=1 .
 \tag{U.2}
$$
The physical angle is fixed by
$\Theta_Q(\varphi)=\varphi+I_\varphi(v/m-1)$, with the original zero
moving mean. Extend this same $\tau$ and $j$ to all long radii $t$,
without any $t$ dependence.

For a moving variation $H$ put $\widehat H=H\circ\Phi_0$ and use a dot
for differentiation in its variation parameter. Then
$$
 \dot m=\Pi_0\widehat H_2,\qquad
 \dot j={\omega_0\over m}
       \left(\widehat H_2-{\widehat v\dot m\over m}\right),
 \tag{U.3}
$$
$$
 \eta:=\dot\tau=
 \mathcal I_0\left({\widehat H_2\over m}
              -{\widehat v\dot m\over m^2}\right),\qquad
 \eta_x=\dot j,\qquad \Pi_0\eta=0 .
 \tag{U.4}
$$
Here $\eta$ is an angular displacement, not a variation of the fixed
intrinsic parameter $\eta_0$. The input to $\mathcal I_0$ in (U.4)
has exactly zero $\Pi_0$ mean. Consequently (U.4) determines the
actual phase; it cannot be replaced by an arbitrarily chosen zero
ordinary mean primitive.

More generally the identities below hold for any real degree-one
family $\tau$, with its actual phase retained, satisfying
$\dot j=\eta_x$ and $\eta_t=j_t=0$. Put
$$
 b={\eta\over j},\qquad D_j=j^{-1}\partial_x,\qquad
 \dot F^{\,g}:=\dot F-bF_x .
 \tag{U.5}
$$
The superscript $g$ always denotes this good tangent to a pulled
physical scalar or vector. It is not an additional change in the
underlying physical field.

## 2. Exact commutation, including the weighted mean and primitive

Direct differentiation gives
$$
 \dot{(D_jF)}=D_j\dot F-{\eta_x\over j^2}F_x
            =D_j\dot F^{\,g}+b\,\partial_x(D_jF).
 \tag{U.6}
$$
Indeed $b_x/j+bj_x/j^2=\eta_x/j^2$. Thus
$$
 \bigl(\dot{(D_j^k\partial_t^aF)}\bigr)^g
       =D_j^k\partial_t^a\dot F^{\,g},\qquad a,k\ge0,
 \tag{U.7}
$$
whenever the displayed derivatives exist. The radial assertion uses
$b_t=0$. A radius-dependent angle would create additional terms and
is not covered by this assertion.

Let $M_jF=\langle jF\rangle_x$ and $J_jF=F-M_jF$. Periodic integration
by parts, with the actual signed variation $\dot j=\eta_x$, gives
$$
 \dot{(M_jF)}
 =\langle j\dot F+\eta_xF\rangle_x
 =M_j(\dot F-bF_x)=M_j\dot F^{\,g}.
 \tag{U.8}
$$
Therefore
$$
 \bigl(\dot{(J_jF)}\bigr)^g=J_j\dot F^{\,g}.
 \tag{U.9}
$$
No scalar mean has been discarded in this computation.

The true physical zero-mean primitive in fixed $x$ is
$$
 I_jF=I_x\{j(F-M_jF)\}
             -M_jI_x\{j(F-M_jF)\}.
 \tag{U.10}
$$
It is uniquely characterized by $D_jI_jF=F-M_jF$ and $M_jI_jF=0$.
Differentiate these two defining equations and use (U.6), (U.8).
Uniqueness of the normalized primitive proves
$$
 \bigl(\dot{(I_jF)}\bigr)^g=I_j\dot F^{\,g}.
 \tag{U.11}
$$
The primitive's varying normalization is part of (U.11); omitting
the second term of (U.10) would in general make (U.11) false.

Multiplication and scalar smooth composition obey the ordinary
Leibniz and chain rules for the good tangent. Hence (U.7)--(U.11)
apply term by term to the complete pulled long equations and their
mean functionals, rather than merely to their principal part.

## 3. The ordinary Fourier chart and the independent mean height

The ordinary-mean-zero chart of T.7 is $y$, with physical zero-mean
height $h^\flat=J_jy$. Define
$$
 z=\dot h^\flat-bh^\flat_x,\qquad
 z_y=P_{\perp,x}(\dot y-by_x).
 \tag{U.12}
$$
Equations (U.8)--(U.9) give exactly
$$
 z=J_jz_y,\qquad M_jz=0,\qquad
 \dot y=z_y+P_{\perp,x}(by_x).
 \tag{U.13}
$$
For example the two apparent scalar corrections cancel as
$-\langle\eta_xy\rangle_x=\langle\eta y_x\rangle_x$.
This is why neither a raw $\dot y$ nor an ordinary-mean-zero
$\dot h^\flat$ may silently replace $z_y$.

If a total physical height also has an independent scalar mean
$a(t)$, its good variation is $z+\dot a(t)$. The constant height
gauge and the original equation recovering $a$ are retained.
Likewise the holonomy scalar below is not set to zero by (U.13).

One should first differentiate the complete physical equation and
only then apply $P_{\perp,x}$ to choose its chart. This ordinary
projection does not by itself commute with the good derivative:
$$
 \bigl(\dot{(P_{\perp,x}F)}\bigr)^g
  =P_{\perp,x}\dot F^{\,g}-\langle bF_x\rangle_x .
 \tag{U.14}
$$
The last term is constant and is accounted for by the true weighted
mean equation. It must not be dropped before that equation is kept.

## 4. Full long linearization and the holonomy small root

Use the complete long variables of T.10:
$$
 P=D_jh^\flat,\quad U=D_j^2h^\flat,\quad
 K_\perp=2h^\flat+h^\flat_t,\quad V=D_jK_\perp,\quad
 K=K_\perp+\kappa(t).
$$
For the good tangent put
$$
 p=D_jz,\quad u=D_j^2z,\quad
 k_\perp=2z+z_t,\quad v=D_jk_\perp,\quad
 k=k_\perp+\dot\kappa .
 \tag{U.15}
$$
These are exactly the good variations of $P,U,K_\perp,V,K$.
There is no separate $\dot j_x$ coefficient left in (U.15).

Write the true removable holonomy equation as
$M_j\mathcal H(q;P,U,K)=0$, where $\mathcal H$ is the complete
integrand of T.12 and $q=w^2$ is fixed here. Then
$$
 0=M_j\{\mathcal H_Pp+\mathcal H_Uu+
                         \mathcal H_K(k_\perp+\dot\kappa)\}.
 \tag{U.16}
$$
Whenever the already required small-root denominator is nonzero,
$$
 \dot\kappa=
 -{M_j(\mathcal H_Pp+\mathcal H_Uu+\mathcal H_Kk_\perp)
        \over M_j\mathcal H_K}.
 \tag{U.17}
$$
This is the actual independent scalar derivative. The formulas use
the removable value at $q=0$ and do not divide by a vanishing $q$.
They neither replace the holonomy equation by an ordinary mean nor
construct a small root outside its verified domain. The original
mean-height equation is differentiated afterwards with this same
$\dot\kappa$ and its unchanged scalar height data.

More generally, if $\mathcal N_j(h^\flat,\kappa)$ is the complete
physical pulled operator, (U.7)--(U.11) give
$$
 \dot{\mathcal N}_j-b\,\partial_x\mathcal N_j
     =\mathcal L_j(z,\dot\kappa).
 \tag{U.18}
$$
For a physical source $f^\flat$, its tangent source is
$\dot f^\flat-bf^\flat_x$. At an off-shell background the residual
satisfies the same exact relation
$$
 \dot{\mathcal R}-b\mathcal R_x
   =\mathcal L_j(z,\dot\kappa)
            -(\dot f^\flat-bf^\flat_x).
 \tag{U.19}
$$
In particular a nonzero residual transport cannot be discarded by
pretending the background solves the equation. If the background
is a true graph point, its zero residual makes that term vanish
for the stated reason.

## 5. Curvature, both physical means, and actual boundary data

At a fixed physical endpoint let the unchanged intrinsic scalars be
$q=w^2$, $E=1+q$, $\chi=w/a$, and define
$$
 D=1-q(2K+K^2+EP^2),\qquad J=1+K+EU .
$$
The true curved outputs are
$$
 B^\flat=\chi(V-P)D^{-1/2},\qquad
 C^\flat=-{\chi\over\sqrt E}JD^{-1/2}.
 \tag{U.20}
$$
With $A=(1+K)k+EPp$, their complete good tangents are
$$
 \dot B^{\,g}
   =\chi\{(v-p)D^{-1/2}+q(V-P)A D^{-3/2}\},
$$
$$
 \dot C^{\,g}
   =-{\chi\over\sqrt E}
                  \{(k+Eu)D^{-1/2}+qJA D^{-3/2}\}.
 \tag{U.21}
$$
Here $\dot D^{\,g}=-2qA$; this fixes the two signs. The full
$\dot\kappa$ occurs in $k$. Both $M_j\dot B^{\,g}$ and
$M_j\dot C^{\,g}$ remain true output rows.

The independent height data at either end transform in the same
way: prescribed pulled height $g^\flat$ has good datum
$\dot g^\flat-bg^\flat_x$, together with its physical scalar mean.
Finite long length, the actual two ends, and all their affine
charges are unchanged.

On the moving cap side the exact same actual outputs are
$$
 W^\flat=(B^\flat,C^\flat)
       =(\widehat u/\widehat v,1/\widehat v)
       =\Psi(Q)\circ\tau .
$$
Let
$$
 P_Q=
 \begin{pmatrix}
 1/\widehat v&-\widehat u/\widehat v^2\\
 0&-1/\widehat v^2
 \end{pmatrix}.
$$
The complete moving differential has the exact fixed-$x$ form
$$
 (\!D\Psi_QH)\circ\tau
      =P_Q\widehat H-\eta D_jW^\flat
      =\dot W^\flat-bW^\flat_x .
 \tag{U.22}
$$
The phase $\eta$ here is (U.4), with its actual moving-mean
normalization. Thus matching (U.21) with (U.22) is precisely the
original physical Jacobi boundary matching. It is not a new
boundary obtained by omitting the angle derivative.

For clarity write $\bar u=\Pi_0\widehat u$. Exact change of measure
gives $M_jB^\flat=\bar u/m$ and $M_jC^\flat=1/m$. Consequently
$$
 M_j\dot B^{\,g}
   ={\Pi_0\widehat H_1\over m}
                -{\bar u\,\Pi_0\widehat H_2\over m^2},
 \qquad
 M_j\dot C^{\,g}=-{\Pi_0\widehat H_2\over m^2}.
 \tag{U.23}
$$
The negative sign of $m$ has not been replaced by $|m|$. These
are the two complete physical curvature means. In the reflection
sector the first vanishes for the actual parity reason; the second
remains an independent scalar row.

Conversely, for complete physical tangent $w=(b_C,c_C)$ in fixed
$x$, set
$$
 p_c=I_j(c_C-mC^\flat M_jc_C),\qquad \eta=-\widehat v\,p_c,
$$
$$
 \widehat H=
 \begin{pmatrix}
 \widehat v&-\widehat u\widehat v\\0&-\widehat v^2
 \end{pmatrix}
                  (w-\widehat v D_jW^\flat p_c).
 \tag{U.24}
$$
This is G.5 pulled to fixed $x$, with the entire primitive mean
restored. It satisfies $\Pi_0\eta=0$: indeed
$\Pi_0(\widehat v p_c)=mM_jp_c=0$.
Thus the forward and inverse boundary gauges use the same true
phase, rather than adding a new free angle constant.

For mismatched nonlinear boundary values, the good derivative of
their difference retains the corresponding
$-b\,\partial_x(\text{boundary residual})$. At an exact matching
point both sides have the same transport, which cancels. Neither
observation deletes a nonzero boundary residual in an iteration.

## 6. Sobolev meaning and the precise remaining obligations

All identities can first be proved for smooth real fields and then
extended using ordinary one-dimensional Sobolev product and
primitive estimates, on a set with fixed positive lower bounds for
$j$, $|m|$, $|\widehat v|$, and the actual long denominator $D$.
One can safely use backgrounds with four more angular derivatives
than the direction. In particular a stated background $H^{8196}$
buffer is compatible with direction orders $1\le s\le8192$,
provided the corresponding radial and endpoint norms in the long
state domain are also retained. This is a sufficient regularity
statement, not a numerical bound for a nearby inverse.

For $\widehat H\in H^s$, the fixed primitive in (U.4) gives
$\eta\in H^{s+1}$, and (U.22) gives a curvature tangent in $H^s$,
with bounds depending on those background norms and lower bounds.
There is no derivative of $\widehat H$ hidden in the phase term.
The same holds for the complete scalar rows in (U.23).

The strong good-height space is the shifted version of T.8:
height $H^{s+2}$, one radial derivative $H^{s+1}$, and two radial
derivatives $H^s$, with the original coefficientwise radial
supremum and independent scalar data. Denote it by $\mathcal Y_s$.
A genuine inverse for the good equation may take values in
$\mathcal Y_s$. This fact does **not** imply
$\dot h^\flat\in\mathcal Y_s$ at unchanged input order, because
$$
 \dot h^\flat=z+b h^\flat_x
 \tag{U.25}
$$
and the cap direction only gave $b\in H^{s+1}$. For a nonconstant
smooth background this transport term generally has only
$H^{s+1}$ angular regularity. Increasing the background regularity
cannot supply a missing derivative of the direction itself.

Accordingly one must either use the actual good tangent and its
phase as the tangent chart, or require extra angular regularity
of the cap input to reconstruct a raw pulled height in the
unshifted strong space. An input buffer of two or four derivatives
is a safe option for that reconstruction when accompanied by its
explicit tame estimates. It cannot be replaced by an unsupported
same-space claim about raw composition.

Finally these exact tangent identities do not provide the new
energy estimate for an unknown-background outer row, for example
a required $H^{1/2}\to H^{-1/2}$ relative radial bound with all
mean and Poisson columns. Nor do they assert a nonlinear nearby
graph exists, that its complete residual lies in a Newton ball,
or that a high-frequency or parameter Schur complement is solved.
Those are separate estimates on the complete equations whose
angle, means, and boundary units are fixed here.
