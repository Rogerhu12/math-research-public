# 整 Euler–Cartan 行与原两中央条件的真实前缀收益

日期：2026-11-12。**状态：以下共同有限精度行、轴比较及指定饱和行
的改进均已证明。** 本文保留原次数 $D$ 的全部混合列。
中央条件确实在第 5 节多消去一层 $p$，但所得是一族指定行，
尚不是 R159 要求的严格全阶预算。

## 1. 原源和同一整矩阵

固定惰性 $p=4r-1\ge7$，$R=r(p-1)$。沿用 R174 的同一
整 Cartan 坐标 $U,V$，以及实际输出参数 $v=V(w)$：

$$
 U=u_0v^r+O(v^{pr}),\qquad
 v_p(u_0)=-1,\qquad
 \pi_0=u_0^{-1}\in p\mathbb Z_p^\times,\qquad
 \tau_p=pu_0\bmod p\ne0.
 \tag{1}
$$

对原整源 $H$，记其在同一整逆中的 Taylor 泛函为

$$
 \widetilde H(U,V)=\sum_{h,j\ge0}L_{h,j}(H)U^hV^j.
$$

对 $k=rh+j<pr$、$0\le j<r$，准确有

$$
 [v^k]H(\gamma_v)=u_0^h\Lambda_{h,j}(H),\qquad
 \Lambda_{h,j}=\sum_{q=0}^{h}\pi_0^qL_{h-q,j+rq}.
 \tag{2}
$$

所有 $L$、$\Lambda$ 都是同一原源上的整线性泛函；
本文没有把各列独立换坐标。

本文的主要有限源是
$$
 E_D=\mathbb Z_p[\mathcal A,\mathcal B]_{\le D},
 \qquad \mathcal A=A_2,\quad \mathcal B=B.
$$
它的次数 $m$ 齐次部分 $H_m$ 在 $a,b$ 中准确齐次
$d_m=17m$。$\mathcal A,\mathcal B$ 均被 $b$ 整除；
所以 $m\ge1$ 时 $H_m$ 在 $b=0$ 上恒为零。
若 $H$ 位于任意正阶的实际前缀核，其常数部分 $H_0$ 已经为零。

## 2. Euler 作用的整字符和首个误差

令
$$
 E=a\partial_a+b\partial_b.
$$
R170 的 $F_\alpha$ 齐次次数为 $d=N\alpha$，故
$E(f\circ F_\alpha)=d(Ef)\circ F_\alpha$。
对 R174 的有限 Teichmüller 群，用
$U\circ F_\alpha=dU$、$V\circ F_\alpha=\alpha^4V$，得到

$$
 (EU)\circ F_\alpha=EU,\qquad
 (EV)\circ F_\alpha=\alpha^{4-(p+1)}EV.
 \tag{3}
$$

由于环境坐标变换和 $E$ 都整，$EU,EV\in\mathbb Z_p[[U,V]]$。
在单项式 $U^hV^j$ 上的字符是 $rh+j\bmod R$。
$EU-1$ 的首个可能正次数至少为 $p-1$，且该次唯一单项式为
$U^{p-1}$；$EV$ 的首个可能次数也为 $p-1$，唯一单项式为
$U^{p-2}V$。因此

$$
 E=\bigl(1+O((U,V)^{p-1})\bigr)\partial_U+
                  O((U,V)^{p-1})\partial_V.
 \tag{4}
$$

若 $H$ 在 $a,b$ 中齐次次数 $d$，则 $EH=dH$。
逐阶比较 (4) 给出

$$
 \boxed{\quad
 L_{h,j}(H)=\frac{d^h}{h!}L_{0,j}(H)
                  \qquad(h+j\le p-1).
 \quad}
 \tag{5}
$$

所有显示的 $h!$ 都是单位。(5) 不被外推到任意总次数。

首个误差也可完全计算。沿 $b=0$ 置 $a=1+x=e^\eta$，则
有限群平均准确为

$$
 U=u(\eta)=\sum_{\substack{n\ge1\\n\equiv1\ (p-1)}}\frac{\eta^n}{n!},
 \qquad
 EU=A(\eta)=u'(\eta)
       =\sum_{\substack{n\ge0\\n\equiv0\ (p-1)}}\frac{\eta^n}{n!}.
 \tag{6}
