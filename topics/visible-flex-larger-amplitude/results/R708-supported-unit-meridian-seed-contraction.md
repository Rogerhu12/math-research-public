# R708 — 支持内单位 meridian 的三均值收缩闭合构造

日期：2026-11-26。状态：**已证明以下明确条件下的准确单位径向积分闭合、共同分支及端口恒等式。** 这不是完整等距嵌入存在定理；混合与角向 Gram、全局几何、20% 幅度、reach、有限表示误差和固定问题精化均未由本文解决。没有运行新的科学计算，也没有把所列充分条件加入已有科学入口的额外验收门。

本构造的用途是产生一个新的实际初始形状，随后仍在原全部自由变量中求解。它不把原两 bubble 或新增 gamma 的少数控制换个坐标再求同一个根，也不由旧小控制球的失败推出任何不可能性。旧 normal-lift、KKT 和显式 H 源码均保持其已登记身份。

## 1. 准确数据与要闭合的积分

取固定准确径向域 $s\in[0,S]$ 和固定材料图
$\theta_0(\phi)$，其中 $\rho_0=\theta_0'>0$。
固定标量度量仍为
$$
g=ds^2+a(s)^2\,d\theta_0^2 .
\tag{1}
$$
本节所有积分、节点和宽度都是准确数学对象；尚未用有限 Gauss 或 binary64 载体代替它们。

给定准确单位参考 meridian $T_0(s,\phi)$，帽端曲线
$$
P(\phi)=R e_r(\theta_0(\phi))+H e_z
$$
和要保持的握持端曲线 $\Gamma(\phi)$。$H$ 是一个全局标量，在这里保持给定值，不令其依角变化。$\Gamma$ 可以来自原全部 core 系数及准确逆图；本构造不删去或冻结任何原本自由的 core 槽。

取严格内部的有限个互不相交支持区间
$$
U=\bigcup_{\alpha=1}^{r}(a_\alpha,b_\alpha)\Subset(0,S),
\quad \ell_\alpha=b_\alpha-a_\alpha,
\quad L=\sum_{\alpha=1}^{r}\ell_\alpha>0 .
$$
要求 $T=T_0$ 于 $[0,S]\setminus U$。于是准确端点条件
$F(0,\phi)=\Gamma(\phi)$，其中
$$
F(s,\phi)=P(\phi)-\int_s^S T(t,\phi)\,dt,
\tag{2}
$$
等价于
$$
\int_U T(s,\phi)\,ds=K(\phi),\qquad
K=P-\Gamma-\int_{[0,S]\setminus U}T_0\,ds .
\tag{3}
$$

这里直接使用所需支持积分 $K$，没有重新证明或放宽既有弦长必要条件。下面给出严格强于单纯 $|K|<L$ 的一组可计算充分输入。

正则性只要求本证明实际用到的经典导数存在。一个方便的充分假设是数据在每个所列径向分片及角上足够光滑，$T_0,T_{0,s},T_{0,\phi},T_{0,\phi\phi}$ 及需要的混合导数连续，分片端口相容；若要进一步对全部外参数求一次六 jet 导数，另要求该混合导数存在。不能只凭任意 $C^2$ 参数映射声称这些更高混合导数已经自动存在。

## 2. 统一正隙条件与一个显式端层选择

假设整个角圈有已知常数
$$
0<k_-\le |K(\phi)|\le k_+<L,\qquad
K_z(\phi)\ge k_z>0 .
\tag{4}
$$
另假设所选端层上的 $T_{0,z}\ge0$。如果后面要推全径向高度单调，再要求这个非负条件覆盖整个域。

条件 (4) 包括正垂直方向信息；仅有先前支持弦长必要条件通过，不能据此补出 $k_z$、端层非反向域或下面的所有余量。当前实际输入是否满足一套有用的定量常数，需要对它自身准确对象另行读取，本文不预填数值。

选一个共同端层总长度 $b>0$，每个支持区间两端各取
$$
\delta=\frac{b}{2r},\qquad
L_c=L-b,\qquad
r_-=\frac{k_--b}{L_c},\quad
r_+=\frac{k_++b}{L_c}.
\tag{5}
$$
要求
$$
b<r\min_\alpha\ell_\alpha,\quad b<k_-,\quad b<k_z,
\quad k_++2b<L .
\tag{6}
$$
于是所有中央区间有正长度，$0<r_-\le r_+<1$。

