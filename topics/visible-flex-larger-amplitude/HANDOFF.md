# HANDOFF — visible-flex-larger-amplitude

/root，visible-larger-public-resume-20261114，GPT-6 Astra Pro（AI辅助）。**未完成，持续真实增幅/固定g精化/全闭检查。** 旧现场见notes/2026-11-14-handoff-public-migration-checkpoint.md及legacy-recovery-checkpoint；完成数据见同日notes。

## 目标与规则

完成条件按README：固定g与H的闭连通C²嵌入族，diamH/δhold≥.2D，δE>0（含反射），reach≥.03D，metric≤1e−6；同g/参数/t区间精化至机器/原tol。H可不连通、网格件<5MB；开放前缀/小幅/样点均未完成。
每push前真实pull --rebase，非快进重拉重推；至少每小时pull，双README仅读新差异，末行记已读SHA。PAT仅瞬时CLI，不入文件；不强推。root独占Git/H/log/open，子线交文件冻结，运行用独立scratch副本。Rule12完整证明直接results，不加独审/冻结门；H<10KB，md<100KB，数据>1MB gzip/件<5MB，大派生表只存源/argv/hash。
旧仓正式迁移d9b031786已读；新公开Rogerhu12/math-research-public根README授权/14规则已全读，题README仅迁移提示变。Rule13用本仓Actions，旧math-research-ci/五queue已停；Rule14禁明文凭证。旧仓不再写。

## 当前公开授权与实际恢复

用户本轮直接指定 Rogerhu12/math-research-public 并明确授权 CLI commit/push main 和本仓 Actions，旧轮因仅有私仓授权产生的公开发布阻塞已解除，不再等待确认。
本轮部分克隆至 /workspace/scratch/e959e57ee07f/math-research-public；只窄检出本题源码/必要笔记/结果，重计算只用本仓Actions。旧 B=/workspace/scratch/ffc1334c1988 仍可只读，未推结果不必一律重做。
已原样恢复旧公开clone 43 个本地提交，末端 e4e38a4fab4cadf9039640dc3495add7eb15eb36，合入最新公开main，不重写任何已推提交；仅本题323路径及一项本题workflow，R235–R237/原RK24、RK48完整solver已恢复。所有新增文件<5MB，未发现明文凭据。旧停止/排队描述是历史，不能当当前运行状态。
优先恢复新球核心M96从.984到.99：旧真实退出1为ENOSPC，423节点checkpoint仍在；前三Newton步接受，尚无完成解。新Actions入口已提交：visible-larger-public-resume.yml，两线M96/rk48；本次先只解.99，成功后从实际输出递进。原A RK48求解已成功，但16层源节点common-grid和闭组装未完成，接续原状态，不重复已成功求解。

## 环境与恢复

B=/workspace/scratch/ffc1334c1988；R=B/math-research-public；T=R/topics/visible-flex-larger-amplitude；B下root-work/strong-work/exact-work/geometry-work。旧B/math-research只读。9CPU/约9.7GiB无swap，共享tmpfs占用大；BLAS/OMP/MKL=1。exec各自PID命名空间，不能猜PID杀进程；只用原session或owned-child supervisor。
本轮clone禁自动repack，只保留窄检出。旧d1aa462cfc02已失，R179–R224多项仅落盘/入队未推，half-positive J/QR/iter2不能冒恢复。
91原源revision869436630c99aa5a68afb55bd8877c826034d117、7A raw已实恢复；其中12源属未迁移私题，Actions仅用MR_TOKEN secret瞬时读，不公开原源。新最终helper已再逐件核91及7raw，8.60s exit0；前次完整恢复494.92s。准备不是科学计算。
A主SHA917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf；fixed-view cd2392da6fdc8676a563ef6a18037fe43ea1519288ae39e811d6ac7a55bbcdfa。raw在B/strong-work/runtime/topics/visible-flex-larger-amplitude；原recipe可重生。

## 旧A增强线的最后真实状态

唯一完整接受强解仍A：M32/35参数/2590节点/1280角，RMS9.9224e−8、完整mean metric6.733e−8/κ8.34551434；G=.2506381129，prefix D≥3.9767551573，远低于完成幅度。13方向响应完整原门通过；margin325 full尾已解，但prefix未接受。半步r1/r2/r3均被−9，不能冒数学失败；r3完整J/QR已有线性残差7.06e−18，试点未返回。
r4原arena I/O修复后首inner步alpha=.125接受，merit .0137068→.0129303，col .0795727/BC5.56e−8；仍不是新接受曲面，其新H未完成重解审计。原小包及完整恢复身份已在notes/2026-11-14-strong-resume-r4-live-checkpoint.*和half-third-sigkill-and-page-IO-r1，旧scratch仅只读。后续优先新球大核心主线，不能用A的尾/校验移植给新核心。

## 原A固定g尾与整闭

