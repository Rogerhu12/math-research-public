# 层 41 的实际 Poincaré 运算：断线后完整重算与独立复验

日期：2026-11-12；负责 qc_global。

本记录延续 `2026-11-12-qc-poincare47-disconnect-recovery.md`。限制商、单生成代数及非零双扩张纤维左逆都已从已发布 R102、R110、R112、R117 的实际数据重新计算。两个丢失的生成器按数学接口重新实现，故新证书字节与旧证书不同；固定截面所给范数及左逆数值完全一致。**本记录不把双扩张坐标修正当作非主局部高度。**

## 1. 已完成的实际计算

设 q=47^4=4879681，L=K+D，deg L=126，g=54。保留 R117 固定的 s,t,u,v,f，以及实际有效除子 D0=div(f)、EB、Eminus、Dv=div(v)。这里 s 的除子是 EB+Eminus。

三个固定 u/v 范数从完整限制商重新得到：

| 除子 | 范数模 q |
|---|---:|
| D0 | 3467725 |
| EB | 708004 |
| Eminus | 4763767 |

比值 708004/3467725=4666447 再次等于 R117 直接在 CM 除子及尖点上所得的主范数。

每个限制代数由实际算子 Fv^{-1}Fg 和真实单位 Q2(v²) 的 126 阶单位 Krylov 矩阵确定。新实现对 EB 选到第 3 个单生成元，旧实现选到第 2 个；代数的基选择变化，实际范数不变。新的随机有理三次截面在 D0、EB、Eminus 上的范数依次为 1712027、1231401、4233153。这一条截面与旧证书中的随机三次截面不同，不能拿旧的三个三次范数直接比较。

固定二次截面 t 的范数仍为

\[
N_{E_-}(t/v^2)=1412636.
\]

真实非零纤维采用

\[
A=E_B-D_0,\qquad B_y=E_--D_v,
\qquad \mathcal P_{[A],[B_y]}=N_A\mathcal O(B_y).
\]

它代表 (B−4,−B−4)。全部支持不交由单位范数认证。令 a=t，Ea=div(a)−EB，A'=Ea−D0，psi=a/f²，则 div psi=A+A'。第一变量的规范平凡化把 O(div psi) 的 1 送到 psi，故坐标 1 的左逆坐标为

\[
\lambda=\psi(B_y)^{-1}
=\frac{N_{D_v}(a/f^2)N_{E_-}(f/v)^2}{N_{E_-}(a/v^2)}.
\]

三个有限代数范数是

\[
N_{E_-}(f/v)=2436042,\quad
N_{E_-}(a/v^2)=1412636,\quad
N_{D_v}(a/f^2)=1311028,
\]

因此

\[
\lambda=149764,\qquad \log_{47}\lambda=4140042\pmod{4879681}.
\]

该坐标和对数是实际双扩张群律的输出；还没有计算选定高度 splitting 在此纤维的值。

## 2. 完整证明接口

恢复笔记已给出范数算法到真实 Poincaré 群律的完整连接。以下列出独立复验实际覆盖的接口，以免把某个局部矩阵等式误称全证明。

1. I_E=H0(L²−E) 的实际 73 维基来自已证明除子；199 个真实 V1·I_E 乘积具有单位子式。因 deg(L³−E)=252，H1=0，故这些乘积生成整个 H0(L³−E) 整格。
2. Q2 和 Q3 分别是实际限制商 V2/I_E、V3/H0(L³−E)，均为秩 126 自由模。程序检查完整商核、存储的单位逆矩阵及全部 820 行乘法关系。
3. Fv 的单位行列式等价于 v 在有限平坦除子 E 上不消失。det Fu/det Fv 是 O(E) 上 u/v 的代数范数，保留非约化重数，不需要因式分解 E。
4. 单生成代数的 1 是 Q2(v²)，生成元算子是真实乘法 Fv^{-1}Fg。完整单位 Krylov 矩阵及最后一次幂的关系给出真实代数同构。全部 199 个二次基以及生成 V3 的 199+126 个实际三次乘积均已检查。
5. 取 a=t 后，Ea 的实际理想由 s/a 的 126 秩完整核确定；检查全部 820 行、单位子式、73 维 Frobenius 下降及下降 cocycle。不是仅记录一个与 −B 同类的形式符号。
6. 范数单位性验证 A、A' 都与 By 不交。最终独立计算 psi(By)，并检查 lambda·psi(By)=1。其符号由 O(div psi)→O0 的规范平凡化决定。

所有 NumPy 累计都覆盖完整内积长度；最大内积维数820，界为

\[
2\cdot820(47^4-1)^2=39050494119936000<2^{63}.
\]

有限代数卷积仅需长度126的相同界。两次乘法之间先模 q；未使用浮点矩阵。

## 3. 独立验证已完成

新的 `verify_p41_poincare_algebras47.py` 不调用生成器的范数函数。它先从已发布评价模型恢复真实商及算子，再使用 Python 整数复数对计算 Euclidean resultant。若欧几里得中间首项非单位，改用独立的纯 Python 单位主元行列式；不能把该情形误判成范数消失。

普通模式已经完整通过三个限制代数、固定二次范数及新随机三次范数。`--inverse` 模式另外独立构造 Dv 和所需 Eminus 代数，重算上述三个范数、全部残余理想、下降及规范反向群律，最终日志为：

> Actual nonzero Poincare left inverse: independent norms, full ideal and descent PASS.

这里只引用本项目自己的程序输出，不是文献定理。

## 4. 新证书及复验

| 路径（相对 scripts/data） | bytes | 新 SHA256 |
|---|---:|---|
| p41_poincare_norms47_checkpoint.json.gz | 2722347 | a590273832f624d3739aa19bd3c4c8b52df859c45affc2ccfe5af8b7978fbba3 |
| p41_poincare_algebras47_checkpoint.json.gz | 390522 | 7d459346e886bc7942ef79391b4dcb7e5daf1f7fb335b2e561e8e7d3cb65f1a7 |
| p41_poincare_inverse47_checkpoint.json.gz | 1251423 | 96d27fd052b95e3c36dd7384e2dcabe3d009aacef9b499b3ae4fb1f332542889 |

从仓库根运行：

```sh
python -u topics/serre-uniformity/scripts/p41_poincare_norms47.py
python -u topics/serre-uniformity/scripts/p41_poincare_algebras47.py
python -u topics/serre-uniformity/scripts/p41_poincare_inverse47.py
python -u topics/serre-uniformity/scripts/verify_p41_poincare_algebras47.py --inverse
```

前两个源码是断线后重建版本；第三个是从原完整工具输出逐字恢复的版本。独立验证器新增 `--inverse` 分支，以前的恢复笔记中“待独立核验”状态现已闭合。

本阶段完成实际有限代数与非零纤维群律接口。后续仍需真实局部/全局高度或双扩张整点闭包的输入，方能得到 QC 共同零点证书。
