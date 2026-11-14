# R183. 任意 p 精度的实际原 theta 源与准确次数代价

日期：2026-11-12。**状态：以下全系数尺度、首个真分母、任意精度原源与准确零前缀均已证明；主目标未完成。**
这是 R180 的全深推广。所有多项式仍属于原
$\mathbb Z_p[A_2,B]$；系数可以依赖 $p$，仅要求在 $\mathbb Z_p$。
本文不把一个已知有限零前缀自动延长为任意指定的前缀。

## 1. 保持实际对象与结论

固定 $p\equiv3\pmod4$、$p\ge7$、$p\ne11$，置

$$
r=(p+1)/4,\quad R=r(p-1),\quad
\varpi^R=p,\quad\lambda=\varpi^r,\quad\gamma=\varpi^p.
\tag{1}
$$

$\mathcal O'$ 表示 $\mathbb Q_p(\varpi)$ 的整数环。
沿 R163、R178 的同一实际形式曲线，取

$$
t(s)=\sum_{m\ge1}t_ms^m,\qquad
t_m=\frac1m\prod_{j=0}^{m-1}\frac{4j+1}{4j+3},
\quad a=e^t,\quad b=sa,
\tag{2}
$$
$$
\mathcal A=A_2=a^{17}P(b/a),\quad B=a^{17}Q(b/a),\qquad
\mathcal C=B-\mathcal A+22\mathcal A^2,\quad c_0=374.
\tag{3}
$$

固定 $P,Q$、原整源及坏位完全沿用 R178。特别

$$
Z=\mathcal C/\mathcal A^2,\qquad
\mathbb Z_p[[a-1,b]]=\mathbb Z_p[[\mathcal A,Z]],
\quad
Z=c_0(a-1)+O\big(b,(a-1)^2\big),
\tag{4}
$$

且 $(b)=(\mathcal A)$。在权 $\mathrm{wt}(a-1)=r$、
$\mathrm{wt}(b)=p$ 下，$\mathcal A$ 的首项为 $b$，
$Z$ 的首项为 $c_0(a-1)$。

令 $q\ge1$，并定义

$$
H_q=\frac{p^q-1}{p-1}.
$$

取整数 $n\ge1$ 满足

$$
H_q-q\le n\le pH_q-q.
\tag{5}
$$

置

$$
\begin{aligned}
N_{q,n}
&=\left\lceil
\frac{(q+n)R\,p^{q-1}}{p^q-1}
\right\rceil-1,\\
J_{q,n}
&=\left\lceil\frac{r+(q+n)R}{p}\right\rceil-1\\
&=(q+n)r-\left\lfloor\frac{(q+n-1)r}{p}\right\rfloor-1,\\
D_{q,n}&=2p^q+J_{q,n}.
\end{aligned}
\tag{6}
$$

**结论。** 存在实际原源的 primitive 多项式

$$
\mathcal P_{q,n}\in
\mathbb Z_p[\mathcal A,B]_{\le D_{q,n}},
\qquad [B^{p^q}]\mathcal P_{q,n}=1,
\tag{7}
$$

同时满足

$$
\boxed{\quad
\frac{\mathcal P_{q,n}
(\mathcal A(\gamma T),B(\gamma T))}
{p^{q-1}\lambda^p\gamma^{2p^q}}
\in p^n\mathcal O'[[T]],
\qquad
\operatorname{ord}_s\mathcal P_{q,n}(\mathcal A(s),B(s))
\ge D_{q,n}+1.
\quad}
\tag{8}
$$

这里分母是 $p^{q-1}\lambda^p\gamma^{2p^q}$，
**不是** $\lambda^{p^q}\gamma^{2p^q}$。
准备多项式的 $Z$ 次数以及清分母次数真正增加到了
$p^q$ 和 $2p^q$。

这些允许区间覆盖任意 $n\ge1$，因为

$$
pH_q-q=H_{q+1}-(q+1).
\tag{9}
$$

若选择满足上界的最小 $q$，则除 $q=1$ 外实际严格超过下界，
不会重复使用相邻区间的公共端点。$q=1$ 正是 R180 的
$1\le n\le p-1$。

## 2. 原对数的首个负层及更大尺度

