# R150：S0、Lt0 的原 theta 伪余式双零面完整排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-27（Asia/Taipei）。

**状态：已证明。** 在原三值互异图 $S=0,L_t=0,L\ne0,A_f\ne0,J\ne0,g_2\ne0$ 上，原 theta 伪余式两个系数同时为零的整个面不存在物理临界点。完整的 82 次 lambda 覆盖已经返回，最后 43 个 lambda 参数和两个 theta 根、两个原 d 根同时在 172 维代数中保留。原 $E_1,E_B$ 的 $t$ 结果式是真正单位。

这关闭此前 HANDOFF 所列 $R_0=R_1=0$ 例外；一般非零线性伪余式图仍开，普通 Hilbert ISP 仍未完成。

## 1. 同一原图的两条必要方程

记号与 [原 theta 首项零面排除的 §1](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-theta-leading-zero-exclusion.md) 完全相同。共同规范为 $p+q=2$，并记

$$
s=2\lambda-3,\ A=2\lambda^2-2\lambda+1,\ C=-4\lambda^2+5\lambda-2,\ R=3-4\lambda,
$$

$$
D=sC-Az,\quad \Delta=s^2-4z,\quad B=2Cz-Ds,
$$

$$
U=D+\theta B,\quad V=U-z^2,\quad Q=1-\theta^2\Delta,
$$

$$
W=(\lambda-1)z-C,\quad E=D+Cz,\quad T_n=-4V-z^2Q,
$$

$$
Y=2(Ds-Cz)+\theta(Bs-D\Delta).
$$

从原 $P_1$ 的 $t$ 系数和原 $P_1,N(V)$ 兼容性得到

$$
G=z^2(z^2-D)Q-2V(V-z^2)=0,
\tag{1}
$$

$$
K=z^3(R-z)(-T_n^2+2DEQ^2-2\lambda DQT_n)
 +8DEQV^2-2VT_nWY=0.
\tag{2}
$$

$G=g_2\theta^2+g_1\theta+g_0$ 的三个原系数为

$$
g_0=-(D-z^2)(2D-3z^2),\quad g_1=-2B(2D-3z^2),
$$

$$
g_2=z^2(D-z^2)\Delta-2B^2.
\tag{3}
$$

小 $J$ 由完整多项式身份

$$
B^2-\Delta(D-z^2)^2=z^2J
\tag{4}
$$

给出，正是既存 $J=0$ 排除中使用的同一多项式。

$K$ 的 theta 次数为四。连续三次对 (1) 作未除首项的伪除法，得到

$$
g_2^3K=Q_\ast G+r_0+r_1\theta.
\tag{5}
$$

这里 $Q_\ast$ 为多项式，$r_i\in\mathbb Q[\lambda,z]$，精确公共因子为

$$
\gcd(r_0,r_1)=z^5J/192.
\tag{6}
$$

故在本图上，$r_0=r_1=0$ 等价于两条原参数式 $F=H=0$：先以 (6) 分别相除，再仅去掉独立于 theta 的已付单位的 gcd 因子。源码所使用的单位表是

$$
\lambda,z,\Delta,J,g_2,D,D^2\Delta-B^2.
\tag{7}
$$

最后一项来自原 $bc\ne0$。没有剥掉任何依赖 theta 的单位范数，两个 theta 根仍全部保留。两个必要式的次数为

$$
(\deg_\lambda F,\deg_zF)=(23,13),\qquad
(\deg_\lambda H,\deg_zH)=(24,13).
$$

## 2. 完整有限覆盖及九个因子的返回

原 QQ 结果式 $\operatorname{Res}_z(F,H)$ 的 lambda 次数为 377，平方自由部分为 82 次。完整分解的各首一因子为

$$
\lambda-13/18,\quad\lambda-1/2,\quad\lambda-3/2,
$$

$$
\lambda^2-5\lambda/4+1/2,\quad
\lambda^2-1/2,\quad
\lambda^2-\lambda+1/2,\quad
\lambda^2-5\lambda+7/2,
$$

$$
\lambda^4-157\lambda^3/35+1221\lambda^2/140-257\lambda/35+229/105,
\quad\Phi_{24},\quad\Phi_{43}.
\tag{8}
$$

