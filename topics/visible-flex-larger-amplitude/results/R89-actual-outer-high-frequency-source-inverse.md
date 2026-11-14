# R89：实际外两胞元的固定条带高频源逆

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

本文对 R26 的同一真实外胞元 11、10，使用 R68 已执行的全部 10,793 个原面板，构造一个一次固定的变宽度 Fourier 空间。在该空间内，所有偶频 $|m|\ge16384$ 的有源向外流恢复一个角导数；其源到场常数为 65540。完整 mean 小根及完整 Wiener 逆均保留。若完整物理强范数不超过 $2^{-34}$，高频自身反馈严格小于 $1/250$。

这是实际背景上的完整条件工具。本文没有声称当前有限中心已处于所定义的新条带域，也没有支付中间偶频 $94,\ldots,16382$、低频参数一致性或外胞元 9 至 0。给定真实高频内迹，本文使用向外初值问题，不擅自指定高频外端高度为零。

## 1. 同一物理方程、signed 模式与完整源

保持 R44/R68 的真实 $r,r_x,w,w_x$、冻结 warp 和实际 source 分段，令

$$
P=\frac{h_\theta}{rw},\qquad K=\frac{h_{\perp,r}}w,\qquad
s=\frac{r_x}{r}>0,\qquad \ell=\frac{w_x}{w},\qquad E=1+w^2.
\tag{89.1}
$$

$P,K$ 均为非均值变量。所有 Fourier 模式为偶整数，非零频率满足 $|m|\ge2$。在复 Fourier 坐标中，背景方程是

$$
\frac d{dx}\binom{P_m}{K_m}=
\begin{pmatrix}-s-\ell&im s\\-im\ell&-2\ell\end{pmatrix}
\binom{P_m}{K_m}+\binom0{N_m}.
\tag{89.2}
$$

它与 R68 对正弦 $P$、余弦 $K$ 写出的实矩阵酉等价。这里 $N$ 使用原 source 坐标 $x$ 的 $K_x$ 单位，不能再乘一个 $r_x$。

完整 mean 相对斜率记为 $\mathfrak m=\mathfrak m(P,K)$，取 R33/R44 的同一 connection 小根。置

$$
U=K_\theta-P,\qquad C=K+P_\theta,\qquad
l=\mathfrak m+K+E P_\theta,\qquad \mathfrak c=s+|\ell|.
$$

原非线性第二源可以准确写成

$$
N=\mathcal P_{\ne0}\frac{Q+B_{\mathfrak m}}{1+l},
\tag{89.3}
$$

$$
Q=Es\,U^2+\ell\{E C^2-w^2(K^2+P^2)\},\qquad
B_{\mathfrak m}=\ell\{2\mathfrak m(K+E P_\theta)+\mathfrak m^2\}.
\tag{89.4}
$$

式中 $E C^2-w^2(K^2+P^2)$ 的减号来自准确消元，不把它改成另一个方程；求绝对上界时可以使用三角不等式。投影 $\mathcal P_{\ne0}$ 在使用的 Fourier 范数中是收缩。$\mathfrak m$ 及 $(1+l)^{-1}$ 均不做有限级数截断。

## 2. R68 的真实面板数据与点态性质

按真实向外次序枚举全部面板 $I_i$，原 source 长度为 $\Delta_i>0$。每片固定使用 R68 保存的准确正 dyadic 尺度 $b_i$，并置

$$
u_m=(P_m,K_m/b_i)^T.
$$

R68 的对数范数界为

$$
\frac d{dx}|u_m|_2\le(d_++|m|\gamma_i)|u_m|_2+\frac{|N_m|}{b_i},
$$

$$
d_+=\max(-s-\ell,-2\ell),\qquad
d_-=\max(s+\ell,2\ell),\qquad
\gamma_i=\tfrac12|s b_i+\ell/b_i|.
\tag{89.5}
$$

