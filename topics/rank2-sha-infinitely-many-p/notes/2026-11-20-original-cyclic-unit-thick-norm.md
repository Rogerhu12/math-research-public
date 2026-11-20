# 同原单位的完整循环商与厚除子范数捷径

日期：2026-11-20。状态：证明与独立 optional helper 已写；没有执行数学计算，
没有改变已运行的 R931 基础工具、上层 consumer 或 CI。

本注只给同一完整 Artin 商的范数算法。是否通过循环门，须在原公开输入上
实际计算；门不通过时原 R931 的所有基素多项式层算法完整保留。
完整 `307 × 306` HNF 及变换矩阵本身可能昂贵，本注不承诺实际时间或内存改善。

## 1. 固定输入和唯一接受门

取 R925 已认证的一个原仿射图表。仍写

\[
R=k[\xi],\qquad k=\mathbf F_{r^2},\qquad r\in\{29,41\},
\qquad A=\Gamma(Y\setminus P,\mathcal O_Y),\qquad
\operatorname{rank}_R A=n=306.
\tag{1}
\]

第二图表时只将原底参数换为原 \(s=1/\xi\)；所有论证逐字适用。
\(A\) 的有序整基、完整乘法、原 \(\omega\in k\)、真实单位
\(u\in R^{1\times n}\) 都是原 `OriginalArtinianNormTools` 对象中的对象。
尤其不把单位改成第一个标准行。

令 \(I\subset A\) 是原 consumer 所产生的一个完整非零理想，
\(H_I\in M_n(R)\) 是其首一上三角行 Hermite 基。置

\[
d=\det H_I\in R,\qquad d\text{ 首一},\qquad
N=\deg d=\dim_k(A/I).
\tag{2}
\]

重复因子保留在 \(d\) 中。这里既不假定 \(I\) 为根理想，也不假定
不同原地方在 \(\xi\) 下有不同像。

构造原完整行矩阵

\[
M=\begin{pmatrix}u\\ H_I\end{pmatrix}\in M_{n+1,n}(R).
\tag{3}
\]

唯一接受门是

\[
\boxed{\operatorname{row}_R(M)=R^{1\times n}.}
\tag{4}
\]

程序使用 `hermite_form(include_zero_rows=True, transformation=True)` 得
\(\mathcal H=UM\)，完整保留 \(307\) 个输出行和 \(307\times307\) 变换。
先核整个矩阵等式，再核全部 \(307\) 个原行对非零 Hermite 基的多项式余式均零。
前者给 \(\operatorname{row}(\mathcal H)\subseteq\operatorname{row}(M)\)，
后者给反向包含，因而单凭实际两个包含已经证明全行模相等。
这不依赖分式域秩或清分母，也无需另计算 \(\det U\) 才能获得完整性。

