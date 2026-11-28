# R150：整个 H198 与原 P164 无共同曲线及固定完整原商长度界 49200

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 完整新结论

在当前 W 的原权域上，[N1 斜率定理](R150-appendix-unit211-W-N1-H198-weight-curve-and-two-generator-monic-square.md) 的整条 H198=0 与[全 W 原 native NS/PS 必要曲线](R150-appendix-unit211-W-entire-original-native-NSPS-necessary-weight-curve.md) $P_{164}=0$ 无共同曲线分量。

本次直接从完整原六行定义得到一个固定整模型见证，而非由模理想空性作 QQ 提升。由此：

$$
\dim_{\mathbb Q}\mathbb Q[e,k]/(H198,P_{164})\le4100.
\tag{1}
$$

在同一已付原域中，原均值商长度至多 24600；保留 $\rho^2=1-Q$ 的两种规范符号并返回完整 HA/HB 后，固定七坐标 $(e,k,\rho,x,y,t,\zeta)$ 的完整原商长度至多 49200。这些界包含非约化重数。

**本结论没有排除整个 H198 原支，也没有排除全 W。** 所有候选点的个别原 N/P 仍须同点返回。H198 不被加入全域权单位表。

唯一首次 run 46089073211、job 140805495228，内层真实 exit 0；源 11.764036160 秒，driver 11.840896530 秒，峰值 RSS 90232 KiB。

## 2. 两条权多项式的准确来源

H198 已由完整 QQ 因式返回证明不可约，双次数 $(14,19)$、总次数 25、198 项。其定义为原 N1 权行列式剥已付因子后的剩余乘以 $-288$：

$$
H198=-288\,\operatorname{remaining}(\Delta_N).
\tag{2}
$$

(2) 的参数定义 6434 字节，SHA-256 为

3569ba450503ee36acfed6f3ef047c3a08cf1735c3f95028a7c6b0f9b060db82。

原 native 六行按固定次序

$$
N_S,\ P_S,\ yN_S,\ tN_S,\ yP_S,\ tP_S
$$

在同一六生成元 $(1,x,y,t,y^2,yt)$ 上给出矩阵 $M_{\rm nat}$，每行都有完整原六式来源。旧已完成的固定 QQ 行列式证明

$$
D_{\rm nat}:=\det M_{\rm nat}
 =c\,U_{\rm paid}\,P_{164},\qquad c\in\mathbb Q^\times,
\tag{3}
$$

其中 $U_{\rm paid}$ 是当前原权单位，$P_{164}$ 双次数 $(97,123)$、总次数 164。原列第一项为 1，故伴随矩阵身份把 $D_{\rm nat}$、因而局部化后的 $P_{164}$ 放入同一原理想，而不只给集合上的必要性。

本次只再生 $M_{\rm nat}$ 的必要定义，其完整矩阵定义 SHA-256 为 e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf。没有重跑此前 95 秒的 QQ 行列式，也没有重跑 H198 的完整因式门或旧 H265 不整除见证。

## 3. 本次完整整模型与非零余式

先固定 $p=1009,k=3$，再开始任何行列式输出。源对完整 $M_{\rm nat}$ 与完整 H198 的每一个 QQ 系数分母作 p 单位检查，并检查 H198 有 p 单位系数。共记录 41148 次系数检查，包含构造与特化各自的检查。因此

$$
D_{\rm nat}\in\mathbb Z_{(1009)}[e,k],
\qquad
H198\in\mathbb Z_{(1009)}[e,k]\text{ 为 p 本原}.
\tag{4}
$$

在 $\mathbb F_{1009}[e]$ 中，从这个原矩阵直接计算固定六阶行列式。55 个 Bareiss 精确除法乘积全部返回。随后完整多项式除法实际给

$$
\overline D_{\rm nat}(e,3)=q(e)\overline{H198}(e,3)+r(e),
\tag{5}
$$

且 $q\overline H+r=\overline D_{\rm nat}$ 全部乘回成立。

| 本次确切对象 | e 次数 | 定义 SHA-256 |
|---|---:|---|
| 原特化行列式 | 195 | 0179d02b56ccce48191cc508b74dee78fadccc9fee71bdcc46e84c51f215f62c |
| H198 的特化 | 14 | 723fdda68a76f8b97d6bb72b4a3c440f8802be0d9ed79fbb96ea1a5d75a0d3a7 |
| 完整商 q | 181 | 91f85d98074889de512aab7b244d38e23fb45a70a20775cc770504856cfcbdf5 |
| 完整余式 r | 13 | 9f080c7c1e47fef98779c339e720aea523cd6badc42f2d39b390d9a7c477900f |

