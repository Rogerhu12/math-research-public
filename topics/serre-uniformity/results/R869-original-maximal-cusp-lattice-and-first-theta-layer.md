# R869 — The maximal original cusp lattice and its first theta layer

Date: 2026-11-16. Status: **proved**. Within the original finite $p$-type, with the actual tame vector fixed, this determines the maximal lattice of forms integral at every cusp. Its first ramified layer is an exact theta derivative with the original CRT factor $1/6$. The corresponding $h=1$ Fourier companion is untwisted of tame level $9$; the actual positive cubic descent remains a separate, already fixed arithmetic transport. No equality with the $q$-pullback Néron lattice or with a first normal coefficient is asserted.

## 1. The original finite type and the exact cusp convention

Let $p\ge41$, $p\equiv5\pmod6$. Let $\mathcal O$ be a finite unramified $p$-adic coefficient ring containing the original character values and tame constants, enlarge its residue field $k$ as necessary, and put
$$
\Lambda=\mathcal O^{\mathbf F_p}/\mathcal O\mathbf1,\qquad
G=\operatorname{PGL}_2(\mathbf F_p),\qquad
\overline\Lambda=\Lambda/p\Lambda.
\tag{869.1}
$$
We use exactly the integral Weyl lattice of R434/R592 for
$\theta_{-1}(a)=[a]^{-(p-1)}$. By R863 there is a nonsplit sequence
$$
0\longrightarrow S\longrightarrow\overline\Lambda
\xrightarrow{\lambda} k\longrightarrow0,
\qquad
S=\operatorname{Sym}^{p-3}V\otimes\det,\qquad
\lambda([c_r])=\sum_r c_r.
\tag{869.2}
$$
The module $S$ is simple and has dimension $p-2$.

Set
$$
\pi=1-\zeta_p,\qquad R=\mathcal O[\zeta_p],\qquad
K_\pi=\operatorname{Frac}(R).
\tag{869.3}
$$
Thus $p/\pi$ has positive $\pi$-adic valuation $p-2$.

The raw newform in the complex Fourier realization is the original **untwisted** form of R575(575.1) and R588(588R.11):
$$
f_\theta=f_{\Psi_\theta},\qquad
\Psi_\theta((a))=a\,\epsilon_3(a)\theta_{-1}(a),\qquad
N(f_\theta)=9p^2,\qquad a_1=1.
\tag{869.4}
$$
The actual positive cubic character $\kappa_4$ arises from the original descent $a=\sqrt[3]4\,u$ in R575. It is not inserted into (869.4). At the chosen $p$-adic place that descent uses the original unit $\sqrt[3]4\in\mathbf Z_p^\times$; retaining it does not change the lattice computation below.

At the fixed reference cusp let
$$
Q=\exp(2\pi i\tau/(6p)),\qquad
F(Q)=f_\theta(Q)-4\zeta^2 f_\theta(Q^4).
\tag{869.5}
$$
This notation writes the two original oldforms as their $Q$ series. For $r\in\mathbf F_p$, the CRT translation is $\tau\mapsto\tau-k_r$, where
$k_r\equiv0\pmod6$ and $k_r\equiv r\pmod p$. R818(818.4) gives the phase on the coefficient of $Q^m$:
$$
e^{-2\pi i m k_r/(6p)}=\zeta_p^{-mr/6}.
\tag{869.6}
$$
Here $6^{-1}$ is taken modulo $p$. In particular the second oldform acquires the phase with its actual exponent $m=4n$, not the phase with $m=n$.

For $v=\sum_r c_r e_r$ write $F_v$ for its image in the fixed original finite type with tame vector (869.5). If $F(Q)=\sum_m A_mQ^m$, then
$$
[Q^m]F_v=A_m\sum_r c_r\zeta_p^{-mr/6}.
\tag{869.7}
$$
The coefficients $A_m$ are integral and $A_1=1$. The relation $\sum_re_r=0$ is respected because the $p$ Euler factor is trivial: $A_m=0$ when $p\mid m$.

All cusp translates are included. The original tame lattice has basis $(H_0,4H_2)$ and matrices
$$
S_6=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
T_6=\zeta\begin{pmatrix}-1&0\\-1&1\end{pmatrix},
\tag{869.8}
$$
as in R592(592.14). These are invertible over $\mathcal O$. The $p$ and tame actions commute. At another cusp, (869.7) is therefore applied to the corresponding $G$-translate of $v$ and the corresponding integral tame translate of $F$. The full pairing-component transports of R592 are retained. Changing a cusp parameter by its actual root of unity also multiplies coefficients only by units.

## 2. The single enlargement and its split reduction

