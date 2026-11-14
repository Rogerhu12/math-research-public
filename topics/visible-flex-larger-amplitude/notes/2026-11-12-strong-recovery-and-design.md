# 强前缀恢复与新轮廓设计

日期：2026-11-12。状态：**数值中间进展，未完成闭图或原完成标准**。

## 1. 固定源和恢复边界

使用 `computations/source-dependencies.json` 的固定源提交
`869436630c99aa5a68afb55bd8877c826034d117`，由主会话恢复到当前 scratch 下的
`visible-flex-source/topics/visible-flexible-closed-surface`。旧
`/workspace/scratch/83b864ada613` 不存在，因此按 2026-11-10 环境中断记录
重新执行当时未推送的成功计算。下述包是本次新求解结果，不冒称找回了旧字节。

## 2. first6.75 / loop7.5 / sync2，q=.0775 恢复

从已提交的 `alternative-neck-loop75-sync2-v098-q0775-m20.json.gz` 出发，
将第一下降转角曲率上限从 7 改为 6.75，保持 vd=.98、其余非控制参数不变。
明确使用 `scale_radius` 改变初猜像，随后重新求非线性 BVP。
这是**改变度量的设计步**，不是固定度量加密。

运行（在课题目录，`SOURCE_TOPIC` 指恢复出的固定源目录）：

```bash
python computations/alternative-neck-design-warm.py \
  --source-topic "$SOURCE_TOPIC" \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --profile computations/alternative-neck-first675-loop75-sync2-v098-resonant-profile.json \
  --q .0775 --modes 20 --angular 512 --nodes 401 --max-nodes 3000 --tol 1e-6 \
  --meridian-chart all-knots --second-control boost_length --newton-backend refresh \
  --design-fields descending_turn_curvature --design-latitude-map scale_radius \
  --restart notes/alternative-neck-loop75-sync2-v098-q0775-m20.json.gz \
  --out-prefix notes/2026-11-12-strong-first675-q0775-m20
```

五轮配点从 422 点增至 859 点；最大配点残差 `9.9969278879e-7`，
物理有限线性 DN 边界残差 `5.5062918e-19`。
实际控制为 `delta=.123115428379487`、`boost_length=.184865957179717`。
完整保存包包括 `.json.gz` 和 `_coeff_00.npy.gz`，摘要另存 `-summary.json`。

| 指标 | 新重做值 |
|---|---:|
| 默认节点/中点 metric Fourier l1 | 2.8989342260e-8 |
| 默认节点/中点 Cartesian Darboux l1 | 3.3184902788e-5 |
| 半图最大高度样本 | 1.93336036135 |
| 主曲率最大样本 | 8.22224498602 |
| 末端高度系数绝对最大值 | 2.09730302734e-5 |
| 最小 Frenet 平方根余量样本 | .00513742405819 |
| 核心 π/2 相位支撑差下界 | .154552269885 |

高度和尾口规模与旧交接吻合；不要求自适应网格或高阶系数逐字一致。
此处仍只匹配有限**线性** DN 尾，没有把实际非线性尾或闭帽认证搬过来。

## 3. 真实五次曲线内部二阶采样

新增 `computations/strong_interior_jet_audit.py`。它在全部保存区间的中点以及
`(3±sqrt(3))/6` 处直接对保存的五次 PPoly 求二阶导数，并用实际物理角链式法则
计算 metric、Cartesian Darboux 张量和主曲率；点上 PDE 二阶只用于作差，
绝不替代保存曲线的实际二阶导数。

```bash
python computations/strong_interior_jet_audit.py \
  --input notes/2026-11-12-strong-first675-q0775-m20.json.gz \
  --source-topic "$SOURCE_TOPIC" \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --angular 512 --radial 801 \
  --out notes/2026-11-12-strong-first675-q0775-interior-jets.json
```

4,232 个径向采样点、512 个角点得到：

- metric Fourier l1 `2.89977885e-8`；
- Cartesian Darboux Fourier l1 `1.81835032e-4`，高于原节点/中点报告；
- Darboux 张量逐点 Frobenius 范数 `8.39623994e-5`；
- 实际二阶与 PDE 二阶重构的向量差 `1.66469720e-4`；
- κ 样本 `8.22238760`，位置仍在第一下降转角。

二阶缺陷峰在短同步段，区间宽 `9.69566463e-5`、区间坐标
`.7886751346`。这再次证实仅节点/中点不足以检查五次实际二阶；本次重做的
网格/角阶不同于中断前计算，不能把较小缺陷单独归因于某一个修改。
以上仍是有限空间采样，不是连续域上界。

## 4. 保留 warm 网格的适配器

新增 `computations/strong_neck_bvp.py`：

- `--workflow amplitude|design` 选择现有脚本；
- `--nodes 0` 保留旧成功曲线的物理网格，经明确的正径向坐标映射用于新初猜；
- 仅把径向独立求值/Jacobian 分为 48 点批次，避免大临时 frame；
- 原源文件不修改，内存替换的精确文本、原哈希和适配器哈希写入输出。

这没有更改物理方程、边界、参数定义、容差或正根守卫。设计步和增幅仍然
重新求解，不能因保留网格而声称固定 g。

## 5. 两项针对性线性预设计

从 first6.75/loop7.5/sync2 的线性根出发，固定 vd=.98，仍只解
`delta,boost_length` 两个共振条件，使用现有
`alternative-neck-fixedspeed-root.py`。这些都是线性筛查，不是已实现的强前缀。

