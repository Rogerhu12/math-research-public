# R80：同一精确全前缀的弱解析内部解与普通源估计

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明（固定径向背景、辅助 incoming）；全文独审通过。** 本文对当前 flat17 第一周期与
R21 已固定的同一 exact bridge 给完整线性内部解和普通径向 $L^2$ 源估计。
两端指定的是明确的 Hadamard incoming；实际核心和尾 DN 的反射反馈仍须另解。
没有改变主度量、选取新的桥长、读取候选数组、执行 PDE 或尾请求。

主要代价是确定的解析宽度 $459/500=.918$ 和有限角阶。本文不以尚未证明的
整数频率相位间隙换取无带损失，也不把负 log 权说成解析衰减。

## 1. 固定背景和已经支付的输入

记 $c=a_s$、$\bar p=(1-c^2)^{-1/2}$，沿整个真实前缀使用同一变量
$$
U=(\beta,\pi)^T,
\quad Z=(x,y)^T=\operatorname{diag}(a/\bar p,\bar p^{-3})U,
\quad \frac{dr}{ds}=\frac1{a^2\bar p}.
\tag{1}
$$
全部 Fourier 模 $j\in\mathbb Z$ 保留，$k_j=\sqrt{1+j^2}$。精确方程是
$$
Z_j'=-ij\begin{pmatrix}0&V(r)\\1&0\end{pmatrix}Z_j+g_j,
\quad V=\frac{a^3a_{ss}}{(1-c^2)^2},
\quad g=(a^3f_1,a^2\bar p^{-2}f_2)^T.
\tag{2}
$$
$f$ 必须是完整线性 GC 系统的两分量普通源；未转换的位置残差不能直接
作为 $f$ 代入。位置与第二形式以及真实 Robin 行的变换见
[实际端口稿](../notes/2026-11-10-78718-geometry-actual-port-transfer-v1.md)。

第一 outward 周期记为 $c$，随后的同一精确桥记为 $b$。以下输入已经由
原函数的全区间推导给出：

1. [R75](R75-flat17-sturm-frequency-propagator.md) 对周期的真实
   齐次 $Z$ 传递给
   $$
   \|T^c_j\|\le17k_j^5\exp\!\left(\frac{459}{1000}|j|\right).
   \tag{3}
   $$
2. [R76](R76-flat17-internal-ordinary-source-provider.md) 对周期
   的两个指定 incoming $a^c_j$ 和普通源 $g^c_j$ 给真实内部与 outgoing：
   $$
   O^c_j\le I^c_j+400k_j^3F^c_j,
   \quad
   \mathcal N^c_j\le200k_j^3 I^c_j+40100k_j^6F^c_j,
   \tag{4}
   $$
   其中 $I^c_j=|a^c_j|$、$F^c_j=\|g^c_j\|_{L^2_r}$，
   $\mathcal N^c_j=\max(\sup_r|Z^c_j|,\|Z^c_j\|_{L^2_r})$。
3. [同一精确桥的势与反馈稿](../notes/2026-11-10-78718-geometry-bridge-two-barrier-feedback-v1.md)
   全文证明：桥的 Sturm 长度 $R_b<21/10$；存在 $0<\ell_b<R_b$ 使
   $V\le0$ 于 $[0,\ell_b]$、$V\ge0$ 于 $[\ell_b,R_b]$；整个桥
   $|V|<1200$。右侧非负外区任意两点、两个方向均满足
   $$
   \|T^b_j(r_2,r_1)\|\le3100k_j^2.
   \tag{5}
   $$
   同一稿亦证明全桥 $a_c\le a\le1$、$a_c>59/100$、$1\le\bar p<6$。

第三项现已全文独审并正式采纳为 [R79](R79-exact-bridge-two-barrier-feedback.md)。
冻结原稿“待审”只记当时状态。作者与 R76 作者有数学讨论，本文不是对 R76 的独立审稿；
本篇另由未参与者全文审查，见第 9 节。

周期与桥共享端点 $a=1,c=0$，所以 (1) 的变量完全相同，角坐标也相同。
桥根仍是 R21 固定的唯一根，不是 raw Target 的冻结浮点端点拼接。
本轮候选的新几何转移证书没有因此自动支付。

## 2. 桥自身的逐模实际存在和通量

