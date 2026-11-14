# R288 方法附录：五位模型排除全部四位局部正 primitive frame

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：本稿的局部正分解障碍已证明。它不是逐位泄漏界的反例，也不是普通或加强相邻序的反例。** 不把局部向量张成误当成正 Parseval 分解；下文给出完整物理度量、唯一分解和一个整数行列式证书。

## 1. 被检验的充分条件

在有限正权 Boolean 模型中取
\[
d=\sum_i b_iE_i,\quad K_s=\ker d\cap\mathcal H_s,
\quad P=P_{K_s},\quad N_i=P n_i|_{K_s}.
\]
如果存在 Parseval frame \((v_\alpha)_\alpha\subset K_s\)，使
\[
P=\sum_\alpha v_\alpha v_\alpha^*
\tag{1.1}
\]
且每个 \(v_\alpha\) 的全部物理支持仅用至多 \(2s\) 个坐标，那么
\[
\sum_iN_i^2\succeq\frac{s}{2}I_{K_s}.
\tag{1.2}
\]
这里“支持于坐标集 \(A\)”指向量只含 \(e_I\)，\(I\subset A\)，不指仅有 \(2s\) 个非零系数。

证明：对 \(f\in K_s\)，有
\[
\begin{aligned}
\sum_i\|N_if\|^2
 &=\sum_\alpha\sum_i|\langle v_\alpha,n_if\rangle|^2\\
 &\ge\sum_\alpha\frac{1}{2s}
   \left|\sum_i\langle v_\alpha,n_if\rangle\right|^2
 =\frac{s}{2}\sum_\alpha|\langle v_\alpha,f\rangle|^2
 =\frac{s}{2}\|f\|^2.
\end{aligned}
\]
这是一个有效充分条件，但下文证明它不对所有真实正权模型成立。允许在同一局部子空间内使用任意多 frame 向量也不能消除障碍。

## 2. 五位模型与完整去权度量

物理坐标为 \(0,1,2,3,4\)，取
\[
s=2,\qquad (b_0,b_1,b_2,b_3,b_4)=(\sqrt t,1,1,1,1),\qquad t>0.
\]
\(\mathcal H_2\) 的物理正交归一基按
\[
01,02,03,04,12,13,14,23,24,34
\tag{2.1}
\]
排序。令 \(D\) 为无权删除矩阵，亦即 \(D_{i,I}=1_{i\in I}\)。定义
\[
T e_I=(b_I)^{-1}e_I,\qquad W=T^*T,
\qquad W_{I,I}=\begin{cases}t^{-1},&0\in I,\\1,&0\notin I.\end{cases}
\]
真实 primitive 空间是 \(K_t=T\ker D\)，并非给无权核免费配欧氏度量。对任意满列秩矩阵 \(K\) 且 \(\operatorname{Ran}K=\ker D\)，完整物理正交投影是
\[
P_t=TK(K^*WK)^{-1}K^*T.
\tag{2.2}
\]
记去权后的投影形式
\[
\widetilde P_t=T^{-1}P_tT^{-1}
                  =K(K^*WK)^{-1}K^*.
\tag{2.3}
\]
这里没有把 \(\widetilde P_t\) 当成欧氏正交投影。

## 3. 五个局部子空间及分解唯一性

对任意四元组 \(A=\{a<b<c<d\}\)，定义完整物理列中的无权局部核基
\[
u_A=e_{ab}+e_{cd}-e_{ac}-e_{bd},\qquad
v_A=e_{ab}+e_{cd}-e_{ad}-e_{bc},\qquad U_A=[u_A,v_A].
\tag{3.1}
\]
直接删除可见 \(DU_A=0\)，两列独立，且张成四位限制的整个二维核。真实局部子空间是 \(\operatorname{Ran}(TU_A)\)。少于四位的出生二 primitive 核为零：三位的删除矩阵行列式为 \(-2\)，两位或更少直接核为零。

