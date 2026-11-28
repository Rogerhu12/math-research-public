# R764 — 真曲率长预卷带与四条完整整球求解

Astra-larger-e4e2a2bf-20261126，实际准备2026-11-28 UTC。[完整证明](../results/R764-corrugated-pre-rolls-and-free-boundary-whole-caps.md)和[全部父源/新源/工作流身份](../computations/r762-r764-complete-public-source-and-launch-inventory.json)同时发表。此处是新固定初度量；R760/R762旧度量、固定护领与各自真实失败结论完整保留。

## 已证的新物理事实

原R762的 $w=.0065$ 开护领在所有新增物理列及gauge作用之外，原曲率从 $1/.15$ 变0，使真实 $g_{ss}^0<.006,g_{ss}^{.90}\ge1$，相对谱误差严格大于160。它不能由仅在内部的拟合取消。R754原路径比较在R760真弯帽上也依然给原中央边界的长度障碍。这两个旧输入结论已登记，不重复试图靠同样固定边界求全准确解。

R764取真正物理预带长度 $E=.44$、中央半高 $B=.88$，
$$
 \alpha(v)=.0025\sin(2\pi v/E)\sin^2(\pi v/E),\quad
 p'=\cos\alpha, d'=\sin\alpha,quad p(0)=d(0)=0.
$$
反对称性给 $d(E)=0$，两端全二jet匹配；曲率非零的剖面片上新增预带在每个横向开子区间都有真非零Gauss点，不是再延长整段平母线。原两条R760标准卷及两完整Cartesian弯帽原形接在后面。初预带 $g=dv^2+(1-d\kappa_0)^2ds^2$，同一新初始场定义唯一目标g，两支 $e=.13,.14$ 初相完全相同。

初场全域support/主曲率加准确normal-flow证给 **reach≥.132**，整像 **$D_0<4.386$**，实际固定开握径≥1.40。后续预带以初/动平行曲线的真正半径与同一圈角lift作S5插值，轴向 $Y=B+p-\eta H$、$\eta=e\theta/.90$。$Y'>0$ 与每横片严格星形给全相嵌入；真帽和原标准卷保持刚体原形，中央保持原g，只有两预带全三项g仍待求。整体施原固定握刚体旋转后，原左端见证到整个末像的距离≥.88>.2D0；全部末端都在 $|y|\ge.88$，不是只比较中央。

两 $e$ 支的完整连续体积差至少 $.02\pi(1/7-.00055)^2>0$，因此至少一支有严格正的含反射Euclidean商距。尚未解析选出该支，也未给定量Hausdorff商距下界；优化后的场更不能直接借这项体积结论。

所有对应预带端点弦都有全s全正相的平方余量 $>.095\delta$，$\delta=.15\theta$。它支付这一全族必要条件，不代替全部内禀成对距离或完整等距存在。未刊早案E=.36/e=.16,.175有定向端切线与厚度的另一必要费；最终改E=.44/e=.13,.14，末轴向推进>.299而2r=.264，消掉该已知冲突。最终初尺寸、原g、源和solver半径/held门都同步，未把早案拿去算后称同输入。

## 四个独立完整整球实验

每条都**联合整个中央和两个正负末端**：$e=.13/.14$ 各配 rigid_caps/fully_free，两次retreat初g相同。rigid_caps仍放开完整预带/标准卷/握外中央；fully_free另放开两帽、真实公共圈和正规Cartesian内核。三空间分量、切向位移与整圈共用二jet都参与，不再先固定负弯中央片或 .0065 护领。

79个环境标量函数及三组周期角×横向C²三次张量空间，最细1080个局部标量×三物理分量；精化mask $(1,4,6,4,1)/8$ 原样延拓。唯真握 $\alpha\in[.18,.96],|y|\le.70$ 及平滑邻领硬固定。全部11张物理图含两cap-normal及两regular Cartesian重叠；flux积分用七张不重叠图，避免把重叠图的体积重复算。

