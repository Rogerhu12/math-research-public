# R858 执行引理：原41单Z的加法链、规范球与完整尾界

状态：**本文公式及有限精度算法已证明；原41数值尚待真实 R854 响应。** 2026-11-16，serre-public-astra-20261115。本文只将既成 SP、ZA、41S 和 R852 接到一个实际消费者；不重新计算旧除法函数、Hom 矩阵、五C秩或原 U.1。

## 1. 输入必须是同一原对象

沿用 [41S](2026-11-16-original-41-adic-field-good-model-and-sigma-input.md) 的唯一原局部域
$$
L_{41}=\mathbf Q_{41}(B,s),\qquad s^2=-3,\qquad
B=\lambda b,\quad\lambda=2^6 3^{180},\quad v_B=7v_{41}.
\tag{R858.1}
$$
其原 Eisenstein 多项式、$\lambda$、$\zeta=(s-1)/2$ 与十四坐标顺序完全读取原来源，不新选另一个域嵌入或平方根。$L_{41}/\mathbf Q_{41}$ 的分歧指数为7、剩余次数为2，$\mathbf Z_{41}$ 整基为 $1,\ldots,B^6,s,\ldots,sB^6$。

首次输入为 R854 真正成功的四响应 $A_0,A_1,B_0,B_1$，含原单位子式/左逆下界与全部原2560行残差证书。R854 的每个值按
$$
\frac{\text{numerator}}{B^\delta41^h}
 +O(B^{N_{\rm response}})
\tag{R858.2}
$$
解释；最后的绝对球精度已扣分母、泛函和逆界，不能替换为 numerator 的存储精度，也不再施原 integer_scale。输入精度不足时提高同一原响应的精度；不能移用辅助素数518位或未经接受的短 A.1 候选。

原点 $P=f(c_1)$ 使用 R852 程序的 beta_C_x、beta_C_y 两根，不是三同源后 f_R 根。线性响应叶消费 (R858.2)，原 unit_chart_solve 不重做；其余常量与 $\sigma$ 作用均沿原精确 DAG。五个 $C_j$ 直接用 R852 已成的原十四有理坐标；$D_j$ 使用同一原 secant/Hom 源。原非挠性、代数分母非零依据直接引用 R843/R844 和 R852 闭包，但数值除法仍须有实际球精度。

## 2. 用七次点运算恢复原单Z

[ZA §4](2026-11-16-original-three-isogeny-sigma-and-one-Z-period-contraction.md) 已在原规范证明
$$
\mathcal Z(P+Q)=\mathcal Z(P)+\mathcal Z(Q)
 +\frac{y_Q-y_P}{x_Q-x_P}.
\tag{R858.3}
$$
倍点的斜率为 $3x_P^2/(2y_P)$。这里是原 $y^2=x^3+b$、$\omega=dx/(2y)$ 及 SP 的正号；不换微分或第二类补空间。

定义 $\beta_n$ 为
$$
\mathcal Z([n]P)=n\mathcal Z(P)+\beta_n,\qquad\beta_1=0.
$$
对所需的非挠点直接递推
$$
\begin{aligned}
\beta_{2n}&=2\beta_n+\frac{3x([n]P)^2}{2y([n]P)},\\
\beta_{n+1}&=\beta_n+\frac{y(P)-y([n]P)}{x(P)-x([n]P)}.
\end{aligned}
\tag{R858.4}
$$
只用链
$$
1,\ 2,\ 4,\ 5,\ 10,\ 20,\ 21,\ 42.
\tag{R858.5}
$$
这是七次新的点加法/倍点。对其中 $n=4,20$ 的加 $P$ 步，$x([n]P)=x(P)$ 会迫 $(n-1)P=0$ 或 $(n+1)P=0$；倍点分母零会迫 $2nP=0$。原非挠性排除这些情况，但不能预填它们的41赋值。

由 (R858.3) 逐步归纳，所得 $\beta_{42}$ 是同一原规范的真值，因而
$$
\boxed{\mathcal Z(P)=
 \frac{\mathcal Z([42]P)-\beta_{42}}{42}.}
\tag{R858.6}
$$
42是41单位。与 SP.22 比较可得
$D_\omega\log\psi_{42}(P)=42\beta_{42}$；所以本链准确实现同一规范，不会增加一个未记录的 $\psi_2$ 符号、积分常数或相位。此等式只作规范识别，不再生成一个独立 $\psi_{42}$ 自动微分计算。

## 3. 形式值及一次认证全部尾项

