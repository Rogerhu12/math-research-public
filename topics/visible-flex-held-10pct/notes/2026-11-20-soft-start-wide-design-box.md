# R55 的较宽设计盒：r≤1.1 与完整 D≤2.69 的余量

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。

本条保留 R55 的全部参考段表、δref=.06 和原 ShortBridge curvature4。只增加较宽参数盒的**新几何预算**，不把实际线性校准根叫作非圆 BVP 解，也不改变当前旧 λ=.02 场的物理度量。

## 1. 新首周期包络

取

$$
\boxed{\frac{21}{20}\le r\le\frac{11}{10},
\qquad .063\le\delta=.06r\le.066.} \tag{1}
$$

R55 的 n3 轨道弦长和单位经向速度仍给

$$
|X|^2\le K_3^2a_r(s)^2+s^2
<\frac{1936}{1323}a_r(s)^2+s^2.
$$

因首周期的 a_ref≥1，这个右侧对 r 非减。新证书在 **r=11/10**、半径预算 **67/50=1.34** 下重新构造有限多项式，并作50个新 Bernstein 标量盒。最小平方余量为

$$
\boxed{
\left(\frac{67}{50}\right)^2
-\frac{1936}{1323}a_r(s)^2-s^2
\ge
\frac{1012957182905894923}{26859028140000000000}>0.}
\tag{2}
$$

因此新盒的整个首个升降周期、所有材料角均满足 |X|<1.34，其上下反射组件直径<2.68。旧 R55 的 r≤1.05/半径1.32证书未被改写，也没有把旧50盒的结论外推到新端点。

(2)余量约.03771，故若采用 R55 §6 说明的全段 relative metric≤10⁻⁶ 条件版本，乘1+10⁻⁶仍有严格余量。它仍然只覆盖首周期，不包括后续 bridge、tail、帽或额外周期。

## 2. 准确保护圆片及 profile 本身

R55 的损耗下界对 r递增，所以 χ(rL*)>.5 在(1)继续成立。准确圆片经向曲率满足

$$
K_m\le\frac{375}{2r\sqrt{231}}
\le\frac{1250}{7\sqrt{231}}
<\frac{123}{10}=12.3.
\tag{3}
$$

平方比较的精确正余量是

$$
(123/10)^2(21/20)^2(231/10000)-(15/8)^2
=\frac{134956359}{400000000}>0.
$$

原参考旋转背景曲率<8的论证继续适用。R55 的首段支撑估计将 r上限换为11/10后仍严格大于.32；只用√231>15即可验证。以上仍不替代未知补弧及 bridge 的真实曲率、支撑。

## 3. 完整闭面可以使用的预算

假设真正的新完整闭面在插柱之前（包括真实帽）满足

$$
D_0\le\frac{67}{25}=2.68,\qquad
X\cdot n\ge\frac{87}{1000}=.087,\qquad
|\kappa_i|\le\frac{123}{10}=12.3
\tag{4}
$$

并已支付 R54 的全 Cartesian 接缝、对称与标记条件。对完整柱长 $0<\ell\le1/100$，R54 给

$$
D\le\frac{269}{100}=2.69,\qquad
X_{\rm new}\cdot n_{\rm new}\ge\frac{41}{500}=.082
>\frac{10}{123}.
$$

支撑到焦距的差为43/61500>0，故 R1 的闭球面引理给

$$
\operatorname{reach}\ge\frac{10}{123},\qquad
\boxed{\frac{\operatorname{reach}}D
\ge\frac{1000}{33087}
=.03022335056\ldots>.03.} \tag{5}
$$

R54 的原 H 宽度.54、原相位.45与原 k=.2均不改变。其严格水平弦下界和完整像下界给

$$
\boxed{\frac{\operatorname{diam}F_0(H)}D
>\frac{13493439}{67250000}
=.2006459330\ldots>.2,} \tag{6}
$$

$$
\boxed{\frac{\delta_{\rm hold}}D>
\begin{cases}
1653761667/15064000000=.1097823730\ldots,&n=3,\\
2770344693/21300496000=.1300601024\ldots,&n=4.
\end{cases}} \tag{7}
$$

四重一行只转换 R54 的条件完整像常数；本条首周期包络的数值证书针对 m3 段表。没有将它当作现有 n4 profile 的实际认证。

这里选择 D≤2.69也保留了 H 的径门。若保持原 H不变而只把 D放至2.71，已有弦下界就不足以证明 Hdiam≥.2D，不能只检查 held 和 reach 两项。

## 4. 新证书及实际执行范围

源码：

    scripts/resume_m3/certify_soft_start_geometry_wide.mjs

命令：

    node topics/visible-flex-held-10pct/scripts/resume_m3/certify_soft_start_geometry_wide.mjs

新 r=1.1 的50个标量盒及本条全部有理比例比较已在 JavaScript 执行器中用 BigInt 实际执行通过。它没有调用 BVP或场审计，没有重跑 R55 的旧 r=1.05盒。输出均为精确分数；小数仅用于展示。

## 5. 当前 q060 尾不能直接继承 R21 背景

本次实际比较了 R21 的冻结 physical_background.json 与 q060 bootstrap port。前者 valleyControlsHead[0]=3.125，后者 valleyControls[0]=4.625；这是物理背景差异，并非数组表示精度。

- R21 背景参数 SHA256：676ed1247742d1a263f2c63e29bae839fd1b11a55fca7f578eb808050be298fa。
- q060 bootstrap port SHA256：aa482f3bbd9506b90e307df72a7890f02f933338a4b3dec230f90b10765b09a5。

因此另份 tail closure budget 中 h(R)<.029、w≤.41、背景曲率≤8，只是**选择同R21物理背景时的条件预算**，不能写成当前4.625背景已经证明。这项差异也不能靠只看相同 R=.3、wCut=.08 或 curvatureBound=8消除。

若新背景独立支付那些界，tail窗口的实际曲率上界120000/9801严格小于12.3（差5523/98010>0），与(4)兼容；若没有，则须使用新背景自己的真实积分、坡度与曲率预算。首周期证书和(4)的其余真实全曲面条件也仍须分别支付。

