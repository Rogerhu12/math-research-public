# R478 — 临界幂 cap 的完整复余量非零与真实光滑正近似

本稿只作纸面证明，没有运行程序、积分、符号观察、人工数值或旧检查。它消费 [R471](R471-five-real-cap-conditions-and-the-complete-complex-second-moment-interface.md) 的完整复积分，给出一个可准确判定的边界模型，并构造具有严格 $A_f>0$ 和末端简单根的实际光滑 cap 逼近它。

**结论。** 对临界幂
$u(y)=4y^{5/2}/15$、$0\le y\le1$，完整复二矩余量在两个共轭根上均非零。证明保留原左常数，用一个唯一的八次多项式原函数和三重因子反证完成，不需要计算任何积分数值。这个非零性可传给本文明确构造的一组真实光滑正 cap。

临界幂本身 $A_f\equiv0$，并非原严格允许 cap。光滑近似的末端矩也不固定为某个旧库的值。因此本文不判定已经冻结的 $\psi_3$ cap，不由极限替代其实际观察。

## 1. 原完整积分及临界模型

在本节固定 $0\le y\le1$，置

$$
u_0=\frac4{15}y^{5/2},\qquad
p_0=\frac23y^{3/2},\qquad
r_0=y^{1/2},\qquad
q_0=\frac12y^{-1/2}.
\tag{1}
$$

左端 $u_0,p_0,r_0$ 都趋零，$q_0$ 可积。原完整量满足

$$
6p_0q_0-2r_0^2=0,\qquad
u_0r_0=\frac35p_0^2,\qquad
q_0=\frac{r_0^2}{3p_0}\quad(y>0).
\tag{2}
$$

对复参数 $z$ 保留真实累计

$$
w_z=p_0-(y+z)r_0,\qquad
a_z=u_0-(y+z)p_0+\frac{(y+z)^2r_0}{2}.
\tag{3}
$$

它们都在左端趋零。末端二矩条件是

$$
a_z(1)=\frac12\left(z^2+\frac23z+\frac15\right)=0,
$$

故两个简单根为

$$
\boxed{z_\pm=-\frac13\pm\frac{2i}{3\sqrt5}.}
\tag{4}
$$

R471 的完整余量在这个可积模型中定义为

$$
\mathcal E_z
=\frac32\int_0^1(y+z)^2w_z^2a_z^2q_0\,dy .
\tag{5}
$$

左端被积式为 $O(y^{3/2})$，因此积分实际收敛；这里没有用一个自由 primitive 常数代替它。

## 2. 完整原函数与非零常数

记

$$
k=\frac{(y+z)r_0}{p_0}
=\frac32\left(1+\frac zy\right),\qquad
A(k)=\frac{k^2}{2}-k+\frac35.
\tag{6}
$$

由(2)，

$$
w_z=p_0(1-k),\qquad
a_z=\frac{p_0^2}{r_0}A(k).
\tag{7}
$$

将(7)直接代入原积分(5)，其完整密度准确为

$$
\frac32(y+z)^2w_z^2a_z^2q_0
=C\,y^{19/2}k^2(1-k)^2A(k)^2,\qquad
\boxed{C=\frac12\left(\frac23\right)^7=\frac{64}{2187}>0.}
\tag{8}
$$

没有把第三导数项独立丢弃，也没有在积分内部额外施加末端的 $A(k)=0$。

因

$$
\frac{dk}{dy}=-\frac{k-3/2}{y},
$$

取唯一的实多项式 $R$，$\deg R\le8$，满足

$$
\boxed{
\frac{21}{2}R(k)-(k-\tfrac32)R'(k)
=C\,k^2(1-k)^2A(k)^2.
}
\tag{9}
$$

它确实存在且唯一：在 $1,k,\ldots,k^8$ 上，左侧线性算子的对角数为
$21/2-j$，$0\le j\le8$，全部非零。此为一个有限三角定义，不调用新的秩观察。

为给出可逐项消费的完整规范，令 $v=k-1$。写

$$
R(k)=\frac{C}{4}\sum_{j=0}^8\rho_jv^j.
$$

置 $\rho_9=0$，则全部九系数由

$$
(21-2j)\rho_j+(j+1)\rho_{j+1}=2b_j,\qquad
(b_0,\ldots,b_8)
=(0,0,\tfrac1{25},\tfrac2{25},\tfrac{11}{25},
\tfrac45,\tfrac75,2,1)
\tag{10}
$$

