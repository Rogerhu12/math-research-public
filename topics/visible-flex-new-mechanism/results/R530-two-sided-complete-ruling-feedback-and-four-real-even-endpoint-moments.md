# R530：同一正交库的双边完整反馈与四个真实偶端矩

日期：2026-11-16。**原式纸证与有限维实际 ODE 构造；没有执行 profile 求积、符号程序、数值射击、秩计算或开发检查。**

本文继续 [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md) 的同一个实际母库。此前从原八矩可见：若 $h$ 为偶函数而 $k,\omega-\omega_c$ 为奇函数，四个独立奇坐标的总矩自动为零。但仅拟定这种几何，不能保证原完整第四 ruling 为零。

本文把该奇偶支架真正接入原 ruling：对正、负两半同时保留各自真实第二、第三累计，用两条完整 $K=0$ 方程共同解两个加速度。它们的系数行列式在一个从起点确定的合法紧域内严格为正。于是得到实际、光滑、非恒 $k$ 的两侧路径，不假定 profile 空间反射，也不删除原 $YC$ 或第三历史。

中心允许四个原 E8 奇坐标。它们可用一个小长度 IFT 准确清除左右端的共同奇累计，留下同一真实路径上的四个偶端矩
$$
p_1,\quad t_1,\quad r_1,\quad s_0.
$$
小长度并不能使它们全零；其中 $t_1$ 有严格负首项。因此本文给出的是一份已经满足整段完整 ruling 的实际返回候选族及其四个准确末端方程，不宣称矩阵零块已经构造。有限长度的四根、两端完整 germs、pose 和第四 period 仍须继续。

## 1. 固定真实库与共同合法状态域

保持 R521 的第一圆、所有正幅副本、位置、右锚及原物理区间：
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
\tag{1}
$$
使用 R521/R523 已付的三个二阶矩、全部第三 ruling 及任意固定原 E8 算子 $E$ 的交叉矩：
$$
\mathbf I(D_\theta)=0,\qquad
I_j\{\phi_\theta,\Phi_E(D_\theta)\}=0,\quad j=0,1,2 .
\tag{2}
$$
后一式由每完整基本块的原八副本第七差分支付，保原 $I_2$ 的额外一阶项与所有真尾。它不是本稿新增的满秩假设。

选择一次常数 $\omega_c$，仅为原算子记号令
$$
y=x+\omega_c,\qquad \eta=\omega-\omega_c .
\tag{3}
$$
这是同一实际 profile 和右锚的固定坐标记法，不在途中平移 profiles。$y$ 的右锚是原右锚加 $\omega_c$。

在构造 profiles 时就选定一个对 $k,\eta$ 变号封闭的紧状态盒，使对两种符号
$$
S_\pm=(h,\pm k,\omega_c\pm\eta)
$$
及全部实际和参考微包都有
$$
h\ge h_*>0,\qquad
z_\pm=x+\omega_c\pm\eta>0,
$$
$$
e_\pm=h z_\pm\mp k>0,\qquad
h^2z_\pm^2>1+k^2 .
\tag{4}
$$
所有不等式有共同严格余量。若从起点可选共同正窗口，足够靠右的有限窗口可以满足一个预定有限参数盒的(4)。这不授权移动一个已经冻结而不满足(4)的库。

R521 的完整式为
$$
\mathscr K=\sin^2\theta
\{\mathcal F(S,\gamma,\upsilon,A,T)
+C_h(S)h_{ss}+C_k(S)k_{ss}\}.
\tag{5}
$$
$A=\Phi_{\mathsf m}$，$T$ 是完整三槽第三累计；$\mathcal F$ 包含全部 $YC$、变化-profile chain、左右尾及原历史。

由 R521(30)及 R523(17)，在(4)中严格有
$$
\boxed{C_h(S_\pm)<0,\qquad C_k(S_\pm)>0.}
\tag{6}
$$
这些系数不含 $A,T$ 或当前速度。因库和紧域固定，四个绝对值各有共同正下界。

## 2. 同一个第三 Gram 与完整中心字段

先固定一个参数向量 $\nu\in\mathbb R^3$。原 R47 的 Gram 右逆可选一条双 collar 紧的 $\chi_\theta^\nu$，使
$$
\mathbf I(\phi_\theta,\chi_\theta^\nu)
=\sin^2\theta\,\nu.
\tag{7}
$$
它对全相位光滑、周期，并在两个 seed 为零。整个两侧区间只使用这一条固定 profile，不沿路径调整。

