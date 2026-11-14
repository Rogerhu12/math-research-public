# R210 — 整个第一带的整 Faber 核、原 theta 截断与首个 Witt 分母

日期：2026-11-12。**状态：以下整性、准确留数、有限 Laurent 商及其锐边界均已证明；不证明原中央系数的跨素数非零。**

本篇延伸 [R208](R208-original-theta-single-pole-faber-and-integral-log-comparison.md) 的两权构造。关键区别是：Faber 核在整个第一带仍整，甚至不损失 $v_p(n)$；全局原函数的分母却在第四个中央权已经不可避免。必须把这两种整性分开。

## 1. 固定参数与首个真正的坐标分母

仍在原曲线
$$
 E_0:y^2=x^3-x,\qquad \omega=\frac{dx}{2y}=dz,\qquad
 s=x^{-2},\quad T=x^2=s^{-1}
$$
上工作。取素数 $p=4r-1\ge7$，置
$$
 R=\frac{p^2-1}{4}=r(p-1),\qquad O=\mathbf Z_p,
$$
并沿用
$$
 z=uF(s),\qquad
 F(s)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(4j+1)}s^j,\qquad
 w=z^4=W(s):=sF(s)^4.
 \tag{1}
$$
R202 §5.1 已证明原椭圆对数的首坏阶准确为 $u^{p^2}$，因此
$$
 [s^j]F\in O\quad(0\le j<R),\qquad
 p[s^R]F\equiv-1\pmod p.
 \tag{2}
$$
特别地，$W(s)$ 至 $s^R$ 的系数整，且首系数为一。它的严格反函数 $s(w)$ 至 $w^R$ 同样整。这一阶数差须保留：$F$ 的首坏项在 $s^R$，但 $W=sF^4$ 的首坏项只能从 $s^{R+1}$ 开始。

后文只在 $n,M\le R$ 使用这些整换元。

## 2. Faber 核的分母消去：不要求 p 不整除 n

对任意正整数 $n$，在特征零中定义
$$
 c_{n,j}=[s^j]F(s)^{-4n},\qquad
 \mathcal F_n(T)=\sum_{j=0}^n c_{n,j}T^{n-j}.
 \tag{3}
$$
如 R208，$\mathcal F_n(T(z))=z^{-4n}+O(z^4)$，且
$$
 \mathcal H_n=-\frac1{4n}\frac{d\mathcal F_n}{\omega}
            =-\frac{xy}{n}\mathcal F_n'(T)
            =z^{-4n-1}+O(z^3).
 \tag{4}
$$
表面上的 $1/n$ 并不造成核的精度损失。

由原椭圆对数的微分直接有
$$
 F(s)+4sF'(s)=(1-s)^{-1/2}.
 \tag{5}
$$
故
$$
 F^{-4n}-\frac{s}{n}(F^{-4n})'
 =F^{-4n-1}(1-s)^{-1/2}.
 \tag{6}
$$
定义
$$
 d_{n,j}=[s^j]F(s)^{-4n-1}(1-s)^{-1/2}.
$$
逐项比较 (6)，得到准确恒等式
$$
 d_{n,j}=\frac{n-j}{n}c_{n,j}.
 \tag{7}
$$
特别地 $d_{n,n}=0$。置
$$
 \mathcal D_n(T)=\sum_{0\le j<n}d_{n,j}T^{n-j-1};