唯一确定。式(10)来自
$v^2(v+1)^2(v^2+1/5)^2$ 的原展开；它保留全部项，而不是只给最高两项。

现在(8)–(9)给真正的原函数：

$$
\boxed{
\frac{d}{dy}\bigl(y^{21/2}R(k(y))\bigr)
=\frac32(y+z)^2w_z(y)^2a_z(y)^2q_0(y).
}
\tag{11}
$$

由于 $k(y)=O(y^{-1})$ 而 $\deg R\le8$，

$$
y^{21/2}R(k(y))=O(y^{5/2})\longrightarrow0
\quad(y\downarrow0).
\tag{12}
$$

所以原左端常数就是零。对(4)的两根，

$$
k(1)=1\pm\frac{i}{\sqrt5},\qquad
\boxed{\mathcal E_{z_\pm}=R(1\pm i/\sqrt5).}
\tag{13}
$$

## 3. 三重因子反证

假设(13)中的一个值为零。$R$ 的系数实，另一个共轭值也为零，因此
$A$ 整除 $R$。

在 $A$ 的任一根 $\kappa=1\pm i/\sqrt5$，有
$\kappa-3/2\ne0$。式(9)的右侧含 $A^2$，故在该点为零。
已知 $R(\kappa)=0$，(9)迫

$$
R'(\kappa)=0.
$$

再微分(9)一次；右侧在 $\kappa$ 仍为零，所以

$$
R''(\kappa)=0.
$$

两根均简单，于是

$$
A^3\mid R.
\tag{14}
$$

因为 $\deg R\le8$，可写

$$
R=A^3(av^2+bv+c),\qquad v=k-1.
\tag{15}
$$

将(15)代回(9)并除去 $A^2$，得到完整多项式恒等式

$$
\left(\frac94v^2+\frac32v+\frac{21}{20}\right)
(av^2+bv+c)
-(v-\tfrac12)\frac{v^2+1/5}{2}(2av+b)
=C(v^4+2v^3+v^2).
\tag{16}
$$

只需四个低/高系数即可产生矛盾，但(16)本身保留全部原项。

常数和一次系数分别给

$$
21c+b=0,\qquad
\frac32c+\frac{19}{20}b+\frac1{10}a=0.
$$

因此

$$
b=-21c,\qquad a=\frac{369}{2}c.
\tag{17}
$$

四次系数给

$$
C=\frac54a=\frac{1845}{8}c.
\tag{18}
$$

三次系数却给

$$
2C=\frac74b+2a=\frac{1329}{4}c.
\tag{19}
$$

而(18)要求 $2C=1845c/4$。故 $c=0$，进而 $a=b=0$、$C=0$，
与(8)严格矛盾。得到

$$
\boxed{\mathcal E_{z_+}\ne0,\qquad \mathcal E_{z_-}\ne0.}
\tag{20}
$$

证明没有依赖复被积函数的符号，也没有把 $A_f\equiv0$ 的临界参考误称为严格正 cap。

## 4. 完整余量对 C2 cap 的连续性

把 R471(28)–(29)的完整局部多项式记为
$\mathcal P(X,u,p,r)$ 和 $\mathcal L(X,u,p,r)$。该原身份是

