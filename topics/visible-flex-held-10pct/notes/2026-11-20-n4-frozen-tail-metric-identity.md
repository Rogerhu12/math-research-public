# 原 WeightedTailPort 的固定背景身份、校准变量与最小绑定

维护：Astra-held10-1b6d88ec-20261120 / n4_continue。

**已核实源码结论：** 当前原 weighted/native DN 在启动时仅构造一次完整背景；一次高度请求 $H\mapsto{\rm response}$ 内没有自由的 valley $\beta$、背景重分配 $\alpha$ 或 warp 校准未知。Newton 只改变有限尾的场状态。与此同时，这些背景变量本身确实决定目标度量；把它们跨配置更换，或无证明改变生成它们的数值校准设置，不能称为固定全部 $g$ 的加密。

**新接口状态：** 独立 [frozen_weighted_tail_metric.py](../scripts/resume_n4/frozen_weighted_tail_metric.py) 已写成并通过 Python 语法编译；没有启动新 worker，没有重跑旧 BVP 或尾，没有新的几何终态。原 frozen_physical_field_refinement.py 和当前 live corrector 均未修改。原未知作业不因本次源码检查取得终态。

## 1. 原背景到底是什么

实际旋转背景在一个尾单元的参数 $x$ 中可写为

$$
X_0(x,\theta)=(r(x)\cos\theta,r(x)\sin\theta,z(x)),
\qquad z_x=w(x)r_x.
$$

所以目标度量为

$$
g=(1+w(x)^2)r_x(x)^2\,dx^2+r(x)^2\,d\theta^2,
\tag{1}
$$

或在物理半径坐标中为

$$g=(1+w(r)^2)\,dr^2+r^2\,d\theta^2.$$

原 momentum engine 的 geometry(profile,x) 从该 profile 读取 $r,r_x,\log w,(\log w)_x$，然后置 $w=\exp(\log w)$、$E=1+w^2$。这些量来自背景 profile，不来自 Dirichlet 高度或射击状态。

### 1.1 同名字母的不同角色

| 量 | 实际源码位置及作用 | 是否决定背景 $g$ | 是否在当前 DN 的 H 请求中调整 |
|---|---|---|---|
| 每源单元的校准根 $\alpha_n$ | tailnext_balanced_tail 中 calibrateBalancedCell；进入 cellSegments 的低谷斜率 | 是 | 否；构造背景时求一次 |
| valley 控制 $\beta_n$ | closing_recalibrated_tail 的 getEntries(n,beta)；在指定段把 $\beta_n v(x)$ 加入 logw | 是 | 否；来自 cfg.valleyControls |
| 总宽度重分配 $\alpha_{\rm warp}$ | assemble 根据完整 A/B 积分使真实切口半径成立 | 是 | 否；worker 在请求循环前 assemble 一次 |
| 正 warpWeightLevels | closing_weighted_tail 对 B 部分乘正权，随后重算完整积分和总宽度系数 | 是；不能仅凭正性称为坐标换元 | 否 |
| actual_metric 中逐角的 alpha、beta 数组 | 从当前 height jets 得到周期展开的投影标架分量 | 是场的派生量，不是背景定义参数 | 可随场改变，不因此改变所用目标 $g$ |
| Newton 回溯步长、stage 的 Q/pi 状态 | nonlinear shooting 的场变量和更新步长 | 否 | 是 |

若仅改变一个背景参数却恰处于处处完全饱和的 cap 中，是否产生同一函数仍须具体证明；这里不把“输入数值不同”无条件等同于“函数一定不同”。但 valley/warp 输入绝不是可默认丢弃的纯求解器变量，两个配置不能未经证明归到同一固定度量序列。

### 1.2 背景依赖的实际公式

getEntries 的原式为

$$
\log w_{\rm raw}=\log w_{\rm source}+\beta_n v(x),\qquad
(\log w_{\rm raw})_x=(\log w_{\rm source})_x+\beta_n v'(x),
$$

其中指定三段分别使用 smooth、1、1-smooth。随后依次应用 cap、可选 flatOuter 和 cut-preserving 恢复规则。

令 $A_n(x),B_n(x)$ 表示该 source 构造所用的两个累积积分；weighted 版本把 $B$ 的被积函数乘上指定正权。assemble 计算

$$
\alpha_{\rm warp}
=\frac{\operatorname{orientation}(r_{\rm cut}-r_{\rm deep})-\sum A_n(1)}
       {\sum B_n(1)}
\tag{2}
$$

并以相应单元起点定义

