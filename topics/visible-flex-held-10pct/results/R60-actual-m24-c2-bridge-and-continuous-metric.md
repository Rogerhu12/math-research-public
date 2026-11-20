# R60：实际 M24 显式 C² 桥的连续几何与完整相对度量

日期：2026-11-20。维护会话：Astra-held10-1b6d88ec-20261120。

**状态：已证明并已实际执行全部连续区间覆盖。** 本结果是新多段轮廓、$q=.06$、材料圆化 $\lambda=.002,\tau=1,S=.5,b=.2,k=.2$ 的指定 M24 有限场的整个桥段结论。径向及角向均连续，采用同一固定 mean1168 与显式公共二 jet 的真实 $C^2$ 图。它不包含真实尾求解、完整闭面、全部时间族或准确圆弧 $\lambda=1$。

## 1. 明确的图与结论

使用[显式 M24 桥定义](../notes/2026-11-20-m24-r59-explicit-c2-bridge-certificate.md)中的对象。两个端点分别以所存 binary64 数作为精确有理数：

$$
s_b=\operatorname{binary64}(.49457743382696573),\qquad
s_e=\operatorname{binary64}(1.4252697037606197).
$$

原物理多项式及角样条在各节点采用共同右侧二 jet，最后节点采用末段左侧二 jet，再以精确五次 Hermite 相连。桥相位最后一段解析延拓到实际 $s_e$；半径 $a_*$ 是其正弦的真实原函数。没有把末端 clipped 查询函数或各段独立舍入的系数称为 $C^2$。

记公共角函数为 $e_*$，则

$$
\theta_*=\psi-\frac{e_*(s)}3\sin(3\psi),\qquad
P_*=a_*e_r(\theta_*)+G_*.
$$

$G_*$ 是完整 M24 共享 Hermite Fourier 场。桥上核心 lift 恒为零。固定原程序的 1168 个字面 binary64 角节点、精确等权 $1/1168$，用真实 Frenet 速度及角图对流计算有限均值 $M_*$，定义

$$
F_*(s,\psi)=P_*(s,\psi)+
\left(z_0+\int_{s_b}^{s}M_*(u)\,du\right)e_z.
\tag{1}
$$

[完整前缀高度证书](../notes/2026-11-20-m24-prefix-absolute-height-certificate.md)已对同一公共 Hermite / mean1168 / 真 primitive 对象证明

$$
.44631325197234495\le z_0\le .47839691621379593.
\tag{2}
$$

