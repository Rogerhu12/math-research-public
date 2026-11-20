# M24 含完整 lift 前缀：连续度量的实际入口

日期：2026-11-20。维护：Astra-held10-1b6d88ec-20261120。

**实际完整计算已 exit 0：全前缀连续 metric≤9.695183718076938e−7、曲率≤9.6498117548569，曲率未决区间0。** [R62](../results/R62-actual-m24-complete-prefix-and-bridge-certificate.md)合并已付入口修补、精确桥接缝和统一目标g，给出整个开放连接器的结论。本文保留真实计算的方法与开发断点。 [R60](../results/R60-actual-m24-c2-bridge-and-continuous-metric.md)已处理桥段，本条接 $0\le s\le s_b$ 的含核心 lift 部分。真实尾另在 chord3 session54314 运行。

## 1. 绑定与对象

输入仍为新 M24 linear 的 run/physical，SHA256 分别为 c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a、f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d。不是后续 trueDN 可能更新的场。

[PrefixPieces](../scripts/resume_m3/explicit_m24_prefix_pieces.py)逐式采用已证[绝对高度对象](2026-11-20-m24-prefix-absolute-height-certificate.md)：原右侧共同二 jet 的精确五次 Hermite $Y_*,e_*$，保持 $\delta$ 且独立规范周期时长的 $a_*$，原完整 lift 及固定 mean1168。每个轮廓子片只在精确 Fraction 中平移到物理中点后作区间求值；仍是同一个函数。端点代数已实际通过，未重算既有高度积分。

真核心直接来自[严格 R53 oracle](2026-11-20-m24-r53-true-core-jet-certificate.md)。原1168均值节点的真 $H,H_\psi,H_{\psi\psi}$ 区间直接复用；外角点和闭盒的 $\Gamma,\Gamma_u,\Gamma_{uu},\Gamma_{uuu}$ 经完整初始角图链式法则，减去同一基圆和冻结 Fourier 投影，构造真 $H_0,\ldots,H_3$。不将缓存小差、采样或另一均值图当作相等。

图为
$$
F=a_*e_r(\theta_*)+G_*+a_*\chi H+Z_*e_z,\qquad
Z_*'=\frac1{1168}\sum W_z(s,\psi_j),\quad Z_*(0)=0.
$$
$W_z$ 保留真实 Frenet、正根和对流；不假定有限场已经等距。目标为 $ds^2+a_*^2d\theta_*^2$。

此定义不宣称入口恰好逐字等于 $\Gamma(\theta_0)$：原 $Y(0)$ 与冻结 initial 的系数差约 $1.7424\cdot10^{-13}$，原角样条首值为 1.0000000000000002。精确中央柱接口已由 [R61](../results/R61-actual-m24-exact-c2-cylinder-inlet.md)另行规范；本条原始未修补图不能由 lift 的名称推成已经闭合。

## 2. 当前连续计算的办法

