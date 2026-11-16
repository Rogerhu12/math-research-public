# R521：完整有限 Frenet 的 tube 常数与 cubic 全单元残差构造

作者：exact_refinement（AI）；日期：2026-11-16。

**可信度：下文证明准确实有限参考上的条件不等式，并给出只用准确有理数和整数平方根的可调用 helper。没有执行新的科学计算，没有取得任何实际场的 Lipschitz 常数或误差 floor。** 该 helper 不修改原 solver、native、FD、full-DN、metric 或资源停止门，也没有建立新工作流。

[R514](R514-complete-field-defect-transport-and-literal-residual-transfer.md) 的式(514.16)含两个尚未实际形成的量：整闭单元 cubic 残差 $\eta_C$，以及 cubic 与当前 quintic 之间合法 tube 上的有限 RHS 常数 $K_N$。本文补的是它们的一条具体构造：**完整物理 Fourier 状态与准确 scalar 的四块常数，真实 cubic 导数的完整 Bernstein 界，及实际样点到整单元的填充距离估计。** numeric shadow、准确目标、FFT/归一化/投影形成差额仍显式存在。

R354 已证明一个已指定仿射方向上的速度二阶式；R314 已证明 literal root、因子、RK 与全行残差的条件后验传递。本文复用这些对象区别，不把它们重新命名为新结果。新增的四块常数对整个声明的状态 tube 统一，能直接进入 R514 的 $\eta_C$ 构造；这不要求证明完整 BVP 逆，也不自动支付 native 尾或全闭面的其它项。

## 521.1 准确参考、真实维度和取向

取完整 $M$ 模态物理系数

$$
y=(r_0,\ldots,r_M,t_1,\ldots,t_M,z_0,\ldots,z_M)
\in\mathbb R^{3M+2}.
$$

固定实际均匀角数 $N>4M$，频率 $\omega_j=2j$。准确三角合成为

$$
r=r_0+\sum_{j=1}^M r_j\cos(\omega_j\phi),\quad
t=\sum_{j=1}^M t_j\sin(\omega_j\phi),\quad
z=z_0+\sum_{j=1}^M z_j\cos(\omega_j\phi).
$$

原旋转坐标角 jet 是

$$
d=(r_\phi-t,\ t_\phi+r,\ z_\phi),\qquad
e=(r_{\phi\phi}-2t_\phi-r,\ t_{\phi\phi}+2r_\phi-t,\ z_{\phi\phi}).
\tag{521.1}
$$

这正是原 BatchedFFTFlow.synth_real 的完整线性对象。$N>4M$ 明确本 helper 使用的非 Nyquist 截断约定；它不是给原求解加一条新验收条件。原 $M=112,N=2048$ 是其一个已声明维度。真实动态 $M$ 可用同公式，但须先有该场自身完整来源和维度，不能用旧 112 个字零补成“已完成的新场”。

在一个固定准确目标、固定参数和固定根成员上写

$$
V_\sigma(d,e,A,\nu,\mu)=
\frac{\sigma\sqrt P\,C-\nu QB}{AW},
\quad
P=A^2\mu^2W-\nu^2Q^3,
\tag{521.2}
$$

其中 $Q=d\cdot d,\ C=d\times e,\ W=C\cdot C$，
$B=Qe-(d\cdot e)d$，$\sigma\in\{-1,1\}$ 在所用路径上固定。
在几何应用中 $\nu=A_x$。nominal scalar 返回的 ap 可以先作为独立输入；它与准确 $A_x$ 的差须在后文计入。

要求所有被比较的真实路径位于同一个有合法外包的 tube 中，且有

$$
0<A_-\le A\le A_+,\quad
0<\mu_-\le\mu\le\mu_+,\quad
|\nu|\le n,\quad
\|d\|_2\le D,\quad \|e\|_2\le E,\quad P\ge p_->0.
\tag{521.3}
$$

可另给 $W\ge w_-\ge0$。这些是完整路径/完整所需角的条件，不是若干角点最小值。一个凸盒全部合法是充分实现；也可保完整路径覆盖，不必把所有不相关盒端点强行解释成同一实际成员。不同根成员的参数沿 $x$ 不换选；统一界最后对原完整根族取外包。

