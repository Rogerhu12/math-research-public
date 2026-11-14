# rawCell0 原 RK 逐步系统及完整精确读回接口

日期：2026-11-14。以下是两个独立新消费者的源码与接口记录。仅完成标准库 AST/编译、冻结源码 SHA 和具体生产/消费字段的静态核对；**没有在本地计算新的 J、矩阵、方向或残差，也没有实际 step-capture 结果可供本接口宣称成功**。科学执行仅允许在 `Rogerhu12/math-research-public` 的 GitHub Actions。

## 1. 输入、范围和源码

直接父对象是 actual28 的完整原 576 段 native 捕获，`result.json` SHA 固定为 `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。其 112 个模式、224 个 shooting 坐标、577 个原节点、原 H/cut/far/scales 及所有原源身份沿冻结 binder 完整校验。

另一个输入必须是**实际完成**的 rawCell0 原 RK 逐步捕获。调用者明确传入它的目录和实际 `result.json` SHA；源码不预填任何尚不存在的结果 SHA，不消费不完整捕获。新对象直接替换 actual28 的原 stages 0–71，保留原 stages 72–575 的 **504 个 J、输出及残差原字节**。它不在先前 578 段对象上继续叠加映射，也不把那个对象冒称原父矩阵。

| 新消费者 | SHA-256 |
|---|---|
| `computations/exact_20261114_rawcell0_step_system.py`（38989 字节） | `fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81` |
| `computations/exact_20261114_rawcell0_step_equilibrated_correction.py`（19017 字节） | `30a467e8f08d73fcdcd8a69b2d911e0d9f57489c3397c21c775ed1ec4f6cabe6` |

逐步捕获生产者锁定为：

| 生产者 | SHA-256 |
|---|---|
| `geometry_20261114_native_rawcell0_step_capture.py` | `c2341018c6293e15ee8e5ba9109b331b29bee2e3e944514e1a0308afe8e6ffd5` |
| `geometry_20261114_native_rawcell0_step_capture_hook.mjs` | `2695cd2dc0abc66fe3f8ae8987b6ae3b50b884f692a418198347a61dddf24435` |
| `geometry_20261114_native_rawcell0_step_windows.mjs` | `07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b` |

冻结的实际 withJac flow 模块为 `717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f`；原 `integrationGrid` 模块为 `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f`。新窗口只在每个原步之前重新置 tangent 为单位矩阵，状态的完整 226 维、原 RHS、原 RK 更新表达式、原 profile 和 x/h 都由生产者保留。原出口 port 只施于该原段最后一个步的 Pi 输出及 J 的 Pi 行。

消费者复用的冻结原代码如下，均未修改：

- 原 capture binder / 浮点对照：`geometry_20261114_native_captured_band_correction.py`，SHA `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390`。
- 幂二均衡、带组装、单舍入精确 RHS：`geometry_20261114_native_equilibrated_band_correction.py`，SHA `8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3`。
- 与深度无关的逐行整数核：`exact_20261114_native_allrows_dyadic_residual.py`，SHA `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。这里只复用 `stage_job`、`boundary_job` 及精确二进制读数等无深度依赖函数，不调用其固定 576 的 row-order、stage-reader、far-witness 或 main。

## 2. 捕获格式和全部字节绑定

入口要求 `original-native-rawcell0-step-capture-result-v1` 与对应 summary 中 `capture_completed=True`，同一请求有意在原 solve 之前以 `VISIBLE_NATIVE_RAWCELL0_STEP_CAPTURE_COMPLETE_V1` 停止。原 native 接受标志保持 false。结果必须绑定原 H、candidate、far、scales、全部 actual28 数组和原 live 身份。

顶层文件包括 `rawcell0-step-spec.json`、`rawcell0-step-summary.json`、`rawcell0-step-array-manifest.json`、`large-array-chunks.jsonl`、72 个 `stage-NNN-completed-report.json`、逐段窗口身份及 `prospective-rawcell0-step-layout.json`。summary 中 `stage_reports` 是按原 stage 0–71 排序的文件描述符，不用一个未绑定的目录扫描推断来源。

每个原 stage $n$ 的实际步数记为 $L_n$。其四个独立完整数组为：

| 数组角色 | 形状与约定 |
|---|---|
| `full_states` | $(L_n+1)\times226$；第 0 行是原输入 224 维加两个正零均值状态，其后每个原步完整状态连续保存，均未施出口 port |
| `shape_outputs` | $L_n\times224$；除该段最后一步之外逐字等于相应 `full_states` 的前 224 项，最后一步只作原 Pi port 转换 |
| `shape_jacobians` | $L_n\times224\times224$；每步独立 tangent 起点，只有该段最后一步应用原出口 port |
| `mean_tangent_rows` | $L_n\times2\times224$；原两行均值变分保留在输入 artifact 中，不静默丢失证据 |

