# R119 续篇：高振荡控制的真实小振幅 Hessian 与统一近共振阈值

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 第56束紧支方向除了 $C^4$ 范数有界，还具有真实
振幅和前三阶导数的小尺度。把这些尺度保留到完整两 phase 补偿及两次
Duhamel 后，同一 dyadic 频带的真实 Wronskian Hessian 变成
$$
 \|D^2\mathscr W_M\|_{\ell^1\times\ell^1}
 <2^{36}K_j^2M\rho^5\Delta^{-3}
       +2^8K_j^3M^2\rho^8 .
 \tag{B.1}
$$
其中 $\rho=2^{-72}/(aM_0\sqrt B)$、$M_0\le M\le2M_0$。
完整补偿项在第一项中，没有因其一阶在原点为0而删除。
近共振径向行的可用阈值随之成为
$2^{-1770}K_j^{-6}B^{-1}$，不再随当前 $M$ 缩小。

该结论仍关于真实径向、固定两端 unit Robin 行。
非径向中矩阵、更新后完整 source Green 和 $\mathcal F_c=0$ 没有据此闭合。

## 1. 同一新对象及方向族的实际范数

使用[高振荡控制](R119-supplement-high-oscillation-polynomial-phase-preserving-control.md)
的同一 $a,\Delta,B=\Delta/a,K_j$ 和原 fixed wave 端口。
给定有限频带
$$
 M_0\le M\le2M_0,\qquad \sqrt B/M_0\le2^{-512}.
$$
每个方向 $\psi_\nu$ 都由该篇在一个尚未占用的真实 quartic 区间
构造，对应频率 $M_\nu\in[M_0,2M_0]$。
其支集半径为
$$
 \rho_\nu=\frac{2^{-72}}{aM_\nu\sqrt B},
 \quad \rho/2\le\rho_\nu\le\rho,\quad
 \rho=\frac{2^{-72}}{aM_0\sqrt B}.
 \tag{B.2}
$$
各自原支集宽度门须成立；方向的支集彼此允许重叠。
第56束的逐 Leibniz 证明实际上给出更强的完整账
$$
 \|\psi_\nu^{(l)}\|_\infty\le\rho_\nu^{4-l},\qquad
 \|\psi_\nu^{(l)}\|_{L^1_x}\le2\rho_\nu^{5-l},
 \quad 0\le l\le4 .
 \tag{B.3}
$$
因此对 $\Psi_v=\sum v_\nu\psi_\nu$，
右侧分别可换成 $\rho^{4-l}\|v\|_1$ 和
$2\rho^{5-l}\|v\|_1$。乘积所需的是
$$
 \int|\Psi_v^{(k)}\Psi_w^{(l)}|dx
          \le2\rho^{9-k-l}\|v\|_1\|w\|_1 .
 \tag{B.4}
$$
没有把频带内的方向数乘到这些 $\ell^1$ operator 范数上。

原已选形状 $\Xi_0$ 支持于这些新区间之外，
$\|\Xi_0\|_{C^4}<2^{-65}$。
新参数满足 $t=\|\varepsilon\|_1<2^{-65}$。
于是 $\Xi_0+\sum\varepsilon_\nu\psi_\nu$ 始终在第54束
真实 $2^{-64}$ 球内，全部原参数盒、$K_j$ 和全标签合同仍适用。
每个 $\psi_\nu$ 精确消去原两 phase 线性行。
支集分离保证在当前 $\Xi_0$ 处同样准确消去，不把原点结论免费沿用。

## 2. 真实两 phase 二阶小量

沿新区间写 $u=F-\Delta^{-1}\Psi_\varepsilon'$。
完整 phase 泛函仍是第54束 (H.7)，当前复盒内
$|u|>3/2,|u|<2,|u_x|<7$。
令 $d=\Delta^{-1}$。从该篇的准确二阶公式及 (B.4) 得
$$
 |D^2\mathsf C_1[v,w]|
 \le d\rho^7\|v\|_1\|w\|_1 ,
$$
$$
 |D^2\mathsf C_2[v,w]|
 \le\left\{\frac d8\rho^7+
 \frac{d^3}{64}
       \left(4\rho^5+140\rho^6+\frac{1715}{2}\rho^7\right)\right\}
          \|v\|_1\|w\|_1 .
 \tag{B.5}
$$
这里两个 $\psi''$ 项和完整 $u_x$ 项都保留。
由于 $\rho\Delta=2^{-72}\sqrt B/M_0\le2^{-584}$，
两行统一满足
$$
       \|D^2\mathsf C\|<2^5\rho^5\Delta^{-3}.
 \tag{B.6}
