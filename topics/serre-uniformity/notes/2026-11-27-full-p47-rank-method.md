# full p47：全平方水平 Heegner 商的严格导数请求

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

## 任务与不重复的范围

R1074 已把原完整 $X_{\rm ns}^+(47)(\mathbf Q)$ 限制到八个真实 CM 盘，
但尚未证明盘内唯一。R45 §1 的无条件秩输入只适用于
$A=\prod_{L'(f,1)\ne0}A_f$；没有证明此处 $A=J$。
R707 的主水平为 41，不能把它的辅助素数 47 当成本题主水平。
本请求新计算完整水平 $47^2=2209$ 的新 Fricke 正号部分，
不重算 R1072、R1074 或旧标量窗口。

当前只是计算方法与请求；运行成功前不把任何预期维数、导数或秩写作已证。

## 精确来源和完备覆盖

使用 SageMath 10.6 的有理 modular symbols：
$\operatorname{ModularSymbols}(2209,2,\mathrm{sign}=1)$。
这里 sign 是 star involution；它本身不是 Fricke 正号。
先取 cusp、新子空间，再单独计算 $W_{2209}$，
核 $W^2=1$，以 $(d+\operatorname{Tr}W)/2$ 得正号维数。

对全新空间作 proof=True 的精确 Hecke 分解。
每个简单因子上实际 Fricke 矩阵必须为 $+I$ 或 $-I$；
全部因子的维数和必须等于新空间维数，
正号因子的维数和必须等于上面的实际正号维数。
每个正号因子用 q_eigenform 取得 $q^{257}$ 以前的精确系数。
核 coefficient field degree 等于该 star-positive 简单因子维数，
$a_0=0,a_1=1,a_{47}=0$，并枚举 coefficient field 到 AA 的全部实嵌入。

这避免把 sign=1、全 cusp space、旧形式或某一个 Galois 嵌入误当成完整所需空间。
Chen–de Smit–Edixhoven 同源及 R45 §1 给
$J_{\rm ns}^+(47)\sim_{\mathbf Q}J_0^+(2209)^{\rm new}$。

## 导数的严格有限区间

对每个标准化新形式与每个实嵌入，令 $c=2\pi/47$。
Fricke 正号在权二给函数方程符号 $-1$，
Dogra–Le Fourn (2021), Lemma 15 给准确公式
$$
L'(f,1)=2\sum_{n\ge1}\frac{a_n(f)}n E_1(cn),
\qquad E_1(x)=\int_x^\infty e^{-t}\frac{dt}{t}.
$$
归一化也可由完成函数的 Mellin 积分直接核实：
函数方程符号使 $L(f,1)=0$，故完成因子的导数不另加常数项。

Deligne 界在每个嵌入成立：
$|a_n|\le d(n)\sqrt n\le2n$。
平方水平平凡特征新形式有 $a_{47}=0$，坏素数项不破坏该界。
又 $E_1(x)\le e^{-x}/x$，故对任意 $M\ge1$，
$$
\left|2\sum_{n>M}\frac{a_n}n E_1(cn)\right|
\le \frac{4e^{-c(M+1)}}{c(M+1)(1-e^{-c})}.
$$
本次固定 $M=256$、512 bit ball 精度。全部前缀和、$\pi$、
指数函数及 $E_1$ 都在 Arb/acb 的认证球中求值；
$E_1$ 用 ComplexBall.exp_integral_e(1)，取包含真实值的实部，
不能换成 symbolic/multiprecision 的普通浮点函数。
代数嵌入先由 AA 精确隔离，再通过有向舍入实区间转换成球；
在 coefficient field 的原多项式基上 Horner 评价。
RealBall.add_error 用尾界的上界增大半径。

只有最终扩大后的区间严格大于或小于零，才记录该嵌入的非消失。
若全部正号因子的全部嵌入成功，才可结合 R45 §1
及其引用的 Gross–Zagier/Kolyvagin 型定理推出整个 $J$ 的 rank=dim。
区间含零只表示该精度未认证，绝不表示导数为零。

## 执行、预算与留存

只在本公开仓库 GitHub Actions 执行；使用官方
sagemath/sagemath 10.6 amd64 image 的 manifest digest
sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879。
这是实际已公布的 10.6 image；运行时再核 SAGE_VERSION=10.6。
数学总预算 600 秒，预留 30 秒；安装/拉 image 的 workflow 外限 25 分钟。
内部 570 秒 alarm，外层 timeout 600 秒并保留终止宽限，
失败只给已完成因子的回执。

数学导入前核 Actions、仓库、实际 checkout/GITHUB_SHA、
请求和全部输入文件 SHA-256。
只输出空间维数、因子分解、每嵌入导数包围球及摘要哈希。
完整 modular-symbol 矩阵、q 系数数组不上传 artifact、不进 Release、不提交。
它们可由本脚本和请求重算。

即使全部导数非零，此计算也不提供 MW 格的饱和、283-adic 对数行列式、
完整高度矩阵、QC 全尾或盘内唯一性，更不完成全素数 Serre 一致性。

## 原始文献与软件接口

- N. Dogra, S. Le Fourn, *Quadratic Chabauty for modular curves and modular forms of rank one*,
  Math. Ann. 380 (2021), 393–448，Definition 4、Proposition 3、Lemma 15；
  [期刊](https://doi.org/10.1007/s00208-020-02112-3)。准确适用范围见 R45 §1、§6。
- B. de Smit, B. Edixhoven, *Sur un résultat d'Imin Chen*, Math. Res. Lett. 7 (2000), 147–153，
  Theorems 1–2；[作者全文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。
- P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHES 43 (1974), Théorème 8.2；
  [原刊](https://www.numdam.org/articles/10.1007/BF02684373/)。
- Sage 官方 [modular symbols](https://doc.sagemath.org/html/en/reference/modsym/sage/modular/modsym/space.html)
  的 q_eigenform、new_subspace；
  [Hecke module](https://doc.sagemath.org/html/en/reference/hecke/sage/modular/hecke/module.html)
  的 decomposition、atkin_lehner_operator；
  [real Arb](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/real_arb.html) 的 add_error；
  [complex Arb](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/complex_arb.html) 的 exp_integral_e。
