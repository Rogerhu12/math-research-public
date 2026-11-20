# R931 上层完整 Artinian Tate/Miller consumer：契约与实现证明

日期：2026-11-20。源码文件：original_ys_artinian_shadow_consumer.py。

状态：已接实际源码，AST 语法检查通过；root/theta全文独审，deep另核原来源和完整分区。尚无数学执行或运行性能回执。它只在公开研究仓库的 Actions 中允许执行。基础 original_ys_artinian_norm_tools.py 保持已经交叉审阅的版本不变。本文及源码不把静态审阅当成原 shadow 的实际 PASS。

## 1. 入口、真实来源和精确返回

唯一前端入口为：

    consume_original_artinian_shadow(
        intersection_context, trace_method="artinian", progress=None
    ) -> (result_context, receipt)

trace_method 必须是 "artinian"。输入是当前原桥 build_original_four_intersections 返回的 rank2_original_Y_four_intersection_context 实对象。上层不构造另一个模型、常数域或格，也不自行凭前缀补原函数。必须已经有：

1. 原 F/P 两个来源证书和同一个 cube/截面嵌入来源；
2. 同一个 \(Y=X_0(3468)\) 的完整 306 秩正规化，两图表、全部 46971 个基乘积及原单位已通过；
3. 原 \(k=\mathbf F_{r^2}\)、原 \(\omega\)、原 \(\pi_1,\pi_2,\pi_4\)、所有差分因子 \(j^m\)、原 \((v+4)/v,\epsilon,\theta_{17},d_{\rm new},\lambda\)；
4. 全七原椭圆方程、两个端点、原 \(W\) 与常数反射已实际检验；
5. 全部原 cusp/分歧来源、七条实际极除子，以及实际 \(d_F\)；
6. 四个原有效 \(E_{00},E_{01},E_{11},E_{12}\) 的全部有限理想、无穷图表理想、恰为 \(s=0\) 的完整边界理想和完整次数。

输入中的实际 engine、geometry、registry、fraction model、原域及来源对象逐一以对象身份核准。已共享的完整 \(E\) 使用现有 validate_shared_original_intersection 再核源；真实 \(c_0=v^{(r-2)/3}x_p^r,\ y_2=y_p^r\) 必须仍来自同一个 OriginalExactIntersectionReuse.power_bundles 实对象。输入比较仅接受同一原分式对象，或两条**完整** 306 坐标分子、分母向量相等。没有使用摘要、次数、局部前缀或剩余值作为等式判据。

每个 pair 的输出和 trace 仍独立计算。即使两个 pair 共享完整 \(E\)，也不据此共享其原输出点或最终 trace。

成功返回的 result_context 具有：

    kind = rank2_original_complete_artinian_shadow_context
    original_intersection_context       # 输入原实对象
    original_torsion_basis
    original_tate_reader                 # 原 calibration；未伪报逐闭点调用
    original_artinian_norm_tools
    complete_pair_length_accounts       # dict，键严格为四个原 tuple(a,b)
    all_nine_original_trace_points
    original_point_detector
    certificate                         # 与返回 receipt 同对象

成功回执的 kind 为 rank2_same_original_artinian_relative_six_frobenius_shadow，status 为 complete_original_shadow；它们只在全部实际运算和接受门已完成后才会产生。回执明确：

    complete_intersection_closed_point_decomposition_claimed = False
    per_point_scalar_trace_comparison_claimed = False
    ordinary_nonvanishing_or_infinitely_many_p_claimed = False

这里的完整性由厚代数、全长度及范数定理给出，不伪称已经列举闭点。

### 1.1 前端可逐字使用的长度账

result_context["complete_pair_length_accounts"][(a,b)] 的键为：

    endpoint_pair: [a,b]
    full_original_intersection_degree
    finite_original_intersection_length
    infinity_original_intersection_length
    ramified_finite_length
    ramified_infinity_length
    common_pole_length
    common_zero_length
    output_O_length
    finite_extra_length
    accounted_full_k_length

除 endpoint_pair 外均为 Python int。receipt 中同名 complete_pair_length_accounts 是按 ((0,0),(0,1),(1,1),(1,2)) 顺序排列的四项可序列化列表。对每项实际断言：

\[
\begin{aligned}
\deg E={}&\ell_{\rm ram,fin}+\ell_{\rm ram,\infty}
+\ell_{\rm common,pole}+\ell_{\rm common,zero}
+\ell_{\rm output\,O}+\ell_{\rm finite\,extra},\\
\deg E={}&\ell_{\rm finite\,original}+\ell_{\rm infinity\,original}\\
={}&\texttt{accounted\_full\_k\_length}.
\end{aligned}
\]

