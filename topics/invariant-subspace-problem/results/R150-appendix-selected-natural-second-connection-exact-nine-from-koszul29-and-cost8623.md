# 同一所选无穷远方阵：完整第二连接秩恰为 9、24 维头空间与条件来源费 8623

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。状态：实际原来源配对完成；以下余维上界是对其完整实算结果的新代数推论。

## 1. 结论与同一原对象

固定原十七式的自然加权无穷远矩阵
$$
A(u)=A_0+uA_1+u^2A_2+\cdots,\qquad B(u)=A(u)_{I,J},
$$
其中 $I,J$ 均有 $4354$ 个元素，原局部参数为 $u=1/s$。本结论保留相同原单项式顺序、原方程常数比例、来源集合和输出集合，不以共动矩阵代替自然矩阵。

[完整一阶正式结果](R150-appendix-selected-natural-first-connection-exact-rank-three.md)已付
$$
\operatorname{rank}_{\mathbb Q}B_0
=\operatorname{rank}_{\mathbb F_{31}}\overline B_0=4318,
\qquad
\operatorname{rank}_{\mathbb Q}\beta_1
=\operatorname{rank}_{\mathbb F_{31}}\overline\beta_1=3.
\tag{1.1}
$$
此前[真实 22 个第二头](R150-appendix-selected-natural-second-left-twenty-two-heads-and-rank-interval.md)给出了 $9\le\operatorname{rank}_{\mathbb Q}\beta_2\le11$。

本文利用实际的 $29$ 维原来源核配对，证明
$$
\boxed{\operatorname{rank}_{\mathbb Q}\beta_2=9,\qquad
\dim_{\mathbb Q}L_2=24.}
\tag{1.2}
$$
$L_2$ 是能够延成完整原二阶左 jet 的常项头空间。已有 $22$ 个显式原二阶 jet 保持有效；本文证明还存在两个独立方向，但**没有构造这两个新方向的完整显式来源**。

同一原非零最大子式 $D$ 的 Q 无穷远阶因而至少为 $93$，其全部 cofactor 及换入任意原来源列的子式至少为 $90$ 阶。结合已付有限公共因子 $K_{101}$，若原目标 $h_0t_\nu$ 已有 Q 多项式来源，则已有加权成本至多 **8623** 的来源。目标成员性本身仍为条件。

## 2. 29 个对象确为同一原 source 核

本次先用已提交的原生成器恢复旧会话已经失去的临时核数据。标准 Koszul 族为
$$
F_j e_i-F_i e_j,\qquad
m_a(F_j e_i-F_i e_j),\qquad i<j,\quad 0\le a\le10,
$$
共 $1632$ 列。对原 $1834$ 个 $J$ 外来源行求完整支撑核，再运输为全部 $6188$ 个原来源系数。

新实际运行重新核了以下事项：

1. 当前自然 $u$ 模型的全部 $17\times77=1309$ 个常系数，逐整数等于旧 point model 的 primitivePointCoefficients。
2. $m_0,\ldots,m_8$ 为 normal 变量，$d=m_9,c=m_{10}$ 为纯变量，原字典一致；来源乘子按总次数 $0,1,2,3$ 枚举。
3. 每个核向量在全部 $1834$ 个 $J$ 外来源坐标严格为零。
4. 每列重新乘回全部 $4367$ 个原输出；$29\cdot4367=126643$ 个整数产品全部为零。
5. 29 列的原 $36$ 个自由来源坐标矩阵具有 Q 秩 $29$。

令
$$
\mathcal K=\ker_{\mathbb Q}B_0,\qquad \dim\mathcal K=36,
$$
并令 $S\subset\mathcal K$ 为这些 29 列张成的空间。它们是**原 source 坐标**的核，不是输出侧的 29 个余类或常左头。事实上本次还核了更强的全输出恒等式 $A_0k=0$；限制到 $I$ 后当然仍有 $B_0k=0$。

因此每个 $k\in S$ 对任何完整常校正都消失：
$$
k^TB_0^T\lambda=0,\qquad \lambda\in\mathbb Q^{4354}.
\tag{2.1}
$$
它同时消去 $M'_0=B_0^TE_{\rm new}$、normal4 和 normal5 校正像。没有对这些校正额外施加低支撑假设。

## 3. 第二连接的完整 forcing 商

