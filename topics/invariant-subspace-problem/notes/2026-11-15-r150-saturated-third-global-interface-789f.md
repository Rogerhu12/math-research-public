# R150：实际第三页正解的六槽全局原式恢复入口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。状态：连续执行入口，尚未运行本次全局数学。已完成的局部第三页来自 run 43664532571；本次只有九个原十七式乘回全部通过才能标记完成。

## 1. 数学对象与有限费用

采用原 6188 来源、4367 输出、十七式矩阵 $A$，固定目标 $31^2h_0T_j$，$j=2,\ldots,10$，模数为 $31^6=887503681$。绝不将该有限模身份解释成特征零结论。

实际局部正解只用 $L_{5,20011}+16L_{5,20012}$，九目标倍数为 $(1,28,16,11,7,7,4,1,11)$。其第二父来源仅 $\omega_3,\ldots,\omega_8$，实际整数系数为 $(344,409,327,102,1,16)$。入口重新逐项核实际 prepared/complete 矩阵以及全部 315 坐标；不是仅读取成功布尔值。

六个辅助槽为四条完整第二像的原 $p^4$ 来源、该主第三来源及一条真实 $D_2$ 的原 $p^3$ 来源。它们共享原高核 $K_2,\ldots,K_8$ 的七条 raw 全局 $q_1$。辅助槽编号与物理目标不同，最后九个物理目标始终单独核对。

固定实际整数投影 $P$ 的次数为 196。费用链为

$$
177\longrightarrow373\longrightarrow469\longrightarrow665
\longrightarrow761\longrightarrow957\longrightarrow1053
\longrightarrow1249\longrightarrow1345.
$$

其中全局 $H_D$ 费用不超过 665，四条全局 $H_W$ 不超过 957。完整证明见 results/R150-appendix-actual-third-constant-solution-six-slot-global-cost1345.md 和第三来源比较定理。

## 2. 运行命令、输入及界

主脚本为 2026-11-15-r150-saturated-third-global-runner-789f.py：

~~~sh
python -B 2026-11-15-r150-saturated-third-global-runner-789f.py \
  --notes-root NOTES \
  --t96-recovery T96 --all198-recovery ALL198 \
  --seven-recovery SEVEN --current-recovery CURRENT \
  --ninth-recovery NINTH --old200-recovery OLD200 \
  --second-recovery SECOND --third-recovery THIRD \
  --out OUTPUT --math-seconds 1200 --memory-mib 1024 --compile-seconds 30
~~~

精确合同固定 49 个实际输入，总原字节数 533394601，来源为 8 份既有 recovery artifact 加 notes 的模型和 torsion 状态。第二页只读取已成 prepared receipt 和 20-jet 原 $q_1$；第三页只读取两份 prepared/complete receipt 及其小矩阵。所有原来源、NF、G quotient、余量及常预基 trace 都按原 SHA256 和实际字节数校验。旧局部页、旧 197/204/208 列均不重算。

五个 C++17 helper 各有独立 30 秒编译上限；编译与既有输入恢复完成后开始唯一 1200 秒数学时钟。每个子进程地址空间限 1024 MiB。原来源和完整原输出数组可同时存在，因而本次明确增加了内存界，未继承前序 512 MiB 边缘配置。

Python 依赖为 NumPy 2.2.6、python-flint 0.9.0。所有 Python 使用 -B。冻结时三个新 Python 文件已实际 AST 解析；最终 1345 界的五份 native 源尚未执行编译，真实编译结果由 Actions 回执记录。较早 1058 界的编译不能冒充本次编译或数学运行。

## 3. raw 全局截面及整数 carry

新的七条 $q_1$ 是全局多项式来源；既有 20-jet 数组只作为已经付清的相同截面依据。source helper 提供显式 raw 模式：沿真实 T96 图列直接做 VQ，并完整验证

$$
R C+\operatorname{rem}=\operatorname{RHS}.
$$

它不运行 1174 个核方向的标准化，不声称来源费用最小。后面的 $q_2,q_3,q_4,w$ 同样可以用 raw 截面；本次所有费用只用已证 $N+96$，完全不依赖标准化。

carry helper 读取全部原 6188 行、完整旧 K200 字典、197 个 paid 目标的 padding 和 canonical field 数据，再把新 raw 七条 $s$ 多项式在 $t=s-2$ 处求 20 项模 961 展开。必须逐坐标核

$$
q_{1,s}=q_{1,t}+31c\pmod {961}.
$$