定义
$$
\zeta=\frac{k_z-b}{k_++b}\in(0,1),\qquad
\nu=\sqrt{\frac{1-\sqrt{1-\zeta^2}}2}>0 .
\tag{7}
$$
最后要求
$$
q:=\frac{b}{\nu(k_--b)}<1.
\tag{8}
$$

这些条件不是空的。令
$$
\zeta_0=\frac{k_z}{3k_+},\qquad
\nu_0=\sqrt{\frac{1-\sqrt{1-\zeta_0^2}}2}.
$$
任取
$$
0<b\le
\min\left\{
 \frac{r\min_\alpha\ell_\alpha}{2},\
 \frac{k_-}{2},\
 \frac{k_z}{2},\
 \frac{L-k_+}{4},\
 \frac{\nu_0 k_-}{4}
\right\}
\tag{9}
$$
即足够。事实上 $b\le k_z/2\le k_+/2$ 给 $\zeta\ge\zeta_0$，
故 $\nu\ge\nu_0$；而 $k_--b\ge k_-/2$ 给 $q\le1/2$。
其余各正长度和严格上界也直接由 (9) 得到。

因此在 (4) 和半球条件下，薄端层总能为下面的准确闭合构造提供一个数学选择。但是端层过薄可能产生很大的形状导数；这项存在论选择不自动满足 reach 或任何原几何预算。

## 3. 完整单位端层及其对三均值参数的导数

记五次端点平坦函数
$$
S_5(t)=10t^3-15t^4+6t^5,\qquad 0\le t\le1 .
$$
它从 0 单调到 1，端点的一、二阶导数为零。

在第 $\alpha$ 个左端层 $[a_\alpha,a_\alpha+\delta]$ 取
$\chi=S_5((s-a_\alpha)/\delta)$；在右端层
$[b_\alpha-\delta,b_\alpha]$ 取
$\chi=S_5((b_\alpha-s)/\delta)$。
外侧 $\chi=0$，中央侧 $\chi=1$，两侧端点均有
$\chi_s=\chi_{ss}=0$。

对一个单位方向 $d$ 定义
$$
Y=(1-\chi)T_0+\chi d,\qquad
T_b=\frac{Y}{|Y|},\qquad
B(d,\phi)=\int_{\text{全部端层}}T_b(s,\phi,d)\,ds .
\tag{10}
$$
$B$ 是完整向量积分，尤其保留它的 $x,y,z$ 三个分量及角导数。不能用一个轴向标量或固定偏移代替它。

对每个 $\phi$ 考虑闭球
$$
\mathcal D_\phi=
\left\{v\in\mathbb R^3:
 \left|v-\frac{K(\phi)}{L_c}\right|\le\frac b{L_c}\right\}.
\tag{11}
$$
其中每个 $v$ 都满足
$$
r_-\le |v|\le r_+,\qquad
v_z\ge\frac{k_z-b}{L_c},\qquad
d=\frac v{|v|}\Longrightarrow d_z\ge\zeta .
\tag{12}
$$
因为 $T_{0,z}\ge0$、$d_z\ge\zeta$，
$$
T_0\cdot d\ge-\sqrt{1-\zeta^2}.
$$
故整个归一化路径都有
$$
|Y|^2
 =1-2\chi(1-\chi)(1-T_0\cdot d)
 \ge\frac{1-\sqrt{1-\zeta^2}}2=\nu^2.
\tag{13}
$$
这付清了端层的非反向问题；没有在零范数处裁剪或假设反解存在。

令 $N(y)=y/|y|$。准确微分为
$$
DN(y)[h]=\frac{(I-N(y)N(y)^T)h}{|y|}.
$$
因此
$$
|B|\le b,\qquad
\|D_d B\|\le\frac b\nu,\qquad
\left\|D_v B\!\left(\frac v{|v|},\phi\right)\right\|
 \le\frac b{\nu r_-}.
\tag{14}
$$
这些是诱导 Euclidean 算子范数。若使用更紧的准确
$\int\chi/|Y|$ 上界也可以；本文只需 (14) 的完整保守界。

## 4. 三均值参数的共同收缩与唯一完整分支

设
$$
\mathcal T_\phi(v)
 =\frac{K(\phi)-B(v/|v|,\phi)}{L_c}.
