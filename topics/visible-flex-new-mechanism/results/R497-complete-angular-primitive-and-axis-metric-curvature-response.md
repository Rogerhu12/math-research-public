# R497 — 完整角原函数下的新九列轴上度量与曲率响应

## 0. 结论与准确范围

本稿从原完整场的角原函数直接证明：新增八个正弦 body 方向在反射轴上取零，并不意味着它们对轴上的重建度量一阶无响应。它们准确保持的是若干**局部切向场 jet**；重建位置的一阶、二阶径向 jet 还含整个角圈的原函数，不能由单个角点的零值删去。

特别地，即使某点满足 $f=X_s\cdot T=0$，原度量误差 $\eta$ 仍可经这八列的一阶 $e=|X_s|^2-1$ 变化而改变。只有本文给出的八条实际积分投影同时为零，才能在该点声称“度量一阶只剩高度列”。

同时给出：

- 任意原背景上，九列在轴上保持及不保持的完整 jet 清单；
- 圆背景上的两个显式非零响应公式，包含正确的 $2j$ 因子；
- 原**实际第一基本形式**下的完整曲率变分公式；
- 一个仅限圆背景的一阶构造：用四个正弦模式分别控制两个轴类的角向正常曲率，同时使全部轴上的位置、径向一阶及二阶 jet 的一阶变化为零。

这不是对已冻结第 $55$ 点的新计算，不断言其峰位置、八列秩、下降方向或全网可达性。全文没有执行数值、符号程序、Jacobian、优化或开发检查。原研究程序在另一个已授权任务中执行，其结果不作为本文假设。

原来源为 [R490](R490-fixed-metric-intrinsic-curvature-bound-and-a-nested-complete-body-extension.md) 及 source commit $\mathtt{09f498cac5d2fad47a35f007b68fe66218420d98}$ 中：

1. [完整 168 场](../scripts/frame_complete_body_extension168.py) 的 scalar_frame、geometry；
2. [原 frame 与角原函数](../scripts/frame_collar_bvp.py) 的 target_frame、periodic_operator；
3. [原度量值](../scripts/frame_metric_epigraph.py) 的 geometry_values；
4. [原两 spectral 分支](../scripts/frame_metric_affine_spectral_model.py) 的 phi、phi_gradient；
5. [原实际度量曲率](../scripts/frame_curvature_psd.py) 的 curvature_values、independent_principal_curvatures。

## 1. 完整场、原角锚与九列

使用原物理径向坐标 $s$，固定正函数 $a(s)$。令

$$
\psi=\theta+u,\qquad
N=(\cos\psi,\sin\psi,0),\qquad
H=(-\sin\psi,\cos\psi,0),\qquad e_3=(0,0,1),
$$

$$
c=(1+v^2)^{-1/2},\qquad
T=cH+vc\,e_3.
\tag{1}
$$

这里 $T$ 为原重建角切向量，严格满足 $|T|=1$。原辅助 frame 的 $\beta$ 不进入此式；它不能替代独立高度控制。

记 $\Pi$ 为原零均值周期角原函数：

$$
\widehat{\Pi F}(k)=
\begin{cases}
(ik)^{-1}\widehat F(k),&k\ne0,\\
0,&k=0.
\end{cases}
\tag{2}
$$

连续物理定义与已发布 Fourier 实现均使用这个锚。对原合法零均值切向场，$\partial_\theta\Pi T=T$。径向和参数微分与 $\Pi$ 交换。以下任何公式都不把 $\Pi F(\theta_0)$ 换成 $F(\theta_0)$ 的函数。

令 $z_s=b$，其中 $z,b$ 已包含原固定参考、旧五高度控制及当前新增高度。完整重建六 jet 为

$$
\begin{aligned}
X&=a\Pi T+ze_3,\\
X_s&=a_s\Pi T+a\Pi T_s+be_3,\\
X_{ss}&=a_{ss}\Pi T+2a_s\Pi T_s+a\Pi T_{ss}+b_s e_3,\\
X_\theta&=aT,\\
X_{s\theta}&=a_sT+aT_s,\\
X_{\theta\theta}&=aT_\theta.
\end{aligned}
\tag{3}
$$

