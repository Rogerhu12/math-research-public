# R133：从两个真实 CM 点校准全部 54 个高度系数

日期：2026-11-12；qc_global。**状态：可逆校准定理已证明。** 本文给出完整的可逆校准公式；尚未算出其 54 个局部高度右端。它与已完成的 R121 对数和 R131 实际 Hecke 作用相接，不宣称已有完整 QC 函数。

## 1. 固定实际类和高度规范

写 $E=\prod_fE_f$，八个域和其生成元 $H=T_2+2T_3$ 都与 R89、R94 一致；它们的次数为 $2,3,3,4,4,8,12,18$。令 $B=B_{-4}$。各域分量 $B_f$ 均非零，且实际 $J(\mathbb Q)\otimes\mathbb Q=EB$。

在固定的 Hecke 相容 Poincaré 高度 $h$ 下，存在唯一
$$s\in E\otimes\mathbb Q_{47}$$
使
$$h(aB,bB)=\operatorname{Tr}_{E\otimes\mathbb Q_{47}/\mathbb Q_{47}}(sab).
\tag{1}$$
确实，Hecke 的 Rosati 自伴随性给 $h(aB,bB)=h(B,abB)$，而有限可分代数的迹配对非退化。这一 $s$ 使用实际 Mordell–Weil 基 $B$；若改用特征微分对数坐标，系数是 $c_f=s_f/\log_f(B_f)^2$，不能忽略这两个对数因子。

R89 已经确定真实带符号关系
$$U_\delta=[20P_\delta-D]=r_\delta B\qquad(\delta=-3,-7)$$
于 $J(\mathbb Q)\otimes\mathbb Q$。R94 的 53 个方向是
$$F_n=a_nT_n+b_n,\qquad G_n=2F_n,$$
其中此处 $a_n$、$b_n$ 指 R94 数据字段 `F_Tn_coefficient` 和 `F_identity_coefficient`，不混用其正文中另记的最大公因数。该证书的实际平移为
$$\eta_{D,G_n}=\xi_n B,\qquad \xi_n=\Xi(F_n).$$
全部次数 $20$ 和一次 $G=2F$ 已包含在上述定义中。

因此对应全局高度值准确为
$$\boxed{h(U_\delta,G_nU_\delta-\eta_{D,G_n})
=\operatorname{Tr}(s v_{\delta,n}),\qquad
v_{\delta,n}=2F_nr_\delta^2-r_\delta\xi_n.}
\tag{2}$$
这里没有重新选择 Jacobi 平方根、Heegner 点的符号、极化或对数周期。

## 2. 一组真实 54 条方程及单位行列式

使用以下有序列表：先取 $P_{-3}$ 上 R94 的全部 53 个方向，次序与其 `indices[1:]` 相同；最后仅加入 $P_{-7}$ 上 $n=2$ 的方向。

在每个 $E_f$ 中取 $1,H,\ldots,H^{[E_f:\mathbb Q]-1}$，并按 R89 的八域顺序拼接。令 $V$ 为这 54 个 $v_{\delta,n}$ 的行坐标矩阵，$G$ 为该基的迹 Gram 矩阵。若 $s$ 的坐标列为 $\mathbf s$，相应 54 个真实全局高度值列为 $\mathbf L$，则
$$\boxed{\mathbf L=M\mathbf s,\qquad M=VG.}\tag{3}$$

所有 R89/R94 所需有理分母在 47 处都是单位。生成程序用逐域多项式乘法严格构造 $V$，由各域定义多项式的 Newton 恒等式构造 $G$，并作模 $47^4$ 的两侧逆验证。准确结果为
$$\boxed{\det V\equiv2,\quad \det G\equiv46,\quad
\det M\equiv45\pmod{47}.}\tag{4}$$
八个迹块的行列式依次为
$$34,28,37,20,5,24,17,33\pmod{47}.$$
所以全部迹块和 $M$ 都在 $\mathbb Z_{47}$ 上可逆。证书明确保存
$$MM^{-1}=M^{-1}M=I_{54}\pmod{47^4}.$$
实际计算中第一组 53 条已秩 53；加入第二点的一条便封闭最后一个方向。

从 (3) 得到
$$\boxed{\mathbf s=M^{-1}\mathbf L\pmod{47^4},}\tag{5}$$
没有额外的 47 进精度损失。同一有限程序可在任意更高模 $47^e$ 重算；(4) 已证明逆存在于整个 $\mathbb Z_{47}$，而不是只在此次截断中形式地求解。

## 3. 右端必须保留的真实坏靶

式 (5) 所需 $\mathbf L$ 尚未输出。它不是随意挑选的局部范数或 R117 的主除子对数。

使用 R54 的同一全局有理截面归一化。若 $P_\delta$ 在坏素数 41 的实际未分歧正则模型上落于分量 $i_\delta$，则准确右端是
$$L_{\delta,n}
=\lambda_{47}(\widetilde s_{2F_n}(P_\delta))
-\log_{47}(41)\,b_{i_\delta}(F_n).
\tag{6}$$
这来自 R54 (2.2)–(2.4)，没有另一个 $1/2$。所有方向必须使用同一点实际到达的同一分量。

由 R55 的实际 $j$ 标号，$P_{-3}$ 的分量标号为 $0$；$P_{-7}$ 的 $j=-3375\equiv28\pmod{41}$，故其分量标号为 $28$。取参考分量 $i_0=0$，前 53 条的坏项均为零；最后一条保留
$$-\log_{47}(41)\,b_{28}(27T_2+4).$$
不能用 R57 另一方向 $18e_{\rm tor}-1$ 的 $240/7$ 替换这个数。选择参考分量只消去同一个共同常数；它不会消去不同分量的实际高度差。

**后续 R134 已直接证明这个准确坏高度差为零**，并证明本方向在全部四个分量的坏高度均相同。因此本校准现在只需 54 个固定规范的真实辅助局部高度值。仍须实际计算这些值，或者使用完全等价的 Mumford/Poincaré 双扩张运算；可逆矩阵和坏项为零本身不提供任何辅助局部高度数值或共同根排除。

## 4. 小型可恢复证书

源码：`scripts/p41_cm_height_calibration47.py`，只用 Python 标准库。
证书：`scripts/data/p41_cm_height_calibration47_certificate.json.gz`，34983 bytes，SHA256
`53d18d3a6fccf250460ac180f41b8d4588a7d110fe8c3994cb400d468da01013`。

证书保存两个源的 SHA、54 个真实点/方向标签、$V,G,M,M^{-1}$ 及全部模 47 行列式。没有七份 Hecke 目标评价等可重建大中间量。

```sh
python -u scripts/p41_cm_height_calibration47.py
```

本次模 $47^4$ 的所有矩阵等式和行列式由完整整数程序验证；另先前直接模 1009 运算也给同一 54 条方程满秩，但 (4) 才是无 47 进精度损失的证明。本文不以模 1009 的非零性推断模 47 可逆。
