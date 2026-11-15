# Request97：从 actual96 真 final 继续同一 ce93 搜索

日期：2026-11-15（UTC）。作者：amplitude。状态：独立 `/tmp` 工作流、请求与静态证据冻结；未修改仓库、未 Git、未下载、未派发、未本地执行科学计算。未来科学调用仍只在本公开仓库 Actions 中运行。

本轮直接复用 request96 的完整接线及 `ce93a364…` 科学入口。新初猜只取实际96完整 status 的 `final.parameters`。全部72个源码 pin、13项直接消费闭包、四个原数学输入、η、方向公式、恢复规则、预算与最终诊断保持。父 J、merit、状态和 FD 不作为本轮的新计算值。

## 1. 真实父原件及续接依据

已读取 root 唯一下载目录中的实际96完整 status 和原 input/source identity；本次只解析 JSON、核字节和 SHA，没有重新计算任何科学读数。

| 字段 | 实际值 |
|---|---|
| run | `43675493266` |
| source commit | `c43f20db7dbcaa2dcf48aca8a79b5df921d9ed4c` |
| job | `132694604911` |
| artifact | `14145702242` |
| 原 ZIP bytes | `502765` |
| 原 ZIP SHA256 | `6ead780b66730f2306dfa4579849c0546900f80d3550ae7c270912c925f601bf` |
| 原 status bytes | `233129` |
| 原 status SHA256 | `3343c5799dcb50a3ff58c52c0dfebaab441bc7a0bfe644a88e9a1a93fae2eacb` |

原文件为 `small-core-inexact-p3-restoration/inexact-p3-restoration-status.json`，schema 为 `R278-original-three-equation-inexact-p3-restoration-LM-v1`，producer 为 ce93。八个外方向均在第一个 α=1 trial 通过，合计八个外 trial、八次内恢复调用；原停止文字是 `explicit outer direction budget completed`，没有 exception 字段。

原初始 merit 为 `146733.11420724491`，原最后 merit 为 `16791.962002764827`。原最后三个单位缺陷是 `[-183.21971055442938, 3.802850231178231, -2.0184856696129315e-08]`。这里直接复制已保存的数值，没有本地重求 merit、缺陷、下降量或比率。

原 `diagnostic_completed=True`，而 `success=False`、`original_unit_stopping_tolerance_met=False`、`low_mode_candidate_has_small_full_recorded_right_residual=False`、`native_nonlinear_solver_called=False`、`full_nonlinear_nonzero_lambda_solution_computed=False` 均保留。八次实际接受支持从最后候选继续同一算法；它不构成共振根、非零 BVP/native 解、精确隐函数或固定 g 分支的存在声明。

唯一新初猜是父 `final.parameters`，也与其 `last_accepted_parameters` 相同：

```json
[0.5059246655778534, -0.3454563899724949, 0.5924659176169055]
```

三项 binary64 小端字节分别是 `17b19cec8830e03f`、`d311481ef51bd6bf`、`7d1885157bf5e23f`。新 request 两处参数字面量及 workflow 固定 expected 字典均与父数组相同；没有选择最后未接受的内 probe。

## 2. 原 own-schema 与 fresh model 接口保持

科学源仍为：

```text
geometry_20261115_small_core_inexact_p3_restoration.py
45133 bytes
ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e
```

已读原 `checked_parent` 和 `main`，没有改动。原 own-schema 分支要求同一 producer 原 SHA、精确 consumed-source 字典及 `last_accepted_point_semantics == "original-three-merit-accepted-candidate-or-fresh-parent"`。实际96满足这份既有来源合同。完整13项消费闭包是原12项 frozen dependencies 加 ce93 自身，与实际96 status、72 pins 中对应项及当前来源文件字节一致。

原 main 从父 `final.parameters` 构造参数数组，随后在 `fresh-parent-state` 上调用原 `model.evaluate(parameters)`，再在 `fresh-parent-original-description-FD` 上调用原 `model.description(state)`，取得本轮实际初始值及完整参数 J。新 request 的参数字段负责绑定和审阅；科学 argv 没有另传 `--parameters` 来覆盖父值。

父原 status 在接线阶段通过 `write_bytes(prior_raw)` 复制到 `prior-candidate/actual96-inexact-p3-restoration-status.json`，科学源也保留其原字节副本。父 J、FD、merit、Arb、circle 只保留为历史结果。本轮 fresh merit 必须采用本轮实测值，不强制其逐位等于父末 merit，也不通过复制父字段制造相等。

旧3b48/ec9/1691仍是完整来源链中的历史代码，角色和字典完全保留；ce93 main 不重新执行旧方向引擎或旧92搜索。既有独立算法/schema 标识继续说明 ce93 相对3b9原模型的关系，不表示97再次换算法。

## 3. 单一请求与完整最小差异

基线是 `/tmp/visible-larger-request96/` 的两个冻结文件：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `visible-larger-public-small-core-resonance.yml` | 20,497 | `18aa067d86b3dce55e6964bff1aefef94d02a36330ab508c446846792c79e968` |
| `public-small-core-resonance-request.json` | 20,124 | `aceca0a8613ae04ad400024c73fa1a4910da66c5f495818ec73f1fc0881fd795` |

由 root 唯一发布到既有 `.github/workflows/visible-larger-public-small-core-resonance.yml` 和 topic computations 请求路径。push trigger 仍只监听：

```text
topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json
```

job/concurrency 仍为 `smallcoreresonance` / `visible-larger-public-smallcoreresonance`，`cancel-in-progress=false`。没有另开科学 workflow/lane，也没有预填未来97 run/job/artifact。

