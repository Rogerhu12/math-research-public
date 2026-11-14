# Actual all213 Cs+Lambda quadratic-derivative frequency windows

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## 1. Same field, norms and delivered operator

This certificate consumes the completed all213 canonical auxiliary
bootstrap after its same-field physical transfer, SHA
0816e8e7d62bb5df1df58848dfe8ab1c9a3699210f5df9b9da7e5e31e6a18d93.
Its centre is the same R100 field C=Cs+Lambda d on the six original
product axes and the forty transverse axes with shared l1 radius1/32.
All 46 actual low-mode caps and the original continuous strip are kept.
The local physical normalization is V'=257/256 times Vs, with strong
pair variables (B p,kappa). This statement does not change the metric,
auxiliary family, parameter axes, radial envelope or mean branch.

For each original cell12 through224, the result gives two positive
13 by15 matrices. The output windows are

    94; 96; 98..104; 106..112; 114..128; 130..184; 186..192;
    194..256; 258..512; 514..1024; 1026..2048; 2050..4096; 4098..8190.

The input windows are 2..92, those thirteen windows, and8192..infinity.
Every endpoint is an even frequency. There are no gaps in either
specified cover.

If q_j is a shared strong Fourier pair mass of the input perturbation
in window j, each output-window weak source mass obeys

\[
 S_{w,s}\le\sum_j\Gamma_{w,j,s}q_j,\qquad
 S_{w,\ell}\le\sum_j\Gamma_{w,j,\ell}q_j.       \tag{1}
\]

The physical materials are the original
\(s(V'/w)^2\) and \(|\ell|(V'/w)^2\). The matrices contain only the
dimensionless coefficients of DQ. They do not contain a new Green
operator, an output strong factor1+m, an extra radial frame cost or a
new envelope-rescaling factor. Those belong to the original consumers.

Here q_j bounds the sum of all input pair masses in that entire
window. It is not a common cap that can be assigned independently to
every input frequency and then summed. The output is likewise the
total weak source mass in its window, not a maximum of individual
output coefficients.

## 2. Pair coefficients and both materials

The exact signed derivative is R106(A16). Its reflection convention is
odd P and even K, equally valid for complex reflected parameters. A
real sine or cosine amplitude has two signed Fourier half amplitudes.
The factor2 in DQ cancels the product's half-amplitude when a positive
sum or difference pair is collected. Thus no further factor2 is
inserted or removed below. The same convention is discussed in
R106 section4 and R116 section4.1.

For centre frequency k and perturbation frequency n, the absolute
s-material coefficients of the four component products, after the
physical B normalization, are bounded by

\[
 E/B^2,\quad En/B,\quad Ek/B,\quad Ekn.
\]

For the ell material, the corresponding coefficients are bounded by

\[
 (Ekn+w^2)/B^2,\quad Ek/B,\quad En/B,\quad1.
\]

These bounds hold for both the sum and difference output; their signs
may differ but their absolute bounds do not. The original real-head
background domain of R23/R106 has E<=5/4 and w^2<=1/4. Taking the
maximum of the four coefficients is valid against the product of the
two combined component masses. One does not sum four independently
spent copies of that mass.

Let B0 be the integer floor of the original certified B lower endpoint
in this cell. Since B>=B0>=120 and k,n>=2, the resulting coefficients
relative to two strong pair masses are

\[
 \beta_s(k,n)=\frac{5kn}{4(1+k)(1+n)},
\]

\[
 \beta_\ell(k,n)=
 \frac{\max\{1,5k/(4B_0),5n/(4B_0),(5kn+1)/(4B_0^2)\}}
 {(1+k)(1+n)}.                                \tag{2}
\]

All centre frequencies satisfy k<=92. The actual producer checks
5k<=4B0 and 5n(B0-k)>=1 for every relevant n through the sufficient
integer inequalities at k=92,n=2. Hence the numerator in the second
formula reduces exactly to

\[
 \max\{1,5n/(4B_0)\}.                         \tag{3}
\]

This is an algebraic simplification of the prescribed upper coefficient,
not a smaller unproved model of the nonlinear equation.

## 3. Frequency support and the original varying strip

Let c_k be the saved strong pair cap of the actual Cs+Lambda centre
on this cell. At any radial point its width is the original tau(r).
Collecting a sum output gives no loss of angular weight. Collecting a
difference output gives the exact factor exp[-2min(k,n)tau(r)]. The
original density certificate, SHA e640e3e..., supplies a lower bound
tau_outer for tau(r) on the whole cell. Thus the coefficient for an
input frequency n into output window W is bounded by