这正是原 ordinary 的六 jet；不是只取局部 frame 的近似。

R490 的新九列使用

$$
\ell=\frac{81}{100},\qquad
\xi=\frac{s-9/250}{\ell},\qquad
P_m(\xi)=
\begin{cases}
\xi^m\exp[-\xi/(1-\xi)],&0<\xi<1,\\
0,&\text{其余}.
\end{cases}
$$

设 $P=P_5(\xi)$、$Q=P_8(\xi)$、$W=\ell P_8(\xi)$。增量为

$$
\Delta u=P\sum_{j=1}^4\alpha_j\sin(2j\theta),\qquad
\Delta v=Q\sum_{j=1}^4\beta_j\sin(2j\theta),\qquad
\Delta z=\gamma W.
\tag{4}
$$

所以 $\Delta b=\gamma W_s=\gamma P_{8,\xi}$、
$\Delta b_s=\gamma W_{ss}=\gamma P_{8,\xi\xi}/\ell$。
本文的径向下标始终是物理 $s$ 导数；没有遗漏 $\ell$ 的缩放。

R490 已付 $P_5$ 左零延拓 $C^4$、$P_8$ 左零延拓 $C^7$，右端全平，且全部所需六 jet 连续。本稿只使用这些已付阶数，不把左端改称全平或 $C^\infty$。

## 2. 在轴上准确保持哪些量

固定

$$
\theta_k=\frac{k\pi}{2},\qquad k\in\mathbb Z.
$$

因 $\sin(2j\theta_k)=0$，对任意有限新系数而不只是无穷小增量，

$$
\Delta u=\Delta v=\Delta u_s=\Delta v_s
=\Delta u_{ss}=\Delta v_{ss}=0
\quad\text{于 }\theta_k.
\tag{5}
$$

式 (1) 及其径向导数立即给

$$
\Delta T=\Delta T_s=\Delta T_{ss}=0,\qquad
\Delta X_\theta=\Delta X_{s\theta}=0
\quad\text{于 }\theta_k.
\tag{6}
$$

这些结论不要求原 $u,v$ 在轴上为零。高度列也不改变这些量。

另一方面，

$$
T_u=-cN,\qquad T_v=c^3(e_3-vH),\qquad
T_\theta=(1+u_\theta)T_u+v_\theta T_v.
\tag{7}
$$

在轴上 $T_u,T_v$ 的值未变，而

$$
\Delta T_\theta
=P\,A_kT_u+Q\,B_kT_v,
$$

$$
A_k=\sum_{j=1}^4 2j\,\alpha_j(-1)^{jk},\qquad
B_k=\sum_{j=1}^4 2j\,\beta_j(-1)^{jk}.
\tag{8}
$$

因此 $\Delta X_{\theta\theta}=a\,\Delta T_\theta$ 一般不为零。这也是轴上一个**有限增量的准确公式**。

两类 jet 的边界如下。

| 轴上量 | 新九列的准确结论 |
|---|---|
| $T,T_s,T_{ss}$ | 任意有限新系数均不变 |
| $X_\theta,X_{s\theta}$ | 任意有限新系数均不变 |
| $T_\theta,X_{\theta\theta}$ | 按 (8) 改变，一般不为零 |
| $X,X_s,X_{ss}$ | 含 $\Pi T,\Pi T_s,\Pi T_{ss}$，不能由 (5) 断言不变 |
| 诱导角度量 $|X_\theta|^2$ | 在全圈均为原 $a^2$ |
| 诱导径向及混合度量 | 须用完整 $X_s$ 判断 |

特别是，原目标 $g=ds^2+a^2d\theta^2$ 未变，不意味着重建诱导度量已经等于 $g$。

## 3. 原度量的准确一阶条件

在任意原背景和固定方向上用圆点表示参数一阶导数。由 (1)，

$$
\dot T=T_u\dot u+T_v\dot v.
$$

记

$$
Z=\Pi\dot T,\qquad
A=\partial_s(aZ)+\dot b\,e_3,\qquad
B=\partial_s^2(aZ)+\dot b_s e_3.
\tag{9}
$$

