# 显式反射图的真实target简单根与局部解析span

状态：**已完成有限输入的有向区间证书：一个实际target简单根及其
实collar；不是全体型别、全传递或非线性等距存在性证书。**

## 1. 对象准确区分

输入来自原 `type_fixed_step02.npz`（SHA256
`05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883`），
但本文件使用的是由完整冻结spline系数**显式对称化**得到的实数对象：

$$
a,\beta_j\longmapsto\tfrac12(f(x)+f(-x)),\qquad
Z,\gamma_j\longmapsto\tfrac12(f(x)-f(-x)).
$$

$Z$先定义为冻结slope的精确积分$\int_0^x z'(s)ds$。没有把原浮点
反导函数系数与slope当成精确代数相等，也没有把原knots的约1.8e-15
反射缺陷当成零。它们相对于原输入的已付$C^2$差见
analytic-radial-smoothing笔记§1、§5。

**这里不应用Gaussian卷积。** 名称包含`analytic_smoothing_inputs`
的NPZ仅提供同一批完整原始系数、knots、slope和反导函数常数。
实际曲面由无限角R33公式$F=aP_\theta T+Ze_z$定义，target取

$$
g_0=E(x)dx^2+a(x)^2d\theta^2,\qquad
E=\frac1{2\pi}\int_0^{2\pi}F_x\cdot F_x\,d\theta.
$$

这里的$E$是无限角原函数的实际均值，不是未付尾的有限角截断输出。
它也不是旧canonical或新的D5/D8参数点；那些对象须用各自输入另算。

## 2. 根函数及区间结果

令

$$
C=a'E'-2a''E,\qquad
C'=a'E''-a''E'-2a'''E.
$$

则$K_0=C/(2aE^2)$。在

$$
I=[.2383698,.2383701]
$$

上，有向结果严格给出

$$
\begin{aligned}
C(.2383698)&<-3.4782679\cdot10^{-5},\\
C(.2383701)&>5.5378890\cdot10^{-5},\\
300.5184&<C'(I)<300.5587,\\
60.1022&<K_0'(I)<60.1105.
\end{aligned}
$$

同一区间$a>1.0972561$、$E>1.5094565$。故由连续性和严格正导数，
$I$中存在且仅存在一个简单根$t$。显式反射使$E,a,K_0$精确为偶函数，
所以负侧有相应的简单根$-t$。本局部证书不排除远处的其他根。

合并全部原knots与其精确反射（包括高度slope）后，根所在共同span为

$$
J=(.23750000000000002,\ .23969803864366687).
$$

$I$到两端的距离分别严格大于.000869799999999975和
.001327938643666870。每一个原scalar spline及反射项在此span内部
都是同一多项式，物理相位是其有限乘积；R33三角组成和角积分因此
在根附近真实解析。无需先把整个C4径向图作Gaussian平滑。

进一步对一个完全位于$J$中的实区间

$$
J_c=[.23788166874999997,\ .23885823125000002]
$$

直接计费，得到

$$
a>1.0969864,\quad E>1.5062020,\quad
231.2144<C'<369.6649,\quad
45.9092<K_0'<74.3898.
$$

任意$t\in I$的根中心实collar$|x-t|\le1/4096$都包含在$J_c$内。
于是其中

$$
K_0(x)=(x-t)\kappa(x),\qquad 45<\kappa(x)<75,
$$

$\kappa$在根处可解析延拓。这里$1/4096$是已付的**实collar半径**；
没有把它同时当成所有分母非零的复strip半径。后续量化复带或canonical
估计仍须对实际分母和所用变换继续计费。

## 3. 有限区间算术怎样覆盖无限角对象

### 3.1 径向与三角函数

所有输入binary64系数、knots及端点均解释成精确实数。基本浮点运算
按IEEE正确舍入后用`nextafter`向外扩。每个spline的导数控制系数
递推也向外计算。在共同span内，先以区间de Boor求中心点零至五阶
导数，再用**该分段多项式的完整Taylor式**覆盖整个径向小区间；
没有丢弃Taylor余项，因为单个quintic片的五阶Taylor式就是它本身。

三角函数用32阶实Taylor多项式，其系数由精确有理数给出，余项
不超过$|x|^{33}/33!$。网格角以四象限减少到$[0,\pi/2]$，其中$\pi$
来自Machin恒等式的精确有理交错和区间。该恒等式也可直接验证：
$\tan(4\arctan(1/5))=120/119$，再减去$\arctan(1/239)$后正切
正好为1，且角度位于$(0,\pi/2)$。交错和的下一项界支付其尾。
因此没有把普通库函数`sin/cos`或普通FFT当成证书端点。

