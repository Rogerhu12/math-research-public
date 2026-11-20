# 同一原函数与完整交理想的精确复用候选

本文及[完整源码补丁](../scripts/original-exact-intersection-reuse.patch)保存独立候选，不修改正在运行的稳定桥。它只复用同一进程内已经完成的实际对象，不减少原四组输出、地方读取或迹。尚未在公开 Actions 运行；本地只做文本、AST、hash 与 patch 可应用性检查。

## 1. 文件与稳定来源

补丁 `original-exact-intersection-reuse.patch` 增加 `original_ys_exact_reuse.py`，并修改桥与 trace 各一处主控制流。候选代码可从下面钉定的稳定来源准确重建。

补丁的原始两文件为：

- `original_ys_fraction_bridge.py`：`b7969c69468509c9d436c7bd465a3a6097dc577006339eca1652aea216509398`。
- `original_ys_normalized_shadow_consumer.py`：`bb91fd32ce7f438494a92cf24f53418fb95c3a98813ced72e4c8b1db8a2ceab9`。

稳定路径本身保持上述 hash。候选只在原 maps 实际门之后按实际成本决定是否整合，不为取得缓存回执而声称四大交理想或 shadow 已经运行。

## 2. 允许什么样的命中

`same_complete_original_fraction` 首先要求类型为实际原 `OriginalFraction`，且两个对象的 `model` 是同一原对象。随后只接受：

1. 同一个被缓存保留的实际 fraction 对象；或
2. 原306维分子向量全部相等，且分母向量全部相等。

两条向量均非 hash、短展开或剩余值，而是原整环的全部精确多项式坐标。原分母非零，因此两种门都直接证明同一个原函数。若两个不同表示实际表示相同函数，但两向量未同时相同，候选只作缓存未命中；这不会丢失正确计算，也不会错误声称两函数不等。

缓存保留实际源对象的引用，因此没有释放后 `id` 被重用的问题。代码也不用 `id`、hash、degree、norm 或地方支集作为键。至多四个条目以顺序扫描核上述完整等式，免于为缓存另作高次交叉乘法。

## 3. 真 r 次幂的复用证明

每条幂 bundle 保存同一个原 model、特征 $r$，以及原三个输入 $(v,x_p,y_p)$。首次计算严格为

$$
c_0=v^{(r-2)/3}x_p^r,\qquad y_2=y_p^r.
$$

后续命中必须逐个通过§2的等式，并核相同 $r$。故返回的是完全相同的两个函数。它不是常数反射或 Artin 置换，也没有把变量固定后只升系数。

在当前固定循环中，若实际 $d_F<2256$，四组输入的 $(x_p,y_p)$ 全是同一个原 F 对象，所以只需一套幂；若 $d_F>2256$，它们按 $a=0,1$ 各为同一个原端点对象，至多两套。实际回执仍报告查询数、不同 bundle 数、每个命中依据及原 pair 标签，不根据这个预期数提前略过等式门。

## 4. 完整 E 理想与闭点分解的复用证明

实际有效除子

$$
E(y_1,y_p)=\operatorname{div}(y_1-y_p^r)
+\operatorname{Pole}(y_1)+r\operatorname{Pole}(y_p)
$$

只依赖原 $y_1,y_p,r$。候选命中时，先逐个核§2的完整函数等式，再核两图表的完整 pole ideals：若不是同一个理想对象，必须核整条 canonical HNF 基矩阵相等，并附核 determinant 和 length 相等。反过来只给同 norm、同 degree 或同支集不能命中。

条目还固定同一个原 six、geometry、两个 chart engines 和原闭点 registry。首次计算照旧执行：全 pole ideal 乘积及真 r 次幂、完整 integral graph kernel、全部源投影、完整两图表 E、全 $s=0$ primary block 和准确射影次数。命中时共享这些**同一个实际对象**；没有另建一个少掉边界或重数的表示。

特别若 $d_F<2256$，原循环呈示使输入不依赖输出标签 $b$，故严格有 $E_{00}=E_{01}$、$E_{11}=E_{12}$。这是有效除子本身相等，不是仅在 Picard 群相等。另一个分支不预设任何两个 E 相同。

每个 pair 仍重新构造并保存它自己的 $a_0,x_o,y_o,x_{\rm out}=a_0x_o/c_0$，也保其原 $a,b$、Artin 标签与循环呈示。没有缓存或替代输出点、局部值、$m_Q,k_Q$、完整迹或最终挠坐标。

同一个完整 E 的分解也可共享。`validate_shared_original_intersection` 在进入 trace 前，核 item 的 finite ideal、完整 infinity chart ideal、infinity boundary ideal、差函数 $g$ 全是条目中的实际对象；核相同 two-chart engines、原 registry、geometry、six 以及完整次数，并再次核原 $y_1,y_p$。仅此之后才读取共享的全闭点列表。

每次共享都重新核

$$
\sum_Q\dim_k(\text{完整局部因子})
=\sum_Qe_Q[\kappa(Q):k]=\deg E.
$$

所以所共享的不是约化支集，而是同一原 maximal ideals、同一剩余域嵌入、全 primary thick factors 和真实交重。随后四个 pair 的原 trace 循环全部照旧执行；其中同一个 Q 的输出函数可能不同，必须独立读取。最终18×9、两轴和 A/C 门完全未变。

## 5. 对内存的作用和限制

该缓存保留至多四套函数幂及四套完整 E 对象，都是原循环结束后已被各 item 保留的对象。重复项只多保存引用，不复制多项式矩阵。它可以去掉重复的高次 r 幂、pole ideal power、graph kernel、全 determinant 分解、primary lifting 和重复闭点对象；不能降低第一份不同 E 的内存峰值。

