# R717 — Exact original CM norms from certified complex traces

## 1. Statement and what the computation is allowed to conclude

Fix the original curve $E_0:y^2=x^3-1$, the differential $dz=dx/(2y)$,
the actual $c_1$ six-torsion marking, and $\theta=\theta_{-1}$ as in
R588/R595.  Let $p\ge41$, $p\equiv5\pmod6$, and $n=p+1$.  Define

$$
\mathcal P_p=\frac{S_2S_3}{C_0^2},\qquad
C_0=72\beta/\alpha,\quad\alpha^3=4,\quad\beta^2=3,
$$
$$
D_p=2^{37}3^{26}p^5.
\tag{717.1}
$$

The exact assertions proved below are

$$
\boxed{\mathcal P_p\in\mathbf Q(\zeta_n)^+,\qquad
D_p\mathcal P_p\in\mathbf Z[\zeta_n].}
\tag{717.2}
$$

Every complex conjugate of $\mathcal P_p$ can be calculated by two
exponentially convergent, explicitly normalized central-value sums.
Their summands can be grouped in $n$ character bins.  A rigorous
uniform tail bound is given in §6.  Three discrete Fourier transforms
then produce intervals containing the integers

$$
t_j=\operatorname{Tr}_{\mathbf Q(\zeta_n)/\mathbf Q}
       (D_p\mathcal P_p\zeta_n^{-j}),\qquad 0\le j<n.
\tag{717.3}
$$

If every interval contains a unique integer, those integers determine
the exact algebraic number, because

$$
\boxed{nD_p\mathcal P_p=\sum_{j=0}^{n-1}t_j\zeta_n^j.}
\tag{717.4}
$$

This is exact recovery using a proved denominator and certified
intervals.  It is not recognition of an algebraic number from an
uncontrolled floating-point approximation.  A failed uniqueness test
is a failed certificate, not permission to round.

The right side of (717.4) may then be evaluated at the exact selected
$p$-adic Teichmüller root.  In particular, since the unchanged R588
norm gives

$$
M_2^2=-\frac{8\zeta^2N_\theta}{(p+1)^2}C_0^2\mathcal P_p,
\qquad N_\theta\equiv-1\pmod p,
\tag{717.5}
$$

we obtain

$$
v_p(M_2)=\frac12v_p(\mathcal P_p).
\tag{717.6}
$$

R711 proves that this is an integer.  In the particular exceptional
case $p=137147$, R712/R711 already imply $\mathcal P_p$ is integral,
and $M_2$ is a unit exactly when $\mathcal P_p\not\equiv0\pmod p$.
No value at that prime is supplied by the mathematical reduction alone.

## 2. The original character labels and the cyclotomic field

Write $\mathcal O=\mathbf Z[\zeta]$, $\zeta=e^{2\pi i/3}$, and
$N(a+b\zeta)=a^2-ab+b^2$.  The actual tame character is

$$
\chi_6(\delta\zeta^i\bmod3,\zeta^j\bmod2)
       =\delta\zeta^{j-i}.
\tag{717.7}
$$

The period in this marking is the positive real period $\Omega$ of
§5, with $\alpha>0$ and $\beta>0$ in the complex embedding.  Along
$0<z<\Omega/2$, the Weierstrass derivative is negative.  Hence
$\Omega/3$ corresponds to $(\alpha,-\beta)$, $2\Omega/3$ to
$(\alpha,\beta)$, and $\Omega/2$ to $(1,0)$.  Multiplication by
$\zeta$ sends $(x,y)$ to $(\zeta x,y)$ and multiplication by $-1$
changes the sign of $y$.  The CRT representative
$a=4a_3+3a_2\bmod6$ therefore gives
$$
\frac{\Omega a}{6}
=\frac{2\Omega}{3}a_3+\frac{\Omega}{2}a_2,\qquad
(a_3,a_2)=(\delta\zeta^i,\zeta^j),
$$
and consequently the exact original point
$Q_{\delta ij}=(\alpha\zeta^i,\delta\beta)+(\zeta^j,0)$.
Thus (717.7) has the original six-torsion labels, with no extra
sign, inverse character, or rescaling of the period.

It is extended by zero to elements not coprime to $6$.  Its conductor
is $(6)$: its cubic part is nontrivial on the units modulo $2$, and
its restriction modulo $3$ is nontrivial on $1+(1-\zeta)$.

