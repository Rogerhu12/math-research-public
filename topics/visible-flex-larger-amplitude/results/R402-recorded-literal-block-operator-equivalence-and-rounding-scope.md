# R402：固定字面表与记录因子上的完整 R305 块作用

作者：AI 助手（amplitude），2026-11-15。本文只作原源码阅读与条件代数推导，没有执行科学数值、编译或性能试验。186 原文件和正在运行的请求保持冻结。

## 1. 结论与对象

原 R305 对同一个实际 field、同一条已选择的 root trace，分别对 224 个状态方向重复角节点线性收缩。可以先用全部原字面 sine、cosine、gram 表形成每次 root update 的两个矩阵，再对完整 224 列作用；最终 flux 也可形成两个矩阵。该变换没有删模态、删角节点、删 stage，也不需要任何理想三角恒等式。

准确的等价对象是：给定本次实际记录的局部线性系数、名义 Newton 步、名义 Cholesky 因子和已选择的回溯词之后，原 R305 线性递推在准确实算术中的作用。它不是 IEEE 舍入映射的导数，不是未经误差支付的完整有限 root 准确导数，也不能把保存的 Cholesky 因子默认为原 C 的精确因子。

预装配改变乘加结合和舍入位置，必须成为独立源码身份。它与 186 的保原输出累加顺序外提是两种不同实现，不能借 186 的条件逐词责任声称新矩阵实现逐词相同。

依据原完整 source：

- [R305 operator header](../computations/geometry_20261115_native_operator_trace128.hpp)，SHA256 950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0。
- [原完整 stage driver](../computations/geometry_20261115_native_operator_stage128.cpp)，SHA256 86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926。
- [共享 primal/trace](../computations/geometry_20261115_native_shared_trace128.hpp)，SHA256 bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b。
- [186 保原运算顺序接口](../notes/2026-11-15-request186-hoisted-complete-final128-interface.md)。

## 2. 原程序中的具体重复

原 header 的 input_direction 对每列形成全部 P、Pt；returned_L_direction 对每一个实际成功 root update、每列完成以下工作：

1. 用原 cosine 表把 J 个 dL 分量作用到全部 N 个角节点。
2. 以局部六坐标系数形成 dq、d-rho。
3. 把 dq 收缩回 J 个方程，把 d-rho 收缩为 2M+1 个 beta。
4. 用原 structured_C_action 将 beta 作用于该次真实名义步。
5. 用该次保存的 L 作两次三角代回，读取全部 C*ds-right 行，更新 de。

最终 RHS 再从同一列的 momentum、dL 形成全部 dU 和 flux 收缩。当前 stage 的 M=112、J=113、K=224、完整状态 226、N=2048 都来自真实 packet/source 约束；这里没有以这些整数代替实际 substep 网格。

rk4_batch_parameters 已共享每个 field 的 primal/root trace，故再次“共享 primal”不能重复计作新的提速。仍重做的是固定表上的方向算术。prepare_field 的原 C 重建、LLᵀ-C、三角代回残差也只每个实际 field/update 做一次，不是 224 份；不得据此夸大可删除成本。

## 3. 三张字面表必须分开

令 S 为 N×M 的原 sine 表；C 为 N×J 的原 cosine 表；G 为 N×(2M+1) 的原 gram 表。所有元素取实际保存的 binary64 字，再按原程序 lift，不替换为某个理想角的精确三角值。

记号区分：后续 W、A、F 矩阵公式中的 C 均指本节 N×J 的字面 cosine 表；文字“原C”、源码 u.C 和因子残差 LLᵀ−C 中的 C 指 J×J 的原 root 矩阵。两者维数、来源与责任不同，不作相互替换。

另定义 B 为 N×J：

$$
B_{n0}=1,\qquad B_{nj}=C_{nj}\quad(1\le j\le M).
$$

原因是 angular_L_direction 的第零项直接从 dL[0] 开始，而方程收缩使用实际 C[n,0]。即使当前表恰好记录 1，也不能在通用接口中未经绑定便把二者混同。令 C_1 为 C 的非零模态列，Omega 为原 frequency 的对角矩阵。

给定单列原 input_direction 已实际形成的 momentum 向量 m∈R^M、target 向量 t∈R^J，以及当前 de∈R^J，在本节准确实线性对象中：

$$
dP=S m,\qquad dP_t=C_1\Omega m,\qquad
dL=t+de,\qquad d\ell=B(t+de).
$$

