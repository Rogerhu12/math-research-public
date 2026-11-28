# Actual M32 recovery interruption, now with a complete nodal checkpoint

The independently versioned fixed_support_literal_driver_v2 process, tool session15071, returned exit137. It did not return a solve_bvp result, physical field, or metric audit. Its incomplete run record is retained with solver_success=false and finite_linear_candidate_pass=false. This is another interrupted numerical execution, not a solver acceptance or a mathematical nonexistence result.

The existing preparation was resumed by its explicit resource gate; the midpoint initializer was not recomputed. The original fixed metric, lambda .002, delta .06413464112662924, q gauge .06, warp_reference_q .06 (actual warp_e .48), mean1168, q branch and all original nonlinear gates remained unchanged.

The first actual adaptive round used1273nodes and printed RMS6.55e-7 and boundary7.70e-12. It did not meet the original requested tolerance2e-7 and added224nodes. The1497node round then completed two full Jacobian/factor pairs and further original Newton trials. A subsequent same-grid nodal and midpoint Jacobian returned, but no following full factor-start event or adaptive RMS return was recorded.

Across the recorded execution there were three completed full QR factors and14complete linear solves. The last full system had145241equations with97states per node and32parameters. The maximum recorded RSS was2756464KiB. The largest directly reported original-matrix residual maximum was below1e-18; the adjacent JSON records every aggregate directly from the event files. Such linear solves do not imply nonlinear convergence.

The resource changes did execute: the obsolete factor was released before a complete Jacobian rebuild, and the independent solve wrapper avoided the earlier factor-reference cycle. This does not by itself exclude another transient memory peak. The post-exit global oom_kill counter read6; there is no immediate prelaunch counter baseline or kernel record naming this PID. The observed exit137 and source/last-event identity are recorded, while its specific cause remains unproved.

## Complete unaccepted state retained

Before the last full-J construction, v2 atomically wrote a separate1497node checkpoint. It has x shape1497, y shape97-by-1497, p shape32, pscale shape31, endpoints exactly0 and1, and finite entries throughout. Its NPZ SHA is

5a28d53fb0bb8e8921574fec93ac82f0c11e133715ad525908c634fec4123af0.

The independent metadata hash matches that file and labels it unaccepted_complete_nodal_before_original_J. The subsequent1496midpoint Jacobian did not overwrite it. Its actual q value is .060000491077815986, with p0=8.184596772498105e-6. These are the latest saved full original unknowns, not an accepted solver return.

A later recovery can therefore retain these exact saved nodes and all components directly; it need not infer nodal coordinates or states from midpoints again. It must still reconstruct the same original frozen problem, treat this field as unaccepted, execute the original nonlinear solver and off-midpoint RMS tests, and complete the original metric audits before promoting it.
