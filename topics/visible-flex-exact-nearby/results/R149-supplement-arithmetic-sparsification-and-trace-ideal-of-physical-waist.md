# R149 ASQ9. Exact arithmetic sparsification of the original waist complement

**Proved on the original selected operator.** Inside the original
$J=2^{4608}$ split, the model divisors give a simultaneous inverse
on all modes outside an explicit sparse set. The remaining ordinary
$q$ count is below $2^{1126}$. This is genuine elimination of a
subset of the original complement, without replacing it by the 96
physical inputs. The same model inverse into the $H^{-4/3}$ window
is trace class, with an explicit small trace-norm tail. These facts
are unconditional for WDH's selected homogeneous row. For the full
positive-coupled row the numerical statements below require its
actual common high WPL bound $A_+\le2^{1293}$ on CG's domain.

## The bounded factor before the diagonal inverse

Use $Y=Y_a^0$, WGB's exact reference inverse $\bar G$ and the
normalized reflected bases of
[WCS.7–12](R133-supplement-certified-Cayley-gap-on-the-reflected-waist-model.md).
One positive frequency $n$ is one real coordinate. In $H^{-4/3}$ the
singular value of the $n$th inverse coordinate, $n\ge97$, is exactly
$$
 t_n=\frac{\Lambda_n^{-4/3}}{|q_n|},\qquad
 |q_n|=\tfrac12 |1-i\nu_i/(4n)|\,|\lambda_n-i|,\quad
 \lambda_n=e^{2\pi i n\rho_{15}}C_{\mu_*}(4n).
 \tag{ASQ9.1}
$$
The first 96 reference coordinates have their own exact comparison
isometry, with the indicated Sobolev weights. They are all retained.

Write $K=T\bar G$ in the true WDH.22/CG.9 order. Before $\bar G$
the homogeneous error has norm below $2^{1167+316}=2^{1483}$;
the full reference correction, including low output, has norm below
$2^{17+316}=2^{333}$ by ASQ5. For the coupled positive term the
ordered map before $\bar G$ has norm below $2^{190}A_+$ by CG.10–13
(with zero contribution if $A_+=0$). Thus in either stated case
$$
 \|T:H^{-4/3}\longrightarrow Y\|<2^{1485}.
 \tag{ASQ9.2}
$$
In a high *output* the finite reference correction vanishes. No
variable projector has been commuted with a cutoff to get (ASQ9.2).

## Invert all the safe frequencies together

Retain $1\le n<2^{1125}$. On each dyadic shell $N=2^b$,
$1125\le b<4608$, retain precisely the integers satisfying
$$
 \|n\rho_{15}-1/4\|_{\mathbb R/\mathbb Z}\le
 r_b=8/N+2^{1486-b-\lfloor b/3\rfloor}.
 \tag{ASQ9.3}
$$
All the others in these shells are safe. Indeed
$|C_{\mu_*}(4n)-1|\le |\mu_*|/(4n)<32/N$ by WDH.4.
An unperturbed chord has length at least four times circular
distance in turns. On the safe set this yields
$|\lambda_n-i|>2^{1488}N^{-4/3}$, hence
$|q_n|>2^{1487}N^{-4/3}$ and $t_n<2^{-1487}$. All $n\ge J$
also have $t_n\le 2^9\Lambda_J^{-1/3}<2^{-1487}$ by WDH.24.
Write $P_s$ for the union of these old high and new safe modes.
Orthonormal diagonal summation in (ASQ9.1) gives the **same**
upper $2^{-1487}$ for $\|\bar G P_s\|_{Y\to H^{-4/3}}$. Thus
$$
 \|K P_s\|<1/4,\qquad
 \|(I+P_s K P_s)^{-1}\|\le4/3\quad\text{on }P_sY.       \tag{ASQ9.4}
$$
This controls a simultaneous block, including its different-shell
and retained-tail interactions. For any bounded physical columns
and affine sources its reconstruction is the full signed
$p_s=(I+P_s K P_s)^{-1}P_s(f-Kq_s-Xc-g_{\rm met}k)$, with
$q_s=(I-P_s)w$. Substitution in the low waist, $\Theta$, weighted
phase and same-world height rows gives exactly ASQ4.2–3/ASQ6.9 with
$P_s,I-P_s$. All 96 actual root inputs and all full source
particulars remain. In particular $P_s$ contains only modes above
512, so CFC's global column-tail observation $\|P_s X\|\le\delta_X$
still applies. The full physical and reference contributions remain
in $KP_s$, including its low output.

