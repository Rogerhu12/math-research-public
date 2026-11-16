# R493：逐次真实 H 的 binary128 live response、准确投影与原完整 FD/fullDN 消费接点

作者：ChatGPT / exact_refinement（AI 辅助研究）  
日期：2026-11-16

**可信度：已证明，限本文的准确投影、条件接口组合及逐源控制流结论。未执行新科学计算，未实现或运行本文所列完整新 live 入口；没有把204/215四组件结果改写为原 native/fullDN 接受。**

## 1. 本次新增的具体结论

[R491](R491-original-native-fullDN-gates-and-complete128-response-consumption.md) 已说明原338行混合端点 Jacobian 可以被原消费者使用，原完整FD/fullDN仍须真实执行。本结论进一步定位可实现的逐次入口：原ac2fc返回对象确实公开了 `dn.tail.initial`、`dn.tail.evaluate`、`cells`、`graphs`、`gains` 和实际参数。因此新实现可以在每次实际请求H上直接形成原target/scales/初猜，调用原完整with-J评价，再以同次数据驱动R273、持久128 owner与所需最终组件。无需借用旧固定actual91探针，也不必先改造全部338行为解析导数。[S1–S7]

有三个已确认的源码接点，不能只靠更改schema掩盖。

1. 69c的原高度/父状态来源固定，204 bridge还检查 `native_call===1` 及初次迭代。它们不是任意H的live入口。
2. f13b的捕获只替换原 `correction(ev,states,target)`。ac2fc先完成evaluate，随后若norm已低于原容差便break，根本不调用correction。因此仅沿旧hook会漏掉零输入或其他已收敛初猜的完整响应来源。
3. 3788 frozen worker在原sourceSolve返回后还会以旧binary64 `actualSlopeJacobian` 覆盖first-slope和meanSlopeCorrection行。不能把128末态投影后再经过这层，继而声称返回的J仍是同次128组件的实际J。[S1–S4、S8]

最薄的新路径是明确的新worker/live方法和协议client。它保留原构造出的实际物理对象，直接调用已存在的公开evaluate；旧sourceSolve、旧probe及冻结运行入口均不改。新方法以原阈值、原完整行数和实际算术身份回答请求，再由原557f/c6a消费者真实执行FD、完整453求解、非线性尾回算及最终audit。本文给出此路径的条件合同和最小源码清单；新运行是否有资源完成、是否通过原门，均未预付。

## 2. 不能混同的维数和两种J

设本条原有限问题的模式数M=112，Q/Π形状维数K=224，stage数d=576，完整局部状态维数K+2=226。原spacing、角数、步数、cusp分段、cut/far、几何和字面系数均按真正配置绑定。

| 实际对象 | 完整布局与作用 |
|---|---|
| 持久射击节点X | 577个节点，每节点224词：112个Q与112个Π。原final-state.f128属于此布局 |
| 每stage的局部RK状态 | 完整226词：前224个形状变量及两个mean累积量。每stage由相应节点状态加原零mean初值进入 |
| 初次原64评价的形状J | 576个224×224矩阵，是当前H、当前初猜处原evaluate实际返回的模型系数 |
| 最终128 stage方向 | 每stage保全部224个形状输入方向，各方向返回完整226行；两个mean行必须保留。不是把输入方向数改为226 |
| 完整高度响应 | 全577节点的224×112响应，另保各stage两个mean输出的112方向贡献 |
| 基础端点jets | 338行，顺序为slope[112]、second[112]、meanSlopeCorrection、meanSecondCorrection、height[112] |
| 完整端点J | 338×112，列为声明的物理cut高度方向；原混合解析/差分行范围不减 |
| 全非线性残差 | cut112、576×224 stage行、far112，共129248行 |
| 独立最终audit | 原全部stage、query、完整角行及query后的实际primal advance；不能用端点J替代 |

特别地，577×224是节点状态资料，不是“577个完整226状态”。两个mean并非被删掉；它们在每stage完整226输出、方向及最终物理读出中承担原来的责任。[S1、S5–S7]

还必须分别记载两种J：首次原64 with-J形成固定的当前H chord/R273模型；末态128全stage方向形成最终边界敏感度。前者不是末态128的J，后者也不因覆盖完整便成为准确连续DN导数。原767a的 `FixedFresh64Model` 明确要求每个本次模型 `nonlinear_iteration=0,snapshot_sequence=0`，但按实际packet比较 `native_call`，没有把所有调用固定成call1。新方法每个真实call均重新支付这个初次模型；不得跨H复用旧J。[S5]

