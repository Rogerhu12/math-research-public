# R114 材料图上的真实 Cartesian 复合及补偿试算

2026-11-26，Astra-visible-flex-6a65e705-20261126 / g5-and-exact。

**状态：三次实际运行已完成；有限求积结果，不是连续度量证书。**
本记录把 R216 的冻结 W 真正与 R114 的 Phi 复合，
并解释为何“弱矩被消掉”仍不足以接受完整度量步。

## 实际对象与所有导数

原数据、几何、W 参数身份沿用
[已冻结 up 补丁](2026-11-26-6a65-exact-weak-moment-cartesian-up-patch.md)。
原 R114 前缀字段 metadata 为
2026-11-12-fd2d-metric-m12-gauge-c2-01/prefix-field.json，
SHA256 780a70825130ce322ac19f5626673e8308531bc4c03bbbe6cbd6fd403332c5a4。
保留它的全部 512 个 cosine/sine 模以及共享节点 value/first/second jets，
以准确 quintic Hermite 定义作 longdouble 求值。

恢复了相邻节点 64–320 的四个分片，完整覆盖所用 up 支撑；没有声称已恢复全前缀。

| 分片起始节点 | Git blob | SHA256 |
|---:|---|---|
| 64 | 58b327aeff1027abd95237aa45b25a5d7cc37c2b | 967016c13bbdca023585561bc66184a4dc60207a72f0fd0feafead4fe9bba20c |
| 128 | d32dcb506e90b43cef0e0ba4c3cda3f14b6aec64 | 4ff214b33934dc01c25734e4c84e649f898a0ac885c46bc2a7955c20c60d3802 |
| 192 | 54b32b2bc92f77cf289ec36311959db5ea7ef554 | 17fec7c7215472cd6957f0fa3837d6d4da0f2cf6f938ea73ca6e0f1a21ac35e6 |
| 256 | 108359951109ed293050264f257384e732fd2590 | 089a79a63ad714f87d10290ff30eff051b1a79cd2ef7247199c07886bcfdbe6d |

blob 身份来自本题 DELETED_DATA_2026-11-15.md；
恢复后逐件校验 SHA256，数据只在临时目录。

记原字段为 $\Phi(s,u)=(s+p,u+q)$，原 native chart 为
$u=\psi-e(s)\sin(3\psi)/3$，$\rho=1-e\cos3\psi,\ \nu=-e'\sin3\psi/3$。
字段 native 导数转换为

$$
A=p_s-(\nu/\rho)p_\psi,\quad B=p_\psi/\rho,\quad
C=q_s-(\nu/\rho)q_\psi,\quad D=q_\psi/\rho.
$$

在每个输入 $(s,u)$，实际取
$S=s+p,\ U=u+q$，反解 $U=\Psi-e(S)\sin3\Psi/3$，
并在 $(S,\Psi)$ 的真实源 quintic Fourier 图上求一阶导数。
不是用未移位的源 jets 加上一个线性误差上界。

若 $E,Z,G$ 为 $X+\zeta W$ 在移位点相对同一供应器
$g_0=dS^2+f(S)^2dU^2$ 的完整归一残差，
$f_S=f(S),f=f(s)$，则新完整 Gram 的三项为

$$
R_{ss}=2A+A^2+f_S^2C^2+(1+A)^2E
+2(1+A)Cf_SZ+C^2f_S^2G,
$$
$$
fR_{su}=(1+A)B+f_S^2C(1+D)+(1+A)BE
+[(1+A)(1+D)+BC]f_SZ+C(1+D)f_S^2G,
$$
$$
f^2R_{uu}=B^2+[f_S^2-f^2]+f_S^2(2D+D^2)
+B^2E+2B(1+D)f_SZ+(1+D)^2f_S^2G.
$$

本支持内 $f$ 准确为仿射函数，所以
$f_S^2-f^2=2ff'p+(f')^2p^2$。
代码先计算小残差和这个准确目标差，以免相减两个 O(1) Gram。
$E,Z,G$ 自身包括 W 的全部线性及二次 Gram 项。
因此以下是实际 $(X+\zeta W)\circ\Phi$ 的观察结果。

## 1. 原 W full step 在 R114 背景上抬高峰值

每三重角周期 512 个节点，每个源 cell 8 点 Gauss；
全部 73 个相交 source cells，共 584 个径向点。

| W 倍数 | sampled metric 最大值 | 十二弱矩最大归一比 |
|---:|---:|---:|
| 0，即旧 R114 Phi | 1.4592641642719353e−10 | 2.253020823198703e−12 |
| 1 | 2.6579697187100195e−10 | 2.64954647127344e−16 |
| 1/2 | 1.5717610633539796e−10 | 1.1264347262739783e−12 |
| 1/4 | 1.4592619365137764e−10 | 1.6897277747364113e−12 |
| 1/8 | 1.4592630503773625e−10 | 1.9713742989675748e−12 |

原 Phi 的最大观察位置在 s≈.2922360076480955，
full W 后移到 s≈.35702887735537514。
虽然弱矩减少，full W 不能作为 R114 背景上的峰值改善接受。
1/4 的极小观察下降也没有独立密网格与连续包围支持，不将其升级为新的下降定理。
512 gauge 模与 512 观察点还可能产生弱矩积分 alias；
这里不会将 2.65e−16 当成连续弱矩值。

