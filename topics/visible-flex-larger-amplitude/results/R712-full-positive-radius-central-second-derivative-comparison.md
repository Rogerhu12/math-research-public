# R712 — 全部正均值半径下的新旧中央 seed 径向二阶严格比较

2026-11-26。会话 `Astra-larger-e4e2a2bf-20261126 / geometry`。

**状态：以下准确解析结论已完整证明，没有科学执行、实际候选数值或新的通过门。** 本条将 [R711](R711-smooth-triangle-central-profile-and-geometric-comparison.md) §6 的中央径向二阶比较扩展到整个 $0<r<1$。它保留同一 [R709](R709-global-convex-mean-closure-without-contraction.md) 准确均值、核心、高度、端层和中央物理长度。已排五段工作 kernel 的区间仍是 $(0,\pi/2)$，本条没有修改它、放宽它的实际根判据，或把数学延拓冒成已经运行。

## 1. 固定对象与命题

保持 R708/R709 的同一个准确均值解 $v(\phi)$，令

$$
r(\phi)=|v(\phi)|\in(0,1),\qquad d=v/r,
$$

并保持同一个单位向量 $w(\phi)\perp d(\phi)$。$w$ 仍是原极向径向向量投影后归一化所得，所有全角选择、周期和反射责任沿 R708/R709；本条不重新选择另一套架。

在每个原中央物理段 $I_i=[a_i,b_i]$ 上，记 $\ell_i=b_i-a_i>0$、$t=(s-a_i)/\ell_i$。比较两条准确单位 meridian：

$$
T_{\rm old}=\cos(\lambda_{\rm old}h_\epsilon(t))d
 +\sin(\lambda_{\rm old}h_\epsilon(t))w,
$$
$$
T_{\rm new}=\cos(\lambda_\delta h_\delta(t))d
 +\sin(\lambda_\delta h_\delta(t))w,
\qquad \epsilon=\frac1{10},\quad\delta=\frac1{128}.
\tag{1}
$$

这里 $h_\epsilon$ 是原五段 profile，$h_\delta$ 是 R711 的平滑三角 profile；两根均用**准确积分**定义，使各自的 cos 均值等于同一个 $r$。两种奇对称 profile 的 sin 均值均为零，所以两段完整向量积分都等于 $\ell_i v$。

**命题。** 对每个 $r\in(0,1)$，新 profile 有 R711 已证的唯一根 $\lambda_\delta\in(0,\pi)$；原五段 profile 在其自然数学延拓 $(0,\pi)$ 上也有唯一根 $\lambda_{\rm old}$。当 $F_s=T$ 是对应准确、零外层旋转、零额外 normal 校正的已闭合 seed 时，逐个中央段、逐个角有

$$
\boxed{\quad
\max_{s\in I_i}|F_{ss,\rm new}(s,\phi)|
\le C_*\max_{s\in I_i}|F_{ss,\rm old}(s,\phi)|,
\qquad
C_*:=\frac{256\pi\sqrt2}{2325}<\frac12.
\quad}
\tag{2}
$$

同一个常数也可用于再对全部 $\phi$ 取上确界。无需 $r>2/\pi$。这个常数比 R711 半区间上的较强常数更宽松，换取的是完整正半径范围；旧半区间结论仍保留。

## 2. 原五段 profile 的准确自然延拓

为明确实际比较对象，令

$$S_5(u)=10u^3-15u^4+6u^5.$$

原准确 profile 的五段是

$$
h_\epsilon(t)=
\begin{cases}
S_5(t/\epsilon),&0\le t\le\epsilon,\\
1,&\epsilon\le t\le\frac12-\epsilon,\\
1-2S_5\!\left(\frac{t-\frac12+\epsilon}{2\epsilon}\right),
 &\frac12-\epsilon\le t\le\frac12+\epsilon,\\
-1,&\frac12+\epsilon\le t\le1-\epsilon,\\
-S_5((1-t)/\epsilon),&1-\epsilon\le t\le1.
\end{cases}
\tag{3}
$$

对 $0<\epsilon<1/8$，它满足 $|h_\epsilon|\le1$、$h_\epsilon(1-t)=-h_\epsilon(t)$。两平台总长度为 $1-4\epsilon>0$，三个过渡段总长度为 $4\epsilon$。定义准确矩函数

