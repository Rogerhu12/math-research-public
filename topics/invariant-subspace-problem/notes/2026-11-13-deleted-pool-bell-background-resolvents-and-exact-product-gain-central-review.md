# 全池删除后的实际 Bell 背景：有限占据头、改进共同预解与精确乘积负项

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI 辅助：GPT-6 Astra Pro。
状态：root 全文核验576行及R115原归一化幂界的完整背景演算引理；原双导子端段尚未排除。
本文的 $G_n$ 是普通 Bell 累积量，不能与准确共振的快系数 $G_n$ 混同。

## 1. 范围、实际变量和两项未付连接

固定
$$
1<\alpha<3,\qquad \beta>0.
$$
设主系数非零幅度的非增重排恰为
$$
\rho_n=e^{-\beta n^\alpha},\qquad n\ge1.
\tag{1.1}
$$
相位和物理排列任意。
固定复 $\ell^2$ 指数权，写
$$
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j),\qquad V(z)=\frac{1-z}{1+z}.
$$
因 $a\in\ell^1$，实际 first 全域有界：
$$
X=a_*I+\sum_ja_jR_j,\qquad
s=a_*+\sum_ja_j,\qquad Z=X-sI.
$$
普通 Bell 累积量为
$$
G_n=\sum_ja_j^n L_n(R_j),\qquad
L_n(v)=
\left.\frac{d^n}{dz^n}
\log(\cosh z+v\sinh z)\right|_{z=0},
\quad n\ge2.
\tag{1.2}
$$
其中 $L_n(1)=0$。
全部级数按范数绝对收敛。

固定非零多项式 $q$，次数为 $p$，设 $q(s)=0$，
并记这个根的重数为 $m\ge1$。
令
$$
\mathcal P(z;\kappa)
=\exp\left(\sum_{n=2}^p\frac{\kappa_n}{n!}\partial_z^n\right)q(z),
\qquad
T=\mathcal P(X;G).
\tag{1.3}
$$
本文所有算子和全部有限位导子都是全域有界的。
对有界实现，不再存在未付闭算子幂域问题。

本文证明：

1. 同时删除几乎全部排序前 $N$ 位后，
   剩余背景在各向异性圆 $R_n=\varepsilon\rho_N^n$ 上的实际共同成本仅为
   $O(N^{4\alpha/3}+N^\alpha\log N)$。
2. 背景的 $T_0^{2r-\ell}$ 与准确位系数逆乘积合并求值，
   可取得严格的 $-cN^{\alpha+1}$ 主项；
   它来自全部所选幅度的乘积，不能以共同最小幅度替代。

但以下连接仍未证明：

- 原双导子稿的 $L_{a_j}(X;G)$ 含有所有选中位，
  本稿的 $L_j^{(0)}$ 在整个池已删除的共同背景上求值。
  两者不能在原 $U_N$ 本体内直接替换。
- 原正交伪逆末段
  $U_N(\operatorname{ad}_T^{2r-\ell}V_N)f$
  尚未被合法改写为本稿估计的背景乘积。
  本稿不将这一改写当作成立，也不更换原有界正交投影。

## 2. 全池选择及精确多仿射背景

固定一个常数 $A>0$，取
$$
h_N=1+\left\lceil A\log_{16}(N+2)\right\rceil.
\tag{2.1}
$$
令 $J_N$ 是按幅度排序的前 $N$ 个实际物理位置，
并置
$$
I_N=J_N\setminus\{j:0\le j<h_N\},\qquad Q_N=|I_N|.
\tag{2.2}
$$
于是
$$
N-h_N\le Q_N\le N,\qquad
\min I_N\ge h_N,\qquad
\min_{j\in I_N}|a_j|\ge\rho_N.
\tag{2.3}
$$
不再删除排序最前的固定比例。
由于 $h_N\to\infty$，所有有限个大幅度的物理位置最终均被排除，
所以
$$
\max_{j\in I_N}|a_j|\longrightarrow0.
\tag{2.4}
$$
这个事实对任意物理排列成立。

对整个 $I_N$ 同时作原双导子稿的真实截断：

