# R381：修正后 H 通量的全部真实有序尾准确消去

日期：2026-11-15。**原式纸面证明；没有执行新的 profile 积分、符号程序、旧根恢复、秩计算、人工检查或研究运行。**

[R378](R378-correction-of-the-third-history-term-in-the-complete-H-flux.md) 补回了第四阶 $YC$ 配对中第三 history 的完整 $P_s,B_s$ 链式项。本稿单独关闭该修正的真实有序尾：在原速度三次梯度已准确分离后，旧尾一形式与新增尾一形式逐项相消。因此，修正后的两个 H 总通量的速度 curl 没有剩余的有序三矩尾贡献。

本稿不把第二场的真实左值设为零，也不声称完整 self 部分或整个 H 通量为零。其完整连续 $C^2$ self 余项另行处理。

## 1. 固定原锚与基准数据

固定共同右 collar，记
$$
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad
u\in C_c^\infty((\ell,r_*)),\quad
v=u',\quad r=u'',\quad t=u'''.
$$
先在 $h=1,d=h\omega-k=0$ 的基准状态工作，置
$$
Q=1+x^2,\quad L=v-xr,\quad W=u-xv,\quad
G=u-\frac{xv}{2},
$$
$$
F=Qr-2xv+2u,\qquad K=2ur+v^2-2xvr.
\tag{1}
$$
几何速度为 $\gamma=h_s,\delta=d_s$，所以
$$
\vartheta=x\gamma+\delta,\qquad
l=\gamma L-\delta r.
$$

原第二局部第一分子为
$a=\gamma A+\delta B$。它的真实左值为
$$
a_L=\gamma A_L+\delta B_L,\qquad
A_L=\frac{\mu_0-\mu_2}{16},\quad B_L=-\frac{\mu_1}{8},
\tag{2}
$$
$$
\mu_0=\int r^2,\quad
\mu_1=\int xr^2,\quad
\mu_2=\int(x^2r^2+2v^2).
$$
这些值来自同一个真实右包的三矩匹配，不是新增自由参数。
证明保留 $a_L$ 及 $\mathrm d_va_L$，不要求任何一个矩为零。

由 R378 式 (7)、(19)，缺项中的两个准确收缩为
$$
\begin{aligned}
\mathcal D_\delta(f)
&=\frac18\int\{2rL+(xv-2Qr)t\}f',\\
\mathcal D_\gamma(f)
&=\frac18\int
\{-2L^2+[(2+3x^2)v-2Qxr-2xu]t\}f'
+\frac14\int(2u-xv)t f.
\end{aligned}
\tag{3}
$$
它们对同右 collar 为零、左端可有真实尾的 $f$ 也成立。
定义 $\mathcal D_V=\gamma\mathcal D_\gamma+\delta\mathcal D_\delta$。

## 2. 旧尾中已经分开的准确梯度

[R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md) 的原自然读出组合具有固定的 $ZZ_{\rm tail}$ 因子 $1/3$ 和 $YC_{\rm tail}$ 因子 $2/3$。R378 只更正后一配对的第三 history 导数；不改变这些因子。

[R365](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md) §3 在其显示的一形式中，将先前两个真实尾项与
$\Theta_{\rm tail}/3$ 合成
$$
\mathrm d_v\left\{
\frac{a_L}{6}\int t(\gamma-x\delta)a
\right\}.
\tag{4}
$$
这是一个准确速度三次梯度，故其速度外微分为零。这项分离并不依赖被 R378 撤回的 H 非零结论；它只是原显示尾项的代数身份。本文仍保留 (4)，不以端口值为零替代它。

分离 (4) 后，旧显示式中剩余的尾一形式是
$$
\mathfrak T_{\rm old}
=\mathrm d_va_L\,
\{K_{\gamma\gamma}\gamma^2+
 K_{\gamma\delta}\gamma\delta+
 K_{\delta\delta}\delta^2\},
\tag{5}
$$
其中
$$
\begin{aligned}
M_{00}&=(1-\tfrac32x^2)v+(x^3-x)r+xu,\\
M_{01}&=(3x^2-1)r-\tfrac72xv+2u,\\
M_{11}&=2xr-v,
\end{aligned}
$$
$$
\begin{aligned}
K_{\gamma\gamma}
&=\frac1{24}\int t(-FM_{00}-2GL),\\
K_{\gamma\delta}
&=\frac1{24}\int t(-FM_{01}+K),\\
K_{\delta\delta}
&=\frac1{24}\int t(-FM_{11}-vr).
\end{aligned}
\tag{6}
$$
这里引用的是旧一形式中一个明确的组成部分；不重新采用旧稿把整个未修正一形式识别为完整 H 的错误结论。

## 3. 新尾的实际 profile

原右包在整个 outer $u$ 支撑区留下常数第一分子 $a_L$。
R378 式 (11) 给新增第三 history 加速度输入
$$
n_{{\rm tail},\rm acc}
=\frac{\mathrm d_va_L}{4}\{Ql+\vartheta F\}.
$$
直接展开
$$
Ql+\vartheta F=\gamma V_\gamma+\delta V_\delta,
\tag{7}
$$
$$
V_\gamma=(1-x^2)v+2xu,\qquad V_\delta=2(u-xv)=2W.
\tag{8}
$$
右侧两个 profile 都真实紧支撑。这是由原右包的常尾代入完整公式后得到的局部化，不是把右包或其第二场假定为紧支撑。

