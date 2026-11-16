# R840 联合交增补 — 非水平分歧的完整低块消元与两个原尾行

日期：2026-11-16。**状态：以下真实有限算子的厚点消元、唯一剩余参数及原函数值的 Taylor 约束已证明。剩余两行与同一高前缀的联合可解性仍开放。**

接
[完整联合交](2026-11-16-r840-full-primitive-and-ramification-ideal-intersection.md)
及
[水平联合块](2026-11-16-r840-actual-horizontal-joint-operator-and-zero-charge-control.md)。
这里处理完整 $\operatorname{ann}_Z(f_2)$ 的另一部分；
没有把高分歧分量换成简单点，也没有加入新的来源。

## 1. 原移动非水平图

保原 $\mathcal H_j,F,e=\mathcal EF,f_2=\mathcal E^2F$、
$Z=V(F,e)$、$3b<p$。
取不在水平或原固定角上的点 $Q$，要求
$$
F_t(Q)\ne0,\qquad Y_Q\ne0,\infty .
\tag{1}
$$
剩余域记为 $k_Q$。用真实参数
$$
x=Y-Y_Q,\quad
u=Y_Q+x,\quad
t=t(x),\quad \tau=t(x)-t_Q,\quad
\mathscr D=u\,\frac d{dx}.
\tag{2}
$$
$\mathscr D$ 是沿曲线的全导数；原固定 $t$ 算子仍是
$\mathcal E=u\partial_x$。本注不使用完整特征 $p$ 对数坐标。

设底投影在此的分歧指数为 $m$。原 $Y$ 次数给
$$
2\le m=\operatorname{ord}_x\tau
 =\operatorname{ord}_xF(t_Q,Y_Q+x)\le b.
$$
因 $m<p$，
$$
\boxed{
e_C=e|_C=x^{m-1}v(x),\quad v(0)\ne0,\qquad
\mathscr D\tau=-e_C/F_t,
}
\tag{3}
$$
$$
Z_Q=\operatorname{Spec}k_Q[x]/(x^{m-1}).
\tag{4}
$$
在这个实际非水平框里没有水平的额外 charge 权。

由固定偏导与曲线全导数的关系，
$$
f_2|_C=\mathscr D e_C+\frac{e_C}{F_t}e_t|_C.
$$
其首项为
$Y_Q(m-1)v(0)x^{m-2}$，故完整局部零化子准确为
$$
\boxed{
\mathcal A_{2,Q}
=\operatorname{ann}_{Z_Q}(f_2)
=(x)/(x^{m-1}).
}
\tag{5}
$$
特别 $m=2$ 时这个零化子确为零；$m>2$ 时则不能预先删掉。

## 2. 真实 $\mathcal O$ 的低行，而非自由微分算子

按完整联合交注，取已经满足
$$
W=FH+eK,\qquad \mathcal EW=FJ,
$$
的同一个原截面，并令
$$
a_C=K|_C=W|_C/e_C,\qquad
a=a_C\bmod x^{m-1}\in\mathcal A_{2,Q}.
\tag{6}
$$
在原呈示中 $J|_Z=\mathcal O(a,B)$。

对任何同一 $W$，
$$
(\mathcal EW)|_C
=\mathscr D W_C+\frac{e_C}{F_t}W_t|_C .
$$
由其在 $C$ 上为零，
$$
W_t|_C=-\frac{F_t}{e_C}\mathscr D(e_Ca_C).
\tag{7}
$$
再固定 $t$ 求导，用 $\mathcal E$ 与 $\partial_t$ 交换，得
$$
F_tJ|_C=\mathscr D(W_t|_C)+\frac{e_C}{F_t}W_{tt}|_C.
$$
因此完整局部恒等式是
$$
\boxed{
J|_C=
-F_t^{-1}\mathscr D
 \left\{F_t\left(\mathscr D+
                 \frac{\mathscr D e_C}{e_C}\right)a_C\right\}
+\frac{e_C}{F_t^2}W_{tt}|_C .
}
\tag{8}
$$
最后一项是同一 $W$ 的真实高项，不在全局删掉。

当 $m\ge3$ 时，严格读取 $<m-3$ 行，(8) 给良定义的原低块
$$
\boxed{
\mathcal L_Q:\ (x)/(x^{m-1})
 \longrightarrow k_Q[x]/(x^{m-3}),
}
$$
$$
\boxed{
\mathcal L_Q(a)=
-F_t^{-1}\mathscr D
 \left\{F_t\left(\mathscr D+
                 \frac{\mathscr D e_C}{e_C}\right)a\right\}
 \pmod{x^{m-3}}.
}
\tag{9}
$$
实际读的是 $\mathcal O$ 投影到这些行。两次微分最多损失两阶，
所以 $a_C$ 改变 $x^{m-1}$ 倍数不影响 (9)；
(8) 的末项也从 $x^{m-1}$ 起。
这不允许把 (9) 延长到最后两行。

原 $B$ 项
$-(2f_3B+3f_2\mathcal EB)$ 的阶至少为 $m-3$，
故它完整留在那最后两行，在 (9) 中准确为零。
因此低块确实只依赖同一个 $a$，也与原 $K_a,U_a,V_a$ 的选择相容。

