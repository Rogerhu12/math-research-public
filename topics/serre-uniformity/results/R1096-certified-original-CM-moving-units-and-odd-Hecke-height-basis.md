# R1096 — 原 full47 的 CM 移动单位、奇 Hecke 整基与完整高度来源

**状态：已证明，含公开 Actions 精确计算。** 本条消费已认证的原
73维 Hodge/Hecke 矩阵和 Gaussian CM 对数，不重做其计算。
新读数证明 $T_2-1$、$T_3$ 在全部原整格上可逆，且
$T_3+T_5$ 生成完整整 Hecke 代数。由此整个 MW 高度可用
在4513处约化支撑分离的真实 CM 除子对读取。
实际全局交数及高度单位尚未计算。

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

## 1. 原对象和已经完成的输入

全篇固定
$$
X=X_{\rm ns}^+(47),\quad J=\operatorname{Jac}(X),\quad q=4513,
\quad \mathcal T=\mathcal T_q,\quad
M=(J(\mathbf Q)/J(\mathbf Q)_{\rm tors})\otimes\mathbf Z_q.
$$
$\mathcal T$ 是 [R1081](R1081-certified-original-level47-Cartan-trace-and-integral-Hecke-algebra.md)
在原曲线上得到的秩73最大未分歧整 Hecke 代数。
原 Hodge 与 Lie 格在每个 DVR 因子上自由秩一。
[R1090](R1090-original-weight-one-integral-Hodge-source.md) 的实际73维 Hodge
基及 [R1093](R1093-certified-original-Gaussian-CM-generator-and-full-MW-lattice.md)
的 $M_2,M_3,M_5$ 矩阵是下面唯一矩阵输入。

令 $y_4,y_{16}$ 为原规范 CM 点，分别有 $j=1728,287496$，并记
$$
u_4=23[y_4]-C_\infty,\qquad
u_{16}=23[y_{16}]-C_\infty,\qquad
B_q=(q+1)-T_q.
\tag{1096.1}
$$
这里 $C_\infty$ 是全部23个尖点。
[R1089](R1089-certified-full-level47-auxiliary-Bq-and-component-groups.md)
已经证明 $B_q\in\mathcal T^\times$；
R1093 已证明
$$
M=\mathcal T u_4=\mathcal T B_qu_4,\qquad
\log M=q\,\operatorname{Lie}(J)(\mathbf Z_q).
\tag{1096.2}
$$
这些旧结论不在本次请求中重新搜索或证明。

[2026-11-12原笔记§3.1](../notes/2026-11-12-qc-local-types-resume2.md)
已经按全部三个循环二子群及粗模重数证明
$$
T_2[y_4]=[y_4]+2[y_{16}],\qquad
T_2C_\infty=3C_\infty,\qquad
(T_2-1)u_4=2u_{16}.
\tag{1096.3}
$$
本条直接使用这个实际除子关系；没有遗失尖点平移或未知挠类。

## 2. 新的完整73维单位读数

在同一原基上，本次精确计算得到
$$
\boxed{\det(M_2-I)=3715,\qquad \det M_3=3071
\quad\text{in }\mathbf F_{4513}.}
\tag{1096.4}
$$
两者均非零。程序还计算并核对逆矩阵；这些矩阵的hash列于§7。
因为原 Hodge 格在 $\mathcal T$ 每个因子上自由秩一，
(1096.4) 严格给
$$
T_2-1\in\mathcal T^\times,\qquad T_3\in\mathcal T^\times.
$$
这不是只检查16个一次块。

由 (1096.2)–(1096.3)，且2在 $\mathbf Z_q$ 中可逆，
$$
\boxed{
M=\mathcal T u_{16}
 =\mathcal T B_qu_{16}
 =\mathcal T T_3u_4.}
\tag{1096.5}
$$
因此 conductor2 的原 CM 点也生成完整73维 MW 整格。

## 3. 只用奇指标的完整整 Hecke 基

