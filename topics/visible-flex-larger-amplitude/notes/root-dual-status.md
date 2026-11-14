# 双控制前缀：实际求解与未付缺口

2026-11-10，visible-larger-astra-20261110。全部是数值证据，不是闭曲面。

## 一般角图与真正 warm continuation

`root_dual_core_bvp.py` 固定主支撑系数 q 和指定 cos4 系数，以 δ、vd 作为两个物理设计控制，其余核心谱随边值方程求出。实际状态 Jacobian 对 complex-step 的相对差约1.42e−15。R5 的坐标转换先保留旧物理像及高度均值，再明确作初猜振幅缩放和入口修正；后者不是等距变换。新解的高度均值由新速度重新积分。

线性比例 q4=−q/(10√2) 的真实有限 linear-DN 分支：

| q | M | 实际 BVP | metric采样上界量 | vd | δ |
|---|---|---|---|---|---|
| .002 | 4 | 成功 | 1.51e−6 | .446303261 | .158502792 |
| .006 | 8 | 成功 | 8.07e−7 | .446203220 | .158551366 |
| .012 | 12 | 成功 | 3.11e−6 | .446014949 | .158636124 |
| .020 | 16 | 成功 | 3.61e−5 | .445676449 | .158771435 |

q=.04/M6 从线性初猜直接求解失败，节点耗尽；不能据此声称不存在。上表只说明有限 BVP 有解，metric未付者明确不能视为合格等距候选。q变化时 g 也变化，不是固定g加密。

## 减轻第二谐波内部放大的新分支

双线性共振的 m4 内部增益约15.7；因此改试 q4=−.2q²，从已成功 q=.006 轨迹作真正非线性重求。在 q=.006/M12 成功，δ=.15854107498042347、vd=.4469332589252557，metric采样量1.4622e−8，height约1.408433；尾部实际H1约2.79589e−4。直接从vd=.4、q=.03线性初猜则越出设计角图，失败记录保留。随后从该真解延拓到q=.02/M12成功，δ=.15855646047499797、vd=.4469391683991532，metric采样量5.24098e−8，height约1.409030；正在继续q=.04。

独立自然分支 q=.02/M6 对 vd=.35/.4/.42/.47 的真求解均成功；q4/q²分别约.07725/.07973/.08260/.07006，均为正。不能凭离共振较远的vd变动假定会自然生成优化负cos4。

## 未付条件

以上端口仍是有限线性DN；没有真实非线性尾、无限接合、帽、固定握持区、全时reach或δ_E证书。小BVP残差也不自动给整个实际曲面的metric界。角图和控制未冻结前的不同M求解不能用作README第5项的固定g收敛证据。

## 复现依赖

`computations/source-dependencies.json` 固定68个必要代码/manifest文件，合计528996字节，源提交869436630c99aa5a68afb55bd8877c826034d117。`prepare-source-dependencies.py --repo <本仓库> --dest <临时目录>` 从 Git 提取这些文件并逐一核对hash；取输出的source_topic传给所有求解器。无需检出源课题的全部数据。报告中的绝对路径只是运行位置，不是数学依赖标识。

## q=.08 与真正有限neck

旧cut二次律从同g已验证的q≈.07/M32作小步warm，q=.08/M32在769节点达到BVP residual9.84e−7，但实际metric=1.44944e−5、Darboux量.01835，末阶core系数4.24e−8；不能计作合格近似。q=.1/M32此前进程退出137，没有输出，未确定外部资源原因，也不是数学失败。旧路线在小q已付同g收敛，当前优先新neck和真实非线性连接。

`root_dual_core_bvp.py`及`geometric-checkpoint-core-pullback.py`现按frozen_profile的hermite_boost_neck标识加载实际provider及finite_neck_terminal_v1切口；warm要求所有未控制profile字段相同。alternative的真实线性q4分支q=.001/M6、.003/M8均成功。root在同q=.003把q4一次从−q/(10√2)降至−.2q²（幅度改变99%），首轮residual约.149，随后离开双控制设计域；这只记录一次大步失败，不排除二次律neck。完整失败摘要为root-neck-quadratic-q003-m8-summary.json。

下一件具体工作：`root_actual_neck_bvp.py`将完整H=sigma*q*y_z交给持久非线性tail客户端，实际slope替换线性DN，有限shooting变分图及endpoint对称差分给高度Jacobian。保留full mean和二阶seam诊断，不把只匹配nonmean斜率称作完整闭图。

## 真正两jet接缝与数值坐标修正

root_actual_seam_audit.py依据R10从共同g−dZ²重建尾口的平面投影框架与连接，保留角holonomy和位置闭合量；只在一个角度对齐位置/方向。旧q003 linear-DN前缀对真实tail第一次响应的baseline，在N256/512给位置差1.44e−12、Fs差4.78e−10、Fss差1.12e−8，mean一阶约1.78e−13、二阶约−4.15e−12。它只是baseline，不是已经联解的闭图。

直接nested真实tail联解在第8次外网格迭代 residual5.90e−7/1160nodes、scaledBC2.61e−15后中断（exit130），没保存成功前缀。固定q4 scale3旧坐标也在1396nodes以4.73e−6失败；其重建物理残差峰集中在descending sync两个真实分段点附近。继承的prefix总长缩放坐标不能固定新neck所有内部knots。

root_neck_chart.py现用各段四次Bernstein正导数的积分构造C²单调坐标；nodal harmonic slopes再乘光滑公共factor，严格保持中间控制量≥.25r。它只改数值坐标，不改物理g。第一版保守slopes虽避免moving knots但引入额外径向导数、需更多nodes，已记录未达tol的尝试；当前balanced版近等长时近仿射。

实际tail联解改为可复核outer Newton：先求真tail，inner用其完整非线性响应的一阶切线；inner成功后重新求原真tail，仅在原physicalBC≤1e−10时接受，最多8次修正。真实slope/mean Jacobian为numerical的解析实现；二阶jet导数仍差分。完整三维mean/二阶seam和有限tail自身缺陷继续单独报告。

## 修正后的实际成功

balanced all-knot下，q003/scale3纯前缀在903nodes、tol1e−6成功，实际metric9.80e−10、Darboux量2.62e−7。真实tail外校正q003/M8在841nodes成功且只需一个外修正：重新求原真DN后的physicalBC3.2854e−19；prefix metric1.07383e−9、Darboux量1.59442e−7。末端nonmean二jet差为first3.29e−19、second2.26e−14；有限tail audit metric4.4478e−15、fullD2.3295e−17、normalizedFullDefect2.77e−16、κ7.99426。最终完整response为root-neck-q003-actual-outer-m8-tail-response_0003.json.gz。以上不含无限尾/帽，不是闭图。
