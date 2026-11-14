# R158：联合快模式的全纯点态符号与任意指数权

日期：2026-11-12。作者：l2_moments。状态：完整证明，根代理与 critical_kernel 已全文独立审读通过。
本正文在执行器失效后由完整上下文重建并复核；没有省略原稿的定义域或真实算子步骤。

本稿将 R154 的有限多项式推广为在实际联合紧值域的某个邻域内全纯的任意函数。
允许邻域不连通、值域非凸、模式代数依赖，以及任意复平方可和指数权。
证明使用逐位点态差分和有限头分支，不把点态 Walsh 代数与实际算子乘法混同。

## 1. 主定理

设有限个连续模式为
$$
u_\nu=a_{\nu,*}+\sum_{j\ge0}a_{\nu j}\chi_j,\qquad 1\le\nu\le d,
$$
并记
$$
a_j=(a_{1j},\ldots,a_{dj})\in\mathbb C^d,\qquad s_j=\|a_j\|_2.
\tag{1.1}
$$
假设联合幅度有限支持，或其非零降序重排满足
$$
\boxed{\frac{-\log s_\ell^*}{\ell^3}\longrightarrow+\infty.}
\tag{1.2}
$$
于是 $\sum_js_j<\infty$，向量值函数 $U=(u_1,\ldots,u_d)$ 连续，且
$$
K=U(\mathbb Z_2)\subseteq\mathbb C^d
\tag{1.3}
$$
为紧集。取任意开集 $\Omega\supseteq K$ 与全纯函数 $F:\Omega\to\mathbb C$。

另取任意复第一 chaos
$$
w=b_*+\sum_j b_j\chi_j,\qquad b\in\ell^2.
\tag{1.4}
$$
它可与全部快模式完全重叠，不要求任何相位、首位或快尾条件。

**定理1.1。** 存在真实有界乘子 $P_{F,w}\in\mathcal G$，满足
$$
\boxed{P_{F,w}e^w=F(U)e^w.}
\tag{1.5}
$$
这里 $\mathcal G$ 为 R151 的四次型解析逼近代数。实际非零判据为
$$
\boxed{P_{F,w}\ne0\quad\Longleftrightarrow\quad F(U)\ne0\text{ 于 }H.}
\tag{1.6}
$$
因此每个非零 $F(U)e^w$ 对 $A$ 循环。若 $F(U)$ 不是常数，则
$$
\boxed{(F(U)-\lambda)e^w\text{ 对每个 }\lambda\in\mathbb C\text{ 都循环}.}
\tag{1.7}
$$
若 $F(U)$ 为常数，仅排除使该向量为零的那个参数。

非零 $P_{F,w}$ 还在所有闭不变限制及所有有限放大上具有稠密像；
R153 进一步给它在所有非零不变子商上的单射稠密性。
当 $w=0$ 时，$P_{F,0}1=F(U)$，故 $P_{F,0}$ 就是该符号的实际有界乘子。

没有要求一个 Taylor 球覆盖整个 $K$。
后文只在有限多个实际头取值附近、各自的小尾球内展开。

## 2. 指数权的真实逐位替换算子

沿用
$$
N_j=A^{2^j}/W_{2^j},\qquad V_j=(I-N_j)(I+N_j)^{-1}.
$$
已有
$$
N_j^2=\eta_jN_{j+1},\qquad\eta_j\to0,\qquad\|N_j\|=1.
\tag{2.1}
$$
每个 $N_j$ 拟幂零。
若 $h$ 不依赖第 $j$ 位，则真实恒等式 $V_jh=\chi_jh$ 成立。

定义
$$
q_j=e^{-2b_j},\qquad M_j=(I-q_jN_j)(I+q_jN_j)^{-1}.
\tag{2.2}
$$
$I+q_jN_j$ 在 $\mathcal A$ 中为单位，故每个 $M_j$ 都是一个真解析芽在 $A$ 上的值；其字符为1。
这不要求同一解析圆盘适用于全部 $j$。

### 2.1 对指数向量的精确作用

