# R217：两个左二次尾不变量在 pure-zero 响应上满射，不能联合读出正字符

日期：2026-11-15。**完整纸面证明；没有新的研究编译、profile 求积、函数消元或采样。**

本稿评价 [R213](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md) 尚未确定的两个左二次尾标量。对 R183 中一个明确允许的非对称导数分包圆，这一对标量在 universal pure-zero 的真实响应空间上已经满射到 $\mathbb R^2$。因此它们联合起来仍不能因子化 R196 的正字符 $\lambda_+$。

证明还保留实际几何：用有限配对控制词、同一个整 pure 校正和真实 Klein 闭合，得到四条闭 hook。它们的 $M=0$、$T=\kappa\mathfrak H$、universal pure 零及严格正字符值相同，而两个左尾标量构成非退化平行四边形。至少三条几何不能由任何允许的二、三阶 gauge 支付该固定圆的完整第四 period。

结论只针对本稿选定合法圆上的**两个左尾标量**。没有排除用平台源、全部退化通量与逐 ruling 商等更大联合映射读出 $\lambda_+$，也没有把这四条不同几何视为同一个目标度量的等距族。

## 1. 两个待判定标量

沿用 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的真实成本空间 $U$、完整响应空间 $\mathcal R$ 及 universal pure 投影 $\pi$。记

$$
U_{\mathrm p0}=U\cap\ker\pi,\qquad
\mathcal R_{\mathrm p0}=\mathcal R\cap\ker\pi.
\tag{1}
$$

最终固定一条 R183 的合法三矩圆
$\phi_\theta=cf+sg$，其中 $c=\cos\theta,s=\sin\theta$。
由 R159，任意 $V\in U_{\mathrm p0}$ 在此圆上写为

$$V(f^2,\phi_\theta)=s^2V_d+2csV_e.$$

R213 的真实左 collar 公式说明 $V_d,V_e$ 在那里各为次数至多二的多项式。对实际成本生成元，这来自完整二、三阶场、右锚与 $s$ 历史；由线性延拓适用于 U。定义

$$
\boxed{\mathcal L(V)=\bigl([x^2]V_d,\ [x^2]V_e\bigr).}
\tag{2}
$$

方括号只抽取左 collar 上的唯一多项式系数，不截断活动区间内的函数。对一个实际闭 hook，R213 还给

$$
\mathcal L(V)
=\frac12\left(\int kK_d\,ds,\ \int kK_e\,ds\right).
\tag{3}
$$

式 (3) 中的 k 和真实 forcing 属于该生成元自己的几何；在 U 的线性组合上，(2) 才是统一定义，不给不同几何偷换成同一条 k。

R181 的 $L_f(w)$ 左尾至多仿射，所以全部允许的二阶 hook gauge 不改 (2)。第三 gauge 在 $M=0$ 下也不改 period；R213 已证明 (3) 同时消掉逐 ruling 商中的三矩空间。因而 $\mathcal L(V)=0$ 是固定圆完整第四 range 的必要门。

本稿将证明，存在上述合法圆，使

$$
\boxed{\mathcal L(\mathcal R_{\mathrm p0})=\mathbb R^2.}
\tag{4}
$$

## 2. 一个保持八矩算子的代数导子

始终采用同一正右积分

$$J(a)(x)=\int_x^r a(\eta)\,d\eta.$$

令

$$\mathscr D f=x^2f'-2xf.$$

对 n 线性 profile 算子 A 定义

$$
\delta A(f_1,\ldots,f_n)
=\mathscr D\bigl(A(f_1,\ldots,f_n)\bigr)
-\sum_{\nu=1}^n A(f_1,\ldots,\mathscr Df_\nu,\ldots,f_n).
\tag{5}
$$

