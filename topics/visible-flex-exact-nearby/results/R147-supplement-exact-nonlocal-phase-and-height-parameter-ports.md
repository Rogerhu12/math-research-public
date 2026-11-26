# R147 PH: exact nonlocal phase and height ports for the original strict parameter column

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**New exact reductions and a paid same-selected phase receiver.** The
reflected strict parameter column has a one-leg phase integral, with the
square of the true transported label derivative. It is generally nonzero.
The full ordinary phase row on its support has norm less than (3/2).
Consequently the completed SB error for the original NP particular costs
less than (1.014851\,10^{-5}) in this phase row. This transfers the row
explicitly to the same original selected state; no compact mean-exact
centre is substituted.

The same-world-frame passive height variation reduces to a single radial
integral, but retains independent frame/position ports. Fixed physical
angle contributes an additional waist row with its own mean. Reflection
only removes qualified odd height tests, not even or mean height rows.
The signed phase integral and the complete height input carriers remain
separate new consumers; this note does not assert the full parameter
Schur or a regular boundary solution.

## PH1. Objects, normalization and the actual scalar phase row

Use exactly NP's implicit selected member

\[
 Q_\delta=Q_0+\delta_*Z_{\rm can},\quad
 \nu_\delta=\nu_0+\delta_*,\quad \eta=\eta_0,
 \qquad |\delta_*|<10^{-10},
 \tag{PH.1}
\]

with the original continuously repaired M32 centre and complete M96
direction. The selected conjugacy \(\mathcal H\) is W's run
43588332723/1, loss (1/250), without changing its constant phase.
Every angular integral uses normalized measure on period \(\pi/2\),
with physical frequencies (4j). The two state means are retained in
the ambient problem.

Set \(b=9/50\), \(C=[1/20,b]\), \(q=\sqrt{-K}\), \(m=\Pi v\), and
use exactly [P.5--6](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md):

\[
 F_\sigma=\beta I(u^2+Kv^2)-\sigma\gamma m q,\qquad
 I=\partial_\phi^{-1}(1-\Pi),
\]
\[
 \dot F_\sigma=2\beta I(uh_1+Kvh_2)-\sigma\gamma q\Pi h_2
     +\beta I(v^2)K_\nu
     +\sigma\frac{\gamma mT}{2q}w',
\quad K_\nu=-wK+Tw',\quad T=\frac{\beta}{2a^2\gamma^2}.
 \tag{PH.2}
\]

Here (h=v_\nu) is NP's true zero-terminal strict particular, not the
yet unconstructed full regular response (q_\nu). Both (h) and its
frozen exact trial (h^a) vanish above (b). The direct metric part is
supported in (C). The mean-speed term in (PH.2) is not put into (I).

Let (H_\sigma(0)=\mathrm{id}) be the original waist-based rays and
\(S_\sigma=H_\sigma^{-1}\). Define
\(a_\sigma=\partial_\phi(\mathcal H\circ S_\sigma)\).
[D.6](R133-supplement-phase-Schur-complete-distributed-adjoint-source.md)
gives the full principal scalar row

\[
 \dot\Omega=\int_0^b
       \langle a_+^2\dot F_+-a_-^2\dot F_-\rangle\,dr.
 \tag{PH.3}
\]

At the selected exact conjugacy this is the complete average in P.15's
invariance-equation linearization. It does not require asserting a smooth
rotation-number function across an arbitrary parameter interval. Away
from that constraint the original nonzero-defect terms in the full
invariance equation must still be retained.

## PH2. Reflection reduces the number of new integrals, not the column

The original state has (u) odd and (v) even. The radial metric and
the true reflected parameter variation therefore give

\[
 F_-(r,\phi)=-F_+(r,-\phi),\quad
 S_-(r,\phi)=-S_+(r,-\phi),\quad
 \dot F_-(r,\phi)=-\dot F_+(r,-\phi).
 \tag{PH.4}
\]

These are uniqueness identities for the actual rays, with their original
identity initial labels. The complete repaired interfaces are retained.
[RRF.18](R133-supplement-true-reflection-rigidity-and-selected-waist-target.md)
proves