零向量处按上 Dini 导数理解，故不需假定范数非零。

这里使用实际源码中更具体的性质：R68 的 $g_i$ 是完整区间包围 $\gamma_i$ 的上端乘 $\Delta_i$，所以

$$\gamma_i(x)\le g_i/\Delta_i\quad(x\in I_i).\tag{89.6}$$

这不只是一个无位置的积分界。新最优尺度和回退旧尺度的两个执行分支都按同一方式计算。对应源码分别为 R68 的 step 和其冻结依赖 analytic_energy_step。

令真实界面跳变的正对数为

$$
j_i^+=\log_+(b_{i-1}/b_i),\qquad
j_i^-=\log_+(b_i/b_{i-1}),\qquad j_1^\pm=0.
$$

R68 保存的 $n_i^\pm$ 是相应完整点态对角上端乘 $\Delta_i$ 再加跳变的向上包围。其连续位置后处理另外给出 $J_i^\pm\ge j_i^\pm$。定义同一准确正预算

$$p_i^\pm=\max(0,n_i^\pm,J_i^\pm).\tag{89.7}$$

于是 $p_i^\pm\ge j_i^\pm$，且

$$
p_i^+/\Delta_i\ge(d_+)_+,\qquad
p_i^-/\Delta_i\ge(d_-)_+.
\tag{89.8}
$$

实际全部面板的 R68 证书给

$$
\sum_i g_i<0.080104707<\frac{21}{256},\qquad
\sum_i p_i^+<282,\qquad \sum_i p_i^-<289,
\tag{89.9}
$$

$$
\frac1{256}\le b_i<18553.354573,\qquad 1+b_i<18555.
\tag{89.10}
$$

后两项和的界直接来自 R68 任意位置对的对数前因子上界 281.281503 和 288.945155：那些前因子还加了两个非负首尾换范数项，故它们上界也控制相应 $\sum p_i^\pm$。这些数字是对数预算；本文没有把它们误当作乘法常数。

有一条用于源密度的点态恒等比较：

$$
s+|\ell|\le(d_+)_++(d_-)_+.
\tag{89.11}
$$

若 $\ell\ge0$，右边的 $(d_-)_+$ 已至少为 $s+\ell$。若 $\ell=-L<0$，$d_+=2L$、$(d_-)_+=\max(s-L,0)$，其和至少为 $s+L$。因此

$$
c_i:=\frac{p_i^++p_i^-}{\Delta_i}\ge\mathfrak c(x)>0
\quad(x\in I_i).
\tag{89.12}
$$

## 3. 一次固定的实际变条带

固定

$$
M=16384,\qquad \kappa=2^{-16},\qquad \tau(a)=\frac{18}{125},
\tag{89.13}
$$

其中 $a$ 是真实 node12。R61 的同一真实内迹条带为
$\tau_b=0.1444358307482676696960\ldots>18/125$，所以这只是合法缩窄。

在面板 $I_i$ 内定义连续线性变化率

$$
-\tau'(x)=\frac{g_i}{\Delta_i}
+\frac{p_i^+}{M\Delta_i}+\kappa c_i.
\tag{89.14}
$$

在进入第 $i\ge2$ 片时另令条带向外跳减 $p_i^+/M$。这完全由已保存真实面板数据定义，与解、迭代次数、源或参数均无关。

总宽度损失满足

$$
\tau(a)-\tau(R)
\le\sum_i g_i+\frac{2\sum_i p_i^+}{M}
+\kappa\sum_i(p_i^++p_i^-)
<\frac{8203}{65536}.
\tag{89.15}
$$

从而在全部两胞元上

$$
\tau(x)>\frac1{64}+\frac{26273}{8192000}>\frac1{64}.
\tag{89.16}
$$

这里额外使用一次 $p_i^+/M$ 专门支付尺度跳变；不能将面板增长和界面跳变只付一次后都使用。所有位置的条带同时由 (89.14) 定义，不在每次非线性迭代重新损失宽度。