令 $h_j=e^{w-b_j\chi_j}$，则 $h_j\in H$ 且不依赖第 $j$ 位。
Rademacher 偶矩或 R16 的乘积收敛保证这些指数向量属于 $H$。
设
$$
D_j=\cosh b_j\,I+V_j\sinh b_j,\qquad
E_j=\sinh b_j\,I+V_j\cosh b_j.
$$
则
$$
D_jh_j=e^w,\qquad E_jh_j=\chi_je^w.
$$
实际计算给
$$
D_j=e^{b_j}(I+q_jN_j)(I+N_j)^{-1},\qquad E_jD_j^{-1}=M_j.
\tag{2.3}
$$
因而 $M_je^w=\chi_je^w$。
若有限集合 $J$ 不含 $j$，则 $\chi_Jh_j$ 仍不依赖第 $j$ 位；
同一计算给 $M_j(\chi_Je^w)=\chi_{J\cup\{j\}}e^w$。
归纳得到
$$
\boxed{M_Je^w=\chi_Je^w,\qquad M_J=\prod_{j\in J}M_j.}
\tag{2.4}
$$
这里只在每个位至多出现一次的 Walsh 单项式上使用乘积。

### 2.2 统一界及真实 $N_j$ 因子

因为 $b_j\to0$，对充分大的 $j$ 有 $|q_j|\le2$ 与 $|q_j|^2\eta_j\le1/2$。
利用真实关系 (2.1)，
$$
(I+q_jN_j)^{-1}=(I-q_jN_j)(I-q_j^2N_j^2)^{-1}
$$
给这些 $j$ 上的统一界
$$
\|(I+q_jN_j)^{-1}\|\le6.
$$
剩余有限多个逆各自有界，故
$$
\boxed{
C:=\max\{1,\sup_j\|M_j\|\}<\infty,\qquad
C_1:=\sup_j2|q_j|\|(I+q_jN_j)^{-1}\|<\infty.
}
\tag{2.5}
$$
并且有真正的算子因式
$$
\boxed{M_j-I=-2q_jN_j(I+q_jN_j)^{-1}.}
\tag{2.6}
$$
低位的常数可以很大，但位数有限；所有后续常数允许依赖固定的 $w$。

## 3. 加权 Walsh 代数与非同态的符号映射

对有限 Walsh 和 $f=\sum_S\widehat f(S)\chi_S$ 定义
$$
\|f\|_{\mathscr W_C}=\sum_S|\widehat f(S)|C^{|S|}.
\tag{3.1}
$$
因 $|S\triangle T|\le|S|+|T|$ 与 $C\ge1$，
该范数对点态乘法次乘性成立。
完备化 $\mathscr W_C$ 是一个交换 Banach 代数，连续嵌入 $C(\mathbb Z_2)$，
且 $\|f\|_\infty\le\|f\|_{\mathscr W_C}$。特别有
$$
\|\chi_j-1\|_{\mathscr W_C}=C+1.
\tag{3.2}
$$

由 (2.5) 定义连续线性映射
$$
\Psi_w(f)=\sum_S\widehat f(S)M_S,\qquad
\|\Psi_w(f)\|\le\|f\|_{\mathscr W_C}.
\tag{3.3}
$$
它取值于 $\mathcal A$。对有限 Walsh 和，(2.4) 给
$$
\Psi_w(f)e^w=fe^w.
\tag{3.4}
$$

**必要区别。** $\Psi_w$ 一般不是点态代数同态，
因为 $\chi_j^2=1$ 而 $M_j^2$ 一般不等于 $I$。
所以不能把 $\Psi_w(F(U))$ 换成 $F(\Psi_w(u_1),\ldots)$。
我们只使用下列互不交坐标乘法：若 $g$ 不依赖第 $j$ 位，则
$$
\boxed{\Psi_w((\chi_j-1)g)=(M_j-I)\Psi_w(g).}
\tag{3.5}
$$
有限 Walsh 展开直接证明此式，随后可按范数连续性延拓。

## 4. 实际0锚与有限头分支

记
$$
\beta=(a_{1,*},\ldots,a_{d,*})+\sum_j a_j=U(0),
$$
并取锚定截断
$$
U_m=\beta+\sum_{j<m}a_j(\chi_j-1).
\tag{4.1}
$$
每个 $U_m(y)$ 正是将 $y$ 的全部 $j\ge m$ 位改成物理0后的 $U$ 值，因此
$$
U_m(y)\in K\quad\text{对全部 }m,y\text{ 成立}.
\tag{4.2}
$$
并且 $U_m\to U$ 一致。

