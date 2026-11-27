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


## 5. 后续真实返回：初始及当前有限几何筛

续记：2026-11-27 17:43 UTC。原§1–4的历史状态和全观测原字保留；本节更新后来的实际状态，不把先前尚未返回改写为早已成功。

root完整读回17:30:55索引14961B，SHA256 e3f9b58ea37158ad897a108ad897a75d850e847e97de5becff43b820ce3575a6，Git blob49d2da5ede4166cc7e33b7a19daf4a455690d010。normal记录的初始几何返回时刻17:26:17 UTC；数学observer的当前几何事件为2026-11-27T17:28:15.741299+00:00。两份几何都属于原完整点7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47。

| 实际字段 | 初始 | 当前 |
|---|---:|---:|
| finite geometry complete | true | true |
| positive physical g | 11.17545381570094 | 11.17545381570094 |
| Phi | 5551.477153263786 | 5551.477153263786 |
| 有限 max_relative_gram | 0.6480138218929927 | 0.6480138218929927 |

accepted_directions仍0、complete_report仍false、observer_failures仍0。几何返回后仍未取得可行场。这里complete与passed是原源码中不同的字段；正的g已经排除这两次有限筛的feasible状态，但没有排除后续求解或全局存在性。

### 5.1 g的完整定义、单位与范围

本解释直接读取实际同源完整geometry70709B，SHA256 2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471、Git blob2677d379e87b359088177b244428894311348996，路径scripts/resume_20261126/so3_fixed_fejer_stage_point_geometry.py的Budgets、_amplitude_values、_scalar_values、scan；并读取实际driver95632B、SHA256 8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d、Git blob3a537a58e82f152c78d0408c8b2c5f4403af1106，路径scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_observed_so3_qp.py的physical_violation、geometric_feasible及原求解分支。未添加一次场、导数、根或统计计算。

令E表示此次实际筛读的当前完整有限grid、存在的extra grid以及两类永久memory并集。当前入口q.N=513个quarter角，读取全部carrier行；原对称合同承担全orbit解释，complete本身不证明连续全角、全t或法向分支的协变。令
\[
 K=\max_E\max(|\kappa_1|,|\kappa_2|),\quad
 r=\max_E\|F\|,\quad d=\max(2,2|H|,2r),\quad
 r_0=1+\sum_j c_j.
\]
这里d是原代码的diameter_point_lower，不能冒充已证的整个闭面直径上界。B是实际binary64 marked budget 4.2减准确2/1000后向下round的body预算；L为实际binary64 .9；Hmin是实际binary64 1.01与L+准确1/1000向上round的较大者。R仍取同一冻结scalar的终端半径。原六类无量纲约束为
\[
\begin{aligned}
g_{\rm reach}&=.03\,dK-.992,\\
g_{\rm body}&=\max_E(4\|F\|^2/B^2-1),\\
g_+&=\max_E(1-\|F-(0,r_0,0)\|^2/L^2),\\
g_-&=\max_E(1-\|F-(0,-r_0,0)\|^2/L^2),\\
g_{\rm cap}&=4(R^2+H^2)/B^2-1,\\
g_{\rm height}&=(H_{\min}-H)/L.
\end{aligned}
\]
源码maximum_physical_g取这六项最大；physical_violation及observer positive_physical_g再取max(0,maximum_physical_g)。点/长度预算同长度量纲，K为长度的倒数，因此此次11.17545381570094是无量纲最大违约，不能解释为长度、百分比或所有约束的统一倍数。QP构造行时另有正的row_normalization_scale；本字段未除这个行尺度，也不是Gram残差。当前公开标量没有给出最大值属于哪一族，不能据此猜测最坏族或具体地址。

scan的complete=true表示声明的全部有限grid、显式地址及六world jets实际读取完整且有穷；passed要求maximum_physical_g<=0。driver的geometric_feasible还同时要求complete、passed和positive_physical_g==0。同一结果明确保留continuous_geometry_certified=False、continuous_metric_certified=False、rigorous_quadrature_or_root_errors_paid=False；不因有限筛完整而继承连续证书。

