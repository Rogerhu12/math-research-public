# R150：S0/Lt0 的 w=0 原支路完整排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127 / r150_open_geometry。

**结论。** 三值互异、L 非零、Af 非零 S0/Lt0 图中，原 U 的双点导数值 w=0 整支为空。原 30 次 lambda 结果式的 17 次平方自由覆盖全部返回；最后 14 谱在完整 28 维原代数中验证原 Res_t(E1,EB) 的逆回乘为 1。此前 L0/w0 的平移证明只处理 L=0，本稿处理的是剩余 S0/Lt0 图，未重做那条已闭结论。

该单位的直接用途：新低次输入的原 N(V) 对 eta=theta·Delta 一次，其首项恰含 w。关闭整个 w0 后，可以保同一配对合法消去 eta，减少一般图的变量。这个用途不参与本稿的排空证明。

## 1. 原覆盖与低谱

沿用 [Lt0 原参数](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-theta-leading-zero-exclusion.md)，记

$$
s=2\lambda-3,\quad A=2\lambda^2-2\lambda+1,\quad C=-4\lambda^2+5\lambda-2,
$$
$$
D=sC-Az,\quad\Delta=s^2-4z,\quad B=2Cz-Ds,
\quad T=C/z,\quad w=\lambda-1-T.
$$

z 非零，因此 w=0 等价于

$$
H_z=(\lambda-1)z-C=0.                            \tag{1}
$$

原 Lt0、P1/N(V) 兼容的多项式 G、K 仍按原定义生成。自含源实际逐项验证完整结果式覆盖

$$
\operatorname{Res}_{\theta}(G,K)=256z^{14}J^2M(\lambda,z).
$$

z、J 的零面已付，故剩余原解必须 M=Hz=0。没有丢掉其他结果式因子。特别地，(1) 的 z 首项 lambda−1 没有被默认非零：lambda=1 时原 Hz=1，根本没有 z 解。

源直接计算 Res_z(M,Hz)，lambda 次数 30，其 monic 平方自由部分的完整因式分解为

$$
(\lambda-1/2)(\lambda^2-5\lambda/4+1/2)\Phi_{14}(\lambda). \tag{2}
$$

实际所有因子乘回核对，平方自由多项式 SHA256 为

```
99f8df882b11e1294fad92bd1c4c46ddcc09d5c3eb57fb95f6aabe80078abc09
```

Phi14 的低到高系数为

```
2/405, -26/405, 89/270, -106/135, 1247/3240,
617/216, -12779/1440, 85681/6480, -71113/6480,
2393/1080, 26599/3240, -111/8, 691/60, -31/6, 1.
```

对 (2) 的每个因子，在整 QQ 商代数中返回原 M、Hz 的 z gcd，全部除法和 Bezout 身份回乘核验：

| lambda 因子 | 原返回 | 处理 |
|---|---|---|
| lambda−1/2 | z gcd 的唯一一次因子使 Delta=0 | 已闭 h=k 支路支付 |
| lambda²−5lambda/4+1/2 | z gcd 的唯一一次因子是 z | 原 z 非零支付 |
| Phi14 | z gcd 恰为一次且首项有真逆 | 继续全原返回 |

这些是每个完整参数因子的原返回，没有数值根采样，也不把多变量 gcd=1 解释为空集。

## 2. 同一 theta 与全部原九式

在 B0=QQ[lambda]/(Phi14) 中，用实际逆取原 z gcd 的根 z=−p0/p1。源核对 M=Hz=0，再由已付原 theta 伪余式双零边界恢复 theta=−F/H；H 的逆在整个 B0 中真实回乘为 1。随后直接验证原 G=K=0。

仍取完整

$$
\mathcal B=B_0[d]/(d^2-\Delta),
$$

保留 14 个 lambda 根、每个同一 z 和 theta、d 的两根。无需假设二次塔不可约。按原公式

$$
\ell=D/z^2,\quad B_v=2T-\ell s,
\quad b=\ell/2+B_vd/(2\Delta),\quad c=\ell-b,
$$
$$
p=1+\theta d,\quad q=1-\theta d,
\quad h=1+(s+d)/2,\quad k=1+(s-d)/2
$$

以及原 P1 的 f 公式、原 W1/W2 重建 Gram。源实际断言 w=0，并检查原 U 三矩、全部物理分母单位、原 P(V)=N(V)=0。

原双点乘法始终通过 `vm` 实现，特别是均值中的 (d·d)1=2d0d1。全部九式

```
E1, EB, EC, P1, PB, PC, N1, NB, NC
```

的 t 次数为 `2,2,2,-1,3,3,2,3,3`。P1 恒零，未用其退化结果式。完整九式输入 SHA256 为

```
3de2b7637e44eb7bde06c93a62656bf44b0c5e5cbb36a7c7838ea93d6b61620f
```

在整个 28 维代数中，原 R=Res_t(E1,EB)=r0+r1d 有实际逆

$$
R^{-1}=(r_0-r_1d)(r_0^2-\Delta r_1^2)^{-1}.
$$

源用扩展 Euclid 验证基代数逆，并逐项回乘 R·R^{-1}=1。原同一 t 上 E1=EB=0 将强迫 R=0，与此矛盾。末分支共 51 次基代数真逆；末逆 SHA256 为

```
401dbcf444050d23452e0262e25746bf08f321fe2436ea4d97beff429862e691
```

结合全部低谱返回，(2) 穷尽，本图的整个 w=0 支路无原解。一般 Lt0、S0 和 ISP 仍开放。

## 3. 执行身份

[自含源](../notes/2026-11-27-unit211-S0-Lt0-w-zero-original-return-8542.py) 17,812 字节，SHA256：

```
0a072a7dcfca1ba8365c23d894d92eab1f84192ec19724e739343b10615f8e24
```

[实际回执](../notes/2026-11-27-unit211-S0-Lt0-w-zero-execution-8542.json)：Python 3.12.14、python-flint 0.9.0，180 秒 alarm；实际 0.148623 秒、exit 0、峰值 RSS 29,636 KiB。stdout SHA256：

```
daa93ca03cdcb5bf90ef191d3e28fdbb426e05d8ca74cf9c9dc462ffffc0133e
```

源独立生成 G/K、完整因子覆盖及全原证书，不读取新低次试探输入或其他 scratch 系数。
