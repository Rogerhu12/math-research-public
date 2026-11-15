# R787 projective v2：直接双探针候选与原129阶准确出口

日期：2026-11-15。状态：独立新候选消费者；本篇没有声明原函数已恢复，也不声明430位足够。

本篇继续使用 [原 R787 关系定义](R787-original-power5-relation-solver-method.md)、
[R786 原129阶全球认证](../results/R786-original-power5-sections-and-129-Laurent-recovery.md)
和 [第一版共同数域分母接口](R787-original-projective-reconstruction-method.md) 的
原 $L$、$B_{\rm fld}=\lambda b$、$s^2=-3$、1234个原截面、$82^{10}$ 尺度、
$Z'$、原映射编号4、次数1206、原尖点相位与零平移。
旧28维 LLL、原430位提升、原1234行准确前缀及原 Laurent 递推均不重做。

## 1. 已结束的第一轮实际说明了什么

第一版实际 run43745966802，
source d71d40bb6cbea1cecc9c23f2efd47401da35cc53，
core e0a5ad95b06bbd75319b1464f5c1b629d3f64d919758fbe7e0a76ad3c41963cb，
在71.023573757秒后以 exit2 返回。
它不是输入格式错误。原1380件输入及全部输出均已通过字节和 SHA 核验。

随后纯 IO run43747260495 读取原记录：
五个初始路径都在第一个坐标 $C_0$ 停止，accepted_prefix 为零；
五个28维格的全部140行只因 denominator_bound 被拒，
zero、nonunit、unchanged 的计数均为零。原整阶乘法界 $K$ 有59位十进制数字，
没有候选进入原129阶准确验证。
详见 [第一轮实际记录](R787-projective-first-ended-search.md)。

因此实际证据只说明这五次约化给出的行没有通过各自矩形的分母上界；
它没有穷尽任何矩形内的全部格点。
它既不说明430位精度不足，也不说明共同数域分母路线失败。
条件 $2KND_{\max}<M$ 保证固定矩形内分式唯一；
它不是原129阶准确出口的必要条件。
第一版未保存被拒约化行的原整数内容，不能假称它们现在可以读回。
本版采用真正不同的双探针格，并保存其全部约化行，不重复旧五个28维格。

## 2. 原归一向量与直接42维格

保持第一版的整阶与次序：
$$
\mathcal O=\mathbb Z[B_{\rm fld},s]\subset L,\qquad
s^2=-3,\qquad
\omega=(1,B_{\rm fld},\ldots,B_{\rm fld}^6,
s,sB_{\rm fld},\ldots,sB_{\rm fld}^6).
\tag{787P2.1}
$$
$f_B$ 是原首一七次整数多项式。这里仅用整阶的自由整数基，
不要求最大整环、主理想环或未知高度估计。

只消费原结束 producer 的
$$
M=1000000753^{430},\qquad
(\bar c,\bar a)\in
(\mathcal O/M\mathcal O)^{1214+1234}.
\tag{787P2.2}
$$
它们已使用同一真实1186 chart：
选定自由列 $f$ 的 $c_f=1$，其余27个自由列为零。
所有新格都直接使用这个原归一向量，不使用前一个格的分母倍数。

对两个固定坐标 $x_1,x_2$，仍以行向量定义
$\operatorname{coeff}(u x_i)=\operatorname{coeff}(u)R_{x_i}$。
本版使用行格
$$
\mathscr L_{x_1,x_2}
=
\{(d,n_1,n_2)\in\mathbb Z^{42}:
n_i\equiv dR_{x_i}\pmod M,\ i=1,2\},
\tag{787P2.3}
$$
其准确整数行基为
$$
\begin{pmatrix}
I_{14}&R_{x_1}&R_{x_2}\\
0&MI_{14}&0\\
0&0&MI_{14}
\end{pmatrix}.
\tag{787P2.4}
$$
乘法矩阵可取逐系数中心代表，这只改变后28行的整数倍，
不改变格。首实现三个块的权都为1。

LLL 后保存42行的全部42个整数、原输入指纹、两个原探针、
每行两个准确同余检查、平方长度次序及其候选对应。
不只保存“合格”行或拒绝计数。
非零分母的不同符号统一为首个非零系数正数；
这一步的行符号也保存。
只省略零分母与相同的实际整数分母，其他行均保留供准确出口。
在原14个分裂点是否为单位只作诊断，不是候选接受条件。

