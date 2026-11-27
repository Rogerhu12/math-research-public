# R150：一般 LS 原 Delta=0、W=0 图的整个 k=-1 权线排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**结论。** 在一般三值互异的原 LS 图，令原 P1/N(V) 两条线的行列式为 Delta。已经支付 Phi 及 W 对 ell 的首项后，原 `Delta=0, W=0, k=Q/(u-1)=-1` 的整个权线为空。因此后续 W=0 图可把 `k+1` 作为单位。这不关闭整个 W=0、一般 LS 或普通 ISP。

本证书从同一个原 Gram 重建四条二次式及两条加权原 N/P 三次式，在 QQ[e] 上得到完整有限覆盖；逐个回到整个 QQ 商代数。没有有限域推断，也没有把形式矩阵的右核列误当成真实单项式列。原 `x=u+1` 纤维全程保留。

## 1. 已付范围和本条权参数

接续[全局首一值二次式](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-Delta-zero-global-monic-value-quadratic.md)及[整个 W 首项零面排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-Delta-zero-W-leading-zero-exclusion.md)。原 u、u−1、Q、1−Q、bc、P02 是单位；在原 Delta=0 图 Phi 也是单位。W=0 上 `u(Q+2)-2` 的整个零面已闭。

写
$$
e=u-1,\qquad k=Q/e,\qquad V=(e+1)k+2.
$$
从 W=0 精确解出
$$
\ell=\frac{(e+1)((k+2)^2-2ek)}{kV},\qquad u=e+1,\quad Q=ek.
\tag{1}
$$
这里 `u(Q+2)-2=eV`，故 V 已付。源码实际核验 (1) 使 W 恒零，且
$$
P02=-\frac{2e^2(e+1)(2ek-k^2-5k-8)}V,\qquad
\Phi=-\frac{2e^2(k+4)}V,
$$
$$
M=\ell(2u-\ell Q)-u^2=-\frac{(e+1)^2 M_{13}}{kV^2}=4bc(1-Q).
$$
全部这些身份和源内 M13 的展开逐项乘回。

本条令 k=−1，得到
$$
Q=-e,\quad V=1-e,\quad
\ell=\frac{(e+1)(2e+1)}{e-1},\qquad
M_3=4e^3+7e^2+e-3.
\tag{2}
$$
以下且仅以下非常数权因子作为已付单位用于剥内容：
$$
e,\quad e+1,\quad e-1,\quad e+2,\quad M_3.
\tag{3}
$$
它们分别来自 Q/u、1−Q、V、P02、bc；ell 及 2e+1 均未倒置。

## 2. 同一个原 Gram 的 x,y,t 坐标

在完整二次代数 `r^2=1-Q` 中取
$$
p=1+r,\quad q=1-r,\quad
b=\ell/2+\frac{u-\ell}{2(1-Q)}r,\quad c=\bar b,\quad a=1-\ell.
$$
令 `X=x+yr, Y=x-yr`。用原 E0、N0 和 P1 依次恢复
$$
f=\frac{ux+(u-\ell Q)y-T_0/2}{2u},
$$
$$
\lambda=\frac{V_2x+(2u-uQ-\ell Q)y-uT_0-(V_2+2u^2)f+bcQt}{P02},
$$
$$
T=\frac{gT_0-P_f f-\Phi bcQt}{QP02}-\ell,
\tag{4}
$$
其中
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
P02=(2-3u)V_2-Qu+2u^3,
$$
$$
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,
\quad P_f=T_0(J-Q),\quad g=\lambda P02-(1-u)T_0.
$$
原 Gram 其余坐标为
$$
r_G=X-ap-ct,\quad s_G=Y-aq-bt,\quad
A_G=2f-2bX-2cY+2bc t.
$$
源码从原四行 Gram 计算 tau、乘法、三个 mean 条件及 N1 极化，实际核对 E0=0、`F2=2f`、`N4(row0)=2 lambda P02` 和原 P1 极化恒等式。只使用 (3) 及其一般 W=0 已付来源，未倒置 `x-u-1`、t 或任何 Gram 方程首项。

