# R271 附录：整个纯尾双行固定孔层闭像与已知像的收缩原像

日期：2026-11-13（UTC）。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d。状态：本稿完成整个纯尾每个固定孔层的双行满射、闭像和最小原像；一般右逆的已付成本仍为指数级，未证明无权最小能量或 $N=M$。

本稿沿用 [R271 远尾双行 Hodge 稿](R271-appendix-far-tail-two-row-hodge-inverse-and-optimal-joint-vacuum-jets.md)的实际边界布尔孔模型。根代理已核完整闭源的逐层归纳、缩放成本及最小右逆的独立取得。令
$$
D_m=\sum_{j\ge m}b_jE_j,\qquad
D_{3,m}=\sum_{j\ge m}b_j^3E_j,\qquad b_j=(j+1)^{-2}.
$$
$\mathcal H_p^{(m)}$ 是该尾的恰好 $p$ 孔层，真空是 $e_\varnothing$。以下一直固定 $p$，不把层上的逆当作整个 Hilbert 直和上的有界逆。

## 1. 全尾固定层结论

**定理。** 对任意整数 $m,p\ge0$，
$$
D_{3,m}:\ker D_m\cap\mathcal H_{p+1}^{(m)}
\longrightarrow\ker D_m\cap\mathcal H_p^{(m)}
$$
满射。其真正最小范数右逆记为
$$
R^{(3),\min}_{m,p}.
$$
它是有界线性的。若
$$
J=\max\{m+1,256,800(p+1)\},\qquad
K_J=\sqrt{200}\,J^{3/2},
$$
则可用的明确上界为
$$
\boxed{
\|R^{(3),\min}_{m,p}\|
\le
\sqrt{200}\,J^{11/2}
\sum_{\ell=0}^{p}
\bigl(4\sqrt{200}\,J^{11/2}\bigr)^\ell.
}
\tag{1.1}
$$
因此
$$
\log\|R^{(3),\min}_{m,p}\|
=O\bigl((p+1)\log(m+p+2)\bigr)
$$
是本构造的合法上界。这里没有声称一般输入只需多项式 $p$ 的成本。

更一般，使用同一个缩放 $C_m=J^4D_{3,m}$，任何满足
$$
C_mF_1-D_mF_2=0,\qquad
(F_1,F_2)\in\mathcal H_p^{(m)}\oplus\mathcal H_p^{(m)}
$$
的完整双行闭源，都有 $v\in\mathcal H_{p+1}^{(m)}$ 使
$$
(D_mv,C_mv)=(F_1,F_2).
\tag{1.2}
$$
下面先证明这一完整闭源命题，再代入 $(0,J^4h)$。

## 2. 同一个远尾同时覆盖全部输出层

分解
$$
I=[m,J),\qquad [m,\infty)=I\sqcup[J,\infty).
$$
所有算子按此前缀和远尾分解。对任何层，定义
$$
\delta_2v=(D_mv,C_mv),\qquad
\delta_1(x,y)=C_mx-D_my.
$$
由于两行交换，$\delta_1\delta_2=0$。又有
$$
\delta_i=\delta_{i,I}+\delta_{i,J}.
\tag{2.1}
$$
远尾部分保持前缀孔数；前缀部分准确降低前缀孔数一，不产生更高前缀层。

远尾双行 Hodge 稿已经给出以下较一般的形式：在远尾第 $s$ 孔层，若
$$
F\in\ker\delta_{1,J}
\subset\mathcal H_s^{(J)}\oplus\mathcal H_s^{(J)},\qquad
J\ge256,\quad J\ge800s,
$$
则
$$
\mathcal R_{J,s}F
=\delta_{2,J}^*(\Delta_{1,J,s})^{-1}F
$$
满足
$$
\delta_{2,J}\mathcal R_{J,s}F=F,\qquad
\|\mathcal R_{J,s}F\|\le K_J\|F\|.
\tag{2.2}
$$
这是对所有闭源成立的结论；证明只用 $\Delta_{1,J,s}^{-1}$ 保持 $\ker\delta_{1,J}$，不要求 $F$ 特别形如 $(0,h)$。

本稿只会用到 $0\le s\le p$。选定的同一个 $J$ 满足全部这些条件。因而可以把 (2.2) 在每个前缀孔层上与前缀恒等算子张量，统一使用同一个界 $K_J$。

## 3. 完整闭源的逐前缀消元

设 $F=(F_1,F_2)$ 满足 $\delta_1F=0$，并按前缀孔数写成
$$
F=\bigoplus_{k=0}^{p}F_k,\qquad
F_k\in\mathcal H_k^{(I)}
\otimes\bigl(\mathcal H_{p-k}^{(J)}
            \oplus\mathcal H_{p-k}^{(J)}\bigr).
