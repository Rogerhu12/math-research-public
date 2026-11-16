# R876 — 原 H22 伴随的完整 CM7／CM13 来源

日期：2026-11-16。范围：本篇确定 R863(A20) 中指定 $H_{22}$ 的完整特征零有限算子、生成空间及两算子的真实关系。它不把此来源认成原 $V_{66}$ 的 Hecke 线，也不赋其指定除 $p$ 行非零。

## 1. 同一个原始来源与绝对规范

沿用 $y^2=x^3+b$、$Dx=2y$、$Dy=3x^2$、$X=x^3$ 及原 sigma 规范。R863(A17)–(A22) 给出的实际来源是
$$
H_{22,b}=\sigma_b^{22}X(65X^2-380bX+464b^2),
\qquad H_{22,b}=65z^4+O(z^{10}).
\tag{1}
$$
它在原 whole degree22、型四空间
$$
\mathcal V_{22,4}
=\operatorname{span}_K\{\sigma^{22},\sigma^{22}X,
                       \sigma^{22}X^2,\sigma^{22}X^3\},
\qquad K=\mathbf Q(\omega)
\tag{2}
$$
中。最高函数极阶为十八，故这些都是 whole 截面，且四维空间已完整列出。

先取 $b=1$。固定
$$
\gamma_7=3+\omega,\qquad \gamma_{13}=4+\omega,\qquad
\mathcal N_\gamma=\gamma^{-1}[\gamma]_*[\bar\gamma]^* .
\tag{3}
$$
此处推前、拉回都使用原标准 theta 结构。若
$q_\gamma(P)=\sigma(\gamma z)/\sigma(z)^{N\gamma}$，则完整有限纤维公式为
$$
\mathcal N_\gamma(\sigma^mR)(Q)
=\frac{\sigma(Q)^m}{\gamma}
 \sum_{[\gamma]P=Q}
 \left(\frac{q_{\bar\gamma}(P)}{q_\gamma(P)}\right)^m
 R([\bar\gamma]P).
\tag{4}
$$
不能删掉式(4)中的 sigma 比或因子 $1/\gamma$。

CM13 使用 R732 从 R297 原除法函数重建的全十三点纤维；在每个同一纤维内同时验证原 $S_{34}$ 的
$\mathcal N_{\gamma_{13}}S=-S$，固定绝对相位。
CM7 使用 R464 的全七点纤维及同一个式(3)规范。
两者都不是只取某个点或某个特征值的替代算子。

## 2. 完整有限读取

在 (2) 的升幂基下，令 $A=\mathcal N_{\gamma_7}$、$B=\mathcal N_{\gamma_{13}}$，
$$
v=(0,464,-380,65)^{\mathsf t}.
\tag{5}
$$
公开脚本以目标 $x=a=1,2,3,4$ 的完整纤维读取每一基列。
所得截面仍在 (2)，故四个互异的 $a^3$ 给非零 Vandermonde，唯一恢复完整算子。
目标 $a=5,6$ 的完整纤维另外核对相同恒等式。
纤维求和使用特征零有理函数迹：对于单首纤维多项式 $F_\gamma$，
$\operatorname{Tr}(R)$ 是 $RF_\gamma'$ 模 $F_\gamma$ 后的最高次系数。
因此这里读到的是整个有限纤维迹，而非一个辅助模素数的插值。

完整有理算子给
$$
\begin{gathered}
AB=BA,\qquad
\det(T-A)=T^4-T^2+1,\qquad
\det(T-B)=(T^2+1)^2,\\
\dim_K\langle v,Av,A^2v,A^3v\rangle=4,\qquad
Bv=-A^3v.
\end{gathered}
\tag{6}
$$
为明确最后一式的绝对相位，同一个原升幂基中
$$
Bv=-\delta
\begin{pmatrix}
2432/27\\2192/9\\4292/9\\1442/27
\end{pmatrix},
\qquad \delta=1+2\omega,
\tag{7}
$$
而 $A^3v$ 是右边相反向量。式(6)的四维秩在 $K$ 中精确读取，没有以目标素数抽样代替。

由 $v$ 的循环性与交换性，$B+A^3$ 杀掉四个基向量
$v,Av,A^2v,A^3v$。故完整空间上的结论是
$$
\boxed{
B=-A^3,\qquad A^4-A^2+I=0,\qquad A^6=-I,\qquad B^2=-I.
}
\tag{8}
$$
特别以 $(v,Av,A^2v,A^3v)$ 为基，两个完整算子已由如下有限呈示全部确定：
$$
A=
\begin{pmatrix}
0&0&0&-1\\
1&0&0&0\\
0&1&0&1\\
0&0&1&0
\end{pmatrix},
\qquad B=-A^3.
\tag{9}
$$
这避免把可重算的原矩阵数据另存文件；式(9)仍是完整算子，而不是仅其特征多项式。