$$
$\mathsf C'(0)=0$，故整条参数球上
$\|D\mathsf C(\varepsilon)\|<
2^5t\rho^5\Delta^{-3}$。

用当前真实 $(D\mathsf F)^{-1}<2^{10}$ 和
$D^2\mathsf F<2^{34}$，完整隐函数式给实际补偿增量 $\eta$：
$$
 \|\eta\|<2^{14}t^2\rho^5\Delta^{-3},\qquad
 \|D\eta\|<2^{15}t\rho^5\Delta^{-3},
$$
$$
 \boxed{\quad \|D^2\eta\|<2^{16}\rho^5\Delta^{-3}.\quad}
 \tag{B.7}
$$
二阶式包含
$-(D\mathsf F)^{-1}D^2\mathsf F[D\eta,D\eta]$；
其费用至多
$2^{74}t^2\rho^{10}\Delta^{-6}$，小于第一项的余量。
这正是 $M^{-4}$ Hessian 项的来源，不能假称补偿在全参数球都没有导数。

## 3. 完整实际生成矩阵的一、二阶费

继续使用原 density wave 变量
$$
 Y_t=\mathsf A_MY,\quad
 \mathsf A_M=
 \begin{pmatrix}0&k\\
 -[M^2Q+Q_t/2-(1+Q)^2/4]/k&0
 \end{pmatrix},\qquad k=\sqrt{7M^2-16}.
$$
其两个端点变换固定。
完整一阶 log-profile 是
$\theta_v=\Psi_v+\sum_sD\eta_s[v]\,b_s$；
二阶是 $\theta_{vw}=\sum_sD^2\eta_s[v,w]\,b_s$。
原两个补偿 bump 的 $C_x^2$ 总费可取 $2^{18}$。
由 (B.3)、(B.7)，对单位 $\ell^1$ 方向可同时使用
$$
 \|\theta_v\|_\infty<2\rho^4,\quad
 \|\partial_x\theta_v\|_\infty<2\rho^3,\quad
 \|\partial_x\theta_v\|_{L^1}<3\rho^4,
$$
$$
 \|\theta_{vw}\|_{C_x^2}
                         <2^{34}\rho^5\Delta^{-3}.
 \tag{B.8}
$$
这些是包含远处两 bump 的完整 profile 范数。

准确下左一阶行是
$$
 D\mathsf A_M[v]_{21}
 =\frac{(M^2-(1+Q)/2)(\theta_v)_t
                         +(\theta_v)_{tt}/2}{k}.
$$
新区间的直接部分满足
$$
 \int\|D\mathsf A_M[\Psi_v]\|dt
 <2M\rho^4+\frac{\rho^3}{2Ma}<3M\rho^4 .
$$
最后一步使用真实
$M^2a\rho\ge2^{-72}M_0/\sqrt B\ge2^{440}$。
补偿部分的积分小于
$2^{34}Mt\rho^5\Delta^{-3}<M\rho^4$。
所以可安全统一取
$$
                  \int\|D\mathsf A_M[v]\|dt<8M\rho^4 .
 \tag{B.9}
$$

二阶包含 $\theta_{vw}$ 的完整线性项和
$(\theta_v)_t(\theta_w)_t/(2k)$。
前者的积分至多 $2^{35}M\rho^5\Delta^{-3}$；
后者由 (B.8) 的真实 sup–$L^1$ 乘积及 $dt=a\,dx$ 给
$$
 \frac1{4Ma}\int|\partial_x\theta_v\partial_x\theta_w|dx
 \le\frac{3\rho^7}{2Ma}<2M\rho^8 .
$$
因此
$$
 \int\|D^2\mathsf A_M[v,w]\|dt
 <2^{35}M\rho^5\Delta^{-3}+2M\rho^8 .                   \tag{B.10}
$$

## 4. 两次有序 Duhamel 与有限步长

原真实每个中间 propagator 都由 $K_j$ 控制。
一次和两次 Duhamel 的完整次序给
$$
 \|DC_M\|_{\ell^1\to{\rm Mat}_2}<8K_j^2M\rho^4 ,
$$
$$
 \|D^2C_M\|
 \le K_j^2\left(2^{35}M\rho^5\Delta^{-3}+2M\rho^8\right)
       +2K_j^3(8M\rho^4)^2 ,
$$
从而得到 (B.1)。
没有交换两个有序积分，也没有只保最后一个 fundamental solution。
固定真实左右 unit 线的 Wronskian 有相同界。

