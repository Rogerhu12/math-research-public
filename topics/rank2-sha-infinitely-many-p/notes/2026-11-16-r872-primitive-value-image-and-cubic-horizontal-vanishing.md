# 原 charge 四十 cubic 原函数格的真实值像与三倍水平消失

日期：2026-11-16。**状态：下列原值像单射、完整水平 Cartier 理想及同一高前缀的额外除子成本已证明。未证明剩余 $K_1$ 商的三尾像，亦未证明新的非 $F^2$ 首核存在。**

本注接[原 cubic 原函数格](2026-11-16-r872-native-cubic-euler-primitive-and-tail-nullspace.md)。
沿用其全部原假设，特别
$$
L=E+40,\quad p>D+40,\quad
\mathscr V_j=\mathcal W_D\cap F^j k(t)[Y],\quad
\mathscr J_3=L^{-1}(\mathscr V_3),
$$
以及 $C=(F)$ 几何整、$e=EF$ 在原点 $P$ 为单位。
所有来源仍是同一个原 $\mathcal W_D\subset H^0(X,\mathcal O_X(B_D))$。
记
$$
H_-= (Y=0)^{\rm strict},\qquad
H_+=(Y=\infty)^{\rm strict},\qquad
D_\pm=C\cap H_\pm .
$$
$C$ 不等于水平边界，故 $D_\pm$ 是 $C$ 上的实际有效 Cartier 交除子；
重数、闭点和固定角均保留。

## 1. 值核准确只有第四幂格

前注的交还可加强为
$$
\boxed{\mathscr J_3\cap\mathscr V_1=\mathscr V_4.}
\tag{1}
$$
确实，若 $W=FB$ 且 $LW\in(F^3)$，则
$$
LW=eB+FLB .
$$
模 $F$ 及 $\gcd(F,e)=1$ 先给 $F\mid B$。
然后应用前注已经支付的两次除法，得到 $F^4\mid W$。
反向由 $L(F^4B)$ 被 $F^3$ 整除立即成立。
所有分母只用原 $2,3$ 及 charge 单位。

所以实际限制给单射
$$
\boxed{
\operatorname{res}_C:\mathscr J_3/\mathscr V_4
\hookrightarrow H^0(C,\mathcal O_C(B_D)).
}
\tag{2}
$$
这并不把右边当成满像；左边的原函数评价仍有全部原来源限制。

## 2. 真实全局商，而非形式分母

若 $W\in\mathscr J_3$，写
$$
LW=F^3A .
\tag{3}
$$
式 (3) 首先是原有理函数域中的因子关系。
因为 $LW$ 是 $B_D$ 的全局正则截面，且沿整 Cartier 曲线 $C$ 的消失阶至少三，
除去原 $3C$ 截面后，所得商实际属于
$$
\boxed{A\in H^0(X,\mathcal O_X(B_D-3C)).}
\tag{4}
$$
在任一原单位框中，(3) 因而是 $l(w)=f^3a$，其中 $f,w,a$ 全都正则。
这一步支付了角点处 $a$ 的整性；不能只由一个 $k(t)[Y]$ 形式商替代它。

## 3. 原两严格水平框上的三次理想

这里使用[十九角 Euler 框](2026-11-15-original-global-euler-frames-and-complete-alpha-residue-pair.md)
及原 $B_D$ 的同一单项式线性化框。

沿严格 $H_-$ 取水平参数 $x$，底参数 $z$ 不受 $E$ 作用。
原局部算子是
$$
l_-=40+x\partial_x .
$$
沿严格 $H_+$，在原 $Y$ 次数上界为 $D$ 的框中是
$$
l_+=D+40-x\partial_x .
\tag{5}
$$
在与固定底纤维相交处，使用保底参数的吹起图。
原框只增乘底参数的幂及底参数单位，不引入依 $x$ 的任意单位。
后续链的图由同一线性化延拓；本节只在严格水平邻域应用 (5)，
不将它套给其它非水平 exceptional 分量。

具体地，负水平的第 $n$ 个原 charge 系数除以 $40+n$；
正水平以 $x^{D-n}$ 表示同一项，其特征同样为 $40+n$。
因此全部逆因子都在原集合
$$
40,41,\ldots,40+D
$$
中，由 $p>D+40$ 逐个为单位。
原固定角的 $z$ 整除条件也逐系数保持。

