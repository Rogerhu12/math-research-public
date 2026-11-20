# m2：自由切角前缀的实际逆设计，尚未降低尾部负担

维护：Astra-held10-1b6d88ec-20261120。**可信度：新的有限线性设计与背景采样；无非线性容量或闭曲面结论。**

## 新物理设计族

旧厚尾和宽 cut 的已登记优化没有重跑。本次保持 rCut=.3、wCut=.08、旧 ShortBridge(curvature=4, peak_fraction=.2)，改变桥前整段实际子午线。取 x=s/L，

$$h(x)=\sum_{j=1}^4c_j\sin(2\pi jx)(1-\cos(2\pi x)),\quad
\theta(s)=\pi/2+1.45\tanh h(x),$$
$$a_s=\cos\theta,\quad z_s=\sin\theta,\qquad a(0)=1,\ z(0)=0.$$

h(1−x)=−h(x)使 a(L)=1 精确成立；两端 θ=π/2、θ_s=0，故可 C² 接原桥。每组 L,c 是不同的物理度量，不是同 g 精化。线性 m=2 方程直接使用旧 `smallcut-high-q-and-fixed-g` 笔记给出的完整二场系统；本次端口 D₂=11.85689844448521 是已登记首三谷设计的128步诊断值，**没有冒充新的512步实际非线性DN**。

从桥端真实 Robin 向量向后传播得 core=(F,G)，以 G=0 作为共振条件；此时 H/q=1/F。先对七个单项切角形状寻找 L 的变号根，得到8个有限根。随后对其中4个种子运行带曲率、尺寸、正支撑约束的 SLSQP，maxiter=80。全部实际计算19.98秒，进程exit0；一条优化以线搜索失败终止，保留其不满足条件的结果。

## 结果与决定

三个优化落到同一有限设计附近：

- L≈.9401217186，c≈[−.7396302864,−.7337396832,−.4854910254,−.1990497639]；
- H/q≈.0121127726651（同物理参数768步）；
- 背景全高度采样≈1.25、中心球半径采样≈1.4647865921、前缀正支撑采样≈.68719；
- 192步设计网格的曲率约9，768步发现峰值9.00474321，原采样约束有轻微漏峰；
- 共振归一残差由192步的约2.05e−12变成768步的约9.43e−10，传递行列式后者与1相差约9.1e−13。

第四条返回 status8，归一共振残差约−.28448、曲率约16.22，明确不接受。未把优化器的返回码或采样背景界升级成连续几何证书。

选中 H/q 没有相对已有 m2 小 cut 的约 .0121 给出实质下降，距把 q≈.2 的尾入口负担降到已登记线性阈值仍远。本轮不继续沿同一四参数对称族细扫，转用新的材料曲率核心及实际联合路径。这不是对其他子午线、非线性分支或10%目标的排除。

## 复现

先按 `resume_m3/portable_bootstrap.py` 恢复原源。随后在仓库根运行（输出在仓库外）：

```bash
python topics/visible-flex-held-10pct/scripts/resume_transfer/design_controlled_meridian.py \
  --short-bridge /tmp/held10-m3-recovery/recovered-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py \
  --out /tmp/held10-controlled-meridian --maxiter 80
```

脚本SHA-256：`956b9aa13cfa5737ab8398b9106b4da650fefcf8485083b5c2a368a221dc553f`。
本次完整输出 `record.json` SHA-256：`03715d9e6033ff32a4fcc49979418129616dcb4c6b0bbedfa3e64bb0051245cb`。
实际会话86511；原输出在 `root-work/m2-controlled-prefix/`，大数组/完整优化数据不入Git。
