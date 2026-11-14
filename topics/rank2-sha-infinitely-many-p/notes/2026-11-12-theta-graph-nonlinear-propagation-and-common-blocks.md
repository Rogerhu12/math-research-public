# 真实 theta 图的首共振传播与全部源的共同次数块

日期：2026-11-12。**状态：以下全源公式、第一完整非线性带的整性及
准确主项均已证明。** 目标仍是原普通系数的饱和 jet。本文不把某个
非零 Taylor 系数当作该饱和 jet 的范数下界，也不把首共振数目乘以
源次数就当作已付的全精度成本。

## 1. 原闭合平面的真正图参数

在 $E_0:y^2=x^3-x$ 上保留
$$
 s=u^4=x^{-2},\qquad a=\vartheta^4,\qquad b=\sigma^4=sa,
 \qquad t(s)=\log a(s)=W(s)/17.
 \tag{1}
$$
这里 $a(0)=1$，$b(z)=z^4+\cdots$。由 R162，
$$
 [s^m]t(s)=\frac1m\prod_{j=0}^{m-1}\frac{4j+1}{4j+3}.
 \tag{2}
$$
写 $b=s e^{t(s)}$ 的形式逆为 $s=s(b)$，并置
$$
                       f(b)=a(s(b)).
 \tag{3}
$$
于是原形式曲线准确是 $(a,b)=(f(b),b)$。
从 $w=z^4$ 换到 $b$，首系数为一；因此所有准确前缀核及其
首非零系数相同。这一饱和 jet 等距不要求逆级数的其余系数整。

源可取 $a^jb^i$、$i+j\le D$。它与 $(a-1)^jb^i$ 的标准源格
仅差一个整幺三角换基，不改变任一局部系数最大范数。

## 2. 全部列共用的完整特征零公式

令
$$
 M_{k;i,j}=[b^k]b^if(b)^j,\qquad n=k-i,\qquad d=i+j.
$$
当 $n<0$ 时值为零，当 $n=0$ 时值为一。
$j=0,n>0$ 时值为零。对于其余情形，Lagrange 反演给
$$
 \boxed{\quad
 M_{k;i,j}=
 \begin{cases}
 \displaystyle\frac{j}{d-k}[s^{k-i}]
                 \exp((d-k)t(s)),&d\ne k,\\[5pt]
 \displaystyle j[s^j]t(s),&d=k.
 \end{cases}
 \quad}\tag{4}
$$
确实，$[b^n]f^j=(j/n)[s^{n-1}]a'a^{j-n-1}$。
若 $j\ne n$，对 $a^{j-n}$ 微分后提取系数，得到
$j/(j-n)[s^n]a^{j-n}$；若 $j=n$，它准确变为
$j[s^j]\log a$。这同时证明了 (4) 的例外项，不能在 $d=k$
处硬除零。

特别，在固定总次数 $d$ 的全部列中，指数始终是同一个
$d-k$。原 $j$ 及取系数阶 $k-i$ 仍保留；本式不是逐列另选
一个不同的连接。

## 3. 第一完整非线性带上的统一整性

固定惰性 $p=4r-1\ge7$。由 R160 的全计数，
$$
 t_m\in\mathbb Z_p\quad(m<r),\qquad
 v_p(t_m)\ge-1\quad(m<p^2),\qquad
 \tau_p:=p t_r\bmod p\in\mathbb F_p^\times.
 \tag{5}
$$
这里 $\tau_p=C_p/(17r)$，与 R160 的 $C_p$ 规范完全相同。
因为 $pr<p^2$，以下整个截断都可使用 (5)。写
$$
 t=t_{<r}+\frac{T_p}{p}\pmod{s^{pr}},\qquad
 t_{<r}\in s\mathbb Z_p[s],\quad
 T_p\in s^r\mathbb Z_p[[s]],\quad [s^r]T_p\equiv\tau_p.
 \tag{6}
$$
这里 $T_p$ 的整性仅需到显示的截断，不声称它在所有次数整。

**统一界。** 对每个整数 $j\ge0$ 及 $0\le n<pr$，
$$
 \boxed{\qquad
       v_p([b^n]f(b)^j)\ge-\lfloor n/r\rfloor.
 \qquad}\tag{7}
$$
证明保留 (4) 的分母。令 $h=\lfloor n/r\rfloor<p$，
$c=j-n$。先设 $p\nmid c$。在
$$
 e^{ct}=e^{c t_{<r}}\sum_{q=0}^{h}
                   \frac{c^qT_p^q}{p^q q!}\pmod{s^{n+1}}
 \tag{8}
$$
中，所有 $q!$ 均为单位。积分指数级数 $e^{c t_{<r}}$ 的第 $m$
系数赋值至少为 $-\lfloor m/(p-1)\rfloor$，直接来自其指数展开。
若 $q<h$，写 $n=hr+e$、$0\le e<r$，则
$$
 \left\lfloor\frac{n-qr}{p-1}\right\rfloor
 =\left\lfloor\frac{r(h-q)+e}{4r-2}\right\rfloor
 \le h-q-1.
 \tag{9}
