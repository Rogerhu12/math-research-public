# R150：S0/Lt0 的 u=2（等价零 base 权 a=0）完整排除

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127 / r150_open_geometry；AI-assisted GPT-6 Astra Pro。

**完整结论。** 在已登记的三值互异、L 非零、Af 非零 S0/Lt0 图中，u=2 的整个原支路无解。这也关闭该图的 ell=1、a=1−ell=0 零 base Frobenius 权支路。26 次必要 lambda 覆盖的全部因子已返回；最后的 18 谱保留同一 lambda、同一 z、同一 theta 及 d 的两根，在完整 36 维原代数内验证原 Res_t(E1,EB) 的逆回乘为 1。本结论不关闭整个 Lt0、整个 S0 或 ISP。

## 1. 不经过大投影的原输入

沿用 [Lt0 的原参数定义](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-theta-leading-zero-exclusion.md)，

$$
s=2\lambda-3,\quad A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,
\quad D=sC-Az,
$$
$$
\Delta=s^2-4z,\quad B=2Cz-Ds,\quad
\ell=D/z^2,\quad u=(D+\theta B)/z^2,
\quad Q=1-\theta^2\Delta.
$$

原 Lt0 恒等式为

$$
(1-\ell)Q=2(u-1)(u-2).                            \tag{1}
$$

原 P0 非零支付 Q、u−1 与 ell 非零。因此在本图内，u=2 当且仅当 ell=1，也当且仅当 a=0。由 u=2 得

$$
H_z:=z^2-D=0,\qquad \theta B=z^2,
\qquad \theta=z^2/B.                              \tag{2}
$$

z 已由 h1/k1 边界排除，故 B 在 (2) 上必非零。这里 theta 的恢复直接来自原 u、ell 定义，不使用一般位置假设，也不使用本轮曾作废的均值试探投影。

令 U=D+theta B、V=U−z²、Q=1−theta²Delta、E=D+Cz、Tn=−4V−z²Q、W=(lambda−1)z−C，Y=2(Ds−Cz)+theta(Bs−DDelta)。与前述附录相同的原必要式是

$$
G=z^2(z^2-D)Q-2V(V-z^2),
$$
$$
K=z^3(3-4\lambda-z)(-T_n^2+2DEQ^2-2\lambda DQT_n)
 +8DEQV^2-2VT_nWY.
$$

自含源逐项验证完整恒等式

$$
\operatorname{Res}_{\theta}(G,K)=256z^{14}J^2M(\lambda,z),\qquad
B^2-\Delta(D-z^2)^2=z^2J.                         \tag{3}
$$

在 (2) 上 J=B²/z² 非零；g2=−2B² 也非零。因此原解必须同时满足 M=0、Hz=0。没有删去 (3) 的未付因子。

## 2. 52 次原结果式与全部 26 次平方自由覆盖

源直接计算 Res_z(M,Hz)，lambda 次数 52。实际平方自由化并完整因式分解得到

$$
(\lambda-3/2)
(\lambda^2-15\lambda/8+3/4)
(\lambda^2-5\lambda/4+1/2)
(\lambda^3+\lambda^2/2-15\lambda/8+7/16)
\Phi_{18}(\lambda).                              \tag{4}
$$

全部因子及其重数实际乘回平方自由多项式。该 monic 多项式 SHA256 为

```
7ce342b51fa14b16fe1a04e06be9373466fc17a75c4b41788d8149413e4e671d
```

Phi18 的低到高系数为

```
891763/8192, -544037/512, 4584625/1024,
-10174621/1024, 36174773/4096, 240294387/16384,
-267610023/4096, 240230585/2048, -131022761/1024,
10649487/128, -8756205/512, -6496297/256,
8167415/256, -5114041/256, 518869/64,
-17589/8, 12087/32, -279/8, 1.
```

对 (4) 的每个因子 phi，都在 QQ[lambda]/(phi) 中返回**原 M 与原 Hz**的完整 z gcd；每一步原多项式除法与扩展 Euclid 的 Bezout 等式都逐项回乘。只剥离原已付单位产生的 z 因子，不以多变量 gcd=1 判空。