置
$$
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
P=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad z=PZ.
\tag{6}
$$
任一模块的 incoming/outgoing 分别是
$$
a_j=(z_{+,j}(0),z_{-,j}(R))^T,\qquad
b_j=(z_{-,j}(0),z_{+,j}(R))^T.
\tag{7}
$$
方程矩阵 $A_j$ 满足 $A_j^*J+JA_j=0$、$\operatorname{tr}A_j=0$。
故真实齐次 $T$ 有 $T^*JT=J$、$\det T=1$。写
$$
PT(R,0)P=\begin{pmatrix}A&B\\C&D\end{pmatrix};
\quad C=\overline B, D=\overline A, |D|^2-|B|^2=1.
\tag{8}
$$
连续 $V$ 和任意 $g_j\in L^2_r$ 给实际变常数积分。若
$w=P\int_0^R T(R,t)g_j(t)\,dt$，给定 (7) 的两个 incoming 后唯一初值是
$z_+(0)=a_{1j}$、$z_-(0)=(a_{2j}-Ca_{1j}-w_-)/D$。
所以固定每个整数模先已有唯一 $H^1_r$ 解，不是先假定解存在再作估计。

记 $I=|a_j|$、$O=|b_j|$、$F=\|g_j\|_2$、
$E=|Z_j(0)|+|Z_j(R)|$。端口正交变换与通量给
$$
E\le\sqrt2\sqrt{I^2+O^2}\le\frac32(I+O),
\qquad
O^2-I^2=2\operatorname{Re}\int Z_j^*Jg_j\,dr
\le2\|Z_j\|_2F.
\tag{9}
$$
所有零源模块的散射矩阵 $\mathcal S_j$ 因而酉；其两个 cross 元素都等于
$1/D$，特别不为零。对固定 $j$ 的存在不意味着其逆在所有角空间自动有界。

## 3. 桥的普通源估计，不对 $g_2$ 增加径向导数

下面固定桥和一个 $j$，简写 $k=k_j$。在负势区长 $\ell_b$ 上，消元只在
弱意义下给
$$
(-\partial_r^2+q)y=ijg_1-\partial_r g_2,
\qquad q=-j^2V\ge0.
\tag{10}
$$
R76 第 3–4 节对任意连续非负 $q$ 已完整证明零 Dirichlet Green 核的
$0\le G\le G_0\le\ell_b/4$、$|G_t|\le1$，以及对普通 $L^2$ 源的弱表达
$$
y-y_h=ij\int Gg_1+\int G_tg_2.
$$
这里 $y_h$ 取实际两端 $y$ 值，$\sup|y_h|$ 至多两端最大值；这是
$(|y_h|^2)''\ge0$ 的直接结果。R76 的 $L^2$ 逼近与 $H^1_0$ 能量证明
允许 (10) 中 $g_2$ 无径向导数，也不要求它具有端点值。

本桥的 $\sqrt{R_b}<3/2$、$\ell_b<21/10$ 给
$$
\frac{|j|\ell_b^{3/2}}4+\sqrt{\ell_b}
<\frac{183}{80}k.
\tag{11}
$$
从桥的右端向后使用 (5) 和真实变常数积分，整个右外区有
$|Z|\le3100k^2E+4650k^2F$。负势区左端就是全桥左端；因此它的两端
$y$ 都满足该界。由 Green 式和 (11)，
$$
Y:=\sup_{[0,\ell_b]}|y|
\le3100k^2E+4653k^2F.
\tag{12}
$$
现在直接积分真实一阶式 $x'=-ijVy+g_1$；因为 $1200\ell_b<2520$，
$$
X:=\sup_{[0,\ell_b]}|x|
\le E+2520kY+\frac32F.
\tag{13}
$$
所以中央的 $|Z|\le X+Y$ 满足
$$
\begin{aligned}
X+Y
&\le 7815101\,k^3E+\frac{23460429}{2}\,k^3F\\
&<12000000\,k^3(E+F).
\end{aligned}
\tag{14}
$$
右外区的界更小。乘 $\sqrt{R_b}<3/2$，两种内部范数可统一写为
$$
\mathcal N^b_j:=\max(\sup|Z_j|,\|Z_j\|_2)
\le18000000\,k^3(E+F)
\le27000000\,k^3(I+O+F).
\tag{15}
$$

将 (15) 代入 (9)，若 $O>I$ 且 $I+O\ge F$，除以 $I+O$ 得
$O-I\le108000000\,k^3F$。若 $O\le I$ 已无问题；若 $I+O<F$ 则
$O<F$。因此所有情形均有
$$
\boxed{\quad O^b_j\le I^b_j+110000000\,k_j^3F^b_j.\quad}
\tag{16}
$$
回代 (15) 得
$\mathcal N^b_j\le54000000\,k^3I+2970000027000000\,k^6F$。
为便于后面组合，取更宽的明确整数常数
$$
\boxed{\quad
\mathcal N^b_j\le10^8 k_j^3I^b_j+4\cdot10^{15}k_j^6F^b_j.
\quad}
\tag{17}
$$
这些常数很粗，不能据此宣称可支付可见幅度；其作用是给真实整桥、全部
Fourier 模及两分量普通源的完整有效输入。证明没有除 $j$，因此也包括均值。