沿用已付完整常左核及完整第一族：
$$
\Lambda\in\mathbb Z^{4354\times36},\qquad
B_0^T\Lambda=0,\qquad
B_0^TE_{\rm old}X+B_1^T\Lambda C=0.
\tag{3.1}
$$
这里 $C$ 的秩为 $33$，$\Lambda C$ 正好给所有第一可延头。取 $F$ 的三列为其在完整 $36$ 维常头空间中的一个补空间，定义
$$
H_F=B_1^T\Lambda F,\qquad
T=B_1^TE_{\rm old}X+B_2^T\Lambda C.
\tag{3.2}
$$
令
$$
E=\mathbb Q^{4354}/\operatorname{im}B_0^T,\qquad
H=\operatorname{span}_E[H_F],\qquad
W=\operatorname{span}_E[H_F,T].
$$
由完整第一秩为 $3$，有
$$
\dim E=36,\qquad \dim H=3,\qquad H\subset W.
\tag{3.3}
$$

任意第一头写作 $\lambda_0=\Lambda Cc$。全部可用的第一层歧义为
$$
\lambda_1=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy.
$$
由 (3.1)，$y$ 的二阶来项可以用 $E_{\rm old}Xy$ 精确抵消。允许 $\lambda_2$ 取所选 $I$ 的所有输出坐标后，完整二阶可解条件正是
$$
[H_Ft+Tc]=0\quad\text{于 }E.
\tag{3.4}
$$
所以
$$
\boxed{\operatorname{rank}\beta_2=\dim W-\dim H=\dim W-3.}
\tag{3.5}
$$
这一步使用完整 $\operatorname{im}B_0^T$，没有把 normal 次数至多 $3$ 或 $4$ 的校正像误当完整校正像。

## 4. 实际小配对与余维 7 上界

有限维线性代数给出完美配对
$$
E\times\mathcal K\longrightarrow\mathbb Q,\qquad
([z],k)\longmapsto k^Tz.
\tag{4.1}
$$
将它限制到 $S$，得到满射
$$
\pi:E\longrightarrow S^*,\qquad \dim\ker\pi=36-29=7.
\tag{4.2}
$$
满射来自任何 $S$ 上的线性泛函都能延拓到 $\mathcal K$；这不是额外的数值秩假设。

设 $K$ 是本次真 29 source 列的基矩阵。本次完整精确配对为
$$
P=K^T[H_F,T]\in\mathbb Q^{29\times36}.
$$
其实际 Q 秩与前三列秩分别是
$$
\boxed{\rho=\operatorname{rank}P=5,\qquad
h=\operatorname{rank}(K^TH_F)=1.}
\tag{4.3}
$$
所有 forcing 行都取原未按 content 除去的整数系数。仅在求小矩阵秩时作可逆的有理逐行、逐列缩放，并将核坐标按逆列尺度运输回来。完整原 $PZ=0$ 也已核过。

由 (4.2)–(4.3)，
$$
\dim W
=\dim\pi(W)+\dim(W\cap\ker\pi)
\le5+7=12.
$$
结合 (3.5)，立即得到
$$
\boxed{\operatorname{rank}_{\mathbb Q}\beta_2\le12-3=9.}
\tag{4.4}
$$

此前的合法下界是 $9$：常块在 Q 与模 $31$ 下均有秩 $4318$，同一常单位主块可在 $\mathbb Z_{(31)}[[u]]$ 中消去；第一层在两个域均有秩 $3$，再消去其三个 $31$ 单位主元。所得同一第二层矩阵的模 $31$ 秩为 $9$，所以其 Q 秩至少为 $9$。这里不把更高层的模 $31$ 指数自动提升到 Q。

(4.4) 与该下界夹逼，证明 (1.2)。

还可精确描述为何 29 维配对已经足够。因 $\dim W=12$，上述余维不等式取等，故
$$
\ker\pi\subset W,\qquad
\dim(H\cap\ker\pi)=3-h=2.
$$
可见部分的二阶商维数为 $5-1=4$；不可见部分至多且实际为 $7-2=5$。两者合计恰为 $9$。

程序同时算得配对系统的 $33$ 个头坐标投影维数
$$
33-\rho+h=29.
$$
这只是 29 个 source 测试留下的候选头空间，**不是完整第二头空间**。上述余维夹逼确定完整头空间为 $24$。

## 5. 旧 22 显式头、完整 24 维存在性及高 normal 部分

