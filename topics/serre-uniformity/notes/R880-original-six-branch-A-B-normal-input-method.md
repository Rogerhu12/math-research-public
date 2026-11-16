# R880 执行附记：原同 \(s\) 七分支中的其余十二个 \(A/B\) normal 右端

日期：2026-11-16。本文固定原 \(p=41\)、辅助素数
\(\ell=1000000753\)、原 \(s\) 剩余值 \(99932770\) 及原
\(\zeta\) 剩余值 \(549966761\)。本项是
[R880 有界代表来源](R880-original-D-pencil-reuse-and-common-cusp-RR-inputs.md)
§7 的有限输入续接。原 branch 0 的 \(A/\tau^5\) 已由
[R877 单 A 消费者](R877-original-canonical-A-single-normal-RHS-method.md) 完成，
\(B/\tau^5\) 已由原 R827 完成。本项仅构造其余六个 \(b\) 分支的十二个
normal 向量，并保每个向量的准确特征零单位解含义。

最终结果名为 `R880-original-six-branch-A-B-normal-inputs`；
代码 `R880_original_six_branch_A_B_normal_inputs.py`。
旧 R880、R824、R827、R877 的配置不改成新标签。

## 1. 来源及原规范

系数域仍为 \(L=K(b)\)、\(K=\mathbf Q(\zeta)\)。原整数生成元
\(B_{\rm fld}=\lambda b\)，\(s=1+2\zeta\)、\(s^2=-3\)。
所有分支通过原 R787 selection 的十四个
`roots_B_s` 识别，不能凭数组下标假设同 \(s\) 的七支排列。
读取其中 \(s=99932770\) 的七支，保原 branch 0 的
\((B_{\rm fld},s)=(3197390,99932770)\)，另外六支各读取一个
原 R824 五次 profile。

每个 profile 的 `kernel_free_columns` 有28项。仅取值为1186的
位置，不取第一列、不另选新的自由方向。冻结 R824 的这列正是原 R787
`initial_A`、`initial_C` 的字节所代表的模向量；其字段
`original_reserved_column_retained_without_new_lift=true` 明确记录这一点。
原 R824 没有对这个保留方向重做提升。每支还保存原1186单位子式和
原 R787 branch 的具体规格。新消费者核原 chart 的行列次序、其余自由坐标
为零、所选自由坐标为一，原 Z 的身份也必须完全相同。

原全局特征零对象仍由
[U.1 原单位图](R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)
及 [R849](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)
的2420阶选行解定义：
\[
 (A^{[j]},C^{[j]})=\iota_0\sigma^j(A,C),\qquad
 B^{[j]}=ZC^{[j]}.
 \tag{6B.1}
\]
这里上标仅描述在相应剩余嵌入中的值；真实准确对象是
\(\sigma^j A,\sigma^j B\)，并非把模向量宣布为特征零系数。
原完整核维数28及单位选行子式保证原归一方向的唯一性。因此应用
\(\sigma^j\) 后仍是同一自由值1186为一的单位解，不会多出未知标量。

## 2. 真正的 Galois 次序

从 R849 已成准确图中的 `original_Galois_automorphism_definition` 读取
\[
 \sigma(b)=a(b)+\zeta\,c(b), \qquad \sigma(\zeta)=\zeta ,
 \tag{6B.2}
\]
其中两项的有理多项式分子、分母保原字节。该节点已声明原 \(\sigma\) 的
阶为7，并固定 \(z,w\) 及原272正规基。

公开数学核心在 \(\ell\) 处核各实际有理分母、\(\lambda\) 为单位，按
\(b=B_{\rm fld}/\lambda\) 评价 (6B.2)，并验证原同 \(s\) 的七支构成从
branch 0 出发的一个七循环。只有完成这一步，才给每个原 branch 赋
\(\sigma^j\) 的准确位置。纯 IO intake 仅保真实 root 表和原分支号，
不在运输阶段推算新 roots 或假定排序。

原 \(\sigma\) 固定 \(K\)，所以六支均使用同一个 \(K\) 剩余嵌入；
不存在另换 \(\zeta\) 后拼合矩阵的操作。正常基的
\(e_{73}\) 坐标、\(\tau,\sigma\) 命名及 R853 的另一反线性作用都不参与本项。

## 3. 原 Z 展开与共同 F69

令原 \(V_5\) 基有1234项，原常数核自由列1214项。
原 Z 的20个 pivot 行与1214个 free 行满足
\[
 (B^{[j]})_{P}=Z_P C^{[j]},\qquad
 (B^{[j]})_{Q}=d_Z C^{[j]}.
 \tag{6B.3}
\]
其中 \(Z_P\) 与 \(d_Z\) 是原
`R787-prime-1000000753-rational-blocks.json.gz` 的整数。
直接进行这一展开；不再插入 common-clear、\(\lambda^i\)、
primitive content 或新的共同分母。

