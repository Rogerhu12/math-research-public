# Run47 — 原半波完整求解链的严格本机Horner值路径

会话 Astra-larger-e4e2a2bf-20261126。原run33 `46133839513/1` 官方已取消；末真正accepted点 `1f0c5699d7bbca0b9f1c143fad76fc07b6363b6df140b11c1fbe9f8e2396b91f` 只保原比较身份。原完整坐标/续算状态未从runner取回。本次从原物理输入和原初值完整重建，不把旧accepted摘要当新起点，也不推断官方取消原因。

## 完整来源与真实变更

[17文件总交付](../computations/run47-complete-native-horner-source-parameter-and-launch-delivery.json)、[完整源交付](../computations/fixed-fejer-halfwave-R729-native-horner-complete-source-delivery.json)、[全参数交付](../computations/fixed-fejer-halfwave-R729-native-horner-complete-parameter-delivery.json)保存全部原父、完整编辑、每件字节数/SHA256/Git及原33外部历史责任；不是节选代码。历史父树 `43914b1da832b13ffc65f9f3074446217fc065b9`。ROOT独立读取17完整父并从全部原编辑重建17完整新科学文件，每件三身份与交付一致；旧driver99954B、新99763B均完整审读，没有裁成局部程序。

原138个科学角色增为140、21个运行源增为23。新增C和Python绑定只用于原正常closure内符合条件的普通CPU binary64、不求导、contiguous值计算；AD/JVP/VJP、functorch、dual、inference、autocast及任何不合条件路径走原完整Torch。原强制endpoint/stage复读仍原式求值。13项下降Horner的d0/d1/d2、移位1/2、原舍入系数表达式及小z判据保留；大z三角支及torch.where未改。C编译明确禁FMA与重结合，记录编译器/version/target/hash、flag、binary hash、系数buffer hash、rounding/MXCSR及调用统计。编译不可用回原完整Torch，未加fixture、AST、微基准或新的科学准入。编译选项不是跨实现逐位同值或实际加速的证明。

closure只在合法作用域共享原宽度/权重的常量tensor；原922×8物理点、求积加总、cumsum、矩阵计算不缩。stage driver只把最终确有失败时需要的Python矩阵转录延后；每次失败尝试所需完整eta/control/value/matrix tensor仍保原位置和原式。全部既有源身份和method-body guards按真实整件更新，没有绕过。

[Horner算术和范围](2026-11-28-halfwave-R729-full-normal-chain-Horner-arithmetic-and-scope.md)给出旧33实际调用数量下界对应约46764577600次标量更新，这是表达式操作计数，**不是实测加速比**。

## 原问题、全部参数和读取范围

ROOT另从原80928B science及70074B pure整件重建新93038B、77713B整件，字节、SHA256、Git完全同交付。新wrapper162/12词中，后157/7原科学词仅变独立输出namespace；每个数值flag和peer词逐项保留。原science575正式+64实时selector、新621+84，原pure564、新590；ROOT逐项核对原selector及其路径未丢，增加项仅实际build/native元数据。两个必要输入步骤与原33完整queue逐字JSON相同，6/26个参数词未变。

完整1,333,370变量、923节点/922胞/8Gauss、原32正常stage和原强制重积分、N38/52 G8/22、4恢复方向/64迭代/15试步/192约束、原未知外部责任、源/式/材料支持检查均不变，全部原预算见完整参数原件。science正常返回后才轮到原完整pure读取。新输出namespace `fixed-fejer-halfwave-R729-native-horner-first`，原问题和固定目标没有换成简化尺寸。

## 正常入口与实际状态

正式[请求](../computations/resume-20261128-actions-request-47.json)普通推送触发独立workflow47；队列包含两原输入步骤和两个完整ready引用。控制器在触发提交的detached sparse worktree读取完整ready并验证身份，展开后运行原队列验证和原argv。每一个科学/读取入口正常构造全部17源并保存完整build/materialization receipt；本机值算子在这条真实完整链中自然使用。请求最后校正文义：官方只证cancelled；360min为配置，未读annotation不冒称取消原因。校正后的请求17861B/SHA256 `46ce681e5b870cb82532eebc1579fd356e17b828473fd94e6d8366b08d2fab01`/Git `0b6702b5f5f5f04710178e81da873357451eceb3`；总manifest两处对应完整身份同步更新，科学源/argv不变。

公共4CPU/16GB、Python3.12.14、NumPy2.3.5、SciPy1.17.0、Torch2.5.1 CPU。job360min，controller21000s只关闭新步骤准入，已启动子进程仍观察到自然返回；原预算不减。至少3000秒真pull/rebase并读双README差异，变化立即停止继续计算等待按新规改源；正常返回每结论普通推，非快进立即真pull/rebase再推。公共整记录按JSON语义分卷保全部紧凑字段，raw/共享库/大报告留runner。repo容量只延迟整份发布，不削减输出、不改变科学子进程。

本条发布时未观测未来run/job/PID、编译器/二进制、当前model/point、数学报告、完整science/pure或加速比。所有actual字段继续为null；之后只登记真实回报。全目标仍欠整个同g闭壳、全时嵌入/法管、商距离和实际精化，不能因编译/runner成功宣告研究完成。

