# R133 supplement: packed complete cap Fourier residual and prefix continuation

2026-11-14, visible-exact-astra-ac0d / newton_source.

**Proved.** The two real physical cap components can be evaluated with
one directed complex FFT per pair, while preserving the entire finite
convolution, the mean and every input column. The new `packed_v5`
producer uses this exact algebra and consumes the completed `v3` and
`v4` rows under their own explicit source identities. It does not
rewrite an interrupted producer's completion flag.

The actual first newly computed closed cell was global cell 604. It
passed all directed coefficient, inverse-angle, convolution and source
gates. The previous 91 rows, global indices 513 through 603, were read
from the unchanged actual `v4` checkpoint. At the first-cell checkpoint
the whole 1,977-cell cap was still incomplete; no full cap or body
inverse follows from this arithmetic result.

## 1. Complete simultaneous synthesis

Write the true finite physical amplitudes of a radial coefficient as

$$
 B(\theta)=\sum_{j=1}^{128}b_j\sin(4j\theta),\qquad
 C(\theta)=c_0+\sum_{j=1}^{128}c_j\cos(4j\theta).
 \tag{F.1}
$$

Every $b_j,c_j$ is a row of all 97 independent input columns. For each
radial coefficient form the exact complex function $B+iC$. Its Fourier
coefficients are purely imaginary and are

$$
 \widehat{B+iC}_j=\frac i2(c_j-b_j),\quad
 \widehat{B+iC}_{-j}=\frac i2(c_j+b_j),\quad
 \widehat{B+iC}_0=ic_0.
 \tag{F.2}
$$

The real part of its inverse transform is $B$, and the imaginary part
is $C$. Thus one complex inverse transform gives both complete real
fields. This operation is applied to every radial Hermite coefficient
and to the whole radial derivative. The original coefficientwise
Fourier bounds for the separate $B,C$ modules remain unchanged; they
are computed from their separate full lifted coefficients, not from
the size of the packed sum.

All arithmetic in (F.2) and in the transform is directed. Correlation
between the two fields is not assumed: rectangular complex intervals
enclose the exact packed function, and extracting either real
component remains a valid enclosure.

## 2. Complete simultaneous residual recovery

Use the already established finite physical residual decomposition

$$
 R_B=V_B+\partial_\theta F_B,\qquad
 R_C=V_C+\partial_\theta F_C.
 \tag{F.3}
$$

Here $V_B,F_C$ are odd and $V_C,F_B$ are even. The finite background
model, all scalar Taylor coefficients and all input columns are the
same as in the preceding complete matrix-residual producer. Pack
$V_B+iV_C$ and $F_B+iF_C$, transform them, and set

$$
 H_j=\widehat{V_B+iV_C}_j+i(4j)\widehat{F_B+iF_C}_j.
 \tag{F.4}
$$

Linearity gives $H_j=\widehat R_{B,j}+i\widehat R_{C,j}$.
Because $R_B$ is real odd and $R_C$ is real even, $H_j$ is purely
imaginary. More particularly,

$$
 \widehat R_{B,j}=\frac{H_j-H_{-j}}2,
 \qquad
 \widehat R_{C,j}=\frac{H_j+H_{-j}}{2i}.
 \tag{F.5}
$$

At $j=0$, the odd component is exactly zero and the entire even mean
is $H_0/i$. No division by a frequency is applied to this mean.
The producer checks that the directed real part of every $H_j$
contains zero before using its exact parity. The positive and negative
Fourier indices are both retained in (F.5).

The coefficient model has complete support through 127, and the trial
has support through 128. Consequently every finite convolution in
(F.3) has support through 255. The 512-point transform resolves the
whole product: $512>2\cdot255$. All entries outside that exact support
are checked to enclose zero before being set to their mathematically
known value zero. No unretained coefficient of the actual infinite
background is set to zero: its original complete remainder remains an
ordinary or angular-divergence source with its original gain.

## 3. Radial integration and original source units

For every recovered component and every output mode/input column,
the complete radial polynomial is converted to Legendre form before
integration. The original identity

$$
 \frac1{|I|}\int_I\left|\sum_{k=0}^{d}L_kP_k\right|^2dr
   =\sum_{k=0}^{d}\frac{|L_k|^2}{2k+1}
 \tag{F.6}
$$

is unchanged. The nonzero ordinary source keeps its full
$|4j|^{-1/2}$ weight; the even mean is computed independently. The
unknown scalar and Fourier remainders keep the same complete
ordinary and divergence bounds, the same module supremum order and
the same input normalization. Pairing two real transforms changes
none of these spaces or source units.

Since (F.2)--(F.5) are exact identities, the new interval values need
not agree bit for bit with the old enclosures. Both arithmetic orders
bound the same exact residual. It would be wrong to relabel an old
row as newly computed or to compare floating midpoints in place of
either interval enclosure.

## 4. Actual prefix and complete cover contract

The unchanged interrupted `v4` producer has source SHA
`28cbc02bfe60d91e608728437f2c5dd2906c56aa3a892f5a2fffbaafe72c6046`.
Its original process returned $-9$, and its original native is
`complete=false`, `failure=null`, with 91 fully saved rows on
$[513,604)$ inside the planned range $[513,768)$. Its container SHA is
`11204689bcbd84eafd155e7b15fb027fda05e1884f65ec5cc9c2ebe36002908d`.
The process cause is unknown. No mathematical failure is inferred
from the signal.

The new producer verifies the actual kind, the explicit old source,
every original input and dependency hash, each exact row index and
its genuine closed interval. It accumulates the already directed
source terms of those saved rows, and starts at 604. The first and
requested final index remain 513 and 768. Original checkpoint and
process files remain unchanged.

Likewise, previously completed `v3` rows are accepted only with source
SHA `9f80d0cb4a54db0e90921e35a8e79e610d2a7ba04f7f2fe46c91093fe436ecf7`.
Their valid ordinary/divergence/mean bounds are consumed as old rows.
The final assembly still requires a complete, nonoverlapping,
consecutive cover of all 1,977 actual cells, and records the kind and
source of every contributing part. It also pays every independent
inlet, outer Robin and even mean row. An incomplete planned range is
not counted as complete because its prefix is valid.

The new source is
`scripts/fourfold_codazzi_physical_cap_matrix_residual_packed_v5.py`.
The small accompanying record contains the first actual new row 604,
the exact original prefix identity, the new source and all dependency
identities, and the precise command. It makes no complete-cap claim.
Large shared Hermite arrays are read without copying and are still
reconstructed by the already published padded-cap/moving97 procedure.

The unchanged active calculation is

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python3 scripts/fourfold_codazzi_physical_cap_matrix_residual_packed_v5.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --proposal /workspace/scratch/ac0d699811ad/physical-cap-precompose-20261114.json \
  --first 513 --count 255 \
  --resume /workspace/scratch/ac0d699811ad/physical-cap-precompose-20261114/continuous-v4-part002-after-profile-native.json.gz \
  --out /workspace/scratch/ac0d699811ad/physical-cap-precompose-20261114/continuous-packed-v5-part002-resume91-native.json.gz
```

The wrapper imposes a 1,792 MiB address-space bound and writes each
completed new closed cell before advancing. At most two heavy
cap/body/signed consumers owned by this worker run concurrently; this
is a process resource limit, not a change to a mathematical gate.