对 $|m|\ge M$，由 (89.5)、(89.6)、(89.8)，

$$
\frac d{dx}\log\!\left(e^{|m|\tau(x)}|u_m(x)|_2\right)
\le-|m|\kappa c_i
\tag{89.17}
$$

用于齐次非零解；一般解仍由 Dini 导数得到对应算子界。在界面，$u$ 的换坐标范数至多为 $e^{j_i^+}$，而解析权跳减因子为 $e^{-|m|p_i^+/M}$，两者乘积不超过1。

因此对任意有序位置 $y\le x$，包括两端落在面板内部的情形，真实齐次传播满足

$$
e^{|m|\tau(x)}
\|\Phi^{u}_m(x,y)\|_2e^{-|m|\tau(y)}
\le\exp\!\left(-|m|\kappa\int_y^x c(t)\,dt\right),
\tag{89.18}
$$

其中 $c(t)=c_i$。已实际支付的较大有限增长和所有跳变已进入 (89.14)，没有留下一个被省略的 $e^{281}$ 前因子。

## 4. 全部无限高频的有源逆

先在物理场连续的高频场上定义；所得积分解的分段连续可微性随后由真实 Duhamel 公式给出

$$
\|H\|_{\mathcal X_H}=
\sum_{\substack{m\in2\mathbb Z\\|m|\ge M}}
(1+|m|)\sup_x e^{|m|\tau(x)}
\left|\left(P_m(x),K_m(x)/b_i\right)\right|_2.
\tag{89.19}
$$

在界面取左右两侧的 supremum。物理场本身连续，$u$ 与解析权按固定定义跳变。这是有限面板上的完备加权连续场空间；Fourier 求和在各径向 supremum 之后进行。

对第二源定义较弱的空间

$$
\|N_H\|_{\mathcal Y_H}=
\sum_{\substack{m\in2\mathbb Z\\|m|\ge M}}
\sup_x\frac{e^{|m|\tau(x)}|N_m(x)|}{b_i c_i}.
\tag{89.20}
$$

**定理89.1。** 零初迹的向外有源解算子 $\mathcal G_H$ 满足

$$
\boxed{\|\mathcal G_HN_H\|_{\mathcal X_H}
\le65540\,\|N_H\|_{\mathcal Y_H}.}
\tag{89.21}
$$

**证明。** balanced 第二源为 $N_m/b_i$。将 (89.18) 代入 Duhamel 公式，每个模式的加权输出至多为其 (89.20) 模质量乘

$$
\int_a^x c(y)\exp\!\left(-|m|\kappa\int_y^x c(t)\,dt\right)\,dy
\le\frac1{|m|\kappa}.
$$

乘以 $1+|m|$，其最大值为
$(1+1/M)/\kappa=65540$。先对位置取 supremum，再对模式求和，即得 (89.21)。没有有限模截断，没有交换 sup 与 sum，也没有从纯齐次估计直接推断源项可积。证毕。

对于非零高频初迹，齐次 lift 在 (89.19) 中不超过该迹的 balanced 范数。由 $b_i\ge1/256$，它至多为物理强迹范数的256倍。初迹包含真实高高度和高动量两分量；二者均由内头输出，不在此重新设零。

物理强范数取

$$
\|(P,K)\|_{\mathcal X_{\rm ph}}=
\sum_{m\ne0}(1+|m|)
\left(\sup_xe^{|m|\tau(x)}|P_m(x)|
+\sup_xe^{|m|\tau(x)}|K_m(x)|\right).
\tag{89.22}
$$

注意其两个分量分别取 supremum。因此从 (89.19) 回到 (89.22) 使用安全的

$$\|H\|_{\mathcal X_{\rm ph}}<18555\,\|H\|_{\mathcal X_H},\tag{89.23}$$

而不把同一位置的欧氏常数未经说明地套到两个不同位置的最大值上。

