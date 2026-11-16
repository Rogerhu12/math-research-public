# R563：第三个真实低尾、完整有序历史与保留自由参数的六矩零族

日期：2026-11-16。**原式纸证；没有执行数值、符号、profile、求积、秩或开发检查。**

本稿在 R556/R559 的同一个 R521 母库、原右锚和一次规范中，
增加第三个真实低尾。三个正时长分别位于真实原累计坐标
$z\approx Z_*$、$z=\vartheta_2Z_*$、$z=\vartheta_3Z_*$；
不是把三份形式权重当作可任意插入的静态成本。

完整第三 incoming、两种算子复合顺序、每次实际水平系数
$W_\infty$ 和高目标都继续沿同一原 ODE。
随后用一个 R559 型长快高度回路支付 $R_1^y$。
得到一个带自由参数
$(\vartheta_2,\vartheta_3,\ell)$ 的真实 $C^1$ 族，在每个参数点都有
$$
\boxed{P_0=P_1=P_2=T_1=S_0^y=R_1^y=0.}
\tag{1}
$$
其中快形状长度为 $L=\ell\sqrt R$；
原三个低尾时长、共同低高度和快幅值通过同一个实际端图选择。
$\chi$ 不随这些自由参数改变。

剩余两个完整原累计仍是 $S_1^y,R_0^y$。
本稿不声称它们的像已覆盖零，也不把(1)称为全矩阵或 period 返回。
新增实际意义是：在(1)的真实纤维内，长度和两个内部停止位置仍可变化，
便于研究这两个未付端口。

## 1. 同一原数据与三个内部节点

保 R544/R552 的
$$
y=x+\omega_c,\quad \eta=\omega-\omega_c,\quad
d=h\eta-k,\quad j=\eta/h+d/h^2,
$$
$$
\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\quad
R=L_h/\sqrt\lambda,\quad
M=(1+\log R)^6,\quad \delta=\lambda^2\zeta .
\tag{2}
$$
原第二规范为0；profiles、原 seed、共同右锚及固定 $\omega_c$ 不变。
全部控制参数都不进入 $\nu$。

采用原算子
$$
Y=\Phi_{p_2}^{\,y},\quad Z=\Phi_{t_1}^{\,y},\quad
\mathcal R=\Phi_{r_1}^{\,y}
$$
和 R552 的完整有序配对 $\mathcal B_j$。
固定已付的
$$
A_Y=-Q_2/(8c)>0,\quad
B_{21}=\mathcal B_2(Z,Y)<0,\quad
D_*=2B_{21}-\mathcal B_2(Y,Z)<0,
$$
$$
Z_*>0,\quad g_0>0,\quad
C_W=-Z_*B_{21}/(16c)>0,\quad \mathfrak b>0.
\tag{3}
$$
这些都属于同一初选母库，不重新选择母或规范。

三个低尾的正时长参数为 $\ell_1,\ell_2,\ell_3$，
共同高度参数为 $\xi>0$：
$$
H_{\rm low}=\sqrt{M\xi},\qquad
T_{{\rm low},i}=\frac{M\ell_i}{\delta R^{3/2}}.
\tag{4}
$$
内部节点满足
$$
1>\vartheta_2>\vartheta_3>0,\qquad
z_2=\vartheta_2Z_*,\quad z_3=\vartheta_3Z_*.
\tag{5}
$$
先在 $(\vartheta_2,\vartheta_3)=(1/2,1/4)$ 附近选一个固定紧盒，
保持节点严格分离且 $\vartheta_3$ 有正下界。
第一低尾使用原饱和入口 $z=Z_*+o^1(1)$，
第二、第三低尾则准确停在(5)的原累计事件。

原状态仍为
$$
a=\sqrt R\,\delta A,\quad
b=R\delta^2\widetilde T,\quad
\Gamma_j=\bar\nu_j+\Xi_j(a,b)/R,\quad
z=a_{p_2}=\sqrt R\,\delta\,\mathsf m_{p_2}.
\tag{6}
$$
所有 $a,b,z$ 均从原真正起点累计。
(6)只是缩放，不是新的自由初值。

## 2. 第三个低尾以前的完整真实 incoming

