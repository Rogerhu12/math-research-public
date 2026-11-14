# 交接：可见振幅数值解附近的精确等距解

会话 visible-exact-astra-f6a2，2026-11-12；**进行中，主目标未完成**。

## 规矩与同步

连通闭 C² 精确同度量嵌入族；固定有内点 H、diam(H)≥.2D；held 位移≥.05D；
含反射 δ_E>0；全时 reach≥.03D。有限模、线性、条件式、数值或障碍均不算完成。
最近已读规矩提交：bcb6d5b933304aafdea4bda3fc1aff28bea06b0e（根README、本题README）。
每次pull检查两README差异，有变只读差异并立即执行，至少每小时pull。
根授权/全部规矩1–13、本题README、原HANDOFF/open/log/notes已完整读过。
用户明确授权读其它目录。只改本题和根LOG；提交前pull，不强推或覆盖并发成果。
根LOG每批一条≤200字，本题log≤5行；Markdown<100KB、H<10KB；>1MB数据gzip，
单文件≤5MB；大可再生中间量只存脚本/参数/hash。仅stage显式冻结清单，避开live。

最近已成功推送 main：0fb5722af1bcd1f73676b56426f4aa0996a4a71e（11:17UTC）。
本次23件恢复/真重算包已推，backup f=f59e22ff6；前数学包0162a1a1512cf235534c6dc251eb8e39d159164d。
前数学包100件/94个冻结成果4,212,382B；包括真实β′、独立覆盖、局部defect、完整δ₄/δ₅预测、
准确δ₅参考、R64实际正领口、参数参考公式和失败路线。统一manifest
true-beta-defect-step5-and-collar-frozen-manifest SHA
6a883c4eba31e6f8e9575a74ad1c7ed981555e477c2cf5cf9bc8f505f89b11e6。
恢复分支e=8b0191cf4ad5c057ff9a3826db09087f06a00501。此前0becd856亦已推。
10:59第二次环境丢失，11:04新空环境；重新部分fetch/checkout并实际pull，
两README相对38e35无差异；仅恢复源码，丢失报告必须真重算。此前07:46丢失包已重算并推。
本次状态登记 notes/2026-11-12-second-executor-recovery.md；此前H完整归档
notes/2026-11-12-handoff-before-second-executor-recovery.md。
全θ419域源码/证明、两grid已逐字恢复并真重跑3germ全过；新report e1a2c3f3...。
准确δ₄±5e−7的真根领口亦从零55/55通过；[1/4,3]两块从零继续。
未推actualfield尚未完成，更没有可复用P分片；noise/real/packet需明确新恢复版再跑。
大δ₄trace/参考分片再次丢失，完整源/参数/hash已推；按需重建，不得伪造丢失数值报告。

## 立即继续：三条同时推进的实际线

1. δ₅/H516已准确保存；完整δ₄1032两腿Emax=2.517276e−11，只是浮点，不能接受KAM。
   δ₅参考已从δ₄trace符号retarget，准确初H与全部接缝已付。下一步是真δ₅全圆/全时间
   e0/e1和参数费用，不能拿δ₄trace换名。不要再盲跑一小时同精度float来猜精度。
2. 单点和连续角弧defect已分别达e0<8.940703e−27和8.539827e−20；仅419局部窗。
   逐弧算法约75s/验证，不能盲扫全圆。numerical正在整物理θ FFT场＋scalar time-circle
   提速；constructive正在δ₅全θ×复时间D/M/W外域；root接完整误差与传播。
   f-only N1024/m33实测10.46s，Q1024/320bits抽查球半径1.59e−62，仍非完整覆盖。
3. R64已证δ₄真实[t,1/4]正环带source/DN，非闭帽。independent继续准确δ₄±5e−7盒
   的[1/4,3]与明确外延；当前对象只定义[-3,3]，旧R22/23的x20尾未与之接合。
   然后必须实际KAM、全传递强余项/有限低块/ordinary sources、相对Killing、
   残差因子Newton以及同一精确族的全部几何比例；完成前不收尾。

## 对象与参数（输入在data/phase_ring_continuation）

原sym输入bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532。
D5 origin type_fixed_step02_d5_jet_interval_inputs.npz：
0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b；direction
8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab。
准确实数c0+δv、alpha0+δw之后才径向偶奇平均；高度准确积分slope；真无限R33 primitive。
Q256/512/1024只作带误差表示，不重新定义曲面。
δ₃=−7832869216826619/4611686018427387904，object e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f，
H129=028a95679f5c6e6ff6438b539c9c427f745f976a4dbc70b46c0bb01dd0f4fb49。
δ₄=−7789866024620307/4611686018427387904，object87566dee6e119bb4127200c2dae38f9cdf692a18475c1cde23961a56605919b5，
H258=8bd6078f8c442b48bab2b15850b99e2455d616ab48e687abb22114a1f1bfe39b。
δ₅=−7789843107295549/4611686018427387904，object91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848，
H516=0439d88f10f46d367e44a984db661ac3806a7bd052f46eca14e71594fa8eb2c2，
tight根489268d254c2a9454ccbee32a4821d9bf577279490f76c9cc6f8d902a5e64e0b。
H准确用旧dyadic+binary64小校正Fraction和，2^-120量化，所保存C0/C1/C2舍入分子0。
δ₅ Δδ=4.9694026581e−9，H改变量max1.71034e−11；真实新返回仍未付。
δ₄原float t′=6.11079949816e−5不在严格[6.110799499427786,6.110799499501956]e−5；
差约1.27e−14如实保存。δ₄±binary(1e−6)真根一二阶jet已付，但β仅覆盖其更小交集。

