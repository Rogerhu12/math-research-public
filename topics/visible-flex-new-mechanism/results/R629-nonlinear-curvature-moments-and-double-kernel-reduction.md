# R629：准确非线性三矩身份、自由内帽第一模逆与双核有限块

2026-11-28。**已证明：近欧氏平面度量的三个准确曲率矩身份、固定三维余核的非线性消元、自由内帽的零/一模显式逆，以及 R628 双核的具体有限维增广块。**

本稿不声称 R628 的新背景已经有全频 tame inverse，不把 Hu 的偶对称单核定理套到新背景。特征返回、小除数、无限角匹配和残差校正仍是实际未完成输入。这里解决的是一个更明确的问题：允许内帽作真实刚体运动以后，第一角模的非线性兼容是否必须另以三个任意的外力或误差项支付。

## 1. 近欧氏平面度量的三个准确曲率矩

设 $\gamma$ 是 $\mathbb R^2$ 上的光滑正定度量，在固定圆盘 $B_R$ 外等于欧氏度量 $e$。假设 $\gamma-e$ 的一个固定低阶范数（例如固定支持上的 $C^4$ 范数）充分小。则存在保持方向的光滑微分同胚

$$
P:\mathbb R^2\longrightarrow\mathbb R^2,
\qquad P(z)=z+O(|z|^{-1})\quad(|z|\to\infty),           \tag{1}
$$

以及光滑实函数 $\phi$，使

$$
\gamma=P^*(e^{2\phi(y)}|dy|^2).
$$

在这些同一个度量自己的等温坐标中，准确有

$$
\boxed{\int K_\gamma\,dA_\gamma=0,\qquad
\int P_1K_\gamma\,dA_\gamma=0,\qquad
\int P_2K_\gamma\,dA_\gamma=0.}                         \tag{2}
$$

特别，(2) 不假设 $K_\gamma=0$；它是对未解状态仍成立的非线性身份。

### 1.1 规范化等温坐标的直接构造

在固定 Cartesian 坐标写 $\gamma=E_0dx^2+2F_0dxdy+G_0dy^2$，并令

$$
\mu=\frac{E_0-G_0+2iF_0}{E_0+G_0+2\sqrt{E_0G_0-F_0^2}},
\quad
\lambda=\frac{E_0+G_0+2\sqrt{E_0G_0-F_0^2}}4.
$$

逐项展开给

$$
\gamma=\lambda|dz+\mu\,d\bar z|^2,
\qquad \mu=0,\ \lambda=1\quad\text{于 }\mathbb R^2\setminus B_R.
                                                               \tag{3}
$$

用满足 $\bar\partial\mathcal Cq=q$ 的平面 Cauchy 算子，令 $\mathcal B=\partial\mathcal C$。其 Fourier 乘子在非零频率上模长为一，故由 Plancherel，$\mathcal B$ 在 $L^2$ 上为等距算子，并与常系数微分交换。

当 $\|\mu\|_\infty<1$ 时，方程

$$
q=\mu(1+\mathcal Bq)                                  \tag{4}
$$

在 $L^2$ 中由 Neumann 级数唯一解出，且 $q$ 支持于 $\overline B_R$。取

$$
P(z)=z+\mathcal Cq(z).
$$

于是 $P_{\bar z}=q=\mu P_z$，并且 $P_z=1+\mathcal Bq$。

这里所需的低阶正则性也可由同一方程直接取得。对多指标 $\alpha$ 微分，最高项保留在左边：

$$
(I-\mu\mathcal B)\partial^\alpha q
=\partial^\alpha\mu+
\sum_{0<\beta\le\alpha}\binom\alpha\beta
(\partial^\beta\mu)\mathcal B(\partial^{\alpha-\beta}q). \tag{5}
$$

$L^2$ 逆的范数不超过 $(1-\|\mu\|_\infty)^{-1}$。先用差分商证明一阶，再按 (5) 归纳，得到每个有限阶 Sobolev 正则性；光滑 $\mu$ 因而给光滑 $q$。固定支持和小 $C^4$ 范数还给小 $H^3$ 范数。Sobolev 嵌入遂使 $\|DP-I\|_\infty<1/2$，只需缩小这个固定低阶邻域。

因此 $P$ 是双 Lipschitz 的局部微分同胚；它由 (1) proper，故是全局微分同胚。由 (3)，

$$
\phi(P(z))=\tfrac12\log\lambda(z)-\log|P_z(z)|.         \tag{6}
$$

这完成所需的等温坐标构造。它没有使用待证的平坦性或 Darboux 方程。

### 1.2 无穷远衰减与全部边界项

因为 $q$ 光滑且紧支撑，Cauchy 积分在支持外给收敛 Laurent 展开

