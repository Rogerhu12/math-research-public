# R564 — 实际 binary64 表因子的完整整数乘积与准确 binary128 舍入

作者：OpenAI ChatGPT /root（AI 协作者）  
日期：2026-11-16（UTC）

**可信度：已证明，限于本文完整有限字条件、实际来源关系和控制流接口。** 没有本次科学运行、速度测量、接受父或连续几何完成结论。本文的代码与逐字变换仅作文本构造；科学import、AST、编译、测试与数值执行仅在本公开仓库自身Actions中发生。

## 564.1 具体问题及与R561的区别

原角平均三处以实际原table字作为乘法右因子：root residual中的cs[i]、root Gram中的gc[k]、primal flux中的sn[j]。原Problem从完整packet读取binary64有限字，并以static_cast<Q>准确提升到真正binary128；它们不是本条重新生成的理想三角函数值。R564仍逐项读取这些实际原word，逐次检查可用表示。

R561保留首个Q乘法，随后仅在正常可准确二进制缩放时替换第二乘法。R564进一步为这三个**首乘积**提供一个完整整数实现：实际左因子为有限normal Q、实际右因子为至多53位有效数的有限normal Q、实际舍入模式为nearest-even，并且准确舍入结果仍在normal范围时，计算完整113×53位整数乘积，再执行原正确舍入规则。带符号零单独准确处理。所有其他情况实际执行原left*factor。

所以本条保的是**原首乘积的RN128字词**，不能写成“快捷分支也实际执行了原首个Q乘法”。当前source/install/compile统计明确记录这个区别。R561旧代码及source-only祖先的声明不被追改，它们描述自己的冻结源码；新当前代码和新回执承担不同的指令事实。

新结果字再交给未改的R561第二乘法选择器。原角/列累加项数、每个原 +=、所有方向算术、root/owner试步和原接受门不动。不建立table缓存、状态缓存或跨root/call缓存，也不利用理想cos/sin对称性合并项。

## 564.2 完整表示和适用域

本条声明的实际ABI是原GNU little-endian IEEE binary128：Q为16字节、113位有效精度、15位指数、8位byte；unsigned __int128同为16字节。代码在表示条件不支持时直接回原Q乘法。本文并未由几项宏断言任意非IEEE实现也具有同一布局。

令normal左因子的符号为$s_a$、带偏置指数为$e_a$、112位fraction为$f_a$。则

$$
A=2^{112}+f_a,\qquad 2^{112}\le A<2^{113},\qquad
a=(-1)^{s_a} A\,2^{e_a-16383-112}.
$$

右因子$ b $也为normal；其fraction最低60位必须实际为0。令

$$
B=\frac{2^{112}+f_b}{2^{60}},\qquad
2^{52}\le B<2^{53}.
$$

这个整数来自真实Q word，不从文件名或“表应当是binary64”推断资格。于是

$$
b=(-1)^{s_b} B\,2^{e_b-16383-52}.
$$

原binary64有限非零字准确提升后满足这项有效位性质，包括原binary64 subnormal提升后在更宽Q指数域成为normal的情况；然而代码不依靠此来源推断，而是每次实际核指数和最低60位。输入文件里原sin接近0但并非0的字仍当实际非零值处理。

原persistent CPP在main里设FE_TONEAREST；原primal/trace独立main检查此模式。本新helper还在每次调用用fegetround读取当时实际模式，不改变模式。不等于FE_TONEAREST时回原乘法，不能把模式失败当候选拒绝。

非有限输入先分别处理为原乘法回退，防止把$0\cdot\infty$当零。两个输入有限后，若任一实际word是带符号零，返回符号异或后的零；否则要求两者normal及右因子上述有效位资格。新适用域是实现分支选择，不是添加数学容差或科学前门。

## 564.3 113×53位乘积的完整表示

令准确整数乘积

$$
T=AB.
$$

由上界和下界，

$$
2^{164}\le T<2^{166}.
$$

所以最高置位只可能在第164或165位。实现没有用一个128位乘法把高位截掉；完整T用一个128位high与一个64位low共同表示。

