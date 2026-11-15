# R721 — 原高度二整参数的最小二挠极帽

日期：2026-11-15。**状态：以下显式有理参数、完整原整窗比较、同类极帽最小性及全部首 Cartier 返回已证明。**
最小性仅指本篇明确的“只在原二挠点有极、原六次型、同一微分及完整原整窗”参数类，不冒更大来源类。

保持原 $E:y^2=x^3+b$、$b=17$，
$$
p=6s-1>101,\qquad q=p^2,\qquad L=(q-1)/6,\qquad
\omega_E=\frac{dx}{2y},\quad D=\frac d{\omega_E}.
$$
第三原来源 $m=136$ 继续保其 $p>136$ 条件。
令 $\mathcal D_2$ 为三个非零二挠点之和。
原点规范仍为 $x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$。

## 1. 全部原输入与一个固定形状的短函数

沿用 R636/R714 的同一个有理来源
$$
Z=\frac{\mathscr R_p(x)}{y^p},\qquad
G=\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!},
\qquad r=\frac{x^2}{y},\qquad H=G+r.
$$
已付的准确等式是
$$
DZ=1,\quad DG=-x+c_pZ^{p-1},\quad
c_p=\binom{3s-1}{2s-1}b^s\in k^\times ,
$$
$$
H=\frac{3b}{5}z^5+O(z^{11}),\qquad
Z_1=Z+c_p^{-1}H^p=z+O(z^q).
\tag{1}
$$
末式是在 R714 已付的完整整截断中比较；
不把全特征零形式对数无限约化。
原 $Z$ 在 $\mathcal D_2$ 单点极阶至多 p，除此无极。

定义原有理不变量
$$
\xi=\frac b{y^2}=\frac b{x^3+b}.
$$
它在 O 从 $bz^6$ 起，在每个非零二挠点有二阶极。
直接求导给
$$
D\xi=-6r\xi,\qquad Dr=x(1+3\xi),\qquad r^2=x(1-\xi).
\tag{2}
$$

取以下明确的剩余域系数：
$$
a_1=-\frac35,\qquad
a_j=\frac{6j-3}{6j-1}a_{j-1}\quad(2\le j\le s-1).
\tag{3}
$$
全部分子、分母在当前 p 处为单位。
特别 $a_{s-1}\ne0$。令
$$
\boxed{\quad
h_p=r\sum_{j=1}^{s-1}a_j\xi^j
 =\frac{x^2}{y}\sum_{j=1}^{s-1}a_j
                      \left(\frac b{y^2}\right)^j .
\quad}
\tag{4}
$$
它在 O 正则，在曲线上除此只可能于 $\mathcal D_2$ 有极；
因末系数为单位，三个二挠点的极阶都准确为 $2s-1$。

### 1.1 它匹配同一个 H 的全部 p 以下行