\tag{15}
$$
由 $|B|\le b$，它把 $\mathcal D_\phi$ 映回自身。
该球凸且不含零，所以沿球内线段积分 (14) 得
$$
|\mathcal T_\phi(v)-\mathcal T_\phi(\widetilde v)|
 \le q\,|v-\widetilde v|,\qquad q<1 .
\tag{16}
$$

从 $v^{(0)}=K/L_c$ 出发迭代 (15)，相邻差以 $q^n$ 几何衰减。
其和可收敛且极限仍在闭球内，因此存在固定点 $v(\phi)$。
若另有固定点，(16) 直接迫使两者相等。还得到可复核的准确尾界
$$
|v-v^{(n)}|
 \le\frac{q^n}{1-q}|v^{(1)}-v^{(0)}|
 \le\frac{q^n b}{(1-q)L_c}.
\tag{17}
$$
这说明准确三均值系统有同一个唯一选择，不依赖任意逐角 Newton 初值或局部根标签。

写
$$
\widetilde B(v,\phi)=B(v/|v|,\phi),\qquad
\mathcal H(v,\phi)=L_c v+\widetilde B(v,\phi)-K(\phi).
$$
其矩阵
$$
J_v=L_c I+\widetilde B_v
$$
满足
$$
\|J_v^{-1}\|\le\frac1{L_c(1-q)}.
\tag{18}
$$
用几何级数可直接证明 (18)，不要求 $J_v$ 对称。
因此在实际混合正则性前提下，唯一固定点对角和给定外参数具有相同的局部可微性；共同唯一域把这些局部选择联成完整角圈的同一分支。

端层 $B$ 依赖完整当前数据。任何参数微分都必须连同该依赖支付，不能把准确闭合后的 $B$ 冻成常数。本式也不是原两 bubble 控制的 Jacobian 换尺度。

## 5. 中段反向配对的单位转角 profile

取
$$
0<\epsilon<\min(1/8,r_-/4).
\tag{19}
$$
在 $t\in[0,1]$ 定义
$$
h_\epsilon(t)=
\begin{cases}
S_5(t/\epsilon),&0\le t\le\epsilon,\\
1,&\epsilon\le t\le\tfrac12-\epsilon,\\
1-2S_5((t-\tfrac12+\epsilon)/(2\epsilon)),
 &\tfrac12-\epsilon\le t\le\tfrac12+\epsilon,\\
-1,&\tfrac12+\epsilon\le t\le1-\epsilon,\\
-S_5((1-t)/\epsilon),&1-\epsilon\le t\le1.
\end{cases}
\tag{20}
$$
各接点的值、一阶和二阶导数匹配。
它满足
$$
h_\epsilon(1-t)=-h_\epsilon(t),\quad |h_\epsilon|\le1,\quad
h_\epsilon=h_\epsilon'=h_\epsilon''=0\ \text{于 }t=0,1.
$$
两段 $|h_\epsilon|=1$ 的平台总长度为 $1-4\epsilon>0$。

定义准确一维均值
$$
a_\epsilon(\lambda)=\int_0^1
       \cos(\lambda h_\epsilon(t))\,dt .
\tag{21}
$$
由于反对称性，$\int_0^1\sin(\lambda h_\epsilon)\,dt=0$。
在 $0<\lambda\le\pi/2$，
$$
a_\epsilon'(\lambda)
 =-\int_0^1|h_\epsilon(t)|
       \sin(\lambda|h_\epsilon(t)|)\,dt<0.
\tag{22}
$$
同时
$$
a_\epsilon(0)=1,\qquad
a_\epsilon(\pi/2)\le4\epsilon<r_- .
$$
于是对 $r=|v|\in[r_-,r_+]$ 有且仅有
$$
\lambda(\phi)\in(0,\pi/2),\qquad
a_\epsilon(\lambda)=r .
\tag{23}
$$
这里的 $\lambda$ 只是 seed 的转角幅度，不是课题的物理弯曲相位。

由 $a_\epsilon(\lambda)\ge\cos\lambda$，
$\lambda\ge\arccos r_+>0$。
由两平台对 (22) 的贡献，
$$
-a_\epsilon'(\lambda)
 \ge(1-4\epsilon)\sin\lambda
 \ge(1-4\epsilon)\sqrt{1-r_+^2}>0 .
