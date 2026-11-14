# R765：原 sigma 截断边界的 Cartier 单位残差

日期：2026-11-14。状态：**已证明。**

本篇固定 R698/R760 的原 $c=0$ sigma 和原变量 $w=u^6$。
它证明原低阶 $T$ 的一个二次卷积严格等于原 Cartier 单位 $B$，
并精确说明为什么不能把低阶 $\overline T$ 延伸成满足同一方程的
完整 $\mathbf F_p$ 幂级数。原下一项的 $p$ 分母正好抵消该单位残差。

该非零卷积尚未被识别为同一个真本原 $h$ 的
$U_hV_h$ 或带原 Legendre 范数的三因子；本篇不声称已完成这一筛选。

## 1. 原变量、原符号与允许范围

固定
$$
E_0:y^2=x^3-1,\qquad dz=dx/(2y),\qquad
p=6N+5\ge41,\qquad u=x^{-1/2}=z+O(z^7),\qquad w=u^6.
\tag{765.1}
$$
原 Weierstrass sigma 满足
$$
\sigma(z)=z+O(z^7),\qquad D_z^2\log\sigma=-x,
\qquad \sigma(z)^6=u^6T(w).
\tag{765.2}
$$
保留 R698 的全部原归一，写
$$
L(w)=\log T(w)=\sum_{j\ge1}\frac{h_j}{j}w^j,
\qquad H(w)=1+wL'(w)=\sum_{j\ge0}h_jw^j,
\tag{765.3}
$$
其中
$$
h_0=1,\qquad (6j-1)h_j=(6j-4)h_{j-1}\quad(j\ge1).
\tag{765.4}
$$
所有导数在本篇均相对于 $w$，除非明确写 $D_z$。
尤其 $H$ 的常数项为一；$L$ 的常数项为零。

对 $0\le j\le N$，(765.4) 的全部分子、分母都非零模 $p$。
所以
$$
h_j\in\mathbf Z_p^\times\quad(0\le j\le N),\qquad
L\bmod w^{N+1}\in w\mathbf Z_p[w]/(w^{N+1}).
\tag{765.5}
$$
因为 $N+1<p$，指数展开至次数 $N+1$ 的各阶乘均为单位。
特别原
$$
T(w)=\sum_{j\ge0}t_jw^j,\qquad t_0=1
\tag{765.6}
$$
有 $t_0,\ldots,t_N\in\mathbf Z_p$。
不预设 $t_{N+1}$ 整；下文会准确求其首个极点。

为避免混淆，令
$$
\mathcal T(w)=\sum_{j=0}^{N}\overline t_jw^j\in\mathbf F_p[w].
\tag{765.7}
$$
这是一个确切次数至多 $N$ 的多项式代表，不是未经说明的完整
$\mathbf F_p[[w]]$ 解。$\mathcal T(0)=1$，故其倒数以及
$\mathcal T'/\mathcal T$ 可在形式幂级数环中使用。

## 2. 两个线性方程及其准确非线性形式

由 (765.4) 对每个 $j\ge1$ 的系数相加，得到特征零中的恒等式
$$
6w(1-w)H'=(1+2w)H-1.
\tag{765.8}
$$
确实，左减右的 $w^j$ 系数为
$$
(6j-1)h_j-(6j-4)h_{j-1},
\tag{765.9}
$$
而常数项为 $-h_0+1=0$。

置 $R=T'/T=(H-1)/w$。代入 $H=1+wR$ 得
$$
6w(1-w)R'=(-5+8w)R+2.
\tag{765.10}
$$
这是 $R$ 的有理系数线性方程；它本身不是 $T$ 的有限宽度线性递推。

