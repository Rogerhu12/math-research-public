# R56：实际参数化真头的切口迹、完整二阶导数及二次余项

作者：root（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已证明，实际有理账本八门全过。** 本文将 [R54](R54-expanded-head-box-and-parameter-hull.md) 的实际 46 参数真头代入 [R45](R45-parameterized-full-head-trace-and-outer-schur.md) 的完整迹公式，支付同一 node12 上统一的参数 Lipschitz 常数和外头 Schur 接合可使用的二次余项常数。没有新 Green 核、矩阵逆、径向积分或非线性求解。

固定对象仍是 q003 实数背景上的 cells 12..224 加 R18 真无限尾。所用参数单位是 R54 的全部 $v_j$；所有下文导数都按这一参数范数解释。外 cells 0..11 的连续解、其 Schur 逆、大幅前缀和整闭面的几何仍各有独立缺口。

## 1. 明确的参数范数与复化

浅端参数为实余弦 canonical 高度 $a_j=\delta Q_{2j}(b)$，$Q=h_\perp/r^4$，取

$$
\|a\|_v=\sum_{j=1}^{46}|a_j|/v_j.
\tag{56.1}
$$

全部 $v_j$ 是 R54 表列的实际正 dyadic 数，指数在 $-232$ 至 $-304$ 之间。实参数给真实头解；作 Cauchy 估计时使用相同范数的复球 $\|a\|_v<1$。

**引理 56.1。** R54 的不变盒、工作域、mean 分支、真实深参数域及统一距离权收缩，对这个复参数球保持有效。

**证明。** R51/R53 中的非线性估计是完整 Fourier Wiener 代数的绝对范数估计；线性提升与真实深图解析，mean 和点态逆使用已选的唯一小解析分支。将余弦参数复化只把两个 signed 频率的同一复半幅代入，所有绝对值卷积界不变。

R54 的提升域及凸包证明只使用 $|a_j|$，轴的复相位不影响任一正源上界；未知差值上界同样以各块 Banach 范数表述。所有路径仍处在相同的严格工作域和分母余量内。因此原全部 641 行及统一收缩对复球也成立。逐次迭代在参数紧集上一致收敛，给出复球内部的 Banach 值全纯解。证毕。

它只复化参数，真实背景函数、度量、角宽、深图的选择均未改变。

## 2. 从正源预算到实际统一参数导数

沿用 R54 的 $J,W,\lambda$，其中

$$
\lambda=3970/4096<1,
\qquad JW\preceq\lambda W.
\tag{56.2}
$$

R54 主账本保存旧参数的完整正源预算 $c_i^0\ge0$。新参数源的逐行上界为 $\eta(1+\lambda)W_i$，实际 $\eta=2^{16}$。定义

$$
C=\max\left\{\max_i\frac{c_i^0}{W_i},\;\eta(1+\lambda)\right\},
\qquad
K=\frac C{1-\lambda}.
\tag{56.3}
$$

由 R54 的逐轴凸包证明，对任意参数方向 $h$，同一完整正源算子满足

$$
B|h|\preceq CW\|h\|_v.
\tag{56.4}
$$

因此两个实际固定点或一个方向导数都满足

$$
\|Y(a)-Y(\widetilde a)\|_W
\le K\|a-\widetilde a\|_v,
\qquad
\|D_aY(a)h\|_W\le K\|h\|_v.
\tag{56.5}
$$

这里 $\|\cdot\|_W$ 是原 641 块的加权最大范数。证明为
$|\delta Y|\preceq J|\delta Y|+B|\delta a|$ 后取该范数，或对固定点方程求导并求和 Neumann 级数。参数球和所有工作域一致，所用连接路径均合法。

不能把 (56.5) 当作完整物理场的界而省去线性提升。令

$$
L_b=\max_j A_{12,j}v_j,
\quad
U_b=W_{L,12}+W_{N,12}+W_{R,12}+W_\infty,
\quad
D_b=L_b+KU_b.
\tag{56.6}
$$

则完整物理强场在 cut 的差与方向导数都受 $D_b$ 控制。实际有理计算支付

$$
\boxed{D_b<2^{-62}.}
\tag{56.7}
$$

R54 的完整 cut 场范数至多 $1+t_{12}'<2$，故 R45 的完整 mean、连接正根和二阶迹域条件同时适用。没有仅控制非均值而遗漏 mean 导数。

## 3. 全部实际迹界

在固定外头角宽 $\sigma=1/64$ 上，使用 R45 的完整 Wiener 范数
$\|u\|_{\sigma,1}=\sum_m(1+|m|)e^{\sigma|m|}|u_m|$。

令 $\varepsilon_b=V(b)/w(b)$。同一已付真实 cut 常数给
$\varepsilon_b\le A_{12}<2^{-51}$、$B_{12}\ge4$、$\tau_b-\sigma>1/8$。程序直接使用更精确的有理 $A_{12}$ 和 $B_{12}$，不只使用这三个展示上界。$b$ 来自 R53 的同一真实半径盒。

对下表每个迹算子 $\mathcal T$，实际结论是

$$
\|\mathcal T(a)-\mathcal T(\widetilde a)\|
<2^e\|a-\widetilde a\|_v,
\qquad
\|D\mathcal T(a)\|<2^e.
\tag{56.8}
$$

零差时按非严格的零界理解；严格数字表示可选的 Lipschitz 常数小于 $2^e$。