## 3. 单位消元与唯一核线

**定理 1。** 对 $m\ge3$，(9) 满射，且
$$
\boxed{
\ker\mathcal L_Q=k_Q\cdot\frac{\tau}{e_C}
 \pmod{x^{m-1}}.
}
\tag{10}
$$
其实际秩恰为 $m-3$。

**证明。** 由于
$$
\frac{\mathscr D e_C}{e_C}
=u\left(\frac{m-1}{x}+\frac{v'}v\right),
$$
对源单项 $x^j$，$2\le j\le m-2$，
(9) 的首项为
$$
\boxed{
-Y_Q^2(j-1)(j+m-1)x^{j-2}.
}
\tag{11}
$$
其余项阶至少为 $j-1$。
所有显示因子都为单位：
$1\le j-1$，且 $j+m-1\le2m-3<2b<p$。
因此这些 $m-3$ 列对 $0,\ldots,m-4$ 行构成真正的三角单位块，
证明满射。

由 (3)，
$$
F_t\left(\mathscr D+\frac{\mathscr D e_C}{e_C}\right)
 \frac{\tau}{e_C}
 =\frac{F_t\mathscr D\tau}{e_C}=-1.
$$
外层导数杀掉它，所以 $\tau/e_C$ 在核中。
它的阶恰为一，首系数
$-1/(mY_QF_t(Q))$ 非零，确实是 (5) 中的非零向量。
源维数 $m-2$、像维数 $m-3$，故核准确为这一线。
$m=3$ 时目标为零，论证仍给完整的一维核。证毕。

因此在完整 $\mathcal O=0$ 的求解中：

- $m=2$：没有零化子列，只保原一个目标行。
- $m\ge3$：实际 $m-3$ 个零化子方向由 (11) 唯一消去；
  剩下一个沿 $\tau/e_C$ 的同源参数，以及原第 $m-3,m-2$ 两行。

这两条末行仍含原 $B$、提升的完整高尾及同一个全局来源，
不是可以独立赋值的两个局部条件。
本定理没有宣称它们为零或独立。

## 4. 原函数块给剩余参数的实际含义

若进一步是同一个真正原函数截面
$$
W=\mathcal E_+^{-1}(F^2L)+G_0,\qquad
L\in\mathcal H_1^{>0},\quad G_0\in\mathcal H_3^0,
\tag{12}
$$
则 $\mathcal EW=F^2L$。在 $C$ 上，
$$
\frac d{dx}W_C=\frac{dt}{dx}W_t|_C,\qquad
\frac d{dx}(W_t|_C)=\frac{dt}{dx}W_{tt}|_C.
\tag{13}
$$
第二式使用
$\mathcal EW_t=2FF_tL+F^2L_t$ 在 $C$ 上为零。
所有偏导仍来自同一个 (12)，不把 $W_t,W_{tt}$ 添加为自由来源列。

写 $a_i=(\partial_t^iW)(Q)$，$i=0,1,2$。
因 $W_{tt}|_C=a_2+O(x)$，依次积分 (13)，且 $2m+1<p$，
得到
$$
\boxed{
W_C=a_0+a_1\tau+\frac{a_2}{2}\tau^2+O(x^{2m+1}).
}
\tag{14}
$$
所需有限积分的分母均为单位；没有用特征 $p$ 导数的全局核仅为常数。

式 (14) 特别说明：
整个原 $\mathcal J$ 在 $Z_Q$ 上的值只有实际常数 $a_0$，
不能给任意 $m-1$ 个厚值。
若再有 $W\in\mathcal I$，则 $a_0=0$，并准确有
$$
\boxed{
a=\frac{W_C}{e_C}\bmod x^{m-1}
 =W_t(Q)\,\frac{\tau}{e_C}\bmod x^{m-1}.
}
\tag{15}
$$
所以 (10) 剩下的标号就是同一个原 $W_t(Q)$。
它不是在不同点之间独立可选的变量；
与水平注中由同一个 $G_0'(t_Q)$ 控制的负水平标号一样，
均须回到全局 $\mathcal O$ 与原来源。

## 5. 保留的全局问题

结合水平注，完整有限矩阵现在可在所述移动平滑部分作如下真单位消元：
正水平全部消元；负水平保一个受同一 $G_0'$ 约束的核线；
非水平高分歧保 (15) 和两个末行；简单非水平点保其原单行。
所有运算均是当前目标特征 $p$ 的原矩阵运算，
未借辅助素数或任意环境列。

奇点、固定角、其余 conductor 分量没有满足 (1) 时仍逐项保留。
即使在所述平滑部分，末行的全局相容也没有自动得到。
之后仍须与同一个
$eK|_C+W|_C\in H^0(C,N^3(-TP))$、
第二个真实长前缀、$3\eta$ 镜轴及原第四短行联立。
这里 $T=s-r-13$，仍是完整物理长度。

本注只压缩完整原 $\mathcal O$ 的已识别厚点部分，
不证明受限 $W_T$ 的像，不证明指定 forcing 非零，
也不把来源商秩转换为原 $M$ 的新增 Smith 因子。
无新数学程序运行。
