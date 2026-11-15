# R658 — 原五来源辅助空间的真实 Gaussian 子式与二次 jet 长度

日期：2026-11-15。**状态：已证明。**

本篇针对 R644 已经使用的同一个特征零辅助空间
$$
u^{66D}L(66D\,O)\cdot
\operatorname{span}\{1,h,\ldots,h^{72D}\},
\qquad h=\sigma/z,\quad z=uH(bu^6).
$$
用一个辅助好惰性素数 $q$ 构造其真实有理系数矩阵的非零子式。子式的所有行都位于一个连续原 $u$ 前缀内，而且
$$
J_D\le66D+72D(q+1)
=\bigl(5184+o(1)\bigr)D^2
$$
可取。这里 $q$ 是大于 $72D$ 和固定坏界的最小素数 $5\bmod6$。

证明保留全部原 sigma、$z/u$ 及椭圆有理因子。只在长度严格小于 $q(q+1)$ 的有限窗口上取 Gaussian 指数，因而全部阶乘都是 $q$ 单位。所用正规高尾在辅助分歧换元后严格落入 $\pi$，不是将原高尾删除。

辅助素数处一个归一子式为单位，并不控制该有理子式在其他素数处的分子。全篇不声称无例外的跨素数整性 cutoff，也不改变旧 $M$、同一个 $R$ 或原完整中央条件。

## 1. 同一辅助空间及真实列

固定原模型
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
dz=\frac{dx}{2y},\quad x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots.
$$
保持 R644 的原参数
$$
u=x^{-1/2},\quad x=u^{-2},\quad
y=-u^{-3}(1+bu^6)^{1/2},\quad
z=uH(bu^6),
\tag{1}
$$
平方根取常数项一。这里 $u$ 不是 $-x/y$。

先给一般有限参数的结论。取整数 $K\ge2$、$M\ge0$，并令
$$
\mathcal V_{K,M}
=\operatorname{span}_{\mathbf Q}
\{x^a y^\delta H_0^m:
 a\ge0,\ \delta\in\{0,1\},\
 2a+3\delta\le K,\ 0\le m\le M\}.
\tag{2}
$$
$H_0$ 先是一个符号。将它代为原固定 $h(z(u))=\sigma(z(u))/z(u)$，
并乘 $u^K$，得到真实有理系数列
$$
B_{a,\delta,m}(u)
=u^Kx(u)^ay(u)^\delta h(z(u))^m
\in\mathbf Q[[u]].
\tag{3}
$$
这里没有使用完整中央正规 $h/E_{\rm c}$ 代替 $h$。

椭圆函数 $x^ay^\delta$ 的原点极阶 $2a+3\delta$ 彼此不同，且恰为
$$
\{0,2,3,\ldots,K\}.
$$
所以
$$
r=K-2a-3\delta
$$
恰遍历集合
$$
\mathcal R_K=\{0,1,\ldots,K\}\setminus\{K-1\},
\qquad|\mathcal R_K|=K.
\tag{4}
$$
每个 $r$ 唯一指定 $(a,\delta)$。于是可将 (3) 记为
$$
B_{r,m}(u)=(-1)^{\delta(r)}u^r
(1+bu^6)^{\delta(r)/2}h(z(u))^m,
\quad r\in\mathcal R_K,\ 0\le m\le M.
\tag{5}
$$
实际列数为 $N=K(M+1)$。R644 的空间准确对应
$$
K=66D,\qquad M=72D.
\tag{6}
$$
原五来源的关系 $SH_{38}=T$ 及其实际有理系数不变；(2) 是原论证中已经支付的辅助空间，不是新增算术来源池。

## 2. 辅助素数与完整 z/u 因子

取
$$
q\equiv5\pmod6,\qquad q>\max(K,M,101),
\quad L=q+1,\quad \pi^L=q.
\tag{7}
$$
在 $\mathcal O'=\mathbf Z_q[\pi]$ 上按 $v_\pi(\pi)=1$ 计赋值。该环是完全分歧 DVR，剩余域为 $\mathbf F_q$。