该前缀保持实际振幅 $\delta$，明确固定周期时长，使其在 $s_b$ 精确有 $(a,a',a'')=(1,0,0)$；与桥的共同均值 primitive 在此接口为 $C^2$。

以 $\theta_*$ 为材料角，目标度量是

$$
g_*=ds^2+a_*^2\,d\theta_*^2.
\tag{3}
$$

于是整个桥段有

$$
\boxed{\;
\left\|g_*^{-1/2}\bigl((DF_*)^tDF_*-g_*\bigr)g_*^{-1/2}
\right\|_{\rm op}<9.3\cdot10^{-7}.
\;}
\tag{4}
$$

这里指相对度量算子的本征值范数，表达式可在任意坐标中按相应目标正交标架解释。式 (4) 尤其保证本桥为浸入。另已连续证明

$$
|F_*|<1.245,\qquad F_*\cdot n_*>.3986798571,\qquad
\max(|\kappa_1|,|\kappa_2|)<8.367444.
\tag{5}
$$

法线方向与 R59 一致。式 (5) 由已付的连续扰动范围
$(V_0,\eta_1,\eta_2)<(.035,.179,1.639)$ 及 (2) 推得，不再留入口高度假设。局部浸入、支撑和曲率没有在本条中升级为完整闭面的嵌入或 reach。

## 2. 先认证的数学 jet 接口

连续计算先处理一个明确定义的中间接口 $D_0$：原精确二进制分片 $Y,e$、formal GL64 半径的实函数、源手填斜率 $a'_0=-\sin\phi$、最后相位的解析延拓，以及同一 1168 节点的真实有限均值 $M_0$。这里所有三角函数按实数数学函数解释。

它是源一阶 jet 的明确数学解释，**不是**宣称 formal GL 半径的真实导数恰好等于手填斜率，也不是原末端 clipped 查询函数的导数。后面单独用已证误差转到 (1) 的真实导数。

令

$$
\rho=1-e\cos(3\psi),\qquad
v=-\frac{e_s\sin(3\psi)}{3\rho}.
$$

计算坐标一阶接口为 $F_{s,0},F_{\psi,0}$。其目标正交材料标架为

$$
D_0=\left(F_{s,0}-vF_{\psi,0},\quad
\frac{F_{\psi,0}}{a_0\rho}\right),\qquad
E_0=D_0^tD_0-I.
\tag{6}
$$

本次实际连续覆盖证明

$$
\sup_{s\in[s_b,s_e],\,\psi\in\mathbb R/2\pi\mathbb Z}
\|E_0(s,\psi)\|_{\rm op}
\le 8.986280795398593\cdot10^{-7}
<9\cdot10^{-7}.
\tag{7}
$$

该数字是触发逐盒验收的充分上界；不声称它是误差最大值的紧估计，也不使用旧有限网格峰值代替 (7)。

## 3. 全角 Laurent 表示与先相消

记 $z=\exp(i\psi)$。圆基准的水平复表示为

$$
E=\exp(i\theta)=
z\exp\left(\frac e6(z^{-3}-z^3)\right).
\tag{8}
$$

水平 Fourier 扰动写作 $U=e^{i\psi}(R+iT)$，竖向扰动写作 $Z$。它们的 Laurent 系数均为实数；例如频率 $m_j$ 的 $R_j,T_j$ 对应 $1\pm m_j$ 处系数 $(R_j\pm T_j)/2$。定义

$$
\mathcal R=1-\frac e2(z^3+z^{-3}),\qquad
\mathcal T=\frac {e_s}6(z^3-z^{-3}),
$$

$$
B=a'_0E-a_0\mathcal TE+U_s,\quad
C=a_0\mathcal RE+\mathcal KU,\quad
W=M_0+Z_s,\quad V=\mathcal KZ,
\tag{9}
$$

其中 $\mathcal K$ 将第 $k$ 个 Laurent 系数乘 $k$。于是水平导数分别是 $B$ 与 $iC$，竖向导数分别是 $W$ 与 $iV$。$\theta_s=i\mathcal T$。

以 $*$ 表示系数卷积，以 $\operatorname{rev}$ 表示反转频率；实系数 Laurent 函数在单位圆上的共轭就是反转。计算坐标中的三个目标度量残差先作完整代数相消：

$$
\begin{aligned}
r_{ss}&=B*\operatorname{rev}(B)+W*W-\delta_0
+ a_0^2\mathcal T*\mathcal T,\\
r_{s\psi}/i&=
\frac{\operatorname{rev}(B*\operatorname{rev}(C))
-B*\operatorname{rev}(C)}2
+W*V-a_0^2\mathcal T*\mathcal R,\\
r_{\psi\psi}&=C*\operatorname{rev}(C)-V*V
-a_0^2\mathcal R*\mathcal R.
\end{aligned}
\tag{10}
$$

第二行实际 Fourier 系数还有因子 $i$，其 $\ell^1$ 范数不变。式 (10) 保留完整角图交叉项，未把计算坐标误当正交材料坐标。

(8) 的指数取 12 阶 Taylor 多项式。Banach 代数 $\ell^1$ 范数及 $|e|/3\le .1$ 给统一余项

$$
r_E\le
\frac{2(|e|/3)^{13}}{13!}.
\tag{11}
$$

例如从该余项引起的水平导数差满足

$$
d_B\le (|a'_0|+|a_0||e_s|/3)r_E,\qquad
d_C\le |a_0|(1+|e|)r_E.
$$

三个 Gram 分量的尾界分别为

$$
2\|B\|_1d_B+d_B^2,\quad
\|B\|_1d_C+\|C\|_1d_B+d_Bd_C,\quad
2\|C\|_1d_C+d_C^2.
\tag{12}
$$

有限向量半宽为 $\max(3M+1,3\cdot12+4)=73$，Gram 残差半宽为 146。受支持集限制截去的基准卷积项在代数上为零；没有用小系数阈值删项，也没有 FFT 或角采样余项。

## 4. 全径向 Taylor 包围与目标归一化

径向分割含物理 PPoly、角样条、晚期 cutoff 和三个桥相位的所有拼点。每个开片内均为明确的解析函数，使用其两侧闭区间极限覆盖节点。对原二进制多项式及固定节点的均值，二阶区间自动微分给出 (10) 各 Laurent 系数的 $s$ 导数。

若 $I=[c-h,c+h]$ 是其中一个子区间，对三个残差系数向量分别使用

$$
\|r(s)\|_1\le
\|r(c)\|_1+h\|r'(c)\|_1+
\frac{h^2}{2}\sup_I\|r''\|_1+
\text{式 (12) 的尾界}.
\tag{13}
$$

式 (13) 只在每个已分开的解析片上使用，不对整个拼接图增加全局 $C^3$ 假设。指数截断部分求径向导数；真实指数余项直接按整个 $I$ 的值界加入，因此没有遗漏指数尾的径向导数项。

若式 (13) 给三个上界 $b_{ss},b_{s\psi},b_{\psi\psi}$，并严格有
$a_0\ge a_{\min}>0,\rho\ge\rho_{\min}>0,|v|\le v_{\max}$，则 (6) 三个对称矩阵分量分别不超过

$$
\begin{aligned}
b_{11}&=b_{ss}+2v_{\max}b_{s\psi}+v_{\max}^2b_{\psi\psi},\\
b_{12}&=\frac{b_{s\psi}+v_{\max}b_{\psi\psi}}
{a_{\min}\rho_{\min}},\\
b_{22}&=\frac{b_{\psi\psi}}{a_{\min}^2\rho_{\min}^2}.
\end{aligned}
\tag{14}
$$

对称矩阵的算子范数不超过最大绝对行和，故
$\max(b_{11}+b_{12},b_{22}+b_{12})$ 为全区间、全角上界。未达到 $9\cdot10^{-7}$ 的盒按径向二分；无法证明 Frenet 正根的盒也必须二分，不能绕过定义域门。

实际 3342 次尝试中，1830 盒接受、1512 次二分，最终栈为空。所有接受盒的固定均值节点上正根平方下界至少
$2.526681016634668\cdot10^{-7}>0$。这是区间算法所给的保守下界，不能当作实际最小根值，更不能外推到不属于这 1168 个均值节点的另一个 Frenet 门。

## 5. 外向舍入的具体范围

四则、平方、根式与有限求和采用已提交 R23 outward kernel。固定字面角节点的三角值先用高精度区间再向外转 binary64；小角函数使用带显式余项的 Taylor 多项式。多项式常数作为精确二进制有理数解释，非二进制的除法常数经过有理到区间转换。

卷积使用实数 midpoint-radius 区间与直接实卷积，另支付浮点点积误差。每项至多 $n<10^6$ 个乘积，令 $u=2^{-53}$、
$\gamma=8(n+1)u\ge\gamma_{2n}$。非负卷积上界为

$$
\operatorname{up}\left(
\frac{\operatorname{up}(\operatorname{flconv}(x,y)+2^{-970})}
{1-\gamma}\right).
\tag{15}
$$

以此包围中心乘积的绝对误差及三个半径卷积项，再向外相加。$2^{-970}$ 在所允许长度下覆盖下溢绝对误差。全部进入范数的区间均检查有限性；分母下界和角对流上界也用区间四则求得。

可变系数累加器分别拥有上下界数组，拒绝共享端点内存。开发中的旧原型 session99823 曾有端点 alias，发现后已取消；其计数和上界均撤销，未用于本证明。这里仅使用修复后源码及 session58879 的完整实际终态。

## 6. 转到真实 C² 图

[显式桥证书 §6](../notes/2026-11-20-m24-r59-explicit-c2-bridge-certificate.md)的旧端恰是 (6)：同一 formal GL 半径、手填斜率、解析延拓、原分片 $Y,e$ 与 mean1168。其新端恰是 (1) 的真实归一化导数。该证书已独立支付共享 Hermite、真实背景原函数和 Frenet 均值的变化，给

$$
\|D_*^tD_*-D_0^tD_0\|_{\rm op}<3\cdot10^{-8}.
\tag{16}
$$

两个端点按各自明确半径归一化，故 (7)、(16) 与三角不等式立即推出 (4)。这里无需支付旧 GL6 高度值与真 primitive 的差：度量只用一阶导数，而绝对位置另由 (2) 直接锚定新图。

本条采用 (3) 的目标 $g_*$。如果选择另一原半径目标，还须单独应用已付的半径相对变化 $<1.637\cdot10^{-12}$；没有宣称这次表示转换保持原查询程序的每个物理函数逐字不变。后续正式固定参数精化必须固定整个新定义，不能逐网格重选。

## 7. 实际执行、身份与复现

实际终态：本地 session58879，观察到 exit 0，耗时 1009.640527386 秒。紧凑记录见[执行 JSON](../notes/2026-11-20-m24-bridge-continuous-metric-execution.json)。

| 对象 | SHA-256 |
| --- | --- |
| [连续证书源](../scripts/resume_m3/certify_bridge_metric_fourier_taylor.py) | fe99f0afc6ed90dac1b9b3616c857421fa621901958dfbafdbb26191c5766bb2 |
| M24 run.json | c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a |
| M24 physical.npz | f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d |
| 完整本地标量输出 | 0bc13cc9d39bce280dffd5cbd0da055cffc439b5bdde6ea696c7b56e2f38e9f7 |
| 复用固定 mean 核 | ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5 |
| 复用 R23 outward 核 | 6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7 |

先按[原 M24 前缀记录](../notes/2026-11-20-m3-newg-wide-m16-spectrum-and-m24-prefix.md)重建相同输入，再运行：

~~~bash
HELD10_WORK=/workspace/scratch/1b6d88ecddf3
HELD10_REPO="$HELD10_WORK/math-research-public"
python -u "$HELD10_REPO/topics/visible-flex-held-10pct/scripts/resume_m3/certify_bridge_metric_fourier_taylor.py" \
  --source-run "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$HELD10_WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --interval-kernel "$HELD10_REPO/topics/visible-flex-held-10pct/scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py" \
  --mean-nodes 1168 --exp-order 12 --target 9e-7 \
  --out "$HELD10_WORK/root-work/m24-bridge-gram-certificate.json"
~~~

本次没有重新求解 BVP、改变原验收门或改写正在运行的真实尾。可再生场及中间系数数组不入 Git/Release。

## 8. 仍须接着支付的主线

当前指定 M24 图仅在 $\lambda=.002$。含核心 lift 的整个前缀连续度量、真实尾与全部 Cartesian 共缝、准确圆弧 $\lambda=1$、完整闭族及全时间 reach、固定 $H$ 与全 $O(3)$ 非全等、冻结全部参数后的空间/频率/时间精化仍未完成。后续真实 DN 若更新有限场或物理参数，必须对该新输入重新绑定并认证，不能无条件继承本数值证书。