### 5.2 完整有界观测

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "initial-complete-geometry-returned",
      "at": "2026-11-27 17:26:17 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "stage": null,
      "cached_angle_roots": 1448,
      "closure_logical_requests": 199290,
      "closure_logical_returns": 199290,
      "closure_logical_failures": 0,
      "closure_original_returns": 38210,
      "closure_cache_hits": 161080,
      "closure_forced_stage_rereads": 34080,
      "closure_forced_endpoint_rereads": 1065,
      "closure_scopes_started": 1065,
      "closure_scopes_closed": 1065,
      "closure_immutable_point_key_checks": 164145,
      "closure_point_word_checks": 2130,
      "closure_original_closure_seconds": 377.9103827559983,
      "closure_binding_and_key_seconds": 50.20927952508384
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T17:28:15.741299+00:00",
      "math_event": "current-geometry-returned",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 11.17545381570094,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 11.17545381570094,
      "current_geometry_complete": true,
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
      "bytes": 3355,
      "sha256": "669bd4f72b6a16a452e7b76a22bdb6137e7a75edef478504a1aacef7524be704",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 5359,
      "sha256": "f1ed5ddbee4a5452d516e3fbb89cb528eb8ed8397ea2f5784ce120de91bf5922",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
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
  "observation_identity_sha256": "fc6a55cbf6ba8155ee0992a8297b13915486c8935f99a5e63eec2175e64cf528",
  "observed_utc": "2026-11-27T17:30:53Z"
}
```

## 6. 实际第一个trial已启动，尚无接受

root随后完整读回17:35:56索引14607B，SHA256 f0da634d57f3bfdb47d845e378bfe425d3ef88a8348ee48e29f6d7d3ccac94c8，Git blob25123756b11968b917d181af4eece02cd563e8fc；该版本在main929cab446c0ad73fc1a28660a4929169c48dca8d实读。原数学事件2026-11-27T17:35:48.630949+00:00为trial-start，其独立完整点为4086c1a7626d1914f7efe80530933dec4a12d96756519776e4ff581727ec787f；normal于17:35:49在这个点进入normal_chain_enter，缓存角数0。

当前点仍原7e06，Phi/Gram/g同上；trial_statistics及trial_geometry尚无返回，trial_accepted=null、accepted_directions=0。五个NoneType字段全部来自这两个尚空对象，不是科学抛错、原求解停止或observer失败。新点及trial-start不构成接受记录。根据原driver，当前正违约决定restoration分支；实际trial-start证明执行已走到试步，但这里没有完整QP报告、所选行或方向文件的读回证据，不预报其值。后续接受须原域条件、真正重读后的正违约严格下降及Armijo条件，并写完原accepted checkpoint；只有发生该真实事件才能改current身份。

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 17:35:49 UTC",
      "point": "4086c1a7626d1914f7efe80530933dec4a12d96756519776e4ff581727ec787f",
      "stage": null,
      "cached_angle_roots": 0,
      "closure_logical_requests": 209139,
      "closure_logical_returns": 209139,
      "closure_logical_failures": 0,
      "closure_original_returns": 48059,
      "closure_cache_hits": 161080,
      "closure_forced_stage_rereads": 34080,
      "closure_forced_endpoint_rereads": 1065,
      "closure_scopes_started": 1066,
      "closure_scopes_closed": 1065,
      "closure_immutable_point_key_checks": 164145,
      "closure_point_word_checks": 2131,
      "closure_original_closure_seconds": 464.8570401159999,
      "closure_binding_and_key_seconds": 50.20927952508384
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T17:35:48.630949+00:00",
      "math_event": "trial-start",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 11.17545381570094,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 11.17545381570094,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "4086c1a7626d1914f7efe80530933dec4a12d96756519776e4ff581727ec787f",
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json",
      "bytes": 3341,
      "sha256": "d91fddc3e42e244d66af615824b55099ef7898a304919ef80631d23a25e238d4",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 5547,
      "sha256": "8ac8cb9b59205ffa70e0f4eb88f2d6e7c408c87fd9cba69d057113f5edb3408e",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
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
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "30075822f03089614e0d6046f772c30d5ea14d5d4aacfc987e3104c4fdd34bfd",
  "observed_utc": "2026-11-27T17:35:54Z"
}
```