\[
 \sum_{k=2,4,\ldots,92}c_k\beta(k,n)
 \left(1_{k+n\in W}
 +e^{-2\min(k,n)\tau_{\rm outer}}1_{|k-n|\in W}\right).    \tag{4}
\]

The output windows all start at94. If n<=92, no difference frequency
can enter them. If n>=94, every centre frequency is smaller than n,
so the difference weight in (4) is exactly bounded by the fixed
cell factor exp(-2k tau_outer). This keeps the suppression of
opposite-frequency interactions. It never borrows an outer-field
strip cap for the inner auxiliary object.

For a finite output with maximum8190 and k<=92, an input n>8282 has
neither a sum nor a difference output in any listed window. The
infinite input window therefore has a finite nonzero contribution
range8192..8282. Its entire mass remains one input variable in (1).
This exact support fact does not set the infinite field itself or
its other nonlinear interactions to zero.

## 4. Exact maximization over every input frequency

For each output/input pair, partition the even input frequencies at
every membership boundary of k+n and n-k. The producer saves all
1,806 resulting intervals. Their coverage, even endpoints and
unchanged membership at both ends are checked exactly. Beyond the
finite support cutoff, the coefficient is exactly zero.

Within one membership interval, define the two positive sums

\[
 A=\sum_{k\ {m selected}}\frac{k c_k}{1+k}\,\omega_k,
 \qquad
 B=\sum_{k\ {m selected}}\frac{c_k}{1+k}\,\omega_k,
\]

where omega is1 on a selected sum and exp(-2k tau_outer) on a selected
difference; a k selected in both branches contributes to both. The
coefficients in (4) are then

\[
 \frac{5n}{4(1+n)}A,
 \qquad
 \frac{\max\{1,5n/(4B_0)\}}{1+n}B.             \tag{5}
\]

The first is increasing in n. With t=1/(1+n), the second is
\(B\max\{t,5(1-t)/(4B_0)\}\), a convex function of t. The maximum
of each expression on the interval is therefore attained at an
endpoint. Evaluating both endpoints proves the maximum over every
even input frequency, rather than merely checking a sample.

All interval sums are formed by adding positive terms. No large
prefix total is subtracted from another total to recover a tiny
frequency tail. Arbitrarily small positive source modes and
exponential factors are retained by Arb and rounded upward to
160 significant dyadic bits. Exact support zeros are kept as zeros.
The primary records a maximizing candidate frequency separately for
each material and each output/input entry.

The maximum over input frequency in (4), multiplied by the one shared
input mass, proves (1) by positivity. There is no mode-count multiplier.
Summing the already valid individual centre caps is conservative even
though the forty transverse parameter axes also share a smaller
common budget; this does not claim that the sum of their full-radius
caps equals their true common mass.

## 5. Actual result and consumer boundary

The complete primary has213 rows, each with two13 by15 matrices, and
retains all46 centre modes. It passed44,125 identity, integer-support,
positivity or outward-rounding gates. The owned execution formally
exited0 after38.511866448 seconds, peak54,828 KiB, below the96 MiB
guard. No radial integration, ODE, Node or Green call occurred.

Primary SHA:
bb4c7036f45d23a33cfe7f8dbeb4ccb142ffab22c91b62b0162de9c628dc9772.
Its compressed size is1,408,692 bytes. Source SHA:
ecd091b4400b21d66dcc78b0933fe09689ae65473d287f0b119f8782a5e1b673.
The resource SHA is
b135d973ba2b8ce6de4d66ae81df571144c9a0b4cb633254a6bcc25b6881d896.

For example, in cell12 the s-material low-window-to94 coefficient
is about0.001408854226, while low-window-to96 is only7.95e-11.
The94-to96 and96-to94 coefficients are about0.001409176618 and
0.000790951660. The94-to94 DQ coefficient is exactly zero because
the centre has no zero frequency. These displays are not substituted
for the exact upward dyadics.

The existing whole-field auxiliary correction, low and far terms,
the complete Q of the unknown field, the full mean and inverse
remainder T, the infinite-band feedback and the true endpoint
readout remain the responsibility of the same-field finite
consumer. These source matrices alone prove neither a contraction,
the cut equation nor a closed surface.
