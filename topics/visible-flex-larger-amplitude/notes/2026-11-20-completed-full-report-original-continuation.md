# 从实际完整 QP 终态继续原模型：末阻尼、全部位置与显式后继模块

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

**状态：独立入口源码，未启动科学计算。** 正在进行的六方向仍用其冻结源。这个入口用于真实归因报告返回后，快速从其实际 `final.npz` 继续下一方向；不预设选择 v3，也不沿用旧数值当新父。

源为 `scripts/resume_20261120/launch_full_phi_from_completed_report.py`，16932 bytes，SHA256 `18ba10e5a37f5032b37388a7bfcdede97d11dc680685d73520732f9a278697f7`。

## 1. 复用已有真实状态规则

入口直接调用 `launch_refinement_from_full_report.py`（SHA256 `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60`）的 `terminal_damping`、`bound_parent_source` 和 `Locations`，没有另写一套阻尼或历史位置逻辑。先核实际父代码，再重放其阻尼规则；对于派生父，helper 从冻结原源和已刊 AST 转换重新构造完整 AST 并与实际源比较，不只相信 provenance 注释。

完整父报告必须 `complete=true`，且其 **`final_bundle_sha256`** 等于指定实际 bundle 的 SHA；它不是 coarse v7 使用的 `output_bundle_sha256`。观察 carrier 同样逐字绑定。末阻尼由每条真实方向的旧阻尼、接受标志、实际步长和满步预测比顺序重放；方向间每个阻尼须连续相符。没有方向时取该实际报告的 `initial_damping`，没有复制旧 job 常量或猜一个 `final_damping` 字段。

默认一个新方向、256 次推进、`qp-atol=0`；相对阈值、working row 上限、原 coarse 中心/低模、角数及各原有限筛选参数从父报告保持，允许调用者明确指定新的方向数/内步数/working row 数。默认保留实际父使用的 QP 模块字节；只有显式 `--qp-source` 才选择另一个模块，例如 R677 的 v3。全部物理、scalar、metric、正谱目标、坐标和步范数依赖仍逐 SHA 与父对应，不把换 solver 变成换问题。

本入口明确延续原 lift 模型。R671 非零尾模型仍须使用其自己的 context/全部六 jet 接口，不能把它的 bundle 交给本入口解释为原模型。

## 2. 全部永久位置的两项输入语义调整

原 driver 对单个 manifest 有 100000-byte 上限，并在六个位置用 `round(value,13)` 去重。完整报告可能记录更多实际 grid/任意位置，且不同 binary 点可以在这一截位下合并。为保持全部已知位置，入口复用已刊 R676 的 `derive_driver`：

- 去掉这一任意 manifest 字节上限，改为只消费明示的不可变纯位置 schema。
- 把六处小数截位键换成准确 binary 数值键。完全相同的数值位置可合并，不同位置不因此消失。

完整 AST 派生来源 `launch_fixed_g_refinement_qp.py` 的 SHA256 为 `100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622`。冻结原 driver 文件 `5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a` 一字不改；新生成的完整 driver 有自己的路径、header、派生记录和实际 SHA。

这项输入派生自身不改变数值线性 solver。若命令另显式选 v3，那是独立记录的模块变化，不能藏在“只改 manifest”的声明中。步问题仍是原 normalized-Phi、原完整范数和 `.992/.025` 条件；所有试步继续真读全部位置。

`Locations` 导出实际 report 的初末记忆、全部试步点、已付任意几何、tagged working rows、grid/radius counterpart 和保护代表。grid 位置只在 Actions 从绑定 carrier 的两个位置坐标向量恢复。所有调用者 manifest 也并入完整 union；已经是纯位置 schema 的文件另外原样传给 solver。旧格式若不是这个 schema，仍保留原文件 SHA，其全部位置经相同提取器进入 union，不继承其中的旧曲率或半径值。

## 3. 准备、实际运行与输出

`--print-command` 只读 JSON/文件字节、写独立 AST 派生源和准备 plan，并打印完整科学 argv；不读任何科学数组，不导入场模块。其未来 union 路径此时可以尚不存在，plan 明确待实际 stage 坐标解析。真正数组解析和求解只在本仓库公开 Actions。

准备物料位于 `WORK/OUTNAME-continuation-inputs/`，其中包括新完整 driver、`continuation-plan.json` 和实际解析后生成的 `complete-parent-and-caller-locations.json`。科学结果在指定新 `outdir/`，不会覆盖父或以前的方向。

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_from_completed_report.py" \
  --repo "$REPO" --work "$WORK" \
  --parent-report "$ACTUAL_FULL_REPORT" \
  --bundle "$ACTUAL_FULL_FINAL_BUNDLE" \
  --carrier "$SAME_SCALAR_CARRIER" \
  --manifest "$ALL_ORIGINAL_PERMANENT_POSITIONS" \
  --outdir "$WORK/full-phi-next-from-actual-report" \
  --qp-source "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullspace_feasible_active_cg_v3.py" \
  --directions 1 --maxiter 256 --qp-atol 0
```

`--manifest` 可重复，不能只给最近一次新峰而遗漏旧集合。省略 `--qp-source` 时保留父的实际模块；上例明确选择 v3 仅供真实报告支持采用时使用，现在没有安排该试验。

如果输入父本身已经是 R676 派生 driver 的实际输出，可用 `--parent-source` 指明其真实源文件，按已有 helper 核对 header 和 SHA。新输出正常返回后再核 `complete`、实际派生 driver SHA、实际 QP module SHA 及 `final_bundle_sha256`，并保存新末阻尼的同一规则重放结果。若子进程失败，原返回码和实际报告身份如实进入 plan，不凭预定方向数造成功。

所有 raw、位置全集与准备 plan 留在 runner work；公开记录只引用实际 run、输入/输出/source SHA 及紧凑结果。此入口没有新 fixture、独审门或本地科学试算。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
