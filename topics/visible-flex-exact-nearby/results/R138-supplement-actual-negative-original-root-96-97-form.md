# R138：原始根端 96/97 两模完整型的实际严格负方向

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

完整数学定义与先验包含见[两模合同](../notes/2026-11-20-R138-root-two-mode-form-contract.md)。

## 已完成结论

公共 [run44745192261/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44745192261) 完成同一 `Qrepair`、同一真实转向根、同一周期物理 frame 和同一固定点 `p=(0,0,1/2)` 的新有符号两模目标。不是从 Actions 的成功状态推断数学符号：完整保存、读回后的对称矩阵行列式严格负；一个明确的有理向量也直接给出严格负型。

本结论只排除“原始全部根数据上的齐次根型非负”这一充分路线。特别地，在全部原根数据上也不可能仅用有限常数乘非齐次根源的平方支付负部，因为令该源为零就与本次严格负方向矛盾。限制于实际全域解的可达根迹时，本次例子尚未排除这种下界。它不证明实际边值问题有核，不证明实际正区逆不存在，也不完成课题。后续必须保留原始 low `1..96` / high `97..infinity` 边界，以可达根迹相对体能量的估计，或其他完整正区逆路线继续。

## 原对象、规范与完整符号

归一角内积为 `(2*pi)^(-1) integral_0^(2*pi)`。两基向量为

\[
 z_1=\sqrt2\sin(384\phi),\qquad
 z_2=\sqrt2\sin(388\phi),
 \qquad f=S z,
 \quad S=P_{1..96}N+P_{\ge97}N^{1/3}.
\]

这是原始第 96、97 模；没有平移原始低高分界。完整独立 mean 通过此前 actual mean 证书的非零分母消元。局部七项、mean rank、两个非局部 primitive 项均包含在目标中。全部 `32768` 闭角格和全部 `32768` 非局部接收格完成，整圈为 `[0,2*pi]`。

令 `M=(M11,M12;M12,M22)` 为该归一齐次根型在这两模上的矩阵。以下十进制区间只是原保存整数球的向外放宽，判断用原整数球：

| 量 | 完整保存球的有理向外包围 |
|---|---|
| `M11` | `[-0.017488, 0.456226]` |
| `M12` | `[18.907223, 21.291389]` |
| `M22` | `[2.221014, 2.403899]` |
| `det M` | `[-453.405384, -353.544241]` |
| `z=(1,-264577/30440)` 的完整型 | `[-202.346427, -146.611290]` |

特别地，保存球直接给

\[
 \det M<-353,
 \qquad
 (1,-264577/30440)\,M\,(1,-264577/30440)^T<-146.
\]

`M11` 的球跨过零无碍上述结论；这里没有将某个未分离的对角符号当作证明。精确有理向量及其完整有符号型保存在 `negative_witness`，而非仅保存一个负浮点近似。

## 没有缩小旧轴误差球

两模消费者读取完整旧 `nominal_q`、`nominal_s` 和 `complete_axis_error`，没有使用旧简写的 `true_root_support_coordinates`，也没有截去正的误差尾。新的完整保存轴区间包含旧完整二维误差球的外接矩形；读回后分别约为

\[
 q\in[-0.355042325,-0.006313255],
 \qquad s\in[0.970374655,1.319103725].
\]

本次审计以有理算术逐项验证：新的 `q/s` 区间确实包含旧完整 nominal 球加减完整 error 上端；每个 actual 矩阵球包含保存 affine 三项在整个该矩形上的区间值；保存行列式球包含从三个完整矩阵球作乘积减法所得的整个区间；保存 witness 球也包含从完整矩阵球和精确有理系数所得的整个区间。两个上端严格负均由原整数球直接比较，未重做任何科学目标。

## 输入、执行与保存审计

- manifest 的 **20** 项 current pin 与 execution receipt 逐项完全相等；在本地当前公开文件上重核 bytes、SHA-256、Git blob SHA，全部吻合。
- **6** 项历史恢复 receipt 与 manifest 完全相等，且对五个原 cubic shard 和一个原 root germ 的本地原 Git blob 重新作字节/哈希核验，全部吻合。恢复仅供定义，未调用旧 producer。
- 输出恰为 manifest 的 **34** 个顶层字段。完整原 axis、mean、X 三份引用与所 pin 原 JSON 对象逐项相等；旧 X 的 false 门和全部原 scope 保留。
- 输出中的 **86** 个完整十进制球记录（含整份旧引用）均符合整数 midpoint/radius/exponent 格式，radius 非负。实际矩阵、行列式、witness 的全部读回与严格符号逻辑对应所 pin science source。
- `complete=True`、`proved=True` 表示本次完整有符号包围完成；`negative_two_mode_direction_proved=True` 和 `all_root_data_nonnegative_form_excluded=True` 有上述原球依据。
- `actual_positive_boundary_problem_singular`、`positive_inverse_proved`、`final_topic_complete` 全为 `False`。
- 一个科学 child，返回码 `0`，无 timeout；科学计时 `55.778553555 s`，child wall `55.887457631 s`。运行 Python `3.12.14`、NumPy `2.3.5`、python-flint `0.9.0`，Arb `320` bits。
- 四种旧目标调用计数均为 `0`；旧 numerical producer / completed target 重算均为 `0`。私有 `mid64/rad64` 缓存与 response prefix 合计 `26738688` bytes，每次写入检查完整 Arb 包含，未发表数组、artifact 或 Release。
- execution 记录 `5` 次 README 检查（保存首个和最后三个完整 receipt），保存 receipt 的根/题 README diff 均为空；发布经历 `2` 次尝试。结果发布容量记录 `199429855` bytes，小于 `200000000`。

## 精确公开来源

- actual：`notes/root_two_mode_form_ci/run-44745192261-1/root-two-mode-conclusion.json`，`36248` bytes，SHA-256 `95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2`。
- execution：同目录 `execution.json`，`14435` bytes，SHA-256 `f66a976a0433204c9c043ab977d58439f091d2304b6cd9ef1df13eac0ae2c0f2`。
- report：同目录 `report.md`，`607` bytes，SHA-256 `792930a1937f0f85a9d44741e335995e5eb1a806403335af440b68fc789177e5`。
- manifest：`notes/2026-11-20-R138-root-two-mode-form-inputs.json`，SHA-256 `2e878faa9a3b62ffd8b827b39398872cf9fe8e50c793689d19385eca61226870`。
- science：`scripts/fourfold_codazzi_root_two_mode_form.py`，SHA-256 `817f033d72060c524539c79a7d3661aa3754ed2ca3eafd5b034f34a13882ab74`。
- 私有缓存哈希（仅识别，不发表内容）：`f887fc0622a7fa7cbb3520a9e966a2915c4162c138f232e54a81676c5a364bf6`；response prefix `26efa66ca03a6a7ac42618bed8bc2ca9cc2d33c346e598b42d2d2ffbf70ddb15`。

本条是实际完整负方向，不是全根型的有限截断正性，也没有覆盖任何未计算的高尾。相对体能量路线仍须完整保留 mean、非齐次根源、原 `r_E/r_B` 和无限 high 作用。