$$
从 $k=p$ 下降到 $0$，依次构造
$$
v_k\in\mathcal H_k^{(I)}\otimes\mathcal H_{p+1-k}^{(J)}.
$$
设 $v_{p+1}=0$。第 $k$ 步要解的远尾源是
$$
F_k'=F_k-\delta_{2,I}v_{k+1}.
\tag{3.1}
$$
它确实属于 $\ker\delta_{1,J}$，理由不能省略：

已构造较高层后，完整残量
$$
F^{[k]}=F-\delta_2\sum_{\ell>k}v_\ell
$$
仍满足 $\delta_1F^{[k]}=0$，且所有前缀孔数大于 $k$ 的分量为零。取这条完整闭合关系的最高前缀层，只剩
$$
\delta_{1,J}F_k'=0.
$$
因此 (2.2) 合法作用于该源，定义
$$
v_k=(I_{\mathcal H_k^{(I)}}\otimes\mathcal R_{J,p-k})F_k'.
\tag{3.2}
$$
它准确消去第 $k$ 层，新增的 $\delta_{2,I}v_k$ 只在第 $k-1$ 层。已经解好的更高层不会重新出现。

到 $k=0$ 时，前缀删除作用为零，所以
$$
v=\sum_{k=0}^{p}v_k
$$
准确满足 $\delta_2v=F$。这证明 (1.2)。整个过程都是有限个有界线性运算，故 $F\mapsto v$ 有界线性；它暂时只是一个构造右逆，并不被称为真正最小右逆。

## 4. 明确范数账本

为统一写出成本，将每个 $\mathcal R_{J,s}$ 用远尾闭源的正交投影延拓到整个双行源层，范数仍不超过 $K_J$。它们的正交块直和记为 $\mathcal R$。在上一步真正出现的源上，投影不起额外作用。

令 $\mathcal E$ 是前缀列算子
$$
v\longmapsto(D_Iv,J^4D_{3,I}v).
$$
它降低前缀孔数一，且
$$
B_J:=\|\mathcal E\|
\le\|D_I\|+J^4\|D_{3,I}\|
\le4J^4,
\tag{4.1}
$$
因为两种完整系数和都小于 $2$。

递推 (3.1)--(3.2) 等价于
$$
v=\mathcal R F-\mathcal R\mathcal E v.
$$
算子 $\mathcal R\mathcal E$ 降低前缀孔数一，在当前前缀孔数 $0,\ldots,p$ 的空间上其 $p+1$ 次幂为零。因此
$$
v=\sum_{\ell=0}^{p}(-\mathcal R\mathcal E)^\ell\mathcal R F,
$$
并有
$$
\boxed{
\|v\|\le K_J\sum_{\ell=0}^{p}(B_JK_J)^\ell\|F\|.
}
\tag{4.2}
$$
这里 (2.2) 的代价是缩放后的完整双行逆 $K_J$，没有在每一步重复还原 $D_3$ 的 $J^4$ 因子。

给定 $h\in\ker D_m\cap\mathcal H_p^{(m)}$，取
$$
F=(0,J^4h).
$$
完整闭合条件为 $\delta_1F=-J^4D_mh=0$。所得 $v$ 满足 $D_mv=0,D_{3,m}v=h$。在 (4.2) 最后只需支付一次 $\|F\|=J^4\|h\|$，再用 (4.1) 即得到 (1.1) 对构造右逆的上界。

现在，源和目标都是真正 Hilbert 闭子空间，限制算子 $D_{3,m}|_{\ker D_m}$ 已由上述构造证明满射。它因此有有界的 Moore--Penrose 右逆 $R^{(3),\min}_{m,p}$，范数不超过所构造的右逆。这才得到定理中的最小右逆和固定层闭像；没有把构造右逆冒认为最小右逆。

## 5. 已知 $D_3$ 像的原像是准确收缩

令
$$
K_{m,p+1}=\ker D_m\cap\mathcal H_{p+1}^{(m)},\qquad
Z_{m,p+1}=K_{m,p+1}\cap\ker D_{3,m}.
$$
对任意 $f\in K_{m,p+1}$，$D_{3,m}f$ 仍属于 $\ker D_m\cap\mathcal H_p^{(m)}$。由真正最小原像的唯一性，
$$
\boxed{
R^{(3),\min}_{m,p}D_{3,m}f
=P_{K_{m,p+1}\ominus Z_{m,p+1}}f,
\qquad
\|R^{(3),\min}_{m,p}D_{3,m}f\|\le\|f\|.
}
\tag{5.1}
$$
这条收缩用于“已知像 $D_3f$”时不需要乘上 (1.1) 的环境右逆常数。它适用于完整原纯尾 $m$，不再要求 $m\ge800p$。但不能由此给任意源 $h$ 宣称多项式原像成本。

