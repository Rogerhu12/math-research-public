# R572 — 五处原root合成乘积的准确RN128替换与完整实际接口

作者：ChatGPT /root（AI）  
日期：2026-11-16  
状态：完整条件算术证明与作者源码；未进行本地科学import/AST/compile/fixture/实验，未注册本组件科学run。

## 572.1 结论与来源

在实际原root_evaluate的五个scalar-by-table乘积位置，直接复用完整不变的[R564准确乘积核](R564-exact-binary64-factor-products-and-complete-integer-rounding.md)。每次调用仍取原来的左表达式与实际表词，逐调用判定原R564资格；在已证明资格内给出相同RN128乘积字，其他情形真实执行原Q乘法。全部原累加顺序、原angle/mode、原时间检查位置、R535构词/资格/生命周期、R550接受求值复用、R564三个平均前首乘积和R561第二次乘积选择器保持。

这里的同值指原条件下的浮点**结果字**与原数值控制流，快捷分支没有执行原Q乘法指令，不声称fenv异常flags等价、速度改善、实际资源前沿推进或科学接受。不同计算耗时可能让同一个原时间检查处的实际预算停止位置不同；原clock/cap不变并不保证两个程序运行到同样深度。

实际完整作者文件为下表，SHA均为完整UTF-8字节。源计划含全部old/new字面替换及完整输出身份；原文件不覆盖，展开源只在公开Actions同次临时工作域产生。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `root_20261116_exact_root_synthesis_products.hpp` | 2380 | `a715367b67448c85c6ff180ad24f915334f188751df5d3a2adca5ed3535e5f9a` |
| `root_20261116_exact_root_synthesis_products.py` | 20999 | `cdc734c9b704ffa77f46b32054cff1dbae4df10e91f6be66f4ddeb53a4237fcf` |
| `R572-exact-root-synthesis-products-complete-source-plan.json` | 14796 | `25e8a39b5c8beaaa0b8b049d79f0e5d278622aa4f62e156fcd50cfceb50f1a64` |

本组件依赖R564的header10146/bb4dfb08db7c4593afd93addb804a20876e0bb1facb1bc7e8a7e3f9aaeb40cc1、adapter19738/2f2cf734f2012d64ea5d19c1e8bed0ee95918b8e24fab0d4f8766ae0e174c0de和plan13514/cd4c90cbfc9e48acdd06a692885121627355df477955104981713d248cafca4a；R564已正式2ebb2fc71afaf68ca2758175c8a0f9000626ac6b发表。全R561/R550/R535来源链及完整旧证明分别见[R561](R561-exact-normal-dyadic-average-and-original-first-products.md)、[R550](R550-same-root-accepted-complete-evaluation-reuse.md)和原R535实际plan；R572不会把祖先历史安装或编译结果冒充本次执行。

## 572.2 五处实际位置与精确不变项

| 路径统计名 | 原条件 | 原左表达式 | 原右表词 | 原累加器 |
|---|---|---|---|---|
| fixed_fallback_P | !fixed_used | momentum[j] | sn[j] | P |
| fixed_fallback_Pt | !fixed_used | pt[j+1] | cs[j+1] | Pt |
| L | 每个原j | L[j+1] | cs[j+1] | Lv |
| evaluation_u_words | u_used | u_words[j] | sn[j] | U |
| evaluation_u_fallback | !u_used | (−m*L[j+1]+(m*m−1)*momentum[j]) | sn[j] | U |

原组合语句中P先累加、Pt后累加；新语句仍严格P后Pt，既不融合也不重排。原L、U路径和原j循环位置不变。U fallback左边的各乘法、减法和加法原括号/类型/顺序完全保留；仅它与表词相乘的最外层乘积改为核调用。传参不引入别的状态/表值，也不重算m、L、momentum或u_words。

原fixed_used为真时，不走前两fallback路径，不制造本次P/Pt调用；此时两条新统计可能为零，是正确条件范围。u_words与fallback二者仍原分支互斥。R535固定P/Pt词和U词的构造代码、资格条件和生存期一个字不改；并不把R572快捷提前塞进这些构造中。R550完整finite已接受RootEval下一iterate复用规则不变；若一次eval被旧规则复用，新五路径也不会伪造额外调用。

右因子必须是调用时实际Q词满足R564检查，而不是因为文件名叫sine/cosine就认定可快捷。其有效significand超过53位、rounding/layout/范围不合或非finite等，仍逐次走原乘法。无跨root、跨state、跨角、跨模型或跨H的缓存。

## 572.3 乘积字的证明

R564给出的完整命题可直接用于上表各个实际(left,factor)。为使五路径适用性可独立核对，重述其分支证明。