取 $r>0$，使 $K$ 的闭 $2r$-多圆盘邻域紧含于 $\Omega$，并记
$$
L_F=\sup\{|F(z)|:\operatorname{dist}_\infty(z,K)\le2r\}<\infty.
\tag{4.3}
$$
这由 $K$ 的紧性和 $\Omega$ 的开放性得到。
选择一个固定整数 $m_0$ 足够大，使
$$
(C+3)\sum_{j\ge m_0}s_j<r.
\tag{4.4}
$$

将低 $m_0$ 位分成 $2^{m_0}$ 个物理柱 $\varepsilon$。
在每一柱内，$U_{m_0}$ 等于某个 $z_\varepsilon\in K$。
其柱指示函数满足
$$
\|1_\varepsilon\|_{\mathscr W_C}
=\left(\frac{1+C}{2}\right)^{m_0},\qquad
\sum_\varepsilon\|1_\varepsilon\|_{\mathscr W_C}=(1+C)^{m_0}.
\tag{4.5}
$$
对 $m\ge m_0$、$0\le t\le1$，在该柱写
$$
U_m-2ta_m=z_\varepsilon+H_{m,t},\qquad
H_{m,t}=\sum_{m_0\le j<m}a_j(\chi_j-1)-2ta_m.
$$
每个坐标在尾部 Walsh 代数中的范数满足
$$
\|(H_{m,t})_\nu\|_{\mathscr W_C}
\le(C+1)\sum_{j\ge m_0}s_j+2s_m<r.
\tag{4.6}
$$
所以在每个 $z_\varepsilon$ 处、半径 $2r$ 的多圆盘 Taylor 级数
都能在这个 Banach 代数中绝对收敛。
没有把不同 $z_\varepsilon$ 的展开中心合并成一个全局球。

## 5. 方向差商的一致 Walsh 范数界

令 $f_m=F(U_m)$，这是只依赖低 $m$ 位的柱函数。
若 $s_m>0$，记 $v_m=a_m/s_m$，故 $\|v_m\|_2=1$，并定义
$$
g_m=\frac{F(U_m)-F(U_m-2a_m)}{2s_m}.
\tag{5.1}
$$
这是不依赖第 $m$ 位的有限柱函数。
当 $s_m=0$ 时令 $g_m=0$。
对 $m\ge m_0$，由前节的局部邻域与线段积分，
$$
g_m=\int_0^1DF(U_m-2ta_m)[v_m]\,dt.
\tag{5.2}
$$

给出一个显式统一常数。
在每个 $z_\varepsilon$ 的 $2r$ 多圆盘上，Cauchy 估计给
$$
\frac{|\partial^{\alpha+e_\nu}F(z_\varepsilon)|}{\alpha!}
\le\frac{(\alpha_\nu+1)L_F}{(2r)^{|\alpha|+1}}.
\tag{5.3}
$$
用 (4.6) 和 $\sum_\alpha(\alpha_\nu+1)2^{-|\alpha|}=2^{d+1}$，
得到每个局部柱内
$$
\|DF(z_\varepsilon+H_{m,t})[v_m]\|_{\mathscr W_C}
\le\frac{d\,2^dL_F}{r},
\tag{5.4}
$$
其中用到 $|(v_m)_\nu|\le1$。
乘回互不交的有限头指示函数，并对 (5.2) 积分，遂有
$$
\boxed{
\sup_{m\ge m_0}\|g_m\|_{\mathscr W_C}
\le(1+C)^{m_0}\frac{d\,2^dL_F}{r}.
}
\tag{5.5}
$$
剩下有限多个 $g_m$ 各自都是有限柱函数。
它们可能不适用线段积分，因为低位连接线段未必在 $\Omega$ 内，
但 (5.1) 两端都属于 $K$，所以差商本身始终定义良好。
逐一纳入常数便得到
$$
\boxed{\sup_m\|g_m\|_{\mathscr W_C}<\infty.}
\tag{5.6}
$$
这也处理了不连通邻域的有限低位跨分支情形。

## 6. 逐位差分真实进入 $\mathcal G$

