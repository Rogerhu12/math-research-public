# A 726-position solve from the p2 Cauchy join and its independently detected near fold (V53)

Use exactly V52's 512-angle physical field, original fixed target, physical mark, outer infinite shell, and both real caps. Free 22 compact cubic radial B-splines supported on [.24,.8] times 11 Cartesian angular indices per coordinate, or 726 true positions. All perturbations and their through-second derivatives vanish at both interfaces. On 67 native uniform radial positions and 80 native angles, evaluate the original metric, curvature, guide, and area rows. First take 220 L-BFGS steps. Then take 12 accepted full-row damped Gauss–Newton steps with up to 35 preconditioned conjugate-gradient iterations, including derivatives of both principal curvatures, the area, all active seven guides and the robust metric residuals.

The first training cost is .783235375 and the last .625909839, native sampled spectral defect .889535764 and .880101529, training curvature norm before physical scaling 23.174517 and 23.237678. On the entire prescribed and independent grids the answers differ sharply.

| Actual state | G10a metric | G10b metric | G11 metric | G11 physical curvature | G11 minimum area ratio | G11 held | G11 half-width |
|---|---:|---:|---:|---:|---:|---:|---:|
| 220 L-BFGS | .9984432 | .9984432 | .9998304 | 107342.73 | .01376558 | .54126269 | 1.01267706 |
| additional 12 GN | .9974185 | .9991059 | .9996856 | 119346.88 | .01831703 | .54895059 | .99711406 |

The small positive sampled area ratios and extreme curvatures expose the near fold left in this actual connector by the coarse native training. Neither state gives a strong geometry candidate. All 4,291,840 G10 and 2,394,112 G11 scalar rows were observed independently of the sparse training, with the genuine same-input target and no guide suppression.

The source accompanying V52 has both solvers. Run `fit726 STATE192 STATE540 F512 A726`, `gn726 STATE192 STATE540 F512 A726 B726`, and `observe STATE192 STATE540 F512 A726` or `B726`. A726 SHA256 0133e459d6b2a341d6eebcb0faec238aad0e73a51b05e27bb118fdf6b16915bc, B726 SHA256 c1447e0113e79f45b33f7aecaf4d9229ee7551194563f4341ac9f220f2c40dcd, each generated JSON with final LF.
