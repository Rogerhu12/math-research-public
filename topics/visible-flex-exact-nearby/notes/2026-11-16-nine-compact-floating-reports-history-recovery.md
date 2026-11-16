# 九份旧 compact-metric 浮点报告的完整历史恢复

## 0. 删除边界与原资格

这是根规15许可的派生报告普通清理，仅删除下表九个JSON，共337304B，不重写历史，不计算任何旧目标。公开仓库 `Rogerhu12/math-research-public` 的恢复提交为 `b1516ca01023ba29e939dbdf34f1eafc24dd5935`。每件都已完整读取UTF8并独立核字节、Git身份及SHA256；后继读取应从该不可变提交按原路径恢复整件并核表中身份，不调用原producer。下面的字段摘存只是索引，不是替代整件的科学输入。

所有九件明确 `certified=false`，`whole_affine_parameter_interval=false`、`whole_real_angular_circle=false`、`whole_radial_interval=false`。浮点finite成功与失败均保持：closed-waist m16只达到0.05、0.1失败；outer-mean m16达到0.65；m128 v13两个均失败、v14 alpha070成功但alpha075网格上限失败；bounded v7成功、v6失败、v7-b8网格上限失败。任何accepted中间checkpoint都不把最终失败改为成功。旧日志的success不构成连续PDE或固定metric族证明。

这些探索同时改变 `E_nu=E exp(nu*h)` 与waist补空间，原target和原waist都未固定；不转移旧g0/waist证明，不将变化的nu用于最终族IFT。只保原regular线性outer行，非线性tail、非第四角模费、mean height/flux仍未闭；相对mean是输出，未消去另一matching行。所有诊断/浮点小residual都不构成区间证书或不存在性定理。未删除任何source、candidate、guess、direction、native、原history对象或下列JSON所引用的内部对象；旧temporary scratch checkpoint路径只保原回执，不声称这些内部临时件仍可恢复。

当前WVC、WCTR、WEX input合同逐path排除这九件；新W2C同物理候选ac1d5b98的原五part与两native不在删除集合。WCTR43901776543/1正在首算，完整192000B pending以及120000B预留继续计入，清理不触发科学入口。

| 原完整路径 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-closed-waist-m16-floating.json | fed9e06149c6d17b3aad98c1aaa3a13e078ff7a3 | 35436 | 7ae394323db3a69e7b36d71246d3c2d73c8895e9018584361bfc1182cbd72a36 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-m128-alpha070-v13-core16-b1-floating.json | e70cdfdfebc0f00def8bcd1d6846bbf559c26f65 | 44699 | e10345b6dbdcb6fc3267ea4d2efe5b13361a4d02e5fdfcd581fd7704fe62a6fa |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-m128-alpha070-v13-core16-floating.json | 6b9c56da56af9910748630de76c4251c6b2e434b | 44341 | c6e3ab6a0da9e462c26c16579b48dd30c6882e929f5ff995abe598b3a6ed6ee2 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-m128-alpha070-v14-full-QR-floating.json | 5c3ef379c73c137938fb98d4cb279cd03328e143 | 27019 | dbe8b09bdd211c2eba28f6070e655421bd3b9ff208f7eec76e9e9f6a10e627b7 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating.json | 39d063a6a3b268a6d7d01701613e62e0ba5b8a14 | 47984 | dee77b0b93736bf80e51dec5d7f5469b848c3daa89f55151e272adcc1fbb9598 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-floating.json | b47a3715f053e16d2eab4f5a491af7af1454769f | 32418 | 5001d4c110bd402f0d500b86670ad81e7d5f072adaa46a1e10644753de2e9754 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-outer-mean-m128-v6-b2-n1024-floating.json | 91f01680610ba5de5ef329c9d33b7c4796ef667c | 29382 | 2200a575894cfcf66f46e48705422ca08b0048288a86f6b76541324dedff0235 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-outer-mean-m128-v7-b8-n1024-floating.json | ac6bc5dce8fbfc67721a5e5fb746f60dd1a608c3 | 25711 | 209f30a8d3ab4233e209eef5d31a5d25a4f41dc0edbdc58030305596d7489d88 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-R133-compact-metric-outer-mean-m16-floating.json | cd0ac81be9f9c49132f534e37482b10cdd8dfca9 | 50314 | cdcda6148f06bf47d59dab8e1e0cc3bd6f3d5054d1ec63d4c7d101f16a902461 |

以下25个顶层字段在九件原JSON中使用完全相同的原token，逐件机械比对一致；每件下一节的specific与省略字段身份共同覆盖原全部顶层字段。原数值token与格式原字保留，不做科学重新计算。

```json
{
  "coordinates": "B=alpha*b; C=Cref_nu+alpha*c",
  "normalized_state_order": "b sine k=1..M, c cosine k=0..M",
  "physical_frequency_factor": 4,
  "object_sha256": "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848",
  "new_metric_family": "E_nu=E exp(nu*h); a fixed",
  "exact_bump": "h=4096 t^6(1-t)^6 for t=(|r|-1/20)/(13/100) in (0,1), zero elsewhere",
  "original_target_fixed": false,
  "old_waist_branch_reused": false,
  "waist_nonmean_complement_allowed_to_change": true,
  "outer_boundary": "Complete retained R74 regular LINEAR stable-center rows; nonlinear tail terms unpaid.",
  "certified": false,
  "requested_interval": [
    "0",
    "25/8"
  ],
  "primitive_nodes": 512,
  "exact_center_parameter": {
    "numerator": "-7789843107295549",
    "denominator": "4611686018427387904"
  },
  "origin_sha256": "0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b",
  "direction_sha256": "8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab",
  "mean_retained": true,
  "regular_mean_height": null,
  "regular_mean_flux": null,
  "nonlinear_regular_tail": null,
  "whole_affine_parameter_interval": false,
  "whole_real_angular_circle": false,
  "whole_radial_interval": false,
  "scipy_version": "1.17.0",
  "scipy_collocation_module_sha256": "59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2"
}
```

## 1. 2026-11-13-R133-compact-metric-closed-waist-m16-floating.json

