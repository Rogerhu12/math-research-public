# R383 — 准确R323目标的同一性、coast控制责任与中心速度必要带

作者：ChatGPT /root/exact_refinement、/root/amplitude（AI协作）；2026-11-15。

**原165的38条准确速度域反证适用于169初始九参数及179已冻结recipe所声明的同一准确R323目标；它们不是另一个目标构造的反证。** 这项传递基于完整来源、参数语义、R323窗口及准确C定义的相同，不能以独立运行的result或definition文件SHA不同否定，也不能把准确结论改贴为字面IEEE程序的证明。

原数值分片416从源码确定为negative-speed-coast。其准确内部直接受p3、theta3、eta3三项控制；仅在前一过渡段增加新控制不改变该准确段，也不通过总长产生间接变化。进一步，准确coast中心速度只依赖theta3、coast长度与固定kappa，得到下文完整必要条件。本结论没有代入新的LC数值，没有断言该中心恰落在某条已读反证叶中，没有证明全搜索无解，也不增加任何科学运行前置门。

## 1. 已完成的实际读取与固定来源

实际165及176r2范围分别见[R356](R356-actual165-finite-target-bound-and-strict-speed-domain-refutations.md)和[R381](R381-actual176r2-complete-strict-refutation-locations-and-readback-recovery.md)。这里继续完成原源码和参数身份比较；不重跑区间、工厂、C、native、FD或ODE。

| 对象 | 实际固定身份 |
|---|---|
| 原165请求 | public-continuous-nine-shared-target-enclosures-request.json，16401B，SHA256 6beff06bb6ffdd9604b936016635b3cf47adbf45181b266f7b0a85743a60f7c3 |
| 原165来源 | run43736208020，commit1f2ec637430e5c6b27b1a93720e106539281a156 |
| 原165consumer | root_20261115_continuous_nine_shared_target_enclosures.py，94125B，SHA256 61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205 |
| 准确工厂 | geometry_20261115_continuous_nine_scalar_factory_v3.py，42270B，SHA256 0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e |
| 原R323实际构造入口 | geometry_20261115_continuous_nine_v3_actual_construction.py，20377B，SHA256 738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0 |
| 独立数值编译 | geometry_20261115_continuous_nine_scalar_numeric_v3.py，SHA256 7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60 |
| 169已发表请求 | public-current-C-projective-full453-physical-DN-request.json，37078B，SHA256 41ccd38061cbf561cc6751cc220a272c9dc24723f088b2826e046ff62d740ff3 |
| 169已发表recipe | current-C-projective-full453-physical-DN169-recipe.json，9940B，SHA256 f8f6b353458f04052940a05bbe28d28c48b0050f631f76f813267924a31d4765 |
| 169所读来源 | de9a730a8f9cf8ea1f3e31fa6f6dd9cfb64e1d80 |
| 179已冻结recipe | current-C-riccati-full453-physical-DN179-recipe.json，10294B，SHA256 d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811，blob3f2387cfb05f041308304462796284d314121320 |

最后一项只是已核的冻结recipe；本文没有取得或编造179实际运行号、成功状态或完整未来输出。

原165consumer的rebuild_actual重新用真实core、recipe和cut叶调用build_expression，逐字段比较完整definition及其canonical序列化；不是仅相信一个自报model SHA。169请求与165的三原输入完整字典、原query、实际C工作参数和共同19源SHA已逐项比较；九系数、原参数来源、seed及active/frozen对象亦已比较。

## 2. 数学输入相同的具体内容

### 2.1 完整core、准确C与原cut

原core输入仍为accepted M96 prefix：

    accepted.json.gz
    2614352B
    SHA256 b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff

原selected geometry canonical SHA256为bf7b3c997d12599d08e2415cb41392a9dc72ffd33993aa169f1c146796858706。它提供准确core系数与末端jet，不能据此声称这个旧场已经解新目标。

准确C仍由原f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df入口、004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea单位面板实现及9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed原生产者定义。target_model_schema仍为R286-original-stored-continuous-model-convention-C-v1，deep_definition为original-exact-root-family。

工厂cut绑定要求完整原C前提、所有许可原根族的统一包含、原实profile及C不变、原cut不被重归一化；使用完整点叶的E、E_r、E_rr hull。它们是准确语义叶的包围，不是把三个独立浮点中点当作新cut数据。

