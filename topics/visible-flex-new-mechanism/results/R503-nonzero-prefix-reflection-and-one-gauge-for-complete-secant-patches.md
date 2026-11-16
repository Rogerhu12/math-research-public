# R503：非零前缀的完整正割反射与同一规范下的真实共用片段

日期：2026-11-16。**完整纸证；没有执行新的积分、profile、符号、rank、几何、优化或开发检查。**

[R500](R500-different-shift-secant-centers-and-real-prefix-divided-difference.md) 给出了真实多中心的必要差商。本稿转向一个可准确通过的方向：在原 E8 内有非零二阶前缀，它们杀掉完整正割 odd 行；更重要的是，围绕同一个全局二阶规范反射这些前缀时，完整 even 部分也逐项保持。于是原真实矩阵桥可以连接有限个具有不同真实二阶历史的标记片段，而这些片段共用同一套完整 ruling 解。

这不是声称连接桥内部已解。全词第四 period、原十三规范、真实总第三与第四成本也不被免费删除。定理首先给**同一个规范下完整片段值的保持**；若第三 Gram 尚未被别的段锁定，还给一次选择同一 $\chi_\theta$、同时清全部标记片段的明确构造。已有保护芽时只能使用其原兼容条件，不另选每段的规范。

## 1. 完整原式与需要保持的真实对象

固定同一个合法圆
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,\qquad
\mathbf I(D_\theta)=0,
\tag{1}
$$
以及物理区间、原右锚、双平 collar。这里不要求 profiles 偶对称。

使用 [R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md) 的完整第三 outer 身份
$$
I_j\{\phi_\theta,\tau(\phi_\theta;D_\theta)\}=0
\quad(\tau\in W,\ j=0,1,2).
\tag{2}
$$
特别，$[A,E]\in W_{71}\subset W$ 对任意 $A,E\in\mathcal E_8$ 的这三个配对都零。式(2)不是说相应三槽算子本身为零。

