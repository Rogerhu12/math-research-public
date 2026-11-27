# 公开13真实入口异常：normal构造的底层来源约束

原始science/pure两次失败已在[前记录](2026-11-27-run13-entry-failure-and-run14-actual-reference.md)登记。现在同一run46028002241/1中两个原异常链读取器均真实返0；这次得到的是原日志中的实际异常，不是重跑求解或推测数值原因。

## 科学入口

原log为6797B，whole SHA256 f1ab18fb5f5da2d736fed5eb0455a5fe61d10261c05511cf3f547ef63bf89887。读取的tail实际包含全日志，第一traceback未截断：

```text
Traceback (most recent call last):
  File "/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py", line 1094, in <module>
    main()
  File "/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py", line 544, in main
    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_angular_refined_normal_lift.py", line 257, in __init__
    raise ValueError('This complete normal layer binds its actual independent supported-smooth-triangle base source')
ValueError: This complete normal layer binds its actual independent supported-smooth-triangle base source

```

实际链是driver c64d在main构造q，进入normal2db0的__init__，在实际base source/schema约束抛ValueError。外层launcher的CalledProcessError只是传播此错误，不能拿外层异常代替inner原因。当前证据未单独区分该复合guard的哪一个布尔子句；完整源码定位和最小修复继续，不扩大可接收模型集合。

## 后续纯读取

原pure log1723B，whole SHA2566668fba14c096b42f02dff93c8e11407870885944165c86b2d41283f96074611，读取包含全日志且第一traceback未截断。完整reader在读取实际scientific report时FileNotFoundError；该报告确未生成。没有pure验证成功、完整物理场、accepted方向、final、typed增量或费用结论。

## 两个真实只读返回的完整紧凑记录

