# R681 固定 SPD 的完整不等式 QP：独立 v4-PCG 接口

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

## 源码与执行状态

源码 [fullspace_feasible_active_pcg_v4.py](../scripts/resume_20261120/fullspace_feasible_active_pcg_v4.py)，32471 bytes，SHA256：

`dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b`。

它依赖已刊冻结 v3 `fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4`，默认同目录 `fullspace_feasible_active_cg_v3.py`，也可显式传 `v3_source`。加载时核实际字节。v3 文件未改；新 `Parameters` 的 AST 与 v3 相同。

本次只作源文本派生、逐块审读与标准库 AST 检查，未 import 或执行科学代码，没有 fixture、单位 J 探测、完整方向或预排。`solve` 仅允许本仓库公开 Actions。模块导入只定义接口，不加载或执行 v3 求解。它没有 full driver、预条件构造程序或非线性回溯。

## 完整原问题与可选入口

保持 [R677](../results/R677-low-damping-fixed-face-CG-and-reliable-updates.md) 的同一二次问题：

$$q(z)=\tfrac12\|Az+v\|^2+\tfrac{\mu^2}{2}\|z\|^2,\qquad Cz\le b,$$

$$g=A^T(Az+v)+\mu^2z,\qquad H=A^TA+\mu^2I.$$

A/v、mu、完整变量映射、原欧氏母范数、全部 C/b 均由调用者原样传入。预条件器只改变这个既定问题的线性求解方向；不把阻尼改成另一坐标的 identity。

接口保留全部原参数，新增三个可选参数：

```python
z, report = qp.solve(
    A, v, C, b,
    damping=actual_mu,
    parameters=parameters,
    block_columns=32768,
    callback=callback,
    preconditioner=fixed_spd.apply,
    preconditioner_metadata=fixed_spd.metadata(),
    v3_source=published_v3_path,
)
```

`preconditioner` 可为 callable 或具有 `.apply` 的对象。其矩阵、正尺度与父场依赖在一次 solve 中必须固定。`preconditioner=None` **直接调用字节绑定 v3 的原 solve，并返回其原报告**；没有重写或仿照一条“应该相同”的无预条件分支。配置 `atol=0` 等原有效参数继续透传。

启用分支复用 v3 的 `StreamedRows`、两遍欧氏行 QR、`ActiveFace`、全不等式线搜索、每 32 次真实线性残差刷新和末真实残差/梯度/Cz。停止仍由原欧氏 $\|Pg\|$ 与原容差判断，不以预条件残差较小替代它。

## 正确活动面度量与已付 Hd 更新

设 P 是当前原欧氏活动面投影，B 是本轮固定实线性 SPD apply。置

$$r=Pg,\qquad y=PBr=PBPg,\qquad e=r^Ty=r^TBr>0.$$

新的 PCG 链以 $d=-y$ 开始。它切于当前面，且 $g^Td=-e<0$。真实阻挡步长仍扫描完整 C/b；不把正余量不等式改成齐次切向条件。

当一步未被约束截断且面不变时，准确线最小化给 $g_+^Td=0$。用已经付过的 Hd 取

$$\beta_H=\frac{y_+^THd}{d^THd},\qquad d_+=-y_++\beta_Hd.$$

则 $d_+^THd=0$，并且

$$g_+^Td_+=-r_+^Ty_+=-e_+<0.$$

在固定 P/B/H、准确算术且从 $-PBPg$ 开始的 PCG 链中，$r_+^TBr=0$。由 $r_+-r=\alpha PHd$ 与 $d^THd=e/\alpha$，上式也就是通常的正确度量系数 $\beta_H=e_+/e$。源码使用前一种已付 Hd 公式，所以可靠梯度替换后仍直接控制相邻方向的共轭误差。没有声称所有历史方向的严格浮点共轭或有限步准确终止。

实际候选经过原两遍面投影后，下降门为

$$g_+^Td_+\le-.01\,e_+,$$