式 (3) 给 $\dot X_s=A$、$\dot X_{ss}=B$。尽管 $\dot T,\dot T_s,\dot T_{ss}$ 在轴上逐点为零，式 (9) 一般不为零。

令 $U=X_s$，原两度量量为

$$
e=|U|^2-1,\qquad f=U\cdot T.
$$

在轴上，完整一阶式是

$$
\dot e=2U\cdot A,\qquad
\dot f=T\cdot A,
\tag{10}
$$

第二式使用 $\dot T=0$，未删除任何角原函数。

对第 $j$ 个 $u$ 或 $v$ 列，令其真实完整 $\dot T$ 分别为 $\dot T_{u,j},\dot T_{v,j}$。在一个给定轴点，八列对 $e$ 全部一阶为零的充要条件恰是

$$
U\cdot\partial_s(a\Pi\dot T_{u,j})=0,\qquad
U\cdot\partial_s(a\Pi\dot T_{v,j})=0,
\qquad 1\le j\le4.
\tag{11}
$$

这是八条实际积分投影，不是 $\sin(2j\theta_k)=0$ 的推论。

原不平滑度量误差为

$$
\eta(e,f)=\frac{|e|+\sqrt{e^2+4f^2}}2.
\tag{12}
$$

在 $f=0,e\ne0$ 时，

$$
\dot\eta=\operatorname{sgn}(e)\dot e.
\tag{13}
$$

故在这一准确范围内，“八列对 $\eta$ 全盲”与 (11) 等价。在 $e=f=0$ 时不能套用可微公式；其单向导数为

$$
D\eta(0,0)[\dot e,\dot f]
=\frac{|\dot e|+\sqrt{\dot e^2+4\dot f^2}}2.
\tag{14}
$$

只有 $\dot e=\dot f=0$ 才为零。

原有限模型的两个平滑 spectral 分支则是

$$
\phi_\pm(e,f)
=\frac{\pm e+\sqrt{e^2+4f^2+\epsilon^2}}2,\qquad \epsilon>0.
$$

在 $f=0$ 时，

$$
\dot\phi_\pm
=\frac12\left(\pm1+
\frac{e}{\sqrt{e^2+\epsilon^2}}\right)\dot e.
\tag{15}
$$

这里 $\dot f$ 的系数确为零，但 $\dot e$ 中的 $\Pi$ 仍完整存在。原代码 group $0$ 是 $+$ 分支，group $1$ 是 $-$ 分支；(15) 不改变原 row 身份。

## 4. 圆背景给出的显式非盲式

本节只取一个明确的局部背景 $u=v=0$，不声称当前第 $55$ 点满足它。在此

$$
N=(\cos\theta,\sin\theta,0),\qquad
H=(-\sin\theta,\cos\theta,0),\qquad
T=H,\qquad \Pi T=N,
$$

$$
U=a_sN+be_3,\qquad e=a_s^2+b^2-1,\qquad f=0.
\tag{16}
$$

取 $n=2j\ge2$。对一个 $u$ 方向 $\dot u=P\sin(n\theta)$，有
$\dot T=-P\sin(n\theta)N$。直接三角展开给完整零均值原函数

$$
\Pi[-P\sin(n\theta)N]
=\frac{P}{n^2-1}
\{n\cos(n\theta)N-\sin(n\theta)H\}.
\tag{17}
$$

可直接求导验证右侧的角导数为左侧；其频率仅为 $n-1,n+1$，均非零，故没有隐藏常数锚。

由 (9)、(16)、(17)，

$$
\boxed{\quad
\dot e_{u,j}(s,\theta_k)
=\frac{4j}{4j^2-1}\,
a_s(s)\,(aP)_s(s)\,(-1)^{jk}.
\quad}
\tag{18}
$$

分子 $4j$ 来自原函数的径向分量 $n/(n^2-1)$，不能换成 $2/(4j^2-1)$。

对一个 $v$ 方向 $\dot v=Q\sin(n\theta)$，有

$$
\dot T=Q\sin(n\theta)e_3,\qquad
\Pi\dot T=-\frac Qn\cos(n\theta)e_3,
$$