## 5. 完整 weak 源及其导数

设 $0<w\le1/2$，非均值场的 (89.22) 范数至多为 $R\le1/64$。R33/R44 的完整复小根给

$$
|\mathfrak m|\le4R^2,\qquad
|D\mathfrak m[\delta P,\delta K]|\le16R\,V,
\tag{89.24}
$$

其中 $V$ 是方向的物理强范数。根及方向均在同一连接域中，不能只控制中心点。

由于 $|m|\ge2$，弱 Fourier 范数中有

$$
\|P\|_0+\|K\|_0\le R/3,\qquad
\|K_\theta-P\|_0\le R,\qquad
\|K+P_\theta\|_0\le R.
\tag{89.25}
$$

这里及以下的径向代数约定仍是先取各 Fourier 系数的径向 supremum 再求和。因为 $\tau(x)\ge0$，$e^{\tau|j+k|}\le e^{\tau|j|}e^{\tau|k|}$；再用 $1+|j+k|\le(1+|j|)(1+|k|)$，每项卷积由固定非负模质量控制。由此所有下述乘积界都在同一个固定 Banach 空间内成立，不只是在每个位置分别成立。特别地，可以用同一模质量序列同时控制 $U_m,C_m$，并用它的 $1/3$ 控制 $|P_m|+|K_m|$。所以 (89.26) 中 $s/\mathfrak c$ 与 $|\ell|/\mathfrak c$ 在取径向 supremum 以前相加为1；没有把两个分别最坏的径向系数偷偷当成同一位置。

$E\le5/4$，故

$$
\|Q\|_0\le
\left[Es+(E+w^2/9)|\ell|\right]R^2
\le\frac{23}{18}\mathfrak c R^2.
\tag{89.26}
$$

同时

$$
\|B_{\mathfrak m}\|_0\le\mathfrak c(10R^3+16R^4),\qquad
\|l\|_0\le5R/4+4R^2.
\tag{89.27}
$$

对完整商 (89.3) 求导，而不是只求二次主部导数，得到

$$
\|DQ\|_0\le\frac{23}{9}\mathfrak c RV,\qquad
\|DB_{\mathfrak m}\|_0\le\mathfrak c(50R^2+128R^3)V,
\quad \|Dl\|_0\le(5/4+16R)V.
\tag{89.28}
$$

所有系数非负，对 $R$ 单调。令 $d=1-5R/4-4R^2$，在 $R=1/64$ 有 $d=1003/1024$，并且

$$
\frac{23/18+10R+16R^2}{d}
=\frac{13252}{9027}<\frac32,
\tag{89.29}
$$

$$
\frac{23/9+50R+128R^2}{d}
+\frac{R(23/18+10R+16R^2)(5/4+16R)}{d^2}
=\frac{31451168}{9054081}<4.
\tag{89.30}
$$

因此在整个指定域内，

$$
\boxed{\|N/\mathfrak c\|_0\le\tfrac32R^2,\qquad
\|DN[\delta]/\mathfrak c\|_0\le4RV.}
\tag{89.31}
$$

(89.31) 是准确可复算的完整源界。分母的几何级数、mean 的所有阶及其方向导数都已包括。它允许任意高频输入；有限输出若另用该弱源，仍须支付输出的 $1+|m|$，不能凭 (89.31) 免费获得有限/无限其他 Green 门。

## 6. 在 balanced 高频空间中的真正小反馈

固定完整物理工作半径

$$R_*=2^{-34}.\tag{89.32}$$

对某个高频方向 $\delta H$，把方向场逐位置除以同一 $b_i$。由于非线性及 mean 根在每个位置是角向代数运算，且方向导数是线性的，

$$\frac{DN(P,K)[\delta H]}{b_i}
=DN(P,K)[\delta H/b_i].\tag{89.33}$$

$b_i$ 只依赖径向面板，故它与所有角导数及角均值交换。又有

