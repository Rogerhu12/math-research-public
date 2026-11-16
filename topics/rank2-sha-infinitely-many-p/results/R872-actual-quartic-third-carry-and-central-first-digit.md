# R872 — 实际 quartic 第三 carry 与中央第一高位

日期：2026-11-16。**状态：下列原十三行带中的真实单位响应、同一修正的第三页标量及其与原四中央第二位的联合式已证明。尚未证明该联合式在原全部修正空间中不可解。**

本篇接 [R868](R868-original-t-slack-and-native-bockstein-image-unit.md) 的低松弛边界、[R871](R871-original-sigma-thirteen-unit-and-low-hurwitz-readers.md) 的完整来源规范，以及 R828 的[一标量四位系统](../notes/2026-11-16-r828-actual-one-scalar-four-digit-and-same-correction-pages.md)和[三条 carry 递推](../notes/2026-11-16-r828-three-native-carry-recursions-and-last-block-tails.md)。本篇不再改变 Gaussian 或目标单位。

关键是固定同一个已经通过原 $p^3$ 的
$X=P+pR+p^2S$。实际高轴第一高位不是自由参数；四中央把它识别成同一个完整中央向量的第二位。本篇在原第三带内算出它的真实单位系数，保 $P,R,S$ 的全部其它行。

## 1. 同一来源、完整矩阵和准确窗口

保持共同 $E_1$、Hasse 对齐后的 $a=a_*=-34\mathcal C_p$、
$p=6s-1>211$，并删除 R821 的固定 Jacobian 坏集。原目标为
$$
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3),
\qquad1\le\ell<s-13.
\tag{1}
$$
所有向量仍在原 $\mathcal W_D$；$P_{134},c_*U_0$、公共 charge 四十、
全部十九角及三条十三行带不变。

沿 R828 一标量系统，固定实际参考 $g_{\Theta,\circ}$、完整 $B(w)$ 和
$$
h_0=-a/18,\qquad H_p-h_0\in p\mathcal O,\qquad b_0=B(0)\in\mathcal O^\times.
$$
同一参考上的计算族为
$$
M(H)=M_0+pH A_1+p^2H^2A_2+
p^3(H^3A_3+H^4A_4)\pmod{p^4}.
\tag{2}
$$
其中 $M(H_p)$ 才是原实际矩阵。其它 $H$ 仅是同一完整整展开的计算参考，不获得新的算术来源。

对任意原向量 $Y$，记原总 charge 读取为 $W_i(Y)$，则
$$
M_0(Y)=w^{13}\sum_{i=0}^3\frac{a^i\epsilon^i}{i!}W_i(Y),
$$
$$
\begin{aligned}
A_1(Y)&=\epsilon w^9B
 \left(W_1(Y)+a\epsilon W_2(Y)+\frac{a^2\epsilon^2}{2}W_3(Y)\right),\\
A_2(Y)&=\frac{\epsilon^2w^5B^2}{2}
                  \left(W_2(Y)+a\epsilon W_3(Y)\right).
\end{aligned}
\tag{3}
$$
$A_3,A_4$ 仍按原全式保留；特别不以 $\epsilon^4=0$ 删除末端四次 carry。

假设真正存在原首核候选
$$
\bar P=t^rF^4q\in\ker\bar M,\qquad
F(t(w),\bar g(w))=w^hu(w),
\tag{4}
$$
其中 $\bar g$ 是完整实际 $g$，$u(0)$、
$e_0=(Y\partial_YF)(0,1)$、$q(0,1)$ 是单位，$h\ge1$。
这里仅要求 (4) 的实际原格成员性，不从四中央零构造它。

置
$$
\boxed{\tau=r+2h-s\in\{1,2,3\},\qquad
\tau<\ell\le r+h-4,\qquad h<s-4.}
\tag{5}
$$
实际 carry 指数为 $k_{\rm carry}=13+\tau$。因 $\tau<\ell$，
物理行 $\epsilon^3w^{13+\tau}$ 确在原第四块内。

R868 的最小零角情形
$$
r=3,\quad\deg_YF(0,Y)=3,\quad\deg_Yq(0,Y)\le2
\tag{6}
$$
有准确 $\sigma_t(\bar P)=0$，因此本篇确实覆盖不能使用
$t^{-\tau}\bar P$ 的原低松弛范围。在 (6) 中，(5) 的短窗是
$\tau<\ell\le h-1$。本篇定理本身只需 (4)–(5)。

