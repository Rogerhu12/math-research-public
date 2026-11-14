# 第 61 轮完整原件的 Actions 读取与字节审计接口

分类：独立只读工程接口；不是新的数学接受条件。  
作者：ChatGPT / exact_refinement。  
日期：2026-11-14 UTC。

## 1. 源与实际输入范围

新入口是 `computations/exact_20261114_read_current576_artifact.py`，65,526 B，SHA-256 `791300246051bad9064a39cc181d0b5eb6d66d7978d73a28f0c8028f6d8e0329`。本说明形成时只执行了源码 AST 解析和静态字段核对，没有导入或执行任何科学生产源，也没有运行读取器。

入口明确绑定真正第 61 轮 run `43645948199` 和原 source commit `cf6b51193255dfc713610d2919598451ccdd49e2`。artifact ID、完整 ZIP 大小和 SHA 必须在实际产物出现后显式传入。源码没有伪填未来 artifact，也不把当前 main 的 SHA 当作原 run 的 SHA。

只允许 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。完整 ZIP 由已经在 actual62 读回中执行成功的原 transport 源处理：

| 仅导入的标准库模块 | 固定 SHA-256 |
|---|---|
| `exact_20261114_fetch_pinned_public_artifact.py` | `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` |
| `exact_20261114_audit_damped_chain_bytes.py` | `5618d29c41d95d668c959b05cee8295ce4285b2a50961277f557f8cfb717b440` |

读取器只在内存中替换 transport 的明确输入 PIN、读回 schema 和附加来源说明，并对 GitHub metadata 的 `workflow_run.head_sha` 另核原 commit。HTTPS、跨 origin 去 Authorization、流式完整 ZIP 大小和 SHA、ZIP 路径与特殊文件拒绝、全成员 CRC、安全新目录发布和临时 ZIP 清理均调用原 transport。`GITHUB_TOKEN` 仅通过环境传给该 fetch 步骤，不放在 CLI、源码或回执里。

四个第 61 轮实际数学/桥接源只读 SHA，不导入：

| 源 | SHA-256 |
|---|---|
| `exact_20261114_current576_damped_system.py` | `695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90` |
| `exact_20261114_current576_damped_chain_qr.py` | `ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f` |
| `geometry_20261114_native_current576_damped_solve.py` | `06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b` |
| `geometry_20261114_native_current576_damped_solve_hook.mjs` | `0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc` |

原 QR 类 `9b951f95…`、精确行核 `0bc8f978…`、字节 helper `b39e9dd9…` 和 spec 记录的原 client/worker/engine 文件同样只核字节。读回 workflow 的 checkout 应保留完整 computations，以便核这些固定 basename；不会执行其中的 RHS、Jacobian、ODE、求解或终态审计。

## 2. CLI

```bash
python -u "$VISIBLE_COMPUTATIONS/exact_20261114_read_current576_artifact.py" \
  --run-id 43645948199 \
  --artifact-id "$ACTUAL_ARTIFACT_ID" \
  --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ZIP_BYTES" \
  --expected-sha256 "$ACTUAL_ZIP_SHA256" \
  --source-commit cf6b51193255dfc713610d2919598451ccdd49e2 \
  --download-out "$RUNNER_TEMP/current576-original-artifact" \
  --out "$VISIBLE_OUT/current576-readback"
```

`ACTUAL_*` 是工作流从已经存在的原产物中登记的必需身份，不能填推测值。名称须为 `visible-mainline-current576native-43645948199-<真实attempt>`。两个输出目录都必须是独立新目录；transport 的目录必须位于 `RUNNER_TEMP`，其父目录预先存在。读取器不接收旧 28、41、54、57 大包，也不重复下载 actual59 父包。

完整下载后的原产物根直接包含 `native-current576-damped/`，不增加 `files/` 或 artifact 名目录。该原件目录保持只读。读回文件在另一目录，原数据不复制到读回输出。

## 3. 每轮原件链

读取器先保存原 `result.json` 的状态、原错误、原 J/audit 申请与返回字段，随后检查深层字节。数值失败不导致这些事实消失。

每个实际 `iteration-NNN` 分别处理：