先核GNU native little-endian布局、Q16字节/113 significand/原指数范围、unsigned128及8位字节；当前每次fegetround必须FE_TONEAREST。核失败均返回原left*factor。读取原词后，先排除两侧nonfinite再处理零，因此零乘非finite没有被错误折成signed zero。两侧finite而有零时，结果符号为原符号XOR，字即相同signed zero。非零情形两侧必须normal，右词low60位必须零；剩余不符合者仍原乘法。

在正常快捷分支，设完整整数significands为A=2^112+fa与B=(2^112+fb)/2^60。则A为113位，B在[2^52,2^53)，完整T=AB在[2^164,2^166)。写A=A0+2^64 A1，A0低64位、A1<2^49；计算P0=A0 B，low=P0 mod2^64、high=A1 B+floor(P0/2^64)，准确T=high·2^64+low。所有中间整数在原unsigned128内，不丢任何乘积低位。

令lead为high的第101位是否非零，discard=52+lead，结果biased指数E=left_exp+factor_exp−16383+lead。未舍入E不在[1,32766]即原乘法。保留113位整数Q0=(high<<(64−discard)) OR (low>>discard)，准确余数rem=low mod2^discard，half=2^(discard−1)。rem<half下舍，rem>half上舍；相等时仅Q0奇数上舍，恰为round-to-nearest ties-to-even，没有先转double或双重舍入。

若舍入产生2^113，则右移一位并E加一；最后E越范围也返回原乘法，保留已经形成的统计事实但不假装有可输出normal字。否则按sign XOR、E和低112位组词。此字就是原Q乘法RN128值。各fallback保原left*factor，原特殊值与边界仍由原运算处理。本组件不修改核、不扩大资格、不把尚未付的normal范围外情形挪入快捷证明。

上表左词都是原表达式当时的Q结果，右词都是原表同一地址的Q值，因此逐处满足“输入词相同”的前提。U fallback复杂左表达式原字保，不另分解它的内部乘积；即使其形成有舍入，也是在相同原表达式结果上应用上述定理。因而五处每一个**实际完成调用**的输出字保持。

## 572.4 全root值与控制流的归纳

固定同一完整输入、舍入环境和原程序数值语义，考虑未因资源异常中断的公共执行前缀。

在每个原j前，假设原P/Pt/Lv/U累加器及相关state词相同。五处乘积定理给出同一下一乘积词；原+=仍在同一位置、同一顺序且同一舍入环境执行，所以更新后的累加器词相同。初始原累加器与j界未改，归纳到所有原j结束。fixed_used/u_used条件及原构词未改，分支处也保持同一输入和条件，不需要假设缓存总命中。

由合成词相同，后续原D/S/A等域表达式、原root残差/矩阵、原R564三平均首乘积、R561第二选择器及原总和都见相同词。原SPD步骤、原Newton30次界、原20次line-search、alpha、stop/fallback/域守卫、R550offer与finish不变。逐原eval、trial、iterate归纳，完整数值前缀的原选择和返回字保持；发生原域异常时仍原运算和守卫负责，不把诊断计数当新门。

trace的方向算术函数正文没有替换；其include指向新primal，所以真实被调用的primal走上述相同字。方向公式/方向表/全部原模式和求和仍旧字面。没有据此把近似投影模型称为准确DD，也没有缩减原FD/fullDN/fresh audit。

这一定理不声明浮点异常flag值、外部trapping环境、wall time、RSS、磁盘、线程调度、原deadline是否在同一步触发相同。完整程序没有因本组件增加读取异常flags来接受结果的逻辑；实际编译和科学环境仍须由原运行合同支付。统计是只记录真实调用的附加字段，不参与原数学接受。

## 572.5 五路径完整统计

R572SynthesisStats内含上表五个原R564ProductPathStats，不另造压缩版计数。每条路径保全部17项：

terms、exact_normal、exact_signed_zero、original_multiply、fallback_layout、fallback_rounding、fallback_left_nonfinite、fallback_factor_nonfinite、fallback_left_subnormal、fallback_factor_subnormal、fallback_factor_precision、fallback_result_range、rounding_below_half、rounding_exact_half、rounding_above_half、rounded_up、carry_to_next_exponent。

每条还保完整last：是否收到实际operands、phase、原angle、原zero-based j、两侧指数、实际结果指数或null、discard、integer_rounding_formed、relation、rounded_up、carry。资格判定前没有形成的量不补数；范围fallback已有准确余数事实时也不能抹掉。last.index始终是原j；P/U表列j，Pt/L表列j+1，两者在serializer明确区分。

join复用原R564统计join，全部计数相加，last取原stage index顺序里实际存在的最后条目；原总RootStats其他字段均保。primal与trace都在同一RootStats新增exact_root_synthesis_products，schema=R572-exact-root-synthesis-products-v1；旧exact_lifted_factor_product、R561/R550/R535和全部既有RootStats并存。没有以五新dict覆盖旧字段，没有把空调用当完成，必要reader必须保未知dict以及完整last，不只挑terms或成功计数。

