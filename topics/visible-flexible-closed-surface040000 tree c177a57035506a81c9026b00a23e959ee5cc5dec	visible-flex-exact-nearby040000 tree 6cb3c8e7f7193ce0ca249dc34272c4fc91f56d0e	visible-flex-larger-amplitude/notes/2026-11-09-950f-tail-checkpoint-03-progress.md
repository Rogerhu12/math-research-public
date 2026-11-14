# 真实加权尾的非线性延拓（进行中）

会话 Astra-visible-flex-950f9f73 / nonlinear_tail，2026-11-09。
全部结果为有限频率、有限深度数值诊断；没有声称已经得到无限尾、精确圆领或完整闭曲面。

## 接手时发现与冻结输入

旧 `root_k9_p04_m3_m4_continuation.json` 只有初始化失败，没有成功的非线性状态。
较新的 `2026-11-09-closing-asymmetric-m3-continuation.md` 已记录加权径宽方案，
其中 `closing_weighted_candidate_v3_k6_width045_config.json` 的物理参数固定为
width=.45、rCut=.6、rCuff=.15、wCut=.5、K=6、N=160。
六谷参数及 cell0 权重 [1,.5,3,.05,1] 均沿用此文件；本会话没有随加密修改它们。

新 worker `scripts/950f-tail-port.mjs` 复制旧 recording worker 的通信和保留逻辑，
仅改为使用 `closing_weighted_tail.mjs` 的已存构造，并把 `warpWeightLevels`、
`constructor` 纳入 warm checkpoint 几何一致性检查。完整源哈希写入每次输出。
只读依赖位置为 `/workspace/scratch/1dce210849f9/math-research`，
旧 HANDOFF 中 `/workspace/scratch/f6f33987b45e/math-research` 已不存在。

## 实际计算

`scripts/950f-tail-run.py` 对一个冻结参数文件保持 worker 常驻，逐个输入物理 cut
高度系数；保留每个请求和完整响应的 `.json.gz`，并在汇总中只列标量审计量。
M4/depth10/steps64/quadrature128 的输入为
`2026-11-09-950f-tail-k6-m4-config.json`，结果为相应 `-result.json`。
linearFar32/linearSteps128 只影响有限深初值/截断线；不是无限尾的充分证明。

第一次实际运行初始化 122.65 秒，通过；没有此前的 384 MB 内存失败。
a=1e-7 的 shooting residual 为 2.92266e-11，完整 Darboux residual 2.62724e-19，
周期展开实际 metric operator error 2.44965e-15，formal height curvature 5.99945。
这仅检查数值管线的一个小振幅状态；继续向目标 cut 幅度约 .00135 延拓。

## 独立线性接口

`scripts/950f-tail-linear.mjs` 在物理 momentum 坐标中传播归一化线，
避免将深部物理 (f,f_r) 相消后的 log gain 用作可信数据。
输出 `2026-11-09-950f-tail-k6-m16-dn-s256-far48.json`，含 m3…m48 的 DN、
真实 cut r,w,w_r,E,E' 及完整物理参数。m3=10.576512627874，与既存 s512
结果 10.576513553891 差约 9.3e-7；尚需按用途细化。

## 几何审计界限

已有 `actualMetricFromDarbouxJets` 可返回周期展开的 F、F_r、F_theta。
其每个 cell 的 z 均值从零计；完整尾坐标须累积 background+非线性均值高度，
再以 prefix 提供的全局平移对齐，才能审计 F·n。
现有 `formalCurvature` 从高度 Hessian 和目标 metric 推出；在 metric 缺陷非零时
不能自动等同于实际 Cartesian 曲率。Cartesian 二阶及所有径向/角向间隔的连续界
仍须另做。未把局部 sampled curvature 用作整个闭面的 reach 证书。

K=6 背景在 rCuff=.15 的无限深界由独立审查者重算；不直接挪用原 .25 半径常数。

## 加权尾 a=1e-4 与线性 cusp 修正

M4/depth10/64步延拓已达 a=1e-4：shooting residual 9.4226e-10，
完整 Darboux 3.20784e-7，周期展开 actual metric 5.34375e-10，
minA=.9608188、minD=.9989397，formal curvature 6.01927。
从 a=1e-4 直接跳到 .0003 时 Newton 阻尼严重，故另保留成功的完整 seed，
启动每次乘 1.2 的幅度延拓；这是固定物理 metric 上的求解策略变更。

发现旧 `physicalModeColumn` 的线性 RK4 未切开径向 warp 的 |w_x| cusp，
而实际非线性 flow 已使用 cusp-aware 算法。新建
`scripts/950f-tail-linear-cusp.mjs` 保持相同 momentum ODE 和物理 profile，
仅在每个 RK 子区间按 profile.integrationBreakpoints 拆分。
同一K6 metric上 K96（m3…288）、far48、512→1024 步的m3 DN差
6.6983e-11，m3 DN=10.576513803204914；相比旧均匀步数结果明显更稳定。
全96 DN 最大差4.1088e-5，集中最高频；前64最大差2.6276e-5。
这些高频值须按用于prefix的实际向量/共轭矩阵误差继续审核，不能据低频精度
直接宣称整个矩阵都到机器精度。