\tag{24}
$$
因此这一步也有统一非零导数，没有把一个可能折叠的三根选择再包装成同样的局部隐式问题。

## 6. 全角光滑、反射协变的中段方向

取固定材料图中的水平径向单位向量
$e(\phi)=e_r(\theta_0(\phi))$，定义
$$
w(\phi)=
 \frac{e-(e\cdot d)d}{\sqrt{1-(e\cdot d)^2}}.
\tag{25}
$$
因 $e$ 水平且 $d_z\ge\zeta$，
$$
\sqrt{1-(e\cdot d)^2}\ge d_z\ge\zeta>0.
$$
所以 $w$ 全角定义良好，与 $d$ 正交、单位且光滑。
这里特意使用 polar 的 $e_r$ 投影，不用在原反射下额外翻号的角向 $e_\theta$。

在每个中央区间 $[a_\alpha+\delta,b_\alpha-\delta]$，
以其准确局部坐标 $t$ 取
$$
T_c(s,\phi)
 =\cos(\lambda(\phi)h_\epsilon(t))\,d(\phi)
  +\sin(\lambda(\phi)h_\epsilon(t))\,w(\phi).
\tag{26}
$$
准确 $|T_c|=1$，两端 $T_c=d$ 且 $T_{c,s}=0$；
在有二阶径向数据时还保 $T_{c,ss}=0$。
由于每个中央区间使用同一局部 profile，
$$
\int_{\text{全部中央区间}}T_c\,ds
 =L_c a_\epsilon(\lambda)d=L_c v .
\tag{27}
$$

现在定义 $T$ 为外部 $T_0$、端层 $T_b$、中央 $T_c$ 的拼接。
式 (15) 和 (27) 给
$$
\int_U T\,ds=B(d,\phi)+L_c v=K(\phi).
\tag{28}
$$
这就是所需的完整三分量端点闭合。没有遗漏平移常数、端层积分、端层的角导数或不同中央长度的权。

## 7. 整个角圈的共同分支、周期与两类反射

