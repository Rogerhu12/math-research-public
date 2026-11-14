# R133 supplement: exact ordered scalar root operator and its one-gain radial remainder

2026-11-14, visible-exact-astra-0df / phase_inverse.

**Proved:** the complete moving root scalarization has an exact second-order
form whose only nonsmoothing radial first-order coefficient is the scalar
$\eta_r/\eta-4b\langle u^2+Kv^2\rangle+5d_\phi$. The apparent angular
first-order term in $AC$ cancels exactly. All residual operator terms,
projections, independent mean and ordinary source ports remain.

This is a structural theorem for the actual moving operator. Its
application uses the full inverse $J=A^{-1}$ already proved in
[the complete moving root scalarization](R133-supplement-complete-moving-root-scalarization.md),
including the successful public root budget in run 43594466882.
It supplies a more precise input to a turning-point construction. It
does not assert that a current full two-row Airy connector or its strong
return remainder has been constructed.

## 1. Spaces, parity and exact operators

Let $\partial=\partial_\phi$, $P=1-\Pi$, $I=\partial^{-1}P$, with
period $\pi/2$. The two states have the reflection parities: $h_1$ is
odd, while $h_2$ is even. Write $f=Ph_2$, $z=\Pi h_2$, and
$$
 \eta=-\gamma m,\quad m=\Pi v,\quad S=u^2+Kv^2,\quad
 d=-bIS,\quad D_0=\partial_r-\mathcal D,\quad
 \mathcal D=PM_d\partial P.                         \tag{O.1}
$$
All compositions below are on the indicated parity spaces, and $P$
is retained on every even mean-zero space. The metric coefficients
$b,K,\gamma$ and $\eta$ are independent of $\phi$.

Use the complete operators from (N.4)--(N.5) of the cited scalarization:
$$
 \begin{split}
 e&=-b(1+3u^2+Kv^2),\qquad b_0=b(1-u^2-3Kv^2),
       \qquad \ell=-2buv,\\
 N_A&=-2bP M_{v_\phi}I M_uP,&
 N_C&=-2bP M_{u_\phi}I M_vP,\\
 N_E&=-2bP M_{u_\phi}I M_uP,&
 N_B&=-2bK P M_{v_\phi}I M_vP,\\
 L&=PM_\ell P+N_A,&M&=PM_\ell P+N_C,\\
 A&=\eta\partial+L,&C&=-\eta\partial+M,\\
 E&=PM_eP+N_E,&B&=PM_{b_0}P+N_B .
 \end{split}                                                    \tag{O.2}
$$
Thus $A$ maps odd states to even mean-zero states, $C$ maps in the
opposite direction, $B$ acts on even mean-zero states and $E$ on odd
states. The symbol $M$ without a subscript in (O.2) denotes the displayed
operator; $M_a$ denotes multiplication by $a$.

For an operator depending on $r$, write
$$
 [D_0,T]=T_r-[\mathcal D,T].                         \tag{O.3}
$$
This is the actual radial commutator between its correct input and output
spaces. It includes the derivative of the original coefficients.

On a fixed Sobolev window, $\mathcal O^{-q}$ will mean a bounded map
$H^s\to H^{s+q}$ for each indicated $s$, with the necessary full
coefficient bounds supplied. Smooth finite-rank mean maps are retained
and belong to every such class on any fixed window. The notation never
means that a finite Fourier section has replaced the operator.

The original $I$ has a complete one-order gain on mean-zero states.
Multiplication by the actual smooth coefficients is bounded on each
fixed Sobolev space. The complete certified $J=A^{-1}$ has one gain,
on its declared windows. These facts will suffice for every order
statement below; no formal symbol calculus is needed.

## 2. The exact cancellation in the product $AC$

Since the two local order-zero multipliers in $A$ and $C$ are the same
$\ell$, their first-order products cancel:
$$
 AC=-\eta^2\partial^2+V_{AC},\qquad
 V_{AC}=\eta PM_{\ell_\phi}P
          +\eta\partial N_C-\eta N_A\partial+LM.      \tag{O.4}
$$
This is an exact identity. It uses $\partial P=P\partial=\partial$ and
the fact that $\eta$ has no angular derivative.

Every term of $V_{AC}$ is bounded with angular order zero. In particular,
the primitive may not be commuted through its multipliers without
retaining its projection:
$$
 \begin{split}
 \partial N_C
   &=-2bP\{M_{u_{\phi\phi}}I M_v
                         +M_{u_\phi}P M_v\}P,\\
 N_A\partial
   &=-2bP M_{v_\phi}\{P M_u-I M_{u_\phi}\}P.
 \end{split}                                                    \tag{O.5}
$$
The second identity uses the complete relation
$I M_u\partial=P M_u-I M_{u_\phi}$.