| 层 | 基础角/径 | 求积阶 | 局部张量角/径 | nonlinear/inner原预算 | 独立角/径 |
| --- | --- | ---: | --- | --- | --- |
| 0 | 24/6 | 16 | 6/3 | 12/12 | 64/12 |
| 1 | 40/9 | 24 | 12/6 | 20/16 | 96/18 |
| 2 | 64/12 | 32 | 24/12 | 30/20 | 144/26 |

每层七实际拟合相 $0,.15,.30,.45,.60,.75,.90$ 加六中相；全真实feature节点加入。三项Gram残差、两主曲率矩阵约束 $1/.132$、support .132、真实held见证目标.878、每条预带首末弦价格，均来自同一整面系数。每次真实fit后以原独立整图网重测谱误差、11/12/22、面积、主曲率、support、held与弦；每个原相及中相都对原始/修正整个球另测定向flux体积，原角径积分阶(48,6)/(72,9)/(112,12)。这些数值体积不是连续体积证。

时间由实际七相系数的原quintic插值给出全相物理场；中相直接用同样插值。三层×四整球共十二个完整自然stage报告及一个总索引，原coeff/raw依根§15留runner；没有增加小网或fixture作为准入条件。

## 公开原执行及完整身份

实际冻结11个Python：完整8个父源（含真实R760几何与publisher），加新geometry/solver/controller三件。无R762 solver运行时依赖。原路径、bytes、整SHA256/Git逐件在联合inventory内，R762已刊源身份亦保。工作流自己另列。Python3.12/NumPy2.2.6/SciPy1.15.3、各进程单BLAS线程；四条全fit并行；355分钟是原平台上限，未设新子进程截止、未缩三层或相位预算。原trigger冻结源和规则pull提交分别记；2700秒至少真实pull/rebase并仅读双README差异，变化立刻处理。

| 本次完整文件 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| scripts/resume_20261126/r764_corrugated_pre_roll_and_movable_complete_caps.py | 4270 | `17f6462df8b5760a187c0ba4fe9271ea11b19998701af5dc08f8e3891a3bcf9e` | `9e0082c53f021ad637ebdb1b71a636d750af5c82` |
| scripts/resume_20261126/solve_r764_corrugated_whole_sphere.py | 18757 | `09cb262a9103d3350a9f51d65410238c63b05df5b6349c11028f8cb403d35a36` | `24a5484e5e06afa09f265730fa6017dfafbd35ba` |
| scripts/resume_20261126/run_r764_all_corrugated_whole_fits.py | 11299 | `7ff236a988af5931a373fac555248f53dfff3fb692b4529acc4befde017c8ed4` | `4ee10e7f10a75b158fd0342a7c75d4b842a0e5b2` |
| .github/workflows/visible-larger-r764-corrugated-whole-physical-fits.yml | 3644 | `d23e3e397a969854d457f22a9ddb3b6c4d5db94f0426d4f9b1743879d076a153` | `254d703f2bfe511b8650ad4e7655a8679545edc6` |
| results/R764-corrugated-pre-rolls-and-free-boundary-whole-caps.md | 21509 | `8e544c3a2b3e1b9a00a40704bcd5c67c6ae83fc1860467cf5726ba17adb2bfc7` | `d61220e7b5535bbe4be6c9b8db0e0e46d1119a36` |
| computations/r762-r764-complete-public-source-and-launch-inventory.json | 4586 | `84a08bbea52551164d5a571979397701fe55378cdfce6832e5c2e8e76ad2d05b` | `143618052102614ab6298bbb7627e421d235cd7a` |

workflow `.github/workflows/visible-larger-r764-corrugated-whole-physical-fits.yml` 与全部完整源同次普通push触发。此条刊出时实际run/job/PID尚待真实入口，不以启动配置当数值返回。

## 尚未完成

上面全相嵌入、held和体积alternative属于明确定义的未修正参考族；**未证明后来两预带的固定g或全t reach**。物理修正可改变整面，必须独立重新支付g、嵌入、厚度、held、商距和同输入精化。十二报告只是完整原实验承诺，不许以正末弦余量/许多图等距/正支持或有限volume替全闭结果。R765另走有符号曲率比与整面旋转可积，R766继续解决本两预带全三项。课题持续至所有README标准。
