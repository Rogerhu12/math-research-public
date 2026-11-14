# R597 增补：同预算联合普通前缀的定量整规范

日期：2026-11-14。**状态：已证明。**
这是一条 R412 实际单位三角块对 R597 结点基准的定量推论；
不另登记 R412 的满射结论，也不把规范变深认成余类非零。

仍保 R597 全部对象，尤其同一个 $r=1,\nu=2$ 的
$\bar P\in\ker\bar J$、$D\ge3$、$p=6s-1>101$、
原全部角点、次数帽、$P_{134}/U_0$ 和两条十三行。
以下 $g$ 是同一原正规化普通轴，$\mathcal E=Y\partial_Y$。
只读取已付整数前缀，不将无限 raw theta 约化。

## 1. 准确可付的前缀长度

为免与临界值 $B$ 或角指数 $B_n$ 混淆，记
$$
b_n^{\rm top}=A_n+e_{n+1}
=\lfloor9n/2\rfloor+4
-2\lfloor(n+1)/4\rfloor-\lfloor(n+1)/3\rfloor+\lfloor n/2\rfloor .
$$
它是原 $n$ 权列允许的最大 $t$ 首阶。
取
$$
\boxed{m=\min\{s,\ b_{D-1}^{\rm top}+1\}.}
\tag{1}
$$
$D\ge3$ 时 $b_2^{\rm top}=13$，所以 $m\ge14$。
对临界 $D\asymp\sqrt p$，
$m=(25/6)D+O(1)$，只在未被 $s$ 截住时使用这个渐近式。

在同一个原有限自由格上考虑普通线性映射
$$
\mathcal L_{m,2}(Q)=
\left(\pi_m Q(t(w),g(w)),\
\pi_m(\mathcal EQ)(t(w),g(w)),\
\pi_2(\mathcal E^2Q)(t(w),g(w))\right).
\tag{2}
$$
它与完整 $J$ 不相同：这里暂不加入任何 $p\mathscr S$ carry。
所读系数因 $m\le s$ 均在原已付整窗口中。

## 2. 同一原列给整单位右逆

对 $j=0,1$ 使用 $n=0,1,2$ 的三列
$$
t^{j-A_n}Y^nq_n=t^jY^nq_n .
$$
其自由多项式次数 $j\le1$ 在原帽内。
它们在同阶三行的首项矩阵为
$\operatorname{diag}(\text{整单位})$ 乘
$(1,n,n^2)^t$，行列式为单位。

对 $2\le j<m$，取满足 $b_n^{\rm top}\ge j$ 的最小 $n$，
使用两个原列
$$
t^{j-A_n}Y^nq_n,\qquad
t^{j-A_{n+1}}Y^{n+1}q_{n+1}.
\tag{3}
$$
这些列确实存在。
由显示 floor 式，$b_n^{\rm top}$ 严格递增，
且 $A_{n+1}\le b_{n-1}^{\rm top}+1$（$n\ge1$）。
后一不等式也可用
$b_i^{\rm top}\ge4i$ 及单独的 $n=1$ 值直接核定。
若最小 $n=0$ 则 $A_0=A_1=0$；
否则 $j>b_{n-1}^{\rm top}$，故 $A_n,A_{n+1}\le j$。
同时 $j\le b_n^{\rm top}\le b_{n+1}^{\rm top}$。
所以 (3) 的两个自由次数都非负且不超过相应原 $e_{n+1}$。
(1) 还给 $n+1\le D$。

两列沿 $g(0)=1$ 的首阶恰为 $j$，
首系数只含 $(-1)^j,7^{A_n},(-1)^{B_n}$，均为单位。
在同阶前两行的矩阵为单位对角乘
$$
\begin{pmatrix}1&1\\ n&n+1\end{pmatrix},
$$
行列式为一。
按 $w$ 阶排列全部所选列，(2) 的对应方阵是单位块三角。
因而存在只用 (3) 及上述六个低列的实际整右逆
$$
\boxed{\iota_{m,2}:\operatorname{target}(\mathcal L_{m,2})
\longrightarrow\mathcal W_D.}
\tag{4}
$$
这逐条保留原角因子、全部次数帽和原源标签。
不是把任意局部函数当作允许来源。
它只是 R412 同一三角机制在这个指定普通前缀上的应用。

## 3. 同一个约化候选的联合整规范

取 R597 任一实际整基准 $P^{\rm base}$。
原相对首核及 $\nu=2$ 给
$$
\mathcal L_{m,2}(P^{\rm base})\in p\operatorname{target}.
$$
令
$$
\boxed{
P^*=P^{\rm base}-
\iota_{m,2}\bigl(\mathcal L_{m,2}(P^{\rm base})\bigr).}
\tag{5}
$$
于是
$$
P^*\in\mathcal W_D,\qquad P^*\equiv\bar P\pmod p,
$$
$$
P^*(t,g),\ (\mathcal EP^*)(t,g)\in w^m\mathcal O[[w]],
\qquad
(\mathcal E^2P^*)(t,g)\in w^2\mathcal O[[w]] .
\tag{6}
$$
(5) 的修正是 $p$ 倍同一实际来源。

