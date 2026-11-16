# R913 — The original Igusa Cartier functional and its two distinct CM companions

Date: 2026-11-16. Status: **proved for the original objects and labels of R908–R911**. The actual upper-half additive subgroup supplies a nonzero functional on a specified Cartier cokernel. Its Igusa weight is different from the weight of the possible first nonzero good-model cotangent layer. Both weights have explicit complete Fourier companions for the same original label. The proof does not assert that this functional detects the named CM vector, or that the indicated cotangent layer is nonzero.

**Convention clarification (2026-11-16).** In §2 the geometric dual endomorphism $\delta^D$ is now distinguished explicitly from the contragredient semilinear descent of R911. The former has the same scalar on the dual additive coordinate and its usual tangent map. This corrects only the justification of the already stated $\zeta^2$ Lie character; no character value, displayed formula, theorem, or remaining nonvanishing boundary changes.

## 1. Original objects and the two weights

Retain
$$
p\ge41,\quad p\equiv2,5\pmod9,\quad
n=p+1,\quad e=p^2-1,\quad
\mathcal H=\{1\le h\le p:h\equiv1\pmod6,\ (h,n)=1\}.
\tag{913.1}
$$
Use the original $X_p$, positive CM quotient $q:J_{X_p}\to A$, rigidification at $c_0$, and centering at $c_1$ of R906–R911. Thus, for the actual Raynaud abelian part $B$ and the original integral target projector,
$$
e_hq_B=[p^{a_h}]\circ f_h,\qquad a_h\ge0.
\tag{913.2}
$$
Neither $a_h$ nor the original integer scale of $q$ is changed below.

Fix an upper-half label $h>n/2$. Set
$$
r=2h-n,\qquad
k_+=r+2=2h-p+1,\qquad
k_-=p+1-r=2p+2-2h.
\tag{913.3}
$$
R911 proves that $r$ is the actual nontrivial Raynaud comparison scale for this label. In particular
$$
0<r<p-1,\quad
4\le k_+\le p-7,\quad
10\le k_-\le p-1,\quad
k_\pm\equiv4\pmod6,\quad k_++k_-=p+3.
\tag{913.4}
$$
For the endpoints, the largest allowed integer $h$ is at most $p-4$, since $h\equiv1\pmod6$ and $p\equiv5\pmod6$. The positive even integer $r$ is at least two. These facts prove (913.4), without a finite-prime check.

Write $k$ for a perfect residue field containing all the actual markings; a sufficiently large algebraic extension is harmless. To avoid confusing the field with either weight, a weight appearing as an index below always has a subscript.

The two relevant inertia characters are
$$
\chi_-(u)=\operatorname N(u)^{h-1},\qquad
\chi_+(u)=\operatorname N(u)^{1-h},
\quad
u\in\mathbf F_{p^2}^{\times},
\tag{913.5}
$$
where $\operatorname N(u)=u^{p+1}$. These characters take values in $\mathbf F_p^\times$ and are trivial for $\operatorname N(u)=-1$, since $h$ is odd. The signs in (913.5) are not interchangeable.

## 2. The additive subgroup gives a Cartier-cokernel functional

R911(911.27–28) constructs, from (913.2), an actual closed immersion
$$
\iota_h:\alpha_{p,1,h}\hookrightarrow B_{\mathrm I}^{\vee}[p].
\tag{913.6}
$$
Its Lie character is
$$
b_h=n((p-2)h+1)\pmod e,
\qquad
u^{b_h}=\operatorname N(u)^{1-h}=\chi_+(u).
\tag{913.7}
$$
The geometric deck transformation $\delta:a\mapsto\zeta a$ acts on this Lie line, through its natural dual endomorphism, as $\zeta^p=\zeta^2$. To check the convention, its original second Raynaud coordinate satisfies $\delta^*y_1=\zeta^2y_1$. The Cartier pairing obeys $e(y,\delta^Dz)=e(\delta y,z)$; in the additive reduction the pairing $\exp(y_1z_1)$ therefore gives $(\delta^D)^*z_1=\zeta^2z_1$. Its usual tangent map has the same scalar $\zeta^2$. This is a geometric endomorphism calculation, distinct from the inverse actions used for semilinear inertia descent in R911. The Picard–Serre pairing then pairs this Lie character with the $\delta=\zeta$ cotangent character used below.