共同原query身份为1303B/SHA256 4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59。原config与两ready输入的完整字典相同；实际C预算同为明确3600秒。预算是计算资源身份，不是目标函数的另一种数学定义。

共同原cut为

$$
R=\frac{5404319552844595}{18014398509481984}.
$$

### 2.2 原R323窗口与支撑

原147原子请求仍为17398B/SHA256 4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707。同一738dd构造入口选择并原样记录[R323](R323-finite-cut-boxes-and-explicit-uniform-dyadic-windows.md)窗口；165与169实际所记均为

$$
\delta_A=\delta_B=\frac1{1024},\qquad
d=\frac1{524288},\qquad
\kappa=\frac12.
$$

原core_end、core内部第一支撑由同一真实core及同一select_recipe形成，保原left和stored_width的有限字词语义。这里没有改用另一套默认支撑，也没有由数值右端点减法重新定义准确宽度。

同一recipe明确root_choice=R286-dovetailed-rational-middle-third。其工厂包围同时覆盖全部许可原根序列，因此不会把另一独立运行的更窄或不同外包围误当作目标本身的改变。

### 2.3 全九系数及实际活动坐标

顺序固定为

    [p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]

原字面为

    [0.3055213835477326,
     0.21645013203050154,
     0.34270051957744246,
     -0.06322334619266512,
     -0.01747451701873286,
     0.9376115689625685,
     1.0751306255033548,
     0.6886900390922872,
     0.9385431607625546]

这些都是JSON number。相同工厂的rational(float)使用Fraction.from_float；字符串分支则使用Fraction(string)。已核169/179没有把这九个number换成仅显示相同小数的有理字符串，因此没有悄换准确dyadic系数。

169/179保active=[0,1,2]、frozen=[3,4,5,6,7,8]，即原p1、p2、p3可在真实后续评价中变化，六个shape系数在该接口内固定。本文的反证传递指这个已选初始九元组；不把它扩大成所有以后可能改变的active参数。

## 3. 准确目标传递命题及证明

**命题383.1。** 固定完整core、core_end、cut、准确C定义与所选根规则、全部R323长度/速度常数、第一真实支撑及九个准确系数。若两个入口均使用上述build_expression定义的准确目标，则对于每一个共同许可C实例，两入口的准确半径a(s)、准确总长L及公共坐标目标a(Lu)相同。某一完整外包围已对这个许可族在闭区间U上证明a_s下界≥1或上界≤−1，该反证也适用于另一个入口所声明的同一准确目标。

**证明。** 原core的全部分片及末端jet由相同输入和同一准确kernel确定。cut三叶E0、E1、E2具有相同语义和根规则；对任一共同许可实例，它们的准确值相同。工厂的v、b、q、两端jet、过渡积分、coast长度、四追加分片、总长及三个支撑均由同一有限表达式图确定；给定相同九系数，全部补偿多项式也相同。因此a、L以及u↦a(Lu)逐点相同。

原165以包含所有许可cut值的完整外包围计算，且每个u查询枚举全部可能的准确分片与支撑，未将切片选择缩成某个未经验证的单支。其有效a_s界包含上述每一个许可实例的真实值。若整个界位于[1,∞)或(−∞,−1]，对应开放条件|a_s|<1在U上失败；换一个具有相同定义的入口不会改变这个事实。证毕。

这项命题不要求独立运行的result、definition序列化文件或cut外包围逐字相等。它们可有不同run、runtime路径、来源收据、工作节点和有效外包围；这些变化不自动改变准确定义。反过来，同一个名称或几个相同浮点参数也不足以证明定义相同，第1—2节的完整身份责任不可省略。

准确目标与literal numeric reference仍是两种不同对象。原419片数值参考以存储字词、其本身的锚和宽度、原lookup分区定义；不能把命题直接宣称为IEEE求值程序的误差证书，也不能把numeric中点系数当成准确C叶。

由第1—2节已核身份及命题383.1，[R381](R381-actual176r2-complete-strict-refutation-locations-and-readback-recovery.md)的两个闭区间反证适用于169初点及179当前已冻结初点的准确R323目标。它们不是另一family上无关的旧反例。原R381的38条严格反证与其它工作宽度未决继续分别保留。

## 4. 416的确切分片身份及不能越过的范围

原consumer强核总numeric piece数为419；CompleteTarget.__init__同时强核最后四个准确分片名依次为：

| 原零基索引 | 分片名 |
|---:|---|
| 415 | first-velocity-transition |
| 416 | negative-speed-coast |
| 417 | last-velocity-transition |
| 418 | canonical-cubic-cut-collar |