$$
r(x)=r_{\rm start}
+\operatorname{orientation}\bigl(A_n(x)+\alpha_{\rm warp}B_n(x)\bigr).
\tag{3}
$$

因此 valley 既能改变 $w$，也会通过积分和 (2) 改变 $r(x)$；warp 权会改变 $r(x)$ 与同一 $w(x)$ 的对应关系。仅保持切口的 $r,w,w_r$ 不固定内区的 (1)，因为设计本来就允许 cut-preserving 的内部改变。

## 2. 为什么一次真实 H→DN 不会偷偷重新调这些量

已读到的 950f-tail-stage-port-v3.mjs 的顺序是：

1. 读取 config。
2. 执行一次 createRecalibrationFactory(cfg).assemble()。
3. 执行 createCompactTailDN({...cfg,tail:physical})。
4. 输出 ready，才开始逐行读取请求。
5. 每次请求只给出 height、jacobian、audit；用同一 dn 调 solve(height,...)。

原 stage-core 的 createCompactTailShooting 接受 options.tail 后直接使用这个 physical；不会退回另一个默认构造器。每节点状态长度为 $2M$，其两块是有限 Fourier 场状态。initial、evaluate、correction、solve 的 Newton 更新都仅作用于这些状态；附加两个 mean 累计量在每段积分时由方程得到，也不是 valley 或全局宽度的自由参数。

solvePhysicalCell 等设计/校准 helper 虽然存在并被模块导出，但当前 worker 的请求路径没有调用它们。单元 profile 闭包只接受 $x$；它们的缓存是背景点值缓存，不接受当前 $H$。

原 response 保存 checkpoint.parameters。它来自同一个 physical.parameters 展开再附加模式数、stage 深度、步数等有限离散说明；不是从拟合后的新 valley 向量生成。ready.parameters 与 checkpoint.parameters 因而提供了可直接比较的完整声明。

### 2.1 native provider 也没有增加背景未知量

当前 native_batch_adapter 在首次使用时，从已构造的原 cells/profile 提取静态的 $r,r_x,w,w_x,E$ 系数、三角求积值和 RK 网格，形成一个模板。以后 prepare(states,withJac) 只改输入状态和 Jacobian 开关；不重新写入这些静态背景系数。

native factory 的 mark 仅补充 shootingEvaluation、manifest SHA 等执行说明。原物理 profile、cutJets、mean/second jets 和验收仍由同一个原对象提供。因此 native 版本中的一次 $H$ 请求也没有多出的背景校准自由度。

这一结论来自真实调用链和变量写入范围，不是因为文件注释用了 frozen 一词。

## 3. 真正容易混入“加密”的背景变化

### 3.1 calibrationSteps 会进入实际背景

tailnext_balanced_tail 的 calibrateBalancedCell 在 mode=2、direction=1 上求传输矩阵下左元为零的 $\alpha_n$。该传输的有限计算使用 calibrationSteps；返回的 cal.alpha 直接进入 cellSegments，再进入实际 logw。

因此对当前有限实现，改变 calibrationSteps 不只是把**同一个场 ODE**积得更准：它可能重新选择用于生成背景的实际 $\alpha_n$。

若物理定义从一开始就是“同一个精确传输零点”，允许用更多步数更准确地评价它，但必须把两套值解释为对同一个精确根的近似，并支付根及 profile 的误差；还需要指定同一个根分支。若定义是“当前数值校准产生的固定有限背景”，则应保持该校准值/生成设置。两者不能混称。

### 3.2 warpSteps、quadratureTolerance 和 cuspAwareQuadrature 也不只是场分辨率

closing_recalibrated_tail 的总宽度、累积 A/B 和 $\alpha_{\rm warp}$ 来自背景积分；它们的有限求值受 warpSteps、quadratureTolerance、cuspAwareQuadrature 及分段/cap 实现影响。更改这些设置可能改变当前 finite profile 的求值及 (2)。

同样有两条诚实路径：固定当前背景生成定义；或者先把物理背景声明为同一真实积分/精确根对象，再验证不同求值精度对它的误差。不能一边改变背景生成结果，一边只报告场 residual 下降。

相反，M、场 RK steps、shootingParts、场 angular quadrature 是对同一背景上场方程的有限离散。改变非线性物理截断深度、linearFar 或 far Robin 的近似，还须证明/测量它们趋向同一个事先定义的深尾；背景参数相同本身不证明尾边界加密已经成立。

### 3.3 当前 q060 与 R21 的身份范围