$$

$V$ 的一次 $b$ 项为 $bA(\eta)e^{-\eta}$，故
$(EV/V)|_{b=0}=A'(\eta)/A(\eta)=dA/dU$。
由 $\eta=U+O(U^p)$ 及第一个非恒定字符的唯一性，

$$
 \boxed{\quad
 E=
 \left(1+\frac{U^{p-1}}{(p-1)!}+O((U,V)^p)\right)\partial_U+
 \left(\frac{U^{p-2}V}{(p-2)!}+O((U,V)^p)\right)\partial_V.
 \quad}
 \tag{7}
$$

这不是只在轴上作出的断言；式 (3) 已排除同次数的其他环境单项式。
两个系数模 $p$ 分别为 $-1,+1$。例如，对齐次 $H$，
首次两个受影响系数准确为

$$
 L_{p,0}=\frac{d^p-d}{p!}L_{0,0},\qquad
 L_{p-1,1}=\frac{d^{p-1}-1}{(p-1)!}L_{0,1}.
 \tag{8}
$$

因此即使 $d$ 是单位，也不能把 (5) 无误差延长。

## 3. 保留第一类周期的完整径向轴比较

对第 5 节的原中央行，可以去掉 (5) 的低总次数限制。
这是一个额外的精确轴比较，不是忽略 (7)。

在特征零形式域中取
$$
 s=b/a,\qquad w=q(s)=s\mathcal L(s)^4,\qquad
 \eta=\log\bigl(a/A_0(s)\bigr),\quad A_0(s)=a(q(s)).
$$
这些变量中原点的真实曲线是 $\eta=0$，并且
齐次 $H$ 准确变为 $e^{d\eta}H(\gamma(w))$。
R174 的有限平均中的角色条件给

$$
 U=u(\eta)+O(w^r),\qquad
 V=wA(\eta)+O(w^{r+1}).
 \tag{9}
$$

具体地，$U$ 的 $w$ 次数只能是 $0\bmod r$，
$V$ 的 $w$ 次数只能是 $1\bmod r$；
$w^0$ 和 $w^1$ 的系数正是 (6)。
这保留了真实 period $q(s)$，没有把对数在扭点处任意代值。

令 $\eta_0(U)$ 是 $u$ 的形式逆，并置

$$
 \mathfrak a(U)=e^{\eta_0(U)},\qquad
 \mathfrak b(U)=A(\eta_0(U)).
 \tag{10}
$$

虽然 (6) 是在特征零写出的，(10) 的两个对象均为真正整级数：
原整坐标 $U(x,0)$ 的导数为一，所以其整逆给
$\mathfrak a=1+x(U)\in1+U\mathbb Z_p[[U]]$；
$\mathfrak b=(EU)|_{b=0}$ 亦整且常数一。
还准确有 $[U](\mathfrak a-1)=1$。

写 $H(\gamma(w))=\sum H_nw^n$，假定 $H_0=0$。
由 (9) 反解，
$$
 \eta=\eta_0(U)+O(V^r),\qquad
 w=V/\mathfrak b(U)+O(V^{r+1}).
$$
$\eta$ 的误差乘上 $H(w)=O(w)$ 后只从 $V^{r+1}$ 影响。
因而对每个 $1\le j\le r$ 有完整的系数级数恒等式

$$
 \boxed{\quad
 \sum_{h\ge0}L_{h,j}(H)U^h
       =H_j\,\mathfrak a(U)^d\mathfrak b(U)^{-j}.
 \quad}
 \tag{11}
$$

这里没有对 $h$ 作截断。$H_0=0$ 是必要条件；
若存在常数项，$\eta$ 的 $O(V^r)$ 误差本身会进入 $j=r$。
原每个 $H_m$、$m\ge1$，均满足该条件。
同时 $L_{h,0}(H_m)=0$ 对全部 $h$ 成立，因为 $V=b\cdot$整单位。

## 4. 全部混合列的共同有限精度谱行

