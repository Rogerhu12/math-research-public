# R561 — 原首乘积不变的准确二次平均与实际 owner 编译接口

作者：OpenAI ChatGPT /root（AI 协作者）  
日期：2026-11-16（UTC）

**可信度：已证明，限于本文完整给出的有限字条件结论与来源接口。** 本文没有执行科学计算、import、AST、编译、测试或 fixture；所有实际运行必须在公开 Rogerhu12/math-research-public 自身 Actions 中完成。本条不是新的数值接受、收敛速度、连续曲面存在性或 README 完成结论。

## 561.1 问题、具体改动与结论

原 binary128 角平均在三个 primal 路径逐项执行

$$
s\leftarrow\operatorname{RN}_{128}
\bigl(s+\operatorname{RN}_{128}
(\operatorname{RN}_{128}(ab)\,c)\bigr),
\qquad c=1/\operatorname{Q}(N).
$$

这里的括号由原左结合表达式、原真实 Q 类型及不重排、不融合的编译选项确定；$a,b$ 是该原项当次已经形成的操作数，$N$ 是原角节点数。R561保留原表达式形成的**第一个已经舍入的乘积**
$x=\operatorname{RN}_{128}(ab)$，保留原 $c=1/\operatorname{Q}(N)$ 的实际计算，保留每个原项、每个原加法及全部累加次序。它只在原 $N$ 为正二的幂、原 $c$ 的实际字词恰为对应正二进制幂、且第二次乘法结果可由 normal 指数准确移动或原带符号零表示时，用字词操作得到同一结果。其他所有情况实际执行原 $x\,c$。

本条不是把 $ab/N$ 改成 $a(b/N)$，不交换原乘法，不提前缩放 $a$ 或 $b$，不恢复已经在首乘积发生的舍入或下溢，不合并任何求和。也没有缓存矩阵、几何、状态、$H$ 或另一个 root 的结果。

完整条件结论为：在原 GCC little-endian IEEE binary128 的有限字条件、原无重排编译合同及同一已到达的科学控制流前缀下，R561 三个 primal 角平均每个返回的有限字、每次原求和结果均与 R550 原第二乘法实现一致；原 root/方向/试步/容差等以这些数值作出的决定一致。正常科学路径的循环数、阈值和取样没有删改。原时间、磁盘、外信号等外部停止可能在不同位置出现，故不声称运行前沿、用时或最终完成范围一致。

## 561.2 准确 normal 缩放引理

### 561.2.1 原字词表示

在本条声明的实际 binary128 ABI 中，16字节Q按little-endian存入16字节无符号整数 $w$。符号位 $s$ 是最高位，15位带偏置指数为 $e$，112位 fraction 为 $f$。有限非零 normal 字满足

$$
1\le e\le32766,\quad 0\le f<2^{112},\qquad
x=(-1)^s(2^{112}+f)\,2^{e-16383-112}.
$$

本实现只在16字节 unsigned __int128、16字节Q、113位有效精度、原指数范围、8位byte及原little-endian编译器合同同时成立时进入此表示路径。该断言的ABI范围明确限于本题原GNU __float128；并没有由几个数值宏推出任意非IEEE实现也具有同一位布局。

原N保持int参数。若N为正二的幂，设 $N=2^k$。通过整数位判定及右移求出k，不用浮点对数。原平台的正int限制使k处于该平台可表示的范围，实际原N=2048对应的k并非通过硬编码代入；本实现实际读取N。原逆数Q字词还必须与

$$
w_c=(16383-k)\,2^{112}
$$

逐位相同。此项实际比较同时确认正号、正确指数及全部fraction为0；仅仅在数学上知道N应为二的幂不替代这个实际检查。

### 561.2.2 normal 情形

设实际首乘积x为normal且 $e>k$。令

$$
w'=w-k\,2^{112}.
$$

因为 $e-k\ge1$，此无符号减法只把指数域从e改成e−k；fraction域没有借位，符号域不变。新字词代表

$$
(-1)^s(2^{112}+f)\,2^{e-k-16383-112}=x\,2^{-k}=x\,c.
$$

