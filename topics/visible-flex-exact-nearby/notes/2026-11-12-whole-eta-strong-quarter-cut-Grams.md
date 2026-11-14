# Complete strong quarter-cut high-output Grams

This is a consumer contract for an **actually completed** output of
scripts/fourfold_phase_family_interface_fourier.py on the exact family
$\delta_5+[-10^{-9},10^{-9}]$. The center-only earlier quarter-cut report
is not an eligible input. The new consumer
scripts/fourfold_phase_interface_strong_grams.py has not executed while
the native environment is unavailable. No strong numerical Gram is claimed.

## Exact finite operator and every output frequency

Write the saved real-even finite multiplier as
$$
 P(\theta)=c_0+\sum_{k=1}^{K}c_k(e^{4ik\theta}+e^{-4ik\theta}),
 \qquad c_k\in\mathbb Q\text{ exactly dyadic}.
$$
The input is the full physical Fourier space $j=-N,\ldots,N$, including
the mean. For an output cutoff $L\ge N$ and an angular Sobolev order $s$,
the complete finite high-output operator is
$$
 (T_{P,L}u)_k=\boldsymbol 1_{|k|>L}
                 \sum_{j=-N}^{N}c_{|k-j|}u_j,
 \quad
 c_\ell=0\text{ for }\ell>K.
$$
Its output support is exactly within $-K-N,\ldots,K+N$. The finite Gram is
$$
 G_{P,L,s}(i,j)=
   \sum_{\substack{-K-N\le k\le K+N\\|k|>L}}
       (4|k|)^{2s}c_{|k-i|}c_{|k-j|}.                     \tag{1}
$$
Every output row in this range is included. No subsequent row truncation
is hidden in a scalar norm. The implementation uses $s=0,1/2,1,3/2$;
thus the exponent $2s$ in the Gram weights is an integer. Acb arithmetic
encloses the exact expression (1), including its numerical roundoff.

For the exact normalized cosine isometry $Q_c$ of R105, the cosine Gram
is $Q_c^*G_{P,L,s}Q_c$. This retains its mean column and all cross terms.
The body and boundary Hilbert spaces use the same normalized Fourier
measure and physical frequency $4k$ as the original core and cap data.

## Complete actual-minus-finite error

Let $E_s$ be the complete multiplier error already certified by the
whole-family producer:
$$
 \|(M_{f_\delta}-M_P)v\|_{H^s}\le E_s\|v\|_{H^s}
 \quad\text{for every }\delta\text{ in the same eta interval}.
$$
It includes parameter variation, true infinite primitive error, every
sample and DFT error, both Fourier aliases and the entire unretained tail.
It is not a bound only on a finite list of coefficients.

For the Euclidean low input norm and the convention that the zero mode
has weight one,
$$
 \|u\|_{H^s}\le \max(1,4N)^s\|u\|_2.
$$
Projection to the high output is contractive. Therefore
$$
 \|T_{f_\delta,L}-T_{P,L}\|\le
       \varepsilon_s:=\max(1,4N)^s E_s.                    \tag{2}
$$
The same bound holds after the exact isometric cosine input restriction.
There is no assumption that different mode or parameter errors are
independent.

Suppose $C\ge\|T_{P,L}\|$ and a selected dyadic Hermitian matrix
$\widehat G$ satisfies $\|G_{P,L,s}-\widehat G\|\le e_G$.
Then the complete Gram error satisfies
$$
 \boxed{\quad
 \|T_{f_\delta,L}^*T_{f_\delta,L}-\widehat G\|
       \le e_G+2C\varepsilon_s+\varepsilon_s^2 .
 \quad}                                                   \tag{3}
$$
This follows by expanding $(T+E)^*(T+E)$; each mixed operator term has
norm at most $C\varepsilon_s$. Thus both Hermitian Loewner inequalities
are paid, not only an upper estimate on selected diagonal entries.
The consumer also saves the scalar operator bound $C+\varepsilon_s$.

## Fields and strong output spaces

The complete family package has five fields. The consumer records:

| actual multiplier | high output spaces |
|---|---|
| $Y$ | $H^1$, $H^{3/2}$ |
| $Y^{-1}$ | $H^1$, $H^{3/2}$ |
| $p_Y$ | $H^0$, $H^{1/2}$ |
| $Yp_Y$ | $H^0$, $H^{1/2}$ |
| $p_Y/Y$ | $H^0$, $H^{1/2}$ |

These cover the stronger height and conormal/frame multiplication inputs
needed when the high inverse loses one angular derivative. Both the full
$2N+1$ and cosine $N+1$ input Grams are retained. The normalized waist
pairing of R105 is an isometry, so it does not add an unrecorded factor
two to these norms.

These multiplier Grams do **not** upgrade the old cap's $H^{-1/2}$ flux
error to a positive-order bound. The complete complementary derivative
mismatch and coefficient commutator in section 7 of the strong
weak-residual contract remain separate inputs. The genuine cap regular
trace and regular flux also remain separate ports; multiplication on a
left-height function does not eliminate them.

## Replay and identity

From the topic directory, after the actual family producer has succeeded:
~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_interface_strong_grams.py \
  --interface notes/native_core_20261112/family_quarter_cut.json \
  --modes 4 --output-cutoffs 4,16,64,256 --bits 256 \
  --out notes/native_core_20261112/family_quarter_cut_strong_Grams.json
~~~
The entry requires the same actual physical radius, exact center and
whole eta interval; it checks the completed report kind, producer source
hash, all stored coefficient-array hashes and dimensions. The complete
proof inputs are linked by hash in its report. The selected matrices are
saved as small NPZ arrays; their selection fees are part of (3).

No global core propagation, full high inverse or nonlinear correction is
claimed by this consumer. Its absent numerical output is not inferred
from the successful old point-only multipliers.