## 4. 两个实际模块接合的无算术下界

对两个模块，把源的 outgoing 记为 $\eta^c_j,\eta^b_j$，即
$$
b^c=\mathcal S^c a^c+\eta^c,
\qquad b^b=\mathcal S^b a^b+\eta^b.
\tag{18}
$$
由零 incoming 的 (4)、(16)，
$$
|\eta^c|\le400k^3F^c,
\qquad |\eta^b|\le110000000k^3F^b.
\tag{19}
$$
两模块通过同一个 $Z$ 接合。给定整个前缀外端 incoming $(I_L,I_R)$，令
$u$ 为周期右 incoming、$v$ 为桥左 incoming。真实接口式是
$$
\begin{aligned}
v&=(\mathcal S^c)_{21}I_L+(\mathcal S^c)_{22}u+\eta^c_R,\\
u&=(\mathcal S^b)_{11}v+(\mathcal S^b)_{12}I_R+\eta^b_L.
\end{aligned}
\tag{20}
$$
源列均保留。于是 $u$ 的反馈分母为
$$
\Psi_j=1-(\mathcal S^b_j)_{11}(\mathcal S^c_j)_{22}.
\tag{21}
$$
记两个反射为 $r_b,r_c$，相应 cross transmission 为 $t_b,t_c$。
酉性给 $|r_m|^2+|t_m|^2=1$，且由 (8) 每个 $t_m\ne0$。因此
$$
\begin{aligned}
|\Psi_j|&\ge1-|r_br_c|\\
&=1-\sqrt{(1-|t_b|^2)(1-|t_c|^2)}
\ge\frac{|t_b|^2+|t_c|^2}{2}>0.
\end{aligned}
\tag{22}
$$
最后一步是 $\sqrt{(1-A)(1-B)}\le1-(A+B)/2$。

周期的 $t_c=1/D_c$，而 $|D_c|\le\|PT^cP\|=\|T^c\|$。
所以已付的 (3) 无需任何相位算术条件便给
$$
\boxed{\quad
|\Psi_j|^{-1}\le578\,k_j^{10}
\exp\!\left(\frac{459}{500}|j|\right).
\quad}
\tag{23}
$$
这里 $578=2\cdot17^2$。此界只用了较短周期的 transmission 下界，
没有把桥的两个势区误合并成周期的单中央区，也没有假设未知的反射相位间隙。

## 5. 完整前缀内部、outgoing 和普通源

记
$$
I=(|I_L|^2+|I_R|^2)^{1/2},\qquad
F=((F^c)^2+(F^b)^2)^{1/2},\qquad
E_j^*=\exp\!\left(\frac{459}{500}|j|\right).
\tag{24}
$$
由 (20)、酉矩阵每项绝对值至多1、(19)、(23)，
$$
|u|\le578k^{10}E_j^*
\left(\frac32 I+120000000k^3F\right)
=867k^{10}E_j^*I+69360000000k^{13}E_j^*F.
\tag{25}
$$
源系数的放宽使用
$\sqrt{400^2+110000000^2}<120000000$；没有逐项假设两个源独立小。
又 $|v|\le I+|u|+400k^3F$，故两个模块 incoming 的 Euclidean 范数都满足
$$
I^c,I^b\le2I+|u|+400k^3F
\le1000k^{10}E_j^*I+7\cdot10^{10}k^{13}E_j^*F.
\tag{26}
$$

整个前缀的内部范数
$\mathcal N_j=\max(\sup|Z_j|,\|Z_j\|_{L^2(0,R_c+R_b)})$
至多 $\mathcal N^c_j+\mathcal N^b_j$。组合 (4)、(17)、(26)，利用 $k\ge1$
和 $E_j^*\ge1$，得到
$$
\boxed{\quad
\mathcal N_j\le2\cdot10^{11}k_j^{13}E_j^* I_j
+9\cdot10^{18}k_j^{16}E_j^*F_j.
\quad}
\tag{27}
$$
精确常数加法分别为 $100000200000<2\cdot10^{11}$ 和
$7004014000000040100<9\cdot10^{18}$。并未重新估算整个前缀的
指数型 Cauchy 传播，也没有把源项遗漏在级联之外。

