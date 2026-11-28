# R85 补充：端口响应复用的完整回代误差与小块验证

2026-11-28 UTC；analytic_construction。以下接 [R85](R85-complete-robin-to-actual-dn-and-fixed-metric-update.md) 的原 U、C、G 及全部节点/参数排列。没有新的矩阵、尾请求、BVP 或区间逆数值。新内容是可用已保存完整矩阵逐列回代支付的误差合同；不由小 S 的浮点条件数推断完整微分问题已可逆。

## 1. 近似基响应怎样传到原 64191 行

取声明的完整基矩阵 J；它可以是 R85 的同点 J_L，也可以是明确标注的旧点 frozen-chord J_0。假设已经按完整 U 的每列计算近似响应 Vhat，并为当前完整右端 b 算得 zhat。定义的是实际代数残差：

$$
 R_V=J\widehat V-U,\qquad r_z=J\widehat z-b.
\tag{1}
$$

给定实际使用的完整 slope 差矩阵 G，令小步骤 hhat 的残差为

$$
 r_s=(I+C\widehat V G)\widehat h-C\widehat z.
\tag{2}
$$

这里 (2) 针对所声明的实数乘积，须包括形成小矩阵与求解过程的舍入误差；不是只读小 LU 的停止标志。

置

$$
 \widehat x=\widehat z-\widehat V G\widehat h.
$$

则有

$$
 \boxed{(J+UGC)\widehat x-b
   =r_z-R_VG\widehat h-UG r_s.}
\tag{3}
$$

证明只需先算 $C\widehat x=\widehat h-r_s$，再把
$J\widehat V=U+R_V$、$J\widehat z=b+r_z$ 代入。全式没有用 J 的逆界，也没有要求 Vhat 是精确解。所有非终端行仍包含 r_z 和 R_V 的相应分量；不能只回代小 S。

特别地，若第 j 个完整基响应已有
$\rho_j\ge\|(R_V)_{:j}\|_\infty$，令 $a=G\widehat h$，便有

$$
 \|(J+UGC)\widehat x-b\|_\infty
 \le \|r_z\|_\infty+\sum_{j=1}^M\rho_j|a_j|
                    +\|G r_s\|_\infty.
\tag{4}
$$

最后一项使用 U 的无权 $\ell^\infty$ 范数1。若原回评采用一个固定的行尺度，应把同一个尺度同时施于 (1)、(3)、(4)，而不能只改变末端权重。逐分量版本是

$$
 |r|\le |r_z|+|R_V|\,|G\widehat h|+|U|\,|G|\,|r_s|.
\tag{5}
$$


这说明何时“旧全 J 的每列残差很小”仍不够：若小系统给出很大的 $G\widehat h$，它会真实放大这些残差。相反，一旦 (3) 的原完整回代足够小，线性步骤的后向误差已由它自己的原方程支付，不必先捏造一个全局 J 逆范数。后向误差本身仍不是非线性收敛、解的前向误差或严格微分逆证明。

实际浮点评价 (1)--(4) 只能先记为实测。若把它升级成严格上界，应对原稀疏点积及小块乘积使用明确的外包算术，或给出原 IEEE 运算次序的舍入预算；不能把普通 `max(abs(J@x-b))` 改标签成区间数。

## 2. literal小块可以廉价严格验证，但必须注明对象

令 $\widehat S$ 是保存的24维或25维小矩阵，T 为其一个保存的近似逆。把这两组 binary64 字面数当成精确 dyadic 数，若以有理运算或外包运算证明

$$
 \eta=\|I-T\widehat S\|_\infty<1,
\tag{6}
$$

则这个 literal 矩阵确实可逆，而且

$$
 \|\widehat S^{-1}\|_\infty\le
 \frac{\|T\|_\infty}{1-\eta},\qquad
 \kappa_\infty(\widehat S)\le
 \frac{\|\widehat S\|_\infty\|T\|_\infty}{1-\eta}.
\tag{7}
$$

证明：$T\widehat S=I-E$ 的 Neumann 级数收敛，且
$\widehat S^{-1}=(I-E)^{-1}T$。维数仅24或25，逐项 Fraction 点积可以避开“大矩阵严格求逆”的存储问题。

