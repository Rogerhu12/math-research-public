# 新 accepted 前缀的公共 R 切口导出入口

日期：2026-11-26。源码
[seam_bridge_cut_trace.py](../scripts/resume_20261126/seam_bridge_cut_trace.py)
在保存实际 accepted 前缀的同一公共 runner 上执行。
它不重建大 Flow、不评价 core、不求解边界问题，也不传出完整场数组。
当前只有源码及函数级校准；新实际场的数值结果须另记，不能继承旧场的 cut 数值。

## 最小父入口

父任务可一次调用
[seam_cut_pair_audit.py](../scripts/resume_20261126/seam_cut_pair_audit.py)，
依次执行原 accepted 尾的连续高度审计和实际前缀两 jet 比较：

~~~bash
python "$TOPIC/scripts/resume_20261126/seam_cut_pair_audit.py" \
  --source-run "$ACCEPTED_RUN/run.json" \
  --physical "$ACCEPTED_RUN/physical.npz" \
  --source-port "$WORK/m24-linear-port.json" \
  --short-bridge-source "$WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --tail-response "$ACCEPTED_TAIL_PACKET" \
  --out "$WORK/cut-pair-audit.json"
~~~

主 JSON 保留 `branches`、`normalized_Darboux`、`continuous_turning`、
`unique_turning_mean_bracket` 原字段，再增加 `bridge_tail_trace` 小摘要。
详细 JSON、日志与 NPZ 均放在同 runner 的 `cut-pair-audit-local/`，
不允许输出目录位于仓库内。该薄入口已通过语法检查，未实际运行新 accepted cut。

若只导出前缀端点，直接调用如下：

~~~bash
python "$TOPIC/scripts/resume_20261126/seam_bridge_cut_trace.py" \
  --source-run "$ACCEPTED_RUN/run.json" \
  --physical "$ACCEPTED_RUN/physical.npz" \
  --source-port "$WORK/m24-linear-port.json" \
  --short-bridge-source "$WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --out-npz "$WORK/current-cut-R-jets.npz" \
  --out "$WORK/current-cut-R-jets.json"
~~~

当同一 runner 还保存一个原 accepted 尾包时，追加
`--tail-packet "$ACCEPTED_TAIL_PACKET"`，即可同时输出实际完整高度
$R$ 阶 0、1、2 jet 的差。该输入仍先经过原残差门限、原 port 和全部真实背景
参数核验。工具不会从“有 accepted 尾包”自行推断 full-H；
warm `.25 H` 包若被用于诊断，仍只对应其缩小后的完整输入。

原 portable 前缀必须通过原 `prefix_gate` 及 raw success；
R63 固定 $g$ 分支必须带真实的 `finite_linear_candidate_pass`。
两种情况都校验 `physical.npz` SHA、当前 ShortBridge 源和 port 的记录绑定。
本工具可以处理 $M$ 不同的完整 $3M+1$ 列物理 quintic，
始终保留原 gauge $.06$ 和字面 mean1168。特别地，不把未知解参数
$q_{\rm actual}$ 代入 gauge 槽重乘已保存的 $Y$。

### 暖 v2、v3 与实际 nonlinear-DN 的显式接受门

暖 v1 和上述原线性分支仍保留各自的原门。明确列出的 v2、v3 分支分别调用
`warm_fixed_m3_model_v2.accepted_input` 和
`warm_fixed_m3_model_v3.accepted_input`，使用对应模型集中核验的实际身份。
v3 是冻结补弧坐标上的另一族 supported phase 控制，完整 `phase_basis`、
v2 零控制锚和全部实际 provider 依赖都由它的接受门绑定；本读取器不把
v3 解释成旧有限 span，也不修改 provider 或旧证书。
同一 Cartesian 图的重新表达保留 `solver_invoked=false`、
`solver_success=null` 和原成功求解器出处；脚本不会补造新的求解器成功，
也不会把未知模型版本解释成已知版本。

实际 nonlinear-DN 分支调用集中只读门
`warm_actual_dn_acceptance.accepted_actual_input`。它核验明确的
`audited_finite_actual_dn_candidate`、原始 RMS、实际 scaled/physical BC、
完整有限度量和成功返回，及原 outer check、完整 checkpoint、native 源的身份。
只读校验原接受的 $\lambda=1$ 线性源及其显式版本后，
逐项比较冻结 profile、warm 定义、provider、角图、gauge、mean1168、
版本化径向 chart 及物理尾参数。最终 raw、physical 和有限度量文件均核 SHA。

