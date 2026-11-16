# R556：同一固定规范内两次真实低尾与四个原矩的准确联合零

日期：2026-11-16。**完整原式纸证；没有执行数值、符号、profile、求积、秩或开发检查。**

本稿继续 R552 的同一 R521 母库、同一从起点选定的 $\chi$ 和真零历史。
把最后高尾在一个实际内部 $p_2$ 坐标处停下，加入第二次真实低尾，
再按新的真实水平入值上升。三个有限几何参数给
$$
\boxed{P_0=P_1=P_2=T_1=0.}
\tag{1}
$$
第二次低尾不复制第一次的历史，不重置原 $A,T$；
两次上升高度分别由各自真入值决定。

本稿采用 R552 的共同饱和前缀，改变其后继控制。
不是在已完成的旧 $P_2=0$ 末端删去成本再另起一条词。
两参数 R552 与本稿三参数族所需的有限余量可从起点一起纳入同一个
$(R,\delta,\chi)$ 选择。路径中不再更换规范。

四个原矩同零仍不是全 $M=0$。本稿还给出一个剩余真实槽的严格负首项，
说明下一修复义务没有被四个等式掩盖。

## 1. 原状态、同一 $\chi$ 与共同前缀

仍用
$$
y=x+\omega_c,\quad \eta=\omega-\omega_c,\quad
d=h\eta-k,\quad j=\eta/h+d/h^2,\quad
\mathfrak r=hj=(k+2d)/h .
$$
原密度与水平式准确为
$$
p_2=-kh/2,\quad p_1=-kd,\quad
p_0=-k(1+d^2)/(2h),
$$
$$
t_1=-\mathfrak r p_2/4-1/8-h_s^2/(8h^2),
\qquad j_s=-2dh_s/h^3.
\tag{2}
$$

固定 R544/R552 的
$$
\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\quad
\delta=\lambda^2\zeta,\quad
R=L_h/\sqrt\lambda,\quad M=(1+\log R)^6,\quad
\epsilon_R=M/R .
\tag{3}
$$
原 $w=0$，第三规范 $\chi$ 由同一个 $\nu$ 一次确定。
三个新增参数不进入(3)。

用同一原算子
$$
Y=\Phi_{p_2}^{\,y},\quad Z=\Phi_{t_1}^{\,y},\quad
\mathcal R=\Phi_{r_1}^{\,y},
$$
及 R552 的完整有序形式
$$
\mathcal B_j(E,F)
=I_{j,y}(F\Delta,E\Delta)
-2I_{j,y}\{g,E(g,F\Delta)\}.
\tag{4}
$$
原右积分与其左多项式尾全部保留。记
$$
B_{21}=\mathcal B_2(Z,Y)<0,\quad
B_{12}=\mathcal B_2(Y,Z),\quad
D_*=2B_{21}-B_{12}<0.
$$
这些严格号已经由 R552 同一次足够大的有限正 $\omega_c$ 支付。

令
$$
A_Y=-Q_2/(8c)>0,\quad
Z_*=\sqrt{-K_*/(2A_Y)}>0,\quad
g_j=-Z_*^2Q_j/2>0\ (j=0,2),
$$
$$
C_W=-Z_*B_{21}/(16c)>0.
\tag{5}
$$
这里以 $Z_*$ 表示 R552 的 $z_\infty$；它是一个正实数，不能与算子 $Z$ 混淆。

完整慢历史及原累计坐标是
$$
a=\sqrt R\,\delta A,\quad
b=R\delta^2\widetilde T,\quad
\Gamma_j=\bar\nu_j+\Xi_j(a,b)/R,\quad
z=a_{p_2}=\sqrt R\,\delta\,\mathsf m_{p_2}.
\tag{6}
$$
$\Xi_j$ 与 $\widetilde T$ 均是 R552 的原完整定义。
特别在所有后继段上
$$
db=-da\circ a+\text{完整受控的 }\mathcal C_{\rm slow}\text{ 项}.
\tag{7}
$$

共同真实饱和前缀由原零 $A,T$ 开始，末值满足
$$
a=Z_*Y+O((1+\log R)^2/R),\quad
b=-Z_*^2Y\circ Y/2+O((1+\log R)^2/R),
$$
$$
\Gamma_j=g_j/R+O((1+\log R)^2/R^2)\ (j=0,2),
\quad \Gamma_1=2c+O(R^{-1}),
$$
$$
W_\infty^e=\kappa_e/R^3+O((1+\log R)^2/R^4)>0.
\tag{8}
$$
其全部真实成本以及非 $Y$ 历史以后继续保留。