## 2. 新真实切向补偿

为消除 W 带来的切向应变，增加准确 C² 材料字段

$$
P(s,u)=\sum_{k=0,3,\ldots,144}\sum_{j=0}^5
a_{kj}\,\chi(s)L_j(2\tau-1)\cos ku,
$$
$$
Q(s,u)=\sum_{k=3,6,\ldots,144}\sum_{j=0}^5
b_{kj}\,\chi(s)L_j(2\tau-1)\sin ku.
$$

$L_j$ 为 Legendre 多项式；同一个紧支撑 bump 保留零两 jets。
共 582 个未知量：mean P 六个、48 个非零模式各十二个。
方向生成对完整三分量的目标 Lie 导数

$$
\delta E=2P_s,\qquad
\delta Z=fQ_s+P_u/f,\qquad
\delta G=2(f'/f)P+2Q_u
$$

作加权 $E^2+2Z^2+G^2$ 拟合。
完整角正交性使不同模式分别形成 6×6 或 12×12 小块；
不是删掉某个 Gram 分量，也不靠将弱矩权重变大。

只用目标 Lie 导数生成候选；接受读数重新计算
$$
(X+W)\circ(\Phi+\xi(P,Q))
$$
的实际移位点、完整 D(Phi+xi v) 和全部 Gram 二次项。
因此没有用预条件器预测冒充真实接受步。

| 补偿倍数 xi，W 始终 full | sampled metric 最大值 | 加权完整 Gram 能量 |
|---:|---:|---:|
| 0 | 2.6579697187100195e−10 | 1.2630271865766555e−21 |
| 1 | 1.4596282728880865e−10 | 6.029799984180018e−22 |
| 1/2 | 1.5794184016739204e−10 | 7.679917954544832e−22 |
| 1/4 | 2.1150802923805474e−10 | 9.742565417403882e−22 |

能量定义是
$\int f\,\mathrm{mean}_{\psi}[\rho(E^2+2Z^2+G^2)]\,ds$，
不包含共同的 $2\pi$ 因子。
full 补偿纠正了大部分抬升，但仍比旧 Phi 的同网格峰大约
3.64e−14，故**尚未取得比原 R114 峰更好的新候选**。
原峰在紧支撑左边缘附近；边缘两 jets 固定对继续降低该处误差形成实际限制。

P、Q 系数绝对值最大分别为
3.831540122468065e−11 与 9.440521671669333e−11。
由有限多项式系数绝对和，新增物理字段的粗导数范数小于 .001，
加上 R114 的旧导数界仍远小于 1；
因此若采用此字段，可以由 R112 的已有条带/次数论证保持 C² 微分同胚，
从而像集仍准确等于 R216 的 X+W。
这不替代新度量下降的检验。

## 实跑、哈希和复现命令

源码：

- scripts/6a65-m12-up-patch-compose-phi.py：
  e9a2e32a26152d3bf42e9ee52841168ba2c311d8a7faf280751075bb7342e77c；
- scripts/6a65-m12-up-patch-tangent-followup.py：
  289dcdc4c3447b6f92b5679402da6e737d657d779676e425ae552ad366bc19dd。

| run | 秒数，exit | 输出 SHA256 |
|---|---|---|
| 原 Phi 上的 W 五档真实复合 | 25.14006627901108，0 | d6b7884ad7884930914cf1db79c7bb4a99172f492f98af0905c530e4486f97f7 |
| 6 径向 × 48 角模补偿拟合 | 20.57870446999732，0 | 89b83620383e4ffda1adb104b63134c17f09506ead1fd680ed06136f8f3c917f |
| 四档真实补偿复核 | 76.16097627699492，0 | df86a101435e45ac5feb3def2d446e8a779d50b11f5b03f2458a1bc651ce671b |

在仓库根运行，数据和输出只放临时目录：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 topics/visible-flexible-closed-surface/scripts/6a65-m12-up-patch-compose-phi.py \
 --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
 --field-data /tmp/visible-flex-6a65e705/exact-work/phi-prefix \
 --parameters topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-up-patch-parameters.json \
 --out /tmp/visible-flex-6a65e705/exact-work/weak-v2-up-compose-NEW.json \
 --angular 512 --gauss 8

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 topics/visible-flexible-closed-surface/scripts/6a65-m12-up-patch-tangent-followup.py \
 --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
 --field-data /tmp/visible-flex-6a65e705/exact-work/phi-prefix \
 --parameters topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-up-patch-parameters.json \
 --out /tmp/visible-flex-6a65e705/exact-work/tangent-fit-NEW.json \
 --angular 512 --gauss 8 --radial-degree 6 --modes 48
~~~

随后同一 tangent-followup 命令以
--apply /tmp/visible-flex-6a65e705/exact-work/tangent-fit-NEW.json
和另一个新 --out 路径作真实复核，不再次求解。

这些运行固定了原供应器 g0；本次没有重付 g0 到原 g 的准确桥转移。
没有以增加观察点代替生成新的几何候选。
继续方向是增加独立径向弱应力/法向自由度，改善全 Gram 的方向，
或将支持扩展到实际峰两侧；不会以本记录作为完成收尾。

