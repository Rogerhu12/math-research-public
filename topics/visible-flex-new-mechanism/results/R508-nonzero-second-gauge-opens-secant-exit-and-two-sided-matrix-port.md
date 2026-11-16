# R508：带非零原二阶规范的正割出口与完整 ruling 内的双号矩阵端口

日期：2026-11-16。**新的完整纸面实际构造；没有执行 profile 求积、符号程序、数值秩、开发检查或科学任务。**

[R505](R505-complete-same-mother-ruling-and-real-nonsecant-local-paths.md) 的中心清理参考正割，在固定状态上对两条速度的一阶能量导数都为零。[R507](R507-real-nonsecant-scalar-return-loops-under-one-complete-ruling.md) 因而从另一个明确正规入口构造了完整 ruling 零的 scalar-return 回路，却仍留下真实矩阵漂移。

本稿换一个**从起点固定的原允许第二规范**，准确打开参考正割本身的出口。原规范是八矩中的一个明确方向 $B=P-cR_y$；其系数使完整 odd 正割系数严格为零。一个同形偶母的完整高三阶、低二阶扰动证明参考点的 $\partial_{h_s}\mathscr K$ 真正非零。此后，实际受约束 ODE 可以从已付参考片段的真实左 germ 平滑离开，而不再需要额外桥来达到另一个正规入口。

新增端点结论也是真实的：在同一母库、同一个 $w_\theta,\chi_\theta$、同一个正长度区间上，可以准确保持终端 $k=0,\omega=\omega_0$，并把原矩阵坐标 $m_{p_2}$ 赋为任意充分小的正值或负值。不是负时间或 signed 成本替身；每一个符号对应一条实际完整 ruling 零路径。其它高度、frame、位置、七个矩阵坐标和完整第三、第四基准全部保留，尚未被控制成指定值。

## 1. 新选择的准确范围

保持 R505 的字面同形母库机制：原 R280 等背景十矩、八副本、十二翻号、五个正权 block 全部保留。每个最细实际 profile 是一个共同实偶 $u$ 的平移，所有真实宽度一次收入 $u$。本稿会从起点选择这个共同母的一个具体光滑小二阶扰动；不能将它当作旧冻结库、十九／二十目标或十三行收据原已保持。

取固定坐标 $y=x+\omega_0>0$，右锚仍在同一个真实右 collar。令
$$
\Delta=f^2-g^2,\qquad
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f^2-\phi_\theta^2.
\tag{1}
$$
原三矩使 $\Delta$ 对全部原八矩输出双 collar 紧。

使用原二次算子
$$
P(u,u)=J(u''{}^2),\qquad
R_y(u,u)=u'{}^2+yJ(u''{}^2).
\tag{2}
$$
它们属于同一原 E8；$R_y$ 只是原 $R$ 与固定 $\omega_0P$ 的组合。设
$$
P_\Delta=P(\Delta),\qquad R_\Delta=R_y(\Delta).
$$
以下简写为 $P,R$，不能与几何参数或矩阵坐标混淆。

原完整能量、配对和 scalar 运动都沿 R505/R482；本稿不使用一个新 forcing。最终选择的规范是
$$
\boxed{w_\theta=B(D_\theta),\qquad B=P-cR_y,}
\tag{3}
$$
而不是逐段或逐 $s$ 另选 $w$。原三矩和八副本 cubic 身份保证(3)是原允许的紧二阶齐次规范。

## 2. 一个明确原八矩方向消去整个正割 odd 项

定义
$$
\beta_P=\int R'P',\qquad
\beta_R=\int R'^2>0,\qquad
c=\frac{\beta_P}{\beta_R},\qquad
q=B(\Delta)=P-cR.
\tag{4}
$$
于是
$$
\boxed{\int R'q'=0}
\tag{5}
$$
是完整准确积分身份，非只最高导数或局部根条件。

这两个系数可以从同形母和实际位置完全读出。令最细包中心为 $y_i>0$，真实差幅为
$R_i=a_i^2-b_i^2\ne0$，把所有八、十二、五块的幅度都留在这些 $R_i$ 中。定义
$$
M_j=\sum_iR_i^2y_i^j,\qquad j=0,1,2,
$$
$$
m_4=\int u''{}^4,\qquad
b_u=\int\{(2u'u''-\xi u''{}^2)^2+2u'{}^2u''{}^2\}.
\tag{6}
$$
这里 $\xi$ 是共同母坐标。$m_4,b_u>0$；后者若为零，便有 $u'u''=0$，从 $(u'{}^2)'=0$ 与平端得 $u=0$，矛盾。

