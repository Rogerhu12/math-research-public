# R1017：原临界 \(H_p\) 的 tame 二、三相位与全范数负一单位定理

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：对全部 \(p\ge41,\ p\equiv5\pmod6\)，原未经筛选的临界
\(H_p(\eta)\) 在每个 \(\eta^{p+1}=-1\) 上都非零。**
这是 R1013 的严格加强：实际二-primary theta 作用把原四维源缩到两项，
实际三-primary 的 canonical lifts 再固定这两项的相对相位为六次单位根。
共同 scalar 保留；未证明原 primitive/Legendre 筛选后同 \(h\) 非零。

## 1. 固定原源与准确目标

完全保持 R1013 的数据：
\[
p=6N+5\ge41,\quad k=\mathbf F_{p^2},\quad
E_0:y^2=x^3-1,\quad dz=dx/(2y),\quad L_6=O(6O),
\]
\[
F=x\sigma^6,\quad G=-xy\sigma^6,\quad
U=x^2\sigma^6,\quad Y_6=y\sigma^6,
\quad R_+=(x^3+2)\sigma^6,\quad R_-=(x^3-4)\sigma^6.
\tag{1017.1}
\]
记原普通 Taylor 系数
\(F=\sum f_i z^{6i+4}\)、\(G=\sum g_jz^{6j+1}\)，及
\[
H_p(\eta)=\sum_{i+j=N-1}\overline f_i\overline g_j\eta^{6i+4},
\qquad T^-=\{\eta\in k^\times:\eta^{p+1}=-1\}.
\tag{1017.2}
\]
临界有限系数的整性和规范均由 R702/R889 固定。

对原每个 norm-\(p\) 向量 \((\alpha,\beta)\)，仍取
\[
A=\begin{pmatrix}\alpha&-\overline\beta\\
                  \beta&\overline\alpha\end{pmatrix},
\quad N\alpha+N\beta=p,\quad
\gamma=-\overline\alpha/\beta,\quad \kappa=\alpha/\beta.
\tag{1017.3}
\]
\(\gamma\) 是核方向，\(\kappa\) 是微分像方向，不将两者识别。
R1013 已构造同一个原 rigidified 比较
\[
I_AA^*=\Omega_\gamma T_A,\qquad
\Omega_\gamma=\sum_{r=0}^{p-1}\gamma^{-r}Q_1^rQ_2^{p-1-r},
\]
\[
s_A=T_A^{-1}(F^p\boxtimes G^p)\in
H^0(L_6)\otimes H^0(L_6).
\tag{1017.4}
\]
\(F^p,G^p\) 在此表示原 Frobenius vacuum 中的实际 sections。
完整有限平坦 splitting、分布和 frame 已由 R1013 证明，本篇只使用其实际结论。

**定理 1017.1。** 对每个 (1017.3)，存在实际
\(a_A,b_A\in\overline k^\times\)，满足
\[
s_A=a_A\,U\boxtimes Y_6+b_A\,Y_6\boxtimes U,
\qquad a_A/b_A\in\mu_6.
\tag{1017.5}
\]
因此
\[
\boxed{\quad H_p(\eta)\ne0\quad\text{对每个 }\eta\in T^-.\quad}
\tag{1017.6}
\]
使用 \(\overline k\) 只是为固定 tame theta bases；
原 \(H_p\) 和其非零结论仍在原 \(k\) 中。共同 scalar 没有归一为一。

## 2. 三个真实半周期算子及二-primary 源限制