| 设计改变 | delta | boost_length | 背景半高 | 最大方向残差 |
|---|---:|---:|---:|---:|
| vu .25→.35 | .138596205734 | .125608934990 | 1.77145156626 | 2.239e-12 |
| boost_speed .86898→.78 | .115947179215 | .290841574874 | 1.98499650771 | 8.343e-12 |
| vu=.35 后，入口加速度 .45→.3 | .138973343513 | .126667127719 | 1.80266877902 | 2.790e-10 |

原 first6.75 线性根背景半高 `1.8080071221`。因此提高 vu 的重新匹配降低了
高度约 .03656；降低 boost_speed 的设计反而增高，先不沿它推进。
降低入口加速度会放宽 R7 的局部门槛，但 R12 的三谐波达到者还必须逐项检验
其连续域可行性，不能把仅由对偶交点得到的数值当作可行核心。

## 6. 正在执行的续算

first6.75 q=.085/M20 已恢复成功，保持旧物理网格的求解用两轮、877 节点，
最大配点残差 `9.98e-7`。metric l1=`2.21321164e-8`、κ样本=`8.37793274`、
height=`1.94251540367`、Hmax=`2.28032509e-5`。实际控制
`delta=.12499169711497989`、`boost_length=.18402293134457642` 与旧交接约在
1e-10 内一致。核心相位支撑差下界 `.1694710757` 仍远低于闭图 0.2D 目标。
保存前缀 `2026-11-12-strong-first675-q085-m20`。这仍是新g增幅设计和有限线性DN。

## 7. 可选角速度 boost 与当前实际设计

新增 `computations/strong_angle_boost.py`，并在原 provider 加默认无效的
`boost_law=angle` hook。新的 boost 用已有 flat-top 角速度积分，保持确切的
起终速度、boost_length 及零端点加速度；它是新的 C² 物理度量。
默认 cubic 的整段记录、物理 knots、半高以及 1,001 点三 jet 与加 hook 前
逐位一致；角 boost 的两端加速度恰为零。检查记录为
`2026-11-12-strong-angle-provider-check.json`。相同 hook 供线性筛查、BVP、
保存曲线加载和实际一/二阶 jets 使用。

在 vu=.35 下重新线性匹配，得到 delta=.1458033978026112、
boost_length=.11507506464263191，背景半高1.79331447849，最大方向残差
9.20e-10，boost自身曲率上限6.57007094878，全prefix背景曲率峰仍7.5。
它比原vu=.25的背景高度低约.01469；其价值还在于避免短cubic boost的曲率峰。

实际非线性新g测试已从本次 q085 成功包启动，明确声明改变字段
`vu,boost_law`，用 radius-scaled 初猜和全部旧物理网格。外层 mesh tol仍1e-6，
M20/N512，内部Newton残差阈值因子1e-4；后者只加严求解停止条件，
原方程、边界、正根域和mesh容差不变。输出前缀
`2026-11-12-strong-angle-vu035-q085-m20`。该进程后来以 exit 137 终止，
仅留下 start 与第一次迭代表头，没有成功终态或可验收输出；不把它解释为
数学失败。同期父会话的另一固定g大LU求解也出现137，因此开始检查实际
Jacobian的内存/线性求解路径，而不是反复启动同一大LU任务。资源原因尚未证实。

所有结论和本节状态会随计算终态更新；没有新的闭合、reach 或完成声明。

## 8. 第一下降转角的非对称角速度筛查

单独的新脚本 `computations/strong_turn_bias.py` 仅用于线性预设计，目前
**尚未接入 provider 的默认实际保存/加载路径**，因此含此设计字段的配置不可
直接交给普通 BVP 当作已经实现的轮廓。

设旧转角用归一化坐标 u∈[0,1]，平滑速率窗口为 w(u)，
∫w=1−ε、w(1−u)=w(u)。把角速度率改为

`sign(Δφ) K w(u) [1+b(2u−1)]`，其中 |b|<1。

由于反对称积分为零，整个转角和物理长度都保持不变，两端角速度仍为零，
从而保留半径函数的 C² 接合。b>0 使第一下降段前部更慢、后部更快，
针对已观察到的前部实际曲率峰分配曲率预算。背景曲率上界为 K(1+|b|)。
积分采用分段局部多项式原函数，避免右端全局多项式大系数抵消。

在 angle boost / vu=.35 的线性根附近：

- `b=.1, K=6.75`：delta=.144687339723、LB=.106710686547，方向残差
  <1.90e−13，背景半高1.78494358008，比对称 turn 的1.79331447849低约.00837；
  全prefix背景曲率峰仍7.5。它只有线性根，还没有实际非线性前缀。
- `b=.3, K=5.7`：受约束求解停在LB下界.04，残差约.004485，且很短boost的
  背景κ约18.9。此尝试**不是**合格线性根，不送入非线性求解；不据此声称
  非对称设计不存在。

相应参数、调用和小报告以 `2026-11-12-strong-bias01-k675-*` 与
`2026-11-12-strong-bias03-k57-*` 保存。当前计算优先级仍是真正把q增大及检查
三控制cos6方向，不在这些线性筛查上停留。

## 9. 同一 BVP Jacobian 的平衡 QR 因子

angle/vu35 的大 LU 任务只留下 exit 137。当前没有证据把它称作方程不相容；
先解决可执行的高模线性系统。新增 `strong_block_qr.py` 的接口为
`BlockQRFactor(J,n,nodes,parameters).solve(rhs)`。