由于 $g_{\Theta,\circ}-g$ 从 $w^{s-4}$ 起，$h<s-4$ 保证
$F(t,g_{\Theta,\circ})$ 仍首阶 $h$，首单位仍是 $u(0)$。
令
$$
C_0=c_*U_0^\circ(0)
 \left(\frac{t(w)}w\right)_{w=0}^{r}q(0,1)\in k^\times .
\tag{7}
$$
公共 $U_0^\circ$ 包括原全部固定来源因子，未被归一成一。
总 charge 四十只影响下面较高的 $F$ 次项，故准确有
$$
\operatorname{ord}_w\bar W_i(P)\ge r+(4-i)h\quad(0\le i\le3),
$$
$$
\boxed{[w^{s+\tau}]\bar W_2(P)=
12C_0u(0)^2e_0^2.}
\tag{8}
$$
证明是
$(\mathcal E+40)^2(t^rF^4q)=12t^rF^2(\mathcal EF)^2q+O(F^3)$；
$h\ge1$ 使后项不进入显示的首系数。

## 2. 同一个 p³ 提升下的计算参考

固定原整 $P,R,S$，并假设
$$
\boxed{X=P+pR+p^2S,\qquad M(H_p)X\in p^3\Gamma.}
\tag{9}
$$
所有 normal、三条十三行、末短块均包含在 (9) 中。
以下不允许分别换 $R$ 或 $S$。

由 (5)、(8)，(3) 的前两个分量达到 $w^s$，在模 $p$ 的目标中为零；
末分量的阶至少 $9+r+h\ge\ell+13$。因此
$$
\boxed{\bar A_1(P)=0,\qquad A_1(X)\in p\Gamma.}
\tag{10}
$$
令
$$
\eta=\frac{H_p-h_0}{p}\in\mathcal O.
$$
由完整 (2) 展开，
$$
\boxed{
M(H_p)X-M(h_0)X
=p^2\eta A_1(X)+2p^3h_0\eta A_2(P)
\pmod{p^4}.
}
\tag{11}
$$
$A_3,A_4$ 的变化在 $p^4$，并非把这两个算子本身从原矩阵删除。
(10)–(11) 支付
$$
M(h_0)X\in p^3\Gamma.
\tag{12}
$$
更一般，$H=h_0+p\eta'$ 的计算族均保这个同 $X$ 的 $p^3$ 性；
第三页的整向量差为
$$
\bar\eta'\left(A_1(X)/p+2h_0A_2(P)\right)\pmod p.
\tag{13}
$$
本篇仅在指定原带行上计算 (13)，并不删其余高尾。

同理，(9) 与 (10) 给
$$
M_0(X)\in p^2\Gamma.
\tag{14}
$$
这一步使用 (2) 中 $A_1$ 前的那个真实 $p$，不是由
$\bar A_1(P)=0$ 直接断言更高整性。

## 3. 两次实际折回给 −6a，而非 −18a

取原第三带内的整行
$$
\boxed{L_\tau=[\epsilon^3w^{\tau+9}],\qquad \tau+9\in\{10,11,12\}.}
\tag{15}
$$
它杀全部 $\bar M$ 的像，因为所有原列的模 $p$ 输出都带完整
$w^{13}$。原最后 $p^3T$ 因而不能改变
$L_\tau M(X)/p^3\bmod p$。

先从真实存在的行
$\epsilon^3w^{13+j}$，$0\le j\le\tau<\ell$，读取 (14)。
完整 $w^s=p\epsilon$ 给
$$
\frac{a^3}{6}[w^j]W_3(X)
+\frac{pa^2}{2}[w^{s+j}]W_2(X)\in p^2\mathcal O.
$$
更高两次、三次折回均已在 $p^2$ 内。因此
$$
\boxed{
[w^j]\,\frac{W_3(X)}p
=-\frac3a[w^{s+j}]\bar W_2(P)\pmod p
\quad(0\le j\le\tau).
}
\tag{16}
$$
这里 $W_3(X)/p$ 只在显示的低前缀读取；它在该前缀的整性已由 (8)、
$X\equiv P\bmod p$ 支付，不把整个 $W_3(X)$ 当作可除 $p$。