## 2. 一条三参数真实控制族

固定一个正数 $\mathfrak b>0$，并固定实际内部阈值
$$
a_*=\frac{Z_*}{2},\qquad \vartheta=\frac{a_*}{Z_*}=\frac12 .
\tag{9}
$$
三个可调参数为
$$
\ell_1>0,\quad \ell_2>0,\quad \xi>0,
$$
最终限制在一个严格位于正象限的固定紧盒中。两次低处参考高度相同：
$$
H_{\rm low}=\sqrt{M\xi}.
\tag{10}
$$
第 $i$ 个低尾的真实时长为
$$
T_{{\rm low},i}=\frac{M\ell_i}{\delta R^{3/2}}\qquad(i=1,2).
\tag{11}
$$

控制顺序为：

1. 从(8)沿原反馈下降到(10)，作第一个低尾；
2. 由其**真实末值**选择高目标，使固定当前 $\Gamma$ 的水平参考满足
   $\mathfrak r=\mathfrak b M/R$，再真实上升；
3. 作第一段高尾，准确停在原坐标 $z=a_*$；
4. 继承该点的全部 $A,T,j,\Gamma$，沿同一反馈降到(10)，作第二个低尾；
5. 由第二低尾的真实末值重新选择高目标，
   仍使水平参考满足 $\mathfrak r=\mathfrak b M/R$，再真实上升；
6. 作第二段高尾，准确停在 $z=0$。

两次内部事件均由原 $p_2$ 坐标定义；不以极限曲线代替它们。
参考高度在过渡两端有开放恒值段，整个过程使用同一个 R544 反馈。
不能将“参考高度恒定”误写成实际 scalar 或历史恒定。

### 2.1 第一次低尾和第一次高目标

R552 的完整低尾方程在本稿的参数盒上给
$$
\Delta a_1=-\frac{M\ell_1}{8R}Z
-\frac{\ell_1}{8\xi R}\mathcal R+o^1(M/R),
$$
$$
\Delta b_1=\frac{M\ell_1Z_*}{8R}\,Z\circ Y+o^1(M/R).
\tag{12}
$$
这里及下文的 $o^1$ 都是整个参数盒上的值和一阶参数导数估计；
$\delta$ 最后统一取小。

真实水平无穷高系数因此成为
$$
W_\infty^{(1)}
=C_W\frac{\ell_1}{\sqrt\xi}\frac{\sqrt M}{R^2}\{1+o^1(1)\}>0.
\tag{13}
$$
由当前真入值选择的第一个高目标为
$$
H_f^{(1)}
=\frac{\mathfrak b\sqrt\xi}{C_W\ell_1}
\sqrt M\,R\{1+o^1(1)\}.
\tag{14}
$$
这一步没有免费重置 $j$。实际过渡误差、速度平方及全部矩成本
按 R552 的有限路径接口计入最后的 $C_R\delta$ 小量。

### 2.2 实际内部事件及其完整 incoming

在第一高尾用
$$
\sigma_1=\delta M^2R^{3/2}(s-s_1).
$$
原恒等式准确给
$$
z_{\sigma_1}=-\frac{kh}{2M^2R}<0.
\tag{15}
$$
$k/h=\mathfrak bM/R+O(R^{-1})$，故这个导数一致远离0。
对充分大 $R$，真入值 $z=Z_*+o(1)>a_*$，
从而存在唯一有限、$C^1$ 依赖三个参数的内部停止时刻 $z=a_*$。

令 $w=a_{t_1}/\epsilon_R$。在该事件之前，
$$
w_1(z)=-\ell_1/8+\mathfrak b(Z_*-z)/4+o^1(1).
\tag{16}
$$
第二历史为
$$
a=a_*Y+\epsilon_R w_1(a_*)Z+o^1(\epsilon_R).
\tag{17}
$$
第三历史的完整一阶部分是
$$
\begin{aligned}
b={}&-\frac{a_*^2}{2}Y\circ Y+\epsilon_R b_1(a_*)+o^1(\epsilon_R),\\
b_1(a_*)={}&
\frac{\ell_1Z_*}{8}Z\circ Y
-\int_{Z_*}^{a_*}w_1(v)\,Y\circ Z\,dv
-\int_{Z_*}^{a_*}v\,Z\circ Y\,dw_1(v).
\end{aligned}
\tag{18}
$$
(18)是第二次低尾的真实 incoming。
不能把它改成 $-a\circ a/2$，也不能在内部事件重新把 $b_1$ 设为0。
原 $\mathcal C_{\rm slow}$ 的完整作用保在 $o^1(\epsilon_R)$ 中，
由 R552 的耗散／慢状态估计支付。

