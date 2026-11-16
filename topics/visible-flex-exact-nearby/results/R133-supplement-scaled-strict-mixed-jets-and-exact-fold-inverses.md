# R133 supplement: scaled strict mixed jets and exact fold inverses

2026-11-16, visible-exact / tail.

**Analytic finite recipe; no new numerical evaluation.** This note gives a separate radial-by-angular majorant packet for the same real strict fold. The radial order is recorded independently of the angular order. A large radial derivative is therefore never used as a pure angular derivative merely because their total degrees agree.

The packet uses the positive drift representation of the fold gap, the already saved individual phase angular derivatives, and exact two-by-two identities. It supplies the complete strict geometry required by the old sufficient packet, the full inverse matrices, and an ordered route through the leading amplitude, full forcing and first transport. The original local root packet remains a separate domain. All source, mean, interface, root and outer equations retain their original meanings.

The new relative-angular input and the new mixed majorants are not asserted to have been computed. Every existing successful record used below is read unchanged. The construction is a new finite positive algorithm, not an instruction to rerun WGS or any old complete residual producer.

## WSJ1. Domain, signs and the actual functions

Work on the original strict interval $0\le r\le r_c$, where
$$
 r_c=\frac{76285779072683}{320000000000000},\qquad
 t=-T>0,\quad s=\sqrt t,\quad a=\eta q>0 .
 \tag{WSJ.1}
$$
All radial derivatives are the true one-sided derivatives on the original pieces. The point $r_*$ is outside this strict calculation; it is handled by the original analytic germ. The same selected real member and actual reflected input normalization are retained.

Use WUA's actual real lifts
$$
 \Phi_\sigma=X-\sigma\omega,\quad
 p_\sigma=\partial_\phi\Phi_\sigma,\quad
 x=X_\phi=\frac{p_++p_-}{2},\quad
 u=\omega_\phi=\frac{p_--p_+}{2},\qquad \sigma=\pm1 .
 \tag{WSJ.2}
$$
The letter $u$ in (WSJ.2) is used only in the fold formulas in this note. When the original physical background occurs in the forcing, it is written $u_{\rm bg}$. No physical mean is identified with a fold derivative.

The original positive phase lower gives $p_\pm\ge m_\Phi>0$. WUA.6--7 gives
$$
 D=\partial_r-d\partial_\phi,\quad
 D\omega=-a x,\quad DX=-a u,\quad
 Dt=-Qx,\quad Q=\frac a{s},\quad
 t=\left(\frac{3\omega}{2}\right)^{2/3}.
 \tag{WSJ.3}
$$
In particular $u=s\,t_\phi=-sT_\phi$. Let
$$
 {\cal D}=p_+p_-=x^2-u^2=x^2+T T_\phi^2>0,\qquad
 \mu=Q^2{\cal D}.
 \tag{WSJ.4}
$$
These are identities of actual functions. No determinant is formed by subtracting two positive norm bounds.

The drift characteristic $\chi'_v=-d(v,\chi_v)$, with initial angle at $r$, gives
$$
 \omega(r,\phi)=\omega(r_c,\chi_{r_c}(\phi))
       +\int_r^{r_c}a(v)x(v,\chi_v(\phi))\,dv .
 \tag{WSJ.5}
$$
Every summand is positive. The separate drift contract supplies ordinary relative bounds
$$
 \frac{|\partial_\phi^b\omega|}{\omega}\le R^\omega_b,
 \qquad 1\le b\le14 .
 \tag{WSJ.6}
$$
Its fixed output is complete_strict_relative_omega_angular_orders_1_through_14. The cut term, all Bell terms for the drift composition, the positive cut gap and every shorter flow are included. WX.12, DX.14 and WGS's higher-flow recurrence use the angular derivatives of $d$; the extra $\pm\eta q$ velocity is radial. This is the reason their full comparison envelopes also qualify (WSJ.5). Similar-looking numerical flow values alone would not establish that fact.

Saved $\Phi_\sigma$ derivatives of orders $1,\ldots,15$ give $x$ through order $14$. Thus the positive-sum proof of (WSJ.6) ends at $14$. An additional route below supplies certain edge derivatives; it does not change this stated range or claim a new positive-sum bound for $R^\omega_{15}$.

## WSJ2. A frozen-scale jet, with no mixing of rows

Fix a real base point $(r_0,\phi_0)$, including a specified one-sided piece at a seam, and put $t_0=t(r_0,\phi_0)$. For an actual scalar or matrix function $F$, write the finite formal jet
$$
 {\cal J}F(\xi,\zeta)
   =\sum_{(p,q)\in{\cal I}_m^P}
       \frac{t_0^p}{p!\,q!}
       \partial_r^p\partial_\phi^qF(r_0,\phi_0)
           \xi^p\zeta^q,\qquad
 {\cal I}_m^P=\{0\le p\le P,\ q\ge0,\ p+q\le m\}.
 \tag{WSJ.7}