第三规范对(5)的影响只是把其括号中的无加速度项改成
$$
\mathcal F_\nu
=\mathcal F-2\mathbf w(S)\cdot\nu,\qquad
\mathbf w(S)=
\left(\frac{1+(h\omega-k)^2}{4h},
\frac{h\omega-k}{2},\frac h4\right),
\tag{8}
$$
这里 $\mathbf I$ 与 $\mathbf w$ 采用同一个坐标；若使用(3)的 $y$ 坐标，则同时按原三矩平移公式变换 $\nu$，物理配对不变。

暂以区间中心 $s=0$ 记第二、第三累计。取
$$
h(0)=H>0,\quad k(0)=\eta(0)=0,\quad
\gamma(0)=0,\quad \upsilon(0)=v_0,
$$
$$
A_+(0)=A_-(0)=A_0,\qquad T_+(0)=T_-(0)=0 .
\tag{9}
$$
$A_0$ 将在第5节限制到四维奇子空间。此时不是把一个未实现的中心矩阵称为原左零锚；第7节会完整改回真实左端。

中心字段的合法性可以直接按原规范解释。在中心另记 canonical 第二累计 $A^{\rm can}(0)=0$，一次取其固定第二规范
$$
w_\theta^{\rm cen}=A_0D_\theta .
\tag{10}
$$
由(2)和原 E8 左尾表，它是真紧并满足三条第三 ruling 交叉条件。若写
$$
A^{\rm can}=A-A_0,\qquad
T^{\rm can}=T+(A-A_0)\circ A_0,
$$
则
$$
A^{\rm can}D+w^{\rm cen}=AD,
$$
$$
-2T^{\rm can}(\phi;D)
+2A^{\rm can}(\phi,w^{\rm cen})-\chi^\nu
=-2T(\phi;D)-\chi^\nu .
\tag{11}
$$
因此中心的非零 $A_0$ 只是同一个合法固定第二规范的精确记法。所有有序复合均为
$(E_1\circ E_2)(a;b,c)=E_1\{a,E_2(b,c)\}$，不是矩阵乘法。

## 3. 双边的真实速度、加速度与两个 ruling

在 $s\ge0$ 使用变量 $h,k,\eta,\gamma,\upsilon$，满足
$$
h_s=\gamma,\qquad k_s=\upsilon,\qquad
\eta_s=\frac{\upsilon}{2h}.
\tag{12}
$$
它们定义正半段以及拟拼出的负半段 scalar 值
$$
S_+(s)=(h,k,\omega_c+\eta),\qquad
S_-(s)=(h,-k,\omega_c-\eta).
\tag{13}
$$
负半段的实际物理参数是 $\sigma=-s$。因此它的**实际**速度和加速度为
$$
(\gamma_-,\upsilon_-)=(-\gamma,\upsilon),
\qquad (h_{\sigma\sigma},k_{\sigma\sigma})_-=(a,-b),
\tag{14}
$$
而正半段为 $(\gamma,\upsilon)$、$(a,b)$，其中
$a=\gamma_s,\ b=\upsilon_s$。

两半仍用相同的物理 profiles、右锚与 $\chi^\nu$。分别代入原完整式(5)(8)，得到
$$
\begin{pmatrix}
C_h(S_+)&C_k(S_+)\\
C_h(S_-)&-C_k(S_-)
\end{pmatrix}
\begin{pmatrix}a\\ b\end{pmatrix}
=
-\begin{pmatrix}
\mathcal F_\nu(S_+,\gamma,\upsilon,A_+,T_+)\\
\mathcal F_\nu(S_-,-\gamma,\upsilon,A_-,T_-)
\end{pmatrix}.
\tag{15}
$$
其真实行列式为
$$
\boxed{
\Delta=-C_h(S_+)C_k(S_-)-C_h(S_-)C_k(S_+)>0.
}
\tag{16}
$$
若两种 $|C_h|$ 的下界为 $c_h>0$，两种 $C_k$ 的下界为 $c_k>0$，则
$\Delta\ge2c_hc_k$。

故(15)给唯一光滑的真实 $(a,b)$。这个可逆性不需要两个 profiles 在空间反射后相同，也没有把正半段的 ruling 用某个未付对称性代替负半段的 ruling。

### 完整第二、第三累计的正反时号

