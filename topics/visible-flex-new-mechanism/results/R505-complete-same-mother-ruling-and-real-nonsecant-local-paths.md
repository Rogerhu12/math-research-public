# R505：完整同形母库的单能量 ruling、同一第三规范下的真实非正割局部路径

日期：2026-11-16。**新的完整纸面构造；没有执行 profile 求积、原根恢复、符号运算、数值秩、开发检查或科学任务。**

本文接 [R503](R503-nonzero-prefix-reflection-and-one-gauge-for-complete-secant-patches.md) 的非零真实前缀比较，转向原非正割段内部的完整第四 ruling。新增结果不是再给一个必要障碍：从起点选取一个明确的同形母包圆后，可以用一个固定的第三规范构造实际、非正割、非恒曲率的局部几何路径，在整个局部区间和全部相位上准确满足完整第四 ruling。

关键是证明一条完整函数身份。该新圆上的全部 $Y$–third 配对，包括原有序尾及真实第三历史，准确消失；完整 second square 则准确只带一个 $\sin^2\theta$ 因子。因此实际约束下降为一个非负能量与同一个第三 Gram 向量的等式，而非逐相位分别选控制。

本文进一步给出：先用同一个第三规范支付一条中心清理的参考正割段，随后在另一个明确的实际状态上得到正则非正割控制入口。参考正割点本身的两条速度一导恰好为零，故不能用后者的正则性冒称已经构造了从参考正割段出发的连接桥。末节另外给同一局部控制族中保两端完整 germs 与有限阶全部传递数据的真实非平凡变形；其端口由这族实际产生，尚不是任意指定闭词端口。

## 1. 一次固定的新库、原恢复与准确适用范围

固定共同物理区间 $I=[\ell,r_*]$、右锚
$$
Jv(x)=\int_x^{r_*}v(t)\,dt .
$$
几何仍为原实际带
$$
X(s,u_{\rm ph})=\alpha(s)+u_{\rm ph}N(s),\qquad
\alpha_s=h^2T,
$$
$$
T_s=kN,\quad N_s=-kT-B,\quad B_s=N,\qquad
h>0,\quad \omega_s=\frac{k_s}{2h},\quad x+\omega>0.
\tag{1}
$$
所有 $s$ 导数固定原 $x$，不重新移动 profiles 或积分锚。

先选任意非零实偶 $C^\infty$ 紧母包，并把一个固定正宽度收入母函数。以下每一个最细微包均为这个母函数的**字面平移**。幅度属于实际 $f,g$ 系数，不能把不同幅宽归一混作同一个 self 值。

采用 [R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md) 的两个实际等距编码，并依次保留原完整八副本、十二翻号副本及五个正权 block。这里消费 R280 §§1–7 的布局和面积构造，**不执行其第8节的不同母形高阶纤维替换**。所有相对位置、幅度、共同窗口都在本稿路径及规范选择时固定。

