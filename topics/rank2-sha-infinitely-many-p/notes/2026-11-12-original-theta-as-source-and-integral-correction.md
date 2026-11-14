# 原两条 theta 行的 Artin–Schreier 初始源及整一层修正

日期：2026-11-12。
**状态：以下实际初始方程、原有限次数源中的完整一层 $p$ 改良及准确次数界已证明。**
全文区分原源 $\mathbb Z_p[A_2,B]$ 与辅助源 $\mathbb Z_p[a,b]$。
新多项式确实属于原源；但不自动属于给定准确消失前缀的核，
尚未据此得到 R159 的严格总预算。

## 1. 原对象、赋值与全深度输入

沿 R162、R167，记

$$
a=\vartheta^4,\quad b=\sigma^4,\quad s=b/a,\quad X=a-1,\quad Y=b,
$$
$$
\mathcal A=A_2=a^{17}P(s),\quad B=a^{17}Q(s),\quad
E_D^{\mathrm{orig}}=\mathbb Z_p[\mathcal A,B]_{\le D}.
\tag{1}
$$

这里是原来的同次数两条秩二输入。$P,Q$ 是 R162 的固定多项式；
尤其

$$
P(s)=s+O(s^2),\qquad Q(s)-P(s)=-22s^2+O(s^3),
\qquad P,Q\in\mathbb Z[1/5][s].
\tag{2}
$$

固定 $p\equiv3\pmod4$、$p\ge7$，并删去 $p=11$。
为显示全部固定分母，下文也写 $p\nmid2\cdot5\cdot11\cdot17$；
其中 $5,17$ 本来就不在惰性范围。置

$$
r=(p+1)/4,\quad R=r(p-1),\quad
\varpi^R=p,\quad\lambda=\varpi^r,\quad\gamma=\varpi^p.
\tag{3}
$$

在 $K'=\mathbb Q_p(\varpi)$ 中用 $\nu_\varpi(\varpi)=1$，
所以 $v_p=\nu_\varpi/R$。整数环记为 $\mathcal O'$，剩余域是
$\mathbb F_p$。有

$$
\lambda^{p-1}=p,\qquad\gamma^r=p\lambda,\qquad\gamma^R=p^p.
\tag{4}
$$

R177 对同一实际曲线已证明：写
$a(s)=\exp(t(s))$、$b(s)=s a(s)$，则

$$
\frac{a(\gamma T)-1}{\lambda},\qquad
\frac{b(\gamma T)}{\gamma}\in\mathcal O'[[T]];
\qquad \bar x+\bar x^p=\tau\bar y^r,\quad
\tau\in\mathbb F_p^\times.
\tag{5}
$$

$\bar x,\bar y$ 是上述整级数的约化，$\bar y=T$。
这是全级数的约化，不只到第 $pr$ 项。

更强的输入来自 R174 同一整 Cartan 坐标
$U,V\in\mathbb Z_p[[X,Y]]$：

$$
U=X-Y/3+O((X,Y)^2),\quad
V=Y e(X,Y),\quad e(0,0)=1.
\tag{6}
$$

沿曲线以 $v=V$ 为输出，有

$$
U=v^r g(v^R),\quad
G(T)=p\,g(p^pT)\in\mathbb Z_p[[T]],\quad
G+TG^p\equiv\tau\pmod p.
\tag{7}
$$

任选 $\widetilde\tau\in\mathbb Z_p^\times$ 提升 $\tau$，定义

$$
\widetilde{\mathcal H}(X,Y)=U^p+pU-\widetilde\tau V^r.
\tag{8}
$$

在 $v=\gamma y$ 下，(7) 准确给

$$
\frac{\widetilde{\mathcal H}}{\lambda^p}
=y^r\{G(y^R)+y^R G(y^R)^p-\widetilde\tau\}
\in p\mathbb Z_p[[y]].
\tag{9}
$$

$V(a(\gamma T)-1,b(\gamma T))/\gamma$ 是
$T+O(T^2)$ 的整级数，故换回 (5) 的参数仍在
$p\mathcal O'[[T]]$。这比剩余域 AS 方程多保留了
**一个完整的 $p$**，而非只多一层 $\varpi$。
后面不会把原坐标误差本身宣称为 $p$ 的倍数。

## 2. 准确系数 374 与原源的初始方程

在原多项式环中取

$$
\mathcal C=B-\mathcal A+22\mathcal A^2,\qquad c_0=374.
\tag{10}
$$

给 $X,Y$ 的权分别为 $r,p$，系数 $p$ 的权为 $R$。
由 (1)–(2)，

$$
\mathcal A=Y(1+X)^{16}+O(Y^2),\qquad
B-\mathcal A=-22Y^2(1+X)^{15}+O(Y^3).
$$