$$
The scale $t_0$ is frozen while these coefficients are formed. This is the formal Taylor jet of $F(r_0+t_0\xi,\phi_0+\zeta)$. It requires only the stated derivatives on that side of the piece, not analytic continuation across a seam.

A scalar bound for a coefficient of (WSJ.7) is a bound for that exact pair $(p,q)$. A vector or matrix uses the complete component or entry sum unless another norm is explicitly stated. Geometry and amplitudes use scalar suprema or component-sup sums. They are not declared Fourier-Wiener $A^0$ functions with the same numerical norm.

Multiplication is the full coefficient convolution
$$
 ({\cal J}F\,{\cal J}G)_{p,q}
   =\sum_{i=0}^p\sum_{j=0}^q
           ({\cal J}F)_{i,j}({\cal J}G)_{p-i,q-j}.
 \tag{WSJ.8}
$$
Take absolute values term by term only after the exact ordered identity has been written. Matrix factors retain their order. For a positive scalar $F$, its relative jet is ${\cal R}F={\cal J}F/F(r_0,\phi_0)$, with constant coefficient $1$.

If $Z=1+Z_+$ is such a relative jet, a complete positive coefficient majorant for $Z^\alpha$, for any fixed rational $\alpha$, is
$$
 {\cal B}_\alpha(B)_{p,q}
  =\sum_{k=0}^{p+q}\left|\binom{\alpha}{k}\right|
                       [B_+^k]_{p,q},
 \quad (p,q)\ne(0,0),\qquad
 {\cal B}_\alpha(B)_{0,0}=1 .
 \tag{WSJ.9}
$$
Here $B_+$ has zero constant coefficient and bounds every other coefficient of $Z$. This is a finite formal coefficient identity. It does not assume a numerical smallness condition on $Z_+$ or sum an infinite analytic series. Reciprocals use $\alpha=-1$; the powers needed below are $2/3,\pm1/2,1/4,-2$.

The derivative shifts are
$$
 {\cal J}(\partial_rF)=t_0^{-1}\partial_\xi({\cal J}F),
 \qquad {\cal J}(\partial_\phi F)=\partial_\zeta({\cal J}F).
 \tag{WSJ.10}
$$
They act on the actual functions. A coefficient $t_0^pF_{r^p\phi^q}$ is not itself passed to an ordinary jet differentiator as though the frozen $t_0$ were a variable coefficient.

In particular, $p=0$ in (WSJ.8)--(WSJ.9) uses only $p=0$ inputs. No radial coefficient can enter a pure angular row. This proves the advertised separation directly.

For comparison, the genuine variable-coefficient operators obey
$$
 (t\partial_r)^2F=t^2F_{rr}+t\,t_rF_r,\qquad
 (tD)^2F=t^2D^2F+(Dt)(tDF),
$$
$$
 [tD,\partial_\phi]
   =-\frac{t_\phi}{t}(tD)+t d_\phi\partial_\phi .
 \tag{WSJ.11}
$$
The connection terms in (WSJ.11) are retained whenever that operator notation is used. The frozen-scale calculus avoids silently dropping them.

## WSJ3. Current inputs and independently indexed background rows

Only complete current records with the same domains and functions are admitted. The WGS main and its original-input companion have the immutable identities in WSJ12. Their common run, source, math-module, manifest and byte identities remain part of admission.

The main's complete_higher_flow_and_cut_conclusion contains the fifteen individual complete_strict_phase_angular_orders_1_through_15 records and strict_phase_lower. The companion contains the original flow orders $1,\ldots,4$, physical mixed-background records $Q_{p,j}$ for $0\le p\le2,\ 0\le j\le3$, intrinsic derivatives, the cut values and cut derivatives. The old complete_strict_coefficient_conclusion gives the saved radial $\eta$ and $\ell_0=2\beta\Pi S$ bounds. The geometric value bounds, positive lowers and the complete $G,G^{-1}$ value bounds are copied from their original fields.

An independent background derivative is allowed to use the original Fourier qualification. For $u_{\rm bg},v_{\rm bg}$, the complete $Q_{p,j}$ pair bound dominates either component. For higher angles,
$$
 U_{p,q},V_{p,q}
 \le384^{\max(q-3,0)}Q_{p,\min(q,3)}
 \quad(0\le p\le2).
 \tag{WSJ.12}
