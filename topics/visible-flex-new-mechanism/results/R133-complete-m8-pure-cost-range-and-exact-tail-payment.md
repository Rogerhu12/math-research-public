# R133：完整 m=8 pure 成本像恰为三十一维响应，整个幂尾周期可准确支付

日期：2026-11-14。**公开实际与完整纸面提升均已完成。** 全部原导数成本在真实水平分部积分后，1009 个完整正规系数都属于此前的 pure 响应像，商余项全部为零。结合 R124 与 R130，准确得到

$$
\boxed{\Pi_8(\mathcal U_4)=\Pi_8(\mathcal R_8)=\mathcal T,\qquad
\dim\mathcal T=31.}
\tag{1}
$$

偶总次数像维数准确为 15。R132 的实际新商上界七在本次收紧为**零**。这并不说明完整两模式商为零；R118、R126、R128 已证明的完整非零方向继续成立。

## 1. 完整输入与本次唯一新增操作

采用 [R132](R132-complete-pure-derivative-costs-and-finite-tail-quotient-bound.md) 已发表的整个

$$
\widetilde L^{[2]}=v^{[2]}-\mathcal B_{m^{[0]}}N^{[2]}
-\mathcal B_{m^{[2]}}N^{[0]}+\Delta L^{[2]},
$$

$$
L^{[4]}=v^{[4]}-\mathcal B_{m^{[2]}}N^{[2]}.
\tag{2}
$$

原 $N^{[2]}$ 未删除；$\Delta L^{[2]}$ 是 R124 的全部矩阵诱导修正。完整原 $N$ 与旧静态代表的差已按真实 $W$ 响应支付，只改变 $\mathcal R_8$。原式始终先做实际 $s$ 微分和 history ODE 代入，再将累计 history 的值置零。

本轮不再运行任何 profile 原式、幂尾代入、原响应公式或旧 forcing。只读取已发表的完整三元 packet

$$
(P,A,R),\qquad P=\sum_{j\in J_{31}}A_jP_j+R,
$$

对其三个分量作完全相同的几何线性操作。三阶几何坐标全部保留。共同右锚仍为 $c$，$r=c-\xi$；$c,\xi$ 不随真实 $s$ 改变。

## 2. 真实水平正规式与完整边界势

记

$$
u=h_s,\quad w=k_s,\quad a=h_{ss},\quad b=k_{ss},\qquad
\omega_s=\frac{w}{2h},
$$

$$
X=\partial_h,\qquad Y=\partial_k+\frac1{2h}\partial_\omega.
$$

按 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 的已证原式，实际得到

$$
\Pi_8\widetilde L^{[2]}=D_sP_1+\widehat Q_2,
\tag{3}
$$

$$
\Pi_8 L^{[4]}=D_sP_3+
\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2
+(H_1u+H_2w)(ub-wa)+\widehat Q_4.
\tag{4}
$$

所有系数是完整 pure 多项式。$\widehat Q_2$、$\widehat Q_4$ 分别是速度二次、四次式；$P_1,P_3$ 为明确的正导数权边界势。$D_s$ 对 $h$ 的 Laurent/log 项、$k$ 和 $\omega$ 都保留全部真实链式导数，不能将 $\omega$ 冻结。

实际证书保存了 $P_1$ 的 244 个 packet 与 $P_3$ 的 560 个 packet，并分别保存 $P_3$ 的三阶项消元势和速度三次势。对完整 $P,A,R$ 三个分量，都准确核对了 (3)–(4) 的原多项式差为零。

式 (4) 中两个非对称速度—加速度项没有被当成全导数删掉。程序从 $b$ 的系数读取 $uH$，同时核对 $a$ 的系数为 $-wH$，再保留整个 $H(ub-wa)$。所有由势的状态导数产生的速度四次项也保留在 $\widehat Q_4$。

## 3. 正规系数的准确成员结论

所有几何键仍按

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss})
$$

保存；正规式最高 jet 阶实际为二。三阶项被显式边界势支付，而非预先截掉。

| 完整正规部分 | 非零完整原多项式 packet | 非零商余项 packet | 商秩 | 偶商秩 |
|---|---:|---:|---:|---:|
| $\widehat Q_2$ | 519 | 0 | **0** | **0** |
| 加速度二次部分 | 148 | 0 | **0** | **0** |
| 完整面积型部分 $H(ub-wa)$ | 168 | 0 | **0** | **0** |
| $\widehat Q_4$ | 174 | 0 | **0** | **0** |
| 完整权四正规式 | 490 | 0 | **0** | **0** |
| 完整权二、四正规式 | **1009** | **0** | **0** | **0** |

