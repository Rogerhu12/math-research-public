# BKT 的有限层 Frobenius 与实际正次数 theta 参考

日期：2026-11-12。状态：已核原始定理，并证明下述实际参考的半径障碍。
这里不否定可能存在尚未建立的特殊周期恒等式；排除的是直接把裸
pure-log 类的有限 unipotent Frobenius 公式当作实际 theta 权导数。

## 1. 使用的原始定理与确切对象

一手来源为 Bannai–Kobayashi–Tsuji，
*On the de Rham and \(p\)-adic realizations of the elliptic polylogarithm
for CM elliptic curves*，
Ann. Sci. Éc. Norm. Sup. **43** (2010), 185–234，
[出版全文](https://www.numdam.org/item/10.24033/asens.2119.pdf)。

本文直接核对了出版版的三个位置：

- Proposition 2.16（pp.202–203）：prime-to-\(p\) 非零挠点 \(P\) 的
  Kronecker 系列 \(\widehat F_{P,b}(t)\) 在整个开正式单位盘收敛；
  Remark 2.17 另把普通处的有界性单列，不能把它移到惰性处。
- Theorem 4.19（p.219）：给出每个有限 \(\mathrm{Log}^N\) 层的
  椭圆 polylog 的可积连接、过滤及 Frobenius。
  此处允许 \(p\ge5\) 在 CM 环中未分歧，确实包括惰性素数。
- Theorem 5.7（p.224）：挠点特化的有限层系数是
  \(e^{(p)}_{-m,k+1}(P)\)、\(e^{(p)}_{-m-1,k}(P)\)，\(m+k\le N\)。
  其后 §5.3／Corollary 5.10 的 Katz \(L\) 值比较明确另假设普通性。

这不是把旧预印本的编号或范围当作出版版。
\(\mathrm{Log}^{(1)}\) 的秩为 \(3\)，所以
\[
\operatorname{rank}\mathrm{Log}^N=\binom{N+2}{2},\qquad
\operatorname{rank}\mathcal P^N=2+\binom{N+2}{2}.
\tag{1}
\]
这些是每个固定 \(N\) 的有限秩对象。原定理本身没有给出本文实际
half-theta 的 weight derivative，也没有断言这些特化一律非零。

## 2. 实际 pure-log 部分确实有一个有限 unipotent 接口

沿用
[实际 pure-log 分解](2026-11-12-actual-rational-reference-pure-logarithmic-form.md)
与[固定 Miller 范数](2026-11-12-short-cycle-miller-and-theta-tangent-norm.md)
的完整规范：
\[
E_0:y^2=x^3-x,\quad \alpha=4-i,\quad
f_0(z)=\theta_T(\alpha z),\quad A=f_0R,
\]
\[
R\omega=\frac1{17}\sum_P\rho_P\,d\log g_P,\qquad
g_P(O)=1,\qquad
\operatorname{div}g_P=17(P)-17(T).
\tag{2}
\]
所有 \(P,g_P,\rho_P\) 属于固定有限数域，与 \(p\) 无关。定义
\[
H(z)=\frac1{17}\sum_P\rho_P\log g_P(z),\qquad H(O)=0.
\tag{3}
\]
则 \(dH=R\omega\)。这是有限个 Kummer 对数的代数线性组合。
例如其微分部分已经可用秩二 unipotent 系统
\[
d\begin{pmatrix}1\\H\end{pmatrix}
 =\begin{pmatrix}0&0\\R\omega&0\end{pmatrix}
  \begin{pmatrix}1\\H\end{pmatrix}
\tag{4}
\]
表示；为包含系数的 Galois/Frobenius 共轭，只需加入固定有限数目的
共轭系统。各 \(g_P\) 的 Kummer Frobenius 也可分别保留。
因此这里的缺口并不是“裸 \(H\) 没有任何有限维几何实现”。

但实际线性化 theta 范数的方向是 \(A=f_0R\)。
分部积分的准确乘法法则为
\[
A=(f_0H)'-f_0'H.
\tag{5}
\]
任何将它送入 R54／R59 的 shifted transform 的比较都必须保留
右边的两个项；(4) 没有包括 \(f_0\) 的指定 theta 平凡化。

## 3. 裸 \(H\) 在惰性处的统一大盘单位

以下固定任意惰性 \(p\ge7\)，使用 \(v_p(p)=1\)。
取原正式参数 \(t=-x/y\)，并置
\[
\widehat H(t)=H(\log_Et).
\]
由于 \(R(t)\in t^4\mathcal O[[t]]\)、\(\omega_E/dt\in\mathcal O[[t]]^\times\)，
积分只除以整数 \(n\)，所以
\[
\widehat H(t)=\sum_{n\ge5}h_nt^n,\qquad
h_5=1/5,\qquad v_p(h_n)\ge-v_p(n).
\tag{6}
\]
\(R([i]P)=R(P)\) 和 \([i]^*\omega=i\omega\) 给
\(\widehat H(it)=i\widehat H(t)\)，故仅 \(n\equiv1\pmod4\) 出现。

令
\[
\rho=p^{-1/(2p)}.
\]
则有比开单位盘收敛更明确的
\[
\boxed{\widehat H(t)/t^5\in
 \mathcal O\langle t/\rho\rangle^\times,\qquad
 \widehat H(t)/t^5\equiv1/5
 \pmod{\{\text{正赋值 Gauss 系数}\}}.}
\tag{7}
\]
这里的 Gauss 归一化按 \(|t|=\rho\)。

证明只用 (6)。若 \(n>5\) 且 \(p\nmid n\)，
其归一化系数赋值至少 \((n-5)/(2p)>0\)。
若 \(v_p(n)=1\)，因为 \(p\equiv3\pmod4\) 而 \(n\equiv1\pmod4\)，
最小可能的 \(n\) 是 \(3p\)，所以
\[
-v_p(n)+(n-5)/(2p)\ge(p-5)/(2p)>0.
\]
若 \(v_p(n)=2\)，最小可能的 \(n\) 为 \(p^2\)，下界为
\[
-2+(p^2-5)/(2p)=(p-5)(p+1)/(2p)>0.
\]
当 \(v_p(n)=r\ge3\)，用 \(n\ge p^r\) 给
\(-r+(p^r-5)/(2p)>0\)；该下界随 \(r\) 增加。
这些加权系数还趋于零，因为 \(v_p(n)=O(\log n)\)。
所以常数项 \(1/5\) 严格控制 Gauss 范数，证明 (7)。

## 4. 保留参考后，实际乘积的半径严格变小

R54 及真实参考比较给
\[
f_0(z)=e^{a z^d}G_0(z),\qquad
d=p+1,\quad v_p(a)=-1,\quad
G_0,G_0^{-1}\in\mathcal O\langle z/\rho\rangle,
\tag{8}
\]
其中 \(a=17c\)，\(c\) 是同一首坏 sigma 系数。
设
\[
S=p^{-p/(p^2-1)}<\rho.
\]
指数因子的半径准确为 \(S\)。
在其 \(z^{dp^n}\) 项上，半径 \(S\) 的加权赋值恒为
\(1/(p-1)\)，故它不属于闭 \(S\) 盘的 Tate 代数。
与在更大闭盘可逆的 \(G_0\) 相乘，不改变这两个结论。

超奇异正式群的 \(\log_E\)、\(\exp_E\) 在半径 \(\rho\) 上为互逆等距
解析换元。这是 [R54 §2](../results/R54-inert-analytic-half-factor-and-central-slope.md)
对本曲线的显式进位证明：若 \(p^r\mid4n+1\)，
\([t^{4n+1}]\log_E(t)\) 的赋值至少 \(-\lfloor r/2\rfloor\)，
故其等距阈值 \(p^{-1/(p^2-1)}\) 严格大于 \(\rho\)。
因此 (8) 对 \(t\) 坐标有相同的精确半径与边界性质。
由 (7) 再乘上 \(t^5\) 和一个在 \(\rho\) 上可逆的函数，得到
\[
\boxed{
f_0(\log_Et)\widehat H(t)
\text{ 的收敛半径准确为 }S<1,
\text{ 且不满足闭 }S\text{ 盘 Tate 条件。}}
\tag{9}
\]
这完全针对 (5) 中实际出现的 \(f_0H\)，不是另一个 theta 模型。
裸 \(H\) 的有限对数表达式并没有消去此参考造成的半径损失。

## 5. 有限 unipotent 层不能在这一步直接替代实际函数

一个初等事实足以辨别直接比较的范围。若一个有限 unipotent 连接
在开单位正式盘上有一个三角代数框架，连接系数在该盘解析，
则每个水平解分量也在该盘解析。
确实，按 unipotent 过滤逐级求解，只作有限次乘法和积分；
若 \(f(t)\) 的半径至少为 \(1\)，其原函数也有半径至少为 \(1\)，
因为除以 \(n\) 只带来 \(O(\log n)\) 的赋值损失。

因此，有限个这样的函数及其有限 tensor/extension 所产生的
线性组合仍在整个开单位盘解析。
BKT Proposition 2.16 的 prime-to-\(p\) 挠点 Kronecker 输入正有这一
性质；把有限 polylog 层平移到本题固定挠点，所用正式盘也不遇到这些
prime-to-\(p\) 的奇点。裸 (3) 就是最简单的例子。

但 (9) 严格排除了将实际 \(f_0H\) 直接认作这种有限层水平分量，
前提是比较使用在该正式盘正则的代数框架。
允许一个额外的非整、非 overconvergent theta 平凡化当然可能改变半径；
那一额外比较本身正是需要证明的输入，不能省略。

这不否认 \(f_0\) 是正次数线丛的代数截面。
把它用自身平凡化后写成常数 \(1\) 也是合法的；
但再变回本题所需的 canonical theta 正式平凡化时，
(8) 的指数因子重新出现。不能用抽象线丛的有限维性绕过该转换。

### 5.1 同一结论适用于全盘正则的有限 Frobenius 比较

以下是一个直接解析命题，不需要 unipotent 假设。
设系数域带有保赋值的 Frobenius 自同构 \(\sigma\)，
\(\varphi(t)\in\mathcal O[[t]]\) 满足
\[
\varphi(0)=0,\qquad \varphi(t)\equiv t^q\pmod p,\quad q>1.
\tag{9a}
\]
设有限秩连接在整个开单位盘有正则解析框架，
并有水平 Frobenius 比较矩阵 \(\Phi(t)\)，其中
\(\Phi\) 与 \(\Phi^{-1}\) 都在整个开单位盘解析。
则以 \(Y(0)=I\) 规范的水平基本解在整个开单位盘解析。

证明如下。解析微分方程先在某个正半径小盘上有唯一基本解。
Frobenius 水平性和初值唯一性给出
\[
Y(t)=\Phi(t)\,Y^\sigma(\varphi(t))\,\Phi(0)^{-1}.
\tag{9b}
\]
对任意 \(0<r<1\)，(9a) 的整系数给出准确界
\[
\|\varphi\|_r\le\max(r^q,p^{-1}r).
\tag{9c}
\]
右端严格小于 \(r\)。其迭代趋于 \(0\)；
Frobenius 共轭的 \(\varphi^{\sigma^j}\) 满足相同界。
故只需有限次迭代 (9b)，就能把闭 \(r\) 盘送入初始收敛盘。
右端的有限个矩阵乘积均在闭 \(r\) 盘解析，给出该盘上的基本解。
不同 \(r\) 上的延拓由初值唯一性相容，因此覆盖整个开单位盘。
这里没有对无限矩阵乘积作未经证明的收敛断言。

由 (9)，实际 \(f_0H\) 也不可能直接成为这种有限 Frobenius
连接在上述正则框架中的水平分量。此应用要求 canonical theta
标量确实直接是该分量，且比较矩阵在全盘解析、可逆；
若其中任一项需要一个只在较小盘收敛的框架变换，
本命题不适用，那个额外变换仍须单独分析。

## 6. 有限截断与固定有限层是两回事

另一个直接检查说明 naive 指数截断不可能固定层数：
\[
\ell(z)=\log f_0(z)=\frac{\alpha^4}{12}z^4+O(z^8),\qquad
H(z)=z^5/5+O(z^9).
\]
若以
\[
H(z)\sum_{j=0}^N\frac{\ell(z)^j}{j!}
\]
替代 \(f_0H\)，第一个遗漏项准确为
\[
\frac{(\alpha^4/12)^{N+1}}{5(N+1)!}\,
 z^{\,4N+9}\ne0.
\tag{10}
\]
所以即便只要求完整复制增长中的低阶 jet，所需指数截断也必须随
该 jet 增长。这句话只针对这一明确截断方案；
不是未经证明地给一切几何实现设同一秩下界。

完整 BKT pro-object 可包含任意高层，
但 Theorem 4.19 的有限层公式不能自动赋予 (10) 的无限和一个
统一的整比较。supersingular Fourier 理论中的分布也不能擅自当作
有界普通测度；原文 Definition 2.18–2.19 已区分二者。

当前能保留的正向事实是：实际裸 pure-log 类 (2)–(4) 有固定有限
Kummer 几何，其分布式也已完整证明。
缺少的是一个同时保留正次数 \(f_0\)、全部 shifted jet 及中心权导数的
比较。本文没有获得能跨 \(p\) 强迫 \(J_{A,p}'(0)\ne0\) 的新定理。
