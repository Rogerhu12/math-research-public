# R252 完整物理角测试：实际续接入口

2026-11-14，amplitude，AI 辅助。

**状态：新有限边界定义和可执行源码；尚未得到该新问题的数值接受。**
数学公式和全部核心、物理及标量导数见 [R252](../results/R252-physical-angle-DN-Galerkin-boundary.md)。这里不把新测试的零点称为旧材料角测试的零点。

## 实际选择依据

公开 Actions `43593855655` 的方向诊断直接消费原 `43592195185` 的完整带 LU 方向、右端、699 节点场、真实 T112 零锚和更早的实际齐次末端子空间。其材料换角方块 $P$ 的浮点条件估计为 $1.14478\times10^{17}$，一次行列均衡后为 $1.50380\times10^{17}$；相对最大奇异值 $10^{-12}$ 的数值秩仅 71/112。这里的数值秩不是精确秩证书，且与 R250 的精确可逆性不矛盾。

真实方向的材料角非均值采样 $L^2$ 为 4942.03066679，保留的 112 模只有 7.104670828，比例约 0.00143760。原完整右 BC 和其齐次末端约束同样病态。诊断扩展到 $\alpha=2^{-40}$ 仍未得到完整有限残差，因而没有 Taylor 收敛结果。这些证据支持改变有限测试方式，不能由此断言所有原矩阵错误都仅来自 $P$。原全 ODE、所有模、完整尾以及原失败记录均保留。

## 明确的新边界

完整物理状态、全部 112 个核心、三个固定支撑的标量控制以及同一个真实 T112 native 尾均保持。高度输入仍是

$$H=e_hP(c)z_+.$$

新右边的全部 112 行为

$$R_\varphi=v_+-\gamma S(c)D(H),$$

其中 $S$ 是完整 native 材料角斜率拉回物理角后的非均值投影。原测试是 $R_\theta=Pv_+-\gamma D(H)$。新测试既不计算 $P^{-1}$，也不是对旧测试施加一个可逆左预条件器。有限截断身份

$$R_\varphi-SR_\theta=(I-SP)v_+,\qquad
R_\theta-PR_\varphi=\gamma(PS-I)D(H)$$

和完整谱尾都必须实测。新源码不会把 $R_\varphi$ 的接受旗移给 $R_\theta$。

`geometry_20261114_physical_test_boundary.py` 继承原维数及材料高度映射，只改变非均值斜率测试。直接物理导数项为 $Z_+f_y$，全部核心列包含 $S_jD+e_hSJP_jz_+$ 两项；三个 scalar 的局部列取原 $Z_+f_p$，其全段影响仍由完整增广 ODE 传递。

## 同一公开任务中的执行顺序

第一步运行 `geometry_20261114_physical_test_response.py`：

```bash
python -u "$COMPUTATIONS/geometry_20261114_physical_test_response.py" \
  --accepted "$ACCEPTED96" --prepared "$WARM699" \
  --tail-anchor "$RUN11/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$T112_CONFIG" \
  --qr-reduced "$RUN10/full-DN112/reduced-001.npz" \
  --out "$OUT/physical-response" \
  --material-angles 4096 --physical-angles 4096
```

输入 SHA 在源码完整固定，分别为真接受 M96 来源 `b4d2b98a…`、原699节点准备场 `0f94dd88…`、真实 T112 零锚 `e788a28d…`、其配置 `01930f3b…` 和原齐次末端包 `ef8164f7…`。这些是原文件的身份核对，不是新数值接受。响应检查不启动 Node、不求新尾、不构造全段 Jacobian。

边界 FD 使用已完成的**真实非线性 T112 全 Jacobian**作为明确的仿射内层映射；不使用 `ready.linearD`。从原端点添加与旧 FD 相同的微小非零高度，覆盖 $S_jD$ 和 $SJP_jz_+$。完整直接/增广方向、三个中心差分步、两层 Richardson、截断收缩检查及原 $5\times10^{-5}$ 门均保留。末端小矩阵只是只读诊断，不另加条件数门。

通过后同一任务立即执行 `geometry_20261114_physical_test_full_dn.py`，传原 `coupling112banded` 的完整求解参数；`--response-check` 指向上述新响应报告，另加 `--physical-angles 4096`。没有第二个 `--original-response-check` 参数。原 699 节点准备场和严格 T112 零锚继续复用；此后非零高度和最终 audit 仍调用真实 native 求解器。

完整原带 LU、全部物理/核心/标量行、原 Newton、17 档回溯、1200 节点预算、RMS $10^{-6}$、边界 $10^{-11}$、固定实际 $p^*$ 的物理 RMS 以及最终真实尾 audit 均不放宽。这里边界数值门明确测新 $R_\varphi$。输出 `finite_boundary_scheme=physical-phi-complete-DN-v1`，并将旧材料测试单列。

## 真实读出与后续限制

最终 `final_height_seam` 保留原 $R_\theta$、材料均值及二阶高度读出；新的 `physical_test_cut_audit.audit_cut` 在原输入规则下绑定完整真实 H 和 native 响应，然后用两档角网格测同一有限场、同一个 D。加密 audit 不改变 native 输入。

输出同时包括新旧残差、两条投影缺项、正确物理/材料均值、全角高度与斜率谱、全部角网格差。它们是实际测量，不是附加 Newton 门，也不等于已证明完整接缝。后续物理读出、完整 C² 闭组装、入口规范形、整面度量、全族 reach 和真实像 Hausdorff 幅度仍须消费该新场自己的数据。

没有本地新数值，没有已接受新闭面，也没有把测试改写当成本题完成。