Let $\Lambda_S\subset\Lambda$ be the inverse image of $S$ under reduction modulo $p$. Define
$$
\mathcal L=(R\otimes_{\mathcal O}\Lambda)
+\pi^{-1}(R\otimes_{\mathcal O}\Lambda_S)
\subset K_\pi\otimes_{\mathcal O}\Lambda.
\tag{869.9}
$$
Since $\Lambda_S$ is $G$ stable, so is $\mathcal L$.

Choose an $\mathcal O$ basis $s_1,\ldots,s_{p-2},e$ of $\Lambda$ such that the $\bar s_i$ are a basis of $S$ and $\lambda(\bar e)=1$. Then
$$
\Lambda_S=\bigoplus_i\mathcal O s_i\oplus p\mathcal O e,\qquad
\mathcal L=\bigoplus_i R\,\pi^{-1}s_i\oplus R e.
\tag{869.10}
$$
The second equality uses $p/\pi\in R$. In the first basis, every original unramified integral group matrix has block shape
$$
\rho(g)=\begin{pmatrix}A_g&b_g\\p c_g&d_g\end{pmatrix},
\qquad A_g\bmod p=\rho_S(g),\qquad d_g\bmod p=1.
\tag{869.11}
$$
In the basis of $\mathcal L$ in (869.10), the same matrix is
$$
\begin{pmatrix}
A_g&\pi b_g\\
(p/\pi)c_g&d_g
\end{pmatrix}.
\tag{869.12}
$$
Both off-diagonal blocks vanish modulo $\pi$. Consequently
$$
\boxed{\mathcal L/\pi\mathcal L\simeq S\oplus k
\quad\text{as }k[G]\text{ modules}.}
\tag{869.13}
$$
This splitting uses the original lower block divisible by $p$, not merely by $\pi$. A generic ramified integral extension would not justify the same conclusion.

## 3. Exact first ramified layer at every cusp

For $s\in\Lambda_S$ choose integral coefficients $s=\sum_r c_r e_r$. Their sum belongs to $p\mathcal O$, since $\lambda(\bar s)=0$. Expand (869.6) to first order:
$$
\zeta_p^{-mr/6}=1+\frac{mr}{6}\pi+O(\pi^2).
\tag{869.14}
$$
Dividing (869.7) by $\pi$ is therefore integral. The constant phase contributes $(\sum c_r)/\pi$, which vanishes modulo $\pi$ because $v_\pi(p/\pi)=p-2\ge1$. Define the well-defined residual functional
$$
\mu_1(\bar s)=\sum_r\bar c_r r.
\tag{869.15}
$$
Changing a representative adds a constant vector, whose first moment is zero. We obtain the exact reduction
$$
\boxed{
\overline{F_{s/\pi}}(Q)
=\frac{\mu_1(\bar s)}6\,\Theta_Q\overline F(Q),
\qquad \Theta_Q=Q\frac d{dQ}.}
\tag{869.16}
$$
For the $G$-translate at any original $p$ cusp the functional is exactly
$\mu_1(\overline{\rho(g)s})$. For an additional tame translate, replace $F$ in (869.16) by that actual integral tame vector from (869.8). Thus (869.16) proves integrality at **all** cusps for every element of (869.9).

The other summand of (869.13) has the reduction
$$
\overline{F_e}(Q)=\overline F(Q)
\tag{869.17}
$$
when $\lambda(\bar e)=1$. The $p$-group translates have the same reduction, because $\lambda$ is $G$ invariant. Its first coefficient is one.

There is no suppressed $6p$ in these equations: they concern the raw weight-two Hodge sections of R592. If one converts such a function to a differential using the displayed $Q$, then
$2\pi i\,d\tau=(6p)\,dQ/Q$, exactly as recorded in R818. That different normalization is not used to alter (869.16).

## 4. Maximality in the actual finite $p$-type

Let $\mathcal L_{\rm cusp}$ be the set of vectors in
$K_\pi\otimes\Lambda$ whose raw original Hodge sections are integral at every cusp, with all the transports just specified. We have proved
$\mathcal L\subseteq\mathcal L_{\rm cusp}$.

Consider the reduction map from $\mathcal L/\pi\mathcal L$ to the tuple of all cusp expansions. Its kernel is a $G$ submodule. The trivial summand in (869.13) maps nontrivially by (869.17). The $S$ summand maps nontrivially by (869.16): for example $s=e_1-e_0$ has
$$
\lambda(\bar s)=0,\qquad \mu_1(\bar s)=1,
\tag{869.18}
$$
and $\Theta_Q\bar F$ has first coefficient one. Since $S$ is simple, its map into the complete cusp tuple is injective. Since $S$ is not the trivial representation, (869.13) then shows that the entire reduction map is injective. Equivalently, no primitive vector of $\mathcal L$ can have every cusp expansion divisible by $\pi$.

