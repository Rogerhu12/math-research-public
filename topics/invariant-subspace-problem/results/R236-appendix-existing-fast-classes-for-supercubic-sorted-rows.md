# R236 附录：排序指数行与既有快类的准确接口：超三次闭合及三次阈值

日期：2026-11-13（UTC）。作者：central_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明的适用范围核查。超三次结论是旧定理的直接推论，
不另计为新关闭范围；本稿防止把单个四次幂界误认为解析逼近类的定义。

已全文核读：
[R140](../results/R140-invariant-subquotient-type-and-fixed-first-regularization.md)、
[R151](../results/R151-quartic-analytic-approximation-gauge-stability.md)、
[R175](../results/R175-fast-symbol-standard-ideals-and-exact-boundary-kernels.md)、
[R179](../results/R179-fast-tail-subalgebra-and-relative-closed-ideals.md)。

## 1. 三种不同的实际条件

R151 的 $\mathcal G$ 要求存在真解析芽 $f_h$，使
$$
\|S-f_h(A)\|\to0,\qquad
\tau_4(S-f_h(A))\to+\infty,\qquad
\tau_4(B)=\liminf_{k\to\infty}
 \frac{-\log\|B^k\|}{k^4}.
\tag{1.1}
$$
单个估计 $\|S^k\|\le K e^{-dk^4}$ 只给 $\tau_4(S)\ge d$。
它既没有构造 (1.1) 的解析头，也没有给余尾型趋于无穷。

R179 的较具体子代数 $\mathcal T$ 要求实际表示
$$
S=H(A)+\sum_{n\ge1}c_n\frac{A^n}{W_n}V_n,\qquad
H,V_n\text{ 逐项真解析},\quad \sup_n\|V_n\|<\infty,
$$
$$
-\log c_\ell^*/\ell^3\longrightarrow+\infty.
\tag{1.2}
$$
同一正整数指数只列一项，重排的是系数幅度。
允许指数任意稀疏、物理排列任意。
R179 证明 $\mathcal T\subset\mathcal G$，
并证明每个非零 $S\in\mathcal T$ 生成标准闭主理想。

R175 的条件则直接是连续符号的坐标振幅
$$
d_j(f)=\frac12\sup_x|f(x)-f(x^{(j)})|,\qquad
-\log d_\ell^*(f)/\ell^3\to+\infty.
\tag{1.3}
$$
它允许任意物理重排，并给所有复 $\ell^2$ first 指数权下的标准理想。

## 2. $\alpha>3$ 已由旧定理关闭，且只需排序上界

设
$$
u=a_*+\sum_ja_j\chi_j,\qquad
\rho_k\le B e^{-\beta k^\alpha},\quad
\beta>0,\quad\alpha>3,
$$
其中 $\rho_k$ 为非零幅度递减重排。
不需要任何下界。
取非零多项式 $q$、任意复 $\ell^2$ first 指数权 $w$。

因为 $\sum_j|a_j|<\infty$，$u$ 连续且值域有界。
在包含其凸包的固定圆盘上取
$L_q=\sup|q'|<\infty$，则
$$
d_j(q(u))\le L_q|a_j|,\qquad
d_k^*(q(u))\le L_q\rho_k.
\tag{2.1}
$$
所以 $f=q(u)$ 满足 R175 的超三次振幅条件。

若 $a$ 有无限支撑，$u$ 不可能只有有限个值：
否则其有限值之间有正最小距离，
一致连续性会使足够细的每个柱集上 $u$ 恒定，
从而 $u$ 是有限柱，其全部高位 Walsh 系数为零，矛盾。
因此 $u$ 的值域无限，非零多项式 $q$ 不会在其全部值域上消失，
所以 $f$ 是非零连续函数。
有限支撑情形则直接使用非零的实际有限柱符号；
如果该符号恰为零，当然不声称零向量循环。

R175 给
$$
r=\min\{n\in\mathbb N_0:q(u(n))\ne0\}<\infty,
$$
$$
\boxed{
\overline{P_{q(u),w}\mathcal A}^{\|\cdot\|}
=\overline{A^r\mathcal A}^{\|\cdot\|}=I_r.
}
\tag{2.2}
$$
并且对任意连续含幺表示 $\pi$，
$$
\ker\pi(P_{q(u),w})=\ker\pi(A)^r,\qquad
\overline{\operatorname{Ran}\pi(P_{q(u),w})}
=\overline{\operatorname{Ran}\pi(A)^r}.
\tag{2.3}
$$
原 Haar 表示的 $A^r$ 单射稠密，所以 $q(u)e^w$ 循环，
全部重数已经包含。

这与 Bell 构造是同一个算子：
有限柱逼近的真实乘子在范数收敛，
作用于循环向量 $e^w$ 后给 $q(u)e^w$；
R176 的 Bell 多项式也给这一像。
两个有界交换乘子在循环向量上相等，故全空间相等。

