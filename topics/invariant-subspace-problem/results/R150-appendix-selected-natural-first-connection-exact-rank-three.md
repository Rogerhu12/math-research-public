# 同一原所选无穷远方阵：特征零自然一阶连接的秩恰为 3

作者：Astra-ISP-789f / normal_annihilator。AI-assisted；GPT-6 Astra Pro。  
日期：2026-11-15。状态：完整原行的精确有理证书已实际完成。

## 1. 对象与结论

沿用原十七式及其自然加权齐次化，记
$$
A(u)=A_0+uA_1+u^2A_2+\cdots,\qquad
B(u)=A(u)_{I,J},
$$
其中原输出集合 $I$ 与原来源集合 $J$ 均有 $4354$ 个元素。本文不改变 $I,J$、原行的非零常数重标、原单项式顺序或局部参数 $u$。

已付的同一原常数矩阵结论是
$$
\operatorname{rank}_{\mathbb Q}B_0
=\operatorname{rank}_{\mathbb F_{31}}\overline B_0=4318.
\tag{1.1}
$$
因而右核与左余空间均为 $36$ 维。此前用同一原自然系数计算的一阶连接满足
$$
\operatorname{rank}_{\mathbb F_{31}}\overline\beta_1=3.
\tag{1.2}
$$
本次以完整原左一阶恒等式证明
$$
\boxed{\operatorname{rank}_{\mathbb Q}\beta_1=3.}
\tag{1.3}
$$

这里
$$
\beta_1:\ker B_0\longrightarrow\operatorname{coker}B_0,\qquad
v\longmapsto[B_1v].
$$
结论只针对同一所选方阵 $B$。本次没有把额外十三个输出行加入所选左校正，因此不把 (1.3) 自动称为 $4367\times4354$ 全输出矩阵的一阶连接秩。

## 2. 完整三十六维原左头及合法的有限支撑

取 $m_0,\ldots,m_8$ 为横向变量，$c=m_{10},d=m_9$ 为纯切向变量。已完成的 $585$ 维精确投影给出 $29$ 维全输出低横向左核。将 $I$ 所删的三个低横向输出坐标置零，三个限制的有理秩恰为 $3$，得到 $26$ 维所选低横向左核。加上 $I$ 内十个纯切向坐标，得到完整基矩阵
$$
\Lambda\in\mathbb Z^{4354\times36},\qquad
B_0^T\Lambda=0,\qquad \operatorname{rank}_{\mathbb Q}\Lambda=36.
\tag{2.1}
$$
各列分别清分母并去公因子；这不改变有理头空间。全部头均支撑在横向次数不超过 $2$ 的原输出上。

先允许一阶校正 $\lambda_1$ 支撑在 $I$ 的横向次数 $1,2,3$ 的输出上，共
$$
132+450+990=1572
$$
个坐标。用上述 $26$ 个低横向常左核选择 $26$ 个独立取值坐标，将这些校正坐标规范为零，剩余 $1546$ 个校正变量。纯切向校正也可用十个纯常左核消去。记剩余坐标的原输出嵌入为
$$
E:\mathbb Q^{1546}\longrightarrow\mathbb Q^{4354}.
$$

于是本次实际求解的是
$$
M_0x+Hc=0,\qquad
M_0=B_0^TE,\quad H=B_1^T\Lambda.
\tag{2.2}
$$
完整头变量数为 $36$，总变量数为 $1582$。

这一支撑限制没有被预设为所有左一阶解的充分参数化。它首先只用于构造合法的正证书。对于原来源乘子的横向次数至少为 $3$ 的列，原常数多项式 $F_0$ 至少含一个横向变量，故 $B_0^TE$ 的对应行严格为零；$B_1^T\Lambda$ 的对应行也严格为零，因为任何自然 $F_1$ 单项式的横向次数非负，而头的横向次数至多为 $2$。

特别地，程序实际记录 `naturalF1PureCoefficientsZero=false`。省去这些零行的证明不要求自然 $F_1$ 在纯切向平面消失，也没有以共动坐标的一阶矩阵替换原自然 $B_1$。

实际保留 $2618$ 条原来源行，另有 $1736$ 条上述严格零行。它们合计原来的全部 $4354$ 条方程。

## 3. $1546$ 个校正列为何确实独立

这一点既由本次精确行化简核实，也有直接的源空间证明。

若 $M_0x=0$，则 $Ex\in\ker B_0^T$。完整常左核已由 (2.1) 给出，且全部支撑在横向次数至多 $2$。由于 $Ex$ 的纯切向坐标为零，它只能落在上述 $26$ 个低横向头的张成空间内。本次所选的 $26$ 个规范坐标在这个空间上的取值矩阵可逆，而 $Ex$ 在这些坐标上也全为零，故 $Ex=0$，继而 $x=0$。因此
$$
\operatorname{rank}_{\mathbb Q}M_0=1546.
\tag{3.1}
$$

