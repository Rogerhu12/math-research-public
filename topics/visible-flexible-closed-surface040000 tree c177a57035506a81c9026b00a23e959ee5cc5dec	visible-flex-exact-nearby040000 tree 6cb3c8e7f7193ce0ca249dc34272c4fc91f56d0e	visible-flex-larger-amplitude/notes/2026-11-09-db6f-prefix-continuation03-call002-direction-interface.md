# continuation03 call002：更小 Newton 步长的只读接口

状态：**仅静态准备；没有运行本稿的 probe、evaluate、correction、角向 root、RK 或求解器。** 作者 /root/coupled_prefix，2026-11-09。原 continuation03 继续由主会话持有；本接口不改控制器、配置、原十档线搜索或接续状态。

## 1. 已关闭输入与可检验的问题

输入是 notes/2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-03_tail_0002.json.gz，SHA256 为 eb7518a7955764f7563f365b9e1b08ea1e9346148c12b66a007650e9cca47460。它对应 $s=127/128$，原请求 jacobian=false、audit=false。response 只有 failed、lastIteration、checkpoint；没有 converged、residual、jets、audit，不能补造。

关闭的 iteration 5 给

$$
N_0=2.604516507642326,\quad
\min A=0.07763554415662655,\quad
\min D=0.9915670399254011,
$$

原 chartCondition 为 $46758.07673463052$。CP 为 $865\times30$，13 个 raw 节点与 rawStates 精确对应。这是失败前原 Newton 基点，不能当成功响应。

主会话的 root-continuation03-call002-failure-audit.json（SHA256 d72b0a1f022be5aba2e353d68089ff5cb753e3c1a28b0b6a87c45614feefdc6b）已核 83 来源、8 响应源、原请求和配置。最后十个 trial 的前八个被 moment guard 或 root 求解拒绝；最后两个完成原 evaluation，但范数上升：

| 原步长 | 原真实范数 | 状态 |
| ---: | ---: | --- |
| $2^{-8}$ | $2.760465083646105$ | residual-not-decreasing |
| $2^{-9}$ | $2.6401266603560583$ | residual-not-decreasing |

指示量 $[N_\lambda-(1-\lambda)N_0]/\lambda^2$ 分别约为 $10887.0021$、$10668.5003$。它只启发选择更小步；最大范数可能不光滑，这不是严格二阶界，也不证明小步一定可行或下降。原控制器已自行回退；本接口不把 FAILED CP 填回成功缓存。

## 2. 完全复用已有只读 probe

直接使用 scripts/db6f-prefix-tail-direction-probe.mjs。本轮重新逐字差分确认：

1. direction-core 相对当前 trial-core 只把已有 correction、scaleFor 加入返回对象。
2. direction-split 相对 trial-split 只换上述公开接口的 import。
3. 原 evaluation、correction、RK、moment root、guard .05、归一尺度及物理参数不变。仍为 M15、spacing3、N256、physicalDepth12、p8、每 stage32 步；没有任何 mode、角求积或径向加密。

冻结 source-map 是 notes/2026-11-09-db6f-prefix-tail-direction-source-map.json。旧方向诊断结果不作为当前失败态的新结果。

### 同态重建与旧 I/O

probe 读取本次显式 checkpoint，不启动 worker，也不使用配置内 initialCheckpoint 的状态。相同 M/depth/p8 的 remesh 走保存节点复制；rawLeft*8 为整数，不执行 remesh RK、不增深、不补模。

probe 保留原 boundary correction。纯 JSON 算术已核：同一 g 的已闭 call001 给实际 cut radius=.6，等于本 CP 的 rCut；使用 JavaScript 原 radius**4 和除法，15 个 $H_j/r_{\rm cut}^4-Q_{0,j}$ 全部逐值为零。CP.cutHeight 与原 request 相同，rawStates 镜像相同、所有 shape 数值有限。因此原 tail.initial(0) 只给零修正，无需关闭边界修正或改配置。

这次元数据核查不调用 profile；将来实际初始化仍须由下面的基点门确认复现，不能跳过。五个旧 I/O 键保持原字节：probe 无 worker 的 trace/iteration/trial 回调，只写自己的 out 和 direction 文件，不消费这些旧输出路径。命令显式同时给 CLOSING_TAIL_CACHE 和 source-root，避免依赖其它会话的临时 fallback。

