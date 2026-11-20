# R658：同一真实闭合候选的全体直径上界与固定握持组件

2026-11-20，Astra-larger-resume-24b2ab87-20261120。

**状态：完整连续位置覆盖已证明并实际完成；另有同父单胞曲率界。**
在 [R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)
的准确数学对象与向外算术模型下，对下述同一真实候选的全部922个径向胞、全部角度、上下镜像和两个平帽，

$$D_0=\operatorname{diam}F_0(S^2)\le {4106819\over10^6}=4.106819.\tag{1}$$

这是连续完整像的上界，不是从已读点估计出的下界。直径定义对连续闭映射的像也适用；(1)没有偷用尚未证明的嵌入或等距。对这个候选的关键完整胞821另已证明

$$\sup_{s\in[s_{821},s_{822}],\,\phi}\max(|\kappa_1|,|\kappa_2|)\le8.069613.\tag{2}$$

(2)只覆盖该胞，不能替代全体曲率或R650的全体正支持输入。本条还给一块固定平帽握持区的准确直径比例，以及后加既有固定标记时的条件预算；**没有完成闭等距、全局reach、整像held或含反射非全等**。

## 1. 固定实际父，所有连续对象保持同一身份

输入是 [v4a从def1六方向](../notes/2026-11-20-curvature-qp-arbitrary-def1-result.md)
的完整实际终态 `curvature-qp-arbitrary-def1-six-step.npz`：

`607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941`。

采用准确binary64自由三jet及core，并按原准确仿射式重建派生端口；
$J=923,M=160$，所有原模保留。实际节点仍是原
$s_i=\alpha_iS+\beta_i$，准确S/R是原同一Hold轮廓，消费R656式(1)的有理盒。
本次准确帽高度为

$$H={8594875381108039\over4503599627370496}>1,$$

lift宽度仍为 $w=3602879701896397/72057594037927936$。
上半场为

$$F=q+\chi(s)(R+S-s)e_r(\Theta(\phi))+\chi(s)H e_z.\tag{3}$$

这里$q$是准确节点上的共享quintic Hermite场，$\Theta$与其完整解析三角lift正是R656定义。
没有把数值carrier节点当成新准确节点，没有截断$\cos\delta,\sin\delta$，没有以参考度量代替真实位置。

对同一core，本次Q2048连续角覆盖给

$$\rho=\Theta_\phi\ge0.16577340676712354>0.\tag{4}$$

故帽边的角重参数化是保持方向的圆微分同胚。原仿射端口使上下镜像在core具有共同两jet、外边与两个平盘具有共同两jet；因此(3)按原配方给闭合C²映射。内部每点正则性、单射性和等距仍是独立任务。

## 2. 全体位置向外界的完整证明

### 2.1 每个闭胞的准确位置控制点

复用R656的quintic Hermite控制点、准确胞宽、符号lift断点切片、De Casteljau限制和升阶。对每个真实piece，把$q$和(3)的lift先统一到degree6，在**同一组Bernstein控制点**上组合。

在每个闭角段$I_j$，R656的严格radix-two包围、三角多项式二导过采样界和完整解析lift的Taylor余项给每个位置控制点分量

$$B_{k,d}(\phi)\in[\ell_{k,d,j},u_{k,d,j}],\quad\phi\in I_j,\quad d=1,2,3.$$

其旋转架始终正交，所以计算三个分量平方和准确等于Cartesian位置长度平方。
对任何径向参数$u\in[0,1]$，Bernstein非负性与和为1给

$$F_d(u,\phi)\in\left[\min_k\ell_{k,d,j},\max_ku_{k,d,j}\right].\tag{5}$$

每个平方区间用向外乘法/过零下界处理，逐分量向外相加，故

$$|F(u,\phi)|^2\le\sum_{d=1}^3\max\{(\min_k\ell_{k,d,j})^2,(\max_ku_{k,d,j})^2\}.\tag{6}$$

源码所用区间平方给(6)的有效向上包围；无需局部正则或曲率。共享端点的闭胞并集包含所有节点，两侧半步角段覆盖整个圆。对位置范数，半周/反射对称使四分之一域覆盖充分，证明见R656第6节。

本次逐一循环 `cell=0,...,921`，源码最终明确检查列表恰等于全部原胞，未将部分返回冒作完整。每piece径向细分数1，角Q2048，四分之一域513个闭角段。没有需要未付盒的除法；唯一胞宽除法在准确宽度下界正时才执行。

### 2.2 镜像、平帽与完整像

水平反射不改$|F|$。两平盘在$z=\pm H$、平面半径不大于R，准确满足

$$|F_{\rm cap}|^2\le R^2+H^2.$$

R656同一有理盒向外计算给两盘共同上界
$3.9610897106765237$，小于侧面全体上界。因而全部像的半径平方都有共同连续上界。

任意像上两点$x,y$满足

$$|x-y|\le|x|+|y|\le2\sup|F|.\tag{7}$$

这即给完整直径上界，并不要求像已嵌入。当前未标记镜像场还中心对称，故实际$D_0=2\max|F|$；证明(1)只需(7)，不依赖这个更强等式。

### 2.3 本次全体实际读出及有理外包

全922胞自然执行结束，实际132.946762574秒、exit0。最高位置平方上界为

$$B=4.2164888565210985,$$

在胞880、闭角段索引177；次高胞881/879/882的界分别为
$4.2155335025865845$、$4.213310798746486$、$4.210026740453238$。
这里小数B按报告中binary64的准确值解释。
向外平方根给 $2\sqrt B\le4.106818163260264$。
进一步按Fraction准确核算

$$\left({4106819\over2\cdot10^6}\right)^2\ge B,$$