新实现可保留原 input_direction 的小规模 target/momentum 标量形成顺序，仅避免其角度循环。这样不必把 r³、r⁴、w、w²、E、mu 的有限字面形成重新解释为其他连续恒等式。非零 geometry/步长参数方向保留原完整 fallback；下面不因固定状态方向而宣布它们不存在。

## 4. 原 C 布局的有限线性作用

对某一次实际 update，令 s∈R^J 为保存的名义 Newton 步。定义 H_s 为 J×(2M+1) 矩阵，使对任意 beta：

$$
(H_s\beta)_0=\beta_0s_0+
\sum_{j=1}^{M}(\sqrt2_{\rm lit}\beta_j)s_j,
$$

$$
(H_s\beta)_i=(\sqrt2_{\rm lit}\beta_i)s_0+
\sum_{j=1}^{M}(\beta_{|i-j|}+\beta_{i+j})s_j,
\qquad1\le i\le M.
$$

这里 sqrt2_lit 是原记录常量，不以数学常数替换其字面词。H_s 的各列系数按上式逐项相加定义；两个索引相同也须保实际贡献。

这恰是原 structured_C_action 的准确实双线性式。它来自原 root_matrix 明写的 beta 布局，不来自把 cosine 外积改写成 gram 的三角积化和差。尤其不宣称 C=F_e。

设本次实际局部系数为 q_P、q_Pt、q_L 及 rho_P、rho_Pt、rho_L，它们分别来自 PointOperator.quad/rho 的前三坐标。对 x∈{P,Pt,L} 定义 J×N 矩阵

$$
W_x=\frac1N\left[C^\mathsf T\operatorname{diag}(q_x)
-H_sG^\mathsf T\operatorname{diag}(\rho_x)\right].
$$

只固定 geometry 的本段用途不涉及第四坐标 U 和后两坐标 w²、E 的方向。未来若一般化，必须显式加入原缺失列，不能把本段公式冒全部参数方向。

定义

$$
A_m=W_P S+W_{Pt}C_1\Omega,\qquad A_L=W_L B.
$$

其中 A_m 为 J×M，A_L 为 J×J；全部 N 个节点与全部 2M+1 个 gram 列都包含在形成中。

## 5. 每次 root update 的完整等价式

**命题一。** 固定上述记录，按原 R305 的准确实线性式形成 dF、beta 和 action，则其传给因子代回的 right 恰为

$$
\boxed{\quad right=de+A_m m+A_L(t+de).\quad}
$$

**证明。** 原式为

$$
dF=de+\frac1N C^\mathsf T
\left[D(q_P)Sm+D(q_{Pt})C_1\Omega m+D(q_L)B(t+de)\right],
$$

$$
beta=\frac1N G^\mathsf T
\left[D(\rho_P)Sm+D(\rho_{Pt})C_1\Omega m+
D(\rho_L)B(t+de)\right].
$$

原 action=H_s beta。将 right=dF-action 展开并按 m、t+de 分组，得到上式。全是有限矩阵分配律，没有 Fourier 正交、cosine 乘积公式、理想频率网格、删除高频或数值秩前提。证毕。

新数值实现可保留每列原 de 递推，而只将角节点工作替换为这两个矩阵的作用。这样每一次实际 update 仍有独立的 right、ds、完整原 C*ds-right 行和 de 更新，不必用“只保存最终总 Jacobian”掩去内部解残差。

## 6. 名义因子不能偷换成 C 的精确逆

令 Lhat 为该 update 实际记录的下三角因子，且其对角非零。定义准确实线性算子

$$
T_{\widehat L}v=(\widehat L\widehat L^\mathsf T)^{-1}v.
$$

原 factor_direction_solve 在准确实算术中恰执行这一算子。有限程序的三角代回还会有舍入；原记录中 LLᵀ-C 和 C*ds-right 未被证明为零。

固定实际选择的 alpha=2^{-backtrack}，更新为

$$
de_{\rm next}=de-\alpha\,T_{\widehat L}
\left[de+A_m m+A_L(t+de)\right].
$$

由命题一逐 update 归纳，原准确实 R305 递推和本矩阵递推给出同一个返回 dL=t+de。这里不把名义 s 换成精确 C^{-1}F；H_s 必须用实际保存的 s。

若想进一步把该对象称为某个理想 root 程序的准确导数，还需另付原有限点系数形成、名义 factor/step 及其残差导数、真实分支稳定等责任。本文只证明记录算子的代数等价。已选择 alpha 固定不表示选择边界可微；也没有对 IEEE 舍入算子求导。

