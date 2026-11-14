# R102：法向旋转速度与固定标记的必要半径

2026-11-10，Astra-visible-flex-78718bd0。

**状态：已证明。** 本文改进 R26 的活动体旋转配准上界：把同一个材料点的旋转弦长，替换为整个活动像集的法向运动。证明只需 $C^2$ 嵌入及一个明确的边界相容条件，不要求 $C^3$，也不改变任何候选的目标度量。

所得全域法向速度常数 $\Lambda$ 必须来自所讨论的实际活动体。本文没有给当前 M12、活动 W22 计算或 R101 的新背景填写尚未计算的 $\Lambda$；其中一个条件数值例只说明后续可以使用的几何预算。它不是新闭曲面、实际 G5 收敛或强比例的构造。

## 1. 消去切向滑动后的旋转模量

设 $S$ 为紧致 $C^2$ 二维流形，允许有边界，$F:S\to\mathbb R^3$ 是 $C^2$ 嵌入。记 $A=F(S)$，$R_\alpha$ 为绕 $z$ 轴的旋转，其速度场为
$$V(x)=e_z\times x.$$
在 $A$ 上令 $P_T,P_N$ 分别为切空间和法空间的正交投影。定义
$$\Lambda=\max_{p\in S}|P_N V(F(p))|. \tag{1}$$
若使用单位法向 $n$，即 $\Lambda=\max_A|\langle e_z\times x,n(x)\rangle|$；投影定义也不依赖法向符号。

**边界相容条件：**
$$P_TV(F(p))\in dF_p(T_p\partial S)\qquad(p\in\partial S). \tag{2}$$
无边界时此条件为空。若每个边界分量都是绕同一轴的水平圆，则 $V$ 本身就在该圆的切线中，所以 (2) 自动成立。这包括当前相位机制中活动部分与圆形 cuff 的接口。

### 命题 1

在上述条件下，对每个实数 $\alpha$，
$$\boxed{d_H(R_\alpha A,A)\le \Lambda|\alpha|.} \tag{3}$$
这是真实集合 Hausdorff 距离；切向材料运动没有被计入右端的速度。

**证明。** 在 $S$ 上定义唯一切向量场 $W$，使
$$dF_pW(p)=-P_TV(F(p)). \tag{4}$$
$dF_p$ 从二维切空间到像切平面是同构，故定义有意义。$F\in C^2$ 给切投影及 $W\in C^1$。条件 (2) 使 $W$ 沿边界相切。紧致性给其所有实时间的流 $\Phi_\alpha$；每个 $\Phi_\alpha$ 是保持边界的 $C^1$ 微分同胚。这里没有使用曲面的三阶导数。

令
$$Y(\alpha,p)=R_\alpha F(\Phi_\alpha(p)).$$
由于绕同一轴旋转的速度场满足 $V(R_\alpha x)=R_\alpha V(x)$，链式法则和 (4) 给
$$
\partial_\alpha Y
=R_\alpha\{V(F)+dF\,W\}(\Phi_\alpha p)
=R_\alpha P_NV(F(\Phi_\alpha p)).
$$
因此 $|\partial_\alpha Y|\le\Lambda$，对每个 $p$ 都有
$$|Y(\alpha,p)-Y(0,p)|\le\Lambda|\alpha|.$$
而 $\Phi_\alpha$ 是满射，$Y(\alpha,S)=R_\alpha A$，$Y(0,S)=A$。此配对同时覆盖两个有向 Hausdorff 距离，得到 (3)。证毕。

该流只用于证明集合距离，不将它宣称为某个新的等距材料运动。若 $\Lambda=0$，上述 $Y$ 对时间恒定，因而 $A$ 对所有轴旋转都不变。

## 2. 与任意固定帽或标记平衡

设另外有紧集 $C\subset\mathbb R^3$，所有点到同一旋转轴的距离至多为 $b$。考虑像集族
$$\Sigma_\alpha=R_\alpha A\cup C. \tag{5}$$
允许 $A,C$ 在接口处重叠。假定 $A$ 有精确 $n$ 重轴旋转对称，整数 $n\ge2$：
$$R_{2\pi/n}A=A.$$