两份上述数学小文件均由原控制器完整有界双读，字节一致；完整identity列于各原对象内。原科学子进程仍未自然返回，已返回阶段仍仅两必要输入。原157/7argv、408/395正式读数、18+30live、全自由量/32stage及原预算继续；准确normal/geometry费用依旧消费真正完整同点报告与immutable snapshot。此次只记录已有结果，未替换目标、删减约束、制造连续证书或新增计算门。


## 7. 第一个trial的真实统计已返回，几何及接受仍未返回

续记：2026-11-27 17:50 UTC。固定main9b7c6f9f95a03ee9e9bdd25b1e4766776d2a2f7d的17:46:02完整索引14239B，SHA25695b6d904d546ade3d30d888bfc4a1b11043476b6ea66cef325b3058ebaf359ba，Git bloba0f2b6581acc567dcfd7374f2ffaf2512b166f93；root已按已知大小取完整正文。它新增的实际事件为2026-11-27T17:45:50.450062+00:00的trial-statistics-returned。

| 归属 | 完整 point | Phi | 有限 max_relative_gram |
|---|---|---:|---:|
| 已有current，未接受新方向 | 7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47 | 5551.477153263786 | 0.6480138218929927 |
| 本trial已返统计 | 4086c1a7626d1914f7efe80530933dec4a12d96756519776e4ff581727ec787f | 5551.4754665542505 | 0.6480137946863029 |

trial的两项值确实略小于原current，但restoration的接受仍需该trial的实际域与完整有限几何违约满足原严格下降/Armijo条件。当前只有统计返回：trial_geometry=null、trial_accepted=null，accepted_directions=0；原current几何g仍11.17545381570094，不能移给trial或用统计下降推断试步已接受。原完整报告仍false，科学子进程未自然返，observer失败仍0。三个剩余NoneType访问只属于尚空trial_geometry；不是科学异常。

