# 同一精确全前缀弱解析普通源解算器：全文独审

日期：2026-11-10。审者：Astra-visible-flex-78718bd0 / independent_audit。

## 0. 结论、对象和审查范围

**全文数学审查及冻结有限算术的真实独立重跑通过。** 被审稿为 [geometry-full-prefix-analytic-source-v1](2026-11-10-78718-geometry-full-prefix-analytic-source-v1.md)，14624 B，SHA256 `60e587e72b27eb75951ba6ed9a46d380c187520fde77098363dc2fb1f359e216`。全部八节已实际完整读取：`7e80e4`、`da789e`、`b270e1`。审者未参与该稿或其反馈粗下界构造，也没有参与主候选参数优化。

准确结论是固定 flat17 第一周期加 R21 同一个唯一精确桥的径向线性 GC 辅助二端口问题：全部整数 Fourier 模及普通径向 $L^2$ 两分量源都有真实内部解和输出，支付确定解析宽度 $\delta_*=459/500$，内部 incoming／source 分别支付 13／16 个角阶，普通源到 outgoing 支付 13 阶。均值、开放平段、二次到一次的接口均保留。

这些有限常数很大；本稿不证明当前 core 输入有足够解析带，不解真实外端 support／非线性尾反馈，不给当前非径向算子的逆，也不完成非线性闭面或 G5。旧主 g 的精确桥存在性继续接受，不把旧几何 metric-transfer 证书挪给新图。

## 1. 已审输入形成的非循环依赖

本次使用以下真实已完整审查的输入：

1. [R75](../results/R75-flat17-sturm-frequency-propagator.md) 的完整物理 Sturm 变换、周期能量、$\Omega<459/1000$ 和 $Z$ 变量的常数 17。已额外实际 `cdc429` 核正式正文 (25)–(28)：17 确为 $Z$ 的界，并非把 $U$ 的 20 错写为 17。
2. [R76](../results/R76-flat17-internal-ordinary-source-provider.md) 的普通 $L^2$ 弱源 Green 表达、全端点／通量闭合及周期 200／40100／400 界。其完整审稿为 [audit-flat17-internal-source-provider-v1](2026-11-10-78718-audit-flat17-internal-source-provider-v1.md)，15491 B，SHA256 `fcebc620ab62dd1d56981074c27d14a33da7d3be273464a455acac793f2ead87`。
3. 同一精确桥势／反馈原稿，以及本审刚完成的 [全文独审](2026-11-10-78718-audit-bridge-two-barrier-feedback-v1.md)，13074 B，SHA256 `b2ce9b33cbc3ba2d292de0b8a89a5cae5d17448a3833205fef01110f081c5f79`：$R_b<21/10$，负势区从桥左端开始，其后为正势外区；$|V|<1200$，外区双向界 $3100k^2$，$a_c\le a\le1$、$a_c>59/100$、$1\le\bar p<6$。

第三项原稿的“待审”是写作时状态，原文件仍冻结；这里的输入已由另一个完整独审实际支付，不是两个待审稿互相引用。R76 的 Green 引理对任意连续非负势成立，它没有依赖本篇的桥组合或反馈界，因此不存在循环论证。

全前缀沿用
\[
Z=\operatorname{diag}(a/\bar p,\bar p^{-3})U,
\quad dr/ds=(a^2\bar p)^{-1},
\]
\[
Z_j'=-ij\begin{pmatrix}0&V\\1&0\end{pmatrix}Z_j+g_j,
\quad g=(a^3f_1,a^2\bar p^{-2}f_2)^T.
\]
第一周期和桥的公共截面有 $a=1,c=0,\bar p=1$，角坐标也相同，故此处没有漏掉接口换基；右 cut 则必须保留其真实对角变换。

## 2. 桥的固定每模真实存在和通量