**准确公式为**
$$
\boxed{\beta_P=m_4M_1,\qquad
\beta_R=m_4M_2+b_uM_0.}
\tag{7}
$$
证明保留全部 primitive。写
$D_{11}=f'^2-g'^2$、$D_{22}=f''{}^2-g''{}^2$，则
$$
P'=-D_{22},\qquad R'=D_{11}'+P-yD_{22}.
$$
由于 $P$ 两端零，
$\int PD_{22}=0$。同形偶母使每包的
$\int 2u'u''{}^3$ 与 $\int\xi u''{}^4$ 为零，所以第一式成立。

对第二式，原左尾并未先删掉。准确 IBP 给
$$
\begin{aligned}
\int R'^2
&=\int(D_{11}'-yD_{22})^2+2\int PD_{11}'\\
&=\int\{(D_{11}'-yD_{22})^2+2D_{11}D_{22}\}.
\end{aligned}
\tag{8}
$$
第一步中的 $\int P^2$ 正好与
$-2\int yPD_{22}=-\int P^2$ 抵消。然后仅用不交支撑及母的偶性，得到(7)。因此
$$
c=\frac{m_4M_1}{m_4M_2+b_uM_0}>0,\qquad
M_1-cM_2=
\frac{M_1b_uM_0}{m_4M_2+b_uM_0}>0.
\tag{9}
$$

## 3. 正割的完整能量与一个固定第三规范

取实际参考几何
$$
h=H\sqrt{1+v^2},\quad v_s=1+v^2,\quad
h_s=hv,\quad k=0,\quad\omega=\omega_0.
\tag{10}
$$
以真实中心 $v=0$ 为原 history 起点，取 $\mathsf m=0$。原 R488/R73 给
$$
\mathsf A_{\rm sec}
=-\frac v{8h^2}R_y-\frac v8T_y,
\qquad
T_y(u,u)=y^2u'{}^2+yJ(y^2u''{}^2+2u'{}^2).
\tag{11}
$$
这个中心值是真实初值，不是把一条已给前缀在中途重置。

在规范(3)下，完整 second profile 为
$$
q_\Delta^{\rm total}=\mathsf A_{\rm sec}(\Delta)+q.
$$
所以其分子是
$$
V_Z=V_{\rm clean}-V_{Y_q},
\tag{12}
$$
其中 $V_{\rm clean}$ 是 R505(31)(36)的中心清理分子。保该稿记号
$\mathcal L=R-yR'$、$D_*'= -\mathcal L$，有
$$
(V_{\rm clean})_T=-vD_*/8,\qquad
(V_{\rm clean})_B=vR/(8h).
\tag{13}
$$
完整交叉直接积分为
$$
\int V_{\rm clean}'\cdot V_{Y_q}'
=\frac v8\int R'q'.
\tag{14}
$$
例如代入
$V_{Y_q}'=(-q''/2,0,h(q'-yq'')/2)$，
只需 $\mathcal L+yR'=R$ 和两端零便得(14)。

因此完整能量准确是
$$
\boxed{
\mathscr E_B
=\mathscr E_{\rm clean}
+\mathcal E_{h,0,\omega_0}(q,q)
-\frac v{4h}\int R'q'.
}
\tag{15}
$$
最后一项由(5)全消，没有丢原 second square。原物理配对是
$$
\mathcal E_{h,0,\omega_0}(q,q)
=\frac{I_0^y(q,q)}{4h}+\frac h4I_2^y(q,q).
\tag{16}
$$
$I_2^y$ 始终含 $2q'{}^2$。

令 $\nu^{\rm clean}$ 是 R505(38)根据同一个最终母和 $H$ 定义的向量。一次固定
$$
\boxed{
\nu_0^B=\nu_0^{\rm clean}-\frac12I_0^y(q,q),\quad
\nu_1^B=0,\quad
\nu_2^B=\nu_2^{\rm clean}-\frac12I_2^y(q,q).
}
\tag{17}
$$
再用同一个原 Gram 右逆选紧、光滑、周期的 $\chi_\theta$，使
$$
\mathbf I_y(\phi_\theta,\chi_\theta)
=\sin^2\theta\,\nu^B.
\tag{18}
$$
原完整相位身份对任意固定八矩第二规范成立，故(15)–(18)准确支付整条参考正割的完整第四 ruling。

这里有一个真正非零的原二阶规范，但只选一次。后继所有路径都保这个字面 $B,w,\chi$。若此前另一个芽已锁定不同规范，不能再调用(17)；本稿是新的从起点选择。