- $j\in I_N$ 时，将 $N_j$ 换成纯位 $E_j$；
- $j\notin I_N$ 且其后有选中位时，在下一个选中位之前截断，
  写成 $N_j^{[k]}$；
- 其后没有选中位时，保留原实际 $N_j$。

记截断族为 $\widetilde N_j$。
它们两两交换；
所有未选 $\widetilde N_j$ 与选中位上的全部矩阵代数交换。
截断平方关系、统一真实逆界和任意跨度误差，
均由原完整多仿射截断证明给出。

现在把全部选中的 $E_j$ 同时置为零。
这样得到真正的背景：
$$
\boxed{
H_{1,0}=Z_0
=\sum_{j\notin I_N}
a_j\bigl[V(t_j\widetilde N_j)-I\bigr],
}
\tag{2.5}
$$
$$
\boxed{
H_{n,0}=G_{n,0}
=\sum_{j\notin I_N}
a_j^nL_n\bigl(V(t_j\widetilde N_j)\bigr),
\quad2\le n\le p,
}
\tag{2.6}
$$
$$
X_0=sI+Z_0,\qquad
T_0=\mathcal P(X_0;G_0).
\tag{2.7}
$$
这些是按范数绝对收敛的真实有界和。
它们相互交换，也与选中位的全部矩阵交换。

在背景中保留的排序前 $N$ 位，全部位于物理头 $j<h_N$，
所以至多有 $h_N$ 个。
其余保留项的幅度排序均在 $N$ 之后。

## 3. 有限占据头的统一四次幂界

先给实际估计的一般形式。
设
$$
H_{\rm head}=\sum_{j\in F} d_j\,\widetilde N_jW_j,
\qquad |F|\le h,
$$
其中各因子交换，
$$
\sup_j\|W_j\|\le C_W,\qquad \sum_{j\in F}|d_j|\le C_d.
\tag{3.1}
$$
每个 $\widetilde N_j$ 是原 $N_j$ 或真实有限截断。

实际非负锥有
$0\le N_j^{[k]}\le N_j$，从而对每个整数 $v\ge1$，
$$
\|(N_j^{[k]})^v\|\le\|N_j^v\|.
$$
R110/R115 的原归一化幂界给
$$
\|\widetilde N_j^v\|
\le
\exp\left[-\frac14\,2^{4j}(v-1)^4\right].
\tag{3.2}
$$
这一步使用真实归一化算子，不是形式幂次数。

展开 $H_{\rm head}^k$，某一占据数组为 $(v_j)$，
$\sum v_j=k$。
令 $u_j=(v_j-1)_+$。
则
$$
\sum_j u_j\ge(k-h)_+.
$$
加权 Hölder 给
$$
\sum_j2^{4j}u_j^4
\ge
\frac{(k-h)_+^4}
{\left(\sum_{j\ge0}2^{-4j/3}\right)^3}.
$$
全部多项式系数绝对求和只付 $(C_WC_d)^k$，所以
$$
\boxed{
\|H_{\rm head}^k\|
\le C^k e^{-c(k-h)_+^4}.
}
\tag{3.3}
$$
$C,c$ 不依赖 $h$、$F$、最大物理位置或截断端点。

在 (2.5)、(2.6) 的每一行中，
$V(tz)-1$ 和 $L_n(V(tz))$ 均真实地含一个 $z$ 因子；
余下有理函数在全部原算子和截断上有一致范数界。
因此背景物理头都满足 (3.1)，且
$C_W,C_d$ 仅依赖原固定行、权和固定次数 $p$。
特别，这里没有引入 $e^{C16^{h_N}}$ 的头部商范数。

从 (3.3) 直接求指数级数，
对全部复数 $z$ 有
$$
\boxed{
\|e^{zH_{\rm head}}\|
\le
K\exp\left[
C h\log(2+|z|)
+C\bigl(1+\log(2+|z|)\bigr)^{4/3}
+C
\right].
}
\tag{3.4}
$$
例如把 $k\le h$ 与 $k=h+\ell$ 分开，
随后优化
$\ell\log(C(2+|z|))-c\ell^4$ 即得此式。
分母 $k!$ 可以保留，也可为上界而舍去；
都不改变 (3.4) 的适用常数。

