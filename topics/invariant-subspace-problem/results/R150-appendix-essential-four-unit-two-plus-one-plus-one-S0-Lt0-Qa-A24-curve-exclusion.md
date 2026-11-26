# R150 / S0 / Lt0：同 eta 投影中整个 A24 曲线的排除

状态：**已证明**。新原 $Q_5/Q_4$ 投影的整个 $A_{24,20}(e,k)=0$ 曲线在剩余 S0/Lt0 原图上为空。因此该原投影现在只剩 $C_{83,64}=0$。本条没有排除一般 S0/Lt0。

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127；2026-11-27（台北）。

## 1. 完整原投影覆盖

使用原低不变量坐标 $e=u-1,k=Q/e,v=4kbc\,t$，及

$$j=k+2-2e,\quad x=k+4,\quad D_3=4e^3-3e^2k-4e^2+ek^2+4ek+4e-k-4,$$

$$\Omega=2e^2-ek+2.$$

沿用已登记的原三 mean/Cramer 必要式 $P_{045},P_{035}$、原 Dixon 差商必要式 $D_8$，以及[同一 eta 原配对/范数组合产生的](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-same-eta-quartic-leading-zero-exclusion.md) $Q_5,Q_4$。新两式的原来源为

$$D\{U^2D-2(1-ek)B^2\}=M_a(UD+2j\eta B)+2B^2M_n,$$

经原三 mean 的带来源返回，再分别与原 $N_1$ 行及两个均值重叠行取 Cramer 行列式。未另外选择 eta 的嵌入。

自含源重新从原 Gram 和正确双点乘法构建以上输入，并核回原组合与全部已付除法。完整二参数分解为

$$\begin{aligned}
\operatorname{Res}_v(P_{045},D_8)
={}&c_D k^{20}(ek-1)^4D_3^{26}x^6(4e-k-4)^8(4e-k)^2\Omega^4
F_{38,32}H_{33,21}^{2},\\
\operatorname{Res}_v(Q_5,Q_4)
={}&c_Q k^6D_3^{10}x^3(4e-k-4)^6(4e-k)^4
A_{24,20}C_{83,64},
\end{aligned}$$

其中 $c_D,c_Q\in\mathbf Q^\times$，全部显列的前因子已支付。下标为 $(e,k)$ 双次数；所有未支付的非恒定因子都已列出。源逐项重建完整因子乘积。

$A_{24,20}$ 有 309 项，其 SHA-256 为

`790a5288f75d73b55c34304a38d9aac5c223e5a816c15d2cffa69cb1903a987e`。

这里取这个完整因子为待排除曲线，而非把多个多元方程的 gcd 当作共同零点覆盖。任何原解在该曲线上同时满足

$$A_{24,20}=0,\qquad F_{38,32}H_{33,21}=0.$$

## 2. 真有理一元的有限参数覆盖

分别取完整 $k$ 结式

$$T_H(e)=\operatorname{Res}_k(A_{24,20},H_{33,21}),\qquad
T_F(e)=\operatorname{Res}_k(A_{24,20},F_{38,32}).$$

它们非零，次数为 744 和 888。实际在 $\mathbf Q[e]$ 内得到并逐步乘回以下完整已付因子拆分：

$$T_H=e^{72}(e-1)^3(e+1)^{254}(e-\tfrac12)^{98}\,C_H(e),\qquad \deg C_H=317,$$

$$T_F=e^{30}(e-1)^{18}(e+1)^{248}(e-\tfrac12)^{110}\,C_F(e),\qquad \deg C_F=482.$$

常数因子吸收到 $C_H,C_F$。$e=0,-1$ 是原单位零点，$e=1$ 和[整个 $e=1/2$ 原纤维](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-ehalf-original-exclusion.md)已经分别排除。故每个待排除原解必须满足实际有理多项式

$$C(e)=C_H(e)C_F(e)=0,\qquad\deg C=799.$$

整个 $C$ 的系数实际在 $\mathbf Q$ 内生成，SHA-256 为

`07727ffe8982e849a00cf675c7a01fe305b11303c1b1f5d4bf81761b54431a87`。

此处未除以 $A,F,H$ 的任何 $k$ 首项；它们的全部降次纤维都在完整结式中保留。

## 3. 第三个原投影给出严格特征零矛盾

再用原 $P_{045},P_{035}$ 的完整 $v$ 结式。源在 $\mathbf Q[e,k]$ 中实际生成并核回

