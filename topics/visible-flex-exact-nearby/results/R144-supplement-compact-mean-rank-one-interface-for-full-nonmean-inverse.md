# R144 supplement: compact mean control, its exact low source and the full nonmean interface

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved at the actual fixed-metric compact centre.** The terminal
mean-control column vanishes identically after \(r=9/50\). Its full
physical moving Gauss--Codazzi body source has angular degree at most
96, and every original transmission column has degree at most 32.
Thus it supplies no direct high body source and no direct positive
body or positive endpoint observation. These are support identities
for the complete physical differential, not for a density-divided
equation.

The two-endpoint scalar elimination changes the remaining equations
by one exact rank-one term. The corresponding coordinate direction
must be removed from the independent shape variables. If it is not
removed, the apparent full control Schur denominator is identically
zero, even though the already proved scalar waist pivot is positive.
The genuine remaining physical parameter and phase pairings are
identified below. No new numerical inverse or complete Schur gate
is asserted.

## 1. The same compact centre and its physical control column

Use exactly the centre, fixed intrinsic \(\eta_0,\nu_0\), raw moving
circle, and original pieces of
[SR](R144-supplement-sharp-compact-root-from-completed-forward-mean.md)
and
[MJ](R144-supplement-compact-terminal-mean-Jacobian-and-two-endpoint-inverse.md).
Write

$$
 Q_*=(u,v_*),\qquad v_*=m_*j_*,\qquad
 j_*=1+\lambda_*\frac wm,\qquad
 \lambda_*=1+\xi_*\chi,\qquad w=v-m.
 \tag{RI.1}
$$

Here \(m,w,u\) are the original raw quantities; \(m_*\) is the exact
terminal mean at the already identified compact root \(\xi_*\).
The radial scalar \(m_*\) is continuous. The remaining raw nonmean
joins are retained. In particular \(Q_*\) has moving Fourier degree
at most 32, even though it is not asserted to solve the full
nonmean equations.

Let \(r_c=\partial_\xi m^t_\xi|_{\xi_*}\), with **fixed terminal
value**, as in MJ.21. Its physical state column is

$$
 h_c=(0,c),\qquad
 c=j_*r_c+\frac{m_*}{m}\chi w
   =r_c+(\lambda_*r_c+m_*\chi)\frac wm .
 \tag{RI.2}
$$

Thus \(\langle c\rangle=r_c\). The exact scalar equation is

$$
 L_*r_c=f_c,\qquad r_c(R)=0,\qquad [r_c]_i=0,\qquad
 f_c=-2\beta K m_*^3\chi\lambda_*\frac{\langle w^2\rangle}{m^2}.
 \tag{RI.3}
$$

The already proved waist pivot is

$$
 \kappa_0=r_c(0),\qquad 0.002415<\kappa_0<0.002469.
 \tag{RI.4}
$$

This is the terminal-graph derivative. The forward family has
fixed waist mean and zero control derivative at the waist; it is
not substituted into (RI.2)--(RI.4).

Since \(\chi\) and \(f_c\) vanish for \(r\ge9/50\), uniqueness of
the homogeneous scalar terminal problem, with all zero response
jumps, gives

$$
 r_c(r)=0,\qquad h_c(r,\phi)=0
              \quad(9/50\le r\le R).
 \tag{RI.5}
$$

This does not assert vanishing before \(1/20\): there \(r_c\) is
generally a nonzero homogeneous mean response. In particular its
nonzero waist value is consistent with (RI.5).

## 2. The complete physical differential, including the control derivative

Keep the original fixed metric, and use
[D.3--D.4](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)
with \(Q=Q_*\). Define

$$
 I=\partial_\phi^{-1}P_{\ne0},\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad
 S_*=u^2+Kv_*^2,\quad d_*=-\beta I S_*.
$$

The full physical moving operator is
\(\mathcal D_*=\partial_r-A_*\), where

$$
 \begin{aligned}
 A_*h={}&(d_*I_2+\gamma m_*J(K))h_\phi+L_*^{\,\mathrm{mat}}h\\
 &-2\beta (Q_*)_\phi I(uh_1+Kv_*h_2)
       +\gamma\langle h_2\rangle J(K)(Q_*)_\phi ,
 \end{aligned}
 \tag{RI.6}
$$