各候选 receipt 明确区分“不同实际 E 个数”和“完整四 pair 个数”，不能把共享两份实际理想说成进行了四次独立 HNF。所有复用都保已完成计算的完整来源记录及首次 pair，不把旧 hash 改名伪装成新的运算。

## 6. 已逐段核到的主要内存位置

下列是对当前稳定源码的静态定位，不是已经测得的 RSS。矩阵的多项式后端可能共享不可变系数对象，因此形状不等于真实字节占用；不应把表中系数位置数直接当作实测内存。

| 位置 | 同时存在的主要对象 | 准确风险与现有限制 |
|---|---|---|
| `original_affine_fast_operations.py::multiplication_matrix_with_certificate` | 返回的306×306整多项式 operator；分量 coefficient groups；逐行 accumulators、contracted、padded、returned | selector cache 的64 MiB只是缓存上限，**不是整个 operator 的内存上限**。每行临时 prime-field矩阵被流式处理，但整93,636条输出多项式必须保留。高次输入的每项次数可接近输入实际权界加4。 |
| `OriginalFraction.__pow__` 经 adapter 的 `multiply` | 每步一份完整306×306 operator 及分子/分母结果向量 | 当前 adapter 的 vector multiplication 先形成整个 operator；真 r 幂的二进制迭代仍会触发多次。精确 bundle 缓存能去掉重复迭代，不能改变第一次的峰值。 |
| `OriginalAffineIdealEngine.zero_pole_ideals` | 两份306×306 $M_N,M_D$，612×306 stacked syzygy input，306×612全核；两306×306投影及 HNF | geometry 对 T、v、六端点、F 都走此门；分子分母全共零必须保。核的官方 saturation verifier 和完整回代还会产生乘积临时量。 |
| `OriginalAffineIdealEngine.ideal_product` / `ideal_power` | 每一步 $H_I M_b$，至多612×306行生成矩阵，以及 HNF 和306×612 transformation | 当前实现已流式处理306个乘法块，并以完整 containment+norm equality 提前结束；它**没有**同时造93,636×306的全乘积生成矩阵。风险来自单个高次 operator、HNF及其 transformation，不应误诊为全生成矩阵已展开。 |
| `OriginalAffineIdealEngine.integral_fraction_multiple` | $M_N,M_D,H_I M_N$ 各306×306；612×306 graph input；306×612全核；两投影、full-source HNF、结果 HNF | 这是四大 E 最直接的高次峰值。差函数的 N/D 权界随真 r 次幂增长，图表 shift 虽已收紧，仍可能很大。必须保完整 source module=unit 门，不能因内存把它换成 field-rank。 |
| `complete_kernel(method='hermite')` | 除上述外显式612×612的全 transformation | 默认 `minimal` 不显式请求这个大方阵。切到 hermite 不是免费的性能回退，需独立看实际峰值；也不能跳过官方完整核 verifier。 |
| `primary_block` / `infinity_boundary` | $\pi^e I_{306}$，与原HNF叠成612×306，再做HNF；$e=v_\pi\det I$ | $e$ 是完整 norm exponent，可能大于真正最小 scalar annihilator。这个保守幂在当前证明中合法且保全部厚度；不得未经证明截短以省内存。 |
| `decompose_complete_ideal` / `OriginalSmallResidualAlgebra` | determinant 的完整因式分解；逐 $\pi$ 的全 primary ideal；至多306维残代数矩阵，但系数位于实际 $k_\pi$ | “残代数维数≤306”不意味着常数大小独立于 $\deg\pi$。一般路径先把残域元素提升为次数<degπ的原多项式，再生成完整原 operator 后 specialize；大 degπ 可能成为下一峰值。没有构造 deg(E)×deg(E) 的全商矩阵。 |

例如一个306×306 operator 若各输出多项式次数约1000，它有约 $93{,}636\times1001$ 个 $k$-系数位置；这只是静态规模指标，不能据此声称某个字节数。完整 graph/HNF 还可能保多份不同中间多项式，实际系数共享与 transformation 次数必须由公开运行的 peak RSS 和 stage 日志判断。

当前长期保留项还包括 geometry 的所有正负 HNF、四个不同 E 的两图表 HNF，以及已分解点的完整局部 ideals/quotient closures。相同 E 共享可以减少其中的重复项；它不会删除任何不同 E 的局部因子。原 reader 的 valuation、principal ideal 和 q-power 缓存也会随实际读到的点数增长，应在 trace 阶段单独记录，而不能以 selector cache 的上限推断它们有界。

## 7. 后续整合接受门

整合时须先以稳定原两文件 hash 核对 patch 来源；复制三个候选或应用该 patch 后做 AST。数学仍只在公开 Actions。新回执应至少保：每条幂/E命中的完整依据、不同对象数、全部四 pair 的原输出 receipt、每个完整 E 的全次数和 closed-point长度等式，以及原完整 trace/18×9门。当前未运行候选，不能提前填任何 cache hit 数或时间/内存收益。


## 8. 独立审查与执行前集成门

补丁SHA256为 `6b59b77463c0ec9db2b58cef875ab7a700a43c40b71372cf2b94d426b3aad680`。root全文核本证明、全部补丁及稳定四pair/trace控制流，deep另独审并核AST与可应用性；global完成实现及自审。只有准确命中同一完整对象才允许复用，四条独立输出和所有真实迹门保留。

补丁尚未应用。若后续实际运行采用它，须同时把新增 `original_ys_exact_reuse.py` 加入host与数学producer的完整依赖manifest并核其哈希；本补丁本身不悄悄修改执行请求，也不替代该集成门。当前记录没有实际cache命中数、运行时间或内存RSS。
