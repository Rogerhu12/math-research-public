# 原 R114 背景上的完整 Gram Schur 步与支撑外残差

2026-11-26，Astra-visible-flex-6a65e705/g5_and_exact。
这是实际执行记录；没有接受新的全域误差下降或第 5 条完成结论。

## 1. 对象和求解方向

源码为 `../scripts/6a65-m12-full-gram-schur.py`，SHA256
`43f404464526d1232eedf144e1de2245c56a44958abddf1b4cb8517d33cf9f8d`。
它复用同目录的 `6a65-m12-multiple-radial-stress.py`、
`6a65-m12-up-patch-tangent-followup.py` 和实际 Phi 复合供应器。
输入对象、四个已恢复的字段分片及重生方法见
`2026-11-26-6a65-r114-compose-and-tangent-followup.md`；原 M12 数据 SHA256 是
`359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`，
字段元数据 SHA256 是
`780a70825130ce322ac19f5626673e8308531bc4c03bbbe6cbd6fd403332c5a4`。

此轮不把 48 个弱矩强制清零。令 $b_j=\chi L_j(2\tau-1)$，
$j=0,1,2,3$，$k=3,6,\ldots,36$。96 个 Cartesian 列是
$b_j\cos(ku)e_r(u)$、$b_j\cos(ku)e_z$。
程序在原始 $X\circ\Phi$ 的实际移位点求列，保留完整 $D\Phi$，
从它们的实际 $2\operatorname{sym}\langle d(X\circ\Phi),d(W\circ\Phi)\rangle$
累计正规方程和 Dirichlet 正则化矩阵。

切向空间为 12 个径向 $\chi L_j$、48 个三倍角频率以及平均 $P$，
共 1164 个变量；反射对称性要求 $Q$ 为正弦，故无平均 $Q$。
切向列使用完整的 $\mathcal L_vg_0$，只用于生成方向，
没有把它当作近似参考 $h$ 的精确导数。
每个角频率先消去 12 或 24 个切向变量，再对白化后的 96 维
Schur 矩阵加 $\mu I$，这里 $\mu=10^{-4}$。

所有试步都重新计算同一个真实位置映射

$$Y_z=(X+zW)\circ\bigl(\Phi+z(P,Q)\bigr),$$

包括移位的源图、移位的补丁、材料图链式法则和全部二次 Gram 项。
没有把线性预测记为实际误差。目标仍是此前明确的 $g_0$；
此采样没有重新支付到原精确桥度量 $g$ 的转移界。

## 2. 实跑和结果

工作目录为本仓库根；临时路径前缀
`/tmp/visible-flex-6a65e705/exact-work/` 下保存本轮生成物。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-full-gram-schur.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --field-data /tmp/visible-flex-6a65e705/exact-work/phi-prefix \
  --out /tmp/visible-flex-6a65e705/exact-work/up-fullgram-r4n12m48-mu1e-4-fit.json \
  --angular 512 --gauss 8 --normal-radial 4 --tangent-radial 12 --tangent-modes 48 --damping 0.0001

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-full-gram-schur.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --field-data /tmp/visible-flex-6a65e705/exact-work/phi-prefix \
  --out /tmp/visible-flex-6a65e705/exact-work/up-fullgram-r4n12m48-mu1e-4-512g8-actual.json \
  --angular 512 --gauss 8 \
  --apply /tmp/visible-flex-6a65e705/exact-work/up-fullgram-r4n12m48-mu1e-4-fit.json
```

两步均实际 exit 0，耗时分别为 67.79477084698738 秒和
64.01083443399693 秒。拟合 JSON 的 SHA256 为
`fd39158dfcdd7fddc832fd6baa9b50773d6855345a1486692680c226d91e8fa3`，
实际复合 JSON 为
`fee6e8568e669c944daa650ee62c0a98eb433c37b35d5a39d2057fdd5228e9c1`。

采样在一个三重对称角周期上用 512 个节点、每个真实源 Hermite 单元
8 点 Gauss；表中能量是代码固定归一的
$\int f\,(e^2+2z^2+\gamma^2)$ 数值求积。

| 同时步长 $z$ | 实际相对 Gram 算子范数采样峰值 | 采样能量 | 48 弱矩最大归一比 |
|---:|---:|---:|---:|
| 0 | 1.4592641637353076e-10 | 5.963958817838139e-22 | 6.975240036863573e-12 |
| 1 | 1.4797859078513276e-10 | 5.369319415685531e-22 | 5.82808331684188e-12 |
| 1/2 | 1.459986546378618e-10 | 5.561335756107323e-22 | 4.402764624329317e-12 |
| 1/4 | 1.459625195742881e-10 | 5.736321446776721e-22 | 5.447481614809676e-12 |

因此是真实能量下降，但三档新图的采样峰值都略高；本轮不采用。
白化 Schur 数值特征值范围约为
$[-8.3795242\cdot10^{-12},\,0.014945906]$，这只是有限数值诊断，
不是无限维逆算子或正定性的证明。切向块保留秩为平均块 12、其余块 24。

## 3. 为什么随后转向完整端口

补丁仍只支持在原上升 affine 段的内部
$a\simeq0.2916001781596422$ 到
$b\simeq0.4196197685711923$。这些紧支撑基函数的零至二阶端 jet
为零，因此不能支付外侧的原始 Gram 残差。

另用同一 `packet` 供应器对原 Phi 图作 1024 角点观察：
在 $s=0.28449797869233384<a$，峰值约
$1.6318374882773525\cdot10^{-10}$；在
$s=0.28548797869233383<a$，约
$1.5496280345030247\cdot10^{-10}$。
这两个点离补丁支撑远大于 Phi 的位移，切向补丁也为零，
所以它们的实际映射不受本轮任何系数改变。
这些数值未附外向舍入，不能提升为严格点态下界。
在 $s=a$ 的原图采样约 $1.4597859681866653\cdot10^{-10}$；
严格的 Cartesian 支撑端点在 $\Phi$ 的原像上，不能把
$\Phi(a,u)$ 默认为恰在 $S=a$。

接下来的实质改变是消费已有 R137 供应器，从同一个 M12 截面建立
完整弧长参数与空间两 jet 的精确 affine 段，并与两侧旧图逐项比较端迹。
只有完整端口条件和全频逆真正闭合，才可能把 R218 的法向 Green
公式用于固定度量的精确修正。本轮有限 Schur 系统没有完成这一步。
