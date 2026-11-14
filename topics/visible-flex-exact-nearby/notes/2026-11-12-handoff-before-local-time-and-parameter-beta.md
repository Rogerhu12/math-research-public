# 交接：可见振幅数值解附近的精确等距解

会话 visible-exact-astra-f6a2，2026-11-12；**进行中，主目标未完成**。

## 规矩、同步、完成标准

连通闭 C² 精确同度量嵌入族；固定有内点 H、diam(H)≥.2D；held 位移≥.05D；
含反射 δ_E>0；全时 reach≥.03D。有限模、线性、条件式、数值、障碍都不算完成。
最近已读规矩提交：e7b5eba551c85a7cb1e64a905809a76a2303abdd（根README、本题README）。
每次 pull 都检查两 README 差异，有变只读差异并立即执行，至少每小时 pull。
根授权/全部规矩1–13、本题README、原HANDOFF/open/log/notes均已完整读过。
用户明确授权读其它目录。只改本题和根LOG；提交前pull、不强推、不覆盖并发成果。
根LOG每批一条≤200字；本题log≤5行；Markdown<100KB、H<10KB；>1MB数据gzip，
单文件≤5MB；大可再生中间量存脚本/参数/hash。仅stage显式冻结清单，避开live进度。

最近已成功推送 main：096c916456e691f920d7ac2d2ed742bb05cde5c7（约08:58UTC，
73件完整原图β/R61/复角chart/δ₃516/旧诊断恢复包）。
前一恢复包af76d3e08b705df035ab5f0d20f6cb8d54f0d6c6含R58/59/60及首dense。
恢复备份分支 visible-exact-recovery-f6a2-20261112-b 的 e6ed9c25026e346cd29fb7ca0adf0fbcc336aad6
是前包rebase前记录；本批备份c=41bfb335749520d8afe12b426159df81e9163639。本次提交登记08:50后完整β/R61/δ₃包；工作中的新源与live输出仍不属于已推结果。
约07:46执行环境曾整体丢失；旧未推包已按下面的恢复记录真实重算，不能引用旧摘要为证书。
旧完整交接已原样归档 notes/2026-11-12-handoff-before-complete-beta.md；更早背景、R1–57、
失败和全部full SHA见该归档、results.md与notes/2026-11-12-executor-recovery.md。

## 立即继续的实际路线

1. 当前准确候选 δ₃=−7832869216826619/4611686018427387904，H129。
   完整516真实射线 Emax=1.99776073018e−7、E′max=1.8454208483e−5，未KAM接受。
   同对象按真实knots分步、rtol2e−12的516点正在跑；之后继续实际Newton。
   下一候选改整批516共用时间网格并按32 accepted segments分片，便于R61验证。
2. R61已付全初值角解析参考+端点Wiener接口；δ₂ pilot 的连续Bernstein有限界全过。
   下一步是同一最终参考的真实 e0/e1 全时间/全初值条带包络、C2场界、两腿与参数门。
   reproduce_newton已跑通严格ordinary span的时间Taylor prototype；Q512消去主尾误差，
   正接入真实Bernstein参考。不得把局部演示冒充881段或全初值验证。
3. 原图完整β已严格完成并独立核验；δ₃ collar已完成，主体bulk两份正在运行。
   最终参数点/盒尚未定，β必须跟随同一对象；参数区间root及β′接口只作准备。
4. constructive负责 R62 固定τ根链式二阶参数源/真实变分，避免固定r伪奇项；
   independent_audit负责δ₃完整β/邻域；root负责全初值参考、复管与总整合。
5. 随后仍须实际KAM、完整传递强余项/有限低块与ordinary sources、真实正帽、
   相对Killing兼容、残差因子Newton及同一精确族的全部几何比例。不能在本中间结果收尾。

## 实际对象身份，严禁转授

原始sym输入 type_fixed_step02_analytic_smoothing_inputs.npz：
bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532。
D5 affine origin type_fixed_step02_d5_jet_interval_inputs.npz：
0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b。
方向 type_fixed_step02_d5_actual_parameter_direction.npz：
8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab。
raw c0+δv、alpha0+δw 先按准确实数施加，再作径向偶奇平均；高度准确积分slope，
角向为无限R33 primitive。Q256/512只作带误差的表示，不另定义真实图。
δ₂=−15291006546051/9007199254740992，对象 aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1；
δ₃描述 e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f；
δ₃ dyadic H 028a95679f5c6e6ff6438b539c9c427f745f976a4dbc70b46c0bb01dd0f4fb49。
所有位置在data/phase_ring_continuation；源/命令/依赖见对应冻结manifest。
旧rounded第二步input1ef92be77cff11904b656c33b3e74994d6415428160319cd92b5df2717d36e14
只属于旧mirror模型。uniform129误差1.7886797465e−6、staggered129误差7.8846588582e−5
均已重新实际跑完；其point-root/N包含及原D5 MP诊断也已恢复，不授予准确δ₃。

