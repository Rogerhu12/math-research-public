# R874 — Original cyclic-p quotient scales and the Kodaira–Spencer leading term

Date: 2026-11-16. Status: **proved**. This calculates an actual cyclic-$p$ quotient on the original fine CM branch, in the specified elliptic frames. It transports the marked tame cubic of R871, including the integral Kodaira–Spencer factor. The resulting leading functions and differentials cancel in the unweighted orbit of cyclic subgroups. That orbit is a one-flag permutation representation; it is not the original cuspidal $T$-invariant vector. No original first-normal unit or same-label three-factor nonvanishing is asserted.

## 1. Actual branch, coordinates and quotient frames

Let $p\ge41$, $p\equiv5\pmod6$. Work on the original fine branch of R378 and R592, after the finite coefficient extension needed for its full marking. Put
$$
 e=p^2-1,\qquad s=p(p-1),\qquad
 \varpi^e=p,\qquad t=\varpi^s\tau,\qquad
 \mathscr O=R[[\tau]].
 \tag{874.1}
$$
The original elliptic family, differential and formal parameter are
$$
 E_t:y^2=x^3+tx-1,\qquad
 \omega=\frac{dx}{2y},\qquad u=-\frac{x}{y}.
 \tag{874.2}
$$
The differential has leading term $du$. Throughout, $v_\varpi(\varpi)=1$; divisibility of a series means divisibility of all its coefficients.

Let $P,Q$ be the original full-$p$ basis. By R592(592.18–22), on the Drinfeld component,
$$
 \overline{\frac{u(aP+bQ)}{\varpi}}
   =a\alpha+b\beta,\qquad
 \alpha^p\beta-\alpha\beta^p=c\ne0,
 \quad (a,b)\in\mathbf F_p^2.
 \tag{874.3}
$$
At either of the fine CM completions every nonzero $\mathbf F_p$-linear combination of $\alpha,\beta$ is a unit. In fact if $a\alpha+b\beta=0$, with $(a,b)\ne(0,0)$, their Moore determinant in (874.3) vanishes. Write
$$
 \ell_L=a\alpha+b\beta
 \quad\text{for }L=[a:b]\in\mathbf P^1(\mathbf F_p).
 \tag{874.4}
$$
Only powers of $\ell_L$ divisible by $p-1$ will be used, so these expressions are independent of the chosen representative of $L$.

Let $C_L$ be the finite flat cyclic subgroup with generic points $i(aP+bQ)$, and let
$$
 \phi_L:E_t\longrightarrow E'_L=E_t/C_L,\qquad
 \widehat\phi_L:E'_L\longrightarrow E_t
 \tag{874.5}
$$
be the actual quotient and its dual. Its special-fiber kernel is the connected subgroup $\ker F$, so its reduction is relative Frobenius. Identify the special-fiber quotient with $E_0^{(p)}=E_0$ by this Frobenius identification, and transport the actual prime-to-$p$ level-six marking by $\phi_L$.

Choose the quotient short equation and differential
$$
 E'_L:y_L^2=x_L^3+t'_Lx_L-1,\qquad
 \omega'_L=\frac{dx_L}{2y_L},\qquad u'_L=-\frac{x_L}{y_L},
 \tag{874.6}
$$
with this fixed reduction. This is possible on the completion: $2,3$ are units, the constant coefficient is a unit reducing to $-1$, and its sixth-root normalization has the unique root reducing to one. All subsequent leading scalars refer to (874.2) and (874.6). An arbitrary independently rescaled quotient differential would change them.