完整原件：35436 B；Git `fed9e06149c6d17b3aad98c1aaa3a13e078ff7a3`；SHA256 `7ae394323db3a69e7b36d71246d3c2d73c8895e9018584361bfc1182cbd72a36`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_compact_metric_normalized_Codazzi_branch",
  "modes": 16,
  "amplitude": 0.05,
  "nu": 0.0008183728052959186,
  "exact_float_nu": "3774078424044387/4611686018427387904",
  "source_sha256": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
  "mean_boundary": "waist",
  "finite_BVP_success": true,
  "reached_requested_amplitude": false,
  "requested_amplitudes": [
    0.0,
    0.025,
    0.05,
    0.1,
    0.2,
    0.35,
    0.5,
    0.65
  ],
  "angular_grid": 256,
  "diagnostic_angular_grid": 512,
  "tol": 2e-06,
  "max_nodes": 3500,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 1.1169088520440799e-10,
    "state_relative_errors": [
      1.0821745672150946e-10,
      1.1689628715987893e-10,
      5.6941134957200417e-11,
      3.453638265554034e-12
    ]
  },
  "seed_rhs_calls": 12059,
  "seed_waist_q": -1.2362284481249458e-08,
  "seed_message": "The solver successfully reached the end of the integration interval.",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-closed-waist-m16-candidate.npz.gz",
  "candidate_sha256": "866456fe908691b4570fdcda16bdd2e2b22d7b0b428bf1cf7d3ab4bad07e04f8",
  "failed_candidate_path": "notes/2026-11-13-R133-compact-metric-closed-waist-m16-candidate-failed.npz.gz",
  "failed_candidate_sha256": "3df99fd1d55dcfd555ddbc39d20cf3ecfc42c48545c27e614ed0ae8232ecbfe4",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Floating finite Fourier/radial boundary model, no continuous PDE or parameter certificate.",
    "nu changes the target on .05<|r|<.18; existing g0 proofs do not transfer there.",
    "The waist curve is also changed by the complementary C modes; old exact waist Cauchy branches are not reused.",
    "The selected mean boundary is explicit; the opposite mean is an output, not an erased matching row.",
    "Every nonlinear regular tail term, true non-fourth-mode linear fee, mean height and flux remain unpaid.",
    "The normalized alpha=0 result is a Jacobi eigenfunction; it is not a nonrotational nonlinear surface.",
    "Neither a guard stop nor a large residual is a mathematical nonexistence theorem."
  ],
  "wall_seconds": 222.8539691549995
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "attempts": {
    "bytes": 30982,
    "sha256": "e4c52619862396b502b9453c3ee06d2436dbe902ff805b1d8065053568824de1"
  }
}
```

原 attempts 全长 4。逐项的完整非数组向量资格与诊断如下；每项的省略原字段均有自身身份，完整attempts仍在原文件内。

### attempt 0

```json
{
  "amplitude": 0.0,
  "nu": 0.0009452572912028995,
  "exact_float_nu": "8718459667313915/9223372036854775808",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 753,
  "diagnostics": {
        "normalized_finite_residual": 1.1971291795720603e-05,
        "normalized_full_B_residual": 1.1971291813905882e-05,
        "normalized_full_C_residual": 6.187947248659231e-06,
        "normalized_A_projection_defect": 3.6637359812630166e-15,
        "C_min": -0.9356875460334886,
        "C_max": -0.1710388544245141,
        "B_abs_max": 0.0,
        "actual_full_B_residual": 0.0,
        "actual_full_C_residual": 0.0,
        "actual_A_projection_defect": 0.0,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 3009,
        "valid": true
      },
  "waist_mean_C": -0.9356875460334886,
  "waist_mean_closure_gap": 1.1102230246251565e-16,
  "waist_turn_number": 0.9999999999999999,
  "waist_total_turn": 6.283185307179585,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 3.03057137321371e-38,
  "maximum_boundary_residual": 2.5043805042641684e-26
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 2456,
    "sha256": "9e72a4737c4102b9841eeafc4076482a5623111c8b26ca93c70649dc5b1a6146"
  },
  "waist_B_coefficients": {
    "bytes": 221,
    "sha256": "989471b5ecb605aaa3da5d4cfa2f29a10162c9408255924c816e61f5fd6e3440"
  },
  "waist_C_coefficients": {
    "bytes": 258,
    "sha256": "d589d283bb4ca6bb469aab3059546c3f6c09e26611e303f2e8750a4d9c659687"
  },
  "outer_B_coefficients": {
    "bytes": 228,
    "sha256": "ab903bca479a72fb9851561059c64085c26756b44f521fd54604cab71b850bec"
  },
  "outer_C_coefficients": {
    "bytes": 251,
    "sha256": "43c6699c9a48304cb45671fb188ae9492add56c7f07ef723dde1c72350f05299"
  }
}
```

### attempt 1

```json
{
  "amplitude": 0.025,
  "nu": 0.0009135532203270249,
  "exact_float_nu": "8426041226542911/9223372036854775808",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 769,
  "diagnostics": {
        "normalized_finite_residual": 1.3206105712887747e-05,
        "normalized_full_B_residual": 1.1973424847683267e-05,
        "normalized_full_C_residual": 1.320610571475811e-05,
        "normalized_A_projection_defect": 3.3306690738754696e-15,
        "C_min": -0.9613829725845606,
        "C_max": -0.17198594019001662,
        "B_abs_max": 0.015924549433897414,
        "actual_full_B_residual": 2.993356211920817e-07,
        "actual_full_C_residual": 3.3015264286895276e-07,
        "actual_A_projection_defect": 8.326672684688674e-17,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 3073,
        "valid": true
      },
  "waist_mean_C": -0.9356875460334886,
  "waist_mean_closure_gap": 1.1102230246251565e-16,
  "waist_turn_number": 0.9999999999999999,
  "waist_total_turn": 6.283185307179585,
  "outer_C_mean_minus_reference": -0.012656667455076306,
  "normalized_outer_regular_linear_residual_l1": 4.6029725670854937e-32,
  "maximum_boundary_residual": 1.232595164407831e-32
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 4685,
    "sha256": "6d6e4da6b3d2182755751b3508762f91a8b6572d29d2dcc0e55769dae72c73f2"
  },
  "waist_B_coefficients": {
    "bytes": 389,
    "sha256": "25d5ab97652fe6071a65fed880a13bd13b05e41a1315cf1ecc3ef81b05239936"
  },
  "waist_C_coefficients": {
    "bytes": 534,
    "sha256": "2ded9780e37a536a7f0f12e15995370035ca86bcf1319a1f7a9ff5e39155c53b"
  },
  "outer_B_coefficients": {
    "bytes": 512,
    "sha256": "d4270202d9442a3d36eb1ba2d3fc98432f26138d08572e71587f3a4da420f224"
  },
  "outer_C_coefficients": {
    "bytes": 549,
    "sha256": "3ddcba88d287da2d09fa850fe14b69077b16e95bb2c834441b5e4d3a1496d505"
  }
}
```

### attempt 2

```json
{
  "amplitude": 0.05,
  "nu": 0.0008183728052959186,
  "exact_float_nu": "3774078424044387/4611686018427387904",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 775,
  "diagnostics": {
        "normalized_finite_residual": 1.650636565666503e-05,
        "normalized_full_B_residual": 1.1798505205579124e-05,
        "normalized_full_C_residual": 1.650636565919683e-05,
        "normalized_A_projection_defect": 3.219646771412954e-15,
        "C_min": -0.9885586778874405,
        "C_max": -0.17245672423486189,
        "B_abs_max": 0.031870324670401844,
        "actual_full_B_residual": 5.899252602789562e-07,
        "actual_full_C_residual": 8.253182829598416e-07,
        "actual_A_projection_defect": 1.6098233857064772e-16,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 3097,
        "valid": true
      },
  "waist_mean_C": -0.9356875460334886,
  "waist_mean_closure_gap": 1.1102230246251565e-16,
  "waist_turn_number": 0.9999999999999999,
  "waist_total_turn": 6.283185307179585,
  "outer_C_mean_minus_reference": -0.04626922464530572,
  "normalized_outer_regular_linear_residual_l1": 5.054514064784373e-29,
  "maximum_boundary_residual": 1.1466475402094063e-27
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 5562,
    "sha256": "34cc412d5c0b7a6669108eacb5b72217d94700a08f9138a7be55d243f09e3c33"
  },
  "waist_B_coefficients": {
    "bytes": 311,
    "sha256": "c28e9e629dbc02d4264ab8f4af7afa71e55559cfaf4a85f713375ed1c13fc5fd"
  },
  "waist_C_coefficients": {
    "bytes": 534,
    "sha256": "6ed7953a1a0431198b5aa5b808aa2907f525e11f54252c1a15256922832f8e33"
  },
  "outer_B_coefficients": {
    "bytes": 518,
    "sha256": "148b3c454bd0d6d63dd188d572405857c1b39388b77e3e689983e11f322e21ff"
  },
  "outer_C_coefficients": {
    "bytes": 553,
    "sha256": "301544034357874ad856bf3809ff874566ee1c8d08305f7957904c8d0e793dbf"
  }
}
```

### attempt 3

```json
{
  "amplitude": 0.1,
  "nu": 0.000783345490127849,
  "exact_float_nu": "7225086888841501/9223372036854775808",
  "success": false,
  "solver_status": 2,
  "solver_message": "A singular Jacobian encountered when solving the collocation system.",
  "radial_nodes": 775,
  "diagnostics": {
        "normalized_finite_residual": 512.5121140603588,
        "normalized_full_B_residual": 0.310899399069878,
        "normalized_full_C_residual": 512.5121140603596,
        "normalized_A_projection_defect": 8.79296635503124e-14,
        "C_min": -29.999996037890977,
        "C_max": -0.1804479497300367,
        "B_abs_max": 0.06374539234733177,
        "actual_full_B_residual": 0.0310899399069878,
        "actual_full_C_residual": 51.251211406035964,
        "actual_A_projection_defect": 8.79296635503124e-15,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 3097,
        "valid": true
      },
  "waist_mean_C": -0.9356875460334886,
  "waist_mean_closure_gap": 1.1102230246251565e-16,
  "waist_turn_number": 0.9999999999999999,
  "waist_total_turn": 6.283185307179585,
  "outer_C_mean_minus_reference": -29.828898264045456,
  "normalized_outer_regular_linear_residual_l1": 1.6544136843562525e-24,
  "maximum_boundary_residual": 9.325281826576448e-20
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 5423,
    "sha256": "96cd46b4d145c93c072fa317e81b94025b2292951dd94197ceae5273366f7ef7"
  },
  "waist_B_coefficients": {
    "bytes": 312,
    "sha256": "0d0ae07fd11cbda68425b1bd8f6fb89257d9ce138f701011472508b65cb20746"
  },
  "waist_C_coefficients": {
    "bytes": 541,
    "sha256": "7b566a96835130fe76f3b805739c695d52b56d677395553729011b8ceab89c4d"
  },
  "outer_B_coefficients": {
    "bytes": 521,
    "sha256": "fcaad3f0b035c33ccfdd0cef80dd58552f0ccb8c0b7e7e09cb7fb3d84b3a4859"
  },
  "outer_C_coefficients": {
    "bytes": 555,
    "sha256": "2050b0edcb8c7fbce3afed025edd53bd904646b8767c41a1ee578d521d77896a"
  }
}
```

## 2. 2026-11-13-R133-compact-metric-m128-alpha070-v13-core16-b1-floating.json

完整原件：44699 B；Git `e70cdfdfebc0f00def8bcd1d6846bbf559c26f65`；SHA256 `e10345b6dbdcb6fc3267ea4d2efe5b13361a4d02e5fdfcd581fd7704fe62a6fa`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_refined_compact_metric_normalized_Codazzi_branch_v13_full_FFT_matrix_free_preconditioned_Newton",
  "modes": 128,
  "amplitude": 0.7,
  "nu": -0.028462943388345506,
  "exact_float_nu": "-4101942439603851/144115188075855872",
  "source_sha256": "98b1d3624199011a4241292e97284fede0cedd96571083d5b75b0358506de685",
  "mean_boundary": "outer",
  "finite_BVP_success": false,
  "solver_status": 2,
  "solver_message": "A singular Jacobian encountered when solving the collocation system.",
  "diagnostics": {
    "normalized_finite_residual": 0.000124226523472169,
    "normalized_full_B_residual": 0.0025965949258257583,
    "normalized_full_C_residual": 6.643211423197165e-05,
    "normalized_A_projection_defect": 4.819066100836267e-06,
    "C_min": -5.185509370163061,
    "C_max": -0.171039167658588,
    "B_abs_max": 0.5598523419917322,
    "actual_full_B_residual": 0.0018176164480780306,
    "actual_full_C_residual": 4.650247996238015e-05,
    "actual_A_projection_defect": 3.3733462705853865e-06,
    "radial_samples": "nodes and quarter/mid/three-quarter points",
    "radial_sample_count": 3397,
    "valid": true
  },
  "nonlinear_system_unmodified": true,
  "target_coefficient_cache_entries": 328,
  "complete_linearized_operator_used": true,
  "accepted_complete_checkpoints": [],
  "initial_radial_nodes": 850,
  "radial_nodes": 850,
  "angular_grid": 1024,
  "diagnostic_angular_grid": 2048,
  "tol": 2e-06,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 3.038250371049599e-10,
    "state_relative_errors": [
      1.568342366964605e-10,
      3.588141409470259e-10,
      1.442685420202958e-10,
      1.5253002318370615e-12
    ]
  },
  "waist_mean_C": -0.9356875460030095,
  "waist_mean_closure_gap": 3.047917473963935e-11,
  "waist_turn_number": 0.999999999967426,
  "waist_total_turn": 6.283185306974917,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 1.5146130477080271e-28,
  "maximum_boundary_residual": 1.5146129380243427e-28,
  "outer_linear_height_homogeneous_A2_norm": 1.7659161034772058e-12,
  "guess_path": "notes/2026-11-13-R133-compact-metric-m128-alpha070-v9-candidate.json",
  "guess_sha256": "0e5e7f206f0d98a5136b4c13b723cce1dfeb7b7abfe2ed2cd4deb2b51b2b2146",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-m128-alpha070-v13-core16-b1-candidate.json",
  "candidate_sha256": "78326de99a1a72be1f74d91d48be53799cd5a86306a6476780609bcaa0c81d0a",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_branch_probe.py": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_codazzi_candidate_shards.py": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "fourfold_codazzi_chunked_collocation_v2.py": "3653968b4be39134f2ff8617636428f15cc3bdd15ebbebfd282bb801a5776ba1",
    "fourfold_codazzi_compact_metric_fast_jacobian.py": "0d82b18aaed063660f7003e36061958a327d134c67490adb7b340deddfc90c17",
    "fourfold_codazzi_guarded_Newton_krylov_v3.py": "307d1675291f706f84436393940d05a224825149a498cdf1710ebe3e9fddf9fc",
    "fourfold_codazzi_matrix_free_fft_collocation_v5.py": "fd7ec9abec913af19c47daf25bca72833221cc5603c9eb1631cfda9542e16233",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Only the LU preconditioner is sparsified; GMRES uses the full untruncated finite Jacobian action and checks its residual. The full nonlinear system and diagnostics are unchanged.",
    "Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.",
    "The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.",
    "The opposite mean boundary is printed, not silently set to zero.",
    "True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.",
    "The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred."
  ],
  "wall_seconds": 577.0137963919988
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "guarded_Newton_history": {
    "bytes": 141,
    "sha256": "d5a9ec6c0f4f107828e0ee0164b8dd27bba208f9eaecbf8b44655beaf9a1d8ea"
  },
  "approximate_linear_solver_history": {
    "bytes": 22671,
    "sha256": "47cbb8e924b7a4cfa4ca15053a15fd0b75936b40eef24f68d928f062d05dac65"
  },
  "waist_B_coefficients": {
    "bytes": 1157,
    "sha256": "4841d8381338942c9fe97ce2cad2078d5393c72db456ce0441d066bfa9774185"
  },
  "waist_C_coefficients": {
    "bytes": 3531,
    "sha256": "dc8cbf358139403d21f7783c29d79d7e3a4fcd03dc5372cb118a38276928ed9b"
  },
  "outer_B_coefficients": {
    "bytes": 3557,
    "sha256": "addee6c244736e93e14213e421ac47a932f92c4a6ea891d9185e742fde989d81"
  },
  "outer_C_coefficients": {
    "bytes": 3610,
    "sha256": "35e0e34958bc1e7108b3d73361c4961e3bdc27e7e30d1b8e1e93e0e7387e30a8"
  },
  "outer_linear_height_estimate": {
    "bytes": 3581,
    "sha256": "99c32e5bd470ca436ab481189f3da43de8833a14d24cfa489be02241d382f655"
  }
}
```