R163 的准确式是

$$
v_p(t_m)=-v_p(m)+
\sum_{h\ge1}(-1)^h
\mathbf1_{\{p^h/4<(m\bmod p^h)<3p^h/4\}}.
\tag{10}
$$

其已证偶奇截断界为

$$
\min_{1\le m<p^H}v_p(t_m)=
\begin{cases}
-H,&H\ \text{奇},\\
-H+1,&H\ \text{偶}.
\end{cases}
\tag{11}
$$

还需一个准确的首次位置：

$$
\boxed{\quad
v_p(t_m)\le-(2j+1)
\text{ 的最小正指标是 }m=r p^{2j};
\quad v_p(t_{r p^{2j}})=-(2j+1).
\quad}
\tag{12}
$$

证明只用 (10)。在 $m<r p^{2j}<p^{2j+1}$ 时写
$m=p^\alpha b$、$p\nmid b$。若 $\alpha\le2j-1$，
R163 的逐 $\alpha$ 负项计数给损失至多 $2j$：
$\alpha$ 偶时上界为
$\alpha+\lceil(2j+1-\alpha)/2\rceil$，
$\alpha$ 奇时为
$\alpha+\lfloor(2j+1-\alpha)/2\rfloor$。
若 $\alpha=2j$，则 $b<r$，所有剩余指标均为零，
损失仍只有 $2j$。在 $m=r p^{2j}$，剩余部分 $b=r$
恰有第一个负指标，其他指标为零，给出等号。
$j=0$ 是同一计数的直接特例。

选取相容根

$$
\sigma_q^{p^{q-1}}=\varpi,\qquad
K_q=\mathbb Q_p(\sigma_q),\qquad
v_p(\sigma_q)=\frac{1}{R p^{q-1}}.
\tag{13}
$$

该 Eisenstein 扩张的剩余域仍为 $\mathbb F_p$。
记 $j=\lfloor q/2\rfloor$、$m_0=r p^{2j}$，并置

$$
\tau_j=p^{2j+1}t_{r p^{2j}}\bmod p\in\mathbb F_p^\times.
$$

有全系数整性及唯一单位项

$$
\boxed{\quad
\frac{p^q t(\sigma_qT)}{\lambda}
\in\mathcal O_{K_q}[[T]],\qquad
\overline{\frac{p^q t(\sigma_qT)}{\lambda}}
=\tau_jT^{m_0}.
\quad}
\tag{14}
$$

这里约化模 $K_q$ 的极大理想，不能擅自替换为模 $p$。

详细核对如下。单项的 $R v_p$ 为

$$
R\big(q+v_p(t_m)\big)+p^{1-q}m-r.
\tag{15}
$$

若 $q$ 奇，(11) 在 $m<p^{q+1}$ 给
$v_p(t_m)\ge-q$。若等于 $-q$，(12) 强迫
$m\ge r p^{q-1}=m_0$；(15) 恰在 $m_0$ 为零。
其他项至少多一层整数 $p$，所以严格为正。

若 $q$ 偶，在 $m<p^q$ 有 $v_p(t_m)\ge-q+1$，
故 (15) 为正。在 $p^q\le m<p^{q+2}$ 有
$v_p(t_m)\ge-q-1$。若赋值至少为 $-q$，
则 (15) 至少为 $p-r>0$；
若恰为 $-q-1$，(12) 强迫
$m\ge r p^q=m_0$，只有该首次指标给零。

剩下的大指标统一处理。若 $p^h\le m<p^{h+1}$，
(11) 给 $v_p(t_m)\ge-h-1$。
置 $d=h+1-q$；奇 $q$ 的剩余范围有 $d\ge2$，
偶 $q$ 有 $d\ge3$。于是 (15) 至少为

$$
p^d-dR-r>0.
\tag{16}
$$

在 $d=2$，
$p^2-2R-r=(2p^2-p+1)/4>0$；
相邻差为 $(p-1)p^d-R>0$。
这同时证明高指标的赋值趋于无穷。
代入唯一零指标时，
$\sigma_q^{m_0}/\lambda$ 的 $p$ 次幂恰好抵消
$q$ 与 $2j+1$ 的差，约化确为 $\tau_j$，得到 (14)。

