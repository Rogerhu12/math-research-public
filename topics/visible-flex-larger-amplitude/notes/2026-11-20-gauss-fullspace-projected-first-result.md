# First all-Gauss complete-space tangent direction with radial quadrature

Date: 2026-11-20. Actual numerical continuation by /root/fullclosed_solver.

## Model and changed finite objective

The genuine parent is Gauss-QP bundle SHA256 `2038ba41e2001036eebe8bc43fccbb54b8d9ccf180f73139420798de278bcaa9`. The unchanged original field has923 nodes, M160, 1,332,245 free variables, and2048 full angles represented by513 exact weighted quarter-orbit samples.

Every original1845 node/midpoint row is retained as a literal prefix. The same scalar oracle carrier adds5532 Gauss rows, for7377 total radial observations. Carrier SHA256 is `71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`; operator source SHA256 is `26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d`. No mesh, prescribed scalar metric, unknown or endpoint condition changes.

The new positive radial squared-row weights are w=.5*legacy composite Simpson+.5*new Gauss. Their sum is S=2.3712998717298257, minimum6.692362983545742e-7 and maximum .0066890618319262645. The actual least-squares row factor is sqrt(w_s)*(1,sqrt(2),1)/sqrt(S*2048), in addition to the operator's angular orbit multiplicity exactly once. This is a different objective from the old equal-stage sum. Legacy raw SSE, all-row raw SSE, weighted SSE, and weighted mean are therefore recorded separately.

The complete H2-type DoubleIntegrated directions and1280 coarse directions whitened in that same norm remain. The latter's nodal B/B^T is constructed from the original structural template; no old-only residual is evaluated there. All actual residuals, Jacobians, point geometry and constraints use all7377 observations.

## New interpolation transpose and tangent slice

The point cotangent now scatters through observation_cells and the literal3-by-6 observation_weights. This covers original nodes, midpoints and every added Gauss point without a parity-based stage assumption. New helper source `scripts/resume_20261120/fullclosed_point_cotangent_observed.py` has SHA256 `de58a82e4a30a794f04e4cbf980d16d0a3b70f47a3afffc71986079ec11e5a5e`.

The new added-stage arbitrary-sixjet directional complex-step difference is1.1369043632571527e-14; the actual Gauss curvature point derivative differs by3.687272243895906e-14. These validate the new point interpolation transpose, not a repeated continuous certificate.

The selection rule is unchanged: top16 separated curvature locations, top2 radius locations and analytic diameter lower bounds, up to16 products r=.03 D|kappa|>=.955, with true acceptance at r<=.98. This parent supplies16 rows. Relative row-Gram cutoff1e-10 retains rank8; Householder QR gives row orthogonality error3.9968028886505635e-15. The actual projected coordinate step has maximal normalized selected-row linear residual4.3247308960994076e-9; the tolerance and numerical residual are reported explicitly rather than asserting exact tangency to discarded numerical directions.

## Actual nonlinear trials

One BLAS thread; one direction;256 maximum LSMR iterations; mu=.0025; atol=btol=1e-6. The inner solve returns stop7. All listed values are actual full-observation nonlinear evaluations.

| State or trial | Weighted SSE | All raw SSE | Legacy raw SSE | Max Gram | Gauss necessary product |
|---|---:|---:|---:|---:|---:|
| Genuine parent | 1.3604706615368882 | 1108.6689095307765 | 276.8493731902904 | .12250456992212366 | .9730101709423132 |
| alpha1, rejected geometry | .4347588396759938 | 1110.048664198167 | 277.45932150165106 | .04950508883403537 | 1.0681985875159627 |
| alpha1/2, rejected geometry | .7011697660292736 | 866.8064742837383 | 216.39926156983273 | .08187981575315151 | .9939768213473531 |
| alpha1/4, accepted | .9812955395142278 | 926.5506583275067 | 231.29820409605992 | .10186568199218482 | .9730072941797351 |

The accepted weighted mean is .00020206141718546146. Its min relative determinant is .94606368805809 and min relative E is .9485375999915028. H=1.9112007287168216, sampled rho min .16595945250161437 and its simple angular Lipschitz lower estimate .13813981316920124.

The accepted full-Gauss K maximum is7.929778549028246 at stage6772, s=1.0134699300537593, phi=.6381360077604268. D_lb=4.090098641737279. The metric worst point is stage6881, s=1.2252440544749044, phi=pi/2. The geometry readout covers3,784,401 representative points, corresponding to15,108,096 full angular orbit points. The old inherited wording in one geometry scope string mentions nodes/midpoints; the executed generic observation map,7377 count and added-stage worst locations establish that the actual readout includes every Gauss point. This wording is corrected in the successor source without rerunning the budget.

