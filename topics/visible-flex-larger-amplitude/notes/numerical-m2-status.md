# m=2 数值设计入口（进行中）

状态：**数值证据；尚无闭曲面候选**。本文件记录改变机制的实际有限 BVP，不能用于宣布本题完成。

## 已执行

- 使用既有 weightedK6 的同一物理径向尾，重新计算 `spacing=2` 的有限线性动量 DN：12 个谐波、每段 256 步、far=48。得到 $D_2=5.7127541910311574$。脚本配置和结果分别为 `computations/numerical-m2-tail-config.json`、`notes/numerical-m2-tail-linear.json`；供 Python 使用的接口为 `computations/numerical-m2-port.json`。
- `computations/numerical-m2-prefix.py` 在独立 Python 进程中，将已存在的平面 Frenet/支撑核心求解器改成 $m=2$。角图为 $\theta=\psi-3q_{\rm ref}h(s)\sin(2\psi)/2$，链式导数中的频率和 $m^2-1$ 同步更改；源文件不修改，逐文件 SHA256 和明确替换列表写入结果。
- 搜索域的旧 $q<0.2$ 限制是数值参数限制，已放宽至 $q<0.48$。实际核心仍由 `PlanarSupportCore` 检查完整支撑函数的正曲率半径；角图目前仍要求 $3q_{\rm ref}<1$。实际幅度与角图参考幅度可以不同。

## 首个分支入口

固定设计形状 $v_u=.25,v_d=.4$, ramp=.4, ramp_eta=.05, cycles=1；同一尾 cut radius=.6、cut slope=.5。线性特征根 $\delta=.21049469476483748$。

| q | M | 收敛节点 | 实际设计 δ | 采样度量误差 | 最大高度 | 自然 cos4 支撑系数 |
|---|---|---|---|---|---|---|
| .02 | 4 | 331 | .21049636736374938 | 2.78651e-9 | 2.62783 | +4.96723e-6 |
| .05 | 6 | 570 | .21050515168427636 | 4.72621e-9 | 2.62811 | +3.10561e-5 |

这些是 `scipy.solve_bvp` 实际收敛的非线性前缀；边界使用有限**线性** DN，末端高度分别约 $4.56\times10^{-4}$ 和 $1.14\times10^{-3}$，并未变成精确旋转圆领。计算文件前缀为 `numerical-m2-v25v40-m4-q02`、`numerical-m2-v25v40-m6-q05`。

两行 q、M 和 δ 都改变，不是固定度量的加密收敛实验。高度偏大，因此停止在这个轮廓上继续增幅，转向较短设计。

## 较短轮廓已求解

$v_u=.45,v_d=.5$，其余ramp参数同上：q=.05/M6实际收敛601节点，δ=.18028774816718476，采样metric≈6.50918e−9，height≈1.60122，κ≈4.19419，cos4支撑系数+1.13655e−4，末端height系数≈.00205233。文件前缀 `numerical-m2-v45v50-m6-q05`。

root进一步线性筛选给出 $v_u=.55,v_d=.6,\delta=.17076594893144723$。q=.08/M8的首次运行在2500节点上限退出，原tol=2e−7而最终残差3.76e−7，**solver_success=false**；仅作后续warm。随后采用支持一般频率的Fourier Jacobian，以q=.15/M10、设计tol=2e−6继续真实有限方程。粗设计容差不替代本题最终度量或收敛门。

## 下一步

- 对 root 给出的较短 profile 真正延拓，先验证小 q，再增幅并追踪高模支撑系数、全图曲率与 Frenet 正根余量。
- 对高 q 的潜在负 cos4 支撑核心，需要允许独立角图参考，或将角图扩成两谐波；不能用错误的 $3q>1$ 单谐波角图。
- 达到合适幅度后，再接实际非线性尾、闭合、全相位 reach 以及固定参数收敛。当前未支付这些条件。

## q=.15 的实际前缀几何

`numerical-m2-v55v60-m10-q15` 实际成功：δ=.170621448627185，449节点，设计残差1.99e−6；重新评估的前缀采样metric约5.68e−7，height=1.30624，最大主曲率约5.51549。核心支撑函数 cos4 系数 +.001786995、cos6 系数 −.000154103。

