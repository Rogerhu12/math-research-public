# Physical-bump joint01: actual closure and two representation defects

## Actual run and scope

The run `15035`, completed transport chunk `920b28`, naturally returned 0. The observed child receipt records return code 0, UTC 2026-11-12T12:01:32.513272 to 12:06:14.646164, elapsed 282.132926 seconds including process setup. The mathematical driver saved 40 actual accepted states and its final field. It did **not** reach its finite tolerance: the final original raw infinity norm is 0.3887710558906947, full sampled Gauss 0.979472309857501, formal principal curvature 7.229798317173662, and central gap 0.8999999827759104. There is no whole metric, geometry or strong-target completion claim.

The owner stop file was written only after this process had already naturally finished. It was not consumed: `owner_stop=false`. The exit must not be relabelled 130. The final accepted entity is `accepted-0040.npz`, SHA256 `1b029c98ec1734120fc74294a4504abd6f3b78a7e3353778307d6ca185e30fe6`. Intermediate accepted entities remain local; the progress records their SHA values.

The actual finite parameters are central c(15), positive-Bernstein tail b(16), and physical radial bumps delta(7), with base T=.02. Changing delta changes g. The finite objective was original raw F plus curvature guidance and the omitted angular Gauss rows. Full angular Codazzi was measured only after this run and is not a success condition silently retrofitted to its earlier reports.

## Near-coincident computational nodes

The computational interval at cell 56 is [0.5799999999999992, 0.58], with actual binary64 width 7.771561172376096e-16. One endpoint is an accumulated physical knot, the other the nominal angular-blend knot. The physical segment formulas themselves remain unchanged. Raw Codazzi divides correction differences by this tiny h. At accepted16 the n mean residual on this cell was 1.20692858024. At accepted40 the largest m coefficient residual is still 0.1216115711433946 on the same cell.

The independent l field has no separate radial differential equation. At accepted40 the largest coefficient jump across that cell is 0.02979255768238742, in l, column 34 (the l mode 6). The n/m coefficient jumps are at most 2.6646e-15/2.3870e-15. Deleting the nearly duplicate node therefore changes this provisional P1 field by more than roundoff, despite a radial displacement below 8e-16. The clean conversion measures and preserves that fact; it does not claim bytewise field equivalence or an unchanged finite equation.

The new separately named provider coalesces adjacent computational knots within 1e-12 times max(1,end), retaining the last member and both domain endpoints. It records every cluster, original/new meshes and the maximum displacement. It never edits the target profile, physical segment list, compact supports or angular chart. This case has 100 to 99 nodes, with new minimum cell 0.0012500000000000844.

## Central seed lifting

The old exact seed multiplier was wc(s)=1-S5(s/.55). It therefore decayed inside the exact central cylinder [0,.32], although the cylindrical solution contains its entire central n function. At K15 and the actual 256-point angular grid, max|seed-EPE(seed)|=0.026389853418673948. The old weight at s=.32 is 0.3493074526702722. Its derivative alone forces an omitted central Codazzi term with sampled angular maximum 0.089965409381843, attained radially at s=.275. This is a finite angular diagnostic, not a continuum bound.

The new declared multiplier is wc(s)=1-S5((s-.32)/(.55-.32)), clipped outside that interval. It is identically one on the whole exact cylinder, and has zero first and second derivatives at both ends. The tail lifting is unchanged. The old correction is first evaluated as its actual P1 field on the new mesh, then the retained Fourier component of (wc_old-wc_new)seed is added. All 38 parameters are unchanged. The omitted seed component remains part of the actual changed field: its maximum sampled node change is 0.019304784994817737. This is an initialization representation change, not a nonlinear solution or a same-discretization refinement claim.

## Closed evidence and continuation

`2026-11-12-fd2d-raw-bump-clean01-report.json` contains the final old and new residual peak locations, actual same-target/chart comparisons, full angular Codazzi measurements, conversion definition and mixed analytic JVP. The clean check naturally returned 0 (`49493`, chunk `5d3f29`): target a,a_s,a_ss,c,K and all angular chart quantities agree pointwise exactly on its comparison grid; the mixed state/central/tail/profile raw+fullCod JVP relative L2 discrepancy is at most 8.60e-10. The old source and old reports are unmodified.

The next run `joint02` uses this explicit clean warm field, K15 unchanged, and adds the actual omitted angular Codazzi rows to the guidance objective. It saves all accepted states separately. Its active files are not included in this closed group. Final continuous residual, actual reconstructed geometry, matching, refinement and closed-surface obligations remain open.
