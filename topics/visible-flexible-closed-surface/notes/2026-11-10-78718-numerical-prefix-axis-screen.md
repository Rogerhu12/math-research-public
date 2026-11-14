# Early exact axis screen of an actual prefix base

2026-11-10, Astra-visible-flex-78718bd0. This prepares a necessary-condition
calculation for the first real inner candidate. It executes no DN, ODE or
geometry producer, and has not yet been run on a future candidate.

The actual entry is `scripts/78718-prefix-nodal-axis-screen.py`. It reuses
the exact nodal algebra of `78718-prefix-nodal-axis-lower-v1.py`, whose
mathematical proof is already in [R78](../results/R78-m14-prefix-exact-axis-metric-lower.md).
It removes that older command's requirement to first produce a full
continuous metric certificate. That certificate is not an input to the
pointwise algebra. The saved Cartesian base and its ordinary lossless storage
parts are the only numerical inputs. Source and input identities are recorded
for reproducibility; no separate approval or source-freezing stage is added.

## Exact statement

Write the actual finite Cartesian map in cylindrical coordinates as

\[
Y=R(s,\psi)e_r(\psi)+T(s,\psi)e_\theta(\psi)+Z(s,\psi)e_z,
\]

where `R` and `Z` have cosine modes `3j`, and `T` has sine modes `3j`.
At either `psi=0` or `psi=pi/3`, all sine factors vanish, so at a saved
shared-jet node

\[
E=|Y_s|^2=R_s^2+Z_s^2.
\]

The shared Hermite definition uses the saved binary64 nodal jets as exact
rational constants. The sums for `R_s,Z_s`, their squares and `E-1` therefore
use `Fraction` arithmetic; no floating evaluation of a polynomial, trigonometric
function or BVP velocity enters this witness.

For the frozen prefix target

\[
g=ds^2+a(s)^2d\Theta^2,
\qquad \Theta=\psi-e(s)\sin(3\psi)/3,
\]

`Theta_s=0` at either axis, and hence `g_ss=1` exactly. The relative symmetric
metric operator consequently has the Rayleigh lower bound

\[
\big\|g^{-1/2}(Y^*e-g)g^{-1/2}\big\|_{\rm op}
\ge \frac{|(Y^*e-g)(\partial_s,\partial_s)|}
          {g(\partial_s,\partial_s)}=|E-1|.
\]

The program evaluates both axes at every interior saved node before the
prescribed common-cut correction support and selects the largest exact
value. Its target identity is the fixed flat-profile/chart pair in the actual
base metadata. A small result does not prove an upper bound: off-axis points,
between-node points and other metric components are not covered.

## Scope of the later common map

For the default width `.15`, the support start is computed using exactly the
producer's binary operation `searchsorted(mesh, mesh[-1]-.15)`. If that common
map is subsequently constructed from this same base with the same width,
its added jet correction is zero strictly before this node index.

This locality alone does **not** transfer the target metric. The exact bridge
may change the target radial coordinate. As [R81](../results/R81-actual-common-prefix-exact-metric-lower.md)
shows, the needed lower bound then involves the new graph's own factor
`lambda^2 E-1`, with its certified lambda enclosure and the appropriate sign.
The screen deliberately sets `new_exact_bridge_target_transfer=false` and
`complete_closed_graph_rejection=false`. A frozen-target excess is an early
diagnostic of this prefix and cannot by itself reject the eventual exact/common
graph. No old lambda value or old strict point bound is copied.

The output includes the exact rational witness and enclosing binary64
endpoints. For prose it additionally supplies a downward decimal rational on
a `10^-24` grid. This is proved directly by integer division, so it avoids
the roundtrip-string problem found in the older common-point display.
The exact rational, rather than any display string, is compared with
`1/500000000`.

## Actual invocation after a base exists

Run from the topic directory, using a new report path:

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-prefix-nodal-axis-screen.py \
  --geometry notes/2026-11-10-78718-numerical-fast07-inner-0001/prefix-base.json \
  --out notes/2026-11-10-78718-numerical-fast07-inner-0001/prefix-axis-screen.json
```

The indicated base is a future producer path, not an assertion that it exists.
The raw CP entrance and Cartesian entrance tools remain separate. This screen
uses the same actual Cartesian base intended for subsequent full-domain
metric certification; it does not replace that certification or change any
solver input. Source syntax was checked by actual tool `21dea5`, exit 0,
with zero geometry reads and zero mathematical solves. The storage reader
interface and original shared-jet source were read directly before wiring it.

One inexpensive actual replay then checked the executable wiring using the
already saved M14 base, not any new candidate. Tool `9cdf74` started the
read-only calculation (session 89485); tool `1bc314` observed natural exit 0.
It took 2.376 seconds, evaluated 12,246 exact points, and recovered the same
native node 1518 / axis pi/3. Tool `a24df0` compared all eight original exact
witness fields and found each equal to the old R78 report, including the full
Fraction lower. No continuous certificate was supplied to the new command.
The report is `2026-11-10-78718-numerical-prefix-axis-screen-oldbase-01.json`
and the real completion record is its `-observed-exit.json` companion.
This replay made zero ODE, solver or geometry-producer calls; it does not
transfer the old witness to fast07 or to a new common target.