令 $M_\pm$ 是在(13)(14)的实际速度上计算的原 $M_{\rm raw}$，令
$\mathcal C_\pm$ 是同样代入实际加速度 $(a,b)$、$(a,-b)$ 后的 R73(16)完整三槽密度。正半段满足
$$
(A_+)_s=\Phi_{M_+},\qquad
(T_+)_s=-\Phi_{M_+}\circ A_++\mathcal C_+ .
\tag{17}
$$
负半段的数据以正变量 $s$ 记录，而其物理时间为 $-s$，故必须是
$$
\boxed{
(A_-)_s=-\Phi_{M_-},\qquad
(T_-)_s=+\Phi_{M_-}\circ A_--\mathcal C_- .
}
\tag{18}
$$
(18)不是另起一条正向、零历史的路径。它准确记录同一个中心初值向左的原解；尤其两个第三项的号都不能省略。

$\mathcal C_\pm$ 对 $a,b$ 至多仿射。将(15)代入(12)(17)(18)，得到通常的有限维光滑 ODE。$T_\pm$ 可用 R521 §1 的同一个有限原算子生成空间表示；允许冗余，但不把其系数当作新的独立控制。全局范围是：只要实际解留在(4)及有限速度、历史盒内，就按同一方程延拓。

## 4. 中心全 jets 光滑：由双边 ODE 交换对称支付

不能只检查 $k''(0)=0$ 后就宣称左右所有导数已经匹配。这里有完整的 ODE 对称证明。

在双边状态上定义
$$
\mathfrak J:
(h,k,\eta,\gamma,\upsilon,A_+,A_-,T_+,T_-)
\longmapsto
(h,-k,-\eta,-\gamma,\upsilon,A_-,A_+,T_-,T_+).
\tag{19}
$$
变换后，(15)的两条方程互换，且实际解出的加速度变为
$$
a\longmapsto a,\qquad b\longmapsto-b.
$$
(17)(18)也恰按交换及时间倒向互换：这里用的是它们已显示的正反时号，不需要另假 $\mathcal C_+$ 与 $\mathcal C_-$ 之间存在某个空间反射恒等式。

因此若 $X(s)$ 解双边 ODE，$\mathfrak J X(-s)$ 也解同一个 ODE。(9)在 $\mathfrak J$ 下固定，普通解的唯一性给
$$
X(-s)=\mathfrak J X(s).
\tag{20}
$$
将整个物理段定义为：$s\ge0$ 取正半段，$s\le0$ 取负半段在 $-s$ 的值。由(20)，它在中心为 $C^\infty$，所有 jets 均匹配，并严格满足
$$
\boxed{
h(-s)=h(s),\qquad
k(-s)=-k(s),\qquad
\omega(-s)-\omega_c=-(\omega(s)-\omega_c).
}
\tag{21}
$$
完整 $A,T$ 也按两侧原 ODE 光滑接上。第三规范没有改变。

在中心两条 ruling 的状态完全相同，故(15)直接给
$$
b(0)=0,\qquad a(0)=-\mathcal F_\nu(X_0)/C_h(S_0).
$$
若选 $v_0\ne0$，实际曲率参数具有
$$
k(s)=v_0s+O(s^3),\qquad
\omega(s)-\omega_c=\frac{v_0}{2H}s+O(s^3),
\tag{22}
$$
所以该族的 $k$ 真正非恒并穿过零，不是常态例子的改名。

由(15)，两半、全相位、整区间的完整第四 ruling 均准确为零。局部存在给一个正而有限的长度 $L$；本文不以局部定理保证任意长的解都留在合法域内。

## 5. 原八矩的四奇四偶分解

本节只用真实几何(21)和 R73 的原八矩，不对 profiles 施加 $y\mapsto-y$ 反射。

在固定 $y$ 坐标中记
$$
d=h\eta-k,\qquad
d_s=\gamma\eta-\upsilon/2,\qquad Q_d=1+d^2.
$$
按(21)，$h,d_s,\upsilon,Q_d$ 为偶，$k,\eta,\gamma,d$ 为奇。原
$$
K_0=ky^2+a_1y+a_0,\quad
a_1=2k\eta-(k^2+1)/h,\quad
a_0=k\eta^2-(k^2+1)\eta/h
$$
的系数奇偶分别为奇、偶、奇。

