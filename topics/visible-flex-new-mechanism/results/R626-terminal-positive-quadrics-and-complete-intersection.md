# R626：真实尾二次型的准确可行阈值与双方交

2026-11-27。**已证明：R625 两条真实首层末二阶方程可准确写成两个严格正定二次型；
当末 $k\ne0$ 时，每一侧有一个显式、严格正的可行阈值。
两侧同时可行的完整问题进一步化为两个椭圆的交，等价于一个次数不超过4的实多项式加一个明确补点，含所有退化情形。**

这里“可行”只指相应末二阶方程。
单侧阈值不保证双方交，双方交不保证整段首层轨道，更不保证固定有限宽度原十九态 BVP 或主 README 完成。
全文为纸证，不启动科学求值，也不把新末加速度自由度加进原 BVP。

## 1. 保留 R625 的原末端与全部两侧平方

采用 [R625](R625-true-terminal-acceleration-and-tail-flat-compatible-input.md)
相同的条件：准确光滑首层轨道的末端假设

$$
A(L)=0,\qquad h_s(L)=k_s(L)=0,
\qquad C_1=0,
\qquad C_2<0,
$$
$$
h=h_L>0,\quad k=k_L\ne0,\quad d=h_L\eta_L-k_L,
\quad q_0=1+d^2,
\qquad C_0=-C_2h^2/q_0.
\tag{1}
$$

$a=h_{ss}(L),b=k_{ss}(L)$ 是待匹配的末几何 jets。
使用原 R598 六个不同参考位置 $c_i>0$ 和严格正权 $w_i$，不重选节点或权。
对 $\sigma\in\{+1,-1\}$ 设

$$
z_{\sigma i}=d+\sigma hc_i,
\qquad \omega_{\sigma i}=w_i(1+z_{\sigma i}^2)^3>0,
$$
$$
R(z)=(kz-1)(z+k).
\tag{2}
$$

R625 的完整两侧末方程是

$$
\sum_i\omega_{\sigma i}
\left[R(z_{\sigma i})+\frac ah(z_{\sigma i}+k)-\frac b2\right]^2
=\frac{16C_2h^7}{q_0}
  \left[a(1-dk)+\frac{hdb}{2}\right].
\tag{3}
$$

这些平方来自真 $A_s=M$ 的全部尾端贡献，不能把它们简化成只含显式速度导数的近似式。

## 2. 一个共同物理强度与每侧严格正定矩阵

引入可逆的末加速度坐标

$$
\xi=\begin{pmatrix}a/h\\-b/2\end{pmatrix},
\qquad u_{\sigma i}=\begin{pmatrix}z_{\sigma i}+k\\1\end{pmatrix},
\qquad e=\begin{pmatrix}1-dk\\-d\end{pmatrix},
$$
$$
\boxed{\tau=-\frac{16C_2h^8}{q_0}>0.}
\tag{4}
$$

$e\ne0$：若第二分量为零，则 $d=0$，第一分量为1。
方括号准确等于 $h e^T\xi$，所以 (3) 等价于

$$
\boxed{F_\sigma(\xi;\tau)=
\xi^TA_\sigma\xi+2m_\sigma^T\xi+c_\sigma
+\tau e^T\xi=0,}
\tag{5}
$$

其中所有系数都由同一真实末 $h,k,d$ 确定：

$$
A_\sigma=\sum_i\omega_{\sigma i}u_{\sigma i}u_{\sigma i}^T,
\quad
m_\sigma=\sum_i\omega_{\sigma i}R(z_{\sigma i})u_{\sigma i},
\quad
c_\sigma=\sum_i\omega_{\sigma i}R(z_{\sigma i})^2.
\tag{6}
$$

对任意非零 $v\in\mathbb R^2$，

$$
v^TA_\sigma v=\sum_i\omega_{\sigma i}
 [v_1(z_{\sigma i}+k)+v_2]^2>0.
$$

因为一个非零一次多项式至多在一个点为零，而 $h>0$ 使六个 $z_{\sigma i}$ 不同。
所以

$$
\boxed{A_\sigma\text{ 严格正定。}}
\tag{7}
$$

定义严格残差

$$
\delta_\sigma=c_\sigma-m_\sigma^TA_\sigma^{-1}m_\sigma.
\tag{8}
$$

它是带正权最小二乘值

$$
\delta_\sigma=\min_\xi
\sum_i\omega_{\sigma i}[R(z_{\sigma i})+u_{\sigma i}^T\xi]^2.
$$

若该值为0，首项系数为 $k\ne0$ 的二次多项式 $R(z)+\xi_1(z+k)+\xi_2$
会在六个不同点全为零，不可能。
故

$$
\boxed{\delta_\sigma>0\qquad(k\ne0).}
\tag{9}
$$

这是准确结构性结论，不把一个浮点最小特征值或 residual 提升为正定/严格正性的证书。

## 3. 单侧完整可行性与唯一正阈值

固定一侧，暂省下标。令

$$
\ell(\tau)=m+\frac\tau2e,
\qquad
\xi_c(\tau)=-A^{-1}\ell(\tau),
$$
$$
\mathcal R(\tau)=\ell(\tau)^TA^{-1}\ell(\tau)-c.
\tag{10}
$$