$$
则
$$
 \boxed{\qquad
 \frac{\mathcal F_n'(T)}{n}=\mathcal D_n(T),\qquad
 \mathcal H_n=-xy\,\mathcal D_n(T).
 \qquad}
 \tag{8}
$$

**定理 2.1（完整第一带的核整性）。**
对每个 $1\le n\le R$，
$$
 \mathcal D_n\in O[T],\qquad
 \deg\mathcal D_n=n-1,\qquad
 \text{首系数}=1,\qquad
 \mathcal H_n\in O[x,y].
 \tag{9}
$$
这包括 $p\mid n$，没有附加 $v_p(n)$ 损失。

证明：计算 $d_{n,j}$ 只读 $F$ 到 $s^j$，而 $j<n\le R$。
由 (2)，这些系数整；$(1-s)^{-1/2}\in\mathbf Z[1/2][[s]]$，也整。
其常数项为一，故 (9) 全部成立。证毕。

在端点 $n=R$，$\mathcal F_R$ 的常数项可以非整，但它在 (8) 中已被导数杀掉。把这一个常数算作核的分母，会错误地提前丢掉第一带端点。

### 2.2. 首个不整核准确在 R+1

取 $n=R+1$。当 $j<R$ 时，$d_{n,j}$ 仍整；唯一新增的系数满足
$$
 d_{R+1,R}
 =-(4(R+1)+1)[s^R]F+\text{一个 }O\text{ 元素}.
$$
由 (2) 及 $4(R+1)+1=p^2+4$，
$$
 p\,d_{R+1,R}\equiv4\pmod p.
$$
因此
$$
 \boxed{\quad
 p\,\frac{\mathcal H_{R+1}}{xy}\equiv-4\pmod{p\,O[T]}.
 \quad}
 \tag{10}
$$
更准确地，$p\mathcal H_{R+1}/(xy)\in O[T]$ 的约化为常数 $-4$；
$\mathcal H_{R+1}$ 在基 $xy\,T^j$ 中最低系数赋值恰为 $-1$。
所以 (9) 的范围是锐的。此处不是假设某个中央导数失败后才出现的分母，而是原椭圆对数自身的首 carry。

## 3. 原共同 theta gauge 在整个第一带内仍可整运输

这一节使用 R199 的实际原轴，故取其原范围 $p\ne11$；也可直接限制到 $p\ge19$。所有函数仍为 R197 的原 $A=A_2,B$。

令
$$
 c_p=68k_r,\qquad b_p=17u_0,\qquad d_p=c_p-b_p.
$$
R197 §5.1 已由同一原系数证明 $d_p\in O$。
R199 则准确给
$$
 A=e^{b_pw^r}f_A(w),\qquad
 B=e^{b_pw^r}f_B(w)\pmod{w^{R+1}},
 \qquad f_A,f_B\in wO[[w]].
 \tag{11}
$$
因此同一个 R197 gauge
$$
 \widehat A=e^{-c_pw^r}A,\qquad
 \widehat B=e^{-c_pw^r}B
 \tag{12}
$$
满足
$$
 \widehat A=e^{-d_pw^r}f_A(w),\qquad
 \widehat B=e^{-d_pw^r}f_B(w)\pmod{w^{R+1}}.
 \tag{13}
$$
在第一带中，指数最多读 $(p-1)!$，所以
$$
 [w^j]\widehat A,\ [w^j]\widehat B\in O
 \qquad(0\le j\le R).
 \tag{14}
$$
这些原 gauged 系数仍是有理数；(11) 只是证明其整性，不用任意新轴替代它们。

再写原
$$
 A=\vartheta^{68}P(s(w)),\qquad B=\vartheta^{68}Q(s(w)),
$$
其中 $P,Q$ 正是 R197 的次数十六多项式，且 $P(s)=s+\cdots$。
由于 $P(s(w))/w$ 是整单位，(14) 的第一式推出
$$
 [w^j]\bigl(e^{-c_pw^r}\vartheta(z)^{68}\bigr)\in O
 \qquad(0\le j\le R-1).
 \tag{15}
$$

固定任何 $1\le M\le R$，定义同一个原参考的有限代表
$$
 \Gamma_{p,M}(s)=
 \left[e^{-c_pW(s)^r}\vartheta(z(s))^{68}\right]_{\deg_s\le M-1}.
 \tag{16}
$$
由 (1)、(15)，$\Gamma_{p,M}\in O[s]$。置
$$
 f_{M,A}(s)=[\Gamma_{p,M}(s)P(s)]_{\deg_s\le M},\qquad
 f_{M,B}(s)=[\Gamma_{p,M}(s)Q(s)]_{\deg_s\le M}.
 \tag{17}
$$
它们在 $sO[s]$ 中，次数至多 $M$，首系数均为一。对每个 $n\le M$，准确有
$$
 [w^n]f_{M,F}(s(w))=[w^n]\widehat F(w)
 =:\widehat R_{n,F},\qquad F=A,B.
 \tag{18}
$$
这是特征零等式，保留任意 $p$ 进精度，并且同一个 $M$ 的代表同时保留全部 $n\le M$ 行。

当只读中央权 $n=rh$、$h\le p-1$ 时，(13) 也说明原轴行与这些 gauged 行之间是单位下三角整矩阵：
$$
 \widehat R_{rh,F}
 =\sum_{j=1}^h\frac{(-d_p)^{h-j}}{(h-j)!}
      [w^{rj}]f_F(w).
 \tag{19}
$$
这只在此处所写的未加 $p^{-h}$ 目标格中成立；若另给每行不同的 $p$ 次归一，仍须保留 R203 的实际整格比较，不能直接套用 (19)。

## 4. 全第一带的单固定极点留数

对 $1\le n\le M\le R$ 及原 $F=A,B$，定义
$$
 \Omega_{n,F}^{(M)}
 =f_{M,F}(s)\mathcal H_n\omega.
$$
它只可能在 $O_E$ 和 $T_0=(0,0)$ 有极点，且
$$
 \operatorname{Res}_{O_E}\Omega_{n,F}^{(M)}
 =\widehat R_{n,F}.
 \tag{20}
$$
由 (8)，准确有
$$
 \Omega_{n,F}^{(M)}=\pi_T^*\eta_{n,F}^{(M)},\qquad
 \eta_{n,F}^{(M)}
 =-\frac14 f_{M,F}(T^{-1})\mathcal D_n(T)\,dT.
 \tag{21}
$$
此式已不含 $1/n$。

写
$$
 \eta=\sum_{h=1-M}^{n-1}\beta_hT^{h-1}dT,\qquad
 \beta_h\in O.
 \tag{22}
$$
与 R208 相同，$T=x^2$ 在两个固定点都以指数 $4$ 分歧，因此
$$
 \boxed{\qquad
 \beta_0=-\frac{\widehat R_{n,F}}4.
 \qquad}
 \tag{23}
$$
在曲线上 $d\log T=2d\log x$，故最终对数系数仍是
$-\widehat R_{n,F}/2$。没有改变 R197 的原尺度。

## 5. 准确的一层 Witt 分解

记
$$
 \mathcal U_0(T)=
 \sum_{\substack{1-M\le h\le n-1\\h\ne0,\ p\nmid h}}
                 \frac{\beta_h}{h}T^h.
$$
再令
$$
 \mathcal U_1(T)=
 \sum_{\substack{q\ne0\\1-M\le pq\le n-1}}
                 \frac{\beta_{pq}}{q}T^q.
 \tag{24}
$$
因为 $M\le R<p^2$，第二式中所有 $0<|q|<p$。两者因此都在
$O[T,T^{-1}]$，且
$$
 \deg_{\pm}\mathcal U_1
 \le\max\!\left\{
 \left\lfloor\frac{M-1}{p}\right\rfloor,
 \left\lfloor\frac{n-1}{p}\right\rfloor\right\}<p.
$$
逐项求导给准确恒等式
$$
 \boxed{\quad
 \eta
 =d\mathcal U_0(T)
   +\frac1p\,d\!\bigl(\mathcal U_1(T^p)\bigr)
   +\beta_0\,d\log T.
 \quad}
 \tag{25}
$$
中间那项的**微分系数**是整的，但其全局原函数可能需要分母 $p$。
等价地，
$$
 p\Omega_{n,F}^{(M)}
 =d\!\left(p\mathcal U_0(x^2)+\mathcal U_1(x^{2p})\right)
       -\frac{p\widehat R_{n,F}}2\,d\log x.
 \tag{26}
$$
所以整个第一带的整原函数代价至多一层 $p$，不随 $n$ 再累加；
但在 (25) 中直接删去中间项并宣布“整 exact/log 分解”是不合法的。

### 5.1. 实际有限 Laurent 商中的 p 扭

把 (22) 的全部系数格记为
$$
 \mathcal V_{M,n}
 =\bigoplus_{h=1-M}^{n-1}O\,T^{h-1}dT.
$$
只对同一有限窗口中的整 Laurent 函数求导，准确得到
$$
 \frac{\mathcal V_{M,n}}
 {d\!\left(\bigoplus_{h=1-M}^{n-1}O\,T^h\right)}
 \simeq O\,d\log T
 \ \oplus\
 \bigoplus_{\substack{h\ne0\\1-M\le h\le n-1\\p\mid h}}
       (O/pO)\,[T^{h-1}dT].
 \tag{27}
$$
证明是各单项式上的对角映射 $T^h\mapsto hT^{h-1}dT$；
非零 $h$ 的赋值在本窗口中至多一。扭项的准确个数为
$$
 \left\lfloor\frac{M-1}{p}\right\rfloor
 +\left\lfloor\frac{n-1}{p}\right\rfloor.
 \tag{28}
$$
因此 R208 的小窗口中确实只有对数自由方向；更深时则还存在这些实际的整扭方向。它们不是原目标留数，也不能从某条留数可除 $p$ 推断它们同时为零。

### 5.2. 两次 Cartier 准确读取原行

在 $\mathbf F_p$ 上，(25) 的系数式给
$$
 \operatorname{Car}(\bar\eta)
   =d\overline{\mathcal U}_1(T)+\bar\beta_0\,d\log T,
 \qquad
 \operatorname{Car}^2(\bar\eta)
   =\bar\beta_0\,d\log T.
 \tag{29}
$$
这是 Cartier 的单项式公式；第一式也明确保留了首个 Cartier 输出中的 exact 分量。
沿原可分映射 $T=x^2$ 拉回，
$$
 \boxed{\quad
 \operatorname{Car}^2(\overline\Omega_{n,F}^{(M)})
 =-\frac{\overline{\widehat R}_{n,F}}2\,d\log x.
 \quad}
 \tag{30}
$$
此处只使用原行的有限代表，不把一次 Cartier 的额外分量当作已经观测到的中央非零。
在 $M\le p$ 时，(24) 的 $\mathcal U_1$ 为空，故 (30) 降为 R208 的一次 Cartier 公式。

### 5.3. 正扭方向只读真实的过去行

正方向还可准确压回原曲线的已观测行。对每个 $h\ge0$，有
$$
 \boxed{\quad
 \beta_h=-\frac14[w^n]\widehat F(w)\,s(w)^h.
 \quad}
 \tag{30a}
$$
这里右端最多读取 $\widehat F$ 至 $w^{n-h}$；特别地，当 $h>0$
时不读取当前第 $n$ 行。

证明如下。记
$$
 \mathscr K_n(s)=F(s)^{-4n-1}(1-s)^{-1/2}.
$$
(21) 的系数给
$$
 \beta_h=-\frac14[s^{n-h}]
 f_{M,F}(s)[\mathscr K_n(s)]_{<n}.
$$
当 $h\ge0$ 时，$f_{M,F}(s)\in sO[s]$ 使截去的尾不贡献所取系数。
又有准确换元恒等式
$$
 W(s)^{-n-1}W'(s)\,ds
 =s^{-n-1}\mathscr K_n(s)\,ds.
$$
作留数换元并使用 (18)，即得 (30a)。

令 $q\ge1$ 且 $pq\le n-1$。约化到 $\mathbf F_p$ 后，
$$
 \bar s(w)^{pq}=(\bar s(w)^q)^p,
$$
因此
$$
 \boxed{\quad
 \bar\beta_{pq}
 =-\frac14\sum_{\ell=q}^{\lfloor(n-1)/p\rfloor}
       [w^\ell]\bar s(w)^q\,
       \overline{\widehat R}_{n-p\ell,F}.
 \quad}
 \tag{30b}
$$
这些全部是真实过去行。由于 $[w^q]s(w)^q=1$，正扭向量
$(\bar\beta_p,\bar\beta_{2p},\ldots)$ 与
$(\overline{\widehat R}_{n-p,F},
  \overline{\widehat R}_{n-2p,F},\ldots)$
准确由对角为 $-1/4$ 的单位上三角矩阵相连。
所以正扭项不提供一个独立的新中央约束，不能再次记入净收益。

对 $h<0$ 不能直接使用 (30a)：$\mathcal H_n$ 的正则尾乘上
$s(w)^h$ 后会贡献留数，有限代表的高次截断也必须保留。
负扭项在 (21)–(25) 中已准确给出；若另想把它们认成原完整函数的
移位行，就须同时支付这些正则尾和所需高行，不能把它们直接标成
已经读出的原前缀。


## 6. 第四个中央权上的原对象锐边界

取
$$
 n=M=p+1=4r,
$$
即第四个中央权 $4n=4(p+1)$。这在所用第一带中，因为 $p+1\le R$。
两条原代表都满足 $[s]f_{M,F}=1$，而 $\mathcal D_n$ 首系数为一。
所以 (21) 的最高 Laurent 项准确为
$$
 \boxed{\qquad
 \beta_pT^{p-1}dT=-\frac14T^{p-1}dT.
 \qquad}
 \tag{31}
$$
它是一个非零的 $p$ 扭方向，原函数必须含 $-T^p/(4p)$。
这不依赖于任何完整中央消失假设，也不依赖数值样本。

即使允许原函数是 $E_0\setminus\{O_E,T_0\}$ 上的任意整正则函数，
(31) 也不能被整积分。证明是在未分歧扩环 $O[i]$ 上取
$$
 (x,y)\longmapsto(-x,iy)
$$
的四阶平均。$\Omega$ 与 $d\log x$ 均不变，$1/4$ 是单位。
若它们之差有整正则原函数，平均后便得到一个不变的整原函数。
而
$$
 \left(O[i][x,y,x^{-1}]/(y^2-x^3+x)\right)^{\mu_4}
 =O[i][T,T^{-1}].
$$
这可由唯一写法 $a(x)+yb(x)$ 逐项验证。
整 Laurent 原函数的 $T^{p-1}dT$ 系数必须属于 $pO[i]$，
与 (31) 矛盾。故一层分母在原对象上已经是必要的。

特别地，若该原行恰好模 $p$ 为零，一次 Cartier 的 exact 分量仍含
$-\tfrac14dT$，不能据此说整个微分已经 exact 或 Cartier 为零；
第二次 Cartier 才准确只留下目标对数行。

## 7. 已支付和仍未支付的范围

本篇已经给出：

1. 不损失 $v_p(n)$ 的实际 Faber 核，以及 $n=R$ 端点和 $R+1$ 首坏系数；
2. 原同一 R197 gauge 在整个第一带的整 theta 代表，同一有限代表保全部前缀行；
3. 原两列在单固定极点上的真实有限留数和任意 $p$ 进精度；
4. 全第一带准确的对数方向、一次 $p$ 分母、扭方向数目及两次 Cartier；
5. 第四中央权的实际单位扭项，证明该分母不能免费取消。

这没有证明 $\widehat R_{n,F}$ 或其除 $p$ 后继式在无穷多个 $p$ 非零。
也没有把全部第一带的积分原函数误差当成原完整无界中央导数的尾：
超过 $R$ 后，(10) 的真实坐标分母与后续 carry 必须继续保留。
最后，(16)–(18) 是实际有限行的全局代表，不是从原曲线 scalar prefix
免费恢复任意环境 Hasse core 的左逆；原净范数和严格全素数预算仍须单独证明。

依赖：[R197](R197-actual-two-weight-determinant-and-common-theta-gauge.md)、
[R199](R199-exact-first-band-exponential-and-complete-divided-image.md)、
[R202](R202-rational-elliptic-parameter-and-unit-cartier-obstruction.md)、
[R208](R208-original-theta-single-pole-faber-and-integral-log-comparison.md)。