将

$$
A=A_0+2^{64}A_1,\qquad
0\le A_0<2^{64},\quad0\le A_1<2^{49}.
$$

先形成128位整数

$$
P_0=A_0B.
$$

其严格小于$2^{117}$，故128位容量足够。再令

$$
L=P_0\bmod2^{64},\qquad
H=A_1B+\left\lfloor P_0/2^{64}\right\rfloor .
$$

由普通整数分配律，

$$
T=H\,2^{64}+L.
$$

第二个乘积$A_1B$严格小于$2^{102}$，加数小于$2^{53}$，粗界也远小于$2^{128}$，故high计算没有128位溢出。又因为它正是$\lfloor T/2^{64}\rfloor$，可用T的严格界得到$2^{100}\le H<2^{102}$。所有乘法、移位和加法都在足够宽的无符号整数域进行；负号留给最终sign异或，不参与这些整数乘法。

代码中的p0、high、low正对应$P_0,H,L$。这给出完整166位乘积，不是高位近似，也不需要外部大整数库或临时数值数组。

## 564.4 规格化、余数与最近偶数舍入

### 564.4.1 最高位和右移数

定义

$$
j=\begin{cases}
0,&T<2^{165},\\
1,&T\ge2^{165}.
\end{cases}
$$

因T的范围已确定，只需检查$H$的第101位；代码使用high>>101是否非零，所得恰为j。要保留113位有效数，应丢弃

$$
r=52+j\in\{52,53\}
$$

位。令

$$
Q_0=\lfloor T/2^r\rfloor,\qquad R=T\bmod 2^r.
$$

由规格化选择，

$$
2^{112}\le Q_0<2^{113},\qquad0\le R<2^r.
$$

这里Q_0是整数significand，不是浮点类型Q。

因为$r<64$，全部被丢弃位都在L内部，故实现可准确形成

$$
Q_0=(H\ll(64-r))\mathbin{\mathrm{OR}}(L\gg r),\qquad
R=L\mathbin{\mathrm{AND}}(2^r-1).
$$

前一式两个部分占不相交的位域，OR等于加法；最终Q_0最多113位，128位中没有丢高位。后一式保留全部丢弃位，没有用一个粘滞位近似可能的tie。所有移位数均为原有限整数范围中的11、12、52、53或其对应半位位置，不会对64/128位类型执行等于或大于宽度的移位。

### 564.4.2 初始输出指数

原准确实乘积为

$$
ab=(-1)^{s_a\oplus s_b}\,
T\,2^{e_a+e_b-32766-164}.
$$

令初始输出带偏置指数

$$
E=e_a+e_b-16383+j.
$$

将$r=52+j$代入可核：

$$
2^{e_a+e_b-32766-164}\,2^r
=2^{E-16383-112}.
$$

因此以Q_0为significand、E为偏置指数的word正是乘积规格化截取的下邻字。指数算术使用普通int；两个原15位有限指数与固定偏置的运算在该范围内不会溢出。

若E不在1至32766，本实现直接回原Q乘法。不试图在快捷路径自行处理subnormal、零下溢或溢出。这一保守范围也允许后续原乘法处理“截取指数为0但舍入可能回normal”等边界，不漏算或拒绝它们。

### 564.4.3 全部最近偶数情形

令半间隔整数$h=2^{r-1}$。原nearest-even规则给出：

$$
Q_1=Q_0+
\begin{cases}
1,&R>h,\\
1,&R=h\text{ 且 }Q_0\text{ 为奇数},\\
0,&R<h,\\
0,&R=h\text{ 且 }Q_0\text{ 为偶数}.
\end{cases}
$$

证明如下：相邻normal可表示数在此binade中的间隔正是被删除r位所对应的单位；R<h时下邻更近，R>h时上邻更近；R=h时两者等距，Q_0的最低保留位决定下邻是否偶数。代码比较准确完整R、h及Q_0&1，完全执行上述四种情况，没有双重舍入。

