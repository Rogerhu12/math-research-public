# 固定曲率 58 后恢复度量预算：19 输入完整消费器

状态：独立新源码及完整人工入口已通过；尚未运行本阶段真实研究候选。旧源码、实际报告和旧目标结果均保留。建议公开 lane 为 `metric_budget_recovery`。

## 1. 实际依据与本次唯一角色转换

来源是 [reserve 实际记录](curvature-soc-metric-reserve-first-actual-result-20261115.md)：run `43665345551`、source `0aae9a6a85583a9f87415e586d8db2c9c7fea6a7`。唯一初态是报告保存的完整 163 系数物理态

`512de71f983e86521dda4250e387ed1449ce29626763f49accde94bdc89666a9`。

该点 768 网的真实最大主曲率为约 $56.98196757$，最大度量算子误差为约 $0.2671995668$；原两网物理门均过，旧曲率目标 55 未达到。本次明确取固定硬曲率上界 $\Lambda=58$，原已合格度量预算 $b_{\rm old}=167/625$，新恢复目标 $b_*=13/50$。这不是把旧 55 宣布成功，也不提高原度量或其他物理门。

完整 $g$ 仍为

`fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。

固定 $b_0$、163 维空间、共同高度原函数、全部系数盒、帽高、正高度、球、内条带、镜像门及原容差均继承。改变的是约束角色和约束 identity；物理 state identity 不加入 $b_*$、$\Lambda$ 或 LP slack。

## 2. 完整消费及源身份

新增三件源码：

- `frame_metric_budget_restoration_rows.py`：11 组值、完整二 jet 导数、角色与细池迁移。
- `frame_metric_budget_recovery.py`：完整两网 objective、选行 Jacobian、主 LP、实际残差 SOC、抛物线回退和接纳。
- `frame_metric_budget_recovery_audit.py`：19 个完整报告的字节/来源/系数/池回放、人工入口、研究入口、原子检查点和语义摘要。

前 18 输入逐项复用已发布 reserve 消费链；第 19 输入为其已完成报告，decoded SHA256 必须为

`c538761402019083cd90f0227ae62d12c68b884a8e829bc1209dcdb266b2dfb2`。

消费器核全部 163 个 `Fraction.from_float` 系数、canonical 物理态、完整 $g/b_0$、既往 source/config、两网坐标、最后接纳记录和旧原始失败辅助量。原粗池 4,240 行、细池 1,310 行均保留，含 ID、组顺序、坐标和哈希。不重跑任何既往优化。输入异常先保存小失败 JSON，不进入新几何。

## 3. 度量恢复与硬门的分账

令 $T=X_\theta/a$，$e=|X_s|^2-1$，$f=X_s\cdot T$。真实算子误差和新目标行分别为

$$
\eta=\frac{|e|+\sqrt{e^2+4f^2}}2,\qquad
m_\mp=b_*\mp e-\frac{f^2}{b_*}.
$$

只有原编号 0、1 的两组 $m$ 可用共同非负 slack 恢复。2–6 仍为原正高度、球、条带和镜像硬行；7–10 是固定 $\Lambda=58$ 的真实曲率 PSD 硬行。曲率使用 [R103](../results/R103-actual-metric-curvature-semidefinite-gates.md) 的实际第一、第二基本形式，保 $q>0$ 和直接主曲率独立筛，不用目标度量冒充实际第一形式。

每个新接纳点必须在原 384、768 两完整网同时通过全部硬门及原 $b_{\rm old}$，且两网合并的真实最大 $\eta$ 严格下降。一般下降门为 $10^{-7}$；若直接达到新目标，只要求真实严格下降。只有两网直接 $\eta$ 和新目标两组 Schur 行同时通过，才标记本阶段目标达到。

初态不必已过 $0.26$。输出分别记录 `single_grid_hard_gate_pass`、`previous_metric_budget_pass`、`single_grid_admissible_recovery_point`、`single_grid_new_target_qualified`，不把预测 slack 或只过池内行解释为完整网合格。

## 4. 软行分离和细网二阶导数

新目标初始已有违例，不能把所有负 $m$ 一次加入池。软行按“比当前选中软行最坏 slack 更差”的真实包络分离，并补完整网真实 $\eta$ 峰的两条行。硬 2–10 组仍按原真实容差收集所有遗漏违例；返回或容量耗尽时不把遗漏当作已通过。

细网从 7 组扩为 11 组，ID 仍为

$$
g(N_rN_\theta)+i_rN_\theta+i_\theta.
$$

原 0–6 组 ID 不动；新增 7–10 组放在原末尾之后。粗池容量仍 12,000，细池容量仍 4,096。超过容量保最后完整网合格态并明确退出，不能默默丢旧行。

细网选行使用完整 768 角圈，每批 6 个所属径向行加原 $0,L$ 两端，最多 8 行。有曲率行时请求完整位置二 jet 和参数二 jet；普通批可用一 jet。每批先核同状态六个位置 jet、$T$、共同中心、度量和高度与原全网一致，才保所选 Jacobian 行。粗网仍最多 16 个所属行加两端。固定高度均值网仍为 384，角查询不改变 $b_0$ 或共同原函数。

单份 `(8,768,3,163)` 的 float64 参数 jet 约 24 MB；多个 jet、形式、缓存会叠加。本阶段尚无真实 RSS 数据，不能把选行矩阵很小等同于全几何临时内存很小。人工回执保存批大小、普通 jet 同态差与缓存复用结果，实际报告会记录真实峰值内存。

## 5. 主步及实际软残差 SOC

主 LP 在继承的归一化信赖域 $10^{-3}$ 内最小化

$$
\rho+10^{-6}\|p\|_{\infty,\rm box},\qquad
m(x)+J_m(x)p+\rho\ge0,\quad\rho\ge0.
$$

硬行用原 fraction-to-boundary 方向；盒和共同帽高保持真仿射约束、不加 slack。解后独立核线性行、盒、帽高和预测改善。

对已经完成两网真实取值的 $y=x+p$，只允许一次 SOC。设 $\rho_0$ 为基点选行 slack，$\rho_p$ 为主步预测 slack，保留一半预测改善：

$$
\rho_{\rm budget}=\rho_0-\frac12(\rho_0-\rho_p).
$$

**最终实现用同一真实 $y$ 的软、硬残差：**

$$
m(y)+J_m(x)w+\rho_{\rm budget}\ge0,
\qquad
h(y)+J_h(x)w\ge\frac14\max(h(x),0).
$$

这修正了前期设计 §3 只用 $m(x)+J_m(x)(p+w)$ 的软行写法。预算来源仍是主步预测，但修正 RHS 必须支付实际非线性度量弯曲。盒和帽高在 $y+w$ 用真仿射值；修正半径为主步实际归一化无穷范数的一半，目标是最小归一化 $L^1$ 修正。

报告分开保存 `corrected_actual_trial_linear_metric_slack` 和 `corrected_predicted_metric_slack`。前者检新 SOC 约束，后者仅用于基点线性模型下的抛物线记账，不能把它误称实际残差。每个原步最多一次 SOC，随后仍用原 $x+\alpha p+\alpha^2w$ 回退；任何接纳都重新完成两网全部真门和真实 $\eta$ 下降判断。

新的遗漏行先入池并退回最后接纳点重新线性化；不在池改变后继续使用旧 Jacobian 的修正。所有试探完整系数都保存，失败点不自动成为下一起点。

## 6. 预算、检查点和最终精化

主 LP、SOC、回退共同使用原 **12 LP / 40 次粗细完整值评价 / 120 秒优化活跃时间**。没有每阶段或每轮重置。两网初始化、初始导数预构建、19 输入准备耗时、优化活跃时间、最终独立审计和全过程壁时分别记录。

正常结束或异常/预算耗尽均保最后已接纳的两网态。最终另有明确记录的两次同参数 384/768 位置/曲率审计，不计成第二轮优化。冻结前后系数及完整 $g/b_0$ 逐位核同。native summary 文件为 `metric-budget-recovery-audit-summary.json`，主阶段键为 `metric_budget_recovery_stage`；通用 brief 处理必须保留此原生摘要。

摘要采用列名加行表，保所有 model/trial/correction/accepted 的索引与诊断；巨大 canonical 内容和全部精确系数保在完整 report。每次 checkpoint 均写摘要并绑定完整 report 字节 SHA。

## 7. 人工验证范围与真实入口

完整人工回执 `metric-budget-recovery-development-20261115.json` 已通过，耗时约 32.63 秒。混合粗细选行方向 Jacobian 最大误差 $1.39\times10^{-10}$；完整细曲率二 jet、旧 ID 迁移、缓存回滚、初态目标未过但旧门合格、硬曲率不可被更低 $\eta$ 绕过均覆盖。

曲边界 SOC 人工例故意令主步线性软残差为 0、真实 $y$ 软残差为 $-0.06$，预算为 0.05；最终新分支必须给出约 0.01 的修正，验证实际软残差被支付。小人工非线性族连续两次真实两网 $\eta$ 下降，注入 fine 异常仍保初态。

完整 19 输入人工 IO 覆盖错误 SHA、系数篡改、细坐标篡改、失败小 JSON、冻结同态和原池保持。既往人工报告链故意使用度量预算 100000；仅 `artificial + evaluate_only` 的 IO fixture 允许保留其宽预算，不能调用 LP，实际路径仍硬断言 $167/625\to13/50$ 和 $\Lambda=58$。没有伪造 Actions 环境或本地评价真实候选。

保守摘要压力例含 12 model、84 trial、12 correction、13 accepted，结果 87,185 字节，全部索引/值可还原，完整报告未删。正常人工 IO 摘要 50,735 字节。

开发命令为新 driver 的 `--check-only --out ...`。真实 19 输入和全部 decoded SHA 参数另存 `metric-budget-recovery-cli-20261115.json`；与旧 18 输入完全相同，仅追加第 19 报告和新输出名。所有研究入口均要求本仓库公开 Actions；本地人工通过不代表 $0.26$ 已恢复，更不构成连续等距、全曲面 reach 或嵌入认证。
