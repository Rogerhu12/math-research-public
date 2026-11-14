# 同一共享背景 B 的闭几何接线

状态：独立源已写并作本地纯 AST/源 SHA 静态核对，**尚无可接受完整父场，未执行
实际几何计算，也没有新网格或新证书**。本入口只在本公开仓库 Actions 运行。

新入口为
`computations/geometry_20261114_shared_background_closed_assembly.py`。
它消费原完整 v3/v4 闭包以及
`geometry_20261114_shared_background_normal_form.py` 的完整 descriptor。
背景准备器保持原 SHA
`da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9`。
数学定义、表示误差账及转移界见
[共享背景与表示预算](2026-11-14-shared-background-and-representation-budget.md)。

## 1. 实际接了哪些函数

`SharedBackgroundAssembly.from_original(original, B, geometry)` 从已通过完整
身份门的原 assembly 创建独立包装对象。它不调用第二次 SE2 拟合，不重算
tail，不重新求 BVP，不产生另一套 prefix 状态。

- `scalar_jets(r)` 对同一精确共享节点实 Hermite (B) 求
  (B(r),B'(r),B''(r))。先按实际输入半径的精确二进制有理值计算，再明确
  舍入为 binary64 供原 renderer 使用；每个实际查询的这一步舍入差精确记录。
- `tail_jets(r,theta)` 的位置、一阶和二阶径向背景统一取上述三值。
  原非轴 FFT/Hermite 扰动及原径向、角向求导实现保持。
- `native_cut_nine(theta)` 的全部九个 ((r^i,	heta^j))、(0le i,jle2)
  jets 使用同一个 (B) 的 cut 节点 jets；角向背景导数仍严格为零。
- 旧 `delta_cache` 全部丢弃。原完整 `cut_difference(theta)` 经虚函数调用
  读取新的 native jets，从同一已配准完整 prefix 重新形成全部角函数差。
  没有把它投影为有限 theta Fourier 多项式，也没有只替换三个均值。
- 原 correction selectors 和非轴 collar 实现继续使用；新对象重新生成它们
  所消费的完整角向 cut difference。原 N 与 2N 未修补差诊断全部重新记录。

查询入口与冻结 tail evaluator 一样使用 binary64 半径和角度；若调用者
交来不能精确表示为 binary64 的扩展精度查询，入口明确拒绝，避免让 (B)
与扰动实际在两个不同半径/角度求值。这不降低原节点或 Fourier 系数精度。

关键不变量是 `A.height`：它仍是同一原表对象，三列内容的 canonical SHA
也逐次检查。原 renderer 的 metric 审计仍读取该表的 (w)，用原

\[
g_0=(1+w^2)\,dr^2+r^2\,d\theta^2.
\]

**没有**用 (B') 或 (1+B'^2) 替换目标度量。完整固定 scalar (p_*)、原
config、actual response、native Cartesian readout 继续沿原 loader 绑定。

## 2. 不变的原件与新增的身份

入口调用已冻结的 `load_full_bundle` 读取**原来源闭包**，保留其全部门：真实
accepted checkpoint、实际 nonlinear tail/J/audit、同 config/source、完整
H、R249 是否开启、三 nodal hashes、实际 complete readout、原计划与背景表、
mesh/normal hashes、唯一记录 SE2 和完整绝对 mean。

随后严格核 descriptor 的整个 `complete_field_binding` 与此原 bundle
一致，核 exact payload SHA，并从 exact 节点重建所有背景 coefficients。
全部半径与原 `background_radii` 逐项一致；每个 exact 0/1/2 节点都重新与
原表实际运算输出的 `as_integer_ratio()` 核对。完整 outer FFT 数据按实际
dtype 检查；不能把较高精度值转成 binary64 后仍称同一对象。

`cap_height`、cut offset、两帽和四个 marker 的原位置、完整 prefix 数值、
R249 选择及已有 SE2 全部不变。导出后另核实际 marker centers、mean gauge
和 registration 与原 assembly 逐项相同。

新导出绑定以下身份：

| 内容 | 绑定方式 |
|---|---|
| 新 wrapper | 自身文件 SHA |
| 原背景准备器与几何源码 | 8 项冻结源 SHA |
| descriptor / exact B | 文件 SHA / exact payload SHA |
| 原完整场与闭来源包 | 原 complete-field binding / 五件 closed bundle hashes |
| 原 prefix 定义 | 原字典完整保留及 canonical SHA |
| 原 FFT、帽/marker、SE2、R249 | 各自完整来源或 canonical SHA |
| 新 mesh 与 normal packet | 新 assembly 中的实际文件 SHA |

这里只给 (B) 一个明确连续 C² 定义。旧 FFT 径向舍入系数、三角求值、
完整 patch 的浮点计算仍有原来的表示误差责任；所记 Fraction-to-float
查询误差不冒充整个 renderer 或全域 C² 误差界。原 operator、曲率、reach、
held 包络不能继承为新几何的通过结果。

## 3. 为什么旧 loader 必须拒绝新包

冻结的旧 `load_full_bundle` 不检查新的 plan schema，也不理解 (B)
descriptor。若只加顶层说明字段，它可能对新网格按旧背景三列重新构造
另一对象，造成 mesh 与连续几何不一致。

因此新 plan/assembly 的 `large_core_prefix` 在原完整字典之外加入唯一
`closed_geometry_wrapper` 身份注记。注记明确 `identity_annotation_only=true`
和 `prefix_numerical_coefficients_unchanged=true`，同时保留原定义全文和
canonical SHA。它不改任何 prefix 系数。

旧 loader 的逐字典定义核对会自然拒绝此新对象。后续 **cover 与 held 必须
经新的 `load_shared_bundle(args)`**，不能直接运行旧入口后忽略该拒绝。
新 loader 有相同七元返回 API：

```text
paths, plan, assembly, reference_background, saved, A, bindings
```

它先重新验证原来源 bundle 和 descriptor，再核新 plan 除显式身份注记
外逐项等于原 plan，新 heights 除重新绑定新 plan 外逐项等于原表，新 mesh/
normal SHA 与新 assembly 一致。最后直接构造同一个共享 (B) 几何包装器，
不会从网格插值、不做新配准，也不会退回旧背景。

参数区分为：

- `directory/basename`：新的共享 B 闭包；
- `source_directory/source_basename`：原实际完整闭包；
- `descriptor`：本次精确 B descriptor；
- `checkpoint/port/config/tail_response/complete/source_topic`：原完整实际输入。

返回 bindings 保留原 prefix 定义，并把新 guard 定义、原/新闭包 hashes
和 B 身份一同写出。后续适配现有空间门时，只替换 loader；R241、R238、
held 的原门与误差余量不变。未产生接有新 loader 的真实 cover/held 报告前，
不能把旧 packet 当作这次新几何的结果。

## 4. 最小实际执行命令

只有真正接受完整父场、其 actual tail readout、原闭包及 descriptor 都已
存在时才运行。无需再执行原 nonlinear solve 或 source primitive：

```bash
python "$C/geometry_20261114_shared_background_closed_assembly.py" render \
  --source-directory "$ORIGINAL_CLOSED" --source-basename surface \
  --descriptor "$BACKGROUND_DESCRIPTOR" \
  --checkpoint "$ACTUAL_ACCEPTED" --port "$ORIGINAL_PORT" \
  --config "$ACTUAL_CONFIG" --tail-response "$ACTUAL_FINAL_AUDIT" \
  --complete "$ACTUAL_COMPLETE_READOUT" --source-topic "$PUBLIC_SOURCE_TOPIC" \
  --out-prefix "$NEW_CLOSED/surface" \
  --mean-batch 8 --reach-ring-stride 2 --reach-angle-stride 4
```

所有输出名必须尚不存在。它复制原 plan 的全部 rings、phase、marker、
实际频率与节点身份，只加新 B 身份；原 reference heights 的数值行原样
保留，显式改绑新 plan SHA。随后调用原 renderer，生成该新场自己的
mesh、normal packet、finite-pair 与 assembly 报告。

这不是新接受器，不把 `finished=true` 当作完成本课题。无父场时本入口
没有可执行对象，当前只保全其源码和接口。