Over $\mathbf F_{p^2}=\mathbf F_p[\bar\zeta]$, the character direction
used by R595 is

$$
\theta(a)=\operatorname{Teich}(a)^{1-p}
          =\operatorname{Teich}(a/\bar a).
\tag{717.8}
$$

Choose a generator $\gamma$ of the norm-one subgroup such that
$\gamma^{n/3}=\bar\zeta$.  If $a/\bar a=\gamma^{k(a)}$, its complex
realization is $\theta(a)=\zeta_n^{k(a)}$.  This fixes the relation
between the complex generator and the final $p$-adic embedding; a
discrete logarithm convention alone would not fix that relation.
In particular $\theta(\zeta)=\zeta^{-1}$ and $\theta$ is trivial on
$\mathbf F_p^\times$.

For every $h\in(\mathbf Z/n)^\times$ with $h\equiv1\pmod3$, define
the two original Hecke characters

$$
\xi_{5,h}((a))=a^5\chi_6(a)\theta(a)^{-h},\qquad
\xi_{7,h}((a))=a^7\chi_6(a)\theta(a)^h.
\tag{717.9}
$$

The unit conditions on $-1$ and $\zeta$ hold exactly, so these are
characters of ideals, with primitive conductor $(6p)$.  On rational
integers their finite factor is $\epsilon_3$, as in R588.  No fixed
conductor-six $C_k$ is substituted for these characters.

The rational kernel assertion needed for the field is

$$
H_r/C_0\in\mathbf Q(x,y,E),\qquad r=2,3.
\tag{717.10}
$$

Here $E$ is the completed-zeta variable.  One can check (717.10)
directly from the full translated $T_r$ sums.  There is also a
Galois proof that does not require expanding their large numerators.
The automorphism $\alpha\mapsto\zeta\alpha$ changes the tame
three-torsion index by one and multiplies both $H_r$ and $C_0$ by
$\zeta^{-1}$.  Changing the sign of $\beta$ multiplies both by $-1$.
Complex conjugation changes both indices $i,j$ to $-i,-j$, and changes
the character coefficients in exactly the same way.  The quotient is
therefore rational.  The addition formulas and the algebraic values
$e_Q$ ensure the quotient is a rational function of $x,y,E$, with
the same complete kernel, not just its highest $E$ term.

Now work over $K=\mathbf Q(\zeta)$.  Galois on $E_0[p]$ commutes
with the full CM action, so it is multiplication by an element
$c\in\mathbf F_{p^2}^\times$.  Over $K(\zeta_n)$ the two finite
sums $S_2/C_0$ and $S_3/C_0$ transform by the inverse characters
$\theta(c)^{-1}$ and $\theta(c)$.  Their product is fixed.  Since
$3\mid n$, this proves
$\mathcal P_p\in K(\zeta_n)=\mathbf Q(\zeta_n)$.

More generally, if $h\equiv1\pmod3$, extend
$\sigma_h(\zeta_n)=\zeta_n^h$ to the division field.  The extra scalar
$c$ from its action on $E_0[p]$ again cancels in the product, so

$$
\sigma_h(\mathcal P_p)
=\frac{S_2(\theta^h)S_3(\theta^{-h})}{C_0^2}.
\tag{717.11}
$$

This argument does not assume that the division field and cyclotomic
field are disjoint.  The two central values in (717.9) are real:
conjugating ideals conjugates their complex coefficients.  The exact
period identity in §5 consequently makes (717.11) real.  Thus
$\mathcal P_p\in\mathbf Q(\zeta_n)^+$.  The remaining embeddings
$h\equiv2\pmod3$ have the same values as $-h\equiv1\pmod3$.

## 3. A uniform global denominator, including the primes two and three

We use the exact original kernels

$$
T_2=-\tfrac12(E^2y+2Ex^2+xy),
$$
$$
T_3=-\tfrac16(E^3x^2+3E^2xy+3Ex^3-2E+x^2y).
\tag{717.12}
$$

Every point $R=P+Q$ in their tame sums has exact order $6p$.
At a prime $\ell\ne p$, the original coordinates $x(R),y(R)$ are
integral.  Indeed, a negative $x$ valuation would place $R$ in the
formal group at the origin of the original integral Weierstrass
equation.  Torsion in that formal group has $\ell$-power order, in
contradiction to the nonzero $p$-primary component of $R$.