对目标模式 $M=M_\nu$，第56束真实导数下界满足
$$
 L_M=2^{-2048}K_j^{-3}a^{-1}\Delta^{-3}M^{-3}
 \ge \underline L_M:=
       2^{-1764}K_j^{-3}M\rho^4/B .
 \tag{B.11}
$$
这里 $\rho_\nu\ge\rho/2$ 的四次费16完整保留。
所以沿任何完整参数位移 $\|\delta\varepsilon\|_1\le R$，
导数改变相对 $\underline L_M$ 的比例小于
$$
 R\left(2^{1800}K_j^5B\rho\Delta^{-3}
             +2^{1773}K_j^6BM_0\rho^4\right).
$$
令
$$
 R\le\min\left\{r_{\rm free},\
 2^{-1804}K_j^{-5}B^{-1}\Delta^3\rho^{-1},\
 2^{-1777}K_j^{-6}B^{-1}M_0^{-1}\rho^{-4}\right\}.
 \tag{B.12}
$$
则总改动小于 $\underline L_M/8$，原方向和其
$L_M/2$ 下界保持。$r_{\rm free}$ 包括原完整参数球的实际余量。
在固定层的同一高频尺度上，后两个允许半径分别按 $M_0$ 与 $M_0^3$
增长；没有先用单位 $C^4$ 粗 Hessian 把它们变成随频率急缩的半径。

## 5. 频率一致的真实近共振阈值

当前径向 $C_M$ 的 true unit 左右行固定，但允许
$\mathscr W_M\ne0$。
把右线投影到 $C_Ml$ 的方向，误差不超过
$2K_j|\mathscr W_M|$。
由 (B.9)，其对任一完整 band 方向的 Wr 导数误差不超过
$$
              16K_j^3M\rho^4|\mathscr W_M|.
$$
因此若
$$
 \boxed{\quad
 |\mathscr W_M|\le2^{-1770}K_j^{-6}B^{-1},
 \quad}                                                   \tag{B.13}
$$
对投影共振线生成的第56束方向仍对原真实行给导数至少 $L_M/2$。
投影的取向合法：右侧乘 $K_j$ 严格小于1，故当前两条单位线有唯一
近的连续取向。
(B.13) 在同一层的高频带内不含额外 $M$ 逆幂。
它是 scalar radial 行的阈值，不能仅据此把一个 nonradial kernel
向量当作单个 Fourier 模。

## 6. 完整 mean 与源变化仍存在

(B.8) 还给当前控制窗真实 mean 电阻
$\mathcal R_0=\int\mu^{-1}dt$ 的方向界
$$
 |D\mathcal R_0|<2\rho^4\mathcal R_0,\qquad
 |D^2\mathcal R_0|
 <(4\rho^8+2^{34}\rho^5\Delta^{-3})\mathcal R_0 .
 \tag{B.14}
$$
它们来自
$D(\mu^{-1})=-\theta\mu^{-1}$、
$D^2(\mu^{-1})=(\theta_v\theta_w-\theta_{vw})\mu^{-1}$。
没有把独立 mean flux 或唯一高度 $\lambda$ 清零。

固定材料源时，canonical weak 第一行中的 $p^{-1}F^t$
具有相同一阶及二阶乘法因子。
若固定的是物理 ordinary $e$，真实 $f=w^2e$ 的变化另给
$$
 |f_v|\le4\rho^4|f|,\qquad
 |f_{vw}|\le(16\rho^8+2^{35}\rho^5\Delta^{-3})|f| .
$$
全部 metric-source、两个 weak 分量和 total/bare 端迹之差仍按第54束
完整公式输入。有源 propagated 列必须保留其自身源导数及全部有序
Duhamel 项；(B.1) 不是任意 source 空间的自动估计。

真实正型跨段 off-diagonal、两端 height/flux frame、外停止及全局
regular 行的参数导数亦未被删除。本篇的 fixed-port 假设只用于
确实固定的当前窗口两侧行；若改用会随第四停止而动的全局行，
必须把该依赖逐项加入。

[严格预算程序](../scripts/fourfold_high_oscillation_small_amplitude_Hessian_20261114.js)
及[实际执行记录](../notes/2026-11-14-R119-high-oscillation-small-amplitude-Hessian-budget.json)
是新纯 V8/BigInt 实算，记录全补偿二阶、完整两次 Duhamel、近共振和
mean/source 的全部显示门。它不宣称已有非径向中矩阵逆。
