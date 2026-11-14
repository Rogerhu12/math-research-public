# R12：ψ 扭曲的准确闭合负曲率核心

**状态：下文的闭合、正则性、固定度量、半转与曲率公式已证明；宏观幅度和嵌入性等待公开 Actions 几何筛。没有圆领连接，也没有满足课题完成标准的闭曲面。**

日期：2026-11-14。当前文件给出独立新构造的完整证明，使用公开 R44 的球面导线机制，见本题 [R6](R6-nonplanar-halfturn-phase-assembly.md)。原 R44 核心幅度限制见 [R11](R11-ruled-core-amplitude-limits.md)；这里改变导线，通常仅保留三重旋转对称，不能套用 R11 对**完整六重对称像集**的幅度上界。

**后续拓扑限制：**[R23](R23-warped-core-linking-obstruction.md) 已证本文正则Jordan投影核心的framing为+3，不能经嵌入annulus接到开放平圆领。本文准确闭合、局部度量及几何计算保留；原圆领封口目标已被排除。

## 1. 两个角变量与准确闭合

用 $\phi\in\mathbb R/(2\pi\mathbb Z)$ 表示构造角，$u,v\in\mathbb R$ 是固定参数，$b>0$ 是整体比例。设

$$
\chi=3\phi,\qquad \psi=\phi+u\sin3\phi+v\sin6\phi,
\qquad p=\psi'=1+3u\cos\chi+6v\cos2\chi.
$$

令

$$
a=\frac12-\frac32v,\qquad
\eta=\frac{-2a}{3+\sqrt{9-4a+4a^2}},\qquad
\sigma=\sqrt{1-\eta^2},
\tag{1}
$$

并在水平复坐标 $W=x+iy$ 中定义球面导线

$$
d_W=e^{i\psi}(-\sin\chi+i\eta\cos\chi),
\qquad d_z=-\sigma\cos\chi.
\tag{2}
$$

显然 $|d|=1$。以

$$
c_\phi=b\,d\times d_\phi
\tag{3}
$$

定义中心曲线。直接叉积得到

