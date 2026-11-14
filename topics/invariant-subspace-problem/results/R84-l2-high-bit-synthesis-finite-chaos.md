# R84：有限chaos的平方可和高位合成与全数组误差

日期：2026-11-12（UTC）。经主会话逐段核验。

**状态：合成定理、实际模型误差和全矩数组推论均已证明。** 任意有限 Walsh 次数向量都允许任意固定阶、平方可和系数的多高位合成。把实际归一化幂换成独立位模型时，整个合成的误差为 $O_{p,r}(\eta_m)$，常数独立高位起点 $m$，不要求有限模式、有限秩或归一化行方向紧性。

因此实际零矩不只给每个高位元组一个小误差，而给全部高位元组构成的矩数组一个统一 $\ell^2$ 小范数。最后写出一阶与一般有限阶配对中最高阶 Boolean creation 的定量推论；它控制纯尾最高阶系数，但尚未单独完成一般一阶与二阶的全部配对分离。

依赖：实际 $N_j$ 与 $E_j$ 的 R9/R12 估计；R24 的 $B$；R50 中创建与删除交换子恒等式。所需四阶矩估计与多位合成在本稿自含证明。

## 1. 记号与局部算子

令 $H_{\le p}$ 为 Walsh 次数至多 $p$ 的闭子空间。对

$$
f=\sum_{|S|\le p}\widehat f(S)\chi_S
$$

定义 Walsh 删除算子

$$
D_jf=\sum_{S\ni j}\widehat f(S)\chi_{S\setminus\{j\}}.
\tag{1.1}
$$

$D_j$ 范数至多一，把 $H_{\le p}$ 送入 $H_{\le p-1}$；不同 $D_j$ 交换且 $D_j^2=0$。对有限集 $K$，记 $D_K=\prod_{j\in K}D_j$。

实际高位算子和独立位模型记为

$$
N_j=\frac{A^{2^j}}{W_{2^j}},\qquad E_j=e_{10},
$$

$$
T_j=2N_j-I,\qquad S_j=2E_j-I.
\tag{1.2}
$$

已知

$$
\|N_j-E_j\|=\eta_j,\qquad
\|T_j-S_j\|\le2\eta_j,\qquad
\|T_j\|,\|S_j\|\le3.
\tag{1.3}
$$

在第 $j$ 位 Walsh 基 $(1,\chi_j)$ 中，

$$
S_j=
\begin{pmatrix}0&1\\-1&-2\end{pmatrix}.
$$

若 $M_{\chi_j}$ 表示乘以 $\chi_j$，直接计算给

$$
\boxed{S_j=-M_{\chi_j}+2(I-M_{\chi_j})D_j.}
\tag{1.4}
$$

例如对 $f=f_0+\chi_jf_1$，右端为

$$
f_1-\chi_jf_0-2\chi_jf_1,
$$

与矩阵表示一致。

## 2. 有限 chaos 的四阶矩界

本节只用

$$
\|u\|_4\le3^{d/2}\|u\|_2
\quad(u\in H_{\le d}).
\tag{2.1}
$$

给一个简短自含证明。对复数 $a,b$ 和 $\rho=1/\sqrt3$，

$$
\frac{|a+\rho b|^4+|a-\rho b|^4}{2}
\le |a|^4+6\rho^2|a|^2|b|^2+\rho^4|b|^4
\le(|a|^2+|b|^2)^2.
\tag{2.2}
$$

把第 $j$ 位 Walsh 一次分量乘以 $\rho$ 的噪声算子记为 $\mathcal T_\rho$。对有限个位，用 (2.2) 及 $L^2$ 中的三角不等式逐位归纳，得到

$$
\|\mathcal T_\rho u\|_4\le\|u\|_2.
$$

确切地说，若最后一位分解为 $u_0+\chi u_1$，先对其他位使用归纳，再对最后一位用 (2.2)，便有输出 $L^4$ 范数平方不超过 $\|u_0\|_2^2+\|u_1\|_2^2$。

