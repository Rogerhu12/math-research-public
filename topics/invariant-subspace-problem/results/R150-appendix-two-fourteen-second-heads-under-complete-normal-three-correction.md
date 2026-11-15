# s=2 原完整第一首项的单个第二阶缺口：全部 normal≤3 校正后的严格负结果

日期：2026-11-15  
作者：AI（ChatGPT；同一原 R150 模块的精确来源计算与证明）

## 1. 结论与范围

令 $t=s-2$，$A(t)$ 为原十七式、全部次数至多三的乘子所给的 $4367\times6188$ 矩阵。采用已核的可逆共动目标坐标，并写

$$
A(t)=A_0+tA_1+t^2A_2+\cdots .
$$

这里的“第二阶首项”指存在 $\lambda_1,\lambda_2$ 使

$$
A(t)^T(\lambda_0+t\lambda_1+t^2\lambda_2)=O(t^3)
$$

的常数项 $\lambda_0$。[此前的完整第一连接证明](R150-appendix-two-full-first-connection-exact-seven-and-truncated-target-membership.md)已经严格证明完整常数左核维数为 $22$、完整第一连接秩为 $7$，故完整第一阶首项空间维数为 $15$。

本次精确有理计算证明：在允许全部 normal 次数不超过三的 $\lambda_2$、全部常数第一修正以及全部三次 normal 齐次核后，第二阶首项空间维数恰为 $14$。投影所得的十四个真实首项已经覆盖这一受限空间；剩余的一个第一阶首项不能用该范围内的校正延拓。

**本次不证明完整第二连接秩为 $1$。** normal 次数四、五的 $\lambda_2$ 及其与三次部分的相消尚未穷尽。因此完整特征零第二连接仍仅满足

$$
0\leq\beta_{2,\mathbb Q}\leq1.
$$

也不由本次负结果判断原九个 $h_0t_j$ 的完整局部成员性。

## 2. 第一阶代表的真实来源与全部歧义

令 $\Lambda$ 为 $155\times22$ 的完整常数左核矩阵；$155=20+135$ 分别是纯切向与一次 normal 目标坐标。原常数矩阵的全部左核均在这 $155$ 个坐标内。

[同原投影与完整局部谱证明](R150-appendix-two-full-field11-smith14-characteristic-zero-gap2-and-local-target-multiplier.md)保留原真实投影的特征零局部正谱 $1^7,2,3$。其十五维第一首项空间嵌入完整原模块，而完整第一首项空间也已证明恰为十五维。因此二者相等。可选矩阵

$$
H\in\mathbb Q^{22\times15},\qquad
Y\in\mathbb Q^{155\times15}
$$

满足

$$
A_0^T\Lambda H=0,\qquad
A_1^T\Lambda H+A_0^TY=0.
$$

两式均在全部 $6188$ 原来源上成立。任一同一首项的其他第一修正与 $Yv$ 的差属于 $\ker A_0^T$，故恰可写成 $\Lambda b$。于是所有第一阶歧义都由

$$
\lambda_0=\Lambda Hv,\qquad \lambda_1=Yv+\Lambda b
$$

保留，其中 $b\in\mathbb Q^{22}$，不是只保留选定代表。

本次从小原投影重新构造这些矩阵，并与此前已成的全部 $605\times15$ 第一修正按逻辑 SHA256 一致性核对；其中 $450\times15$ 的二次 normal 块逐元素确为零。新构造另在所有原来源上核验了 $185640=6188\cdot15\cdot2$ 个第一阶恒等式坐标。

## 3. 第二阶强迫项及高来源分解

定义

$$
R_2=A_2^T\Lambda H+A_1^TY,\qquad C=A_1^T\Lambda.
$$

第二阶条件为

$$
A_0^T\lambda_2+Cb+R_2v=0.
$$

对于本次十五条完整第一阶代表，$R_2$ 在 normal 乘子次数二、三的全部 $5100=2295+2805$ 条来源行上都严格为零。这一零性由原系数生成及乘回验证，不由截断猜测。

把低来源定义为 normal 乘子次数零、一的全部 $1088=170+918$ 行。令

$$
B=A_0^T|_{\text{normal 目标次数一、二}}
$$

在低来源上的矩阵，形状为 $1088\times585$；纯切向常数校正被 $A_0^T$ 杀掉，故不必重复列入 $B$。

[已付完整三次 normal 高核定理](R150-appendix-two-complete-normal-three-high-kernel-and-first-head-stability.md)的高块为

$$
H_3:\mathbb Q^{990}\longrightarrow\mathbb Q^{2295}.
$$

它保留三次 normal 目标的全部六个切向次数切片，精确秩为 $988$，核维数为二。两条真实有理核列记为 $W$，补到其他目标坐标后在全部 $5100$ 高来源行上仍为零。本次重新核验其 $10200=5100\cdot2$ 个原高来源乘积，并核对两条已付候选列的逻辑哈希。令

$$
C_h=(A_0^TW)_{\mathrm{low}}\in\mathbb Q^{1088\times2}.
$$

因此，当 $\lambda_2$ 的 normal 次数至多三时，高来源方程迫使其三次部分恰在 $\operatorname{im}W$；其余条件完整等价于

$$
Bx+C_hc+Cb+R_2v=0
$$

的全部 $1088$ 行。这里没有删除高来源，也没有只挑一条三次核。

## 4. 七个 incoming 列的精确缩减