全度数仍由原实际 \(d_F\) 分支决定：\(2256+r d_F\) 或 \(2256(r+1)\)。不存在预设 \(d_F=1296\) 的替代。

## 2. 完整除子分离及 capped power 的正确性

固定同一个有限图表 \(A/k[\xi]\)。上层没有修改基础 helper 的理想和、完整有效商、Fitting、全图核或范数算法。

### 2.1 全分歧和无穷边界

先直接在原格核原分式 \(v=\xi^2-1\) 的完整交叉乘法等式。其真正有限零理想与既有完整几何中的零理想逐整个 HNF 相等；正负全次数均为 \(2\cdot306=612\)。已给的原全分歧记录逐项核：

- 有限两纤维的阶是 \(1,289\)，几何支集度 36；
- 无穷纤维的阶是 \(-2,-578\)，几何支集度 18；
- 全部阶不被 3 整除，总分歧几何度 54。

有限 \(E\) 按真实理想 \((v)\) 作完整 Fitting 分离。无穷的原 infinity_boundary_ideal 全保，且其首一行列式范数严格为 \(s^L\)，其中 \(L\) 是该完整厚理想的 \(k\) 长度。它的所有厚分量均在原分歧纤维，而非遗漏的另一个仿射点。上述两部分按 R883 的原 CM 固定点结论有零的整个 \([6]\) 输出；它们的完整长度仍进入总账。

余 \(E_{\rm nr}\) 上实际用完整单位解再核 \(v^{-1}\)，所以后续使用“\(v\) 是单位”不是仅来自口头支集判断。

### 2.2 真零极除子及 \(c_0\) 的合法简化

所有零极使用原完整饱和图核给出的真正除子。已有原几何缓存只在同一原函数对象时复用；新需要的 \(a_0,x_p\) 只计算完整有限图表零极，不把这个局部于图表的缓存冒写为全局两图表缓存。该附加缓存限于七个原 \(x\) 映射的实对象。

在已实际认证 \(v\) 为单位的 \(E_{\rm nr}\) 上，

\[
\operatorname{ord}_Q c_0
=\frac{r-2}{3}\operatorname{ord}_Q v
  +r\operatorname{ord}_Q x_p
=r\operatorname{ord}_Q x_p.
\]

故该开集上严格有 \(Z(c_0)=rZ(x_p)\)，并始终有 \(P(y_2)=rP(y_p)\)。这只是原真实幂函数的除子恒等式；原 \(c_0,y_2\) 对象及来源都保留。上层因此无需另求高次 \(c_0\) 的完整图核。

### 2.3 每步截回原完整 \(E_{\rm nr}\) 的幂

给定非零完整理想 \(I,J\)，_capped_power(I,J,e) 返回**整个** \(I+J^e\)。它对完整理想作二分乘方，每次乘法后取完整理想和 \(I+(\cdot)\)。正确性为

\[
I+(I+J^a)(I+J^b)=I+J^{a+b}.
\]

这在任意交换环的理想中直接成立，不依赖支集约化或秩猜测。源码保整数幂的完整递推记录、每次完整乘法和、全部 HNF 来源及最终 \(I\subset I+J^e\)。中间取商长度至多 \(\dim_k A/I\)；乘法前未经截回的两因子之积长度至多两倍该数。这是代数尺寸界，不是实际时间保证。

用此算法恰构造

\[
\begin{aligned}
C_{\rm pole}&=\min(E_{\rm nr},P(y_1),rP(y_p)),\\
C_{\rm zero}&=\min(E_{\rm nr},
  3\min(Z(a_0),rZ(x_p))).
\end{aligned}
\]

内层先与 \(E_{\rm nr}\) 取最小不改变外层结果，因为逐点 \(\min(e,3\min(e,a,b))=\min(e,3\min(a,b))\)。两共同支集完整 HNF 和必须为 \(A\)。完整乘积给共同除子的和，有效商回乘整个 HNF 必须恰回原 \(E_{\rm nr}\)。这严格是原逐点 \(3m_Q\) 的消去，不是把 \(E\) 的共同零任选消掉。

### 2.4 输出 \(O\)

余 extra 按原 \(P(y_{\rm out})\) 分离**整个**厚局部分量。输出 \(O\) 的长度进入 output_O_length；不只是减去仿射极阶。其它非分歧 cusp（\(\xi=0,\pm3\)）以及所有非 cusp 未被预先排除。它们都经过同一完整 extra 处理。

## 3. 原值、全厚曲线恒等式及所有常数边界

