# 旧固定 g 的 face-PCG 启动器：独立核验物理 base，不改来源谱系

## 1. 实际失败与静态定位的界限

公开 run `45762076394` 的[实际返回记录](2026-11-26-public-actions-45762076394-1-part-003.md)显示，旧固定 g face-PCG 首入口实际在约 6.13 秒后以 exit 1 返回，未生成数值报告；已读外层错误为 captured preparation 的 `CalledProcessError`。这不是一次失败的 QP、预条件器或几何尝试。

静态源检查另定位到一个确定的接口错误。原 `launch_full_phi_exact_tail_from_completed_report.py`（`425fd1d1...`）使用

```python
original_base = parent_source.get('declared_derivation', {}).get(
    'frozen_driver_sha256', parent_source['sha256'])
if original_base != DRIVER_SHA:
    raise ValueError(...)
```

旧 composite 来源把 `frozen_driver_sha256` 放在该层，R683 all-row 来源把它放入 `published_composite_lineage`，v5 再加 `previous_all_rows_lineage`。已经由完整 binder 验证的 all-row/v5 父，在上述顶层查找中仍落到实际 **derived driver** SHA；它自然不等于冻结的物理 base `b1b0725a...`。该接口不匹配由代码和来源布局即可确定，但本文不把尚未显示的原内层 traceback 冒称为已经实读的异常文本。

## 2. 修复顺序与保留的检查

新 `face_pcg_verified_parent_source.py` 先调用原已刊 `derive_full_phi_face_pcg.py`（`7b3e7911...`）的完整 `bind_soc_parent`。旧 pure SOC、composite、all-row、v5 的全体 AST、真实 source SHA、runtime roles、保留的来源谱系等检查仍全部由原发布链执行。

只有原 binder 成功且报告明确 `actual_entire_body_AST_matched=True` 后，adapter 才：

1. 读取原 binder 已核验的 `model`。
2. 按独立字面 `BASES` 表选择对应 canonical 物理 base。
3. 对该实际文件再次核 SHA256，并核对该表与原 `7b3e...` 的 `BASES` 完全一致。
4. 在返回对象中另加 `verified_physical_base={model,path,sha256,...}`。

原 `declared_derivation`、实际 parent report 和实际 derived driver SHA 都保持原样。新字段描述的是 canonical 物理 base，绝不冒充实际运行 driver 的 SHA。

新 preparation-only planner 只把 `original_base` 的右端换为该已核字段。原 `DRIVER_SHA` 字面赋值以及 `if original_base != DRIVER_SHA` 比较均作 AST 核对并原样保留。原 fixed lambda/eta、scalar、node/carrier、M/J/N、谱参数、母范数、终端阻尼重放及完整位置并集检查不动。

对原模型 `18ba10e5...` planner 使用同一方式；两个 planner 的完整旧源 SHA 都仍在新 helper 中字面绑定。

## 3. 科学 driver 完全不改

新 adapter 的 `derive_driver` / `build_ast` 直接委托给原 `7b3e...`。新 launcher 先按原 `f092e359...` 完整构造旧 v5 launcher，再仅追加：

- 独立 parent adapter 的身份和默认路径；
- 上述完整 preparation-only planner；
- 两层 captured subprocess 的失败输出；
- 新来源记录。

原 v5 QP `76b27520...`、R683 all-row helper `a2c6d334...`、coarse Gram、完整模型和原科学参数不变。本次新的实际 continuation 从已返回 all-row 父 `d4bc3506...` 继续，使用该父真实终端 mu；新路径保留旧失败路径及日志。

旧纯报告 reader 仍可使用，因为实际科学 driver body/schema 没有改变。不得把这次启动器修复当成一次新的数学结论、一次新的有效数值方向，或一次已完成的加速比较。

## 4. 真实子错误的保留

原两个层级都用 `subprocess.run(..., check=True, capture_output=True, text=True)`，失败后外层 traceback 容易只留下 `CalledProcessError`。

新复制体保留捕获供成功时解析真实 argv，但采用 `check=False`。若子过程失败，先把其真实 stdout 和 stderr 写回 stderr，再携带原 returncode、args、stdout、stderr 抛出 `CalledProcessError`。成功时不把额外文字混进 `--print-command` 的标准输出。该修改不吞掉错误，也不将失败伪装成成功。

## 5. 已完成的静态核对

只运行标准库源构造，没有输入实际 field/report 数组，也没有科学 fixture：

- 新完整 launcher 可由原冻结发布链自然生成。
- 两个 model 的 preparation-only planner 均成功生成；四个预期编辑点恰好各一次。
- 两个 planner 的 literal physical `DRIVER_SHA` 赋值/比较均逐 AST 保持。
- 在同一真实源码与同一 manifest 源路径上，原 `7b3e...` 和新 adapter 生成的科学 driver **逐字节相同**，本次本地源构造中为 81,440 B、SHA256 `f6f9e8d4d6bd2e054a8a5f7c1612c6c1ead61dd02194c85025686ada0b903a7d`。这个摘要只描述本次给定路径的源构造；实际 Actions 的完整源身份仍须由当次报告绑定。

## 6. 完整文件

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `face_pcg_verified_parent_source.py` | 12013 | `8c3d11bb55c029ffcae23b126d566108947e9a92523574a53bfda7a4556f487f` |
| `launch_full_phi_face_pcg_verified_base.py` | 9781 | `618e5a988b733430dfe706897f4f695702b743e7f4a9953b651b5955ac89f36d` |

两源刊于 `scripts/resume_20261126/` 后，launcher 保持原 face CLI，并额外支持 `--verified-parent-adapter` 与纯源 `--prepare-source-only`。实际新 step 见对应小 JSON；该 step 不重跑 old chain 来重做旧结论，只从已经存在的完整实际父继续一次原 256 budget。

实际父 binder 的运行、修复后启动成功与否、真实 QP/SOC 返回、实际驻点残差及最终几何接受，仍须由本公开仓库 Actions 自然返回。本文不提前替它们填写成功。

实际完整首请求保 [参数](../computations/resume-20261126-face-PCG-verified-base-first-steps.json)，排在新固定深谷分支之后；d4bc报告、实际原driver和全部旧位置已在同runner，不重建旧方向。独立修复的实际成败按新唯一step读取。
