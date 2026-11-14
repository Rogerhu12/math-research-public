# R119 supplement: paying the complete radial transversality cost from the actual middle angular width

2026-11-14, visible-exact / root. **Proved; 21 new exact rational gates passed.**

The complete lower bound for a compensated radial Wronskian derivative,
including its very large layer-dependent constants, now fits inside the
already fixed middle-frequency angular budget. No low-frequency radial
weight is changed.

This conclusion concerns the actual single-mode transversality bound.
It does not yet choose one profile for several modes, estimate a
finite-parameter bad set, or invert the coupled nonradial middle matrix.

## 1. The two inputs concern the same controlled family

The [compact C4 control theorem](R119-supplement-quantitative-phase-preserving-compact-control.md),
blob \(\mathtt{5662bf40391a53a2212311406cf7ad63064908fc}\),
gives, at each true radial resonance and for fixed actual unit Robin
lines, a real compact metric direction of sum \(C_x^4\) norm at most one.
Its two first phase integrals vanish exactly; the actual two-bump
compensation keeps both phases fixed, with zero first derivative.
For the actual normalized Wronskian it proves
\[
 |\Delta_m'(0)|\ge D_{j,M},\qquad M=|m|,
\]
\[
 D_{j,M}
 =2^{-2^{27}}\delta^{285554}(j+5)^{-144890}M^{-19966}
   \exp\{-2^{74}(j+5)-2^{71}M\delta^{3/4}\sqrt{j+5}\}.
                                                               \tag{W.1}
\]
The original material factor \(dt=a\,dx\), the true left wave
normalization, and the right resonant amplitude have already been
included in this expression.

The [complete controlled-profile chart](R119-supplement-controlled-profile-full-label-and-raw-ports.md),
blob \(\mathtt{f11edbccd752bf034aa40e71888859d667a04b42}\),
reinstantiates the actual low/middle boundary for this family:
\[
 \delta=\delta_j=\frac2{25}\,2^{-j},\qquad j\ge8193,
 \qquad
 \widehat M_j=2^{-40}\delta^{-1/8}.                     \tag{W.2}
\]
Its original angular width is
\[
                              h_j=8\delta^{1/256}.     \tag{W.3}
\]
The result below applies throughout \(M\ge\widehat M_j\), with no
upper-frequency restriction. The actual fourfold modes form a subset
of that domain. The threshold is not replaced by a merely asymptotic
power of \(\delta\).

## 2. Statement with the full constants

For every \(j,M\) in (W.2),
\[
 \boxed{\quad
       -\log D_{j,M}
          <2^{-800}M\delta^{1/256}
           =2^{-803}Mh_j .
       \quad}                                           \tag{W.4}
\]
Consequently the actual direction furnished by the input theorem satisfies
\[
                       |\Delta_m'(0)|
                         >e^{-2^{-803}Mh_j}.             \tag{W.5}
\]
Equation (W.4) includes all powers of \(\delta\), \(j+5\), and \(M\),
the constant \(2^{27}\log2\), and both exponential terms in (W.1).
In particular the layer-only exponential has not been renamed a
harmless constant and applied to low-frequency sources.

## 3. A uniform elementary bound for the layer factor

Write
\[
 J=j+5,\qquad x=\log_2(\delta^{-1}).
\]
Since \(8<25/2<16\),
\[
                           j+3<x<j+4<J .                \tag{W.6}
\]
The following bound holds for every integer \(j\ge8193\):
\[
                              J<2^{j/512}.              \tag{W.7}
\]
At the first layer, \(J=8198<2^{14}<2^{8193/512}\).
For the induction step, the binomial expansion and
\(\binom{512}{q}\le512^q\) give
\[
 (1+1/J)^{512}
 \le\sum_{q=0}^{512}(512/J)^q
 <\frac1{1-512/J}\le\frac{8198}{7686}<2 .
\]
Thus \(J+1<2^{1/512}J\), which advances (W.7) by one layer.
This argument proves the entire unbounded layer range; no finite
table of sample layers is used.

## 4. Dividing the full cost by the true frequency