对余 \(I=I(D_f)\)，原 \(x_{\rm out}=a_0f_{\rm out}/c_0\) 和 \(y_{\rm out}\) 均由基础 helper 的完整饱和图核回收。分子、分母必须是同一原分式的全部 306 坐标；完整图核中取同一系数组合，使配对分母模 \(I\) 等于 1，再回代**全局**分式身份。因此原分式任意阶共同零都正确处理。单独找 \(Dx=N\bmod I\) 的解从未用来识别原值。

随后实际在**整个** \(A/I\) 验证

\[
y_{\rm out}^2=x_{\rm out}^3+1.
\]

这里不是只检查约化点。R931 中原误差恒等式

\[
x_{\rm out}^3-(y_{\rm out}^2-1)
=(y_{\rm out}^2-1)\frac{(y_1+y_2)(y_1-y_2)}{y_2^2-1}
\]

在 ordinary、共同三挠和双极三个原情形的阶均至少 extra 的完整重数 \(e_Q-3m_Q\)，保证该门应当通过；源码仍实际计算完整余项。

构造所有支集理想时从 I.basis 起，stack 给定元素的完整乘法算子。若要同时给 \(x-x_Q,y-y_Q\)，就 stack 两个完整算子。这得到 \(I+(h)\) 或 \(I+(h_1,h_2)\) 的全秩完整行模。

**特别地，程序不调用 principal_ideal(0)。** \(h=0\)、原输出恰为常数、原输出恰为常数挠点、某个辅助分量为空，都由同一全模定义正确处理。只要 \(I\neq A\)，曲线上的仿射输出也不会被误作射影无穷点。若 \(I=A\)，所有后续范数为 1，并明确记录全长度 0。

## 4. 两辅助点与两个加法图表

完整复用 OriginalTateTraceReader 给出的原 \(T_1,T_2\)、另一轴 \(U_i\)、循环子群、Miller 链和同原 \(M,M^{-1}\)。不另选挠点基、\(\omega\) 或 pairing 方向。

对一个 \(i\)，\(\langle T_i\rangle-U_i\) 的全部 \(\ell\) 个不同原 \(k\)-有理仿射点都使用两条坐标方程完整拉回。其理想乘积只用于确定有限并集的支集，并在每步加回原 \(I\)；接着完整 Fitting 分离恢复原 \(I\) 在这些点的**所有**厚度。

good 上取 \(R=U_i\)，bad 上取 \(R=2U_i\)。除去数学证明 \(U_i\notin\langle T_i\rangle\) 外，程序还对 bad 上 \(\langle T_i\rangle-2U_i\) 的整个拉回理想实际核为 \(A\)。第一分量的原 bad 理想与 good 理想的全和也必须是 \(A\)。所以两个辅助选择都在完整局部环层面排除了禁止的剩余支集。

然后在每个非空辅助分量上按 \(x-x_R\) 再完整 Fitting 分离。

- 单位分量使用 \(\lambda=(y-y_R)/(x-x_R)\)；
- 零支集的整个厚分量使用 \(\lambda=(x^2+xx_R+x_R^2)/(y+y_R)\)。

每个分母用完整单位解核回乘积 1。第二式保 \(P=R\) 的倍点情形，而 \(P=-R\) 已因 \(P+R=O\in\langle T_i\rangle\) 被辅助选择排除。程序实际在全厚商中再核两条关系：

\[
\lambda\,(\text{所用分母})=\text{所用分子},\qquad
\lambda(x-x_R)=y-y_R.
\]

同一群律给

\[
x_Z=\lambda^2-x-x_R,\qquad
y_Z=-y+\lambda(x-x_Z),
\]

并对整个厚商重验 \(y_Z^2=x_Z^3+1\)。这里是在 \(E_0(A/I)\) 中加法；没有把尚未全局满足曲线方程的 \(Y\) 上两个有理函数直接代入一个全局弦分式。

辅助和加法两层每次都核全子分量长度之和等于母分量长度。无需显式保存 CRT 幂等元坐标：完整两理想和为 \(A\)、乘积回原理想，已经认证同一个完整 clopen 分解。基础 helper 的 with_idempotents=False 只省去不消费的坐标，不省任何全厚分量。

## 5. 每条原 Miller line 的单位与原 \(k\) 范数

每个实际原链条目为 (square,(ax,ay,a0,bx,b0))，全部系数必须仍在同一个原 \(k\)。逐步精确计算

\[
\frac{a_xx_Z+a_yy_Z+a_0}{b_xx_Z+b_0}.
\]