但是 $\widehat S=I+C\widehat V G$ 中 $\widehat V$ 可能只是近似基响应。式 (6) 严格证明的对象仅是保存的小矩阵，不能凭此推出原 $J+UGC$ 可逆，也不能把旧点 J 当成当前导数。对一个真实完整方向，仍使用第1节原完整回代。

各高度坐标大小差异明显时，可以事先记录正对角尺度 D_h，验证
$D_h^{-1}\widehat S D_h$。所有尺度必须非零并完整保留各模；这只是相似变换，不删除高模。不同尺度下的条件数不同，报告须带尺度，不能把某个坐标下较好的数字称为范数无关的性质。R85 的25维联合块另含原参数坐标，若缩放也必须逐项记录该参数的单位。

## 3. 真正微分小块还需哪些误差半径

若已有同点的完整响应包络

$$
 |A-\widehat A|\le \Delta_A,\qquad
 |G-\widehat G|\le \Delta_G,
$$

则 R85 的 $S=I+AG$ 相对中心 $S_0=I+\widehat A\widehat G$ 满足

$$
 |S-S_0|
 \le \Delta_A|\widehat G|+|\widehat A|\Delta_G
                       +\Delta_A\Delta_G=:\Delta_S.
\tag{8}
$$

如保存的是舍入后的中心 Sbar，还须把准确 $S_0-\mathrm{Sbar}$ 的绝对值加进 $\Delta_S$。对于近似逆 T，只要严格验证

$$
 \boxed{\bigl\||I-T\,\mathrm{Sbar}|+|T|\Delta_S\bigr\|_\infty<1,}
\tag{9}
$$

整个被包住的真实小块均可逆，其逆界仍由相应的 (7) 给出。25维联合块可以逐项使用同一检验，避免把两个接近的标量相减后只观察 $\chi_N$ 的浮点符号。

这些半径不能凭残差大小猜出。确实，若 J 可逆，

$$
 A-\widehat A=-C J^{-1}R_V
\tag{10}
$$

（这里 $\widehat A=C\widehat V$，符号与 (1) 一致）。故基响应的普通线性残差并不直接等于 $\Delta_A$；需要已经证明的投影逆/完整逆包络，或经验证的完整线性求解。一个可降低所需逆界精度的双侧形式是：若另有 $\widehat L$ 近似 $CJ^{-1}$，定义
$R_L=C-\widehat L J$，则

$$
 A-\widehat A=-\widehat L R_V-R_LJ^{-1}R_V.
\tag{11}
$$

右端余项含左右两个残差，而非只一个；但最后的 J 逆界仍不能省略。这里只给出准确的需付量，没有虚构该界已经存在。

同样，当前 native 返回的 heightJetJacobian 和 shooting residual 是实际数值输出；对完整已构造尾图的 metric、曲率、height 区间证书，并不自动包住“尾解随 H 改变”的导数。因此 $\Delta_G$ 还需同一有限 shooting 解分支的导数验证。此前两步长 $v_q$ 差分的一致性也只是数值核对，不能当成25维块中完整 q 列的严格误差半径。若用精确模型解析列，则其有限求积、完整 lift、moving chart 与原 mean 规则全部保留。

## 4. 下一实际执行的最小顺序

当前可先在独立进程中只冷读已经保存的完整 M24 CSR 和它自己的 c9c4906f…快照身份，逐列求 $\widehat V$，每列保存完整向量和原 J 回代标量。这个阶段不导入物理 Flow，不重建 J，不调用 native 尾，也不声称得到 accepted 点的导数。矩阵进程只承担原矩阵/因子、一个 RHS、一个方向和小 A；V 可逐列落入临时工作目录。

随后用原模型在实际要校正的共同网格上评价完整 F_L，再取已经严格绑定到该 H 的真实 packet 建 G 与 g。若原 packet 的 H 不相同，必须走原真实请求；不能按“差得很小”复用。用 R85 形成完整初猜，执行本条 (3) 的原矩阵回代与原非线性/domain 回评。原8outer和最终 physical-H 审计仍保持。

这一路能减少重复完整 Jacobian 装配，但不能承诺旧点 chord 收敛。其停止条件仍来自实际原残差、域和原求解门；若完整残差不降，应回到同点新 J 或别的真实输入，不能降低门或只报小块可逆。全 $\lambda$ 分支、固定 g 收敛与闭面完成均未由本补充支付。
