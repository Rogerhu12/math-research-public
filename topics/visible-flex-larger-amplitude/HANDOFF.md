# HANDOFF — visible-flex-larger-amplitude

维护：Astra-larger-resume-24b2ab87-20261120（AI）。接手/root及Astra-larger-parallel-16f63c8b-20261117。**未完成；继续全部README标准，完成后再增加比例，不因阶段/时长停止。**

## 规则与目标

最近规则核查：2026-11-20 11:47 UTC，真实pull/rebase至 `04ae1ebc3c0e7bf3fa4439095e62d7486818b751`，双README相对上次已读无差异。

公开仓库内工作，终端git普通push；NFF立即pull/rebase再推，每次查双README差异，至少每小时pull。根README已授权全部必要修改/发布；完整证明直接登记，不加冻结/独审门。raw只scratch，Git/Release/artifact只保小源/参数/run/SHA/紧凑结论。题≤200MB、单MD<100KB、H<10KB、open<30KB。令牌只瞬时CLI，不写文件/提交/回复。根唯一git writer，代理写work及小blob。

必须同一固定g、闭连通C²嵌入、全t强C²连续；固定有内点H且diamH≥.2D、整像δhold≥.2D、含反射δE>0；全t reach≥.03D、全域relative metric≤1e−6；固定g/参数/t实际mesh/频率/t精化至机器或原求解容差。D是完整F0直径。还须网格配方和严格存在缺口。带边片、有限不收敛场、低幅/障碍均不完成。

## 同一场与已证接口

原923节点/M160/1332245自由量，共享quintic q加完整未截断χ[(R+S−s)er(Θ)+Hcap ez]；全部原端口保留，core前三系数固定、其余是未知量。标量/准确S/R来自原FullHold，真实节点αS+β；不以a采样插值换g。物理材料Θ角下g不随core坐标变换改变。上下镜像加±H两盘，R248相位公式消去活动时间；固定marker仍须同场付清。

[R653](results/R653-exact-quarter-angle-closed-Gram-reduction.md)保全方程的准确角轨道化；[R654](results/R654-complete-integrated-H2-norm-and-endpoint-spectrum.md)付D/h完整H²范数/端口谱；[R655](results/R655-node-midpoint-blind-space-and-Gauss-control.md)付原节点/中点920维非线性盲空间。R648/R651/R652仅原开放prefix，不能移用当前闭场。R650正定流支持给实际闭球面嵌入/reach，不能单靠K。

同g观察保原1845行、追加5532六Gauss行，共7377×513代表点；实际全角2048。carrier在work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz，SHA `71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`，a误差≤2.481523e−13。新Jw为.5旧Simpson+.5新Gauss正权，Σw=S；weighted/all_raw/legacy_raw三种值不得混减，最大Gram/K不加权。

镜像未标记体中心对称，D=2max|F|；全部实际点给Dlb，.03DlbK≤1只是必要条件。旧.98与现.992均为求解器余量，不是README新标准；只超它们不能称真reach失败。

## 当前实际候选与数值链

