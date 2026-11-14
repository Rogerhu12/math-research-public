# 任意 L² 测试端的一阶零矩空间有限维

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：已证明；供 R104 登记。

本稿允许固定测试端 $g$ 是任意非零 $L^2$ 向量，证明所有与它实际全矩消失的次数至多一向量形成有限维空间。证明还给出该维数的局部上半连续性，以及存在这类一阶消失向量的测试端集合是闭的无内点锥。这些都是结构限制；没有证明每个这样的有限维空间都为零。

## 1. 主结论

令
$$
H_{\le1}
=\left\{a_*+\sum_{j\ge0}a_j\chi_j:
|a_*|^2+\sum_j|a_j|^2<\infty\right\}.
$$
沿用实际算子 $A$ 和双线性型
$$
B(u,v)=\int u(y)v(-1-y)\,d\mu(y).
$$
对任意 $g\in H$，定义闭线性子空间
$$
\mathcal Z_g
=\{f\in H_{\le1}:B(A^nf,g)=0\text{ 对全部 }n\ge0\}.
\tag{1.1}
$$

**定理 1.1。** 对每个 $0\ne g\in H$：

1. 存在有限 $m$，使投影到
   $$
   F_m=\operatorname{span}\{1,\chi_0,\ldots,\chi_{m-1}\}
   $$
   在 $\mathcal Z_g$ 上单射，并有有界逆。因此
   $$
   \boxed{\dim\mathcal Z_g\le m+1<\infty.}
   \tag{1.2}
   $$
2. 在 $H\setminus\{0\}$ 上，函数 $g\mapsto\dim\mathcal Z_g$ 上半连续。特别地，维数在每个非零测试端附近有统一有限上界。
3. 集合
   $$
   \mathcal B_1
   =\{g\in H:\mathcal Z_g\ne\{0\}\}
   \tag{1.3}
   $$
   是一个包含 $0$ 的闭复锥，并且没有内点。等价地，$\mathcal Z_g=\{0\}$ 的测试端构成 $H$ 中的稠密开集。

这里第 3 点不声称 $\mathcal B_1=\{0\}$。一个闭的无内点锥仍可能含有非零向量。

核心是下述真实尾测试的统一近标量结论。记
$$
N_j=\frac{A^{2^j}}{W_{2^j}},\qquad
T_j=2N_j-I,\qquad
S_j=2E_j-I,\qquad W_n=\|A^n\|.
$$
由常向量循环性，可为固定 $g\ne0$ 选取整数 $n_0\ge0$，使
$$
\beta=B(A^{n_0}1,g)\ne0.
\tag{1.4}
$$
令
$$
X_m=\overline{\operatorname{span}}\{\chi_j:j\ge m\},
\qquad
U_m:X_m\longrightarrow\ell^2([m,\infty))
$$
为 Walsh 系数等距映射。定义
$$
\Phi_{g,m}f
=\bigl(B(A^{n_0}T_jf,g)\bigr)_{j\ge m}.
\tag{1.5}
$$
它在全部 $H_{\le1}$ 上有界，而且
$$
\boxed{
\|\Phi_{g,m}|_{X_m}-\beta U_m\|\longrightarrow0
\quad(m\to\infty).
}
\tag{1.6}
$$
所以对充分大的 $m$，
$$
\boxed{
\|\Phi_{g,m}f\|_{\ell^2}
\ge\frac{|\beta|}{2}\|f\|_2
\qquad(f\in X_m).
}
\tag{1.7}
$$
本稿给出 (1.6) 的完整误差式；$g$ 无需具有有限次数或任何特定尾衰减速率。

## 2. 一阶合成与任意 L² 端点的对偶

