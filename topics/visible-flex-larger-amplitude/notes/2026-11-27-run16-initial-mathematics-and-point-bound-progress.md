# 第16次：真实初始数学量与各自点绑定

记录：2026-11-27 17:17:11 UTC。Astra-larger-e4e2a2bf-20261126。**科学子进程尚未自然返回；这是已有操作返回的标量，不是接受场或完成证书。**

## 1. 真实数值及其来源

run46037017666/1、job140634874993；science sourcecommit a8b0749a3907ef7241745d07c5c24a7670aa842d，完整launcher ed81031f、driver8dc9d876、observer bff1e03a均为已刊全来源。17:10:48公开索引15926B，whole SHA256 7c632d7a964268c11a4d4d26b07fa4e25868bc5ba14410b1aab6e9164db645c2、Git blob833ec440f823b923724aa499ea60ecb5180c36dd，root已size-first完整读取。

原数学事件实际发生在 **2026-11-27T17:07:51.249471+00:00**，是 **initial-statistics-returned**：

| 已实际返回字段 | 原数值或身份 |
|---|---|
| 完整 caller point | 7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47 |
| 初始 Phi | 5551.477153263786 |
| 原全部有限metric观测上的 max_relative_gram | 0.6480138218929927 |
| 当前统计点 | 7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47 |
| 当前统计状态 | initial statistics returned; no accepted direction |
| 原实际接受方向数 | 0 |
| 完整报告完成 | false |
| 观测helper失败数 | 0 |
| 完整当前normal model | 8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6 |
| 固定数学目标 | 957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9 |

这里normal model8cc039…和固定reference model ea64e2…是不同对象，不能互换。实际初始与当前统计恰是同一完整点7e06；这个等号不赋予accepted或final身份，也不是从root缓存猜测归属。原Phi与Gram数值显示当前数值初值尚远离所需metric精度，不能把输入构造成功当成满足目标。

## 2. 几何与trial当时尚未返回

这份索引采样的geometry与trial对象尚为空。因此控制器访问十三个相应dot-path时记录NoneType不可下标；完整原错误对象保在下方。这些是尚无对象的进度字段，不是原科学函数抛错，也不是observer失败；不为此修改科学源、参数或预算。

数学小文件3328B，whole SHA256578e096eb6e1402b50243a10be0cdff372e315c4e997ea5d0b73fd8edf6b4308，两个完整有界读取逐字一致。原normal小文件另有自己3295B/ae10b18c…身份与17:10:46时刻；不得把该根事件时刻当统计返回时刻。

有限metric观测不等于全域连续Gram算子范数；尚未返回的几何g不填0。下次若出现新trial，其Phi/Gram也须保自己的完整point，只有原接受判据成立并checkpoint完成之后才能记为accepted current。真正完整子进程返回集当前仍只有两必要输入。

## 3. 完整原有界观测

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 17:10:46 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "stage": null,
      "cached_angle_roots": 530,
      "closure_logical_requests": 20280,
      "closure_logical_returns": 20280,
      "closure_logical_failures": 0,
      "closure_original_returns": 5162,
      "closure_cache_hits": 15118,
      "closure_forced_stage_rereads": 4704,
      "closure_forced_endpoint_rereads": 147,
      "closure_scopes_started": 148,
      "closure_scopes_closed": 147,
      "closure_immutable_point_key_checks": 15429,
      "closure_point_word_checks": 295,
      "closure_original_closure_seconds": 121.99587437999719,
      "closure_binding_and_key_seconds": 5.2932093759965255
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T17:07:51.249471+00:00",
      "math_event": "initial-statistics-returned",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_state": "initial statistics returned; no accepted direction",
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json",
      "bytes": 3295,
      "sha256": "ae10b18c78431b865445ab71440e53aebad354f193bb69bd47bf979e9e26f242",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 3328,
      "sha256": "578e096eb6e1402b50243a10be0cdff372e315c4e997ea5d0b73fd8edf6b4308",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "initial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "initial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "initial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "current_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "current_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "current_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "latest_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "field": "latest_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "f916a61c2681966cdd9abdb4f7a8ac2c2cf651a8a74840320cc0263eaa4f69c4",
  "observed_utc": "2026-11-27T17:10:46Z"
}
```

## 4. 继续执行

原科学对92522B、全157/7argv、408/395正式读数与18+30live保持；完整目标、全部1333370自由量、32stage和原预算不变。原source/参数及两真实输入见[启动记录](2026-11-27-run16-complete-own-point-mathematical-research-launch.md)。[完整准确费](2026-11-27-stage-observed-fixed-fejer-complete-accurate-fees.md)全38/36与8/48已刊，等真实科学返回后按容量接完整步骤，不以mutable观测当immutable包，不削项、不设新门。