对四次相位函数，这就是输出上的 $\mathscr D$ 减去全部四个输入槽的导数。$\mathscr D$ 保持双 collar 为零的光滑输入；(5) 是完整 universal 函数算子的代数运算。**本文不把它视为实际几何的非仿射坐标变换、允许的输入相位控制或一个新的零成本 gauge。**

采用 R73 的八矩坐标
$(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$，以 $E_j$ 表示相应单位方向。直接同锚分部积分给：

| 方向 $E$ | $\delta\Phi_E$ |
|---|---|
| $E_{r_0}$ | $-2\Phi_{r_1}-2\Phi_{s_0}$ |
| $E_{r_1}$ | $4\Phi_{p_0}-2\Phi_{s_1}$ |
| $E_{s_0}$ | $-2\Phi_{s_1}$ |
| $E_{p_0}$ | $-2\Phi_{p_1}-\Phi_{t_1}/2$ |
| $E_{s_1}$ | $4\Phi_{p_1}-2\Phi_{t_1}$ |
| $E_{p_1}$ | $-\Phi_{p_2}$ |
| $E_{t_1}$ | $4\Phi_{p_2}$ |
| $E_{p_2}$ | $0$ |

这里表中下标简写仍指同一个单位方向。为完整支付原函数和符号，记

$$
J_0=J(f''g''),\quad
J_1=J(\eta f''g''),\quad
J_2^*=J(\eta^2f''g''+2f'g').
$$

逐项有

$$
\begin{aligned}
\delta(fg)&=2xfg,\\
\delta(fg'+f'g)&=4fg,\\
\delta(f'g')&=-2xf'g'+2(fg'+f'g),\\
\delta J_0&=-2xJ_0-2J_1-2f'g',\\
\delta J_1&=-2xJ_1-J_2^*-2xf'g',\\
\delta J_2^*&=-2xJ_2^*-2x^2f'g'-4fg.
\end{aligned}
\tag{6}
$$

所有右端边项为零；左端未重锚。对一个系数 $a(x)$，另加
$x^2a'(x)$ 乘原项。将 (6) 代入 R73 的完整六项式，得到变换后的八坐标

$$
\begin{aligned}
\widetilde p_0&=4r_1,&
\widetilde p_1&=4s_1-2p_0,&
\widetilde p_2&=4t_1-p_1,\\
\widetilde r_0&=0,&
\widetilde r_1&=-2r_0,&
\widetilde s_0&=-2r_0,\\
\widetilde s_1&=-2(r_1+s_0),&
\widetilde t_1&=-p_0/2-2s_1 .
\end{aligned}
\tag{7}
$$

局部系数也满足原 $A_0=-A_1'/2$ 和 $A_2=C'-W$，所以这不是只匹配尾系数。式 (7) 即上表。

导子 (5) 对算子组合满足 Leibniz 法则。因此

$$
\delta[E,F]=[\delta E,F]+[E,\delta F].
\tag{8}
$$

R71 已真实可达的第三交换子在 (8) 下闭合。对 R83 的完整第四响应

$$
\begin{aligned}
K_{E,\tau}(F,\phi)
={}&2\tau(\Phi_ED;D)-4\tau(\phi;\phi,\Phi_ED)\\
&+4\Phi_E(\phi,\tau(\phi;D)),\qquad D=F-\phi^2,
\end{aligned}
\tag{9}
$$

同样有

$$\delta K_{E,\tau}=K_{\delta E,\tau}+K_{E,\delta\tau}.\tag{10}$$

所以对由 E8 与 R71 交换子生成的响应，$\delta$ 的每个有限次迭代仍是有限个**真实可实现响应方向**的实线性组合。真正的几何实现来自 R71、R83，不来自把 (5) 冒作一个几何变换。

## 3. 起始 pure-zero 响应及其准确左尾

采用 R215 的

$$
P(a,b)=J(a''b''),\quad
R(a,b)=a'b'+xJ(a''b''),\quad
\tau_R=[P,R],\quad K=K_{P,\tau_R}.
\tag{11}
$$

R215 已由完整原式证明

$$K\in\mathcal R_{\mathrm p0}.\tag{12}$$

输入槽次数不被 (5) 改变，故 universal pure 为零的身份也被 $\delta$ 保持。由 (10)，

$$
K_1=\delta K,\qquad K_3=\delta^3K
\quad\text{都属于 }\mathcal R_{\mathrm p0}.
\tag{13}
$$

下面准确评价它们的 (2)，不调用新规范化或采样。

暂把 f、$\phi$ 看成任意双 collar profiles，置

$$p=f',\quad q=f'',\quad v=\phi',\quad z=\phi''.$$

直接从 (11) 得

$$
\tau_R(a;b,c)
=a'b''c''+
J\!\left(a''(b'''c'+b'c''')+(x-\eta)a''(b''c'')'\right).
\tag{14}
$$

因此 K 的左尾至多仿射，记作 $b_0+x b_1$。其准确两个系数是

$$
\boxed{b_1=-8\int q q'(q q'-z z')\,dx,}
\tag{15}
$$

$$
\boxed{\begin{aligned}
b_0=8\int\bigl\{&
xqq'(qq'-zz')-p q(q')^2-v q q'z'\\
&+2pzz'q'+q^2zz'\bigr\}\,dx.
\end{aligned}}
\tag{16}
$$

积分遍及整个共同 profile 区间；并没有删除平台两侧的原尾。

为核对 (16)，令 $a=PD$、$d_2=q^2-z^2$，则
$a'=-d_2,a''=-d_2'$。写
$\mathsf m(u,w)=\int u''w''$，从 (9)、(14) 的左常数项得到

$$
b_0=2\mathsf m(a,RD)
-8\mathsf m(\phi,R(\phi,a))
+4\mathsf m(\phi,P(\phi,RD)).
\tag{17}
$$

中间的 $-8$ 包含 (9) 最后一项中
$-4P(\phi,R(\phi,PD))$，不能漏掉真实第三历史项。用

$$
(RD)''=2(pq'-vz')-xd_2',
$$

$$
\mathsf m(\phi,R(\phi,a))
=\int z'\{za'+(xz-v)a''\},
\qquad
\mathsf m(\phi,P(\phi,RD))=\int zz'(RD)'',
$$

代入 (17)，再用 $\int z^3z'=0$，即得 (16)。同一展开的左一次项为
$-2\int(d_2')^2-4\int zz'd_2'$，化简为 (15)。边项均由输入导数的真实 compact 支撑消失，不需要 a 的左常值为零。

## 4. 三次导子如何生成二次尾

记 $\mathfrak v$ 为系数泛函的**全部输入变分**

$$
\mathfrak v b(f,\phi)
=D_fb[\mathscr Df]+D_\phi b[\mathscr D\phi].
$$

若某个算子的左尾为 $b_0+b_1x+b_2x^2$，由于

$$\mathscr D1=-2x,\qquad \mathscr Dx=-x^2,\qquad
\mathscr D(x^2)=0,$$

其 $\delta$ 左尾系数满足

$$
\begin{aligned}
b_0(\delta A)&=-\mathfrak v b_0(A),\\
b_1(\delta A)&=-2b_0(A)-\mathfrak v b_1(A),\\
b_2(\delta A)&=-b_1(A)-\mathfrak v b_2(A).
\end{aligned}
\tag{18}
$$

这里 $\mathfrak v^2$ 是线性向量场 $f\mapsto\mathscr Df$ 的二次导数，包含 $\mathscr D^2f$；不是只把输入替成 $f+\epsilon\mathscr Df$ 后漏掉二阶向量场项。

起始 K 的 $b_2=0$，所以 (18) 给

$$
\boxed{
b_2(K_1)=-b_1,\qquad
b_2(K_3)=-6\mathfrak v b_0-3\mathfrak v^2b_1.
}
\tag{19}
$$

## 5. 一个合法圆上两列的准确非零行列式

本节选 R183 中一个更具体但完全允许的子类：在每个导数包上仅 f 或仅 g 变化。稍后说明左三矩补偿仍可保持这一性质，故不假定 f、g 的**值**支撑不交。

定义

$$
A_*=\int(f'')^2(f''')^2>0,\qquad
J_*=\int g\,f''(f''')^2.
\tag{20}
$$

在 f-active 包上 g 为某个常数 G，有
$z=cq,z'=cq',v=cp$；在 g-active 包上 $p=q=q'=0$。式 (15)、(19) 立刻给

$$b_2(K_1)=8s^2A_*,
\qquad
\boxed{\mathcal L(K_1)=(8A_*,0).}
\tag{21}
$$

对于 $K_3$，只需计算 $cs$ 系数。真实微分是

$$
(\mathscr D f)'=x^2q-2f,\quad
(\mathscr D f)''=x^2q'+2xq-2p,\quad
(\mathscr D f)'''=x^2q''+4xq'.
\tag{22}
$$

在 f-active 包上，因为 g=G，

$$
\begin{aligned}
\mathfrak v v&=c\,\mathfrak v p-2sG,&
\mathfrak v z&=c\,\mathfrak v q,&
\mathfrak v z'&=c\,\mathfrak v q',\\
\mathfrak v^2z&=c\,\mathfrak v^2q+4sG,&
\mathfrak v^2z'&=c\,\mathfrak v^2q'.
\end{aligned}
\tag{23}
$$

第二行使用 $\mathscr D^2G=2x^2G$。从 (16) 看，$\mathfrak v b_0$ 的 $cs$ 项只来自 $-vqq'z'$ 中 $\mathfrak v v$ 的 $-2sG$；从 (15) 看，$\mathfrak v^2b_1$ 的 $cs$ 项只来自 $\mathfrak v^2z$ 的 $4sG$。故

$$
[cs]\,\mathfrak v b_0=16J_*,
\qquad
[cs]\,\mathfrak v^2b_1=32J_*.
\tag{24}
$$

这里 $[cs]$ 指直接乘 $cs$ 的系数，而 (2) 使用 $2cs$ 规范。

在 g-active 包上，f 可以是非零常数，但
$q=q'=0$ 以及 $\mathfrak v q=\mathfrak v q'=0$；
虽然 $\mathfrak v^2q=4f$，它在 $\mathfrak v^2(qq')$ 中仍乘零因子。
所以这些包对 (24) 没有遗漏项。双常平台同理。此处明确保留平台值，不能由“导数分包”擅自设 f 或 g 为零。

结合 (19)、(24)，得到

$$
[cs]\,b_2(K_3)=-192J_*,
\qquad
\boxed{\mathcal L(K_3)=(B_*,-96J_*),}
\tag{25}
$$

其中 $B_*=[s^2]b_2(K_3)$ 是由 (16)、(19) 完全定义的有限实数，其具体值不影响独立性。因此

$$
\boxed{
\det\begin{pmatrix}
\mathcal L_d(K_1)&\mathcal L_d(K_3)\\
\mathcal L_e(K_1)&\mathcal L_e(K_3)
\end{pmatrix}
=-768A_*J_*.
}
\tag{26}
$$

### 5.1 准确构造 $J_*\ne0$，并支付三左矩与八 packet

仍取 R183 的原矩形

$$f_0=s_1-s_3,\qquad g_0=s_2-s_4,\qquad s_j'=\rho_j.$$

四个导数支撑从左到右不交，$\rho_j\ge0$、$\int\rho_j=1$。
第一个 f 上升包上 g=0，第三个 f 下降包上 g=1。因此原矩形部分给

$$J_*^{\rm rect}=-\int\rho_3'(\rho_3'')^2.\tag{27}$$

取一个光滑单调平端 step $\chi:[0,1]\to[0,1]$，内部 $\chi'>0$。让 $\rho_3$ 先在长度 a 上按 $\chi$ 上升到 1，再在某个平台后在长度 b 上按 $1-\chi$ 下降至 0；区间外为零，且 $a,b>0,a\ne b$。各拼点都是无限平的。归一化面积之前，

$$
\int\rho_3'(\rho_3'')^2
=(a^{-4}-b^{-4})\,C_\chi,\qquad
C_\chi=\int_0^1\chi'(\chi'')^2>0.
\tag{28}
$$

正的面积归一化仅乘一个正立方因子，所以 (27) 严格非零。

接着执行 R183 的三个左补偿。由于原矩形满足
$f_0'g_0'=f_0''g_0''=0$，三个普通复平方矩
$M_\nu(f_0+ig_0)$ 全为实数。三阶实 Vandermonde 系统给实数 $z_j$，因此可取平方根 $\beta_j$ 为实数或纯虚数。每个新增补偿包于是仅属于 f 或仅属于 g；轴导数性质保持。

f-only 左补偿的 g 值为零，g-only 补偿的 $f''$ 为零，故它们不改 (27)。右侧三个不同的取值平台仍是 $(1,0),(1,1),(0,1)$，所以没有常数 GL2 换基能使这个 pair 的值支撑不交。

最后按 R183 取八个完整基本 packet，幅度

$$a_j=(-1)^j\binom7j^{1/3},\qquad 0\le j\le7.$$

完整 packet 之间 profiles 本身为零，故 (20) 的 $J_*$ 按
$\sum_j a_j^4>0$ 相加，不发生七阶交错抵消。二、三阶 range 仍由原三矩及 $a_j^3$ 的第七有限差分支付。

统一正幅度和正仿射 profile 坐标可放入最终共同物理 I，且保 $A_*>0,J_*\ne0$。具体地，若
$f(x)=C f_*(Hx+d),g(x)=C g_*(Hx+d)$，$C,H>0$，则

$$A_*=C^4H^9A_*^{\rm old},\qquad
J_*=C^4H^7J_*^{\rm old}.$$

本稿的 $K_1,K_3$ 始终在这个**最终坐标 x** 中由 (5)、(11)、(13) 定义；没有假定最后仿射变换只给任意既定读出乘一个常数。
式 (26) 非零，完成 (4)。

## 6. 两个左尾联合也不能因子化 $\lambda_+$

R196 的真实正字符杀全部 $\mathcal R$。而 [R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 给完整算子

$$
H=C_2+\frac1{48}R^{(0)}
+\frac{11}{64}R^{(2)}-\frac{13}{96}R^{(3)}
$$

满足 $H\in U_{\mathrm p0}$、$\lambda_+(H)=1$。若存在
$\ell\in(\mathbb R^2)^*$ 使

$$\lambda_+|_{U_{\mathrm p0}}=\ell\circ\mathcal L,$$

则对 (13) 的两条响应有 $\ell(\mathcal L(K_1))=\ell(\mathcal L(K_3))=0$。
由 (26)，$\ell=0$；这与 $\lambda_+(H)=1$ 矛盾。故

$$
\boxed{\lambda_+|_{U_{\mathrm p0}}\text{ 不经这两个固定圆左尾标量因子化。}}
\tag{29}
$$

也可直接给出 kernel 反例。令

$$
\beta=\frac{\mathcal L_e(H)}{-96J_*},\qquad
\alpha=\frac{\mathcal L_d(H)-\beta B_*}{8A_*},
\quad H_{\rm tail}=H-\alpha K_1-\beta K_3.
$$

则

$$
\pi H_{\rm tail}=0,\qquad
\mathcal L(H_{\rm tail})=(0,0),\qquad
\lambda_+(H_{\rm tail})=1.
\tag{30}
$$

式 (30) 是真实函数空间内的线性组合，不把它宣称为一个实际负成本或一个已经取得的有限路径。

## 7. 保留全部基准的四条实际闭 hook

本节将 (26) 提升为实际几何见证，不把 $\delta$ 或线性 span 当作成本自由加减。

由 (7)–(10)，每个 $K_j$（$j=1,3$）都是有限个 R83 原响应的实线性组合。对其中每一个原响应，R71 的有限小环重复实现所需第三系数，R70 的同一常值 scalar/frame 端口局部族实现小矩阵参数。把相应 R83 配对词有限拼接，可得同端口、frame I 的实际 $M=T=0$ 两字 $Z_{j,+},Z_{j,-}$，使

$$
V_{Z_{j,+}}-V_{Z_{j,-}}=2t_jK_j,\qquad t_j\ne0.
\tag{31}
$$

实系数可以放进第三控制的参数；没有要求一个局部单环直接包含任意大的系数。所有基准及偶参数成本都保留在各个 $V_{Z_{j,\pm}}$ 内。
因为 $\pi K_j=0$，每一对的整 pure 值相同。

在 R180/R210 的闭 hook 背景中，在同一类 Klein prototype 里插入
$Z_{1,\epsilon_1}Z_{3,\epsilon_3}$，其中 $\epsilon_1,\epsilon_3\in\{+,-\}$。
四种组合有相同的 universal pure 成本。选择**同一条** R206 的实际 $M=T=0$ 校正块 D，在四个 ambient 副本中清掉这个共同 pure 值。

这样得到四条有限真实闭几何 $X_{\epsilon_1,\epsilon_3}$，都有

$$M=0,\qquad T=\kappa\mathfrak H,\qquad\pi V=0.$$

每段矩阵为零，完整第四成本准确相加；固定另一符号时，两种翻转给

$$
\Delta_1V=8t_1K_1,\qquad
\Delta_3V=8t_3K_3.
\tag{32}
$$

真正的 frame 与空间位置闭合均按修改后的 prototype 分别由 Klein 字完成，不要求插入块位移为零。全部背景、配对词及同一个 D 先有限选定，再选共同合法 I 与第 5 节的同一个 R183 圆。没有为不同符号改右锚、丢 $s$ 历史或改用不同 profiles。

由 R105 的 $XX^R$ 论证，每个成本都属于 U。R196、(32) 给

$$
\lambda_+(V_{\epsilon_1,\epsilon_3})
=\text{同一个严格正数},
\tag{33}
$$

而它们的 $\mathcal L$ 值由 (26)、(32) 构成非退化平行四边形。因此四个值彼此不同，至多一个等于 $(0,0)$。**至少三条几何的两个左尾必要门之一严格失败，全部允许的二、三阶 gauge 都不能修复其完整 period。**

这没有指明未评价的公共基准使哪一个符号可能通过，也没有声称第四 ruling 已付。四条几何的目标度量一般不同；每一个失败结论都分别在该几何自己的固定目标与同一第一圆上成立。

## 8. 与更大的 joint 读出问题的边界

R215 只排除一个退化通量与 $\lambda_+$ 为倍数；本稿进一步准确排除**两个左二次尾标量的联合因子化**，并给实际四路径见证。两者都保留原右尾、全部真实 $s$ 历史、种子和合法三矩圆。

仍未排除 $\lambda_+$ 经包含整个平台函数、全部 R181 退化通量及其他逐 ruling 商信息的更大联合映射因子化。式 (30) 只让两个左尾为零，未让这些其他数据为零；式 (33) 也不是在比较所有 joint 数据都相同的几何。

本稿不使用 R216 的标准四阶 flat 点门，不将其状态/profile 假设扩大；也不撤销 R196 的 universal 正性。所得新结论是：这两个具体固定圆不变量的真实响应方向已经独立，故它们无法承载那个消掉全部响应的非零正字符。
