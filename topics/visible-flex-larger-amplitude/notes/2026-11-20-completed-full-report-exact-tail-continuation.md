# 从实际 R671 完整 QP 终态继续同一非零尾模型

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

**状态：独立续算入口，只有源码与 AST 检查，未执行科学计算，也未安排后继方向。** 本入口用于实际 R671 完整报告返回后，从其真实 `final.npz` 继续；第一轮从原 lift 到非零尾的迁移仍用原入口。本入口不重新进行该迁移，不沿用旧 job 的阻尼常量。

源为 `scripts/resume_20261120/launch_full_phi_exact_tail_from_completed_report.py`，21935 bytes，SHA256 `425fd1d1254450afac26b2ca29ca4ffbb6fb93d59588163bef726e34999e4703`。

## 1. 实际父、真实末阻尼与同一模型

入口复用 `launch_refinement_from_full_report.py`（SHA256 `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60`）的完整父源绑定、末阻尼重放和历史位置提取。先核实际父 driver 的完整身份，再按该 driver 的已知规则恢复阻尼；若父是独立 AST 派生源，helper 会重新生成整个 AST 并与实际文件核对，不只相信注释。

父须是冻结 R671 driver `b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8` 的实际完整输出，或它经过下述已刊 manifest 输入派生后的输出。指定 bundle 的 SHA 必须等于报告 **`final_bundle_sha256`**；这与 coarse v7 的 `output_bundle_sha256` 不同。观察 carrier、准确节点报告和 scalar 输入也须分别与该实际父绑定相符。

末阻尼按父报告每条真实方向的阻尼、接受标志、步长和满步预测比顺序重放，方向间阻尼须连续相符：接受满步且满步比大于 `.75` 才减半并保留原下限；其他接受步保持；未接受方向乘四。没有方向时读取该父的 `initial_damping`。没有硬套别的 run 常数，也没有假设完整 driver 提供 coarse 格式的末阻尼字段。

非零模型完全从 `exact_tail_context_final.definition` 读取，重算 canonical SHA，并核它与初态 definition、顶层字段和实际输入一致。必须有 `0 < lambda <= 1`，以及准确相同的物理 eta 两端、mesh/M、原 g/scalar、观测 carrier、全部 canonical source 与 operator source。工厂固定为 `exact_reference_tail_lift.py`，SHA256 `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`。

CLI 故意不提供新的 lambda、eta 或迁移模式选择。生成的科学命令明确使用父的同一 lambda，`source-lambda=target-lambda`，并且只能 `migration=keep-q`。因此**种子传递本身**保持父的 q/H/core 以及同一个物理场；此处没有 nodal projection。plan 对应标记为 `seed_physical_field_changed_or_nodal_projection_performed=false`，只描述这一初始化步骤。后续 QP 接受步当然可以改变 q/H/core，并得到同一模型内的新物理场；该标记不宣称求解终态与父场相等。

## 2. 完整物理接口、目标与范数保持

入口仍通过冻结 R671 launcher 和完整 driver 接入同一工厂。native/observed 两算子、六 jet、完整 core 链、任意点 cotangent 和物理高度方向 `b-h` 全部保持；没有把非零尾 bundle 交回旧 lift 公式。其他物理、正谱、坐标、步范数依赖逐角色核 SHA，并额外核它们与 canonical model 的 scalar/integer/Hold/observed 及 dense/batch/observed 声明一致。

保持父的 normalized 正谱目标 `p=8, epsilon=.001, scale=.05`、径向混合比例 `.5`、角范数转折 `nu_c=24`、全部原未知量与观察行、数值几何筛选 `.992`、active band `.025` 和要求比例 `.03`。父的角数、coarse 低模/中心、目标阈值和其他有限筛选参数也从实际报告保持。这里保持的是父所用模型、目标和步范数；没有将非零尾等同于原 lift 的有限表示。

