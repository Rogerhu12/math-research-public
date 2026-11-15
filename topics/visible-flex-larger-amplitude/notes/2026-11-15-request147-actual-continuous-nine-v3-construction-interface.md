# Request147 — 真实原 core、同次连续 C cut 与 R323 新九控制目标构造

作者：AI（/root，GPT-6 Astra Pro）。日期：2026-11-15。  
状态：完整源码、参数、workflow接线完成；未填未来run或任何实际构造/域/场成功。所有科学计算仅在本公开仓库Actions。

## 1. 本轮要实际完成的对象

[R300](../results/R300-continuous-nine-control-scalar-family-and-cut-calibration.md)的新连续九控制族与[v3完整实现](2026-11-15-continuous-nine-v3-cut-factory-and-physical-interface.md)已经发表。本次将它们接到一个具体、可执行的现场：

1. 按原f12f v3源、原三输入、全部1440片/六primitive及原1800秒预算，重新产生完整连续C数据；
2. 保持144的原binary cut点第一、whole-natural第二查询，按原1c39读回全点叶的准确三jet hull；
3. 从原公开accepted M96前缀的真实完整文件取得准确core几何和原末材料端点；
4. 用[R323](../results/R323-finite-cut-boxes-and-explicit-uniform-dyadic-windows.md)明确有限盒公式选新collar/两过渡窗，保真实146末九参数；
5. 调用不改字节的v3 factory，分别遍历完整基底域和完整给定九参数域；
6. 若准确definition实际产生，则用既有v3 numeric构造完整有限搜索profile，保存全部系数身份、支持、相邻jet词及公共材料域含义。

这是原完整来源上的新目标构造，不是旧场继续成功。本轮没有当前C的非零尾/J，没有新BVP，不能用数值profile实例化替代完整112、native、final audit或闭曲面/metric/reach验收。

## 2. 已固定源与运行入口

| 角色 | 文件 | 字节 | SHA256 |
|---|---|---:|---|
| 新同现场构造wrapper | geometry_20261115_continuous_nine_v3_actual_construction.py | 20377 | 738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0 |
| request | public-continuous-nine-v3-construction-request.json | 17398 | 4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707 |
| 独立workflow | visible-larger-public-continuous-nine-construction.yml | 38452 | f539e75219d2c7c85fbf335c5e1d17ccc9a2fae3e3af56b631c5d4a0516a034a |
| 原准确v3 factory | geometry_20261115_continuous_nine_scalar_factory_v3.py | 42270 | 0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e |
| 原v3 numeric | geometry_20261115_continuous_nine_scalar_numeric_v3.py | 22469 | 7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60 |
| 原v3 physical薄层 | geometry_20261115_continuous_nine_augmented_v3.py | 6138 | d86f6fdf3cf59df3d45c907c655fe54ab830180facd27b7402e649b2e14d151b |

除workflow在根.github/workflows外，前三个运行文件都在本题computations。v3 physical保来源且编译，但本轮不在缺当前C尾端口时实例化完整物理BVP。

Request共19 source pins：144原11项逐项不变，加准确core kernel a9a25d96、原scalar 8ff23e31、原PrefixControls f019e6b3、原full physical f76b9c37、三个已发表v3源和本次wrapper。所有完整SHA都在request；原78来源恢复合同、原九条E数学来源map不变。没有执行旧publisher或重标旧native响应。

科学核心f12f、点读回1c39和原factory/numeric源均不改变。本次wrapper只负责真实来源绑定、R323公式参数生成、原factory调用和有限profile实际输出。

## 3. 原输入与真实core指针

原C三输入从公开历史提交8bd267107cc8710d371f3b62c02986655ac965b0恢复：

| 输入 | 字节 | SHA256 |
|---|---:|---|
| 原T112 config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| ledger ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| stored ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |
| accepted M96前缀 | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |

accepted原公开路径是notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz。只读真实解压JSON的：

- geometry：/fixed_scalar_profile/geometry；
- core_end：原accepted.mesh[-1]的binary64值，再准确提升为dyadic。

