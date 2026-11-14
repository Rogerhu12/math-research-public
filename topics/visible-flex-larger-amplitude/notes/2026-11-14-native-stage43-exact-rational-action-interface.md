# 原 stage43 / step11 的四局部 Jacobian 精确作用消费者

## 身份与执行范围

新增独立入口为
`computations/exact_20261114_single_step_rational_action.py`。

源文件为 35,445 字节，SHA256：

`9c42982291bd1a7b7cf21c472d8aae877136fb884708a8310ca6bb882c1d103e`。

本次实现只读取已经完成的捕获与方向文件。在本地仅做 Python AST 解析，未导入模块、未调用科学函数、未产生比较结果。全部实际整数、有理数及范数计算只允许在 `Rogerhu12/math-research-public` 自己的 GitHub Actions 中执行；入口同时检查 `GITHUB_ACTIONS=true` 与完整仓库名。源码只使用 Python 标准库，不导入原 native、NumPy 或 SciPy，也不调用 root、RHS、Jacobian、ODE、solve、trial 或 audit。

它消费 `geometry_20261114_native_stage43_local_j_probe.py` 的真实结果。捕获源三项固定为：

| 文件 | SHA256 |
|---|---|
| `geometry_20261114_native_stage43_local_j_probe.py` | `1185bbda5390c7ef3a9043ac59139b9359fececc802146f4be64aa7639730b21` |
| `geometry_20261114_native_stage43_local_j_probe_hook.mjs` | `8992f3920729b0f6eabf7a1e15520290fc47942c72c0c4d6433d8ac6cb291059` |
| `geometry_20261114_native_stage43_local_j_window.mjs` | `966ddc4946cc63f69260dd1871c2ac31ad0383eb5593f6c3a0b45b0cfcdef5ec` |

原完整 RK4 算术源为公开的
`topics/visible-flexible-closed-surface/scripts/78718-tail-fourier-product-flow.mjs`，
SHA256 `717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f`。

固定定位为原 stage 43、原 flow step 11、新 shooting stage 519、其入节点 520。这里的 520 是 1373 节点扩展系统的索引；向量分量仍为原 Q/Pi 坐标，不能把它当作原 577 节点索引。

## 三个被精确区分的有限对象

每条输入向量都比较以下三个完整作用：

1. 原 actual41 保存的 short-J 与两个 mean tangent rows 对该向量的精确作用。
2. 本次捕获中，同一次四级局部 A 调用随后产生的 observed short-J 与 mean tangent rows 对该向量的精确作用。
3. 把本次保存的四个 binary64 局部 A、原 h、原出口 port 解释为精确有理数以后，按原四级结构得到的作用。

第三项不把保存的局部 A 宣称为真实连续流导数。原 actual41 没有独立保存四个局部 A；相同状态、几何字段、源码与根求解记录属于复现证据，不能替代不存在的旧 A 字节比较。因此，只有第 2 项与第 3 项之差直接描述本次给定局部 A 后的浮点 tangent 传播及出口除法；第 1 项与第 3 项之差另保留复现差异。输出逐分量保存并精确核对

$$
J_{\rm old}v-\mathcal R(A_1,A_2,A_3,A_4)v
=
(J_{\rm old}-J_{\rm observed})v
+
(J_{\rm observed}v-\mathcal R(A_1,A_2,A_3,A_4)v).
$$

没有把任意一项改成新的原 native 接受门，也没有仅凭某个范数归因整个 block solve 的失败。

## 完整 RK4 作用

形状维数 $K=224$，完整输出维数 226，模式数 $M=112$。令 $P$ 取完整向量的前 224 个形状分量，$\iota v=(v,0,0)$。四个保存矩阵均为 $A_i\in\mathbb R^{226\times224}$，未施出口 port。

消费者逐项计算

$$
\begin{aligned}
k_1 &= A_1v,\\
k_2 &= A_2(v+\tfrac h2 Pk_1),\\
k_3 &= A_3(v+\tfrac h2 Pk_2),\\
k_4 &= A_4(v+hPk_3),\\
w &= \iota v+\tfrac h6(k_1+2k_2+2k_3+k_4).
\end{aligned}
$$

最后只有形状行 112 至 223 除以原出口 port；两个 mean 输出不缩放。均值行完整计算和保存，但不反馈到下一局部 A 的 224 列输入，这与原源码的矩阵乘法范围一致。原 step 的 port 实际为 1；代码仍从原位记录精确读入该数，不把一般端口接口与内部状态坐标混用。

所有 binary64 输入均直接从 little-endian 64 位字解码为整数乘二的幂。乘加、中间向量与四次矩阵作用均采用整数 dyadic 运算；最终除以 6、出口 port、原 sigma 及报告中的范数比采用 `Fraction`。不经过打印十进制重建，不形成普通浮点 dot，不先舍入小量或删模式。负零的位身份保留在原文件和输入 hash；其精确实值为零。

