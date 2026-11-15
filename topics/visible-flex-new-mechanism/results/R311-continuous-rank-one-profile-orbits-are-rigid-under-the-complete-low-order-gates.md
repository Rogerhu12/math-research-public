# R311：完整低阶门使固定 rank-one 包空间内的任意连续轨道刚性

日期：2026-11-15。**完整纸面证明，没有执行求积、符号程序、profile 扫描、人工测试或研究计算。**

[R304](R304-positive-one-history-remainder-excludes-disjoint-real-rank-one-circles.md) 排除了同一小共振偶端芽上的不交实 rank-one 微包圆。本稿指出其中的核心身份其实逐参数成立：不需要余弦／正弦，不需要闭曲线，也不需要先把轨道写成某个 $GL_2$ 圆。只要 profiles 始终位于同一个固定 rank-one 包空间，原完整必要门就迫轨道恒定。

同时，原固定三矩本身并没有这种刚性。第2节给一个准确的非圆三矩轨道，说明不能把真正的第四阶障碍误归因于三条二次约束。这也明确排除“只把圆换成椭圆或非圆系数曲线”作为当前构造的修复办法。

来源：[R56 原恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R184 任意固定首阶 profile 的第四联合式](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R221 完整线性 ruling 响应](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R243 原偶部商](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)、[R296 完整零／一层](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)、[R300 原 directed 行](R300-one-history-tail-compensation-and-thirty-eight-dimensional-principal-space.md)及 R304。

## 1. 固定资料与参数无关的原式

固定 R304 同一个真实端芽：
$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\kappa/h,\qquad
\varepsilon=\kappa^2/4,\quad
0<\kappa^2<1/100,\quad h_e>0.
\tag{1}
$$
所有参数在实际几何的初始设计时选择。本文不改变已选度量、右锚、空间 collar 或原 gauge 的定义。

固定有限个非零实光滑紧 profiles $u_i$，其支撑两两不交，均位于同一双零 collar 内。取固定种子
$$
f=\sum_{i=1}^N a_i u_i.
$$
令 $T$ 为一个连通参数空间，$\tau_0\in T$，并取连续实系数
$$
\phi_\tau=\sum_{i=1}^N c_i(\tau)u_i,\qquad
c_i(\tau_0)=a_i.
\tag{2}
$$
应用时 $T$ 可以是区间、圆或更高维连通参数域。不要求轨道是三角多项式。这里的 $u_i$ **不随 $\tau$ 变化**；各实际位置、宽度和形状也保持固定。

定义
$$
d_i(\tau)=a_i^2-c_i(\tau)^2,\qquad
C_i=\int_I(u_i'')^4>0,\qquad
D_\tau=f\odot f-\phi_\tau\odot\phi_\tau.
\tag{3}
$$
原对称槽 $\odot$ 的含义不变。

R296 的完整第四恢复先以任意一对 $(\phi,D)$ 写成双线性／三线性式，随后才把圆代入。R300 的两类原式
$$
\begin{aligned}
\mathscr L^X(\phi,D)
&=2\mathcal T(XD;D)-4\mathcal T(\phi;\phi,XD),\\
\mathscr H^{Y\to X}_{j_0}(\phi,D)
&=-I_{j_0}(YD,XD)
+2I_{j_0}\{\phi,Y(\phi,XD)\}
\end{aligned}
\tag{4}
$$
没有外部轨道参数的导数。因此，R304 的逐点 Green、self、原能量和 annihilator 推导在每个固定 $\tau$ 对(3)原样成立。不能将这个事实扩大为任意新轨道已经满足全部原 range；所需门会在第3节逐项假设。

## 2. 固定三矩允许什么：圆的部分刚性与真实非圆自由度