$$
These are ordinary $A^0$ derivative bounds of the actual finite background, not of an Airy amplitude. Use the full ordinary two-index Leibniz sum for
$S=u_{\rm bg}^2+K v_{\rm bg}^2$ and $\beta S$. The drift is the original
$d=-\beta I(S-\Pi S)$. Consequently its angular-zero row uses the actual
$A^0$ primitive fee $1/4$; its angular order $q\ge1$ uses the complete
$q-1$ derivative of $\beta S$, with the Fourier projection retained.
This projection is a contraction in the original $A^0$ norm. A pointwise sup norm alone would not justify that step.

Thus the needed new independently indexed $d_{r^p\phi^q}$ bounds can be formed from (WSJ.12), rather than copying a total-degree sum into every angular slot. The exact degree-zero scalar or any other already separately saved identical scalar is copied, not recalculated. New per-index envelopes are distinct from the old group maxima.

The radial functions have no angular derivatives:
$$
 a=\eta q,\quad
 a_r=\eta_rq+\eta q_r,\quad
 a_{rr}=\eta_{rr}q+2\eta_rq_r+\eta q_{rr}.
 \tag{WSJ.13}
$$
All terms in (WSJ.13) are retained. The first two radial derivatives of $a$ are enough for the phase and gap construction through radial order three. The leading gauge additionally requires the original $q_{rrr}$ and $(\beta\Pi S)_{rr}$. These are separate real one-sided input obligations, already present in the WGS sufficient packet; they do not follow from the fourteen angular bounds.

## WSJ4. Exact triangular phase and gap recurrences

Let $P_\sigma={\cal R}p_\sigma$, $W={\cal R}\omega$,
$A={\cal R}a$, and let $V_\sigma={\cal J}(d+\sigma a)$.
The true phase equation implies
$$
 (p_\sigma)_r
       =\partial_\phi[(d+\sigma a)p_\sigma].
 \tag{WSJ.14}
$$
It gives the exact normalized recurrence
$$
 (P_\sigma)_{p+1,q}
   =\frac{t_0(q+1)}{p+1}
       [\,V_\sigma P_\sigma\,]_{p,q+1}.
 \tag{WSJ.15}
$$
The coefficients on the right have radial order at most $p$. Start with
$$
 (P_\sigma)_{0,0}=1,\qquad
 |(P_\sigma)_{0,q}|
   \le\frac{P^\Phi_{q+1}}{q!\,m_\Phi},
       \quad1\le q\le14 ,
 \tag{WSJ.16}
$$
where $P^\Phi_j$ is the saved complete ordinary phase derivative bound.
For upper bounds in (WSJ.15), use all terms of the convolution, the upper endpoint for $t_0$, and the complete $d+\sigma a$ triangle. This does not assert that two different sign flows are the same function.

Let $X_1={\cal J}x$. It is formed exactly as the half sum
$$
 X_1=\tfrac12[p_+(r_0,\phi_0)P_+
                  +p_-(r_0,\phi_0)P_-].
$$
Use their complete positive value bounds after the identity. The gap equation in (WSJ.3) gives
$$
 W_{p+1,q}
  =\frac{t_0}{p+1}
            [\,({\cal J}d)\,\partial_\zeta W\,]_{p,q}
    -\frac{3Q(r_0,\phi_0)}{2(p+1)}
            [\,A X_1\,]_{p,q}.
 \tag{WSJ.17}
$$
The second coefficient uses $t_0a(r_0,\phi_0)/\omega(r_0,\phi_0)=3Q/2$.
It does not divide repeatedly by a small cut lower for $\omega$.
Start with $W_{0,0}=1$ and
$|W_{0,q}|\le R^\omega_q/q!$ for $1\le q\le14$.
An already saved whole value bound for $Q$ is sufficient in (WSJ.17);
it is not necessary to recompute that successful scalar.

Recurrences (WSJ.15) and (WSJ.17), with the full sums followed by positive
triangles, construct every pair in ${\cal I}_{14}^3$. They use only
the already specified phase angular orders through fifteen and coefficient
radial orders through two. They do not require $\Phi_\sigma$ at angular
order sixteen.

For clarity, their first two radial identities are also
$$
 \omega_r=d u-a x,\qquad
 x_r=d_\phi x+d x_\phi-a u_\phi,\qquad
 u_r=d_\phi u+d u_\phi-a x_\phi,
$$
$$
 \omega_{rr}
 =(d_r+d d_\phi)u+(d^2+a^2)u_\phi
       -2ad x_\phi-(a_r+a d_\phi)x .
 \tag{WSJ.18}
