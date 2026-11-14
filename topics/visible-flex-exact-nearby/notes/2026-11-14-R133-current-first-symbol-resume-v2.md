# Current first-symbol finite part: exact continuation after the actual cache-floor gate

The genuine public run `43589646508`, attempt 1, returned code 1.
Its original failed native and partial checkpoint have the same SHA256
`5167e64ff6076e0100fa1c643b7168ce889b2fe4f6dab034631ce8d7115f0e1d`.
They were published at
`409ca5fdf95b9b9d7eda5eee7c6770698869c24b` under
`notes/first_symbol_finite_part_ci/run-43589646508-1/consumers/`.

The report contains 2,838 actually accepted strict integral cells,
covering exactly
`[0,136414032713052333/576460752303423488]`. The complete saved
integral interval is
`[67.906600932631739994689160765352515,
  67.906600981862047436439103874596274]`, with the extra directed
decimal rounding radii kept in its native records. It also contains
both successful directed root Newton steps. Neither is a complete
finite part, and the original failure remains a failure.

The last rejected cell repeatedly split its own radial allocation.
Its Taylor remainder eventually fell below `6.374e-47`, while the
remaining point-jet interval width still exceeded that local
allocation. Shrinking the cell further cannot eliminate a fixed
point-jet enclosure floor. The existing total accepted width was
less than `4.924e-8`, so the original uniform radial allocation had
not exhausted the whole target width `1/1000`.

## Exact continuation

`scripts/fourfold_codazzi_current_first_symbol_resume_v2.py` imports
the unchanged original integrator, SHA256
`c866d7d0f75a36d969d291c4379be34df1b1634a5234875d40819baf555c9a7f`.
It checks the original native's hash, candidate, continuous-centre
definition, source, run, exact cut and declared whole width. It then
checks every original cell's chronological coverage and candidate
piece and retains the original aggregate interval. All 2,838
integrals are reused; none is reintegrated. The two actual root
steps are checked as the same nested certificate and reused
without another root iteration.

Only the two remaining original scalar germs are opened for new
integration. The actual remaining scalar/candidate intersections
receive equal shares of `width_goal/4`. Binary children split their
own share. The original prefix width and the actual cumulative new
width are also checked against the whole strict allowance. The final
unchanged full-width gate remains `1/1000`; no result threshold has
been relaxed.

At a newly needed strict midpoint, first use the original cached
true jets. If their propagated point interval would use more than
one quarter of the cell's allocation, evaluate **only that point**
with the same complete `FullArbScalarTarget` at the same intrinsic
object, eta0 and nu0. All infinite angular exponential tails are
paid by that provider. Its exact scalar germ is checked against the
original row. The saved complete whole-cell sixth-derivative bound
is retained for the integral Taylor remainder. Using a tighter
enclosure of the same true midpoint and the original whole
derivative bound is an ordinary rigorous Taylor integral; it does
not change the scalar model's mathematical object.

Each fresh point stores its complete K/beta/gamma/s jets, Xi jets,
actual scalar germ and complete provider tail metadata. The public
child declares at most 512 such new points; if this finite resource
budget is insufficient, it preserves the actual prefix and fails.
It never replaces all 169 original germs or repeats a completed
successful integral. The final root finite-part calculation is the
same original exact subtraction and derivative-tail formula.

This continuation remains at explicit-family delta=0. It evaluates
the strict-symbol finite part, not the complete returned beta, the
unknown R31-selected delta, a true PDE solution or a whole inverse.
Actual execution, success or failure will be recorded by the new
public process; no local numerical replay is used as evidence.