此外，整个前缀的零源散射矩阵仍由完整真实传递矩阵定义，故酉。
对源部分取 $I=0$，由 (20) 全 outgoing 的范数至多
$|u|+|v|+|\eta^c|+|\eta^b|$。用 (19)、(25) 得
$$
|\eta^{\mathrm{full}}_j|
\le138830000800\,k_j^{13}E_j^*F_j
<\frac32\,10^{11}k_j^{13}E_j^*F_j.
$$
因此全 outgoing 还满足更好的单独估计
$$
\boxed{\quad
O_j\le I_j+\frac32\,10^{11}k_j^{13}E_j^*F_j.
\quad}
\tag{28}
$$
齐次 outgoing 在同一角权下酉，不损失解析带；内部 (27) 与普通源
(28) 仍如实具有 $459/500$ 的带损失。不能由前一句把后两句改成无损。

## 6. 全 Fourier 解的真实存在、正则性与唯一性

对 $\sigma\ge0$ 和实数 $\nu$ 定义
$$
\|h\|_{\sigma,\nu}^2
=\sum_{j\in\mathbb Z}e^{2\sigma|j|}k_j^{2\nu}|h_j|^2.
\tag{29}
$$
两个端口、两个内部变量和源的两分量使用同一权。记
$\delta_*=459/500$。若
$$
a\in X_{\sigma+\delta_*}^{\nu+13}(\mathbb C^2),
\qquad
g\in L^2_r X_{\sigma+\delta_*}^{\nu+16}(\mathbb C^2),
\tag{30}
$$
则整个同一精确前缀的 (2)、(7) 有唯一全模解，满足
$$
Z\in C_rX_\sigma^\nu\cap H^1_rX_\sigma^{\nu-1},
\tag{31}
$$
$$
\max\left(\sup_r\|Z(r)\|_{\sigma,\nu},
\|Z\|_{L^2_rX_\sigma^\nu}\right)
\le2\cdot10^{11}\|a\|_{\sigma+\delta_*,\nu+13}
+9\cdot10^{18}\|g\|_{L^2_rX_{\sigma+\delta_*}^{\nu+16}}.
\tag{32}
$$

证明先用每个固定模的真实存在及 (20)–(23) 解接口，再取有限 Fourier 部分和。
将 (27) 乘 $e^{\sigma|j|}k_j^\nu$ 后用 $\ell^2$ 三角不等式即得 (32)。
由 Tonelli，$\sum e^{2(\sigma+\delta_*)|j|}k_j^{2(\nu+16)}F_j^2$
就是 (30) 的源范数平方。两个部分和之差满足完全相同的估计，其右端为
数据的 Fourier 尾，故真正在 $C_rX_\sigma^\nu$ 和 $L^2_rX_\sigma^\nu$ 收敛。

全前缀 $|V|<1200$，所以从 (2)
$$
\|\partial_r Z\|_{L^2_rX_\sigma^{\nu-1}}
\le1200\|Z\|_{L^2_rX_\sigma^\nu}
+\|g\|_{L^2_rX_\sigma^{\nu-1}}.
\tag{33}
$$
同样的尾差估计使导数收敛。两个模块的界面 traces 相等在此极限保留，
没有额外的接口 delta 源。每模的唯一性保证全类唯一性；实数据的解由
$j\leftrightarrow-j$ 共轭对称为实。$\sigma>0$ 时任意严格子带中的角解析性
来自 Fourier 级数一致收敛；$\sigma=0$ 时 (31) 是通常 Sobolev 分布解。

对 outgoing，任意实数 $\lambda$ 在右端有限时还有
$$
\|b\|_{\sigma,\lambda}
\le\|a\|_{\sigma,\lambda}
+\frac32\,10^{11}\|g\|_{L^2_rX_{\sigma+\delta_*}^{\lambda+13}}.
\tag{34}
$$
均值不需要求逆 $j$：全长 $R_c+R_b<18/5$，并有
$$
z_+(r)=I_L+\int_0^r(Pg)_+\,dt,
\qquad z_-(r)=I_R-\int_r^{R_c+R_b}(Pg)_-\,dt.
\tag{35}
$$
故两个均值实际端口都保留，且 (27)–(34) 当然包含它。

若另有共同的多项式或 log 权，可将它同时乘入 (29)，证明不变；输入仍须
比输出多出真正的 $e^{\delta_*|j|}$。特别，负的超多项式 log 权不支付
这段正解析带宽。任意每模数值非零也不支付该 Fourier 求和步骤。

推广共同权时须保留其实际解释：若输出 $\sigma=0$ 且额外使用负的超多项式 log 权，
一般只得到系数完备化，未必是分布。基本空间 (29)–(34) 的 $\sigma\ge0$ 与多项式角阶
不受影响；正解析宽度压过该 log 因子。此说明不减少 (23) 的真实解析损失。

