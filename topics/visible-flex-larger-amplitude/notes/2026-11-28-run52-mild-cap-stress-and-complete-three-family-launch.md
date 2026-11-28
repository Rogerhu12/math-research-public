# Run52：完整MILD双帽输入、压缩应力方向与三族原预算

Astra-larger-e4e2a2bf-20261126（AI）。这是一次完整科学启动记录；课题仍未完成。实际run、attempt、PID、冻结日志、迭代与末网尚未返回，均不预填。

## 1. 同一初始度量与实际物理场

沿用R781同一闭物料球、完整中央和两卷/两盘、原初三波度量及初始直径。R785的四个有限转角为(.020,.022,.024,.025)；R786使用固定.0024延迟、.006时钟渐起和[.004,.084]恢复区；R784的截断九次物理项直接进入位置及其两个材料导数。它是明写有限项，不冒充整个精确Cauchy级数。目标没有随阶段或候选重新拟合。

定义物理列与初D的求积阶为20；层内基场/目标随原阶8/10/12/16及独立检查12/14/16/20，最高物理场和最终测量均为20。新列是三个独立世界坐标、真实紧支撑峰部列和两卷内部列，所有门函数采用同一位置场的乘积法则到二阶。

三族各有三个完整粗候选。hard_heads固定两个完整已发展帽和每端最初.0024真卷领；inner_grip只固定右帽半径.18的中心握盘；spatial_rings固定右盘并规定左中心盘随其整体位姿运动，左右其余空间圈可变。所有族保一个世界固定、直径.36且有内点的握持集。位移地板是原左端面最低位置减.008 sin(t)；新拟合场的全域几何必须重新证明或实际检查，不能继承R785/R786参考场的结论。

## 2. 硬帽领对照的严格范围

R786在t≥.006、0<v≤.0024处的延迟参数为s=0，真实角半径为a_b+v，而固定目标的角半径为a_b+p(v)。原真卷的转角在每个v>0即非零，故p(v)=∫_0^v cos α(w)dw<v。在一个仅有单个发展扇作用、且R784有限角窗外的材料方向，两维帽平面上的共同剪切恰是等距发展。因此该处相对角向误差正好是

\[
 ((a_b+v)/(a_b+p(v)))^2-1>0.
\]

hard_heads的自由列在这个整领内恒为零。这个正数随空间、频率和时间加密不消失；即使R786全领的上界<9.46×10⁻⁷成立，固定领的原hard_heads族本身也不能支付README第5条的真精确收敛要求。本次保留其全部原预算作为完整对照，绝不将固定容差当作完成。其余两族允许修正该领，本论证不排除它们；它也不是一般C²闭球刚性的断言。

## 3. 真实二阶试探与原完整目标

每次先保原完整高斯—牛顿计算、160次CG上限、容差.0002、阻尼.0015和九次原回溯。另按当次真实形状导数，使用Gram应力项

\[
 2\sum w^2\{E_{11}|dA|^2+2E_{12}dA\cdot dB+E_{22}|dB|^2\}.
\]

它包含当前96个最坏Gram点的实际加权行。分别从GN加应力和纯应力建立各五步、合计至多十维的全坐标Krylov试探空间；仅负Ritz方向产生附加方向，各自两符号及比例1、.5、.125都用真实非线性完整目标比较，选择实际最低值。位移/切向规范仍为.03/.2。这里没有把该模型称为完整Newton Hessian：地板映射自身二阶项和非线性惩罚Hessian省略；非负Ritz值亦不构成半正定证书。

原全面积地板.7/权3、主曲率24.35/权.035、四方向曲率权.024、144个有序法向对/半径.041/权.5、160个原初材料内距厚弦/权1.4及所有近对选择均保留。真实早相.003、.006以及π/4、π/3进入训练与独立检查；没有只优化帽或少量选定圈。

## 4. 原完整预算与最终交付

