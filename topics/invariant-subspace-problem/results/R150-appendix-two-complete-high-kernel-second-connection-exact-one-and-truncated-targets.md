# s=2 完整高核恰二维、第二连接恰一及九目标的三阶截断来源

日期：2026-11-15  
作者：AI（ChatGPT；Astra-ISP-789f / literature_audit）

## 1. 新的完整结论

对同一原十七式及全部次数至多三来源，令 $t=s-2$，并使用已核的可逆共动坐标写原矩阵为

$$
A(t)=A_0+tA_1+t^2A_2+\cdots,\qquad
A(t):\mathbb Q[[t]]^{6188}\longrightarrow\mathbb Q[[t]]^{4367}.
$$

其常秩为 $4345$，泛秩为 $4354$，故有九个正 Smith 指数及十三个自由左核方向。完整第一连接已经证明秩为七。

本次将 normal 次数四、五的全部校正一并纳入，严格证明

$$
\beta_{2,\mathbb Q}=1,\qquad
\dim K_2=14.
$$

这里 $K_2$ 是能够提升为真实二阶左 jet 的全部常数首项空间，不是某个受限代表族。

相应地，完整正 Smith 指数已经缩小为

$$
1^7,2,b,\qquad b\in\{3,4,5\}.
$$

此外，每个完整二阶左 jet 的三个系数都只含纯切向及一次 normal 坐标。对九个原平方目标 $t_j$，$j=2,\ldots,10$，因此有

$$
t_j\in\operatorname{im}A(t)+t^3\mathbb Q[[t]]^{4367},
$$

以及

$$
h_0t_j\in\operatorname{im}A(t)+t^4\mathbb Q[[t]]^{4367}.
$$

这些是有限阶截断成员性；本稿仍不声称原 $h_0t_j$ 的完整局部或全局成员性。

## 2. 已付完整低层接口

[此前的完整第一连接证明](R150-appendix-two-full-first-connection-exact-seven-and-truncated-target-membership.md)给出十五条真实第一阶 cochain，记为

$$
(\lambda_0,\lambda_1)=(\Lambda Hv,Yv),
$$

其中 $\Lambda$ 是完整二十二维常数左核，$H$ 有十五列，且 $\Lambda$ 与 $Y$ 均支撑在纯切向及一次 normal 目标坐标内。所有同头第一修正还必须保留 $\lambda_1\mapsto Yv+\Lambda b$ 的完整二十二维歧义。

原真实投影的正谱为 $1^7,2,3$，并给出十四条真实二阶 cochain；它们全部在原 $6188$ 行上验证，二阶系数也仅用纯切向及一次 normal 坐标。

在 [全部 normal≤3 校正后的单 RHS 证明](R150-appendix-two-fourteen-second-heads-under-complete-normal-three-correction.md) 中，所有第二强迫项的 $5100$ 条高来源行已经实际验证为零；低来源保留全部 $1088$ 行。记

$$
M=[B_{585},C_h,C_P]\in\mathbb Q^{1088\times594}.
$$

其中 $B_{585}$ 保留一次、二次 normal 常数校正，$C_h$ 是两条已付三次高核的真实低返回，$C_P$ 是模原常像的七个完整第一 incoming 方向。七列替代完整二十二列由原矩阵恒等式证明，未删除首阶歧义。

对十四个已成二阶首项之外的唯一首项，其真实强迫项 $r$ 满足

$$
\operatorname{rank}_{\mathbb Q}M=592,\qquad
\operatorname{rank}_{\mathbb Q}[M,r]=593.
$$

这一增秩已经通过一个真实有理解及全部低行 Schur 余量验证。之前尚缺的唯一完备性问题是：normal 四、五的高校正是否能够与三次部分联合相消，并改变低返回像。

## 3. 本次使用的完整高块

按 normal 次数分开目标坐标，令

$$
V_3=\mathbb Q^{990},\quad V_4=\mathbb Q^{1485},\quad
V_5=\mathbb Q^{1287}.
$$

取原来源中 normal 乘子次数二、三的全部行，分别为 $2295$、$2805$ 行，定义

$$
H_{\ge2}:V_3\oplus V_4\oplus V_5\longrightarrow
\mathbb Q^{2295}\oplus\mathbb Q^{2805}.
$$

这是原 $A_0^T$ 的真实 $5100\times3762$ 子矩阵。原 $F_0$ 的纯切向部分在 $s=2$ 为零，因此低目标 normal 次数至多二的坐标不作用于这些高来源行。

所有三个目标列块和两个来源行块均按原系数生成。实际非零项计数为

$$
\begin{pmatrix}
50490&76410&0\\
0&61710&93390
\end{pmatrix}.
$$

特别保留了三、四与四、五之间的全部交叉作用；本证明没有把某个单块的单射性误当成整个联合高块的单射性。

## 4. 两条真实有理核给出上界

令 $W\in\mathbb Q^{990\times2}$ 为此前完整三次高核的两列，并令