## 3. 每次真实调用的完整来源链

### 3.1 明确的输入与初猜

记第c次真实发送给新worker的原请求为

$$
\mathcal R_c=(H_c,\ \mathrm{jacobian}_c,\ \mathrm{audit}_c).
\tag{493.1}
$$

H_c是实际协议中的完整112个binary64值。其原词、负零位置、真正配置、source closure、run/job/attempt与call号单独保存。新schema必须标明新的binary128实现，不能伪造原ready中的旧endpoint/predictor方法身份。

原物理高度到射击target的有限运算顺序保留为原JS表达式

$$
t_{c,j}=\operatorname{fl}_{64}(H_{c,j}/(r^{\,4})_{\rm original\ JS}),
\tag{493.2}
$$

即原 `Float64Array.from(height,v=>v/r**4)`。不把它悄悄替换为先以binary128计算r的四次方再除。原scales的真实函数为

$$
\sigma_0=\max(10^{-250},|t_{c,0}|,\ldots,|t_{c,M-1}|),
\qquad
\sigma_{n+1}=\operatorname{fl}_{64}
  (\sigma_n/|\mathrm{gains}[n][0]|).
\tag{493.3}
$$

实现必须按原循环与表达式形成，不从旧snapshot恢复。该函数原为内部函数；最小新入口可明确复制这几行到新source并列完整diff，或由独立确定source view只增加命名导出。它不能声称原公开API已有一个不存在的 `scaleFor` 方法。[S1]

初猜只允许实际原 `initial(target)`，或真正可取得、明确来源的前一次状态所形成的warm。若使用上一call的128末态，经第5节投影得到的64节点仅是新call初猜；每个新H仍重新评价全部原方程。既不借上一call的residual/J/audit接受，也不从204/215已删除raw的SHA恢复状态。原tangent/amplitude predictor若被保留，必须使用真实可取得的对应数组；若新入口不用它，ready/记录不能继续宣称已经执行该predictor。

### 3.2 无correction捷径的首次完整评价

新live入口不调用原fixed探针，也不等待 `correction` 被触发。它在每次实际H上明确执行

```text
target := original height-to-target expression
scales := original scaleFor expression and order
states := actual original initial or explicitly bound warm
ev := dn.tail.evaluate(states, target, true, scales)
snapshot := complete current arrays and original returned scalars
R273 := original full current system and complete original-coordinate direction
packet := actual same-call trace writer and physical-query writer
owner128 := current packet + current fresh64 model
requested final components := same owner's actual final128 state
response := declared projection and protocol assembly
```

这是拟实现的调用合同，不是已经运行的伪代码结果。原evaluate的物理/有限性异常照常返回实际stage/rawCell/rawSegment；不由新层补齐缺失J或把异常当零残差。

即使原64 ev.norm已经低于原容差，新的128路线仍必须取得其真正当前输入与实际128结果。完整R273是本条明确选择的输入形成责任；它的模型误差或梯度读回不是另加的非线性接受阈值。旧correction-only hook的唯一替换证明不能用来证明这条新调用已经发生，必须以新entry/source与实call记录绑定。[S1、S3、S5]

### 3.3 可直接复用与必须新接的边界

61e2 `writeNativeTraceVariationPacket` 的实际 `currentIdentity` 已接受整数 `native_call>=1`，并把完整577行states/delta、target、scales、far、当前snapshot和call来源逐一绑定。824b物理packet又把同一primal packet、配置、所有physical queries/cusp advances和实际source receipts绑定；两个writer都不自行求root/RHS/J或选择旧状态。[S6]

因此“旧204调用点只准call1”不等于“packet格式只能表达call1”。保留generic writer即可，新的entry必须实际提供它要求的完整当前参数与数组。原writer固定的112/224/576、原literal阈值、方向及物理配置适用范围保持；本文不把它泛化成任意M、任意容差或另一个continuous-C族。

新call的共同身份至少包含：实际H原词摘要、完整数值配置、call、初次snapshot、当前R273矩阵/方向、两packet、128末态及其replay、各所需component的输入/输出receipt。所有component必须指向这一call的实际final-state.f128，不能一个取当前state而另一个沿旧H的boundary graph。

## 4. 条件组合命题：由实际当前状态形成可消费响应

**命题493.1（逐call有限组合）。** 固定一个符合本条原配置的真实请求。假设：

