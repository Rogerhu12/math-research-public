# 交接：可见且有厚度的闭曲面等距弯曲

维护会话 **Astra-visible-flex-2ecfcd69-20261128**。**进行中，未达README完成标准；不能阶段收尾。**

## 目标、规则与认领

同一g上的连通闭C2嵌入连续族，点点固定有内H，按全闭面直径D：diamH/D≥.2、held/D≥.05、含反射δE>0、全时reach/D≥.03、全域全时metric≤1e−6，并在固定几何/g/相位范围上真正加密到原求解容差。基础完成后继续held/D≥.2、δE/D≥.05。原终值B=2e−9、旧实际L12>1.95883e−8沿[既有G5合成](notes/2026-11-10-78718-fixed-g-refinement-composition.md)，不另加stationarity或伪时间积分门。样本/normal/网格均不能替代完整终值。

本轮部分clone后真实pull，已完整读根/题README、旧H/open并依索引读log/相关notes/results。根/题完整读于公开`3138f2d6564d66a92968cb963a904fad0dab5bd4`；私根完整读于`db8c308d5df4b018c12e225e2267064403f20208`。私库QUEUE认领已推`2d9db302569bbd09e28a6fe55e0409c42b0c29f4`。私库最近真实pull 2026-11-28 09:18:06 UTC，已读`15fe66c4883af521488edf8ca0f9af680c9d6928`根差无变化、认领仍在。

每次literal pull立刻看根/题README差，至少每小时；只读差并即时遵守，记本H。拒推立刻pull--rebase再推循环，不能force/改已发表历史。每完整结论一推。root独占main，代理只写同级scratch；2026-11-28按用户指令全部子代理显式用gpt-6.2-astra接续。Git只收源码/参数/小结论/哈希；完整可重算数组/报告/STL不入Git或Release。不写根LOG。H<10KB、单MD<100KB、open保持短；results.md已接近上限，不再追加。

## 继承事实，不重做

旧CI均早已LSMR800/stop7自然结束；H1有限几何已过，两fullH旧界失守不证明曲面失败。原输入恢复不算优化。旧H/open及CI完整来源见 `notes/2026-11-28-2ecf-{handoff-inherited-20261126,open-inherited-history}.md`。[旧无缓存重演](notes/2026-11-28-2ecf-m12-obsolete-replay-cancelled.md)已取消130，六输入阶段保留；没有保存的旧field不重演。文献Hu2611.00534v1小幅周期未给本题比例；Ghomi2611.17269配对/不可数非刚性不自动给连续弯曲。

## M12原固定g：已保存实际场

原源X+C，中央/真cuff/有限尾/深collar/帽完整。H2只约束增量，不改原目标。[准确C2/Boehm](notes/2026-11-28-2ecf-m12-c2-h2-direct-consumer.md)及[准确缓存/真暖union](notes/2026-11-28-2ecf-m12-fixed-source-packet-cache-and-true-union.md)保源字节与两端两jet。

| 实际场 | 独立采样峰 | 自身全域metric | 自身全时reach/D |
|---|---:|---:|---:|
| M32首H2 | 8.26045815e−10 | 9.999199636e−7 | >.03114912 |
| C2第二场 | 8.05757388e−10 | 9.976475574e−7 | >.03114830 |
| M48/G6 | 6.07253082e−10 | 9.963039080e−7 | >.03116477 |
| M48/G12 04r1 | 5.438487573e−10 | 9.963221964e−7 | >.03109937 |

前三场完整SHA/原失守项见[首实场](notes/2026-11-28-2ecf-m12-h2-first-actual-field.md)、[C2实步](notes/2026-11-28-2ecf-m12-first-c2-actual-step-and-spectrum.md)、[M48全部7阶段](notes/2026-11-28-2ecf-m12-c2-m48-actual-angular-refinement.md)、[M48全几何/三STL](notes/2026-11-28-2ecf-m12-m48-full-geometry-and-closed-meshes.md)。各场证书不互借。

[G12/G14扩充](notes/2026-11-28-2ecf-m12-g12-g14-exact-query-extension.md)8554新准确查询保原g；旧[LM SIGKILL−9](notes/2026-11-28-2ecf-m12-g12-sigkill-and-preserved-input.md)无field，OOM无证。[单band核](notes/2026-11-28-2ecf-m12-one-band-complete-gram-fixture.md)通过后，[G12 04r1](notes/2026-11-28-2ecf-m12-g12-single-band-actual-field.md)6阶段全真0，field5778bee4…、独立/10730祖先union同峰，RSS1,563,640KiB。它仅积分加密。[G12自身全几何/三STL](notes/2026-11-28-2ecf-m12-g12-full-geometry-and-closed-meshes.md)亦真0，held/D>.052783098；原R249全局reach界未过而R253区域转移过，旧失守字段保留。

M64/G12从真实M48/G6父态独立准确转移，完整142784列；后继h503实际物理加密保原g、全源及祖先观察。当前B主证固定使用M48/G12场5778…，prefix/tail直接计算完整X+C+W相关Gram，不能靠固定d0三角界冒终值；全时间由原orbit解析覆盖。

<!-- 2ecf-m12-diagnostic --> [实际nonlinear梯度被动核](notes/2026-11-28-2ecf-m12-actual-nonlinear-gradient-probe.md)已0；[准确query父链核](notes/2026-11-28-2ecf-m12-exact-query-extension-parent-chain.md)已0，新h必须保完整实际祖先身份；原活动入口冻结。

