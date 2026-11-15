# R390：两个固定自然总通量的真实联合控制

日期：2026-11-15。**有限纸面构造；没有执行新的 profile 积分、几何计算、符号程序、参数扫描、人工检查或研究运行。**

[R386](R386-complete-quartic-velocity-natural-flux-and-a-new-mixed-direction.md)
已给完整四次速度成本的准确自然读出。本稿从该完整公式选择两个固定真实紧 profile，构造四个实际方向的严格正核，再把它们接到同一有限几何族。

结论是：可以一次固定两个实 $C_c^\infty$ profile、共同右锚、物理窗口、常值端口和严格 $\omega$ 下界，使两个自然总通量在真实 $M=T=0$、scalar/frame/空间位移全部闭合的有限路径上同时取任意指定的二元实值。对每个紧目标集，可用同一有限拼接类型、同一个正脉冲尺度，取得光滑截面。

本稿不把系数函数的线性维数当作实际控制。四列正核、原矩阵桥、真实历史倒行、全部非零桥基准以及最后一次二维求解均在下面保留。

## 1. 两个固定读出与原完整公式

固定同一个右锚 $r_*$。记
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
对真实紧 profile $u$，使用
[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)
的原自然总通量
$$
\Lambda_u(V)=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{1}
$$
$\mathscr G$ 是原有序 pure $2+2$ 三矩尾映射。它使用真实右辅助包，不能任意重锚或把左尾置零。

实际状态记为 $S=(h,k,\omega)$，$h>0$，并置
$$
d=h\omega-k,\qquad e=hx+d,\qquad Q=1+e^2,
$$
$$
v=u',\qquad r=u'',\qquad t=u''',\qquad
\gamma=h_s,\quad\delta=d_s.
$$
R386 的完整正规四次速度读出为
$$
\boxed{
\Lambda_u(\mathcal Q_S[\gamma,\delta])
=-\frac{1}{32h^8}
\int Q\{\gamma v-(\gamma x+\delta)r\}^4t.}
\tag{2}
$$
这包含原 $C_A m_2$、$\mathcal B_{m_2}N_2$、全部 $ZZ/YC$ 链项及真实尾；不是一个尚未取得 $U$ 资格的 ambient 单项。

特别在 $h=1$，
$$
\Lambda_u(\mathcal Q_S[0,1])
=\frac{X(u)+dM(u)}{80},\qquad
M(u)=\int r^5,\quad X(u)=\int xr^5.
\tag{3}
$$
在 $h=1,d=0$ 的纯 $\gamma$ 方向则是
$$
\Lambda_u(\mathcal Q_S[1,0])
=-\frac1{32}\int(1+x^2)(v-xr)^4t.
\tag{4}
$$
两个式子都不依赖该层中的独立 $k$。

## 2. 真紧偶母包与一对镜像 profiles

取非零非负偶 bump $\eta\in C_c^\infty(\mathbb R)$，选一个有限 $b>0$，使
$\eta(y),\eta(y-b),\eta(y+b)$ 的支撑互不交。定义
$$
r_0(y)=\eta(y)-\frac12\eta(y-b)-\frac12\eta(y+b).
$$
准确有
$$
\int r_0=\int yr_0=0.
$$
在母包的右 collar 取 $u_0=J^2r_0$，故 $u_0$ 是真实紧光滑偶函数，$u_0''=r_0$。其左侧仿射尾由上述两矩准确消去；缩放、平移后再用共同物理右锚恢复，仍是下面同一个函数，没有新增积分常数。并且
$$
M_0=\int r_0^5=\frac{15}{16}\int\eta^5>0.
\tag{5}
$$

固定 $0<a<1$。在下文所有几何选择之前，选择一个充分小但有限的正 profile 宽度 $\rho$，并固定
$$
u_+(x)=u_0\!\left(\frac{x-a}{\rho}\right),\qquad
u_-(x)=u_0\!\left(\frac{x+a}{\rho}\right)=u_+(-x).
\tag{6}
$$
$\rho$ 可同时保证两个支撑不交。它之后不再随目标或几何脉冲尺度变化。

定义
$$
M=\rho^{-9}M_0>0,\qquad m=\frac{M}{80},\qquad A=am>0.
\tag{7}
$$
两个 profile 的第五矩及第一加权矩准确为
$$
M(u_\pm)=M,\qquad X(u_\pm)=\pm aM.
\tag{8}
$$
固定向量读出
$$
\mathcal L(V)=\bigl(\Lambda_{u_+}(V),\Lambda_{u_-}(V)\bigr)\in\mathbb R^2.
\tag{9}
$$

