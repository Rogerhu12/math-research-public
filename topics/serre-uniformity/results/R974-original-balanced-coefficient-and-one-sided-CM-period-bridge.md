# R974 — The original balanced coefficient and a one-sided CM period bridge

Date: 2026-11-20. Authoring agent: literature_frontier. Independently checked by root against the primary sources.

**Status: proved one-sided integral comparison and sufficient unit criterion.** The conclusions below are one-sided integrality of the actual Manin periods and an exact comparison between the adjoint value and a specified two-variable Kronecker coefficient. It uses critical additive periods and integral modular symbols, not a comparison between the Scholl motive and an abstract CM motive. All computations in this note are symbolic. No numerical mathematics has been executed locally.

## 1. Exact statement and the direction of the inequality

Use the two rows of R970. Write
$$
n=w-1=p-r,\qquad r\in\{2,8\},
\qquad n\equiv3\pmod6,\qquad p\ge41.
\tag{974.1}
$$
Let $f=F_w\in S_w(\Gamma_0(9))$ be R970's rational normalized CM form. Put $K=\mathbb Q(\sqrt{-3})$. One may use $E:y^2=x^3+1$ with its invariant differential $\omega_E=dx/(2y)$ and its CM Hecke character $\psi$. Its finite character at two has order three. Since $n\equiv3\pmod6$, $\psi^n$ has the original conductor $\sqrt{-3}$ character and is exactly the character $\Xi_w$ of R913/R970; no new twist of $f$ is made.

Choose an $\mathcal O_K$-generator $\Omega_E$ of the period lattice of $(E,\omega_E)$, and set
$$
P_n=\left(\frac{\Omega_E}{2\pi i}\right)^n.
\tag{974.2}
$$
The real model makes the conjugate lattice equal to the original lattice, so $\overline{\Omega_E}/\Omega_E$ is an $\mathcal O_K$-unit; a real generator is not required. Any change by an $\mathcal O_K$-unit is harmless for the integral assertion. After a finite extension of the coefficient ring at the fixed prime above $p$, the claim is
$$
\boxed{\quad \Omega_f^+/P_n\text{ and }\Omega_f^-/P_n
\text{ are algebraic and }p\text{-integral}.\quad}
\tag{974.3}
$$
Here the periods are precisely the integral Manin periods of Tilouine--Urban §3 used in R970: their Betti vectors generate the intersections of the actual integral parabolic cohomology lattice with the two rational $f$-eigenlines. Equation (974.3) does not say that either quotient is a unit.

Consequently
$$
v_p\left(\frac{P_n^2}{\Omega_f^+\Omega_f^-}\right)\le0.
\tag{974.4}
$$
This direction matters. If a separately proved formula writes R970's adjoint algebraic value as a $p$-unit times
$$
c_n\frac{P_n^2}{\Omega_f^+\Omega_f^-}
\tag{974.5}
$$
with an explicitly normalized $c_n$ that is a $p$-unit, then R970's integrality of the congruence ideal, together with (974.4), forces that adjoint value and the two period quotients to be units. Without a proof that $c_n$ is a unit, no such conclusion follows.

## 2. The precise primary integral input

Guido Kings and Johannes Sprang, *Eisenstein--Kronecker classes, integrality of critical values of Hecke L-functions and p-adic interpolation*, Annals of Mathematics **202** (2025), 1--109, Theorem 4.10 and §4.2. The accepted author version is arXiv:1912.03657v4 (14 September 2024):

- <https://annals.math.princeton.edu/2025/202-1/p01>
- <https://arxiv.org/pdf/1912.03657>

For an imaginary quadratic character $\chi$ with critical infinity type $(\beta,-\alpha)$, $\alpha\ge1$, $\beta\ge0$, and nontrivial conductor $\mathfrak f$, their theorem gives
$$
\frac{(\alpha-1)!(2\pi i)^\beta}
 {\Omega^\alpha(\Omega^\vee)^\beta}
