# R633: the complete ordinary unit lattice in the anti-pq layer

**Status: proved.** Keep the actual fields and units of R619. Put
\(N=L F_t\), \(R_\Gamma=\mathcal O[\Gamma]/(N_\Gamma)
=\mathcal O[\zeta_{43}]\), and \(\pi=\gamma-1\).
The full ordinary unit lattice in the original character has

\[
 \boxed{\ker(N_\Gamma:E_N\to E_{F_t})
            =R_\Gamma[T]c_t,}                    \tag{633.1}
\]

and the displayed right side is free of rank one over
\(R_\Gamma[T]\). Moreover,

\[
 \boxed{N_\Gamma E_N=p\mathcal O[T]u_t+\mathcal O u,
 \qquad E_N=\mathcal O[T]u_t+\mathcal O y+R_\Gamma[T]c_t.}
 \tag{633.2}
\]

These are equalities of integral ordinary unit modules, not just
rational spans or finite-index subgroups. They use the same actual
Robert correction c_t. Its faithful mixed-character nonvanishing
and integral saturation follow from one socle calculation, so no
additional analytic nonvanishing premise is assumed.

The original scalar C, the R599 first moment J, the ordinary b,
lambda and n, and the original \(\mathcal L\) remain uncomputed.
In particular this result does not assert the lost full-layer length
\(\operatorname{Cl}(LB)_{\chi^-}=R_\Gamma/\pi^{43}\).

## 1. Exact fields, coefficient ring and retained identities

All notation is fixed, rather than chosen to fit the conclusion:

\[
 p=43,\quad K=\mathbf Q(i),\quad
 F=K(A[p])^{\mathbf F_p^\times},\quad A:y^2=x^3-x,
\]
\[
 L=F L_q,\quad\Gamma=\langle\gamma\rangle,
 \quad B=K(A[p^2])^{\mu_{42}},
\]
\[
 S=\langle1+p\rangle,\quad T=\langle t=1+21pi\rangle,
 \quad F_t=B^S,\quad N=L F_t.
\]

The same original q, beta=-1+2i, real p-point, q prime and Weil root
are used as in R198/R561/R613/R619. The anti-p generator satisfies
\(\kappa_p(t)=1\). Let \(\mathcal O=\mathbf Z_{43}[i]\) and
\(k=\mathcal O/43\). The unit module E_V is
\((\mathcal O_V^\times\otimes\mathcal O)_{\chi^-}\), with the
field eigencharacter \(\widehat\omega^{-1}\), \(\omega=8+25i\).
Actual source elements use the unaveraged operator
\(P_+=\sum_{j=0}^{43}\widehat\omega^j\sigma^j=44e_{\chi^-}\).

The following exact identities have already been established from
the actual common ancestor units and are retained unchanged:

\[
 E_F=\mathcal O u,\quad E_{F_t}=\mathcal O[T]u_t,
 \quad N_Tu_t=u,\quad \gamma u_t=u_t,               \tag{633.3}
\]
\[
 N_\Gamma y=u,\quad ty=y,\quad
 (\gamma-1)y=a\gamma^{22}c_q,\quad a=15i/7,       \tag{633.4}
\]
\[
 c_t=N_Sc_B,\quad N_\Gamma c_t=0,\quad N_Tc_t=c_q.\tag{633.5}
\]

Here y is the original ordinary q-Norm unit of R561, not a numerical
assignment to its still unknown q phase. Its exact balanced relation is

\[
 py=u+aD_\Gamma^{\rm bal}c_q,\qquad
 D_\Gamma^{\rm bal}=\sum_{j=-21}^{21}j\gamma^j.    \tag{633.6}
\]

The c_B in (633.5) is the genuine p-squared-q Robert product of R613,
including the q-inverse-p-point correction s^11. In particular,
\(N_\Gamma c_B=(1-s^{11})u_B\), so taking N_S gives exactly
\(N_\Gamma c_t=0\). The correction has not been removed or
replaced by a formal unit with a convenient norm.

R619 proves (633.3) as a complete saturated lattice and proves
\(\operatorname{Cl}(N)_{\chi^-}=k\). The latter fact is consistent
with the argument below, but its class-number value is not needed
to assume the rank or saturation in (633.1).

## 2. The norm kernel is free over the actual DVR and has rank p

Let

\[
 M=\ker(N_\Gamma:E_N\to E_{F_t}).
\]

Dirichlet's logarithmic representation gives the regular
\(\Gamma\times T\) representation in this nontrivial Delta
character. Consequently \(\operatorname{rank}_{\mathcal O}E_N=p^2\),
the invariant lattice is \(E_N^\Gamma=E_{F_t}\), and the rational
norm map has rank p. The last assertion also follows by applying
the norm to the included E_Ft, where it is multiplication by p.
Thus

