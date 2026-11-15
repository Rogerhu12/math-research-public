# R238：完整 block 的次层双能量准确归为一个标量

日期：2026-11-15。完整纸面推导；没有执行新 profile 积分、符号目标或几何计算。

本稿接 [R235](R235-nonseparable-complete-third-order-circles-with-zero-exceptional-leading-energies.md) 与 [R237](R237-complete-next-mixed-layer-after-exceptional-leading-cancellation.md)，回答一个具体问题：原两根旋转与两个同构 block 是否还能自动消掉下一对必要能量？答案是其中一个相位自动消失，另一个恰为同一标量的同号倍数。因此必须支付一个新的标量等式；本稿不预设该标量的符号或非零性。

来源另包括 [R229 同锚边界身份](R229-p2-energy-boundary-identity-for-exceptional-germs.md)、[R231 领先双能量](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R233 四尺度圆](R233-four-scale-moment-circles-cancel-both-exceptional-leading-energies.md)。

## 1. 完整 block 与四个标量

固定正区间 $I=[\ell,r]$ 和同一个正右积分 J。沿用

$$
\mathcal G=-\frac12\Phi_{p_2},\qquad
\mathcal D=\Phi_{p_1}-\frac18\Phi_{t_1},\qquad
E(U,V)=\frac14\int_I(x^2U''V''+2U'V').
\tag{1}
$$

设一个完整 block 的三矩 pair $(f,g)$ 由互不交的微包组成，且每个微包内 $g=s_i f$，$s_i\in\{-1,1\}$。例如 R235 旋转前的完整八复制 block 满足此条件，且已支付全部四个第三 ruling 槽。

二次原式逐点给

$$
A=\mathcal G(f,f)=\mathcal G(g,g),\qquad
B=\mathcal D(f,f)=\mathcal D(g,g),
$$

$$
X=\mathcal G(f,g),\qquad Y=\mathcal D(f,g).
\tag{2}
$$

X、Y 因三矩交叉零而在两 collar 为零；A、B 一般保留实际左尾。定义

$$
P=E(A,X),\qquad Q=E(X,X)>0,
$$

$$
U=E(A,Y),\qquad V=E(X,Y),\qquad
t=-P/Q,\qquad Z=U+tV.
\tag{3}
$$

这里 Q 的正性及 $|t|<1$ 由 R233 的正 bulk 与两种符号均出现给出。R235 另选 block 保证 $t\ne0$。

## 2. 同一个旋转的四能量

取

$$
f_\alpha=\cos\alpha f+\sin\alpha g,\qquad
g_\alpha=-\sin\alpha f+\cos\alpha g.
$$

写 $s=\sin2\alpha$、$c=\cos2\alpha$。完整双线性展开给

$$
\mathcal G(f_\alpha,f_\alpha)=A+sX,\quad
\mathcal G(g_\alpha,g_\alpha)-\mathcal G(f_\alpha,f_\alpha)=-2sX,
\quad\mathcal G(f_\alpha,g_\alpha)=cX,
$$

$$
\mathcal D(g_\alpha,g_\alpha)-\mathcal D(f_\alpha,f_\alpha)=-2sY,
\qquad\mathcal D(f_\alpha,g_\alpha)=cY.
\tag{4}
$$

因而 R231 的两个领先量为

$$
L_c=-2s(P+sQ),\qquad L_s=c(P+sQ).
\tag{5}
$$

二者同时为零当且仅当 $s=t$：若 $c\ne0$，第二式直接给出；若 $c=0$，则 $s=\pm1$，第一式也给同一结论，而 $|t|<1$ 已排除此情形。

在这个已定旋转上，R237 的两个完整次层能量准确为

$$
\boxed{M_c=-2tZ,\qquad M_s=\cos2\alpha\,Z.}
\tag{6}
$$

因此对于单个完整 block，四个能量同时为零当且仅当

$$
\sin2\alpha=t,\qquad Z=0.
\tag{7}
$$

式 (7) 不声称 Z 已知非零；它说明在领先旋转选好后，不能再将该角当成一个自由参数支付第二个标量。

## 3. 真尾与微包 bulk：不能混同的两个层次

对右 collar 为零且左尾至少在本稿形式中的 U、V，R229 的真实边界式为