## 3. 实际 p^q 次幂的准确首分母

写真实级数

$$
a(s)^{p^q}=\exp(p^q t(s))
=\sum_{m\ge0}d_m^{(q)}s^m,\qquad d_0^{(q)}=1.
$$

由 (14) 与 R177 的指数分母计算，

$$
\frac{a(\sigma_qT)^{p^q}-1}{\lambda}
=\sum_{\ell\ge1}\frac{\lambda^{\ell-1}}{\ell!}
\left(\frac{p^q t(\sigma_qT)}{\lambda}\right)^\ell
\in\mathcal O_{K_q}[[T]].
$$

因为
$v_p(\lambda^{\ell-1}/\ell!)=(s_p(\ell)-1)/(p-1)$，
单位恰在 $\ell=p^h$；Wilson 分块给其约化 $(-1)^h$。
所以

$$
R\,v_p(d_m^{(q)})+p^{1-q}m\ge r\qquad(m>0),
\tag{17}
$$
$$
\overline{\frac{a(\sigma_qT)^{p^q}-1}{\lambda}}
=\tau_j\sum_{h\ge0}(-1)^hT^{m_0p^h}.
\tag{18}
$$

由 $v_p(d_m^{(q)})\in\mathbb Z$ 得

$$
\boxed{\quad
d_m^{(q)}\in\mathbb Z_p\ (m<r p^q),\qquad
v_p(d_{r p^q}^{(q)})=-1.
\quad}
\tag{19}
$$

确实 $m<r p^q$ 时 (17) 的右界严格大于 $-R$。
在 $m=r p^q$，有 $\sigma_q^m/\lambda=p$；
该项在 (18) 中为 $h=0$（偶 $q$）或 $h=1$（奇 $q$），
非零。因此更准确地，

$$
p d_{r p^q}^{(q)}\equiv
\begin{cases}
\tau_j,&q\ \text{偶},\\
-\tau_j,&q\ \text{奇}
\end{cases}
\pmod p.
\tag{20}
$$

(18) 还给无限多个达到 (17) 的系数，故实际
$a(s)^{p^q}$ 的收敛半径准确为
$p^{-1/(R p^{q-1})}$。本篇仅使用全系数界；
不在临界圆周的单位参数处代入该无限约化级数。

## 4. 同时支付原截断与两个边界

简记 $N=N_{q,n}$、$J=J_{q,n}$。
令 $c_q=p-p^{1-q}=(p^q-1)/p^{q-1}$。
(5) 给

$$
r p^{q-1}
\le N+1=\left\lceil\frac{(q+n)R}{c_q}\right\rceil
\le r p^q.
\tag{21}
$$

所以 $N<r p^q$，(19) 支付下述所有系数的整性：

$$
\mathfrak J_{q,n}(a,b)
=a^{N+p^q}-\sum_{m=0}^{N}
d_m^{(q)}a^{N-m}b^m
\in\mathbb Z_p[a,b].
\tag{22}
$$

沿原 $b=sa$，准确有

$$
\mathfrak J_{q,n}(a(s),b(s))
=a(s)^N\sum_{m>N}d_m^{(q)}s^m.
\tag{23}
$$

由 (17)，在原 $\gamma$ 尺度下，

$$
R\,v_p(d_m^{(q)}\gamma^m)
\ge r+c_qm
\ge r+c_q(N+1)\ge r+(q+n)R.
\tag{24}
$$

因此

$$
\frac{\mathfrak J_{q,n}(a(\gamma T),b(\gamma T))}
{p^{q-1}\lambda^p}
\in p^n\mathcal O'[[T]],
\qquad
\operatorname{ord}_s\mathfrak J_{q,n}\ge N+1.
\tag{25}
$$

乘 $a(\gamma T)^N$ 不损失整性，因为 R177
已经证明它是常数一的整单位。

还必须核查原精确前缀所需的 $J\le N$。
由 (21)，$r\le p^{1-q}(N+1)$，从而

$$
r+(q+n)R\le r+c_q(N+1)\le p(N+1).
$$

故

$$
0\le J=\left\lceil\frac{r+(q+n)R}{p}\right\rceil-1
\le N.
\tag{26}
$$

