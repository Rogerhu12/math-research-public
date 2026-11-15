# 原镜轴迹的正水平完整 jet、法向框变换与 t=1 整纤维消去

日期：2026-11-15。**状态：以下实际读取及整纤维消去已证明；指定迹在真实 $\ker\alpha_\eta$ 上的行依赖仍开放。**

接 [R822](../results/R822-original-cartier-residue-descent-and-actual-ramification-trace.md)
与 [对数主部接口](2026-11-15-mirror-trace-logarithmic-principal-part-and-thirteen-tail.md)。
本注始终使用同一个原变化列
$\Delta R=q_{\rm src}t^rF H$、$H\in\mathcal H_2$；
当需要保持原首修正时，仍要求同一个 $H$ 属于真实镜轴核。
没有先指定边界值再另选 normal 修正。

## 1. 实际次数及完整正水平框

使用 R495/R805 的原规范
$$
P^{\rm fact}=d^{-C_D}t^rF^3Q\in\overline{\mathcal W}_D,
\qquad q_{\rm src}=d^{-C_D}Q,\qquad d=1+8t.
$$
记真实次数
$$
a=\deg_tF,\qquad b=\deg_YF,\qquad
c=\deg_YQ=\deg_Yq_{\rm src},\qquad N_*=3b+c.
$$
由原整个来源帽，准确有
$$
3a+r+\deg_tQ\le M_D,\qquad
N_*\le D,\qquad M_D=f_D+C_D .
\tag{1}
$$
没有将清 $d$ 后的 $M_D$ 偷换成 $f_D-1$。
原 $f_D<p$、$D<p$ 和 $C_D<p/2$ 给 $a,b<p$；
故原曲线正规化上的 $t$、$Y$ 两映射都可分且所有局部分歧 tame。

在有限底点的正水平图取
$$
x=Y^{-1},\quad
f(t,x)=x^bF(t,x^{-1}),\quad
\widehat q=x^c q_{\rm src}(t,x^{-1}),\quad
\widehat H=x^{2b}H(t,x^{-1}).
\tag{2}
$$
$\widehat H$ 的 $2b$ 是整个真 $\mathcal H_2$ 的帽；
若该列实际次数更低，就保其额外 $x$ 零，不把它填满。
在非固定有限底点，这些函数均正则。

令
$$
K=t^{2r+1-s}(1-t)^{3s},\qquad
e=\mathcal EF,\qquad
\Lambda_H=W_sF_tq_{\rm src}t^rH\,de/e
$$
为前注的同一个对数留数代表。
在 $C$ 上
$$
e=-x^{1-b}f_x,\qquad
W_sF_tq_{\rm src}t^rH
=Kx^{-N_*}f_t\widehat q\widehat H .
$$
所以准确有
$$
\boxed{
\Lambda_H
=Kx^{-N_*}f_t\widehat q\widehat H
\left((1-b)\frac{dx}{x}+\frac{df_x}{f_x}\right).
}
\tag{3}
$$
这里 $df_x$ 是沿同一曲线的全微分；
不能把它换成固定 $t$ 的偏导 $f_{xx}dx$。

## 2. 光滑移动根的全长系数读取

