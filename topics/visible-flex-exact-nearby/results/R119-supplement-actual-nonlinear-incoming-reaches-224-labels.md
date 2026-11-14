# R119 续篇：真实非线性 incoming 到达 224 标签，并闭合正帽的 incoming 反馈

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** R133 的整个非线性长段解在远端得到的真实角解析增宽，
可以通过本题已经构造的新强尾原点 Schur 逆，进入同一个
$\ell^1_{224}$ 非线性标签球。这不是 ordinary 224 阶角导数的换名。
对已经给出的周期正帽图，本文还解出包含实际 $f_B(a)$ 反馈的 incoming
固定点。所得标签、尾曲面和正帽—长段曲面都是真实存在的全频对象。

这个固定点消去的是完整 incoming 列。尾部的自身非线性剩余和长段的
非零 $f_B$ 混合剩余仍被明确保留；本文不把它称为远端完整方程
$\mathfrak F=0$ 的解。

## 1. 固定同一个公共度量及未改的长段

固定[新联合 KAM](R119-supplement-stronger-tail-joint-actual-return-KAM.md)
给出的一个零标签参数 $\Gamma^0$。在这个实参数上，依
[新 raw/regular 定理 §§3–4](R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md)
重新停止第四 connector，并选定一个真正的全模好 bump 参数
$t_0\in G_{\Gamma^0}^{\ddagger}$。本篇始终使用这个固定度量。
它的主体参数可以是 R133 已允许的任意参数；其支持在 $(.05,.18)$ 的
改动不影响本篇长段。

新深 profile、$\Gamma^0$、第四停止与双 bump 的改动都在 $u\ge B$。
[真实重停定理 §8](R119-supplement-retuned-fourth-connector-and-common-bumps.md)
及新 raw 定理 (V.8)–(V.11) 保证

$$
 B=2^{24}-25/8,\qquad a_*,z_*,\omega\text{ 及 }[0,B]
 \text{ 的参考几何准确未变}.
 \tag{I.1}
$$

因此 R133 的真实长段 Dirichlet map 在这里是**同一个算子**。不是仅因
两个 DN 主符号相近而转授旧结论。用其原物理坐标

$$
 t=\omega(B-u),\quad L=\omega B,\quad
 a=a_Be^t,\quad w=a/(4\omega),\quad E=1+w^2.
 \tag{I.2}
$$

归一化高度 $h$ 满足 $h(0)=f_B,h(L)=f_*$，真实非mean斜率为
$K_{B,\perp}(f_B,f_*)=2f_B+h_t(0)$。物理高度采用原来的
$Z=Z_{\rm ref}-v$；因此物理 $Z_a$ 的缺口是下文斜率缺口的 $-w_B$ 倍。
它没有被改名为 grounded flux。

本篇的尾图与 $
\Gamma^*(a)$ 的另一个联合构造暂不混合。特别没有假定在
$\Gamma^0$ 上选好的 $t_0$ 对所有变化的 $\Gamma$ 仍是全模好参数。
未来若改用 $\Gamma^*(a)$，须把已经证明的完整参数列和相对网络逆一起消费。

## 2. 三个真正的空间及已存在的非线性输入

所有非mean频率为 $m\in4\mathbb Z\setminus\{0\}$，$M=|m|$。记

$$
 \|a\|_{224}=\sum_{m\ne0}e^{224M}|a_m|,
 \qquad
 \|g\|_{\mathfrak Z_s}=\sum_{m\ne0}e^{sM}M|g_m|
                         =\|g\|_{\dot A^1_s}.
 \tag{I.3}
$$