完成平方后，(5) 准确等价于

$$
\boxed{(\xi-\xi_c)^TA(\xi-\xi_c)=\mathcal R(\tau).}
\tag{11}
$$

因此 $\mathcal R<0$ 时无实解，$\mathcal R=0$ 时只有一点 $\xi_c$，
$\mathcal R>0$ 时是一条非退化椭圆。
定义

$$
\alpha=e^TA^{-1}e>0,\qquad
\beta=m^TA^{-1}e,
\qquad\delta=c-m^TA^{-1}m>0.
$$

展开 (10) 得

$$
\boxed{\mathcal R(\tau)=\frac\alpha4\tau^2+\beta\tau-\delta.}
\tag{12}
$$

它的两个根异号，因为 $\alpha>0,\delta>0$。
唯一正根是

$$
\boxed{\tau_{\rm crit}
=\frac{2(\sqrt{\beta^2+\alpha\delta}-\beta)}{\alpha}
=\frac{2\delta}{\sqrt{\beta^2+\alpha\delta}+\beta}>0.}
\tag{13}
$$

第二个分母严格正，因为 $\sqrt{\beta^2+\alpha\delta}>|\beta|$。
在 (1) 的 $\tau>0$ 范围内，得到完整的充要条件

$$
\boxed{\text{第 }\sigma\text{ 侧真实末二阶方程有实 }(a,b)
\iff \tau\ge\tau_{{\rm crit},\sigma}.}
\tag{14}
$$

因此双方同解必须满足

$$
\tau\ge\max(\tau_{{\rm crit},+},\tau_{{\rm crit},-}),
$$
$$
\boxed{C_2\le-\frac{q_0}{16h^8}
            \max(\tau_{{\rm crit},+},\tau_{{\rm crit},-}).}
\tag{15}
$$

(15) 只保证两侧各自非空，并不保证两个椭圆相交。
例如两个正半径椭圆可以分离或严格套住；下一节保留这项联合条件。

对于任意一侧的真正解，(5) 还给
$\tau e^T\xi=-\sum_i\omega_i[R(z_i)+u_i^T\xi]^2<0$，
严格性再次用 $k\ne0$。故 $h e^T\xi<0$，这正是 R625 的必要符号门。
这里该符号由完整单侧等式推出，不另作为代替等式的资格。

## 4. 双方同时成立：所有退化情形

取相同的 $\tau$，计算两侧 $\mathcal R_\pm$ 和 $\xi_{c,\pm}$。

若任一 $\mathcal R_\sigma<0$，双方同解集为空。
若 $\mathcal R_+=0$，则唯一可能点是 $\xi_{c,+}$，
它是双方同解当且仅当 $F_-(\xi_{c,+};\tau)=0$。
交换两侧给出 $\mathcal R_-=0$ 的相同处理；若两侧都为0，只需判断两中心是否相等。
所以无实侧和点侧已经完整处理。

以下假设 $\mathcal R_+>0,\mathcal R_->0$。
任选一个实可逆矩阵 $T$，使

$$
T^TA_+T=\mathcal R_+ I_2.
\tag{16}
$$

它总存在；例如若 $A_+=U^TU$ 是正对角 Cholesky 分解，可取
$T=\sqrt{\mathcal R_+}\,U^{-1}$。
于是第一侧的全部实解恰为

$$
\xi(\theta)=\xi_{c,+}+T\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix},
\quad \theta\in\mathbb R/(2\pi\mathbb Z).
\tag{17}
$$

这没有漏掉第一侧椭圆上的点。
将它代入第二侧，记

$$
B=T^TA_-T,\quad
g=T^T(A_-\xi_{c,+}+\ell_-),
$$
$$
f=\xi_{c,+}^TA_-\xi_{c,+}+2\ell_-^T\xi_{c,+}+c_-.
\tag{18}
$$

则第二侧在 (17) 上化为准确二阶三角多项式

$$
F_-(\xi(\theta);\tau)
=A_0+A_c\cos\theta+A_s\sin\theta
  +A_{2c}\cos2\theta+A_{2s}\sin2\theta,
\tag{19}
$$

其中

$$
A_0=f+\tfrac12(B_{11}+B_{22}),\quad
A_c=2g_1,\quad A_s=2g_2,
$$
$$
A_{2c}=\tfrac12(B_{11}-B_{22}),\qquad A_{2s}=B_{12}.
\tag{20}
$$

所有二次项和一次项均保留，没有只取某一侧的最大值或范数。

## 5. 一个完整的四次多项式加补点

对 $\theta\ne\pi\pmod{2\pi}$ 置 $t=\tan(\theta/2)$。
将 (19) 乘 $(1+t^2)^2>0$，准确得到

$$
p(t)=p_0+p_1t+p_2t^2+p_3t^3+p_4t^4,
\tag{21}
$$

系数为

