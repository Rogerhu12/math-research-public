# R535 — 原128 root内有限固定字词复用与真实owner编译接点

作者：ChatGPT /root（AI）。日期：2026-11-16 UTC。

**可信度：已证明，限原固定有限程序、声明的浮点语义及完整求值条件；新源未执行。** 本项不产生新的收敛记录、导数证书、速度结论或README完成声明。源码文本、全字节身份和显式逆替换在此核对；科学算术、import、AST、编译与运行只由后续公开仓库Actions执行，不增加fixture或独立核验前门。

## 535.1 实际缺口与精确范围

[R509实际221](R509-actual221-current-H-one-accepted-and-owner-resource-partial.md)已完整读回当前H的原128求解：第一方向alpha=1全576段/129248行严格接受，残差从14074125.721549422871053526172072936降至0.00119384019932733053462024588807814309；下一方向alpha=1只完成133段/30016行，原owner6000秒额度内未过2e−9，独立fresh replay也未完成。四个后置组件尚未开始。已清原state不可由SHA续用。

因此[R529](R529-current-owner128-complete64-model-and-original-nonlinear-gates.md)/[R532](R532-current-owner128-projection-and-complete64-stage-library.md)的后置完整模型构造本身不消除该先行owner成本。本项只处理实际原primal root中的重复表达式：

1. 同一root调用内，固定的momentum、pt与全部角点P/Pt；
2. 同一次root_evaluate内，完整U模式系数；
3. 将两种复用诚实接入真正persistent128编译include，同时保原solve/replay与全部门。

本项没有改变原Problem输入、M/N/深度、有限Fourier表、profile、RK4、target、scales、far、H、全状态、双mean、原30×20 root规则、原32×10 native规则及各严格阈值。没有跨root、RK点、cell、状态或H的缓存。

## 535.2 原固定源与声明新文件

实际原源均在本课题computations/：

| 角色 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| primal | geometry_20261115_native_primal128.cpp | 23890 | 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d |
| trace祖先 | geometry_20261115_native_trace_variation128.cpp | 34622 | 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d |
| persistent C++ | geometry_20261115_native_persistent128.cpp | 22364 | 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd |
| 原Python owner | geometry_20261115_native_persistent128.py | 43371 | 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322 |

三个正式实现文件：

| 文件 | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_native_root_finite_words.hpp | 7102 | 6706eae670bf5746eb42d194bd456d290c290d451ddc52d80359d0263f90e7cc |
| computations/root_20261116_native_root_finite_words.py | 10892 | 1c99623e2cd63d0a4700011c96e5054645cf7dd8ee5cf3357f0c77d1727026db |
| notes/R535-native-root-finite-words-complete-source-plan.json | 10232 | f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b |

plan声明两个临时include依赖的完整文本：

| 角色 | 临时basename | bytes | SHA256 |
|---|---|---:|---|
| primal view | root_20261116_native_root_finite_words_primal128.cpp | 25230 | 3e1cb0a416418fe56fbee889df5debdfc9ed097b797a1b8e086b563ce4fd9241 |
| trace view | root_20261116_native_root_finite_words_trace128.cpp | 34950 | 2e122e0ca6ad21e1c11ab711cc5af40a6955d3ff054f6cd445dbd885fbb98b12 |

生成文件不重复收入Git。primal有9个、trace有4个唯一显式literal改动；Python compile_owner有4个。每次替换之前核完整祖先bytes/SHA和唯一位置，之后核全输出bytes/SHA；按反序逐项逆替换回完整原文。这个源绑定不是科学fixture，不运行数值，也不构成新的BVP门。

## 535.3 原表达式与不变输入

原Problem把每个binary64表词准确lift到binary128。原packet入口检查finite及实际M112/depth576，N在原合法范围；profile的r、w、w2、E等原域检查保留。原进程要求FE_TONEAREST。后续源没有改变舍入模式。

对一次原root(p,state,cell,g,policy,stats)，state、p、g均以const引用传入。root内只有局部e与trial改变；p、state和g不变。target的形成、target_scale的qmax次序、原30次Newton和20次alpha回溯保持原样。

记RN为原Q算术的逐操作binary128结果。下述公式仅是原表达式的排版，括号与源代码结合次序以literal为准：

$$
r_3=(r r)r,\qquad
p_j=\frac{(-m_jr_3)Q_j}{\mathrm{sq2}\,w},
\qquad
p'_j=m_jp_j.
$$

第n角原顺序为