当前 portable_bootstrap 从 q060_cosine_reference_binding 中覆盖物理尾参数，q060 的首 valley 是 4.625；旧 R21 记录首项为 3.125。两者不是一个已经证明相同的背景定义。只能说当前同一次 worker 固定了其自己的 q060 背景，不能把 R21 的连续曲率、深尾或旧常数直接搬来。

短 q060-port 的 parameters 是 exporter 手选字段，遗漏了 delta0、R、a、etaPower、etaRatioAtN0、rejoinR20At、rejoinIndexOffset 等构造默认值；它也不保存各单元 $\alpha_n$ 或 $\alpha_{\rm warp}$。只有切口五个数相等，远不足以标识完整 $g$。

### 3.4 当前 M8→M12 的 angular quadrature 128→256

已读当前 [prepare_lifted_mode_restart.py](../scripts/resume_m3/prepare_lifted_mode_restart.py)：它从原 tail config 复制，只将 modes 改为新模式数，并将 angular quadrature 倍增到严格大于 $4M\,{\rm spacing}$。对 M12、spacing=3，128 不足而 256 足够；没有改变 calibrationSteps、warpSteps 或 quadratureTolerance。

这一次 angular quadrature 不进入背景组装，理由来自上述实际构造器：closing_recalibrated_tail 在调用深源时显式写
modes:1、steps:1、quadrature:16，独立传入 calibrationSteps；A/B 积分另用固定 G8/G16 和自己的背景积分设置。weighted wrapper 对累积积分只读 warpSteps，不读 cfg.quadrature。cfg.quadrature 后来用于 momentum engine 的场角求积，而其 geometry(profile,x) 仍只读已固定 profile。

因此，在其他配置保持时，这个模式数/场角求积变动没有重新选择背景函数；即使展开 parameters 为记录目的保留了 quadrature 字段，也不能因此把它误认为背景积分阶数。升模的完整参考补偿和新的 BVP 是否通过仍分别核验，这个源码身份结论不把当前设计延拓变成 README#5 已完成。

## 4. 最小完整冻结对象与能检查到的身份

对目前已读源码，完整背景定义至少包括：

- 切口和重分配：rCut、wCut、width、curvatureBound、orientation。
- 深源及有限修改区：delta0、R、a、etaPower、etaRatioAtN0、prefixR、prefixEnd、prefixReturnStart、protectCell、rejoinR20At、rejoinIndexOffset。
- 形状控制：全部 valleyControls、warpWeightLevels、slopeCap、capTransition、capMode、pulseCaps、valleyCaps、flatOuterThroughCell、flatOuterStartSegment、flatSlope。
- 当前有限背景评价设置：calibrationSteps、warpSteps、quadratureTolerance、cuspAwareQuadrature。
- 源定义：实际 weighted/recalibrated 构造器、已验证依赖中的 cellSegments/smooth/calibration/rejoin 实现及其默认常数。派生的 rCuff、oldCut、epsilonScale、prefixRByCell 也保存比较。

完整 $g$ 还包括前缀 profile、真实切口坐标映射及整曲面各拼接块。q/c、核心窗口、mean 高度原点和 $t$ 范围即使不全是旋转目标的参数，也属于用户要求保持的完整物理设计；原 FrozenPhysicalField 的冻结范围继续适用。

可直接核的现有字段是：

| 记录 | 内容及限制 |
|---|---|
| worker ready.parameters | 默认值展开后的完整 physical.parameters，加当前有限离散参数；应从这里取得背景定义 |
| response.checkpoint.parameters | 每次实际响应的完整声明，可与 ready/上一层逐项比较 |
| ready.cut 与 response.jets | radius、backgroundSlope、backgroundSecond、E、Ep，应在同一 worker 的 H 变化中保持一致；只证切口，不能代替内部定义 |
| client config 与 source_sha256 | config 在 client 记录每次响应时重新从文件读取；若启动后编辑文件，日志可能与已加载 worker 不同，必须禁止这种混淆 |
| closing_tail_dependency_blobs | 底层 profile/calibration/rejoin 的固定源码；现有 loader 启动时核这些 Git blob |
| native static metadata | 实际 profile 的静态系数和网格摘要；仅为该有限求值的记录，不是连续函数证书 |

现有 response 不单列每个 $\alpha_n$ 和 $\alpha_{\rm warp}$ 的实际浮点值。完整配置、源码和固定构造路径已经足以确认一次请求没有 $H$ 依赖的重校准；但若跨实现、跨校准精度要声称同一**精确** $g$，仅比较这些 metadata 仍不能替代真实根/积分的数学误差界。

## 5. 独立绑定接口及其拒绝范围

新文件不修改任何现有 worker、live corrector 或旧场校正源。它包装一个**已经启动**的原 WeightedTailPort：

