# R150：完整原坐标高核商的八个正指数及长度 26

作者：Astra-ISP-789f / normal_annihilator。AI 辅助，模型 GPT-6 Astra Pro。

## 1. 已完成结论

在同一原自然无穷远矩阵、同一所选输出 $I$ 和来源 $J$ 下，本次实际计算的完整高核商在
$R=\mathbb F_{31}[[u]]$ 上为
$$
\operatorname{coker}D
\cong (R/(u))^3\oplus R/(u^2)\oplus R/(u^4)
\oplus (R/(u^5))^2\oplus R/(u^7).
$$

因此该高核商有 8 个正 Smith 指数
$$
1,1,1,2,4,5,5,7,
$$
长度为 26，最大正指数为 7。原 $202\times202$ 配对矩阵的常秩为 194，另外 194 个 Smith 因子为单位。全部 8 个正方向在第 7 阶实际退出；不是仅由先前长度差 26 反推其谱。

本结论已经包含两套完整原坐标运输：

- 202 条高源形式核保留全部 6188 个原来源坐标，至 $u^{21}$ 的 19406948 个原输出产品全部为零；
- 202 条外来源左形式核保留全部 1834 个原坐标，至 $u^{21}$ 的 7252608 个原 Koszul 产品全部为零；
- 两套 202 个规范自由坐标均完整核验为 $I_{202}$；
- 高商配对及每阶原 202 行单位消去产品全部保留并核验。

这完成了有限域分解
$$
243=66+2+149+26
$$
最后一项的完整原来源实现与实际 Smith 谱。本次没有计算对应的特征零高核商，也没有证明所选子式的最高系数为 $31$ 单位。

## 2. 实际运行与输入身份

实际 Actions run 为 43740928483，step 为 original-two-mapper-higher-quotient，执行源为
35d9b82b4be396ebee6455bf7ab11a285a5d4e29。退出码为 0。

数学时间为 16.187683781000032 秒；两个 native 的首次编译合计 4.837825502000214 秒，单独记时；外层墙钟为 21.10306201399999 秒。实际 Python-flint 为 0.9.0，数学预算 600 秒、地址空间上限 1024 MiB。

实际回执：

[43740928483-original-two-mapper-higher-quotient.json](../notes/r150-source-kernel-session-789f/43740928483-original-two-mapper-higher-quotient.json)。

原临时完整回执为 29987 字节，SHA-256：
e8c1c44941b1da567bd96e1744f5a470b0c6e7cd3b1de346e74bc22c813904ce。

本次数学绑定：
cf5394c4c557bc98dea3917ce61ed7ebc62c80d3d9050204e976aff2037d1344。

总入口：

[2026-11-15-r150-original-two-mapper-higher-quotient-runner-789f.py](../notes/2026-11-15-r150-original-two-mapper-higher-quotient-runner-789f.py)。

该冻结源码 29018 字节，SHA-256：
b5b2bcd1f5ff2a04c729afcdfb8afea6e09948ce7bdd466a66bc0f90bad7eae3。

先前两个正规小映射的实际输入、完整逐系数身份和独立精度损失已经在
[两个 202 维正规映射及独立精度回收](R150-appendix-two-regular202-mappers-and-independent-precision-recovery.md)
中登记。它们在本次直接复用，没有重算原大消元或先前 full32/O35。

## 3. 两个原坐标运输实际完成

高源 native 从同一原 4340 常单位出发。3333 预基的自然尾不是被假设为单位阵的零尾：实际保留并核验了 1711875 个严格降 moment 次数 1 的尾项，同时核验后继 1007 单位产品。原 F/B/G 轨迹与原来源、输出字典均绑定。

程序对每个 $d=0,\ldots,21$，先以真实常单位回填原来源，再逐项验证
$$
\sum_{i=0}^{\min(10,d)}A_iK_{H,d-i}=0
$$
的全部 $4367\times202$ 个坐标。整层乘回完成后才保存该层和原子 ledger。高源 native 本身耗时 10.893192329 秒，原 19406948 个产品全部通过。

外来源左 native 使用同一 1603 常单位及其转置逆，对每个 $d$ 核验
$$
\sum_{i=0}^{\min(10,d)}O_i^T\Lambda_{O,d-i}=0
$$
的全部 $1632\times202$ 个坐标。原 1834 行无删除，原 202 自由坐标和整个 231 尾块均保留。外来源 native 本身耗时 0.80638177 秒，原 7252608 个产品全部通过。