数学小文件6457B/SHA25601a4a01164d8fe5004095d387b5628d09e76a512108977434a1bc95f5de8da4c已由控制器完整双读且一致。所有原source/model/target完整身份、当前点与trial点分别列于下方完整有界对象。

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 17:45:50 UTC",
      "point": "4086c1a7626d1914f7efe80530933dec4a12d96756519776e4ff581727ec787f",
      "stage": null,
      "cached_angle_roots": 513,
      "closure_logical_requests": 227989,
      "closure_logical_returns": 227989,
      "closure_logical_failures": 0,
      "closure_original_returns": 56574,
      "closure_cache_hits": 171415,
      "closure_forced_stage_rereads": 36160,
      "closure_forced_endpoint_rereads": 1130,
      "closure_scopes_started": 1131,
      "closure_scopes_closed": 1130,
      "closure_immutable_point_key_checks": 180850,
      "closure_point_word_checks": 2261,
      "closure_original_closure_seconds": 625.0081058919999,
      "closure_binding_and_key_seconds": 57.5306812550449
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T17:45:50.450062+00:00",
      "math_event": "trial-statistics-returned",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 11.17545381570094,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 11.17545381570094,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "4086c1a7626d1914f7efe80530933dec4a12d96756519776e4ff581727ec787f",
      "trial_Phi": 5551.4754665542505,
      "trial_Gram": 0.6480137946863029,
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json",
      "bytes": 3366,
      "sha256": "2e4484d951c13387f2feb390eca6a3b43c2b5a789338921d16027724ef041afd",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 6457,
      "sha256": "01a4a01164d8fe5004095d387b5628d09e76a512108977434a1bc95f5de8da4c",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
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
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "f58d726575870fc37b875d6a7aca6dab532172a3fd1b9aa01580715c246e3dc7",
  "observed_utc": "2026-11-27T17:46:00Z"
}
```

## 后续实读：新试步开始，上一试步决定没有被公开快照捕获

2026-11-27 19:05:19 UTC，root完整读取固定Gitblob6a08a6152ad30d5c0306a5063b0ed3d5d3aa0e52的18:56:32 UTC完整index，14608B/SHA256 4382e54faa3cfa14fd3b0138c2794d02ff863b53b7808081d0c7d964ae77c9fb；代理当次fixed main为c9b6c57b10282dd370e396d8c68e3057a1213d64。这里的事实严格来自这一整份快照，不用新点倒推未看到的中间数值。

数学事件变成2026-11-27T18:55:13.705307+00:00的trial-start，trial点25f40272f9a7516354d785f3e9a4629e61c432eb281a9eeb85c2eaadbbe679a7；当前点仍7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47，Phi=5551.477153263786、finite Gram=.6480138218929927、有限g=11.17545381570094，accepted_directions=0，complete_report=false，observer_failures=0。本次新trial统计/geometry/accepted尚未返回。

上一4086c1试步已看到其完整统计，但其geometry/decision没有被此次公开index保留下来。因而不编造它的g、实际line-search步长、拒绝原因、QP状态或已返全部历史；也不把新trial-start等同于已看到前一decision。原完整科学子进程尚未自然返回，完整报告及真实历史后续仍须读。这里five NoneType摘要错误只对应新trial尚无statistics/geometry对象；不能冒科学子进程失败。normal工作点与新trial一致，计数、原closure累积耗时和binding/key耗时只是原helper相应局部计量，不能当全部F/J/试步总耗时，angular order/batch在这个18字段display没有展示，均不推断。

两份实际进度原文件完整读两次一致：normal3373B/7f153f28d4952e19fc4758fbacc254ebc8b28384f4744b9feab27ef23868959a；math5547B/dc28189b0901a7bc4812171870f082b22bbd8f467d54e4c359de8223b61a0480。当前own model/driver/source/target、所有48选中标量及未知项保下面完整有界观察原对象：

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 18:56:30 UTC",
      "point": "25f40272f9a7516354d785f3e9a4629e61c432eb281a9eeb85c2eaadbbe679a7",
      "stage": null,
      "cached_angle_roots": 64,
      "closure_logical_requests": 537749,
      "closure_logical_returns": 537749,
      "closure_logical_failures": 0,
      "closure_original_returns": 216397,
      "closure_cache_hits": 321352,
      "closure_forced_stage_rereads": 68416,
      "closure_forced_endpoint_rereads": 2138,
      "closure_scopes_started": 2139,
      "closure_scopes_closed": 2138,
      "closure_immutable_point_key_checks": 457346,
      "closure_point_word_checks": 4277,
      "closure_original_closure_seconds": 1801.6770967322,
      "closure_binding_and_key_seconds": 172.39890153116005
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T18:55:13.705307+00:00",
      "math_event": "trial-start",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 11.17545381570094,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 11.17545381570094,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "25f40272f9a7516354d785f3e9a4629e61c432eb281a9eeb85c2eaadbbe679a7",
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json",
      "bytes": 3373,
      "sha256": "7f153f28d4952e19fc4758fbacc254ebc8b28384f4744b9feab27ef23868959a",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 5547,
      "sha256": "dc28189b0901a7bc4812171870f082b22bbd8f467d54e4c359de8223b61a0480",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
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
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "a81124551a5038c10f890860dd946d1164910a17677271a3cf4b7e295b867452",
  "observed_utc": "2026-11-27T18:56:30Z"
}
```

## 第二试步真实统计返回（2026-11-27 19:13:20 UTC实读）

root完整读取19:06:37 UTC index，14240B/SHA256 b47cdf850649de905b6582e96d3487f66754d8f612ed827d2e8819785a307ea6/Gitblob95038acaa3768b9751404a9e193a807d5c7a04d8；代理当次fixed main5ea418544b4a24dda083ca70d6456a015140d16f。数学事件为19:05:05.854797 UTC的trial-statistics-returned，仍是25f40272f9a7516354d785f3e9a4629e61c432eb281a9eeb85c2eaadbbe679a7，真实Phi=5551.476309922079、finite Gram max=.6480138082898852。当前7e06点、初始/当前Phi、Gram与g全部仍是原字；accepted_directions=0，report未complete，helperfail=0。第二试步geometry和decision未返，因此同样不能从统计量的微降推接受或几何改善。

