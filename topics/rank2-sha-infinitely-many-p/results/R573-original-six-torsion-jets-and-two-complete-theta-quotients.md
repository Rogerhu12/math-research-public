# R573 — 原六挠全 jet、两负矩的同一局部行与两个完整 theta 商

日期：2026-11-14。**状态：已证明。**

沿 [R570](R570-original-global-negative-moment-cartier-lines-and-polynomial-primitives.md)
的同一 canonical 原函数，本篇把固定二、三挠点的取值关系扩大到整个
$E[6]$，并支付缺失 $\mu_6$ 型所强迫的完整 jet。
新增约束包括：

- 原负五行的常数项读 $a_1$，一次项准确读原负二行 $a_4$；
  若两者都为零，其二次项仍是显示的单位；
- $a_4=0$ 时两个不同的原 theta 来源均可除同一个固定
  $\sigma(6z)^2$ 因子，降到同一级，并有两个准确的单位质量；
- 所有有限相位保留为实际 $r(t)^6$，未将六挠点换成 $6p$ 挠点。

这些是两指定值同时消失必须满足的新完整约束。
它们尚未构成同时消失不可能的证明。

## 1. 来源、符号和原方程

先用基曲线
$$
E_0:y^2=x^3+1,\quad X=x^3,\quad
D x=2y,\quad D y=3x^2,\quad p=6s+1>19.
$$
$\pi=\psi_0(\mathfrak p)$、$V=\bar\pi$、
$\mathfrak h=\binom{3s}{s}\ne0$、
$r$、$q_4,q_1$ 均沿 R549/R565/R570，不改普通地点或有限角色。
特别
$$
\sigma(Vz)=r(z)\sigma(z)^p,\qquad
q_4=r^6x(V),\qquad q_1=-r^6x(V)y(V),
$$
$$
\mathcal R_4=D^{p-3}q_4=P_4(X),\qquad
\mathcal R_1=D^{p-6}q_1=P_1(X),\qquad
a_i=[X^p]P_i .
\tag{1}
$$
$a_4,a_1$ 分别是 R570 (3) 中原负二、负五单位矩乘准确单位后的模 $p$ 值。

保留全部原规范：
$$
\mathcal C(P_i(X)\omega_E)=0,\qquad \deg P_i\le p,
$$
$$
D^2\mathcal R_4=\mathfrak h q_4-\xi x^p,\qquad
D^5\mathcal R_1=\mathfrak h q_1+\xi(xy)^p.
\tag{2}
$$
这里 $\xi=r(0)$，$\xi^3=1$。
[R565](R565-original-paired-v-lame-and-nonzero-cartier-bilinear-row.md)
及 paired-V 检查点还给
$$
[X^{p-1}]P_4=\frac{\mathfrak h^5}{30},\qquad
[X^{p-1}]P_1=\frac{\mathfrak h^2}{720}.
\tag{3}
$$
本篇没有添加 Frobenius 多项式改变这些原函数。

## 2. 全 E[6] 的 canonical frame 确实整

对任意 $t\in E[6]\setminus\{O\}$，取 R570 的完整对称 lift
$$
\sigma_t(z)=e^{-\eta_t(z+t/2)}\sigma(z+t),\quad
c_t=\sigma_t(0),\quad g_t=D\log\sigma_t .
$$
这里 $c_t$ 与 $g_t(0)$ 的整性可以直接用原 division 函数支付，
不需要把准周期或 $p$ 挠点对数置零。