$a_m$ 是新强尾真实层 $b_m$ 上的内部标签，不是 $B$ 切口的高度系数。
[新强全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
和实际 balanced connector 给

$$
 \|X(a)\|_{\mathcal X_{224}}<16\|a\|_{224},
 \qquad \|a\|_{224}<1/64,
 \tag{I.4}
$$

$$
 \|f_B(a)\|_{\dot A^2_{\sigma_B}}+
 \|k_B(a)\|_{\dot A^1_{\sigma_B}}
 <2^{-447}\|X(a)\|<2^{-443}\|a\|_{224},
 \qquad \sigma_B=777/400.
 \tag{I.5}
$$

这里的新 cut128 规范、有限几何、$A,w/a$ 盒与逐段长度已由新 raw 定理
重新支付；(I.5) 消费 [balanced224 的 (W.12)–(W.18)](R119-supplement-balanced-connector-label-domain-224.md)，
并以真实新的 $16\|a\|$ 代替旧标签图的 $13\|a\|/4$。
全部 nonlinear modes、holonomy mean 小根与两条径向迹都在这个估计中。

实际原点 Schur 行和其已重证的全频逆为

$$
 D_0 a=DT_k(0)a+\mathsf C_LDT_f(0)a,
 \qquad (\mathsf C_Lf)_m=M\coth(ML)f_m,
$$
$$
 \|D_0^{-1}g\|_{224}\le\frac1{16}\|g\|_{\mathfrak Z_{2074}}.
 \tag{I.6}
$$

这是新 raw 定理 (V.20) 的同一算子；它已经使用真实完整两迹矩阵、raw404
和新好 bump 的全模夹角，没有除以可能为零的高度。

另一方面，[R133 真非线性筛选与增宽](R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md)
给每个实际输入

$$
 \|f_*\|_{\dot A^2_\sigma}\le r_f=10^{-8},\qquad
 S=\sigma+7L/16>S_-:=10724906.843270461
 \tag{I.7}
$$

的整个真实 incoming

$$
 g_*(f_*):=K_{B,\perp}(0,f_*),\qquad
 \|g_*(f_*)\|_{\mathfrak Z_S}<18\|f_*\|_{\dot A^2_\sigma},
 \quad \|Dg_*(f_*)\|_{\dot A^2_\sigma\to\mathfrak Z_S}<24.
 \tag{I.8}
$$

这里 $S$ 是原物理角的指数宽，包含所有高模。它来自真正变角宽 PDE
收缩及与已存在未加权解的唯一性识别，不是假设解已属于这个空间。
实际 $\sigma$ 在 R133 的完整范围内且小于 $1/8<\sigma_B$。

## 3. 完整 nonlinear incoming 的实际 224 标签列

因为最小非零频率为4，直接逐项有

$$
 \|g\|_{\mathfrak Z_{2074}}
 \le e^{-4(S-2074)}\|g\|_{\mathfrak Z_S}.
 \tag{I.9}
$$

于是定义的不是形式未知量，而是现有有界算子的实际像

$$
 a^{\rm in}(f_*):=D_0^{-1}g_*(f_*).
 \tag{I.10}
$$

它满足

$$
 \boxed{\quad
 \|a^{\rm in}(f_*)\|_{224}
 \le\frac98e^{-4(S-2074)}\|f_*\|_{\dot A^2_\sigma},\qquad
 \|D a^{\rm in}\|
 \le\frac32e^{-4(S-2074)}.
 \quad}                                                   \tag{I.11}
$$

令 $E_-=4(S_--2074)=42891331.373081844$。
$\log(9/8)<1/8$，所以以下宽松严格值无需使用浮点下溢的0：

$$
 \frac98e^{-E_-}<e^{-42891331}<2^{-60000000},
 \qquad
 \frac32e^{-E_-}<2^{1-60000000}.
 \tag{I.12}
$$

这给一个真正输入到已付球的结论：

$$
 \|a^{\rm in}\|_{224}<2^{-60000000}r_f,
 \quad\|X(a^{\rm in})\|<2^{4-60000000}r_f
                                      <2^{-262144}.
 \tag{I.13}
$$

相应 $f_B(a^{\rm in})$ 在真实物理角宽 $\sigma_B$ 上小于
$2^{-60000443}r_f$，因而准确进入正帽—长段原有的独立
$\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$ 域。没有把一个未获授权的更宽
标签球当输入，也没有把输入留在低于224的标签权上。

## 4. 把实际正帽的 incoming 反馈一并解掉

令 $c$ 表示一个已经允许的内侧曲率输入。可以取
[原开放帽图](R133-supplement-actual-periodic-cap-open-inner-graph.md)
的 $c_{\ne0}(1)$，或
[不依赖旧中心的帽图](R133-supplement-universal-small-inner-periodic-cap.md)
的 $c_{\ne0}(3/2)$。后者真实 $f_*$ 上界为 $2\cdot10^{-9}$，本篇统一
放宽到 $r_f=10^{-8}$。保持其原 $A_2$ 正则条件与共同实偶反射条件。

这两个已证明的完整收缩都给同一物理长段端口图

$$
 f_*=\Phi(c,f_B),\qquad
 \|\Phi(c,f_B)\|_{\dot A^2_\sigma}\le r_f,
 \quad \|f_B\|_{\dot A^2_\sigma}<2^{-60}.
 \tag{I.14}
$$

固定 $c$，这个 map 在复化的 $f_B$ 球上全纯。只用这个已存在的球，
对 $\|f_B\|\le2^{-61}$ 的 Cauchy 界给

$$
 \|D_{f_B}\Phi\|\le2^{61}r_f<2^{35}.
 \tag{I.15}
$$

这里没有为了求导把整个帽扩张到长段单独拥有的 $2^{-27}$ 圆盘；
原开放帽更强的 $3.254260$ 界当然也可用，但不是本证明的前提。

尾图 (I.5) 在 $\|a\|<1/64$ 的复球上全纯。对
$\|a\|\le1/256$，在单位方向取半径 $1/256$ 的圆盘，得到

$$
 \|Df_B(a)\|_{\ell^1_{224}\to\dot A^2_{\sigma_B}}
                              \le2^{-442}.
 \tag{I.16}
$$

现在在实际 Banach 球 $\|a\|_{224}\le R_a:=2^{-60000000}$ 上定义

$$
 \mathcal I_c(a)=D_0^{-1}g_*(\Phi(c,f_B(a))).
 \tag{I.17}
$$

由 (I.5) 所有中间输入都在 (I.14) 的半球；由 (I.11)–(I.12)，

$$
 \|\mathcal I_c(a)\|<R_a r_f<R_a/2,
 \qquad
 \operatorname{Lip}\mathcal I_c
 <2^{1-60000000}\,2^{35}\,2^{-442}
 =2^{-60000406}<1/4.
 \tag{I.18}
$$

因此对每个允许 $c$，存在唯一实际 $a_c^{\rm inc}\in\ell^1_{224}$，满足

$$
 \boxed{\quad
 D_0a_c^{\rm inc}
   =g_*(f_{*,c}),\qquad
 f_{*,c}=\Phi(c,f_B(a_c^{\rm inc})),\qquad
 \|a_c^{\rm inc}\|<R_a r_f.
 \quad}                                                   \tag{I.19}
$$

整个新尾及帽—长段曲面现在可在相同的实际 $f_B(a_c^{\rm inc})$ 上取值。
真实帽反馈没有停在 $f_B=0$ 的辅助问题。唯一性保实共轭、四重周期和共同
反射，并与共同角平移交换；没有只对有限模实现这个固定点。

若 $c$ 的导数列为 $L_c=\|D_c\Phi\|$，同一固定点给

$$
 \|D_ca_c^{\rm inc}\|_{\to\ell^1_{224}}
 <2^{2-60000000}L_c.                                    \tag{I.20}
$$

可分别消费原开放图的 $.000844633495$，或新小输入帽图的
$.000037884495$。这不是对尚未证明的主体输入邻域增加授权。

## 5. 真实剩余的准确恒等式与当前可付的 norm

写 $a=a_c^{\rm inc}$、$f=f_B(a)$、$f_*=f_{*,c}$。定义

$$
 \begin{aligned}
 R_T(a)&=k_B(a)+\mathsf C_L f_B(a)-D_0a,\\
 E_B(f)&=K_{B,\perp}(f,0)+\mathsf C_L f,\\
 M_B(f,f_*)&=K_{B,\perp}(f,f_*)-K_{B,\perp}(f,0)-g_*(f_*).
 \end{aligned}                                          \tag{I.21}
$$

所有项都是已存在的真实 map。由 (I.19)，未解的完整远端方程准确成为

$$
 \boxed{\quad
 \mathfrak F(a,f_*)=k_B(a)-K_{B,\perp}(f,f_*)
                  =R_T(a)-E_B(f)-M_B(f,f_*).
 \quad}                                                   \tag{I.22}
$$

没有删除 $\mathfrak F(a,0)$，也没有以 $S_Lf_*$ 代替完整 $g_*(f_*)$。
在当前实际物理角宽，三项都可严格定量：

1. 因 $\coth(4L)<2$，(I.5) 给
   $\|k_B+\mathsf C_Lf_B\|_{\mathfrak Z_{\sigma_B}}<2^{-442}\|a\|$。
   对半径 $1/64$ 的完整全纯图沿方向 $a$ 展开；在
   $\|a\|<1/128$ 上，二阶以上之和至多
   $2\cdot64\cdot2^{-442}\|a\|^2=2^{-435}\|a\|^2$。
2. 长段零内端问题的准确 Green 给
   $\|h(f,0)\|_{\mathcal Y}\le16\|f\|+
   2^{14}r_*\|h\|$，$r_*=2^{-20}$。所以
   $\|h\|<17\|f\|$。原完整两端二次迹界 (D.27) 给
   $\|E_B(f)\|_{\mathfrak Z_\sigma}<2^{22}\|f\|_{\dot A^2_\sigma}^2$。
3. R133 (S.29) 在相同的实际宽 $\sigma$ 给
   $\|M_B(f,f_*)\|_{\mathfrak Z_\sigma}
     \le25\,2^{27}e^{-7L/4}r_f\|f\|_{\dot A^2_\sigma}$。

合并 (I.5)，得到

$$
 \|\mathfrak F(a,f_*)\|_{\mathfrak Z_\sigma}
 <2^{-434}\|a\|_{224}^2
       +2^{-411}e^{-7L/4}r_f\|a\|_{224}
 <2^{-120000400}.
 \tag{I.23}
$$

最后一个只是保守严格上界；真实量并未被置0。
尽管 (I.23) 极小，它不属于 (I.6) 所要求的
$\mathfrak Z_{2074}$ 合同。当前 $R_T$ 只由 (I.5) 授予宽
$\sigma_B=1.9425$，$M_B$ 只在实际 $\sigma$ 上支付。
故不能把 (I.22) 再送入 $D_0^{-1}$ 而宣称闭合收缩。
真正下一项仍是更新后完整 mixed-tail/connector 的相对逆或等价边界解图。

## 6. 两个 mean、实际法向单位与源项范围

尾和长段在本篇各自满足真实 $M=1$。它们的 mean 斜率分别为各自
完整非mean两迹的同一个 holonomy 小根。只有在 (I.22) 准确为0时，
共同 $f_B$ 与共同非mean $k_B$ 才使两个 mean 小根相等；本篇不提前
把这个 mean 缺口清零。

尾端平均高度采用真实积分

$$
 v_{0,B}=\lambda+\int_{\rm flat}^{B}awK_0\,dt.
 \tag{I.24}
$$

正帽—长段端的独立整体平移可与此值对齐，但另一端 mean 高度是输出。
R133 对内端输入改变给出的准确跨度仍为

$$
 \Delta[v_0(L)-v_0(0)]
 =\int_0^L aw\,\Delta\mu\,dt,
 \quad
 |\Delta[v_0(L)-v_0(0)]|
 \le\frac{aw(L)}{165}(1-e^{-15L/4})\|f_*\|.
 \tag{I.25}
$$

mean 斜率的独立远端界是
$|\Delta K_{B,0}|\le e^{-7L/4}\|f_*\|/44$，并没有把 (I.25)
错误地乘上这个指数。整体 $\lambda$ 只有一个，不另指定两个 mean 高度。

本篇的尾、connector 与长段都是 source-free 的完整非线性解。
线性化时 ordinary source、weak flux source 及度量参数列仍须使用已经付出的
连续源和完整 Piola/normal-shear 合同；本篇没有把这些列包含在
$g_*(f_*)$ 的无源逆内。尤其，bare weak flux 的两端迹不能由内部
$L^2$ 源范数自动取得。

## 7. 必要的严格预算

`scripts/fourfold_actual_incoming_224_20261113.py` 以准确有理数和 Arb
核对真实宽差、严格指数、完整输入球、feedback 收缩及剩余界，输出
`notes/2026-11-13-R119-actual-incoming-224-budget.json`。
证明依赖的完整非线性构造和空间身份在上文逐一给出；脚本没有用有限
Fourier 检查代替无限维存在性，也没有声称已消去 (I.22)。