于是

$$
\boxed{\quad
\dot e_{v,j}(s,\theta_k)
=-\frac1j\,b(s)\,(aQ)_s(s)\,(-1)^{jk}.
\quad}
\tag{19}
$$

两种方向都满足 $\dot f(s,\theta_k)=0$。高度方向则给

$$
\dot e_\gamma(s,\theta_k)=2b(s)W_s(s).
\tag{20}
$$

所以即使 $f=0$，(18) 在 $a_s(aP)_s\ne0$ 时非零，(19) 在 $b(aQ)_s\ne0$ 时非零。某一特殊背景上其中的乘积可能为零，必须按其真实值判断；单凭正弦列的轴上零值无法推出八列同时无响应。

这些恒等只涉及频率至多 $9$。在原两网的 Fourier 原函数中，这些频率不触及 Nyquist，因而同一离散三角多项式恒等在精确算术中仍成立。此句不是对实际 binary64 $\pi$、三角函数或峰值的新增误差认证。

式 (17)—(19) 已由另一代理独立手拆三角项核对；核对范围只限本节公式，没有扩大为实际场的秩或可行性证明。

## 5. 完整曲率的一阶式

使用原曲率实现的缩放切基 $(\partial_s,a^{-1}\partial_\theta)$。其实际第一基本形式为

$$
I=\begin{pmatrix}|U|^2&U\cdot T\\U\cdot T&1\end{pmatrix}.
$$

假设该点确为浸入，令

$$
q=|U\times T|>0,\qquad
\nu=\frac{U\times T}{q},
$$

$$
II=\begin{pmatrix}
\nu\cdot X_{ss}&\nu\cdot X_{s\theta}/a\\
\nu\cdot X_{s\theta}/a&\nu\cdot T_\theta/a
\end{pmatrix}.
\tag{21}
$$

这是原 frame_curvature_psd 的实际 $I,II$，没有用目标单位矩阵代替 $I$。

在轴上由 $\dot T=\dot X_{s\theta}=0$，并沿用 (9)，有

$$
\dot\nu
=\frac{(1-\nu\nu^\top)(A\times T)}q,\qquad
\dot I=
\begin{pmatrix}
2U\cdot A&T\cdot A\\
T\cdot A&0
\end{pmatrix}.
\tag{22}
$$

令 $M=\dot T_\theta$，其准确值由 (8) 的一阶式给出。则

$$
\begin{aligned}
\dot{II}_{11}&=\nu\cdot B+\dot\nu\cdot X_{ss},\\
\dot{II}_{12}&=\dot\nu\cdot X_{s\theta}/a,\\
\dot{II}_{22}&=(\nu\cdot M+\dot\nu\cdot T_\theta)/a.
\end{aligned}
\tag{23}
$$

所以即使只考察轴上曲率，完整一阶响应一般同时依赖：

1. 局部角导数 $M$；
2. 由整个角圈原函数给出的 $A=\dot X_s$；
3. 同一原函数的二阶径向导数 $B=\dot X_{ss}$。

若 $S=I^{-1}II$，则

$$
\dot S=I^{-1}(\dot{II}-\dot I\,S).
\tag{24}
$$

对一个单主曲率 $\kappa$，取 $I$-归一的广义特征向量 $v$，其准确导数为

$$
\dot\kappa=v^\top(\dot{II}-\kappa\dot I)v.
\tag{25}
$$

重复特征值处应取相应有限维对称扰动的特征值；多个全网最大值并列时也不能只用一个点的导数代替完整最大值方向导数。

式 (22)—(25) 说明：局部 $\dot T_\theta$ 的存在并不独立决定实际曲率变化。只有先验证 $A,B$ 的真实条件，才可作相应简化。例如 $A=B=0$ 时，$\dot\nu=\dot I=0$，(23) 只留下角向一项。这是一个有条件的简化，不是八列的普遍性质。

## 6. 圆背景中可准确分开的轴值与角导控制

本节给一个纸面可闭的一阶构造，说明这些量在完整原函数中可以分开；范围仍严格限于 (16) 的圆背景。

