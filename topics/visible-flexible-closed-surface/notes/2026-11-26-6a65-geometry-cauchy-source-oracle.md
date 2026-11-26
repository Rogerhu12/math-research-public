# 实际 Cauchy 场与真 R205 尾的直接 oracle；独立接口 probe

## 接口身份

新程序 `6a65-geometry-cauchy-tail-source.cjs` 直接调用已有
`6a65-cauchy-global-position.cjs` 的完整 factory。
输入必须有完整有限参数向量；构造前后逐项用 `Object.is` 核对 $z$ 不变。
尾部 amplitude 和真实 cuff 高度分别读自
$z_{\rm amplitude}$ 与 $\mathrm{base.height}+z_{\rm cutHeight}$。
没有重新指定它们，也不把观察角数改成源场的 primitive 角规则。

基本六 jets $X,X_s,X_{ss},X_u,X_{su},X_{uu}$ 直接来自原位置 factory。
源码不对背景做 Fourier 或 Hermite 投影。
若核心 cut 是 $S$，则真正半曲面还包含

$$
S\le s\le S+.48,\qquad r=.8-(s-S),
$$

并由原 `referenceFactory(A).tailPoint(r,u,Z)` 返回尾部完整两 jets。
真实 cuff 为 $r=.32$；对这个实际端点显式返回 .32，
防止二进制浮点相减产生略小于 .32 的数而误报越界。

metadata 绑定 candidate、完整输入文件、完整 $z$、factory、基、位置实现和尾实现的 SHA；
另带实际 $c,S,S+.48,A,Z$、中央 $A_q$、source 的 primitiveAngles、
完整径向基与物理度量定义。它不证明输入曾经通过什么优化或连续域证书。

## 更高混合 jets

为消费自然周长二阶链和完整短窗 Hermite 改接，`deep:true` 还返回
$X_{ssu},X_{suu},X_{ssuu}$。
令 $X_u=aT$，保持原 source 的角函数、相同 mean-phase 与 Gauss8 分片规则，
对其作显式的一阶 $u$ dual 运算，得到
$T,T_s,T_{ss}$ 以及它们的 $u$ 导数。
随后使用

$$
\begin{aligned}
X_{ssu}&=a_{ss}T+2a_sT_s+aT_{ss},\\
X_{suu}&=a_sT_u+aT_{su},\\
X_{ssuu}&=a_{ss}T_u+2a_sT_{su}+aT_{ssu}.
\end{aligned}
$$

这些是同一角场的解析微分，不是把独立拟合的高阶表拼接到背景上。
每次 deep 采样同时报告这套计算与原 $X_u,X_{su},X_{uu}$、
原 mean-phase 的差，可在真正 checkpoint 消费时核对。

## 常驻 JSONL 协议

```sh
node --expose-gc 6a65-geometry-cauchy-tail-source.cjs \
  serve /absolute/topic/scripts candidate.json actual-checkpoint.json
```

stdin 每行一请求，例如

```json
{"id":"meta","method":"metadata"}
{"id":"row","method":"sample","s":0.2,"u":[0,0.173,1.4,3.641],"deep":false}
```

每行对应一个带相同 `id` 和 `ok` 的 stdout JSON。
sample 返回 `radius:{a,as,ass}`、六个向量数组、
自身有限 metric/curvature/immersion/held 观察；
deep 额外带三个混合 jets 和一致性差。
`clear` 请求释放最后一个截面缓存。
另有 `probe`、`archive` 模式，输出原场数据与完整身份；
raw 文件只允许写在仓库外。

## 本地实际核验用的是新 probe，不是 CI state

CI 的实际 raw 继续只留同一 runner。
本地没有下载、复制或重构它的 checkpoint。
按公开 candidate 和本次公开 recipe.config，
本条另造所有自由 theta/phi/height/rho 系数均为零的明确新 probe；
cut-height 与 amplitude 保留这个 recipe 的参数
$A=.8746432018013935$、$Z=.51$。
它有 1788 列，primitiveAngles 128，中央 gap1。
它不是当前 CI 曲面，没有完整 value baseline 或 LM 接受。
输入和 metadata 都明确标记 `interfaceProbeOnly`；
没有继承任何 CI 的 metric、曲率或 held 指标。

程序 `6a65-geometry-cauchy-oracle-interface-check.cjs` 实际自然 exit 0，
内部用时 1.42 秒。核验包括：

- 7 个物理截面上的 8 个全圆角点，其中有非节点角；
- core cut 与原 R205 的完整六 jets 差至多 $1.094\times10^{-14}$；
- 真 cuff 与平圆端口的六 jets 差全部为零；
- deep 计算与原 $X_u,X_{su},X_{uu}$ 最大差 $8.216\times10^{-15}$，
  mean-phase 差为零；
- 一个非节点位置 $s=.3050192,u=.7131234$，
  用两个步长的五点中心差分核三个混合 jets，
  最大相对差 $2.630\times10^{-11}$；
- 真实常驻子进程的 metadata、cuff 两个 JSONL 请求自然 exit 0，
  输入身份匹配、cuff radius 为 .32、六 jets 都存在。

这个 probe 没有检验一般非零系数的全部状态；
真正同 job checkpoint 的有限值与更高 jets 一致性必须在消费时另行记录。
它提供的是已实际跑通、具有完整边界和物理参数身份的接口。

## 实际文件哈希

| 文件 | SHA256 |
|---|---|
| oracle 源码 | `f5036c5f2df96ee75ef970a6f6f9c21bb7bb9447e623abd1674759736a14e440` |
| 独立接口核验源码 | `fae4b5f0965f2df62cabc31e3dbdfc90c4902dcbb1d6ec25d437d08ccc278cde` |
| 新 probe 输入 | `caea08fb40e0d431bbd9dad90d833f20ea50cd5f0798df8cd0435426e7b54750` |
| 实际核验报告 | `66e38541e3d6cc9fe4ff81059f40644d4ddf65b0be1d378d6546f56a9323e027` |
| 公开 candidate | `9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d` |
| 公开 recipe | `4c929d16fa8304918338df1b7952f5219ab12eaf985a450f86ac022f0e4ac517` |