`numerical-m2-geometry.py` 对保存的插值曲线重新计算位置、导数和相位点云（257×384径角点、7相位）：双镜像前缀的直径样本为3.01125944，相位π/2的表面点云Hausdorff约.29973699，比例约.0995387；局部曲率半径/此前缀D约.06021，Frenet正根余量最小约.03859。**这些仅为有边前缀采样数值，不是全闭曲面reach证明。**

外向见证 $p=(0,A,0)$ 到前缀的距离约.281904，因上方外鼓而小于核心支撑差；相位Hausdorff最大来自凹入侧的核心点。这说明后续闭图的held验证应同时考察内向和外向见证。

直接 q=.15→.25/M12 的大步延拓在第二次迭代失败（残差1.26，BC .052），所存 `numerical-m2-v55v60-m12-q25` 是失败warm，不能报告成候选。现以 q=.18 的较小步继续。


## 进一步真实延拓与尚未合格的图

- v55v60、q=.18/M10实际成功：δ=.17053856686761762，496节点；采样metric≈1.61704e−6、κ≈6.16163、height≈1.30212、core最小ρ≈.42295。
- v55v60、q=.20/M12实际成功：δ=.17046556089440737，538节点；采样metric≈9.60672e−6、κ≈6.65745、height≈1.29872、core最小ρ≈.35302。它超出最终度量门，目前仅粗设计图。双镜像前缀D样本≈3.00856216；5相位点云的最大Hausdorff≈.39850863，比例≈.13245817；局部曲率半径/D≈.04992676；Frenet余量≈.03396。外向A轴见证约.32570，因此后续不能仅引用平面核心支撑差。
- 从上一图转v65v60、q=.20/M12也有限求解成功，但采样metric≈.01041946、κ≈18.6282，并出现cos24≈1.73e−4的大高模。该图不是等距候选，不能把solver success代替几何门。高度降至1.1190的优势不能抵销这些缺陷。
- 已生成较精细24模/512步/far48线性port `computations/numerical-m2-port24.json`；首模比旧256步值改变约5.85e−11。正在对较稳v55v60/q20进行真正M16求解，以区分谱截断与分支问题；物理δ在当前设计模式仍可变，因此不宣称这已是固定g收敛实验。


## 谱升阶的实际改善

v55v60、q=.20从M12升到M16后再次实际收敛，575节点、32.1秒，δ=.17046556209971098。采样metric由9.60672e−6降至7.09126e−7，height=1.298723254、κ=6.65932，核心/末端位置量几乎不变。这支持继续升频消除该分支的有限谱误差。由于δ仍随设计求解改变约1.2e−9，此项不是README要求的固定g加密证明；最终必须冻结选定g后运行--fixed。

## q=.24 与实际非线性尾的当前界限

v55v60、q=.24/M16 也完成有限前缀求解：1495 节点、δ=.17025973511178502、κ≈7.95323、height≈1.29021、末端首 height 系数绝对值≈.01311603。其采样 metric≈1.74637e−4，超出最终门；核心最小曲率半径≈.21311。文件 `numerical-m2-v55v60-m16-q24` 是已收敛的粗设计方程解，不是合格闭图。现将自然分支的进一步盲目加密暂停，转先解决实际尾。

`computations/numerical-m2-tail-probe.py` 从成功 q=.20/M16 checkpoint 提取完整 16 模物理末端 height 向量；首项为 −.010872411228584962，次项为 +.0001139547299975254。符号包含径向桥的方向 σ=−1。脚本沿 $H_j(\lambda)=\lambda^jH_j(1)$ 延拓，只有 λ=1 才是完整目标；每次都调用真实有限非线性动量根、Frenet 尾流和 multiple shooting，不用线性响应代替最终尾。

直接从 λ=1/64 启动的三组尝试（完整 M16 / depth8 / 4子段 / 16步 / N256；完整 M16 / depth12 / 8子段 / 32步 / N512；低阶 M4 / depth8 / 4子段 / 32步 / N128）均在第一轮 Newton shooting 评估之前失败。报错包括 `momentum branch D/S/A rejected` 与 `momentum Newton line search failed`，并且将步长减至 λ=1/4096 仍未生成可行线性 warm 流。这些是**失败尝试，不是尾响应**。

`numerical-m2-tail-initial-diagnostic.mjs` 定位了原因：原 weightedK6/m2 线性 warm 在 λ=1/64 的 rawCell1/segment5 首败；λ=1/4096 时首败移至 rawCell5/segment5。后者的物理 Q 约3.17e−8，但归一动量 target 的 L 角幅约.828，初猜 A 最小约.172，说明非常小的物理系数仍可能对应强非线性根。该诊断只评估线性初猜，不证明真实分支不存在。