实际 Jacobian 的每个内部块只有

`A_i Δy_i + B_i Δy_(i+1) + C_i Δp = r_i`，

另有只作用于两端和参数的边界行。对相邻两个块，用竖直堆叠的
`[B_left; A_right]` 作 QR，正交变换消去中间节点，留下同样形式的粗块。
按平衡二分树递归，最后只解 `2n+k` 阶边界矩阵，再三角回代全部中间节点。
只要原矩阵非奇异，精确算术中这些局部被消去的列必满秩，故这就是同一个
Newton 系统的精确因子；没有截断、正规化或传播长转移矩阵。实现会拒绝不符合
相邻块/端点边界结构的输入。浮点性能仍须由真实矩阵残差检验。

实际检查器 `strong_block_qr_check.py` 从 angle/vu35 的真实新g warm 中构造
M12、122节点、n=37、k=12 的完整 collocation Jacobian，大小4526，389236非零：

| 项目 | 结果 |
|---|---:|
| 实际函数/边界取值 | 1.082s |
| 实际 Jacobian 装配 | 9.890s |
| QR因子 / 单次回代 | .708s / .069s |
| sparse-LU因子 / 单次回代 | .228s / .0023s |
| QR相对后向误差 | 3.944e-16 |
| QR步与sparse-LU步的相对差 | 1.061e-12 |

它是线性代数诊断，不是新曲面成功；输出中明确 `inspection_only=true`，
检查后有意结束而不运行 nonlinear solve。QR较慢，但避免全局LU fill；
没有仅凭这些小矩阵数据宣称大矩阵运行一定成功。

`strong_neck_bvp.py` 提供可选 `--linear-solver block-qr`，默认仍为原 sparse-LU。
精确的后端替换、因子源码哈希和每次因子耗时保存到记录；保持原Newton merit、
正根域、线搜索和容差。源码哈希已改为运行开始缓存，避免结束时读取被同步移动的脚本。

随后重启同一个 angle/vu35/q085/M20 新g设计、原877节点 warm，改用 block-qr，
内部Newton恢复默认factor=1（父会话实际collocation诊断已说明1e-4不自动结清
真实二阶误差）。新输出前缀 `2026-11-12-strong-angle-vu035-q085-qr-m20`。
这与先前被终止的LU任务分开保存，不覆盖失败事实。

此第二次 M20 任务同样以 exit 137 结束，只有一次 `block_qr_factor` 事件：
n=61、877节点、20参数的因子完成于3.203s，其后没有首个非线性迭代终态，
也没有输出检查点。因而 QR 的局部分解本身已经完成，但资源终止的真正原因
尚不能确定。这两次任务都没有保留峰值RSS，不把理论存储估计称作实测。

下一次实际新g计算降为 M12/N256，初始301网格加物理分界点，max_nodes=1800，
仍用 tol=1e-6 与默认内部 Newton 阈值。`strong_neck_bvp.py` 新增显式可选的
每Newton/每回溯 `merit/alpha/RSS` 跟踪，以及 `gc.collect` 前后RSS和不可达对象数，
检查旧 Flow 是否因闭包引用循环保留。显式回收不改变数学方程或接受准则。
因本环境没有 `/usr/bin/time`，新增 `strong_resource_run.py` 用 `wait4` 保存
子进程退出状态、信号、墙钟时间和实测 `ru_maxrss`，包括子进程被信号终止时。
输出前缀 `2026-11-12-strong-angle-vu035-q085-qr-m12`；它是低阶新g设计，
即使成功也须再提升谱阶，并单独检查实际物理五次区间内的二阶峰。

### 9.1 M12 实际终态与曲率代价

该任务已成功，873节点、5次外层加密，最大残差 `9.97e-7`，末端BC
`2.91e-16`。实际控制为 delta=`.17706770842712258`、
LB=`.0941592305108482`；自然c6=`−.00038503389259220177`。
其运行墙钟517.8s，`wait4` 实测峰值RSS299308KiB。自动Newton刷新确实发挥作用：
旧因子的一次完整回溯失败后，第三个实际Jacobian使merit从34678下降至.578，
再到1.08e-5，没有修改原接受准则。

新的实际几何并非改善了全部预算：半高从旧q085的1.942515降到1.908185，
但曲率峰样本升到10.4636，位置在短angle boost；有限阶metric l1为
3.0712e-6，Darboux l1为1.0306e-3，均还不是可验收精度。完整区间内双峰
审计4288径向点×512角点确认κ=10.46361274，Darboux l1仍为1.0306e-3，
实际二阶与PDE二阶的差样本峰为4.9875e-4。该分支不能被描述为reach达标，
M12的高支撑模也仍可见，须提高谱阶或改设计。

资源JSON、完整Newton事件日志gzip及实际系数包均已保存。在该任务执行中，
包装器随后增加了只供未来运行的 `triple` 分派；为保留开始时的确切源码，
额外保存 `2026-11-12-strong-angle-vu035-q085-qr-m12-driver-at-start.py.gz`，
解压后的SHA256确认为输出记录的
`aaff5c25d5de96d72ea6570b36bea71dd3e1d9042445216d58aa7de01f7c0e8e`。

接着启动同q085的三控制真实新g步：只把c6向零移动5%，规定为
`−.0003657821979625917`，解 delta、LB、boost_speed 三个物理控制，
保留M12/N256以及873节点warm。输出前缀
`2026-11-12-strong-angle-vu035-q085-c6less5-m12`。这一步仍是设计，
不是固定g收敛。