$$
P_n=0+\sum_{j=0}^{M-1}p_j s_{nj},
\quad
P'_n=0+\sum_{j=0}^{M-1}p'_j c_{n,j+1},
$$

其中每个乘法和每次从j=0至M−1的累加都分别执行原Q运算。这里的求和不授权改成树形和、向量归约、FMA或准确实数再一次舍入。

对本次e，先按原j序形成L_j=target_j+e_j。原

$$
U_n=0+\sum_{j=0}^{M-1}
\left[-m_jL_{j+1}+(m_jm_j-1)p_j\right]s_{nj}.
$$

中括号内的完整Q字词记为u_j。它依赖本次L，因而只可在本次root_evaluate内复用；不能跨Newton/trial复用。

## 535.4 两种局部缓存的实际生命期

R535FixedRootWords是root函数内的自动局部对象，持有本次p/state/g地址，仅在该root原两个root_evaluate调用点传入。没有static、thread_local或进程全局数值缓存。root返回或异常退出即销毁，原每RK四个RHS调用分别获得自己的root对象。

第一次root_evaluate在原time_check与evaluations计数之后，尝试构造固定词：

1. 用完整原表达式和原j顺序形成momentum与pt，pt[0]仍为+0；
2. 所有被缓存mode词finite才继续；
3. 每个n从+0开始，原j顺序累加P/Pt，每32个角点调用原time_check；
4. 所有N对实际词finite才令qualified=true。

遇到第一个非finite mode或角词，只记录相应fallback与实际位置，qualified保持false；后续原root_evaluate使用其原完整表达式。缓存构建中的非finite不是新的BVP拒绝，也不修改原域错误或将非法词置零。原的目标/域/根返回判断仍在原循环中进行。

固定词资格成功后，所有后续root_evaluate读取本次已保存momentum/pt/P/Pt。source中的p/state/g地址必须仍是同一个局部调用；该检查是闭合调用来源约束，不是原BVP的新条件。

每次root_evaluate分别形成完整u_j。m_j、L_{j+1}、p_j与实际u_j都finite时才读取缓存u_j；否则该次所有角点继续原完整U表达式。原每个u_j*s_{nj}及每次U累加仍按j顺序执行，不删零项、模式、角点或mean。资格失败时尚未形成的缓存后缀不被读取。

## 535.5 有限字词等同性

**命题1。** 固定原source输入、原舍入模式和原编译浮点语义，忽略资源中断、内存分配失败与未被原算法读取的浮点异常标志历史。对一个原root_evaluate的完整执行，新源得到相同的P、Pt、Lv、U及其后全部Angular字段、原residual、err、max_quad和原域统计；非finite不满足资格时转回原表达式。有限结果的符号零和subnormal字词保留，不宣称NaN payload或资源停止前沿相同。

**证明。**

若固定缓存未提供、未qualified，则其P/Pt和momentum/pt仍按原表达式计算，结论对此部分平凡。若qualified，则p/state/g在整个局部root不变。原momentum与pt是这些固定输入的相同Q表达式，因此每次原重新计算得到相同字词。新缓存第一次形成的momentum/pt就是这些词；复制Q向量不改变其有限表示。

对每一固定n，缓存P/Pt从原+0开始。假设到j−1时累加器与原相同；第j个原momentum/pt及sine/cosine词相同，乘法输入、舍入与随后加法输入相同，所以两新累加器相同。对j归纳得到完整P/Pt字词相同。n之间不共享累加器，不改变原每个角的和。

L仍逐项执行target+e；Lv仍按原j顺序加L[j+1]*cs[j+1]。对U，如果本次u缓存不qualified，执行原表达式；若qualified，缓存u_j是原完整括号表达式的Q结果，原finite输入和逐操作结合顺序相同。实际U循环依然执行u_j*sn[j]并按原j顺序加到+0。再次按j归纳得到U字词相同。signed zero与subnormal不是被筛掉的零项，所有实际乘加仍发生。

原K、T、u、D、S、A、sqrt、fc、gc、quad和finite测试正文不改，故相同输入给相同输出与原首个域拒绝位置。原n顺序、每一residual[i]+=quad*cs[i]*invN的次序、最后加e及finite/err/qmax全部不改；按n和i归纳，原完整residual与所有原统计相同。

缓存资格扫描不更新原minD/minS/minA、root停止计数或原科学残差，只记录新具名操作计数。因此其数学输入输出不污染旧判据。证毕。

