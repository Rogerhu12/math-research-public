# R515：同一次 physical128 查询内的有限径向模式词共享

**作者：OpenAI ChatGPT；日期：2026-11-16。**

**可信度：已证明（限本文明确的源码组合与条件等价命题）；新组件尚未编译或科学运行，未给出实际耗时、native/fullDN 接受或连续几何结论。**

## 1. 结论

当前 R501 的 live128 调用代码明确沿原 persistent128 owner、fresh replay、完整 stage/boundary/endpoint/audit 消费链接线；是否实际走到各阶段仍由该 run 的终态负责。本文在其中找到一个与 R471、R474、R494 不同的重复：原 `physical_jets` 对每个角点重新形成同一个径向模式词 `dp`，但该词只依赖本次已经形成的 state、RHS、geometry 和模式频率，完全不依赖角指标。

新增独立头文件只在**一次真实 physical 查询内部**保存已经由原表达式形成的有限 binary128 词。其余角表读取、`dP/dPt` 累加、完整右端、原 C 形成和求解、全部七列角 jet、曲率/holonomy/height、端点所有行均保留。非有限词不进入缓存，之后每次使用仍执行原表达式。缓存资格不是新接受条件。

同时交付实际 compiler-source adapter 及完整字面 source plan：原 R493 标量导出源先真实生成，随后三个明确的调用点类别改为新函数；完整 stage、boundary 和 forcing 数学不变。新组件 launcher 由原 2369787d 的完整文本按五项明确替换生成，使用新的 schema 与真实 source closure；没有复制一整套不变的 owner/solver 数学源。

本结论不改变正在运行的 211、215、221、222，不创建新请求。旧 R501 owner/pipeline 的固定组件 pin 仍是旧源；后继若把新组件接入 live fullDN，必须登记真实新组件及其上游调用身份，不能认为本文已替换当前 run。

## 2. 真实来源及已覆盖优化的分界

本次按已发表 R501 头 `f0c787340f29734e17c9428ba7588e2a58ae665e` 读取实际来源。当前 `geometry_20261116_live128_same_call_owner.py` 的 `execute` 明确调用原 owner C++ `7789007e`；其工程 view 将四组件指向 `geometry_20261116_live128_final_components.py` 的 `2369787d`。组件载入 `06a25776` scalar-source factory，并保留原 stage/physical/boundary 源与各自精度合同。[S1–S5]

| 路径 | 已有范围 | 本文是否改变 |
|---|---|---|
| persistent128 owner / fresh replay | 原 binary128 状态、32×10 原下降、实际 fresh replay | 否 |
| R402/R405/R414 stage | recorded literal 线性图、完整 dyadic 点积、SIMD/宽指数 fallback；全 576×224，含 226 行两均值 | 否 |
| 原 boundary112 | 原完整 QR/边界图、既有来源与残差读回 | 否 |
| 原 endpoint338×112 | 原全行对称差分加真实 trace first-slope 行；原门允许此混合响应 | 仅其每次 `cut_readout` 内的径向模式重复 |
| 独立 physical audit | 原节点、全部 query、所有角、每个 query 后原 advance | 仅每次 `physical_jets` 内同一重复 |
| R471 | 195 式有限 root 方向的合资格零 nonlinear flux 路径 | 不是本次对象 |
| R474/R494 | 原 dense linear 乘加中有限 A/T 资格下省去零系数项；后者用于 noJ caller | 本文没有再次做零 j 省略 |

原 `physical128.hpp` 的 `physical_jets` 仍是既有 C-based physical program，不因为共享有限词变成准确隐式根的径向导数。R491 已说明原混合响应与全解析 Jacobian 是不同责任；全解析不是原 fullDN 门。本文也不将 nominal factor 与 C、C 与 $F_e$ 等同。[S6；R491 §§3、5、8]

## 3. 原表达式和依赖

记本次调用中

$$
r_2=g.r\,g.r,\qquad r_3=r_2\,g.r,\qquad
\sigma=g.dr/g.r,\qquad k=\mathrm{geometry.k}.
$$

这些记号只复述原源码变量，不允许变更其形成括号。对每个模式 $j$，原词由下面完整字面表达式形成：

```cpp
-p.frequency[j]*r3/(p.sq2*g.w)
    *(rhs[j]+(3*sigma-k)*state[j])
```

它的运算图是