For example, if $U_j,V_j$ bound the complete ordinary Wiener norms
of $\partial^ju,\partial^jv$, put
$$
 \begin{split}
 \ell_j&=\|\partial^j\ell\|_{\mathcal A_0},\\
 L_*&=\ell_0+\frac{|b|}{2}V_1U_0,\qquad
 M_*=\ell_0+\frac{|b|}{2}U_1V_0 .
 \end{split}
$$
Then a sufficient complete ordinary $L^2$ norm is
$$
 \|V_{AC}\|
 \le |\eta|\ell_1
    +2|b\eta|\{V_0(U_1+U_2/4)+V_1(U_0+U_1/4)\}
    +L_*M_* .                                      \tag{O.6}
$$
The factors $1/4$ are the actual fourfold primitive norm.

Keeping only its multiplication coefficient, without removing its
remainder, (O.4) also gives
$$
 V_{AC}
 =P M_{-4b\eta\,v u_\phi+4b^2u^2v^2}P
       +\mathcal O^{-1}.                            \tag{O.7}
$$
For instance, the terms $PM_\ell P M_\ell P$ and
$PM_{\ell^2}P$ differ by the complete finite-rank operator
$-PM_\ell\Pi M_\ell P$. All analogous projection terms in (O.5) are
part of the remainder in (O.7), rather than assumed zero.
Only (O.4), not a truncated version of (O.7), is used next.

## 3. An exact second-order equation with every source retained

Let
$$
 F_2=zb_2+Pg_2,\qquad
 Q=([D_0,A]+AE)J .                                  \tag{O.8}
$$
The independent mean still satisfies the complete equation
$$
 z_r=\{b(1-\langle S\rangle)-2bKm^2\}z
       -2bm\langle uh_1+K(v-m)f\rangle+\langle g_2\rangle .
                                                               \tag{O.9}
$$
Here $b_1,b_2$ are precisely those in (N.5), not new local
approximations.

From $AJ=1$ and the differentiated identity
$A[D_0,J]=-[D_0,A]J$, one obtains
$$
 A(D_0-E)J=D_0-Q .                                  \tag{O.10}
$$
Multiplying the exact weak scalarization by $A$ therefore gives
$$
 \boxed{
 \{D_0^2+\eta^2K\partial^2-TD_0+V\}f
       =Ag_1+(D_0-Q)F_2+A(zb_1),}
                                                               \tag{O.11}
$$
where the ordered operators are
$$
 T=B+Q,\qquad V=QB-[D_0,B]-K V_{AC}.                 \tag{O.12}
$$
Indeed,
$(D_0-Q)(D_0-B)=D_0^2-(Q+B)D_0+QB-[D_0,B]$.
No $K^{-1}$ or $(-K)^{-1/2}$ has been introduced.

The reconstruction remains
$$
              h_1=J\{(D_0-B)f-F_2\},\qquad h_2=f+z. \tag{O.13}
$$
Equations (O.9), (O.11) and (O.13) are equivalent to the original
two complete moving rows wherever the proved $J$ is available.

The interpretation of the source is essential. For an ordinary radial
$L^2$ source, $(D_0-Q)F_2$ in (O.11) is a distributional flux, as
$F_2$ is inside the differentiated expression. The original weak
form (N.8) and reconstruction (O.13) specify its graph domain. There
is no request that $\partial_rg_2$ itself belong to $L^2$, and
$Ag_1$ may be interpreted in the appropriate negative angular
Sobolev space. A source theorem for (O.11) must pay this full weak
pair of source terms.

## 4. The scalar part of the radial first-order coefficient

Define the angular scalar functions
$$
 t_Q=\eta_r/\eta+d_\phi+e,\qquad
 T_0=t_Q+b_0.
$$
The exact remainder operator
$$
 R_Q=[D_0,A]+AE-PM_{t_Q}PA                         \tag{O.14}
$$
is of angular order zero. More explicitly,
$$
 \boxed{
 R_Q=L_r-[\mathcal D,L]+\eta PM_{e_\phi}P
          +\eta\partial N_E+LE-PM_{t_Q}PL .}          \tag{O.15}
$$
To verify this formula, expand
$$
 \begin{split}
 [D_0,A]
    &=\eta_r\partial+L_r+\eta PM_{d_\phi}\partial P
                                      -[\mathcal D,L],\\
 AE&=\eta PM_e\partial P+\eta PM_{e_\phi}P
                                      +\eta\partial N_E+LE.
 \end{split}
$$
The three first-order terms are exactly
$PM_{t_Q}P\,\eta\partial$ and cancel in (O.14).
This computation is between the odd and even mean-zero spaces;
none of their projection factors has been dropped.

