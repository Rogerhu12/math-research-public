# 第三次执行器中断与已发布检查点（2026-11-12）

状态：研究未完成，继续工作。本文件是恢复记录，不是新的数值证书。

## 已确证的主线发布

2026-11-12 20:09:06.891921 UTC 最后实际 pull 成功，main 为 `cb6b2058a1c288ee9d3b90a3033fdcd3050d4338`。两份 README 即时比较无变化。源提交 `22a28bbecd259cd3038853d689c6652330d92ceb`，父 `268c3bec2b0b270dcc9c24a7fa63234ad0839b4f`，topic 树 `70d2f9be1e1b85b7f791428a50c3814e2f13763f`。260 件变化共 46,328,659 字节；独立 source 76433、八批 cache 11707、普通 merge 11127 均正式退出 0。发布后同树/祖先以及自有 cache 精确删除均已核验。

初次 source 28152 退出 1，只因三篇尾部文档空行导致 git diff --check；无新 commit/ref。只修尾空行后重新选择、建立 v2 source 并发布，原失败记录仍保留。聚合 `2026-11-12-root-r84-r87-stable-batch-v2.json` 为 60017 字节，SHA256 `f9a98ff72dc810fd66d433e84cea200c6fc3c537b59845ee20aa8b01890f468d`。

已推 R84、R85、R86、R87 全文和其实际主数据；新 seg1 8 子段、1095 叶完整 J/mean/R77、8594 叶合成、seg0 原候选完整 J；strong r3/r4/r5 失败及缓存、r6 准备；pulse/cache 源准备。不能把主线 HANDOFF 中旧“待推”描述继续当现状。API 已重核这些提交文件存在，根和课题 README 与最后实际 pull 相同。

## 环境状态与终态限制

上述发布后执行器 transport 断开；后续 exec_command 返回恢复超时或 No usable execution environment is available，原会话无法继续 write_stdin。没有观察到合法可重启该执行器的工具。原文件可能仍在底层，也可能已丢失；当前不可访问不证明删除。不得根据跨 exec 的进程列表判断旧作业退出或原因。

没有发现新的强分支接受点、全46场数值或新线性中心数值。特别是 strong r7/80885 终态未知；exact 新全46场入口未启动；root 新线性中心入口及其最后 AST/plan 检查均未启动。不得把失联记作 OOM、数学失败、正常完成或运行超时。

GitHub 连接仍可读写。根 README 第8条明确允许仅此连接可用时提交文本和小于100KB文件；第2条授权必要 workflow。仅用小文本保全并准备本题 Actions 恢复，正常运行器内仍用 partial/sparse git、真实 pull/README 差异检查、普通 push。连接 GET 不记为 git pull。若新 README 差异出现，停止执行旧规则的后续计算并读差异立即适配。

## 未推的实际结果：必须恢复原文件或重新真实执行

### strong

r6/58524 正式退出 1，wait4 168.42秒、249864KiB；明确 OSError28 ENOSPC 在 disk_factor_begin。此前全部334 Jac回调、4173点和202367096B块装配完成，未完成 factor、无新接受。radial8/cache256MiB、同 frozen MJS，生产缓存身份5d412603…；新环境必须按实际版本和源码重新建立 key，不能冒用旧 key。

完整 cache 29519 逐项读取验证正式0，报告2493758B、SHA1591c847…；该报告/新cache未推，若丢失重做而非从本记录捏造。自有冗余释放2164件57343817B经先核归档后执行，保留334完整Jac和2全RHS；报告1075671B、SHA ccae30b8…未推。两报告超过1MB应gzip后再由终端git提交，连接不得编码搬运。

r7/80885 使用同r6数学/argv，fresh outstem `strong-actual-q096-combined-m24-tol7-prefixcache-radial8-workspace-heap96-r7`，仅 TMPDIR 改到旧root相邻 `strong-q096-workspace-arenas-r7`。实际普通 TemporaryFile/pwrite/pread核过，初始全RHS/J缓存命中，colloc约1.5616055e−4、BC约2.45819e−9；之后执行器失联，终态未知。恢复使用新运行名，不能覆盖 r7。

### tail

seg7 R77/27861 1740叶正式0，D≤.00669514854408，8594合成也正式0；未推原数据。实际四case probe正式0，最坏part0/bin0半叶界约.00318688/.00392974；完整中点上界.000711283，m2真点下界>.00029860117，仅点结论。真实矩/λ相对半宽已经极小，不把实际候选缺陷归为矩精度。

