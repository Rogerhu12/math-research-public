# 可和超指数临界族的实际成本边界：任意双池失败与辅助预解下界

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。
**状态：已证明的实际成本边界。**
本文确定现有两种提升机制对一类真实余例所缺的成本，
不构造非零核，不证明该向量不循环，也不对一般可能方法作否定。

## 1. 一个准确保留的迟首临界族

固定
$$
\frac32<\alpha<3,\qquad \beta>0,\qquad \kappa>2.
$$
取自然物理顺序上的正主行
$$
a_j=e^{-\beta(j+1)^\alpha}\quad(j\ge0),\qquad
a_*=-\sum_{j\ge0}a_j,\qquad b=0.
\tag{1.1}
$$
主行可和，且其非零幅度重排准确为
$$
\rho_n=e^{-\beta n^\alpha}\quad(n\ge1).
\tag{1.2}
$$
令
$$
c_0=0,\qquad
c_j=a_j^\kappa=e^{-\kappa\beta(j+1)^\alpha}\quad(j\ge1).
\tag{1.3}
$$
辅助可和，在所有 $j\ge1$ 与主幅度的 $\kappa$ 次幂准确相等，
只缺失最早主位。

置
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v_c=\sum_jc_j(\chi_j-1),
$$
$$
f_\lambda=u^2+2\sum_j a_j^2(\chi_j-1)+v_c-\lambda.
\tag{1.4}
$$
实际自然算子在此全域有界：
$$
X=\sum_j a_j(R_j-I),\qquad
B=\sum_j a_j^2(R_j-I)^2,\qquad
Y=\sum_j c_j(R_j-I),
$$
$$
T_\lambda=X^2-B+Y-\lambda I,\qquad
R_j=V(N_j).
\tag{1.5}
$$
$T_\lambda1=f_\lambda$。

$X$ 的实际字符为零。
共同根定理因此把唯一可能坏位移明确为
$$
\boxed{\lambda=0.}
\tag{1.6}
$$
首位条件同样给 $c_0=-2a_0\chi(X)=0$，与 (1.3) 一致。
所有 $\lambda\ne0$ 已由首位字符互素排除，不重新列为未闭。

$f_0$ 实际非零：其任意两个不同非零主位的最高二阶 Walsh 系数为
$2a_i a_j\ne0$。
若写 $x_j=(1-\chi_j)/2$，还可明确看出
$$
f_0=8\sum_{i<j}a_i a_jx_ix_j
-2\sum_{j\ge1}a_j^\kappa x_j.
\tag{1.7}
$$
这不是恒等零的退化例。

## 2. 任意两个各 N 位池都不满足现有行列式预算

令 $I_N,J_N$ 是任意两个不交的真实物理位集，各有 $N$ 位。
不要求它们是连续排序带。
定义
$$
d_N=\min_{j\in I_N,k\in J_N}|a_kc_j-a_jc_k|.
$$
若某个行列式为零，则当然不能使用非零双池准则。
下面即使假设全部非零，成本仍超限。

并集有 $2N$ 个不同物理位，故至少有一位 $\ell$ 的主幅度排名不小于 $2N$。
于是
$$
a_\ell\le\rho_{2N}.
$$
从另一个池任取一位 $j$。
由全局有界性及 $c_\ell\le C a_\ell$，
$$
|a_jc_\ell-a_\ell c_j|
\le
\|a\|_\infty|c_\ell|
+\|c\|_\infty a_\ell
\le C a_\ell.
$$
这里 $C$ 与所选池及 $N$ 无关。
所以
$$
\boxed{
d_N\le C\rho_{2N}
=C e^{-\beta(2N)^\alpha}.
}
\tag{2.1}
$$
因此只要 $d_N>0$，
$$
1+\log^+d_N^{-1}
\ge \beta(2N)^\alpha-C.
\tag{2.2}
$$

现有二位提升需要
$$
1+\log^+d_N^{-1}=O(N^{3/2}).
$$
当 $\alpha>3/2$ 时，(2.2) 排除这个条件，
而且不是只排除某一固定两条排序带。
缩放任何固定常数的池尺寸也不改变指数冲突。

还可直接核对原双池输入的绝对系数，而不只观察最小行列式。
本例 $0<c_j\le a_j<1$（$c_0=0$ 也满足上界），所以
$$
\frac{a_j+a_k}{4|a_kc_j-a_jc_k|}
\ge \frac1{8\min(a_j,a_k)}.
\tag{2.3}
$$
两个池的并集中，至少 $N$ 位的主排名不小于 $N$；
其中一个池至少有 $N/2$ 个这样的位。
当 $r_N\asymp\sqrt N$ 时，可在该池选出 $r_N$ 个高排名位，
再在另一池选任意 $r_N$ 位。
无论固定匹配怎样安排，每一对均含一位幅度不超过 $\rho_N$。
于是这个实际输入的绝对系数预算至少为
$$
H_{I,J}\ge (8\rho_N)^{-r_N},
\qquad
\log H_{I,J}\ge\beta r_NN^\alpha-Cr_N.
\tag{2.4}
$$
这类子集确实出现在原完整双池平均中。
全部外部阶乘及幂次归一化最多减去 $O(r_N\log N)$，不能抵消 (2.4)。

