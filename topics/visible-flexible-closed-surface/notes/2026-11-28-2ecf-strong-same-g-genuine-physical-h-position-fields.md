# 强同一度量的 33、65 节点真实物理位置场

R258 给出了原 R233 位置前缀的不可消径向误差。这里沿同一固定椭圆、同一目标 $g=ds^2+f(s)^2du^2$、同一物理 ramp 长度与同一准确 Γ95 coast 端口，实际生成两组更密的原生 Cartesian 位置、径向速度与径向加速度。新数据来自同一个实际 Cauchy 积分的新增物理节点。

| 实际场 | 物理节点 | 单元 | 每节点保存的完整 P,V,A | master SHA-256 |
|---|---:|---:|---|---|
| 原场 | 17 | 16 | $768\times3\times3$ 复 Fourier 系数 | `0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7` |
| H33 | 33 | 32 | 同上 | `4fcc0542ddf34674672556a85608ac0ab56c8b34f3bd81451f6c7b75e99f0544` |
| H65 | 65 | 64 | 同上 | `479dab51bd77a211f64a256bbb16d67b4382e150af0deee7fa6baf84d8e5464a` |

原 DOP853 参数保持 $r=\mathrm{binary64}(.06)$、$v=\mathrm{binary64}(.045)$、$c=13/128$，相对容差 $2\times10^{-12}$、原分量绝对容差 $2\times10^{-14}/(1+k)^2$ 与最大物理步 $.0005$。原 master 采用 65 个真实 dense output 中每四个位置。新进程重积分后，65 个实际节点完整到达，1637 次 RHS 调用，旧 17 个节点的全部系数与原 master 最大逐项差恰为零。H33 采用每两个节点，H65 采用全部节点。两层双端保存的 $P,V,A$ 都在原 native 角中对完整 768 点 FFT，绝对加速度由同一步的 $l=(m^2+K)/n$ 和实际法向得到，位置与切向由同一真实 frame 取出。没有对旧物理五次样条插 knot 冒充新状态。

## 两种明确的位置消费

每个新格用相邻实际 $P,V,A$ 做物理五次 Hermite。中央节点仍按精确椭圆柱覆盖，终格右端仍换取 R232/R233 同一准确 Γ95 coast 出口的三个函数和完整角导数；同一旧终点 raw Fourier jet 仍逐系数保留作证明用代理。真实中央与 coast 两端接合沿原有端迹恒等式。

1. 原供应器约定可以对新场做 R233 的准确积分二次归一化。producer 报告的 `exactGeometryDefinition` 记录这个定义。两套 master 的生成阶段未支付其准确全域误差。
2. 直接在准确中央椭圆材料角 $u=a_\ell^{-1}\int_0^\theta\ell$ 下使用新 Cartesian 物理场，沿用 R227 的原生场表示。这张新的位置图保持相同目标 $g$，其交叉 Gram 项需直接支付。强前缀和后续兼容求解优先消费这一表示。全部真正右端迹匹配同一 R137 coast。第二种定义的全域度量和自身曲率需要自己的证书。

在现有 G10/G11 字面供应链的一个数值实现中，在 ramp 内可从 `WarmMaster(newRamp, oldCoast, coast_length=.02).jet(s,u)` 取得第二种表示的字面近似。此处不将它的有限反参计算与数学定义等同。新位置需要建立自己的源身份；原归一化场的样本、误差和 reach 均不直接转借。

## 可移植运行

令 `SCRIPTS` 为公开课题的 scripts 目录，`DATA` 为原 R233 定义的两个 master 所在目录，`OUT` 为新的输出目录。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$SCRIPTS/2ecf-strong-ramp-physical-h.py" \
  --scripts "$SCRIPTS" --ramp "$DATA/gap105-prefix-ramp-master.npz" \
  --coast "$DATA/gap105-prefix-coast-master.npz" --out "$OUT"
```

会话 Astra-visible-flex-2ecfcd69-20261128。实际进程 26540 自然返回 0，8.209824 秒。完整输出仅保留身份：

- 新生成入口　`763842285c4c06cad7a5f650840c719671a3b22e995a3dbef028b95f9bb4febc`
- 原完整 master 生成源码　`83bc55f4ef0977dc3cefe2332e1f2a3d4b8dbd19f3493a788719d231d1ffbb7b`
- 原 warm consumer　`75dfcbd01870df003e6814b9cb07a992df3713e01b9fcedda432a57c4569463b`
- 原准确 R137 coast master　`f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d`
- 本次 `report.json`　`a5b0cd35d0fa319a7c8a8c39fe36dd81e924486348fd0164343b8fba0c7f4801`
- 本次 stdout　`aa02c1f958573a0f6dcf27985b556728d7bf011a434db3d0a979e1e5f255f461`

报告含本机时间。可重生两个 master 与参数定义均逐项列明，不入 Git。