```json
[
  {
    "step_id": "read-actual13-science-first-and-last-original-failure-tracebacks-20261127",
    "returncode": 0,
    "seconds": 6.198117221000075,
    "source_sha256": "5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360",
    "source_commit": "0a7d89b08543cba92c609adee44b980de8f95a57",
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/postprocess/actual13-science-first-and-last-original-tracebacks.json",
        "sha256": "b126f8b6cab07c5d7874e0d27f038e3742303b8a6d9e018e60faa94f8d764c3c",
        "bytes": 11320
      }
    ],
    "metrics": {
      "postprocess/actual13-science-first-and-last-original-tracebacks.json": {
        "schema": "actual-public-followup-first-and-last-failure-tracebacks-v1",
        "source_sha256": "5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360",
        "derived_from_source_sha256": "ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338",
        "status_sha256": "65e42c8517d07972e2ca98c1090e6c595285a2b7ae1a0699612c72568a68529d",
        "status_sha256_scope": "exact captured status bytes, not a later mutable status version",
        "step_id": "complete-fixed-fejer-angular-N4096-independent-20261127",
        "actual_source_sha256": "e93b1ef25a24a3f925a33b4c323a7b31dc93b42bd2bda1aca887d8f89aa73e52",
        "actual_source_commit": "50e4489cdfa544d4c16463d5bfe3624231e29c23",
        "actual_returncode": 1,
        "actual_recorded_seconds": 8.492643880999935,
        "actual_log_path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/followup-logs/0003-4b2537518a1d.log",
        "actual_log_sha256": "f1ab18fb5f5da2d736fed5eb0455a5fe61d10261c05511cf3f547ef63bf89887",
        "actual_log_bytes": 6797,
        "log_unchanged_during_read": true,
        "tail_start_byte": 0,
        "tail_bytes_read": 6797,
        "maximum_tail_bytes": 64000,
        "captured_tail_contains_entire_log": true,
        "captured_tail_sha256": "f1ab18fb5f5da2d736fed5eb0455a5fe61d10261c05511cf3f547ef63bf89887",
        "traceback_markers_in_captured_tail": 2,
        "first_traceback_found": true,
        "first_traceback_start_byte": 0,
        "first_traceback_is_first_in_entire_log": true,
        "first_traceback_excerpt": "Traceback (most recent call last):\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py\", line 1094, in <module>\n    main()\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py\", line 544, in main\n    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],\n        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_angular_refined_normal_lift.py\", line 257, in __init__\n    raise ValueError('This complete normal layer binds its actual independent supported-smooth-triangle base source')\nValueError: This complete normal layer binds its actual independent supported-smooth-triangle base source\n",
        "first_traceback_excerpt_clipped": false,
        "first_traceback_final_nonempty_line": "ValueError: This complete normal layer binds its actual independent supported-smooth-triangle base source",
        "first_traceback_final_line_clipped": false,
        "last_traceback_found": true,
        "last_traceback_start_byte": 1215,
        "last_traceback_excerpt": "Traceback (most recent call last):\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_angular_refined_actions.py\", line 342, in <module>\n    main()\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_angular_refined_actions.py\", line 338, in main\n    subprocess.run(command, env=env, cwd=args.repo, check=True)\n  File \"/opt/hostedtoolcache/Python/3.12.14/x64/lib/python3.12/subprocess.py\", line 571, in run\n    raise CalledProcessError(retcode, process.args,\nsubprocess.CalledProcessError: Command '['/opt/hostedtoolcache/Python/3.12.14/x64/bin/python', '-u', '/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py', '--repo', '/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5', '--reference-bundle', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/reference.npz', '--preparation-report', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/report.json', '--carrier', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/observations.npz', '--node-report', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json', '--scalar-input', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json', '--outdir', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent', '--manifest', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/locations.json', '--material-envelope-binding', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json', '--independent-envelope-branch', '--pending-parallel-envelope-run', '45909290354/1', '--pending-parallel-envelope-run', '45929088658/1', '--pending-parallel-envelope-run', '45943410994/1', '--pending-parallel-envelope-run', '45972294636/1', '--pending-parallel-envelope-run', '46011377225/1', '--pending-parallel-envelope-source', '45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5', '--pending-parallel-envelope-source', '45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9', '--pending-parallel-envelope-source', '45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5', '--pending-parallel-envelope-source', '45972294636/1=c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1', '--pending-parallel-envelope-source', '46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd', '--envelope-near-active-rows', '32', '--angles', '4096', '--stage-block', '64', '--angle-block', '8', '--integration-order', '8', '--inverse-root-iterations', '18', '--inverse-root-tolerance', '2e-12', '--norm-kind', 'jet-sum', '--radial-norm-length', '0.05', '--angular-transition', '24.0', '--torch-threads', '4', '--damping', '0.01', '--directions', '1', '--maxiter', '16', '--restoration-directions', '4', '--restoration-damping', '0.01', '--restoration-maxiter', '64', '--line-trials', '15', '--qp-atol', '0.0', '--qp-rtol', '1e-06', '--qp-feasibility-tolerance', '2e-11', '--qp-rank-tolerance', '2e-12', '--active-rows', '192', '--active-block-columns', '32768', '--active-band', '0.025', '--reach-ratio', '0.03', '--reach-safety-factor', '0.992', '--marked-diameter-budget', '4.2', '--witness-lower-budget', '0.9', '--amplitude-height-floor', '1.01', '--amplitude-top-radius', '2', '--amplitude-top-distance', '4', '--spectral-p', '4', '--spectral-epsilon', '0.001', '--spectral-scale', '0.05', '--legacy-fraction', '0.5', '--target', '1e-09', '--panels', '128', '--seed-boundary-total-length', '1/16', '--seed-profile-delta', '1/128', '--seed-radial-quadrature-order', '8', '--seed-profile-quadrature-order', '16', '--seed-mean-maxiter', '128', '--seed-mean-tolerance', '2e-12', '--seed-mean-backtracks', '24', '--seed-mean-armijo', '0.0001', '--seed-scalar-iterations', '64', '--endpoint-bubble-1-left', '1/32', '--endpoint-bubble-1-middle', '1/4', '--endpoint-bubble-1-right', '15/32', '--endpoint-bubble-2-left', '17/32', '--endpoint-bubble-2-middle', '3/4', '--endpoint-bubble-2-right', '31/32', '--endpoint-root-tolerance', '2e-12', '--endpoint-root-iterations', '24', '--endpoint-root-backtracks', '18', '--endpoint-root-armijo', '0.0001', '--endpoint-control-radius', '2.0', '--normal-stages', '32', '--gamma-left', '1/16', '--gamma-middle', '1/8', '--gamma-right', '3/16', '--moment-input', '/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json', '--moment-input-sha256', 'df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c', '--moment-definition-sha256', '05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e', '--moment-input-binding', 'supported-smooth-triangle-reference']' returned non-zero exit status 1.\n",
        "last_traceback_excerpt_clipped": false,
        "last_traceback_final_nonempty_line": "subprocess.CalledProcessError: Command '['/opt/hostedtoolcache/Python/3.12.14/x64/bin/python', '-u', '/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_angular_refined_so3_qp.py', '--repo', '/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5', '--reference-bundle', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/reference.npz', '--preparation-report', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/report.json', '--carrier', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/observations.npz', '--node-report', '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json', '--scalar-input', '/hom\n[bounded diagnostic: middle characters omitted]\n-left', '1/32', '--endpoint-bubble-1-middle', '1/4', '--endpoint-bubble-1-right', '15/32', '--endpoint-bubble-2-left', '17/32', '--endpoint-bubble-2-middle', '3/4', '--endpoint-bubble-2-right', '31/32', '--endpoint-root-tolerance', '2e-12', '--endpoint-root-iterations', '24', '--endpoint-root-backtracks', '18', '--endpoint-root-armijo', '0.0001', '--endpoint-control-radius', '2.0', '--normal-stages', '32', '--gamma-left', '1/16', '--gamma-middle', '1/8', '--gamma-right', '3/16', '--moment-input', '/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0003-4b2537518a1d-50e4489cdfa5/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json', '--moment-input-sha256', 'df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c', '--moment-definition-sha256', '05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e', '--moment-input-binding', 'supported-smooth-triangle-reference']' returned non-zero exit status 1.",
        "last_traceback_final_line_clipped": true,
        "first_and_last_are_same_traceback": false,
        "no_traceback_tail_excerpt": "",
        "no_traceback_tail_excerpt_clipped": false,
        "maximum_excerpt_characters": 7000,
        "traceback_scope": "first and last markers in bounded original log tail; no missing prefix inferred",
        "complete_log_published": false,
        "scientific_arrays_read": false,
        "scientific_reports_read": false,
        "field_or_J_evaluations": 0,
        "numerical_failure_cause_inferred": false,
        "github_run_id": "46028002241",
        "github_run_attempt": "1"
      }
    },
    "summary_errors": [],
    "missing_outputs": []
  },
  {
    "step_id": "read-actual13-pure-first-and-last-original-failure-tracebacks-20261127",
    "returncode": 0,
    "seconds": 6.202091429999882,
    "source_sha256": "5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360",
    "source_commit": "fc5217507366eac0ceb13e13863b522b9a59a83e",
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/postprocess/actual13-pure-first-and-last-original-tracebacks.json",
        "sha256": "6f4e32151f221a88e159d711321f64f175d602b633014c24d3d0b128c185c0b5",
        "bytes": 6189
      }
    ],
    "metrics": {
      "postprocess/actual13-pure-first-and-last-original-tracebacks.json": {
        "schema": "actual-public-followup-first-and-last-failure-tracebacks-v1",
        "source_sha256": "5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360",
        "derived_from_source_sha256": "ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338",
        "status_sha256": "03a5fc80c8f15b9c1e2ea894f996cd52ca0bdcdf6d5a97ce98ea899bf369786f",
        "status_sha256_scope": "exact captured status bytes, not a later mutable status version",
        "step_id": "actual-fixed-fejer-angular-N4096-independent-20261127",
        "actual_source_sha256": "7ffea5bfda0108af0276e60a16c29e15669e3ad5996331cf35bdf369d9659507",
        "actual_source_commit": "f515d65bcfcf76aa07d1001f3f81605192ab424d",
        "actual_returncode": 1,
        "actual_recorded_seconds": 6.1936070869999185,
        "actual_log_path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/followup-logs/0004-3e1018ad9af6.log",
        "actual_log_sha256": "6668fba14c096b42f02dff93c8e11407870885944165c86b2d41283f96074611",
        "actual_log_bytes": 1723,
        "log_unchanged_during_read": true,
        "tail_start_byte": 0,
        "tail_bytes_read": 1723,
        "maximum_tail_bytes": 64000,
        "captured_tail_contains_entire_log": true,
        "captured_tail_sha256": "6668fba14c096b42f02dff93c8e11407870885944165c86b2d41283f96074611",
        "traceback_markers_in_captured_tail": 1,
        "first_traceback_found": true,
        "first_traceback_start_byte": 0,
        "first_traceback_is_first_in_entire_log": true,
        "first_traceback_excerpt": "Traceback (most recent call last):\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0004-3e1018ad9af6-f515d65bcfcf/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_angular_refined_so3_report.py\", line 1398, in <module>\n    main()\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0004-3e1018ad9af6-f515d65bcfcf/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_angular_refined_so3_report.py\", line 1389, in main\n    result = read_report(a.repo, a.report, verify_final_bundle=a.verify_final_bundle)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0004-3e1018ad9af6-f515d65bcfcf/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_angular_refined_so3_report.py\", line 1122, in read_report\n    report = json.loads(Path(report_path).read_text())\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.12.14/x64/lib/python3.12/pathlib.py\", line 1027, in read_text\n    with self.open(mode='r', encoding=encoding, errors=errors) as f:\n         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.12.14/x64/lib/python3.12/pathlib.py\", line 1013, in open\n    return io.open(self, mode, buffering, encoding, errors, newline)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nFileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent/report.json'\n",
        "first_traceback_excerpt_clipped": false,
        "first_traceback_final_nonempty_line": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent/report.json'",
        "first_traceback_final_line_clipped": false,
        "last_traceback_found": true,
        "last_traceback_start_byte": 0,
        "last_traceback_excerpt": "Traceback (most recent call last):\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0004-3e1018ad9af6-f515d65bcfcf/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_angular_refined_so3_report.py\", line 1398, in <module>\n    main()\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0004-3e1018ad9af6-f515d65bcfcf/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_angular_refined_so3_report.py\", line 1389, in main\n    result = read_report(a.repo, a.report, verify_final_bundle=a.verify_final_bundle)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/runner/work/_temp/visible-larger-research-46028002241-1/followup-sources/0004-3e1018ad9af6-f515d65bcfcf/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_angular_refined_so3_report.py\", line 1122, in read_report\n    report = json.loads(Path(report_path).read_text())\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.12.14/x64/lib/python3.12/pathlib.py\", line 1027, in read_text\n    with self.open(mode='r', encoding=encoding, errors=errors) as f:\n         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.12.14/x64/lib/python3.12/pathlib.py\", line 1013, in open\n    return io.open(self, mode, buffering, encoding, errors, newline)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nFileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent/report.json'\n",
        "last_traceback_excerpt_clipped": false,
        "last_traceback_final_nonempty_line": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent/report.json'",
        "last_traceback_final_line_clipped": false,
        "first_and_last_are_same_traceback": true,
        "no_traceback_tail_excerpt": "",
        "no_traceback_tail_excerpt_clipped": false,
        "maximum_excerpt_characters": 7000,
        "traceback_scope": "first and last markers in bounded original log tail; no missing prefix inferred",
        "complete_log_published": false,
        "scientific_arrays_read": false,
        "scientific_reports_read": false,
        "field_or_J_evaluations": 0,
        "numerical_failure_cause_inferred": false,
        "github_run_id": "46028002241",
        "github_run_attempt": "1"
      }
    },
    "summary_errors": [],
    "missing_outputs": []
  }
]
```