余式最高系数是 $540\in\mathbb F_{1009}^{\times}$，因此它实际非零。没有只核某个数值点，也没有把任何瞬时消元主元支付成原单位。源不输出系数数组；上述各对象由固定源定义与完整乘回唯一指定。

## 4. 从整模型到真正 QQ 不整除

假如 $H198\mid D_{\rm nat}$ 在 $\mathbb Q[e,k]$ 中成立，写 $D_{\rm nat}=H198\cdot Q_0$。由 (4) 和 Gauss 内容乘法公式，$Q_0$ 也属于 $\mathbb Z_{(1009)}[e,k]$：H198 的最小系数 p 赋值为零，而乘积的最小赋值非负。

因此整除身份可以模 p 并专门化 $k=3$，必迫 (5) 的余式为零，与实际最高系数 540 矛盾。所以

$$
H198\nmid D_{\rm nat}\quad\text{in }\mathbb Q[e,k].
\tag{6}
$$

这个论证既不要求 $k=3$ 对应原物理解，也不依赖某个 QQ 或模几何饱和为空。实际 H 的 e 次数确实保持为 14，但“非零余式反证全局整除”只需要完整 p 本原整性；它没有倒置 e 首项来排除其它纤维。

由 (3)，若 $H198\mid P_{164}$ 就必有 $H198\mid D_{\rm nat}$。故 (6) 直接给 $H198\nmid P_{164}$，无需先加入 H198 与 $U_{\rm paid}$ 互素的假设。H198 的已刊 QQ 不可约性于是给出

$$
\gcd_{\mathbb Q[e,k]}(H198,P_{164})=1.
\tag{7}
$$

式 (7) 只说明没有共同曲线分量，不表示多变量单位理想。其仿射有限交点及重数全部保留。

## 5. 4100、24600 与完整固定规范 49200

由 (7)，平面 Bézout 对总次数 25 和 164 的两条曲线给出 (1)，包括非约化结构。倒置已有纯权单位时，有限 Artin 代数只删除不满足单位条件的分量，不增加长度。

整个现有 W 的原均值代数已由 $(1,x,y,t,y^2,yt)$ 六个单项式生成，不要求自由。把它基变换到 (1)，再施加 NS/PS 或其它同点原式，故原均值环境长度至多

$$
6\cdot4100=24600.
$$

原规范 $\rho^2=1-Q$ 是首一二次，再增添 rho 最多乘二。剩下的 $\zeta$ 不增加另一个二次因子：在本图既有的 $D\ne0,\ell\ne0,m=u-\ell\ne0$ 条件下，完整 HA/HB 给

$$
Ms^2=D,\qquad 2mDs=K,\qquad
s=(\ell\zeta-T)/u,
$$

$$
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell T A_2+2T^3.
$$

因而

$$
\zeta=\frac{T+uK/(2mD)}{\ell}
\tag{8}
$$

唯一。所有 a,b,c,p,q、原 Gram 及其余规范值坐标都按同一原图由 $(e,k,\rho,x,y,t,\zeta)$ 恢复。式 (8) 的 D 局部化发生在已经有限的 Artin 环中；随后取完整原个别 N/P 的商，也不会增加长度。因此固定七坐标原商长度至多

$$
\boxed{2\cdot24600=49200.}
$$

这是固定 W 规范下的完整原商界，不是未经规范化矩阵的自由轨道数；也不把当前 D 非零图的单位结论移到一般 D=0 碰撞图。

## 6. 源、实际规则读取及保存范围

源：

[2026-11-28-unit211-W-entire-H198-vs-native-P164-fixed-integral-model-8542.py](../notes/2026-11-28-unit211-W-entire-H198-vs-native-P164-fixed-integral-model-8542.py)

实际 blob b9d649fb933c4545a09ce0cdab73877cea41e9db，9176 字节，SHA-256 为 fa703c6466eb776425ccec39125477555e118b2aea48c3c5289ed7c01c414a64。双计时接口都钳制到最初 180 秒绝对截止，地址空间上限 4 GiB。本次 source commit 为 73d062e38fd4d05330867da403d6ef0c5e299592。

2026-11-28 00:39:57.022125 UTC 已真实 pull 同一 main 提交，两 README blob 仍为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、5fbd905291dd044c88d35bd9c07ac0e586ff795a；差异为空。stdout 为 3341 字节，SHA-256 为 43bd11896fb6fe44ee5de0162e41c94d60e01a930aa6c487458ff5a12315ac5c。附[实际回执](../notes/2026-11-28-unit211-W-entire-H198-vs-native-P164-fixed-integral-model-receipt-8542.json)。

旧 6aadb 版本仅作首次派发前计时接口修正，从未执行。此前 publisher 网络 pull 超时没有启动数学门，不计为本输入失败。本次只保存小源、定义、SHA 与实际回执；没有保存或传送可重算大系数。
