# R225. 一个显式有理 32 模核心、全角极值与入口预算

作者：strong_recovery（AI assisted），2026-11-14。

**状态：静态核心的纯代数结论已证明，并已在 functions V8 中实际完成精确有理计算。** 本文没有求解新的 ODE 或 BVP，没有提供闭面、固定握持区、全族 reach 或刚体商幅度证书。完整 32 模定义、Laurent 尾界以及严格全角极值是本条新增内容。支撑函数与凸曲线的关系、边界 Hausdorff 恒等式沿用 [R1](R1-two-mode-core-phase-gap.md)；竖直入口的准确二 jet 和短入口见证定理沿用 [R7](R7-core-witness-initial-acceleration.md)。[R2](R2-rational-curvature-power-cores.md) 和 [R12](R12-three-harmonic-core-optimization.md) 已有其他多模构造及三谐波优化；本文不把这些一般事实、两模最优射线或 R7 门槛重新列作新发现。

## 1. 完整有限定义及定理

令
$$
t=\frac7{13},\quad A=\frac87,\quad \epsilon=\frac3{10},\quad
b_0=1,\qquad b_{k+1}=\frac{1/2-k}{k+1}b_k.
$$
对所有 $1\le n\le32$，定义准确有理数
$$
\widehat c_n=\frac{52}{35}\sum_{k=0}^{64}b_{k+n}b_k t^{n+2k},
\qquad
\widehat h(\theta)=1+\sum_{n=1}^{32}\widehat c_n\cos(2n\theta),
\qquad \widehat\rho=\widehat h+\widehat h''.
\tag{225.1}
$$
32 个系数分别包含 65 项，共 2080 个准确有理求和项；不是只指定三个低模。令 $n(\theta)=(\cos\theta,\sin\theta)$、$\tau(\theta)=(-\sin\theta,\cos\theta)$，并设
$$
\widehat C(\theta)=\widehat h(\theta)n(\theta)+\widehat h'(\theta)\tau(\theta).
\tag{225.2}
$$

**定理。** $\widehat C$ 是解析、严格凸、中心及双轴对称的平面闭曲线，周长准确等于 $2\pi$。在整个 $0<\theta<\pi/2$ 上，$\widehat h'<0$、$\widehat\rho'>0$。因此全角极值均为下列准确有理端点：
$$
\begin{aligned}
h_{\max}&=1+\sum_{n=1}^{32}\widehat c_n,&
h_{\min}&=1+\sum_{n=1}^{32}(-1)^n\widehat c_n,\\
\rho_{\min}&=1+\sum_{n=1}^{32}(1-4n^2)\widehat c_n,&
\rho_{\max}&=1+\sum_{n=1}^{32}(-1)^n(1-4n^2)\widehat c_n.
\end{aligned}
\tag{225.3}
$$
核心直径、四分之一转相位的边界 Hausdorff 距离准确为
$$
D_C=2h_{\max},\qquad
G=h_{\max}-h_{\min}
=2\sum_{\substack{1\le n\le32\\n\ {\rm odd}}}\widehat c_n.
\tag{225.4}
$$
特别地，下列有理开区间包含准确值；端点是十进有理数，不是浮点容差：
$$
\begin{aligned}
0.305097987159569376672066&<\rho_{\min}<0.305097987159569376672067,\\
4.011764622138386631892890&<\rho_{\max}<4.011764622138386631892891,\\
2.690195959931689272713600&<D_C<2.690195959931689272713601,\\
0.799999999993045493125677&<G<0.799999999993045493125678.
\end{aligned}
\tag{225.5}
$$
全部极值有理分子分母均由随附生成器准确输出；这里没有求解三角多项式的浮点驻点。

## 2. 用于证明的圆盘加椭圆比较函数

设
$$
f(\theta)=\sqrt{\cos^2\theta+\epsilon^2\sin^2\theta},\quad
\mu=\frac1{2\pi}\int_0^{2\pi}f(\theta)\,d\theta,\quad
\beta=1-A\mu,\quad h=\beta+Af.
\tag{225.6}
$$
Cauchy--Schwarz 给 $\mu^2\le109/200<9/16$，所以 $\mu<3/4$。又 $f\ge|\cos\theta|$，除离散点外严格，故 $\mu>2/\pi>7/11$。最后一个严格有理比较可由
$$
\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx=\frac{22}{7}-\pi>0
$$
直接得到。因此
$$
\frac17<\beta<\frac3{11}.
\tag{225.7}
$$
直接微分给 $f+f''=\epsilon^2/f^3$。因为 $\epsilon\le f\le1$，比较曲率半径满足
$$
\frac{43}{175}<\rho=h+h''<\frac{943}{231},
\quad h(0)-h(\pi/2)=A(1-\epsilon)=\frac45,
\quad 2h(0)<\frac{218}{77}.
\tag{225.8}
$$
比较函数中的 $\mu$ 不需要数值计算；(225.1) 的常数项已经准确固定为 1。