在上端 $n=pH_q-q$，两个截断准确为

$$
N=r p^q-1,\qquad J=R H_q,
\qquad D_{q,n}=2p^q+R H_q.
\tag{27}
$$

若不满足 (5) 的下界，则 $J\le N$ 未必成立；
本文不把次数加一的前缀推广到那一范围。

## 5. 原坐标准备、清分母及真正初始权

把 $c_0^{p^q}\mathfrak J_{q,n}$ 写入 (4) 的实际整坐标，
记为 $\mathscr H_{q,n}(\mathcal A,Z)$。
在 $\mathcal A=0$ 时 $b=0$，
$a=1+c_0^{-1}Z+O(Z^2)$。模 $(p,\mathcal A)$ 有

$$
\overline{\mathscr H_{q,n}}
=\bar c_0^{\,p^q}\bar a^N(\bar a-1)^{p^q}
=Z^{p^q}\cdot\text{常数项为一的单位}.
$$

因此在系数环 $\mathbb Z_p[[\mathcal A]]$、
极大理想 $(p,\mathcal A)$ 上的 Weierstrass 准备给

$$
\mathscr H_{q,n}=S_{q,n}\mathscr W_{q,n},\qquad
S_{q,n}\in\mathbb Z_p[[\mathcal A,Z]]^\times,
\tag{28}
$$
$$
\mathscr W_{q,n}
=Z^{p^q}+\sum_{i=0}^{p^q-1}w_i(\mathcal A)Z^i,\qquad
w_i\in(p,\mathcal A)\mathbb Z_p[[\mathcal A]].
\tag{29}
$$

$S_{q,n}(0,0)\equiv1\pmod p$。
在整个原 $\gamma$ 缩放中，
$\mathcal A/\gamma,Z/\lambda\in\mathcal O'[[T]]$，
二者常数为零，所以准备单位及其逆的实际值均整且常数为单位。
因此 (25) 的精度和原阶数都完整传给 $\mathscr W_{q,n}$。

把每个 $w_i(\mathcal A)$ 截到 $\mathcal A$ 次数 $J$，
记为 $\mathscr W^{[J]}_{q,n}$。
删项的缩放权至少为
$p(J+1)\ge r+(q+n)R$，原 $s$ 阶至少为 $J+1$。
由 (26)，截断后同时保留 (25) 的精度和阶数 $J+1$。
定义

$$
\mathcal P_{q,n}(\mathcal A,B)
=\mathcal A^{2p^q}
\mathscr W^{[J]}_{q,n}
\left(\mathcal A,\frac{\mathcal C}{\mathcal A^2}\right).
\tag{30}
$$

逐项为

$$
\mathcal C^{p^q}+
\sum_{i<p^q}\sum_{j=0}^{J}
w_{ij}\mathcal A^{2p^q+j-2i}\mathcal C^i.
\tag{31}
$$

全部指数非负，原总次数至多 $2p^q+J$，
而仅首项贡献 $B^{p^q}$，系数为一。
乘 $\mathcal A^{2p^q}$ 后，原阶数增加 $2p^q$，
实际尺度增加 $\gamma^{2p^q}$。
这证明 (7)–(8)，没有把形式坐标的逆当成原有限源的免费换基。

最后核准最小权，避免 $q>1$ 的归一错误。
仍给 $X=a-1,Y=b,p$ 权 $r,p,R$。
对 $1\le i\le p^q$，

$$
v_p\binom{p^q}{i}=q-v_p(i),\qquad
i-(p-1)v_p(i)\ge1,
$$

后一个等号只在 $i=1,p$ 成立。
因此 $(1+X)^{p^q}-1$ 的最小权为 $r+qR$，
初始式为 $p^{q-1}(X^p+pX)$。
这里 $X^p$ 的单位常数准确由
$\binom{p^q}{p}/p^{q-1}=\binom{p^q-1}{p-1}\equiv1\pmod p$
给出。
另一方面，直接在原 $\gamma$ 尺度展开

$$
\frac{a(\gamma T)^{p^q}-1}{p^q\lambda}
=
\sum_{\ell\ge1}
\frac{(p^q\lambda)^{\ell-1}}{\ell!}
\left(\frac{t(\gamma T)}{\lambda}\right)^\ell
$$

