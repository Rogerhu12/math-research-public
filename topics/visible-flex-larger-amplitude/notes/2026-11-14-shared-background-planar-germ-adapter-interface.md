# 共享 B 闭场的 R258 / R254 / marker 消费接口

作者：ChatGPT（geometry agent）  
日期：2026-11-14  
分类：既有证明的同场绑定适配与纯源码检查；没有新的数值或 δE 接受结论。

## 1. 针对的具体缺口

[`geometry_20261114_full_state_planar_germ.py`](../computations/geometry_20261114_full_state_planar_germ.py) 的精确内核已经覆盖实际完整前缀、同一 actual tail 的全部 FFT 节点、有限 collar、全角 outer correction 和四个固定 marker。然而其原入口只认识旧 `load_full_bundle`、未带 `closed_geometry_wrapper` 注记的前缀字典，以及旧 full-state held schema。

共享 B renderer 会保存带 guard 的 plan/assembly；正确消费者必须调用 `load_shared_bundle`。不能把新文件交给旧 loader，不能换旧证明摘要的标签，也不能删除实际闭包中的 guard。新增
`geometry_20261114_shared_background_planar_germ.py`
只补这三个明确的接口差异，保原证明内核和原返回状态。

它是已交付 `full_dn_closed_followup build/measure` 之外的独立步骤。先前闭场接口中记录的旧 R258 缺口，由本补件提供可执行绑定；该 build 本身仍不运行 planar-germ，新构造报告中相应键为 `planar_germ_shared_B_loader_adapter_invoked:false`。没有让尚未实际运行的证明成为闭场的已付结论。

## 2. 为什么共享 B 不要求重写角差证明

把原圆加非圆部分写为 $V(r,\theta)$，切口完整目标的径向 jets 写为 $T_i(\theta)$，把外侧共享 Hermite 基函数写为 $h_i(r)$。同一明确共享背景下的精确实规范形为

$$
F_B(r,\theta)=V(r,\theta)+B(r)e_z+
\sum_{i=0}^{2}h_i(r)\bigl[T_i(\theta)-V_i(c,\theta)-B^{(i)}(c)e_z\bigr].
$$

这里 $V_i(c,\theta)$ 是同一非公共背景部分的 cut 径向 jet；没有更换目标 metric，$B$ 也没有替代原 g 的定义。对同一个 r 和任意两角作差，直接相减得到

$$
\begin{aligned}
F_B(r,\theta)-F_B(r,\theta_0)
={}&V(r,\theta)-V(r,\theta_0)\\
&+\sum_{i=0}^{2}h_i(r)
\left[T_i(\theta)-T_i(\theta_0)
-V_i(c,\theta)+V_i(c,\theta_0)\right].
\end{aligned}
$$

所有 B 项严格消去；这是一条恒等式，不是小误差近似或线性化。无 outer patch 的部分令全部 $h_i=0$ 即可，collar 同样如此。完整高度 mean/z0 仍在曲面本身和其 cut/帽高度中，只因选用同半径差分见证而从这些差分中消去。

R258 正是消费这三个同半径位置差的仿射行列式。其 `ActualFFTNodes` 保完整 actual FFT 系数、原 radial dtype 与共享值/一阶/二阶节点；`prefix_cut_terms` 保完整实际前缀、同材料图和原 SE2 的精确实角；`prove_tail` 用原有理/Arb 行列式证据。因此在同一 `saved/tail/sigma/cut/W/ap/app/registration` 下，公共 B 不改变该证据对象。B 自己新增的径向节点也不会破坏结论：角差仍等于原分段多项式或实旋转包络表达式，进一步分割其径向区间不能使一个已证非恒零的行列式在开子区间恒零。

原 R258 从角解析性和非恒零径向见证排除平面开片的论证、原 marker 仿射独立检查以及相位/反射的非平面性转移原样使用。这里没有据 renderer 的高模浮点噪声推断精确非线性极限，也没有把四个样点不共面误当没有径向解析论证的普通点云事实。

## 3. 三个绑定改动

### 3.1 完整闭场使用新 loader

在原 R258 `main` 文本中，只给 parser 添加 `--source-directory`、`--source-basename`、`--descriptor` 三个几何参数。新的执行 namespace 显式把 `load_full_bundle` 入口绑定到 `geometry_20261114_shared_background_closed_assembly.load_shared_bundle`；实际所有原文件、原源、R249 节点、自己的 tail、B descriptor、原 metric table、mean/帽与记录的 SE2 都先经这个新 loader 验证。

源中保留原 `main` 和修改后 `main` 的 SHA，移除这唯一 parser 插入后必须逐字还原原函数。执行结束仍返回原 R258 的状态：非平面/marker 证明完成为 0，有 unresolved 为 2；没有新增数值阈值或审批步骤。

### 3.2 只向前缀证明提供经核实的私有数学视图

共享 B 对前缀数值系数没有改动，其 prefix guard 自己明确写着 `identity_annotation_only:true` 和 `prefix_numerical_coefficients_unchanged:true`。新 loader 已核这个结构，适配器再核：

