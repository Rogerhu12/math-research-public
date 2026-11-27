# h=k 的三次权曲线：同点原一次因子剥除与完整 66 次参数覆盖

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。实际运行日期为 2026-11-27 UTC。

## 1. 完整结论与原域

沿用[整条 P 曲线的原 Delta 平方返回及 1474 次覆盖](R150-appendix-unit211-collision-P3-original-Delta-square-and-complete-1474-parameter-cover.md)。当前仍是原 h=k、Delta 非零的已付图，并满足同一个准确因子
$$
P(\lambda,u)=P_{25,3}(\lambda,u)=0.
$$
原 $P$ 对 $u$ 三次、对 $\lambda$ 二十五次，其不可约性与所有系数已由[两条原 QQ 投影](R150-appendix-unit211-equal-singleton-two-original-QQ-projections-common-curves-and-finite-base-remainder.md)完整固定。

本次取得一个独立的首一、平方自由必要覆盖
$$
F_{66}(\lambda)=0,\qquad \deg F_{66}=66.
$$
它与此前 $F_{1474}$ 的完整 QQ gcd 仍为同一个 $F_{66}$。所有原 $P$ 点，包括全部真实输入分母零纤维与原 $Q$ 首项退化，都被这条 66 次覆盖包含。

故本部分至多有 66 个不同 $\lambda$、198 个不同 $(\lambda,u)$。结合此前两残余曲线至多 39195 个不同基点，当前整个碰撞 Delta 非零图的不同 $(\lambda,u)$ 至多
$$
198+39195=39393.
$$
这个数仍只计基点。所有原 $Q$ 纤维及完整个别 N/P 条件继续保留；本稿不宣称 Q 有限或整 P 曲线已排空。

## 2. 真正的 Delta/Tnum 公因子

使用此前真实三维权代数
$$
\mathcal A=\mathbb Q(\lambda)[u]/(P/g_3),
$$
其中 $g_3=[u^3]P$。保留整个代数，不假设它是域或约化。原 $g_3$ 零面及所有初始系数分母零面先进入参数图覆盖。

沿用原图定义
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,
$$
$$
w=\lambda-1-T,\quad S=2\xi+3-2\lambda,\quad
\eta=\xi+3-2\lambda,\quad V_2=2u-\ell Q,
$$
$$
T_0=V_2-2u^2,\quad J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
P_f=T_0(J-Q),\quad G=\lambda P_{02}-(1-u)T_0,
$$
$$
P_c=QP_{02}(\ell+T)-GT_0,\quad
N_F=(3-4\lambda)Q+J\xi\eta,\quad
N_C=\eta(-G\xi+Qwu).
$$
两条同点原值线的真实量为
$$
\Delta=\Phi N_F-S\xi P_f,\qquad
T_{\mathrm{num}}=P_fN_C-P_cN_F.
$$
它们在 $\mathcal A[Q]$ 中分别二次、三次。

新三步精确欧氏链对这两条低次原式给出首一一次式
$$
\Gamma(Q)\in\mathcal A[Q],\qquad \deg_Q\Gamma=1.
$$
实际完整返回
$$
\Delta=D_1(Q)\Gamma(Q),\qquad
T_{\mathrm{num}}=T_1(Q)\Gamma(Q).
$$
每个等式均核对全部三个权基底分量，所用逆也都实际乘回一。没有重新运行旧 $C_R,C_W$ 的长欧氏门。

在实际原点上，Delta 已由整零支原排除支付。只要本节真实系数的分母非零，$\Delta(Q_0)\ne0$ 直接迫 $\Gamma(Q_0)\ne0$。这是在同一个原 Q 上的单位来源，不是给某个无原来源的 gcd 因子强加非零。所有 $\Gamma,D_1,T_1$ 系数分母零纤维仍进入参数覆盖。

## 3. 四个原条件准确降为 Q 三次/四次