这里没有使用更强而尚未证明的断言“仅高横向来源就独自生成全部高横向输出”。

## 4. 实际精确计算和原行证书

首次运行完成了丢失的 $585$ 维有理余空间重建，以及 (2.2) 的原整数输入构造；随后在有理行化简阶段达到时钟上限。首次没有产生完整 RREF 或新的特征零一阶秩结论。

续算沿用完全相同的源码、输入和数学绑定，复用已完成的 $585$ 缓存及原整数输入。它只重新开始此前尚未保存内部进度的本次 RREF。没有重做旧 $4318$ 阶消元、增加 Dixon 位数或换素数。

实际运行：

| 项目 | 实值 |
|---|---|
| GitHub Actions run | $43702348535$ |
| step | `selected-natural-first-characteristic-zero-left-envelope-continue180` |
| 执行源提交 | `57f2ef394446bad1c2509191d281c49b25b82622` |
| 共享数学预算 | $180$ 秒 |
| 每进程地址空间上限 | $1024$ MiB |
| 实际数学时间 | $91.64425810400007$ 秒 |
| 其中原 envelope 核心时间 | $91.6299156130001$ 秒 |
| 进程退出码 | $0$ |
| 原整数输入 | $2618\times1582$，$73434$ 个非零整数项 |
| 完整 RREF 秩 | $1549$ |
| 常数校正列秩 | $1546$ |
| 头的障碍秩 | $3$ |
| 独立可提升左头数 | $33$ |
| 完整原一阶产品坐标 | $4354\cdot33=143682$，全部为零 |

实际 RREF 保存后才重建候选列；完整候选也先保存，再逐条乘回全部原未缩放方程。候选变量证书的最大整数位长为 $3147$。这个数是变量列的位长，不另称展开后的全部输出头系数具有相同位长。

设实际证书中的校正变量矩阵与头系数矩阵分别为
$$
X\in\mathbb Z^{1546\times33},\qquad
C\in\mathbb Z^{36\times33}.
$$
每列分别作了非零有理缩放，因此整数代表可不同，但均严格满足
$$
B_0^TEX+B_1^T\Lambda C=0.
\tag{4.1}
$$
保存的 $33$ 个自由头坐标构成非零对角子矩阵，故
$$
\operatorname{rank}_{\mathbb Q}C=33.
\tag{4.2}
$$
所有校正与头的输出坐标都在同一个 $I$ 内。没有借助 $I$ 之外的十三个输出坐标消去余式。

相关真实 gate 均为真：

- `all4354OriginalConstantLeftProductsZero`；
- `all4354OriginalFirstLeftJetProductsZero`；
- `allSelectedOutputSupportVerified`；
- `allHeadProjectionFreeCoordinatesIndependent`；
- `completeFixedSupportEnvelopeComputed`。

## 5. 上下界闭合及完整第一层参数化

对任意 $\lambda_0\in\ker B_0^T$，其属于 $\beta_1$ 对偶映射的核，当且仅当存在 $\lambda_1$ 使
$$
B_0^T\lambda_1+B_1^T\lambda_0=0.
\tag{5.1}
$$
(4.1)–(4.2) 给出 $33$ 个独立的这种头，所以
$$
\operatorname{rank}_{\mathbb Q}\beta_1\le36-33=3.
\tag{5.2}
$$

为解释模 $31$ 下界如何合法运输到有理数域，令 $\mathcal D=\mathbb Z_{(31)}$。由 (1.1) 可在同一原常数矩阵中选取一个模 $31$ 非零的 $4318$ 阶子式；它是 $\mathcal D$ 上的单位。沿这个单位块作原形式 Schur 消元，常数余块因有理秩恰为 $4318$ 而严格为零。一阶余块属于 $\mathcal D^{36\times36}$，其模 $31$ 约化就是已付的同一自然连接。模 $31$ 秩为 $3$ 的非零子式因此仍是有理非零子式，给出
$$
\operatorname{rank}_{\mathbb Q}\beta_1\ge3.
\tag{5.3}
$$
结合 (5.2) 得到 (1.3)。

于是全部可提升的左头空间恰为 $\operatorname{im}(\Lambda C)$。更进一步，完整第一层左射流具有精确参数化
$$
\boxed{
\lambda_0=\Lambda Cc,\qquad
\lambda_1=EXc+\Lambda d,
\quad c\in\mathbb Q^{33},\ d\in\mathbb Q^{36}.
}
\tag{5.4}
$$
证明是：先用 (4.1) 选择一个给定头的实际校正，再减去该校正；差满足 $B_0^T(\text{差})=0$，故恰落在完整常左核 $\operatorname{im}\Lambda$。