未分 profile 权与逐真权的商秩均为零。每一个原多项式仍通过 R116 的 31 个原响应基列准确重构。这里的结论是完整正规系数**属于 $\mathcal T$**；它们本身并非都为零。全正规式仍有 1009 个非零原多项式、4387 个非零单项系数。

完整原多项式支持在 45 个 $(c,r)$ 单项位置上，实际

$$
\min b=25,\qquad \max(a+b)=33.
$$

其中权二正规式为 45 个不同单项、3148 个非零单项系数；权四正规式为 36 个不同单项、1239 个非零单项系数，最高总次数为 32。

程序对原完整多项式、原响应部分和原余项分别报告全部 $r<25$ 行。三者的低尾幂系数都准确为零。这个语义输出没有控制删项，也没有作为失败门；真实结果与 R85/R88 的端点势及 R130 的真实 span 结论一致。

## 4. 任意真实零矩路径的整个 pure 幂尾都属于响应像

[R124](R124-zero-matrix-static-tail-payment-and-remaining-derivative-costs.md) 已证明完整归一化静态 pure 密度逐系数属于 $\mathcal T$。本次再证明 (3)–(4) 的全部正规系数属于同一固定 $\mathcal T$。

取任意真实有限路径 B，满足 $h>0$、真实水平关系、共同右锚、首末常值 scalar germs，以及完整矩阵 $M_B=0$。两端的 $u,w,a,b$ 分别为零，故本稿明确的 $P_1,P_3$ 的各个端值均为零。于是 R124 与 (3)–(4) 给

$$
\boxed{\Pi_8V_B\in\mathcal T.}
\tag{5}
$$

这允许固定开 scalar 端口，也不先要求 $T_B=0$ 或末 frame 为 I；矩阵与局部化条件才是 (5) 所用的真实假设。端口不是常值 germs 时，必须加回 (3)–(4) 的完整势端差。

式 (5) 没有删除 R109 的权零局部势 $P_h+F_*$，也不删除 B 的未知第四基准成本。它使用的是 R109 已付的真实零矩局部化和 R124 完整 $m_0+m_2$ 规范化。

## 5. 从全部正规系数到准确真实成本像

[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) 已证明，在有限真实函数环境中

$$
\mathcal U_4=\mathcal R_8+K,
$$

其中 K 是完整八矩归一化后的十四类水平状态系数值的真实 span。静态一类由 R124 支付；余下三类速度二次、三类加速度二次、两类面积型和五类速度四次均由本次 (3)–(4) 支付。因此

$$
\Pi_8(\mathcal U_4)\subseteq\mathcal T.
$$

反向包含来自 R105 已证的 $\mathcal R_8\subseteq\mathcal U_4$，故得到 (1)，以及

$$
\boxed{
\dim\bigl(\Pi_8(\mathcal U_4)/\Pi_8(\mathcal R_8)\bigr)=0,
\qquad
\dim\Pi_{\rm even}\Pi_8(\mathcal U_4)=15.
}
\tag{6}
$$

这不是仅将一个特定几何路径代入后得到零，也不是将未付的几何系数假设独立。原式成员证书与 R130 的真实双向 span 定理共同给出完整结论。

完整商的含义仍需区分：本次证明诱导的商映射

$$
\mathcal U_4/\mathcal R_8\longrightarrow
\Pi_8(\mathcal U_4)/\Pi_8(\mathcal R_8)
$$

是零映射；并非每个完整成本的原 $\Pi_8$ 多项式都为零。R123 曾只对 G 给出这种现象；现已对整个 canonical 第四成本空间证明。因而再用同一个 $m=8$ pure 尾不能发现完整新商方向。

## 6. 既有真实四块直接升级为整个 pure 幂尾为零

使用 R116 §6–7 已经固定的 15 个实际尾系数查询 $Q_{\rm tail}$：总次数 26、28、30 的全部 12 行，加上次数 32 的三个固定满秩行，其中包括 $c^7r^{25}$。该查询在

$$
\mathsf F(\mathcal T),\qquad
\mathsf F(P)=2\{P(c,r)+P(-c,-r)\},
$$

上是同构。这里使用的是该文已经指定的尾系数查询。

R116 的同一个实际设计为

$$
\mathcal C=B\,\sigma B\,B^R\,(\sigma B)^R,
\qquad B=ZJ,
$$

其中 J 是固定未知成本的真实零矩 $I\to D$ 基准，Z 是 R101–R102 保全部基准的有限控制词。全部连接成本、prototype 成本、$V_J,T_J$、空间位移和长度均已保留；共同正物理区间在紧控制族上先固定，再选有限复制次数。R116 已证明