R84 的一次合成情形给出与 $m$ 无关的常数 $C,D>0$，使对任意有限系数列 $(c_j)_{j\ge m}$ 及 $f\in H_{\le1}$，
$$
\left\|\sum_{j\ge m}c_jS_jf\right\|_2
\le C\|c\|_{\ell^2}\|f\|_2,
\tag{2.1}
$$
$$
\left\|\sum_{j\ge m}c_j(T_j-S_j)f\right\|_2
\le D\eta_m\|c\|_{\ell^2}\|f\|_2.
\tag{2.2}
$$
可以直接取 R84 的 $C=C_{1,1}=7$。对第二式还可独立验证：
$$
\begin{aligned}
\left\|\sum_{j\ge m}c_j(T_j-S_j)f\right\|_2
&\le2\sum_{j\ge m}|c_j|\eta_j\|f\|_2\\
&\le2\left(\sum_{j\ge m}\eta_j^2\right)^{1/2}
\|c\|_{\ell^2}\|f\|_2
\le D\eta_m\|c\|_{\ell^2}\|f\|_2.
\end{aligned}
\tag{2.3}
$$
实际权满足统一几何比 $\eta_{j+1}\le\theta\eta_j$，$\theta<1$，故例如
$D=2(1-\theta^2)^{-1/2}$ 可用。
这一项甚至不要求 $f$ 有限次数；有限次数只用于纯模型合成 (2.1)。

对任意 $g\in H$，用保范数双线性对偶，
$$
\left|
\sum_{j\ge m}c_j B(A^{n_0}T_jf,g)
\right|
\le
W_{n_0}(C+D\eta_m)
\|c\|_{\ell^2}\|f\|_2\|g\|_2.
$$
对全部有限系数 $c$ 取上确界，得到
$$
\boxed{
\|\Phi_{g,m}\|_{H_{\le1}\to\ell^2}
\le W_{n_0}(C+D\eta_m)\|g\|_2.
}
\tag{2.4}
$$
因而 (1.5) 的整个无限数组确实属于 $\ell^2$。
这里是通过 $f$ 端的合成估计作对偶；没有给任意 $g$ 施加有限 chaos 合成假设。

同样，对固定 $n_0,m$，
$$
\|\Phi_{g,m}-\Phi_{\widetilde g,m}\|
\le W_{n_0}(C+D\eta_m)\|g-\widetilde g\|_2.
\tag{2.5}
$$
这将在维数稳定性中使用。

## 3. 有限头模型给出精确的标量对角

令 $A_m$ 是低 $m$ 位的有限链，$\mathbb E_m$ 是对低 $m$ 位作条件期望的正交投影。记
$$
g_m=\mathbb E_m g,\qquad
\beta_m=B(A_m^{n_0}1,g_m).
\tag{3.1}
$$
有
$$
\|g-g_m\|_2\longrightarrow0,\qquad
\|A^{n_0}-A_m^{n_0}\|
\le n_0\alpha_m^{\rm op}.
\tag{3.2}
$$
$\alpha_m^{\rm op}$ 是实际径向权，趋于零。
$\mathbb E_m$ 与逐位反射相容，且 $A_m^{n_0}1$ 只依赖低 $m$ 位，因此
$$
\beta_m=B(A_m^{n_0}1,g).
$$
所以
$$
|\beta_m-\beta|
\le n_0\alpha_m^{\rm op}\|g\|_2.
\tag{3.3}
$$

取 $f=\sum_{i\ge m}a_i\chi_i\in X_m$。对 $j\ge m$，
$S_j$ 不作用于低 $m$ 位，而 $A_m^{n_0}$ 只作用于低 $m$ 位，故张量分离给
$$
B(A_m^{n_0}S_jf,g_m)
=\beta_m\int S_jf\,d\mu_{\rm tail}.
\tag{3.4}
$$
逐位计算为
$$
S_j\chi_j=1-2\chi_j,\qquad
S_j\chi_i=-\chi_j\chi_i\quad(i\ne j).
\tag{3.5}
$$
因此
$$
\int S_jf\,d\mu_{\rm tail}=a_j,
$$
并得到精确等式
$$
\boxed{
\bigl(B(A_m^{n_0}S_jf,g_m)\bigr)_{j\ge m}
=\beta_m U_mf.
}
\tag{3.6}
$$
无限 $\ell^2$ 系数情形由有限部分和及有界性取极限。
这里的张量分离仅用于纯模型 $S_j$、$A_m$ 和有限头 $g_m$；没有把实际 $N_j$ 的进位作用假装为独立位作用。

