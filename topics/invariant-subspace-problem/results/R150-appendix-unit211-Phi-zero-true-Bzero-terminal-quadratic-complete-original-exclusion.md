# 正确 $\Phi=0,\ B=0$ 终端二次权因子的整原值排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：literature_deddens；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 本稿在当前 $D_{\mathrm{val}}\ne0$ 的正确原 $\Phi=0,\ B=0$ 图上，排除整个
$$
\phi_2(x)=2x^2+4x-1=0.
$$
结合[终端 $C_{76}$ 原覆盖](R150-appendix-unit211-Phi-zero-true-Bzero-terminal-C76-original-ideal-cover.md)，剩余不同权对上界由 $76$ 降为 $74$。两个剩余次数 $34,40$ 的因子及其全部原纤维保留。本稿不宣称整个 $B=0$ 已闭。

## 1. 原图和全部二次嵌入

沿用[正确整 $B$ 的十二行两列来源](R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)。有理权图为
$$
u=\frac{(x+1)^2}{3x},\qquad
Q=\frac43(x^2-x+1),\qquad
\ell=\frac{(x+1)(5x-1)}{6x^2}.
$$
所有原分母仅沿既有完整排除支付；特别不倒旧未付的 $H_3$。在这条图上
$$
\ell-\frac12=\frac{2x^2+4x-1}{6x^2},
$$
故本次二次因子也是这条 $B$ 图内的整 $\ell=1/2$ 纤维。此说明不借用已撤回的旧 $\Phi$ 半权结论。

令
$$
K=\mathbb Q[x]/(x^2+2x-\tfrac12).
$$
判别式 $6$ 非有理平方，所以 $K$ 是完整二次域。程序以 $a+bx$ 的两个有理坐标运算；其共轭与范数分别为
$$
\overline{a+bx}=a-2b-bx,\qquad
N(a+bx)=a^2-2ab-\tfrac12b^2.
$$
每次实际逆都在两个坐标中乘回，保留两个复嵌入。没有选一个数值根。

新源只取既有正确原四式、首一 $\omega$ 二次和原坐标映射的必要定义；不再构造旧 $C_{76}$ 或 $C_{315}$。个别原 $NS,PS$ 在这个完整常数域中首次返回，得到六个真正原余式
$$
r_i=a_i(\lambda)+b_i(\lambda)\omega,\qquad i=0,\ldots,5,
$$
与首一
$$
q_\omega=\omega^2+q_1(\lambda)\omega+q_0(\lambda).
$$
本次 $q_0,q_1$ 的实际 $\lambda$ 次数均为一。六行的两列次数依次是
$$
(3,3),(3,3),(3,3),(2,2),(5,5),(5,5).
$$

## 2. 真正原 $\lambda$ Bézout，保留平方重数

对全部十五对 $(i,j)$，定义固定原 cofactor
$$
c_{ij}=a_i b_j-a_j b_i.
$$
逐对实际返回
$$
b_jr_i-b_ir_j=(c_{ij},0).
$$
随后在完整 $K[\lambda]$ 中做欧氏 Bézout，并把组合返回六条原行的两坐标。得到的准确首一 gcd 为
$$
\boxed{\quad g(\lambda)=(\lambda-\tfrac12)^2.\quad}
\tag{1}
$$
全部原 cofactor 的 $\lambda$ 次数（零式记为 $-1$）为
$$
-1,-1,5,6,6,-1,5,6,6,5,6,6,7,7,8.
$$
返回的是实际六原式组合 $(g,0)$，所以 $g$ 属于原理想。没有以只看 common-zero 必要条件代替该来源，也没有把平方约成一次。

## 3. 完整八维原代数中的正单位目标

