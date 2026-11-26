# R603 九参数强准备输入与原 R598 质量问题：实现说明

日期：2026-11-26。科学执行仅在本公开仓库 Actions。
本地或无环境期间只编辑、读源、做绑定/hash；没有导入或运行科学源。

入口为 `scripts/r603_vtwo_center_mass_continuation_agent.py`。
本包直接从已付 R598 run **45828239888 / job 139937889703** 的十一参数生成新九参数。
尚未运行的“只固定 \(h_{ss}(0)=H\)”十参数草稿不单独执行，
也不是本入口的运行依赖。完整质量实现仍直接来自已发布原 R598 源。

## 1. 已付入口与需要修复的真实机械错误

前源提交 `92d261c4e239c4aa5e6cd59033d12c3f4e0087b2`，
源 SHA256 为 `513290476ce4795e75b7d3802b2d94f906c55465cbaca59970eaf93b919146c0`。
完整 stdout SHA256 为
`85ff477ffd81e30b8b8d02968d8343f578740692c4e93bb0f8f18392126101d9`；
收据是 `notes/2026-11-26-r598-wide-prepared-first-public-receipt-agent.md`。

前次实际完成新 192 阶表、400 nfev / 8916 residual calls 的十一参数 guide、
其原 frame/双 collar 预算、513 点真 A 与两侧 coefficient/positive-energy 预收。
之后原 `encode(geometry)` 用 5×513 整阵除长度5的 limits，发生真实广播错误。
六个 rho 积分、固定规范 LS、mass RHS/Jacobian/trial/accepted-state 当时都没有进入。
这不是质量式或母本身的不可达性结论。

本源的 `ColumnCoordinates` 只作批量适配：
对 5×N 数据的每列分别调用原 `FiniteCoordinates.encode`。
单向量也仍走原函数。原严格盒、atan 图、全部参数与单位不变。
`ColumnMassRHS.set_gauge_unit` 在旧方法后以同一个固定单位重装适配器，
不会被旧 setter 换回只接收单列的类。

## 2. 新输入为何同时选择 \(a=H,\ v=2\)