桥势连续、区间有限，每个固定 $j$ 的线性 ODE 有真实基本解。$g_j\in L^2$ 在有限区间属 $L^1$，故变常数积分存在并给绝对连续解；右端属于 $L^2$，所以解在 $H^1$。

设 $J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$、Hadamard 矩阵 $P$。系数满足 $A_j^*J+JA_j=0$、trace 为零，因此 $PTP$ 为 determinant 一的 $\operatorname{diag}(1,-1)$-unitary。记其 entries 为 $A,B,C,D$，比较逆矩阵可得 $C=\bar B,D=\bar A,|D|^2-|B|^2=1$。特别每个有限模的 $D$ 非零。

对真实源积分 $w=P\int T(R,t)g(t)dt$，指定 $z_+(0)=a_1,z_-(R)=a_2$ 后，唯一的另一初值是 $(a_2-Ca_1-w_-)/D$。本稿因此先建立每模解，不以先验估计冒充存在。

精确端口重排仍给
\[
|Z(0)|^2+|Z(R)|^2=I^2+O^2,
\quad E=|Z(0)|+|Z(R)|\le\tfrac32(I+O).
\]
实际 $H^1$ 解的通量积分为
\[
O^2-I^2=2\Re\int Z^*Jg\le2\|Z\|_2F.
\]
这些与 R76 的端点排列完全一致。零源散射矩阵的两 cross entries 都是 $1/D$，不为零；逐模存在的结论没有升级成尚未支付的全频无损逆。

## 3. 整桥普通源：Green 的合法应用和全部常数

负势部分恰从桥左端起，长 $\ell_b<R_b$。置 $q=-j^2V\ge0$，原一阶系统在弱意义给
\[
(-\partial_r^2+q)y=ijg_1-\partial_r g_2.
\]
R76 已完整证明 $0\le G\le\ell_b/4$、$|G_t|\le1$，以及通过 $L^2$ 光滑逼近和 $H^1_0$ 能量识别的
\[
y-y_h=ij\int Gg_1+\int G_tg_2.
\]
这里 $g_2'$ 不是新增的 $L^2$ 数据；源无边界迹也合法。齐次 $y_h$ 的模平方凸，故由两端实际 $y$ 值控制。桥的负势区端点有零势，不影响该引理。

由 $R_b<21/10$ 得 $\sqrt{R_b},\sqrt{\ell_b}<3/2$，且
\[
\ell_b^{3/2}/4+\sqrt{\ell_b}
< (21/10)(3/2)/4+3/2=183/80.
\]
以 $k=\sqrt{1+j^2}\ge1$、$|j|\le k$，原稿 (11) 正确。

从全桥右端向后，外区任意点及负势区右边界满足
$|Z|\le3100k^2E+4650k^2F$；负势区左边界就是全桥左端，其范数 $\le E$，也被该式控制。于是
\[
Y:=\sup_{[0,\ell_b]}|y|\le3100k^2E+4653k^2F,
\]
因为 $4650+183/80<4653$，并可用 $k\le k^2$。这里不能假设有一段不存在的左外区；本稿确实直接用了全桥左端。

不除 $j$ 地积分第一分量，并用 $1200\ell_b<2520$：
\[
X:=\sup|x|\le E+2520kY+\tfrac32F.
\]
合并得到
\[
X+Y\le7815101\,k^3E+\frac{23460429}{2}\,k^3F
<12000000k^3(E+F).
\]
两个精确系数分别是 $1+2521\cdot3100$、$2521\cdot4653+3/2$；用 $k\ge1$ 吸收低次项，所有方向合法。外区更小。再乘 $\sqrt{R_b}<3/2$ 并用端口的 $E\le3(I+O)/2$，给
\[
\mathcal N^b\le18000000k^3(E+F)
\le27000000k^3(I+O+F).
\]