$$
\begin{aligned}
(d\times d')_W
 &=\sigma e^{i\psi}\big[-p\sin\chi\cos\chi
       +i(3+\eta p\cos^2\chi)\big],\\
(d\times d')_z
 &=p(\sin^2\chi+\eta^2\cos^2\chi)+3\eta.
\end{aligned}
\tag{4}
$$

平移 $\phi\mapsto\phi+2\pi/3$ 时水平导数乘 $e^{2\pi i/3}$，因此其三个分段积分之和为零。竖直周期积分为

$$
\int_0^{2\pi}c_z'\,d\phi
=2\pi b\,[a+(1-a)\eta^2+3\eta],
\tag{5}
$$

因为

$$
\frac1{2\pi}\int_0^{2\pi}p\sin^2\chi\,d\phi
=\frac12-\frac32v=a.
$$

$u$ 项的平均值严格为零。式 (1) 是方程
$a+(1-a)\eta^2+3\eta=0$ 在 $(-1,1)$ 中的唯一根。
证明：该二次式在 $-1,1$ 的值分别为 $-2,4$，故恰有一个区间内的根；式 (1) 连续、分母恒正，在 $a=0$ 给零，且不能穿过 $\pm1$。此写法也不在 $a=1$ 发生伪奇点。

所以 $c$ 严格闭合。将水平积分常数选为使 $c(\phi+2\pi/3)=Q_{2\pi/3}c(\phi)$，竖直积分常数取零平均，就有完整 $C_3$ 对称。水平常数可只用第一段积分 $J=\int_0^{2\pi/3}c_W'\,d\phi$ 确定：

$$
c_W(0)=\frac{J}{e^{2\pi i/3}-1}.
\tag{6}
$$

下面的半转对称还保证式 (6) 是实数。

## 2. 竖直坐标与正则性不需数值积分

对式 (4) 展开三角函数并利用式 (5) 消去常数项，得到准确零平均原函数

$$
\begin{aligned}
\frac{c_z}{b}={}&
\frac{u(1+3\eta^2)}4\sin3\phi
+\left[-\frac{\sigma^2}{12}
       +\frac{v(1+\eta^2)}2\right]\sin6\phi\\
&-\frac{u\sigma^2}{12}\sin9\phi
-\frac{v\sigma^2}{8}\sin12\phi.
\end{aligned}
\tag{7}
$$

特别地，$v=0$ 保留原 R44 的 $\eta=-3+2\sqrt2$，而 $u$ 可自由改变三瓣形状。

方向速度满足

$$
k^2:=|d_\phi|^2=(3+\eta p)^2+\sigma^2p^2\sin^2\chi.
\tag{8}
$$

当 $\sin\chi\ne0$ 时，右侧不能为零：若第二项为零，$p=0$，第一项等于 $9$。当 $\sin\chi=0$ 时，$p=1+6v\pm3u$。因此准确的全角正则性判据仅为

$$
3+\eta(1+6v-3u)\ne0,
\qquad
3+\eta(1+6v+3u)\ne0.
\tag{9}
$$

例如 $v=0,\ |u|\le1.2$ 时，$k\ge3-4.6|\eta|>2.21$。这只是方向正则性，不是中心曲线或带面的全局嵌入证明。

## 3. 固定度量与完整端口二阶导数

定义材料角 $\theta$，使

$$
\ell(\phi)=\int_0^\phi k(r)\,dr=q\theta,
\qquad q=\frac1{2\pi}\int_0^{2\pi}k(r)\,dr.
$$

只要式 (9) 成立，这给圆周的光滑微分同胚。令

$$
X(s,\theta)=c(\phi(\theta))+s\,d(\phi(\theta)).
\tag{10}
$$

因为 $d\perp d_\phi$，且 $d\times d_\phi$ 与 $d_\phi$ 正交等长，

$$
g=ds^2+q^2(b^2+s^2)d\theta^2,
\qquad a(s)=q\sqrt{b^2+s^2}.
\tag{11}
$$

这对所有 $s$ 是准确浸入度量，且
$K=-b^2/(b^2+s^2)^2<0$。公式没有除以 $\mathrm{II}_{\theta\theta}$、中心线曲率或任何会因非凸截面变号而消失的量。

脚本返回与既有连接器相同的端口数组：`inlet(theta,s,derivative=j)` 的形状为 `(3,N,3)`，依次为 $\partial_\theta^jX,\partial_\theta^jX_s,\partial_\theta^jX_{ss}$。径向数据是

$$
X=c+sd,\qquad X_s=d,\qquad X_{ss}=0,
$$

角向链式系数为

$$
\phi_\theta=\frac qk,
\qquad
\phi_{\theta\theta}=-\frac{q^2k_\phi}{k^3}.
\tag{12}
$$

在选定 $u,v,b$ 后，$q$ 的积分定义属于**固定度量本身**；后续加密不能通过重新优化这些参数冒充固定度量收敛。当前 `WarpedRuledCore` 的浮点求积用于求解器接口；独立的区间积分给出准确 $q$ 的包围。

## 4. 半转与宏观三瓣的一阶来源

由于 $\chi,\psi$ 都是奇函数，取 $A_x=\operatorname{diag}(1,-1,-1)$ 有

$$
d(-\phi)=-A_xd(\phi),\qquad c(-\phi)=A_xc(\phi).
\tag{13}
$$

$k$ 是偶函数，所以材料角保留同一对称。准确核心满足
$X(-s,-\theta)=A_xX(s,\theta)$，包含组装所需的完整位置二阶导数关系；因此可使用 R6 的半转组装条件。若接现有圆尾坐标 $(r\sin\theta,-r\cos\theta,C)$，应对**全部**核心位置与导数统一水平转 $-\pi/2$，把半转变为 $A_y$，不能只重设端圈中心或材料相位。

在 $v=0,u=0$ 附近，$\eta$ 不随 $u$ 变。对水平中心曲线准确求一阶变化：

$$
\left.\partial_uc_W\right|_{u=0}=b\sigma\left[
\frac{7+5\eta}{16}e^{4i\phi}
+\frac{2-\eta}{2}e^{-2i\phi}
+\frac{1+\eta}{20}e^{10i\phi}
+\frac{1-\eta}{32}e^{-8i\phi}\right].
\tag{14}
$$

相对于原主圆半径 $R=b\sigma(6+\eta)/2$，三瓣径向一阶系数为

$$
\frac{23-3\eta}{8(6+\eta)}u\approx0.5043u.
\tag{15}
$$

式 (14) 给出测试 $u=.6,.8,1,1.2$ 的具体理由；它不保证有限 $u$ 时的 Hausdorff 振幅、不保证嵌入，也不能替代连续几何筛。新项一般破坏原 R44 核心的六重像集对称，但保留三重旋转和式 (13)。

## 5. 局部曲率预算与未解决的非局部问题

令 $\kappa=\det(d,d_\phi,d_{\phi\phi})/k^3$ 是单位球面导线的有符号测地曲率，$R_s=\sqrt{b^2+s^2}$。在正交基 $(X_s,X_\theta/a)$ 中，形算子为

$$
S=\begin{pmatrix}
0&-b/R_s^2\\
-b/R_s^2&\kappa/R_s
\end{pmatrix}.
\tag{16}
$$

故同一 $\phi$ 上最大绝对主曲率随 $|s|$ 不增，且在中央截面等于

$$
\Lambda(\phi)=\frac{|\kappa|+\sqrt{\kappa^2+4}}{2b}.
\tag{17}
$$

这和 rectifying flat core 的 $\kappa_{\rm space}+\tau^2/\kappa_{\rm space}$ 不同，没有小中心线曲率的除法。脚本同时给出 $\sup\Lambda$ 的连续上界和由区间小片推出的下界：前者是局部预算，后者可与完整曲面直径下界合用，排除必然违反 reach 比例的参数。两者都不是 reach 的下界。

真正的 reach 还要控制所有非局部法弦：对完整闭嵌入面，任意两点 $x,y$ 的必要约束为

$$
\operatorname{reach}\le
\frac{|x-y|^2}{2|n_x\cdot(y-x)|}
$$

（分母为零的对忽略）。脚本在三个 $s$ 层上报告浮点样本，只作诊断；未把网格上的最小值当成全曲面 reach 证书。当前也尚未证明每个筛选核心嵌入。

## 6. 连续中心曲线误差与投影接口

`certified_centerline(u_text,v_text,scale_text,N)` 把输入十进制字符串当作准确实参数，以 50 位十进制定向区间计算式 (1)、(2)、(4)、(7) 及前三阶导数。$N$ 为 6 的倍数。令 $h=2\pi/N$，全角导数上界为 $M_j\ge\sup|c^{(j)}|$。

每片用中点积分计算 $c'$，每个水平分量误差不超过 $M_3h^3/24$，累加后通过式 (6) 包围准确锚点。每个顶点 box 另外包含参数根、三角函数与算术舍入误差。取其二进制中点形成多边形，统一 Euclidean 误差为 $\varepsilon_v$。真实曲线到该有序多边形及反向的距离均不超过

$$
\varepsilon=\varepsilon_v+M_2h^2/8.
\tag{18}
$$

这是逐片线性插值误差，不以样本差代替余项。最后一片利用准确闭合连接到第一个顶点。方向弧长积分使用同一中点公式，并由 $d',d'',d'''$ 的区间给 $k''$ 上界。

稳定 API：

| 字段 | 含义 |
|---|---|
| `vertices` | `(N,3)` 二进制中点；对距离模块是准确二进制坐标 |
| `vertex_boxes` | 每个准确 $c(2\pi j/N)$ 的三分量区间 |
| `vertex_error` | 统一三维 Euclidean 中点误差上界，Decimal |
| `position_cells` | 每个完整参数片的三坐标包围 |
| `derivative_cells` | 每片 $c_\phi$ 的三坐标包围 |
| `second_derivative_upper` | 全角 $M_2$，Decimal |
| `report` | 可存 JSON 的参数、误差、曲率、正则性和状态 |

`warped_ruled_projection.py` 由另一独占脚本消费此接口。拟用旋转见证点到**整个投影填充域**的距离，而非只到边界：证明该点有一条与曲线正距离的通向无穷射线，再由式 (18) 的误差扣减给到填充域的下界；不预设径向图或 Jordan 性。

这仍是条件预算：若核心半宽为 $w$，其水平投影在 $\operatorname{Fill}(c_W)+\overline B_w$ 内。若将来的整个连接和帽也在同一集合内，则旋转中央点得到的平面距离下界再减 $w$，才是完整像集的 $\delta_{\rm hold}$ 下界。若整个闭面还满足 $|z|\le Z$，可用

$$
D\le\sqrt{(\operatorname{diam}c_W+2w)^2+4Z^2}
\tag{19}
$$

作全曲面直径预算，因为填充域包含在边界的凸包内。所有包络条件都必须由实际连接独立检查；核心、参考母线或材料位移都不能替代它们。

## 7. 已做的廉价实现检查与公开 Actions 命令

`notes/warped-ruled-core-smoke-20261114.json` 只检查人工参数 $u=.13,v=.02,b=1$，没有候选扫描或优化：

- $|d|^2-1$ 最大误差 $2.23\cdot10^{-16}$；方向一至三阶导数四点差分相对误差 $1.1$–$1.4\cdot10^{-11}$。
- 竖直有限谐波原函数的导数误差 $9.16\cdot10^{-16}$；诱导度量相对误差 $6.67\cdot10^{-16}$。
- 中央完整半转位置二阶导数误差 $1.82\cdot10^{-14}$。
- 零扭曲时与旧 R44 全部端口导数一致到 $4.05\cdot10^{-14}$。
- 一个 24 片的人工参数区间接口检查通过；浮点参考点与区间端点的最大舍入级差为 $3.34\cdot10^{-16}$。它只检查代码接口，不构成参数搜索或新的严格误差来源。

真实筛选由公开仓库 Actions 执行；脚本为研究扫描显式检查仓库环境。建议第一轮：

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/warped_ruled_core.py \
  --warp-u .6,.8,1,1.2 --warp-v 0 --scale 1 --half-width .05 \
  --nodes 1536 --sample-angles 384 \
  --out "$RUN_DIR/warped-ruled-u-scan.json"
```

数据逐候选写入 JSON，记录源码与辅助脚本哈希、Actions 来源字段。若几何预算通过，才固定一个参数继续准确核心到圆尾的连接；单独放大 $b$ 不会改善任何无量纲比例。当前不修改已冻结的旧 `ruled_core_geometry.py` 或 `ruled_core_to_tail_bvp.py`。
