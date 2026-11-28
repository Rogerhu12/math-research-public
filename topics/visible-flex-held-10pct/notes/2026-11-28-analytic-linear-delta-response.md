# R72 的完整线性 δ 响应：实际计算

2026-11-28，`Astra-held10-7c4e33ee-20261128 / analytic_construction`。

**状态：数值证据。** 本次在实际恢复的 multistage profile、完整原 ShortBridge
及原 M24 线性 DN 上，首次测得 R72 留下的主模 δ 响应和伴随积分。
这是旋转背景的二维线性方程；没有把它当成有限振幅 Schur 响应、非线性
尾、完整 BVP 接受或 10% 闭族。未重跑已登记的 v2/v3/v4/v5 失败链。

## 1. 完整计算及数值结果

在固定参考前缀坐标 ξ 上使用 R72 的原方程，联立积分

$$
X_\xi=A X,\qquad (X_\delta)_\xi=A X_\delta+A_\delta X,
\quad A=\frac r{1+rh}M_3(v),\quad
A_\delta=\frac{M_3(v)}{\delta_{\rm ref}(1+rh)^2}.
$$

初值是 $X=(1,0)^t,X_\delta=0$。前缀按全部真实 profile 接点分段；桥用
它自己的固定局部弧长，继续传播 $X,X_\delta$，没有省掉桥的转移。
Robin 行为 $\ell=(1,-C)$，其中实际
$C=.025803935943320925$。同时积出 R72 的前缀积分
$I=\int X^tJM_3(v)X/a^3\,d\xi$ 和桥的 trace 原函数。

| 量 | 本次实际值 |
|---|---:|
| 重新定位的线性根 δ | .06414432506429057 |
| 与原记录 .06414432506418023 的差 | $1.10342\cdot10^{-13}$ |
| $\mathscr R_3=\ell X_{cut}$ | $3.00063\cdot10^{-15}$ |
| $\partial_\delta\mathscr R_3=\ell X_{\delta,cut}$ | −326.4513389554927 |
| $I$ | −.17490536231904275 |
| $\gamma=X_{cut,2}$ | .002678888726307153 |
| $\det B$，由原桥 trace 积分求得 | .2999999999999972 |
| R72 式 (6) 右端 | −326.4513389478258 |
| 两种导数算法的相对差 | $2.34857\cdot10^{-11}$ |

后两列比较只在主模近共振点计算。程序不在非共振高模上使用 R72 的共振公式。
桥输入仍是原 GL64 查询器；没有把其 radius 数组与真 primitive 偷换。

直接变分积分采用 DOP853，`rtol=2e-11, atol=2e-13`；收紧至十分之一后
导数为 −326.45133895441353。主模 cut 量很小，收紧容差后在原根处的
归一化残差约 $4.96\cdot10^{-10}$，所以这里不声称根或导数已经区间认证。
步长 $10^{-5},2\cdot10^{-6},4\cdot10^{-7},8\cdot10^{-8}$ 的 δ 中心差分
与变分积分的导数相对差分别为
$1.544\cdot10^{-9},5.941\cdot10^{-11},5.718\cdot10^{-11},1.644\cdot10^{-10}$。

此外在同一 δ 上测量的高模归一化 Robin 响应
$\mathscr R_m/(\|\ell_m\|\|X_{m,cut}\|)$ 为：

| m | 归一化响应 |
|---:|---:|
| 6 | .014198432996862303 |
| 9 | −.004146282444265032 |
| 12 | −.01802682735242139 |
| 18 | −.3884636007694484 |
| 24 | −.0015103509069442115 |

这几个有限高模没有测得共振；它们不是全部高模的统一逆界。原始转移有很大
增长（例如 m=24 的 cut 范数约 $8.61\cdot10^{20}$），故不能把低维射击直接
改作完整非线性高模求解器。

## 2. 对当前续入的实际意义

R72 的线性模型中，固定 δ 的主模平面入口振幅响应正比于
$\mathscr R_3=0$；改变 δ 的响应正比于
$a_3\partial_\delta\mathscr R_3$。本次实际值支持原 δ-design 具有可用的
横截方向，支持继续已经到达 λ=.128/M48 的原 R53 完整状态割线主线。
它不说明 v5 的实际高 phase 块可逆，也不推翻 v5 在真实有限幅上已登记的
RMS/metric/域失败；不能据本次数据再重跑同一失败链。

后续正在准备同一个实际 accepted R53 场上的完整 λ 切线初猜：对原
collocation 残差 $F(Z,\lambda)$ 计算 $JZ_\lambda=-F_\lambda$，保 p0 的
加性 δ 语义、原计算 t、完整 lift、端口和均值规则。那是待实际执行的新
初猜工具，不由本条取得新的接受场。

## 3. 复现与哈希

源码：`scripts/resume_20261128/analytic/linear_delta_response.py`。

```sh
env -u LD_LIBRARY_PATH -u LD_PRELOAD python \
  topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/linear_delta_response.py \
  --repo REPO --work RESTORED_WORK --out SCRATCH/linear-delta-response.json
```

`RESTORED_WORK` 是原 `tail_recovery_setup.py` 完成的工作目录，本次实际使用
`/workspace/scratch/7c4e33ee17de/held10-design-work`。运行用时约 10.72 秒，
退出码 0。可再生完整 JSON 只在 scratch 保存；公开保留本小标量记录。

| 输入/输出 | SHA-256 |
|---|---|
| 本次脚本 | `80ce3dc7dd2e47adbf88964cc5f64933f2832a716fe00c087cbfad0d88e03298` |
| 本次输出 | `58ae750c5580bef474bb6906aea34512b8f20099b9a570e072d7185592dc57d8` |
| 原 profile | `3f4042ffe0666bf8ba5b09dca3d056f9b0604b8e4ab3367e537d924bb7b0cfcc` |
| 原 chart | `dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93` |
| 实际 M24 port | `42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b` |
| 原 ShortBridge | `7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4` |
| 原 linear flow | `0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5` |
| 原 multistage provider | `887a8d04157dfcee504f80d8cc2e7b66d9ae430775b4bc1df0bfea70bd49ceed` |

数学公式来源：[R72](../results/R72-delta-robin-response-and-phase-compatibility.md)。