式 (8) 还使 (16) 在 $j<\tau$ 时为零。故
$$
\boxed{
[w^\tau]\,\frac{BW_3(X)}p
=-\frac3a b_0[w^{s+\tau}]\bar W_2(P)\pmod p .
}
\tag{17}
$$

现在必须对 (3) 的三个分量全部折回：
$$
\boxed{
L_\tau A_1(X)=
p^2[w^{2s+\tau}]BW_1(X)
+ap[w^{s+\tau}]BW_2(X)
+\frac{a^2}{2}[w^\tau]BW_3(X).
}
\tag{18}
$$
除以 $p$ 后，第一项模 $p$ 为零；第二项不能省掉。
用 (17)，得到
$$
\begin{aligned}
L_\tau(A_1(X)/p)
&=\left(a-\frac{3a}{2}\right)b_0
 [w^{s+\tau}]\bar W_2(P)\\
&=\boxed{-6ab_0C_0u(0)^2e_0^2}\pmod p.
\end{aligned}
\tag{19}
$$
若只读 (18) 最后一项，就会误得 $-18a$；
从第二块折回的 $+12a$ 是同一原矩阵不可删除的贡献。

对于 (13) 的另一项，准确有
$$
L_\tau A_2(P)=
\frac p2[w^{s+\tau+4}]B^2W_2(P)
+\frac a2[w^{\tau+4}]B^2W_3(P).
\tag{20}
$$
第一项模 $p$ 为零；第二项由
$r+h\ge\ell+4\ge\tau+5$ 为零。因此 (13) 在这条行上的实际响应是
$$
\boxed{
\upsilon_\tau=-6ab_0C_0u(0)^2e_0^2\in k^\times.
}
\tag{21}
$$
式 (20) 仅支付指定低行，不声称 $A_2(P)$ 的全部高尾为零。

## 4. 与四个原中央第二位的真实联合式

定义同一提升的计算参考标量
$$
\boxed{
\mathcal B_\tau(P,R,S;h_0)
=\frac{L_\tau M(h_0)(P+pR+p^2S)}{p^3}\pmod p.
}
\tag{22}
$$
其整性是 (12)，并非单独选择三个分块商。
由 (11)、(21)，若同一个 $P,R,S$ 可进一步以原 $T$ 提升到 $p^4$，则必须
$$
\boxed{
\mathcal B_\tau(P,R,S;h_0)
-6ab_0C_0u(0)^2e_0^2\,\bar\eta=0 .
}
\tag{23}
$$
$T$ 在 (15) 的原 carry 行不起作用；其它行仍须由同一 $T$ 解决。

这里的 $\eta$ 是实际标量。R865 的完整有限乘积给
$$
\bar\eta=h_0\bar L_1,\qquad
L_1=\sum_{j=1}^{s-1}
 \left(\frac1{6j}-\frac1{6j+3}\right)
+\sum_{j=1}^{s}\frac1{2j-1}.
\tag{24}
$$
故 (23) 也可写成
$$
\mathcal B_\tau+
\frac{a^2b_0}{3}C_0u(0)^2e_0^2\,\bar L_1=0.
\tag{25}
$$
没有证明 $L_1$ 非零，也没有以某个固定底数的 Fermat 商非零替代它。

原四中央给另一个更直接的同源表达。沿 R828 记
$\mathfrak F(H)\in\mathcal O^4$ 为四个完整四权中央多项式，
使用同一 $g_{\Theta,\circ},B,a$，而非四个独立自由参数。
令
$$
f=\mathfrak F(h_0),\qquad
\eta_0=e_0^tB_4^{-1}.
\tag{26}
$$
这里 $e_0^t$ 指固定首标准行，不是 (4) 的 quartic 导数标量；
$B_4$ 正是 R821(24)–(25) 的固定矩阵，行次序 $S,T,U,V$，
列次序 $(A_{\nu,4},A_{\nu,3},A_{\nu,2},A_{\nu,1})$。
由其原归一化，
$$
\eta_0\mathfrak F'(h_0)\equiv b_0\pmod p.
$$
四原完整中央同时零，必要地给 $f\in p\mathcal O^4$，以及
$$
\bar\eta=-\frac{\eta_0f}{p\,b_0}\pmod p.
\tag{27}
$$
因此 (23) 化成具体联合行
$$
\boxed{
\mathcal B_\tau(P,R,S;h_0)
+6aC_0u(0)^2e_0^2\,
             \frac{\eta_0\mathfrak F(h_0)}p
=0\pmod p.
}
\tag{28}
$$
第二项是四原中央的**同一个完整第二位组合**，
不是四个裸首系数的任意替代。其余三个中央第二位、第三／第四位和全部
$H^{-hp}$／高 $B$ 项照原式保留。
式 (28) 只对同一 (9) 作必要检验，不把某个 $R,S$ 依中央分别另选。

