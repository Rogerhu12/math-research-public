# R768: the original supported dual Kummer class and its ordinary companion

Date: 2026-11-14. **Status: proved.** The restriction to $M$ of the
actual Gamma/scalar dual primitive need not be an ordinary unit
class. Its possible ideal-class component is, however, exactly a
multiple of the original nonzero q socle, and the same marked
$X_t$ is an actual Kummer lift of that socle. Subtracting this
specified lift gives an ordinary class satisfying the full three
direction equations below. The ideal coefficient is intrinsic,
real, and unchanged by the original finite-flat correction.
The coefficient satisfies $b\lambda_{\rm id}=0$. If $b\ne0$,
the true dual restriction is already represented by an ordinary
unit class in the original $T$-fixed scalar field.
This result does not evaluate $J_\ell,b,\sigma_2,I_\alpha$.

The proof also puts R766's remaining two diagonal terms and the
true ordinary companion in one common integral construction.
It does not replace a supported global primitive by an arbitrary
solution of its necessary local or module equations.

## 1. The actual full-divisor Kummer sequence

Keep $p=43$, $\mathcal O=\mathbf Z_{43}[i]$, $k=\mathcal O/p$,
$M=LB$, $P=S\times T$, $\pi=\gamma-1$, and $X=t-1$.
Every character module uses the original unaveraged $P_+$.
Write

$$
\mathscr K_M=(M^\times\otimes\mathcal O)_{\chi^-},
\quad E_M=(\mathcal O_M^\times\otimes\mathcal O)_{\chi^-},
\quad D_M=(\operatorname{Div}_{\rm fin}M\otimes\mathcal O)_{\chi^-}.
$$

Define the group of full-divisor Kummer classes

$$
\mathscr V_M=
\{a\in\mathscr K_M:\operatorname{div}a\in pD_M\}
/p\mathscr K_M.
$$

There is an exact sequence, with all the original commuting actions,

$$
\boxed{
0\longrightarrow E_M/pE_M
\longrightarrow\mathscr V_M
\xrightarrow{\partial_{\rm id}} A_M[p]
\longrightarrow0,\qquad
\partial_{\rm id}[a]=[\operatorname{div}(a)/p].
}
\tag{768.1}
$$

This is a full ordinary class group, not a class group with the
q primes deleted. To check exactness, a p-torsion ideal class has
a divisor $D$ for which $pD$ is principal, furnishing a lift $a$.
If the class of $D$ is zero, write $D=\operatorname{div}c$;
then $a-pc$ is an ordinary unit. Finally an ordinary unit in
$p\mathscr K_M$ already belongs to $pE_M$, since $D_M$ is
torsion-free. These statements are preserved by the flat
coefficient extension and the prime-to-p character projector.

We use the Kummer identification already fixed in R756 for the
restriction of $W(1)$ to $G_M$. It is the identification with
the indicated character part of $\mathscr K_M/p\mathscr K_M$.
It does not require that $M$ contain $\mu_p$: the coefficient
on $G_M$ is the Tate twist, and the Kummer exact sequence is
used with that twist retained.

The actual unit and q principalizations are

$$
\operatorname{div}_{F_t}X_t=P_+P_0,\qquad
N_TX_t=A_\alpha,\qquad
\operatorname{div}_M X_t=p\mathfrak q,
$$
$$
\mathfrak q=P_+Q_M,\qquad
e_q=[\mathfrak q]\in A_M.
\tag{768.2}
$$

R715 and R731 prove

$$
A_M=R_\Gamma/\pi^{43},\qquad
A_M^\Gamma=ke_q,\qquad e_q\ne0,\qquad pe_q=0.
\tag{768.3}
$$

In particular

$$
\boxed{\kappa(X_t)\in\mathscr V_M,\qquad
\partial_{\rm id}\kappa(X_t)=e_q.}
\tag{768.4}
$$

Thus $\kappa(X_t)$ is not in $E_M/pE_M$. The fact that its
localization at q is zero, proved below, cannot change (768.4).

## 2. The true supported dual primitive has no omitted finite valuations

Use the original support $\Sigma=\{2,p,q,\infty\}$ and the actual
negative-adjoint direction of R755,

$$
y=\ell_{\rm cyc}-2i\kappa_q
  =2\kappa_S-2i\kappa_q.