先走 R556 的共同前缀、第一次低尾和第一高尾，
准确到达 $z=z_2$；再走第二低尾和第二高尾，
准确到达 $z=z_3$。
这里第二高尾不再停在0。
这两次事件的严格 $z_s<0$ 及真实停止导数沿原 R556 范围保留。

令 $\epsilon_R=M/R$。
在第三低尾入口，完整首阶为
$$
a=z_3Y+\epsilon_R w_3^- Z+o^1(\epsilon_R),
\qquad
w_3^-=-\frac{\ell_1+\ell_2}{8}
       +\frac{\mathfrak b(Z_*-z_3)}4,
\tag{7}
$$
$$
b=-\frac{z_3^2}{2}Y\circ Y
+\epsilon_R b_3^-+o^1(\epsilon_R).
\tag{8}
$$
其中 $b_3^-$ 的两个有序复合必须分别保留：
$$
\boxed{
b_3^-=-\int_{\mathcal P_3}
 \{\,w\,Y\circ Z\,dz+z\,Z\circ Y\,dw\,\}.
}
\tag{9}
$$
$\mathcal P_3$ 是由实际极限词决定的完整前路：
从 $(0,0)$ 出到 $(Z_*,0)$，经过第一低尾竖段，
高尾到 $z_2$，第二低尾竖段，再高尾到 $z_3$。
竖段按 $da,db$ 同时变化的原有序积分读取，
不是随意取一个 Stieltjes 左值或右值。

例如第二低尾已经贡献
$\ell_2z_2 Z\circ Y/8$；它在(9)中存在，
不能把(8)换成 $-a\circ a/2$。
原 $\mathcal R$ 等 $O(R^{-1})$ 横向项也在真实 $a,b$ 中继续累计；
(7)–(9)只显示用于下列首阶的部分。
原 $P_0,R_1$ 费用仍由完整点态表另行读取。

由当前真入值，
$$
\Gamma_j=\vartheta_3^2g_j/R+O(M/R^2)\quad(j=0,2),
\qquad \Gamma_1=2c+O(R^{-1}).
\tag{10}
$$
所以第三低尾以前的 $\Gamma_0,\Gamma_2$ 仍严格正。
没有拿第一低尾的 old Gram 代替(10)。

## 3. 原水平系数与第三段的正 $k$

写 $\vartheta_1=1$，并定义正的部分和
$$
q_i^{[1]}=\sum_{j=1}^{i}\ell_j\vartheta_j.
$$
它们不是第三 history 的替代物，只用于记录实际首系数。
R556 两次原式计算以及以下相同的单段推导给
$$
W_\infty^{(i)}
=C_W\frac{q_i^{[1]}}{\sqrt\xi}
       \frac{\sqrt M}{R^2}\{1+o^1(1)\}.
\tag{11}
$$

为核第三次，先由第二高尾末端的真实
$\mathfrak r=hj=\mathfrak bM/R+o^1(M/R)$
及当前(10)计算入值
$$
W_\infty^{\rm before\,3}
=C_W\frac{\ell_1+\vartheta_2\ell_2}{\sqrt\xi}
       \frac{\sqrt M}{R^2}\{1+o^1(1)\}>0.
\tag{12}
$$
固定这一瞬时原 Gram 的准确水平参考是
$$
\frac{k_g(h)}{h^2}
=W_\infty^{\rm before\,3}
+2\Gamma_0\int_h^\infty
 \frac{dr}{r^4\sqrt{\Gamma_1^2-\Gamma_0\Gamma_2-\Gamma_0^2/r^2}}.
\tag{13}
$$
因此实际有限下降的参考全段正 $k$。
在低处，原(10)(13)给
$$
k_{{\rm in},3}
=\frac{\vartheta_3^2g_0}{3cH_{\rm low}R}\{1+o^1(1)\}>0 .
\tag{14}
$$
$H_{\rm low}^2W_\infty^{\rm before\,3}$ 与(14)的比值为
$O(M^2/R)=o(1)$。
实际下降误差由同一 R544 反馈在最后取小 $\delta$ 后控制，
不改变这个严格号。

