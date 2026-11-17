# HANDOFF — Astra-held10-7322d0de-20261118

维护会话：**Astra-held10-7322d0de-20261118**（AI）。前会话 Astra-held10-f00f08c9-20261117。**进行中，尚无满足全部完成标准的候选。** 已登记结论不重做；完整历史、失败和命令见 results、notes、log。

## 目标与同步规则

连通闭曲面连续 C² 嵌入族；固定有内点闭 H、diamH≥.2D；整像 δhold≥.1D，含全部反射取商 δE>0，全时 reach≥.03D。一个固定 g/物理参数/时间范围，metric≤1e−6，空间/频率/时间加密下降至求解/机器地板；材料位移、solver success 或条件窗口不替代全验收。

- 已部分克隆、实际 pull，全文读根 README 授权及全部规则、本题 README/旧交接/全部记录。
- 已读规则提交：`63f61bd14b821137dce0c43cb892f8194458da78`。2026-11-18 04:51:47（UTC+8）独立稀疏发布worktree真实pull后双README无变化；至少每小时pull，变化只读diff并立即执行。
- 每条结论更新本文件并发布。ref 拒绝即真实 pull --rebase 后非 force 重发至成功。终端无可用认证，按根8用已连接 GitHub 小文本原子提交；终端真实 pull 仍照常。
- 可再生 mesh/场/检查点/逐盒表不入 Git、Release、CI artifact；只留源、参数、命令、hash、紧凑标量。单文件<100KB、本文件<10KB。无根 LOG。达到标准后继续扩大比例。
- agent 只在原 worktree 写源，主会话独占独立 publication worktree 的 Git。旧 scratch 只读；数值运行副本独立，避免执行中改源。

## 1. n4：实际尾、低 eta 增幅与圆化

**实际联合锚点**：eta1/q001/M12见n4-first-true-coupled-state；eta.1/q.01/M16在724点完整接受，实际g为δ=.030027177128250468/vd=.2483630655929876，见n4-eta010-true-coupled-state。新精化均从后者出发，仍lambda0/未闭合。

原非周期q01在.2H后工程中断；周期版本重新完成全部联立。R30证明N512/spacing4的128独立标量行与原有限求积恒等，全部D/S/A/root/2e−9门保留；空间点不得周期复制。

**actual g 的M20已接受**：完整g/port冻结，1913点/RMS9.99605e−9，prefix metric2.38461e−8→1.950429e−9/tensor1.62251e−5→3.51076e−6；4次真尾最终res1.66494e−9/minA.942545/metric2.27685e−12/fullD8.96381e−8，mean两jet5.95e−14/−7.11e−13。见n4-actual-fixed-m20。现同g M24/1536/N512/tol1e−8继续，三jet/全图初值≤2.09e−15，旧1913点全留；不借线性g结果。

**原 w.08 增幅**：eta.1/λ0 的 q.01/M16、q.0125/M16、q.015/M20 原 BVP 接受；最后784点 metric9.23853e−7/tensor3.64609e−4/K6.99816/rootmin.00229460。δ/vd随 q 重解，仍线性 port，非同g。q.02大跳与重复 q.0175/M20 明确取消，不是数学失败。q.0175/M24 的初始 rho 守卫曾因系数区间过宽拒绝；同一 Gram 的 Taylor100→180使逆误差由10326.78降至1.90e−40，原门下界.736211。未改核心或放门，M24 实际 BVP 继续。见 n4-eta010-amplitude、n4-m24-coefficient-certificate。

**线性g固定精化**：原w.08/q.01冻结δ/vd，M16→20/tol1e−8到1920点，metric2.38461e−8→1.95003e−9，tensor1.62253e−5→3.51078e−6；见n4-fixed-metric-refinement。最终API从已求参数/原投影重建核心、归一后合并物理网格。true q001/M12→16身份检查三jet≤9.44e−16、全图≤1.83e−15、993旧点全保留；见n4-fixed-seed-identity。已执行旧源另存。

**新 wCut=.16**：原 worker 重建24模 port 和双根，背景 min(1−a′²)=.01602343；新整g的 eta.1/λ0/q.01、.0125/M16 接受731/748点，metric2.48504e−8/5.97569e−7，tensor1.32802e−5/2.12364e−4，rootmin.01563/.01530。见 n4-thicker-cut-prefix-states。q.015/M20随后原BVP接受867点，但完整metric1.20586e−5/tensor.0232143未过，rootmin.001623；见 n4-thicker-cut-q015-full-metric。冻结该g/M20/tol1e−8后2484点，metric1.20598e−5/tensor.0232092几乎不变，单独径向精化未解；见n4-w016-q015-radial-plateau。现同g/M24/tol1e−8，tight原Gram系数证明及原门，运行q015-fixed-m24。圆化优先q0125接受态，从λ.001完整材料链起。新C²网格插值rho下界保留原两界/阈值/32768上限，λ.005同核心由原拒绝变为2048点下界.26731；只过初猜守卫，见n4-circle-second-order-rho-bound。所有新δ/vd仍新设计。

**n4条件窗/旧失败**：R19/19A已证中心对称整像下界、公共H及四重核心+二重帽。eta1/q.02/.022条件held比>.104902/.115401；eta.1/q.049条件>.103812，零控制rho>.234093。实际lambda1/闭合未付；见n4-large-radius-circle-core、n4-large-radius-eta-selection。低幅q001直接lambda.1/材料lambda.15虽BVP接受但metric失败，lambda.2/.175节点门失败；精确lift保留，非入口投影缺失或不存在，见n4-low-amplitude-circle-terminal。