还要核准纯 $\gamma$ 列的真实符号。令
$$
v_0=u_0',\quad t_0=r_0',\quad L_0=v_0-yr_0.
$$
紧端分部积分给
$$
\int r_0^4t_0=0,\qquad
\int yr_0^4t_0=-\frac{M_0}{5},\qquad
\int L_0r_0^3t_0=-\frac{M_0}{20}.
\tag{10}
$$
最后一式用
$\int v_0r_0^3t_0=-M_0/4$。

将 (6) 直接代入完整式 (4)，得到
$$
g_\rho:=
\Lambda_{u_+}(\mathcal Q_{h=1,d=0}[1,0])
=-\frac{\rho^{-10}}{32}
\int\{1+(a+\rho y)^2\}(\rho L_0-ar_0)^4t_0.
$$
由 (10)，其一阶 $\rho$ 项准确为
$$
\boxed{
g_\rho=
\frac{M_0a^3(a^2-1)}{160}\rho^{-9}
+O(\rho^{-7}).}
\tag{11}
$$
这里是一个有限多项式展开：$r_0$ 偶，$L_0,t_0$ 奇，所以所有偶次 $\rho$ 系数都准确为零。没有无限渐近求和或数值求积。

因此可以一次选定有限 $\rho>0$，使
$$
g_\rho<0,\qquad B:=-g_\rho>0.
\tag{12}
$$
同时反射在 (4) 中给准确身份
$$
\Lambda_{u_-}(\mathcal Q_{h=1,d=0}[1,0])=-g_\rho.
\tag{13}
$$

## 3. 四个完整 Q4 列与严格正核

固定有限 $D>a$。所有状态取 $h=1$；用同一个稍后指定的大正 $K$，写
$$
S_0=(1,K,K),\qquad
S_+=(1,K,K+D),\qquad
S_-=(1,K,K-D).
\tag{14}
$$
它们的 $d$ 分别为 $0,D,-D$。

由 (3)、(12)、(13)，以下四列是原完整 Q4 的实际读出：
$$
\begin{aligned}
v_1&=\mathcal L(\mathcal Q_{S_0}[0,1])=A(1,-1),\\
v_2&=\mathcal L(\mathcal Q_{S_0}[1,0])=-B(1,-1),\\
v_3&=\mathcal L(\mathcal Q_{S_+}[0,1])=A(1,-1)+Dm(1,1),\\
v_4&=\mathcal L(\mathcal Q_{S_-}[0,1])=A(1,-1)-Dm(1,1).
\end{aligned}
\tag{15}
$$
全部数值来自同一个固定的向量读出 (9)。没有在不同列中重选 profiles。

两列的行列式与一个严格正核分别为
$$
\det(v_3,v_4)=-4ADm\ne0,
\tag{16}
$$
$$
\boxed{
v_1+\frac{3A}{B}v_2+v_3+v_4=0.}
\tag{17}
$$
因此这四列的正锥是 $\mathbb R^2$。更具体地，任一实线性表示都可加上 (17) 的充分大正倍数，使四个系数全为正。

实际构造并不止于这条正锥结论。下面用正脉冲幅的四次幂实现这些系数，并在原完整成本上一次求解。

## 4. 先固定共同物理域和端口

先取有限共同区间 $I=[\ell,r_*]$，含 (6) 的两个 profile、原有序尾读出所需的固定右辅助包，并在两端保开 collar。辅助包可一次放在两个主支撑的右方。

固定
$$
\Omega>\max(0,-\ell)+1
$$
及有限
$$
K>\Omega+D+2.
\tag{18}
$$
因此三个端口 (14) 都有严格正的 $\omega$ 余量。
共同最终端口固定为 $S_0$。

这里允许 $I$ 含负的 $x$。合法性由整个实际几何满足
$\omega>\Omega$，从而 $x+\omega>1$ 给出；不是把原式在极点另一侧形式延拓。

所用实际桥是
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)
§8–9 的受控 $\omega$ 版 R70。
它同时处理给定 scalar germs、frame 与真实矩阵目标。在固定小目标邻域内，
其有限拼接类型、辅助整数和正时间余量可一次选择，得到光滑桥族。

## 5. 四个真正水平脉冲