\[
 \mathcal H(-\phi)+\mathcal H(\phi)=2\mathcal H(0),\qquad
 \mathcal H'(-\phi)=\mathcal H'(\phi).
 \tag{PH.5}
\]

In particular no assumption \(\mathcal H(0)=0\) is needed. Equations
(PH.4--5) imply \(a_-(r,\phi)=a_+(r,-\phi)\), hence

\[
 \boxed{\dot\Omega=2\int_0^b\langle a_+^2\dot F_+\rangle\,dr.}
 \tag{PH.6}
\]

Both terms in (PH.3) add with the same sign. With
\(W=a_+^2\), \(A=I(P_{\rm odd}W)\), \(M=\Pi W\), the complete
state and direct metric parts become

\[
 L_\Omega h=\int_0^b\langle\ell_1h_1+\ell_2h_2\rangle dr,
\quad \ell_1=-4\beta uA,
\quad \ell_2=-4\beta KvA-2\gamma qM,
 \tag{PH.7}
\]
\[
 t_\Omega=-2\int_C\beta K_\nu\langle Av^2\rangle dr
       +\int_C M\frac{\gamma mT}{q}w'\,dr.
 \tag{PH.8}
\]

These follow from (I^*=-I), with the complete odd projection and its
mean-zero primitive. The last term of \(\ell_2\) is a constant angular
load. Neither (PH.7) nor (PH.8) is assigned finite Fourier support.
No integration by parts in (r), moving seam term, or (w')-term is
silently discarded.

## PH3. A full ordinary phase dual on the same selected background

P.18--25 prove for the original (Q_0)

\[
 a_0(r)=2|\beta|c_I R_0(r)+\gamma_0(r),\quad
 c_I=\frac\pi{4\sqrt3}<\frac12,\quad
 R_0=\sup_\phi\sqrt{u_0^2+q_0^2v_0^2},\quad
 \|a_0\|_{L^2(0,r_*)}<.591950779 .
 \tag{PH.9}
\]

The bound includes the genuine root remainder, all angular frequencies
and the even mean. We restrict its integral to ([0,b]), and now pay
the actual change of background. The original D/SP whole-family bounds,
and the exact deductions STC.5--7, give on this shorter interval

\[
 .5338<q_0,q_\delta<1.03,\quad |\beta|<2,\quad
 \gamma_0,\gamma_\delta<7,\quad R_0<1.912,
\]
\[
 \|Q_\delta-Q_0\|_{A_0}\le19|\delta_*|<2\,10^{-9},
\qquad |K_\delta-K_0|<1.048\,10^{-7}.
 \tag{PH.10}
\]

The curvature bound is the complete saved SP
`metric_K_difference_upper` on the wider \(|\delta|\le10^{-8}\)
family; it is only restricted, not recomputed. It includes every
compact seam. The constants (2,7) in STC are deductions from the
positive terms of D, not compact-centre transfer fees.
In particular \(|v_0|\le R_0/q_0<4\), and

\[
 |q_\delta-q_0|\le\frac{1.048\,10^{-7}}{2(.5338)},\quad
 R_\delta-R_0\le1.03(2\,10^{-9})+4|q_\delta-q_0|
                       <4.22\,10^{-7}.
 \tag{PH.11}
\]

The exact metric identity gives
\(|\gamma_\delta-\gamma_0|\le7(e^{5\,10^{-11}}-1)<4\,10^{-10}\).
Thus, with (a_\delta=2|\beta|c_I R_\delta+\gamma_\delta),

\[
 a_\delta\le a_0+10^{-6},\qquad
 \|a_\delta\max(1,q_\delta)\|_{L^2(0,b)}<.610.
 \tag{PH.12}
\]

The last inequality uses \(\sqrt b<.425\) and P.25's already proved
complete bound. This is an explicit same-selected transfer.

W's complete derivative Wiener bound is \(\|\mathcal H'\|_{A_{1/128}}<33/32\),
including its constant coefficient one. The original R31 bound is
\(L_\delta<1/16\) for every partial leg of the same real family.
Therefore

