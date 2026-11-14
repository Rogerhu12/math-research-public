# R270 第六附录：不交慢模式的点态多项式积与全部平移幂

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明；这是已证单模式循环图定理的实际独立位乘积闭合。
不把同一主模式的不同根因子视为支持不交。

## 1. 结论及单模式前提

取有限个复 first
$$
u_\nu=c_\nu+\sum_{j\ge0}a_{\nu j}\chi_j,\qquad
a_\nu\in\ell^2,\qquad 1\le\nu\le d.
$$
假设其非恒定部分的物理支撑两两不交：
$$
J_\nu=\{j:a_{\nu j}\ne0\},\qquad
J_\nu\cap J_\mu=\varnothing\quad(\nu\ne\mu).
\tag{1.1}
$$
指数权
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2
$$
任意，可以与所有 $J_\nu$ 重叠。

**一般乘积定理。**
给定非零标量多项式 $q_\nu$。
假设每个单模式向量 $q_\nu(u_\nu)e^w$ 已有循环性结论。
则
$$
\boxed{
\left[\prod_{\nu=1}^d q_\nu(u_\nu)\right]e^w
\text{ 对原实际 }A\text{ 循环}.
}
\tag{1.2}
$$
它也自动非零。

**无条件平移幂推论。**
若每个 $u_\nu$ 非常数，则对任意
$\lambda_\nu\in\mathbb C$、$m_\nu\ge1$，
$$
\boxed{
\prod_{\nu=1}^d(u_\nu-\lambda_\nu)^{m_\nu}e^w
\text{ 循环}.
}
\tag{1.3}
$$
常数模式可以加入，只须其相应常数因子非零。
主行可全部是任意慢的 $\ell^2\setminus\ell^1$ 行，
不需要熵条件、空谱锚或快辅助模式。

这里所用的单模式事实确为点态幂：

- [R144](R144-first-mode-shift-resultant-cyclicity.md) §1 推论 1.2、式 (1.3) 证明任意非常数复 $\ell^2$ first 的
  $(u-\lambda)^m$ 循环。
- [R147](R147-exponential-weighted-first-mode-polynomial-cyclicity.md) §1 定理 1.1 后推论 1 及 §9 首段，
  明确把它扩为任意复 first 指数权下的
  $(u-\lambda)^me^w$。
- 它来自 $q(z)=(z-\lambda)^m$ 与
  $q(z-2a_{j_0})$ 互素；两个唯一根相差非零 $2a_{j_0}$，
  不存在附加尾假设。

这不是自然算子幂 $(X-\lambda)^m$ 的结论。
其真实算子包含全部单模式 Bell 修正，下面完整保留。

本推论也没有关闭同一模式的任意普通 $q(u)$：
例如 $(u-a)(u+a)$ 的两个因子使用同一个支撑，
违反 (1.1)，其对应标量多项式还可能与平移多项式有共同根。
不能借 (1.3) 把这样的同模式因子分别处理后相乘。

## 2. 倾斜 first 及共同自然词域

置
$$
R_j=V(e^{-2b_j}N_j),\qquad
X_\nu=X_{\nu,b},\qquad \xi=e^w.
$$
每个 $X_\nu$ 是 R176 的实际倾斜闭 first，
有 $C_0$ 自伴性，全部有界交换子保持其自然幂域并与之交换。

需要的共同域结论是：
$$
\boxed{
\xi\text{ 属于任意有限混合词 }
X_{\nu_r}\cdots X_{\nu_1}
\text{ 的自然域，且该值只依赖出现次数}.
}
\tag{2.1}
$$
它是 R145 的实际 mixed-jet 证明在固定指数基 $\xi$ 上的版本，
也可由 R147/R176 的倾斜形式直接得到。
为避免从单个模式的幂域擅自推多模式域，简述验证如下。

对有限截断
$$
X_{\nu,N}=c_\nu I+\sum_{j<N}a_{\nu j}R_j
$$
和参数 $\mathbf t$，不同位恒等式给真正的有限 Bell 等式，
其点态端为 $e^{\sum t_\nu u_{\nu,N}+w}$。
各二阶以上混合 cumulant 的系数行按 $\ell^2$ 乘积估计可和，
所以对应 Bell jets 按算子范数收敛。
点态混合矩乘 $e^w$ 在 $H$ 收敛，由 Rademacher 矩界、
指数矩及 Hölder 得到。