To count (ASQ9.3), PD.13 gives
$\|(n-m)\rho_{15}\|>1/(136\pi |n-m|)>1/(512N)$ for distinct
indices in one shell. The arc in (ASQ9.3) is an interval inside
$(0,1)$, since $r_{1125}<1/4$ and the radii decrease. It contains
at most $1+1024Nr_b=8193+2^{1496-\lfloor b/3\rfloor}$ points.
Summing in groups of three shells from $b=1125=3(375)$ gives
$$
 \operatorname{rank}(I-P_s)
 < 2^{1125}+3483(8193)+6\,2^{1496-375}<2^{1126}.          \tag{ASQ9.5}
$$
The original cutoff is unchanged. The new projection gives the
proved inverse on its entire complement in $Y$. The remaining
integer upper is still too large for a dense inversion.

For exact addressing one can count any interval without visiting
its frequencies. For $l=1/4-r_b$, $u=1/4+r_b$, membership equals
$\lfloor n\rho+1-l\rfloor-\lfloor n\rho+1-u\rfloor$; there are
no rational endpoint ties. The
[exact count helper](../scripts/fourfold_codazzi_sparse_waist_frequency_count.py)
uses this formula and Euclidean floor sums. In detail, for rational
shift $a/v$, $d=21212218271020390$, and $1\le n<L$, the distance
of $n\rho+a/v$ from each integer, if less than one, is at least
$1/[d v^2(d+5L)]$. The numerator after multiplication by $dv$ has
form $U+nv\sqrt5$, $U$ integral. Its nonzero algebraic norm has
absolute value at least one; its conjugate is at most $v(d+5L)$
when the distance is less than one. Thus replacing $\sqrt5$ by
$2^{-p}\lfloor2^p\sqrt5\rfloor$ is exact for these floors whenever
$2^p>L v^2(d+5L)$. The integer square root realizes this bound.
After quotient removal, for integers $0\le A,B<m$, let
$N' =\lfloor(AN+B)/m\rfloor$, $B'=(AN+B)\bmod m$.
Counting the same lattice pairs by height gives
$\sum_{j=0}^{N-1}\lfloor(Aj+B)/m\rfloor
=\sum_{j=0}^{N'-1}\lfloor(mj+B')/A\rfloor$ if $N'>0$.
The zero case terminates. This proves the implemented decreasing
Euclidean recursion, also for arbitrary intercepts after Euclidean
quotient removal. No full frequency list or new actual count is
assumed.

## A trace-norm estimate at the original tail

Here the Cayley drift can be tracked more accurately on short
intervals. For $N=2^b$, $b\ge7$, split $[N,2N)$ into 128 equal
subintervals. For distinct indices at distance $d\le N/128$ in one
subinterval, the Cayley factors differ by at most $32d/N^2$:
differentiate $(1-i\mu_*/(8x))/(1+i\mu_*/(8x))$ on real $x\ge N$.
PD.13 therefore gives chord separation of the actual points $\lambda_n$
at least $1/(68d)-32d/N^2>1/(136d)\ge128/(136N)$.
An arc of chord radius $s$ around $i$ has length at most $\pi s$
(for $s\ge2$ use the full circumference). Summing the 128 packing
counts gives at most $128+512Ns$ points. If $\delta_j$ denotes the
$j$th increasingly ordered distance, then
$\delta_j\ge j/(1024N)$ for $j>256$. For all the first 256
use the original CYA bound $\delta_j\ge1/(2048N)$.
Counting all signs once as in WCS.9 yields
$$
 \sum_{N\le n<2N}|q_n|^{-1}
 \le N[2^{20}+2^{11}(1+b)] .
 \tag{ASQ9.6}
$$
The finite range $97\le n<128$ is already covered by WCS.
The harmonic sum estimate here is $\sum_{j\le N}1/j\le1+\log N
\le1+b$. Hence, using $2^{-1/3}<4/5$,
$$
 \sum_{n\ge 2^b}t_n
 \le 2^{-b/3}
 [5\,2^{20}+2^{11}(5(b+1)+20)] .
 \tag{ASQ9.7}
$$
This proves trace-class summability of $\bar G:Y\to H^{-4/3}$.
At $b=4608$ the bracket is less than $2^{26}$.
With original high output the homogeneous $PKP$ thus has trace norm
$<2^{1483+26-1536}=2^{-27}$. On the coupled gate above the entire
$PKP$ has trace norm $<2^{-26}$. In particular the original
homogeneous high Fredholm determinant differs from one by
$\le e^{2^{-27}}-1<2^{-26}$, and the coupled one by $<2^{-25}$.
For completeness the determinant bound follows by the absolute
exterior-power expansion: if the singular values sum to $t$, the
$k$th sum of products of distinct singular values is at most
$t^k/k!$, and it bounds the absolute trace of the $k$th exterior
power by finite-rank approximation. This also establishes convergence
for the uncompressed $I+K$ and its finite-rank bordered modifications.
No sign or nonvanishing of that **full** determinant follows from
the small *tail* determinant. In particular this theorem neither
certifies the retained sparse modes nor claims that a coarse
coordinate error can supply the complete regular inverse.