$$A_\epsilon(\lambda)=\int_0^1\cos(\lambda h_\epsilon(t))\,dt.$$

它在实线上光滑，$A_\epsilon(0)=1$。对 $0<\lambda<\pi$，

$$
A_\epsilon'(\lambda)
=-\int_0^1 h_\epsilon(t)\sin(\lambda h_\epsilon(t))\,dt<0.
\tag{4}
$$

被积量在全段非负，在两个平台上等于严格正的 $\sin\lambda$，所以不等式严格。又因平台在 $\lambda=\pi$ 时贡献 $-(1-4\epsilon)$，过渡段贡献至多 $4\epsilon$，

$$
A_\epsilon(\pi)\le8\epsilon-1<0.
\tag{5}
$$

因此连续性与严格单调性给出：对每个 $0<r<1$，$A_\epsilon(\lambda)=r$ 在 $(0,\pi)$ 有且只有一个根。特别对 $\epsilon=1/10$，式(5)上界是 $-1/5$。

这也给出根在 $r\in(0,1)$ 上的光滑依赖，因为根处的导数从不为零。与同一个准确全角 $r(\phi)$ 复合，根的周期、反射以及所需角向正则性均由唯一性继承；没有逐角任意挑选另一个分支。

现有工作源 `supported_unit_seed_mean_jets.py` 的 `central_amplitude_bracket` 明确取 `hi=pi/2`，并检查严格工作 bracket。该实现及其来源 SHA 保持不变。上面的自然延拓只是准确函数 (3) 的数学结论；若将来真要运行旧 profile 的 $(0,\pi)$ 变体，必须有独立完整源、模型、求积与根身份，不能绕过现有 guard。

## 3. 整个 $(0,\pi)$ 上的 sinc 亏损界

令

$$f(x)=\frac{1-\sin x/x}{x^2}=\frac{x-\sin x}{x^3},\qquad0<x<\pi.$$

直接微分得到

$$
f'(x)=-\frac{g(x)}{x^4},\qquad
g(x)=2x+x\cos x-3\sin x.
\tag{6}
$$

各阶导数为

$$
g'(x)=2-2\cos x-x\sin x,\qquad
g''(x)=\sin x-x\cos x,\qquad
g'''(x)=x\sin x.
$$

在 $0<x<\pi$ 上 $g'''(x)>0$，而 $g(0)=g'(0)=g''(0)=0$。连续积分三次即给 $g''(x)>0$、$g'(x)>0$、$g(x)>0$。因此 $f$ 严格递减，且

$$
f(x)>f(\pi)=\frac1{\pi^2}.
$$

所以得到完整区间界

$$
1-\operatorname{sinc}x\ge\frac{x^2}{\pi^2},
\qquad0<x<\pi.
\tag{7}
$$

写成非严格形式便于后续统一使用；在这个开区间内实际为严格大于。

对 $0<r<1$，记 $\lambda_\triangle\in(0,\pi)$ 为唯一 sinc 根。其存在唯一性可直接由端值 $1,0$ 和

$$
\sin x-x\cos x=\int_0^x t\sin t\,dt>0
$$

得到。将其代入(7)，

$$\lambda_\triangle\le\pi\sqrt{1-r}.$$

R711 已证明同一全区间上
$A_\delta(\lambda)\le\operatorname{sinc}\lambda$，且两函数严格下降。因此其唯一根满足

$$
\lambda_\delta\le\lambda_\triangle\le\pi\sqrt{1-r}.
\tag{8}
$$

这里没有使用 $\lambda_\triangle<\pi/2$ 或 $r>2/\pi$。

## 4. 旧根的统一下界与中央二阶比较

对任何满足 $|h|\le1$ 的旧 profile 以及 $0<\lambda<\pi$，cos 的偶性和在 $[0,\pi]$ 上的单调性给

$$\int_0^1\cos(\lambda h(t))\,dt\ge\cos\lambda.$$

又有

$$1-\cos\lambda=\int_0^\lambda\sin u\,du\le\int_0^\lambda u\,du=\frac{\lambda^2}{2}.$$

因而任何该区间内满足准确均值 $r$ 的旧根均有

$$
r\ge\cos\lambda_{\rm old}\ge1-\frac{\lambda_{\rm old}^2}{2},
\qquad
\lambda_{\rm old}\ge\sqrt{2(1-r)}.
\tag{9}
$$