\bigl(\chi(\mathfrak c)N\mathfrak c-1\bigr)
L_{\mathfrak f}(\chi,0)
\in\mathcal O_{\mathfrak p}
\tag{974.6}
$$
whenever the chosen auxiliary ideal $\mathfrak c$ and the conductor have norms prime to $p$. The bases of the invariant differentials of $E$ and $E^\vee$ are integral at $p$. The theorem does not impose ordinarity: that hypothesis first enters the interpolation constructions of §5.

The CM type in (974.6) is chosen to put the negative exponent $-\alpha$ in the holomorphic CM type. For our real $j=0$ elliptic curve, both periods $\Omega$ and $\Omega^\vee$ are $\Omega_E$ times algebraic units away from two and three. Indeed the principal polarization identifies $E^\vee$ with $E$ over $\mathbb Z[1/6]$ and identifies their invariant-differential lattices. Its Rosati action conjugates $\mathcal O_K$. The induced $\mathcal O_K$-dual homology structure differs from an $\mathcal O_K$-basis by the different of $K$, supported at three. Thus the integral period structures of Kings--Sprang Definition 4.5 differ from these chosen periods only by units at every $p>3$.

One should not replace their de Rham pairing involving the complex conjugate Hodge form in Proposition 4.6 by an algebraic scalar without explanation. The principal polarization and the different, as just described, suffice for the unit assertion about the two holomorphic period lattices.

## 3. Removing the regularizer for every critical twist needed here

Let $\nu$ be any finite-order Dirichlet character of conductor prime to $p$, and let $1\le s\le n$. The critical Hecke character is
$$
\chi_s=\psi^n(\nu\circ N_{K/\mathbb Q})N_{K/\mathbb Q}^{-s},
\tag{974.7}
$$
with infinity type $(n-s,-s)$. In particular $\alpha=s$, $\beta=n-s$ in (974.6). Its conductor cannot be trivial: its total infinity degree $n-2s$ is odd, so invariance under the unit $-1$ requires a nontrivial finite character.

Choose an algebraic integer $a\in\mathcal O_K$ congruent to one modulo the conductor of $\chi_s$, and set $\mathfrak c=(a)$. As $p$ is inert, $\mathcal O_K/p=\mathbb F_{p^2}$. The Chinese remainder theorem allows the residue $x=a\bmod p$ to be any element of $\mathbb F_{p^2}^\times$, while keeping $a$ prime to the conductor. Then
$$
\chi_s(\mathfrak c)N\mathfrak c
\equiv x^{n-s+1}\bar x^{1-s}
=x^{e_s}\pmod p,
\qquad
e_s=2p-r+1-(p+1)s.
\tag{974.8}
$$
For $1\le s\le p-r$, the extremal exponents are
$$
e_1=p-r,\qquad
e_{p-r}=-p^2+(r+1)p+1.
\tag{974.9}
$$
Thus $-(p^2-1)<e_s<p^2-1$. An exponent could be zero only if $p+1$ divided $r+1$; this is impossible for $p\ge41$ and $r+1=3$ or $9$. Hence $x\mapsto x^{e_s}$ is nontrivial. We may and do choose $x$ so that $x^{e_s}\ne1$. The regularizer in (974.6) is then a $p$-unit and can be removed.

Using the period lattices of §2 gives the concrete conclusion
$$
\boxed{\quad
\frac{(s-1)!(2\pi i)^{n-s}}
 {\Omega_E^n}
L(f\otimes\nu,s)\in\overline{\mathbb Z}_p,
\qquad1\le s\le n.
\quad}
\tag{974.10}
$$
Here $L(f\otimes\nu,s)$ denotes the coefficient-twisted Dirichlet series. If its imprimitive conductor differs from the primitive Hecke conductor, the difference is multiplication by finitely many Euler polynomials at primes dividing the conductor of $\nu$. These polynomials have coefficients integral at $p$ and are evaluated at $\ell^{-s}$ with $\ell\ne p$, so (974.10) still holds. This does not require division by those polynomials.

The factorial in (974.10) is precisely the Mellin factorial. There is no omitted denominator from a symmetric-power convention. In our range it is also a $p$-unit, but the argument does not need to divide by it.

## 4. From multiplicative twists to the actual additive periods

