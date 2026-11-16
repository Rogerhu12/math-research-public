# R522：完整 dyadic 矩阵点积的双输出与整数位平面复用

作者：ChatGPT /root（AI 协作），2026-11-16 UTC。

**可信度：已证明，限完整有限输入点积的字等价、完整矩阵覆盖及明确源码组合。尚未编译、执行科学或测量性能。** 本条针对实际 R414/R445 的完整 stage 矩阵乘法；不改变原有限问题、原全部224列、两条均值、owner/replay、FD、fullDN或任何接受门。

## 1. 实际接点与已付祖先

原 [R405](R405-complete-dyadic-digits-and-once-rounded-binary128-dot-products.md) 的有限 binary128 字解码、完整整数和及最终一次 RN113 在 geometry_20261115_native_exact_digit128.hpp，18871 B / 5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc。原 [R414](R414-complete-signed-digit-SIMD-and-RN113-equivalence.md) 的 scalar/AVX2 有符号整数部分和在 geometry_20261115_native_simd_exact_digit128.hpp，9006 B / 1695b945c706523036ab85d46e1db89494719ff1b5a86efe469c39d696a556e6。

实际 operator 为 geometry_20261115_native_simd_digit_operator_trace128.hpp，29035 B / b183eeecf4f3009bf202dd0f465c8d4fdb17d8cc0ce14bb90d1ed5e6ecf485ac。它有两个完整消费者：

1. DenseMap.apply_batch 调用原完整矩阵 multiply，形成全部 requested columns。
2. RightCache.left_multiply 为每一左行、每一右列独立调用原完整 dot，覆盖实际 gram、momentum、L 和 flux 的原全矩阵。

相邻两个右列的 dot 都读取同一左行的相同 digit plane。本条将这两个完整输出放在同一个小 reducer 中，使源码里的左 plane 载入和奇位移动只形成一次。没有截断列、稀疏近似、低秩、理想三角恒等式或新的浮点 dot。

新的独立头文件是 [geometry_20261116_native_paired_exact_digit128.hpp](../computations/geometry_20261116_native_paired_exact_digit128.hpp)，8729 B / 480b1b9a197659722dfa19f8f3e491939b13b414fc60e63f9265b30aa20b1d47。它包括上述两个原件，不修改其字节。

## 2. 完整有限字与原计数范围

对原 prepare 成功解码的有限字向量，在它实际选取的 exponent base 下写

$$
a_i=2^{e_a}\sum_{\ell=0}^{L_a-1}a_{i\ell}2^{20\ell},
\qquad
b_i=2^{e_b}\sum_{m=0}^{L_b-1}b_{im}2^{20m},
$$

其中每个有符号 digit 满足 $|a_{i\ell}|,|b_{im}|\le2^{20}-1$。正负号、完整113位 significand、normal/subnormal exponent、负零解码全部沿原 R405。fast packed 表达只有在原最多12层及原 packing budget 允许时使用；不能把超过12层当作零或截断成固定六层。

因此完整点积的准确值为

$$
S(a,b)=2^{e_a+e_b}\sum_{\ell,m}2^{20(\ell+m)}
          \sum_{i=0}^{k-1}a_{i\ell}b_{im}.
\tag{522.1}
$$

原 active plane 只是完整解码后“该 plane 所有 digit 都为零”的事实。略过该 plane 不略过任何非零输入 bit。本条使用原 PackedVector / prepare，不重写这个判定。

当某一输入为全零、超过 exponent fast span，或原 packing 预算不足时，新 dot_pair 对两个完整输出依次调用原 exact_digit_simd128::dot。没有用其中一列的合法性代替另一列，也不改变 wide 的逐完整 significand product。

## 3. 两个部分和可以共享一次输入载入

固定原一个 block，长度 $r\le2048$，以及三个原 digit planes $a,b,c$。目标是两个独立整数

$$
P_b=\sum_{i=0}^{r-1}a_i b_i,\qquad
P_c=\sum_{i=0}^{r-1}a_i c_i.
$$

每个输出的任意子集部分和都满足

$$
\left|\sum_{i\in I}a_i b_i\right|
 \le2048(2^{20}-1)^2<2^{51}<2^{63},
\tag{522.2}
$$

$c$ 同理。故 signed int64 multiplication、累加和所有中间水平归并均不会溢出；两个输出之间不需要任何算术混合。

**引理522.1（scalar pair）。** scalar_pair 在每个 $i$ 将 $a_i$ 向 signed int64 扩展一次，分别乘已向 signed int64 扩展的 $b_i,c_i$，各自累加。返回准确的 $(P_b,P_c)$。

**证明。** 两个乘积的准确值绝对值小于 $2^{40}$，原 int32 值到 int64 的扩展准确。由 (522.2) 每一步 signed 加法也准确。两条循环不变量分别是已访问前缀的准确和；最终覆盖所有 $r$ 项。共享变量 av 只保同一个实际整数，不改变任一乘法。证毕。

**引理522.2（AVX2 pair）。** 在实际已支持 AVX2 的原 GNU x86 分支，avx2_pair 返回同样的两个准确整数。