这一下界不需要旧 profile 的特殊五段公式；五段公式仅用于准确存在性和其最大斜率。

固定角 $\phi$ 后，$d,w,\lambda$ 沿同一中央径向段不变。由它们是正交单位向量，

$$
|T_s|=\frac{\lambda}{\ell_i}|h'(t)|.
\tag{10}
$$

在所比较的准确闭合初 seed 上 $F_s=T$，所以 $|F_{ss}|=|T_s|$。原 $S_5'$ 的准确最大值为 $15/8$。式(3)的三个过渡段均给同一最高相位斜率 $15/(8\epsilon)$，于是

$$
\max_{s\in I_i}|F_{ss,\rm old}|
=\frac{75\lambda_{\rm old}}{4\ell_i}.
$$

R711 已给 $\max|h_\delta'|=4/(1-4\delta)$，在 $\delta=1/128$ 时为 $128/31$，故

$$
\max_{s\in I_i}|F_{ss,\rm new}|
=\frac{128\lambda_\delta}{31\ell_i}.
$$

两根均严格正，可相除。将(8)(9)代入，

$$
\frac{\max_{s\in I_i}|F_{ss,\rm new}|}
 {\max_{s\in I_i}|F_{ss,\rm old}|}
=\frac{512}{2325}\frac{\lambda_\delta}{\lambda_{\rm old}}
\le\frac{512}{2325}\frac{\pi\sqrt{1-r}}{\sqrt{2(1-r)}}
=\frac{256\pi\sqrt2}{2325}=C_*.
\tag{11}
$$

因此式(2)的非严格比例界已证，并且该常数与 $r$、$\phi$ 和共同 $\ell_i$ 无关。

## 5. $C_*<1/2$ 的自足有理证明

这里不依赖浮点近似。准确多项式除法给

$$
\frac{x^4(1-x)^4}{1+x^2}
=x^6-4x^5+5x^4-4x^2+4-\frac4{1+x^2}.
$$

两边在 $[0,1]$ 积分，利用 $\arctan1=\pi/4$，

$$
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx
=\frac17-\frac23+1-\frac43+4-\pi
=\frac{22}{7}-\pi.
\tag{12}
$$

严格正性来自被积函数在 $(0,1)$ 严格为正。因此 $\pi<22/7$。又因 $2<100/49$，有 $\sqrt2<10/7$。所以

$$
C_*<\frac{256}{2325}\frac{22}{7}\frac{10}{7}
=\frac{56320}{113925}<\frac12,
\tag{13}
$$

最后一步等价于整数不等式 $112640<113925$。式(2)的严格半数上界至此完整成立；没有执行数值积分、采样或科学计算。

## 6. 保留的几何范围与尚未支付的责任

本结论覆盖原旧根已经位于 $(0,\pi/2)$ 的全部**准确共同正半径范围**，不再要求 $r>2/\pi$；同时覆盖式(3)准确函数在 $(0,\pi)$ 的全部 $0<r<1$ 自然延拓。工作 bracket、工作根和准确根的误差仍须相应完整费用，不能从一个工作日志直接宣布准确比较前提已付。

比较保持同一个准确均值 $v$、$d,w$、同 core/H、相同端层和相同中央长度。每段准确积分及其两角导数仍相同，故 R711(16)–(17) 的支持内局部化和支持外三 jet 一致性继续适用；R711(18) 的完整角 frame、(19) 的真正主曲率矩阵上界以及(20)–(21)的位置/握持/Gram 预算也可继续消费新输入。

但式(2)仅控制**中央段**的径向二阶向量，不称全部端层二阶也减半，更不称整场 principal curvature 或 reach 改善。新旧场的混合与角向二阶、法向投影、Gram 正性、全相位嵌入与近远点分离仍必须由同场完整论证支付。特别，超过 $\pi/2$ 的准确相位可能使某些竖直方向反转，不能迁移原单调高度或已有嵌入论据。

若外层旋转已非零，或实际 normal 校正不是零，换 seed 会改变相应积分及隐式根；本条不把准确初 seed 的比例迁给未比较的优化末场。当前工作求积、根和浮点费用仍由 R710/R707 等完整链负责。原 $10^{-6}$、幅度、Euclidean 商、握持、reach 与固定问题加密完成标准均保持原定义；本条不增加 fixture 或新的预先通过门。
