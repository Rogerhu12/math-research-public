# Partial H2 batch stopped after the closed-surface diameter correction

Date: 2026-11-20. Actual partial numerical work; no completed direction or accepted child.

Source `scripts/resume_20261120/fullclosed_integrated_h2_lm_v2.py`, SHA256 `107e0c58a240b6d3c5a8a338b279e03cec405fd43f2900272605d8f906d2b0aa`, adds explicit radial coarse centers and an optional sampled curvature cap. The attempted batch used the m6/r5 parent SHA256 `7bf4a3b5660537990425a1182a07dfb95e96e4038fe9d771ee764466c435dd0b`, complete SSE268.94965596739405, maximal relative Gram .19741091623846563, and sampled maximum principal curvature10.745681657888415.

The attempted configuration was m12/r11 coarse columns (1280 columns), all original DoubleIntegrated H2-type directions, initial mu=.005, maximum 256 inner iterations and two planned directions, with an explicit numerical curvature cap16. The same-norm coarse Gram preparation succeeded: normalized condition31547.093856025258 and separated-versus-literal norm relative difference4.137174555750721e-15. This does not establish a nonlinear solve result.

During the first LSMR direction, rereading the actual closed-surface interface established that the completed surface includes the upper sheet and its z=0 mirror, capped by disks at z=+H and z=-H. The phase family preserves H. Thus its reference F0 diameter satisfies D>=max(2,2|H|), not merely the weaker D>=2 bound used to choose cap16. The source parent is not demonstrated to satisfy this stronger necessary curvature condition.

The running batch was immediately interrupted with SIGINT; session exit code130. The last persisted progress line records176 JVPs and176 VJPs at54.91171163400031 seconds. This is a lower bound on work before interruption, not an invented exact final call count. Zero directions completed, zero nonlinear line-search trials ran, zero new states were accepted, and no final bundle was produced. The numerical linear algorithm itself did not return a failure diagnosis; the scientific trial-selection target was corrected.

The next source version uses an explicit necessary numerical point screen

reach_ratio * max(2,2*abs(H)) * sampled_max_principal_curvature <= safety_factor,

with reach_ratio=.03 and a declared factor below1, and checks the actual parent before a linear budget. This remains a necessary pointwise screen, not a continuous reach certificate. It uses the proven reference-family diameter lower bound, not the diameter of the current Ft as a substitute for D0. A genuinely qualifying parent must be selected before resuming.

All source and partial work identities are retained; no prior warm is recomputed and no continuous certificate is rerun.