固定非零非负偶函数
$\psi\in C_c^\infty((-1,1))$，并置
$$
c_4=\int_{-1}^1(\psi')^4>0.
$$
选几何小参数 $\varepsilon>0$，令
$$
\tau=\varepsilon^{3/2},\qquad s=\tau t,\quad -1\le t\le1.
\tag{19}
$$
它与已固定的 profile 宽度 $\rho$ 无关。

每个脉冲使用正幅 $z_i$。所有 $z_i$ 限于一个在下文先固定、离零的紧盒。

对第 $1,3,4$ 列，分别令 $d_i=0,D,-D$，定义
$$
\begin{aligned}
h(s)&=1,\\
d(s)&=d_i+\varepsilon z_i\psi(t),\\
k(s)&=K-2\varepsilon z_i\psi(t),\\
\omega(s)&=K+d_i-\varepsilon z_i\psi(t).
\end{aligned}
\tag{20}
$$
对第 $2$ 列，定义
$$
H(s)=1+\varepsilon z_2\psi(t),\qquad
h(s)=H(s),\quad d(s)=0,\quad
k(s)=KH(s)^2,\quad \omega(s)=KH(s).
\tag{21}
$$

原水平关系是
$$
k_s=2\omega h_s-2d_s,\qquad
\omega_s=\frac{\omega h_s-d_s}{h}.
\tag{22}
$$
(20)、(21) 逐点准确满足它们及 $d=h\omega-k$。
各自两端都是同一个指定常值端口：前三个 $\delta$ 脉冲分别在 $S_0,S_+,S_-$；
$\gamma$ 脉冲在 $S_0$。所有正阶 scalar jets 在端 collar 为零。

充分小但有限的 $\varepsilon$ 保持 $h>1/2$、$\omega>\Omega+1$。
frame 方程按原式真实演化。它的系数在固定状态盒上有界，所以每个短段 $B_{i,\varepsilon,z_i}$ 满足
$$
F_i=I+O_{C^1(z_i)}(\tau).
\tag{23}
$$
由 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 的原矩阵密度只有导数权零和二，
$$
M_{B_i}
=O_{C^1(z_i)}(\tau+\varepsilon^2/\tau)
=O_{C^1(z_i)}(\varepsilon^{1/2}).
\tag{24}
$$
这不是对第三历史或第四成本的大小估计。

## 6. 原局部密度的向量领先项

采用
[R109](R109-local-density-of-the-complete-fourth-quotient.md)
的完整密度
$$
L=v-\mathcal B_mN=L_0+L_2+L_4
$$
以及
[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)
的原水平分部积分正规化。

如 [R385](R385-actual-two-sided-natural-flux-control-from-complete-Q4-pulses.md)，
在一个含全部局部模板、$U$ 与 $\mathcal R$ 的固定有限真实环境中，
逐分量使用 (9) 的线性读出 $\boldsymbol\ell$。
它在 $\mathcal R$ 上为零。短段尚未总 $M=0$ 时，仅记
$$
I_{\boldsymbol\ell}(B)=\int_B\boldsymbol\ell(L)\,ds;
$$
暂不把它等同于该短段的真实第四 canonical 成本。

[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)
使全部完整加速度平方系数在每个状态上的两个读出均为零。
[R382](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md)
又使全部完整 H 系数逐状态为零。
这些是更正后成立的全状态身份，不使用已经撤回的旧 H 非零值。

所以在 (20)、(21) 的某个固定单位速度方向上，剩下完整 Q4、
导数权二和导数权零。正规端势在两个常值 germs 消失。
设该方向速度为
$\alpha=\varepsilon z_i\psi'/\tau$。
由 (15)、状态变化 $O_{C^1(z_i)}(\varepsilon)$ 及 Q4 的完整光滑公式，
$$
\int_{B_i}\boldsymbol\ell(L_4)\,ds
=c_4\frac{\varepsilon^4}{\tau^3}z_i^4v_i
+O_{C^1(z_i)}(\varepsilon^5/\tau^3).
$$
原 $L_2,L_0$ 连同其全部校正保留，且
$$
\int_{B_i}\boldsymbol\ell(L_2)\,ds
=O_{C^1(z_i)}(\varepsilon^2/\tau),\qquad
\int_{B_i}\boldsymbol\ell(L_0)\,ds
=O_{C^1(z_i)}(\tau).
$$
因此
$$
\boxed{
I_{\boldsymbol\ell}(B_{i,\varepsilon,z_i})
=c_4\varepsilon^{-1/2}z_i^4v_i
+O_{C^1(z_i)}(\varepsilon^{1/2}).}
\tag{25}
$$
所有常数可依赖已固定的 $\rho,I,K,D$ 和正幅盒，但不依赖趋零的 $\varepsilon$。

## 7. 真实矩阵恢复、同号倒行与固定端口运输

对每个短段的实际数据 (23)、(24)，选 R354/R70 的光滑桥
$$
C_i:(S_i,F_i)\longrightarrow(S_i,I),\qquad
M_{C_i}=-M_{B_i},
\tag{26}
$$
其中第 $2$ 列也取 $S_i=S_0$。
相对 frame 目标是短段实际末 frame 的逆。
这些目标在固定小邻域内，所以桥的真实长度、状态、有限 jets 和一次幅导数统一有界。
特别
$$
I_{\boldsymbol\ell}(C_i)=O_{C^1(z_i)}(1).
\tag{27}
$$
桥有自己的完整成本；不把目标趋零的桥当作空路径。

令 $D_i=B_iC_i$，则同一端口、frame $I\to I$ 且 $M_{D_i}=0$。
现在才用原 R109 的保真历史关系
$$
V_{D_i}-\int_{D_i}L\,ds\in\mathcal R.
$$
因此
$$
\mathcal L(V_{D_i})
=c_4\varepsilon^{-1/2}z_i^4v_i
+O_{C^1(z_i)}(1).
\tag{28}
$$

用
[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)
的同 $k$ 真倒行。若
$b_i=-2T_{D_i}(\phi;D_{\rm profile})$，
其 canonical 第三场准确是
$$
Z_3^{\rm rev}=-OZ_3\circ{\rm rev}+Y_{b_i}^{\rm rev}.
$$
后一项产生的额外第四成本为 $-2A_{D_i}(\phi,b_i)=0$，
因为整个矩阵 $M_{D_i}=0$。故
$$
M_{D_i^{\rm rev}}=0,\qquad
T_{D_i^{\rm rev}}=-T_{D_i},\qquad
V_{D_i^{\rm rev}}=V_{D_i}.
\tag{29}
$$
这里真实第四成本是同号。
所以 $P_i=D_iD_i^{\rm rev}$ 准确满足
$$
M_{P_i}=T_{P_i}=0,\qquad V_{P_i}=2V_{D_i}.
\tag{30}
$$
第三历史可以很大；等式不靠小量截断。

再为三个有限状态预先固定真实桥
$$
A_i:S_0\longrightarrow S_i,\qquad
M_{A_i}=0,\qquad F_{A_i}:I\to I,
\tag{31}
$$
全程 $\omega>\Omega$，首末为指定常值 germs。
这些桥不依赖脉冲幅或 $\varepsilon$；$S_i=S_0$ 的桥也允许有非零基准。
令
$$
Q_i=A_iP_iA_i^{\rm rev}.
$$
原完整传递式中所有涉及 second 的交叉项因各段矩阵为零而消去，
桥的 third 由真正反向桥相消。因此
$$
M_{Q_i}=T_{Q_i}=0,\quad F_{Q_i}=I,\qquad
V_{Q_i}=2V_{A_i}+2V_{D_i}.
\tag{32}
$$
全部 $Q_i$ 现在使用同一个固定端口 $S_0$。

## 8. 同一有限参数下的二维精确求解

将四个 $Q_i$ 真实串接。各自 $M=T=0$，故完整第四成本准确相加。
记
$$
\Phi_\varepsilon(z)
=\mathcal L(V_{Q_1Q_2Q_3Q_4}).
$$
由 (28)、(32)，包括所有 bridge 基准在内，
$$
\boxed{
\Phi_\varepsilon(z)
=2c_4\varepsilon^{-1/2}\sum_{i=1}^4z_i^4v_i
+R_\varepsilon(z),\qquad
R_\varepsilon=O_{C^1(z)}(1).}
\tag{33}
$$

由严格正核 (17)，固定
$$
z_1=1,\qquad z_2=(3A/B)^{1/4},
$$
只让
$$
z_3=w_3^{1/4},\qquad z_4=w_4^{1/4}
$$
在 $w=(1,1)$ 的一个固定小正邻域中变化。
令 $\mathsf V=[\,v_3\ v_4\,]$，则
$$
\Phi_\varepsilon(w)
=2c_4\varepsilon^{-1/2}\mathsf V\bigl(w-(1,1)\bigr)
+\widetilde R_\varepsilon(w).
\tag{34}
$$
$\mathsf V$ 可逆，$\widetilde R_\varepsilon$ 及其一次 $w$ 导数统一有界。

对任意固定紧目标集 $\mathcal K\subset\mathbb R^2$，方程
$\Phi_\varepsilon(w)=y$ 等价于
$$
w=(1,1)+\frac{\sqrt\varepsilon}{2c_4}
\mathsf V^{-1}\{y-\widetilde R_\varepsilon(w)\}.
\tag{35}
$$
一次选取充分小但严格正的有限 $\varepsilon$，即可使右边对所有
$y\in\mathcal K$ 都把同一个闭小球映入其内部，且 $w$ 导数范数小于 $1/2$。
收缩定理给唯一的真实解 $w(y)$；原路径和桥光滑依赖幅值，
非退化的有限参数隐函数定理又给目标附近的光滑截面。

于是
$$
\mathcal L(V_{Q_1Q_2Q_3Q_4})=y
\tag{36}
$$
是整个原成本的准确等式。
两自由正幅在同一有限 $\varepsilon$ 下同时选择；没有对两个坐标分开选极限路径。
未将无穷复制、零时长路径或实数次拼接用于实际实现。

## 9. 原 Klein 字闭合整个空间位移

还需支付空间闭合，不能只停在 frame 恒等。
按 R385 使用
[R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md)
的固定真实 $M=T=0$ frame 桥，
并由 R354 安装到同一个 $S_0$、保 $\omega>\Omega$：
$$
C_1:I\to g_1,\quad C_2:I\to g_2,\qquad
g_1=\operatorname{diag}(1,-1,-1),\quad
g_2=\operatorname{diag}(-1,1,-1).
$$
它们的第四成本完整保留。

令 $Q=Q_1Q_2Q_3Q_4$。
第一 prototype 为 $QC_1$，第二为 $C_2$，使用原八边词
$$
1,2,1,2,2,1,2,1.
\tag{37}
$$
每种 prototype 都在四个 ambient 左旋位置
$\{I,g_1,g_2,g_1g_2\}$ 各出现一次。
四个矩阵之和为零，所以两种 prototype 的完整真实空间位移分别相消。
这个论证也包括随两个目标变化的 $Q$ 的全部位移。

所有段均 M0/T0，故最终闭路径 $X$ 的完整成本为
$$
V_X=4V_Q+4V_{C_1}+4V_{C_2}.
\tag{38}
$$
记固定向量基准
$$
b_K=\mathcal L(4V_{C_1}+4V_{C_2}).
$$
它可以非零，不能在求解前删除。
对指定最终目标 $y$，在 (35) 中改用
$(y-b_K)/4$，便准确得到
$$
\boxed{
\mathcal L(V_X)=y,\qquad
M_X=T_X=0,\qquad
\text{scalar、frame 与空间位移全部闭合},\qquad
h>0,\ \omega>\Omega.}
\tag{39}
$$
紧目标集经固定仿射变换仍是紧集，故同一有限 $\varepsilon$ 和光滑截面保持。

## 10. 选择顺序和准确完成范围

所有对象按下列有限次序选择：

1. 选 $\eta,b,u_0$，固定 $a\in(0,1)$，再一次选小正 $\rho$，使 (11) 的真符号成立；得到两个固定 profiles。
2. 固定原右辅助包、共同 $I$、右锚、$\Omega$、有限 $D,K$、三个端口及两读出。
3. 固定 $\psi$、四列正核、幅值盒、全部 M0/transport/Klein 桥类型与有限辅助整数。
4. 对一个指定紧目标集，一次选择正的有限 $\varepsilon$ 和 $\tau=\varepsilon^{3/2}$。
5. 最后仅由准确方程 (35) 选择两个正幅；所有原桥目标随实际短段数据共同更新。

原 $\alpha_s=h^2T$、$h>0$ 与 $x+\omega>1$ 给真实闭正则几何数据。
本稿不证明嵌入、reach 或全 range/period。

(39) 是两个固定自然总通量的实际联合满射及紧集光滑截面。
参数选择产生不同的真实几何；它不保持一个预先冻结的 $g$。
也不要求 whole pure/self、其它自然读出、同一个二阶 gauge 或全部 period 同时保持。
更不把 R386 至少三个函数方向升级成实际三维控制。

本稿所增加的实际机制是：完整纯 $\gamma$ 列与纯 $\delta$ 列在这两个固定 profiles 上提供相反的第一方向，两个不同固定 $d$ 状态再提供独立的第二方向；严格正核使这些方向可由四个真实正幅脉冲联合使用。全部加速度平方和 H 层由已更正的完整零身份消去，所有非零桥基准则在同一个有限二维方程中支付。