## 2. m3：高幅真正联合与三重圆弧入口

**R32严格条件窗**：n3/eta0、a=.21/b=.08，q∈[.0849,.0851]、固定相位.7046及H角[.3521,.3525]，完整支撑控制在保护域恒0且||b+b″||∞≤.08时，核心rho>.219613、|平面m3|>.0200361。两柱长.54/.5401可选出|活动矩|>1e−6，须用实际图决定；三重帽排全部O(3)。若完整未标记图D≤2.6498/支撑≥.0801/K≤12.5等，则held/D>.1045139、reach/D>.03018。δ∈[.056,.07]初负K窗已付。实际λ1/完整图/全g精化未付，不能用旧R31代替。

**beta4.625/q.040完整真联合**：936点，δ=.061051601505166045；prefix metric6.91e−9/tensor2.34148e−4/K8.71925/物理BC9.05e−10；tail res1.37680e−9/minA.742322/metric5.98745e−10/fullD4.11830e−6，4次tail和audit原门均过。q.060首warmup原线搜索失败res3.67146e−9，无新prefix；见m3-beta4625-*。这两批是新g。

**n3实际圆化**：积分core/单次完整lift/自由c6/锁主频入口已接通；lambda0三jet≤3.44e−13，初始.02/.002原门失败见m3-exact-round-core-start。高矩canonical路径旧c的15宽度峰值最低79.163，见m3-complete-compact-control-width-screen。lambda.0002/parts8尾门失败后parts16有限真联合接受：936点、δ=.06104444009746941、tail res6.88357e−10；但prefix metric3.97036e−4/tensor.364761、mean seam一阶−9.83e−6，未过完整门，见m3-round-lambda0002-finite-acceptance-metric-gap。现从原好锚点走raw低2×2投影新路径lambda.02；改变途中高矩，lambda1全free空间相同，非同g精化。

beta4.125的q.02/.025/.03/.04均完整接受，q04 tail res8.02413e−10/minA.617549；见m3-beta4125-*。q03 minA在stage40首谷、最大残差stage43，ULP解释不放门。新beta4.625/q04旧prefix最小root在s=.99473后桥、a′=−.997961，远过lift终点.38666；见m3-prefix-positive-root-bottleneck，不当作失败迭代位置。

beta3.625/q.0225接受，q025三条原门失败；见m3-beta3625-*。旧跨beta/ULP诊断见tail-residual-and-positivity-locations，均非不存在。

原gδ=.06105607686781097的q02/M16/parts8、prefix983→2462均原门接受，metric5.845e−11/tensor1.947e−6；闭图见§3。旧q025接受、q026/.0275七条失败详m3-true-radial-refinement与m3-finite-continuation-initializers，不重跑。

## 3. 已完成的低幅全闭图和全域连续 metric

R21/R23已定义原有限C²闭图和全mean接缝，R24固定帽排全部O(3)。R28新M16/64图用自身1261568盒、尾界及体积矩，D≤2.301491469394、reach≥.1、H径比>.6979428、held/D>.00546265624、δE>0，不搬M8矩。

同checkpoint尾32→64步真实R处metric1.8282e−9→1.4441e−10；整图采样最大仅至1.6485e−9，prefix主导。两层尾二阶差仍.00629485，未证C²极限；每层重做cut/mean，不是差分步造成的主要误差。

R27已严格区分原背景真积分与工厂偏差；R29尾连续operator界9.996590773606874e−7，R31前缀<8.253e−7。真桥积分/舍入/各层唯一共用atlas全部支付，未改图或逐层换g；C3协变来自精确频率定义，非小DFT残差假设。

**合并圆领/固定帽，同一低幅全闭图全域全时metric<1e−6已经证明。** 上述是充分界，非真实最大误差估计；held仍远小于.1，不能标完成。既有空间/频率/尾径向下降是独立数值证据，没有证明精确无限解。高幅积分core导出接口已保留一次完整reference lift，并用全角Hermite恒等式补中心；非解probe七jet差≤9.41e−15，不认作新解/连续证书。原chunk解码已复核修正，待首个accepted圆化CP端到端检验；见m3-integral-core-export-interface。不重扫低幅盒。

## 4. 其他已登记结论与未付入口

R12/R14接缝结构、R15轴曲率必要界、R16过零权逆障碍、R17对称限制、R18完整混合DAE已证。R20/R22单/双谐波圆弧距离及条件切空间障碍不等于不存在。R25固定Q/g正A凸域动量唯一根不推出shoot存在。R26三谐波有限近弧最优窗缺第三物理核。

旧m2 q20/q22仅线性DN同g精化；R11开放几何held/D>.1076，R13若真实尾/全闭满足完整条件可给held/D>.10338、reach/D>.03191，实际尾未付。m2三谷/六谷/循环11根、n4第三核7次有限搜索均见相应notes；不当容量、同g或不存在，不重跑。

## 当前分工与工作树

m3_true_coupling：n3真实圆化/parts16及原始compact新路径；closed_geometry：积分core接口/连续证明；n4_round_core：q0175/M24、actual q01固定M20、w16 q0125圆化；root：w16 q015固定M24、控制能量基/逐结论同步。

原源树 /workspace/scratch/7322d0dee069/math-research-public；发布树 /workspace/scratch/7322d0dee069/publication。持续按 open.md 推进，不以阶段结果、时长或等待用户回复收尾。