## 7. 最终 flux 的两个矩阵

令 phi_P、phi_Pt、phi_L、phi_U 为最终原 PointOperator.flux 的前四个坐标系数。E 为从 J 个 dL 分量抽出非零 M 个模态的选择矩阵。原程序中

$$
dU=S[-\Omega E\,dL+(\Omega^2-I)m].
$$

因此定义 M×M 和 M×J 矩阵

$$
F_m=\frac1N S^\mathsf T
\left[D(\phi_P)S+D(\phi_{Pt})C_1\Omega+
D(\phi_U)S(\Omega^2-I)\right],
$$

$$
F_L=\frac1N S^\mathsf T
\left[D(\phi_L)B-D(\phi_U)S\Omega E\right].
$$

**命题二。** 在同一记录系数的准确实作用中，原全部 flux 方向恰为

$$
\boxed{\quad dflux=F_m m+F_L dL.\quad}
$$

证明是将原四坐标局部线性式中的 dP、dPt、dL角值和 dU 代入，再分组，仍不涉及任何理想三角恒等式。

其后的完整 226 RHS 标量程序保持原字面，包括 Y、Pi 两组全部112模态、meanSlope 的 dr*w*dL[0] 和另一均值坐标、独立几何字和 prefactor。无需把这些小标量表达式再压成一个不同舍入的简化公式。非零 geometry 情况使用原完整 D 程序/fallback。

## 8. RK、端口和全部范围

所有 a、b、c、d 四个 field 的 primal 值、root trace、原停止阈值和选出的步仍由原程序实际形成。新线性动作只替换对应 field 的方向计算。按原 RK 状态递推逐场代入命题一、二，可由线性归纳得到同一个记录系数准确实 RK 方向。

完整 stage 仍以真实 node n+1 的当前128状态出发，对 224 个原单位种子全部传播；两均值行保留。原状态方向的初始均值行为零，不代表传播后的均值行可删。端口对原 Pi 坐标的 ratio 除法、输入输出节点身份、全部576阶段保持。

因此完整后继仍须原真实 owner/replay→全部576×224→112边界→338×112混合端点→独立audit。没有以局部field比较替代全stage、以factor残差替代物理接受，或以某个已有accepted状态省略本次真实来源。

## 9. 哪些可以逐词保持，哪些不能

**可保原每个输出算术图的列块重排。** 将互不依赖的 column 循环移到内层，用小固定列块复用同一个 literal表/局部系数；只要每一个输出仍按原 j、n、k 顺序执行同样的 primitive、原括号和 invN位置，且没有跨列共享会改变分支或舍入的状态，那么独立列之间的执行交错不改变各输出 primitive 序列。这是条件程序等价，不是实测性能或硬件环境证书。

**预装配不具有这项逐词保证。** 形成 A_m、A_L、F_m、F_L 后再乘方向，原先“先对方向乘表再收缩”的结合次序改变；可能把 invN、乘积、加法移至不同层。即使准确实代数相等，有限 binary128 结果也可能不同。新源码必须说明原列循环图并未逐词复刻，记录实际新矩阵身份与各层算术策略。

不能一面把每列重做的角点乘法换成预先矩阵乘法，一面只保留旧schema或写“同 IEEE words”。本段也不把“原 local_partial_rows 相同”当作完整方向误差已付。

## 10. 密集预装配仍不是 29 倍保证

对 K 列，原每次 update 至少反复形成 N×J 的 dL角值、N×J 的方程收缩和 N×(2M+1) 的 gram 收缩；最终还有输入与flux角变换。预装配将列相关的角工作移为每field/update一次，但它自身仍需要加权字面表的密集积。

一般形成 H_sGᵀ、A_m、A_L 所需的标量工作仍包含 N、M² 量级；随后每列还需两个小矩阵作用、原两次三角代回和所有 C 解残差行。故“先组完整小矩阵”只是可明确实现的结构改进，不能仅凭复杂度符号声称达到完成576stage所需的约29倍吞吐。

可在每个实际阶段的原必要摘要中记录预装配次数、角节点/系数覆盖、真实列数、实际时间、fallback和未付后缀，保持整个完整运行。没有另设孤立benchmark或非零/秩通过门。若实际预装配更慢，同样如实返回，不通过缩列/放宽域来把资源问题改写为成功。

## 11. 更强但独立的精确字面点积途径