$$
M_{\mathcal C}=T_{\mathcal C}=0,\qquad
Q_{\rm tail}\bigl(\Pi_8V_{\mathcal C}\bigr)=0.
$$

它的 scalar 常值 germ 是反射不动的 $(h_0,0,0)$。R104 的真实前缀 frame 为 $I,D,I,D$，其中 $D=\operatorname{diag}(-1,1,-1)$。若 B 的本地位移为 $\Delta$，令 $A=\operatorname{diag}(1,-1,-1)$，四块的全局位移是 $\Delta,DA\Delta,-\Delta,-DA\Delta$，准确相消；末 frame 为 I。因此 $V_{\mathcal C}$ 本身属于 R105 的真实 $\mathcal U_4$。

过去尚未知道未知基准的尾像归属，所以 15 个查询为零不足以推出整个尾为零。现在 (1) 给

$$
\Pi_8V_{\mathcal C}\in\mathcal T.
$$

R106 的完整四块奇偶律又给它只有偶总次数，故

$$
\Pi_8V_{\mathcal C}\in\mathcal T\cap\{\text{偶总次数}}
=\mathsf F(\mathcal T).
$$

在这个准确的 15 维空间上，已付的 $Q_{\rm tail}$ 为同构。因此同一个既有有限实际设计立即满足

$$
\boxed{\Pi_8V_{\mathcal C}(c,r)\equiv0.}
\tag{7}
$$

式 (7) 同时消去全部 $c,r$ 系数，强于此前只支付 D25 和另外 11 个指定系数；不需要新的 Brouwer 求根、profile 计算或另选几何。它也不是由几个系数零猜测全函数，而是由本次完整像等式和已证有限查询同构推出。

这个升级仍只处理既有闭浸入数据的 $m=8$ pure 尾测试。它不将该设计称为完整第四成本已零或已完成闭嵌入等距弯曲。

## 7. 实际来源、完整证书与资源

公开 run 为 [43653293263](https://github.com/Rogerhu12/math-research-public/actions/runs/43653293263)，source `2f0add61f44365d713abf836beaa8b0be2806a3d`，lane `derivative_m8_geometry_ibp`。冻结驱动 [literature_derivative_m8_geometry_ibp.py](../scripts/literature_derivative_m8_geometry_ibp.py) 为 21856 bytes，SHA-256 `2347633b50858f19e8cb5afa2956dabbcd172b669016f0ac2a390a0e6ee2b46c`。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| [小主报告](../notes/actions-43653293263-1-derivative_m8_geometry_ibp/geometry-ibp.json) | 15625 | `3711ccefbc761f0ad5a480fbd344e2020fe83275317d690fa25179c20fc072c6` |
| [公开人工检查](../notes/actions-43653293263-1-derivative_m8_geometry_ibp/geometry-ibp-development.json) | 5326 | `b38eec3a67d8df535a6259e053b5995512b4f3a85ce0a8a92d5bc622f6d37875` |
| [完整证书](../notes/actions-43653293263-1-derivative_m8_geometry_ibp/geometry-ibp-certificate.json.gz) | 483512 | `a62173b39804ab7f3b0c1f14a23f840a81813717bb8ce88d7659c0e64e90e2f1` |
| [终端发布回执](../notes/actions-43653293263-1-derivative_m8_geometry_ibp/receipt.json) | 33991 | `28ecf52779aca20b1d064f26b590546205ae0fcd3074aa41a3dcdfdbc8b389d8` |

完整证书原文 4472950 bytes，SHA-256 `3e0b01e2d7e3ed6634420524ea99ab8d4a9a56c280dd9a2da35365dca02067c7`。全部完整几何系数、响应重构、边界势、低尾支撑与准确零余项均保存于其中，大数据没有读入对话。

六项公开人工检查全部通过，0.003315813 秒。实际新消费耗时 **1.612911694 秒**，峰值 RSS **83.125 MiB**，285300 次线性操作；profile 公式评价、响应公式评价和多项式研究代入次数均为零。主报告 completion 为 complete。

## 8. 现在真正未付的范围

本次完整支付的是单一 $m=8$ pure 幂尾投影。对任意光滑 profile 的通用 pure 算子成员关系，需要回到原表达式证明；不能由 (1) 自动推广，也不应盲跑另一个幂指数代替这个证明。

完整 $-2$ mixed 模式、完整第四算子商、正成本锥、第四逐 $s$ ruling、双 collar、更高阶与收敛仍未支付。闭嵌入、reach 和宏观运动要求也没有因此完成。后续将利用已保存的完整原因子研究通用原式，而不再重复本次已完成的 $m=8$ 查询。