如果Q_1=$2^{113}$，则把significand右移一位成$2^{112}$，并令E增加1。这是唯一可能的舍入进位，因为Q_0<$2^{113}$且只加至多1；新word正是相邻binade的第一个数。若新E超过32766，仍回原Q乘法。其他情况Q_1位于$[2^{112},2^{113})$，E仍为合法normal。

最终word用原符号异或、偏置指数E及fraction$Q_1-2^{112}$组装，经std::memcpy转回Q。这个word正是原准确实乘积在当前nearest-even模式下的RN128结果；它不是由binary64计算乘积后再提升而来。

## 564.5 零、完整回退和有限字等价定理

两输入均有限且任一为正/负零时，准确乘积为零，符号等于原符号异或。实现先排除非有限，再以word左移1是否为0判两个零，返回该异或符号位构成的零。它不把非零subnormal改成零，不把实际微小三角表字改成理想0。

全部原回退范围为：不支持的word layout、当次非nearest模式、左或右非有限、两者非零时左或右为Q subnormal、右fraction最低60位不全0、未舍入输出指数不在normal范围、或最近偶数进位越过normal最大指数。每一分支直接执行原left*factor，保持实际原操作数，不给数值失败新含义。

**定理。** 在本文声明的原ABI和Q正确舍入合同下，对所有已到达且正常返回的有限输入，R564给出的首乘积字与原left*factor字相同；快捷normal分支由§564.3–4完整整数计算和最近偶数规则给出，有限零分支由符号规则给出，其余分支就是原运算。非有限分支保原表达式，但不扩大成任意NaN payload/信号异常行为的普遍定理。

此定理不要求预先限制左因子的有效位，它保完整113位。也不要求理想三角函数、table某列精确对称、原残差很小或解已经接受。资格不符只是原计算回退。

它同时不声称硬件或软件浮点异常**状态旗标**一致：用整数取得同一舍入字不一定设置原inexact旗标。当前源显式标记floating_exception_flag_equivalence_not_claimed。原相应primal/trace/persistent源中的fenv接点是舍入模式设置/检查，不从inexact旗标选科学分支；新代码每次读取模式且不更改它。任何任意外部异常观察者或改变程序环境的信号处理不在字词定理的范围。

## 564.6 与原累加、R561、R550和R535的组合

三个真实调用点均把新首乘积结果送入原R561 helper：

~~~cpp
r561_average_actual_product(
  r564_exact_lifted_factor_product(actual_left,actual_factor,
                                  actual_path_stats,n,index),
  original_average,original_R561_path_stats,n,index)
~~~

原actual_left依次为quad、value、f；actual_factor依次为原cs[i]、gc[k]、sn[j]。R564没有把invN乘到factor，也没有把第二乘法移过加法。R561仍接收一个已经形成的Q word；本定理说明它就是原首乘积的RN128字。因此其原准确dyadic或原fallback选择接收相同输入和同一原invN，得到同一第二乘积。

再按原n及原列次序对 += 归纳，每个完整已到达累加前缀都具有相同旧sum和相同下一项，原Q加法结果相同。完整root residual、Gram、primal flux于是相同；以它们为输入的原root/方向/试步/容差判断在同一个已到达有限控制流前缀中保持。

R550只在同root内复用原accepted完整RootEval，R535只共享原局部有限词；它们的资格及原返回内容不被本条改写。原trace方向函数正文全保，只包含当前新primal源并序列化新统计。对该未改方向正文，本条供给相同的已到达primal字；不通过“值相同”另外宣称完整连续导数误差或全J数值接受。

原time_check位置、各预算阈值和所有原scientific gates不变，但新代码的耗时会改变到达检查时的真实时间。故不声称两次run必访问相同试步后缀、用时更小或能在原6000秒内完成；实际资源partial仍按原范围报告。

## 564.7 三路径完整统计及失败时的含义

新RootStats成员为r564_product，序列化键exact_lifted_factor_product，schema为R564-exact-lifted-factor-product-v1。三个完整路径是root_residual、root_gram、primal_flux；每条保全部十七项：