**证明。** 每轮只有在 count-i≥8 时用 memcpy 从每个输入载入恰好8个 int32 字，故没有未对齐别名规则或尾部越界读取。原 _mm256_mul_epi32 对每个64位lane中的低32位作有符号乘法，覆盖位置0、2、4、6。对 av/bv/cv 作64位lane内部逻辑右移32位后，原位置1、3、5、7的完整 int32 bit pattern 位于低半部；该乘法指令仍将它解释为 signed int32，所以负的奇位也正确。没有把逻辑移位误当成有符号数值除法。

be/bo 和 ce/co 是四个独立64位累加向量。每个lane都是原乘积集合的一部分；(522.2) 同时约束每个lane和后续水平归并，因此 _mm256_add_epi64 的结果等于准确 signed 整数，不经过模溢出。原奇偶覆盖无遗漏或重复。剩余不足8项逐一以引理522.1方式累加。故两个返回值分别是全部 $r$ 项的准确和。证毕。

新 AVX2 函数限定 target("avx2") 且 noinline；基准 translation unit 没有新增全局 -mavx2 或 -march=native。选择沿原 R414 实际 CPU feature dispatch。无法编译/运行 AVX2 的原分支用完整 scalar；不要求某硬件作为科学前门。本条没有声称未来 runner 实际选择哪个后端。

## 4. 完整两个 dot 的字等价

**定理522.3。** 固定已经由原 prepare 返回的三个 PackedVector，长度相同；若新旧调用都完整返回且使用原相同的 binary128 字编码合同，则 dot_pair 的两个输出分别与原

$$
\operatorname{dot}(a,b),\qquad\operatorname{dot}(a,c)
$$

逐字相同。范围包括准确抵消、subnormal、负非零下溢成负零，以及原明确舍入溢出得到带符号 infinity。

**证明。**

若三个操作数中任一个全零或不 packed，源码直接依原顺序调用这两个原 dot，结论立即成立。

否则为每个输出建立其自己的原 ExactSum，base 分别是 $e_a+e_b$ 和 $e_a+e_c$。外循环依原 $\ell$，内循环依 $m$；右列层数不同时遍历两者最大值，但仅当该列该层实际存在且 active 时处理它。缺失层没有被读入内存。只有一个右层 active 时使用原 dispatch.partial；两个都 active 时用前述 pair reducer。

对每个输出，投影回自己的 active 层集合后，所加的每个准确整数部分和、移位 $20(\ell+m)$ 和每个原至多2048项block均与 (522.1) 相同。引理522.1–2保证这两个整数未受共享载入影响。两个 ExactSum 之间不存在共享可变状态，故完整准确整数正/负和分别等于各自原 dot。

最后逐个调用未经修改的 ExactSum.rounded。准确总和为零时沿原规则编码 +0；负的非零总和在原 subnormal quantization 舍入到零时保留负号；normal/subnormal交界、ties-to-even、完整113位significand和带符号溢出全部沿原 round_magnitude。没有先作 normal round 再二次 round，也没有中间 double 投影。相同准确整数、base和符号传入同一舍入函数，输出字完全相同。证毕。

这里不将 infinity 当成可接受 stage 值：原 DenseMap.check / finite_direction 保持，仍会按原合同处理非有限数学结果。非有限输入在原 decode 处失败，本文不声称 NaN payload、异常先后或失败路径逐字相同。

## 5. 全矩阵覆盖、原缓存和资源边界

新 multiply 的 shape/null/checked_product、全 row-major 输出分配、B列 prepare顺序、每次仅一个左行 prepare 以及原 packing reservation均保持原表达式：

$$
B_{\rm row}
=\min(12\,k\,\operatorname{sizeof}(\mathrm{int32}),\,67108864),
\qquad
B_{\rm col}=67108864-B_{\rm row}.
$$

这里67108864是**原 digit packing 预算**，不是全部进程内存上限；原 Word 列表、输出和其他矩阵照原合同另存。新代码只多同时持有第二个小 ExactSum，不分配第二份左行或矩阵 digit planes，不增 packing budget。不声称总内存字节数与旧调用完全相同；真实分配失败仍作为异常传播。

每行按照 $j=0,2,4,\ldots$ 取两个相邻列；若 $n$ 为奇数，最后一列调用原完整 dot。$n=1$ 全走原尾项，空维度沿原返回。每个 $(i,j)$ 恰好写一次，没有把未访问列补为零。

RightCache 保原全部 immutable packed columns，row_reserve、缓存构造、原左行 prepare以及 check/stat 位置不变；只将内部列循环换成相同两列/奇尾。所有 gram/momentum/L/flux 的真实矩阵形状和字均保持。没有以地址作为跨生命周期cache key，也没有复用另一个H或另一个stage的系数。

每个新整数block仍最多2048项。两个输出共同读取时，连续一段实际 reducer 可以形成**两个**原block，随后再次调用原 poll；不是声称原每一个 poll 的墙钟时刻相同。所有 poll 仍调用同一个 caller 的绝对时钟，没有私有新计时器或重置预算；外部进程timeout/owner合同不动。工作顺序改变可能令同一有限时间预算下完成的前缀不同，不保证旧运行的已访问范围、终止时刻或错误顺序。