For a rational endpoint $a/c$ with $c>0$, define by analytic continuation
$$
L(f,a/c,s)=\sum_{m\ge1}a_m(f)e^{2\pi i am/c}m^{-s}.
\tag{974.11}
$$
Only $c\le8$ will be needed below. These additive twists can be expressed as $p$-integral combinations of the multiplicative twists in (974.10), uniformly in the critical integer $s$.

For completeness, partition the sum by $d=(m,c)$ and put $q=c/d$. On $(j,q)=1$, finite Fourier inversion gives
$$
e^{2\pi i aj/q}=\sum_{\nu\bmod q}b_\nu(a)\nu(j),
\quad
b_\nu(a)=\frac1{\varphi(q)}
\sum_{u\in(\mathbb Z/q)^\times}
e^{2\pi i au/q}\nu(u)^{-1}.
\tag{974.12}
$$
Every $b_\nu(a)$ is integral at $p\ge41$, since $q\le8$ and $\varphi(q)\le6$. Thus
$$
L(f,a/c,s)=\sum_{d\mid c}d^{-s}
\sum_{\nu\bmod c/d}b_\nu(a)
\sum_{j\ge1}a_{dj}(f)\nu(j)j^{-s}.
\tag{974.13}
$$
At a good prime $\ell\ne3$ the elementary Hecke recurrence is equivalent to
$$
U_{\ell^v}f=a_{\ell^v}(f)f
-\ell^n a_{\ell^{v-1}}(f)V_\ell f,
\qquad v\ge1.
\tag{974.14}
$$
Applying the coefficient twist and Mellin series shows that the inner series in (974.13) equals
$$
\left(\prod_{\ell^v\parallel d}
\bigl(a_{\ell^v}(f)
-\ell^{n-s}\nu(\ell)a_{\ell^{v-1}}(f)\bigr)\right)
L(f\otimes\nu,s)
\tag{974.15}
$$
when $3\nmid d$. If $3\mid d$, that inner series is zero, since the original primitive CM form has $U_3f=0$. Every factor in (974.15), and also $d^{-s}$, is integral at $p$. The identities first hold in a right half-plane and then at all critical $s$ by analytic continuation. No Euler factor has been inverted.

Mellin integration gives
$$
\int_{a/c}^{i\infty}f(z)(z-a/c)^{s-1}\,dz
=\frac{i^s(s-1)!}{(2\pi)^s}L(f,a/c,s).
\tag{974.16}
$$
Its quotient by $P_n$ is exactly $(-1)^s$ times the expression in (974.10), combined with integral coefficients from (974.13)--(974.15). Indeed $i^{s+n}/i^{n-s}=i^{2s}=(-1)^s$. Therefore it is algebraic and integral at $p$.

Replacing $(z-a/c)^{s-1}$ by $z^{s-1}$ uses binomial coefficients and powers of $a/c$. These coefficients are integral at $p$, because $p\nmid c$. Hence every monomial moment of degree at most $n-1$ at these endpoints is integral after division by $P_n$.

## 5. The actual integral Betti lattice, not a rational period space

The left cosets $\Gamma_0(9)\backslash\mathrm{SL}_2(\mathbb Z)$ are indexed by $\mathbb P^1(\mathbb Z/9)$. We can choose the following twelve representatives, by their primitive bottom rows:
$$
g_d=\begin{pmatrix}0&-1\\1&d\end{pmatrix},
\quad0\le d\le8;
\qquad
h_c=\begin{pmatrix}1&0\\c&1\end{pmatrix},
\quad c=0,3,6.
\tag{974.17}
$$
For a bottom row whose first entry is a unit modulo nine, normalize it to $(1,d)$. Otherwise its second entry is a unit and it normalizes to $(c,1)$ with $c=0,3,6$. Thus these are exactly all the cosets.

The endpoints of the corresponding Manin edges $g\{0,\infty\}$ belong to
$$
\{\infty,0,-1,-1/2,\ldots,-1/8,1/3,1/6\}.
\tag{974.18}
$$
Every required period is therefore covered by §4. The matrices in (974.17) have integral entries and determinant one, so transporting the coefficient lattice $\operatorname{Sym}^{n-1}\mathcal O^2$ introduces no denominator.

