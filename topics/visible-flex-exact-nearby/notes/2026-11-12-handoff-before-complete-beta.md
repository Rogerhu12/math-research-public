# 交接：可见振幅数值解附近的精确等距解

会话 visible-exact-astra-f6a2，2026-11-12；**进行中，主目标未完成**。

## 规矩、同步与完成标准

连通闭C²精确同度量嵌入族；固定有内点H、diam(H)≥.2D；held位移≥.05D；
含反射δ_E>0；全时reach≥.03D。有限模、线性、条件式、浮点、障碍都不算完成。
最近已读规矩提交：cac21c4371f2681805882b9c891c143a5d1d54d9（根README、本题README）。
每次pull只读两README差异并立即应用，至少每小时pull。根授权/全部规矩1–13、
本题README、原HANDOFF/open/log及8篇旧Markdown notes已完整读过。用户明确授权
读其它文件夹；只读外题，未改外题。提交前pull，不强推，保留并发更新。
并行者不执行git；只stage明确冻结清单，不stage live进度或__pycache__。
上一批已推be982bd6ec488db1fdf01e4d65d1390cb351b465（R53–55/原图连续包）。
本批登记R52、R56–57、参数盒/真实ODE校正及root复门。更早恢复/hash详见
notes/2026-11-12-handoff-before-core-certificates.md及be982版本H，不能覆盖失败。

## 2026-11-12 07:46 UTC 环境恢复检查点

执行环境整体丢失，所有旧会话失效。最后本题成功推送
f064d89654c5b1becd9e0ffdb90af2229fc88306（R52/56/57和实际ODE包）仍在main。
已重新稀疏clone并显式pull；两README对上次1606提交无变化。
R58、R59、R60、full Arb collar、exact-affine第二步射线、参数根/型别/标量
后续包未推，原输出丢失。旧摘要不能代替数值证书，按恢复note重做。
恢复规范路径未变；旧来源/结果SHA见notes/2026-11-12-executor-recovery.md。
各owner恢复源码后立即分批推送；三线继续计算，不能在恢复或中间结果收尾。
R60正文已重建，实际残差输入仍欠；R59旧592-cell全跑仅见500通过，须整跑。

## 立即继续，不能停在中间结果

1. constructive的准确sym affine evaluator/dense runner已恢复并重跑258点。
   δ₂=−15291006546051/9007199254740992，真实Emax7.8954e−5仍未接受；
   新同图Newton给δ₃=−.0016984827643356504、H129，须紧root及516真节点检验。
   两步都用R57同一准确affine曲线，不转授旧rounded/mirror对象。
2. 原图full Arb collar已重新证明1305.4032588697..1305.4032591712；
   root全文审源并224bits独立合成。bulk分0..3、4..83、84..166三份连续
   完整覆盖正在跑；完整β未付。下一对象是当前准确δ，而非原D5中心。
3. 准确affine全参数型别/point-root/scalar已重做；169闭单元support全过，
   N<−.31819107、ζ>.68787339、跨腰圈|ell|<1.805322。复几何图表继续。
4. R58新mixed源/结果已独立全JSON复算一致。R59全592单元宽θstrip1/64
   已证明|nraw|>.28049754；R60定理已独审。新首43两腿trace、准确jump、
   q=exp L正权和H初值误差均已重新冻结。它们仍不支付真实ODE e0/e1。
5. 下一实际缺口：全初值解析reference的连续残差、全管二阶源与Wiener
   残差，完整β危险格/参数KAM、有限低块/ordinary sources、真帽及Killing
   匹配，定量Newton与同一精确族的几何比例。不得停在本恢复/条件结果。

## 原 step02：有限候选与严格对象

data/phase_ring_continuation/type_fixed_step02.npz，SHA256
05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883。
M24/n201/Gauss3/Q256quarter，radius_shift必须保留；β4(0)=.20747484022400084。
alpha=(.7396093769906578,−.005100267374734773,−.049352132159964625)。
样本metric7.84528e−5、腰比代理.0515009792，不是等距解或闭面。
冻结mean0/2的三步全历史见notes/2026-11-12-constrained-mean-continuation.md。
Schur软列同时改E、a，不是固定metric核；参数搜索同步g0(p)，选p后才冻结目标。

严格对象：物理a/β显式取偶、γ/Z取奇；Z准确积分冻结slope，再作无限R33
角原函数。无Gaussian；原binary knots/height不能假定已严格反射/积分一致。
完整快照type_fixed_step02_analytic_smoothing_inputs.npz，SHA
bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532。
以下原图证书只属于这个对象；各note均同2026-11-12前缀。

- symmetric-root-interval：t∈[.2383698,.2383701]，C′>300.5184，K0′>60.1022。
  common span(.2375,.23969803864366687)，实collar半宽1/4096内45<K0/(x−t)<75。
  symmetric-root-tight另给t∈[.23836991573145,.23836991573148]，不覆盖旧包。
- symmetric-core-scalar-gates：全|x|≤.25，Q=Fz/x>.94476942414、Fx,z>.94255365317、
  area>.84960041123。root独立全JSON重放相同。
