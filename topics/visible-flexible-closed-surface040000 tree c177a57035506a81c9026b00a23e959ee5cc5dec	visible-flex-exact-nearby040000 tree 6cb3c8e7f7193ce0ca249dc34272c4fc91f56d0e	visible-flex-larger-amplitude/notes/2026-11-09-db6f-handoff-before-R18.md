# 交接：可见且有厚度的闭曲面等距弯曲

会话：Astra-visible-flex-db6f0b0e，2026-11-09。**尚未完成：R17实际闭C²族D≤3.92、δ_hold/D>.05099275、δ_E>0；现完整尾metric≤9.96894e−7、κ≤8.465446已过门，合全support给reach/D≥.0301345。完整tail独立重放逐行相同，继续固定g加密至求解容差（G5），不能报完成。** 下列短名均在 notes/2026-11-09- 下。

## 完成门与冻结主候选

严格按本题README：连通闭M的C²连续嵌入族；固定闭H有内点且diam(H)≥.2D；不对齐δ_hold≥.05D，另证δ_E>0；全部t reach≥.03D；同一g全域相对metric≤1e−6；物理metric/参数/t范围冻结后网格、频率和时间加密趋机器/求解容差，不以固定taper或改物理层数压缺陷；未参与者独立重跑及几个<5MB网格。更强目标继续保留。

主候选 **flat17**：outward vu=.17、vd=.18、ramp=.4、ramp_eta=.05、cycles1；delta=.07254443456654512，warp_reference_q=.1。weighted K6尾 width=.45/rCut=.6/wCut=.5/protect160；rCuff是输入的精确差，不默认为有理3/20；无中央柱ell=0。物理profile完全冻结，求解q略变不算改g。

### 同一g的实际求解

- M8/32真联解：`db6f-prefix-flat-v17v18-coupled-m8-q10-fine.json.gz`，最终tail同stem `_tail_0017.json.gz`。778nodes、17DN；prefix metric sample1.11866e−7，tail3.16462e−7/fullD6.25149e−4、minA .19508944；cut mean二阶差1.34e−10。
- M8/64真联解：`db6f-prefix-flat-v17v18-fixed-m8-d10-p2-s64`，最终tail_0018；q=.0999999298851，prefix2570nodes、tol2e−9、metric1.11838e−7；tail3.1785e−7、mean二阶缝−1.83e−11。M8频率截断平台，不能说径向metric趋零。
- M8/128真联解已成，用可选“内层仿射DN+外层完整真DN校正”，4次真实DN，原始BC残差7.216e−16；64→128同g/同prefix tol的六项物理jet差：C0 1.905e−10、Fs2.474e−10、Fθ8.582e−10、Fss6.554e−9、Fsθ2.607e−9、Fθθ3.972e−8。见 `db6f-prefix-fixed-g-convergence.md`、`...radial32-64-128-cauchy.json`。
- M12/depth12/parts4/steps64完整联解已成功：`db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64.json.gz`及tail_0018；2570nodes、tol2e−9、collocation1.997e−9、BC1.016e−18；prefix actual metric8.95134e−9（比M8降12.49倍），尾sourceMetric1.964966e−8（降16.42倍）、minA.191565、shoot1.54224e−9。CP旧scope误留linear字样，另附勘误，不改CP hash。M14/N256真联解已成：BC4.18e−17、shoot3.86e−10、tailMetric8.56e−9，但prefix7.95e−8反升已在源Galerkin曲线，非Hermite；不能称单调。旧M16停滞已留档；新M16从完整M14接续，最终N512真DN。新增mode须先升raw height/slope再重算momentum，不能直接补零momentum。

## 已支付的具体中间输入