- actual plan 和 actual assembly 的 guarded prefix 都精确等于 `guarded_definition(saved.definition, same_geometry)`；
- 二者保留的 `original_complete_prefix_definition` 精确等于同一 `saved.definition`；
- guard 要求的 loader 正是共享 B loader。

随后仅在传给原 `certify_prefix` 或原 prefix-report reuse 检查的**私有复制字典**中移除这一已核 identity-only guard。真实文件与完整 `complete_field_binding` 保持原样，旧几何 loader 从未接触这些新闭包。精确前缀函数看到的仍是字节绑定的同一 R249 shared physical knots/三列 nodal jets；没有复制、重投影或修改这些数值数组。

这使原前缀证明原有的完整 `saved.definition` equality 和共享节点 SHA 检查保留，而不是取消它们。已有 exact prefix report 只有确实属于同一 checkpoint/定义/节点/完整 witness artifacts 时才可复用。

### 3.3 optional held 必须是同一共享 B 报告

`--held-report` 可省略；省略不会阻塞独立非平面性证明。提供时必须是实际
`actual-complete-shared-background-held-Hausdorff-cover-witness-v1`
schema、正确 frozen producer SHA、同一完整新场 binding、同一 B descriptor SHA 和显式新 loader。

提供的 held 报告仍是它自己所声明的条件性整像距离证据，不在这里被升级为连续包络已经证明。没有把它的数值作为新的 planar-germ 验收门。

## 4. 直接 CLI 与原件要求

此入口沿用原 R258 的 NumPy/SciPy、`python-flint`/Arb runtime；只允许在本公开仓库 Actions 运行。它不重新解 BVP/native tail 或 radial ODE，但会按照原证明程序消费实际完整 tail FFT 节点、精确前缀与全部 tail/collar/outer patch pieces。

```bash
python computations/geometry_20261114_shared_background_planar_germ.py \
  --directory "$BUILD/shared/closed" --basename surface \
  --source-directory "$BUILD/normalized/closed" --source-basename surface \
  --descriptor "$BUILD/shared/background-normal-form.json.gz" \
  --checkpoint "$ACTUAL" --port "$PORT" --config "$CONFIG" \
  --tail-response "$FINAL_TAIL" --complete "$OWN_COMPLETE" \
  --source-topic "$ORIGINAL_PUBLIC_SOURCE" \
  --precision 160 --max-precision 2560 \
  --out "$OUT/shared-planar-germ"
```

可另传：

- `--prefix-report`：已完成的、相同 R249 finite prefix 的原 R254 报告及其全部相对 witness artifacts；
- `--held-report`：上面同一 shared closed 通过新 held consumer 得到的真实报告。

输入目录保持 `full_dn_closed_followup` 输出的完整 plan/assembly/background/normal/phase mesh 布局；actual complete tail 和其相对 raw-node 文件也全保留。真正数值/参数/SHA由后续实际请求绑定，没有填未来接受值。

输出沿原 R258：完整 prefix、tail、marker 证据与分块 witness/实际 FFT 节点记录，最终 `summary.json` 的 schema 为 `R258-actual-shared-background-planar-germ-inputs-v1`。完整 shared field binding、descriptor、原/新 main SHA、私有 prefix-view 规则及全部 frozen proof source SHA 都保存。没有新 workflow dispatch，本补件只是现有链之后可直接执行的组件。

## 5. 证明与未付项

如果此程序将来实际成功，它证明的是**这份精确共享节点规范形**的 prefix 与 tail/collar/outer-correction 各活动参数开片非平面，以及实际固定帽的 marker 代数。共享 B 的精确实 C² 定义可以被识别和绑定。

以下输出仍明确为 false / 未付，不能因本补件存在而提前销账：

- 所有 absolute mean/接口及 renderer 对精确规范形的 C²/误差转移；
- 全相位嵌入、原目标 g 的全域 metric 误差与 reach；
- supplied held 报告的连续包络与同一对象的实际连续 image-change 证明；
- 所有 R238 假设都已支付、实际 δE 已证为正、精确非线性极限非平面；
- 整课题完成。

`same_exact_common_background_mean_and_all_seams_C2_certified` 仍为 false；新增的 `shared_common_background_real_C2_definition_identified:true` 只说识别了这一明确 B，并不把“一个 C² 背景”扩张为“所有接口及全局假设已证”。不新增六或九 jet 必须机器精度收敛的门。

## 6. 本次静态核的具体范围

只读原 main、原 `ActualFFTNodes` / `prefix_cut_terms` / `prove_tail`、原 `certify_prefix` / reuse、实际 marker 与 shared loader/guard 来源。已做新文件 AST、七个冻结源 SHA、原 main 插入/反向剔除逐字 round trip，并确认本地没有 import 数值模块或运行新科学。原证明内核文件没有修改；未来实际证明是否通过，只由其 Actions 的完整报告决定。
