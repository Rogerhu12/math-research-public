# R557：同一规范的真实快高度回路与五个中心矩的准确联合零

日期：2026-11-16。**完整原式纸证；没有执行数值、符号、profile、求积、秩或开发检查。**

本稿继续 R556 的同一个 R521 母库和一次选定的 $\chi$。
新增段从原词的真实非零 incoming 出发，不再选择第三规范。
一条小幅快高度回路补偿 R556 严格负的中心 $R_1^y$，
同时把它的负 $T_1$ 速度成本和三个 $p$ 增量带回同一个端点映射，
得到
$$
\boxed{
P_0=P_1=P_2=T_1=R_1^y=0.
}
\tag{1}
$$
这是固定中心坐标的五个独立矩准确为零。
尚未清 $S_1$ 时，不能把 $R_1^y=0$ 写成原 $R_1^x=0$。

完整第二、第三历史和真正端 germs 全保。
末端另有一个明确的负 $S_0^y$ 首项，故本稿仍未得到全 $M=0$、
frame／位置或高阶 period 返回。

## 1. 原同词端图与一条严格负余量

保持 R552/R556 的固定坐标及规范：
$$
y=x+\omega_c,\quad \eta=\omega-\omega_c,\quad d=h\eta-k,
$$
$$
\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\quad
\delta=\lambda^2\zeta,\quad R=L_h/\sqrt\lambda,\quad
M=(1+\log R)^6.
\tag{2}
$$
原第二规范仍为0。$H,H_0,c,L_h$、母库、右锚和 $\omega_c$ 全部不变。
所有后文参数都不进入 $\nu$。

沿用 R556 的 $Z_*>0,g_0>0,D_*<0,\mathfrak b>0$。
令 $\theta=(\ell_1,\ell_2,\xi)$ 表示它的三参数真实族。
在最后高尾准确停在 $z=0$ 时，其完整端点映射有
$$
\begin{aligned}
\frac{\delta R^{5/2}}M P_1
&\longrightarrow
-\frac{D_*}{2c}\left\{
\frac{Z_*^2}{16}(\ell_1+\ell_2/4)
-\frac{\mathfrak b Z_*^3}{24}\right\},\\
\delta R^{5/2}P_0
&\longrightarrow
Z_*-\frac{g_0(\ell_1+\ell_2/4)}{6c\xi},\\
\frac{\delta R^{3/2}}M T_1
&\longrightarrow
\frac{\mathfrak bZ_*}{4}-\frac{\ell_1+\ell_2}{8}.
\end{aligned}
\tag{3}
$$
这些是同一个完整词上的 $C^1$ 收敛。
其正共同零为
$$
\theta_*=
\left(\frac{2\mathfrak bZ_*}{9},
\frac{16\mathfrak bZ_*}{9},
\frac{g_0\mathfrak b}{9c}\right),
\tag{4}
$$
且三维 Jacobian 可逆。

更精确地，R556 已在同一个参数盒上支付
$$
\boxed{
\delta R^{3/2}R_1^y
=-\frac{\ell_1+\ell_2}{8\xi}+o^1(1).
}
\tag{5}
$$
本稿使用这个完整实际余量，不将原历史重新设零。

暂将 R556 最后高尾的实际停止坐标由0放宽为一个很小的实数 $v$：
$$
z=\sqrt R\,\delta\,\mathsf m_{p_2}=v.
\tag{6}
$$
该高尾在0的两侧都有原 $z_s<0$ 的真实开放区间，
所以(6)仍是唯一、光滑依赖参数的实际事件。
$v$ 后面只用于补偿新增段的真实 $p_2$ 成本。

## 2. 从真正 incoming 下降到原高度

从(6)的真实末端沿 R544 同一个反馈，作一条有限参考下降到原 $H$。
取一个开放恒参考段后作为快回路入口。
本节的有限过渡仍先在固定 $R$ 上选择，所有原矩与速度平方成本
记入 $C_R$，最后以同一个 $\delta$ 控制。

