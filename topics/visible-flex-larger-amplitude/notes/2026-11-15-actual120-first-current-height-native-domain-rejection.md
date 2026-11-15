# actual120：完整前缀域预检通过，首次当前高度的原尾求解被 D/S/A 条件拒绝

本次没有得到接受的非零112边值场。原输入和新六参数接口已经真实运行；失败发生在第一次当前完整112高度的原 native 请求，尚未返回全雅可比，未进入原边界有限差分、完整 DN 或最终审计。原响应是 `Error: momentum branch D/S/A rejected`，不是时间预算耗尽，也不是121的摘要传输问题。

## 1. 实际公开运行与读回身份

- 公开 [run43694844403](https://github.com/Rogerhu12/math-research-public/actions/runs/43694844403)，source `ace38440324f09471482826136584da38960c417`，创建于2026-11-15 08:30:44 UTC。
- compute job `132752997196` failure；独立 report job `132753527828` success。report成功只说明原摘要传递和字节核对成功。
- 两个已完成 job 的 `BEGIN_SIX_CONTROL_FULL112_SCALAR_SUMMARY` 间原 compact JSON逐字相同：**19463 bytes / `4f2be484a9d33faf5b9072bbb0c22989d885351a28a229f504aed34d1f081b85`**，hash排除分隔LF。`summary_complete=true`，`readback_errors=[]`；未有90KB fallback或省略。
- compute原日志92387 bytes / `ef65ea1f22691a1f059d44a6def89902d708fdc4d6fae972495ff3ded934020d`；report原日志43623 bytes / `76392651e181012cdcb02a5bb8f4952b48fd48ccd7134f79338f2808209db4c2`。

root读原已完成日志、全部阶段、完整首次H和原trace；本地仅字段选择与字节/hash操作，无科学导入、重新计算或从输出猜造缺失阶段。原完整输入、99源pin和调用范围见[120请求接口](2026-11-15-request120-actual119-batch3-positive-lambda-full112-interface.md)，不在Git重复存储可重算payload。

## 2. 真正使用的初猜和原预检

仍为实际119第3批末六参数：

`[0.41654476801167684, 0.23884336093393582, 0.5270922473095916, -0.13437878055563054, -0.005765450212224129, 0.4141025261683763]`。

三个odd控制固定，前三p保原active平方问题。显式 $\lambda=0.001$ 只缩原前三core目标和一阶初猜，不缩六个scalar系数；M=T=112、N=2048、699输入节点、完整453状态和高109自由未知量保持。初猜仅借原零H全J与同circle低三线性传递，不是已接受非零锚。

原输出 `initial_collocation_max=6.8749454041621035e-06`。低三unit方程仍为 `[-40.59554745991145, -0.020429301868211316, -6.463227430456828e-05]`；原112线性右行前三为 `[-18.7513817252759, 0.0012195172149540542, -1.016669334572825e-06]`，其余109初猜为原负零。这些值都只是初猜的实际诊断，不能代替非线性全112接受。

完整前缀RMS域预检 iteration0通过、没有加节点，两组各698点、invalid_count均0。节点和中点也有原实际最小值：

| 原查询 | 原 minimum_beta_squared | 原最小值位置s |
|---|---:|---:|
| nodes | 0.0022538385815712436 | 2.262368580603409 |
| midpoint0.5 | 0.002267325049764346 | 2.2641940822709667 |
| RMS0.17267316464601146 | 0.002245239130645116 | 2.2629990109034166 |
| RMS0.8273268353539885 | 0.002259211840830444 | 2.2621383298889284 |

这四项原最小值的 $\phi$ 均为0；它们是该次离散query的域结果，不是连续全域metric、C²或reach证书。预检通过没有覆盖后续原尾求解的D/S/A条件。

## 3. 首次完整当前H请求的实际停止

原worker成功发送ready；原storedMetricAdapter的前后fingerprint同为 `8a87255bf9e025190a1a98ff800859f05f95a94113045a60af9391fcace51d24`，原配置 `maxIterations=32`、`solveTolerance=2e-09`、576深度、2048 quadrature及原尾g没有换掉。

原trace为：

1. `08:31:48.277Z` 注册原 `fourier-root-and-product-moments-v1` 和 `full-shooting-tangent-v1`。
2. `08:31:49.213Z` call1请求 **完整112项**当前H，`jacobian=true`、`audit=false`。H的首四项为 `[0.0008954476172889355, 5.023344896215423e-07, -2.0011103217478445e-07, 8.168067469179438e-08]`；原数组还含非零高模小量，不能截成前三模。
3. `08:31:49.232Z` 原compact-storage GC事件。
4. `08:32:53.089Z` call1返回 `Error: momentum branch D/S/A rejected`。

原请求H的canonical JSON身份为2572 bytes / `317ddda93a22ed1ca8e2a2d214e283a53da0b302dd3e1573893edba5985ae6e7`。保存的原response标明 `actual_nonlinear_solve=true`、`finite_tail_only=true`、`failed`为上述原异常、`lastIteration=null`。这不是一次已收敛response；`checkpoint_present=false`、`full_J_present=false`、`audit_present=false`，耗时原值63.87812351699999秒。原trials为空，没有已记录的Newton迭代残差、接受步或失败的具体r/角位置。

因此，当前证据只能定位为“第一次真实当前H求解在返回全J前被原D/S/A检查拒绝”。它不证明真实非零解不存在，不区分哪一个D/S/A量、哪个RK阶段触发，不证明浮点底线，也不支持用小H或高精度的预期改进冒作实际结果。顶层 `actual_current_H=null` 是未完成该阶段的含义；实际**请求**H另由原native日志完整保留，两者没有矛盾。

adapter诚实保 `phase=exception`、`success=false`、`new_coupled_finite_acceptance=false`、`full_Cartesian_closed_surface=false`。唯一live call为 `{jacobian:true,audit:false,completed:false}`；owner关闭已尝试且实际成功，无关闭异常。

## 4. 没有运行或通过的后续责任

原摘要中以下字段全为空或空列表：`boundary_FD`、`original_full_DN`、`accepted_result`、全部inner evaluations、完整banded solve reports和native trials。不能将初始域预检通过写作全DN接受，也不能把缺失阶段解释为通过。

所有原阈值保持：outer8、inner17 trial、native32 iteration/10 trial、collocation1e-6、boundary1e-11、native2e-9、boundary FD5e-5。此次没有运行这些后续循环，没有改变阈值来处理失败。

wrapper原 `elapsed_seconds=87.784149554`，科学child与wrapper均exit1，`budget_exhausted=false`、`external_signal=null`、`stdout_copy_errors=[]`。300分钟墙钟并未触发。rules runner 08:31:25开始、08:32:53结束，无README变化、无同步失败、科学checkout未改；原rules记录的partial文件保留仅到后续readout，最终cleanup明确已删除本请求拥有的临时payload。没有raw artifact、Release或Git上传。

## 5. 保留的关键原文件身份

| 原临时文件 | bytes | SHA256 |
|---|---:|---|
| process-status.json | 2769 | `866b4d9b22c3ae7ae3a79ac2aaeeb632c4a4e1c12b927b8d0dca5f219d9bfc3d` |
| science/adapter-status.json | 11721 | `eb2357d5f68e34e4cce7c7cbe5a5114e47934b1ecc8d026d07bbed2c96f4dead` |
| initial-guess/prepared.json.gz | 2474073 | `06015e1820f521bab293f52f5d755f7e00f95bc05cdcae156595981fc82dde95` |
| RMS-domain-preflight.json | 1521 | `92e8cbe3fac75a115b25e9fdc458600f42401f267e5b299476224e0fc2068ccf` |
| true-tail_0001.json.gz | 7734 | `9e966d0364a10e6d64b8d9908e78632945e493636b23aad7754786c2e9fc1107` |
| true-tail_ready.json.gz | 6859 | `72233811ae2b5221a9f27122d68e40b55e43d53dd07c722dc6224ba5330189ac` |
| true-tail_trace.jsonl | 3257 | `d9c7eeafc1b0dd5bc49f2baf660b00d355c041bb56933f6e96e05e9c57891bd8` |

原初猜解码7877601 bytes / `449a04059301a506a8812033c82e10351a0d7b3aeaa3b7531dd7bbc0651e70dd`；原失败response解码20807 bytes / `491e3aeba44c65f005090f582918c0496a2170d00774440e1faf9ed305911eac`。这些身份供真实重建辨认，不声称已删除payload能由hash恢复。

## 6. 按实际阶段继续

[同worker完整H(s)接口](2026-11-15-original-same-worker-full-height-continuation-interface.md)现在有明确尝试依据：前缀预检已过，首冷当前H在原尾域检查被拒。独立124将从真实零H请求开始，随后沿**同一完整112向量**渐进到H_*，只使用原worker真正收敛last；每次仍原Newton与原接受门。新实验不保证首正s可达，零点的旧比例warm无效必须保原fallback。

拟定显式初步s=1/64、接受后步长翻倍且上限1/4、原数学failure后减半、最小2^-20与最多64请求；这些是独立实验资源参数，不是新数学接受门。真实协议/写record错误不能用缩步掩盖。最终必须直接原H_*数组再求全J、原FD，随后同owner原fullDN/finalJ/fresh audit；120源码和原失败事实保持不变。

这不是完成课题。113/122完整高精度与有限trace方向、118完整物理模型及123新控制继续分别承担自己的实际责任，不能从另一条线的改善替本次未完成阶段付款。