候选分母为
$$
D=\sum_i d_i\omega_i\in\mathcal O,\qquad D\ne0.
\tag{787P2.5}
$$
它不是先前分母与新因子的连乘，也不被中心约化后冒称相同元素。
不使用 $D_{\max}$、$N$、$K$、矩形唯一性或预期 bit 数作为硬筛选。
LLL 的近似长度、某行较短和两探针同余都不是成功证书。

## 3. 宽界候选与实际自由列

对每个候选 $D$，构造全部2448个候选 $L$ 系数：

- 非自由 $C_i$ 与全部 $A_i$：准确求 $D\bar c_i,D\bar a_i$，
  再逐个原14坐标取模 $M$ 的中心代表。
- 选定自由列：直接取 $C'_f=D$ 这个实际整阶元素。
- 其余27个自由列：直接取零。

因此即使 $D$ 的某个系数超过 $M/2$，仍保持
$$
C'_f=D\ne0,\qquad C'_j=0\quad(j\ne f\text{ 为自由列}).
\tag{787P2.6}
$$
自由列例外只是明确选择其整数 lift；它仍满足同一个模关系。
绝不把中心代表 $\operatorname{center}(D)$ 当作原 $D$。
其余坐标的中心选择可能并非真实 $Da_i,Dc_i$；本版不预先断言它们相等。

随后用原准确稀疏核
$$
B'=Z'C',\qquad
B'_P=Z_pC',\quad B'_Q=d_ZC',
\tag{787P2.7}
$$
其中原 $d_Z>0$。由 (787P2.6) 可知 $B'\ne0$。
对 $A',B'$ 共同除去整数内容 $e$，同时保存去内容前的 $D$
和去内容后的实际 $L$ 标度 $D/e$。
原 basis integer scale、basis order、字段和 producer 均不改变。

没有使用新素数筛选或浮点残差；每个候选直接进入下节原准确检验。
这样当前实现只有一种数学成功出口。

## 4. 唯一成功出口保持原129阶全部等式

逐阶准确检查
$$
246^3\kappa^{m+1}A'_{m-1}
+\sum_{j=0}^{m}R_{m-j}\kappa^jB'_j=0,
\qquad m=0,\ldots,128,
\tag{787P2.8}
$$
其中 $A'_{-1}=0$，每阶全部20个 $L$ 坐标、
280个有理坐标均必须为零。
原 R781 的 $R_0,\ldots,R_{128}$、
$\kappa^0,\ldots,\kappa^{129}$ 及逐 SHA 链原样消费。

某阶非零即记录这个原 Laurent 阶、完整准确非零残差和候选身份，
停止该候选的后续验算，转下一个已明确保存的候选。
**原 Laurent 残差不是某个 $A_i$ 或 $C_i$ 错误的定位。**
本版不把残差的 $(m,t,L)$ 坐标伪映射成下一探针下标。

若全部等式成立，原 R786 的全球注入首先给
$A'=yB'$。更具体地，原已成1186非零 minor 与特征零秩上界
使同一自由模式有唯一解；(787P2.6)–(787P2.8) 因而给
$$
(A',C')=D(A,C)
\tag{787P2.9}
$$
（共同整数内容除去前）。
成功系数相对原归一方向的倍数恰为 $D/e$。
因此它不仅给某个非零核向量，而且认证了同一原1186归一方向。
这一步不需要任何格长度唯一性估计。

成功 RESULT、FINAL 和 recipe 沿用原接口：
R787-original-power5-function-relation、
p41-original-power5-function-relation-certificate.json、
R787-original-function-recipe.json.gz。
真实新 core/source/configuration 与双探针方法 SHA 单独绑定；
不能冒用旧 R787 或第一版 projective 的 core SHA。

## 5. 固定探针对与有限执行控制

坐标按原 $C_0,\ldots,C_{1213},A_0,\ldots,A_{1233}$ 次序编号。
新核心固定以下探针对次序：

| 格编号 | 原两个探针 |
|---|---|
| 0 | $C_0,C_1$ |
| 1 | $C_0,C_2$ |
| 2 | $C_1,C_2$ |
| 3 | $C_0,A_0$ |
| 4 | $C_1,A_0$ |
| 5 | $A_0,A_1$ |

表中后继只是确定的有限候选搜索，不是错误坐标定位，也没有成功概率保证。
首实际请求只允许第0个格与至多42个不同非零候选。
如首批没有成功，真实记录会保全部42行、全部已经测试的结果和精确下一位置；
增加运行控制只继续既定后继，不重做已完成 LLL 或已拒候选。

