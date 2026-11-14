# 同一 $g,b_0$：一次高度四次阶段后的一次单 Q 联合 pilot

日期：2026-11-14。状态：**已证明的表示、Jacobian 与调用范围；新 driver 待公开人工检查。** 不包含新的实际求解结果。

新增文件：

- `scripts/frame_joint_height_objective.py`：当前位置的 signed-$z$ 非线性约束，与目标函数共用一次 geometry/Jacobian 评价；
- `scripts/frame_height_quartic_joint_audit.py`：四份输入回放、一次四次高度阶段、零 Q 嵌入、一次联合阶段、同态审计。

已公开的 quartic、单 Q、affine gate、原模型和输入报告不修改。

## 1. 本次选择的实际依据

公开高度阶段 `43630874689` 的完整报告位于
`notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz`。
解压后 SHA256 为
`f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3`。

该阶段在原九高度系数盒内找到了 sampled ball、signed-$z$ 和共同帽高可行点，但 metric 成本上升。这给新阶段一个明确用途：先在同一固定 $T,a$ 的高度可行域内改善 metric，而不是继续最小系数距离；然后只增一个入口所需角方向，联合改变 $u,v$ 与九高度系数。此前的失败输出继续保留，新的目标下降不能与不同采样网格的成本混比。

## 2. 四输入与原状态回放

driver 必须读取并以 decoded SHA256 绑定：

| 输入 | 公开来源 |
|---|---|
| 原独立高度 selected | `actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json` |
| 不可变原 $c_0$ | `actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json` |
| 完成的 short paired/bounded 审计 | `actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz` |
| 完成的九高度可行阶段 | `actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz` |

只有 `bounded_short` 路径用于当前真实 pilot。源实现、原完整 selected 状态、short 完整状态、九高度阶段初/末状态、准确 binary64 高度差、未改变的 $u,v,g$ 和采样定义均按已发布记录回放。不是把最终九个数字随意插入一个近似相似的模型。

上一阶段的完整**数值多面体**也保留：从原参考状态重建 $X,I$ 后，原 $A,b$、原盒、cap target、采样和数值定义必须重现。不会在重新评价时静默换一组更容易满足的门。任何输入/回放异常都写出小 JSON 和绑定摘要后退出，零次候选优化；阶段中途异常保留此前已完成 checkpoint。

## 3. 第一步：一次廉价高度四次阶段

保持原参考 $T,a$ 和全部九高度行/盒，以已公开 LP/QP 的选中高度为可行初值。目标和解析导数由 `frame_height_quartic.py` 给出：

$$
v=C(c-c^0),\qquad e=e_0+2U_z^0v+v^2,
\qquad q=q_0+T_zv,
$$

$$
J=\frac12\operatorname{mean}(e^2+2q^2).
$$

该阶段不需要每个 trial 重新构造曲面。预定最多一次 SLSQP：$120$ iterations、$300$ 个新目标评价或 $30$ 秒；三个预算先到者停止。逐圈无约束四次最小值、$S$ 和速度必要筛仍作为诊断，不参与改变约束。

输出的绝对高度系数及两个参考差均按准确 binary64 有理数核对。之后通过原 geometry 完整重建，核六个位置 jet 的有限高度变化、$T$ 不变、原采样帽高、signed-$z$ 与球。若完整重建不能通过声明容差，不进入联合阶段。

## 4. 第二步：零 Q 嵌入与新工作网格

通过 `SingleQProblem` 加入

$$
\lambda_Q W_5(t-t_c)B_3(t)\widehat Q(\theta),
\qquad \widehat Q\propto k_\theta/k^3
$$

这一列，初值 $\lambda_Q=0$。实际原 $162$ 维状态变成 $163$ 维。新状态完整保存，原数学场在零新系数下被包含，并在新工作网格上逐项核对六个位置 jet。该方向只提供必需 $v_8$ 的一个角分量，不代表完整 Cauchy 条件已经支付。

新工作网格为 $61$ 个均匀径向点，加原准确结构节点及入口 $24$ 等分点；合并后的实际节点数随报告记录。角节点 $192$。初态也在这张网格评价，工作成本只与同张网格上的成本比较。最终仍回到原 fine grid（当前 $160$ 个径向点）及 $384/768$ 角节点作同态审计。

原 $u,v$ 系数盒保持 $[-8,8]$；新归一 Q 系数也明确取 $[-8,8]$；九高度盒逐项沿用上一公开多面体。没有 metric 变量，没有新 $b_0$，没有改变核心或帽。

## 5. 两个真实硬约束

### 共同帽高

由不可变 $b_0$ 与相同高度基，

$$
h=\sigma\left(z_0+\int_0^L b_0\right)
+\sum_j\sigma I_j(L)c_j.
$$