它仍是有限normal，精确乘积已经是一个可表示Q数。故原第二次正确舍入乘法的结果就是该字词；本次没有任何舍入误差被移动到另一运算。本引理甚至不需要利用相邻数字的误差界，因为第二乘积本身准确可表示。原正常舍入合同足够，不需要新的数值容差。

在C++实现中，经std::memcpy把实际product复制到无符号字词，读取指数；通过实际条件后减去k左移112位，再用std::memcpy返回Q。没有指针类型重解释别名，没有浮点指数求解，没有调用一个不同精度的缩放函数。

### 561.2.3 两个带符号零

原字词条件 $(w\ll1)=0$ 只匹配正零与负零。在实际已核为正的c下，原精确乘法保留零符号。实现直接返回实际product，逐位保留该符号；从首乘积的下溢得到的零也只保留已经发生的原结果，绝不恢复本来丢失的数值。

### 561.2.4 完整回退范围

以下每一种情况均执行原表达式 product*scale.inverse：

1. native word layout不支持；
2. N不是正二的幂；
3. 原逆数实际字词并非所声明的准确正二进制幂；
4. 首乘积为非有限字；
5. 首乘积为非零subnormal；
6. 首乘积为normal但 $e\le k$，因而缩放可能进入subnormal/零范围。

第6种即使在某些特殊fraction上仍可准确表示，也保守地走原乘法。本条不为这些情况添加接受门，不重算候选，也不把资格失败记为数学失败。非有限字保留原第二乘法，但本文不扩大为任意NaN payload、信号NaN或外部浮点异常观察者的普遍等价定理。完整有限正常执行的字词定理及原fallback代码关系已经足以界定本项改动。

### 561.2.5 首乘积与累计误差为何没有改变

原代码的a*b始终先真实执行，并把这个实际Q值作为helper的product参数。辅助过程没有访问未舍入的实数ab，也没有重新计算a或b。上两节给出返回值与原第二乘积的相同Q字词；随后原 += 使用同一个旧s、同一个返回Q和相同原加法。对角索引n及内部列索引按原顺序归纳，全部前缀和均逐位相同。

这个归纳不把二进制误差近似当相等，也不借助有限随机fixture。原first-product如果已舍入或下溢，其实际结果被原样保留，是引理的输入而非被证明为无误差的量。

## 561.3 三个真实调用点与完整控制流范围

本条以已刊R550两个完整源视图为基线；R550本身以R535原有限词及未改原persistent owner为祖先。生成器不修改这些基线，只在Actions生成两个有新basename、完整SHA的派生源。

| 原真实位置 | 原项 | 新helper统计路径 | 保持内容 |
|---|---|---|---|
| root_evaluate residual角积分 | quad*cs[i]*invN | root_residual | 全N、全J、原n/i次序、同一个quad/cs、原residual += |
| root_matrix Gram角积分 | value*gc[k]*invN | root_gram | 全N、k=0..2M、原bm/B构造及原求解 |
| primal rhs flux角积分 | f*sn[j]*invN | primal_flux | 全N、全M、原n/j次序及后续完整rhs/mean |

每一函数仍按原表达式计算invN。每次原函数调用仅多一个R561DyadicScale标量对象；它包含原inverse、整数shift和三个资格布尔值，不分配向量、表或跨调用存储。helper仍逐项调用，不减少n、i、k、j范围。原第一乘积分别是quad*cs[i]、value*gc[k]、f*sn[j]，没有用cached实数值替代。

root_matrix签名增加实际RootStats引用，仅为记录本次调用；primal root和trace primal root两个实际caller同时按完整计划修改。原spd_solve、残差norm、root停止/回退、线搜索、30×20内部root循环以及32×10 owner原试步限制都保持原源。所有原阈值、完整行、原两个mean、实状态列、域/BC及后置接口保持。

R550同root accepted完整RootEval的下一iterate一次消费继续存在；R561不会重新求一个被R550合法复用的RootEval，也不把省去求值的统计虚填回来。R535资格与局部有限词仍由真实原表达式产生。等价推理针对同一实际到达的有限字与原控制流；不由“源码少了一个乘法”推出用时一定改善。

## 561.4 trace 的完整责任

新trace只做四处完整literal变更：