| 字段 | 实际含义 |
|---|---|
| terms | helper接到一个原实际操作数对 |
| exact_normal | 完整整数乘积/最近偶数返回normal Q |
| exact_signed_zero | 有限输入的符号零快捷返回 |
| original_multiply | 已进入并随即执行原Q乘法分支 |
| fallback_layout | native表示不满足 |
| fallback_rounding | 当次实际模式不是FE_TONEAREST |
| fallback_left_nonfinite | 原左字非有限 |
| fallback_factor_nonfinite | 原右字非有限 |
| fallback_left_subnormal | 两者非零而原左字为Q subnormal |
| fallback_factor_subnormal | 两者非零而原右字为Q subnormal |
| fallback_factor_precision | 原右fraction最低60位不全0 |
| fallback_result_range | 规格化或进位后不能保证normal范围 |
| rounding_below_half | 实际快捷normal结果的余数小于半间隔，包含准确乘积 |
| rounding_exact_half | 实际快捷normal结果的完整余数正好等于半间隔 |
| rounding_above_half | 实际快捷normal结果的余数大于半间隔 |
| rounded_up | 实际快捷normal舍入给截取significand加1 |
| carry_to_next_exponent | 实际快捷normal舍入产生唯一binade进位 |

每条路径保last_present及完整last：phase、angle_zero_based、index_zero_based、left_biased_exponent、factor_biased_exponent、result_biased_exponent、discarded_bits、integer_rounding_formed、rounding_relation、rounded_up、carry_to_next_exponent。

没有形成相应事实的指数或位数为null；没有发生整数舍入时rounded_up和carry为null，而不是虚构false。无任何实际调用时last=null。刚收到原操作数即记录当前调用，表示尚未计算首乘积；完整整数舍入已形成但最终指数溢出回退时，last保已形成的整数中间事实，同时phase明确原overflow回退、result exponent仍未冒作一个快捷返回。零分支result exponent=0，不冒normal运算或舍入已发生。

join沿原stage index顺序，last仅从实际last_present记录更新；不以worker墙钟完成顺序构造“最后一次”。原R561三路径十项及last、R550两路径十三项及last、R535十八项及原全部RootStats完整保留。不统计假想省去的原Q乘法次数，也不把来源准备时的计数0当运行覆盖。

在正常完整前缀可以用控制流解释计数关系，但异常、异步终止、未写完输出、未开始组件均保其实际范围，不能靠代数关系补未来计数。本条不记录全部科学数组或每项逐字trace，不用未知性能指标反填接受结果。

当前统计明确两个同时成立的事实：original_first_product_RN128_word_preserved=true；original_first_Q_multiplication_not_executed_on_shortcut=true。原R561对象中first_product_is_original_rounded_word仍正确描述它收到的字；不能把这个word命题误读为本条也执行了已被替换的首Q指令。

## 564.8 完整公开源码、生成源与逐字关系

本条三件发布来源：

| 文件（相对本题） | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_exact_lifted_factor_product.hpp | 10146 | bb4dfb08db7c4593afd93addb804a20876e0bb1facb1bc7e8a7e3f9aaeb40cc1 |
| computations/root_20261116_exact_lifted_factor_product.py | 19738 | 2f2cf734f2012d64ea5d19c1e8bed0ee95918b8e24fab0d4f8766ae0e174c0de |
| notes/R564-exact-lifted-factor-product-complete-source-plan.json | 13514 | cd4c90cbfc9e48acdd06a692885121627355df477955104981713d248cafca4a |

两件新C++视图仅Actions生成，不把展开文本重复入Git：

| 角色 | basename | bytes | SHA256 | literal数 |
|---|---|---:|---|---:|
| primal | root_20261116_exact_lifted_factor_product_primal128.cpp | 26887 | 5a13551c0d68f3e12577d2da9c096bfb340a27787ac5bf3b658cf6fb9973e798 | 7 |
| trace | root_20261116_exact_lifted_factor_product_trace128.cpp | 36019 | ed8c674215ffe1f94a65010d115447804d07812b7f5f70c387b080f56c140447 | 3 |