运行时保留的 `higherTransverseLeftCorrectionsRuledOut=false` 表示计算没有先假设支撑限制充分。实际 $33$ 维正证书与完整下界夹逼之后，(5.4) 是由完整常核推出的数学结论。它没有额外丢弃第一校正的 $36$ 维歧义。

## 6. 对后续自然 $u$-Smith 页的准确作用

因为常数单位块与第一连接的小单位块都在 $\mathcal D$ 上有单位子式，且它们的有理秩与模 $31$ 秩分别相等，可在 $\mathcal D[[u]]$ 上作可逆左右变换，得到
$$
B(u)\sim
\operatorname{diag}\!\bigl(I_{4318},\,uI_3,\,u^2T(u)\bigr),
\qquad T(u)\in\mathcal D[[u]]^{33\times33}.
\tag{6.1}
$$
因此特征零恰有三个正 Smith 指数等于 $1$，其余 $33$ 个至少为 $2$。这是同一自然参数和同一所选方阵的结论。

已完成模 $31$ 全 Schur 计算的第二层秩为 $9$，故 (6.1) 的 $T(0)$ 在有理数域的秩至少为 $9$。若下一步实际构造 $24$ 个独立的原左二阶头，则可把第二层秩也夹成 $9$；目前没有把这个后继构造记作已完成。

准确的下一原式为
$$
B_0^T\lambda_2
+B_1^T\Lambda d
+\bigl(B_1^TEX+B_2^T\Lambda C\bigr)c=0.
\tag{6.2}
$$
其中 $d$ 是 (5.4) 的全部第一校正歧义，不能只保某个选定 $EXc$ 而删去它。后续如压缩这 $36$ 个 $d$ 方向，必须同时保实际原预像及其核对应的校正来源。

本次没有证明所有高阶 Smith 指数与模 $31$ 相同，没有证明特征零行列式的无穷远阶为 $243$，也没有证明原参数行列式首项是 $31$ 单位。原 $h_0$ 的特征零多项式成员性仍未由本结论解决。

## 7. 小回执、临时证书身份与可重建来源

永久保存的是源码、参数、实际 run 及小回执。下列可重算数组仅保于当前临时计算会话，不上传 Git、Release 或长期附件。

| 临时文件 | 字节 | SHA-256 |
|---|---:|---|
| `same-original-natural-left-envelope-integer-input.json.gz` | $3244457$ | `2fabe7d680cc65e6098c4a9940d7f8e7c5eb21c0ffd57e5a168b0b348f53ba8a` |
| `complete-same-I-characteristic-zero-left-heads.json.gz` | $633788$ | `3107ab8547071205466ff5b5aa2ef5f0e3ea81a976258a25184c9a0d7e709fe2` |
| `complete-left-envelope-rref.json.gz` | $1515677$ | `3eae6c4d2b9d2c01187ea436665499555b3a8b9843bdd7ed2925b4551e0148d2` |
| `complete-original-left-first-jets.json.gz` | $1701626$ | `2aabfc92860f66942e7a8eb3d9254ab911e7b8b2f255d40bfaa1235ed4d482fe` |

完整临时主回执为 $6772$ 字节，SHA-256
`8319aa18c49d4d56bbc9a898fa16ef40b897071587468c510cd12a325faeef99`。
核心语义绑定为
`717dd4bfc621d633c40c01ffd0e35345828ffc98b9edf25b10989153ece49d91`；
外层同源重建绑定为
`69b179dd9a10089e285160425211bd0af0c75f7e1c520ac9fc349c394076c655`。

可重建与审计入口：

1. [同一原常数秩 $4318$ 与 $585$ 投影](R150-appendix-selected-second-transverse-rank556-constant4318-and-infinity-order50.md)。
2. [完整 $49/36$ 余空间接口](R150-appendix-selected-exact-cokernels49-36-and-natural-schur-interface.md)。
3. [原自然第一连接及输出限制](R150-appendix-natural-first-connection-complete49-36-and-output-restriction4340.md)。
4. [本次 exact envelope 核心](../notes/2026-11-15-r150-selected-natural-first-left-envelope-789f.py)，$20823$ 字节，SHA-256 `4901fa8fcebbda69a9c6042cdf20f622083c8e75285b19051bba47f435dc2ac9`。
5. [同源重建及缓存续算入口](../notes/2026-11-15-r150-selected-natural-first-left-envelope-rebuilt-runner-789f.py)，$12026$ 字节，SHA-256 `3e7b9ea6875f52961ddfaff2615afd3481ef85bbd75b8b1d5b76cebb94ee9bf2`。
6. [实际完成小回执](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-first-characteristic-zero-left-envelope-continue180.json)。
7. [首次仅到准备完成的小回执](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-first-characteristic-zero-left-envelope.json)。
