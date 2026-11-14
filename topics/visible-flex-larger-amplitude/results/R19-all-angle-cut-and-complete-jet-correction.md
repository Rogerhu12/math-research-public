# R19：全角 cut 包络与完整解析两-jet 修正

作者：exact_closure（GPT-6 Astra Pro，AI-assisted），2026-11-12。

状态：**已证明**。下面给出代数引理的完整证明，附有对保存的有限 Fourier cut 数据的精确有理计算。它给出一个**单一 cut 上**满足完整 Darboux 方程和完整角平均条件的邻近解析两-jet。它不证明径向轨道存在，不证明保存的有限 Robin 轨道已经接到 R18，也不构成课题完成。

## 1. 输入与两种明确不同的实数对象

输入为

`notes/2026-11-12-closure-rational-q003-m8-d8-s16-l1024-response.json.gz`，

SHA256 `89a0e36c853902e64c83917302352b1218c24e501c1828aa9419fa80d593f5af`。这是新固定背景 `visible-larger-rational-deep-alpha-v1` 上实际有限非线性求解的 M8/depth8 结果；全部非线性轨道仍是数值对象。

脚本为 `computations/closure_scaled_endpoint_cut_enclosure.py`，精确有理输出为 `notes/2026-11-12-closure-scaled-endpoint-q003-cut-enclosure.json`。每个 JSON 浮点字段先用 `Fraction.from_float` 解释为它实际保存的二进制有理数，再作整数/有理数运算；输出同时保存分数、入口脚本哈希和输入哈希。十进制显示不是包络的依据。

定义以下两个对象，分别计算，不互换：

1. **`direct_stored_jet`**：$r,E,E',k_0,(k_r)_0$ 均是保存的 `radius,E,Ep,meanSlope,meanSecond` 的精确二进制值；非均值的高度、斜率和二阶系数也分别取保存值。
2. **`split_background_jet`**：$r,w,w_r$ 及各非均值系数仍取保存值，但在实数层定义 $E=1+w^2$、$E'=2ww_r$、$k_0=w+\texttt{meanSlopeCorrection}$ 和 $(k_r)_0=w_r+\texttt{meanSecondCorrection}$，其中每一项先转成精确二进制有理数，随后做精确加乘。这不等于把已有的浮点加乘结果取成实数。

两者相差（第一种减第二种）如下；JSON 中保留各项的精确分数：

| 字段 | 第一种减第二种 |
|---|---:|
| $E$ | $-8.117950756059152\times10^{-17}$ |
| $E'$ | $-3.3010631265518006\times10^{-17}$ |
| $k_0$ | $6.156688238632051\times10^{-18}$ |
| $(k_r)_0$ | $7.545742718033691\times10^{-17}$ |

第二种能保留完整 mean 小修正，故归一残差更小。不能因此把第二种的界引用成第一种的界。这两种对象都还没有包住源背景在精确实数中的 profile evaluation error；它们处于同一数值背景的不同浮点表达层。固定 $g$ 的精确证明仍须把源求值误差及径向离散误差另行接上。

## 2. 完整角向分子，不作角采样

在 cut 半径 $r$ 处写保存的三组有限 Fourier 数据为

$$
h(\theta)=\sum_{j=1}^M H_j\cos(2j\theta),\qquad
k(\theta)=k_0+\sum_{j=1}^M K_j\cos(2j\theta),\qquad
k_r(\theta)=(k_r)_0+\sum_{j=1}^M T_j\cos(2j\theta).
$$

令

$$
p=h_\theta/r,\quad S=1-p^2,\quad
\Delta=E-k^2-Ep^2,\quad B=k+Ep_\theta,
$$

以及完整 Darboux 分子

