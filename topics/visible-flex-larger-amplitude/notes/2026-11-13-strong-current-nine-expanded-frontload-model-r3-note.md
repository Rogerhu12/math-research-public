# Expanded frontload box: same current-A finite model

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

All three models reuse the same accepted-A M32 baseline, actual complete nine-control response and 19 genuine geometry fields. No field, Jacobian, BVP or ODE is recomputed. After frontload +.064 was active in all preceding successful models, this run extends its upper design bound to +.128 and the k0 negative bound to -.128. All other previous physical search ranges, trust256, complete-gap nondecrease and twice-baseline five core-tail budgets remain unchanged. These boxes are numerical design choices, not physical necessary conditions.

| S cap / baseline | Predicted curvature | Predicted curvature times S | Frontload increment | k0 increment |
|---:|---:|---:|---:|---:|
| 0.98 | 8.3655164153179 | 32.612132672945 | 0.128 | -0.079339963028175 |
| 0.99 | 8.2671584099365 | 32.55755800614 | 0.128 | -0.025960185828246 |
| 1.0 | 8.2389888169784 | 32.77436472546 | 0.128 | 0 |

Each selected numerical model passed the complete replay of all 14,465,280 finite geometric inequalities and retained the exact saved-binary complete core-gap and weighted-tail readouts with their explicitly stated floating LP tolerance. The best predicted product is about 32.55756 at S cap .99. This is only a modest improvement over the preceding +.064 frontload model (about 32.60359), while the latter has already received a separate complete nonlinear warm-field evaluation. None of these expanded-box points has been evaluated as a combined warm or accepted as a nonlinear solution.

Observed individual second differences in the original actual fields are not a certified multivariable remainder. The larger-box predictions do not imply a new metric, all-time geometry, reach, closed diameter or amplitude certificate. The original .064 candidate proceeds to the production solver separately; these .128 models are retained as design data only.
