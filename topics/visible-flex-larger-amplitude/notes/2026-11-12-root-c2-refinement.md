# 2026-11-12：固定g五次C²表示的真实内部误差

visible-larger-20261112。**数值诊断；没有完成强幅闭图。**

## 输入与冻结项

恢复的`2026-11-12-strong-first675-q0775-m20.json.gz`是真有限linear-DN前缀，M20/N512/tol1e−6、859节点。新`root_c2_polished_refinement.py`冻结其物理profile、tail参数/cut、参考材料角图、gauge和总长，全部core系数变为解的未知量。冻结数据逐项SHA256写入输出；实际nonlinear-tail输入被拒绝，防止静默替换边界条件。

该脚本只收紧`root_domain_newton.py`的内部配点停止阈值，最终SciPy网格残差及边界容差仍照指定值。径向独立计算分批，不改角积分或方程。首个运行命令为：

```bash
python -u computations/root_c2_polished_refinement.py \
  --fixed-reference notes/2026-11-12-strong-first675-q0775-m20.json.gz \
  --newton-residual-factor .0001 \
  --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --modes 20 --angular 384 --nodes 0 --tol 1e-6 --max-nodes 2500 \
  --out-prefix notes/2026-11-12-root-q0775-c2-polish
```

**角积分从原N512变为N384，所以这不是单独改变Newton阈值的因果对照。** 物理g相同，但不能把改善全部归给内部阈值。

## 真实保存曲线审计

保存的是物理s上的五次Hermite PPoly。其实际二阶导数是审计对象；点上PDE二阶仅作为对照，不能替换实际导数。每个区间除端点/中点外，加$(3\pm\sqrt3)/6$两点，并有独立均匀径向网格。

| 样本量 | 原恢复解 | 同g polish解 |
|---|---:|---:|
| 径向节点 | 859 | 876 |
| 角求解点数 | 512 | 384 |
| metric Fourier l1 | 2.89893e−8 | 2.89241e−8 |
| 全内部Darboux Fourier l1 | 1.81835e−4 | 6.70020e−5 |
| 实际二阶与PDE二阶最大差 | 1.66470e−4 | 8.25442e−5 |
| κ最大样本 | 约8.2224 | 8.222387829 |

原nodes/mid审计仅给Darboux3.31849e−5，确实漏掉内部峰。polish仍有明显峰，主要在短descending-speed-sync段。输出`...-interior.json`记录完整定位；所有数值为有限样本，不是连续上界或完整曲面的reach。

## 不支持“Newton过早停止是主因”

`root_collocation_lobe_diagnostic.py`按**记录的求解角点数**重建实际数值坐标t内的三次配点中值

$$y_m=(y_i+y_{i+1})/2-h(f_{i+1}-f_i)/8,$$

以及真实Simpson配点残差

$$e=y_{i+1}-y_i-h(f_i+4f_m+f_{i+1})/6.$$

物理s到数值t的逆先用Newton修正，避免小区间内逆图误差被$h_s^{-2}$放大。仅由端点位置误差$e$引出的五次修正$e(10u^3-15u^4+6u^5)$，二阶峰精确系数为$(10/\sqrt3)|e|/h_s^2$。这是**单一分量的诊断尺度**，不控制所有插值误差。

原N512解最大相对配点残差6.41316e−12，最坏孤立修正二阶尺度7.39474e−8；polish N384解对应4.48347e−12、3.45105e−8。原配点系统已非常准确，这个尺度比1e−4实际峰小约三阶；现有证据不支持把整峰归因Newton早停。后续应针对径向离散和物理五次插值收敛，而不是只反复压Newton阈值。

## 真降径向容差的执行终止

以polish为restart，保持相同g/M20/N384，tol改1e−7、max-nodes4500、Newton factor1e−4；命令其余同上，输出前缀`2026-11-12-root-q0775-fixed-tol7`。工具报告exit137，日志只有876节点start和首轮表头，没有已接受解、误差或首轮终态。只保存冻结profile和这份失败说明，不编造计算结果，不据此判方程不可解。