The full linear step has max nodal delta Y/U/A=.005041395896855981, .019714900406194925, .152718045316199; the accepted correction is one quarter of it. Endpoint projection residual is4.573977915173222e-18. LSMR normr=.00952640556192736, normar=.00007140521185746831, normA=51.03424915225823, condA=17.455446221243744, normx=.42914149560969495. Direction and true line search take361.71333524299916 seconds.

## One additional continuous-location lower witness

After the solve, the root's existing local-curvature reader is run once from this accepted Gauss worst point, using the exact same quintic cell and analytic lift at arbitrary u and phi. Nelder-Mead uses max300 iterations and xatol=fatol=2e-10; it returns success after86 iterations and189 evaluations. It finds cell821, u=.11022924905924839, phi=.6372331788884487, s=1.0132184743085018, with K=7.969807246586475. Combined with the already established D point lower bound, the necessary product is .9779189338251378, still below the declared .98 screen.

This is a newly discovered actual point and therefore a lower witness to the continuous maximum, not a certified local or global maximum or continuous upper bound. The successor tangent solve will include this actual arbitrary point. The root local-reader SHA256 is `f376c058fd9d931ee4df6dabf68cbabc93e8e6c0b61cb15a1b2c20fd9f135456`.

## Executed identities and continuation

Driver `scripts/resume_20261120/fullclosed_gauss_h2_projected_lm.py`, SHA256 `c6e5fbf2426a273b0672710125720181f7bdd558011717369afe1efb84aac180`.
Accepted/final NPZ SHA256 `def1ccbded6c463a014a71a39f259c59501412d5c84afec07ce7253c9dc34f5d`.
Direction NPZ SHA256 `9fff58576d7c497dcf88ed37959532eb78f7758dba0792079e02a34937293402`.

An earlier initialization attempt passed a legacy prefix into unweight(), whose API requires every stage. It exited before LSMR or any nonlinear trial. The diagnostic now divides the prefix by the same explicit orbit factors; no full row weight or equation changed. Its setup record is separate and is not an extra numerical budget.

All source paths, source hashes, quadrature parameters, actual coarse centers and every nonlinear trial are in the work-only report. Raw arrays are not committed. The new parent is preferred to descendants that already fail the stronger local-point screen. No closed-isometry, continuous metric/reach, all-t, held/E3, or fixed-g refinement completion is claimed.

## Complete public reproduction recipe

The actual report SHA256 is `b3ed83be596ba2548c668a2fda2e3ad46a45e149edbca830e362be939074d654`. Rebuild the parent and same-scalar carrier using the linked [Gauss-QP recipe](2026-11-20-curvature-qp-gauss-six-step-result.md) and its dependencies. All source dependencies below are retained in the topic; a scratch report is not needed to discover the arguments.

With `repo`, `topic`, and repository-external `work` set as in that recipe, the actual scientific parameters are:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/fullclosed_gauss_h2_projected_lm.py" \
 --repo "$repo" \
 --bundle "$work/geometry_path/curvature-qp-gauss-six-step.npz" \
 --outdir "$work/fullclosed_solver/gauss-h2-projected-first-fixed" \
 --implementation "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --geometry-observed-source "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --observations "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --low-modes 12 \
 --coarse-centers .3,.6,.8300000000000001,1.0570671854957785,1.1975374839662283,1.3580749679324564,1.5587468228902417,1.759418677848027,1.9400233473100337,2.140695202267819,2.26109831524249 \
 --legacy-fraction .5 --reach-ratio .03 --reach-safety-factor .98 \
 --active-band .025 --active-max-rows 16 --active-rank-tolerance 1e-10 \
 --active-top-curvature 16 --active-top-radius 2 \
 --max-directions 1 --maxiter 256 --damping .0025 \
 --lsmr-atol 1e-6 --lsmr-btol 1e-6 --line-trials 15 --target 5e-7 \
 --angles 2048 --stage-block 64
```

The actual coarse center node indices are `[130,250,342,831,838,846,856,866,875,885,891]`. The published default helper has SHA256 `16cd8680d3d63e66a7ff335feadaa275a3efc96729028aaafa7fd9668a09181f`; complete DoubleIntegrated coordinates use `d429d68baded58908454e49f4bfdf8e43ce9d3f857ed666eafa95c1c366462db`; scale source uses `ff147637f4d5ebc52700e0ee58ba168374fb86ff72f641ae004ba67e2eb5c560`. Other sources are exactly the preceding Gauss-QP dependencies, plus the new driver and point helper identified above. This command changes only filesystem placement of the same executed source bytes. Numerical re-execution does not promise byte-identical timing reports or compressed NPZ metadata.