primal的七处是加入新header、加入新RootStats成员、原序join、三个首乘积调用点和完整统计序列化。trace的三处是包含新primal、诚实登记R561 ancestor与R564当前primal完整身份、完整新统计序列化；原所有方向正文未改。基线R561 primal26420 B/0e01b54b3b456711efd23ba94961eb669aef5394ab848e720fcf4a4ac64c854f，trace35787 B/07b8fd4dd7d31b2728e0f74a3ed9c9e6653593376529c12d26cdb57d617b8dc5。

完整plan内每一old/new/count=1按顺序要求唯一出现；正向结果核完整bytes/SHA，逆序逐个new唯一替回old后恢复整个基线。原Git源码不覆盖；新basename独占创建，若已存在只接受完整相同身份。这是来源关系，不是另加科学对拍或数值门。

R561祖先adapter实际为18526 B/9d954a23b1a8991c4aff38c1ffb6879229552cc9894ba70e7c3fb485fa928082；其完整plan13708 B/5667d987ea5b7387bb0c4f6c61d86cd9ea94035299da91d3c7889fb1cde5f5a7、header6760 B/e94b31dc091a8a727ab6f4808fb61e951cb892fc496120fe8312c82b7d71c0ac均由新plan完整绑定。这里19738是**本条R564 adapter**，18526是R561祖先；不能混淆两个来源身份。

R550 plan12303 B/14b5c02071359276be2988dc273d6864df3d61e728df10df5b1bddc498134457及R535 plan10232 B/f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b继续完整绑定；所有更深header、生成原件及adapter的实际身份由真正祖先接口验证，不能只保最外层hash就丢掉它们。

## 564.9 真正 source-only 准备及完整CLI

本条adapter只有在GITHUB_ACTIONS=true且GITHUB_REPOSITORY为公开Rogerhu12/math-research-public时执行，要求四个真实环境键GITHUB_REPOSITORY、GITHUB_RUN_ID、GITHUB_RUN_ATTEMPT、GITHUB_SHA。HERE是实际adapter所在computations目录；所有普通源必须在该同一目录、使用明确basename、非symlink、完整bytes/SHA匹配。计划路径也必须是实际普通文件且完整身份匹配。

实际caller持有本次新source准备目录，然后执行：

~~~bash
mkdir -p "$ACTUAL_CURRENT_SOURCE_PREPARATION/R564"
python3 -u "$COMP/root_20261116_exact_lifted_factor_product.py" \
  --source-plan "$TOPIC/notes/R564-exact-lifted-factor-product-complete-source-plan.json" \
  --average-source-plan "$TOPIC/notes/R561-normal-dyadic-average-complete-source-plan.json" \
  --reuse-source-plan "$TOPIC/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --word-source-plan "$TOPIC/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$ACTUAL_CURRENT_SOURCE_PREPARATION/R564/source-binding.json"
~~~

这些变量来自本次真实工作流，不能指向另一次run临时文件。binding-out以xb写新文件，父目录/既有文件/I/O失败必须如实保留。

prepare_sources的四参数为本条plan、R561 plan、R550 plan、R535 plan。它从实际已核完整R561 adapter加载来源模块，核module.__file__和其真实HERE，再调用实际R561.prepare_sources；R561内部真实调用R550，R550真实调用R535。所有祖先均**source-only**，不安装任何祖先compile hook，不调用g++或科学main，不给某root另开时钟。已有同字祖先文件按完整身份核，不作为旧run科学结果使用。

checked_ancestry核R561 schema/source_preparation_complete=true/compiler_completed=false及未执行科学求值的阶段旗标，同一四键run和同一个HERE，实际adapter/header/完整plan，以及R561计划中两个输出、R550/R535计划恰等于本条声明。然后真正调用R561.checked_ancestry取得并验证R550/R535完整binding与R550原plan。最后逐件核R561的两个原R550基线、原owner、原CPP、两个R561生成视图、三个祖先header、完整逆关系及未覆盖原件。