因自然读出的 $YC_{\rm tail}$ 系数为 $2/3$，新增的尾一形式准确为
$$
\boxed{
\Delta\mathfrak T
=\frac{\mathrm d_va_L}{6}
\,\mathcal D_V(\gamma V_\gamma+\delta V_\delta).}
\tag{9}
$$
后面不重选 $\mathrm d_va_L$；它仍是 (2) 的同一个真实三矩值。

## 4. 三个完整紧导数身份

将 (8) 代入 (3)，保留全部局部项，得到
$$
\boxed{
\mathcal D_\gamma(V_\gamma)+6K_{\gamma\gamma}
=-\frac14\int(L^2V_\gamma)'=0,}
\tag{10}
$$
$$
\boxed{
\mathcal D_\gamma(V_\delta)+\mathcal D_\delta(V_\gamma)
+6K_{\gamma\delta}
=\frac14\int\{rL V_\gamma-2W L^2\}'=0,}
\tag{11}
$$
$$
\boxed{
\mathcal D_\delta(V_\delta)+6K_{\delta\delta}
=\frac12\int(WrL)'=0.}
\tag{12}
$$
每个端点乘积都由 $u,v,r$ 的真实紧支撑支付，与 $A_L,B_L$ 是否为零无关。

以下给出直接展开，以便核对 mixed 因子。

首先
$$
V_\gamma'=(1-x^2)r+2u,\qquad
V_\delta'=-2xr,\qquad
L'=-xt,\qquad W'=-xr.
\tag{13}
$$
代入 (3)、(6)，纯 $\gamma$ 的差为
$$
-\frac14\int L^2V_\gamma'
+\frac12\int xLtV_\gamma
=-\frac14\int(L^2V_\gamma)'.
$$
这里展开后所有 $r^2$、$u^2$ 项先相消，剩余 $t$ 的系数准确是
$4xL V_\gamma$，整体因子为 $1/8$。

mixed 差先合为
$$
\begin{aligned}
&\mathcal D_\gamma(V_\delta)+\mathcal D_\delta(V_\gamma)
+6K_{\gamma\delta}\\
&\quad=\frac14\int
\left\{
rL[2xv+(1-3x^2)r+2u]
+t[(v-2xr)V_\gamma+4xLW]
\right\}.
\end{aligned}
\tag{14}
$$
由 (13)，(14) 的被积式恰是
$\{rLV_\gamma-2WL^2\}'/4$。
它对应一个 $\gamma\delta$ 系数，没有把交叉项错误加倍或折半。

最后，纯 $\delta$ 的差为
$$
-\frac12\int xr^2L
+\frac12\int tW(v-2xr)
=\frac12\int(WrL)'.
\tag{15}
$$
例如
$$
\int tW(v-2xr)=\int xr^2L
$$
可以先对 $r^2$ 和 $r$ 分部积分两次准确核得。这里仍仅使用紧 outer。

## 5. 原 2/3 因子使全部剩余尾一形式消去

由 (10)–(12)，
$$
\begin{aligned}
\mathcal D_V(\gamma V_\gamma+\delta V_\delta)
={}&\gamma^2\mathcal D_\gamma(V_\gamma)\\
&+\gamma\delta\{
\mathcal D_\gamma(V_\delta)+\mathcal D_\delta(V_\gamma)\}\\
&+\delta^2\mathcal D_\delta(V_\delta)\\
={}&-6\{K_{\gamma\gamma}\gamma^2+
K_{\gamma\delta}\gamma\delta+
K_{\delta\delta}\delta^2\}.
\end{aligned}
\tag{16}
$$
将 (16) 代入 (9)，即得
$$
\boxed{\Delta\mathfrak T=-\mathfrak T_{\rm old}.}
\tag{17}
$$

因此，全部真实尾在修正后只剩 §2 已显示的准确速度梯度 (4)；
其 H curl 为零。式 (17) 在一形式层成立，强于只在某个
$\gamma/\delta$ 系数、某个真权或偶 profile 上为零。

这一步始终保留原 self、pure、有序 $2+2$ 的共同右锚与原三矩匹配，
也保留同一原二阶选择。没有让各片段独立重锚，没有把左侧常数变成额外 gauge。

## 6. 状态输运与尚欠的 self

[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md) 的完整正仿射协变及真实三矩的可逆三角输运独立于旧 H 显示值。把 outer、实际右包、锚点和全部字段同时输运后，(17) 仍成立。因此本稿的 H 尾消去不是只在一个单点状态或一个偶输入成立。

原 H 的完整值还含 self 部分。R378 已证明该部分补回缺项后没有
$u'''^2$ principal，并属于连续 $C^2$ 层；本稿只进一步证明没有遗漏的有序尾可在该层另行贡献。

**本稿已付：** 原三条 (10)–(12)、原因子 $2/3$ 下的一形式身份 (17)，以及任意真实左三矩值的 H 尾 curl 为零。

**本稿未付：** 剩余完整 self 是否为零、是否有新的非零 $\Lambda$ 类、
其与 Q4 的关系，以及任何新的具体实际控制维数。
旧 R358/R362/R365/R371 的失效非零与维数证明不因本稿被恢复。