在(4)附近的固定参数盒及足够小 $v$ 上，
最后高尾的缩放历史有
$$
\bar A:=\delta A=O(M/R^{3/2}),\qquad
\bar T:=\delta^2\widetilde T=O(M/R^2).
\tag{7}
$$
这些界并不要求先令 $T_1$ 或 $R_1$ 精确为0。
有效 Gram 满足
$$
\Gamma_1=2c+O(M/R^2),\qquad
\Gamma_0,\Gamma_2=O(M/R^2).
\tag{8}
$$
R552 的稳定支判别式因此在全部有限下降上严格正；
当前 $h j$ 和 $k/h$ 小，原合法窗口与 $C_k,B$ 正性保持。
同一水平分部积分及正常反馈给实际低入点
$$
h=H+O(C_R\delta),\quad
k,\eta,d,j=O(M/R^2)+O(C_R\delta),
$$
$$
h_s,k_s=O(C_R\delta).
\tag{9}
$$
$\Gamma_0$ 此处不必为正；它的小量与判别式才是本次下降的条件。
没有把 R556 两个旧正 $\Gamma_0$ 低端的号免费搬来。

改用真实第三状态
$$
\mathsf A=\delta A,\qquad
\mathsf T=\delta^2T_{\rm third}.
$$
由原速度势转换，入口仍有
$$
\boxed{
\mathsf A_{\rm in}=O(M/R^{3/2}),\qquad
\mathsf T_{\rm in}=O(M/R^2)+O(C_R\delta^2).
}
\tag{10}
$$
它们是实际非零向量。后文所有第三交叉项都含这个真实 incoming。

## 3. 固定一个非平凡闭振子的高度形状

