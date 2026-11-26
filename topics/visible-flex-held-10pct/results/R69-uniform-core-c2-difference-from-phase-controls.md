# R69. 同一补弧族的完整核心 C² 差界

维护：Astra-held10-06bbeb39-20261126。2026-11-26 UTC。

本条把 R65/R68 的真实 phase 差转换成**包含闭合原函数和平移规范的完整核心位置、一阶及二阶导数差**。它可用于两个实际已接受场的核心比较；不是完整连接器、尾或闭面的 C² 界，更不能仅由有限两层差推出 Cauchy 性。

独立审阅：fixed_metric 核验闭合 Green 恒等式、两个系数的模、全扇区延拓与共同规范条件；其先前短证明的一阶/二阶界亦保留。

## 1. 必须相同的几何定义

取 $P=2\pi/3$、$\rho=e^{iP}$。两个核心使用同一个完整基准支撑向量、R53 同伦值 $\lambda$、窗口 $S,b$、相位基底及材料弧长坐标；全部常数是原来冻结的实数，频率里的 $\pi$ 是真实常数。有限控制向量严格补零嵌入同一序列空间，令

$$
\Phi_i(u)=\phi_*(u)+\sum_{j\ge1}d_{i,j}\Psi_j(u),\qquad
\kappa_i=\Phi_i',\qquad i=0,1.
$$

R65 使用 $\omega_j=3j$；R68 使用 $\omega_j=j\pi/(\pi/3-S)$。两者不能混为同一个基底。置

$$
E_0=\sum_j\frac{|d_{1,j}-d_{0,j}|}{\omega_j+D_1},\qquad
E_1=\sum_j|d_{1,j}-d_{0,j}|,\qquad
D_1=\frac{630}{256b}.
\tag{1}
$$

由 $|W|\le1$ 和 $\|\Psi_j'\|_\infty\le1$，

$$
\|\Phi_1-\Phi_0\|_\infty\le E_0,
\qquad \|\kappa_1-\kappa_0\|_\infty\le E_1.
\tag{2}
$$

也可使用更精确的已认证 $E_0,E_1$，只要仍满足 (2)。令

$$
\eta=\min(2,E_0),\qquad K_i\ge\|\kappa_i\|_\infty.
$$

$K_i$ 必须来自同一真实基准/控制的连续界；例如 $K_*+\sum_j|d_{i,j}|$ 是充分选择，其中 $K_*\ge\|\phi_*'\|_\infty$。不能把旧 M24 的曲率数值直接填给新的场。

## 2. 闭合原函数的有界线性算子

用复数表示核心所在平面。法向与单位切向分别为

$$
n_i=e^{i\Phi_i},\qquad T_i=i n_i.
$$

二者满足 $T_i(u+P)=\rho T_i(u)$。以三重旋转中心为同一个原点，真实闭合核心唯一写为

$$
J_i=\int_0^P T_i(v)\,dv,\qquad
\Gamma_i(0)=\frac{J_i}{\rho-1},\qquad
\Gamma_i(u)=\frac{J_i}{\rho-1}+\int_0^u T_i(v)\,dv.
\tag{3}
$$

确实，$\Gamma_i(P)=\rho\Gamma_i(0)$；按旋转延拓三次得到闭曲线。式 (3) 是真实积分定义，并未通过重新平移两场使位置差变小。原补弧族的反射对称还使该原点规范与原实现的实轴规范相同；有限浮点求积及取实部误差仍须由真核区间入口另行支付。

记 $C=(\rho-1)^{-1}$，$\Delta T=T_1-T_0$。从 (3) 得到比单独界原点和积分更直接的恒等式

$$
\Delta\Gamma(u)
=\rho C\int_0^u\Delta T(v)\,dv
 + C\int_u^P\Delta T(v)\,dv,
\qquad 0\le u\le P.
\tag{4}
$$

由于 $|C|=|\rho C|=1/\sqrt3$ 且
$|e^{ia}-e^{ib}|\le\min(2,|a-b|)$，有

$$
\boxed{\ \|\Gamma_1-\Gamma_0\|_\infty
\le \frac{P}{\sqrt3}\eta.\ }
\tag{5}
$$

旋转延拓保持范数，所以该界覆盖整个真实 $2\pi$ 周期，不只是一个扇区。

## 3. 完整一阶、二阶差

直接由 $\Gamma_i'=T_i$ 得

$$
\boxed{\ \|\Gamma_1'-\Gamma_0'\|_\infty\le\eta.\ }
\tag{6}
$$

再由 $\Gamma_i''=-\kappa_i n_i$，分别把两项写成
$-\Delta\kappa\,n_1-\kappa_0\Delta n$ 或
$-\Delta\kappa\,n_0-\kappa_1\Delta n$，取较小者，得到

$$
\boxed{\ \|\Gamma_1''-\Gamma_0''\|_\infty
\le E_1+\min(K_0,K_1)\eta.\ }
\tag{7}
$$

三式共同包含完整闭合原函数，没有丢掉零模位置差。若两场使用同一个固定 C² 重参数化 $u=\chi(x)$，链式法则给

$$
|\Delta(\Gamma\circ\chi)'|\le\eta|\chi'|,
$$

$$
|\Delta(\Gamma\circ\chi)''|
\le\bigl(E_1+\min(K_0,K_1)\eta\bigr)|\chi'|^2
  +\eta|\chi''|.
\tag{8}
$$

这允许在同一个冻结材料图下转换核心差；不能省掉整个前缀的未知 Fourier 场、真实 mean1168 原函数或尾场差。

## 4. 对精化序列的准确含义

若一个实际求得的同问题序列 $d^{(N)}$ 在 $\ell^1$ 中 Cauchy，完整基准和窗口始终相同，则 (1) 给 $E_0,E_1\to0$；其控制 $\ell^1$ 范数有统一界，所以上述 $K_i$ 也可统一选择。于是 (5)–(7) 证明这些核心在共同规范下是 C² Cauchy。R63/R68 预设的加权 $\ell^1_4$ 收敛当然更强。

实际精化比较器可以对 literal 二进制控制系数做精确有理差，并在真实 $\pi$ 的向外区间上计算 (1)。这不要求用采样最大值冒充连续相位界。**三份有限解、两次相邻差下降或一份小残差，均不自动证明上述整个序列的 Cauchy 假设。**

当前无新的实际 $\lambda=1$ 场或数值代入。本条只支付从同一真实 phase 控制到完整核心 C² 的解析比较环节；其余全场、全时几何、固定问题残差下降和 10% 完成条件继续保留。