## 3. 2026-11-13-R133-compact-metric-m128-alpha070-v13-core16-floating.json

完整原件：44341 B；Git `6b9c56da56af9910748630de76c4251c6b2e434b`；SHA256 `c6e3ab6a0da9e462c26c16579b48dd30c6882e929f5ff995abe598b3a6ed6ee2`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_refined_compact_metric_normalized_Codazzi_branch_v13_full_FFT_matrix_free_preconditioned_Newton",
  "modes": 128,
  "amplitude": 0.7,
  "nu": -0.028462943388345506,
  "exact_float_nu": "-4101942439603851/144115188075855872",
  "source_sha256": "98b1d3624199011a4241292e97284fede0cedd96571083d5b75b0358506de685",
  "mean_boundary": "outer",
  "finite_BVP_success": false,
  "solver_status": 2,
  "solver_message": "A singular Jacobian encountered when solving the collocation system.",
  "diagnostics": {
    "normalized_finite_residual": 0.000124226523472169,
    "normalized_full_B_residual": 0.0025965949258257583,
    "normalized_full_C_residual": 6.643211423197165e-05,
    "normalized_A_projection_defect": 4.819066100836267e-06,
    "C_min": -5.185509370163061,
    "C_max": -0.171039167658588,
    "B_abs_max": 0.5598523419917322,
    "actual_full_B_residual": 0.0018176164480780306,
    "actual_full_C_residual": 4.650247996238015e-05,
    "actual_A_projection_defect": 3.3733462705853865e-06,
    "radial_samples": "nodes and quarter/mid/three-quarter points",
    "radial_sample_count": 3397,
    "valid": true
  },
  "nonlinear_system_unmodified": true,
  "target_coefficient_cache_entries": 328,
  "complete_linearized_operator_used": true,
  "accepted_complete_checkpoints": [],
  "initial_radial_nodes": 850,
  "radial_nodes": 850,
  "angular_grid": 1024,
  "diagnostic_angular_grid": 2048,
  "tol": 2e-06,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 3.038250371049599e-10,
    "state_relative_errors": [
      1.568342366964605e-10,
      3.588141409470259e-10,
      1.442685420202958e-10,
      1.5253002318370615e-12
    ]
  },
  "waist_mean_C": -0.9356875460030095,
  "waist_mean_closure_gap": 3.047917473963935e-11,
  "waist_turn_number": 0.999999999967426,
  "waist_total_turn": 6.283185306974917,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 1.5146130477080271e-28,
  "maximum_boundary_residual": 1.5146129380243427e-28,
  "outer_linear_height_homogeneous_A2_norm": 1.7659161034772058e-12,
  "guess_path": "notes/2026-11-13-R133-compact-metric-m128-alpha070-v9-candidate.json",
  "guess_sha256": "0e5e7f206f0d98a5136b4c13b723cce1dfeb7b7abfe2ed2cd4deb2b51b2b2146",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-m128-alpha070-v13-core16-candidate.json",
  "candidate_sha256": "b967a73d32c3ed8c8ef6c62811e865b4b2aa28a6340aa4a3440888034a1336c2",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_branch_probe.py": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_codazzi_candidate_shards.py": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "fourfold_codazzi_chunked_collocation_v2.py": "3653968b4be39134f2ff8617636428f15cc3bdd15ebbebfd282bb801a5776ba1",
    "fourfold_codazzi_compact_metric_fast_jacobian.py": "0d82b18aaed063660f7003e36061958a327d134c67490adb7b340deddfc90c17",
    "fourfold_codazzi_guarded_Newton_krylov_v3.py": "307d1675291f706f84436393940d05a224825149a498cdf1710ebe3e9fddf9fc",
    "fourfold_codazzi_matrix_free_fft_collocation_v5.py": "fd7ec9abec913af19c47daf25bca72833221cc5603c9eb1631cfda9542e16233",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Only the LU preconditioner is sparsified; GMRES uses the full untruncated finite Jacobian action and checks its residual. The full nonlinear system and diagnostics are unchanged.",
    "Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.",
    "The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.",
    "The opposite mean boundary is printed, not silently set to zero.",
    "True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.",
    "The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred."
  ],
  "wall_seconds": 280.73004526000295
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "guarded_Newton_history": {
    "bytes": 141,
    "sha256": "d5a9ec6c0f4f107828e0ee0164b8dd27bba208f9eaecbf8b44655beaf9a1d8ea"
  },
  "approximate_linear_solver_history": {
    "bytes": 22315,
    "sha256": "414140c27c6520682b1ce27db292c57ee2d88efa2d450e431e08df5d8c5680c8"
  },
  "waist_B_coefficients": {
    "bytes": 1157,
    "sha256": "4841d8381338942c9fe97ce2cad2078d5393c72db456ce0441d066bfa9774185"
  },
  "waist_C_coefficients": {
    "bytes": 3531,
    "sha256": "dc8cbf358139403d21f7783c29d79d7e3a4fcd03dc5372cb118a38276928ed9b"
  },
  "outer_B_coefficients": {
    "bytes": 3557,
    "sha256": "addee6c244736e93e14213e421ac47a932f92c4a6ea891d9185e742fde989d81"
  },
  "outer_C_coefficients": {
    "bytes": 3610,
    "sha256": "35e0e34958bc1e7108b3d73361c4961e3bdc27e7e30d1b8e1e93e0e7387e30a8"
  },
  "outer_linear_height_estimate": {
    "bytes": 3581,
    "sha256": "99c32e5bd470ca436ab481189f3da43de8833a14d24cfa489be02241d382f655"
  }
}
```

## 4. 2026-11-13-R133-compact-metric-m128-alpha070-v14-full-QR-floating.json

完整原件：27019 B；Git `5c3ef379c73c137938fb98d4cb279cd03328e143`；SHA256 `dbe8b09bdd211c2eba28f6070e655421bd3b9ff208f7eec76e9e9f6a10e627b7`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_refined_compact_metric_normalized_Codazzi_branch_v14_full_block_boundary_QR_Newton",
  "modes": 128,
  "amplitude": 0.7,
  "nu": -0.028463024309522047,
  "exact_float_nu": "-8203908203148855/288230376151711744",
  "source_sha256": "6d4255ebfc6ca15124de3a23d05e00035c1dcaa19a1aa0abd4c2a93f10fdfe71",
  "mean_boundary": "outer",
  "finite_BVP_success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "diagnostics": {
    "normalized_finite_residual": 8.179213796604275e-06,
    "normalized_full_B_residual": 0.00185117416067201,
    "normalized_full_C_residual": 2.329993451039014e-06,
    "normalized_A_projection_defect": 3.4286928622950796e-06,
    "C_min": -5.185512476163809,
    "C_max": -0.17103916765858804,
    "B_abs_max": 0.5598515864242426,
    "actual_full_B_residual": 0.001295821912470407,
    "actual_full_C_residual": 1.6309954157273098e-06,
    "actual_A_projection_defect": 2.4000850036065557e-06,
    "radial_samples": "nodes and quarter/mid/three-quarter points",
    "radial_sample_count": 3397,
    "valid": true
  },
  "nonlinear_system_unmodified": true,
  "target_coefficient_cache_entries": 540,
  "complete_linearized_operator_used": true,
  "accepted_complete_checkpoints": [
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha070-v14-full-QR-floating/accepted-000.npz",
      "sha256": "3efe9b9686cb474803f78ebf6a86a22df8fcf53581bd0262b753eb2c61982c73",
      "bytes": 3405974,
      "nodes": 850,
      "step": {
        "nodes": 850,
        "iteration": 0,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.028462943388345506,
        "proposed_nu": -0.028463024309522047,
        "affine_invariant_cost": 1.0112379641207826e-07,
        "next_cost": null,
        "max_collocation_residual": 3.6958013879134517e-08,
        "max_boundary_residual": 1.5146129380243427e-28,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": true,
        "converged_trial_collocation_residual": 6.118110784069234e-12,
        "converged_trial_boundary_residual": 2.2329532839244516e-21
      }
    }
  ],
  "initial_radial_nodes": 850,
  "radial_nodes": 850,
  "angular_grid": 1024,
  "diagnostic_angular_grid": 2048,
  "tol": 2e-06,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 3.038250371049599e-10,
    "state_relative_errors": [
      1.568342366964605e-10,
      3.588141409470259e-10,
      1.442685420202958e-10,
      1.5253002318370615e-12
    ]
  },
  "waist_mean_C": -0.9356875459879767,
  "waist_mean_closure_gap": 4.551203858227382e-11,
  "waist_turn_number": 0.9999999999513598,
  "waist_total_turn": 6.28318530687397,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 1.9826709648659315e-37,
  "maximum_boundary_residual": 2.2329532839244516e-21,
  "outer_linear_height_homogeneous_A2_norm": 1.7658620204903105e-12,
  "guess_path": "notes/2026-11-13-R133-compact-metric-m128-alpha070-v9-candidate.json",
  "guess_sha256": "0e5e7f206f0d98a5136b4c13b723cce1dfeb7b7abfe2ed2cd4deb2b51b2b2146",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-m128-alpha070-v14-full-QR-candidate.json",
  "candidate_sha256": "88a1e73b62a1c0157b81cf71f2dc93c912c079bd07b85acbdadbb13267a85c7b",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_branch_probe.py": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_codazzi_candidate_shards.py": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "fourfold_codazzi_chunked_collocation_v2.py": "3653968b4be39134f2ff8617636428f15cc3bdd15ebbebfd282bb801a5776ba1",
    "fourfold_codazzi_compact_metric_fast_jacobian.py": "0d82b18aaed063660f7003e36061958a327d134c67490adb7b340deddfc90c17",
    "fourfold_codazzi_guarded_Newton_krylov_v3.py": "307d1675291f706f84436393940d05a224825149a498cdf1710ebe3e9fddf9fc",
    "fourfold_codazzi_matrix_free_fft_collocation_v5.py": "fd7ec9abec913af19c47daf25bca72833221cc5603c9eb1631cfda9542e16233",
    "fourfold_codazzi_block_qr_collocation.py": "62a538a21334f591a227492cade1af369403dc4ed18fad184fc8604abc8bf429",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Every finite collocation block, Fourier coupling and parameter column is retained in the boundary-row QR factorization. The same independent full FFT action and original backward-residual gate check every solve; all nonlinear gates are unchanged.",
    "Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.",
    "The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.",
    "The opposite mean boundary is printed, not silently set to zero.",
    "True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.",
    "The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred."
  ],
  "wall_seconds": 61.35520063399599
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "guarded_Newton_history": {
    "bytes": 636,
    "sha256": "9833fd8999e6f2af3510a47cbad2ae4cb1bc851d0863099efaa4cf8779a96751"
  },
  "complete_linear_solver_history": {
    "bytes": 1005,
    "sha256": "4f885be95bcba36f468aff529b5bc034399fd5cb011f0d1dba62788179e1af5b"
  },
  "waist_B_coefficients": {
    "bytes": 3568,
    "sha256": "3b04c5aa3a087c2555c6458899ad8a2159497049028313faa0ba6f249de4c791"
  },
  "waist_C_coefficients": {
    "bytes": 3537,
    "sha256": "bfd92524d739b80ce93d4e8841bb7c7d89fba5c8cfd49d8f141fa4061a57ee24"
  },
  "outer_B_coefficients": {
    "bytes": 3562,
    "sha256": "6c2da7d9e03068e7d3aaee4c6372b2539dbd08547ad0e6d232cb347bed9540af"
  },
  "outer_C_coefficients": {
    "bytes": 3597,
    "sha256": "b877d682b39950e4c16016ddae1b7de3fd293a738c964fd6f6d7725a23269aee"
  },
  "outer_linear_height_estimate": {
    "bytes": 3582,
    "sha256": "80370c6802426d75dcfddb541696b1b229cca8fc7e6233b9214e6ba069afc97a"
  }
}
```