取 \(\zeta^2+\zeta+1=0\)，置
\[
s=\zeta-\zeta^2,\quad r=\sqrt3,\quad i=s/r,\quad i^2=-1.
\]
对 \(e^3=1\)，令 \(P_e=(e,0)\)。
在 \(H^0(L_6)\) 的有理 section 表示中，定义实际 theta lift
\[
\rho_e f(Q)=\frac{(x(Q)-e)^3}{3r}\,f(Q+P_e).
\tag{1017.7}
\]
其 divisor 正是所需 \(L_6\) 平移比较。加法公式为
\[
x(Q+P_e)=\frac{e(x+2e)}{x-e},\qquad
y(Q+P_e)=-\frac{3e^2y}{(x-e)^2}.
\tag{1017.8}
\]
直接代入得到
\[
\rho_e^2=1,\quad \rho_e\rho_f=-\rho_f\rho_e\ (e\ne f),
\quad \rho_1\rho_\zeta=\lambda\rho_{\zeta^2},
\quad \lambda=\frac{(1-\zeta)^3}{3r}=-i.
\tag{1017.9}
\]
循环置换 \(1,\zeta,\zeta^2\) 保持最后的乘法常数。

令 \(S=\rho_1+\rho_\zeta+\rho_{\zeta^2}\)。
由 (1017.8) 的实际矩阵可得
\[
V_-=\langle R_-,F,G\rangle,\qquad
V_+=\langle R_+,U,Y_6\rangle,\qquad
S|_{V_-}=-r,\quad S|_{V_+}=r.
\tag{1017.10}
\]
例如
\[
\rho_e(x^2)=\frac{e^2x^3+3x^2-4e^2}{3r},\qquad
\rho_e(y)=\frac{(1-e^2x)y}{r},
\]
求和即分别给 \(r x^2,r y\)；其余四项同由
(1017.8) 展开。两块维数各三。二、三-primary theta 子群交换，
故两块在整个三-primary theta 作用下稳定。

在 \(L_{6p}\) 的 Frobenius vacuum 中使用 multiplier 的 \(p\) 次幂
定义 \(\rho_{e,p}\)。于是
\[
\rho_{e,p}(f^p)=(\rho_e f)^p,
\quad \rho_{1,p}\rho_{\zeta,p}
 =\lambda^p\rho_{\zeta^2,p}.
\tag{1017.11}
\]
记 \(\mathcal K_A=T_A^{-1}\)。其与 tame theta 的实际运输来自
\(I_AA^*\)；\(\Omega_\gamma\) 与 tame 群交换。

二在 \(\mathbf Z[\zeta]\) 中惰性。
模二 \(N\alpha+N\beta=1\)，所以 \(\alpha,\beta\) 恰有一个非零，
另一个为零。故 \(A\) 在 \(E_0[2]^2\) 上是 monomial：
每一原轴送到一个目标轴，非零条目是 \(\mathbf F_4^\times=\mu_3\)，
只循环排列三个 \(P_e\)。
因 (1017.7)、(1017.11) 的 lifts 都平方为一，
每轴运输只能多三个符号。
对角 CM 的真实相容性使这三个符号相同，记作 \(\delta_j\)：
CM 循环排列 \(e\)，其对 \(\mathcal K_A\) 可能带的统一角色
在共轭算子时消去，不能造成各 \(e\) 不同的符号。

比较 (1017.9) 与 (1017.11) 的乘法常数，逐轴得到
\[
\delta_j^2\lambda=\lambda^p\delta_j,\qquad
\delta_j=\lambda^{p-1}=\left(\frac{-1}{p}\right)=:\delta.
\tag{1017.12}
\]
因此所有二挠 lift 相位都已保留并实际确定，未凭底层矩阵丢掉 character。

又令 \(\epsilon=(3/p)\)，则 \(r^p=\epsilon r\)。
原 \(F^p,G^p\) 各在 \(S_p\) 的特征值 \(-\epsilon r\) 空间。
由于 \(p\equiv5\pmod6\)，
\[
\delta\epsilon=\left(\frac{-3}{p}\right)=-1.
\]
按 (1017.12) 运输后，每轴的 \(S\) 特征值为
\((-\epsilon/\delta)r=r\)。轴置换不影响这个结论。因此
\[
s_A\in V_+\otimes V_+.
\tag{1017.13}
\]

