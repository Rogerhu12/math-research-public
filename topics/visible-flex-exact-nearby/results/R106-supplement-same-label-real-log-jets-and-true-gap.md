# R106 supplement: same-label real log jets with the complete true first-jet gap

**Proved and run on the complete original reference.** Every relative
characteristic \(H_{t,s}=F_t\circ F_s^{-1}\), at every pair of real strict
times, every real angle and every parameter in the original box, obeys
\[
 \begin{split}
 |H_{t,s}'|,\ |(H_{t,s}^{-1})'|&<14.983653,\\
 |H_{t,s}''|&<31247.731109,\\
 |H_{t,s}'''|&<465239799.167,\\
 |H_{t,s}^{(4)}|&<13514609362131 .
 \end{split}                                               \tag{LJ.1}
\]
The second through fourth bounds improve the previous complete real
bounds by factors greater than \(3.9628802\), \(6.7996012\) and
\(13.6459129\), respectively. The first derivative bound is unchanged.

These are real derivative permissions. The old complete complex strip
and complex derivative modulus remain unchanged by this theorem.
No fixed-width operator difference of two bare pullbacks is inferred.

## 1. Exact original object and common label

Use the same 550-segment Fourier/Bernstein reference and the same true
retargeted characteristic family as in
[the full real-ray jet theorem](R106-supplement-full-relative-real-ray-jets-and-density-budget.md).
The original label has period \(2\pi\), and
\[
 F_t=4Y_t,\qquad F_t(y+2\pi)=F_t(y)+2\pi.
\]
All times use this same original label \(y\).
The real affine parameter box, the true solution, its retarget
descriptor, and every reference coefficient remain fixed.

The native calculation consumes all 23 original U/L shards, all 550
time segments and all eight Bernstein controls in each segment.
It checks their exact binary64 coefficient interpretation, all 549
exact seams, the complete original producer and input hashes, and the
entire actual parameter identity. The Fourier degree remains 516.

The input gate supplies the complete symbolic retarget C1 fee on
width \(s_f=1/512\). The whole-parameter true-Jacobian error has width
\(s_r=1/1024\) and bound
\[
 \varepsilon_J<0.002581862687.
\]
Neither error is dropped when higher derivatives are requested.

## 2. Complete closed angular cells

Take 4096 cells centered at \(y_l=2\pi l/4096\), of half width
\(h=\pi/4096\). For an exact control
\[
 Y_{\rm ref}(y)=y/4+\sum_{k\ne0}u_ke^{iky},
\]
the normalized \(j\)-th derivative, \(j=1,2,3,4\), has nonzero
coefficients \(4(ik)^ju_k\), and its mean is one for \(j=1\) and zero
otherwise. A directed Arb DFT encloses its value at each cell center.

The full finite Fourier variation on the cell is bounded by
\[
 V_j=8h\sum_{k=1}^{516}k^{j+1}|u_k|.
\]
For that control, with the original retarget C1 fee \(e_k\), add the
complete true derivative fee
\[
 E_j=V_j+
 4(j-1)!\left(e_k/s_f^{j-1}+\varepsilon_J/s_r^{j-1}\right).
                                                               \tag{LJ.2}
\]
Thus every closed-cell interval includes the entire finite polynomial,
the complete symbolic retarget correction, the whole-parameter true
ray error, and all frequencies in the already paid tails.

The first derivative is proved positive before any division.
For \(j=2,3,4\), enclose
\[
 M_j(t,y)=F_t^{(j)}(y)/F_t'(y)
\]
on each complete control cell. A Bernstein interpolation does not make
this ratio linear, but it preserves the ratio enclosure: if
\(v_k>0\), then
\[
 {\sum_k b_k u_k\over\sum_k b_k v_k}
  =\sum_k {b_kv_k\over\sum_\ell b_\ell v_\ell}\,{u_k\over v_k}.
\]
The coefficients on the right are nonnegative and sum to one.
The complete true derivative errors in (LJ.2) can first be distributed
among the control enclosures, so this argument applies to the actual
jet at every intermediate time, not only to the finite reference.

For each angular cell retain a full-time first-derivative range and
full-time intervals for \(M_2,M_3,M_4\). Their lower and upper
endpoints are saved; they are not only sampled diagnostic extrema.

## 3. Exact same-label divided-jet identities

Fix two arbitrary times \(s,t\), and write
\[
 v=F_s'(y),\quad h=H_{t,s}'(F_s(y))={F_t'(y)\over F_s'(y)},
 \qquad \Delta_j=M_j(t,y)-M_j(s,y).
\]
Repeated differentiation of \(F_t=H_{t,s}\circ F_s\), without
estimating its separate terms first, gives
\[
 H''={h\over v}\Delta_2,                                  \tag{LJ.3}
\]
\[
 H'''={h\over v^2}
       \left[\Delta_3-3M_2(s)\Delta_2\right],              \tag{LJ.4}
\]
\[
 H^{(4)}={h\over v^3}
 \left[\Delta_4-6M_2(s)\Delta_3+
       (15M_2(s)^2-4M_3(s))\Delta_2\right].                \tag{LJ.5}
\]
For example, differentiating
\(H''=h(M_2(t)-M_2(s))/v\), using
\(\partial_{F_s(y)}=v^{-1}\partial_y\), proves (LJ.4);
one further differentiation gives (LJ.5).