所以得到读者可直接使用的有理界(1)。该核算只是把已得向外输出改写成有理数字，不增加未经证明的数值模型。

## 3. 同一父的关键胞曲率预算

对同一6077、相同准确节点/core/H，在胞821单独使用R656完整六jet核，Q16384、每piece32个径向子胞、$\beta=1/4$。所有闭盒均证明真实第一基本形式正定，未付盒数0。实际报告为：

| 连续量 | 对整个胞821及全部角的有效界 |
|---|---:|
| 主曲率绝对值上界 | 8.069612833529575 |
| $A_{1/4}F\cdot n$ 下界 | .4574082206109734 |
| $|F|^2$ 上界 | 2.963330077087749 |
| $|F_\phi\times F_s|^2$ 下界 | .03816367894631581 |
| $|F_s|^2$ 下界 | .993411790562202 |
| 既有两符号握持见证距离平方下界 | .9771716453742239 |

该次自然返回用时12.300707886秒。取准确有理外包(2)，与(1)结合得到

$$ {3\over100}\,{4106819\over10^6}\,{8069613\over10^6}
 =0.99421319973141<1.\tag{8}$$

所以这一整个关键胞的曲率没有消耗全部README要求的$0.03D_0$曲率预算。
(8)并未对其余921胞断言任何曲率上界，未付全局支持，也不从局部曲率推出reach。它支持将后继有限点**算法**筛选余量由.98明确改成.992的选择；这个选择不修改README标准，也不将有限点通过变成连续证明。

## 4. 固定握持区与标记组件的准确比例

按 [R248](R248-finite-C2-phase-family-and-global-reductions.md)
未标记相位公式，整个未标记像是$F_0(S^2)$的绕轴旋转，所以直径(1)对所有相位成立。
在平帽的Cartesian圆盘参数中，旋转前后的参数平移相互抵消，帽映射逐点固定。
选上帽中心的闭子盘

$$H_{\rm grip}=\{(x,y,H):x^2+y^2\le(9/20)^2\}.$$

因为准确$R>0.56473417>9/20$，此盘严格包含于帽内部，在参数面中具有非空二维内点，且

$$\operatorname{diam}H_{\rm grip}=9/10.$$

因此对当前未标记相位映射，有准确比例

$$\frac{\operatorname{diam}H_{\rm grip}}{D_0}
\ge\frac{900000}{4106819}>0.219>0.2.\tag{9}$$

这是一块真实固定区域的组件结论。未标记全部像互为刚体旋转，故它本身**不能**解决含反射Euclidean商距离为正的要求。

如以后按R650附录C，在各帽内部接入同一固定$p_3$标记，取支撑半径
$R_*=27/200<9/20$、高度不超过$h=1/1000$，则每点移动不超过h，故一般三角不等式给

$$D_{\rm marked}\le D_0+2h\le4.108819.\tag{10}$$

固定标记图在整个握持参数盘上不随相位变化，且握持圆周不动，其像直径至少$9/10$，所以

$$\frac{\operatorname{diam}H_{\rm marked}}{D_{\rm marked}}
\ge\frac{900000}{4108819}>0.219>0.2.\tag{11}$$

实际6077的H>1允许使用R650附录C给出的标记局部支持/曲率组件预算。
未改动的胞821对应(8)变成

$$.03\,(4.108819)(8.069613)=.99469737651141<1.$$

但本条**没有生成或宣称已完成这种标记闭族**。标记改变帽的共同度量，必须按既有固定帽配方选择全族共同g，不能说它保持旧平帽度量不变。R625/R629非全等还需其完整假设；全域reach、整像held和严格等距仍分别有未付责任。

## 5. 完整来源、可复现参数与保存范围

| 对象 | SHA256 |
|---|---|
| 准确6077自由三jet/core/H bundle | `607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941` |
| 原节点/同Hold报告 | `fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692` |
| 本次位置专用完整源 | `9085e6713faa1aba1dcc99a0e30ed038f33ca6ec24a2c187e9668a9c4fe26623` |
| R656完整六jet源 | `2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377` |
| 原严格FFT/区间核 | `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d` |
| 全922胞位置报告 | `bcca11139b357459c955fb7507820da8fe63a6bf3aa63a5cddd65967d23efe06` |
| 单胞821六jet报告 | `b57972d3258a4f8b0bc55c3e60738ee753db9a03b0af1e85554baec6f0bbe9b5` |

位置源保存在 `scripts/resume_20261120/fullclosed_radius_interval.py`，只复用R656的真实位置子集；没有复制或修改旧区间核。Python3.12.14、NumPy2.3.5、单BLAS，IEEE非FTZ算术假设沿R656。两次都是本地执行，不补造公开run编号。完整逐胞JSON与NPZ只在scratch，按根规矩15保源码/参数/身份/紧凑结论；重跑计时和路径字段可改变报告SHA。

原warm/节点报告的恢复入口是 `scripts/resume_20261120/reproduce_and_solve.py`；6077父链的所有实际参数与完整CLI见本条第1节所链接v4a记录，以及其直接引用的def1、2038及warm重建记录。令repo为checkout、topic="$repo/topics/visible-flex-larger-amplitude"、work为仓库外重建目录：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/fullclosed_radius_interval.py" \
 --bundle "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --geometry-source "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --out "$work/root/continuous-6077-complete-radius-q2048-r1.json" \
 --angles 2048 --radial-subdivisions 1

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --bundle "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --out "$work/root/continuous-6077-cell821-q16384-r32.json" \
 --cells 821 --angles 16384 --radial-subdivisions 32 --beta 1/4
~~~

本条只登记新全体D界、固定握持大小组件以及同父新单胞连续预算。未重算R648/R651/R652旧prefix结论，未将这些旧场证书移用当前候选。