可知只有 $\ell=1$ 留在约化中：
$\ell\ge2$ 的赋值为
$q(\ell-1)+(s_p(\ell)-1)/(p-1)>0$。
由 R177，约化是 $\tau T^r$，
其中 $\tau=p t_r\bmod p$。
故 (22) 的初始式准确为

$$
p^{q-1}(X^p+pX-\widetilde\tau Y^r).
\tag{32}
$$

$\widetilde\tau$ 可取任意 $\tau$ 的单位提升；
不同选择只改变更高权代表。
经 (4) 和 (28) 转回后，准备单位的常数模 $p$ 为一，
$c_0^{p^q-p}\equiv1\pmod p$，所以 (31) 的初始式为

$$
\boxed{\quad
p^{q-1}\mathcal A^{2p^q-2p}
\left(
\mathcal C^p+p c_0^{p-1}\mathcal C\mathcal A^{2p-2}
-c_0^p\widetilde\tau\mathcal A^{r+2p}
\right).
\quad}
\tag{33}
$$

其最小权为

$$
\boxed{\quad
\Omega_q=r+qR+2p^{q+1}.
\quad}
\tag{34}
$$

$q>1$ 时，虽然 $\mathcal P_{q,n}$ 首一于 $B^{p^q}$，
该首一项通常不在最小权部分；
不能据其 $B$ 次数把 (34) 替成
$p^q(r+2p)$。系数版的实际估计为

$$
v_p\!\left([s^m]\mathcal P_{q,n}
(\mathcal A(s),B(s))\right)
\ge\frac{\Omega_q-pm}{R}+n.
\tag{35}
$$

## 6. 与完整前缀问题的准确接口

本文给出任意深的原有限次数 primitive 源，
并同时保留完整精度及一个准确零前缀。
$Z$ 准备阶 $p^q$、清分母 $2p^q$、
系数截断 $J_{q,n}$ 都已计入真实次数。
因此可以在 R181 的实际源像中使用相应的首一伴随矩阵；
不需要把原源扩大成所有余式多项式。

但是，若所研究的原共同前缀长度大于
$D_{q,n}+1$，减去 $\mathcal P_{q,n}$ 的倍数仍可能改变旧行。
必须保留该倍数和余项的完整卷积条件。
这些关系不依赖两条中央导数共同消失，
单独不提供 R159 的严格全素数预算。
也未给任何固定有理源在无穷多个 $p$ 同时满足的新等式。

## 来源与依赖

- [R163 原全部惰性赋值](../notes/2026-11-12-actual-theta-inert-valuation-and-even-power-jet-resonance.md)，
  §2–3：本篇 (10)–(12) 的准确计数来源。
- [R177 完整 canonical AS 图](../notes/2026-11-12-full-depth-canonical-as-reduction-and-source-initial-form.md)，
  §1–3：原 $\gamma$ 整图、Wilson 全指数约化与真正尺度。
- [R178 原 theta 坐标与单层源](../notes/2026-11-12-original-theta-as-source-and-integral-correction.md)，
  §2–5：$c_0=374$、实际整逆、原清分母及准备单位的全部范围。
- [R180 多层原源](../notes/2026-11-12-original-theta-multiple-precision-source-polynomials.md)：
  本篇 $q=1$ 特例与准确前缀的相同规范。
- Mel Hochster，*The structure theory of complete local rings*，
  作者讲义，2026 年网页版本（PDF 未署成文年份），pp. 14–15，
  Weierstrass preparation theorem 及 monic-associate 推论：
  [已读作者原文](https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2026/04/Structure.pdf)。
  本篇使用环为 $\mathbb Z_p[[\mathcal A]]$、极大理想 $(p,\mathcal A)$；
  R178 §4 亦给了同一逐层除法证明。

[原 theta 全窗口有限校准](../scripts/check-theta-p-power-integral-window.py)
直接从有理 $t_m$ 生成 $a^{p^q}$：$p=7,q=1,2,3$ 及
$p=11,q=1,2$ 的全部首坏窗口、规范系数界与首坏余数均根端复算通过。
它们只作有限排错，完整证明为本文 (10)–(20)。

