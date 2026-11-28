# 正确 Phi 的 f=u 支：同点原列返回 C92，至多 261 个不同权对

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：本条准确原覆盖已证明。**

## 1. 定理与范围

在当前正确 $\Phi=0$、$D_{\mathrm{val}}\ne0$、非零孤立均值的 unit211 图，限制到 $f=u$。此前[整 t=0](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)与[整 u=3/2](R150-appendix-unit211-Phi-zero-fu-entire-u-three-half-original-exclusion.md)已关闭。

沿[原单 y 曲线](R150-appendix-unit211-Phi-zero-true-fu-single-y-common-weight-curve.md)，令
$$
s=u-1,\quad\delta=1-Q,\quad
L=Q-2s(u-2),\quad K=Q+4s,
$$
$$
M_n=2uL-L^2-u^2Q,\qquad y=4s^2-Q+2L\lambda .
$$
当前计算只用原单位 $Q\delta sKLM_n(2u-3)$，没有 y 首项或权范数逆。

本次新同点原列计算实际给出非零 $C_{92}(u)$，满足
$$
\boxed{\deg C_{92}=92,\qquad C_{92}^{13}\in I_{\mathrm{original}}.}
\tag{1}
$$
该身份在原已付系数环上的多项式理想中成立，不将原分母视为整数多项式常数。完整 QQ 因式分解的平方自由支持次数为 88。再引用独立的原零基点 mean 排除，去掉其 u 因子后，当前原点必须落在一个平方自由 87 次纯 u 支持上。