由于 $\chi_m$ 只有 $+1,-1$ 两值，精确点态恒等式为
$$
\boxed{f_{m+1}-f_m=s_m(\chi_m-1)g_m.}
\tag{6.1}
$$
第 $m$ 位物理0时两边都为零；物理1时两边都等于
$F(U_m-2a_m)-F(U_m)$。
由 (3.5)、(2.6)，有真正的算子差分
$$
\Psi_w(f_{m+1})-\Psi_w(f_m)=s_mN_mT_m,
\tag{6.2}
$$
其中
$$
T_m=-2q_m(I+q_mN_m)^{-1}\Psi_w(g_m).
\tag{6.3}
$$
每个 $g_m$ 是有限柱函数，因此 $\Psi_w(g_m)$ 为有限多个
真解析 $M_j$ 的线性组合及乘积；所以 $T_m$ 也是真解析芽在 $A$ 上的值。
由 (2.5)、(3.3)、(5.6)，
$$
\boxed{\sup_m\|T_m\|<\infty.}
\tag{6.4}
$$
有限头的真正解析性和无限尾的统一范数界均已分别证明。

R154 引理2.1（源自 R115 的带有界因子占据估计）指出：
若 $c_m$ 的降序模长为超三次，$T_m$ 逐项真解析且统一有界，则
$$
\sum_m c_mN_mT_m\in\mathcal G.
\tag{6.5}
$$
其理由是范数绝对收敛、有限头真解析，而实际尾的四次型趋于无穷。
该估计只在尾部使用因子范数；无需因子的字符非零或单位性。
对任意重排，需删除的有限多个大系数均可吸收进一个实际有限头，
所以没有把重排速度误当成原坐标速度。

将 (6.5) 用于 $c_m=s_m$，定义
$$
\boxed{
P_{F,w}=F(\beta)I+\sum_{m\ge0}s_mN_mT_m\in\mathcal G.
}
\tag{6.6}
$$
由 (6.2)，其部分和正是 $\Psi_w(f_m)$。
我们没有通过 $\mathcal G$ 的一般范数闭性得出此结论。

## 7. 极限、非零判据与循环性

由 $U_m\to U$ 一致及 $F$ 在 $K$ 上连续，$f_m\to F(U)$ 一致。
另一方面 (6.6) 的部分和在算子范数中收敛。
使用 (3.4) 与 $e^w\in H$，得到
$$
P_{F,w}e^w
=\lim_m\Psi_w(f_m)e^w
=\lim_mf_me^w
=F(U)e^w.
\tag{7.1}
$$
R16/R147 已证明每个这样的 $e^w$ 对 $A$ 循环，且它几乎处处非零。
若 $P_{F,w}e^w=0$，则 $P_{F,w}$ 杀掉 $e^w$ 的全部多项式轨道；
由其有界性与循环性，$P_{F,w}=0$。
反向显然，故得到 (1.6)。

若 $F(U)\ne0$，R151 给 $P_{F,w}$ 稠密像，并与 $A$ 交换。
因此
$$
\overline{\mathbb C[A]P_{F,w}e^w}
=\overline{P_{F,w}\,\overline{\mathbb C[A]e^w}}
=\overline{P_{F,w}H}=H.
\tag{7.2}
$$
这证明主定理。构造对 $F$ 线性，且常数1给 $I$，所以
$$
P_{F-\lambda,w}=P_{F,w}-\lambda I.
\tag{7.3}
$$
每个非零 $F(U)-\lambda$ 都适用同一证明。

这里实际非零无需模式独立性。
由于 $F(U)$ 连续且 Haar 测度具有全支撑，
$F(U)=0$ 于 $H$ 还等价于 $F$ 在实际紧集 $K$ 上恒为零，
但不等价于它在 $\Omega$ 上恒为零。

## 8. 覆盖范围及边界

1. 取多项式 $F$ 即重新得到 R154 的全部结论，
   包括快模式共振平方与任意指数方向的重叠。
2. 若 $G$ 在 $K$ 邻域全纯且在该邻域无零点，
   则 $F=1/G$、局部选定的全纯根等都可作为点态符号；
   只需确实存在定义在 $K$ 邻域的那个全纯函数，不能预设不存在的全局分支。
3. 函数可以在 $\Omega$ 的不同连通分支上取不同的解析表达式；
   有限头分支构造已包含这种情况。
4. 本稿要求 (1.2)，没有用一般 $\ell^1$ 慢尾替代它。
   也没有推出任意连续 $F(U)$ 都循环；一般连续函数缺少
   (5.6) 所需的统一加权 Walsh 方向差商界。
5. 证明未把 $e^w$ 当成有界点乘算子，未假设它有实际有界乘子；
   使用的只是单个循环向量 $e^w$ 与真实有界 $M_j$。

一般无限维 $L^2$ 端点与原不变子空间问题仍未由本稿解决。