完整 workflow diff 只改变 job/绑定步骤的父名称、父 sparse path、request97编号、真实96参数/size/SHA、原父副本 basename 和 request identity 输出名。按步骤对象比较，仅 checkout 步骤0和来源绑定步骤4有变化；另有 job 的显示名称更新。`PYSOURCE`、`PYDIAGNOSTIC`、`PYREAD` 三段正文逐字同96，原 argv 构造、原78恢复、always读回、artifact和publisher接线不变。

完整 request diff 只更新请求编号/时间、真实96父 tuple/status/保存读数、参数初猜及对应来源说明。source-chain、全部72 pin字典、四数学输入描述器、runtime、direction-model、scope、proof引用、输出契约和预算逐值同96。两份完整 diff 及可逆源文本替换回执随稿。

新父公开路径为：

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43675493266-1-smallcoreresonance/small-core-inexact-p3-restoration/inexact-p3-restoration-status.json
```

该233129字节父文件直接使用原 JSON，读取/复制时不重序列化。独立审阅副本 `actual96-original/inexact-p3-restoration-status.json` 与 root 下载原件逐字相同。

## 4. 原算法、预算与最终检查

唯一科学调用保持：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261115_small_core_inexact_p3_restoration.py" \
  --accepted <原 accepted96 文件> \
  --prepared <原699/prepared112 文件> \
  --tail-anchor <原真实T112零锚完整J> \
  --tail-config <原T112配置> \
  --parent-status <上述 actual96 完整原 status> \
  --parent-status-sha256 3343c5799dcb50a3ff58c52c0dfebaab441bc7a0bfe644a88e9a1a93fae2eacb \
  --damping 0.1 --candidate-steps 8 --backtracks 20 \
  --inner-newton-steps 12 --inner-backtracks 20 \
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14 \
  --out "$VISIBLE_OUT/small-core-inexact-p3-restoration"
```

保留原三方程、完整3×3参数J、实际非零第三残差的 normal-plus-Schur方向、η=0.1列缩放阻尼模型、实际完整三项 merit/gdot/.2 Armijo、内层 strict abs(d3) 减少与原域判定。内恢复中间点仍是未接受试探；外候选按原完整三项 merit 接受。内层1e−8目标不另加成外层资格门，第三残差不清零。

原最终单位残差/full112标志、description和FD、160-bit/depth14标量 Arb 与完整 circle/Fourier检查继续原函数。保留699站点、112场模/112尾模、2048物理角、4096材料与边界角、单 RHS worker。没有新增根阈值、native/BVP接受门或高模成功声明。

运行环境仍为 Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、三组 BLAS线程1、原全部 Action pins；job60分钟、科学步骤45分钟不变。这是一次显式8方向预算的续接，不自动增大预算或重复科学重试。

## 5. 原件、输入验证范围与输出

原四输入的描述器和SHA不变。当前 sparse checkout 未包含这些历史payload，本次没有为其下载或声称做了新的本地payload审计。四描述器与96请求逐值一致，且与已下载实际96的 `request96-input-and-source-identity.json` 中原 verified-input 记录相同；其原件36706字节/SHA `ccb5dc4e9186ccd89a2b509dee5d129a6d0ae230330612f285330d1b1f26d621` 已核。未来 Actions 仍按原 checkout 和原完整size/SHA检查读取四输入。

输出路径/schema保持：

```text
small-core-inexact-p3-restoration/inexact-p3-restoration-status.json
R278-original-three-equation-inexact-p3-restoration-LM-v1
```

所有 inner报告、完整原 status、streamed model evaluation trace、FD/Arb/circle、异常/partial输出仍由原 always步骤上传。原完整派生读回过90KB时保留在 `large-arrays/complete-diagnostic-readback.json`，不截断原 status 或科学轨迹。

publisher仍为 `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`，原 lane、普通 pull/rebase、README读取和artifact保全保持。该草稿不执行发布、不代填未来成功。

## 6. 静态证据和冻结件

本地已完成 source/原JSON/bytes 范围的检查：

- 72个实际来源文件SHA全匹配原 pins；Python只做AST/compile，未导入数学库。
- ce93原size/SHA未变；真实96 own-schema、producer、13消费闭包、四原输入身份、last-accepted语义和三个参数bits一致。
- 父文件233129字节完整复制、SHA相同；八方向/八首档alpha1/预算停止从原JSON读取。
- 7段shell `bash -n`、4段inline Python AST/compile通过；三段科学/恢复/读回正文逐字同96。
- 请求中全部非父科学配置保持；workflow全部替换可精确逆向恢复 frozen96原字节。
- 最终静态报告的旧父标签已纠正为 `original96_verified_input_receipt_equal`，仅本地回执名称修正，workflow/request和科学源未变。

冻结件均位于 `/tmp/visible-larger-request97/`：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `visible-larger-public-small-core-resonance.yml` | 20,497 | `705d94c43f39b3c00acb3ddc037fdbab8c347780ba24b2a7b128bc8b9a940198` |
| `public-small-core-resonance-request.json` | 20,103 | `6e4c05517e82b4fb0ed2337faf6c03fc6d5382b1027d3e9d91f481342ff67a89` |
| `request97-static-check.json` | 31,670 | `80f01b4aba142652a05d9cb115f74e46adbd598d11d2632ae9e313b464fe4ff3` |

完整 `workflow-from-actual96.diff`、`request-from-actual96.diff`、生成回执、静态checker、父literal读回和 `frozen-files.json` 同目录。本文与各附件的最终字节/SHA由冻结清单记录。以上工作不运行科学、不改旧源码，也不设第二次科学审查或新的接受条件。