将其代入 R73(9)(10)，八个独立坐标恰为
$$
\begin{array}{c|c}
\text{独立奇坐标}&p_0,\ p_2,\ r_0,\ s_1\\
\text{独立偶坐标}&p_1,\ t_1,\ r_1,\ s_0 .
\end{array}
\tag{23}
$$
例如
$$
p_0=-\frac{k(1+d^2)}{2h},\quad
p_1=-kd,\quad p_2=-kh/2,
$$
$$
r_0=\frac{a_0Q_d+(d_s/h^2)(\gamma Q_d/h-2dd_s)}{8h},
$$
$$
s_1=\frac{a_1d-(\gamma/h^2)d_s}{4}.
$$
这些式子直接核出(23)。原 trace 关系
$$
t_0=p_0/4+s_1/2
$$
说明 $t_0$ 也是奇坐标的组合，**不增加第五个独立奇维**。

令 $E_{\rm o},E_{\rm e}$ 为这两个四维子空间，$\mathcal P$ 在偶子空间为 $+1$、奇子空间为 $-1$。则
$$
M_-=\mathcal P M_+ .
\tag{24}
$$
现在限制中心矩阵参数 $\mathsf a$ 在 $E_{\rm o}$，并令 $A_0=\Phi_{\mathsf a}$。由(17)(18)，在矩阵系数层准确有
$$
\boxed{\mathsf m_-(s)=-\mathcal P\mathsf m_+(s).}
\tag{25}
$$
特别，令
$$
O_L=\operatorname{pr}_{E_{\rm o}}\mathsf m_+(L),\qquad
E_L=\operatorname{pr}_{E_{\rm e}}\mathsf m_+(L),
$$
则两个真实中心累计端值是
$$
\mathsf m_+(L)=O_L+E_L,\qquad
\mathsf m_-(L)=O_L-E_L .
\tag{26}
$$
因此从左到右的原总矩阵为
$$
\boxed{M_{\rm tot}=2E_L.}
\tag{27}
$$
四个奇坐标的总积分在任何存在长度上自动为零；它们的共同端入值 $O_L$ 仍须另保，不能自动叫作零锚。

## 6. 四个中心参数准确清共同奇端值；四偶根仍未付

把(9)的 $H,\omega_c,v_0,\nu$ 放在一个固定小参数盒中。对充分小的 $L$，定义真实端映射
$$
\mathscr O(\mathsf a,L;H,\omega_c,v_0,\nu)
=\operatorname{pr}_{E_{\rm o}}\mathsf m_+(L).
$$
它由完整双边 ODE 定义，而非一个静态密度替代。于 $L=0$，
$$
\mathscr O(\mathsf a,0;\cdots)=\mathsf a,\qquad
D_{\mathsf a}\mathscr O=I_{E_{\rm o}} .
\tag{28}
$$
有限维 IFT 因而给唯一邻近的真实 $\mathsf a(L;\cdots)$，使
$$
\boxed{O_L=0.}
\tag{29}
$$
原奇密度在中心为零，且关于 $s$ 为奇，所以
$\mathsf a(L;\cdots)=O(L^2)$。固定有限库与参数盒后，该估计及导数界由同一 ODE 光滑依赖得到。

这只在小 $L$ 的上述分支上支付(29)。到有限较大长度，须继续跟踪该真实端映射及其中心参数；本文不假定其四阶 minor 永不退化。

在(29)后，
$$
\mathsf m_+(L)=E_L,\qquad
\mathsf m_-(L)=-E_L,
$$
故矩阵零目标准确缩为同一条已经 $K=0$ 的路径上的
$$
\boxed{
E_L=(m_{p_1}(L),m_{t_1}(L),m_{r_1}(L),m_{s_0}(L))=0.
}
\tag{30}
$$
这里没有新的实际 rank 断言，也没有把(28)移用成(30)满射。

### 小长度严格不是矩阵零解

中心有 $k=d=\gamma=0$、$d_s=-v_0/2$。R73 给四个偶密度
$$
(M_{p_1},M_{t_1},M_{r_1},M_{s_0})_{s=0}
=\left(0,-\frac18,-\frac1{8H^2},
-\frac{v_0^2}{16H^2}\right).
\tag{31}
$$
由它们的偶性，
$$
E_L=L\left(0,-\frac18,-\frac1{8H^2},
-\frac{v_0^2}{16H^2}\right)+O(L^3).
\tag{32}
$$
特别，充分小的正 $L$ 有 $m_{t_1}(L)<0$。所以(29)的真正局部构造没有暗中制造一个矩阵零块；(30)须在有限幅值、有限长度的后继分支中实际求解。

## 7. 从中心累计改回真实左端：同一个 $w,\chi$ 的完整式