默认一个方向、256 次内推进、`qp-atol=0`。默认保留实际父 QP 模块的字节；只有显式 `--qp-source` 才选另一个模块，例如在真实归因支持后选择 R677 v3。该显式变化独立写入 plan，不混入“只改 manifest”的声明。相对阈值和 working row 上限默认沿用父；调用者如显式调整，完整 argv 与实际参数分别记录。

## 3. 全部永久位置与独立输入派生

复用 `launch_fixed_g_refinement_qp.py` 的 `derive_driver`（SHA256 `100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622`），只对独立新文件作已刊的输入语义派生：去掉单 manifest 的任意 100000-byte 截断；将六处 `round(value,13)` 键改为准确 binary 数值键，并明示纯位置 schema。冻结 R671 driver 一字不改，新完整 driver 保存自己的路径、来源和 SHA。这不会重新精化 mesh/M，也不改变数值线性 solver；另行选 QP 模块时如实独立记录。

共享 `Locations` 收集父报告全部已知格式中的初末几何、试步点、工作行、grid/radius counterpart、拒绝峰和保护代表，并合入调用者每份 manifest。已经是不可变纯位置 schema 的原 manifest 还会原样传入；旧格式保留其完整文件 SHA，全部识别位置经同一提取器进入 canonical union。不同 binary 位置不因小数截位丢失，完全相同的点可去重。

grid 位置仅在公开 Actions 从绑定 carrier 的两个位置向量恢复。所有位置在当前新场重新计算，旧曲率/半径值和旧合格标签不继承。工作行有界不意味着从永久非线性筛选中删除其他位置。

## 4. 直接调用与输出

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_exact_tail_from_completed_report.py" \
  --repo "$REPO" --work "$WORK" \
  --parent-report "$ACTUAL_R671_FULL_REPORT" \
  --bundle "$ACTUAL_R671_FINAL_BUNDLE" \
  --carrier "$SAME_OBSERVATION_CARRIER" \
  --node-report "$SAME_ACCURATE_NODE_REPORT" \
  --scalar-input "$SAME_SCALAR_INPUT" \
  --manifest "$ALL_ORIGINAL_PERMANENT_POSITIONS" \
  --outdir "$WORK/R671-next-from-actual-report" \
  --directions 1 --maxiter 256 --qp-atol 0
```

`--manifest` 可重复，须保留全部原集合。省略 `--qp-source` 即保留父模块；如有实际依据要换模块，显式附加该参数。若父本身是输入派生 driver 的输出，可用 `--parent-source` 指向其真实完整源。没有新的 lambda/eta/migration 参数，也没有继承别的 job 的预定父 SHA 或阻尼。

附加 `--print-command` 只读取 JSON/文件字节，进行源码身份/AST 准备，写完整 plan 并打印科学 argv；不导入科学模块、不读科学数组。此时未来位置 union 尚未生成是明示状态。真正坐标解析与求解仅在本仓库公开 Actions。

准备文件在 `WORK/OUTNAME-continuation-inputs/`：独立的 `derived-R671-full-phi-exact-positions.py`、`continuation-plan.json`，以及实际恢复位置后生成的 `complete-parent-and-caller-locations.json`。科学输出写入新的 `outdir`，父及既有方向不覆盖。plan 包含每个实际输入/源/派生源 SHA、完整 argv、末阻尼重放、canonical model 身份、参数、位置统计和实际返回码。

实际子进程返回零后，入口核报告完整性、实际 driver/QP 源 SHA、`final.npz` SHA、终态 canonical model 不变，以及初始化确为同 lambda 的 keep-q。新的 q/H/core 可随实际接受步改变；终态几何筛选按真实报告保存，不凭完成方向数或正常退出宣称达标，也不沿用父的连续证书。所有 raw、完整位置和准备 plan 留在 runner work；公开记录仅刊实际 run、SHA 与紧凑结论。此准备没有新 fixture 或本地科学运行。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