### 9.2 QR递归闭包的确定性资源修复

父会话的固定g QR计算在三次因子后记录峰值RSS依次602284、767012、
947476KiB，并主动中止，未产生已接受终态。检查明确发现 Python 局部递归
`build` 的函数cell自引用会保留CSR Jacobian，`forward/backward` 的同类cell
会保留rhs/answer；这与数学QR操作本身无关。strong任务开启的显式GC此前
能回收它们，但不能把这种偶然回收当作内存实现保证。

`strong_block_qr.py` 已在递归调用结束的 `finally` 中分别把
`build/forward/backward` 置为None，打断这些闭包周期，不改变任何数值操作或
次序。同一个真实M12/122节点Jacobian的重检已完成：QR后向误差
`3.943828605399385e-16`、QR/LU步相对差`1.0613770767745716e-12`、
Newton步最大分量`961.0140734705743`，与修复前逐值相同。关闭自动GC时，
weakref检查CSR、rhs及answer底层存储的继续保留均为false。
记录为 `2026-11-12-strong-block-qr-acyclic-actual-m12.json`。
修复前helper的确切源码另存gzip，其解压SHA256仍为
`7aae3bf9fb75b3b8b805258574c84e12e57fabbe41f83272867debf16c1a565c`，
用于复现此前已成功的M12结果；修复版数学运算未变且不再依赖周期GC。

## 10. 实际Jacobian控制响应与下一条成功设计

### 10.1 三控制5%步的完整失败记录

`angle-vu035-q085-c6less5-m12` 已自然结束，没有成功：8个因子预算后，
外层rms为`1.70e-2`、BC为`1.09e-4`，求解器要求把873节点加到2419，
超过本次max_nodes=1800。输出中 `solver_success=false`，没有几何audit；
该失败包不用于继续成功分支。过程中的高模支撑m20升至8.68e-5，
多次接受步长缩到1/131072，显示当前离散问题的严重病态。
资源记录为797.5s求解墙钟、峰RSS436328KiB，正常退出码0，
**不是**先前的exit137，也不是不存在性结论。

这次原 `root_triple_core_bvp.py` 同时把数值参考角图从[2,4]改为[2,4,6]。
有限M12下的坐标截断影响尚未被排除，故不能直接把病态解释为真实曲面的
物理折点。后续比较保留原[2,4]参考图。

### 10.2 同一个成功有限BVP的真实切向响应

`strong_control_response.py` 对成功angle/vu35/M12的实际873节点Jacobian
只做一次因子，再求各物理方向的耦合响应。基点暖转换后的scaled collocation
为8.08e-10、BC为3.16e-11。每个方向同时解delta、LB及全部自由核心系数，
其线性方程后向误差均小于8.5e-16；物理参数差分采用h与h/2对照。
额外的actual_q4方向使用固定弧长的解析入口导数，**参考角图不变**。
这只是当前有限BVP的切向计算，不是新的曲面或固定g误差证书。

| 外加方向 | 自然c6的一阶响应 | 为使c6向零5%的切向步 | 预测LB |
|---|---:|---:|---:|
| actual q4 | .06313713444 | +.00030491873 | .09235052 |
| boost_speed | −.00141159607 | −.01363824615 | .09878789 |
| vu | −.00162504842 | −.01184684367 | .10737828 |
| 首下降转角K | −2.49997e-7 | −77.0078（出物理域） | −3.2143（出物理域） |
| 初始加速度k0 | 5.39683e-5 | +.3567223 | .08942863 |

物理方向的c6响应在h/h2下相对差为4.2e-10至4.3e-8。
自由q4确能移动c6，但在这个基点其切向变化会继续缩短已经过短的boost；
vu降低则预测delta下降、LB增长，且给未来较强核心留下较低入口速度。
故先实际尝试vu=.35→.34。没有把任意一条切向外推当作新解。

完整数据为 `2026-11-12-strong-angle-q085-control-response.json`，
伴随resource及事件日志。`strong_free_q4_bvp.py` 也已准备：保持旧参考图，
固定实际q1/c6，放开实际q4，仍只用delta/LB两个物理控制；目前仅语法检查，
尚未用它产生任何已接受新前缀。

### 10.3 vu=.34 的实际改善

新g任务 `2026-11-12-strong-angle-vu034-q085-m12` 成功：883节点、3次
外层迭代、rms `9.95e-7`、BC `2.34e-16`。实际控制
delta=`.16962369592397325`、LB=`.10458773499520523`，自然
c6=`−.00036851572438290764`。与成功vu=.35/M12相比较：

| 有限样本量 | vu=.35 | vu=.34 |
|---|---:|---:|
| 半高 | 1.9081854 | 1.9040866 |
| 最大主曲率样本 | 10.463581 | 9.555060 |
| metric Fourier l1 | 3.0712e-6 | 3.0345e-7 |
| Darboux Fourier l1（默认nodes/midpoints） | 1.0306e-3 | 2.5239e-4 |
| 支撑m20 | 1.3468e-6 | 1.2291e-7 |

这次实算同时降低了高度和boost曲率，且高模响应减小。求解墙钟403.5s，
实测峰RSS329580KiB。它仍未满足课题指标，q=.085的核心相位差下界仅
.16923535；这里也没有闭合或reach声明。