新的物理r first-part完整111叶（108 Taylor+3完整branch/sign union）64415正式0；fullmean/J/R77的12337正式0，D≤.0109493304903。它不优于旧候选，未选入现有8594叶、未展开其余7部分。后续 signed-J 诊断从未执行。两新入口旧本地SHA为 moments fff04ec7e4547fc23d00f25ac6794eb5e2429ef14bebbe29c8cd74731e90ff77、candidate 20d0ce487d61361501e9086d3f8126c7ae3eadf11590d16626915b0743416a13；重建若非逐字相同应登记新版本。

## root 未执行的真实线性中心入口

预备路径 `computations/root_outer_linear_centre_fields.py` 已在旧本地写过，未执行，最后 AST/plan 调用在进程创建前被拒，故不存在已观察的最终源SHA或通过QA结论。恢复时重建新版本并实际执行。

目的：在同 g、同 μ11、同 cut、同 R84 真φ/χ下，保持原18个非selected模候选，将m2/m4候选换成真实外端齐次场 L_R。所有非线性量必须在这个新物理场重算，不能借R79在旧 C* 的有符号源值。

输入主件：
- R84 `closure-outer-whole-field-m2m4-r1.json` 和 `closure-outer-whole-field-green-budget-r1.json`；
- `closure-outer-linear-cancellation-r1.json` 的实际外端Q/S0；
- 两cell真实五正矩材料、原完整源，cell10用已收紧的 `closure-cell10-true-moments-taylor-r1-summary.json`；
- 原强M20 ports、frozen depth12/f225 response及q003-m8-d12-f225 ready，身份由既有helper逐项核对。

准确算法：
1. 对18组的全部10793原叶，合并原10933子片的真实 `phi_physical_PK` 成每叶包含盒，精确有理检查完整无缝覆盖和同 V。
2. 原20模 H/K/Kx 由 R48 真实五矩 finite-Horner 重建；cell10正前后缀按实际细矩再求，不借旧有源结果。用已证每叶总场范数作合法分量相交。保存所有20模 Psin=−2m Re(H)/(r w)、Kcos=2Re(K)，及全区间每模每分量sup的强质量。
3. 仅m2/m4换成 `phi_physical_PK * (Qout/S0)`。其余18模仍原真实候选。选中场与原字段分别记录，不能跨新旧场取更小缺陷。
4. E=1+w²，Tcos=m Psin，Usin=−m Kcos−Psin；用完整复Fourier卷积计算
   Q=E s U²+ell[(K+T)²+w²(2KT+T²−P²)]，
   其中s=rx/r、ell=wx/w保真实符号。保存m2/m4的有符号余弦系数。
5. 强绝对范数 R=||P||+||K||、T/U等真实质量；c≤4R²、l≤c+||K+ET||<1。完整mean改动≤|ell|[2c(||K||+||T||)+c²+2w²c||T||]，保逆分母的余项 `(mean+l Qnorm)/(1-l)`，绝不只算有限二次。
6. 逐叶保存新有符号 N2/N4 及完整域门、原20模质量。18个gzip组+小summary，真实资源/failed片段也保存。

后续有序精确消费者：同原R84 kernel，将每原叶新N中心/半径乘 signed/absolute核；先求全积分，再有序前缀φ和后缀χ、同片绝对段。输出场按旧V和真实ω归一，另得切口∫χJN/W。不得与旧R79的源值相交，因为中心已变。

设Y0=L_R，Crest为原其余18模，rest参数变化δrest由真实每模强质量支付。R86给固定rho16域内Γ16=.14364150901468593，则
`||Y*−Y0|| ≤ (||G N(Y0+Crest)||+Γ16 δrest+head)/(1−Γ16)`。
再用准确 cut 源导数/实际参数轴闭合自映。旧m2/m4 cut导数/轴约.587887/2629，乘F16/Fold上界后很大，粗rho16三角球不能直接宣称通过。新中心值和偏差界都必须真实算出。

## 全频与新候选的纸面后续

弱源由强Wτ1到Wτ0可避免最大频率92放大，输出有限Green必须补1+m。uniform V0=2^-40需每叶真实证明Vold≤V0和完整权变换；未执行不能声明成立。高频条带消费还欠任意子区间R68 frame prefactor及更宽strip中心量。

tail新carrier：在真实r子段令a=m²HL/rL、b=wL(HrL−a)，fc=HL+a(r−rL)+b∫dt/w。则fc′=a+b/w、fc″=−b wr/w²，真实线性算子L_m fc=(wr/w)(a−m²fc/r)。残余以R48五正矩补两端二jet；额外支付正积分∫rx/w及前后缀。所有完整mean/J/R77仍需计算，不能用PDE二阶导数替换候选真实导数。完整mean高度只有一个共同常数，双端旧mean高度一般不能免费同时保住。

本题原完成门一项未降。继续恢复与计算，不把中断记录当收尾。