第一关系给出 $C$ 的二十二列模 $\operatorname{im}B$ 的秩恰为七。实现使用 $H$ 的真实自由坐标选择矩阵 $E_F$，以及实际独立列

$$
P=(9,10,11,14,15,16,17)
$$

（零基编号），并在原低来源上核验完整矩阵恒等式

$$
C=-B_1Y_1E_F+C_P(I-HE_F)_P.
$$

这里 $Y_1\in\mathbb Q^{135\times15}$ 是 $Y$ 的一次 normal 行限制（其二十个纯切向行恒为零），$B_1$ 是 $A_0^T$ 在一次 normal 目标上的真实限制，$\operatorname{im}B_1\subseteq\operatorname{im}B$。所以替换 $C$ 为七列 $C_P$ 精确保留全部二十二个第一修正的作用，并非固定或丢弃其余参数。

由此得到常矩阵

$$
M=[B,\ C_h,\ C_P]\in\mathbb Q^{1088\times594}.
$$

它的真实秩为 $592$，完整齐次核维数为二。

## 5. 唯一缺少首项的一次精确求解

从原投影重新恢复十四个完整第二阶首项及其三层 cochain；全部 $259896=6188\cdot14\cdot3$ 个原乘回坐标均为零。在十五维第一首项坐标中，补入真实坐标 $e_5$（零基编号）得到可逆的十五维首项框架。记其强迫项为

$$
r=R_2e_5.
$$

所有其他首项模已成十四维空间，只需这一列 $r$。

本次没有重求旧的 $583$ 单位块或二十二个旧不相容右端。对 $M$ 的真实 $592$ 列、$592$ 行单位块，只求一个右端的有理解，并把解乘回全部 $1088$ 行。常块的行清分母与 primitive 缩放只作用于单位矩阵本身，不由右端决定；右端比例在原乘回前恢复。

精确结果是

$$
\operatorname{rank}_{\mathbb Q}M=592,\qquad
\operatorname{rank}_{\mathbb Q}[M,r]=593.
$$

完整 Schur 余量秩为一，故 $r\notin\operatorname{im}M$。全部 $595$ 列的核仍只有原来两个零首项齐次方向。结合已成十四个真实第二首项，证明 normal≤3 范围内的第二首项空间恰为十四维。

单位行选择采用事先固定的素数 $17$；最后的增秩与不相容结论来自完整有理 Schur 余量及原行乘回，不是有限域负结果。

## 6. 为什么仍需 normal 四、五的完整高块

一般 $\lambda_2$ 还可以含 normal 次数四、五部分。此时高来源条件是

$$
H_{\ge2}
\begin{pmatrix}\lambda_{2,3}\\ \lambda_{2,4}\\ \lambda_{2,5}\end{pmatrix}=0,
\qquad
H_{\ge2}=
A_0^T|_{\substack{\text{全部 normal 乘子次数二、三来源}\\
\text{normal 目标次数三、四、五}}},
$$

其中 $H_{\ge2}$ 的形状为 $5100\times3762$。不能把四、五次部分分别置零，也不能仅由单独某块的单射性删除跨块相消。新增高齐次核可能通过其三次部分改变低来源返回，因此本次 $593$ 的低增广秩尚不是完整第二连接的正秩证明。

两条已成 $W$ 补零后给出 $H_{\ge2}$ 的两个独立真实有理核，故其有理秩至多 $3760$。若后继完整原高块在一个固定素数下得到秩 $3760$，即可夹逼证明这两条核已穷尽完整高核，届时才可把本次结果升级为完整 $\beta_{2,\mathbb Q}=1$。本稿不预填该后继秩。

## 7. 实际执行与可复算身份

实际任务为 run **43740928483** 的 step **two-one-true-rational-second-connection**，执行源码提交为 **48b1926b0f6f1543086fe8331fea0beadd4c0001**。数学用时 **5.525103607999881 秒**，退出码为零。

源码：

- notes/2026-11-15-r150-two-one-true-rational-second-connection-789f.py
- SHA256：d4ff08a474ef3abe6c7ee08bea7829e6fa3d52eb2e04c71469b18b2ea2c27bb8。

实际小回执：

- notes/r150-source-kernel-session-789f/43740928483-two-one-true-rational-second-connection.json
- 完整外回执 $20775$ 字节，SHA256：950aecf40605fbd3156c223d7e18d4ee1821940386872f59d88cc24f756ed1a2。
- 原始数学回执 $12714$ 字节，SHA256：9ee595e16b635521be1c0e671dd7a1225a712aea7b2344829d1a72b2aee8fb5c。
- 实际 checkpoint binding：3de42bed91acf562cce951f7c79f9e4f871cbd31ec82e7430d03bb97198f970f。

常矩阵 $M$ 的逻辑 SHA256 为
4bc8ac3db2ee7c5a77c6b4f66b72d05baf27c45fde5f153c14984e7ee87bde37；
完整 $1088\times1$ Schur 余量逻辑 SHA256 为
2fcd7d467208d101a853ff9b3cb58180e6329467464e54c364fc7aeb6269a743。

证明依赖的既有结论是完整常数核、完整第一连接恰七、原投影局部谱 $1^7,2,3$、完整三次 normal 高核恰二维及旧第一 cochain 的原来源身份；本次源码与回执逐一固定其输入 SHA256。全部可重算矩阵只保留在当前临时任务中，仓库保留源码、参数、实际运行身份和小回执。