## 输入与绑定

必选：

```bash
python "$VISIBLE_TOPIC/computations/exact_20261114_single_step_rational_action.py" \
  --capture-directory "$VISIBLE_OUT/stage43-local-j" \
  --capture-result-sha256 "$ACTUAL_LOCAL_J_RESULT_SHA" \
  --out "$VISIBLE_OUT/stage43-exact-action"
```


`ACTUAL_LOCAL_J_RESULT_SHA` 必须来自已经完成的本次 `result.json`，不填预期或虚构 SHA。同一 Actions job 可以先完成捕获，再读取该真实文件的 SHA，随后执行消费者。输出目录必须是新目录。

消费者要求：

- `result.schema=original-native-stage43-local-j-capture-result-v1`，完整捕获已完成，四个 field 状态位与原 actual41 一致，原几何与 x/h 记录一致。
- actual41 result SHA 固定为 `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf`；actual44 原四字段 receipt SHA 固定为 `d7d00de365b2118e1346e8f8630d5bad408957da91fdf51f38496f73b0e0c5f2`。
- result 的 SHA 绑定完整 summary；result 与 summary 同时绑定 array-manifest 描述器，三者 producer/source 身份一致。
- 所有 manifest 数组的完整文件 SHA、字节数、`<f8`、C-order、shape 和有限位分类均核对。选定描述器与 manifest 完全相同。
- 四个 226×224 A、四个 226 状态/RHS、原及本次完整 short-J、两组 mean rows、完整入/出口状态均保留来源。field0 与原完整 226 入状态直接逐字比较。
- h、port、sigma 使用原 `float64le_hex`，另核 JSON 显示值和有限分类。sigma 仅用于原形状 stage 行的误差尺度；均值行不冒作原 224 条 stage 方程。

两个默认输入是 Q112 与 Pi112 的精确单位基。它们只是线性作用探针，未被当成非线性高度输入或 trial。

### 可选 actual43 最佳方向

要在同一次执行加入实际失败方向，追加：

```bash
  --direction-result "$GAUGE_SELECTED/result.json.gz" \
  --direction-result-sha256 "$ACTUAL43_RESULT_SHA"
```


只需保存 actual43 完整 result、result.step_delta 指向的原坐标完整 raw 文件，以及 result.step_direction_checkpoint 指向的完整 gzip checkpoint，保持原相对目录。无需下载或读取 transformed-J、G 系数、LU 因子或全行 exact ledger，更不会重形成 G 或重新求解。

消费者固定实际43 producer SHA `16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00`、G source SHA `24a51a4e804859bcdbed78b133599a073c6a0a890039e5fe5500281ef7e90b92`，并核原完整1372矩阵
`e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521`。
best_iteration 选中 raw 的 SHA 必须与最终 step_delta 相同；全部 1373×224 原 Q/Pi raw words 与 checkpoint（含 negative-zero 列）逐位核对，再原样取节点 520。该向量不缩放、不阈值化，也不因它来自失败方向而假称已解原系统。

## 输出、资源与解释边界

`input-binding.json` 保存完整输入描述器与源身份。每条向量产生：

- `case-XX-input.f64le`：实际完整输入原字节。
- `case-XX-exact-action.json.gz`：四级完整 dyadic 输入与导数、三个 226 分量精确作用、三种逐分量精确差、Q/Pi/均值/完整块的精确最大值与位置、原 sigma 下的形状差。
- numerator/denominator 以十六进制整数保存，dyadic 以整数和二进制指数保存。40 位十进制仅是明确标注的便于阅读近似；它不参与精确比较。

`summary.json` 保持小文本，`result.json.gz` 保留完整回执。若摘要的完整有理数太长，会改为指向 case 文件，不因出版大小拒绝科学结果。失败会保 traceback、已完成 case 与实际错误，不伪造完成。

每个向量的保守上界为 $6\cdot226\cdot224=303744$ 个 dyadic 标量乘积，三条输入最多 911232 个；精确代数零项可直接跳过，其余全部模式和耦合保留。没有矩阵乘矩阵或全 1372-block 操作。输入 raw 只数 MB，Python 整数内存取决于实际指数跨度；实际执行记录耗时、最大 RSS 和执行乘积计数，不预报已完成速度。

本入口回答的是保存有限数组之间的确定关系。它不能单独判定局部 A 的 root/隐式导数是否准确，不能证明真实连续 ODE 的导数误差，不能由三条向量推出整个矩阵的算子范数，也不能代替原 nonlinear residual、domain、trial、tol 或本课题任何完成标准。
