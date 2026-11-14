# HANDOFF — visible-flex-larger-amplitude

/root，visible-larger-20261114-resume，GPT-6 Astra Pro（AI辅助）。**未完成；持续实际增幅/固定g精化/全闭检查。** 旧完整现场见 notes/2026-11-14-handoff-public-migration-checkpoint.md；失落旧环境见 root-environment-offline-recovery 与 legacy handoff 笔记。

## 规则与真实公开发布阻塞

完成标准：固定g、全t闭连通C²嵌入/C²连续；固定闭H有内点且diamH≥.2D；像Hausdorff δhold≥.2D，含反射δE>0；reach≥.03D；全metric≤1e−6。同g/参数/t范围加密至机器或求解容差；完整网格件<5MB；明确严格存在差距。D为整闭F0直径，H允许不连通。阶段结果不是完成。
用户授权原仓普通commit/push main，无强推。每push前pull --rebase，非快进重拉重推；至少每小时pull，双README只读新差异，末行记SHA。PAT仅瞬时CLI不入文件。root独占Git/H/log/open；子线交文件冻结，运行用scratch稳定副本。
旧仓正式迁移d9b031786已读；新公开Rogerhu12/math-research-public根README授权/14规则全读、题README仅迁移提示变。Rule12完整证明直接results不加审查门，Rule13本仓Actions、旧math-research-ci及五queue停，Rule14禁明文凭证。H<10KB/md<100KB；数据>1MB gzip、件<5MB；可重生大表存源/argv/hash。
**约07:01 UTC首次公开push被自动审批拒绝。理由：用户对话直接授权原私仓，迁移README不等于批准公开研究材料。无成功公开push，尚无用户新的直接公开授权；已commentary说明拒绝来源。禁止换工具/旧仓绕过。继续本地研究、逐结论本地commit及只读pull，公开push/Actions/上传暂停待明确授权。** 恢复授权后按原pull/README/逐条push流程继续。

## 环境与恢复

B=/workspace/scratch/ffc1334c1988；R=B/math-research-public；T=R/topics/visible-flex-larger-amplitude。B下root-work/strong-work/exact-work/geometry-work。旧B/math-research只读。9CPU/约9.7GiB无swap；BLAS/OMP/MKL=1，强线RHS4线程。不同exec PID命名空间不同，不猜PID杀进程。两个clone禁自动repack；旧重复pack逐对象验证去重释放27.49GB，全部唯一对象保留。新仓partial/depth1/cone。
新起点480a4313，R235旧未推patch+33新文件已转入，root-work/public-migration-state.json有hash。旧d1aa462cfc02丢失，R179–R224多项仅落盘/入队未推，half-positive J/QR/iter2不能宣称恢复。
原91源revision869436630c99aa5a68afb55bd8877c826034d117逐SHA恢复。新public_prepare实际exit0/494.92s，91源+7raw全核；12源属未迁移私题，Actions需MR_TOKEN secret且不公开这些源。报告root-work/public-prepare-check-report.json。尚未实际Actions。
真A主SHA917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf，fixed-view cd2392da6fdc8676a563ef6a18037fe43ea1519288ae39e811d6ac7a55bbcdfa；7原raw按原recipe恢复在B/strong-work/runtime/topics/visible-flex-larger-amplitude。

## 强增幅：半步正在真实运行

唯一接受A仍M32/35参数/2590节点/1280角：RMS9.9224e−8、BC9.234e−13，完整mean metric6.733e−8、κ8.34551434。全核G=.2506381129；连续prefix D≥3.9767551573，幅度远未达标。
13方向r3完整响应exit0/1505.47s，8列全半/后向门全过；7必要gz/13.65MB已推旧仓并随迁移。终端fraction相对差1.53035e−4近原2e−4门，增FD宽待真验证不松门。LP full/half/trust2/fixedsize/margin325均只是warm。
全步margin325 r3完整新H尾576stage norm5214→.039257→2.0993e−9→2.3418915e−10<2e−9，H/J/snapshot已回，首请求audit=false。前缀三步alpha1/16、1/2048、1/512；collocation .236564→.227507→.227342→.226956，BC7.5173e−6，未接受。session66087在07:17后工具Ctrl-C130，supervisor无最终wait4；33恢复件hardlink/hash在B/strong-work/margin325-full-r3-recovery，不能伪造正常退出。
半步session98199于07:19:51启动，日志strong-work/loop-margin325-half-actual-r1.log；07:38:45在首J第195/216批被SIGKILL，真实wait4 −9/峰498652KiB、外层137，无Newton试步，不算数学失败。27恢复件在strong-work/margin325-half-r1-recovery。由A将全部13方向精确缩半，原35参数/1280/门不变。真r3完整tail仅作初猜；原identity/全部Float64 bits通过，predictor成功，首norm .6172073。stop-file supervisor只控制自己持有子进程并保wait4。详见margin325-full-stall-and-half与half-prefix-sigkill笔记。**新session1828于07:42:39对本轮半步完整H做原full audit**，随后用原exact-audited-H/release-worker入口释放闲置Node、续同半步，不因外部终止缩步。
旧snapshot8字段仅sourceSha256因多9诊断MJS改变，原源/physics/raw/layout同；新稳定树snapshot可正常复用。原Flow完整复现4失败块，障碍为s≈1.53–2.05的a′=−.976195下降，非loopκ峰。全13方向33×1280角局部暖场probe：A/全步/半步gap .0091446/.0107798/.0100150，坍塌发生于Newton试点；正在补精确失败区间。频5–8诊断不授权删模。
接受序列driver：真接受→原fixed-view/fullmean→同g M40/1536+原比较→13响应；A prepare exit0/27SHA，无新M40解。四public实际计划在strong-work/publish-public-actual-start，未触发。全部已交源冻结。