The commutator in (O.15) is bounded with order zero. Its local part
has the exact finite-rank correction
$$
 [\mathcal D,PM_\ell P]
       =PM_{d\ell_\phi}P-PM_\ell\Pi M_{d_\phi}P.      \tag{O.16}
$$
For its primitive part, each product
$\mathcal D N_A$ and $N_A\mathcal D$ is already bounded with
order zero. Formula (O.5) and
$M_d\partial=\partial M_d-M_{d_\phi}$ give complete bounds.
The same argument applies to $[\mathcal D,B]$ in (O.12).

For reference, writing $d_j^*=\|\partial^jd\|_{\mathcal A_0}$,
a direct bound at order zero is
$$
 \begin{split}
 \|[\mathcal D,L]\|
 \le{}&d_0^*\ell_1+\ell_0d_1^*\\
 &+2|b|d_0^*\{U_0(V_1+V_2/4)+V_1(U_0+U_1/4)\}
       +\frac{|b|}{2}V_1U_0d_1^* .                    \tag{O.17}
 \end{split}
$$

Now use $AJ=1$ in (O.14):
$$
 Q=PM_{t_Q}P+R_QJ,\qquad
 T=PM_{T_0}P+R_{-1},\qquad R_{-1}=N_B+R_QJ.          \tag{O.18}
$$
Both terms in $R_{-1}$ have one full angular gain on every
declared window for which the coefficient multipliers and $J$
have the required bounds. This is an operator identity with an
actual gain, rather than a formal omission of $R_{-1}D_0$.

Finally,
$e+b_0=-4bS$ and $d_\phi=-b(S-\langle S\rangle)$ give
$$
 \boxed{
       T_0=\eta_r/\eta-4b\langle S\rangle+5d_\phi .}  \tag{O.19}
$$
Thus the only angularly varying nonsmoothing radial coefficient
is the explicitly known $5d_\phi$.

Because $Q,B$ and $[\mathcal D,B]$ have order zero, and $B_r$
is an actual coefficient derivative, the complete $V$ in
(O.12) also has angular order zero. All products in that expression
remain ordered.

## 5. Radial regularity and the already certified domains

The actual complete root budget covers the repaired explicit family
$|\delta|\le10^{-8}$, at $\eta_0$, on radial disks of radius $10^{-5}$
and moving angular width $1/1024$. Its full angular inverse is proved
on ordinary $L^2$, analytic Hilbert and Wiener spaces, with declared
integer and fractional Sobolev bounds. Derivatives such as $L_r$,
$B_r$ and $\eta_r$ require an inner radial disk and must be paid.

For example, on the inner half-disk the Banach-valued Cauchy bound is
$2/R$ times the corresponding complete outer-disk norm. The scalar
$\eta_r/\eta$ additionally uses the genuine nonzero gap of $\eta$.
Using a smaller oscillation enclosure for $\eta$ instead of its
absolute value is legitimate only if that full enclosure is supplied.
No small radial derivative is inferred merely from an approximate
solution residual.

The stated one-gain property of $R_{-1}$ at a Sobolev index $s$
uses $R_Q:H^{s+1}\to H^{s+1}$ and $J:H^s\to H^{s+1}$.
For higher indices one must supply the additional complete multiplier
derivatives, or pay a positive angular strip loss by Cauchy.
The present explicit family has finite moving Fourier degree at most
96; its products can have degree 192 and its primitive intermediate
retains its true range. That finite degree does not apply to an unknown
nonlinear PDE correction.

## 6. The precise turning-point input and what remains

The full scalar differential expression is now
$$
 \boxed{
 D_0^2+\eta^2K\partial^2
       -PM_{\eta_r/\eta-4b\langle S\rangle+5d_\phi}P\,D_0
       -R_{-1}D_0+V .}                             \tag{O.20}
$$
It has the exact simple-root principal part, a specified local scalar
radial coefficient, a one-gain radial remainder, and a bounded angular
potential. Its independent mean and weak sources are (O.9)--(O.13).

This is closer to a genuine Airy input than an equation with an
unclassified radial commutator. It is still not already the scalar
Airy model. A local change of the radial and angular variables may turn
a fixed-$r$ angular primitive into an integral along a nonconstant
new-radial curve. An estimate at each new radial coordinate cannot be
claimed by relabelling it as the old primitive. Likewise, eliminating
a radial first-order term by a gauge requires keeping its commutators
with the principal angular operator and all endpoint graph changes.

Once the actual local principal normalization, two-row root and
positive ports, and the appropriate transformed operator/source bounds
are supplied, (O.20) is the exact complete input for its perturbation
argument. The strong order $4/3$ return remainder and the finite root
constant in the directed return-word contract remain separate
quantitative obligations. No previously computed finite part is
promoted to the complete returned coefficient by this algebra.
