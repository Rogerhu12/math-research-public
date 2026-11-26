# R974. 原指定残余域的绝对表示与全部厚范数的返回

**状态：已证明。** 这是原有限域表示层的修复，不是原 F 除子、四交、shadow
或无穷素数非零定理。实际 API 回执须另按 source/run/hash 登记。

日期：2026-11-27（UTC+8）；会话：Astra-rank2-Sha-0b097461-20261127。

## 1. 真实失败要求修复的对象

R956 v7 的 run `45838674625` 在原厚范数预门中失败；
准确记录见[原日志回执](../notes/2026-11-27-artinian-v7-final-and-successor.md)。
其原常数域是
$$k=\mathbf F_{29}[\omega]/(\omega^2+\omega+1).$$
`OriginalArtinianNormTools.norm_unit` 对每个真实不可约
$\pi\in k[\xi]$ 构造 $k_\pi=k[\xi]/(\pi)$，需要该域的全部坐标、
原 $k$ 嵌入和返回映射。Sage 10.6 的
`P.quotient(pi).field_extension(...)` 不保证给出原接口所需的
**绝对**有限域表示；非素底域上的多项式扩张可以仍为相对多项式商域。
其相对 `degree()` 不能用于绝对坐标或绝对 Frobenius 次数。

修正保持原 $P=k[\xi]$、$\pi$、$k$、原 $\omega$、全部理想与乘法算子；
只给同一个 $k_\pi$ 一个带有完整正反映射的计算表示。

## 2. 指定底域同构

**命题。** 设 $k$ 是有限域，$|k|=q=p^e$，
$\pi\in P=k[\xi]$ 为首一不可约多项式，$d=\deg\pi\ge1$。
记 $Q=P/(\pi)$，$\bar\xi$ 为 $\xi$ 的剩余类。
取一个大小 $q^d$ 的绝对有限域 $F$，以及显式单射
$\iota:k\hookrightarrow F$。
令 $\pi^\iota$ 为逐系数施加 $\iota$ 的多项式，取其任一根 $r\in F$。
则存在唯一与 $\iota$ 相容的域同构
$$
\Phi:Q\longrightarrow F,
\qquad \Phi\left(\sum_{j=0}^{d-1}a_j\bar\xi^j\right)
=\sum_{j=0}^{d-1}\iota(a_j)r^j. \tag{1}
$$
若 $(c_0(v),\ldots,c_{d-1}(v))$ 是 $v\in F$ 在基
$(1,r,\ldots,r^{d-1})$ 下相对 $\iota$ 的 $k$ 坐标，则
$$
\Psi(v)=\sum_{j=0}^{d-1}c_j(v)\bar\xi^j \tag{2}
$$
是 $\Phi$ 的逆。尤其对所有 $a\in k$、$f\in P$、$v\in F$，
$$
\Psi\Phi(\bar f)=\bar f,\qquad \Phi\Psi(v)=v,\qquad
\Psi(\iota(a))=\bar a. \tag{3}
$$

**证明。** 有限域 $Q$ 的元素数为 $q^d$。有限域的乘法群是阶 $q^d-1$
的群，故每个 $u\in Q$ 满足 $u^{q^d}=u$。特别是
$\pi\mid \xi^{q^d}-\xi$，而后者的导数为 $-1$，所以 $\pi$ 可分。
在包含 $\iota(k)$ 的大小 $q^d$ 的域 $F$ 中，$\pi^\iota$ 因而分裂成
$d$ 个互异一次因子。也可以由有限域唯一性，将 $Q$ 的某个同构与
$k$ 的 Frobenius 自同构复合，从而使其在 $k$ 上等于指定 $\iota$。

