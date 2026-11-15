# R787 projective：消费原430位提升的数域共同分母重构

日期：2026-11-15。状态：独立消费者的证明与执行契约；尚未声明430位足以恢复原函数。

本篇保持 [R787 的原数学定义](R787-original-power5-relation-solver-method.md)、
[R786 的129阶全球认证](../results/R786-original-power5-sections-and-129-Laurent-recovery.md)，
以及原第4号映射、次数1206、原 $b$、原微分、尖点相位、全部常数和零平移。
只读取一个已经结束且完整认证至430位的 R787 checkpoint。
它不是新 Dixon 提升任务，不求新 Schur 逆，不替换仍在运行的原核心，
也不重新生成已成的1234行实前缀或任何 R781 Laurent 系数。

数学 RESULT 和成功文件名保持
R787-original-power5-function-relation、
p41-original-power5-function-relation-certificate.json、
R787-original-function-recipe.json.gz。
新任务的 core、source、configuration 和本方法 SHA 均必须如实独立；
原 R787 核心 SHA 不可冒充为新核心 SHA。

## 1. 原字段、原归一向量与完整认证

原 R781 字段使用
$$
L=\mathbb Q(B_{\rm fld},s),\qquad
B_{\rm fld}=\lambda b,\qquad s^2=-3,
\qquad
\mathcal O=\mathbb Z[B_{\rm fld},s].
\tag{787P.1}
$$
$f_B$ 为同一个首一整系数七次多项式。
因此 $\mathcal O$ 是 $L$ 中秩14的整阶；不需要声称它是最大整环或主理想环。
整基次序为 $B_{\rm fld}^i s^j$，$j=0,1$ 在外、$i=0,\ldots,6$ 在内。
任何乘积都先按 $s^2=-3$ 和原 $f_B$ 准确约化。
这与原280维字段的 $t$ 最内次序一致。

令 $M=\ell^{430}$，$\ell=1000000753$。
原430位产物含
$$
\bar a\in(\mathcal O/M\mathcal O)^{1234},\qquad
\bar c\in(\mathcal O/M\mathcal O)^{1214}.
\tag{787P.2}
$$
它们是同一共同 chart 的原归一向量，
而不是14个分支各自任取的核向量。
原 chart 的真实秩为1186，选定自由列记为 $f$：
$c_f=1$，其余非主元自由列为零。
原已证非零 minor 与 R786 的1186上界给特征零秩1186，
故该共同自由模式有唯一的 $L$ 解。

原稀疏整数核 $Z'$ 保持
$$
b=Z'c,\qquad
Z'_P=Z_p,\quad Z'_Q=d_ZI.
\tag{787P.3}
$$
这里只消费已完成的 $Z_p,d_Z,P,Q$；不调用原 Job 来补 missing cache。
原1234个 $82^{10}F_j$ 的129项实前缀也逐行原字节读取。
R786 索引与这些实行内的 R786_row_sha256 逐项相配，
不再读取或转换1234条旧 cyclotomic 数学行。

对任何候选整数向量 $(a',c')$，先准确求 $b'=Z'c'$。
原最终验算仍是
$$
246^3\kappa^{m+1}A'_{m-1}
+\sum_{j=0}^m R_{m-j}\kappa^jB'_j=0,
\qquad m=0,\ldots,128,
\tag{787P.4}
$$
其中 $A'_{-1}=0$，每条等式包含原20个 $L$ 坐标、280个有理坐标。
原 R781 field、$R_0,\ldots,R_{128}$、$\kappa^0,\ldots,\kappa^{129}$
及其逐阶段 SHA 链必须保持。
只有全部129条准确为零且 $b'\ne0$ 才恢复原 $y=A'/B'$。

## 2. 为什么一个 $L$ 分母可能节省所需精度

原 R787 按全部2448个 $L$ 未知数的34272个有理坐标分别作有理重构。
本消费者寻找同一个 $0\ne D\in\mathcal O$，使
$$
a'=Da,\qquad c'=Dc
\tag{787P.5}
$$
在原整阶基中的整数系数较小。
若先把 $D^{-1}$ 写成有理系数，乘法矩阵的伴随公式会引入
$N_{L/\mathbb Q}(D)$ 这个整数分母；
其有理坐标高度可能显著大于 $D$ 与各个 $Da_i,Dc_i$ 的高度。
(787P.5) 允许直接保留数域分母，不必先制造该范数分母。

