# 两个实际胞元的归一化比例二阶导数严格预算

**已证明的范围：** 同一 `26e53e8c...` pulse 基场、同一精确度量、同一构造 $q_{4096}$，对实际胞元 458 和 817 的全部径向位置，严格包围 $\lambda=a/b$ 的 $|\lambda-1|,|\lambda'|,|\lambda''|$。胞 817 按 R641 的精确分界分成 before/after 两片，最终取并。这里只提供规范化比例的三 jet；本条自身不声称曲率、reach、全 818 胞或闭曲面已认证。

| 完整范围 | $|\lambda-1|$ | $|\lambda'|$ | $|\lambda''|$ |
|---|---:|---:|---:|
| 胞 458 | $5.124188388888559\,10^{-13}$ | $1.1871816398481187\,10^{-11}$ | $1.4893824913661438\,10^{-7}$ |
| 胞 817 全胞 | $1.6732386559085348\,10^{-12}$ | $1.7896051171227986\,10^{-10}$ | $3.454575557585751\,10^{-5}$ |

表中为程序报告的向外 binary 上界；每个区间盒按 $\lambda\in[1-d_0,1+d_0]$、$\lambda'\in[-d_1,d_1]$、$\lambda''\in[-d_2,d_2]$ 解释，构造端点时继续向外舍入。

## 1. 保留小残差的导数恒等式

沿 R641，$G=|F_\varphi|^2$、$q=\sqrt G$、$b=\langle q\rangle_N$。辅助标量 $A$ 在旧段为精确原五次式，在 pulse 段为同一精确积分标量的三次 Taylor 式。定义

$$
R=AG_s-2A'G,\qquad
S=AR_s-3A'R
 =A^2G_{ss}-4AA'G_s+(6(A')^2-2AA'')G.
\tag{1}
$$

令 $h=b/A$。对每个固定构造角点直接求导，利用
$q_s=(A'/A)q+R/(2Aq)$，得到

$$
h_s=\left\langle {R\over2A^2q}\right\rangle_N,
\qquad
h_{ss}=\left\langle {S\over2A^3q}
                    -{R^2\over4A^3q^3}\right\rangle_N.
\tag{2}
$$

再令 $\Lambda=A/b=1/h$，有

$$
\Lambda_s=-\Lambda^2h_s,\qquad
\Lambda_{ss}=2\Lambda^3h_s^2-\Lambda^2h_{ss}.
\tag{3}
$$

当 $G=A^2\rho^2$ 时，$R=S=0$。式 (2) 因而保留了应当抵消的量，不把较大的 $b_{ss}$ 和 $a''$ 分开包围后再相减。它只需要共同五次式的 $F_{ss\varphi}$，不需要 $F_{sss}$ 或比 $C^2$ 更强的径向正则性。

## 2. 有限多项式均值与非线性余项

写 $q=A\rho\sqrt{1+z}$，R641 已给 $|z|\le U<1$。令

$$
m_S=\left\|\langle S/\rho\rangle_N\right\|_\infty,
\quad S_*=\|S/\rho\|_\infty,
\quad R_*=\|R/\rho\|_\infty,
$$

$$
\eta(U)={U\over\sqrt{1-U}(1+\sqrt{1-U})}.
$$

从 (2) 得完整上界

$$
|h_{ss}|\le
{m_S+S_*\eta(U)\over2A_-^4}
 +{R_*^2\over4A_-^6\rho_-(1-U)^{3/2}}.
\tag{4}
$$

其中 $\langle S/\rho\rangle_N$ 先形成径向多项式，再取 Bernstein 凸包，保留有限均值内的抵消。$S_*$ 使用 R641 的有方向 FFT、三角 Bernstein/过采样及带权角覆盖。旧五次标量时 $S$ 径向次数至多 **18**，pulse 三次 Taylor 时至多 **14**；两者物理角带宽均至多 **1280**。没有删掉最高径向或角模。

这次实际中，胞 458 的 $m_S\le5.371842\,10^{-7}$ 而 $S_*\le1.431439\,10^{-4}$；末胞 before 片的 $m_S\le1.375371\,10^{-6}$ 而 $S_*\le.714920$。直接以 $S_*$ 替均值会丢掉必要的抵消。式 (4) 对应三个分项均在原报告保存；before 片分别小于 $3.668622\,10^{-7}$、$7.979732\,10^{-8}$、$1.934203\,10^{-7}$。

## 3. $a/A$ 的二阶误差没有省略

设 $e_0=a-A$、$e_1=a'-A'$、$e_2=a''-A''$，$\beta=a/A$。准确恒等式为

$$
\beta'=\frac{e_1}{A}-\frac{e_0A'}{A^2},
\quad
\beta''=\frac{e_2}{A}-\frac{e_0A''}{A^2}
 -\frac{2e_1A'}{A^2}+\frac{2e_0(A')^2}{A^3}.