| 切口迹 | 严格 dyadic Lipschitz 指数 e |
|---|---:|
| P | -123 |
| K⊥ | -113 |
| (P,K⊥) 联合 | -113 |
| K（含完整 mean） | -113 |
| G 连接 | -112 |
| h⊥ | -129 |
| hθ | -128 |
| hθθ | -126 |
| hr（含完整 mean） | -114 |
| hrθ | -113 |
| hrr | -106 |
| 完整 polar jet 最大值 | -106 |

表中 $P$、$K_\perp$、$G=(\Gamma-1)/w^2$ 与 R45 完全同义。$K$ 包括真实 mean。联合 $(P,K_\perp)$ 使用两个 Wiener 范数之和；最后一行的 polar 二阶 jet 使用下面六个 Wiener 范数的**最大值**：

$$
\mathcal J=(h_\perp,h_\theta,h_{\theta\theta},
              h_r,h_{r\theta},h_{rr}).
\tag{56.9}
$$

**证明。** 将 (56.6) 代入 R45 (45.26)–(45.28)、(45.35)，并使用同一真实背景的 $w(b)\le1/2$。完整系数依次可取

$$
\begin{array}{c|c}
\text{迹}&\text{乘 }D_b\text{ 的系数}\\\hline
P&\varepsilon_b/B_{12}\\
K_\perp\text{ 或 }(P,K_\perp)\text{ 联合}&\varepsilon_b\\
K\text{（完整 mean）}&17\varepsilon_b/16\\
G&3\varepsilon_b\\
h_\perp&b\varepsilon_b/(4B_{12})\\
h_\theta&b\varepsilon_b/(2B_{12})\\
h_{\theta\theta}&3b\varepsilon_b/(2B_{12})\\
h_r&5\varepsilon_b/8\\
h_{r\theta}&3\varepsilon_b/2\\
h_{rr}&144\varepsilon_b
\end{array}
\tag{56.10}
$$

所有系数都乘同一个完整物理差 $D_b$。真实半径小于1、$B_{12}\ge4$，所以 $144\varepsilon_b$ 也支配 (56.9) 的最大值范数。程序对每项精确分式向上取严格 dyadic 上界，得到表中指数。证毕。

这组 jet 明确区分了高度零模：$h_\perp$ 不含高度积分常数，而 $h_r,h_{rr}$ 包含完整 mean 导数。cuff 的高度规范仍然固定；cut 上的 mean 高度数值须作为外接合的一条标量位置条件继续匹配，不能逐胞元重新平移。所有二阶界都是同一 polar 坐标中的界；Cartesian 图还需 R30/R27 的坐标转换。

单个 canonical 坐标导数可由 (56.8) 除以 $v_j$ 得到。若按真实物理高度 $H_{2j}=b^4a_j$ 求导，还须再除以 $b^4$；小的规范常数不能直接作为不带单位的物理导数。

## 4. 实际二次迹余项

固定上述任一 Banach 值迹，记 $T_0=\mathcal T(0)$、
$A_T=D\mathcal T(0)$。由复球版本的 (56.8)，

$$
\sup_{\|a\|_v<1}\|\mathcal T(a)-T_0\|<M,
\qquad M=2^e.
\tag{56.11}
$$

在 $\|a\|_v\le1/2$ 内，R45 的两个混合 Cauchy 圆各取半径 $1/4$，得到
$\|D^2\mathcal T(a)\|\le16M$。沿 $ta$ 积分后，实际非线性余项
$\mathcal R_T(a)=\mathcal T(a)-T_0-A_Ta$ 满足

$$
\boxed{\|\mathcal R_T(a)\|\le2^{e+3}\|a\|_v^2,\qquad
\|D\mathcal R_T(a)\|\le2^{e+4}\|a\|_v.}
\tag{56.12}
$$

特别地，外头 R44 使用的联合 $(P,K_\perp)$ 迹有

$$
\|\mathcal R_T(a)\|\le2^{-110}\|a\|_v^2,
\qquad \|D\mathcal R_T(a)\|\le2^{-109}\|a\|_v.
\tag{56.13}
$$

对 (56.9) 的完整 polar jet 最大值范数，对应常数为 $2^{-103}$ 和 $2^{-102}$。这些都是关于准确真头迹及其准确中心导数的界；没有把辅助低中心、有限差分或有限尾切线替换为 $T_0,A_T$。

## 5. 已执行资料与仍待支付的外头条件

正式执行通过 `strong_resource_run.py` 返回 exit0（工具完成块 `aeb9f3`），wall0.303419秒，wait4峰18816KiB。完整账本
`notes/2026-11-12-root-r56-actual-head-trace-bounds-r1.json`
为11200B，SHA256 `a78d3456d9fb20609d034798ea437628e23d1cc88d77c9a8633d5ac294f3789f`；包含每项未四舍五入的精确分式、全部单位约定、八个域/比较门以及源与输入 SHA。

源为 `computations/root_head_actual_trace_bounds.py`。实际输入包括 R54 完整扩盒、R53 同一真实高度转换及 R45 已正式完成的 `closure-cut-trace-interface-constants-r1.json`，三者的同一 density/连续角宽 SHA 已核对。

R56 支付了外头接合所需的一组实际统一导数和迹余项。外头的连续径向 Green 核、候选的真实 Darboux 缺陷、完整低/高边界 Schur 逆、mean 高度位置及强前缀仍须继续求证；本结果没有给这些尚缺的量填入数值。