置
$$
\beta=\frac{B(H,0)}{2c}>0.
$$
这里 $c=C_k(H,0)$，是原 R544 的同一个常数。
先取一非零 $\psi_0\in C_c^\infty(0,1)$。
一次正时间伸缩可令所得 $\psi$ 满足
$$
\int(\psi''')^2=\int(\psi'')^2.
\tag{11}
$$
具体伸缩长度由两个正积分之比的平方根定义；
这是一个有限存在选择，不执行求积或近似。
把其支撑放在一个固定有限快区间的内部，预留两端开放零区间。

定义
$$
\boxed{
D_f=\psi'',\qquad
f_*=-\frac{\psi''+\psi}{\beta}.
}
\tag{12}
$$
于是准确有
$$
(D_f)''+D_f=-\beta f_*'',
$$
且 $f_*,D_f$ 的全部端 jets 都为0。
它们均非平凡；紧支撑的 $\psi''+\psi=0$ 只能有零解。

还有两个有用的精确积分：
$$
\int f_*'(D_f)'=0,\qquad
\int(D_f)'f_*''=0.
\tag{13}
$$
第一式由(11)及一次 IBP，第二式由(12)中两个平方导数的端项为0。
因此这个回路的领先交叉速度 Gram 与完整二阶速度面积都为0，
但其高度速度平方严格正。

记
$$
\boxed{
C_f=\frac1{8H^4}\int(f_*')^2>0,\qquad
C_s=\frac1{4H^2}\int((D_f)')^2>0.
}
\tag{14}
$$
$C_f,C_s$ 都是本次固定的有限真实常数。
(11)没有使 $C_f$ 退化：若 $f_*'=0$，紧支撑迫 $f_*=0$，继而 $\psi=0$。

## 4. 实际快控制：不是把零历史 R545 直接移植

选快幅度尺度
$$
\varepsilon=R^{-3/4}
$$
和一个可调正幅值 $a_f$，最终限制在一个固定正紧区间。
快时钟仍是原固定 $\delta$：
$$
\tau=(s-s_{\rm in})/\delta .
\tag{15}
$$
这里没有采用另一条 $\delta=\zeta\varepsilon$ 规范。
$\delta$ 仍是(2)中从起点一次选择的数据。

在快区间的中段使用高度控制，其领先形状为
$$
h=H+\varepsilon a_f f_*(\tau).
\tag{16}
$$
实际控制另外保入口原反馈的真实 germ，并加入第5节四个有限内控。
区间两端开放部分使用原 R544 的加速度反馈形式。
因此(16)只描述已支付的领先形状，不是硬把真实 $h$ 接到一个
不相容的常函数上。

令 $G=h_\tau$、$V=k_\tau$。
这些符号只表示快速度；真实速度为它们除以 $\delta$。
原完整快方程准确是
$$
\mathsf A_\tau
=\delta^2\Phi_{M_0(S)}+\Phi_{M_2(S;G,V)},
\tag{17}
$$
$$
\begin{aligned}
\mathsf T_\tau={}&
-\{\delta^2\Phi_{M_0}+\Phi_{M_2}\}\circ\mathsf A
+\delta^2\mathcal C^{[1]}\\
&+\partial_\tau P_{\rm acc}(S;G,V)
+\mathcal A(S)
  (V h_{\tau\tau}-G k_{\tau\tau})\\
&+\sum_j\mathcal B_j(S)
  G^{\,3-j}V^{\,j}.
\end{aligned}
\tag{18}
$$
完整 ruling 乘以 $\delta^2$ 后是
$$
\begin{aligned}
0={}&C_hh_{\tau\tau}+C_kk_{\tau\tau}
+\delta^2R_0+R_2(S;G,V)\\
&+L_{\rm vel}(S;G,V)(\mathsf A\Delta)
-E_S(\mathsf A\Delta,\mathsf A\Delta)\\
&-4E_S\{\phi,\mathsf T(\phi;\Delta)\}
-2\mathbf w(S)\cdot\bar\nu .
\end{aligned}
\tag{19}
$$
其中 $\bar\nu=\delta^2\nu$ 仍由(2)给出。
$C_k>0$ 使中段给定高度控制后可解真正 $k_{\tau\tau}$。
(17)–(19)没有删除 $YC$、原 potential、速度面积或 $\mathsf A_{\rm in}$。

在本稿尺度上
$$
\lambda=o(\varepsilon^2),\qquad
M/R^2=o(\varepsilon^2),\qquad
M/R^{3/2}=o(\varepsilon).
\tag{20}
$$
先固定 $R$ 后再小 $\delta$，使所有 $C_R\delta$ 也低于所需的
$\varepsilon$ 次数。由(9)(10)(17)–(19)，有限快区间上的真实解具有
$$
h=H+\varepsilon a_f f_*+O_{C^2}(\varepsilon^2),\quad
d=\varepsilon a_f D_f+O_{C^1}(\varepsilon^2),
$$
$$
k=-2\varepsilon a_fD_f+O_{C^1}(\varepsilon^2),\quad
\eta=-\varepsilon a_fD_f/H+O_{C^1}(\varepsilon^2).
\tag{21}
$$
这些展开保参数的一阶导数。

直接取(19)的一阶，得到
$$
D''+D=-\beta f''.
\tag{22}
$$
原 $\lambda$、真实 incoming 势和全部速度／历史项在本次
一阶变分中低阶，但在(17)–(19)中始终存在。
这是对当前实际入口的原式推导，不是引用 R545 零 history 的结论
后把其初值改名。


## 5. 四个原加速度内控与真正末 germ

在(16)的形状之外选四个固定光滑内控，只修改原唯一输入
$h_{\tau\tau}$。它们支撑在快区间内部，处在最终开放反馈段之前。
这里不增加独立的 $k$ 控制或新的规范。

在线性极限，令状态为 $(X,X',D,D')$，输入为 $X''$；
由(22)，输入列及其前三个系统迭代为
$$
\begin{aligned}
b_0&=(0,1,0,-\beta),&
b_1&=(1,0,-\beta,0),\\
b_2&=(0,0,0,\beta),&
b_3&=(0,0,\beta,0).
\end{aligned}
\tag{23}
$$
$\beta>0$，所以这四列独立。等价地，原端点积分核由
$1,\tau,\sin\tau,\cos\tau$ 的可逆线性变换给出。
这四个解析函数独立，因而可选四个内点及其充分小的固定光滑
bump，使四个真实输入的端点矩阵可逆。
这是显示的有限线性控制论证，没有执行新的秩或样点检查。

在入口开放段保持真实 incoming 的原反馈；
经一个固定光滑 cutoff 进入形状(16)，在末端再平滑切回
R544 的原加速度反馈。零极限下，两端的参考形状与振子全部为0，
所以两次切换都不改变(12)的极限解。
最终开放反馈段的线性流可逆，故它也不改变(23)的满秩性。

实际四个端点条件取为
$$
\boxed{
h(T_f)=H,\quad h_\tau(T_f)=0,\quad
d(T_f)=q_{\Gamma_{\rm out}}(H),\quad d_\tau(T_f)=0 .
}
\tag{24}
$$
$q_{\Gamma_{\rm out}}$ 是含本次完整末历史的原稳定支，
按原 $\widetilde T=T-P_{\rm acc}+\mathcal A h_sk_s$ 计算，
因此也包含尚未求零时的真实端速度势；
不是取一个预设零 history 的 $q$。
将(24)的残差除以 $\varepsilon a_f$，其四内控 Jacobian
收敛于(23)给出的可逆矩阵。
因为(20)及完整历史方程使实际非线性残差为
$O(\varepsilon^2)+O(C_R\delta)$，
原有限维 IFT 给四个 $O(\varepsilon)$ 的归一化控制修正。
它们及解对 $(\theta,a_f,v)$ 一阶光滑；(21)的精度不变。
所有小 $\delta$ 条件在同一个固定参数盒上统一选取。

需要特别说明：只付 $d,d_s$ 两值，不足以付真正反馈 germ。
本稿使用(24)的四个值和末端开放反馈段。
R544 的准确反馈量为
$$
\mathscr C=h_s-V_{\rm fb}
-\kappa\frac{d-q_\Gamma(h)}{\delta},
\tag{25}
$$
其中参考高度在该段恒为 $H$。
原加速度反馈正是 $\mathscr C_s=0$ 的完整解式，
包含有效 Gram 的真实导数和原反馈质量因子。
在(24)处 $V_{\rm fb}=0$，故 $\mathscr C=0$。
于是整个末端开放区间均有 $\mathscr C=0$，
与原反馈方程完全一致。

由原水平式，(24)还给 $k_s=0$。
更高 jets 是同一个实际反馈系统在真实 incoming 下的 jets；
它们没有被强行设为常态，也不声称与原词起点的周期 germ 相同。
至此，新增回路与前后段组成一条真正光滑的实际词。

## 6. 完整第三交叉项和原端势的账

令
$$
\mathcal N(\tau)=\delta^2\Phi_{M_0}+\Phi_{M_2}.
$$
从(18)积分，完整第三增量准确分为
$$
\begin{aligned}
\Delta\mathsf T={}&
-\int\mathcal N\circ\mathsf A_{\rm in}\,d\tau
-\int\mathcal N\circ(\mathsf A-\mathsf A_{\rm in})\,d\tau\\
&+\delta^2\int\mathcal C^{[1]}\,d\tau
+[P_{\rm acc}]_{\rm in}^{\rm out}\\
&+\int\mathcal A(S)(VG_\tau-GV_\tau)\,d\tau
+\int\sum_j\mathcal B_j(S)G^{3-j}V^j\,d\tau .
\end{aligned}
\tag{26}
$$
本式保原算子复合次序。第一行的第一个积分就是非零 incoming
所产生的真实第三交叉项，不能删去或改为一个新的左锚。

由(21)，快速度 $G,V=O(\varepsilon)$，
而 $\Delta\mathsf A=O(\varepsilon^2)+O(C_R\delta^2)$。
所以(26)的前两个积分分别为
$$
O(\varepsilon^2\|\mathsf A_{\rm in}\|)
+O(C_R\delta^2\|\mathsf A_{\rm in}\|),
\qquad
O(\varepsilon^4)+O(C_R\delta^2).
\tag{27}
$$
$P_{\rm acc}$ 是原速度二次势。输出的快速度由(24)准确为0；
输入的快速度是实际慢反馈速度乘以 $\delta$，
故其原端势为 $O(C_R\delta^4)$。这里没有假设两个原端势
分别不存在。

速度面积的二阶项逐项为
$$
\begin{aligned}
\int\mathcal A(S)(VG_\tau-GV_\tau)
&=-4\varepsilon^2a_f^2\mathcal A(S_c)
  \int D_f'f_*''+O(\varepsilon^3)\\
&=O(\varepsilon^3).
\end{aligned}
\tag{28}
$$
最后一步用(13)，不是以“闭高度”代替闭振子的面积条件。
状态系数的变化、四内控的 $O(\varepsilon)$ 修正、
入口非零小量都已包含在这个三阶余项中。
原三次速度项也是 $O(\varepsilon^3)$。
$\delta^2\mathcal C^{[1]}$ 的完整贡献在有限快区间由最后一次
$\delta$ 选择控制。

因此
$$
\boxed{
\Delta\mathsf T
=O(\varepsilon^3)
+O(\varepsilon^2\|\mathsf A_{\rm in}\|)
+O(C_R\delta^2).
}
\tag{29}
$$
(10)(20)使中间项低于 $\varepsilon^3$。
相同估计保所有端图参数的一阶导数。
真实 $T_{\rm third}$ 的增量是(29)除以 $\delta^2$；
它通常不为0，也不必小。本文只使用完整缩放状态的界。

原水平式还给
$$
j_\tau=-2d\,h_\tau/h^3.
$$
其二阶增量为
$-2\varepsilon^2a_f^2H^{-3}\int D_f f_*'$。
闭振子能量身份，或直接代入(12)，给这个积分准确为0。
故
$$
\Delta j=O(\varepsilon^3)+O(C_R\delta).
\tag{30}
$$
最终 $k,\eta$ 仍为
$O(M/R^2)+O(\varepsilon^3)+O(C_R\delta)$，
且有效稳定支保持原判别式和合法窗口。
(26)–(30)解释了为何该回路可以作为原词的真实后继；
没有把它作为一个零 history 的独立模块来拼接。

## 7. 原矩成本：正 $R_1^y$ 与负 $T_1,S_0^y$ 同时出现

本节使用 R73 的完整原 $M_0+M_2$，
以及 R555 的准确负速度 Gram。
在 $S_c=(H,0,\eta=0)$ 的快一阶代入
$$
h=H+\varepsilon a_f f_*,\qquad
d=\varepsilon a_fD_f
$$
后，原实际时间 $ds=\delta\,d\tau$ 给
$$
\begin{aligned}
\delta\,\Delta R_1^y
 &=\varepsilon^2a_f^2 C_f+o^1(\varepsilon^2),\\
\delta\,\Delta T_1
 &=-\varepsilon^2a_f^2H^2 C_f+o^1(\varepsilon^2),\\
\delta\,\Delta S_0^y
 &=-\varepsilon^2a_f^2 C_s+o^1(\varepsilon^2).
\end{aligned}
\tag{31}
$$
同一个原表给
$$
\begin{aligned}
\delta\,\Delta S_1^y
 &=-\frac{\varepsilon^2a_f^2}{4H^2}
     \int f_*'D_f'+o^1(\varepsilon^2)
   =o^1(\varepsilon^2),\\
\delta\,\Delta R_0^y
 &=\frac{\varepsilon^2a_f^2}{8H^4}
     \int f_*'D_f'+o^1(\varepsilon^2)
   =o^1(\varepsilon^2).
\end{aligned}
\tag{32}
$$
本稿特意选择(11)，只消这个交叉首项。
没有假设完整交叉矩准确为0，也没有从正 $R_1$ 增量删除负的
$S_0$ 速度平方。

例如，R555 的逐点身份
$$
r_1=u s_1+(h^{-2}-u^2)t_1+\frac14(h^{-1})_s^2,
\qquad u=d/h,
$$
在本次一阶代入准确产生(31)的 $1/(8H^4)$。
同表的
$$
\begin{pmatrix}8N_{t_1}&4N_{s_1}\\
4N_{s_1}&4N_{s_0}\end{pmatrix}
=-\int
\begin{pmatrix}v\\w\end{pmatrix}
\begin{pmatrix}v&w\end{pmatrix}\,ds,
\quad v=h_s/h,\ w=d_s/h
\tag{33}
$$
说明三个负成本属于同一个 Gram；
它们不是可以各自自由调号的三个方向。

真实静态部分在快区间上的贡献为 $O(C_R\delta)$；
乘以(31)的 $\delta$ 后是 $O(C_R\delta^2)$。
实际 incoming 对几何系数的变化、控制修正和原加速度解
均已由(21)保留，给三阶或更低阶的归一化余项。

原三个 $p$ 密度没有速度二次部分。因此在这个有限快区间，
$$
\Delta P_i=O(C_R\delta),\qquad i=0,1,2.
\tag{34}
$$
先前有限下降的完整 $P_i$ 成本为有限 $C_R$。
所有这些成本以下都用真端点映射校正，不把(34)写成准确零。

由于 $\varepsilon^2=R^{-3/2}$，快回路给 $R_1^y$ 的所需
$1/(\delta R^{3/2})$ 量级，
但其 $T_1$ 成本在(3)的尺度上只为
$$
-\frac{a_f^2 H^2C_f}{M}+o^1(M^{-1}).
\tag{35}
$$
(35)趋零，却仍存在于后面的实际 $T_1$ 方程中。
正是原三个端参数负责同时支付它。


## 8. 先用真实停止坐标支付新增 $P_2$

在快回路之前的高尾使用(6)的停止参数 $v$。
随后依次走实际有限下降、入口开放反馈段、完整快回路及其末 germ。
对这个**完整词**定义
$$
\mathcal G_2(v,\theta,a_f)
=\sqrt R\,\delta\,P_2^{\rm total}.
$$
高尾的原定义给第一项准确为 $v$；
后继有限下降的 $P_2$ 有界于 $C_R$，
快回路则满足(34)。因此
$$
\boxed{
\mathcal G_2
=v+O_{C^1}(C_R\sqrt R\,\delta)
  +O_{C^1}(C_R\sqrt R\,\delta^2).
}
\tag{36}
$$
这里每个固定 $R$ 上的 $C_R$ 包含真入值、四内控、
过渡规则及全部参数导数。其有限性来自已经写出的完整
缩放 ODE；不要求它对 $R\to\infty$ 有一个免费统一界。

最后一次选小 $\delta$ 后，
$\partial_v\mathcal G_2$ 一致接近1。
实际 IFT 给一个唯一的小实值
$$
v=v_{R,\delta}(\theta,a_f)
$$
使整词 $P_2=0$。
高尾在0的两侧均有真实开放区间，
所以不论这个修正的符号如何，它都由实际停止事件实现。
没有删去新增段的 $p_2$，也没有另加一个只在代数上补值的响应。

把该 $v$ 代回后，其对其余端图的影响在同一次 $\delta$ 选择中
为 $o^1(1)$。以下每个参数点都已经满足真正的总 $P_2=0$。

## 9. 同一个四参数端图给其余四个准确零

以
$$
(\ell_1,\ell_2,\xi,a_f)
$$
作为剩余四个真实参数。
前面四内控与最后停止位置都是这些参数的真实光滑函数，
不是额外自由端值。

完整词的归一化端图取为
$$
\mathcal F_{R,\delta}=
\left(
\frac{\delta R^{5/2}}M P_1,\ 
\delta R^{5/2}P_0,\ 
\frac{\delta R^{3/2}}M T_1,\ 
\delta R^{3/2}R_1^y
\right).
\tag{37}
$$
由(3)(5)(31)(34)–(36)，它在一个固定正参数盒上
$C^1$ 收敛于
$$
\begin{aligned}
\mathcal F_1^\infty
&=-\frac{D_*}{2c}
 \left\{\frac{Z_*^2}{16}(\ell_1+\ell_2/4)
              -\frac{\mathfrak bZ_*^3}{24}\right\},\\
\mathcal F_0^\infty
&=Z_*-\frac{g_0(\ell_1+\ell_2/4)}{6c\xi},\\
\mathcal F_t^\infty
&=\frac{\mathfrak bZ_*}{4}-\frac{\ell_1+\ell_2}{8},\\
\mathcal F_r^\infty
&=-\frac{\ell_1+\ell_2}{8\xi}+a_f^2 C_f .
\end{aligned}
\tag{38}
$$
其中 $T_1$ 的真实快成本(35)只在极限中消失；
它在 $\mathcal F_{R,\delta}$ 内从未删除。

前三式仍在(4)有共同零。
第四式由一个严格正的实际幅值支付：
$$
\boxed{
a_{f,*}
=\left(\frac{\ell_{1,*}+\ell_{2,*}}
{8\xi_* C_f}\right)^{1/2}>0.
}
\tag{39}
$$
在该点，(38)的 Jacobian 是一个块下三角矩阵：
左上三维块是 R556 的可逆端图，
右下元素为 $2a_{f,*}C_f>0$。
因此四维 Jacobian 可逆。

先以(4)(39)为内部点选一个固定正参数盒，
然后按下一节的顺序选择有限 $R$ 和正 $\delta$。
原有限维 IFT 给该盒中的真实参数
$$
(\ell_{1,R,\delta},\ell_{2,R,\delta},
 \xi_{R,\delta},a_{f,R,\delta})
\longrightarrow(\theta_*,a_{f,*}),
\tag{40}
$$
在它们对应的同一个完整实际词上，
$$
P_0=P_1=T_1=R_1^y=0.
$$
第8节已经准确支付总 $P_2=0$，故得到(1)。
这是五个实际方程的共同零，
不是五个独立段首项的形式相消。

## 10. 一个必须继续保留的负矩

从 R555 原表，在固定中心坐标中始终有
$$
s_0=s_0^{[0]}-\frac14(d_s/h)^2.
\tag{41}
$$
因而原词其余部分的速度项不会给 $S_0^y$ 一个未记的正补偿。
在 R556 的两个低尾，
$$
|s_0^{[0]}|\le C R^{-2},\qquad
T_{{\rm low},i}=O(M/(\delta R^{3/2})).
$$
在两个高尾，原
$h\asymp\sqrt M R$、$|d/h|=O(R^{-1})$、
$|k/h|=O(M/R)$ 给
$$
|s_0^{[0]}|\le C M^3/R^2,\qquad
T_{\rm high}=O((\delta M^2R^{3/2})^{-1}).
$$
这些是把 R555 的完整静态式
$4s_0^{[0]}=u\mathcal B$ 代入同一个实际状态盒得到的界。
共同饱和高前缀使用 $h\asymp R$、
$k=O(1)$、$u,\eta=O(R^{-1})$，
故该静态槽为 $O(R^{-2})$；
其原 $\delta R^{3/2}s$ 时长为 $O(1+\log R)$，
在本节尺度上仍趋零。
更早的原短快入静态费用和全部有限过渡静态费用
按 R544/R550 的同词界保留，最后统一归入小 $\delta$ 费用。

所以
$$
\delta R^{3/2}
 \left|\int_{\rm core+finite\ transitions}s_0^{[0]}\,ds\right|
\le C M/R^2+o_\delta(1)=o(1).
\tag{42}
$$
(41)的完整负速度平方仍保在原累计内。
无需把它误称为0，(31)(40)–(42)已经给
$$
\boxed{
\limsup\ \delta R^{3/2}S_0^{y,{\rm total}}
\le-a_{f,*}^2 C_s<0.
}
\tag{43}
$$
这里的极限顺序是有限 $R$ 先足够大、随后 $\delta$ 足够小；
也可取满足全部统一余量的一列正 $(R,\delta)$ 来理解。
因此(40)得到的实际五矩零词仍有
$S_0^y<0$，尚不是矩阵零。

本稿没有把(32)的两个交叉首项为0写成
$S_1^y=R_0^y=0$。在原 trace 关系
$T_0=P_0/4+S_1/2$ 下，五个零之后仍有三个独立二阶矩：
$$
S_1^y,\qquad S_0^y,\qquad R_0^y.
\tag{44}
$$
它们的后续修复须保持本稿全词的真 incoming 和五个端方程。

## 11. 坐标、选择次序与真实结论

R555 的原坐标转换在三个 $P$ 为0后给
$$
T_1^y=T_1^x,\qquad
S_1^y=S_1^x-2\omega_cT_1^x,\qquad
R_1^y=R_1^x-\omega_cS_1^x+\omega_c^2T_1^x .
\tag{45}
$$
所以本稿五个准确零中的第五个是
$$
R_1^y=R_1^x-\omega_cS_1^x=0,
$$
不是尚未支付的 $R_1^x=0$。
同样，剩余 $S_0^y$ 的号也只按本稿固定中心坐标读取。
完整矩阵零当然与坐标无关，但本稿尚未达到该目标。

选择顺序如下。

1. 保 R521/R552 的同一正交母库、实际右锚、
   固定 $\omega_c$、同一原第二规范及全部原算子。
2. 固定 $\mathfrak b>0$、两个低尾阈值和(4)附近的正参数盒；
   固定原 $H$、闭振子形状(11)(12)、四个实际内控和开放反馈段；
   取(39)附近的正幅值盒。
3. 取足够大的有限 $R$，令
   $\lambda=L_h^2/R^2$、$M=(1+\log R)^6$、
   $\varepsilon=R^{-3/4}$，使所有纯 $R$ 的误差足够小。
4. 在该共同参数盒上固定全部有限过渡规则及其真实导数界，
   包括最后向原 $H$ 的下降。它们的完整费用进入 $C_R$。
5. 最后一次选正 $\zeta$，令 $\delta=\lambda^2\zeta$。
   此时从起点一次固定(2)的 $\chi$；
   同一个 $\delta$ 同时支付原长段、快回路、第三交叉项、
   真停止事件及两个实际 IFT 的余量。
6. 先解第8节的真实 $P_2$ 停止坐标，再解(37)的四参数共同零。
   四内控在每个参数点均由第5节同一个真实端点 IFT 给出。

这是把 R556 控制族从起点纳入一个稍大的有限参数盒，
不是事后改变一条已经冻结的路径的 $\chi$。
在每条最终实际词内部，从真正零 $A,T$ 起点到末端只有一个固定规范。
新增参数均不进入 $\nu$；没有拼接两份不同 $\chi$ 的收据。

**定理。** 在上述同母、同右锚和一次规范选择下，存在一条有限光滑实际词，
其原全相位第四 ruling 恒为0，真实原矩满足
$$
P_0=P_1=P_2=T_1=R_1^y=0.
$$
该词末端有真实开放反馈 germ，完整二、三阶历史及全部矩成本
从原零历史起点连续累计。它同时满足(43)的严格负 $S_0^y$ 余量。
其余三个独立二阶矩、frame／位置闭合、
第三／第四 period、同十三规范及最终主问题仍未完成。

### 原来源与本稿新增范围

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：
  原完整 $M_0+M_2$、水平式和有序第三累计；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：
  同母全相位因子、原 $C_k,B$ 正性及唯一高度加速度输入；
- [R544](R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：
  同一个 $\chi$、完整有效 Gram、反馈质量及真正开放反馈 germ；
- [R545](R545-complete-fast-height-loops-and-the-signed-oscillator-energy-transfer.md)：
  原快方程与闭振子面积身份。
  其零 history、不同尺度的具体结论未被直接移植；
  本稿(17)–(30)另付当前 incoming 和尺度；
- [R552](R552-three-exact-p-moments-with-one-gauge-and-a-positive-t1-remainder.md)：
  原长段有序历史、实际有限过渡及统一 $C^1$ 精度；
- [R555](R555-five-remaining-moments-gram-energy-and-real-history-area-interfaces.md)：
  原负速度 Gram、$r_1$ 完整身份和固定中心坐标转换；
- [R556](R556-four-exact-matrix-moments-by-two-real-low-coasts-with-one-gauge.md)：
  三参数实际端图、四个原矩零及严格负 $R_1^y$ 首项。

本稿新增的是一个含真实 incoming 的实际快回路、
一个五方程共同端图及准确的第五中心矩零。
没有执行任何新科学计算。