保留三条 mean 系数 `E1,EBe,EBo` 以及 N1，共四个 `(x,y,t)` 二次式。

## 3. 两条加权原 N/P 的来源

记
$$
A=2\lambda^2-2\lambda+1,\qquad B=4\lambda^3-6\lambda^2+3\lambda-1.
$$
对原四行定义源中原算子 N4 和 `P2(v)=tau((v-tau(v)1)^3)`；源码核 `P2(row0)=P02`。新增两条必要三次式为
$$
N_s=bN4(row_B)+cN4(row_C)-2\lambda P02(\ell+2T+A),
$$
$$
P_s=bP2(row_B)+cP2(row_C)-P02(\ell+3T+3A+B).
\tag{5}
$$
它们具有明确原理想来源。取原全局值坐标
$$
v_1=(T-\ell\zeta)/u,\quad v_0=v_1+\zeta,\quad
h=1+v_0+v_1r,\quad k_v=\bar h,
$$
$$
H_A=\ell M\zeta^2-2TM\zeta+V_2T^2-u^2A,
\quad H_B=u^2(B-2v_0A+(h-1)(k_v-1)T).
$$
源码逐项核验
$$
b h^2+c k_v^2=\ell+2T+A+H_A/u^2,
$$
$$
b h^3+c k_v^3=\ell+3T+3A+B+((3+2v_0)H_A-H_B)/u^2.
$$
从而对原 `N_B=N4(row_B)-2 lambda P02 h^2` 等式，实际回乘得到
$$
bN_B+cN_C=N_s-2\lambda P02 H_A/u^2,
$$
$$
bP_B+cP_C=P_s-P02((3+2v_0)H_A-H_B)/u^2.
\tag{6}
$$
因此原九式及值矩条件确实迫使六条 `E1,EBe,EBo,N1,Ns,Ps` 全为零。这里只用必要条件排空，不声称这六式与完整原理想等价。

原物理单位的最终返回也是实际身份：
$$
D=\ell A-T^2,\qquad D+\ell H_A/u^2=bc(h-k_v)^2.
\tag{7}
$$
原三值互异图中 HA=0、bc 非零且 h≠kv，所以 D 非零。

## 4. QQ[e] 上的完整 12 维覆盖

在 (2) 的整个权线上，仅按 (3) 剥去已付内容。四条二次式的 e 次数分别为 5、3、3、6，两条三次式的 e 次数均为 10。

把四个二次式乘以全部次数不超过2的十个单项式，把两个三次式乘以全部次数不超过1的四个单项式，得到 48×35 矩阵 M。35 列为 `(x,y,t)` 中次数不超过4的全部单项式，最后一列是常数1。48 条原乘法行全部重建回乘。

无分母消元只是寻找证书。对最后第40、41行，源码恢复两条真正的 QQ[e] 多项式 cofactor 行 c0、c1，并逐项核验
$$
c_i M=\delta_i e_{\rm const},\qquad \deg\delta_0=\deg\delta_1=128.
\tag{8}
$$
两条共70个列身份均实际相乘。故每个原点都满足 δ0=δ1=0，消元主元为零的纤维也包含在内；没有倒置117次秩子式。

QQ 一元扩展 Euclid 的完整两乘回给
$$
a_0\delta_0+a_1\delta_1=G_{73},\qquad\deg a_0=\deg a_1=54.
$$
G73 的完整分解为下式，非零有理内容略去：
$$
\begin{aligned}
G_{73}\doteq{}&e^{30}(e+1)(e-1)(e+2)M_3^8(4e+5)^3\\
&\cdot(4e^2+5e+3)^2(4e^2+6e-1)\\
&\cdot(6e^3+14e^2+11e+2)\\
&\cdot(16e^4+26e^3-e^2-11e-12).
\end{aligned}
\tag{9}
$$
完整因子乘积回乘 G73，所有已付因子的整除均回乘。按 (3) 去除单位，再取平方自由部分，得到整个原权参数的12次覆盖
$$
C_{12}\doteq (4e+5)(4e^2+5e+3)(4e^2+6e-1)
\cdot(6e^3+14e^2+11e+2)\cdot(16e^4+26e^3-e^2-11e-12).
\tag{10}
$$
源码核其次数12、与导数互素；首一 C12 的 SHA256 为 `349564fc817a821e560ada110e8bd8948278039b6f67038b5a46be0c90e7e345`。