每个数组都保留 `<f8`、C-order、完整 shape、`total_bytes`、拼接 `raw_sha256` 和逐 chunk 描述符。使用原冻结 binder 的纯字节验证方法读取这个**新目录的新数组清单**，不调用旧捕获构造函数去冒认其数据。每块长度、文件 SHA、数组连续行范围、完整拼接 SHA 和跨数组文件唯一性均核验。

新捕获的 journal 允许四种数组按实际完成次序交错写入。消费者按 `(array,chunk_index)` 核对其与 manifest 的完整一一对应、每个数组内顺序及全覆盖，保留原 journal SHA，不错误地要求交错 journal 等于分组 manifest 的 flatten 顺序。额外的原 RHS/root 几何观测 gzip 包同样核压缩文件及解压原件的完整 size/SHA；这些已完成观测在本消费者中不重算。

每段 schedule 保留每一步的 `global_step/profile_index/grid_index/grid_branch`、x/h 二进制位、完整数组行号、四次原 RK field 调用及原出口 port。`profile_schedules` 给出每个原 profile 的真实 `step_count`、cuts、grid 与 ordinary h 位。消费者核其和原 cuts 的对应、全部 profile 覆盖和所有步编号。

**普通分支的 h 不用相邻舍入 x 值之差代替。** 普通分支保原 $x=n(1/12),h=1/12$；cusp 分支保原 `integrationGrid(12,cuts)` 输出和实际 x/h。段 11、28、31、63 等是否有 cusp 由原实际 profile 身份绑定，不能把它们假设成普通 12 步。总步数必须等于实际完成的 local-J 数和四分之一原 field 调用数。

## 3. 动态 shooting 映射与新残差

新深度由实际捕获决定：

$$
D=504+\sum_{n=0}^{71}L_n.
$$

不把第一项之外的总步数预设为 $72\times12$。所有原节点的新位置 `oldToNew[n]` 由此前实际段长累加得到，`oldToNew[576]=D`。

在一个原段内，捕获的 flow 顺序是 inner-to-outer。shooting 的行顺序相反。若 $o_n=\operatorname{oldToNew}[n]$，原 flow 步 $k\in\{0,\ldots,L_n-1\}$ 对应的新行段为

$$
i=o_n+L_n-1-k.
$$

原 577 个节点保原完整 224 维值，不由新出口覆盖。对 $1\leq k<L_n$，新节点 $o_n+L_n-k$ 取该段实际 `full_states[k,:224]`。该段新输出取逐步捕获的 `shape_outputs[k]`，定义本次有限数组残差

$$
r_i=\operatorname{RN}\bigl(\operatorname{out}_k-y_i\bigr).
$$

这里明确使用实际 binary64 减法后的存储数组，和 native 对有限输出的残差存储约定一致。内部节点的两个减法操作数是同一实际状态字；原段出口对照的是原出端节点，不能用旧残差代替一个可能发生位差的新出口。剩余 504 段则直接复用原 `stage-residuals` 与 `stage-out` 字节。

新矩阵逐段方程为

$$
J_i\,\delta_{i+1}-\delta_i+r_i=0.
$$

原 cut、far graph、cut target、physical H、cut residual 与 far residual 完全复用。原节点的 sigma 原字保留；所有插入节点的 sigma 显式取对应原 parent-stage 的 sigma。消费者另与捕获方导出的整个 `explicit-step-node-scales` 数组逐位核对，并独立重建全部 prospective cells/oldToNew 后比较。

新的完整范数遍历所有新行及其显式 sigma。它**不是**声称原 576 段矩阵的全行范数不变；保持的是所有旧节点 sigma、原边界及原 H。新旧矩阵的有限舍入表示分别具有身份，不能根据它们来自同一原 RK 步就宣称两个保存矩阵逐值相同。

## 4. 可调用 API 与矩阵身份

`RawCell0StepSystem(capture_directory, step_directory, actual_step_result_sha256, B=None)` 提供：

- `M=112,K=224,depth=D,original_depth=576`，以及完整 `old_to_new/cells/step_counts`。
- `all(name)` / `raw(name)`：新 base、outputs、residuals、显式 scales 及原边界/H 数组。
- `stages()` / `stage_bytes()` / `stage_raw(i)`：新完整 J 的有序流和单行见证所需原字节。
- `export_inputs(output)`：导出新状态/残差/边界数组；不重复复制全部大 J。
- `binding/arrays/J_rows`：全部原捕获、新捕获、producer、chunk、步映射和每块 J 身份。

生成的 `new_matrix_identity_sha256` 包括本 adapter 源 SHA、原 result SHA、新实际 result SHA、完整 cells/oldToNew、所有 J block SHA 及新有限数组 SHA。每次求解/均衡/精确读回都流读相同的完整块，不把旧 72 个长 J 误当新 step J。

