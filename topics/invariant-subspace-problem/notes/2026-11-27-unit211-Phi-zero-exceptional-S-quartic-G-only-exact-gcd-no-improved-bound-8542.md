# Phi=0 例外四次纤维：原 F/G 商的完整 QQ 共同因子与未增加的结式下界

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

在
$$
\phi=\frac1{420}(420\lambda^4-1884\lambda^3
 +3663\lambda^2-3084\lambda+916)
$$
的整个四次域 $K=\mathbb Q[\lambda]/(\phi)$ 中，前一[整纤维与 112 点证明](../results/R150-appendix-unit211-Phi-zero-exceptional-whole-S-moment-quartic-exclusion-and-112-cover.md)已返回完整原 F、G、H 的首一共同四次 g。

本次新的数学输入只使用原商
$$
f=F/g,\qquad q=G/g,\qquad
\deg_\rho f=22,\quad\deg_\rho q=27.
$$
完整短除法及两项原商乘积已经实际核对。没有重跑此前的 $208\times104$ 合并矩阵或 160 维原值返回。

在 $K[\rho]/(\widehat f)$ 中，原 q 的乘法像按完整 QQ 基
$$
\lambda^i\rho^j,\qquad 0\le i<4,\quad0\le j<22
$$
构造新的 $88\times88$ QQ 矩阵。实际 QQ 秩为 **88**，故该像是整个代数。因此
$$
\gcd_{K[\rho]}(f,q)=1,\qquad
\gcd_{K[\rho]}(F,G)=g.
$$
原 F/G 的共同 $\rho$ 因子次数准确为 4，而非 8；原 H 没有将一个八次 F/G 因子截短成四次。

源还以完整 F/G 短除得到的四个原 57 列核向量逐项乘回。它们支付的 QQ 结式下界仍是
$$
v_\phi(R)\ge4.
$$
完整模 R 在 $\bar\phi$ 处的八次重数提供上界 8，故目前仅有 $4\le v_\phi(R)\le8$。原域 gcd 的次数本身不决定高阶接触造成的额外结式赋值。

这一成功计算没有进一步提高 QQ 下界，也没有改变严格 112 点覆盖。源按预先约定没有重跑旧的模余项 Bézout。下一个新对象是这些真实原核列的第一阶 $\phi$ 提升，而非重做本次 88 阶矩阵。

## 实际身份

源：

[2026-11-27-unit211-Phi-zero-exceptional-S-quartic-original-quotient-G-only-multiplicity-input-8542.py](2026-11-27-unit211-Phi-zero-exceptional-S-quartic-original-quotient-G-only-multiplicity-input-8542.py)

- 源 blob：aad74661fee348c41d53d133192cd73e4a026260。
- SHA-256：6e5d91a0a484d428fd90a1c4f80b8dc9181b0a6007a6d4cc06c97da1b2a9bbe6。
- run / job：46046833176 / 140668075698。
- 源提交：73df15632e879167c4093bb79097fb788816c288。
- 驱动时间：1.209605683 秒；峰值 RSS：70264 KiB；内层退出码：0。
- 新原商线性矩阵完成于 1.040350450 秒；完整 F/G gcd 返回于 1.077593820 秒。
- stdout：3043 字节；SHA-256：0b597add7c16fbce7adb0946940da46e11e7e1b58e1e60ae6e3b470daa13408d。

此为有完整数学内容的非改进返回，不是运行失败，也不作原图空性结论。普通 Hilbert ISP 尚未完成。