[R249](results/R249-local-material-two-jet-continuous-budget.md)保材料二jet抵消；[R252](results/R252-full-source-cross-Gram-and-actual-H2-metric.md)保source cross；[R253](results/R253-regional-source-normal-transfer-and-actual-H2-reach.md)前缀/尾各自p×CX。所有完整网格每份44714顶点/89424面、Euler2、固定帽3458顶点逐字一致；不是PL自交/连续插值/G5证书。

[R250](results/R250-full-finite-tail-smooth-source-regularization.md)规整全部18551有限尾缝、原节点两jet零；[Q查询](notes/2026-11-28-2ecf-r250-certified-query-source-consumer.md)和G12查询均0。[M48+Q全域转移](notes/2026-11-28-2ecf-m12-actual-m48-plus-Q-full-geometry.md)是新物理图e81f3ecf…，同g/W，metric<9.963071e−7、reach>.0311647758。全部现行nonlinear场仍Q-free，无Q Newton/STL；不得静默换源。R235不排C2极限。

## 强幅度：完整密训练和独立观察

完整12789位置列=87×147；旧稀G2/G3结论已归档，[独立真观察](notes/2026-11-28-2ecf-polar-independent-third-observer-reveals-prefix-peaks.md)证实漏峰，旧排序不借新成本。

[G10源失败/恢复](notes/2026-11-28-2ecf-polar-G10-source-failure-and-primitive-audited-recovery.md)、[一致arc审计/分块恢复](notes/2026-11-28-2ecf-polar-consistent-arc-audit-and-split-source-recovery.md)均保真实失败和正式行。新[完整G10/四基线](notes/2026-11-28-2ecf-polar-G10-complete-source-four-baselines-and-parent-choice.md)958径点×(128+192)、4291840全行，prepared de75e963…，自身新R²选zero6=9.49114。[G11完整源/观察](notes/2026-11-28-2ecf-polar-G11-complete-source-and-six-actual-observations.md)668×256半格角，其中540径点不在G10；其[先前433行失败恢复](notes/2026-11-28-2ecf-polar-G11-source-failure-and-433-row-recovery.md)独立保留。G3进入训练后不再算径向独立。

<!-- 2ecf-live-g10 --> [原g own14/14，G11 metric .212742、κ47.028、held .723879；全部4291840行保留，未成连续解。](notes/2026-11-28-2ecf-polar-original-steps-07-14.md)

[完整log-radius算子](notes/2026-11-28-2ecf-polar-complete-log-radius-joint-operator-audit.md)12789XYZ+87alpha，alpha移动明确改变g；全normal跨块/metric/area导数保留。[全大场FD失败与尺度审计](notes/2026-11-28-2ecf-polar-full-design-derivative-failure-and-scale-audit.md)保exit1和全规模后继0，门未放宽。[分块源/算子身份](notes/2026-11-28-2ecf-polar-complete-streamed-memory-and-operator-identity.md)全物理行不删。

<!-- 2ecf-live-design --> [87α新g设计own17/17，G11 metric .149376、κ14.524、held .611961，尚未满足强目标；设计不算同g改善。](notes/2026-11-28-2ecf-polar-design-steps-09-17.md)
<!-- 2ecf-live-normal --> [完整稀疏jet正常矩阵](notes/2026-11-28-2ecf-polar-complete-sparse-jet-normal-actual-audit.md)全G10真核通过；显式迁移baseline逐值同，接受不重计。

强比例、连续几何/whole reach和真正同g收敛仍未完成。R233原背景界不借给变化后前缀。原fixed链/新g设计链各继续，不以一个子任务结束停工。

<!-- 2ecf-total-prefix --> [原前缀四区与共享余项](notes/2026-11-28-2ecf-m12-prefix-four-regions-and-shared-remainder.md)：151片≤1.235521e−9；全前缀在算。

<!-- 2ecf-total-tail --> [整个原内collar](notes/2026-11-28-2ecf-true-inner-collar-total-Gram.md)104片U<1.957403e−9<B；[原尾50单元](notes/2026-11-28-2ecf-tail-correlated-C4-adaptive-cover.md)已过，全部18552有限尾正三路继续。

<!-- 2ecf-background-depth --> [原背景depth8](notes/2026-11-28-2ecf-original-background-depth8-extension.md)已自然0，原36profile不变，仅补36个原剖面；完整72profile供全尾部使用。

<!-- 2ecf-target-curvature --> [新增保存α7的piecewise prefix目标K证界；仅该α与原显式scalar片，source rounding/base seams/connector-tail和位置reach均未付，不移借给后续α。](notes/2026-11-28-2ecf-polar-saved-design-prefix-target-curvature-bound.md)

<!-- 2ecf-live-m12-refinement --> [h503首次LM −9，原源/注入保留；单线程映射带重试。](notes/2026-11-28-2ecf-m12-h503-original-LM-sigkill.md)

## 工作位置

公开clone `/workspace/scratch/2ecfcd6930d6/math-research-public`；私clone同级 `math-research`。代理scratch为 `m12-work`、`exact-work`、`strong-work`；root临时完整输出在 `root-work`。公开note给重生命令/身份，临时盘丢失则按原配方重生、不算新结论。始终继续open下一项直到完成。

<!-- 2ecf-rules --> 最近真实 pull/rebase：2026-11-28 09:32:21 UTC；已读公开 main `8874f0c2fc047cddc2e5a0b67a7ab6f4b2b44f9d`，根/课题 README 逐差无变化。