1. 完整原64基点和R273已经按第3节实际形成，原packet与新owner输入逐字绑定；
2. 当前128 owner完成其原完整残差/原阈值判定和原独立replay责任；输出的state、残差及全226输出均有实际本次原件；
3. 请求所需的最终stage/boundary/endpoint/audit按其已声明程序在同一末态完成；没有用失败或partial数组补齐数据；
4. 第5–6节的明确投影和组装得到真正协议payload，再执行原TailClient/SharedNativeClient的已有输入、finite、residual、当前H和请求项判定。

则该payload可作为本次新算术实现的有限native响应进入原FD/fullDN消费者；这一结论不需要新增“全部338行解析”的条件，也不声称fullDN随后必然通过。

**证明。** 第1项把H、配置与实际状态模型绑定。第2项提供本call的完整非线性末态，不能由另一call的完备性替代。第3项的stage与boundary组成在准确实系数条件下满足R491式(491.1)的全行关系；实际实现的readback仍按原数值记录，不私设新容差。endpoint读取同state及同boundary图，完整338行和338×112输出具有其原声明的混合方法身份；audit若被请求，则从同state独立完成其全原schedule。第4项对每个被消费值规定唯一表示，并执行真正消费者已有的分支。由R491所核原调用正文，所需字段可以进入affine boundary与完整fullDN，而其后仍有真实内层、非线性回算、RMS、最终audit和cut判定。因此只得到可消费性及来源条件，不得到后续数值接受。证毕。

本命题不是新增四项“验收审计”。这些是实际生产被请求数组和正常返回所需的来源/完整性条件；不另跑一套对拍、解析检查或残差阈值。未请求的audit不应仅因本结论而成为普通响应的额外前门；真正 `audit=True` 的最终调用必须支付原完整audit。若实现为了既有组件接口实际多算某部分，应如实记录，不能以该额外结果代替或改变原请求门。

原767a owner与204研究bridge中的 `native_accepted=false`、`fullDN_completed=false` 继续按各自原schema保存。新的live响应有独立的产生位置和backend身份；它的converged只来自实际新响应的原数值条件，不能反写旧实验flag为true。原64 worker受控停止也不被重标成原64正常接受。

## 5. binary128到协议binary64的唯一投影

### 5.1 为什么必须规定实际word投影

完整前缀/fullDN现有数值数组为binary64。若响应由binary128产生，必须把接口算术写明。直接把qstr打印的十进制字符串转换成Python float，不能在没有论证时宣称等于一次准确RN64；也不能把若干已分别投影的部分重新相加，当成原128总量的投影。

本路线选择从实际IEEE binary128 raw word或准确hex literal定义一次round-to-nearest、ties-to-even投影P。数组原件保留在Actions临时目录；协议需要的binary64是明确新表示，不覆盖128状态。

对一个有限非零binary128词，将其准确写成

$$
x=(-1)^s m\,2^e.
\tag{493.4}
$$

正规数的整数m含隐含首位，$e=E-16383-112$；次正规数没有隐含位，$e=-16494$。正负零独立保留。读取原raw时须遵守实际producer已经声明并检查的16字节、113位有效精度及little-endian格式，不对别种布局猜测。

定义整数nearest-even函数：若整数除法给$a=qb+r$，$0\le r<b$，则$r<b/2$取q，$r>b/2$取q+1，恰半时取偶数者。令$h=\lfloor\log_2|x|\rfloor$。当$h\ge-1022$时，以$2^{h-52}$为量子对$m2^e$作上述整数舍入；若进位成为$2^{53}$，正确移位并增加指数。次正规范围使用固定量子$2^{-1074}$，同样一次ties-to-even；可能进位到最小正规数。超过binary64表示范围按该舍入模式产生无穷大，随后交原finite分支报告失败，不能饱和或减小数值规避原门。

**命题493.2（投影唯一性）。** 上述整数算法得到准确实x的IEEE binary64 RN结果；保原零符号，负非零舍入为零时得到负零。若结果有限，正规区间给标准相对舍入界$|P(x)-x|\le2^{-53}|x|$，次正规/零区间给绝对界$|P(x)-x|\le2^{-1075}$；边界用相应相邻量子解释。

**证明。** binary64每个binade的相邻可表示数是所列量子的整数倍，且两端相邻binade连接时进位规则一致。整数商/余数精确决定最近者；中点的偶数规则与尾有效位相同。次正规集合是固定量子的整数格，过零和最小正规边界按同一规则连接。最大误差是所处格间距的一半，遂得界。零符号由显式符号支保存。证毕。

