# R99：真实第四切向越过 P1 字符核的准确证书

日期：2026-11-14。**已证明。** 消费公开 Actions run **43640085842**、来源提交 **bccbbe27c8c105666b2d2438b9d1d48812e3ce55**、lane **fourth_character_transverse**。没有重新运行旧列空间、旧目标或旧秩测试。

## 1. 结论与范围

[R98](R98-weight-zero-separation-of-all-positive-state-P1.md) 的正字符只消去 reciprocal 七维二阶空间产生的 P1 响应。本次取 [R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md) 实际允许的第八个二阶方向

$$P=\Phi_{t_1}.$$

记完整相位第四切向为

$$\begin{aligned}
\mathcal B_P(T)(F,\phi)
={}&2T(PD;D)-4T(\phi;\phi,PD)\\
&+4P(\phi,T(\phi;D)),\qquad D=F-\phi^2.
\end{aligned}\tag{1}$$

将 R98 的查询公式明确扩展为 $\widetilde\Lambda$ 后，实际原式证书证明

$$\boxed{\begin{aligned}
\widetilde\Lambda\bigl(\mathcal B_{\Phi_{t_1}}(\tau_{p_1,t_1})\bigr)&\ne0,\\
\widetilde\Lambda\bigl(\mathcal B_{\Phi_{t_1}}(T_k^{\rm shape})\bigr)&\ne0.
\end{aligned}}\tag{2}$$

两个方向都由已证明的真实第三控制及 R83 的 $M=T=0$ 第四族实现。它们不属于原 P1 响应空间 $\mathcal R_*$；这里只证明各自越过同一个字符核，没有声称两方向在商空间中独立。

本稿**不**从非零模数读取实数符号，不声称已有负第四基准或完整 $P_0+NP_1$ 相消，也没有构造某个已经施加三矩的具体 $C^\infty$ 圆。实际合法圆、共同物理区间以及有限复制如何处理基准成本，需要另行支付。第四 ruling、所有更高阶、有限等距族、闭面嵌入、reach 和宏观幅度仍未完成。

## 2. 不能暗中扩大 R98 的泛函定义域

沿用 R98 的 14 个保留权零原列，以及 14 个 pivot 查询。令其准确有理矩阵为 $A$，额外查询对应的原列行为 $a$。定义

$$\lambda_0(X)=\operatorname{ev}_{23}(X)
-aA^{-1}\operatorname{ev}_{\rm pivot}(X),\qquad
\kappa=\lambda_0(b_0)\ne0.\tag{3}$$

这里 $A$、$a$、$b_0$ 均保持原证书的真实有理定义。对可评价的有限权表达式，另定义

$$\boxed{\widetilde\Lambda(X)=\lambda_0(\Pi_0X)/\kappa.}\tag{4}$$

(4) 在 R98 原空间

$$V=\mathcal R_*+\operatorname{span}\{b_{H,d}\}$$

上与原 $\Lambda$ 一致。本次没有预设新的第四列属于 $V$。每个新列从原式核为权零，因此其 (4) 直接使用原来 15 个查询。

所有实数系数以有理 Cramer 式 (3) 定义。打印的模 $p$ 系数只是这些系数的约化，不能当作有理或实系数本身。

## 3. 完整相位 Jacobi 支付两个零方向

令

$$\tau_{Q,R}(a;b,c)=Q(a,R(b,c))-R(a,Q(b,c)).$$

对任意三个对称双线性算子 $P,Q,R$，(1) 给

$$\boxed{
\mathcal B_P(\tau_{Q,R})+
\mathcal B_Q(\tau_{R,P})+
\mathcal B_R(\tau_{P,Q})=0.}\tag{5}$$

完整证明可直接分两组。含 $D^2$ 的项为

$$2\sum_{\rm cyc}\{Q(PD,RD)-R(PD,QD)\},$$

按双线性对称性两两相消。其余项为

$$-4\sum_{\rm cyc}
\{Q(\phi,R(\phi,PD))-R(\phi,Q(\phi,PD))\}$$

和

$$4\sum_{\rm cyc}P(\phi,Q(\phi,RD)-R(\phi,QD)),$$

循环重排后相消。因此 (5) 对整个目标 $F$ 和相位 $\phi$ 成立，不只在纯对角或单一 Fourier 模式上成立；也没有假设算子结合。

按 R98 权零表的列号，

$$\begin{aligned}
\mathcal B_{t_1}(\tau_{p_0,p_2})&=C_9-C_1,\\
\mathcal B_{t_1}(\tau_{p_2,s_1})&=C_3-C_{13}.
\end{aligned}\tag{6}$$

所以这两列准确属于 $\mathcal R_*$，且其 $\widetilde\Lambda$ 值准确为零。实际模零与纸面定理相符；这里没有用“模零”单独推“有理零”。

## 4. 固定原式、固定 profile、固定查询

本次四个第三模板依次为

$$\tau_{p_0,p_2},\quad \tau_{p_1,t_1},
\quad\tau_{p_2,s_1},\quad T_k^{\rm shape}.$$

它们是完整第三空间 $W_0$ 的四个旧原模板，对应 v2 原序号 1、12、16、109。前三个直接由已冻结 $\Phi_8$ 原式恢复；最后一个从完整 colored local third root 及其 R73/R79 分解提取。四模板的旧 SHA 全部逐一匹配，内槽对称和权零均检查通过。没有换方向、改归一或仅保留对角表达式。

每列都代入完整 (1)，两个实际模式是 $-4,-2$。全部查询使用同一实有理 pair：

