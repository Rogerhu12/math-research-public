# 同g的M/W分离、几何暖启动和实际进度

2026-11-10，numerical_recovery。所有改变只进入后续的通用入口，当前root
活动M15的源/参数均未修改。没有额外冻结、审批或独跑前置。

## 1. 后续可直接选择的路线

`scripts/78718-run-prefix-mode.py` 原 `--modes M` 表示前缀阶数。
新增 `--tail-modes W` 表示真实尾阶数，要求W≥M；省略仍取W=M。
`--angular` 和 `--tail-angular` 分别控制求积；省略各取满足
$N\ge\max(512,8(3\,\text{阶数}+1))$ 的最小二次幂。

当前M15实际返回后，若它自己的连续prefix已经足够，可先保持前缀M15，
只把真正尾及边界反馈提高到W22：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
 --modes 15 --tail-modes 22 --jacobian fourier --transforms fourier \
 --restart topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01.json.gz \
 --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-direct-01
```

这条**尚未执行**，CP须由当前真实主计算产出。若新prefix本身不够，则改
`--modes 22` 并给新stem，得到M22/W22/N1024。有限上阶的实际误差仍须求出，
不以单个固定态的预测代替。

要只获得一个真正W22暖状态而不进入BVP，附加 `--tail-only`。当前已实际
准备过的具体旧warm路线是：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
 --modes 15 --tail-modes 22 --tail-only \
 --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
 --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
 --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-w22-warm-only-01
```

它也**尚未执行**。目前M15的重内层活跃；实读MemAvailable从约5.93GB降至
4.34GB，且Node1536只限JS堆、不限总RSS，故不叠加这一DN。默认仍是每进程
DATA6GiB/Node1536MiB，不能据此假设两个进程峰值一定能同时容纳。

tail-only在真实目标H上用原DN求解，响应可不另算最终外用Jacobian/audit
（请求为false/false），因为它只是新的初猜。原Newton方程、残差和求解
策略未改变。后续联解自己的实际请求仍须取得真Jacobian，最后真audit也
不能省。输出状态明确为`ACTUAL_TRUE_DN_BOOTSTRAP_SUCCESS_ONLY`，
`finite_coupled_success=false`，不保存伪prefix解。

## 2. 边界投影的精确含义

新 `scripts/78718-prefix-projected-tail.py` 保留原flow、BC函数、
`solve_with_actual_tail`、谱权和真实外迭代，仅给较宽真尾一个M维view：

$$H_W=E H_M=(H_M,0),\qquad T_{M,W}=P_M T_W(EH_M),$$
$$D T_{M,W}=P_M D T_W(EH_M)E.$$

原完整响应Jacobian的行是`slope W, second W, meanSlope, meanSecond, height W`。
view保留每个向量前M行、两个均值行和前M列；所有有限BC仍使用原
$qR_Z-P_M\mathrm{slope}_W/\sqrt{E_{cut}}$ 以及原physicalBC容差。
M/W不等时的新main去掉原M=W检查，并保存完整W jets；其余调用原数学对象。
相等时仍调用原coupled main。

完整W request/response/Jacobian保留在实际末尾文件中。CP同时写出
`tail_seam.full_tail_jets`、低模view及高模坡度/二阶量的标量诊断。
这些高模没有被低模BC消掉，不宣称高模接缝已经匹配。
后端实际common-cut按全部planar/height模式扩基，并连同两个均值匹配完整
XYZ的零、一、二jet，最后以真实连续metric预算支付。相关完整公式见
`2026-11-10-78718-geometry-prefix-tail-mode-split-interface.md` 和R87。
R87中要用实际修正宽度和完整rho/b因子，不能把整个修正区当成warp已为零。

## 3. 为何改变warm表示

直接给新增动量π补0不保持旧$u_r$：π是非线性ω的投影，低频高度/斜率
本来就能产生高频π。当前采用另名
`78718-tail-geometric-warm-remesh.mjs` 与
`78718-prefix-tail-geometric-worker.mjs`：在相同depth/parts下先读取旧engine
的raw Q/L，新增raw模式补0，再由新engine重新初始化全部动量。
首端使用正确portRatio归一化，其余按实际cell的μ和profile处理。
同N的保持恒等式与跨N的浮点差别在R86中说明；这里只把它当初猜转换。

原trial client的solve/close方法被直接复用。新
`78718-prefix-tail-geometric-client.py`只选择这个worker，完整记录真实源路径
与SHA。原residual、36轮、line search/floor、深度/parts/steps、固定物理
参数及audit协议不改。`78718-tail-mode-continuation.py`仍使用原H延拓
Coordinator；1/8、最低1/1024、每外请求最多32次的政策保持。

尾研究代理实际全865节点转换 **8fdf73/session46809→31b1a1自然exit0**：
M15→M22/N512的maxQChange=0，$u_r$公共角最大差约$5.8094\times10^{-16}$；
N512→1024约$5.8009\times10^{-16}$，零DN、零BVP。
该报告为 `2026-11-10-78718-tail-geometric-warm-probe-m22-01.json`。
这是转换检验，不是新高阶轨道或解。