固定实际全词起点与同一个 $w_\theta,\chi_\theta$。真实二阶历史为
$$
A_s=\Phi_{\mathsf m(s)},\qquad
\mathsf m_s=M_{\rm raw}(h,k,\omega,h_s,k_s).
\tag{3}
$$
[R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 的原商势给
$$
T_s=P_s^{\rm end}-\frac12A_s^2+\tau_s,\qquad \tau_s\in W,
$$
$$
P_s^{\rm end}=\Theta_0+\Pi(j^1S_s)-\Pi(j^1S_0).
\tag{4}
$$
比较两个实际前缀时，必须保同一个真实 $\Theta_0$ 和同一 lift。
若到达相同的几何一阶 jet，两个 $P_s^{\rm end}$ 确实相同；这是(4)的端点身份，不是把第三 incoming 自由归零。

令 $q_s=A_sD_\theta+w_\theta$。原完整 ruling 为
$$
\begin{aligned}
K_s={}&R_s+L_s(q_s)-\mathcal E_s(q_s,q_s)
-4\mathcal E_s\{\phi_\theta,P_s^{\rm end}(\phi_\theta;D_\theta)\}\\
&+2\mathcal E_s\{\phi_\theta,A_s(\phi_\theta,A_sD_\theta)\}
+4\mathcal E_s\{\phi_\theta,A_s(\phi_\theta,w_\theta)\}
-2\mathcal E_s(\phi_\theta,\chi_\theta).
\end{aligned}
\tag{5}
$$
$R_s,L_s$ 恰为 R482(18)(22)，包括全部局部恢复和变化-profile chain；不替成 principal。

在真实正割段
$$
k=0,\quad \omega=\omega_0,\quad
h=H\sqrt{1+v^2},\quad v_s=1+v^2,\quad y=x+\omega_0>0
\tag{6}
$$
上，
$$
A_s=A_*+A_{\rm sec}(v),\qquad
A_{\rm sec}=-\frac{v}{8h^2}R_y-\frac v8T_y .
\tag{7}
$$
所有被比较片段取同一个 $(H,\omega_0)$ 与同样的局部 $v$ 区间；frame 可以相差真实刚体转动，位置可以平移，原配对不受影响。

## 2. 改变真实中心前缀时，整个 ruling 的准确增量

固定一个片段的中心历史 $A_*$，写
$$
q_*=w_\theta+A_*D_\theta .
\tag{8}
$$
将实际中心改为 $A_*+E$，$E\in\mathcal E_8$；相同局部几何使全段历史差一直等于 $E$。两条实际前缀采用同一个(4)，因而端点势项无差。全部真实第三差的 $W$ 部分只按(2)在此配对中消掉，其完整第三算子仍保留。

定义以下三个**完整原配对**：
$$
\begin{aligned}
\mathscr R_{j,\theta}(E;q_*)={}&
-2I_j(q_*,ED_\theta)
+4I_j\{\phi_\theta,E(\phi_\theta,q_*)\}\\
&-I_j(ED_\theta,ED_\theta)
+2I_j\{\phi_\theta,E(\phi_\theta,ED_\theta)\},
\quad j=0,1,2.
\end{aligned}
\tag{9}
$$
$ED_\theta$ 真紧；inner 的单包 primitives 不因此被重新锚定。
$I_2$ 始终含 $2a'b'$。

**定理 1：完整前缀增量。** 对(6)的整个片段，
$$
\boxed{
\Delta K_s(\theta)
=\frac vh\,\beta_\theta^{\omega_0}(ED_\theta)
+\mathbf w(s)\cdot\boldsymbol{\mathscr R}_\theta(E;q_*),
}
\tag{10}
$$
其中
$$
\mathbf w(s)=\left(\frac{1+h^2\omega_0^2}{4h},
\frac{h\omega_0}{2},\frac h4\right)
\tag{11}
$$
是同一物理 $x$ 坐标中的完整三矩权。$\beta$ 是 R494(19)(20) 的完整泛函。

### 证明

将 $A_s\mapsto A_s+E$ 直接代入(5)。除 $L_s$ 外，得到
$$
\begin{aligned}
&-2\mathcal E_s(q_s,ED)-\mathcal E_s(ED,ED)\\
&+2\mathcal E_s\{\phi,A_s(\phi,ED)+E(\phi,A_sD)+E(\phi,ED)\}
+4\mathcal E_s\{\phi,E(\phi,w)\}.
\end{aligned}
\tag{12}
$$
R494 的任意紧外槽恒等式给
$$
L_s(ED)=\frac vh\beta^\omega(ED)
+2\mathcal E_s(A_{\rm sec}D,ED)
-4\mathcal E_s\{\phi,A_{\rm sec}(\phi,ED)\}.
\tag{13}
$$
代 $A_s=A_*+A_{\rm sec}$、$q_s=q_*+A_{\rm sec}D$。

第一项中的 $A_{\rm sec}D$ 与(13)的第一条能量修正相消。
剩下的 $A_{\rm sec}$ 两项之差是原
$[A_{\rm sec},E]$ outer 配对，由(2)准确为零。同理，
$A_*(\phi,ED)$ 与 $E(\phi,A_*D)$ 的差按同一个原交换子身份为零。
于是(12)(13)的余式恰是(9)的 physical 配对，加显示的 $\beta$ 项。证毕。

令
$$
\mathscr R_2^y=
\mathscr R_2+2\omega_0\mathscr R_1+\omega_0^2\mathscr R_0.
$$
则(10)还可准确写成
$$
h\,\Delta K_s=
v\,\beta^\omega(ED)
+\frac{\mathscr R_0+H^2\mathscr R_2^y}{4}
+\frac{H^2\mathscr R_2^y}{4}v^2 .
\tag{14}
$$
所以整个片段不变恰需
$$
\beta^\omega(ED)=0,\qquad
\mathscr R_0=0,\qquad \mathscr R_2^y=0
\tag{15}
$$
对所有相位成立。不能只付第一条后声称两个 even 行已保。

## 3. 一个逐项支付全部 even 增量的非恒前缀反射

固定 $A_g,B\in\mathcal E_8$，使用同一个全局二阶规范
$$
w_\theta=-A_gD_\theta .
\tag{16}
$$
在一个中心取 $A_*^+=A_g+B$，另一个中心取
$A_*^-=A_g-B$。于是
$$
q_*^+=BD_\theta,\qquad q_*^-=-BD_\theta,\qquad E=-2B.
\tag{17}
$$
代入(9)，其第一、第三项分别是
$$
+4I_j(BD,BD),\qquad -4I_j(BD,BD),
$$
第二、第四项分别是
$$
-8I_j\{\phi,B(\phi,BD)\},\qquad
+8I_j\{\phi,B(\phi,BD)\}.
$$
故逐个原矩、逐个相位准确有
$$
\boxed{\mathscr R_{j,\theta}(-2B;BD_\theta)=0,\quad j=0,1,2.}
\tag{18}
$$
没有假定这两个四次量各自零，也没有删掉实际左尾。

由(10)，
$$
\boxed{
K_s^-(\theta)-K_s^+(\theta)
=-\frac{2v}{h}\,\beta_\theta^{\omega_0}(BD_\theta).
}
\tag{19}
$$
因此若
$$
\beta_\theta^{\omega_0}(BD_\theta)=0\quad\text{对全部 }\theta,
\tag{20}
$$
则两个片段的**整个**完整 ruling 一样，使用同一个
$w_\theta,\chi_\theta$ 和同一个真实初端类。

这个保持定理无需第三 Gram 还有自由度。若某一片段已经在一个既定规范下满足全 $K=0$，另一个片段在同一个规范下也满足全 $K=0$。

式(16)是一条准确范围条件。任意已经求出的原 period particular 不一定有这个形式。对一般 $w_\theta$，仍使用定理1，不能把其中的 $q_*$ 偷换成 $BD_\theta$。尤其本稿不把原十三行核中一个未付的新规范选择说成允许操作。

## 4. 完整 odd 核确有非零实际前缀，不靠母的偶性

本节构造(20)中的非零 $B$，不求原旧矩阵的数值秩。

写 $C=\cos\theta,S=\sin\theta$。对任意 $E\in\mathcal E_8$，
$$
ED_\theta=S^2E(f^2-g^2)-2CS\,E(f,g).
\tag{21}
$$
圆的三矩使这里两条完整输出都真紧。定义 local quadratic 密度
$$
Q_y(a,b)=
\frac{(ya'-a)b''''+(yb'-b)a''''}{2}
+y(a''b'''+b''a'''),
$$
$$
F_y=(f'-yf'')f''',\qquad
U_y=Q_y(f,f)-F_y,\qquad
V_y=Q_y(g,g)-F_y.
\tag{22}
$$
R494 的完整式为
$$
\beta_\theta^\omega(\eta)
=\frac12\int\eta(C^2U_y+2CSQ_y(f,g)+S^2V_y).
\tag{23}
$$
因此
$$
\beta_\theta^\omega(ED_\theta)
=\Gamma_{31}^\omega(E)C^3S+
 \Gamma_{22}^\omega(E)C^2S^2+
 \Gamma_{13}^\omega(E)CS^3+
 \Gamma_{04}^\omega(E)S^4,
\tag{24}
$$
其中四条完整原行明确为
$$
\begin{aligned}
\Gamma_{31}^\omega(E)&=-\int E(f,g)U_y,\\
\Gamma_{22}^\omega(E)&=\frac12\int E(f^2-g^2)U_y
                     -2\int E(f,g)Q_y(f,g),\\
\Gamma_{13}^\omega(E)&=\int E(f^2-g^2)Q_y(f,g)-\int E(f,g)V_y,\\
\Gamma_{04}^\omega(E)&=\frac12\int E(f^2-g^2)V_y .
\end{aligned}
\tag{25}
$$
这四个相位单项式在单位圆上独立；例如在 $C\ne0$ 除以 $C^4$ 后是不同的 $\tan\theta$ 次数。所以(20)等价于四条真实线性方程
$\Gamma^\omega(B)=0$，不是相位采样。

$\mathcal E_8$ 的维数为八。故
$$
\dim\ker\Gamma^{\omega_0}\ge4.
\tag{26}
$$
这只是四条完整方程的 elementary linear algebra，不是对旧科学输出重新求秩。式(25)给出了选核所需的真实数据；没有把任意四个形式数当作可独立指定的矩。

### 4.1 可随合法 $\omega$ 使用的明确核公式

每个(25)对 $\omega$ 仿射。取其真实 $4\times8$ 系数矩阵
$G(\omega)=G_0+\omega G_1$，令其在实有理函数域上的秩为 $r\le4$。
若 $r=0$，原八基全在核中。

若 $r>0$，取一个非零的 $r\times r$ minor
$M(\omega)=G_{I,J}(\omega)$，记 $\Delta=\det M$。对每个
$\ell\notin J$，定义原 E8 中的实际多项式列
$$
\boxed{
B_\ell(\omega)=
\Delta(\omega)E_\ell-
\sum_{j\in J}
[\operatorname{adj}M(\omega)\,G_{I,\ell}(\omega)]_j E_j .
}
\tag{27}
$$
由最大秩与 Cramer 恒等式，
$$
G(\omega)B_\ell(\omega)=0
\tag{28}
$$
在 $\Delta\ne0$ 上成立，继而作为多项式身份在所有 $\omega$ 成立。
每列次数至多 $r\le4$。在 $\Delta\ne0$ 的一个合法区间，$\ell$
坐标分别为 $\Delta$，所以这些 $8-r\ge4$ 列独立，并给一个光滑的真实核族。

至多四个实根是这一个所选呈示可能失去独立的位置；不是声称完整核在这些点消失。固定 $\omega_0$ 也可直接选择该点的实际非零 minor，不需要使用整个 pencil。

## 5. 这些核方向确改变完整第二场

为避免把(26)当成只在冗余算子系数中的自由度，给出所需的忠实性。

设原严格不交包为
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,
\qquad (a_i,b_i)\ne(0,0),
$$
且至少三个实际三矩向量
$\mu_i=\mathbf I(u_i,u_i)$ 张成 $\mathbb R^3$。当前库中三个不同中心的共同形状、同宽副本已经满足这一点：
$$
\mu(c)=(m_0,m_1+cm_0,m_2+2cm_1+c^2m_0),\quad m_0>0,
\tag{29}
$$
三个不同 $c$ 的行列式是非零 Vandermonde 乘 $m_0^3$；非零幅度只乘正因子。

假设某个 $E$ 满足
$$
ED_\theta\equiv0\quad\text{对全部 }x,\theta.
\tag{30}
$$
在各实际间隙上，原输出恰为右方微包三矩的真实二次尾
$p_E(\sum_{j>i}d_j\mu_j)$。相邻两间隙的零多项式相减，得到
$$
d_i(\theta)p_E(\mu_i)=0 .
\tag{31}
$$
$d_i(\theta)=a_i^2-(a_iC+b_iS)^2$ 不恒为零，故
$p_E(\mu_i)=0$。三矩张成迫 $p_E(n)=0$ 对任意 $n\in\mathbb R^3$。

[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)
的完整尾表写为
$$
p_E(n)=
(r_0+r_1x-p_0x^2/4)n_0+
(s_0+s_1x-p_1x^2/4)n_1+
(t_0+t_1x-p_2x^2/4)n_2,
$$
$$
t_0=p_0/4+s_1/2.
\tag{32}
$$
恒零便迫原八坐标全部零。所以(30)只可能 $E=0$。

因此任何非零 $B$ 来自(26)或(27)，都会改变某个相位的完整
$BD_\theta$，并因 $Z_2=K_s(D_\theta)-Y_{q_s}$ 真正改变第二恢复场。它不是重新表示同一个零方向，也不是只在末端矩阵记号中改变一个数。

## 6. 一次共同 Gram 选择可清所有反射片段；已锁规范时不重复消费

先固定非零 $B\in\ker\Gamma^{\omega_0}$ 及共同 $A_g$。
在中心历史为 $A_g\pm B$ 的任意有限个相同正割模板上，
(19)(20)给完整 $K^+=K^-$。其 odd 行准确为零。

若没有另一个已经锁定第三 Gram 的保护段，先取一个共同初始
$\chi_\theta^0$，将这一个共同值写成
$$
K_s^0(\theta)=\frac{a_\theta+c_\theta v^2}{h}.
\tag{33}
$$
R488 的原配对给第三规范变化
$$
\delta K_s=-\frac{I_0(\phi_\theta,\delta\chi_\theta)}{2h}
-\frac h2 I_2^y(\phi_\theta,\delta\chi_\theta).
\tag{34}
$$
故一次指定
$$
I_0(\phi_\theta,\delta\chi_\theta)=2(a_\theta-c_\theta),
\qquad
I_2^y(\phi_\theta,\delta\chi_\theta)=2c_\theta/H^2
\tag{35}
$$
便同时清掉全部这些反射模板。

原 R47/R488 的紧 Gram 右逆给同一个光滑、周期的
$\delta\chi_\theta$。对非退化圆 $\phi_\theta$ 不为零；原相位种子处
$D_\theta=0$、$w_\theta=0$，上述目标为零，可以保持该种子。
所有模板只使用这一套函数，绝不逐片另选。

若已有保护芽或原十三行已经锁定三矩，则(35)不再是免费的控制。
此时本稿给的是：**任何一片已付的完整解自动传到它的反射片；**
仍须先让唯一全局规范满足原(35)的兼容值。尤其(16)与两个完整
period 必须来自同一个最终成本；本稿不从 Gram 满射推出这种全局存在性。

## 7. 非对称有限标记字的真实实现与全部未删成本

先给 $A_g$ 和一个固定小 E8 系数盒；将其中全部可能的 $B$ 及所需中心目标一起纳入 R70 的紧参数族。原有限 IFT 可统一固定圈数、连接词与共同物理窗口。随后才在该窗口从起点选 profile 库，并从第4节的核中选一个非零 $B$；核是线性的，缩小 $B$ 即落入预先的盒，不产生先选母、再改窗口的循环。

取任何预先固定的有限符号序列 $\epsilon_j\in\{+1,-1\}$，不要求回文、成对或全路径偶对称。指定标记中心
$$
A_j=A_g+\epsilon_jB .
\tag{36}
$$
所有标记模板取同一(6)。先固定模板的两端真实短过渡及中心两半段原
$M_{\rm raw}$ 积分，再用 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) /
[R469](R469-global-gauge-locking-and-real-prefix-obstructions-between-rational-germs.md) 的实际有限矩阵桥，依次实现(36)。
每个目标都包含此前真实累计，不能只给连接桥一个孤立的
$\pm B$ 数。

负的矩阵目标用正时长实际桥实现，不用负路径。有限参数盒中可选同一个有限词型和光滑依赖。全部 scalar/frame 端 germs、$\omega_s=k_s/(2h)$、共同物理窗口及两端 collars 按原桥合同保留。窗口在全部桥的包络确定后、profile 从起点选择之前统一安排；本稿不把任意旧冻结窄窗口强行放入此构造。

原 R472/R482 保每个真实第三 incoming 的正确类。由于同一全词初端和相同标记几何一阶 jets，(4)在标记片内相同；差在 $W$ 的部分只在(2)的具体 outer 配对中消去。完整 $T$ 本身仍记在字中。

于是得到下列**实际片段定理**：

> 对满足本稿同一点前提的库，在固定共同二阶规范(16)下，可以实际实现任意有限的非对称中心符号序列(36)，这些中心确有不同的第二恢复场，而对应整个正割模板的完整 ruling 全都相同。若原共同第三规范支付其中一个，便同时支付全部；若未被其它段锁定，可按(35)一次选择共同第三规范支付全部模板。

定理没有声称连接桥内部满足 $K=0$，也没有声称总 $M,T,V$ 自动达到原最终目标。后置矩阵/第三复位只能按原完整传递使用。特别 [R472](R472-two-level-prefix-reset-and-unavoidable-ruling-in-actual-return-bridges.md)(5)–(7) 中的所有交叉项与每个真实桥的 $V_B$ 都保留；它们不因(18)被删除。

若在保持 $\tau$ 的最终字中改变了完整 period 源，而要求继续使用同一个 $w_\theta$，就仍须准确支付新的总 period。不能先按(35)完成片段，再在未保 $w_\theta$ 的条件下加成本控制而声称全部片段仍然完成。若后继同点实际截面可共同保 period、十三行及这个规范，才能按其原范围接上；本稿不把那个仍待解决的条件归入本定理。

## 8. 对非偶母和下一真正全路径问题的精确提示

本稿的原增量、四行核与反射相消全部不使用母偶性。但这不等于仅换成非偶母就能解锁原十三规范。

R492(36) 对一般母的准确额外行是
$$
\beta_\theta^\omega(\eta)-\ell_\theta(\eta)
=\left(\frac e{8t}-\frac\omega4\right)
\sum_i\lambda_i\zeta_i\mathfrak p(u_i),
\qquad
\mathfrak p(u)=\int u'(u'')^2 ,
\tag{37}
$$
其中 $\eta=\sum_i\lambda_i u_i+\sum_i\nu_i\chi_i+\eta_{\rm gap}$
在原完整 period 核内。若当前同宽母库另外有
$\mathfrak p(u_i)=c\,M_3(u_i)$，这个额外行已被原
$P_{-4}$ 杀掉。共同形状的非偶平移副本就可能如此。
因此本稿不以“非偶”一词制造新的合法 gauge 行；要走此入口仍须给真实不同 cubic 比值及原全部纤维/布局的联合证据。

当前正向推进不是更大的残差目录，而是(10)保住全部 even 后的
(18)(19)：它给非零、真实可实现、共用完整片段解的二阶前缀反射。
下一必须解决的是这些连接桥自身的
$K=F+C_hh''+C_kk''$，以及同一固定规范的完整 period/十三行接线。
不以已付标记片段代替全词，不以真实桥的末值可达代替其内部方程。

### 来源范围

- R494：任意紧输入的完整正割三槽式与 $\beta$，保原锚；
- R482：真实第三商势与完整 ruling，含变化-profile chain；
- R480：同一个库的全 $W$ outer，不授算子本身为零；
- R259：原 E8、三矩尾与实际左右顺序；
- R70/R469/R472：真实有限桥、二三阶端点类和所有第四基准；
- R47/R488：单套紧 Gram 右逆，只在该套三矩尚允许时使用；
- R492：非偶附加行的准确原十三规范边界。

tail_cost 只窄核了(17)代入(9)的四项抵消与 $\beta$ 因子；本文没有把该窄核冒作真实桥内部或全路径已解。全文无新的科学执行。