Since $p\equiv2\pmod3$, the cube map on $\mathbf F_p$ is bijective, and $\#E_0(\mathbf F_p)=p+1$. Thus its Frobenius $F$ has $F^2=[-p]$, and its Verschiebung is $-F$. Since $[-1]u=-u$, the two formal isogenies have reductions
$$
 \overline{\phi_L(u)}=u^p,\qquad
 \overline{\widehat\phi_L(u'_L)}=-(u'_L)^p.
 \tag{874.7}
$$
These signs use the fixed Frobenius quotient frame; they are not chosen separately for each line.

## 2. The two differential factors and the complete degree-p comparison

Define $a_L,b_L\in\mathscr O$ by
$$
 \phi_L^*\omega'_L=a_L\omega,\qquad
 \widehat\phi_L^*\omega=b_L\omega'_L.
 \quad\text{Then}\quad a_Lb_L=p.
 \tag{874.8}
$$
Weierstrass preparation for the formal quotient gives
$$
 \phi_L(u)=U_L(u)\prod_{i\in\mathbf F_p}
              \bigl(u-u(i(aP+bQ))\bigr),
 \qquad \overline{U_L(u)}=1.
 \tag{874.9}
$$
The product of the nonzero residues $i\ell_L$ is $-\ell_L^{p-1}$. Taking the coefficient of $u$ and then using (874.8) proves
$$
 \boxed{\quad
 \overline{\frac{a_L}{\varpi^{p-1}}}
       =-\ell_L^{p-1},\qquad
 \overline{\frac{b_L}{\varpi^{p(p-1)}}}
       =-\ell_L^{1-p}.\quad}
 \tag{874.10}
$$
In particular both quotients are units, and their product is one.

For clarity we give the coefficient bounds needed below, rather than discard intermediate terms in the isogeny compositions. Write
$\phi_L(u)=\sum_{i\ge1}A_i u^i$. For $1\le i\le p$,
$$
 v_\varpi(A_i)\ge p-i,\qquad A_p\equiv1\pmod\varpi.
 \tag{874.11}
$$
Moreover
$$
 v_\varpi(A_i)\ge p-i+1\quad(2\le i\le p-1),
 \tag{874.12}
$$
because the scaled kernel polynomial reduces to
$Z^p-\ell_L^{p-1}Z$. Multiplication by the integral unit $U_L(u)$ does not destroy the extra divisibility: a positive-degree coefficient of $U_L$ is accompanied by at least one extra power of $\varpi$ after $u=\varpi Z$.

Choose a complementary torsion point with leading coordinate $m$, independent of $\ell_L$. Its image in the quotient satisfies
$$
 \overline{\frac{u'_L(\phi_L(Q_L))}{\varpi^p}}
       =m^p-\ell_L^{p-1}m\ne0.
 \tag{874.13}
$$
Indeed $m/\ell_L\notin\mathbf F_p$. These images generate the dual kernel. Applying the same preparation to
$\widehat\phi_L(u')=\sum_{j\ge1}B_j(u')^j$ gives
$$
 \begin{aligned}
 v_\varpi(B_j)&\ge p(p-j) &&(1\le j\le p),\\
 B_p&\equiv-1\pmod\varpi,\\
 v_\varpi(B_j)&\ge p(p-j)+1 &&(2\le j\le p-1).
 \end{aligned}
 \tag{874.14}
$$
The last extra power again follows because the scaled roots form a one-dimensional additive $\mathbf F_p$-space. Only these finite ranges can contribute to degree $p$ in a composition; no coefficient of index greater than $p$ is being silently removed.

Set $p=6r+5$. In the original parameter $u$ the coefficient of $u^p$ in $[p]_{E_t}(u)$ is
$$
 c_p(t)=tV(t)+pW(t),\qquad
 V(0)\bmod p=\kappa,\qquad
 \kappa=(-1)^r\frac{(3r+2)!}{(2r+1)!\,r!}\in k^\times.
 \tag{874.15}
$$
This is the linear coefficient of the Hasse polynomial, namely the coefficient of $t x^{p-1}$ in
$(x^3+tx-1)^{(p-1)/2}$. All displayed factorials are below $p$. With the original R770 Cartier constant,
$$
 B=(-1)^{r+1}\binom{3r+2}{2r+1},
 \qquad \kappa=-(r+1)B=-\frac B6\quad\text{in }k.
 \tag{874.16}
$$

First compose $\phi_L\circ\widehat\phi_L=[p]_{E'_L}$. Its outer linear term contributes $a_L B_p$. For an outer index $2\le i\le p$, a product with inner indices summing to $p$ has valuation at least
$$
 (p-i)+p\sum_{\nu=1}^i(p-j_\nu)
 =p-i+p^2(i-1)>p-1.
 \tag{874.17}
$$
Since $t'_L$ reduces to zero, (874.15) holds on the quotient with $t$ replaced by $t'_L$. The series $t'V(t')$ is a unit times $t'$, and $v_\varpi(p)=e>p-1$. Consequently the composition first proves $v_\varpi(t'_L)=p-1$, and then gives
$$
 \kappa\,\overline{\frac{t'_L}{\varpi^{p-1}}}
       =\ell_L^{p-1}.
 \tag{874.18}
$$
Thus the exact quotient parameter is
$$
 \boxed{\quad
 \overline{\frac{t'_L}{\varpi^{p-1}}}
   =\kappa^{-1}\ell_L^{p-1}
   =-\frac6B\ell_L^{p-1}.
 \quad}
 \tag{874.19}
$$
Its scale is $\varpi^{p-1}$; the source parameter has scale
$\varpi^{p(p-1)}$. They must not be interchanged.

For the opposite composition $\widehat\phi_L\circ\phi_L=[p]_{E_t}$, both endpoint terms have valuation $s$: they are $b_L A_p$ and $B_p a_L^p$. Every intermediate outer index $2\le i\le p-1$ has the lower bound $s$, improved to $s+1$ by (874.14). Thus there is no uncomputed contribution at that order. Using (874.10) gives
$$
 \boxed{\quad
 \kappa\bar\tau
 =\ell_L^{p^2-p}-\ell_L^{1-p}
 =\mathcal D,\qquad
 \mathcal D=
 \frac{\alpha^{p^2}\beta-\alpha\beta^{p^2}}
      {\alpha^p\beta-\alpha\beta^p}.
 \quad}
 \tag{874.20}
$$
One can also check the last equality directly from the full torsion polynomial. Its scaled reduction is
$Z^{p^2}-\mathcal D Z^p+c^{p-1}Z$. In the present coordinate the leading coefficient of $[p]$ is $-1$, by (874.7), whereas the normalized linear coefficient is $p\varpi/\varpi^{p^2}=1$. Hence
$$
 c^{p-1}=-1,\qquad
 \prod_{a,b\in\mathbf F_p}(Z-a\alpha-b\beta)
       =Z^{p^2}-\mathcal D Z^p-Z.
 \tag{874.21}
$$
This fixes the relation satisfied by the actual $c$; it does not replace it by a selected root. Differentiating (874.20) in characteristic $p$ yields the useful exact identity
$$
 d(\ell_L^{p-1})=\ell_L^{2(p-1)}\,d\mathcal D.
 \tag{874.22}
$$
By the original R378 parameter calculation, restated in R592(592.20–22), $d\mathcal D$ is a unit differential at both fine CM lifts.

## 3. The actual Kodaira–Spencer factor

Use the de Rham basis $(\omega,x\omega)$ of R592(592.24), with alternating pairing normalized by
$\langle\omega,x\omega\rangle=1$. The Kodaira–Spencer differential in this frame is
$$
 \operatorname{KS}_{E_t}(\omega^2)
 :=\langle\omega,\nabla\omega\rangle
 =b(t)\,dt,\qquad
 b(t)=-\frac9{2(4t^3+27)},\quad b(0)=-\frac16.
 \tag{874.23}
$$
The same formula applies to the quotient frame (874.6). This sign agrees with the fixed algebraic convention
$E_4=c_4=-48t$, $E_6=-c_6=-864$: the Serre derivative has $\partial t=-6$ at $t=0$.

On the characteristic-zero generic fiber, isogeny pullback is horizontal and multiplies the alternating de Rham pairing by its degree $p$. Therefore
$$
 \begin{aligned}
 p\,\operatorname{KS}_{E'_L}((\omega'_L)^2)
 &=\langle\phi_L^*\omega'_L,
                    \nabla(\phi_L^*\omega'_L)\rangle\\
 &=\langle a_L\omega,d a_L\otimes\omega
                         +a_L\nabla\omega\rangle\\
 &=a_L^2\,\operatorname{KS}_{E_t}(\omega^2).
 \end{aligned}
 \tag{874.24}
$$
The $d a_L$ term vanishes because the pairing of $\omega$ with itself is zero. Hence the exact identity is
$$
 \boxed{\quad
 a_L^2 b(t)\,dt=p\,b(t'_L)\,dt'_L,\qquad
 \frac{dt'_L}{dt}=\frac{a_L^2}{p}\frac{b(t)}{b(t'_L)}.
 \quad}
 \tag{874.25}
$$
In particular
$$
 v_\varpi(a_L^2/p)=-(p-1)^2,\qquad
 v_\varpi(dt'_L/d\tau)=p-1.
 \tag{874.26}
$$
Here the second equality is an equality of coefficient contents in the completed local ring: the leading coefficient is a unit by (874.10), and $b(t)/b(t'_L)$ is a unit. The expression $a_L^2/p$ is not itself integral. Its denominator is compensated only after multiplying by $dt=\varpi^s d\tau$.

Reducing (874.25) after division by $\varpi^{p-1}$ gives
$$
 d\left(\overline{t'_L/\varpi^{p-1}}\right)
       =\ell_L^{2(p-1)}d\bar\tau.
 \tag{874.27}
$$
This agrees with (874.19), (874.20), and (874.22), including the constants. It provides a separate differential check on the quotient/source scales without deleting $p$ from Kodaira–Spencer.

## 4. Pullback of the marked tame cubic

Let $P^\dagger$ be the actual conjugate full-six point of R871, obtained by the Frobenius transport of the source marking just specified. All the quotients $E'_L$ reduce to this same marked point: on the special fiber every $\phi_L$ is the same relative Frobenius. The tame functions used below are evaluated in their transported markings, not merely on a curve with the same $j$ invariant.

Retain the exact rational companion $R=W/\mathcal A$ of R871, and write
$$
 U_\dagger=\left(V_4^\dagger/E_4\right)(P^\dagger)\in k^\times.
 \tag{874.28}
$$
By R871(871.24,32), in the quotient frame (874.6),
$$
 R(t')-R(0)=-\frac{U_\dagger}{324}(t')^3+O((t')^4).
 \tag{874.29}
$$
Indeed $E_4=-48t'$ and $E_6=-864$, and
$(-48)^3/(48\cdot864^2)=-1/324$. The unit $U_\dagger$ carries the actual six-level phase. Nothing in this argument sets it to one.

To make the substitution into the mixed-characteristic quotient precise, first work on the tame curve over its original unramified coefficient ring $R_0=W(k)$, or a sufficiently large finite unramified extension of $\mathbf Z_p$ containing the transported six-level marking. The completed local coordinate $t'$ and the marked CM section are defined over this ring. In this section an admissible lift means a series $\widetilde R\in R_0[[t']]$ whose reduction modulo $p$ is the regular function $R$. Only after choosing such a lift do we base change to the ramified ring $R$ in (874.1). Such an unramified integral lift can be made from the original forms: lift the two oldforms defining $W$ to characteristic zero and average over the actual $H_6^\dagger$. Its order is prime to $p$, and R871(871.20) shows that the reduction of the average is $W$. The averaged form vanishes at the marked CM section by its order-three stabilizer and weight $p-1\equiv1\pmod3$. The usual integral Eisenstein lift of $\mathcal A$, of weight $p-1$, also vanishes there and has a simple zero: its reduction has the original simple Hasse zero. Dividing these local forms therefore gives an integral regular quotient reducing to $R$.

This construction only asserts a local lift. It does not assert that an unaveraged quotient of arbitrary characteristic-zero lifts is regular, or that its global constant is the original $c_0$-rigidification. Subtract $\widetilde R(P^\dagger)$, the value of this chosen lift at its marked CM section.

Substitution of (874.19) into (874.29) gives
$$
 \boxed{\quad
 \overline{\varpi^{-3(p-1)}
  \bigl(\widetilde R(E'_L)-\widetilde R(P^\dagger)\bigr)}
 =\rho\,\ell_L^{3(p-1)},\qquad
 \rho=-\frac{U_\dagger}{324\kappa^3}
      =\frac{2U_\dagger}{3B^3}\in k^\times.
 \quad}
 \tag{874.30}
$$
There is no lower term of comparable valuation hidden in the lift. Its nonconstant coefficients of degrees one and two are divisible by $p$, so their valuations after substitution are at least $e+(p-1)>3(p-1)$. Terms of degree at least four have valuation at least $4(p-1)$. Changing between admissible unramified lifts in $R_0[[t']]$ adds a series divisible by $p$; after subtracting each lift's own marked CM constant the same inequality applies. Thus (874.30) is independent within this specified class of lifts. No independence is asserted for arbitrary lifts over the ramified ring $R$: two such lifts of a $k$-function may differ only by $\varpi$, which would not give the preceding bounds.

Differentiating in the actual fine parameter and using (874.22) gives
$$
 \boxed{\quad
 \overline{\varpi^{-3(p-1)}d\widetilde R(E'_L)}
   =3\rho\,\ell_L^{4(p-1)}\,d\mathcal D.
 \quad}
 \tag{874.31}
$$
For each individual $L$ its coefficient is a unit at the fine CM point. Equation (874.25), with its factor $a_L^2/p$, is the same differential transport expressed through the quotient elliptic frame. It is not permissible to replace it by $a_L^2$ before taking this leading term.

## 5. Exact cancellation of the one-flag orbit

For every integer $1\le m\le p$ the following polynomial identity holds in characteristic $p$:
$$
 \boxed{\quad
 \sum_{[a:b]\in\mathbf P^1(\mathbf F_p)}
       (aX+bY)^{m(p-1)}=0.
 \quad}
 \tag{874.32}
$$
The summands are independent of representatives. Choose $(1,u)$, $u\in\mathbf F_p$, and $(0,1)$. Expanding the former sum, only exponents divisible by $p-1$ can remain. The coefficient at exponent zero has the factor $p=0$, and the terminal coefficient $-Y^{m(p-1)}$ cancels the final line $(0,1)$. For the interior exponent $j(p-1)$, $1\le j<m$, Lucas's formula gives
$$
 \binom{m(p-1)}{j(p-1)}
 \equiv
 \binom{m-1}{j-1}\binom{p-m}{p-j}=0.
 \tag{874.33}
$$
The last lower index exceeds the upper one because $j<m$. This includes $m=p$; it does not use negative factorials.

Applying (874.32) with $m=3$ and $m=4$ proves respectively
$$
 \sum_L\rho\ell_L^{3(p-1)}=0,\qquad
 \sum_L3\rho\ell_L^{4(p-1)}d\mathcal D=0.
 \tag{874.34}
$$
Consequently the leading terms in (874.30) and (874.31) cancel in the unweighted sum over all cyclic subgroups. The common quotient marking and common $\rho$ are essential here. The denominator $p+1$ of an average is a unit and does not change the cancellation.

A nonsplit Cartan acts freely and transitively on $\mathbf P^1(\mathbf F_p)$. Its orbit of one cyclic subgroup is therefore exactly this sum. This statement is about that one-flag orbit, with the specified quotient frames; it makes no identification with the original cuspidal Cartan trace.

## 6. Why this does not calculate the original cuspidal normal term

The one-cyclic-subgroup construction belongs to the permutation representation on $\mathbf P^1(\mathbf F_p)$:
$$
 k[\mathbf P^1(\mathbf F_p)]=k\oplus\operatorname{St},
 \qquad \dim\operatorname{St}=p.
 \tag{874.35}
$$
The constant summand splits since $p+1$ is a unit, and the augmentation module is the defining-characteristic Steinberg representation. In contrast, the actual original finite type in R592/R863 has dimension $p-1$ and the nonsplit residual sequence
$$
 0\longrightarrow
 S=\operatorname{Sym}^{p-3}V\otimes\det
 \longrightarrow\overline\Lambda
 \longrightarrow k\longrightarrow0.
 \tag{874.36}
$$
The simple module $S$, of dimension $p-2$, is not a composition factor of (874.35). In particular no equivariant construction using only the functions of one cyclic subgroup in (874.35) can realize the full original extension.

This distinction is visible already in the original characteristic-zero vector. The reference $e_0$ of R592 is fixed by the split diagonal torus and by the Weyl element, but it is not Borel fixed: a nontrivial unipotent translation takes it to $e_r\ne e_0$. Thus its actual nonsplit average
$(p+1)^{-1}\operatorname{Tr}_{T_\zeta}e_0$
must not be replaced by an unweighted average of a Borel-fixed one-flag vector. Two distinct cyclic subgroups, or an equivalent two-flag datum and its original ramified phases, are needed even to represent its symmetry correctly.

R869 supplies the genuine cusp phases
$\zeta_p^{-mr/6}$, the source lattice
$\mathcal L=R_\pi\Lambda+\pi^{-1}R_\pi\Lambda_S$,
and its first theta layer. R867 supplies the separate nonsplit Drinfeld de Rham realization. Those are the actual inputs that a source comparison must still transport; the leading cancellation (874.34) neither deletes their phases nor computes the map from them to the target Néron parameters of R859/R861.

In particular R706's allowed-prime $h=1$ minimum-valuation counterexample remains in force, as do R750's complete common-phase relations. The individual cyclic-quotient units in (874.31) are not claimed to give $v_p(M_{2,1})=-1$, a unit first normal coefficient, a primitive/Legendre same-label nonzero term, or a nonzero height. The new statements are the exact two quotient scales, their Kodaira–Spencer comparison, and the stated leading transport and cancellation, in the original frames.

### Original and primary sources

- [R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md), (592.1–2), (592.18–26): the original scaled full-level branch, actual formal parameter, Hasse coefficient and Gauss–Manin matrix; it restates the required local geometry of R378 §§2–3.
- [R871](R871-original-tame-Abel-companion-and-marked-cubic-unit.md), §§4–6: the actual conjugate six-level marking, regular tame companion, cubic coefficient, and retained characteristic-$p$ homogeneous terms.
- [R869](R869-original-maximal-cusp-lattice-and-first-theta-layer.md), §§1–3 and 5–7: the full CRT phase, maximal original source lattice, and the distinction between it and the target normal lattice.
- [R863](R863-original-cuspidal-extension-and-full-first-ramified-phase.md) and [R867](R867-original-Drinfeld-de-Rham-extension-and-Cartan-Cartier-image.md): the actual cuspidal extension and its separate de Rham realization.
- Edixhoven–Parent, *Semistable reduction of modular curves associated with maximal subgroups in prime level*, [author PDF](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf), §§2.1–2.2: the full-level subgroup model, relative Frobenius/Verschiebung and the original local model.
- Fred Diamond, *Kodaira–Spencer isomorphisms and degeneracy maps on Iwahori-level Hilbert modular varieties: the saving trace*, [published article](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/kodairaspencer-isomorphisms-and-degeneracy-maps-on-iwahorilevel-hilbert-modular-varieties-the-saving-trace/6F092EA257A685CDBC34D006A47035DF), introduction (1.1) and discussion of (5.21), for the integral isogeny/trace context. Formula (874.25) above is proved directly from horizontal pullback and the degree-$p$ alternating pairing, not inferred from an unproved integral cancellation.

All new assertions here are paper proofs. No local mathematical execution or finite-prime scan was used.