Let
\[
                         L=-\log D_{j,M}.
\]
Taking the logarithm of the full expression (W.1) yields exactly
\[
\begin{split}
 L={}&2^{27}\log2+285554\,x\log2+144890\log J
       +19966\log M\\
    &+2^{74}J+2^{71}M\delta^{3/4}\sqrt J.                \tag{W.8}
\end{split}
\]
Use \(\log2<1\), \(\log J<J\), and (W.6). Since
\(2^{27}<2^{14}J\), \(285554<2^{19}\), and \(144890<2^{18}\),
all terms in the first line except the frequency logarithm,
together with \(2^{74}J\), have sum less than
\[
             (2^{74}+2^{19}+2^{18}+2^{14})J<2^{75}J .
                                                               \tag{W.9}
\]

Put \(M_0=2^{-40}\delta^{-1/8}\).
The true threshold obeys
\[
 \log_2 M_0=-40+x/8>-40+(8193+3)/8>2,
\]
so \(M_0>e\). The function \((\log M)/M\) is decreasing for
\(M\ge M_0\). Also
\[
             \log M_0=(-40+x/8)\log2<J/8.
\]
It follows that
\[
 \frac{19966\log M}{M}
 \le\frac{19966\log M_0}{M_0}
 <2^{52}J\delta^{1/8}.                                 \tag{W.10}
\]
The layer-only part (W.9), divided by \(M\ge M_0\), is less
than \(2^{115}J\delta^{1/8}\).
Combining both bounds, using \(2^{115}+2^{52}<2^{116}\), gives
\[
 \frac LM
 <2^{116}J\delta^{1/8}
             +2^{71}\delta^{3/4}\sqrt J .               \tag{W.11}
\]
The first term is precisely where the actual moving-middle lower
frequency pays the otherwise enormous layer-only cost. Nothing
in this calculation applies below that threshold.

## 5. Comparing with the unchanged angular width

Divide (W.11) by \(\delta^{1/256}\).
Since \(\delta<2^{-j}\), (W.7) gives
\[
 2^{116}J\delta^{1/8-1/256}
           <2^{116-61j/512},\qquad
 2^{71}\sqrt J\,\delta^{3/4-1/256}
           <2^{71-763j/1024}.                          \tag{W.12}
\]
Both exponents decrease strictly with \(j\).
At the very first layer the exact integer inequalities are
\[
 61\cdot8193>(116+801)\cdot512,\qquad
 763\cdot8193>(71+801)\cdot1024 .
\]
Hence each term in (W.12) is less than \(2^{-801}\).
Their sum is less than \(2^{-800}\), proving (W.4).
The factor 8 in the original \(h_j\), rather than a newly chosen
angular width, gives the exact \(2^{-803}\) in (W.5).

## 6. Meaning for the remaining common-parameter problem

The very small fraction in (W.4) is a real reserve for subsequent
estimates. It does not by itself pay unspecified second derivatives,
parameter-volume factors, interval-localization fees, determinant
multiplicities, or infinitely many frequency constraints.
Each of those must be stated and charged when introduced.

In particular:

* The direction in (W.5) can depend on the resonant frequency and
  its actual radial solution. It is not yet one common perturbation.
* A lower bound at a resonant point alone gives neither a finite
  interval on which the derivative stays nonzero nor a quantitative
  bad-set bound. Those require the actual compensated Hessian.
* The scalar radial Wronskian is not the determinant of the entire
  nonradial coupled system. Its original physical source columns,
  ordinary and weak sources, both total traces, independent mean,
  and positive-DN cross contacts remain to be consumed.
* The original \(\zeta_j\), \(h_j\), and low-frequency radial source
  weights remain exactly as before.

Thus the next use of (W.4) is in a quantitatively finite parameter
construction on the genuine middle domain, followed by the full
nonradial network. No permission is granted to multiply an entire
layer's old low source norm by \(D_{j,M}^{-1}\).

## 7. Actual arithmetic and reproduction

The complete calculation function in
[scripts/fourfold_middle_transversality_angular_width.mjs](../scripts/fourfold_middle_transversality_angular_width.mjs)
was executed in the available V8 runtime with normalized BigInt
rationals. Its 21 gates all passed. The proof above supplies the
elementary logarithmic monotonicity and layer induction; the
arithmetic checks retain every displayed numerical margin,
power, and conversion to the original width.

The complete execution report is
[notes/2026-11-14-R119-middle-transversality-angular-width-rational.json](../notes/2026-11-14-R119-middle-transversality-angular-width-rational.json).
It records the input proof identities, source SHA-256, exact
threshold and domain, and the explicitly unproved downstream
claims. No native numerical body solve or lost candidate
reconstruction is represented by these algebraic gates.