第三低尾的完整静态算子主项为
$-Z/8-\mathcal R/(8M\xi)$；
其它原矩系数为 $O(R^{-1})$，
真实速度二次项仍按原反馈计入。
于是
$$
\Delta a_3=-\frac{M\ell_3}{8R}Z
-\frac{\ell_3}{8\xi R}\mathcal R
+O^1(M/R^2)+o_\delta^1(R^{-1}),
\tag{15}
$$
$$
\boxed{
\Delta b_3=\frac{M\ell_3z_3}{8R}\,Z\circ Y
+o^1(M/R).
}
\tag{16}
$$
(16)从原 $db=-da\circ a+\mathcal C_{\rm slow}$ 取得，
入口就是(7)–(9)。
新 $Z$ 增量与旧横向 $Z$ 项的复合为 $O((M/R)^2)$，
仍在真实累计中；没有重置它。
原 $\mathcal R$ 增量对 $b$ 为 $O(R^{-1})$，
低于(16)的尺度，但并不从原 $T$ 删除。

完整有效 Gram 的首变化为
$$
\Delta\Gamma_2
=-\frac{M\ell_3z_3 B_{21}}{8R^2}
+o^1(M/R^2)>0.
\tag{17}
$$
在低处，$W_\infty$ 对 $\Gamma_2$ 的主导导数为
$(2cH_{\rm low})^{-1}$；
$\Gamma_0$、$\Gamma_1$ 与真实水平偏差给低阶项。
因此
$$
W_\infty^{(3)}
=C_W\frac{\ell_1+\vartheta_2\ell_2+\vartheta_3\ell_3}{\sqrt\xi}
       \frac{\sqrt M}{R^2}\{1+o^1(1)\}>0,
\tag{18}
$$
即(11)的第三次实际版本。
第三低尾曲率的相对变化仍为 $O(M^2/R)$，
故整个低尾保持 $k>0$。

由这个真正末值选择第三高目标，使水平参考
$\mathfrak r=\mathfrak bM/R$，得到
$$
\boxed{
H_f^{(3)}
=\frac{\mathfrak b\sqrt\xi}
 {C_W(\ell_1+\vartheta_2\ell_2+\vartheta_3\ell_3)}
 \sqrt M\,R\{1+o^1(1)\}.
}
\tag{19}
$$
随后实际上升、继续完整历史，并沿第三高尾到最后的小停止值 $z=v$。

三个高尾均使用各自真实目标。
每段的原慢时钟 $\sigma_i=\delta M^2R^{3/2}(s-s_i)$ 给
$$
z_{\sigma_i}=-kh/(2M^2R)<-c_*<0.
\tag{20}
$$
正部分和、严格分离节点及共同紧参数盒使 $c_*$ 可统一固定。
故三个真实事件和三个高目标对所有参数一阶光滑。

## 4. 全三低尾词的五个原端图

在本节先停在 $z=0$。
令
$$
q_0=\ell_1+\ell_2+\ell_3,\quad
q_2=\ell_1+\vartheta_2^2\ell_2+\vartheta_3^2\ell_3,\quad
q_4=\ell_1+\vartheta_2^4\ell_2+\vartheta_3^4\ell_3.
\tag{21}
$$
原完整领先回路为
$$
w(z)=-\ell_1/8+\mathfrak b(Z_*-z)/4
-\ell_2{\bf1}_{z<z_2}/8-\ell_3{\bf1}_{z<z_3}/8.
\tag{22}
$$
全部竖段仍按(9)(16)的真实双变量积分处理。

由原有序恒等
$\oint\Xi_2 dz=(M/R)D_*\oint zw\,dz+o^1(M/R)$，
以及每个低尾的完整逆高度与时间费用，得到
$$
\begin{aligned}
\frac{\delta R^{5/2}}M P_1
&\longrightarrow
-\frac{D_*}{2c}
 \left(\frac{Z_*^2q_2}{16}
             -\frac{\mathfrak bZ_*^3}{24}\right),\\