**每条分子和每条分母都实际取得完整单位证**，不只验最终 Miller 函数有理。除已明示系数使该因子就是一个非零原 \(k\) 常数外，完整使用基础 helper 的单位解。常数快捷分支先核整个向量确是该原常数乘原单位，再在完整商核其逆的乘法返回。

随后调用原 _evaluate_miller，在实际辅助点 \(R\in E_0(k)\) 得到同一链的 \(f_{T_i}(R)\)。先在该完整厚商中除以此原常数，才计算

\[
\operatorname{Norm}_{(A/I_{\rm component})/k}
\bigl(f_{T_i}(P+R)/f_{T_i}(R)\bigr).
\]

因此常数分母也被准确提升到该厚商的完整 \(k\) 长度幂；不会遗漏残域度或只除一次这个常数。

基础 Norm 只分解 \(k[\xi]\) 中的首一行列式范数，沿每个 \(\pi\) 的所有完整层计算至多 306 维的实际诱导算子行列式，并用原嵌入的 \(k[\xi]/(\pi)\to k\) resultant。每层实际核满整商的 intertwiner，每因子及全体都核 \(\sum\deg(\pi)\dim(\text{layer})\) 等于完整长度。它没有把厚代数换为约化代数，也没有取到 \(\mathbf F_r\) 的绝对范数。

由 R931 的局部全旗标公式，该值恰为

\[
\prod_Q\operatorname{Norm}_{\kappa(Q)/k}
\bigl(f_{T_i}(P(Q)+R_Q)/f_{T_i}(R_Q)\bigr)^{k_Q}.
\]

虽然没有逐个列举 \(\kappa(Q)\)，所有闭点度数和真正 \(k_Q\) 都在这个实际完整行列式中。中途不将度数或重数约去模 \(\ell\)。

两辅助、两加法图表的所有范数在原 \(k\) 相乘后，才取 \((r^2-1)/\ell\) 次幂，以原 root_powers 读 log。最后严格使用

\[
\text{coordinates}=M^{-1}\bigl(6\,\text{logs}\bigr),
\]

得到同原挠点基中的整个 \([6]\)trace。实际回验原 torsion["coordinates"] 表及 \(\ell\)-挠条件。

## 6. 原九点、全 Artin 和两轴完全保留

四个实际 whole trace 完成之后，才应用原 \(W\) 对称及常数反射恢复其余九点矩阵，与旧 consumer 的公式逐项相同。仍核两个原 Frobenius 约束和全部 \(\ell\)-挠条件。

接着完整调用现有 legacy.read_full_artin：

- 全部 18 个原 Artin 标签；
- 每个标签的完整 \(3\times3\) 点阵；
- 原 \((2,0,1)\) 顺序及三对原形式；
- 原实际 CM 矩阵和系数域；
- 全 \(18\times9\) 读者与原九项公式的实际比较；
- 原 \(A,C\) 两点检测，和三对同时零/非零条件的比较。

返回的非零仅为这一固定辅助素数上的原有限 shadow 与相应 R880/R859 AJ 检测结论；没有对 ordinary 两 \(p\) 位、原 \(D_{\rm fun}\) 增广阶或无穷多个目标 \(p\) 作新声称。

## 7. 依赖、内存和验收范围

上层 SOURCE_DEPENDENCIES 逐字列出本文件、稳定 R931 基础 helper、原 ideal/local/closed helpers、原 fraction/exact-reuse、原 normalization/fastops/section embedding、原 quotient helper，以及原 relative-six/Tate/coefficient 三个消费者。它是上层执行闭包的新增依赖清单；独立 producer 仍应保留从 cube、compact、306 环、maps、geometry 到四 \(E\) 的已有全来源清单。

上层不保全部 \(\kappa(Q)\) 的原数据，不保存大型矩阵文件，也不逐点搜索参数。支持理想、图核、完整 HNF 与层算子仍可能很大。本实现没有实际运行时间或峰值内存承诺。

可静态确定的范围是：

- 原 \(k[\xi]\) 模秩始终 306；
- capped power 的取商长度不超过其母除子长度；
- 两辅助的禁止集每个恰含 \(\ell=5\) 或 7 个原有理点；
- 每轴最多两个辅助分量、各最多两个加法分量；
- 每个 Norm 层在其指定 \(k_\pi\) 上维数至多 306；
- 原真 x-map 附加有限图表缓存至多七个，保存实际原对象；
- 原 \(x,y\) 两个完整乘法算子在辅助分离后即释放，再进入 Miller line 与 Norm，避免在该阶段额外保这两个不用的算子。

实际 producer 应只在全部接受门成功后写 final PASS。任何失败只证明该具体执行未完成；不证明原 shadow 零或不存在，更不推翻 ordinary 或最终无穷素数问题。
