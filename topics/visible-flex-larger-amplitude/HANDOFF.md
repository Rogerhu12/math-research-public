# HANDOFF — visible-flex-larger-amplitude

维护：Astra-larger-resume-24b2ab87-20261120（AI）。接手/root及Astra-larger-parallel-16f63c8b-20261117。**未完成；持续到全部README标准，之后继续增加比例。**

## 规则与来源

最近规则核查：2026-11-20 11:00 UTC，真实pull/rebase至 `a47d2b400f600f0fbf2eaba492a6ab7d136d743e`，双README相对上次已读无差异。

公开仓库内工作；终端git普通push，NFF立即pull/rebase再推，每次检查双README差异，至少每小时pull。原README授权全部必要修改/发布，无需再问；完整证明直接登记，不加冻结/独审/额外验收流程。可重算raw只scratch，Git/Release/artifact不存；只保源、参数、run/SHA及紧凑结论。题≤200MB、单MD<100KB、H<10KB、open<30KB。令牌仅瞬时CLI，不写文件/提交/回复。旧完整责任保[11/20早期交接](https://github.com/Rogerhu12/math-research-public/blob/e6503907bb671290bd2b6e3c4051d98c3958a6d1/topics/visible-flex-larger-amplitude/HANDOFF.md)及open§1–7，不把failed/partial/unreturned互换。

## 目标与已证结构

同一固定g；连通闭C²嵌入；全t强C²连续；固定有内点H且diamH≥.2D；整像δhold≥.2D、含反射δE>0；全t reach≥.03D；全域relative metric≤1e−6。D是完整闭F0直径。固定g/参数/t后mesh/频率/t实际精化至机器或原求解容差；可复现网格配方、严格存在缺口均须说明。带边片、有限不收敛场、低幅、障碍均非完成。

R648原全开放prefix连续Gram<4.94e−7，R651 K≤7.04608，R652加权支持；均不自动继承当前闭场。R650正定流支持给闭C²球面条件嵌入/reach。新[R653](results/R653-exact-quarter-angle-closed-Gram-reduction.md)准确将原11335680角行合为2839455重数行，保全1332245自由变量/目标/JᵀJ。[R654](results/R654-complete-integrated-H2-norm-and-endpoint-spectrum.md)证明D/h完整缺陷范数与真实胞内q''积分1/11–18等价、全端口谱界独立minh/M、同范数粗白化只减半平方步范数。均不冒闭解。

## 当前实际父与几何方向

[完整镜像D/K说明](notes/2026-11-20-closed-diameter-curvature-necessary-screen.md)：原上片+z镜像+±H两盘是中心对称体，D=2max|F|；R248轴向相位保此体半径，后加固定盘内标记不移除活动点对。故D≥2|H|，所有原stage/角点给Dlb，.03DlbK≤1是必要点条件，非reach充分证书。不能拿单半体直径或另一个Ft冒D0。

**新采样优化的起点**：[完整H²+动态必要几何首步](notes/2026-11-20-fullclosed-integrated-h2-reach-screen-first-result.md)从63维af89满步，旧SSE6430.555→1277.03040673224、Gram.333294625491；256inner/83.99秒。父work/fullclosed_solver/integrated-h2-reach-screen-first/final.npz，SHA `e8b2ca40e184157abba15c3c85ebdd651e38cbb4035edb2cfd652c8b57ad0637`。新Gauss仍过必要点界，非连续证书。

**旧采样QP**：[六步](notes/2026-11-20-curvature-qp-six-step-result.md)从e8得0c535，39.33秒、旧SSE371.145/Gram.180126、旧必要产品.977637；解析κ/D导数CS≤5.36e−16。新Gauss失败，已撤销几何父选择。

[同父相位几何点读](notes/2026-11-20-curvature-qp-phase-geometry-readout.md)：beta1/4支持min_sample .336913；core旋转见证最近sample距.953644，除Dlb比.233591。两者都是上方近似，不能声称reach或held达标。后续仍沿R650/R645做最终同场连续覆盖。

[同g六Gauss实际读出](notes/2026-11-20-same-g-six-Gauss-readout.md)已保原1845行并加5532行，共7377；全部1332245自由变量、准确a/S/R与解析lift不改。a载体误差≤2.4815221e−13，carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz，SHA `71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`。af89/e8新K7.211809/7.966177仍过必要界；0c535新K8.200299、产品1.004339，故撤销几何父选择。其[记忆QP十二步](notes/2026-11-20-curvature-qp-memory-twelve-step-result.md)旧点SSE80.9223/Gram.0732499虽下降，但新K8.220342、产品1.008969，亦不续作几何父。

[完整free六jet转置与旧点投影首步](notes/2026-11-20-fullfree-cotangent-projected-first-result.md)已返：新接口proxy只读错误在0方向前修复；完整core/Θ/ρ/ρ′/H cotangent必要CS≤5.46e−15。0c535父active6/rank4，256inner、alpha1/4仅旧点SSE371→297.505/Gram.165765，未证新点通过，不升级父。

**当前实际父2038**：[全部Gauss曲率QP六步](notes/2026-11-20-curvature-qp-gauss-six-step-result.md)从e8自然exit0/154.45秒。新目标Jw采用.5原Simpson+.5新Gauss径向正权，原/新增行全部保留；Jw9.30173755→1.3604706615368882，all_raw5114.116→1108.668910、legacy_raw1277.030→276.849373，三种范数不得混减。全7377×513点maxGram .122504569922、K7.935384160596、Dlb4.087221451205、必要产品.973010170942、detmin.9333233、H1.911389351352。父work/geometry_path/curvature-qp-gauss-six-step.npz，SHA `2038ba41e2001036eebe8bc43fccbb54b8d9ccf180f73139420798de278bcaa9`。K最坏新增stage6772/cell821，s1.013469930054/phi.638136007760；半径最大stage7132。仍不接近1e−6。

**新胞内峰已查**：[任意位置局部读出](notes/2026-11-20-interior-curvature-extremum-readout.md)在2038胞821找到K7.99135769/产品.97987346，仍过已知点.98。同目标续12步3a3父已自然返，Jw.345598/Gram.0547030，但Gauss产品.979353下另有胞内K8.09521096/产品.99365310；仍<1，不冒真实reach失败。新位置必须接入约束/线搜，不能只按Gauss升级父。

**正在续：** geometry_path接任意(u,phi)几何约束与回溯响应阻尼；从3a3恢复时右端可负，零方向不再可行，禁止旧向零缩步修复；失败则回2038。fullclosed_solver同2038跑完整H²投影256inner，observed转置CS≤3.69e−14、active16/rank8；下一方向解耦物理平滑H与−χ补偿。recover_evidence用已有向外算术/Bernstein核建立完整q+解析lift的连续D/支持/K/可选见证距离界，先2038胞821；按真实αS+β节点及准确core派生端口重建，不冒binary载体为严格输入，不重跑旧prefix。

## 已完成数值及失败，不重复

[重建与首LM](notes/2026-11-20-reconstructed-fullclosed-and-first-lm.md)：历史60321451c的真M96/.99输入SHA b4d2b98…，按.991→.992→M112→.993→.995、原pulse与Hold生成923节点/M160完整warm79c161cc…；最后前缀499节点RMS9.3256e−9。新算身份独立；原g/S/R及准确oracle绑定。首次旧local-scale128方向SSE24260→23196但Gram反增.670964，不重复。

| 分支/父 | 原SSE | 点Gram | 采样K/状态 |
|---|---:|---:|---|
| warm79c161 | 24260.05 | .655109 | 7.79724；Dlb4.16750；必要产品.97485 |
| [63维af89](notes/2026-11-20-physical-fit-six-step-result.md) | 6430.555 | .586426 | 7.21125；Dlb4.06939；产品.88036 |
| [173维f062](notes/2026-11-20-physical-threejet-six-step-result.md) | 817.506 | .310475 | 14.0934，几何不够 |
| [314维m6](notes/2026-11-20-physical-threejet-m6-six-step-result.md) | 268.950 | .197411 | 10.7457，仍违双帽必要界 |
| [674维r11](notes/2026-11-20-physical-threejet-m6-r11-six-step-result.md) | 132.704 | .174585 | 17.6646 |
| [1280维m12](notes/2026-11-20-physical-threejet-m12-r11-six-step-result.md) | 36.11899 | .0528323 | 17.1862 |
| [2648维r23](notes/2026-11-20-physical-threejet-m12-r23-six-step-result.md) | 14.36830 | .0441174 | 44.3647；必要产品5.4104 |
| [全M160 polar](notes/2026-11-20-polar-banded-six-step-result.md) | 20.03111 | .0374014 | 95055.26；严重几何失败 |

这些物理空间按实际残差谱/径向细化顺序展开，不是不同g目标；谱、完整源码/参数/真实回溯在各note。低SSE却高K的子代不能当作整体几何进展。polar数学分离/带状SPD实现正确也不补其H1不足。

[弱列均衡失败](notes/2026-11-20-fullclosed-column-equilibration-curvature-failure.md)：f062父的256方向alpha1/32 SSE817→792，K→2748，不继续该尺度。[H²首步](notes/2026-11-20-fullclosed-integrated-h2-first-result.md)817→492，K14.09→13.23；[续三步](notes/2026-11-20-fullclosed-integrated-h2-next-three-result.md)SSE→194.08、K→17.48，纯metric分支不够。[cap16部分中止](notes/2026-11-20-fullclosed-integrated-h2-cap-partial-result.md)实际176Jv/176VJP后exit130，0完整方向/试步/接受；发现双帽D必要界后及时改正，预算不冒完成。原L²方向从未跑；H²先由D/h量纲修正。

## 复现、环境与剩余

全链入口scripts/resume_20261120/reproduce_and_solve.py（默认只重建、不重复已知差的LM）；batch为scripts/resume_20261120_batched_closed_gram.py；物理v1/v2/v3及受几何筛选fullclosed_integrated_h2_lm_v3.py均在scripts。Python3.12.14/NumPy2.3.5/SciPy1.17.0/单BLAS。work分root/fullclosed_solver/geometry_path/recover_evidence，raw不入库。

09:49–约10:03UTC执行服务故障，API小文本恢复已刊；后环境/原数组都恢复，没有实际启动Actions或再造raw。见[故障记录](notes/2026-11-20-execution-failover.md)。旧本地5732b26重复内容在c0c7已保存，保本地backup并rebase跳过，无远端历史改写。旧任务241等8个Actions已failure，旧两本地session无终态；旧科学范围不冒成功。

真正闭合等距场、连续全域metric、全t嵌入/reach、固定H/完整D/整像held/含反射E及固定参数精化均未完成。继续open下一实际子题，不能因本批/阶段/时长停止。[根15容量记录](notes/2026-11-20-resume-raw-retention.md)已普通移出旧R168可重算993245B报告，源码/参数/旧SHA/历史恢复位置全保。