## 7. 物理普通源与原 GC 变量的明确换算

整个前缀 $a\le43/40$、$\bar p\ge1$。由 (1)–(2) 精确计算两个分量的
$L^2$ 单位：
$$
\|g\|_{L^2_r}^2
=\int\left(a^4\bar p^{-1}|f_1|^2+a^2\bar p^{-5}|f_2|^2\right)ds
\le(43/40)^4\|f\|_{L^2_s}^2.
\tag{36}
$$
所以全前缀可保守取 $\|g\|_2<(5/4)\|f\|_2$。
在周期上已有原变量界；在桥上 $a>59/100$、$\bar p<6$，因此
$$
\sup|U|\le216\sup|Z|,
\qquad
\|U\|_{L^2_s}^2
=\int(\bar p^3|x|^2+a^2\bar p^7|y|^2)dr
\le6^7\|Z\|_{L^2_r}^2.
\tag{37}
$$
周期的原变量换算比此更小；因 $\sqrt{6^7}<540$，全前缀两种范数可用
同一个540倍。于是 (27) 的物理版为
$$
\boxed{\quad
\max\left(\sup_s|U_j|,\|U_j\|_{L^2_s}\right)
\le2\cdot10^{14}k_j^{13}E_j^*I_j
+7\cdot10^{21}k_j^{16}E_j^*\|f_j\|_{L^2_s}.
\quad}
\tag{38}
$$
同样，$O_j\le I_j+2\cdot10^{11}k_j^{13}E_j^*\|f_j\|_{L^2_s}$。
所有换算只依赖径向变量，所以相同的全角范数结论成立。

这里 $I_j,O_j$ 始终是 (7) 中 **Sturm 变量** 的端口。在核心侧 $a=1,c=0$
有 $Z=U$；在 cut 侧则必须先应用 (1)。没有把两端不同的坐标缩放省略。

## 8. 本稿没有支付的实际闭合门

上述命题给同一真实全前缀、任意声明的解析输入、全部整数模和普通 $L^2$
源的完整辅助解。没有仅将酉性当成内部估计；桥的真实单屏障源估计、两个
模块的接口源列及所有 Fourier 极限均已明写。

它仍不等于实际曲面问题的逆。平面核心要求自己的反射关系；真尾在当前
非径向高度处的 $DT(H)$ 通常耦合所有角模。还须解实际端点反馈差矩阵，
处理 mean、几何闭合/标量行、相应 range，以及完整无限尾的普通源。
当前非径向候选的线性化也不再是 (2) 的径向 Fourier 对角系。

这里的固定解析损失和很大的有效常数不能直接送入反复使用同一宽度的
非线性 Newton 迭代；也没有证明当前实际 core 的解析带及范数满足 (30)。
不能据此声称当前真实候选的 $K_0$、无带损失的 weighted inverse、
任意精度同 $g$ 收敛、全非线性闭面族或 README/G5 已完成。

同一固定整数频率反射相位的更强间隙仍可能改进 (23)，但目前未付。
本稿的结论不依赖把实际二次到一次退化接点替换成另一简单根模型。


## 9. 正式采纳与完整独审

[冻结原稿](../notes/2026-11-10-78718-geometry-full-prefix-analytic-source-v1.md)，14624 B，
SHA256 60e587e72b27eb75951ba6ed9a46d380c187520fde77098363dc2fb1f359e216；
根实际 3c517a 全文读。[八节全文独审](../notes/2026-11-10-78718-audit-full-prefix-analytic-source-v1.md)，
14704 B，SHA256 ea05f99b015806f82135fee76ebc9631296e5f5accf3eb5d5d7617fd9704d57b，
根实际 61a642 全文读。审者未参与本证明或候选优化，核桥弱源、通量、周期17常数、
两源反馈、实际Fourier极限和物理Jacobian，无实质缺口。

独审实际 c4d608 自然 exit 0，独立重跑 scripts/78718-geometry-full-prefix-analytic-source-check.py；
36 有理门，0 PDE、0 tail、0 候选数组。
[独立报告](../notes/2026-11-10-78718-audit-full-prefix-analytic-source-check-01.json)，2035 B，
SHA256 559b636ced9e2227d32cf4eeceedb1d1c9754214507d361813d3300a5b65ea8d。
有限算术不替代全文证明。正式稿只改标题、状态、相对链接，更新R79已审状态，并按独审明确
额外负log权的分布范围；公式和证明不变。第8节全部未付门保留。
