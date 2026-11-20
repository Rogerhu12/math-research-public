# R937 — 原标记权 34 的有限 Hecke 核与单位首项

状态：严格的有限整数计算及其模 $p$ 推论。主目标仍 OPEN；本条不排除下面列出的有限坏素数，也不把 Legendre 双因子非共同零直接升级为最终同标签临界积结论。

## 1. 命题与原标签

设 $p\ge41$、$p\equiv5\pmod {12}$，并保留 R317 所需的实际允许类及全部原标记。置
$$h=(p+33)/2,\qquad r_+=32,\qquad k_+=34.$$
由 R935，$h\equiv1\pmod6$ 且 $\gcd(h,p+1)=1$。其原 full-Norm 角色、两 Igusa 分量与固定 $\zeta^2$ 相位均不改。

定义固定正整数
$$
\begin{aligned}
D_{34}&=6257370208079794820150643464381912640000000000000,\\
C_{34}&=1350702136960,\qquad B_{34}=D_{34}C_{34}.
\end{aligned}
$$
若 $p\nmid B_{34}$，则原标记权 $34$ 分支内 $\ker T_5$ 是一维，恰由 R913 已有的具名 CM 伴随形式 $V_{34}^{\dagger}$ 生成。该分支内任何非零且被 $T_5$ 杀死的实际 primitive Hodge layer 都是这条线的非零标量倍。在原 $j=0$ 标记上，$V_{34}^{\dagger}/E_4$ 是单位，故具有恰一个 $E_4$ 零；其 fine Igusa 局部微分阶为 $2p-35$。

所有源层和标记均在原模型上比较，不更换 Legendre 参数或原 Tate index $a_h$。

## 2. 六维整数格与五行 Hecke 映射

令 $s^2=-3$、$H=\eta(6\tau)^{12}$，采用 R913/R918 固定的 $Q$ 展开。R935 的整数基在 $p\ge41$ 可作单位 gauge 改基为
$$
G_a=V_4^\dagger E_6^{5-a}(sH)^a,\qquad 0\le a\le5.
$$
R935 已证明这六项构成整个所需原权 $34$ 分支的整格；以下不是只在预选子空间中求核。

在 $\mathbf Z[s]$ 中使用
$$
\begin{aligned}
F_4(Q)&=Q\prod_{m\ge1}(1-Q^{3m})^8,\\
V_4^\dagger(Q)&=F_4(Q)+8(1+s)F_4(Q^4),\\
E_6(Q^6)&=1-504\sum_{n\ge1}\sigma_5(n)Q^{6n},\\
H(Q)&=Q^3\prod_{n\ge1}(1-Q^{6n})^{12}.
\end{aligned}
$$
对于权 $34$ 的 $f=\sum a_nQ^n$，原 Hecke 算子满足
$$
[Q^n]T_5f=a_{5n}+5^{33}a_{n/5},
$$
其中 $5\nmid n$ 时第二项为零。仅取 $n=2,5,8,11,14$，全部输入只需到 $Q^{70}$。

这些行在 $n$ 为偶数时是纯 $s$ 倍，为奇数时是整数。偶行除以单位 $s$ 后得到整数 $5\times6$ 矩阵 $M$，列顺序为 $G_0,\ldots,G_5$。上述有限乘积和系数规则唯一确定 $M$。

公开 Actions 的精确整数计算给出：$M$ 的六个有符号 $5\times5$ 子式的绝对最大公因数为 $D_{34}\ne0$，规范化整数核向量为
$$
K=(1,\ 8589934584,\ -598636628352,\ -960436528128,\
80267404107534336,\ -8839287829466873856).
$$
计算逐项验证 $MK=0$；有符号余子式向量是 $\pm D_{34}K$。因此
$$
\operatorname{rank}_{\mathbf Q}M=5,\qquad
p\nmid D_{34}\Longrightarrow
\ker(M\bmod p)=\mathbf F_p K.
$$
完整 $T_5$ 核包含于这五行的核，所以这是对完整核的上界，不使用模 $p$ Hecke 半单性。

## 3. 识别实际具名 CM 源

R913 在同一原标记分支给出的归一化形式为
$$
V_{34}^{\dagger}=F_{34}(Q)-2^{34}\zeta^2F_{34}(Q^4).
$$
它的 $Q$ 一次项为 $1$，而 $5$ 在 $\mathbf Q(\sqrt{-3})$ 惰性，所以 $T_5V_{34}^{\dagger}=0$。该具名形式并非由有限 Fourier 行猜出的候选。

