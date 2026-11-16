# R583 — 完整原内循环的一次实际舍入模式观察与八类乘积的逐字等价

维护：ChatGPT /root（AI），2026-11-16。分类：**已证明的有条件源码等价、完整来源构造及实际安装接口**。本条不含新的科学运行、速度测量、非零高度接受或几何证书。

## 1. 结论及确切条件

在 R572 的实际 primal/trace 源码上，只把四个完整内循环中每个 R564 乘积的实际舍入模式观察移到该循环入口，作为显式整数参数传入同一完整乘积核。条件是：从入口观察起到完整内循环结束，**执行该循环的实际线程的舍入模式，以及观察该模式的返回值，保持不变**。每次进入循环重新观察；不跨角度、调用、root、H 或线程缓存。

在相同实际输入字、同一原环境/布局分支和上述条件下，R583 与 R572 的每个共同执行到的乘积返回同一 Q 字，进入同一原统计分支并更新同一完整字段；每个加法仍在同一原顺序和同一实际模式下进行。因此共同完成的每个原循环结果相同。继续沿原控制流归纳，可得共同执行的有限数值前缀内相同的原 root 状态、阈值比较和试步选择。**运行时间、资源截止点、浮点异常标志、整个运行是否完成不在该等价范围内。**

条件排除循环途中由不在本源码契约内的外部/异步干预改变线程模式，或使模式观察不稳定的情形。没有新增“必须 nearest”的科学接受门，也不调用 fesetround。观察到任一非 FE_TONEAREST 返回值，包括失败值时，每个实际乘积仍走原 Q 乘法的 rounding fallback。实际模式不是根据编译参数推定的常量。

四个完整实际循环体和所调用的 R564/R561 算术辅助函数没有模式设置器或用户回调。完整冻结源的检查说明条件在源码内的来源，不声称排除外部信号处理器或运行时干预。原 time_check 位置未改；所改内循环内没有 time_check、sqrt 或任意调用者回调。循环外原算术、根域判断和资源检查照原源码执行。

本条接续 [R535](R535-original128-local-finite-root-words-and-real-compiler-hook.md)、[R550](R550-same-root-accepted-complete-evaluation-reuse.md)、[R561](R561-exact-normal-dyadic-average-and-original-first-products.md)、[R564](R564-exact-binary64-factor-products-and-complete-integer-rounding.md)、[R572](R572-exact-root-synthesis-products-and-original-sum-order.md)，不扩大祖先命题的其他条件。

## 2. 完整文件与源身份

以下均为作者源码/方案或由明确字面变换定义的完整源码视图，不是科学输出。字节数按完整 UTF-8 文件，SHA 为 SHA256。方案保存全部 old/new 文本及唯一逆变换。

| 文件 | 字节 | SHA256 | 保存职责 |
|---|---:|---|---|
| computations/root_20261116_loop_rounding_observation.hpp | 4657 | 0bc58ed32c05efc5bd2833ef0f0faf61b1093db2676f7bc993198318b4acef9c | 本次作者文件 |
| computations/root_20261116_loop_rounding_observation.py | 22648 | 0b769cc0558758ce2415c0374c3286bb8433d377286259821e9e588e5550635e | 本次作者文件 |
| notes/R583-loop-rounding-observation-complete-source-plan.json | 24218 | 9e1ac431926c76e0e77858695e2d1772e07eb58dcaba1211f2c9eca7328af0f1 | 本次作者文件 |
| root_20261116_loop_rounding_observation_primal128.cpp | 28149 | dc8a2394379d6d8ca4187aff2979b5a31b17d07af39e5b566224bab26eeebe76 | Actions内生成/安装的完整源视图；展开文件不进main |
| root_20261116_loop_rounding_observation_trace128.cpp | 36388 | 37e54b0483727dc1c579474239764b1c2beca0af7f0dd64a04911ef5cdd0e4c0 | Actions内生成/安装的完整源视图；展开文件不进main |
| original-compile-owner-R583-function.txt | 8626 | 5783fbb213a5a7faf7bf33d606979b16ac9755aef19005aa3b36f79de52585ef | Actions内生成/安装的完整源视图；展开文件不进main |