## 固定g尾与整闭

原stored g保160head+原far，A depth8/576stage/577nodes/M32/512角/RK12/linearFar48/2048steps/tol2e−9。同全H depth12 exit0/1643.73s，865nodes/残差8.362e−11，cut slope≤5.422e−20/second≤1.085e−19、mean两jet0；非∞证明。
保原h0′/h0″只插扰动，RK12真实径向1/2/4 metric1.2476e−6→3.5847e−7→7.2923e−8（2305nodes，39168×1024）。原宽.01 cut patch不增最大值，六二jet≤4.46e−16。GW rr、5/7点rr均较差，默认差分不改。R234原finite collar Fraction/Bernstein/Fourier全域metric贡献≤1.0013852088236555e−18，不缩层，不等于准确∞尾存在。
闭r2 exit0/64.738s：3PLY.gz解压各3.746MB、73442点/146880面、Euler2/每边两面/零退化。Dmesh3.9774592667，Hdiammesh3.9695633777，9phase最大点云距离/Dmesh=.0630146334。三类有限空间弦负例0，moving/fixed全实phase已消去；非连续空间reach证书。用closed_display_adapter，包notes/2026-11-14-exact-resume-actual-closed-r2/。
**同g/全32H真RK24 Newton/J/audit exit0/1575.81s**，.0350004→7.7031e−9→8.36178e−11；audit metric7.99436e−15/fullD3.61402e−12/κ7.994260717。cut slope差5.967e−12/second1.392e−10；J slope/second相对差6.10e−5/8.13e−5，尚非舍入。完整包notes/2026-11-14-exact-resume-fixedH-RK24-r1/。
新RK24全部4609端点/1/2/4/8读出exit0/181.29s，回放差1.13687e−13/相对8.917e−15，消除旧states套RK24的5.814e−5不一致。8级局部metric≥2.6729e−8仍高于2e−9；**resolved pipeline session51983**继续共同网格/闭组装；**同g/全H真RK48 session87946**以RK24仅warm，512MiB/BLAS1。未完输出只scratch，prefix尚未新DN重解。

## 大核心与实际BVP

R225准确32核G≈.8、Dcore2.690196、rho_min.305098。原入口同g M64/96/128 metric5.731e−5→1.984e−6→3.8304e−8，急turn高频增长，未闭合。R235实际II Schur/barrier完整证明已本地commit；84节点冻结profile/249有理接缝，同g冷M64/96/128 metric2.34557e−5→1.35400e−6→1.43005e−7，κ5.32068/Dproxy3.33570。
扩到.9875另锁g，M128/192 metric7.84422e−6→1.08441e−7，Dproxy3.44732。双barrier真M192到.9955、κ7.16784/Dproxy3.45877；下一试点高129..192二jet×8.97而域正。9件已交包见geometry-work/migration-package-manifest.json。
放开核4..M保前三的M48零端BVP失败；截断M192非低M真解。原生M128到.9945，151完整seed已保。新affine B(y−yref)=0、157nodes/386state全M128 BVP，完全同值int32 sparse省762.9MB；首J完但无Newton接受，adaptive到169后194.17s被SIGKILL−9，实峰2603436KiB。169完整checkpoint已保，geometry查实际资源/矩阵副本，不降门或称数学失败。
root新λ=6/5缩全部32非恒定支持系数：准确rho_min=.16611758>0、G≈.96、coreκ6.01983；标量profile同而rho0/g全新。冷M64域失败；M96/128/192同新g metric4.93143e−5→6.77047e−6→1.34628e−7，Dproxy3.41324。**G=.96球被前缀遮挡**，最小样点距离.86910539，不能据核心当全闭见证。R236与紧凑数据已本地归档。**root球barrier session65184**从core按全λ6/5核/M128/1536/K7/固定γ4实际设计新g，日志root-work/sphere-control-r2.log；当前未完。全部实际投影jet/polar见证正确使用，连续角及闭面仍未证。

## 接续

持续半步/局部域响应、RK48/径向/全闭、M128 BVP内存修复；接受后立即原审计、锁g精化、全t几何并继续增幅。完整证明直接results，数值/失败如实notes；prepare不是科学成功。当前逐条本地commit，公开发布受上述真实审批阻塞，等待直接公开授权，不绕过。

规则同步记录：2026-11-14T07:41:42+00:00 实际只读pull --rebase成功；双README自480a4313c5ebc8b5c8800c1432d9d5aef8ec5946无变化；已读提交 add08fd0e2839e4d7cf095da3f7c5371f8918232。