Choose a nonzero tangent vector $v_h$ in the image of (913.6). Its line, rather than an arbitrary vector of the ambient Lie space, comes from the original quotient. The product of the canonical component polarizations and Picard–Serre duality of R911 give a perfect pairing
$$
\operatorname{Lie}(B_{\mathrm I}^{\vee})\times
\omega_{B_{\mathrm I}}\longrightarrow k.
\tag{913.8}
$$
Let $\lambda_h(\omega)=\langle v_h,\omega\rangle$. It is nonzero. Scaling the generator of $\alpha_{p,1,h}$ scales $\lambda_h$ by an element of $k^\times$; no normalization by its value on a proposed test vector is made.

Let
$$
W_h^+=
(\omega_{B_{\mathrm I}})_{\chi_-,\,\delta=\zeta},
\qquad
W_h^-=
(\omega_{B_{\mathrm I}})_{\chi_-,\,\delta=\zeta^2}.
\tag{913.9}
$$
The first subscript specifies the full inertia character, including the action that interchanges the two Igusa parts when that occurs. The actual tame quotient is already included in $B_{\mathrm I}$. By equivariance of (913.8), the functional is supported on $W_h^+$.

Let $\mathcal C$ be the Cartier operator on the invariant differentials, or equivalently on the normalized component curves. It is $p^{-1}$-linear. The restricted $p$ operation on the Lie algebra is dual to Cartier:
$$
\langle v^{[p]},\omega\rangle
=\langle v,\mathcal C\omega\rangle^p.
\tag{913.10}
$$
This is the Picard/Cartier description of the restricted Lie algebra; Oda, §4, printed p. 110, and §5 give this identification. It can also be checked in the Serre pairing by the local residue identity
$\operatorname{Res}(g^p\omega)=
\operatorname{Res}(g\,\mathcal C\omega)^p$.

Since (913.6) is a group homomorphism and the restricted $p$ operation on $\operatorname{Lie}(\alpha_p)$ is zero, $v_h^{[p]}=0$. Consequently $\lambda_h$ annihilates the Cartier image. Naturality and semilinearity give
$$
\mathcal C(W_h^-)\subset W_h^+:
\quad
(\zeta^2)^{1/p}=\zeta,\qquad
\chi_-^{\,1/p}=\chi_-.
\tag{913.11}
$$
Projection to these character spaces uses groups of order prime to $p$, so no other character contributes to that image. We obtain the genuine nonzero functional
$$
\boxed{\quad
0\ne\lambda_h\in
\left(W_h^+/\mathcal C W_h^-\right)^\vee .
\quad}
\tag{913.12}
$$
This is a cokernel statement. An additive Lie line does not canonically give a holomorphic vector in $\ker\mathcal C$, and (913.12) must not be replaced by such a statement. In particular the two $\delta$ characters in (913.11) must be retained.

## 3. Étale Igusa points and multiplicative Igusa structures

The sign determining the weight is fixed by the original moduli problem, not by a choice of notation for a character.

Edixhoven–Parent, §2.1, describes an ordinary full-$p$ point by its kernel line and an induced isomorphism to the étale group $E[p](k)$. Their ordinary component is the exotic Igusa curve. The isomorphism from the usual Igusa problem is
$$
(E,P\in E^{(p)}[V])
\longmapsto (E^{(p)},(0,P)).
\tag{913.13}
$$
All auxiliary tame markings are transported along the same Frobenius isogeny.

Gross, §5, instead uses an embedding
$$
\beta:\mu_p\hookrightarrow E[p].
\tag{913.14}
$$
His canonical section $\mathfrak a$ has
$$
\mathfrak a^{p-1}=A,\quad \mathfrak a(q)=1,\quad
\langle d\rangle_p^*\mathfrak a=d^{-1}\mathfrak a
\quad(\beta\mapsto d\beta).
\tag{913.15}
$$
These are Proposition 5.2, with a simple zero at every supersingular Igusa point.

