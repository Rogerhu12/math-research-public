# R106 supplement: complete real relative-ray jets and the same density phase budget

**Proved for every real angle, every original parameter in the full affine
box, and every pair of times of the original complete forward leg.**
The original 550 Fourier/Bernstein segments and all 4,400 controls give
higher **real** derivatives of the actual relative characteristic and
its inverse. Exact radial reflection supplies the other branch.

The new bounds include

$$
\|H''\|_\infty<123831.016,\qquad
\|H'''\|_\infty<3163445102.81,\qquad
\|H^{(4)}\|_\infty<184419183252454.                         \tag{J.1}
$$

They hold for \(H=H_{t,s}\) with **arbitrary interior times** \(s,t\),
including either orientation. They are not only endpoint bounds.
The full consumer pays every derivative through order twelve.
It leaves all previously paid complex widths and complex moduli unchanged.

The direct consequence for
[the actual high first phase](R46-supplement-actual-high-density-first-phase-and-two-order-remainder.md)
at the same \(N=2^{20}\) is

$$
\|R_H\|_{H_N^0\to H_N^2}<3190477.614,\qquad
\|R_H\|_{H_N^{-2}\to H_N^0}<56.564759 .                    \tag{J.2}
$$

The preceding bounds for these same two windows were
\(1.183021\,10^{10}\) and \(164.024500\).
All low histories, means, ordinary-source columns and physical reconstruction
positions remain as in the original high density theorem.
This is a reduction of explicit interior constants, not a closure of the
finite head or the returned operator.

## 1. The exact original absolute ray coordinates

Let \(Y_t(x)\) be the complete actual physical angle, parametrized by the
normalized original label \(x\), of period \(2\pi\).
Thus \(Y_t(x+2\pi)=Y_t(x)+\pi/2\). Define

$$
F_t(x)=4Y_t(x),\qquad
F_t(x+2\pi)=F_t(x)+2\pi .                                 \tag{J.3}
$$

The actual normalized relative characteristic is exactly

$$
H_{t,s}=F_t\circ F_s^{-1},\qquad F_t=H_{t,s}\circ F_s .
                                                               \tag{J.4}
$$

The fixed strict radial cuts correspond to times within the same
complete forward leg. At a fixed parameter their conversion to the
original time variable is independent of the angle. Thus (J.4) applies
to every pair of strict radial times without an extra angular chain rule.

The previously proved same-label real ratio certificate supplies

$$
C_r^{-1}\le H_{t,s}'\le C_r,\qquad C_r<14.983653,            \tag{J.5}
$$

uniformly in both \(s,t\). The integrated true-ray certificate separately
supplies the genuine absolute lower bound

$$
Y_t'\ge {223623\over7812500}=0.028623744 .
$$

Consequently the consumer uses a positive lower bound
\(m\le F_s'\), taking the better of this bound times four and the
independent closed-cell real lower bound.
For the absolute first-derivative upper bound it takes the better of
the two independently paid upper bounds, also multiplied by four.
It does not confuse the relative first-derivative constant \(C_r\)
with an absolute derivative or a complex constant.

## 2. Every Fourier coefficient, retarget correction and true-ray error

On each original segment the base finite reference is exactly

$$
Y^{\rm base}_t(x)=x/4+
 \sum_{c=0}^7 b_c(t)
 \sum_{|n|\le d}u_{c,n}e^{inx},
\qquad b_c(t)\ge0,\quad\sum_cb_c(t)=1.                    \tag{J.6}
$$

The \(u_{c,n}\) are the exact saved binary64 dyadics, with their exact
reality symmetry and genuine continuous seams.
The consumer checks every original shard hash and byte count,
its Fourier degree and array shape, all exact time endpoints, all
eight controls, and every one of the 549 seams.

For each control \(c\), the already proved symbolic retarget correction
has derivative modulus at most \(\epsilon_c\) on width \(s_f=1/512\).
The complete actual-ray comparison has

$$
|Y_t'-q_t^{\rm retarget}|\le
\epsilon={655848592\over254021484375}
\quad\hbox{on width }s_r=1/1024.                         \tag{J.7}
$$

Here \(q_t^{\rm retarget}\) is the derivative of the full retarget
reference; it is not asserted to be the true Jacobian.
Both the retarget fee and (J.7) are included before any higher derivative
is bounded.

For \(j\ge2\), define on each control

$$
M_{j,c}
=8\sum_{n=1}^d n^j|u_{c,n}|
 +4(j-1)!
 \left({\epsilon_c\over s_f^{j-1}}
       +{\epsilon\over s_r^{j-1}}\right).                \tag{J.8}
$$

The factor eight in the finite term is the exact factor four from
\(F=4Y\) times the two conjugate Fourier sides. The last two terms
also carry the exact factor four.
Cauchy's estimate is applied to the already paid **derivative** errors,
so its factorial is \((j-1)!\), not \(j!\).
Bernstein positivity then gives

$$
\sup_{t,x}|F_t^{(j)}(x)|\le M_j:=\max_{\text{all 4,400 controls}}M_{j,c}.
                                                               \tag{J.9}
$$

This covers the continuous time interval of every segment; it is not
an evaluation at its endpoints or a time sampling test.

The finite coefficient modulus in the implementation is the directed
rectangle bound \(|\Re u|+|\Im u|\).
Every frequency power is formed by outward-rounded interval
multiplication, and every positive coefficient sum uses the existing
directed pairwise Box reduction.
Thus neither a floating Fourier magnitude nor an unverified reduction
is used as a rigorous upper bound.
The finite errors and complete infinite true-ray correction are retained
separately in (J.8).

The producer verifies the exact original object, exact center parameter,
whole half-width, complete reference gate and summary, and the true-ray
producer and its own frozen input hashes. No part of the newer nonlinear
Codazzi branch or a changed outer profile is substituted into these
original ray constants.

## 3. Divide the full Bell identity before estimating it

Differentiating \(F_t=H_{t,s}\circ F_s\) gives

$$
F_t^{(j)}
=\sum_{k=1}^j H_{t,s}^{(k)}(F_s)
 B_{j,k}(F_s',F_s'',\ldots,F_s^{(j-k+1)}).                \tag{J.10}
$$

The coefficient of \(H^{(j)}\) is exactly \((F_s')^j\).
The useful estimate divides **each Bell monomial** by this actual
positive coefficient first.
Every monomial in \(B_{j,k}\) has weighted degree \(j\).
Set

$$
x_1=1,\qquad x_\ell={M_\ell\over m^\ell}\quad(\ell\ge2).
$$

Then, pointwise and for all pairs \(s,t\),

$$
{|B_{j,k}(F_s',F_s'',\ldots)|\over(F_s')^j}
\le B_{j,k}(1,x_2,x_3,\ldots).                            \tag{J.11}
$$

The first variable is exactly one because its powers cancel before
bounding. In particular no unnecessary power of
\(\sup F_s'/\inf F_s'\) is inserted.

Start with \(h_1=C_r\). For \(j\ge2\), the complete inductive bound is

$$
\widehat h_j={M_j\over m^j}
 +\sum_{k=1}^{j-1}h_kB_{j,k}(1,x_2,x_3,\ldots),
$$

$$
h_j=\min\left\{
 \widehat h_j,\ {(j-1)!C_c\over(X/2)^{j-1}}
\right\}.                                                \tag{J.12}
$$

The second bound is the independently proved original complex Cauchy
bound, with unchanged \(C_c\) and \(X\).
Either valid upper bound can be used at the next induction level;
taking their minimum does not require a common extremizer.
In this native run the new bound improves every level from two
through twelve.

For example, the first three inequalities before taking this minimum are

$$
\widehat h_2={(1+C_r)M_2\over m^2},
$$

$$
\widehat h_3={(1+C_r)M_3\over m^3}
              +{3h_2M_2\over m^2},
$$

$$
\widehat h_4={(1+C_r)M_4\over m^4}
 +{6h_3M_2\over m^2}
 +h_2\left({4M_3\over m^3}+{3M_2^2\over m^4}\right).       \tag{J.13}
$$

These identities explain why the relative bound is considerably
better than multiplying two coarse independent composition norms.
They also show explicitly that the entering time is arbitrary.
Interchanging \(s,t\) proves exactly the same estimates for the inverse.
The existing exact reflection gives both physical characteristic branches.

## 4. Reusing the same complete real Sobolev estimates

Only the real derivative list in the original finite Bell matrices
is changed. For a fixed \(N\), use \(h_1,\ldots,h_{j+1}\) in

$$
\mathsf P_{ab}=N^{b-a}B_{a,b}(h_1,h_2,\ldots),
$$

$$
\mathsf D_{ab}=
\begin{cases}
C_r^a,&a=b,\\
C_rN^{b-a}B_{a+1,b+1}(h_1,h_2,\ldots),&b<a.
\end{cases}                                               \tag{J.14}
$$

After the same binomial-weighted finite matrix norm,
multiply by the same real \(L^2\) Jacobian factor \(\sqrt{C_r}\).
This gives the same scalar bounds \(p_j\) and density bounds \(d_j\)
on \(H_N^j\), with smaller numerical values.

For the cross-branch material derivative, replace the three real
Jacobian moduli by \((C_r,h_2,h_3)\), and the logarithmic derivative
moduli by

$$
(C_rh_2,\quad C_rh_3+C_r^2h_2^2,\quad
 C_rh_4+3C_r^2h_3h_2+2C_r^3h_2^3).                        \tag{J.15}
$$

Everything else is read from the exact frozen first-phase report:
the full \(\kappa=\mathcal F/\mu\) integral, the full
\(R=a\mathcal F/\mu^2\) modulus, the entire material derivative
\(Q_\sigma\), the true physical source \(mf\), and the actual
nonzero-head and two-mean interfaces.

The endpoint and integral bounds (P.16)--(P.21) then apply unchanged.
In particular the forward and opposite windows still use their
different factor orders; the cheaper adjoint estimate is not inserted
in the forward window.
The new native obtains:

| \(N\) | Complete \(0\to2\) remainder | Complete \(-2\to0\) remainder |
|---:|---:|---:|
| \(2^{20}\) | \(3190477.614\) | \(56.564759\) |
| \(2^{30}\) | \(1.815979\) | \(3.602187\,10^{-5}\) |
| \(2^{40}\) | \(1.730798\,10^{-6}\) | \(3.433803\,10^{-11}\) |

The report also records the full base norm, both interpolated
\(4/3\)-order windows, the updated order-one and order-two high
Volterra gains, and both windows of the ordinary-source and
low-height error columns. The complete sources are exactly those
of (P.23)--(P.25); their projectors and both scalar means are unchanged.

None of these real \(H_N^j\) estimates grants a positive fixed
angular weight, a wider complex flow, or a stronger complex inverse
derivative. Such uses would require separate payment.

## 5. Reproduction and remaining interface

The producer is scripts/fourfold_actual_relative_ray_real_jets.py.
The report is notes/2026-11-13-R106-full-relative-real-ray-jets.json.gz.

~~~bash
python3 scripts/fourfold_actual_relative_ray_real_jets.py \
  --out notes/2026-11-13-R106-full-relative-real-ray-jets.json.gz
~~~

It requires the already restored exact original Fourier shards.
It does not run the original numerical forward integration, change a
reference, or recompute any of the 215 native operator leaves.
The report includes all 550 continuous segment bounds, the winning
control for each derivative, each exact input hash, the complete
relative Bell recurrence through order twelve, and all numerical
density consequences stated here.

The real high block still has its full low-history drive. To obtain
a new returned strong remainder, its low time problem, the physical
root/cap port maps and final circle reconstruction must be joined with
these same projectors and source units. No assertion of that further
closure is part of the present derivative certificate.