数学 tag 固定整个探针对表、三个权、42维、直接原归一探针、
不使用高度硬筛和实际 $D$ 自由列规则。
maximal lattices、maximal tested candidates 和分钟数是停止位置，
不改变既有数学对象的身份；续算须先验证其余整个 tag 完全一致。
候选数上限与格数上限分别报告 search_node_budget_reached、search_lattice_budget_reached；
分钟预算另由 BudgetStop/time 标志报告，未执行表尾另列 remaining_schedule。
若本次只达到运行控制，不能写整个有限表已经耗尽。
即使六个格全部暂未给成功，也只报告这些明确候选未成功，不否定原关系存在。

## 6. 实际来源、有限存储和崩溃边界

CLI 保持前版字段名，核心与方法路径独立：

~~~sh
python scripts/R787_projective_two_probe_reconstruction.py \
  --config REQUEST \
  --method notes/R787-original-projective-two-probe-reconstruction-method.md \
  --field-core scripts/R781_original_Laurent_prefix.py \
  --retained INPUT_ROOT --output OUTPUT --budget-minutes 300
~~~

仍为原1380件真实闭包：
R787 的430位 lift、chart、selection、rational-blocks、
1234条原 real rows 和 metadata；
R781 的134件原闭包；R786 的4件 metadata/index。
原源 run43708449812、
source ac5998f333ab49c4747874e2e44b7ca4ccfa3acf、
原 configuration SHA
71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d。
原数学 method SHA 仍为
1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b。
旧430位过程实际 exit1/BudgetStop，而非成功函数 producer；
包装层保持这一区别。

所有新阶段仍使用 R787-projective- 前缀，但整个 tag 是本版真实身份。
第一版数学阶段不能直接改 tag 冒充本版完成产物。
本版不再计算第一版 $K$ 与五个矩形，不运行任何旧28维 LLL。
来源读取、逐 SHA 校验、格式组装不构成重新生成旧数学前缀。

每个新42维格整体原子保存后，current 只记录格编号和 next_candidate_position。
完整候选矩阵在准确验算前原子保存；
每阶展开及零等式也原子保存，预算或硬中断后直接回用。
成功 recipe 若已保存但队列尚未推进，续算优先接受这条已完整认证边界。

对已经准确拒绝的候选，先保存首个完整非零残差及终止结果，
再保存它的全部临时候选/展开文件名、字节数和 SHA 清单，
最后删除这些不再被续算读取的大工作矩阵。
每个删除动作都可由这个原子清单重复完成。
保留所有42个原 LLL 行、候选 $D$、准确拒绝和小 SHA 记录，
不把已拒候选再排队重算。
**当前未完成候选和成功候选的数据不执行这项清理。**
因此不积累42份百兆级候选工作副本，也不丢掉任何尚需消费的格行。

输出 manifest 只列实际仍存在的完整阶段；
closed-work receipt 另外明确哪些已完成失败的工作文件只保身份。
不能再笼统声称所有曾生成的数学文件原字节永远都在。
活跃产物和续算输入只在一日 Actions artifact 内传输，
不进入 Git 或 Release。

## 7. 本版完成后仍然没有自动解决的项目

只有成功 (787P2.8) 才能给后继 R792 读取原 $y$。
$\beta$ 的实际求值、原 A/B 的正常坐标、两图极理想、
$\eta$、Picard 比较函数、第二类 period 和原高度均由各自真实消费者处理。
本版没有修改原规范，也不把候选生成或一个失败记录当作这些项目的结果。

## 来源

- R781、R786、R787（2026）：原字段、尺度、归一 chart、129阶全局认证与已成输入；上文链接的原结果和方法仍是本版数学定义。
- R787 projective 第一版实际 run43745966802 与纯 IO run43747260495（2026），见上述固定 source 与实际记录。
- M. H. M. Jayantha Suranimalee，*Linear Algebra over Finitely Generated Fields and Rings*，
  Kaiserslautern 博士论文，2021，§§1.3.5–1.3.6，
  [作者原件](https://kluedo.ub.rptu.de/files/6560/dissertation_Suranimalee.pdf)：
  数域共同分母的整数格思路。本文直接证明双探针行格与原准确出口，
  不借用未核实的成功高度估计。
- python-flint 0.9.0 官方
  [fmpz_mat.lll 文档](https://python-flint.readthedocs.io/en/latest/fmpz_mat.html)：
  只作候选生成；必要同余与原最终等式均独立准确核验。