R1013 的原 global \(\mu_6\) 计算同时给 \(s_A\) 的角色为五。
在 \(V_+\) 中 \(R_+,U,Y_6\) 的角色分别为零、二、三，
所以角色五空间恰为
\[
(V_+\otimes V_+)_5
 =\langle U\boxtimes Y_6,\ Y_6\boxtimes U\rangle.
\tag{1017.14}
\]
这已证明 (1017.5) 的两项形状，但还未证明两个系数都非零
或其相对相位；后两点必须用下面实际三-primary 运输。

## 3. 三-primary 的 canonical lifts 与原两种三维基

令 \(P=(0,i)\in\ker[s]\)。原 \(L_6\) 上的实际算子
\[
R f(Q)=-\frac{(y(Q)+i)^2}{4}\,f(Q+P)
\tag{1017.15}
\]
满足 \(R^3=1\) 及
\([-1]R[-1]^{-1}=R^{-1}\)。可直接用
\[
x(Q+P)=-\frac{2i(y-i)}{x^2},\qquad
y(Q+P)=i+\frac4{y+i}
\tag{1017.16}
\]
核准。三个平移后的 \(y+i\) 之积为 \(8i\)，故 multiplier 的
三次积为一。

这里“canonical”有精确含义：对一个三挠点，要求其 theta lift
三次为一，并在 \([-1]\) 下送到自己的逆。先将任一 lift 归一成
三次为一，再用唯一的 \(\mu_3\) scalar 满足第二条件；
唯一性用平方映射在 \(\mu_3\) 上可逆。
因此对称线丛的实际相容比较精确运输这些 lifts，不能另外添一个
三-primary character。两个 canonical lifts 的乘积与和点的
canonical lift 之差只能是 \(\mu_3\) scalar；这些相位后面全部保留。

由 (1017.15)–(1017.16)，在原基上有
\[
\begin{array}{lll}
RF=-F/2-iG/2,&RG=-3iF/2-G/2,&RR_-=R_-,\\
RU=U,&RR_+=-R_+/2-3iY_6,&RY_6=-iR_+/4-Y_6/2.
\end{array}
\tag{1017.17}
\]
例如 \(RU=U\) 直接来自
\((y+i)^2(y-i)^2=x^6\)。
这展示了两个原三维块上的实际作用，不是抽象指定一个同维表示。

取 \(Q_3\in E_0[3]\) 使实际 commutator 满足
\(R\tau_{Q_3}=\zeta\tau_{Q_3}R\)，其中 \(\tau_{Q_3}\) 为上述
canonical lift。令
\[
\delta_0^-=R_-,\quad\delta_t^-=\tau_{Q_3}^{\,t}R_-,
\qquad
\delta_0^+=U,\quad\delta_t^+=\tau_{Q_3}^{\,t}U,
\quad t\in\mathbf F_3.
\tag{1017.18}
\]
它们分别给 \(V_-,V_+\) 的基，且 \(R\delta_t^\pm=\zeta^t\delta_t^\pm\)。
因为两个 \(\delta_0^\pm\) 均为偶 section，canonical 对称性给
\[
[-1]\delta_1^\pm=\delta_{-1}^\pm.
\]
由 (1017.17) 的一维 eigenspaces，存在非零
\(k_-,k_+\) 使
\[
\begin{aligned}
\delta_1^-&=k_-(F-(i/s)G),&
\delta_{-1}^-&=k_-(F+(i/s)G),\\
\delta_1^+&=k_+(R_+-(6i/s)Y_6),&
\delta_{-1}^+&=k_+(R_++(6i/s)Y_6).
\end{aligned}
\tag{1017.19}
\]
每行两项确实具有同一个 \(k_\pm\)，而非两个未知相位。
特别地
\[
F=\frac{\delta_1^-+\delta_{-1}^-}{2k_-},\qquad
G=\frac{r(\delta_{-1}^--\delta_1^-)}{2k_-},\qquad
Y_6=\frac{r(\delta_{-1}^+-\delta_1^+)}{12k_+}.
\tag{1017.20}
\]
两轴都使用同一组实际基，所以目标两项的最后换算因子相同。

## 4. 实际 \(A\bmod3\)、四点运输及全部相对相位

