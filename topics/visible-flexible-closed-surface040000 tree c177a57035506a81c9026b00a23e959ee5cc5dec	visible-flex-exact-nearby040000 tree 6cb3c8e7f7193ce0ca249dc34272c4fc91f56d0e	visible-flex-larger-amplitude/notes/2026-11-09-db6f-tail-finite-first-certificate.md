# 显式有限尾及 R6 圆领的一阶连续证书

2026-11-09，`/root/tail_theory`。状态：**完整有限表示的条件推导与向外舍入计算，待独审**。这不是无限非线性尾或精确等距解的存在定理。

## 1. 被认证对象

输入是宏观 `flat17`、`q=.1`、M8 真正前缀/尾联解的 32 步 shooting checkpoint，经全 XYZ 导出得到的有限表示：

`notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json`。

它包含从 raw node 8 到 cut 的 4638 个共节点。每个节点的角向展开为

$$V_x+iV_y=\sum_{m\equiv1\pmod3}a_m(r)e^{im\theta},\qquad
V_z=\sum_{m\in\{0,3,\ldots,24\}}c_m(r)\cos(m\theta).$$

系数、节点与导数数据的 binary64 值被当作精确实数定义；不是给原 ODE 解加了未经计算的误差条。背景是原来的同一个旋转曲面，$X_h=r e^{i\theta}+V_h$。高度背景不参与下面的一阶水平几何证书。

每个径向跨上的 $V_r$ 是四次多项式，由两端 $V_r,V_{rr}$ 和物理中点的 $V_r$ 决定；$V$ 由对 $V_r$ 精确积分定义。储存的后续节点位置只是此精确积分的浮点近似值，不是额外的插值约束。这消除了对量化位置值做二次差分的问题，并使有限表示恰为 C²。

在最深端与原 cuff 之间附加相同 Fourier 系数的 R6 五次 Hermite 圆领。它把 $V,V_r,V_{rr}$ 从最深端延拓到 cuff 的全零二阶 jet，故与旋转帽恰为 C²。无限旋转背景仍是原固定背景；这里未改变物理 metric 或截断它的材料定义。

## 2. 多项式与区间算法

设跨度长 $L>0$，局部坐标 $t\in[0,1]$，令端点数据为 $u_0,u_1,v_0,v_1$，其中 $u=V_r$、$v=LV_{rr}$，中点数据为 $u_m$。置

$$A=16u_m-8(u_0+u_1)-2(v_0-v_1).$$

则 $G(t)=V_r$ 的五个幂系数为

$$u_0,\quad v_0,\quad -3u_0+3u_1-2v_0-v_1+A,
\quad2u_0-2u_1+v_0+v_1-2A,\quad A.$$

直接代入可核对 $G(0),G(1),G'(0),G'(1),G(1/2)$。其精确积分增量为

$$\Delta V=L\left[\frac7{30}(u_0+u_1)+\frac8{15}u_m+
\frac1{60}(v_0-v_1)\right].$$

程序从最深端的精确 binary64 $V$ 开始，用向外舍入区间逐跨累加该式，因而所有节点常数项被包围。没有使用仅近似的储存累积位置替代精确积分定义。

对次数 $d$ 的幂多项式 $p(t)=\sum p_jt^j$，Bernstein 控制点为

$$b_k=\sum_{j=0}^k\frac{\binom{k}{j}}{\binom dj}p_j.$$

由于 Bernstein 基函数非负且和为一，对任一角导数阶数 $\ell$，完整平面 Fourier 和满足

$$\sup_{t,\theta}\left|\partial_\theta^\ell
 \sum_m p_m(t)e^{im\theta}\right|
\le\max_k\sum_m |m|^\ell |b_{k,m}|.$$

高度余弦和也满足相同的绝对值界。因此无需角向采样；没有把遗漏频率解释为无限 Fourier 解的小尾，所认证对象本来就是上述有限 Fourier 多项式。

程序使用 `db6f-audit-continuous-hermite.py` 的闭区间类。输入浮点数为点区间；每次加、乘、除之后用 `nextafter` 向外扩展；有理系数用 `Fraction` 转换后比较精确有理值以确定端点。Fourier 绝对和逐项向上舍入。对 R6 圆领直接使用同一 Bernstein 过程，分母半径采用 cuff 的严格正下界。

## 3. 一阶界如何给平面几何

记 $u=V_h$，并在每一跨度有

$$|u|\le a_0,\qquad |u_r|\le a_1,\qquad |u_\theta|\le b_0,
\qquad r\ge r_->0.$$

以 $\det(\partial_rX_h,\partial_\theta X_h)$ 为平面 Jacobian；其圆背景值为 $+r$。二维行列式的双线性和 $|\det(v,w)|\le|v||w|$ 给

$$\frac{\det(X_{h,r},X_{h,\theta})}{r}
\ge1-a_1-\frac{b_0}{r_-}-\frac{a_1b_0}{r_-}.$$

独立地，极角导数的分子满足

$$\frac{\det(X_h,X_{h,\theta})}{r^2}
\ge1-\frac{a_0}{r_-}-\frac{b_0}{r_-}
-\frac{a_0b_0}{r_-^2}.$$

若第二式严格为正且 $a_0<r_-$，角曲线不经过原点，其极角严格递增。沿 $r e^{i\theta}+s u$、$0\le s\le1$ 的同伦亦不经过原点，所以绕数为一。故每条水平参数截面是严格星形简单闭曲线。此处“水平参数截面”指固定材料半径 $r$ 的水平投影；高度可以随角度变化，未假定该空间截面位于水平平面。

这些是连续的有限表示结论。若上尾使用外向参数 $X_\theta\times X_r$，其水平面积投影分量是上述 Jacobian 的相反数，应用散度公式时必须保留方向。

## 4. 宏观 M8 的认证结果

运行：

```sh
python scripts/db6f-tail-first-bounds.py \
  notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  notes/2026-11-09-db6f-tail-first-flat17-m8-q10-n8-s32.json
```

整个尾，包括从 node 8 到 cuff 的精确 R6 圆领，向外舍入结果给

$$|V_h|\le 0.00013909529395060973,
\qquad |V_z|\le0.0008350432938459332,$$

$$\det(X_{h,r},X_{h,\theta})/r\ge0.9949233155001174>0.$$

每一截面的极角分子下界也严格为正，且 $|V_h|/r<1$，所以所有截面简单。报告分别列出有限外段与精确圆领的全部一、二阶 Fourier 粗界；二阶粗界在这里没有被用于推出曲率或 reach。

该结果能为尾部体积矩积分提供有用输入，尤其优于粗需求 $|V_h|\le.02$、$|V_z|\le.01$。但完整体积矩还依赖前缀接口、竖直定位、外向方向与实际闭嵌入，不能由本报告单独推出。

## 5. 范围限制

这是一份保存的有限 C² 显式映射的连续证书。它不认证原 Darboux 方程、同 metric 的全曲面误差、曲率、reach、无限非线性稳定图、精确解极限、前缀/尾接口或 README 完成。特别是把径向导出网格加密而保留旧步长求得的 shooting checkpoint，会暴露旧 CP 的离散误差；真正径向收敛须在相同物理 metric 下同步重新求解 CP。

较新的 `db6f-tail-increment-export.mjs` 还将径向节点定义为局部积分增量的精确和，并用一个精确有理归一化保持两端锚点不变。该脚本改进表示方式，未更改 g。本文所列宏观数值使用前述冻结 int2 文件；后续新数据须独立重跑，不能沿用本证书。
