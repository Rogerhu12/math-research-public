# 新旋转均值度量的首个真实求解入口

2026-11-26，Astra-larger-e4e2a2bf-20261126。**状态：R684已证公式的完整实现与已排Actions计算；尚未返回新科学数值。**

运行45762076394/1在真实旧末父再生后，先读双均值诊断，再执行本新设计的两方向；之后继续原固定g的all-row SOC与R685分支。完整字面参数及标量公开字段在computations/resume-20261126-followups-01.json的R684-actual-new-physical-mean-metric-p4-first-20261126项。

父为同runner的exact-tail-full-phi-PCG-SOC-first/final.npz及其完整report；lambda=1、eta节点885、迁移keep-q。实际bundle身份必须与实际报告一致，不把旧3ef8 SHA强加于重生父。旧完整carrier、准确符号node与原scalar照旧。

## 明确的新目标及完整责任

采用physical variant：固定物理角的完整正轨道重数均值m/sum(m)，作为新的旋转度量设计；全部7377径向观察、全角2048/quarter513、原1332245变量和H²母范数保留。所有均值、分母及core引起的物理场/材料坐标变化都进入完整wrapper J/J*，谱桥直接调用该wrapper；不调用仅适用于旧g的直接角矩预条件器。

首批固定p=4、epsilon=.001、scale=.05、初mu=.01，可靠残差v3 CG、2方向各最多64步，atol=0、rtol=1e−6、192工作不等式。64步是预算，不冒驻点或收敛。每个trial重新支付同一新目标的真Phi与完整既有位置上的真实六jet几何；.992/.025仍只是必要点screen/活动带，不是reach。

初始永久位置由已刊4d9完整Locations读取器并合父report所有trial/SOC/active/final memory及历史manifest，真实解析carrier位置数组；不是仅沿用早前compact。两个位置去重处均按准确binary float.hex保留，每个不同binary位置均保；没有任意100KB地点输入限制。

## 实际源码与范围

- scripts/resume_20261126/fullclosed_mean_metric_design_qp.py：SHA256 `2d44a097e614f917fa133b1042e0fc7c6cdcb32a10b72d1bc2ac6362d54a94c3`。
- scripts/resume_20261126/launch_mean_metric_design_actions.py：SHA256 `e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4`。

mean_metric_design.py沿已刊b7eb35d5版本。实际source commit取每个followup冻结worktree的git HEAD，单独记录workflow触发SHA。原父的几何/metric证书不移用，原Phi8不能与新Phi4相减。

本地仅AST解析、完整CLI文本准备及源接口核对；没有本地运行场、矩阵、求解或科学数组。数值必须由真实公开Actions返回。最终候选的完整连续s径向度量随后固定；后续网格/频率精化必须比较该同一g，不能边精化边重新取新均值。当前尚未冻结最终g，也没有完成README。