## 3. 两阶段调用；第二阶段有前置门

同 stem 的 -launch.json 保存精确 argv、cwd、环境和全部未来输出路径，状态 PREPARED_NOT_RUN。主会话顺序持有这两个进程；本稿未启动它们。

第一阶段不传 direction 或 lambdas。原 probe 做一次 state-only evaluation、一次 variational evaluation，调用原 correction，并保存逐 stage residual 差、原线性残差以及 UNSOLVED direction。它不调用 Newton solve。

第二阶段前必须核：

- 输入/来源 SHA 未变，未来输出路径未使用；
- 第一阶段真实退出 0，输出完整；stateOnly.norm 与 variational.norm 都逐值等于 $N_0$；
- maximumNormalizedResidualDifference 为零，chartCondition 逐值等于 $46758.07673463052$；
- direction 的真实 SHA 与报告一致，内部 CP/config SHA 匹配；
- linearizedResidualMaximum 有限且逐 stage 误差已保存，不能预先当零或宣称达到原容差。

任何身份/复现门失败，保留实际结果并停止，不称后续点为原失败方向的小步。这里的门只保障诊断对应关系，不改原方程验收。

第二阶段读取同一个已保存 direction，只评价

$$
\lambda=2^{-12},\quad2^{-13},\quad2^{-14}.
$$

CLI 的精确 dyadic 字符串是 0.000244140625,0.0001220703125,0.00006103515625。不重算另一方向，不加 $2^{-10}$ 或 $2^{-11}$，不继续扫描，不把 trial 送回 worker 接受。

**原 probe 捕获每项 trial 错误，因此退出 0 只表示流程结束，不保证三项 evaluation 成功。** 有 error 而无 norm 的行须原样保留。state-only 路径不产生可作 trial 当前全域界的 minA/minD，不能把基点值抄过去。

## 4. 线性预测与未来真实结果

令 $\mathcal R$ 包括 stage、cut、远端 Robin 残差，统一用原 scaleFor(target)；$A$ 是原 variational RK 线性化，$\Delta$ 是原 correction，$e=\mathcal R+A\Delta$。在精确线性代数表示下，

$$
\mathcal R+\lambda A\Delta=(1-\lambda)\mathcal R+\lambda e,
\qquad
\|\mathcal R+\lambda A\Delta\|_\infty
\le(1-\lambda)N_0+\lambda\|e\|_\infty.
$$

probe 的 linearizedResidualMaximum 是 $\|e\|_\infty$ 的有限精度诊断，不是区间认证。下表取 $e=0$，将来必须与实测线性误差并列：

| $\lambda$ | 理想 $(1-\lambda)N_0$（显示值） | 真实 $N_\lambda$ |
| ---: | ---: | --- |
| $2^{-12}$ | $2.603880639354327$ | **未运行** |
| $2^{-13}$ | $2.6041985734983264$ | **未运行** |
| $2^{-14}$ | $2.604357540570326$ | **未运行** |

预测把保存的 binary64 $N_0$ 当精确有理数再乘 dyadic，分子分母留在来源账本；显示舍入不是严格上界。未来关闭报告应并列步长、预测、$\lambda\|e\|_\infty$、真实 norm 或错误、是否满足原严格下降 $N_\lambda<N_0$。下降也不等于原 $2\cdot10^{-9}$ 达标，不自动授权改线搜索或控制器。

## 5. 本轮实际范围

只读关闭的 JSON/JSONL 和源码差分；完成纯 JavaScript JSON 算术及有限标量分数核查。最初临时元数据命令因多写右括号在解析时退出 1，无模块导入/输出；修正命令真实退出 0。另一次准备 Markdown 的工具字符串解析失败，未触及文件系统；随后用新建补丁写入本稿。来源账本保留真实 receipt。

没有运行两条 probe 命令，没有创建 future direction、trial、solver 输出。已审数值源码、03 配置和活动文件都未修改。将来若获授权执行，实际退出和结果另记，不改本稿 PREPARED_NOT_RUN 的历史身份。