当前实际下一步是相邻径向块的平衡QR线性解法，先用真实Jacobian检验其与原Newton系统一致，再定向细分短sync或降低tol。这个修改只换线性代数，不放宽方程、边界条件或验收。


## 修复闭包后的局部QR仍需降低存储

`strong_block_qr.py`已消除递归局部函数对CSR/Jacobian及RHS/答案数组的自引用保留；真实M12 Jacobian的解逐值不变。第一次旧QR作业随观测峰602→767→947MB被主动中断（exit130），不能记作自动内存终止。

第二次从原成功q0775恢复，仅降低径向tol到1e−7：M20/N512、Newton factor1、max2500、修复后的QR。859节点配点达到6.30754e−13；外层最大残差1.36e−6，增至1484。1484节点配点5.59942e−13、BC2.59450e−15，外层残差1.99e−7，增至1634。下一次factor完成前子进程被signal9终止；wait4记录峰938148KiB、468.447秒。

完整日志及resource保存为`2026-11-12-root-q0775-fixed-tol7-bounded-*`。**没有最终接受解，不能把中间Newton残差或外层趋势当作tol1e−7通过。** 进一步压缩目标为直接保存相邻块A/B/P和端点BC，消除全局CSC/CSR及双份索引/构造临时数组；保留完全相同的配点方程、实际Jacobian、QR算法和验收。


## 直接块通过求解器，但在后处理前终止

`2026-11-12-root-q0775-fixed-tol7-direct`用同一M20/N512/g、Newton factor1与tol1e−7。相邻块直接装配把859点factor峰降到260392KiB；1484点388492KiB；1634点423096KiB。第三轮日志明确记录Solved/1634节点、max residual9.99e−8、BC2.79e−16。随后在物理PPoly保存或后续审计阶段前被signal9终止，695.004秒。日志没有更细阶段标记，不能确定具体后处理函数；未留下物理系数包，因此不把它记入可复现的已接受C²链。

这同时说明先前的全局矩阵存储问题已在Newton阶段被消除，但整个作业还没有可靠落盘。当前`root_dual_core_bvp.py`新增求解器返回即保存的raw x/y/p/三次配点系数，明确不是物理C²曲面；每个数组分片gzip<5MB并校验SHA。物理PPoly完整包改在audit之前保存，带`audit_pending`；新增`--raw-collocation-restart`与`--postprocess-only`只在物理数据、布局、角图、数值容差完全一致时接受。实际尾类还记录真实coupling上下文，不能当linear-DN包重用。

多个独立进程在约405–550MB时也被signal9终止，尚不能断言单进程上限或具体原因。后续大计算按全组串行，先保住真实接受状态，再完成原验收；不放宽任何方程或容差。当前仍须从上一个完整q0775包重做这一轮。

## 05:32 UTC：tol1e−7 已完整重做并保存

新的输出前缀是 `2026-11-12-root-q0775-fixed-tol7-checkpointed`。仍从原859节点成功包开始，固定原g、M20/N512、完整32模线性端口、gauge、参考材料图和总长，Newton factor1、径向tol1e−7、max2500。完整命令存于对应resource JSON。

真实路径859→1484→1634节点，3轮外层，最大残差9.99e−8、BC2.79215e−16。此次完整进程正常exit0，178.4936秒，峰RSS422684KiB。raw配点状态在求解器返回后立即保存，SHA256为`d1895ca91085f1d922dec1be66a33fe8338bbb50813c1165a4373d29ea5cb1e0`；该包明确标为非物理曲面。随后物理五次包也先于audit保存，最终`audit_pending=false`，物理主包SHA256为`55e74a280f52a9e50e62658d3c7318a9b906dbe3b363bccca4d5a1d8162b81f5`，两个系数块的SHA和大小均在主包内。

在raw落盘后回收已不可达对象及释放分配器空闲页，观测RSS423236→92476KiB；物理插值后audit前169732→97288KiB。它们是这次实际执行的观测，不把之前signal9的具体原因归定为某一个内存机制。

### 不漏内部峰的同g径向对照

完整实际五次审计覆盖7332个径向点、每点512角点，包含每个原区间的两个二阶峰和中点；batch4、17.02秒、峰RSS83756KiB，exit0。