$\Phi_{24}$、$\Phi_{43}$ 分别定义为该完整平方自由分解中唯一的首一 24 次、43 次因子。自含源码从 (1)–(7) 重新生成其全部有理系数，验证分解乘积；并输出低次系数在前的完整列表。因此这里没有把一个仅凭数值猜出的参数多项式当作来源。

完整平方自由部分的 SHA-256 为

```
f3610eb65af548b799ac0c88030537da37741ab20f65d29a7b109c25da3c0dfe
```

$\Phi_{24}$ 与 $\Phi_{43}$ 的低次在前系数列表 SHA-256 分别为

```
b39d8f3a7f57c23fe0ce11019275d91e42ff87c83b0d318b8b0684d52f9cd77c
7c5e01fcffebba57c44403b53244405c1eeafcf105e29a58a5d798dfb3e232f9
```

为避免高次数域中直接 Euclidean 除法的系数膨胀，先在 $\mathbb Q[\lambda][z]$ 上完整生成 subresultant 链，再专门化到每个 (8) 的完整商代数。所有精确商均回乘。低次数谱处可能发生原首项降次，故对前八个因子仍计算**两条原 $F,H$** 的完整扩展 gcd；不能直接把异常专门化的一个 subresultant 宣称为 gcd。

返回结果如下，每次所用逆、多项式除法与 Bézout 身份都在完整原代数中乘回。

| 原 lambda 因子 | 剩余 z 因子被何种已付单位吸收 |
|---|---|
| $\lambda-13/18$ | $J$ 的一次因子 |
| $\lambda-1/2$ | $\Delta$ 的一次因子，三次 |
| $\lambda-3/2$ | $z$，五次 |
| $\lambda^2-5\lambda/4+1/2$ | $z$，六次 |
| $\lambda^2-1/2$ | $\Delta$ 的一次因子，两次 |
| $\lambda^2-\lambda+1/2$ | 原 $F,H$ 的 gcd 本身为 1 |
| $\lambda^2-5\lambda+7/2$ | $z$，一次 |
| (8) 中的四次因子 | $J$ 的一次因子，两次 |
| $\Phi_{24}$ | 最后非零必要 subresultant 为 z 一次式，完整落在 $g_2=0$ |

每一行去掉的都是 (7) 的原单位；九行最后余 z 次数均为零。共实际验证 211 个代数逆、165 条多项式除法和 46 条 Bézout 身份。

## 3. 唯一剩余的 43 次参数与完整二次塔

令

$$
\mathbb K=\mathbb Q[\lambda]/(\Phi_{43}).
$$

该谱上最后非零必要 subresultant 为

$$
S_1(\lambda)z+S_0(\lambda)=0,
$$

且 $S_1$ 的实际 extended-gcd 逆存在。故所有原点都满足唯一

$$
z=-S_0S_1^{-1}\in\mathbb K.
\tag{9}
$$

源码把 (9) 重新代回原 $F,H$，两者都为零，并逐个验证 (7) 在这整个 43 维代数中为单位。定义

$$
\beta=-g_1/g_2,\qquad \kappa=-g_0/g_2.
$$

保留完整代数

$$
\mathcal B=\mathbb K[\theta]/(\theta^2-\beta\theta-\kappa),\qquad
\mathcal C=\mathcal B[d]/(d^2-\Delta).
\tag{10}
$$

其 $\mathbb Q$ 维数为 $43\cdot2\cdot2=172$。不要求任何一个二次多项式不可约，也没有任取某个 theta 根或 d 根。

在 (10) 中精确重建同一个物理参数：

$$
\ell=D/z^2,\quad T=C/z,\quad B_v=2T-\ell s,\quad w=\lambda-1-T,
$$

$$
b=\ell/2+B_vd/(2\Delta),\quad c=\ell/2-B_vd/(2\Delta),
$$

$$
p=1+\theta d,\quad q=1-\theta d,\quad
h=1+(s+d)/2,\quad k=1+(s-d)/2.
\tag{11}
$$

令 $u=\ell+\theta B_v$、$Q=pq$、$V_2=2u-\ell Q$、$T_0=V_2-2u^2$。原 (1) 给

$$
P_{02}=2P_0=2\ell Q(u-1),\qquad T_0+4(u-1)+Q=0.
$$

原 $P_1$ 的 f 系数在本图非零；其与 (2) 的同源值是

$$
f=\frac{-T_0^2+2\ell Q^2(\ell+T)-2\lambda\ell QT_0}{4(u-1)T_0}.
\tag{12}
$$

