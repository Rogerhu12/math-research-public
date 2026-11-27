# R150：S0/Lt0 一般图的参数曲线首项零纤维完整返回

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127 / r150_open_geometry；AI-assisted GPT-6 Astra Pro。

**已完成的结论。** 在 S0、三值互异、Af 非零、Lt0 的原系统中，先前已闭的 J0、g2 零面及原 theta 伪余式双零面之外，参数曲线 M(lambda,z)=0 的 z 首项零纤维全部无原解。这个首项恰为

$$
\operatorname{lc}_z M=(4\lambda-1)^2(2\lambda^2-2\lambda+1)^4.
$$

本次同时返回 lambda=1/4 及 2lambda^2-2lambda+1=0 的两谱。完整原代数分别为 22 维与 40 维；两者的原均值结果式 Res_t(E1,EB) 均有实际回乘为 1 的逆。故后续处理一般 M 图时可合法支付此首项。**一般 M 图其余点、整个 S0 与 ISP 尚未因此关闭。**

## 1. 原参数输入与覆盖

沿用 [原 theta 首项零排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-theta-leading-zero-exclusion.md) 与 [原 theta 伪余式双零排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-theta-remainder-zero-exclusion.md) 的归一化、原九式和单位。置

$$
s=2\lambda-3,\quad A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,\quad D=sC-Az,
$$
$$
\Delta=s^2-4z,\quad B=2Cz-Ds,\quad
U=D+\theta B,\quad V=U-z^2,\quad Q=1-\theta^2\Delta,
$$
$$
W=(\lambda-1)z-C,\quad E=D+Cz,\quad T_n=-4V-z^2Q,
\quad Y=2(Ds-Cz)+\theta(Bs-D\Delta).
$$

原 Lt0 和原 P1/N(V) 兼容给出

$$
G=z^2(z^2-D)Q-2V(V-z^2)=0,
$$
$$
K=z^3(3-4\lambda-z)(-T_n^2+2DEQ^2-2\lambda DQT_n)
 +8DEQV^2-2VT_nWY=0.
$$

写 G=g2 theta^2+g1 theta+g0，以 g2 作三步无除法伪除：

$$
g_2^3K=Q_*G+r_0+r_1\theta.
$$

实际公因子为 z^5 J/192。令 F、H 为 r0、r1 除此共同因子的结果。因 J、z、g2 非零且原余式双零例外已闭，原解上 H 非零，故

$$
\theta=-F/H.                                      \tag{1}
$$

这不是以一般位置代替零纤维；先前完整返回恰支付了 (1) 的遗漏边界。

本次源从 G、K 重新生成整个必要结果式，并实际逐项验证完整恒等式

$$
\operatorname{Res}_{\theta}(G,K)=256z^{14}J^2M(\lambda,z).
$$

其中 M 的次数 (deg_lambda,deg_z)=(26,12)。z=(h−1)(k−1) 由三值互异图中的 h1/k1 已闭边界支付；J=0 已由原小 J 全返回关闭。因此除去 z、J 后，M 确实覆盖整个剩余原解，未忽略任何结果式因子。代码在取 M 后立刻 assert 整个 res 与上述乘积相等。已闭 J 因子不重跑。另由系数运算逐项验证

$$
\operatorname{lc}_zM=(4\lambda-1)^2A^4.             \tag{2}
$$

因此 (2) 的整个零面只有下列两类，无遗漏首项零参数。

## 2. lambda=1/4 的完整 11 次 z 代数

M(1/4,z) 实际降到 11 次。除非零有理常数后得到 monic Psi11；其低次到高次系数为

```
-390471296/2187,
1329893696/2187,
-2603238232/3645,
385310872/2187,
3725032103/12150,
-50085267011/218700,
-53021448683/1749600,
7306202671/72900,
-683773147597/13996800,
12133187237/1166400,
-83360311/97200,
1.
```

直接使用整代数 B11=QQ[z]/(Psi11)，取 lambda=1/4，不删除任何 z 因子。源验证原 M=0、F+H theta=0、G=K=0；所有原物理单位与 H 的逆均由扩展 Euclid 生成，并实际回乘 1。

## 3. A=0 的同一 lambda 返回

先在 QQ[lambda]/(lambda^2-lambda+1/2) 中将原 M 约化为

$$
M\equiv m_0(z)+m_1(z)\lambda.
$$

取这一个原表达式的二次范数

$$
N(z)=m_0^2+m_0m_1+\tfrac12m_1^2.                  \tag{3}
$$

(3) 只是必要 z 覆盖；随后必须恢复同一 lambda，不能把来自不同嵌入的条件拼合。N 除常数后是 monic Psi20，低到高系数为