更小邻域确有真实非线性解。M4 在 λ=1e−8 成功，并连续延拓；完整 M16 则从 λ=1e−5 实际成功，已到 λ=4.75e−5，最后一次归一 shooting residual≈3.48e−12、4次迭代、末端首 slope≈−2.95029210e−6。所有已成功点的参数、完整 state 压缩响应和逐项源 hash 均由 `numerical-m2-q20-tail-w16-small-*` 保存。**这些尺度远小于 λ=1，不可当成 q=.20 实际尾已解决。** 进一步延拓和对最后成功尺度的真实曲率/度量 audit 尚在运行。

`numerical-m2-tail-conditioning.mjs` 同时检查有限线性稳定线上的归一动量峰值，区分物理尾设计与积分精度问题。原设计在首模目标 height −.01087 的线性外推下，max |L|≈6836（rawCell6）；改 prefixR 为4、8、16、32、64并未改善。这个线性现象只用于挑选下一套物理设计，不是实际非线性存在性或幅度上界。

完整 M16 的上述小幅尾实验现已结束：最大成功 λ=9.390625e−5，H1=−1.02098737e−6，归一 shooting residual=3.52134e−12；真实非线性尾采样 audit 给 minLeading=.27965812、minD=.99999416、formal curvature=5.99902218、actual metric=3.77725e−15、normalizedFullDefect=1.65093e−8。λ=.0001065625、.000112890625、.000131875 的实际启动均失败。这证明一个很小的有限尾邻域已被实际求解，仍未支付完整目标幅度或无限深收敛。

源题已提交笔记 `2026-11-09-closing-physical-cell-recalibration.md` 说明全 M10=0 重校准和简单 flat sleeve 在旧 m2/m3 问题上已失败；本轮额外 prefixR/flat 扫描也未改善。因此接下来使用源优化器的透明内存适配 `numerical-m2-tail-optimize.mjs`，直接针对 m2 的实际物理线性正性门重优化前七谷；每个候选为不同 metric，只作设计筛选，最优者仍须另接真实非线性、固定参数加密以及闭图审计。

## m2 专用谷控：193 倍线性改善及首次真实验证

七谷的218项直接物理传输搜索得
`beta=[1.9375,1.875,3.375,4.5625,5.5625,6.8125,4.3125]`。
固定其余 weightedK6 参数，同一 metric 的512步/far48细化给首模线性正性采样门约3.07601929e−4；比原 m3 谷控移植到 m2 的1.59038e−6提高约193倍。cusp-aware 有限线性 DN2=5.696892954617947；tail背景高度增量=.0487721721。冻结配置和16模入口为 `computations/numerical-m2-tail-opt-config.json`、`computations/numerical-m2-tail-opt-port16.json`。这是新的尾 metric；原前缀的末端 slope 不能直接沿用拼接。

完整 M16 真实非线性尾随后在 λ=.0025 成功：H1=−2.71810281e−5，归一 shooting residual=1.58669e−11，4次Newton迭代，求解过程全尾 minA=.91062714、minD=.99984500。该点实际承受的首高度超过原尾本轮完整 M16 最大成功值约26.6倍。继续向目标 λ=1 推进仍在进行；这个首次成功尚未完成其全尾 audit，更不是闭合或无限深结果。

同一批笔记还保存以平滑最小门目标做七维 coupled Nelder–Mead 的局部搜索，目的是检查坐标法局部停滞；不能仅凭搜索失败宣布该设计族有幅度上界。

原尾的 M4 低阶延拓最后成功 λ=.000121579543（H1≈−1.32186279e−6），audit minLeading=.05025416，紧贴默认 projectionFloor=.05；在更大试点 root 初始评估失败。这是所用严格正根/guard分支的数值可达范围，不能视为实际尾存在性的严格上界。其 normalizedFullDefect≈.01656，尽管 physical actualMetric≈4.11e−14，说明低阶相对 Gauss 误差已显著；不应以其较大 λ 取代 M16 完整向量的证据。

为排除源码在别的研究会话中变动的影响，新试验将使用主会话从 commit `869436630c99aa5a68afb55bd8877c826034d117` 生成的固定 cache，读取 `source-origin.json` 记录 revision；在此之前已开始的试验仍保留启动时逐项 source hash。`numerical-m2-tail-probe.py` 已加入相应 origin 优先、git fallback 的来源读取，不要求固定 cache 含 git 元数据。