两个 native 总计核验 26659556 个原产品坐标。总入口另逐文件核实际 SHA、完整 field header、全零产品和自由单位块，不只依赖 native 的布尔完成标记。

两个映射各自保留 $0,\ldots,21$ 项。高源小核使用 full32，独立精度损失 11；外来源左小核使用 O35，独立损失 14。原常单位回填不再除 $u$。随后逐项配对不会产生额外精度损失。

## 4. 高商的完整模块解释

取 $R=\mathbb F_{31}[[u]]$、$M=R^{6188}$、$V=R^{4367}$，并固定本课题同一原自然矩阵 $A$、同一所选来源 $J$ 和同一所选输出 $I$。令 $B=A_{I,J}$，$F=R^{J^c}$，$N=\ker A$，$\Psi=\Pi_{J^c}|_N$。

$B$ 在分式域可逆，因而 $I$ 对 $A$ 的分式域像单射，严格给出 $\ker A_I=\ker A$。同时 $\Psi$ 单射：若 $n\in N$ 的 $J^c$ 坐标为零，则 $B n_J=0$，故 $n=0$。于是有精确列
$$
0\longrightarrow\operatorname{coker}\Psi
\longrightarrow\operatorname{coker}B
\longrightarrow\operatorname{coker}A_I
\longrightarrow0.
$$

原 1632 条 Koszul 曲线组成的 $\Phi$ 是 $M$ 的原始直和项。此前实际尾单位子式使
$$
N=\operatorname{im}\Phi\oplus
j(E_{216}\ker(SE_{216})).
$$
本次高源映射 $K_H$ 是后一项的完整 202 列正规基。将 $O=\Pi_{J^c}\Phi$ 记为原外投影，完整 202 列左基 $\Lambda_O$ 的原自由块为单位；故 $\Lambda_O^T$ 满射且其核恰为 $\operatorname{Sat}(\operatorname{im}O)$。

这里 $\operatorname{tors}(\operatorname{coker}O)$ 确实注入 $\operatorname{coker}\Psi$。若 $v=\Psi n$ 且 $u^a v=Oq$，单射性给出 $u^a n=\Phi q$。由 $\Phi$ 原始得到 $n\in\operatorname{im}\Phi$，所以 $v\in\operatorname{im}O$。因此
$$
\operatorname{Sat}(\operatorname{im}O)\cap\Psi(N)
=\operatorname{im}O.
$$
对
$$
D=\Lambda_O^T\Pi_{J^c}K_H
$$
便有第二个精确列
$$
0\longrightarrow\operatorname{tors}(\operatorname{coker}O)
\longrightarrow\operatorname{coker}\Psi
\longrightarrow\operatorname{coker}D
\longrightarrow0.
$$
同一 $I,J$ 的已付长度严格给出
$$
\ell(\operatorname{coker}D)
=243-(66+2)-149=26.
$$

这也支付有限精度截止。由于 $\operatorname{coker}\Psi$ 是 $\operatorname{coker}B$ 的子模、$\operatorname{coker}D$ 又是其商，原 $u^{21}$ 消去子式余核的事实同时消去 $\operatorname{coker}D$。因此 D 的每个正 Smith 指数不超过 21。两映射各自完整保留到 21 阶后，配对不会另损精度；全部方向退出时便已得到完整高商谱。该论证从原精确列出发，不依赖将两个长度上界相减，也不把总长 26 当作跳过未完成方向的许可。

## 5. 实际配对、常单位消去及完整正谱

总入口使用同一有序 $J^c$，实际形成
$$
D_d=\sum_{i=0}^{d}\Lambda_{O,i}^T
(K_{H,d-i}|_{J^c}).
$$
所有 $D_d$ 均为原坐标的 $202\times202$ 矩阵。

实际 $D_0$ 秩为 194。选取真实常数单位行列后，程序逐阶形成规范源图 $Y(u)$，使 194 个原单位行的 $D(u)Y(u)$ 全部为零，8 个自由来源坐标严格为 $I_8$。剩余 8 行形成原 $8\times8$ Schur 系列。每阶都保存完整 $D_d$、$Y_d$、202 行产品及常单位逆。

该小 Schur 的实际逐层记录如下。表中的秩是这一层仍活动部分的常秩；指数是累计除 $u$ 次数。

| 指数 | 活动维数 | 实际常秩 |
|---:|---:|---:|
| 0 | 8 | 0 |
| 1 | 8 | 3 |
| 2 | 5 | 1 |
| 3 | 4 | 0 |
| 4 | 4 | 1 |
| 5 | 3 | 2 |
| 6 | 1 | 0 |
| 7 | 1 | 1 |