这只是可节省精度的数学机制，**不证明本题的430位已经足够**。
真正共同分母集合是 $\mathcal O$ 的一个理想，未必主理想；
本任务只找其中一个非零元素，不宣称求出了其生成元或最短元素。
两个不同坐标还可能分别消掉共同分母的不同因子，
所以一个坐标的短分母不能直接作为全向量的成功证书。

## 3. 28维格只生成候选

设 $x\in\mathcal O/M\mathcal O$。
以行向量约定定义乘法矩阵 $R_x$：
$$
\operatorname{coeff}(\delta x)=
\operatorname{coeff}(\delta)R_x\pmod M.
$$
下面的整数格恰描述一个数域 numerator/denominator 的模关系：
$$
\mathscr L_x=
\left\{(\delta,n)\in\mathbb Z^{14}\times\mathbb Z^{14}:
n\equiv\delta R_x\pmod M\right\},
\qquad
\begin{pmatrix}I_{14}&R_x\\0&MI_{14}\end{pmatrix}
\text{ 是其行基。}
\tag{787P.6}
$$
因此未知分母虽只有14个坐标，直接使用的整数格维数是28。
多个探针同时约束时可形成 $14(r+1)$ 维格；首实现不需要大规模同时格。

对格的两块可施正整数权，以寻找不等高度的分子和分母。
LLL 的输出只用于列出有限个候选；每个输出候选都重新准确检查
$n-\delta x\in M\mathcal O$。
正确性不依赖“LLL 必然找到所需方向”、数值长度排序或某个未经证明的成功概率。
首实现还只保留在原14个 $\ell$ 分裂点均非零的 $\delta$，作为搜索策略；
原全向量确在 $\mathcal O\otimes\mathbb Z_\ell$ 中，
所以存在 $\ell$-单位的共同整数分母，但这不保证该策略当前找到它。

为给搜索使用一个固定、可核的矩形，写
$\omega_i\omega_j=\sum_k\mu_{ij}^k\omega_k$，取
$$
K=\max\left(1,\max_k\sum_{i,j}|\mu_{ij}^k|\right),
\qquad
\|uv\|_\infty\le K\|u\|_\infty\|v\|_\infty.
$$
选定正整数界 $N,D_{\max}$ 满足
$$
2KN D_{\max}<M,\qquad N,D_{\max}<M/2.
\tag{787P.7}
$$
若两个非零分母的分式各自满足这个同一固定矩形与同一个模关系，
则交叉乘积的全部系数既被 $M$ 整除，又严格小于 $M$，故两个 $L$ 分式相同。
这只是矩形内的唯一性；没有把未知真解的高度预设在矩形内。
实际搜索可使用若干预定的不同矩形，每个单独满足 (787P.7)。

## 4. 增量共同分母、有限搜索和准确出口

初始 $D=1$。对固定矩形与当前准确整阶元素 $D$：

1. 逐个计算 $D\bar c_i,D\bar a_i$，在固定14坐标中取模 $M$ 的中心代表。
   原自由列直接检查为准确的 $D$，其余自由列为零。
2. 若全部候选分子均在界 $N$ 内，形成完整 $(a',c')$，
   然后执行 (787P.3)–(787P.4)。
3. 若某个 $L$ 坐标太大，以该 $x=D\bar c_i$ 或 $D\bar a_i$ 作 (787P.6)，
   对每个保留的短向量产生新分母
   $$
   D_{\rm new}=D\delta\in\mathcal O.
   \tag{787P.8}
   $$
   **这里是原整阶中的准确乘积，不把 $D_{\rm new}$ 中心约化后冒称相同标度。**
   新分母的坐标超过 $D_{\max}$ 时，只淘汰这一搜索候选。
4. 每次更新都重新对同一个完整向量扫描，不能假设旧坐标在新分母下仍小。
   不同候选、矩形和已完成扫描均有独立身份；有限搜索路径原子保存。

一个候选不通过 (787P.4)，就记录其首个非零原关系，继续其余已经明确列出的路径。
预算耗尽保留当前路径；有限候选暂尽只记“本次未找到”，不写原函数已恢复，
更不能据此否定原准确关系存在。

若一个候选通过全部 (787P.4)，且在去内容之前准确满足
$$
c'_f=D\ne0,\qquad
c'_j=0\quad(j\text{ 是其余自由列}),
\tag{787P.9}
$$
则由原1186 chart 的唯一性，$(a',c')=D(a,c)$：
它是**同一原归一方向**的整倍数，不是碰巧给出另一个未绑定的核方向。
同时 $d_Z\ne0$ 保证 $b'=Z'c'\ne0$。
原129阶全球注入于是给原 $A'=yB'$。