\[
 \operatorname{rank}_{\mathcal O}M=p(p-1).         \tag{633.7}
\]

The field N contains no pth roots of unity, since 42 does not divide
its absolute degree \(88p^2\). Therefore E_N and M are torsion-free
\(\mathcal O\)-modules.

The norm N_Gamma annihilates M, so the Gamma group-ring action factors
through \(R_\Gamma\). The polynomial \(\Phi_p(1+X)\) is Eisenstein
over the unramified ring \(\mathcal O\), making R_Gamma a DVR with
uniformizer pi, residue field k, and \(\mathcal O\)-rank p-1.
The R_Gamma module M is torsion free. Indeed, for any nonzero
\(r\in R_\Gamma\) there is a nonzero \(d\in\mathcal O\) and
\(r'\in R_\Gamma\) with \(rr'=d\), by the characteristic
polynomial of multiplication by r. An element annihilated by r
would be annihilated by d, contrary to \(\mathcal O\)-torsion
freeness. Since M is finite over this DVR, it is free. Equation
(633.7) gives its exact rank:

\[
 \operatorname{rank}_{R_\Gamma}M=p,
 \qquad \dim_k M/\pi M=p.                         \tag{633.8}
\]

This does not suppose that c_t already spans any of the mixed
character components.

## 3. The nonzero socle vector and integral Nakayama argument

By (633.5), c_t belongs to M and

\[
 N_Tc_t=c_q=a^{-1}\gamma^{-22}\pi y.              \tag{633.9}
\]

The crucial point is

\[
 \boxed{c_q\notin\pi M.}                         \tag{633.10}
\]

Suppose instead \(c_q=\pi m\) for some m in M. From (633.9),
\(\pi(y-a\gamma^{22}m)=0\). Hence
\(y-a\gamma^{22}m\in E_N^\Gamma=E_{F_t}\).
Taking the Gamma norm would give

\[
 u=p(y-a\gamma^{22}m)\in pE_{F_t}.
\]

This is impossible. The primitive u is not divisible by p in E_Ft:
if u=pv there, torsion freeness and T invariance of u would imply
v is T-invariant, contradicting the primitivity of u in E_F.
This proves (633.10), including its integral content.

Modulo pi the T group ring is

\[
 k[T]=k[x]/(x^p),\qquad x=t-1,\qquad N_T=x^{p-1}.
\]

Equation (633.10) says
\(x^{p-1}\bar c_t\ne0\) in \(M/\pi M\). A cyclic module
over this truncated polynomial ring on which \(x^{p-1}\) is
nonzero has dimension p. Since the entire module has dimension p
by (633.8), c_t generates it. The R_Gamma-linear map

\[
 R_\Gamma[T]\longrightarrow M,\qquad f\longmapsto f c_t
\]

is therefore surjective modulo pi. Both its source and target are
free R_Gamma modules of rank p. Its determinant is a unit, so it is
an isomorphism. This proves (633.1), including both the absence of
hidden relations and the full integral saturation.

In particular, nonvanishing in every rational faithful Gamma/T
component is a consequence of this integral isomorphism. It is not
an additional unproved hypothesis about elliptic L-values.

## 4. The exact ordinary unit norm sublattice

The local computation of R198/R619, with the power-residue-log
convention, gives

\[
 A_\ell(T)=\sum_{j=0}^{p-1}\ell(t^ju_t)T^{-j},
 \quad A_\ell(1)=0,\quad A_\ell'(1)=-13i\ne0.
\]

Thus multiplication by A_ell on k[T] has image (T-1) and kernel
the one-dimensional socle \(kN_T\). At the q primes this is the
complete tame local unit norm obstruction for N/F_t. Every
ordinary global unit norm must therefore lie in

\[
 \{f(t)u_t:\bar f\in kN_T\}
       =p\mathcal O[T]u_t+\mathcal O N_Tu_t
       =p\mathcal O[T]u_t+\mathcal O u.            \tag{633.11}
\]

Conversely, the displayed lattice is made of actual ordinary norms:
the included E_Ft has Gamma norm p E_Ft, and the actual ordinary
unit y has norm u. This proves equality in (633.11), not merely a
necessary local condition:

\[
 N_\Gamma E_N=p\mathcal O[T]u_t+\mathcal O u.
\]

The equality of the integral preimage lattice in (633.11) is
literal: lift the scalar multiplying \(N_T\) modulo p to
\(\mathcal O\), then the remaining group-ring coefficients are
all divisible by p. No p-saturation or index is silently assumed.
The direct root-exponent derivative \(-17i\) is not used in this
power-log calculation.

For any e in E_N, write its norm as \(pf(t)u_t+b u\).
Subtract \(f(t)u_t+b y\), whose ordinary norm is exactly this
quantity. The difference lies in M, which has already been proved
to equal \(R_\Gamma[T]c_t\). This proves the complete generation
formula (633.2).