所以

$$
\begin{aligned}
\mathcal C
&=22Y^2\big((1+X)^{32}-(1+X)^{15}\big)+O(Y^3)\\
&=374XY^2+O_{\mathrm{wt}}(>r+2p).
\end{aligned}
\tag{11}
$$

系数准确是 $22(32-15)=374$。
其余 $X^iY^2$ 项有 $i\ge2$，其余 $Y^j$ 项有 $j\ge3$；
$p>r$ 保证这些权严格较大。同时
$\mathcal A=Y+O_{\mathrm{wt}}(>p)$。

于是沿同一真实缩放图，

$$
\frac{\mathcal A}{\gamma}\longmapsto y,\qquad
\frac{\mathcal C}{\lambda\gamma^2}\longmapsto c=c_0xy^2.
\tag{12}
$$

消去 $x$ 得

$$
\boxed{\quad
c^p+\bar c_0^{\,p-1}c\,y^{2p-2}
-\bar c_0^{\,p}\tau y^{r+2p}=0.
\quad}
\tag{13}
$$

因 $\bar c_0\in\mathbb F_p^\times$，两个幂次系数可分别简化成
$1,\bar c_0$；保留显示形式方便核准整数提升。
实际分支仍是 $x(0)=0$，不能因 (13) 在原点有多条归一化分支
就任意改换。

具体原源提升为

$$
\mathcal F_p(\mathcal A,\mathcal C)
=\mathcal C^p+p c_0^{p-1}\mathcal C\mathcal A^{2p-2}
-c_0^p\widetilde\tau\mathcal A^{r+2p}.
\tag{14}
$$

代回 (10) 后，它属于 $E_{2p+r}^{\mathrm{orig}}$。
给 $\mathcal A,\mathcal C$ 的权为 $p,r+2p$，给 $p$ 的权为 $R$，
三项相同的权为

$$
\Omega=p(r+2p).
\tag{15}
$$

特别第二项的权为 $R+(r+2p)+(2p-2)p=\Omega$。
由 (12)–(13) 只能立即得到

$$
\varpi^{-\Omega}
\mathcal F_p\big(\mathcal A(\gamma T),\mathcal C(\gamma T)\big)
\in\varpi\mathcal O'[[T]].
\tag{16}
$$

不能把 (16) 直接写成 $p\mathcal O'[[T]]$；
坐标误差可先在 $\lambda$ 层出现。

## 3. 支付除法坐标，不能免费改原源

考虑

$$
Z=\frac{\mathcal C}{\mathcal A^2}
=22+a^{-17}\frac{Q(s)-P(s)}{P(s)^2}.
\tag{17}
$$

它在原 $(X,Y)$ 形式邻域中确实整且正则：
$P=s p_0$、$p_0(0)=1$，而 $Q-P$ 被 $s^2$ 整除，
所以 $(Q-P)/P^2\in\mathbb Z_p[[s]]$，常数为 $-22$。
于是

$$
Z(0,0)=0,\quad Z_X(0,0)=374=c_0,\quad
\mathcal A_Y(0,0)=1,\quad\mathcal A_X(0,0)=0.
\tag{18}
$$

Jacobian 行列式为 $-c_0$，在所选素数处为单位。
形式逆函数定理给

$$
\mathbb Z_p[[X,Y]]=\mathbb Z_p[[\mathcal A,Z]].
\tag{19}
$$

同时 $(Y)=(\mathcal A)$，故在新坐标中

$$
U=c_0^{-1}Z+O(\mathcal A,Z^2),\qquad
V=\mathcal A e_1(\mathcal A,Z),\quad e_1(0,0)=1.
\tag{20}
$$

(19) 只是完成局部环同构。
**$Z=\mathcal C/\mathcal A^2$ 并不是原多项式源中的免费新列。**
下面会逐项乘 $\mathcal A^{2p}$ 清除全部分母，并按原
$\mathcal A,B$ 总次数支付代价。

## 4. 原坐标中的 Weierstrass 准备

将

$$
\mathcal H_p(\mathcal A,Z)
=c_0^p\widetilde{\mathcal H}
\big(X(\mathcal A,Z),Y(\mathcal A,Z)\big)
\in\mathbb Z_p[[\mathcal A,Z]]
\tag{21}
$$

视为完备局部环
$\mathcal R=\mathbb Z_p[[\mathcal A]]$、
$\mathfrak m_{\mathcal R}=(p,\mathcal A)$ 上的 $Z$ 级数。
模 $(p,\mathcal A)$ 时，

$$
\overline{\mathcal H_p}
=\big(c_0\overline{U(0,Z)}\big)^p
=Z^p\cdot\text{一个常数项为一的形式单位}.
\tag{22}
$$

