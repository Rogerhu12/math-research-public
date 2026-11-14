# 当前 M15 后的实际升频选择：优先一次到 M22

2026-11-10，numerical_recovery。**这是下一次数值计算的选择，尚无 M22 解。**
当前 M15 由 root 运行，参数和进程不因本文改变。

## 选择及理由

建议当前 M15 完成后，先读取其实际结果；若仍需升频，直接从它自己的 CP
和最终真实 tail 转到 **M22/N1024**，不先顺序支付M16、M18两个大联解。
当前最有区分力的证据来自尾的内部遗漏模式，不是仅从旧M14的单点误差
外推，也不是把某个固定态的局部上阶诊断称为新解。

independent_audit 对当前 M15 真实首包的 cell0 实测内部峰约
$1.4909764312\times10^{-8}$，在stage40/$x=.40625$；原生端点的
$4.88\times10^{-9}$ 低估了它。该固定状态的原投影方程在首遗漏频率48、51
有明显残量，而 N512→2048的公共角点metric变化仅约$2.5\times10^{-15}$。
在同一个局部状态中补零并重算原 root/ODE速度，M16/M18/M22的局部metric
分别约 $9.855\times10^{-9}$、$3.403\times10^{-9}$、$2.203\times10^{-10}$。
完整记录是 `notes/2026-11-10-78718-tail-metric-location-m15-first-01.json`，
实际 `fc528e / session27364`→`c15c22` exit0。**这些不是三张新尾解**，只表明
M16/M18在这项已观察到的误差来源上余量不足，而M22有较大改善空间。

随后真实 `d51727 / session78112`→`ba5e29` exit0 的680点局部升频粗扫
发现峰迁移：在同一旧M15轨道cell0各段的1/8网格上，补零M22的最大值
约 $5.710711\times10^{-9}$，M18约 $9.600185\times10^{-9}$，都在
stage34/$x=.125$。报告为
`notes/2026-11-10-78718-tail-local-mode-sweep-m15-first-01.json`。
所以前一段的 $2.203\times10^{-10}$ 只属于stage40的原峰，**不是全cell余量，
更不保证M22够用**。新增动量直接置零还不保持旧径向一jet；另一研究正在
比较先转raw高度/斜率、补零后重新投影动量的暖启动。实际M22仍值得推进，
但下一选择以真正的新尾演化为准。

M14的实际共同prefix径向下界 $>7.74\times10^{-8}$（R81）对那张固定图
有效；不能不经计算地搬到M15的另一组support参数。为避免这一外推，我
对已有M15 matched-cut UNSOLVED warm做了42点固定曲线投影，覆盖全prefix
并含旧重点位置。保持曲线不动，N2048评价并以2048角点算FFT诊断：

| 速度投影M | $E-1$ FFT-l1最大 | $F/a$ FFT-l1最大 |
|---:|---:|---:|
| 15 | $1.4292\times10^{-10}$ | $5.1772\times10^{-11}$ |
| 16 | $1.6613\times10^{-10}$ | $3.5849\times10^{-11}$ |
| 18 | $5.7788\times10^{-11}$ | $8.5465\times10^{-12}$ |
| 22 | $2.8713\times10^{-12}$ | $3.0766\times10^{-13}$ |

这张UNSOLVED曲线经过原全局Z-only cut匹配，其角向 $G$ 诊断仍约
$1.1541\times10^{-6}$，所有投影阶都完全一样；不能因此声称它已经是
等距解。真正的BVP必须同时修正曲线及自由参数。表中只比较原速度投影在
这个固定初猜上的局部误差，既不是连续包围，也不是新的求解结果。

此真实计算为 `98390d / session25071`→`7104da`自然exit0，程序自报2.227秒，
零DN、零BVP、零流积分。源为
`scripts/78718-prefix-next-mode-diagnostic.py`；报告
`notes/2026-11-10-78718-numerical-m15-warm-next-mode-diagnostic.json`
154,323 B / SHA
`5f0b54e3245a1d4a0bf4415c954545fc6ee6acb033791fcefbe651bf54de4746`。

## 可实际运行的 warm route

使用 `scripts/78718-run-prefix-mode.py`，它自动从成功CP取自己最后的
真实 `tail_seam.tail_record`。原 saved-mesh restart 将15模的R/T/Z
映入22模并补0，再做原inlet校正；原tail warm-remesh将两半shooting状态
按旧新模式索引对应，其余补0。随后首先做新M22/N1024的**真DN**，再进入
原物理BC联解；不会拿旧M15响应或Jacobian充当M22成功。

在repo根的下一实际命令为：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
 --modes 22 \
 --restart topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01.json.gz \
 --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m22-direct-01
```

这条命令尚未执行，输入CP也要由当前M15实际产出后才能用。若M15未完成，
必须明确改用实际保存的初猜及真实尾状态，不能把缺失未来文件写成成功。

为检查实际初始化而非只猜参数，已用旧M15 UNSOLVED warm和本轮新N512首包
实际运行同一入口的 `--modes 22 --prepare-only`：**87b9cd自然exit0**，
约0.602秒。得到67状态、22参数、2633节点、N1024、最大权8192；新prefix
请求与补零后的该真实首tail标签的最大差0.0。未调用DN/BVP。
报告 `2026-11-10-78718-numerical-generic-m22-initial-prepare-01-mode-run.json`
8,745 B / SHA
`9a566ee367312863a22a684b34f42cc3a80a44be62d407e80fa3717fe8dfcfa0`。
两次小计算的实际argv/回执为
`2026-11-10-78718-numerical-next-mode-observed.json`。

## 资源账：比较成本而不许诺峰值

原direct CSC对 $n=3M+1$、$k=M$、径向节点数$m$的精确显式槽数是
$(2n+k)(nm+k)$。以下是最终CSC的float64值、int32索引及indptr总字节；
全部规模低于int32索引上限。

| M / 默认N | 状态数 | 2633节点CSC | 6599节点CSC | 8000节点CSC | $n^2N$相对M16 |
|---|---:|---:|---:|---:|---:|
| 15 / 512 | 46 | 156.0MB | 391.0MB | 474.0MB | .881 |
| 16 / 512 | 49 | 177.0MB | 443.7MB | 537.8MB | 1 |
| 18 / 512 | 55 | 223.0MB | 559.0MB | 677.6MB | 1.260 |
| 22 / 1024 | 67 | 331.0MB | 829.5MB | 1005.6MB | 3.739 |

MB在表中为$10^6$字节。$n^2N$只是RHS Jacobian工作量的粗代理，不是
墙钟时间模型，未包含不同Newton轮数、tail延拓次数、mesh增长或LU填充。
原规定最小角数为$8(3M+1)$；M22超过512，因此本实际入口选择N1024。

M22的单次计算明显较重，但M16和M18并无目前所见的tail余量。继续保留
每进程DATA6GiB、Node1536MiB、max_nodes8000；真实启动前看可用内存，
不与另一重BVP并开。显式CSC不是峰值：还要容纳Jacobian块、LU、临时
数组和Node堆，不能据此保证不触内存限额。若新M22 bootstrap/联解实际
失败，再依据它自己的失败位置与保存状态决定数值恢复，而不预先做一串
没有针对性的昂贵尝试。

原物理g、phase范围、profile、chart、尾物理构造、tol$2\times10^{-9}$、
BC和physicalBC均保留。更大M只改变数值频率/求积与初猜；最终全图误差、
所有时刻的reach/嵌入及其余README完成条件仍需实际结果支付。