原 \(V_5\) 的已含整数尺度是
\[
 82^{10}=13744803133596058624.
 \tag{6B.4}
\]
R877 已保存20个完整 F69 分块，每块至多64个原基列，
最后一块保至1234列。它们的行次序是
\[
 (n,r),\qquad 0\leq n\leq68,\quad0\leq r\leq19.
 \tag{6B.5}
\]
即共1380个原短坐标，包含常数块。这些数组只读取；
本项不重做1234个 real 行的相位转换或模 reduction。

将六个支的向量按真实分支号固定排列，组成
\[
 {\cal V}=[A^{[j_1]},B^{[j_1]},\ldots,A^{[j_6]},B^{[j_6]}]
       \in\mathbf F_\ell^{1234\times12}.
\]
每个已成 F69 分块 \(F_a\) 仅乘相应十二列切片，原子保存
\(F_a{\cal V}_a\)。二十块相加得
\[
 {\cal R}=F_{69}{\cal V}\in\mathbf F_\ell^{1380\times12}.
 \tag{6B.6}
\]
各右端均绑定其原 profile、free1186和原 Z。
branch 0 的旧 A/B 右端不重算。

## 4. 一个旧 S5 逆，十二列完整回代

原 R842 的 \(S_5\) 矩阵已经完整保存：
\[
 S_5\in\mathbf F_\ell^{1380\times1234}.
\]
原 R827 同一素点的1234阶选行逆 \(U=S_5[I,:]^{-1}\) 及两侧乘回
是既成来源。读取这些原数组，**不新求逆、不重验旧乘法等式**。
新计算为
\[
 X=U{\cal R}[I,:],\qquad S_5X={\cal R}.
 \tag{6B.7}
\]
第二式须实际核全部 \(1380\times12\) 项。
不能只验被选1234行，不能用未成 R815 矩阵作替代。

原 normal 次数为
\(\epsilon=(0,1^{144},2^{127})\)，原 S5 列映射
\[
 (a,k),\qquad0\leq a<272,\quad0\leq k\leq5-\epsilon_a
 \tag{6B.8}
\]
恰有1234项。按该原映射将每个 \(X\) 列还原为
\(6\times272\) 系数数组，超出 \(5-\epsilon_a\) 的槽必须为零。
于是得到同 \(\sigma^j\) 的两条正规多项式向量
\[
 v_{A,j}(z),v_{B,j}(z),\qquad
 \sigma^j y=\frac{v_{A,j}\cdot\beta}{v_{B,j}\cdot\beta}.
 \tag{6B.9}
\]

准确语义是原 S5 选行单位解施于准确 U.1 共轭右端。
R877 已证明原 S5 是整个 \(V_5\) 的完整基；因此各准确右端在它的像内。
真实单位选行子式给准确坐标的 \(\ell\) 整性，(6B.7) 是这些坐标的
实际剩余像认证。它不声称已将1234个准确有理函数系数全部展开。

每支保存 A、B 的非零模向量、完整1380回代和原权界。
这证明 B 作为原函数不为零；不宣称它在任一特定纤维是单位。
后继若要除以 B，须在所需完整有限代数中另核其单位性。

## 5. 成功、恢复及留存

输出阶段统一为 `R880-six-branch-*.json.gz`：

1. 完整原来源/原尺度审计；
2. 真 \(\sigma\) 七循环与原 branch 对应；
3. 六个原1186向量/原 Z 展开阶段；
4. 二十个新十二 RHS 部分和、最终1380×12右端；
5. 十二列 S5 解和全1380回代；
6. 六组 normal A/B，以及含 branch 0 旧引用的七组 Galois index。

每个完成阶段都原子写入，固定新数学标签，预算/运输位置不入标签。
当前断点独立保存，明确 `complete=false`。硬断后的完整块按原 SHA、
新标签及全部真实依赖直接复用；历史 false FINAL 不会使已推进的新块失效。

新 FINAL 仅在十二 RHS、十二列完整回代及七循环都实际完成后为 true。
它分别报告已成的七组正规输入、尚未展开的特征零系数、未计算的七组
有界 D*、五个原 \(L_j\) 的128/144 RR空间和高度。后几项保持 false。
不把正常输入完成替代原 Picard 求核，不把辅助素点结果写成原41高度值。

首请求预算仅控制实际可运行时间；所有新算术只在公开仓库 Actions。
Git 中只保存这份方法、源码、请求和工作流；原矩阵与模数据只在一日
artifact 中留存。纯 IO intake 对原 selected carrier 的所有成员逐 SHA 核后
只续传必要原叶，不因通用旧 guard 搬回已经不需要的1234个大原 Fourier 文件。