## 已证的实际连续几何与完整相位

R57 whole独立控制盒实N<−.30865；只有准确affine子族另有共同简单根及型别。
accurate affine全实169闭单元给 N<−.31819107、ζ>.68787339，|ell|<1.805322。
R58 mixed参数根jets全JSON独立重跑一致：t′∈[6.09017437e−5,6.13118355e−5]、
t″∈[−9.61182263e−7,−9.19232306e−7]，近根退化商Q的参数二阶也已付。
R59 whole592单元物理角宽1/64给 |nraw|>.28049754，不等于Re nraw<0。
旧1/128实部门失败31个单元、最大上界+.1224366898已重新保存；新模长全过。
affine复角chart同θ宽1/64已证Re(Q)> .94248569、Re(F·F)>.64513410、
Re(area²)>.91127224、Re(support numerator)>.92958433，|ζ|>.51007583、|ell|<2.90805284。
其证书 a1bfb82ee751e31a51a9997804ca2da68aaa4eb76b63081f1e4c0f9806e68a8f，
源0f0f27282edc5ef4baf29c3abfb3d67264216495d6e0821872a8da26e9f3cfde已全文独审。
仅r、δ为实数；这里未给径向复域或已验证返回流。

原sym完整β：36.79967508215<β<36.80349990665。
167真实knot spans，259被接受子区间+腰部，无缺口/重叠；root独立Fraction覆盖、
224bits分别端点求和及全部积分源逐式审查通过。D5危险格距离>.42801799599，
但原sym真实principal rotation尚未调D5，β不转授到D5/affine。
完整报告 da84c1a8ff5b1a5b00d33c236d37752a5ffa4d187bc88115f99db473742c52f2；
证明 notes/2026-11-12-symmetric-complete-directed-beta.md；独立审核见
notes/2026-11-12-beta-full-cover-and-chart-independent-review.md。
δ₃真根 t≈.2383968737297399329298489762，tight证书 afdc964a11682f9c54ceb1e6a165950f007ea26ab917f8dbde8b38c9fe78629f；
collar严格1307.20897680857..1307.20897711147，报告037cd700677da4a34b423de431e9b22ab9903b5cd844a6a9348e6ccd0ee8918d。
δ₃ bulk 0..83/84..166正在跑；不得用未完成和live输出宣称完整β。
测试δ₃±1e−8仅统一根区间已证，不是最终KAM盒；最终δ还可能再移约1e−5。

## R60/R61 与参考的准确口径

R60/R61以 e0=Yτ−f、e1=Lτ−fθ、q=exp L，付连续残差积分A/B、C2源积分C。
r=r0+A、Δ=1−exp(B)Cr>0、R=exp(B)r/Δ，且整个|q|R管严格留在同一解析域。
R61 Y=x/4+U 与L为有限实Fourier×时间多项式，整个初值复strip直接覆盖，
不付采样节点半网格费；finite端点Eref保留−ω常数。
真实端点误差经4εθ coth((S−s)/2)进入Wiener，全部高模包含。
两腿换向及根运动必须同符号/链式口径，首尾τ用准确±π/2而非浮点近似。

δ₂ pilot：881段、Fourier129、degree7 Bernstein，共用准确端点使所有Y/L跳跃为0。
Sx=1/128给 |ImY|≤.008003221422，|q|∈[.02781265273,20.05986776]；
Sx=1/512初始||H−4Y||≤4.078145e−15，q0=1。真实e0/e1仍欠。
构造和有向验证源/完整hash/重放见 notes/2026-11-12-R61-continuous-Bernstein-reference-pilot.md。
25MB中间系数按根规矩只存manifest/源/报告，最终证书参考必要分片应保存。
普通probe显示同δ₃/同rtol按knots分步使∫|e0|/q从1.92374e−8降至4.67171e−11，
只是选数值方法的诊断。实际有向Taylor接口必须保时间相关再相减，并单付Cauchy尾。

## 保存/重启入口

- notes/2026-11-12-recovered-exact-affine-sources-frozen-manifest.json：准确evaluator源。
- notes/2026-11-12-exact-affine-258-and-step3-frozen-manifest.json：δ₂完整258、新δ₃/H。
- notes/2026-11-12-regular516-legacy129-and-knot-probe-frozen-manifest.json：仅archive_required
  19件应入库；66个large intermediates只保hash/生成入口，仍留本地。
- notes/2026-11-12-independent-beta-ready-manifest.json：15件冻结β/参数准备；列出live排除项。
- 新全批统一manifest在提交前生成。所有progress、工作中Taylor/参数源另等冻结。

环境再丢失时，先pull并按规则差异检查，读这份H与列出notes，从最后成功推送的
完整对象恢复；missing大型探索trace按冻结版本/命令重做，不能拿旧日志代替新验证。