在 \(\ker[s]^2=\langle P\rangle^2\) 上，
令 \(a=\alpha\bmod s,\ b=\beta\bmod s\in\mathbf F_3\)。
原 norm 等式给
\[
a^2+b^2=p=-1\pmod3,
\]
所以 \(a,b\in\{1,-1\}\)，且实际作用矩阵为
\[
A_0=\begin{pmatrix}a&-b\\b&a\end{pmatrix},
\qquad A_0^{\mathsf T}A_0=-I.
\tag{1017.21}
\]
本篇不称这个 multiplier \(-1\) 矩阵为同一配对的辛矩阵；
使用的是 \(L_6\) 与 \(L_{6p}\) 两个实际中心配对间的运输。

记
\[
\Delta_t^-=(\delta_{t_1}^-)^p\boxtimes(\delta_{t_2}^-)^p,
\qquad
\Delta_y^+=\delta_{y_1}^+\boxtimes\delta_{y_2}^+,
\quad t,y\in\mathbf F_3^2.
\]
高层 vacuum 中，\(R_x^{(p)}\) 对 \(\Delta_t^-\) 的特征是
\(\zeta^{p x^{\mathsf T}t}\)；这是实际 Frobenius 作用的负号。
canonical 相容性给
\[
\mathcal K_A R_x^{(p)}
 =R_{A_0x}\mathcal K_A.
\tag{1017.22}
\]
故输出特征标签 \(y\) 满足
\(A_0^{\mathsf T}y=pt=-t\)，由 (1017.21) 恰为 \(y=A_0t\)。
这些联合特征空间全为一维，遂有
\[
\mathcal K_A\Delta_t^-=d_t\,\Delta_{A_0t}^+,\qquad d_t\ne0.
\tag{1017.23}
\]
这里还没有归一 \(d_0\)。

