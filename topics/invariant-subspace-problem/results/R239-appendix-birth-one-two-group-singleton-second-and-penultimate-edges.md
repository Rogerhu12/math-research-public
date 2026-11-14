# R239 附录：两组任意重数加一异常位的整个出生一第二及末第二相邻边

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文给出完整有限模型定理。新增范围是任意两个组大小、任意高度的第二和末第二边；一般内部高度、一般多权及普通 ISP 仍开。独立精确证书为 [独立整数程序](../notes/2026-11-14-birth-one-second-edge-uniform-certificate-0c.py)，只依赖 SymPy 的有理数多项式运算，不读取任何临时表或外部数据。

## 1. 全空间定理及与已有结果的区分

取 q,L≥1 个权分别为 a,b 的物理位，另有一位权 c，均严格正。整体缩放后置 b=1、z=a²、w=c²。写 N=q+L，故总物理位数为 N+1，出生一的高度 h=N−1。令

$$F_n=\frac{D^n(D^*)^n}{(n!)^2}\big|_{\mathcal H_1},\qquad
K_1=\ker D\cap\mathcal H_1,\qquad
\Gamma_n=P_{K_1}F_n^{-1}|_{K_1}.$$

这里所有逆先在完整物理层上取。

**定理。** 若 N≥4，则在整个 K_1 上严格有

$$\boxed{\Gamma_2\Gamma_3^{-1}\Gamma_2\prec\Gamma_1,}\tag{1.1}$$

以及

$$\boxed{\Gamma_{h-2}\Gamma_{h-1}^{-1}\Gamma_{h-2}
\prec\Gamma_{h-3}.}\tag{1.2}$$

所有指标均是合法高度；N=4 时两式是已有首末边的两个位置。结合任意正权出生一首末边定理，当前权型的第一、第二、末第二、末第一边全部已付，但当 h 更大时不声称它们覆盖中间各边。

组大小最小值≤3 的整个高度此前已经证明：短组一由[两异常权稿](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)的全出生结论支付，短组二由[三异常权出生一稿](R271-appendix-three-exceptional-weights-full-birth-one-primitive-gram-bound.md)支付，短组三由[三位等权短串加一异常位](R239-appendix-three-equal-short-weights-one-exceptional-birth-one-and-all-births.md)的出生一全高度及全部 primitive 结论支付。交换两组、同时以新池权作整体缩放，保持这些范围。故本次新证明只需 q,L≥4；没有把有限 q 范围外推至任意 q。

## 2. 先支付两类组内不可约分量

S_q×S_L 的真实正交分解为

$$K_1=V_{\rm short}\oplus V_{\rm pool}\oplus K_{\rm fix},\qquad
\dim K_{\rm fix}=2.$$

组内坐标和为零的部分均包含于 primitive，且 D、D*、完整 F_n 及其逆与两组置换交换，因此这个分解约化 Γ_n。

若 q≥2，完整 F_n 在短组标准部分的标量为

$$e_n(z^{[q-2]},1^{[L]},w).$$

确实，对角项是删去一短位后的 e_n，非对角项是 z 乘删去两短位后的 e_(n−1)，两者之差准确等于上述系数。池标准部分同理给 e_n(z^[q],1^[L−2],w)。两个序列均由 h 个严格正变量生成，故 Newton 不等式给它们的倒数在每个内部位置严格 log 凸。相应零维部分直接删除。

所以只需证明同一个完整固定二维块；不能用该块代替未处理的组内部分。

## 3. 完整固定源及实际真空系数

用已经自足证明的[出生一真空归约](R239-appendix-birth-one-two-group-singleton-vacuum-reduction.md)。为明确同源性，首一源坐标 (α,β) 的真实源 Gram 是

$$H_0=K_0\begin{pmatrix}1+w/L&w/L\\w/L&w/L+w/(qz)\end{pmatrix},
\qquad K_0=(q!)^2z^q.$$

它来自物理源振幅：单独位 q!z^(q/2)α、每短位 (q−1)!z^((q−1)/2)√w β、每池位 −q!z^(q/2)√w(α+β)/L。三个组的加权总源之和为零。这一基对全部高度相同。

定义

$$Z_j=[x^j](1+zx)^q(1+x)^L,\qquad
P_j=[x^j](1+zx)^{q-1}(1+x)^{L-1},$$

并置 P_(−1)=0、

$$D_i=P_i^2-P_{i-1}P_{i+1}\quad(i\ge0),\qquad D_0=1.$$

所有本次使用的 Z_j,D_i 均严格正。D_i 的严格正性由普通 Newton 不等式给出，包括 i=0。

若 m_j=Θlog Z_j、v_j=Θ²log Z_j、Θ=z∂_z，则有