此前全部保为core-*；数值编译保同一pieces顺序及全部系数映射。因此R381的numeric_piece=416有明确源码含义，不能再说其所属构造段未知。

但这个标签是原数值参考固定分片的索引。准确查询的位置是Lu，原consumer仍枚举所有可能的准确分支；边界不确定时可有多支。176r2的必要38表没有返回accurate_possible_piece_indices，故本文不声称每个反证叶已逐项证明“只命中准确coast一支”。反证本身来自完整准确a_s包围，传递命题也不需要这个更强的单支断言。

下节的控制公式是对真实准确coast本身的精确陈述；它不把numeric标签和准确唯一分支偷换。

## 5. 准确coast上三个直接系数的完整公式

记准确core末点为s_A，末jet为R_A、v_A、b_A。工厂定义

$$
S_1=s_A+\delta_A,\qquad
I_A=\frac{\delta_A(v_A-\kappa)}2+\frac{\delta_A^2b_A}{12},
$$

$$
I_B=\frac{\delta_B(-\kappa+v_B)}2-\frac{\delta_B^2b_B}{12},\qquad
L_C=\frac{R_A-R_B+I_A+I_B}{\kappa}>0.
$$

总长为

$$
L=S_1+L_C+\delta_B+d.
$$

九项控制都是相应支撑端点的C²零jet补偿。它们不改变以上末端校准，故S1、LC、L及基底均不依赖九系数。

准确coast支撑恰为[S1,S1+LC]。令

$$
t=\frac{s-S_1}{L_C}\in[0,1],\qquad
B_j(t)=64t^3(1-t)^3(2t-1)^j,\quad j=0,1,2.
$$

原参数映射是index=3·order+support。于是准确coast完整半径及导数为

$$
a(s)=R_A+I_A-\kappa L_Ct
+L_C^2\{p_3B_0(t)+\theta_3B_1(t)+\eta_3B_2(t)\},
$$