$$
\|\delta H/b_i\|_{\mathcal X_{\rm ph}}
\le(256+1)\|\delta H\|_{\mathcal X_H}
=257\|\delta H\|_{\mathcal X_H}.
\tag{89.34}
$$

此处两个分量的 supremum 分别控制，不把它们当成同一位置最大值。由 $\mathfrak c/c_i\le1$，(89.21)、(89.31) 给

$$
\|\mathcal G_HP_HD N[\delta H]\|_{\mathcal X_H}
\le65540\cdot4\cdot257R_*\|\delta H\|_{\mathcal X_H}
=\frac{4210945}{1073741824}\|\delta H\|_{\mathcal X_H}
<\frac1{250}\|\delta H\|_{\mathcal X_H}.
\tag{89.35}
$$

若方向是按 (89.22) 测量的有限中频场 $\delta E$，则
$\|\delta E/b_i\|_{\mathcal X_{\rm ph}}\le256\|\delta E\|_{\mathcal X_{\rm ph}}$；
同一充分常数 $1/250$ 也控制其到高频响应的映射列。完整 mean 对方向的贡献已经通过 (89.28) 计入，不能在耦合时再把它漏掉。

## 7. 实际非零高内迹与有限中心的纯高残差

R78 的完整 R74 复参数积盒给出真实内迹中 $|m|\ge8192$ 的联合 balanced 物理强范数上界

$$
\frac{695120740485650607377290890840438620026179722216766164723}{2^{379}}.
\tag{89.36}
$$

这里使用 R78 的 head 行，条带为真实 $\tau_b$，而不是已缩到外侧 $1/64$ 的更小显示数。该原 balanced 变量为 $(B_{12}P,K)$ 且 $B_{12}\ge1$，故它也控制未加 $B_{12}$ 的物理迹。限制到 $|m|\ge16384$、缩窄到 $18/125$ 后不增大。再由 (89.10) 乘256，严格小于 $2^{-181}$。记此真实高初迹 lift 为 $H_{\rm bd}(a)$，则

$$\|H_{\rm bd}(a)\|_{\mathcal X_H}<2^{-181}.\tag{89.37}$$

这是非零真无限头输出的包围；本文没有另选一个远端 Robin 图。

令 $C_0$ 是仅含 $0<|m|\le92$ 的给定非均值中心，其 (89.22) 范数不超过 $R_*$。mean $\mathfrak m(C_0)$ 是角向常数，因此 (89.4) 的完整分子频率不超过184，$l$ 的频率不超过92。若 $|m|\ge16384$，Neumann 项 $(Q+B_{\mathfrak m})(-l)^k$ 只能从 $k\ge177$ 开始贡献，因为

$$184+176\cdot92=16376<16384.\tag{89.38}$$

在 (89.32) 下 $\|l\|_0\le5R_*/4+4R_*^2<2^{-33}$。故完整无限商的高频尾满足

$$
\|P_HN(C_0)\|_{\mathcal Y_H}
\le256\cdot\frac32R_*^2(2^{-33})^{177}<2^{-5900},
$$

$$
\|\mathcal G_HP_HN(C_0)\|_{\mathcal X_H}<2^{-5883}.
\tag{89.39}
$$

这只是有限中心自身的纯高源；如果有实际中频场，必须通过下一节的真实差分源另计，不能把它视为同样有有限支撑。

## 8. 一个保留实际中频的条件高块存在定理

**定理89.2。** 给定真实 R74 内头参数 $a$，给定有限中心 $C_0$（模式 $2,\ldots,92$）和给定中频场 $E$（模式 $94,\ldots,16382$）。设

$$
\|E\|_{\mathcal X_{\rm ph}}\le r_M,\qquad
r_H=2^{-179}+\frac{r_M}{200},
$$

$$
\|C_0\|_{\mathcal X_{\rm ph}}+r_M+18555r_H\le2^{-34}.
\tag{89.40}
$$