`DynamicExactContext` 明确使用新 $D$：cut 行为 $j$，stage 行为 $112+i\cdot224+j$，far 行为 $112+D\cdot224+j$。完整行数为 $(D+1)224$。全系统最坏见证保存其新行号、对应原 stage/step、完整 J 行、下一节点方向、当前方向、残差及 sigma 的原二进制位。

## 5. 同一新矩阵的均衡、求解和精确误差修正

消费入口 `exact_20261114_rawcell0_step_equilibrated_correction.py` 复用已冻结幂二均衡与 LAPACK 接口，不生成新的 J 或 ODE 计算。cut、全部完整 step、far 按原模式排序；半带宽仍为 $k_l=112,k_u=335$，LAPACK 存储为

$$
\mathrm{AB}\in\mathbb R^{560\times((D+1)224)}.
$$

行列指数从显式 node sigma 的最近二进幂开始，再用保存系数的实际二进制指数作有界均衡。最终每个系数直接从原存储字按一次 `ldexp` 形成；过程中的非可逆缩放、下溢、实际恢复与原字节的差异照实保留。

每次方向都使用完整 cut/stage/far 的精确 dyadic 整数核读回，不用普通浮点 dot 替代。二进制操作数视为精确整数乘二次幂，所有产品和加减在整数中累积。每行精确 e、全系统/逐块最大值与坐标、完整行序、J/方向身份及最坏行 operands 均保留。误差修正右端由 $-e$ 乘最终行幂二尺度后，按 exact nearest/ties-even **单舍入**为 binary64，再解同一 LU。

修正次数有显式有限预算；精确新系统范数未严格下降时保前一个方向。没有把“完成线性诊断”称为 native 接受，也没有因该诊断新加课题完成门。解释框架沿 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md) 所述有限数组缺陷与非线性余项的区别。

最后把方向限制到原 577 个节点，另存新 schema `complete-original-node-restriction-of-rawcell0-step-direction-v1`，同时保全部负零位置。该限制不声称求解原长 J 系统。原 576 段浮点残差及其一个实际最坏行的精确值另作诊断，**不**用来选择/拒绝新方向，也不替代之后必须实际执行的原 nonlinear evaluate、原 trial 和原 native 全部验收。

## 6. 资源及 Actions CLI

默认 `--equilibration-passes 3 --refinement-steps 3 --exact-workers 2`，允许的范围分别为 0–8、0–8、1–4。`--max-band-bytes` 默认 4294967296，只是明确的单个带数组分配上限。实际 $D$ 得到后先写 `actual-memory-budget.json`；超过预算时报告资源限制而停止，不裁模式、节点、cusp 步或方程来适配内存。

该记录给出实际 band shape/bytes、潜在 LAPACK 副本的两倍数组预算、最大单原段 J 数组、完整 J 虚拟流大小、实际输入数组大小、exact worker 队列预算、cgroup 内存限制和 RSS。Python 大整数及 BLAS workspace 不伪称已包含在数组估算中。分解后另记真实 LU 是否共享 F-order 输入、指针身份及峰值 RSS；若实际生成了副本，及时释放不再使用的原 band 引用。

```sh
python "$COMPUTATIONS/exact_20261114_rawcell0_step_equilibrated_correction.py" \
  --capture-directory "$ACTUAL28_CAPTURE" \
  --step-directory "$ACTUAL_STEP_CAPTURE" \
  --step-result-sha256 "$ACTUAL_COMPLETED_STEP_RESULT_SHA256" \
  --equilibration-passes 3 --refinement-steps 3 --exact-workers 2 \
  --max-band-bytes 4294967296 \
  --out "$RUNNER_TEMP/rawcell0-step-equilibrated-correction"
```

`ACTUAL_COMPLETED_STEP_RESULT_SHA256` 必须来自将来真实完成并核验的捕获；此处没有占位结果被当作实际数值。输出目录须全新且不位于任一输入目录内。消费者全程只读两个源 artifact。

主要输出包括 `input-binding.json`、完整新系统数组与身份、资源账、均衡指数/缩放账、band/LU/pivot 身份、逐轮新方向 checkpoint、**全部** exact residual 行账及其单舍入 RHS、最终新全节点方向、独立原节点 restriction 和旧长矩阵诊断。所有大原数组和 exact JSONL 留在 artifact 的 `large-arrays/`，小摘要与 manifest 可按公开仓库规则出版。新 J 本体仍由已绑定的原 artifact 与 step artifact 提供；本输出明确标为虚拟流，不声称另外导出了重复的完整 J 文件。

本接口不读取私有仓库，不触发 native solve，不产生新的 closed field、reach、held distance 或 operator 完成结论。之后每一个实际成功或失败须按真实回执另记。