```
862356025/81, -3096360200/81, 7005495010/81,
-10938433310/81, 13254977426/81, -12528148144/81,
3164461304/27, -5663363378/81, 2629466443/81,
-102928478/9, 93231512/27, -131407526/81,
34735774/27, -72227240/81, 11677180/27,
-11255480/81, 2192269/81, -26338/9,
1840/9, -22/3, 1.
```

在完整 B20=QQ[z]/(Psi20) 中，实际找到 m1 的逆；定义

$$
\lambda=-m_0m_1^{-1}.
$$

源在 B20 内逐项验证 A=0 与**原 M(lambda,z)=0**，再由 (1) 恢复同一 theta，验证 G=K=0。因此两个 lambda 嵌入及其全部 z 根都保留；没有独立取范数后错配嵌入，也没有 m1 首项零分支被删。

## 4. 返回原 Gram，完整保留 d 的两根

对 i=11、20 分别在

$$
\mathcal B_i=B_i[d]/(d^2-\Delta)
$$

工作。无需假设任何二次塔不可约。全部构造在整代数中完成，因而包括每个基参数上 d 的两根。

令

$$
\ell=D/z^2,\quad T=C/z,\quad w=\lambda-1-T,
\quad B_v=2T-\ell s,
$$
$$
b=\ell/2+B_vd/(2\Delta),\quad c=\ell-b,
\quad p=1+\theta d,\quad q=1-\theta d,
$$
$$
h=1+(s+d)/2,\quad k=1+(s-d)/2,\quad u=\ell+\theta B_v.
$$

然后取原式

$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,
\quad P_{02}=(2-3u)V_2-Qu+2u^3,
$$
$$
f=\frac{-T_0^2+2\ell Q^2(\ell+T)-2\lambda\ell QT_0}
{4(u-1)T_0}.
$$

源实际验证 P02=2ell Q(u-1)、T0+4(u-1)+Q=0，验证原 U 三矩、P(V)=N(V)=0，并由原 W1/W2 公式重建物理 Gram。原九个 t 多项式按

```
E1, EB, EC, P1, PB, PC, N1, NB, NC
```

完整生成。两类上的次数均为

```
2, 2, 2, -1, 3, 3, 2, 3, 3.
```

这里 P1 确实恒零；源没有错误地用其结果式判空。全九式先被验证、记录输入身份，再使用原 E1、EB。

## 5. 两个实际单位证书

分别在上述 22、40 维代数计算

$$
\mathcal R=\operatorname{Res}_t(E_1,E_B)=a+bd.
$$

令 n=a^2-Delta b^2。源在整个 Bi 中为 n 取得扩展 Euclid 逆，并验证

$$
\mathcal R\,[(a-bd)n^{-1}]=1.                    \tag{4}
$$

若存在原解，E1 和 EB 在同一 t 上为零，则其原结果式必须零，与 (4) 矛盾。这里结果式由原实际次数的 Sylvester 行列式生成；计算未假设原九式均为最高标称次数，也未用多变量 gcd=1 代替无公共零点证明。

| lambda 面 | 基代数维数 | 含 d 的完整维数 | 真逆身份数 | 原 Res_t(E1,EB) 逆 SHA256 |
|---|---:|---:|---:|---|
| lambda=1/4 | 11 | 22 | 25 | baf0d7e675d281447db1f494c8a9a810c1087a0829788a73724ad83aa54b7332 |
| A=0 两根 | 20 | 40 | 26 | d17f3df6f7f929f47902012e6c2c90dc1eb56c6ac729e9943f4788bca4b5f128 |

原九式输入 SHA256 分别为

```
1d90fa406a950a4882563cd6d6fc003782d2df7c1588f823fac4e1a8cc2e0dd5
ae0e6130eee453353c345a8c2a038cc9521433e5b2f93dec73dc63c7256a6569
```

这完成 (2) 全零面。后续 M 图上 (4lambda-1)A 非零可作真单位；仍须返回一般图的其余全部原解候选。

## 6. 执行身份

[自含源](../notes/2026-11-27-unit211-S0-Lt0-parameter-leading-zero-return-8542.py) 14,350 字节，SHA256

```
f970e31be8ffdd360a30a7e4f108c312fb8801061c380e86a77b05dfaa49a158
```

[小回执](../notes/2026-11-27-unit211-S0-Lt0-parameter-leading-zero-execution-8542.json) 记录 Python 3.12.14、python-flint 0.9.0、180 秒 alarm，实际 0.774927 秒、exit 0、峰值 RSS 30,840 KiB。实际 stdout SHA256

```
8d4a2304095b26efbe55584a72cfd353e66bf76eb8d00ded203a1376f63c8781
```

源从 G、K 生成所有覆盖、同嵌入返回和原式证书，不依赖先前未完成 driver，也不需要仓库存储大系数数组。