本节在原第零行已经杀掉常数的源上工作，即 $H_0=0$；
所有正阶的实际前缀都满足此条件。
置 $g_{m,j}=L_{0,j}(H_m)$。若 $N\ge1$，且
$$
 h+j+(r-1)(N-1)\le p-1,
 \tag{12}
$$
则 (2)、(5) 给同一个源上的准确同余

$$
 \boxed{\quad
 h!\Lambda_{h,j}(H)\equiv
 \sum_{\substack{0\le q<N\\q\le h}}\pi_0^q(h)_{\underline q}
       \sum_{m=1}^{D}(17m)^{h-q}g_{m,j+rq}
                         \pmod {p^N}.
 \quad}
 \tag{13}
$$

其中 $(h)_{\underline q}=h!/(h-q)!$。
条件 (12) 正是每个 $L_{h-q,j+rq}$ 的实际总次数条件，
高 $q$ 项先由 $\pi_0^q$ 的整性消去；没有先删高次 Taylor 尾。

例如，若再有 $h\ge ND$，则对同一真实前缀
$\operatorname{ord}_vH(\gamma_v)\ge rh+j$，

$$
                         \Lambda_{h,j}(H)\in p^N\mathbb Z_p.
 \tag{14}
$$

证明取单首一谱多项式 $Q(T)=\prod_{m=1}^D(T-17m)$。
序列 $(h)_{\underline q}d^{h-q}$ 是 $d^h$ 对 $d$ 的
第 $q$ 个导数，故 $Q(T)^N$（$T$ 为序列移位）杀死 (13)
右侧的全部 $q<N$ 项。用其首项在 $h$ 处作用，其他行均早于
$h$，已被原前缀准确杀掉；(12) 同时适用于这些早行。
$h!$ 是单位，遂得 (14)。这是同一整个源的行关系，
不是各列分别选择的插值。

本节只声称 (12) 内的有限精度改进。
它本身未提供全 $k,p,D$ 的严格总预算。

### 4.1. 第二个 $V^r$ 带及完整首段的模 $p^2$ 行

还可以保留 (9) 的下一项，从而把模 $p^2$ 的共同式延至全部
$h<p$，而不是只在 (12) 的低总次数范围。
记 $b_n=[w^n]b(w)$，并置
$$
 \kappa_p=u_0-b_{r+1}.
$$
这是一个 $p$ 进整数：$q(s)=s\mathcal L^4$ 及其逆到次数 $r+1$ 都整，
因为所用 $4n+1$、$n\le r$ 的分母不被 $p$ 除。
$a(w)$ 的次数 $<r$ 整，故 $b_r$ 及 $b_{r+1}-a_r$ 整。
再用 $u_0=a_r-b_r/3$，得到 $\kappa_p\in\mathbb Z_p$。
这里只证明整性，不把它一概称为单位或一概称为 $p$ 的倍数。

有限角色平均准确给
$$
 \begin{aligned}
 U&=u(\eta)+u_0 A(\eta)w^r+O(w^{2r}),\\
 V&=A(\eta)w+b_{r+1}A'(\eta)w^{r+1}+O(w^{2r+1}).
 \end{aligned}
 \tag{14a}
$$
例如 $U$ 的 $w^r$ 项要求 $\eta$ 次数为 $0\bmod p-1$，
而 $V$ 的 $w^{r+1}$ 项要求该次数为 $p-2\bmod p-1$，
所以两系数恰为 $A$、$A'$，不是未指定的单位倍。