由 R514 的已证恒等式，

$$
\|V_\sigma\|_2=\mu,\qquad
AW\ge d_-:=
\max\left(A_-w_-,\frac{p_-}{A_+\mu_+^2}\right)>0.
\tag{521.4}
$$

第二项来自 $P\le A^2\mu^2W=A\mu^2(AW)$。它不要求某个向量分量、$\nu$ 或独立 interval normal 分量隔零。$\sigma$ 取哪一支不改变下列绝对值常数；与原物理场的关系仍须按 R514 的实际取向/反射/径向方向固定，不能以任一方便支冒原 worker。

定义准确有限系数 RHS

$$
f_N(x,y)=\Pi_N
 V_\sigma(d(y),e(y),A(x),\nu(x),\mu(x)).
\tag{521.5}
$$

$\Pi_N$ 包括全部物理分量和两均值。非均值行的绝对权和至多 2，均值行至多 1。因此从每角三向量 Euclidean 范数到完整系数最大范数，可统一使用 $\pi_N=2$。这先定义准确三角/有限 DFT 参考；真实 FFT、字面三角表或 rounded matvec 是另外的形成对象。若要改成保存的 literal 矩阵，应使用它真实的合成/投影范数，不能无条件继承这里的 2。

## 521.2 全部合成行的显式范数

设 tube 内完整系数绝对值界为 $R_j,T_j,Z_j$。直接由(521.1)及 $|\sin|,|\cos|\le1$ 得

$$
\begin{aligned}
D_1&=\sum_{j=1}^M(\omega_jR_j+T_j),\\
D_2&=R_0+\sum_{j=1}^M(\omega_jT_j+R_j),\\
D_3&=\sum_{j=1}^M\omega_jZ_j,
\end{aligned}
\qquad
D=\sqrt{D_1^2+D_2^2+D_3^2},
\tag{521.6}
$$

$$
\begin{aligned}
E_1&=R_0+\sum_{j=1}^M[(\omega_j^2+1)R_j+2\omega_jT_j],\\
E_2&=\sum_{j=1}^M[(\omega_j^2+1)T_j+2\omega_jR_j],\\
E_3&=\sum_{j=1}^M\omega_j^2Z_j,
\end{aligned}
\qquad
E=\sqrt{E_1^2+E_2^2+E_3^2}.
\tag{521.7}
$$

以上包含每个实际频率，保 $r_0$ 对旋转角 jet 的作用。$z_0$ 的角导数确为零，但其状态、径向 RHS、残差和均值投影仍保留。

令 $S_1=\sum_j\omega_j,\ S_2=\sum_j\omega_j^2$。将所有系数方向的绝对值都置为 1，得到完整状态最大范数的两个可算算子界：

$$
L_d=\sqrt{(S_1+M)^2+(1+S_1+M)^2+S_1^2},
$$

$$
L_e=\sqrt{(1+S_2+M+2S_1)^2+(S_2+M+2S_1)^2+S_2^2}.
\tag{521.8}
$$

于是每角都有
$\|d(v)\|_2\le L_d\|v\|_\infty$、
$\|e(v)\|_2\le L_e\|v\|_\infty$。
实际逐角/逐行的受证范数可以更窄；本文不要求新增数值对拍，也不据粗界大小预判原问题失败。

**证明。** 每个分量都是明确的完整线性和。逐项用三角不等式给(521.6)—(521.7)，再对三分量取 Euclidean 范数。以单位方向的分量界 1 代入，同得(521.8)。有限最大值覆盖全部 $N$ 行；这里没有用“只看最坏角样本”替代所有行。

## 521.3 可直接形成的一、二阶 majorant

考虑任意 affine 输入路径，具有方向界

$$
\|\dot d\|_2\le u,\quad \|\dot e\|_2\le v,\quad
|\dot A|\le a,\quad|\dot\nu|\le b,\quad|\dot\mu|\le c.
\tag{521.9}
$$