| 量 | 原M20/N512/tol1e−6 | 本次同M/N、tol1e−7 |
|---|---:|---:|
| 节点数 | 859 | 1634 |
| metric Fourier l1 | 2.89893e−8 | 2.8733603632e−8 |
| 全内部Darboux Fourier l1 | 1.81835e−4 | 2.8872794440e−5 |
| 实际二阶与点上PDE二阶最大差 | 1.66470e−4 | 2.6427249428e−5 |
| κ最大样本 | 约8.2224 | 8.2223877637 |

本次默认nodes/mid audit 的Darboux为2.6028438484e−5；内部审计仍需单列。最坏内部Darboux在descending speed sync，物理s=2.2176813726，区间868，宽度0.00016971390394，局部坐标0.7886751346。实际/PDE二阶差峰在同段的另一个内部极值。度量误差几乎未随这一次径向加密变化，不能单凭此一对数据证明某项误差地板，但继续只压Newton阈值没有已见证的收益。

固定物理数据和同材料点/两jet的独立比较由 `root_fixed_linear_chain_audit.py` 完成；它明确拒收实际非线性尾包，防止混淆两种边界问题。连续空间/角域证书、更多固定g精化以及真实非线性闭合仍待完成。

该实际比较现已exit0（120.16秒、峰RSS160820KiB），所有冻结物理数据的规范JSON逐项一致。原859点与新1634点两套网格的全部内部双峰也同时进入比较。同材料点最大位移1.1824942783e−8，径向一阶差4.0639545736e−8，角向一阶差2.3862427018e−8，径向二阶差1.6625477307e−4、混合二阶差5.0988907422e−7、角向二阶差4.1444310505e−7。完整hash与定位见`2026-11-12-root-q0775-fixed-tol7-chain.json`。这只给出有限采样下两条实际表示的差，明显未达到全部两jet的机器一致；不把小点位移冒充C²收敛完成。

### raw 的真实恢复已核验

随后用相同固定g/配置和`--raw-collocation-restart ...checkpointed-raw-collocation.json.gz --postprocess-only`实际重建一次，不运行新Newton。恢复进程正常exit0，82.54秒、峰RSS228604KiB。原包与恢复包的物理系数数组形状均为(6,1633,61)，按uint64位模式比较完全相同；规范profile、端口、gauge、材料角、mesh、参数、完整core和完整默认summary等15项精确比较全部通过。解码后的系数字节SHA256为`c5c9655268394945a54b44b7adfa42e6d424b6fa703573b186a59b952487fb1d`。

完整恢复命令、资源记录与比较步骤在`2026-11-12-root-raw-postprocess-check-resource.json`和`2026-11-12-root-raw-postprocess-check.json`。重复的物理输出是可重生中间文件；正式原物理包及raw包为权威输入。这一步核验了实际恢复能力，不是额外的一次精化或新曲面。

### 固定表示的度量误差谱：下一项优先升M

`root_prefix_metric_spectrum.py`只取已有独立audit的四个最坏径向位置，不重新求解。先按原求解N512计算高度均值的一阶导数并冻结，再在512/1024观察角网上计算同一物理表示的度量误差。FFT标签是计算角eta频率；没有冒充物理theta谱。

在metric l1峰s=.9842367069，E−1的最大成分为eta频率40，成对l1幅1.4693886213e−8；保留带40以上的能量比例约.4176。F/a的主成分为42，成对幅2.8410043839e−9、带外比例约.6729。其他审计峰的E−1也以40为主，不能把它们统称为纯带外误差。

两观察网格的共同角点值逐位相同，所选各分量Fourier l1变化最大2.14834e−15；另外独立重算N1024的均值导数仅差5.55112e−17。结果见`2026-11-12-root-q0775-fixed-tol7-metric-spectrum.json`，最终执行1.53秒、峰85664KiB。它支持在保持g/N512/tol1e−7不变时尝试M20→24，不支持继续盲增角采样；实际是否下降仍由下一次完整求解决定。二阶径向峰仍有独立误差，不能被这个四点频谱诊断代替。
