# R24：保持中心作用量的精确均值曲线与第四模横截

2026-11-10，visible-exact-astra-76e8。

**状态：已证明的中间结论。** 本文给 R20 背景一个可自由选择的轴对称
均值方向：中心正势的作用量准确不变，而第四模仍严格横截。它可用于
选择有限幅计算中的均值自由度，避免仅靠深度变化产生中心作用量漂移。
本文没有从作用量不变推出全部高模非共振，更没有证明非径向实际逆
或有限幅非线性存在。

## 1. 对象、明确两个方向与结论

固定整数 $k\ge1$，令
$$
\mu=k\sqrt2,\quad A=\mu^2+\mu/4,\quad
V=A\operatorname{sech}^2x-\mu^2,\quad
q=-V,\quad h''=qh,\quad h(0)=1,\ h'(0)=0.
$$
R20 已证明 $h>0$。第四模核为
$$y=\operatorname{sech}^{4\mu}x,\qquad w=h'/h.$$
令 $x_0>0$ 为唯一正转折点，则
$$
\tanh^2x_0=\frac1{4\mu+1},\qquad
V>0\ \text{于 }(-x_0,x_0),\quad V=0\ \text{于 }\{\pm x_0\}.
\tag{1.1}
$$
两个明确非负偶函数为
$$
\phi_i(x)=
\begin{cases}
\exp\!\left(1-\dfrac1{1-64k^2x^2}\right),&|x|<1/(8k),\\
0,&\text{其它},
\end{cases}
\tag{1.2}
$$
以及
$$
v(x)=(4\mu+1)\tanh^2x,\qquad
\phi_o(x)=\Psi(8v(x)-6),
$$
$$
\Psi(s)=
\begin{cases}
\exp\!\left(4-\dfrac1{s(1-s)}\right),&0<s<1,\\
0,&\text{其它}.
\end{cases}
\tag{1.3}
$$
它们为 $C^\infty$ 函数。外方向恰支持在 $3/4<v<7/8$ 的两个对称小区间，
严格位于正势区内，离转折点有正距离。内方向的支持满足
$v\le(4\mu+1)/(64k^2)<1/8$，所以两支持不交。

定义实际背景
$$
h_{\alpha,\beta}=h\exp(\alpha\phi_i+\beta\phi_o),\qquad
V_{\alpha,\beta}=-h_{\alpha,\beta}''/h_{\alpha,\beta}.
\tag{1.4}
$$
存在零点附近唯一的实解析函数 $\beta=\beta(\alpha)$、$\beta(0)=0$，
满足
$$
\mathcal J(\alpha,\beta(\alpha))=\mathcal J(0,0),\qquad
\mathcal J(\alpha,\beta)=
\int_{-x_0}^{x_0}\sqrt{V_{\alpha,\beta}(x)}\,dx.
\tag{1.5}
$$
在足够小的实参数区间内，根号确为正势内部的正根；
整个正势区及两转折点都不变。并且
$$\beta'(0)<0.\tag{1.6}$$