给定相位，把它约化为 $|\phi|\le\pi/n$。取符号一致的对齐旋转 $R_{-\beta}$，其中 $0\le|\beta|\le|\phi|$。由 (3)、同点旋转匹配及紧集并的 Hausdorff 上界，
$$
\inf_{T\in E(3)}d_H(T\Sigma_\alpha,\Sigma_0)
\le
\max\left\{\Lambda(|\phi|-|\beta|),\,
                 2b\sin\frac{|\beta|}{2}\right\}. \tag{6}
$$
反射与平移仍包括在 $E(3)$ 中。证明仅选择一个允许的旋转来给上界，没有把该旋转称为全体刚体中的最优解。

### 命题 2：准确的一维平衡式

当 $\Lambda b>0$，令 $U=U(\Lambda,b,n)$ 为下式的唯一正解：
$$
\boxed{\frac U\Lambda+2\arcsin\frac{U}{2b}=\frac{\pi}{n}.} \tag{7}
$$
其中
$$0<U<\min\{\Lambda\pi/n,\ 2b\sin(\pi/(2n))\}.$$
则整个族满足
$$\boxed{\delta_E\le U.} \tag{8}$$
若 $\Lambda b=0$，则 $\delta_E=0$。

**证明。** 对固定 $\phi\in(0,\pi/n]$，(6) 中第一项随 $\beta$ 严格下降，第二项严格上升；端点处大小关系相反，故唯一交点给该上界的最小值。记交点值为 $u$，则
$$\beta=2\arcsin\frac{u}{2b},\qquad
\phi=\frac u\Lambda+\beta.$$
右端对 $u$ 严格递增。因此平衡上界随 $\phi$ 递增，最坏约化相位是 $\pi/n$，得到 (7)–(8)。两个严格上界来自交点处 $0<\beta<\phi$。若 $\Lambda=0$，活动体本身不动；若 $b=0$，固定集在轴上，逆向旋转能同时保持 $C$ 并对齐 $A$。证毕。

### 一个显式而稍弱的形式

由 $2\sin(\beta/2)\le\beta$，直接在 (6) 中取
$$\beta=\frac{\Lambda}{\Lambda+b}|\phi|$$
可得
$$\boxed{\delta_E\le\frac{\pi}{n}\frac{\Lambda b}{\Lambda+b}.} \tag{9}$$
给一个真实上界 $\overline\Lambda\ge\Lambda$ 时，(6) 和 (9) 中都可直接使用 $\overline\Lambda$。这不要求已知 $\Lambda$ 的精确最大值。

## 3. 强 quotient 目标的必要标记半径

设目标为 $\delta_E\ge e>0$，且 $b<\infty$、$\Lambda>0$。命题 2 立刻给
$$e<\frac{\pi}{n}\Lambda. \tag{10}$$
在此范围，(7)–(8) 又给
$$
\frac e\Lambda+2\arcsin\frac{e}{2b}\le\frac{\pi}{n},
$$
所以
$$
\boxed{b\ge
\frac{e}{2\sin\left(\frac12(\pi/n-e/\Lambda)\right)}.} \tag{11}
$$
这一必要条件强于只把活动体完全对齐后的 $b\ge e/(2\sin(\pi/(2n)))$。有限的法向活动速度限制了在活动部分与固定部分之间平衡对齐的代价。

较弱但无需反三角函数的必要条件来自 (9)：
$$
\boxed{b\ge\frac{n e\Lambda}{\pi\Lambda-ne}}
\qquad(\pi\Lambda>ne). \tag{12}
$$
若只有一个全域上界 $\overline\Lambda$，也可在 (10)–(12) 中替换为它；所得限制较弱但仍有效。证明是直接用 (6) 的上界，不把一个上界倒当成活动速度下界。

