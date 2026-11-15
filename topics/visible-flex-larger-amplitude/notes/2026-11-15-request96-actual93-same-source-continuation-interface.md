# Request96：从 actual93 真 final 继续同一 ce93 搜索

日期：2026-11-15（UTC）。作者：geometry。状态：工作流、请求及静态证据已冻结，未 Git、未 dispatch、未下载新包、未本地执行数学。全部未来科学仍仅在公开仓库 Actions 运行。

本轮沿用 actual93 的同一完整科学源，不创建第二个求解入口，不改变 η、方向公式、恢复规则、外/内预算或最终诊断。唯一新初猜来自实际93完整 status 的 `final.parameters`。父 J、merit、状态、FD、Arb 或 circle 数据只作为原结果保全，不作为新的模型计算值。

## 1. 真实父与停止范围

已亲读 root 唯一取回的 actual93 原件：

| 字段 | 实际值 |
|---|---|
| run | `43674264245` |
| source commit | `8adc3251a8fe2ee7bcbc5d6d8381631b1558141e` |
| job | `132690828561` |
| artifact | `14145249554` |
| ZIP bytes | `620340` |
| ZIP SHA256 | `16bb4f5542472de72a5d03ef72fc5da113c925de844ff4fbd8a7856f17662d37` |
| 原 status bytes | `372627` |
| 原 status SHA256 | `0913ea5d90ddb23bd408b33175887b5b24665fe0db8324d873bbe0b08c12a647` |

原 status 为 `small-core-inexact-p3-restoration/inexact-p3-restoration-status.json`；原 schema 为 `R278-original-three-equation-inexact-p3-restoration-LM-v1`，producer 是 `ce93a364…`。

本地只读取已保存原值：八个外方向均接受，合计十五个外 trial/内 restoration 调用，实际接受 α 依次为 `1, 1, 1/2, 1, 1/16, 1, 1, 1/4`；没有 exception 字段，停止原文为 `explicit outer direction budget completed`。原最后 merit 为 `146733.11420722902`，原前三单位缺陷为 `[-206.33215777138622, 500.8924725765619, -3.79434721027843e-08]`。这些数字均直接复制，未重新计算 merit、缺陷或比值。

原 `success=False`、完整单位 stopping flag=False、full112 小残差 flag=False、native 调用=False 均保留。已完成一次候选搜索不等于得到 BVP/native 非零解。此次续8轮不预断言未来收敛。

唯一初猜为：

```json
[0.5078436152033409, -0.3849212262335502, 0.5911288427829965]
```

它与父 `last_accepted_parameters` 相同；新 request 的两个参数位置及工作流固定 `expected` 都与该原数组逐字面值及 binary64 bits 核对。没有取最后未接受内 probe。

## 2. 同源 own-schema 接口已存在

科学入口仍为：

```text
geometry_20261115_small_core_inexact_p3_restoration.py
45133 bytes
ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e
```

已亲读其 `checked_parent` 和 `main`。原函数已有 own-schema 分支：要求本 producer SHA、精确完整 consumed-source 字典，以及 `last_accepted_point_semantics == "original-three-merit-accepted-candidate-or-fresh-parent"`。实际93三者相符，无需改科学源码。其完整13项 source closure 等于原十二个 frozen dependencies 加本 ce93 入口，已与 actual93 原 status 和本 checkout 的实际来源文件核对。

`main` 仍从父 `final.parameters` 构造初猜，随后依次调用原 `model.evaluate(parameters)` 和原 `model.description(state)`，才取得当前初始值和完整 J。新 request 标记 `scientific_source_unchanged=True`；旧 source-chain 名称、历史3b48/ec9/1691来源角色、独立 R278 算法/schema 声明仍保原样。它们说明相对原3b9模型的既有算法来源，不表示96又换了算法或执行了旧92搜索。

原父 status 在 workflow 绑定阶段用 `write_bytes(prior_raw)` 复制到 `prior-candidate/actual93-inexact-p3-restoration-status.json`；科学源仍再以 `write_bytes(parent_raw)` 保全其输入副本。没有 JSON 反序列化后重新写回父文件。本地另有完全相同的审阅副本 `actual93-original/inexact-p3-restoration-status.json`，其 SHA 与原件相同。

## 3. 唯一公开接线及最小差异

基线是 `/tmp/visible-larger-request93/` 已冻结的：

| 基线文件 | bytes | SHA256 |
|---|---:|---|
| `visible-larger-public-small-core-resonance.yml` | 20,198 | `6872ff02d77a40478057989f72549ce7fff4ec4ae14ed9f4fc3f9a3309a350f4` |
| `public-small-core-resonance-request.json` | 19,846 | `9a5f4f3fb275bc4ce9440a0d48fd962e75a275ed3e3508c5805d97b64e57b6d4` |

新草稿仍覆盖同一 workflow 和同一个 computations request 文件，由 root 唯一发布。push trigger 保持：

```text
topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json
```

job/concurrency 仍 `smallcoreresonance` / `visible-larger-public-smallcoreresonance`，`cancel-in-progress=false`。不是额外 workflow 或另一并发科学 lane。