Now suppose that $v\in\mathcal L_{\rm cusp}\setminus\mathcal L$. Choose the least positive integer $r$ such that $\pi^r v\in\mathcal L$. This is a primitive vector of $\mathcal L$. Yet every cusp expansion of it is divisible by $\pi^r$, contradicting the injectivity just proved. Therefore
$$
\boxed{\mathcal L_{\rm cusp}=\mathcal L.}
\tag{869.19}
$$
By the all-cusp integral Hodge-section principle already used in R592 §3, this is also the maximal lattice obtained by intersecting this particular finite $p$-type with the integral raw Hodge sections on the original full-level model. It does not say that this type is the whole space of global Hodge sections, or that its lattice is the pullback of a Néron cotangent lattice under $q$.

The same argument works for the full explicitly integral tame lattice by taking its actual translates and the resulting cusp tuple. Statement (869.19) is made for the fixed actual vector (869.5), so no unnecessary choice of a larger tame lattice is needed for the assertion.

## 5. The original Cartan line does not enlarge

For the original torus $T_\zeta$, R863 gives $S^{T_\zeta}=0$. Explicitly, after diagonalizing that torus, the characters on
$\operatorname{Sym}^{p-3}V\otimes\det$ are $q^2,\ldots,q^{p-1}$, with $q$ of order $p+1$, so none is trivial.

Let $v_T=(p+1)^{-1}\operatorname{Tr}_{T_\zeta}e_0$ be the same original average as in R592/R727. R434 proves
$$
(R\otimes\Lambda)^{T_\zeta}=R v_T,\qquad \lambda(\bar v_T)=1.
\tag{869.20}
$$
Averaging an element of $\Lambda_S$ lies in $p\mathcal O v_T$: the average is on this rank-one line and its reduction has $\lambda=0$. Therefore its contribution after division by $\pi$ is still in $R v_T$. Averaging (869.9), whose averaging denominator is a unit, gives
$$
\boxed{\mathcal L^{T_\zeta}=R v_T.}
\tag{869.21}
$$
This is compatible with its actual first cusp coefficient, which is a unit by (869.7). The one-step enlargement is in the other finite-type directions. It is not an extra division of the original Cartan average by $p$ or by $\pi$.

## 6. The exact original $h=1$ companion for the theta layer

We now identify $\Theta_q\bar f_\theta$ in the **base variable of (869.4)**. Let
$$
f_4=f_{\Xi_4},\qquad
\Xi_4((a))=a^3\epsilon_3(a).
\tag{869.22}
$$
This is the untwisted weight-four form of tame level $9$, with
$f_4(\tau)=\eta(3\tau)^8$ as in R390 §6.

One may also realize the same residual $f_\theta$ by a holomorphic theta series of weight $2p$:
$$
G_{2p}=f_{\Xi_{2p}},\qquad
\Xi_{2p}((a))=\bar a^{\,2p-1}\epsilon_3(a).
\tag{869.23}
$$
The infinity type is $(0,2p-1)$; the corresponding holomorphic theta series is obtained using the conjugate complex CM type. It is not an antiholomorphic modular form. Its finite conductor is $(\sqrt{-3})$, hence its level is $9$. Indeed the sign character $\epsilon_3$ is nontrivial there, and the displayed infinity type is compatible with the units: $2p-1$ is odd and divisible by three. The same unit check applies to (869.22).

At the chosen inert place, $\bar a=a^p$ in $\mathbf F_{p^2}$. For $(a,p)=1$,
$$
\Psi_\theta((a))\equiv a^{2-p}\epsilon_3(a),\qquad
\bar a^{\,2p-1}\equiv a^{2-p},\qquad
\operatorname N(a)\,a^{2-p}\equiv a^3.
\tag{869.24}
$$
The middle exponents differ by $2(p^2-1)$. Comparing the ideal sums term by term gives
$$
\boxed{\bar f_\theta=\overline G_{2p},\qquad
\Theta_q\bar f_\theta=\bar f_4.}
\tag{869.25}
$$
These are complete Fourier equalities. If $p$ divides the norm, the corresponding original $f_\theta$ term is omitted; the terms of $G_{2p}$ and $f_4$ have factors $p^{2p-1}$ and $p^3$, respectively, and are zero modulo $p$. The prime at three is omitted in all three series. Thus no $p$-multiple Fourier terms have been silently retained.