## 4. 所有真实进位和头截断误差的统一界

对任意有限尾测试系数 $c$，精确分解
$$
\begin{aligned}
&\sum_{j\ge m}c_j
\left[
B(A^{n_0}T_jf,g)-B(A_m^{n_0}S_jf,g_m)
\right]\\
&=
B\left(A^{n_0}\sum_{j\ge m}c_j(T_j-S_j)f,g\right)\\
&\quad+
B\left((A^{n_0}-A_m^{n_0})
\sum_{j\ge m}c_jS_jf,g\right)\\
&\quad+
B\left(A_m^{n_0}\sum_{j\ge m}c_jS_jf,g-g_m\right).
\end{aligned}
\tag{4.1}
$$
全部高位合成都先作用于原来的 $f\in H_{\le1}$，实际幂在其后作用。
所以 (2.1)—(2.2) 给
$$
\begin{aligned}
&\left\|
\Phi_{g,m}f-
\bigl(B(A_m^{n_0}S_jf,g_m)\bigr)_{j\ge m}
\right\|_{\ell^2}\\
&\le
\left[
W_{n_0}D\eta_m\|g\|_2
+C n_0\alpha_m^{\rm op}\|g\|_2
+C\|A_m^{n_0}\|\,\|g-g_m\|_2
\right]\|f\|_2.
\end{aligned}
\tag{4.2}
$$
这个估计对整个 $H_{\le1}$ 有效；接下来只在 $X_m$ 上使用精确模型式 (3.6)。

再加上 (3.3)，得到显式近标量界
$$
\boxed{
\|\Phi_{g,m}|_{X_m}-\beta U_m\|
\le e_m(g),
}
\tag{4.3}
$$
其中
$$
\boxed{
e_m(g)=
W_{n_0}D\eta_m\|g\|_2
+(C+1)n_0\alpha_m^{\rm op}\|g\|_2
+C\|A_m^{n_0}\|\,\|g-\mathbb E_mg\|_2.
}
\tag{4.4}
$$
每项都趋于零：$n_0$ 固定，实际 $\eta_m,\alpha_m^{\rm op}\to0$，
$\|A_m^{n_0}\|\le1$，而条件期望在 $H$ 中强收敛到恒等。
因此证明 (1.6)，并在 $e_m(g)\le|\beta|/2$ 时得到 (1.7)。

若 $n_0=0$，所有含 $n_0\alpha_m^{\rm op}$ 的项为零；论证同样成立。
一般可把 $m$ 继续取大，使 $2^m>n_0$，不影响以上结论。

## 5. 全矩消失空间的有限维图结构