将此代入真实通量，三种情形 $O\le I$、$O>I$ 且 $I+O\ge F$、$I+O<F$ 完全覆盖。中间情形除正数 $I+O$ 得
$O-I\le4\cdot27000000,k^3F=108000000k^3F$，所以统一放宽至
\[
O^b\le I^b+110000000k^3F^b.
\]
回代内部：incoming 系数 $54000000<10^8$；源系数
$27000000(110000000+1)=2970000027000000<4\cdot10^{15}$，得
\[
\mathcal N^b\le10^8k^3I^b+4\cdot10^{15}k^6F^b.
\]
零模从未除以 $j$，包含在整个推导中。常数的粗大不影响其严格有效性，但不得由其声称可见幅度已付。

## 4. 内部反馈的无相位算术粗界

两个模块的仿射源输出由零 incoming 的真实解定义：
\[
|\eta^c|\le400k^3F^c,\qquad
|\eta^b|\le110000000k^3F^b.
\]
接口 $u$ 为周期右 incoming／桥左 outgoing，$v$ 为桥左 incoming／周期右 outgoing，精确式为
\[
v=S^c_{21}I_L+S^c_{22}u+\eta_R^c,
\quad u=S^b_{11}v+S^b_{12}I_R+\eta_L^b.
\]
所以 $\Psi=1-r_br_c$，消元右边同时有 $r_b\eta_R^c$ 和 $\eta_L^b$，没有漏掉其中一个模块的普通源。

已审 AM–GM 平方差给
\[
|\Psi|\ge\frac{|t_b|^2+|t_c|^2}{2}\ge\frac{|t_c|^2}{2}.
\]
周期 $t_c=1/D_c$，$P$ unitary，故
\[
|D_c|\le\|PT^cP\|=\|T^c\|
\le17k^5e^{(459/1000)|j|}.
\]
这给 $|t_c|\ge(17k^5e^{(459/1000)|j|})^{-1}$。取平方再倒数，准确得到
\[
|\Psi|^{-1}\le2\cdot17^2 k^{10}e^{2(459/1000)|j|}
=578k^{10}e^{(459/500)|j|}.
\]
此界不需要桥 transmission 的定量下界，更没有需要未证的整数相位间隙。不能把它误读成统一多项式界：指数代价确实存在，而且已计入后续解析宽度。

## 5. 两源、内部角阶和全 outgoing 的独立核算

记 $E_j^*=e^{(459/500)|j|}$，$I=\sqrt{|I_L|^2+|I_R|^2}$，$F=\sqrt{(F^c)^2+(F^b)^2}$。酉矩阵 entries 模至多一。接口消元右侧 incoming 的两个绝对值之和 $\le\sqrt2I<3I/2$；source 的和由二维 Cauchy–Schwarz 包围为
\[
400F^c+110000000F^b
\le\sqrt{400^2+110000000^2}F<120000000F.
\]
故
\[
|u|\le867k^{10}E_j^*I+69360000000k^{13}E_j^*F.
\]
而 $|v|\le I+|u|+400k^3F$。周期 incoming norm $\le I+|u|$，桥 incoming norm $\le I+|v|$，二者都被
\[
2I+|u|+400k^3F
\le1000k^{10}E_j^*I+7\cdot10^{10}k^{13}E_j^*F
\]
控制。最后一步只用 $k\ge1,E_j^*\ge1$，没有额外假设源分别小。

全域 sup 至多两个模块 sup 之和，全域 $L^2$ 为两段平方和的平方根，亦至多两个模块 norm 之和。因此
\[
\mathcal N\le\mathcal N^c+\mathcal N^b
\le2\cdot10^{11}k^{13}E_j^*I+9\cdot10^{18}k^{16}E_j^*F.
\]
真实合并系数为
\[
(200+10^8)1000=100000200000,
\]
\[
(200+10^8)7\cdot10^{10}+40100+4\cdot10^{15}
=7004014000000040100.
\]
它们严格落在所取整数界内。13 阶来自接口 10 阶加内部 3 阶；source 的 16 阶来自接口 10、模块源 3、内部 3。剩余模块直接源的 6 阶被同一 $k^{16}E_j^*$ 包含。