The completed multiplication formula, with $pQ=-Q$, is

$$
E^*(P+Q)=-\frac{e_Q}{p}
 -\frac1{p^2}D\log\psi_p(P+Q).
\tag{717.13}
$$

There is no missing quasi-period in (717.13): the completion makes
the multiplication identity an identity at torsion points.  It is
the same division-polynomial identity used in R589 to identify the
formal and algebraic values.

To bound the last term at $\ell\ne p$, pass to a good integral model.
At $\ell\ge5$ the original model is already good.  At two and three
the following explicit transformations supply good models:

$$
\begin{array}{c|c|c}
\ell&\text{transformation}&\text{good equation}\\ \hline
2& i^2=-1,\ u^3=2i,\ x=u^2x',\ y=u^3y'+i
 &y'^2+y'=x'^3\\
3&u^4=3,\ x=u^2x'+1,\ y=u^3y'
 &y'^2=x'^3+u^2x'^2+x'
\end{array}
\tag{717.14}
$$

Their discriminants are respectively $-27$ and $-16$, units at the
indicated prime.  In both cases $v_\ell(u)\ge0$, and $D=uD'$.
Division-polynomial covariance gives
$D\log\psi_p=uD'\log\psi'_p$.

The point $Q$ has nonzero reduction on these good models.  At two its
three-primary component is nonzero, and at three its two-primary
component is nonzero; prime-to-$\ell$ torsion injects into good
reduction.  Thus $[p]R=-Q$ has nonzero reduction and
$\psi'_p(R)$ is a unit.  Its logarithmic derivative is integral.
Equation (717.13) proves

$$
v_\ell(E^*(P+Q))\ge\min\{0,v_\ell(e_Q)\}
                 \qquad(\ell\ne p).
\tag{717.15}
$$

The actual six-torsion coordinates are integral and the original
completed values are

$$
e_Q=\frac{y_Qx_Q^2(-19x_Q^6+4328x_Q^3-16)}{5184}.
\tag{717.16}
$$

Consequently (717.15) gives bounds $-6$ at two, $-4$ at three, and
zero at every other $\ell\ne p$.  Applying (717.12), summing the
roots-of-unity character weights, and then multiplying yields

$$
\begin{array}{c|ccc}
&S_2&S_3&S_2S_3\\ \hline
v_2&\ge-13&\ge-19&\ge-32\\
v_3&\ge-8&\ge-13&\ge-21.
\end{array}
\tag{717.17}
$$

Since $C_0^2=15552/\alpha^2$, one has
$v_2(C_0^2)=14/3$ and $v_3(C_0^2)=5$.  Therefore

$$
v_2(\mathcal P_p)\ge-110/3,
\qquad v_3(\mathcal P_p)\ge-26.
\tag{717.18}
$$

At $p$, every nonzero $p$-torsion point is in the supersingular formal
group, with $v_p(Y(P))=1/(p^2-1)$.  The original R589 primitive
estimate gives $v_p(E(P))>-1$: its pole has valuation $-1/(p^2-1)$,
the terms with one $p$ in their index have valuation at least
$p/(p^2-1)-1$, the first possible two-$p$ index is $5p^2$, and all
higher index valuations are still larger.  In the exact addition
formula the slope has valuation $-1/(p^2-1)$ and $e_Q$ is integral.
Thus $v_p(E(P+Q))>-1$.  Also $P+Q$ reduces to the nonzero prime-to-$p$
point $Q$, so its coordinates are integral.  It follows that

$$
v_p(S_2)>-2,\quad v_p(S_3)>-3,
\quad v_p(\mathcal P_p)>-5.
\tag{717.19}
$$

The bounds hold at every place of the algebraic fields in question,
not just at one selected embedding.  Equations (717.18)--(717.19) and
integrality elsewhere prove $D_p\mathcal P_p$ is an algebraic
integer.  Together with §2 and the ring of integers of a cyclotomic
field, this proves (717.2).  The exponents in $D_p$ are deliberately
uniform bounds, not asserted optimal denominators.

## 4. Both original root numbers and the exact Gauss sums

For $M=6p$, let $\eta=\chi_6\theta^{\pm h}$ be either finite factor
from (717.9).  If $a=A+B\zeta$, use the additive character