1. 原 bridge summary、完整 `current-corrections.jsonl`、iteration 目录和真实 snapshot/result/context/manifest 一致；`native_call=1`，原 it 和 sequence 同序。原子进程的 argv、实际退出码、独立 stdout/stderr 和 returned-correction 引用逐一核对。
2. snapshot 的全部十阵按实际 chunk 顺序读取。九个状态、残差、出口、sigma、cut、far、H、target 阵与完整 `[576,224,224]` J 均核完整字节、大小和 SHA；576 个 J block 另保其实际逐块 SHA。没有用先前基态填补新轮。
3. 核实际 numerical sources/config、完整 cells、graphs/gains/far 身份，及原 `rawNode=[0,72,144,216,288,360,432,504,576]`。仅第 0 轮当前 state 必须等于实际59 selected raw SHA；以后每轮保其实际新 state。H、target、sigma、far 保本次固定原件；cut/far 残差不作零假设。
4. 原 minA/minD/meanHeight 的 IEEE `numberRecord` 按 bits 和分类核验，保留 NaN、正负 infinity 和负零的元数据表示。这不是新的 finite guard。原 norm 数字直接引用，不重算。
5. 子 QR 的 input binding、完整当前矩阵 definition 的 canonical SHA 和本轮 snapshot 逐字段关联。九份子程序导出的原输入与 snapshot 原字节相等。
6. 完整 QR 结果必须保所有 577 个 R/S/affine 因子及 129248 个纯常数分量，共 464891392 B；完整因子参数记录为 577 个 node penalty、1153 次 QR。读取每个 f64 字段并核已存 IEEE 分类及字节哈希，检查每个 R 下三角确为保存的零字节。所有常数均纳入审计，不重新算常数能量、秩、三角解或模型梯度。
7. 完整 z/delta 和 `[577,224]` checkpoint 包含全部 modes。负零 sidecar 解码与原方向 raw bytes 逐字比较。恢复 underflow 仅通过已存 z/delta 的零与非零 bits 分类核对；不重新形成 `sigma*z`。
8. 对完整精确行账，读取全部 cut112 + stage576×224 + far112，即 129248 行。核行序、每个二进制 dyadic 文本、原 J block、当前方向、实际 sigma word、每块已存最大值与全局选中记录的逐字段关联。最坏见证的完整 224 个 J 行 operand、方向和原 r 的 bits 回连到本轮 snapshot。**不重新加乘、除以 sigma、约分、比较有理数大小或重算范数。**

formed V/rho 的完整 provenance 和 canonical model identity 被核对；生产者没有导出的系数 payload 不由读取器重形成。原 R273 有限数组模型、原未缩放方程精确读回及原非线性接受结果保持各自范围。

## 4. 失败和 partial

`native_accepted` 不要求为 true。原 native 全迭代失败、最终 J/audit 失败或某轮子程序失败都按原报告保留。

如果某轮只有 partial snapshot/factor，则读取所有实际存在文件并核已有声明的 descriptor，明确写 `complete_qr_scope_verified=false`；不把 partial 因子当作完整方向。若生产者声称完整却缺文件、SHA 不符或行账不连续，审计返回非零并保已读的原标量和错误位置。这个 byte discrepancy 不追溯成为原 native 的数值接受门。

若规则同步或启动前置失败、连 native result 都没有，读回仍登记实际缺失范围和现有文件清单，不编造 iteration。

## 5. 输出与资源

主小报告是 `current576-readback-summary.json`，每轮有独立的 `original-readout.json`、`byte-summary.json` 和 `reader-status.json`。完整每轮字节细节、原 factor index、全文件清单和原 transport receipt 放在各级 `large-arrays/` 下 gzip 保存；这些目录应仅随 artifact 保留，不批量进入 Git。

读取器以已核缓存避免把父目录清单检查变成第三次大阵读取；文件变更通过实际 size/mtime 和已有 hash 关联检查。只保一小块 J/一个因子及小 JSON，完整 J/factor 不常驻内存。不复制原大阵，下载 ZIP 由原 transport 在完整提取核验后删除。

资源按实际完成轮数而不是成功预期分配。每完整轮原 snapshot 和 QR 的主要固定 raw payload 约 704385296 B，另有实际精确 ledger、checkpoint 和日志；32 轮固定 raw 为22540329472 B。读取工作流还需在下载期间容纳完整原 ZIP。这里没有假定实际轮数、压缩比或耗时，不据资源估算裁掉原常数或因子。

这些报告只支付原件身份与完整读回。真正的数学结论仍来自已经执行的原 Actions 数值；后续过程不需等待这个读回作为额外审批条件。