原完整normal3379B/ca21e8fff61a3d7557c1e8fd34be4aba5f786c6328f1bec2490e38db00f6e9f9，math6458B/70589ffc291f60c4149184f6c546f3f2eab38b798ce6c264e57c9998ae905066，均两次完整有界读取一致；三个NoneType selector只对应尚null的trial_geometry。工作角根cached513与局部累计计数不补未显示order/batch，也不作完整试步耗时。全观察对象如下，保完整source/model/own-point与未知边界：

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 19:06:29 UTC",
      "point": "25f40272f9a7516354d785f3e9a4629e61c432eb281a9eeb85c2eaadbbe679a7",
      "stage": null,
      "cached_angle_roots": 513,
      "closure_logical_requests": 554965,
      "closure_logical_returns": 554965,
      "closure_logical_failures": 0,
      "closure_original_returns": 224550,
      "closure_cache_hits": 330415,
      "closure_forced_stage_rereads": 70464,
      "closure_forced_endpoint_rereads": 2202,
      "closure_scopes_started": 2203,
      "closure_scopes_closed": 2202,
      "closure_immutable_point_key_checks": 472450,
      "closure_point_word_checks": 4405,
      "closure_original_closure_seconds": 1962.4239058361654,
      "closure_binding_and_key_seconds": 179.132834062185
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T19:05:05.854797+00:00",
      "math_event": "trial-statistics-returned",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 11.17545381570094,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 11.17545381570094,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "25f40272f9a7516354d785f3e9a4629e61c432eb281a9eeb85c2eaadbbe679a7",
      "trial_Phi": 5551.476309922079,
      "trial_Gram": 0.6480138082898852,
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json",
      "bytes": 3379,
      "sha256": "ca21e8fff61a3d7557c1e8fd34be4aba5f786c6328f1bec2490e38db00f6e9f9",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 6458,
      "sha256": "70589ffc291f60c4149184f6c546f3f2eab38b798ce6c264e57c9998ae905066",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
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
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "eaf6712026c1f99331060cda98a651fe0f770a858fdc5cee54a4645714673b56",
  "observed_utc": "2026-11-27T19:06:35Z"
}
```

## 第三试步真实开始；第二试步完整几何决定仍未捕获（2026-11-27 20:29 UTC整理）

root完整读取20:17:07 UTC index，14612B/SHA256 f0280167841f08f143341a03cd8625abb36c5d71b54c7f2f759bb3efea583a3f/Git blob 737e6773ad0345af1ab49357eb181ac101ca0a14。其中20:13:08.480555 UTC为新的 trial-start，真实point为`880d748acf6fae711c248b21dcb190c6aa7fb4232a6b930a8dfb9c8eb8cf823e`。当前接受态仍为原7e06点，accepted_directions=0，当前Phi、finite Gram与完整有限几何g仍分别为5551.477153263786、.6480138218929927与11.17545381570094；complete_report=false。第三试步的统计、几何与决定在这份记录里均尚未返回。

第二试步25f402的统计返回已在上一节完整记录；其后几何与decision未被原五分钟观察器保留下来。不能从出现下一试步反填它的几何值、实际拒绝分项、alpha或决定时刻，也不能把此次进度当执行断点。首试步同样的未捕获边界继续保留。新18观察器的上一完成trial保留是独立新源码，不会追溯补齐16旧记录。

本次两份小进度文件均经controller两次完整有界读取且字节身份一致；数学文件5549B/384e57f5a694d2fe19b89ac90320c585b4a02f213c30f7ee55e8484810e052b8，所有null与selector TypeError完整保如下。normal记录里的208个角根与计数不携带当前order/angle_batch，不能借别组或先前记录补它们，也不证明当前试步被接受。

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 20:17:02 UTC",
      "point": "880d748acf6fae711c248b21dcb190c6aa7fb4232a6b930a8dfb9c8eb8cf823e",
      "stage": null,
      "cached_angle_roots": 208,
      "closure_logical_requests": 869259,
      "closure_logical_returns": 869259,
      "closure_logical_failures": 0,
      "closure_original_returns": 386045,
      "closure_cache_hits": 483214,
      "closure_forced_stage_rereads": 103072,
      "closure_forced_endpoint_rereads": 3221,
      "closure_scopes_started": 3222,
      "closure_scopes_closed": 3221,
      "closure_immutable_point_key_checks": 753117,
      "closure_point_word_checks": 6443,
      "closure_original_closure_seconds": 3124.379667731944,
      "closure_binding_and_key_seconds": 286.43740762292975
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T20:13:08.480555+00:00",
      "math_event": "trial-start",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 11.17545381570094,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 11.17545381570094,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "880d748acf6fae711c248b21dcb190c6aa7fb4232a6b930a8dfb9c8eb8cf823e",
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json",
      "bytes": 3388,
      "sha256": "0c05c9129594b75abbac086ab921a290579bb07813d39ab7fc246ff5d201842e",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 5549,
      "sha256": "384e57f5a694d2fe19b89ac90320c585b4a02f213c30f7ee55e8484810e052b8",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
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
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "482e7462aef17a0fab8684e33f64b6b2eb4357a2ab1b85d5283db2aff86600b3",
  "observed_utc": "2026-11-27T20:17:05Z"
}
```