差商 $c\bmod31$ 的全部 $6188\times20\times7$ 系数存为 q1-s-to-t-carry.bin。若 field 层不一致，记录首个原行、Taylor 次数和两个来源标签后失败；不能用 Bockstein 像抵消这个实现失配。

这明确要求局部 $q_2$ 同步改为 $q_2-c$，whole-source 投影后为 $q_2-Pc$。所保存的 $c\bmod31$ 足以核初始来源运输；更高的整数 carry 不用该 field 文件代替，而由后续每一步原 $p^6$ 来源乘积实际保留。

## 4. 连续数学步骤

1. 从实际 prepared 矩阵合成六槽 $F_0$，保父来源的未约整数常系数。整条乘 $P$ 后，核原 $p^2$ 整除、真实 G 像以及完整原来源 $q_2$，形成六槽 $L_3$。
2. 整条乘第二个 $P$。保存第六槽真实 $H_D$ 的原 $p^3$ 见证；前五槽在完整 315 维中必须落 $U_7$。付真实七来源后恢复 $q_3$，形成原 $p^4$ 来源。
3. 整条乘第三个 $P$。保存前四槽实际 $H_{W,a}$，核它们模 $U_9$ 后准确等于完整第二像基。主槽在真实基 $(U_7,b_8,AH_D/p^3)$ 上纠偏，恢复 $q_4$ 后形成原 $p^5$ 来源。
4. 整条乘第四个 $P$。对完整九个原余量解 $U_9+\langle AH_{W,a}/p^4\rangle$ 的真实常数纠偏，恢复最终原 $A$ 像，再对全部九目标做原十七式模 $p^6$ 乘回。

中间 $p^4$ 位只允许 $p\kappa_8$ 和 $pH_D$ 纠第一像；不能替换为未缩放的 $\kappa_9$。最终 $p^5$ 位才使用已证明合法的 $p\kappa_9$。每次全局成员判据保全部 505 个自由观察和完整 315 维 torsion；不能仅验证根 2 的局部坐标。

原 NF 使用真实 3333 常预基，所输出 forward/backward DAG 必须逐 SHA 等于既有源。wide NF 为 R150NX31，wide trace 为 R150NW31，均使用 u16 参数指数或长度。真实 NF/G/image/来源和原式身份层次分开保存。

## 5. 完成、失败与恢复

主回执为 saturated-third-global-pipeline-receipt.json。唯一成功 outcome 为 all-nine-original-p6-complete，必须同时满足：

- status=completed；
- fullOriginalAllNineMod887503681IdentityVerified=true；
- allNineOriginalSeventeenIdentitiesVerified=true；
- allSixAuxiliaryOriginalIdentitiesVerified=true；
- full315FinalReconciliationVerified=true；
- sameQ1IntegerCarryVerified=true；
- finitePositiveSourceBudgetsVerified=true 和 finite_budget_verified=true；
- completedOriginalTargetLabels=[2,3,4,5,6,7,8,9,10]；
- 全部实际最终来源费用从真实原乘积回执读取，并且不超过 1345。

既有局部 individualTargetCompatible=[true,...,true] 不构成本次全局完成。任意失败或时钟到达均为 failed-or-incomplete，保具体阶段、原日志和实际数组，不填补缺失恒等式。

通过 --resume-recovery SAVED 复用完成阶段和真实 native 检查点；可再传 --resume-results SAVED_RESULTS 复用已封存证书字节。绑定只使用输入字节、代码/header SHA 和规范来源多项式，不使用恢复目录路径。VQ 保完整 partial 来源数组及 next-row；wide 原运输保 raw/beta 双槽；原乘回保完整 product 数组与原源输出前缀。恢复不会重算已完成阶段。

全部实际 recovery 文件和 stage-cache 无损保存。大流采用 gzip level 1，分片每份不超过 4500000 B，清单保原完整 SHA、压缩完整 SHA 和全部分片 SHA。封存时间单独记录，不挤占数学时钟；局部检查点绝不标为全局证书。

## 执行预算接续记录

首轮及首续已保存真实检查点；后续共享数学时钟由 300 秒提高至 1200 秒，以连续完成已有 VQ 数组的完整原来源核验。五个 native、矩阵、carry 及 runner 的数学源码字节不变，输入 SHA、源多项式、模式和 header 绑定全部保持，因此旧完整 cache 及 partial 可继续复用。编译仍各 30 秒，子进程仍 1024 MiB；外层数学步骤 40 分钟、job 90 分钟，低于根 README 的 6 小时上限。提高的是后续执行预算，不补记任何尚未完成的恒等式。