The point $P$ and $\beta$ are paired by the canonical $F/V$ duality. Replacing $P$ by $aP$ replaces $\beta$ by $a^{-1}\beta$. Hence a weight-$k_0$ cusp form has associated Igusa differential
$$
\Phi_{k_0}(F)=\frac16\operatorname{KS}
\left(F/\mathfrak a^{\,k_0-2}\right),
\tag{913.16}
$$
and its character for $P\mapsto aP$ is
$$
a^{-(k_0-2)}.
\tag{913.17}
$$
Here KS denotes the Kodaira–Spencer identification on the Igusa curve. The factor $1/6$ only specifies the original full-six cusp parameter: if $q=Q^6$, then
$$
\Phi_{k_0}(F)=F(Q)\,dQ/Q
\tag{913.18}
$$
at the marked cusp. Without this factor the expansion is $6F(Q)dQ/Q$. No ramified factor is absorbed in (913.16). Gross Proposition 5.7, or Cais Proposition 3.1 for the tame moduli problem, makes this an isomorphism with the appropriate holomorphic differential eigenspace when $2<k_0<p$.

For scalar $u=a\in\mathbf F_p^\times$, the actual index-restoring Cartan element is $aI$. It sends the ordinary generator to $aP$, whereas $\operatorname N(u)=a^2$. Therefore the inertia character $\chi_-$ in (913.9) requires
$$
-(k_0-2)\equiv 2(h-1)\pmod{p-1}.
\tag{913.19}
$$
The unique solution with $2<k_0<p$ is $k_0=k_-$. Thus (913.12) belongs to the actual weight-$k_-$ Igusa Cartier cokernel.

This scalar calculation does not discard the remaining norm character. If $p\equiv1\pmod4$, the original normalizer has two Igusa parts of type $\mathrm{Ig}(p)/C_4$. Its full inertia eigenspace is obtained by extending the differential on either part to the other with the specified full character $\chi_-$; the value on a chosen nonsquare norm remains $\operatorname N(u)^{h-1}$. The stabilizer consists of square norms, and (913.19) proves compatibility on it. Also $k_--2$ is divisible by four, so the differential descends through $C_4$. If $p\equiv3\pmod4$, there is one part of type $\mathrm{Ig}(p)/\{\pm1\}$. A nonsquare norm is $-a^2$; the original $w_1$ changes the generator only by $-1$, already killed by the quotient. Since $h-1$ is even, its character is again exactly (913.5). This proves the full-character comparison in both cases.

The tame level quotient is taken throughout by its actual finite group. Its order is prime to $p$; averaging and pullback therefore preserve these identifications. Passing through (913.13) transports differentials on the *Igusa curves*. It does not pull a nonzero elliptic invariant differential through Frobenius, whose differential is zero.

## 4. The possible first cotangent layer has the other weight

Use the original unit generator $\omega_h$ of the positive target cotangent line. R908–R911 prove the integrality of
$$
L_h=\varpi^{-pr}f_h^*\omega_h\in\omega_B.
\tag{913.20}
$$
The reduction $\overline L_h$ is allowed to be zero. Its full coordinate-ring inertia character, if nonzero, is
$$
t_h-pr
=(p-1)h-p(2h-n)
=n(p-h)\equiv n(1-h)\pmod e.
\tag{913.21}
$$
Its $\delta$ character is still $\zeta$.

No Drinfeld holomorphic differential has this nontrivial norm character. Indeed R911 lists its possible characters as $(p-1)j$ with $0<j<n/2$ odd; divisibility by $n$ would imply $n\mid2j$, which is impossible. Thus
$$
\overline L_h\in
(\omega_{B_{\mathrm I}})_{\chi_+,\,\delta=\zeta}.
\tag{913.22}
$$
Applying (913.17) now gives
$$
-(k_0-2)\equiv2(1-h)\pmod{p-1},
\tag{913.23}
$$
whose solution in $2<k_0<p$ is $k_0=k_+$.

