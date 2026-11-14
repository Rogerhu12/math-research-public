# R239 附录：三位等权短串加一个异常位的最高二维 primitive 块——全部高度严格系数一

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的有限模型结论。** 本文处理两条对称串长度为 $3,L$、再加一条长度一串的相对出生 $t=3$。其完整 primitive 重数为二，全部高度及所有正权比均满足严格相邻系数一。没有把该块扩充为相同四个异常头的所有出生，也不推断任意多权或原高孔尾的统一界。

整数多项式证书：[可重算 Python/FLINT 文件](../notes/2026-11-13-three-short-weights-saturated-all-height-certificate-0c.py)。它按下面给出的有限多项式直接展开全部系数；没有有限参数扫描或由数值点外推。

## 1. 模型、真实源及完整 MP 费用

第一条串来自三个共同正权 $a$，第二条串来自 $L$ 个共同权一，另有一个正权 $c$。令
$$
z=a^2>0,\qquad w=c^2>0,\qquad L\ge4,
\qquad t=3,\qquad h=3+L+1-2t=L-2\ge2.
$$
两组内部的正交对称串分解保持删除算子及其伴随；本文在指定长度 $3,L,1$ 的块上取**完整出生层的逆**再压缩到整个二维 primitive。各表示重数按正交直和原样保留。

可以使用不归一的对称池坐标。设第一组和单个位的实际占据数分别为 $3-r,1-k$，其中 $0\le r\le3$、$k\in\{0,1\}$。在出生层，长池占据数为 $\ell=r+k-1$。固定源写作
$$
g_{\alpha,\beta}(r,k)
=\frac{(-1)^\ell a^r c^k}{\binom L\ell}
(\alpha r+\beta k),
\qquad 0\le\ell\le L.
\tag{1.1}
$$
这里的坐标基在所有高度都相同，且 $(\alpha,\beta)\mapsto g_{\alpha,\beta}$ 是二维 primitive 的同构；直接删除给零。

采用[完整固定块 MP 的有限差分公式](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) §§10–11，全部 $D^n/n!$ 原像的最小费用准确是
$$
\begin{aligned}
H_n[\alpha,\beta]
=\min_{\xi\in\mathbb C}\sum_{r=0}^3\binom3r z^r
\left\{
\frac{|\alpha r+\xi|^2}{\binom L{n+r-1}}
+w\frac{|\alpha r+\beta+\xi|^2}{\binom L{n+r}}
\right\}.
\end{aligned}
\tag{1.2}
$$
分母指数非法时，要求相应分子在该整数点为零，并删掉那项；不能把负阶乘保留下来。完整低次自由项在这里恰为一个共同常数 $\xi$。第一组置换平均及长池置换平均不增范数，且保源；上述完整 MP 公式消掉所有剩余零源分量。因此 (1.2) 不是某个试探原像的费用。

记 $H_n$ 同时表示这个正定二次型的二乘二矩阵。真实 primitive Gram 与 $H_n$ 只差一个不依赖 $n$ 的共同合同，所以本文所证目标准确为
$$
\boxed{H_nH_{n+1}^{-1}H_n\prec H_{n-1},
\qquad 1\le n\le h-1.}
\tag{1.3}
$$

## 2. 四个相邻分布及完整交叉项