## 小 cut 的首个固定尾设计

固定cache上的新参数为 rCut=.35、wCut=.08、width=.25、K8、orientation=+1，因此实际 rCuff=.10。前七谷从多初值重优化，199候选后得到
`beta=[3.6875,3.5,4.8125,5.625,5.625,5.5625,5.6875]`。
512步/far48同参数细化给 m2 线性T门1.14793531e−4、tail背景高度约.023、形式 amplitude=.00008 的曲率采样约7.99939。它仍是线性筛选与形式几何，不是实际闭尾。

`computations/numerical-m2-tail-smallcut-35-port16-r1024.json` 保存1024步/far48的16模 cusp-aware 线性DN及对512步的逐模比较：D2=10.34919095642181，D4=28.331800517131015，首模变化2.01e−10，所有16模最大斜率变化1.70e−6。高模DN的变号在加密后稳定：m16≈7.40885、m18≈−20.54547、m32≈−641.36492，因此不能强行替换成正的渐近斜率。入口图的极点/共振对前缀求解的影响须由实际BVP检验。

对应冻结参数为 `computations/numerical-m2-tail-smallcut-35-optimized-config.json`，根源配置与优化历史、源revision/hash均已保存；主会话负责新的 DirectionalBridge 角度正则性和完整前缀重求。较小圆帽的单帽直径不直接否决H条件：若采用上下两个固定帽的并集，须最后核验该并集的真实直径与全曲面D。

邻近 rCut=.30、wCut=.08、width=.25、K8 的独立多起点七谷重优化更有希望：
`beta=[4.25,3.9375,4.9375,4.9375,8.6875,7.5625,6.6875]`，实际 rCuff=.05，背景tail height=.0226843112。
512步/far48的 m2 采样T门=2.11656487e−4，比.35 cut约高1.84倍。
1024步/far48的16模真实线性port为 `computations/numerical-m2-tail-smallcut-30-port16-r1024.json`：D2=11.856879482263345、D4=30.839583663099948。尚无该小cut metric的实际非线性尾、前缀接合或闭图；减少入口H的收益必须由新前缀实际求解支付，不能由r^4预期代替。

## 优化旧 cut 的固定cache真实 audit

七谷优化旧 cut 的M16最终保留 req7：λ=.0192578125，H1=−2.0937885686e−4。更大λ=.021630859375 的req9在5次Newton后明确 `multiple-shooting line search failed`，残差19.04034、A_min=.05441；随后启动的req10被主动中断，完整失败迭代保留。不得把停滞迭代替代req7真解。

由req7在固定cache独立重新求解/audit，得到归一shooting residual1.95694e−10、minLeading=.25798302、minD=.99880421、formal κ=5.99902120、actualMetric=1.76577e−10、fullD=4.22258e−7、normalizedFullDefect=5.27697e−4。后两项提示仍有相对Gauss谱尾误差；小physical metric不能自动替代固定参数升阶。报告 `numerical-m2-q20-tail-opt-w16-audit-summary.json` 与单一压缩响应 `numerical-m2-q20-tail-opt-w16-audit-response_0001.json.gz` 可作为独立复算入口。

现已从该成功state启动同一物理metric、同一完整16项入口H（其余补零）、同一radial depth/parts/steps的M24/N384真实求解与audit；只改变角谱阶数，且将失败时Newton上限设为12，避免同一坏步长时停滞。

另外为主会话固定g的前缀升阶，`computations/numerical-m2-port32.json` 保留旧 `numerical-m2-port24.json` 的全部物理参数、cut及前24个浮点DN值，新增频率50..64来自固定source1024步/far48。新增来源与原port SHA256单列为 `extension_source`，既有port24不改。

## 固定 H 的真实尾升阶结果

M24/N384 先在6次Newton后达归一残差1.69e−9，但重建 audit 的FFT要求2幂网格，因而该次 audit 失败；失败响应中的收敛state只作为下一次warm。随后M24/N512从它正确remesh并重新实际求解，残差1.54737e−9，audit完整返回。入口脚本现明确检查N为2幂。

固定原16项physical H（逐值核对相等），新增8项严格零；物理metric、depth8/parts4/steps24均不变：