The full-norm extension is the one with character $\chi_+$, not the extension with $\chi_-$. The same two-component argument applies. When $p\equiv1\pmod4$, $k_+-2$ is divisible by four; when $p\equiv3\pmod4$ only evenness is needed.

Consequently the actual objects occur on different sides:
$$
\begin{array}{c|c|c}
\text{original object}&\text{cotangent inertia character}&
\text{usual Igusa weight}\\ \hline
\lambda_h\text{ on its paired space}&\chi_-&k_-\\
\overline{\varpi^{-pr}f_h^*\omega_h}&\chi_+&k_+
\end{array}
\tag{913.24}
$$
The first row is nonzero as a functional on a Cartier cokernel. The second row has not been proved nonzero. Equating these rows would ignore both duality and the power $\varpi^{pr}$.

## 5. Complete same-label Fourier companions

Use the original raw untwisted form and chosen inert coefficient place:
$$
f_h=f_{\Psi_h},\qquad
\Psi_h((a))=a\,\epsilon_3(a)[a]^{-h(p-1)},\qquad
N(f_h)=9p^2.
\tag{913.25}
$$
This is R575/R869's raw form. The actual positive cubic descent $\kappa_4$ is still the original change $a=\sqrt[3]4\,u$, locally by the fixed unit $\sqrt[3]4\in\mathbf Z_p^\times$. It is not inserted into (913.25) or reversed.

For either $k_0=k_\pm$, define the tame CM form
$$
F_{k_0}=f_{\Xi_{k_0}},\qquad
\Xi_{k_0}((a))=a^{k_0-1}\epsilon_3(a).
\tag{913.26}
$$
Because $k_0-1$ is odd and divisible by three, the unit compatibility is the same as in R869(869.22–24). The finite conductor is $(\sqrt{-3})$, the modular level is $9$, the nebentypus is trivial, and $a_1(F_{k_0})=1$. Conjugating the ideals shows its coefficients are rational algebraic integers. The point of this construction is the fixed original inert place; no conductor-$p$ character has been replaced in characteristic zero.

Write $\Theta_q=q\,d/dq$. Reduction of (913.25) gives the ideal term $a^{1-h(p-1)}\epsilon_3(a)$. For $(a,p)=1$,
$$
\begin{aligned}
(k_+-1)+(p+1)(p-h)
&=1-h(p-1)+(p^2-1),\\
p(k_--1)+(p+1)(h-1)
&=1-h(p-1)+2(p^2-1).
\end{aligned}
\tag{913.27}
$$
In the second line reindex the ideals of $F_{k_-}$ by conjugation and use $\bar a=a^p$ in the residue field. The finite sign $\epsilon_3$ is unchanged. If $p$ divides an ideal norm, the original term is omitted; the companion term is divisible by $p^{k_0-1}$ and hence is zero modulo $p$. The prime above three is omitted in all forms. This proves the complete equalities
$$
\boxed{
\bar f_h=
\Theta_q^{\,p-h}\overline F_{k_+}
=
\Theta_q^{\,h-1}\overline F_{k_-}.}
\tag{913.28}
$$
All three series have zero $p$-multiple Fourier coefficients. Thus
$\Theta_q^{p-1}$ acts as the identity on them, and
$$
\begin{aligned}
\overline F_{k_+}&=\Theta_q^{\,h-1}\bar f_h,&
\overline F_{k_-}&=\Theta_q^{\,p-h}\bar f_h,\\
\overline F_{k_+}&=\Theta_q^{\,r}\overline F_{k_-},&
\overline F_{k_-}&=\Theta_q^{\,p-1-r}\overline F_{k_+}.
\end{aligned}
\tag{913.29}
$$
In particular $U_p\overline F_{k_\pm}=0$. These are complete Fourier statements, not equalities of sections of unequal weights without their Hasse/Igusa transport.

## 6. The original six-level vector and its phase