1. **前缀连续几何与metric。** M8精确共享jet Hermite841nodes：σ≥.8126404343、κ≤5.606077、半周期见证≥.199891596；v2 metric≤3.622549869e−7，独审和独立全量复跑PASS（db6f-root-review-metric-v2）。v1曾漏邻piece薄片，已修且保留失败。新M12/F24有2570nodes，root运行同一已审后台得metric≤2.568629447e−8、σ≥.814440512、κ≤5.547266、见证≥.199891143；目标frozen_profile与桥常数逐字段和M8完全相同。M12共同cut-v2全前缀metric≤2.572086e−8、κ≤5.547266；Δ两jet≤3.48e−12/5.19e−12/3.37e−9，待独审。
2. **精确桥root缺口已有预算。** `db6f-exact-bridge-and-metric-transfer.md`/`db6f-root-exact-bridge.py` 定义真实cut w=.5、wr=−7w/c；用Fraction Taylor积分正负端点夹唯一L*，非信任Decimal初猜。径向常数重新参数化使旧有限图对精确匹配g的误差≤3.622553187875372e−7，新增target预算≤3.319322e−13。tail_theory全文独审与独立复跑PASS；物理尾正精确归一α、真正空间接缝仍另付。
3. **显式全尾及一阶连续界。** `db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json` 定义共享C²积分Fr五次图+精确R6圆领；源/导出均32步。独立连续Fourier/Bernstein界：|Vh|≤.000139095294、|Vz|≤.000835043294、Jxy/r≥.9949233155，截面严格星形、整个尾的水平投影为嵌入环域。`db6f-audit-tail-first-and-phase`独审与全量复跑PASS。尚不是metric/κ/全曲面嵌入证。此旧宏观包仍用绝对r；新 `db6f-tail-inc-flat17-m8-native64-n8-s64` 用Δr精确和/共同归一防消减，另待认证。
4. **尾的收敛与固定定义。** native64→128全XYZ metric采样均约3.22e−7。coupled连续比较27697共同跨：尾扰动C0≤7.58e−10、θθ≤4.77e−8、rθ≤6.70e−7，但rr≤.0324932，最坏r∈[.5209378646,.5209492975]；未到全尾C²容差；已定位raw0/5窄cusp插值，真source Vrr同点64→128仅差4.63e−8；固定source的critical局部加密使height rr测试差从.00498降至2.63e−8，完整XYZ adaptive导出正做。旧CP仅细导出曾把shoot误差挤末端，已保存失败；须native重shoot。finite source0..159 calibration冻结为精确binary几何参数，6组源完全一致且在[.5,2]，SHA bcfaba00...ca9f4；n≥160仍用已审无限深定义，不能随calibrationSteps改g。
5. **精确背景与紧α。** 整个背景height<.083159188、0<w≤16/15、实际背景κ≤6、|w_r|<24均已交叉独审。冻结source的高阶Taylor积分及余项、内段临界值A与剩余B账本亦经独审/全量复跑PASS：α∈[97.64534740775791,97.64534740780157]，仅α不确定性贡献metric<2.185e−12。见 `db6f-audit-high-order-and-tight-alpha`。v1无效CLI参数guard缺漏不影响绑定正式输入；作者留快照并补v2。primitive/inverse与stable等价源已审；raw0/1全18profile原函数root独立重放逐值相同。w/wr producer已审并修跨raw边界内界；strict prefix4999行root复跑全部相同（db6f-root-review-background-packet），suffix四计划/全部overlay独立重放5237行全相同。
6. **体积矩与固定帽。** R16三固定凸起（中心半径.08、局部半径.03、高.0005）κ≤10/3，B3=3πa³b²h0/4>0。R17已对实际公共接缝闭图证明完整A3>.433598，三阶中心矩张量范数严格排除含反射的全部E3全等；两份独审与矩重跑PASS。
7. **全相位。** `db6f-all-phase-assembly.md`独审PASS：活动带Fα=RαF0(s,θ−α)，帽固定，圆领完整两jet使全域C²及C²连续。数值ψ必须反解θ=ψ−e(s)sin3ψ/3，不能直接平移ψ。相对metric、同轴support/κ/球包络在全部α不变；R10处理全时reach。τ只定义在活动带；帽误差0，逐块上确界保持。相位区间须含π/3。

## 正在组装与明确未付

- root `db6f-root-tail-seam.py` 检查全部Cartesian cut jets。导出尾原H'(r)=+w，上尾必须将整个Z（含V及其两jet）反射。正确宏观M8/32的切口诊断差 C0≤6.51e−10、C1≤6.46e−10、C2≤1.77e−8；前缀16圆柱模、尾平面需32模。现已定义exact共同cut修正 `db6f-root-common-cut.py`：53跨、W=.14826、32模，重算metric3.6225994883e−7、κ5.60608、见证>.19989159637，值/混合/全部二jet按同一公式精确匹配；完整构造见db6f-common-cut-and-closed-map，独审/294项Fraction端迹核对与4项复跑PASS；此同一M8图的尾metric/κ现已连续验证过门。
- root闭图有理账本 `db6f-root-closed-budget.json` 已算：全support>.73704、D≤3.92、δ_hold/D>.05099275、完整未标记A3>.433598，R16给δ_E>0；公共接缝/全局预算已全文独审及4项新输出复跑PASS，正式R17；仍只是几何完成，非本题完成。帽矩可用全部加帽幅度的正support/散度定理支付，不借未得reach。
- **完整尾已过门。** `db6f-audit-tail-tight-full.json`（ed175后台）覆盖5237盒、collar+4637跨：metric≤9.96893823788e−7，实际κ≤8.465445374；R10结合R17全support>.737给reach/D≥.030134509。supplier方法、表示/三公式已交叉独审；新overlay/wr继承helper经root审读，root全量consumer重跑5237行全部同值。最终包 `db6f-audit-tail-tight-final-packet.json`，保留strict前缀、宽suffix、5跨局部depth2/3修正；不以工作容差充当真实门。
- 精确圆领误差随表示N降低，始终同一无限g；纯M12 N8闭合metric界5.36e−24已独立Fraction复算，不等于实际无限非线性图存在。公共外域C² Cauchy/严格存在性仍有差距，诚实注明。
- R17与新尾证书已支付全部有限图的几何/metric阈值；严格汇总R18正做。M8背景→M12精确物理网格transfer已成28928盒，独审/全量重放PASS；physicalDepth仅shoot截断，protect160固定。G5加密未到求解容差，网格交付与最终未参与者全流程仍待；继续更强比例目标。

## 结果与复现

R1–R12均为已审中间引理；R10是完整C²球面图正support+实际κ给reach≥min(σ,1/K)；R12是regular cut holonomy定mean/二阶。R13无柱镜像与法向见证；R14旧指定有限前缀连续几何；R15内尾背景与有限圆领界；R16固定帽体积矩非全等条件证明；R17实际有限闭图的全相位嵌入/宏观held/严格非全等（未付尾metric与reach）。均不等于本题完成。

当前仓库 /workspace/scratch/db6f0b0e7462/math-research。恢复旧950f未发布248文件约21MB，manifest=db6f-recovery-manifest，已推。43个实际源依赖冻结到本题repro/source-root，之后用此--source-root。只写本题、QUEUE自己行、根LOG追加；终端git pull --rebase后push，不强推；令牌仅终端环境，数据不经集成/对话，>1MB压缩、单文件<5MB、无PDF。最近确认main 3b9d750b5（R17/紧α/内尾与全部已完成复现数据已推）。

分工：coupled_prefix跑真实联解/固定g加密；tail_theory做全尾表示/背景/独审桥；independent_geometry未参与优化，做连续证书/独审/正α；root负责闭合组装/全局指标/H与主线。旧H均已归档，不丢失败路线。
