# R150：S0/Lt0 的 ell=1/2 原支路完整排除

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127 / r150_open_geometry；AI-assisted GPT-6 Astra Pro。

**结论。** 在三值互异、L 非零、Af 非零的剩余 S0/Lt0 图中，ell=b+c=1/2（等价 base Frobenius 权 a=1/2）整个原支路为空。20 次必要 lambda 覆盖全部返回，末 16 谱的完整 32 维原代数中，原 Res_t(E1,EB) 的逆已实际回乘为 1。一般 Lt0、S0 与 ISP 仍未因此关闭。

这个边界的排除将用于后续原均值低次输入的除法；该输入须另行完整核验。本次排空独立地从原 G、K、M 及 ell=1/2 出发。

## 1. 原必要覆盖与所有因子

沿用 [Lt0 原参数定义](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-theta-leading-zero-exclusion.md) 和 [原 theta 余式双零已闭边界](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-theta-remainder-zero-exclusion.md)。记

$$
s=2\lambda-3,\quad A=2\lambda^2-2\lambda+1,\quad C=-4\lambda^2+5\lambda-2,
$$
$$
D=sC-Az,\quad \Delta=s^2-4z,\quad B=2Cz-Ds,
\quad\ell=D/z^2.
$$

ell=1/2 给出原必要式

$$
H_z=z^2-2D=0.                                    \tag{1}
$$

自含源从原 Lt0 式 G 与原 P1/N(V) 兼容式 K 重新生成并逐项验证完整恒等式

$$
\operatorname{Res}_{\theta}(G,K)=256z^{14}J^2M(\lambda,z),
\qquad \deg_{\lambda,z}M=(26,12).                  \tag{2}
$$

z 非零来自 h1/k1 边界；J=0 已完整返回并关闭。故剩余原解必须满足 M=Hz=0，没有从 (2) 丢掉未付因子。

Res_z(M,Hz) 的 lambda 次数为 52，平方自由部分次数 20，其完整 monic 因式分解是

$$
(\lambda-1/2)(\lambda-3/2)
(\lambda^2-5\lambda/4+1/2)\Phi_{16}(\lambda).       \tag{3}
$$

源将实际全部因子乘回核对。平方自由多项式 SHA256：

```
1e53ff01fcf5aebc2b4b61d53e738a8d62491d6f295b342c70c06cceafaad087
```

Phi16 的低到高系数为

```
-32418369/22528, 67726531/5632, -6046553693/135168,
13014430415/135168, -46526167219/360448, 26596569/256,
-1506874389/45056, -923741521/33792, 997612755/22528,
-252896363/8448, 12723791/1056, -3136367/1056,
2013673/4224, -56389/528, 2051/48, -689/66, 1.
```

## 2. 原完整 z 返回，包括低谱首项零

每个 lambda 因子都在其整商代数内返回原 M、原 Hz 的完整 z gcd。所有欧氏除法和扩展 Euclid 的 Bezout 身份实际回乘；不将一般参数子结式直接套到退化低谱。

| lambda 因子 | 原 z 返回 | 排除或继续 |
|---|---|---|
| lambda−1/2 | gcd 的一次因子属于 Delta | h=k 已闭，Delta 非零支付 |
| lambda−3/2 | gcd 的一次因子是 z | z 非零支付 |
| lambda²−5lambda/4+1/2 | gcd 的一次因子是 z | z 非零支付 |
| Phi16 | gcd 恰为一次 | 唯一 z 返回同一 lambda，继续原 theta 与 Gram |

没有删除 Phi16 的任何根，没有删除原低谱，也没有用多变量 gcd=1 当作无公共零点证明。

## 3. 保同一 theta 的完整 32 维原代数

令 B0=QQ[lambda]/(Phi16)。原 M、Hz 的 z gcd 一次首项有实际逆，源取 z=−p0/p1 并检查原 M=Hz=0。

原 theta 伪余式在 G 下满足

$$
g_2^3K=Q_*G+r_0+r_1\theta,
\qquad \gcd(r_0,r_1)=z^5J/192.
$$

除公因子后记 F、H。先前已付的 g2 非零及原余式双零例外保证原剩余图可用 theta=−F/H；在本 Phi16 整代数中，H 的逆实际存在且回乘为 1。取此**同一 theta**后直接检查原 G=K=0，避免把独立范数的不同嵌入拼合。

令

$$
\mathcal B=B_0[d]/(d^2-\Delta).
$$

全部 16 个 lambda 根、各自同一 z 和 theta、d 的两个根都保留；不假设该二次塔不可约。使用

$$
T=C/z,\quad w=\lambda-1-T,\quad B_v=2T-\ell s,
$$
$$
b=\ell/2+B_vd/(2\Delta),\quad c=\ell-b,
\quad p=1+\theta d,\quad q=1-\theta d,
\quad h=1+(s+d)/2,\quad k=1+(s-d)/2,
$$

以及原 Lt0 的 f 公式，从原 W1、W2 重建完整 Gram。源实际检查 ell=1/2、全部原物理分母单位、原 U 三矩、原 P(V)=N(V)=0，且用正确 dual-number 乘法 `ddv=vm(d,d)` 生成全部九式。其 t 次数为

```
E1, EB, EC, P1, PB, PC, N1, NB, NC
 2,  2,  2, -1,  3,  3,  2,  3,  3.
```

P1 在本图恒零，并未拿其退化结果式判空。原九式输入 SHA256：

```
cc4d631897aab1486ccd946be1f258cd4adfd8cdc8c891b993f5917c45769ecb
```

最终将原 R=Res_t(E1,EB) 写为 r0+r1d。在整个 B0 中为 r0²−Delta r1² 取得扩展 Euclid 逆，实际验证

$$
R\,(r_0-r_1d)(r_0^2-\Delta r_1^2)^{-1}=1.
$$

因此原 E1、EB 不可能在同一 t 上共同为零。共 52 次基代数真逆身份；该末逆 SHA256：

```
1ab152624c2d9000cf609475f2407df569d5776895344dd76c221db2767f995c
```

结合表中全部低谱，(3) 的完整覆盖穷尽，证明 ell=1/2 的整个本支路为空。后续在一般图中可把 ell−1/2 作为已支付单位。

## 4. 执行身份

[自含源](../notes/2026-11-27-unit211-S0-Lt0-half-weight-sum-original-return-8542.py)，17,836 字节，SHA256：

```
f6e972a386ca03bb0748a6b657cb28858b0563fbf048a13996a945ea9c088d32
```

[实际小回执](../notes/2026-11-27-unit211-S0-Lt0-half-weight-sum-execution-8542.json)：Python 3.12.14、python-flint 0.9.0，180 秒 alarm；实际 0.475966 秒、exit 0、峰值 RSS 30,200 KiB。stdout SHA256：

```
ad8de1f70c647951a25b3f82a91520e3784b58eada18eef7cab9712125ee110d
```

源自含生成完整覆盖及真逆证书，不读取本轮作废的均值数据或大系数数组。一般图的新低次输入尚须独立完成原式核对与后续消元，本附录不将待算输入声明为排空。