那么从真实非零高内迹出发的完整高方程

$$
H=H_{\rm bd}(a)+\mathcal G_HP_HN(C_0+E+H)
\tag{89.41}
$$

在 $\|H\|_{\mathcal X_H}\le r_H$ 内有唯一解，收缩常数小于 $1/250$。

**证明。** (89.40) 保证整个闭球及任意两点之间的线段均在完整 mean/逆的同一工作域中。将源分解为 $N(C_0)$ 与完整差分，(89.35)、(89.37)、(89.39) 给

$$
\|T(H)\|_{\mathcal X_H}
<2^{-181}+2^{-5883}+\frac{r_M+r_H}{250}<r_H.
\tag{89.42}
$$

最后一个严格不等式在 $r_M=0$ 时已由
$2^{-181}+2^{-5883}<(249/250)2^{-179}$ 成立；
$r_M$ 的剩余系数为
$1/200-1/250-1/50000=49/50000>0$。
同域差分由 (89.35) 给严格收缩。Banach 不动点定理适用。解的连续物理跨面板接合由真实 Duhamel 公式保证；条带仍大于 $1/64$，所以所得角向级数及任意固定阶角导数一致收敛。证毕。

该定理保留 $E$、全部高初迹以及完整 mean 根。它只解所投影的高方程；当低/中方程尚未解决时，不由此声称完整 mean 传播约束、全部 Darboux 方程或外端参数一致性已经成立。

## 9. 数据身份、严格算术与待付接口

本文所用实际背景门均来自已经正式完成的 R68 和 R78：

- R68 原面板最优固定 frame 作业 37378，正式 exit 0；连续/任意位置对后处理 70557，正式 exit 0。面板、源、背景和尺度都未更改。
- R78 完整复参数/高迹作业 97965，正式 exit 0；本文只缩窄其真实 head 条带并投影到更高频。
- 本文的整数及有理比较已用工具中的 JavaScript BigInt 精确算术逐项核销，不使用浮点显示来决定门。没有伪造新的 Python/Arb 作业或 ODE 终态。

固定输入：

| 文件 | SHA256 |
|---|---|
| notes/2026-11-12-root-outer-continuous-frame-r1.json | d47f1507427d75c9e94452296cf4e5706e1b3468135d44b486845b1c212f70fe |
| notes/2026-11-12-root-r78-true-cut-cauchy-r1.json | 9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930 |
| computations/root_outer_optimal_frame_budget.py | ef41df6103a8c8b9cabc4ac8f2be133a244d5e0361e7d861ff7266426498e63b |
| computations/tail_outer_background_column_flow.py | 5b548692afa79035e8ac612c8148de0f4ed2a22e9c40ee7592fa36913156193c |

精确常数记录见 [R89 有理账本](../notes/2026-11-12-closure-r89-exact-strip-ledger.json)。

仍需实际支付的接口如下：当前候选或所选线性中心在 (89.22) 的新变条带范数；全部中频 $94,\ldots,16382$ 的真实响应及其与低场的耦合；低46和参数的两端一致性；外胞元9至0；最终整个闭面及强幅度/reach 完成门。不能把原固定 $1/64$ 候选范数直接升级为本文较宽的条带，也不能从本定理反向指定一个未支付的高外端 Dirichlet 条件。

## 参考

- [R33：完整 mean 与变条带非线性源](R33-full-head-forcing-on-a-variable-analytic-strip.md)。
- [R44：兼容外高度与完整连续缺陷](R44-compatible-outer-height-and-continuous-defect.md)。
- [R61：真实 cut 与完整参数迹](R61-strong-positive-parameter-columns-and-true-cut.md)。
- [R68：最优固定 frame 的实际全频齐次预算](R68-optimal-fixed-frames-and-actual-outer-strip.md)。
- [R78：各向异性真实 cut 的复解析接口](R78-anisotropic-true-cut-holomorphic-interface.md)。
