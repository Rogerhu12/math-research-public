# Four further p8 directions and the new residual concentration

Date: 2026-11-20 UTC. This batch continues the
[first six p8 directions](2026-11-20-curvature-qp-spectral-p8-six-step-result.md)
with the **same executed v6 source, true Phi, p=8, epsilon=0.001, scale=0.05,
physical-H² norm, 1,964 columns, all original rows and 0.992 geometry screen**.
It inherits the final square-root damping 0.015440957971131026. No exact
spectral residual Hessian was used in this batch.

## 1. Completed numerical result

Four directions and 12 actual trial fields completed in 145.352794732
seconds. All four directions accepted alpha=1/4. The eight rejected trials
failed actual Phi descent; none was accepted by a frozen quadratic proxy.
The final field is ca3679b4, passes the implemented final known-point screen,
and remains far from the README's continuous 1e-6 metric target.

| Quantity | Input 8d7407 | Output ca3679 |
|---|---:|---:|
| True normalized Phi | 1.9794928665089188e-7 | 1.907280008101566e-7 |
| Maximum sampled Gram norm | 0.015773377107712205 | 0.01507268828896618 |
| Old positive radial Jw | 0.2061976085003055 | 0.20417889354529722 |
| Old mean Jw/(S·2048) | 4.2458748986518334e-5 | 4.204306952169127e-5 |
| All raw quadratic sum | 765.6888688223185 | 754.4818009811452 |
| Legacy raw quadratic sum | 191.53718633579336 | 188.73441998911667 |
| Minimum sampled relative Gram determinant | 0.9804141816471336 | 0.9797826242389714 |
| Current known-point 0.03·D_lb·K | 0.9919678809041862 | 0.9918324577164394 |
| H | 1.8784136406728087 | 1.8782943995597212 |

The final highest known curvature is 8.071829876227618 at cell 191, u=0,
phi=0.500779220047, s=0.4525. The largest known point radius yields
D_lb=4.0958596044311655 at cell 880, u=0.8957522785341593,
phi=0.46200858941808964. The final scan reads 583 fixed/current arbitrary
locations, the full Gauss/grid set, and local refinements. The scalar
carrier and fixed support core coefficients are unchanged; exact affine
port checks pass.

The final flags `continuous_metric_certified`, `reach_certified`, and
`exact_solution_claimed` remain false. The numerical margin 0.992 is not a
continuous reach certificate or a new user completion threshold.

## 2. Actual four directions

All four used the inherited mu=0.015440957971131026, retained after each
accepted quarter step. Their accepted model ratios were 0.3349453373,
0.2954036691, 0.3348619346, and 0.4318796553.

| Direction | Phi after | Old Jw after | Max Gram after | Known product after |
|---|---:|---:|---:|---:|
| 1 | 1.9246140534821014e-7 | 0.2032927779167936 | 0.014946068887904913 | 0.9919257636674127 |
| 2 | 1.9136924935718143e-7 | 0.20444119341309772 | 0.015165435118286608 | 0.991885468441826 |
| 3 | 1.909440575288122e-7 | 0.20388068086039704 | 0.015004478729667856 | 0.9918635373414683 |
| 4 | 1.907280008101566e-7 | 0.20417889354529722 | 0.01507268828896618 | 0.9918324577164389 |

The accepted Phi decreases monotonically, while the sampled maximum moves
slightly up and down. The first accepted field in this batch has its lowest
maximum; it was saved separately and was not relabeled as the final Phi
iterate. On each direction both the full and half trials raised Phi, even
with the inherited larger physical norm penalty. This is evidence about
the current frozen-weight direction model, not an impossibility result.

The four QPs contain 1524, 1548, 1548, and 1548 rows; each has ten negative
bounds from the stricter 0.9918 linear margin. The general repair supports
these bounds and returned an explicitly checked feasible linear direction.
The actual nonlinear line search remained authoritative. Since this uses
the same spectral assembly already checked in the first batch, its new
spectral probe was deliberately skipped; no old probe value is reported as
a new experiment.

## 3. One new actual residual spectrum

After the batch, the already published full-Gauss spectrum reader was run
once on ca3679. This is a read-only diagnostic of the **original quadratic
residual energy**, not a Fourier identity for nonlinear Phi and not a
continuous error bound.

The actual Jw is 0.20417889354529722; the DCT/DST reconstruction is
0.20417889354529734, with difference 1.1102230246251565e-16 under the
reader's normalization. The ss, mixed, and phiphi component energies are
0.07230006616739802, 0.06112500385974255, and 0.07075382351815662.
Ninety percent of the finite angular energy lies at mode at most 8 and
99 percent at mode at most 16. Modes above 12 contain 5.390424170272295%;
above 24 contain 0.1003981927431305%. The residual is therefore not
predominantly an unresolved high angular frequency tail.

The actual largest sampled Gram norm is at cell 832, stage 6842,
s=1.096523983094783, phi=1.3775147475213059. Its raw components are
(0.014966071169377093, 0.0014488434597866597, -0.004615963768572984),
so the ss defect dominates that peak. Another broad high-error region lies
in the fine prefix around s=0.99747: at cell 656, stage 5782,
phi=1.3621749396424494, the maximum is 0.014289993011475885 with components
(-0.005017319821707611, 0.008821964899534455, -0.005896829239189105).

