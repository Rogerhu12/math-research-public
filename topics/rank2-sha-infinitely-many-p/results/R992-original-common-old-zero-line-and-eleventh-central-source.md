# R992 — 原两 old 块的共同真零线、第十一来源与完整十三边界

日期：2026-11-26 UTC。**已证明：原 degree130 两个13-old块之间有一条非零、首项一的完整来源，其中央导数在全部好惰性素数处无条件为零，并在 R968 已固定的普通射线上也无条件为零。它给原 H/F11 一个准确的 whole 零关系，可作为 R989 同一六位系统的第十一行。** 该来源不属于任一单独的 old primitive 线；两个质量一 old 差的非零中央没有被改写为零。

本篇还将 R987/R993 的真实两核边界与这条新零线合并：两条 rank≥2 canonical、这条无条件零线以及一个明确非零 old 对照的边界恰满四维。全部常数来自同一原来源；这一边界满秩不替代原 $P_2$、平移缺陷 $\Xi_T$、高 jet 或移动零点的完整 Cartier 读取。

## 1. 原 level10 质量核及准确的新来源

先在同一个 $E_1:y^2=x^3+1$、原微分 $dz=dx/(2y)$ 与原 sigma 中工作。置

$$
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\pi=(7+\delta)/2,\quad\bar\pi=(7-\delta)/2,\quad
N\pi=13,\quad w=z^6.
\tag{1}
$$

R978 的两个质量一来源是

$$
\Psi_-:=\Psi_{125}=\sigma^{10}x^2(X-8),\qquad
\Psi_+:=\Psi_{12500}=\sigma^{10}x^2(X+10),\qquad X=x^3.
\tag{2}
$$

因此同一个完整 level10 principal 空间的质量核是

$$
f_0=\sigma^{10}x^2=\frac{\Psi_+-\Psi_-}{18},\qquad
f_0(0)=0,\qquad f_0=z^6+O(z^{12}).
\tag{3}
$$

记 $D_\alpha f(z)=f(\alpha z)$，$\Delta_\pm=D_\pi\Psi_\pm-D_{\bar\pi}\Psi_\pm$。定义

$$
\boxed{\quad
\mathcal X_{130}
=\frac{D_\pi f_0-D_{\bar\pi}f_0}{2520\delta}
=\frac{\Delta_+-\Delta_-}{45360\delta}.\quad}
\tag{4}
$$

R978 的原绝对 CM 规范给 $\pi^6-\bar\pi^6=2520\delta$。由(3)，

$$
\mathcal X_{130}(0)=0,\qquad
\boxed{\mathcal X_{130}=w+O(w^2)\ne0.}
\tag{5}
$$

两个 raw pull 都是 R978 已付的 standard even degree130 截面；(4)没有更换半特征、除法函数或相位。原 $\mu_6$ 作用固定 $f_0$，故也固定 $\mathcal X_{130}$。复共轭同时交换两 raw pull 并将 $\delta$ 变号，所以(4)的全部系数在 $\mathbf Q$ 中。

### 1.1 不读取生成系数的完整分子

沿 R978 的原 norm13 除法函数，写

$$
R_\pi(X)=X^2+(2+6\delta)X+\frac{40+24\delta}{13},
\qquad
\sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X),
\tag{6}
$$

$$
x(\pi z)=\frac{x A_\pi(X)}{\pi^2 R_\pi(X)^2},
\qquad \deg A_\pi=4,\quad [X^4]A_\pi=1.
\tag{7}
$$

式(7)仍是原完整分子，以下恒等式唯一指定它，未新增选择。令 $q(x)=R_\pi(x^3)$，撇号表示对 $x$ 求导，则

