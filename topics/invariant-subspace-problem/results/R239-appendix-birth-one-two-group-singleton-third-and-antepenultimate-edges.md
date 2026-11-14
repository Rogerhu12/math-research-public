# R239 附录：两组任意重数加一异常位的整个出生一第三与末第三边

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：完整有限模型定理。本文新增任意两组大小、任意权比的第三和末第三相邻边，并把已证全高度普通权比扇区扩大。一般大普通权比的更内部边、一般出生及普通 ISP 仍开。独立证书为 [独立整数证书](../notes/2026-11-14-birth-one-third-edge-uniform-certificate-0c.py)，仅使用 SymPy 精确有理数多项式，不读取临时数据。

## 1. 整个原源空间的定理

取 $q,L\ge1$ 个物理位的权分别为 $a,b$，另一个物理位权为 $c$，全为严格正数。整体缩放后令
$$z=a^2/b^2,\quad w=c^2/b^2,\quad N_{\rm tot}=q+L,\quad h=N_{\rm tot}-1.$$
总物理位数为 $N_{\rm tot}+1$。用完整物理层的真逆定义
$$F_j=D^j(D^*)^j/(j!)^2\big|_{\mathcal H_1},\qquad
K_1=\ker D\cap\mathcal H_1,\qquad
\Gamma_j=P_{K_1}F_j^{-1}|_{K_1}.$$

**定理 1。** 若 $N_{\rm tot}\ge5$，则在整个 $K_1$ 上严格有
$$\boxed{\Gamma_3\Gamma_4^{-1}\Gamma_3\prec\Gamma_2,\qquad
\Gamma_{h-3}\Gamma_{h-2}^{-1}\Gamma_{h-3}\prec\Gamma_{h-4}.}\tag{1.1}$$
当指标重叠或落在已付首两边中，按同一个不等式读取。本文从不先压缩 $F_j$ 再取逆。

$\min(q,L)\le3$ 的所有高度已由下列完整旧定理支付：短组一用 [两异常权](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)，短组二用 [三异常权](R271-appendix-three-exceptional-weights-full-birth-one-primitive-gram-bound.md)，短组三用 [三位等权短串加一异常位](R239-appendix-three-equal-short-weights-one-exceptional-birth-one-and-all-births.md)。交换两组并整体缩放保持比较。所以新的计算仅需 $q,L\ge4$；这保证此次出现的 $Z_2,\ldots,Z_5$ 和全部旧低范数都处于合法内部，无强制根端点被遗漏。

## 2. 全部约化分量与共同物理源

置换对称给真实正交分解
$$K_1=V_{\rm short}\oplus V_{\rm pool}\oplus K_{\rm fix},\qquad\dim K_{\rm fix}=2.$$
两组内标准子空间和完整三维群固定空间同时约化 $F_j$ 及其逆；压缩到 $K_1$ 后，上式三个子空间同时约化 $\Gamma_j$。固定二维部分始终先在三维群固定空间中取完整逆，再压缩到 $K_{\rm fix}$，不声称该二维空间约化 $F_j$。在两个组内标准部分，$F_j$ 的标量分别为
$$e_j(z^{[q-2]},1^{[L]},w),\qquad e_j(z^{[q]},1^{[L-2]},w).$$
这是组内对角元减非对角元的直接删位身份；Newton 不等式给它们的倒数严格 log 凸。因此全部合法相邻边已在这些分量上严格成立，零维部分删除。

固定二维部分使用 [完整真空归约](R239-appendix-birth-one-two-group-singleton-vacuum-reduction.md) 的同一首一源 $(\alpha,\beta)$。其物理振幅分别为：异常位 $q!z^{q/2}\alpha$、每短位 $(q-1)!z^{(q-1)/2}\sqrt w\,\beta$、每池位 $-q!z^{q/2}\sqrt w(\alpha+\beta)/L$。真实源 Gram 是
$$H_0=(q!)^2z^q\begin{pmatrix}1+w/L&w/L\\w/L&w/L+w/(qz)\end{pmatrix}.$$
这同一个源对所有高度适用。

令
$$Z_j=[x^j](1+zx)^q(1+x)^L,\qquad
P_j=[x^j](1+zx)^{q-1}(1+x)^{L-1},$$
$$D_i=P_i^2-P_{i-1}P_{i+1},\quad P_{-1}=0,\quad D_0=1.$$
写 $v_j=\Theta^2\log Z_j$、$\Theta=z\partial_z$，两类位协方差的直接删位展开给
$$Z_j^2v_j=qLzD_{j-1}.$$
$D_i>0$ 来自严格 Newton。除去共同正数 $(q!)^2z^q$，再作对全部高度相同的源合同 $\beta=\sqrt{qLz}\,\beta_{\rm new}$，高、低首一范数准确成为
$$a_j=1/Z_j,\qquad b_{j-1}=Z_j/D_{j-1}.\tag{2.1}$$
完整二维形式仍为
$$H_j=(a_j+wa_{j+1})|\alpha|^2+
\frac{wb_{j-1}b_j}{b_{j-1}+wb_j}|\beta_{\rm new}+\delta_j\alpha/\sqrt{qLz}|^2,$$
其中 $\delta_j=\Theta\log Z_{j+1}-\Theta\log Z_j$。这些来自完整 MP；共同源合同不改变相邻比较。