配置/结果：`2026-11-09-950f-tail-k6-m96-dn-cusp-s{512,1024}-far48.json`。
旧均匀结果均保留；不把它们覆盖成新算法的输出。

## 同metric 分段射击修复 M8 条件数

旧 whole-cell M8 在 a=.0001、minA≈.96081/minD≈.99894 时残差停在约 .00178，
故未接受。保留 stall trace 后，改为每个旧profile的两段多重射击；每段32步，
即总径向64步/原profile不变。内段不改变 mu 归一化，仅原cell外端将 momentum
除以 2^a。线性初值/深线改用 stable momentum 坐标并拆实际 cusp。
节点变换与物理ODE、角向root、mean、holonomy方程没有变化。
实现 `950f-tail-subdivision.mjs`、`950f-tail-stage-core.mjs`、`950f-tail-stage-split.mjs`；
所有旧源码保持未改。new core 对失败也保留最后一次真实Newton状态，防止丢失诊断。

M8 a=.0001：初始化9.24秒，求解45.31秒，shooting2.76861e-11，
fullD1.30786e-11，actualMetric7.56107e-15，minA=.9608093，
formalCurvature6.0192713，max chart condition13945.13。
相比旧M4同物理幅度 fullD3.20784e-7/metric5.34375e-10 显著下降。
因线性预处理算法也修正，正在补同一 stage2 算法下的 M4 对照，
不把所有改善先验归于角向加密。

新Python客户端 `scripts/950f-tail-client.py` 的 `WeightedTailPort` 兼容
solve(height,jacobian=True,audit=True)，保留全mean jets；仅在实际ODE响应收敛
后返回成功。它仍是有限M/有限depth工具，尚未证明封闭无限尾。

## 完整多模prefix边值路径：已到宏观目标的52%

使用既存宏观prefix的完整cut向量（含H2等），而非只给纯cos；物理metric不变。
`950f-tail-stage-port-v2.mjs` 只在warm初值加线性DN响应以补足新的Dirichlet差，
旧小步line-search因此恢复全步Newton。纯initial变化已保留源码版本。

M8路径已通过lambda=.236135294,.3,.36,.43,.52；最后H1=-.00066063824，
shoot2.2204e-11，physical fullD1.1888894e-4，actualMetric6.07618e-8，
minA=.388361，minD=.993173，formal curvature6.33016。
这只说明有限M8尾在该边值能求解；它未与原linear-port prefix匹配，
且非全频收敛证书。lambda=.62的下一步在初值root Newton即失败，
没有得到新解，也不能推成该幅度或一般几何不存在。
已保存成功/失败完整响应，并从lambda=.52启动 .03 一步的细延拓。

另一方面，真正prefix+实际DN的小q耦合由macro_prefix独立推进；不能把这条
冻结目标H的探路当作已经匹配的完整构造。

## 固定metric的depth10→12与多模细延拓

M12纯首谐波 a=.0003，保持parts2、每段32步、Ntheta256及全部物理参数，
从raw depth10扩至12后通过：shoot1.58898e-9，fullD1.68347205e-9，
actualMetric5.67546010e-13；两深度cut slope最大差 1.7347234759768071e-18、mean slope correction差 0。
新增深节点只用稳定线性图作初值，之后仍完整求解非线性ODE；这只是有限截断
深度稳定性诊断，不是已接入无限尾。warm remesh代码独立保留v3版本。

冻结宏观cut多模向量的lambda细延拓已到 .58（H1=-.000736865731），
shoot6.00214e-11、fullD2.73760322e-4、actualMetric1.38826819e-7、
minA=.2912221/minD=.9923763；lambda=.55的minA=.3395956。
相同M8下未投影fullD随幅度增大，下一步必须角向加密。仍未与原prefix真正耦合；
真正联解由macro_prefix独立推进。

多模细路径又通过lambda=.61：H1=-.000774979476，shoot4.10364e-11，
fullD4.07200668e-4、actualMetric2.07068592e-7、minA=.24335203、
minD=.99197749。已固定相同8个物理Dirichlet系数，补零到M12启动角向加密；
不改prefix几何也不拿M12原prefix略有差别的H当同边值对照。

新增 `2026-11-09-950f-tail-effective-tail-interface.md`，把实际raw7/8的小量
到完整无限尾之间的五组待证量列成可检查接口，并证明3Z旋转对称+精确
mean holonomy蕴含水平平移period闭合。未声称其余R46常数已经移植。

M8多模细路径已完成到lambda=.67（H1=-.000851206965）：
shoot2.01296e-10、physical fullD9.27755066e-4、actualMetric4.66941863e-7、
minA=.1484417（RK内部最小.1484094）、minD=.9911785、formal curvature6.44655。
lambda=.70在初始root line-search即失败，没有新的有效state；未认定几何不存在。
由于这一M8状态的未投影残差已显著，接下来优先M12同边值加密，再考虑更细延拓，
避免用欠解析角尾判断正则分支。完整失败响应随成功状态一起保留。