For comparison as tame modular forms, let $A$ be the Hasse invariant, with $q$ expansion one, and let $\partial_k$ be the same Serre derivative
$q\,d/dq-(k/12)E_2$ in weight $k$. Since $2p=0$ in the residue field, (869.25) and the tame $q$-expansion principle give
$$
\partial_{2p}\overline G_{2p}=A^2\bar f_4,
\qquad
\Theta_{\rm Katz}\overline G_{2p}=A^3\bar f_4.
\tag{869.26}
$$
The two sides have weights $2p+2$ and $3p+1$, respectively. The second theta operator is the modular operator with the indicated Hasse factor; it is not a declaration that different weights have been identified as ordinary sections.

Returning to the actual two-oldform vector (869.5), the exact source derivative is
$$
\boxed{\Theta_Q\bar F
=\bar f_4(Q)-16\zeta^2\bar f_4(Q^4).}
\tag{869.27}
$$
Combining this with (869.16) gives the actual first ramified layer, including the oldform factor four and the CRT factor $1/6$:
$$
\boxed{
\overline{F_{s/\pi}}(Q)
=\frac{\mu_1(\bar s)}6
\left(\bar f_4(Q)-16\zeta^2\bar f_4(Q^4)\right).}
\tag{869.28}
$$
At other cusps the same formula uses the already specified original $G$ and tame transports. The positive cubic twist is still the descent in (869.4), not a replacement of the two raw theta series by a different Hecke family.

For the precise level-six comparison, write $q_*=\exp(2\pi i\tau'/6)$,
$$
V_4^\dagger(\tau')
=f_4(\tau'/6)-16\zeta^2f_4(2\tau'/3).
$$
The Jacobi identities used in R390 give
$$
V_4^\dagger=\eta(\tau')^4(B-\zeta^2 A_2),\qquad
A_2=\vartheta_2(\tau')^4,\quad B=\vartheta_4(\tau')^4.
\tag{869.29}
$$
The subscript on $A_2$ distinguishes it from the Hasse invariant in (869.26). At the conjugate full-six CM marking $A_2=\zeta B$, one has the actual unit formula
$$
\frac{V_4^\dagger}{E_4}
=-\frac{\zeta^2\eta^4}{A_2-\zeta^2B}.
\tag{869.30}
$$
This is the conjugate of R390(390.34). In particular it is a unit at that marking, so the tame form has a simple zero there. This statement keeps the marking: replacing $\zeta^2$ in (869.27) by $\zeta$ while leaving the CM point fixed would change it. The equality $Q=q_*$ means $\tau'=\tau/p$ in the split-cusp expression; it does not identify this tame point with a full-level Drinfeld normal parameter without the original Frobenius and integral comparison.

## 7. The remaining source-to-normal step

The lattice (869.19) and the theta layer (869.28) are statements about actual raw Hodge sections on the full-level model, with all cusp tests and actual finite matrices. They give a concrete source lattice, stronger than a guessed integral span or a single-cusp check.

Its reduction is split by (869.13), whereas R867 realizes the original $\overline\Lambda$ as a nonsplit de Rham extension on a fine Drinfeld component. These are different integral realizations, related by the explicit $\pi^{-1}$ change in (869.9). A comparison must retain that change and the global specialization coefficient; it cannot identify the two reductions by an unspecified unit.

In particular (869.28) is not yet the reduction of the original first-normal coefficient. The exact companion, the tame unit in (869.30), and R867's Cartier unit do not by themselves calculate the map $q$ through the bad model. R859/R861 fix the target Néron parameters. What remains is to transport this source lattice and its marked theta layer to those parameters, keeping the original coarse $c_1$ basepoint and the actual specialization factor. No new claim about the still-open primitive same-$h$ product or the original height follows solely from this lattice theorem.

### Original inputs

- [R434](R434-primitive-cartan-trace-and-scalar-invariant-cm-logarithm.md), §§2–4, and [R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md), §§2–3: the exact integral Weyl matrices, all-cusp realization and integral Hodge-section principle.
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), (575.1–2), §§2–5: the raw untwisted theta newform, the original two-oldform direction, and the positive arithmetic descent.
- [R818](R818-original-primitive-cusp-coefficients-and-unramified-Hom-existence.md), (818.3–6): the full-$6p$ cusp, the actual $6^{-1}$ CRT phase and its arithmetic scale.
- [R863](R863-original-cuspidal-extension-and-full-first-ramified-phase.md), §§2–4: the simple radical, original nonsplit residual extension and torus characters.
- [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §§5–6: the already established CM theta conventions, $\eta(3\tau)^8$, and the explicit marked weight-four unit. Only those fixed tame calculations are used; no withdrawn rank-zero appearance is restored.
- [R867](R867-original-Drinfeld-de-Rham-extension-and-Cartan-Cartier-image.md): the separate fine-component de Rham lattice, whose actual source comparison remains as stated above.

All the new lattice, phase, and coefficient arguments are paper proofs. No local mathematical computation or new finite-prime scan was used.