像 R145 的三角 Bell 递推一样，
由总次数归纳构造
$$
v_\alpha=\lim_N\prod_\nu X_{\nu,N}^{\alpha_\nu}\xi
\quad\text{于 }H.
$$
对每个模式的通常伴随有限柱图核心测试，
$X_{\nu,N}^*g\to X_\nu^*g$，
故
$$
v_\alpha\in\operatorname{Dom}X_\nu,\qquad
X_\nu v_\alpha=v_{\alpha+e_\nu}.
\tag{2.2}
$$
这里倾斜只增加一个有界交换项，因此伴随图核心保持有效。
反复 (2.2) 得到 (2.1)。

更强地，令
$$
\mathcal E
=\operatorname{span}\{Dv_\alpha:
D\in\{A\}',\ \alpha\in\mathbb N_0^d\}.
\tag{2.3}
$$
则 $\mathcal E$ 包含 $\xi$，被每个 $X_\nu$ 和所有有界交换子保持，
并包含于全部有限混合词的自然域。
这些闭算子在 $\mathcal E$ 上代数交换。
后续全部算子词都在这个明确的共同域上进行。

## 3. 每个点态多项式的真实 Bell 算子

对第 $\nu$ 个模式，记
$$
K_{\nu,n}=\sum_j a_{\nu j}^n L_n(R_j),\qquad n\ge2,
$$
其中 $L_n$ 是 R270 使用的真实对数 cumulant 多项式。
这些和按算子范数绝对收敛，属于 $\mathcal A$；
本稿不把它们归入 $\mathcal G$。

将 $q_\nu$ 归一为首一，次数记为 $p_\nu$。
定义真实自然算子
$$
T_\nu=
\left[
\exp\left(\sum_{n=2}^{p_\nu}
\frac{K_{\nu,n}}{n!}\partial_z^n\right)
q_\nu(z)
\right]_{z=X_\nu},
$$
$$
\operatorname{Dom}T_\nu=\operatorname{Dom}X_\nu^{p_\nu}.
\tag{3.1}
$$
指数仅是有限微分多项式。
R176 给 $T_\nu$ 闭、$C_0$ 自伴，且
$$
\boxed{T_\nu\xi=q_\nu(u_\nu)e^w.}
\tag{3.2}
$$
它的所有有界 Bell 系数都是完整交换子，
因此 (2.3) 在 $T_\nu$ 下保持不变。

单模式前提使 (3.2) 循环。
R176 的图循环定理遂给
$$
\overline{\operatorname{Ran}T_\nu}=H.
\tag{3.3}
$$
$C_0$ 自伴性同时给 $\ker T_\nu=0$。
因此对于任意循环 $x\in\operatorname{Dom}T_\nu$，
再次使用同一个图循环定理，
$$
\boxed{T_\nu x\text{ 循环}.}
\tag{3.4}
$$
这一步不能仅由 (3.2) 的一个循环输出直接猜测；
真正的桥是其闭自然图和 R176 的任意循环域向量图核心。

## 4. 不交支持准确取消跨模式 Bell 项

对参数 $\mathbf t$，每个位的系数是
$$
\ell_j(\mathbf t)=\sum_\nu t_\nu a_{\nu j}.
$$
(1.1) 保证每个 $j$ 至多有一个非零模式系数。
所以局部 logarithm 的混合导数中，
只要涉及两个不同模式就严格为零。
总 cumulant 生成式准确分解为
$$
\sum_j\sum_{n\ge2}\frac{L_n(R_j)}{n!}\ell_j(\mathbf t)^n
=
\sum_\nu\sum_{n\ge2}
\frac{t_\nu^n K_{\nu,n}}{n!}.
\tag{4.1}
$$
它保留每个模式内部的全部高阶修正。

将各 $q_\nu(\partial_{t_\nu})$ 作用到真实混合生成式，
或者先在有限位验证后用 §2 取极限，得到
$$
\boxed{
\left[\prod_{\nu=1}^d q_\nu(u_\nu)\right]e^w
=
T_dT_{d-1}\cdots T_1\xi.
}
\tag{4.2}
$$
这是原 $H$ 中的向量等式；右边所有步骤都有真实自然域。

指数系数 $b_j$ 任意重叠不破坏 (4.1)：
它已经被包含在同一个固定局部 $R_j$ 中，
而跨模式 cumulant 的零因子仍是
$a_{\nu j}a_{\mu j}=0$。
没有假定权 $e^w$ 是全空间有界点乘。

## 5. 每一步的域及循环性

由 §2，$\xi\in\mathcal E$；
§3 给每个 $T_\nu\mathcal E\subseteq\mathcal E$。
因此按顺序
$$
x_0=\xi,\qquad x_\nu=T_\nu x_{\nu-1}
$$
时，每个 $x_{\nu-1}$ 都属于下一算子的准确自然域。

$\xi=e^w$ 循环。
对每一步使用 (3.4)，归纳得全部 $x_\nu$ 非零且循环。
最后由 (4.2) 得 (1.2)。

将每个 $q_\nu$ 取为 $(z-\lambda_\nu)^{m_\nu}$，
R147 的精确点态幂结论保证全部单模式前提，
于是得到 (1.3)。
也可混合使用 R144 的平移互素类、
R268 已关闭的某个单模式全部多项式类，
或其他已经具有 R176 Bell 图识别的单模式结果。

## 6. 一个没有空谱锚的独立慢例子

例如取
$$
u=\sum_{k\ge0}\frac{(-1)^k}{(k+1)^{3/4}}\chi_{2k},
\qquad
v=\sum_{k\ge0}\frac{(-1)^k}{(k+1)^{2/3}}\chi_{2k+1}.
$$
两行均在 $\ell^2\setminus\ell^1$；
各自的正、负部分都不可和。
它们的物理支撑分别为偶数位和奇数位。
对任意复 $\lambda,\mu$、任意正整数 $r,s$ 以及任意复 first 指数权 $w$，
$$
\boxed{(u-\lambda)^r(v-\mu)^s e^w\text{ 循环}.}
$$
此例不要求其中一个模式有空谱，也没有使用主行的排序熵预算。


## 6A. 有限共享头下的单原子版本

还可以允许各模式在同一个有限物理头 $J_0=\{0,\ldots,h-1\}$ 内重叠，
只要求删去该头后的支撑两两不交。
固定一个头原子 $\varepsilon\in\{\pm1\}^h$，记其指标函数为 $h_\varepsilon$。
在该原子上，各模式的低头成为标量，故
$$
h_\varepsilon
\prod_\nu(u_\nu-\lambda_\nu)^{m_\nu}e^w
=
c_\varepsilon h_\varepsilon
\prod_\nu(\widetilde u_\nu-\widetilde\lambda_{\nu,\varepsilon})^{m_\nu}
e^{w_{\rm tail}},
$$
其中 $\widetilde u_\nu$ 只使用尾部不交支撑，
$c_\varepsilon\ne0$ 来自指数权的有限头。
若有尾模式为常数，只须其对应标量因子不为零。

右侧不含 $h_\varepsilon$ 的尾向量由前述定理循环。
定义有限头的真实 Walsh 乘子
$$
H_\varepsilon=\sum_{F\subset J_0}
\widehat h_\varepsilon(F)\prod_{j\in F}V_j.
$$
它是真解析 $A$ 函数。更明确地，
$$
H_\varepsilon
=\prod_{j<h}\frac{I+\varepsilon_jV_j}{2}
=\left(\prod_{\substack{j<h\\\varepsilon_j=-1}}d_j^{-1}\right)
 A^{r_\varepsilon}\prod_{j<h}(I+N_j)^{-1},
\qquad
r_\varepsilon=\sum_{\substack{j<h\\\varepsilon_j=-1}}2^j.
$$
所有有限分母都是实际有界单位，$A$ 单射且像稠密，故 $H_\varepsilon$ 单射且像稠密。
同时 $H_\varepsilon1=h_\varepsilon\ne0$。

对任意只依赖尾坐标的 $g\in H$，有
$$
H_\varepsilon g=h_\varepsilon g.
$$
先对尾有限 Walsh 和用不同位恒等式
$V_FV_G1=\chi_{F\cup G}$ 验证，再用 $H_\varepsilon$ 有界、
头尾独立和 $L^2$ 稠密性取极限即可。
所以 $H_\varepsilon$ 把已知尾循环向量送成所需掩码向量。

因此该单原子加权点态积只要非零就循环。
这个结论保留掩码；不同头原子对应的循环向量之和，
不由本论证自动循环。

## 7. 没有覆盖的相乘

去掉掩码的乘积定理依赖物理支持真正不交。
即使只有有限个重叠位，也会出现非零的跨模式 Bell 修正；
它们虽可能是真解析或快系数，
却是多个独立慢变量之间的额外多项式项。
本稿没有将 R270 的一个慢变量定理直接用于这些项。

特别，同一 $u$ 的两个不同根因子不能当作两个不交模式；
未覆盖的普通 $q(u)$ 及一般独立慢多模式单个多项式核仍保持原范围。
本稿逐步应用各个已闭的 $T_\nu$；没有把它们在任意全域上的乘积自动称为闭算子。