先取 $2\le n\le h-2$。四个完整正权分布为
$$
W_i(r)=\frac{\binom3r z^r}{\binom L{n-2+i+r}},
\qquad 0\le i\le3.
$$
定义
$$
b_i=\sum_rW_i(r),\quad m_i=\sum_r rW_i(r),\quad
e_i=\sum_r r^2W_i(r),\quad
\tau_i=b_ie_i-m_i^2,
$$
$$
a_i=\tau_i/b_i>0,\qquad \mu_i=m_i/b_i.
\tag{2.1}
$$
对每个分布先完成关于 $r$ 的平方，再消去 (1.2) 的共同常数，得到相邻三个矩阵
$$
H_j=\begin{pmatrix}A_j+B_j\delta_j^2&-B_j\delta_j\\-B_j\delta_j&B_j\end{pmatrix},
\tag{2.2}
$$
其中
$$
\begin{array}{c|ccc}
j&n-1&n&n+1\\\hline
A_j&a_0+wa_1&a_1+wa_2&a_2+wa_3\\
B_j&\dfrac{wb_0b_1}{b_0+wb_1}&\dfrac{wb_1b_2}{b_1+wb_2}&\dfrac{wb_2b_3}{b_2+wb_3}\\
\delta_j&\mu_0-\mu_1&\mu_1-\mu_2&\mu_2-\mu_3.
\end{array}
\tag{2.3}
$$
这是完整二维费用；每个 $\delta_j$ 及其随高度变化的部分都保留。

作一次共同剪切令中间 $\delta_n=0$，并写
$$
x_s=\mu_0-2\mu_1+\mu_2,\qquad
y_s=-\mu_1+2\mu_2-\mu_3.
\tag{2.4}
$$
下面的 $x_s,y_s$ 是交叉源参数，不是第 4 节的非负高度变量。

令 $K=H_{n-1}-H_nH_{n+1}^{-1}H_n$。直接完整块逆给
$$
\begin{aligned}
K_{11}&=A_- -A_0^2/A_++B_-x_s^2,\\
K_{12}&=-B_-x_s-A_0B_0y_s/A_+,\\
K_{22}&=B_- -B_0^2/B_+-B_0^2y_s^2/A_+.
\end{aligned}
\tag{2.5}
$$
旧两值全部高度定理适用于 $a_i$：它们是两串相对出生二的完整单项最高系数最小费用。因而其相邻比严格递增。正和 $A_j=a_i+wa_{i+1}$ 也严格对数凸：展开差式后，常数项、一次项及二次项分别是 $a_0a_2-a_1^2$、$a_0a_3-a_1a_2$、$a_1a_3-a_2^2$，都正。所以
$$
K_{11}>0.
\tag{2.6}
$$
因此只须证明完整 $\det K>0$。

## 3. 完整四次式与三个实际多项式分子

为缩短代数，暂写
$$
(p,q,r,t)=(b_0,b_1,b_2,b_3),\quad
(a,b,c,d)=(a_0,a_1,a_2,a_3),
$$
其中这里的小写 $q$ 只是一个正标量，不是短串长度。定义
$$
\begin{aligned}
\Lambda(w)&=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),\\
F(w)&=pq(qt-r^2)+wqr(pt-qr)+w^2rt(pr-q^2).
\end{aligned}
$$
准确的清分母式为
$$
P(w):=\det K\,
\frac{(p+wq)(q+wr)^2(c+wd)t}{w},
\tag{3.1}
$$
$$
\begin{aligned}
P(w)={}&q\Lambda(w)F(w)
-wpq^3r(c+wd)(r+wt)x_s^2\\
&-wq^2r^2t(a+wb)(p+wq)y_s^2
-2wpq^2rt(b+wc)(q+wr)x_sy_s\\
&-w^2pq^3r^2t x_s^2y_s^2.
\end{aligned}
\tag{3.2}
$$
它是 $w$ 的四次多项式。两端系数为
$$
P_0=pq^2(ac-b^2)(qt-r^2)>0,
\qquad P_4=qrt(bd-c^2)(pr-q^2)>0.
\tag{3.3}
$$
这里 $b_i$ 的严格对数凸也可直接由 Beta 积分矩及严格 Cauchy--Schwarz 得到。