先直接证明原 $H$ 的高尾。由 (1) 的微分身份，
$$
H(bu^6)=\sum_{n\ge0}
\frac{\binom{-1/2}{n}b^n}{6n+1}u^{6n}.
\tag{8}
$$
因 $q$ 为奇素数，分子在 $\mathbf Z_q$ 中整。置 $e=v_q(6n+1)$。
若 $e=0$ 且 $n>0$，代入 $u=\pi v$ 后系数的 $\pi$ 赋值至少 $6n>0$。

若 $e=1$，由 $q\equiv5\pmod6$ 和 $6n+1\equiv1\pmod6$，正整数 $(6n+1)/q$ 至少为五，故
$$
6n-L\ge5q-1-(q+1)=4q-2>0.
$$
若 $e\ge2$，则
$$
6n-eL\ge q^e-1-e(q+1)>0.
$$
最后一不等式在 $e=2$ 成立，随 $e$ 递增严格增强。因此
$$
\boxed{
H(b\pi^6v^6)\in1+\pi\mathcal O'[[v]].
}
\tag{9}
$$
这些系数的赋值还随 $n$ 趋于无穷，所以 (9) 实际上是 Tate 单位。完整平方根
$(1+b\pi^6v^6)^{1/2}$ 及其逆同样整，模 $\pi$ 为一。

这付清了全部原换参，不以 $z=u$ 取代 $z=uH$。

## 3. 第一 Gaussian 与全部 regular 高尾

令 $c_q$ 为原 $\log(\sigma/z)$ 在 $z^{q+1}$ 处的系数，取原规范而不加任意自由参数。R301/R618 给
$$
v_q(c_q)=-1,\qquad a_q:=qc_q\in\mathbf Z_q^\times,
$$
以及准确形式分解
$$
h(z)=e^{c_qz^L}U_q(z),\qquad U_q(0)=1.
\tag{10}
$$
若 $U_q(z)=\sum_{\ell\ge0}u_\ell z^\ell$，R618 的完整系数界等价于
$$
v_q(u_\ell)\ge-\lfloor\ell\tau_q\rfloor,\qquad
\tau_q=\frac{2q-1}{q(q^2-1)}.
\tag{11}
$$
非六的倍数处系数为零，也满足该界。

对 $\ell>0$，
$$
v_\pi(\pi^\ell u_\ell)
\ge\ell-L\lfloor\ell\tau_q\rfloor
\ge\ell(1-L\tau_q)>0,
$$
因为
$$
L\tau_q=\frac{2q-1}{q(q-1)}<1.
\tag{12}
$$
由此 $U_q(\pi v)$ 及其逆是模 $\pi$ 等于一的整 Tate 单位。再用 (9) 作真实复合，得到
$$
\boxed{
U_q\!\left(\pi vH(b\pi^6v^6)\right)
\in1+\pi\mathcal O'[[v]].
}
\tag{13}
$$
复合合法：内变量的常数项为零，系数整；每个固定系数只有有限项贡献。严格的线性赋值增长还保证所需闭单位盘内的解析复合。

另一方面，第一 Gaussian 准确为
$$
c_qz(\pi v)^L
=a_qv^L H(b\pi^6v^6)^L.
\tag{14}
$$
不能把 (14) 的全指数当成整系数级数；在本篇只需下述明确有限窗口。

