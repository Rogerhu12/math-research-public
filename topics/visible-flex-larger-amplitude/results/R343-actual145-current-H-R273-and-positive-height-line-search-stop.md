# R343：actual145 当前正H完整R273方向已产生四次下降，末轮原十试步仍拒绝

日期：2026-11-15。性质：公开 Actions 原执行结果及字节读回；不是新存在性、误差下界或原生接受证明。

## 1. 实际结论与执行身份

actual145 在保留原同进程 warm/predictor、原完整576段映射及十档 noJ 回溯的条件下，将原局部图 correction 替换为本次当前H/状态/完整J/原sigma的完整R273方向。零H请求收敛；首个正高度比例 s=1/64 的请求真实返回了五次完整方向，前四轮分别以 alpha=1、1/16、1、1/2 接受。第五轮十个实际 noJ 评价全部返回有限残差，但均不严格下降，原失败是：

> Error: multiple-shooting line search failed at 2317.31958952296

19个正H试步中有4个接受、15个 residual-not-decreasing、0个 D/S/A guard 拒绝。它已不同于 R315/actual124 的13个正H请求全部在最初试步层触发 D/S/A。当前结果仍没有任何非零H原生接受，后续原338×112响应、FD、fullDN及最终物理审计均未进入。

- [原run43716379970](https://github.com/Rogerhu12/math-research-public/actions/runs/43716379970)；source commit：`a513ada7d1dbe1b2fa51d3f1f987c59b48233dba`。
- compute job `132818710078` 为 failure，report job `132880508698` 为 success；后者只表示已有读回成功。
- 原规则监控起止为 `2026-11-15 12:57:22 UTC` 至 `2026-11-15 16:38:26 UTC`；science/wrapper returncode 均3，README_change=null、external_signal=null，无规则中断。
- 原包装器 elapsed_seconds=13264.184668586，声明科学墙钟18000秒；budget_exhausted=false。停止是首正H的真实数学拒绝触发既定策略，不是耗尽64请求或墙钟。
- request SHA256 `8800b003bb21dc36d7d4a9739d9f0e8e9f16109754d2d4a9c8f628012a24c99c`；recipe SHA256 `e9f724327bbe0303d1de4e832e2f56cd704cd71c6d396d5cfbc4eb00fb78ef33`。

## 2. 当前场、输入和原门

本次仍采用 actual120/124 的同一显式六参数实验：

`[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]`，

顺序为 p1,p2,p3,theta1,theta2,theta3，后三冻结，前三保持原物理问题的active参数；lambda_target=0.001。它不是新九控制或新C族，也没有使用旧91/95/103失败 checkpoint。699节点的 fresh-circle-low-three-linear 只作初猜；高109核坐标仍是自由未知量，未声称高109非共振已付。

四数学输入实际从历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复：

| 输入 | 原字节 | SHA256 |
|---|---:|---|
| accepted | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail anchor | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| T112 config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

两历史ready也按原563a9997…/c1c44f23…恢复；原ready/current config没有被改写为新接受场。Actions启动记录实际核了115项source identity；本读回没有在本地再次导入这些科学源或重算场。

原本次 fresh H_star 完整112列已保在原摘要，首项 `0.0008954476172889355`；原896字节 `<f8` 身份为 `d19e25eabad7f2c84ecdd10580caee1c3b41ef9d1e0a1a3ae07c58486277eced`。它含全部高模原值，未截成前三模。首正请求的完整112高度raw SHA为 `fb6da818e40bcdaa0bc57ceb9a86d5ae2845132054389a2eac73ea866283a032`；五轮snapshot均绑定这一实际请求。最后原H目标并未到达s=1。

保留原native最多32轮、每轮十档、严格norm下降和2e-9门；未新增L2、exact账或QR最优性门。R273使用显式eta=1、全部577个惩罚块、所有cut/stage/far行；不是旧H/J的重标签。原226态和两个mean仍由原flow负责。最终338行、112输入列的边界响应不能由这些224状态方向或exact账替代。

## 3. 同一owner的两个真实请求

| call | s | 原请求秒数 | 实际结果 | 后继状态 |
|---|---:|---:|---|---|
| 1 | 0 | 1176.004412504 | converged=true，norm=0，原checkpoint存在 | worker last为零H |
| 2 | 0.015625 | 12054.504250708 | iteration4原十档全拒，failed response存在 | last仍为call1，未把失败checkpoint晋为成功 |

两次协议都请求 jacobian=false、audit=false；这不取消内部每轮完整withJ。零H响应没有被标为最终非零场。首正请求保留原tangent warm，trace明确记录其 maxChartCondition=385639413119263240000、maxRelativeCorrection=3.844494357362678e+252。这是原初猜诊断，不能单凭其数量级判定后面所有失败的唯一原因。原trace还确认首次完整withJ真实返回，而不是在initial或首次root中断。

首正请求包含19条trace事件及19条原trial；零H包含6条trace、0trial。原最终trace总数26还包括worker生命周期记录。Python cache与worker last在失败后保持原零H来源；已接受的四个中间Newton态只属本次失败请求内部，不能冒作可对外接受的native锚。

## 4. 五次当前系统与完整精确读回

每一轮均有新的 current_state、snapshot、矩阵身份与delta。全部QR退出0、桥接错误null、完整direction_returned=true。每轮报告：

- 原行/列129248，augmented_rows=258496，576段、577节点、block_width224。
- qr_calls=1153、formation_calls=1152、pure_constant_rows=129248；全部577惩罚块保留。
- factor及constant字节464891392；declared上界2147483648。
- 原形成underflow计数0。此计数不是完整舍入误差为零的证明。
- exact账每轮129248行、576段、28901488个原乘积位置。它对保存的binary64系数和最终delta做准确dyadic算术，按本次原sigma缩放；不把eta惩罚行算进原残差。
- QR数值工作精度报告 dtype=float128、itemsize16、significand_bits=64，属于该平台longdouble数值实现，不能叫113位binary128持久状态或严格QR分解证书。

下面的exact范数是原报告的十进制显示，未在本地由分数再计算。节点/行均按原零基编号。

| iteration | 原当前withJ norm | 当前最大行 node/component/global row | exact保存仿射终点范数 |
|---:|---:|---|---|
| 0 | 195955.61867016536 | 58/Pi111/13326 | 2.080989969356973859886570445112751078677236215431135423057695609E-1 |
| 1 | 6775.933695117896 | 58/Pi111/13326 | 2.080985591654180873052553674164794808138183289990271307779985972E-1 |
| 2 | 5340.898475958211 | 59/Pi111/13550 | 2.080985240685701282971821594203909614471977060071562021578518145E-1 |
| 3 | 2789.867248510024 | 58/Pi112/13327 | 2.080979624784268585350610231885723154489371125632623645558389957E-1 |
| 4 | 2317.31958952296 | 58/Pi109/13324 | 2.080976813130716819050010405495418183786857496773813255776344670E-1 |

五轮仿射终点最大行都是node40/Q2/global9073，对应rawCell0/rawSegment3；当前原残差最大行则在node58或59的高Pi模。末轮当前最坏为node58/Pi109/global13324，原sigma word `17355deb870d323f`。这里的“仿射终点”是保存的线性模型r+A delta，不能称真实noJ映射导数已验证，更不是实际全步残差。

| iteration | 当前state raw SHA256 | 返回delta raw SHA256 |
|---:|---|---|
| 0 | `9d6bec566bf987e05a81ab33f3e412b714bc5c48f7293c433568e99b4b552df4` | `ac24572558e34cc1426495b699d233a0985732e48bb88dcca1623e2dd3531b57` |
| 1 | `f5a4a9b3d65ca4085f7af5b31f92ef1168b71553c1c6a2f302a15474856449ed` | `bced8e502f6b6be15121c706f504808d37ebace8baa85fd93fd8e5431cb3ca47` |
| 2 | `86a815357ae1a45a0e7daccf1bf8dde2a6f5303187f3093275555f3d90eacf66` | `47113e70a27aca55b233127cfd2e395da00997b08f238267bd774fc9e58c2674` |
| 3 | `7ed56c0ba9e74f02aa8609ee744d175d399790c08022ee5cf89d613c3161009e` | `4e315d88e88aa9936e0263266311650eb4152ae0c1fc7b09fdf62f2d6d597a44` |
| 4 | `bcebfa6fc37b7285da3498fdebc9983263c1dd8f08b49d203f800ee2fb08f6ba` | `27f6859cd57fbca03279773dc7b70d1a9e5c8d99d99164642692ba5b1c829a7f` |

末轮新矩阵SHA `911def78090cf4270c5da459fd40fc1be2adea44ad634bc09267591da7394da6`；末snapshot result `b7877920186e36a50087f50acc2ed5b35b74fb9ee6d6931a62b9891de84248bb`；末exact全账gzip身份 `1f1a7b2f24b0b67a02b0162c2a538c4714ad6b3a566452bacc94ecde95d747ff`，原4912820字节。这些payload已按规则删除，身份不构成可恢复现场。

末轮formed数值诊断还记录：base_objective=`8340735.6423920859916`，objective=`0.023623099417241689881`，full_unpreconditioned_model_gradient_two_norm=`2.281794312413644452e+23`，factor_triangular_residual_infinity=`0.000101425990195025406144`。原报告明确这些longdouble量不是严格后验包围，不从它们声称模型已准确最优；也不因其数值额外拒绝原试步。

## 5. 全部19个实际试步

下表逐项抄原native trial记录。accepted仅表示该原Newton迭代内部严格残差下降，不表示整个正H请求已通过2e-9。

| iteration | trial | alpha | baseNorm | trialNorm | 原kind |
|---:|---:|---:|---:|---:|---|
| 0 | 0 | 1 | 195955.61867016536 | 6775.933695117896 | accepted |
| 1 | 0 | 1 | 6775.933695117896 | 12883.972097044852 | residual-not-decreasing |
| 1 | 1 | 0.5 | 6775.933695117896 | 11433.107333806529 | residual-not-decreasing |
| 1 | 2 | 0.25 | 6775.933695117896 | 10405.587187339477 | residual-not-decreasing |
| 1 | 3 | 0.125 | 6775.933695117896 | 7503.516372233028 | residual-not-decreasing |
| 1 | 4 | 0.0625 | 6775.933695117896 | 5340.898475958211 | accepted |
| 2 | 0 | 1 | 5340.898475958211 | 2789.867248510024 | accepted |
| 3 | 0 | 1 | 2789.867248510024 | 3258.231187213628 | residual-not-decreasing |
| 3 | 1 | 0.5 | 2789.867248510024 | 2317.31958952296 | accepted |
| 4 | 0 | 1 | 2317.31958952296 | 3323.581811506391 | residual-not-decreasing |
| 4 | 1 | 0.5 | 2317.31958952296 | 4609.656727249437 | residual-not-decreasing |
| 4 | 2 | 0.25 | 2317.31958952296 | 4783.01926525404 | residual-not-decreasing |
| 4 | 3 | 0.125 | 2317.31958952296 | 3768.6950829407447 | residual-not-decreasing |
| 4 | 4 | 0.0625 | 2317.31958952296 | 7343.474818724777 | residual-not-decreasing |
| 4 | 5 | 0.03125 | 2317.31958952296 | 2386.5856895319916 | residual-not-decreasing |
| 4 | 6 | 0.015625 | 2317.31958952296 | 5139.563375140021 | residual-not-decreasing |
| 4 | 7 | 0.0078125 | 2317.31958952296 | 12554.412791161762 | residual-not-decreasing |
| 4 | 8 | 0.00390625 | 2317.31958952296 | 4887.836498107898 | residual-not-decreasing |
| 4 | 9 | 0.001953125 | 2317.31958952296 | 3476.521703862006 | residual-not-decreasing |

末轮所有十档均真实返回；没有补算未访问档、没有D/S/A异常、没有把小alpha当连续整段证书。末三档也没有回到同一base词：原记录分别12554.412791161762、4887.836498107898、3476.521703862006。因此不能将本轮套用“后三档同词平台”描述，更不能从这些scalar给出普遍浮点下界。

前四个已接受noJ norm逐字等于随后fresh withJ的原norm。但这种已观察标量一致，不证明各完整残差向量一致、同一有限root执行轨迹一致，或隐式/有限trace导数一致。

## 6. 已付、未付与读回范围

本次付了当前正H的五次完整J快照、完整R273候选、原全部已访问noJ回溯。原末minA=0.9315745715410189、minD=0.9999646948519476；它们是最后基点的原值，不是沿整条alpha路径的下界。末chartCondition=null是新完整系统没有计算旧图条件数，不能写成零或已证良态。

没有付：正H收敛、s=1高度端点、最终338×112响应/J、三方向三步FD、外层fullDN、最终独立physical/cut/mean审计、闭面、连续域及原metric目标。original_full_DN、accepted_result为空；new_coupled_finite_acceptance=false。原32轮上限不是本次完整执行32轮的声明。

原compute完整log为465111字节，SHA256 `6e2c5514f2b4ad37f19ad5d9813e939afbaaf58c6b54b924b7bea4d8c6127c89`；report log为164203字节，SHA256 `442c5a663bcc686937d202383c87697323a45668d11ce8c32abda8803594183a`。两job的有限主摘要逐字相同：79733字节、SHA256 `276bbe45aeee68e227cd81805a9ed8c43fdd2dffd1dd0a90b9aa2df6837ddcad`，不含分隔LF。

原summary_complete=false：它为满足短report限制而省略若干大section，不能改写为完整摘要。必要内容在compute的两个完整request-returned事件、五个完整correction事件和五个 request145_reader_original_R273_record 中仍在；这五条各自summary_complete=true，本次已读。所有五轮QR stderr均原0字节，stdout完整文本也已按各自size/SHA核对，共10个子日志身份相符。末尾readback_errors=[]，没有观察到桥接或QR进程异常。

大J、因子、exact ledger是在每轮子进程退出、完整577×224 delta复制校验、返回记录写完后退休；每轮移除1751文件，两目录仅snapshot/large-arrays及qr/large-arrays。原删除字节依次709373959、709356160、709345475、709287657、709299908。读回只读剩余元数据和原标量，不声称本地重新审了这些完整payload。原完整科学log91923字节，SHA `469beb1040c74fb31fbb198b1d686fe26e429413e10a49975c2b6c960e3f6d17`；它在RUNNER_TEMP，未上Git/Release/artifact。

## 7. 可复现入口与下一实质责任

原run绑定的workflow和唯一请求 public-six-control-r273-height-request.json 固定上述recipe、四数学输入和115项源。主要实际新源如下：

- `exact_20261115_original_r273_current576_chain_qr.py`：21836 B，SHA256 `d5d9874242499df7a79fe4411a420de0cfe8464c64c80dd9c18ec501d226a296`。
- `exact_20261115_original_r273_current576_system.py`：28284 B，SHA256 `3557608524becae2bbf1c2100af12c865082329efccbd5078008cb2c8591c101`。
- `geometry_20261115_original_r273_height_path.py`：23355 B，SHA256 `73c62d94a60eb1ee2fd50d68c14d6af29c590729fcdb764c5c4036ca963305ed`。
- `geometry_20261115_original_r273_tail_client_hook.mjs`：46729 B，SHA256 `f13b0a0d3f7e6d3487f0eda92dc9e76117137ee106c9f33471e762e35c9106e0`。
- `geometry_20261115_original_r273_tail_client.py`：18253 B，SHA256 `2fe2c25233061de0fd89b7af72cba5ddd2e2d144889492ec42156f781c4828a9`。
- `geometry_20261115_six_control_r273_height_full112.py`：46439 B，SHA256 `d1f21025a91234252c856cb15bf26ce48e2628e8fa92352a9d98ffd53b14a69d`。
- `root_20261115_six_control_r273_height_run.py`：9959 B，SHA256 `f5f86bbac39011ea18396aecd62db2af86a2f2ed787199523e0ac8cb3a89f754`。
- `root_20261115_six_control_r273_height_scalar_readout.py`：37864 B，SHA256 `be629d07ce38ad67ea436f8ce1cf55b3484c06e5db7fff575ad755d4bac9d84d`。

复现必须从这些真实输入重新生成当前H、warm及每轮完整J；不能由本结论的state/delta哈希伪造续解。原代码、参数、run和输出SHA已足够标明实验，本文不保存可重算raw。

本轮支持保留完整系统候选这条改进：在相同正H比例与原warm政策下，它已得到四次真实下降并避免旧130次DSA拒绝现象。它也明确留下新的缺口：保存模型的仿射终点约0.208与末轮全部实际noJ残差之间仍有显著差异。下一步应在同一当前正H和真实状态上区分状态形成、有限原root/RK映射及其方向模型；旧零H或失败73场的导数结论不可直接移贴。R283/R305/R314/R325所区分的有限trace与严格形成责任仍适用，但本次尚未支付该正H的相应证书。原warm的极端诊断值可作为后续有明确身份的初猜对照动机，不能据此先定唯一病因，也不应只反复降低H或增加同一回溯次数冒作解决。