$$

Let $E_\alpha$ be any supported primitive with

$$
\delta E_\alpha=y\cup d_q,\qquad d_q=\kappa(A_\alpha).
\tag{768.5}
$$

On $G_M$, the direction $y$ vanishes. Hence its restriction is
a cocycle. Denote its Kummer class by $e_\alpha$.
R756's conjugation computation gives

$$
\pi e_\alpha=-2i[\mathcal U],\qquad
(s-1)e_\alpha=2[\mathcal U],\qquad
Xe_\alpha=0,
\tag{768.6}
$$

where the actual ordinary unit is

$$
\mathcal U=A_\alpha-pZ,\qquad
\operatorname{div}_M Z=N_T\mathfrak q,\qquad
N_\Gamma Z=N_SZ=N_TZ=A_\alpha.
\tag{768.7}
$$

Brackets on ordinary units mean their classes in $E_M/pE_M$
and then in Kummer cohomology.

We verify that $e_\alpha$ belongs to the full group $\mathscr V_M$.

Outside $\Sigma$, the pair consisting of $d_q$ and $E_\alpha$
is unramified. The usual local Kummer valuation of an unramified
class is zero modulo $p$ at residue characteristic different
from $p$. Thus no omitted outside-support divisor occurs.

At $p$, the complete character prime-divisor module is zero:
the original nontrivial $\Delta$ character is inertial, while
a prime divisor is fixed by inertia. This is the same actual
prime-divisor calculation used in R657 and R700. Thus no
character valuation at $p$ survives, without imposing an
unproved finite-flat condition on $E_\alpha$.

At $2$, package $(d_q,E_\alpha)$ as a cocycle for the extension
of $W(1)$ by itself with off-diagonal action $-y$.
The original local calculation is
$H^1(\mathbf Q_2,W(1))=0$. The short exact sequence for this
extension therefore gives zero $H^1$ for the full two-step
module as well. The pair is locally a coboundary.
On $G_M$, where the off-diagonal character is zero, the
restriction of its second component is a coboundary.
Hence $e_\alpha$ is locally zero above $2$.

At q one can prove the stronger statement

$$
\boxed{e_\alpha|_{M_Q}=0\quad\text{at every q prime }Q.}
\tag{768.8}
$$

Indeed, work first over the original quadratic completion
$K_q=\mathbf Q_{q^2}$. In R755's notation

$$
v=\kappa_S+i\kappa_q,\qquad
\mathfrak p=-i\bar v^{\,2}.
$$

After the exact local gauge correction, the primitive is
$\mathfrak p$ plus a local k-valued one-cocycle.
The correction being removed is $y$ times a local
zero-cochain. On $G_{M_Q}$ it is zero because $y=0$.

The original local extension $M_Q/K_q$ has group
$\Gamma\times S$: $\Gamma$ is the ramified degree-$p$
factor and $S$ the unramified degree-$p$ factor; $T$ splits.
The marked values are $v(f)=32$ and $v(x_q)=i$.
Both $v$ and every k-valued local one-cocycle factor
through this elementary abelian quotient. Explicitly,
the two possible additive characters are determined by
their values on the unramified generator $f$ and tame
generator $x_q$; they kill $f^p$, $x_q^p$, their
commutators, and the q-primary wild inertia.
Their restrictions to $G_{M_Q}$ are therefore zero.
The quadratic cochain $\mathfrak p$ also restricts to zero.
This proves (768.8), with the local quadratic correction
and all marked translates retained.

The same argument also gives

$$
\boxed{\kappa(X_t)|_{M_Q}=0.}
\tag{768.9}
$$

Here is a direct Kummer check. The q completion of $F_t$
at each marked prime is $K_q$. Its unit classes become
p-th powers after the unramified degree-$p$ extension:
the p-primary residue group grows from $\mu_p$ to
$\mu_{p^2}$, and principal units are p-divisible.
The original real uniformizer satisfies
$\theta^p/q$ with zero p-primary unit phase in $M_Q$,
so $q$ also becomes a p-th power. Thus restriction
kills all of $K_q^\times/K_q^{\times p}$, including
the actual local class of $X_t$. This proves (768.9)
without asserting that $X_t$ is a global p-th power.

There are no odd-primary archimedean valuations to retain.
The preceding checks prove $e_\alpha\in\mathscr V_M$.