\[
 \sup_{r\le b,\sigma}|a_\sigma|
 <\frac{33}{32}e^{1/16}
 <\frac{33}{32}\frac{16}{15}=\frac{11}{10}.
 \tag{PH.13}
\]

The field estimate P.20 and (PH.3) now prove, for every full (e) of
ordinary (L^2_rL^2_\phi), including both means,

\[
 |L_\Omega e|
 \le 2(11/10)^2(.610)\|e\|_{L^2_rL^2_\phi}
 <\frac32\|e\|_{L^2_rL^2_\phi}.
 \tag{PH.14}
\]

This bound does not need reflection of (e). With the
[completed ASB error](R147-supplement-actual-short-parameter-errors-and-refined-signed-borders.md),

\[
 \boxed{|L_\Omega(v_\nu-h^a)|<1.014851\,10^{-5}.}
 \tag{PH.15}
\]

The exact-rational
[saved-bound consumer](../scripts/fourfold_codazzi_nonlocal_parameter_port_saved_bounds.py)
checks these outward displays without any new old-target evaluation.

## PH4. The necessary original phase carrier and its true-label fee

The existing complete finite phase transport has angular extent 64 and
radial degree 12. Its original 0--130 germs cover exactly ([0,b]).
Their whole public natives retain every accepted interval, original
candidate piece, scalar-native SHA, polynomial SHA, and complete
two-leg terminal state. The fixed immutable commit is
`46f127c7153f5393dcd2a00f42d4c1d3662c294d`.
Germs 0--126 are at
`data/phase_transport_resume127_20261114/transport/transport-germNNNN.json.gz`;
germs 127--130 are at
`notes/phase_transport_complete_ci/run-43580721166-1/transport-germNNNN.json.gz`.

The only allowed reconstruction is the original degree-12 recurrence at
256-bit precision, with exactly the same sequential dyadic midpoint
choices and both original ray signs. Each **whole** polynomial SHA and
every whole two-leg endpoint is retained. The old residual/norm gates
are not called again. The two legs are necessary for the original
carrier identity even though (PH.6) needs one new signed integral.
NP's four exact arrays similarly retain all four original whole hashes;
no trial is reselected.

