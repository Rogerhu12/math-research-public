# R133 supplement: actual radial-reference Airy profiles and complete old-circle source budgets

2026-11-14, phase_inverse.

**Actual public result.** Public Actions run
[43635999157](https://github.com/Rogerhu12/math-research-public/actions/runs/43635999157)
completed successfully. Its mathematical child returned zero, all
nine gates passed, and all six complete radial windows were consumed.
It reused all six accepted analytic amplitude tensors, all 1328
completed moment rows and all 1328 completed directed matrix rows.
The only new mathematics was six scalar Airy-profile evaluations
and 4377 complete source-integral rows.

The true radial reference removes the large central-profile cost
caused by combining unrelated radial extrema. The resulting source
bounds are much smaller than those from the preceding analytic
profile calculation. They remain too large to grant the intended
complete strong-return gate. No full high-frequency boundary-value
inverse or true PDE branch is asserted.

## 1. Actual execution and immutable identities

The workflow event and independently recorded scientific checkout
were both

~~~text
2b5de38c629076b1cf3c7bc445b283fe5726b102
~~~

The actual mathematical child took 14.693844024000008 seconds.

The complete native,
[radial-reference-Airy-sources.json.gz](../notes/radial_reference_Airy_sources_ci/run-43635999157-1/consumers/radial-reference-Airy-sources.json.gz),
has 3434233 bytes and SHA256

~~~text
fec8740c26064b973c61828a960c3e5c7e864b83542222c155b9e56474c39853
~~~

The readable
[process.json](../notes/radial_reference_Airy_sources_ci/run-43635999157-1/consumers/process.json)
has 53604 bytes and SHA256

~~~text
54f24e5d4750a3607acfaa1e1b11e7ea58eb390a8270d07c5e78b7f77943b15d
~~~

The
[worker-process.json](../notes/radial_reference_Airy_sources_ci/run-43635999157-1/worker-process.json)
has 2472 bytes and SHA256

~~~text
d027062143f1cce021eb7477cd82dd67feb5cc116a8dc61c9a4089f30f5b372b
~~~

The scientific producer is
[fourfold_codazzi_radial_reference_Airy_sources.py](../scripts/fourfold_codazzi_radial_reference_Airy_sources.py),
SHA256

~~~text
10e961471e790286fc439ce56b5e0fff9e9b00e1a444d61396f4187fabe35414
~~~

The
[18-file scientific manifest](../notes/2026-11-14-R133-radial-reference-Airy-sources-CI-inputs.json)
has SHA256

~~~text
831bbaa726f36b1bb9e0b69fec67e55031b54ef341dfa77b6a7d5cf549f9bae2
~~~

It pins 8635725 bytes, including the two complete repository natives.
The sole external original native is the already completed larger-root
record from run 43616813816, SHA256
`dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212`.
No original forcing or directed-matrix computation was restored and
run again.

The other two original complete native identities are:

| Input | Actual run | Native SHA256 |
|---|---|---|
| Original complete moment rows | 43629465215 | `7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c` |
| Six complete analytic amplitude tensors and directed rows | 43634456797 | `e54f05c3eea0e2ed9a8f7511004059b730b448adb26c9e035cc1803325080db8` |

Before freezing the science, the worker actually pulled from
`2b5de38c629076b1cf3c7bc445b283fe5726b102` to the same commit.
Before publication it pulled to
`56677b0f11922e67de47343dec9a9ba634040787`.
Both recorded root/topic README diffs are empty. The complete
output and failures were preserved in the run's independent
publication directory and artifact.

## 2. What changed in the actual bound

This run executes
[the true-radial-reference theorem](R133-supplement-radial-reference-Airy-partition-and-central-series-bounds.md),
R.1--R.15. For each real radial point and each real parameter
$|\delta|\le10^{-8}$ it retains

$$
 \overline A(\rho)=\frac32\int_0^1s^{1/2}a(s\rho)\,ds,\qquad
 |A-\overline A|\le a_+j,\qquad
 \epsilon=\frac{a_+j}{a_-}<1.
 \tag{A.1}
$$

The central/high input decomposition uses
$(2/3)n|\rho|^{3/2}\overline A(\rho)$.
It changes neither the actual Airy trial nor any radial derivative.
It creates no interface source. The positive real reference is
used only for real parameters; no such positivity is assigned to
complex parameter values.

At the smallest window the accepted radial envelopes are approximately
$a_-=4.39808468$ and $a_+=22.18422104$. Their spread had entered the
old entire-disk bound even though it is primarily radial variation.
The new relative angular error is only
$\epsilon<0.000507638$ there. The actual Airy argument disk is now
bounded by $Z<1.310815$, and the complete two-column positive-series
calculation gives

$$
 C_A<1.570370,\qquad C_D<1.823784
          \quad(R=1/1000).
 \tag{A.2}
$$

At the largest window $R=1/50$, the same actual gates give

$$
 \epsilon<0.057696,\quad
 Z<1.360300,\quad C_A<1.663224,\quad C_D<1.930630 .
 \tag{A.3}
$$

Each entire series and its derivative uses sixteen finite terms
and its complete geometric tail. Every tail ratio is strictly
below one. No sampled Airy values, zero-tail convention or
unpaid asymptotic range enters these bounds.

The high-profile prefactors still use the original bounds for
the actual $A$, not the partition's $a_-$ without its relative
error. Both negative ray branches and the single positive real
map $X$ remain as before.

## 3. Exact operator and parameter scope

The family is the same repaired centre plus the same complete
193-component direction, at the fixed $\eta_0$ and
$|\delta|\le10^{-8}$. The full old mean and all Fourier outputs
are retained. The input cutoff is $|j|\ge97$, the physical
frequency is $n=4|j|$, and the density normalization is $n^{7/6}$.

The source operator is the complete leading old-circle $I/J$
remainder together with its independent even-mean row:

$$
 H^{-4/3}\longrightarrow
 L^2_r(H^{-2/3}\times H^{-2/3}).
 \tag{A.4}
$$

The second row is a pure independent mean, so its
$H^{-2/3}$ and $H^{-1}$ norms agree exactly.

All $H^{-1}$, $H_D$, $w_0$, radial and angular amplitude
tensors, real composition constants and complete exponential
Fourier-tail factors were copied from the successful previous
native. The exact U.20--U.29 derivative and mean identities,
the M.14 complete directed words, and the original projected
operator order are unchanged.

The true-root interval is

$$
 \left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}
 \right].
 \tag{A.5}