Here is the integral cohomology point explicitly. The Farey tessellation yields the usual Manin edge chain complex for the relative homology of the compactified modular curve. Its stabilizer relations come from the elements of orders two and three. Both orders are invertible in $\mathcal O$. A closed $\operatorname{Sym}^{n-1}\mathcal O^2$-valued differential whose edge integrals are in that lattice therefore gives an integral cohomology class: the edge values satisfy the triangle and reversal relations by integration, and the relations commute with extension of scalars. If one uses the self-dual polynomial pairing to identify coefficients with their dual, its only extra denominators divide $(n-1)!$, which is a unit here since $n-1<p$.

The resulting class is integrally parabolic. The four cusps of $\Gamma_0(9)$ are represented by $\infty,0,1/3,2/3$. The primitive obtained by integrating from each cusp has, at the base endpoint, the moments in §4 (with denominators at most three). They are integral. Thus on each cusp stabilizer the cocycle is the coboundary of an **integral** vector. This checks membership in the image of compactly supported cohomology, not merely vanishing of boundary restriction after tensoring with the fraction field.

Consequently the actual class
$$
\frac{\omega_f}{P_n}
=\frac1{P_n}
\left[f(z)(X-zY)^{n-1}\,dz\right]
\tag{974.19}
$$
belongs to the integral parabolic Betti lattice used by Tilouine--Urban. It lies in the $f$-eigenspace since all Hecke correspondences act on the same class and $f$ is an eigenform.

Complex conjugation on this Betti lattice is an integral involution. Since two is a unit, applying $(1\pm c_\infty)/2$ to (974.19) gives integral elements of the two $f$-eigenlines. If $\delta_f^\pm$ are the integral generators in the definition of the Manin periods, then
$$
\frac{\omega_f^\pm}{P_n}
=\frac{\Omega_f^\pm}{P_n}\delta_f^\pm.
\tag{974.20}
$$
The integral generators are primitive in these intersections, so the coefficients in (974.20) are integral. The convention is exactly Tilouine--Urban's displayed definition in §3, printed p. 15: $\omega_f=f(z)(X-zY)^{k-2}dz$ with $k=w=n+1$. Their lattice $V_k$ is the homogeneous polynomial representation of degree $k-2$. If the edge complex is constructed with the dual representation, the integral alternating form on $\mathcal O^2$ identifies it with this representation; in degree $n-1$ the induced dual pairing has denominators dividing $(n-1)!$, a unit. Thus no $2\pi i$ or nonunit scalar is inserted on passage to their convention. This proves (974.3). No assertion about an algebraic correspondence of motives is needed.

## 6. The exact adjoint coefficient, including the Euler factor at three

Write $\psi_+$ for the character of the original $E_+:y^2=x^3+1$. The finite character of $\psi_+^n$ is the original quadratic character at $\sqrt{-3}$, so
$$
\psi_+^{2n}((\alpha))=\alpha^{2n}
\quad\text{for every nonzero principal ideal of }\mathcal O_K.
\tag{974.21}
$$
This is well-defined because $6\mid2n$. It is the conductor-one Hecke character, including its Euler factor at three. Class number one makes (974.21) a specification on every nonzero ideal.

The primitive adjoint representation decomposes as
$$
\operatorname{Ad}(f)=\chi_{-3}\oplus
\operatorname{Ind}_{K}^{\mathbb Q}(\psi_+^{2n}N^{-n}).
\tag{974.22}
$$
At $\mathfrak q=(\sqrt{-3})$, (974.21) gives
$$
\psi_+^{2n}(\mathfrak q)=(-3)^n=-3^n,
\tag{974.23}
$$
since $n$ is odd. The primitive adjoint Euler factor at three, evaluated at one, is consequently
$$
\left(1-(-3)^n3^{-(n+1)}\right)^{-1}
=\left(1+\frac13\right)^{-1}=\frac34.
\tag{974.24}
$$
The local form at three is the original supercuspidal type of R970. Tilouine--Urban's **imprimitive** definition in §3, printed p. 17, omits the local adjoint factor at a supercuspidal prime; its displayed alternatives retain factors only for principal series and special types. Thus, writing $L_{\rm TU}$ for precisely the function in their Theorem 3.1,
$$
L_{\rm TU}(\operatorname{Ad}f,1)
=\frac43 L(\chi_{-3},1)L(\psi_+^{2n},n+1)
=\frac{4\pi}{9\sqrt3}L(\psi_+^{2n},n+1).
\tag{974.25}
$$
Here $L(\chi_{-3},1)=\pi/(3\sqrt3)$ is the Dirichlet value for the primitive quadratic character. In particular omitting the factor $4/3$ would change the exact scalar, though not its valuation at an original prime.