若异常发生于一对中间，不返回半个 dot_pair。完整矩阵函数亦不会将半成品作为返回值；原 stage 只有全部requested columns和原全部RK step完成后才写该stage payload。当前部分工作与原错误仍由原stage ledger/stat承担，不把未返回矩阵当已完成。

原统计仍按**每个输出**登记 digit_products、integer_partial_sums 和 SIMD乘法数。共享一次左载入不使两个逻辑点积变成一个，不用计数减少冒减少了计算列。实际时间、trace字节和日志SHA不是定理522.3的对象。

## 6. 在实际全stage中的适用范围

当前 b183 operator 的小 H、point权、invN/frequency、原系数构造、root branches、原 nominal-factor triangular solve、C residual读回、全226状态及两mean、RK组合和port公式全未修改。只修改上述两个完整矩阵接口。

因此，固定同一真实 field/tape/输入和实际可返回的资源路径时，可按原系数形成、每个完整矩阵action、每个RHS方向以及每个RK阶段归纳：本条替换的数值点积字和由其继续形成的原数值字与 b183 相同。这是相对于**R414完整once-rounded dot算法**的命题，不是相对于R305旧顺序浮点图的字等价；R402/R414原有的 coefficient reassociation、nominal-factor误差和未付严格导数责任都保留。

不因新的数字核给出准确点积就宣称当前完整 stage 是准确 Frenet 导数、原 IEEE roundmap 的导数，或全338×112端点J已经通过FD。原 root policy、32×10 owner、fresh replay、所有224列与576段、原boundary/endpoint/audit和fullDN末门不变。没有任何实际 native/fullDN 接受结论。

## 7. 三个真实source view与原组件调用

[生成器](../computations/root_20261116_native128_paired_digit_source_views.py)和[完整计划](../notes/r522-native128-paired-digit-source-plan.json)给出全部 before/after/count 与输入/输出完整SHA。生成器只做文本、JSON和bytes/hash；不import、AST、compile或执行科学。

| Actions生成件 | B | 完整SHA256 |
|---|---:|---|
| geometry_20261116_native_paired_digit_operator_trace128.hpp | 29617 | 082d5a1fdd900071fb1cc008304c5a4c97bce92b173851bda1514ec1682eb7be |
| geometry_20261116_native_paired_digit_stage128.cpp | 12880 | 49a7e226eadc7748d5d2b3f94119c2e4dd7024348e6878c673e73b1a33db3b55 |
| geometry_20261116_live128_paired_digit_final_components.py | 33416 | 93ecdd833922f833bdb50a8f264bc5db1913f5ce16dbb0cb4f7fbc7d285070f1 |

Operator从原b183通过5个literal项形成；stage从R445的实际12691 B/eca87efc原件通过3项形成，只换include、schema和范围标记，原stage数字体保持。两头文件和stage引用都用真实新文件名，不把新字节冒作旧b183/eca。

组件先从32027 B/2369787d原件依已发表R515计划的原5项，准确形成32429 B/0a7f4721中间文本，再用本条15项形成真实新组件。R515每次physical查询的有限径向词共享继续使用其原adapter和原scope，未复制另一物理实现。19个明确public输入（含一份metadata计划）逐件完整读核；generator另单独绑本身。该19计数不是任意动态import闭包的证明，实际完整祖先closure仍由原caller提供，组件的原load_baseline/source_receipts继续实际检查。

组件CLI仍真实运行stages/boundary/endpoint/audit。stage compiler把真实新operator、新kernel、原R405/R414、原qualified recorded header、原hoisted header和真实新stage复制到同一原owned compiler目录；原R283prefix和原qualified geometry fallback保留。原compiler flags、300秒cap与process manager不改。receipt的新schema/文件名/返回key明确当前来源，实际compiler process仍由原lifecycle保存。receipt准备不等于编译已启动、返回或成功。

组件的当前schema、source SHA和stage report schema均同步；不将原0a7f或eca SHA传成新组件身份。boundary/endpoint此前组件必须按同一新source/完整source集合验证。原source、已有R518输出及正在运行的221均不替换。

## 8. 发表、执行与尚未支付

本条发表新kernel、generator、literal plan、本证明及完整接口；三份展开view仅在未来公开Actions同真实computations生成，不进Git，不上传raw或分块。没有新request、workflow、run、owner或cleanup marker。

完整调用方式及新source receipt见[接口](../notes/2026-11-16-native128-paired-digit-complete-component-interface.md)。它是已接实际组件主流程的source组合，尚未把R518的owner/assembly/pipeline/necessary reader注册为该新组件。后继若实际调用，必须完整接新tuple及实际编译binding；不能仅换一个文件名或伪用旧pin。

本条的收益事实只到“新reducer源码复用同一left plane载入/奇位移动，输出完整且字等价”。编译器也可能已消除旧代码的一部分重复，新增pair循环/两个ExactSum也有成本；没有任何实际时间或吞吐结论，不先建立独立benchmark/fixture/对拍门。完整证明成立即登记；原科学结果依真实后续run支付，当前README完成条件仍未满足。