$$
xA_\pi(x^3)
=13xq^2-4(x^3+1)(q''q-(q')^2)-6x^2q'q.
\tag{8}
$$

因此包括零质量列在内的完整来源是

$$
\boxed{
\mathcal X_{130}=\sigma^{130}x^2 P_{\mathcal X}(X),\qquad
P_{\mathcal X}(X)=
\frac{\pi^6 A_\pi(X)^2R_\pi(X)^6
 -\bar\pi^6\bar A_\pi(X)^2\bar R_\pi(X)^6}{2520\delta}.}
\tag{9}
$$

两个分子项的次数都是20，由(1)得

$$
\deg P_{\mathcal X}=20,\qquad [X^{20}]P_{\mathcal X}=1.
\tag{10}
$$

这是完整多项式身份，使用 R978 已真实返回的两个 raw pull 的第一列，没有用首项拟合整个来源。由(6)–(8)，$R_\pi\in13^{-1}\mathcal O_K[X]$、$A_\pi\in13^{-2}\mathcal O_K[X]$。对 $u\in\mathcal O_K$，有 $(u-\bar u)/\delta\in\mathbf Z$。故可用以下充分固定分母：

$$
\boxed{P_{\mathcal X}\in(2520\cdot13^{10})^{-1}\mathbf Z[X]}
\tag{11}
$$

它只引入 $2,3,5,7,13$，不新增大于211的坏素数。

## 2. 完整新来源仍在原六源角帽中

置 $Q_2(X)=7X^2-4X+16$，保持原负角 $t=-x^{-3}$。先证明完整整除

$$
\boxed{(X+1)Q_2(X)\mid P_{\mathcal X}(X).}
\tag{12}
$$

在非零二挠点处 $X=-1$。因为 $\pi\equiv\omega\pmod2$、$\bar\pi\equiv\omega^2\pmod2$，原有理映射(7)给

$$
A_\pi(-1)=\omega(\pi R_\pi(-1))^2,
\qquad
\bar A_\pi(-1)=\omega^2(\bar\pi\bar R_\pi(-1))^2.
$$

由(6)直接得 $\pi R_\pi(-1)=-27\omega$、$\bar\pi\bar R_\pi(-1)=-27\omega^2$。所以(9)的两个分子项在 $X=-1$ 都等于 $27^{10}$。

对二次因子使用原 $\gamma=3+\omega$ 及其共轭。R983 的原除法函数给

$$
Q_2=7R_\gamma R_{\bar\gamma},\qquad
R_\gamma=X+(-2+6\delta)/7.
$$

这些根对应的点属于 $E[7]$。由 $\pi+\bar\pi=7$，其 $\pi$ 与 $\bar\pi$ 像互为负点、$x$ 坐标相同。原 norm13 身份又给

$$
\pi R_\pi+\bar\pi\bar R_\pi=Q_2.
$$

故模 $Q_2$ 有 $\pi R_\pi=-\bar\pi\bar R_\pi$，再由(7)得 $A_\pi=\bar A_\pi$。分母在这些点非零，因为非零点不可能同时位于 norm7 和 norm13 核。于是两个表达式 $A_\pi^2(\pi R_\pi)^6$ 与 $\bar A_\pi^2(\bar\pi\bar R_\pi)^6$ 在 $Q_2$ 的全部根处相等。该二次多项式无重根，且 $Q_2(-1)=27\ne0$，证明(12)。

写 $P_{\mathcal X}=\sum_{j=0}^{20}b_jX^j$，完整角式是

$$
\mathcal X_{130}=\Theta^{65}f_{\mathcal X}(t),\qquad
f_{\mathcal X}(t)=\sum_{j=0}^{20}b_j(-t)^{21-j},\qquad
\Theta=x\sigma^2.
\tag{13}
$$

因此 $\deg f_{\mathcal X}\le21$，在 $t=0$ 的阶准确为一；(12)还给 $t=1$ 及 $7+4t+16t^2$ 两个根处均至少一阶。这些条件准确支付原 $B^{(6)}$ 的 charge65 帽：

$$
21=\left\lfloor65\frac{64}{195}\right\rfloor,\qquad
1=\left\lceil\frac{65}{195}\right\rceil.
\tag{14}
$$

加入该真实来源仍保持 R960/R982 的同一规范化、完整角帽和 $2/13$ 累积 Hilbert 主项；原物理窗没有扩大。

## 3. 惰性完整 Tate 身份与准确二重中央零

固定原有限坏集之外的 $p=6s-1>211$，置

$$
d=p+1,\qquad c=[z^d]\log(\sigma/z),\qquad
q_\pi=\pi^d/13,\quad q_{\bar\pi}=\bar\pi^d/13.
\tag{15}
$$

在惰性完成中，Frobenius 模 $p$ 将 $\pi$ 送到 $\bar\pi$，故 $q_\pi,q_{\bar\pi}\in1+p\mathcal O$。仍用原完整 Newton 函数；对每个非负整数 $k$，它们的准确插值是

$$
J_{10,f_0}(k)=k!(10c)^{-k}[z^{dk}]f_0,
\qquad
J_{130,D_\pi f_0}(k)=k!(130c)^{-k}\pi^{dk}[z^{dk}]f_0.
$$

R978/R989 的同一整 sigma 窗和 Hurwitz 界适用于 $f_0$，因为其 regularized 式为 $w f^{-5}W^2$。下式两边都是真正的限制 Tate 函数，在稠密的非负整数上相等，所以

$$
\boxed{
J_{\mathcal X,p}(v)
=\frac{q_\pi^v-q_{\bar\pi}^v}{2520\delta}
          J_{10,f_0,p}(v).}
\tag{16}
$$

其中 $J_{10,f_0,p}(0)=f_0(0)=0$，第一个因子在零处也为零。因此

$$
\boxed{J_{\mathcal X,p}(v)\in v^2\mathcal O\langle v\rangle,
\qquad J'_{\mathcal X,p}(0)=0.}
\tag{17}
$$

这里不使用秩、Selmer 或中央失败假设。与此同时，R978 对(2)的两个质量一来源仍分别给

$$
J'_{\Delta_-,p}(0)=J'_{\Delta_+,p}(0)
=d\log_p(\pi/\bar\pi)\ne0.
\tag{18}
$$

导数零只属于(4)这个指定差，两个单独的 old 方向仍非零。(18)中的对数非零：局部单位的对数若为零，该单位便是根单位；嵌入单射使 $\pi/\bar\pi$ 成为全局根单位，与其两个 norm13 赋值 $1,-1$ 矛盾。

## 4. 普通零在原 whole degree10 射线上也成立

本节准确保持 R968 的普通射线。其整个 standard even $\mathcal S_{10}$ core 在每个向量上都是同一个 $\upsilon_p=\chi_{10}\lambda_p$，没有按不同曲线另选 scalar。由 R968 §2 和 R978(19)，

$$
\nu_{f_0}|_{p\mathbf Z_p}
=\upsilon_p[\kappa_p]_*\nu_{f_0}.
$$

又 $\nu_{f_0}(\mathbf Z_p)=f_0(0)=0$，遂得真正的单位质量

$$
\boxed{\nu_{f_0}(\mathbf Z_p^\times)=0.}
\tag{19}
$$

式(19)使用整个 degree10 core，不能仅将单位质量换成总质量来证明。

定义原指数为 $(p-1)v$ 的 principal 读者

$$
\mathcal L_p^{\rm ord}(f;v)
=\int_{\mathbf Z_p^\times}\langle y\rangle^{(p-1)v}\,d\nu_f(y).
$$

raw pull 的 Amice 测度准确是 $[\pi]_*\nu_{f_0}$，乘 $\pi$ 保持完整单位域。因此

$$
\mathcal L_p^{\rm ord}(\mathcal X_{130};v)
=\frac{\langle\pi\rangle^{(p-1)v}
       -\langle\bar\pi\rangle^{(p-1)v}}{2520\delta}
        \mathcal L_p^{\rm ord}(f_0;v).
\tag{20}
$$

由(19)，右边两个因子在零处都消失，故其第一导数在这个同一原射线上准确为零。这里不将 whole degree10 scalar 推广到任意其它普通素数或其它半特征。

返回共同 $b=17$ 模型时，准确使用

$$
f_{0,b}(z)=b^{-1}f_{0,1}(\vartheta_bz),\qquad
\mathcal X_{130,b}(z)=b^{-1}\mathcal X_{130,1}(\vartheta_bz),
\quad\vartheta_b^6=b.
\tag{21}
$$

两个零身份继续准确成立。将(18)的非零导数表达为首六阶归一的 degree130 来源时，统一有 $b^{-1}$；不将质量一规范与(21)互换。

## 5. 保留两 old 块的完整 H/F11 真零

准确使用 R978 的两个完整 old 投影：

$$
H_- -\frac{11}{37800}F_{11,-}
 =\frac{\delta}{2721600}\Delta_-,\qquad
H_+ -\frac{11}{23625}F_{11,+}
 =\frac{\delta}{1701000}\Delta_+.
\tag{22}
$$

将第一式乘 $8/5$ 后从第二式相减。因

$$
\frac85\frac{11}{37800}=\frac{11}{23625},\qquad
\frac85\frac{\delta}{2721600}=\frac{\delta}{1701000},
$$

这些完整原函数满足

$$
\boxed{
H_+-\frac85H_-
-\frac{11}{23625}(F_{11,+}-F_{11,-})
=-\frac2{25}\mathcal X_{130}.}
\tag{23}
$$

最后的常数由 $\Delta_+-\Delta_-=45360\delta\mathcal X_{130}$ 和 $\delta^2=-3$ 得到。式(23)是 whole 身份，已经消去全部函数系数；它的中央导数由(17)、(20)在各自准确范围内为零。

在所显示投影之外，$H,F_{11}$ 的全部非 $\mu_6$ 块、其它 primitive 块及原完整 mixed 测试仍保留。没有给全 $H$、全 $F_{11}$ 或 $F_{10}$ 的导数赋零。

### 5.1 这条真零线的实际好位 Hecke 像却中央非零

新零关系有一个可明确核定的边界。R976 固定两个 old 块的 good7 本征值分别为 $-\omega,-\omega^2$。因此

$$
\boxed{(N_7+\omega^2)\mathcal X_{130}
=\frac{\Delta_-}{45360}
=-\frac{\delta}{27}(2F_{10}+11\Phi_*).}
\tag{24}
$$

在惰性读者下得到

$$
\boxed{J'_{N_7\mathcal X,p}(0)
=\frac{p+1}{45360}\log_p(\pi/\bar\pi)\ne0.}
\tag{25}
$$

在原普通射线上，对应指数为 $(p-1)v$ 的导数是

$$
\frac{p-1}{45360}(1-\upsilon_p)\log_p(\pi/\bar\pi)\ne0.
\tag{26}
$$

式(25)–(26)不使用 $\Phi_*$ 的失败假设，回共同 $b=17$ 模型时各除以17。所以(17)/(20)是一个指定的真来源关系，其实际 good7 Hecke 像并不继承这个零。

## 6. 第十一行仍使用同一完整六位输入

新来源的 charge 为65，与 $\Phi_*,\Phi_{260}$ 相同。保持 R989 的全部原记号，

$$
q_{\mathcal X}=65/17,\qquad
B_{\mathcal X}
=w^{-1}\mathcal X_{130}e^{-q_{\mathcal X}\kappa w^s}
=f^{-65}\sum_{j=0}^{20}\widetilde b_jw^jW^{62-3j},
\quad\widetilde b_0=1.
\tag{27}
$$

所有 $W$ 幂均至少为二，固定系数在(11)之外整。因此 R989 的整个 Hurwitz 证明、$h=7,8$ 的整端点和全部 $h\ge9$ 尾，以相同半径及费用适用于(27)。特别，同一 $W,f$ 到 $w^p$ 的输入及相同两次真实除 $p$ 已足够，最高输入仍是 $6s-1=p$。

对同样五个原高轴 $x$，定义

$$
C_{\mathcal X,h}(x)
=[w^{hs-1}]B_{\mathcal X}e^{q_{\mathcal X}\eta_x},
$$

$$
F_{\mathcal X}^{[6]}(x)
=\sum_{h=1}^6
\frac{(-1)^{h-1}(h-1)!p^{h-1}}
 {q_{\mathcal X}^{h}a^{h-1}}C_{\mathcal X,h}(x).
\tag{28}
$$

其完整误差与 R989 相同：

$$
F_{\mathcal X}^{[6]}(x)
\equiv\frac ap J'_{\mathcal X}(x;0)\pmod{p^6}.
\tag{29}
$$

在实际点 $x=0$，(17)无条件给 $F_{\mathcal X}^{[6]}(0)=0\pmod{p^6}$。若前五条 canonical 中央导数同时失败，其唯一必要点 $x^{\dagger,[6]}$ 就是模 $p^6$ 的实际点。因此新增的真正必要行是

$$
\boxed{\mathfrak r_{\mathcal X|5,p}^{[6]}
:=F_{\mathcal X}^{[6]}(x^{\dagger,[6]})=0\pmod{p^6}.}
\tag{30}
$$

对旧五位点的任意整提升 $x_5$，第六位提升仍可完整消去。令 $b_{\mathcal X}$ 是按原行序排列的前五个实际来源系数，$c_{\mathcal X}=b_{\mathcal X}B_5^{-1}$，则

$$
\boxed{\mathfrak r_{\mathcal X|5,p}^{[6]}
=F_{\mathcal X}^{[6]}(x_5)
-c_{\mathcal X}F_{\mathrm{old5}}^{[6]}(x_5)\pmod{p^6}.}
\tag{31}
$$

右侧的原五项仍须准确读到第六位。完整 $t\to w$ 三角、全部来源列及 $\Gamma_L^{(6)}$ 的每个有序前缀均保持。这新增一个来源行，不增加第七长块或扩大 $L<p$ 窗。

这个 whole 来源与原十条在 $\mathbf Q$ 上线性独立。在 degree130 内，它是两个 old 块中的非零向量，$\Phi_*,\Phi_{260}$ 则在两个 primitive 线上。不同 degree 不能在有限 whole theta 关系中相消：在原 CM frame 沿固定非零周期的整数倍平移，最高 degree 的二次指数增长严格最快，其 whole 系数只能为零，再按 degree 下降。这里准周期满足 $\eta_\lambda\lambda>0$，由 R966 的原 CM 规范可直接核定。原十条自身独立已由 R982 证明。这个论证不声称前十一个低 jet 满秩，也不声称(31)已在无穷素数非零。

## 7. 新真零加入后的准确四维十三边界

本节消费 R993 已返回的实际常数，不新增数学执行。对两个核置

$$
K_\pi=K[X]/(R_\pi),\qquad K_{\bar\pi}=K[X]/(\bar R_\pi).
$$

对完整 degree130 principal 来源 $f$，以 $m_\pi(f)\in K_\pi$、$m_{\bar\pi}(f)\in K_{\bar\pi}$ 表示 R987/R993 同一规范下的两个非零六点轨道 canonical 平移质量，二次迹记为 $t_\pi(f),t_{\bar\pi}(f)$。若 $f=\sigma^{130}x^2P_f(X)$，准确读法为

$$
m_\pi(f)=\frac{P_f(X)}{6^{10}X^6(X+1)^5R_\pi'(X)^{10}}
\quad\text{于 }K_\pi,
$$

共轭核同理。这里保整条二次商，没有只读一个根；全部映射都在原 whole 来源空间上线性。

### 7.1 整个已返回矩阵固定第二个 level10 norm13 本征值

在原有序基 $(\sigma^{10}x^2,\sigma^{10}x^5)$ 上，R987 返回的整个 norm13 矩阵是

$$
\boxed{
N_\pi=
\begin{pmatrix}1/3&20/3\\1/12&1/6\end{pmatrix}
+\delta\begin{pmatrix}-2/9&20/9\\1/36&-5/18\end{pmatrix}.}
\tag{32}
$$

其原 serialization 的 SHA-256 为
`064f23e1b663c72059c80997ef086e10e55b16583a29a52702fc6ae8c73731be`，准确等于 R987 和 R993 同次执行的整个矩阵哈希。直接回乘得

$$
N_\pi(-8,1)^t=\omega^2(-8,1)^t,
\qquad N_\pi(10,1)^t=(10,1)^t.
\tag{33}
$$

所以两个真实 good13 标量为 $\theta_{125}=\omega^2\pi$、$\theta_{12500}=\pi$。它们也有独立的有限角色证明：sextic twist 比为100；在 $\pi$ 处，$\delta=6$、$\omega=9\in\mathbf F_{13}$，且 $100^2=3=\omega^2$。原 inverse-twist 约定遂将第一个 normalized 本征值 $\omega^2$ 变为1。这两个已识别的来源构成完整 level10 基，故相应本征身份亦唯一确定(32)，不依赖哈希论证其数学唯一性。没有用点数猜本征线。

完整投影身份是

$$
Q_\pi D_{\bar\pi}
=\frac\pi{13}D_\pi N_\pi
\quad\text{on the complete level10 space}.
\tag{34}
$$

由(3)、(33)及(2)的两来源质量均为一，得到

$$
(Q_\pi\mathcal X_{130})(0)
=-\frac{\pi(1-\omega^2)}{13\cdot18\cdot2520\delta}.
$$

每个非零轨道有六个点，且 $\mathcal X_{130}(0)=0$，所以 $t_\pi=(13/6)(Q_\pi\mathcal X_{130})(0)$。又 $1-\omega^2=-\delta\omega$，故

$$
\boxed{t_\pi(\mathcal X_{130})=\frac{\pi\omega}{272160}
=\frac{-5+3\delta}{544320},\qquad
t_{\bar\pi}(\mathcal X_{130})=\frac{\bar\pi\omega^2}{272160}.}
\tag{35}
$$

还可完整写出新第三列，而不止读其迹：

$$
\boxed{m_\pi(\mathcal X_{130})
=\frac{\pi(X-8)}{3265920\delta}\quad\text{于 }K_\pi,
\qquad
m_{\bar\pi}(\mathcal X_{130})
=-\frac{\bar\pi(X-8)}{3265920\delta}\quad\text{于 }K_{\bar\pi}.}
\tag{35a}
$$

证明如下。在 $\ker\pi\setminus\{0\}$，$\bar\pi T=7T$；$7$ 是 $\mathbf F_{13}^\times$ 的非平方，所以交换两个六点轨道，给
$X(\bar\pi T)=-(2+6\delta)-X(T)$。R987 的原局部三维空间和质量规范给非零核点上的
$m_\pi(D_{\bar\pi}\Psi_-)=(\omega^2\pi-1)/12=\omega^2/3$；而 $m_\pi(D_\pi f_0)=f_0(0)=0$。
因此(3)的实际函数比给

$$
m_\pi(\mathcal X_{130})
=\frac{\omega^2}{7560\delta\,(X+10+6\delta)}.
$$

在完整二次商中直接有
$(X-8)(X+10+6\delta)=432\omega^2/\pi$，故得(35a)。共轭式按 $\mathcal X_{130}$ 的有理系数得到。
又 $N_{K_\pi/K}(X-8)=R_\pi(8)=216(5+3\delta)/13$、$N_{K/\mathbf Q}(5+3\delta)=52$，所以(35a)在当前 $p>211$ 的每个轨道均为单位；没有新增未付的根或相位。

### 7.2 三条真零方向与第四条非零对照

置

$$
G_{\rm old}=\Delta_-+21840\delta\Phi_*
=3360\delta(\Phi_*-F_{10}).
\tag{36}
$$

这是 R993 的实际同 degree、至少十二阶的来源。其完整回执给二次迹

$$
t_\pi(G_{\rm old})=2\pi/3,
\qquad t_{\bar\pi}(G_{\rm old})=-2\bar\pi/3.
\tag{37}
$$

两条 primitive 来源在每个核上的迹均为零。在迹零基
$e_\pi=X+1+3\delta$、$e_{\bar\pi}=X+1-3\delta$ 中，R993 给

$$
m_\pi(\Phi_*)=\beta e_\pi,\quad
m_{\bar\pi}(\Phi_*)=\bar\beta e_{\bar\pi},\qquad
\beta=-\frac{1+2\delta}{997920},
$$

$$
m_\pi(\Phi_{260})=\rho_\pi\beta e_\pi,\quad
m_{\bar\pi}(\Phi_{260})=\rho_{\bar\pi}\bar\beta e_{\bar\pi},
$$

$$
\boxed{\rho_\pi=-\frac{11(1+\delta)}{40},\qquad
\rho_{\bar\pi}=-\frac{11(1-\delta)}{40}.}
\tag{38}
$$

由 $\rho_{\bar\pi}-\rho_\pi=11\delta/20\ne0$，它们张成两条迹零方向。式(35)、(37)给余下行列式

$$
\boxed{
t_\pi(\mathcal X)t_{\bar\pi}(G_{\rm old})
-t_{\bar\pi}(\mathcal X)t_\pi(G_{\rm old})
=\frac{13}{408240}\ne0.}
\tag{39}
$$

所以在有序边界基 $(e_\pi,e_{\bar\pi},1_\pi,1_{\bar\pi})$ 下，四个来源列 $(\Phi_*,\Phi_{260},\mathcal X_{130},G_{\rm old})$ 的行列式是

$$
\boxed{
\beta\bar\beta(\rho_{\bar\pi}-\rho_\pi)
\frac{13}{4\cdot408240}
=\frac{1859\delta}{32659200\cdot997920^2}\ne0.}
\tag{40}
$$

其分子、分母只含 $2,3,5,7,11,13$，故在全部当前 $p>211$ 都是单位。加入 $\mathcal X_{130}$ 因而给第三条独立的实际边界行。在两条 canonical 中央失败的假设下，这三条来源的中央导数确实全为零；而(18)、(36)给 $G_{\rm old}$ 在惰性读者中的导数为明确非零的 $d\log_p(\pi/\bar\pi)$，普通原射线另保原单位质量因子。

剩下的一条边界余向量也可准确指定。置

$$
\mathscr R_\partial(f)
=\bar\pi\omega^2 t_\pi(f)-\pi\omega t_{\bar\pi}(f).
\tag{41}
$$

它杀掉 $\Phi_*,\Phi_{260},\mathcal X_{130}$，并将 $G_{\rm old}$ 送到 $-26/3$。因此，在这些原来源的实际四维张成空间上，两 canonical 失败强制整个惰性中央泛函为

$$
\boxed{
J'_{f,p}(0)
=-\frac3{26}(p+1)\log_p(\pi/\bar\pi)
                \mathscr R_\partial(f).}
\tag{42}
$$

证明是在这全部四个基向量上准确相等，没有将整个22维空间的 whole Cartier 泛函替换为零阶边界。原普通射线版本将 $(p+1)$ 改为 $(p-1)(1-\upsilon_p)$；共同 $b=17$ 版本在本节固定的 $b=1$ 坐标中另有统一 $17^{-1}$。

## 8. 新行已经消费的范围与仍须保持的全余项

式(17)、(20)、(23)是带固定完整来源及同一 R989 六位误差的真中央零输入，实际 old 非零方向仍在。式(35)–(42)指定了加入这条真零以后尚余的一条边界方向。

原平移有理模型仍有整个共同因子

$$
\left(P_2(P)^{65}a_T(P)^{10}-P_2(P+T)^{65}\right)R_f(P+T),
\qquad
a_T(P)=\frac{R_\pi(X(P))}{R_\pi(X(P+T))}.
\tag{43}
$$

在两个六点轨道上的零阶权仍准确是 R993 保留的
$D_T=1-P_2(T)^{65}(D R_\pi(T))^{10}$。
实际差 $\Phi_{260}-\rho_\pi\Phi_*$ 及其共轭分别只有一次 $R_\pi$ 或 $\bar R_\pi$ 因子，已返回的首除商非零。所以(40)不消去(43)的高阶导数，不能仅凭质量零判定其完整 Cartier 值。$Z$ 的移动零除子及二挠贡献仍在全局读者中。

后继实际比较可直接使用唯一指定方向(41)、第十一真行(31)和非零值(25)，无需新增素数扫描或将 old primitive 改成秩二曲线。本篇尚未证明固定曲线、无穷素数的 Sha 主目标。

## 依赖与真实回执

- R968：whole even degree10 scalar 与原普通射线。
- R978：两条完整 raw norm13 拉回、两个实际质量一来源及全部 $H/F_{11}$ old 系数。
- R976：两个 old 块的实际 good7 本征值。
- R987：canonical13 lift、完整 level10 norm13 规范及(32)的原全矩阵哈希。
- R989：同一六位输入和整个无限尾；(27)逐项核新来源的适用条件。
- R993：source `4d1a123b11a4161bdd4e4592eb145ff163d65a38`、run `45903334519`、job `140194103108` 的实际两核规约；两个原矩阵哈希和所有旧门都保留。式(36)–(43)消费其准确 $\rho,\beta$、old 迹及首除商。

以上新来源、whole 身份、中央零及行列式均由所显示公式证明，不需新增数学执行。(32)手写矩阵的 serialization 与原回执哈希比对只是静态文本核对。仓库不新增生成系数或矩阵文件。