工作流只改 job/绑定步骤的来源文字、父 sparse path、request96 身份、原三参数字面值、父 SHA/size/schema/producer、原父副本名和 request identity 输出名；增加的 final-point semantics 比较正是 ce93 已有 own-schema 约束的来源复核。科学 command 及其 argv 构造、原78恢复正文、完整 always-readback 正文逐字不变。

新父公共路径为：

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43674264245-1-smallcoreresonance/small-core-inexact-p3-restoration/inexact-p3-restoration-status.json
```

完整72 source pin 字典、source-chain 字典、四数学输入描述器、runtime、direction-model 字典、scope 和原 proof 引用均与93相同。请求仅更新真实父来源/原读数、参数初猜、request编号/时间及同源说明。

## 4. 预算、原方程和完整验收保持

唯一科学调用继续原 CLI：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261115_small_core_inexact_p3_restoration.py" \
  --accepted <原 accepted96> \
  --prepared <原699/prepared112> \
  --tail-anchor <原真实T112零斜率J锚> \
  --tail-config <原T112配置> \
  --parent-status <上述 actual93 完整原 status> \
  --parent-status-sha256 0913ea5d90ddb23bd408b33175887b5b24665fe0db8324d873bbe0b08c12a647 \
  --damping 0.1 --candidate-steps 8 --backtracks 20 \
  --inner-newton-steps 12 --inner-backtracks 20 \
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14 \
  --out "$VISIBLE_OUT/small-core-inexact-p3-restoration"
```

父参数由原 source 读取；不另外用 `--parameters` 覆盖。完整原三方程/3×3 J、包含实际非零第三残差的 normal-plus-Schur 方向、η0.1 列缩放 LS、原实际三项 merit/gdot/.2 Armijo、内层 strict abs(d3) 减小规则和最后有限恢复点责任均不变。内层1e−8仍是原目标，并不被另加成外层 eligibility 门；实际第三残差不清零。

原最终 unit/full112 标志、description/FD、160-bit/depth14 scalar Arb 与完整 circle/Fourier 检查均沿 ce93 原函数执行。保全部112尾模、699站点、2048物理角/4096材料与边界角、单 RHS worker。参数搜索仍不宣称沿一个固定 g，也不宣称精确隐函数或高模横截性。

runtime 保持 Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、原三组 BLAS 线程1与 action pins。job60分钟、科学 step45分钟保持；没有第二次自动科学重试。

## 5. 输出、读回和父件真实字节

新 run 的输出仍为：

```text
small-core-inexact-p3-restoration/inexact-p3-restoration-status.json
R278-original-three-equation-inexact-p3-restoration-LM-v1
```

完整 status、所有 inner reports、原 streamed evaluation trace、FD/Arb/circle、失败和 partial 原件都按93方式 always 上传。读回正文完全不变；超过90,000字节的完整派生视图仍保 `large-arrays/complete-diagnostic-readback.json`，不截断科学原 status 或 inner 原件。

publisher 保持 `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`，lane仍 smallcoreresonance，普通 pull/rebase、README 检查和 artifact retention 不变。新 run/job/artifact tuple 尚未产生，没有预填。

本地静态核并未取回四个历史数学 input 的大 payload：它们在当前 sparse tree 中未检出。四描述器与93请求完全相同，并与已下载 actual93 原 `request93-input-and-source-identity.json` 内四个真实 verified-input 收据逐字一致；未来同一工作流 checkout 后仍执行原完整 size/SHA 检查。这不被写成新的本地 payload hash 证明，也没有为此另行下载或阻塞调度。

## 6. 已付静态证据和交付

已完成以下源文本/原字节核对：

- 本地72个实际来源文件 SHA 全符合原72 pins；Python 仅 AST/compile，没有导入。
- ce93 source 的原 SHA/size 完全不变；真实父 own-schema、producer、完整13-source closure、last-accepted语义、原四输入 SHA 及 final参数 bits 均吻合。
- 原父 status 完整复制 SHA 相同；原 parameters 不是本地重新求解所得。
- 7 段 shell `bash -n`、4 段 inline Python AST/compile 全过。`PYSOURCE`、`PYDIAGNOSTIC`、`PYREAD` 三段正文逐字同93；只有 `PYPINS` 更新父/请求身份。
- 所有工作流改动可精确反向还原为 frozen93 原 bytes；完整 diff 随稿。

新冻结件均在 `/tmp/visible-larger-request96/`：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `visible-larger-public-small-core-resonance.yml` | 20,497 | `18aa067d86b3dce55e6964bff1aefef94d02a36330ab508c446846792c79e968` |
| `public-small-core-resonance-request.json` | 20,124 | `aceca0a8613ae04ad400024c73fa1a4910da66c5f495818ec73f1fc0881fd795` |
| `request96-static-check.json` | 31,670 | `1ab3c1e6db2e8780587e4a7babf0136de63649c30a4b199f03ab085c482b2661` |

`workflow-from-actual93.diff`、`request-from-actual93.diff`、源生成回执、静态 checker 与 `frozen-files.json` 同目录。除独立 `/tmp` 草稿外，没有仓库/Git修改、下载、科学执行或派发；本次工作没有引入任何新的科学接受标准。