原三矩是
$$
\mathbf I(u,v)=\left(
\int u''v'',\ \int xu''v'',\
\int\{x^2u''v''+2u'v'\}
\right).
$$
固定度量的这部分必要条件为
$$
\mathbf I(\phi_\tau,\phi_\tau)=\mathbf I(f,f).
\tag{5}
$$
由于支撑不交，令
$$
m_{j,i}=I_j(u_i,u_i),\qquad
M=(m_{j,i})_{\ 0\le j\le2,\ 1\le i\le N},
$$
则(5)准确等价于
$$
\boxed{M(c(\tau)^2-a^2)=0.}
\tag{6}
$$
平方逐分量进行。这里的 $m_{2,i}$ 保留 $2\int(u_i')^2$，不是点质量二阶矩。

### 2.1 已正交的二维平面里没有新的“椭圆自由度”

若既有两个实 profiles $f,g$ 满足
$$
I_j(f,g)=0,\qquad I_j(f,f)=I_j(g,g)\quad(j=0,1,2),
$$
则在这个二维平面内，
$$
I_j(\alpha f+\beta g,\alpha f+\beta g)
=(\alpha^2+\beta^2)I_j(f,f).
$$
因 $f\ne0$ 时 $I_0(f,f)>0$，(5)迫
$$
\alpha^2+\beta^2=1.
\tag{7}
$$
所以在同一已经正交归一的二维系数平面，把圆改写成不同速度或不同线性坐标，不增加满足(5)的实际首阶状态。

更一般，若用两个固定向量写
$\phi_\tau=A\cos\tau+B\sin\tau$ 并要求(5)对全部 $\tau$ 成立，比较 $1,\cos2\tau,\sin2\tau$ 得
$$
I_j(A,A)=I_j(B,B)=I_j(f,f),\qquad I_j(A,B)=0.
$$
这在三个实际二次形式中仍是同一个正交圆。不同外观的坐标椭圆不能代替这些真实身份。

### 2.2 较高维里三矩确有非圆连续轨道

三矩本身也不迫一般轨道恒定。例如在一个有 $N\ge4$ 个非零种子系数的固定包空间，取任意
$$
0\ne v\in\ker M.
$$
这样的 $v$ 存在，因为 $M$ 至多三行。对充分小的实参数 $t$，定义
$$
\boxed{
c_i(t)=\operatorname{sgn}(a_i)\sqrt{a_i^2+t v_i}.
}
\tag{8}
$$
可明确取
$$
|t|<\min_{v_i\ne0}\frac{a_i^2}{2|v_i|},
$$
使根号内严格为正。于是 $c(0)=a$，轨道光滑、非恒定，并且
$$
M(c(t)^2-a^2)=tMv=0
$$
准确成立。它不需要求积或新的存在性假设；$M$ 使用实际固定 profiles 的真矩。

若种子中有零系数，这个例子只在至少四个非零活动系数上使用。式(8)只支付(5)，**没有**支付 Gaussian 面积、二层或一层。这段建设性例子用来区分：第三节的刚性确来自更完整的原条件，不是三矩的维数计数。

## 3. 一条有限必要子系统已经迫逐分量平方固定

采用 R304 的原方向
$$
P=\Phi_{r_0},\quad
W=aR+bS,\quad
Z=dL+e_-U,\quad B_{-3}=c_PP.
$$
所有几何常数均按 R304(4)，特别 $c_P(d+7e_-)\ne0$。

对每个 $\tau$ 假设以下原必要门成立：

1. 原三矩(5)及相关低阶 range，使 $PD_\tau,WD_\tau,ZD_\tau$ 是合法的真实 whole 槽；
2. 原完整 $A_{-1,-3}$ 面积的 $I_0$ 门；
3. 三个原 directed 行
   $$
   \mathscr H^{P\to P}_{2}=
   \mathscr H^{W\to P}_{1}=
   \mathscr H^{Z\to P}_{0}=0;
   \tag{9}
   $$
4. 完整 $E_{-3}$ 一层中 $\sigma h^{-2}j^0$ 的原系数为零。

当整个第四 ruling 偶部通过原 $\mathcal W_e$ 商门时，上述都是必要条件：第3项来自对应完整对称乘积及面积的和／差，第4项来自真实词独立性。这里没有把某个 directed 行自行加强为未经原式要求的新门。

由旧面积的原非紧 self 与零跨核，逐参数准确有
$$
\mathcal A_\tau=\sum_i c_i(\tau)^2d_i(\tau)C_i=0.
\tag{10}
$$
R304(26)–(28)完全没有用到 $c_i=a_i\cos\theta+b_i\sin\theta$；它们在(10)上是关于实际 $a_i,c_i$ 的代数与积分身份。因此由(9)得到
$$
\frac1{c_P}[\sigma h^{-2}j^0]\mathscr R_{-3,\tau}
=-D_\kappa\sum_i d_i(\tau)^2C_i,
\tag{11}
$$
其中
$$
D_\kappa=
\frac{16+184t-1713t^2-2475t^3-4590t^4}
{288\kappa(51t^2+2t+8)},\qquad t=\kappa^2.
$$
在(1)的范围内 $D_\kappa\ne0$，且全部 $C_i>0$。故第4门迫
$$
\boxed{d_i(\tau)=0\quad\text{对每个 }i,\tau.}
\tag{12}
$$
换言之，
$$
\boxed{c_i(\tau)^2=a_i^2.}
\tag{13}
$$

这个论证没有取轨道平均，没有用 R304 的 $A_4=5C_{22},E_4=C_{22}$，也不需要另一个特定相位。圆全角在 R304 中用于产生 $\theta=\pi/2$ 的显式严格正数；本稿用逐参数必要门得到更直接的离散状态约束。

## 4. 连续性和零种子分量

若 $a_i=0$，(13)立即给 $c_i(\tau)=0$；不能在这个固定包轴上凭非圆轨道新激活一个 profile。

若 $a_i\ne0$，则
$$
c_i(\tau)/a_i\in\{-1,1\}.
$$
这是连通空间到离散两点集的连续映射，故为常数。初值(2)迫该常数为1。因此
$$
\boxed{c_i(\tau)=a_i\quad\text{对每个 }i,\tau,\qquad
\phi_\tau\equiv f.}
\tag{14}
$$

这证明如下精确结论。

**轨道刚性定理。** 在同一(1)真实端芽、同一固定实不交微包空间和同一初始种子上，任何满足第3节有限必要子系统的连续轨道，在其种子所属的连通分支上恒定。

如果参数域不连通，(13)最多允许不同连通分支取不同的有限符号选择；它不产生从原种子出发的连续变形。若去掉连续性，跳变符号同样不是原问题要求的光滑参数族。

## 5. 对下一机制的准确含义

式(8)说明较高维固定三矩流形确有真实非圆自由度，但(11)把这些方向全部截断。因此，把现有圆改成椭圆、一般有限 Fourier 系数曲线、某条非 $GL_2$ 平面曲线或更高维的固定包幅值轨道，都不能在这个端芽上同时保全部原门。增加时间、复制次数、宽度参数或同一固定包空间的坐标数，也不改变(13)。

本文不处理以下两类真正不同的对象：

- 一个活动区间中，$f$ 与 $\phi_\tau$ 不是同一实 profile 的常数倍，或 profile 形状随参数变化而离开了这个固定空间；
- 从实际几何的最初设计改用其他端芽、端口类型或拼接结构。

第一类必须重新计算 R304 的 mixed 原 annihilator，不能只由参数更多断言能逃。第二类也必须保真实水平方程、匹配与 frame、完整低阶历史和同一目标；不能把新几何当成旧 fixed-$g$ 解的免费重参数化。

本稿只完成固定 rank-one 包空间内的准确刚性。它没有判断一般局部 rank-two 轨道、不同合法端芽或整个主课题的可解性。
