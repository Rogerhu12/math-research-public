# 固定 4096 构造节点的比例三 jet 严格核：三个已认证范围的实际比较

在同一 `26e53e8c...` pulse 基场、同一精确标量和同一 $q_{4096}$ 上，直接包围有限均值

$$b(s)=4096^{-1}\sum_{j=0}^{4095}|F_\varphi(s,2\pi j/4096)|,\qquad \lambda=a/b.$$

这次只计算胞 458，以及胞 817 的 before/after 两个精确子区间。全部径向位置仍由有向 Bernstein 凸包覆盖；角点是 **定义 $b$ 本身的全部 4096 点**，不是用较少采样替代连续角证明。曲率核所需的连续角覆盖仍由 R643 的实际几何运算支付。

## 1. 与已冻结核的关系

新入口 `parallel-model-arclength-lambda2-node-kernel.py` 校验代表胞源 `d0661f3d...`，复用其未改变的以下准备步骤：固定输入身份、共同 binary 五次场、原胞的精确有理子区间限制、原有限角 Fourier 变换、精确旧五次标量、同一解析／pulse 积分 oracle 及 Taylor 余项。

生成入口把角求值数固定为 4096，保留 $T=F_\varphi$ 的三个分量，去掉未用于有限均值的 $F,F_s$ 求值、非线性残差的角插值、primitive 和 16384 全角覆盖。所有径向多项式的次数都保留。新入口的生成核 SHA256 为

`c9f4c46610555cbe351de378fe9bd8355c9407919d75237496e5997a0da44713`。

取 $\rho_j=\rho(2\pi j/4096)$。它的最高物理频率为 $640<4096$，故有限均值 **准确** 满足 $\langle\rho\rangle_{4096}=1$。各 $\rho_j$ 的有向区间下界为 `0.16601843096426755`。这里无需连续角度的 $\rho$ 下界；正性、平均和所有后续除法均针对同一组定义节点。

## 2. 保留均值抵消

用 R643 §6 相同的 $A$、$G=|T|^2$、

$$D=G-A^2\rho^2,\quad R=AG_s-2A'G,\quad S=AR_s-3A'R.$$

对每个构造节点，$D/\rho,R/\rho,S/\rho$ 都是径向多项式。先对这三者逐系数作有限有向平均，再取 Bernstein 凸包，得到 $m_D,m_R,m_S$；另外对 $D/\rho^2,R/\rho,S/\rho$ 逐节点取 Bernstein 凸包得到 $D_*,R_*,S_*$。相应的径向最高次数为：

| 标量段 | $D$ | $R$ | $S$ |
|---|---:|---:|---:|
| 旧精确五次 | 10 | 14 | 18 |
| pulse 三次 Taylor | 10 | 12 | 14 |

因这些量仅用于有限平均，每个节点上统一的
$U=D_*/A_-^2<1$ 已足够。令

$$\eta(U)=\frac{U}{\sqrt{1-U}(1+\sqrt{1-U})},\qquad
e_q=\frac{A_+\rho_+U^2}{8(1-U)^{3/2}}.$$

则 $|b-A|\le m_D/(2A_-)+e_q$。后续完全沿用已证明的恒等式

$$h=b/A,\qquad
h_s=\left\langle\frac{R}{2A^2q}\right\rangle_{4096},\qquad
h_{ss}=\left\langle\frac{S}{2A^3q}-\frac{R^2}{4A^3q^3}\right\rangle_{4096},$$

以及

$$|h_{ss}|\le\frac{m_S+S_*\eta(U)}{2A_-^4}
 +\frac{R_*^2}{4A_-^6\rho_-(1-U)^{3/2}}.$$

$\Lambda=1/h$ 和 $\beta=a/A$ 的全部乘积项、$a-A$ 的 0/1/2 阶 Taylor 余项均保留，最终 $\lambda=\beta\Lambda$。新核还以两个各自完整合法的 $|\lambda'|$ 上界取较小者：直接对数导数式及 $\beta'\Lambda+\beta\Lambda'$。该操作不丢弃任何误差。

这里不需要对 $R,S$ 作非线性 Fourier 变换，也没有 alias 假设。只在直接求 $T,\rho$ 的有限角多项式时使用已冻结的有向 FFT。全部平均权为准确二进制数 $1/4096$；每一步四则运算、平方根和所有 Bernstein 转换均沿用 R638 的向外舍入。

## 3. 三次真实输出

下表列实际向外 binary 上界。各区间内的 $\lambda$ 三 jet 均是 uniform 界，消费时对 $1\pm d_0$ 继续向外舍入。

| 范围 | $|\lambda-1|$ | $|\lambda'|$ | $|\lambda''|$ | 新／旧实际秒数 |
|---|---:|---:|---:|---:|
| 458 / all | 4.863926540356843e−13 | 1.1851153563982787e−11 | 1.4893731887841842e−7 | 2.172 / 12.829 |
| 817 / before | 1.6129269311598574e−12 | 1.7342798789195596e−10 | 3.45228957913458e−5 | 2.211 / 13.784 |
| 817 / after | 1.6156711052936752e−12 | 8.391420553613823e−11 | 3.707311028413336e−7 | 1.991 / 13.946 |

三次的三项界都不大于原 `83ee1ba2...` 伴随源的结果。817 before 的 $|\lambda''|$ 仍主要由 $a''-A''$ 的 `3.96728516214905e−5` Taylor 预算决定，没有改变实际标量来压低这一项。精确分界仍为
`1152921504606846971/1152921504606846976`，其后到 1 的真实微小子区间没有舍去。

整胞 817 可用三界逐项最大：
`1.6156711052936752e−12 / 1.7342798789195596e−10 / 3.45228957913458e−5`。

耗时只是这三次实际运行的观测，不是复杂度或其他机器性能保证。尚未运行新的全域比例三 jet 批次；原 819 片 Gram 批次源、参数和运行均未改变。

## 4. 冻结来源与重现

新源 SHA256：`e6ddb8c54093b27b03984dac56f86c2864dac0d167c74f133600d50533427927`。

| 仓库外报告 | SHA256 |
|---|---|
| `parallel-model-pulse-lambda2-nodes-cell458.json` | `dcee02943ade86bfd901a683d770624175479f676e440a2e6bd8c942ec9af44d` |
| `parallel-model-pulse-lambda2-nodes-cell817-before.json` | `c032f182eda7a59d597d6850df684dad417a1cf7f2b1a3b8b76e5753c1c98372` |
| `parallel-model-pulse-lambda2-nodes-cell817-after.json` | `c2cc44297a9af8b2e700b2b774a40969ccb5c5189e335bca9689cbac42f31453` |

从仓库根执行，`WORK` 为仓库外工作目录。复用 R637/R641 的完整固定基场重现配方。旧比较报告可由 R643 §6 的冻结伴随源再生；省略 `--reference` 只去掉比较元数据，不改变新界的计算。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-arclength-lambda2-node-kernel.py \
  --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
  --engine topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-pulse-gram-representative-cells.py \
  --interval-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
  --scalar-oracle topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-inward-integral-enclosure.py \
  --cell 458 --part all \
  --reference "$WORK/parallel-model-pulse-lambda2-cell458.json" \
  --out "$WORK/parallel-model-pulse-lambda2-nodes-cell458.json"
```

另外两次只替换 `--cell 817`、`--part before/after` 和对应的输入比较报告／输出名称。构造节点数和标量积分段数均在入口固定为 4096。报告记录完整依赖、生成核 SHA、区间端点和所有预算。原始 JSON 留在仓库外；报告含实际运行时间，因此重跑不承诺整文件 SHA 相同。