## 3. The intrinsic socle coefficient and the unique ordinary companion

Apply $\partial_{\rm id}$ to the first equation of (768.6).
Since $\mathcal U$ is an ordinary unit, its image is zero.
By (768.3), there is therefore a unique $\lambda_{\rm id}\in k$
with

$$
\partial_{\rm id}(e_\alpha)=\lambda_{\rm id}e_q.
\tag{768.10}
$$

Use the specified lift (768.4) and set

$$
\boxed{
e_{\rm ord}=e_\alpha-\lambda_{\rm id}\kappa(X_t)
\in E_M/pE_M.
}
\tag{768.11}
$$

This ordinary class is uniquely determined by $e_\alpha$ and
the fixed original $X_t$. A representative unit of its class
is of course determined only modulo $pE_M$.

The coefficient is independent of the choice of the supported
primitive. The complete supported dual cohomology space is,
by R743,

$$
H^1(G_{\mathbf Q,\Sigma},W(1))
=\mathbf F_p d_0\oplus\mathbf F_p d_q.
$$

Its two restrictions are ordinary classes:

$$
d_0|_M=\left[\frac{i}{1848}u\right],\qquad
d_q|_M=[\mathcal U].
\tag{768.12}
$$

Thus any global primitive change has zero ideal-class image.
Coboundaries make no change either. In particular the exact
remaining change of the ordinary companion is

$$
e_{\rm ord}\longmapsto e_{\rm ord}
+a\left[\frac{i}{1848}u\right]+c[\mathcal U],
\qquad a,c\in\mathbf F_p.
\tag{768.13}
$$

These are changes of the true supported primitive. A larger
solution space of bare module equations is not substituted
for this precise global ambiguity.

Use the same real $X_t$ as R763/R766.
Its divisor makes $\tau e_q=e_q$, while rational restriction
makes $\tau e_\alpha=e_\alpha$ under the original semilinear
Kummer action. Applying $\tau$ to (768.10) gives

$$
\boxed{\lambda_{\rm id}\in\mathbf F_{43}.}
\tag{768.14}
$$

Consequently the ordinary companion is also real as a class.
It may be represented by a real ordinary unit by averaging,
since $2$ is a unit in $\mathcal O$.
This rationality assertion does not set the coefficient to zero.

The same coefficient is obtained for the original flat target.
Indeed R755 gives

$$
E_{\rm fl}=E_\alpha+8e_c(d_0)-8e_q(d_0).
\tag{768.15}
$$

Both reference primitives on the right restrict to ordinary
Kummer classes on $M$. For the scalar reference this follows
from the original ordinary norm ancestor $u_s$, with
$N_Su_s=u$; for the q reference it follows from the original
ordinary norm unit $y$, with $N_\Gamma y=u$.
The standard positive norm cochains of R200/R749 restrict
to derivative combinations of these ordinary units.
Any other supported choices add only the two ordinary
classes (768.12). Thus their ideal-class images are zero,
and (768.15) preserves $\lambda_{\rm id}$.
This uses only ordinariness of the reference constructions;
it does not replace the unknown pairing $I_\alpha$ by the
known scalar reference value $9\varepsilon$.

## 4. A single actual antiderivative of the q-prime difference

Apply R736's simultaneous ordinary norm lemma with $d(T)=T-1$.
Its augmentation is zero. It gives a genuine global q-unit
$Q_X$ with

$$
\operatorname{div}_M Q_X=X\mathfrak q,\qquad
N_\Gamma Q_X=N_SQ_X=XX_t.
\tag{768.16}
$$

This uses the full divisor and the original q labels.
Define the ordinary unit

$$
\boxed{h_X=XX_t-pQ_X\in E_M.}
\tag{768.17}
$$

Its Kummer class is independent of all allowed choices of
$Q_X$, because their differences are ordinary units. Precisely,

$$
[h_X]=X\kappa(X_t),\qquad
\pi h_X=-p\pi Q_X,\qquad
(s-1)h_X=-p(s-1)Q_X.
\tag{768.18}
$$

The derivatives of $Q_X$ in the last two formulas are ordinary:
both groups fix the complete divisor $X\mathfrak q$.

For this $Q_X$, R766's general exchange supplies
$R_X=B_\Gamma B_SQ_X=pH_X-\rho_Xu$ with