$$\boxed{Z_j^2v_j=qLz\,D_{j-1}.}\tag{3.1}$$

这里也有直接有限证明：普通 j 元子集中，任意一个短位与一个池位的协方差是 −zD_(j−1)/Z_j²；因两组总占据数相加恒为 j，短组计数方差等于全部 qL 个交叉协方差之负和。两位协方差公式由展开删位初等对称和逐项核验。

将共同正数 K_0 除去。实际高、低首一范数因而准确为

$$a_j=1/Z_j,\qquad b_{j-1}=Z_j/(C D_{j-1}),\qquad C=qLz>0.\tag{3.2}$$

这些公式来自完整 MP，所有端点已由真空归约中的强制根证明。此次 n=2 的三个位置是 1,2,3，q,L≥4 保证全部所需旧范数在合法内部。

进一步在所有高度作同一个源替换 β=√C β_new。于是低范数变成

$$\widetilde b_{j-1}=Z_j/D_{j-1},$$

高范数 a_j 不变，shear 除以 √C。这个可逆合同不改变相邻不等式。

## 4. n=2 的完整四次式和三项固定次数分子

以下只用局部代数记号

$$e=Z_1,\quad f=Z_2,\quad g=Z_3,\quad \ell=Z_4,\qquad
E=D_0=1,\quad F=D_1,\quad G=D_2,\quad H=D_3.$$

令

$$a=1/e,\ b=1/f,\ c=1/g,\ d=1/\ell,
\qquad p=e/E,\ Q=f/F,\ r=g/G,\ s=\ell/H.$$

普通组大小仍叫 q；局部低范数 Q 与它不同。准确 Pearson 身份在共同缩放后给

$$X=(eF-gE)/2,\qquad Y=(fG-\ell F)/3,\qquad
\chi=qLz(z-1)^2,$$

$$x=-\frac{\sqrt\chi\,X}{efg},\qquad
y=\frac{\sqrt\chi\,Y}{fg\ell}\quad(z\ge1).\tag{4.1}$$

z=1 时两 shear 都为零，公式直接成立。它也可通过 c_j=−q(q−1)/2−Θlog Z_j、实际二阶系数递推直接相减核验。

把中心 shear 用一个共同剪切消为零，令

$$A_-=a+wb,\quad A_0=b+wc,\quad A_+=c+wd,$$

$$B_-=\frac{wpQ}{p+wQ},\quad B_0=\frac{wQr}{Q+wr},\quad
B_+=\frac{wrs}{r+ws}.$$

实际差 K=H_1−H_2H_3^−1H_2 的首主子式为

$$K_{11}=A_--A_0^2/A_++B_-x^2>0.\tag{4.2}$$

严格性来自旧 a 序列的严格 log 凸及固定正线性和的 Cauchy–Schwarz；此处还可直接用 Z_j 的 Newton 界。

令

$$\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),$$

$$\Phi=pQ(Qs-r^2)+wQr(ps-Qr)+w^2rs(pr-Q^2).$$

完整行列式的正分母清除恰为

$$\mathcal P(w)=\det K\,(p+wQ)(Q+wr)^2(c+wd)s/w,$$

$$\begin{aligned}
\mathcal P={}&Q\Lambda\Phi
-wpQ^3r(c+wd)(r+ws)x^2\
&-wQ^2r^2s(a+wb)(p+wQ)y^2
-2wpQ^2rs(b+wc)(Q+wr)xy\
&-w^2pQ^3r^2s x^2y^2.
\end{aligned}\tag{4.3}$$

这是此前完整二维 shear 的同一个真实四次式；所有正分母都保留。其首末系数为

$$\mathcal P_0=pQ^2(ac-b^2)(Qs-r^2)>0,$$

$$\mathcal P_4=Qrs(bd-c^2)(pr-Q^2)>0.$$

旧低范数序列的严格比较由[两权全高度定理](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)支付。

将 (4.1) 代入另外三个系数，逐项清除单项式分母，准确得到

$$\mathcal P_i=N_i/\mathcal D_i\quad(i=1,2,3),$$

$$\mathcal D_1=\mathcal D_3=EF^3G^2Heg\ell,
\qquad\mathcal D_2=EF^3G^2Hefg^2\ell>0.\tag{4.4}$$

独立证书从 (4.3) 的有限乘积重新生成全部系数与这三个分母。N_1,N_2,N_3 分别有 11、19、11 个通用单项式，不含依赖物理组大小的枚举。为便于纸面核对，两个外侧中间分子可压成

$$\begin{aligned}
N_1={}&(f^2-eg)g\ell(FGe\ell-EHfg)\
&+(fg-e\ell)ef(G^2f\ell-FHg^2)\
&+\chi(2GXYe\ell-FY^2eg-HX^2f\ell),
\end{aligned}\tag{4.5}$$