$$
\operatorname{fl}\!\left(
 \operatorname{fl}\!\left(
   \operatorname{fl}((-m_j)r_3)/
   \operatorname{fl}(s_2w)
 \right)
 \operatorname{fl}\!\left(
   f_j+\operatorname{fl}(
       \operatorname{fl}(\operatorname{fl}(3\sigma)-k)y_j)
 \right)
\right).
\tag{515.1}
$$

这里 $\operatorname{fl}$ 表示原 Q/binary128 运算；式子用来标记同一图，并未把它改成准确实除法、融合乘加或新的舍入方式。实际实现保留原 C++ 表达式本身，包括一元负号、乘除左结合和括号。原 `r3`、`sigma`、`rhs` 的形成也不移动到另一个 field。[S6]

对固定本次调用，`p.frequency[j]`、`r3`、`p.sq2`、`g.w`、`rhs[j]`、`sigma`、`k`、`state[j]` 全部不随 $n$ 改变。源码中改变的是 `right`、`Tdot` 和局部累加器；这些不反写上述输入。OpenMP audit 使用每个 stage 自己的 y/field；新增缓存不是 static、全局表或地址键缓存。[S6–S8]

原角向运算继续逐字执行：

```cpp
Q dP=0,dPt=0;
for(int j=0;j<p.M;++j){
    // 原或已形成的同词 dp
    dP+=dp*sn[j];
    dPt+=p.frequency[j]*dp*cs[j+1];
}
```

随后仍有完整 $n=0,\ldots,N-1$、$j=0,\ldots,J-1$ 的
`right[j]-=dq*cs[j]/p.N`。没有使用三角正交、理想 cosine 乘积恒等式、删角点或移动 $1/N$。[S6]

## 4. 实现

独立头文件提供两个同类型函数：

- `physical128::physical_jets_radial_mode_cache`；
- `physical128::cut_readout_radial_mode_cache`。

它包含完整、未修改的原 `physical128.hpp`，复用原 `Problem/PhysicalPacket/FieldTape/Jets/CutReadout`。新 physical 函数与原函数的数值正文仅有以下变化：

1. 增加本次调用私有的 $M$ 个 Q 词及 $M$ 个 ready 字节；
2. 原 `dp` 所在位置，ready 为真时载入已存 Q；否则执行原完整表达式；
3. 只有 `finiteq(dp)` 为真时存词并置 ready。

没有预先计算未访问的 $j$；首次实际访问仍处在原第一个角的原 j 循环位置。每个角原 `time_check` 仍在原位置，所有后续算术语句和检查逐字保留。新 cut 函数与原 cut 函数只改名称及其 physical 函数调用；原 cut 缩放、完整 root capture、338 行和两均值表达式保留。

新增缓存最多占 $M$ 个 Q 与 $M$ 个 ready 字节的数据区及容器管理空间；不是 $N\times M$ 表，也没有跨 query 保留。函数退出、原异常或资源中止都会终止该缓存的有效期。缓存分配失败不被捕获后重新运行旧科学程序；沿原调用者真实错误路径报告。

## 5. 条件逐词等价

**命题 515.1。** 在原有效 shape、同一次不可变输入、原 Q 类型、同一原舍入环境及原未融合/未 fast-math 的运算合同下，对实际到达的每个角/模式位置，新增程序提供给原 `dP/dPt` 两条语句的有限 `dp` 词与原程序相同。对未缓存的非有限词仍执行原表达式，不因缓存新增接受或拒绝。

**证明。** 固定 $j$。在首次访问前 ready 为假；新程序在原位置执行原表达式，得到同一 Q 词。若词非有限，则不置 ready，下一次访问仍走同一原表达式。若词有限，复制到同类型 Q 槽后置 ready。该词没有经 decimal、binary64、整数转码或重新算术形成。此后输入和舍入环境不变，原程序重新执行同一表达式会返回相同有限 Q；新程序直接取这个已经形成的词。因此对各 $n$ 归纳成立。各个 $j$ 的槽独立。证毕。

### 5.1 零和次正规

`finiteq` 接受 $+0$、$-0$ 和有限次正规词。存储操作是 Q 到 Q 的值复制；新代码没有 `+0+dp`、`abs` 或强制正零，因此保留原符号零。ready 必须在赋值后才变真；初始化的零槽不会被误当成已形成的结果。原表达式若发生下溢，缓存的是其原最终舍入词，未截去尾数或另做一次精度转换。

