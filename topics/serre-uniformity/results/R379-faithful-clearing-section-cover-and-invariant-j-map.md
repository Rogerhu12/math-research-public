# R379：真实清极截面的非椭圆盘覆盖与不变的 j 映射

**状态：已证明，全部有限环运算已完成。** 在已固定的 $X_{ns}^{+}(41)$ 实际整截面模型中，重新选择 Serre 导数的清极截面，得到一个在全部 85 个 $j\not\equiv0,1728\pmod {47}$ 的有理盘和全部 820 个忠实源点上均为单位的截面。新旧清极表达给出相同的真实导数、相同的经典不变量及 $j$ 映射。没有除以 47，也没有删除原单位断言。本条没有独自完成任何新的规范高度或圆盘排除。

## 1. 已固定的准确对象与实际障碍

记 $Q=47^4=4879681$，$R_2=(\mathbf Z/Q\mathbf Z)[i]$，$i^2=-1$。沿用已发布整模型的 $L=K_X+D$、$\deg L=126$、73 个权二坐标 $W$，以及维数 199、325 的 $V_2,V_3$。全部 820 个评价点的剩余几何点互异；这些点及其半线性 Frobenius、各次截面乘法均为原模型的数据。

既有程序 `p41_cleared_serre_derivative47.py` 构造了 21 个真实椭圆点上的消失条件。其限制矩阵秩为 21，完整整核

$$
K=H^0(L-E_2-E_3),\qquad \operatorname{rank}K=52
$$

已经求出，并证明每个清极截面 $v\in K$ 都使 $G=v\delta(W)$ 成为实际全局三次截面向量。原来的一个选定 $v$ 在 820 个源点上为单位，但这不保证它在每个额外有理盘上为单位。

这一差别在 SS_j10_14 实际出现。按原盘 $f_c=1$ 的坐标计算，旧截面值为

$$
v_{\rm old}(P)=3470668=47\cdot73844,
\qquad v_{47}(v_{\rm old}(P))=1.
$$

所以经典不变量的旧辅助分母在该点为非单位。该点本身仍有良好的真实 $j$ 值；不能把旧分式的辅助零点当成几何极点，也不能直接作非单位倒数。

## 2. 新截面的实际构造

生成器从原 52 维核中选种子 $s$，取 Frobenius 迹

$$
v_0=Ks,\qquad
v=v_0+A_1\overline{v_0},
$$

其中 $A_1$ 是同一个已发布 Frobenius 矩阵。实际验证

$$
E v=0,\qquad A_1\overline v=v.
$$

原 SS atlas 的 110 个真正圆盘中心与 19 个普通盘中心共给 129 个中心。只选出其中 $j\not\equiv0,1728$ 的 85 个中心检验；本条没有声称在应当清除的椭圆支撑处也是单位。

固定随机种子 379470 的第零个候选即同时通过：

- 全部 820 个忠实源点评价为单位；
- 全部 85 个上述有理盘中心的评价为单位；
- 全部 21 个真实椭圆点上的消失条件；
- 完整半线性 Frobenius 恒等式。

每个盘的标签、剩余 $j$ 及完整四位截面值均保存于数据文件。SS_j10_14 的新值为

$$
v(P)=3227829\equiv10\pmod {47},
$$

故该辅助问题已被实际消除。因为截面及盘坐标为整，中心处为单位也保证它在整个相应剩余盘上为单位。

## 3. 全部三次恒等式与同一个导数

在原源点物理规范下，实际 Serre 导数为

$$
\delta(W)=\beta_0^{-1}W'+96W,
\qquad \beta_0=-3/27652.
$$

原 $W'$ 的全部系数来自已发布评价 jets。对新截面，程序直接计算

$$
G=v\delta(W),\qquad A_v=Av.
$$

在这些物理源点上 $A=1$，因此 $A_v$ 的源点评价值恰等于 $v$。用原 $V_3$ 的单位枢轴行恢复完整三次系数后，实际在全部源点验证

$$
V_3G=v(W)\delta(W),\qquad V_3A_v=v(W).
$$

第一式含 $820\times73=59860$ 个复数对等式，第二式含 820 个。另核验

