# 实际径向 C² 小尾：真实 Gram 与固定背景曲率

2026-11-17，Astra-larger-parallel-16f63c8b / geometry_amplification。

**状态：实际数值证据；正则性使用已证明的径向积分构造。** 同一 smallcut 的物理 $r$ 接受场，经积分 K 高度和径向几何重构，真实 Gram 算子采样约 $1.3\times10^{-10}$。本条只有一个带边有限 tail；没有原大幅 prefix 的 $\lambda=1$ 接合、完整闭面、全时段或 reach 通过。

源码：[径向几何读者](2026-11-17-parallel-geometry-radial-tail-readout.py)，复用已发表的 [实际高度读者](2026-11-17-parallel-geometry-tail-readout.py) 和 [字面角原函数](2026-11-17-parallel-model-angular-reconstruct.py)。数学定义、$C^2$ 量词及初值项详见 [height-to-geometry 说明](2026-11-17-parallel-model-height-to-geometry.md)；本条不重复其理论结论。

## 1. 唯一被数值积分的几何

沿用 [四列实际 Gram 对照](2026-11-17-parallel-geometry-actual-tail-gram.md) 中积分 K 的高度。所有非均值高度系数以浅端真值锚定，对实际 $w k_j$ 作积分，故 $h$ 的真实二阶径向导数只需 $w'$ 和实际 $k_j'$。普通物理角高度均值由同一个加权 mean 根积分。

在固定物理角 $\phi$ 中，定义

$$
P=\frac{h_\phi}{r\rho w},\quad K=\frac{h_r}w-1,
\quad S=1-w^2P^2,\quad
D=1-w^2\{2K+K^2+(1+w^2)P^2\},
$$
$$
a=\sqrt{D/S},\qquad b=-\frac{w^2(1+K)P}{\sqrt S},
\qquad A_r=\frac{w^2(1+K)(K_\phi/\rho-P)}{rS\sqrt D}.
$$

浅端使用同一高度的角原函数闭圈，随后定义

$$
\alpha_r=A_r,\qquad
(F_{xy})_r=b\,t+a\,n,
\quad t=(\cos\alpha,\sin\alpha),\quad
n=(\sin\alpha,-\cos\alpha).
\tag{1}
$$

这是一个准确声明的径向积分候选。径向数值积分只是评价 (1)，而非另拟合一张显示网格。实际一、二阶径向 jet 分别为

$$
F_r=(bt+an,h_r),
\quad
F_{rr}=((b_r+aA_r)t+(a_r-bA_r)n,h_{rr}).
\tag{2}
$$

代码直接微分 $a,b$ 的代数式，不代入旧 P/K PDE。角向 $F_\phi,F_{\phi\phi}$ 则来自重构位置的 FFT 导数；没有用兼容误差的预测式代替字面导数。归一化目标准确为

$$
g_h=(1+w^2)dr^2+r^2\rho(\phi)^2d\phi^2.
$$

在 $S,D>0$ 的统一分支上，已证构造使 $F$ 为 $C^2$；**正则浸入还须实际 Gram 正定**，不由 $S,D$ 两个代数条件单独推出。本次数值另外读出了最小 Gram determinant。所有全域下界仍只按采样可信度记录。

## 2. 实际积分和接点处理

保留状态/背景节点的完整并集及左右真实 jet。每个原子单元，以 Gauss 节点插值积分连接 $\alpha$，再积分实际 $bt+an$。$\alpha$、$XY$ 和高度均值的跨单元增量使用 Kahan 补偿求和，减小数千个小步累积的舍入误差。Gauss8和Gauss12保持同一输入、同一背景、同一高度积分定义。

初始角原函数的有限误差没有设成零。它的实际转角密度误差和 $F_\phi-r\rho\sqrt S\,t$ 都写入报告。后续每个单元两端及全部 Gauss 节点都读取完整 Gram、实际主曲率和接点 $F_r,F_{rr}$ 差。

角网加密时重新评价同一原始 K 插值和高度积分；加权 mean 和角原函数的有限求积也相应加密。因此以下是明确的几何积分/角求积检查，**不是新的 BVP 接受，也不是声称一个固定有限 BVP 的固有误差已经证明趋于零**。

## 3. 原物理 r 小 cut：三次精化

输入及背景分别为

```text
4fc1a7cdcde9a6f1d0c8fb07cc61cde6dba366c3e8a13b55eaa1a4e167424648
b24084c47f03ab87af2f22edeb641d9f50b8a8bbce01d7e9578b2796c5298a3d
```