另外，全前缀真实传递本身仍 $J$-unitary 且 det 一，故齐次全散射酉。不能用上式对齐次 outgoing 人为收取指数。对 $I=0$ 的源解，外端输出 norm 至多
\[
|u|+|v|+|\eta^c|+|\eta^b|.
\]
此时 $|v|\le|u|+400k^3F$，所以该源输出系数为
\[
2\cdot69360000000+2\cdot400+110000000
=138830000800<\tfrac32\cdot10^{11}.
\]
由线性叠加与齐次酉性，得到
\[
O\le I+\tfrac32\cdot10^{11}k^{13}E_j^*F.
\]
该单独边界估计确实比内部 source 的 16 阶更强；本稿没有混同两者。

## 6. 全 Fourier 求和、界面 traces 和真实正则性

对于 $\sigma\ge0$ 和实 $\nu$，本稿基本空间为指数权 $e^{\sigma|j|}k_j^\nu$ 的 Hilbert 空间。输入要求
\[
a\in X_{\sigma+\delta_*}^{\nu+13},
\quad g\in L^2_rX_{\sigma+\delta_*}^{\nu+16},
\quad \delta_*=459/500.
\]
每模先由两个模块和非零 $\Psi$ 解出唯一实际解；接口处两侧的 $(z_+,z_-)$ 均为 $(v,u)$，故完整 $Z$ 的 traces 相同。有限段 $H^1$ 函数以相同 trace 拼接即为全段 $H^1$，弱导数没有界面 delta 项。源只需两段 $L^2$，不需要在接口相等或有端点值。

先取有限 Fourier 部分和，逐模乘 $e^{\sigma|j|}k_j^\nu$ 后用 $\ell^2$ Minkowski；$E_j^*$ 恰被输入的 $\sigma+\delta_*$ 吸收。源的模平方和与 $L^2_r$ 范数由 Tonelli 识别。对两个部分和差，用完全同一估计，其右端变为输入 Fourier 尾，趋于零，因此在 $C_rX_\sigma^\nu$ 和 $L^2_rX_\sigma^\nu$ 都真正收敛。这不是形式逐模声明。

全域矩阵范数至多 1200，乘 $j$ 从阶 $\nu$ 到 $\nu-1$ 有 norm 至多一。因此
\[
\|Z_r\|_{L^2_rX_\sigma^{\nu-1}}
\le1200\|Z\|_{L^2_rX_\sigma^\nu}+\|g\|_{L^2_rX_\sigma^{\nu-1}}.
\]
同样用于部分和差，得到导数收敛及 $H^1_rX_\sigma^{\nu-1}$。输入给出的 source 阶与宽度足够嵌入该右端空间。界面及外端 traces 在强连续 norm 极限中保留，实际方程在分布意义成立。

任何另一同类解逐坐标满足同一每模 ODE／端口条件，因此由每模唯一性相同。实数据的 $j\leftrightarrow-j$ 共轭对称也被唯一性保留。$\sigma>0$ 时严格子带内的 Fourier 级数及角导数一致收敛，给角解析性；基本权的 $\sigma=0$ 情形为通常 Sobolev 分布解。此处仍只声明径向 $H^1$，没有从仅 $L^2$ 源凭空推出经典径向 $C^1$。

按更强单独 outgoing 界，任意实际有限的右端范数给
\[
\|b\|_{\sigma,\lambda}\le\|a\|_{\sigma,\lambda}
+\tfrac32\cdot10^{11}\|g\|_{L^2_rX_{\sigma+\delta_*}^{\lambda+13}}.
\]
$j=0$ 直接积分 $z'=Pg$，全长 $R_c+R_b<18/5$，两个均值端口完全保留；没有除零或均值伪逆。