## 3. 直接核对 R179 的逐项解析表示

令
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad
s=a_*+\sum_ja_j.
$$
真实倾斜 first 满足
$$
X-sI
=\sum_j a_jN_j[-2t_j(I+t_jN_j)^{-1}].
\tag{3.1}
$$
每个方括号都是 $A$ 的真解析芽；
其解析半径可随 $j$ 变化，但范数一致有界。
$N_j=A^{2^j}/W_{2^j}$，指数 $2^j$ 互异。
(3.1) 的系数重排仍超三次，所以 $X-sI\in\mathcal T$。

对 $n\ge2$，写
$L_n(v)=(v-1)\widetilde L_n(v)$，则
$$
G_n=\sum_j a_j^nN_j
 [-2t_j(I+t_jN_j)^{-1}\widetilde L_n(R_j)].
\tag{3.2}
$$
方括号仍逐项真解析且一致有界；
$|a_j|^n$ 的重排超三次。
所以所有 $G_n\in\mathcal T$。
R179 的加乘封闭给任意 Bell 多项式 $T\in\mathcal T$，
再由其非零性得到 (2.2)。

这个核对说明超三次结论没有依赖物理系数按大小排序；
排序只用于真实表示中的系数重排假设。

## 4. $\alpha=3$ 的已有严格常数阈值

现在仅假设
$$
\rho_k\le B e^{-\beta k^3},\qquad \beta>0.
\tag{4.1}
$$
仍有 $f=q(u)$ 连续、非零，且
$d_k^*(f)\le C e^{-\beta k^3}$。
R159/R175 的振幅枚举增量为
$$
P_{m+1}-P_m=c_mN_{j_m}V_m,\qquad
c_m=K_w^m d_{j_m}(f),\qquad
\sup_m\|V_m\|<\infty,
\tag{4.2}
$$
每个 $V_m$ 真解析，指数 $2^{j_m}$ 互异。
虽然 R175 主定理使用超三次假设，
(4.2) 的逐项构造在本情形仍范数收敛，
因为 $\sum_m K_w^m e^{-\beta m^3}<\infty$。
其完整尾系数重排满足
$$
\Gamma(c):=\liminf_{\ell\to\infty}
 \frac{-\log c_\ell^*}{\ell^3}\ge\beta.
\tag{4.3}
$$
证明是先用任意 $\beta'<\beta$ 给
$|c_m|\le e^{-\beta'm^3}$ 的最终上界，
再删除有限枚举头，比较剩余上确界并令 $\beta'\uparrow\beta$。

令 $r=\min\{n:f(n)\ne0\}$；
真实形式整数值公式给 $\operatorname{ord}P_{f,w}=r$。
若 $r=0$，乘子本来就是单位。
若 $r\ge1$，已有以下两个充分条件。

第一，若
$$
\boxed{\beta>\frac{80}{3}r^4,}
\tag{4.4}
$$
选 $\gamma<\beta$ 和 $\varepsilon>0$，
使 $D=(1-\varepsilon)\gamma/4>100r^4/15$。
R179 (9.2)--(9.4) 的实际有界因子占据估计给，
在删除有限大系数并按整数指数切到足够远后，
$$
\tau_4(B_K)\ge
(A_K^{-1/3}+D^{-1/3})^{-3}>
\frac{100}{15}r^4.
$$
余下有限头是真解析，首阶恰为 $r$。
R140 定理4.1 因而给原乘子单射，
以及每个闭不变限制、每个有限放大限制上的稠密像和强主理想近似。

第二，若
$$
\boxed{\beta>400r^4,}
\tag{4.5}
$$
R118 的实际归一化幂与首单位因子条件成立；
用 R175 引理2.1 的同一有限头处理，
可得标准范数闭主理想 (2.2) 及普遍表示公式 (2.3)。

(4.4)--(4.5) 是已有证明的明确充分阈值，
不声称必要，也不把较弱阈值误用于标准范数理想。
一般正的 $\beta$ 没有自动满足这些与实际首阶 $r$ 相关的条件。

## 5. 对后续工作的界线

对于任意排序上界 $e^{-\beta k^\alpha}$，
若已经证明某个 Bell $T$ 有
$\|T^k\|\le K e^{-d k^{1+\min(\alpha,3)}}$，
则 $\alpha\ge3$ 只给一次四次型下界；
它本身不替代 §§1、3 的实际解析尾表示。

超三次 $\alpha>3$ 的全部重数已由旧定理关闭；
$\alpha=3$ 包含上述常数阈值特例。
若继续用高位反射研究混合重根，
真正尚需补的指数区间是 $1<\alpha\le3$ 的剩余范围，
并不是所有 $\alpha>1$ 都未处理。

普通 ISP、多模式一般慢符号和边界问题的完成状态不由本核查改变。
