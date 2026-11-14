# R134 附录：正第一阶的实际计数半群界与有限阶整预解

日期：2026-11-13（UTC）。kernel_resume_1cf / Astra-ISP-1cf8c51d；根独立核验局部严格收缩、有限集合半群分解、全平面实际逆及增长阶。
状态：已证明。完整实际定量引理；用于实 β4 剩余支的二次正性／半条带接口。
已有空谱和真实域底座见 [R134](R134-empty-spectrum-first-chaos-polynomial-cyclicity.md)。
本稿不单独宣称该剩余核已为零。

## 1. 设置和结论

令
$$
X=X_{\sum_{j\ge0}a_j\chi_j},\qquad a_j\ge0,\quad
a\in\ell^2\setminus\ell^1.
$$
按 R128，$X$ 是原 Haar 模型的最大增生闭第一阶，
且有界预解属于 $A'$；R134 已给 $\sigma(X)=\varnothing$。
写 $S(t)=e^{-tX}$ 为其真实收缩半群。

定义有限计数和
$$
\Theta_a(t)=\sum_{j\ge0}\lfloor t a_j\rfloor,\qquad t\ge0.
\tag{1.1}
$$
因为 $a_j\to0$，对每个固定 $t$ 只有有限个非零项。
令 $\rho=9/10$、$c_0=-\log\rho>0$。
则
$$
\boxed{\|S(t)\|\le \rho^{\Theta_a(t)}
=\exp[-c_0\Theta_a(t)].}
\tag{1.2}
$$
这是实际算子范数估计，含全部 carry，并不先把整条主行换成纯张量模型。

特别
$$
\Theta_a(t)/t\longrightarrow\infty,
\tag{1.3}
$$
所以半群比每个固定指数更快衰减。
若对某个 $p>1$、$c>0$ 和充分大 $t$ 有
$$
\Theta_a(t)\ge ct^p,
\tag{1.4}
$$
则对 $q=p/(p-1)$ 存在有限常数 $C_1,C_2$，使
$$
\boxed{
\|(X-z)^{-1}\|
\le C_1\exp\!\left[C_2(\operatorname{Re}z)_+^q\right]
\le C_1e^{C_2|z|^q}\qquad(z\in\mathbb C).
}
\tag{1.5}
$$
故整预解有有限阶增长。

条件 (1.4) 在正系数的任意物理排列下不变。
充分条件是
$$
N_a(1/t):=\#\{j:a_j\ge1/t\}\ge c t^p
\quad(t\text{ 大}),
\tag{1.6}
$$
因为 $\Theta_a(t)\ge N_a(1/t)$。
例如正行满足
$$
a_j\ge c_*(j+1)^{-\sigma},\qquad \frac12<\sigma<1
\tag{1.7}
$$
时可取 $p=1/\sigma$，所以 $q=1/(1-\sigma)$。
也可仅要求下降重排满足相同下界。
不需要物理位上的上比较界；原 $a\in\ell^2$ 始终保留。

## 2. 单个位的严格收缩，含真实 carry

实际局部算子为
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
N_j=E_j+\eta_jE_j^*N_{j+1}.
$$
$V_j$ 增生由 R128 §6 的准确 Cayley 恒等式给出。
纯单个位
$$
S_j^0=I-2E_j
$$
也增生，并且实际差满足
$$
\|V_j-S_j^0\|\le8\eta_j,\qquad
\eta_j\le e^{-770\cdot16^j}.
\tag{2.1}
$$
因此 $e^{-sV_j}$、$e^{-sS_j^0}$ 对 $s\ge0$ 都是收缩。

对这两个有界生成元使用准确 Duhamel 恒等式，
$$
e^{-V_j}-e^{-S_j^0}
=-\int_0^1 e^{-(1-s)V_j}(V_j-S_j^0)e^{-sS_j^0}\,ds,
$$
得到
$$
\|e^{-V_j}-e^{-S_j^0}\|\le8\eta_j.
\tag{2.2}
$$
$E_j^2=0$，故
$$
e^{-S_j^0}=e^{-1}(I+2E_j),\qquad
\|I+2E_j\|=1+\sqrt2.
$$
所以
$$
\|e^{-V_j}\|
\le e^{-1}(1+\sqrt2)+8e^{-770}<9/10=\rho.
\tag{2.3}
$$
任意 $s\ge0$ 写成整数部分与余数，使用半群乘积和收缩性：
$$
\boxed{\|e^{-sV_j}\|\le\rho^{\lfloor s\rfloor}.}
\tag{2.4}
$$
这里不能只把 $V_j-S_j^0$ 当作整条无界主行的一个粗全局扰动；
(2.2) 在每个位付一次实际误差，之后 (2.4) 保留严格局部衰减。

## 3. 真正有限集合分解给全无界半群

取任意有限位集合 $F$，置
$$
H_F=\sum_{j\in F}a_jV_j,\qquad
T_F=X_{\sum_{j\notin F}a_j\chi_j}.
$$
$H_F$ 有界、$T_F$ 最大增生，且真实闭域上
$$
X=T_F+H_F,\qquad \operatorname{Dom}X=\operatorname{Dom}T_F.
\tag{3.1}
$$
该式由第一阶有限有界扰动和 R128 的域交换给出。

