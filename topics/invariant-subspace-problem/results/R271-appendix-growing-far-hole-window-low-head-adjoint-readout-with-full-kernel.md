# R271 附录：增长远孔窗口上的低强头伴随读数与完整核 forcing

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文将[原连续尾的局部伴随读数](R271-appendix-strong-head-low-hole-powers-and-continuous-tail-local-adjoint-readout.md)从固定总孔输入，扩大到“强头孔数固定、远孔数允许随远尾起点线性增长”的完整乘积窗口。常数保持不变；所有强位、原非等权远尾和完整核投影均保留。它不覆盖原 $n\asymp Q\gg m+R$ 的移动高出生窗口，也没有将返回投影换成孔投影。

## 1. 原模型、两个独立截断和结论

沿用前稿的原 N/Y 模型：
$$
C=A_m+D_<,\qquad
D_<=\sum_{m\le i<x}(i+1)^{-2}E_i,\qquad
x=m+R,\qquad h=2^m+R,
$$
$$
D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad
\mathcal L_m=C+D_x=A_m+D_{\ge m},\qquad C^h=0.
\tag{1.1}
$$
$\mathcal L_m$ 本身不依赖重新分组的 $R$。$P_{\le s}^{\rm str}$ 计算前 $x$ 个物理位的全部孔数，$P_{\le N}^{>}$ 计算第 $x$ 位以后的远孔数。两者作用在不同张量因子上。

令
$$
x\ge3072+48s,\qquad
0\le N\le\left\lfloor\frac{x}{48}\right\rfloor,\qquad
\Pi_{s,N}=P_{\le s}^{\rm str}P_{\le N}^{>}.
\tag{1.2}
$$
这不是总孔 $\le s$ 的截断；其总孔上限为 $s+N$，且 $N$ 可以随 $x$ 增长。

保留原平方强度与常数：
$$
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3},
$$
$$
\tau_x=\log\!\left(7\sqrt{\frac2{S_x}}\right),\qquad
\mathcal B_s(x)=(s+3)\sqrt{\frac2{S_x}}\,
                 e^{s\tau_x+\tau_x^{4/3}}.
\tag{1.3}
$$

存在一个原物理有界算子
$$
\mathcal G_{s,N}:\Pi_{s,N}\mathcal H\longrightarrow\mathcal H
$$
满足
$$
\boxed{
\mathcal L_m\mathcal G_{s,N}
=I_{\Pi_{s,N}\mathcal H},
\qquad
\|\mathcal G_{s,N}\|\le\mathcal B_s(x).
}
\tag{1.4}
$$
常数不依赖 $N$、强位数 $R$ 或完整幂零宽度 $h$，只保留 (1.3) 的 $s,x$。

因此对每个实际 Hilbert 向量 $y$，
$$
\boxed{
\|\Pi_{s,N}y\|
\le\mathcal B_s(x)\|\mathcal L_m^*y\|.
}
\tag{1.5}
$$
后文给出完整 MP 自然域及原核 forcing 的准确身份。

## 2. 同一个逐层右逆和同一个有限列

前稿已在每个远孔层构造一个同一选择的原连续尾右逆 $Q_{x,j}$：
$$
D_xQ_{x,j}=I,\qquad
Q_{x,j}:\mathcal H_j^>\to\mathcal H_{j+1}^>.
$$
令
$$
J_x=\left\lfloor\frac{x+1}{12}\right\rfloor.
$$
在 $j\le J_x$ 时选真正的完整层 MP 右逆，故
$$
\|Q_{x,j}\|\le\sqrt{\frac2{S_x}}.
\tag{2.1}
$$
在全部 $j\ge0$ 上，同一选择满足原 R234 的粗界
$$
\|Q_{x,j}\|\le[10000(x+j+1)^2]^{j+1}.
\tag{2.2}
$$
对低层，(2.2) 只是 (2.1) 的一个更大上界；没有在估计途中换解。