## 5. 四个整个商代数中的原单位证书

分别在 `QQ[e]/(phi)` 中返回原48×35矩阵。每个逆由 QQ 扩展 Euclid 的两项乘回为1支付，不依赖挑选一个复嵌入或假设矩阵列自由。

| 完整 phi | 商代数维数 | 原矩阵秩 | 返回 |
|---|---:|---:|---|
| 4e+5 | 1 | 35 | 原行组合等于常数1列 |
| 4e²+6e−1 | 2 | 35 | 原行组合等于常数1列 |
| 6e³+14e²+11e+2 | 3 | 35 | 原行组合等于常数1列 |
| 16e⁴+26e³−e²−11e−12 | 4 | 35 | 原行组合等于常数1列 |

四条单位行均对原35列完整回乘。把真实单项式列代入，左侧为原式的组合，右侧为1；故这些因子的所有复根及原所有 Gram 点都排尽。

## 6. 最后整个二次商代数回到原 D

在
$$
K=\mathbb Q[e]/(4e^2+5e+3)
$$
上原矩阵秩为33，未主元列恰为 x 和1。源码没有把二列核当成自由原解，而是用实际原行组合提取
$$
y=\tfrac12,\qquad t=0,\qquad (x-\tfrac12)^2=0.
\tag{11}
$$
全部原行组合再次对35列回乘。把同一 (11) 代回 (4)，在完整非约化代数 `K[x]/((x-1/2)^2)` 中实际得到
$$
\ell=\tfrac12,\qquad T=-\tfrac12,\qquad
\lambda=\tfrac12+(\tfrac e6+\tfrac38)(x-\tfrac12).
\tag{12}
$$
六条原必要式在该代数中的返回也逐条为零；随后原 D 的返回为
$$
D=\ell(2\lambda^2-2\lambda+1)-T^2
=(\tfrac e6+\tfrac38)^2(x-\tfrac12)^2=0.
\tag{13}
$$
每次多项式余式均核原式=商乘首一二次式+余式。没有先丢弃重根或只选一个嵌入。由 (7) 原点的 D 是单位，(13) 排尽最后整个二次域覆盖。

于是 (10) 的全部12维覆盖均已返回并排除，得到本条所称整个 k=−1 权线为空。

## 7. 自含源和真实执行

- 源：`notes/2026-11-27-unit211-generic-LS-Delta-zero-W-kminus1-original-return-8542.py`，18947字节。
- 源 SHA256：`43393adf1bd9190a6c361ec6750f4e96716086727d9f02035b0d301410450cb7`。
- 实际 exit0；墙钟3.740542983秒；峰值 RSS33156KiB；源内3.310101391秒、RSS32000KiB。
- 配置180秒、4GiB；Python FLINT0.9.0。无外部大门、无缓存多项式输入。
- stdout13375字节，SHA256：`b6ee2dbca1efa1debc01a2ad2fd3ced4af5e99ce629fb01a527c986876320ed7`。
- 小回执：`notes/2026-11-27-unit211-generic-LS-Delta-zero-W-kminus1-execution-8542.json`。
- 两条多项式 cofactor 的 SHA256 分别为 `c06508df1de9505be52a9b68b1f25027ecdc548f8b34bfd9426652ab8a1db0e0`、`046bb9945ac09a65b649d3b9b442e98dc75b554962306cd1c740a79824e4e085`。
- 128/128次两常数子式的 QQ Bézout 系数联合 SHA256 为 `71a13b8f039eb674244b44259b24af33b3a40d445cca6d790f5c2cb233efd695`。

这里没有新增失败的计算门。后续只可使用已经支付的 k+1；一般 W=0 的其余原同点值条件仍须继续，不能把本条局部排除扩大成整个课题完成。