$$

Both sides of that bracket are integrated separately.
The positive collar/body split uses the same actual fixed cut

$$
 r_b=\frac{1192029371497}{5000000000000}.
 \tag{A.6}
$$

No low/high or independent-mean inverse is inferred from
the given-head positive graph.

## 4. Actual six-window source bounds

All displayed entries are outward-rounded upper bounds from
the successful native. The final column applies the already
paid complete negative source-to-primitive map to this specific
leading nonlocal and mean source component.

| Radius | Complete rows | Negative ordinary source | Positive collar source | Positive body source | Negative source after primitive/Cauchy propagation |
|---|---:|---:|---:|---:|---:|
| $1/1000$ | 144 | $715694.724049$ | $199021.846640$ | $621947.653951$ | $108478.950298$ |
| $1/500$ | 274 | $909406.646498$ | $202283.446172$ | $773649.172599$ | $232414.850442$ |
| $1/200$ | 627 | $1460023.429273$ | $217220.128424$ | $1081716.210842$ | $1163784.437977$ |
| $1/100$ | 898 | $2664238.959912$ | $262512.853764$ | $1584442.923920$ | $13952595.147485$ |
| $3/200$ | 1106 | $4097511.885815$ | $324000.994152$ | $2197380.266981$ | $147716523.959699$ |
| $1/50$ | 1328 | $5549241.466141$ | $392453.943853$ | $2905007.824822$ | $1225496405.939750$ |

The previous analytic negative source upper bounds were
$3.385779\,10^{10}$ at $R=1/1000$ and
$7.109141\,10^{11}$ at $R=1/50$.
Those original bounds and all their evidence remain intact.
The new comparison concerns proved upper estimates, not
a lower bound or an observed norm of the true operator.

For the smallest window the dominant terms are now

| Complete first-row term | Outward upper source bound |
|---|---:|
| $S_V$ | $59576.353657$ |
| $S_Q$ | $9369.710777$ |
| $R_QJ\,T(g_d)$ | $632140.252773$ |
| $R_QJL\,T(h)$ | $7632.963754$ |
| Complete primitive error | $9373.080713$ |
| Original $r_Q$ mean | $0.094551$ |
| Original $v_\phi$ mean | $0.502444$ |
| Original raw $D$ mean | $9.826480$ |
| Original $V_0$ mean | $1.425716$ |

The $R_QJ\,T(g_d)$ term still dominates this particular
complete upper bound. Its ordered whole-word matrix cost
and real radial amplitude derivatives remain the next
substantive quantitative inputs.

## 5. Successful reuse and remaining obligations

The run verified the preceding ten-gate actual analytic
receipt, the original root and moment identities, all six
complete saved tensors, the true parameter and root domain,
the exact positive cut, all 1328 reused rows, both complete
central-series tails and all 4377 radial integrals.

The native reports zero repeated original target, coefficient,
ray, amplitude, moment, directed-matrix or Fourier-tail
calculations. It preserves the entire original tensor field
and stores the new scalar profiles separately. Its recovery
path also preserves each accepted new profile before source
integration, and retains accepted integral rows exactly.

The result still leaves the complete corrected source assembly
open. In particular,

~~~text
local_L0_w1_paid = false
positive_source_to_root_conversion_claimed = false
complete_strong_return_norm_evaluated = false
numerical_cutoff97_inverse_claimed = false
actual_PDE_branch_claimed = false
~~~

The newly executed profile bounds do not pay the local
$L_0w_1$ residual, the complete old inverse remainder on
$w_1$, all propagated original seams, the full finite-head
feedback or the genuine strong-return inverse.