它们就是上一条的 $M=8$、$r\in[.06863598072661437,.3]$、浅端 $P_1=.001$。7191个原子单元全部读取。

| 角网 N | 径向 Gauss | 角—径向点数 | 最大实际 Gram 算子采样 | 最大主曲率采样 |
|---:|---:|---:|---:|---:|
| 512 | 8 | 36,817,920 | $1.3062173734\times10^{-10}$ | 11.0186307592 |
| 512 | 12 | 51,545,088 | $1.3062044895\times10^{-10}$ | 11.0190728705 |
| 1024 | 12 | 103,090,176 | $1.3230369379\times10^{-10}$ | 11.0190728705 |

最后一列的几何误差稳定在 $1.3\times10^{-10}$ 附近，未宣称单调下降。径向 Gram 分量最大 $8.89\times10^{-16}$；交叉分量分别约 $2.61\times10^{-13}$、$2.68\times10^{-13}$、$6.03\times10^{-13}$，所以主误差是累计角向长度偏差。1024角网的实际初始角兼容差为 $5.12\times10^{-14}$，后续最大角兼容差约 $4.54\times10^{-12}$。

最大 $F_r$ 接点差小于 $9\times10^{-19}$，最大 $F_{rr}$ 接点差约 $3.55\times10^{-15}$。最小 Gram determinant 约 $.004710897858$，最小平面外向速度约 $.99998487798$。这些接点数字核对了该积分定义的实现，没有把一个显示插值换称为 $C^2$ 表面。

### 3.1 曲率峰主要来自已固定背景

Gauss12 最坏点为

$$
r=.2825098790106652,
\quad w=.04192252361838733,
\quad w' =11.047446235411728.
$$

同点的实际主曲率为 $11.0190728705$，而该**同一个固定 Hermite 背景**的轴对称参考径向曲率已经是

$$
\frac{|w'|}{(1+w^2)^{3/2}}=11.0183862890.
$$

两者只差约 $.000687$。因此不能拿旧 scalar producer 的曲率 clamp 标签代替这份重新声明的 Hermite 背景的真实峰，也不能期待只精化 K 场就把该背景峰降到8或6。这里的曲率不适合作为新大直径闭面的 reach 父证书；其作用是实际验证几何读者并暴露背景责任。

## 4. 复现及身份

在仓库根运行，输出只放仓库外：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-radial-tail-readout.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-dynamic-d4-m8-a0001.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-tail-d4-s64.json \
  --angles 1024 --radial-gauss 12 \
  --out /workspace/scratch/16f63c8bce6b/parallel-dynamic-d4-m8-a0001-physical-radial-geometry-n1024.json
```

| 对象 | SHA256 |
|---|---|
| 当前径向读者 | `adc0a3e27032d966f4e193414b9646288ef0c7b191eb4e45611d5ff8134a7531` |
| 共同实际高度读者 | `9606511eab76ce9a4d268af11eb62010f555753358b7f1f1ca38af6b8df44815` |
| 字面角 helper | `63844e36ba779f8847ad72464745b334394ae2a89c720b51497d5e2029a5522f` |
| N512/G8 补偿报告 | `237efcce3005e9cc43ef0c51be9ace03eeb911f80962f2b16bca0ddba95796bb` |
| N512/G12 报告 | `ef38e0acb9b0a883a4c4e350ce0af30d6dc2209b9c111e515a1ebd05376af5fc` |
| N1024/G12 报告 | `d330414b24d55179c8409b980aeda642f2f595217a2b43a69047f44f0b3d3a3b` |

前两次报告的径向读者在增加一般 $\rho$ 参数前运行，SHA 为 `dd6142f6f5045184ef489a0ee5605386aae6d95c16aeaf1fcedaaf3392e2b7f0`；当前默认 $\rho=1$ 保持同一数学定义。N1024报告使用当前冻结源。所有原始状态、表和报告只在仓库外，不提交可重算数据。

这一步补上旧小尾的实际 $C^2$ 几何构造和真实 Gram，不把它当作大幅前缀的父证书。下一条[真正物理角尾几何](2026-11-17-parallel-geometry-weighted-actual-tail.md)读取另一份已接受字段和完整112项 $\rho$，两种输入不混用。完整闭合、固定握持幅度、全相位和全局 reach 责任仍未完成。