定义最大读取行号
$$
J=K+ML.
\tag{15}
$$
由 $K<q<L$ 和 $M<q$，
$$
\boxed{J<qL.}
\tag{16}
$$
对次数不超过 $J$ 的系数，(14) 的指数只使用
$$
j=0,\ldots,M<q,
$$
因为 $K<L$。因此这些 $j!$ 全是 $q$ 单位。由 (9)，在此**整个**有限窗口中有
$$
\exp\{ma_qv^LH(b\pi^6v^6)^L\}
\equiv e^{m\bar a_qv^L}\pmod\pi
\qquad(0\le m\le M).
\tag{17}
$$
右端也仅按次数 $\le J$ 读取。(17) 没有延伸到第 $q$ 个 Gaussian 项，更没有忽略该处的 $q!$ 分母。

将 (9)、(13)、(17) 代回原列 (5)，得到
$$
\boxed{
\pi^{-r}B_{r,m}(\pi v)
\in\mathcal O'[v]/(v^{J+1}),\qquad
\pi^{-r}B_{r,m}(\pi v)
\equiv(-1)^{\delta(r)}v^r
e^{m\bar a_qv^L}\pmod\pi.
}
\tag{18}
$$
为说明取商中的表示没有混淆高项，(18) 只断言归一列在 $v$ 次数 $\le J$ 的系数整且有显示约化；所有需要的原矩阵行均在此范围内。原 $z/H$、sigma 高尾及椭圆因子均已经逐项支付。

## 4. 真实有理子式及其准确 q 赋值

从原普通 $u$ 系数矩阵中选取行
$$
\mathcal I=
\{r+jL:r\in\mathcal R_K,\ 0\le j\le M\}.
\tag{19}
$$
这些行彼此不同，因为全部 $r$ 都小于 $L$。它们位于连续前缀
$$
0,1,\ldots,J,
$$
且最大行恰为 $J$：$r=K$ 是原常数椭圆列对应的合法余类。