它们对应原CompleteProfile的实际获取方式。新的准确core内部多项式继续由固定a9a25d96 prefix_coefficients形成，原共享首jet/全部knots不删。完整原accepted的success和M96身份核验不把它变成新目标的已接受场。

第一控制支持明确采用原PrefixControls的binary64运算：left=.05*L0、right=.30*L0、stored_width=right-left，再将这些实际字准确提升。它不是默认CompleteProfile的另一组.15/.70支持。实际准确端点仍须满足0<left<left+width<L0。

cut始终是原config numeric rCut的准确binary64值。查询的0.3数字与config原词逐字核对；不把有理3/10或Rout换作原cut。

## 4. 真实146末参数，只作新族初猜

来源见[R320](../results/R320-actual146-direct-normal-responses-and-finite-parameter-resolution.md)：

- run43716274591/source69765fcd81ca84819cdeb09c4fe14c55fdb5fb80；
- compute132818390627/report132818651357；
- 原status2741264 B / 252a9ceabf63305cdab40312b104e397acb7a8deb52ea513d4ecc038104d80e5；
- primary73169 B / befc5446223c3f45bc96f4d53aeae6e0115f2fe3214051bc4219f2465fefe1e9；
- 完整scalar view1329928 B / 9593cb0a813caba9a1d43fc59fa7ef6ad2859968fb9804e189ef69bedc623233。

全部九个literal值保持原顺序：

~~~json
[0.3055213835477326,0.21645013203050154,0.34270051957744246,-0.06322334619266512,-0.01747451701873286,0.9376115689625685,1.0751306255033548,0.6886900390922872,0.9385431607625546]
~~~

没有导入146的state/J/merit、原Arb域或原末radius。这九个值在新基底和新支持上未必可行，需本次完整九参数域遍历实际决定。基底域与给定参数域分别记录，不能因基底可行就把旧九点称为新族可行点。

## 5. 同一有限cut盒上的明确宽度公式

新wrapper首先调用原v3 factory的cut_jet_from_actual_cover，绑定当前同job的result、input-binding、query-plan、query-results、完整点readout与全叶SHA。保同一run/source/config、准确cut和所有点叶，不将144未来或已清结果当输入。

E0/E1/E2继续是R300真实语义叶；其有限有效盒只用于严格包含和参数选择。实际盒须给E0下界>1以及v盒严格在(-1,0)，准确core末须A>R、|V|<1。未满足时输出具体error/phase，不改原cut、warp、根族、宽度阈值或native门。

R323选择κ=1/2。设gamma=A-R，M为cut速度盒对0和−1的严格余量，B、Q分别为b、q的绝对上界，T=1+B+Q。取

$$
d=\Theta\!\left(\min\{1,\gamma/(8T),R/(8T),M/(8T)\}\right),
$$

其中Theta是R323的准确整数位数dyadic公式。按原表达形成RB/VB/BB盒；再用实际D下界、mA/mB和两端加速度上界形成R323明确最小值，得两个相同过渡宽度e。

wrapper保存全部实际中间盒/严格余量/Theta输入及指数/原完整11条件；这些计算全部在Actions。准确expression tree不把盒端点或中点写入语义叶。没有另作根refinement或迭代参数扫描，也没有将当前有限盒声明为可任意精化实数oracle。

固定root_choice为R286-dovetailed-rational-middle-third，是新目标对真实根的数学声明。实际v3仍统一包含原全部允许根族；本次没有数值生成该无限选根序列。

## 6. 原factory、完整两域与有限数值profile

运行原factory时：

- sqrt_bits=256；
- max_domain_cells=65536；
- max_domain_depth=32；
- 每次domain_budget_seconds=300，最多基底/给定九参数两次。

core、所有新pieces、全部控制支持、所有闭叶/未访stack按原factory处理。参数配方和准确definition在本job临时目录实际写出后再逐SHA消费，不预填未来文件身份。原factory的error/return code、两域完成标志、所有未付计数和文件身份原样记录。