字面表不需要理想三角结构才能用块矩阵乘。所有有限 binary128/64 数都是 dyadic，可将矩阵条目按行/列共享二进制指数展开为有符号小整数 digit。以下只证明该内核的有限代数合同，不宣称已有实现或实际提速。

取 digit宽度 b=20，每个内积块长度 k≤2048。若

$$
|a_{\ell n}|<2^{20},\qquad |b_{n r}|<2^{20},
$$

则每个乘积及任意顺序的部分和满足

$$
\left|\sum_{n\in I}a_{\ell n}b_{nr}\right|
\le k(2^{20}-1)^2<2^{51}.
$$

所以使用有符号64位整数的乘积/累加可精确完成该块，没有溢出；也不需要对三角表作任何近似。若 A、B 的所有原dyadic位都被展开，则

$$
A_{in}=\sum_\ell a^{(\ell)}_{in}2^{u_i-20(\ell+1)},\qquad
B_{nj}=\sum_r b^{(r)}_{nj}2^{v_j-20(r+1)}
$$

给出原字面矩阵积的准确恒等式

$$
(AB)_{ij}=\sum_{\ell,r}
\left(\sum_n a^{(\ell)}_{in}b^{(r)}_{nj}\right)
2^{u_i+v_j-20(\ell+r+2)}.
$$

可用分块整数矩阵积计算括号内项，再在有符号宽整数累加器中按二进制位置合并，最后仅一次 round-to-nearest-even 到 binary128。这样一个内积是该输入dyadic点积的正确舍入，而不是原顺次quad累加的逐词结果。

具体实现必须覆盖负数、精确零、normal/subnormal、指数跨度、ties、溢出和原rounding环境。digit数不能凭“六份已足够”截去小项；必须真实完整展开，或显式保精确余项/进入完整原quad fallback。不可把遗漏尾位称作原字面算子。未来使用 SIMD 只改变整数运算并行，不改变上述安全上界；依赖其他库时仍需其真实接口/编译来源。

该内核可加速预装配的密集角收缩，但是否抵消digit展开/整数累加/轮数开销尚未测量。它也不自动解决三角解或原名义factor误差。它是独立后继选项，绝不作为186的前置门。

## 12. 有限形成误差必须分层保留

即使上述内积正确舍入，矩阵形成后的中间系数再次参与乘法/解算，也不等于全线性算子一次准确计算。若某一步形成 Ahat=A+EA、Bhat=B+EB，则准确实恒等式给

$$
|\widehat A\widehat B-AB|
\le |A||E_B|+|E_A||B|+|E_A||E_B|.
$$

另加实际乘法内核的舍入包围，才是该步输出误差界。逐 root update 的算子误差仍会通过真实 T_L、alpha和递推累积，不能把某一个点积的半ulp界冒成完整stage导数界。

本节只提供证明传播的代数结构。没有对实际系数、inverse或整链形成区间外包，没有从小数残差宣称严格误差证书。原 LLᵀ-C、C*step-F、C*ds-right 仍应读取，且仍不是这些误差本身的包围。

## 13. 最小可执行源码接点

建议独立实现以下对象，保持旧950e/186源原样：

- PreassembledUpdate：本次 actual update索引、实际s/L/C身份、A_m与A_L及其真实形成方式。
- PreassembledField：原PreparedField/actualRootTrace责任、全部PreassembledUpdate、F_m/F_L。原primal不重写，新的preassembly只能消费同一次捕获的真实记录。
- input_momentum_target_original：保原小标量input形成，不生成每列P/Pt大向量。
- returned_L_preassembled：每列原de初值、实际update顺序/alpha、原factor_direction_solve及全部C残差行照付；仅right角收缩换为完整矩阵作用。
- rhs_direction_preassembled：最终flux用两个矩阵，后续完整226 RHS标量代码原样复用。
- rk4_batch_preassembled：原四field、h、种子224、mean/port均保。非零geometry/参数接口明确原fallback，不能因当前state-only调用默删。
- 独立stage/launcher source-view：在本次same-job当前128点生成完整576stage；原boundary、endpoint、audit继续读取真实新stage身份，不能把新近似矩阵改标签冒旧word版本。

记录只输出必要计数、原flags、误差/范围及矩阵SHA；成功大矩阵仍临时。所有真正数值/性能由一次完整公开Actions运行支付，不另加fixture。主控已为独立完整预装配后继保留 Request190、实际结论 R403；当前没有生成其运行事实，也没有改186预算及任何科学接受门。20-bit digit内核仍只是条件实现途径，本结论不以它代替尚未实现的数值误差或速度责任。
