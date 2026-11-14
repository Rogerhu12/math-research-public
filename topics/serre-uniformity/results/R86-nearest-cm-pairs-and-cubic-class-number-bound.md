# R86：最近 CM 点对与三次类数界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，根会话已逐节独立复核。** 本文加强 R83 的统一几何非消失判据为
$$
\boxed{
p\ge\frac{4M}{h(\mathcal O)^{1/3}}
\quad\Longrightarrow\quad P_\eta\ne0.
}
$$
证明利用大纤维中必有更近的点对，因而其左序容许更小判别式的辅助 CM 序；对全部纤维大小积分，得到三次而非四次的类数界。底域、环类导子及素数均可变化。结合 Siegel 下界的统一指数为 $5/6+\epsilon$，其常数仍无效；显式类数判据没有这种无效性。

它仍不控制变化三次字符的导子上界，不排除 exceptional 分母或完整惯性分支，不是 Serre 一致性的完整解答。

## 1. 设定和结论

沿用 R83 的全部设定：$\mathcal O\subset K$ 为虚二次序，
$$
\operatorname{disc}(\mathcal O)=-M,\qquad
h=h(\mathcal O).
$$
$p>3$，$p\nmid M$，$p$ 在 $K$ 惰性；$R$ 为 $B_{p,\infty}$ 中满足 $R\cap K=\mathcal O$ 的极大序。$\eta$ 为 $\operatorname{Pic}(\mathcal O)$ 上阶恰为 $3$ 的字符，定义
$$
\varphi([\mathfrak a])=[\mathfrak aR],
\qquad
P_\eta=\sum_{[\mathfrak a]}\eta(\mathfrak a)^{-1}[\varphi(\mathfrak a)].
$$
在周期层面不要求 $\eta$ 原始。

**定理 86.1。** 若 $P_\eta=0$，则 $r=M/p>1$，而令 $s=\lfloor r\rfloor$ 后，
$$
\boxed{
h<64rs^2\le64r^3.
}
\tag{86.1}
$$
连同 R83，有更精确的联合必要条件
$$
\boxed{
h<\min\{16rs^3,\ 64rs^2\}.
}
\tag{86.2}
$$
因此
$$
\boxed{
p\ge4M/h^{1/3}
\quad\Longrightarrow\quad P_\eta\ne0.
}
\tag{86.3}
$$
这里没有 $p\equiv2\pmod3$ 的假设，也没有对辅助序导子或辅助判别式与 $p$ 的互素性假设。

**推论 86.2。** 若 $\eta$ 为准确导子 $c$ 的原始三次环类字符，$M=|D_K|c^2$，则 (86.3) 保证存在水平 $p$、权 $2$、平凡 nebentype 的新形式 $g$，使
$$
L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.
\tag{86.4}
$$
这里使用 R76 §6、R83 §6 已核准的 Cai–Shu–Tian 公式及完整 Brandt 尖点谱。所有常数在 $K,c,\eta$ 上统一。

## 2. 大纤维中存在近点对

假定 $P_\eta=0$。R83 §2 给 $r>1$，且每个非空纤维大小 $n$ 至少为 $3$。每个纤维可选出 $n$ 个两两不同、同 $p$ 取向的嵌入点，其纯部 $v_i$ 位于
$$
\operatorname N(v_i)=M/4
$$
的实三维球面上。差 $\omega_i-\omega_j=v_i-v_j$ 属于对应左序 $S$ 的两边素理想 $\mathfrak P$，且
$$\mathfrak P^2=pS.$$

令 $\delta$ 为这个有限点集的最小平方弦长，即
$$
\delta=\min_{i\ne j}\operatorname N(v_i-v_j)>0.
$$
最小球心角为 $2\arcsin\sqrt{\delta/M}$。以每个点为中心、该角一半为角半径的开球面帽两两不交，故
$$
n\left(1-\sqrt{1-\delta/M}\right)\le2.
$$
因 $n\ge3$，右侧变形中的 $1-2/n$ 非负，可以平方而不改变含义：
$$
\sqrt{1-\delta/M}\ge1-\frac2n
\quad\Longrightarrow\quad
\boxed{
\delta\le\frac{4M(n-1)}{n^2}<\frac{4M}{n}.
}
\tag{86.5}
$$
帽边界相切不影响面积论证；最后的严格不等号只用了 $n-1<n$。