## 3. 第二次下降：正 $k$ 的真实来源

在内部事件，完整有效 Gram 满足
$$
\Gamma_j=\vartheta^2g_j/R+O(M/R^2)\quad(j=0,2),
\qquad
\Gamma_1=2c+O(R^{-1}).
\tag{19}
$$
所以 $\Gamma_0,\Gamma_2$ 仍严格正。实际高处
$\mathfrak r=\mathfrak bM/R+o^1(M/R)$。
当前水平无穷高系数由其真入值计算为
$$
W_\infty^{\rm before\,2}
=\frac{\mathfrak r}{h}
+\frac{\Gamma_2}{\Gamma_1h}
+O(\Gamma_0/h^3)
=C_W\frac{\ell_1}{\sqrt\xi}
\frac{\sqrt M}{R^2}\{1+o^1(1)\}>0 .
\tag{20}
$$
第二项相对第一项低 $M^{-1}$。这不是把第一次的旧 $W_\infty$
沿未知历史免费保持；(19)(20)用的是(17)(18)之后的真实入值。

固定该瞬时 $\Gamma$ 的准确参考水平式为
$$
\frac{k_g(h)}{h^2}
=W_\infty^{\rm before\,2}
+2\Gamma_0\int_h^\infty
\frac{dr}{r^4\sqrt{\Gamma_1^2-\Gamma_0\Gamma_2-\Gamma_0^2/r^2}}.
\tag{21}
$$
所以第二次下降全段正 $k$。到低处，
$$
k_{{\rm in},2}
=\frac{\vartheta^2g_0}{3cH_{\rm low}R}\{1+o^1(1)\},
\qquad
p_{2,{\rm in},2}
=-\frac{\vartheta^2g_0}{6cR}\{1+o^1(1)\}.
\tag{22}
$$
$H_{\rm low}^2 W_\infty^{\rm before\,2}=O(M^{3/2}/R^2)$
与(22)的比值为 $O(M^2/R)=o(1)$，故它不改变这个严格号。
实际有限下降相对于(21)的误差仍是最后控制的 $O(C_R\delta)$。

第二个低尾的慢方程完全保留(17)(18)。其新增首项为
$$
\Delta a_2=-\frac{M\ell_2}{8R}Z
-\frac{\ell_2}{8\xi R}\mathcal R+o^1(M/R),
$$
$$
\boxed{
\Delta b_2=\frac{M\ell_2a_*}{8R}Z\circ Y+o^1(M/R).
}
\tag{23}
$$
原 incoming 中的横向 $Z$ 项与新增 $Z$ 的复合为 $O((M/R)^2)$，
属于已控制的下一阶，而非被删除。
(23)给
$$
\Delta\Gamma_2
=-\frac{M\ell_2a_*B_{21}}{8R^2}+o^1(M/R^2)>0.
\tag{24}
$$
整段曲率增量相对于(22)仍为 $O(M^2/R)$，故低尾始终真实 $k>0$。

于是第二低尾之后，
$$
\boxed{
W_\infty^{(2)}
=C_W\frac{\ell_1+\vartheta\ell_2}{\sqrt\xi}
\frac{\sqrt M}{R^2}\{1+o^1(1)\}>0 .
}
\tag{25}
$$
注意(25)的系数是 $\vartheta$，不是后面 $P_0,P_1$ 权重中的
$\vartheta^2$；前者来自(24)对当前 $a_*Y$ 的一次配对。

由这个真入值选择第二高目标，得到
$$
\boxed{
H_f^{(2)}
=\frac{\mathfrak b\sqrt\xi}
{C_W(\ell_1+\vartheta\ell_2)}
\sqrt M\,R\{1+o^1(1)\}.
}
\tag{26}
$$
它通常与(14)不同。沿同一反馈真实上升，继承所有历史。
在最后高尾，(15)的对应版本再次成立，并唯一到达 $z=0$。
由于(6)始终从原零矩阵起点累计，这准确是整词 $P_2=0$。


## 4. 完整三参数端点映射

在本节，每个参数值都已经按原事件准确停在 $P_2=0$。
全部端点函数由同一真实词读取，不是独立段目标的形式和。

### 4.1 有序交叉积分给 $P_1$