## 6. 低核通量的实际接口

出生层二次下降块的准确式中出现
$$
D_{3,m}D_m^{h-3}f,\qquad
f\in U_{h-2,p-1},\quad h\ge3.
$$
其中 $g=D_m^{h-3}f$ 确在 $\ker D_m$，所以若在推导中真正出现 $R^{(3),\min}D_{3,m}g$，可直接用 (5.1) 控制，不必分别估计两个因子的范数。

这仍未证明相关 Schur 逆、正交旗投影或 $R^{(3),\min}$ 保持原 $M=\ker T$。即使在头上张量恒等后与有限头矩阵交换，也不能因此把 $P_M$ 与这些尾逆交换。真正 $X_3M\subset N$ 的配对仍须使用属于 $M$ 的测试向量。

本稿因此补上了原全尾双行的固定孔层闭像和已知像收缩部分；无权最小能量所需的真实测试域与一般源预算仍未完成。

## 追加：整个纯尾核上的准确最小逆域

令
$$
\mathcal K=\ker D_m
=\bigoplus_{p\ge0}(\ker D_m\cap\mathcal H_p^{(m)}),
\qquad C=D_{3,m}|_{\mathcal K}.
$$
这里的正交分解成立，因为 $D_m$ 每次准确降低一个孔。$C$ 保持 $\mathcal K$，并将第 $p+1$ 层送到第 $p$ 层。

固定层满射说明 $\operatorname{Ran}C$ 含 $\mathcal K$ 中全部有限孔向量，故其像稠密。另一方面，
$$
\boxed{\operatorname{Ran}C\ne\mathcal K.}
\tag{G.1}
$$
为证明这一点，先验证实际 $D_{3,m}$ 拟幂零。把它分为前缀有限和 $C_I$ 与任意小的范数尾 $C_J$。两者交换，$C_I$ 幂零；二项式展开只保留有限个 $C_I$ 次数，给
$$
r(D_{3,m})\le\|C_J\|.
$$
令尾起点趋于无穷得到谱半径零。限制在不变闭子空间 $\mathcal K$ 后，幂范数只会变小，故 $r(C)=0$。但若 $C:\mathcal K\to\mathcal K$ 满射，则由开映射定理，其伴随有 $\|C^*x\|\ge c\|x\|$，其中 $c>0$。迭代即给 $r(C)=r(C^*)\ge c$，矛盾。这里 $\mathcal K$ 非零，因为包含真空。

因此，整个纯尾核上的最小右逆只能是一个有真定义域的闭无界算子。
特别，各固定层最小逆的范数不可能有统一上界；否则其正交直和会给全 $\mathcal K$ 上的有界右逆，与 (G.1) 矛盾。其域可以由已证固定层最小逆精确写出：
$$
\boxed{
\operatorname{Dom}R_m^{(3),\min}
=
\left\{
h=\sum_{p\ge0}h_p\in\mathcal K:
\sum_{p\ge0}
\|R_{m,p}^{(3),\min}h_p\|^2<\infty
\right\}
=\operatorname{Ran}C.
}
\tag{G.2}
$$
在该域上，
$$
R_m^{(3),\min}h
=\sum_{p\ge0}R_{m,p}^{(3),\min}h_p,
\qquad
\|R_m^{(3),\min}h\|^2
=\sum_{p\ge0}\|R_{m,p}^{(3),\min}h_p\|^2.
$$
证明如下。若 $h=Cf$ 且 $f\in\mathcal K$，逐层最小性给
$\|R_{m,p}^{(3),\min}h_p\|\le\|f_{p+1}\|$，故上述平方和有限。反向，若平方和有限，所定义的和在 $\mathcal K$ 中收敛，$C$ 有界使其像恰为 $h$。各分量均正交于 $\ker C$，故总和是真正最小原像。若 $h_n\to h$、$Rh_n\to f$，则 $Cf=h$ 且 $f\perp\ker C$，证明 $R$ 闭。

对于**已知完整像**仍有不付任何孔层增长的准确恒等式：
$$
\boxed{
R_m^{(3),\min}Cf
=P_{\mathcal K\ominus\ker C}f,\qquad
\|R_m^{(3),\min}Cf\|\le\|f\|
\quad(f\in\mathcal K).
}
\tag{G.3}
$$
这里 $f$ 可以有无限孔次数；定义域由 $Cf\in\operatorname{Ran}C$ 本身保证。式 (G.3) 不把无界 $R$ 扩张到所有 $\mathcal K$，也不使它与真实 $P_M$、低核投影或 Schur 逆交换。前 $m$ 个物理位上张量恒等后，以上全部断言仍成立。