其二阶输入导数为零。这里以 $J=(J_0,J_1,J_2)$ 表示值、一阶导数、二阶导数的非负上界，不是 Taylor 系数。两个对象的乘积使用

$$
(J\star K)_0=J_0K_0,\quad
(J\star K)_1=J_1K_0+J_0K_1,
$$

$$
(J\star K)_2=J_2K_0+2J_1K_1+J_0K_2.
\tag{521.10}
$$

此规则同样适用于 dot/cross 的范数上界。取

$$
q=(D^2,2Du,2u^2),\quad
c_*=(DE,uE+Dv,2uv),\quad w=c_*\star c_*,
$$

$$
b_*=(D^2E,\ 4DuE+2D^2v,\ 4u^2E+8Duv).
\tag{521.11}
$$

$q,c_*,w,b_*$ 分别包围 $Q,C,W,B$ 的三阶次。$b_{*,0}$ 用了 $\|B\|_2^2=QW$；其它两项是完整乘积法则的三角估计，未删交叉项。

再令

$$
\mathfrak a=(A_+,a,0),\quad
\mathfrak m=(\mu_+,c,0),\quad
\mathfrak n=(n,b,0),
$$

$$
p_j=[\mathfrak a^{\star2}\star\mathfrak m^{\star2}\star w]_j
+[\mathfrak n^{\star2}\star q^{\star3}]_j\quad(j=1,2),
$$

$$
t_*=\mathfrak n\star q\star b_*,
\qquad d_*=\mathfrak a\star w.
\tag{521.12}
$$

于是 $|P^{(j)}|\le p_j$。这是对相减的两部分分别取绝对上界，不用被减项来伪造更小导数。所有高次/混合项仍完整；原(521.2)的 $P$ 沿该输入路径次数至多八。

取准确有理数 $\ell>0$，使 $\ell\le\sqrt{p_-}$，并定义

$$
k_0=A_+\mu_+DE,\quad
k_1=\frac{p_1}{2\ell},\quad
k_2=\frac{p_2}{2\ell}+\frac{p_1^2}{4\ell^3},
$$

$$
u_1=k_1c_{*,0}+k_0c_{*,1}+t_{*,1},
$$

$$
u_2=k_2c_{*,0}+2k_1c_{*,1}+k_0c_{*,2}+t_{*,2}.
\tag{521.13}
$$

最后设

$$
\boxed{
\mathcal L(u,v,a,b,c)=
\frac{u_1+\mu_+d_{*,1}}{d_-},
\qquad
\mathcal H(u,v,a,b,c)=
\frac{u_2+\mu_+d_{*,2}
      +2\mathcal L(u,v,a,b,c)d_{*,1}}{d_-}.
}
\tag{521.14}
$$

**命题521-A。** 在完整(521.3) tube 内，沿每条上述 affine 路径，

$$
\|\dot V_\sigma\|_2\le\mathcal L,\qquad
\|\ddot V_\sigma\|_2\le\mathcal H .
\tag{521.15}
$$

**证明。** $Q$、$C$ 的前两次导数直接给(521.11)的前两对象。对
$B=Qe-(d\cdot e)d$ 两次求导，分别用 $\|\dot d\|\le u$、
$\|\dot e\|\le v$，得到 $4DuE+2D^2v$ 与
$4u^2E+8Duv$。所有其它多项式按(521.10)逐项相乘，即得(521.12)。

