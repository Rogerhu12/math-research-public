# 原 theta 有限次数源的多层 p 精度与实际 p 次幂尺度

日期：2026-11-12。
**状态：以下全系数尺度、准确整截断及原源 $p^n$ 改良已证明。**
本篇加强 R178 的单层关系，并支付次数加一的准确零前缀；
仍未把新多项式自动放进任意指定的更长前缀核。

## 1. 保持实际对象与原源

固定惰性 $p\equiv3\pmod4$、$p\ge7$、$p\ne11$，置

$$
r=(p+1)/4,\quad R=r(p-1),\quad
\varpi^R=p,\quad \lambda=\varpi^r,\quad\gamma=\varpi^p.
\tag{1}
$$

令 $K'=\mathbb Q_p(\varpi)$、$\mathcal O'=\mathcal O_{K'}$，
$\nu_\varpi(\varpi)=1$、$v_p=\nu_\varpi/R$。
仍取同一实际曲线上的

$$
a(s)=\exp t(s),\quad b(s)=sa(s),\qquad
t(s)=\sum_{m\ge1}t_ms^m,\quad
t_m=\frac1m\prod_{j=0}^{m-1}\frac{4j+1}{4j+3}.
\tag{2}
$$

原两条秩二 theta 输入是

$$
\mathcal A=A_2=a^{17}P(b/a),\qquad
B=a^{17}Q(b/a),\qquad
E_D^{\mathrm{orig}}=\mathbb Z_p[\mathcal A,B]_{\le D}.
\tag{3}
$$

$P,Q$ 为 R162 的固定多项式，满足
$P=s+O(s^2)$、$Q-P=-22s^2+O(s^3)$。
沿用 R178 的

$$
\mathcal C=B-\mathcal A+22\mathcal A^2,\qquad c_0=374,\qquad
Z=\mathcal C/\mathcal A^2.
\tag{4}
$$

$Z$ 在原 $X=a-1,Y=b$ 邻域中整且正则；
$(\mathcal A,Z)$ 是整形式坐标，
$Z_X(0)=c_0$、$\mathcal A_Y(0)=1$。
固定例外 $2,5,11,17$ 已在 R178 支付；所选惰性范围只额外删 $11$。
以下的准备多项式系数仅要求属于 $\mathbb Z_p$，不宣称有理性。

## 2. 实际 p 次幂的更大整尺度

R163 给

$$
v_p(t_m)\ge-1\quad(1\le m<p^2),
\qquad v_p(t_m)\ge0\quad(m<r),
\qquad v_p(t_r)=-1.
\tag{5}
$$

若 $p^h\le m<p^{h+1}$、$h\ge2$，
同一全系数定理给保守而足够的界
$v_p(t_m)\ge-(h+1)$。
因此

$$
\frac{p\,t(\varpi T)}{\lambda}\in\mathcal O'[[T]],
\qquad
\overline{\frac{p\,t(\varpi T)}{\lambda}}
=\tau T^r,\quad
\tau=p t_r\bmod p\ne0.
\tag{6}
$$

逐项核对如下。对 $m<r$，
$\nu_\varpi(p t_m\varpi^m/\lambda)\ge R+m-r>0$。
对 $r\le m<p^2$，(5) 给下界 $m-r$，只在 $m=r$ 等于零。
对 $m\ge p^2$，有

$$
\nu_\varpi(p t_m\varpi^m/\lambda)
\ge m-r-hR\ge p^h-r-hR>0.
\tag{7}
$$

最后一个式子在 $h=2$ 时由
$p^2-r-2R=(2p^2-p+1)/4>0$ 成立；
随后相邻差为 $(p-1)p^h-R>0$。
这也表明该下界随 $m$ 趋于无穷。
故 (6) 是全系数结论，唯一单位系数是 $m=r$。

令

$$
a(s)^p=\exp(p t(s))=\sum_{m\ge0}d_ms^m,\qquad d_0=1.
\tag{8}
$$

把 (6) 记为 $H(T)$。由

$$
\frac{a(\varpi T)^p-1}{\lambda}
=\sum_{j\ge1}\frac{\lambda^{j-1}}{j!}H(T)^j,\qquad
v_p\!\left(\frac{\lambda^{j-1}}{j!}\right)
=\frac{s_p(j)-1}{p-1}\ge0,
$$

得到

$$
\boxed{\quad
R\,v_p(d_m)+m\ge r\qquad(m>0).
\quad}
\tag{9}
$$

这是实际 $a^p$ 的系数界，不是把任意指数函数换入原问题。
特别

$$
d_m\in\mathbb Z_p\quad(0\le m<pr),\qquad
d_m\in p\mathbb Z_p\quad(1\le m<r),\qquad d_r\equiv\tau\pmod p.
\tag{10}
$$

最后一个同余也可从 R177 的指数约化直接读出。
完整地，Wilson 的相同分块计算给

$$
\overline{\frac{a(\varpi T)^p-1}{\lambda}}
=\tau\sum_{j\ge0}(-1)^jT^{rp^j}.
\tag{11}
$$

因此

$$
p d_{pr}\equiv-\tau\pmod p,\qquad v_p(d_{pr})=-1.
\tag{12}
$$

所以 (10) 的整截断上界 $m<pr$ 确实有实际首个失败项。
这里仅讨论形式级数的有界系数；没有声称可在任意单位 $T$
处对临界边界的无限级数作数值代入。

## 3. 保留全部分母的真实有限 ab 多项式

固定整数

$$
1\le n\le p-1,\qquad N_n=(n+1)r-1<pr.
\tag{13}
$$

用真实系数 (8) 定义

$$
\mathfrak J_{p,n}(a,b)
=a^{N_n+p}-\sum_{m=0}^{N_n}d_m a^{N_n-m}b^m
\in\mathbb Z_p[a,b].
\tag{14}
$$

所有指数非负；(10) 付清全部系数整性。
其次数至多 $N_n+p$，最高 $a^{N_n+p}$ 系数为一。

沿原曲线 $b=sa$，有准确恒等式

$$
\mathfrak J_{p,n}(a(s),b(s))
=a(s)^{N_n}\sum_{m>N_n}d_ms^m.
\tag{15}
$$

由 (9)，在 $s=\gamma T$ 下，每个尾项满足

$$
\begin{aligned}
\nu_\varpi(d_m\gamma^m)
&=\nu_\varpi(d_m\varpi^m)+(p-1)m\\
&\ge r+(p-1)m\\
&\ge r+(p-1)(N_n+1)=pr+nR.
\end{aligned}
\tag{16}
$$

R177 给 $a(\gamma T)=1+\lambda\,\mathcal O'[[T]]$，
所以乘其整数次幂不损失 (16)。
得到整个级数的实际精度

$$
\boxed{\quad
\lambda^{-p}\mathfrak J_{p,n}
(a(\gamma T),b(\gamma T))\in p^n\mathcal O'[[T]].
\quad}
\tag{17}
$$

在 $X=a-1,Y=b$ 的权
$\mathrm{wt}(X)=r,\mathrm{wt}(Y)=p,\mathrm{wt}(p)=R$ 下，
(14) 的最小权是 $pr$，初始式为

$$
X^p+pX-\widetilde\tau Y^r,
\tag{18}
$$

其中可取 $\widetilde\tau=d_r$。
确实 $a^p-1$ 只有 $X^p,pX$ 达到此权；
(10) 使 $m<r$ 的非恒项权大于 $pr$，$m>r$ 的项亦然。
乘 $a^{N_n}$ 不改初始式。
任意其他单位提升 $\tau$ 仅改变该初始式的高权代表。

## 4. 在实际原坐标中保持 p 次 Weierstrass 阶

使用 R178 已付的整形式逆
$(X,Y)=(X(\mathcal A,Z),Y(\mathcal A,Z))$，令

$$
\mathscr H_{p,n}(\mathcal A,Z)
=c_0^p\,\mathfrak J_{p,n}
\big(a(\mathcal A,Z),b(\mathcal A,Z)\big)
\in\mathbb Z_p[[\mathcal A,Z]].
\tag{19}
$$

取系数环
$\mathcal R=\mathbb Z_p[[\mathcal A]]$、
$\mathfrak m=(p,\mathcal A)$。
因 $(b)=(\mathcal A)$，在 $\mathcal A=0$ 时 $b=0$，并且
$a=1+c_0^{-1}Z+O(Z^2)$。
所以模 $(p,\mathcal A)$，

$$
\overline{\mathscr H_{p,n}}
=\bar c_0^{\,p}\bar a^{N_n}(\bar a-1)^p
=Z^p\cdot\text{常数项为一的形式单位}.
\tag{20}
$$

于是关于 $Z$ 的正则阶始终准确为 $p$，不随 $n$ 增长。
完备局部环 Weierstrass 准备给

$$
\mathscr H_{p,n}=S_{p,n}\mathscr W_{p,n},
\qquad
S_{p,n}\in\mathbb Z_p[[\mathcal A,Z]]^\times,
\tag{21}
$$
$$
\mathscr W_{p,n}
=Z^p+\sum_{i=0}^{p-1}w_{i,n}(\mathcal A)Z^i,
\qquad w_{i,n}\in(p,\mathcal A)\mathbb Z_p[[\mathcal A]].
\tag{22}
$$

这与 R178 使用的同一个标准定理及逐层除法完全相同。
在整个实际 $\gamma$ 缩放下，
$\mathcal A/\gamma,Z/\lambda\in\mathcal O'[[T]]$，
二者常数项为零，故 $S_{p,n}$ 的值及其逆均整且常数为单位。
由 (17)，

$$
\boxed{\quad
\lambda^{-p}\mathscr W_{p,n}
(\mathcal A(\gamma T),Z(\gamma T))
\in p^n\mathcal O'[[T]].
\quad}
\tag{23}
$$

这一步保留整个形式级数，而不只保留给定有限 jet。
系数只需在 $\mathbb Z_p$，无需宣称在 $\mathbb Q$。

给 $\mathcal A,Z,p$ 的权为 $p,r,R$，
(18)–(19) 的初始式准确为

$$
Z^p+p c_0^{p-1}Z-c_0^p\widetilde\tau\mathcal A^r.
\tag{24}
$$

比较 $Z^p$ 系数得 $S_{p,n}(0,0)\equiv1\pmod p$，
所以 $\mathscr W_{p,n}$ 有同一初始式。

## 5. 原源的显式精度—次数关系

令

$$
J_n=\left\lceil\frac{pr+nR}{p}\right\rceil-1
=(n+1)r-\left\lfloor\frac{nr}{p}\right\rfloor-1.
\tag{25}
$$

将 (22) 每个系数的 $\mathcal A$ 次数截到 $J_n$，
记为 $\mathscr W_{p,n}^{[J_n]}$。
任何被删单项在实际缩放后的权至少为

$$
p(J_n+1)\ge pr+nR.
\tag{26}
$$

因 $1\le n<p$ 且 $p\nmid r$，这里实际严格大于；
只需要非严格不等式即可保留 (23)。

定义

$$
\boxed{\quad
\mathcal P_{p,n}(\mathcal A,B)
=\mathcal A^{2p}
\mathscr W_{p,n}^{[J_n]}
\left(\mathcal A,\frac{B-\mathcal A+22\mathcal A^2}{\mathcal A^2}\right).
\quad}
\tag{27}
$$

若 $w_{i,n}=\sum_j w_{ij,n}\mathcal A^j$，则

$$
\mathcal P_{p,n}
=\mathcal C^p+
\sum_{i=0}^{p-1}\sum_{j=0}^{J_n}
w_{ij,n}\mathcal A^{2p+j-2i}\mathcal C^i.
\tag{28}
$$

所有 $\mathcal A$ 指数非负。
每项的原总次数至多 $2p+j$，而仅 $\mathcal C^p$ 可贡献 $B^p$。
因此

$$
\boxed{\quad
\mathcal P_{p,n}\in E_{D_{p,n}}^{\mathrm{orig}},\quad
D_{p,n}=2p+(n+1)r-\left\lfloor\frac{nr}{p}\right\rfloor-1,
\quad [B^p]\mathcal P_{p,n}=1.
\quad}
\tag{29}
$$

它是原有限次数整源的 primitive 元。
其规范初始权仍为 $\Omega=p(r+2p)$，初始式仍是 R178 的

$$
\mathcal C^p+p c_0^{p-1}\mathcal C\mathcal A^{2p-2}
-c_0^p\widetilde\tau\mathcal A^{r+2p}.
\tag{30}
$$

由 (23)、(26)，乘
$(\mathcal A(\gamma T)/\gamma)^{2p}$ 后得到

$$
\boxed{\quad
\frac{\mathcal P_{p,n}
(\mathcal A(\gamma T),B(\gamma T))}
{\lambda^p\gamma^{2p}}
\in p^n\mathcal O'[[T]],
\qquad1\le n\le p-1.
\quad}
\tag{31}
$$

也即全部实际系数满足

$$
v_p\!\left([s^m]\mathcal P_{p,n}(\mathcal A(s),B(s))\right)
\ge\frac{\Omega-pm}{R}+n.
\tag{32}
$$

两个端点明确为

$$
D_{p,1}=(5p-1)/2,\qquad
D_{p,p-1}=2p+R.
\tag{33}
$$

所以原源在次数至多 $2p+R$ 已有相对于同一个初始权
$\Omega$ 的 $p^{p-1}$ 改良。
不声称 $n$ 继续增大时仍能不变地使用本构造；
(12) 说明原 $d_m$ 在 $m=pr$ 确实出现分母。

此外，该同一多项式确实有一个已付清的原准确零前缀：

$$
\boxed{\quad
\operatorname{ord}_{s=0}
\mathcal P_{p,n}(\mathcal A(s),B(s))
\ge D_{p,n}+1.
\quad}
\tag{34}
$$

由 (15)，$\mathfrak J_{p,n}$ 沿原图的阶至少为 $N_n+1$；
Weierstrass 单位在该图上常数为单位，故
$\mathscr W_{p,n}$ 保持同一阶。
删去的系数项都是 $\mathcal A^jZ^i$，其中 $j\ge J_n+1$；
沿原图 $\mathcal A,Z\in s\mathbb Q_p[[s]]$，
所以删项的阶至少为 $J_n+1$。
又 $J_n=N_n-\lfloor nr/p\rfloor\le N_n$，
从而截断后的 $\mathscr W_{p,n}^{[J_n]}$ 阶至少为 $J_n+1$。
最后 $\operatorname{ord}_s\mathcal A=1$，
清分母所乘的 $\mathcal A^{2p}$ 给出
$2p+J_n+1=D_{p,n}+1$，证明 (34)。
这项准确前缀与 (31) 的全系数精度同时成立。

## 6. 此结论没有省去的原前缀任务

(31) 是原 $\mathbb Z_p[A_2,B]$ 的真实有限次数结论，
不依赖两条中央导数共同为零。
它提供逐 $p$ 可构造的整多项式族；
这些系数在 $\mathbb Z_p$，并非同时作用于所有 $p$ 的固定
有理多项式族。

虽然 (34) 已支付长度 $D_{p,n}+1$ 的准确零前缀，
把一个更长准确零前缀的 $P$ 减去 $\mathcal P_{p,n}Q$，
仍可能改变此前的零行。
因此全精度关系和相应余项须一同保留在原饱和前缀矩阵，
不能把 (31) 直接读成所有 $\varphi_{D,k}$ 的改良。
主目标的无穷非零及 R159 的严格总预算仍需新的共同核论证。

## 来源与依赖

- [R163 实际全系数赋值](2026-11-12-actual-theta-inert-valuation-and-even-power-jet-resonance.md)：
  §2–3 的准确计数，给 (5)、(7) 的全部范围。
- [R177 全深 AS 约化](2026-11-12-full-depth-canonical-as-reduction-and-source-initial-form.md)：
  原 $\gamma$ 整图与指数全部 $p$ 次幂项；本篇在更大的
  $\varpi$ 尺度对实际 $a^p$ 重新证明整性。
- [R178 原 AS 源及单层修正](2026-11-12-original-theta-as-source-and-integral-correction.md)：
  $374$、真实 $(\mathcal A,Z)$ 坐标、原清分母及次数规范。
- Mel Hochster, *The structure theory of complete local rings*，
  作者讲义，2026 年网页版本（PDF 未署成文年份），pp. 14–15，
  Weierstrass preparation theorem 及 monic-associate 推论，
  [已读作者原文](https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2026/04/Structure.pdf)。
  使用环准确为 $\mathbb Z_p[[\mathcal A]]$、极大理想 $(p,\mathcal A)$；
  R178 §4 已给同一逐层除法构造。