将此前同点四原式记作 $C_R,C_W,C_O,C_{N1}$。实际对每式完整返回
$$
C_i=\Gamma^2\,\widehat C_i,\qquad i=R,W,O,N1.
$$
相应 Q 次数为
$$
\deg_Q(\widehat C_R,\widehat C_W,\widehat C_O,\widehat C_{N1})
=(3,4,4,4).
$$
每次除法和最终平方乘积都在整个 $\mathcal A[Q]$ 中实际核回。因为前节给出了原点上的 $\Gamma\ne0$，在所述系数图上，原四式与这四条降次式同时为零等价。完整的 O、N1 条件并未因随后只选两对投影而删除。

这次没有把 Gamma 在整个权代数上的范数当作原物理单位；所需的只是在同一个原点的 Q 处不为零，以及完整保留它的参数分母。

## 4. 固定七阶原结式及瞬时计算主元零面

构造
$$
\mathcal R_W=\operatorname{Res}^{(3,4)}_Q(\widehat C_R,\widehat C_W),
\qquad
\mathcal R_N=\operatorname{Res}^{(3,4)}_Q(\widehat C_R,\widehat C_{N1}).
$$
这里上标固定原次数 3、4；两者都是七阶 Sylvester 行列式。

源码在 $\mathbb Q(\lambda)$ 上用准确除法递推计算这些行列式。若
$$
a=qb+r,\quad \deg a=m,\quad\deg b=n,\quad\deg r=r_0,
$$
则使用完整结式恒等式
$$
\operatorname{Res}(a,b)
=(-1)^{mn}\operatorname{lc}(b)^{m-r_0}
 \operatorname{Res}(b,r).
$$
每次除法都实际乘回，所有首项幂和符号保留。最终结果是固定次数 Sylvester 多项式本身，不只是某个去掉主元因子的泛型投影。

以下延拓区别是本结论的关键。令 $R$ 是仅倒置原 $g_3$、四降次输入、Gamma 精确身份及最终输出真实分母的 $\mathbb Q[\lambda]$ 局部化。则
$$
R[u]/(P/g_3)
$$
在 R 上自由三维，嵌入其 $\mathbb Q(\lambda)$ 标量扩张。因此，固定 Sylvester 多项式与递推所得结果既然在后者相等，它们在前者也相等。递推过程中临时倒置的主元不需要变成原点假设：只要真实输入和最终输出仍在 R 中，该多项式身份便跨过临时主元零点成立。

所以，某专门化点的 Q 首项下降，或任一瞬时欧氏主元为零，仍满足“同一个有限 Q 公共根迫原固定 Sylvester 行列式为零”。它们未被用来缩小物理域。实际输入、Gamma 身份和最终输出的分母零纤维则完整并入下一节的 chart，不能以这项延拓为由删除。

两条实际结果的最高系数 $\lambda$ 次数为 1014、1088；规范三分量编码 SHA256 分别为：

- 71ea9cb1917af5adf7a997a96bd92984c54da96ad0df2f8a0126fc93bb5ddb24；
- 614339c9354e1fa1d64b9ee4b6f5fe4203f4eed8849829df85d1346e5ec9f070。

## 5. 整三维权范数、完整 chart 与 66 次覆盖

对上述两个结式元素，在真实基底 $1,u,u^2$ 上形成三阶乘法矩阵，取整个代数的行列式范数。每个原三阶矩阵与其完整伴随矩阵实际相乘返回行列式倍单位阵。

两个范数的准确有理式分子、分母次数为：

| 原对 | 范数分子次数 | 范数分母次数 |
|---|---:|---:|
| R/W | 1677 | 704 |
| R/N1 | 1768 | 770 |

任一实际原点给出该三维权代数到复数的求值映射；同 Q 原根使对应结式在该求值下为零，故乘法算子不可能可逆，整个范数必须为零。此论证不要求权代数是域，也不删除任何范数零分量。

把全部真实图分母收进 $C_{\rm chart}(\lambda)$，实际其次数为 823。两范数分子在 QQ 上的准确 gcd 为 $G_N$，次数 1185，各除法均完整乘回。因此所有原 P 点必在
$$
C_{\rm chart}(\lambda)\,G_N(\lambda)=0
$$
中：chart 为零的完整异常纤维直接保留；其余点同时使两个范数分子为零，故使它们的一元 gcd 为零。