Keep the original CRT cusp and tame marking of R869, with
$$
\mathcal V_h(Q)=f_h(Q)-4\zeta^2f_h(Q^4).
\tag{913.30}
$$
For the companion define, on that transported full-six marking,
$$
V_{k_0}^{\dagger}(Q)
=F_{k_0}(Q)-2^{k_0}\zeta^2F_{k_0}(Q^4).
\tag{913.31}
$$
This is the actual two-oldform direction, not an arbitrary linear combination selected by its CM value.

Here is a direct check of the uniform dependence on $k_0$. Put
$H_0=F_{k_0}(\tau/6)$ and $H_2=F_{k_0}(2\tau/3)$. The inert prime two gives
$a_2=0$ and $a_4=-2^{k_0-1}$, whence
$$
F_{k_0}(-Q)=-F_{k_0}(Q)-2^{k_0}F_{k_0}(Q^4).
\tag{913.32}
$$
The Fricke eigenvalue at nine is one. One can verify its sign without a local sign convention: $F_{k_0}(\tau/3)$ is invariant under $\Gamma(3)$, has $T$ eigenvalue $\zeta$, and is a Fricke eigenvector. The relation $(ST)^3=S^2$ forces its $S$ eigenvalue to be one. Therefore in the normalized basis
$(H_0,2^{k_0}H_2)$ the matrices are
$$
H_0|S=2^{k_0}H_2,\quad
(2^{k_0}H_2)|S=H_0,
\qquad
H_0|T=-\zeta^2(H_0+2^{k_0}H_2),\quad
(2^{k_0}H_2)|T=\zeta^2(2^{k_0}H_2).
\tag{913.33}
$$
They are the same matrices as for the weight-four vector in R869. Its actual $H_6$-invariant line on the conjugate marking is consequently (913.31). The $Q_8$ kernel and the mod-two standard plane are unchanged; the normalized matrices, rather than a dimension count, supply this identification.

The relative Frobenius in (913.13) multiplies the six-level Weil pairing by $p\equiv-1\pmod6$. The original determinant-$-1$ correction of R575(575.14) therefore remains part of the transport to the fixed pairing component. It conjugates the mod-three deck generator to its inverse. On the pre-Frobenius marking $T^2$ acts on (913.31) by $\zeta$, whereas on its six-level Hauptmodul $T^2$ is $\delta_\zeta^{-1}$. After the stated correction the corresponding original differential has $\delta$ character $\zeta$, as required in (913.9) and (913.22).

This describes the same marked transport as R869(869.27–30), not a new choice of the six-level phase. In particular, changing $\zeta^2$ to $\zeta$ without transporting the CM marking would change the vector. The curve is still the original $X_1$ and its actual quotient; no replacement by the untwisted $Y$ or by a different $c_Y$ eigenspace is involved.

The two exact oldform factors can now be checked directly:
$$
k_-+2(h-1)=2p,\qquad
k_++2(p-h)=p+1.
\tag{913.34}
$$
Since $2^{2p}\equiv2^{p+1}\equiv4\pmod p$, (913.28) gives
$$
\boxed{
\overline{\mathcal V_h}
=\Theta_Q^{\,h-1}\overline V_{k_-}^{\dagger}
=\Theta_Q^{\,p-h}\overline V_{k_+}^{\dagger}.}
\tag{913.35}
$$
These formulas include both the original oldform coefficient four and the unchanged $\zeta^2$ phase.

## 7. The complete Hecke correction agrees with the same label

We give the correction because matching an inertia weight alone would not identify the correct Hecke packet.

Let $\ell\nmid6p$ be prime and let $\phi:E\to E'$ have degree $\ell$. On full $p$ level the natural isogeny correspondence multiplies the Weil-pairing index by $\ell$. Choose $u$ with $\operatorname N(u)=\ell\bmod p$. Edixhoven–Parent (12) shows that composing it with $\gamma(u)$ restores the index and leaves the ordinary level datum unchanged. The resulting correspondence on the usual Igusa parameter is
$$
P\longmapsto \phi^{(p)}P.
\tag{913.36}
$$
For a differential of full inertia character $\chi$, pullback therefore gives
$$
T_\ell^{\rm orig}=\chi(u)^{-1}T_\ell^{P}.
\tag{913.37}
$$
The value is independent of the choice of $u$, because $\mu_{p+1}$ acts trivially on the actual Igusa contribution. For nonsquare norms the same equation includes the actual interchanged component; the extension in §3 supplies its stated character, not an omitted sign.