$$
P(z)=z+\frac{c_1}{z}+\frac{c_2}{z^2}+\cdots,
\qquad P_z=1+O(|z|^{-2}).                              \tag{7}
$$

外侧 $\lambda=1$，所以 (6)、(7) 给

$$
\phi(y)=O(|y|^{-2}),\qquad \nabla\phi(y)=O(|y|^{-3}).   \tag{8}
$$

对于 $\gamma=P^*(e^{2\phi}|dy|^2)$，直接计算 conformal Christoffel 符号得到

$$
K_\gamma\,dA_\gamma=-P^*(\Delta\phi\,dy_1dy_2).
$$

以 $1,y_1,y_2$ 为测试函数在 $|y|\le T$ 分部积分。常数测试的边界项为 $O(T^{-2})$；线性测试的两个边界项
$\int(y_i\partial_n\phi-\phi\partial_ny_i)$ 都为 $O(T^{-1})$。令 $T\to\infty$ 全部消失，正是 (2)。

因此第一矩并非在原 Cartesian 坐标中任意写成 $\int x_iK\,dA=0$；必须使用**同一未解度量**的 $P_i$。省略这一依赖会把准确身份改成错误的线性近似。

## 2. 对旋转目标度量 Darboux 残差的准确形式

在圆盘上令 $g=E(r)dr^2+r^2d\theta^2$，其中 $E=1+w^2$，$w$ 在两端有开平帽延拓。设高度 $Z$ 在外帽为常数，在内帽为一个平面的准确仿射高度，并使

$$
\gamma=g-dZ\otimes dZ>0.
$$

将整个内盘填满，再在外盘外令 $g=e$、$Z$ 为该常数。于是 $\gamma$ 是上一节的平面度量。在旋转背景 $Z=h,h'=-w$ 处，$\gamma=e$；只需取其固定低阶邻域，即可使用 (2)。

定义

$$
\Delta=E-Z_r^2-\frac E{r^2}Z_\theta^2>0,
$$

$$
\begin{split}
\mathcal D(Z,E)={}&E\left\{Z_{rr}Z_{\theta\theta}
                 -(Z_{r\theta}-Z_\theta/r)^2\right\}