取这个乘积的首一平方自由部分，再只剥前文已付的标量 $\lambda,A,B,S,J_2$ 与该覆盖的实际 gcd，删除次数依次为 1、2、3、1、2，得到首一平方自由 $F_{66}$。没有剥任何未付的 Q 首项、u 首项、其它参数因子或只在某一权分量上非零的量。

本次又读取此前已经保存的完整 $F_{1474}$ 参数片，只将其作为数据使用。准确 QQ 扩展 gcd 返回
$$
aF_{1474}+bF_{66}=cF_{66},\qquad c\in\mathbb Q^\times,
$$
同时两个对应整除商都实际乘回；首一 gcd 的次数仍为 66。因此新的独立覆盖与旧完整覆盖的交集就是同一条 $F_{66}=0$。没有重新计算旧 1474 次泛型门。

## 6. 有限基点上界及其限度

原 P 的 QQ 不可约性与正 u 次数保证它作为 $\mathbb Q[\lambda][u]$ 的系数内容为常数。因此没有任何复 $\lambda_0$ 使 $P(\lambda_0,u)$ 恒等于零；每个固定 $\lambda_0$ 上至多三个不同 u，包括 u 首项下降的全部情况。

于是 P 部分至多 $66\cdot3=198$ 个不同基点。此前全覆盖为已闭 $J_2=0$、此 P 部分、或两条不同不可约残曲线的交点。后者的 39195 上界保持，故总数至多 39393。这不是非约化商长度、完整原解个数或 Q 候选个数。每个候选仍要在同一 $\lambda,u,Q$ 上返回原条件。

## 7. 精确小输入与唯一真实执行

源：[2026-11-28-unit211-collision-P3-low-Gamma-deflated-original-Q-norms-8542.py](../notes/2026-11-28-unit211-collision-P3-low-Gamma-deflated-original-Q-norms-8542.py)。

- 实际 source blob：0451d215b5e46930bf3e261b6645741a377681a8；
- SHA256：0c518251e0d96e67029eab21fd7f4135c5e6fb5acae78703754618488346a3c0；
- run / job：46048832386 / 140674782649；
- 内层退出 0，驱动墙钟 28.359331440 秒，峰值 117372 KiB；
- 数学末标记在 28.275373881 秒发出；
- 21 个准确原 Q 除法乘回，13 个整个权代数的真逆乘回；
- 除法组合 SHA256：9e0e068187b69892549d087645c634bdb44b28589a0a1bdf4a19d6478ee12e12；
- stdout 9387 字节，SHA256 cb33590d8537eca090e92356f728aac50805cc679266a8b7ba685da3dd7a4dac；
- 限额 180 秒 / 4 GiB，无重跑或延时。

真实 pull 于 2026-11-27 18:21:38.651333 UTC 从 aa94508e7cae1eb05cbd6ce65951867895dc398d 读到 bb97bcba0cc6806539be17bbde34c589b5fa17eb，两份 README 未变。

[完整 F66 小输入](../notes/2026-11-28-unit211-collision-P3-exact-66-cover-8542.json)为升次排列的 67 个准确有理系数字符串。原规范 JSON 为 1960 字节，SHA256
77134be0755d744c136fd627db8b5cbc1e7ee38f419658dbb99736d518d1ee06；
仓库文件加末行换行后为 1961 字节，SHA256
d54fabefc3b1b646dca9350ed5a0bf9d884282bb67ec381337f45f4c20273ea8。
全输入已经从真实日志的压缩文本解出，并核对长度、Adler 校验与上述 SHA。

[小执行回执](../notes/2026-11-28-unit211-collision-P3-Gamma-deflation-complete-66-cover-receipt-8542.json)保存所有数学阶段、chart 范围和实际退出状态。没有保存两条兆字节级结式或大范数系数缓存。后续可直接从 F66 的准确 QQ 因子进入原有限纤维，全部首项零面与同点原条件仍须保留。