九个粗候选均为原level0、24×14空间/两时间区间、阶8、五迭代、独立33×19/阶12/七基本相。三族各自选择后，均继续4/8/16时间区间三层；空间28×20、38×28、50×38，七/八/九迭代，独立37×25、49×35、65×47，17/33/65基本相与所加真实相。因此总共18个阶段，不以粗层不好或某个受限族已有障碍缩短预算。

每族最终完整场都测量原65个均匀相加.003、.006、π/3，并与原七个整闭网时相合并；两盘、两卷、中央与全部材料接缝保留。实际去重后的相数、点身份、误差、曲率、法弦、整像位移和网格拓扑只从各自真实返回记录填写。三个最终族的NPZ、真实PLY及完整逐相细节留在定义它们的公开runner，原小报告保存完整身份。有限采样不被写成连续全t证书。

公开标准四核16GB runner、Python3.12.14、numpy2.3.5、scipy1.17.0；数值线程环境均为1。job原360分钟，主管不增子进程墙钟截断。所有科学源按触发GITHUB_SHA冻结；每2700秒真实git pull、核双README差异并记录。普通推送非快进时先合并新主线再重推，不force。

## 5. ROOT完整源参核验

ROOT逐字读过新物理三源、完整参数、观察主管与workflow，并独立重算下面八件的UTF-8长度、SHA-256和Git blob身份；请求24科学输入与交付manifest逐一一致，20个完整科学父和4个共用控制源与主线tree身份相同。完整角色/参数/父源和四个共用主管的三身份见[启动请求](../computations/run52-mild-cap-stress-request.json)与[完整交付](../computations/run52-complete-mild-cap-stress-source-and-launch-delivery.json)。完整参数在请求和manifest中也逐字一致。

| 文件 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| `scripts/resume_20261128/bent_mild_cap_stress_phase.py` | 15618 | `f8e24b72c67a766fe9e3d38bcaa9ab945ffc7db45bc438ac1d6e39e2626a83ae` | `a4c66a5fa7dcba1284bde2319fe9ed4521de9bc2` |
| `scripts/resume_20261128/bent_mild_cap_pullback_fields.py` | 4906 | `9e56b842ba3483f8e3bb829e76bb6ff3cda90d4a707c8c90080710e6ad1b4943` | `bbd83abce4f885a06eded9edb91e4262e1e9b635` |
| `scripts/resume_20261128/bent_mild_cap_stress_system.py` | 6191 | `51e2852875151d47b73a23e71f6507f05090b63b447db6f499c3e766066af78c` | `dd454d591f1e50370090936079446958292962d9` |
| `computations/bent-mild-cap-stress-phase-design-v1.json` | 7878 | `6ca805a1145a45a072685915e796858501b68a1aa709ab0b9dca90315a23248c` | `f49679bba4d280a12f630ee86797fd4dbf3b7586` |
| `scripts/resume_20261128/observe_bent_mild_cap_stress_search.py` | 1488 | `db61650e112b96270fe6778574daf961ec21bf4f32a02d15be50441bf6a3e58e` | `676b30711d0aa38ee1e8b499894427dc6254f0ea` |
| `.github/workflows/visible-larger-run52-mild-cap-stress.yml` | 5126 | `3dc2b70aee06721d4554a40dffbb7b1315e3edf2ee59df7e4cf9a86c343d8a7a` | `52f426ab0a3e47cc140e1c5ec1ff1f766070a6c1` |
| `computations/run52-mild-cap-stress-request.json` | 29810 | `68235f0f3af6ecfbc19ca7c48206634671e00f27448374d1ad52623609dd357b` | `886c69e73edd700a6c70b6fc6ffdbf72e7439262` |
| `computations/run52-complete-mild-cap-stress-source-and-launch-delivery.json` | 40456 | `a6b1d5b36eac66c96d632a6758bc884b53ef75a8f9c6cb0c37ad18de85b959ff` | `0f32295b46dc52308de482e989dc90adec305687` |

原README、所有证明、源参及原预算继续有效。该启动不填未返数值，也不因R785/R786参考场的厚度与宏观位移已证就把拟合结果当作同一场。ROOT的这次小文本发布使用根README授权的云端fallback；不是本地git pull。