每次除 $u$ 之前，整个常数 Schur 残块先实际核为零。最后一行使 8 个正方向全部退出，因此无需继续产生第 8 至 21 阶的新配对。其完整和为
$$
3\cdot1+2+4+2\cdot5+7=26.
$$

规范化常单位源列为零基索引
$$
0,\ldots,191,\ 199,\ 201,
$$
相应 8 个自由源列为
$$
192,193,194,195,196,197,198,200.
$$
常单位目标行为
$$
0,\ldots,191,\ 192,\ 193,
$$
剩余目标行为 $194,\ldots,201$。这些索引属于本次完整 202 基，不是原 6188 来源编号。

## 6. 八维剩余块的原自由坐标

下表仅将已付原字典与本次规范自由坐标对齐。这是实际完整向量的自由坐标标识，不能把表中的单项式本身当作一条 syzygy，也不能丢弃这些完整向量在其它原坐标的系数。

原来源编号为 1 基，原式使用 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$。

| 高商自由源原编号 | 对应原式乘子坐标 |
|---:|---|
| 6119 | $\Gamma_4\,m_8m_{10}^2$ |
| 6120 | $\Gamma_5\,m_8m_{10}^2$ |
| 6131 | $N_{10}\,m_9^3$ |
| 6133 | $\Gamma_1\,m_9^3$ |
| 6148 | $N_{10}\,m_9^2m_{10}$ |
| 6150 | $\Gamma_1\,m_9^2m_{10}$ |
| 6165 | $N_{10}\,m_9m_{10}^2$ |
| 6182 | $N_{10}\,m_{10}^3$ |

8 个目标自由原坐标为
$$
6136,6137,\ 6153,6154,\ 6170,6171,\ 6187,6188.
$$
它们按相同字典恰是 $\Gamma_4,\Gamma_5$ 各乘
$$
m_9^3,\quad m_9^2m_{10},\quad m_9m_{10}^2,\quad m_{10}^3.
$$
这一对齐是已发布小回执及已核字典的直接读取和整数索引解码，不另称一次 Actions 数学运行。

## 7. 小证书与恢复身份

| 临时证书 | 字节 | SHA-256 |
|---|---:|---|
| source/high202-receipt.json | 3443 | 86179f0b12b9f29fd8647efe6a17032b0ee2e4bfc7e24ab04ae2b125fe337942 |
| outside/outside202-receipt.json | 2095 | e752d4a53e6857cb45df33f1f750bd7944eb4e8172eb86e75bd1c78b7f226197 |
| quotient/constant-higher-quotient-unit-profile.json | 1899 | efbd337b65f30cef4c3ffc317afd3e8407eb16367a5adc729b30264056e6fe07 |
| quotient/complete-quotient-layer-ledger.json | 3970 | 0b9fbb935805097ea12fe64ef7aa3cffedc0b918a93ace837a1900070e85f97a |
| quotient/complete-original-higher-small-smith.json | 3188 | 68c3cf085e212f03859ff807952e82ba493a318b9f4e4c426f0c3551013ad0e6 |

完整临时 manifest 保留每个原运输层、零产品、配对层和回代图的散列。所有大数组仅保存在该 job 临时目录；长期提交源码、参数、实际 run 和小回执即可重建。

本次实际 outcome 为 complete-original-higher-kernel-field-smith。完整原运输、全部原产品、完整高核模块和完整有限域 Smith 的成功字段均为 true。这里不是时间耗尽前缀，也不是仅一个选定子族的像秩。

## 8. 特征零范围

此谱只在 $\mathbb F_{31}[[u]]$ 上已经付清。此前精确构造的 13 条特征零原始左核及 $\lambda_{I,\mathbb Q}=2$，并不自动给出本次 202 条高源形式核在 $\mathbb Z_{(31)}[[u]]$ 上的共同正规基。有限域各原乘回通过也不支付这一基变换。

因此本次 characteristicZeroHighSmithComputed、characteristicZeroFullSmithComputed 和 selectedLeadingCoefficientUnitProved 仍全部为 false。后继若计算特征零 $8\times8$ 或其它小表示，必须先付其真实特征零原来源、共同坐标运输及适用的规范化；不能直接将本次有限域 194 个单位或 8 个正指数搬到特征零。

同样，长度分解并不把当前条件性的特征零来源界变成已解成员性。本次新增的是原高商的完整有限域结构及一个实际只需 8 个正方向的后继定位。