已从此成功包提升至M20/N512，并以883节点、1次外层迭代成功。
保留相同q和未控profile及旧32项有限线性DN接口，delta/LB随新阶数
重新Newton求解，分别只变约3–4e-10，c6变4.1e-11。该过程仍会微调物理g，
因此明确属于设计谱提升，**不称固定g收敛**。M20的metric Fourier l1为
2.4713e-8，κ样本9.55533035、半高1.904086558；半高和曲率的改善没有被
提高谱阶推翻。墙钟325.2s，峰RSS667648KiB（暖转换阶段）。

实际五次区间内双峰审计也已完成：4328径向点×512角点的Darboux l1
为2.40564e-4，最大点在boost的区间内部u≈.2113；actual-vs-PDE二阶差
样本1.64904e-4，最大点在短sync的u≈.7887。κ峰9.55533024与默认audit
一致，二阶误差仍未付清。数据和完整系数前缀均为
`2026-11-12-strong-angle-vu034-q085-m20`。

### 10.4 后端接入与正在进行的下一步

`strong_neck_bvp.py` 现在可选 `direct-block-qr`，复用父会话已在真实
固定g和含几何参数Jacobian上核对的 `root_block_collocation.py`。
每批fun_jac结束显式回收废弃Flow循环，并在刷新因子前释放旧QR树。
默认sparse-LU没有改动。旧包装器SHA `7f5e0940...` 的确切源码已存
`2026-11-12-strong-driver-before-direct-block.py.gz`，供vu034两份成功包
及其它先前运行按开始时源码重放。

真Jac响应工具还增加了固定旧参考图、固定数值gauge的actual_q1解析
入口方向，以及给定新q1/目标c6时的q1/q4联合切向预测；这两个新增入口
尚未用于新的数值报告。旧五方向报告的确切源码存
`2026-11-12-strong-angle-q085-control-response-driver-at-start.py.gz`，
解压SHA为 `2c276a348be75236922c77ddc7a063d2875ad2d01636253463626404e68e869c`。
保存该快照时一度遇到共享overlay空间不足，之后按旧SHA精确恢复；已完成
的44份JSON和21份gzip全部解析/CRC核对通过，没有已保存数值包截断。

本节记录时的唯一strong大作业是 `2026-11-12-strong-angle-vu032-q085-m20`：
从上述成功M20包真正把vu由.34改为.32，只解delta/LB，保持q、q4和旧
参考图，使用直接块及每批Flow GC。首因子实测峰RSS276424KiB，首次
线搜索α=.25通过；此后已在10.7所述终态成功。按父会话资源安排先让
尾响应、再真实耦合独占恢复，之后继续强q和核心形状。

### 10.5 三点真Jacobian的纯Flow缓存修复

直接块装配按径向点分批调用双控制 `fun_jac`。旧函数完成两次物理参数
中心差分后调用 `self.flow(p[0])`，会重建原基点Flow；这丢弃了先前已经
生成的完全相同Fourier稀疏表。下一批再次为相同基重建表。

`strong_flow_cache_check.py` 仅从成功vu034/M20的真实warm中选三个径向
状态，不建立全局Jacobian、不运行Newton。候选仅把函数最后一行改成
恢复函数开头已经选定的原 `f` 和键 `(float(p[0]),float(p[1]))`；之前的
所有状态导数、参数中心差分和返回算术逐字保留。原实现和候选各连续
求值两次：四份state-J和parameter-J均 `np.array_equal`，最大差为0。
原实现两次各构造一次表，候选第一次一次、第二次零次，且保留同Flow
和同表对象。首次诊断第二调用CPU从.4997s降到.1580s；安装后再次核对，
第二调用CPU从.3688s降到.1605s，峰RSS126308KiB。墙钟受共享调度影响，
这只是三点诊断，不冒称完整Jacobian加速倍数。

该替换已装入 `strong_neck_bvp.py` 的动态源码适配，精确文本仍记录在
每次输出的transforms中；不修改父会话根BVP源码、方程、离散域或接受
准则。旧适配器源码另存 `2026-11-12-strong-driver-before-flow-cache.py.gz`，
解压SHA256为 `2159142e8fa3288990312bf96bafaeac6e1e6d88f896bb3fbc4feadee6218305`。
结果为 `2026-11-12-strong-flow-cache-three-point.json` 和
`2026-11-12-strong-flow-cache-three-point-installed.json`；两份伴随inspection
summary的有意RuntimeError表示诊断结束，不是新的BVP失败。

当时正在运行的vu032已加载旧源码，未被热修改；前三步分别接受
alpha=.25,.5,.5，scaled collocation残差约.03842→.02835→.01395→.00716。
尚无最终解，该缓存修复用于后续新运行。

### 10.6 FreeQ4入口与恢复身份的小检查

`strong_free_q4_bvp.py` 已加独立raw恢复身份，包含外部规定的实际q1/c6，
避免相同p布局/物理profile/参考图而不同c6的原始数值包被错误恢复。
free-q4布局和规定核心系数也在audit之前写入物理检查点。

`strong_free_q4_check.py` 只执行真实adapter的warm构造及入口检查，不建立
全局Jacobian或求BVP：M12/N256、28点warm、q1=.085，规定c6为
`-.0003500899774354651`。参考图仍为原 `[.085,-.006010407640085654]`，
p2确实控制实际q4，p3控制实际c8；解析入口导数对h/h2中心差分的最大
差为`1.974e-11`，warm入口残差0，峰RSS102280KiB。报告为
`2026-11-12-strong-free-q4-inlet-check.json`。这验证了接口和导数，尚未
产生任何新的FreeQ4非线性成功解。

### 10.7 vu=.32 的正式成功终包