该界只论证一次表示投影，不是整个root、ODE、J、DN或原fullDN的误差界。尤其不能从此推出投影后的J等于投影响应映射的导数。

### 5.2 不以投影替换原门

设owner末范数为原128词$\nu$，原tolerance是实际原binary64字面lift。原owner的$\nu<\tau$保留；协议还真正使用$P(\nu)$执行TailClient已有的严格$P(\nu)<\tau_{64}$。若投影恰落到边界，旧门可以拒绝；不能使用nextafter、epsilon、向零截断或把owner布尔代替消费者比较。

checkpoint.cutHeight保存本次实际输入H，而jets.height保存实际端点height词的P投影。两者不可强设相等以隐藏真实cut残差。原SharedNativeClient对请求H的检查及最终cut消费者已有的源/容差继续运行。

完整协议负零不能经过一次会将-0改为0的无说明重编码。可由明确投影器产生保留-0.0的JSON并由worker直接转发其原文本，或使用实际binary64字词载体在client还原；实际选择须写入新schema和来源，不把JSON.stringify的原行为冒成原词保持。大payload只在Actions内管道/文件传递，不作为90KB必要摘要搬回。

### 5.3 需要补齐的实际scalar序列化

a090的338基础rows与338×112混合J已经有raw128文件；meanSlope/meanSecond总量及cut五scalar目前主要通过36位qstr报告。最小新source view只在真实计算位置增加明确scalar word输出，保原表达式的括号、运算次序和字面输入。[S7]

推荐字段就是原真实 `cut_original_jet_scalars` 的13个名字：radius、backgroundSlope、backgroundSecond、E、Ep、meanSlope、meanSecond、minLeading、minD、endpointFullD、endpointPhi、formalCurvature、original_C_radial_solve_readback。mean totals必须取原128相加后所得词；不能在64端重新由background与correction相加。具体实现可在原计算处将同一表达式结果绑定局部变量，并使报告与新增raw都读取该实际值；这是新的序列化source身份，不声称未编译的新文件与旧机器码逐词相同。

audit的完整aggregate已有实际Q变量，可直接保存原8个原协议scalar及原C-solve读回的raw/hex；不可把partial的min/max补成完整。owner.norm与mean_height_sum已有准确binary128_hex，可由同一投影器读取。没有必要为此重算root、改变物理公式或另做完整角审计。

## 6. payload的逐字段实际来源

以下是新正常响应必须真正组装的字段，不是由summary推测的目标形状。

| 原消费字段 | 同call的真实来源与处理 |
|---|---|
| residual | owner final完整norm的准确word，经P；保128原词与原below-tolerance记录 |
| converged / failed | 当前求解与请求内容真实返回；不拷贝旧probe的实验flag |
| jets.slope / second / height | endpoint的cut-original-program-jets.f128，按第2节完整行序切片后P |
| 两个meanCorrection | 同一338基础rows的两个标量，分别P |
| meanSlope / meanSecond及cut字段 | 第5.3节同次新增scalar word输出，经P；不在client重组另一公式 |
| heightJetJacobian | complete-mixed-cut-J.f128完整338×112，经P、原row-major展开 |
| heightJetJacobianMethod | 明确原first-slope/meanSlope trace与其余原symmetric行；不沿用全部解析文字 |
| audit | 当前audit=True时的同state完整原audit与实际source；原有限采样范围、错误与覆盖保留 |
| checkpoint.states | 本call577×224实际末state的明确P投影；128原件独立保留 |
| checkpoint.cutHeight | 本次实际输入H；不是从返回height反解 |
| checkpoint.parameters / rawNode / rawStates | 实际当前原配置与索引；rawStates是原rawNode对真实节点的选择，不是另一次求解 |
| history / progress | 本次128owner真实方向、全部原trial、接受、失败、资源停止；不填成旧64迭代历史 |
| 算术与输入receipt | 当前H、两packet、首次模型、末state、replay、组件、投影source和实际返回payload的完整身份 |

原TailClient会把实际返回写入本job记录，再检查完整finite、形状、原residual与请求项。新client应保这个顺序和原异常语义；构造阶段ready的source/backend元数据须独立声明，不能伪装成旧 `fourier-root-and-product-moments-v1` 的逐词执行。

非audit同H的缓存只能沿原TailClient实际相等判定与请求J可用性工作；命中记录属于旧真实call的缓存响应，不能编造一次新solve或新replay。audit=True仍送真实请求。没有被命中的新H，必须执行第3节全新来源链。

## 7. 最小独立源码切点与真正消费者调用