设数据对某个正交空间变换 $Q$ 和角变换 $\phi\mapsto\phi'$ 满足
$$
K(\phi')=QK(\phi),\quad
T_0(s,\phi')=QT_0(s,\phi),\quad
e(\phi')=Qe(\phi).
\tag{29}
$$
支持、$b$、$\epsilon$ 和局部径向 profile 共同固定。
归一化及积分与正交变换交换，故
$$
\mathcal D_{\phi'}=Q\mathcal D_\phi,\qquad
\mathcal T_{\phi'}(Qv)=Q\mathcal T_\phi(v).
$$
唯一固定点推出 $v(\phi')=Qv(\phi)$，继而
$d'=Qd$、$w'=Qw$、$\lambda(\phi')=\lambda(\phi)$ 和
$T(s,\phi')=QT(s,\phi)$。

这覆盖原 polar 反射
$Q_y=\operatorname{diag}(1,-1,1)$、$\phi'=-\phi$，
以及半周旋转
$Q_\pi=\operatorname{diag}(-1,-1,1)$、$\phi'=\phi+\pi$。
两者合成给另一 quarter 反射。对 $\phi+2\pi$ 使用相同数据与相同唯一域，给真正周期同支。

这里依靠的是共同不变域里的唯一性，不是“各角存在一个局部 IFT 根”就自动推出反射或周期。若数据不满足 (29)，也不从对称的算法名称假定其满足。

## 8. 完整角导数及可执行隐式接口

以下所有偏导都在固定 $v$ 时定义，$\widetilde B$ 含端层 $T_0$ 和归一化的完整依赖。准确公式是
$$
\begin{aligned}
J_v v_\phi&=K_\phi-\widetilde B_\phi,\\
J_v v_{\phi\phi}
 &=K_{\phi\phi}-\widetilde B_{\phi\phi}
   -2\widetilde B_{\phi v}v_\phi
   -\widetilde B_{vv}[v_\phi,v_\phi].
\end{aligned}
\tag{30}
$$
$J_v$ 的同一逆界是 (18)。对 $r=|v|$、$d=v/r$，
$$
\begin{aligned}
r_\phi&=d\cdot v_\phi,\\
r_{\phi\phi}
 &=d\cdot v_{\phi\phi}
   +\frac{|v_\phi|^2-(d\cdot v_\phi)^2}{r},\\
d_\phi&=\frac{(I-dd^T)v_\phi}{r},\\
d_{\phi\phi}
 &=\frac{(I-dd^T)v_{\phi\phi}}r
   -2\frac{r_\phi}{r}d_\phi-|d_\phi|^2d .
\end{aligned}
\tag{31}
$$
进而
$$
\lambda_\phi=\frac{r_\phi}{a_\epsilon'(\lambda)},\qquad
\lambda_{\phi\phi}
 =\frac{r_{\phi\phi}
        -a_\epsilon''(\lambda)\lambda_\phi^2}
        {a_\epsilon'(\lambda)}.
\tag{32}
$$
$w$ 的导数由 (25) 的同一个正分母准确求导，不能在各角独立重选其正负方向。

这些公式给同一准确 $T,T_s,T_\phi,T_{\phi\phi}$。
任何工作实现应固定共同 $U,b,\epsilon$ 和准确积分定义，以完整三均值系统及 (21) 为数学对象；有限求根残差、节点、权、宽度、三角函数和归约误差另外记录。不能把工作正权和或 inverse 残差直接称为 (28) 的准确等式。

如果把此构造用于当前完整外参数的可微入口，则三均值和幅度的全部角 jet 方程都须保留其外参数链，末次只使用 (28) 的三个方程不足重建所有导数。本文给出了准确系统和逆界；没有宣称已经实现其完整数值 J/J*。

## 9. 径向接合、core/cap 全六 jet

端层外侧 $\chi=0$ 且 $\chi_s=0$，故
$T=T_0$、$T_s=T_{0,s}$；中央侧 $\chi=1$ 且 $\chi_s=0$，
故 $T=d$、$T_s=0$。
这与 (26) 的端值一致。角导数也因相同端值函数逐项一致。
因此 $T,T_s,T_\phi,T_{\phi\phi}$ 具备 (2) 产生 $C^2$ 参数映射所需的连续性。
端层二阶平坦还在数据足够光滑时保更高一阶的径向接合，但本结论不依赖 $F_{sss}$。

由 (2) 得完整六 jet：
$$
\begin{aligned}
F&=P-\int_s^S T\,dt,&F_s&=T,&F_{ss}&=T_s,\\
F_\phi&=P_\phi-\int_s^S T_\phi\,dt,&
F_{s\phi}&=T_\phi,&
F_{\phi\phi}&=P_{\phi\phi}-\int_s^S T_{\phi\phi}\,dt .
\end{aligned}
\tag{33}
$$
这保留了随角变化的完整积分常数。

由于 (28)，core 端准确满足
$F(0)=\Gamma$、$F_\phi(0)=\Gamma_\phi$、
$F_{\phi\phi}(0)=\Gamma_{\phi\phi}$。
若原固定端口为
$$
\Gamma_z=0,\quad T_0(0)=e_z,\quad
T_{0,\phi}(0)=0,\quad T_{0,s,z}(0)=0,
\tag{34}
$$
则
$$
F_s(0)=e_z,\qquad F_{s\phi}(0)=0,\qquad F_{ss,z}(0)=0.
$$
这些正是中圈反射所需的全部二阶匹配：对负半边使用
$F_-(s,\phi)=Q_zF_+(-s,\phi)$，
$Q_z=\operatorname{diag}(1,1,-1)$，
六 jet 在零处逐项匹配，而不只检查位置闭圈。

若原帽端为
$T_0(S)=-e_r(\theta_0)$、$T_{0,s}(S)=0$，则
$$
\begin{aligned}
F(S)&=R e_r+H e_z,&
F_s(S)&=-e_r,&F_{ss}(S)&=0,\\
F_\phi(S)&=R\rho_0 e_\theta,&
F_{s\phi}(S)&=-\rho_0 e_\theta,&
F_{\phi\phi}(S)&=R(\rho_0'e_\theta-\rho_0^2e_r).
\end{aligned}
\tag{35}
$$
支持严格在内部，因此这些帽端 jet 没有由新层改动。沿原 Cartesian 平帽参数化接合时保准确 $C^2$ 端口。式 (34)–(35) 仍只是参数映射的端口结论，不替代全局 immersion 或 embedding。

## 10. 同一固定目标的三 Gram 与明确未解部分

准确单位速度给
$$
E=|F_s|^2=1 .
$$
但固定材料图中的其余两个分量是
$$
B=\frac{T\cdot F_\phi}{\rho_0},\qquad
C=\frac{|F_\phi|^2}{\rho_0^2},
\tag{36}
$$
仍须解 $B=0$、$C=a^2$。对应原相对 Gram 的混合及角向残差是
$B/a$ 和 $C/a^2-1$。
这里不能把当前 core 的 $\rho_c$ 换进目标分母，也不能把 (36) 的角均值当成原固定 $a$。

仅 $E=1$ 甚至不能单独推出 immersion；$F_\phi$ 仍可能退化或平行于 $T$。
全角闭合、反射和帽端 $C^2$ 也不自动推出无自交、全像 $D/L$ 幅度界、正 reach、非平面性或含反射 Euclidean 商非零。

同样，辅助均值迭代、$\lambda$ 和后面的种子投影参数都不是物理弯曲相位。
只有当同一个固定度量的其余方程和全部同场条件真正支付后，才可消费既有连续相位族机制；本文没有产生一个已满足课题全部标准的 physical flex。

## 11. 一个更强的正高度与单一 SO(3) 图条件

一般构造 (19)–(28) 已有完整闭合，但中央 $T_z$ 不一定非负。
如果另能选
$$
0<\bar\lambda<\arcsin\zeta,\qquad
(1-4\epsilon)\cos\bar\lambda+4\epsilon<r_-,
\tag{37}
$$
则
$a_\epsilon(\bar\lambda)\le
(1-4\epsilon)\cos\bar\lambda+4\epsilon<r_-$，
所以所有角的解均满足 $\lambda<\bar\lambda$。

由 $w\perp d$，$|w_z|\le\sqrt{1-d_z^2}$。
于是整个中央段
$$
T_{c,z}\ge
\zeta\cos\bar\lambda-\sqrt{1-\zeta^2}\sin\bar\lambda>0.
\tag{38}
$$
端层为两个非负高度方向的正归一化插值，因此 $T_{b,z}\ge0$。
若外部 $T_{0,z}\ge0$，且它在每个非空开子区间有正积分，
则所有 meridian 的 $z(s,\phi)$ 严格增加。
这个附加输入并不由仅 $T_{0,z}\ge0$ 自动推出。
单条 meridian 的高度严格单调也不等于不同角的整张参数映射全局单射。

条件 (37) 有一个便于预判的严格充分极限：
$$
\frac{k_-}{L}>
 \sqrt{1-\left(\frac{k_z}{k_+}\right)^2}.
\tag{39}
$$
若 (39) 成立，可先在
$\arccos(k_-/L)<\bar\lambda<\arcsin(k_z/k_+)$
选定角度，再取足够小的共同 $b,\epsilon$，由连续性保 (37)。
本文没有声称 actual 输入已经满足 (39)。

若中央正高度界 (38) 成立，且整个支持上 $T_{0,z}\ge0$，
中央 $T$ 与 $T_0$ 一致避开反向；端层也由 (13) 避反向。
可取完整最短旋转图
$$
\omega(s,\phi)=
 \frac{\operatorname{atan2}(|T_0\times T|,\,T_0\cdot T)}
      {|T_0\times T|}\,(T_0\times T),
\tag{40}
$$
在 $T=T_0$ 处用连续极限。由于没有 $T=-T_0$，该图光滑且
$\exp([\omega]_\times)T_0=T$、$|\omega|<\pi$。
在支持外 $\omega=0$；支持端因 $T=T_0$、$T_s=T_{0,s}$，
还保 $\omega_s=0$。
按 (29) 的反射，叉乘给
$\omega(s,\phi')=\det(Q)Q\omega(s,\phi)$，
恰是原轴向旋转变量的变换规律。

如果 (37) 未支付，则一般单位闭合构造仍成立，但 (40) 的全域单图覆盖不能自动继承；必须另付真实非反向域或采用明确不同的旋转图输入。不能在反向点剪裁来假装同一准确场。

## 12. 形状导数成本与有限求解空间的边界

薄端层有明确代价。令 $M_0$ 包围端层上的 $|T_{0,s}|$。
由 $\max S_5'=15/8$ 和 (13)，
$$
|T_{b,s}|\le\frac{M_0+15/(4\delta)}{\nu}.
\tag{41}
$$
设中央长度 $\ell_{\alpha,c}=\ell_\alpha-2\delta$。
由 (20)，
$$
|T_{c,s}|
 =|\lambda\,\partial_s h_\epsilon|
 \le\frac{15\pi}{16\epsilon\,\ell_{\alpha,c}},
\tag{42}
$$
若使用 (37)，可将分子中的 $\pi/2$ 换成 $\bar\lambda$。
这说明只为收缩取非常小的 $b$ 或 $\epsilon$ 可能造成很大的导数上界，
不应把准确闭合误写成几何可用性。上界很大本身也不证明真实曲率失败；
它只是不够强的几何信息。

式 (40) 是一个完整连续初始旋转场，不等于已经处于当前固定
$M=160$、923 节点共享 quintic 的有限表示中。
若要用作实际全变量求解输入，应在明确准确域与当前完整材料图上构造它，
再将其投影/拟合到原全 Fourier 与全部共享节点 jet 空间：
全部原 free core、全部原 rotation 槽和 $H$ 仍保留为求解变量。
不得把生成 seed 时给定的 core/H 值误变为之后固定不动的自由量，
也不能只保少数构造参数就声称原全空间。

投影后的物理场是新的数值候选。它的真实端点残差、原全部三 Gram、
几何、幅度与全部历史地址必须重新读取；
精确 seed 的 $E=1$ 或 (28) 不能未经误差账搬给它。
固定原网格若不能表示需要的端层，必须明确改变初始输入或在同一目标下
作有身份的径向/角向精化，不能用降低观测密度掩盖未表示的形状。

本机制没有更换 $a$ 或目标度量。它改变的是求解的初始 meridian 形状，
通过完整单位积分构造先付闭合；这与只在旧固定两/三 bubble 形状中换
控制尺度或线性预条件不同。但它也没有证明某一个旧有限控制选枝会接受
该投影后的候选，或其外层求解一定收敛。

## 13. 完整条件构造定理与实现合同

**定理。** 假设第1节的准确输入、正则性和共同支持满足 (4)，端层参考
$T_{0,z}\ge0$，并选择满足 (6)–(8) 的共同 $b$ 和满足 (19) 的
$\epsilon$。则 (10)–(28) 构成唯一指定均值分支的全角单位 meridian
$T$，它在支持外等于原 $T_0$，满足 (3)，并由 (2) 产生端点准确闭合、
径向 Gram 准确为一的 $C^2$ 参数候选。数据若满足 (29)，则完整周期及
反射同支成立；原端口若满足 (34)–(35) 的输入，则保全部 core/cap
二阶接合。若再有 (37) 及相应全域半球条件，则有 (38) 的中段正高度
和 (40) 的完整旋转图。

**证明。** (11)–(16) 保证端层归一化无零、共同闭球自映且收缩；
完整迭代给唯一 $v$ 和 (18) 的导数逆界。式 (20) 的准确反对称性
消掉全部中段正弦积分，(21)–(24) 唯一确定幅度且其导数不退化，
故 (27)–(28) 精确满足三个积分分量。正则性和 (30)–(33) 给完整
二阶物理 jet；共同域的唯一性给 (29) 的全角关联。支持在内部且端层
平坦，故六端口按 (34)–(35) 逐项匹配。最后 (37)–(40) 给所述加强结论。
证毕。

真正的后继 producer 应保存以下准确输入与实际责任：

1. 实际 reference/scalar/core/chart/$H$ 的完整身份，准确 $S,U,b,\epsilon$；
2. $K$ 的完整定义以及所采用的 $k_-,k_+,k_z,\nu,q,r_\pm$ 的真实来源；
3. 均值迭代的完整三向量、实际残差与误差，唯一分支的共同选择；
4. 准确 $a_\epsilon$ 定义、幅度分支、所有端层/中央积分和角 jet；
5. 连续 seed 到完整有限自由点的真实映射、未付费用和新候选摘要；
6. 全部历史物理地点在新场上的真实重读以及原全部求解/几何条件。

这些是一个完整候选生成机制的合同，不是新添到正在运行科学方向前的
额外 fixture。现有输入缺某项正隙时，只能说本文这组充分条件未被支付；
不能据此宣布其它单位闭合形状不存在，更不能终止课题。