额外共同的多项式／log 权可以逐模同乘，代数不变，但不能支付或抵消 $e^{\delta_*|j|}$。此推广的分布解释仍遵守 R76：若 $\sigma=0$ 且再加负超多项式 log 权，一般只能视作系数完备化；若保留正 $\sigma$，指数衰减压过该 log 因子。原基本空间 (29)–(34) 没有这个歧义。

## 7. 物理源、径向 Jacobian 与 cut 的端口尺度

$dr=ds/(a^2\bar p)$，所以直接变元给
\[
\|g\|_{L^2_r}^2=int(a^4\bar p^{-1}|f_1|^2+a^2\bar p^{-5}|f_2|^2)ds.
\]
全域 $a\le43/40,\bar p\ge1$，故两个系数都不超过 $(43/40)^4$，取平方根得到 $(43/40)^2<5/4$。这里没有把 $L^2$ 坐标 Jacobian 省掉。

$U=\operatorname{diag}(\bar p/a,\bar p^3)Z$。桥上第一对角因子 $<6/(59/100)<216$，第二 $<216$，周期的界更小，所以全域 pointwise 倍数可取 216。

反向 $L^2$ 变元给
\[
\|U\|_{L^2_s}^2=int(\bar p^3|x|^2+a^2\bar p^7|y|^2)dr.
\]
在桥上 $a\le1,\bar p<6$，两个因子都小于 $6^7$；周期已审的换算远小于此界。$6^7<540^2$，因此 full sup 和 $L^2$ 共同可用 540 倍。

代入内部界，$540(2\cdot10^{11})<2\cdot10^{14}$、$540(5/4)(9\cdot10^{18})<7\cdot10^{21}$，得到原稿 (38)；输出源系数 $(5/4)(3/2)10^{11}<2\cdot10^{11}$。这几个数都是合法放宽，不声称精锐常数。

$I,O$ 一直指 Hadamard **Sturm** 端口。在左端 $Z=U$；右 cut 的 $a,c,\bar p$ 不同，须先按 (1) 转换再分组。作者 §7 明确保留这一点，没有把右端原 GC 的两个分量当作已正交归一的同一端口。

## 8. 冻结 checker 的真实独立重跑与适用边界

全文阅读有限 checker（`c4d8cb`）：`78718-geometry-full-prefix-analytic-source-check.py`，4539 B，SHA256 `29cd7113eaf633d565b171ff9f21f0fe6c1629bbd2ba12cc4dc7d25d98a92fe4`。所有除法有 Fraction 操作数或整数精确表达，不借 binary 浮点误差来完成常数门。它只核 36 项有限有理恒等／不等式，记录原稿、桥稿、R75、R76 的实际身份；不自称重证 Green 或构造 PDE 解。

**c1cdab exit 0** 已核完整原稿 14624 B/SHA、checker 与作者报告相同身份，以及作者报告四份源的全部字节／SHA。随后实际独立命令为：

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
scripts/78718-geometry-full-prefix-analytic-source-check.py
--report notes/2026-11-10-78718-audit-full-prefix-analytic-source-check-01.json
```

cwd 为本题目录，**c4d608，自然 exit 0**。36 有理门通过，0 PDE、0 tail、0 候选数组。独立报告 [audit-full-prefix-analytic-source-check-01.json](2026-11-10-78718-audit-full-prefix-analytic-source-check-01.json)，2035 B，SHA256 `559b636ced9e2227d32cf4eeceedb1d1c9754214507d361813d3300a5b65ea8d`。与作者报告同值是实际确定性复跑，不是借用作者回执。

全文没有实质缺口。此模块真实推进了整个同一精确前缀的辅助内部／普通源解算器；固定解析损失和巨大常数不能直接用于反复消费同一带宽的非线性 Newton，也没有证明当前 core 满足输入宽度或 norm。当前非径向线性化、真实外端反馈、无限尾 source、原选定 range／scalar 行和最终闭图仍必须各自支付。不能把本稿登记为主问题完成。