$$
 L_*^{\,\mathrm{mat}}=
 \begin{pmatrix}
 -\beta(1+3u^2+Kv_*^2)&-2\beta Kuv_*\\
 -2\beta uv_*&\beta(1-u^2-3Kv_*^2)
 \end{pmatrix}.
$$

The symbol \(L_*^{\,\mathrm{mat}}\) in (RI.6) is the local matrix,
not the scalar mean operator \(L_*\) in (RI.3).
Substitution of the complete physical column (RI.2) gives, on every
open original piece,

$$
 \begin{aligned}
 (\mathcal D_*h_c)_1
  ={}&-\gamma K(m_*c_\phi+r_c(v_*)_\phi)
       +2\beta K\{uv_*c+u_\phi I(v_*c)\},\\
 (\mathcal D_*h_c)_2
  ={}&c_r-d_*c_\phi-\beta(1-u^2-3Kv_*^2)c\\
     &+2\beta K(v_*)_\phi I(v_*c)+\gamma r_cu_\phi .
 \end{aligned}
 \tag{RI.7}
$$

In particular the last terms coming from the varying angular mean
in (RI.6) have not been deleted. The derivative \(c_r\) contains

$$
                  \frac{m_*+\xi_*r_c}{m}\chi'w.
 \tag{RI.8}
$$