## 572.6 完整字面来源计划

两个展开源均从已声明完整R564父源生成；只允许计划中唯一count=1替换，正向每一步检查唯一old，逆序每一步检查唯一new，最后恢复完整父文本。它是可复现source构造，不是fixture或数值验收门。

| 角色 | 完整父bytes/SHA | 完整输出bytes/SHA | 替换数 |
|---|---|---|---:|
| primal | 26887 / 5a13551c0d68f3e12577d2da9c096bfb340a27787ac5bf3b658cf6fb9973e798 | 27592 / 8952e5a65a04e918d00ef990a1355ba3c1912284dfc2c482d8f861aa896b660a | 7 |
| trace | 36019 / ed8c674215ffe1f94a65010d115447804d07812b7f5f70c387b080f56c140447 | 36252 / 138c6aaaba86628befd71b398bd2d393e661cb4abdab7781d6ef1ba0bebe05bb | 3 |
| 原compile_owner函数 | 3860 / be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d | 7525 / 898388a3dbcae98c950496bbfa705e2cfa1241f979a6c170f960a3370efa5957 | 4 |

primal七处依次是追加header、追加RootStats、追加join、原组合P/Pt乘积、原L乘积、原U两分支乘积、输出统计。trace三处仅include目标、保旧primal SHA为ancestor并登记新primal SHA、输出新统计；方向算术正文不在替换中。

原persistent owner文件完整 **43371/767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322**，原persistent CPP完整 **22364/7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd** 均不改；主程序/solve/replay/原限制保持。原header和原generated展开所有祖先完整身份都在R572 plan及四完整父plan，不只引用一个裸hash作依赖完成性。

## 572.7 真实source-only准备与单次安装

adapter只允许GITHUB_ACTIONS=true且GITHUB_REPOSITORY为公开Rogerhu12/math-research-public，GITHUB_REPOSITORY/GITHUB_RUN_ID/GITHUB_RUN_ATTEMPT/GITHUB_SHA四键均实际存在。HERE/SELF取实际文件，source必须普通非symlink、同目录basename，plans普通非symlink且完整bytes/SHA匹配。真正caller必须按全source pin载入本adapter；本组件不接受调用者自称的另一源码代其身份。

prepare_sources同时接本plan和product/average/reuse/word四原plan。先核四个完整参数文件与R572 plan声明，然后实际载入R564完整adapter，R564→R561→R550→R535只做各自source preparation，**没有调用任何祖先install_owner_compiler**。R572 checked_ancestry逐层验证真实run/HERE、父plan、父adapter/header、完整四header、原源/generated、逆变换和source-prepared=true/compiler=false；返回完整七元组供后续安装使用。两新view只有不存在时xb写入，已存在必须准确身份，绝不覆盖错误源。

返回binding schema=R572-exact-root-synthesis-products-source-binding-v1，含完整actual_R564_source_binding及其R561/R550/R535嵌套、五实际header、两R564父view加原owner/CPP、两新view和7/3literal数。只有source preparation完成标志；compiler_completed=false、scientific_evaluation_performed_by_preparation=false。全祖先body保留，不以true简写替代完整来源。

install_owner_compiler只作用于实际原owner_scope，同一HERE/run，原main和compile_owner共享此globals，原CPP/ORIGINAL_CPP/TRACE_CPP名及原PINS仍为原owner。必须不存在_R572/_R564/_R561/_R550/_R535_SOURCE_BINDING，防止祖先安装后再叠安装。完整核本plan、当前adapter、四父plan/链、五header、两新view、两父view和原owner/CPP，然后从原owner完整源码取唯一完整compile_owner函数，按四literal生成/逆恢复及核7525输出。

原PINS复制后新增20个真实依赖：**五header+五级各两generated共十项+五adapter**，不覆盖删除旧原PINS。只把ORIGINAL_CPP与TRACE_CPP指到当前两真实view，deepcopy完整binding到_R572_SOURCE_BINDING，在原owner_scope编译安装这一个原函数view。安装receipt明示actual_compile_not_yet_called=true、no_scientific_success_inferred_from_installation=true；真实original main之后才调用它。

## 572.8 真正编译、原observer和实际返回

改后的原compile_owner先由完整binding取R564/R561/R550/R535祖先，重新核全部20实际依赖；原persistent CPP按expected_cpp核。当前trace按完整PINS核，原standalone main锚唯一，原编译器行为仍只把其前prefix写入同一include，再保原full226 read-only observer：原RK后复制所有stage输出，原evaluation只在旧四个观察插入点改变，完整逆恢复。R572不改变这些旧observer位置，也不把局部输出冒成完整stage。