## 4. 排序尾的小范数及真正 Laplace 预解

由积分比较，对每个固定 $1\le n\le p$，
$$
\sum_{k>N}\rho_k^n
\le C_nN^{1-\alpha}\rho_N^n.
\tag{4.1}
$$
令背景的剩余排序尾为 $H_{n,\rm tail}$。
统一有理函数界给
$$
\|H_{n,\rm tail}\|
\le C_n'N^{1-\alpha}\rho_N^n.
\tag{4.2}
$$
因此对任意固定 $\varepsilon>0$，
取
$$
R_n=\varepsilon\rho_N^n,
$$
充分大 $N$ 后有
$$
\|H_{n,\rm tail}\|\le R_n/4.
\tag{4.3}
$$
这里使用了 $\alpha>1$。

头尾相互交换。
对 $|\zeta|=R_n$，(3.4)、(4.3) 给真正的范数可积式
$$
\zeta(\zeta-H_{n,0})^{-1}
=
\int_0^\infty e^{-t}e^{tH_{n,0}/\zeta}\,dt.
\tag{4.4}
$$
可用积分求导与端点验证左右逆，不是只写形式 Laplace 级数。
所有复方向均被同一个范数估计控制。

设 $\Lambda_n=\log^+(R_n^{-1})=O(N^\alpha)$。
被积函数的对数上界为
$$
-\frac34t
+C h_N(\Lambda_n+\log(2+t))
+C(\Lambda_n+\log(2+t)+1)^{4/3}+C.
$$
将 $\log(2+t)^{4/3}$ 吸收到固定比例的 $t$，
剩余 $(2+t)^{Ch_N}$ 的积分只付
$O(h_N\log(h_N+2))$。
因此
$$
\boxed{
\log^+\sup_{|\zeta|=R_n}
\|\zeta(\zeta-H_{n,0})^{-1}\|
\le
C_\varepsilon\left[
N^{4\alpha/3}+h_NN^\alpha
+h_N\log(h_N+2)+1
\right].
}
\tag{4.5}
$$

这给所有固定有限背景行的实际共同演算：
若 $F_N$ 在多圆盘
$$
|z_n|\le R_n,\qquad1\le n\le p
$$
的邻域全纯，则
$$
\boxed{
\|F_N(H_{1,0},\ldots,H_{p,0})\|
\le
K\sup_{\prod|\zeta_n|=R_n}|F_N(\zeta)|
\exp(\Gamma_{0,N}),
}
\tag{4.6}
$$
其中
$$
\boxed{
\Gamma_{0,N}
\le C_{\varepsilon,A}
\left[N^{4\alpha/3}+N^\alpha\log(N+2)+1\right]
=o(N^{\alpha+1}).
}
\tag{4.7}
$$
这里共同 Cauchy 演算只付一次成本，
不按选中位或乘积因子重复付费。
全部背景变量属于由实际截断族生成的交换幺 Banach 代数，
其唯一字符把每个截断模式送到零，
所以这些变量的谱均为 $\{0\}$，多圆演算合法。

## 5. 背景差分单位的准确下界

对 $j\in I_N$，定义
$$
L_j^{(0)}
=
\mathscr L_{a_j}(X_0;G_0),
\qquad
\mathscr L_a(z;\kappa)
=-2[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)].
\tag{5.1}
$$
这是背景上的实际差分单位。

取固定足够小的 $\varepsilon>0$。
原 Bell 根重数估计在
$$
|z_1|\le2\varepsilon\rho_N,\qquad
|\kappa_n|\le2\varepsilon\rho_N^n
$$
上给
$$
\boxed{
|\mathscr L_{a_j}(s+z_1;\kappa)|
\ge c_q|a_j|^m
\quad(j\in I_N).
}
\tag{5.2}
$$
因为 $|a_j|\ge\rho_N$，
其主要项 $-2q(s-2a_j)$ 的模为固定常数乘 $|a_j|^m$；
全部按 Bell 权分组的扰动为
$O(\varepsilon|a_j|^m)$。
(2.4) 保证最终避开其它固定标量根。