请求按 $t=0,\ldots,63$ 的有限次序检查
$H_{{\rm odd},t}=T_3+tT_5$ 的特征多项式，首个成功后停止。
$t=0$ 的特征多项式与导数的最大公因子次数20。
$t=1$ 得到
$$
H_{\rm odd}=T_3+T_5,\qquad
\deg\chi_{\rm odd}=73,\qquad
\gcd(\chi_{\rm odd},\chi_{\rm odd}')=1,\qquad
\operatorname{disc}(\chi_{\rm odd})=2650\pmod q.
\tag{1096.6}
$$
准确剩余因子次数为
$$
1^{16},\quad 2^6,\quad 3^4,\quad 11,\quad 22.
$$

平方自由的73次特征多项式意味着最小多项式也为73次，
故 $\mathbf F_q[H_{\rm odd}]$ 在原 Hodge 上维数73。
它包含在既有的73维 $\mathcal T/q\mathcal T$ 中，所以两者相等。
对有限 $\mathbf Z_q$ 模 $\mathcal T/\mathbf Z_q[H_{\rm odd}]$
应用 Nakayama；或使用判别式单位给出的最大未分歧整序，均得到
$$
\boxed{
\mathbf Z_q[H_{\rm odd}]
=\mathbf Z_q[T_3,T_5]
=\mathcal T.}
\tag{1096.7}
$$
特别
$$
1,H_{\rm odd},\ldots,H_{\rm odd}^{72}
\tag{1096.8}
$$
是 $\mathcal T$ 的实际整基。

每个 (1096.8) 都是奇指标 Hecke 算子的整数线性组合。
这是因为 $3,5$ 为奇数，Hecke 乘法
$T_mT_n=\sum_{d\mid(m,n)}d\,T_{mn/d^2}$
保持奇指标；常数算子 $T_1$ 也在其中。
后继可以使用这些实际有限对应，而无需另设 away2 生成假设。

## 4. 原 CM 除子的全部奇 Hecke 移动均在4513处分盘

$y_4,y_{16}$ 在$q$处均为ordinary。
原 CM 端态约化嵌入几何端环，故
$$
\operatorname{End}(\overline E_4)=\mathbf Z[i].
$$
对 $\overline E_{16}$，几何端环包含 $\mathbf Z[2i]$，
其唯一更大整序为 $\mathbf Z[i]$。
若取后一整序，额外自同构迫 $j=1728$。但
$$
287496-1728=2^3\,3^6\,7^2
$$
是$q$单位，所以
$$
\operatorname{End}(\overline E_{16})=\mathbf Z[2i].
\tag{1096.9}
$$
ordinary 保证端态代数仍是 $\mathbf Q(i)$，没有超奇异端态增大问题。

奇度同源在 $2$-adic Tate 模上为同构，因而保持几何端环在2处的
局部整序。两条 (1096.9) 的局部整序不同。
所以任意奇指标 Hecke 目标的 $\overline E_{16}$ 都不可能同构于
$\overline E_4$。这已在底层椭圆曲线上排除相交，故也排除了
原47标记粗曲线上的相交。

现在取实际有限除子
$$
D_4=B_qu_4,\qquad D_{16}=B_qu_{16}.
$$
[R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)
证明了准确的消尖点式及逐几何约化盘零次数：
$$
D_i=23\{(q+1)[y_i]-T_q[y_i]\},\qquad
\operatorname{sp}(D_i)=0.
\tag{1096.10}
$$
式中保留全部$q+1$个 Hecke 目标和全部粗模重数。
对 $\mathbf F_q$-有理的 $y_i$，全部这些目标均约化到同一个原点。
特别，$D_i$ 没有尖点支撑。

若 $P\in\mathbf Z[X]$，则 $P(H_{\rm odd})D_{16}$
仍逐盘零次数；其支撑来自 conductor2 CM点的奇度同源目标。
由 (1096.9)–(1096.10)，
$$
\overline{\operatorname{supp}(D_4)}
\ \cap\
\overline{\operatorname{supp}(P(H_{\rm odd})D_{16})}
=\varnothing.
\tag{1096.11}
$$
负系数只改变重数，不改变这个支撑断言。

此外，$\mathbf Z[i]$ 没有范数3端态，所以 $D_4$ 与 $T_3D_4$
的约化支撑也分离。$T_3$ 的单位性提供一个单独的移动例子；
对完整代数族使用 (1096.11)，无需假设任意后续 Hecke 都保持这个
单独的 $T_3$ 分离。

## 5. 完整高度泛函的真实交数来源

固定 R1094 已构造的整、$\mathcal T$-相容各向同性 Hodge 补空间 $W$。
R1094 的整双极核及 ramified power-sum 引理适用于
(1096.10)–(1096.11)，因此
$$
\boxed{
h_q^W(D_4,P(H_{\rm odd})D_{16})\in q^2\mathbf Z_q
\qquad(P\in\mathbf Z[X]).}
\tag{1096.12}
$$
证明使用整个 Galois 不变循环的幂和；不要求每一个
$\mu_q$ 目标的参数都属于 $q\mathbf Z_q$，也不通过除以分歧次数取平均。

对$\ell\ne q$，记
$I_\ell(D_4,P(H_{\rm odd})D_{16})$ 为同一原曲线正则模型的
Néron交数，包含必要垂直修正。好素处它为整数；
坏47处可能分母由原分量群指数46控制，因此所有这些数仍为
$q$-整数。使用 R43/R1094 的
$\chi_\ell(\ell)=-\log_q\ell$ 规范及
$$
\frac{-\log_q\ell}{q}\equiv
\frac{\ell^{q-1}-1}{q}\pmod q,
$$
得到
$$
\boxed{
\begin{aligned}
q^{-1}h^W(D_4,P(H_{\rm odd})D_{16})
\equiv{}&
\sum_{\ell\ne q}
 I_\ell(D_4,P(H_{\rm odd})D_{16})\\
&\hspace{6mm}\cdot\frac{\ell^{q-1}-1}{q}\pmod q.
\end{aligned}}
\tag{1096.13}
$$
这个和只含有限个非零交数。$2,3,47$ 不得删去；
47的垂直项也不得用 R1074 的特定同盘 raw 配对零取代。

(1096.13) 先对有限真实对应成立。现在利用整基 (1096.8)
以及全球高度的双线性连续延拓，定义
$$
\Gamma(T)=q^{-1}h^W(D_4,TD_{16})\in\mathbf Z_q
\qquad(T\in\mathcal T).
\tag{1096.14}
$$
这里并未把某个局部高度单独定义在任意 Jacobian 类上。
先以73个真实除子对证明整性，再延拓的是全球高度。

置 $a=(T_2-1)/2\in\mathcal T^\times$，则
$D_{16}=aD_4$。Hecke 自伴性及 $W$ 的相容性给
$$
q^{-1}h^W(SD_4,TD_4)=\Gamma(a^{-1}ST)
\qquad(S,T\in\mathcal T).
\tag{1096.15}
$$
而 $M=\mathcal T D_4$，所以 (1096.14) 的73个整基值确实确定
整个原 MW 高度的第一层。由于 $\mathcal T$ 未分歧，
其迹配对完美，可唯一写
$$
\Gamma(T)=\operatorname{Tr}_{\mathcal T/\mathbf Z_q}(\kappa T),
\qquad \kappa\in\mathcal T.
\tag{1096.16}
$$
首层高度矩阵为单位，准确等价于 $\kappa\in\mathcal T^\times$。
本条没有算出 $\kappa$ 或其中任何一个指定块值，
不以整 MW 生成或支撑分离替代这个未付输入。

## 6. 原16个一次块上的新 CM16 对数

用 R1093 的
$H_2=T_2+2T_3+4T_5$ 一次根标记，且原73维 Hodge 坐标中
每个 eigenform 的第一个非零坐标为1。
程序逐项核对原 eigenform hash，读取 $a_2,a_3$ 后计算
$$
\lambda_{16}(f)
=\frac{a_2(f)-1}{2}\lambda_4(f),\qquad
\lambda_i(f)=q^{-1}\log(B_qu_i)(\omega_f)\pmod q.
\tag{1096.17}
$$
原 $B_q$ 保留在所有这些值中。

| $H_2$ 根 | $a_2$ | $a_3$ | $\lambda_{16}$ |
|---:|---:|---:|---:|
|434|3512|2686|2069|
|1054|3077|1544|2854|
|1615|3672|2662|1468|
|2250|3077|1544|339|
|2425|924|4307|4284|
|2472|1279|2018|4084|
|2604|911|4463|4344|
|2838|3672|2662|1237|
|3030|2552|428|1046|
|3112|924|4307|3888|
|3531|911|4463|3295|
|3560|2959|3705|2368|
|3639|2959|3705|843|
|3645|1279|2018|4240|
|3786|2552|428|2071|
|3795|3512|2686|2999|

这些是有限新推导值；完整高次数块的单位结论使用§2的73维行列式，
并非由此表外推。

## 7. 唯一新执行与可重现信息

- 方法：[full-p47-CM-height-move-method](../notes/2026-11-27-full-p47-CM-height-move-method.md)。
- 参数：[full-p47-CM-height-move-request.json](../notes/full-p47-CM-height-move-request.json)。
- 消费者：[full_p47_CM_height_move.py](../scripts/full_p47_CM_height_move.py)。
- workflow：仓库根 `.github/workflows/serre-full-p47-CM-height-move.yml`。
- 源提交：`b548e13e40cd703836c929586e480c97c2a51c3b`。
- 公开 [run45948995182](https://github.com/Rogerhu12/math-research-public/actions/runs/45948995182)，
  job140340211167，成功；实际数学窗口 $6.975637309$ 秒，
  预算120秒、reserve10秒。
- 固定 SageMath10.6 官方镜像
  `sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879`。
- 原95个 descriptor、五个 Hodge hash 和四个原 Hecke矩阵hash均按请求消费。
  没有重新搜索原基、重新算CM级数、$L'$、秩或全标签。
- 只保存脚本、参数、run、上述小结论和hash；不保存矩阵/长级数/artifact/Release。

| 对象 | SHA-256 |
|---|---|
|消费者|77db14996f8976f534ce6f5d07dcf7e2e26acecc65d13bfb8834d3ef8f22ecb0|
|方法|db12d56c67d007b6da6f73a778296acfb3a5d08598b7de7184b72f991dcd37b4|
|请求|bc89913668d6b3d209719a720c7562a7914459441526b6a565fc69edbfc2b7e6|
|完整新小结论|fba3bc1da08a11a26d3dc9055f2bcba135db379d15b07bcbc170391e8437db56|
|$(M_2-I)^{-1}$|386f69f78ebd7c9352b4e7a3fccda0f3c8c0e06e70a3ff3deb0379b57c821293|
|$M_3^{-1}$|e1c66ab3a762facc43050ab435ce1f20994c207391b9eda4b2a209e06145359d|
|$H_{\rm odd}$ 矩阵|e0105e4915c8685dcac366c72bdad0d0c7ff2e5b0b72768d06fd5573fc31cfbf|
|$\chi_{\rm odd}$|990a3205813f9785f40b97a754092530d9797edaee616b2814f2382530d06b37|

本条完成原高度的移动整基和真实非$q$来源，未计算原47标记交数，
未证明八个CM圆盘内部唯一，也未完成任意充分大$p$的主目标。


## 8. 原整基可选在 $n\le2255$ 的奇指标内

本节是纸面后继，不增加数学执行。令
$$
\mathcal I=
 \{n:1\le n\le2255,\ n\ \text{为奇数},\ 47\nmid n\}.
$$
则对本条的原整 Hecke 代数有
$$
\boxed{\quad
 \mathcal T=\sum_{n\in\mathcal I}\mathbf Z_qT_n .
 \quad}
\tag{1096.18}
$$
因此存在73个互异的 $n_1,\ldots,n_{73}\in\mathcal I$，
使 $T_{n_1},\ldots,T_{n_{73}}$ 成为 $\mathcal T$ 的整基。
此处证明存在性及明确上界，没有报出尚未计算的73个指标。
特别 $2255<q$，所选指标同时与 $2\cdot47\cdot q$ 互素。

### 8.1. 以原 normalized newforms 读取整谱坐标

令 $N=47^2$。使用
[R1080](R1080-certified-full-level47-Jacobian-rank.md)
已经识别的
$S_2(\Gamma_0(N))^{\mathrm{new},\,w_N=+1}$；
其73个复嵌入对应原 $J$ 的73个 Hecke 特征。
这里仅使用原 Chen 同源的特征零 Hecke 对应，
不把它宣称为两条曲线在$q$处的整 Hodge 格同构。

取有限未分歧扩张 $O/\mathbf Z_q$ 分裂 $\mathcal T$，
剩余域为 $k$。对应的73个 normalized newforms 记为
$f_\sigma=\sum_{r\ge1}a_r(f_\sigma)Q^r$，其中 $Q$ 是 Fourier 变量，
与固定素数$q$区别开。其 Hecke 系数为代数整数，故在$O$中；
$a_1(f_\sigma)=1$。相应 Hecke 特征在
$\mathcal T\otimes O\simeq O^{73}$ 上就是73个坐标投影。

由 (1096.6)，$H_{\rm odd}$ 的73个剩余特征值两两不同。
因此每个 $\overline f_\sigma$ 非零，且这73个约化线性无关：
对一个关系逐个作用 $H_{\rm odd}$ 的 Lagrange 插值投影即可；
分母为互异特征值之差，均为单位。
这一步在原 congruence modular forms 的整 Fourier 格中进行。

于是对任意
$$
\ell:\mathcal T/q\mathcal T\longrightarrow\mathbf F_q
$$
扩张到$k$后，都可取 $c_\sigma\in k$，使
$$
f=\sum_\sigma c_\sigma\overline f_\sigma,\qquad
a_r(f)=\ell(T_r)\quad(r\ge1).
\tag{1096.19}
$$
此处对 $47\mid r$ 的 $T_r$，暂指该 congruence newspace 上的算子。
如§8.3所示，它们恒为零；最终基只使用原 full47 的
prime-to47对应。将$c_\sigma$提升到$O$便给可用于
Sturm 同余定理的整 modular form，故没有从一个任意有理基
未经饱和就模$q$约化的步骤。

### 8.2. 精确的 odd-part 退化算子与 Sturm 界

对 Fourier 级数定义
$V_d f(Q)=f(Q^d)$，这里没有附加权二的标量。
由于 $2\nmid N$，权二的准确 Hecke 公式是
$$
a_r(T_2f)=a_{2r}(f)+2a_{r/2}(f),
$$
其中非整数下标的系数约定为零。故
$$
g=f-V_2T_2f+2V_4f
 \ \in\ S_2(\Gamma_0(4N);k)
\tag{1096.20}
$$
满足
$$
a_r(g)=
 \begin{cases}
 a_r(f),&r\ \text{为奇数},\\
 0,&r\ \text{为偶数}.
 \end{cases}
\tag{1096.21}
$$
例如 $r=2s$ 时，后两项的系数是
$-a_{2s}(f)-2a_{s/2}(f)+2a_{s/2}(f)$，
所以所有偶系数准确相消。式 (1096.20) 由整退化映射定义，
并可先在$O$上作出；$q\nmid4N$。

本节只用通常的 Sturm 上界，不需要更锐的 cusp-form 版本。
准确的群指数及权二界为
$$
[\mathrm{SL}_2(\mathbf Z):\Gamma_0(4\cdot47^2)]
 =4\cdot47^2\left(1+\frac12\right)
                 \left(1+\frac1{47}\right)
 =13536,
\qquad
\frac{2\cdot13536}{12}=2256 .
\tag{1096.22}
$$
因此若 $a_r(f)=0$ 对所有奇数 $r\le2255$ 成立，
则 (1096.21) 使 $g$ 的全部 $1\le r\le2256$ 系数为零；
最后的2256是偶数，也已经消失。
Sturm 定理给 $g=0$，从而 $f$ 的**全部奇系数**为零。

所用同余定理的明确形式及证明可见
[Stein 作者书稿，Theorem 9.18](https://wstein.org/books/modform/modform/newforms.html#sturm-s-theorem)；
原定理为 J. Sturm, “On the congruence of modular forms,”
*Number Theory*, LNM 1240 (1987), pp. 275–280。
也可参照
[Agashe–Stein 作者稿§2，Theorem 2.1](https://wstein.org/papers/generating_hecke/generating_hecke/node3.html)。
这里对层级 $4N$ 的整形式使用该定理，不把原 Cartan 曲线
一个尖点的有限 jet 直接称作此 Sturm 检验。

### 8.3. 删除47倍指标并得到整张成

原空间中每个 newform 的**准确 conductor**均为 $47^2$，
且 nebentypus 平凡。新形式的局部 Euler 因子定理给
$a_{47}=0$，即
$$
U_{47}f_\sigma=0,\qquad a_{47r}(f_\sigma)=0
\quad(r\ge1).
\tag{1096.23}
$$
这正是 $p^2\mid N$ 的 trivial-character newform 情形；
上述 Agashe–Stein 作者稿§2也明确列出这个标准公式。
它不是关于 level $47^2$ 全空间中 oldforms 的断言。
所以假设$\ell$在 (1096.18) 右端的像上为零，
已足以使 (1096.19) 的所有奇数 $r\le2255$ 系数为零：
被略去的47倍系数由 (1096.23) 自动为零。

由§8.2，$\ell(T_r)=0$ 对所有奇数$r$成立。
另一方面，每个 $H_{\rm odd}^j$ 都是奇指标、prime-to47
Hecke 算子的整数线性组合，见§3。因此
$$
\ell(H_{\rm odd}^j)=0\qquad(0\le j\le72).
\tag{1096.24}
$$
而 (1096.8) 模$q$仍为基，故$\ell=0$。

这证明有限集合 $\{T_n:n\in\mathcal I\}$ 的像张成
$\mathcal T/q\mathcal T$。设$L$为这些算子的
$\mathbf Z_q$-线性张成；$\mathcal T/L$是有限生成
$\mathbf Z_q$模，且其模$q$商为零，Nakayama 引理给$L=\mathcal T$。
从这些原算子中选出73个模$q$线性无关者，所得行列式为$q$单位，
故它们本身就是整基。这完成 (1096.18)。

### 8.4. 对原高度读取的准确含义

对任何这样选出的73个指标，
$\Gamma(T_{n_i})$ 都由 (1096.13) 的同一个原 CM 除子对读取。
它们的全部奇度目标仍由§4保证在4513处分盘。
与 $H_{\rm odd}^{72}$ 展开的巨大指标相比，
(1096.18) 允许只计算 $n_i\le2255$ 的实际 Hecke 对应。

这并不允许把 $T_{n_iq^2}$ 替成仅循环$q^2$核：
在非$q$局部交数中，$B_q^2$仍按完整三项展开，
一般复合$n_i$的 Hecke 核重数也照原定义保留。
本节没有执行基搜索、没有读取新的高度值，也没有断言
(1096.16) 的$\kappa$为单位。