- 包含新的R561 primal视图；
- 把原R550 primal身份诚实标成ancestor，并加入真实R561 primal身份；
- 原trace primal root_matrix调用传原RootStats；
- 在完整RootStats序列化中附加新的完整统计对象。

原dual类型、dual乘法法则及F_direction、C_direction、rhs_from_root、rhs_direction等全部方向算术正文未改。特别是原方向乘法包含a.d*b.v+a.v*b.d，不可因其value的逆数是二进制幂就删掉导数项或改变带符号零运算。本条没有给dual缩放新shortcut。

原方向算法消费同一已到达primal word，在本文有限字条件下，该word与R550相同；原方向正文于是接受相同的输入。所有原shadow、replay、分支、误差传播和失败检查保留。不能把“方向正文未改”声称为另行证明完整native解、全混合J或连续线性化误差已经合格；实际对应组件仍须按原末门运行。

## 561.5 所有实际计数与 last 的语义

新RootStats成员为r561_average，序列化键为exact_dyadic_angular_average，schema为R561-exact-normal-dyadic-angular-average-v1。对象完整包含root_residual、root_gram、primal_flux三条实际路径。每路径下列十个无符号计数全部返回，不能只取“加速命中”子集：

| 字段 | 准确含义 |
|---|---|
| terms | 本helper收到一个实际已经形成的首乘积 |
| exact_normal | 使用准确normal指数移动 |
| exact_signed_zero | 返回实际原带符号零 |
| original_multiply | 真执行原第二乘法 |
| fallback_layout | 原word表示资格不支持 |
| fallback_count | 实际N不是正二的幂 |
| fallback_inverse | 原inverse实际字词不匹配 |
| fallback_nonfinite | 首乘积非有限 |
| fallback_subnormal | 首乘积为非零subnormal |
| fallback_normal_to_subnormal | normal首乘积指数不足以保证normal结果 |

每条路径还有last_present及完整last。last含phase、angle_zero_based、index_zero_based、positive_dyadic_shift、original_product_biased_exponent；不适用的整数以null返回，无实际项时last为null，不伪造第0项。刚收到首乘积即记录该事实；完成资格分支时用实际分支phase更新。不会因未来会执行某分支而提前补计数。

join沿原stage index顺序合并，last只从实际last_present的路径更新。并行worker的物理结束顺序不替代原规定的统计归并顺序。原RootStats、R535十八项实际统计、R550两路径各十三项及完整last全部继续序列化；新对象没有删除旧字段。

在helper完整返回的有限前缀内，terms由两类准确返回与原乘法分支组成；fallback计数明确对应原乘法资格原因。但是异常、异步终止、截断输出仍只报告实际写出的范围，不利用这个关系推导未返回计数或补造last。整数计数不参与科学接受、误差界或root选择，不能把计数0当作某未启动组件实际执行后无命中。

新对象还明确记录原first-product、只替换第二乘法、其他word原fallback、全项/全次序、方向正文不变、无跨call缓存/科学前门、原stage归并，以及不声称资源前沿或速度相等。

## 561.6 全部发布源与仅Actions生成源

本条发布三件完整可执行来源及本证明，不发布展开C++或可再生科学raw。三个公开文件身份如下。

| 文件 | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_exact_dyadic_average.hpp | 6760 | e94b31dc091a8a727ab6f4808fb61e951cb892fc496120fe8312c82b7d71c0ac |
| computations/root_20261116_exact_dyadic_average.py | 18526 | 9d954a23b1a8991c4aff38c1ffb6879229552cc9894ba70e7c3fb485fa928082 |
| notes/R561-normal-dyadic-average-complete-source-plan.json | 13708 | 5667d987ea5b7387bb0c4f6c61d86cd9ea94035299da91d3c7889fb1cde5f5a7 |

完整计划包含每条old/new/count=1字面替换及全前后bytes/SHA，不是只列若干hash的空接口。两个输出的完整身份为：