同一个圆盘还给
$$
\boxed{
|\mathcal P(s+z_1;\kappa)|
\le C_q\varepsilon\rho_N^m.
}
\tag{5.3}
$$
该式使用 $q$ 在 $s$ 的真实重数 $m$。
各 Bell 权低于 $m$ 的项多出相应的 $z_1$ 次数，
权高于 $m$ 的项则更小。
不将普通累积量误认为快系数。

于是对任意 $F\subset I_N$，$|F|=r$，任意整数 $k\ge0$，
由同一次 (4.6) 得
$$
\boxed{
\left\|
T_0^k\prod_{j\in F}(L_j^{(0)})^{-2}
\right\|
\le
K(C_q\varepsilon)^k c_q^{-2r}
\rho_N^{mk}\prod_{j\in F}|a_j|^{-2m}
e^{\Gamma_{0,N}}.
}
\tag{5.4}
$$
这是完整 $H$ 上真实有界乘积；
所有因子交换且各个逆均已在共同全纯域内构造。
没有使用未知核关系或假定未知限制的稠密值域。

## 6. 精确幅度乘积产生的严格负项

固定
$$
0<\eta_-<\eta_+<1/2.
$$
取整数 $r=r_N$ 满足
$$
\eta_-N\le r\le\eta_+N
$$
且 $r\le Q_N$。
原投影方案中的 $r=\lfloor\eta Q_N\rfloor$ 满足这个要求。

对任意 $F\subset I_N$、$|F|=r$，
最坏的逆幅度乘积由排序最后的 $r$ 个位置给出：
$$
\sum_{j\in F}\log|a_j|^{-1}
\le
\beta\sum_{v=N-r+1}^N v^\alpha.
\tag{6.1}
$$
令
$$
k=2r-\ell,\qquad0\le\ell\le2r.
$$
由 (5.4)，
$$
\begin{aligned}
\log\left\|
T_0^{2r-\ell}\prod_{j\in F}(L_j^{(0)})^{-2}
\right\|
\le{}&
-m\beta(2r-\ell)N^\alpha\\
&+2m\beta\sum_{v=N-r+1}^N v^\alpha
+\Gamma_{0,N}+C(r+k+1).
\end{aligned}
\tag{6.2}
$$
用
$$
\sum_{v=N-r+1}^Nv^\alpha
=
\frac{N^{\alpha+1}-(N-r)^{\alpha+1}}{\alpha+1}
+O(N^\alpha)
$$
并注意
$$
d_\alpha(\eta)
=
\eta-\frac{1-(1-\eta)^{\alpha+1}}{\alpha+1}>0
\quad(0<\eta<1),
$$
在 $[\eta_-,\eta_+]$ 上取正最小值，
得到固定 $c_*>0$：
$$
\boxed{
\log\left\|
T_0^{2r-\ell}\prod_{j\in F}(L_j^{(0)})^{-2}
\right\|
\le
-c_*N^{\alpha+1}
+m\beta\ell N^\alpha
+\Gamma_{0,N}+O(N^\alpha+N).
}
\tag{6.3}
$$
它对所有上述 $F,r,\ell$ 一致成立。

特别，原末短段长度
$$
L_N=\left\lceil C_0N^{(\alpha+1)/4}\right\rceil
$$
满足
$$
\sup_{0\le\ell<L_N}\ell N^\alpha
=o(N^{\alpha+1})
\quad(\alpha<3).
$$
所以 (6.3) 在整个末短段统一给
$$
\left\|
T_0^{2r-\ell}\prod_{j\in F}(L_j^{(0)})^{-2}
\right\|
\le e^{-c_*N^{\alpha+1}/2}
$$
对充分大 $N$ 成立。