$$
\widetilde W=
\begin{pmatrix}W\\0_{1485\times2}\\0_{1287\times2}\end{pmatrix}.
$$

本次读取同一个已验证的临时来源，核对文件、binding、逻辑矩阵哈希及 verified 状态，随后重新在原有理系数上核验

$$
H_{\ge2}\widetilde W=0
$$

的全部 $10200$ 个坐标。两列有非零二阶子式，故确实独立。因此

$$
\operatorname{rank}_{\mathbb Q}H_{\ge2}\leq3760.
$$

上界的来源是真实有理核，不是有限域核的猜测提升。

## 5. 固定 17 的完整下界

对 $H_{\ge2}$ 的每一条完整原有理行，先清该行全部分母，再除该整行的整数内容，得到整数矩阵 $H_{\mathbb Z}$。每行只使用一个非零有理比例，三个目标列块共同缩放；全部 $5100$ 条比例恒等式均逐项核验。因此

$$
\operatorname{rank}_{\mathbb Q}H_{\mathbb Z}
=\operatorname{rank}_{\mathbb Q}H_{\ge2}.
$$

这一步只处理原常数矩阵，不含任何 RHS，也不对参数 jet 作行内容除法。

在预先固定的素数 $17$ 下，实际完整消元得到

$$
\operatorname{rank}_{\mathbb F_{17}}
(H_{\mathbb Z}\bmod17)=3760.
$$

全部 $5100$ 原行与 $3762$ 原列均保留，真实主元与全部依赖原行归零都已核验。一个非零有限域子式给出同一整数矩阵在特征零的非零子式，因此

$$
3760\leq\operatorname{rank}_{\mathbb Q}H_{\ge2}\leq3760.
$$

结论为

$$
\ker_{\mathbb Q}H_{\ge2}=\operatorname{im}\widetilde W.
$$

不需要把任何有限域核提升为有理核，也没有声称完整参数模块在 $17$ 上平坦。

## 6. 第二连接的完整性

取任意完整二阶候选

$$
\lambda(t)=\lambda_0+t\lambda_1+t^2\lambda_2.
$$

完整第一首项只有十五维，而其所有真实第一修正都在 normal 次数至多一内。其第二强迫项在全部高来源上严格为零。因此第二阶高来源方程要求

$$
H_{\ge2}(\lambda_{2,3},\lambda_{2,4},\lambda_{2,5})^T=0.
$$

由上节完整高核等式，必有

$$
\lambda_{2,4}=\lambda_{2,5}=0,\qquad
\lambda_{2,3}\in\operatorname{im}W.
$$

所以所有完整校正都已经被前述 $M$ 的两条高返回列及全部低列覆盖。此前 $592\to593$ 的真实有理增秩现在成为完整不相容性证明：缺少的第十五个首项无法延拓，十四个已成二阶首项就是完整 $K_2$。故

$$
\dim K_2=14,\qquad\beta_{2,\mathbb Q}=15-14=1.
$$

这也表明此前完整 $\mathbb F_{11}$ 第二连接秩为零的计算不能代替本点特征零第二连接；原投影在 $11$ 下的第二连接虽保持秩一，完整第二页仍不保秩。此处只记录已实证的秩差，不由有限域负读数推断原有理目标的成员性。

## 7. 全部二阶 cochain 的一次 normal 支撑与目标读数

十四个完整二阶首项与原投影二阶首项相同，而且原投影已经提供一次 normal 支撑的完整三层代表。

设另一条完整二阶 jet 与该代表具有相同 $\lambda_0$。相减后写成

$$
0+t\mu_0+t^2\mu_1.
$$

其原方程恰给

$$
A_0^T\mu_0=0,\qquad A_1^T\mu_0+A_0^T\mu_1=0.
$$

也就是一条完整第一阶 jet。完整第一阶的两个系数都已证明在纯切向及一次 normal 坐标内。因此所有完整二阶 jet 的 $\lambda_0,\lambda_1,\lambda_2$ 都在该支撑内，而非只有本次选定代表如此。

原九个目标严格为

$$
t_j(s,m)=
\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,\qquad j=2,\ldots,10.
$$

在同一共动坐标中它们正是 $n_j^2$，是二次 normal 目标，而不是线性 $n_j$。所以任一完整左核 jet 模 $t^3$ 与每个 $t_j$ 的全部配对系数均为零。

在 $\mathbb Q[t]/(t^3)$ 上，Smith 对角化逐项给出像与转置核的双湮灭关系。于是

$$
t_j\in\operatorname{im}A(t)+t^3\mathbb Q[[t]]^{4367}.
$$

原 $h_0=t\,u(t)$ 且 $u(0)=17886115659776\ne0$，再乘这一真实原多项式就得

$$
h_0t_j\in\operatorname{im}A(t)+t^4\mathbb Q[[t]]^{4367}.
$$

