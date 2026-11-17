# 实际端圈的 C2 平化：固定新度量下的具体补段成本

2026-11-17，Astra-larger-parallel-16f63c8b / geometry_amplification。

**状态：拼接公式已证明；本次应用为实际数值证据。** 对 [best4 物理 M32 弱场](2026-11-17-parallel-geometry-best4-weighted-m32.md) 的真实深端 F、Fr、Frr，构造宽 $.0788790203722$ 的明确补段，准确接到半径1.767318285443017的平圆环。旧有限尾本体与补段的加密 Gram 采样分别为 $2.04539712\times10^{-6}$ 和 $2.05739712\times10^{-6}$；补段曲率约 $.02947$。二者都未过课题当前 $10^{-6}$ 门。

新参考 g **只在原 depth4 之外的未构造区间延伸**，原有限尾的 g 保持不变。选定新 g 后，其参数在加密中冻结。该补段不等于旧 cut 与强前缀的接合，不将弱 $\lambda=10^{-4}$ 当作 $\lambda=1$，也不声称固定五次补段已满足“精确解近似且误差持续下降”。

## 1. 一次选定的参考补段

设原尾到达 $r=b$，固定角换元为 $\Theta'(\phi)=\rho(\phi)>0$。记旧参考斜率的端点为 $w_b,w_b'$，取新的平 cuff 半径 $R>b$，$\ell=R-b$、$u=(r-b)/\ell$。选一个常数 $H_b$ 和固定 $A\ge0$，定义

$$
w_*(u)=w_b(1-3u^2+2u^3)
 +\ell w_b'(u-2u^2+u^3)+A u^2(1-u)^2,
$$

$$
z_*(u)=H_b+\ell\int_0^u w_*(v)\,dv,
\qquad B(r,\phi)=(r\cos\Theta,r\sin\Theta,z_*(u)).
$$

因此 $w_*(0)=w_b,w_{*,r}(0)=w_b'$、$w_*(1)=w_{*,r}(1)=0$。在补段上**定义并冻结**

$$
g_*=(1+w_*^2)\,dr^2+r^2\rho(\phi)^2\,d\phi^2. \tag{1}
$$

B 对 (1) 正好等距。旧有限区间上仍用原 g；w 及其一阶导数的匹配给出两个参考度量在接点的 C1 匹配。外侧接同高度平面圆环，参考度量亦相容。这里不继承被替代的、尚未生成的 source 深度4之后无穷尾。

## 2. 使用实际边界函数的三组 Hermite 数据

这里应用已有 [R227](../results/R227-hermite-seam-general-reference-hessian.md) 与 [R230](../results/R230-actual-A-finite-Hermite-cardinal-sameg-bridge.md) 的三jet Hermite构造；以下展开本次真实端圈的具体公式，不重复登记一般拼接定理。

令 $F^-$ 是实际有限尾，并定义三个边界函数

$$
\Delta_j(\phi)=\partial_r^j(F^--B)(b,\phi),\qquad j=0,1,2.
$$

取

$$
p_0=1-10u^3+15u^4-6u^5,
\quad p_1=u-6u^3+8u^4-3u^5,
\quad p_2=\tfrac12u^2(1-u)^3,
$$

并定义真实 Cartesian 补段

$$
F^+(r,\phi)=B(r,\phi)+p_0(u)\Delta_0(\phi)
 +\ell p_1(u)\Delta_1(\phi)+\ell^2p_2(u)\Delta_2(\phi). \tag{2}
$$

**C2 匹配证明。** 在0处，$p_0$ 的0/1/2阶 jets 为 $(1,0,0)$，$p_1$ 为 $(0,1,0)$，$p_2$ 为 $(0,0,1)$；在1处三者的这三阶 jets 都为0。对 r 微分时的 $\ell^{-1}$ 因子恰由 (2) 的幂抵消。因此内端 F、Fr、Frr 与 $F^-$ 全部相等，外端与 B 全部相等。对角变量微分同一边界函数，Fphi、Fphiphi、Frphi 也匹配。实际 R631 候选的这三个边界函数对角变量光滑，故该拼接是 C2。外端 B 的高度一、二阶 r 导数均为0，所以接平环仍 C2。这个证明使用真实连续边界函数；导出的有限角网只是其数值评价，不把端点网格的插值另当成已经精确接合的函数。$\square$