## 5. 2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating.json

完整原件：47984 B；Git `39d063a6a3b268a6d7d01701613e62e0ba5b8a14`；SHA256 `dee77b0b93736bf80e51dec5d7f5469b848c3daa89f55151e272adcc1fbb9598`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_refined_compact_metric_normalized_Codazzi_branch_v14_full_block_boundary_QR_Newton",
  "modes": 128,
  "amplitude": 0.75,
  "nu": -0.033907361865808484,
  "exact_float_nu": "-4886565832447093/144115188075855872",
  "source_sha256": "6d4255ebfc6ca15124de3a23d05e00035c1dcaa19a1aa0abd4c2a93f10fdfe71",
  "mean_boundary": "outer",
  "finite_BVP_success": false,
  "solver_status": 1,
  "solver_message": "The maximum number of mesh nodes is exceeded.",
  "diagnostics": {
    "normalized_finite_residual": 0.00010322226124280234,
    "normalized_full_B_residual": 0.4071058735972771,
    "normalized_full_C_residual": 7.650301505337034e-05,
    "normalized_A_projection_defect": 0.0007439025028894708,
    "C_min": -8.679718607712918,
    "C_max": -0.1710391676585331,
    "B_abs_max": 0.6303904539267435,
    "actual_full_B_residual": 0.3053294051979578,
    "actual_full_C_residual": 5.737726129002776e-05,
    "actual_A_projection_defect": 0.0005579268771671031,
    "radial_samples": "nodes and quarter/mid/three-quarter points",
    "radial_sample_count": 5513,
    "valid": true
  },
  "nonlinear_system_unmodified": true,
  "target_coefficient_cache_entries": 1286,
  "complete_linearized_operator_used": true,
  "accepted_complete_checkpoints": [
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-000.npz",
      "sha256": "cd0979b792e29728b7c65d4eb49122a0dca13506f6ead6a5dd714f9303fef441",
      "bytes": 3400050,
      "nodes": 850,
      "step": {
        "nodes": 850,
        "iteration": 0,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.028463024309522047,
        "proposed_nu": 0.029421456784631626,
        "affine_invariant_cost": 33.493422617180286,
        "next_cost": 1.3920392306603628,
        "max_collocation_residual": 9.506106348366409e-05,
        "max_boundary_residual": 2.2329532839244516e-21,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": false,
        "converged_trial_collocation_residual": null,
        "converged_trial_boundary_residual": null
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-001.npz",
      "sha256": "d202b75c73bfa3ea5a087e2b1ae8bb04b89aa7379f8d4f4b5cae4872ed28aa07",
      "bytes": 3401634,
      "nodes": 850,
      "step": {
        "nodes": 850,
        "iteration": 1,
        "accepted": true,
        "step_fraction": 0.5,
        "nu": 0.029421456784631626,
        "proposed_nu": 0.00027645506093028696,
        "affine_invariant_cost": 2.9569481715314243,
        "next_cost": 1.0515669236441343,
        "max_collocation_residual": 3.5071979324544355e-05,
        "max_boundary_residual": 8.09551892071619e-17,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": false,
        "converged_trial_collocation_residual": null,
        "converged_trial_boundary_residual": null
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-002.npz",
      "sha256": "bda7a5bf333c01969da5f29051695cbd25f42e18c651d2ae1f466d40a9b54321",
      "bytes": 3399714,
      "nodes": 850,
      "step": {
        "nodes": 850,
        "iteration": 2,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": 0.00027645506093028696,
        "proposed_nu": -0.03264194061098334,
        "affine_invariant_cost": 0.8021017480456865,
        "next_cost": 0.012990254041445012,
        "max_collocation_residual": 1.7422680998008307e-05,
        "max_boundary_residual": 4.2735917162110297e-17,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": false,
        "converged_trial_collocation_residual": null,
        "converged_trial_boundary_residual": null
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-003.npz",
      "sha256": "d418a974784eb3e35ac2334a704ed1ff993ac8c173f0164e4f1f1fd9792ecd24",
      "bytes": 3401467,
      "nodes": 850,
      "step": {
        "nodes": 850,
        "iteration": 3,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.03264194061098334,
        "proposed_nu": -0.03390705488161112,
        "affine_invariant_cost": 0.0017644464519359052,
        "next_cost": 1.2484483757204806e-05,
        "max_collocation_residual": 2.486568498503904e-05,
        "max_boundary_residual": 1.0083973884996563e-17,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": false,
        "converged_trial_collocation_residual": null,
        "converged_trial_boundary_residual": null
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-004.npz",
      "sha256": "4276025d28db955991fead839794c6137526aa56a36924cf1082bef6b499f130",
      "bytes": 3402221,
      "nodes": 850,
      "step": {
        "nodes": 850,
        "iteration": 4,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.03390705488161112,
        "proposed_nu": -0.033907354480277443,
        "affine_invariant_cost": 1.0672993627709324e-05,
        "next_cost": 5.568887293831099e-12,
        "max_collocation_residual": 6.970435433711389e-07,
        "max_boundary_residual": 4.94186453532898e-19,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": false,
        "converged_trial_collocation_residual": null,
        "converged_trial_boundary_residual": null
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-005.npz",
      "sha256": "259b5570a582bc2fb52b2a172d0531100aeea96f9d92debff1b7adbba8104278",
      "bytes": 3404989,
      "nodes": 850,
      "step": {
        "nodes": 850,
        "iteration": 5,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.033907354480277443,
        "proposed_nu": -0.03390735169463149,
        "affine_invariant_cost": 5.5782643359336085e-12,
        "next_cost": null,
        "max_collocation_residual": 8.835933505288646e-10,
        "max_boundary_residual": 2.350983924582217e-20,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": true,
        "converged_trial_collocation_residual": 3.0672905316738493e-16,
        "converged_trial_boundary_residual": 1.611357952714327e-23
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-006.npz",
      "sha256": "79d3413757cd25172ddf9c7e91a086b996c675783f231b2a9285ebcbb0c90ca1",
      "bytes": 5473948,
      "nodes": 1379,
      "step": {
        "nodes": 1379,
        "iteration": 0,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.03390735169463149,
        "proposed_nu": -0.03390736201245356,
        "affine_invariant_cost": 1.1516700876501238e-06,
        "next_cost": 1.901137975138677e-14,
        "max_collocation_residual": 2.9674871508268805e-08,
        "max_boundary_residual": 1.611357952714327e-23,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": false,
        "converged_trial_collocation_residual": null,
        "converged_trial_boundary_residual": null
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-floating/accepted-007.npz",
      "sha256": "9174f9a538a330731580116b6bf646b10c68a3c20ca16eb217b4ff468364a194",
      "bytes": 5474024,
      "nodes": 1379,
      "step": {
        "nodes": 1379,
        "iteration": 1,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.03390736201245356,
        "proposed_nu": -0.033907361865808484,
        "affine_invariant_cost": 1.9003776424381182e-14,
        "next_cost": null,
        "max_collocation_residual": 2.554439203089902e-11,
        "max_boundary_residual": 6.236952148753304e-21,
        "trial_already_passed_complete_collocation_and_boundary_tolerances": true,
        "converged_trial_collocation_residual": 1.1137232350133194e-16,
        "converged_trial_boundary_residual": 7.501580253793775e-25
      }
    }
  ],
  "initial_radial_nodes": 850,
  "radial_nodes": 1379,
  "angular_grid": 1024,
  "diagnostic_angular_grid": 2048,
  "tol": 2e-06,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 3.038250371049599e-10,
    "state_relative_errors": [
      1.568342366964605e-10,
      3.588141409470259e-10,
      1.442685420202958e-10,
      1.5253002318370615e-12
    ]
  },
  "waist_mean_C": -0.9356875460227811,
  "waist_mean_closure_gap": 1.0707545960997322e-11,
  "waist_turn_number": 0.9999999999885565,
  "waist_total_turn": 6.283185307107685,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 4.257736643090125e-38,
  "maximum_boundary_residual": 7.501580253793775e-25,
  "outer_linear_height_homogeneous_A2_norm": 1.9240471108256406e-12,
  "guess_path": "notes/2026-11-13-R133-compact-metric-m128-alpha070-v14-full-QR-candidate.json",
  "guess_sha256": "88a1e73b62a1c0157b81cf71f2dc93c912c079bd07b85acbdadbb13267a85c7b",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-m128-alpha075-v14-full-QR-candidate.json",
  "candidate_sha256": "b837161a4c3050f36f0ea2052874a5efd71621471df34edd30a44f44f66741f5",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_branch_probe.py": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_codazzi_candidate_shards.py": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "fourfold_codazzi_chunked_collocation_v2.py": "3653968b4be39134f2ff8617636428f15cc3bdd15ebbebfd282bb801a5776ba1",
    "fourfold_codazzi_compact_metric_fast_jacobian.py": "0d82b18aaed063660f7003e36061958a327d134c67490adb7b340deddfc90c17",
    "fourfold_codazzi_guarded_Newton_krylov_v3.py": "307d1675291f706f84436393940d05a224825149a498cdf1710ebe3e9fddf9fc",
    "fourfold_codazzi_matrix_free_fft_collocation_v5.py": "fd7ec9abec913af19c47daf25bca72833221cc5603c9eb1631cfda9542e16233",
    "fourfold_codazzi_block_qr_collocation.py": "62a538a21334f591a227492cade1af369403dc4ed18fad184fc8604abc8bf429",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Every finite collocation block, Fourier coupling and parameter column is retained in the boundary-row QR factorization. The same independent full FFT action and original backward-residual gate check every solve; all nonlinear gates are unchanged.",
    "Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.",
    "The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.",
    "The opposite mean boundary is printed, not silently set to zero.",
    "True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.",
    "The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred."
  ],
  "wall_seconds": 384.0775091569958
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "guarded_Newton_history": {
    "bytes": 4914,
    "sha256": "a7c7e5fc299c9f00d417800f636a18983e16084ac79d1cfdf038df1efcf86ce6"
  },
  "complete_linear_solver_history": {
    "bytes": 11400,
    "sha256": "8781cbb98dafaa0d2ead863effcbb1abf05a86dfad544b8a8d8a20fba77d0a90"
  },
  "waist_B_coefficients": {
    "bytes": 3570,
    "sha256": "7e5daaf84eb36291533881d7e29b25a1b8866f4ed15726932e3286e8f1e6c182"
  },
  "waist_C_coefficients": {
    "bytes": 3441,
    "sha256": "478164029c055d283b4a186f4685df6dd101884c4b4a00672b75639482169876"
  },
  "outer_B_coefficients": {
    "bytes": 3574,
    "sha256": "74e364b2b837580eecbd60fb1838a9bab9dc54690f7e27fcfbe01b4a1e14c486"
  },
  "outer_C_coefficients": {
    "bytes": 3595,
    "sha256": "1251549c3026b5a270dd21d447ace0b5e621a126791912e2250ef98f399d1693"
  },
  "outer_linear_height_estimate": {
    "bytes": 3567,
    "sha256": "8eb1e5cb2e4e89a107f0592d2db1d9d824ce54f138dcd539765e92af8da76c0a"
  }
}
```

## 6. 2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-floating.json

完整原件：32418 B；Git `b47a3715f053e16d2eab4f5a491af7af1454769f`；SHA256 `5001d4c110bd402f0d500b86670ad81e7d5f072adaa46a1e10644753de2e9754`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_refined_compact_metric_normalized_Codazzi_branch_v7_full_FFT_matrix_free_preconditioned_Newton",
  "modes": 128,
  "amplitude": 0.65,
  "nu": -0.023721616162222504,
  "exact_float_nu": "-6837290349363917/288230376151711744",
  "source_sha256": "50191f3b2b3e695bc67e0ed6c93d41fc934221d26ec89f55967cbd11aaa92957",
  "mean_boundary": "outer",
  "finite_BVP_success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "diagnostics": {
    "normalized_finite_residual": 8.057861446595551e-06,
    "normalized_full_B_residual": 8.802996576569126e-06,
    "normalized_full_C_residual": 4.625175364272871e-06,
    "normalized_A_projection_defect": 2.9868010287259494e-09,
    "C_min": -3.7455163247798664,
    "C_max": -0.17103916765864002,
    "B_abs_max": 0.49922759734547617,
    "actual_full_B_residual": 5.721947774769932e-06,
    "actual_full_C_residual": 3.0063639867773663e-06,
    "actual_A_projection_defect": 1.9414206686718672e-09,
    "radial_samples": "nodes and quarter/mid/three-quarter points",
    "radial_sample_count": 2601,
    "valid": true
  },
  "nonlinear_system_unmodified": true,
  "target_coefficient_cache_entries": 291,
  "complete_linearized_operator_used": true,
  "accepted_complete_checkpoints": [
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-floating/accepted-000.npz",
      "sha256": "008dccf45b1a6fb3da8bbb31708aa1ffff409bd226ff3acd0061aa29278164c8",
      "bytes": 2599789,
      "nodes": 650,
      "step": {
        "nodes": 650,
        "iteration": 0,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.023722177521444274,
        "proposed_nu": -0.023721614896017137,
        "affine_invariant_cost": 1.0428472891247295e-12,
        "next_cost": 7.43232816784674e-24,
        "max_collocation_residual": 2.3146413055902346e-07,
        "max_boundary_residual": 2.0122934192040947e-22
      }
    },
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-floating/accepted-001.npz",
      "sha256": "7282c6a1cd434066cb9157511a1ae1a8f838dd83f573375935d31ede566bf26e",
      "bytes": 2604214,
      "nodes": 651,
      "step": {
        "nodes": 651,
        "iteration": 0,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.023721614896017137,
        "proposed_nu": -0.023721616162222504,
        "affine_invariant_cost": 5.053814417453753e-17,
        "next_cost": 3.81039818116207e-26,
        "max_collocation_residual": 6.8188564278544306e-09,
        "max_boundary_residual": 5.048709793414476e-29
      }
    }
  ],
  "initial_radial_nodes": 440,
  "radial_nodes": 651,
  "angular_grid": 1024,
  "diagnostic_angular_grid": 2048,
  "tol": 2e-06,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 3.038250371049599e-10,
    "state_relative_errors": [
      1.568342366964605e-10,
      3.588141409470259e-10,
      1.442685420202958e-10,
      1.5253002318370615e-12
    ]
  },
  "waist_mean_C": -0.9356875460078499,
  "waist_mean_closure_gap": 2.563882439687859e-11,
  "waist_turn_number": 0.999999999972599,
  "waist_total_turn": 6.28318530700742,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 9.635701897360659e-32,
  "maximum_boundary_residual": 1.061597764435239e-32,
  "outer_linear_height_homogeneous_A2_norm": 1.6161307268917117e-12,
  "guess_path": "notes/2026-11-13-R133-compact-metric-outer-mean-m128-v7-b8-n1024-candidate.json",
  "guess_sha256": "15952f4245b7c4214f58f32a68ca64a875caa7a23d3c0b3b8d7c11321db349c6",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-candidate.json",
  "candidate_sha256": "4f19203308f8d95cb65f90d52c75edb7f476307698138be37efe7e305bde3e14",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_branch_probe.py": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_codazzi_candidate_shards.py": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "fourfold_codazzi_chunked_collocation.py": "5b96d9298014703cf41c59a2d9466e81d523673fb659a52ca6488a03ef939a73",
    "fourfold_codazzi_compact_metric_fast_jacobian.py": "0d82b18aaed063660f7003e36061958a327d134c67490adb7b340deddfc90c17",
    "fourfold_codazzi_guarded_Newton_krylov.py": "03e466ef693694b6dc94e0f88328e842ecc435ba031572f2a83578776bf5ff9e",
    "fourfold_codazzi_matrix_free_fft_collocation.py": "bb1095f2635ae3961b4b25ae50ae84d2007e02ca1268ffdd1b8348d4484a5600",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Only the LU preconditioner is sparsified; GMRES uses the full untruncated finite Jacobian action and checks its residual. The full nonlinear system and diagnostics are unchanged.",
    "Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.",
    "The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.",
    "The opposite mean boundary is printed, not silently set to zero.",
    "True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.",
    "The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred."
  ],
  "wall_seconds": 329.8344093359992
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "guarded_Newton_history": {
    "bytes": 1298,
    "sha256": "837d9de358ec66031a5d02a454d6be5a40f5b825bc2ee5c99f12eeb3fc4a79eb"
  },
  "approximate_linear_solver_history": {
    "bytes": 7554,
    "sha256": "d150ee5e76442ea685c52e34528386b30c8c5322dbe84f61050b1f1e791bdd2c"
  },
  "waist_B_coefficients": {
    "bytes": 1309,
    "sha256": "621e10e77a524a1e5b964e7990ef1259b7f9d7fd5e40eccc371f95bf11f99317"
  },
  "waist_C_coefficients": {
    "bytes": 3581,
    "sha256": "abf17f5d3d73954d49539fe6f6651dddfe9b07b2322c73fe6f83bceac3f29245"
  },
  "outer_B_coefficients": {
    "bytes": 3571,
    "sha256": "6f117808f02d76bd1eedbbbc897e6a732b013ce1fcce1fb67902f522075a7a76"
  },
  "outer_C_coefficients": {
    "bytes": 3627,
    "sha256": "61da159717c6b6107c29068f0d4d428244f1c91e34d12c014159bfaec2f5393a"
  },
  "outer_linear_height_estimate": {
    "bytes": 3582,
    "sha256": "1155c73a5a41161626a3e24c66c8ef85f9b0f1c8b13ae8ae63c479ee2a86bdcd"
  }
}
```

## 7. 2026-11-13-R133-compact-metric-outer-mean-m128-v6-b2-n1024-floating.json

完整原件：29382 B；Git `91f01680610ba5de5ef329c9d33b7c4796ef667c`；SHA256 `2200a575894cfcf66f46e48705422ca08b0048288a86f6b76541324dedff0235`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_refined_compact_metric_normalized_Codazzi_branch_v6_full_matrix_free_preconditioned_Newton",
  "modes": 128,
  "amplitude": 0.65,
  "nu": -0.023721707968258524,
  "exact_float_nu": "-1709329202663053/72057594037927936",
  "source_sha256": "fa48d5aedd5b41581ed30ac9758c4f279cef2032aa1a24e36bf02cb86c9f3e97",
  "mean_boundary": "outer",
  "finite_BVP_success": false,
  "solver_status": 2,
  "solver_message": "A singular Jacobian encountered when solving the collocation system.",
  "diagnostics": {
    "normalized_finite_residual": 0.008394644946573283,
    "normalized_full_B_residual": 0.008455893341367888,
    "normalized_full_C_residual": 0.00018251995339234415,
    "normalized_A_projection_defect": 3.31428884337015e-10,
    "C_min": -3.7452805439197228,
    "C_max": -0.17103916765864122,
    "B_abs_max": 0.49922655413899103,
    "actual_full_B_residual": 0.0054963306718891275,
    "actual_full_C_residual": 0.0001186379697050237,
    "actual_A_projection_defect": 2.1542877481905977e-10,
    "radial_samples": "nodes and quarter/mid/three-quarter points",
    "radial_sample_count": 1757,
    "valid": true
  },
  "nonlinear_system_unmodified": true,
  "target_coefficient_cache_entries": 172,
  "complete_linearized_operator_used": true,
  "accepted_complete_checkpoints": [],
  "initial_radial_nodes": 440,
  "radial_nodes": 440,
  "angular_grid": 1024,
  "diagnostic_angular_grid": 2048,
  "tol": 2e-06,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 3.038250371049599e-10,
    "state_relative_errors": [
      1.568342366964605e-10,
      3.588141409470259e-10,
      1.442685420202958e-10,
      1.5253002318370615e-12
    ]
  },
  "waist_mean_C": -0.9356875459993489,
  "waist_mean_closure_gap": 3.4139802096433414e-11,
  "waist_turn_number": 0.9999999999635137,
  "waist_total_turn": 6.283185306950336,
  "outer_C_mean_minus_reference": -5.465064010866787e-44,
  "normalized_outer_regular_linear_residual_l1": 5.048709793414637e-29,
  "maximum_boundary_residual": 1.4358056523730719e-21,
  "outer_linear_height_homogeneous_A2_norm": 1.6126728651026978e-12,
  "guess_path": "notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz",
  "guess_sha256": "4046eb7ac8da162ab9aad9fcb4991933200abdbc2c22ed6329d49bb13d72b856",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-outer-mean-m128-v6-b2-n1024-candidate.json",
  "candidate_sha256": "9ae67bb4514cf74b32c58d33c556146d98298095e6f838018bd129ea23ca41f7",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_branch_probe.py": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_codazzi_candidate_shards.py": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "fourfold_codazzi_chunked_collocation.py": "5b96d9298014703cf41c59a2d9466e81d523673fb659a52ca6488a03ef939a73",
    "fourfold_codazzi_compact_metric_fast_jacobian.py": "0d82b18aaed063660f7003e36061958a327d134c67490adb7b340deddfc90c17",
    "fourfold_codazzi_guarded_Newton_krylov.py": "03e466ef693694b6dc94e0f88328e842ecc435ba031572f2a83578776bf5ff9e",
    "fourfold_codazzi_matrix_free_collocation.py": "dfa07b7257b5ba5dff3c7580e6a8d74f2b7302691d6391a0a66c04f4f304592e",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Only the LU preconditioner is sparsified; GMRES uses the full untruncated finite Jacobian action and checks its residual. The full nonlinear system and diagnostics are unchanged.",
    "Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.",
    "The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.",
    "The opposite mean boundary is printed, not silently set to zero.",
    "True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.",
    "The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred."
  ],
  "wall_seconds": 548.185132857001
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "guarded_Newton_history": {
    "bytes": 141,
    "sha256": "031dbb1b1de2531938c9de110a0854fa7f8c2fc16f04bbb366b32889a49ea555"
  },
  "approximate_linear_solver_history": {
    "bytes": 11984,
    "sha256": "b62fda9aab53bc0fa455f1bdecff6095da7589ace2d3d91ab85b32705d2738ef"
  },
  "waist_B_coefficients": {
    "bytes": 1292,
    "sha256": "cb0b813604d649015bcf06c02e50f6ca1d3dc63f995391cb224d94cb03d93ea3"
  },
  "waist_C_coefficients": {
    "bytes": 2343,
    "sha256": "7a7e3138114f3193db497e59979d5050a1b790a055b0bc15825271e39ebb0218"
  },
  "outer_B_coefficients": {
    "bytes": 2343,
    "sha256": "54866a8a5731147c4081753da1a753ad714f1cf9e4d12ccb634770e038f6f1c8"
  },
  "outer_C_coefficients": {
    "bytes": 2419,
    "sha256": "e3693c42f82a654b17385a0c6690e1a66ffc6dedbc9c8cbd046710a4816e3a6e"
  },
  "outer_linear_height_estimate": {
    "bytes": 2405,
    "sha256": "d7df8744701e18d6ae15361e008c6ae5d5213a5bcca007d73c1753d3929f13d9"
  }
}
```

## 8. 2026-11-13-R133-compact-metric-outer-mean-m128-v7-b8-n1024-floating.json

完整原件：25711 B；Git `ac6bc5dce8fbfc67721a5e5fb746f60dd1a608c3`；SHA256 `209f30a8d3ab4233e209eef5d31a5d25a4f41dc0edbdc58030305596d7489d88`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_refined_compact_metric_normalized_Codazzi_branch_v7_full_FFT_matrix_free_preconditioned_Newton",
  "modes": 128,
  "amplitude": 0.65,
  "nu": -0.023722177521444274,
  "exact_float_nu": "-1709363037535891/72057594037927936",
  "source_sha256": "50191f3b2b3e695bc67e0ed6c93d41fc934221d26ec89f55967cbd11aaa92957",
  "mean_boundary": "outer",
  "finite_BVP_success": false,
  "solver_status": 1,
  "solver_message": "The maximum number of mesh nodes is exceeded.",
  "diagnostics": {
    "normalized_finite_residual": 5.774430580429912e-05,
    "normalized_full_B_residual": 5.913249526071898e-05,
    "normalized_full_C_residual": 1.4584135742623516e-05,
    "normalized_A_projection_defect": 2.929081865943317e-09,
    "C_min": -3.7455162626927505,
    "C_max": -0.17103916765863997,
    "B_abs_max": 0.4992274656770939,
    "actual_full_B_residual": 3.8436121919467336e-05,
    "actual_full_C_residual": 9.479688232705286e-06,
    "actual_A_projection_defect": 1.9039032128631563e-09,
    "radial_samples": "nodes and quarter/mid/three-quarter points",
    "radial_sample_count": 1757,
    "valid": true
  },
  "nonlinear_system_unmodified": true,
  "target_coefficient_cache_entries": 172,
  "complete_linearized_operator_used": true,
  "accepted_complete_checkpoints": [
    {
      "path": "/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints/2026-11-13-R133-compact-metric-outer-mean-m128-v7-b8-n1024-floating/accepted-000.npz",
      "sha256": "66e3f23fe81ea0a27a86b7daa6b4b493a5035fcec1ba1584ff4ab7feff951a8c",
      "bytes": 1761830,
      "nodes": 440,
      "step": {
        "nodes": 440,
        "iteration": 0,
        "accepted": true,
        "step_fraction": 1.0,
        "nu": -0.023721707968258524,
        "proposed_nu": -0.023722177521444274,
        "affine_invariant_cost": 1.5625052850481543e-07,
        "next_cost": 2.7945221279690287e-16,
        "max_collocation_residual": 4.561108508140372e-06,
        "max_boundary_residual": 1.4358056523730719e-21
      }
    }
  ],
  "initial_radial_nodes": 440,
  "radial_nodes": 440,
  "angular_grid": 1024,
  "diagnostic_angular_grid": 2048,
  "tol": 2e-06,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 3.038250371049599e-10,
    "state_relative_errors": [
      1.568342366964605e-10,
      3.588141409470259e-10,
      1.442685420202958e-10,
      1.5253002318370615e-12
    ]
  },
  "waist_mean_C": -0.9356875454838766,
  "waist_mean_closure_gap": 5.496121335824e-10,
  "waist_turn_number": 0.9999999994126115,
  "waist_total_turn": 6.283185303488915,
  "outer_C_mean_minus_reference": 2.4080131862111467e-55,
  "normalized_outer_regular_linear_residual_l1": 7.165319263937279e-30,
  "maximum_boundary_residual": 2.0122934192040947e-22,
  "outer_linear_height_homogeneous_A2_norm": 1.6162997110210753e-12,
  "guess_path": "notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz",
  "guess_sha256": "4046eb7ac8da162ab9aad9fcb4991933200abdbc2c22ed6329d49bb13d72b856",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-outer-mean-m128-v7-b8-n1024-candidate.json",
  "candidate_sha256": "15952f4245b7c4214f58f32a68ca64a875caa7a23d3c0b3b8d7c11321db349c6",
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_branch_probe.py": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_codazzi_candidate_shards.py": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "fourfold_codazzi_chunked_collocation.py": "5b96d9298014703cf41c59a2d9466e81d523673fb659a52ca6488a03ef939a73",
    "fourfold_codazzi_compact_metric_fast_jacobian.py": "0d82b18aaed063660f7003e36061958a327d134c67490adb7b340deddfc90c17",
    "fourfold_codazzi_guarded_Newton_krylov.py": "03e466ef693694b6dc94e0f88328e842ecc435ba031572f2a83578776bf5ff9e",
    "fourfold_codazzi_matrix_free_fft_collocation.py": "bb1095f2635ae3961b4b25ae50ae84d2007e02ca1268ffdd1b8348d4484a5600",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Only the LU preconditioner is sparsified; GMRES uses the full untruncated finite Jacobian action and checks its residual. The full nonlinear system and diagnostics are unchanged.",
    "Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.",
    "The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.",
    "The opposite mean boundary is printed, not silently set to zero.",
    "True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.",
    "The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred."
  ],
  "wall_seconds": 119.80191131099855
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "guarded_Newton_history": {
    "bytes": 580,
    "sha256": "646bb00287f82b893fbc325b1cd6bcb344ef4b2ed1076d40711c778b215c87b3"
  },
  "approximate_linear_solver_history": {
    "bytes": 2331,
    "sha256": "21496907cdd1cd074d1d703efb54f704bee6928f2e38e92dbe7b056b2abc6d64"
  },
  "waist_B_coefficients": {
    "bytes": 1307,
    "sha256": "dd176e6e5335060db35e63e734fd927291021d24b7391814f1271565381dac12"
  },
  "waist_C_coefficients": {
    "bytes": 3586,
    "sha256": "d233dd287f8ea373c724a1ed10dd2ba3c70dd722c54fae1b69d4ed1591896fa9"
  },
  "outer_B_coefficients": {
    "bytes": 3562,
    "sha256": "697c9ca60c2ee58897626c990cf644469e805b188f5f30ac79defe4d6b27da93"
  },
  "outer_C_coefficients": {
    "bytes": 3599,
    "sha256": "0cd89aa19a516b4e958353cca25653512560be2ca062ac7f5ef216c1a90131da"
  },
  "outer_linear_height_estimate": {
    "bytes": 3575,
    "sha256": "3d255af4f07c37f0ac41742788bacd6afdd4a29eea58357e5fb7c31074ceb3db"
  }
}
```