- symmetric-core-N-support-interval：174闭span/全部角，Nraw<−.39163955818、
  N<−.31863118221、h=F·ν>.80688764949、ζ=h/|F|>.68864540976。
  JSON SHA36a83e821e7ca2572fdc95378d688505c1fee788b633e7f0195ff61ecf35eeac；
  source SHA f489e86dadf7d013d5044fa3b7588b9699268f2db3923d80419a811cb077b40b。
  root以Q512复算6关键单元符号全过；不同网格膨胀不能混最紧界。
- symmetric-ground-state-log-gate：全实G=Fz/(x|F|)>.80137467107，
  |ℓ|<1.807519、|ℓr|<27.579692、|ℓθ|<59.324319。准确ground-state含腰圈。
- symmetric-root-complex-gate：共同实collar×|Im r|≤2^-16×|Imθ|≤2^-11，
  真分母/平方根分支均严格非零，32.13<|K0/(r−t)|<88.49，|ℓ|<7。
  |κ|不是Reκ；窄tube不是collar半径复圆盘。root独立JSON逐项相同。

旧uniform-tail的1396单元六jet≤1.130e−10只含尾/alias；root/core另加有向
三角DFT舍入。Gaussian h1e−5的C²差4.262e−6是备选对象，不授予旧返回。

## 新 D5 与参数管

p=.4413514918092046；有限候选type_fixed_step02_d5_jet_corrected_probe.npz SHA
0dcfb37f84a1b3d6197b375aa8700628a00398c0b509ce5da6c92f1ecf489199。
样本metric7.9227e−5、腰比.05150175。明确sym无限快照
 type_fixed_step02_d5_jet_interval_inputs.npz SHA
0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b。
旧真实射线用了近似mirror，仍须重算明确sym map或支付对象变更。
原图ζ/Q/β不能搬给D5；R37速度必须用G_actual，不能用G0。

R55：全|r|≤binary(.24)、592闭span/全角，Φ>.37235、−Nraw>.42529、N<−.3092。
自身根[.2383968,.2383972]及有理中心.238397半宽1/4096 collar，53<K0′<68。
原冻结12件清单R55-and-staggered-frozen-manifest.json；独立2单元因式/直接叉积
均通过，root全文/代码/全部hash及准确collar覆盖已核。

R57：raw控制c+δv、alpha+δw，|δ|≤binary(.01)。更大独立控制点盒592cells
N<−.30865；只有保持相关性的affine子族另有根(.238394,.238400)、common collar。
第一步rounded predictor SHA566c9561...及全部19296phase+3mean准确入盒，因此
继承N/复角门，但不能仅因入盒继承affine根。新输入完整hash在冻结manifest。

R56：原图、新D5、整个R57盒均连续通过物理θ strip1/256，Re Nraw分别
<−.17256、−.19294、−.19191。准确速度为−Mraw/Nraw−σ√−K0 Gactual/Nraw。
全部分母/全实径向/全角已付；这只是系数域，不是返回域。真实Jacobian的
Riccati门仍须全部实初值J与二阶系数积分，不得以有限射线代替。

## 已证算子：实际输入尚须各自供齐

results.md索引R1–57。R1–24旧几何不转给当前图；径向逆不能吸二阶非径向项；
共轭共振不等于PDE核。R30–34付参数KAM/完整β危险格，R35–44付真实正cap、
完整source/固定型别/有限Airy/直接log权/Dyson首符号等，均未代付实际全网。
R45：内部2/3、K=−H*、所有正负窗口/root/regular交叉、实际Airy Cayley。
R46：真实Cauchy/frame/polar及strict R2，完整β物理有限部和PT校准。
R47：有限Taylor/cutoff的完整lag/mean/物理source及B∂/伴随，无椭圆Cauchy。
R48：dyadic H和D5=(15121+√5)/27422、D8=(4852+√8)/8804，cohom K=3/2。
R49：真实symmetrizer的同log宽任意ε损失双向Cauchy/普通源。
R50：β分部降阶、真实bulk三jet/new g0,g1减项；固定R37同一ℓ/χ。
R51：真实虚部Ms<S与Wiener复合，须覆盖全部Newton/参数Taylor线。
R52：真根Taylor/固定物理cut及全部无限尾、角均值、径向预算，不等于β区间。
R53：共同自伴根shear，负trial强R2，正物理source5/3、新frame cap反射−I+R2。
R54：准确固定cut矩阵/Airy frame给同一自伴首符号+R2，全lag/mean/cross保留；
全网经η损失后R2−η。R53–54已独立逐式核；真实低块、cap和所有系数常数仍欠。
R55–57见上。任何candidate变化都须重算或支付变化预算。

## 失败、外题与恢复

旧canonical三正根/外负环、仅消外环predictor核心N正、quarter1外环负、
M32三步C²差.623/.461/.862及exit137全保留。旧weighted M16 degree1已含振幅，
make_candidate(series,1.,order=1)，不再乘.06。各已推清单见永久notes/旧H。
源continuous-flexibility-swarm/R520全文已读；其固定充分小q完成不含本题5%预算。
be982下该题当前README/HANDOFF亦全文读，准确SHA/阅读范围在source-transfer笔记。
R492/R499/R513/517–519只引用实际读过范围；root已完整核使用的R499 B3–5。
邻visible-flexible-closed-surface仍未完成；旧近似几何不授予当前图。
只取使用单文件，不递归抓大库；main规矩变动立即读差异并更新本H。