因此它关于 $Z$ 正则、阶准确为 $p$。
形式 Weierstrass 准备给

$$
\mathcal H_p=S_p(\mathcal A,Z)\mathscr W_p(\mathcal A,Z),
\qquad S_p\in\mathbb Z_p[[\mathcal A,Z]]^\times,
\tag{23}
$$
$$
\mathscr W_p=Z^p+\sum_{i=0}^{p-1}w_i(\mathcal A)Z^i,
\qquad w_i\in(p,\mathcal A)\mathbb Z_p[[\mathcal A]].
\tag{24}
$$

这里仅用完备局部环版本。其构造亦可直接描述：
模 $\mathfrak m_{\mathcal R}$ 先用 (22) 除 $Z^p$；
若已除至 $\mathfrak m_{\mathcal R}^n$，在
$\mathfrak m_{\mathcal R}^n/\mathfrak m_{\mathcal R}^{n+1}$
上用同一个 $Z^p$ 乘单位作除法，
将余项选成次数小于 $p$ 的多项式。
逐层得到 $Z^p=q\mathcal H_p+\rho$。
完备性给极限，$q$ 为单位、$\deg_Z\rho<p$，
于是 $\mathscr W_p=Z^p-\rho$。完整标准证明的原始来源见文末。

给 $\mathcal A,Z,p$ 的权分别为 $p,r,R$。
(20) 表明 $\mathcal H_p$ 的最小权为 $pr$，初始式为

$$
Z^p+p c_0^{p-1}Z-c_0^p\widetilde\tau\mathcal A^r.
\tag{25}
$$

整单位 $S_p$ 的权零初始项只是其常数约化。
$\mathscr W_p$ 又在 $Z$ 上首一，比较初始式的 $Z^p$ 系数给
$S_p(0,0)\equiv1\pmod p$。
因此 $\mathscr W_p$ 也有同一个初始式 (25)。
此处的初始式保留系数的 $p$ 赋值，不能直接删除 $pZ$。

在原缩放图上，$\mathcal A/\gamma,Z/\lambda\in\mathcal O'[[T]]$，
二者常数项都是零。
所以 $S_p$ 的值和其逆的值均为 $\mathcal O'[[T]]$ 的单位。
(9)、(21)、(23) 遂给

$$
\boxed{\quad
\lambda^{-p}
\mathscr W_p\big(\mathcal A(\gamma T),Z(\gamma T)\big)
\in p\mathcal O'[[T]].
\quad}
\tag{26}
$$

所有系数只需属于 $\mathbb Z_p$。
没有声称准备多项式系数是有理数，更没有将它当成与 $p$ 无关的
全局多项式。

## 5. 清除真实分母后的有限次数原源

置 $J=2r-1$，将每个 $w_i(\mathcal A)$ 截到 $\mathcal A$ 次数
不超过 $J$：

$$
\mathscr W_{p,J}
=Z^p+\sum_{i=0}^{p-1}\sum_{j=0}^{J}w_{ij}\mathcal A^jZ^i.
\tag{27}
$$

遗漏的每个单项在缩放后的权至少为

$$
p(J+1)=2pr>pr+R=r(2p-1).
\tag{28}
$$

这是因为 $w_{ij}$ 全整，且 $Z$ 的权 $r$ 非负。
所以 (26) 对 $\mathscr W_{p,J}$ 仍然成立，保留完整一层 $p$。

现在定义真正的原多项式

$$
\boxed{\quad
\mathcal P_p(\mathcal A,B)
=\mathcal A^{2p}\mathscr W_{p,J}
 \left(\mathcal A,\frac{B-\mathcal A+22\mathcal A^2}{\mathcal A^2}\right).
\quad}
\tag{29}
$$

其有限展开为

$$
\mathcal P_p=\mathcal C^p+
\sum_{i=0}^{p-1}\sum_{j=0}^{J}
w_{ij}\mathcal A^{\,2p+j-2i}\mathcal C^i.
\tag{30}
$$

$2p+j-2i\ge0$，故没有剩余分母。
每项在原 $\mathcal A,B$ 中的次数至多

$$
(2p+j-2i)+2i=2p+j\le2p+2r-1.
\tag{31}
$$

$\mathcal C^p$ 的 $B^p$ 系数为一，其余项的 $B$ 次数小于 $p$。
于是 $\mathcal P_p$ 是原整源中的 primitive 元：

$$
\mathcal P_p\in E_{\,2p+2r-1}^{\mathrm{orig}},\qquad
[B^p]\mathcal P_p=1.
\tag{32}
$$