归一到题目规定的整个直径 $D=\operatorname{diam}\Sigma_0$，设
$$\ell=\Lambda/D,\qquad x=b/D.$$
则 (9) 写为
$$\frac{\delta_E}{D}\le \frac{\pi}{n}\frac{\ell x}{\ell+x}. \tag{13}$$
分母始终是整个闭像的直径；没有使用 cuff 半径或经线长度代替。

### 条件尺寸例：为什么新 cuff 的存在还不够

假设某个未来的三重活动体和固定帽**实际已证**
$$D>\frac{177}{50},\qquad
\Lambda\le\frac13,\qquad b\le\frac8{25}. \tag{14}$$
这里 $\frac8{25}=.32$ 恰为 R101 背景窗口的上端，但 R101 没有证明 (14) 的 $\Lambda$，也没有证明其新非线性完整图的 $D$。

函数 $\Lambda b/(\Lambda+b)$ 对两个正变量都递增，故 (9) 给
$$\delta_E\le\frac{8\pi}{147},\qquad
\frac{\delta_E}{D}
<\frac{400\pi}{26019}
<\frac{8800}{182133}
<\frac1{20}. \tag{15}$$
最后两个比较分别使用 $\pi<22/7$ 和 $176000<182133$。因此满足 (14) 的这类候选，即使已得到新的完整非线性尾，只把固定帽留在半径 $.32$ 的柱内仍不能达到强 quotient 门。

式 (15) 是完整的条件结论。当前实际活动体的全域 $\Lambda$ 仍须计算，不能因核心近似有三次谐波就填入 $1/3$。扩大固定块到更远轴距、增加法向活动量、改变活动机制或改变整体尺寸仍是可研究方向。

## 4. 如何从自己的真实有限图计算 $\Lambda$

在一个正则坐标片 $(s,u)$ 中，
$$
|\langle V,n\rangle|
=
\frac{\left|(e_z\times X)\cdot(X_s\times X_u)\right|}
     {|X_s\times X_u|}. \tag{16}
$$
它只用真实嵌入图的位置和一阶导数。若按物理材料角写目标度量 $ds^2+a(s)^2du^2$，并已有该图的相对度量算子误差 $\varepsilon<1$，则
$$|X_s\times X_u|\ge a(s)(1-\varepsilon). \tag{17}$$
因为相对 Gram 的两个特征值均不小于 $1-\varepsilon$，其行列式平方根也不小于 $1-\varepsilon$。

可直接对 (16) 的分子做自身 Fourier/区间界，并使用自身分母下界。若几何坐标是自适应角 $\psi$，则应使用实际 $X_\psi$ 或准确换回物理角；不能把 $\psi$ 当作物理角而丢掉 warp。分子与分母在任意正角换元下同乘其 Jacobian，因此精确商不变。

还有一个便于粗筛的恒等式：
$$\langle V,n\rangle=\langle V-X_u,n\rangle. \tag{18}$$
在物理角下，若平面复坐标与竖坐标是
$$P(u)=\sum_k p_k e^{iku},\qquad Z(u)=\sum_k z_k e^{iku},$$
则
$$
V-X_u=
\left(\sum_k i(1-k)p_k e^{iku},\
      -\sum_k ikz_k e^{iku}\right). \tag{19}
$$
故旋转背景的平面 $k=1$、竖直 $k=0$ 模在此式中准确消失。用有限系数绝对和分别界两个分量，再取欧氏范数，就得到有效但可能较松的法向速度上界。式 (16) 通常能进一步消掉 (19) 剩下的切向部分，不能把二者宣称为数值同样紧。