`2026-11-12-strong-angle-vu032-q085-m20` 已完整保存并正常exit0：
M20/N512、883→889节点、2轮外层迭代、rms `9.95e-7`、BC `3.49e-15`。
第一轮接受24步（4个真实Jacobian）后只需新增6个径向点，第二轮一个
新Jacobian、一整步把scaled collocation降到`8.17e-13`。物理控制为
delta=`.15764858379009572`、LB=`.12244806104956663`，仍固定q=.085、
旧q4律和原32项有限线性DN。

| 两个独立的新g设计，均M20/N512 | vu=.34 | vu=.32 |
|---|---:|---:|
| 自然c6 | -.000368515766 | -.000337550182 |
| 最大主曲率默认样本 | 9.55533035 | 8.47814516 |
| 半高默认样本 | 1.904086558 | 1.904523716 |
| metric Fourier l1 | 2.47132e-8 | 1.06685e-7 |
| 默认Darboux Fourier l1 | 2.28697e-4 | 3.33833e-4 |
| 端口H系数最大值 | 2.12449e-5 | 2.16679e-5 |

曲率样本降低约11.3%，半高几乎不变；离散误差并未同步改善。完整五次
区间内部双峰审计尚待独占窗口，不能把默认节点/中点的Darboux值当成
连续二阶上界。高模支撑也有改变，例如c14由原负支变成`1.15939e-5`。

`phase_pi_over_base_mode_support_gap_lower=.16924470154216148` 是
**核心支撑函数的相位差下界**，不是整面held数、更不是held/D。此结果
仍是带边有限线性-DN前缀，未完成闭合、reach或固定g的收敛要求。

求解墙钟2571.7s，资源包装器墙钟2579.3s，user+sys约443.2s，峰RSS
289764KiB。使用的适配器运行时SHA仍为 `2159142e8fa3...`（即
`2026-11-12-strong-driver-before-flow-cache.py.gz`），没有热装后来的缓存。
成功包、summary、2.53MB压缩coeff块、resource和压缩Newton日志均已保存；
JSON解析和gzip CRC通过。已释放大作业窗口给tail，再由父会话运行实际
耦合；未在此阶段收尾。

### 10.8 默认关闭的有界几何Flow缓存

`--geometric-flow-cache-size 8` 仅复用完全相同的实际Flow对象，默认0关闭。
键覆盖全部physical cfg和port、构造标量/关键字、bridge对象身份、实际
参考系数/频率、数值径向参考结点以及class工厂的live chart字典。
完整profile和chart变更会失配；不可序列化物理字段绕过缓存。

`strong_flow_lru_check.py` 在三点实际M20/N512状态上核对基点及四种变更：
cfg/start_acceleration、gauge q、参考角图系数、数值meridian结点。
原构造器与缓存构造器的J/PJ全部逐字相等、最大差0；每个变更确实触发
5次新构造。正式CLI开关亦已走同一检查。首次诊断重复调用CPU
`.18317→.04189s`，正式开关复核`.17851→.04884s`。这些仅是三点计时，
不能冒充整Jacobian加速比例。

5个常驻Flow在首次诊断约多11.6MiB RSS；跨四类变更、最多8项且持续
淘汰时，整个诊断峰172868KiB（正式开关172776KiB），原基点约126MB。
更高M/N的存储代价须重测。缓存次数和helper SHA写入每次输出。
程序/数据为 `strong_flow_lru.py`、`strong_flow_lru_check.py` 和
`2026-11-12-strong-flow-lru-three-point[-installed].json`。

### 10.9 同旧参考图的三控制入口

`strong_triple_same_chart_bvp.py` 保留原三控制delta/LB/boost_speed、实际
规定q/q4/c6及全部物理方程/边界/接受准则，将数值参考图单独保留为
旧成功包的[2,4]两项。它不把规定的c6塞进参考图；实际入口仍由完整
PlanarSupportCore生成。比值1的warm缩放不再构造无用的全域几何，非平凡
缩放逐24点处理；raw恢复身份包括实际规定系数，初猜仍经明确物理拉回。

`2026-11-12-strong-triple-same-chart-inlet-check.json` 检查了vu032成功包的
M12小warm，规定c6为原值的.95。实际Flow的参考系数/频率为旧两项[2,4]，
实际core前三项等于q/q4/c6目标。三个物理参数Jacobian对独立h/h2中心
差分的规范误差最大为`2.47e-8`（boost_speed仅`1.67e-9`）；自由c8入口
导数差最大`1.70e-11`，warm入口残差0，峰RSS107336KiB。未做全局Jacobian
或三控制Newton，故没有新三控制成功声明，也没有据此断言旧失败只由图造成。

### 10.10 q=.09 的有限内存warm与明确待运行命令

标准双控制amplitude warm中的全域 `f.geo(s,N)` 也已在strong动态适配中
改为24点批次，比值1时跳过原本恒等的缩放。`strong_warm_scaling_check.py`
实际构造q=.09/M20、28点warm（角数1312）后，比较原全域仿射式与分批式：
最大差`2.55e-18`，属于归约顺序舍入；不是逐字相等。它只影响初猜计算
存储，后续方程、容差和接受条件不变。峰RSS126348KiB；没有运行q=.09
的BVP，检查报告 `2026-11-12-strong-q090-warm-batch-check.json`。

