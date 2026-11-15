# R133 supplement: actual complete cut shape, mean and component scalars

2026-11-15, visible-exact-astra-0df9.

**Actual public computation completed.** Public run
[43715426316/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43715426316)
returned science child code 0 and passed all nine new identity and
complete-consumption gates. The complete signed 193-slot response and
the saved repaired 32-mode base were consumed without re-evaluating an
old trial, intrinsic target, matrix, angle, repair or Green operator.

The new component and shape bounds are available for the selected
parameter cap-row estimate. The separately recorded J.18 sufficient
low-entry test is false at the declared full parameter radius
$10^{-10}$. That is a statement about this upper bound, not a lower
bound on the actual curvature difference.

## C1. Frozen source, actual execution and evidence

The deployment was commit
97dece31bb939b2dc245ce0deda11a3d821c1af2.
The exact scientific source
[scripts/fourfold_codazzi_selected_cut_shape_mean.py](../scripts/fourfold_codazzi_selected_cut_shape_mean.py)
has 16,748 bytes and SHA256
745fc480b101dbd7ca035c11826d2d0208c4d2db3568e0bbb4214fa401ddbb19.
The [consumer contract](../notes/2026-11-15-R133-selected-cut-shape-mean-contract.md)
has 9,975 bytes and SHA256
67e20185e59f29cb9d02a6320648cf102d0b6137b172188ec5a3fc07bb3e97ba.

| Complete evidence | Bytes | SHA256 |
|---|---:|---|
| [actual-cut-shape-mean-conclusion.json](../notes/selected_cut_shape_mean_ci/run-43715426316-1-selected-cut-shape-mean/actual-cut-shape-mean-conclusion.json) | 7,733 | 5d74a0f24afe7d490cd17f04f0c0ea5efb671fd277ced502269f4d94c748a413 |
| [process.json](../notes/selected_cut_shape_mean_ci/run-43715426316-1-selected-cut-shape-mean/process.json) | 13,640 | 82b7c37637c9ebec074ae7647595200c2cd790cf19728ef0e4d93a8452e59812 |
| [input manifest](../notes/2026-11-15-R133-selected-cut-shape-mean-CI-inputs.json) | 6,993 | 95541c2e2bd7cd7547d13319fdacdaf3a0d8ba1eb1ac675fd4d68480b6994b57 |

The science child started at 12:45:42 UTC and returned 0 at 12:45:43 UTC.
Its internal mathematical runtime was 0.027363467 seconds.
The complete scientific conclusion and identity were emitted before
terminal Git publication in an 8,475-byte stdout payload with SHA256
435a021f0fb122077ebdac3620c13df83a86fec45d34d0ab70c381ef14289242.

The full signed temporary audit has 24,323 bytes and SHA256
3658bd3983e0ed67961e07730aaf3f6652cd27598cbfac6dc7bbe140e21f751d.
It was not persisted. The retained complete scalar conclusion is
sufficient for every use described below.

## C2. Exact cut, component ordering and original identity

The cut is the actual left interior trace at $L=9/10$, at the fixed
intrinsic parameter $\eta_0$. The complete continuous response is
$$
 Z=(\xi,\zeta),\qquad Q_\delta=Q_0+\delta Z,\qquad
 |\delta|\le10^{-10}.
 \tag{C.1}
$$
The centre definition is
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
and the direction definition is
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.

The original successful boundary run 43599771405/1 supplied the full
raw physical response trace, SHA256
b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263,
89,319 bytes. Its exact order is 96 odd sine amplitudes, the one
genuine even mean, and 96 even cosine amplitudes.
The already mean-flow-corrected boundary vectors are distinct
objects and were not substituted for this raw response.

The accepted base cut native has SHA256
119dedb2e62f23553b81dea9eb787d8298c1224eebc2cc38790ec50274df0ca7,
1,116,129 bytes. Its 65 exact base coefficients, exact physical
offset and complete true mean reconstruct the same repaired
32-mode base at this cut. Every saved normalized-angle coefficient
was checked against that same base.

The old base data's original wider $\eta$ box is used only as an
enclosure of fixed $\eta_0$. This computation does not claim a
new result uniform on that wider parameter box.

All norms use the original moving angle $\phi$ with normalized
measure, physical frequencies $4j$, sine/cosine square Gram $1/2$
and independent mean square Gram $1$. The response amplitudes are
already physical and are not multiplied by $\alpha$.

## C3. Complete continuous repair and signed shape

Let
$$
 m_0=\langle v_0\rangle,\qquad j_0=v_0/m_0,\qquad
 \mu_Z=\langle\zeta\rangle,\qquad e_Z=\zeta-j_0\mu_Z .
 \tag{C.2}
$$
The actual signed base mean remains enclosed by
$$
 m_0=-3.2072027190\ \pm\,4.13\cdot10^{-11}.
$$
The complete response mean is enclosed by
$$
 \mu_Z=-0.003278095187252\ \pm\,6.70\cdot10^{-16}.
 \tag{C.3}
$$
It is not the scalar intrinsic field $s$ and is not discarded by
the identity $\langle e_Z\rangle=0$.

The complete response repair fee is
$$
 E_Z=2.292\cdot10^{-16},\qquad
 E_{Z,\phi}=384E_Z=8.80128\cdot10^{-14}.
 \tag{C.4}
$$
Each component bound contains its own valid complete fee, while a
complete pair bound pays the already proved pair fee only once.