该命题是固定完整有限程序的语义论证，不是声称严格实数方程等价于任意浮点代数重排。实现没有利用交换律、分配律或“误差足够小”替换原表达式。

## 535.6 原root、RHS、RK与native选择的保持

**命题2。** 在上述固定输入与两次执行均完成相应计算的条件下，原root的返回词、原30×20选择和原fallback选择不变；原完整RHS、RK4、每段226输出、全部576段shooting residual及strict native trial判据保持相同有限词。

**证明。** 第一次原e为同一全+0向量，target与target_scale未改。由命题1，第一次ev相同。原stop、original_stop计数、scale及fallback阈值比较的输入完全相同。若返回，finish构造的L和ev相同；若继续，root_matrix直接消费相同完整Angular行，其数值体未改，随后原spd_solve同样未改，得到相同step。

每个alpha=scalbnq(1,-k)、trial[j]=e[j]-alpha*step[j]均原样。由命题1每个完整trial评价相同，原strict err下降或原stop选择相同；因此第一被接受k相同、下一e相同。按Newton次数归纳，原返回、fallback或数学异常一致；原未访k没有被生成新拒绝记录。

原rhs从同样root词形成所有flux、Q/Pi及两mean导数；原RK4四次调用、所有步和端口读写数值体不改。按RK步、stage和原全行归并顺序归纳得到完整残差相同。原owner的全128状态、R273方向协议、alpha试步、norm/strict decrease、外tol及fresh replay均没有被本项改写，因而在相同实际方向输入及完成范围内继续原选择。证毕。

现有R283 trace shadow的数学主体也不改。它自身调用root_evaluate时没有新固定缓存参数，所以只使用本次U有限词资格；由命题1，其原primal-shadow逐词检查与完整有限trace路径不被替换。此事实不把有限trace导数变成IEEE舍入映射的导数，原方向责任与后置stage/endpoint/audit来源保持原分界。

## 535.7 编译语义与明确未覆盖的行为

实际compile_owner保原命令：

~~~text
g++ -std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math
    -I <owned-work> -I <actual-HERE> <original-persistent.cpp> -o <owned-executable> -lquadmath
~~~

原Q为__float128，原断言sizeof(Q)=16、FLT128_MANT_DIG=113，原进程FE_TONEAREST检查不变。证明按此原逐操作binary128语义；没有声称在fast-math、FMA重写、不同精度或改变舍入模式的程序中成立。

完整缓存会先计算所有P/Pt，然后进入原逐角域检查。原若很早域拒，新程序可能额外计算更多固定角词；资格扫描、分配、向量复制与新计数也有成本。因此不承诺：

- 同一墙钟预算下相同已完成stage前沿、相同timeout时刻或速度；
- 相同内存分配失败位置；
- 相同未被原算法读取的浮点sticky flags、trap时序或NaN payload；
- 完整导数误差界、更多可行H、收敛或原2e−9一定通过。

原源不设置浮点trap、不读取这些异常flags作科学分支；本项不增加此类读取。原time_check异常原字向外传播，原partial/error/stage记录继续真实反映新运行。非finitefallback会执行原表达式，不用finite资格决定原BVP是否接受。

## 535.8 真实统计及其限制

新R535WordStats含18个uint64实际计数：

| 范围 | 字段 |
|---|---|
| 固定缓存请求/决策 | fixed_requests、fixed_builds_started、fixed_builds_completed、fixed_qualified_builds |
| 非finite资格回退 | fixed_nonfinite_mode_fallbacks、fixed_nonfinite_angular_fallbacks |
| 真实已形成词 | fixed_mode_pairs_formed、fixed_angular_pairs_formed |
| 实际root_evaluate路径 | fixed_evaluations_used、fixed_evaluations_fallback、fixed_evaluations_without_local_cache |
| 每次U资格 | u_builds_started、u_builds_completed、u_qualified_builds、u_nonfinite_mode_fallbacks、u_mode_words_formed |
| 原角行内的U读取 | u_angular_rows_used、u_angular_rows_fallback |

builds_completed表示一次资格决策结束，可能是合法finite结果，也可能是明确fallback；不表示所有N角均已处理，更不表示完整科学求值。角行U计数在该行全部U项形成后、原D/S/A门之前增加，不能当合法域点数。所有计数只是实际调用次数，不推算墙钟或收敛。

