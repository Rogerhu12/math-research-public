# R162：小 Hecke 整基、CM 点关系的清挠与完整双变量搬运

日期：2026-11-12；负责：root。**状态：已证明，109 个准确坐标及群阶证书已完成。** 本文把 R144/R148 的实际 CM 校准点和全部平移写成次数不超过 91 的真实 Hecke 算子作用于 B−4 的形式，并用明确的 47 进单位倍数消除未知有理挠点。随后给出保留所有主函数的搬运公式。

这没有把这些主函数的存在等同于已计算它们，也没有宣称该路线必定比额外两条 CM Miller 链更快。实际非形式范数和各个框架转换仍须计算。

## 1. 实际 Hecke 整基

固定
$$X=X_{\rm ns}^+(41),\quad J=\operatorname{Jac}(X),\quad B=B_{-4}.$$
R89/R94 的八个 Hecke 域次数为
$$2,3,3,4,4,8,12,18,$$
总和为 54。在各域使用 H=T2+2T3 的升幂基，按这八域次序排列坐标。R133 的迹 Gram 矩阵在 47 处行列式为单位，所以这些幂基给出一个秩 54 的有限 étale Z47 代数的整基。R140 又把这个代数准确识别为 Z47[T3]。

取 R94 已给出的 54 个真实算子 T_n，指标集合为
$$
\begin{split}
\mathcal I=\{&1,2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30,31,\\
&33,34,35,37,38,39,42,46,47,51,53,55,57,58,59,61,62,65,66,67,\\
&69,70,71,73,74,77,78,79,83,85,86,87,89,91\}.
\end{split}
\tag{162.1}
$$
所有 n 与 41 互素；T1 是恒等。以 T_n 为行、上述幂基为列的矩阵记为 C。准确计算给
$$\boxed{\det C\equiv1\pmod{47}.}\tag{162.2}$$
证书保存 C 及其逆模 47^4，并逐项核对双侧乘积为单位矩阵。每个源系数的分母均为 47 单位。因此这 54 个算子本身构成同一个整代数的基，不必用 T3 的高次复合对应来表达目标算子。

这是实际算子等式：R94 已识别它们在 X 上的真实 Hecke 对应；特征零阿贝尔簇的 endomorphism 若在全部微分上为零，就自身为零。因此八域中的完整坐标等式也给 J 上的 endomorphism 等式。此处没有仅使用一个有限域近似特征值。

## 2. 16 消去全部有理挠点

J 与 R57/R74/R89 识别的水平 41² 新 Fricke 正部有理同源，所以其好约化及 Frobenius 多项式与该模块相同。特别在 q=3,5 有好约化。由实际全部八个特征形式，
$$\#J(\mathbb F_q)=\prod_f N_{K_f/\mathbb Q}(q+1-a_q(f)).\tag{162.3}$$
逐域范数准确如下。

| 域次数 | q=3 的范数 | q=5 的范数 |
|---:|---:|---:|
| 2 | 8 | 64 |
| 3 | 46 | 260 |
| 3 | 43 | 281 |
| 4 | 79 | 1249 |
| 4 | 431 | 1249 |
| 8 | 40321 | 2595321 |
| 12 | 10198217 | 1029108591 |
| 18 | 44618190919 | 11419324541353 |

每项由清分母后的整数乘法矩阵、Bareiss 行列式准确计算，再用有理多项式 resultant 独立核对；两种算法全部相同。乘积为
$$\#J(\mathbb F_3)=9885260908361518487967568463408,$$
$$\#J(\mathbb F_5)=222472952808095853509278542118929794430720.$$
它们的最大公因数准确为 16。

在 Z_q 上的好约化模型，q≥3 时形式核的参数位于 qZ_q，形式对数及指数互逆；该核无挠。于是 J(Q) 的全部挠点在这两个剩余群中都单射，包含 q 主部分也不遗漏。Lagrange 定理遂给
$$\boxed{\#J(\mathbb Q)_{\rm tors}\mid16,\qquad
16J(\mathbb Q)_{\rm tors}=0.}\tag{162.4}$$
这里没有宣称有理挠点群的阶恰为 16，也没有从有限域群阶求其完整结构。所得消去因子已是 47 单位，足够用于后续真实点关系。

## 3. 全部 CM 校准点和平移的准确坐标

记 b=P−3、u=P−12、c=P−7，Uδ=[20Pδ−D]。沿用 R89 的实际带符号坐标
$$U_{-3}=r_3B,\quad U_{-7}=r_7B
\quad\text{于 }J(\mathbb Q)\otimes\mathbb Q.$$
R144 的真实二同源关系给 r12=T2 r3/3。于是
$$x_u=[u-b]=\frac{r_{12}-r_3}{20}B,\qquad
x_c=[c-b]=\frac{r_7-r_3}{20}B.\tag{162.5}$$