[实际源](../scripts/resume_m3/certify_prefix_metric_interval_taylor.py)在所有物理片、角片、轮廓片及 lift 接头处分开径向区间。记
$$
U=F_s-vF_\psi=U_0+u,\quad V=F_\psi/(a_*\rho)=e_\theta+w,\quad
U_0=a_*'e_r+M e_z.
$$
在区间运算前先消去基圆目标：
$$
\begin{aligned}
E_{11}&=(a_*')^2+M^2-1+2U_0\cdot u+u\cdot u,\\
E_{12}&=a_*'e_r\cdot w+Mw_z+e_\theta\cdot u+u\cdot w,\\
E_{22}&=2e_\theta\cdot w+w\cdot w.
\end{aligned}
$$
完整 $u,w$ 含 $G_s,G_\psi,(a_*\chi)'H,a_*\chi H_\psi$ 与 $v$；没有删掉参考 lift 或对流。

对径向盒中心 $c$、半宽 $h_s$，在每个外角节点用
$$
\|E(s,\psi_j)\|
\le\|E(c,\psi_j)\|+h_s\|E_s(c,\psi_j)\|
+\frac{h_s^2}{2}\sup_I\|E_{ss}(\cdot,\psi_j)\|.
$$
所有这些量由同一二阶区间自动微分得到。各片可使用其单侧三阶场导数，不对整体共同 Hermite 图增加 $C^3$ 假设。

全角则用 Banach 空间线性插值余项：
$$
\sup_\psi\|E(s,\psi)\|
\le \max_j\|E(s,\psi_j)\|
+\frac{h_\psi^2}{8}\sup_\psi\|E_{\psi\psi}(s,\psi)\|.
$$
最后一个角盒严格包含真实 $2\pi$；该点由真周期性等于零节点。$h_\psi$ 使用全部字面节点间距的外向上界，未假定它们是精确等距符号节点。

每个对称 $2\times2$ 区间矩阵按
$$
\frac12\left(|E_{11}+E_{22}|
+\sqrt{(E_{11}-E_{22})^2+4E_{12}^2}\right)
$$
包围算子范数。各项先向外运算，再取节点/盒的最大值。

## 3. 已实际发现的角包围门

2336 外角点/盒下，九个不同径向阶段的严格点探针实际 exit 0，24.4265秒。它们不是完整径向覆盖。点处算子上界最大约 $3.12\cdot10^{-7}$，但角二导区间界达到约1.54，角插值余项达到 $1.40\cdot10^{-6}$，超过预算。仅细分径向不能解决这一项，故未启动注定无法据此通过的完整2336覆盖。

[4672新严格导出](2026-11-20-r53-4672-angular-refinement.md)已实际 exit0。它只增加外角分辨率，原均值1168、所有参数和实际场均未改。新箱宽约减半，步长平方项约缩至四分之一；是否足够仍以完整计算实际返回为准。

早先首个开发探针因常量向量的二阶自动微分零项未按形状展开而在建表时抛 IndexError，没有产生数学验收值；修正后的九点探针才用于上述判断。保留旧日志，不把程序错误称作场的反例。

## 4. 同次几何输入

完整覆盖在接受每个度量盒时，另用已经算出的均值与角 jets 包围主曲率，避免再求同一批均值。若取任一连续单位法线 $n$，目标材料标架中的第二基本形式为
$$
h_{11}=n\cdot(U_s-vU_\psi),\quad
h_{12}=n\cdot U_\psi/(a_*\rho),\quad
h_{22}=n\cdot V_\psi/(a_*\rho).
$$
若该盒度量误差上界为 $\epsilon<1$，则
$$
\max|\kappa_i|\le \|h\|_{\rm op}/(1-\epsilon).
$$
曲率范围单独记录；若某盒的法线区间未证，则记录 unresolved，不因此冒称全几何通过。尺寸与外向支撑由独立包装复用同图、同角盒与已证均值范围推进。

## 5. 当前执行

完整计算 session2559 已实际 exit0，用时3540.0320036400008秒。目标 $9.7\cdot10^{-7}$ 下，395个原片经过670次必要二分，1735次尝试、1065个接受闭区间完成全覆盖；全metric≤9.695183718076938e−7，同次全K≤9.6498117548569、曲率未决0。源保持冻结；[真实终态/命令/hash](2026-11-20-m24-prefix-continuous-metric-execution.json)已保存。

| 源 | SHA256 |
| --- | --- |
| certify_prefix_metric_interval_taylor.py | 6b36ccd6bab54fa35c6fe62a433f417faf7a51b80c35b798b17567eb22714986 |
| explicit_m24_prefix_pieces.py | 1a0a45db78a9aa62884459a6542d20f6995ea152962030919fbbb74d8aee573e |

~~~bash
HELD10_WORK=/workspace/scratch/1b6d88ecddf3
HELD10_REPO="$HELD10_WORK/math-research-public"
HELD10_SCRIPTS="$HELD10_REPO/topics/visible-flex-held-10pct/scripts/resume_m3"
python -u "$HELD10_SCRIPTS/certify_prefix_metric_interval_taylor.py" \
  --source-run "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --core-mean-intervals "$HELD10_WORK/geometry-work/newg-m24-r53-core1168-intervals.npz" \
  --core-mean-certificate "$HELD10_WORK/geometry-work/newg-m24-r53-core1168-certificate.json" \
  --core-angle-intervals "$HELD10_WORK/geometry-work/newg-m24-r53-core4672-angles.npz" \
  --core-angle-certificate "$HELD10_WORK/geometry-work/newg-m24-r53-core4672-angles.json" \
  --interval-kernel "$HELD10_REPO/topics/visible-flex-held-10pct/scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py" \
  --target 9.7e-7 \
  --out "$HELD10_WORK/root-work/m24-prefix-continuous-metric-certificate.json"
~~~

当前对象仍是 $\lambda=.002$ 的指定 linear 场。本次计算已通过，仍不能移用到未来更新的 trueDN 场，不能替代中央/尾部精确接口、准确圆弧、完整闭族、全时 reach 或冻结全部参数后的精化。