来源路径校注：原参数历史元信息含双重topic前缀的delivery字符串，原字面保留。当前真实完整父件位于 `topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-complete-parameter-delivery.json`，16430B/Git `0c4c502566125f92e7872ad8029cafcab533134d`；新source delivery及正常builder使用这个实际单前缀路径，ROOT发布保留检查亦针对真实完整父件。该历史路径拼写不作为不存在的新科学输入。


## 真实初几何与首试探统计（截至原完整观察2026-11-28T18:48:56Z）

[官方run46171090151/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46171090151)、job141059443197实际in_progress，科学源`5538870311afb814eb332f2926b8c82eee1930e2`、真PID3601；未自然返回。两原输入准备步骤完整exit0，分卷18548B/Git`495692df64cd75bf7923e327d63ca10eeb4c0e74`/SHA256`88eec3a50359eaf06bf26929537b339bcc7697e457ab313e325d5d0ee2860220`，完整inputs/outputs/metrics和empty missing/error已读。原2218叶准备accuracy_reached=false，whole_tail=true/unresolved_tail_dropped=false，不能以输入准备成功充全科学准确。

ROOT完整读取[初几何固定观察](https://github.com/Rogerhu12/math-research-public/blob/36e38cbe03f3cb2b24ea600601a33766e5e9f5d5/topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46171090151-1.md)29820B/SHA256`9072c8530a90d3e9494aa689e350f6350bea277dea2c24320bd206e5a350b6b6`/Git`098006e53b9f651ef9dedca118541f41d1a69a6f`，以及[18:48完整固定观察](https://github.com/Rogerhu12/math-research-public/blob/90cbff0d736d68cce070f5e5ad92ebf484116d6a/topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46171090151-1.md)28731B/SHA256`eea1f1db7ab2e228c0ca96371882e1bceec19cb186e9ca83724fd05b86ceb781`/Git`33438f63da68ef403a639c0f181c0073780418a0`；长度和双hash均核同。中间18:13:35Z版28728B/Git`0ee619835f47f3ff2a1ef48129a522c15b58b7ff`同样全读，三个不同观察不能合成一个不存在的新统计时刻。

新实际model `02b815f1fc471afe0bd4699471c96ef3bc2adbdf66a061903b18798004f089d6`，driver `c005f212047fd63bd458136dddb8944062e4320b19a1070f4c0e919b55b586ba`，数学source `4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94`、target `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`。原33 model是`61c6542b3cfe39dea9fbf8c002c8ea204f5dad193ddaffe94bc7c908822682d7`、driver`a359ab4907b22719b01ed5a6de65e61859d313c68d4a4d3b4fe0e0822d7effd3`；两运行数学source/target相同但model/driver身份不同，完整包不同。

17:56:52.447061Z初完整几何实际返回，真点`7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47`，Phi681.6517423825408、relative Gram.4061652531176999、initial_geometry_complete=true、最大正物理g=.5305849371949052。ROOT与[原33原报告](2026-11-28-run33-section16-retry.md)核同的是这个完整点及这些已返回标量，不宣称两完整数据逐bit一致或整个算法等价。

|初完整几何项|真实数值|
|---|---:|
|reach g|.5305849371949052|
|body diameter g|−.03813552733778258|
|distance plus g|.11391238912344381|
|distance minus g|−3.0936337267043594|
|cap diameter g|−.06715131487906445|
|height floor g|−1.0411715967426867|
|maximum absolute principal|12.32709940409259|
|body diameter point lower|4.117175466515689|

实际最坏K地址cell885/u.8306046932331322/phiπ/2/branch1/s2.1573631007205925。首restoration α1真trial`291f3943db2d5de24f7911923412fb8013b0d3cc739c09a0b5f6038a183151ad`，18:13:22.525168Z统计返回Phi731.1417800730309/Gram.4097559009463338；截至18:48:56Z其完整几何与trial_accepted仍未返回、accepted_directions=0、complete_report=false。原33已拒绝这个旧run的同名trial、后已接受另一半步的结论，不能借来填新47的尚未返回字段。

native实际built：C源`6dbfbe17c4e535dce61500d9c8da72a088bb377bfba21985f5ef5415cb4e3933`、Python绑定`cfe09c087fd06bdccaf8e35118f87af885cae31603a7884489a1eb9bdf7a54bf`，原系数buffer`2346ea2b127eec428c09de2f80fbb7a15b032ffec0a6dee36ddad5c260e4c185`；gcc15.2.0 Ubuntu15.2.0-16ubuntu1/x86_64-linux-gnu，完整编译器哈希`864711037b900acdb7a449cf48d912cefa935b527fb60c767ccb956779e66136`。真实.so15584B/SHA256`26ef7aabf14bafc5503be4f7b968fa8635a22fb09c0aa5ca94b5cc839ac50ac1`。初完整几何时611原native calls/1,769,900,704 Horner updates；18:48:54Z整个原进程累计27930 calls/80,552,573,152 updates、47701原closure返回/0逻辑失败，whole-original-fallback0，rounding0/MXCSR8098。次数和一个观察窗口不证明整体加速；native_scientific_speedup_measured=false保原。

原observer的缺compile_error键和尚无trial geometry/last completed trial等TypeError完整保在上述原观察，未删除或补值；built状态不被缺省error键误称编译失败，未返试探不被误称数学拒绝。当前全部原140角色、完整源/参数/32stage/原变量和自然science后pure预算继续；本次只登记已发生的真实结果。