$$
E(U,V)=\frac14\int_Ix^4(U/x)''(V/x)''
+\frac12\left[x^3(U/x)'(V/x)'+x(U/x)(V/x)\right]_{\ell}^{r}.
\tag{8}
$$

对一个紧支撑实微包 u，记

$$
S(u)=\frac14\int_Ix^4\left((\mathcal G(u,u)/x)''\right)^2>0,
$$

$$
\mathfrak T(u)=\frac14\int_Ix^4
(\mathcal G(u,u)/x)''(\mathcal D(u,u)/x)''.
\tag{9}
$$

它们是局部 bulk。一般并不分别等于
$E(\mathcal G(u,u),\mathcal G(u,u))$ 和
$E(\mathcal G(u,u),\mathcal D(u,u))$。

具体地，左 collar 中 $\mathcal G(u,u)$ 是 $c x^2$；而由原八矩式，

$$
\mathcal D(u,u)
=-\frac{x^2}{4}\int_I\xi(u''(\xi))^2\,d\xi
-\frac{x}{8}\int_I\left(\xi^2(u'')^2+2(u')^2\right)\,d\xi.
\tag{10}
$$

所以两者除以 x 后都是仿射尾，其二阶导数只支撑在该微包内。这使不同微包的 bulk 交叉为零，但没有自行消掉 (8) 的总体边界项。

现在写

$$
f=\sum_i a_i u_i,\qquad g=\sum_i s_i a_i u_i,
\qquad s_i=\pm1,
\tag{11}
$$

各 $u_i$ 支撑不交。对完整三矩 block，X、Y 都紧，故 (3) 的四个能量在 (8) 中的**总体**边界项为零。于是准确得到

$$
\boxed{
\begin{aligned}
P&=\sum_i s_i a_i^4S(u_i),&
Q&=\sum_i a_i^4S(u_i),\\
U&=\sum_i s_i a_i^4\mathfrak T(u_i),&
V&=\sum_i a_i^4\mathfrak T(u_i).
\end{aligned}}
\tag{12}
$$

这是先保全总体边界、再利用紧性得出的公式。不能把每个单微包原能量直接替成其 bulk，并把未支付的边界项逐包丢掉。

令 $q_i=a_i^4S(u_i)>0$、$r_i=\mathfrak T(u_i)/S(u_i)$。则

$$
Z=Q\left[
\frac{\sum_iq_is_ir_i}{Q}
-\frac{\sum_iq_is_i}{Q}\frac{\sum_iq_ir_i}{Q}
\right].
\tag{13}
$$

因此 Z 是符号 $s_i$ 与局部比值 $r_i$ 的准确加权协方差。领先旋转只支付符号的加权平均；没有从该平均自动推出 (13) 为零。

## 4. 新 bulk 的完全局部式与平移次数

令

$$
W=x^2u''-2xu'+2u.
$$

由 R229 的 $R=(u/x)''$ 及 $3R+xR'=u'''$，

$$
(\mathcal G(u,u)/x)''=-\frac{xW u'''}4.
\tag{14}
$$

R237 的 $\mathcal D$ 原式直接求两导数，得到

$$
\boxed{
(\mathcal D(u,u)/x)''
=\frac14(3x^2u''-5xu'+4u)u'''
-\frac{W^2}{4x^3}.
}
\tag{15}
$$

例如置 $u=xy$、$r=y''$、$m=y-xy'$，左边先化成
$2x^3r^2+3x^4rr'/4-3xmr/4-x^2mr'/4$；再用
$3r+xr'=u'''$ 即得 (15)。这不使用新的 profile 求积。

把 (14)、(15) 代入 (9)，第一项 $x^2W^3u'''$ 是
$W^3W'=(W^4)'/4$，因紧支撑其完整边界为零。于是

$$
\boxed{
\mathfrak T(u)=-\frac1{64}\int_I
x^5W(3x^2u''-5xu'+4u)(u''')^2.
}
\tag{16}
$$

式 (16) 不是一个已经证得固定符号的平方积分。两个括号一般不能同号推定，本稿不由它宣称 $\mathfrak T$ 正、负或非零。