## 第三试步统计实际返回（2026-11-27 20:31 UTC实读）

新完整index于20:27:13 UTC写出，14243B/SHA256 f27f6e7c3938d1e83261c7b4b4a7b2abe1eb05579d41503e375a23fa6a7fc621/Git blob b6a51c156bfe9724a1c7e6ab34e8e3288e4c240b。其数学事件20:22:50.125478 UTC为trial-statistics-returned，第三880d同点Phi=5551.4767315961935、finite Gram最大=0.6480138150914985。该trial的完整几何和接受决定仍未返回；current7e06、accepted0与初始/当前Phi、Gram、g原字不变。统计改善不足以决定接受。

数学文件6461B/33aa2795944983c15cd052985cd1313e9c5716ded70513afa8a09453f8b47a61，仍由controller两次完整有界读取一致，未补原live不含的order/angle_batch或第二trial丢失几何。完整观察对象如下。

```json
{
  "step_id": "complete-fixed-fejer-stage-point-observed-independent-20261127",
  "scientific_source_commit": "a8b0749a3907ef7241745d07c5c24a7670aa842d",
  "scientific_source_sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
  "pid": 3868,
  "observations": {
    "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 20:27:03 UTC",
      "point": "880d748acf6fae711c248b21dcb190c6aa7fb4232a6b930a8dfb9c8eb8cf823e",
      "stage": null,
      "cached_angle_roots": 513,
      "closure_logical_requests": 882823,
      "closure_logical_returns": 882823,
      "closure_logical_failures": 0,
      "closure_original_returns": 393408,
      "closure_cache_hits": 489415,
      "closure_forced_stage_rereads": 105056,
      "closure_forced_endpoint_rereads": 3283,
      "closure_scopes_started": 3284,
      "closure_scopes_closed": 3283,
      "closure_immutable_point_key_checks": 764635,
      "closure_point_word_checks": 6567,
      "closure_original_closure_seconds": 3291.295748833876,
      "closure_binding_and_key_seconds": 291.42915824906333
    },
    "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T20:22:50.125478+00:00",
      "math_event": "trial-statistics-returned",
      "math_driver": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "math_model": "8cc03937539fc4b8bda075ed27dca794517b5b4995b0256b692ff90e4b9efac6",
      "math_source": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 5551.477153263786,
      "initial_Gram": 0.6480138218929927,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 11.17545381570094,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 5551.477153263786,
      "current_Gram": 0.6480138218929927,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 11.17545381570094,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "880d748acf6fae711c248b21dcb190c6aa7fb4232a6b930a8dfb9c8eb8cf823e",
      "trial_Phi": 5551.4767315961935,
      "trial_Gram": 0.6480138150914985,
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-normal-evaluation-progress.json",
      "bytes": 3393,
      "sha256": "7c2357c5b11f67dbc09ac48c8e34990805030983ba7e078e63a3a7bb91af2746",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-stage-point-observed-independent/actual-mathematical-progress.json",
      "bytes": 6461,
      "sha256": "33aa2795944983c15cd052985cd1313e9c5716ded70513afa8a09453f8b47a61",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
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
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "49d8a4e58344e00440449dc13195276ab99e7dd9fe2e6f47068b3c8e0fa00024",
  "observed_utc": "2026-11-27T20:27:11Z"
}
```