取实现最近距离的两点 $\omega_0,\omega_1$，再任取该纤维中第三个点 $\omega_2$。置
$$
a=\omega_1-\omega_0,\qquad b=\omega_2-\omega_0,
$$
并写
$$
\operatorname N(a)=kp,\qquad
\operatorname N(b)=lp,\qquad
\operatorname N(a-b)=mp.
$$
这些范数是正的 $p$ 倍数，且两球面点的平方距离至多 $M$，故
$$
1\le k,l,m\le s,\qquad
k\le\frac{4r(n-1)}{n^2}<\frac{4r}{n}.
\tag{86.6}
$$
三个不同球面点不共线，因此 $a,b$ 线性独立。R83 §2 的整性计算给
$$
\beta=-ab/p\in S,\qquad
d=-\operatorname{disc}\mathbb Z[\beta]
=4kl-(k+l-m)^2>0.
$$
于是
$$
d\le4kl\le4ks
\;<\frac{16rs}{n}.
\tag{86.7}
$$
同时仍有 R83 的 $d\le3s^2$。取最优 overorder
$$
\mathcal A=S\cap\mathbb Q(\beta),
$$
其绝对判别式 $d_{\mathcal A}$ 不大于 $d$，所以
$$
\boxed{
d_{\mathcal A}\le3s^2,\qquad
d_{\mathcal A}<\frac{16rs}{n}.
}
\tag{86.8}
$$
最近点对可以随纤维选择；本证明不要求不同纤维选择相同的辅助序或同一个分数域。

## 3. 纤维分布的两个上界

对实数 $t\ge0$ 定义
$$
A(t)=\#\{x\in\operatorname{im}\varphi:\ |\varphi^{-1}(x)|>t\}.
$$
这是一个取非负整数值的有限阶梯函数。因每个非空纤维至少含三个点，$A(t)=\#\operatorname{im}\varphi$ 对 $0\le t<3$ 成立；下文不把 $t<3$ 的区间省略。

R83 引理 83.3 给每个辅助序至多覆盖 $2h(\mathcal A)$ 个真实 Brandt 右理想类；引理 83.4 对任意实数 $Y>0$ 给
$$
\sum_{0<d\le Y}h(-d)\le\frac{2Y^{3/2}}{3\sqrt3}.
$$
因此对全部 $t\ge0$，先有不依赖 $t$ 的上界
$$
A(t)\le 2\sum_{0<d\le3s^2}h(-d)
\le4s^3.
\tag{86.9}
$$

对任意 $t>0$，被 $A(t)$ 计数的纤维大小 $n>t$；(86.8) 因而给 $d_{\mathcal A}<16rs/t$。每个这样的 Brandt 类都在相应小判别式序的覆盖并集中，所以
$$
\begin{aligned}
A(t)
&\le2\sum_{0<d\le16rs/t}h(-d)\\
&\le\frac4{3\sqrt3}\left(\frac{16rs}{t}\right)^{3/2}\\
&=\frac{256}{3\sqrt3}(rs)^{3/2}t^{-3/2}.
\end{aligned}
\tag{86.10}
$$
此证明对 $0<t<3$ 也有效：对应的每个实际纤维仍有 $n\ge3>t$。不过这段区间直接使用 (86.9) 更简便。

合并得
$$
\boxed{
A(t)\le
\min\left\{
4s^3,\,
\frac{256}{3\sqrt3}(rs)^{3/2}t^{-3/2}
\right\}\quad(t>0).
}
\tag{86.11}
$$
两个比较函数的交点为
$$
t_0=\left(
\frac{256(rs)^{3/2}}{12\sqrt3\,s^3}
\right)^{2/3}
=\frac{16r}{3s}.
\tag{86.12}
$$
特别 $t_0\ge16/3>3$，故第一个积分区间完整包含所有小于三的 $t$。

## 4. 积分及严格常数