$$
For $v_\sigma=d+\sigma a$,
$$
 (p_\sigma)_{rr}
  =v_\sigma^2(p_\sigma)_{\phi\phi}
    +[(v_\sigma)_r+3v_\sigma d_\phi](p_\sigma)_\phi
    +[(d_\phi)_r+v_\sigma d_{\phi\phi}+d_\phi^2]p_\sigma .
 \tag{WSJ.19}
$$
Equations (WSJ.13), (WSJ.18) and (WSJ.19) explicitly retain
$\eta_r,q_r,d_r$, the mixed derivatives of $d$, and all quadratic terms.
The third radial row is generated by the same recurrence with
$a_{rr},d_{rr}$; no derivative is taken of a numerical upper bound.

## WSJ5. The complete $t$-weights and the edge at total degree fifteen

Put $\tau={\cal R}t$. The exact identity is
$$
             \tau=W^{2/3}.
 \tag{WSJ.20}
$$
Thus (WSJ.9) constructs $t^\alpha/t_0^\alpha=\tau^\alpha$, including
$\alpha=\pm1/2,1/4,-1$, on every pair in ${\cal I}_{14}^3$.
All pure angular bounds use only (WSJ.6), with no radial row or repeated
small-$\omega$ denominator.

There is a separate edge identity:
$$
 t_\phi=\frac{u}{s},\qquad
 {\cal J}u=\tfrac12[p_-(r_0,\phi_0)P_-
                         -p_+(r_0,\phi_0)P_+].
 \tag{WSJ.21}
$$
Use the actual difference first and the complete positive sum for its
bound; do not subtract upper endpoints. Multiplying this full jet by
$s(r_0,\phi_0)^{-1}\tau^{-1/2}$ gives the full $t_\phi$ jet on
${\cal I}_{14}^3$. The scalar negative power uses the true strict positive
$t$ lower.

If $q\ge1$, a coefficient of $t$ is then recovered by
$$
       ({\cal J}t)_{p,q}
          =\frac1q({\cal J}t_\phi)_{p,q-1}.
 \tag{WSJ.22}
$$
The $q=0,\ p\le3$ values were already constructed in (WSJ.20).
Equations (WSJ.21)--(WSJ.22) supply the complete absolute $t,T$ packet on
${\cal I}_{15}^3$, and $y=T_\phi=-t_\phi$ on ${\cal I}_{14}^3$.
This is an additional exact route; it is not a claim that the drift
positive-sum theorem supplied relative angular order fifteen.

Similarly, $X_\phi=x$ supplies every $q\ge1$ coefficient of $X$
through total degree fifteen. Its radial-zero-angle coefficients use
$X_r=d x-a u$, with the required coefficient derivatives retained.
The lift value $X_{0,0}$ remains omitted. An omitted lift is never
replaced by zero to satisfy a generic jet's closure check.

The same construction preserves both original $\Phi_\sigma$ derivatives:
for $q\ge1$ shift $p_\sigma$; for radial-only derivatives use
$(\Phi_\sigma)_r=(d+\sigma a)p_\sigma$. No bounded periodic value is assigned
to either lift.

## WSJ6. An exact scaled inverse for the full $H$ matrix

The original matrix and its scaling are
$$
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},\quad
 H=i\epsilon x\,Id+T_\phi K_T,\quad
 S_t=\operatorname{diag}(1,s).
$$
Direct multiplication gives
$$
 \widehat H=S_tHS_t^{-1}
       =\begin{pmatrix}i\epsilon x&u\\-u&i\epsilon x\end{pmatrix}.
 \tag{WSJ.23}
$$
For real $x,u$, this is a normal matrix diagonalized by a constant
unitary matrix. Its eigenvalues are $i(\epsilon x+u)$ and
$i(\epsilon x-u)$. Since $p_\pm=x\mp u>0$,
$$
       \|\widehat H^{-1}\|_2=\frac1{\min(p_+,p_-)} .
 \tag{WSJ.24}
$$
This is a pointwise finite-matrix identity. $S_t$ is a variable
multiplication matrix, not a fixed unitary change of the physical function
space. Formula (WSJ.24) alone is not an unweighted multiplier or derivative
bound.

Define the actual functions
$$
 h_a=\tfrac12(p_+^{-1}+p_-^{-1}),\qquad
 h_b=\tfrac12(p_+^{-1}-p_-^{-1}).
$$
Then the entire original inverse is
$$
 \boxed{\quad
 H^{-1}=
 \begin{pmatrix}
   -i\epsilon h_a&s h_b\\
   -s^{-1}h_b&-i\epsilon h_a
 \end{pmatrix}.
 \quad}
 \tag{WSJ.25}