若 $u$ 次数至多 $d$，将其 $S$ 项系数乘以 $\rho^{-|S|}$ 得到 $v$，则 $u=\mathcal T_\rho v$ 且 $\|v\|_2\le3^{d/2}\|u\|_2$，证明 (2.1)。无限位情形由有限条件期望在 $L^2$ 中逼近，并用同一估计得到 $L^4$ Cauchy 性。

还需删除算子的计数恒等式：

$$
\sum_{|K|=k}\|D_Kh\|_2^2
={r\choose k}\|h\|_2^2
\quad(h\in H_{=r}),
\tag{2.3}
$$

以及

$$
\sum_{|K|=k}\|D_Kf\|_2^2
\le {p\choose k}\|f\|_2^2
\quad(f\in H_{\le p}).
\tag{2.4}
$$

每个 Walsh 系数分别被其支撑中的 $k$ 元子集计数，故两式直接成立。

## 3. 独立位模型的平方可和合成

固定 $p,r\ge0$。对有限支撑的齐次 Walsh 多项式

$$
h=\sum_{|J|=r}c_J\chi_J
$$

定义

$$
\mathscr S_r(h)f
=\sum_{|J|=r}c_J S_Jf,\qquad
S_J=\prod_{j\in J}S_j.
\tag{3.1}
$$

**定理 3.1。** 存在只依赖 $p,r$ 的常数 $C_{p,r}$，使

$$
\|\mathscr S_r(h)f\|_2
\le C_{p,r}\|h\|_2\|f\|_2
\quad(f\in H_{\le p}).
\tag{3.2}
$$

可取

$$
C_{p,r}=
\sum_{k=0}^{\min(p,r)}
4^k3^{(p+r-2k)/2}
\sqrt{{p\choose k}{r\choose k}}.
\tag{3.3}
$$

$r=0$ 时可以改取 $C_{p,0}=1$。这些常数与系数支撑位置和尾起点无关。

**证明。** 对 (1.4) 的乘积按选择删除项的子集 $K\subseteq J$ 展开。不同位的删除算子与乘法交换，因此精确得到

$$
\begin{split}
\mathscr S_r(h)f
={}&(-1)^r hf\\
&+\sum_{k=1}^{\min(p,r)}
(-1)^{r-k}2^k
\sum_{|K|=k}
\left(\prod_{j\in K}(1-\chi_j)\right)
(D_Kh)(D_Kf).
\end{split}
\tag{3.4}
$$

当 $k>p$，$D_Kf=0$。对固定 $k$，点态 Cauchy–Schwarz 和 $|1-\chi_j|\le2$ 给

$$
\begin{split}
&\left\|
\sum_{|K|=k}
\left(\prod_{j\in K}(1-\chi_j)\right)
(D_Kh)(D_Kf)
\right\|_2\\
&\qquad\le
2^k
\left\|\left(\sum_{|K|=k}|D_Kh|^2\right)^{1/2}\right\|_4
\left\|\left(\sum_{|K|=k}|D_Kf|^2\right)^{1/2}\right\|_4.
\end{split}
\tag{3.5}
$$

例如第一因子由 $L^2$ 三角不等式及 (2.1) 满足

$$
\left\|\left(\sum_{|K|=k}|D_Kh|^2\right)^{1/2}\right\|_4^2
\le\sum_{|K|=k}\|D_Kh\|_4^2
\le3^{r-k}\sum_{|K|=k}\|D_Kh\|_2^2.
$$

对另一因子同理，结合 (2.3)–(2.4)，再乘上 (3.4) 中的 $2^k$，得到 (3.3) 的第 $k$ 项。$k=0$ 项由 Hölder 和 (2.1) 控制。证毕。

因为有限 Walsh 多项式在 $H_{=r}$ 中稠密，(3.2) 使 $\mathscr S_r(h)f$ 对任意 $h\in H_{=r}$ 都有唯一 $L^2$ 定义。其输出次数至多 $p+r$。这是固定有限次数输入上的双线性合成界，不宣称 $\mathscr S_r(h)$ 对整个 $L^2$ 都有相同有界性。

## 4. 排序后的实际与模型合成误差

令 $h$ 只使用尾指标 $j\ge m$，并定义有限和

