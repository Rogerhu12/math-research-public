# 交接：同一个可见振幅的精确闭等距族

visible-exact-astra-ac0d，2026-11-14 08:01 UTC。主目标未完成；持续执行，不因时长、阶段或等待收尾。

## 正式迁移、规则与同步

唯一工作仓库现在是 Rogerhu12/math-research-public，路径 topics/visible-flex-exact-nearby。新根与题README均全文已读；根blob 1d05db9ebc859a5fd9a8ef773ab05ef1e9de0598，题blob 7e2b93d66ee7dc61b0962cd6f2545dceb01daf12。
最后真实pull --rebase：2026-11-14 08:02 UTC，SHA 8a0b15fbbeb349c98aee05ff81267ba9ad75e3c2；根/题README blobs未变，差异检查完成。
每次push前真pull；至少每小时pull；每次检查两README，只读变更并立即执行。每结论独立commit/push；非FF立刻pull --rebase再推成功，不force。自身公开repo Actions已允许；旧math-research-ci/ci-queue停用，不再派发。PAT只瞬时CLI/env，不入文件/提交；公开输出无秘密。
自动审批曾拒公开目标；已重新核原repo6caee8bb根§14及题README首段明确授权转同owner公开repo并pull/commit/push，按用户要求立即执行新规。本条无私密数据或凭据。
root独占Git/H/open/results/log；代理只写自有新文件。H<10KB、md<100KB、open约30KB、单件≤5MB/>1MB压缩；大可重建数组留scratch；不freeze、独审、冗余核验；不动根LOG。只提交明确路径。
工作路径 /workspace/scratch/ac0d699811ad/math-research-public。旧math-research只供仍运行的径向进程读原源/依赖，不再编辑/提交/pop。迁移已逐blob核并恢复全部未推结果，详notes/2026-11-14-handoff-before-public-migration.md；κ=M²/B旧stash修订已随69推。
发布助手仅git_checked_publish_public.py/publish_conclusions_public.py；旧助手禁止用。每push前pull/check README/记SHA自动执行，有变即读差异。

## 对象、完成标准与重建

同一固定精确度量的连通闭C²嵌入族，C²连续。D=diamF0；闭H有内点、diamF0H≥.2D且逐点固定；未对齐held≥.05D；含反射E(3)非全等δE>0；每时reach≥.03D。phase单独是刚体旋转，须同族四个不同非共面静态曲率marker。
Eν=Eexp(νw)，w支(.05,.18)，a不变；ν/腰/deep/profile/marker变更均付同对象全费，不搬旧g0/R131。最终可选ν，但整个flex族固定同一ν。
最终candidate SHA ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413；6145nodes/M32/N512/[0,25/8]，α=6890507429876859/9007199254740992，ν=−2572625729470897/72057594037927936，η0=−7789843107295549/4611686018427387904。六stage全部原字段/位模式忠实复原已旧54f293b迁入，完整身份/路径见open与之前H归档。candidate在scratch replay-final-20261114/stage06。连续修复旧9239cfc：6143×65精确接口，腰不变，offset A0<3.861e−18/A3<5.635e−16/mean<5.842e−21；定义SHA440866a3…，原/修复中心不混。
Python3.12.14/np2.3.5/scipy1.17；PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps含flint.9/SymPy1.14，BLAS/OMP1。

## 当前完成范围与继续点

完整历史身份、失败与旧数值见[本次归档](notes/2026-11-14-handoff-before-complete-cap128-boundaries.md)、open §§1–8及每项native。以下不替代原证明范围。