若还乘原固定局部导子因子
$$
C_D^\ell
e^{-(5/6)\ell^4+105\ell^3},
$$
则对全部 $0\le\ell\le2r$ 也可统一支付：
$$
\sup_{\ell\ge0}
\left[
m\beta\ell N^\alpha
-\frac56\ell^4+105\ell^3+\ell\log C_D
\right]
=O_D(N^{4\alpha/3}+N^\alpha+1).
$$
这一成本同样为 $o(N^{\alpha+1})$。
固定倍数的二项式、$e^{O(N)}$ 的右伪逆范数、
以及 $e^{O(N\log N)}$ 的外部组合系数也可吸收。

这些结论全部针对 (5.4) 的准确背景乘积。
不能因其指数合适就把原末段宣告趋零。

## 7. 真实 carry 的选择与独立性

对整个池的同时截断，
原任意跨度估计给
$$
\|T-\widetilde T\|
+\|Z-\widetilde Z\|
+\sum_{n=2}^p\|G_n-\widetilde G_n\|
\le
C e^{-385\,16^{h_N-1}}.
\tag{7.1}
$$
由于 (2.1)，
$$
16^{h_N-1}\ge(N+2)^A.
$$
因此只要后续已经支付的外部增长为 $e^{O(N^B)}$，
选任何固定 $A>B$ 即可使该 carry 乘积趋零。
增加这个固定 $A$ 只把 $h_N$ 改成固定倍数的 $\log N$，
不改变 (4.7) 的主幂。

例如原双导子稿已付的
$e^{O(N^{\alpha+1}+N\log N)}$ 范数预算，
选择 $A>\alpha+1$ 足够。
若一个新构造另有更大的、但明确固定的多项式指数成本，
须相应先选 $A$，不能免费沿用这个例值。

本文没有通过 (7.1) 自动控制未经展开的任意逆导子。
所有需要将背景逆替换为原逆的步骤，
仍须保留真实乘积顺序、共同演算和所需逆差预算。

全部常数的依赖如下：

- 可依赖原固定行、$q$、$p$、$m$、$\alpha$、$\beta$、
  倾斜权、$\varepsilon$、$A$ 和固定 $\eta_\pm$；
- 不依赖 $N$、所选 $F$、物理最大位或截断跨度；
- 涉及固定局部测试矩阵的常数只在最后导子界中额外依赖该矩阵。

## 8. 对原端点问题的准确意义

本文实际将“全池已删除的背景”共同成本从旧的
$N^{\alpha+1}$ 尺度降到
$$
N^{4\alpha/3}+N^\alpha\log N.
$$
这不是改变一个常数。
同时，保留全部 $\prod_{j\in F}|a_j|$ 后，
(6.3) 获得严格的负 $N^{\alpha+1}$ 项；
若提前把每个 $|a_j|$ 换成 $\rho_N$，该主项会被错误抹去。

但是原等式
$$
\sum_{\ell<L_N}\binom{2r}{\ell}
\mathcal B\!\left(
(\operatorname{ad}_T^\ell D)U_N
(\operatorname{ad}_T^{2r-\ell}V_N)f,g
\right)
$$
目前尚未被改写为这些背景乘积。
原 $V_N=(C_{I_N}^r)^\dagger$ 的正交范围投影必须继续保留；
系数匹配的非酉降阶共轭不能免费取代它。

尤其对于居中迟首共振二次
$X^2+Y-B$、$c_j\asymp a_j^\kappa$、$\kappa>2$，
一次系数为 $8a_jX+4c_j$，
其所需 $X$ 圆半径是 $a_N^{\kappa-1}$；
普通主尾范数 $O(a_NN^{1-\alpha})$
并不自动小于这一半径。
所以本文没有把普通 Bell 背景结论直接外推到该余族。

原交换子端点、该迟首临界族与完整 ISP 仍未关闭。
本文给的是一个可检验的真实背景演算接口。

## 9. 来源

- [全域 Bell 差分及双导子](../results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)：
  普通累积量、真实多仿射截断、全域差分单位及未闭的原末短段。
- [R115](../results/R115-unit-normalized-series-and-boolean-cyclicity.md)：
  真实归一化幂与不同占据预算。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意物理跨度壳估计及全部实际逆界。
- [两位伪逆校准](2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)：
  绝对小系数不自动吸收原最高伪逆导子项。