## 3. 第三边的完整行列式

局部记号取
$$e=Z_2,\ f=Z_3,\ g=Z_4,\ \ell=Z_5,\qquad E=D_1,\ F=D_2,\ G=D_3,\ H=D_4,$$
$$a=1/e,\ b=1/f,\ c=1/g,\ d=1/\ell,\qquad
p=e/E,\ Q=f/F,\ r=g/G,\ s=\ell/H.$$
普通组重数 $q$ 与局部低范数 $Q$ 不同。实际 Pearson 恒等式给
$$X=(eF-gE)/3,\qquad Y=(fG-\ell F)/4,\qquad\chi=qLz(z-1)^2,$$
$$x=-\frac{\sqrt\chi X}{efg},\qquad y=\frac{\sqrt\chi Y}{fg\ell}\quad(z\ge1).\tag{3.1}$$
这里 $x=(\delta_3-\delta_2)/\sqrt{qLz}$、$y=(\delta_3-\delta_4)/\sqrt{qLz}$；共同消去中心后两个外侧形式写成 $A_-|\alpha|^2+B_-|\beta_{\rm new}-x\alpha|^2$ 与 $A_+|\alpha|^2+B_+|\beta_{\rm new}-y\alpha|^2$。$z=1$ 两项均为零。

设 $A_-=a+wb,A_0=b+wc,A_+=c+wd$ 和
$$B_-=\frac{wpQ}{p+wQ},\quad B_0=\frac{wQr}{Q+wr},\quad B_+=\frac{wrs}{r+ws}.$$
在中心剪切为零的同源坐标中，$K=H_2-H_3H_4^{-1}H_3$ 有
$$K_{11}=A_--A_0^2/A_++B_-x^2>0.$$
严格性来自高范数的严格 log 凸以及同正系数和的 Cauchy–Schwarz。令
$$\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),$$
$$\Phi=pQ(Qs-r^2)+wQr(ps-Qr)+w^2rs(pr-Q^2).$$
全部逆费用保留后的真实四次分子是
$$\mathcal P=\det K\,(p+wQ)(Q+wr)^2(c+wd)s/w,$$
$$\begin{aligned}
\mathcal P={}&Q\Lambda\Phi-wpQ^3r(c+wd)(r+ws)x^2\\
&-wQ^2r^2s(a+wb)(p+wQ)y^2
-2wpQ^2rs(b+wc)(Q+wr)xy\\
&-w^2pQ^3r^2s x^2y^2.
\end{aligned}\tag{3.2}$$
所有清除因子为正。首末系数为
$$\mathcal P_0=pQ^2(ac-b^2)(Qs-r^2)>0,\qquad
\mathcal P_4=Qrs(bd-c^2)(pr-Q^2)>0.$$
低范数的严格比较由 [两权全高度定理](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md) 支付。

将 (3.1) 代入，三个中间系数准确为 $\mathcal P_i=N_i/\mathcal D_i$，其中
$$\mathcal D_1=\mathcal D_3=EF^3G^2Heg\ell,\qquad
\mathcal D_2=EF^3G^2Hefg^2\ell>0.\tag{3.3}$$
$N_1,N_2,N_3$ 依次有 $11,19,11$ 个通用单项式。外侧两项可完整写成
$$\begin{aligned}
N_1={}&(f^2-eg)g\ell(FGe\ell-EHfg)
+(fg-e\ell)ef(G^2f\ell-FHg^2)\\
&+\chi(2GXYe\ell-FY^2eg-HX^2f\ell),\end{aligned}\tag{3.4}$$
$$\begin{aligned}
N_3={}&(fg-e\ell)g\ell(F^2eg-EGf^2)
+(g^2-f\ell)ef(FGe\ell-EHfg)\\
&+\chi(2FXYe\ell-EY^2eg-GX^2f\ell).\end{aligned}\tag{3.5}$$
中间项可直接按 (3.2) 取 $w^2$ 系数；独立脚本重新生成它而不读取表。其全域正性也已由 [规范中间系数定理](R239-appendix-birth-one-normalized-middle-quartic-positivity.md) 独立证明；下面的完整整数证书另行验证本边三项。

## 4. 一次覆盖全部重数的精确整数证书