## 9. 2026-11-13-R133-compact-metric-outer-mean-m16-floating.json

完整原件：50314 B；Git `cd0ac81be9f9c49132f534e37482b10cdd8dfca9`；SHA256 `cdcda6148f06bf47d59dab8e1e0cc3bd6f3d5054d1ec63d4c7d101f16a902461`。

以下字段与第0节共同组成全部未省略的原顶层字段，值使用原JSON token，未重算浮点或改写原资格。

```json
{
  "kind": "floating_compact_metric_normalized_Codazzi_branch",
  "modes": 16,
  "amplitude": 0.65,
  "nu": -0.015865248827379504,
  "exact_float_nu": "-2286423318628049/144115188075855872",
  "source_sha256": "e1692ce4e7b1090adb0aeab7414f8df32411072283cedad3d848ca4fb18ef0a4",
  "mean_boundary": "outer",
  "finite_BVP_success": true,
  "reached_requested_amplitude": true,
  "requested_amplitudes": [
    0.0,
    0.025,
    0.05,
    0.1,
    0.2,
    0.35,
    0.5,
    0.65
  ],
  "angular_grid": 256,
  "diagnostic_angular_grid": 512,
  "tol": 2e-07,
  "max_nodes": 3500,
  "analytic_Jacobian_audit": {
    "passed": true,
    "diagnostic_only": true,
    "radial_points": [
      0.02,
      0.08,
      0.12,
      0.17,
      0.25,
      1.0,
      3.07
    ],
    "central_step": 1e-06,
    "parameter_relative_error": 1.1169088520440799e-10,
    "state_relative_errors": [
      1.0821745672150946e-10,
      1.1689628715987893e-10,
      5.6941134957200417e-11,
      3.453638265554034e-12
    ]
  },
  "seed_rhs_calls": 12059,
  "seed_waist_q": -1.2362284481249458e-08,
  "seed_message": "The solver successfully reached the end of the integration interval.",
  "candidate_path": "notes/2026-11-13-R133-compact-metric-outer-mean-m16-candidate.npz.gz",
  "candidate_sha256": "45a0066ded3dc823dcb3dfc36d09ff29fbbdc4a0ebac08a9ec201c4f28dd4545",
  "failed_candidate_path": null,
  "failed_candidate_sha256": null,
  "dependency_sha256": {
    "fourfold_codazzi_compact_metric_return_probe.py": "6b857134df75524e0fffcaa163212bfbb03c3edffee983f27cde3f9357ab9a38",
    "fourfold_phase_codazzi_two_end_probe.py": "510a0ebf823f35942c0b45e67fb3ec5319cfe124996d88656fcc18a52c565eb2",
    "fourfold_phase_codazzi_rotational_reference_probe.py": "c8495d0c1721a21a24b48c8cdce9e825a8110f4923edd01e9eb2b7fe76b2d411",
    "fourfold_codazzi_rotational_cap_jacobi_probe.py": "2bfb4c8d7bca6ffe75d6496f8f9c3baa17ba5ee83045c6ca09dc475853d30114",
    "fourfold_phase_symmetric_geometry.py": "322205cff55ed31a7eeca478880e1716917958741f9eaf4ad56b12b0cae575ad",
    "fourfold_phase_geometry.py": "ef3e8261afd187bd97637f65d90f25048ad25accaaeb479097b5875e0db2e937"
  },
  "limitations": [
    "Floating finite Fourier/radial boundary model, no continuous PDE or parameter certificate.",
    "nu changes the target on .05<|r|<.18; existing g0 proofs do not transfer there.",
    "The waist curve is also changed by the complementary C modes; old exact waist Cauchy branches are not reused.",
    "The selected mean boundary is explicit; the opposite mean is an output, not an erased matching row.",
    "Every nonlinear regular tail term, true non-fourth-mode linear fee, mean height and flux remain unpaid.",
    "The normalized alpha=0 result is a Jacobi eigenfunction; it is not a nonrotational nonlinear surface.",
    "Neither a guard stop nor a large residual is a mathematical nonexistence theorem."
  ],
  "wall_seconds": 371.87412145500275
}
```