The multiplicative structure paired to $\phi^{(p)}P$ is
$$
\beta'=\ell^{-1}\phi\beta.
\tag{913.38}
$$
Indeed the isogeny multiplies the $F/V$ pairing by $\ell$. Gross's standard prime-to-$p$ Hecke correspondence uses $\phi\beta$, so (913.38) inserts $\langle\ell^{-1}\rangle_p$. By (913.15–17), on weight $k_0$,
$$
T_\ell^{P}=\ell^{-(k_0-2)}T_\ell^{\rm Gross}.
\tag{913.39}
$$
The operators here are the usual correspondence operators on curve differentials. Gross Proposition 5.9 identifies $T_\ell^{\rm Gross}$ with the weight-$k_0$ modular Hecke operator. The factor $1/6$ in (913.16) is constant and introduces no further Hecke factor.

For the two original characters, (913.37–39) become
$$
\begin{aligned}
T_\ell^{\rm orig}\bigm|_{\chi_-,\,k_-}
&=\ell^{\,1-h-(k_--2)}T_\ell^{\rm Gross}
=\ell^{\,h-1}T_\ell^{\rm Gross},\\
T_\ell^{\rm orig}\bigm|_{\chi_+,\,k_+}
&=\ell^{\,h-1-(k_+-2)}T_\ell^{\rm Gross}
=\ell^{\,p-h}T_\ell^{\rm Gross},
\end{aligned}
\tag{913.40}
$$
where the last equalities are in $\mathbf F_p^\times$. These are precisely the two twists in (913.28).

The original quotient is equivariant for the original raw prime-to-$6p$ Hecke correspondences after the fixed cubic transport. The two $\delta$ characters are kept when applying those correspondences: for a split prime they are preserved, while for $\ell\equiv2\pmod3$ they are interchanged. In the latter case the CM eigenvalue is zero. This also follows directly from the Gauss inner-twist operator of R575(575.15–20):
$R_{\rm can}T_\ell=\chi_{-3}(\ell)T_\ell R_{\rm can}$, hence the corresponding relation for $\delta$ and $\delta^{-1}$. Thus no assertion that every $T_\ell$ is an endomorphism of $W_h^+$ alone is used. The relation extends to $q_B$, to $f_h$ by complete-BT full faithfulness, and to the genuine finite-flat quotient and its dual by flat closure. The reduced Hecke eigenvalues are in $\mathbf F_p$: this follows already from (913.28) and the integral rational coefficients of $F_{k_\pm}$.

The transpose correspondence has the same action in the present spaces. Composing an isogeny with its dual gives the scalar $\ell$ on the level; this scalar lies in the full non-split Cartan and is $\pm I$ at level six, hence is already identified in the original quotient. Thus the Serre pairing transports the original Hecke action to the dual functional without an additional diamond.

It follows that the weight-$k_-$ functional of (913.12), transported by (913.16), satisfies
$$
\lambda_h(T_\ell^{\rm Gross}F)
=a_\ell(F_{k_-})\,\lambda_h(F).
\tag{913.41}
$$
If the layer $\overline L_h$ in (913.20) is nonzero, its weight-$k_+$ image is an eigenvector with
$$
T_\ell^{\rm Gross}\overline L_h
=a_\ell(F_{k_+})\,\overline L_h.
\tag{913.42}
$$
In (913.41), extend $\lambda_h$ by zero on the other $\delta$ characters of the full inertia eigenspace. The equation then includes the inert primes, at which its right-hand side is zero. Equation (913.42) has the same interpretation inside the full marked differential space. Equations (913.41–42) refer to the same original $h$ and its full inertia extension. They do not merge $h$ with any half-period shift.