$$
\mathscr T_r(h)f
=\sum_{\substack{|J|=r\\J\subseteq[m,\infty)}}c_JT_Jf,
\qquad T_J=\prod_{j\in J}T_j.
\tag{4.1}
$$

**定理 4.1。** 对 $f\in H_{\le p}$，

$$
\|(\mathscr T_r(h)-\mathscr S_r(h))f\|_2
\le \Delta_{p,r}(m)\|h\|_2\|f\|_2,
\tag{4.2}
$$

其中可以取

$$
\Delta_{p,r}(m)=
2\sum_{\ell=1}^r
3^{\ell-1}C_{p,r-\ell}
\left[
\sum_{j\ge m}{j-m\choose\ell-1}\eta_j^2
\right]^{1/2}.
\tag{4.3}
$$

约定当 $j-m<\ell-1$ 时组合数为零。

**证明。** 把每个 $J$ 写成 $j_1<\cdots<j_r$。不需要混合矩阵互相交换，排序后的 telescoping 恒等式本身给

$$
T_J-S_J
=\sum_{\ell=1}^r
T_{j_1}\cdots T_{j_{\ell-1}}
(T_{j_\ell}-S_{j_\ell})
S_{j_{\ell+1}}\cdots S_{j_r}.
\tag{4.4}
$$

固定错误位的次序 $\ell$ 及它的值 $j=j_\ell$。更早指标构成

$$
K\subseteq[m,j),\qquad |K|=\ell-1,
$$

更晚指标构成

$$
L\subseteq(j,\infty),\qquad |L|=r-\ell.
$$

对固定 $K,j$，先将所有更晚指标的和放在错误因子之后：

$$
T_K(T_j-S_j)
\left(\sum_{|L|=r-\ell}c_{K\cup\{j\}\cup L}S_Lf\right).
\tag{4.5}
$$

括号内是定理 3.1 的合成，输入始终是原来的 $f\in H_{\le p}$。所以其范数至多

$$
C_{p,r-\ell}\|f\|_2
\left(\sum_L|c_{K\cup\{j\}\cup L}|^2\right)^{1/2}.
$$

随后才应用范数至多 $2\eta_j$ 的错误因子和范数至多 $3^{\ell-1}$ 的前段 $T_K$。后者无需保持有限 chaos，因为此时只使用全空间算子范数。

对有限个 $K$ 用 Cauchy–Schwarz，数量为 $\binom{j-m}{\ell-1}$，得到该 $j,\ell$ 部分的上界

$$
2\,3^{\ell-1}\eta_j C_{p,r-\ell}\|f\|_2
\sqrt{{j-m\choose\ell-1}}\ b_{j,\ell},
\tag{4.6}
$$

其中

$$
b_{j,\ell}^2
=\sum_{\substack{|K|=\ell-1\\K\subseteq[m,j)}}
\sum_{\substack{|L|=r-\ell\\L\subseteq(j,\infty)}}
|c_{K\cup\{j\}\cup L}|^2.
$$

每个 $r$ 元集恰好有一个第 $\ell$ 小元素，所以

$$
\sum_{j\ge m}b_{j,\ell}^2=\sum_J|c_J|^2=\|h\|_2^2.
\tag{4.7}
$$

再对 $j$ 用 Cauchy–Schwarz，最后对有限个 $\ell$ 相加，得到 (4.2)–(4.3)。证毕。

这个次序处理避免了错误做法：不能先把某个小范数错误因子作用于 $f$，再假定其输出仍有有限 Walsh 次数而应用定理 3.1。式 (4.5) 明确把无限的后段模型合成放在错误因子之前。

## 5. 本模型中常数独立尾起点

实际权满足

$$
\alpha_j=e^{-L_j},\qquad
\eta_j=e^{-(L_{j+1}-L_j)},
$$

$$
L_{j+1}-L_j=
1400\,16^j-630\,8^j+300\,2^j.
$$

直接相减得

$$
(L_{j+2}-L_{j+1})-2(L_{j+1}-L_j)
=19600\,16^j-3780\,8^j>0.
$$