$$
\mathbf e_M(a)=e^{2\pi iB/M},\qquad
\tau_M(\eta)=\sum_{a\bmod M}\eta(a)\mathbf e_M(a).
\tag{717.20}
$$

The two local computations are exact:

$$
\tau_6(\chi_6)=-6,\qquad
\tau_p(\theta^{\pm h})=p.
\tag{717.21}
$$

Here is a short evaluation of the first one, retaining the CRT sign.
Write $a=3b+2c$, with $b\in(\mathcal O/2)^\times$ and
$c\in(\mathcal O/3)^\times$.  The character contributes a minus
sign because $2\equiv-1\pmod3$.  The two resulting sums are

$$
\sum_{b=1,\zeta,\zeta^2}\zeta^{j(b)}(-1)^{B(b)}
=1-\zeta-\zeta^2=2,
$$
$$
\sum_{c=\delta\zeta^i}\delta\zeta^{-i}\zeta^{B(c)}
=2-\zeta-\zeta^2=3.
$$

Their signed product is $-6$.

For the second computation put $\delta=\sqrt{-3}=1+2\zeta$ in
$\mathbf F_{p^2}$.  Then $B(a)=\operatorname{Tr}(a/\delta)$.
For any nontrivial character $\nu$ trivial on $\mathbf F_p^\times$,
the sum of $\nu$ on the nonzero trace-zero fiber is
$(p-1)\nu(\delta)$, while its sum on each nonzero trace fiber is
$-\nu(\delta)$.  Hence the standard trace Gauss sum is
$p\nu(\delta)$.  Scaling its additive character by $\delta^{-1}$
multiplies it by $\nu(\delta)$, and
$\nu(\delta)^2=\nu(-3)=1$.  This gives the second equality of
(717.21), in exactly the additive character (717.20).

Now write $a=pc+6b$.  The factor $\chi_6(p)=-1$, whereas
$\theta(6)=1$.  Thus

$$
\boxed{\tau_{6p}(\chi_6\theta^{\pm h})
=-\tau_6(\chi_6)\tau_p(\theta^{\pm h})=6p.}
\tag{717.22}
$$

For clarity about the archimedean phase, consider

$$
\Theta_{\ell,\eta}(y)=\sum_{a\in\mathcal O}
\eta(a)a^\ell
\exp\left(-\frac{2\pi yN(a)}{\sqrt3M}\right),
\qquad \ell=5\text{ or }7.
\tag{717.23}
$$

The covolume of $\mathcal O$ is $\sqrt3/2$ and its Euclidean dual is
$(2i/\sqrt3)\mathcal O$.  In Poisson summation on $M\mathcal O$,
the finite sum at the dual point $2ib/(M\sqrt3)$ is
$\tau_M(\eta)\eta(b)$: its additive phase is precisely the
$\zeta$ coefficient of $a\bar b$ divided by $M$.  The transform of
$z^\ell e^{-\pi t|z|^2}$ is
$(-i)^\ell t^{-\ell-1}w^\ell e^{-\pi|w|^2/t}$.  The $i^\ell$
from the dual lattice cancels $(-i)^\ell$, so no additional guessed
weight sign remains.  Including the covolume gives

$$
\Theta_{\ell,\eta}(y)
=\frac{\tau_M(\eta)}M y^{-\ell-1}
\Theta_{\ell,\eta}(1/y)
=y^{-\ell-1}\Theta_{\ell,\eta}(1/y).
\tag{717.24}
$$

Thus both root numbers are $+1$.  This permits a nonzero central
value; it does not prove that either value is nonzero.

## 5. The two central-value sums and every period factor

Put

$$
c_p=\frac{\pi}{3\sqrt3p},\qquad
K_r(t)=e^{-t}\sum_{j=0}^r\frac{t^j}{j!}.
\tag{717.25}
$$

Mellin transforming (717.23), splitting the integral at $1$, and using
(717.24) at the center gives the exact identities

$$
\boxed{
\begin{aligned}
L(\xi_{5,h},3)
 &=2\sum_{(\mathfrak a,6p)=1}
       \frac{\xi_{5,h}(\mathfrak a)}{N\mathfrak a^3}
       K_2(c_pN\mathfrak a),\\
L(\xi_{7,h},4)
 &=2\sum_{(\mathfrak a,6p)=1}
       \frac{\xi_{7,h}(\mathfrak a)}{N\mathfrak a^4}
       K_3(c_pN\mathfrak a).
\end{aligned}}
\tag{717.26}
$$