定义实际有理行列式
$$
\Delta_{K,M,q}
=\det\bigl([u^{r'+jL}]B_{r,m}(u)\bigr)_{
 (r',j)\in\mathcal R_K\times\{0,\ldots,M\},
 (r,m)\in\mathcal R_K\times\{0,\ldots,M\}}.
\tag{20}
$$
可把行列按 $r$ 分块排序；换成原递增行序只改一个符号。

对 (20) 每行乘 $\pi^{r'+jL}$、每列乘 $\pi^{-r}$。由 (18)，归一矩阵整，约化后按 $r$ 分成 $K$ 个方块。第 $r$ 块恰为
$$
(-1)^{\delta(r)}
\left(\frac{(m\bar a_q)^j}{j!}\right)_{0\le j,m\le M}.
\tag{21}
$$
不同 $m=0,\ldots,M$ 在 $\mathbf F_q$ 中不同。普通 Vandermonde 行列式给
$$
\det\left(\frac{(m\bar a_q)^j}{j!}\right)
=\bar a_q^{M(M+1)/2}
 \frac{\prod_{0\le m<m'\le M}(m'-m)}
      {\prod_{j=0}^{M}j!}
=\bar a_q^{M(M+1)/2}\ne0.
\tag{22}
$$
最后一步使用
$\prod_{0\le m<m'\le M}(m'-m)=\prod_{j=1}^{M}j!$。
所以归一后的完整矩阵是整单位矩阵。

行缩放指数减列缩放指数准确为
$$
\begin{aligned}
&\sum_{r\in\mathcal R_K}\sum_{j=0}^{M}(r+jL)
-\sum_{r\in\mathcal R_K}\sum_{m=0}^{M}r\\
&\hspace{30mm}=KL\,\frac{M(M+1)}2.
\end{aligned}
$$
因为 $v_\pi(q)=L$，因此有更准确的证书
$$
\boxed{
v_q(\Delta_{K,M,q})=-K\frac{M(M+1)}2.
}
\tag{23}
$$
尤其
$$
\boxed{
q^{KM(M+1)/2}\Delta_{K,M,q}\in\mathbf Z_q^\times.
}
\tag{24}
$$
(20) 是原固定特征零级数的有理系数子式；(23) 只是利用一个辅助素数证明其非零。不是另一个正规来源的子式，也不是只在模 $q$ 环境中的形式维数计数。

## 5. 连续前缀结论及 R644 的二次长度

**定理。** 对全部 (2)、(7) 参数，原固定列 (3) 的连续普通 $u$ 前缀
$$
([u^n]B_{r,m})_{0\le n\le J},
\qquad J=K+M(q+1),
\tag{25}
$$
全列满秩。任意非零特征零线性组合的原点接触不超过 $J$。显示子式 (20) 同时支付其完整原高尾和准确辅助素数赋值 (23)。

**证明。** (20) 是 (25) 的一个实际非零列满秩子式。系数域扩张不改变这个秩，故任何非零线性组合在 $0,\ldots,J$ 中至少有一个非零系数。证毕。

对 R644 的参数 (6)，取 $q_D$ 为大于 $\max(72D,101)$ 的最小素数 $5\bmod6$。固定模数六的素数定理给
$$
q_D=(72+o(1))D.
\tag{26}
$$
同一输入的作者正文与量词见 K. S. Kedlaya，*Notes on analytic number theory*，§4.4，Theorem 4.12，
[Primes in arithmetic progressions](https://kskedlaya.org/ant/chap-primes-in-ap.html)。
只用 $\pi(x;6,5)\sim x/(2\log x)$ 推出任意固定相对长度区间最终含这种素数，不使用增长模数或未付短区间界。

所以 R644 中逐行保留提高秩行的确定算法至迟在
$$
\boxed{
J_D\le66D+72D(q_D+1)
=\bigl(5184+o(1)\bigr)D^2
}
\tag{27}
$$
结束。也可以直接用 (19) 的显示行集替代该贪心选行规则，并将 (20) 作为 R644 的 $\Delta_D$。二者都属于同一个原有理系数空间。

(27) 给出的是最大行号；连续前缀的长度为该数加一。一个完全可计算、无渐近符号的界就是 (27) 左侧的显示整数。

## 6. 证书范围和全局预算边界

本篇的辅助素数 $q_D$ 与 R644 最终应用时的惰性素数 $p$ 是不同量词。具体地：

- (20) 是一个固定非零有理数，其归一只在选定辅助 $q_D$ 处为单位。
- 若最终 $p>J_D$ 且 $v_p(\Delta_D)=0$，R644 原完整中央正规后的同一有限 jet 单位性和闭边界论证继续成立。
- (23) 不控制 $\Delta_D$ 在其他素数处的分子，也不能把 $v_p(\Delta_D)=0$ 删除。
- 有理系数的共同分母、整数证书高度及它们随 $D$ 的增长须由原整微分递推另付。这里不因一个辅助子式非零而免费赋予全局高度界。

本篇没有扩大五来源算术零池，也没有给其任意乘积新增完整中央零。原长塔、普通分布、Bost 饱和成本和旧同一个 $R$ 的 $d_2$ 都保持原量词。R657 的 $G_0\mathcal W_D$ 连续前缀与本篇的 $u^KL(KO)h^{\le M}$ 是两个分别付清的真实空间；此处没有用一个包含关系将它们混为同一来源。

## 依赖

- [R644](R644-bounded-degree-original-polynomials-and-full-boundary-obstruction.md)：原五来源、同一辅助空间及闭边界应用。
- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：原 sigma 去第一 Gaussian 后的全部系数界。
- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)：原第一 Gaussian 的一次分母单位。
- [R657](R657-original-long-ordered-prefix-and-quadratic-contact-bound.md)：另一原空间的连续长前缀；本篇不以该空间代替 (2)。
- K. S. Kedlaya，*Notes on analytic number theory*，§4.4，Theorem 4.12，[作者正文](https://kskedlaya.org/ant/chap-primes-in-ap.html)：固定进度中的辅助素数选择。

全篇是原形式级数和有限真实矩阵的证明，不使用新增素数扫描。
