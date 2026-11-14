# R18 M8 闭网格 exporter 独立审查与完整字节重放

审查者：/root/tail_theory，2026-11-09。审查者没有参与本 exporter 的实现、网格采样方案或 face 索引构造。背景相对高度 helper 由本审查者编写，因此该 helper 的有效性与实际 76 点输入链采用 independent_geometry 的另份独立审稿；不在此自行独审自己的算法。

**结论：PASS。** 对冻结 exporter 全文静态检查后，独立执行完整 build，三份 PLY.gz 与作者输出逐件 SHA256 相同。另以独立二分、相位索引、帽公式和镜像/面方向检查验证主要坐标约定。此项认证的是 R18 M8 已指定连续图的数值离散导出；不新增连续 metric、reach、顶点严格误差或 README 第 5 项结论。

## 1. 冻结输入

- exporter：scripts/db6f-export-closed-mesh.py，SHA256 ee4a474ebdecf4462e41f19b8b22c591f0e532e0419f0d7b3e4f2677d43b1708。
- 原始网格清单：notes/2026-11-09-db6f-visible-m8-manifest.json，SHA256 6a49b75c5a0c112fc798c4167356b9b8f57e0f489e33b6ed9aedcc2c1eff3282。
- 输入 plan、geometry、whole certificate、tail manifest、数值高度报告及源代码 hash 均由原清单和计划绑定。该 geometry 为 R17/R18 的 common-cut M8/32 图，不能将本输出称为 M12/M15 网格。
- 独立重放清单：notes/2026-11-09-db6f-tail-review-visible-m8-replay-manifest.json。
- 独立小检查器：scripts/db6f-tail-review-closed-mesh.py；机读结果：notes/2026-11-09-db6f-tail-review-closed-mesh.json。

完整 PLY 顶点、面数组不读入对话。此审查不重复另一个独立验证器的全边表/连通分量账本；下述实际面方向检查与该账本互补。

## 2. 材料角与相位

prefix 在各径向采样点先由已审的确切 clamped spline 计算 $e(s)$，包含 $s/end>3/4$ 的五次 cutoff 和固定 $8q$ 倍率。新脚本对区间端点与样条节点的选择正确；其 Horner 计算使用 Fraction，只有最后转为数值代表。

必须解的材料角关系为

$$
\theta=\Theta(s,\psi)=\psi-\frac{e(s)}3\sin(3\psi).
$$

因为采样中的 $|e|\le .8<1$，该角函数严格递增；初始括区间
$[\theta-|e|/3,\theta+|e|/3]$ 的两端确实夹住根。exporter 的 residual 符号与二分括区间更新相符，Newton 超出括区间时回退到中点。其坐标随后用该 $\psi$ 评价径向/切向 Fourier 分量，未直接把材料 $\theta$ 当成辅助角。

独立检查器对 144 个实际经向位置，用同一已审样条系数的另一种确切幂次求和逐值核对 $e$；全部相同。对 20,736 个实际 $(s,\theta)$，另用 70 次单调二分反解，和 exporter 数值逆的最大差为 $1.866\cdot10^{-14}$。这仍是数值一致性检查，不将浮点 residual 解释为严格角误差区间。

在 $t=0,1/4,1/2$，$\alpha=2\pi t/3$，且 $N=144$ 给 $Nt/3=0,12,24$，均是整数。数组的正向 roll 满足

$$
(\operatorname{roll}_{k}F)_j=F_{j-k},
$$

所以它取到 $\theta-\alpha$，再作空间 $R_\alpha$，与连续族
$F_\alpha(s,\theta)=R_\alpha F_0(s,\theta-\alpha)$ 相符。独立检查器直接用模 $N$ 索引和复数乘法重算三个实际网格，最大坐标差 $2.221\cdot10^{-16}$。所有固定帽顶点在三个时刻逐位相同。

## 3. 尾、公共接缝及上下帽

