# warp 后有限 cell 的物理 m2 重校准（进行中）

会话：Astra-visible-flex-4ffd372b / closing_geometry，2026-11-09。
可信度：有限 profile 的数值研究；尚非非线性闭尾、统一尾定理或完成的闭曲面。

## 物理变量与校准目标

轴对称图背景 slope 为 w(r)>0。m2 高度模态满足
$$f''+(w'/w)f'-(4w'/(rw))f=0.$$
定义
$$u=f/r^4,\qquad \pi=r^8w u'/\sqrt{12}.$$
直接代入得到精确物理方程
$$u'=\sqrt{12}\,\pi/(r^8w),\qquad \pi'=-\sqrt{12}\,r^6wu.$$
每个有限 cell 使用原尺度 $\mu_n$ 仅作数值归一化，状态为 $(u,\pi/\mu_n)$。
重校准要求实际 warp 后的首列传输从 $(1,0)$ 出发，在另一端满足 $M_{10}=0$；
原 source 的校准参数不再被当作这个条件已经成立的证据。

新脚本 `closing_recalibrated_tail.mjs` 缓存各 cell 关于 valleyControls[n] 的径向积分 A/B。
给定全局 warp 系数 alpha 后从深到浅逐个解 beta_n，再以实际端点半径更新 alpha。
深背景、cut jets 的定义保持不变；capMode 可选择原构造器或主线的新 cut-preserving 版本。
所有依赖通过 `closing_tail_sources.mjs` 验证 Git blob 后导入。

## 首轮单 cell 诊断

脚本 `closing_cell_scan.mjs`，每 segment 128 RK4 步：

- 主线 cut-preserving cap=.02 / K6 / width=.35，cell0 的 $M_{10}$ 在 beta=1 与 2 之间过零。
  beta=1 时列向量约(-.0178353,4.65854)，beta=2 时约(.514720,-257.520)。
  因而过零附近的 u 增益很小，单点校准可能放大内部高度；不可提前声称改善幅度。
- 原 constructor a=2.75 / wCut=.1 / K5 / width=.5，cell0 同样在 beta=1 与 2 之间过零。
  对应列向量约(-1.66993,114534.34)与(-.615342,-78974.83)。
- beta=0 的 alpha、heightSpan、minimumWarpWidth 已由新缓存构造器复现到约末位舍入。

原始扫描保存于 `closing_root_cap002_cell0_scan.json`、`closing_w01_cell0_scan.json`。
下一项计算为完整 protectCell 深度的实际重校准和总宽度闭合，随后重新计算物理 DN、
全尾线性化 H_theta_theta 正性阈值与曲率采样。单个 $M_{10}=0$ 不是这些后续性质的替代。

## 完整有限校准的首个结果：全零动量不是正确优化目标

旧 root N80 几何已由独审发现未改深尾的曲率超界，因此这里只保留其有限校准作为失败输入诊断。
新输入 `closing_root_cap002_p160_config.json` 改用 protectCell=160，属于新固定 metric。

对旧 N80 输入，各有限 cell 的实际 M10=0 与外层总宽度迭代在4轮收敛：
alpha=72.03747985957325，端点误差约4.86e-12，heightSpan=.02166110764319。
但 cell0 增益为 -.0083607069，cell1至5分别约-.579、-.696、-.756、-.803、-.989。
这些压缩层把深部幅度放大；完整诊断的线性化正性阈值反而降至1.19e-14（cell11 valley）。
因此本次全 M10=0 校准明确失败，不能把求根收敛误作可用尾部。
深层实际增益则约-64，beta趋于2 log(alpha)，证明代码能恢复预期的深层扩张支。
输出为 `closing_root_cap002_recal_s128.json`，其 N80 完整背景不满足目标曲率。

cut 的真实 DN 不要求 pi_cut=0；下一轮释放 cell0，并直接优化实际 DN/阈值。
同时引入有限浅 pulse 的非对称 cap；通过平滑改变 log(cap)并加入其导数保持接缝。
`closing_recal_diagnostic.mjs` 输出每层阈值，供识别哪些层过度消耗扩张增益。

## N160 上释放端口及浅 pulse 的结果

`closing_root_cap002_p160_beta0_diag_s256.json` 使用新的保护深度160，保留上述校准的深层控制并释放 beta0。
beta0=0 给真实 m2 DN=5.6776582568、T门1.96797e-12；beta0=-1 也仅提高至7.10e-12。
瓶颈仍为cell11，说明仅释放一个压缩层不足以挽回全零动量校准的损失。

`closing_root_cap002_p160_pulse0_scan_s128.json` 提高cell0首pulse的cap并重新求该cell的M10=0。
首cap从.02提高到.65时，增益从-.00836提高至-.4770，仍未进入扩张支；
首cap=.8开始，最小径宽已约.35022，超过.35预算。
这排除的是这一有限扫描里的零动量选支，不是所有低曲率尾。

## 转为 mode3 的直接门限优化

新通用物理状态保持 $u=f/r^4$，取
$$\pi=\frac{r^4w}{\sqrt{12}}(f'-m^2f/r).$$
则
$$u'=\frac{m^2-4}{r}u+\frac{\sqrt{12}}{r^8w}\pi,$$
$$\pi'=-\frac{m^2(m^2-1)}{\sqrt{12}}r^6wu-\frac{m^2-4}{r}\pi.$$
脚本 `closing_modes_diagnostic.mjs` 使用这一真实物理方程；m=2退化为前文系统。

N160基线（不做全零动量重校准）每segment256步、far48：

| 模式 | 实际物理DN | H_theta_theta线性门 | 纯模态角梯度门 |
|---|---:|---:|---:|
| m2 | 5.6769169976 | 4.1077458e-6 | 5.3863308e-5 |
| m3 | 10.5437607044 | 4.0607627e-5 | 2.2207018e-4 |

m3各层T门从外向内为4.06e-5、6.57e-5、5.30e-4、.0213、4.42、4815等；
因此核心是前3至4层，深部存在大量未用的线性余量。
原始数据 `closing_root_cap002_p160_modes_s256_far48.json`。

直接优化不再要求M10=0，而针对最小T门与角梯度门。
`closing_optimize_gate.mjs` 对外侧beta0至beta3做多初值坐标搜索，所有评价使用实际profile和固定far。
搜索过程每个候选均是不同metric；最终选定参数后必须另做同一metric的步数/far加密。

直接搜索得到 beta0…3=[1.25,2.4375,3.0625,2.6875]。
其同一metric s512/far64复核：m3 DN=10.5454484371，T门=.0001122068073，角梯度门=.0007956539394。
基线门约提升2.76倍，仍未达到主线约.00128的cut高度需求。
参数 `closing_root_cap002_m3_opt_s128_config.json`；同metric复核
`closing_root_cap002_m3_opt_refine_s512_far64.json`。
mode2在这一同metric上的门仅9.96e-9，不能把m3改善套到m2。

提高最外1至3个cell的pulse与valley cap的粗扫描未直接产生数量级改善，
`closing_root_cap002_m3_outercap_scan_s96.json`保留全部21项，包括宽度不够的失败项。
后续结构改造保留深部到选定cell的首个高平台，用C²混合接恒坡度annulus，
最后再恢复精确cut jets；它直接移除无效的浅valley，仍以真实导数重算K6径向warp。
新脚本 `closing_flat_sleeve_scan.mjs`。

恒坡annulus扫描已明确不改善当前基线：删除到cell0后，最坏门移到cell1，
w_flat=.02–.2的门仅3.70e-6至4.50e-6；继续删除到cell1后门降至约2.4e-7，
到cell2后约1.1e-8。原因是删除层同时移除了供深谷使用的外向放大。
`closing_flat_sleeve_m3_scan_s96.json`保留各个实际profile；这是数值失败定位，非一般障碍定理。

主线m3短prefix的直径预算允许尝试K8–9。
新 `closing_asymmetric_gate_scan.mjs` 保留外侧谷，抬高其beta并只加强首pulse，第二pulse仍cap=.02。
它针对局部谷的正性与整体放大之间的权衡，不要求M10=0。
扫描同时保存heightSpan≤.08的最佳候选和不限该条件的最佳候选，供主线按真实D预算选择。

## 附加角小量标签勘误

上述早期JSON及表格中 `gradientAmplitudeThreshold` 曾存 r*w/(m*abs(f))。
它只是在控制归一化 P=f_theta/(r*w) 的 |P|<1 小球，**不是投影或嵌入的必要条件**。
由实际momentum engine的 S=1-w²P²=1-f_theta²/r²，角投影必要条件是 |f_theta|<r；
D还含径向高度导数，须同时检查。m2在wCut=.01时幅度<.003的旧必要性表述已撤回。

新代码的 `gradientAmplitudeThreshold` 改为正确角投影界r/(m*abs(f))，
旧保守小球另命名 `rescaledAngularSmallnessThreshold`，并明确其充分小量范围。
旧JSON原样保留；其H_theta_theta门、真实DN、最坏T点不变。
已有直接优化的最优点均由T门主导，该勘误不改变其T结论，但新搜索使用正确标签。
新增可选固定幅度的形式二基型诊断：对线性height lift与固定metric计算Hess_g h/n_z，
它仍含二阶Gauss缺陷，只辅助筛选曲率风险，不是实际闭曲面的reach证书。

## K8–9 非对称浅pulse的改善

98项粗扫描 `closing_m3_asymmetric_k89_scan_s96.json` 的最佳T门为4.54232464e-4：
K9、width=.35、N160、cell0首pulse cap=.4、第二pulse cap=.02、valleyCap0=.1，
beta0…3=[3,2.4375,3.0625,2.6875]，其余beta为0。
实际m3 DN=11.53880823，heightSpan=.0403232521，最坏点移至cell4 valley。
相对于最初m3基线T门提升约11.2倍；仍非非线性存在或reach结论。
配置 `closing_m3_asymmetric_k89_scan_s96_best_config.json`。

K8、首pulse cap=.2、同一beta给T门3.38163875e-4、DN11.25191296、heightSpan=.0274578389。
两者均继续优化beta0…5，同时以同一metric做步数/far加密。

六谷优化的固定候选与s512/far64复核：

| 候选 | beta0…5 | m3 DN | T门 | tail height |
|---|---|---:|---:|---:|
| K9 / 首cap .4 | 3.125,2.8125,4.0625,5,5.25,4.0625 | 11.5412877431 | .0006854580991 | .0403638053 |
| K8 / 首cap .2 | 2.8125,2.9375,4.25,5.1875,5.375,4.125 | 11.2490970642 | .0005485434906 | .0274171722 |

它们的真实角投影高度界均约.2；旧归一化小球界不能再称必要条件。
在指定cut高度幅度.001的形式线性height二基型诊断中，
K9候选的max|kappa|≈13.1869、min线性A≈-.45888；
K8候选约12.1649、-.82301。故两者都不能作为当前目标幅度的有效闭尾，
而且即便T门刚达到目标，仍要单独核算非旋转曲率余量。
形式曲率不满足完整非线性Gauss，以上用于明确筛选失败，不作实际曲面不存在结论。
复核文件 `closing_m3_k9_opt_refine_s512_far64_a001.json`、
`closing_m3_k8_opt_refine_s512_far64_a001.json`。