本节给出完整可实施的source分工，不把尚未写出的模块列为已发表文件。

| 新的最小作用点 | 具体变化 | 保持的既有数学与责任 |
|---|---|---|
| live worker/entry | 新ready身份；每个真实H走公开evaluate和新bridge；正常返回本callpayload；不经过3788的旧J覆盖层 | 原物理构造、root/flow对象、当前H/warm定义、完整配置及原失败 |
| current capture/bridge视图 | 从f13b捕获与完整R273路径提取实际输入形成；用新entry源证明替代“唯一correction替换”声明；去旧fixed-H/call1限制 | 原十数组、全部cut/stage/far、原方向系统/QR/eta，snapshot不额外求RHS |
| per-call128 owner组合 | 每call完整新packet/model/out；复用原767a/7789及实际四组件数学；编译产物可只读共享，状态/模型不能跨H冒用 | 原32方向、十档、2e-9字面、root停止/物理域、独立replay与完整原未访 |
| scalar-export source view与assembler | 第5节raw标量、P及第6节完整payload；新的算术/schema/byte identities | 原338混合J、C-based physical program、完整226/mean、audit原schedule |
| 显式Python client/112入口来源视图 | 新source/ready绑定，保原solve检查与同一owner；让557f实际调用它 | 原actual_boundary_fd、original_full_solve、c6a/完整banded正文及最终cut |

前三项可由小的确定source generator和已声明的唯一literal替换形成新basename；每个base完整SHA、替换次数、生成源实际SHA、实际HERE及传递依赖都要真实绑定。不复制一个巨大私有目录来隐藏未绑定依赖，也不通过修改旧module的全局变量或假报 `__file__` 越过来源检查。旧研究入口的fixed actual91条件原样保留；新入口的适用H必须由真实参数接线决定。

557f已有明确 `--tail-client` / `expected_tail_client_sha256` 与 `load_client` 注入位置；其SharedNativeClient包装同一个真实client。新的完整入口必须真的调用：

1. 当前完整场endpoint产生H，真实新client.solve(H,jacobian=True,audit=False)；
2. 原三扰动/原全部方向与步长的actual_boundary_fd；
3. original_full_solve中的原完整453内层与原Newton/17档；
4. 每个更新endpoint的新H真实回算，原true-BC/RMS判断；
5. 实际最终H的jacobian=True,audit=True和原seam/cut审读。

这条接线不以新增数学predicate决定是否调用fullDN；原已有有限性/域/FD/容差和资源分支照常。FD检查的是实际显式affine边界与完整链式法则，不把它解释成准确非线性DN导数证书。原RMS1e-6、BC1e-11、FD5e-5及其完整contraction判定保持，全部112、338、453和两mean不减。[S8–S10、R491]

## 8. 预算、停止和raw生命周期

新的live session只能引用入口实际指定的一条绝对job/science deadline。每个call、R273、owner、组件、响应组装及原FD/fullDN都扣同一剩余时间；不能每次H重新启动总钟。204的单点资源计划、208的18000秒与连续C分支18900+2700等不同入口合同不能互相挪用。后继入口须明确选择它自己的原来源和总预算；本文不凭纸面接口预填新的额度或完成保证。

同一client串行持有本次call目录。只有科学消费者实际接收payload、来源与必要错误读回完成且对应owned子进程已reap/quiet，才能退休该call不再被任何预测器/消费者引用的raw。要继续作warm的实际state必须留真实原件或明确已形成的投影，不能只留SHA。编译文件共享须与只读source/编译身份相符，不能使另一call写入本call对象。

完整状态、J和角表只在Actions本job供科学读取；原必要摘要仍一份不超过90000B，记录每个call的原门、全部trial必要值/失败地址、组件完成/未访、错误、原schema和文件身份。不能为了通道便利把完整338×112或577×224数组拆包/编码搬回，也不能以摘要成功冒完整科学完成。若超限或中断，明确transport partial；若无法证quiet，明确跳过删除。

旧研究组件由于预算/错误只形成partial时，新正常协议必须返回实际失败或未完成，不用shape期望补数。不同层的stop保原地址：owner iteration/trial/stage、stage direction/RK位置、boundary列、endpoint列、audit query/advance、fullDN迭代及最后未访调用。没有返回的普通响应，不得被写成“尾已收敛而只缺一份摘要”。

## 9. 本结论支付和保留的边界

已经支付的是：固定旧probe不能直接成为live入口的源码原因；原实际evaluate可重入的最小方法；correction-only与旧J覆盖两个确定接点；全部维数与同call来源合同；一次准确binary128→binary64投影的构造和证明；必需scalar word补口；原FD/fullDN的真实调用路线。