$$
所以该项赋值至少 $-h+1$。$q=h$ 的剩余次数小于 $r<p$，
没有额外阶乘分母，赋值至少 $-h$。再乘 $j/c$ 不降低此界。
$h=0$ 时直接使用所有所需阶乘均小于 $p$。

若 $p\mid c$ 且 $c\ne0$，令 $e_c=v_p(c)\ge1$。
$e^{c t_{<r}}$ 的每个非恒定系数在 $p^{e_c}\mathbb Z_p$；
(8) 的另一因子在所需次数的每个非恒定系数至少属于
$p^{e_c-1}\mathbb Z_p$，因为 $q<p$。
除以 $c$ 后下界是 $-1$，足以处理 $h\ge1$。
$h=0$ 时前述低次数展开直接给整性。
最后 $c=0$ 时使用 (4) 的 $j t_j$，由 (5) 得到同一界。
这证明 (7) 对全部源列同时成立。

因此对于原 $ab$ 源的真正饱和 jet，至少有合法的第一带上界
$$
 \boxed{\qquad
 \log\|\varphi_D^k\|_p\le\lfloor k/r\rfloor\log p
                 \qquad(0\le k<pr).
 \qquad}\tag{10}
$$
这是先估计同一整个整源，再限制到实际前缀核，因而没有核的
替换。(10) 只覆盖显示的有限带，且未提供所需的严格全局预算。

## 4. 每个整带起点的准确共同主项

对任意 $j\ge0$ 及 $1\le h<p$，(4)–(9) 进一步给
$$
 \boxed{\qquad
 p^h[b^{hr}]f(b)^j
 \equiv
 \frac{j(j-hr)^{h-1}}{h!}\tau_p^h\pmod p.
 \qquad}\tag{11}
$$
$h=1$ 时指数零按一处理，包括 $j=hr$。

若 $c=j-hr$ 为单位，(9) 证明 $q<h$ 的所有项严格高一层。
$q=h$ 只能从每个 $T_p$ 取其首项，故它是
$c^h p^{-h}\tau_p^h/h!$；乘 $j/c$ 后得到 (11)。
若 $p\mid c$，第3节给 $[b^{hr}]f^j$ 的赋值至少为 $-1$，
所以 $h\ge2$ 时两边均为零。
当 $h=1$ 时，$q=1$ 的首项给 $j\tau_p$；其余项乘 $p$ 后消失。
$c=0$ 的例外项 $j t_j$ 亦准确给同一结论。

所以 (11) 不排除 $j-hr$ 被 $p$ 除的情形，也没有误将这些
位置称为单位。对原列 $a^jb^i$，将行号改为 $k=i+hr$ 即可
使用同一个公式。

取实际坐标本身 $j=1$。因为 $4r=p+1$，在 $1\le h<p$ 中
$1-hr\equiv0\pmod p$ 恰好发生在 $h=4$。于是
$$
 \boxed{\quad
 v_p([b^{hr}]f)=-h\quad(1\le h<p,\ h\ne4),
 \qquad v_p([b^{p+1}]f)\ge-1.
 \quad}\tag{12}
$$
特别
$$
 p^2[b^{2r}]f\equiv\frac14\tau_p^2\ne0\pmod p.
 \tag{13}
$$
故即使减去全部 $<r$ 的整项以及首个 $p^{-1}b^r$ 项，真实图
在 $b^{2r}$ 仍有一个精确的 $p^{-2}$ 系数。非线性传播一直
出现在下一个 Gaussian 共振 $r+(p^2-1)/4=pr$ 之前。
这给逐共振消元必须保留的实际成本，不排除通过有完整格证明的
进一步非线性坐标变换来支付它。

### 4.1. 整个第一带的共同主行，而非仅带起点

保留 R169 的真正第一类周期
$$
 \mathcal L(s)=\sum_{e\ge0}
       \frac{\binom{2e}{e}}{4^e(4e+1)}s^e.
$$
在准确的低次数范围内有
$$
 \boxed{\qquad
 T_p(s)\equiv\tau_p s^r\mathcal L(s)
                         \pmod{p,s^{2r}}.
 \qquad}\tag{14}
$$
确实，R160 的导数式给
$p t'(s)\equiv(C_p/17)s^{r-1}(1-s)^{2r-1}\pmod{p,s^p}$。
对 $0\le e<r$ 积分时 $r+e<p$，所以没有额外的 $p$ 分母，且
$$
 \frac{[s^{r+e}]T_p}{\tau_p}
 \equiv(-1)^e\binom{2r-1}{e}\frac r{r+e}
 \equiv\frac{\binom{2e}{e}}{4^e(4e+1)}\pmod p.
$$
最后一个分母在显示范围内是单位。(14) 仅使用所需低 jet，
不把全部周期的模 $p$ 约化任意截成一个固定多项式。

