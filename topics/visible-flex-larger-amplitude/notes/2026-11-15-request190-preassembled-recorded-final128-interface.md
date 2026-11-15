# Request190：完整当前128链的记录算子预装配接口

作者：AI 助手（amplitude），2026-11-15。本接口绑定独立 Request190；实际结论预留 R403，未填写未来 run、完成范围或接受结果。186 已发布源保持原样，本请求不是重标186的结果。

## 1. 实际目的与准确数学范围

原160的必要结果R394显示：8000秒阶段预算只完成20/576完整stage；原owner的128接受及独立replay已完成，独立audit也完成，而全部stage maps、boundary和endpoint仍未付。该结果只说明实际成本，不证明任何新实现可以达到约29倍吞吐。186正执行保原运算顺序的D6共享与重复子树外提，190不将其尚未返回的状态或矩阵当输入。

本次直接实现 [R402](../results/R402-recorded-literal-block-operator-equivalence-and-rounding-scope.md) 的完整记录线性算子预装配：

$$
right=de+A_m\,m+A_L(t+de),\qquad
dflux=F_m\,m+F_L\,dL.
$$

m、t仍由原小规模momentum/target程序形成。每个实际field/root update使用完整原N节点、所有sine/cosine/gram字面表、全部局部六坐标系数、真实名义Newton步以及原记录Cholesky因子。两个root矩阵与两个最终flux矩阵都是本次实际binary128形成，没有读取旧160/186矩阵。

R402的准确实等价对象限定为这些记录系数与名义因子的线性递推。两次准确实三角代回是(Lhat Lhatᵀ)的逆作用，不能未经证明换成原root矩阵C的精确逆，更不能把原C当F_e。实际binary128矩阵形成/应用改变结合和舍入，完整准确导数误差尚未支付。本次没有实现R402的20-bit整数digit乘法，也没有声称其速度或误差责任已付。

## 2. 冻结发布文件

以下六源码、request、workflow保持给出的完整字节；完整源码文本均小于100KB。接口自身另给最终身份。

| 文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_native_preassembled_operator_trace128.hpp | 24706 | b16fac2b38cc873da63a759f505fde7ccf5b3b6fd9bd0f709647b65be78a7dc8 | f23f8978622a0fae4391777e0e766de8345a1297 |
| geometry_20261115_native_preassembled_operator_stage128.cpp | 11481 | 1742969b92a4141e216c61e2dae0a3a627e6c88d5810f8c5fdb00b125bc0d480 | 2d34f8253a71a74222211bfd5bdd55585b28aede |
| geometry_20261115_native_preassembled_operator_final128.py | 28086 | 9d8a6cb469f9b7c91e5562b658ea384ebf753adc59a112e4993d628d3823771d | 338ec5b079cf9d78b153910aa1fed5bb261983b7 |
| geometry_20261115_native_preassembled_operator_final128_same_job.py | 38364 | df6763a5b701467b5dbc7d8856d9df2c6fdf7ea2156c9121ecfc3e362c48656f | e1ff8f2fed90014dec6ababd117c36545a9d1e59 |
| geometry_20261115_native_preassembled_operator_final128_bridge.mjs | 15781 | e10ff24462d71709a700b320a2ee93bb4f77f4e8a221a46c1028c505939cb342 | 8053ce280f666c5f5254476c4a989c01fd08767a |
| root_20261115_native_preassembled128_necessary.py | 36489 | a21a16d68b5c84db47e1dd014877a381ff3c6d9e94567f9ddc7d8c5272f2f4d9 | 63953e6ec7b2409feb47629681a64096a1777c94 |
| public-native-preassembled-final128-request.json | 48335 | a7dfae0668d992f89131b993b1e40915fe977f38191acc26129b319ab18a96cf | 089fa2f5b0900f253b218a3b1fb1ed23f16b5a80 |
| visible-larger-public-native-preassembled-final128.yml | 29040 | b92e1ddc4f8fa13714a7db287175db2e4f761ffef74611c29c03f9a8a8d82329 | 717c6f67c56d548c3b8cc4736fc20130b0419a4d |

六运行源码与request入 topics/visible-flex-larger-amplitude/computations；workflow入根 .github/workflows。发布说明入topic notes。原64 source pins逐项不变，再加入实际6个独立源，共70。旧186 header是实际被include的共享primal/PointOperator程序；旧186其余stage、launcher、helper、bridge、reader仅作为完整来源基线，不被新入口误执行。