**相位引理。** 对所有 \(t,t'\in\mathbf F_3^2\)，
\[
d_t/d_{t'}\in\mu_3.
\tag{1017.24}
\]
证明如下。两个实际 canonical shift
\(\tau_{Q_3}\boxtimes1\)、\(1\boxtimes\tau_{Q_3}\)
在高层 Frobenius 基上分别把 \(t\) 送到 \(t+e_1,t+e_2\)，系数为一。
其在 \(\mathcal K_A\) 下的像是相应实际点 \(A(Q_3,0)\)、
\(A(0,Q_3)\) 的 canonical lift。
将任一点写成原 \(P,Q_3\) 基的坐标后，该 lift 仅以某个
\(\mu_3\) scalar 区别于 \(R^u\tau_{Q_3}^v\)；
后者在 (1017.18) 中的每个非零矩阵元都是三次单位根。
逐列比较 (1017.23)，便得
\(d_{t+e_j}/d_t\in\mu_3\)。
两个 shifts 生成 \(\mathbf F_3^2\)，故得到 (1017.24)。
这保留了实际 lift 的每一个相对相位，只留下共同非零 scalar。

由 (1017.20)，指定原 \(F^p\boxtimes G^p\) 的支持恰为
\[
(t_1,t_2)\in\{1,-1\}^2,
\]
四个系数是同一个非零常数乘 \(\pm1\)。
由于 \(a,b\) 均为 \(\pm1\)，(1017.21) 把这四点双射到
\[
(0,1),(0,-1),(1,0),(-1,0).
\tag{1017.25}
\]
因此 \(s_A\) 在四个轴点上的系数都非零，而且任意两个之比在
\(\mu_6\) 中。

最后，\(\Omega_\gamma\) 的总 \(Q\) 次数 \(p-1\) 为偶数，
\(I_AA^*\) 亦与 \([-1]\) 相容，所以
\(\mathcal K_A\) 在此与对角 \([-1]\) 交换。
原 \(F^p\boxtimes G^p\) 是奇 section，故每条轴的两个相反点
系数也相反。结合 (1017.20) 的同一目标换算因子，得到
\[
s_A=a_A\,U\boxtimes Y_6+b_A\,Y_6\boxtimes U,
\quad a_A b_A\ne0,\quad a_A/b_A\in\mu_6.
\]
这完成了 (1017.5) 的全部断言。

## 5. 原第五阶读数排除全部范数负一零点

在原 frame 中，
\(U=z^2+O(z^8)\)、\(Y_6=-z^3+O(z^9)\)。
所以 (1017.5) 的首齐次项为
\[
P_A(u,v)=-u^2v^2(a_Av+b_Au).
\tag{1017.26}
\]
在非零像方向 \(\kappa\) 上，它唯一可能的非零根是
\[
\kappa=-a_A/b_A\in\mu_6.
\]
但 \(6\mid p+1\)，每个六次单位根的范数都是一；原
\(\kappa^{p+1}=-1\)。因此 \(P_A(\kappa,1)\ne0\)。

R1013 (1013.17)–(1013.19) 是同一个实际 section 的准确整 jet 比较：
\[
\frac{(6B)^5}{12}\gamma^{-2}H_p(\gamma^{-1})
 =10\beta^2\overline\alpha^{\,3}P_A(\kappa,1).
\tag{1017.27}
\]
所有外乘因子在 \(p\ge41\) 时皆为单位。
R1012 的每方向十二表示保证每个 \(\eta\in T^-\) 都能写成
\(\gamma^{-1}\)。于是 (1017.27) 证明 (1017.6)，且没有
\(p>10^{12}\) 的门槛或例外方向。

## 6. 对原任务的范围

本篇把 R1013 的统一有限零点界加强为零点集合为空，并给
R1012 的相同原导数平衡读数在全部实际方向非零。
没有换源、换微分、改 sigma 规范，亦未使用有限扫描猜测。

原 O1 仍要求同一个
\[
h=6i+7,\qquad i+j=N-1,\qquad
(h,p+1)=1,\qquad P_{h-1}(1/s)f_i g_j\ne0.
\]
(1017.6) 是原未经筛选 \(H_p\) 的值定理，尚不是这些实际 Fourier
坐标的保留支撑定理。上述相位分析明确保留了随 \(A\) 变化的共同
scalar，不能在求 primitive 投影时把它替换成一。
后继 [R1020](R1020-original-critical-convolution-complete-theta-scalar-bridge.md) 已证明这个真实 scalar 与原 \(\sigma^2\) 小 index 源的完整精确比例；继续保留它并计算
同一个原 mask 下的读数。
O2 的 bare 高系数仍须保完整余项；O0 的全部全局覆盖和非 CM
实际首提升继续开放。**Serre 主目标仍 OPEN。**

## 7. 依赖与全文核准

- [R1012](R1012-original-p-similitude-divided-high-coordinates-and-critical-bridge.md)：原 norm-\(p\) 同源和每个核/像方向的十二表示。
- [R1013](R1013-original-theta-descent-and-uniform-critical-zero-bound.md)：原有限平坦下降、完整 tame 相容比较、global \(\mu_6\) 角色及准确第五阶 jet；本篇加强其 §4 和 §6，没有重做已成分布。
- [R878](R878-original-finite-theta-action-and-section-projections.md)、[R889](R889-original-theta-distribution-and-same-label-sigma-jet.md)：原 theta lifts、tame 中央化和合法有限整范围。
- R1013 已实读的 Moonen, Theorem 8.10/Proposition 8.15，及 Shin, Propositions 2.12–2.13，提供实际下降与 theta 表示基础；本篇额外所需相位均由 (1017.7)–(1017.24) 显式证明。

o1_theta 与 root 独立纸面核准实际半周期算子、两块的 \(S\) 特征值、
Frobenius 的 \((3/p)\) 与 \((-1/p)\) 符号、canonical 三挠 lifts、
两种基的同一换算因子、\(A_0^{\mathsf T}y=pt\) 的正确标签、
四点到两轴的运输及相对 \(\mu_6\) 相位。无数学程序执行、
无旧矩阵枚举或已成窗口重跑。