因此现有绝对系数预算的逆成本达到 $r_NN^\alpha$，
而四次局部衰减是 $r_N^4\asymp N^2$。
不能通过固定调小平均参数来消去正指数差 $\alpha-3/2$。
这描述的是已建立输入及其范数控制方式的成本，
不是关于所有可能输入或平均方式的最优性定理。

## 3. 把实际辅助分成正锥主项和真正快修正

令
$$
Z=\sum_{j\ge1}c_jN_j.
\tag{3.1}
$$
全部 $N_j$ 在原函数锥上保持非负，$c_j>0$，故 $Z$ 是保序算子。
这不表示 $Z$ 是 Hilbert 自伴正算子。

由真实有理恒等式
$$
R_j-I=-\frac{2N_j}{1+N_j}
=-2N_j+\frac{2N_j^2}{1+N_j},
$$
准确有
$$
\boxed{
Y=-2Z+G,\qquad
G=2\sum_{j\ge1}c_jN_j^2(I+N_j)^{-1}.
}
\tag{3.2}
$$
这里
$$
N_j^2=\eta_jN_{j+1},\qquad
\eta_j\le e^{-385\,16^j}.
$$
$(I+N_j)^{-1}$ 是一致有界的真实解析因子。
所以 R154 引理2.1 给
$$
\boxed{G\in\mathcal G,\qquad\chi(G)=0.}
\tag{3.3}
$$
这使用实际 carry 的双指数快尾；
并没有假设慢主项 $Z$ 或 $Y$ 属于 $\mathcal G$。
全部算子因子交换。

R151 的零字符 $\mathcal G$ 四次幂型遂给常数 $C_G$，使
$$
\boxed{
\log^+\|e^{sG}\|
\le C_G[\log(2+|s|)]^{4/3}
}
\tag{3.4}
$$
对全部复 $s$ 成立。
确实，可由
$\|G^n\|\le C_0C_1^ne^{-\gamma n^4}$、
指数幂级数及四次 Legendre 上界直接得到 (3.4)。
若 $G=0$ 则更加直接。

## 4. 正锥半群的真实下界

R115 §4 的准确二进位归一化给，对不同位的任意有限集 $E$，
$$
\prod_{j\in E}N_j
=
M_{\sum_{j\in E}2^j},\qquad
\left\|\prod_{j\in E}N_j\right\|=1.
\tag{4.1}
$$
它不是纯 Boolean 近似。

对任意正整数 $m$，在 $Z^m$ 的保序展开中，
只保留所选的 $m$ 个不同位 $1,\ldots,m$。
这 $m!$ 个排列项都相同并非负，故
$$
Z^m\ge
m!\left(\prod_{j=1}^m c_j\right)
N_1\cdots N_m
$$
在函数锥序中成立。
正算子的范数在该锥序下单调，所以
$$
\|Z^m\|\ge m!\prod_{j=1}^m c_j.
\tag{4.2}
$$

对于实 $s>0$，再从 $e^{2sZ}$ 的保序指数展开中只取第 $m$ 项：
$$
\begin{aligned}
\|e^{2sZ}\|
&\ge \frac{(2s)^m}{m!}\|Z^m\|\\
&\ge (2s)^m
\exp\left[-\kappa\beta\sum_{j=1}^m(j+1)^\alpha\right].
\end{aligned}
\tag{4.3}
$$
注意指数展开中的 $m!$ 已与不同位排列的 $m!$ 准确抵消。

由
$$
\sum_{j=1}^m(j+1)^\alpha\le C_\alpha(m+1)^{\alpha+1},
$$
取
$$
m=\left\lfloor\varepsilon(\log s)^{1/\alpha}\right\rfloor
$$
且固定足够小的 $\varepsilon>0$，得到
$$
\boxed{
\log\|e^{2sZ}\|
\ge c_{\rm low}(\log s)^{1+1/\alpha}
}
\tag{4.4}
$$
对全部充分大 $s$ 成立。

由 (3.2) 的交换关系，
$$
e^{2sZ}=e^{-sY}e^{sG}.
$$
所以结合 (3.4)、(4.4)，
$$
\boxed{
\log\|e^{-sY}\|
\ge
c_{\rm low}(\log s)^{1+1/\alpha}
-C_G[\log(2+s)]^{4/3}.
}
\tag{4.5}
$$
因为 $\alpha<3$，
$$
1+\frac1\alpha>\frac43,
$$
右边的首项严格支配快修正成本。
因此实际慢辅助 $Y$ 不属于 $\mathcal G$；
若它属于，(3.4) 型上界将与 (4.5) 矛盾。