$$
Use the complete relative reciprocal jets $P_\pm^{-1}$, their genuine
positive value gaps, and both full powers $\tau^{1/2},\tau^{-1/2}$ in
(WSJ.25). A bound for $h_b$ uses the complete sum of the two reciprocal
majorants. Neither its value nor any derivative is obtained by subtracting
two norm uppers.

All four entries and all Leibniz terms are retained. A complete entry-sum
bound follows by summing their complete bounds; a whole matrix norm may be
used only after the corresponding full matrix identity. This supplies
$H^{-1}$ on ${\cal I}_{14}^2$, and in particular every old required
index in ${\cal I}_{13}^2$. It avoids the extra angular derivative that
would be requested by independently estimating $T_\phi/{\cal D}$ without
using (WSJ.25).

For an explicit radial check, put
$\nu_\sigma=(p_\sigma)_r/p_\sigma
=d_\phi+(d+\sigma a)(p_\sigma)_\phi/p_\sigma$. Then
$$
 (p_\sigma^{-1})_r=-\nu_\sigma p_\sigma^{-1},\qquad
 (p_\sigma^{-1})_{rr}
       =(\nu_\sigma^2-(\nu_\sigma)_r)p_\sigma^{-1},
$$
$$
 (\nu_\sigma)_r
   =(d_\phi)_r+(d_r+\sigma a_r)\ell_\sigma
       +(d+\sigma a)\partial_\phi\nu_\sigma,\qquad
 \ell_\sigma=(p_\sigma)_\phi/p_\sigma .
 \tag{WSJ.26}
$$
The $\ell_\sigma$ here is a logarithmic derivative of a phase, not the
physical coefficient $-2\beta u_{\rm bg}v_{\rm bg}$.
Recovering (WSJ.25) also differentiates $s^{\pm1}$ in full. There is no
free cancellation of $S_t$'s derivatives and no new claim of self-adjoint
physical evolution.

## WSJ7. Positive factorization of $Q,\mu^{-1}$ and the radial inputs

Let $E_\eta={\cal R}\eta$ and $E_q={\cal R}q$; these have only radial
coefficients. With $A=E_\eta E_q$, the exact relative jets are
$$
 {\cal R}Q=A\tau^{-1/2},\qquad
 {\cal R}(\mu^{-1})
       =\tau A^{-2}P_+^{-1}P_-^{-1}.
 \tag{WSJ.27}
$$
The value bounds are the old same-domain values, or an explicitly new
whole positive candidate from
$$
 Q_0=a_0t_0^{-1/2},\qquad
 (\mu^{-1})_0=\frac{t_0}{a_0^2p_{+,0}p_{-,0}} .
$$
The candidate must retain every factor and use lowers for all denominators.
An already saved identical value expression is read, not evaluated again.

Equation (WSJ.27) supplies the required ${\cal I}_{13}^2$ packets.
The absence of angular derivatives in $E_\eta,E_q$ is an identity of the
actual radial functions; it is not a small-norm assumption.

For a transparent second-radial check, let
$\alpha=a_r/a=\eta_r/\eta+q_r/q$,
$\tau_r^{\log}=t_r/t$, and $g=\log(\mu^{-1})$. Then
$$
 g_r=\tau_r^{\log}-2\alpha-\nu_+-\nu_-,
$$
$$
 g_{rr}=\frac{t_{rr}}t-\frac{t_r^2}{t^2}
       -2\left(\frac{a_{rr}}a-\alpha^2\right)
       -(\nu_+)_r-(\nu_-)_r,\qquad
 \frac{(\mu^{-1})_{rr}}{\mu^{-1}}=g_{rr}+g_r^2 .
 \tag{WSJ.28}
$$
These equations are only a verification of the finite power recipe; they
authorize no new numerical logarithm. They show why $Q,\mu^{-1}$ at
radial order two require $\eta_{rr},q_{rr}$, whereas the second-radial
$H^{-1}$ construction from (WSJ.19) needs only $a_r,d_r$.
The extra inputs are not suppressed by the scaling.

## WSJ8. Leading amplitude and full forcing in the same ordered calculus

The old positive $G$ has the exact form
$$
 G=C_*t^{1/4}q^{-1/2}E_G,\qquad
 (E_G)_r/E_G=-\ell_0,\qquad \ell_0=2\beta\Pi S .
 \tag{WSJ.29}
$$
Read the old whole $G$ value upper and lower. The relative $E_G$ jet
through radial order three has no angular terms and has coefficients
$$
 1,\quad -t_0\ell_0,\quad
 \frac{t_0^2}{2}(\ell_0^2-(\ell_0)_r),\quad
 \frac{t_0^3}{6}(-\ell_0^3+3\ell_0(\ell_0)_r-(\ell_0)_{rr}).
 \tag{WSJ.30}