| 角色 | 仅Actions生成的basename | bytes | SHA256 | literal数 |
|---|---|---:|---|---:|
| primal | root_20261116_exact_dyadic_average_primal128.cpp | 26420 | 0e01b54b3b456711efd23ba94961eb669aef5394ab848e720fcf4a4ac64c854f | 12 |
| trace | root_20261116_exact_dyadic_average_trace128.cpp | 35787 | 07b8fd4dd7d31b2728e0f74a3ed9c9e6653593376529c12d26cdb57d617b8dc5 | 4 |

实际基线分别为R550 primal25794 B/40e89e28adc36848cf0d28b466e219065e10bdf8b37145d5e18326a6cd5eb6e1，trace35565 B/822488bd3ca682478939baa7df047aa614218b6724e448f01705e10c9225eb71。R550 header7311 B/8610fdd602ca3cea28a0d28af254e1929e954d7762161cc4887af5a097190f26，adapter16634 B/66c2ff0d0b29c41cef00cc6a77764e4e168d2885c52b3f56c2abd961fad8f97c，完整plan12303 B/14b5c02071359276be2988dc273d6864df3d61e728df10df5b1bddc498134457。R535完整plan10232 B/f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b及其全部实际祖先由真正R550接口继续验证，不由本条简写取代。

对每一literal，正向应用前要求当时old唯一；逆向按逆序要求new唯一，再恢复整个原source文本。新完整字节必须等于计划输出的bytes与SHA。原文件不覆盖；新basename不存在时xb创建，已存在时只接受完整相同身份。这个source-level可逆关系不是一个新的科学门或数值fixture。

完整original persistent owner仍为geometry_20261115_native_persistent128.py，43371 B/767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322。original persistent C++仍为geometry_20261115_native_persistent128.cpp，22364 B/7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd。两原件保持原bytes，不写回旧源码或旧run。

## 561.7 真正可调用的来源准备接口

### 561.7.1 执行位置与完整CLI

adapter的HERE是其实际文件所在computations目录，SELF是其实际文件。执行要求GITHUB_ACTIONS=true、GITHUB_REPOSITORY为本公开仓库，并要求GITHUB_REPOSITORY、GITHUB_RUN_ID、GITHUB_RUN_ATTEMPT、GITHUB_SHA四项实际环境都存在；这些值全部进入run绑定。本地只写文本和纸证，不执行本节命令。

由实际公开Actions caller先创建**本次新source准备目录**；下面的TOPIC、COMP、ACTUAL_CURRENT_SOURCE_PREPARATION都由该真实入口确定，不能指向另一次run缓存。完整调用为：

~~~bash
mkdir -p "$ACTUAL_CURRENT_SOURCE_PREPARATION/R561"
python3 -u "$COMP/root_20261116_exact_dyadic_average.py" \
  --source-plan "$TOPIC/notes/R561-normal-dyadic-average-complete-source-plan.json" \
  --reuse-source-plan "$TOPIC/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --word-source-plan "$TOPIC/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$ACTUAL_CURRENT_SOURCE_PREPARATION/R561/source-binding.json"
~~~

三个source-plan路径必须实际存在，其完整bytes/SHA与当前R561计划逐项一致；不是通过同名文件或未核hash继承。binding-out是本次新文件，xb写入，不能覆盖既有同名回执。父目录缺失、已存在文件或写入失败属于真实I/O错误，不伪装成生成成功。

函数级完整调用为prepare_sources(plan_file,reuse_plan_file,word_plan_file)。它执行的是来源生成与身份核验，既不安装R550/R535编译hook，也不调用科学main，不调用g++，不创建原科学总钟。

### 561.7.2 真实祖先，不是重新描述的假receipt

R561从计划中的实际R550 adapter完整文件加载该来源模块；先核普通非symlink文件、basename、bytes/SHA，再核真实module.__file__及其真实HERE。本模块的R550祖先确实定义HERE；此接口不凭祖先通常应有某属性来访问不存在的字段。

随后调用实际R550.prepare_sources。R550内部依原合同调用实际R535来源准备，所以R561拿到的actual_R550_source_binding内包含实际actual_R535_source_binding。没有只复制预期source列表，就把祖先标complete；也没有在未运行的源生成步骤补上compiler_completed=true。

checked_ancestry完整核验：