$$
\mathcal L
=\frac{d}{dy}\mathcal P
+\frac32(y+z)^2w_z^2a_z^2u'''.
$$

所以对左端三 jet 为零的 cap，

$$
\boxed{
\mathcal E_z(u)
=\int_0^1\mathcal L(y+z,u,u',u'')\,dy
-\mathcal P(1+z,u(1),u'(1),u''(1)).
}
\tag{21}
$$

左端 $\mathcal P=0$；(1)也具有同一零端值，故同样适用。式(21)是原完整积分的分部形式，保留末端 primitive，并不要求单独的第三导数在极限中一致收敛。

因此，若 $u_n\to u_0$ 于 $C^2[0,1]$，则末端三矩和根 $z_{n,\pm}$ 收敛于(4)，并且

$$
\mathcal E_{z_{n,\pm}}(u_n)
\longrightarrow \mathcal E_{z_\pm}(u_0).
\tag{22}
$$

这里末端方差在(1)处严格正；充分接近时两根仍非实且简单。
由(20)，对一个足够大的**有限** $n$，(22)的两个真实值都非零。

## 5. 实际光滑正 cap 的明确近似

为说明(22)不只是形式连续性，下面给出允许 cap 的实际构造。
取

$$
c_0=(2/3)^{2/3}.
$$

选一个固定光滑曲率密度 $b$，满足：

- $b>0$ 于 $(0,1)$；
- 在左端一个小邻域，
  $b=(e^{-1/y})''$，其中 $e^{-1/y}$ 在 $y\le0$ 延为零；
- 在右端一个小邻域，$b=1-y$。

左端可选在 $y<1/4$，那里 $(e^{-1/y})''>0$；
中间用保持正值的光滑连接即可。因此

$$
b(1)=0,\qquad b'(1)=-1.
$$

令 $\rho_\delta$ 是一个实际非负光滑单位质量函数，支撑在
$(\delta,2\delta)$。定义

$$
\begin{aligned}
v_{\delta,\varepsilon}(y)
={}&c_0\int_0^y(y-t)\rho_\delta(t)\,dt
+\varepsilon\int_0^y(y-t)b(t)\,dt,\\
p_{\delta,\varepsilon}&=v_{\delta,\varepsilon}^{3/2},\\
u_{\delta,\varepsilon}(y)&=\int_0^y p_{\delta,\varepsilon}(t)\,dt,
\qquad \delta,\varepsilon>0.
\end{aligned}
\tag{23}
$$

近左端，第一项为零，第二项准确为
$\varepsilon e^{-1/y}$。所以

$$
p_{\delta,\varepsilon}
=\varepsilon^{3/2}e^{-3/(2y)}
$$

在那里全平，$u_{\delta,\varepsilon}$ 亦有真实光滑零 germ。
内部 $v,v'>0$，并且

$$
v''=c_0\rho_\delta+\varepsilon b>0.
$$

直接求导，若 $p=v^{3/2}$，则

$$
6p p''-2(p')^2=9v^2v''.
\tag{24}
$$

因此该 cap 在 $0<y<1$ 严格满足 $A_f>0$；
其 $r=p'>0$，$q=p''>0$。末端

$$
A_f(1)=0,\qquad
A_f'(1)=9v(1)^2v'''(1)
=-9\varepsilon v(1)^2<0.
\tag{25}
$$

故末端是一个真实简单 $A_f$ 根。近右端可按同一
$v''=\varepsilon(1-y)$ 延过该点，得到根内侧的严格负号 germ；
这不把整个母的后续闭合当成已付。

最后验证所需的实际 $C^2$ 收敛。对 $y\ge2\delta$，

$$
v_{\delta,\varepsilon}
=c_0(y-m_\delta)+O(\varepsilon),\qquad
v'_{\delta,\varepsilon}=c_0+O(\varepsilon),
\qquad \delta<m_\delta<2\delta.
$$

在 $0\le y\le2\delta$，

$$
0\le v\le C y,\qquad 0\le v'\le C,\qquad
0\le r=\frac32\sqrt v\,v'\le C\sqrt y .
$$

所以令 $\delta,\varepsilon\downarrow0$，有

$$
u_{\delta,\varepsilon}\longrightarrow\frac4{15}y^{5/2}
\quad\hbox{于 }C^2[0,1].
\tag{26}
$$

无需要求 $q$ 的一致收敛；它在左窄层可以很大。
(21)已证明这种真实近似足以控制完整余量。

由(20)–(26)，可固定两个足够小但严格正、有限的参数
$\delta,\varepsilon$，获得一个真实光滑正 cap，满足所有(24)–(25)的严格门，且其两复根值同时非零。

## 6. 适用范围

本文准确支付两个结论：

1. 临界参考的**完整**复值确非零，非零性由原锚、多项式原函数和代数反证证明。
2. 存在明确的真实光滑 cap，左端全平、内部 $q>0,A_f>0$、
   末端为简单 $A_f$ 根，并且两复值非零。

没有支付的是：固定 $\psi_3$ 的具体积分值、所有允许 cap 的普遍非零、
或完整五个共同 self 条件的同时可消。本文近似中末端三矩会改变；
若要纳入特定全母数据及二十目标，须另保真实从开始构造或回补接口，
不能把(26)当成对旧冻结母的修改许可。

正幅与正宽的输运仍按 R474 的完整比例
$\mathcal E\mapsto a^5H^{-2}\mathcal E$，所以已证明的非零性不会因一次合法的共同坐标归一消失。所有 actual 成本、共同窗口和同十三行前提继续保留。