若准确definition产生，原numeric构造器将当前有限叶中点用作binary64搜索近似。完整definition/source身份、每个系数和所有节点/支持仍保；所有相邻piece的三jet binary词与相同/不同标志完整分段输出。数值中点不保证来自一条共同根，数值接缝词相同与否也不被误称为准确C²或误差证书。

数值profile的mode metadata为112，active scalar为9。准确公共材料域u∈[0,1]上的径向metric仍是L_true²du²；数值长度是另一项实际读数。原physical薄层不被调用来制造缺失的尾端口或全场成功。构造器正常返回不能支付新的C Jacobian、nonlinear native或任何闭合几何指标。

## 7. 科学资源、规则同步与失败

原E科学参数逐字保持144：

deep_definition=original-exact-root-family；precision_bits256；integral_absolute_bits96、relative80、guard8；原100000 evaluation、value_width_bits24、max_depth48、query_depth12、200000 panels/200000 query nodes、budget1800秒。全1440片/六primitive、原point与whole范围保全；新构造没有缩去它们。

独立workflow仅新request路径触发，独立concurrency且cancel-in-progress=false；不取消144/145/140等已有任务。compute95分钟；原E step45分钟，完整点读回10分钟，新构造step20分钟，report5分钟。后两项是本轮新增作用的显式资源，不是把原E1800秒改大。新域预算按每次300秒解释，不能冒总共300秒。

原3b8规则runner仍每2700秒真实pull/rebase，只显式装入本次已读21bd/bff双README。E与新构造各自使用一个原runner/独立镜像目录，新构造开始时再次真同步；科学checkout不由该镜像更改。认证只在rules父进程和其GitCLI环境，数值child清GH_TOKEN/GITHUB_TOKEN/MR_TOKEN。新helper保GITHUB_OUTPUT仅用于GitHub步骤结果传输。

输入/来源/构造的工程异常记录真实phase、原type/message/traceback；原factory非零码保留并使wrapper非零。完整域未付、数值profile不能表示太短窗口、或input缺失都不标为原native数学拒绝。任一步骤超时/规则中断时，后续always读回保现有原结果及两个rules结果，不能把输出缺失补成完成。另有独立construction_readback步骤：主输出存在即逐字核SHA传递；缺失则读取实际已写recipe、width selection、factory/result和construction-result，保完整内容或全部无损分段，明确primary_output_unavailable/summary_complete=false，解析不完整文件也保真实错误。它不重跑科学，不把被信号中断的域栈称为完成。

## 8. 完整读回与清理

三种独立摘要分别传给report：

1. 原E结果、所有query与完整unpaid种类/后缀；
2. 原完整点两jet readout；
3. 新构造result、实际recipe/原factory结果/两域/数值profile身份与状态。

第2项仍使用不改字节1c39源的原REQUEST144 cut块标识；实际run/source在块内，不能据该历史标签误称重用了144数据。第1、3项分别用REQUEST147独立块，hash口径明确：第1为compact JSON不含LF，第2为原canonical UTF8含LF，第3为canonical ASCII UTF8含LF。

完整R323中间盒和全部数值接缝metadata按每段20000 ASCII字符无损分段，原完整组bytes/SHA及序号全部保存，每事件≤89000 B。主summary≤90000 B；若其完整内容更大，则整组无损分段，主summary明确summary_complete=false和完整组身份，不截丢科学试探或假填空成功。

准确model、域ledgers、数值specification和所有原C大账均只存在本request临时目录。实际读回后always清理这一owned目录，不上传Git、Release或新artifact。库内只保存本源、明确参数/公式、真实run/身份与紧凑结论。

## 9. 源级完成范围

本次在终端不可用期间完成全文编辑、JSON/元数据/哈希和对原144 workflow完整差异的文本核对，没有本地导入科学模块、执行任何公式、Python AST或数值测试。Actions起步继续实际19来源SHA与Python语法编译；这属于原执行接线，不是新增fixture或人工审批门。

147实际输出产生后须马上逐原件结清，继续新C有限头/全112响应、原非线性完整问题及闭合几何责任。本接口不将构造完成或一个数值profile当作课题完成。
