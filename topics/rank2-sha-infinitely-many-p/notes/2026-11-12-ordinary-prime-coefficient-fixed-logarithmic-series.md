# 普通首权商：固定的两条系列及其相消

日期：2026-11-12。状态：以下恒等式与整性已证明；首权商对无穷素数非零仍未证明。
本篇使用 R51 的已认证实际截面，不用近年预印本作输入。

## 1. 固定坐标与三个有理系列

对 $E_D:y^2=x^3-Dx$，在原点取 $u=x^{-1/2}=z+O(z^5)$，
并令 $v=Du^4$。由 $dx/dz=2y$，选原点的正确平方根，得到
$$
\frac{du}{dz}=\sqrt{1-v},\qquad
z=uF(v),\qquad
F(v)=\sum_{n\ge0}\frac{c_n}{4n+1}v^n,\quad
c_n=\frac{\binom{2n}{n}}{4^n}.
\tag{1}
$$
特别是
$$
F+4vF'=(1-v)^{-1/2}.
\tag{2}
$$

设 $\vartheta_D(z)^2=x(z)\sigma_D(z)^2$，
$\vartheta_D(0)=1$，并写
$\Theta(v)=\vartheta_D(z(u))$。
这个 $\Theta\in1+v\mathbb Q[[v]]$ 与 $D$ 无关，准确满足
$$
\frac{\Theta'}{\Theta}
 =\frac{H(v)}{4\sqrt{1-v}},\qquad
H(v)=\sum_{n\ge0}\frac{c_n}{4n+3}v^n.
\tag{3}
$$
验证如下：$\vartheta_D=\sigma_D/u$，而
$d\zeta_D/du=-u^{-2}(1-Du^4)^{-1/2}$，故
$$
u\zeta_D(z(u))
 =1-\sum_{n\ge1}\frac{c_n}{4n-1}v^n.
$$
再用
$[v^n]\sqrt{1-v}=-c_n/(2n-1)$（$n\ge1$）及
$2nc_n/(2n-1)=c_{n-1}$，即得 (3)。
这也固定了符号和积分常数；例如 $\Theta=1+v/12+\cdots$。

定义完全固定的有理系列
$$
q(v)=v+\frac35v^2-\frac15v^3+\frac15v^4,\qquad
B(v)=\Theta(v)^{17}q(v),\qquad
W(v)=\frac{B(v)}{\sqrt{1-v}}=\sum_{n\ge1}w_nv^n.
\tag{4}
$$
R51 的实际 $E_{17}$ 截面正是
$$
A(z(u))=\frac1{17}B(17u^4).
\tag{5}
$$
一般 $D$ 的同型表达式 $D^{-1}B(Du^4)$ 只是为核对缩放而引入；
本文不称它为每条 $E_D$ 的 Katz 中央因子。

## 2. 准确的 residue 换元

令 $p=4r+1$ 是普通目标素数，$p\ge13$、$p\ne17$。
记 $b_m=[z^m]A(z)$。由 (1)，形式 residue 换元给
$$
\begin{aligned}
b_{p-1}
 &=\operatorname{res}_{z=0}\frac{A(z)\,dz}{z^p}\\
 &=17^{r-1}[v^r]\,
       W(v)F(v)^{-p}.
\end{aligned}
\tag{6}
$$
此式没有近似，也没有 $p$-进周期。等价的 Lagrange 形式是
$$
b_{p-1}
 =\frac{17^{r-1}}r[v^{r-1}]B'(v)F(v)^{1-p}.
\tag{7}
$$
(6) 比 (7) 更适合除以 $p$ 后的计算。

## 3. 截断整性：危险的 $F_r$ 确实不出现

$F_r=c_r/p$ 可能有 $p$ 分母，因此不能笼统声称 $F$ 到 $v^r$ 都整。
但 $W(0)=0$，所以 (6) 只使用 $F$ 到 $v^{r-1}$。
在这个范围 $4n+1<p$，从而
$$
F\bmod v^r\in\mathbb Z_p[v]/(v^r).
\tag{8}
$$
同样，计算 $B,W$ 到 $v^r$ 只需 (3) 的系数到 $v^{r-1}$。
此时 $4n+3\le4r-1=p-2$，而解 (3) 的递推只除以 $1,\ldots,r$。
于是
$$
\Theta,B,W\bmod v^{r+1}\in\mathbb Z_p[v]/(v^{r+1}).
\tag{9}
$$
因为 $F(0)=1$，形式 $\log F\bmod v^r$ 所需的整数分母也都小于 $p$。
故在所需截断中可以严格使用
$$
F^{-p}=\exp(-p\log F)\equiv1-p\log F\pmod{p^2}.
\tag{10}
$$
这里指数式只用有限项；$n\ge2$ 项的 $p^n/n!$ 均在 $p^2\mathbb Z_p$。

综合 (6) 与 (10)，得到
$$
\boxed{
b_{p-1}\equiv17^{r-1}
 \left(w_r-p[v^r]W\log F\right)\pmod{p^2}.
}
\tag{11}
$$
R51 已证明本题 $b_{p-1}\in p\mathbb Z_p$，
而 (9) 保证右侧另一个贡献为 $p$ 倍，所以同时有
$$
w_r\in p\mathbb Z_p.
\tag{12}
$$
因此除以 $p$ 是合法的，且
$$
\boxed{
\frac{b_{p-1}}p\equiv
17^{r-1}\left(\frac{w_r}p-[v^r]W\log F\right)\pmod p.
}
\tag{13}
$$

## 4. 甚至可以合并为一个固定的有理系列

定义
$$
I(v)=\sum_{n\ge1}\frac{w_n}{4n+1}v^n,\qquad
G(v)=I(v)-W(v)\log F(v)\in\mathbb Q[[v]].
\tag{14}
$$
则 $4vI'+I=W$。对 $p=4r+1$，(12) 正好保证 $[v^r]I$ 在 $p$ 处整，
于是 (13) 可写为
$$
\boxed{
[v^r]G\in\mathbb Z_p,\qquad
\frac{b_{p-1}}p\equiv17^{r-1}[v^r]G\pmod p.
}
\tag{15}
$$
这是同一个固定 $G$ 的素数对角，不是按 $p$ 改定义一个系列。
但索引仍是 $r=(p-1)/4$，不能把 (15) 当成同一个固定代数数的模 $p$ 约化。

由 R51，若能证明
$$
[v^{(p-1)/4}]G\not\equiv0\pmod p
$$
对无穷多个普通目标素数成立，便得到本题所需的无穷性。
目前 (15) 是充分证书的准确转写；没有证明这条非消失。
更不能仅证明 $w_r/p$ 或 $[v^r]W\log F$ 非零便停止：
需要排除这两项在 $\mathbb F_p$ 中相等。

## 5. 与普通 Mellin 导数的关系

沿用[普通斜率笔记](2026-11-12-ordinary-theta-slope-convolution-and-weight-moments.md)
的 $M_1$。实际单位矩为
$$
M_1=
\left(1-\frac{\pi^{p-1}}{\bar\pi^p}\right)
\Omega_p^{p-1}(p-1)!\,b_{p-1}.
$$
那里已证明
$$
\log(1+p)J_p'(0)\equiv\frac{M_1}{p-1}\pmod{p^2}.
\tag{16}
$$
故 (15) 非零准确检测首导数的单位情形。
它不声称 $[v^r]G\equiv0$ 就有 $J_p'(0)=0$；
较高估值的非零导数仍可用该笔记的高阶 Newton 证书检测。

实现见
[固定系列的模 $p^2$ 计算](../scripts/check-ordinary-fixed-log-series.py)。
脚本只用所列有限递推，默认检查 $p=13,29,37,41$；
$p=13$ 还与 R51 的独立准确值
$b_{12}=9313603/50400$ 比较，得到
$b_{12}/13\equiv12\bmod13$。
有限样例没有被用来推断 (12) 或无穷性。