|量|M16/N256|M24/N512|
|---|---:|---:|
|normalizedFullDefect|5.27697e−4|1.98512e−4|
|fullD|4.22258e−7|1.09967e−7|
|actualMetric|1.76577e−10|2.16077e−11|
|minLeading|.25798302|.25663194|
|formal κ|5.99902120|5.99902120|

它显示真实改善，但2.66倍的相对Gauss缺陷降低尚不足以宣称纯角谱误差或无限尾收敛。完整源hash、响应hash和比较在 `numerical-m2-tail-fixed-refinement.json`。

下一项实际目标由主会话提供：`root-smallcut30-k4-q02-m8` 的完整8项入口H，补8个严格零后使用M16求真实小cut尾，homotopy从λ=.25起步。默认正floor仍为.05；脚本现允许显式选较小严格正值并记录为算法参数，不接受负floor。首个真实尝试正在运行，尚未宣告匹配成功。

## 小 cut 的完整混合模态真实尾已得到

主会话前缀 `root-smallcut30-k4-q02-m8` 的实际末端目标前四项为
`[-.0002663526100916714, -.00005840795920643501, -6.290143620495577e-7, -8.024334228198851e-7]`。
完整8项均保留，M16其余8项严格零；所有同伦请求仍为
\(H_j(\lambda)=\lambda^jH_j(1)\)。下列数值是这个混合向量的
实际有限非线性响应，不是仅首模或线性尾。

第一轮10次请求分别在λ=.25、.375、.5、.5625、.5859375成功。
更大的若干步（含最后.62109375和.603515625）在首次shooting迭代前
`momentum Newton line search failed`；这些warm失败不是存在性上界。
原参数M16/N256、depth8/parts4/steps24、floor=.05未在本轮中变化。

最后λ=.5859375的真实audit保存在
`numerical-m2-smallcut30-q02-tail16-response_0011.json.gz`，对应
\(|H_1|=.000156065982475589\)，\(|H_2|=.0000200527814047972\)。

|量|实际有限尾结果|
|---|---:|
|shooting residual|2.29936e−10|
|actualMetric|4.48601e−9|
|fullD|4.23073e−5|
|normalizedFullDefect|.0098038954|
|minLeading / minD|.133547917 / .999718775|
|formal κmax|8.03370558|
|cut 首 slope|−.001839203154|
|cut meanSlopeCorrection|1.26260003e−5|
|cut meanSecondCorrection|.000511490036|

相对Darboux缺陷仍明显，当前优先进行同H、同物理尾、同径向设置的
M24/N512真求解；原16项逐值保留并补8项严格零，暂不推进λ。
该升阶入口为 `numerical-m2-smallcut30-q02-tail24-fixed-*`。

`numerical-tail-branch-locator.mjs` 对上述成功M16图沿相同RK审计网格定位：
最小A在rawCell0/segment4、r=.244049128、w=.003589442、
θ=6.160466844，距反射轴.122718463；该点主曲率约
(.00202569,−.00707804)，并非最大曲率处。minS=.999998685。
这说明当前A最小值不能直接等同于reach瓶颈；定位是离散采样诊断，
不是所有角度/参数的证书。完整记录
`numerical-m2-smallcut30-q02-lambda05859375-branch.json`。

## 实际 D–N 的解析一阶导数适配

新增独立模块 `numerical-tail-slope-jacobian.mjs`，用真实shooting tangent
和cut链式法则计算首slope及meanSlope对完整physical H的解析导数。
`numerical-tail-analytic-client.py` / `numerical-tail-analytic-worker.mjs`
在内存中适配固定源码，只替换这两类Jacobian行；二阶jet行仍明确标记
为源对称差分。原方程、metric、warm策略和接受条件不变。
完整推导、同实际解的两档差分核对及使用方法见
`numerical-tail-analytic-endpoint.md`。live同H重解核对首slope变化不超过
5.09e−21、全域audit不变，允许后续coupling使用真正解析一阶DN导数。

另为固定g前缀升阶生成 `numerical-m2-port48.json`：前32个DN数值和
physical参数直接保留port32，追加频率66..96来自固定source1024步/far48；
来源与旧port SHA256均保存在extension_source。它仍是旧weightedK6的
有限线性port，不能与smallcut30 port混用。

## 小 cut 固定目标的 M24 精修障碍