每个 $V_j$ 属于 $A'$，故与 $T_F$ 的完整域及预解交换，
也与其收缩半群交换。
有限有界扰动的直接半群计算给
$$
\boxed{
S(t)=\left(\prod_{j\in F}e^{-ta_jV_j}\right)e^{-tT_F}.
}
\tag{3.2}
$$
为核其生成元，可在 $\operatorname{Dom}T_F$ 上对右侧求导，
得到 $-(T_F+H_F)$；右侧是强连续收缩半群，
其闭生成元由 (3.1) 唯一识别为 $-X$。
这里没有把无穷乘积当作未经证明的有界半群。

给定 $t$，取
$$
F_t=\{j:ta_j\ge1\},
$$
它有限。由 (2.4)、(3.2) 及尾半群收缩性，
$$
\|S(t)\|
\le\prod_{j\in F_t}\rho^{\lfloor ta_j\rfloor}
=\rho^{\Theta_a(t)},
$$
证明 (1.2)。

对任意固定有限 $F$，
$$
\liminf_{t\to\infty}\Theta_a(t)/t
\ge\sum_{j\in F}a_j.
$$
正系数不可和，令有限 $F$ 的总质量任意增大，得到 (1.3)。

## 4. 全平面的实际 Laplace 预解及增长

(1.3) 保证对每个 $z\in\mathbb C$，
$$
\mathcal R(z)=\int_0^\infty e^{tz}S(t)\,dt
\tag{4.1}
$$
在算子范数中绝对收敛，并在紧 $z$ 集合上一致收敛；
所有固定阶 $z$ 导数也由同样支配界允许逐项积分。
因此 $\mathcal R$ 是 $B(H)$ 值整函数。

在 $\operatorname{Re}z<0$，
通常收缩半群的 Laplace 恒等式给
$\mathcal R(z)=(X-z)^{-1}$。
R134 已证明右侧在整个平面存在并解析，
故对各矩阵元用恒等定理，得到
$$
\boxed{(X-z)^{-1}=\mathcal R(z)\quad(z\in\mathbb C).}
\tag{4.2}
$$
若要避免借用整预解的继续，亦可对
$f\in\operatorname{Dom}X$ 积分真实轨道导数，
先得到 $\mathcal R(z)(X-z)f=f$，再用 R134 的全平面双射识别。
没有将一个仅形式积分称作实际逆。

若 (1.4) 成立，可增大有限常数得到
$$
\|S(t)\|\le C e^{-\gamma t^p}\qquad(t\ge0)
$$
其中 $\gamma>0$。
Young 不等式给
$$
rt\le(\gamma/2)t^p+C_\gamma r^{p/(p-1)}
\qquad(r,t\ge0).
$$
代入 (4.1)，得
$$
\|(X-z)^{-1}\|
\le C e^{C_\gamma(\operatorname{Re}z)_+^q}
\int_0^\infty e^{-(\gamma/2)t^p}\,dt,
$$
即 (1.5)。

## 5. 有界交换扰动和未知不变限制

若 $H_0\in A'$ 有界，则 $X+H_0$ 在原 $X$ 域上闭，
其真实半群为
$$
S_{H_0}(t)=e^{-tH_0}S(t).
$$
因此
$$
\|S_{H_0}(t)\|
\le e^{t\|H_0\|}\rho^{\Theta_a(t)}.
\tag{5.1}
$$
在 (1.4) 下仍给同一个有限阶 $q$ 的整预解界，
只改变常数。
任意复 $\ell^2$ 指数倾斜的 $H_{a,b}$ 是这种实际有界交换扰动；
标量常数也可吸收进 $H_0$。

每个 $S(t)$、$S_{H_0}(t)$ 是有界交换子，
因而由 R88 保持任何闭 $A$ 不变空间 $M$。
限制半群的生成元是自然限制 $(X+H_0)_M$；
R128/R134 已付其准确域和所有预解保持。
特别
$$
((X+H_0)_M-z)^{-1}
=(X+H_0-z)^{-1}|_M,
$$
且其范数不超过原 $H$ 上范数。
所以 (1.5) 对每个未知 $M$ 同样成立。
本节没有沿用未知限制上的通常伴随同域或 $C$。

## 6. 为后续排核保留的边界

本稿只给实际正主行、其有界交换扰动和未知限制的定量整预解。
没有从有限阶本身排除任意慢 Bell 核。

$\sigma=1$ 的谐和例不能由 (1.6) 取某个 $p>1$；
此时更细的 $\Theta_a(t)$ 确可含 $t\log t$ 量级，
但相应整预解通常需双指数型预算。
本稿不把它自动纳入后续有限阶 Phragmén–Lindelöf 论证。

依赖：R125/R128 的真实第一阶域、正 Cayley 和最大增生性；
R134 的全平面预解及有界交换扰动；
原权的实际局部差 $\|V_j-S_j^0\|\le8\eta_j$。
半群存在及左半平面 Laplace 恒等式只使用最大增生算子的标准收缩半群定理。