[完整阶段1–6原卷](https://github.com/Rogerhu12/math-research-public/blob/882086668df076632531f609a83a172dfe75d473/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46028002241-1-part-001.md)57966B，whole SHA25683cb443967c0c8ec25f8e0cbece736740568fd21e676f85fa8f03a889fb423a0，Git blob c4df0fdbe5de291eb0dcbd74aa2a47b6a5811cc7。原所有参数/command/输出身份仍完整保；两reader从不读科学数组或重算F/J。

继续按本条真实风险修完整normal/base接口和所有受影响的来源闭合，保原目标、全部变量、32normal、预算及完整history。新尝试必须用新的实际输出路径，保原失败报告和日志身份；不会删除guard、替换固定g、缩小参数或增加独立审查/fixture门。J1845只核同一构造约束是否同样受影响；未经证据不泛改。

## 16:24 UTC：完整实际源码给出的确切子条件

实际driver c64d2340fb51d67af98f56e3f6bec136048a43ceb9f7d9bc3ff12dc0b0488d25（95387B，blob726c884ccfa214d62c6846e651ded5beb811ca40）在该调用传：
```python
expected_base_source_sha256=SOURCE_PINS['meridian'][1],
expected_base_schema='complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1',
```
其中source pair本身就是实际3f4d5c0ec5b03eba9e93660e1341c32f1bd4872e0d1250d489894dd4ba6ed915。实际normal2db038574bb13e226b61826949cc66d917f0186fe5b9156a50eb7180da3d4bda（98437B，blobc65014dcebbcc5ccc8949aec47daf50dfbfd99ed）全体具有：
```python
SUPPORTED_BASE_SCHEMA = 'complete-fixed-fejer-angular-refined-supported-SO3-meridian-v1'
SUPPORTED_BASE_SOURCE_SHA256 = '3f4d5c0ec5b03eba9e93660e1341c32f1bd4872e0d1250d489894dd4ba6ed915'
```
base3f的实际SCHEMA与normal常量一致。故复合guard中失败的是driver传入的旧schema字面，而非这两个完整source SHA不相等。最小科学入口修复为把这一字面改成已严格pin的真实N4096 base schema，保normal/base/128个原source pair及所有数值方法不变；需同时闭合新driver的launcher/pure和全部新输出参数。修复未实施前不预报科学成功。

J1845该同一实际调用已由完整driver97ae6ab8、normal543ef572及base78ded268核对：三处schema都是complete-fixed-fejer-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1，三处完整base source SHA都是78ded2682f5a42bc44a1939e9d814eec17254d1385dfe08a545d6aee109892ef。它不存在这一次N旧字面失配，不据此变更J；此窄范围源码事实不称整族审查通过或科学结果。
