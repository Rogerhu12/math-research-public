# R150 continuation：参数 2 的完整原投影谱与横向来源商长度上界 18

作者：Astra-ISP-789f / literature_audit。AI-assisted，GPT-6 Astra Pro。2026-11-15 UTC。

状态：原参数 $s=2$ 的真实 $224\times155$ 投影已经完整求出。它的九个正 Smith 指数为 $1^7,2,3$，总长度准确为 $12$。这与负六参数的投影谱相同，但当前参数 2 的完整原模块上界仍为 $30$，所以本轮只推出横向平方来源商长度不超过 $18$，没有证明或否定原 $h_0$ 九目标在此处的局部成员性。

## 1. 原来源与真实投影

取

$$
R=\mathbb Q[s]_{(s-2)},\qquad t=s-2,\qquad
V=R^{4367},\quad L=A(s)R^{6188}.
$$

$A$ 始终为原 17 式乘全部总次数不超过 3 的单项式所得的原完整来源矩阵。原二项式矩变换后记

$$
I=(z_2,\ldots,z_{10}),\qquad W=(I^2)_{\le5},\qquad\pi:V\to V/W.
$$

$W$ 的秩为 4212，商目标的秩为155。原九目标准确是 $t_j=z_j^2$，而非线性横向坐标。

[原参数 2 点分类](R150-appendix-rank-one-physical-mean-at-two-full-critical-emptiness.md)已付完整常数秩4345和投影常数秩133；原 generic rank 分别是4354和142。此次计算在自然参数 $t=s-2$ 中保留全部原来源投影：

- 170 个原纯乘子行；
- 54 个实际 $g(s)c^ad^{b+2}z_j$ 行，$a+b\le2$；
- 全918个原一次横向乘子行逐项与这些 $g$ 倍行核对；
- 其余5100个原来源按横向次数投影恒为零。

实际

$$
g(2+t)=-64t-72t^2-24t^3-2t^4,
$$

原纯向量 $g d^2\eta$ 的零基编号6坐标满足 $\eta_6(2)=1024\ne0$。双向生成只除该局部单位，始终没有除 $g$。因此这确是 $\pi L$ 的完整呈现，未扩大接触点的来源模块。

## 2. 实际完整 Taylor–Smith 谱

常数单位 Schur 的实际记录为：

| 阶数 | 当前形状 | 本阶实际秩 | 累计秩 | 已确定长度 |
|---:|---:|---:|---:|---:|
| 0 | $224\times155$ |133|133|0|
| 1 | $91\times22$ |7|140|7|
| 2 | $84\times15$ |1|141|9|
| 3 | $83\times14$ |1|142|12|

每一阶段只解真正的常单位右端，保全部剩余行列，完整乘回全部 Taylor 卷积；只有确认整个 Schur 常数项为零后才除 $t$。三阶时已达到原 generic projection rank142，剩余 Schur 系数全部为零。故

$$
\operatorname{tors}((V/W)/\pi L)
 \simeq (R/(t))^7\oplus R/(t^2)\oplus R/(t^3),
$$

自由秩为13，投影总长度准确为

$$
\delta_{P,2}=12.
$$

这已经是完整投影谱。提高此同一投影的 Taylor 阶数不会把长度12变成29；先前17阶入口的时间上限中断不参与本结论。

## 3. 对原完整模块的准确结论

[原局部投影长度差及参数 2 上界](R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)已经证明

$$
\delta_{A,2}\le30.
$$

其中30来自原模31长度32先剥去已付 $E_8^2$ 的碰撞：$E_8$ 首项为31单位，$E_8(2)=13888\ne0$，而其模31约化在2含一个一次因子。该上界仍保留全部原最大子式。

原 generic 来源已包含 $W_{\mathbb Q(s)}$，因此

$$
0\longrightarrow T_2:=W/(L\cap W)
\longrightarrow V/L
\longrightarrow(V/W)/\pi L
\longrightarrow0
$$

中的 $T_2$ 是有限长度挠模，且

$$
\operatorname{length}_R T_2=\delta_{A,2}-12.
$$

结合上界，当前严格结论为

$$
12\le\delta_{A,2}\le30,\qquad
0\le\operatorname{length}_R T_2\le18.
$$

特别地，有限长度准则给出一个已付但保守的统一局部来源包含：

$$
(s-2)^{18}W\subset L.
$$

原

$$
h_0=s^3(s-2)F_+^2F_-^2E_8
$$

在本点恰有一阶零点，因为实际

$$
F_+(2)=-4,\quad F_-(2)=3172,\quad E_8(2)=13888,\quad
\left.\frac{h_0}{s-2}\right|_{2}=17886115659776\ne0.
$$

长度差不超过18尚不足以推出 $(s-2)W\subset L$，更没有给出任何 $h_0t_j\notin L$ 的障碍。小回执中相应充分条件的布尔值为 false，含义仅为本充分条件未达到，不是成员性否定。

[负六参数](R150-appendix-minus-six-local-smith-length12-and-original-nine-target-membership.md)有不同的完整上界12，因而在那里可夹得 $T_{-6}=0$。不能把该完整上界搬到参数2。

## 4. 实际回执与来源身份

运行 **43729338969**，步骤 **two-original-projected-order4**，执行来源 commit：

22889e90bc66c833bac107fb562f254c7cb63758。

[实际完整小回执](../notes/r150-local-projection-session-789f/43729338969-two-original-projected-order4.json)记录：

- exit code 0；
- 数学时间4.637497190000005秒，墙钟4.727798578000005秒；
- 原临时回执8820字节；
- 原临时回执 SHA-256：9c965a0846e84cd6dc3e0302319da87c7cc7f1ed45933633b6190a66627dd5c4；
- 全17式、170纯行、918一次横向行、5100高横向行，以及全部Taylor Schur身份均通过；
- 未重算完整原Macaulay矩阵、旧正常形或任何新有限域rank。

[本点独立源码](../notes/2026-11-15-r150-two-original-projected-local-smith-789f.py) SHA-256：

867cc7f715913b6cd3dc5b8bcdd84969fee765df0930593e9066ebda26417e8f。

本次实际参数为最高Taylor阶4、共享时间90秒、内存1024MiB。generator和单项式actions的固定SHA分别为2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186与2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332。

原 $P_0,\ldots,P_4$ 的逻辑 SHA-256：

- 46524385c6d85965c82a11def39150c5144cb824ea240e101193146e206cae75；
- 3eca3953de350e5ca4509424ed8e954b89d8b696c4f0c3279a7490fdf36a549b；
- 235a1d86f53178784248e8844b28995c5eea3fa2ef50fda9de0b9566a833fd62；
- 4bf62186e323ea5620029324293f2e5509c95a6b8acc48afeb75d506cce5d421；
- 68f05d229f0814dfb561ea3879dd48d0347ff9456d755bae5a2f4fbdfd2c92a4。

## 5. 后续所需的新信息

此同一投影已算完。进一步提高原九目标结论，需要缩小完整 $T_2$ 的实际长度或最大指数，或者直接研究九个指定平方在该完整商中的类；继续同一投影的高阶展开不能提供这项缺失信息。

其它数域点若给出更强的真实 $E_8$ 公共因子，可以按已付整除论证减少参数2的模31碰撞上界，但不得预设那个数域结果。本文不宣布全局 $\mathbb Q[s]$ 成员性，也不改变原 Hilbert 空间问题的开放范围。