To agree exactly with the coefficient in R973, now use
$$
E_-:y^2=x^3-1,\qquad \omega_-=dx/(2y).
$$
Its Weierstrass uniformization has $g_2=0,g_3=4$. Choose the positive real generator $\Omega_-$ for its period lattice
$$
\Lambda_-=\Omega_-\mathcal O_K,
\qquad A(\Lambda_-)=\frac{\operatorname{area}(\mathbb C/\Lambda_-)}{\pi}
=\frac{\sqrt3\,\Omega_-^2}{2\pi}.
\tag{974.26}
$$
Let $\sigma(z)=\sigma(z;0,4)$ be the Weierstrass sigma function normalized by $\sigma'(0)=1$. The reduced-theta quadratic exponential vanishes on this equianharmonic lattice: its coefficient has weight two and multiplication by a sixth root of unity forces it to vanish. Thus the precise Kronecker theta function of Bannai--Kobayashi is
$$
\Theta(z,w)=\frac{\sigma(z+w)}{\sigma(z)\sigma(w)}.
$$
Define the rational coefficient and the corresponding period
$$
c_n=[z^nw^{n-1}]\Theta(z,w),\qquad
P_{n,-}=\left(\frac{\Omega_-}{2\pi i}\right)^n.
\tag{974.27}
$$
There is no Gaussian factor in (974.27). Bannai--Kobayashi, Theorem 1.17 and Definition 1.5, give
$$
c_n=-\frac{e^*_{n-1,n+1}(0,0;\Lambda_-)}
{(n-1)!A(\Lambda_-)^{n-1}}.
\tag{974.28}
$$
The sign is $(-1)^{(n-1)+(n+1)-1}=-1$.

Class number one, the six units, and (974.21) give the exact lattice sum identity
$$
e^*_{n-1,n+1}(0,0;\Lambda_-)
=6\Omega_-^{-2}L(\psi_+^{2n},n+1).
\tag{974.29}
$$
To check it, first take a complex parameter in the absolutely convergent region. For $\gamma=\Omega_-\alpha$, the lattice summand is
$\Omega_-^{-2}\bar\alpha^{n-1}/\alpha^{n+1}$. Conjugation permutes the nonzero algebraic integers and turns this into
$\Omega_-^{-2}\alpha^{2n}/N(\alpha)^{n+1}$. Each integral ideal is counted six times. The identity at the boundary is then obtained by the very analytic continuation in the definition of $e^*$. No conditional rearrangement of a boundary series is needed.

Substituting (974.26), (974.28), and (974.29) into (974.25) yields
$$
\boxed{
\frac{L_{\rm TU}(\operatorname{Ad}f,1)}
{\pi^{n+2}\Omega_f^+\Omega_f^-}
=u_n c_n\frac{P_{n,-}^2}{\Omega_f^+\Omega_f^-},
\qquad
u_n=2^{n+2}3^{(n-8)/2}(n-1)!.
}
\tag{974.30}
$$
The positive real square root $\sqrt3$ is used in $3^{(n-8)/2}$. In simplifying the powers of $i$, one uses
$$
P_{n,-}^2=-\frac{\Omega_-^{2n}}{(2\pi)^{2n}},
\tag{974.31}
$$
because $n$ is odd. This minus sign cancels the minus sign in (974.28). Every factor of $u_n$ is a unit at $p$: $p>3$ and $n-1=p-r-1<p$.