## 4. 轻量进度

通用driver写`<stem>-progress.jsonl`，只有标量与时间：

- true-tail初始化起止及完整warmEmbedding诊断；
- 每个真实尾请求起止、物理调用数、残差；
- 内层BVP起止、节点数、状态数；
- RHS Jacobian起止及节点数；
- LU分解起止、矩阵维数/nnz、factor nnz；
- Newton调用/接受步/无步计数；
- 本进程VmRSS/VmHWM和环境MemAvailable。

它没有打印数组，不访问其它工具session的PID，也不是存活证明或数学
验收门。LU观察只读`nnz`，不为日志取出L/U矩阵。尾-only结束另存已结束
子进程的peak RSS，供下一次资源安排。

后续主计算可显式选 `--jacobian fourier`，或以 `--jacobian original`
回到原装配；缺省仍是original。Fourier选项安装root的
`78718-prefix-fourier-jacobian.py`，只替换新建Flow的`adapt_fun_jac`，
原RHS、BC与容差不变。元数据记录实际选择及来源SHA。它在第一次
build_classes前安装，所以BC直接调用的同一Flow导数也使用一致后端。
根实际32点比较 `d32b54/session22824→df2eda` exit0：M15/N512
0.129s→0.0292s，M22/N1024 0.405s→0.0583s；相对Frobenius差约
$1.97\times10^{-15}$、$2.59\times10^{-15}$，参数导数严格同值。
这只证明这次小样本计时与数值一致性，不保证整次BVP的加速比例。
完整有限DFT数学等价证明由root的R88给出。当前活动M15没有热替换。

另有 `--transforms fourier|original`，默认original。前者用
`78718-prefix-long-fourier-transforms.py` 替换新Flow实例的values/project
线性变换，RHS本身、frame及warp公式不重写。它和R88的six-JVP装配作用在
不同层：先选Flow.adapt_fun_jac，再由新Flow初始化挂FFT变换；后者不改
`B/B1/B2`或原norm，所以six-JVP的有限DFT表保持一致。两者都读取同一个
当前frame，复数输入在FFT变换中分开实/虚以保留complex-step。
未知/复制表或不适合FFT的N直接使用原方法。实际性能及范围见
`2026-11-10-78718-numerical-prefix-long-fourier-benchmark.md`，R90写数学恒等式。

尾部也可选 `--tail-jacobian fourier|fourier-root|original`，默认original。
Fourier选项只是让client选择另名
`78718-prefix-tail-geometric-fourier-worker.mjs` 和其product-Jacobian/
variational-flow模块；不新增cfg物理键，保原state RHS/root和真DN流程。
实际worker及额外源SHA写入mode-run和完整tail包，ready必须明确宣告选择。
`fourier-root`另选择完整根Gram/变分工厂，同一组合worker可显式选
`--tail-predictor tangent|linear`，默认linear。tangent当前要求一个Fourier
尾后端；它只用本次已收敛轨道的Js改下一初猜，首次bootstrap仍用原warm。
本批代码没有启动过整次DN，实际M15/W22/N512命令、资源范围和纯准备结果见
`2026-11-10-78718-numerical-m15-w22-fast-route.md`。

generic每次inner返回会在下一真DN前保存独立的UNSOLVED outer候选，
原cubic和节点无损保留，物理quintic按原最终公式另算；详见
`2026-11-10-78718-numerical-inner-snapshot.md`。这些观察和数值选项都不是
必须通过的额外研究门。

## 5. 这批真实已执行范围

**8a1b5a自然exit0**：旧UNSOLVED M15 matched-cut warm + 本轮真M15首tail，
以M15/N512和W22/N1024真正准备2633点初猜，cut H差0.0、最大前缀权2048；
0DN/0BVP。报告
`2026-11-10-78718-numerical-m15-w22-geometric-prepare-01-mode-run.json`，
9915字节 / SHA `a7b8b35fec33c1366b5a0a67fbfff19087ae7b1a6414946b381cc16875a19b0f`。

**b86951自然exit0**：对(3,5)、(15,22)、(22,22)三个小型线性响应，独立
对view前向结果作二进有限差分，与view所给Jacobian逐项恰相等；高目标
模式为0、两个均值导数行保留。没有任何物理DN或BVP。
源与报告在 `2026-11-10-78718-numerical-projected-tail-interface-check.{py,json}`，
JSON SHA `e0a95249bdd73d2d1a911d904f6557fa56f823c505cc09e10bdd59c5c579fe05`。
这些是实际已做的范围，不要求启动前重复。

## 6. 主返回后的最短prefix调用

通用后端 `78718-closed-mode-backend.py plan` 读实际成功CP，随后仅依次
`run-stage --stage prefix-base`、`prefix-target`、可选`prefix-inlet-lower`，
便能以R83必要条件先排除保入口扩张；`prefix-base-metric`随后给完整连续
上界。无需先做尾export，更不用重取旧M12大参照包。
完整具体命令与其余闭图/网格路线见
`2026-11-10-78718-numerical-generic-backend.md`。