本次 main 保存三个作者文件和本文。两个 C++ 展开视图及完整 compile_owner 视图仅由方案在公开 Actions 实际 computations 目录形成；预先声明的身份不代替实际形成、编译、执行回执。detached 小作者源对象供并行作者完整交接，不作为科学父、运行结果或已在 main 发表的证明。

完整方案：[R583-loop-rounding-observation-complete-source-plan.json](../notes/R583-loop-rounding-observation-complete-source-plan.json)。适配器：[root_20261116_loop_rounding_observation.py](../computations/root_20261116_loop_rounding_observation.py)。实际核：[root_20261116_loop_rounding_observation.hpp](../computations/root_20261116_loop_rounding_observation.hpp)。

| 实际父对象 | 字节 | SHA256 |
|---|---:|---|
| R572 adapter | 20999 | cdc734c9b704ffa77f46b32054cff1dbae4df10e91f6be66f4ddeb53a4237fcf |
| R572 plan | 14796 | 25e8a39b5c8beaaa0b8b049d79f0e5d278622aa4f62e156fcd50cfceb50f1a64 |
| R572 header | 2380 | a715367b67448c85c6ff180ad24f915334f188751df5d3a2adca5ed3535e5f9a |
| R572 primal | 27592 | 8952e5a65a04e918d00ef990a1355ba3c1912284dfc2c482d8f861aa896b660a |
| R572 trace | 36252 | 138c6aaaba86628befd71b398bd2d393e661cb4abdab7781d6ef1ba0bebe05bb |
| 原 R564 header | 10146 | bb4dfb08db7c4593afd93addb804a20876e0bb1facb1bc7e8a7e3f9aaeb40cc1 |
| 原 persistent owner Python | 43371 | 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322 |
| 原 persistent CPP | 22364 | 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd |
| 原 owner 内完整 compile_owner | 3860 | be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d |

五个祖先 plan 在当前方案逐个固定，不能仅核最外层父计划：

| plan | 字节 | SHA256 |
|---|---:|---|
| R535-native-root-finite-words-complete-source-plan.json | 10232 | f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b |
| R550-accepted-root-evaluation-complete-source-plan.json | 12303 | 14b5c02071359276be2988dc273d6864df3d61e728df10df5b1bddc498134457 |
| R561-normal-dyadic-average-complete-source-plan.json | 13708 | 5667d987ea5b7387bb0c4f6c61d86cd9ea94035299da91d3c7889fb1cde5f5a7 |
| R564-exact-lifted-factor-product-complete-source-plan.json | 13514 | cd4c90cbfc9e48acdd06a692885121627355df477955104981713d248cafca4a |
| R572-exact-root-synthesis-products-complete-source-plan.json | 14796 | 25e8a39b5c8beaaa0b8b049d79f0e5d278622aa4f62e156fcd50cfceb50f1a64 |

## 3. 完整核的两个唯一变换

原完整 R564 函数3959B/SHA 7a090c6d559aaceffaf61d5bbb52f5b95489a79a6a34cbff50e645406b47f51d；变换后完整核4069B/SHA 395abbd9ddf2eeba47d1bd0912dbc7e89d8c597e648cb00342c72f76a66413d0。完整函数体全部收入方案，不以几个查找片段替代。

第一项把