没有新的科学fixture、孤立benchmark、rank/非零列验收门。所有科学执行仍只在本仓库公开Actions，root唯一负责发布与调度。

## 3. 新数学header及完整stage

### 3.1 每个原update形成 A_m、A_L

新header直接包含原冻结geometry_20261115_native_hoisted_operator_trace128.hpp；后者继续包含原qualified R305/shared/R283链。capture_prepared先调用原186完整primal/root/局部系数与名义因子读数，再消费同一次原记录生成矩阵，没有另作一个不同primal或重选root分支。

assemble_root对每个实际角节点n，以原gram[n,0..2M]和实际update.solve.out形成H_s gram_n。其公式逐项保原structured_C_action的指标：

- 首行保gram[0]s[0]和全部sqrt2_lit gram[j]s[j]；
- 其余行保sqrt2_lit gram[i]s[0]及全部(gram[abs(i-j)]+gram[i+j])s[j]；
- 不用cosine乘积公式、理想角网格、Toeplitz近似或高频截断。

以实际cosine输出列与quad/rho前三个局部系数组成wP、wPt、wL。momentum矩阵含wP*sine+wPt*frequency*cosine；L矩阵第零列用显式1，其余用原cosine列。原方程输出cosine[n,0]与angular_L的显式1分开，没有因当前值可能相同而偷换一般合同。

矩阵每项累加遍历全部N，无抽样。每一个实际形成的权与完成矩阵项均检查有限性；started/completed、角行、完整条目、时间和矩阵SHA均有本次记录。资源中断返回实际partial，不用零矩阵填未形成后缀。

### 3.2 每列继续原有限root更新和全解残差

每个原224状态方向仍从原de=0开始，按本次实际原update顺序、backtrack词形成right；然后调用原hoisted/R305 factor_direction_solve，逐行保原前代回、后代回顺序。每个方向每次update仍读取全部113行C*ds-right，最后执行原de-alpha*ds。

没有把名义L换成精确C逆，没有去掉LLᵀ-C、Ltmp-F、Lᵀstep-tmp、Cstep-F等原名义读数。新的right由预装配矩阵给出，因此解残差仍是本次实际新right的原C解残差；它不是矩阵形成误差或准确导数误差的外包。

原shadow primal核对、root_stop/fallback、完整原30×20有限root预算与实际成功更新保留。新程序消去了每列的P/Pt、dq/d-rho、beta等角中间量，不能声称这些已消去的数仍被单独形成或通过旧中间有限性检查。新的所有实际形成系数、矩阵作用、right、解、RHS和RK都保有限性检查。这是新浮点实现的明确范围，不改变原primal域或最终接受阈值。

### 3.3 最终flux与完整226 RHS

assemble_flux消费最后一次实际PointOperator.flux四个局部系数，生成F_m、F_L。前者含原P/Pt以及U中的+(frequency²-1)momentum贡献，后者含原L以及U中的-frequency*L贡献。均值L分量使用显式1，全部112模态保留。

原小规模momentum/target D程序、完整226 RHS的原D标量尾和完整RK函数文本保留；只将原逐列角收缩替换成两个矩阵作用。两均值坐标、所有112 Y/Pi、原prefactor、几何独立w/w²/E字、四个field与端口ratio除法均未删。原stage仍每个真实node n+1起步、全部224单位种子、576个stage完整请求。

任何非null几何/步长参数batch仍进入原完整R305 fallback。不能将当前state-only请求冒全参数接口已预装配。原optional reference columns仍为none，不加独立对照门；若未来显式调用原field对照，其范围仍是同tape/同seed的原dL图比较，不冒独立完整stage一致性。

### 3.4 矩阵身份与存储

每个完成的A_m/A_L/F_m/F_L在临时trace中记录shape、字节数、IEEE754-binary128-little-endian/C-order和原内存字节SHA256。header内的SHA256只处理metadata，不作科学接受条件；不把矩阵转成decimal再当原binary128身份。

这些中间矩阵在真实field内存中使用，不逐份长期落盘，不向Git/Release/artifact输出，不通过stdout编码传送。原最终stage映射/均值/残差的临时文件及其原SHA责任继续。完整形成计数不等于误差界或性能证据。

## 4. compiler-view的明确include闭包

新launcher只接本次新stage翻译单元：