令高度方向为零。对四个 $u$ 系数施加

$$
\sum_{j=1}^4\frac{2j\,\alpha_j}{4j^2-1}=0,\qquad
\sum_{j=1}^4\frac{(-1)^j2j\,\alpha_j}{4j^2-1}=0,
\tag{26}
$$

对四个 $v$ 系数施加

$$
\sum_{j=1}^4\frac{\beta_j}{2j}=0,\qquad
\sum_{j=1}^4\frac{(-1)^j\beta_j}{2j}=0.
\tag{27}
$$

由 (17) 及 $v$ 的原函数，(26)—(27) 正好令
$\Pi\dot T(\theta_k)=0$ 于所有轴。由于每一组模式使用同一个径向 $P$ 或 $Q$，这些等式对整个径向区间同时成立。因此

$$
\dot X=\dot X_s=\dot X_{ss}
=\dot X_\theta=\dot X_{s\theta}=0
\quad\text{于所有 }\theta_k.
\tag{28}
$$

但两个轴类的 $A_k,B_k$ 仍可任意指定。证明可按奇偶模式对拆开：

- $u$ 的 primitive 权与角导权之比是
  $$
  \frac{2j/(4j^2-1)}{2j}=\frac1{4j^2-1};
  $$
  在 $j=1,3$ 及 $j=2,4$ 各对内互不相同；
- $v$ 的对应比为
  $$
  \frac{1/(2j)}{2j}=\frac1{4j^2},
  $$
  在相同两对内也互不相同。

故每对的二乘二矩阵可逆。等价地，(26) 留下的两个 $u$ 方向满射至 $(A_0,A_1)$，(27) 留下的两个 $v$ 方向满射至 $(B_0,B_1)$。这里轴下标按模 $2$ 取类，不是逐点独立选成本。

在此背景令 $E=a_s^2+b^2>0$，选择原叉积定向

$$
\nu=\frac{-bN+a_se_3}{\sqrt E}.
$$

两坐标方向为主方向，角向正常曲率为
$\kappa_\theta=b/(a\sqrt E)$。由 (8)、(23)、(28)，

$$
\boxed{\qquad
\dot\kappa_{\theta,k}
=\frac{bP\,A_k+a_sQ\,B_k}{a\sqrt E},
\qquad
\dot\kappa_{s,k}=0.
\qquad}
\tag{29}
$$

在 body 开区间 $P,Q>0$，且 $E>0$ 使 $b,a_s$ 不同时为零。因此两个轴类的角向正常曲率的一阶变化可独立指定，同时全部轴上的一阶诱导度量保持。

这没有证明全圈等距变化：离开轴的度量一般改变。它也没有证明最大外曲率可下降，因为最大值可能位于别处，或由未改变的径向主曲率决定。对一般非圆背景，(26)—(29) 不可无验证搬用；必须回到 (9)、(22)、(23) 的真实原函数响应。

## 7. 对当前实际任务能与不能得出的结论

当前九维纤维保持旧 $159$ 个独立参数、固定 $g,b_0$ 和永久参考，新增列的完整身份仍是 R490 的 $168$ 独立、$172$ 物理系数族。本文不重新标识原 $163$ 家族，也不修改任何实际约束、池、预算或收据。

对冻结第 $55$ 点，本文现在支付的是正确判断接口：

- 若实际度量最大点恰位于上述轴且 $f=0,e\ne0$，八列是否一阶无响应应由 (11) 的真实值决定；
- 若还研究该点的曲率，则必须同时保留 (22)—(23) 中完整 $X_s,X_{ss}$ 的角积分记忆及实际第一基本形式；
- 若某些响应真的为零，这只是该背景与这些方向的事实，不能从本稿反例推出它们非零；
- 若响应非零，也不直接给出满足全部硬约束、比较已接受点并有规定下降量的实际新候选。

R490 的 intrinsic 必要界未阻断当前固定目标 $g$；本文同样没有把此必要界或圆背景的局部控制提升为全局外曲率、嵌入或 reach 存在证明。下一实际问题仍须使用同一真实点的完整响应和全部原门，但不能再用“角场在轴上取零”替代这些响应。