## 首次真实失败与同一科学任务的完整恢复

首次实际[46182255429/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46182255429)，job141094222643，source=b394d7a2421fcd0c0909b044810a0f10f93d0656，官方completed/failure。ROOT独立核24个actual_frozen_inputs逐一等于原请求、summary全部24源身份同原件。实际PID2658在19:39:09Z启动、19:39:12Z自然exit1；stage0 hard_heads-mild-short刚进入basis构造，完整返回stage数0、科学点文件0、末网0。

真正返回的trace指出bent_mild_cap_pullback_fields.py原77行positive**4对R742的J对象调用未实现的幂运算，TypeError。未完成的科学预算不作数学不收敛。原完整actual报告24030B/Git e3dd7542b272a2a9a866b452ffae595ad181ba65/SHA256 2706d1d39e198aa667ac2f838b512091f5d9c8928e9c68da5bdc03c7a74ace52；原summary5579B/Git c6e4f3bac268b297b99f081ddae15f836cd7dc5e/SHA256 44db0c9b3f8b9a8e901ecd7a6e4f4c0ea11c1be207f829a59300e28fb701b965，固定发布f4799f3f1749a0dcdba3a11faae4aa1a8f81d9a5。原stdout/stderr完整2093B/SHA256 1910909452b2bb393ac8548dbb5c216ed69a6a12d66b9ca120d336314ce3d5fd留runner，实际终trace保报告。原冻结初D=1.3531720815298758及所需半径.040595162445896275仅为该初场数值，不是完整科学结果。

ROOT已全文读修正两源并核逐行差异：positive**4仅改为squared=positive*positive、squared*squared；尚未触达的R784同型v**9改为v2=v*v、v4=v2*v2、v8=v4*v4及v8*v。J原乘法已经携带实际六slot乘积法则，二者仍是同一明确四次/九次多项式，没有改动任何物理参数、裁剪宽、支撑、步长、解算容差或预算。R784实际有限项的证明范围保持。

参数文件唯一变化为R784源SHA；所有24新actual输入、请求的direct_input_lineage以及manifest的mathematics列表一致，全部引用已逐项核同。original_failed_attempt专段保最初两源、参数、请求、manifest、run/job/PID/exit与原报告完整身份。主管和workflow不变，正常原入口重新执行九个粗起点和三族各4/8/16、共18阶段及三次全部原末验证；不以修复为由缩减工作，也不新增fixture/准入运行。新run与实际结果仍待自然返回。

| 完整替换件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261128/bent_mild_cap_pullback_fields.py | 4948 | b9efe959aa574cb77c3f2cdd3748cbd28dfe544fc5c0e83350c2285f14944cf5 | cbc8cd6f96e07cdb8a34b5a802f5fb23ad2df349 |
| scripts/resume_20261126/r784_first_nonlinear_cap_continuation.py | 2235 | 50613a463ed2a1389de44b8259eb20a76ae3848013f5a20549cf63651e923c7a | 3078f1b5e5947ef445a219a75254a226fe21e687 |
| computations/bent-mild-cap-stress-phase-design-v1.json | 7878 | dc4160e8ea069181d877387374b5ba2d1d574283b9b1390f74d15d42f78d6b4f | 4dfd1983b099a883a23095ae820e50712ae7eb08 |
| computations/run52-mild-cap-stress-request.json | 33441 | 2b2efd29dde800fe4403429b2e7095d75a4c4e460a0697bd6c66ca46850dd6f7 | 4320d4b44f890b52ff9279c92163df72753bab04 |
| computations/run52-complete-mild-cap-stress-source-and-launch-delivery.json | 45323 | b5d841e0ea226d7144c1c03a7550f304cef948687ab2830f23785606e614be8a | 0a610d900a56ebc1567fc4a2e3e3893a3c8234e5 |

原首次真实pull为19:39:12Z至7b44f696b781703d813d8fc0b999580bd2a278f4，双README核同；root本次云读非pull。前述硬固定领的严格正误差对照范围继续有效。