$$f(t)=[t(1-t)]^8,\qquad
g(t)=f(t)(1+2t+3t^2+5t^3),\quad t=\xi-2\in[0,1].\tag{7}$$

它的支撑为 $[2,3]$，零延拓是 $C^7$。本次没有给 (7) 施加三矩圆条件。所有原语都是相同右 collar 的真实积分；在支撑内等价于以 $\xi=3$ 为右端，未用 word 正规形代替数值。

15 个查询与 R98 完全相同：在 $t=j/49$ 取对应模式的实部或虚部，pivot 行为

$$0,1,2,3,4,6,7,10,11,14,15,18,19,22,$$

额外行为 23。第 23 行为 $t=6/49$、$\xi=104/49$ 的 $-2$ 模式虚部。原报告保存每列的全部 15 个值及模式 polynomial hash。

## 5. 公开实际非零证书

使用素数

$$p=2147483647,\qquad \kappa\bmod p=2115674793.$$

消费的 R98 旧 15×15 模增广矩阵再次核对了泛函消 14 列、非零 $\kappa$ 和 Schur 行列式关系；没有重新评价旧 14 列、旧目标或重新做其秩测试。

| 新列 | 第三方向 | $\lambda_0\bmod p$ | $\widetilde\Lambda\bmod p$ | 准确解释 |
|---:|---|---:|---:|---|
| 0 | $\tau_{p_0,p_2}$ | 0 | 0 | (6) 已证明准确零 |
| 1 | $\tau_{p_1,t_1}$ | 79250643 | 2054146430 | 准确有理值非零 |
| 2 | $\tau_{p_2,s_1}$ | 0 | 0 | (6) 已证明准确零 |
| 3 | $T_k^{\rm shape}$ | 1427607783 | 721224600 | 准确有理值非零 |

本次原式 polynomial 评价遇到的 76 个有理分母恰为整数 1 至 76，全部在模 $p$ 下可逆；查询分母 49 也在其中。分母列表 SHA 为

**5cc48736335777482252a7c768f1dec012fa1e89fe72c28d48269c1085baa000**。

最高 polynomial 次数为 76，原式 atom 评价 2310 个、monomial 评价 4140 个，操作检查 16177 次。因此两个非零约化确实来自已定义的准确有理数，推出 (2)。

由于这四列都是权零，且 $\widetilde\Lambda$ 消全部真实 $\mathcal R_*$，(2) 还直接推出两列各自不在 $\mathcal R_*$。本结论不依赖 word 正规化的完备性，也没有把一个未约简余项作为非成员证据。

## 6. 来源、字节与执行范围

实际文件为 [fourth-character-transverse-probe.json](../notes/actions-43640085842-1-fourth_character_transverse/fourth-character-transverse-probe.json)，原始/存储长度同为 **15296 B**，SHA256 为

**98aad6ca4167ea4f8efcebdded508732263d0435f8517bcf4aa814404e105020**。

[receipt.json](../notes/actions-43640085842-1-fourth_character_transverse/receipt.json) 的来源提交、run、lane、输出长度和 SHA 均匹配。十个直接数学依赖的当前字节/SHA 与实际报告全部相同；receipt 另列 135 个来源文件，此处不把其列出冒称对所有来源逐个作了独立数学审查。仅从已存的 15 行重新核对四个 Cramer 线性组合及归一关系，全部相符；没有本地重算任何研究 profile 或几何。

主源码 [literature_fourth_character_transverse_probe.py](../scripts/literature_fourth_character_transverse_probe.py) 为 18310 B，SHA256：

**84a8ea232536263af398f781b5647ab540e06e21e9c2a83005d4cee2708451c3**。

消费的旧权零报告为 56173 B，SHA256：

**1146e6789d2f842ecc255930e2394bec5073029b13dcff4cc6f1aa445d07a78d**。

运行状态 **complete**，用时 **2.405658037 秒**，RSS 峰值 **35.6640625 MiB**。新编译只包含恢复所需的 colored local third root，9625 个 coefficient nodes、180 个 profile atoms、3941 个 geometry expansion nodes；没有编译旧常态第四目标。资源预算没有触发。

## 7. 真实控制意义与仍需保留的成本

R83 构造的真 $M=T=0$ 路径族满足

$$V_{Z(t,\lambda)}
=E(t)+2\{V_{L(\lambda)}-V_{L(0)}\}
+\lambda t\,\mathcal B_P(T),\qquad E(-t)=E(t).\tag{8}$$

本次 (2) 因而给出了完整 operator 层非零第四切向。在已经含有 $Z(0,\lambda)$ 的真实基准中替换该块，并使用同一新单 P 的四块组装，第四常项变化为

$$\Delta P_0=4\{E(t)-E(0)+\lambda t\,\mathcal B_P(T)\}.\tag{9}$$

同时二阶矩阵、完整第三算子和已有 $P_1$ 保持不变。这正是尚未由 R98 排除的有限 $N$ 方向。

但本稿保留实际基准

$$4V_{A(0)}+2V_{L(\lambda)}+2V_{L(0)}$$

以及 (9) 的偶次部分。非零切向不能单独证明整个成本可以取负或完整函数能够归零。也不能把第四倒行同号的成本当成可自由相减。

下一步应先在真实有限拼接及同一物理区间中研究基准和复制，而非继续扩大已被 R98 完整排除的正长度 P1 状态空间。本稿的非零证书可作为该后续推导的确定输入；它本身不提前支付后续结论。