仅在本索引省略的大字段仍由整件恢复元组唯一确定；下列身份采用原字段 token 加单个LF，非重序列化值。

```json
{
  "attempts": {
    "bytes": 45999,
    "sha256": "c6ed83ffcd17b09059a9d4a8f15990c3f53af107fa74fdd572329e8a3dea6f42"
  }
}
```

原 attempts 全长 8。逐项的完整非数组向量资格与诊断如下；每项的省略原字段均有自身身份，完整attempts仍在原文件内。

### attempt 0

```json
{
  "amplitude": 0.0,
  "nu": 0.0009455601093559079,
  "exact_float_nu": "8721252671798625/9223372036854775808",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1250,
  "diagnostics": {
        "normalized_finite_residual": 1.2557144076986802e-06,
        "normalized_full_B_residual": 1.2557144267720012e-06,
        "normalized_full_C_residual": 6.078251050811723e-07,
        "normalized_A_projection_defect": 3.552713678800501e-15,
        "C_min": -0.9356875460334886,
        "C_max": -0.1710388544245141,
        "B_abs_max": 0.0,
        "actual_full_B_residual": 0.0,
        "actual_full_C_residual": 0.0,
        "actual_A_projection_defect": 0.0,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 4997,
        "valid": true
      },
  "waist_mean_C": -0.9356875460334886,
  "waist_mean_closure_gap": 1.1102230246251565e-16,
  "waist_turn_number": 0.9999999999999999,
  "waist_total_turn": 6.283185307179585,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 1.1823455792740644e-44,
  "maximum_boundary_residual": 4.791828111072997e-29
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 3071,
    "sha256": "eaa50667602b805256cb787f56d08285d964a5abfaf825ed3ef77cc652650fe2"
  },
  "waist_B_coefficients": {
    "bytes": 221,
    "sha256": "82de3d4fb1505fc3f474a9978e35856258a402d83c73deebcd9712750c136e5d"
  },
  "waist_C_coefficients": {
    "bytes": 258,
    "sha256": "35fab70c2fcdb31bfdf0944a46d6af4b7cb12edf6f8aed4b4132f6cbf4fda594"
  },
  "outer_B_coefficients": {
    "bytes": 221,
    "sha256": "37e7d0b812612c44e47273d747411c0597927dadca2b1c9f3297ae4472faa6cc"
  },
  "outer_C_coefficients": {
    "bytes": 258,
    "sha256": "539d50f17165a84432fd1346fe52a912bde216fd81ec80ef26d3e4736a9f3b6a"
  }
}
```