~~~cpp
static inline Q r564_exact_lifted_factor_product(Q left,Q factor,
    R564ProductPathStats &s,int angle,int index){
~~~

换为

~~~cpp
static inline Q r583_exact_lifted_factor_product_at_loop_mode(Q left,Q factor,
    R564ProductPathStats &s,int angle,int index,int observed_rounding){
~~~

第二项把原观察注释和

~~~cpp
if(std::fegetround()!=FE_TONEAREST){
~~~

换为声明循环入口来源的注释和

~~~cpp
if(observed_rounding!=FE_TONEAREST){
~~~

布局分支仍在这个条件之前。其他全部字节，包括原 lambda、整数乘积、条件次序、统计更新、fallback 和返回式，均保持。新 header 只是完整新核加声明的前后包装。准备器在实际完整 R564 header 验证原完整核恰出现一次，作两替换，逐项逆回整个原函数并核全字节/SHA；再验证 wrapper+新核恰等于磁盘上的完整新 header。

没有把一般 Q×Q 缩成 binary64，也没有从数学三角函数值重造因子。每次 left/factor 仍是原实际 Q 输入字；factor 不满足至多53位的条件时，完整原 fallback 保留。

## 4. 模式观察引理及证明

记具体循环入口返回整数 r。取循环中任一实际乘积，其原模式观察若发生，返回同一 r。设对应调用前 left/factor、统计状态、角度和索引一致。

若原编译/运行布局不满足，两核在同一 layout 检查处走 original-layout-fallback，更新同一字段并作同一 left*factor。原核此时没有模式观察，新循环入口已有一次。故这里只证明数值和原统计等价，不能声称所有布局上的模式观察次数都减少，也不声称整个环境可观察行为等价。

若布局满足且 r≠FE_TONEAREST，原、新比较同为真，两核更新 fallback_rounding、original_multiply 和同一 last_phase，在实际位置作 left*factor。线程模式在循环内不变，故对应原 Q 乘法处在相同模式。观察失败值也在此情形，不被伪装成 nearest。

若布局满足且 r=FE_TONEAREST，两比较同为假；余下完整函数逐字相同。因此相同输入字产生相同指数和有限性/零/normal/factor 精度判断、相同整数乘积、舍入关系、进位和输出字，或相同原 fallback。统计亦相同。三种情形穷尽。证毕。

引理保持原布局优先级，不删掉非 nearest/未知观察值的完整 fallback；其假设写在全核之前，不只在正常样例上讨论。

## 5. 保留的原精确乘积

R564 完整证明继续适用。这里明确“模式观察复用”没有变成“乘积复用”。

对 nearest-even 下合格的正常有限输入，Q 的有效整数为 a，因子有效整数为 b，2^112≤a<2^113，2^52≤b<2^53。写 a=a0+2^64 a1；原 unsigned __int128 运算形成 p0=a0b、high=a1b+floor(p0/2^64)，low 为 p0 低64位。完整精确积为 high·2^64+low，并非先截 a 到 binary64。a1<2^49，high 位宽留在原无符号128范围内。

原 lead 从积最高位决定，discard=52+lead。quotient 由 high/low 拼出，余数是 low 的低 discard 位；discard仅52或53，原 uint64_t 移位范围合法。remainder 大于 half，或相等且 quotient 为奇数时进位，恰为 nearest-even。进到2^113时原右移并增指数。符号按原两个输入符号异或。

原 result-range 在舍入前和舍入后各检查；左/右非有限、subnormal、因子超过53位、结果范围不合格等完整原 Q fallback 均保。有限 signed-zero 检查仍在两个非有限检查之后，不会把0×无穷偷换为有限零。原分支统计一字不动。

不声称整数路径在其他模式下形成相同定向舍入：其他模式直接用原 fallback。本条不保证异常标志、errno、信号、计时行为等价。

## 6. 四个完整循环与八类路径

primal 在完整 R572 源上仅五项唯一变换：新增 header include，以及下列四个完整原循环片段。全部 old/new 文本包括原紧邻上下文，均保在 plan；全28149B生成后逐项逆回完整27592B父源。

| 实际函数及完整索引范围 | 新模式变量 | 原实际统计路径 |
|---|---|---|
| root_evaluate，j=0,…,M−1 | r583_synthesis_rounding | fixed_fallback_P、fixed_fallback_Pt、L、evaluation_u_words、evaluation_u_fallback |
| root_evaluate，i=0,…,J−1 | r583_residual_rounding | root_residual |
| root_matrix，k=0,…,2M | r583_gram_rounding | root_gram |
| rhs，j=0,…,M−1 | r583_flux_rounding | primal_flux |

第一循环只有 fixed_used 为假才执行 P/Pt 两原乘积；L 总在；U 的 words/fallback 互斥。“八类路径”是五个 synthesis 统计对象加三个原平均统计对象，不是每个 j 同时执行五个乘法。

P 仍为 momentum[j] 与 sn[j]，Pt 仍为 pt[j+1] 与 cs[j+1]，L 仍为 L[j+1] 与 cs[j+1]，U words 仍为 u_words[j] 与 sn[j]；U fallback 的 left 仍在原位置按原括号形成 (-m*L[j+1]+(m*m-1)*momentum[j])。这些 left 内部算术、cs/sn/frequency 的来源及访问均未改。

残差仍先形成 quad*cs[i] 的实际第一乘积，再交原 r561_average_actual_product，按原次序加到 result.residual[i]。Gram 仍由 value、gc[k] 形成第一乘积，再按原第二乘积与顺序加到 bm[k]；flux 同理保留 f、sn[j]、原第二乘积和 flux[j] 累加。

从循环入口相同状态按索引归纳：left/factor 同字；第4节给出第一乘积同字；如有 R561，其输入、average、实际模式都相同，故同字；原 += 的累加器、被加数、模式也相同，故下一状态相同。第一循环的分支依赖同一原状态，归纳仍成立。这里没有使用实数结合律重排浮点求和。

在 layout 满足的原源路径，synthesis 每次进入原有2M次或4M次乘积模式观察，新源一次；residual 的 J 次、Gram 的2M+1次、flux 的 M 次各由一次代替。只这是源位置的调用数量关系，R561 自己的资格检查/模式观察保持。没有测量程序速度，不能推断会多完成多少角度、方向或高度。unsupported layout 上原核本来就跳过模式读取，不能套用上述减少关系。

## 7. 完整统计与共同有限前缀

原 R564ProductPathStats 定义、begin、join、打印器与 R572 组合 header 保持。八个实际路径各自的17计数完整保留：

~~~text
terms, exact_normal, exact_signed_zero, original_multiply,
fallback_layout, fallback_rounding, fallback_left_nonfinite,
fallback_factor_nonfinite, fallback_left_subnormal,
fallback_factor_subnormal, fallback_factor_precision,
fallback_result_range, rounding_below_half, rounding_exact_half,
rounding_above_half, rounded_up, carry_to_next_exponent
~~~

完整 last 字段亦保：last_present、last_integer_rounding_formed、last_rounded_up、last_carry、last_phase、last_relation、last_angle、last_index、last_left_exponent、last_factor_exponent、last_result_exponent、last_discard。begin 在原角度/索引清理同一字段；join 遍历和覆盖规则不变。不以总数或一个末phase代替全统计。

共同执行前缀内，模式引理给出所有这些字段逐项相同。若运行因耗时变化走到更远调用，总量自然可不同；不能比较不同前缀而声称计数相同。资源截止位置、未访数量、子进程退出和清理都须由实际运行分别记录，旧运行未返数值不能补新运行。

trace 只作两项变换：include 改为完整 R583 primal；把原 included_R572_primal_cpp_sha256 改作 ancestor 名称并加入当前 R583 primal 真 SHA。原方向算术正文逐字保留。它调用新 primal 的值等价遵守上述条件；“方向算术未改”不意味着 IEEE 舍入函数的实分析导数。原方向方程、FD、root域与审计职责保持。

R535 fixed/U 字形成、R550 同次接受 root 完整 evaluation 复用、R561 第二乘积选择均未改。旧字段 original_R564_three_angular_average_products_unchanged 在本链中表示原三个乘积的数值/累加顺序保持；实际调用函数与模式观察源已改。新回执显式写 per_product_fegetround_call_retained=False、numerical_equivalence_requires_constant_actual_thread_mode_within_each_loop=True，并绑定完整新源，不能借旧字段说被调函数逐字不变。

## 8. 完整 source-only 祖先链

模块 require_actions 要求 GITHUB_ACTIONS=true、GITHUB_REPOSITORY 为 Rogerhu12/math-research-public（大小写归一后比较），且 GITHUB_REPOSITORY/RUN_ID/RUN_ATTEMPT/SHA 四项齐备。执行、项目导入、来源准备、编译、算术仅在公开仓库自身 Actions。

prepare_sources 接受六 plan，顺序为 R583、R572、R564、R561、R550、R535。当前与五父 plan 各核完整字节/SHA。来源文件须是实际同 computations 目录的普通文件而非 symlink，basename不得逃逸。plan 可在 notes，其实际完整路径入回执。

R583 调用固定实际 R572.prepare_sources，沿 R564→R561→R550→R535 仅准备源；不调用任何祖先 installer。之后核实际 run/source root、完整adapter/plan/header/生成源/原源回执、source_preparation_complete=True、compiler_completed=False、scientific_evaluation_performed_by_preparation=False，以及全部逆变换和未覆盖原源条件。

checked_ancestry 保存整个 actual_R572_source_binding，解出各层 binding/plan，逐项核 R572 实际父源、输出、五个 header，且五个实际 source_plan 收据与五个传入计划完全对应。不能用一个“祖先成功”布尔值代替整链。

当前两源按完整字面变换形成；已有目标仅当全身份相同才复用，否则失败；新目标用 xb。binding 收入当前两个父源/输出、六 header、原 owner/CPP、当前adapter的完整身份，original/generated分开，最后才置准备完成。不由准备成功推断编译或数学接受。

## 9. 一次实际 owner 安装

install_owner_compiler(owner_scope, source_binding) 接收原 owner.main 实际使用的 globals；要求 compile_owner 与 main 的 __globals__ 正为该对象，实际 HERE/binding目录相同，原 CPP/ORIGINAL_CPP/TRACE_CPP 名称与全部原 PINS 正确，且六个 _R583/_R572/_R564/_R561/_R550/_R535_SOURCE_BINDING 都未安装。只直接装 R583 一次。

安装重新核完整 plan/ancestry/header/两个输出；从原43371B owner按唯一函数起点及下一def提取完整3860B compile_owner，作声明的四个唯一替换，逆回整个原函数，再核完整新8626B。原 owner 文件不覆盖。

新增编译依赖24件：六 header、六层 primal/trace 十二件、六 adapter。原 owner、CPP、最初primal/trace 等原 PINS 仍留；24不是全部系统库/完整传递依赖的数量。只扩展实际 PINS，把 ORIGINAL_CPP/TRACE_CPP 指向当前两视图，存完整当前 binding，再在真实 globals 定义这个编译函数。原 main/solve/replay/时钟/限额/协议保原函数。

实际 main 调用时再次核24项依赖并走原编译流程。persistent CPP不改；原 trace 数值前缀和完整226观察插入仍按原源执行，原四个 evaluate→evaluate_full 文字变化及整 evaluation 逆回不改。因为当前整体源已变化，回执明确 frozen_R283_numerical_prefix_is_byte_identical=False；不能冒称新前缀与最初R283全字相同。

原编译参数完整保：

~~~text
g++ -std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math
    -I <work> -I <actual-computations>
    <actual-computations>/geometry_20261115_native_persistent128.cpp
    -o <work>/persistent128-owner -lquadmath
~~~

真实 work/computations 由原运行分配。实际 compile.stdout.log/stderr.log、生成include、executable、returncode、command和整来源链入原编译回执；source_preparation_alone_is_not_compilation=True，模式条件、六层源与原 CPP/observer 保持均显式记录。

安装回执写 actual_compile_not_yet_called=True 与 no_scientific_success_inferred_from_installation=True，区别于后续真实编译。不能把 exec 定义函数视为编译成功，更不能本地执行以代公开Actions证据。

## 10. 全 CLI 与失败语义

下面仅在公开 Actions 内、以本课题目录为工作目录执行：

~~~sh
python3 computations/root_20261116_loop_rounding_observation.py \
  --source-plan notes/R583-loop-rounding-observation-complete-source-plan.json \
  --synthesis-source-plan notes/R572-exact-root-synthesis-products-complete-source-plan.json \
  --product-source-plan notes/R564-exact-lifted-factor-product-complete-source-plan.json \
  --average-source-plan notes/R561-normal-dyadic-average-complete-source-plan.json \
  --reuse-source-plan notes/R550-accepted-root-evaluation-complete-source-plan.json \
  --word-source-plan notes/R535-native-root-finite-words-complete-source-plan.json \
  --binding-out <new-actual-work>/R583-source-binding.json
~~~

输出父目录由原caller建立，xb不覆盖回执。CLI仅准备来源，不装owner、不编译、不启动科学。真实caller取本次完整binding，向原owner真实globals调用install_owner_compiler一次，再由原main走编译与科学；不能只打印binding后继续用旧R572编译器。

plan schema 为 R583-loop-rounding-observation-complete-source-plan-v1，binding schema 为 R583-loop-rounding-observation-source-binding-v1。正常准备返回0，打印 R583_SOURCE_PREPARATION 后的全JSON；准备异常返回2，保完整type/message/traceback及partial_sources。

partial_source_state逐一保留两个预期新输出完整身份、存在性、实际完整身份或错误，再调用原R572完整partial_source_state保全部祖先形成状态。不重新生成失败来源，不重跑科学，不补未形成字段。读取异常另存read_errors。

完整JSON以sort_keys=True、ensure_ascii=True、紧凑分隔、allow_nan=False，加LF形成ASCII全体并写出。大于90000B只报实际bytes/SHA、complete_necessary_body_returned=False、source_child_returncode，返回70；identity不是正文，不能恢复未返字段。本组件不承诺binding必小于90000。真实request244须纳入原完整必要回读；只对完整可逆已知关系使用压缩，未知R583字段保全，禁止截断/丢字段/提高限制。

最终序列化、写文件或输出的其他异常保真实进程异常，不虚构成功包装。真实科学caller的全环境、末阶段错误、quiet、清理、退出码仍必须实际回读。

## 11. 未动的数学门、资源门和作者检查边界

原M112/N2048、699×453、3active+109core、338×112/全部未知量、双mean、每模型fresh W/J、全H、FD/RMS/域/BC/merit/final fresh J+audit不变。原full576/full224/local226、root阈值/试步、native2e−9、replay/fullDN完整职责保留。本源码等价不支付数值接受或误差界。

R583不改原owner6000、总19200、replay1200、stage8000、boundary600、endpoint600、audit1800、readback120或原内存策略。R593/R594独立证明同一总钟内owner12000；R584244若采用，须在真实请求/源链明确声明，不能说R583本身扩大了资源，也不能把12000当原6000。

本次只作完整源阅读、纸证、唯一字面变换和逆变换、JSON与字节/SHA管理；无本地项目导入、AST、compile、test、fixture、科学求值或测速。完成证明/源后立即独立发布，不等独审或机械重跑。后续真实运行支付自身数学目标，不成为本结论额外发布门。

旧失败/未返/未访照旧保。225的534/576不补576；224零H成功和正H内部一次试步不称正H接受；超过90000的旧正文SHA不代完整值。本条未形成非零112/338/450父解。

## 12. 继续责任

R584/request244由exact_refinement接本组件，在R594/request248原初始化与19200总钟/owner12000基线上构造完整真实caller：准备六层源，R583只装一次，worker/client/fullDN实际对象和完整来源一致，原63输入及全部祖先不丢。独立写完即发表并唯一正式派发，R585指定exact_refinement唯一终态读者。未来run/job不预填已存在，不混request242三参数初猜。

几何线继续同一实际保存C_lit/Q、物理/增广RHS各自controls、有限DFT及严格余项、真实全E cover/BVP/闭合和原所有几何门；模式观察优化不能替代这些对象。

课题仍只有旧M96/N1024/scalar=.99开放前缀接受。完整非零112/338/450、同一固定g的连通闭C²嵌入族、全t强C²、全域relative metric≤1e−6、固定H与整像held、含反射E、全t reach、完整闭F0的D及固定问题后的真实精化序列，均继续真实支付。README未完成，本条不是停点。