The change from $E_+$ used in §§1--5 to $E_-$ is also explicit. Over an algebraic extension choose $t$ with $t^6=-1$. The isomorphism
$(x,y)\mapsto(t^2x,t^3y)$ from $E_+$ to $E_-$ pulls $\omega_-$ back to $t^{-1}\omega_+$. Hence the period lattices differ by $t^{-1}$, with a possible sixth root of unity from the choice of lattice generator. The ratio is an algebraic unit at every finite prime. Since $2n$ is divisible by six and $n/3$ is odd,
$$
P_{n,-}^2=-P_n^2
\tag{974.32}
$$
for compatible generators; any remaining generator change has $2n$-th power one. The square Hecke character (974.21) is unchanged by this quadratic twist. Equations (974.3)--(974.4) therefore apply to $P_{n,-}$ as well.

Combining (974.30) with (974.3) and the already proved R970 criterion gives the useful rigorous implication
$$
\boxed{\quad c_n\in\mathcal O_{\mathfrak p}^{\times}
\ \Longrightarrow\ \eta_f=\mathcal O
\ \Longrightarrow\ \text{the original complete trace is nonzero}.\quad}
\tag{974.33}
$$
Indeed, the left side of (974.30) has nonnegative valuation by R970, whereas its right side has nonpositive valuation by (974.3) when $c_n$ is a unit. Both valuations must be zero. The two individual integral period quotients are then units as well. This argument only requires the one-sided period bound proved here; it does not assume the period unit conclusion beforehand.

Bannai--Kobayashi source: *Algebraic theta functions and the p-adic interpolation of Eisenstein--Kronecker numbers*, author version math/0610163v4 (11 December 2007), §§1.1 and 1.4, especially Theorem 1.17; <https://arxiv.org/pdf/math/0610163>.

## 7. What this does and does not settle

The new input is a specific, directly integral bound on **the same periods** that occur in R970. It is stronger than an equality up to an arbitrary algebraic number. It does not prove a period ratio is a unit on its own and does not identify the original trace with a CM special value as a scalar.

The remaining analytic-arithmetic input is the $p$-unit status of the precisely normalized critical value of the unramified character $\psi^{2n}$ at $n+1$. The finite character of $\psi^n$ squares to one, so that square character has conductor one. Its Kronecker coefficient is the genuine two-variable coefficient with indices $(n-1,n+1)$, not a pure holomorphic Eisenstein coefficient of weight $2n$. The proof of (974.3) uses only critical indices of the original form with **sum $n$**; it says nothing about a coefficient with sum $2n$.

The local elliptic-unit/Artin--Hasse route being pursued in parallel has a different intermediate object. Neither the low FL unit nor a general two-variable radius estimate is used in (974.3).

### 7.1 Exact use of the four finite values already computed in R973

R973 supplies certified nonzero residues of this same coefficient $c_n$ for the four original cases

| $p$ | $r$ | $n=p-r$ | $c_n\bmod p$ |
|---|---|---|---|
| $41$ | $8$ | $33$ | $13$ |
| $47$ | $2$ | $45$ | $4$ |
| $227$ | $2$ | $225$ | $171$ |
| $857$ | $8$ | $849$ | $317$ |

These four previously computed coefficients can be consumed directly in (974.33), giving the nonzero original complete traces at those four primes. This is a consequence of the theorem and the existing coefficient receipt; it is not a new calculation of those traces. It does not establish the unit assertion for any uncomputed prime, and does not turn whole-trace nonvanishing into a same-label $Q'$ assertion. The latter distinction is material at $p=227$ by R945.

## 8. Primary-source boundary against a different shortcut

Bertolini--Darmon--Venerucci, *Heegner points and Beilinson--Kato elements: a conjecture of Perrin-Riou*, Remark 3.2, printed pp. 22--23, explicitly discuss the difficulty of choosing the Betti, de Rham and $p$-adic étale realizations of a higher-weight CM modular motive and the corresponding Hecke-character motive compatibly. The author PDF is
<https://www.math.mcgill.ca/darmon/pub/Articles/Research/77.BDV/bdv.pdf>.

Schappacher's absolute-Hodge period isomorphism and Blasius' theorem for Hodge classes on abelian varieties do not by themselves supply an integral comparison for the Scholl lattice. The proof above is designed to avoid that missing comparison entirely.