$$
\pi H_X=B_SQ_X,\quad
(s-1)H_X=B_\Gamma Q_X,\quad
N_\Gamma H_X=N_SH_X=\rho_Xu.
$$

R763's ordinary torsor correction applies with exactly the
same original unit $Z_y$ satisfying $N_SZ_y=y$.
The element $V_y=\pi(s-1)Z_y$ has both norms zero and

$$
B_\Gamma B_SV_y\equiv u\pmod{pE_M}.
$$

It changes the residue of $\rho_X$ by $-1$ and keeps (768.16).
One can therefore arrange $R_X\in pE_M$ and take its actual
ordinary quotient as $H_X$. The resulting exact equations are

$$
\boxed{
H_X=R_X/p\in E_M,\quad
N_\Gamma H_X=N_SH_X=0,\quad
\pi(s-1)H_X=-h_X.
}
\tag{768.19}
$$

This does not prescribe $N_TH_X$.

For completeness these choices can respect the real marking.
First replace $Q_X$ by $(Q_X-t\tau Q_X)/2$.
It preserves (768.16) and gives $\tau Q_X=-t^{-1}Q_X$.
As $\tau B_\Gamma=-\gamma B_\Gamma\tau$ and
$\tau B_S=B_S\tau$, one has
$\tau R_X=\gamma t^{-1}R_X$.
The residual $\rho_X$ is consequently purely imaginary modulo p.

R763 constructs the ordinary $V_\tau$ with
$\tau V_\tau=-V_\tau$ and
$B_\Gamma B_SV_\tau\equiv iu\pmod p$.
The translated unit $t^{22}V_\tau$ satisfies

$$
\tau(t^{22}V_\tau)=-t^{-1}(t^{22}V_\tau),
$$

because $2\cdot22\equiv1\pmod{43}$, and it has the same
coefficient $i$ in the displayed congruence.
A scalar in $\mathbf Z_p$ therefore clears $\rho_X$ while
preserving this real law. After taking the quotient in (768.19),

$$
\tau H_X=\gamma t^{-1}H_X,\qquad
\tau h_X=-t^{-1}h_X.
\tag{768.20}
$$

Every change made here is an allowed ordinary torsor change.
In particular it leaves $[h_X]$ and the original moment unchanged.

## 5. The forty-step primitive is represented by D_T H_X modulo p

R766's last two Taylor polynomials satisfy

$$
d_{40}=43\cdot881+X d_{41},\qquad
d_{41}=1805+42X.
$$

The element $d_{41}$ is a unit of $\mathcal O[T]$,
since its augmentation is nonzero modulo p.
The top witness in that proof may therefore be chosen as

$$
Y_{40}=881X_t+d_{41}(t)Q_X.
\tag{768.21}
$$

Its full divisor and both norms are exactly those required
for $d_{40}$. Conversely any such top witness recovers a
$Q_X$ by the integral formula
$d_{41}^{-1}(Y_{40}-881X_t)$.
Thus this is an equivalence between actual global norm
witnesses, not a formal antiderivative in a residue ring.

The balanced Gamma and scalar operators kill the $X_t$ term.
Starting R766's lower recursion from (768.21), equations
(768.19) give the exact unaveraged common primitive

$$
\mathcal L_{\Gamma S}=X^{41}d_{41}(t)H_X.
$$

The difference between $D_T$ and $X^{41}d_{41}$ has every
coefficient divisible by p. It follows that

$$
\boxed{
[\mathcal L_{\Gamma S}]=D_T[H_X],\qquad
[\mathcal U]=-D_T[h_X].
}
\tag{768.22}
$$

The second equality also follows directly from
$XD_T=p-N_T$ and (768.17), so it fixes the sign independently.

The real average of R766 preserves (768.22).
Indeed, if $q_0=X^{41}d_{41}$, its averaged common primitive
is $(q_0-\tau q_0)H_X/2$ by (768.20).
Modulo p one has $q_0=D_T$ and
$\tau D_T=p(N_T-1)-D_T=-D_T$.
Thus the averaged primitive still equals $D_TH_X$ modulo p.
All integral three-norm and depth statements of R766 remain
valid; (768.22) concerns their additional marked mod-p description.