Here is a bound for using that original carrier in a new phase pairing.
Let \(\widehat a_{0,+}\) be its derivative, based on the original
finite (H_{24}). W/RW.8 gives
\(\|\mathcal H-K_{48}\circ H_{24}\|_{A_{1/128}}<2.211\,10^{-7}\).
The whole original K48 derivative-change record is less than
\(1.422\,10^{-8}\). The original H root contract gives
\(\|H_{24}'\|_{A_{1/32}}<33/32\). Fourier differentiation with
\(e>2\), followed by the real inverse-ray derivative bound, costs

\[
 \frac{16}{15}\left(64(2.211\,10^{-7})
                 +\frac{33}{32}(1.422\,10^{-8})\right).
 \tag{PH.16}
\]

The R31 whole first-parameter field integral is dominated by its saved
complete return first-parameter bound (Y<.541\): in the original
source (Y=2e^{2L_\delta}(D_{1,\delta}+C_{1,\delta})\), with positive
summands. Thus comparison of the two transported (H_{24})'s on
complex strip (1/256) gives a complete value change less than
\((11/10)10^{-10}(.541)<6\,10^{-11}\). All intermediate complex
images lie inside the old strip (1/32): the one- and two-flow width
upper bounds are respectively (1/240) and (1/225\).
Cauchy's derivative estimate costs at most (256(6\,10^{-11})\).

Finally the original full transport residual gives a derivative error
less than (2\,10^{-12}\). L.7 states the sharper endpoint display;
the same bound holds inside every original step, because the complete
unprojected residual controls every shorter source integral, the finite
polynomial is continuous at its exact endpoints, and the whole source
and composition budgets are nonnegative. No derivative of a uniform
scalar remainder is taken.
Adding these three complete errors proves

\[
 \sup_{0\le r\le b}|a_{\delta,+}-\widehat a_{0,+}|<1.6\,10^{-5},
\quad
 \sup|a_{\delta,+}^2-\widehat a_{0,+}^{\,2}|<3.521\,10^{-5}.
 \tag{PH.17}
\]

The finite carrier is not assumed to satisfy exact reflection: its
original cosine coefficients may be nonzero. Formula (PH.6) uses the
true reflected labels; (PH.17) pays their approximation by the original
plus carrier. A new signed trial integral must additionally pay the
full change from (\dot F_{+,0}[h^a]\) to
\(\dot F_{+,\delta}[h^a]\), including its metric source and mean.
Then (PH.15) pays the remaining true PDE-response error. These are
separate errors; no old explicit-family response (Z\) is substituted
for NP's particular.

## PH5. Exact same-world-frame passive position variation

Use the complete off-shell reconstruction of
[H.1--8](R133-supplement-residual-sensitive-vector-height-and-Airy-contact.md).
To avoid confusing curvature (q) with a connection coefficient, write

\[
 d=-\beta I(u^2+Kv^2),\quad J=v/m,\quad \tau=dJ-\gamma u,
\quad M=\Omega(p,k,t),
\]
\[
 p=\beta\tau/\gamma,\quad k=a(\gamma Kv+du/m),\quad t=ad/m,
\quad c_r=(a\gamma,a\tau,0)^T,
\quad Q_r=QM,\quad F_r=Qc_r,
 \tag{PH.18}
\]

where \(\Omega(p,k,t)=\left(\begin{smallmatrix}0&-p&-k\\p&0&-t\\k&t&0\end{smallmatrix}\right)\)
and (Q) is the actual orthogonal frame. Define the world skew matrix
\(K_f=\delta Q\,Q^T\). Direct differentiation gives
\((K_f)_r=Q\delta M Q^T\), with no assumption on the Codazzi residual.
For the independent terminal ports (Y_b=\delta F(b)\),
\(K_b=\delta Q(b)Q(b)^T\), variation of (F_r\) and changing the
order of the two radial integrals yield

\[
\boxed{\begin{aligned}
 \delta F(0)={}&Y_b-K_b(F(b)-F(0))\\
 &+\int_0^b Q(r)\delta M(r)Q(r)^T(F(r)-F(0))\,dr
       -\int_0^b Q(r)\delta c_r(r)\,dr .
\end{aligned}}
 \tag{PH.19}
\]

For example (K_f(r)=K_b-\int_r^bQ\delta M Q^T\), which fixes all
signs in (PH.19). The state and metric variations vanish above (b\);
this only says \(\delta M=\delta c_r=0\) there. Vanishing frame and
position variations above (b) requires the independent outer ports to
be fixed to zero. With arbitrary ports at a farther endpoint (R),
the corresponding first line is (Y_R-K_R(F(R)-F(0))\).
All original interface transmission terms remain when affine frame or
position jumps are prescribed.

## PH6. The full ordinary height load, including its constant mean

Take a fixed world covector (e_z\) and a fixed moving test weight
\(\zeta(\phi)\). Let
\(v_f=\zeta Q^Te_z\), \(z_f=Q^T(F(r)-F(0))\), and define

\[
 r_p=(v_f)_2(z_f)_1-(v_f)_1(z_f)_2,\quad
 r_k=(v_f)_3(z_f)_1-(v_f)_1(z_f)_3,\quad
 r_t=(v_f)_3(z_f)_2-(v_f)_2(z_f)_3 .
\]

The radial integrand in (PH.19)'s scalar height row is
\(r_p\delta p+r_k\delta k+r_t\delta t
 -a((v_f)_1\delta\gamma+(v_f)_2\delta\tau)\).
Set

\[
\begin{aligned}
 k_\tau&=(\beta/\gamma)r_p-a(v_f)_2,\\
 k_d&=k_\tau v/m+a r_k u/m+a r_t/m,\\
 k_1&=-\gamma k_\tau+a r_k d/m,\qquad
 k_2=k_\tau d/m+a r_k\gamma K,\\
 k_\mu&=-k_\tau dv/m^2-a r_kdu/m^2-a r_td/m^2.
\end{aligned}                                                   \tag{PH.20}
\]

Since \(\delta d=-2\beta I(uh_1+Kvh_2)\) at fixed metric and
\(\mu=\Pi h_2\), skew-adjointness of (I) gives the exact ordinary
state load

\[
 \ell_{H,1}=k_1+2\beta u I(k_d),\qquad
 \ell_{H,2}=k_2+2\beta Kv I(k_d)+\Pi k_\mu.
 \tag{PH.21}
\]

In particular the last constant acts on the genuine even mean.
For the metric derivative (a_\nu=\beta_\nu=0\), put

\[
 k_\gamma=-u k_\tau-\beta\tau r_p/\gamma^2+a r_kKv-a(v_f)_1,
\qquad k_K=a r_k\gamma v .
\]

The complete direct metric contribution is

\[
 \int_C\left[\gamma_\nu\Pi k_\gamma
       +K_\nu\Pi\{k_K+\beta I(k_d)v^2\}\right]dr,
\qquad \gamma_\nu=w\gamma/2 .                           \tag{PH.22}
\]

Thus (PH.19--22) are a concrete new signed pairing recipe, not a claim
that local zero state makes height zero. The original full means and
all Fourier outputs remain. Ordinary (L^2) dual bounds can use ASB;
the complete primitive/mean dual form can instead use SB.12 when its
angular row derivative is the better paid input.

## PH7. Fixed physical angle requires an additional waist term

The actual physical angle is
\(\Theta=\phi+Iv/m\), \(J=\Theta_\phi=v/m\), and
\(\delta\Theta=Ih_2/m-(Iv)\mu/m^2\).
For (Z_{\rm phys}(\theta)=e_z\cdot F(\Phi(\theta))\),

\[
 \delta Z_{\rm phys}\circ\Theta
   =e_z\cdot\delta F-\frac{e_z\cdot F_\phi}{J}\delta\Theta.
 \tag{PH.23}
\]

A fixed physical test \(\zeta_\theta\) with normalized (d\theta\)
therefore uses \(\zeta=\zeta_\theta(\Theta)J\) in (PH.19--22),
and also the coordinate term \(-\langle C_\theta,\delta\Theta\rangle\),
where \(C_\theta=\zeta_\theta(\Theta)e_z\cdot F_\phi\).
Its complete ordinary (h_2(0)\) row is

\[
 \boxed{\ell_{{\rm angle},2}
       =\frac{I C_\theta}{m}
        +\frac{\langle C_\theta,Iv\rangle}{m^2}\,1 .}
 \tag{PH.24}
\]

No mean or physical Jacobian has been omitted. The weight is frozen at
the base when differentiating a fixed physical functional. Its induced
variation is exactly the coordinate term already written in (PH.23).
The whole original passive reconstruction has
\(F_\phi=Q(c_\phi+P)\), \(Q_\phi=Q(L+E)\); its genuine defects
(E,P\) need not vanish at the unsolved centre. In particular replacing
\(F_\phi\) by (Qc_\phi\), or converting this row into a cap/Airy row
without H.10--19's complete residual/contact terms, is not allowed.

## PH8. Exactly which height reflection can vanish

If the original supplied world anchor is invariant under a vertical
reflection (S\) with \(S^Te_z=e_z\), let
\(D=\operatorname{diag}(1,-1,1)\).
The actual parity in (PH.18) gives
\(M(r,-\phi)=DM(r,\phi)D\), \(c_r(r,-\phi)=Dc_r(r,\phi)\).
Uniqueness then propagates the supplied identities
\(Q(r,-\phi)=S Q(r,\phi)D\) and
\(F(r,-\phi)=S F(r,\phi)\), with the same affine reflection plane.
For a reflected variation with that same fixed anchor,
\(\delta(e_z\cdot F)\) is even. Also \(\Theta\) and
\(\delta\Theta\) are odd and \(F_{z,\phi}\) is odd, so
(PH.23) remains even in the genuine physical angle.

Only a genuinely odd physical height test then has zero pairing.
The mean and cosine tests survive; independent position/frame ports
must separately satisfy the stated reflection condition. No particular
waist-plane constraint is inferred from NP's local root/outer zero
state, and no unqualified height row is deleted from the original
bordered system.