令 $\mathcal Q_x$ 按实际远孔次数拼接这些 $Q_{x,j}$。它只作用远尾，与 $C$ 交换。在有限输入次数及下述有限幂范围中，各项均有界。定义
$$
\mathcal G_{s,N}
=\left.\sum_{k=0}^{h-1}(-C)^k\mathcal Q_x^{\,k+1}
 \right|_{\Pi_{s,N}\mathcal H}.
\tag{2.3}
$$
同一有限望远镜、$D_x\mathcal Q_x^{k+1}=\mathcal Q_x^k$ 及 $C^h=0$ 直接给 (1.4) 的方程。

关键是：前稿已经付清
$$
\|C^kP_{\le s}^{\rm str}\|
\le7^k e^{-\gamma(k-s)_+^4},
\qquad \gamma=\frac{770}{256}.
\tag{2.4}
$$
此界只需要强头的输入孔数 $\le s$，不需要远孔输入也 $\le s$。对固定 $k$，不同输入远孔层 $p$ 被送到不同输出层 $p+k+1$；按 $0\le p\le N$ 直和取最大值。因此 (2.3) 第 $k$ 项的范数至多
$$
7^k e^{-\gamma(k-s)_+^4}
\max_{0\le p\le N}\prod_{\nu=0}^{k}\|Q_{x,p+\nu}\|.
\tag{2.5}
$$
这里没有额外的 $\sqrt{N+1}$ 因子，也没有把增长的远孔数放入 (2.4) 的借位阈值。

## 3. 低幂段与高幂段

### 3.1 低幂段

若 $k\le J_x-N$，则 $p+\nu\le J_x$，故 (2.1) 给
$$
\max_p\prod_{\nu=0}^{k}\|Q_{x,p+\nu}\|
\le(2/S_x)^{(k+1)/2}.
$$
这些项的和不超过
$$
\sqrt{\frac2{S_x}}\sum_{k\ge0}
e^{\tau_xk-\gamma(k-s)_+^4}
\le
(s+2)\sqrt{\frac2{S_x}}\,
e^{s\tau_x+\tau_x^{4/3}}.
\tag{3.1}
$$
最后一步与前稿相同：将四次项分成两半，使用
$$
\sup_{y\ge0}\left(\tau_xy-\frac\gamma2y^4\right)
=\frac3{4^{4/3}(\gamma/2)^{1/3}}\tau_x^{4/3}
\le\tau_x^{4/3},
$$
以及 $\sum_{\ell\ge1}e^{-(\gamma/2)\ell^4}<1$。

### 3.2 高幂段

若 $k>J_x-N$，因为 $k,N$ 是整数，
$$
k>\frac{x+1}{12}-N
\ge\frac{x}{16}+\frac1{12}.
$$
特别，
$$
k\ge\frac{x}{24},\qquad k\ge128,\qquad
N\le\frac k2,\qquad s\le\frac k2.
\tag{3.2}
$$
后两式分别使用 $N\le x/48$ 和 $x\ge3072+48s$。所以 (2.2) 给
$$
\max_p\prod_{\nu=0}^{k}\|Q_{x,p+\nu}\|
\le
[10000(x+N+k+1)^2]^{(k+1)(N+k+1)}.
\tag{3.3}
$$
由 (3.2)，
$$
x+N+k+1\le28k,\qquad
(k+1)(N+k+1)\le2k^2.
$$
故 (2.5) 的对数不超过
$$
-\frac{\gamma}{16}k^4
+k\log7+2k^2(16+2\log k).
$$
对 $k\ge128$，后两项之和不超过 $k^3$，继而不超过
$\gamma k^4/32$。高段因此被 $e^{-\gamma k^4/32}$ 支配，总和小于 $1$。

