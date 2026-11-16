# CAP5: one startup repair with the completed prefix retained

Date: 2026-11-16. This addendum continues the exact bounded question in
[the original design](cap-five-positive-curvature-search-design-20261116.md).
It does not open a second 120-second or 400-integral allocation. Sources,
parameters, identities, and this explanation may be published; original
numerical payloads remain in public Actions stdout and runner temporary files.

## 1. Actual failure and what was already paid

The first run was 43831664308, job 133178210211, source
03bfffd120026aa5f25187dc0c0ec5c01705e709, using
`.github/workflows/visible-cap-five-positive-curvature-search.yml`.
Its original UTF-8 job log has 106370 bytes and SHA256
`0e78611cfb99dc2e6a9158991d920a3740185919bb25924c5a4865333fce2520`.

Integral 1 completed the genuine germ prefix on [0,1/32], including all eight
primitive coefficients and the three positive initial values. It used 63
quadrature callbacks. Integral 2, the first all-zero-parameter cap, failed on
its 14th ODE callback with `OverflowError('math range error')`. There was no
complete cap, no initial five-by-fifteen Jacobian, no fixed whitener, and no
optimizer start or refinement to reuse. The last finite stage was
y=5/128: the automatic startup had tried the full original maximum step
1/128 from y=1/32.

The authoritative original clock, sampled after its final result output,
was **0.5630522320000182 seconds**. The cumulative original account is
2 integrals started, 1 completed, 1 failed, 14 ODE callbacks, and 63 prefix
callbacks. All six original records and the failure remain part of the
observation. Their CAP5_RECORD output occupies 8431 bytes of the original
3,000,000-byte soft allowance.

## 2. The one numerical repair

Every new DOP853 cap integration, including a necessary final refinement,
receives the explicit original-coordinate initial step

```text
first_step = 1e-6
```

The method, relative and absolute tolerances, maximum steps, analytic
sensitivities, endpoints, positive log coordinates, and objective are
unchanged. At the starting germ point, the exact log derivative of U is

```text
(log U)'(1/32) = 6094848/3969 < 1600.
```

The other positive log-state rates are obtained from the same exact germ
and have the same small initial length scale. All fifteen parameter bumps
vanish on [1/32,5/128]. Thus this startup correction concerns the shared
known germ, not a parameter-dependent new family. The explicit first step
limits the initial U log increment suggested by this rate to below 0.0016,
instead of the unstable full maximum-step trial. Subsequent step acceptance
is still DOP853's original adaptive procedure.

This is an actual failure repair, not a proof that all later stages will
succeed or a rigorous error enclosure. No exponential clipping, state
projection, target alteration, artificial residual, jitter, fallback
solver, new start, or hidden retry is introduced. A later exception is
reported as a failed started integral and ends the same attempt according
to the original exception path.

The three raw log coordinates are now saved before their exponential is
evaluated. A later overflow therefore retains the actual offending stage;
it is not converted into a finite value.

## 3. Literal restoration of the completed prefix

The continuation imports the existing read-only stdlib Actions reader.
Before scientific imports it reads the original failed run/job metadata,
the small original request at the original source commit, and that one
original job log. It checks the failure status, run/job/source/workflow
identity, complete raw-log byte count and SHA256, all six record numbers,
and these literal JSON-plus-newline records:

| Original item | Bytes | SHA256 |
| --- | ---: | --- |
| PREFIX_COMPLETE, record 3 | 655 | d1bd2dca8e358f526f9fd904fe37e79c6d651c00ac36e502712b8c98c4015c76 |
| INTEGRAL_FAILED, record 5 | 854 | 37a2d67d6536a04d4cfb87e59cfd03a83c83e5b4e57dc64f75af8addab85a7a3 |
| FINAL_REPORT, record 6 | 4837 | 858e14bf1727a21e3740e54140158f642339ce4e1b04066cf0218174884ca6b6 |
| CAP5_FINAL_CLOCK | 333 | a4ec5d0df80d2f929bae363319c95095d744989a4a329d9af06dbf4ae688b4ef |

The original request is 6143 bytes, SHA256
`353d61eae47e5763176eee3dff13edd56b0e000660afe959cbbe44f799d85c8f`.
Its schema, entry point, limits, dependency pins, family, six starts,
mathematical sources, and classification are compared field by field with
the continuation request. Only the continuation source/receipt/interface
fields differ.

The eight completed coefficients, their recorded estimated error, and
U,v,v' at 1/32 are copied from the original FINAL_REPORT and compared
exactly with PREFIX_COMPLETE. They are not regenerated, re-integrated,
rounded into source constants, or silently replaced by a formula.
The prefix quadrature function and quadrature import are absent from the
continuation. The restored prefix is emitted with its source receipt.
A changed or incomplete receipt prevents all new scientific calls.

The complete family, all twelve density terms, endpoint normalization,
five residuals, fifteen sensitivities, box [-6,6]^15, fixed six starts, and
all later optimization decisions retain the original definitions. The
newly completed all-zero cap is still the first source of the original
fixed preconditioner. No unfinished state from the failed integral is
treated as a complete cap.

## 4. One cumulative account

The continuation clock starts before every input read and scientific
import. The ledger is initialized immediately with the original elapsed
time and all original counts. Every check uses

```text
same_scope_elapsed = 0.5630522320000182 + current_process_elapsed.
```

The hard scientific stop remains 120 seconds; the search reserve remains
112 seconds. The original maxima remain 400 started integrals and 397
cumulative starts at the search cutoff. The next cap is integral 3. Record numbering continues at
7. The output allowance starts with the 8431 original record bytes already
charged. Restore time, metadata/log I/O, imports, failures, result encoding,
temporary output, and stdout serialization all consume the same remaining
time. Prefix restoration consumes no new integral or quadrature callback;
its wall time is fully charged.

FINAL_REPORT retains the original receipt, prefix, last successful or
failed stage, starts, refinements, and best complete candidate, if any.
CAP5_FINAL_CLOCK retains both current-process and cumulative counts.
Its authoritative combined clock is
`total_same_scope_seconds_including_carried`.
`entry_elapsed_seconds_including_output` is the new process duration only.
A receipt failure still emits the elapsed new cost and the carried account;
`carried_receipt_verified=false` prevents it being mistaken for a resumed
scientific result.

A result remains a bounded floating observation. A small residual is not
an exact zero, and failure of this family or budget is not global
nonexistence. There is no old psi3 E, self, rank, forcing, independent
development, or mother-installation rerun.

## 5. Publication and execution boundary

The entry remains
`scripts/literature_cap5_positive_curvature_search.py`; the request remains
`computations/request-cap-five-positive-curvature-search.json`.
Its source manifest binds the revised entry, unchanged original design,
and this addendum. The existing reader and workflow remain separately
source-bound. Public/private rule pulls, queue handling, detached-source
execution, and credential removal remain the workflow's responsibility.

This addendum and the source/request were prepared by static reading and
editing only. No local import, compile, development check, integral,
optimizer, symbolic computation, workflow, or numerical retry was run.
Only the parent may publish and trigger this single continuation.