$K=\sqrt P$ 满足 R354 的
$K'=P'/(2K)$、
$K''=P''/(2K)-(P')^2/(4K^3)$；
$P\le A^2\mu^2W$ 给 $K\le k_0$，于是
$|K'|\le k_1,|K''|\le k_2$。
对 $U=\sigma KC-\nu QB$ 完整求导，得到(521.13)。

令 $D_{\rm den}=AW$。从 $D_{\rm den}V=U$ 得

$$
D_{\rm den}V'=U'-D_{\rm den}'V,\qquad
D_{\rm den}V''=U''-D_{\rm den}''V-2D_{\rm den}'V'.
$$

使用已证 $\|V\|_2=\mu\le\mu_+$ 与(521.4)，先包围 $V'$ 再包围 $V''$，即为(521.14)。这保留 R354 的全部导数项，只利用准确速度长度避免再用较粗的 $\|U\|/D_{\rm den}$ 上界。证毕。

该命题不声称这些上界窄或计算便宜；它消除了未指定的“存在某个 Lipschitz 常数”。$p_-$ 很小时常数可能很大，只能如实返回。

## 521.4 完整有限 RHS 的四块常数与状态二阶余项

用同一个 tube、同一全部角范围，定义

$$
\begin{aligned}
K_y&=2\mathcal L(L_d,L_e,0,0,0),\\
K_A&=2\mathcal L(0,0,1,0,0),\\
K_\nu&=2\mathcal L(0,0,0,1,0),\\
K_\mu&=2\mathcal L(0,0,0,0,1),\\
H_y&=2\mathcal H(L_d,L_e,0,0,0).
\end{aligned}
\tag{521.16}
$$

**定理521-B。** 若两个输入
$\zeta_i=(y_i,A_i,\nu_i,\mu_i)$ 之间的整条线段均在所声明合法 tube 中，则

$$
\|f_N(\zeta_1)-f_N(\zeta_0)\|_\infty
\le K_y\|y_1-y_0\|_\infty
 +K_A|A_1-A_0|+K_\nu|\nu_1-\nu_0|+K_\mu|\mu_1-\mu_0|.
\tag{521.17}
$$

固定 scalar 后，若 $y+\alpha v$、$0\le\alpha\le1$ 的整段也被覆盖，则

$$
\|f_N(y+v)-f_N(y)-D_yf_N(y)v\|_\infty
\le \frac{H_y}{2}\|v\|_\infty^2 .
\tag{521.18}
$$

**证明。** 命题521-A分别应用于四个输入块。合成(521.8)与全部投影行权给(521.16)，然后在线段上积分一阶导数，得到(521.17)；无须把变化拆成可能离开 tube 的四条坐标折线。状态二阶方向界对任意单位最大范数方向统一成立；缩放方向并用 Taylor 积分余项即得(521.18)。这里给的是 $D_y^2f_N[v,v]$ 的完整方向界，不声称已存储每个混合 Hessian 分量。证毕。

还总有全部系数 $|f_{N,j}|\le2\mu_+$，两个 mean 行可用 $\mu_+$。常数增广行的局部 RHS 为零时可继续保零；这不删除其真实边界、入口 core 注入或参数控制对物理 RHS 的作用。本文没有把这条 $3M+2$ 维物理定理冒成原 native 的 226 态/root 图或完整 453/450 BVP 逆结论。

## 521.5 真实 cubic 的完整导数界

在单元 $I=[x_0,x_1]$、$h=x_1-x_0>0$，选择**实际保存系数字词的准确提升**

$$
C(x)=\sum_{j=0}^3 c_j(x-x_0)^j,\qquad c_j\in\mathbb R^{3M+2}.
\tag{521.19}
$$

如果原存储为 SciPy PPoly 的降幂行，消费者只按原行定义倒序取得 $c_j$，不重新拟合曲线，不把另一套准确 Hermite 系数替代它。令 $a_j=h^jc_j$，则 $t=(x-x_0)/h$ 的完整 degree-3 Bernstein 系数为

$$
B_k=\sum_{j=0}^k
\frac{\binom{k}{j}}{\binom3j}a_j,\quad 0\le k\le3.
\tag{521.20}
$$

因此可直接取

$$
C_1=\max_{k=0,1,2}\left\|\frac3h(B_{k+1}-B_k)\right\|_\infty,
$$

$$
C_2=\max_{k=0,1}
\left\|\frac6{h^2}(B_{k+2}-2B_{k+1}+B_k)\right\|_\infty.
\tag{521.21}
$$

各分量 $\max_k|B_{k,j}|$ 也是该 cubic 的完整值界，供(521.6)—(521.7)使用。需覆盖 quintic、nominal采样输入或共同 scalar 路径时，必须扩大到它们的真实联合 tube；只有 cubic 的值界不自动覆盖那些其它状态。

**证明。** 单项式到同次数 Bernstein 的恒等式给(521.20)。Bernstein 基底非负且和为1；两次求导的差分公式给(521.21)。所有四行、全部 $3M+2$ 分量都保留，没有以端点/中点采样替代多项式闭域范围。

## 521.6 整闭单元残差的显式 Lipschitz 界

设准确 $A,\nu,\mu$ 在 $I$ 上连续，逐完整 scalar 分片 $C^1$，并有真实界

$$
|A'|\le a_x,\qquad|\nu'|\le n_x,\qquad|\mu'|\le m_x.
$$

所有分片与公共端点完整覆盖，且(521.3)覆盖 $C(x)$ 及所需比较路径。置

$$
r_C(x)=C'(x)-f_N(x,C(x)).
$$

**定理521-C。** 该残差在闭单元上 Lipschitz，且可取

$$
\boxed{
L_r=C_2+K_yC_1+K_Aa_x+K_\nu n_x+K_\mu m_x.
}
\tag{521.22}
$$

**证明。** 在每个光滑片内部按链式法则，

$$
r_C'=C''-D_yf_N\,C'
 -(\partial_Af_N)A'-(\partial_\nu f_N)\nu'
 -(\partial_\mu f_N)\mu'.
$$

使用(521.16)、(521.21)即得导数范数不超过 $L_r$。有限分片上积分并由同一准确 scalar/残差的公共端点连续性拼合，得到整个闭单元的 Lipschitz 界。若实际参考在某处有跳跃，应分开处理并显式加入跳跃量，不能照此连续性假设越过它。这里使用的角合成/投影与 $x$ 无关；若换成真正随 $x$ 变化的角表，还须保其导数项。

对准确前缀，已刊 R400/R514 的公共坐标关系为

$$
k=L_*/L_{\rm num},\quad
A(x)=a_*(kx;p),\quad \nu(x)=k\,a_{*,s}(kx;p),\quad\mu=k.
$$

在同一个根成员上 $k,p$ 固定，所以

$$
a_x\le k_+\,\sup|a_{*,s}|,\qquad
n_x\le k_+^2\,\sup|a_{*,ss}|,\qquad m_x=0.
\tag{521.23}
$$

这些三 jet 正是准确 target 的真实接口；必须枚举所有可能相交的 DAG piece、所有控制支撑和端点。R483/R492等来源只有在实际绑定后才可使用其真实范围。这里没有将 numeric length 等同准确 length，也没有改变 C/root 族。

尾部若用 $A=r,\mu=\sqrt{E_C(r)}$，则还需同一准确对象的
$\mu'=E_C'/(2\sqrt{E_C})$ 真实包围。本文没有绑定该尾部导数的实际读取，也没有把原 native literal 226 态问题改成(521.5)。该范围仍未付；它不阻止原 native 或直接 Gram 消费继续。

## 521.7 原数值样点到同一个准确残差

给定原实际样点 $x_i\in I$。设 $\widehat r_i$ 是所声明的原残差有限字向量，$b_i\ge\|\widehat r_i\|_\infty$；若原只有已经舍入的 norm 标量，不能未经形成界直接把它当 $b_i$。

设真实样点的 nominal 输入为
$\widehat\zeta_i=(\widehat y_i,\widehat A_i,\widehat\nu_i,\widehat\mu_i)$。
明确包围

$$
\|C(x_i)-\widehat y_i\|_\infty\le\epsilon_{y,i},\quad
|A(x_i)-\widehat A_i|\le\epsilon_{A,i},
$$

$$
|\nu(x_i)-\widehat\nu_i|\le\epsilon_{\nu,i},\quad
|\mu(x_i)-\widehat\mu_i|\le\epsilon_{\mu,i}.
\tag{521.24}
$$

另外 $\tau_i$ 包围原 C′求值、RHS形成、残差相减及必要 norm 形成的完整差额。例如若存储 $\widehat c_i',\widehat f_i,\widehat r_i$，可逐项包围

$$
(C'(x_i)-\widehat c_i')
+(\widehat c_i'-\widehat f_i-\widehat r_i)
+(\widehat f_i-f_N(\widehat\zeta_i)).
\tag{521.25}
$$

这包括真实 FFT/normal/平方根/有限投影与声明的准确参考之间的差；不是只读一次 old FD 就把它设零。然后(521.17)给出

$$
b_i^*=b_i+\tau_i+K_y\epsilon_{y,i}
+K_A\epsilon_{A,i}
+K_\nu\epsilon_{\nu,i}
+K_\mu\epsilon_{\mu,i}
\ \ge\ \|r_C(x_i)\|_\infty .
\tag{521.26}
$$

原 numerical flow 的 $\widehat\mu=1$ 与准确 $k$ 之差明确在最后一项。若 nominalscalar不由同一个准确根实现，不能冒称它是族内一员；应覆盖从这个 nominal 输入到每个声明准确成员的真实比较路径，或直接对准确目标评价残差。

将实际样点的不同位置排序为 $s_0<\cdots<s_q$，定义准确填充距离

$$
d_I=\max\left(s_0-x_0,\ x_1-s_q,\
\max_{j<q}\frac{s_{j+1}-s_j}{2}\right).
\tag{521.27}
$$

只有一个样点时删去最后的空最大值。所有位置取其真实准确坐标；不把打印近似当作另一个规则。

**定理521-D。** 若至少存在一个上述实际已包围样点，则

$$
\boxed{\quad
\eta_C=\max_i b_i^*+d_I L_r
\ \ge\ \sup_{x\in I}\|C'(x)-f_N(x,C(x))\|_\infty.
\quad}
\tag{521.28}
$$

**证明。** 每个 $x\in I$ 到一个实际样点的距离至多 $d_I$。用定理521-C的 Lipschitz 界，再用(521.26)，取最大值即得。无样点、样点未返、未包围形成差或未覆盖合法 tube 时，不能填 $\eta_C=0$。

原 c6a 的 frozen_physical_residual 使用实际 Lobatto 相对残差，并加 $.05$ 两端完整状态平方和。R514已证明：只有取得该**准确有限正权和**的上界及其形成差后，才能由 $R/\sqrt{w_i}$ 控制各样点归一残差。本文没有猜当前后端权、把 $10^{-6}$ 当准确 $R$，或把 normalised 数字直接填进(521.26)。若该前提真已付，(521.5)的 $|f_j|\le2\mu_+$ 可参与归一分母的还原；实际 rounded 分母和参考改变仍须在(521.25)中保留。

## 521.8 对 R514 的真实支付范围

取同一个准确 target、同一个完整 tube，并令 $Q_H$ 是当前保存的准确 quintic。若实际完整差满足

$$
\|Q_H-C\|_\infty\le E_0,\qquad
\|Q_H'-C'\|_\infty\le E_1,
$$

则 R514 的恒等式与(521.16)、(521.28)直接给

$$
\boxed{
\|Q_H'-f_N(x,Q_H)\|_\infty
\le \max_i b_i^*+d_I L_r+E_1+K_yE_0.
}
\tag{521.29}
$$

共享节点/斜率条件确实成立时可用原(514.14)—(514.15)；若实际 PPoly 系数与准确 Hermite 数据并非严格共享端点，改用两条实际多项式之差的完整 Bernstein 界，不能擅自删端点差。

这支付了“完整准确 finite-coefficient RHS 残差”的一个明确构造步骤。要传到整个闭场，原(514.18)仍必须保有限 N投影到连续角的差、完整材料映射、cut/patch/collar、真实 native重构、两反射和两帽；R514的径向锚及积分也没有由本式自动取得。更没有证明每次 mesh/M/t 加密必然使这些界严格下降，或得到机器精度/原 solver阈值的 metric floor。R459真实同目标上下界仍是独立可用的证据。

## 521.9 helper、真实输入和有限实现合同

新源 [geometry_20261116_finite_frenet_tube_residual_majorants.py](../computations/geometry_20261116_finite_frenet_tube_residual_majorants.py)，18782 B，SHA256 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad，实现上述全部非负 recurrence。它只依赖标准库 Fraction、comb、isqrt；拒绝 float，避免把十进制近似默当原 word。

正平方根采用相对 dyadic 网格：对 $x>0$ 选择整数 $k$ 使
$1\le x/2^{2k}<4$，令
$m=\lfloor2^b\sqrt{x/2^{2k}}\rfloor$，
则 $m2^{k-b}\le\sqrt x\le(m+1)2^{k-b}$。
整数平方判断能保准确端点；因 $m\ge2^b$，下端严格正，不会因绝对网格过粗把已证正下端舍为零。之后各乘加/除法均为准确有理运算。精度参数只影响外包宽度，不新增 solver 门。

| 函数 | 输入与结果 |
|---|---|
| fourier_synthesis_majorants | 全 $3M+2$ 系数绝对界、实际 $M,N$、sqrt_bits；返回(521.6)—(521.8)和完整投影范数 |
| frenet_directional_majorants | 完整 domain 与五个非负方向权；返回(521.14)和实际用到的正下端 |
| finite_rhs_majorants | 同域/同合成；返回四块 $K$、完整状态二阶方向界与 mean/非mean值界 |
| cubic_power_bounds | 四个真实 local-power行、准确端点、完整 $M$；返回(521.20)—(521.21) |
| closed_cell_residual | 上述常数、实际 cubic、三 scalar导数界、全部实际样点与形成/目标差额；返回(521.22)—(521.28)，无样点返回明确 unavailable/null |
| quintic_residual_transfer | 已绑定同 tube 的 $\eta_C,E_0,E_1,K_y$；返回(521.29) |
| scalar_necessary_summary | 必要标量和范围；不搬原四行系数、所有样点或全科学树 |

helper不读取或制造 checkpoint/receipt，不校验科学输入已被哪个 producer 严格证明，不执行 FFT、root、ODE或额外全域扫描。未来实际 caller 必须从既有同 job现场绑定真实数据和原 source，记录缺域/缺样点/预算未返；不能从已经清理的 SHA恢复原件。完整临时系数/逐样点记录仍按原生命周期保留，必要正文单90KB，不拆包或编码大表。

现阶段发布的是可调用的准确算术核与条件结果，没有将它暗接到任何正在运行的 workflow，也没有宣称任何实际 $\eta_C,K_y$ 已返回。接口见[参数与接点说明](../notes/2026-11-16-finite-frenet-tube-and-cell-residual-interface.md)。

## 来源与现有结论的边界

- [R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md)：20501 B / b6e293c20ffb6584f316b3e38877b7e3d4fb61cbad1f008718ab034f605cb183。其速度恒等式/指定方向二阶式在本文被明确复用。
- [R314](R314-verified-posteriori-bounds-for-literal-root-traces-and-directions.md)：26371 B / c2c94a1217c8e15782f2bd086c1f4a799637f3f283b42f2a1cfb601c82529ad2。该 literal root/因子/RK 后验责任不被本 Frenet 前缀核替代。
- [R514](R514-complete-field-defect-transport-and-literal-residual-transfer.md)：26256 B / e2bf21893c2448f4fa63f427ecc83df36e89c57dad2568bc732be92105fa76aa，main c09aaf9a6e1661efeacb34e4158f0322733bd2a9。
- [R519](R519-same-evaluation-sixjet-local-defects-and-metric-consumption.md)：12851 B / 9df3edb40c02d1c92ebf0aef75f840527852c29033b869e701d07414feb649e3，main 0bddd18b72e56337ee4ed6c55e19a6bedc5c06e2。它是同次六jet的直接可选诊断，不声称已构造本文的样点残差/完整 tube。
- [原 BatchedFFTFlow](../computations/geometry_20261114_r225_free_core_bvp.py)：23914 B / a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08。
- [原 full-DN frozen_physical_residual](../computations/geometry_20261114_full_dn_solve.py)：30017 B / c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162。
- [完整准确前缀 target](../computations/geometry_20261115_continuous_ten_frozen450_prefix_metric.py)：32761 B / 011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84。真实 accurate/numerical length 与完整 piece/support 枚举来自此类，而非旧 finite-Gauss接受标签。