$$
Use complete positive triangles for (WSJ.30), then
${\cal R}G=\tau^{1/4}E_q^{-1/2}{\cal R}E_G$.
This forms finite derivative coefficients, not a new exponential or a
repeat of the old forward/reverse leading propagation products.
The pure angular row of $G$ uses only $\tau^{1/4}$.

The complete original leading amplitude can be factored as
$$
 a_0^{\rm amp}=\frac G2(p_+^2+p_-^2),\qquad
 b_0^{\rm amp}=\frac{i\epsilon G}{2s}(p_-^2-p_+^2),\qquad
 v_{0,\sigma}=G p_\sigma^2 .
 \tag{WSJ.31}
$$
These are precisely WUA.10--11. In particular the second component is
not omitted. Its bound keeps the whole two-term difference as a positive
sum; both $s^{-1}$ and its derivatives remain. Formula (WSJ.31)
constructs the full leading packet on ${\cal I}_{14}^3$.
It uses $q$ through radial order three and $\ell_0$ through radial
order two in (WSJ.30).

Keep the actual coefficients $e,b_{\rm loc},t_Q,T_0,r_Q,\vartheta,V_0$
of WUA.12 with their full physical background, $\Pi S$, and all
nonlocal predecessors. In particular
$t_Q=\eta_r/\eta+d_\phi+e$ and
$T_0=\eta_r/\eta-4\beta\Pi S+5d_\phi$.
They are not inferred from a principal symbol alone.

On the frozen formal jets the original differential operator is
$$
 {\cal D}_0=\partial_\xi-t_0({\cal J}d)\partial_\zeta,\qquad
 {\cal J}(DF)=t_0^{-1}{\cal D}_0{\cal J}F .
$$
Its square explicitly retains
$$
 {\cal D}_0^2F
 =F_{\xi\xi}-2t_0dF_{\xi\zeta}
    +t_0^2d^2F_{\zeta\zeta}
    +(t_0^2d\,d_\zeta-t_0d_\xi)F_\zeta .
 \tag{WSJ.32}
$$
Here $d$ denotes its full formal jet. In particular $d_\xi$ is the
true radial derivative with its scale, not zero.

The matrix called $H_D$ in WUA is
$H_D=i\epsilon(DX)Id+(DT)K_T$. It is not $\partial_rH$.
Before taking bounds use the exact ordered identity
$$
                    H^{-1}H_D=-i\epsilon QK_T .
 \tag{WSJ.33}
$$
Thus the complete first forcing is still
$$
 \binom{F_b}{F_a}
 =-\mu^{-1}\left[
       (D^2+\eta^2K\partial_\phi^2-T_0D+V_0)w_0
                    +i\epsilon\vartheta QK_Tw_0\right].
 \tag{WSJ.34}
$$
This preserves the full $\vartheta$ term. It does not replace the
complete scalar residual by its local part.

Equations (WSJ.27), (WSJ.31)--(WSJ.34) give an explicit ordered positive
recipe for both forcing components on ${\cal I}_{12}^1$.
The demand for $w_0$ at radial order three is essential: differentiating
$D^2w_0$ once in $r$ needs that third row. A packet stopping at
radial order two is insufficient for the full first-transport calculation.
The old degree-fourteen/radial-three leading packet supplies a complete
fallback for any newly undeclared slot.

## WSJ9. First transport, genuine extension and the residual interface

For each actual sign and branch let $R_\sigma=v_{1,\sigma}/v_{0,\sigma}$.
The exact physical transport equation is
$$
 (\partial_r-(d+\sigma a)\partial_\phi)R_\sigma={\cal K}_\sigma,
 \quad
 {\cal K}_\sigma
 =\frac{Qp_{-\sigma}}{2G p_\sigma^2}
           \left(F_a-\frac{i\epsilon\sigma}{s}F_b\right).
 \tag{WSJ.35}
$$
Its cut value is the original nonzero local free-amplitude trace. Along
the correctly oriented true characteristic,
$$
 R_\sigma(r)=R_\sigma(r_c)\circ\chi^\sigma_{r\to r_c}
        -\int_r^{r_c}{\cal K}_\sigma(v)\circ\chi^\sigma_{r\to v}\,dv .
 \tag{WSJ.36}
$$
Both branches, all shorter intervals, the original cut trace and the
whole forcing in (WSJ.34) enter its angular Bell sum. The ordinary radial
integral is not replaced by a root reset or a chosen favorable subinterval.

Pure angular orders through twelve follow from the full cut and integrand
jets and the old flow bounds. Its first and second radial rows use
$$
 (R_\sigma)_r=v_\sigma(R_\sigma)_\phi+{\cal K}_\sigma,