令 $z=e^{2i\theta}$。因
$$
f(\theta)=\frac{13}{20}\sqrt{1+tz}\sqrt{1+t/z},
\tag{225.9}
$$
且两个平方根均取从 1 延拓的解析分支，其在单位圆上的乘积为正实数，二项级数在该圆绝对一致收敛。配对相反 Laurent 次数得到
$$
h(\theta)=1+\sum_{n\ge1}c_n\cos(2n\theta),\qquad
c_n=\frac{52}{35}\sum_{k\ge0}b_{k+n}b_k t^{n+2k}.
\tag{225.10}
$$
系数 $52/35=2A(13/20)$ 已含从 Laurent 系数到余弦系数的因子 2。这里每个 $c_n$ 是无限级数，而真正候选 $\widehat c_n$ 是 (225.1) 的有限有理数，两者明确分开。

## 3. 完整尾界及保留系数的截断误差

由递推和 $b_1=1/2$，归纳得 $|b_n|\le1/(2n)$ 对所有 $n\ge1$ 成立。再由 $\sqrt{1-x}=1-\sum_{k\ge1}|b_k|x^k$，有
$$
\sum_{k\ge0}|b_k|t^{2k}=2-\sqrt{1-t^2}<2,
\qquad |c_n|<\frac{52}{35}\frac{t^n}{n}.
\tag{225.11}
$$
所以整个 $n\ge33$ 尾可分别用下列明确有理量控制：
$$
T_0=\frac{338}{3465}t^{33},\qquad
T_\rho=\frac{27716}{63}t^{33}.
\tag{225.12}
$$
准确地说，$\sum_{n\ge33}|c_n|\le T_0$，
$\sum_{n\ge33}(4n^2-1)|c_n|<T_\rho$，其中
$$
\sum_{n\ge33}nt^n=\frac{t^{33}(33-32t)}{(1-t)^2}.
$$
(225.12) 是界的定义，并没有把未知的尾和写成等式。

对每个保留模，整个 $k\ge65$ 尾满足
$$
|c_n-\widehat c_n|\le\eta_n,\qquad
\eta_n=\frac{52}{35}\frac{t^{n+130}}{1-t^2}.
\tag{225.13}
$$
这里仅用 $|b_k|\le1$ 及准确几何级数求和。定义
$$
E_0=\sum_{n=1}^{32}\eta_n,\qquad
E_\rho=\sum_{n=1}^{32}(4n^2-1)\eta_n,\qquad
\delta_0=T_0+E_0,\quad \delta_\rho=T_\rho+E_\rho.
\tag{225.14}
$$
则 $\|h-\widehat h\|_\infty\le\delta_0$、
$\|\rho-\widehat\rho\|_\infty\le\delta_\rho$。

这些有理界已实际交叉相乘验证：
$$
E_0<7\cdot10^{-31},\qquad E_\rho<10^{-27},
\qquad \delta_0<2\cdot10^{-10},\qquad \delta_\rho<10^{-6}.
\tag{225.15}
$$
可供手算核对的整数关系为
$$
7^{12}\,1600=22146059521600<23298085122481=13^{12},
\quad t^{33}<\frac{2197}{1404928000000},
\quad \sum_{n=1}^{32}(4n^2-1)=45728.
$$
生成器比较的是准确的 $T_0+E_0$ 与 $2\cdot10^{-10}$，没有先把 $T_0$ 上舍入成该阈值再错误地忽略正的 $E_0$。由 (225.8)、(225.15)，$\widehat\rho>43/175-10^{-6}>0$，并且 $|G-4/5|\le2\delta_0<4\cdot10^{-10}$。

## 4. 严格全角极值：同时控制支撑函数和曲率半径