There is one term per ideal.  A convenient unique generator is
$a+b\zeta$ with $a>0$, $0\le b<a$.  This is the half-open angular
sector $0\le\arg(z)<\pi/3$.  The conditions of being coprime to
$6p$ are respectively $(a,b)\not\equiv(0,0)\pmod2$,
$a+b\not\equiv0\pmod3$, and
$(a,b)\not\equiv(0,0)\pmod p$.

The positive real period of the original curve is

$$
\Omega=\int_1^\infty\frac{dx}{\sqrt{x^3-1}}
=\frac{\Gamma(1/6)\Gamma(1/2)}{3\Gamma(2/3)},
\qquad A=\frac{\sqrt3\Omega^2}{2\pi}.
\tag{717.27}
$$

R588's original CRT identities, including their signs and factorials,
are

$$
L(\xi_{5,h},3)=\frac{\Omega\,2!A^2}{36p}S_2(\theta^h),
\quad
L(\xi_{7,h},4)=\frac{\Omega\,3!A^3}{36p}S_3(\theta^{-h}).
\tag{717.28}
$$

Therefore each required conjugate is exactly

$$
\boxed{
\sigma_h(\mathcal P_p)
=\frac{\alpha^2p^2}{144\Omega^2A^5}
 L(\xi_{5,h},3)L(\xi_{7,h},4),
\qquad h\equiv1\pmod3.
}
\tag{717.29}
$$

Here $\alpha=\sqrt[3]{4}>0$ in the complex calculation.  The final
$p$-adic reinsertion of $C_0^2$ uses the unique cube root of $4$
modulo $p$, as required by R595.  Equation (717.29) includes both
factorials, both occurrences of $36p$, the original real period, and
the original completed-zeta covolume.  Omitting any of them would
invalidate the integer trace recovery.

## 6. A rigorous tail bound for every character simultaneously

Let $X$ be a positive integer cutoff for the ideal norm.  The number
of ideals of norm $m$ in $\mathbf Q(\zeta)$ is at most the divisor
function $d(m)\le2\sqrt m$.  Also

$$
\left|\frac{\xi_{2r+1,h}(\mathfrak a)}
                  {N\mathfrak a^{r+1}}\right|
       =(N\mathfrak a)^{-1/2}.
$$

The tail of the corresponding sum in (717.26) has absolute value at
most $4\sum_{m>X}K_r(c_pm)$.  Since
$K'_r(t)=-e^{-t}t^r/r!\le0$, comparison with the integral gives

$$
\boxed{
\mathcal E_r(X)=\frac4{c_p}e^{-c_pX}
  \sum_{j=0}^r(r-j+1)\frac{(c_pX)^j}{j!}
}
\tag{717.30}
$$

as a valid uniform error bound for $r=2,3$.  This includes the factor
two in the central-value formula.  It bounds the whole omitted
lattice, not selected shells or an empirically small final summand.

A certificate chooses an integer $b$ and verifies with outward-rounded
ball arithmetic that both $\mathcal E_2(X),\mathcal E_3(X)<2^{-b}$.
It then enlarges each real central-value interval by the exact radius
$2^{-b}$.  The complete constants in (717.29), the two Fourier sums,
and the trace transforms are computed with interval arithmetic as
well.  Thus their final radii include the analytic tails and every
arithmetic rounding error.

For a fixed error target, the necessary cutoff is of size
$O(p(b+\log p))$.  The sector has $O(X)$ lattice points.  This
procedure does not expand any elliptic series through degree $p^2$.

## 7. Fourier bins, exact trace recovery, and a complete certificate

For each lattice generator $a+b\zeta$ of norm at most $X$, let
$k=k(a+b\zeta)$ from (717.8).  Accumulate two bins, with no character
power inserted yet:

$$
B_5[k]=\sum\frac{(a+b\zeta)^5\chi_6(a+b\zeta)}{N(a+b\zeta)^3}
                         K_2(c_pN(a+b\zeta)),
$$
$$
B_7[k]=\sum\frac{(a+b\zeta)^7\chi_6(a+b\zeta)}{N(a+b\zeta)^4}
                         K_3(c_pN(a+b\zeta)).
