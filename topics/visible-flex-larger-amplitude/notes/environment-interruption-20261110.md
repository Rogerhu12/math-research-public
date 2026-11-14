# 执行环境中断后的恢复交接

2026-11-10 16:19 UTC，visible-larger-astra-20261110。

**状态：课题仍未完成。此文件保存中断后的文字记录，不代表尚未提交的数值包已经进入仓库。**

## 1. 已确认保存的位置

最后一次终端正常推送为 [122c66aaacc427040a020bf17976325032b9ab09](https://github.com/Rogerhu12/math-research/commit/122c66aaacc427040a020bf17976325032b9ab09)。它包含120个本轮文件、约36.6MB，新增R12/R13、q040真实固定g的M14/M20链及完整Cartesian接缝、q003三个有限闭网格、新轮廓至q0775、旧尾方向同H对比、低H4方向原H的真尾包与外倍数计划。最大单文件4,262,482B。提交未强推，未上传PDF或逐页图片。

随后执行环境报告unavailable；终端返回exec-server transport disconnected / No usable execution environment。最后两份配置复现检查未执行成功。使用现有GitHub连接仅提交小文本恢复记录；未通过API发送数值大包，未把终端凭据交给连接工具。

工作区若恢复，先保全其中未提交文件，再正常同步main。不能把下面的“已算出”改写成“已经推送”。

## 2. 新轮廓的实际结果：完成计算，数值包尚未推送

保持vd=.98、loop K7.5、sync K2，第一下降段K由7降到6.75；每一步都重新解实际非线性prefix BVP，设计控制delta/boost_length改变，属于新g设计。仍只使用有限linear-DN边界，不是实际非线性尾耦合或闭图。

| 新first K6.75分支 | q=.0775/M20 | q=.085/M20 |
|---|---:|---:|
| 节点数 | 988 | 995 |
| metric L1样本 | 8.27935e−8 | 6.187368335e−8 |
| 完整平均高度后的height | 1.9333603615 | 1.9425154038 |
| 双镜像prefix直径样本 | 3.9228522806 | 3.9407757327 |
| 局部精化κ峰 | 8.2224302406 | 8.3779379024 |
| κ乘D样本 | 32.2553792213 | 33.0155743755 |
| 1/(κD样本) | .0310025808 | .0302887355 |
| 尾口高度系数最大值 | 2.09730e−5 | 2.280324750e−5 |

q085的delta=.12499169713346911，boost_length=.18402293140495685，最大collocation残差9.98e−7、Frenet margin最小.0051360474。q0775旧first K7的κD样本为33.1660532309，调整后净改善约2.75%。这些只提供局部必要预算，有限空间采样不证明reach，也没有支付held≥.2D。

主要待抢救文件（相对本课题）：

- computations/alternative-neck-curvature-map.py：新增可选interior-jet-lobes；
- computations/alternative-neck-darboux-map.py；
- notes/alternative-neck-design-warm.md；
- notes/alternative-neck-loop75-sync2-v098-q0775-size-screen.json；
- notes/alternative-neck-first675-loop75-sync2-v098-q0775-m20.json.gz、同名summary及coeff_00.npy.gz；
- 同q0775前缀的curvature-map、size-screen、darboux-map、darboux-conditioning JSON；
- notes/alternative-neck-first675-loop75-sync2-v098-q085-m20.json.gz、同名summary及coeff_00.npy.gz；
- 同q085前缀的curvature-map、size-screen、darboux-map JSON。

first675的seed、resonant profile和linear-root小文件已经在122c66中。不要误收旧q070/M16失败大系数包。

## 3. 必须保留的二阶插值问题

q0775短sync段的保存物理五次PPoly，区间宽约3.24949e−5；其二阶系数与点上PDE投影相差.03822。两端差接近零、中点约3.16e−6，内部双峰却达到.05354。局部17点Darboux样本约.004781，比原nodes/mid审计.003414更大。

同一多项式用longdouble求值仅变1.23e−16；384→976角点的PDE二阶投影差4.56e−14；不是这里的普通求值舍入或FFT混叠。证据支持有限collocation端点积分不一致经五次重构放大的解释。

五次端点位置修正
$$S(u)=u^3(10-15u+6u^2)$$
的二阶导数在
$$u=(3\pm\sqrt3)/6$$
取极值，而在两端和中点均为零。后续C²比较应至少包括这些区间内部点。

q085原Darboux审计1.77107e−5也漏峰；补全部区间内部极点后为.00409591146，仍位于sync段，局部κ约.615，并非全局κ峰。没有将点上PDE二阶写回saved map；这样替换不能算同一显式曲线的真实二阶导数。改善必须来自真正同g降tol/加密后的显式曲线比较。

## 4. 较大尾输入已经真解：数值包尚未推送

输入方向来自原loop8的真实q070/M18 checkpoint，完整18H保留，M24另外补6个严格零。原H2=−2.24807581119149e−5、H4=−1.651528456675837e−8。原H真包和external-plan已在122c66。

统一外倍数依次约2、3.5、5.337898277389474，三次请求全部成功。最终H2=−1.2e−4、H4=−8.815690903949647e−8，M24/N512/depth8/parts8/steps12：

| 项目 | 最终值 |
|---|---:|
| shooting残差 | 2.36275e−10 |
| physical fullD | 3.983863723712588e−9 |
| 源normalizedFullDefect | 4.615919516507773e−7 |
| 乘parts8后的原profile规范量 | 3.6927356132062184e−6 |
| actualMetric | 2.255973571774276e−13 |
| formal κ最大 | 7.9942546936068855 |
| minA | .3788028508906767 |
| minD | .9996963353417263 |
| 首模实际cut slope | −.0014205594760717819 |

原profile规范量仍高于1e−6；没有降低阈值。外倍数不是已得到的强prefix。minA点r=.2348117057、θ=0，κ仅约.00580587；κ最大点r=.0551261031、θ=π/2，A约1。

待抢救：notes/numerical-neck-q070-tail24-external-response_0003.json.gz，及该前缀summary/config/response_adapter/curvature；computations/numerical-tail-defect-spectrum.mjs；notes/numerical-q003-tail-depth-trace-readout.json。

频谱诊断脚本已写但未运行，同H下一档加密尚未开始。先诊断Darboux频率48以内/以外的贡献，再只选升M或steps12→24之一；不能凭小metric宣称二阶精修完成。原external-plan中已有完整重现命令；若工作区丢失，按已提交计划及原H warm包重生。

## 5. root分支和未完成进程

- 新loop7.5/sync2 q070把自然负cos6绝对值增5%后真成功：1008节点，metric4.75611e−8、κ8.66715、height1.905439、tail Hmax1.99660e−5。净局部预算比基点更差。checkpoint为root-neck-loop75-sync2-triple-q070-c6more-retained-m18，包尚未推送。
- 新first675 q0775三控制，cos6=−.00020046211102671033（自然绝对值95%），M20/N512/tol2e−7，命名root-neck-first675-triple-q0775-c6less-m20。环境断开前只见开始求解，**没有成功终态**。
- 固定g q040 M28初次、径向分批重试和随后M24/N512/tol1e−8，均以exit137结束，只有迭代表头，没有可验收prefix结果。进程/资源原因未证实，不能作为数学不存在证据。已完成固定g链仍止于M20。
- root_fixed_chain_audit.py所调用的compare_shape已在工作区加入每个保存区间的两个上述内部极点及中点；此修改尚未推送，也未重新产生链报告。旧报告只声称原采样网格的误差。
- root_tail_replay_config.py已写但其调用被环境断开拒绝，未验证；文档替换是否执行不得假定成功。恢复后用全新输出目录重定位仅I/O路径，并验证所有非路径配置逐字相同，避免覆盖已提交数据。

## 6. 无限尾入口审计与必须修正的metric语义

新增但未推送：notes/geometric-infinite-tail-entry.md、computations/geometric-infinite-tail-gates.py、notes/geometric-infinite-tail-gates.json。**其中calibration限定补丁因断开未落盘，恢复后必须先修订，不能原样无条件采用。**

当前delta0=.006、eta0=.0003与源R20的.08/.004同为.075倍。局部Q估计只要求eta/delta≤.05等固定界；L/A可以改固定常数，保留幂指数。它支持同机制的参数转移，但不自动认证当前保存的metric或trace。

R20的18参数是中心无穷端标签及17个cut不稳定谱坐标，不是18个任意cut高度。提取b2..18并解中心方程后，仍须消去第一模稳定差、2..18模稳定差，以及全部j≥19的完整二维差。有限DN每模一个Robin条件不自动替代这一流形条件；R20也不分类所有C²尾。

与实际prefix的剩余方程为
$$U_{\rm cut}^{P}(c)-\mathcal P_{N\to{\rm cut}}\Gamma_N(b)=0,$$
并保留完整mean导数和Cartesian两jet。直接照搬极粗常数给当前J0=5577、乐观Green账本N尺度约1.12e37；这是证明账本的费用，**不是实际所需深度或不可行性结论**。需要重估实际有限块Green和非线性球。

校准必须区分：

1. g_root以真实canonical mode2传递矩阵(21)=0的精确根alpha_n定义；512步只是近似，尚欠alpha误差、profile两jet及有限warp积分的绑定。
2. 当前rejoinR20At=null调用createBalancedTail，直接使用数值cal.alpha。若把这些存数定义为g_stored的精确系数，换成真根或512→1024通常会改变g，不能冒充固定g加密。
3. 对g_stored，一条充分路线是证明有限低模加权矩阵差受C_alpha delta_n^(1/2)控制，并保留高模统一界和非线性球。此误差可并入Green门的C_E；固定单胞元残差容差不提供全层可和界。
4. 若(21)非零，精确中心轴及简单乘积公式不能照搬，应采用扰动后的Green/中心束。可选rejoin模块的真根声明不能借给未启用该分支。

本地依赖manifest曾增至90件852195B，新增pinned源notes/general-exact-mild-tail-quadratic-material.md（13650B）；该manifest变更尚未推送。main仍为89件838545B，可从固定源提交869436630c99aa5a68afb55bd8877c826034d117恢复缺文件。

## 7. 恢复顺序

先核对工作区是否保留并抢救上述完成包；不要重跑已经完成的三次外倍数。然后正常拉取main、检查两README，并将数值包经终端提交（每件<5MB，数据>1MB gzip）。修正calibration声明和内部二阶采样，再做真实同H精修、q085原g精修/三控制净预算，最后才选择下一增幅起点。目标仍是完整闭图held≥.2D和全时reach≥.03D，未放宽完成标准。