$$\operatorname{Res}_v(P_{045},P_{035})
=c_R k^{14}D_3^{11}x^2(e+1)^6(4e-k-4)^4(4e-k)^3\Omega\,R_{132,109},$$

其中 $c_R\ne0$，前因子全部已付。因此所有剩余原解还满足 $R_{132,109}=0$。剥除后的多项式 SHA-256 为

`eda457be0935386401451ddf8b2d09410dc6ea5a6d263c9a3e415de36eec1f96`。

定义完整的有理一元结式

$$S(e)=\operatorname{Res}_k(A_{24,20},R_{132,109}).$$

任何待排除原解都必须同时使 $C(e)=S(e)=0$。这里不需要展开 $S$ 的大有理系数；可以严格计算它的完整约化并验证它与实际 $C$ 互素，具体如下。

取 $p=1031$，令 $\mathbf Z_{(p)}$ 为分母不被 $p$ 整除的有理数环。源逐个核验 $A,R,C$ 的所有系数属于这个环。它还核验

$$\deg_k A=\deg_k\overline A=20,\qquad
\deg_k R=\deg_k\overline R=109,$$

$$\deg_e C=\deg_e\overline C=799.$$

前两项保证以完整 $20+109$ 阶 Sylvester 矩阵计算时，约化与行列式交换；约化后没有擅自缩小原结式的次数。因此源实际算得的

$$\overline S=\operatorname{Res}_k(\overline A,\overline R)$$

确为完整 $S$ 的系数约化，次数 3116。最后在 $\mathbf F_{1031}[e]$ 内实际核回

$$b(e)\overline C(e)+c(e)\overline S(e)=1,$$

$$\deg b=3115,\qquad\deg c=798.$$

该 Bézout 系数对的 SHA-256 为

`2b9a06010223b92f593c0da3b93d1b5756aec6a7457d52549a7d62bbb70cd4db`。

**为何这足以推出特征零互素。** 若某个正次数首一 $g\in\mathbf Q[e]$ 同时整除 $C,S$，由于 $C$ 的全部系数在 $\mathbf Z_{(p)}$ 中且其首项是该环的单位，Gauss 引理使 $g$ 也可取为 $\mathbf Z_{(p)}[e]$ 中的首一多项式。于是 $\overline g$ 保持正次数。对 $S$ 作首一 $g$ 的多项式除法不引入非单位分母，故 $\overline g$ 还整除 $\overline S$。这与上述实际乘回一的 Bézout 身份矛盾。因此 $\gcd_{\mathbf Q[e]}(C,S)=1$，二者没有共同复零点。

此论证只利用一个**真实有理一元有限覆盖**和另一个完整一元结式的精确约化。它没有从多变量模素数单位理想推出有理单位理想，也没有略去可能逃往无穷远的参数：真实 $C$ 的 799 次首项约化不消失正是控制该问题的必要检查。无需知道 $S$ 的 $e$ 次数是否保持，因为该次数并未用于让公因子保持；保持公因子的是首项为单位的 $C$。

因此整个 $A_{24,20}=0$ 曲线不含剩余原解。由完整 $Q_5/Q_4$ 投影，剩余原解必须满足 $C_{83,64}=0$。

## 4. 实际执行

自含源：`notes/2026-11-27-unit211-S0-Lt0-Qa-A24-curve-original-return-8542.py`。

- 33,151 字节，SHA-256 `e3fec4da9b7064faf25ccc1460a03d13f7f972ad9d4df1fd57ee47909d84f9eb`。
- 无参数；Python 3.12.14、python-flint 0.9.0；180 秒 alarm、4 GiB 地址空间上限。
- 实际退出码 0；外部墙钟 58.803022 秒，源内 58.705388 秒；最大 RSS 131,608 KiB。
- stdout 22,941 字节，SHA-256 `0fad5f623b281fc0b2b1f1d7befe67697cd4101727476994284b7f3db54cede6`。
- 回执：`notes/2026-11-27-unit211-S0-Lt0-Qa-A24-curve-execution-8542.json`。

完整源不读取 scratch 数据；原式、全部因子、有限覆盖和最终乘回一证书都由源即时重建。一般 S0/Lt0 的剩余 $C_{83,64}$、原全理想幂来源和普通 Hilbert ISP 仍未完成。

后续对C83与H33的完整QQ投影曾真实触发120秒SIGALRM，未返回结式；准确[失败回执](../notes/2026-11-27-unit211-S0-Lt0-Qa-C83-H33-projection-failure-8542.json)保留，不能作排除证据。转用原N1/Qa低次主子式及同点重建，不重跑该大输入。