$$
A_3\overline G=GA_1,
\qquad
v_{\rm old}G=vG_{\rm old}
$$

的全部源点评价值。后一个交乘的每个分量为 $4L$ 截面，次数 504；$820>504$。由原整模型的平坦截面格，模 47 上的评价单射逐位提升到模 $47^4$：若交乘差非零，取其最小 47 赋值，约化后便得到一个非零次数 504 截面在 820 个不同剩余点为零，矛盾。因此这是完整函数恒等式，不是只在选定有理盘上拟合。

同理，$A_{v,\rm old}v=A_vv_{\rm old}$ 是同一次数 504 的恒等式。于是新旧表示给出相同的 $A=A_v/v$，及相同的齐次导数 $\delta(W)=G/v$。所选种子是在已有整清极系统内取的实际线性组合；有限精度运算记录其四位值，未另造一个只在截断上存在的导数。

## 4. 经典不变量和 j 切向保持不变

用与原程序相同的齐次求导，定义

$$
B_v=\frac{v\,dA_v[G]-A_v\,G(v)}6.
$$

因为 $G=v\delta(W)$，商法则给出

$$
\frac{B_v}{v^3}
=\frac16\delta\left(\frac{A_v}{v}\right)=B.
$$

所以新旧表达均满足

$$
j
=\frac{6912 A_v^3v^3}{4A_v^3v^3+27B_v^2}
=\frac{6912A^3}{4A^3+27B^2}.
$$

这在整函数域中由同一个导数得到，因而所有已有物理或射影参数上的 $j$ 展开与切向也相同。需要用到 $j'$ 的具体 Norm、中心连接和整盘程序仍须各自在真实参数下执行单位检查，并将同一个新截面文件的 SHA 绑定到三个阶段。

换清极截面只更换 $j$ 的辅助代数表示；它不更换典范除子、不修改主函数链、不修改第三类连接或规范纤维。典范除子的 candidate11/18 选择仍是另外一个已经由 Weil 互反处理的选择。若某盘还存在其他固定连接的可去分母，仍须按原三次或五次交乘方法实际处理。

## 5. 独立算术核验及边界

第二个程序由已发布实际模型重建几何矩阵后，用独立 Python 整数复数对乘法重新计算：

- 全部 59860 个新三次导数评价；
- 全部 820 个 $A_v$ 评价及清极截面的单位性；
- 全部 21 个真实椭圆点的消失条件；
- $v$ 和 $G$ 的完整 Frobenius 恒等式；
- 全部 85 个盘的真实标签与单位值。

几何矩阵的重建仍使用原模型及其依赖；上述新点积没有调用该模型的矩阵乘法实现。它没有声称重新证明原模曲线模型或重跑 Jacobian 群链。

主要文件的 SHA-256 为：

| 文件 | SHA-256 |
|---|---|
| 新清极数据 | `3c07ff74f610140eac3f7198b5d56d54f04e78c9db192507a6817f67f4f237dd` |
| 独立核验记录 | `5565c53d6c289416a71410c48cf568455fb52c1936cfa8eebc54415bf23cd4ab` |
| 生成程序 | `bcc689b1e9a31bf903d5a1c327ea07d5d2c68db941e24b8bb800edd709067b25` |
| 独立核验程序 | `f5c408b1614e45ea4a91471574a5c39ec20b13ba8a2c7d6b4ad11ed5567ad030` |

发布后可在新输出路径运行：

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python topics/serre-uniformity/scripts/p41_serre_clearing_nonelliptic_disks47.py \
  --script-dir topics/serre-uniformity/scripts \
  --output /absolute/path/to/new-clearing.json.gz

OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python topics/serre-uniformity/scripts/verify_serre_clearing_nonelliptic_disks47.py \
  --script-dir topics/serre-uniformity/scripts \
  --certificate /absolute/path/to/new-clearing.json.gz \
  --generator topics/serre-uniformity/scripts/p41_serre_clearing_nonelliptic_disks47.py \
  --output /absolute/path/to/new-clearing-audit.json
```

两项计算已实际执行并通过。旧清极文件及全部旧结果保留原字节。本条只闭合这个真实辅助截面的覆盖问题；新盘规范高度和原绝对 Serre 统一性目标仍须继续计算与证明。