所有raw仅work，完整历史细节/未返责任保[c4c4600固定交接](https://github.com/Rogerhu12/math-research-public/blob/c4c4600b2ff1e1271dcc46be63277598b3368f72/topics/visible-flex-larger-amplitude/HANDOFF.md)及open，旧失败不重算。

| 同g候选 | Jw / 全Gauss Gram | 已知任意点情况 |
|---|---|---|
| [2038六步](notes/2026-11-20-curvature-qp-gauss-six-step-result.md) | 1.36047066 / .12250457 | 后补低phi峰产品.985812，不能再叫双峰.98可行 |
| [3a3续12步](notes/2026-11-20-curvature-qp-gauss-twelve-step-02-result.md) | .34559814 / .05470304 | 胞821产品.993655；v4a三次真实恢复全拒 |
| [def1完整256](notes/2026-11-20-gauss-fullspace-projected-first-result.md) | .98129554 / .10186568 | 原单峰过，新增低phi峰产品.983179 |
| [61a620物理H首步](notes/2026-11-20-physical-height-first-result.md) | .83836863 / .09341222 | 双峰/局部D复读产品.982831，未过旧.98 |
| [6077，v4b起点](notes/2026-11-20-curvature-qp-arbitrary-def1-result.md) | **.36916145 / .04536289** | **全已知点产品.989229，过新.992；仍非连续全域证书** |

6077实际父：work/geometry_path/curvature-qp-arbitrary-def1-six-step.npz，SHA `607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941`。它来自def1的v4a六步中4次接受；最终复搜低phi basin后未过旧.98，原结果如实保。def1在work/fullclosed_solver/gauss-h2-projected-first-fixed/final.npz，SHA `def1ccbded6c463a014a71a39f259c59501412d5c84afec07ce7253c9dc34f5d`；2038在work/geometry_path/curvature-qp-gauss-six-step.npz，SHA `2038ba41e2001036eebe8bc43fccbb54b8d9ccf180f73139420798de278bcaa9`。

[任意点算法/负界修复](notes/2026-11-20-curvature-qp-arbitrary-formulas.md)已刊；[3a3恢复](notes/2026-11-20-curvature-qp-arbitrary-restore-result.md)µ.001/.01/.1三方向36trial全拒，135.35s，终态同父，不冒完成。原v4边界round(phi)错误1次启动无接受终态，已另源v4a修。v4a又暴露拒绝trial LRU会逐出当前已知峰，故v4b永久保护双basin且整条线搜锁定当轮约束点，不能用旧单峰检查冒全部已知点。

[实际加权谱](notes/2026-11-20-gauss-weighted-residual-spectrum.md)：3a3的90%能量≤mode7，49.39%Jw在s1.1–1.6，最大是Fs²−1径向伸长；先物理H/径向及几何控制，不盲扩频。[完整H方向](notes/2026-11-20-physical-height-coordinate-preparation.md)已用可逆A=I+vq eHᵀ解耦−χ补偿；全部原变量/方程不变，尺度sH=sqrt(7S³/120)，不是旧q-H²同范数。

## 连续证据与正在执行

[R656](results/R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)准确q+解析lift的连续几何接口已证：真实αS+β、准确派生core、向外Bernstein/严格角余项。固定2038胞821/881/895给K≤8.077131/6.482645/6.591227，支持正，帽/半径/witness同付，其余919胞未覆盖。

[R658](results/R658-complete-body-diameter-and-fixed-grip.md)实际全922胞/全角/两帽/镜像位置覆盖自然返，6077的D≤4.106819。报告bcca1113、全源/参数刊。相同父胞821 Q16384/r32给K≤8.069613、support≥.4574082、0未付盒，.03DK≤.9942132；仅本胞，非全域reach。半径.45固定帽盘diam=.9；若接既有高≤.001固定标记，D≤4.108819且握持比例>.219，未冒标记族/held/非全等已完成。

- geometry_path：[v4b12步](notes/2026-11-20-curvature-qp-protected-992-twelve-step-result.md)已自然返2b143，Jw.28981378/Gram.04620002、known product.991814。按新尾部谱扩17径向中心，六步5接受/1拒得1240，Jw.28193249/Gram.03569674；新prefix227峰product.992944只超算法余量。N8192密角纯读完成、无更高新样本；保留新峰，接物理H²正则恢复/下降。
- fullclosed_solver：24de父完整256/64行已返13ce，Jw.29494283/Gram.03981718；新2b143及r17所有已知点重评后product.989822<.992。完整永久κ/半径记忆保留；准备分块更大行矩阵以同投影接下一完整方向，不移植其他父的曲率数值。
- recover_evidence：[R657](results/R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md)完整连续Gram接口已证，def1胞839严格上下界.10186124/.10187890，同a五次Taylor余项约1.08e−14，不能靠证明网格加密冒求解收敛。严格同像径向复合已实际返：Jw仅降.504%，Gram略升，不作主父；接正block-Lp/IRLS真实目标方向，不以冻结权重代价下降冒max下降。

## 复现与不重跑

全链入口scripts/resume_20261120/reproduce_and_solve.py默认只重建：历史60321451c输入b4d2b98经.991→.992→M112→.993→.995、原pulse/Hold得warm79c161；新对象身份独立，旧目标/源与参数保notes。Python3.12.14/NumPy2.3.5/SciPy1.17.0/单BLAS；work四代理目录隔离，原数组都仍在。

纯metric 173/314/674/1280/2648维旧子代K14至44；全M160 polar K95055、弱列尺度K2748，均不再当几何父。旧节点/中点QP 0c535/c71已由Gauss揭必要产品>1；不回用。旧cap16仅176Jv/176VJP、exit130、0完整方向/试步/接受；原L²未跑。09:49–约10:03UTC执行故障已恢复，未实际启动新Actions；重复5732本地保backup并rebase跳过，不改远端史。源/失败/原任务未返责任均见固定历史H及notes。

[容量记录](notes/2026-11-20-resume-raw-retention.md)保已移出旧R168及R33可重算报告的源/参数/hash/固定历史恢复，当前研究不使用它。真正闭等距、全域metric、全t嵌入/reach、最终同一候选的固定H/完整D/整像held/含反射E与固定参数精化仍未完成；继续实际求解与open下一子题。