令 $E_4(\alpha)$ 为
$$-\partial_x^2-16V_{\alpha,\beta(\alpha)}$$
从原零特征值延续出的简单特征值。则
$$
\boxed{\quad E_4'(0)<-\frac7{2k}<0.\quad}
\tag{1.7}
$$
因此严格保持 (1.5) 后，第四模调节仍有明确横截量。
核心以外的 $h$、势和全部端点 jet 完全不变；实际曲面两端高度可分别
有常数平移，和 R16 的均值自由度相同。

## 2. 作用量导数对任意正方向严格为负

先取任意非零、非负、光滑偶函数 $\phi$，支持紧含于正势区。
由 $h_\gamma=he^{\gamma\phi}$，
$$
\dot V=-\phi''-2w\phi'.
\tag{2.1}
$$
设 $f=V^{-1/2}$，只在包含支持的正势紧区间使用它。
两次分部积分给
$$
\dot{\mathcal J}
=\frac12\int\frac{\dot V}{\sqrt V}
=\int\phi\left[-\frac12 f''+(wf)'\right].
\tag{2.2}
$$
没有转折点边界项，因为 $\phi$ 在其附近恒为零。

在正半个正势区，$h''=-Vh<0$，所以 $h'<0$、$w<0$，
而 $w'=-V-w^2<0$。又
$$
V'=-2A\operatorname{sech}^2x\tanh x<0,
$$
$$
V''=-2A\operatorname{sech}^2x(1-3\tanh^2x)<0,
\tag{2.3}
$$
因为 $\tanh^2x<(4\mu+1)^{-1}<1/3$。因此
$$
f'>0,\qquad
f''=\frac34 V^{-5/2}(V')^2-\frac12V^{-3/2}V''>0,
$$
且 $(wf)'=w'f+wf'<0$。于是 (2.2) 的密度严格为负。
在负半轴由偶性相同，零点处也由 $V''(0)<0,w'(0)<0$ 得严格负值。
所以
$$
J_i:=\partial_\alpha\mathcal J(0,0)<0,\qquad
J_o:=\partial_\beta\mathcal J(0,0)<0.
\tag{2.4}
$$

## 3. 两个方向的第四模投影具有相反符号

对任意上述 $\phi$，R16/R20 的准确核投影恒等式为
$$
\kappa(\phi)=-32\int\phi D\,dx,\qquad
D=(y'-wy)^2+15q\,y^2.
\tag{3.1}
$$
等价地，
$$
\left.\frac{d}{d\gamma}E_4(\gamma)\right|_0
=-\frac{\kappa(\phi)}{\|y\|_2^2}.
\tag{3.2}
$$
对 $\phi_i$，R20 的逐项估计已经支付
$$\kappa_i:=\kappa(\phi_i)>\frac7k.\tag{3.3}$$

下面独立付外方向的相反符号。首先 $x_0<1/2$：
由 $\tanh(1/2)>11/24$、$\mu\ge\sqrt2>7/5$，
$\tanh^2(1/2)>121/576>(4\mu+1)^{-1}$。
在 $[0,x_0]$ 上，$\tanh x\ge(11/12)x$。
记 $t=\tanh x$、$\delta=\mu/4$。此处 $-\delta\le q<0$、$h\le1$，
故
$$
h\ge1-\frac{\delta x^2}{2}
\ge1-\frac{18\mu}{121(4\mu+1)}
>1-\frac9{242}>\frac{24}{25},
$$
$$
|h'|\le\delta x\le\frac3{11}\mu t,\qquad
|w|\le\frac{25}{88}\mu t.
\tag{3.4}
$$
又 $y'/y=-4\mu t$，所以
$$
\left|\frac{y'}y-w\right|
\ge\left(4-\frac{25}{88}\right)\mu t
>\frac{11}{3}\mu t.
\tag{3.5}
$$
在外支持上 $v>3/4$，故
$$
t^2>\frac{3}{4(4\mu+1)},\qquad
V=\frac{\mu}{4}(1-v)<\frac{\mu}{16}.
$$
使用 $4\mu+1<5\mu$，得到
$$
\frac{D}{y^2}
>\frac{121}{9}\mu^2t^2-15V
>\frac{121\mu}{60}-\frac{15\mu}{16}
=\frac{259\mu}{240}>\mu.
\tag{3.6}
$$
负半轴由偶性相同。因此
$$
\kappa_o:=\kappa(\phi_o)
<-32\mu\int\phi_o y^2\,dx<0.
\tag{3.7}
$$
外方向既不退化，也不是把未知符号当作数值输入。

## 4. 精确保持作用量，而非仅一阶消失

令 $\zeta=\alpha\phi_i+\beta\phi_o$。准确展开为
$$
V_{\alpha,\beta}
=V-\zeta''-2w\zeta'-(\zeta')^2.
\tag{4.1}
$$
所有变化紧支在两块原正势区内；其余地方的势完全不变。
支持的闭包离 $\pm x_0$ 有正距离，且原 $V$ 在这些闭包上有正最小值。
因此在某个明确由这些有限上确界决定的参数邻域中，变化后的势在支持上
仍正；原正势区、转折点和外部负势区全都保持。

在变化支持上，正根号是势的实解析函数；支持外积分项与参数无关。
故 $\mathcal J$ 对 $(\alpha,\beta)$ 实解析。
由 (2.4) 的 $J_o\ne0$，通常的实解析隐函数定理给唯一的局部曲线 (1.5)，
并且
$$
\beta'(0)=-\frac{J_i}{J_o}<0.
\tag{4.2}
$$
不需要把逐阶保持作用量的形式级数当作实际曲线。
这里未声称该参数区间有指定可见振幅大小。

## 5. 沿精确曲线的真实第四模横截

原第四模零特征值为简单基态，非零谱距离大于 $10k$（R20）。
(4.1) 给紧支有界的实解析乘法扰动，所以在足够小参数区间内存在唯一
邻近的简单特征值和归一化特征向量。可直接在半径小于 $5k$ 的原 resolvent
围道上用 Neumann 级数构造谱投影，再将特征方程求导；
这证明所用的可微性，并给
$$
E_4'(0)=
-\frac{\kappa_i+\beta'(0)\kappa_o}{\|y\|_2^2}.
\tag{5.1}
$$
因为 $\beta'(0)<0$、$\kappa_o<0$，分子严格大于 $\kappa_i>7/k$。
同时 $8\mu>2$，故
$$
\|y\|_2^2=\int\operatorname{sech}^{8\mu}x\,dx
<\int\operatorname{sech}^2x\,dx=2.
$$
于是 (5.1) 给 (1.7)。

几何也来自同一个 $h_{\alpha,\beta}$：
$a_{\alpha,\beta}=h_{\alpha,\beta}^{-1}$，
$z_{\alpha,\beta}(x)=\int_0^x h_{\alpha,\beta}^{-2}$。
两端完全保留原 $h$ 的尾和极点二阶图，只平移高度常数；
$z_x>0$ 保持内部无自交，补两极后仍是闭 $C^2$ 嵌入。
本节只说明实际均值方向合法，不提供其有限幅几何比例。

## 6. 可以据此做什么，不能据此做什么

(1.5) 是中心正势作用量的准确恒等式。它提供一个可以实现的均值参数
选择，同时保留一个已付常数的低模横截方向。这比只检查某次计算中
一个近共振模的符号更稳定，也不要求把平均度量固定为原输入。

但是作用量只记录径向高频主相位的一项信息。
它不等于全部 Sturm 特征值，不控制所有次阶项，更不控制实际非径向
线性化的模式耦合。因此不能由 (1.5) 宣称 R20 的完整算术谱隙在这条
曲线上仍成立，也不能宣称已经构造出精确非旋转嵌入。
数值采用该自由度后，仍需计算完整未投影度量残差、支付实际无限频率逆、
真实平尾接合及可见幅度。