取非固定的 $Q\in C\cap(Y=\infty)$，并假设 $f_t(Q)$ 为单位。
此时 $x$ 是曲线的局部参数，真实 $t=t(x)$ 满足
$$
t'(x)=-f_x/f_t.
$$
记 $m_t=\operatorname{ord}_Q(t-t(Q))$。
因 $m_t\le b<p$，
$$
f_x(t(x),x)=x^{m_t-1}v(x),\qquad v(0)\ne0.
$$
由 (3) 直接得到
$$
\boxed{
\operatorname{Res}_Q\Lambda_H
=[x^{N_*}]
\left\{
K(t(x))f_t(t(x),x)\widehat q(t(x),x)\widehat H(t(x),x)
\left(m_t-b+x\frac{v'}v\right)
\right\}.
}
\tag{4}
$$
若点不在原域上，先在其剩余域读取 (4)，再作完整域迹。
式 (4) 保真实 $q$、$\widehat H$ 和曲线 $t(x)$ 的全部所需高尾，
并非只取最高 $Y$ 系数在 $Q$ 的值。
$m_t=b$ 时括号常数消失，也必须保后续项，不能自动把整行删去。

## 3. 奇异分支的 conductor 和准确极阶

在同一非固定正水平图中，允许 $Q$ 奇异。
对任一正规化分支取参数 $v$，记
$$
m_x=\operatorname{ord}_v x,\quad
m_t=\operatorname{ord}_v(t-t(Q)),\quad
\mathfrak c_v=\text{该分支的平面曲线 conductor 指数}.
$$
这里 $\mathfrak c_v$ 包括同一平面奇点其他分支的交数。
局部对偶化生成元 $dt/f_x=-dx/f_t$ 的拉回阶为
$-\mathfrak c_v$。
由两投影均 tame，准确有
$$
\operatorname{ord}_v f_x=\mathfrak c_v+m_t-1,\qquad
\operatorname{ord}_v f_t=\mathfrak c_v+m_x-1.
\tag{5}
$$
这是原平面 Gorenstein 曲线与其正规化的 conductor 公式；
没有用“光滑支的 $f_t$ 为单位”代替奇点。

在非固定点 $K$ 为单位。
写 $v_q=\operatorname{ord}_v\widehat q$、
$v_H=\operatorname{ord}_v\widehat H$，均非负。
由 (3)、(5) 及任意有理函数的对数微分至多简单极，
得到真正上界
$$
\boxed{
\operatorname{poleord}_v\Lambda_H
\le
\max\{0,(N_*-1)m_x-\mathfrak c_v+2-v_q-v_H\}.
}
\tag{6}
$$
若 $p$ 整除 $\operatorname{ord}_v e$，对数微分的简单极系数消失，
只会改善 (6)，不在其首项补回一个不存在的整数。
实际残数仍在同一正规化参数中读取，并作全部剩余域迹。
(6) 不是“残数为零”的判据；(4) 给光滑情形中不能省掉的高 jet。

## 4. 原 α 转置在正水平必须保 2b 项

此节只说明同一个真正全局对偶截面的框变换，不假设候选主部已经延拓。
设
$$
\omega\in H^0(C,\omega_C\otimes N_C^{-1}(q_\Delta P)),
\qquad N_C=\mathcal O_C(C).
$$
用原有限 $F$ 框写其普通微分系数为 $\omega_F$；
在正水平局部单位框中写为 $\omega_\infty$。
由于 $F=x^{-b}f$，准确有
$$
\omega_\infty=x^{-b}\omega_F.
$$
同时
$$
x^{2b}\mathcal EH=2b\,\widehat H-x\partial_x\widehat H,\qquad
x^be=-xf_x \quad\text{于 }C.
$$
因此真实法向项为
$$
\boxed{
\frac{(\mathcal EH)|_C}{e}\,\omega_F
=
-\frac{2b\,\widehat H-x\partial_x\widehat H}{xf_x}\,
\omega_\infty.
}
\tag{7}
$$
$2b$ 来自同一个真实 $\mathcal H_2$ 框；
不能因在 $Y=\infty$ 使用 $x\partial_x$ 而删掉。

若仍在第2节的光滑 $f_t$ 单位情形，令
$\omega_\infty=w(x)dx$，则 $w$ 正则。
把固定 $t$ 的 $\partial_x\widehat H$ 与沿 $C$ 的导数区分后，
(7) 除正则项等于
$$
\left(\frac{d\widehat H/dx}{f_x}
-\frac{2b\widehat H}{xf_x}\right)w(x)\,dx .
$$
令 $V=w/f_x$，分部积分准确给
$$
\boxed{
\operatorname{Res}_Q
\left(\frac{\mathcal EH}{e}\omega_F\right)
=
-\operatorname{Res}_Q
\left[\widehat H\left(V'+\frac{2b}{x}V\right)dx\right].
}
\tag{8}
$$
该式与 (4) 的高 jet 不同：
例如 $f_x(Q)$ 也是单位时，(8) 只读
$-2b\,\widehat H(Q)w(Q)/f_x(Q)$；
(4) 仍可读到 $x^{N_*}$。
这不是指定迹已经不在 $\operatorname{im}\alpha_\eta^*$ 的证明，
因为真正 $B_0\in H^0(C,N_C^2(-hP))$ 的各局部 jet 受同一全局来源约束，
而 $\alpha_\eta^*$ 还有原 $P$ 处的值项及其余所有边界。
奇点处 $\omega_\infty$ 使用原对偶化层，拉到正规化可含 conductor 极；
不能将光滑情形的“$w$ 正则”搬到那里。

## 5. 精确充分门下整个 t=1 纤维的残数为零

**整纤维消去。** 若
$$
\boxed{3s>N_*a,}
\tag{9}
$$
则对全部原 $H\in\mathcal H_2$，
$\Lambda_H$ 在 $t=1$ 上每条正规化分支的残数均为零。
这包括原三步吹起链上的所有点和全部奇异分支。

证明如下。在有限 $Y$ 处，$F_t,q_{\rm src},H$ 都正则；
$d(1)=9$ 为单位，因而没有 $q_{\rm src}$ 的分母极。
$K$ 在每条支上含严格正阶 $(1-t)^{3s}$，
故 $A H$ 严格消失，乘至多简单极的 $de/e$ 后无残数。

在 $Y=\infty$ 处，仍用 (2) 的原图再拉到正规化。
令
$$
m_x=\operatorname{ord}x,\qquad
m_t=\operatorname{ord}(t-1).
$$
$\widehat q,\widehat H,f_t$ 正则，并且
$m_t\ge1$、$m_x\le a$。
最后一条既可由 $Y:\widetilde C\to\mathbf P^1$ 的次数为 $a$ 得到，
也可由最高系数 $f_b(t)$ 在 $t=1$ 的完整交数得到，奇点及多分支均保。
所以
$$
\operatorname{ord}(A H)
\ge3s\,m_t-N_*m_x
\ge3s-N_*a>0.
\tag{10}
$$
再次使用 $de/e$ 至多简单极，得每支残数为零。
吹起不改变这些有理函数及正规化分支，故这同时支付原三步链；
全残域迹亦为零。证毕。

(9) 是准确的额外充分门，不因“$r=2$”就自动成立。
若要仅用原 $D$ 帽，一条直接充分条件是
$$
3s>
\frac{D}{3}\left(M_D-r-\deg_tQ\right),
\tag{11}
$$
由 (1) 推得；可以取原整数上取整／下取整作更精细读取。
本注不以未付款的更小 $t$ 帽代入 (11)。

## 6. 真正保留下来的联合问题

在前注已经支付的原 $r=2$ 两类中，非固定 $Y=0$ 移动项确实消失；
在 (9) 下，本注再删去整条 $t=1$ 纤维。
两项都是对原全部变化列成立，因而也对同一个实际镜轴核成立。

正水平其他移动根的 (4)、原 $t=0,h_7,d,\infty$ 及其全部例外仍保留。
尤其前注只删除了对数代表的某些项，并没有同时删除
$\alpha_\eta^*$ 对真正全局 $\omega$ 的对应项。
必须将 (7)–(8) 与原 $P$ 值项、全部边界、原低行右逆高尾一起读取。
没有将高 jet 值当成自由参数，也没有把原 $\Delta=13$ 的短尾移到长 $J$ 窗口。

原 $M$、$P_{134}/U_0$、同一个 $R$、全部 normal、两条十三行 carry 和下一位仍不改变。
本文不声明指定 forcing 非零或主目标完成。