## 4. 参考正割的速度导数归为一个完整可判定配对

在某个参考状态固定 $h,k,\omega,\mathsf m$，只对实际速度
$\gamma=h_s$ 求偏导。原
$$
W_h=\left(a_h/h,\ 0,\ ya_h\right)
$$
是 second 分子的 $\gamma$ 导数，其中 $a_h$ 是 R482 的完整原函数。

R505(48)证明
$\int V_{\rm clean}'\cdot W_h'=0$，所以(12)给
$$
\boxed{
\partial_\gamma\mathscr E_B
=-\frac2h\Lambda_h(q),\qquad
\Lambda_h(q)=\int V_{Y_q}'\cdot W_h'.
}
\tag{19}
$$
这与 clean 状态的两速度退化不矛盾；新增的一项完全来自真实 $q=B\Delta$。

完整展开为
$$
\boxed{
\Lambda_h(q)=
-\frac1{2h}\int Qq''a_h'
+\frac h2\int\{q'a_h+yq'a_h'-yq''a_h\},
\quad Q=1+h^2y^2.
}
\tag{20}
$$
第一项含全部三阶平方，后三项至多线性含三阶导。$q',a_h$ 本身仅依赖原二阶数据与其真实有限 Volterra 原函数。式(20)没有删除这些低项；下一节会对它们给出统一界，证明一个实际有限母上(19)非零。

## 5. 同形母的真实有限选择使(19)严格非零

### 5.1 先固定一个非零系数窗口

取一个非零实偶 $u_0\in C_c^\infty$，使 $u_0''(0)=r_0\ne0$。这是原允许类别中的选择，不要求特殊数值母或 profile 求积。

对该母计算(4)(6)所定义的实常数，暂记 $c_0$。原实际布局的 $R_i,y_i$ 一次固定。定义
$$
S_h=\sum_iR_i^2(1+h^2y_i^2)^2y_i(1-c_0y_i).
\tag{21}
$$
由(9)，$S_0=M_1-c_0M_2>0$。所以可以选一个固定而严格正的 $h_*$，使 $S_{h_*}>0$。这只是有限多项式在 $h=0$ 处的严格号和连续性，不把 $h=0$ 当作实际几何。

对一个包，$L_i=u'-(y_i+\xi)u''$。由原同锚式，
$$
q''=-2R_i\{u''+cL_i\}u''',\qquad
a_h'=\frac{R_iQ_i}{8h^2}L_i u''',
\quad Q_i=1+h^2(y_i+\xi)^2.
\tag{22}
$$
因此(20)的三阶平方项准确为
$$
\frac1{8h^3}\sum_iR_i^2\int
Q_i^2\{u''+cL_i\}L_i\,u'''{}^2 .
\tag{23}
$$
在 $u=u_0,\xi=0,h=h_*$，其括号总系数是
$$
-r_0^2S_{h_*}<0.
\tag{24}
$$
选一个固定、足够小的对称内窗 $J$，使该总系数在 $J$ 上仍严格负。没有要求每一个包的系数分别同号。

### 5.2 低二阶而高三阶的完整扰动

选非零实偶 $\zeta\in C_c^\infty(J)$，令
$$
u_N=u_0+N^{-5/2}\zeta(\xi)\cos(N\xi).
\tag{25}
$$
这只是一个纸面定义的真实光滑族；本稿未执行任何 $N$ 或求积。其实际估计是
$$
\|u_N-u_0\|_{C^2}=O(N^{-1/2}),\qquad
u_N'''=u_0'''+N^{1/2}\zeta\sin(N\xi)+O(N^{-1/2}).
\tag{26}
$$
对每一个 $N$ 都用其实际(4)定义 $c_N$，于是
$\int R_N'(P_N-c_NR_N)'=0$ **准确**成立，而不是只在极限成立。由(7)，$c_N\to c_0$。

(23)的系数只依赖二阶数据及 $c_N$，所以在 $J$ 上一致收敛到严格负的系数。除以 $N$ 后，
$$
\boxed{
\frac{\Lambda_{h_*}(q_N)}{N}
\longrightarrow
\frac1{16h_*^3}
\int_J\zeta^2
\sum_iR_i^2Q_i^2
\{u_0''+c_0L_{i,0}\}L_{i,0}\,d\xi<0.
}
\tag{27}
$$
这里 $\sin^2(N\xi)$ 的平均 $1/2$ 可由一次真实 IBP 得到；没有使用求积观察。原系数的 $C^2$ 小误差乘 $u_N'''{}^2$ 至多给 $o(N)$。式(20)的后三项有统一有界的二阶／primitive 系数，至多线性乘 $u_N'''$，故为 $O(N^{1/2})$；窗外的三阶导保持固定，给 $O(1)$。因此(27)是完整表达的极限，不是把 principal 的号直接授给未控制余项。

固定一次充分大而有限的 $N$，即有
$$
\Lambda_{h_*}(q_N)<0,\qquad
\partial_\gamma\mathscr E_B>0.
\tag{28}
$$
从此母、$c_N$、$B$、全部布局、$w,\chi$ 都冻结，不再沿几何路径改变。

原 R280 五块相对位置与正幅只依布局：$A_\pm/m^2$ 和两个 $\chi_\pm$ 的差不依母的 $m,\nu$。所以(25)可以从起点嵌入同一实际八／十二／五块，(2)(3)及有序面积保持准确。最后的共同正幅归一不改变上述非零结论。

本稿不把(25)称为保持旧四自然矩、唯一 $A_u$ 镜点或二十高阶目标的纤维扰动。它可能改变那些尚未要求的量；目前只用 R505 字面同形库所需的确切条件。

## 6. 从已付参考片段的真实 germ 平滑离开

选 $v_*\in(0,1)$，例如 $v_*=1/2$，并令
$$
H=\frac{h_*}{\sqrt{1+v_*^2}}.
\tag{29}
$$
以这个 $H$ 完成(10)(17)(18)，在参考点 $v=v_*$ 有 $h=h_*$。由(28)及连续性，选一个足够短的实际参考区间 $[0,L]$，使 $0<v<1$ 且完整
$\partial_\gamma(\mathscr E_B+2\mathbf w_g\cdot\nu^B)$ 始终非零。

带入从正割中心真实积分到此的全部 $\mathsf m$、第三历史、frame、位置；不能把这些入值重新置零。原隐函数定理给该参考轨道邻域中的光滑分支
$$
\gamma=G_B(h,k,\omega,\mathsf m,\upsilon),
\qquad \upsilon=k_s,
\tag{30}
$$
使完整 ruling 为零。实际 ODE 为
$$
\boxed{
h_s=G_B,\quad k_s=\upsilon,\quad
\omega_s=\upsilon/(2h),\quad
\mathsf m_s=M_{\rm raw}(h,k,\omega,G_B,\upsilon).
}
\tag{31}
$$
在 $\upsilon=0$ 时，已付参考正割是(31)的解，局部唯一性保证所得就是它。

现在选择任意充分小、严格内支撑的光滑 $\upsilon(s)$。左 collar 上它准确为零，所以新路径与已付参考片段具有相同的整个真实左 germ；随后可在内部变为非零曲率。原 profile、两个规范和真实 history 初值始终固定，完整二、三阶 ruling 及(31)上的全相位第四 ruling 均准确成立。

这已是从原参考片段直接产生的非正割出口。它不同于 R505 的 clean 参考态：该态退化仍然成立，本稿是用一次真实非零二阶规范打开另一个、完整 paid 的参考态。

## 7. 三个原端点读出有准确满秩：两 scalar 复位与一个真实矩阵坐标

下面证明一个实际矩阵端口，不只说控制函数很多。

对参考区间 $[0,L]$，令 $h_{\rm sec}(s)$ 为(10)的实际高度。取有限控制
$$
\upsilon_z(s)=\sum_{j=1}^3 z_j\psi_j(s),\qquad
\psi_j\in C_c^\infty((0,L)),
\tag{32}
$$
按(31)恢复全路径。原 $p_2$ 矩阵密度在所有几何上准确为
$$
(M_{\rm raw})_{p_2}=-kh/2 .
\tag{33}
$$
这不是从某个 leading 表外推；它就是 R73(9)。

在零控制的真实正割上，$k=0$，故其 $p_2$ history 始终为零。对一个控制变分 $\delta\upsilon=\psi$，原 ODE 逐项给
$$
\delta k(L)=\int_0^L\psi,\qquad
\delta\omega(L)=\int_0^L\frac{\psi(s)}{2h_{\rm sec}(s)}\,ds,
\tag{34}
$$
$$
\boxed{
\delta m_{p_2}(L)
=-\frac12\int_0^L\psi(t)
\left(\int_t^Lh_{\rm sec}(s)\,ds\right)dt .
}
\tag{35}
$$
式(34)中高度变分乘参考 $\upsilon=0$，因此没有漏项；(35)中高度变分乘参考 $k=0$，也准确消失。其它状态、速度与矩阵变分不影响这三个显示的一阶式。

三条真实权函数
$$
f_1(t)=1,\qquad
f_2(t)=\frac1{2h_{\rm sec}(t)},\qquad
f_3(t)=-\frac12\int_t^Lh_{\rm sec}(s)\,ds
\tag{36}
$$
线性独立。甚至有准确 Wronskian
$$
\boxed{
f_2'f_3''-f_2''f_3'
=\frac{1-v(t)^2}{4}>0.
}
\tag{37}
$$
因为原正割 $h_s=hv$、$v_s=1+v^2$ 给
$f_2'=-v/(2h)$、$f_2''=-1/(2h)$、
$f_3'=h/2$、$f_3''=hv/2$。因此不是用一个未读的数学秩或实际采样猜测独立性。

选择三个内点张成(36)的点值空间，再取其附近足够小的实际光滑 bumps，就得到一个严格可逆的(34)(35)矩阵。该选择是有限纸面存在，所有支撑一次冻结，原两端 collar 保留。

定义真实终点映射
$$
\mathcal P(z)=
\bigl(k_z(L),\ \omega_z(L)-\omega_0,\ m_{p_2,z}(L)\bigr).
\tag{38}
$$
它在 $z=0$ 为零，且由(34)–(37)微分可逆。有限维 IFT 因而给每一个充分小的实数 $\eta$ 一条实际控制 $z(\eta)$，满足
$$
\boxed{
k_{z(\eta)}(L)=0,\qquad
\omega_{z(\eta)}(L)=\omega_0,\qquad
m_{p_2,z(\eta)}(L)=\eta .
}
\tag{39}
$$

$\eta$ 可以取正、零、负；所有路径都走同一个正长度 $L$，不是把负目标换成负时间。若 $\eta\ne0$，由(33)知 $k$ 不可能恒零，所以确是非正割路径。

在右 collar，控制又准确为零；(39)使 $k=0,\omega=\omega_0$ 在整个右 collar 成立，而 $m_{p_2}=\eta$ 在该 collar 为真实常数。高度与其余历史沿(31)继续，不假设它们恰等于参考终值。

## 8. 哪些端口和成本仍在同一个实际账中

(39)给的是三个原终点读出的实际开像。没有证明整个 $\mathfrak{sl}_3$ 端点映射满射，也没有把其它七个矩阵坐标的变化消掉。特别不能将 $\eta$ 读出写成一条“只含 $p_2$ 的纯成本”并与其它独立截面任意拼接。

对每个小 $\eta$，以下数据均来自同一个真实路径，必须一起保存：

- 终端高度及其完整 scalar germs；
- frame、中心线位置和原 $x+\omega>0$ 的共同窗口；
- 完整八矩终值及原第三、第四恢复、传递和规范作用；
- 若后来接入周期词，原全部 period 与同一个十三行的真实变化。

左 germ 与参考片段完整相同；右 collar 只支付了所列 $k,\omega,p_2$，并未支付其它端口。R505 的有限分离可以把这些剩余数据放入同一个实际有限映射；但未到达的目标不能靠常秩定理或冗余参数数目自动变成零。

所有新路径和参数位于一个预先选定的紧小盒，按原 ODE 连续依赖可统一保持 $h>0,x+\omega>0$。原桥、prototype 乘数、倒行、$\delta X^*$ 与 Klein 合成的全部基准仍需在最终词中共同支付。本稿没有用原 signed $U$ 的一列替代这些实际段。

## 9. 相比 clean 分支得到的具体新自由度

R505 clean 正割的速度退化是原完整平方事实，不是缺一个数值 Jacobian。这里通过原合法 $w_\theta=B(D_\theta)$ 保持整参考正割可解，同时准确消除其 odd 项，再用完整(20)的三阶平方及统一余项构造一个真正非退化的速度入口。

因此本稿已支付两项此前分离的任务：一个实际已付参考段可以在不更换规范的情况下平滑转入非正割段；而在这种完整 ruling 零族中，原 $m_{p_2}$ 有保终 $k,\omega$ 的双号实际端口。它为继续同一个受约束矩阵控制问题提供真实方向，尚不等于所有矩阵或所有全局周期条件已经控制。

本稿选择的是新的理论母库与基几何，并非重标旧数值曲面或旧十九／二十目标库。主课题的固定度量有限等距族、闭嵌入和厚度仍未达成；全部新结论均是原完整方程中的纸面实际构造。
