# R189 对 R190 完整半径设计字段的嵌套补充

**状态：已证明，并有一次非零完整共同点 V8 小核。** 本文只扩展 R189 的实际注入，不修改 R190 provider、正在优化的参数或物理约束。

源码 `scripts/fd2d_r190_prolongation.cjs`，SHA256
`38d90cadd9c6f085278ff33f2829c0968a30c60455b0feee6410b501e2f992c2`。
所读实际 provider 为 `scripts/fd2d-direct-position-designed-metric-provider-R190.cjs`，SHA256
`cc45895fcf75972ee4339e5b86da70aaa589cb6491b2dbb29da26f1409771abb`。

## 1. 完整真实布局

R190 保留 R187 的两角、高度修正和末高块，另在末高后追加 $J$ 个半径系数：
$$
z=[\theta_{JK},\phi_{JK},Z_J,z_*,\rho_J],
\qquad
n_0=2JK+J+1,\quad n=n_0+J.
$$
半径是真实完整函数
$$
a_\rho(s)=a_{\rm base}(s)+\sum_{j=0}^{J-1}\rho_j B_j(s).
$$
基 $B_j$ 与 R189 完全相同，$h=(S-c)/(J+3)$。代码没有另一个自适应半径 knot 图或只在节点定义的半径。

把 $J$ 变为 $J^+=2J+3$，每个旧半径系数同样按
$$
\rho^+_{2j+r}\mathrel{+}=\frac1{8}{4\choose r}\rho_j,\qquad 0\le r\le4
$$
注入。R189 的两尺度恒等式立即给出完整 $a_\rho,a_{\rho,s},a_{\rho,ss}$ 准确相同。与此同时用原 R189 映射注入两角与高度并补零高角模，因此完整 $T,Z$、full primitive 及 $X$ 的六个位置 jet 全部保持。

这是同一实际物理度量和同一实际图的空间注入。其后的优化若改变 $\rho$，则是重新设计物理 $g=ds^2+a_\rho(s)^2du^2$，不能把该下降称为固定 $g$ 的加密收敛。要做最终固定 $g$ 的检验，应在每次注入后保持完整新半径系数块不变，只优化允许的图变量；本模块不擅自启用或取消这种约束。

## 2. 半径系数盒的完整保持

R190 的现有充分搜索域是 $|\rho_j|\le C$，其中 $0<C<.8$。对每个固定的新索引 $i$，只有与 $i$ 同奇偶的 $r$ 参与。完整内部行的权和分别是
$$
\frac{1+6+1}{8}=1\quad(i\text{ 偶}),\qquad
\frac{4+4}{8}=1\quad(i\text{ 奇}).
$$
边界行只是删掉一些非负项，权和至多 1。把缺失的权补在值为零的虚拟系数上，每个新系数都是旧系数与零的凸组合，故
$$
\max_i|\rho_i^+|\le\max_j|\rho_j|\le C.
$$
该结论可逐层重复，不需要放宽原盒、不需要缩小旧控制，也不需要裁剪新控制。

对完整 cardinal cubic 平移族，有 $\sum_{j\in\mathbb Z}B_3(t-j)=1$。可从单位区间示性函数的整数平移分割和其三次单位积分卷积直接推出；最终函数连续，所以端点值也成立。当前有限基组是其非负子集，于是 $\sum_jB_j(s)\le1$。若原已付基准 $a_{\rm base}\ge.8$，同一盒给
$$
a_\rho(s)\ge.8-\max_j|\rho_j|>0.
$$
注入保持实际函数，也保持这个充分半径下界的系数证明。

## 3. 为什么半径用准确 dyadic 累加再舍入

普通 binary64 顺序求和可能在盒边界产生一 ulp 的人为越界。此处没有改变数学掩码，也没有扩大 R190 的原判断。

