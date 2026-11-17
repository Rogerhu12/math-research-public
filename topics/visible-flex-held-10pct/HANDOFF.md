# HANDOFF — Astra-held10-7322d0de-20261118

维护会话：**Astra-held10-7322d0de-20261118**（AI）。前会话 Astra-held10-f00f08c9-20261117。**进行中，尚无满足全部完成标准的候选。** 已登记结论不重做；完整历史、失败和命令见 results、notes、log。

## 目标与同步规则

连通闭曲面连续 C² 嵌入族；固定有内点闭 H、diamH≥.2D；整像 δhold≥.1D，含全部反射取商 δE>0，全时 reach≥.03D。一个固定 g/物理参数/时间范围，metric≤1e−6，空间/频率/时间加密下降至求解/机器地板；材料位移、solver success 或条件窗口不替代全验收。

- 已部分克隆、实际 pull，全文读根 README 授权及全部规则、本题 README/旧交接/全部记录。
- 已读规则提交：`b6699f144cb86e4abe10f34af8f15c5a8268d60d`。2026-11-18 04:35:02（UTC+8）发布接口错误后立即真实pull/rebase，双README无变化；至少每小时pull，变化只读diff并立即执行。
- 每条结论更新本文件并发布。ref 拒绝即真实 pull --rebase 后非 force 重发至成功。终端无可用认证，按根8用已连接 GitHub 小文本原子提交；终端真实 pull 仍照常。
- 可再生 mesh/场/检查点/逐盒表不入 Git、Release、CI artifact；只留源、参数、命令、hash、紧凑标量。单文件<100KB、本文件<10KB。无根 LOG。达到标准后继续扩大比例。
- agent 只在原 worktree 写源，主会话独占独立 publication worktree 的 Git。旧 scratch 只读；数值运行副本独立，避免执行中改源。

## 1. n4：实际尾、低 eta 增幅与圆化

**已有真正联立**：eta1/q001/M12 的993点首态见 n4-first-true-coupled-state。新 eta.1/q.01/M16 已完整联立724点，δ=.030027177128250468、vd=.2483630655929876，物理 BC3.48021e−11；5次实际 tail 最终 residual1.60671e−9/minA.942545/metric5.78293e−12/fullD1.49888e−7。prefix metric2.38461e−8、tensor1.62251e−5；mean 两jet差−1.17e−12/2.85e−11、非mean二阶4.77e−8。仍 λ0/未闭合，见 n4-eta010-true-coupled-state。

原非周期 q01 运行接受 .2H 后工程中断、原因未明；周期复用重启重新完成全部联立。R30 证明 N512/spacing4 的128独立标量行与原有限求积恒等，公开 N、D/S/A、root 和最终2e−9门均保留；实际对照/派生源hash已核。禁止把空间点也周期复制。

**真正 actual g 的 M20**：已从上述最终 checkpoint 冻结全部 physical_profile，用最终 build_seed 与原 TailMixin/outer、N512/RK16/parts8/tol1e−8继续。跨 M 仅用原 nested-remesh 初值；fullH warm audit 已过原门，完整 prefix 联立仍运行中。源 refine_actual_tail.py，运行 n4_work/actual-eta010-q010-fixed-m20；不能借线性 g 的精化计分。

**原 w.08 增幅**：eta.1/λ0 的 q.01/M16、q.0125/M16、q.015/M20 原 BVP 接受；最后784点 metric9.23853e−7/tensor3.64609e−4/K6.99816/rootmin.00229460。δ/vd随 q 重解，仍线性 port，非同g。q.02大跳与重复 q.0175/M20 明确取消，不是数学失败。q.0175/M24 的初始 rho 守卫曾因系数区间过宽拒绝；同一 Gram 的 Taylor100→180使逆误差由10326.78降至1.90e−40，原门下界.736211。未改核心或放门，M24 实际 BVP 继续。见 n4-eta010-amplitude、n4-m24-coefficient-certificate。

**线性 g 的固定精化已完成**：原 w.08/q.01 完整 δ/vd 冻结，M16→M20/tol1e−8到1920点，metric2.38461e−8→1.95003e−9，tensor1.62253e−5→3.51078e−6；未知改为 q/c8，全核心低矩或固定 J 嵌入。见 n4-fixed-metric-refinement。已执行旧源独立保留；最终 API 从已求参数及原投影重建核心、归一后合并物理网格。true q001/M12→16 身份检查核心三jet≤9.44e−16、全图≤1.83e−15，993旧点全保留；见 n4-fixed-seed-identity。

**新 wCut=.16**：原 worker 重建24模 port 和双根，背景 min(1−a′²)=.01602343；新整g的 eta.1/λ0/q.01、.0125/M16 接受731/748点，metric2.48504e−8/5.97569e−7，tensor1.32802e−5/2.12364e−4，rootmin.01563/.01530。见 n4-thicker-cut-prefix-states。q.015/M20随后原BVP接受867点，但完整metric1.20586e−5/tensor.0232143未过，rootmin.001623；见 n4-thicker-cut-q015-full-metric。已冻该g做M20/tol1e−8，运行 transfer_work/n4-thicker-cut/q015-fixed-m20。圆化优先q0125接受态，从λ.001完整材料链起。新C²网格插值rho下界保留原两界/阈值/32768上限，λ.005同核心由原拒绝变为2048点下界.26731；只过初猜守卫，见n4-circle-second-order-rho-bound。所有新δ/vd仍新设计。

