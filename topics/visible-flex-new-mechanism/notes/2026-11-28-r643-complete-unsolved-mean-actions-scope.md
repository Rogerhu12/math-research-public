# R643：真实1566列 mean/position 联立求解的公开 Actions 范围

2026-11-28，会话 Astra-new-mechanism-8cdb3418-20261128。
**状态：新完整数学输入和可运行实现；尚无此 scope 的数值终态。**
接已发布的 [R643](../results/R643-fixed-metric-unsolved-mean-height-and-periodic-position-system.md)，
不改变正在运行的 R631 新 R=.8 设计。二者的 E 身份不能互借。

## 1. 真实来源与新的必要求解

唯一当前来源是自然完成的 run46117718197/job140895158286/source19de4da3，
原 FINAL 459140 B、SHA
1fb5abfdf70e6c8154938b07ec5bd3353b68735c0dd5fd49f704204e65bd024e。
实际保留 response SHA19519575...、hard tau1；新接受步数为0。
[原终态](2026-11-28-r618-centered-complete-state-natural-terminal.md)已记录两条真实
近帽 attainer，而不是把所有失败推给没有定位的舍入。

新输入完整继承原 centered scope 的571219 B literal stdin，
以及这份自然 FINAL 的全部失败、接受态、原费用和更早费用。没有把旧 pending
试值当成接受态，也没有以新文件名重复旧 fixed-E scalar-elimination 范围。

冻结目标仍为86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5；
参考 H=.5188903877153482、amplitude=1e-5，原内口、所有真实尾、旧角场
和完整端核心映射不变。新联立系统求解实际 m，而不是继续求 trial lambda=s/W。

## 2. 已接通的全部方程

显式链用同一参考 Decimal split 构造 E、E'，然后直接评价

- p=-W+s_seed+delta m_r+f_r、p_r=-W'+s_seed_r+delta m_rr+f_rr；
- 原 b、u、N 和完整 D=C p_r-E B²-E'M/2；
- canonical F=<a>-1、G=<R>；
- R643 的实际归一周期相位及完整 S，保所有 F/A 与 G 项。

每次 trial 和每条参数方向都不再求 mean 根，不除 W 或 c0。
外侧 seed 的旧 zeta 坐标只在固定种子读入时解码一次；这不是新 trial 坐标。
所有正域分母和完整离解权重项继续保留。
近帽真退化留在全 Jacobian 内，没有被宣称已经有一致逆。

原 accepted m_seed 只在实际所需半径评价，且按半径复用。
缓存保其同源 target、实际 Decimal x/s_r、根 receipt 和标量；
不保每个 supplemental 半径的重复512角种子数组。
所有这些重建都进入新科学时钟与原模块费用，没有把未保存 workspace 算成已付数组。

当前真角空间的1472自由列全部保留。
新 mean 的94条自由函数是61条去完整核心迹的原 bulk、28条原 compact、
4条真 Gaussian 径向尾和1条近核心常值 plateau。
两条核心 mean lift 为同实际 P 的从属函数，不另加自由坐标。
总数1566；原 tau 硬等于1，旧 H 继续只属于冻结 E。

## 3. 全列、全行与自动细网求解

初始范围使用原950个 work 径向点、256角点、512 canonical mean 点。
全部121600位置行，加每半径 F 与 rG 两行，共123500行。
fine仍为原1728径向点、512角点，总445824行；所有原点与输出奇模保留。

每个真正新迭代生成全部1566列解析 J，并使用原 R613 全行 QR/SVD。
不形成 normal equations，不裁奇异方向、不选高残差行。
声明的最多800000000个 materialized J 元素覆盖原完整 fine 的698160384项；
完整 fine J 的主数组约5.59 GB，方向按16列分块、QR按4096行分块。
新模型也提供完整真实 row-pass 接口，未把其备用接口冒充已算过的 J。

步长只使用真实 b/u/N/A 正域、实际高度与 p/(1+sqrt(E)) 方向，
并保存准确 attainer。没有原 lambda 盒，也不按 c0 的大小裁列。
每个实际 nonlinear trial 同时消费新真实尾界和所有位置/F/G 行。

work的1e-8只是晋升分配；其后自动进入同一 E 的完整 fine，目标2e-9。
即使 work有限空间停滞，也继续同一来源的完整 fine 联立求解，
而不是将 work stall 当成本任务完成。
细网目标也要求 F 与 rG 达到同一有限阈值；最终真实直接 metric 仍另读。
每网最多200个新迭代、每J最多6个damping方向、每方向11个真实线搜索试值。
最大科学时长18000秒，最后6000秒用于同态完整读出；这是资源上限，不是完成标准。

## 4. 新 mean 的真尾不能借旧隐式根