原 \(H_I\) 已有秩 \(n\)，故 \(\mathcal H\) 恰有一个零行，非零部分是
\(n\times n\) 的首一上三角 Hermite 基。门 (4) 当且仅当该部分为 \(I_n\)。
官方 Sage 文档说明了所用 Hermite 变换的接口和 \(UM=\mathcal H\) 契约；
上述全返回与两向包含是本程序另行执行的完整证据：
[Sage：一元多项式矩阵的 Hermite 形](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_polynomial_dense.html#sage.matrix.matrix_polynomial_dense.Matrix_polynomial_dense.hermite_form)。

若非零 Hermite 基不等于 \(I_n\)，它的首一行列式次数严格为正。
程序返回明确 `miss_original_unit_not_cyclic`，保留完整 HNF 回执，
交由原全部 \(\pi\)-层范数算法继续。此情况不是原数学输入失败。
实际身份、HNF 返回或单位值检查失败则仍是错误，不能吞为优化 miss。

## 2. 同一个完整厚商确为原 \(R/(d)\)

假设门 (4) 通过。由原单位定义得到原 \(R\)-代数同态

\[
\alpha:R\longrightarrow A/I,\qquad c\longmapsto cu\bmod I.
\tag{5}
\]

门 (4) 恰给 \(\alpha\) 满射。设其核为首一 \((g)\)。
由 \(H_I\) 的伴随矩阵，\(dA\subseteq I\)，尤其 \(du\in I\)，故 \(g\mid d\)。
另一方面 (2) 与满射给

\[
\deg g=\dim_k R/(g)=\dim_k A/I=N=\deg d.
\tag{6}
\]

两首一多项式相除且等次，故 \(g=d\)。因此

\[
\boxed{R/(d)\ \xrightarrow[\ c\mapsto c\cdot1\ ]{\ \sim\ } A/I}
\tag{7}
\]

是同原 \(k\)、同原底参数、同原单位定义的全非约化代数同构。
此处没有另选 primitive generator，没有将厚商换为其约化，也没有只匹配维数。

## 3. 由完整变换恢复全部原基的逆映射

取 \(U\) 的前 \(n\) 行和第一列，写

\[
\gamma_j=U_{j0},\qquad
V=U_{\{0,\ldots,n-1\},\{1,\ldots,n\}}.
\]

完整变换的前 \(n\) 行正是

\[
I_n=\gamma u+V H_I.
\tag{8}
\]

这里 \(\gamma\) 是列，\(u\) 是行。逐原基行 (8) 给
\(e_j\equiv\gamma_j u\pmod I\)。于是逆映射为

\[
\beta:A/I\longrightarrow R/(d),\qquad
h\longmapsto c=h\gamma\bmod d.
\tag{9}
\]

把每个 \(\gamma_j\) 降到模 \(d\) 的标准代表后，程序仍核：

1. 原全部 \(306\) 个基行 \(e_j-\gamma_j u\) 属于完整 \(I\)；
2. 原全部 \(306\) 个理想基行的标量像为零，即 \(H_I\gamma=0\pmod d\)；
3. \(u\gamma=1\pmod d\)，且 \((\omega u)\gamma=\omega\pmod d\)；
4. \(du\in I\)，且 \(\deg d\) 就是原完整 \(k\)-长度。

每次读取实际 \(h\) 时，再核

\[
\boxed{h-cu\in I,\qquad \beta(cu)=c\pmod d.}
\tag{10}
\]

因此 \(c\) 是同一原函数在同一厚商中的值。没有从某个约化剩余域多项式
反推原点，也没有使用不唯一的分式方程 \(D x=N\) 来代替 R931 的完整分式图。
原分式仍先经过原 `recover_fraction`，本捷径只消费已经恢复的真实整值。

公式 (5) 是代数同态，(7) 已证明双射，所以 (9) 自动保原完整乘法。
不需要重新验证原 \(46971\) 对全局基乘法，也不由任意线性同构猜乘法。

## 4. 完整范数是一次原常数域 resultant

对实际 \(h\in A\)，令 \(c=\beta(h)\)。由 (7)，乘 \(h\) 的完整
\(k\)-线性算子与原 \(R/(d)\) 上乘 \(c\) 共轭，故

\[
\boxed{N_{(A/I)/k}(h)=\det_k(m_h)
=\operatorname{Res}_{\xi}(d,c).}
\tag{11}
\]

为直接核厚度，可在 \(\bar k\) 中写
\(d=\prod_\alpha(\xi-\alpha)^{e_\alpha}\)。
各局部厚代数 \(\bar k[\varepsilon]/(\varepsilon^{e_\alpha})\) 上乘 \(c\)
为三角算子，对角全是 \(c(\alpha)\)，所以其行列式为
\(c(\alpha)^{e_\alpha}\)。全乘积正是首一 \(d\) 的 resultant。
证明允许所有 \(e_\alpha>1\)，没有扔掉长度；程序本身不做此分解。

实际单位值当且仅当 \(\gcd(c,d)=1\)。`try_norm_unit` 核该完整多项式 gcd，
核 resultant 非零并属于同一个原 \(k\) 对象。它不把结果取到素域。
同原 \(\omega\) 的嵌入已由 (9) 的全单位返回保留。

边界约定均保持原 R931：

- \(I=A\) 时 \(d=1,N=0\)，商为零代数，空除子范数为 \(1\)；
  此时不计算额外 \(307\times306\) HNF，回执明确标注。
- 若实际值为常数 \(a\in k^\times\)，范数严格为 \(a^N\)，程序另核此恒等式。
- hit 分支通过完整 gcd 检查真实值为单位；非空商的零值或非单位值会明确失败。
  gate miss 只认证非循环，不认证所给值为单位；正式范数须调用完整 fallback，
  后者的所有非单位错误均原样保留，不能把 miss 当成范数成功。
- \(d\) 有重复因子时仍使用完整 \(d\)，不是其 squarefree 部分。

## 5. 独立 helper 的范围与接入方式

文件 `original_ys_cyclic_unit_norm.py` 导出
`OriginalCyclicUnitNormShortcut(original_tools)`。三个接口为：

```python
shortcut = OriginalCyclicUnitNormShortcut(the_same_original_norm_tools)
context_or_none, gate_receipt = shortcut.prepare(the_same_complete_ideal)
norm_or_none, receipt = shortcut.try_norm_unit(the_same_complete_ideal, actual_value)
norm, receipt = shortcut.norm_unit_with_fallback(the_same_complete_ideal, actual_value)
```

最后一个接口只在明确 miss 时调用原对象的未修改 `norm_unit`，保留其全部
\(\pi\)-层回执。它不覆写任何方法，不改源对象，不改变 Miller、辅助点、
支集分离、四 pair、\(6M^{-1}\) 或原 \(18\times9\) 读取。

缓存只复用同一个实际理想对象，并比较不可变的原完整 HNF 快照；
同一个成功商内的多个真实单位值可以复用 (8)–(9)，无需反复做循环门 HNF。
所有输出只有源、完整返回与标量结果的回执/哈希，不保存系数或矩阵数据文件。

此同构理论上也允许将原商乘法、逆元及支集计算逐项运输到 \(R/(d)\)，
但这些不属于本 helper，也没有被偷偷接入当前已审上层。
目前只实现范数捷径，并保持明确的原完整回退。

全文核对：theta 推导并实现，root/global 全文核完整HNF返回、两向包含、原单位/omega、厚同构与resultant；root仅澄清try接口miss不认证单位的契约。只有AST和源码检查，无数学执行。保存源码 SHA256 `b3b2bfc21328e164de64845bc906efbaa01d143f6de7d80829c1bbbd4d775eb8`。
