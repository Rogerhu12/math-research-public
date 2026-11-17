# R17：两重中心对称但无轴反射的核心及精确复矩

维护会话：`Astra-held10-f00f08c9-20261117`；初稿 `literature_mechanisms`，主会话独立四次卷积核验。这里只分析一个真实打破反射的核心参数、R7的适用性以及现有表示需要改哪些部分；没有重新求前缀，也没有证明新边值问题可解。

## 1. 一个不能靠整体旋转消除的相对相位

取平面支持函数

`h(phi)=1+q cos(2phi)+epsilon sin(4phi)`，`q*epsilon!=0`。

它满足 h(phi+pi)=h(phi)，故相应凸曲线及所围区域保持二重中心对称。曲率半径为

`rho=h+h''=1-3q cos(2phi)-15 epsilon sin(4phi)`，

所以 `3|q|+15|epsilon|<1` 是严格凸性的充分条件，周长仍严格为2pi。

若存在关于过原点、方向alpha的反射对称，必须有 `h(2alpha-phi)=h(phi)`。独立比较频率2，非零q迫使 `cos(4alpha)=1,sin(4alpha)=0`，即 alpha=k*pi/2。对这些alpha，频率4项变成 `-epsilon sin(4phi)`，与非零epsilon矛盾。中心对称凸体的中心唯一，任何反射若保持整个体都必须固定该中心，所以也没有漏掉偏移的反射轴。

因此此core没有任何轴反射。整体旋转若能把它变成某个反射对称core，逆旋转会给原core一个反射轴，与上证矛盾。等价地，复Fourier系数满足 `h_2=q/2,h_4=-i epsilon/2`，相对相位不变量 `h_4/h_2²=-2i epsilon/q²` 非实；不能同时把两模旋成纯cosine。

## 2. 它解除哪个必要障碍，又没有证明什么

在原对称轴上，反射曾强制 b=II_ru/(r sqrt(E))为零。新core没有该空间反射，求出的曲面也不应被表示强制留在 b=0子空间。在负Gauss曲率处，A=0、D>0只要求

`c=II_uu/r²=0`，`b²=-K_g`，

因而不必迫使另一主曲率a发散。原样本的 `K_g≈-1.45626e-5` 对应所需 `|b|≈.0038161`，从大小上并未用尽曲率10的预算。

这仅是Gauss代数上的可能出口。新core必须通过真正的Gauss–Codazzi/Frenet边值问题，才能知道b是否达到了正确值。任意非零epsilon只打破对称，并不自动给足 `b²=-K_g`。当K_g>0时，离轴也不能在D>0分支令c=0；经过D=0则属于另一种投影换图问题。

## 3. R7的两fold固定标记不依赖轴反射

R7使用的是：上半活动体的pi旋转对称、下半的z反射、完整体的中心对称，以及两张固定帽的具体复二阶矩。它不需要分别关于x、y平面的反射。保留二重中心对称后，centroid仍为零，`C_xz=C_yz=0`；复矩A允许为复数，仍有

`Q(alpha)=A exp(2i alpha)+B2`。

若固定标记取B2为正实数，则alpha=0与pi/2的二阶矩范数差仍为 `-2 B2 Re(A)`。因此需要保留的是Re(A)!=0，而不是A必须实。

对本节只有cos2和sin4的显式core，可直接精确积分。记 `h(phi)=sum h_k exp(i k phi)`，则

`AC=integral_C (x+i y)^2 dA`

`=(pi/2) sum_(k1+k2+k3+k4=-2) (1-k1)(1-k2)(1-k4²) h_k1 h_k2 h_k3 h_k4`。

代入 `h_0=1,h_2=h_-2=q/2,h_4=-i epsilon/2,h_-4=i epsilon/2`，有限展开给

`Re AC=pi q [1-9q²/4-45 epsilon²/2]`，

`Im AC=pi epsilon q [75 epsilon²+42q²-20]/8`.               (1)

该恒等式仅为四次有限Laurent卷积，不依赖截断余项。比如q=.2、epsilon=.005时，rho>=.325，core曲率<=1/.325，且 `Re AC=pi*.1818875>.5456625`。所以这类非反射core并不会自动破坏R7需要的矩非零性。

如果另加求解器确定的高模修正，应重新用一般复Fourier卷积或连续扰动界认证Re AC。不能无条件沿用旧cos-only系数的数值下界。

## 4. core支持函数与弧长入口的最小扩展

一般二重中心对称支持函数写为

`h=1+sum_m [a_m cos(m phi)+b_m sin(m phi)]`，`m=2,4,...,2M`。

保留 `h_0=1` 即固定周长2pi；不引入频率1即可固定中心平移。材料弧长仍由rho=h+h''给出，但必须使用完整反函数

`theta(phi)=phi+sum_m (1-m²)/m * [a_m sin(m phi)+b_m(1-cos(m phi))]`，

其常数选择使theta(0)=0。由rho>0可逆，且theta(phi+pi)=theta(phi)+pi。位置仍是 `gamma=h e_r+h' e_t`，所需导数仍为 `gamma_theta=e_t`、`gamma_thetatheta=-e_r/rho` 等。

