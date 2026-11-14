# R133 supplement — a nearby exact phase target with the same fourth-root gap

2026-11-14. **Proved arithmetic target and exact error-transfer result.**
The principal circle return itself, the parameter Schur scalar, and the
nonlinear boundary problem are not asserted to be solved here.

## 1. The actual fitted rotation and a more compatible target

The unchanged root/transport contract has SHA256
`1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43`.
Its finite test lift $H$ uses the exact angular rotation

$$
 \Omega_{\mathrm{fit}}
   =\frac{3889733506671123}{9007199254740992}
   =0.4318471698762230692736352466\ldots .                 \tag{1}
$$

Angles have period $\pi/2$, so a normalized rotation number $\rho$
corresponds to $\Omega=\pi\rho/2$, not to $2\pi\rho$.
The previously proposed target

$$
 \rho_{\mathrm{old}}=\frac{612575-\sqrt5}{2228182}
$$

obeys the strict certified bounds

$$
 \frac{31609581821389}{10^{19}}
 <\Omega_{\mathrm{fit}}-\frac\pi2\rho_{\mathrm{old}}
 <\frac{31609581821390}{10^{19}}.                          \tag{2}
$$

In particular its discrepancy is about $3.160958182139\,10^{-6}$;
it cannot be silently treated as the fitted rotation.

There is a much closer quadratic target **with exactly the same bound
seven on all partial quotients**:

$$
 \boxed{\displaystyle
 \rho_{\mathrm{new}}
   =\frac{45217079201-\sqrt5}{164472125458},
 \qquad \Omega_{\mathrm{new}}=\frac\pi2\rho_{\mathrm{new}}.} \tag{3}
$$

Its continued fraction is

$$
 \rho_{\mathrm{new}}
 =[0;3,1,1,1,3,7,1,3,1,1,1,2,2,1,7,\overline1].          \tag{4}
$$

The strict angular comparison is

$$
 \boxed{\displaystyle
 \frac{68387956541454}{10^{24}}
  <\Omega_{\mathrm{new}}-\Omega_{\mathrm{fit}}
  <\frac{68387956541455}{10^{24}}
  <7\,10^{-11}.}                                        \tag{5}
$$

Thus the new constant target changes the certified finite-lift defect by
at most $7\,10^{-11}$. It does not change the fixed approximate centre,
its $\eta_0$, its $\nu$, the two ray fields, the original finite $H$, or
any already computed scalar or transport polynomial.

## 2. Exact construction and verification of the quadratic identity

For a finite continued fraction use

$$
 p_{-2}=0,\ p_{-1}=1,\quad q_{-2}=1,\ q_{-1}=0,\qquad
 p_k=a_kp_{k-1}+p_{k-2},\quad q_k=a_kq_{k-1}+q_{k-2}.
$$

For the prefix in (4), ending with the last displayed $7$, these exact
integer recurrences give

$$
 (p_{14},q_{14})=(11078,40295),\qquad
 (p_{15},q_{15})=(85345,310433).
$$

Let $\varphi=(1+\sqrt5)/2=[1;1,1,\ldots]$. Appending that complete
quotient gives

$$
 \rho_{\mathrm{new}}
 =\frac{85345\varphi+11078}{310433\varphi+40295}
 =\frac{107501+85345\sqrt5}{391023+310433\sqrt5}.
$$

Multiplication by the conjugate of the denominator and cancellation of
the common integer factor gives exactly (3). This proves (4), since
every displayed positive partial quotient and the tail are positive.
It also proves irrationality, because the coefficient of $\sqrt5$ in
(3) is nonzero.

The producer additionally certifies, using interval arithmetic rather
than binary64 floor operations, that

$$
 \frac{2\Omega_{\mathrm{fit}}}{\pi}
 =[0;3,1,1,1,3,7,1,3,1,1,1,2,2,1,19,\ldots].              \tag{6}
$$

Replacing the first $19$ by $7$ and taking the constant-one tail retains
the original uniform arithmetic constant. Merely matching further
partial quotients including $19$ would require changing that constant.
Formula (5), rather than a qualitative claim that the numbers are close,
is the bound used below.

## 3. Full denominator estimate, including all fourth roots of unity

We give the needed continued-fraction estimate explicitly. Let an
irrational $\rho=[a_0;a_1,\ldots]$ have $1\le a_k\le A$ for $k\ge1$,
and suppose $q_0=1<q_1$ as in (4). For every integer $n\ge1$,

$$
 \|n\rho\|_{\mathbb R/\mathbb Z}>
       \frac1{(A+2)n}.                                   \tag{7}
$$

To prove this, choose $k$ with $q_k\le n<q_{k+1}$ and write
$\alpha=[a_{k+1};a_{k+2},\ldots]$. The convergent identity gives

$$
 \rho=\frac{p_k\alpha+p_{k-1}}{q_k\alpha+q_{k-1}},\quad
 |q_k\rho-p_k|=\frac1{q_k\alpha+q_{k-1}},\quad
 q_{k-1}\rho-p_{k-1}=-\alpha(q_k\rho-p_k).                 \tag{8}