其 $u,v,\lambda_Q$ 导数准确为零。`HeightAffineGate` 保存准确物理定义与本次冻结数值 row/intercept，目标仍是已选 $\tau=0.061$ 的 R66 上分支加 $0.001$ 余量；不是仅凭题目 $0.03D$ 自动得到的绝对阈值。

### 当前场的 signed-$z$

联合改变切向场时，上一阶段固定 $T$ 的高度多面体不可继续使用。现在每个工作节点都重新计算

$$
s_{ik}(p)=\sigma X_z(p;t_i,\theta_k)-z_{\min},
\qquad s_{ik}\ge0,
$$

$$
\partial_p s_{ik}=\sigma\,\partial_pX_z(p;t_i,\theta_k).
$$

此处保持上一阶段的 $z_{\min}=0$。这是所选正半带镜合分支的采样分离约束；单侧一般曲面并不无条件要求相同符号。它不是完整 reach 充分条件。

SLSQP 收到真实 affine cap `LinearConstraint`、当前 signed-$z$ 的非线性 inequality 与解析 Jacobian、原系数盒。没有把 `keep_feasible` 当作 SLSQP 保证，也没有在 trial 后暗中投影。

## 6. 目标、缓存和候选选择

联合目标保持原 direct metric 加原 ball/strip `smooth_positive` 项，ball/strip 未换成新的硬约束，也不改其数值阈值。每个不同参数状态只调用一次
`direct_residual_and_jacobian`，取得当前 $X,\partial_pX$、cost 和 gradient。目标 `fun/jac` 与 signed-$z$ `fun/jac` 共用同一缓存；不会为了约束再做一次热求积或 $\Pi$。

缓存只保成本、梯度、signed-$z$ 值/Jacobian 和小筛选记录，不保整个 residual Jacobian。报告记录缓存字节和实测 peak RSS。设工作采样总数为 $N$、参数数为 $163$，signed-$z$ Jacobian 的双精度数组占 $8N\cdot163$ 字节；整个 geometry 峰值会更大，不能把这个数组大小冒称总内存。

每个评价点都独立检查：原盒、cap affine margin、真实共同高度重构一致性、**当前** signed-$z$。best eligible 只能从同时通过这些门的点中选；较低成本但 signed-$z$ 失败的点仅作为未接受 trial 记录。库返回 success 不能绕过门。异常或预算退出保留已有 best eligible。

联合阶段预定最多一次 SLSQP：$80$ iterations、$120$ 个新 geometry/Jacobian 评价或 $300$ 秒。每 $10$ 次或 $60$ 秒保存 full checkpoint 与紧凑摘要。它是一次有明确新自由方向和真实约束的有限 pilot，不是把旧 $250$ 次配置延长。

## 7. 最终重构与解释边界

选中状态按完整准确系数回放，确认全部冻结 $g$ 与不可变高度参考仍相同。重新评价工作网格、原 fine grid 和同态角加倍，并报告：

- 全域及 entry/body/patch 的 direct metric 缺口；
- 共同帽高、当前 signed-$z$、ball、strip；
- 面积、曲率、镜像点对法弦筛；
- 新系数和完整位置二 jet 的角加倍差。

优化器的粗网格约束不保证 fine grid 或连续域通过；若精化发现违反，原样记录，不重新优化后伪称同一次结果。不可变高度积分的旧比较可作为来源证据，但不自动给当前改变后的 $T$ 全部积分误差认证。

特别是此前镜像法弦样本尚低于 $0.061$，只保证 signed-$z\ge0$ 并不能补这个缺口。当前 pilot 若降低 metric，仍必须继续处理 reach 与全局嵌入，任何一个门通过都不代表课题完成。

## 8. 人工 full-main 检查

新的 `--check-only` 用人工 carrier 生成四输入 fixture，经过 gzip/hash/完整状态/原数值多面体回放、零 Q 嵌入、完整重构、摘要绑定与同态角加倍。这个 geometry 路径选择 evaluation-only，不伪造 `GITHUB_ACTIONS`，不绕过真实研究求解 guard。

单次 SLSQP 与动态约束的优化调用由明确三变量数组 toy 另外覆盖：同一参数连续调用四个 callback 只触发一次评价；切向变量变化会改变 signed-$z$；能通过 cap/box 但违反当前 signed-$z$ 的点必须拒绝；第二次评价故意失败时保留已有合格初点。新源只做过本地 AST 检查，数值人工回执仍待公共 Actions。

```bash
python topics/visible-flex-new-mechanism/scripts/frame_height_quartic_joint_audit.py \
  --check-only --out "$RUNNER_TEMP/frame-height-quartic-joint-check.json"
```

实际命令另需上述四个路径和四个 `--expected-*-sha256`，且只能在 `Rogerhu12/math-research-public` 的真实 Actions 环境运行。输入或中途故障均留下可读小摘要；不会因文件尚未写完而只得到无诊断的空产物。