并保留实际严格负斜率检查。这里的参考是 $(Pg_+)^T(PBPg_+)$，不是 raw $\|Pg_+\|^2$。在 B 乘正常正比例 t 时，同一准确 PCG 链的 y、d、实际斜率与 e 同比例变化，这个比较保持相同尺度。有限精度下非正/非有限计算能量、坏斜率或不可用 B 都如实返回，不冒成全局 SPD 证明。

大替换误差、坏共轭系数、坏下降或活动面变化的重启继续逐项记录。达到内迭代预算或已到原欧氏投影梯度容差时，不为不会用到的下一方向额外调用 B；这不跳过下一轮仍适用的 R668 释放判别或最终真实诊断。

## R668 释放与尺度安全的零位移

R668 的单位向内下降率、原阈值及实际 $g\cdot w,c_i\cdot w,g\cdot d,c_i\cdot d$ 符号核对保留。释放后第一方向仍为原欧氏 $-P_{\mathrm{new}}g$，不能直接换成可能指向被释放行外侧的 $-P_{\mathrm{new}}BP_{\mathrm{new}}g$。

完成首个正长度真实可行步后，显式记录 `completed_euclidean_release_starter` 并从新点启动正确 PCG 链；不把一个任意欧氏起始方向冒作该 B 度量下的标准 PCG 初始方向。若首步前先遇零长度新阻挡行，欧氏 starter 策略保留至出现正长度推进。

原 v3 以 alpha 数值本身判断很小步。启用 B 的新分支明确用原坐标位移

$$\alpha_{\mathrm{block}}\|d\|\le10^{-15}$$

判数值零步，避免任意放大预条件方向被误作零位移。实现用 BLAS 的缩放平方和范数 `dnrm2`，再比较 $\alpha_{\mathrm{block}}\le10^{-15}/\|d\|$；不拿可能溢出的乘积作判据。非有限阻挡 alpha 不参加零步判定；仅报告用的乘积如溢出会标明并置空，不伪装成有限值。真正不可表示的方向范数返回明确数值失败。`None` 分支仍完整保留原 v3 判断。

## 与 R681 小模块的最小接线

调用者可在原实际 bridge/A 已构造后，用本轮同一 B/R/scale 构造 `CoarseFrame` 和当前 `Gc`，再构造

$$\mathcal B=\beta_{\mathrm{bg}}(I-WW^T)^2+WH_c^{-1}W^T.$$

首个明确可用的选择是

$$\beta_{\mathrm{bg}}=1/\mu^2,$$

即原 normalized-Phi 正则化地板的倒数；无需新增 J 乘积。这个参数属于固定预条件 apply，不替换原二次目标中的 mu 或步范数。v4 不自动选择或更新它。若日后采用已付 Rayleigh 倒数，也必须在新链/新 solve 前明确选择并记录，不能在既有 PCG 链中悄悄更换 B。

构造阶段 `SmallSPDUnavailable` 可由调用者明确退回 `preconditioner=None`，然后从原 v3 开始。构造接口/来源不符的 `ValueError` 不应冒作同一科学问题的正常数值回退。

运行中若 `.apply` 抛异常、返回错误形状/非实非有限值或算得非正预条件能量，v4 返回 `status=fixed_preconditioner_application_failed` 与当前真实截断 z，仍付末真实残差、梯度、全部 Cz 和释放诊断。它不在链中换 identity，不自动重试。外层如评价这一截断步，仍须通过原真实模型下降、Phi 和全部永久几何筛选；不能把它称为 QP 已收敛。外层若希望换 B，必须显式重新开始求解。

启用报告 schema 为 `fullspace-feasible-active-set-fixed-PCG-v4`。`fixed_preconditioner` 记录调用者来源/尺度、应用次数/耗时/失败、欧氏 starter 次数及最后实际能量；history 增加方向种类、正确度量能量、下降参考、零位移尺度和共轭误差。原欧氏末梯度、完整约束残差、真实模型目标及 A/A* 产品计数继续保留。

当前只有准备源和这些代数保证。PCG 可能减少线性未收敛余量，但不保证扩大真实几何允许步长；所有实际收益与额外成本仍须由后续公开 Actions 返回说明。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