对任意常数项一的可逆幂级数 $A$，定义
$$
\mathscr Q(A)=
6w(1-w)(AA''-A'^2)+(5-8w)AA'-2A^2,
\tag{765.11}
$$
以及
$$
H_A=1+wA'/A,\qquad
\mathscr E(H_A)=6w(1-w)H_A'-(1+2w)H_A+1.
$$
则有**不依赖截断的代数恒等式**
$$
\boxed{\mathscr E(H_A)=w\,\mathscr Q(A)/A^2.}
\tag{765.12}
$$
证明只需 $R_A=A'/A$，以及
$R_A'=(AA''-A'^2)/A^2$；先展开
$\mathscr E(1+wR_A)$，其常数项消去，剩下
$w\{6w(1-w)R_A'+(5-8w)R_A-2\}$。
因此对原特征零 $T$，$\mathscr Q(T)=0$。

## 3. 原低阶截断的首个非零残差

**定理 765.1。** 对 (765.7) 的原截断，有
$$
\boxed{
\mathscr Q(\mathcal T)
\equiv 3\overline h_Nw^N\pmod{w^{N+1}}
\quad\text{于 }\mathbf F_p[w].
}
\tag{765.13}
$$
特别首个显示系数严格非零：
$$
[w^j]\mathscr Q(\mathcal T)=0\ (0\le j<N),\qquad
[w^N]\mathscr Q(\mathcal T)=3\overline h_N\in\mathbf F_p^\times.
\tag{765.14}
$$

证明。由原 $T$ 的整低阶系数，
$$
H_{\mathcal T}=1+w\mathcal T'/\mathcal T
\equiv\sum_{j=0}^{N}\overline h_jw^j\pmod{w^{N+1}}.
\tag{765.15}
$$
用 $\widetilde h_{N+1}$ 表示 $H_{\mathcal T}$ 的下一系数。
它确实存在于 $\mathbf F_p$；它不是极点系数 $h_{N+1}$ 的约化。
由 (765.9)，$\mathscr E(H_{\mathcal T})$ 的次数
$1,\ldots,N$ 系数为零，次数 $N+1$ 的系数是
$$
\begin{aligned}
\bigl(6(N+1)-1\bigr)\widetilde h_{N+1}
 -\bigl(6(N+1)-4\bigr)\overline h_N
&=p\widetilde h_{N+1}-(p-3)\overline h_N\\
&=3\overline h_N.
\end{aligned}
\tag{765.16}
$$
常数项也为零。因此
$\mathscr E(H_{\mathcal T})\equiv3\overline h_Nw^{N+1}$
模 $w^{N+2}$。将 (765.12) 乘上
$\mathcal T^2$ 再除去显式因子 $w$，由于
$\mathcal T^2(0)=1$，正好得到 (765.13)。
最后 (765.5) 给非零性。$\square$

这里的系数错位必须保留：$H$ 方程的首个失败项在 $w^{N+1}$，
$T$ 的非线性方程的首个失败项在 $w^N$。

### 3.1 为何二阶导数没有暗中要求一个可约化的下一项

直接从 (765.11) 可见，若把 $\mathcal T$ 换成
$A=\mathcal T+c w^{N+1}$，则 $\mathscr Q(A)$ 的 $w^N$ 系数可能受到
$A''$ 和 $A'$ 的影响。然而其**全部**改变量恰为
$$
\begin{aligned}
6N(N+1)c+5(N+1)c
&=(N+1)(6N+5)c\\
&=p(N+1)c=0\quad\text{于 }\mathbf F_p.
\end{aligned}
\tag{765.17}
$$
次数至少 $N+2$ 的项经过 (765.11) 的微分及所带因子后，
不影响次数至多 $N$ 的系数。
所以 (765.13) 确由 $\mathcal T$ 本身决定；不能通过任意添一个
整的下一系数消去该残差。

## 4. 残差就是同一个原 Cartier 单位

R574/R702 使用的原常数为
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbf F_p^\times,
\qquad D_z^{p-1}x=-B.
\tag{765.18}
$$
它与本篇残差的关系没有额外周期、isogeny 或 Gaussian 标度：
$$
\boxed{3\overline h_N=B.}
\tag{765.19}
$$

证明。从原递推的乘积式，
$$
\overline h_N
=\prod_{j=1}^{N}\frac{6j-4}{6j-1}
=(-1)^N3^{-N}\frac{\prod_{j=1}^{N}(3j-2)}{N!},
\tag{765.20}
$$
其中第二等式用了 $6j-1\equiv-6(N+1-j)\pmod p$。
另一方面，利用 $2N+1+(N+1)=3N+2$，
$$
\begin{aligned}
B
&=(-1)^{N+1}\prod_{j=1}^{N+1}\frac{2N+1+j}{j}\\
&=(-1)^{N+1}3^{-(N+1)}
 \frac{\prod_{j=1}^{N+1}(3j-2)}{(N+1)!},
\end{aligned}
\tag{765.21}
$$
因为 $3(2N+1+j)\equiv3j-2\pmod p$。
各显示分母均为单位。将 (765.21) 除以 (765.20)，得到
$$
\frac{B}{\overline h_N}
=-\frac{3N+1}{3(N+1)}=3\quad\text{于 }\mathbf F_p,
\tag{765.22}
$$
最后一步使用 $3N+1+9(N+1)=12N+10=2p$。
这证明 (765.19)。$\square$

因此 (765.13) 可准确写成
$$
\boxed{\mathscr Q(\mathcal T)=B w^N+O(w^{N+1}),\qquad B\ne0.}
\tag{765.23}
$$

## 5. 完整展开为一个非零二次卷积

记 $\tau_i=\overline t_i$，并在下面有限和中令
$0\le i,j\le N$。把 $AA''-A'^2$ 的系数对 $i,j$ 对称化，
(765.23) 等价于
$$
\boxed{
\begin{aligned}
B={}&
\sum_{i+j=N+1}
\left(3(i-j)^2-\frac{N+1}{2}\right)\tau_i\tau_j\\
&-\sum_{i+j=N}
\left(3(i-j)^2+N+2\right)\tau_i\tau_j
\quad\text{于 }\mathbf F_p.
\end{aligned}
}
\tag{765.24}
$$
两和均按有序对计；$2$ 是单位。

核对如下。在 $AA''-A'^2$ 中，总指标 $i+j=s$ 的对称化系数为
$\tfrac12((i-j)^2-s)$；在 $AA'$ 中为 $s/2$。
$6w$ 和 $5$ 两项取 $s=N+1$，给
$3(i-j)^2-(N+1)/2$。
$-6w^2$、$-8w$ 和 $-2A^2$ 三项取 $s=N$，
给 $-3(i-j)^2-N-2$。这是 (765.24) 的全部项。

特别至少一个右端带权单项非零。
这是原 $T$ 的确定非零卷积；没有重新选择 $T$、Gaussian 或基点。
但它混合两个相邻总指标 $N$ 与 $N+1$，
也还没有带入 $C,Z$ 和原本原/Legendre 投影。

## 6. 原下一项的极点恰好恢复特征零方程

在特征零中，(765.4) 的下一步是
$$
p h_{N+1}=(p-3)h_N.
\tag{765.25}
$$
故
$$
v_p(h_{N+1})=-1,\qquad
p h_{N+1}\equiv-3\overline h_N=-B\pmod p.
\tag{765.26}
$$
因为 $N+1$ 是单位，$[w^{N+1}]L=h_{N+1}/(N+1)$ 也恰有一阶极点。
在 $T=\exp L$ 的 $w^{N+1}$ 系数中，除线性项
$[w^{N+1}]L$ 外，每个项只使用 $L_1,\ldots,L_N$
及至多 $(N+1)!$ 的单位分母。因此这些其余项都整，且
$$
\boxed{
v_p(t_{N+1})=-1,\qquad
p t_{N+1}\equiv-\frac{B}{N+1}
\equiv-6B\pmod p.
}
\tag{765.27}
$$

将真正的 $t_{N+1}w^{N+1}$ 放回原 $T$，
其对 $[w^N]\mathscr Q$ 的贡献不是零，而是
$$
p(N+1)t_{N+1}\equiv-B\pmod p.
\tag{765.28}
$$
这准确抵消截断的 $B$，与特征零恒等式 $\mathscr Q(T)=0$ 一致。
这里不能先把 $p$ 约化为零再丢掉 $t_{N+1}$ 的极点。

于是不存在 $A\in\mathbf F_p[[w]]$ 满足
$$
A\equiv\mathcal T\pmod{w^{N+1}},\qquad
A(0)=1,\qquad \mathscr Q(A)=0.
\tag{765.29}
$$
事实上 (765.17) 证明任意这样的整扩展仍保留非零的 $w^N$ 残差。

## 7. 与真正同标签问题的接口和边界

R760 固定的实际非端点标签为
$$
h=6a+1,\qquad 1\le a\le N,\qquad (h,p+1)=1,
$$
并且
$$
U_h=[w^{a-1}]\mathcal T C Z^{2-h},\qquad
V_h=[w^{N-a}]\mathcal T Z^{h+2},
\tag{765.30}
$$
$$
\overline N_h=-P_{h-1}(1/\sqrt{-3})^2.
\tag{765.31}
$$
所有这些抽取仍只使用至多 $N$ 的合法整系数。
本篇没有把它们延伸越过 (765.27) 的极点。

(765.24) 提供的是 $\tau_i\tau_j$ 的带权非零二次组合。
要从中推出所需结论，还必须证明它能在保留 $C,Z$ 换参的同时，
化成由同一真本原 $h$ 且 $N_h$ 为单位的 $U_hV_h$ 所构成的组合，
或者得到足够强的公共零排除。这个步骤本篇尚未证明。

因此不能将“至少一个 (765.24) 的单项非零”改写成“三单位标签已存在”。
原主目标和真实高度排除的完成标准保持不变。

## 依赖

- [R698](R698-two-actual-square-roots-at-one-low-degree.md)：原 $H,L,T,C,Z$ 和同一 $w=u^6$。
- [R760](R760-original-critical-sigma-jets-from-four-digit-division-data.md)：合法低阶整性、原普通导数及全部同标签系数。
- [R574](R574-completed-zeta-Cartier-input.md)、[R702](R702-first-pole-block-and-uniform-shifted-units.md)：原 $D_z^{p-1}x=-B$ 及固定的二项式标度。

本篇全部为形式恒等式与整性证明，没有新增或重跑正式计算。