代入 $r$ 并逐系数施加 $\iota$ 给出环同态 $P\to F$，
它以 $\pi$ 为零。因此它下降为非零的域同态 $\Phi:Q\to F$，
必为单射；两边元素数相同，故为满射。不可约性同时说明
$1,r,\ldots,r^{d-1}$ 在 $\iota(k)$ 上线性无关，继而是基。
公式 (2) 所用的坐标唯一，直接得 (3)。它也说明 $\Psi$ 与加法和乘法
相容，因为它是环同构 $\Phi$ 的双侧逆。原 $\omega\in k$ 在返回时
仍精确等于其原剩余类 $\bar\omega$。证毕。

这里并未用一个不明根替换原商域。选择根只是表示 (1) 的一部分；
必须同时保留 (2) 才能返回原 $Q$。若选择另一个根 $r'$，新同构为
$\Phi'=\tau\Phi$，其中 $\tau$ 是固定 $\iota(k)$ 的 $F$ 自同构，
并有 $\Psi'=\Psi\tau^{-1}$。因此整个
$Q\xrightarrow{\Phi}F\xrightarrow{\Psi}Q$ 不依赖这项表示选择。

## 3. 全矩阵、原范数与 Frobenius

对任意矩阵 $M$，逐项施加域同构给
$$
\Phi(MN)=\Phi(M)\Phi(N),\qquad
\Phi(\det M)=\det\Phi(M). \tag{4}
$$
行关系、行空间、核、秩、商空间上的诱导算子均按这个同构返回。
这不是只比较矩阵的一个主元或一个行列式：每个原坐标都由 (3)
回到原商域，(4) 对全部行和列成立。

取 $h\in P$，在 $Q$ 中非零。其原相对范数为
$$
N_{Q/k}(\bar h)=\operatorname{Res}_\xi(\pi,h)\in k, \tag{5}
$$
其中 $\pi$ 首一。证明可将 $\pi$ 在代数闭包中分解为互异根，
乘法算子在这些根上的本征值正是 $h$ 的取值；其乘积同时是相对范数
和上述结式。式 (1) 给出
$$
\iota\!\left(N_{Q/k}(\bar h)\right)
=\Phi(\bar h)^{(q^d-1)/(q-1)}. \tag{6}
$$
因此从 $F$ 算出的结果经 $\Psi$ 返回时，是原 $k$ 中的常数，
不是把结果再取到 $\mathbf F_p$ 的绝对范数。
特别地，原范数不在 $\mathbf F_p$ 时，这项性质完全保持。

同态保持整数幂，故对每个 $u$ 都有
$\Phi(u^p)=\Phi(u)^p$。绝对 Frobenius 的正确次数由
$|F|=p^{ed}$ 决定。计算表示必须验证
`field.cardinality() == characteristic**field.degree()`，
从而其坐标数确为 $ed$；不能删除这个门而接受相对次数 $d$。

## 4. 原全部厚层未被约化

R931 的厚范数算法对原有限 $k$ 代数 $A/I$，逐个基素因子 $\pi$
使用全部层
$$
H_j/H_{j+1},\qquad H_j=I+\pi^jA.
$$
这些层是原 $Q=k[\xi]/(\pi)$ 上的向量空间。
程序先用完整多项式理想包含矩阵取得其全部关系、代表和诱导算子，
再在该层的残余域中求行列式。

第 2 节只改变此处 $Q$ 的表示。由 (4)，每层的全部关系空间和算子
按同构返回；由 (5)–(6)，每层行列式的相对范数回到原 $k$。
所有层的乘积便仍为 $\det_k(m_h\mid A/I)$。原程序对
每层维数、全部累计长度、$H_j=H_{j+1}$ 的终止和理想行列式的检查
不变。因此厚度、非约化部分和原常数域均未被替换。

这也适用于嵌套残余域：先用 $\Phi_1,\Psi_1$ 表示 $k_\pi$，
第二层在其原实际系数域上使用 $\Phi_2,\Psi_2$，
则完整返回使用 $\Psi_1\Psi_2$。式 (3) 逐层保持原 $\omega$；
不能只比较两层的域基数后任意认同它们。

## 5. 生产实现与针对本次故障的实际门