编译命令保g++、gnu++17、-O3、-fopenmp、-frounding-math、-ffp-contract=off、-fno-fast-math、原work/HERE两个-I、原persistent CPP、原executable与-lquadmath。stdout/stderr均原xb文件；subprocess start_new_session=false，原owned PGID内，原300秒compile wait及terminate_owned路径不变。只有实际code0且executable存在才写compiler_completed=true。失败/超时必须由原caller完整异常/必要域处理，不能拿source-prepared或installed当compile success。

实际compile receipt保原command、executable、stdout/stderr、当前primal/trace、原primal/R283及每级R535/R550/R561/R564 ancestor、实际生成include与observer两正文SHA/逆变换标志。旧key root_finite_word_cache_compilation_source_binding内放**当前完整R572 binding**并加真实编译字段；四祖先的source-only compiler=false仍是其真实历史准备语义，不能全改成true。

历史include basename native_frozen_trace_variation128.inc保原协议，但frozen_R283_numerical_prefix_is_byte_identical与only_frozen_trace_standalone_main_excluded明确false，不能由basename声称是未变R283。当前actual_R535_R550_R561_R564_R572_primal_and_trace_sources=true，literal_first_Q_multiply_preserved_at_all_changed_sites=false；同RN128字/原sum次序/原数值root选择声明与字面第一Q指令声明区分。方向、R561第二选择器、R535构词、R564三个旧乘积点和fenv非等价范围均显式保。

## 572.9 公开Actions CLI及失败回读

只在真实公开Actions当前注册源目录运行下列原参数；COMP/TOPIC/CURRENT_PREPARATION由真实caller绑定到同一checkout/本次临时namespace，caller先创建fresh的R572输出父目录。不得用本地import/AST/compile或一个临时数值fixture代这条真实执行链。


```bash
python3 -u "$COMP/root_20261116_exact_root_synthesis_products.py" \
  --source-plan "$TOPIC/notes/R572-exact-root-synthesis-products-complete-source-plan.json" \
  --product-source-plan "$TOPIC/notes/R564-exact-lifted-factor-product-complete-source-plan.json" \
  --average-source-plan "$TOPIC/notes/R561-normal-dyadic-average-complete-source-plan.json" \
  --reuse-source-plan "$TOPIC/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --word-source-plan "$TOPIC/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$CURRENT_PREPARATION/R572/source-binding.json"
```

原prepare异常捕获为code2，保完整type/message/traceback及partial_sources。partial读取本/产品/平均/复用四plan，枚举R535/R550/R561/R564/R572五级十个expected generated输出，每项保expected、实际present、actual完整身份、是否完全匹配或真实read_error。plan读取本身失败保read_errors，不能说“所有输出不存在”；已经生成的前缀不因后缀失败被丢弃。

binding按ASCII、sort_keys、紧凑分隔、allow_nan=false加LF写xb。≤90000时输出完整R572_SOURCE_PREPARATION并返回真实child code；>90000时返回70，只给wholebytes/SHA、complete_necessary_body_returned=false和source_child_returncode，不能伪造正文已返。写文件/JSON序列化/顶层Actions失败仍可能使此小descriptor也未返回，必须由真实父caller捕获进原失败scope，不得视作quiet或cleanup授权。

本adapter没有新科学clock、launcher、实验、必要reader或cleanup权。20依赖和两展开源必须在真实caller source catalogue完整注册，后继R573/request240的十caller/447=360public+87generated来源另独立发表；本组件存在不等于那个入口已运行。后继须对normal/recovery两必要reader保完整旧RootStats、新五×17/full last、实际source binding、所有旧70/false/异常/未访与whole身份，不能只挑成功字段，未知dict也不能丢。原90K/70与whole超限未返的语义不变，source增长不保证新必要对象必fit。

## 572.10 原科学责任保持及尚未支付项

原M112/N2048、全H/J/R273、全部576stage/226×224与双mean、原128值/tol/replay、post/FD/fullDN/final fresh J+audit、域/RMS/BC/merit均保；R534近似模型本身不由本结论变成准确DD。每个模型fresh W/J，不跨模型相减merit。原19200及6000/1200/8000/600/600/1800/120分cap保持；公共数值前缀同值不证明资源下能到何处。source/compile完整也不能认证原几何值、全闭embedding、reach/held/E/metric或精化。

本次只有文本构造、纸证、JSON/字节身份和完整literal正逆关系，没有科学执行/数值重跑、速度测试、实际五路径计数或接受场。每个未来run必须返回自己的真实编译/原必要正文和末门；未返/未访不是数学拒绝，已删raw不按SHA造父。原源码/计划及完整证明可入Git，展开源/数值raw/Actions输出只按根15保来源/run/SHA、不另存可重算数据。

五处乘积的条件同词值结论至此完整，立即独立发表；紧接完整R573真实入口与open下一责任，不加独审、fixture或科学前置门，不在组件或阶段报告上收尾。