固定一条已经选定的有限路径及其 $L$。置
$$
B=A_-(L),\qquad T_\ell=T_-(L).
$$
从真实左端 $-L$ 采用 canonical 零历史，记为 $\widehat A,\widehat T$。R73/R526 的有序入历史公式严格给
$$
\boxed{
\widehat A=A-B,\qquad
\widehat T=T-T_\ell+\widehat A\circ B .
}
\tag{33}
$$
微分第二式得到
$\widehat T_s=-A_s\circ\widehat A+\mathcal C_s$，且左端值为零；因此这个交叉项既保号也保槽次序。

对最终正向运行的全段一次固定
$$
\boxed{
w_\theta=B D_\theta,\qquad
\chi_\theta=\chi_\theta^\nu+2T_\ell(\phi_\theta;D_\theta).
}
\tag{34}
$$
于是
$$
\widehat A D+w=AD,
$$
$$
\begin{aligned}
-2\widehat T(\phi;D)+2\widehat A(\phi,w)-\chi
={}&-2T(\phi;D)+2T_\ell(\phi;D)
-2\widehat A(\phi,BD)\\
&+2\widehat A(\phi,BD)-\chi^\nu
-2T_\ell(\phi;D)\\
={}&-2T(\phi;D)-\chi^\nu .
\end{aligned}
\tag{35}
$$
因此原完整第二、第三字段逐字保持，最终真实左零锚路径仍满足整段完整 $K=0$。

### 原规范与两 collar 合法性

$BD$ 的紧性及三条交叉矩由(2)直接给出。中心表示(10)(11)中的 second 规范已合法，故每完整块的 third forcing 仍满足原全部第三 ruling。块外二阶字段为零；原 R56 中第三 $P$ 的左尾就是该完整第三 ruling，也为零，$B$ 及局部项同为零。因此去掉原紧 $\chi^\nu$ 后，真正第三 scalar 输出 $T_s(\phi;D)$ 在两外 collars 为零。其中心入值 $T(0)=0$ 已显示保留，不能把任意额外非紧第三入值一并消去。

特别 $T_\ell(\phi;D)$ 真紧，(34)是允许的第三齐次 profile。其相位光滑、周期；$D$ 在两个 seed 为零，原 $\chi^\nu$ 也保 seed，所以两条最终规范均保种子。

(34)在整条选定路径上固定一次。若改变 $L$、中心参数或控制分支，所需的 $B,T_\ell$ 一般改变；本稿不宣称整个参数盒已共享同一个重锚后的规范。若后继要求在一条固定最终规范下继续变动参数，须把相应(34)端数据也纳入真实端映射。

### 四偶根的准确收益

在(29)分支，$B=-\Phi_{E_L}$。因此若最终(30)成立，
$$
\widehat A(L)=0,\qquad B=0,\qquad w_\theta=0 .
\tag{36}
$$
这会得到一条同一固定 $\chi$、完整 $K=0$、真实 $M=0$ 的段。原第三端口仍是
$$
T_{\rm tot}=T_+(L)-T_-(L)-2\Phi_{E_L}^{\,2}.
\tag{37}
$$
特别在(30)上，它是 $T_+(L)-T_-(L)$，并未被本文设零。若再满足 [R526](R526-real-incoming-history-reversal-and-one-gauge-endpoint-completion.md) 的真实两端反射 germs，则其实际倒行及真正入历史可清除第三端口；不能在尚未支付 germs 时直接拼接。

## 8. 剩余两矩的完整原式与真实面积条件

本节给(30)中后两项的可直接使用形式，保其速度项。仍在固定 $y$ 坐标，令
$$
a=h_s/h,\qquad d=h\eta-k.
$$
原 R73 给
$$
\boxed{
8M_{r_1}
=h^{-2}\{(2kd+k^2-1+a^2)(1+d^2)-2a\,d\,d_s\},
}
\tag{38}
$$
$$
\boxed{
4M_{s_0}
=h^{-2}\{d(d+k)(kd-1)-d_s^2\}
=\frac{k\eta(1+d^2)}h-\eta^2-(a\eta-\eta_s)^2.
}
\tag{39}
$$
这些式子在本稿的实际反馈路径上评价；没有把 $h,k,\eta$ 再改为任意可选函数。