~~~python
from frozen_weighted_tail_metric import attach_frozen_tail_metric
from frozen_physical_field_refinement import FrozenPhysicalField

# obj 已经解释为 fixed=True 的完整物理前缀，
# obj.tail 已经是原真实 WeightedTailPort。
guard = attach_frozen_tail_metric(
    obj,
    # 第二层及以后提供第一层保存的小型完整背景定义：
    # expected_definition=previous_guard_definition,
)
frozen = FrozenPhysicalField(obj, par)

# 留给同一物理设计的下一层：参数和源码标识，不含场数组。
guard_definition = guard.definition
# 正常运行原 frozen.correct_once / 原完整审计；这里没有新调用它们。
~~~

绑定执行以下实际检查：

1. 读取完整 ready 背景参数，要求所有现有必要字段，拒绝把短 port 当全定义；将显式 config、prefix port 中已有的背景字段与 ready 比较。
2. 固定实际 worker 对象、完整 ready/config/source 记录和原 prefix port。旧 client 会在每条响应记录时重读 config，故 wrapper 在请求前后都检查它没有被编辑。
3. 每条真实响应都要求 checkpoint.parameters，比较完整背景字段；五个背景切口 jet 必须与该 worker 的 ready 值相同。
4. 跨数值层时可传 previous guard.definition，锁住背景参数和几何源码；纯场分辨率字段不混入这个跨层背景签名。
5. 原 true DN 的收敛判据、残差门、正根域、请求参数和响应值全部由原 client/调用者继续决定。绑定不以自己构造的仿射响应代替真实尾。

配置身份错误抛出 ValueError 子类，不能作为一个可回溯的域失败被 Newton 静默吞掉。若 prefix port 和 live ready 的切口有限求值有微小差异，description 保留五个差值；原完整 seam 审计仍须支付它们，不将其改写为零。

**边界：** 这只保证当前调用没有偷换声明的有限背景，不证明该背景与某个精确无限尾同一，不证明当前场通过任何门，也不证明 README#5。当前旧 FrozenPhysicalField 源若单独使用，仍缺少这里的显式尾背景绑定；不能仅凭它冻结了 q/c/profile，就自动宣称跨 worker、跨校准设置的全部 $g$ 也已冻结。

## 6. 源码复现依据与本次验证

只读核对的恢复清单为
[scripts/nonlinear_tail/m3_coupled_seed_deliverable/m3_source_recovery_manifest.json](../scripts/nonlinear_tail/m3_coupled_seed_deliverable/m3_source_recovery_manifest.json)，
SHA-256：

~~~text
8e177f9cd0ab54d6db1d29baff4faad5ba5fda5f073c4743ab55d35dda73576e
~~~

其实际恢复的两个几何构造器未因 sparse/shared/periodic/native 补丁而改变：

| 文件 | SHA-256 |
|---|---|
| closing_weighted_tail.mjs | 740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e |
| closing_recalibrated_tail.mjs | 4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6 |
| closing_tail_dependency_blobs.json | 71d6aa7ced8ee553901a7c2748d569359dace927fc6573eaccd5032714c3fa60 |

底层被核对的 Git blob：

- tailnext_balanced_tail.mjs：0bbb0b21150158e514596155de2d5c35c37e7613。
- f6tail_r20_rejoin_source.mjs：1ef9371db3a05f9167b1934046517c47dd9406f5。
- general_root_smooth_tail_cells.cjs：3b98e488e05b2cce59ff8d9d03b4ad78302d8efa。

native 核查的是 [native_extended/prepare_recovered_native.py](../scripts/resume_n4_tail/native_extended/prepare_recovered_native.py) 所生成的同一调用路径，以及 [native_batch_adapter.mjs](../scripts/resume_n4_tail/native_extended/native_batch_adapter.mjs)、[native_batch_factory.mjs](../scripts/resume_n4_tail/native_extended/native_batch_factory.mjs) 的静态/状态写入分离。q060 参数来源是 [portable_bootstrap.py](../scripts/resume_m3/portable_bootstrap.py) 和 [q060_cosine_reference_binding.json](../scripts/resume_closed/q060_cosine_reference_binding.json)。

本次新文件执行的命令仅为：

~~~text
python -m py_compile topics/visible-flex-held-10pct/scripts/resume_n4/frozen_weighted_tail_metric.py
~~~

真实 exit 0。没有执行绑定后的真实 DN、BVP、区间积分或固定参数精化；不能把语法通过写成这些计算的成功。该小接口本身不保存数组，实际 full field、stage state 和可重算数据仍只留临时计算目录。

