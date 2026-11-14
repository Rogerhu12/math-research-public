# R123：实际 Weierstrass 微分尺度及形式群对数的有限精度提取

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的实际尺度与转换公式。** R102/R110/R117 使用短 Weierstrass 模型的斜率构造权一、权二截面。本篇把同一规范准确转换成模曲线上的微分，并证明模 $47^4$ 对数提取所需的消去公式。它不声称已经算完 $[\#J(\mathbb F_{47})]B_{-4}$ 或完整非主 Poincaré 高度。

在正在使用的真实评价族
$$E_t:y^2=x^3+x+32+t$$
上，权二截面到局部参数 $t$ 下微分的因子准确为
$$\boxed{\beta(t)=-\frac3{4+27(32+t)^2}.}\tag{123.1}$$
特别
$$\boxed{\beta(0)=-\frac3{27652}
\equiv2880480\pmod{47^4},\qquad\beta(0)\equiv38\pmod{47}.}\tag{123.2}$$
因此它不改变所需的单位秩，却必须保留在真实 Abel–Jacobi 对数坐标中。

## 1. Gauss–Manin 系数的完整代数计算

考虑特征零底域上的光滑族
$$y^2=f(x)=x^3+Ax+B,\qquad D=4A^3+27B^2\ne0,$$
并固定相对微分
$$\omega=\frac{dx}{2y},\qquad \eta=x\frac{dx}{2y}.$$
这里 $dA,dB$ 是基底上的微分，$d_x$ 是相对变量 $x$ 的微分。定义
$$\alpha=-\frac{dD}{12D},\qquad
\beta=\frac{9B\,dA-6A\,dB}{2D},\qquad
R(x)=\alpha x-\beta x^2-\frac{2A}{3}\beta.$$
在有理相对微分中，有准确恒等式
$$-\frac{(x\,dA+dB)\,dx}{4y^3}
=\alpha\omega+\beta\eta+d_x\left(\frac{R(x)}y\right).\tag{123.3}$$

为直接核验，乘以 $4y^3/dx$，并用
$$d_x(R/y)=\left(R'f-\tfrac12Rf'\right)dx/y^3.$$
四次、三次、二次项分别因 $R$ 的三个系数相消；一次和常数项分别化为
$$4A\alpha-6B\beta=-dA,\qquad
6B\alpha+\frac43A^2\beta=-dB,$$
由所给 $\alpha,\beta$ 立即成立。这不是只在某个数值点检查的近似。

左边是固定 $x$ 时 $\omega$ 的基底导数。去掉相对全微分，得到
$$\boxed{\nabla\omega=-\frac{dD}{12D}\omega
+\frac{9B\,dA-6A\,dB}{2D}\eta.}\tag{123.4}$$
在无穷远处取 $z=-x/y$，有 $\omega=(1+O(z^4))dz$、
$\eta=(z^{-2}+O(z^2))dz$，所以标准留数配对中
$(\int\omega)\eta$ 的留数为一。相应的 Kodaira–Spencer 映射将
$\omega^{\otimes2}$ 送到 $\beta$；下一节用本题已经固定的 Tate 规范准确校准其符号和整体尺度。

## 2. 与同一个 Tate 规范精确相合

在 R110 所用的 Tate 参数 $q$ 上，短模型可写成
$$A=-E_4/48,\qquad B=E_6/864,\qquad
D=-\Delta/16,\qquad
\Delta=(E_4^3-E_6^2)/1728.$$
这里 $E_4,E_6$ 的常数项为一，所用不变微分是 $du/u$。特别在节点纤维，
$$x=\frac{u}{(1-u)^2}+\frac1{12},\qquad
y=\frac{u(1+u)}{2(1-u)^3},\qquad \frac{dx}{2y}=\frac{du}{u}.$$
这与 R102 的实际斜率规范、R110 的尖点值和同一个 Weil 根一致。

代入 (123.4) 的第二个系数，得
$$\beta=\frac{3E_6\,dE_4-2E_4\,dE_6}{E_4^3-E_6^2}.$$
Ramanujan 的准确微分恒等式
$$q\frac{dE_4}{dq}=\frac{E_2E_4-E_6}{3},\qquad
q\frac{dE_6}{dq}=\frac{E_2E_6-E_4^2}{2}$$
使分子恰为 $(E_4^3-E_6^2)dq/q$。因此
$$\boxed{\operatorname{KS}(\omega^{\otimes2})=\frac{dq}{q}.}\tag{123.5}$$
这是完整级数恒等式，不只比较尖点首项。故一个在实际短模型和所选 $\omega$ 下数值为 $g$ 的权二截面，其对应模曲线微分准确为
$$g\frac{9B\,dA-6A\,dB}{2D}.\tag{123.6}$$
当该截面属于 R110 由尖点留数核求出的 $54$ 维典范空间时，(123.6) 是相应真正的全纯微分。

## 3. 层41的47进评价族及导数转换

对实际族 $A=1$、$B=32+t$，式 (123.6) 给 (123.1)。此处
$$D(0)=27652\equiv16\pmod{47},$$
所以 $\beta(t)\in\mathbb Z_{47}[[t]]^\times$。而
$$j(t)=\frac{6912}{4+27(32+t)^2},\qquad
j'(0)=-\frac{746496}{47789569}\equiv15\pmod{47}.$$
因此 $t$ 是真实粗模圆盘的参数；评价点 $j\equiv9$ 不需要椭圆稳定子修正。

若某一原始权二截面的圆盘展开为
$$g(t)=g_0+g_1t+O(t^2),$$
则真实微分和其局部原函数分别为
$$g(t)\beta(t)dt
=\bigl(\beta_0g_0+(\beta_0g_1+\beta_1g_0)t+O(t^2)\bigr)dt,$$
$$\int_0^t g(s)\beta(s)ds
=\beta_0g_0t+\frac{\beta_0g_1+\beta_1g_0}{2}t^2+O(t^3),\tag{123.7}$$
其中
$$\beta_0=-3/27652,\qquad
\beta_1=\frac{5184}{27652^2}=\frac{324}{47789569}
\equiv679746\pmod{47^4}.$$
所以一阶切向只需乘 $\beta_0$，进一步的积分展开则还要保留 $\beta_1g_0$。
原始权二导数不能直接当作微分系数的导数。

## 4. 在实际整坐标中提取模47⁴形式对数

令 $\mathcal J/\mathbb Z_{47}$ 为好约化的 Jacobian，
$J_1=\ker(\mathcal J(\mathbb Z_{47})\to\mathcal J(\mathbb F_{47}))$。
设 $f$ 是零点附近一个实际整局部浸入，其所有坐标属于完整局部环；必须先置
$$F(P)=f(P)-f(0).$$
则对每个 $Y\in J_1$，有
$$\boxed{
dF_0(\log Y)\equiv
\frac{2F(Y)-6F(-Y)+F(-2Y)}6\pmod{47^4}.}\tag{123.8}$$

**证明。** 取实际不变微分的对偶 Lie 坐标，写 $z=\log Y\in47\operatorname{Lie}(\mathcal J)$。
不变导子在整形式群的完整局部环上定义。对任一整坐标函数，其沿 $z$ 的指数展开为
$$F(\exp z)=\sum_{n\ge1}\frac{D_z^nF(0)}{n!}.$$
因为 $z\in47\operatorname{Lie}$，分子第 $n$ 项属于 $47^n$。
对 $n\ge4$，$n-v_{47}(n!)\ge4$，所以所有高阶项均在 $47^4$ 中，且该级数收敛。
前三级可写为
$$F(\exp z)=L(z)+Q(z)+C(z)\pmod{47^4},$$
分别为次数一、二、三的齐次式，$L=dF_0$。
把 $z,-z,-2z$ 代入，上式右边的加权和在线性、二次、三次项上的系数分别为
$$2+6-2=6,\qquad2-6+4=0,\qquad2+6-8=0.$$
六是47进单位，遂得 (123.8)。若不先减 $f(0)$，常数的权和为 $2-6+1=-3$，公式将不成立。证毕。

论证也适用于本次未分歧二次系数环。没有假设任意 Grassmann 参数就是形式群对数；需要先构造代表无关的实际整局部坐标，R117 后续的固定72次除子与 Abel 逆正提供这一接口。

## 5. 通过真实 Abel 切向接到54个微分坐标

设 $\omega_1,\ldots,\omega_{54}$ 是 R110 的实际典范微分基。
在54个实际评价点 $P_j$ 上取与 (123.1) 相同的圆盘参数 $t$，形成真正的 Jacobian 切向
$$T_j(t)=[P_j(t)-P_j].$$
从局部浸入 $F$ 中选择54个坐标，记其实际导数矩阵为
$$C_{ij}=\left.\frac{d}{dt}F_i(T_j(t))\right|_{t=0}.$$
设原始权二典范截面评价矩阵为 $W_{kj}$；准确的微分矩阵则为
$$\Omega_{kj}=\frac{\omega_k(P_j)}{dt}=\beta_0W_{kj}.\tag{123.9}$$
当 $C$ 有单位行列式时，令 $v(Y)$ 为 (123.8) 右边所选54个坐标，即有
$$\boxed{
\left(\int_0^Y\omega_k\right)_{k=1}^{54}
\equiv\Omega C^{-1}v(Y)\pmod{47^4}.}\tag{123.10}$$
这是 $dF_0$ 和实际微分在同一组切向 $T'_j(0)$ 上的基变换。若底层 Picard 坐标采用了负的 Abel 逆，它的符号已经包含于真实 $C$，无需再凭约定额外加负号。

对实际 $B=B_{-4}$，若 $Y=\epsilon hB\in J_1$、$\epsilon\in\{\pm1\}$ 且
$47\nmid h$，则 (123.10) 再乘 $\epsilon h^{-1}$ 就给 $B$ 的真实对数，不损失47进精度。
这仍以完成该实际乘法、三个形式群点的坐标及单位校准矩阵为前提；本篇没有把正在计算的矩阵当成已输出的数据。

若所选基在未分歧二次扩张上，$C,\Omega,v(Y)$ 必须沿同一半线性 Frobenius 规则下降。
基变换公式与该规则相容；不能只因 $B$ 有理，就在一个非有理微分基中要求每个坐标单独固定。

## 6. 规范来源和适用边界

1. S. Ramanujan, *On certain arithmetical functions*, Transactions of the Cambridge Philosophical Society **22** (1916), no.9, 159–184，§6、TableII后列出的三条微分恒等式。[原文转录及扫描入口](https://ramanujan.sirinudi.org/Volumes/published/ram18.html)。原文 $P,Q,R$ 分别为这里的 $E_2,E_4,E_6$；本篇只使用后两条准确恒等式。
2. [R102](R102-actual-level41-makdisi-model-at47.md)、[R110](R110-actual-cusps-and-canonical-divisor-ideals-at47.md)：实际斜率、短 Weierstrass 模型、Tate 参数、$du/u$ 和完整典范核的共同规范。Gauss–Manin 约化及所有有理尺度在 §1–§3 自证。
3. [R117](R117-actual-cm-group-operations-and-principal-poincare-norm-at47.md) 和[实际形式群工作记录](../notes/2026-11-12-qc-formal47-log-work.md)：真实群律、主除子范数、整局部坐标和当前可恢复计算。§4–§5证明对数精度与坐标转换，不替代尚未完成的非主高度。

本结果固定了实际积分的尺度和精度接口；一般层共同根、完整Poincaré高度及Serre一致性主目标仍未完成。