## 6. The ordinary companion satisfies the complete retained system

Since $X_t$ is fixed by Gamma and S, (768.6), (768.11),
and (768.18) give

$$
\boxed{
\begin{aligned}
\pi e_{\rm ord}&=-2i[\mathcal U],\\
(s-1)e_{\rm ord}&=2[\mathcal U],\\
X e_{\rm ord}&=-\lambda_{\rm id}[h_X].
\end{aligned}
}
\tag{768.23}
$$

The third equation retains the nonordinary ideal-class lift.
Replacing it by $Xe_{\rm ord}=0$ would already impose the
unproved assertion $\lambda_{\rm id}[h_X]=0$.

There are also the exact mod-p norm constraints

$$
\boxed{
N_\Gamma e_{\rm ord}=N_Se_{\rm ord}=0,\qquad
N_Te_{\rm ord}=-\lambda_{\rm id}[\mathcal U].
}
\tag{768.24}
$$

For the first two, $\mathcal U$ is fixed by Gamma and S
modulo p: each derivative of (768.7) is p times an ordinary
unit. Thus, for instance,
$\gamma^je_\alpha=e_\alpha-2ij[\mathcal U]$.
Summing for $j=0,\ldots,p-1$ gives zero, since both p and
$p(p-1)/2$ vanish in characteristic p.
The scalar calculation is identical.
The two norms of $\kappa(X_t)$ are zero because $X_t$ is fixed.
For T, (768.6) gives $N_Te_\alpha=0$, while
$N_T\kappa(X_t)=\kappa(A_\alpha)=[\mathcal U]$.
This proves (768.24).

By (768.8)--(768.9), $e_{\rm ord}$ is locally zero at every q
prime as a Kummer class. This means its unit residue is a
p-th power in the actual $\mu_{p^2}$ residue group.
It does not assert that every integral representative has
zero full $\mu_{p^2}$ phase.

Here is a useful exact way to display the remaining corrections.
In $E_M/pE_M$ put

$$
e_* = 2D_T\bigl(\pi-i(s-1)\bigr)[H_X].
$$

Using (768.19)--(768.22), its discrepancies from (768.23) are

$$
\begin{aligned}
\pi e_*&=-2i[\mathcal U]+2D_T\pi^2[H_X],\\
(s-1)e_*&=2[\mathcal U]-2iD_T(s-1)^2[H_X],\\
Xe_*&=-2N_T\bigl(\pi-i(s-1)\bigr)[H_X].
\end{aligned}
\tag{768.25}
$$

Consequently the actual difference $r=e_{\rm ord}-e_*$
has the full system

$$
\boxed{
\begin{aligned}
\pi r&=-2D_T\pi^2[H_X],\\
(s-1)r&=2iD_T(s-1)^2[H_X],\\
Xr&=-\lambda_{\rm id}[h_X]
       +2N_T\bigl(\pi-i(s-1)\bigr)[H_X],\\
N_\Gamma r&=N_Sr=0,\qquad
N_Tr=-\lambda_{\rm id}[\mathcal U].
\end{aligned}
}
\tag{768.26}
$$

In the norm line we used $N_\Gamma H_X=N_SH_X=0$
and $N_TD_T=p\cdot21N_T=0$ modulo p.
The two diagonal terms and the top T norm are all retained.
The existence of the genuine supported $E_\alpha$ proves
that an actual $r$ of this kind exists; selecting an arbitrary
solution of (768.26) alone would not certify the supported
global cochain or its regularized q pairing.

## 7. A nonzero ordinary Bockstein fixes the original normalization

The unit $[\mathcal U]$ in the last norm equation is nonzero.
Its precise ordinary Bockstein can be calculated without
evaluating $J_\ell$ or a new norm unit.

Let $e_L=[P_+Q_L]$ be the original nonzero ordinary class of $L$.
The extension of its full divisor to $M$ is exactly
$N_T\mathfrak q$: S is unramified at q and T splits, so
no ramification factor p is inserted in this extension.
Thus the same $Z$ in (768.7) gives its principalization in $M$.

For $M/L$ the full character divisor invariants descend:
$D_M^P=jD_L$. Away from p the extension is unramified,
and the p-prime character module is zero. Hilbert 90 and
the full divisor sequence consequently identify
$\ker(A_L\to A_M)$ with $H^1(P,E_M)$, sending a
principalization $Z$ to the cocycle $g\mapsto(g-1)Z$.
Its value for the present original class is nonzero.
In the original R715/R720 convention,