本层binding schema为R564-exact-lifted-factor-product-source-binding-v1；它保完整actual_R561_source_binding（其中完整R550/R535仍原样），四headers、四actual_original_sources（R561两基线、原owner、原CPP）、R564两generated_sources、primal7/trace3实际literal数、真实run/adapter/plan，以及准备/编译/科学求值的分别旗标。只有本次所有新源已写并核完整身份，才置source_preparation_complete=true；compiler_completed仍false。

## 564.10 失败、八个输出地址与原90KB读回

prepare_sources内部异常返回source child2和完整type/message/traceback。本次partial_source_state在完整计划可读时，从真正R550/R561/R564计划列出R535、R550、R561、R564各两件共八个生成地址，逐项返回expected、present、实际普通文件身份、complete_declared_identity_matches或完整read_error。计划本身读取失败则明确read_errors，不从预期列表补已经生成。

顶层require_actions、实际binding文件写入等不在这个捕获范围内的失败可能直接非零；后继caller必须保实际exit、stdout/stderr和存在范围，不能假定每次错误都有同样的binding JSON。source-only没有依赖下游科学组件成功。

完整binding按普通ASCII JSON和末LF写一次文件。实际≤90000 B时stdout返回R564_SOURCE_PREPARATION及完整正文；超过原90000 B时返回70，只输出实际bytes/SHA、source_child_returncode及complete_necessary_body_returned=false。完整文件仍在本次source目录；descriptor不冒完整body，不拆包或编码科学raw。

外层若读这个完整对象，必须从本次实际路径读取全文件并核身份，保完整祖先、错误和未生成范围。可能的本层70、祖先70与source child2都保各自原事实，不能因新外层读到完整文件就倒改旧层退出或false。未知完整必要体积不预称fit；原source和science两个语义scope仍各自90KB、超限70。

## 564.11 原 scope 一次直接安装及实际 compiler

### 564.11.1 真正安装位置

实际caller在原persistent owner真实globals形成后、原main首次编译前，调用install_owner_compiler(owner_scope,source_binding)。它要求_R564_SOURCE_BINDING、_R561_SOURCE_BINDING、_R550_SOURCE_BINDING、_R535_SOURCE_BINDING在该scope中全尚不存在。三个祖先只准备源，不能先装祖先再把本条叠在错误scope里。

重新核同run/HERE、当前adapter、四份plan和全部祖先、四headers、当前两源/两基线，原persistent owner完整原件，以及原CPP/ORIGINAL_CPP/TRACE_CPP名字。原compile_owner和main的__globals__必须都是这个真实scope；保原PINS中的原primal/trace祖先值。原post defer等独立接口仍由完整后继按自己的原顺序安装，不与本条来源安装混为一件事。

原owner是geometry_20261115_native_persistent128.py，43371 B/767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322；原CPP是geometry_20261115_native_persistent128.cpp，22364 B/7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd，二者整件未改。

### 564.11.2 完整编译函数与依赖

从原owner全文唯一def compile_owner起点到下一原def边界提取完整原函数；完整四条literal及全逆关系在新plan中：

| 函数 | bytes | SHA256 |
|---|---:|---|
| 原函数 | 3860 | be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d |
| 当前派生函数 | 6909 | 7c332e958280eaf84d18dbf60ab545c2cb6fbbb1f5eb8b533528415e647e83dd |

保全部旧PINS，再加入四header、四代各两件生成include、四adapter共十六依赖的真实SHA；把ORIGINAL_CPP/TRACE_CPP只指向本条新视图，deepcopy整个本次binding存入_R564_SOURCE_BINDING，再在真实owner_scope中定义新函数。定义尚非调用；安装receipt明确actual_compile_not_yet_called=true。

安装当前旗标literal_first_Q_multiply_preserved_at_all_changed_sites=false，而original_first_product_RN128_values_and_reduction_order_retained=true，另保方向正文和R561第二乘选择不变、fenv旗标等价不宣称。不能为了复用旧reader字面把false改成true。