在 $0<\theta<\pi/2$ 上，
$$
-\frac{h'}{\sin2\theta}
=\frac{A(1-\epsilon^2)}{2f}\ge\frac{13}{25}.
\tag{225.16}
$$
用 $|\sin(2n\theta)/\sin2\theta|\le n$ 及
$2n^2\le4n^2-1$，可将完整保留误差和完整未保留尾统一估计为
$$
\left|\frac{\widehat h'-h'}{\sin2\theta}\right|
\le\delta_\rho.
$$
因此 $-\widehat h'/\sin2\theta\ge13/25-\delta_\rho>0$。

曲率半径导数需要更高的完整权重，不能免费从 (225.15) 推出。原函数满足
$$
\frac{\rho'}{\sin2\theta}
=\frac{3A\epsilon^2(1-\epsilon^2)}{2f^5}\ge\frac{351}{2500}.
\tag{225.17}
$$
定义
$$
T_{\rho,1}=\frac{416}{35}\sum_{n\ge33}n^3t^n,\quad
E_{\rho,1}=\sum_{n=1}^{32}2n^2(4n^2-1)\eta_n,\quad
\delta_{\rho,1}=T_{\rho,1}+E_{\rho,1}.
\tag{225.18}
$$
由 (225.11)，完整误差满足
$$
\left|\frac{\widehat\rho'-\rho'}{\sin2\theta}\right|
\le\delta_{\rho,1}.
$$
这是因为每项导数除以 $\sin2\theta$ 的绝对值至多
$2n^2(4n^2-1)|\Delta c_n|$，未保留项再用
$2n^2(4n^2-1)(52/35)t^n/n<(416/35)n^3t^n$。
取 $N=33,r=1-t$，无限和仍是准确有理数：
$$
\sum_{n\ge N}n^3t^n
=t^N\left[
\frac{N^3}{r}+\frac{3N^2t}{r^2}
+\frac{3Nt(1+t)}{r^3}
+\frac{t(1+4t+t^2)}{r^4}\right].
\tag{225.19}
$$
实际精确比较给 $\delta_{\rho,1}<1/500$；故
$$
\frac{\widehat\rho'}{\sin2\theta}
\ge\frac{351}{2500}-\delta_{\rho,1}>0.
\tag{225.20}
$$
这就证明 (225.3) 的全部连续极值，端点值由全部 32 个有理系数求和。支撑函数在短轴的准确值严格为正。正曲率半径和双轴对称保证 (225.2) 是严格凸闭曲线；$\widehat C'=\widehat\rho\,\tau$，因此其周长
$\int_0^{2\pi}\widehat\rho\,d\theta=2\pi$。

又
$$
(|\widehat C|^2)'=2\widehat h'\widehat\rho<0
$$
于开第一象限，因此最大距离原点的半径为 $h_{\max}$；中心对称给 $D_C=2h_{\max}$。旋转 $\pi/2$ 后的支撑差在此象限为
$\widehat h(\theta)-\widehat h(\pi/2-\theta)$，其导数
$\widehat h'(\theta)+\widehat h'(\pi/2-\theta)<0$。
所以全角支撑差的最大绝对值准确为 $G$。由 R1 的凸体边界 Hausdorff 恒等式，得到 (225.4) 的距离结论。这是两个平面边界集合的距离，不是未构造的三维闭面距离。

## 5. 完整材料角及 R7 的条件性入口结论

对应周长 $2\pi$ 的准确材料角可以定义为
$$
\varphi(\theta)=\theta+
\sum_{n=1}^{32}\frac{(1-4n^2)\widehat c_n}{2n}\sin(2n\theta),
\qquad \varphi'=\widehat\rho>0.
\tag{225.21}
$$
于是按 $\varphi$ 重参数的核心速度准确为 1。所有高模均保留；没有用只含三个低模的材料角代替它。

现在额外假设存在某个 $C^2$ 等距入口 $F(s,\varphi)$，满足 R7 原条件
$$
|F_s|^2=1,\quad F_s\cdot F_\varphi=0,\quad
|F_\varphi|^2=a(s)^2,\quad a(0)=1,\quad
F(0,\varphi)=\widehat C,\quad F_s(0,\varphi)=e_z.
\tag{225.22}
$$
这些是假设，不是由静态核心自动给出的存在性结论。R7 强制 $a'(0)=0$，并在 $k_0=a''(0)$ 时给
$F_{ss}=k_0\widehat\rho\,n$、$F_{s\varphi}=0$。
在短轴取 $q=(0,h_{\min},0)$、外法向 $e_y$，以及旋转长轴点
$p=(0,h_{\max},0)=q+G e_y$。若 $0<k_0\le3/10$，完整准确有理门为
$$
k_0G\rho_{\max}\le\frac3{10}G\rho_{\max}<\frac{49}{50}<1.
\tag{225.23}
$$
在端点 $k_0=3/10$ 时，准确乘积在
$$
(0.962823509304842838261446,\;
 0.962823509304842838261447)
$$
内。R7 遂保证：对这个假设存在的入口，存在充分小的正长度，使整个短入口与闭球 $\overline B(p,G)$ 仅在 $q$ 接触。该长度没有在本文给出统一的正下界，后续片与帽仍可能遮挡见证。

同一条件下，核心处主曲率的绝对值为 $k_0\widehat\rho$ 与 $1/\widehat\rho$。全角最大值不超过
$$
\max\left\{\frac3{10}\rho_{\max},\frac1{\rho_{\min}}\right\}
=\frac1{\rho_{\min}}<\frac{41}{10}.
\tag{225.24}
$$
实际值在
$(3.277635520672870722703282,\;
3.277635520672870722703283)$ 内。
这只是入口核心的主曲率，不能给整个闭面的曲率或 reach。

## 6. 与课题最终幅度及现行 BVP 的边界

将来若一个真实相位中的点 $p$ 仍到另一相位的**全部闭面**距离至少 $G$，才可由该点得到集合 Hausdorff 下界。若想仅靠此见证达到 $D/5$，还必须准确证明
$$
D\le5G.
\tag{225.25}
$$
本核心准确预算 $5G$ 在
$(3.999999999965227465628388,\;
3.999999999965227465628389)$ 内。仅写 $D\le4$ 与 $G\approx.8$ 不能推出 (225.25)。虽然本核心自身满足 $D_C<5G$，尾、帽、握持区可能增大完整 $D$；它们也必须保持球外条件。关于所有欧氏刚体（包含反射）的最优配准距离、固定闭内点握持区、全族嵌入和 reach，本条没有给出结论。

现行 M32 的 35 参数实际 BVP只强制前三个低核心目标，另外 29 个核心模仍参与真实方程求解；它不会自动保持 (225.1) 的完整向量。新核心可作为完整静态设计或初猜输入，但若真实求解改变任何高模，必须用真实全部 32 模重算 (225.3)--(225.25) 及入口投影。不能把前三个数
$$
\widehat c_1\in(.384922791179523111791064,.384922791179523111791065),
$$
$$
\widehat c_2\in(-.049745427051346617920141,-.049745427051346617920140),
$$
$$
\widehat c_3\in(.013108380520310278890699,.013108380520310278890700)
$$
当成足以继承本条全谱证书的三个边界目标。当前已接受 A 与尚未收敛 half-positive 候选都不是 (225.1) 的核心。

## 7. 实际执行、复现与来源

独立 ASCII 源为 [r225_rational_32_core.js](../computations/r225_rational_32_core.js)，11406 字节，SHA256：
930e3c1c07e066f4865398a9e27622cfcea9035944a4513940209509cdc2c3d7。

本次实际在 functions.exec 的 V8 isolate 中先载入该原文，再调用 R225_generate()；时戳 2026-11-14T02:48:50.331Z 至 2026-11-14T02:48:50.428Z，Date.now 墙钟差 97 ms，全部 126 个显式有理门通过。所有科学比较均用约分 BigInt 分数和交叉相乘；24 位小数区间用整数向下/向上取整产生。没有以双精度小数代替证明。引擎具体版本、峰值 RSS、wait4 和终端 owned 状态均未暴露，因此不声明它们；本次没有终端、Node 进程、ODE、Jacobian、QR 或 BVP 调用。

完整可再生 JSON 有 55754 ASCII 字节，SHA256：
aaffcd79c19e7a498cf3df8200d996a62af362d7c4c2955313183cbcdbca29c9。
按根规 11，不将这份廉价可再生全分数表作为大段会话或提交数据；源、证明、小执行回执和输出 hash 足以完整复现。从 computations 目录复现可用：

```bash
node r225_rational_32_core.js > r225_rational_32_core.json
```

该命令是复现命令，不是假称本次已经执行的命令。V8 中 JSON.stringify(R225_generate(), null, 2) + "\n" 给同一输出字节。

小执行回执见 [2026-11-14-R225-rational-32-core-v8-receipt.json](../notes/2026-11-14-R225-rational-32-core-v8-receipt.json)。

先行正文已在提交 c2efbb20c47a84adbc76fdca62b250c178d0d7fe 真实只读：
R1 SHA256 acd27925c9265dd4927e02bdb06b75ff9b188f901d398c1379eac41b4aa60582；
R2 ad5fb0b81c64ed73e589c85d8fed5846c2d82a6b697bd4859426033fadb0ea17；
R7 2f1879daf29cc7eeff4c1457f47b6076547c9ff43aab41d339f411c5d9eaadd1；
R12 eb50d2a32c396a5884ea12472f899437b354f5ca5dfe43e700ddf703e5c939e6。
现行三低模接口来源 strong_actual_three_control_bvp.py SHA256
a84c8587c8ed605fdc0627c1183d79ff0afaa26d21f2b78e00c7091fa5ba6da4 亦已只读核过。
本课题 results 目录的远端 filename:R225 检索实际返回 0 件；编号最终由根代理正常登记，不据搜索结果占用其他课题的同号结果。
