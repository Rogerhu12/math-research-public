# R236 附录：首偏离不晚于首主系数的二次循环性

日期：2026-11-13（UTC）。状态：已证明；一般 Hilbert ISP 未完成。
完整源稿见[有限 dyadic 差、核内单位与 Fourier 排核](../notes/2026-11-13-earliest-support-dyadic-quadratic-cyclicity-central-review.md)。

## 1. 定理与已关闭的范围

在原 Haar 加权 odometer 上，取任意复行 $a,b\in\ell^2$、
常数 $a_*,b_*\in\mathbb C$，以及非零 $c\in\ell^1$。写
$$
u=a_*+\sum_ja_j\chi_j,\qquad
w=b_*+\sum_jb_j\chi_j,\qquad
j_a=\min\{j:a_j\ne0\},\quad j_c=\min\{j:c_j\ne0\}.
$$
空主支撑时令 $j_a=+\infty$。

**定理。** 若 $j_c\le j_a$，则
$$
\boxed{\ 
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w
\quad\text{非零且对原 }A\text{ 循环。}\ }
\tag{1.1}
$$
不要求主行可和、相位对齐、排序尾率、共同圆周预解预算，
也不要求偏离和主系数逐位同阶。指数权允许任意复 $\ell^2$ 行。
$a_*=0$ 保留在定理内。

特别，只要首个非零主位已有非零偏离，便满足条件；
此前还可有任意偏离，后续偏离只须可和。若实 $\kappa>2$ 且
$$
0<|c_j|\le C|a_j|^\kappa\quad(a_j\ne0),\qquad
c_j=0\quad(a_j=0),
$$
则首支撑相同，且 $\ell^2\subset\ell^\kappa$ 保证 $c\in\ell^1$。
因此全部这种全行偏离已闭，不需要统一下界。
整数 $\kappa$ 包含 $c_j=\gamma a_j^\kappa$；
非整数仅比较绝对值，不引入多值复幂。

## 2. 实际闭实现和未知核

令
$$
R_j=V(e^{-2b_j}N_j),\qquad
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_ja_j^2(R_j-I)^2.
$$
两尾按算子范数绝对收敛，属于单字符代数 $\mathcal A$ 的根式。
用 R176 的实际倾斜 first $X=X_b$ 定义
$$
T=X^2+Y-B,\qquad \operatorname{Dom}T=\operatorname{Dom}X^2.
\tag{2.1}
$$
R176 §§2–5、10 给准确自然域上的闭性、完整 $C$ 自伴性，
并给循环图核心 $\mathbb C[A]e^w$。实际 Bell 恒等式为
$$
X^2e^w=\left[u^2-\sum_ja_j^2(I-R_j^2)\right]e^w,
$$
故 $Te^w$ 正是 (1.1)，且
$$
[Te^w]_A=\overline{\operatorname{Ran}T}.
\tag{2.2}
$$
若主行为空，直接取全域有界 $X=a_*I$，上述域事实直接成立。

反设 $M=\ker T\ne0$。R176 §8 给
$$
M\subset\bigcap_p\operatorname{Dom}X^p,\qquad
X_M=X|_M\in B(M),\qquad X_M^2=(B-Y)|_M.
\tag{2.3}
$$
$B-Y$ 的字符为零；限制幂范数不增，故 $X_M$ 拟幂零。
每个 $F\in\mathcal A$ 保持 $M$ 并与 $X_M$ 交换，因此
$$
r(F_MX_M)=0,\qquad I_M+F_MX_M\text{ 在 }M\text{ 上可逆}.
\tag{2.4}
$$
这里没有从全空间 $X$ 的谱推断限制的谱。

## 3. 每个非例外 dyadic 差的真解析因子

设 $\Gamma$ 为全部 dyadic 根，$U_\zeta v(y)=\zeta^yv(y)$，
$\gamma_\zeta S=U_\zeta S U_\zeta^*$。
对于 $\zeta^{2^h}=1$，R176 §9 支付全部自然幂域，且
$$
\gamma_\zeta X=X+D_\zeta,\quad
D_\zeta=\sum_{j<h}a_j
 [V(e^{-2b_j}\zeta^{2^j}N_j)-V(e^{-2b_j}N_j)].
\tag{3.1}
$$
$D_\zeta,\Delta_\zeta Y,\Delta_\zeta B$ 都是真正解析有限头。
在同一个 $\operatorname{Dom}X^2$ 上准确有
$$
\gamma_\zeta T-T=2D_\zeta X+E_\zeta,\qquad
E_\zeta=D_\zeta^2+\Delta_\zeta Y-\Delta_\zeta B.
\tag{3.2}
$$