+rZ_rZ_{rr}\\
&-\frac{E'}2\left(r+Z_rZ_{\theta\theta}-Z_\theta^2/r\right).
                                                               \tag{9}
\end{split}
$$

R574 的曲率恒等式逐项给

$$
K_\gamma=-\frac{\mathcal D}{r^2\Delta^2},\qquad
K_\gamma dA_\gamma=
-\frac{\mathcal D}{r\Delta^{3/2}}\,dr\,d\theta.          \tag{10}
$$

因此取真实曲率密度残差

$$
\mathscr R(Z,w)=-\frac{\mathcal D(Z,1+w^2)}{r\Delta^{3/2}},
                                                               \tag{11}
$$

则它在所有未解状态上都满足

$$
\int\mathscr R=0,\qquad
\int P_1\mathscr R=0,\qquad
\int P_2\mathscr R=0.                                  \tag{12}
$$

这里积分在 $dr\,d\theta$ 下；内外平帽的曲率准确为零，故也可只积非平连接区。权 $\Delta^{-3/2}$、同一 $P$ 及真实内帽必须全部保留，不能只对 (9) 作未经加权的有限 FFT 求和。

在 $Z=h$ 处 $\Delta=1,P=(r\cos\theta,r\sin\theta)$，对固定 $w$ 的高度增量 $u$ 有

$$
D_Z\mathscr R(h,w)u=(wu_r)_r+\frac{w'}r u_{\theta\theta}
=:L_wu.                                                \tag{13}
$$

故 (12) 的线性化正给常数与两条第一角模的余核条件；R628 的 (16) 是其中一个二阶实例。

## 3. 固定三维余核投影足以恢复完整非线性方程

取两个光滑径向函数 $b_0,b_1$，紧支撑于一个固定普通子区间 $I\Subset(a,b)$，满足

$$
2\pi\int b_0(r)\,dr=1,\qquad
\pi\int r b_1(r)\,dr=1.
$$

令

$$
B_0=b_0(r),\qquad B_1=b_1(r)\cos\theta,\qquad
B_2=b_1(r)\sin\theta.
$$

对残差定义固定线性矩

$$
\ell_0R=\int R,\quad
\ell_1R=\int r\cos\theta R,\quad
\ell_2R=\int r\sin\theta R,
$$

以及

$$
\Pi R=R-\sum_{j=0}^2B_j\ell_jR.                       \tag{14}
$$

由角正交和规范，$\ell_iB_j=\delta_{ij}$，故 $\Pi$ 是到这三个固定矩核空间的投影。

**命题。** 在足够小的固定低阶邻域中，

$$
\boxed{\Pi\mathscr R(Z,w)=0\quad\Longrightarrow\quad
\mathscr R(Z,w)=0.}                                    \tag{15}
$$

证明：前提写成 $\mathscr R=\sum B_jc_j$。用准确 (12) 得 $M(Z,w)c=0$，其中

$$
M_{ij}=\int\psi_i B_j,
\qquad(\psi_0,\psi_1,\psi_2)=(1,P_1,P_2).
$$

在背景处 $M=I$。第 1 节的构造及低阶估计给 $P$ 连续依赖度量，故缩小固定低阶邻域后 $\|M-I\|<1/2$。于是 $M$ 可逆，$c=0$。证毕。

投影并未删掉整个零模或第一模：它只去掉三个固定紧支撑方向，剩余全部径向第一模方程仍须实际求解。因为准确矩会迫被投掉的三个系数为零，这不是允许物理残差或更换目标度量。

若只保反射对称 $Z(r,-\theta)=Z(r,\theta)$，而不保 half-turn，规范化 $P$ 也由唯一性与反射相容。第二坐标为奇函数，正弦矩自动为零；可以仅用 $B_0,B_1$。这个反射子空间同时容纳 $\cos2\theta$、$\cos3\theta$ 和实际内帽倾斜。

## 4. 内帽自由刚体参数给零、一角模的具体线性逆

先取紧支撑的径向源；同一公式也适用于所写积分及其导数被真正超 $w$ 全平界控制的源。

### 4.1 零角模

若 $\int_a^b R_0=0$，置

$$
J_0(r)=\int_a^rR_0(s)\,ds=-\int_r^bR_0(s)\,ds,
$$
$$
F_0(r)=-\int_r^b\frac{J_0(s)}{w(s)}\,ds.              \tag{16}
$$

则 $(wF_0')'=R_0$；外帽高度为零，内帽高度为一个自由常数，所有正阶尾 jets 为零。这是该外帽规范下的唯一解：齐次解满足 $wF_0'=C$，外平帽光滑性迫 $C=0$，外高度规范再迫常数为零。

### 4.2 第一角模

若 $\int_a^b rR_1(r)\,dr=0$，置

$$
J_1(r)=\int_a^r sR_1(s)\,ds=-\int_r^b sR_1(s)\,ds,
$$
$$
F_1(r)=-r\int_r^b\frac{J_1(s)}{w(s)s^2}\,ds.          \tag{17}
$$

于是

$$
(wF_1')'-\frac{w'}rF_1=R_1.
$$

外帽 $F_1=0$，内帽 $F_1=\beta r$。这正是平帽的自由倾斜，不要求它也为零。唯一性同样直接：齐次方程给 $w(rF_1'-F_1)=C$，外帽光滑性迫 $C=0$，继而 $F_1=cr$；外帽规范迫 $c=0$。

因此第一模不是因“它含刚体解 $r$”而必须禁用。给内帽正确的自由刚体边界以后，所需的一个加权矩正是 (12) 解决的余核，而解本身由 (17) 明确给出。若仍错误地要求内帽第一模为零，会额外加上 $\int J_1/(wr^2)=0$，恰好把 R628 的非零倾斜人为删掉。

## 5. 非线性内帽图必须用真实旋转尾

仅在内盘上写一个仿射高度，还不足以无条件套旧全平函数空间。在其邻近尾部，直接添加 $\beta r\cos\theta$ 而不加入相应的径向旋转项，可能产生按 $w$ 而非按快速核衰减的残差。

一个明确的可用图如下。设 $h_a=h_w(a)$，取固定径向 cutoff $\chi$，在整个左端尾为 $1$，在右端尾为 $0$，变化只发生于普通紧区间。令

$$
Z^{\rm ref}_{w,\beta}(r,\theta)
=h_a+(h_w(r)-h_a)\cos(\beta\chi(r))
                   +r\cos\theta\sin(\beta\chi(r)).     \tag{18}
$$

在左尾，(18) 是整个旋转背景 $X_w$ 绕内帽中心作一个真实刚体转动后的竖直坐标；在右尾仍是原背景。因而两个尾在零修正时都准确满足 Darboux 方程，内盘是准确倾斜平面。只在紧过渡区产生新残差。

可再加入一个内帽高度常数乘 cutoff，以及相对于这两个真实尾全平的未知修正。水平坐标仍须从同一 $g-dZ^2$ 恢复；它在内帽是一个真正的平面等距嵌入，不能保留旧水平圆盘却只改高度。

对有限固定背景，足够小的 $\beta$ 保持 $g-dZ^2$ 正定并落在第 1 节的邻域。这个定性小邻域尚未量化为宏观转角；特别不能忽略 R628 高正层对允许角度的影响。

## 6. 双共振的明确增广矩阵

现在固定 R628 得到的一个有限、平滑、同背景双核 $w_*$，保留其两个正中心高度参数 $(A,C)$ 的光滑族 $w_{A,C}$，并保留反射对称而去掉 half-turn。记两个规范核为 $f_2\cos2\theta,f_3\cos3\theta$。

两条核的实径向 Green 配对矩阵是

$$
G_{j\alpha}=\int_a^b f_j(\partial_\alpha L_j)f_j\,dr,
\qquad j=2,3,\quad\alpha=A,C.
$$

参数只改变普通紧区间内的 $w$，故分部积分准确给

$$
G_{j\alpha}=\int_a^b(\partial_\alpha w)
\left\{-(f_j')^2+\frac{2j^2}{r}f_jf_j'
                         -\frac{j^2}{r^2}f_j^2\right\}dr. \tag{19}
$$

它的每一行是对应射击行列式导数的一非零倍数。可在两个普通切口间直接证明：从固定左尾线启动参数导数，把 $f_j\partial_\alpha L_jf_j$ 积分为左右 Wronskian；左端为零，右端正是偏离真右尾稳定线的行列式导数。右稳定向量非零，而正则二阶方程的 Wronskian 配对非退化，因而规范因子非零；不要求该向量的每个分量分别非零。没有在发散的裸端点上分别写未定义通量。

R628 的中心 Jacobian 为 $45/16\ne0$，且真实尾匹配、有限高层和足够小的平滑均保此非退化性，故

$$
\det G\ne0.                                           \tag{20}
$$

取一个总幅值 $q$，同时保留两模的非零归一，例如 $u_*=f_2\cos2\theta+f_3\cos3\theta$。使用 (18) 的真实帽图，把 $Z$ 写成 $h_w+q u$ 的平滑参数化版本；内帽倾斜参数可写为 $qb$，且 $b=0$ 于初始点。对准确曲率残差除以 $q$ 并在 $q=0$ 光滑延拓，再应用固定投影 (14)。初始零为

$$
q=0,\quad w=w_*,\quad u=u_*,\quad b=0.
$$

固定两个核归一线性泛函 $\mathfrak l_2u=1,\mathfrak l_3u=1$。所需增广线性方程的具体形状是

$$
L_{w_*}\dot u
+\dot A\,(\partial_A L)u_*
+\dot C\,(\partial_C L)u_*=R,\qquad
\mathfrak l_2\dot u=\mathfrak l_3\dot u=0,              \tag{21}
$$

其中 $R$ 留在 (14) 的固定矩核中，$\dot u$ 的内帽允许常数和第一模倾斜。先将 (21) 配对两个核，(20) 唯一解出 $(\dot A,\dot C)$；零、一模随后用 (16)、(17) 解出。这是两个真实中心控制和两个核归一的最小有限块，不需要预先指定一个未知非同轴圆领。

二次源只有 $0,1,4,5,6$ 角频，因此在这个双模归一的分支若真正构造出来，第一阶背景参数变化为零；R628 的第一模帽倾斜首项为 $q^2\beta$。这一陈述仍以完整非线性分支存在为前提，不从一个形式展开宣称已经积分成功。

## 7. 已解决和未解决的准确分界

本稿把真正的非线性第一模兼容归结到已证明的 (2)、(15)，给出自由内帽的实际线性逆，并给出双共振的非奇异有限块 (19)–(21)。这些都是同一真实旋转目标度量与同一平面度量 $g-dZ^2$ 上的身份。

仍未解决的是 (21) 中**全部其余角频同时**的统一逆，以及其在真实非线性状态附近的控制。R628 §5 只给预先固定有限 $j$ 的全平稳定线；它不提供 $j\to\infty$ 的小除数界、双端匹配下界、特征返回图控制或固定损失 tame estimate。Hu 原构造的负曲率组件返回、角行程选择和残差修正也不能因本稿的三矩身份而省去。

最终相位族只需要一个非零有限幅值的准确嵌入：设计阶段可以真实调整 $(A,C)$，成功后冻结 $w,g$ 再使用 R1 的相位动作。因此无需额外要求幅值参数 $q$ 本身保持同一度量。但该一个有限幅值的全域根、其实际倾斜和偏心量、全部几何与同 $g$ 精化仍须做出；本稿没有以局部身份或有限块代替它们。

来源与复用：R628 的同一全平双核与二阶端口；R574 的完整 Darboux–平坦度量关系；R1 的不同圆领轴相位传递。本稿的三矩身份、固定投影消元及真实旋转尾图均由上文直接证明。
