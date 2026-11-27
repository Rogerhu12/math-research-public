# R150 Lt0：Q=2((u−1)²+1) 的完整原曲线排空

日期：2026-11-27。AI-assisted GPT-6 Astra Pro；会话：Astra-ISP-8542378f-20261127。

**状态：已证明，原源已实际通过。** 在现余 S0/Lt0 原图中，整条曲线

$$
Q=2\bigl((u-1)^2+1\bigr)
$$

不存在原临界点。等价地，在 e=u−1、k=Q/e 坐标中

$$
\Omega=2e^2-ek+2
$$

可以在后续一般图中作为单位。本证明只依赖已经完成的 k=4e 与 v=0 整支排空及原 Cramer 子式；不依赖尚在运行的四变量 QQ 门，也不依赖其他未完成的二参数投影返回。

## 1. 原单位上的完整曲线坐标

使用[原低次不变量系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-low-invariant-original-system.md)和[原 Cramer 子式](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-original-Cramer-minor-system.md)。仍记

$$
e=u-1,\quad k=Q/e,\quad j=k+2-2e,
\quad v=4kbc\,t.
$$

e、k、u=e+1、j、bc、T0 和 ek−1 都是原已付单位；e−1=0 与 4e−k−4=0 分别属于已闭 a=0 与 ell=1/2 整支。另由[乘法一致性退化线](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-mean-consistency-line-exclusion.md)和[零孤立点配对](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-zero-singleton-pairing-exclusion.md)支付 4e−k 和 v。后两份证明均不使用本稿，因此没有循环支付。

在 Omega=0 上，因为 e≠0，原 k 完全由

$$
k=\frac{2e^2+2}{e}
$$

恢复。这里没有再添一般位置假设。原单位在该曲线上的关键身份为

$$
ek=2(e^2+1),\qquad ej=2(e+1),
$$
$$
e(4e-k-4)=2(e^2-2e-1),\qquad
 e(4e-k)=2(e-1)(e+1).
$$

自含源逐项检查这些身份；后面的一元矛盾恰使用这些已付因子。

## 2. 四个原子式的专门化与全首项保留

[自含源](../notes/2026-11-27-unit211-S0-Lt0-quadratic-invariant-curve-return-8542.py)从正确原 Gram、双点乘法、同根 P/N、三条原 mean 的可逆 Cramer 矩阵和完整归约追踪开始。它实际检查全部二十个 3×3 子式的原行组合，任何归约分母与因子剥除均乘回；不读取大系数数组。

行号仍按零起始：0=N1elim，1=原 NB 偶部，2=原 PB 偶部，3=原 U 矩，4、5=两个原 mean 乘法一致性临界对。

对每个本次使用的原子式 D(e,k,v)，设它对 k 的次数为 m，令 Dcur 为代入 k=(2e²+2)/e 后乘 e^m 的多项式。源码实际给出并检查多项式除法身份

$$
e^mD(e,k,v)-D_{\rm cur}(e,v)
=(ek-2e^2-2)H(e,k,v).
$$

因此清除的分母只有已付 e。这一身份在原多项式环中成立，没有把数值替换或形式分式当作原返回。

之后只剥原已付单位在曲线上的分子，保留每次原乘回。选取以下四式：

| 返回子式 | 清分母 e 次数 | 返回后 (e,v) 次数 | 项数 |
|---|---:|---:|---:|
| F045 | 16 | (24,5) | 107 |
| F035 | 19 | (28,5) | 130 |
| F034 | 21 | (34,6) | 177 |
| F015 | 22 | (34,5) | 166 |

其中三式专门化后含 v 因子，已由此前**完整**的 v=0 排空支付；本稿没有自行删除未知的 v=0 分支。每个全部剥除积都再次按已付因子剥至非零常数。

对 F045 与其余三式分别取完整 Res_v。实际 e 次数依次为

$$
224,\qquad 266,\qquad 254.
$$

三个投影均保完整首项；未按任何 v 首项除法。故只要原曲线中存在有限原 v 公共零点，无论何处次数下降或某返回式恒零，三条一元结式都必须同时为零。

## 3. 实际 QQ[e] Bézout 只有已付因子

在 QQ[e] 实际逐次扩展 Euclid，产生三个一元系数 A224、A266、A254，次数分别为 203、161、78，并核对累计乘回

$$
A_{224}R_{224}+A_{266}R_{266}+A_{254}R_{254}
=e^{32}(e+1)^{40}(e-1)^2(e^2+1)^{18}(e^2-2e-1)^4.
$$

右边次数 118，恰是三条完整结式的首一 gcd。这里是一元精确 Bézout 身份，没有把多变量 gcd 或数值采样作为排空证据。

原解令左边为零。但右边的每一个因子都已经支付：

| 因子 | 在原曲线上的支付 |
|---|---|
| e | 原 u−1≠0 |
| e+1 | 原 u≠0 |
| e−1 | 已闭 a=0 整支 |
| e²+1 | ek=2(e²+1)，e、k 非零 |
| e²−2e−1 | e(4e−k−4)=2(e²−2e−1)，已闭半权整支 |

右边不可能为零，矛盾。加上此前已经独立关闭的 k=4e、v=0，Omega=0 的整个原支路均无解。

## 4. 真实执行

[实际回执](../notes/2026-11-27-unit211-S0-Lt0-quadratic-invariant-curve-execution-8542.json)：Python 3.12.14、python-flint 0.9.0，exit 0，3.710581 秒，峰值 RSS 52,788 KiB；全部原 Gram/Cramer 组合、原曲线清分母身份、投影及一元 Bézout 都实际通过。

自含源 21,095 字节，SHA256：

```
0f23810cf5c2617eef839e6803155342ee10d794006693ec2abaa72a089bda05
```

三条完整结式 SHA256：

```
5eb92b667a00e76c11506dbd800cc39890bdc950813affce590b1ca0d6300583
5a4a27a0403b19409da0d795186ab693666a0a3adcb613e0ddc3951db832c50c
30bbadfc1eac83313f55cf8513b621046078f91723ee54fc2a08a3e09e8b06a2
```

累计一元 Bézout 系数 SHA256：

```
11b71cf67d66dd804df8b799b6b2c7184612673c8eec8e0b73d547e67958cd25
```

本稿不宣布一般 S0/Lt0、全部 R150 或普通 ISP 完成；当前一般图继续保留完整原 P/N 与所有物理约束。
