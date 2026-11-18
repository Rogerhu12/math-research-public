# n4：独立小修正根的两臂三段流对照

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 结论与范围

在已经冻结的 stage 43、38、175 三个完整输入上，A 臂只把隐式点根未知量改为独立的 $\ell=L-\mathrm{target}$，使前两段相对既有 MP90 读数的最大归一流误差分别从 $3.37198\times10^{-9}$、$9.59210\times10^{-9}$ 降到 $1.30829\times10^{-9}$、$2.44455\times10^{-9}$；stage 175 的主导误差没有改变。B 臂再分离 RHS 的字面系数线性项与非线性修正，在前两段均不及 A。

这只是固定 binary64 系数、原 RK 分段与原阈值常数下的有限算术对照。两臂均没有运行全尾、流 Jacobian、DN、prefix 或完整几何审计，没有生产安装，也没有新的实际尾接受。MP90 是此前独立执行并与 MP60 比较的读数，不是严谨误差界或真 ODE 证书。

## 冻结身份及唯一改动

输入仍来自 `one-ulp-tail.json.gz`，SHA256 `b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e`。该状态已经经过原 Newton 更新，不能再描述为只改一个邻数的状态。模型为 spacing 4、M20、parts32、N512、原 RK16；每个 stage 的输入和输出均含完整 42 分量，最后两项为 mean 状态。完整目标 H、物理配置、原 grid/trig/profile/系数均沿用已冻结 capsule。

本次执行源为 `scripts/resume_n4_tail/probe_shifted_root_stage_flow.py`，SHA256 `fa4c6187031cee0b6828ec5b2af29be1c5c0f1c46ee3fa80aa485c061f1fbf34`。执行前冻结的两臂计划 SHA256 为 `5a009eb533917fbfa9f7e454fd611d54205bfd84e2207a6a869612471006efc0`。基类、V8 标量桥、capsule、已经通过 126 个输出及全部记录事件字节核对的 float baseline，以及既有 MP90 文件都由计划和记录绑定。本次未重复 baseline 或 MP 运行。

原点根残差为

$$R(L)=L+\mathrm{quad}(L,Q)-\mathrm{target}.$$

A 臂令 $L=\mathrm{target}+\ell$，保存独立的 $\ell$，以

$$\widetilde R(\ell)=\ell+\mathrm{quad}(\mathrm{target}+\ell,Q)$$

进行点根 Newton。实数算术下两式等价，$dL/d\ell=I$，因此原点根矩阵及 Cholesky 仍适用。A 的 RHS、投影与 RK 运算树继承原实现。

B 臂使用同一 $\ell$ 点根，并把 RHS 改写为冻结字面系数的线性作用及 $\ell$、nonlinearFlux 修正之和。若 $\mathrm{TF}$ 为 targetFactor、$\mathrm{pref}$ 为 fluxPrefactor，则其四个线性系数为

$$
A_{11}=\sigma(m^2-4),\quad
A_{12}=\sigma\,qLNum\,\mathrm{TF}/r^3,
$$
$$
A_{21}=\mathrm{pref}\,m(m^2-1)pNum/pDen,\quad
A_{22}=4\sigma-\mathrm{pref}\,m^2\mathrm{TF}.
$$

修正项分别为 $\sigma qLNum\ell/r^3$ 和 $\mathrm{pref}\,m(-m\ell+\mathrm{nonlinearFlux})$。没有把独立舍入的 `pref * targetFactor` 当作恰好等于 $\sigma$；原 angular rows 仍读表示后的总量 $L$。两臂都没有加入 Kahan/Neumaier 补偿。

原 floor、30 次迭代上限、20 次减半、$8\times10^{-14}$ 停止容差及 $5\times10^{-12}$ fallback 容差保持。必须区分“阈值常数相同”与“浮点停判逐位相同”：本次使用的稳定残差 `ell + quad` 和原 `moments - target` 在 binary64 下不同。每次返回同时保存 stable residual 和 formed-moment residual；不声称原浮点停止路径身份。

## 已保存输出的完整比较

下表误差由完整 42 输出与既有 MP90 输出相减得到。物理归一误差按原前 20 分量、后 20 分量的 portRatio 和该段归一尺度计算；两个 mean 分量另行全量比较。

| stage | 原流对 MP90 的最大归一误差 | A：只移根 | B：再拆线性项 |
|---:|---:|---:|---:|
| 43 | $3.371978087586687\times10^{-9}$ | $1.308286581988172\times10^{-9}$ | $2.697639096500749\times10^{-9}$ |
| 38 | $9.592101763097453\times10^{-9}$ | $2.444545120703848\times10^{-9}$ | $8.864090125397875\times10^{-9}$ |
| 175 | $1.352021999967683\times10^{-8}$ | $1.352021999967683\times10^{-8}$ | $1.352021999967683\times10^{-8}$ |

完整 42 分量的最大绝对误差，A 为 $7.2072285967\times10^{-13}$、$1.3853323461\times10^{-12}$、$7.8940835024\times10^{-16}$；B 为 $1.4861041845\times10^{-12}$、$5.0233111532\times10^{-12}$、$7.8940835024\times10^{-16}$。两个 mean 的最大绝对误差在两臂均为 $2.4705127628\times10^{-21}$、$6.9174357359\times10^{-21}$、$4.9692599572\times10^{-20}$，与原流相同。

每段均完成 64 次点根；三个 stage 的每次更新数分别仍为 2、2、1，无 fallback。紧凑记录保留每段 stable 与 formed-moment 的最大相对停止残差，以及全部输出身份和资源记录哈希。

## 固定目标残差不能替代算术误差

A 对固定 target node 的三个归一残差为 $5.36560\times10^{-9}$、$5.61710\times10^{-9}$、$9.50741\times10^{-10}$；B 为 $3.71464\times10^{-9}$、$1.20366\times10^{-8}$、$5.57075\times10^{-12}$。尤其 B 的 stage 175 固定目标残差很小，但该段对 MP90 的主导误差仍为 $1.35202\times10^{-8}$。这说明不能按“更接近一个固定 target”选择算术公式；本次判据始终为对既有 MP90 的完整输出误差。

## 执行与可复核来源

A、B 分别在独立目录 `n4_work/parts32-shifted-root-only-v1`、`n4_work/parts32-shifted-root-linear-v1` 执行。observer 对 session 57523、12653 均记录真实 child exit 0，终态时间均为 2026-11-18 01:28:25 UTC；耗时分别约 6.005、6.003 秒。没有用失联、日志停顿或中间值推断终态。

`scripts/resume_n4_tail/record_shifted_root_comparison.py` 只读取完成文件，核对执行命令与冻结计划、所有来源哈希、完整输入/输出、两类点根残差，并在 140 位读数精度下重新计算 MP90 比较标量。它不调用数学流。对应紧凑记录为 `scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_shifted_root_comparison.json`。场、节点、完整 trace 与可再生表保留在 scratch；记录只保留来源、命令、哈希与标量。