这一有限阶结论不使用导数封闭，也不将参数坐标运输遗漏在配对之外。

## 8. 剩余谱与下一条最小缺口

此前完整有限域 $11$ 的原谱为 $1^7,3,4$，由实际最大子式给特征零总长上界 $14$。真实原投影总长为 $12$，给完整特征零总长下界 $12$。结合本次完整第一、二连接，余谱只有

$$
1^7,2,3;\qquad1^7,2,4;\qquad1^7,2,5.
$$

所以第三连接只能为零或一。完整二阶十四个首项中，投影已给十三个真实第三阶首项。后继应检验唯一剩余首项，并保留完整第二 incoming 像：

- 若唯一第三 RHS 相容，则第三首项有十四个，$\beta_{3,\mathbb Q}=0$；
- 若该 RHS 不相容，则第三首项恰十三个，$\beta_{3,\mathbb Q}=1$，完整谱为 $1^7,2,3$、总长为 $12$。

后一情形还会由原投影满射的长度差推出 $W/(L\cap W)=0$；本稿尚未断言该情形已经发生。

## 8a. 原投影差模的完整循环结构

令 $R=\mathbb Q[[t]]$、$L=\operatorname{im}A$，并保持原横向平方输出子模
$W=(I^2)_{\le5}$。原投影给
$$
0\longrightarrow T:=W/(L\cap W)
\longrightarrow C:=R^{4367}/L
\longrightarrow C_P\longrightarrow0.
$$
两余核自由秩都是十三，故 $T$ 为有限扭子模，并诱导扭子部分的满射。其理由也可直接写出：
若 $y\in\operatorname{Tor}C_P$，取原像 $x\in C$，则某个 $t^n x\in T$；
再乘一个消去有限模 $T$ 的幂，便知 $x$ 也属于 $\operatorname{Tor}C$。

原 $C_P$ 的正谱为 $1^7,2,3$，故 $t^3\operatorname{Tor}C_P=0$，于是
$$
t^3\operatorname{Tor}C\subseteq T.
$$
另一方面，完整 $C$ 的正谱已是 $1^7,2,b$，所以
$$
\ell(t^3\operatorname{Tor}C)=b-3
=\ell(\operatorname{Tor}C)-\ell(\operatorname{Tor}C_P)
=\ell(T).
$$
有限长度包含且等长迫使相等，得到自然子模中的准确结论
$$
\boxed{
T=t^3\operatorname{Tor}C
\cong R/(t^{\,b-3}),\qquad b\in\{3,4,5\}.
}
$$
$b=3$ 时右端是零模；$b=4,5$ 时分别是长一、长二的单个循环块。这一结构来自原投影满射，不只来自两个总长度的数值比较。

特别地，若 $b\le4$，则 $tT=0$，原 $h_0=t\,u(t)$ 的一次因子已经消去整个 $W$，故九个 $h_0t_j$ 全部有真实局部来源。只有 $b=5$ 时还需判断这九个指定平方类在上述长二循环模中的位置；不能只因差模非零就宣布某个指定目标不属于原像。

## 9. 实际执行身份

实际 run **43740928483**，step **two-complete-normal345-high-field17**，执行源码提交 **b92dc639cfb725ca0e4a77e402841afcf6719c67**。总数学步骤用时 **4.196554438000021 秒**，其中 native 秩计算 **1.779103328 秒**，退出码为零。

源码：

- notes/2026-11-15-r150-two-complete-normal345-high-field17-789f.py
- SHA256：5b223050e322576121f3f9d52a7366fde283440fe72852aa36e423fcb5d9b046。
- notes/2026-11-15-r150-two-complete-normal345-high-field17-native-789f.cpp
- SHA256：ac89263afb07205d418d8dbb6c967b48e287f2a1ff572b4fb20f1704b78e1ba4。

实际小回执：

- notes/r150-source-kernel-session-789f/43740928483-two-complete-normal345-high-field17.json
- 外回执 $11592$ 字节，SHA256：1582aa530b7439636798e33cf447ce46c3e85b352ab47b1e236cccc56525584a。
- 原始数学回执 SHA256：1a2e1dc9010da88479d428008304ff45e8604ee04ffcb63251b415f4f5b08f89。
- binding：28bddf30e73c27eb623837d9569c9b43db83bd93f54d6ce84eedef0f24d0e862。

原有理行流 SHA256：
3a666812737ddf2e0a1710f4e590641705f3e58512e6416a7a654bc35dcd1872；
整行 primitive 整数流 SHA256：
2196a859932efc4acd4362091adb67a1882d85df7569bbddc8d7c8cc5597deb3；
全部真实行比例 SHA256：
0330b4d37e0f360a521832a266078379e3a43d254b09f6b0d1450c59dd6b756c。

全部原矩阵、消元 DAG、归一主元与核列只在当前临时任务保留。仓库保留小源码、参数、运行身份及实际小回执，不上传可重算大数据。