对 R94 全部 53 个方向
$$F_n=a_nT_n+c_n,\qquad G_n=2F_n,$$
其中 η_(D,Gn)=ξ_nB。由 R148 的**准确**点关系
$$\eta_{D,F_n}=20\kappa_n+2F_nU_b$$
可在有理向量空间写成
$$\kappa_n=rac{\xi_n/2-2F_nr_3}{20}B.\tag{162.6}$$
这一步的 1/2 来自 G=2F，不是函数范数的微分因子。实际第二变量为
$$D_{u,n}=F_nx_u-\kappa_n,\qquad
D_{c,2}=F_2x_c-\kappa_2.\tag{162.7}$$

生成器对 (162.5)、全部 (162.6) 及 (162.7) 共
$$2+53+53+1=109$$
个元素作完整有理数运算，并求解同一个矩阵 C。验证在八个数域的所有坐标上均为**准确相等**。所有 109 组 T_n 坐标分母的最小公倍数为
$$\boxed{d_0=79079601958670508000,\qquad47\nmid d_0.}\tag{162.8}$$
作为三个直接入口，x_u、x_c、κ2 各自约分后的公共分母为
$$79079601958670508000,\quad7907960195867050800,\quad39539800979335254000.$$
完整 54 项分子数组均保存在证书，不省略为近似小数。

对任一上述真实点 C，记其证书中的算子为 R_C∈End(J)⊗Q；即 C=R_CB 在 J(Q)⊗Q。令
$$\boxed{e=16d_0=1265273631338728128000,\qquad H_C=eR_C.}\tag{162.9}$$
由于 d0 清掉全部分母，H_C 是 (162.1) 中真实整对应的整数线性组合。d0 C−d0 R_CB 是 J(Q) 的挠点；乘以 (162.4) 的 16 后，得到
$$\boxed{eC=H_CB\quad\text{于实际 }J(\mathbb Q).}\tag{162.10}$$
且 e≡24 mod47。这样才消去了此前有理坐标等式中可能残留的挠点，而不是直接将它略去。

给定 C 的实际度零除子代表和 B 的实际代表 A，(162.10) 保证存在实际主函数 h_C，使
$$\operatorname{div}h_C=eC-H_CA.\tag{162.11}$$
因 X 有有理点 b，Picard 类为零的有理除子可以用 Q 上的有理函数平凡化；亦可在 Q47 上使用同一结论。具体计算仍必须构造 h_C 并验证 (162.11)。在 Makdisi 模型中，这意味着保留群运算中的主截面，再作完整零类/理想等式检验；仅比较 Lie 坐标不能生成 h_C。

## 4. 保留主函数的两变量搬运公式

以下给通用公式，也固定符号。设 C,D 是 R148 的两个实际度零除子，R_C、R_D 取上述已证坐标；选
$$\operatorname{div}h_C=eC-H_CA,\qquad
\operatorname{div}h_D=eD-H_DA.\tag{162.12}$$
先在相关代表支撑适当不交时，以 ε(C,D) 表示 R154 的规范有理范数元。写目标纤维元素为
$$z=u_0\,\epsilon(C,D).$$
局部 Poincaré 对数采用 R140/R141 同一个 Hecke 相容规范。则
$$\boxed{
\begin{aligned}
e^2\lambda(z)={}&e^2\log u_0+e\log h_C(D)
+\log h_D(H_CA)\\
&+\lambda\bigl(\epsilon(A,H_CH_DA)\bigr).
\end{aligned}}\tag{162.13}
$$

**证明。** 双扩张两条加法律把 z 的 e² 次幂送到 (eC,eD) 纤维，规范框架变成 ε(eC,eD)。按 R154 的主除子规范，先将 eC=H_CA+div(h_C) 改成 H_CA，得到标量
$$h_C(eD)=h_C(D)^e.$$
再将第二变量 eD=H_DA+div(h_D) 改成 H_DA，得到标量 h_D(H_CA)。最后使用真实自伴随 Hecke 对应 H_C 的范数投影公式，
$$\mathcal P_{H_CB,H_DB}\simeq\mathcal P_{B,H_CH_DB}.$$
在这里明确使用未经任意压缩的实际对应除子，规范有理范数元相互对应，不另出现一个人为自由标量。取同一个相容对数即得 (162.13)。证毕。

若将 H_CA 或 H_DA 改用较小的等价除子，必须把该次主函数范数继续乘入；它们不会因 Hecke 相容性消失。H_C 的非形式搬运不能用 R141 的混合 Hessian 代替。