由于同一点还满足对 Q 首一三次的 $\Psi(u,Q)=0$，得到
$$
\boxed{\#\{\text{不同 }u\}\le87,\qquad
       \#\{\text{不同 }(u,Q)\}\le261.}
\tag{2}
$$
全部这些权零纤维保留。没有把 (2) 扩大为完整原几何点数界，也没有宣称整个 f=u 或 Phi 分支已空。

## 2. 已付原三次与新的同点条件

先前实际原 cofactor 给
$$
\begin{aligned}
\Psi={}&Q^3+(-10u^2+24u-15)Q^2\\
&+(32u^4-152u^3+276u^2-228u+72)Q\\
&-32u^6+224u^5-672u^4+1104u^3-1040u^2+528u-112
\end{aligned}
\tag{3}
$$
属于同一点原五值理想。此前三个 cofactor 恰成比例，单靠它们只有这条权曲线；本次没有重算这三个 cofactor。

记五个真实原值为
$$
E=E_{\mathrm{Be}},\quad O=E_{\mathrm{Bo}},\quad
N=N_1,\quad S=N_S,\quad P=P_S.
$$
清除原已付分母与已付行内容后，得到多项式
$\widetilde E,\widetilde O,\widetilde N,\widetilde S,\widetilde P$。
前三条对 y 至多二次，后两条至多三次，所有原尺度均逐项乘回。

新的二十四个原列是
$$
Q^i\{\widetilde E,y\widetilde E,\widetilde O,
y\widetilde O,\widetilde N,y\widetilde N,
\widetilde S,\widetilde P\},\qquad i=0,1,2.
\tag{4}
$$
每列先按首一 (3) 作真正 Q 短除，返回
原式等于商乘 $\Psi$ 加余式。把余式放入固定十二坐标容器
$$
\mathcal V=
\bigoplus_{\substack{0\le i<3\\0\le j<4}}
\mathbb Q[u]\,Q^iy^j.
\tag{5}
$$
这里仅将 (5) 作为原多项式的固定次数自由容器。没有支付 $y^4$ 的约化，也没有将它冒充为完整 y 商或自由结合代数。

首一 Q 短除保全部复嵌入和非约化纤维，没有通过因式选取丢掉任何 Q 分量。

## 3. 实际原满秩与目标 1

在 $\mathbb Q(u)$ 中选原列并消去，每条新边先完整返回十二坐标的多项式身份
$$
g\,v_{\mathrm{new}}
=b\,v_{\mathrm{old}}-a\,v_{\mathrm{pivot}},
\qquad a,b,g\in\mathbb Q[u].
\tag{6}
$$
每个原种子、每个除去的 pure-u 内容和每个终端组合分母都保存在原 DAG 中。任何这些中间主元都没有被宣布为物理单位。

实际只处理 (4) 的前十八列，即 E、O、N 及其 y 倍再乘 $1,Q,Q^2$，已经达到十二维满秩。源码随后对常数目标 1 返回完整十二坐标等式，余式真实为零。没有使用高次 y 约化，亦未进入备用的正 $D_{\mathrm{val}}$ 目标。

终端组合的实际可达 DAG 共 60 个节点。其全部原边及终端分母 LCM 次数为 103；最大可达深度加一为 13。因此由 (6) 的实际深度归纳，
$$
\delta_u^{13}\in
(\widetilde E,\widetilde O,\widetilde N,
 \widetilde S,\widetilde P,\Psi).
\tag{7}
$$
原五行尺度只含已付权，$\Psi$ 又已有完整原理想来源，故剥 $\delta_u$ 的已付支持后得到 (1)。

这是原列在同一个 y 点的完整组合，加入了先前比例标量 cofactor 没有支付的共同值约束。泛型满秩只用于构造此组合；所有未付 pure-u 极点由 $C_{92}=0$ 完整保留。

## 4. 精确因式与 u=0 的独立来源

实际完整 QQ 因式分解为
$$
C_{92}=\gamma\,u^4(u-2)^2
 (2u-1)F_2F_3F_{7,a}F_{7,b}
 F_{9,a}F_{9,b}F_{9,c}F_{11}F_{13}F_{15},
\tag{8}
$$
其中 $\gamma\ne0$，下标给出各不可约因子的次数，未写出的幂全为一。低次两个因子为
$$
F_2=2u^2-4u+1,\qquad F_3=2u^3-8u^2+12u-7.
$$
完整乘积和平方自由支持的适当正幂整除均实际乘回。未去 u 因子时，平方自由支持次数为 88，对应原运行直接输出的 264 个权对上界。

原 $u=bp+cq$ 正是基点 mean $d_0$。[独立的零基点 mean 全排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)已经在真实 Frobenius 乘法下证明 $pq(bp+cq)\ne0$，其自含旧源明确使用真正 $\operatorname{mul}(d,d)$，不依赖本会话已撤回的错误 compact E1。

当前 $p=1+\rho,q=1-\rho$ 且 $pq=Q\ne0$。以非零 p 同步缩放原 Gram 和孤立列，得到旧稿的 $p'=1,q'=q/p$，其基点 mean 为 $u/p$。原 mean、N/P、完整物理秩条件在该非零缩放下保持，故旧完整 $d_0=0$ 排除准确支付当前 $u\ne0$。旧稿还覆盖全部 $q'=\pm1$ 边界；不存在因规范变化漏掉的支路。

所以从 (8) 删去 u 的平方自由一次支持，余支持次数恰为 87。其所有未付根仍保留，包括 $u=2$、$u=1/2$ 以及所有非线性因子。式 (3) 首一，任一固定 u 至多有三个不同 Q，从而得到 (2)。这里没有把 u=0 的物理排除误写成裸均值理想的常数证书。

## 5. 可再生参数与唯一实际回执

不保存可重算的大因子系数载荷。新纯 u 支持由冻结源、原列 (4)、确定消元次序及最终实际分母 LCM 唯一重建：

| 对象 | 次数 | SHA256 |
|---|---:|---|
| 实际 DAG 分母 LCM | 103 | 6df08c5bc26002d21192dc5d6b35ab5f772cc9163d7a21bd82609e241d2eda25 |
| $C_{92}$ | 92 | b5734ddd5b9e817918d65e41c32eaf20430c38785428cd0dce3ea901d0612e7d |
| 原运行平方自由支持 | 88 | a97425846cca6f9b8634fe74b47ea49d730ba34e08bb2cd7a69e592346d8d3a3 |

- [唯一新源](../notes/2026-11-28-unit211-Phi-zero-true-fu-same-point-twelve-by-twentyfour-8542.py)，Git blob 2d054ee9b45fe69103e83b5335a4d2786d769ead，SHA256 e35e019e9ee84448b8e4e5afc31c81f449b8b515598329e2fb8c2e38d4870aa6。
- [输入说明](../notes/2026-11-28-unit211-Phi-zero-true-fu-same-point-twelve-by-twentyfour-8542.md)与[小回执](../notes/2026-11-28-unit211-Phi-zero-true-fu-same-point-twelve-by-twentyfour-8542.execution.json)。
- Actions run 46118971095，job 140899028896；内层 exit 0，0.470012789 秒，41612 KiB。
- 源提交与实际 pull 均为 46fd2e364a6459d12d88ca7f6d9cf591156e715c；2026-11-28 06:57:48.313274 UTC，两 README 无变化。
- stdout 8334 字节，SHA256 bbcca9f762dc371de8f8ca305279fad7551cd09ba03df78b8c6f9a6034d50fe8。

实际记录包含 25 次完整 Q 首一短除、152 个短除步、312 个容器坐标、216 个种子坐标、720 个新边坐标、72 个零边坐标及 12 个目标坐标返回；共有 3672 次多项式精除。所有后续权纤维仍须由新的原条件处理，本定理不以有限候选替代原排除。