即使 $p_1,t_1$ 两个总矩已经为零，(38)(39)也不自动为零。给一个精确的剩余正面积门：从真实左端令
$$
P_0(s)=\int_{-L}^s M_{p_0}(t)\,dt,\qquad
M_{p_0}=-\frac{k(1+d^2)}{2h}.
$$
总奇矩已零，故 $P_0(-L)=P_0(L)=0$。对(39)只作一次真实 IBP，得到
$$
\boxed{
4\int_{-L}^{L}M_{s_0}
=2\int_{-L}^{L}P_0\eta_s
-\int_{-L}^{L}\{\eta^2+(a\eta-\eta_s)^2\}.
}
\tag{40}
$$
边界是原 $[-2P_0\eta]_{-L}^{L}=0$。所以 $s_0$ 返回需要实际累计 $P_0$ 与真实 $\eta_s=k_s/(2h)$ 支付右边的非负量。这没有引入可逐点指定的第三或矩阵控制，也不由零端值取消内部面积。

(38)(40)与(30)一起给有限幅值研究的准确目标。小长度负首项(32)、R524 的全矩阵必要界及当前反馈均须同时保留；本文不把任一无约束的八矩配平曲线当作已经满足(15)。

## 9. Frame、完整端 germs 与第四累计仍另保

本稿的中心交换只保证(21)，不保证 $s=\pm L$ 各自是反射中心。一般有
$$
h^{(j)}(-L)=(-1)^j h^{(j)}(L),\quad
k^{(j)}(-L)=(-1)^{j+1}k^{(j)}(L),
$$
以及 $\eta$ 与 $k$ 相同的奇偶关系。两端完整 germs 尚未闭合，不能只因中心光滑或两个高度相等而应用倒行拼接。

纯几何上可以把 pose 也准确保账。令
$$
D_B=\operatorname{diag}(-1,-1,1).
$$
原 frame 矩阵满足
$D_B\Omega(k)D_B=-\Omega(-k)$。以中心 $F(0)=I,\alpha(0)=0$ 归一，(21)给
$$
F(-s)=D_BF(s)D_B,\qquad
\alpha(-s)=D_B\alpha(s).
\tag{41}
$$
所以若 $G=F(L),v=\alpha(L)$，总相对 frame 是 $D_BG^tD_BG$；ambient 端差是 $(I-D_B)v$，从真实左端 frame 读取的相对平移则是
$
(D_BG^tD_B)(I-D_B)v.
$
两种位移的零门等价，但坐标记法不同，不能由(27)推返回。

(41)仅是几何关系。因为本稿没有在 profile 空间作反射，完整 $Y,Z,W$ 不因此自动具有 R523 的字段奇偶。故第四 characteristic 累计必须原样保留为
$$
\boxed{
V_{\rm tot}(x,\theta)
=\int_0^L\{\mathcal R_{4,+}(s,x,\theta)
+\mathcal R_{4,-}(s,x,\theta)\}\,ds.
}
\tag{42}
$$
两项均在各自实际正向物理 jet 上计算。本文不将(42)写成某个半段的两倍，也不宣称其为零。所有后继 prototype、桥、倒行及真实成本都须从(42)继续。

## 10. 本稿完成的实际步骤

当前 R521 库中的新步骤是：完整 $K=0$ 已在两个实际半段**同时**求解，中心全 jets 光滑及 $h$ 偶、$k,\eta$ 奇由同一个双边 ODE 的唯一性严格保证。这不是先任意挑一条奇偶几何再漏查 ruling。

中心四个原 E8 奇参数确属合法第二字段；小长度 IFT 准确清共同奇端值，原八矩返回由此缩为同一实际路径的四偶端矩。真正左端零锚、固定 $w,\chi$、全第三交叉和 collars 由(33)–(35)统一恢复。

仍未支付的是有限长度的(30)及实际端 germs、pose、整个(42)与后续 period/十三规范。四偶根若能在这同一个分支上达到，就直接得到 $M=0,w=0$ 的候选段，而不需另独立把中心第三入值或半段第三端口设零；但它不能被另一个母库、另一条无 ruling 桥或分别存在的规范替代。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(9)–(17)：八矩、trace、变化-profile chain 与完整有序第三累计；
- [R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) §5、R523(24)：同一完整八副本与 E8 第二规范的真实 cubic 交叉矩；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 未消历史的(23)(24)：完整字段 $q,b$ 及 ruling；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)、[R523](R523-real-reflection-segments-one-fixed-gauge-and-exact-third-endpoint-transfer.md)：同一有限库、完整相位合成、$C_k>0$ 与强窗口中的 $C_h<0$；
- [R526](R526-real-incoming-history-reversal-and-one-gauge-endpoint-completion.md)：原入历史、同规范重锚及矩阵零段的准确完成范围。

所有结论按本稿原式证明；没有新增研究执行或以单独的维数计数代替实际端点控制。