\tag{717.31}
$$

The two truncated central values for $h\equiv1\pmod3$ are
$2\sum_kB_5[k]\zeta_n^{-hk}$ and
$2\sum_kB_7[k]\zeta_n^{hk}$.  Add the tails from §6 and apply
(717.29).  Fill the conjugate entry at $-h$ with the same real value;
set entries at nonunits modulo $n$ equal to zero.  The negative
Fourier transform of this array, multiplied by $D_p$, contains exactly
the integers in (717.3).

An implementation may use Bluestein convolution with
$\epsilon=e^{\pi i/n}$, since

$$
\zeta_n^{jk}=\epsilon^{j^2+k^2-(j-k)^2}.
\tag{717.32}
$$

Using ball polynomial multiplication here retains a certified error
bound; no unverified floating-point FFT is needed.  The signs of the
first two transforms and the final negative transform are fixed by
(717.31) and (717.3).

For every $j$, the final ball must contain exactly one ordinary
integer and must contain zero in its imaginary part.  Integrality
from §3 then forces that integer to equal $t_j$.  Summing the trace
definition against $\zeta_n^j$, and using finite character
orthogonality, gives (717.4): only the embedding $h=1$ survives.

A full reproducibility certificate contains the parameters and source
hash, the exact finite-field generator and its order checks, the
integer cutoff and tail inequalities, exact dyadic representations
of all bin intervals, all final trace intervals and their unique
integers, and the resulting integer polynomial.  If the work is
sharded by rows $a$, the row ranges are disjoint and cover the whole
sector; each shard records its completed range and hash before a
separate checked merge.  Partial and failed outputs remain evidence
of an incomplete calculation and are not labelled a successful
reconstruction.

## 8. The selected $p$-adic value, with no numerical root matching

Use the exact unramified ring

$$
R_s=(\mathbf Z/p^s\mathbf Z)[Z]/(Z^2+Z+1).
\tag{717.33}
$$

Lift the recorded finite-field generator $\gamma$ uniquely to
$\widehat\gamma\in R_s$ satisfying $\widehat\gamma^n=1$ and
$\widehat\gamma\bmod p=\gamma$.  Hensel's derivative is a unit
because $p\nmid n$.  The check
$\widehat\gamma^{n/3}=Z$ preserves the complex-to-$p$-adic orientation
in (717.8).  Evaluate the exact polynomial from (717.4) at this root.

The result has zero $Z$ coefficient modulo $p^s$.  Indeed Frobenius
sends $\widehat\gamma$ to $\widehat\gamma^{-1}$, and the exact
polynomial represents a real cyclotomic number.  This is an exact
descent check, not a floating-point test that a component is small.

Since $n2^{37}3^{26}$ is a $p$-adic unit, an evaluation modulo
$p^{5+k}$ determines $\mathcal P_p\pmod{p^k}$ whenever
$\mathcal P_p$ is integral.  More generally, the first nonzero
$p$-adic digit of the numerator determines its valuation after
subtracting the known five powers of $p$ in $D_p$.

If the recovered polynomial is zero modulo the exact cyclotomic
polynomial $\Phi_n$, then $\mathcal P_p=0$ exactly.  Otherwise it
cannot vanish at any characteristic-zero primitive $n$th root;
increasing $s$ must eventually reveal its first nonzero $p$-adic digit.
One must not infer exact zero merely from zero at a chosen precision.

Finally, if $v=v_p(\mathcal P_p)$, then (717.5) and
$N_\theta\equiv-1\pmod p$ give the fully normalized leading square

$$
\overline{p^{-v}M_2^2/\zeta^2}
=8\,\overline{C_0^2}\,\overline{p^{-v}\mathcal P_p}
\quad\text{in }\mathbf F_p.
\tag{717.34}
$$

For a calibration of this genuinely new computation, the retained
old $p=41$ certificate has $p^2S_2S_3\equiv1274\pmod{41^2}$;
its mod-$41$ residue is $3$, giving
$(pM_2)^2/\zeta^2\equiv24$.  The new path can be checked against
those existing values without repeating the old torsion-orbit or
Cartier computation.  Any actual new numerical conclusion is to be
taken only from the public runner's complete interval-and-integer
certificate.