1. root径向directed session19425仍读旧目录不可变源；输出 /workspace/scratch/ac0d699811ad/geometry-verified-20261114/attempt04.json.gz。08:00已98/141blocks、6271/8966格，原源3347e061…/jets b93fa88a…；四阶余项、operator norm、全η、准确φk与原uint64回接。前三实际失败完整保留。只将新的不可变快照交tensor --resume；61块/3903格快照36f3185d…与tensor706750a8…已推a9c3a233。完整mesh 8966×512×8正常0/198.985s已推d4af39c6，native5ed344a8…；Rmesh1.275559740657、support>.901284727159、全凸包距>.129668021172。角7722盒/6143跳全部完成，Fφφ<5.970523/Nφφ<4.646383；模型锚点与真GC几何仍分开。
2. 完整C0状态/δν几何预算已推1352e025，native00efc032…，7722盒正常0/25.05s：frame15.736315/.304809，原外锚点position30.196406/.105999，曲率141.332651/3.988052，ε≤1e−3、τ≤1e−5，锚点另付。root新腰C0/正向积分已实际0/6.779s/9门：sec(π/8)位置核，witness2(sec(π/8)−1)<.164785，正向总位置7.578231ε+.612629τ。源fourfold_codazzi_C0_waist_and_forward_geometry.py、scratch geometry-verified-20261114/C0-waist-forward-response.json.gz；完整证明已写并本条单推，native86a3e4c7…；原外锚模型→canonical腰对齐费还须真实支付。
3. newton全部regular q/ψ均6144块193态完整，FFT2.590797e−11/3.166507e−11已迁入。body v2实际exit1但7721系数/双mean全前缀已完成；v3复用后523行过粗主动止，原异常/前缀保，改联合Taylor残差及单独mean误差方程。完整独立boundary-v5已actual0/12.0068s、256物理矩+两组6143跳，native2d64468b…，Robin L2<1.454039e−17，S_end∈[8.167929616818,8.194927720677]仍减完整body积分，17件包已推38ad751e；旧mean失败容器三binary片仅保存一次。signedν session53534继续。不得把端式当真Schur或宽上界当不可行。
4. cap物理128完整257态/128输入/1296块normal0/764.783s、FFT6.475151e−15；完整moving97预合成normal0/28.518s。H128×97已推ab795771，paired B128×193/C128×97已推3078fefc；误差<1.496913e−11，物理C>128尾<1.757236e−14。完整19文件包已推1a1ac02e，含所有真实端行/mean匹配、首2/1977连续片及全部源/重建SHA，重建manifest c0e7c80f…；eL<6.518184e−12，独立C mean匹配行HS<.097206789641，不能删该行。首2 ordinary weighted B/C<6.482306e−7/5.103790e−7。全1977片正在4个互斥范围实际消费，512单cell已actual0并复用；v3/v4同row公式，版本只修boundary均值标量及汇总。大state/单侧derivative数组在physical-cap-DN-padded128-refined16-20261114与physical-cap-precompose-20261114，绝不重求finite提案或重复相同cell。
5. phase全两ray复域已推2147abff，distributed adjoint已推9d78f797；3071strict+root+mean+repair给σ1/4、输入ρ>.1639445393、P′−1<.334292688，P″3.257207/P‴57.403329。全Arb7阶scalar首germ已推f39e9da1；其余168germ四range由公开Actions真实执行。首run43572460867入口错未起math，真实失败已保；修复6b2a926d，新run43573003976四job已进入math，前三range[1,127)原生已实际推回，末[127,169)继续，聚合须核complete/process与准确germ覆盖。52input manifest eb25464d…不可变，worker602e696d…；不得修改active科学源。root-sliver10门3件已推f06e3f25：1910bdc2…、末端两ray <4.968975e−14。此前cap6截断q6/7无效输出永久invalid。agent继续真实flow/PDE residual、conjugacy、β/j与ν Schur。

## 已证模块与未完成的同对象接线

完整mean7721/6143 Γ<1.013237；strict3071/2549正向10.124885/10.240174、reverse404.222565/408.729241；root15/fold27，positive4650/N97 feedback .303291679/.788277736；negative-height .711062297；ν5M1156/864 signed625.523019均非全逆。
physical帽全模/全η/两mean已证χ<.820523、inverse5.571744，完整moving-cap桥1341盒追加χ<.003840162。全7296残差native6f52030b…，RU/RV A0<2.267544e−7/4.159086e−7，A1<8.646130e−5/1.529992e−4，L2<4.201205e−8/8.194504e−8；vgap>.0901531879/mean>1.0687328018；原右零η域拒与25盒成功独立保存，交集仅η0。不得重标整个邻域。
phase响应误差L2(E0)→C0≤1.273240无q^-1；浮点qν Ω′≈.0202241584=direct .0393631446−state .0005213003−mean .0186176859，尚未认证。目标ρ*=(612575−√5)/2228182、CF max7给principal gap1/(36|j|)，不能替代真conjugacy和β/j/strong正规型。最后ν须全族固定。

## 深尾与真正终局

旧53–68完整普通/weak源、两physical图、Γ*两列、phase补偿和实际band继续。原Nm<Cζe^-τ∞M M^-30960；68五函数generator>2^-175000 M^-1891。已证公共径向network inverse<2^175007 M^1894、好集>1−147/16384、余29066幂；非径向全簇与完整源到同原端口尚待。
69全J0型49门a25cbbb3，70全negative pocket50门519d4ea2，71实际Γ*59门41dd5ae2，72同当前Γ全盒53门08601008；真实非零径向补偿保留。tail正在全t∈[0,1/80]、e>0、κ≥16e的共同低κ PSD方向；主项精确因子已成但余项/全簇尚未获证，不能用逐模方向替混合簇。新P1024 profile未采用。
全补逆、真ν Schur、非线性F=0、精确闭族及真实帽全部未完成。最终同精确闭G须R≤511/400、support>4/49、|κ|≤12、κ+≤196/27，平帽a≤7e−6、z±∈[.9,1]、四独特非共面marker145..148，再付真实腰误差。几何预算尚是条件结论，不授最终reach/held。子问题完成接open下一项，只有README全部标准真正满足才收尾。




最新已单推实际结论：results/R133-supplement-complete-C0-waist-and-canonical-forward-geometry.md。