本结论不复用 R473 的零项累加命题：这里没有省略 `dp*sn` 或 `m*dp*cs`，两个可能含有有符号零的原乘加仍全部执行。

### 5.2 累加和后续程序

固定每个角，两个累加器仍从原 $+0$ 开始，模式访问顺序与每个乘加括号相同。由命题 515.1 逐 j 归纳，有限的 `dP/dPt` 词相同；继而 `Tdot[n]`、`dq` 和每条 right 更新相同。再对 n 归纳，原完整 right 和 C 输入相同。

C 仍由原 `root_matrix` 形成，`spd_solve` 及全部 `C*Ldot-right` 读回未改变。第二个角循环、sqrt/hypot、height、所有极值和 holonomy 的原算术与顺序保留，故同一完成调用的原有限返回字段相同。cut 调用只替换该等价子程序，全部原 cut 行同样保留。

### 5.3 非有限、异常和时间边界

非有限 dp 不缓存，所以没有“输入有限便假设所有中间有限”的漏洞。原 arithmetic/finite/domain 检查仍决定返回或异常；新代码不捕获资源异常、不重开预算、不把任何异常转换为缓存资格拒绝。

这里不声明 NaN payload、外部观察的 sticky exception flag/errno 次数、内存分配轨迹或 wall-clock 分支逐字相同。原已读调用链没有把重复形成 dp 的异常次数作为数学判定量；本文只保其有限数值词与原失败分类责任。若资源钟在不同位置耗尽，真实未完成范围仍按原 query/advance/column 地址记录，不能从条件等价补成完成。

原 actual compiler flags 保留 `-std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math`，并使用原 `-lquadmath`。原 `action_guard` 的 round-to-nearest/字节序约束保留；没有引入一个额外数值对拍、fixture 或接受门。[S7–S9]

## 6. 完整科学范围保持

端点原程序首先对实际 node 求 base cut；随后对所有 112 个实际列分别求 plus 和 minus cut，每次均有自己的新缓存。没有把 base 的词借给扰动点。原步长、完整338行对称差分、原 first-slope trace/RHS 列和两均值组装均不变。[S8]

独立 audit 对所有 576 个实际 stage 的原完整 query schedule 逐点捕获 field、计算 jets/metric、写全部角和状态，之后执行该 query 的每个原 advance。缓存只替换其中 physical 子调用；它既不复用 owner/replay 的 field，也不移除 `capture_field`、root trace 或 advance。未访 query 与已读 query 后未完成 advance 必须继续分别报告。[S7–S8]

stage 源 `eca87efc`、SIMD header `b183eeec`、完整数字核及 nominal-factor/完整224列传播不变；boundary `c218f128` 也未改。本实现并不把 endpoint/audit 的 C-based 诊断错误解释成实际 finite-root 径向导数的完整证明。

## 7. 实际 source 接线

新 compiler adapter 的 API 与原 R493 qualifier 一致：

`copy_named_source`、`forward_lines`、`prepare_compile`、`wrapped_base_process`。

对于原 physical C++ 编译请求，它先调用原 `prepare_compile`，得到尚未编译的完整 R493 scalar-export 源（19958 B / `5f6b2d3c…`）；验证完整字节后只执行三种替换：

| 类别 | 精确次数 | 变化 |
|---|---:|---|
| physical include | 1 | 包含新小头；它再包含原完整头 |
| 原 cut 调用 | 3 | base、plus、minus 改调新同类型 cut |
| audit physical 调用 | 1 | 改调新同类型 physical |

原 R493 的四处实际 scalar-word 导出均保留，不能退回没有这些 live words 的 a090 输入。新 translation unit 为20048 B / `c0364bcd…`。原 header 与 shared header 同新小头实际复制到当前独占 compiler 目录；原生成 R283 prefix 保留。编译 argv 只改一个源路径，flags、输出 executable、原进程管理器和预算参数不变。

旧 factory 的收据作为 `upstream_prepared_but_not_compiled_binding` 保留，明确其中原执行标签仅是准备层祖先；真正 compiler 输入由新 `actual_executed_source` 与完整命令记录。不能把新 CPP 冒成旧 `5f6b…`，也不能声称旧中间源已经执行。