1. R550真实schema、source_preparation_complete=true、compiler_completed=false、scientific_evaluation_performed_by_preparation=false；
2. 同一run四键与同一实际source root；
3. 实际R550 adapter、header及完整计划，计划receipt中的真实绝对路径/bytes/SHA；
4. 用实际R550.read_plan读取该完整计划，核其header、R535计划及两生成视图恰为当前R561声明；
5. 用实际R550.checked_ancestry继续核完整R535实际binding；
6. 所有R550原来源、两个实际生成源、两个祖先header及完整逆关系/未覆盖原件。

这些项目是当前源绑定的责任，不是一个新候选正确性或科学数值接受门。错误时保原类型、信息、traceback及已生成范围；不得以重新手写一个符合schema的对象绕过祖先真实执行。

### 561.7.3 本次完整binding

新schema为R561-exact-dyadic-average-source-binding-v1。成功binding完整保留：

- actual_source_root、run四键、实际adapter身份、完整source_plan receipt；
- actual_R550_source_binding整个原对象，包括其R535祖先，所有实际源/字段/顺序所表达的责任均保；
- actual_headers的三个实际header；
- actual_original_sources：两个完整R550基线、原persistent owner、原persistent CPP；
- actual_generated_sources：两个完整R561新视图；
- actual_source_view_literal_counts：primal12、trace4；
- 完整逆关系、source_preparation_complete=true、compiler_completed=false；
- scientific_evaluation_performed_by_preparation=false及不覆盖原source、不发布科学raw/生成展开的旗标。

只有所有新视图实际写出且核验完整身份后，source_preparation_complete才置true。这不说明后续实际编译已开始，也不说明某原owner/refinement已通过。生成源的bytes/SHA是源身份，不是一次科学运行的输出身份。

### 561.7.4 失败、完整读回与原90KB限制

prepare_sources内部异常由CLI捕获为source child code2：完整error.type、error.message、error.traceback；source_preparation_complete=false、compiler_completed=false。partial_source_state在能核完整计划时列出原R535两件、R550两件、R561两件六个预期输出，并逐项给present、完整expected、实际ordinary file身份、complete_declared_identity_matches或完整read_error。不能核计划本身时记录该实际读取错误，不能把空列表解释为“六件都不存在”。

require_actions在顶层、binding文件I/O等不属于该try内的失败可能直接非零；caller必须保留真实exit/stdout/stderr和文件存在范围，不能宣称所有非零都会形成同样的error JSON。

binding采用完整普通ASCII JSON及末LF写一次文件，既不切块也不压缩数值payload。若实际文件≤90000 B，stdout输出R561_SOURCE_PREPARATION及完整该对象；若实际>90000 B，只输出事件descriptor、完整bytes/SHA、complete_necessary_body_returned=false、真实source_child_returncode，并返回70。原source child2与读回运输70的责任分开；不存在“descriptor是完整body”的替代。

未来外层若要在自己的来源必要范围返回这个对象，必须读取本次实际完整文件并核身份，保完整祖先及所有错误/未访，遵守原独立90KB限；未知输出大小不能预先宣称fit。此处不新设数据缓存或Git/Release/artifact存储，临时真实源生成文件与回执按当前运行生命周期处理。

## 561.8 原 owner_scope 内一次直接安装

### 561.8.1 安装前置条件

真正caller从本次实际来源准备文件读出完整source_binding，并在**原persistent owner模块已经真实形成的同一个globals字典**调用install_owner_compiler(owner_scope,source_binding)。它必须在原main首次编译前完成。不能先安装R535或R550再来替换其编译函数；三键_R535_SOURCE_BINDING、_R550_SOURCE_BINDING、_R561_SOURCE_BINDING在该scope中都须尚不存在。

R535/R550在此只作为已经实际生成的来源祖先；真正的编译安装只有R561一次。本文允许同一source目录已有完整相同祖先视图，并按完整字节核验，不能把重复source prepare当一次额外科学求值。

安装函数重新验证同run、实际source root、当前adapter、完整计划、完整祖先、所有headers/base/generated sources。还核原owner source整件身份、原CPP/ORIGINAL_CPP/TRACE_CPP名称，以及原compile_owner和main的__globals__就是同一个实际owner_scope。原所需祖先PINS继续具有原实际值。这个scope关系确保随后原main真正解析到新compile_owner，而不是在另一个孤立dict安装了一个从未调用的函数。