$$
$$
 (R_\sigma)_{rr}
 =(v_\sigma)_r(R_\sigma)_\phi
   +v_\sigma\partial_\phi(R_\sigma)_r
   +({\cal K}_\sigma)_r,\qquad v_\sigma=d+\sigma a .
 \tag{WSJ.37}
$$
The last term requires the complete forcing's radial-one row.
Then $v_{1,\sigma}=Gp_\sigma^2R_\sigma$ and the original half-sum and
$1/(2i\epsilon s)$ half-difference give both components of $w_1$.
This is a sufficient complete ${\cal I}_{12}^2$ route, not a claim
that each listed derivative is minimally necessary.

The genuine amplitude remains
$$
 w_1^{\rm ext}=w_1+{\cal B}(T)K_Tw_0 .
$$
Use the already complete univariate potential/extension derivative ports
and their genuine full tail, with the new $T$ jets in the full finite
chain rule. The $C^{64}$ cutoff is not treated as holomorphic across its
transition. No original $C_n$, second reference, $\beta_n$, mean
primitive or $ {\cal B}$ tail is dropped.

The resulting packet has the same functions and ordered types consumed
by the ten-word N6 expansion. It does not itself evaluate a new N6
remainder or change its three exact symbol cancellations. The full
physical $J,J_r$, mean kernel, two means, every true jump and the four
waist endpoints remain separate complete objects. A source refined with
this packet must still be received in the original PW/SP windows.
No physical inverse, signed finite normalization or metric Schur gate
follows from a smaller jet bound.

## WSJ10. Complete demand table and safe fallback

The following is a sufficient replacement packet. All entries are
individual normalized coefficients of the actual function, with the
frozen radial weight (WSJ.7), not a total-degree sum.

| Node | New qualified index set | Exact route and any extra predecessor |
|---|---|---|
| $p_\pm$, $x,u$ | ${\cal I}_{14}^3$ | Individual old $\Phi$ angular orders 1--15; $d,a$ radial 0--2 |
| Relative $\omega,t,t^\alpha$ | ${\cal I}_{14}^3$ | Drift relative angular 1--14; (WSJ.17), (WSJ.20) |
| Absolute $T$, $X$, $\Phi_\pm$ derivatives | ${\cal I}_{15}^3$, lifts' value omitted | Edge identities (WSJ.21)--(WSJ.22), exact radial-only equations |
| $x,y$ for the old geometry packet | ${\cal I}_{14}^3$ | $x=(p_++p_-)/2$, $y=-u/s$ |
| $Q,\mu^{-1}$ | ${\cal I}_{13}^2$ | Positive factorization; $\eta,q$ radial 0--2 |
| Complete $H^{-1}$ | ${\cal I}_{13}^2$ (also ${\cal I}_{14}^2$ if requested) | Full (WSJ.25), not only a determinant or weighted norm |
| $G,w_0$ | ${\cal I}_{14}^3$ | $q$ radial 0--3; $\ell_0$ radial 0--2; full (WSJ.30)--(WSJ.31) |
| Both full forcing components | ${\cal I}_{12}^1$ | Leading radial three; complete background radial two; (WSJ.34) |
| Full free $w_1$ and genuine addition | ${\cal I}_{12}^2$ | Full cut trace, all-shorter flow, forcing radial one, complete extension |

In particular $|{\cal I}_{14}^3|=54$,
$|{\cal I}_{15}^3|=58$, $|{\cal I}_{13}^2|=39$,
$|{\cal I}_{12}^1|=25$, and $|{\cal I}_{12}^2|=36$.
These are exact index counts, not new computed scalar counts.

The independent relative-angular-$\omega$ output still ends at fourteen.
If a consumer specifically asks for relative order fifteen, it must use a
separately declared complete route, for example the old absolute phase
order fifteen divided by the true positive $\omega$ lower. The edge
construction for $T$ does not relabel that different output as already
supplied.

For every requested node and $(p,q)$, a future driver records one of:
new complete mixed recipe; exact identity; or read-only old complete
fallback. The old WGS coefficient convention is
$\|\partial_r^p\partial_\phi^q F\|/(p!q!)$, with its entire fixed group
maximum dominating the requested coefficient. A valid old-to-scaled
fallback is $t_+^p$ times that original upper. A valid new-to-ordinary
conversion is $t_-^{-p}$ times the new scaled bound. Factorials are
restored only when an ordinary derivative is requested.

The fallback must have the same actual function, domain, component norm,
free/genuine normalization and inverse direction. Local $X-\phi$
receives its exact identity derivative only in its original local
realization; there is no additional identity term in $X_r$.
An omitted lift value cannot be decoded as zero.

