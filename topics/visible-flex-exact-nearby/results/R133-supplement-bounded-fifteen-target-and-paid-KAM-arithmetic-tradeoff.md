# R133 supplement: bounded15 target and the paid arithmetic tradeoff

2026-11-14, visible-exact-astra-0df / phase_inverse.

**Proved arithmetic and full-error statement.** Let $G=K48\circ H$
be the completed full Laurent proposal. The exact quadratic target

$$
 \boxed{\rho_{15}=
 \frac{5831714953207175+\sqrt5}{21212218271020390},
 \qquad \Omega_{15}=\frac\pi2\rho_{15}}
 \tag{B.1}
$$

has all positive continued-fraction coefficients at most15. With
every original transport/root fee and every postcomposition fee paid,
the same true return satisfies

$$
 \boxed{\|G\circ P-G-\Omega_{15}\|_{A_{1/50}}
       <1.463790602032\,10^{-13}.}
 \tag{B.2}
$$

Its principal fourth-root gap is $1/(68|j|)$, not the earlier
$1/(36|j|)$. The new target is not asserted to be the realized
rotation. The original bounded-seven targets and their results remain
available and unchanged.

## 1. Exact continued fraction and why small bounds8--10 do not suffice

The actual exact dyadic $\Omega_{\rm p}$ from the complete K48
terminal has the interval-certified prefix

$$
 \frac{2\Omega_{\rm p}}\pi
 =[0;3,1,1,1,3,7,1,3,1,1,1,2,2,1,15,5,4,8,\ldots].
 \tag{B.3}
$$

Every floor operation is certified by320-bit Arb. Keeping this
prefix through8 and then appending the infinite tail
$\overline1$ gives (B.1), by the exact integer continued-fraction
matrix and $\tau^2-\tau-1=0$. In particular

$$
 0<\Omega_{15}-\Omega_{\rm p}
 <2.2\,10^{-18}.
 \tag{B.4}
$$

The actual signed difference is enclosed around
$2.19817734229146573079355\,10^{-18}$.

There is a useful exact obstruction to merely changing7 to8,9 or10.
The open continued-fraction cylinder with the prefix in (B.3) through
its entry15 has rational endpoints

$$
 \frac{185047}{673088},\qquad \frac{173969}{632793}.
$$

Every irrational in this open interval has that entry15, by uniqueness
of the infinite continued fraction. Thus every irrational whose
positive partial quotients are all at most14 lies outside the interval.
The exact angular distances from $\Omega_{\rm p}$ to its two endpoints
are respectively greater than
$2.9487323426085\,10^{-12}$ and
$7.3922902290409\,10^{-13}$. Consequently

$$
 \operatorname{dist}(\Omega_{\rm p},
   \{\tfrac\pi2\rho:\rho\ {\rm irrational},\ a_j(\rho)\le14\})
 >7.3922902290409\,10^{-13}.
 \tag{B.5}
$$

This is a complete cylinder argument, not a scan through proposed
bounded-type targets. A target within $10^{-13}$ of this specified
proposal therefore requires maximum partial quotient at least15.
The complete true-rotation enclosure from the K48 theorem is narrower
than $1.464\,10^{-13}$, so the same triangle inequality also separates
every bounded14 target from that true rotation by more than
$5.928\,10^{-13}$.

## 2. All-denominator and all-fourth-root arithmetic

For a real irrational with all positive partial quotients at most$A$,
the complete unimodular-convergent argument in the earlier
bounded-seven theorem proves, for every integer$n\ge1$,

$$
 \|n\rho\|_{\mathbb R/\mathbb Z}>
 \frac1{(A+2)n}.
$$

Applying it with$A=15$ gives $1/(17n)$. Since
$2|\sin\pi t|\ge4\operatorname{dist}(t,\mathbb Z)$,

$$
 |e^{4ij\Omega_{15}}-1|>\frac4{17|j|}.
 \tag{B.6}
$$

For each fourth root of unity $\zeta=e^{2\pi i\ell/4}$,
apply the same irrationality bound to $4|j|$:
the distance of $j\rho_{15}-\ell/4$ to an integer is at least
$\|4j\rho_{15}\|/4>1/(272|j|)$. Therefore

$$
 \boxed{\min_{\zeta^4=1}|e^{4ij\Omega_{15}}-\zeta|
       >\frac1{68|j|}\quad(j\ne0).}
 \tag{B.7}
$$

There is no denominator cutoff. In the physical Wiener norm, the
full fourth-root homological multiplier has the direct one-derivative
loss

$$
 \sup_{j\ne0}68|j|e^{-4|j|\delta}
       \le\frac{17}{e\delta}.
$$

For the normalized circle equation against1 alone, R31 uses
$K=17/4$, from (B.6).

## 3. The actual complete error and the R31 cost comparison

The source reads the actual K48 terminal central coefficient,
the norm of every noncentral Laurent coefficient, the infinite
exponential tail, and the two paid transport/root fees. It subtracts
$\Omega_{15}$ from the central coefficient before taking its absolute
value. Their sum proves (B.2). The normalized circle error on
width1/16 is less than $5.855162408128\,10^{-13}$.
Its actual real derivative bound remains
$2.692451910125\,10^{-12}$ in physical units, because changing a
constant target does not change that derivative.

For the fixed family $F_\delta=4G P_\delta G^{-1}$ and initial lift
identity, the true parameter row is independent of the target angle.
Thus it is meaningful to compare the two target choices while holding
the other R31 inputs fixed. Let $r=17/9$, the ratio of the new and old
circle constants. R31's definitions give exactly

$$
 L_{H,15}=rL_{H,7},\qquad C_{15}\le r^2 C_7,\qquad
 Z_{15}\le rZ_7.
$$

Here $L_a,A_*,M,R$ are unchanged. Every term in$C$ is respectively
constant, linear or quadratic in$K$, and every term in$Z$ is constant
or linear. Therefore the sufficient smallness threshold can decrease
by at most

$$
 r^2=289/81<3.568.
$$

The actual complete K48 error for the bounded-seven target is
$5.553045010343\,10^{-11}$, whereas (B.2) is below
$1.463790602032\,10^{-13}$. With these certified input bounds,
the worst-case net improvement of the R31 smallness ratio is greater
than106.32598513. The parameter-domain correction shrinks by the
full error ratio; the coordinate-domain correction loses only the
factor$r$ and still improves substantially.

This is an algebraic comparison of sufficient gates, not a claim
that the unprovided uniform $P,Q,T,B$ bounds already make those
gates pass. The first scalar phase $\beta/j$, any competing
fourth-root eigenphase terms, and the strong operator remainder must
be compared with the new $1/68$ principal margin. The old $1/36$
margin is not transferred to this target.

## 4. Actual native and scope

All eight Arb/integer gates passed in.005 seconds. The source is
`scripts/fourfold_codazzi_phase_terminal_bounded15_target.py` and the
3482-byte native is
`notes/2026-11-14-R133-complete169-K48-bounded15-target-native.json.gz`,
SHA256
`94d2aaf1ef5fcccd71d4e26b40cf31518ff765bbc9e3a2103ebcb17de4fd54d4`.

The native keeps the exact quadratic identity, all prefix quotient
intervals, the full continued-fraction matrix, both cylinder endpoints,
the complete reused K48 input SHA and every paid error term.
It explicitly records the new gap cost and the outstanding strong
remainder and PDE obligations. No scalar cache, transport polynomial,
original target primitive, or physical centre was recomputed to
establish this arithmetic statement.