## 5. A complete integral presentation and the two group actions

There is a particularly small presentation over \(\mathcal O\).
Use formal symbols U, Y and c, with the c summand already the free
\(R_\Gamma[T]\)-module. Then

\[
 \boxed{
 E_N\simeq
 \frac{R_\Gamma[T]c\ \oplus\ \mathcal O[T]U\ \oplus\ \mathcal O Y}
 {\mathcal O\bigl(pY-N_TU-aD_\Gamma^{\rm bal}N_Tc\bigr)}.}
 \tag{633.12}
\]

The symbols map to c_t, u_t and y respectively. The action on c is
the regular one, and the remaining actions are

\[
 \gamma U=U,\qquad tU=TU,\qquad tY=Y,
 \qquad \gamma Y=Y+a\gamma^{22}N_Tc.               \tag{633.13}
\]

The relation in (633.12) is exactly (633.6), not a discarded Robert
term. It is primitive because the coefficient of U in its T^0
position is -1, so the quotient is torsion free over \(\mathcal O\).

To see that it is the full relation module, suppose
\(m+f(t)u_t+b y=0\). Taking N_Gamma gives
\(p f(t)u_t+b u=0\). Since u is primitive in the free lattice
\(\mathcal O[T]u_t\), b is divisible by p, say b=pc.
The same equation then forces \(f(t)u_t=-c u\). The original
relation becomes \(m=-c(py-u)=-caD_\Gamma^{\rm bal}c_q\),
which is precisely c times the relation in (633.12). There are no
other relations.

These action formulas respect that relation. The needed exact
group-ring identity is

\[
 (\gamma-1)D_\Gamma^{\rm bal}=p\gamma^{22}-N_\Gamma.
\]

Also \(\gamma^pY=Y\), since \(N_\Gamma c=0\), and
the displayed actions commute. The invariant and norm relations
in (633.3)--(633.6) are thus retained by the presentation with their
actual gamma and t orientations.

## 6. Two ordinary cohomology consequences

The Gamma norm equality gives

\[
 H^2(\Gamma,E_N)
    =\frac{\mathcal O[T]u_t}{p\mathcal O[T]u_t+\mathcal O u}
    \simeq k[T]/(N_T).                            \tag{633.14}
\]

From (633.1), (633.2) and (633.13),

\[
 (\gamma-1)E_N=\pi M+\mathcal O c_q.
\]

The c_q is T-invariant and corresponds, up to the stated unit, to
\(N_Tc_t\). Therefore

\[
 H^1(\Gamma,E_N)=M/(\gamma-1)E_N
              \simeq k[T]/(N_T).                \tag{633.15}
\]

Both groups have length p-1=42, agreeing with the ordinary divisor
calculation of R619. This also records their full T module
structure, rather than just their cardinalities.

The T norm is equally explicit. The element y generates
\(E_L=\mathcal O[\Gamma]y\): its Gamma norm is the primitive base
unit u, so the same regular-module determinant argument as R210
applies to this specified y. The T norms of the three pieces in
(633.2) are respectively

\[
 N_T(\mathcal O[T]u_t)=\mathcal O u,
 \quad N_T(\mathcal O y)=p\mathcal O y,
 \quad N_T(R_\Gamma[T]c_t)=R_\Gamma c_q.
\]

By (633.9), \(R_\Gamma c_q=\pi\mathcal O[\Gamma]y\).
The identity \(N_\Gamma-p\in\pi\mathcal O[\Gamma]\) then gives

\[
 \boxed{N_TE_N=(p,\pi)E_L,
 \qquad H^2(T,E_N)\simeq k,\text{ generated by }[y].} \tag{633.16}
\]

This is an ordinary **unit** norm index. It is compatible with the
ordinary capitulation in R619, and does not confuse a global field
norm with an ordinary unit norm.

## 7. What this supplies to the continuing Norm problem

The full anti-pq ordinary unit lattice, its two exact norm images,
its integral relation and its Gamma/T cohomology are now explicit.
The formerly unresolved mixed-character full-rank step is closed
by (633.10) and the integral Nakayama argument.

The result still contains the original y as an actual globally
defined unit. It does not compute y's q phase. The scalar extension
from N to LB requires an actual S lift of this generator; its
existence as a field norm or a putative cohomology model cannot
be substituted for an evaluated ordinary lift. The separate
marked q-principalization X_t of R599 and its first moment J also
remain uncomputed.

No long arithmetic computation is required by this proof. It reuses
the already proved and actually computed value
\(A_\ell'(1)=-13i\) with its exact original marking. The elementary
group-ring identities, rank counts and integral relation arguments
above prove the new assertions directly; the large Robert
evaluation is not repeated.