由(7)，贯穿两次低尾和两段高尾，
$$
a=zY+\epsilon_R wZ+o^1(\epsilon_R),
$$
$$
db^{[1]}=-wY\circ Z\,dz-zZ\circ Y\,dw.
\tag{27}
$$
其误差具有 R552 第6、10节所需的一阶总变差控制。
出程领先 $w=0$；第一次低尾把 $w$ 降到 $-\ell_1/8$；
两段高尾都有 $dw/dz=-\mathfrak b/4+o^1(1)$；
第二低尾在领先层 $z=a_*$ 处再把 $w$ 降低 $\ell_2/8$。
所以回程的完整领先函数是
$$
w(z)=
-\ell_1/8+\mathfrak b(Z_*-z)/4
-\frac{\ell_2}{8}{\bf1}_{\{0\le z<a_*\}}.
\tag{28}
$$
(28)中的跳表示真实低尾在极限图上的竖段。
实际路径光滑；竖段上的 $da,db$ 都按(23)(27)完整积分，
不是任取一个 Stieltjes 左值或右值。

完整 $z$ 起末均为0，故 R552 的原有序分部积分给
$$
\oint\Xi_2\,dz
=\epsilon_R D_*\oint zw\,dz+o^1(\epsilon_R).
\tag{29}
$$
直接分两段积分(28)，
$$
\boxed{
\oint zw\,dz
=\frac{Z_*^2}{16}(\ell_1+\vartheta^2\ell_2)
-\frac{\mathfrak b Z_*^3}{24}+o^1(1).
}
\tag{30}
$$
第二低尾此前的(18)全部已经包含在(29)，未被对称化或重锚。

原稳定约束和 $p_1=2u p_2$ 的完整恢复于是给
$$
\boxed{
F_{1,R,\delta}:=\frac{\delta R^{5/2}}M P_1
\longrightarrow
-\frac{D_*}{2c}
\left\{\frac{Z_*^2}{16}(\ell_1+\vartheta^2\ell_2)
-\frac{\mathfrak b Z_*^3}{24}\right\}.
}
\tag{31}
$$
$\Gamma_1$ 的变化、$\Gamma_0(u^2+h^{-2})$、原快入和全部有限过渡
按 R552 的精度保留；$M\gg(1+\log R)^4$ 使它们在(31)严格低阶。

### 4.2 原逆高度项给 $P_0$

两个低尾的当前 $Y$ 坐标分别为 $Z_*$ 与 $a_*=\vartheta Z_*$，
故低尾 $p_2$ 密度的首系数分别为 $-g_0/(6cR)$、
$-\vartheta^2g_0/(6cR)$。它们的实际 $h^{-2}p_2$ 成本为
$$
-\frac{g_0\ell_1}{6c\xi\,\delta R^{5/2}},
\qquad
-\frac{\vartheta^2g_0\ell_2}{6c\xi\,\delta R^{5/2}},
$$
各自加一个 $o^1((\delta R^{5/2})^{-1})$。
第二个权重来自真实(19)(22)，不是复制第一次的密度。

原 $u^2$ 项在完整 $Y$ 出回路的领先层相消；
横向误差只给 $O(M/R)$ 的归一化余项。
第一次高尾的逆高度项给 $Z_*$，
两段后继高尾因(14)(26)的高度平方为 $\asymp MR^2$
而仅给 $O(M^{-1})$。因此
$$
\boxed{
F_{0,R,\delta}:=\delta R^{5/2}P_0
\longrightarrow
Z_*-\frac{g_0(\ell_1+\vartheta^2\ell_2)}{6c\xi}.
}
\tag{32}
$$

### 4.3 全部时间成本给 $T_1$

原(2)在两个高尾都给
$t_1=-\mathfrak r p_2/4-1/8-h_s^2/(8h^2)$。
两段同一领先 $\mathfrak r=\mathfrak b M/R$，
其 $z$ 总下降量是 $Z_*+o^1(1)$。
两个低尾则分别有真实负成本
$-M\ell_i/(8\delta R^{3/2})$。
原快入、对数等待和过渡成本都与 R552 同账保留，于是
$$
\boxed{
F_{t,R,\delta}:=\frac{\delta R^{3/2}}M T_1
\longrightarrow
\frac{\mathfrak b Z_*}{4}-\frac{\ell_1+\ell_2}{8}.
}
\tag{33}
$$
两个高尾的 $-1/8$ 项因其实际慢时间长度而低 $M^{-3}$；
真实 $h_s^2$ 成本最后取小 $\delta$ 控制。低尾的 $-1/8$ 绝不删除。
也可由原准确坐标
$a_{t_1}=\sqrt R\,\delta T_1$ 在(28)的末值读出(33)。

