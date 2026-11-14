# 真实头部的全部 46 列与整胞元 Green 包

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

## 本次实际支付的内容

冻结的 R26 真实源、R29 Peano–Baker/射影区间程序已覆盖 source
physical node225 至 node12 的全部 213 胞元，以及物理角频率
$m=2,4,\ldots,92$。这次没有用 M8 零填来代替高 38 列。
每个低模的真实线性深端子空间均使用 R18 (9.4) 的带宽
$|s-s_{\rm ideal}|\le\nu_m2^{-60}$。

全部 46 个浅端高度增益都严格非零，因而这一区间内的 46 维
线性深子空间确实在浅端投影成高度图。证书使用分别保存的有符号
振幅上下端点和射影方向；不能把跨度较大的正区间重新转为对称
Arb 球后包含零，误判成真实退化。最末 $m=92$ 的增益两端约为
$1.23817\cdot10^{2487}$ 与 $2.76449\cdot10^{2487}$，均严格正。
全部精确 dyadic 端点见 raw manifest 和六个列组。

这是真实固定有理深源的线性接口结论。它不把旧浮点端口当作相同
实源，也不支付完整非线性浅头或强幅曲面。

## 可重算输入与代码

线性入口及三个依赖的冻结源快照保存在
`2026-11-12-closure-real-head-interval-v2-source.json.gz`，整个归档 SHA256
为 `84a865de3bcaacb2e268617092ca0f64923ad886a87e7912279d2f804fcad514`。
本次用同一份 v2 源，没有修改已付 M8 的程序。

在课题目录执行：

```bash
/workspace/scratch/c0de65fac774/research-venv/bin/python \
  computations/closure_real_linear_head_enclosure.py \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --source-ledger notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json \
  --response notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-response.json.gz \
  --out-prefix notes/2026-11-12-closure-real-linear-q003-low46-recovered \
  --modes 46 --reference-modes 8
```

线性结果记录 10225 个自适应面板、10504 次标量积分、2198 次
源积分，elapsed 93.466607664 秒，峰值 RSS 93608 KiB。
会话 98069 的最后一次工具返回紧邻上下文压缩，其正式退出码
在当前工具记录中不可恢复；后续 poll 返回 Unknown process。
因此这里只称完整主包、summary、raw manifest 及六个列组已产出，
不捏造该会话的 formal exit 0。

后续独立 Green 消费确实正常 exit 0（会话 24209），且检查了六个
列组 SHA256、胞元顺序和全部非零增益。因此已产出的数值证书可直接
使用，无需为遗失终端退出码重新计算这些积分。

## 真实参考的全胞元源预算

参考场取保存的 node12 前八个非均值高度；其余 38 个参考高度选为零。
**这只是一个明确线性参考的定义，不声称完整非线性修正的这些高度为零，
更不省略 46 个原始深参数。** 每个实际保留的参考模在整胞元上的
$Q,\Xi$ 由真实列包围，R23 完整 mean 分支及全频非线性源再由该
整胞元强范数估计。

统一角宽 $\tau=1$ 下有

$$
X_{12}\le8.966949256767410\cdot10^{-38},\qquad
\max_n\frac{X_n}{r_n}<2.926562\cdot10^{-11},
$$

以及

$$
\sum_{n=12}^{224}B_nX_n^2
\le1.281363313698966\cdot10^{-51}.
$$

这些显示值只为阅读；推理实际使用 JSON 中外舍入 dyadic 端点。
它们是计算出的正 majorant 上界，不能把其正下端点解释为未知解
范数或源范数的正下界。

## Green 计算结果及未付的门

执行冻结入口：

```bash
/workspace/scratch/c0de65fac774/research-venv/bin/python \
  computations/closure_real_head_green_enclosure.py \
  --columns notes/2026-11-12-closure-real-linear-q003-low46-recovered.json.gz \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out-prefix notes/2026-11-12-closure-real-green-q003-low46-recovered
```

该作业正式 exit 0，elapsed 11.992134697 秒，峰值 RSS 87780 KiB。
每个模的第二列 $\psi$ 从浅端 $Q=0,\Xi_{12}=1$ 向内作真流的
余子式逆传播；完整物理 Wronskian 是
$\mu_{12}\phi_Q(\mathrm{cut})$。R29 的两端 Green 核因此消去
大 Cauchy 增益后才估计，未直接拿整个 Cauchy 矩阵范数作收缩常数。
同胞元的 $Q$ 与 $\Xi$ 分量 supremum 分别取值，再相加。

全部 46 模、213×213 胞元对的 dyadic 上界为
`gamma_log2_upper`。完整 R23 标量 $L^1_r\mathcal W_1$ 源
通过每对胞元最坏 Fourier 块后得到

$$
\eta\le
1577999014353775689658318750711133572308321097549771923853
\,2^{-172}
\approx263601.254882815.
$$

因此 R29 的 $4\eta<1$ 与 $8\eta<1$ 门均未通过。
这份合法上界不能给出 46 模投影问题的收缩，不能把 M8 的
$\eta<0.001967$ 转借过来。失败原因在当前充分界，未证明方程
无解；源的逐模结构被统一标量范数抹去，高列被配上了相同完整
源预算。后续保留本包不改，使用变角宽、物理变量和逐模径向源
密度继续支付实际完整问题。

## 稳定输出

- `2026-11-12-closure-real-linear-q003-low46-recovered.json.gz`
  及对应 `-summary.json`、`-raw-manifest.json`。
- 同前缀的六个压缩列组 `-columns-01-08` 至 `-columns-41-46`，
  每件小于 1.4 MB，完整 SHA256 已在 manifest 中记录。
- `2026-11-12-closure-real-green-q003-low46-recovered.json.gz`
  及对应 `-summary.json`。
- `2026-11-12-closure-real-low46-validation.json` 记录消费检查和
  该次真实终端状态边界。

上述数据对应尚未付非线性全头闭合的真实线性参考。高频深端、
R18 非线性低端误差、mean 高度、外 0..11 胞元和实际前缀匹配仍需
进入同一完整方程，不能以单个端点或有限 Robin 代替。