$$
\boxed{\begin{aligned}
p_0&=A_0+A_c+A_{2c},\\
p_1&=2A_s+4A_{2s},\\
p_2&=2A_0-6A_{2c},\\
p_3&=2A_s-4A_{2s},\\
p_4&=A_0-A_c+A_{2c}.
\end{aligned}}
\tag{22}
$$

每个实根 $t$ 都给出一个双方同解

$$
\boxed{\xi=\xi_{c,+}+T
 \begin{pmatrix}(1-t^2)/(1+t^2)\\2t/(1+t^2)\end{pmatrix}.}
\tag{23}
$$

还必须检查半角坐标漏掉的点

$$
\boxed{\xi_\pi=\xi_{c,+}-T\begin{pmatrix}1\\0\end{pmatrix}.}
\tag{24}
$$

由 (19)，它是双方同解当且仅当
$F_-(\xi_\pi;\tau)=A_0-A_c+A_{2c}=p_4=0$。
所以不能只取数值多项式的有限实根而漏掉 (24)。
当最高系数退化时，(21) 就按实际次数求实根；(24) 仍单独按准确条件保留。

若 $p$ 恒等为零，则 (19) 在 $\theta\ne\pi$ 上恒零，连续性也覆盖 $\theta=\pi$；
整个第一侧椭圆都是双方同解，不应误报为四个离散支或根算法失败。
若 $p$ 不恒零，(21) 的所有实根加 (24) 准确给出全部双方同解，
没有其他相交点。
最后回到真实加速度

$$
\boxed{a=h\xi_1,\qquad b=-2\xi_2.}
\tag{25}
$$

这是一套完整的有限维等价消元，不是通过改变 $h,k,d,C_2$ 来另挑一个更易相交的末端。

## 6. 正则支与相切不能混同

若 $\mathcal R_+>0$，则第一侧在椭圆上的梯度不为零。
在某个双方交点 $\xi(\theta)$，两侧关于真实加速度坐标的 Jacobian 为

$$
J_\xi=2\begin{pmatrix}
(A_+\xi+\ell_+)^T\\
(A_-\xi+\ell_-)^T
\end{pmatrix}.
\tag{26}
$$

其行列式非零，当且仅当

$$
\frac d{d\theta}F_-(\xi(\theta);\tau)\ne0.
\tag{27}
$$

证明：$\xi'(\theta)=T(-\sin\theta,\cos\theta)^T$ 是非零第一侧切向量，
且与第一行梯度正交。第二行不平行于第一行，等价于其与该切向量配对非零，
这恰是 (27)。
由于 $(a,b)\mapsto\xi$ 可逆，(26) 非退化也等价于真实两个末加速度方向非退化。
在此条件下，标准隐函数定理给 $h,k,d,C_2$ 附近唯一的相应末 jet 支。

在有限半角根处，$dt/d\theta=(1+t^2)/2\ne0$，
而乘子 $(1+t^2)^2$ 严格正，所以 (27) 也等价于该多项式实根为单根。
漏点 (24) 应直接用 (27) 检查，不把“无有限 t”误称为退化。
相切、点椭圆或全椭圆重合均不满足这条一般正则支结论，须保留各自的退化情况。
本稿不从末 jet 的正则性推出整个射击/边值算子的可逆性。

## 7. 全部系数仍是原有限参考矩，最高次数10

在每一固定 $h,k,d$ 上，$z=d+\sigma hy$ 是 y 的一次式。
$Q^3=(1+z^2)^3$ 次数6，$u$ 次数1，$R$ 次数2。
因此 (6) 中

$$
\deg(Q^3uu^T)\le8,\qquad
\deg(Q^3Ru)\le9,\qquad
\deg(Q^3R^2)\le10.
\tag{28}
$$

R598 已证的同一三组次数10正参考矩身份恰好足够；
可使用原有限和，也可准确使用

$$
\sum_iw_iP(c_i)=\frac{50}{99}
\int_{401/100}^{599/100}P(y)\,dy.
\tag{29}
$$

两种写法是同一代数系数，不能把积分域换成整个母窗口 $[4,6]$。
这里无需新增 profile 求积或重新重建原正势表。
若把它实现成实际输入接口，其几何参数、选定支、数值根误差和所有科学评价成本仍须公开报告。
本文没有科学求出当前 R625 输入的任何新末加速度值，也没有把纸证阈值冒当前有限候选的测量结果。

## 8. 与原有限宽度 BVP 的关系

本结论只给 (1) 同一条件首层中的准确末二阶关系。
它可以用于说明为什么只有必要符号还不够，或为后续明确的新输入选择真正的末 jets；
不能在原十九态求解中增加两个独立末加速度参数以免除原反馈方程。
实际 BVP 中 $a,b$ 已由同一个原两 ruling 矩阵、完整 A/rho/势和常规范确定。

即使两侧椭圆有一个正则交点，也仍未给出能把自由中心连到该末点的真 $M$ 首层全程，
未给出固定 $\varepsilon$ 解，未支付原尾中心和所有周期/位置闭合。
若数值候选未满足 $A(L)=0$ 或双末速度为0，更不能把其末读数直接代作 (1) 的严格实例。
原连续闭面、固定度量精化、全时嵌入/reach 与宏观握持幅度继续按主 README 完整支付。