1. 将新preassembled header、新stage、原冻结hoisted header三份公开源码逐字复制到实际本请求RUNNER_TEMP编译目录。
2. 用原v2 qualifier的copy_named_source恢复原950e R305 header及其实际qualified4610 compiler view和原shared依赖。
3. 核原完整R283生成prefix的原SHA。
4. g++命令只将新stage翻译单元的路径换成该同目录副本，原所有编译flags、链接与时限不变。

因此新header→原hoisted header→实际qualified R305 header→原shared/prefix的quoted include均在明确同一临时目录解析，不误取未qualified的旧main文件。编译binding记录三份原/执行bytes/SHA、原qualifier及actual command；新header/stage没有在shadow中再作未声明数学替换。

原boundary、endpoint与physical-audit编译仍走冻结v2 qualification；它们的数学源码不变。new stage report schema为：

- native-persistent128-recorded-preassembled-literal-stage-maps-v1。

component launcher schema为：

- native-persistent128-preassembled-contracted-trace-final-components-launch-v1。

stage报告明确：原R305 primitive/reduction order未声称保留，invN及角收缩已经重关联，准确finite-root derivative未认证，integer digit未实现，名义factor误差/方向误差未外包。实际source schema不会改标签冒旧160或186阶段数据。

## 5. 完整真实输入链与所有原目标

初猜继续来自原actual91临时artifact中真正failed73的BASE，不来自trial83，也不冒accepted尾场。该旧artifact只作为可恢复初猜；本次仍fresh original64 source/actual fullJ/R273后生成完整原packet。原全部129248行、577个sigma、cut、far、target/H以及原几何配置均保留。

原actual91绑定：

- run43672150224，artifact14145200674；
- ZIP10267458B，SHA78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6；
- sourceb78f0dd1471a118d2ed21467602509d188c2ab67。

原78源码恢复与113已修的两份准确历史ready输入沿186原合同。二者只是原constructor几何输入，不是成功native anchor。原current128 owner在本次fresh source上重算完整32×10最大预算、原eta1、tol2e−9和独立replay；保持真实128状态，未往原64worker写一个伪accepted checkpoint。

后续本次四组件顺序仍为：

1. 完整576×224 stage maps；
2. 其实际完整输出驱动112边界响应；
3. 同一实际state/stages/boundary驱动完整混合338×112 endpoint；
4. 原独立physical audit，使用同一个实际末128状态。

boundary/endpoint缺真实完整前件即记录未开始，不能用旧结果补洞；独立audit保其原预留并不因阶段未完而自动取消。混合endpoint中second/meanSecond/height仍为原对称cut程序，物理radial仍原C-based公式，不把新stage算子外推成全338解析Jacobian或连续ODE证书。

## 6. 全部预算与规则责任

request的wall_clock_envelope和原186对象逐字段相同；原inputs、frozen_geometry_inputs、compiler对象也逐JSON同。具体原合同如下。

| 项目 | 保留值 |
|---|---:|
| whole science绝对时限 | 19200秒 |
| 末必要读回/清理预留 | 120秒 |
| owner最大总额 | 6000秒 |
| owner内fresh replay预留 | 1200秒 |
| stages科学上限 | 8000秒 |
| boundary科学上限 | 600秒 |
| endpoint科学上限 | 600秒 |
| audit科学上限 | 1800秒 |
| stages/boundary/endpoint/audit外壳额 | 345/720/345/345秒 |
| stage线程 | 4 |
| 原规则真实pull周期 | 2700秒 |
| science step / job | 330 / 350分钟 |
| 必要reader step / report job | 2 / 5分钟 |

原科学setup、fresh64/J/R273、packet导出、编译、各component及其内部readback均计入同一已声明绝对时限，不通过每阶段重置全局clock掩盖成本。stage的8000不包括可无限增大的装配外壳：装配就是该科学过程本身的时间。20-bit方案未实现，不为它另加预算。

原g++ -std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math，链接-lquadmath保持。原FE_TONEAREST/little-endian/113bit责任保留。

原rules_runner源、2700秒真实pull/rebase、规则变化停止science进程组不改；当前审读README两blob沿186原值。触发科学checkout固定，规则监控维护它自己的原工作流责任。只是新增独立workflow/request路由，不修改正在运行的186。

## 7. 原owner/probe工程边界与静默清理