记
$$
(A,B,C,D)=(\tau_0,\tau_1,\tau_2,\tau_3),
$$
$$
X=m_0qr-2m_1pr+m_2pq,\qquad
Y=-m_1rt+2m_2qt-m_3qr,
$$
$$
V_0=qt-r^2,\quad V_1=pt-qr,\quad V_2=pr-q^2.
\tag{3.4}
$$
于是 $x_s=X/(pqr)$、$y_s=Y/(qrt)$，而 $a=A/p,b=B/q,c=C/r,d=D/t$。代入 (3.2)，三个中间系数准确为
$$
P_1=\frac{N_1}{prt},\qquad
P_2=\frac{N_2}{pqr^2t},\qquad
P_3=\frac{N_3}{prt},
\tag{3.5}
$$
其中
$$
\begin{aligned}
N_1={}&(q^2rtAC-pr^2tB^2)V_1
+(pq^2rAD-p^2qtBC)V_0\\
&-qtCX^2-prAY^2-2ptBXY,\\
N_3={}&(qr^2tAD-prt^2BC)V_2
+(pqr^2BD-pq^2tC^2)V_1\\
&-qtDX^2-prBY^2-2ptCXY,
\end{aligned}
\tag{3.6}
$$
以及
$$
\begin{aligned}
N_2={}&A(Cpq^2r^3t^2-Cq^4r^2t^2
+Dpq^3r^3t-Dq^4r^4-q^2r^2Y^2)\\
&+B^2(-p^2r^4t^2+pq^2r^3t^2)\\
&+B(-Cp^2q^2r^2t^2+Cpq^3r^3t
+Dp^2q^3r^2t-Dp^2q^2r^4\\
&\hspace{30mm}-2pr^2tXY-p^2r^2Y^2)\\
&+C^2(-p^2q^4t^2+p^2q^3r^2t)
+C(-q^2t^2X^2-2pq^2tXY)\\
&-Dq^2r^2X^2-X^2Y^2.
\end{aligned}
\tag{3.7}
$$
这些是纯有限代数恒等式，尚未省去任何交叉费。

## 4. 非负高度变量下的全部整数系数

置
$$
x=n-2,\qquad y=L-n-4,\qquad L=x+y+6.
$$
内部区间恰满足 $x,y\ge0$。除去四个分布共有的正因子 $x!y!/L!$ 后，它们成为有限多项式权
$$
\boxed{\widetilde W_i(r)=\binom3r z^r
(x+1)_{i+r}(y+1)_{6-i-r},\quad 0\le i,r\le3.}
\tag{4.1}
$$
$(u)_k=u(u+1)\cdots(u+k-1)$，$k=0$ 时为一。因子共有且与相邻三个源相同，只使全部 $H_j$ 乘同一正常数，不影响 (1.3)。

按 (4.1) 重新计算 (2.1)、(3.4)、(3.6)–(3.7)，得到 $N_1,N_2,N_3\in\mathbb Z[x,y,z]$。证书逐项实施这些明确多项式加、乘及整数求和，然后又作 $x=X_0-1$ 的精确代入。全部非零系数如下：

| 多项式 | 原非零系数数目 | 代入 $x=X_0-1$ 后非零系数数目 | 总次数上界 | 负系数 |
|---|---:|---:|---:|---:|
| $N_1$ | 24201 | 17145 | 86 | 0 |
| $N_2$ | 42086 | 29718 | 104 | 0 |
| $N_3$ | 24201 | 17591 | 86 | 0 |

表中所有非零系数都是**严格正整数**；次数包括 $z$ 次数。程序保存的是这些有限恒等式的生成式及逐项断言，不必保存大型中间系数表。它对所有系数作检查，不是插值，因此不含先验未知次数的外推。

非零多项式的所有系数为正，立刻给 $N_i>0$ 于 $x,y\ge0,z>0$；若某些非负变量等于零，下面的明确零次锚仍给严格性。因此由 (3.3)、(3.5) 得 $P(w)>0$ 对全部 $w>0$ 成立。结合 (2.5)–(2.6) 得内部所有 (1.3)。

## 5. 低端强制根的精确极限