有限尾与 R6 collar 均由已审的精确物理半径网格/积分表示读取。对查询半径先用 Fraction 选择实际 span 和其局部参数；取多项式包含区间的中点作为网格数值代表，不把中点宣称为某个严格顶点区间证书。

上尾的坐标是

$$
xy=r e^{i\theta}+V_h(r,\theta),\qquad
z=H_c+\int_r^c w(s)\,ds-V_z(r,\theta).
$$

其中 common-cut 读取器的 $H_c$ 正是原 prefix 精确 cut 均值加 tail 扰动 cut 均值。因此反射覆盖整个 tail 的高度扰动；这里没有只反射非均值、遗漏均值或背景符号的问题。独立完整重放的最大接缝代表差与作者完全相同，为 $2.498001805406602\cdot10^{-16}$。

cut、finite-tail/R6 接口和 cuff 各只保留一圈共享顶点；镜像中央入口也只保留一圈。lower 由全部 upper band 的 $z$ 取负得到。上帽是固定圆盘加三个

$$
h\bigl(1-|x-b_j|^2/b^2\bigr)_+^3,\qquad
h=1/2000,\quad b=3/100,
$$

凸起，中心半径 $2/25$、角距 $2\pi/3$；下帽为平圆盘。脚本在 lower cap 分支正确移除了上帽凸起，未把它们镜像到下帽。所有凸起支撑都在 cuff 内部，因此 cuff 接口是平帽。

独立小检查的所有非帽上下圈 XY 差和完整 Z 反射差均为零；对固定 cap/cuff 圈从实际 XY 重算上述三凸起公式，符合机读报告中的数值容差。极点没有落入凸起支撑，使用 $\pm H_{\rm cap}$ 正确。

## 4. 面次序与数据格式

经线顺序从下极点开始，经过下帽、下尾、下 prefix、公共中央圈，再经过上 prefix、上尾、上帽到上极点；$\theta$ 按逆时针增加。条带三角形先沿 $\theta$、后沿经线前进，因此在柱状段法向向外，在下帽向下、上帽向上。下极点 fan 的索引次序给负 $z$ 法向；上极点 fan 给正 $z$ 法向。完整环序没有重复 cut/cuff/中央圈，极点也不是半径零的重复环。

实际三网格的面数组完全相同。独立检查器另核全部极点 fan 和四处代表条带的索引公式；它们与上述方向推导相符。完整边重数、连通和 Euler 检查见 independent_geometry 的另份实际 PLY 验证记录。

每个网格有 67,250 个顶点和 134,496 个三角形，使用 binary little-endian PLY，三个坐标为 float64，面为一个 uchar 计数加三个 int32 索引。独立解析重新计算精确字节长度，所有 face 计数均为 3、索引均在合法范围、所有顶点有限。每个未压缩文件约 3.363 MB，小于 5 MB；因为大于 1 MB，保存为 gzip，压缩文件也均小于 5 MB。

## 5. 独立重放命令与边界

完整 build 使用作者的冻结计划与已由另一代理核对的实际高度输入，输出到本审查者的新路径：

    python scripts/db6f-export-closed-mesh.py build \
      --plan notes/2026-11-09-db6f-visible-m8-plan.json \
      --height-samples notes/2026-11-09-db6f-visible-m8-heights.json \
      --out-prefix notes/2026-11-09-db6f-tail-review-visible-m8-replay

实际退出 0，约 2.32 秒。三件重复字节内容不必再次发布，原始文件的哈希已经逐件吻合；审查报告保留输出清单和可重放命令。随后运行独立小检查器，亦实际退出 0。

上文是数值导出程序及其实际结果的独立核对。连续 $C^2$、全相位嵌入和 reach 仍由 R17/R18 指定图及其证书支付。背景数值求积、反解、源函数求值、浮点三角及写入 double 后的完整顶点误差尚未作严格区间控制；没有据此声称 PL 网格本身精确等距、具有连续曲面的 reach，或已经满足 README 第 5 项。