\delta R^{5/2}P_0
&\longrightarrow Z_*-\frac{g_0q_2}{6c\xi},\\
\frac{\delta R^{3/2}}M T_1
&\longrightarrow \frac{\mathfrak bZ_*}{4}-\frac{q_0}{8},\\
\delta R^{3/2}R_1^y
&\longrightarrow-\frac{q_0}{8\xi},\\
\frac{\delta R^{7/2}}M S_0^y
&\longrightarrow\frac{A_Y^2Z_*^4}{4}
 \left(\frac{2\mathfrak bZ_*}{5}-q_4\right).
\end{aligned}
\tag{23}
$$
各项都是同一完整词上的 $C^1$ 极限。
最后一行使用 R559 的完整原速度账：
最早快准备的归一负费用为 $O(R^{-1/2}/M)$，
饱和等待静态费用为 $O((1+\log R)/M)$，
各有限桥和恒参考尾速度费用最后用同一个 $\delta$ 支付。
增加的是一个固定数量的第三低尾及第三高尾，不改变这些界的类型。

### 4.1 新增第三段的 $C^1$ 范围

第三入口是原(7)–(9)的光滑真实状态；
不是一个新独立初值。
在新增低慢时间中，$a,b$ 增量为 $O(M/R)$；
在第三高慢时间中，它们保持原 $O(1)$ 盒。
原居中法向系统的刚度、阻尼和反馈质量在这些盒上有统一正余量。
先在三个有限低／高慢区间中控制状态与变分，
再用原稳定法向卷积恢复实际速度；
不能对全部 $O(\delta^{-1})$ 物理时长取未经缩放的 Gronwall。

水平量仍使用 R552 的准确分部积分
$$
j-j_{\rm in}
=[\mathcal J]_{\rm in}^{s}
-\int\mathcal J_\Gamma\Gamma_s\,ds
-2\int(d-q_\Gamma)\frac{h_s}{h^3}\,ds.
\tag{24}
$$
所以第三恒参考尾也没有把逐点小 $h_s$ 乘长时钟当成小累计。
(12)(18)的严格正值支付第三高目标的参数导数；
(20)支付新增内部和最终停止事件的导数。
由最大区间上的同一联合盒改进，第三段真实存在到所需端点，
并保(23)的全部一阶精度。


## 5. 正权先作为代数根，随后才进入实际端图

先只解(23)的四个 core 极限方程
$P_1=P_0=T_1=S_0^y=0$。
它们要求
$$
q_0=2\mathfrak bZ_*,\quad
q_2=2\mathfrak bZ_*/3,\quad
q_4=2\mathfrak bZ_*/5,\quad
\xi_*=\frac{g_0\mathfrak b}{9c}.
\tag{25}
$$
置 $w_i=\ell_i/(2\mathfrak bZ_*)$。
在 $\vartheta_2=1/2,\vartheta_3=1/4$ 处，
$$
\boxed{(w_1,w_2,w_3)=(107,440,128)/675}
\tag{26}
$$
严格为正，且直接有
$$
\sum w_i=1,\qquad
\sum w_i\vartheta_i^2=1/3,\qquad
\sum w_i\vartheta_i^4=1/5.
$$
例如两个后式的分子分别是
$107+110+8=225$、
$107+440/16+128/256=135$。
这里只是有限有理恒等，不是执行一次权重搜索。

从 $(\ell_1,\ell_2,\ell_3)$ 到 $(q_0,q_2,q_4)$ 的矩阵是
节点 $\vartheta_i^2$ 的 Vandermonde 矩阵，其 determinant 为
$$
\prod_{i<j}(\vartheta_j^2-\vartheta_i^2)\ne0.
\tag{27}
$$
因此在(26)附近，(25)的正根随
$(\vartheta_2,\vartheta_3)$ 光滑变化；
缩小外参数盒后所有 $\ell_i$ 有共同正下界。

到这里，(26)仍只是一个极限端图的正根。
它的实际可实现性需要第2–4节已经建立的第三真实 low、
有序 history、正 $W_\infty$ 和 $C^1$ 端图。
不能从(26)本身推出一条真实路径。

## 6. 更长的快回路，并保留长度为自由参数

从第三高尾末端沿原反馈有限下降到原 $H$，
继承全部真实 $A,T$。其缩放入值仍满足
$$
\delta A_{\rm in}=O(M/R^{3/2}),\quad
\delta^2T_{{\rm third},{\rm in}}=O(M/R^2),
$$
且开放恒参考段有 R559 的真实强准备。
不将第三段的有序历史重设为0。