实际完整 normal 次数至多 $4$ 的扩展已经证明：该支持内仍恰有 $22$ 个头，且任何合法第二族的 normal4 分量均为零。相关实际回执是

[完整 normal4 结果](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-normal-four-complete130.json)。

现在完整 $I$ 输出的第二头空间已证明为 $24$ 维。因此两个新增头方向必须使用 normal5 校正，不能从旧 normal4 核的 130 个方向中单独得到。

这也给出一个不需新计算的精确后继接口。对同一个第二头，两组二阶提升的差满足
$$
\Delta\lambda_1=\Lambda Cy,\qquad
\Delta\lambda_2=E_{\rm old}Xy+\Lambda e.
\tag{5.1}
$$
右边支撑在 normal 次数至多 $3$。所以第二校正的 normal4、normal5 部分只依赖其头，而不依赖所选低层提升。

从完整 $24$ 维头空间取 $\lambda_2$ 的 normal5 部分，是一个真实线性映射。其核恰为已有 normal 次数至多 $4$ 的 $22$ 维头空间，故此映射的秩恰为 $2$。整个 normal4+normal5 高部分同样仅有 $2$ 维，且投到 normal5 上是单射的。

这说明下一显式构造只需捕获这一真实的二维高部分；本文尚未给出它的两个具体向量，也没有将 normal5 已停下的 786 个 pivots 宣称为完整求解。已有 22 个真 jet 可先用于构造合法第三层正证书，但那只能是受限 22 头入口；完整第三连接声明仍须保全部 24 维二阶来源。

## 6. 实际执行证据与历史 outcome 的范围

[主线完整小回执](../notes/r150-infinity-remote-session-789f/43702348535-same-source-koszul29-second-pairing.json)记录：

| 项目 | 实际值 |
|---|---|
| run / step | 43702348535 / same-source-koszul29-second-pairing |
| 执行源码提交 | 40344709899b84fb685dcf6874819aa3283c50ff |
| 新 wrapper SHA256 | 33b8a3e0c501488e5da6e2d654bfa84c915237ea537279fd45d24ba846653f14 |
| 退出码 | 0 |
| 共享预算 / 每进程内存 | 180 秒 / 2048 MiB |
| 数学时间 | 30.57484820100035 秒 |
| 实际墙钟 | 30.62542993900024 秒 |
| 原模型恢复 / 原 29 源恢复 / 新配对 | 0.465129596 / 28.330147234 / 1.768152662 秒 |
| 原整数乘回坐标数 | 126643，全部为零 |
| 29 列原自由坐标 Q 秩 | 29 |
| 配对 Q 秩 / 前三列 Q 秩 | 5 / 1 |
| 完整配对核维数 / 33 头投影维数 | 31 / 29 |
| 新 M0 右端 / 新 NF / 新 Dixon 位数 | 0 / 0 / 0 |

本次数学 binding 为
ea772f01fa0ab8a761287893c15a94f83ebc6326703b40b82a5846e02b020e39。
新恢复的原 29 source binding 为
2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2。

| 本 job 临时对象 | 字节数 | SHA256 |
|---|---:|---|
| actual-koszul29-by36-original-forcing-pairing.json.gz | 112488 | b1b4c81c2e827fa92a375dfdc94d183604741badba3962de9e998add821946b1 |
| complete-koszul29-pairing-nullspace-and-head-projection.json.gz | 26563 | 0b9f98f1d53d3da4438fa3e5bb9fc4dca74db09a9d9331077f5a857f91895045 |
| 原完整 pipeline 小回执 | 17241 | be9838a14ddc10dd79282c6800b7c5e0d94be4f113c93533cabe222f59219911 |

旧 wrapper 只实现了下界 $\rho-h$，因此忠实输出
paired-subspace-insufficient-to-close-second 及先前区间 $[9,11]$。原源码、原回执和原字段全部保持历史事实。本节以上使用完整 source 核维数 $36$ 与真子空间维数 $29$，另加了余维上界 (4.4)，所以数学结论可以严格强于原 wrapper 的 outcome。没有把原回执改写为它没有计算的结果。

全部可重算大数组仍仅在当前 job 临时保存；永久保存源码、参数、小回执、run ID 与 SHA。

## 7. 同一子式的 $93/90/90$ 阶界

