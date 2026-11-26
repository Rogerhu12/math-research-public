# R68 补弧谱族 v3：实际零锚入口与真实延续

会话：Astra-held10-06bbeb39-20261126。状态：五个独立 v3 文件已经 root 与 actual_tail 审阅并排同一 warm runner 的下一命令；当前尚无 v3 实际同图验收或新 BVP 结果。

[R68](../results/R68-complement-interval-phase-controls.md) 定义新补弧谱族和连续曲率列的明确下界。它与 v2 的有限 span 不相同。原 v2 provider/model/step 全部保留，正在运行的 v2 没有被修改或取消。

## 唯一允许的直接转换

输入为已实际接受的 v2 零控制锚：

- run SHA：bea39fb06862dfbfa1a00c6b89981f42a02c01b135739a0ee3ec15d716fa4e1f；
- raw SHA：5dd5419b19ce21ae2ebb088ea5d13ca6f453e60f15970757126dadd8eca18f7a；
- physical SHA：85ee93caf241c557d131aacae4e0253e023ce8d45ca0db41f109ab937741898a。

新集中门重新调用 v2 的真实 accepted_input，核所有实际 p 为零、重建物理控制为零、lambda 等于原 R53 锚值。完整 profile、物理尾、两种 chart、gauge、mean1168 与原支撑向量逐项绑定；不能用非零旧控制置零冒充同图。

同图入口使用同一个基准对象，实际重算 F/Fu/Fuu、投影、原 raw 节点与 RMS 取样点的坐标、f/fm/collocation/RMS/两种 BC 逐位等式。physical 的 x/c 仍取同一个场，p 仍全零。随后实际重做原角 floor 及两倍 floor 的完整度量。任何门未过都不接受。

身份仍为 same_cartesian_map_verified_reexpression，solver_invoked=false、solver_success=null、raw.success=null；实际成功的上游求解来源单独保留。新参数导数按新 basis 计算，不声称与 v2 Jacobian 相同。

## 真频率与后续求解

warm_definition 明确声明真 P=2π/3、L=P/2−S、ω_j=jπ/L 和冻结的字面 S/b；每个 M 取同一无限族的前 M 列。double 实现是这些真实常数的数值评价，连续真图及其浮点转移仍需独立 oracle，不把打印频率当重新优化后的目标。

provider 的控制合同仍为 d_j=phase_scale·p_(j−1)，legacy floor1e−9、完整 gauge、原曲率域门和辅助坐标约束不变。model 另外绑定原 v2 validator 和公共 bootstrap 源 SHA。父入口只在实际同图门通过后调用新的 solve_bvp：

~~~bash
python scripts/resume_20261126/warm_fixed_m3_continue_v3.py \
  --repo REPO --work WORK \
  --source-run WORK/warm-v2-design/reexpressed-anchor/run.json \
  --outdir WORK/warm-v3-design
~~~

原631节点保持、完整 lift 系数为1；必要升M严格补零同族未知。原 RMS/BC/physicalBC 和双角完整度量门保留。仅真实 BVP 成功而度量单独超门才升M，其余失败从最后 accepted 场二分 lambda，失败场永不晋源。分块8与释放失效 LU 仅改变资源生命周期；实际 Newton/辅助域计数通过小记录保留。

## 已执行的小检查

[检查源](../scripts/resume_20261126/check_warm_v3_contract.py)和
[实际小记录](2026-11-26-warm-v3-synthetic-contract.json)是合成核心 API 检查：
零控制 F/Fu/Fuu 逐位同；M8 与 M24 公共频率前缀逐位同；
4列实际参数链的二jet中心差分最大误差 1.3414647170861826e−10；
非零控制 lambda1 的保护弧曲率误差约 5.55e−17。
它没有调用 BVP，未创建 accepted 场，也不替代上面的真实原场验收。

真 DN 与连续几何入口须显式适配 v3 并绑定同一个完整定义，不能套旧族的证书。实际 lambda1、full H、公共 Cartesian 两jet、固定问题收敛及全时10%条件仍待支付。

## 实际首步失败与下一项定位

[首 λ=.004 真返回](2026-11-26-warm-v3-first-lambda-failure.json)为status1/maxnodes，3168点、RMS .12464611971520359，raw SHA db0e9c6b5754cdabb7fe1af9748b3cb7b3569a707551cc97872034cb45f406ae。原Newton统计 accepted_steps1/calls3/no_step3、27个域拒和56个merit拒，唯一接受步最小α=2^-20；辅助exp预门没有拒绝。实际控制只有约10^-6量级，不把这称作λ推进，也不推断域拒的具体类别。父链仍从真正接受的λ.002锚点试λ.003。

另新增只读 probe_warm_projected_parameter_columns.py（SHA 4dd05d821b2abe27046acbd4b822d99397f0940d106ffae8665b165e84ad5711）。它只用原v2/v3同零锚实际raw，对两个相互隔离进程中的真实inlet projection、完整exact-lift余部、七原节点的RHS和BC参数列作有限矩阵诊断，并对四个选列作两档FD；不改变部署五源，不解BVP/逆问题。原p0实际映d1=phase_scale*p0，不能称纯gauge；保继承q_aux域并报告其真实d1范围。原exact-lift保留，不能把低阶Fourier投影条件数当完整BVP条件数。compile/help已实际通过，本地没有runner的实际raw，故未执行数值诊断。完整数组仅runner scratch，小投影另存。