在去掉 $a',b'$ 的共同整数内容 $e$ 后，成功 recipe 的原系数是
$a'/e,b'/e$；其相对原归一方向的倍数为 $D/e$。
所以 metadata 同时保存去内容前的 $D$ 和去内容后的 $D/e$，
不把后者仍写成 $D$。
原 recipe 的有理清分母字段记本次在 (787P.5) 之后没有额外有理清分母，
并增加 algebraic_L_denominator 字段明确真正的数域标度。
原 $82^{10}$、basis index、原 R786 producer 和原字段说明均逐项保留。
分子分母的共同缩放不会改变 $y$、$\beta$、CM 相位或原高度常数。

## 5. 源、配置、断点与输出

命令行：

~~~sh
python scripts/R787_projective_reconstruction.py \
  --config REQUEST \
  --method notes/R787-original-projective-reconstruction-method.md \
  --field-core scripts/R781_original_Laurent_prefix.py \
  --retained INPUT_ROOT --output OUTPUT --budget-minutes 300
~~~

最小输入分三目录：

- R787：原430位 lift、chart、selection、rational-blocks、
  1234条完整 real-power5-row，以及其原 manifest/run/core/public-input metadata。
  rational-blocks 内已有的逆矩阵只是原文件的一部分；新核心不使用它求解。
- R781：原134件闭包，即 field、000..129、manifest/certificate/run。
- R786：原 manifest/certificate/run/basis-index 四件。
  原 carrier 的1372成员先全部按原 SHA 核过，再只转交这批实际消费文件。

完整 source identity、结束状态及实际 exit 1 由包装层核查，
核心再核 manifest、原 configuration、每个消费文件的原 SHA/bytes、
原430位全残差标志以及完整字段/尺度/source 接缝。
禁止读取仍运行的 producer checkpoint 或填造实际成功状态。

请求含 core_sha256、projective_method_sha256、R787_method_sha256、
R786_proof_sha256、field_core_sha256、pinned_R787_configuration_sha256、
retained_source 与 checkpoint 的真实文件名。
原 R787 method SHA 为
1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b；
它继续定义原数学关系。本篇 SHA 另外绑定新重构策略。
新数学 tag 保原 retained_artifacts、field、basis_integer_scale 与全部必要原接口，
同时增加 projective_mode、真实旧 checkpoint identity 与新 core/source。
预算和最多搜索节点数只控制何时返回，不改变已有节点的数学身份。

所有新阶段使用 R787-projective- 前缀；原成功 recipe 使用既有文件名。
扫描、LLL 候选、候选系数、每阶准确展开/加权/零关系各自完整原子保存。
崩溃发生在阶段保存与队列更新之间时，续算先复用完整阶段再推进队列；
不得重新运行已经保存的格约化或准确验算。
最后的 stage_manifest 逐项列 file/bytes/SHA；未完成的 queue/current 另外引用。

成功 FINAL 必须包含原 R787 成功字段，另含
same_normalized_1186_direction_verified=true 与原430位 source；
未找到时 FINAL/receipt 的 complete 与所有成功旗标均不得为真。
函数恢复之外的 $\beta$、Picard、第二类 period、极理想、$\eta$ 和高度仍分别待真实消费者。
数学数据只进入当前活跃的一日 artifact，脚本/参数/run/SHA 才进入 Git。

## 依据

- R781（2026）、R786（2026）、R787（2026）：原字段与尺度、已成前缀、共同 chart、全部129阶认证。
- M. H. M. Jayantha Suranimalee，*Linear Algebra over Finitely Generated Fields and Rings*，
  Kaiserslautern 博士论文，2021，§§1.3.5–1.3.6：
  [作者论文原件](https://kluedo.ub.rptu.de/files/6560/dissertation_Suranimalee.pdf)。
  其中给出数域分母格及增量共同分母思路。本篇对实际原整阶、来源和最终全关系认证另作上述直接证明；
  不采用任何未在本题核实的成功高度界。
- python-flint 0.9.0 官方 [fmpz_mat.lll 文档](https://python-flint.readthedocs.io/en/latest/fmpz_mat.html)：
  格约化只作候选生成，所有必要模关系与最终字段等式仍准确核对。