同样，R148 的 eN 是含碰撞的切向范数框架。要把其坐标 3987767 或 4622835 作为 u0 使用，必须先按真实移动函数完成到 ε(C,D) 的转换，或直接在同一切向 Deligne 符号中实施 (162.13)。不能在 C、D 支撑相交时写未定义的普通点值 h_C(D)。R159 只在保留准确端点因子后允许提取单位部。

## 5. 与唯一一条完整 B 链的连接

令 m=#J(F47)，R121 已实际完成对应点乘，R151 正保留完整主函数。取 R154 的同一终点规范
$$\operatorname{div}f=mA-A_Y,\qquad Y=mB,$$
其中 A_Y 为 R136/R145 的第一套实际 Abel 代表。令
$$T=H_CH_D$$
为**指定实际对应的复合**。函数范数 N_T f 满足
$$\operatorname{div}(N_Tf)=mTA-TA_Y.$$
把 R154 用于 A、TA，即得
$$\boxed{
\begin{aligned}
m^2\lambda\bigl(\epsilon(A,TA)\bigr)
={}&\lambda\bigl(\epsilon(A_Y,TA_Y)\bigr)\\
&+m\log f(TA)+\log(N_Tf)(A_Y).
\end{aligned}}\tag{162.14}
$$
因此 (162.13)、(162.14) 给出一条 mB 主函数链的完整复用公式。还保留以下实际输入：h_C、h_D、T 的范数，以及形式终点的真实框架变换。本文没有把这些计算当作已经完成。

若选第二套 Abel 代表 A2(TY)，并实际构造
$$\operatorname{div}k_T=TA_Y-A_2(TY),$$
则同一主除子符号给
$$\lambda\bigl(\epsilon(A_Y,TA_Y)\bigr)
=\log k_T(A_Y)+\Lambda\bigl(\sigma(Y,TY)\bigr).\tag{162.15}$$
R140 的全尾界在 Y,TY∈47J 上给
$$\Lambda\bigl(\sigma(Y,TY)\bigr)
\equiv B(\log Y,T\log Y)+\frac12\log\delta(Y,TY)
\pmod{47^4}.\tag{162.16}$$
这里 B 为 R141 的实际修正矩阵，δ 必须来自**同一个**双 Abel 框架。R145 的 4263370 是 Y,Y 这一指定输入的值；不能未经计算把它用于 Y,TY。k_T(A_Y) 也必须由实际主函数求得。

本题 m≡9 mod47，e≡24 mod47，所以
$$e^2m^2\equiv32\pmod{47},\qquad(32)^{-1}\equiv25\pmod{47}.$$
因此上述清挠、清分母和最后两变量倍乘的除法都不损失 47 进精度。支撑相交造成的精度问题仍按 R159 的整因子算法处理。

## 6. 执行范围及文件

小 Hecke 基降低了对应指标：无需自动展开 T3^53。它没有使 54 项稠密整数线性组合变成一次免费群运算。构造真实 T_nB、整数多点和、h_C/h_D 的成本应与直接从两个实际 CM 初始点运行 Miller 链比较；任一路线均须保留全部主函数与框架。

- [完整有理数生成器](../scripts/p41_small_hecke_cm_transport47.py)。
- [109 组坐标、整基双侧逆及两处群阶证书](../scripts/data/p41_small_hecke_cm_transport47_certificate.json.gz)。

证书 92253 字节，SHA256：b7df8021b574598e10f6aac3578f9d63e162374359184742781d40b73f8cd2e5。
源码 SHA256：3675d464c063dc2952cc2176a998d1e59d837e76b067b8f4a4f4d01e8bff290f。

从仓库根复算：
~~~bash
python -B topics/serre-uniformity/scripts/p41_small_hecke_cm_transport47.py
~~~

证明输入是已经识别的实际对象：[R89](R89-signed-CM-coordinates-and-actual-T2-translation.md) 的带符号 CM 坐标；[R94](R94-central-involution-and-complete-Chow-Heegner-operator.md) 的全部对应和平移；[R144](R144-cm-height-difference-calibration-without-section-constants.md) 的校准点；[R148](R148-global-correspondence-section-with-diagonal-and-basepoint.md) 的准确 κ；[R154](R154-double-miller-transport-and-hecke-reuse.md) 的范数与主除子符号；[R159](R159-integral-weierstrass-cancellation-and-exact-jet-precision.md) 的整盘消去。

本结果关闭“只在 J(Q)⊗Q 相等却未处理挠点”的接口，给完整有限数据和真实范数公式。它不关闭剩余主函数、完整辅助高度或全部 QC 共同根问题。