$$
[(g-1)Z]_{g\in P}=\frac19[f_t].
\tag{768.27}
$$

The factor 9 is the actual R619 Artin coefficient of
$f_t$, not a choice of generator for this proof.

Let $\beta_P:(E_M/pE_M)^P\to H^1(P,E_M)[p]$ be the
connecting map for multiplication by p. The divisor of
$Z$ is P invariant, and $A_\alpha$ is P fixed. Therefore

$$
\frac{(g-1)\mathcal U}{p}=-(g-1)Z,
$$

with an ordinary unit on the right. It follows that

$$
\boxed{
\beta_P[\mathcal U]=-\frac19[f_t]\ne0.
}
\tag{768.28}
$$

This verifies $[\mathcal U]\ne0$ with the original sign
and normalization. In particular (768.24) gives

$$
\lambda_{\rm id}=0
\quad\Longleftrightarrow\quad N_Te_{\rm ord}=0.
\tag{768.29}
$$

It is an equivalence about the true ordinary companion,
not a proof of either side. The two true primitive changes
in (768.13) have T norm zero, so this reading of the
coefficient is independent of all those changes.

There is no confusion between the two q classes used here.
The class $e_q$ in (768.3) is the nonzero socle class in $M$
and is lifted by $\kappa(X_t)$. The class $e_L$ in (768.27)
is the original class in $L$ which capitulates in $M$
through the divisor of $Z$.

## 8. T invariance forces b times the ideal coefficient to vanish

Put $V=M^T=LF_s$. Since $Xe_\alpha=0$, the coefficient
in (768.10) satisfies the stronger ordinary transfer condition

$$
\boxed{\lambda_{\rm id}e_q\in j_{M/V}A_V=N_TA_M.}
\tag{768.30}
$$

Here is a full-divisor proof. Choose an ordinary representative
of (768.11) and a lift $\widehat\lambda\in\mathcal O$ of
$\lambda_{\rm id}$. It gives a representative $a$ of $e_\alpha$
with the exact divisor
$\operatorname{div}a=p\widehat\lambda\mathfrak q$.
The equality $X[a]=0$ in Kummer cohomology means
$Xa=pB$ for a genuine global completed element $B$.
Its divisor is $\widehat\lambda X\mathfrak q$.
Applying $N_T$ and using the absence of p-torsion in
$\mathscr K_M$ gives $N_TB=0$.

Hilbert 90 for the actual cyclic extension $M/V$ now gives
$B=XC$ with $C\in\mathscr K_M$. Consequently

$$
X(\widehat\lambda\mathfrak q-\operatorname{div}C)=0.
$$

The divisor in parentheses is a full T-invariant divisor.
The extension $M/V$ is ramified only at p; its complete
p-prime character module is zero. At every other prime its
invariant orbit sum is exactly the extension of the base prime.
Therefore $D_M^T=jD_V$, with no omitted finite-divisor term.
Its class is $\lambda_{\rm id}e_q$, proving the first
inclusion in (768.30).

The class norm $A_M\to A_V$ is onto. Indeed $M/V$ has
prime degree and is ramified at p, so it is disjoint over
$V$ from the ordinary Hilbert class field of $V$.
Base change and the positive ideal Artin map give the
surjective class norm, exactly as in R684 §2.4.
Since $j\circ\mathrm{Nm}=N_T$, its image after extension
is $N_TA_M$. This proves the equality in (768.30).

Use now the actual marked action
$t=1+b\pi+O(\pi^2)$, where $b\in\mathbf F_{43}$.
The integral transfer calculation of R684 §4 is

$$
N_T=\sum_{j=0}^{42}\binom{43}{j+1}(t-1)^j
\equiv (b^{42}-1)\pi^{42}\pmod{\pi^{43}}.
\tag{768.31}
$$

The term $j=0$ is $p\equiv-\pi^{42}$.
Every intermediate term has valuation at least 43,
and the last term contributes $b^{42}\pi^{42}$.
Thus the formula includes $b=0$ and makes no division
by the action $t-1$.