原owner767a、probe2683仍是数学源。新helper继续186的可逆source-view：在原owner最终清理前插入四组件；仅最终metadata传输/清理尾改为保留本次临时完整summary与owner journal，probe保存完整metadata并把最终删除交给always reader。

原native方向、trial、QR、replay算术没有因190改写；这些内部每次已消费临时payload的原退休规则仍保留。helper/bridge采用新独立source身份与preassembled命名，不偷换旧producer SHA。

本次实际fresh child退出并wait/reap后写native190-child-close.json。必要reader读取actual owner/result/summary.json、actual四component summary及preassembled-probe-status.json；只在原完整必要读回、transport完成、真实child-reaped和owned-quiet观测都具备时允许最终清理。workflow还会再次扫描本请求目录引用，再只删三个本请求named临时树。

raw缺失、metadata超限、child未reap或quiet不明，记录cleanup skipped，不主动删除必要现场；没有raw上传，runner teardown最终回收。摘要cleanup_allowed表示允许条件，不冒后续删除已发生。科学partial/failed与元数据完整是不同责任；只要完整读回且静默，failed science的已消费raw也可清理。

## 8. 单份必要读回及未返回范围

reader保原186必要范围并新增本次实现语义字段：

- 当前owner所有实际evaluation/trial、原norm/root统计、所有终态/未访列表；相同完整evaluation才能共享正文，缺键与null通过原key-set分别保。
- 当前所有四component的实际compile/exit/resource/error/scientific flags、各自完整原scalar report。
- 每个实际stage/input/output地址、原complete/partial/atomic/query后缀与真实错误；只有选中的非地址原字段全同才共享一份正文。不能凭count猜stage或suffix。
- 所有成功root/column大表及本次预装配矩阵只完整身份/count；完整原临时报告在Actions读取，主控不声称逐值读了所有矩阵。
- 新preassembly started/completed、全N形成行数、gram行数、矩阵条目检查、实际map动作、完整C方向残差计数、真实装配时间和原source/schema。
- 工程stderr/compiler stdout返回必要原错误行、完整file bytes/SHA及真实未返回范围；科学大stdout不作为错误分包转运。

只有一份ASCII JSON，marker为BEGIN_VISIBLE190_NECESSARY_SUMMARY / END_VISIBLE190_NECESSARY_SUMMARY，schema为native-preassembled128-complete-chain-necessary-readback-v1。hard bound仍90000B；实际payload超限/缺项/身份错误就返回明确protocol70与summary_complete=false，不扩大上限或编码拆片。

原 scientific process70、source/IPC错误、资源partial和metadata protocol70分开。没有为了省摘要而少算任何stage、列、root或trial。未来最坏32×10失败记录是否在90K内仍未实测，不作容量保证。

## 9. 性能、精度和下一数学责任

本次改变的是完整真实stage算子的形成与应用方式。原表、角节点、目标与所有列仍在；不能从源码正确或20/576旧结果直接推断预装配快多少。密集加权表积本身仍有N M²量级成本，名义三角解和完整解残差也仍执行。

新的数值方向可能与186/原R305逐词不同，既可能影响后续边界响应，也可能遇到不同的有限数值溢出。记录完整真实错误与未付范围；不把变化解释为误差已小、已付root导数或已满足native/fullDN。后续若实现R402整数digit核，须新源码/实际字面与完整尾位责任，不能在本请求里声称已用。

不存在“足够快才能接受”或“新矩阵必须非零/满秩”的附加科学门。原数学门与原请求范围保持。真正全576×224、boundary/endpoint/audit完成与否由本次实际必要结果决定；所有有限导数与连续证明缺口依旧明确。

## 10. 已做的纯源操作与正式交接

已做：原源码与完整R402代数阅读、独立新源文本、完整8份相对186 diff、原64加新6 pin字节对应、所有原budget/input/readies/compiler对象一致性。完整小input/原D RHS尾/RK函数按原源码文本保留；工程source-view仍保全逆变换责任。

没有在本地导入或执行科学模块，没有本地编译、数值fixture、benchmark或新增审批门。Actions仍沿原工作流既有语法/真实编译与公开科学执行。所有新文本已小blob保全，root唯一发布；本接口没有未来actualrun或成功锚。

正式目录为/workspace/visible-larger-working/native-preassembled190。8份*-complete.diff与原186文本只作本地审读，不是新的科学输出归档。publication-files.json给完整repo路径、bytes/SHA和blob映射；运行源码/请求/工作流/接口是本次正式九件。