在这些实际框中，设 $f_0(z)=f(z,0)$，取
$$
I=(x,f_0(z)).
$$
因为 $f\in I$、$a$ 正则，(3) 右边属于 $I^3$。
而 $I^3$ 按 $x$ 次数分次：第 $x^n$ 项在 $n<3$ 时必须被
$f_0^{\,3-n}$ 整除，$n\ge3$ 时没有这个附加条件。
(5) 的逆只把每个原系数除以一个常数单位，所以
$$
l_\pm^{-1}(I^3)\subseteq I^3 .
$$
由此 $w\in I^3$。在原曲线环 $\mathcal O_C$ 中，
$f_0=f-x(f-f_0)/x$，故
$$
I\mathcal O_C=(x).
$$
结论是原环中的实际整除，而不只是正规化上逐支的阶界：
$$
\boxed{w|_C\in(x^3).}
\tag{6}
$$
这个证明不要求 $F_t$ 或 $F_Y$ 为单位，因此保水平重根、原固定角、
奇点 conductor 下降及全部残域。任意依 $x$ 的换框会改变 (5)，
所以证明没有在那样的未校准框中使用逐系数逆。

两水平图合起来给
$$
\boxed{
\operatorname{res}_C(\mathscr J_3)
\subseteq
H^0\!\left(C,\mathcal O_C(B_D)(-3D_--3D_+)\right).
}
\tag{7}
$$

## 4. 同一个高前缀的真正限制

仍在前注 $r=3,\ \tau\in\{1,2,3\},\ \tau<\ell\le h-1$ 的原窗口，
令 $T=s-13$。
沿 $C$ 的原非垂直支 $Y=\psi(t)$，置
$$
\zeta=\log(g_{\Theta,\circ}/\psi),\qquad\operatorname{ord}_w\zeta=h .
$$
对 $W\in\mathscr J_3$，(3) 及其两次 $L$ 导数给
$$
(LW)|_C=(L^2W)|_C=(L^3W)|_C=0 .
$$
而
$$
(L^4W)|_C=6e^3A|_C .
$$
前注的真实 Gauss 门已给 $A\in t^2$。
在 $P$ 的原单位框内作 Euler Taylor 展开，得到
$$
e^{40\zeta}W(t,g_{\Theta,\circ})
=W|_C+O(w^{4h+2}).
\tag{8}
$$
这里只需长度 $T<2h+2$，所有所用阶乘都是原 $p$ 单位；
高阶项不被当作额外长窗。
公共 $U_0/P_{134}$ 和 $t/w$ 仍是原已固定单位。

因此前注的唯一实际值门等价于
$\operatorname{ord}_P(W|_C)\ge T$。
结合 (1)、(7)，有真正单射
$$
\boxed{
(\mathscr J_3\cap K_1)/\mathscr V_4
\hookrightarrow
H^0\!\left(
C,\mathcal O_C(B_D)(-TP-3D_--3D_+)
\right).
}
\tag{9}
$$
右侧仍只是容纳原值像的空间，未被认成可以任选的截面格。

例如记
$$
d=B_D\cdot C,\qquad
z_-=C\cdot H_-,\qquad e_+=C\cdot H_+ .
$$
非零原值必须满足准确交数门
$$
\boxed{T+3z_-+3e_+\le d.}
\tag{10}
$$
如果这个严格反门成立，则
$\mathscr J_3\cap K_1=\mathscr V_4$。
此结论仅约束本原函数块；不排整个非 $F^2$ 首核。
这里 $z_-$ 是完整水平交数，不能用某个去固定因子后的多项式次数
直接替代。

## 5. 对原边界行和剩余商的含义

式 (6) 是整个三倍 Cartier 水平交上的零值，
所以用 $\mathscr J_3\cap K_1$ 调整一个原修正，
不能改变其在 $3D_-$ 或 $3D_+$ 上的相应实际 restriction 类。
这不是把其它边界残数或原高 normal 行宣称为零：
它们可能读取更高 jet，或读取同一个 $W$ 在非水平分歧处的值。

特别，前注已经支付的三尾零像仍是
$$
\Pi:K_1/(\mathscr J_3\cap K_1)\longrightarrow k^3 .
$$
本注补出被商去部分的真实全局值限制。
剩余来源商、同一个 $R,S$ 的其它 Bockstein 行和指定 forcing
仍须联立；没有由 (9) 的维数或 (10) 的不足主阶宣布原目标完成。

本注为原符号和实际框推导，无新增数学数值运行。