在固定 $U$ 时反演，$\eta$ 的第一修正为 $-u_0w^r$。
$w$ 的相应修正系数是
$\kappa_p A'(\eta)/A(\eta)$。
因此，对 mass 为零的齐次 $H$，写 $g_j=L_{0,j}(H)$，
对所有 $0\le j\le r$ 有完整的 $U$ 级数恒等式
$$
 \boxed{\quad
 \sum_{h\ge0}L_{h,j+r}(H)U^h
 =\mathfrak a(U)^d\mathfrak b(U)^{-j-r}
       \left(g_{j+r}+j\kappa_p\mathfrak b'(U)g_j\right).
 \quad}
 \tag{14b}
$$
这里 $g_0=0$。在 $U=0$ 处它还给
$g_{j+r}=H_{j+r}-d u_0H_j$。
这一可能含 $p^{-1}$ 的写法是两个真实项的相消；
$g_{j+r}$ 的整性来自原整 Cartan 逆，不能把两项分别假定为整。
当 $j=r$ 时，(14a) 中尚未写出的 $w^{2r}$ 修正乘上
$H(w)=O(w)$ 后才从 $V^{2r+1}$ 影响，所以显示的端点也合法。

由 (6)，
$$
 \mathfrak a(U)=e^U+O(U^p),\qquad
 \mathfrak b(U)=1+\frac{U^{p-1}}{(p-1)!}+O(U^p).
$$
将 (11)、(14b) 同时代回原 (2)，保留 $q=0,1$，而用整性
把 $q\ge2$ 项留在 $p^2$ 中。于是对整个原混合源，
所有 $0\le j<r$、$1\le h\le p-2$ 都有
$$
 \boxed{\quad
 h!\Lambda_{h,j}(H)\equiv
 \sum_{m=1}^{D}
 \left(d_m^h g_{m,j}
       +\pi_0 h d_m^{h-1}g_{m,j+r}\right)\pmod{p^2}.
 \quad}
 \tag{14c}
$$
这次不再要求 $h+j+r-1\le p-1$。
$h=0$ 的行仍准确是 $\Lambda_{0,j}=\sum_mg_{m,j}$。
最后一个 normal step 必须保留实际首 carry：
$$
 \boxed{\begin{aligned}
 (p-1)!\Lambda_{p-1,j}(H)\equiv
 \sum_{m=1}^{D}\Bigl[
 &(d_m^{p-1}-j)g_{m,j}\\
 &+\pi_0(p-1)\bigl(
 d_m^{p-2}g_{m,j+r}+j\kappa_p g_{m,j}\bigr)\Bigr]
 \pmod{p^2}.
 \end{aligned}}
 \tag{14d}
$$
所以把最后一行也当作无误差的幂矩会漏掉两项。
所有这些式子仍是同一个 $L$、同一个 $\Lambda$、同一个原源；
没有用参数不同的列来拼出一个伪共同矩阵。

## 5. 原两中央条件确实进入原饱和行

记
$$
 \beta_r(H_m)=[w^r]H_m(\gamma(w)).
$$
对原两个线性坐标，这就是 $[z^{p+1}]\mathcal A$、
$[z^{p+1}]\mathcal B$，即 R169 的真实第一中央系数。
式 (11) 表明这些数整，并且

$$
 \frac{\Lambda_{h,0}(H)}{\pi_0}
 \equiv [U^{h-1}]\mathfrak b(U)^{-r}
              \sum_{m=1}^D\beta_r(H_m)\mathfrak a(U)^{17m}
                   \pmod p,\qquad 1\le h<p.
 \tag{15}
$$

左侧整性是准确的：$q=0$ 项 $L_{h,0}$ 恒为零，
其余项都含 $\pi_0$；除后 $q\ge2$ 项仍含 $p$。
这里依靠完整轴式 (11)，所以不再要求 $h+r\le p$。

**指定真实行定理。** 设 $1\le D<p$，
$H\in E_D$ 且
$\operatorname{ord}_vH(\gamma_v)\ge rD$。则

$$
 \boxed{\quad
 p^{D-1}[v^{rD}]H(\gamma_v)
 \equiv(-17\tau_p)^{D-1}\beta_r(H_1)\pmod p.
 \quad}
 \tag{16}
$$

证明令 $c_m=\beta_r(H_m)$。
前面的 $h=1,\ldots,D-1$ 行在 (15) 中准确为零。
乘去共同整单位 $\mathfrak b^{-r}$，并用首项一的整变量
$x=\mathfrak a(U)-1$，得到
$$
 S(x)=\sum_{m=1}^Dc_m(1+x)^{17m}
                    \equiv0\pmod{p,x^{D-1}}.
$$
首个可能系数在两次操作中都不变。
多项式
$$
 \frac1{(D-1)!}\prod_{m=2}^D(T-17m)
$$
与 $\binom{T}{D-1}$ 具有相同首项，其差次数至多 $D-2$。
先前的零矩因此给
$$
 [x^{D-1}]S\equiv(-17)^{D-1}c_1\pmod p.
$$
使用 (2)、$\pi_0u_0=1$、$pu_0\equiv\tau_p$，恰得 (16)。
$D<p$ 使所有显示的阶乘及不同谱值之差都是单位；
不需要更强的 $p>17D$。

若原两条中央首层都为零，
$$
             \beta_r(\mathcal A)=\beta_r(\mathcal B)=0\pmod p,
 \tag{17}
$$
则 (16) 对**全部原次数 $D$ 的饱和前缀**给

$$
 \boxed{\qquad
 v_p\bigl([v^{rD}]H(\gamma_v)\bigr)\ge-D+2.
 \qquad}
 \tag{18}
$$

不使用 (17) 时，同一行的已付下界是 $-D+1$。
$D=1$ 时 (18) 就是实际整行再被 $p$ 除；
未把负的成本截成错误的单位等式。
参数 $v(w)=w+O(w^2)$ 保持准确前缀首系数，所以 (16)–(18)
也是真实原 $w$ 参数下的同一结论。

还有对同一 $H$ 的延伸。若 $H$ 已在 $rD$ 前缀内并满足
(17)，则 $c_1=0\bmod p$ 和先前 $D-1$ 个矩，经单位
Vandermonde 矩阵迫使全部 $c_m=0\bmod p$。
故 (15) 给
$$
                   \Lambda_{h,0}(H)\in p^2\mathbb Z_p
                        \qquad(1\le h<p).
 \tag{19}
$$
因此在任一更晚的实际前缀 $rh$、$D\le h<p$，
都有 $v_p([v^{rh}]H)\ge-h+2$。
必须准确区别新增之处：若本来就有 $r(D+1)$ 的前缀，
即使没有 (17)，前 $D$ 个矩也会给同样的全部 $c_m=0\bmod p$。
中央条件使此完整矩消去**提前一个实际 normal step**；
没有把每个后续行重新计算成额外的独立收益。

## 6. 有限独立校准及未付范围

[准确脚本](../scripts/check-euler-cartan-central-prefix-gain.py)
不计算 Cartan 逆或使用 (16) 造系数。
它从 R162 的固定有理 $P,Q,W$ 生成真实原列，
用最小 $p$ 赋值 pivot 的整列消元保留准确饱和核，
同时运输原线性部分的中央泛函，逐个剩余核基核对 (16)。
默认只检查
$(p,D)=(7,1),(7,2),(7,4),(7,6),(11,3),(11,4)$；
$p=7,D=6$ 特别超出旧的 $D\le p-r$ 范围，
校准了 (11) 的实际加强。一般证明仍是上述轴及矩比较。

[第二带独立脚本](../scripts/check-euler-cartan-second-band.py)
另在 $p=7$ 从有限角色平均直接构造真正的二维 Cartan 形式逆，
保留环境总次数 $13$，分别检查 $\mathcal A$、$\mathcal B$、
$\mathcal A^2$。全部 $135$ 个精确等式或模 $p^2$ 比较通过，
包含 (14b) 的 $j=r$ 端点及 (14d) 的 $h=p-1$ 两项修正；
它不使用这两式来生成被检验的二维系数。

已付的是：原全部列、同一实际前缀、完整 $\pi_0$ 行、
准确谱次数、及两条原中央值的指定比较。
本结果不把 (17) 外推为 $\beta_r(H_m)=0$ 对所有乘积成立；
高次数的零矩是在同一前缀下推出来的。
对 $j\ne0$ 的全部高精度，以及 $k\ge pr$ 的新共振，
仍须保留真实余项。本文尚未给出 R159 所需的严格全阶预算。

## 依赖

- [R174：真实整 Cartan 及全部前缀矩阵](2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)。
- [R170：全 Gaussian 整映射](2026-11-12-full-cm-theta-plane-and-sparse-resonance.md)。
- [R169：原两中央行与周期规范](2026-11-12-joint-central-amplitudes-and-period-frobenius.md)。
- [R171：首传播和整个带的共同主行](2026-11-12-theta-graph-nonlinear-propagation-and-common-blocks.md)。
- [R159：真正次数敏感的斜率标准](2026-11-12-degree-sensitive-jets-and-direct-slope-boundary.md)。