last_present与完整last对象同时保留。last包含实际phase、原zero-based mode/angle或null、本次是否使用固定/U缓存。每次root_evaluate先清本次使用标志；缓存构建、原角行及中断位置均真实标记。各stage仍用原RootStats::join的stage索引顺序合并，最后记录是这个声明次序的最后实际记录，不冒线程最后墙钟事件，也不是完整root轨迹。

原所有RootStats字段及打印值保持；新对象仅添加在root_statistics.root_finite_word_cache。实际原owner print_root_stats与primal standalone打印均显式调用新serializer，不能只有结构体计数而从输出漏掉。原必要reader当前选择会丢root_statistics，所以后续R536必须完整选入这个新具名对象及其上下文、presence和失败记录；不能从新stdout源已写计数推断必要正文已返回。

## 535.9 真正的owner编译接点

原persistent CPP不改，仍包含owned-work中的native_frozen_trace_variation128.inc。该basename是原兼容路径，不再表示其全部数学前缀原字不变。

prepare_sources只在公开仓库Actions内，从实际HERE已存在的原源与固定plan形成两个新include依赖；保完整原祖先文件不覆盖。install_owner_compiler在真实已有owner_scope上仅替换声明的compile_owner函数，并将该函数实际依赖的ORIGINAL_CPP/TRACE_CPP改为新basename。所有原PINS仍保留，另加新header、两个新view和实际adapter身份。

新compile_owner仍执行原一次g++，原300秒编译allowance、同PGID、原TERM/KILL与原失败处理不改。原evaluate函数正文只经过原四个只读full226 observer改动及原完整逆核，原完整所有stage输出仍保。

编译回执不再写frozen_R283_numerical_prefix_is_byte_identical=true或only_frozen_trace_standalone_main_excluded=true；两者明确false。分别返回：

- 实际被include的primal与trace view；
- 原primal/R283祖先身份；
- 实际生成include、header、完整source plan和adapter；
- 实际完整编译命令、退出码、stdout/stderr及executable身份；
- root_finite_word_cache_compilation_source_binding中实际compiler_completed=true。

prepare_sources返回的compiler_completed=false与安装返回的actual_compile_not_yet_called=true严格区别实际编译。若编译失败，不构造虚假的完成回执；原owner异常、已有source准备绑定、compile日志身份与原raw保留责任由完整调用者读回。

install_owner_compiler对同scope只允许一次实际安装；要求原main与compile_owner共用真实namespace、原变量/祖先pins正确，后续原main/solve/fresh replay调用同一实际新compiler函数。不另起owner、不旁跑旧root、不捕获异常后以旧binary重试、不重开科学钟。

## 535.10 能证明的重复量，不能预填的速度

若一个root在相同固定状态上完整调用root_evaluate共E次，且本项相关finite资格成立：

- 原momentum/pt表达式由每次M个变为同root一次M个，其后只是词复制；
- P/Pt的两条原M项角和由E次全N角变成一次全N角，后续读取相同词；
- 每次评价内u_j完整系数表达式由每个角重复，即NM次，变为M次；所有NM个u_j*sn与原U加法仍发生。

这些是源码级重复表达式数，不是benchmark。E=1时固定P/Pt不能减少原完整求和次数，还增加资格检查/存储；原域早拒或资源不足时，前置构造可能额外做工作。root_matrix、SPD、原flux Fourier和、RK4、R273、后置stage/boundary/endpoint/audit仍承担原成本。

新缓存内存只随原M和N线性增长，未缓存NM矩阵或整stage/J；它是每实际root局部向量，OpenMP仍原1–4线程。所有全状态和数组仍原dtype/完整形状，未作精度下降或字段选择。

## 535.11 剩余实际工作

本项完成局部source/proof/真实compiler API。拟226/R536只是协调保留，尚未登记或派发。后续必须在独立真实新request中完成：

1. 从已刊225完整链保留全部原科学来源与R522/R515实际后置实现；
2. 在原源准备阶段真正调用prepare_sources并纳入新source closure；
3. 在真实same-call owner_scope形成后、原main之前实际调用install_owner_compiler；
4. 必要reader保完整新18计数/last及实际编译回执、原所有门/失败/未访/quiet；
5. 原19200单钟、owner6000/replay1200及四组件原caps、单90K/70保持；
6. 原输入重建、正常fullH/J/FD/fullDN运行及唯一实际终态读回。

不改正在运行的225或旧221，不迁已清父，不以源完成宣布原容差/闭面/比例/精化通过。每完成结论立即刊；实际计算继续原open责任。