上述M16目标原16项与M24请求前16项已逐值核对相等，新增8项严格零。
同H M24/N512第一次真实求解在第2步退出：shooting残差1658.772285、
minA=.05385549；多次线搜索在rawCell0/segment4被root拒绝，较小步虽
可评估却不降残差。保存包 `numerical-m2-smallcut30-q02-tail24-fixed-response_0001.json.gz`
是**失败迭代，不是M24解**。

根据已成功M16图的A最小处曲率很小，单独进行一次floor=.01恢复，
只改算法正分支guard，g和H严格保持。它复现相同line-search失败，
末残差1658.772281；`numerical-m2-smallcut30-q02-tail24-floor01-*`
也没有成功M24解。不能把两次失败直接解释为真实尾不存在，亦不能声称
精修门已付清。随后从已成功M16的较低λ=.25先求实际M24，再沿完整
混合向量尝试接近该固定目标；这是单一路径，未开新的物理参数扫描。

全尾两jet位置诊断 `numerical-m2-smallcut30-q02-lambda05859375-curvature16.json`
进一步区分两种风险：κmax8.03371在r=.2865662、非反射轴θ=.834486，
A=.991108，其Gauss缺陷仅3.49e−10；最坏normalized defect=.0098039则
在r=.27706848、θ=0反射轴，A=.657102。后一点背景Kg=−1.30802e−5，
但有限图形式主曲率(.00843244,.00346602)同为正，Gauss残差+4.23073e−5
已经使符号翻转。这是需要解释的C2精修缺陷，不能用小metric或较好κmax
掩盖。反射轴上的最小A=.158229，也未达到目前数值guard。

## 数值匹配条件数已解决一档

M24低λ=.25在parts4/steps24时残差降至6.98e−8后未达2e−9容差；
Gblock条件数约3.016e8，minA稳定.66117。停止并保留未收敛state后，
使用 `numerical-tail-subdivide-warm.mjs` 真正插入中间匹配节点，
parts8/steps12保持原每个physical profile的96步RK网格。原289节点
逐值不变，新节点由同一非线性流计算，warm包明确不作成功声明。

随后真实M24求解达到残差2.36145e−10，条件数降至2.4533e4；
physical fullD7.26552e−15、actualMetric8.66025e−15、minA=.661184、
κmax7.994255。成功响应为
`numerical-m2-smallcut30-q02-tail24-parts8-solve-response_0001.json.gz`。
详细同网格论证、初猜兼容性与严格参数核对在
`numerical-tail-shooting-subdivision.md`。

随后M24在λ=.375真收敛，但直接增至.5的切向初猜相对改变量约.898，
残差676.65降至560.61后进展缓慢，条件数仍只有2.454e4。这次大步
已停止并保留失败迭代；不能再归咎于先前的局部传输条件数。

该M24成功分支随后沿完整混合H向量向指定λ=.5859375尝试，
从已验证.375用步长.03125接续，记录前缀为
`numerical-m2-smallcut30-q02-tail24-parts8-finepath-*`。原路径2次
请求加本路径8次，总预算为10次。λ=.40625/.4375分别达到
真实shooting残差1.66e−10/1.87e−10，随后λ=.46875/.5分别达到
3.49e−10/3.01e−10。后者经历阻尼但在9次迭代内成功，完整
H1=−1.33176305046e−4、H2=−1.46019898016e−5，cut slope1为
−.001572299831225；真包是finepath-response_0004。该中间点没有
全尾audit，不能提前当作原强目标的同H谱精修结果。
继而λ=.53125达到3.08e−10；.5625/.546875的切向初猜在首次动量
root评估失败，缩步后的λ=.5390625达到2.20e−10。请求预算用完后，
对最后真点作完整audit，成功包为finepath-response_0009.json.gz。
这次**没有达到原λ=.5859375目标**，没有在该原目标上得到M24同H
精修结论。

最后λ=.5390625的完整H首两项为−1.43580703878e−4和
−1.69726741810e−5。全尾physical fullD=2.65868838e−6，源normalized
defect=.000308049984311；还原原profile参数后为.00246439987449。
actualMetric=1.40945e−10，formal κmax=8.02216621，minA=.22258707，
minD=.99974176。二阶缺陷仍明显，不能用metric较小提前宣布谱精修
已达到容差。对这一**实际达到的同H**追加的M16真解及audit也已成功：
physical fullD=7.98793679e−6、原profile规范量=.00740420373765、
metric=8.93847e−10。因此M24的两种二阶缺陷均降到原来的.33284倍，
约改善3倍。严格输入检查与完整数值见
`numerical-m2-smallcut30-q02-lambda05390625-refinement.json`；不是拿
不同λ的M16/M24数据充作谱比较。最坏点/轴上诊断见同前缀
`-curvature24.json`，更详细解释已写入shooting-subdivision记录。