`2026-11-12-strong-planned-continuations.json` 保存三个具体且尚未执行的
命令、成功基点哈希和设计输入哈希：vu032下q=.09；vu032/q085下
boost_speed=.85；同旧参考图的c6减5%三控制备选。前两条仍是下一实际
设计方向，第三条没有替换它们。所有命令显式启用已核对的8项Flow缓存和
直接块、从真实成功vu032包开始；等待父会话tail→exact独占窗口结束后
才可启动。它们都是新g设计，不能称同g加密。

## 11. 较大切口/帽的静态候选

按父会话建议，仅使用成功frozen_profile比较rCut=.30/.45/.55/.65/.75和
loop半径rCut+.05。真实loop_ratio是1.1；增切口降低背景半高，但完整
前缀/bridge的球包络反而增大，最大点在末个loop turn。固定loop coast
径向跨度.035比固定ratio更有利，rCut=.55/.65给出cuff=.30/.40、背景
球包络约3.912/3.948。它们的主要潜在收益是固定帽空间和尾容量，不是
已证实的D改善。详细公式、完整表和未支付的新tail/cap高度见
`2026-11-12-strong-larger-cut-static.md` 及同名JSON。

## 12. 实际尾高度已有反射，撤回额外相位建议

联解 `tail_height` 实际为 `bridge.sigma*q*y[iz:]`，当前 sigma=−1，
WeightedTailPort原样发送该完整向量。此前聊天直接比较前缀q*y与负H₂
尾射线，漏了已有反射；由此提出的π/2 warm转换建议现明确撤回。
恢复first675 q085与angle vu032的真实尾H₂均负，分别−2.280325087e−5、
−2.166791494e−5；与旧q040/M14 warm的H₂同号，无需额外相位变换。
其H₄分别正1.584103904e−8、1.390639588e−8，与旧warm负H₄不同，
仍必须由完整边界初值修正和真实非线性求解处理。小工具仅读保存包并
直接执行原联解函数，没有新尾求解或变换包；完整核对见
`2026-11-12-strong-tail-height-convention.md`及同名JSON。

## 13. vu032 的小样本曲率定位

为等待串行尾/actual窗口时判断下一设计方向，只读vu032成功五次场，
在boost和first descending turn合计70个径向点、512个角点评估真实
Cartesian主曲率；batch4、无Jacobian/worker/新Newton。
`strong_sparse_curvature_budget.py` 与
`2026-11-12-strong-vu032-sparse-curvature.json`保留所有小样本。

| 部位 | 本次实际κ最大样本 | 对应背景子午曲率 | s | 段内u |
|---|---:|---:|---:|---:|
| boost | 8.47497966 | 6.45711974 | .9382162020 | .92 |
| first descending turn | 8.04358001 | 6.75 | .9792339448 | .08 |

所以在这两段的采样范围内boost仍较紧，虽已接近而不是远高于first turn。
背景曲率次序与实际曲率次序不同，不能只优化背景K。此前默认更密采样的
全局值为8.47814516；本次稀疏值不取代它，更不能取代待做的五次区间
内部双峰审计。峰RSS78304KiB、资源墙钟9.46s、exit0，已完全退出，
未占用下一大BVP窗口。

## 14. 大跨步warm的凸性诊断，不是强分支障碍

`strong_core_warm_domain.py` 仅把vu032保存core代入现有amplitude warm的
外推公式：q1/q4线性缩放，第j项（j≥3）按q比值的ceil(j/2)次幂缩放。
利用 `rho=1−sum((4j²−1)c_j T_j(cos2phi))` 的浮点Chebyshev临界点求最小值，
q=.09得到rho_min≈.7899403，入口core这一必要条件仍有余量。完整20项
相同外推首次检测到rho=0约在q=.23981368；只保留前三项的另一个假想
外推约在q=.37395080过零。后一个删除高模的对象也不是已解场。

这说明不能把当前完整系数按旧warm幂律一次放大到q≈.4；其中高阶微小
系数会被幂律严重放大。真正的延拓会重新求所有自由系数与几何，故这些
数值既不是强幅度不可行证明，也不是新g结果。它们支持先做q=.09的小步，
并继续准备同图c6控制。完整输入/hash/表在
`2026-11-12-strong-core-warm-domain.json`，没有新BVP或Jacobian。

## 15. 随q增长控制c6的具体主线

父会话已采用先真实q=.09、再按实际c6/κ/height决定同图三控制的路线，
不从旧vu=.35/M12局部Jacobian大跳。旧导数若硬外推到当前c6=0，需
Δvp≈−.239或Δq4≈+.00535，远超局部可信范围；更直接的目标是随q上升
先保持c6在约−3.4e−4的管道内。

另得到一条完整20谐波静态核心预算路径：q升到.402，q4沿原线性律，
频率6以上保持当前实际保存值。有理不等式给端点全角rho>.1216561145、
轴向相位见证d=.8032910944、未来距离直径预算5d=4.0164554721，R7入口
积<.947932801；rho下界比.03×5d多.00116245。它是明确的平面核心族，
不是解族；真实BVP仍会重求高模，不能套用这些预算验收曲面。

控制矩阵、连续核心不等式、条件性的q090 c6-held/q100/free-q4命令及
严格局部/外推区分见`2026-11-12-strong-controlled-amplitude-path.md`、
`2026-11-12-strong-control-path-budget.json`和
`2026-11-12-strong-controlled-continuations.json`。程序为
`strong_control_path_budget.py`。没有提前启动调度中的q090。

## 16. actual嵌套加载链的prefix缓存核对