All other product derivatives of (RI.2) also remain in \(c_r\).
The leading coefficient \(m_*/m\) in (RI.8) is not small with
\(\xi_*\). Dividing the density equation by \(m_*\) and bounding
only the resulting coefficient of \(\chi'\) would not be the
physical source (RI.7).

The angular mean of the second line is exactly zero:

$$
                 \langle(\mathcal D_*h_c)_2\rangle=0.
 \tag{RI.9}
$$

Indeed the full nonlinear mean identity is
\(m'=\beta m(1-\langle u^2\rangle-Km^2\langle j^2\rangle)\).
Its derivative along (RI.2) is precisely (RI.3). This proof uses
the exact mean equation for the compact centre, not the false
assertion that all of \(Q_*\) is a Gauss--Codazzi solution.

### Exact angular support

Every factor \(u,v_*,c\) in (RI.7) has degree at most 32.
Radial or angular differentiation, taking the mean, and \(I\)
preserve this support bound. The products \(S_*,v_*c\) have degree
at most 64. Every product in (RI.7) therefore has degree at most
96, including \(u_\phi I(v_*c)\), \((v_*)_\phi I(v_*c)\) and
\(d_*c_\phi\). Consequently

$$
 P_{\ge97}\mathcal D_*h_c=0,\qquad
 P_{\le96}\mathcal D_*h_c=\mathcal D_*h_c.
 \tag{RI.10}
$$

This is an exact identity on the raw moving circle, with physical
frequencies \(4j\). The low vector has the original odd96,
moving-even-mean, even96 order; its middle body component vanishes
by (RI.9). No truncation or neglect of a tail is involved.

The assertion concerns the full physical \(\mathcal D_*\), before
any density division or physical-angle composition. An inverse
response to this finite source can have arbitrarily high
frequencies. No support assertion about that response follows
from (RI.10).

## 3. Every original join and the two different meanings of atom

At an original raw interface \(r_i\), continuity of
\(m_*,r_c,\lambda_*,\chi\) gives the exact physical jump

$$
 [h_c]_i=
 \left(0,\,
  (\lambda_*(r_i)r_c(r_i)+m_*(r_i)\chi(r_i))
                       \left[\frac wm\right]_i\right).
 \tag{RI.11}
$$

It has zero angular mean and degree at most 32. It need not
vanish at the negative raw joins. Thus the complete control
column consists of (RI.7), every (RI.11), and the original
boundary and other functional rows applied to \(h_c\). An
ordinary radial \(L^2\) source norm cannot receive (RI.11) as
zero-cost data.

In a weighted raw-state chart \(x=S h\), the same physical
transmission is, exactly,

$$
 x^+-S^+(S^-)^{-1}x^-=S^+[h]_i .
 \tag{RI.12}
$$

This retains the original change of weights once. A different
original trace chart must use its own actual transformation,
not replace its transmission matrix by the identity.

The 193 atoms of
[R141, G.5](R141-low193-directed-green-and-complete-observation-certification.md)
are **endpoint observations**, not the interior source jumps
(RI.11). Both objects remain in the complete interface and must
not be confused.

The original positive interval lies beyond the compact support,
as in
[the selected-family root theorem, Section 1](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md).
Therefore (RI.5) gives zero direct control contribution to all
three positive observations

$$
 \mathcal O h=
 \bigl(Sh_L,\ R_a h_L(a),\ \Theta R_bh_L(R)\bigr),
 \qquad \mathcal O(h_c|_{[a,R]})=0,
 \tag{RI.13}
$$

where \(R_a\) takes root odd96 and the independent moving mean,
\(R_b\) takes outer even96, and
\(\Theta_j=(1+16j^2)^{-5/12}\). The original mixed boundary
inputs \(h_L^e(a)\) and
\((h_L^o+p_0h_L^e,h_L^m)(R)\), \(p_0=13/80\), also receive
zero directly from \(h_c\).

All local outer state and state-jet functionals of this column
vanish. A phase, height or position functional defined by an
integral through the negative interval need not vanish. Such a
functional must be applied to (RI.2) with its original complete
definition. In particular zero outer curvature variation does
not prove zero variation of a reconstructed position.

## 4. The terminal graph as a source and observation map

Let \(z=(p,\eta)\) be an uncontrolled shape variation in the
original reflection class, with \(\langle\eta\rangle=0\).
Retain the units \(\delta j=\eta/m\) of MJ.16. Define

$$
 B_{\mathrm{shape}}z
 =-2\beta m_*\langle up\rangle
  -2\beta K m_*^3\lambda_*\frac{\langle w\eta\rangle}{m^2}.
 \tag{RI.14}
$$

Let \(T_*\) be the complete actual scalar terminal inverse with
zero mean-response jumps. For this paragraph the terminal mean
variation is zero. Put

$$
 Rz=T_*B_{\mathrm{shape}}z,\qquad
 \sigma z=(Rz)(0),\qquad
 \mathcal Jz=\left(p,j_*Rz+\frac{m_*}{m}\eta\right).
 \tag{RI.15}
$$

For independent scalar body data, actual mean jumps and a
terminal mean port \(b_R\), write

$$
 r_f=T_*(f_m,k,b_R),\qquad h_f=(0,j_*r_f).
 \tag{RI.16}
$$

Here the notation \(T_*(f_m,k,b_R)\) means the complete solution
with those prescribed data, not the zero-terminal operator
applied to a body function. The full mean-eliminated physical
state is \(\mathcal Jz+h_f\).

The actual physical outer-density mean equation has not been
identified with \(b_R=0\). If that equation makes \(b_R\) depend
on unknown outer shape, its true scalar port remains an unknown
in (RI.16), with the original physical matching row retained.
Alternatively its already justified exact chart can be composed
with (RI.15). The moving mean and the physical-density mean are
not the same row.

These definitions admit a precise ordinary \(L^2\) pairing
without taking an \(L^2\) trace. With
\(H_*(r,s)=\exp\int_s^r a_*(t)\,dt\), one has

$$
 \begin{aligned}
 \sigma z
 &=\int_0^R\bigl[
   \left\langle a_p(s),p(s)\right\rangle_\phi
       +\left\langle a_\eta(s),\eta(s)\right\rangle_\phi
                         \bigr]\,ds,\\
 a_p&=2H_*(0,s)\beta m_*u,\\
 a_\eta&=2H_*(0,s)\beta K m_*^3\lambda_*\,w/m^2 .
 \end{aligned}
 \tag{RI.17}
$$

The sign follows from the terminal formula
\(T_*F(0)=-\int_0^R H_*(0,s)F(s)\,ds\).
The coefficients in (RI.17) are bounded on the finitely many
pieces and thus in radial-angular \(L^2\). This gives the exact
dual row in that space. It reads only the first 32 angular
labels. Its useful numerical \(L^2\) norm is a separate
receiver; MJ's \(0.087\) has radial \(L^\infty\) input and
must not be reused as this \(L^2\) norm.

There is also an explicit raw physical body load. For
\(h=\mathcal Jz\), the inverse coordinate identity is
\(p=h_1\) and
\(\eta=(m/m_*)(h_2-j_*\langle h_2\rangle)\). Thus put

$$
 a_{\mathrm{phys},1}=a_p,\qquad
 a_{\mathrm{phys},2}=\frac m{m_*}
       \bigl(a_\eta-\langle a_\eta j_*\rangle\bigr).
 \tag{RI.17a}
$$

Then \(\sigma z=\int_0^R\langle a_{\mathrm{phys}},h\rangle\,ds\).
The subtracted scalar in (RI.17a) is the genuine moving-mean
slot; it cannot be omitted. This load still has degree at most
32, and it annihilates the independent pure mean reconstruction
\((0,j_*r_f)\) pointwise. Consequently the same identity applies
to \(h=\mathcal Jz+h_f\).

For the WVC weighted raw state \(x=Sh_L\), the corresponding
load is exactly \(S^{-T}a_{\mathrm{phys}}\) on the positive
interval. The negative part retains its original state
coordinates. These are volume pairings on the two intervals;
a mean trace is not taken directly from an arbitrary weighted
body \(L^2\) vector.

Mean-source jumps in (RI.16) contribute exactly
\(-\sum_i H_*(0,r_i)k_i\) to \(r_f(0)\), and the terminal
port contributes \(H_*(0,R)b_R\). These affine terms remain in
the same waist right side below.

## 5. Exact rank-one elimination and its required shape slice

Let \(\mathcal N\) denote the **actual retained nonmean and
physical rows** of the problem under consideration. It includes
the nonmean body, all nonmean transmissions, the retained waist
and physical outer rows, and any retained phase or height rows.
Any row temporarily treated as an output must be named and
recovered as that same physical row. No row is removed merely
to make a matrix square.

Set

$$
 B=\mathcal N\mathcal J,\qquad b_c=\mathcal N h_c.
 \tag{RI.18}
$$

After moving the complete affine data (RI.16) to the right,
the controlled equations and the desired waist mean \(b_0\)
are exactly

$$
 Bz+b_ct=y,\qquad
 \sigma z+\kappa_0t=g,\qquad
 y=f_{\mathcal N}-\mathcal Nh_f,\quad
 g=b_0-r_f(0).
 \tag{RI.19}
$$

Thus scalar elimination gives

$$
 \left(B-\frac{b_c\otimes\sigma}{\kappa_0}\right)z
       =y-\frac{b_c}{\kappa_0}g,\qquad
 t=\frac{g-\sigma z}{\kappa_0}.
 \tag{RI.20}
$$

The rank-one range vector is the complete tuple \(b_c\),
including (RI.7), (RI.11) and all retained functional rows.
It is not just the derivative of the scalar mean equation.

However, the representation with unrestricted \(z\) is
redundant. Let

$$
 z_c=(0,\chi w).
$$

By (RI.14) and (RI.3),

$$
 Rz_c=r_c,\qquad \sigma z_c=\kappa_0,\qquad
 \mathcal Jz_c=h_c,\qquad Bz_c=b_c.
 \tag{RI.21}
$$

Consequently the operator in (RI.20) kills \(z_c\) identically.
Its zero direction represents the zero physical variation:
\((z,t)=(z_c,-1)\) gives
\(\mathcal Jz+t h_c=0\).

Use the already defined bounded functional

$$
 \ell(\eta)=\sigma(0,\eta)/\kappa_0,\qquad
 X_\perp=\{(p,\eta):\ell(\eta)=0\}.
 \tag{RI.22}
$$

Then \(\ell(\chi w)=1\), and every uncontrolled shape decomposes
uniquely as \(z=z_\perp+\ell(\eta)z_c\).
The true independent variables in (RI.19) are
\((z_\perp,t)\in X_\perp\times\mathbb R\). On that slice the
eliminated operator is exactly

$$
 K_\perp=B|_{X_\perp}
         -\frac{b_c\otimes(\sigma|_{X_\perp})}{\kappa_0}.
 \tag{RI.23}
$$

All other independent physical variables and their original
equations must remain alongside (RI.23).
The internal density control is a state coordinate; adding it
while retaining unrestricted \(\eta\) does not add a physical
degree of freedom.

## 6. Which Schur denominator actually has to be nonzero

The positive lower bound (RI.4) proves the scalar graph and
coordinate elimination. It is not a full coupled inverse test.
There are two useful exact forms, depending on the already
chosen full complement.

First, if an actual square complement
\(A=B|_{X_\perp}:X_\perp\to Y\) has been proved invertible with
its declared original row set, then the block system

$$
 \begin{pmatrix}A&b_c\\\sigma&\kappa_0\end{pmatrix}
 \binom{z_\perp}{t}=\binom yg
$$

is invertible if and only if

$$
 \Delta_c=\kappa_0-\sigma A^{-1}b_c\ne0.
 \tag{RI.24}
$$

Indeed put \(u_c=A^{-1}b_c\), \(z_y=A^{-1}y\). The unique
solution, when (RI.24) holds, is

$$
 t=\frac{g-\sigma z_y}{\Delta_c},\qquad
 z_\perp=z_y-u_ct.
 \tag{RI.25}
$$

Conversely if \(\Delta_c=0\), the nonzero coordinate pair
\((-u_c,1)\) is a kernel vector of this block system. This
proves necessity as well as sufficiency. An enclosure separating
the signed scalar \(\Delta_c\) from zero suffices; the stronger
condition \(|\sigma A^{-1}b_c|<\kappa_0\) is only one possible
way to prove it.

The prerequisite that \(A\) have that square row set matters.
Restricting an invertible unrestricted \(B\) to the codimension
one space \(X_\perp\), without changing the original retained
row or parameter count, does not produce such an \(A\). This
theorem does not authorize removing an extra physical equation.

Second, suppose the available actual complement inverse is the
unrestricted \(B^{-1}\). In that case (RI.21) gives the exact
identity

$$
 \boxed{\quad
 \kappa_0-\sigma B^{-1}b_c=0 .
 \quad}
 \tag{RI.26}
$$

There is no numerical control pairing to certify away from
zero in (RI.26). A new internal coordinate cannot repair a
missing physical compatibility condition.

For a genuine external parameter \(\nu\), write its complete
mean-eliminated equations, in one consistent source sign
convention, as

$$
 Bz+g_\nu\dot\nu=y,\qquad
 \sigma z+d_\nu\dot\nu=g.
 \tag{RI.27}
$$

The mean body source, its terminal and jump data, the nonmean
metric source, and all boundary/reference parameter terms are
included when constructing \(g_\nu,d_\nu\). In particular the
mean source
\(-\beta m_*^3J_*\partial_\nu K\) from MJ.17 is retained, with
\(J_*=\langle j_*^2\rangle\).
Then the genuine Schur scalar for this specified waist row is

$$
 \Delta_\nu=d_\nu-\sigma B^{-1}g_\nu,
 \tag{RI.28}
$$

and the solution is

$$
 \dot\nu=\frac{g-\sigma B^{-1}y}{\Delta_\nu},
 \qquad z=B^{-1}y-(B^{-1}g_\nu)\dot\nu .
 \tag{RI.29}
$$

This is a sufficient and necessary criterion for (RI.27), with
the same proof as (RI.24)--(RI.25). Neither \(\kappa_0>0\) nor
the small selected value of \(\xi_*\) supplies (RI.28).

The original remaining physical row may instead be the actual
fourth Robin row, an independent phase row, or a prescribed
height functional. It must then use its own complete row
\(\sigma_b\) and direct column \(d_{b,\nu}\), giving
\(d_{b,\nu}-\sigma_bB^{-1}g_\nu\). The waist row in (RI.28)
cannot be substituted for it without a proved equality of the
complete row systems. This retains the original true parameter
and physical-output conventions of
[the mean-eliminated Schur theorem](R133-supplement-exact-mean-elimination-full-adjoint-and-nu-Schur.md).
For several genuine parameters and independent output rows the
same substitution gives the finite matrix
\(D-\Sigma B^{-1}G\), with all its rows and columns retained.

## 7. Minimal future pairings and all body/193-observation responses

Equations (RI.24)--(RI.29) specify the required computations
without declaring the absent full nonmean inverse available.
For a legitimate sliced square complement \(A\), only one
control response \(u_c=A^{-1}b_c\) and one pairing
\(\sigma u_c\) enter its scalar denominator. For an unrestricted
complement \(B\), the internal control response is already the
exact identity \(B^{-1}b_c=z_c\); the needed new column is the
**genuine parameter response** \(u_\nu=B^{-1}g_\nu\), and its
pairings with every original remaining physical row.

For example, in (RI.25) the complete physical state is

$$
 h=h_f+\mathcal Jz_y+
          (h_c-\mathcal Ju_c)
          \frac{g-\sigma z_y}{\Delta_c}.
 \tag{RI.30}
$$

Consequently for every declared body or endpoint observation
\(\mathcal O_J\),

$$
 \mathcal O_Jh=
 \mathcal O_J(h_f+\mathcal Jz_y)
 +\mathcal O_J(h_c-\mathcal Ju_c)
          \frac{g-\sigma z_y}{\Delta_c}.
 \tag{RI.31}
$$

This one formula retains the WVC body, root97, outer96 and
joint193 receivers when the full actual solution has been
connected to that positive interface. On the positive interval,
(RI.13) makes the correction vector in (RI.31)
\(-\mathcal O_J\mathcal Ju_c\), which need not vanish. It is the
nonmean inverse's response to the negative control source and
its complete rows. Thus a zero direct positive column does
not erase a returned positive or high response.

For a genuine parameter, let \(h_\nu^{\,0}\) be its full direct
mean/reference reconstruction before solving the nonmean
equations. The corresponding physical column is
\(h_\nu^{\,0}-\mathcal Ju_\nu\); the same observations and every
original functional row are applied to this complete column.
All ordinary data and independent interface data similarly
use their actual \(B^{-1}\) response. No low jump receiver is
manufactured from an ordinary \(L^2\) receiver.

The minimal numerical information, once the required inverse
exists on the actual stated spaces, is therefore:

| Purpose | Complete input or pairing |
|---|---|
| Scalar coordinate pivot | Existing \(\kappa_0\), not a new target |
| Internal control column | Exact (RI.7), all (RI.11), and retained functional rows; no direct positive or high body source |
| Legitimate sliced control denominator, if that complement is used | \(A^{-1}b_c\) and \(\sigma A^{-1}b_c\) |
| Genuine parameter denominator | \(B^{-1}g_\nu\), each original output row applied to it, and every direct parameter entry |
| An actual right side | \(B^{-1}y\) and the same output pairings, retaining all mean and nonmean source atoms |
| Positive observations of a corrected column | Body, root97, outer96 and joint193 of the complete reconstructed physical column |

For a signed enclosure \(|\Delta|\ge d>0\), (RI.31) gives the
rigorous receiver bound

$$
 \|\mathcal O_Jh\|
 \le \|\mathcal O_J(h_f+\mathcal Jz_y)\|
   +\frac{\|\mathcal O_J(h_c-\mathcal Ju_c)\|}{d}
                       |g-\sigma z_y|.
 \tag{RI.32}
$$

The two components of the joint193 endpoint receiver arise
from the same input. Their separate upper bounds cannot be
assigned a fictitious input orthogonality. The signed column
and pairing may be formed before taking any majorant.

## 8. Exact relation to the current WVC positive Green computation

The current R141/PS operator is the original WVC hybrid
\(A_L^c\). Its principal speed retains the declared family
value, while its lower coefficients use the repaired centre.
It is not \(P_{\le96}A_*P_{\le96}\).
The original source roles, weights, mixed boundary and all
193 endpoint observations in R141 remain unchanged.

If its full directed Green \(G_c\) has been certified, the
ordinary positive low coefficient transfer to the actual
compact centre must use the full difference

$$
 V_*=P_{\le96}A_*P_{\le96}-A_L^c,\qquad
 h_L=G_c(V_*h_L+f)
 \tag{RI.33}
$$

for homogeneous original mixed data. In body units
\(x=Sh_L\), the feedback is
\(S G_cV_*S^{-1}\). A bound strictly below one for this exact
body feedback, together with the complete endpoint receivers
and actual boundary lifts, is a sufficient transfer condition.
Another rigorous inverse proof for the same operator is also
possible. No such numerical condition is supplied here.

The complete state/principal-mean differences, all higher
frequency returns, actual physical outer rows and any genuine
intrinsic differences must be included. In particular the
same-phi \(C^0\) bridge of SR does not itself bound a complete
first-order operator on all frequencies. A finite low transfer
must pay the physical derivative factor \(4\cdot96\), as in
D.7--D.8, or use the corresponding exact cellwise operator.
One cannot call the hybrid a compact-centre differential to
skip (RI.33).

The support identity (RI.5) means the **direct** compact-control
column contributes zero to the positive part of (RI.33) and
its boundary observations. It says nothing about \(V_*\) on
other inputs, the negative-to-positive coupled response, the
true \(J_*\) feedback, the nonmean centre residual, a physical
parameter Schur determinant, or the final nonlinear
construction.

This supplement establishes the stated exact source reduction
and complete finite-rank interface. It introduces no scientific
run and re-evaluates no previously completed numerical target.