新尾消费者只复用原 infinite-germ/Gaussian/source inequalities。
固定 accepted seed 的已付 cap-to-mouth mean 证据从原自然 FINAL 直接消费，
不重跑它的旧 gate。

对当前角响应，完整加入10条旧真 germ 与96条新 angular Gaussian。
对94条新 mean，90条由真实支撑在此尾准确为零，4条 Gaussian 完整入界；
没有把浮点 underflow 当成一段新数学零函数。
Gaussian helper 的径向三 jets 与 mode 参数无关，借其 mode=1 调用只取这些
径向公式，不向实际角场加入任何 j=1 项。

新全尾正域界直接使用真实 mean slope：

p/W 的绝对上界包含固定 seed s/W 界、实际新 mean_r/W 界与全部实际角场界。
由此给 b/r、u²、N 的整个 cap-to-mouth 下界，并在 seed 到当前场的同一
正域内给真实 F 的 Lipschitz 上界。这里不再把原“由当前角场解出的mean”
冒充独立的新 m，也不施加新的 trial lambda 根盒。

原全部7类源误差仍明列未付；新 G 与完整 S 的连续真尾误差也明确未闭，
不默认零。该消费者给的是新输入的必要实际真尾物理域和高度输入，
不是完整连续 PDE 或 README 证书。

## 5. 实际高度和实际位置消费者

最终读出若已在同 q、同完整 fine，则直接复用已付 data/state；
只有当前还在 work 时才构造完整 fine。

原 pre-tanh 三 jets、全部 post 至j96、全部 D 输出谐波、完整 tail L_j
和实际 mean 三 jets 都保留观察。没有按输出 Nyquist 或旧44带漏掉从属项。

真实 m_seed 仍定义为从 cap 积分 s_seed。
数值读取复用所有已付端点 s_seed/s_seed_r，每个 fine span 只补一个实际
midpoint，采用两半段 Hermite 积分并保存粗/细差；最后真实核心端使用原
s_seed 的带变量替换 quadrature。全 m 再加真实显式 mean 函数；
m(R) 从实际积分和 plateau 得到，中央柱与反射中心不被偷偷设回零。
这些求积差、根误差、源误差都没有被改称 interval certificate。

两套原 h、h/2 stencil 在同一份归一周期 Y 上求真实径角导数。
保留全部原 fine 半径，合并重复 supplemental 查询，复用已付 fine Y。
原纯 stencil 几何公式读取新的实际 p、p0_r 与完整角 jets，
而不是把旧隐式 mean 的导数拿来替代。
两套实际 metric、曲率、outward 和 identity/direct 差都必须记录；
当前有限恒等式不授连续资格。

## 6. 发布绑定与费用

入口为 scripts/r643_actual397_coupled_mean_20261128.py，
request为 computations/request-r643-actual397-coupled-mean-20261128.json.gz，
workflow为 .github/workflows/visible-r643-actual397-coupled-mean-20261128.yml。

本地只作源码、AST、literal来源和hash绑定处理，没有执行任何科学构造。
所有64个完整依赖（含原冻结身份确实读取的旧workflow文件）逐项绑定；
新request按根规矩压成单一 gzip，并使用既有
run_inverse_state_gzip_stdin_20261127.py 通过stdin传送真实重建输入，
不落盘额外科学载荷，不向科学命令行暴露凭证。

完整科学stdin为1113038 B、SHA256
 a91b811ec60787dba772b233e52160e71054c76d6d6730b79753efcc6b84a011。
压缩请求的规则读取提交号在发布pull后更新，其准确运输字节/hash以实际提交中的
该单一gzip文件及Actions运行收据为准；这个元数据更新不改变上述科学stdin或五份科学源码。

hourly Rules使用单独的
computations/r643-hourly-rule-metadata-20261128.json，
仅681 B、SHA256
a9b4d7987b411f4d9b8ec6e46ba342d308ca1692976e179e33eb1b5eaa1d446c。
其中只有已读README blobs、queue、pull-helper hash与完整gzip路径；
它没有科学载荷，也不是请求数据分块。该metadata已进入gzip请求的source绑定，
不应再单独更改它；冻结driver仍按原JSON读取它即可。

运行每55分钟在实际状态/逐块计算安全点 public pull，比较根与题README准确差异。
有差异或pull失败即保存旧scope实际态、停止该旧规则scope，由主会话读差异续接；
仅为完整终态费用序列化恢复原pinned源码，不继续旧规则科学。
私库每小时实际pull由主会话承担。

终态完整保存真实末接受1566坐标、pending另列、全部QR/J/源根/试值/直接查询费用，
先前运行的账原样继承但不重计。当前小核心不冒充宏观进展；
本范围也不声称无限角带一致逆、整个闭面reach或README已经完成。