R601 在真 \(A_s=M\) 的 prepared 中心给
\[
V=H_A+2F_0=\frac{v}{12H}u,\qquad
V_s=\frac{a-H}{4H^3}(1+H^2y^2)(u'-yu'').
\]
因此 \(a=H,b=0\) 同时延后两个高导系数的一阶生成。
同一中心两原 ruling 仍用一个固定规范支付
\[
\zeta_0=2H(R_c^0+C_{h,c}H).
\]
原完整正平方仍存在，不因这个选择变成零。

R603 进一步证明一个**有明确假设的缩微族必要条件**：
同一母形状、共同正时间区间、\(h/k\) 在 C² 收敛、
真零 rho incoming、\(\varepsilon^2\widehat\nu\) 有有限常极限，
且 prepared、\(a=H\)、非零极限中心速度时，必须 \(|v|\to2\)。
证明先用完整方程的 C⁰ 极限得到正六节点范数 \(\mathcal F=w\cdot P\)，
再在极限轨道计算 jet；没有交换巨大能量的二阶导数极限。
它不排除任何固定有限 \(\varepsilon\) 的其它根。

据此本次选择 \(v_*=2\) 的更强有限初猜。
源码也可明示选择 \(-2\)，当前请求只运行 \(+2\) 这一份输入。
该选择是对真实固定规范最高层的相容准备，不是把缩微必要条件提升为有限根存在。
没有改变正平方的系数，也没有添加 energy homotopy 或逐点控制。

正式依据：

- `results/R601-prepared-center-true-jet-and-fixed-gauge-acceleration.md`；
- `results/R603-prepared-leading-energy-and-speed-two-guide.md`。

## 3. 新九参数、两个准确消元与唯一常数 c

新自由向量按顺序为
\[
(H,\alpha_1,\alpha_2,\alpha_3,b_1,b_2,b_3,b_4,L).
\]
从已付十一参数只读取
\(H=1.9+\tanh(\sum_{j=0}^4\alpha_j)\)、
原 \(\alpha_{1,2,3}\)、原 \(b_{1,\ldots,4}\) 和原 L。
这次的 \(\alpha_0,\alpha_4,b_5,c\) 全部重新定义。
数值转换只在公开 Actions；没有把未付的转换结果伪装成既有输出。

高度保留原五余弦/tanh 形式，用 R601 消元
\[
B_*=-\frac{HL^2}{\pi^2[1-(H-1.9)^2]},\quad
\alpha_4=\frac{B_*-\alpha_1-4\alpha_2-9\alpha_3}{16},
\]
\[
\alpha_0=\operatorname{atanh}(H-1.9)-\sum_{j=1}^4\alpha_j .
\]
故连续定义中 \(h(0)=h_{ss}(0)=H\)，全域 \(.9<h<2.9\)。

对曲率原六个奇半波，令 \(\theta=\pi x/2,\ s=Lx\)，
\[
T_*=\frac{2Lv_*}{1.95\pi},\quad
b_5(c)=\frac{T_*-c-3b_1-5b_2-7b_3-9b_4}{11},
\]
\[
k(x)=1.95\tanh\!\left(c\sin\theta+
          \sum_{j=1}^{5}b_j(c)\sin((2j+1)\theta)\right).
\]
连续定义中准确有 \(k_s(0)=v_*,k_{ss}(0)=0\)；
原末 \(h_s(1)=k_s(1)=0\) 仍保持。
对每个候选，\(c,b_5(c)\) 是整条路径上的常系数，
不随 x 重新选择。

唯一 \(c\) 仍由 \(\int_0^1hk\,dx=0\) 定义。
不同于旧独立 \(b_5\) 族，这里的单调方向是
\[
\partial_cK_c=\sin\theta-\sin(11\theta)/11>0
\quad(0<x\le1).
\]
R603 已严格证明其正性、积分单调性和两个相反的极限。
实现使用固定正 Gauss96 和 brentq；
初始 bracket 半径为 \(2+2\sum_{j=1}^4|b_j|+|T_*|\)，必要时倍增，
声明的上界1024仍只是本次有限搜索 scope。
连续唯一性不被误写成所有数值 bracket 必已覆盖。

新参数盒为 \(H\in[.95,2.85]\)，
三个自由高度系数和四个曲率系数各在 \([-2.5,2.5]\)，
\(L\in[2.05,7.5]\)。
依赖系数 \(\alpha_0,\alpha_4,b_5(c)\) 不暗中截断。
映射后的已付输入若不在本盒则明确报错，不悄悄裁剪。

## 4. 真七末矩与完整新历史仍必须支付

257 节点上拟合七个剩余真实矩 \(p_0,p_1,t_1,r_1,s_1,s_0,r_0\)，
prepared 奇中心从同一真实 \(H,v_*\) 得到。
原 \(\int hk=0\) 连续定义给末 \(p_2=0\)，
但数值 Gauss/brent 与后续 Simpson 有误差，
所以八个实际数值末矩仍全部输出。
采样 eta 与速度 penalty 不升级为连续盒证书。

新九参数问题最多400 nfev，三点差分每次都重新求同一个单调 c。
这既不重跑旧十一参数问题，也不执行未跑的较弱十参数族。
输出真实 residual calls、单调 root solves/integrand calls、选中参数、
实际十一系数、c、八末矩、全部几何范围，
并读出中心 \(h_{ss}-h,\ k_s-v_*,\ k_{ss}\) 的实际数值误差。

选中后以513点重算真 A、完整正负 rho、中心势和一个固定 \(\chi\)。
所有旧中间数组、旧 \(\rho,\nu\) 都不转移。
原 `make_seed` 用实际 \(a[0],b[0]\) 设 \(\zeta_0\)，
另两个规范数仍是全程一次 LS 拟合的常数。
进入质量 BVP 后原十个真实中心参数全部释放；
九参数只是初猜，不把最终真实解强行限制在一个 guide 族内。

## 5. 全部原质量方程、尺度、AD 和回付保持

同一 R598 母保持十八完整块、576微包、
\(\varepsilon=1/12000\)、窗口 \([4,6]\)、每侧 collar \(1/3000\)、
原 \((2w)^{1/4}\) 实幅。
六参考块按 \(6=3\times2\) 的齐次四次正权读出，不多提一次权。
没有保存原数值 coefficient table，本次仅为新实际求解重新生成192阶表和正 Gram；
所有重建成本计入，不重跑已付 identity / directional derivative / quadrature 门。

每stage仍是原19态加两代数加速度：
\[
f_++C_{h,+}a+C_{k,+}b=0,\qquad
f_-+C_{h,-}a-C_{k,-}b=0 .
\]
31变量local AD、原两侧负号、全部29 BC、稀疏Lobatto与阻尼LSMR完全继承。
特别负侧为反射几何、\(JA\)、物理 \((a,-b)\) 和整个 rho 导数的反号。
原 \( \nu,\bar\nu,\widehat\nu\)、sigma defect、
真实中心参数依赖与重锚读出全部保持。

19 differential row unit均为1，仅两ruling merit行用一次固定的能量单位。
原物理 residual 和原收敛阈值单独报告；
状态 rho 与 \(\zeta_0\) 未改坐标，
固定guard单位只从该新真实seed确定其有限搜索域。
不把大原缺陷除后称为精确根。

最多50个迭代槽、每次12trial、LSMR1600；接受必须有真实严格merit下降。
只有原flow/ruling max不超过 \(10^{-7}\)、原BC max不超过 \(10^{-10}\)，
才作一次129-stage同输入refinement。
任何离散通过仍不是连续原根、rank或题完成证明。

## 6. 完整状态先保存，真实几何随同一条路径读取

在 seed 全部完成后、第一次mass evaluate前，
打印完整65×21 stage、十参数、固定单位和canonical SHA到公开stdout，
明确标成完整输入，不冒充accepted root。
每个真正接受的mass状态仍由原实现先完整打印再inspection。
没有artifact/cache/release，不把原轨迹或数值表写入仓库。

新guide读取原frame/alpha、双collar位置、sampled直径、
主曲率/focal-cap与两pose，并用实际十八物理副本读第一变分。
求解结束后对实际末态稳定Hermite插值另读一次几何，
不能用旧guide的几何代替更新后的状态。

对尚未满足运动学的插值，形算子使用真
\[
(h_s,k_s)=(\text{原chart导数})
           (\text{Hermite前两行导数})/L,
\]
并报告与独立速度状态的差。
原frame/alpha、正负两侧位置、R573 shape entries均不改变。
样本focal-cap/diameter只描述这条实际曲面，
不提供连续reach下界，亦不支付pose/period/holding。

上次实际guide的 .0274676 必要比率问题没有被消除；
新路径必须重读其自己的完整预算，不能以质量merit下降略过。

## 7. 执行责任

请求绑定入口、全部真实import源、R601/R603及其前置原证明、
说明、前次收据、workflow的精确SHA。
原runner在科学前actual pull双仓、核README/QUEUE并删除凭据。
单job，stdout only，自然终态后一次完整日志闭账，不读live stdout。

科学费用包括必要的原定义/表/正Gram重建、新九参数guide、
全history预积分、全部mass RHS/Jacobian/trial、真实物理回付和两个frame范围读出。
实际科学未运行前只声明源已准备和静态/纸审状态，
不声称初猜、矩、加速度、原根或宏观门已经达到。