$H$ 和 r 均为 $\mu_6$ 型 $-1$，故 $H/r$ 在 O 是
$\xi k[[\xi]]$ 中的实际级数。
由 (1)、(2)，
$$
DH=3x\xi+c_pZ^{p-1}.
$$
另一方面，对 $rF(\xi)$ 有完整式
$$
D(rF)=x\{(1+3\xi)F-6\xi(1-\xi)F'\}.
\tag{5}
$$
$Z^{p-1}/x$ 在 O 的阶为 $p+1=6s$，
所以它作为不变量的展开从 $\xi^s$ 起。
因此 $F=H/r$ 的前 $s-1$ 行满足
$$
(1-6j)[\xi^j]F+(6j-3)[\xi^{j-1}]F
 =3\,1_{j=1}\quad(1\le j<s).
$$
这些全是单位行，恰给 (3)。
于是
$$
\boxed{\qquad H-h_p=O(z^p).\qquad}
\tag{6}
$$
这里不仅用了首项；全部原 $z^{6j-1}<z^p$ 行已同时匹配。
没有改变原 H 或原 Gaussian 的规范。

## 2. 显式低极帽参数

定义
$$
\boxed{\qquad \widehat Z=Z+c_p^{-1}h_p^p.\qquad}
\tag{7}
$$
因为 $D(h_p^p)=0$，
$$
D\widehat Z=1,\qquad d\widehat Z=\omega_E.
\tag{8}
$$
由 (1)、(6)，
$$
\widehat Z-Z_1=c_p^{-1}(h_p-H)^p=O(z^{p^2}).
$$
所以完整原整窗不变：
$$
\boxed{\qquad \widehat Z=z+O(z^q).\qquad}
\tag{9}
$$
$\widehat Z$ 为原 $\mu_6$ 型 $+1$，
因为 $h_p$ 型为 $-1$ 且 $p\equiv-1\bmod6$。

(4) 的准确极阶和原 Z 的较低极阶给
$$
\boxed{\qquad
(\widehat Z)_\infty=M_p\mathcal D_2,\qquad
M_p=p(2s-1)=\frac{p(p-2)}3.
\qquad}
\tag{10}
$$
这里 $M_p>p$，故两项没有最高极阶相消。
相比 R714 的 $(p^3-p^2)\mathcal D_2$ 上界，
(10) 降低一整个 p 阶，而 (8)、(9) 完全保持。

(7) 只使用原 Z 和显示的 $s-1$ 个单位递推。
它不依赖原 sigma 的未知第二位，也不增加任何数值执行假设。

## 3. 在明确的原参数类中最小

考虑任一 $V\in k(E)$，满足：

- $dV=\omega_E$；
- V 为 $\mu_6$ 型 $+1$，只在 $\mathcal D_2$ 有极；
- 在同一原整窗口中 $V=z+O(z^q)$。

**定理。** 这样的 V 在每个非零二挠点的极阶至少为 $M_p$。
因此 (7) 达到这个参数类的最小极帽。

证明先用 $DZ=1$。
$Z$ 是 $k(E)/k(E)^p$ 的 p-基；特别
$$
\ker(D:k(E)\longrightarrow k(E))=k(E)^p.
$$
这也可直接在基 $1,Z,\ldots,Z^{p-1}$ 上求导验证。
故存在唯一 f，使
$$
V-Z=c_p^{-1}f^p.
\tag{11}
$$
完美剩余域中的常数 p 次根包含在这个表达中。
由型和除子，f 为型 $-1$，只在 $\mathcal D_2$ 有极，并在 O 正则。
又由 V 与 $Z_1$ 的原窗比较，
$$
f-H=O(z^p).
\tag{12}
$$

所有具有上述型和极支持的 f 都准确形如
$$
f=rP(\xi),\qquad P\in k[\xi],\quad P(0)=0.
\tag{13}
$$
为支付这条全局分类，$f/r$ 为 $\mu_6$ 不变量，
故属于 $k(x^3)=k(\xi)$。
在 O，r 有一阶极，所以 $P$ 在 $\xi=0$ 至少一阶零。
在 $x=0$ 的两个点，r 的零阶为二，
而 $\xi-1$ 的零阶为三；
因此 $P$ 不能在 $\xi=1$ 有极，否则 f 仍有极。
其它有限 $\xi$ 处 r 非零，也不能有极。
唯一允许的极为 $\xi=\infty$，所以 P 为多项式。
这证明 (13)，没有遗漏在 $x=0$ 可被 r 消去的极项。

(12) 与第1节的单位三角式要求
$$
[\xi^j]P=a_j\quad(1\le j<s).
$$
$a_{s-1}$ 为单位，故 $\deg P\ge s-1$。
由 (13)，f 在每个二挠点的极阶至少 $2s-1$。
于是 (11) 的第二项极阶至少 $p(2s-1)>p$，
不能被原 Z 抵消。这证明最小性。

本定理不允许增添其它极点、改变原型或缩短原窗口；
在这些更大类别中没有宣称同一最小界。

## 4. 原整个 sigma 整窗的有理返回及新总极帽

令 $U_{\rm AH}\in k[w]_{<L}$ 为 R717 的**实际**原 U 截断；
它可用 R718 的完整 division 输入恢复。
R720 的两固定低度来源仅恢复其已证明的较短窗口，
不能在此免费冒充全部 $n<L$ 输入。

定义
$$
\widehat\Sigma=\widehat Z\,U_{\rm AH}(\widehat Z^6),
\qquad
\widehat A_m=\widehat\Sigma^{\,m}\phi_m,
\quad m=34,72,136,
\tag{14}
$$
其中 $\phi_m$ 是原完整多项式来源。
由 (9) 与 R717 的原整截断，
$$
\widehat\Sigma=\sigma^\circ+O(z^q),\qquad
\widehat A_m=(\sigma^\circ)^m\phi_m+O(z^{q+5}).
\tag{15}
$$
第二式保原 $\phi_m$ 在 O 的极阶 $m-6$。
它不在其它点引入极，因为原 $\phi_m$ 是同一 x、y 多项式。

$1+6(L-1)=q-6$，所以
$$
\boxed{\qquad
(\widehat A_m)_\infty
 \le m(q-6)M_p\mathcal D_2
 =m(q-6)p(2s-1)\mathcal D_2.
\qquad}
\tag{16}
$$
在 O，$\widehat A_m$ 从 $z^6$ 起，没有额外原点极。
(16) 取代 R717 的
$m(q-6)(p^3-p^2)\mathcal D_2$ 上界；
所有实际高系数和原 $\phi_m$ 仍在。

## 5. 全部原首 Cartier 行与其它零点

由 (8)，$\widehat Z$ 的每个零点都是单零：
若其零阶大于一，$d\widehat Z$ 不可能在该点为非零正则微分。
因此
$$
\deg(\widehat Z)_0=3M_p,\qquad
(\widehat Z)_0-O\text{ 为有效除子}.
$$
这些其它零点继续明确保留。

对 $1\le h\le p-1$，置
$$
\Theta_{m,h}=\widehat Z^{-h-1}\widehat A_m\omega_E,\qquad
\rho_{m,h}=\operatorname{Res}_O\Theta_{m,h}.
$$
在 O，输入的极阶至多 $h-5<p$，
故 Cartier 后最多有一个简单极。
定义准确有限部
$$
B_{m,h}
 =\frac{\mathscr C(\Theta_{m,h})}{\omega_E}
       -\frac{\rho_{m,h}^{1/p}}{\widehat Z}.
\tag{17}
$$
这是在 O 正则的实际有理函数。
局部 Cartier 公式、$D\widehat Z=1$ 及 (15) 给
$$
\boxed{\qquad
\bar g_{m,h}
=\left(\frac{D^{h-1}B_{m,h}(O)}{(h-1)!}\right)^p,
\qquad 1\le h\le p-1.
\qquad}
\tag{18}
$$
它读取的指数是 $h(p+1)\le p^2-1$，
严格位于 (15) 已付窗口内。
全部阶乘为单位，且减去的是原实际留数，
不是另定一个 Gaussian 常数。

整个输入的极支持也可完整控制：
$$
\begin{aligned}
(\Theta_{m,h})_\infty\le{}&
 (h-5)_+O\\
&+\{m(q-6)-h-1\}M_p\mathcal D_2\\
&+(h+1-m)_+\{(\widehat Z)_0-O\}.
\end{aligned}
\tag{19}
$$
因为 $\widehat\Sigma$ 在每个 $\widehat Z=0$ 处至少一阶零，
原 $\phi_m$ 除 O 外正则。
在 $\mathcal D_2$，$\widehat\Sigma^m/\widehat Z^{h+1}$
的最高可能幂为 $m(q-6)-h-1$；
这些数对当前 h 都非负。
这证明 (19)，包括所有额外零点的真实代价。

尤其 $h+1\le m$ 时，(19) 的第三项准确不需要；
更高 h 则不能删去它。
R718(21) 的原 Fermat 商 Cartier 观察也可把 $Z_1$ 换成
$\widehat Z$，因其只读第 p 行，而 (9) 已支付全部坐标误差。
其中 division 核上的实际极和所有 $\widehat Z$ 零点仍保。

## 6. 对主问题的准确收益

本篇减少的是原有理参数及完整 sigma 模型的真实全局极帽，
并证明该受限参数类的最优性。
所有原第二位、Gaussian 规范和同一个原来源完全保持。

它没有把 (16) 的随 p 增长的来源自动加入旧 $\mathcal W_D$，
没有从 Cartier 返回推出指定条目非零，
也没有证明原 $j_m=0$ 迫 R708 的逐行前缀零。
原同 R、两十三行 carry、全中央进位和固定曲线无穷 p 的目标继续。

依赖：
[R636](R636-original-rational-cartier-return-for-two-critical-rows.md)；
[R714](R714-original-height-two-rational-parameter-and-full-first-cartier-window.md)；
[R717](R717-original-height-two-artin-hasse-return-and-second-digit-support.md)；
[R718](R718-original-cm-distribution-and-unique-gaussian-resonance.md)；
[R720](R720-two-fixed-cm-sources-and-density-one-resonance-window.md)。
