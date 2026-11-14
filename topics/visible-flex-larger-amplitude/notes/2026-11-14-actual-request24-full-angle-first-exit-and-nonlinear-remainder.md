# Actual request 24: full-angle first exit and nonlinear remainder

## Actual run and byte identity

The public repository's request 24 completed successfully on source
`ae319f7544b3c94b5dbcb5290557ed04b66641eb`: run `43606770409`, job
`132483017505` (`Mainline angledomain`). The diagnostic finished at
2026-11-14 14:49:16 UTC. Its producer was the unchanged
`geometry_20261114_full_angle_domain_direction_probe.py`, SHA256
`794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8`.

The complete artifact `14119155118`,
`visible-mainline-angledomain-43606770409-1`, is 5,608,313 bytes; the downloaded
ZIP SHA256 is
`c4c59d92d121ed060ae7575baffdaf1b772f46a4948b7f7bc7e2a91b279a7cd0`.
The numerical diagnostic itself reported 1.571898049 seconds. This is a
successful diagnostic, not a newly accepted BVP or warm field.

The saved base remains request 20's complete warm, SHA256
`0036063ff99e7b3624e494b29430b9a3a8ec3eaae15f277447efcc71b8cc5e71`.
The exact request 22 direction has SHA256
`9a5916d9419df61ade98d89a917ef6778ac1d75b42977ce3ed110ec123a58873`;
its model has SHA256
`a5120beeac90342fdfd0f1596caa6b0549bb19bb459c5ec6b9ed5c9e6c85083d`.
The producer also checked the original accepted96, prepared699, true T112
zero-J anchor, configuration, original22 domain rows, full source ledger,
and the original22 accepted warm. The latter's complete 699 states were
reconstructed **numerically entrywise identically** from the base and the
saved direction at alpha `2^-9`.

## What was actually evaluated

For intervals 473, 475, 477, 479 and 480, the diagnostic used the original
left RMS fraction `0.17267316464601146` and **all 2,048 original uniformly
spaced physical-phi angles** at each query. It retained all physical,
core and scalar-control direction entries. Nine distinct original mesh
nodes supply the two-endpoint Hermite chains.

It evaluated the actual nodal RHS and its full saved-direction complex
derivative, then the complete Hermite query and original beta-squared
expression. The formula from R262 independently supplied `Bz`. Every
original22 alpha from 1 through `2^-9` used fresh trial nodal RHS values.
No LSMR, new full collocation Jacobian, full BVP or native tail was run;
no warm was created. The other original node, midpoint, RMS and rho gates
were not replaced or declared revalidated by this local diagnostic.

At the base, the selected nodal RHS values equal their saved values
entrywise. Across the five queries, the independent original-expression
complex directional derivative and the R262 full-angle formula differ by
relative maxima between `2.648271825674784e-13` and
`5.518825745088542e-13`. This check uses the **entire actual22 direction**;
it is distinct from the earlier operator check that tested only global
controls and free inlet core. The separately combined Hermite direction
differs from the spline form by at most `4.0149361699853836e-18`; the
complete complex query check differs by at most `2.710505431213761e-20`.
Every previously reported original22 bad query is replayed with difference
zero at its reported angle.

The three protected-row actions remain near zero, with differences between
the full-angle chain and the saved covectors at most
`2.831864137717993e-12`. These are readout comparisons, not newly imposed
acceptance thresholds.

## The nearest failure is predicted by the missing angular inequalities

For each query, the first positive zero of the linearized margin is
`min(-beta_squared / Bz)` over angles with `Bz < 0`:

| Interval | Original angle index | Base beta squared at that angle | Bz | First linear exit alpha |
| --- | ---: | ---: | ---: | ---: |
| 473 | 22 | 0.15118983360267868 | -17.313245852102384 | 0.008732610562699274 |
| 475 | 0 | 0.6586720634968625 | -28.372586396131837 | 0.02321508706681257 |
| 477 | 0 | 0.6006901992479723 | -34.32953602387089 | 0.017497766320823126 |
| 479 | 0 | 0.6124343859212082 | -25.588414278565807 | 0.023934049967067137 |
| 480 | 2037 | 0.029958340828950325 | -12.617821258570533 | 0.002374287938862774 |

The interval-480 first exit lies strictly between the original accepted
`2^-9 = 0.001953125` and rejected `2^-8 = 0.00390625`.
At `2^-8`, the four actually negative grid angles are exactly the four
linearly negative grid angles. At the actual minimum, index 11,