$$\begin{aligned}
N_3={}&(fg-e\ell)g\ell(F^2eg-EGf^2)\
&+(g^2-f\ell)ef(FGe\ell-EHfg)\
&+\chi(2FXYe\ell-EY^2eg-GX^2f\ell).
\end{aligned}\tag{4.6}$$

最后一行是仍须付的真实 shear 费用，不能只凭前两行正就宣布完成。以下对全部实际参数一次支付三个分子。

## 5. 任意组大小的完整整数正系数证书

先取 z≥1；令

$$q=4+x,\quad L=4+y,\quad z=1+u,\qquad x,y,u\ge0.$$

对 j=0..4，证书准确生成

$$Z_j=\sum_{r=0}^j\binom{4+x}{r}\binom{4+y}{j-r}(1+u)^r,$$

$$P_j=\sum_{r=0}^j\binom{3+x}{r}\binom{3+y}{j-r}(1+u)^r,$$

其中每个二项式是有限下降积除以 r! 的有理系数多项式。随后准确构造 D_i、X、Y、χ，并将它们完整代入 (4.3)–(4.4)，不对 x,y,u 取样。

这是固定次数的有限计算。先验总次数上界为

$$\deg(e,f,g,\ell)\le(2,4,6,8),\quad
\deg(E,F,G,H)\le(0,4,8,12),$$

$$\deg X\le6,\quad\deg Y\le12,\quad\deg\chi\le5.$$

由全部通用单项式逐项相加，得到 deg N_1≤44、deg N_2≤52、deg N_3≤40。证书展开整个有限多项式；没有把某些采样列、某一段 z 次数或缺失单项式当作全部系数。

为使结果完全为整数，分别乘下表的公共正分母。逐个非零系数检查，结果为：

| 分子 | 公共分母倍数 | 正整数项数 | 负项数 | 总次数 | 最小系数 | 常数项 |
|---|---:|---:|---:|---:|---:|---:|
| N_1 | 2,985,984 | 4,324 | 0 | 44 | 5 | 10,576,038,020,618,649,600 |
| N_2 | 5,971,968 | 6,930 | 0 | 52 | 3 | 21,321,292,649,567,197,593,600 |
| N_3 | 497,664 | 3,311 | 0 | 40 | 5 | 352,534,600,687,288,320 |

每个常数项严格正。因此对所有实 x,y,u≥0 已有 N_i>0，特别覆盖全部整数 q,L≥4 和全部 z≥1。这个结论是准确多项式恒等式与全系数正性，不是从有限参数扫描外推。

证书无临时数据依赖：用 QQ 多项式环精确生成二项式下降积及所有乘积，按单项式指数完整收集系数；乘相应固定分母后，逐项断言其为严格正整数，再核项数、次数、最小值、常数项。它在当前环境完整运行，三项全部 PASS。证书还准确断言 (4.4) 的三个分母、11/19/11 个通用项以及 (4.5)–(4.6) 两紧式，末尾由一个独立实际完整3×3逆核准共同源缩放和整个行列式因子；一般参数的结论仍来自前述完整整数多项式证书。不存在浮点符号判定。

## 6. 拼回全部正权、全部源和对偶边

由 (4.4) 和 §5，三个中间系数严格正；首末系数已经严格正。因此对每个 w>0，P(w)>0，所有清除因子又严格正，故 det K>0。结合 (4.2)，K 严格正定，得到固定二维块的 (1.1)。§2 的两个完整组内分量同时严格，正交直和即给整个 K_1。

当 0<z<1，交换两普通组，并以原短组权作整体归一，新的参数为

$$(q,L,z,w)\longmapsto(L,q,z^{-1},w/z).$$

新的 z 大于一，两个组大小仍至少四。物理置换和同一整体权缩放保相邻比较，故覆盖全部 z>0。较小组大小≤3 的全部权型使用 §1 已说明的已发表完整结论。

最后，对同一个出生一空间使用[真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)定理1及§5。它以同一个可逆源合同把 Γ_n 与倒数权模型的 Γ_(h−n) 对应。将 (1.1) 应用于倒数权，得到反向相邻 Schur 式；对正定矩阵使用

$$AB^{-1}A\prec C\iff AC^{-1}A\prec B$$

即可得到 (1.2)。这里没有把每层换成不同源坐标，也没有把完整层逆替换成压缩原 Gram 的逆。

本定理没有给 n=3..h−3 的一般内部比较。继续的实际目标是把 (4.3) 的通用分子与同一 Z_j 的全局负实根正核或更长正递推相接；这一步不能由本次第二边证书自动外推。