在这个λ=.5点，与既有M16真包严格核对相同完整H后，全部共同cut
slope的最大改变为5.88e−12、second为1.36e−10，meanSlopeCorrection
和meanSecondCorrection分别改变5.44e−16和1.28e−13。记录
`numerical-m2-smallcut30-q02-lambda05-cut-refinement.json` 只作端点
实际D-N/两jet比较，未把端点稳定性当作全尾二阶残差的证明。
跨parts比较时，源normalizedFullDefect
要乘shootingParts才恢复到同一原profile参数；physical fullD、metric
和κ无需该坐标修正。

## smallcut30 的32模冻结线性端口

为较大幅度neck前缀升阶，生成
`computations/numerical-m2-tail-smallcut-30-port32-r1024.json`，保持原
16模port的parameters、cut和全部16项DN逐值不变，追加真实传输得到
的频率34..64。固定source重算首16项与原值的最大差严格为0。

新增模式存在Dirichlet pole附近的大斜率，因此再作一次2048步/far48
同参数核对：最坏mode40从17396.5354404580变为17396.5353573036，
绝对差8.31544e−5，相对差4.77994e−9。完整比较在
`numerical-m2-tail-smallcut-30-linear32-comparison.json`。提供独立的
`numerical-m2-tail-smallcut-30-port32-r2048.json`：首16仍冻结原r1024
值，新增16项采用真实r2048结果。旧port未改；两者都只是有限线性
设计端口，实际非线性耦合仍须调用真尾。

`numerical-m2-make-port.py` 新增 `--preserve-port`，会严格核对同一
physical参数/cut及低模前缀，保留旧值并记录重算差。例如先用固定源
`950f-tail-linear-cusp.mjs` 对既有optimized-config运行32模、2048步、
far48，再运行：

```bash
python computations/numerical-m2-make-port.py \
  --linear notes/numerical-m2-tail-smallcut-30-linear32-r2048.json \
  --out notes/numerical-port32-regenerated.json \
  --source-topic "$FLEX_SOURCE_TOPIC" \
  --preserve-port computations/numerical-m2-tail-smallcut-30-port16-r1024.json
```

这一路径已实际重放并逐值核对published port的parameters、cut、modes、
linearSlope四个完整字段，结果在
`numerical-m2-tail-smallcut-30-port32-replay-check.json`。

## 下一项：真实neck边界方向

在上述有限预算结束后，改用已成功的原loop8
`alternative-neck-k7-v098-q070-m18.json.gz` 的完整18模终端数据。
`numerical-neck-tail-direction.py` 检查cut角图及其两jet恰为identity、
参考Z恰为零，并检查全部系数分块的SHA256。按实际桥的σ=−1和
`Z_prefix=σ Z_tail+constant`，尾请求首两项为
−2.24807581119e−5、−1.65152845668e−8，后者与首项的比值为
7.34640909e−4，明显不同于前述高H4混合路径。完整方向及来源保存在
`numerical-neck-q070-tail-direction.json`。

`numerical-m2-tail-probe.py` 现支持明确的 `--homotopy uniform` 和
`--height-multiplier`。原H已用M24、parts8、N512真实验证，并逐值核对
18项、补6个严格零高项。4次迭代后残差9.68e−10，全尾fullD为
1.72074e−15，原profile规范量9.37028e−14，metric6.00e−15，
minA=.89182943、κmax7.99425469。成功包为
`numerical-neck-q070-tail24-base-response_0001.json.gz`。

现以单一外部倍数放大所有模式，
目标首项绝对值1.2e−4对应倍数5.33789827739；此处只计划少量递增
步骤，名义取2、3.5、5.337898，共最多5次请求、失败缩步。精确命令
参数和初始真解hash在 `numerical-neck-q070-tail24-external-plan.json`。
外倍数大于1时，报告不会把成功标作原前缀目标已达到；它们是
尾部边界方向实验，**不代表已求出了更大幅的前缀**。此项尚待真尾
放大结果，原高H4路径的有限失败也不是该新方向的普遍容量上限。