## 5. (22) 保留的同源高尾及真实可调范围

为明确 (22) 没有丢掉原高尾，令 $m=\tau+9$，
$\mathcal K^0_{j,d}$ 是 R828 三 carry 公式在 $H=h_0$ 的值。
则
$$
\begin{aligned}
\mathcal K^0_{3,1}(Y)_m
&=\frac{a^2}{2}\left(
 [w^{s+\tau-4}]W_2(Y)+h_0[w^\tau]BW_3(Y)\right),\\
\mathcal K^0_{3,2}(Y)_m
&=a\left(
 [w^{2s+\tau-4}]W_1(Y)+h_0[w^{s+\tau}]BW_2(Y)
 +\frac{h_0^2}{2}[w^{\tau+4}]B^2W_3(Y)\right),\\
\mathcal K^0_{3,3}(Y)_m
&=[w^{3s+\tau-4}]W_0(Y)+h_0[w^{2s+\tau}]BW_1(Y)\\
&\quad+\frac{h_0^2}{2}[w^{s+\tau+4}]B^2W_2(Y)
 +\frac{h_0^3}{6}[w^{\tau+8}]B^3W_3(Y).
\end{aligned}
\tag{29}
$$
所有乘积先在实际原级数中计算，再取指定系数。
在本行 $m\le12<s-3$，原 $A_4$ 的最低 $w$ 阶为 $s-3$，
因此它对这一行严格为零；此结论不删除它在其它原行的贡献。
准确有
$$
\boxed{
\begin{aligned}
\mathcal B_\tau={}&
\frac{\mathcal K^0_{3,1}(P)_m+
 p(\mathcal K^0_{3,1}(R)_m+\mathcal K^0_{3,2}(P)_m)}{p^2}\\
&+\mathcal K^0_{3,1}(S)_m
 +\mathcal K^0_{3,2}(R)_m+\mathcal K^0_{3,3}(P)_m
 \pmod p.
\end{aligned}}
\tag{30}
$$
只有显示的合并分子由 (12) 保证被 $p^2$ 整除；
不能分别给其中几项预先除 $p$。
式 (29) 保原全部 regular 高尾，而非只保 $B_{<4}$。

还可以准确定位一个仍未付的调整方向。保持 $P,R$ 固定，
若 $\bar Y\in K_1=\ker\bar M$，则 $S\mapsto S+Y$ 保持完整 $p^3$ 提升。
但 (22) 改变
$$
\mathcal K^0_{3,1}(Y)_m
=\boxed{\frac{a^2}{2}[w^{s+\tau-4}]\bar W_2(Y)}.
\tag{31}
$$
这里 $\bar W_3(Y)\in w^\ell k[[w]]$，而 $\tau<\ell$，
所以 (29) 的 $h_0$ 项确实消失。
同一变化也在整个第三页沿实际 $\beta_1(\bar Y)$ 移动，
绝非只改变这一标量。

于是能否用固定 $P,R$ 下的 $S$ 调整 (28)，准确取决于原有限泛函
$$
\boxed{
K_1\longrightarrow k,\qquad
\bar Y\longmapsto[w^{s+\tau-4}]\bar W_2(Y)
}
\tag{32}
$$
是否非零。它读取原第二长块的最后三条真实尾之一。
不能由一般首核已有 $W_2\in w^{s-13}$ 就把它删掉；
也不能从某个纯 quartic 子格在此为零推它杀全部 $K_1$。

即使 (32) 非零，逐标量可调仍不保证全第三页可解；
若 (32) 为零，改变更早的同源修正 $R$ 及其补偿 $S$ 仍须整体考察。
本篇不把单位 (21)、实际 $L_1$，或新形式的联合行当作主目标非零。

本篇是完整符号证明，无新增数学数值执行。