在 $\mathbb Q[[u]]$ 上记同一非零方阵 $B(u)$ 的 Smith 指数为
$\alpha_1\le\cdots\le\alpha_{4354}$。常核、第一可延头及完整第二可延头分别给
$$
\#\{\alpha_i\ge1\}=36,\qquad
\#\{\alpha_i\ge2\}=33,\qquad
\#\{\alpha_i\ge3\}=24.
$$
故
$$
\boxed{\operatorname{ord}_\infty D
=\sum_i\alpha_i\ge36+33+24=93.}
\tag{7.1}
$$
最小的 $4353$ 个指数在每个阈值最多少一，因而
$$
\sum_{i=1}^{4353}\alpha_i\ge35+32+23=90.
$$
由 Smith 的 determinantal-ideal 恒等式，同一原方阵的全部 cofactor 均至少消失 $90$ 阶。

每个其他原来源列，按其自己的原列权归一后仍在 $u=0$ 正则。沿被替换列作 Laplace 展开，每项均含一个上述 cofactor，故所有原来源换列子式也至少消失 $90$ 阶。对按真实目标权归一后的原目标列，同样有该 cofactor 界。这里不声称来源换列保持 $92$ 或 $93$ 阶，也不借用模 $31$ 的 cofactor 阶 $222$。

## 8. $K_{101}$ 后的条件来源费 $8623$

原权定义及完整余式运输沿用
[原子式权定义](R150-appendix-original-projective-minor-conditional-source-cost8814.md)
与[公共因子的原来源降度式](R150-appendix-common-minor-factor-conditional-source-cost8740.md)：
$$
a_\ell=
\begin{cases}
20+10|\gamma|,&m^\gamma N_i,\\
25+10|\gamma|,&m^\gamma\Gamma_i,
\end{cases}
\qquad
b_i=10|\beta_i|,\qquad
\delta_\ell=a_\ell-10.
$$
其中 $|\gamma|\le3$、$\max a_\ell=55$、$\max\delta_\ell=45$，
$$
H=\sum_{\ell\in J}a_\ell-\sum_{i\in I}b_i=8770.
$$

[零点第六阶正式结果](R150-appendix-zero-fifteen-sixth-left-jets-exact-first-four-factor101-and-cost8625.md)
给出有限公共因子
$$
K_{101}=s^{55}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2,
\qquad \deg K_{101}=101,
$$
它整除全部原最大子式；不称其为完整 gcd。另同一 $D$ 的非零模 $31$ 约化次数已实付为 $8770-243=8527$，所以 $\deg_{\mathbb Q}D\ge8527$。

令 $d_*=D/K_{101}$、$q=\deg d_*$。结合 (7.1)，
$$
\boxed{8426=8527-101\le q\le8770-93-101=8576.}
\tag{8.1}
$$
对每个原来源列 $A_\ell$，定义
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{101}.
$$
它是多项式，并在全部原 $4367$ 个输出上满足
$$
A_JP_\ell=d_*A_\ell.
$$
这是原泛秩 $4354$ 下从所选 $I$ 投影回完整原像的伴随恒等式。新换列阶界给
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-90-101.
\tag{8.2}
$$

明确假设原目标 $b_\nu=h_0t_\nu$ 已属于
$\operatorname{im}_{\mathbb Q[s]}A$。该成员性保证
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{101}
$$
为多项式。原目标权 $\tau_\nu=44+2\nu\le64$，因此
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-90-101.
\tag{8.3}
$$

将所有非基来源系数按 $d_*$ 作余式整理，再利用完整原来源恒等式回收基列。三个加权成本分支逐项为
$$
\begin{aligned}
\text{非基余式：}\quad q-1+45&\le8620,\\
\text{基列转移：}\quad8770+55-90-101-11&=8623,\\
\text{基列目标：}\quad8770+64-90-101-10-8426&=207.
\end{aligned}
$$
故
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\
\exists x^{(\nu)}:\quad
Ax^{(\nu)}=h_0t_\nu,\qquad
\max_\ell(\deg x^{(\nu)}_\ell+\delta_\ell)\le8623.
}
$$

完整二阶秩 $9$ 和头空间维数 $24$ 已证明，不以两个显式新来源尚待恢复为由削弱该维数结论。另一方面，原目标成员性仍是上述成本命题的前提；指定行列式最高系数的 $31$ 单位性、完整 Q Smith 长度及原九目标特征零多项式来源均未由本文得到。