`strong_actual_cache_check.py`通过真实root_actual_bounded入口建立
Actual(Base)，只在28点warm的3个径向点重复prefix J/PJ。cache8确实
经actual.module=adapter.module装上，4miss→4hit，两次J/PJ逐字相同、
最大差0；ensure_tail硬guard调用0次，tail始终None，没有worker/BVP。
峰RSS110868KiB。结果为`2026-11-12-strong-actual-cache-check.json`及
对应inspection-summary；故意的inspection-complete异常不是非线性
失败。父会话入口不需修补，可在下一真实actual作业显式启用8项缓存。

## 17. q090实际延拓完整成功

父会话已完成前置独占作业并放行，本分支于UTC约05:34启动
`2026-11-12-strong-angle-vu032-q090-m20`：从正式vu032/q085包保留889节点，
q=.09、原q4律、M20/N512/tol1e−6、max2000、直接块、cache8，完整重求
delta/LB与自由core。运行状态见`2026-11-12-strong-q090-run-state.json`。
初始scaled collocation约.06767，首全步被merit拒绝、半步接受，随后连续
全步收敛。889→891节点、2轮外层、rms9.97e−7、BC4.23e−16；默认audit
完整结束并exit0。raw数组和物理五次包在audit前已保存；物理metadata
SHA为`9959985ea96ca1df3fe8b77139fb202aefd0c0b6fa0fcd2f9378830629bc46cf`。

| 两个独立新g设计，均M20/N512 | q=.085 | q=.09 |
|---|---:|---:|
| delta | .15764858379009572 | .1588987202722233 |
| LB | .12244806104956663 | .12169993773275324 |
| 自然c6 | −.00033755018199025175 | −.0003767998246403099 |
| 默认实际κ样本 | 8.4781451628 | 8.6888114782 |
| 默认半高样本 | 1.9045237160 | 1.9093052655 |
| metric Fourier l1 | 1.06685e−7 | 1.37903e−7 |
| 默认Darboux Fourier l1 | 3.33833e−4 | 1.66985e−4 |
| 核心相位支撑差下界 | .1692447015 | .1791503069 |

真实沿原q4律的有限步割线为dc6/dq=−.0078499285300、d(delta)/dq=.25002730、
d(LB)/dq=−.14962466；这不是无穷小导数，也没有混入vp变化。完整系数
割线与资源/文件hash清单在`2026-11-12-strong-q085-q090-secant.json`。
c6确实往更负方向漂，且κ/半高均增加，为下一次c6管道校正提供了实际
依据。q090的入口二阶误差样本1.449e−6，完整内部双峰/谱精化仍未做。

求解墙钟185.36s、包装器186.84s、CPU143.59s、峰330744KiB；cache8共
884hit/36miss、最多8项、28次淘汰。单QR约1.1s，不将不同物理任务的总
时间比冒充缓存单独加速比。全部gzip CRC、物理coeff哈希和<5MB文件
限制已核对。终态已立即通知父会话与tail，窗口交tail M32同H，本分支
只整理小数据，不自行串联下一BVP。

## 18. q090轻云与boost定位

父会话要求的原root_prefix_geometry轻云radial241/angular128/phases1已
完成；同网格angle vu032/q085也独立读取。D样本分别为q085
3.866429792543022、q090 3.8757880749110063。配合原实际二阶κ样本，
κD为32.7801530431→33.6759919124，q090已超过局部筛查值100/3；相应
1/(κD)=.0296947452。原first675/q085不同g的旧密云κD为33.0155991190。
这是无连续采样误差的设计筛查，不是reach证明或不可能性结论。

q090另用70×512点小诊断确认boostκ8.68554269、first-turn8.12701140，
紧处仍在boost。两个轻云峰约109MB，小定位峰78440KiB，均正常退出。
完整对照与下一次评价要求见
`2026-11-12-strong-q090-geometry-and-triple-readiness.md`及对应JSON。

## 19. 同图q090 c6-held终态为未收敛

tail M32正式完成并退出后，于UTC约05:59从正式成功q090包开始新g试算：
指定q=.09、原q4律、c6=−.00033755018199025175，三物理未知为delta/LB/
boost_speed，保留q090原[2,4]数值参考图。M20/N512/tol1e−6/max2000、
直接块QR/cache8和原有限线性尾端口均按计划执行。

运行正常退出（工具和子进程均exit0），但solver_success=false。891节点
上的8次新Jacobian/8次更新后，scaled collocation残差仍为.0063476674，
边界残差8.59356e−6；最小接受步为1/1024。Newton因子预算耗尽，外层
第一轮RMS残差.0070514323（最坏在入口），拟增1466节点使总数超过
max2000，正式报“maximum number of mesh nodes”。这不是OOM，也不是
已证明的物理折点；当前记录没有测量Jacobian条件数。不可将末态高阶
缩放参数很大直接等同于条件数或物理解发散。

raw与物理五次失败包都完整落盘，physical audit=null，未对失败态运行
κD云或将其作为成功设计。最终δ=.1622394545894、LB=.1301054197138、
vp=.857640708365仅描述失败迭代，不可用来替代成功g。完整gzip CRC、
raw与coeff哈希、<5MB限制已核对；Newton日志压缩保存，执行314.03s、
峰339928KiB。详细执行证据和文件清单在
`2026-11-12-strong-q090-c6held-failure.json`；run-state与控制plan均已更新。
工具session68623已实际poll得到exit0，窗口交root使用成功vu032/q085
开展真实尾耦合。本分支只准备来自成功q090的更小控制步与当前响应，
没有从失败三控制包继续或并起新大型求解。