\tag{5}
$$

旧标量 $A=a$，这三个误差准确为零。pulse Taylor 以 R641 的 $|a^{(4)}|\le1300000$ 支付

$$
|e_2|\le1300000\,\frac{(\ell/2)^2}{2},
\tag{6}
$$

其中 $\ell$ 是本片精确径向长度。before 片 (6) 为 `3.96728516214905e−5`；after 片宽 $5/2^{60}$，对应 `3.056285312137948e−30`。最后用

$$
\lambda=\beta\Lambda,\qquad
\lambda''=\beta\Lambda''+2\beta'\Lambda'+\beta''\Lambda
\tag{7}
$$

支付全部乘积项。末胞 before 的主余量确实来自 (6)，没有把 $A''$ 冒作 $a''$。

## 4. 实际数据、来源与入口

伴随源为 `notes/2026-11-17-parallel-model-arclength-lambda2-cancellation.py`，SHA256：

`83ee1ba24ee0c68be8b92369cd10ee8d6932d7e480efee11caff4ddf2a550cf0`。

它只调用已冻结 R641 代表胞源 `d0661f3d...` 一次。Python return observer 在该函数执行完毕后保留已算好的区间多项式局部变量；不改原算术、输入、原报告或正在运行的全域批处理。随后独立形成 (1) 的 $S$ 和 (4)–(7)。原完整 Gram 报告也作为仓库外附属文件保存，伴随报告记录其 SHA；无需另存任何数组或另跑求解器。

| 计算 | 仓库外报告 | SHA256 |
|---|---|---|
| 458 / all | `parallel-model-pulse-lambda2-cell458.json` | `b4fd72a568ab3a7f9dea492ed9fed98b42e30a69b284433ac9f102acbb6a9ec6` |
| 817 / before | `parallel-model-pulse-lambda2-cell817-before.json` | `231a4d44e61601470aad865756450900b0276fa197644b3560b2c5fe80dacd38` |
| 817 / after | `parallel-model-pulse-lambda2-cell817-after.json` | `fa45627eea2d3bbf908b6a60a78406c360ada3c72a66fb75caf76979d717214e` |

读取字段名分别是 `lambda_minus_one_bound`、`lambda_s_bound`、`lambda_ss_bound`。after 片三界为 `1.6732386559085348e−12 / 8.942475274951117e−11 / 3.934682800953897e−7`；before 为 `1.670206238711441e−12 / 1.7896051171227986e−10 / 3.454575557585751e−5`，逐项取最大即为整胞 817 表值。

从仓库根执行，工作文件仍在仓库外。三次仅替换 `--cell`、`--part`、`--out`：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-arclength-lambda2-cancellation.py \
  --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
  --engine topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-pulse-gram-representative-cells.py \
  --interval-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
  --scalar-oracle topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-inward-integral-enclosure.py \
  --cell 458 --part all \
  --out "$WORK/parallel-model-pulse-lambda2-cell458.json"
```

构造 $N=4096$、证明 $Q=16384$、标量 4096 段在此入口固定。实际三次运行分别约 12.83、13.78、13.95 秒。报告含 wall-clock，所以重跑报告整文件哈希不承诺逐字相同。本条只提供比例盒；缩放像 $\mathcal G=c+\lambda(F-c)$ 的实际 0/1/2jet 与曲率消费已另行执行，见 [R643第6节](../results/R643-continuous-curvature-of-two-actual-pulse-cells.md#6-实际规范化曲面的同两胞曲率)。