$$

For any integer $p$, unimodularity of the two adjacent convergents
provides integers $a,b$ with

$$
 (p,n)=a(p_k,q_k)+b(p_{k-1},q_{k-1}).
$$

If $|n\rho-p|<|q_k\rho-p_k|$, (8) implies $|a-b\alpha|<1$.
When $b=0$, this forces $a=0$, contrary to $n\ge1$.
When $b\ge1$, since $\alpha>a_{k+1}$, integrality gives
$a\ge ba_{k+1}$, whence
$n\ge b(a_{k+1}q_k+q_{k-1})\ge q_{k+1}$, a contradiction.
When $b\le-1$, integrality instead gives $a\le ba_{k+1}$, whence
$n\le bq_{k+1}<0$, also a contradiction. Therefore every $p$ satisfies

$$
 |n\rho-p|\ge|q_k\rho-p_k|
 >\frac1{(A+2)q_k}\ge\frac1{(A+2)n},
$$

where the strict middle inequality uses
$\alpha<a_{k+1}+1\le A+1$ and $q_{k-1}<q_k$.
This proves (7) for every denominator, without a frequency scan.

For $\rho_{\mathrm{new}}$, take $A=7$. If $j\ne0$, put
$\delta=\operatorname{dist}(j\rho_{\mathrm{new}},\tfrac14\mathbb Z)
=\|4j\rho_{\mathrm{new}}\|/4\le1/8$. Concavity of the sine on
$[0,\pi/2]$ gives $2\sin(\pi\delta)\ge4\delta$. Thus

$$
 \boxed{\displaystyle
 \min_{\zeta^4=1}|e^{4ij\Omega_{\mathrm{new}}}-\zeta|
  =2\sin(\pi\delta)
  \ge\|4j\rho_{\mathrm{new}}\|
  >\frac1{36|j|}.}                                      \tag{9}
$$

This is the same explicit principal fourth-root gap used for the old
arithmetic target. The phase factor, the normalization by $\pi/2$,
and the factor four in the denominator are all retained.

## 4. How the new target enters the actual transport certificate

Let $P$ be the complete return of the unchanged repaired centre and let
$H$ be the finite test lift in the original root contract. For every
complex input strip on which the expression is defined,

$$
 \|H\circ P-H-\Omega_{\mathrm{new}}\|
 \le\|H\circ P-H-\Omega_{\mathrm{fit}}\|+7\,10^{-11}.       \tag{10}
$$

Indeed the two defect functions differ by the constant
$\Omega_{\mathrm{fit}}-\Omega_{\mathrm{new}}$; (5) and the triangle
inequality prove (10). The complete transport formula may alternatively
subtract the exact Arb enclosure of $\Omega_{\mathrm{new}}$ directly
from its terminal Fourier mean. No scalar germ, candidate cubic,
transport interval, or unretained-frequency residual needs recomputing
for this change of the constant on the right-hand side.

The original scalar, residual, and root-sliver fees consequently remain
fees for the **same** approximate object. Equation (9) also preserves
any arithmetic inequality whose only hypothesis is the explicit
principal gap $1/(36|j|)$. There is no transfer here of a conclusion
that the actual return is conjugate to the new target.

The following obligations remain unchanged in substance:

- The full 169-germ terminal transport defect must be evaluated.
- A true conjugacy and a genuine nonzero $\nu$ Schur scalar must be
  proved, with the complete regular-state and adjoint errors included.
- If $\nu$ or the background is corrected to realize (3), every
  background-dependent bound must be checked on that corrected object
  or covered by its already proved uniform parameter bounds.
- The real $\beta/j$ phase correction, the strong return remainder,
  root amplitudes and Maslov terms, and positive-side reflection still
  enter the same full return operator. Their competition with (9) has
  not been removed by the arithmetic choice.
- Any dependence on the particular old quadratic number, beyond the
  displayed lower bound (9), must be replaced explicitly. A previously
  conditional lock to $\rho_{\mathrm{old}}$ is not a lock to (3).

The old floating value $S_\Omega\simeq0.020224$ is not used in any
proof or gate above. Neither (5) nor that floating value proves the
existence of a parameter correction. The final chosen $\nu$ must still
be fixed throughout the ultimate flex family.

## 5. Actual source and certified computation

The source is
`scripts/fourfold_codazzi_phase_nearby_bounded7_rotation.py`.
The native is
`notes/2026-11-14-R133-nearby-bounded7-phase-target-native.json`.
It records the exact integer convergents, all certified floors in (6),
the strict rational intervals (2) and (5), the original contract SHA,
and the producer SHA. All eleven gates use exact integer arithmetic
or 256-bit Arb enclosures. The infinite bound (9) is the proved lemma
of Section 3, not a finite numerical check.

```bash
python scripts/fourfold_codazzi_phase_nearby_bounded7_rotation.py \
  --root-contract notes/2026-11-14-R133-final-phase-root-sliver-and-transport-contract-native.json.gz \
  --out notes/2026-11-14-R133-nearby-bounded7-phase-target-native.json
```