这一分支还必须把最终 `result`、`tail_seam`、真实 accepted stage、
`height-target-outer-XX.json` 与同一个 full-height 包串起来：
原请求 factor 为 $1$，原完整 Jacobian 和 audit 均已实际请求，
包的完整 `cutHeight` 和 request height 等于最终新场登记的
`candidate_H`。height-target 的物理和 raw SHA 必须等于最终字段；
实际入口最后使用字节复制保存 `physical.npz`，不会把同数组的另一次
不明序列化当作同一文件。原 `load_packet` 随后再次核实际尾残差门及背景。
如果同时指定 `--tail-packet`，必须给这一个最终包。

这些记录连同当次集中接受门的路径和 SHA 在 `source_acceptance` 中明确标出。它们证明的是实际有限返回
和完整输入的身份；公共 Cartesian 两jet是否一致仍由真实两侧迹及后续修补
预算决定，不能从 full-height 请求身份推出。

## 实际端点定义

`physical.npz` 最后一段是原公共 $C^2$ quintic。将其 binary64 系数和
物理节点解释为精确有理数，直接取最后左多项式在 $s_c$ 的 0、1、2 阶值，
再乘固定 gauge，得到完整 $qY$。

桥起点复用原 `multistage_flat_profile._reference` 的定义：

$$
s_b=\operatorname{binary}\left[
\left(\frac{\delta}{\operatorname{float}(\delta_{\rm ref})}\right)
\operatorname{float}\left(\sum_j\ell_j\right)\right].
$$

这里 $\delta$ 来自实际 `frozen_profile`；只作源代码的那一次规范乘法，
不能分别求 $T_u,T_d$ 后加起来制造一 ULP 假 cell。
终点是原 `physical.x[-1]`，并须逐字等于 $s_b+\mathrm{bridge.L}$。

当前 `ShortBridge` 只依赖同一个 cut、起始半径和桥参数；
$\delta,q,c$ 不改变它的相位形状。代码在同 runner 直接调用绑定的
`ShortBridge(cut,1.,curvature,peak_fraction)`，
显式传入原 `curvature=4,peak_fraction=.2`，不误用直接类的默认 $8,.5$。
实际返回的字面相位参数进入 40 阶精确有理原函数外包；
如果源平台生成的字面参数变化，也不会偷偷套用旧 field 的数值端点。

## mean 和公共 R 的两阶

区间求值保留与旧证书相同的 mean kernel 和 interval kernel SHA。
1168 个字面角点通过已登记的字节 SHA 逐字核验。
late quintic cutoff 的 0、1、2 jet 在 cut 为零；
core lift 的支撑在该点之前，故此处材料角就是 $\psi$。
工具计算同一 Frenet mean 的 $M,M_s$，并要求所有原 mean 节点的平方根严格正。

统一目标 cut 为 $R_c=\operatorname{binary}(.3)$、
$w_c=\operatorname{binary}(.08)$、$w_{R,c}=-7w_c/R_c$，
$E=1+w_c^2$。对每个完整 Cartesian 系数使用

$$
F_R=-\sqrt E\,F_s,\qquad
F_{RR}=E F_{ss}-\frac{w_cw_{R,c}}{\sqrt E}F_s.
$$

平面 Fourier 迹完整输出。竖向位置只输出相对于**同一个真高度原函数符号**
$Z_c$ 的值，NPZ 字段明确命名为 `height_R_jets_relative_Zc`；
没有将 $Z_c$ 选成零，也没有从旧场继承绝对高度界。
竖向一、二阶则是实际完整值。

若与尾比较，尾在上侧按原完整高度反射；在
$z_b=Z_c+\mu_c$ 的原合同下，零模位置差先符号消去，随后才计算其余区间差。
输出不是两个宽 $Z_c$ 区间相减，也不改变尾的 meanSlope/meanSecond。
记录同时区分两个精确合同：原 worker 的 binary64 总高度导数，
以及“真实 R58 背景导数 + 原字面 meanCorrection”所定义的高度导数。
后者才是相应真实背景替换的分量合同，二者差异连同总和 rounding
逐项给出。只有共享 $R$ stage 导出使用同一组扰动 cut 系数时，
后者才可直接当作该共享图的迹；不得自动把原 worker 总导数和它等同。
完整平面接缝还需同一尾共享 $R$ 图的实际平面节点两阶，
本入口不会以高度比较替代它。

## 已完成的源码校准

已执行 `py_compile`。函数级校准检查了：新入口对原已登记字面相位给出的
有理半径区间与直接原函数工具逐字相同；canonical $s_b$ 与旧已登记字面值相同；
解析旋转背景的完整上侧高度导数区间包含 $-w$ 和 $-w_R$。
这些检查未构造伪造的 accepted 包，不算新前缀或 full-H 通过。
大数组和 NPZ 仅保留在实际 runner，仓库只存源、入口和后续小执行记录。

2026-11-26 的 v3 读取适配只改变实际来源的明确分支与集中门调用；上述端点、mean1168 和公共 $R$ 公式不变。当前尚无新 v3 实际 cut 数值证书。