在每一个最初等距编码中，
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
b_i^2=B_0>0,\quad
R_i=a_i^2-B_0,\quad T_i=a_ib_i,
$$
$$
R_i\in\{-B_0/2,8B_0\},\qquad
R_i^2-4T_i^2=\frac{7B_0}{2}R_i,
\tag{2}
$$
$$
\sum_iR_it_i^j=\sum_iT_it_i^j=0\quad(0\le j\le10).
\tag{3}
$$
原三个真实矩为
$$
\boldsymbol\mu(u)=
\left(\int u''{}^2,\ \int xu''{}^2,\
\int\{x^2u''{}^2+2u'{}^2\}\right).
\tag{4}
$$
同形偶母给
$$
\boldsymbol\mu_i=m(1,t_i,t_i^2+\nu),\qquad m>0.
\tag{5}
$$
$\nu$ 保含原 $2u'{}^2$；没有点质量近似。

令
$$
C_\theta=\cos\theta,\quad S_\theta=\sin\theta,\quad
\phi_\theta=C_\theta f+S_\theta g,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{6}
$$
三矩、原八副本的完整第三 ruling 及 hook 不可见性，仍分别来自 R280、[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) §5 和 [R476](R476-full-third-diagonal-kernel-is-invisible-to-disjoint-rank-one-circles.md)。这些是逐实际 $s$ 的身份。若后来要求周期，还必须由同一个真实整词另付 $M=0$ 和第三 period；局部构造本身不声称这些总端点条件。

固定一个原八矩算子 $\mathsf A_g=\Phi_{\mathsf m_g}$，并只用一条第二规范
$$
w_\theta=-\mathsf A_gD_\theta .
\tag{7}
$$
三矩使它双 collar 紧；八副本的原 cubic 身份使它满足同一第三 ruling 合法性。真实当前矩阵满足
$$
\mathsf m_s=M_{\rm raw}(h,k,\omega,h_s,k_s),\qquad
\mathsf A_s=\Phi_{\mathsf m(s)}.
\tag{8}
$$
故真正 second profile 与场是
$$
q_\theta=(\mathsf A_s-\mathsf A_g)D_\theta,\qquad
Z_\theta=K_s(D_\theta)-Y_{q_\theta}.
\tag{9}
$$
$\mathsf m$ 沿整条路径按(8)积分，不是可逐时指定的自由八维函数。存在性可直接取 $\mathsf m_g=0$ 并从原零历史开始；非零 $\mathsf m_g$ 版本保其实际传入，不因 R70 可达而删除到达它的桥内 ruling。

这里没有继承旧 R455/R480 不同最终母的十九、二十目标、全部 rational period 或十三行收据。字面同形是一个新的从起点选择；若以后再换母，必须另证本稿完整 self 数据保持，不能仅以原 $C^2$ 低阶纤维代替它们。

## 2. 完整 self 的共同平移次数确实不超过十

写原分子场
$$
Y_u=FV_Y/(x+\omega),\quad
Z_u=FV_Z/(x+\omega),\quad
C_u=FV_C/(x+\omega).
$$
这里 $C_u$ 是原完整三阶恢复的单包分量，包含原 second history、变化-profile chain、第三历史与固定(7)的作用，尚未加本文另行选择的 $\chi_\theta$。这里的第三入历史始终来自同一原 canonical 路径恢复；若另加一条不在此合同中的独立第三 profile，必须把它纳入固定 $\chi$ 或另付其配对，不能也称为自动消失。

将母包平移后搬回母坐标，位置参数记为 $t$。直接沿 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)(2)、(5)–(7)，各三个分量的次数界为
$$
\begin{array}{c|ccc}
& T\text{ 分量}&N\text{ 分量}&B\text{ 分量}\\ \hline
V_Y&0&-\infty&1\\
V_Z&4&3&5\\
V_C&8&7&9 .
\end{array}
\tag{10}
$$

证明必须包含真实历史。第一行是原
$V_Y=(-u'/2,0,hu-eu'/2)$。二阶 forcing 的四个分子配对次数至多二，故 $P,B$ 至多二；原 $\eta_0$ 至多三，$\mathcal R_H$ 至多四，真实 $s$ 积分的 $W$ 至多四。由
$$
V_{\rm new}=(W_x/2+\eta_0/h,\ (x+\omega)P+B,\
e(W_x/2+\eta_0/h)-hW)
\tag{11}
$$
得到第二行。固定八矩规范的输出次数至多四，其 $Y$ 场也在这一界内。

再将 $Y$ 和完整 $Z$ 配对，四个 forcing 分子均至多六；于是 $P,B$ 至多六，$\eta_0$ 至多七，$\mathcal R_H,W$ 至多八，给第三行。原 $P_s,B_s$、$\nabla_s$、变化-profile 项及从原起点继承的 $s$ 积分均保留；求 $s$ 导数或实际 $s$ 积分不增加这个位置次数。右锚始终在同一个零 collar，换元不产生可以任意删掉的积分常数。

所以紧 outer 的完整单包配对
$$
\int V_Y'\cdot V_C'
\tag{12}
$$
是位置的次数至多十的多项式。对
$$
\frac1h\int_\ell^{r_*}|V_Z'|^2
\tag{13}
$$
还必须保单包左尾。其左分子为 $xU_\mu+V_\mu$，两向量对三矩线性；左 strip 的积分为其真实长度乘 $|U_\mu|^2/h$。按(5)，这一项的位置次数至多五。包内部分由(10)至多十，右侧本来为零。因此(13)也是完整十次多项式，不是只看包内 principal。

同一界适用于完整 base 的共同平移：有限个 self 多项式以及下一节的三矩有序核共同给出。整个证明没有称单包 $Z$ 或 $C$ 左紧，也没有以原 whole-period pure 零删除原函数。

## 3. 完整 $Y$–third 有序项仍只需两组三矩

设 outer 包 $u_i$ 在 inner 包 $u_j$ 左方。原第二场的左分子准确是
$$
V_{Z_j}=xU_{\mu_j}(s)+V_{\mu_j}(s).
\tag{14}
$$
由 [R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md) §§3–4 的原恢复，第三 mixed 场 $C_{ij}$ 局域在第 $i$ 包。其完整原 $\beta_{\mu_j}$ 是二次 $x$ 多项式，系数线性依赖 $\mu_j$，并保真实初值和全部 $s$ history。准确积分身份为
$$
\boxed{
\int V_{Y_i}'\cdot V_{C_{ij}}'
=\frac14\int\{\mathcal A_\beta(u_i'')^2+
\mathcal A_\beta''(u_i')^2\},\qquad
\mathcal A_\beta=he\beta-\frac Q2\beta',\quad Q=1+e^2.
}
\tag{15}
$$
$\deg_x\mathcal A_\beta\le2$，故它是一个真正的
$\Gamma_s(\mu_i,\mu_j)$ 双线性核。

R292 的 closed-path/pure 前提用于其后面的 period 身份；(14)(15)的局部推导只用真实二阶平台方程和同一原锚。本稿使用的是这一逐 $s$ 身份，不是未经支付的全 period 关系。

为明确保存原 $\tau$ 与 Green 项，可用 R405 的完整局部密度式
$$
V_Y'\cdot V_C'
=\frac14(\mathcal A_\beta r^2+\mathcal A_\beta''p^2)
+D_x\left(\frac{\mathcal B_\beta}{4}
+\frac{\tau\mathcal B_\tau}{16h^2}\right),
\tag{16}
$$
其中 $p=u',r=u''$，
$$
\begin{aligned}
\mathcal B_\beta={}&he\beta pr-\frac Q2\beta r^2
+\frac{Q\beta''-2h^2\beta}{2}p^2
-he\beta''up+h^2\beta''u^2,\\
\mathcal B_\tau={}&heQpr-\frac{Q^2}{2}r^2
-2h^3eup+2h^4u^2 .
\end{aligned}
$$
两端 $u=p=r=0$ 使显示边界为零；没有假设右 inner 的单包矩为零。

固定(7)不破坏这条闭合。其对 inner 左尾只减去 $Y$ 作用于原二次多项式，分子仍是(14)。原齐次 tail 方程继续成立，$\beta$ 保相应真实入值。等价地可把新增项按原 E8 复合展开；其对二次 tail 的 outer 作用是原三个 $\mathfrak{sl}_2$ profile 方向，原三矩仍闭合。所有这些项都计入同一个 $\Gamma_s$。

若实际配对的 outer 是 $u_k$、第三场 outer 是 $u_i$ 且 $k\ne i$，该积分为零。$i\ne j$ 时用 $C_{ij}$ 的严格局域性；$i=j,k<i$ 时，$C_{ii}$ 的真左分子仿射，故其导数为常向量，准确有
$$
\int V_{Y_k}'\cdot\text{常向量}=0.
\tag{17}
$$
$k>i$ 时该第三场在此本来右零。这与 R292(27)的原尾理由相同，不把“局部 forcing 零”误作任意 period 零。

因此，未加 $\chi$ 的完整 $Y$–third ruling 配对具有准确形式
$$
\boxed{
\sum_i c_i(\theta)^2d_i(\theta)S_i(s)
+\sum_{i<j}c_i(\theta)^2d_j(\theta)
\Gamma_s(\mu_i,\mu_j),
}
\tag{18}
$$
其中 $c_i=a_iC_\theta+b_iS_\theta$、
$d_i=a_i^2-c_i^2$，$S_i=P_s(t_i)$ 且 $\deg P_s\le10$。原第三场规范的固定因子可以收入 $S_i,\Gamma_s$，不会改变任何消去。所有 canonical 第三入历史均按原完整恢复进入二者；独立的固定第三规范 $\chi_\theta$ 在第5节单列。

## 4. 八、十二与五块准确消去(18)，并将 second square 化为一个相位

### 4.1 任意双线性核的完整四次混合链

对(18)的两个 even 相位系数，原代数是
$$
E_{04}=B_0\sum_jR_j\left\{S_j+\sum_{i<j}\Gamma_s(\mu_i,\mu_j)\right\},
\tag{19}
$$
$$
E_{22}-E_{04}
=\sum_i(R_i^2-4T_i^2)S_i
+\sum_{i<j}(R_iR_j-4T_iT_j)\Gamma_s(\mu_i,\mu_j).
\tag{20}
$$
同格距(5)给 $\sum_{i<j}\mu_i$ 的三个分量次数至多三，所以(19)前缀次数至多五。结合(3)及完整 self 的十次界，$E_{04}=0$。

(20)的 self 用(2)(3)消去。只对 $\Gamma_s$ 的对称部分使用
$\sum R_i\mu_i=\sum T_i\mu_i=0$，其对角余项次数至多四，仍精确为零。反对称部分恰由三个原有序面积
$$
\mathcal A_{rs}
=\sum_{i<j}(R_iR_j-4T_iT_j)
(\mu_{r,i}\mu_{s,j}-\mu_{s,i}\mu_{r,j}),
\quad0\le r<s\le2
\tag{21}
$$
控制。没有把整个有序 $\Gamma_s$ 改成对称核。

原十二副本的真实共同幅度四次权
$\binom{11}{j}$ 与 $g$ 翻号 $(-1)^j$，使两个 odd 系数成为第十一差分，完整十次界使其为零。原八副本在此前支付全部 cubic ruling，不能把八份的三次符号权误用作二次矩闭合。

最后 R280 §7 的两个真实面积异号布局、五个最终位置及五个严格正四次权给 $\mathcal A_{01}=\mathcal A_{02}=\mathcal A_{12}=0$。不同完整 base 的真实 $D_\theta$ 三矩为零，故它们之间的(18) cross 本来为零。全部最后平移与正幅均保留。

这就是 [R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md) §§6–7 对任意双线性 $\Gamma$ 的原有限消元；本稿另付了(18)的完整新 self 和原尾范围。因此
$$
\boxed{\frac1h\int V_{Y_\phi}'\cdot V_{W_\theta^0}'=0}
\tag{22}
$$
对任意真实局部几何、全部 $s,\theta$ 成立。它不限于 W 中的一条第三方向，也不删除第三场本身。

### 4.2 同一个真实对称能量

在当前几何和历史下定义
$$
\mathfrak B_s(F,G)=\frac1h\int
\partial_xV_{Z_F}\cdot\partial_xV_{Z_G}.
\tag{23}
$$
这是整个物理区间上的真实对称双线性配对。对 $i<j$，(14)给
$$
\mathfrak B_s(u_i^2,u_j^2)
=-\frac1hV_{Z_i}(\ell)\cdot U_{\mu_j}.
\tag{24}
$$
所以有序 cross 也是两组三矩的真实双线性核；它可以不对称，(23)的对称性通过交换完整输入和实际次序实现。

置
$$
\Delta=f^2-g^2,\quad F_{fg}=f\odot g,\quad
A=\mathfrak B_s(\Delta,\Delta),\
B=\mathfrak B_s(\Delta,F_{fg}),\
C=\mathfrak B_s(F_{fg},F_{fg}).
$$
用同一个(2)(3)、完整 self 十次界、对称/反对称分拆及(21)，得到 $A=4C$。十二翻号副本使 $B=0$；其共同平移次数仍不超过十。跨完整 base 的 second 场在两 collar 都零，故(24)跨 base 项为零。

现在才作相位代数：
$$
\begin{aligned}
\mathfrak B_s(D_\theta,D_\theta)
&=S_\theta^4A-4S_\theta^3C_\theta B
+4S_\theta^2C_\theta^2C\\
&=\boxed{S_\theta^2\mathfrak B_s(\Delta,\Delta)}.
\end{aligned}
\tag{25}
$$
这不是逐包能量为零；右端一般严格正。

## 5. 完整第四 ruling 只有一个真实能量约束

令
$$
\mathscr E(h,k,\omega,\mathsf m,h_s,k_s)
=\frac1h\int|\partial_xV_{Z_\Delta}|^2.
\tag{26}
$$
它包括全部 second 局部项、真实 $\mathsf m-\mathsf m_g$ 与其交叉平方。由 R56(4)、(22)(25)，原完整第四 ruling 在加入同一个 $\chi_\theta$ 后准确为
$$
\boxed{
\mathscr K(s,\theta)
=-S_\theta^2\mathscr E
-2\mathbf w_g(h,k,\omega)\cdot
\mathbf I_x(\phi_\theta,\chi_\theta),
}
\tag{27}
$$
$$
\mathbf w_g=
\left(\frac{1+(h\omega-k)^2}{4h},
\frac{h\omega-k}{2},\frac h4\right).
$$
所有 $Y$–third、second square 及第三规范的原系数已保留。原第四加速度行在此新库上确实为零，但剩下的(26)不能随之删去。

对任意预先固定的 $\nu\in\mathbb R^3$，R47/R56 的真实 Gram 右逆给同一个、光滑相位周期、双 collar 紧规范，使
$$
\mathbf I_x(\phi_\theta,\chi_\theta)=S_\theta^2\nu.
\tag{28}
$$
明确可用 $L_0\phi,L_1\phi,L_2\phi$ 的正定 Gram。$f,g$ 独立使 $\phi_\theta\ne0$；两个 seed 的右端为零，所以 $\chi_0=\chi_\pi=0$。该规范在整个局部路径上固定，不依赖 $s$。

于是全部相位的完整方程严格等价于
$$
\boxed{\mathscr E+2\mathbf w_g\cdot\nu=0.}
\tag{29}
$$
若别处已经锁定第三 Gram，(28)只能取该已锁向量；不能再次自由选择。本稿下面会用同一个 $\nu$ 同时支付参考正割与一个明确非正割入口。

## 6. 参考正割的完整能量：四个固定实常数

一次固定 $y=x+\omega_0$ 记号。以下所有 profile 函数都只是同一实际函数的坐标重写，右锚是 $r_*+\omega_0$。矩向量用 $\mathbf I_y$；离开 $\omega=\omega_0$ 后，(27)使用对应 $\omega-\omega_0$ 的真实权。

对二次槽 $\Delta=f^2-g^2$ 定义
$$
\begin{gathered}
D_{00}=f^2-g^2,\quad D_{01}=ff'-gg',\quad
D_{11}=f'^2-g'^2,\\
D_{12}=2(f'f''-g'g''),\qquad
D_{22}=f''{}^2-g''{}^2,\\
P=J(D_{22}),\qquad C_2=J(y^2D_{22}+2D_{11}),\\
R=D_{11}+yP,\qquad T_2=y^2D_{11}+yC_2,\qquad
D_*=yD_{11}+C_2,\\
\mathcal L=D_{11}-yD_{12}+y^2D_{22}=R-yR',\\
N=\frac{D_{00}}2-\frac{yD_{01}}2+
\frac{y^2D_{11}}4+\frac{yC_2}{8}.
\end{gathered}
\tag{30}
$$
因 $\Delta$ 的三个真实矩为零，这些整包函数均双 collar 紧；没有对单个微包作这个声明。

在 $k=0,\omega=\omega_0$，原完整 second normal 分子准确为
$$
(V_{Z_\Delta})_N=\frac R{8h}+hN.
\tag{31}
$$
这是 R73(2)及原 $B$ 完整相加；$N$ 中的 $C_2$ 未被删除。

定义
$$
\boxed{
a=\frac1{64}\int R'^2,\quad
b=\frac14\int R'N',\quad
c=\int N'^2,\quad
d=\frac1{64}\int\mathcal L^2.
}
\tag{32}
$$
它们在同一固定圆上定义，没有进行新的评价。$a,d>0$、$c\ge0$。例如最右微包的 $R_i\ne0$，在它上面
$R=R_i\{u'^2+yJ(u''{}^2)\}$，而 $y>0$；非零母包迫 $R$ 非零，紧性给 $a>0$。同一包上
$\mathcal L=R_i(u'-yu'')^2$ 不恒零，否则 $u'=yu''$ 与右零 collar 迫 $u=0$，故 $d>0$。

因此 normal 能量恰为
$$
\mathscr E_N(h)=a/h^3+b/h+ch.
\tag{33}
$$

取原实际参考正割
$$
h=H\sqrt{1+v^2},\quad v_s=1+v^2,\quad
h_s=hv,\quad k=k_s=0,\quad\omega=\omega_0,
$$
$$
\mathsf A_s-\mathsf A_g
=-\frac v{8h^2}R_y-\frac v8T_y.
\tag{34}
$$
它严格满足原 Mraw 方程；$\mathsf A_g$ 是真正中心常数，见 R488(10)(36)。

R482 的 $a_h[\Delta]$ 在这里满足
$$
a_h=\frac{R'}{16h^2}+\frac{T_2'}{16}-\frac{D_*}{8},
\quad
D_*'=-\mathcal L,\quad
a_h'=\frac{1+h^2y^2}{16h^2}R''.
\tag{35}
$$
将(34)(35)代入完整 $V_Z=(\eta/h+q'/2,\ zP+B,\
e\eta/h-hq+eq'/2)$，得到
$$
\boxed{
(V_Z)_T=-vD_*/8,\qquad
(V_Z)_B=vR/(8h).
}
\tag{36}
$$
故其导数为 $v\mathcal L/8$、$vR'/(8h)$。完整能量是
$$
\begin{aligned}
\mathscr E_{\rm sec}
&=\mathscr E_N(h)+v^2(a/h^3+d/h)\\
&=\boxed{\frac{a/H^2+b-d}{h}
+h(c+d/H^2)}.
\end{aligned}
\tag{37}
$$
没有第三 self 或任何尾项藏在这一步之外；它们已在(22)完整支付。

在固定 $y$ 三矩中选择一次
$$
\boxed{
\nu_0=-2(a/H^2+b-d),\quad
\nu_1=0,\quad
\nu_2=-2(c+d/H^2).
}
\tag{38}
$$
因为 $k=0,\omega=\omega_0$ 时
$2\mathbf w_g^y\cdot\nu=\nu_0/(2h)+h\nu_2/2$，(37)(38)使整条参考正割的(29)为零。再以(28)选择同一个 $\chi_\theta$；以后不再更换它。

## 7. 同一 $\chi$ 下存在明确的正则非正割入口

在实际状态
$$
h=h_0>H,\quad k=0,\quad\omega=\omega_0,\quad
\mathsf m=\mathsf m_g,\quad k_s=0
\tag{39}
$$
上，$q_\Delta=0$，normal 与两个 tangent 分量正交。原
$\eta_\Delta=\gamma a_h[\Delta]$，$\gamma=h_s$，所以
$$
\mathscr E=\mathscr E_N(h_0)+\gamma^2 c_h(h_0),
$$
$$
\boxed{
c_h(h)=\frac1h\int
\left\{\left(\frac{a_h'}h\right)^2+
\bigl((ya_h)'\bigr)^2\right\}>0.
}
\tag{40}
$$

严格正性不能由一个未评价的数值 Gram 冒认。最右微包上，原式给
$$
a_h'[u^2]
=\frac{1+h^2y^2}{8h^2}(u'-yu'')u'''.
\tag{41}
$$
若右端乘积恒零，则
$((u'-yu'')^2)'=-2y(u'-yu'')u'''=0$。
平端给 $u'-yu''=0$，再由 $y>0$ 和右 collar 得 $u=0$，矛盾。最右包的真实 $R_i\ne0$，所以(41)也证明 $\Delta$ 的(40)严格正。

取正的实际速度
$$
\boxed{
\gamma_0^2=
\frac{(h_0^2-H^2)(a+d h_0^2)}
{H^2h_0^3c_h(h_0)}>0 .
}
\tag{42}
$$
由(33)(37)，其分子准确是同一个(38)所要求的能量与 $\mathscr E_N$ 之差。因此(39)(42)满足完整(29)，而
$$
\partial_\gamma(\mathscr E+2\mathbf w_g\cdot\nu)
=2\gamma_0c_h(h_0)\ne0.
\tag{43}
$$

这是真正的正则入口，并非只给条件性非零 minor。可选择 $\mathsf m_g=0$，把它作为原零历史局部路径的实际起点；一般非零入值则必须由实际前缀供给。两种情况都不把 $\mathsf m_s$ 从(8)中释放出来。

## 8. 实际受约束 ODE 产生非恒曲率的非正割路径

令 $\bar{\mathsf m}=\mathsf m-\mathsf m_g$、$\upsilon=k_s$。由(43)的普通有限维隐函数定理，在(39)(42)的一个真实状态邻域内存在唯一光滑分支
$$
\gamma=G(h,k,\omega,\bar{\mathsf m},\upsilon),
\qquad G>0,
\tag{44}
$$
使(29)恒成立。能量只用固定有限 profiles 与其原函数的有限系数，所以这是有限维光滑函数，不涉及重新求一个无限维 profile 根。

任取足够小的真实光滑控制 $\upsilon(s)$，解同一个系统
$$
\boxed{
\begin{aligned}
h_s&=G(h,k,\omega,\bar{\mathsf m},\upsilon),\\
k_s&=\upsilon,\qquad
\omega_s=\upsilon/(2h),\\
\bar{\mathsf m}_s
&=M_{\rm raw}(h,k,\omega,G,\upsilon).
\end{aligned}}
\tag{45}
$$
再解原 frame 与 $\alpha$ 方程(1)。局部 ODE 存在唯一性给一个正长度实区间；缩短这个固定区间和控制盒，统一保持 $h>0,x+\omega>0$ 及(44)所在邻域。

由(45)，真实水平关系、全部八矩 history 以及完整(29)同时成立。由(27)，
$$
\boxed{\mathscr K(s,\theta)=0
\quad\text{对整个局部区间和全部相位。}}
\tag{46}
$$
二、三阶 ruling 已由同一完整包装支付，故 R56 原右锚恢复在该局部区间给真正双 collar 的二、三、四阶场。这里“局部”不要求 $s$ 周期；完整 characteristic 周期条件仍是以后整词的任务。

选择非零 $\upsilon$，例如支持在该区间内部的一条真实小 bump，则 $k$ 不恒为零，所得路径不是 R488 的正割分支；$\omega$ 也按实际方程改变。没有把负目标当负时间，没有逐相位另选几何，没有沿路径更换(7)(28)。

该构造选择新的基几何和新的目标背景；它不是在一个已经冻结的数值曲面上改变 $g$，也不声称给同一个固定目标度量的非线性等距族。结论是原理论构造中一个真实可用的完整局部路径族。

## 9. 参考正割的直接速度分叉确实退化，连接桥仍须另付

还需排除一个容易误用的推论：(43)不位于(34)的同一历史状态，因此不能据此宣布“从已付参考正割内部直接分叉”。

事实上在真实(34)处固定 $h,k=0,\omega,\mathsf m$，任意速度改变只使 tangent 分子增加
$$
\delta V=(\xi/h,0,y\xi)
\tag{47}
$$
的一项；对原 $\gamma,\upsilon$ 分别取相应 $\xi=a_h\,\delta\gamma$、$a_k\,\delta\upsilon$。整个 $\Delta$ 三矩使 $\xi,R$ 双 collar 紧。

由(36)和 $\mathcal L=R-yR'$，
$$
\begin{aligned}
\int V_{\rm sec}'\cdot\delta V'
&=\frac v{8h}\int
\{\mathcal L\xi'+R'(\xi+y\xi')\}\\
&=\frac v{8h}\int(\mathcal L+yR'-R)\xi'=0.
\end{aligned}
\tag{48}
$$
所以完整能量对两条速度的一导都为零，并有准确平方余项
$$
\mathscr E_{\rm fixed\ state}
=\mathscr E_{\rm sec}+\frac1h\int|\delta V'|^2.
\tag{49}
$$
这没有排除更高阶状态轨道离开正割族；它只证明当前正则能量 IFT 不能直接应用于该参考状态。

因此本文已构造的是：同一 $\chi$ 支付参考正割，以及另一个真实正则入口上的非正割路径族。二者之间达到所需 $h,k,\omega,\mathsf m$ 的原 R70 桥，即使端矩阵可以实际控制，其**内部**仍必须满足(29)。本文没有支付这条额外连接，也没有把(39)写成对已冻结路径的任意瞬时重置。

## 10. 可以保两端完整 germs 与全部有限阶基准的真实局部变形

(45)还给一个具体可用的局部自由度结论，不需要假设某个额外 endpoint rank 满秩。

固定一个足够短区间 $[0,L]$，所有控制均在两端共同 collar 恒为零。起点固定为(39)(42)。按 R56 §6 的有限分离闭合，为固定 $f,g,w,\chi$ 一次列出至第四阶的完整右锚恢复所需有限 profile 字表，并保其真实 $s$ 系数。将下列真实终点数据合成一个有限映射 $\mathcal P$：

- $h,k,\omega,\bar{\mathsf m}$ 的终值；
- 完整 frame、中心线位置终值；
- 二、三、四阶完整恢复在终点的分离系数，以及原 $A,T$ 和固定输入的完整第四传递、period/十三行贡献的有限呈示。第四层保全部原未正规化项；当该段没有 $M=0$ 时，不把它冒称为已落入原正规成本空间 $U$。

允许冗余系数；要求这些系数相等只是一个明确的充分保持条件，不冒作某个未经证明的独立基。其数目 $d<\infty$ 在选择控制参数数目以前已固定。字表不因控制参数增多而增大；所有输入 profiles 和 Taylor 阶数始终固定。

选 $N>d$ 个线性独立的实际 $C_c^\infty((0,L))$ 控制 bumps，以足够小参数 $z\in\mathbb R^N$ 线性组合成 $\upsilon_z$。全部路径按(45)实际产生，$\mathcal P(z)$ 光滑。取该小开参数盒中其导数达到最大实际秩 $r\le d$ 的一点。相应非零 minor 给一个常秩邻域；可选这一点的控制非零，因为非零控制点在参数盒中开稠密。

常秩定理遂给通过该点的一个维数 $N-r>0$ 的真实参数纤维，其 $\mathcal P$ 值精确相同。控制 bumps 独立，故不同参数确给不同 $\upsilon$ 及不同实际曲率路径，不是同一路径的冗余参数标签。

两端控制均零，(45)在共同 collars 上是同一个自治 ODE。共同起点使所有左 germs 相同；共同终点状态与反向局部唯一性使所有右 germs 也相同，连同由 ODE 决定的全部端导数。加入的 frame、位置和恢复系数使原完整有限阶端传递及相应成本基准也同时相同。

这个结论给**一族已经真实产生的非正割段之间**、保其自身两端全部 germs 与完整有限阶数据的非平凡变形。没有宣称这些共同端口是预先任意指定的，也没有说其共同 $M,T,V$ 为零。若该段随后嵌入一个固定整词，替换只保其已列入 $\mathcal P$ 的全部真实贡献；未列入的新高阶条件仍须另付。

全部 prototype 次数、原 $\delta X^*$、实际 frame/位置桥、倒行和 Klein 成本都不能由这个等值纤维删除。它提供局部可变路径，尚不提供所需全局返回或新成本方向。

## 11. 与当前完整主问题的接线

本稿的新闭合事实是：

1. 用原真实有限布局、同一个字面母包和全部原尾，完整 $Y$–third 配对准确为零，second square 准确是一个 $\sin^2\theta$ 能量；
2. 原第三 Gram 以一个固定向量支付该能量后，存在一个明确正则入口，并由实际八矩 ODE 得到非恒 $k$ 的完整 ruling 零路径；
3. 同一向量也准确支付参考正割，但参考正割上的速度退化被明确保留；
4. 正则局部族中存在保两端真实 germs 与完整有限阶端数据的非平凡变形。

仍欠的是：在同一个最终 profile/规范上，将这些实际段连接为满足原 frame/位置返回、全部 period、十三行及固定第三目标的整词。旧不同母的十九/二十目标、R467/R468 成本截面及其既有保护芽不能不加证明地搬到本稿同形新库。反过来，若从起点要求那些门，也必须重新证明它们与本稿完整 self 身份共同可实现。

即使以后该整词闭合，真正有限等距族、嵌入、厚度与宏观幅度仍需要原后继工作。本文解决的是一个此前尚无明确正则入口的完整非正割局部路径问题，不以局部 IFT 代替主目标。

### 原式与窄核范围

- R56、R73：全部分子、真 $M_{\rm raw}$、变化-profile chain、右锚和有限分离；
- R183、R280、R480：原八／十二／五块的实际幅度、完整三矩、有序面积及任意双线性核消元；
- R292、R405：完整 $YC$ 左尾和逐 $s$ 三矩核；
- R47、R488、R482：固定第三 Gram、真实正割历史和一般 second 恢复；
- R472、R503：原完整传递、真实前缀与未付桥内 ruling 的边界。

tail_cost 仅独立纸核了 $A=4C,\ B=0$ 后(25)的末端相位代数；未将该窄核扩大为本稿新增 self 次数、原尾或全部路径证明。其它推导均以上述完整显示原式为准，没有任何新科学执行。