### 3.2 直接角变换与Parseval

Q256四分之一圈上直接作向外的实sine/cosine变换。对每阶径向
$T,T_x,T_{xx},T_{xxx}$，设其cylindrical系数为
$A_m\sin m\theta,B_m\cos m\theta,C_m\sin m\theta$，$m\in4\mathbb Z$。
实际原函数系数精确为

$$
U_m=-\frac{mA_m+B_m}{m^2-1},\quad
V_m=\frac{A_m+mB_m}{m^2-1},\quad
W_m=-\frac{C_m}{m}\quad(m>0),
$$

且$U_0=B_0$。再按实际$a$及其径向导数作Leibniz组合，并加入精确
高度slope，得到同一有限原函数的$F_x,F_{xx},F_{xxx}$系数。

角均值由Parseval**完整求和**：零模权1，所有正模权$1/2$。
用此计算

$$
E=\langle|F_x|^2\rangle,\quad
E'=2\langle F_x\cdot F_{xx}\rangle,\quad
E''=2\langle|F_{xx}|^2+F_x\cdot F_{xxx}\rangle.
$$

这一步的每一个积和都向外计算，既没有漏最高metric频率，也没有
只检查原来的配置点。

### 3.3 无限角尾及混叠

Q256等效全圈N1024、Cartesian cut509。使用真实相位在
$|\operatorname{Im}\theta|\le.08$上的逐模界。
对指数函数的前三径向导数，Bell多项式为

$$
B_0=1,\quad B_1=q_1,\quad B_2=q_2+q_1^2,\quad
B_3=q_3+3q_1q_2+q_1^3.
$$

若$B_j,P_j$是两个相位第$j$阶的strip上界，Cartesian切向量的第$r$阶
径向导数范数可由

$$
2e^{\sigma+B_0+P_0}\,B_r(B_1+P_1,\ldots)
+e^{P_0}\,B_r(P_1,\ldots)
$$

控制（首个$B_0$符号表示相位界，$B_r(\cdot)$表示上述Bell多项式）。
随后用uniform-phase-primitive-tail中的完整尾/alias级数及实际半径
Leibniz公式。在整个$J_c$上得到

$$
(e_x,e_{xx},e_{xxx})
\le(2.373\cdot10^{-16},3.874\cdot10^{-14},1.150\cdot10^{-11}).
$$

若有限原函数各阶范数为$L_1,L_2,L_3$，均值所需补偿分别取

$$
\begin{aligned}
e_E&=2L_1e_x+e_x^2,\\
e_{E'}&=2(L_1e_{xx}+L_2e_x+e_xe_{xx}),\\
e_{E''}&=2(2L_2e_{xx}+e_{xx}^2+L_1e_{xxx}+L_3e_x+e_xe_{xxx}).
\end{aligned}
$$

这些已经加到上述根证书。整个$J_c$上的三项均值补偿分别不超过
8.713e-16、1.454e-13、4.429e-11。

另外把角变换加倍为Q512，只读复算左端点；八个区间量$a,E,E',E''$、
$C,C',K_0,K_0'$全部相交。这是不同cut的实现核查，不替代已付的尾界。

## 4. 保存和精确重做

完整原输入仍为
`data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz`，
SHA256 `bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532`。
完整finite证书是同目录 `type_fixed_step02_symmetric_root_interval.json`，
SHA256 `a40084d57e07db9c2b9162c76a094d7a7b087abddc740ed146f79f708342aa2f`。
它包括三个根区间求值、整个collar求值、无限尾费用、输入和依赖哈希，
以及Q512的独立cut核查。

源 `fourfold_phase_root_interval.py` SHA256：
`07cde6d560bd2681b69bc4a4487178276a21bda8fd3e0a56cdd43800ddd0f840`。
依赖沿用有理指数区间核和uniform-tail基本运算，完整哈希写在JSON中。

```bash
mkdir -p /tmp/visible-exact-root
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_root_interval.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --left .2383698 --right .2383701 --quarter-nodes 256 \
  --collar-radius .00048828125 \
  --out /tmp/visible-exact-root/report.json
```

不读背景ODE，不重新拟合，亦不改任何Newton检查点。此证书支付
实际显式反射对象的一个简单target根和真实局部解析span；全核心
$N<0$、$F_z/x>0$、真实返回与完整传递相位仍有各自的输入门。