### 561.8.2 完整编译函数变更

在未改原persistent owner全文中，以唯一def compile_owner开始及其后原下一个def边界提取完整函数：

| 函数 | bytes | SHA256 |
|---|---:|---|
| 原compile_owner | 3860 | be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d |
| R561完整派生compile_owner | 6256 | 97e534367318ae3f16e3d24b0628cc603ca99c0cbb7e6b830db6d59e6a5afc03 |

计划中四条完整old/new/count=1变更依次正向并全逆恢复原函数。它们只增加完整依赖绑定、诚实标注当前trace来源、改写完整编译receipt；不删掉原完整evaluate observer、原行处理、原原子输出或任何科学调用。

保留全部原PINS，然后加入三header、R535两个视图、R550两个视图、R561两个视图及三adapter的实际完整pin。将ORIGINAL_CPP、TRACE_CPP指向本条新的primal/trace basename；持有完整source_binding的deepcopy作为_R561_SOURCE_BINDING。在实际owner_scope中exec定义完整新compile_owner；此时只有定义/安装，尚未实际调用编译或科学求值。

安装返回独立schema后缀-installed-v1的完整receipt：run、actual_adapter、完整source_plan、原/新完整函数身份、逆关系、原persistent main/solve/replay/limits保持、三祖先真实源、原first-products/reduction/trace方向正文保持、原CPP完整身份，以及actual_compile_not_yet_called=true与no_scientific_success_inferred_from_installation=true。它不篡改source_preparation阶段的compiler_completed=false。

### 561.8.3 真正g++仍由原main调用

随后仍调用原persistent owner main一次；所有原main/solve/replay/预算和调用方式保持。真正compile_owner首先核十二件header/generated/adapter依赖完整bytes/SHA，再执行原CPP pin、完整当前trace pin、原standalone main唯一性、完整observer接点与原逆关系等已有责任。

原persistent CPP22364 B/7789007e…不改。生成include仍用原native_frozen_trace_variation128.inc文件名，这是原编译接口的历史名；新receipt不会因文件名含frozen就声称数值前缀与R283原字节相同。真实包含的是当前R561 trace及其R561 primal，再连真实R550/R535来源。

g++保原gnu++17、O3、fopenmp、frounding-math、ffp-contract=off、fno-fast-math、原work/HERE include路径及lquadmath；原300秒编译上限、原PGID/TERM/KILL/reap与错误保留流程不改。科学clock由原调用链决定；本条不为编译hook或某个root另起19200/6000等新预算，也不调整已有时钟起点。

原代码只有实际g++ returncode0且真实executable满足原存在检查后，才形成完整成功编译record。它包含真实command、实际CPP、included_primal_source、included_trace_source_view、原primal/R283/R535/R550祖先、真实生成include、真实stdout/stderr/executable及退出码的完整receipt。

### 561.8.4 历史键与诚实编译范围

完整编译绑定仍通过历史外键root_finite_word_cache_compilation_source_binding传回，内部schema明确是R561当前binding，整个对象保留。该兼容键不意味着只运行R535或只描述缓存；完整body同时记录三个改动的实际源与当前include。

顶层复制本次完整source_binding后，加入actual_compiler_command、actual_generated_include、actual_compile_returncode、actual_executable、actual_compile_stdout、actual_compile_stderr，以及compiler_completed=true。嵌套R550/R535 source-only子对象里的compiler_completed=false仍原样保留；这是各自阶段的实际含义，不是矛盾，也不能把嵌套false篡改为祖先另编译过。

原frozen_R283_numerical_prefix_is_byte_identical与only_frozen_trace_standalone_main_excluded两旗标在新record中明确false。全部原observer正文和实际修改范围以完整source计划为准，不把“只删standalone main”当成新trace字节关系。编译成功仍只支付编译责任，原owner数值门、replay、后置full stage及FD/fullDN尚须真实完成。

## 561.9 后续完整caller与reader的必要责任

本组件的真实完整入口保留为R562/request236，实际结论保留R563，由amplitude唯一读取终态。它是独立入口，不修改正在运行的232、233或其他冻结run。