每个有限 binary64 输入都被明确拆成整数乘二次幂 $m2^e$。掩码为整数分子除以 8，因此一条新半径系数的未舍入值可由 BigInt 移位、整数相加准确计算。随后直接按最近、偶数规则舍入到 binary64：

- 正常数保留至多 53 位有效二进制位；
- 次正规数以 $2^{-1074}$ 为量化单位；
- 被舍弃部分与半个单位准确比较，等距时按末位偶数决定。

最终整数与二次幂的乘积已经是目标可表示数，不再隐含另一次数值近似。这个舍入映射单调；若准确结果在 $[-M,M]$ 内，且端点 $M=\max_j|\rho_j|$ 本身是可表示数，则舍入结果也在该闭区间内。因此本实现连原 binary64 系数盒也保持，**未作 clip**。

这不宣称浮点新系数代表的完整函数与旧函数逐位相同。准确实数注入由掩码恒等式定义；新可执行参数缓存是其最近 binary64 版本。高度和角系数沿用 R189 的原普通浮点求和；共同点误差如实测量。每次半径注入检查实际新最大系数不超过原最大系数，若违反会报明确实现错误，不悄悄改数值。

## 4. 可用接口

```javascript
const {prolongR190State} = require("./fd2d_r190_prolongation.cjs");

const injected = prolongR190State(z, oldProvider.definition, {
  radialRefinements: 1,
  modes: 15,
  angles: 128
});
const nextOptions = {...oldOptions, ...injected.providerOptions};
```

返回：

- `vector`：新完整向量；
- `definition`：原实际定义中只更新维数、基数、角阶/求积数和明确布局；
- `providerOptions`：新 $J,K,N$ 及未变的半径系数界；
- `provenance`：掩码、原/新维数、原/新最大半径系数、实数恒等与浮点范围。

不能用归一后的 `centralGap` 替代原请求中的 `gap` 重新求中央曲线。engine、bundle、原边界 gap、$c,S$ 与参考全部保持。$J12,K7$ 的 R190 向量为 193 维；细化到 $J27,K15$ 后为 865 维。

新 provider 的径向 Gauss2 目标会改变；若同时角求积 $64\to128$，primitive 的有限求积也改变。必须在同一实际注入态上重新算新 baseline/normal，不沿用原范数或预测方向。

## 5. 实际小核与一次 loader 失败

完整记录见 `notes/2026-11-12-fd2d-R190-prolongation-v8-check-01.json`。使用实际冻结 R190 源、B32 candidate 和明确非零确定性向量，不冒充主线接受态。只在五个共同径向点暴露原 `makeSlice/sliceValues` 的只读入口；未改其运算，未调用 whole objective、normal 或 JVP。

实际 V8 核耗时 158 ms：

- 193 到 865 维，原数组不变；
- 半径 0–2 jet 的最大 scaled 差 $1.47812\times10^{-13}$；
- 同原 angular rule 的完整 $r_E,r_F$/metric/immersion 差至多 $3.77476\times10^{-15}$；
- 双倍 angular rule 的差单列，为 $4.05232\times10^{-15}$；
- 24 个正/负盒边界及次正规数细化情形全部保持原系数界；
- 11 个正常、次正规、最大有限数的 dyadic 解码/舍入往返正确；
- 非零例的最大半径系数由 $.0699946280$ 变为 $.0684466770$，是凸平均系数变化，实际完整半径函数仍按同一掩码恒等保持。

第一次调用在 engine 的 CommonJS `require.main` 判别处遇到 V8 没有 require 的真实异常，尚未构造 provider 或计算场。第二次仅给 loader 一个 `require.main=null` 的空 require 入口，禁止所有文件 require，源与数学完全不变，之后上述唯一非零场核真实完成。两次均未创建 OS 进程，不能写成 shell exit 0。

本组不代替完整强幅度、全时 reach 或连续 metric 证明；它给出下一真实同场细化和后续固定物理 $g$ 检验的正确入口。