All differences in these formulas are taken at the same original
label. If a cell has \(F'\ge m\), relative first derivative at most
\(C\), \(|M_j|\le B_j\) and range width \(\Delta_j^*\), then
\[
 \begin{split}
 L_2&={C\over m}\Delta_2^*,\\
 L_3&={C\over m^2}(\Delta_3^*+3B_2\Delta_2^*),\\
 L_4&={C\over m^3}
  [\Delta_4^*+6B_2\Delta_3^*
       +(15B_2^2+4B_3)\Delta_2^*].
 \end{split}                                               \tag{LJ.6}
\]
These cover both time directions because the same full-time intervals
serve for both \(s\) and \(t\).

## 4. Necessary intersection with the already proved true gap

The raw closed-cell calculation was completed in 1044.9 seconds.
By itself it gave
\[
 H''<118968.010,\quad
 H'''<4.671293\,10^9,\quad
 H^{(4)}<3.259172\,10^{14}.
\]
The second derivative modestly improved the prior result, while the
third and fourth did not. Those raw bounds and all actual closed-cell
intervals remain in the first native report.

The same previously proved true-ray theorem gives the stronger
global normalized first-jet gap
\[
 F_t'\ge m_0=0.114494976
\]
at every real time, label and parameter. It also gives a complete
upper bound \(M_0\) and absolute normalized jets \(A_j\).
There is no reason to discard these independent true inequalities
when a wider Fourier-cell enclosure is available.

The second light consumer therefore sets, in each saved cell,
\[
 m=\max(m_{\rm cell},m_0),\quad
 M=\min(M_{\rm cell},M_0),\quad
 C=\min(C_r,M/m).
                                                               \tag{LJ.7}
\]
Before (LJ.6), intersect each ratio range with
\[
 -A_j/m\le M_j\le A_j/m.                                  \tag{LJ.8}
\]
All intervals remain nonempty. Positivity and the original complete
true gap precede these divisions.

There is also an independent exact divided-Bell estimate.
Set
\[
 J_j={\min(A_j,MB_j)\over m^j},\qquad j=2,3,4.
\]
Since the first divided Bell variable is one,
\[
 \begin{split}
 B_2^{\rm rel}&=(1+C)J_2,\\
 B_3^{\rm rel}&=(1+C)J_3+3h_2J_2,\\
 B_4^{\rm rel}&=(1+C)J_4+h_2(4J_3+3J_2^2)+6h_3J_2 .
 \end{split}                                               \tag{LJ.9}
\]
At each level take the minimum of (LJ.6), (LJ.9), and the already
proved original global bound, using the previously selected lower
jets \(h_2,h_3\) in the next line. Each candidate is a proved upper
bound for the same derivative, so their minimum is valid.

Taking the maximum over the 4096 cells gives the directed values
\[
 \begin{split}
 h_2&<31247.731108818,\\
 h_3&<465239799.166736,\\
 h_4&<13514609362130.236.
 \end{split}
\]
The worst cells are 3400, 3398 and 3398. This final intersection
reuses the saved complete intervals and performs no new Fourier
transform, field evaluation, geometric solve or true-ray integration.

## 5. Scope, downstream use and reproduction

The map \(F_s\) is a real circle diffeomorphism, so its image of all
original labels is the entire physical normalized circle. Equations
(LJ.3)--(LJ.9) therefore bound the relative map at every real point,
not only at labels used to start a particular trajectory. Exchanging
\(s,t\) gives its inverse. The exact reflection already used in the
original complete ray theorem supplies the other characteristic branch.

The full real first-jet, inverse and high derivative permissions now
have the same actual scope. Every old complex strip and complex
modulus is retained separately. Any later improvement of a complex
positive-real-part region must pay its own analytic remainder.

The first complete calculation is:

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_relative_ray_log_jets.py \
  --out notes/2026-11-13-R106-full-relative-real-log-jets.json.gz
~~~

The required true-gap intersection is:

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_relative_ray_log_jets_refine.py \
  --out notes/2026-11-13-R106-full-relative-real-log-jets-refined.json.gz
~~~

Both complete sources and both native reports are retained. The
second report is the one supplying the improved constants (LJ.1).
A consumer of the first report alone must retain its own, weaker
certified bounds; it cannot assume that the intersection was already
performed.

No projection, source, root mean, independent regular port or physical
reconstruction is modified by these improved real derivative bounds.
No full returned inverse is asserted.

