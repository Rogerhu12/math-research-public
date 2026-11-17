# 真正物理角尾几何：完整 rho、实际 Gram 和高度规范

2026-11-17，Astra-larger-parallel-16f63c8b / geometry_amplification。

**状态：实际数值证据。** 对已接受的 $M=8,\lambda=10^{-7}$ 物理角尾场，保留完整112项固定 $\rho$，积分真实 K 并按同一径向 $C^2$ 构造读出，N512/Gauss8 到 N1024/Gauss12 的实际 Gram 为 $9.40596\times10^{-8}\to9.40745\times10^{-8}$。这不是强前缀的 $\lambda=1$ 接合，不是完整闭面、全时段或 reach 证书。

源码：[固定径向读者](2026-11-17-parallel-geometry-radial-tail-readout.py)、[完整物理角高度适配器](2026-11-17-parallel-geometry-weighted-height-reader.py)，复用 [实际高度读者](2026-11-17-parallel-geometry-tail-readout.py) 和 [角原函数 helper](2026-11-17-parallel-model-angular-reconstruct.py)。准确积分定义及实现说明见 [径向小尾读出](2026-11-17-parallel-geometry-radial-c2-tail.md)；严格正则性量词见 [height-to-geometry](2026-11-17-parallel-model-height-to-geometry.md)。本条使用实际 $F_r,F_{rr}$ 以及重构位置的 FFT 角导数，不以预测的兼容误差代替 Gram。

## 1. 实际字段和同一背景

numerical_route 的新接受场为
`parallel-weighted-tail-d4-m8-scale1e7.json.gz`，输入 SHA

```text
ca2dcbd728446dbec42326e1e8cd4f4e826cefe9c80109781ef2378f6fec8715
```

其状态不是材料角 P，而是

$$
(\widetilde P_{\sin,1},\ldots,\widetilde P_{\sin,M},
K_{\cos,1},\ldots,K_{\cos,M},c_\phi),\qquad
\widetilde P=\rho P=\frac{h_\phi}{rw}.
$$

JSON 的 `rho_cos_coefficients` 含完整112项。适配器全部保留，使用

$$
P=\widetilde P/\rho,\qquad
T=\widetilde P_\phi/\rho^2-
\widetilde P\rho_\phi/\rho^3,
$$

并对字面 $Q_N(\rho B)=0$ 求根及隐式微分；没有将112物理模误换成112材料模，也没有将非零加权均值当成零。独立以完整链式导数检查三处实际半径，均值导数残差在 $8.8\times10^{-15}$ 以下。

新固定背景为 `parallel-prefix-tail-d4-s64-w06-k6.json`，SHA

```text
362509077ff7b1ce5011c838b73b5de056ced76257295be5ca53d5e6ddb357ce
```

浅端高度锚定真实 **物理 $\phi$ 均值** $.9703876955889461$。它不等于材料角均值 $.9196724087226285$；不能将其中一个均值和另一个坐标的 K 零模混用。这里 $\lambda=10^{-7}$ 仅缩小非均值浅端数据，因此仍不是强前缀的 $\lambda=1$ 接合。

## 2. N512/Gauss8 的实际完整读出

3889个原子单元、19,911,680个角—径向点上：

| 量 | 实际采样值 |
|---|---:|
| 最大 Gram 算子 | $9.4059605105\times10^{-8}$ |
| 最大径向 Gram 分量 | $8.89\times10^{-16}$ |
| 最大交叉分量 | $4.55\times10^{-11}$ |
| 最大主曲率 | 5.99786883419 |
| 同点背景径向曲率 | 5.99785849063 |
| 最小 Gram determinant | .051229304642 |
| 最小 $L$ | .683783048791 |
| 最小平面外向速度 | .999999787749 |
| 最大接点 $F_r$ 差 | $2.17\times10^{-19}$ |
| 最大接点 $F_{rr}$ 差 | $5.66\times10^{-14}$ |

本次新 k6 背景未出现上一小 cut 的11倍曲率峰。最大 Gram 点在深端最后一单元附近，$r=1.6991050014279583$，主要是角向长度误差。完整 $\rho$ 的采样范围为 $[.1660203899354,4.6138611293463]$。