采用 R559 的同一固定 $\psi$ 与
$$
D_L=\psi_L'',\quad
f_L=-(\psi_L''+\psi_L)/\beta,\quad
\psi_L(\tau)=\sqrt L\,\psi(\tau/L),\quad
\beta=B(H,0)/(2c),
$$
但本稿取
$$
\boxed{L=\ell\sqrt R,\qquad \varepsilon=R^{-3/4}.}
\tag{28}
$$
$\ell$ 在任意预选的固定正紧盒内变化；
高度领先形状是 $H+\varepsilon a f_L$。
这比 R559 的特定长度增加了一个 $M^{1/4}$ 因子，
所以必须核其统一接口，不能只换字母调用固定区间结论。

令 $\sigma=\varepsilon\sqrt L$、
$a_R=M/R^{3/2}$、$g_R=M/R^2$。
原长快证明所需的小量现在为
$$
\sigma=O(R^{-1/2}),\quad
a_RL=O(M/R),\quad
g_RL^2=O(M/R),\quad
L^{-2}=O(R^{-1}),
\tag{29}
$$
全部趋0，且
$$
L(a_R\sigma+\sigma/L+\sigma^2)\longrightarrow0.
\tag{30}
$$
完整第三增量中的三个非静态项分别为
$$
a_R\sigma^2/L=O(M/R^3),\quad
\sigma^2/L^4=O(R^{-3}),\quad
\sigma^3/L^2=O(R^{-5/2})=o(g_R).
\tag{31}
$$
因此 R559 的完整历史盒、正振子能量、
真实因果核与四个末内控估计逐式适用。
原 $-\int M_2\circ A_{\rm in}$、两个端速度势与第三面积均仍保留；
没有靠历史为0或改变 $\chi$ 取得(29)–(31)。