固定一个满足 (1.7) 的 $m$，令
$$
c_g=\frac{|\beta|}{2},\qquad
M_g=W_{n_0}(C+D\eta_m)\|g\|_2.
$$
正交分解
$$
H_{\le1}=F_m\oplus X_m,\qquad
f=f_{\rm head}+f_{\rm tail}.
$$
若 $f\in\mathcal Z_g$，则对每个 $j\ge m$，
$$
B(A^{n_0}T_jf,g)
=\frac{2}{W_{2^j}}B(A^{n_0+2^j}f,g)
-B(A^{n_0}f,g)=0.
$$
因此 $\Phi_{g,m}f=0$，并由尾左界得
$$
c_g\|f_{\rm tail}\|_2
\le\|\Phi_{g,m}f_{\rm tail}\|_{\ell^2}
=\|\Phi_{g,m}f_{\rm head}\|_{\ell^2}
\le M_g\|f_{\rm head}\|_2.
\tag{5.1}
$$
于是
$$
\boxed{
\|f\|_2
\le
\left[1+(M_g/c_g)^2\right]^{1/2}
\|f_{\rm head}\|_2
\qquad(f\in\mathcal Z_g).
}
\tag{5.2}
$$
头投影在 $\mathcal Z_g$ 上单射；其值域包含在有限维 $F_m$ 中，
故 $\dim\mathcal Z_g\le m+1$。
更具体地，$\mathcal Z_g$ 是 $F_m$ 某个子空间上的有界线性图
$$
\mathcal Z_g=\{u+R_gu:u\in F_m'\},
\qquad
\|R_g\|\le M_g/c_g.
\tag{5.3}
$$
这证明定理 1.1 的第一部分。

(5.2) 不说明 $F_m'=\{0\}$。它仅说明任何可能的一阶零矩向量均由有限个低位系数唯一决定，而且不存在单位范数的这类向量逃逸到无限高位。

## 6. 测试端变化时的紧性与维数上半连续

固定 $g_0\ne0$，用上文为它选取 $n_0,m$，使
$\Phi_{g_0,m}$ 在 $X_m$ 上有左界 $c>0$。
在本节，$n_0,m$ 保持固定；即使测试端改成 $g$，仍使用同一族 $A^{n_0}T_j$。
由 (2.5)，当 $\|g-g_0\|$ 足够小时，
$$
\|\Phi_{g,m}f\|\ge\frac c2\|f\|
\qquad(f\in X_m).
\tag{6.1}
$$
因此附近所有 $\mathcal Z_g$ 的维数都不超过同一个 $m+1$。

更强地，设 $g_\nu\to g_0$，且
$$
f_\nu\in\mathcal Z_{g_\nu},\qquad \|f_\nu\|\le1.
$$
其头投影在有限维 $F_m$ 中有收敛子列。
又由 (2.5) 和 $\Phi_{g_\nu,m}f_\nu=0$，
$$
\|\Phi_{g_0,m}f_\nu\|\longrightarrow0.
\tag{6.2}
$$
对所取子列的两项作差。头部分已经是 Cauchy 列，而尾部分满足
$$
\begin{aligned}
c\|(f_\nu-f_\mu)_{\rm tail}\|
&\le\|\Phi_{g_0,m}(f_\nu-f_\mu)_{\rm tail}\|\\
&\le
\|\Phi_{g_0,m}f_\nu\|+
\|\Phi_{g_0,m}f_\mu\|+
\|\Phi_{g_0,m}(f_\nu-f_\mu)_{\rm head}\|
\longrightarrow0.
\end{aligned}
\tag{6.3}
$$
所以该子列在整个 $H_{\le1}$ 中强收敛到某个 $f$。
逐个实际矩连续取极限给
$$
B(A^nf,g_0)=0\quad(n\ge0),
$$
即 $f\in\mathcal Z_{g_0}$。

现在若沿一个序列 $g_\nu\to g_0$ 都有
$\dim\mathcal Z_{g_\nu}\ge k$，在每个空间中取 $k$ 个正交单位向量。
对有限个向量反复抽子列，(6.2)—(6.3) 使它们强收敛到
$\mathcal Z_{g_0}$ 中的 $k$ 个正交单位向量。
因此
$$
\boxed{
\limsup_{\nu\to\infty}\dim\mathcal Z_{g_\nu}
\le\dim\mathcal Z_{g_0}.
}
\tag{6.4}
$$
这就是非零测试端处的上半连续性。

关键紧性来自统一的尾左界和有限头维数；
不是从原 Hilbert 单位球的弱紧性直接宣称范数不坍缩。

## 7. 一阶消失测试端集合闭且无内点

若 $g_\nu\in\mathcal B_1$ 且 $g_\nu\to g_0\ne0$，取
$f_\nu\in\mathcal Z_{g_\nu}$、$\|f_\nu\|=1$。
§6 给强收敛子列，其极限 $f\in\mathcal Z_{g_0}$ 且仍有范数 $1$。
因此 $g_0\in\mathcal B_1$。
若极限为 $0$，则 $\mathcal Z_0=H_{\le1}$，所以 $0\in\mathcal B_1$。
这证明 $\mathcal B_1$ 在整个 $H$ 中闭。

对任意非零复标量 $\lambda$，$B$ 对第二端线性给
$\mathcal Z_{\lambda g}=\mathcal Z_g$；又 $0\in\mathcal B_1$，
故 $\mathcal B_1$ 是闭复锥。

R11 已证明每个非零有限柱向量对实际 $A$ 循环。
若 $g$ 是这样的向量，且
$B(A^nf,g)=0$ 对全部 $n$，则由 $B$ 对称性，
$$
B(f,A^ng)=0\quad(n\ge0).
$$
$g$ 的轨道线性张成稠密，$B$ 非退化，因此 $f=0$。
所以每个非零有限柱 $g$ 都不在 $\mathcal B_1$ 中。
非零有限柱向量在 $H$ 中稠密，从而闭集 $\mathcal B_1$ 没有内点，
其补集是稠密开集。定理 1.1 全部得证。

R91/R101 还给更大的已知好测试端类，但本段的稠密性只需 R11，
并不依赖一般有限 chaos 分离的后续证明。

## 8. 有限附加矩的观察下界

这里记录一个可复用的直接推论。
固定 $g\ne0$ 且 $\mathcal Z_g=\{0\}$，选取上述 $n_0,m$。
仅由尾左界可知 $\ker\Phi_{g,m}$ 有限维，证明与 §5 相同。
全部普通矩在这个有限维核上的共同核就是 $\mathcal Z_g=\{0\}$，
所以存在有限多个整数 $r_1,\ldots,r_d$，使这些矩已在
$\ker\Phi_{g,m}$ 上分离所有向量。

于是存在 $\kappa_g>0$，使对所有 $f\in H_{\le1}$，
$$
\boxed{
\|\Phi_{g,m}f\|_{\ell^2}^2
+\sum_{\ell=1}^d|B(A^{r_\ell}f,g)|^2
\ge\kappa_g^2\|f\|_2^2.
}
\tag{8.1}
$$
证明可用反证：若有单位向量使左端趋零，有限头先取收敛子列，
尾左界像 (6.3) 一样给出整向量强收敛；
极限仍为单位向量，落在 $\ker\Phi_{g,m}$ 并被所有选出的矩杀掉，
与其选择矛盾。

这里并没有把无限矩族自动换成有限矩族。
仍保留一个完整的平方可和 dyadic 尾测试族；
只用有限附加普通矩处理剩余的有限维核。

## 9. 准确边界及下一层障碍

本稿的一阶尾对角成立，是因为对纯高尾一阶向量
$f=\sum_{j\ge m}a_j\chi_j$，
单个位模型测试与有限头 $g_m$ 配对精确提取 $a_j$。
真实进位、实际幂的头截断及任意 $L^2$ 测试端的头截断，
都由 (4.4) 在整个高尾 $\ell^2$ 单位球上一致控制。

对次数 $p>1$，同样的 $p$ 位测试能恢复纯高尾最高阶系数，
但固定低位乘上较低阶无限尾仍形成无限维空间。
它不再只是有限头系数空间，故不能直接照搬 §5 的有限维图论证。
本稿没有将这一剩余空间误写为有限维。

最后，$\mathcal B_1$ 闭且无内点也不能推出它没有非零元素。
第一 chaos 向量对全 $H$ 的逐向量循环性、任意 $L^2$ 两端的矩分离、
以及整个 Hilbert 不变子空间问题，均没有由本条单独解决。
