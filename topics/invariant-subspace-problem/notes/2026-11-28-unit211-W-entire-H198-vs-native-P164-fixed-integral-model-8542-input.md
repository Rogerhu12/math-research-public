# R150：整个 H198 与原 native P164 的新整模型输入

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 单一新目标及原范围

已经完成的 [N1 斜率定理](../results/R150-appendix-unit211-W-N1-H198-weight-curve-and-two-generator-monic-square.md) 给出完整 QQ 不可约权多项式 H198，双次数 $(14,19)$、总次数 25。其 SHA-256 是 3569ba450503ee36acfed6f3ef047c3a08cf1735c3f95028a7c6b0f9b060db82。整条 H198=0 尚未排除。

已完成的 [全 W 原 native NS/PS 定理](../results/R150-appendix-unit211-W-entire-original-native-NSPS-necessary-weight-curve.md) 给出六行

$$
N_S,\ P_S,\ yN_S,\ tN_S,\ yP_S,\ tP_S
$$

在同一六生成元 $(1,x,y,t,y^2,yt)$ 上的完整原迹矩阵 $M_{\rm nat}$。其固定原行列式满足

$$
D_{\rm nat}=\det M_{\rm nat}=c\,U_{\rm paid}\,P_{164},
\qquad c\in\mathbb Q^\times,
\tag{1}
$$

其中 $U_{\rm paid}$ 仅含已经支付的权因子，$\deg_{\rm total}P_{164}=164$。本次不重新执行此前 95 秒 QQ 行列式，也不重新因式分解 H198。

新目标只判断：是否能以一个原整模型的非零除法余式证明

$$
H198\nmid D_{\rm nat},\quad\text{因而 }H198\nmid P_{164}.
\tag{2}
$$

这是整条 H198 的有限交支输入，不是排空测试。与旧 H265 不整除结果的区别在于整个新权曲线 H198；旧 H265 的结论不能替代本次 (2)。

## 2. 固定的 p 整性及 Gauss 论证

在任何行列式输出之前固定 $p=1009,k=3$。新源码逐个检查完整 $M_{\rm nat}$ 的所有 QQ 系数分母及完整 H198 的所有 QQ 系数分母都为 p 单位，并检查 H198 至少有一个 p 单位系数。因此

$$
D_{\rm nat}\in\mathbb Z_{(p)}[e,k],\qquad
H198\in\mathbb Z_{(p)}[e,k]\text{ 为 p 本原}.
\tag{3}
$$

若在 $\mathbb Q[e,k]$ 中有 $D_{\rm nat}=H198\cdot Q_0$，Gauss 的内容乘法公式迫使 $Q_0\in\mathbb Z_{(p)}[e,k]$：两个多项式的最小 p 赋值相加，而 H198 的最小赋值为零。故模 p 并专门化 $k=3$ 仍有整除。

新输入只在 $\mathbb F_{1009}[e]$ 中计算六阶固定行列式，并实际返回每次 Bareiss 多项式除法和

$$
\overline D_{\rm nat}(e,3)=q(e)\,\overline{H198}(e,3)+r(e).
\tag{4}
$$

若实际 $r\ne0$，由 (3)–(4) 得到 (2)。此逻辑不要求特化点对应物理解，也不由某个模理想为空推出 QQ 理想为空。任何临时主元均没有被加入原权单位表。

若本次 H 特化为零或常数，或最后余式为零，只记录这个固定模型未产生见证；不扫描别的素数或 k，不宣称 QQ 整除或有限性。

由 (1)，假设 $H198\mid P_{164}$ 就必有 $H198\mid D_{\rm nat}$。因此 (2) 不需要先假定 H198 与 $U_{\rm paid}$ 互素，也不倒置任何新权因子。结合已实际完整 QQ 因式证明的 H198 不可约性，非零余式足以给出

$$
\gcd_{\mathbb Q[e,k]}(H198,P_{164})=1.
\tag{5}
$$

此处 gcd 为一只用于证明两条曲线无共同分量；不用于判空。

## 3. 若 (4) 非零时的准确长度推论

只有首次实际返回 $r\ne0$ 后，(5) 才给出完整仿射交代数

$$
B_0=\mathbb Q[e,k]/(H198,P_{164}),
\qquad \dim_{\mathbb Q} B_0\le25\cdot164=4100.
\tag{6}
$$

这是平面 Bézout 的有限方案长度界，包含非约化重数。已付纯权局部化只删除有限 Artin 分量，不增加长度。

全 W 的同一原均值商已由六个单项式生成，不要求自由；把它基变换到 (6) 并再施加其它同点原式，长度至多 $6\cdot4100=24600$。然后加入原

$$
\rho^2=1-Q
$$

最多乘二。在当前既有 $D\ne0$、$\ell\ne0$、$u-\ell\ne0$ 原值范围，完整 HA/HB 给出唯一的

$$
\zeta=\frac{T+uK/[2(u-\ell)D]}{\ell},
\quad
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell T A_2+2T^3.
\tag{7}
$$

故固定规范七坐标 $(e,k,\rho,x,y,t,\zeta)$ 的完整原商长度至多 49200。式 (7) 使用当前原域已付几何条件；它不外推一般 $D=0$ 碰撞图。个别原 N/P 条件仍须同点施加；额外取商或有限 Artin 代数的局部化不会增加这个界。此处没有把自由六维环境当成原商自由，也没有计算未经规范化矩阵的点数。

本次即使成功，也只给有限支持及原环境长度；不宣称 H198 整支或全 W 为空。

## 4. 唯一尚未执行源

源名：

2026-11-28-unit211-W-entire-H198-vs-native-P164-fixed-integral-model-8542.py

完整 SHA-256：

fa703c6466eb776425ccec39125477555e118b2aea48c3c5289ed7c01c414a64

固定 180 秒 / 4 GiB，尚未执行。仅执行 native 源的 8074 字节原六行定义前缀，以及 N1 slope 源的 4799 字节必要定义前缀；后二者各自通过全源与片段 SHA 核验。N1 定义中剩余因子恰为 $-H198/288$，源直接以这个已完成的完整因式身份构造 H，不重做分解。只输出定义、次数、少量非零见证、SHA 和实际状态，不传送系数数组或编码缓存。

固定依赖共五件：

- 2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py；
- 2026-11-28-unit211-W-original-N1-slope-weight-coordinate-monic-square-8542.py；
- 2026-11-28-unit211-W-K7-open-physical-lambda-original-three-column-projection-binding-corrected-8542.py；
- 2026-11-28-unit211-W-original-physical-lambda-four-heads-and-affine-identity-8542.py；
- 2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py。

源码已经固定必要原输入；具体非零余式、实际退出码与 (6)–(7) 是否取得本次新见证，均等待唯一首次运行。

首次派发前的计时接口修正：本最终 9176 字节版本同时钳制 signal.alarm 与 signal.setitimer(ITIMER_REAL)，包含嵌套前缀中的直接 setitimer 调用，始终不越过本源最初的绝对 180 秒截止。数学输入、固定 p/k 和资源界没有改变。旧 blob 6aadb3b4bf6124bb5e52ff0308720064a19c102a 从未执行，不记为数学失败。