所有在 (11)、(12) 及原 Gram 重建中实际使用的分母均在 (10) 中算出真逆。尤其 theta 依赖的 $Q,u,u-1,T_0,L,A_f$ 等也真正可逆；没有把它们范数为零的纤维静默丢掉。

## 4. 原九式的单位证书

从 (11)、(12) 的同一原 Gram、原 Frobenius 乘法与原迹，重新生成九条原 $t$ 多项式

$$
E_1,E_B,E_C,P_1,P_B,P_C,N_1,N_B,N_C\in\mathcal C[t].
$$

同一原 $E_0$、最高基值、$N_0$、三个 U 矩、$P(V)$、$N(V)$ 均实际校验。原 $P_1$ 确实恒零，九式的 $t$ 次数依次为

$$
2,2,2,-1,3,3,2,3,3.
\tag{13}
$$

这里 $-1$ 表示零多项式。原九式规范系数序列 SHA-256 为

```
660ebc7709c05b106d07ca28da21d237edd7effd7c12b4dd18008e92c60be04a
```

取**原** Sylvester 行列式

$$
\mathcal R=\operatorname{Res}_t(E_1,E_B)\in\mathcal C.
$$

任何共同有限 t 都迫 $\mathcal R=0$，包括首项降次的点。实际计算写成 $\mathcal R=a+bd$，其中 $a,b\in\mathcal B$，并取

$$
n=a^2-\Delta b^2=n_0+n_1\theta.
$$

它的第二层范数为

$$
N=n_0^2+\beta n_0n_1-\kappa n_1^2\in\mathbb K.
$$

源码求得 $N$ 的真实 extended-gcd 逆，在完整原代数中构造

$$
\mathcal R^{-1}
=(a-bd)\,(n_0+\beta n_1-n_1\theta)N^{-1}
$$

并直接验证

$$
\boxed{\mathcal R\,\mathcal R^{-1}=1.}
\tag{14}
$$

所以原 $E_1,E_B$ 没有共同 t；整个原九式当然没有解。逆的规范序列 SHA-256 为

```
f05fa352bf636c6b0a31b1605b871e623f34bbf14ef9cc194285fee9979959f3
```

末层完成 27 个基础代数逆及 17 个 theta 代数逆身份。第 2 节九个因子与 (14) 合并，覆盖全部 82 次参数谱及全部两个 theta、两个 d 根，故原 $r_0=r_1=0$ 面完整排除。

一个直接的后续接口是：在仍未闭的 $g_2\ne0$ 原图上，(5) 与本结论迫 $r_1\ne0$；否则也有 $r_0=0$，与本条矛盾。因此所有剩余原点都可以合法写成 $\theta=-r_0/r_1$。这只是把除法例外完整付清，一般图尚未排空。

## 5. 源码、参数与实际执行

- 自含源码：[2026-11-27-unit211-S0-Lt0-theta-remainder-zero-complete-return-8542.py](../notes/2026-11-27-unit211-S0-Lt0-theta-remainder-zero-complete-return-8542.py)，19,424 字节；从 (1)–(7) 开始重建，不读外部系数数组。
- 源 SHA-256：`7676916844285f11026a8a606ef2b084cbc83e3e5c8e6b9625b0c86e9880bd73`。
- Python、python-flint 0.9.0，源内 alarm 180 秒；本次实际 exit 0，26.732127 秒，峰值 RSS 49,952 KiB。
- stdout SHA-256：`d2855f87523bb9d3b6df21a8df17014f0aa5c786aca9b4434586ee2e1079e3ee`。
- 小回执：[2026-11-27-unit211-S0-Lt0-theta-remainder-zero-execution-8542.json](../notes/2026-11-27-unit211-S0-Lt0-theta-remainder-zero-execution-8542.json)。只保存源、参数、哈希、各谱返回和小回执；subresultant 大系数数组仅作临时计算，未入库。

本轮先实际执行此前尚无完成回执的直接数域 gcd 源。它已完成 377/82 次覆盖及八个低谱，在高次数域阶段仍运行；随后因更低成本的 QQ subresultant 方法已经取得完整返回而主动中断（exit130）。这次未完成尝试没有被改记为成功，正式证据仅为上述另一份自含源的真实 exit0 和 (14)。