## 5. 三参数真零与非退化 Jacobian

记
$$
q=\ell_1+\vartheta^2\ell_2,\qquad
s=\ell_1+\ell_2.
$$
因为 $0<\vartheta<1$，从 $(\ell_1,\ell_2)$ 到 $(q,s)$ 是可逆线性映射。
(31)–(33)的共同零要求
$$
q=\frac{2\mathfrak b Z_*}{3},\qquad
s=2\mathfrak b Z_*,\qquad
\xi=\frac{g_0\mathfrak b}{9c}.
\tag{34}
$$
取本稿固定的 $\vartheta=1/2$，得到
$$
\boxed{
\ell_{1,*}=\frac{2\mathfrak b Z_*}{9},\quad
\ell_{2,*}=\frac{16\mathfrak b Z_*}{9},\quad
\xi_*=\frac{g_0\mathfrak b}{9c}.
}
\tag{35}
$$
三个参数都严格正。

在 $(q,s,\xi)$ 坐标中，
$$
\partial_qF_1=-\frac{D_*Z_*^2}{32c}>0,\qquad
\partial_sF_t=-\frac18,\qquad
\partial_\xi F_0=\frac{g_0q}{6c\xi^2}>0.
\tag{36}
$$
其余非零导数不改变三角消元，故 Jacobian 可逆。
这是一条显示的有限代数证明，不执行新的秩或采样。

先固定一个以(35)为内部点的小正参数盒。
完整(31)–(33)在该盒上 $C^1$ 收敛，所以充分大的有限 $R$、
再统一小的正 $\delta$ 给一个真实近零点
$$
(\ell_{1,R,\delta},\ell_{2,R,\delta},\xi_{R,\delta})
\longrightarrow(\ell_{1,*},\ell_{2,*},\xi_*).
\tag{37}
$$
在该点 $P_0,P_1,T_1$ 准确为0；
最后事件早已按原(6)(15)准确支付 $P_2=0$。
这证明(1)，并非把四个领先项的相消当作实际四个等式。

### 5.1 第二段并未增加未付的长期假设

本稿新增的是固定有限个慢区间及有限过渡，不是重复次数趋无穷。
原 $C_k,B$、反馈质量、刚度和阻尼在所有段上保持严格正界：
$\bar A=O(R^{-1/2})$、$\Gamma_1=2c+O(R^{-1})$，
$|k/h|+|d/h|+|\eta|=O(M/R)$。
低尾的曲率增量相对其正入值为 $O(M^2/R)$；
两个高尾的准确 $z$ 速度都一致远离0。

对 R552 的居中法向方程作参数微分，仍用其稳定基解；
慢变分分别在两个有限低尾坐标和两个有限高尾坐标内积分。
第二低尾的初值是(17)(18)，本来就 $C^1$ 依赖三个参数，
无需新增独立初值自由度。
(20)(25)的正水平系数和
$\ell_1,\ell_1+\vartheta\ell_2>0$
给两个高目标的归一化 $C^1$ 界。
两个内部／最终事件的参数导数由(15)支付。
因此有限次真实组合仍有(31)–(33)所需的 $C^1$ 精度。

恒参考长段的 $j$ 仍用 R552(62)的完整水平分部积分估计，
不把小 $h_s$ 乘上 $O(\delta^{-1})$ 时长来冒充小累计。
所有原 $M_2$、$\mathcal C_{\rm slow}$、加速度势及速度平方成本
在最后同一个 $\delta$ 选择中保留。

## 6. 一个仍未清掉的真实矩：负的 $r_1$ 余量

记 $\mathsf R_1=\int m_{r_1}^{\,y}\,ds$。
由 R73/R548 的完整静态 rank-one 矩阵，逐点准确有
$$
\boxed{
m_{r_1}^{(0)}
=\frac{1+d^2}{h^2}\,t_1^{(0)}.
}
\tag{38}
$$
这仅是静态部分的身份；真实速度二次部分单独保留。