$$
F=B k_r-\frac Er(k_\theta-p)^2
   -\frac{E'}2(1-p^2+kp_\theta).
\tag{2.1}
$$

这里 $E p_\theta$ 是两个量的乘积，$E'$ 是背景度量的径向导数。式 (2.1) 可直接由 $g=E(r)dr^2+r^2d\theta^2$ 的高度 Darboux 方程得到；与固定源 `f6tail_momentum_physical_jets.mjs` 的相对变量代入后，有

$$
\texttt{darboux}=\frac{F}{E^2r}.
\tag{2.2}
$$

因此它与 $F\Delta^{-3/2}$ 的归一不同。脚本分别输出 `source_physical_Darboux_abs_upper` 和 `weighted_Darboux_numerator_abs_upper`，不把后者当成 source 的 `fullD`。

使用复 Laurent 表示但只存实有理系数：写 $p=iP$、$k_\theta-p=iR$，其中 $P,R$ 的 Laurent 系数实且奇。于是

$$
F=B k_r+\frac ErR^2-\frac{E'}2(1+P^2+kp_\theta),\quad
\Delta=E-k^2+EP^2,\quad S=1+P^2.
$$

所有卷积都是精确有理运算。对 $a(\theta)=\sum_m a_m e^{im\theta}$，令 $\|a\|_0=\sum_m|a_m|$，则 $|a(\theta)|\le\|a\|_0$ 对所有实角成立。实偶多项式的下界为 $a_0-\sum_{m\ne0}|a_m|$。当前 $F$ 的最高频率是 $32$；输出包含它的全部频率，而非仅保留的 $2,4,\ldots,16$。

由这些有理下界，同时验证 $B_{\min}>0$、$\Delta_{\min}>1/2$、$S_{\min}>0$。这处理了当前 cut 的所有实角，未用角向网格。

## 3. 完整角平均的有理级数包络

完整角平均条件是

$$
\Phi(k)=\left\langle
\frac{1+kp_\theta/S}{\sqrt\Delta}\right\rangle-1=0.
\tag{3.1}
$$

设 $T=\Delta-1$、$t=\|T\|_0<1$、$u=\|P^2\|_0<1$。分别使用

$$
(1+P^2)^{-1}=\sum_{n\ge0}(-P^2)^n,
\qquad
(1+T)^{-1/2}=\sum_{n\ge0}(-1)^n\frac{\binom{2n}{n}}{4^n}T^n.
$$

截断到 $n=d$，记第二个截断为 $V_d$、第一个为 $U_d$，$N_d=1+kp_\theta U_d$。由于二项系数 $\binom{2n}{n}/4^n\le1$，有

$$
\left|\Phi-\left(\langle N_dV_d\rangle-1\right)\right|
\le
\frac{\|kp_\theta\|_0 u^{d+1}}{(1-u)(1-t)}
+\frac{\|N_d\|_0t^{d+1}}{1-t}.
\tag{3.2}
$$

当前只需 $d=4$。右侧约 $9.663\times10^{-29}$，仍是精确有理上界。定义输出的完整 $\Phi$ 上界为 $\phi$。

只移动总径向斜率的常数项 $k\mapsto k+s$。直接求导并化简得到

$$
\frac{d}{ds}\Phi(k+s)
=\left\langle\frac{B+s}{\Delta_s^{3/2}}\right\rangle,
\qquad
\Delta_s=\Delta-2sk-s^2.
\tag{3.3}
$$

令 $\eta=8\phi/B_{\min}$。若

$$
\eta\le B_{\min}/2,\qquad
\Delta_{\min}-2\eta\|k\|_0-\eta^2\ge1/2,\qquad
\Delta_{\max}+2\eta\|k\|_0+\eta^2\le2,
\tag{3.4}
$$

则 $|s|\le\eta$ 上导数至少为 $B_{\min}/6$。在 $s=\pm\eta$ 的变化量大于 $\phi$，故连续性及严格单调性给出唯一根 $s_*$，且 $|s_*|\le\eta$。当前两个算术对象均精确通过 (3.4)。这不是把有限角平均根改称完整角平均根。

## 4. 同一 $E,E'$ 下的完整解析两-jet 修正

在完整根 $s_*$ 处保持 $h$ 与 $k$ 的所有非均值系数，定义

$$
k_{\rm ex}=k+s_*,\qquad
(k_r)_{\rm ex}
=\frac{\frac Er(k_\theta-p)^2
   +\frac{E'}2(1-p^2+(k+s_*)p_\theta)}{B+s_*}.
\tag{4.1}
$$

此时 (2.1) 在每个角上恰好等于零，且 (3.1) 恰好为零。径向二阶导数一般含无限多个 Fourier 模态；这里没有把它截到 M8。

记 $J=k_r-E'p_\theta/2$。由 (2.1) 得到精确恒等式

$$
(k_r)_{\rm ex}-k_r=-\frac{F+s_*J}{B+s_*}.
\tag{4.2}
$$

取解析 Wiener 范数

$$
\|a\|_{\log2}=\sum_m2^{|m|}|a_m|.
$$

若 $b=B_0-\|B-B_0\|_{\log2}-\eta>0$，则 Neumann 级数证明分母在该 Banach 代数中可逆，其逆范数不超过 $b^{-1}$。从而

$$
\|(k_r)_{\rm ex}-k_r\|_{\log2}
\le\frac{\|F\|_{\log2}+\eta\|J\|_{\log2}}{b},
\tag{4.3}
$$

并且更紧的实角界为

$$
\sup_{\theta\in\mathbb R}|(k_r)_{\rm ex}-k_r|
\le\frac{\|F\|_0+\eta\|J\|_0}{B_{\min}-\eta}.
\tag{4.4}
$$

当前两个对象均有 $b>0.07999$，故得到 $|\operatorname{Im}\theta|\le\log2$ 内的完整解析 trace。因为输入最高频率为 $16$，修正后频率 $|m|\ge18$ 的未表示部分，其无权 Wiener 范数至多是 (4.3) 右侧乘 $2^{-18}$。

这些数据均为实、偶、$\pi$ 周期。对其平面投影取与圆相容的定向，角向 tangent 相位导数就是 (3.1) 中的 integrand。完整根使它在 $2\pi$ 上积分为 $2\pi$；$\pi$ 周期性使半周积分为 $\pi$。平面 tangent 在半周后变号，因此其平移 period 也恰为零。高度本身 $\pi$ 周期，故 cut 的完整空间曲线闭合。式 (4.1) 还支付 cut 上的 Darboux 相容条件。这一结论仍只针对一条 cut 的完整两-jet。

## 5. 当前 q003 数据的包络

下表向上缩略显示上界；精确比较以 JSON 的有理数为准。

| 量 | `direct_stored_jet` | `split_background_jet` |
|---|---:|---:|
| $\|F\|_0$ | $1.130812\times10^{-17}$ | $2.555632\times10^{-19}$ |
| source 同归一 $\|F\|_0/(E^2r)$ | $3.721582\times10^{-17}$ | $8.410770\times10^{-19}$ |
| 完整 $|\Phi|$ | $4.108229\times10^{-17}$ | $4.991966\times10^{-26}$ |
| 完整 mean 根的 $|s_*|$ | $4.108335\times10^{-15}$ | $4.992094\times10^{-24}$ |
| 径向二阶修正，所有实角 | $9.600742\times10^{-14}$ | $3.194738\times10^{-18}$ |
| 径向二阶修正，$\log2$ 解析 Wiener 范数 | $8.856561\times10^{-13}$ | $7.896369\times10^{-13}$ |
| 修正后未表示的 $|m|\ge18$ 二阶 trace，无权 Wiener 范数 | $3.378510\times10^{-18}$ | $3.012226\times10^{-18}$ |

本轮运行约 12 秒，峰值 RSS 12.4 MiB；只对已有输入作有理运算，没有启动新的大尾求解。

## 6. 与 R18 接口的关系及剩余工作

这一步确认实际 cut 的完整角向缺陷可以明确计算，并可以在同一 $E,E'$ 的局部两-jet 层作完整 mean / 全频修正。它没有显示修正后的 cut 处在 R18 真正无限尾的 trace 流形上。即使局部修正数值很小，径向传播的边值问题仍可能放大它；这个放大要由浅层的实际线性逆与非线性控制来支付。

当前缺少的是：保留固定新 $g$ 的实际浅层全频求解、源函数求值包络、径向加密误差及数学端口 F224（物理 node225）到浅 cut 的真 trace 匹配。保存的 finite Robin 响应、上表局部修正和 R18 小球不能互相替代。depth12/far225 的实际响应仍按团队资源安排等待独占窗口。

复算入口：

```bash
python computations/closure_scaled_endpoint_cut_enclosure.py \
  --input notes/2026-11-12-closure-rational-q003-m8-d8-s16-l1024-response.json.gz \
  --out notes/2026-11-12-closure-scaled-endpoint-q003-cut-enclosure.json
```
