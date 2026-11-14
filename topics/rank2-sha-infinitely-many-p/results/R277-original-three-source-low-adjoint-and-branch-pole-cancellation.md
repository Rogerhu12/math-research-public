# R277 — 原普通首权的低截断伴随、三方向首 forcing 与实际三源消分歧极

日期：2026-11-13。**状态：以下原首权的完整分部积分、模 $p^2$ 下一位重聚合、具体 $A+B$ 的固定角原函数、三方向 forcing 的 primitive 低 jet，以及一条合法三原源组合消去 $v=1$ 的 $1/\sqrt{1-v}$ 极均已证明。没有把这个局部消极当作完整中央非零。**

本篇按 R274 已付的低次数精度工作，不使用 R275 特征零 exact adjoint 的不解性来排除截断恒等式。
固定对象是 R270 的三条**原来源**
$S_A=A_{17}(2z)/16,S_B=A_{34},S_H=A_{136}$，
共同 charge 为 $68$。

## 1. 实际首权密度中的 $p$ 项

沿用
$$
t=\sqrt{1-v},\quad
F(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+1)}v^n,\quad
\mathfrak H(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+3)}v^n,
$$
$$
Y(v)=\Theta(v)^{68},\qquad
a_A=Q_A/t,\quad a_B=Q_B/t,\quad a_H=Q_H.
\tag{1}
$$
准确有
$$
4vF'+F=1/t,\qquad
\frac{Y'}Y=\frac{17\mathfrak H}{t}.
\tag{2}
$$
取普通 $p=4r+1$。原首权正是
$$
b_i=[z^{p-1}]S_i
=[v^r]YF^{-p}a_i.
\tag{3}
$$

令 $\mathcal Z_i$ 为**实际角原函数**
$$
\mathcal Z_i'=a_i,\qquad \mathcal Z_i(0)=0.
\tag{4}
$$
它们是固定代数函数，首项均为 $v^2/2$；不是对完整 Mellin 取原函数。
定义
$$
\boxed{
C_i=\mathcal Z_i\left(\frac{3}{4v}-\frac{17\mathfrak H}{t}\right),
\qquad
N_i=\frac{\mathcal Z_i}{4vtF}.
}
\tag{5}
$$

**定理 1。** 同一个原首权满足准确恒等式
$$
\boxed{
b_i=[v^r]YF^{-p}(C_i+pN_i),\qquad i=A,B,H.
}
\tag{6}
$$

**证明。** 写 $M=YF^{-p}v^{-r-1}$。由 (2) 及 $r=(p-1)/4$，
$$
-\frac{M'}M
=-\frac{17\mathfrak H}{t}
 +p\frac{F'}F+\frac{r+1}{v}
=-\frac{17\mathfrak H}{t}+\frac{3}{4v}+\frac{p}{4vtF}.
\tag{7}
$$
这里 $p/(4v)$ 与首权的 $r/v$ 准确相消，但最后的 $p/(4vtF)$ **没有**消失。
对 $\operatorname{Res}_0M\mathcal Z_i'\,dv$ 作形式 Laurent 分部积分即得 (6)。
所有运算只在原点进行，不在十七挠点处求 theta 分数指数。$\square$

(6) 是原完整系数中的伴随恒等式。
把 $pN_i$ 省去，会直接改掉首权除以 $p$ 后的目标下一位。

## 2. 低截断下一位必须重组回同一原 log 行

以下取 $p\ge41$，使本文固定角原函数的全部分母为单位。
设
$$
W_i=Ya_i,\qquad w_{i,r}=[v^r]W_i,\qquad
A_i=[v^{r+1}]Y\mathcal Z_i.
$$
$C_i,N_i$ 均从 $v$ 起，故原目标只用 $F,\log F$ 到次数 $r-1$；
这一段整。由 $F^{-p}\equiv1-p\log F\bmod p^2$，
$$
b_i\equiv [v^r]YC_i+
p[v^r]Y(N_i-C_i\log F)\pmod{p^2}.
\tag{8}
$$

下面两条是精确的有理系数恒等式：
$$
\boxed{
[v^r]YC_i=w_{i,r}-\frac p4 A_i,
}
\tag{9}
$$
$$
\boxed{
[v^r]Y(N_i-C_i\log F)
=-[v^r]W_i\log F+\frac14A_i
 +\frac p4[v^{r+1}]Y\mathcal Z_i\log F.
}
\tag{10}
$$
证明 (9) 只需比较 $(Y\mathcal Z_i)'$ 的第 $r$ 项。
对 $(Y\mathcal Z_i\log F)'$ 作同样比较，并使用
$$
\frac1{4vtF}-\frac{F'}F=\frac1{4v},
$$
便得 (10)。

原中心质量零给 $w_{i,r}\in p\mathcal O$。
故 (8)–(10) 准确恢复
$$
\boxed{
\frac{b_i}{p}\equiv
\frac{w_{i,r}}p-[v^r]W_i\log F\pmod p.
}
\tag{11}
$$
这里 $A_i/4$ 两项确实相消。新伴随没有消除原 moving log；
它把原 log 行分成了可以逐项核实的原点下一位和 forcing。

原完整中央导数零因而给合法条件
$$
\boxed{
\frac{[v^r]YC_i}{p}
+[v^r]Y(N_i-C_i\log F)=0\pmod p,
}
\tag{12}
$$
而不是 $[v^r]YN_i=0$，也不是分别把 (8) 的两项置零。
更深精度仍须使用 R270 的前三权聚合和其 tame $-4$ carry。

## 3. $A+B$ 的真正角原函数与固定边界

先给该合法原线性组合的完整多项式：
$$
\begin{aligned}
Q_+(v):=Q_A+Q_B
={}&\frac25v(v-1)(v+1)(v^2-2v+5)(5v^2-2v+1)P_8(v),\\
P_8(v)={}&11v^8-132v^7+960v^6-1540v^5+1438v^4\\
&\hspace{8mm}-236v^3-232v^2-12v-1.
\end{aligned}
\tag{13}
$$
它准确为十五次，首项 $2v$。
这里的 $P_8$ 仅为本式八次多项式，不是 R264 的水平核多项式。

对任意多项式 $Q(v)=\sum_{n=0}^dq_nv^n$，
唯一多项式 $B_Q$ 满足
$$
(1-v)B_Q'-\tfrac12B_Q=Q.
\tag{14}
$$
写 $B_Q=\sum b_nv^n$，它的全部系数由
$$
b_{d+1}=0,\qquad
b_n=\frac{(n+1)b_{n+1}-q_n}{n+1/2}
\quad(n=d,d-1,\ldots,0)
\tag{15}
$$
给出。于是
$$
\int_0^v Q(s)(1-s)^{-1/2}\,ds
=tB_Q(v)-B_Q(0).
\tag{16}
$$
本篇只需次数十六以内，所以分母素数至多三十一。

令 $B_A=B_{Q_A},B_B=B_{Q_B},B_+=B_A+B_B$。
精确值为
$$
\begin{aligned}
B_A(0)&=-\frac{1248227362551868}{22563055139625},\\
B_B(0)&=\frac{727339049799116}{7521018379875},\\
B_+(0)&=\frac{186757957369096}{4512611027925}.
\end{aligned}
\tag{17}
$$
三者在 $v=1$ 都为零，因为对应 $Q(1)=0$ 和 (14)。
因而
$$
\boxed{
\mathcal Z_+=tB_+(v)-B_+(0),\qquad
\mathcal Z_+(1)=-B_+(0)\ne0.
}
\tag{18}
$$
所以 $A+B$ 虽在 R275 的真 $\beta$ 部分式中消去了常商，
在本篇的实际 forcing 中仍有
$-B_+(0)/(4vtF)$ 的分歧项。两种边界不能混同。

第三条的角原函数是普通多项式
$$
\mathcal Z_H(v)=\int_0^vQ_H(s)\,ds\in\mathbb Q[v]_{\le17},
$$
且
$$
\boxed{
\mathcal Z_H(1)=\frac{3410630213}{44924880},\qquad
Q_H(1)=\frac{32768}{55}.
}
\tag{19}
$$
全部 $B_A,B_B,B_+,\mathcal Z_H$ 系数已在本篇精确证书中逐项列出。

## 4. 一条合法三原源组合消去真正的分歧极

定义固定有理数
$$
\boxed{
\kappa=
\frac{B_+(0)}{\mathcal Z_H(1)}
=\frac{32869400496960896}{60295968781641855}.
}
\tag{20}
$$
取真正的原线性组合
$$
S_*=S_A+S_B+\kappa S_H.
\tag{21}
$$
若三原完整中央导数为零，则 $S_*$ 的完整中央导数为零；
这一步只有常数线性组合，没有引入来源乘法。

置
$$
R_H(v)=\frac{\mathcal Z_H(v)-\mathcal Z_H(1)}{v-1}
\in\mathbb Q[v]_{\le16},
$$
$$
\boxed{
K_*(v,t)=B_+(v)-\kappa tR_H(v).
}
\tag{22}
$$
由 $\kappa\mathcal Z_H(1)=B_+(0)$，准确有
$$
\boxed{
\mathcal Z_*:=\mathcal Z_A+\mathcal Z_B+\kappa\mathcal Z_H
=tK_*(v,t).
}
\tag{23}
$$
因此这一原组合的两项伴随变为
$$
\boxed{
C_*=K_*\left(\frac{3t}{4v}-17\mathfrak H\right),
\qquad
N_*=\frac{K_*}{4vF}.
}
\tag{24}
$$
**原来显式的 $1/t$ 因子全部被实际三源组合消去。**
这里仍保留原 $F$、$\mathfrak H$、$Y=\Theta^{68}$；
未把它们改成独立的有理来源。

在真实二次参数 $t$、$v=1-t^2$ 下，
$$
\boxed{
K_*=-\kappa\frac{32768}{55}\,t+O(t^2).
}
\tag{25}
$$
因为 $B_+(1)=0$，而 $R_H(1)=Q_H(1)$。
这给出了明确的固定非零首项；
除 (20) 及 $55$ 的固定分子分母素数外，它是单位。
(25) 只记录角分歧因子的消除；
不据此预设全局 $F$ 在任何 $p$-adic 延拓支上的值为单位。

原首权因而满足完全实际的公式
$$
\boxed{
[z^{p-1}]S_*
=[v^r]YF^{-p}K_*
 \left(\frac{3t}{4v}-17\mathfrak H+\frac p{4vF}\right).
}
\tag{26}
$$
这是可直接接到其他原 forcing 计算的候选：其角分歧极已经付清，theta 次数仍是 $68$。
它在 $\beta$ frame 的多项式部分仍含
$\kappa t\,\vartheta(\beta z)^4/(-55\beta^4)$，
所以并未同时消掉全部十七边界；也没有把该四次幂称为秩零 Mellin 单位。


### 4.1 原点与完整中央聚合仍逐项保留

在原点，(4)、(21) 给
$$
\mathcal Z_*=\frac{2+\kappa}{2}v^2+O(v^3),\qquad
K_*=\frac{2+\kappa}{2}v^2+O(v^3),
$$
$$
N_*=\frac{2+\kappa}{8}v+O(v^2),\qquad
C_*=\frac{3(2+\kappa)}8v+O(v^2).
\tag{26a}
$$
所以 (26) 仍使用原 $v^{-r-1}$ 权；没有给原测度增添原点原子，
也没有在消 $v=1$ 极时删掉 $v=0$ 的首项。

在完整普通 Mellin 中，准确有
$$
M_*=M_A+M_B+\kappa M_H,\qquad
q_*=\frac{M_*}{M_\vartheta}=q_A+q_B+\kappa q_H.
$$
$\kappa$ 是固定常数，故三条原完整中央零确实推出 $q_*'(0)=0$。
对 R270 的同一有限系数定义
$$
\widetilde q_{*,j}=\widetilde q_{A,j}+
 \widetilde q_{B,j}+\kappa\widetilde q_{H,j},
$$
$$
Z_{\mathrm{tame},*}
=\frac{[z^{p-5}]S_*}{24[z^{p-1}]\vartheta}\pmod p.
$$
在 $\kappa$ 整的允许素位，完整零准确强迫
$$
\boxed{
\begin{aligned}
\widetilde q_{*,1}&\in p^2\mathcal O,\\
4\widetilde q_{*,1}-\widetilde q_{*,2}&\in p^3\mathcal O,\\
3\widetilde q_{*,1}-\tfrac32\widetilde q_{*,2}
 +\tfrac13\widetilde q_{*,3}
 +68p^3b_0^{-4}Z_{\mathrm{tame},*}&\in p^4\mathcal O.
\end{aligned}}
\tag{26b}
$$
式 (24) 的角极消除没有删去 (26b) 的非中央修正，也没有把各正权独立置零。
若 $\kappa$ 的分母被某个固定素数整除，可先乘其固定分母写成原整常数组合；
本文的单位和 primitive 说法则照常排除该固定坏集。

## 5. 三条 forcing 的低 jet 确实是三个整方向

直接计算原 $a_i$ 的前三个系数：
$$
\bigl([v^j]a_i\bigr)_{\substack{i=A,B,H\\j=1,2,3}}
=
\begin{pmatrix}
1&211/10&2419/40\\
1&-9/10&14651/40\\
1&-567/55&5799/55
\end{pmatrix},
\qquad
\det=\frac{34463}{4}.
\tag{27}
$$
积分 (4)、除以 $4v$，再乘同一个常数一单位 $(tF)^{-1}$，
给真正的 $N_i$ 低 jet 矩阵
$$
\boxed{
\bigl([v^j]N_i\bigr)_{\substack{i=A,B,H\\j=1,2,3}}
=
\begin{pmatrix}
1/8&217/120&14463/3200\\
1/8&-1/40&219829/9600\\
1/8&-89/110&82933/13200
\end{pmatrix}.
}
\tag{28}
$$
其行列式是
$$
\boxed{
\det=\frac{34463}{6144}
=\frac{11\cdot13\cdot241}{2^{11}\cdot3}.
}
\tag{29}
$$
所以对 $p\ge41,\ p\ne241$，这些原 forcing 的低 jet 形成 primitive 的三维格。
乘共同 $YF^{-p}$ 的低次数单位不会改变此行列式。

这个结论是关于**已列出的原有限目标中的三个 forcing 方向**；
$1/F$ 仍在同一个目标单位中，不因此产生三个新的任意 theta 来源。
如需把它们返回 R266/R249 的原多项式来源，仍需相应的完整乘子与次数成本。

也不能从 (29) 推出三条指定中央系数中至少一个为单位。
完整中央零只给 (12) 的三个聚合数，未把 $C_i/p$ 与 $N_i$ 分开。
事实上，不存在非零常数组合使整个 $N$ 函数消失：
若 $\sum c_iN_i=0$，则 $\sum c_i\mathcal Z_i=0$，
微分给
$$
c_AQ_A+c_BQ_B+c_HtQ_H=0.
$$
二次扩张 $\mathbb Q(v,t)/\mathbb Q(v)$ 先迫 $c_H=0$；
$Q_A,Q_B$ 首项相同、最高项相反，故二者不成比例，再迫 $c_A=c_B=0$。
(21) 所作的是消去一个明确分歧极，而非消去整个 forcing。

## 6. 精确证书与继续使用的接口

[固定精确脚本](../scripts/check-original-three-ordinary-adjoint.py)
与 [全部有理／Gaussian 系数](../scripts/check-original-three-ordinary-adjoint.json)
给出本篇全部源多项式、角原函数、真实 $K_\beta^4$ 四层部分式、低 jet 矩阵、
$\kappa,R_H$ 和固定边界。运行结果为 **10 项 PASS**；
没有枚举或扫描目标素数。

后续需要比较的是同一个 (26) 与原完整 Newton 聚合，
或将其 $K_*$ 在保持原 $Y,F,\mathfrak H$ 的条件下运输到其他已付的连接。
当前已消掉的只有 (24) 中明确的角分歧极；
首权除以 $p$ 的真实下一位、R270 第三层 tame $-4$ 修正和全部 $\beta$ 边界仍在。