因为 $5t=-t+6t$，sigma 的完整周期律给
$$
\psi_5(t)=\epsilon_t c_t^{-24},\qquad \epsilon_t\in\{1,-1\}.
\tag{4}
$$
$\psi_5(t)$ 是单位：在良好约化下，非零六挠点不属于 $E[5]$。
另一方面 $\psi_6$ 在每个非零六挠点都是单零，
$$
\boxed{g_t(0)=-\frac{\psi_6''(t)}{72\,\psi_6'(t)}.}
\tag{5}
$$
此式来自
$D\log\psi_6(z)=6\zeta(6z)-36\zeta(z)$ 在 $t$ 处的常数项。
$p>19$ 时 $\psi_6'(t)$ 是单位，故 (5) 整。
由 $Dg_t=-x(z+t)$，本篇所需的所有低于 $p$ 阶导数都整。

所以 R570 的完整相位恒等式
$$
q_i(z+t)=
\frac{(T_{Vt}^{(6)}f_i)(Vz)}{\sigma_t(z)^{6p}},
\qquad f_4=x\sigma^6,\quad f_1=-xy\sigma^6
\tag{6}
$$
可以在此整个固定 $E[6]$ 上逐项约化。
只要 $m_i+j<p$，
$$
\boxed{
D^j\mathcal R_i(t)=c_t^{-6p}\mathfrak h^{m_i+j}
 (T_{Vt}^{(6)}f_i)^{(m_i+j)}(0),
\quad m_4=p-3,\ m_1=p-6.
}
\tag{7}
$$
分母的 $p$ 次幂被 $D$ 杀掉，是在上述整性支付后使用的。

这里不能以相同理由处理 $E[6p]$。
在 $\ker V$ 的实际分支上，paired-V 的非零 deck 常数
$D+6a_T$ 仍须保留；本篇未迭代到这些点。

## 3. 缺失型给全 jet；交叉 jet 精确读 a4

原完整空间 $\mathcal S_6$ 的型 $1$、型 $4$ 各一维，
分别为 $\langle f_1\rangle$、$\langle f_4\rangle$；
**型 $5$ 完全没有**。因此由 (7)
$$
\boxed{
D\mathcal R_4(t)=0,\qquad D^4\mathcal R_1(t)=0
\quad(t\in E[6]\setminus\{O\}).
}
\tag{8}
$$
这是无条件恒等式。

定义实际平移系数
$$
\Pi_iT_u^{(6)}f_i=c_u^6 d_{ii}(u)f_i,\qquad
\Pi_4T_u^{(6)}f_1=c_u^6 d_{41}(u)f_4 .
$$
(6) 的常数项及 R570 的原点最高系数给
$$
\boxed{
\begin{aligned}
\mathcal R_i(t)&=r(t)^6d_{ii}(Vt)a_i,\\
D^3\mathcal R_1(t)&=r(t)^6d_{41}(Vt)a_4.
\end{aligned}
}
\tag{9}
$$
没有把两条原负矩相等化，也没有丢掉实际 $r(t)^6$。

这些系数可完全显式地算。在 $u$ 处记
$x=x(u),y=y(u),g=g_u(0)$，则
$$
d_{11}=-5x^3-2b-6gxy,
$$
$$
d_{44}=-5x^3-2b-24gxy+72g^3y+54g^4x,
$$
$$
\begin{aligned}
d_{41}={}&-18x^3y-6by-(108x^4+72bx)g\\
&-216x^2yg^2-(180x^3+72b)g^3-54xyg^4 .
\end{aligned}
\tag{10}
$$
它们分别是 $Df_1/\sigma^6$、
$D^4f_4/(24\sigma^6)$、
$D^4f_1/(24\sigma^6)$ 的完整值。
特别 $g=0$ 时
$$
d_{41}=-6y(3x^3+b).
\tag{11}
$$

## 4. 原六挠除子和两个完整强制因子

暂把 $b$ 保为符号，定义
$$
Q_4(X)=X^4+220bX^3-1776b^2X^2-320b^3X-512b^4,
$$
$$
Q_5(X)=(X+4b)Q_4(X).
$$
原 division 多项式逐项递推给
$$
\boxed{\psi_6=6xy\,Q_5(X),\qquad
\psi_6^2=36x^2(X+b)Q_5(X)^2.}
\tag{12}
$$
$p>19$ 时 $Q_5$ 是五个互异的 $\mu_6$ 轨道的方程，
其根均不为 $0,-b$；这是 $[6]$ 可分及其挠点互异的直接结果。

于是 (8) 先给一个无条件的整多项式限制：
$$
\boxed{Q_5\mid P_4'.}
\tag{13}
$$
这里导数为 $d/dX$，在 $Q_5$ 的根上 $DX=6x^2y$ 是单位。

令
$$
D_7=X(X+b)Q_5,\qquad
D_{12}=X(X+b)Q_5^2=\frac{x\psi_6^2}{36}.
$$
由 (9)，有
$$
\boxed{a_1=0\ \Longrightarrow\ D_7\mid P_1.}
\tag{14}
$$
同样 $a_4=0$ 使 $P_4$ 在所有六挠点全零；
再用 (8) 的一阶零，得到
$$
\boxed{a_4=0\ \Longrightarrow\ D_{12}\mid P_4.}
\tag{15}
$$
在 $x=0$ 的两个分支，$X$ 的零阶为三；
在 $y=0$ 的三个分支，$X+b$ 的零阶为二。
这两处已经完整计入 (14)–(15)，未错误地把 $X$ 当成处处无分歧的参数。

另一个完整强制因子来自交叉 jet。
直接求导给
$$
D^3P(X)=y\,\mathscr L_3P(X),
$$
$$
\boxed{
\mathscr L_3P
=216X^2(X+b)P'''+108X(7X+4b)P''
 +48(7X+b)P'.
}
\tag{16}
$$
记 $A_1=\mathscr L_3P_1$。于是
$$
D^4P_1=3x^2\bigl(A_1+2(X+b)A_1'\bigr).
$$
若 $a_4=0$，(8)–(9) 在五个无分歧轨道上给
$Q_5^2\mid A_1$；在两个 $\delta$-挠点给 $X\mid A_1$；
在非零二挠点则由 $D^4P_1=0$ 给 $X+b\mid A_1$。
故
$$
\boxed{a_4=0\ \Longrightarrow\ D_{12}\mid\mathscr L_3P_1.}
\tag{17}
$$
(17) 不要求 $a_1=0$。

## 5. 两个实际 theta 商的级与单位质量

回到 $b=1$。若 $a_4=0$，写
$P_4=D_{12}Q$、$\mathscr L_3P_1=D_{12}R$。
(3)、(16) 给
$$
\deg Q=\deg R=p-13,\qquad
[X^{p-13}]Q=\frac{\mathfrak h^5}{30},\quad
[X^{p-13}]R=-\frac{\mathfrak h^2}{6}.
\tag{18}
$$
最后一个系数使用 $\mathscr L_3$ 在 $X^{p-1}$ 上的最高系数 $-120$；
最高的 $a_1X^p$ 被所有这些导数准确杀掉。

用原规范 $\sigma(6z)=-\psi_6(z)\sigma(z)^{36}$，整个全局来源商为
$$
\boxed{
\begin{aligned}
\frac{\sigma^{6p}\mathcal R_4}
     {f_4(z)\sigma(6z)^2}
 &=\frac1{36}\sigma^{6(p-13)}Q(X),\\
\frac{\sigma^{6p}D^3\mathcal R_1}
     {f_1(z)\sigma(6z)^2}
 &=-\frac1{36}\sigma^{6(p-13)}R(X).
\end{aligned}
}
\tag{19}
$$
它们都是整个
$\mathcal S_{6(p-13)}$ 的全纯 theta 截面，包含所有原物理周期。
不是只在原点做形式除法。

两者在 $O$ 的准确质量分别为
$$
\boxed{\frac{\mathfrak h^5}{1080},\qquad
       \frac{\mathfrak h^2}{216}.}
\tag{20}
$$
$p>19$ 时都是单位。
所以假设原负二行首层为零，确实强迫两个同级、单位质量的真实
约化来源出现；不能把其中一个商默认为零。

这些商的级随 $p$ 增长。本篇没有给它们固定特征零来源或有界测度，
因而不把 (19) 记作普通全部 jet 的改进。

## 6. 两个目标在同一个 delta 局部行中

现在取非零 $\delta$-挠点 $t$：$x(t)=0,y(t)^2=1$。
primary 规范使 $Vt=t$，且 R570 已付 $r(t)^6=1$、
$g_t(0)=0$。

在这里 (9)、(11) 及 (16) 分别给
$$
D^3\mathcal R_1(t)=-6y(t)a_4
=48y(t)P_1'(0).
$$
故
$$
\boxed{P_1'(0)=-a_4/8.}
\tag{21}
$$
这是真实的交叉行，不是把 $P_1$ 的最高系数偷换成 $a_4$。
常数项仍准确为 $P_1(0)=-2a_1$。

二阶原方程还给一个无条件单位：
在 $x=0$，$x(V)=N/r^2$ 的 $x$ 导数为 $\mathfrak h$，
所以 $N_x(0)=\mathfrak h\xi^2$。
比较 (2) 的 $x$ 一次系数得
$$
\boxed{P_4'(0)=\mathfrak h^2/24.}
\tag{22}
$$

再用原 $D^p=\mathfrak hD$，而非把超过 $p$ 阶的 sigma 导数直接约化：
$$
D^6\mathcal R_1(t)=D^pq_1(t)
=\mathfrak hDq_1(t)=-2\mathfrak h^2.
$$
以 $t$ 为原点的局部展开为
$$
x(t+z)=2y(t)z+2z^4+\cdots,\qquad
X(t+z)=8y(t)z^3+24z^6+\cdots.
$$
因此
$$
D^6P_1(X)(t)=17280P_1'(0)+23040P_1''(0),
$$
结合 (21)，得
$$
\boxed{P_1''(0)=\frac{3a_4}{32}-\frac{\mathfrak h^2}{11520}.}
\tag{23}
$$

于是当两个原指定负矩第一层同时为零时，
$$
P_1(0)=P_1'(0)=0,\qquad
P_1''(0)=-\mathfrak h^2/11520\ne0.
$$
完整固定因子进一步为
$$
\boxed{
a_4=a_1=0\ \Longrightarrow\
X^2(X+1)Q_5(X)\mid P_1(X).
}
\tag{24}
$$
$P_1$ 在 $X=0$ 恰二重，$P_4$ 在 $X=0$ 恰一重，
分别由 (23)、(22) 支付。
(24) 是 degree $8$ 的固定因子；(15) 仍是 degree $12$。

这与指定值同时为零并无逻辑矛盾：
下一项非零并不使前两项不能为零。
新的问题是 (14)–(24) 与原完整 (2)、canonical Cartier-zero
以及真实除子 $r,N$ 能否同时满足，未用极帽将其提前排除。

## 7. 原 b=17 的尺度及没有删除的边界

R570 (21) 保同一个 $V$ 给
$$
P_{i,b}(X)=b^{7s}P_{i,0}(X/b),\qquad
a_{i,b}=b^{s-1}a_{i,0}.
$$
所以 (21)–(23) 的原曲线版本精确为
$$
\boxed{
\begin{aligned}
P_{1,b}(0)&=-2b\,a_{1,b},&
P_{1,b}'(0)&=-a_{4,b}/8,\\
P_{4,b}'(0)&=\frac{b^{s-1}\mathfrak h^2}{24},&
P_{1,b}''(0)&=\frac{3a_{4,b}}{32b}
 -\frac{b^{s-2}\mathfrak h^2}{11520}.
\end{aligned}
}
\tag{25}
$$
$\mathfrak h$ 仍指基曲线的值。
(19) 两商的原质量分别是
$b^s\mathfrak h^5/1080$ 与 $b^s\mathfrak h^2/216$。
这些都是准确的单位尺度，不将基 $V$ 暗换为原曲线的另一 Frobenius 根。

本文只给原两负矩的必要条件与完整 conditional 来源，
没有由它们推出原 $S/T$ 中央关系或受限 mixed cut 为零。
特别不使用 R567 旧版关于 native 残差已等于整个算术总行的误述。

## 8. 可复算证书

[check-r573-complete-six-torsion-negative-moment-jets.mjs](../scripts/check-r573-complete-six-torsion-negative-moment-jets.mjs)
在原已有的 $13,19,31,61$ 四个纤维上：

- 从原 division 递推重建 $r,N,M,P_4,P_1$；
- 核对整个 $\psi_6$、$\mathscr L_3$、全五轨道的一阶/四阶零；
- 在 $\mathbf F_p[X]/(Q_5)$ 中用 (5) 计算完整 canonical $g_t$，
  保真实 $x(V),y(V),r(t)^6$，验证 (9) 的三条全值关系；
- 核对 (21)–(23)，以及 $p=61$ 真正出现的 $a_1=0$ 的全 $D_7$ 因子。

共 73 项精确检查。它没有扩大素数扫描，也没有通过
“尚未找到反例”宣称负矩非消失。所有一般素数结论由正文全平移、
缺失型及真实微分方程支付。
