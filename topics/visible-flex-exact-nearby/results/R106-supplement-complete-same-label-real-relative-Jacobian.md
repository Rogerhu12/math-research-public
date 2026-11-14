# R106 supplement: the complete real relative Jacobian, keeping the common label

For the same actual fixed-type object, the same whole parameter interval
\(p_5\pm10^{-9}\), and every pair of physical times on the complete
negative-curvature forward leg, the actual relative characteristic map
\(H\) and its inverse satisfy

\[
\boxed{\quad 0.06673940192<H'(\theta)<14.983652402.\quad}       \tag{J.1}
\]

This is a complete real-angle, real-time and whole-parameter bound. It
replaces the previous sufficient real upper bound \(36.730914\) when a
consumer needs the real Jacobian of an actual relative map. It does not
change the paid complex strip or the complex modulus. Those remain the
old R106 quantities and must still be used for higher-derivative Cauchy
estimates unless separately improved.

The computation uses the complete original finite Fourier/Bernstein
reference and its already certified retarget errors. It adds the complete
true-flow Jacobian error before forming any ratio. The finite retarget
function called \(Q\) is never identified with a true Jacobian.

## 1. Why the same label is needed

R106 writes the complete actual ray as

\[
\Theta(\tau,x,p)=Y(\tau,X_p(\tau,x),p_5),\qquad
\Theta(-\pi/2,x,p)=H_5(x)/4.
\]

Here \(x\) is a normalized initial label of period \(2\pi\), and
\(\Theta\) is a physical angle of period \(\pi/2\). The finite reference
\(Y\) is fixed as the real parameter varies. The completed integrated
source refinement proves, on the full real time interval and the full
complex label strip \(1/1024\),

\[
|\Theta_x(\tau,x,p)-Y_x(\tau,x)|\le\epsilon_J,
\quad
\epsilon_J=\frac{655848592}{254021484375}
 <0.002581862687.                                          \tag{J.2}
\]

Both factors in the derivative of a relative map are evaluated at the same
initial label:

\[
\bigl(\Theta_{\tau_1}\circ\Theta_{\tau_0}^{-1}\bigr)'
   (\Theta_{\tau_0}(x))
 =\frac{\Theta_x(\tau_1,x)}{\Theta_x(\tau_0,x)}.             \tag{J.3}
\]

The normalized-label-to-physical-angle factor cancels exactly. Replacing
the numerator and denominator by unrelated global extrema discards this
common-label information. The present consumer retains it on every
closed angular cell while covering all times. Because both time orders
are included, the same bound applies to the inverse map.

The radial rewriting \(r=t(p)\sin\tau\) is independent of the angular
label. Thus (J.3) covers every relative radial map in the complete strict
interval \([-r_c,r_c]\), uniformly for the whole real parameter interval.
The other actual characteristic branch follows from the exact angular
reflection already proved for this fixed-type family. This assertion
does not use R101's final conjugacy as an intermediate-time flow.

## 2. Complete reference controls on closed real angular cells

The immutable reference consists of all 550 time segments. On each segment
the original field is

\[
Y_4(\tau,x)=x/4+\sum_{j=0}^7 B_j(\tau)U_j(x),
\]

where the degree-seven Bernstein weights are nonnegative and sum to one
for every real time in that segment. Each \(U_j\) is the complete stored
finite Fourier polynomial with exact binary64 dyadic coefficients. Both
positive and negative Fourier modes are kept, with their exact real
conjugacy.

Use \(N_\theta=4096\) centers \(x_n=2\pi n/N_\theta\) and the closed
cells \(|x-x_n|\le\pi/N_\theta\), taken modulo the circle. For a fixed
control put

\[
q_j(x)=\tfrac14+U_j'(x),\qquad
\delta_j=\frac\pi{N_\theta}
                  \sum_{k\ge1}2k^2|\widehat U_j(k)|.         \tag{J.4}
\]

The full finite Fourier inequality
\(|e^{ik(x-x_n)}-1|\le |k||x-x_n|\) proves

\[
q_j(x_n)-\delta_j\le q_j(x)\le q_j(x_n)+\delta_j             \tag{J.5}
\]

throughout the closed cell. A directed Arb native inverse DFT encloses
every \(q_j(x_n)\). The grid strictly exceeds twice the full Fourier
degree, so no finite alias is introduced. The coefficients, the DFT,
\(\pi/N_\theta\) and the full sum in (J.4) are all evaluated with
outward arithmetic. No ordinary floating FFT value is used in the proof.

For every segment and every Bernstein control, the existing complete
reference derivative gate separately supplies the full retarget \(C^1\)
fee \(e_j\). It includes the complete symbolic product \(Q_j a\), not a
Fourier truncation of that product. The bound is already paid on the
wider label strip \(1/512\), so restriction to the real cell is valid.

Consequently, for every parameter in the stated box and every time in
that segment, (J.2) and Bernstein convexity give, on cell \(n\),

\[
\begin{split}
\Theta_x(\tau,x,p)&\ge
 \min_j\{\underline q_j(x_n)-\delta_j-e_j-\epsilon_J\},\\
\Theta_x(\tau,x,p)&\le
 \max_j\{\overline q_j(x_n)+\delta_j+e_j+\epsilon_J\}.
\end{split}                                                \tag{J.6}
\]

The program then takes these minima and maxima over all 550 time
segments, separately for each closed angular cell. Call the resulting
numbers \(l_n,u_n\). Every \(l_n\) is strictly positive. Therefore

\[
 C_{\rm real}=\max_n\frac{u_n}{l_n}                         \tag{J.7}
\]

is a full same-label bound for (J.3) and its reciprocal. There is no
discrete-time sampling in (J.6), and the closed-cell variation in (J.4)
pays the entire angular circle.

## 3. Actual completed output and scope

The computation used 192-bit Arb arithmetic and took 253.57 seconds.
All 550 segments, all eight real-time controls on each segment, all
4096 closed angular cells, and all 549 exact reference seams passed.
The directed output is

\[
\begin{split}
C_{\rm real}&<14.983652401472606,\\
C_{\rm real}^{-1}&>0.0667394019299139.
\end{split}
\]

The largest complete cell fee, including (J.2), is less than
\(0.016242204100\). The common true label derivative lower bound from
these deliberately coarse first-order cells is greater than
\(0.014096083930\). The ratio is maximized by cell 3400, whose saved
directed endpoints enclose a lower bound greater than
\(0.0146807131055\) and an upper bound less than
\(0.219970702179\). The global independent upper/lower ratio of these
new cell bounds would be worse; it is not the quantity used in (J.7).

For clarity, the proof gives three different kinds of information:

| Quantity | Valid domain and use |
|---|---|
| New \(C_{\rm real}\) and its reciprocal | All real angles and all pairs of real times; change of variables and top derivative coefficients |
| Old complex relative derivative modulus \(C_J<36.730914\) | The unchanged paid complex strip; analytic Cauchy derivatives |
| Old normalized relative-flow strip \(2.7952875\,10^{-5}\) | The unchanged whole complex domain |

One must not insert \(C_{\rm real}\) as a bound for the complex derivative.
The later exact density-transport consumer uses the new real number only
where (J.1) authorizes it and retains the old complex number in all higher
Cauchy derivatives.

## 4. Reproducibility and immutable inputs

The source is
`scripts/fourfold_true_relative_ray_jacobian_cells.py` and the full output is
`notes/2026-11-13-R106-complete-relative-real-Jacobian.json.gz`.
The report SHA256 is

    43e5d0854f0510eea5c035446a56a33ca8a80b1307dd3b2c67e66733702c370b

The source verifies the original complete derivative report and its
producer/dependencies, the reference summary's exact report SHA, the
original manifest and retarget descriptor, the same actual object and
parameter family, every read base coefficient shard, every exact time
row, and each exact shared reference seam. It consumes the already
proved complete retarget control fees and the exact rational true-flow
error (J.2). The output records every input SHA, each segment's complete
accepted bounds and the digest of the final cell endpoints.

Only the original finite reference coefficients need to be present. The
existing forward-reference recovery reconstructs those exact canonical
paths and verifies their historical hashes. No raw ODE or native
geometric calculation is repeated by this consumer.

From the topic directory, choose a new output path:

~~~bash
python3 scripts/fourfold_true_relative_ray_jacobian_cells.py \
  --nodes 4096 --bits 192 \
  --out notes/R106-complete-relative-real-Jacobian-reproduced.json.gz
~~~

This proves a new actual relative-flow input. It does not compute the
returned nonmean subprincipal phase, an Airy contact map, a full returned
strong remainder, or the final inverse. In particular the principal
circle return and the full two-row PDE return remain distinct objects.