[端圈导出器](2026-11-17-parallel-geometry-end-jet-reader.py) 从冻结径向积分中取真实端圈 jets。所有 Fr/Frr 仍是原构造的解析导数，不是由末端两个网格差分。补段的角导数则对这些实际边界函数求导；数字实现保留原 literal Fphi/Fphiphi/Frphi，并对更高角导数作 FFT。

## 3. 可控制的顶部支撑高度

只记高度分量 $d_j=(\Delta_j)_z$，令 $h_b'=\partial_r(F^-)_z$、$h_b''=\partial_{rr}(F^-)_z$。由 (2) 直接得到

$$
\partial_r(F^+)_z=(1-u)^2(a_0+a_1u+a_2u^2),
$$

$$
a_0=h_b',\quad a_1=2h_b'+\ell h_b'',\quad
a_2=A-30d_0/\ell-15d_1-\tfrac52\ell d_2.
$$

定义

$$
T(\phi)=30d_0/\ell+12d_1+\tfrac32\ell d_2-3w_b-\ell w_b'. \tag{3}
$$

则 $a_0+a_1+a_2=A-T$。若全角域 $a_0\ge0,a_1\ge0$ 且 $A\ge\sup T$，高度不减：$a_2\ge0$ 时各项非负；$a_2<0$ 时二次式凹，其最小值在两个端点，两端均非负。于是补段整体位于平 cuff 的高度之下。

这些是可直接评估的边界条件。当前高度三组 jets 都是有限 Fourier 函数；若 $T=T_0+\sum(T_j^c\cos j\phi+T_j^s\sin j\phi)$，则
$\sup T\le T_0+\sum\sqrt{(T_j^c)^2+(T_j^s)^2}$。脚本输出相应 Fourier 系数界的浮点评价，不把浮点评价冒充严格区间包围。

本次选定且两次加密都保持

$$
\begin{aligned}
b&=1.6884392650708613,&R&=1.767318285443017,\\
w_b&=.0011985974673136036,&w_b'&=-.00040729843166375384,\\
H_b&=1.1391306715668115,&A&=.003016=377/125000.
\end{aligned}
$$

加密数据中 $\sup T$ 的 Fourier 界评价约 $.00301525641063$，$a_0,a_1$ 的 Fourier 下界评价分别约 $.00109050992486,.00214814087786$。因此所选 A 留有明确数值余量，未在第二次运行重新用 `auto` 选择 g。实际高度径向导数最小 $-2.17\times10^{-19}$ 来自平端的浮点消减。

## 4. 本体与补段分别精化

输入实际场仍是 `parallel-best4-weighted-m32-scale1e4.json.gz`，SHA
`47c4f2838c24c319717d7493417ef1424fa49675bcce9ec720bef1f8d3a59bed`；背景 SHA 为
`487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15`。完整112项 rho 没有裁切。

第一列使用原尾 N1024/G8 端圈及补段257个均匀 r 点；第二列使用原尾 N2048/G12 端圈及补段1025个 r 点。新 g 的全部参数、原 K 插值、补段公式均固定。

| 实际采样量 | 粗读 | 加密 |
|---|---:|---:|
| 原有限尾本体 Gram | $2.0453965359\times10^{-6}$ | $2.0453971183\times10^{-6}$ |
| **新增补段** Gram | $2.0573906600\times10^{-6}$ | $2.0573971235\times10^{-6}$ |
| 补段 rr 分量 | $1.0467329793\times10^{-6}$ | $1.0467385094\times10^{-6}$ |
| 补段 rphi 分量 | $4.0852433\times10^{-7}$ | $4.0961812\times10^{-7}$ |
| 补段 phiphi 分量 | $2.0573739379\times10^{-6}$ | $2.0573794806\times10^{-6}$ |
| 原尾本体最大曲率 | 5.99764276661 | 5.99764287836 |
| **新增补段** 最大曲率 | .0294700682176 | .0294700682176 |
| 平 cuff 高度 | 1.139185662453843 | 1.139185662453843 |

补段最小 Gram determinant 约 $.07857676224$、平面投影 Jacobian 约 $.28031527573$、polar 角导数约 $.16602034138$，均为采样证据。最大 Gram 仍主要来自角向长度，最坏点约 $u=.06738$。