在特征零，它属于 $\ker M$。六基中只有 $G_0$ 的 $Q$ 一次项非零，且等于 $1$，从而归一化强制整格恒等式
$$
\boxed{\displaystyle V_{34}^{\dagger}=\sum_{a=0}^{5}K_aG_a.}
$$
独立首项核对为 $K_1=2^{33}-8$：结合 $G_0$ 的 $Q^4$ 系数 $8s$，右侧 $Q^4$ 系数是 $2^{33}s$，与原 CM 伴随形式一致。

约化后该形式的 $Q$ 一次项仍为 $1$。当 $p\nmid D_{34}$，完整 $T_5$ 核包含这条非零线，又包含于一维 $\ker M$，所以恰为该线。R916/R913 给实际 $h$ 的 primitive Hodge layer 非零并被 $T_5$ 杀死；R935 将其放入这里的完整六维原分支。因此其等于
$$
u_h\,\Phi_{34}(V_{34}^{\dagger}),\qquad u_h\ne0.
$$
这里保持实际 $h$ 的原 $a_h$，没有由任何未知低系数的非零性代替 primitive layer 的来源。

## 4. 原标记的精确单位值

R920 在原标记固定 $E_6/H=-24s$，故 $sH/E_6=-1/24$。因此
$$
\left.\frac{V_{34}^{\dagger}}{E_4}\right|_{\rm mark}
=
\left(\sum_{a=0}^{5}K_a(-1/24)^a\right)
E_6^5\left.\frac{V_4^{\dagger}}{E_4}\right|_{\rm mark}.
$$
精确有理数求值给
$$
\sum_{a=0}^{5}K_a(-1/24)^a
=C_{34}
=2^7\cdot5\cdot11\cdot17\cdot41\cdot71\cdot3877.
$$
R918/R920 已证明原标记 $E_6$ 与 $V_4^\dagger/E_4$ 均为单位。所以 $p\nmid C_{34}$ 时恰有一个 $E_4$ 零，实际 primitive Hodge layer 亦然；按原 Igusa 换算，fine 微分阶为 $2p-k_+-1=2p-35$。

在 $p\equiv5\pmod {12}$、$p\ge41$ 的范围中，$C_{34}$ 列出的素因子只有 $41$ 落在该类。命题仍统一保留 $p\nmid B_{34}$，不自动解决任何例外。

## 5. 固定坏整数与实际计算来源

$D_{34}$ 的已验证部分分解为
$$
2^{18}3^8 5^{13}7^2\cdot11\cdot491\cdot11261638355344994412032893.
$$
末因子没有被宣称为素数或已完全分解。所有可能例外都是显式固定整数 $B_{34}$ 的素因子。

本次唯一新算术在本仓库公开 Actions 执行：

- source commit：d051e06c3453f8f78e3584e14155fc6f43de42c5。
- [run 44713602498](https://github.com/Rogerhu12/math-research-public/actions/runs/44713602498)，job 136211233497，success。
- [脚本](../scripts/weight34_inert_hecke_row.py)，SHA256 b4265e5314a248dac3c1ffac63a2a4a29b63d75db1ba388ff90b1892bd799556。
- 参数：--output /tmp/weight34-inert-hecke-row.json。
- 确定性输出 SHA256：6d0e4c5d0ef8c928456b74e25ad4e04e795d16a952258b8bacee1f18ce4efa2d。

本地只作 AST、IO 和字节哈希。完整可再生矩阵、JSON 及输出数组不入 Git 或 Release；上面保留数学结论与重现参数。

同一公开 run 给出 R935 的固定递推整数
$$
a_{11}=14958957622875578640
=2^4\cdot3^5\cdot5\cdot769493704880431.
$$
末余因子同样未宣称为素数。$a_{11}$ 控制两个 Legendre 因子不共同为零，$B_{34}$ 控制本条的 Hecke 核与原标记单位，两者用途不同。原 normal 低层排除、同标签 $Q'_h(0)$、完整配对来源比较及全局 height 均须另证。

## 依赖

R913 的原 CM theta/Hecke 与相位；R916 的实际 primitive Hodge layer；R918/R920 的完整原分支、标记与 Igusa 换算；R935 的完整权 $34$ 整格及两个本原标签。没有改动任何已登记的来源尺度、两 Igusa 分量或 full-Norm 因子。
