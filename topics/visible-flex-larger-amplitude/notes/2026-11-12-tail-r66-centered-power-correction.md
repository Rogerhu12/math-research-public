# Same-candidate centered-power correction

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

## What the completed computation proves

Session 24039 completed the prepared six-case, two-representation diagnostic with tool and wait4 exit code 0, wall time 3.654759407043457 seconds and peak RSS 31696 KiB. It uses the original segment 7 candidate, positive integrals, physical endpoint two-jets, complete mean root, and every finite residual mode through 80. Its primary package is `2026-11-12-tail-outer-seg7-part0-quartic-diagnostic-r1.json.gz`.

At $x=1/256,3/512,1/128$, the full-angle physical Darboux upper bounds are respectively less than $0.000568380$, $0.000711283$, and $0.000772304$. These three points do not bound the interval between them. The complete interval still had upper bound $0.760858$ in both requested representations. The normalized quartic coefficients themselves are narrow, and the actual point derivatives $k_{2,x}$ are approximately $1.093713\,10^{-5}$, $3.730692\,10^{-5}$ and $7.729353\,10^{-5}$.

## Exact implementation issue and scope

In the installed python-flint interface, an expression `delta**j` invokes a power operation which returns `nan` for a signed interval crossing zero, even when the Python value `j` is an integer such as 1 or 2. The first helper `tail_outer_centered_quartic_fields.py` used that expression after centering a positive-width interval, so its proposed tighter polynomial range was nonfinite.

The existing helper `intersection(a,b)` evaluates

```python
lo, hi = max(a.lower(), b.lower()), min(a.upper(), b.upper())
return lo.union(hi)
```

Here the first argument was always the original finite five-basis enclosure. With `b=nan`, both comparisons with that second argument are false in this runtime; `max/min` therefore retain the finite first argument. The returned hull is an outward enclosure of the **original** finite interval, rather than an invalid narrower interval. At an exact point the centered displacement is zero and the original point computation is finite. This explains why the stored finite bounds and their full mean/domain checks remain valid, but does not license a claim of centered tightening in the first execution.

The original 1740-interval segment audit, 7563-interval complete-cell composition, exact stream checks, and all executable/primary files are retained. The note and manifest are corrected to distinguish the mathematical centered-polynomial identity from the implementation actually used. No state, metric, mode, endpoint, mean condition, or acceptance criterion changes.

## Replacement

The independent v2 helper evaluates the shifted integer polynomial by Horner multiplication and addition, uses repeated multiplication for its integer shift powers, and checks finiteness before any intersection. This preserves the exact R48 quartic and its actual derivative. A nonfinite replacement enclosure now raises an error instead of silently falling back. New targeted and whole-segment outputs use fresh names and are not inferred from the old data.

The next calculation first compares the same six subsets with this finite implementation. Only a complete covering run may replace the whole-segment bound. Even a smaller continuous candidate residual still needs the outer Green/Schur existence estimate; it is not a certificate of an exact outer solution or of principal curvature.