$$
a_s(s)=-\kappa+
L_C\{p_3B_0'(t)+\theta_3B_1'(t)+\eta_3B_2'(t)\},
$$

$$
a_{ss}(s)=p_3B_0''(t)+\theta_3B_1''(t)+\eta_3B_2''(t).
$$

这保全部三项、真实宽度因子及同一个局部坐标，没有把有限差分或单独profile slope冒作准确导数。

另外六项分别作用于严格位于core内部的support0或第一速度过渡的support1；它们在准确coast上为零。若新增系数xi的支撑也固定在support1，且同样为零jet、不改变原校准，那么xi也不直接改变准确coast；因为L与LC不依赖这些系数，它也没有通过总长产生间接coast变化的渠道。

这不排除新控制通过完整求解使active p3后来取到不同真实值。那时p3项确实改变coast，必须按新实际参数评价；不能沿用初点反证当作所有后续点的结论。

## 6. 中心速度必要带：完整证明与实际未计算范围

**命题383.2。** 对任一固定准确C实例及其LC>0，在准确coast中心s_c=S1+LC/2有

$$
a_s(s_c)=-\kappa+2L_C\theta_3.
$$

因此整个准确coast满足开放速度域|a_s|<1的必要条件是

$$
\frac{\kappa-1}{2L_C}<\theta_3<
\frac{\kappa+1}{2L_C}.
$$

**证明。** B0关于t=1/2对称，所以B0'(1/2)=0；B2也对称，所以B2'(1/2)=0。直接从定义得B0(1/2)=1，而B1=(2t−1)B0，故B1'(1/2)=2。代入第5节的完整a_s式即得中心恒等式。LC>0允许除以2LC，将−1<−κ+2LCθ3<1等价整理即得必要带。证毕。

这一带只是一项必要条件，通过它不证明整个coast、其它分片或完整目标域通过。若要对全部许可C实例作统一域证明，必要条件必须对每一个对应LC成立；用一个任意中点替代完整LC族不合法。

在169/179的active=[0,1,2]接口内，theta3冻结，p1、p2、p3的变化不改变中心速度；eta3也不进入中心式。新增仅在support1的xi同样不进入。这个不变性是原表达式的精确作用范围，不是一次有限差分或数值秩估计。

本文**没有**执行以下计算：将实际LC界代入中心式、计算中心公共u、把中心与R381的38叶比较、证明当前theta3已越过必要带、寻找新的coast系数、判断全搜索无解。R381已证明的是它给出的闭u子集上的速度域失败；中心命题是独立的解析必要条件，不能把二者未经实际计算拼成更强结论。

## 7. 原保存字段足以怎样继续真实coast计算

下一项公开Actions可以消费原165已保存的小元数据和必要原输入，无需为取得coast参数重跑完整C。必须区分准确对象、有效外包围和字面参考。

### 7.1 原完整result中已有的字段

原105512B result，SHA256 e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619，原日志label为complete-target-result。其

    shared_calibration_and_literal_defect_binding

包含：

- exact_lengths：kappa、d、da、db的准确有理字符串；
- positive_coast_width_grid：准确LC的有效320位外包围；
- intersected_accurate_length_grid：准确L的有效外包围；
- exact_core_RA、exact_core_IA；
- expanded_length_coefficients的constant、v、b、q；
- 三组全部系数的准确合并多项式及原声明范围。

顶层accurate_total_length同样保L界。LC、L在这里是准确表达式对象的有证区间，不能叫作已经得到了某个精确点值。176r2的55100B必要摘要故意没有重返整个shared binding；它的缺省不代表原105512B result中不存在。

若已有原definition正文，S1可由core_end+da准确恢复。若只消费上述result及原input中的R，利用已给constant定义也可在Actions按

$$
S_1={\tt constant}-\frac{\delta_B}{2}-d
-\frac{R_A-R+I_A}{\kappa}
$$

作准确有理恢复；这是第5节同一校准恒等式，不替换cut叶。本文仅给公式，没有本地执行这项科学运算。

### 7.2 原input-binding中确有完整cut叶，但没有所有输入正文

原input-binding62398B，SHA256 996593f3a615c3694596463c949990a4967cc5c5a1bf48b100fbc4e149e73e48，原label为complete-input-and-rebuilt-definition-binding。其中

    original_tail_binding.actual_cut_twojet_enclosures

包含完整原E、E_r、E_rr ball记录；相邻字段还保original_binary_cut、selected_complete_query、semantic_leaves以及原C/config/全点叶来源。这不是仅剩三个SHA。

但actual_recipe、actual_definition和actual_core_input主要是收据与选择身份，不能从这些hash捏造原recipe、definition或core geometry正文。完整原recipe另在738dd入口的complete-construction-summary中，以actual_recipe字段保留；原165实际该摘要27207B，SHA256 6ff7fb33455be8dbc4eef1eb819a8f7b90329c8575c442dc810c83db13117fb8，含最后LF。

工厂definition正文未由该wrapper直接打印，不能假称已从其receipt完整恢复。若后继需要重建完整model，可在Actions用固定历史core正文、上述实际recipe、完整cut叶及原0d893工厂重建；input中all_definition_fields_rebuilt_and_exactly_compared保原逐字段canonical SHA，供明确的原结构身份对照。新参数点必须形成新的参数/definition身份，不冒原165接受或原definition逐字相同。

### 7.3 运输、计算及停止范围

原1.48GB官方日志只允许在Actions内流式扫描；本地不取整份日志或拆传大科学表。恢复旧JSON及核字节是读回操作；中心、coast界、新参数或新域的任何乘除、区间与多项式计算都是新的科学操作，只能在明确的新公开Actions中进行。

后继可选什么算法由相应新任务定义；本结论不规定某一未执行参数、不替原full3目标或native门、不承诺一次修域成功。原C完整族、九系数、全部支撑、同一cut及完整域责任都应保留；读回/工作预算不足须保真实partial，不以参数文件或原收据冒新实际结果。

## 8. 对当前路线的明确影响

169初始准确目标的严格速度域问题是真实已付证据，不能再仅归为原165的粗盒未决。相同初点、相同准确目标换一个sampler或native方向，本身不会消除这项标量域反证；这些算法仍可研究其它责任，但不能把初点叫作已证明的准确可行目标。

在新的明确参数变化中，coast三系数是实际作用于这段的控制。仅给第一速度过渡新增xi不能直接修正这一段；原active p3能改变其一般位置，却不能改变冻结theta3决定的中心速度。下一实际计算应保这些区别，读回新真实参数、全部域结果和未付责任，不把本命题升级为不存在可行解或不存在BVP解的证明。

本结论不改任何已冻结科学源、原终检、当前运行实例或接受阈值；也不等待另一数值审核作为发表条件。171、175等独立原任务继续按各自完整scope执行及读回。