仍用同一多项式证书，令 $\varepsilon=x+1\downarrow0$、$y\ge0$ 固定。在 $\widetilde W_i(r)/\varepsilon$ 中，唯一发散项是 $i=r=0$；其质量趋于正无穷。其余项的极限为
$$
\binom3r z^r\,(i+r-1)!(y+1)_{6-i-r},
\qquad i+r\ge1.
\tag{5.1}
$$
令 $L=y+5$，则 (5.1) 与 $\binom3r z^r/\binom L{i+r-1}$ 仅差同一正因子 $(y+5)!/y!$。因此发散质量准确强制第一个单项多项式在零点为零；其余三个分布准确趋于真实 $n=1$ 所需分布。这就是 (1.2) 在非法 $\binom L{-1}$ 位置的强制根规则。

尤其 $b_0/\varepsilon\to\infty$，而 $b_i/\varepsilon$（$i=1,2,3$）及所有 $a_i/\varepsilon$ 均趋于有限正常数；$\mu_0\to0$。因此 (2.2)–(2.3) 准确趋于真实 $H_0,H_1,H_2$，其中左侧平行和趋于 $wb_1$。没有把发散的单独分布范数当成源费用。

完整证书给
$$
N_1(\varepsilon-1,y,z)=\varepsilon^8\widehat N_1(\varepsilon,y,z),
\quad
N_2(\varepsilon-1,y,z)=\varepsilon^{10}\widehat N_2(\varepsilon,y,z),
$$
$$
N_3(\varepsilon-1,y,z)=\varepsilon^8\widehat N_3(\varepsilon,y,z).
\tag{5.2}
$$
全部 $\widehat N_i$ 系数非负；在 $\varepsilon=0$ 时，分别有 $759,1106,715$ 个严格正整数项，且每个都含至少一个 $y^0z^k$ 正项。可以取以下明确锚：
$$
[y^0z^{23}]\widehat N_1(0,y,z)=3370285969440768000,
$$
$$
[y^0z^{29}]\widehat N_2(0,y,z)=1802621524226605056000,
$$
$$
[y^0z^{23}]\widehat N_3(0,y,z)=4814694242058240000.
\tag{5.3}
$$
所以三个边界多项式对所有 $y\ge0,z>0$ 都严格正。

为确认它们正是行列式的费用而非无关消失阶，全部分布除以 $\varepsilon$ 时，$P$ 由 (3.1) 的齐次次数准确乘 $\varepsilon^{-7}$。再乘 $\varepsilon$ 消去唯一的发散质量，(3.5) 的分母 $prt$ 恰有二阶零，$pqr^2t$ 恰有四阶零。于是三个中间系数的有限极限分别由 (5.2) 的八、十、八阶正首项给出。这里清分母因子的各 $p,q,r,t,a,b,c,d$ 均取自已经除以 $\varepsilon$ 的分布；$\varepsilon(p+wq)(q+wr)^2(c+wd)t/w$ 因而也趋于正常数。故真实低端 $\det K>0$，且 $K_{11}>0$ 仍由两值序列的严格比较得到。

这证明所有 $h\ge3$ 的 $n=1$。其余已经处理的内部高度一起覆盖 $1\le n\le h-2$。

## 6. 另一端、高度二及准确范围

[完整正权倒数对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)把高度 $n$ 与 $h-n$ 对应，并将这里的 $(z,w)$ 换成 $(z^{-1},w^{-1})$，同时保持真实完整逆及共同源合同。因此第 5 节给最后高度 $n=h-1$。这不是把左核或源 Gram 删掉后的形式反射。

$h=2$ 时 $L=4$，本块属于[四个异常正权加等权池的整个高度二严格系数一](R239-appendix-four-exceptional-weights-full-height-two-primitive-gram-bound.md)。所以所有 $h\ge2$ 都已覆盖，得到 (1.3)。原真实第一下降常数因而严格小于 $((n+1)/n)^2\le4$。

这里始终只处理短串长度三、相对出生三的完整二维块。短串长度三但相对出生一、二的二维块没有被本证书处理；更长短串及原一般多权也不自动跟随。本文与两组任意重数加一异常位的固定高度研究互补，普通 ISP 及原高孔窄源比较继续开放。
