# Actual finite check of the angular Gauss complement

The root-owned helper scripts/fd2d_gc_gauss_complement.py was checked without
editing it. The checker is scripts/fd2d-metric-gauss-complement-check.py.

At the selected finite angular grid, with the existing even basis E and
projection PE, define \(P_h=I-E\,PE\). The added rows are
\[
 w\sqrt{2/N_\theta}\,P_h(nl-m^2-K_g)
\]
at each noncut radial node. The original projected Gauss and Codazzi
residuals remain separately defined and unchanged.

For independent field variations, the pointwise derivative is
\[
 l\,dn+n\,dl-2m\,dm-dK_g.
\]
State columns use the existing even/odd basis values. Tail columns use the
complete exact lifting parameter derivatives. The physical T column uses
the new analytic fields_T and K_T from the closed analytic provider; it
does not choose a finite step from the distance to the physical boundary.
The central parameter columns before boundary elimination are zero.

An angularly constant K_T lies in the retained exact Fourier space. The
checker nevertheless measures the difference caused by dropping that
constant through the actual floating projection matrices. It also measures
the retained projection of the supposedly omitted rows, rather than
declaring floating orthogonality exact.

The first invocation actually exited 1 in session 17081, chunk cac016:
the newly published input NPZ was temporarily absent while the source
checkout was being rebased. It failed before any JVP computation. The
failure receipt records that FileNotFoundError and does not classify it
as a mathematical defect. The parent subsequently stabilized the source
tree and moved publishing operations to a separate worktree.

The same actual input was then genuinely rerun under a new output name.
The final report is
notes/2026-11-12-fd2d-metric-gauss-complement-check-02.json.
It completed with exit 0 in session 75915, chunk fe2232, in 22.13 seconds.

All three tested directions were nonzero. At centered step \(10^{-6}\):

| Direction | Norm of the analytic direction | Norm of the difference divided by max(1,norm of analytic direction) |
| --- | ---: | ---: |
| all independent node fields | .05282242260 | 2.608436902e-9 |
| exact tail controls | .04980595512 | 1.196766033e-9 |
| physical T | .09373212636 | 2.127566898e-9 |

The denominator convention is stated explicitly because these direction
norms are below one. The corresponding relative errors against their
own nonzero norms are approximately 4.94e-8, 2.40e-8, and 2.27e-8.

The original F and complete independent fields were unchanged exactly
in floating comparison. The helper source bytes were unchanged throughout
the run. The retained projection of the omitted residual was at most
3.185e-15, and the floating effect of omitting angular-constant K_T was
6.218e-15. These are recorded numerical limits, not exact zero claims.

This checks a finite-grid search helper. It does not certify angular modes
beyond that grid, any continuous radial residual, or the geometry of the
supplied initializer. No body integration or BVP was repeated for this check.

