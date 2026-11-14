# 低阶显式投影：四个冻结点以内的局部量测计划

状态：**计划，未执行量测，未实现或替换 momentum engine。** 2026-11-09，`/root/tail_theory`，与 `/root/coupled_prefix` 讨论。原 continuation 的恢复计算由 root 单独持有，本计划不接入该活动进程。

前提是已审 `db6f-tail-quadratic-projection-equivalence.md`：显式 $q_2$、$B^L$、$UK$ 投影在理想等距角点的原有限 N 实数方程中严格等价。root 已全文独审，并精确重跑核查脚本得到相同输出。这里仅计划判断这个代数改写有没有可测的局部浮点评估收益，不把现有阻尼归因于舍入。

## 1. 最多四个输入点

1. 已闭 M15 的 $\lambda=1/16$ 失败 stage35 入口，其默认 `L=target` 通过原 guard。直接读取 `tail-m15-failed-stage-diagnostic.json.gz` 最后一案的 `firstFailure.state/geometry/target`，不用运行 RK 或新 root。
2. 同一输入的 `rootTrace.lastL`，即当时仍通过原 guard 的最后接受迭代。它不是 root，必须保持非解标签。
3. 同一 stage35 的已验证 base 成功控制输入。现有 positive-floor 报告只存 root 摘要，未保存其 L 系数，不能从摘要重建。若执行本计划，只重算这一个原 root，保存完整 `(Q,L,g)` 及原相对残差；不复做八组 lower-floor 扫描。
4. 一个完整 M14/N512 候选的保存端点作已解对照，例如 raw0/segment4 的既知低 A 端点。现存 margin 表也未存 L，因此需要一次原 root 调用；不扫描全部188端点，不运行整段 RK 或完整 DN。

前三项的原配置与旧控制 CP、五个失败 stage 输入都已有 hash 绑定，见 `tail-m15-first-rk-failures` 和 `tail-m15-positive-floor-probe`。第四项在实施前显式记录具体完整 CP、stage、source x 及 hash，不能只用“低 A 端点”这个描述选择任意输入。若只准备比较前两项，可直接取消后两项，不补入其它扫描点。

每点记录原 M/N/spacing、guard、源 hash 和精确保存的 binary 输入。必须保存原实际算出的 $p_j,P_{\theta,j},u_j$，避免把系数形成的舍入误差与最后角投影的舍入误差混成一个未定义参照。重建的点态数组应先与原 `evaluateL` 记录核对。

## 2. 三种评估及两个参照

在固定输入下比较三种只读评估：

- 原程序的 moment、B 与 split flux 累加。
- 保留原节点和三角表，仅按已证恒等式在每个点改写低阶部分后再累加；这分离点态代数改写的影响。
- 按系数公式投影 $q_2/B^L/UK$，其余项仍在原 N 个点求和。

第三种是独立公式对照器，不暴露新的 `root/rhs/rk4` 接口，也不把结果回写任何 worker。它不构成候选 engine 实现。

参照分两类，不能混称“原有限 N 的精确值”：

**固定 rounded 表参照。** 把原保存的 binary64 `cs/sn`、系数和标量当作精确实数，用高精度算术累加相同公式。它有意保留旧表的正交缺陷，主要量测算术累加和点态消去。

**理想等距表参照。** 以精确角点的高精度近似及真正 $\sqrt2$ 计算相同归一基，并显式说明固定了哪些系数、哪些关系重新按实数公式派生。它用于检查剥离公式的目标有限 N 模型，并显示 rounded 表相对这个模型的偏差。不能暗中把第一类的已舍入系数与第二类重新派生的系数逐项混用。

当前环境没有 mpmath/gmpy2，NumPy longdouble 只有63位显式尾数。若执行计划，可以用标准库 Decimal 的80位与120位重复值作高精度诊断，三角值由 Machin $\pi$ 与有限 Taylor 求得；两档一致性只能说明数值稳定性，不能冒充有向区间误差证。也可以先仅用 longdouble 作筛选，明确其参照精度限制。没有必要为这四点安装大型依赖。

## 3. 应输出的差量

每个合法点至少输出：

- 所有 moment 模、特别是最高四模的绝对差；同时保留参考值、原 `maxQuad` 和原 root scale，避免只给极小分母的相对百分比。
- B 的逐项最大差和绝对行和差界。它们是矩阵数值差，不直接等于 Newton 更新误差。
- $UK$ 与完整 nonlinear flux 各模差。只有原 `pref` 的全部输入均已绑定时，才另报乘上原 `pref*frequency` 后的物理 RHS 差。
- 两档参考精度之间的差、原 guard 余量、是否来自真正 root、是否来自未收敛迭代。

`rows.quad`、`maxQuad`、原 guard、原目标残差及所有原源文件都保持不变。比较器可保留原完整 pointwise q 以核查，不得用余项替代这个字段。

## 4. 解释和停止范围

如果只有舍入级差而没有可辨的参照精度改善，就保留该负结论，不启动第二条完整求解路线。即使高模差显著下降，也只证明这些固定点上的局部评估更接近所定义参照；仍不能解释原 global shooting 停滞，更不能声称整尾可解、metric 下降或 G5 已完成。

任何后续真正 engine 派生都需要另行冻结 source imports、保持原方程与 guard，并核 state-only/variational 路径和完整原残差。这一步当前未实施。本计划最多形成小输入包、只读差量表和解释记录；不启动新全尾、ODE、BVP、Jacobian扫描或最终 XYZ 导出。