后继必须把本条三个公开文件、两个实际新生成视图及完整call链准确加入原来源map，保所有祖先source值、原numeric request对象及原全部资源参数。R561 source-only准备的实际文件路径与原owner_source目录必须相同；真实owner_scope只直接装R561一次，并独立保R534原post defer安装及原main，而不是把source prepare的成功解释为所有hook都被实际调用。

源读回、正常科学必要与recovery必要都须保：

- 整个R561来源binding及完整R550/R535祖先；
- 实际安装receipt与实际编译record分别存在/缺失/错误的准确地址；
- 整个原RootStats，包括新的exact_dyadic_angular_average三个十计数/full last；
- 全部原错误、失败/未访/未启动范围、partial与原时钟/资源记录；
- 原独立source/science完整必要scope、90KB/70与实际owned quiet/cleanup条件。

已有八具名表可按其原完整可逆关系运输；未知新RootStats子字典必须保literal或明确完整可逆表示，不能因旧reader只知道18或13项就静默丢掉这三组十项。不得把whole RootStats改成命中率、只留成功计数、截断traceback，或通过增加多个body规避同一对象的上限。

若源绑定或读回超限，必须保实际完整文件身份、实际旧子退出和未返责任；源准备完成、安装完成、真实编译完成、数值owner完成、post完成、协议fullDN完成是各自独立事实。任一未付不能从上一层的true推出来。完整quiet也不能只由GitHub step success补造；删除仍须原真实owned范围及完整必要读回条件。

## 561.10 不改变的原问题与剩余实际工作

本条没有修改M112/N2048、全338×112输出/J、699×453、双mean、真实完整576 stage/577节点/每节点224 shooting state/每局部226状态、原FD十方向×三步长×两层及其阈值、原RMS/BC/域/merit、final fresh J/audit。没有改变原128 residual/tol/replay权威或R529/R532同DN模型与原非线性末门。source/checks不是新科学接受门，条件有限字引理不直接产生完整响应。

原19200总钟、owner6000、replay1200、stage8000、boundary600、endpoint600、audit1800以及各原外层资源行为继续由正式入口保留。本条不会为追求完成而抬限，不拿单次乘法计数或某一次不同轨迹的用时推性能。实际原time checks位置保持，但代码成本的变化可改变到达某check时的真实墙钟，故允许真实资源partial并必须如实记录。

目前本条仅完成完整source、有限字证明、真实准备/一次安装/原main编译接口及全scope读回责任。尚无R561本次科学run、实际命中数、速度或完成接受。未来R563必须回报原实际轨迹、完整错误/未访、是否真正通过owner/replay/post/FD/fullDN，以及真实必要运输与清理，不能以纸证替代。

本题仍须同一固定g、连通闭C²嵌入、全t强C²连续、固定内点H与直径/整像held/反射不全等、全t reach、全域relative metric及固定目标后的实际mesh/M/t精化达到README标准。当前只接受旧开放prefix，本条没有弥补这些连续几何和完整非零112/338/450责任。

## 561.11 原件与证明依赖

本条有限字引理在§561.2完整证明，不借用未核的外部数值实验。祖先实现与原科学门的完整出处：

- [R535：原128同root有限词与真实编译hook](R535-original128-local-finite-root-words-and-real-compiler-hook.md)及其完整source plan；
- [R550：同root原accepted完整求值一次复用](R550-same-root-accepted-complete-evaluation-reuse.md)，包含完整条件证明、全部来源/CLI、原编译函数与原预算范围；
- [R551：request232完整同DN模型入口](R551-request232-accepted-root-reuse-and-honest-projected-model-complete-entry.md)，用于独立后继完整来源组合的基线，当前232实际结论仍另记；
- [R528：actual225首完整接受步与原owner预算partial](R528-actual225-one-live128-accepted-step-and-owner-resource-partial.md)，仅说明一条真实先前停点，不作为本条速度证据。

每项公开source完整bytes/SHA及所有literal均在本条源和计划内；实际运行号与源head由正式后继唯一派发后的官方记录支付。正文一经完整即独立发表，不等待fixture、额外科学门或独立机械重跑。