原stored g保160head+原far，M32/512角/depth8/576stage/577nodes/RK12/tol2e−9。全H depth12真exit0，cut jet稳定，非∞存在证明。R234原finite collar Fraction/Bernstein/Fourier全域metric贡献≤1.0013852088e−18，原宽不变。
背景保留的真RK12径向1/2/4 metric1.2476e−6→3.5847e−7→7.2923e−8；固定.01 patch共享prefix六cut jets，未缩宽/换g。闭r2三mesh解压各3.746MB、Euler2/每边两面/零退化；Dmesh3.97745927、Hdiammesh3.96956338，九phase最大点云距离/Dmesh=.06301463。三类有限空间弦负例0，其中moving/fixed全实phase；连续空间reach未证。
RK24真Newton/J/audit已exit0/1575.81s，norm8.36178e−11、finite metric7.99436e−15。cut jet稳定，但slope/second J相对变6.10e−5/8.13e−5，非舍入稳定。新4609真节点回放1.13687e−13消除旧states套RK24的不一致。
RK24完整4→8/整闭exit0：global metric4.77033e−8是原prefix cut（tol1e−7）；未patch尾2.67290e−8。补source knot局部改善而邻域未全优，GW默认不换。不能把cut平台作为tail自身2e−9门。
**RK48 solver87946已真exit0/4114.75s**，完整J/audit、norm1.67235558e−10。24→48 cut slope/second差3.55e−13/8.29e−12，freq40 J仍差.0671/1.5655，未机器稳定。**v3 pipeline13425在08:37:18真exit1/ENOSPC**，真16读出仅约288/576段，不能记9217节点完成；完整RK48不受影响。exact正在清自有可再生副本后续，partial/terminal见exact-work/current-checkpoint.json。旧v1/v2历史源保history；prefix未新DN重解。

## 真正大核心与新主线

R225全32核G≈.8，R235真实Schur/barrier已证。84节点同g多频入口、延至.9875的新g多频结果均归档；旧急turn/双barrier高模增长非不存在证明。
旧M48 free-core原样源32b38b...及完整失败包保存；旧M128−9启动源没有逐字归档，明确不冒用现a1e5486源码。169节点/真实资源记录仍可靠。新M128短端.99475、base_step.005、264节点prepare真0，BC0/colmax5.88685e−9，待16GiB runner原tol1e−5 BVP；directCSC同值且释放旧LU/J。
R236：λ=6/5全32核准确G≈.96/rho_min>.1661，条件球外保持证明完成。照搬旧scalar会遮挡到.8691；**新从core球控制到.95真exit0/848.78s/102888KiB**，采样G≈.96保持，Dproxy3.45097493。冻结381节点/1140有理接缝，geometry SHA5b9a574cb3774e9765b6782819dda0332bdb24fc6961b8e6473d2b2f512196bc。冷M96/M192同粗时间metric1.917e−10/6.322e−8；保持M192、dt减半/rtol1e−12后降至2.1272e−13，真exit0/262.59s。未声称完整六jet或闭面收敛；见notes/2026-11-14-root-sphere-controlled-prefix-r1。
新球M128短turn到.984，点域/球保持，高模随后增长；冻结415节点/1242接缝新g，原生M96冷至.984 metric6.6398e−8、κ6.29532、Dproxy3.49295，非裁频初猜。7件完整包见geometry-work/scaled-sphere-turn-frozen-package.json。
**geometry全M96正Gauss两端BVP真exit0**，固定前32核/64高核未知，2轮/416节点/连续残差5.457066e−7/BC8.27e−23；峰296844KiB/820.49s，session1015已闭。节点metric6.65963e−8、κ6.295315、Dproxy3.492954605、球样本G≈.96；高核33..96新系数约1e−12，R237准确证全角rho>.16611593994/G≈.959999999997，材料角须重构。磁盘QR真实线性残差验证保留；实际末端设计算子非精确稳定流形，不冒全闭成功。输出B/geometry-work/scaled-sphere-M96-normal-BVP-r1.json.gz及log/resource，12件完整包已本地commit。新材料角物理C²quintic真exit0：831×1024/1661×2048 metric均6.65151e−8、κ6.30099→6.30153，球样本保持；四件包见material-quintic note，checkpoint在geometry-work/geometry-successor-checkpoint.json。新scalar可接原tail cut，.99续法未启动、完整DN未付。

## 接续

优先新球核心正Gauss匹配及完整闭合；同时消费同半步真实Newton和RK48/源分区精化。接受后立即原审计、锁g精化、全闭/全t几何，并继续增幅。完整证明直接results，数值/失败如实notes；本轮直接公开授权已生效，逐结论普通push并使用本公开仓库Actions。

规则同步记录：2026-11-14T17:14:55+08:00实际pull --rebase成功；双README自c2eafa9无变化，已读提交 05e0f9795f53c8ae415c30d44ce1dfbac16cf8ae。