考虑整个
$$
\mathcal A=K[\lambda,\omega]/(g,q_\omega).
$$
这是一个 $\mathbb Q$ 维数为八的代数，基可以取
$$
x^a\lambda^j\omega^k,\qquad a,j,k\in\{0,1\}.
$$
它保留 $\lambda=1/2$ 的全部幂零信息，并且没有对 $q_\omega$ 取根或平方自由化。

将六条 $r_i$ 各乘这八个完整基元素，得到真正原理想的 $8\times48$ 有理矩阵。其真实 rank 为四，余商维数为四。**此原理想没有返回常数一。**

程序只用 rref 选择实际原列，随后在选出的 $4\times4$ 子式上求精确逆，双向乘回；并将全部 $48$ 列在完整八坐标中返回。选择的是原列 $0,1,2,3$、系数行 $0,1,2,3$，不是 Gaussian 中间余列。

原物理目标取
$$
U=\lambda tD_{\mathrm{val}},
\qquad
D_{\mathrm{val}}=\ell(2\lambda^2-2\lambda+1)-T^2
=bc(h_U-k_U)^2.
\tag{2}
$$
$t,T$ 都使用同一个原坐标映射；目标乘法及 $\omega$ 短除在 $\mathcal A$ 中完整返回。实际结果为
$$
1\notin(r_0,\ldots,r_5)\mathcal A,\qquad
\boxed{\quad U\in(r_0,\ldots,r_5)\mathcal A.\quad}
\tag{3}
$$
正幂次数恰为一，八个有理目标坐标全部乘回。

由于 $g$ 本来就是六原行的组合，$q_\omega$ 本来就是原四式的组合，(3) 从 $\mathcal A$ 返回完整原 $I_6$。在当前图内，$\lambda$ 由非零孤立 mean 规范支付，$t$ 由正确整 $t=0$ 排除支付，$D_{\mathrm{val}}$ 是当前 distinct-simple-value 范围的原单位。故 (3) 与原点存在矛盾，整个 $\phi_2=0$ 排除。

全程只将 $D_{\mathrm{val}}$ 作为正目标相乘，没有倒其范数。这里的 rank 四及余商维数四不被误写为裸原代数为空；排除依赖准确的物理单位范围。

## 4. 剩余权覆盖

旧终端多项式的完整 QQ 因式为
$$
C_{76}=\text{非零常数}\cdot\phi_2F_{34}F_{40},
$$
三个因子均一次。新定理去掉整个 $\phi_2$ 原纤维，因此当前 $B=0$ 原权必须满足
$$
F_{34}(x)F_{40}(x)=0.
$$
所以至多 $74$ 个不同 $x$，相应至多 $74$ 个不同 $(u,Q)$ 权对。此处只有不同权点数界；没有给两个剩余因子的完整几何纤维计数或判空。

## 5. 唯一实际执行与来源

本次新源：
[2026-11-28-unit211-Phi-zero-true-Bzero-terminal-quadratic-original-return-8542.py](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-terminal-quadratic-original-return-8542.py)。

- 源 blob：70176725e3e22b60252a20409b8ca74fbaf7f868。
- SHA256：a60dbe5808c0b2408ad4d3a0ac40f8c801ce9ade6fb3eb316a2d7bce7c059c4a。
- Actions run：46120369360；job：140903335008；内层 exit $0$。
- 驱动时间：0.343444863 秒；峰值子进程 RSS：42340 KiB。
- 源提交及真实 pull：e59d51b4d5b2c15f0e7f8afb39144581c9f04ac1。
- 2026-11-28 07:15:47.297353 UTC 两 README 真实读取且无变化。
- stdout：2815 字节；SHA256 342fca68780195e51423fc30789d9c8aea7041c0c9a9752c315752f63d55e9e4。

实际返回包括：六条原行、三十个 cofactor 坐标、十二个 Bézout 坐标、三十二个双逆坐标、全部 $384$ 个原理想列坐标和八个正目标坐标。两个二次嵌入及全部重数由同一完整有理代数覆盖；不需要再播放任何已成证书。