内端0/1/2阶 Cartesian 数值接差分别不超过 $0,0,5.43\times10^{-20}$；平端分别不超过 $0,2.17\times10^{-19},2.41\times10^{-18}$。两网在共同角点的 F、Fr、Frr 差分别不超过 $1.12\times10^{-15},8.89\times10^{-16},1.09\times10^{-19}$；Fphiphi 差约 $6.63\times10^{-10}$，是直接 FFT 二阶角导数的读出差，未隐去。

当前原尾最高高度采样约1.13914432549，低于新平 cuff 高度。补段最大原点范数2.10265496352，对同一 b677 见证点的最小距离约1.17170769864。它们不替代完整活动体及闭盖的连续域位置/reach 检查。

## 5. 适用范围与未支付条件

这给出了一个实际可复现的 C2 收尾及成本，未证明最优，也没有连续域严格极值证书。特别是：

- 原尾与补段都仍超过当前 $10^{-6}$ 度量门，不能写为达标。
- 固定显式五次补段在加密后误差稳定在非零值。它没有证明来自同一个精确等距解，也没有支付 README 第5项。后续若把它作求解初猜，必须在**已经冻结的新 g** 上求解和精化，不能每次改 A、宽度或参考度量后当作同 g 收敛。
- 内端与这里的有限尾匹配，不是与真实强 $\lambda=1$ 前缀匹配。原始 cut 的模式、位置及全部 Cartesian jets 仍有独立责任。
- 平 cuff 提供 [R632 回头盖](../results/R632-c2-return-cap-parallel-body-and-diameter.md) 所需的实际平2-jet接口，但尚未把回头盖装到完整活动体并证明全体点对 reach。该尾片仍不能登记为闭曲面。

同公式对材料 $\lambda=.0014$ 的一次实际应用，保守选高 A 后补段 Gram 约 $2.21\times10^{-5}$；故“小高度”或“能写 C2 拼接”都不足以推出低度量误差。此比较只用于成本定位，不作为不可行性定理。

## 6. 源码、接口与复现

新增源 SHA256：

```text
2026-11-17-parallel-geometry-end-jet-reader.py
5054d3b13bde5e32b5afe5bd54d2471136d676dae1169354a69d505bea4890cd
2026-11-17-parallel-geometry-flat-cuff.py
000efac8f5d01511a9a2504c4fe188a3ece13957574460a8910f19cc15cc94dd
```

先按 [物理 M32 几何命令](2026-11-17-parallel-geometry-best4-weighted-m32.md#5-复现冻结源和未完成责任) 运行，将 `--radial-reader` 改成 `notes/2026-11-17-parallel-geometry-end-jet-reader.py` 的完整 topic 相对路径。导出器自动把 NPZ 写到原 raw 输入所在目录，文件名带角点数与径向 Gauss 阶。两份实际端圈 NPZ 的 SHA 为

```text
N1024/G8
a453c4d23cf8599ea97ea3e0c6c7b34fee99f7425dd6b0499d4cc5ba5c124883
N2048/G12
f366fc28451c7f266f7169b4c2abd8184bea942862c2286d654a3c0517d51108
```

补段加密命令：

```sh
OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-flat-cuff.py \
  --jets /workspace/scratch/16f63c8bce6b/parallel-best4-weighted-m32-scale1e4-end-jets-n2048-g12.npz \
  --cuff-radius 1.767318285443017 --lift .003016 \
  --radial-points 1025 --witness-major 1.4141197181548968 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-weighted-m32-scale1e4-flat-cuff-fixed-n2048.json
```

粗读换为 n1024-g8 的端圈及257个 r 点，**保持 lift=.003016**。两份实际补段报告的 SHA 为

```text
N1024, radial257
a2b5637b4987f8c321af73c1f77147337d8837ae6810ff66e8c735365feb4f47
N2048, radial1025
d901d9a76ab8c0d342898205f0a761da13d3d3efdbfb3069f4b705eaf450df56
```

给其他直接高度优化器的函数接口为
`height_jets(u, width=..., w0=..., w1=..., mean_height=..., hb=..., hrb=..., hrrb=..., lift=...)`。
三组边界高度可直接以有限模在 $\Theta(\phi)$ 评价，无须材料角网插值。返回 h/hr/hrr、参考 w/wr；与完整 Cartesian 补段的高度部分在实际17径向点×1024角点上逐项相同。所有 raw、NPZ 均不入库。
