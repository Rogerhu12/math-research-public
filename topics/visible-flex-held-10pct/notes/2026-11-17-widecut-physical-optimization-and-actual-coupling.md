# 宽切口物理重设计及两次实际非线性联立

维护会话：`Astra-held10-f00f08c9-20261117`。物理设计由主会话运行，真实前缀/尾联立由 `true_a_analysis`，所有接受门保留原源码。本笔记只登记有限设计与实际终态；目前没有10%闭族。

## 1. 四个不同的实际物理度量

全部使用原 `closing_weighted_tail_v1` 的双脉冲拓扑、rCut=.35、wCut=.30、width=.25、protectCell=160；新cut上真实重新组装工厂，未把旧DN数组改标签。原八列worker使用512步和far48，M8/depth8、orientation=+1；upper输入完整−H，再反射整个worker z及均值。

初始配置保留旧7个 valleyControls，并没有在新cut校准。其真端口 D1=10.2048675443、背景高.02703723、采样κ7.998893。完整深线性最小gate仅1.81496e−11，瓶颈在深cell7；这只是一个特定线性诊断，不是非线性容量上界。q=.02线性端口prefix虽有metric4.595e−9，实际冷启动λ=.01遇原D/S/A拒绝；另一次从λ1e−5起的冷启动遇原Newton line search失败，两次都没有得到完整真联立。

原不可变 `closing_weighted_hard_gate_opt.mjs` 对7个真实物理控制做438次评估后，选定控制

`[1.90625,1.671875,3.21875,5.03125,5.640625,5.65625,4]`，其余至160项为零。

新线性gate为6.4671578e−5，背景高.02651688；同原worker重新生成全部端口，首模为9.86804231267902。该已选物理参数才用于下面的非线性联立。128步筛选的9.86805974不是512步实际worker使用值。

另一个更高峰/更宽谷候选使用背景曲率10、前三pulseCaps (.7,.15)、(.08,.04)、(.04,.025)，valleyCaps .2/.08/.04。402次同类物理评估后gate只有5.00119e−5、高.04511143，没有优于前一设计；未将它冒充同g加密或非线性失败。四份原始物理配置及精选标量在 `scripts/nonlinear_tail/widecut`；不提交完整优化历史。

## 2. 单独把每圈momentum归零不是充分设计目标

7圈共同物理校准在128步得固定尺度残差8.94e−14，但内传增益约为−.304、−.668、−.685、−.715、−.747、−1.225、−2.807。近端原R_n=2，不能误用深端R64来解释这些数。完整深gate反而降至7.00e−15。

冻结128步根再用512步复算，首圈momentum不再为零（−.00450；固定尺度相对约8.1e−7），增益只改变约5.7e−7；其它圈增益变化更小。弱增益/较差深gate判断稳定，但不把128步根当精确解。在beta∈[−5,25]、步长.5的466次真实组装扫描中只见每圈同一个变号根；这个有限扫描不证明唯一性。完整小表、源码与命令是 `widecut_calibration_compact.json` 及三个calibration/scan脚本。

## 3. 两个通过原接受门的实际前缀—尾解

|项目|固定q≈.001点|新设计q=.002点|
|---|---:|---:|
|完整prefix δ|.1715771558592994|.17157709107394398|
|实际主支持幅度|.0010133858465463923|.002|
|prefix metric|1.05477e−10|2.3900e−9|
|物理非均值BC误差|6.08115e−12|4.43e−15|
|全有限尾minA|.6756653|.3279589|
|全有限尾minD|.99987942|.99976187|
|尾采样形式曲率|7.99891|7.99891|
|尾metric|1.68754e−12|1.2022e−9|
|尾fullD/Gauss诊断|2.97978e−9|2.214e−6|

第一点初次design内层停在rms3.0148e−6；该未接受状态仅用作初值。冻结整个δ/profile后，切回原fixed formulation，以主幅度为未知，在2036节点、原tol1e−6、物理BC2e−9及真实outer门不变的条件下接受。归一化outer BC为2.4832e−9，物理BC为6.0811e−12，不能把两个不同归一化量与同一个阈值比较。

q=.002最初直接跳到最终完整H向量时Newton拒绝。随后同一tail物理g用.51/.65/.8/1的完整向量warm通过，再让prefix δ按原design formulation调整，最终通过。它与前一点的prefix g不同，绝非整个曲面的同g精化。

全均值/非均值高度两jet都记录。q≈.001的mean一/二jet差为4.39e−15/−1.87e−13，非均值为6.08e−12/1.26e−10；q=.002相应约−2.72e−13/5.60e−12和4.43e−15/9.20e−14。Cartesian连续C²拼接仍须另支付，不能直接用这些采样值宣布闭合。

**第二点的尾fullD约2.214e−6、归一缺陷约8.894e−4，明显比第一点差。** 小的C0 metric和原solver success没有解决其C²/Gauss收敛；尚无模式/深度加密、完整闭尾或全时reach证书。所有数值均来自紧凑completed记录，原始summary的hash保持不变。新exporter只在报告层修正旧audit.scope，把affine内层与真实outer/mean检查分开说明。

此前beta8 q=.0006也保留实际终态：内层maxnodes时rms约1.99e−6，尾仍接受、无D/S/A拒绝；这是一次内层分辨率失败，不是幅度上界。该单独g的记录随本包保留。

## 4. 从源重建

在仓库根目录运行：

```bash
python topics/visible-flex-held-10pct/scripts/nonlinear_tail/widecut/prepare_widecut_runtime.py \
  --repo "$PWD" --dest /absolute/scratch/widecut-replay
```

准备器恢复既有71文件闭包和原优化器这1个新增不可变源，逐个核SHA，再真实启动原worker，重建八列DN与linear chart。主会话已在空目录独立运行，得到与历史实际消费文件逐字相同的canonical port SHA `6069af3af1ac6656bfcc32768823f65d58588ddcb1473ed994e7ba9975a75704`，全部8列、cut和物理参数相同；固定profile SHA也相同。

生成的 `widecut-preparation.json` 列出seed、design、fixed重试、q002新design的完整命令，分别执行并把log和状态留在scratch。固定重试使用发布的固定profile，未把机器上重算出来的另一个δ悄悄称为同g。历史尾response编号随Newton调用次数可能变化；若重算调用数不同，必须显式选取其最后一份完整已收敛尾state并更新initialCheckpoint，不能使用失败state。源日志、实际原argv、明确的等价命令及输入/输出hash均保留在本目录紧凑记录中。

要重跑原物理优化器，先设置 `CLOSING_TAIL_CACHE` 为恢复source下的 `repro/source-root/topics/large-amplitude-twist-flex/scripts`，再执行原 `scripts/closing_weighted_hard_gate_opt.mjs`，参数依次为配置、scratch输出、`2 128 48 7`。优化过程改变物理g，完整历史只在scratch生成。不得把优化得到的新g之间的误差变化当同g加密。