置 $q=4+x,L=4+y,z=1+u$，$x,y,u\ge0$。对 $0\le j\le5$ 准确生成
$$Z_j=\sum_{r=0}^j\binom{4+x}{r}\binom{4+y}{j-r}(1+u)^r,\qquad
P_j=\sum_{r=0}^j\binom{3+x}{r}\binom{3+y}{j-r}(1+u)^r.$$
每个二项式按有限下降积定义。特别，$\binom{3+x}{5}$ 的个别普通幂系数可为负；证明完全不假设每个原始二项式的系数非负，只对最后的整个 $N_i$ 收集并检验。

先验总次数界为
$$\deg(e,f,g,\ell)\le(4,6,8,10),\qquad
\deg(E,F,G,H)\le(4,8,12,16),$$
$$\deg X\le12,\quad\deg Y\le18,\quad\deg\chi\le5.$$
由通用单项式逐个相加，得到 $\deg N_1\le64,\deg N_2\le76,\deg N_3\le60$。精确展开的是完整有限多项式；没有抽样，没有只取部分 $z$ 次数，也没有从有限整数重数外推。

下表中的公共正整数把全部系数一次变为整数：

| 分子 | 公共分母倍数 | 严格正整数项数 | 负项数 | 总次数 | 最小系数 | 常数项 |
|---|---:|---:|---:|---:|---:|---:|
| $N_1$ | 1,031,956,070,400 | 12,528 | 0 | 64 | 7 | 255,855,511,794,806,371,123,200,000 |
| $N_2$ | 12,383,472,844,800 | 20,539 | 0 | 76 | 3 | 13,539,873,684,181,153,159,839,744,000,000 |
| $N_3$ | 85,996,339,200 | 10,415 | 0 | 60 | 7 | 12,792,775,589,740,318,556,160,000 |

所有常数项严格正，因此对每个 $x,y,u\ge0$ 都有 $N_i>0$。独立证书以 QQ 多项式环精确计算所有乘积，逐项断言整数性和严格正性，并核项数、次数、最小值和常数项；同一完整展开已全部运行通过。证书开头另外核清分母身份、$11/19/11$ 单项式数量、(3.4)–(3.5)，并在实际有理模型 $q=L=4,z=4,w=3/2$ 中先取完整 $3\times3$ 逆，验证同源缩放后的行列式恰为 (3.2)。后者只校准身份，不承担普遍正性的证明。

## 5. 拼回所有正权与倒数边

五个系数全严格正，故对任意 $w>0$ 有 $\det K>0$；与 $K_{11}>0$ 合起来给完整固定二维块的严格比较。§2 的两个标准分量亦严格，正交直和给整个 $K_1$。

若 $z<1$，交换普通两组并以原短组权归一，参数变为 $(L,q,z^{-1},w/z)$。物理置换及统一权缩放保持相邻不等式，故覆盖所有 $z>0$。小组大小不超过三的分支在 §1 已付。

最后用 [真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md) 的同源合同反射高度 $j\mapsto h-j$。将第三边用于倒数权模型，再用正定矩阵等价式
$$AB^{-1}A\prec C\iff AC^{-1}A\prec B$$
即得末第三边。没有逐层任意变换源，也没有改变完整逆的取法。定理 1 完成。

## 6. 全高度普通权比扇区的扩大

已有 [全高度有界普通权比证明](R239-appendix-birth-one-bounded-ordinary-contrast-all-heights.md) 证明：在每个内部 $n,m=h-n\ge3$，规范 $P_1>0$ 在 $\delta\le0$ 或 $B\ge0$ 成立；反射给 $P_3$，且 $P_2$ 已全域严格正。其实际参数满足
$$\eta<\lambda/4,\quad u\eta<\lambda/4,\quad
\lambda=(z-1)^2/z,$$
而 $B\ge0$ 的充分条件为
$$\eta\le\frac{m(h+2)}{(n+1)(m+2)}.$$
本定理将任意权比的已付首末范围扩到三边，所以只剩 $n,m\ge4$。在这一范围
$$\frac{m(h+2)}{(n+1)(m+2)}>\frac m{m+2}\ge\frac23,$$
反射式同理。故以下完整全高度结论成立：
$$\boxed{\lambda\le\frac83\quad\Longleftrightarrow\quad
\max\{a^2/b^2,b^2/a^2\}\le\frac{7+2\sqrt{10}}3.}\tag{6.1}$$
异常权 $c>0$ 完全任意，两组重数完全任意，整个 $K_1$ 的每个合法相邻边严格成立。

对固定 $h\ge8$，函数 $m/((h-m+1)(m+2))$ 在 $4\le m\le h-4$ 严格递增，所以最小值在 $m=4$；得到更宽的固定高度条件
$$\boxed{\lambda\le\frac{8(h+2)}{3(h-3)}.}\tag{6.2}$$
$h\le7$ 的所有内部边已由首三与末三边覆盖，无须任何普通权比条件。这里只扩大实际有限模型的已证扇区；未付的大权比、更内部相邻边继续保留为开放项。