## 完整β与独立审核

原sym β在36.79967508215..36.80349990665；只属于原对象。
δ₃点完整β在37.02315597217..37.02687658944，167spans/257叶；
δ₃±1e−8在37.01422398291..37.03580857868，167spans/249叶。
root用新flat源从准确knots独立重建覆盖，224bits分上下端点重加均通过。

新Δ₅=[δ₃−1/100000,δ₃+1/100000]全族真正β′已完成：167spans/265叶+waist+FP collar，
|β′|<1325.998893955<1326，β在37.00989598321..37.04013657839，危险格距>.19138138420。
root独立256bits得β′<1325.998893951070、β在37.00989598323246..37.04013657837160。
δ₄距Δ₅边界最小6.7516911722e−7；δ₅为6.701997145629275e−7，二者±5e−7均包含。
root全文审collar/finish/combine，constructive全文审bulk两个源；失败27叶未进入选择。
旧collar-p40只是有效系数checkpoint，domain500重新付完整外域后才完成。
完整13件manifest independent-true-beta-derivative-ready SHA
880691d30f4b533e9b36f2d3e41336a99e0b3ad626ee0c622864f27b3006dd4f。
独立复核见 beta-derivative-complete-independent-review.md 与两个cover-audit.json。

## 真实流参考与缺陷修正

R60/61：e0=Yτ−f,e1=Lτ−fθ,q=eL；A≥∫|e0/q|,B≥∫|e1|,C≥∫B2|q|/2。
r=r0+A，Δ=1−e^B Cr>0，R=e^B r/Δ；全管|q|R<d。跨段/两腿必须带真实前端误差。
δ₃共享参考550段/K258在Sx1/128有|ImY|<.008102177，.027134<|q|<20.550317；
其31MB分片是可重建中间量，manifest0b5c7b41...定义完整函数。
普通/跨knot/真实±π/2转向、native根都局部通过；不把binary±π/2当真端点。

δ₃419全时间τ[.4959063944238653,.5020636678136512]，三个common germs都已通过
相关外域门，Rt3/order40，hx1/256/Rx4时|D|>.7504；hx1/64因完整像过大失败。
精确cap[0,1/1024]含全部3germs，后段仅第三germ；同一修正限制不产生新跳跃。
全时间门仅是域/尾，不能当连续残差。full-time-outer-gate-frozen-manifest SHA
c9eb591648f72815d30f40959a6a21dbe944a11da702689358c9eabca89f8223。

局部defect：419归一窗[31/64,33/64]，x=.5+i/512（或±1/4096实角弧）。
Y=原完整Fourier/Bernstein+准确有限P(u,v)，每角行P(-1,v)=0由Fraction恒等式保证。
修正后重新证明真场/全外像/双Cauchy尾，不假设Newton收缩。最后e0单点8.940703e−27、
连续弧8.539827e−20；e1约1.622914e−7；匹配左值的局部物理误差1.644447e−23。
全文及端点独审通过。整腿必须把P_end传给下一P_start，逐段重置0会把误差作为跳跃带回。
普通multipoint/Horner已实测失败；centered Horner精度修好但没提速，失败源/报告保留。

δ₅符号参考：Y5f=Y4f+Qf*a，Y5b=Y4b+Qb*(Qf,end*a)，L=L4；
a=h5/4−U4f,start准确分母2^122，Q为明确degree7/K128有限dyadic函数，非已证Jacobian。
原trace身份仍δ₄、target明确δ₅；全部1100段接缝/初值准确，直接jets不截断符号产品。
manifest step5-reference-retarget SHA66d7cbbc3cbb6542e954712c652addee0ba220d8407ee828b71a2151466ab537；
13小件455KB可stage，70大shards141MB只存完整SHA/重放。真实δ₅e0/e1全部重付。

## 参数、KAM和实际正领口

R62真固定τ二参数源已证，8ray仍仅样本。参数参考zref=Z+t′sinτ v+q d满足
 ez=eZ+t′sinτ vθ e0+q d e1；两腿d带端点。新parameter-reference-flow-error.md证明
|yp−zref|/|q|≤e^(B+2CR)[rz0+Az+R(Jz+P12)]，二阶再用真实Bpp/B12；输入仍需计算。
R63固定H局部Wiener逆令R31初始id，δ₅s1/128,r.001的κ<.057574443、R<3.520010337。
Hardy端点因子sqrt(2coth(S−s)−1)，须完整边界。选s0=3/512,δ0=3/2560的费用
proxy比旧eps门宽23.04倍，但actual P/Q/T/σ/E仍未付，不能宣称KAM通过。

R64同一R37固定型别/ground-state算子，在δ₄[t,1/4]55准确闭cells/全角通过：
K/(r−t)>14.32125,m>.02475984,M<46.04708,g<40.389，完整source-contact<34550，
ordinary L2H^-2/3 contact<5955237，实际正角权2^-75，signed Robin逆≤2，mean/cross保留。
root全文审源/证明、独立Fraction覆盖和256bits常数重算均通过；没有外帽/H结论。
R64 manifest SHA d7f580f241cdcd2e6118a75c581efbf8c5f529b5b1e0b5d97cb8c9b598c59cc8。

## 重启与未推恢复

先pull并核README差异，记录新已读SHA，再读本H与本批统一冻结清单。
大中间trace/reference按各清单准确命令重做；不把旧摘要或浮点轨道当连续证书。
任何新源冻结后不再原地改动；保存新版本/新报告，避免已记录hash失效。
继续README主目标，完成前不得停在阶段报告。