对居中的 $X$ 用同一分解，主系数换成 $a_j$，
也可得到 $X\notin\mathcal G$。
这不取消旧单变量 $\mathcal G[X]$ 理论的效力；
只是说明本例的独立慢 $Y$ 不能直接作为其快系数输入。

## 5. 真实圆周预解的下界

$Y$ 是实际有界零字符 $\mathcal A$ 元，故谱为 $\{0\}$。
对任意 $R>0$，定义真实圆周预算
$$
\Gamma_Y(R)=
\sup_{|z|=R}\log^+\|z(z-Y)^{-1}\|.
$$

对整个函数 $z\mapsto e^{-sz}$，
真实单变量 Cauchy 演算给
$$
e^{-sY}
=\frac1{2\pi i}\int_{|z|=R}
e^{-sz}(z-Y)^{-1}\,dz,
$$
从而
$$
\|e^{-sY}\|\le e^{sR}e^{\Gamma_Y(R)}
\quad(s>0).
\tag{5.1}
$$
取 $s=R^{-1}$，与 (4.5) 合并：
$$
\boxed{
\Gamma_Y(R)\ge
c_{\rm low}[\log R^{-1}]^{1+1/\alpha}
-C_G[\log(2+R^{-1})]^{4/3}-1
}
\tag{5.2}
$$
对充分小 $R$ 成立。
特别有
$$
\Gamma_Y(R)\ge c_{\rm res}[\log R^{-1}]^{1+1/\alpha}
\tag{5.3}
$$
对充分小 $R$ 成立。

这是原空间真实预解范数的下界，
不只是一个粗上界没有优化到所需阶数。
证明未声称某个固定方向恰取得圆周最大值。

## 6. 原公共半径上必须支付的超二次成本

对于任意固定 $D>0$ 和 $\epsilon>0$，取
$$
R_N=\epsilon\rho_N^D
=\epsilon e^{-D\beta N^\alpha}.
\tag{6.1}
$$
由 (5.2)–(5.3)，
$$
\boxed{\Gamma_Y(R_N)\ge c_DN^{\alpha+1}.}
\tag{6.2}
$$
因为快修正项的阶数为 $N^{4\alpha/3}$，
严格低于 $N^{\alpha+1}$。

二次近共振与结果式逆所用的公共尺度
$$
D=2(\kappa-1)
$$
只是 (6.1) 的一个特例。
即使完整乘积分母的共同预解成本只收取一次，
(6.2) 在 $\alpha>1$ 时仍高于 $N^2$，
故无法由现有 $r_N\asymp\sqrt N$ 的四次成本支付。

这不排除未知核上的逆远小于全空间圆周预算；
也不排除非圆轮廓、不同输入、不同配对或其他新机制。
准确结论只是：对本真实例，
当前“独立变量公共圆 + 全空间 $\Gamma_Y$”估计不能成为所需证明。

## 7. 与所有已经关闭范围的关系

本例：

- 是绝对可和主行，不能重新计入非可和主行二分。
- 满足
  $\log\rho_n^{-1}/n=\beta n^{\alpha-1}\to\infty$，
  所以没有指数下界种子。
- 当 $\alpha>3/2$ 时，任意双池的定量条件都由 (2.2) 失败。
- 辅助迟于主首位，且居中字符根与首位临界关系相容。
- 由实际半群下界知 $Y\notin\mathcal G$，
  不只是它未满足某个充分的排序快尾条件。
- 其唯一未由上述接口排除的位移是 $\lambda=0$；
  没有重新开放已经关闭的其他标量位移。

所以该族给出一个集中而明确的后续目标。
本文证明的是两条现行成本路线的真实不足，
不是非循环、点谱存在或 ISP 的反例。

## 8. 来源

- [R115](../results/R115-unit-normalized-series-and-boolean-cyclicity.md) §4：
  互异二进位归一化幂的准确范数恒等式。
- [R154](../results/R154-supercubic-modes-all-polynomials-exponential-weights.md) 引理2.1：
  带真实解析因子的快 carry 修正属于 $\mathcal G$。
- [R151](../results/R151-quartic-analytic-approximation-gauge-stability.md)：
  零字符 $\mathcal G$ 的正四次幂型及半群对数 $4/3$ 成本。
- [二位标量 Bézout 源](2026-11-13-two-site-scalar-bezout-lifts-and-late-support-quadratic-cyclicity-central-review.md)：
  实际双池行列式与精确平均成本。
- [非可和主行二分源](2026-11-13-nonsummable-main-dichotomy-and-all-order-sylvester-joint-inverses-central-review.md)：
  指数种子与一次联合预解的已证范围。
- [共同例外根定理](../results/R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md)：
  有界主行的准确字符根及唯一可能坏位移。

下一机制须额外利用真实核关系或改变输入结构；
本稿不以一条方法边界替代这项仍待证明的工作。