置 $m=2^{j_c}$，固定 $\zeta^m\ne1$。
$\Delta_\zeta Y$ 的精确首阶是 $m$，首系数
$$
-\frac{2c_{j_c}e^{-2b_{j_c}}}{d_{j_c}}(\zeta^m-1)\ne0.
$$
由 $j_c\le j_a$，
$$
\operatorname{ord}D_\zeta\ge2^{j_a}\ge m,\qquad
\operatorname{ord}(D_\zeta^2),\
\operatorname{ord}\Delta_\zeta B\ge2^{j_a+1}>m.
$$
主行为空时后两项准确为零。因此存在实际收敛的解析芽
$$
E_\zeta=A^m e_{\zeta,0}(A),\quad e_{\zeta,0}(0)\ne0,
\qquad D_\zeta=A^m d_{\zeta,0}(A).
$$
合法定义
$$
F_\zeta=
\left(\frac{2d_{\zeta,0}}{e_{\zeta,0}}\right)(A)\in\mathcal A,
$$
便得真正域恒等式
$$
\boxed{\ \gamma_\zeta T-T
=E_\zeta(I+F_\zeta X).\ }
\tag{3.3}
$$
这是两个实际解析芽的可去因子，未取 $E_\zeta^{-1}$，
也未把慢算子的形式除以 $A^m$ 当成有界除法。

R151 §3.1 对真解析 $E_\zeta$ 给每个未知不变限制上的
$\overline{E_\zeta M}=M$。结合核内单位 (2.4)，
$$
(\gamma_\zeta T-T)M=E_\zeta M,\qquad
\boxed{\overline{(\gamma_\zeta T-T)M}=M.}
\tag{3.4}
$$
逆和解析邻域都可依赖固定 $\zeta$，无一致性要求。

## 4. 完整 C 配对与有限维矛盾

$\gamma_\zeta T$ 仍是有界交换系数的首一自然二次式，
故完整 $C$ 自伴，且
$$
U_\zeta M=\ker\gamma_\zeta T\subset\operatorname{Dom}X^2.
$$
使用
$$
\mathcal B(v,z)=\int v(y)z(-1-y)\,d\mu(y),
$$
对 $v\in M,z\in U_\zeta M$ 得
$$
\mathcal B((\gamma_\zeta T-T)v,z)
=\mathcal B(v,\gamma_\zeta Tz)=0.
$$
(3.4) 的左端稠密性于是给
$$
\mathcal B(M,U_\zeta M)=0\qquad(\zeta\notin\mu_m).
\tag{4.1}
$$
未假设 $CM=M$，也未把原空间 $C$ 自伴性传给限制。

对任意 $v,z\in M$，函数 $v(y)z(-1-y)$ 属于 $L^1$。
由
$$
\mathcal B(v,U_\zeta z)
=\zeta^{-1}\int v(y)z(-1-y)\zeta^{-y}\,d\mu(y),
$$
其 Fourier 支撑包含于有限群 $\mu_m$。
Haar 柱条件期望的 $L^1$ 收敛说明：该乘积在每个模 $m$ 柱上为常数。

取 $M$ 的可数稠密族，其总本质支撑 $E$ 因 $AM\subset M$、
原权几乎处处严格为正而满足 $E+1\subset E$ 模零测集。
测度不变性和 odometer 遍历性给 $\mu(E)=1$。
在每个模 $m$ 柱 $C_r$ 上，可选稠密族中的 $v_r,z_r$，
使 $v_r(y)z_r(-1-y)$ 在正测集非零；它既是柱常数，
便在整柱几乎处处等于某个 $k_r\ne0$。

任意 $v\in M$ 的 $v(y)z_r(-1-y)$ 也为柱常数，
故 $v|_{C_r}$ 必是 $v_r|_{C_r}$ 的标量倍数。
共 $m$ 个柱得到 $\dim M\le m$。
但 $A|_M$ 同时单射且拟幂零，在非零有限维空间上不可能。
因此 $M=0$，完整 $C$ 自伴性和 (2.2) 完成 (1.1)。

## 5. 新例及真正保留的缺口

对
$$
a_j=(-1)^j(j+1)^{-\sigma},\quad \tfrac12<\sigma<1,\qquad
c_j=\beta |a_j|^\kappa\omega_j,\quad |\omega_j|=1,\quad\beta\ne0,
$$
主 first 按 R138 属全平面连续谱，辅助为全支撑慢幂。
即使旧共同圆周预算指数
$2\sigma(\kappa-1)/(\kappa\sigma-1)>2$，本定理仍直接闭合。
这是有限最低阶机制，无需修复旧预解预算。

若首偏离更晚，即 $j_c>j_a$，则对移动首主位的 $\zeta$，
仍可写
$$
\gamma_\zeta T-T=2D_\zeta(X+K_\zeta),\qquad K_\zeta(0)=0,
$$
但 $X_M+(K_\zeta)_M$ 只知拟幂零，不能据此取得可逆或稠密像。
R270C/D 未证明该未知限制密度；全空间循环 iff 也不是逐向量循环空间相等。

因此例如 $a_0\ne0,c_0=0$、其余位全纯 $\kappa$ 偏离的慢幂情形，
仍需独立机制。此前真实预解、稀疏支撑和固定盘核内逆准则
在首偏离较晚时保有独立范围。
本定理不处理任意向量、任意两个独立慢方向或一般普通不变格。