The raw shape coefficients are formed with their signs as
$q_{\zeta,j}-q_\mu(j_0)_j$, before taking absolute values or square
sums. For the continuous correction, the identity
$$
 e_{\zeta}-j_0\langle e_{\zeta}\rangle
 =P_\perp e_{\zeta}-(j_0-1)\langle e_{\zeta}\rangle
 \tag{C.5}
$$
gives the complete shape fees
$$
 \begin{aligned}
 {\cal E}_{A^0}&\le(1+\|j_0-1\|_{A^0})E_Z,\\
 {\cal E}_{\phi,A^0}&\le384E_Z+\|(j_0)_\phi\|_{A^0}E_Z .
 \end{aligned}
 \tag{C.6}
$$
Thus the same mean that is subtracted in the shape is retained
independently in (C.3) and in all scalar outputs.

## C4. Actual complete bounds

The following decimals are rounded upward from the full directed
intervals in the retained conclusion. They have not yet been
multiplied by the selected parameter radius.

| Quantity | Complete upper bound |
|---|---:|
| $\|\xi\|_{A^0}$ | $0.241363696$ |
| $\|\xi_\phi\|_{A^0}$ | $0.991176944$ |
| $\|\zeta\|_{A^0}$ | $0.601228813$ |
| $\|\zeta_\phi\|_{A^0}$ | $2.456459299$ |
| $|\mu_Z|$ | $0.003278096$ |
| $\|e_Z\|_{A^0}$ | $0.597994429$ |
| $\|(e_Z)_\phi\|_{A^0}$ | $2.456636503$ |
| $\|(e_Z)_\phi\|_2$ | $1.649000368$ |
| $\|\zeta_\phi\|_2$ | $1.648878378$ |
| $\|\zeta\|_{H^1}$ | $1.699522570$ |
| $\|Z\|_{A^0\oplus_1 A^0}$ | $0.842592509$ |
| $\|Z_\phi\|_{A^0\oplus_1 A^0}$ | $3.447636242$ |
| $\|Z\|_{L^2\oplus_2 L^2}$ | $0.444101620$ |

The saved base coefficients also give
$$
 \|j_0-1\|_{A^0}<0.013334283,\qquad
 \|(j_0)_\phi\|_{A^0}<0.054056879,\qquad
 \|(j_0)_\phi\|_2<0.037226798.
 \tag{C.7}
$$
The exact reference mean and finite base shape, including its
continuous centre repair, are already included in these bounds.

For a direct CS.27 consumer, the six fields in
complete_scalar_bounds are respectively
xi_A0, xi_phi_A0, zeta_A0, zeta_phi_A0,
zeta_mean_absolute and complete_shape_A0.
Their values are complete Arb ball strings.
Multiplication by $d=10^{-10}$ is performed once at that later
selected-parameter comparison. No $\alpha$ or extra repair fee is
introduced there. The additional complete_shape_phi_A0 field may
give the independent whole bound
$\|e_Z\|_{A^0}\le\|(e_Z)_\phi\|_{A^0}/4$.

This is a scalar input interface for the complete cap-row estimate.
It is not an entrywise modification to a signed Gram, a projection
of unknown high input, or a recomputed boundary operator.

## C5. The recorded J.18 low test and its precise meaning

Apply the sufficient bound from
[the shape-and-mean trace theorem](R133-supplement-shape-and-mean-separated-physical-inner-curvature-trace.md),
using the smaller of the two complete shape derivative bounds.
The actual scalar coefficient satisfies
$$
 B_Z^{(1)}
 :=\min\left\{\frac{\|(e_Z)_\phi\|_2}{16}
                +\frac{|\mu_Z|}{576},
        \frac{\|\zeta_\phi\|_2}{16}
                +\frac{13|\mu_Z|}{2304}\right\}
 <0.103068215.
 \tag{C.8}
$$
At $d=10^{-10}$, its recorded complete upper is
$$
 dB_Z^{(1)}
 =1.0306821409716908652\ldots\cdot10^{-11},
 \tag{C.9}
$$
where the displayed equality names the recorded upper bound, not the
actual physical curvature difference.

The target of that particular diagnostic is $10^{-9}/128=7.8125\cdot10^{-12}$.
The directed lower remaining budget is therefore
$$
 -2.4943214097169086525\ldots\cdot10^{-12}.
 \tag{C.10}
$$
The retained conclusion accurately records
positive_remaining_low_gamma_budget_proved=false
and a sufficient unknown comparison radius of zero.
The independent coarse neighbourhood margin remains positive:
$$
 2^{-10}-d\|\zeta\|_{H^1}
 >0.0009765623300477.
 \tag{C.11}
$$

Equations (C.9)--(C.10) do not prove that the actual physical input
exceeds the target. They show that this J.18 upper-bound test does
not provide a positive remaining unknown-correction radius at the
declared full $d$. A sharper proved value-map estimate may be
consumed separately without changing these actual recorded fields.

## C6. Preservation and remaining scope

All nine new gates passed. They verify immutable parameters/source,
both old native hashes and the original process, the original ten
boundary gates, the full raw 193-slot trial at the same centre,
the exact left cut, the complete repaired base and true mean,
the negative base mean/Jacobian margin, all 32 signed phase identities,
and complete evaluation of the scalar norms with every repair fee.

All old native bytes and means are unchanged. The successful source
is locked for reuse. There were zero old target, trial, angle, repair,
matrix or Green recomputations, and no new numerical archive or
Actions artifact was persisted.

The unknown correction was not evaluated. No core existence,
nonlinear selfmap, high-block inverse, waist or phase equation,
complete boundary matching or full physical-curvature entry is
claimed by this scalar computation.