| lambda 因子 | 原返回后的处理 | 结论 |
|---|---|---|
| lambda−3/2 | 全部 z gcd 为 z | z 非零排除 |
| lambda²−15lambda/8+3/4 | 唯一 z；按 (2) 恢复原 theta，原 K 是单位 | 原 K=0 矛盾 |
| lambda²−5lambda/4+1/2 | 全部 z gcd 为 z | z 非零排除 |
| lambda³+lambda²/2−15lambda/8+7/16 | 唯一 z；按 (2) 恢复原 theta，原 K 是单位 | 原 K=0 矛盾 |
| Phi18 | 唯一 z，原 G=K=0，全部物理单位有逆 | 进入完整原 Gram 返回 |

两条原 K 单位的逆 SHA256 分别为

```
2cc8dcf096ed2c6344f1cd8d94e84185d69c4ea40516a06aa695b088a4277953
77142594cfe10aa5d5de23b4ce60fc008159383e5ffa4e3dbbb00c293868c5a4
```

这两条 K 单位不是额外假设：Res_theta(G,K) 允许 G 的另一个 theta=0 分支产生投影点，而 u=2 固定的是 theta=z²/B。将**同一 theta**返回原 K 才排除了这两类投影点。

## 3. Phi18 的完整 36 维原返回

写 B0=QQ[lambda]/(Phi18)。原 M、Hz 的 z gcd 是一次，源用实际逆令 z=−p0/p1，并在 B0 内验证 M=Hz=0。按 (2) 取 theta，验证原 G=K=0。

随后在

$$
\mathcal B=B_0[d]/(d^2-\Delta)
$$

中同时保留全部 lambda 根与 d 两根；不假设该二次塔不可约。置

$$
T=C/z,\quad w=\lambda-1-T,\quad B_v=2T-\ell s,
$$
$$
b=\ell/2+B_vd/(2\Delta),\quad c=\ell-b,
\quad p=1+\theta d,\quad q=1-\theta d,
$$
$$
h=1+(s+d)/2,\qquad k=1+(s-d)/2.
$$

源验证 ell=1、u=2、三条原 U 矩和全部物理分母单位，并取

$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad P_{02}=2\ell Q(u-1),
$$
$$
f=\frac{-T_0^2+2\ell Q^2(\ell+T)-2\lambda\ell QT_0}
{4(u-1)T_0}.
$$

直接按原 W1、W2 重建 Gram，而非用任何新生成的大参数投影。原 P(V)、N(V) 均实际为零，全部九式

```
E1, EB, EC, P1, PB, PC, N1, NB, NC
```

的 t 次数为 `2,2,2,-1,3,3,2,3,3`。原均值明确使用 dual-number 乘法 (d·d)_1=2d0d1；P1 恒零，未用其退化结果式。

最后在整个 B 中计算原 R=Res_t(E1,EB)=r0+r1d，并为 r0²−Delta r1² 取得实际 B0 逆。逐项验证

$$
R\,(r_0-r_1d)(r_0^2-\Delta r_1^2)^{-1}=1.
$$

故原 E1、EB 不可能在同一 t 上同为零。共检查 52 次基代数真逆；末逆 SHA256 为

```
c5224d819118fd04ab924e589221be37e183c3bcc15f0523857a3fcc7328b46a
```

原九式输入 SHA256 为

```
0ff265959dbfdb0653df0bbeb569307292ac4d358077d7dd3c3848a364707c9d
```

结合表中全部低谱返回，(4) 完全穷尽，因此 u=2、ell=1、a=0 三个等价描述的整个本支路无原解。

## 4. 执行身份与边界

[自含源](../notes/2026-11-27-unit211-S0-Lt0-u2-original-return-8542.py) 17,407 字节，SHA256

```
9342f3a73f1af187c2fa0d5c297f4d26719f02605553e60964bff6aa0fd420a7
```

[执行回执](../notes/2026-11-27-unit211-S0-Lt0-u2-execution-8542.json)：Python 3.12.14，python-flint 0.9.0，180 秒 alarm；实际 0.368863 秒、exit 0、峰值 RSS 30,304 KiB。stdout SHA256

```
6ad5d4f848a9daf399521840413467371a3c8d4334a34b0d1ed534b5df29a22e
```

本源自含生成 G、K、M、26 次覆盖及所有返回证书，不读 scratch 的均值数据。此前错误试探的确切废止范围另见 [均值分量纠错记录](../notes/2026-11-27-r150-Lt0-invalid-mean-projection-correction-8542.md)。一般 Lt0 图其余参数仍须继续处理。