### attempt 1

```json
{
  "amplitude": 0.025,
  "nu": 0.0009138559314120141,
  "exact_float_nu": "8428833243499447/9223372036854775808",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1252,
  "diagnostics": {
        "normalized_finite_residual": 1.2562967697377979e-06,
        "normalized_full_B_residual": 1.2562967856338727e-06,
        "normalized_full_C_residual": 6.104022773345541e-07,
        "normalized_A_projection_defect": 3.1086244689504383e-15,
        "C_min": -0.9613829725856808,
        "C_max": -0.17103885442449382,
        "B_abs_max": 0.01592454931949856,
        "actual_full_B_residual": 3.140741964084682e-08,
        "actual_full_C_residual": 1.5260056933363852e-08,
        "actual_A_projection_defect": 7.771561172376097e-17,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 5005,
        "valid": true
      },
  "waist_mean_C": -0.9356875460335,
  "waist_mean_closure_gap": -1.1324274851176597e-14,
  "waist_turn_number": 1.0000000000000122,
  "waist_total_turn": 6.283185307179662,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 1.0739639011739418e-44,
  "maximum_boundary_residual": 3.0644171614401563e-27
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 1676,
    "sha256": "9d5be641c714a8cd3afeacafbd4c855a2fa1d4392294054ca46a43dd7add4631"
  },
  "waist_B_coefficients": {
    "bytes": 309,
    "sha256": "8ba419acdbd9dbb89f1db0135d940903d811e35a68d86dba26a34286c14fbf68"
  },
  "waist_C_coefficients": {
    "bytes": 531,
    "sha256": "18b23363134fb6e767973bf9f88a2b714dc2926af27fce45e2c6fd64db54e255"
  },
  "outer_B_coefficients": {
    "bytes": 510,
    "sha256": "0d889a59dceee7e6839e73e5b62d78a7a943cd792408f9d23763f2dd25daeb8b"
  },
  "outer_C_coefficients": {
    "bytes": 551,
    "sha256": "e15aba4133803717490b794407de807b3fdfc7bc30eaf94babec769f9da1e181"
  }
}
```

### attempt 2

```json
{
  "amplitude": 0.05,
  "nu": 0.000818675788676831,
  "exact_float_nu": "7550951376531913/9223372036854775808",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1255,
  "diagnostics": {
        "normalized_finite_residual": 1.2580484054971183e-06,
        "normalized_full_B_residual": 1.2581180406072033e-06,
        "normalized_full_C_residual": 6.125060495049128e-07,
        "normalized_A_projection_defect": 3.3306690738754696e-15,
        "C_min": -0.9885586778922393,
        "C_max": -0.17103885442447353,
        "B_abs_max": 0.03187032444161645,
        "actual_full_B_residual": 6.290590203036017e-08,
        "actual_full_C_residual": 3.0625302475245644e-08,
        "actual_A_projection_defect": 1.6653345369377348e-16,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 5017,
        "valid": true
      },
  "waist_mean_C": -0.9356875460335342,
  "waist_mean_closure_gap": -4.551914400963142e-14,
  "waist_turn_number": 1.0000000000000486,
  "waist_total_turn": 6.283185307179892,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 1.7428649650039912e-44,
  "maximum_boundary_residual": 7.336025957113427e-28
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 1674,
    "sha256": "cee91b82679aa3cc31245d203f46ea00ec3735c194ea0dd38bd48e43a6d2e01f"
  },
  "waist_B_coefficients": {
    "bytes": 292,
    "sha256": "eb202db6cb030121fd941bf033cad7d9a232da86053fcb79efbd27c085083bb9"
  },
  "waist_C_coefficients": {
    "bytes": 541,
    "sha256": "a5e09f281735316f6190511486edff8f8d8c0bbd0bc6650b1010aba443b3157f"
  },
  "outer_B_coefficients": {
    "bytes": 508,
    "sha256": "1e0e090835a0549a2c60ae87080ee3430c3d57b54ab658e53315db4376bead60"
  },
  "outer_C_coefficients": {
    "bytes": 553,
    "sha256": "0f0fd413474f6cadc381aa3efe875fb459629655e0e9cc32d8d08e8bf08116ec"
  }
}
```