由 (25)、(28)，在
$\mathrm{wt}(\mathcal A)=p,\mathrm{wt}(\mathcal C)=r+2p$、
$\mathrm{wt}(p)=R$ 下，
$\mathcal P_p$ 的最小权为 $\Omega$，
准确初始式就是 (14)，没有另乘 $\mathcal A$ 因子。

将 (26) 乘上 $(\mathcal A(\gamma T)/\gamma)^{2p}$，得主结论：

$$
\boxed{\quad
\frac{\mathcal P_p(\mathcal A(\gamma T),B(\gamma T))}
{\lambda^p\gamma^{2p}}\in p\mathcal O'[[T]],
\qquad
\deg_{\mathcal A,B}\mathcal P_p
\le2p+2r-1=\frac{5p-1}{2}.
\quad}
\tag{33}
$$

这是相对于同一最小权 $\Omega$ 的完整一层 $p$ 改良。
逐系数亦可写为

$$
v_p\!\left([s^m]\mathcal P_p(\mathcal A(s),B(s))\right)
\ge\frac{\Omega-pm}{R}+1.
\tag{34}
$$

它对全部 $m$ 成立，没有截在 $m<pr$。
证明未使用原两条中央导数同时消失，
故不能单凭此结论宣称共同失败假设已经产生严格总预算。

## 6. 与辅助 ab 源的准确比较

在辅助源 $\mathbb Z_p[X,Y]$ 中，直接将 (8) 截到总次数
$2p-2$，记为 $\mathcal Q_p$。
任何遗漏单项的 $X,Y$ 权至少 $r(2p-1)=pr+R$，所以

$$
\mathcal Q_p\in\mathbb Z_p[X,Y]_{\le2p-2},\qquad
\frac{\mathcal Q_p(X(\gamma T),Y(\gamma T))}{\lambda^p}
\in p\mathcal O'[[T]].
\tag{35}
$$

其初始式是 $X^p+pX-\widetilde\tau Y^r$。
这并不给相同次数的原 $E_D^{\mathrm{orig}}$ 元素；
真正支付原源代价的是 (29)–(33)：

$$
\begin{array}{c|c|c}
\text{源}&\text{次数上界}&\text{整值的准确归一}\\ \hline
\mathbb Z_p[a,b]&2p-2&
\lambda^{-p}\mathcal Q_p\in p\mathcal O'[[T]]\\
\mathbb Z_p[A_2,B]&(5p-1)/2&
(\lambda^p\gamma^{2p})^{-1}\mathcal P_p\in p\mathcal O'[[T]].
\end{array}
\tag{36}
$$

原源的额外次数及 $\gamma^{2p}$ 来自真实
$Z=\mathcal C/\mathcal A^2$ 与逐项清分母，不能免费省略。

## 7. 已付范围和下一实际问题

本文给的是一个存在于原有限次数源中的 primitive 多项式，
其完整局部函数值较初始权统一多一层 $p$。
系数由同一 Cartan 坐标、Weierstrass 除法及有限截断构造；
未添加自由 $Z$ 列，未替换原两条 theta 行。

若 $P$ 原来在指定前缀零核中，从 $P$ 减去
$\mathcal P_p Q$，余项通常不再保持同一个前缀。
因此尚不能直接推出原全部 $\varphi_{D,k}$ 的范数改良。
须把 (30) 的关系和余项同时放进完整前缀矩阵，
如 R176 那样保留各块之间的实际抵消。
本文没有证明 $\mathcal P_p$ 的值为零，
也没有证明 $J'_{17,p}$ 或 $J'_{34,p}$ 无穷次非零。

## 来源与依赖

- [R162 原固定多项式与 jet](2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)
  和 [R167 实际 ab 实现](2026-11-12-closed-theta-sigma-plane-and-integral-dynamics.md)：
  原对象、完整规范及源次数。
- [R174 整 Cartan 坐标](2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)
  和 [R177 全深 canonical AS 约化](2026-11-12-full-depth-canonical-as-reduction-and-source-initial-form.md)：
  (5)–(9) 的真实全级数与一层 $p$，不是任意选取的 AS lift。
- Mel Hochster, *The structure theory of complete local rings*，
  作者讲义，2026 年网页版本（PDF 未署成文年份），pp. 14–15，
  “The Weierstrass preparation theorem”及紧随的 monic-associate 推论，
  [作者原文](https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2026/04/Structure.pdf)。
  已读完整证明；这里只在
  $\mathcal R=\mathbb Z_p[[\mathcal A]]$、$\mathfrak m=(p,\mathcal A)$
  上使用，§4 另给本题的逐层构造。
- [R176 原除幂源格与共同前缀](2026-11-12-actual-divided-source-lattices-and-prefix-saturation.md)：
  下一步仍需支付的完整前缀比较，其首带结论未被本篇直接外推。