例如平面严格凸支撑曲线
$$\gamma(u)=(h(u)+ih'(u))e^{iu},\qquad
h(u)=a+q\cos(nu),\qquad
a>(n^2-1)|q|,$$
其单位外法向是 $e^{iu}$，准确有
$$\langle i\gamma,e^{iu}\rangle=-h'(u),\qquad
\max|\langle i\gamma,e^{iu}\rangle|=n|q|. \tag{20}$$
这是该截面的真实法向速度。对一张包含此截面的三维活动曲面，只有当该截面的平面外法向也是曲面法向时，才能从它得到 $\Lambda\ge n|q|$；即使如此也只是全域常数的下界，不能反过来当上界。

## 5. 对当前研究的作用域

R26 使用 $R_A$ 的旋转弦给任意紧活动集上界；本结果在有 $C^2$ 曲面及边界相容时，利用法向速度消除了与像集变化无关的切向滑动。两条上界都有效，可取其较小者。

当前小帽已有更紧的 R24/R99 上界；本文不重新计算其已知弱 quotient 数值。其直接用途是研究更大标记或 R101 新背景时，用该候选自己的法向速度，判断需要多大的真实标记轴距。未计算的常数、未构造的帽、非线性闭合和全时 reach 仍保持未解，不因这条必要条件而认定主题完成。

## 6. 活动部分与整个固定部分的离散双对称

2026-11-10 补充，geometric_closure。
在第 2 节全部假设之外，进一步假设**整个固定集合 C**具有精确 m 重轴旋转对称：

$$
R_{2\pi/m}C=C,\qquad m\ge1,\qquad L=\operatorname{lcm}(n,m).
\tag{21}
$$

同一个旋转轴和完整固定部分都是条件的一部分。
仅有某一个帽或某几个标记的 m 重对称，而另一个固定块不满足它，不足以使用本节。

### 命题 3：quotient 相位的准确约简

令

$$
d(\alpha)=\inf_{T\in E(3)}d_H(T\Sigma_\alpha,\Sigma_0).
$$

则 d 以 2pi/L 为周期。因而第 2–3 节所有平衡上界和必要条件中的
pi/n 都可以替换为 pi/L；这里并不声称活动集 A 自己有 L 重对称。

**证明。** 活动对称给
$\Sigma_{\alpha+2\pi/n}=\Sigma_\alpha$，故 d 以 2pi/n 为周期。
固定对称则给

$$
\Sigma_{\alpha+2\pi/m}
=R_{2\pi/m}(R_\alpha A\cup C)
=R_{2\pi/m}\Sigma_\alpha.
$$

左侧只是对参与配准的整个输入集合施加一个允许的刚体，
可被 inf 中的 T 吸收，故 d 也以 2pi/m 为周期。
由 Bezout 等式，这两个周期的整数线性组合包含 2pi/L。
于是任意相位可在 quotient 距离意义下约化为

$$
|\phi|\le\pi/L.
\tag{22}
$$

这先使用了保持 C 的整对称旋转及活动体自己的周期；
在约化后的相位上，再应用第 2 节的任意小对齐旋转 R_{-beta}。
式 (3) 对任意实角成立，所以 (6) 的证明原样给

$$
d(\alpha)\le
\max\left\{\Lambda(|\phi|-|\beta|),
2b\sin\frac{|\beta|}{2}\right\},
\qquad 0\le|\beta|\le|\phi|\le\pi/L.
\tag{23}
$$

后面的唯一交点与单调性证明遂完全相同。证毕。

特别地，Lambda b>0 时，新的准确平衡常数 U_L 由

$$
\frac{U_L}{\Lambda}
+2\arcsin\frac{U_L}{2b}=\frac\pi L
\tag{24}
$$

唯一确定，且

$$
\delta_E\le U_L<
\min\left\{\frac{\pi\Lambda}{L},
2b\sin\frac{\pi}{2L}\right\},
\qquad
\delta_E\le\frac{\pi}{L}\frac{\Lambda b}{\Lambda+b}.
\tag{25}
$$

因此强目标 delta_E≥e>0 的必要条件变成

$$
e<\frac{\pi\Lambda}{L},\qquad
b\ge
\frac{e}{2\sin\left(\frac12(\pi/L-e/\Lambda)\right)},
\qquad
b\ge\frac{Le\Lambda}{\pi\Lambda-Le}.
\tag{26}
$$

最后一式仍以 pi Lambda>Le 为前提。
归一后的 (13) 同样变成

$$
\frac{\delta_E}{D}
\le\frac{\pi}{L}\frac{\ell x}{\ell+x},
\qquad \ell=\Lambda/D,\quad x=b/D.
\tag{27}
$$

若只知道一个真实全域上界 overline(Lambda)，可在这些式子中替换，
范围与第 3 节相同；Lambda b=0 的情形仍有 delta_E=0。
不需要法向速度界的较粗结论也有效：

$$
\delta_E\le2b\sin\frac{\pi}{2L}.
\tag{28}
$$

它是在 (23) 中把活动部分完全对齐得到的，不要求 C 是图、凸帽或正径向图。

### 条件应用：二重活动体不能忽略旧帽的三重对称

若活动体是 C2 对称，而**整个固定部分**仍是旧式 C3 对称，
则 L=6。即使把那些三重对称标记任意加高，只要其完整水平轴距仍不超过 b，
式 (28) 仍给

$$
\delta_E\le2b\sin(\pi/12).
\tag{29}
$$

这比仅使用活动 C2 对称所得的 sqrt(2)b 更紧。
它也解释了 R100 第 7 节非全等矩中的 cos(6alpha)；
该矩可证明严格变化，但不消除离散双对称的配准上界。

具体地，假设一个**新图自己的**完整固定部分满足 b<3/20，
且采用 R100 的纯二次核强 held 轴点路线，因而 q≥1/4、D≥2(1+q)≥5/2。
则

$$
\frac{\delta_E}{D}
<\frac3{25}\sin(\pi/12)
<\frac3{25}\frac{11}{42}
=\frac{11}{350}
<\frac1{20}.
\tag{30}
$$

这里使用 sin(x)<x 和 pi<22/7，全部最后比较均为有理数。
因此在这些条件下，加高而仍保持 C3 的窄固定帽不能支付强 quotient 目标；
这不否决 R100 的 held/D≥.2 路线。

若追求 delta_E/D≥1/20 而保留 C2/C3 双对称，至少必须有

$$
\frac bD\ge
\frac1{40\sin(\pi/12)}
=\frac{\sqrt6+\sqrt2}{40}.
\tag{31}
$$

有限的真实 Lambda 再由 (26) 提供更强限制。
b 是**所有固定部分的实际最大轴距**，不是单独的边界 cuff 半径；
若固定帽发生 overhang，不能未经证明把 b 换成 cuff 半径。
同样，D 必须来自该新完整图，不能把 R21 的旧帽高度或某个 D 上界倒作新图的 D 下界。
破坏固定部分的 C3 对称、扩大其实际轴距或改用新的活动/整体几何，
都改变本条件的适用范围；本文不据此预支任何这样的新闭构造。

### 不需新数值常数的 C2/C3 直径限制

二重活动对称还给一个全域几何界。若 $p=(w,z)\in A$，则 $(-w,z)\in A$，所以 $2|w|\le D$。由法向投影不增加长度，
$$\Lambda\le R_A\le D/2.$$
将这个真实上界代入 (26)，对于 C2 活动体、完整 C3 固定部分及强目标 $\delta_E/D\ge1/20$，必有
$$
\boxed{\frac bD\ge
\frac{1}{40\sin(\pi/12-1/20)}
>\frac{21}{178}.} \tag{32}
$$
最后的严格有理界由
$$0<\pi/12-1/20<11/42-1/20=89/420,\qquad \sin x<x$$
直接得到。若还有该新图自身的 $b\le8/25$，则
$$\boxed{D<\frac{1424}{525}<2.713.} \tag{33}$$
这不需要为新图另填一个未经计算的法向速度常数。它仍不把一个 $D\le2.9$ 的上界当成 $D=2.9$，所以不能据此排除所有满足那个上界的候选；它只是要求双强目标的新图实际还必须满足 (33)。破坏完整固定部分的 C3 对称会改变此前提，单独的强 held 目标也不受 (32) 限制。