在 $t=0$，原来源只剩 $n=0,1,2$ 三权。
(6) 的三个常数行与 $1,n,n^2$ Vandermonde 迫
$P^*(0,Y)=0$ 整系数成立。
所以 $P^*$ 仍有全局 $t$ 因子，而非仅沿 $g$ 消失。
置 $H^*=d^{C_D}\mathcal EP^*/t$。
由 (6)，
$$
H^*(t,g)\in t^{m-1},\qquad
H^*_Y(t,g)=t\cdot\text{整单位}.
\tag{7}
$$
后一式的首单位来自同一个原 $\nu=2$；
第三前缀的精确消零保证没有较低的 $p$ 倍项。

因 $m\ge14$，(7) 先给 $H^*(0,1)=H^*_Y(0,1)=H^*_t(0,1)=0$。
其约化仍是原结点，故沿 R597 指定的非垂直支作同一整 Hensel 提升：
$$
\boxed{\mathcal EP^*|_{\psi^*}=0,\qquad
\psi^*-g\in w^{m-2}\mathcal O[[w]].}
\tag{8}
$$
这里可用原 $g$ 的有限整前缀作任意整形式延拓；
强 Hensel 的所读接触及 (8) 不依赖此延拓的高系数。

沿此支仍有
$$
B^*=\mathcal E^2P^*|_{\psi^*}=w^2\cdot\text{单位},
\qquad C^*=\mathcal E^3P^*|_{\psi^*}\in w .
$$
临界 Taylor 展开和 (6)、(8) 给
$$
\boxed{A^*=P^*|_{\psi^*}\in w^m\mathcal O[[w]].}
\tag{9}
$$
确实，$B^*\eta^2$ 至少从 $2m-2$ 起，
$C^*\eta^3$ 至少从 $3m-5$ 起，
都严格高于或等于 $m$。

## 4. 与原 eta0、carry 和同一修正的兼容

约化分支仍是原 $\bar\psi$，故仍可选
$$
\eta=\log(g/\psi^*)=\eta_0+p\xi,\qquad
\eta_0\in w^{s-2}\mathcal O[w].
$$
因 $m\le s$，两项的初始零段相容，并得到准确整结论
$$
\boxed{\xi\in w^{m-2}\mathcal O[[w]],\qquad A^*\in w^m.}
\tag{10}
$$
当 $m=s$ 时也只说两者从 $s-2$ 开始；
没有把 $\eta_0$ 或 $\xi$ 的 $s-2,s-1$ 项抹去，
更没有延长原 $\log g$ 的可约化窗口。

用 (10) 的基准代入 R597 全部原公式。
原 $s$ 阶移位仍先在 $w$ 中实施：
$\mathscr SA^*$、$\mathscr S(B^*\eta_0)$、
$\mathscr S^2A^*$ 和两条十三行全保。
特别，$A^*\in w^m$ 且 $m\le s$，
不推出 $\mathscr SA^*=0$。

由于 $m-2\ge12$，R597 的所有三阶展开所需消项门均成立。
首 forcing 的非carry部分 $A^*/p$、$B^*\xi$
都从 $w^m$ 起；除 $p$ 仍只在原所需截断后作。
而整个第三块准确为
$$
\boxed{\Psi_2=a\,\pi_\ell\mathscr SZ^+
=\begin{cases}
a z_0,&\ell=1,\\
a(z_0+z_1w),&\ell=2.
\end{cases}}
\tag{11}
$$
一阶 Laurent 极 $\kappa=C^*/B^*$ 与 $\xi$ 的乘积
至少从 $w^{m-3}$ 起，故不会进入长度 $\ell\le2$；
这次消失由真实来源选择 (5) 支付。

若原候选写作 $P^{\rm base}+pR^{\rm base}$，
换为 (5) 时必须取
$$
R^*=R^{\rm base}+(P^{\rm base}-P^*)/p .
\tag{12}
$$
因此同一个实际两位来源保持不变。
之后仍按 R597 的完整低行右逆和
$\mathcal K_{2,\ell}$ 将它正规化，
并用该同一个 $R$ 计算全部前两块、$z_0,z_1$ 及真正 $d_2$。
(10) 不许可在已经固定的旧 $R$ 上单独换掉 $\xi$。

这条定量规范把真实 forcing 的非carry项推到约 $(25/6)D$ 的深度，
没有改变整个实际像商，也没有证明指定高续段的非零或可消。
若 (1) 已进入旧 R412/R444 的满射窗，
仍只使用那些已付结论，不由本记录重复登记新的满射范围。

依赖：
[R597](../results/R597-original-nodal-critical-lift-and-complete-low-ell-second-class.md)、
R412 的原逐阶连续电荷单位块、
R593 的整个 $w^{13}$、$U_0$ 及同一修正到第三精度的运输。