For $b\ne0$, Fermat's equality gives $N_TA_M=0$.
Since $e_q\ne0$, (768.30) forces $\lambda_{\rm id}=0$.
For $b=0$, the image is instead the nonzero socle $ke_q$,
so the same argument imposes no further condition on
$\lambda_{\rm id}$. In all cases

$$
\boxed{b\lambda_{\rm id}=0.}
\tag{768.32}
$$

In particular, under the original possible obstruction value
$b=24$, the true restricted primitive is ordinary:
$e_\alpha=e_{\rm ord}$. This is not a contradiction to
$b=24$, and is not a proof that the original obstruction
is nonzero.

## 9. For nonzero b the genuine dual class descends to an ordinary scalar-layer unit

Assume $b\ne0$ for this section, and continue to write
$V=M^T$ and $N=M^S=LF_t$. R684 gives

$$
A_V=A_M/(t-1)A_M\simeq k,\qquad
j_{M/V}=0.
\tag{768.33}
$$

The actual class groups $A_L$ and $A_N$ are also $k$.
The extension map $A_L\to A_N$ is zero: the original
generator $e_L$ extends to $N_T[P_+Q_N]=p[P_+Q_N]=0$.
Thus the full ordinary capitulation identifications are

$$
H^1(T,E_M)\simeq A_V,\qquad
H^1(T,E_N)\simeq A_L.
\tag{768.34}
$$

Each follows from Hilbert 90 and the full invariant-divisor
equality, as in §7; no ramified p divisor survives the character.

The actual norm between the two groups in (768.34) is an
isomorphism:

$$
\boxed{
N_S:H^1(T,E_M)\xrightarrow{\sim}H^1(T,E_N).
}
\tag{768.35}
$$

It is important that its target is the smaller unit lattice.
To prove (768.35), first the class norm
$\mathrm{Nm}_{V/L}:A_V\to A_L$ is onto: $V/L$ has
degree p and is ramified at p, so the same ordinary
Hilbert-class-field disjointness argument applies.
Both groups have length one; hence it is an isomorphism.

The capitulation diagram identifies that class norm with
the displayed unit-cohomology norm, including its sign.
If $\operatorname{div}_M z=j_{M/V}D_V$, then its cocycle
is $(t-1)z$. Taking the S norm gives the cocycle
$(t-1)N_Sz$, and its full divisor is

$$
\operatorname{div}_N N_Sz
=j_{N/L}\mathrm{Nm}_{V/L}D_V.
$$

Extension and norm of ideals commute in this actual
base-change square. Away from p this can also be checked
orbit by orbit; at q the residue factor p occurs on both
sides, and at p the character divisor module is zero.
There is no division by p in the diagram. This proves
(768.35). The endomorphism $N_S$ on the upper cohomology
module alone would not establish this assertion.

Let
$\beta_T:(E_M/pE_M)^T\to H^1(T,E_M)[p]$
be the ordinary p-Bockstein. Under $b\ne0$, (768.32)
gives $e_\alpha=e_{\rm ord}$, and (768.6) makes it T invariant.
The norm in (768.24) is zero in $E_N/pE_N$ as well as
in $E_M/pE_M$. Indeed $E_N$ is p-saturated in $E_M$:
if $pv$ is S fixed, torsion-freeness forces $v$ to be S fixed.
Naturality of the connecting map therefore gives

$$
N_S\beta_T(e_\alpha)=\beta_T(N_Se_\alpha)=0.
$$

The injectivity in (768.35) implies $\beta_T(e_\alpha)=0$.
The same argument applies to $[\mathcal U]$, whose S norm
is zero even integrally. The multiplication-by-p exact
sequence now supplies unique ordinary classes
$e_V,U_V\in E_V/pE_V$ mapping respectively to
$e_\alpha$ and $[\mathcal U]$.

These are the actual restrictions of $E_\alpha$ and $d_q$
to $G_V$. The direction $y$ is already zero on $G_V$,
so $E_\alpha|_{G_V}$ is a cocycle. Restriction of Kummer
classes from $V$ to $M$ is injective here.
One can check this in the completed multiplicative groups:
if $a\in\mathscr K_V$ and $a=pc$ with $c\in\mathscr K_M$,
then $p(t-1)c=0$ and the absence of p-torsion makes
$c$ T fixed, hence $c\in\mathscr K_V$.
The same check applies after the original character projection.
Thus the ordinary lifts just obtained agree with the true
Kummer restrictions, rather than merely with arbitrary
T-invariant classes over $M$.