结合 (3.1)，并用
$\sqrt{2/S_x}e^{s\tau_x+\tau_x^{4/3}}\ge1$，即得
$$
\|\mathcal G_{s,N}\|
\le (s+3)\sqrt{2/S_x}e^{s\tau_x+\tau_x^{4/3}}
=\mathcal B_s(x).
$$
高段中出现的是增长的 $N$；(3.2) 正是保证它仍可由同一个四次借位预算吸收的依据。

## 4. 完整核投影在局部 Green 中的准确位置

将 $\mathcal G_{s,N}$ 视为 $\mathcal G_{s,N}\Pi_{s,N}$，则 (1.4) 的伴随恒等式是
$$
\boxed{
\Pi_{s,N}=\mathcal G_{s,N}^*\mathcal L_m^*.
}
\tag{4.1}
$$
它在整个实际 Hilbert 空间上成立，给出 (1.5)。

令
$$
\mathscr K_m=\ker\mathcal L_m.
$$
对标准自然域
$$
f\in\operatorname{Ran}\mathcal L_m^*
          \oplus\ker\mathcal L_m
=\operatorname{Dom}(\mathcal L_m^*)^\dagger,
$$
取 $y=(\mathcal L_m^*)^\dagger f$。则
$$
\mathcal L_m^*y=(I-P_{\mathscr K_m})f.
$$
所以不仅有范数界，还有准确同源身份
$$
\boxed{
\Pi_{s,N}(\mathcal L_m^*)^\dagger f
=
\mathcal G_{s,N}^*(I-P_{\mathscr K_m})f,
\qquad
\|\Pi_{s,N}(\mathcal L_m^*)^\dagger f\|
\le\mathcal B_s(x)\|f\|.
}
\tag{4.2}
$$
右边保整个 $\mathscr K_m$ 的物理正交投影。它不将 forcing 换成 $\Pi_{s,N}f$，也不预先缩短核或强位 nuisance。

(4.2) 给左边在全部 Hilbert 输入上的有界延拓。此延拓不依赖所选可行右逆：若另一右逆 $\widetilde{\mathcal G}$ 也满足 (1.4) 的方程，则
$\operatorname{Ran}(\mathcal G_{s,N}-\widetilde{\mathcal G})
\subseteq\mathscr K_m$，故
$$
(\mathcal G_{s,N}-\widetilde{\mathcal G})^*
(I-P_{\mathscr K_m})=0.
$$
因此这个低输出算子仍是完整 MP 的局部读数，未由候选代替真正最小者。

## 5. 原返回接口的适用边界

本文的实际增益是 $N$ 可取至 $\lfloor x/48\rfloor$，而成本不随 $N$ 增长。对固定 $s$，
$$
\log\mathcal B_s(x)=O_s((\log(x+1))^{4/3}).
$$
这不是固定多项式 $x$ 成本。

它可以读取同一个完整伴随解在这些低强头、增长远孔层上的分量；它仍不是整个解的范数界。特别：

- 原返回列满足的是正向方程
  $(C+D_x)\mathcal Rr=-P^{\rm hi}\mathcal TJ_br$；
  不可将 (4.2) 直接乘这个残量当作返回范数。
- 原返回测试还含真实 $P_{\widehat{\mathscr E}}$ 和全部零源 Schur。该投影一般不保强头孔数，不能替换为本文的 $\Pi_{s,N}$。
- 强联块的原主要高出生窗口是 $n\asymp Q\gg x$，不在 (1.2) 内。即使选择较小 cut，也须保所有右段和普通末端；$h=2^m+R\ge m+R=x$，因此整个 $h$ 段不能落入 $N\le\lfloor x/48\rfloor$ 的低远孔窗口。
- 若与原全局 $T$ 配对，$T-\mathcal L_m$ 的跨位 carry 及同一 $W$ 来源仍须真实运输。

因此本稿扩展的是完整局部伴随读数的已付区域；原普通封口、返回混合配对及 $N=M$ 不因本稿关闭。