因此，任何满足 (1.1) 的四物理位局部正分解必可合并为
\[
P_t=\sum_{|A|=4}TU_AX_AU_A^*T,\qquad X_A\succeq0,
\tag{3.2}
\]
等价于
\[
\widetilde P_t=\sum_{|A|=4}U_AX_AU_A^*.
\tag{3.3}
\]
对实对称块写
\(X_A=\bigl[\begin{smallmatrix}\alpha_A&\beta_A\\\beta_A&\gamma_A\end{smallmatrix}\bigr]\)。按
\[
0123,0124,0134,0234,1234
\tag{3.4}
\]
排列五块，再按每块 \((\alpha,\beta,\gamma)\) 排列未知量。线性映射 (3.3) 的一个 \(15\times15\) 整数子矩阵由以下输出条目选取：
\[
\begin{gathered}
(01,01),(01,02),(01,03),(01,12),(01,13),\\
(02,02),(02,03),(02,12),(02,13),\\
(03,03),(03,12),(03,13),\\
(12,12),(12,13),(13,13).
\end{gathered}
\tag{3.5}
\]
其行列式恰为 \(-2\)。这个整数证书可由 (3.1) 直接构造：\(\alpha_A,\beta_A,\gamma_A\) 三列分别为 \(u_Au_A^*,u_Av_A^*+v_Au_A^*,v_Av_A^*\) 的指定条目。[随附精确脚本](../notes/2026-11-14-local-positive-frame-obstruction-789f-next.py)以精确整数计算该行列式；无需浮点秩判断。

故 (3.3) 的实对称分解至多有一组。若存在复 Hermitian 正块解，对全部块取实部即得同一实目标的实对称正块解，因此只需排除这个唯一的实解。

## 4. 唯一分解与负块

令
\[
J=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\succ0.
\]
(3.3) 的唯一解为
\[
\boxed{
X_A=\begin{cases}
\dfrac{t}{4(t+2)}J,&0\in A,\\[5pt]
\dfrac{4-t}{12(t+2)}J,&A=\{1,2,3,4\}.
\end{cases}}
\tag{4.1}
\]
可用 (2.3) 逐条核验 (4.1)。另一种完全免逆的核验是置右端和为 \(S_t\)，检验
\[
DS_t=0,\qquad S_tWK=K.
\tag{4.2}
\]
由 \(S_t=S_t^*\) 和第一式，存在唯一实对称 \(A_t\) 使 \(S_t=KA_tK^*\)；第二式给 \(A_t(K^*WK)=I\)，即 (2.3)。随附脚本直接精确核验 (4.2)，不是只在某个 \(t\) 数值点求解。

当 \(t>4\) 时，不含第零位的唯一块严格负定，因此 (3.2) 不可能由正块实现。具体取 \(t=9\)，即正权 \((3,1,1,1,1)\)，已给一个完全有限的障碍。\(t=4\) 时该块为零；\(0<t<4\) 时五块均正定。

这一失败保留了整个真实物理投影与源度量。它不能由“无权局部向量张成，经对角变换仍张成”修复，因为所缺的是正 tight 分解，而不是线性张成。

## 5. 原泄漏命题在此模型中没有失败

为明确区分目标与充分条件，以上同一模型中真实算子 \(\sum_iN_i^2\) 的两个特征值为
\[
\lambda_{(2,2)}=\frac{2(t+1)}{t+2}\quad(\text{重数 }2),\qquad
\lambda_{(3,1)}=\frac{5t^2+10t+21}{3(t+2)^2}\quad(\text{重数 }3).
\tag{5.1}
\]
两者对 \(t>0\) 都严格大于 \(1=s/2\)：
\[
\lambda_{(2,2)}-1=\frac{t}{t+2}>0,\qquad
\lambda_{(3,1)}-1=\frac{2t^2-2t+9}{3(t+2)^2}>0.
\]
第二个分子是 \(2(t-\tfrac12)^2+\tfrac{17}{2}\)。这些特征值可从完整五维源矩阵
\[
N_i^{\mathrm{coord}}=(K^*WK)^{-1}K^*Wn_iK
\]
的特征多项式直接精确得到，脚本同时核验其二次、三次因子；源坐标不正交不改变特征值，且算子相对 \(K^*WK\) 自伴。

故本稿排除的是“所有 \(2s\) 位局部 primitive 子空间有正 Parseval 合成”这条加强路线。一般正权的 \(\sum_iN_i^2\succeq(s/2)I\) 仍需证明或真实反例，本稿没有给它任何一般结论。

## 6. 精确复核

运行保存的精确脚本：

```sh
python topics/invariant-subspace-problem/notes/2026-11-14-local-positive-frame-obstruction-789f-next.py
```

脚本仅做整数/有理函数运算：核基、局部二维核、\(-2\) 的线性唯一性子式、符号恒等式 (4.2)、以及 (5.1) 的特征多项式。它不依赖有限参数扫描，也不改变任何仓库追踪文件。