对平移 $u_d(x)=u(x-d)$，换回固定原变量后 (16) 是 d 的次数至多九的多项式。R235 的 S 同理是次数至多十的多项式。它们只在实际允许的正坐标放置上解释为原能量；在重叠或非法位置的多项式值仅可用于证明多项式非恒零，不能冒那里的跨包正交。

## 5. 正伸缩的准确次数

对正 H，定义 $u_H(Hx)=u(x)$。同一原算子逐项给

$$
\mathcal G(u_H,v_H)(Hx)=H\mathcal G(u,v)(x),
\qquad
\mathcal D(u_H,v_H)(Hx)=\mathcal D(u,v)(x).
\tag{17}
$$

因此

$$
S(u_H)=H S(u),\qquad \mathfrak T(u_H)=\mathfrak T(u),
\tag{18}
$$

而完整 block 的四个标量变成

$$
(P,Q,U,V)\longmapsto(HP,HQ,U,V).
\tag{19}
$$

所以 t 和 Z 均不随该正伸缩改变。共同 profile 幅度 a 则使四个标量同乘 $a^4$，零条件不变。

一个便于核对的特例是尚未做八复制的四尺度基本 pair：
$u_i(x)=\psi(x/a_i)$、$w_i=|v_i|a_i^3$、微包幅度为 $\sqrt{w_i}$。
记 $S_*=S(\psi)$、$T_*=\mathfrak T(\psi)$，则

$$
P=S_*\sum_i s_iv_i^2a_i^7,\quad Q=S_*\sum_iv_i^2a_i^7,
$$

$$
U=T_*\sum_i s_iv_i^2a_i^6,\quad V=T_*\sum_iv_i^2a_i^6.
\tag{20}
$$

这些等式给出准确的尺度依赖，但不允许把 (20) 原样用于平移后的八复制 block；后者必须用 (12) 中真实平移后的 S 与 $\mathfrak T$。

## 6. R235 两个同构完整 block 的结论

R235 取两个相互不交、正伸缩同构的完整 block。第一个旋转角为 $\alpha$，第二个为 $\beta=\pi/2-\alpha$，故

$$
\sin2\beta=\sin2\alpha=t,\qquad
\cos2\beta=-\cos2\alpha.
$$

每个 block 本身均为三矩圆且已支付全部第三阶。它们的四个能量也按完整 block 准确相加：右方 block 的 $A_f$ 在左方为 $cx^2$，而另一能量槽是紧的 $\mathcal D$ 差或交叉像，所以 $E(x^2,Z)=0$；所有其他交叉同样为零。

若两 block 另乘实非零幅度 $a_1,a_2$，合成后的 R237 两量为

$$
\boxed{
M_c^{\rm total}=-2tZ(a_1^4+a_2^4),\qquad
M_s^{\rm total}=\cos2\alpha\,Z(a_1^4-a_2^4).
}
\tag{21}
$$

等幅时恰为

$$
\boxed{M_c^{\rm total}=-4tZ,\qquad M_s^{\rm total}=0.}
\tag{22}
$$

R235 已保证 $t\ne0$，且 $a_1^4+a_2^4>0$。所以同一两个旋转根、正伸缩和任意实非零幅度，不能另外改变 $M_c$ 的零性。合成圆要同时通过这两个新门，准确等价于原完整 block 的 $Z=0$。

这不排除重新选择基本节点、微包形状、非同构 blocks 或更多完整 blocks 后支付 Z。也不声称原已选 R235 实例必有 $Z\ne0$。

## 7. 下一建设性问题

本稿把下一问题缩为一条有明确来源的标量方程，而不是继续增加不受约束的相位数。可在保留三矩和完整八复制第三阶消去的参数族中直接研究

$$
UQ-PV=0,\qquad P\ne0,\qquad Q>0.
\tag{23}
$$

若找到这样的完整 block，R235 的两互补角与同构放置会同时支付 $L_c,L_s,M_c,M_s$，且四条 projective 方向仍排除任何常数 GL(2) 分离。这个条件构造仍只涉及已知两层；不能据它称第四完整 ruling 或 period 已解。

本文所有等式保留同一个右锚与真实左尾。没有新的求积、NF、响应秩、采样或实际路径计算。