非 physical 的 stage/boundary 编译和普通进程调用继续委托原 factory；原进程管理器每次只调用一次，不捕获失败重试。新 component source view 加入旧/新完整依赖，修改真实 qualifier 和组件 schema；完整四组件 CLI、同状态输入、原前件验证、全部 flags/失败/未访、局部必要回复及临时全文责任保留。

这只是源码组合条件；现有 live owner 固定 tuple 尚未修改。将来接入新 owner/pipeline 时还须把新组件源/schema 与必要 readback 的真实 compiler receipt 一起登记。那是实际来源接线，不是对已完成数学另加独审或执行前门。

## 8. 能减少什么，尚未证明什么

若本次所有模式 dp 均有限且全部 N 角完成，原表达式在源码层出现 $MN$ 次实际循环访问，新函数形成 M 次、复用 $M(N-1)$ 次。角表乘加仍是完整 $MN$；没有将原物理问题降维。若前缀中止，只对实际到达的位置作上述条件陈述。

没有科学运行，所以没有命中计数、wall time、吞吐倍数或 compiler 是否原已自动做同样消除的实证。尤其不能从 $N$ 次重复可共享推出整条576×224链提速 $N$ 倍。原 root/factor、完整 dense/FFT、boundary、state replay 与传输成本都仍存在。

可以直接登记的新结果是：一个不依赖零解、不依赖理想三角恒等式、保原精度与全部 query 的局部有限词共享实现，及其真实编译接点。没有用它预付215、221或未来 native/fullDN 成功，更没有支付准确连续 C²/metric/reach/held。

## 9. 来源与阅读范围

下表是本次取得完整正文并按本文调用点阅读的源码身份。物理头、两处新函数及其真实调用/编译接点已逐段阅读；owner/response assembly 取用的是实际来源、调用及返回范围，不宣称逐函数复核其全部其它分支。blob 文本 UTF-8 字节哈希不是科学日志或运行输出。

| 标识 | 来源 | 字节 / SHA-256 |
|---|---|---|
| S1 | [live128_same_call_owner](../computations/geometry_20261116_live128_same_call_owner.py) | 18850 / 5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5 |
| S2 | [live128_final_components](../computations/geometry_20261116_live128_final_components.py) | 32027 / 2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866 |
| S3 | [live_scalar_source](../computations/geometry_20261116_native128_live_scalar_source.py) | 15897 / 06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b |
| S4 | [persistent128](../computations/geometry_20261115_native_persistent128.cpp) | 22364 / 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd |
| S5 | [live128_response_assembly](../computations/geometry_20261116_live128_response_assembly.py) | 28584 / 08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb |
| S6 | [physical128](../computations/geometry_20261115_native_physical128.hpp) | 12683 / 4b0569a245147e346149d462d974a80cac853bcf9d5abf13700b743acd33af35 |
| S7 | [shared_trace128](../computations/geometry_20261115_native_shared_trace128.hpp) | 13605 / bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b |
| S8 | [physical_final128](../computations/geometry_20261115_native_physical_final128.cpp) | 18055 / a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 |
| S9 | [native_final128_components](../computations/geometry_20261115_native_final128_components.py) | 25877 / ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045 |
| S10 | [qualified_json_components_v2](../computations/geometry_20261115_native128_qualified_json_components_v2.py) | 17484 / 5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf |
| S11 | [native_trace_variation128](../computations/geometry_20261115_native_trace_variation128.cpp) | 34622 / 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d |
| S12 | [native_primal128](../computations/geometry_20261115_native_primal128.cpp) | 23890 / 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d |
| S13 | [simd_digit_operator_trace128](../computations/geometry_20261115_native_simd_digit_operator_trace128.hpp) | 29035 / b183eeecf4f3009bf202dd0f465c8d4fdb17d8cc0ce14bb90d1ed5e6ecf485ac |
| S14 | [simd_stats_qualified_stage128](../computations/geometry_20261116_native_simd_stats_qualified_stage128.cpp) | 12691 / eca87efc267d692e401d2ed49904d3d8e73cc16cad12eb3ae24042328f81025e |

R491 的主门结论见已刊 commit `abeed0e09fc341a90c56ddd5f51f96e373f7f4fd`；其 original mixed-response 责任未因本文改变。R515新增源码、完整 source plan 及实际生成视图身份见伴随接口。源码派生仅做文本/JSON/字节核对，没有 import、AST、compile、fixture、科学算术或新运行。