令 $Q=[42]P$，在原方程上取
$$
t=-x(Q)/y(Q),\qquad u=t^2x(Q),\qquad A=bt^6.
$$
41S 已证明该倍率送原点到适用形式盘。实际数值消费者仍必须从球同时认证
$$
v_B(A)>0,\qquad v_B(u-1)>0.
\tag{R858.7}
$$
前者单独不能选定 $u^2(1-u)=A$ 的 $u(0)=1$ 分支。

由 SP.9–11，
$$
\mathcal Z(Q)=\frac{3u-2}{t}
 +\sum_{n\ge1}\frac{H_n b^n t^{6n-1}}{6n-1},
\quad
H_n=[A^{n-1}]
 \frac{9u(A)+4}{u(A)^2(3u(A)-2)}\in\mathbf Z.
\tag{R858.8}
$$
有理项直接使用实际 $u$，无另一截断误差。系数下标为 $n-1$，因为 SP 的 $H(t)=bt^4\sum_{n\ge1}H_nA^{n-1}$。

若 $\delta=1-u$，则 $\delta=A/(1-\delta)^2$；Lagrange 系数公式给
$$
[A^n]\delta=\frac1n\binom{3n-2}{n-1}.
\tag{R858.9}
$$
其整性也由整隐函数递推直接得到。$u(0)=1$，上述所有倒数的常数项都是1，故 (R858.8) 的 $H_n$ 都是整数。消费者只生成本次所需的有限前缀，已成系数和部分和原子保留。

**全尾引理。** 取已认证的整数下界 $a\ge1$ 满足 $v_B(A)\ge a$，并令 $c=v_B(t)$。给定目标绝对 $B$ 精度 $T$，选 $N\ge2$，置
$$
L=\min\{\ell\ge0:41^\ell\ge6(N+1)-1\}.
$$
只要
$$
(N+1)a-c-7L\ \ge T,
\tag{R858.10}
$$
则 (R858.8) 中全部 $n>N$ 项及其收敛总和都属于 $B^T\mathcal O_{L_{41}}$。

证明。SP.27 给每项下界
$$
na-c-7v_{41}(6n-1)
 \ \ge\ g(n):=na-c-7\log_{41}(6n-1).
$$
对实数 $x\ge3$，
$$
g'(x)=a-\frac{42}{(6x-1)\log41}
 >1-\frac{14}{17}>0,
$$
使用 $\log41>3$；例如 $e<3$ 即给 $e^3<27<41$。因此所有 $n\ge N+1\ge3$ 满足
$g(n)\ge g(N+1)\ge(N+1)a-c-7L\ge T$。
又该下界随 $n$ 趋于无穷，级数收敛。完备 DVR 的 $B^T$ 理想闭合，所以整个尾项同样在该理想内。证明完成。

整数 $L$ 只需逐次整数乘41，(R858.10) 总能在有限 $N$ 达到；不依赖浮点对数，也不只检查最后一个可见项。若使用更保守的正下界 $a$，引理仍有效。截断后的球精度还须同时受实际输入、所有除法及有限和误差限制；全尾界不提高原响应精度。

## 4. 原Eisenstein基上的规范球

令原 $B$ 的多项式为 $f(X)=X^7+\sum_{i<7}f_iX^i$。41S 已证 $41\mid f_i$ 且 $v_{41}(f_0)=1$。因此
$$
\gamma=\frac{B^7}{41}
 =-\sum_{i<7}\frac{f_i}{41}B^i
\tag{R858.11}
$$
是整单位。规范球写为
$$
B^v U+O(B^{v+R}),\qquad U\in\mathcal O^\times,\quad R>0;
\tag{R858.12}
$$
零中心球单独记 $O(B^M)$，只给下界，不假装知道实际值为零。

任意原十四坐标有理常量的非零系数可写为 $c_i=41^{k_i}a_i$，其中 $a_i$ 是41单位。准确恒等式
$$
c_iB^i=B^{7k_i+i}a_i\gamma^{-k_i}
\tag{R858.13}
$$
也适用于负 $k_i$，$s$ 块另乘 $s$。其准确最小赋值是两块全部 $7k_i+i$ 的最小值：不同 $i$ 的值模7不同；同一个 $i$ 上 $1,s$ 在 $\mathbf F_{41^2}$ 中线性独立，首项不可能互消。因此提出 $B^v$ 后只需计算仍低于所求精度的整单位项。原 $b,\zeta$ 坐标先按 (R858.1) 转到这个基，所有转化是原域内的准确等式。

在整球绝对精度 $M$ 下，第 $B^i$ 坐标只确定到
$41^{\max(0,\lceil(M-i)/7\rceil)}$。这来自赋值的同一最小值公式，不能把全部十四坐标错标成相同的 $B$ 位数。