原 `PlanarSupportCore` 的cos-only系数、逆弧长及参数导数都需作此扩展。物理g、中心精确二jet和原角warp的链式法则没有改变；原warp只要仍可逆并在cut处零二jet，可以继续作为计算坐标，没必要先把warp也重设计成非反射形式。

## 5. 现有完整物理模Fourier表示需加哪些通道

原CylindricalPrefix保留每个偶模的

`cos(m psi)e_r`，`sin(m psi)e_t`，`cos(m psi)e_z`，

再加常数径向e_r，共 `3M+1` 个状态，mean z单独积分。这正是轴反射子空间，不能表达本例。

完整二重中心对称表示应让R、T、H的每个偶模同时具有cos和sin，即添加

`sin(m psi)e_r`，`cos(m psi)e_t`，`sin(m psi)e_z`。

还需保留常数切向e_t，使零模水平角向分量可由Frenet方程自己确定；不能任意把它沿s清零，因为s依赖的空间旋转通常改变g_su。于是最直接的完整状态为 `6M+2`，mean z仍独立处理。

新增基的解析导数为

- `(sin(mpsi)e_r)'=m cos(mpsi)e_r+sin(mpsi)e_t`，二阶为 `-(m²+1)sin(mpsi)e_r+2m cos(mpsi)e_t`。
- `(cos(mpsi)e_t)'=-cos(mpsi)e_r-m sin(mpsi)e_t`，二阶为 `2m sin(mpsi)e_r-(m²+1)cos(mpsi)e_t`。
- `(sin(mpsi)e_z)'=m cos(mpsi)e_z`，二阶为 `-m²sin(mpsi)e_z`。
- `e_t'=-e_r`，`e_t''=-e_t`。

现有 `values/project` 与几何 `frame_jvp` 是一般Cartesian张量运算，原JVP代数本身可复用；需要改状态切片、基生成、核心入口Jacobian、checkpoint映射与BC装配。原prefix的每频线性DN因背景旋转对称，在cos/sin两通道上用同一个D_m；但完整真实非线性尾也必须同时支持两个通道，不能把sine端向量交给cos-only worker。

非线性momentum/DAE表示同样要把Q和非均值moment分别扩成cos/sin两组，L包含一个mean加两组；角导数用正确的cos/sin旋转矩阵。仅加sine通道仍不会让旧逐点正A/正Gram图覆盖A=0；若目标利用负K处的过零，还需要覆盖该分支的原方程求解表示。

## 6. epsilon不是免费存在参数

原设计的M个cosine height BC变为2M个cos/sin height BC。不能保持原来M个核心/度量参数不变、只在入口塞一个epsilon后称为相同BVP。

可先把所有二重支持系数作为设计未知量，固定整体相位（例如主sin2系数为零）和主cos2幅度q，随后选择足够的物理profile参数并严格核对边界条件数量与Jacobian秩。若再把sin4=epsilon也指定为固定非零值，又减少一项核心自由度，需要相应的设计自由度或已证明的边界恒等式。不能为凑维数随意删一条真实边界条件。

尤其，在当前反射对称解附近，线性化的反对称块如果除整体相位外可逆，那么固定相位后的隐函数定理会把附近解锁在反射子空间。此时任意小的sin4入口扰动不能保持全部尾BC。当前m4的线性core横截性约.447，远不是一个已验证的额外零模；不存在“只要epsilon非零就能延伸”的依据。

可研究的路径是调更多物理profile参数，寻找额外反对称核/分支，或用完整非对称边值问题作独立设计。即使双模线性共振出现，非线性相对相位的相容条件仍须求解，不能预设sin4相位能够自由选择。

## 7. 连续几何证书也要改变

二重中心对称仍允许只审半个角周期，再以pi旋转补全；旧R11依赖x偶/y奇的单象限缩减不能原封不动使用。中心lift、有限Cartesian Fourier/Hermite构造和PSD曲率判据仍适用，但输入系数与角域必须对应新表示。

原witness `p=(h(0),0,0)` 也需修正：本例 `gamma(0)=(1+q,4epsilon,0)`，旧x轴点一般不在core上。可以选择真实core点后作一次固定平面旋转让它落在x轴，或直接对任意 `p=(px,py,0)` 用pi旋转轨道的距离式

`dist² = |p|²+x²+y²+z²-2|-px*y+py*x|`

来审计相位pi/2的候选点。这个式子只用二重中心对称，不要求分别有x/y反射。全部prefix和尾上的连续witness距离、尺寸及曲率都要重新支付，不能仅用core支持函数的相位差替代。

## 8. 独立有理符号复算

运行 `python topics/visible-flex-held-10pct/scripts/nonreflection_core_moment_exact.py`（Python 3、SymPy）。脚本从四项有限卷积独立重建 Re/Im A_C，逐式减去闭式并断言为零，同时核 q=1/5、epsilon=1/200 的有理界。它不调用前缀或尾部求解器，也不提供新边值问题的解。