```text
base beta squared                 0.029958340829104535
linear change                    -0.049288364291293386
linear beta squared              -0.01933002346218885
actual beta squared              -0.016337963638822117
actual - base - alpha*Bz           0.002992059823366734
```

At `2^-9`, interval 480 is positive at every original angle: its actual
minimum is `0.006012562494966844`, with linear value
`0.0053141586833047524` and remainder `0.0006984038116620919` at that
same minimum. At `2^-7`, eight angles are actually negative, all within
the twelve linearly negative angles. These observations identify the
nearest rejected step's missing angular inequalities; they do not indicate
failure of the three protected point derivatives.

## Larger steps also have genuine nonlinear loss of domain

At alpha `2^-6`, intervals 475, 477 and 479 are linearly positive at **all**
2,048 angles but are actually negative at respectively 6, 10 and 2 angles.
The following values compare the linear and actual expressions at the
same actual minimizing angle, not two separately chosen minima:

| Interval | Actual minimum index | Linear beta squared there | Actual beta squared | Nonlinear remainder |
| --- | ---: | ---: | ---: | ---: |
| 475 | 0 | 0.21535040105730252 | -0.10761484701916246 | -0.322965248076465 |
| 477 | 1013 | 0.10916480069428447 | -0.10410061929359093 | -0.2132654199878754 |
| 479 | 0 | 0.2126154128186175 | -0.022616961872942376 | -0.2352323746915599 |

Interval 480 at this step has 28 actually negative angles, including four
that remain linearly nonnegative. Consequently, a full-angle linear
feasibility model still needs a positive margin reserve and the unchanged
actual nonlinear backtracking/domain checks. Linear feasibility alone
does not license a unit step or certify the angular continuum.

## Actual R263 fixed-model posterior

Unlike the original22 producer, this Actions diagnostic explicitly
computed and saved the R263 posterior from the pinned original model:

```text
lambda                                      270
unpreconditioned projected KKT norm          340.3776142312528
preconditioned normal residual                2.6032267432266403e-5
Delta = -b^T Az - (||Az||^2+lambda^2||z||^2)/2 0.535027165933812
E = ||P g||^2/(2 lambda^2)                    0.7946290827829872
E / Delta                                    1.4852125898992021
direction-error upper bound                  0.004669103075874524
```

These are posterior bounds for the **fixed damped tangent model**. They
neither certify the nonlinear BVP nor attribute the observed angular
failures to the truncated inner solve. The small preconditioned normal
and much larger unpreconditioned KKT norm remain different quantities.

## Preserved outputs and next use

All angles, all ten original trial margins, all first-order derivatives
and all pointwise nonlinear remainders are in the five compressed query
files. The principal file identities are:

| File under `full-angle-domain-direction/` | SHA256 |
| --- | --- |
| `summary.json` | `5abd72edf5131fc15664bb8f7a94f9c07b8a6859f2cffdd9c37cae06ff413f7d` |
| `intent.json` | `780bd0788558312c97640b06f824ea3b52248749f5554b40ec2bbe5d68b82f61` |
| `interval-473-all-original-angles.json.gz` | `4b59f665c153418b880e27f6f3de8df7704876e835cbde17f1721bbb7e06f9f3` |
| `interval-475-all-original-angles.json.gz` | `dbce0ae8b5ccfd77182e57da826e61b19e1fdbbd82c816a771020c572812b81e` |
| `interval-477-all-original-angles.json.gz` | `63c532404ce1dd056b550791696375ea5411db3090405ad18372e5e3e4ad5c70` |
| `interval-479-all-original-angles.json.gz` | `c27de4a6ce5ea8f4e02a05e62dd924ef5d9e85b6ec8b4b60f366f67175be0567` |
| `interval-480-all-original-angles.json.gz` | `0405a358d7f13ce98d684cdec48cab3d0096b352f6bcd5485fecd18dced21662` |

The evidence supports using all `5 * 2048` selected angular inequalities
for the next direction rather than protecting another single angle.
A feasible projection of an LSMR direction is an algorithmic candidate;
it is not the R265 constrained-model optimum. Any such candidate must be
checked against the complete original residual action, actual directional
descent, real merit change and every original domain gate. The latest
actual warm remains the request22 warm; this diagnostic does not advance
it or supply an accepted nonzero native tail.