在第 $i$ 个低尾，
$$
t_1^{(0)}=-1/8+O(R^{-2}),\quad
d^2/h^2=O(R^{-2}),\quad h^{-2}=(M\xi)^{-1}+o_\delta(1).
$$
结合其原时长(11)，
$$
\delta R^{3/2}\Delta\mathsf R_{1,i}
=-\frac{\ell_i}{8\xi}+o^1(1).
\tag{39}
$$
两个高尾上 $m_{r_1}^{(0)}/t_1^{(0)}
=u^2+h^{-2}=O(R^{-2})$，
故它们在(39)尺度上的贡献为 $O(M/R^2)=o(1)$。
共同前缀的该槽为更低阶。
全部有限过渡的真实速度二次项和静态项为有限 $C_R$；
恒参考尾的真实 $h_s,k_s=O(C_R\delta)$。
因此原速度二次贡献也在最后选小 $\delta$ 后为 $o(1)$，
并未从(38)免费推广为零。

在实际四矩共同零(37)上，
$$
\boxed{
\delta R^{3/2}\mathsf R_1
\longrightarrow
-\frac{\ell_{1,*}+\ell_{2,*}}{8\xi_*}
=-\frac{\mathfrak b Z_*}{4\xi_*}<0.
}
\tag{40}
$$
所以本稿清掉四个原矩后，仍有一个明确非零的真实余矩。
它是固定 $y$ 坐标的 $r_1$，不声称未经坐标识别的其它单槽有同号；
但全矩阵零当然要求这个槽也为零。

(40)不是对所有同规范路径的不可达结论，只刻画本稿实际四矩零族。
后继需要真正改变这部分原矩，而非继续在相同领先 $Y/Z$
配平图中把它忽略。

## 7. 选择顺序、原锚与实际结论

完整选择顺序为：

1. 保 R552 同一母、固定 $\omega_c$、同一右锚及
   $Q_0,Q_2,B_{21},D_*$ 的原严格号；
2. 固定 R544 原零历史快入、共同前缀和反馈；
3. 固定 $\mathfrak b>0$、内部阈值 $a_*=Z_*/2$，
   在(35)附近选一个固定正三参数盒；
4. 取充分大的有限 $R$，令 $M=(1+\log R)^6$、
   $\lambda=L_h^2/R^2$，支付全部纯 $R$ 的 $C^1$ 误差；
5. 在同一参数盒上固定四条有限高度过渡的规则及其导数界，
   两个高目标按各自真实 incoming 的(14)(26)确定；
6. 最后一次取小正 $\zeta$，令 $\delta=\lambda^2\zeta$，
   同时支付两次低尾、两次高尾、所有实际事件、
   全部过渡成本和三参数 IFT 的余量；
7. 在已固定的同一个 $\chi$ 上选择(37)的参数，读取原四矩零。

原 $A,T$ 从真实零历史累计，第三方程始终是
$$
T_s=-\Phi_{M_{\rm raw}}\circ A+C_s.
$$
(18)(23)(27)明确保留两次低尾之间的有序交叉项。
所有原左右尾、第四累计、frame 和位置都按原方程继续，
没有作为一个不明 baseline 重新设零。
原 R521 全相位因子与真实反馈仍使完整第四 ruling 始终为0。

固定平移坐标的原身份
$$
P_2^y=P_2^x,\quad
P_1^y=P_1^x-2\omega_cP_2^x,\quad
P_0^y=P_0^x-\omega_cP_1^x+\omega_c^2P_2^x,
$$
$$
T_1^y=T_1^x+\omega_cP_2^x/2
$$
说明(1)也是原未平移坐标的四个准确零。

**定理。** 在上述从起点一次选择中，存在由真零历史开始、使用同一个
R521 母库和同一个 $\chi$ 的有限光滑实际词，
其完整全相位第四 ruling 为0，且原
$$
P_0=P_1=P_2=T_1=0.
$$
该同点尚有(40)的严格负 $r_1^y$ 余量。
剩余四个独立二阶矩、frame／位置返回、第三／第四 period、
同十三规范及最终主问题仍未完成。
本稿不使用另一 33 母库的轨道、控制或成本。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：
  原八矩、真实水平关系、静态 rank-one 全表和有序第三累计；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：
  同一母库、全相位和原加速度控制；
- [R544](R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：
  唯一 $\chi$、真零历史入点及全状态反馈；
- [R548](R548-real-history-turn-and-negative-p2-access-with-one-fixed-gram.md)：
  原高历史与完整静态矩阵；
- [R550](R550-positive-horizontal-branch-and-exact-p2-zero-with-one-fixed-gauge.md)：
  共同实际饱和前缀及真实内部坐标；
- [R552](R552-three-exact-p-moments-with-one-gauge-and-a-positive-t1-remainder.md)：
  完整低尾、真实水平目标、全部有序历史、$C^1$ 接口及原成本精度。

本稿没有执行任何新科学计算。