令 $n=hr+e$，其中 $1\le h<p$、$0\le e<r$，并令 $c=j-n$。
第 3 节的严格一层余量与 (14) 给出完整式
$$
 \boxed{\quad
 p^h[b^{hr+e}]f(b)^j\equiv
 \frac{j c^{h-1}\tau_p^h}{h!}
       [s^e]a(s)^c\mathcal L(s)^h\pmod p.
 \quad}\tag{15}
$$
右侧只使用 $a$、$\mathcal L$ 到 $e<r$ 的整系数。
若 $p\nmid c$，指数展开中唯一可留下的项是 $q=h$；将
$T_p^h$ 的低 jet 换成 $\tau_p^h s^{hr}\mathcal L^h$ 即得。
若 $p\mid c$ 且 $h\ge2$，第 3 节的 $-1$ 下界使两侧均为零。
当 $h=1$ 时，$a^c\equiv1\pmod{p,s^r}$，直接保留 $q=1$
给出同式；$c=0$ 的对数例外亦由 (14) 给出同式。
因此 (15) 保留了全部共振例外，没有在 $c=0$ 处作非法除法。

更适合整源的是如下写法。设 $H(a,b)=a^d R(b/a)$ 是一个
整系数、总次数 $d$ 的齐次源多项式，令 $k=hr+e$ 如上，则
$$
 \boxed{\quad
 p^h[b^k]H(f(b),b)\equiv
 \frac{\tau_p^h(d-k)^{h-1}}{h!}
 [s^e]a(s)^{d-k}\mathcal L(s)^h
                         \bigl(dR(s)-sR'(s)\bigr)\pmod p.
 \quad}\tag{16}
$$
因为 $R_i s^i$ 对应列 $a^{d-i}b^i$，$i\le e$ 时可用 (15)，
其 $c=d-k$ 与 $i$ 无关。若 $i>e$，该列的系数已由 (7)
落在较低分母层，乘 $p^h$ 后为零。因此整块恰是 (16)，
而不是逐列选择不同 gauge。

对于原平面基 $A_2^j V^c$，在 (16) 中准确取
$d=17j$、$R=P(s)^jV(s)^c$。当 $j+c>e$ 时，右侧自动为零。
这只是同一全列主行的支撑限制，仍未证明真实前缀把其余
高阶功能全部消掉。式 (16) 可用于进一步的共同前缀消元，
不能单独代替饱和格证明。

## 5. 与原两中央条件及有限校准的关系

R169 的两中央首层只读
$Z/(\sqrt{1-s}\mathcal L^2)$ 到 $s^{r-1}$。
本篇的 $\tau_p$ 则由 $t_r$ 给出，R160 已证明它始终是单位。
因此不能把原两条中央零性直接称为 $ab$ 平面首径向共振消失。

同时，(12) 是一个指定坐标的系数断言。这个坐标没有位于
$b^{hr}$ 阶的前缀核中，故 (12) 不能用来反向断言原饱和
$\varphi_D^{hr}$ 必有某个范数。可用于所有前缀的是 (10) 的上界，
不是将 (12) 当作下界。

原 $A_2,B$ 是 $a,b$ 的固定齐次十七次多项式：
$$
 A_2=a^{17}P(b/a),\qquad B=a^{17}Q(b/a).
$$
在好惰性位，将它们代入一个整系数的次数 $D$ 源多项式，
仍得到整系数的 $ab$ 多项式，次数至多 $17D$。
所以 (10) 亦给原平面的同一第一带上界；这个包含关系不被
称为两个完整源格的等距或同构。

[准确脚本](../scripts/check-theta-graph-first-propagation.py) 从
$b=s e^t$ 真正逆级数计算 $f(b)=b/s(b)$，独立核对 (4)、(11)。
默认只验证 $p=7,11$ 的所有 $n<pr$、整个 $hr+e$ 带及
$j=0,1,2,3,5,17,34$。
例如 $j=1$ 的赋值分别为
$$
 \begin{array}{c|l}
 p=7&-1,-2,-3,-1,-5,-6\\
 p=11&-1,-2,-3,-1,-5,-6,-7,-8,-9,-10.
 \end{array}
$$
这校准了 $h=4$ 的例外，且没有扩成跨素数数值结论。

## 来源

- R162 的固定整数流与 $W$ 精确系数：
  [两 theta 行的非线性方程](2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。
- R160 的一层估值在整个 $m<p^2$ 的范围：
  [首进位与全列谱](2026-11-12-inert-theta-carry-and-common-degree-spectrum.md)。
- R169 的原中央低 amplitude：
  [联合中央行与完整周期](2026-11-12-joint-central-amplitudes-and-period-frobenius.md)。
- (4)、(7)、(11) 是本篇在原全部列上的直接推导，不调用未付的
  饱和格迭代，也不将非线性图误当一条有理常系数递推。