`scripts/original_ys_closed_point_tools.py` 中
`ActualFiniteFieldQuotient` 保持 $d=1$ 时原底域对象不变；
$d>1$ 时执行：

1. 用 `base.extension(d, map=True)` 的整数次数接口获得绝对域及
   原 `base` 的显式嵌入；逐系数送入原 $\pi$。
2. 验证全部 $d$ 个根，按绝对坐标排序后固定其中一个 $r$。
3. 用 `vector_space(base=embedding, basis=[1,r,...,r**(d-1)])`
   取得该指定幂基的双向线性映射，构造 (1)–(2)。
4. 检查整个相对幂基、整个绝对幂基、原底域幂基的双向返回，
   继续原 $\pi$ 归零、根返回、原底生成元和域基数全部检查。

Sage 10.6 官方源码对整数次数扩张与多项式扩张的区别、
以及指定底嵌入和幂基的向量空间映射均有明确实现：

- [`finite_field_base.pyx`, `extension` 与 `free_module`](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/finite_rings/finite_field_base.pyx)。
- [`polynomial_quotient_ring.py`, `field_extension`](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/polynomial_quotient_ring.py)。

小入口 `scripts/check-original-finite-field-quotient-api.py` 使用原
$\mathbf F_{29^2}$ 模 $[1,1,1]$，先重现旧返回的相对次数问题；
再验证一次、素底二次、原底二次/三次及二次残余域之上再作二次扩张。
它检查全部幂基乘法、原标量作用、完整绝对坐标、实际矩阵行列式、
原相对结式范数，并沿两层返回原 $\omega$。

另取原厚预检的 $\pi=\xi^2-c$，其中 $c$ 是原 $k$ 的乘法生成元。
根的原范数为 $-c$。平方厚度和 306 个自由模拷贝给
$$N=(-c)^{2\cdot306}=(-c)^{612}\notin\mathbf F_{29}.$$
小入口只核这个真实标量公式和完整表示返回，
不会把它称为原 306 维几何或双图预检已通过。

未执行的完整大链继续保留两原特征零 PASS、原参数、全部 306 行、
两图、四交、所有厚范数和双轴 shadow 的原检查。

## 6. 将人工 1530 长度 API 预检移出生产的默认路径

根 README 第 12 条要求不为防错重复设置流程。这里必须区分
原数学对象的计算与人工 API 预检。
`produce-original-artinian-shadow.py:original_thick_norm_preflight`
构造的是任意原底域乘法生成元 $c$ 所给的
$$
I=(\xi^2-c)^2(\xi-1)A,\qquad h=\xi.
$$
它的作用是用可预先证明的范数 $(-c)^{612}$ 检验 split、inverse、
common-zero graph 和 norm 接口。这些理想不是原 $F$ 或 $P$ 的
零极理想，也不是四个原交除子。

逐项读原 `main()` 的数据流可知，此函数的返回只被 `emit` 和最终
`same_original_two_chart_artinian_preflight_sha256` 使用。
实际 `geometry` 的输入仍是 `six`；`intersections` 的输入是该
`geometry` 和 `six`；`shadow` 的输入是这些实际交理想。
这三步没有消费人工预检的局部 engine、理想、矩阵、范数或回执。
底层运算适配器的缓存和操作计数不属于数学输入。

因此可把该人工预检改为显式的 `--run-api-preflight` 可选检查，
默认直接处理原几何对象。未执行时，回执须准确写
`auxiliary_api_preflight_executed=False`，该预检摘要为 `None`；
不再输出预检 PASS，不把它混作已执行的原数学门。
原函数仍保留，手动要求时执行完全相同的两图预检。

这项调整不删实际原数据的校验：两个原特征零来源认证、完整 maps、
原 $F/P$ 图核和全部整回乘、两图粘合的理想等式、四交全部六类长度、
每个实际厚层的完整算子/曲线方程/相对范数，以及九对和双轴 shadow
仍分别按其真实对象执行。第 2–4 节证明的是表示与这些数学操作相容，
人工预检的存在与否不充当任何未证数学前提。