所以 $\eta_{j+1}\le\eta_j^2\le\theta\eta_j$，其中固定

$$
\theta=\eta_0=e^{-1070}<1.
$$

于是对所有 $m,k\ge0$，

$$
\eta_{m+k}\le\eta_m\theta^k,
$$

并由组合数生成函数，

$$
\sum_{j\ge m}{j-m\choose\ell-1}\eta_j^2
\le
\eta_m^2
\frac{\theta^{2(\ell-1)}}{(1-\theta^2)^\ell}.
\tag{5.1}
$$

因此

$$
\boxed{
\Delta_{p,r}(m)\le D_{p,r}\eta_m,}
\tag{5.2}
$$

其中

$$
D_{p,r}=
2\sum_{\ell=1}^r
3^{\ell-1}C_{p,r-\ell}
\frac{\theta^{\ell-1}}{(1-\theta^2)^{\ell/2}}
\tag{5.3}
$$

只依赖 $p,r$ 及固定模型。

结合定理 3.1，$\mathscr T_r(h)f$ 也对任意平方可和尾系数 $h$ 在 $L^2$ 中有唯一极限，且

$$
\|\mathscr T_r(h)f\|_2
\le(C_{p,r}+D_{p,r}\eta_m)\|h\|_2\|f\|_2.
\tag{5.4}
$$

没有把这个极限擅自宣称为整个 $H$ 上的有界交换算子；它是有限次数输入上的一致合成。

## 6. 实际零矩强制整个高位矩数组很小

设

$$
f\in H_{\le p},\qquad g\in H,
$$

且

$$
B(A^nf,g)=0\qquad(n\ge0).
\tag{6.1}
$$

每个有限 $T_J$ 都是 $A$ 的多项式，所以

$$
B(A^n\mathscr T_r(h)f,g)=0
$$

对有限支撑 $h$ 成立，再由 (5.4) 对全部 $h\in H_{=r}$ 成立。

**推论 6.1。** 对固定 $n,r$，有

$$
\left(
\sum_{\substack{|J|=r\\J\subseteq[m,\infty)}}
|B(A^nS_Jf,g)|^2
\right)^{1/2}
\le
\|A^n\|D_{p,r}\eta_m\|f\|_2\|g\|_2.
\tag{6.2}
$$

**证明。** 对任意有限系数 $c_J$，左侧数组与这些系数的双线性配对等于

$$
B(A^n\mathscr S_r(h)f,g)
=B\bigl(A^n(\mathscr S_r(h)-\mathscr T_r(h))f,g\bigr),
$$

用 (5.2) 控制后，取 $\ell^2$ 对偶即得。证毕。

如果需要精确逐位删除公式，令 $A_m$ 为低 $m$ 位有限链。它与全部 $S_j$、$j\ge m$ 交换。由

$$
\|A^n-A_m^n\|\le n\alpha_m
$$

及定理 3.1，得到

$$
\begin{split}
&\left(
\sum_{\substack{|J|=r\\J\subseteq[m,\infty)}}
|B(S_JA_m^nf,g)|^2
\right)^{1/2}\\
&\qquad\le
\left(\|A^n\|D_{p,r}\eta_m+nC_{p,r}\alpha_m\right)
\|f\|_2\|g\|_2.
\end{split}
\tag{6.3}
$$

这里把 $A^n$ 放在合成之后再替换成 $A_m^n$，所以从未需要假定 $A^nf$ 具有有限 Walsh 次数，也没有引入依赖 $m$ 的 chaos 次数常数。

在 $n=0$ 时，整组独立位矩数组的范数就是 $O_{p,r}(\eta_m)$。对固定 $n>0$，精确低位链数组的范数是 $O_{p,r,n}(\alpha_m)$。

## 7. 一般有限 chaos 的精确删除恒等式

若 $T$ 不作用于第 $j$ 位，逐位积分给

$$
\boxed{
B(S_jTf,g)
=B(TD_jf,g)+B(Tf,D_jg)
+2B(TD_jf,D_jg).}
\tag{7.1}
$$

对有限位集 $J$，这些删除算子交换，所以