The current radial centers jump from 0.83 to 1.0570671854957785 and
1.077134370991557. These new locations give a concrete basis for later
localized radial-column additions near 0.99–1.02 and 1.097, if the improved
direction model still stalls. They do not prove that such additions work,
and no added-center solve is claimed in this note. The immediate next
implementation keeps this same objective and evaluates the exact positive
Hessian in the matrix residual; the full nonlinear field Hessian is a
different object.

## 4. Exact artifacts

| Item | SHA-256 |
|---|---|
| Unchanged executed v6 source | 1872298863d3d0309c74a35f4f93bdf1373528c5e28d3cfd0e6c4545f3be0ea0 |
| Input bundle | 8d7407edf7587403ebec783d1c208888f78ef78b4079c719ad3c87dcfc50db59 |
| Output bundle | ca3679b4d6401febdf89b222d253ae6ae88b0b3ab2cd7b4464185ae2d9c2c632 |
| Complete result JSON | b4c59f2bc8c1c2a567768adb2fc5f492ec289a76c3d550a16de4954acf011cfc |
| Output grid memory | c0e330c598b1ed593f0d2ee633d3459790b11c58d1200f91441f905a6d6289dd |
| Output arbitrary memory | ff0c040de68a8cdc6de212fea8b4a3625d873329e1a7292fa5cc49ac4060691a |
| Initial immutable witness manifest | 2dacff35a61b1d18c107083a6022a0440a9ac92faef3ae0d20c7db7738b110d0 |
| Final immutable witness manifest | 7c07f3f39f609f0c3ff0b3b3b160e72a83df27be4f2da91b8605f6b87864974c |
| Spectrum reader source | 1705bee9921b429152943f78065bc24f2b541898de71b5230d5deaa85ed1300c |
| New spectrum JSON | f5bc461ecabbf84964b849196e1c3f7676b109b9913882b0dc6013cecd328962 |

The numerical run stem is `work/geometry_path/curvature-qp-spectral-p8-next-four`.
The final location-only handoff contains 523 curvature points, 91 radius
points and 7 protected seeds. Every location must be reread at descendants;
this increasing list is still not a continuous cover.

## 5. Complete actual command and regeneration

The complete public source/dependency map and the 8d7407 input recipe are
in the [first p8 result](2026-11-20-curvature-qp-spectral-p8-six-step-result.md).
The same-scalar carrier remains SHA 71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112.
The first batch writes the memory files used here. Its final immutable
manifest is produced by the published history-location exporter, as given
in that record. No new scalar solve, hidden fixed witness, or new module
version is needed for this continuation.

From `/workspace/scratch/24b2ab87057a`, the actual command was:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v6_spectral.py \
 --gauss-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
 --qp-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
 --memory-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v2.py \
 --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --bundle work/geometry_path/curvature-qp-spectral-p8-six-step.npz \
 --memory-input work/geometry_path/curvature-qp-spectral-p8-six-step.memory.json \
 --local-memory-input work/geometry_path/curvature-qp-spectral-p8-six-step.local-memory.json \
 --fixed-point-input work/geometry_path/curvature-qp-spectral-p8-six-step-witnesses.json \
 --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
 --batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
 --base-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace.py \
 --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
 --norm-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py \
 --coordinate-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py \
 --scale-source math-research-public/topics/visible-flex-larger-amplitude/scripts/integrated_l2_scale_20261120.py \
 --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
 --spectral-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_weights.py \
 --out work/geometry_path/curvature-qp-spectral-p8-next-four.json \
 --safety .992 --steps 4 --damping .015440957971131026 --local-refine 9 \
 --spectral-p 8 --spectral-epsilon .001 --spectral-scale .05 --skip-spectral-probe \
 --centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --seconds 1800
```

All other defaults are the same as the first p8 run: positive legacy fraction
0.5; grid memory 32/4, moving arbitrary memory 12/2; angles 2048; stage block
64; low modes 12; top grid locations 32/4; reach ratio 0.03; linear margin
0.0002; 12 backtracks; 40,000 repair projections; 3 failed restoration
attempts. The time bound did not bind. The new spectral assembly probe was
skipped because its source and dimension were unchanged, as explicitly
recorded by the CLI.

The additional read-only diagnostic was:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/read_gauss_residual_spectrum_20261120.py \
 --repo math-research-public \
 --bundle work/geometry_path/curvature-qp-spectral-p8-next-four.npz \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --out work/geometry_path/curvature-qp-spectral-p8-next-four-spectrum.json
```

The exact reader is the published
`scripts/read_gauss_residual_spectrum_20261120.py`; its default angles and
legacy fraction are 2048 and 0.5. The final immutable handoff is recreated by
`export_curvature_history_manifest.py --report` with this batch's `.json`,
`--input-manifest` with the first p8 final witness file, the unchanged
`--carrier`, this batch's final `--bundle`, and
`--out work/geometry_path/curvature-qp-spectral-p8-next-four-witnesses.json`.
The iteration-budget status records only the completion of these four
directions. The research continues with the actual ca3679 field.


执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