对每个大小为 $n_x$ 的纤维有
$$n_x=\int_0^\infty\mathbf 1_{\{n_x>t\}}\,dt.$$
因为只有有限多个纤维，可直接求和，得到
$$
h=\int_0^\infty A(t)\,dt.
\tag{86.13}
$$
由 (86.11)–(86.12)，
$$
\begin{aligned}
h
&\le4s^3t_0+
\frac{256}{3\sqrt3}(rs)^{3/2}
\int_{t_0}^{\infty}t^{-3/2}\,dt\\
&=4s^3\frac{16r}{3s}
 +\frac{512}{3\sqrt3}(rs)^{3/2}
  \left(\frac{16r}{3s}\right)^{-1/2}\\
&=\frac{64}{3}rs^2+\frac{128}{3}rs^2\\
&=64rs^2.
\end{aligned}
\tag{86.14}
$$
此处实际为严格不等式：R83 §5 已证每个纤维大小小于 $4r$，所以 $A(t)=0$ 对 $t\ge4r$ 成立；而 (86.11) 右侧的比较函数在全部有限 $t>0$ 仍严格为正。因此积分在一个正测度区间上严格减小，
$$h<64rs^2.$$
这证明 (86.1)。与 R83 的 $h<16rs^3$ 联用得到 (86.2)。

若 $p\ge4M/h^{1/3}$，则 $r\le h^{1/3}/4$，从而 $64r^3\le h$，与 (86.1) 矛盾。这证明 (86.3)。原始字符时再用 R83 §6，得到推论 86.2。

## 5. 统一渐近及实际分支

R83 §7 已完整写出
$$
h(\mathcal O_c)\ge C_\delta M^{1/2-\delta}
\qquad(\delta>0),
$$
其中 $C_\delta>0$ 对 $K,c$ 统一，但使用 Siegel 下界因而一般无效。取 $\delta=3\epsilon$，代入 (86.3) 得：

**推论 86.3。** 对每个 $\epsilon>0$，存在对 $K,c,\eta$ 统一的常数 $C'_\epsilon>0$，使
$$
\boxed{
p\ge C'_\epsilon M^{5/6+\epsilon}
\quad\Longrightarrow\quad
\exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0
}
\tag{86.15}
$$
对准确导子 $c$ 的原始三次环类字符成立。这里的常数一般无效；未用 GRH。

显式 (86.2)–(86.3) 中的类数可以按约化二元型精确计算，常数 $4$ 完全有效。R86 与 R83 的简洁阈值分别为 $4M/h^{1/3}$ 和 $2M/h^{1/4}$；当 $h>2^{12}=4096$ 时，前者严格更小。带 $\lfloor M/p\rfloor$ 的联合条件通常更精确。

在 R66 的实际小惯性分支，三次角色原始。若存在一个非 exceptional 的实际同余曲线分母素数，则 R69/R72 迫使全部相关中心值消失，故必须满足
$$
\boxed{
h(\mathcal O_{c_\eta})
<\min\left\{
16\frac Mp\left\lfloor\frac Mp\right\rfloor^3,\,
64\frac Mp\left\lfloor\frac Mp\right\rfloor^2
\right\}.
}
\tag{86.16}
$$
特别 $p<4M/h^{1/3}$。和 R81 合用还须 $M>3p$。这给更强的必要导子增长，仍没有相反的导子上界或所有 exceptional 的排除。

## 6. 来源和独立部分

- [R83：小辅助 CM 序、球面装填与统一三次周期界](R83-small-auxiliary-cm-orders-and-uniform-period-bound.md)：使用其同取向模型、辅助序覆盖数、所有小判别式序类数总和及单纤维上界；这里重新证明最近点估计及完整分布积分。
- [R76：三点纤维及三次非消失](R76-three-point-fibres-and-cubic-nonvanishing.md)：最优嵌入的理想证明、$\mathfrak P^2=pS$ 整性以及已发表中心值公式接口。
- L. Cai, J. Shu, Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*, **Algebra & Number Theory 8** (2014), 2523–2572，Theorem 1.2。[原文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)。

§§2–4 为本篇完整的几何及计数证明，不引入未发表的三点非消失命题或任何有限抽样假设。