They satisfy, in the actual scalar-layer unit lattice,

$$
\boxed{
\begin{aligned}
e_V&=[E_\alpha|_{G_V}]\in E_V/pE_V,\qquad
U_V=d_q|_V\in E_V/pE_V,\\
\pi e_V&=-2iU_V,\qquad (s-1)e_V=2U_V,\\
N_\Gamma e_V&=N_Se_V=0.
\end{aligned}
}
\tag{768.36}
$$

The norm equalities have their actual targets
$E_{F_s}/pE_{F_s}$ and $E_L/pE_L$; saturation of the
corresponding invariant lattices justifies them.
Both classes are real. At q the extension $M/V$ is split,
so the q-local vanishing proved in §2 remains valid for
$e_V$ and $U_V$ at every original q prime of $V$.

The only changes coming from the true global primitive
are still the two classes in (768.13), now in $E_V/pE_V$.
No value of $e_V$ or its rational regularized q pairing
has been assigned. For $b=0$, neither the isomorphism
(768.35) in this form nor the conclusion (768.36) has
been asserted.

## 10. Exact remaining arithmetic

The marked supported dual restriction now has the actual form

$$
e_\alpha=e_{\rm ord}+\lambda_{\rm id}\kappa(X_t),
$$

with (768.23)--(768.28), the genuine q-local vanishing, the
real condition, and the exact global ambiguity (768.13).
The same ideal coefficient persists for $A_{\rm fl}$ and satisfies
$b\lambda_{\rm id}=0$. It cannot be altered by changing the supported primitive,
by an allowed ordinary change of the norm witness, or by
using the q-local vanishing of $\kappa(X_t)$.

R755's numerical target remains the regularized local pairing
$I_\alpha=-\langle w_q,\mathscr S_\alpha\rangle$.
The restricted class over $M$ does not by itself recover that
pairing: passage to the original rational cochain, including
its quadratic local term and global descent, is still required.
Likewise no equality between the ideal coefficient,
$\sigma_2$, and the unknown $b$ has been inferred.

When $b\ne0$, the genuine primitive has the stronger ordinary
scalar-layer realization (768.36). In particular this applies
under $b=24$, but does not exclude that value by itself.
The next comparison can therefore use the actual $E_V$ lattice
and its Gamma and scalar norm equations without deleting an
unproved ideal-class term.

The new result records an actual global obstruction component
and a common ordinary system for the genuine primitive. It
does not identify abstract one-dimensional quotients or claim
that the original first moment, b, or the second obstruction
has been evaluated.

## Dependencies

- [R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md):
  the original q principalization and the Artin coefficient 9.
- [R657](R657-full-ordinary-class-module-and-exact-scalar-norm-criterion.md):
  the exact local decomposition and the p-prime divisor character.
- [R684](R684-ordinary-intermediate-class-groups-and-all-p-direction-transfers.md):
  full pure-p invariant divisors, class norms, transfers, and the scalar field.
- [R700](R700-p-ramified-free-lattices-and-the-retained-ordinary-quotient.md):
  the full ordinary and local character conventions.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md)
  and [R720](R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md):
  the actual class endpoint, original cocycle, and its normalization.
- [R731](R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md):
  the genuine nonzero q socle and all full ordinary corrections.
- [R736](R736-original-three-norm-exchange-and-minus-four-moment-phase.md):
  the actual simultaneous norm lemma, $X_t,Y,Z$, and q uniformizer.
- [R743](R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md),
  [R749](R749-original-scalar-primitive-and-the-exact-reference-pairing.md),
  and [R755](R755-exact-dual-Gamma-scalar-primitive-for-the-original-flat-target.md):
  complete supported cohomology, ordinary reference primitives,
  local quadratic gauge, negative adjoint, and the real flat target.
- [R756](R756-original-three-norm-ordinary-lattice-and-exact-scalar-cohomology.md),
  [R763](R763-ordinary-torsor-normalization-with-fixed-moment-and-real-marking.md),
  and [R766](R766-original-T-descent-and-the-forty-step-ordinary-exchange.md):
  the original cube, allowed ordinary corrections, and integral T descent.