整单位求逆可以先在
$\mathbf F_{41^2}[B]/(B^7)$ 中求逆：常数项非零，先逆该常数，再取至 $B^6$ 的有限几何和。随后用
$X\mapsto X(2-UX)$ 提升；误差恒等式
$1-U X_{\rm new}=(1-UX)^2$
证明每层精度至少加倍。已知单位中心的任何允许整提升都给同一所求球；每层乘回只用于实际算法本身，不把未确定的高坐标当真来源。

在 (R858.12) 中，两单位球相乘的相对精度是二者较小值；求逆得到
$B^{-v}U^{-1}+O(B^{-v+R})$。
加法先取双方绝对精度的较小值，再移到共同最低 $B$ 次，最后按实际抵消归一化。分母球包含零时只有 NeedPrecision，原代数非零证明本身不能替代实际赋值。所有结果的标签必须使用传播后的绝对精度。

原 R791 的 $\sigma(b)$ 给 $\sigma(B)=B\eta$，$\eta$ 为单位；唯一41位使 $\sigma$ 等距。对 (R858.12) 作
$$
\sigma(B^vU)=B^v\eta^v\sigma(U)
\tag{R858.14}
$$
保持绝对精度，即使 $v<0$。$\sigma$ 真正作用于整个求值，含四响应，不能只替换常量叶。原复共轭为 $B\mapsto B,s\mapsto-s$，同样等距。有限代表变换后最多保留输入的已证球精度，不能从新的坐标形式增造精度。

## 5. 原五行与保留的高度缺口

R852 已成原五个 $C_j$ 坐标和 $D_j$ DAG；ZA 给原椭圆部分的一次行
$$
3\left(B_{g_j}-\frac{p_j}{q_j}B_f\right)
 =7\,\operatorname{tr}_{\chi,L}(C_j\mathcal Z(P)+D_j)
 =\frac{c_\chi}{2}\operatorname{Tr}_{L_{41}/\mathbf Q_{41}}
      (C_j\mathcal Z(P)+D_j).
\tag{R858.15}
$$
因此只需一次 (R858.6)，不独立求七个 $\mathcal Z$。十四次迹可用
$(1+\mathrm{conj})\sum_{k=0}^6\sigma^k$ 计算；原 $c_\chi$ 保留为命名标量。不能把42阶/84次好约化扩域的 trace 再带入这里多乘6，也不能删去原外层7。

实际输出应为原 $\mathcal Z(P)$ 球和 (R858.15) 中 $c_\chi$ 的五个系数球，逐一保实际精度、非零状态及所用尾界。输入不足或节点分母不可分辨时保留已成阶段并报告真实原因，不能把它当 A.1 拒绝、原点不存在或高度为零。

这些仍是原椭圆周期行。原 [YP](2026-11-16-original-Y-RR-connections-and-Hecke-period-row.md) 的同一个 $Y$、$\ell$、刚性化、真 Hecke 算子及完整非 $p$ 行全部保留；R852 的五 $C$ 秩5也不证明指定高度非零。全部新数值只由本公开仓库 Actions 完成，机器数据不入 Git/Release。

## 6. 已成来源

- [SP 原sigma和周期输入](2026-11-16-original-CM-sigma-and-Poincare-period-inputs.md)，a06a80ea0d857520a9dbbd1bd18f75cce147403b812a9752e0760703ed1e16f9，尤其 SP.9–11、22、26–28。
- [ZA 原三同源及单Z收缩](2026-11-16-original-three-isogeny-sigma-and-one-Z-period-contraction.md)，268fa3fbb9647d7f6f3f781534d9425e09c45ad7945e9aea9a9abd2082834d97。
- [41S 原局部域与好模型](2026-11-16-original-41-adic-field-good-model-and-sigma-input.md)，133d64af94c4dba1262ce240e3ac23db5d1c24158f922cf3ba6419fa855af1eb。
- [41C 原输入契约](2026-11-16-original-41-single-Z-consumer-source-contract.md)，569aa684267e4c4ae76581ce6ad6c6b4fd2ad62b45869ed87809a4c22151eeee。
- [R852 实际五C和DAG](../results/R852-certified-original-five-one-Z-coefficients-and-constant-DAG.md)，run43801628875，真实程序839节点，原C坐标和D源不重算。
- [R854 原四响应方法](R854-original-41-cleared-row-saturation-and-four-responses.md) 及其 [几何整化](R854-original-41-geometric-row-scaling.md)：本文只能消费真实成功球，不预填未来 artifact 或精度。