$$
B(S_JTf,g)
=\mathcal M_T\left[
\prod_{j\in J}
\bigl(D_j^{(1)}+D_j^{(2)}+2D_j^{(1)}D_j^{(2)}\bigr)
(f\otimes g)
\right].
\tag{7.2}
$$

这不需要形式有限模式。对有限 chaos，可由有限 Walsh 多项式逼近及连续性取极限。

因此 (6.3) 对整组真实删除残差给统一 $\ell^2$ 控制，未把每个移动导数向量都错误地置于某个固定有限维空间。

## 8. 最高阶无交叠卷积与创建算子推论

再设 $g\in H_{\le q}$，取 $r=p+q$。式 (7.2) 中每个位至少删除一阶；只有全部取一次删除、且分别在两端删除恰好 $p,q$ 阶的项存活。故对 $|J|=p+q$，

$$
B(S_Jf,g)
=
\sum_{\substack{S\subseteq J\\|S|=p}}
\widehat f(S)\widehat g(J\setminus S).
\tag{8.1}
$$

于是最高阶无交叠卷积 $f_{=p}\star g_{=q}$ 的纯尾部分满足

$$
\left[
\sum_{\substack{|J|=p+q\\J\subseteq[m,\infty)}}
\left|
\sum_{\substack{S\subseteq J\\|S|=p}}
\widehat f(S)\widehat g(J\setminus S)
\right|^2
\right]^{1/2}
\le D_{p,p+q}\eta_m\|f\|_2\|g\|_2.
\tag{8.2}
$$

特别地，若

$$
f=a_*+\sum_j a_j\chi_j,
$$

令

$$
\sigma_m^2=\sum_{j\ge m}|a_j|^2,\qquad
\mu_m=\sup_{j\ge m}|a_j|,
$$

并记 $g_{q,m}$ 为 $g$ 的全部指标都在 $[m,\infty)$ 中的纯 $q$ 阶部分。则 (8.1) 是 Boolean 创建算子 $C_{a_{\ge m}}g_{q,m}$ 的系数。

创建与删除交换子在纯 $q$ 阶上给

$$
\|C_{a_{\ge m}}u\|_2^2
\ge
\left(\sigma_m^2-2q\mu_m^2\right)\|u\|_2^2.
\tag{8.3}
$$

这是 R50 的同一个恒等式：$[C_a^*,C_a]=\sigma_m^2I-2\sum_{j\ge m}|a_j|^2P_j$，而纯 $q$ 阶上 $\sum P_j=qI$。

只要 $\sigma_m^2>2q\mu_m^2$，就有

$$
\boxed{
\|g_{q,m}\|_2
\le
\frac{D_{1,q+1}\eta_m}
{\sqrt{\sigma_m^2-2q\mu_m^2}}
\|f\|_2\|g\|_2.}
\tag{8.4}
$$

例如 $a_j=(j+1)^{-1}$ 时，分母对充分大 $m$ 至少为 $c_qm^{-1/2}$，故

$$
\|g_{q,m}\|_2
\le C_q\sqrt m\,\eta_m\|f\|_2\|g\|_2.
\tag{8.5}
$$

这对任意无限秩的 $g\in H_{\le q}$ 成立，而不是只对有限模式成立。

## 9. 当前结论与剩余缺口

(6.2)–(6.3) 是从实际全部零矩推出的全数组控制；(8.4) 又在一端第一 chaos 的尾足够分散时，把最高阶纯尾压到实际进位误差的尺度。

这尚不能直接推出 $g=0$。例如对二阶 $g$，(8.4) 控制的是两指标都高于 $m$ 的部分；固定低位行与任意高位之间的系数仍可能有慢尾。它们每一行虽是一阶向量，却可能有无穷多行，不能自动由 R78 的有限模式结论取极限。

同样，创建算子的下界需要 $\sigma_m^2>2q\mu_m^2$；一般平方可和系数列的尾可能在少数位上集中，不能无条件删去这一假设。后续需要结合较低阶删除残差，或给固定低位行的恢复建立能与 (8.4) 配合的统一估计。