## 3. 同场 N1024/Gauss12 精化

固定同一个接受字段、背景、全部 $\rho$ 系数与高度积分锚。55,752,704个角—径向点的实际结果为：

| 量 | N512/G8 | N1024/G12 |
|---|---:|---:|
| 最大真实 Gram 算子采样 | $9.4059605105\times10^{-8}$ | $9.4074531837\times10^{-8}$ |
| 最大交叉分量 | $4.54761\times10^{-11}$ | $1.69664\times10^{-12}$ |
| 最大主曲率采样 | 5.99786883419 | 5.99787427992 |
| 同点背景径向曲率 | 5.99785849063 | 5.99786396186 |
| 最小 Gram determinant | .051229304642 | .051229301301 |
| 最小 $L$ | .683783048791 | .683783048784 |
| 最大 $F_r$ 接点差 | $2.17\times10^{-19}$ | $6.94\times10^{-18}$ |
| 最大 $F_{rr}$ 接点差 | $5.66\times10^{-14}$ | $5.66\times10^{-14}$ |
| 深端高度均值 | 1.2627007534707082 | 1.2627007534707082 |

径向 Gram 两次均在 $8.89\times10^{-16}$ 内。精化后最坏点在 $r=1.6991050936566396$、$\phi=0$，仍是深端附近的角向长度偏差。没有声称误差单调下降，也没有把几何积分/角求积加密当作新的 BVP 接受。有限 mean 求积随角网一同加密，参数与原 K 字段不变。

## 4. 深端真实高度与闭盖预算的限制

本次同场积分给

$$
H_{\rm deep}=1.2627007534707082,
\qquad \Delta h_{0,\phi}=.2923130578817621.
$$

这是深度4有限 tail 的高度，不是尚未付出的完整平 cuff 高度。若暂将它用于 $R_{\rm cuff}=1.767318285443017$、半圆半径 $.145$、$C^2$ 过渡损失 $.002$ 的回头盖公式，得到直径预算约4.812865，$.960000994083/D$ 约 $.1994656$，尚未支付 $.2$ 门。真实剩余 tail 和回头盖均未生成，故该代入不作为闭面上界证书。

这说明为什么不能将材料均值下的 $K=0$ 参考高度1.212当成此物理角候选的实际 H。另一个短 bridge 背景已由 numerical_route 设计，但在它上面尚无本条所读取的接受场，本文不把仅有背景的降低高度代作成功候选。

## 5. 复现与冻结源

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-radial-tail-readout.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-weighted-tail-d4-m8-scale1e7.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-d4-s64-w06-k6.json \
  --height-reader topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-weighted-height-reader.py \
  --height-anchor left --anchor-mean-height .9703876955889461 \
  --angles 1024 --radial-gauss 12 \
  --out /workspace/scratch/16f63c8bce6b/parallel-weighted-tail-d4-m8-scale1e7-radial-geometry-n1024.json
```

首轮将角网/Gauss改为512/8。两次读取相同的已有接受输入，不重新求解 BVP；所有 raw 与报告都只放仓库外。

| 对象 | SHA256 |
|---|---|
| 径向读者 | `adc0a3e27032d966f4e193414b9646288ef0c7b191eb4e45611d5ff8134a7531` |
| 物理角适配器 | `edff3edcdbc135658d6ef22aff905ea48f59f7c25a27f607dca7a91c2f7ecc7a` |
| 共同实际高度读者 | `9606511eab76ce9a4d268af11eb62010f555753358b7f1f1ca38af6b8df44815` |
| 字面角 helper | `63844e36ba779f8847ad72464745b334394ae2a89c720b51497d5e2029a5522f` |
| N512/G8 报告 | `71aae47be801fe5e4441e8e8a4d496ca9813ac525ae02f2bb6a846c05a5ae0f8` |
| N1024/G12 报告 | `2b464f112f00bf15366e25e3a222ff8b028932e2d33ea26d103f5ed06e1deb80` |

实际强幅度仍是后续目标；本条不将极小 trace 视为闭合接口，不把尚无接受场的新短 bridge 背景写为成功候选。全场见证球、完整 D、曲率/瓶颈与全时段责任继续保持。