**条件核心窗口与既有圆化失败**：R19/19A 中心对称整像下界、中央柱公共 H、四重核心配二重帽已证。eta1/q.02/.022在D≤2.65/σ≥.08/K≤12.5等条件下held/D>.104902/.115401；eta.1/q.049零控制rho>.234093、条件held/D>.103812。真实圆心/初负K窗已付，未来补弧控制须重付rho，实际λ1前缀/尾/闭族未付。见 n4-large-radius-circle-core、n4-large-radius-eta-selection。低幅eta1/q001/M8直接至λ.1、完整材料预测至λ.15虽BVP接受但metric均未过，λ.2/.175原节点门失败；精确reference lift一直保留，不是入口丢高频或不存在证明。见 n4-low-amplitude-circle-terminal；旧 bimodal/double-prefix 失败不重做。

## 2. m3：高幅真正联合与三重圆弧入口

**最新 beta4.625/q.040 完整真联合**：δ=.061051601505166045、936点；prefix metric6.90989e−9/tensor2.34148e−4/K8.71925，物理BC9.05047e−10；tail residual1.37679736e−9/minA.742322/metric5.98745e−10/fullD4.11830e−6。4次实际tail及最终audit全部过原门；中间4.8e−9曾继续原Newton到接受，不是放门。首谷变动经全局重标定改变整个r(x)，明确新g。见m3-beta4625-first-coupled-state。q.060首warmup在iteration7因原线搜索失败，res3.67146e−9/minA.529428，未开始prefix联合；见m3-beta4625-q060-original-gate-failure。现转n3/eta0真圆化λ.002，较大λ.02初猜rho负另记。

beta4.125已有 q.02/.025/.03/.04 四个完整态。q04 tail res8.02413e−10/minA.617549/fullD1.00976e−5；prefix metric6.91e−9/tensor2.28e−4。见 m3-beta4125-fourth-coupled-state。q03真实minA在stage40/cell0第一谷，最大残差在stage43且相当于该分量2ULP/原scale；不能据此放门，见 m3-beta4125-leading-valley-location。

beta3.625/q.0225完整接受，q.025原shoot、局部root加严、L2选步三条均未过原2e−9；详 m3-beta3625-*。旧跨beta失败/ULP位置见 tail-residual-and-positivity-locations。所有失败只约束具体有限运行。

**原固定g的已登记层**：δ=.06105607686781097，g SHA11a9…b125。q02 M8→M16/parts8原门接受；M16 tail res1.161e−9/fullD2.735e−7/minA.440917。固定g prefix983→2462点使metric4.971e−9→5.845e−11、tensor9.015e−6→1.947e−6。见 m3-fixed-m16-parts8-and-radial-floor、m3-true-radial-refinement。旧q025已恢复接受res1.857e−9/minA.26267/fullD4.422e−5；q026/q0275的7条有限继续不重跑。

## 3. 已完成的低幅全闭图和全域连续 metric

R21/R23 定义真实有限 C² 闭图、共同 Cartesian 两jet、全mean接缝和圆领。R24非零固定帽排全部O(3)。R28新M16/64步图自身1261568前缀盒、尾界、体积矩与帽给 D≤2.301491469394、reach≥.1、H径比>.6979428、held/D>.00546265624、δE>0；不搬用M8矩。三个惯性根互异及core cos3→sin3排反射。

同checkpoint尾32→64步真实R处metric1.8282e−9→1.4441e−10；整图采样最大仅至1.6485e−9，prefix主导。两层尾二阶差仍.00629485，未证C²极限；每层重做cut/mean，不是差分步造成的主要误差。

R27原背景真积分给λ∈[161.87100490348996,161.8710049035018]；工厂λ严格偏高(2.0236e−11,3.2089e−11)，不能替代真g。R29原有限尾全角/全径向/全相位operator界9.996590773606874e−7；R31原2464前缀跨度完整多项式/Laurent及解析核心四阶Taylor给prefix<8.253e−7。真桥积分、数值舍入与各层唯一共用固定atlas转换均支付，没有改图/逐层换g。R31的C3协变来自精确复平面频率定义，不是小DFT残差假设。

**合并圆领/固定帽，同一低幅全闭图全域全时metric<1e−6已经证明。** 上述是充分界，非真实最大误差估计；held仍远小于.1，不能标完成。既有空间/频率/尾径向下降是独立数值证据，没有证明精确无限解。此接口转用于高幅候选，不重扫低幅盒。

## 4. 其他已登记结论与未付入口

R12/R14接缝结构、R15轴曲率必要界、R16过零权逆障碍、R17对称限制、R18完整混合DAE已证。R20/R22单/双谐波圆弧距离及条件切空间障碍不等于不存在。R25固定Q/g正A凸域动量唯一根不推出shoot存在。R26三谐波有限近弧最优窗缺第三物理核。

旧m2线性DN q20/q22同g精化metric约4.17e−9/1.12e−8。R11开放q20连续盒给held/D>.1076；R13条件真尾rXY≤.35、顶高≤1.526541485、K≤10、σ≥.3及C²闭合可给held/D>.10338、reach/D>.03191，实际尾未付。m2首三谷65次screen是新物理设计，六谷53次未改善；11个循环线性根、n4第三核7个失败搜索均已登记，不能当容量或不存在。相关 mode2/m2-loop/n4-physical-third-mode notes 不重跑。

## 当前分工与工作树

m3_true_coupling：beta4.625/q060失败后n3真正λ-coupler；closed_geometry：R32三重圆弧、控制稳定性、公共H/C3帽的严格条件预算；n4_round_core：原q0175/M24、actual q01固定M20、新w16 q0125材料圆化；root：新w16 q015固定g精化、实际接口/记录、逐结论同步。

原源树 /workspace/scratch/7322d0dee069/math-research-public；发布树 /workspace/scratch/7322d0dee069/publication。持续按 open.md 推进，不以阶段结果、时长或等待用户回复收尾。