### 564.11.3 真正原 main 和 g++

真正原main随后调用当前compile_owner。新函数先核十六实际依赖的完整bytes/SHA，然后沿原函数核原CPP、完整trace、原standalone main边界、完整evaluate observer和原行接点/逆关系。原persistent CPP、main、solve/replay、全部资源和数值逻辑保持。

g++仍为原gnu++17/O3/fopenmp/frounding-math/ffp-contract=off/fno-fast-math、原work/HERE include与lquadmath；原300秒编译上限、PGID/TERM/KILL/reap和stdout/stderr记录保持。原科学总钟及6000等内钟不重开或增加，准备/安装没有新科学数值门。

原生成include历史名仍为native_frozen_trace_variation128.inc；新record明确frozen_R283_numerical_prefix_is_byte_identical=false、only_frozen_trace_standalone_main_excluded=false。实际included_primal和included_trace是当前R564；原primal/R283/R535/R550/R561祖先分别具名保存完整receipt，不能只靠含frozen的文件名宣称原byte未变。

只有实际g++返回0且真实executable满足原检查，才写完整成功record。历史兼容键root_finite_word_cache_compilation_source_binding保整个R564 binding及所有嵌套祖先，再加真实command、include、returncode、executable、stdout/stderr及compiler_completed=true。嵌套source-only祖先的compiler_completed=false照原样保，准确界定各阶段；不虚构祖先另编译过。

新actual编译record也明确首Q指令并非全部保、其RN128值和原累加/root选择保、完整113×53或原fallback、方向正文/第二乘选择保及不承诺fenv状态旗标一致。编译成功只支付编译范围，不支付owner、replay、model、FD/fullDN或几何接受。

## 564.12 当前入口、必要消费者与剩余责任

完整后继保留为R565/request237，实际R566由amplitude唯一终态读取。它应从已正式R562/request236的完整417来源、63生成源和原全部输入/资源对象继续，新增本条实际源/生成视图及真正caller；不得改现有232/233/236运行或继承它们的求解结果。

正常和recovery必要reader必须读取完整新RootStats、三路径17计数/full last、全部旧统计；整个R564 source_binding及R561/R550/R535祖先；实际安装与真实编译各自receipt；完整原错误、未启动/未访/partial、资源及quiet/删除范围。旧具名八表可以保其原完整可逆关系，但未知新字段必须完整literal或明确完整逆，不能按旧计数字段白名单丢掉本条对象。

R561旧binding中“原首乘法执行”的source描述只属于其冻结source-only阶段；当前binding/编译/necessary不得传播为本次全部执行事实。也不能把“同词证明”表述为已经实际用两种实现对拍。本文没有做该实验，且完整纸证不等待新fixture。

全部M112/N2048、576stage、577节点/224 shooting state/每局部226含双mean、338×112混合响应、699×453、原owner32×10、root阈值/回退、同H128 tol/replay、同DN完整投影模型、原FD两组10方向×3step×2Richardson、原RMS/BC/域/merit及final fresh J/audit保持。19200总钟及6000/1200/8000/600/600/1800各原cap保持。

本条没有实际新run、真实分支计数、速度或可续接受父；没有宣称比通用Q乘法必快。正常输入有较小有效位的右因子只是结构性质，性能收益及真实资源前沿由后继原完整运行决定。数学上仍须本题README的同g闭C²强连续族、固定H、完整像保持/反射不全等、全t reach、全域metric和固定目标后的真实mesh/M/t精化；本条不替这些尚未支付的责任。

完整依赖见[R535](R535-original128-local-finite-root-words-and-real-compiler-hook.md)、[R550](R550-same-root-accepted-complete-evaluation-reuse.md)、[R561](R561-exact-normal-dyadic-average-and-original-first-products.md)与[R562正式完整入口](R562-request236-exact-dyadic-average-and-complete-projected-model-entry.md)。核心整数舍入定理已在本文逐步证明；来源计划完整给出全部literal和原/新身份，完整结论形成即发表，不增加独立审核、机械重跑或新的科学门。