If both old and new complete bounds are retained for the same exact
scalar norm, their finally saved upper endpoints may select a whole
bound with the old winning equality. This selects no operator entries
and subtracts no norms. A graph with a missing predecessor remains
incomplete; it is not repaired by deleting that term.

For products with known $t$-weights, keep the exact powers and their
ordered coefficients until the complete identity is formed. Positive
powers use an upper value and negative powers a lower value. In
particular do not first pay $t_-^{-2}$ for every radial term and then
forget that an exact neighboring factor contained a power of $t$.
Conversely do not cancel a weight merely because two independent
positive bounds look similar.

## WSJ11. Executable boundary and complete scope

A scalar implementation can use finite arrays indexed by the explicit
pairs above. The constant coefficient is retained separately; no
degree-five-through-six or degree-ten-through-twelve maximum is fed back
as an individual new angular derivative. For rational powers use the
finite coefficient algorithm (WSJ.9), and for all other nodes use the
displayed ordered products and recurrences.

The natural complete graph groups are: admitted original values and
norm tags; separate background coefficient rows; both phase rows;
relative gap and powers; complete absolute geometry including edge
indices; $H^{-1},Q,\mu^{-1}$; full leading/forcing; and full
first-transport/genuine-amplitude packet. A numerical contract must fix
the exact output indices, original record paths and any new goals before
execution. Existing successful values are copied. None of these
instructions imports or calls an old mathematical producer.

Each complete graph is saved before successors read its outward upper
or positive lower. A failure retains the whole produced prefix and its
exact attempted lower if a positivity gate failed. No run, bound
evaluation, scientific library import or old target repetition has
occurred in this note.

This packet addresses the strict real coefficient calculation. It does
not extend the local analytic disk, change the true radial interface
list, delete a nonzero mean, turn a radial function into a finite column,
or establish norm continuity of the full evolution. The original
positive/root response, the complete negative receiver, all four waist
terms, the finite complement and every compatibility row retain their
places in the whole operator.

## WSJ12. Immutable evidence

All source bodies listed here were inspected as complete UTF-8 text,
without importing or evaluating their mathematics.

| Primary or current record | Git blob | Bytes | SHA-256 |
|---|---|---:|---|
| WUA: global real genuine trial, WUA.6--16 | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WGS complete finite-jet contract | 4980f1a2c119b6470afc24a2fc662c75fa210479 | 28978 | 4d3638fe6ae8793b937d4c7f57a4c092d59d41df94991722d8b622ed958e576e |
| WGS no-entry math module, exact finite recurrences | afa3b49b2035be07abee6a7f9041899c135dcdea | 31846 | cb9c9aa0f7e5749967ece4e51210f359b4c58eecc7f83a05040607543ac47621 |
| WGS actual main, run 43820816332/1 | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| WGS actual original-input companion, same run | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| WX true waist coordinates, WX.12 and all-shorter scope | ef394649b79b06e27d7d3a36bdf98a7fcd801039 | 20033 | c5157bbb14b300c1a418642e96917b49f0f90c1ebc3571a124a26b863adc9ae1 |
| DX4 complete fourth flow derivatives, DX.14 | f89dda096499d6ca8ee07afd0ffecf2b490ecb41 | 15978 | 6b493e3792c6863f9a65d8d52d994697d37de416157b68ed21f2cee51182f58b |
| L.5 full first Airy forcing and radial inverse jets | 2451ca1c639f04dd69de5c01ff25e59c65a6abb3 | 15780 | a798e93d73aa64115cb43313985054e0d682a41fd1393f4efea4704301699e3a |
| Complete ordered N6/true-jump/receiver module | 3288b02946fc2c53d70505cfcbabd6a5c1f841eb | 53183 | b8332d68174c8ae524874cc293cc8e65793f570bf733726d80d2f4d60f9bcdb4 |

The WUA path is [the global genuine trial](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md).
The WGS path is [the complete global free-jet contract](R133-supplement-complete-global-fold-and-free-first-transport-finite-jets.md).
Its math source is scripts/fourfold_codazzi_global_fold_free_transport_jet_math.py.
The actual pair is under notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/
as actual-scientific-conclusion.json and complete-original-inputs.json.

The current main proves its complete old 437-slot graph with all 24 gates
passed. Its original 66 current scalar copies, 40 historical scalar
copies, nine scopes and complete 72-leaf local coefficient object remain
unchanged. Those successful targets are not this note's new relative
and separately indexed goals. The forthcoming drift-angular certificate
must keep its own complete input identities and must not be marked
numerically successful before its actual computation.