在真正末端开放反馈 germ 之后，
令
$$
C_1=\frac{\int(\psi')^2}{8H^4\beta^2},\qquad
C_3=\frac{\int(\psi''')^2}{4H^2}.
$$
新增回路的完整成本为
$$
\begin{aligned}
\delta R^{3/2}\Delta R_1^y
 &=a^2C_1+o^1(1),\\
\frac{\delta R^{3/2}}M\Delta T_1
 &=-a^2H^2C_1/M+o^1(M^{-1}),\\
\frac{\delta R^{7/2}}M\Delta S_0^y
 &=-\frac{a^2C_3}{M\ell^4}\{1+o^1(1)\}.
\end{aligned}
\tag{32}
$$
第三项如今在 core 的 $S_0$ 首尺度上趋零，
但实际端图仍准确保留它并调整原低尾参数。
这就是第三个真实低尾带来的余地。

两个交叉增量仍不能删：
$$
\boxed{
\begin{aligned}
\delta R^{5/2}\Delta S_1^y
 &=-\frac{a^2 I_2}{4H^2\beta\ell^2}+o^1(1),\\
\delta R^{5/2}\Delta R_0^y
 &=+\frac{a^2 I_2}{8H^4\beta\ell^2}+o^1(1),
\qquad I_2=\int(\psi'')^2>0.
\end{aligned}}
\tag{33}
$$
这些是新增回路的原增量，不是完整词余两槽的最终值。
core 端参数会随 $\ell$ 的真实根而变化，
其对两槽的贡献必须另外读取，不能用(33)替代。

## 7. 带三个外参数的实际六矩共同零

外参数为
$$
\vartheta=(\vartheta_2,\vartheta_3,\ell).
$$
内参数为
$$
(\ell_1,\ell_2,\ell_3,\xi,a).
$$
最后高尾的小停止位置 $v$ 仍先通过原
$\sqrt R\,\delta P_2$ 的实际 IFT 选择。
后续有限下降、长度 $O(\delta L)$ 的快回路及全部内控
有真实静态 $p_2$ 增量；
其归一式为
$$
\sqrt R\,\delta P_2^{\rm total}
=v+O^1(C_R\sqrt R\,\delta)
+O^1(C_R\sqrt R\,\delta^2L).
\tag{34}
$$
所以同一正小 $\delta$ 使 $\partial_v$ 接近1，
得到 $P_2=0$ 的实际事件。
$v$ 的两个小符号都处在原末高尾的开放 $z_s<0$ 区间内。

在(34)已经清零的真实族上，读取五维端图
$$
\mathcal F=
\left(
\frac{\delta R^{5/2}}M P_1,\ 
\delta R^{5/2}P_0,\ 
\frac{\delta R^{3/2}}M T_1,\ 
\frac{\delta R^{7/2}}M S_0^y,\ 
\delta R^{3/2}R_1^y
\right).
\tag{35}
$$
其共同 $C^1$ 极限为
$$
\begin{aligned}
F_1^\infty&=-\frac{D_*}{2c}
 \left(\frac{Z_*^2q_2}{16}
              -\frac{\mathfrak bZ_*^3}{24}\right),\\
F_0^\infty&=Z_*-\frac{g_0q_2}{6c\xi},\\
F_t^\infty&=\frac{\mathfrak bZ_*}{4}-q_0/8,\\
F_s^\infty&=\frac{A_Y^2Z_*^4}{4}
       (2\mathfrak bZ_*/5-q_4),\\
F_r^\infty&=-q_0/(8\xi)+a^2C_1 .
\end{aligned}
\tag{36}
$$
这里 $\ell$ 是真正保留下来的外参数：
它在有限实际端图中存在，但不进入(36)的首项。

在(25)(26)的正根上，取
$$
a_*^2=\frac{2\mathfrak bZ_*}{8\xi_*C_1}>0.
\tag{37}
$$
以 $(q_2,q_0,q_4,\xi,a)$ 作内坐标，
原五维 Jacobian 可按以下五个非零元素三角消元：
$$
-\frac{D_*Z_*^2}{32c},\qquad
-\frac18,\qquad
-\frac{A_Y^2Z_*^4}{4},\qquad
\frac{g_0q_2}{6c\xi^2},\qquad
2aC_1.
\tag{38}
$$
再结合(27)，对原五个内参数也可逆。

先固定节点和长度的一个外紧盒，并取包含其全部正极限根的内正盒。
充分大的有限 $R$、最后同一小正 $\delta$ 后，
参数型 IFT 给
$$
(\ell_1,\ell_2,\ell_3,\xi,a)
=\mathcal Q_{R,\delta}(\vartheta_2,\vartheta_3,\ell),
\tag{39}
$$
它是实际 $C^1$ 函数，且所有三个低尾时长仍严格正。
在每个(39)上，(35)五项准确为0，
(34)已经支付第六项 $P_2=0$。
于是整个外参数盒上都有(1)。

真实 $T_1$ 和 $S_0$ 的快费用(32)已通过(39)一起支付。
它们不是在先取 core 根之后另行忽略。
同样，末端四内控由当前 incoming 的真正端点 IFT 给出，
不是独立选一个局部特解来接每个参数点。

## 8. 选择次序与可使用的后继范围

本稿只增加固定有限个原控制段。选择顺序为：

1. 保同一 R521/R552 母、固定右锚、固定 $\omega_c$、
   原全部严格号与同一个 R544 反馈；
2. 在 $(1/2,1/4)$ 附近固定严格分离的外节点盒，
   固定一个正长度盒和原 $\psi$、末内控规则；
3. 用(25)–(27)(37)固定正内参数盒，
   保所有真实部分和 $q_i^{[1]}$ 有统一正下界；
4. 取充分大的有限 $R$，从而固定
   $M,\lambda,\varepsilon$ 及整个外盒上的有限 $L$；
5. 固定全部有限实际高度过渡及导数界，
   每个高目标仍由其当前真实 incoming 选择；
6. 最后一次取小正 $\zeta$，$\delta=\lambda^2\zeta$，
   从起点固定唯一的 $\chi$，
   同时支付三低／高段、增长快区间、事件、末 germ
   和所有原成本的统一余量；
7. 在这份固定规范内使用(34)(39)选几何参数。

原 $A,T$ 一直从真正零 history 起点恢复，
第三方程始终为
$$
T_s=-\Phi_{M_{\rm raw}}\circ A+C_s.
$$
(9)(16)保第三低尾以前的全部有序交叉；
原 R521 全相位因子和真实加速度控制使完整 ruling 恒为0。
所有额外原型、第四累计、frame 和位置均继续按原 ODE，
没有因端图只读取六个数而删除。

在固定中心坐标中，(1)后剩余矩阵仍为
$$
\begin{pmatrix}
0&0&-4R_0^y\\
0&2S_1^y&0\\
0&0&-2S_1^y
\end{pmatrix}.
\tag{40}
$$
因此后继的准确问题是读取同一(39)族上的
$$
\vartheta\longmapsto
\bigl(S_1^y(\vartheta),R_0^y(\vartheta)\bigr).
\tag{41}
$$
不能只用(33)把(41)冒充一条已知双向线。
实际上，原 $R_0^y$ 有一个仍严格为正的完整首项。
R555 的静态表给低尾
$$
\rho=h^{-2}+u^2=(M\xi)^{-1}+o(M^{-1}),\qquad
\mathcal B=u\mathcal A+2p_0=A_Yz_i^2/R+o(R^{-1}),
$$
故
$$
\delta R^{5/2}R_0^y\big|_{\rm low}
\longrightarrow\frac{A_YZ_*^2q_2}{8\xi}>0.
\tag{42}
$$
高尾、共同饱和前缀在此尺度上分别为 $O(M/R^2)$、
$O((1+\log R)/R^2)$。
原最早快准备的完整速度费用为
$O(\lambda^2/\delta)$，归一后是 $O(R^{-3/2})$；
其余真实有限桥与尾速度费用仍在同一个 $\delta$ 中支付。
因此在实际六零族(39)上，
$$
\boxed{
\delta R^{5/2}R_0^y
\longrightarrow
\frac{A_YZ_*^2(2\mathfrak bZ_*/3)}{8\xi_*}
+\frac{a_*^2I_2}{8H^4\beta\ell^2}>0.
}
\tag{43}
$$
这个号在外参数紧盒上严格一致。
所以第三低尾释放的自由参数并不能在当前机制内清掉 $R_0^y$；
后继必须给真正不同的原负 $R_0$ 作用，而非只重配这些正时长。
本稿没有计算(41)的完整 $S_1$ 次阶像。

**实际定理。** 同一 R521 母库、同一右锚和一次 $\chi$ 下，
存在上述带三个外参数的有限光滑真实 $C^1$ 族。
每个参数点均由原零 $A,T$ 开始，
完整全相位第四 ruling 恒为0，
原六个固定中心矩满足(1)，末端有真实开放反馈 germ，
并保(43)的严格正 $R_0^y$ 余量。
第三个低尾的节点、时长与其后的高目标都由原累计事件和
真实 incoming 决定；不是正形式权重的任意拼接。

这个定理提供了实际六零纤维中的新自由度，
没有完成两个余矩、frame／位置、第三／第四 period、
同十三规范或最终主目标。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：
  全矩、原静态低尾表及真实水平式；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：
  同一母库、全相位与原加速度控制；
- [R544](R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：
  唯一规范、真零历史入口与完整反馈；
- [R552](R552-three-exact-p-moments-with-one-gauge-and-a-positive-t1-remainder.md)：
  有序配对、完整低尾和 $C^1$ 长段恢复；
- [R555](R555-five-remaining-moments-gram-energy-and-real-history-area-interfaces.md)：
  原剩余矩、负速度 Gram 和中心坐标；
- [R556](R556-four-exact-matrix-moments-by-two-real-low-coasts-with-one-gauge.md)：
  两次低尾的真实 incoming、正 $W_\infty$ 与实际内部事件；
- [R557](R557-five-centered-matrix-moments-with-a-real-fast-height-loop-and-one-gauge.md)：
  非零 incoming 下的四个真实末内控；
- [R559](R559-six-exact-matrix-moments-by-a-slow-fast-height-loop-with-one-gauge.md)：
  完整 $S_0$ 净首项、增长快区间的有序历史和正振子能量。

本文没有执行任何新科学计算。