### attempt 3

```json
{
  "amplitude": 0.1,
  "nu": 0.00043693320237164166,
  "exact_float_nu": "8059994961456017/18446744073709551616",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1258,
  "diagnostics": {
        "normalized_finite_residual": 1.265404133418973e-06,
        "normalized_full_B_residual": 1.2654035129310449e-06,
        "normalized_full_C_residual": 6.02145470859905e-07,
        "normalized_A_projection_defect": 1.199040866595169e-14,
        "C_min": -1.0479606567356077,
        "C_max": -0.17103885442443284,
        "B_abs_max": 0.06391016436611233,
        "actual_full_B_residual": 1.265403512931045e-07,
        "actual_full_C_residual": 6.02145470859905e-08,
        "actual_A_projection_defect": 1.1990408665951691e-15,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 5029,
        "valid": true
      },
  "waist_mean_C": -0.935687546033663,
  "waist_mean_closure_gap": -1.7430501486614958e-13,
  "waist_turn_number": 1.0000000000001863,
  "waist_total_turn": 6.283185307180757,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 2.5223372357846707e-44,
  "maximum_boundary_residual": 1.3575134288471821e-28
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 2115,
    "sha256": "02d096cdb20b9e3fbf1e055e6596773a859621cdd4dcf95c3ab2381d25cbc647"
  },
  "waist_B_coefficients": {
    "bytes": 291,
    "sha256": "9de365c00f0acaf9cb8b498e98964b2ef0fca7c57ce270b675aa3cd00f0cd3b9"
  },
  "waist_C_coefficients": {
    "bytes": 536,
    "sha256": "b08045760a29f218fb8c0d2b2fc7330f21202f04f477533cbc99491a29643886"
  },
  "outer_B_coefficients": {
    "bytes": 518,
    "sha256": "fa22c4327ad3906beb37ae17a366a920fd6f0031229616750bb2ca357be874c6"
  },
  "outer_C_coefficients": {
    "bytes": 554,
    "sha256": "8f3d7fb68ae2efd4a83b3a6e52a8818bda65b54d7323caa6a2f8c61086c938ef"
  }
}
```

### attempt 4

```json
{
  "amplitude": 0.2,
  "nu": -0.001106686097516335,
  "exact_float_nu": "-5103688802704051/4611686018427387904",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1274,
  "diagnostics": {
        "normalized_finite_residual": 1.0618557605981086e-06,
        "normalized_full_B_residual": 1.088305509766574e-06,
        "normalized_full_C_residual": 5.846870233527923e-07,
        "normalized_A_projection_defect": 6.390050710791684e-10,
        "C_min": -1.1925895083037121,
        "C_max": -0.17103885442435082,
        "B_abs_max": 0.12921350811488336,
        "actual_full_B_residual": 2.176611019533148e-07,
        "actual_full_C_residual": 1.1693740467055847e-07,
        "actual_A_projection_defect": 1.2780101421583367e-10,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 5093,
        "valid": true
      },
  "waist_mean_C": -0.9356875460342002,
  "waist_mean_closure_gap": -7.115419364822628e-13,
  "waist_turn_number": 1.0000000000007605,
  "waist_total_turn": 6.283185307184364,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 2.3471749277440686e-44,
  "maximum_boundary_residual": 5.825602066952182e-27
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 2123,
    "sha256": "8feb1648fe4fadaffb6eb35be72280b10edbf41a55c0f65fd23cc66906f70070"
  },
  "waist_B_coefficients": {
    "bytes": 295,
    "sha256": "7fe7f62e3abca9d06a9449e81cdf877ae119587c9f234d83e146acadcc072099"
  },
  "waist_C_coefficients": {
    "bytes": 535,
    "sha256": "eadadd61eef5d09cf45b23bac43dcb9b4c875580731e78717fd02b874e8e5fa0"
  },
  "outer_B_coefficients": {
    "bytes": 514,
    "sha256": "76f64705ab8d035cd70999119978829789fb037748a17bbd67612fc88e0829c0"
  },
  "outer_C_coefficients": {
    "bytes": 553,
    "sha256": "e413aa29ba3f6f29113e47db0345304dbaa67a669aa4a02cf45222c293d7c3d8"
  }
}
```

### attempt 5

```json
{
  "amplitude": 0.35,
  "nu": -0.005497206087777065,
  "exact_float_nu": "-6337847113853853/1152921504606846976",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1312,
  "diagnostics": {
        "normalized_finite_residual": 1.0978725953082079e-06,
        "normalized_full_B_residual": 0.0002772048650805066,
        "normalized_full_C_residual": 5.195239660554796e-07,
        "normalized_A_projection_defect": 3.925041626162695e-06,
        "C_min": -1.5146352604510536,
        "C_max": -0.1710388544242246,
        "B_abs_max": 0.23333325559484086,
        "actual_full_B_residual": 9.70217027781773e-05,
        "actual_full_C_residual": 1.8183338811941784e-07,
        "actual_A_projection_defect": 1.3737645691569433e-06,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 5245,
        "valid": true
      },
  "waist_mean_C": -0.935687546033158,
  "waist_mean_closure_gap": 3.3073543903583413e-13,
  "waist_turn_number": 0.9999999999996466,
  "waist_total_turn": 6.283185307177365,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 3.0144338449362373e-44,
  "maximum_boundary_residual": 1.132055138368642e-25
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 2552,
    "sha256": "d1fb8d0b44d2508cde18b870206fb64f986f355a013bbe5fc82fb61e5825864b"
  },
  "waist_B_coefficients": {
    "bytes": 311,
    "sha256": "f374acc9d191e0cea72401d191fa24927dd937ec39b2103c37ed401e71a4c5eb"
  },
  "waist_C_coefficients": {
    "bytes": 528,
    "sha256": "d29be2916619ef1f2bc6fd28bc724ac227072cf851d7bf1c93ce63709485b443"
  },
  "outer_B_coefficients": {
    "bytes": 508,
    "sha256": "ac1136b492d84b64bed0561da6f9a63d05347fab0653287b8e36c1a3e37018e6"
  },
  "outer_C_coefficients": {
    "bytes": 554,
    "sha256": "e40c2a12b558b064538e217c7727dc5bac4809e0e9a97c0ffac6c82361a3845e"
  }
}
```

### attempt 6

```json
{
  "amplitude": 0.5,
  "nu": -0.012749527717567852,
  "exact_float_nu": "-3674801169791257/288230376151711744",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1365,
  "diagnostics": {
        "normalized_finite_residual": 9.356454063260235e-07,
        "normalized_full_B_residual": 0.05193008283118971,
        "normalized_full_C_residual": 2.8589236353931957e-05,
        "normalized_A_projection_defect": 0.0007289014281472994,
        "C_min": -2.1161918954501213,
        "C_max": -0.1710388544240914,
        "B_abs_max": 0.35193176493350137,
        "actual_full_B_residual": 0.025965041415594855,
        "actual_full_C_residual": 1.4294618176965979e-05,
        "actual_A_projection_defect": 0.0003644507140736497,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 5457,
        "valid": true
      },
  "waist_mean_C": -0.935687546163302,
  "waist_mean_closure_gap": -1.2981327124350628e-10,
  "waist_turn_number": 1.0000000001387357,
  "waist_total_turn": 6.283185308051288,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 1.9399225615496686e-44,
  "maximum_boundary_residual": 2.5814366673753987e-27
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 2543,
    "sha256": "26affd793a61b5b4b803599d3e6a8421694f7f1cf5a56ee6c3b8be115ec8d4f2"
  },
  "waist_B_coefficients": {
    "bytes": 256,
    "sha256": "0b52959be74f80df51dbac124de5e5aa958f53ec6a8790af74862cdb1e8fa1ff"
  },
  "waist_C_coefficients": {
    "bytes": 512,
    "sha256": "16d02f79c7a4081ecb5c0854d0ee4bd83d4bc243c4350569af229692aa58fcfb"
  },
  "outer_B_coefficients": {
    "bytes": 517,
    "sha256": "11dffc20ad379c9c8e48079401d6cc5c822fbdd15a85d6ce7e8d91045bf46a30"
  },
  "outer_C_coefficients": {
    "bytes": 550,
    "sha256": "6919f38583b3078c979f2f83971d5c0d5093f525f20292c97f8416f5267436e3"
  }
}
```

### attempt 7

```json
{
  "amplitude": 0.65,
  "nu": -0.015865248827379504,
  "exact_float_nu": "-2286423318628049/144115188075855872",
  "success": true,
  "solver_status": 0,
  "solver_message": "The algorithm converged to the desired accuracy.",
  "radial_nodes": 1756,
  "diagnostics": {
        "normalized_finite_residual": 1.017293508528639e-06,
        "normalized_full_B_residual": 1.9921605047776492,
        "normalized_full_C_residual": 0.0015032621005553748,
        "normalized_A_projection_defect": 0.026469476221952393,
        "C_min": -3.557051565733527,
        "C_max": -0.17103885442394612,
        "B_abs_max": 0.5119454402337122,
        "actual_full_B_residual": 1.294904328105472,
        "actual_full_C_residual": 0.0009771203653609936,
        "actual_A_projection_defect": 0.017205159544269055,
        "radial_samples": "nodes and quarter/mid/three-quarter points",
        "radial_sample_count": 7021,
        "valid": true
      },
  "waist_mean_C": -0.9356877982216294,
  "waist_mean_closure_gap": -2.5218814070360196e-07,
  "waist_turn_number": 1.0000002695217456,
  "waist_total_turn": 6.2831870006346575,
  "outer_C_mean_minus_reference": 0.0,
  "normalized_outer_regular_linear_residual_l1": 3.512004276214073e-44,
  "maximum_boundary_residual": 4.831549773756172e-26
}
```

```json
{
  "guarded_Newton_history": {
    "bytes": 4029,
    "sha256": "bd7d6321fa505265562f6687c341d707a4ffa12d0c25cff0610eaacdbb7e0ea1"
  },
  "waist_B_coefficients": {
    "bytes": 270,
    "sha256": "4486748dd187eba1e3704ceeb52eda4bbe8ccced0216bfe3b3250f8f576298ad"
  },
  "waist_C_coefficients": {
    "bytes": 501,
    "sha256": "73e66731350d5a58d00915c10d552696bf27010b29d4d818bc7b5ba5ca746e5b"
  },
  "outer_B_coefficients": {
    "bytes": 514,
    "sha256": "e15d2f91166db27878981837a8dc99e37dcf84b4e4f4ef1093efe1195c5359c9"
  },
  "outer_C_coefficients": {
    "bytes": 549,
    "sha256": "fd7e2d1754bb4c31a920a578e4bc3caacdd303241fddbd68c21887d0e1f3b681"
  }
}
```