## 3. 指定 H22 的谱范围

式(6)的循环性使 $H_{22}$ 的最小多项式准确为
$$
\Phi_{12}(T)=T^4-T^2+1=(T^2+\omega)(T^2+\omega^2).
\tag{10}
$$
所以 $H_{22}$ 本身既不是 $A$ 的特征向量，也不是 $B$ 的特征向量。
其 $B$ 循环空间是二维，其两算子联合生成空间是整个四维 (2)。
在包含 $i$ 的分裂域中，四个共同特征对准确为
$$
(\xi,-\xi^3),\qquad \Phi_{12}(\xi)=0.
\tag{11}
$$
由于 $H_{22}$ 对 $A$ 循环，它在四条特征线上均有非零分量。
在 $K$ 上，两块的准确投影可写为
$$
e_\omega=\frac{A^2+\omega^2 I}{\omega^2-\omega},\qquad
e_{\omega^2}=\frac{A^2+\omega I}{\omega-\omega^2};
\tag{12}
$$
两块各二维，且两投影的 $H_{22}$ 分量都非零。

共同 $\mu_6$ 特征线为空。这既由 (10) 与 $T^6-1$ 互素看出，
也由 $B^2=-I$ 与 $\mu_6$ 中没有平方为 $-1$ 的元素看出。
因此不能把 $H_{22}$ 只按 degree22 或含坏素数11，直接认成 R816 的原 $E_{-11}$／$V_{66}$ 算术线。
若要将 (11) 识别为完整 Hecke／Schwartz 家族，仍需逐一支付原 $2,3,11$ 的全部局部角色及绝对倍率；本篇不作这一额外认定。

对于一般 $b\ne0$，取 $\theta^6=b$。
由 $\sigma_b(z)=\theta^{-1}\sigma_1(\theta z)$、$x_b(z)=\theta^2x_1(\theta z)$，
基
$$
b^{3-j}\sigma_b^{22}X_b^j,\qquad 0\le j\le3
\tag{13}
$$
共同缩放为 $\theta^{-4}$ 倍的 $b=1$ 基。因此 (6)–(12)
完整运输到原 $b$ 来源；不是在变化的 $b$ 上重新选择一个特征向量。
本文的秩结论为特征零结论，后续若要在目标素数处使用循环基的单位性，
仍须保其固定分母与非零行列式的有限坏集。

## 4. 对原除 p 行的准确用途

R863(A22) 中的第一低卷积现在具有指定的四维输入 (1) 及完整有限作用 (8)，第二低连接配对仍原样保留。
本篇没有证明这两个配对的和非零，也没有使原 $\mathfrak B$ 与 (3) 无修正地交换。
因此原四条中央首必要条件没有被增加成四条共同特征线上的零条件。

实际可用的新信息是：必须保留 $H_{22}$ 的四个有限特征分量；
若使用其原 CM13 伴随，可以准确以 $-A^3H_{22}$ 代替；
若使用 CM13 两次，则准确为 $-H_{22}$。任何进一步跨源消元都须作用于 R863(A22) 的两个完整配对和同一原 frame。

## 5. 公开执行来源

- 脚本：[`check-r863-original-h22-full-cm-source.py`](../scripts/check-r863-original-h22-full-cm-source.py)。
- 实际命令：`python .../check-r863-original-h22-full-cm-source.py --workers=4`。
- 环境：Python 3.12，`python-flint==0.9.0`。依赖仅原 R732 与 R464 两个 producer，无生成数据输入。
- source commit：`afbf59efb25396efb1286ab193857e3652643add`。
- [公开 run 43836767572](https://github.com/Rogerhu12/math-research-public/actions/runs/43836767572)，job `133195218638`，全部完整纤维及精确算子检查 PASS。
- 脚本 SHA256：`31c7434e4478739fa26a6e6507798ac08fbf091f8fd9465d94b02939d7c06e07`。
- 完整输出 SHA256：`ce2d8bc3782fb2e858d90652b99e4d952815b1f66d9aa0aee6ed37cb09ea84c5`。
- 规范矩阵 SHA256：`bd856191b55d757d6a75d181a6bc11c8656f2134cc4a93da4b7a02c56ea04dca`。

所有矩阵均由脚本重建并留在公开日志；没有新增可重算输出数据文件。

参考：[R863 原连接伴随及 A.4–A.5](R863-original-balanced-frobenius-factor-and-partner-chain.md)；
[R732 原 CM13 完整算子](R732-original-type-five-full-cm13-and-two-eigenlines.md)；
[R816 原 V66 全角色与来源](R816-original-minus-eleven-rank-two-schwartz-and-degree66-source.md)。