尚未支付的是：新worker/client/assembler及整个后继的最终冻结source closure、实际Actions执行、任一新H的数值返回、原FD/fullDN接受及其完整末场。本文未从215hash恢复数据，未运行新科学，也没有把完整数组读取、全解析或独立对拍设为新门。

即使未来有限fullDN通过，它仍不自动证明无限尾、准确隐式根、连续C族、连续Fourier/RK误差、闭面共同g、全部t的metric/reach/held。后续研究按原数学对象继续；不能用本条正常协议组合取代这些责任。

## 10. 精确来源

本表列本次纸面/源码读取的固定字节。数值正文均未执行；原fullDN详细门已经在R491逐源列出。相同basename的其他稿不能代替这些身份。

| 标识 | 固定文件/真实作用点 | SHA-256 |
|---|---|---|
| S1 | [78718-tail-tangent-core.mjs](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs)：公开evaluate/initial、内部scaleFor、solve前置break、cutJets/J/audit | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |
| S2 | [geometry_20261115_native_word_first_current576_solve.py](../computations/geometry_20261115_native_word_first_current576_solve.py)：固定原H/父来源 | 69c9a8d5cccfcfdcdda35c475b089609c789747803a7b363a17fb67c5bae28d0 |
| S3 | [geometry_20261115_original_r273_tail_client_hook.mjs](../computations/geometry_20261115_original_r273_tail_client_hook.mjs)：当前十数组/QR及correction唯一替换 | f13b0a0d3f7e6d3487f0eda92dc9e76117137ee106c9f33471e762e35c9106e0 |
| S4 | [geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs](../computations/geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs)：单call1、原64受控停止 | 718f1c475b4722eaddeae9eb5bf610c438f2a0c221a7e26e10850fbf00126471 |
| S5a | [geometry_20261115_native_persistent128.py](../computations/geometry_20261115_native_persistent128.py)：FixedFresh64Model、当前owner/replay | 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322 |
| S5b | [geometry_20261115_native_persistent128.cpp](../computations/geometry_20261115_native_persistent128.cpp)：实际128状态、全残差/226输出 | 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd |
| S6a | [geometry_20261115_native_trace_variation128_bridge.mjs](../computations/geometry_20261115_native_trace_variation128_bridge.mjs)：generic currentIdentity与原packet writer | 61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7 |
| S6b | [geometry_20261115_native_final128_packet.mjs](../computations/geometry_20261115_native_final128_packet.mjs)：同call物理packet/原schedule | 824b7440d2604e828df4326b1cef1b1bf332d203eeb7e81968704d2febdcd7c2 |
| S7a | [geometry_20261115_native_physical_final128.cpp](../computations/geometry_20261115_native_physical_final128.cpp)：基础338、完整混合J、实际scalar/audit | a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 |
| S7b | [geometry_20261115_native_final128_components.py](../computations/geometry_20261115_native_final128_components.py)：同state/owner/call/run绑定 | ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045 |
| S7c | [geometry_20261116_native_simd_stats_qualified_final128.py](../computations/geometry_20261116_native_simd_stats_qualified_final128.py)：当前qualified四组件launch | e5c85e6bf5e864de39b0675f997c716466ead0dd158a6c22b73c714257e7433f |
| S8a | [tail_frozen_worker.mjs](../computations/tail_frozen_worker.mjs)：sourceSolve后原64 slope覆盖 | 3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054 |
| S8b | [exact_20261114_true_tail_client.py](../computations/exact_20261114_true_tail_client.py)：ready/solve/cache/原finite门 | 1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09 |
| S9 | [geometry_20261115_six_control_height_continuation_full112.py](../computations/geometry_20261115_six_control_height_continuation_full112.py)：SharedNativeClient、actual_boundary_fd、original_full_solve | 557f3aab83116c1d8eef83e4c83306e8058749ccdb56b2ec8808effd2e16bf21 |
| S10 | [geometry_20261114_full_dn_solve.py](../computations/geometry_20261114_full_dn_solve.py)：原完整消费者正文 | c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 |

R273两核心分别为3557608524becae2bbf1c2100af12c865082329efccbd5078008cb2c8591c101（current576 system）与d5d9874242499df7a79fe4411a420de0cfe8464c64c80dd9c18ec501d226a296（chain QR）。后继选择复用这些数学体时仍须完整来源闭包，而非只列本节几个文件。