On a $Q$ expansion Cartier is
$$
\mathcal C\left(\sum a_mQ^m\,dQ/Q\right)
=\sum a_{pm}^{1/p}Q^m\,dQ/Q.
\tag{913.43}
$$
Thus the Cartier functional has the usual $U_p$ interpretation, with coefficient Frobenius and the transported tame marking retained. In particular Cartier exchanges the two $\delta$ characters in (913.11); one must not silently turn it into a linear endomorphism of $W_h^+$ alone.

## 8. Exactly what remains to be proved

We have located a nonzero functional supplied by the actual original quotient on a marked, same-label Igusa Cartier cokernel, and identified its Hecke system with the explicit companion $F_{k_-}$. This is stronger than an existence claim in an unrelated ambient theta module.

Nevertheless it does not prove
$$
\lambda_h\bigl(\Phi_{k_-}(\overline V_{k_-}^{\dagger})\bigr)\ne0.
\tag{913.44}
$$
The normalized companion is a nonzero global form and is killed by $U_p$. A nonzero eigenfunctional on the relevant cokernel need not detect that particular eigenvector: congruent eigenforms or a nonsemisimple residual Hecke packet can put it in the kernel. No semisimplicity, one-dimensional packet, or saturation at this original vector has been assumed.

Likewise (913.20) may reduce to zero. The theorem does not improve the already proved bound
$$
v_\varpi(I_h)\ge pr
\tag{913.45}
$$
to equality. The original map still has the additional index $e a_h$.

Finally, neither (913.44), if later proved, nor a global good-model Hodge unit is automatically the first normal coefficient at the contracted original component. That comparison must still retain the original ramified source lattice, the actual $c_1$ parameter, and the specified source column. In the R897/R898 realization the unresolved coefficient remains the one attached to the original $u_{GF}$ and
$$
P_{h-1}(1/s)\,f_i g_j,\qquad
h=6i+7,\quad i+j=N-1,\quad p=6N+5.
\tag{913.46}
$$
No full-space rank or global companion nonvanishing has replaced (913.46).

## Sources and exact scope

- [R908](R908-original-finite-flat-CM-quotient-and-two-gluing-scales.md), §§1–3, 5, 8: the actual quotient, positive Raynaud order, dual closed immersion, and the cotangent bound.
- [R910](R910-original-normalizer-inertia-and-one-sided-CM-gluing.md), §§2–3, and [R911](R911-original-Picard-descent-and-exact-CM-gluing-dichotomy.md), §§2–6: full inertia, the actual normalizer action, Picard duality, and the upper-half additive subgroup.
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), (575.1), (575.13–25), and [R869](R869-original-maximal-cusp-lattice-and-first-theta-layer.md), §§6–7: raw theta normalization, original positive cubic descent, determinant correction, and the fixed oldform phase.
- Edixhoven–Parent, *Semistable reduction of modular curves associated with maximal subgroups in prime level*, [original PDF](https://arxiv.org/pdf/1907.02418), §2.1, §2.2.4(12), Theorems 3.1 and 3.3: the ordinary/exotic Igusa data, index change, and actual normalizer quotient.
- Gross, *A tameness criterion for Galois representations associated to modular forms (mod p)*, Duke Math. J. 61 (1990), [original PDF](https://www.math.purdue.edu/~tongliu/seminar/Mlift/Gross.pdf), Proposition 5.2 and Propositions 5.7–5.9, printed pp. 461–464: the multiplicative Igusa section, differential correspondence, and Hecke/Cartier normalization. No compatibility assertion from his later §§15–16 is used.
- Cais, *On the $U_p$ operator in characteristic $p$*, [author paper](https://arxiv.org/pdf/1305.4188), Propositions 3.1–3.2: the same Igusa differential construction for a general tame moduli problem.
- Oda, *The first de Rham cohomology group and Dieudonné modules*, Ann. Sci. ÉNS 2 (1969), [original PDF](https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf), §4, printed p. 110, and §5, especially Corollary 5.11: restricted Lie, Cartier, and the functorial Picard/Dieudonné comparison. The residue identity in §2 specifies the duality convention used here.

No new numerical computation is used in this proof.

