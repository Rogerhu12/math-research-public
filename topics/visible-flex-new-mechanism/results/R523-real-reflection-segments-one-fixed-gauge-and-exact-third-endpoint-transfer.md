# R523：完整 ruling 的真实反射段、一次固定规范与准确第三端口

日期：2026-11-16。**新的原式纸证和实际局部构造；没有执行 profile 求积、符号程序、数值秩、开发检查或科学任务。**

本稿在 [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md) 允许的同一次初选中，固定下文(16)的合法紧域和同一个有限正副本库。用原恢复的真正时间反射，可以构造一条正长度、非恒 $k$ 的实际路径，使两端 $h,k,\omega$ 值精确相同，且在**同一固定** $w_\theta,\chi_\theta$ 下，全段、全相位的完整第四 ruling 为零。

这里新增的端口信息比“scalar 返回”更强：从左端按原 canonical 零历史记账，其完整第二、第三传递准确满足
$$
T_{\rm tot}=-\frac12 A_{\rm tot}^{\,2}.
$$
这是一条完整原三槽算子身份，含原变化-profile 项，不只是在固定圆上的若干积分相等。它把后继真正 $M=0$ 半轨道的第三返回一并支付，但本文尚未制造该 $M=0$ 半轨道。

构造的中间证明以区间中心为积分锚。随后会明确改回真实左端：第二、第三规范必须一次固定为相应的端点算子值，才可保持完整字段。不能把中心的有符号累计当成从左端已经产生的原历史，更不能把每一段分别选择的规范拼成一个整词。

## 1. 同一个 R521 库与原完整状态

保 R521 的原实际几何
$$
\alpha_s=h^2T,\qquad
T_s=kN,\quad N_s=-kT-B,\quad B_s=N,\qquad
\omega_s=\frac{k_s}{2h},
\tag{1}
$$
以及一个固定右锚 $Jv(x)=\int_x^{r_*}v(y)\,dy$。记
$$
S=(h,k,\omega),\quad
\gamma=h_s,\quad \upsilon=k_s,\quad
z=x+\omega,\quad e=hz-k,\quad Q=1+e^2.
$$
第一圆、二次缺陷仍是
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{2}
$$

R521 已在**同一有限真实库**中支付：

- 每个完整基本块的三个二阶矩与全部四条第三 ruling；
- 实际互不交的有限正幅旋转／反射副本；
- 全部 $YC$、原尾和真实第三历史参与的
  $$\mathscr K=\sin^2\theta\{\mathcal F+C_hh_{ss}+C_kk_{ss}\};$$
- 在 $h>0,z>0,e>0$ 的预定合法紧域上 $C_k>0$，以及保原第二、第三历史的反馈系统。

本文不改这些 profiles、位置、幅度或右锚，不继承另一个 R455/R480 母库的规范收据。

令 $A=\Phi_{\mathsf m}$。原历史必须满足
$$
A_s=\Phi_{M_{\rm raw}(S,\gamma,\upsilon)},
\tag{3}
$$
$$
T_s(a;b,c)=-A_s\{a,A(b,c)\}+\mathcal C_s(a;b,c).
\tag{4}
$$
这里下标 $s$ 在(3)(4)表示导数。$T$ 是原 canonical 第三算子，不是 frame 的切向量；混淆可能时 frame 仍写作 $(T,N,B)$。$\mathcal C_s$ 按 R73(16)保全部局部 third 与变化-profile chain。

组合约定为
$$
(A_1\circ A_2)(a;b,c)=A_1\{a,A_2(b,c)\},
\qquad A^2=A\circ A.
\tag{5}
$$
没有把(5)改成矩阵乘法；$\Phi_{\mathsf m}$ 的二次算子复合须按原 profile 槽保留。

## 2. 真正时间反射：$M_{\rm raw}$ 偶，$\mathcal C_s$ 奇

设
$$
D_F=\operatorname{diag}(-1,1,-1).
$$
原 frame 方程的矩阵满足
$$
D_F\Omega(k)D_F=-\Omega(k).
\tag{6}
$$
以下只作原式恒等，不假设路径已经周期或 $M=0$。

把一条几何的参数反射为 $s\mapsto -s$，保 $h,k,\omega$ 的函数值，并将 $\gamma,\upsilon$ 变号，两个加速度不变。对固定 profile $a$，第一分子仅有 $T/B$ 分量，所以
$$
V_{Y_a}^{\,\rm rev}(s)=-D_FV_{Y_a}(-s),\qquad
\nabla_sV_{Y_a}^{\,\rm rev}(s)=D_F\nabla_sV_{Y_a}(-s).
\tag{7}
$$
这里 $\nabla_s=\partial_s+\Omega(k)$，所有导数固定同一个 $x$。

R73 的 second 局部场 $K_s(b,c)$ 的 normal 分量关于速度为偶，两个 tangent 分量来自线性的 $\eta_D$，所以
$$
V_K^{\,\rm rev}(s)=D_FV_K(-s),\qquad
\nabla_sV_K^{\,\rm rev}(s)=-D_F\nabla_sV_K(-s).
\tag{8}
$$
(8)含局部场的真 $s$ 导数，故加速度和原 $P_s,B_s$ 均已参与，不能只靠静态项猜奇偶。

对 $H(Y_a,Y_b)$，R56 的 $J,T_x,T_s$ 在(7)下均为偶。其 $P,B$ 为偶，真实 $s$ 导数为奇，而 $\lambda,\gamma$ 也为奇。因此 R56(5)逐项给
$$
\boxed{M_{\rm raw}(S,-\gamma,-\upsilon)
=M_{\rm raw}(S,\gamma,\upsilon).}
\tag{9}
$$
这也可直接从 R73 的完整八矩表读取：静态项与速度二次项均为偶。

对 $H(Y_a,K(b,c))$，由(7)(8)，其 $J,T_x,T_s$ 全为奇，$P,B$ 为奇，$P_s,B_s$ 为偶。代同一个 R56(5)，原密度
$\ell_s=R[H(Y_a,K(b,c))]$ 整体为奇。

还必须保 R73(15)的 chain：
$$
\Psi_s(a,b)
=-\frac{(d/h)_s}{4}a'b
-\frac{\gamma Q}{8h^3}a'b'
-\frac{e_s}{8h^3}J_e(a,b),\qquad d=h\omega-k.
$$
它对速度为奇，而 $\Phi_{M_{\rm raw}}$ 由(9)为偶。因此原
$\mathcal C_s=\ell_s-\Psi_s(a,\Phi_M(b,c))$ 给
$$
\boxed{
\mathcal C^{\,\rm rev}_s(a;b,c)
=-\mathcal C_{-s}(a;b,c).
}
\tag{10}
$$
这是完整三线性算子身份，保真锚和全部 profile 原函数。没有假定单包原函数左紧。

## 3. R521 的完整反馈系统是可逆的

先在中心 $s=0$ 采用
$$
S(0)=S_*,\qquad
\gamma(0)=\upsilon(0)=0,\qquad A(0)=T(0)=0,
\tag{11}
$$
并在这个中心记号下取 $w_\theta=\chi_\theta=0$。这只是先解一个两侧初值问题；第5节会把它改成左端真实 canonical 记账。

R521 的完整控制是 $a(s)=h_{ss}$，而
$$
b(s)=k_{ss}
=-\{\mathcal F(S,\gamma,\upsilon,A,T)+C_h(S)a(s)\}/C_k(S).
\tag{12}
$$
原 second 场为 $Z=K_s(D)-Y_{AD}$，第三 scalar 分量为
$-2T(\phi;D)$。在
$$
\mathcal I:(S,\gamma,\upsilon,A,T)
\longmapsto(S,-\gamma,-\upsilon,-A,T)
\tag{13}
$$
下，second 分子按 $D_F$ 变换，third 分子按 $-D_F$ 变换，第一分子按 $-D_F$ 变换。因此完整 fourth forcing 的 second square 和 $Y$–third 配对均保持。

等价地，由 R482 **未消第三历史的(24)**，局部第四项为偶，$\mathcal L_s(AD)$ 中线性的速度与 $A$ 同时变号，$AD$ 的能量平方不变，$T$ 项也不变。这里没有使用 R480 的 $W$ outer 零。

所以
$$
\mathcal F(\mathcal I X)=\mathcal F(X),\qquad
b(\mathcal I X,a)=b(X,a).
\tag{14}
$$
再由(9)(10)，整个实际 ODE 在时间反射下保持：
$$
S(-s)=S(s),\qquad
(\gamma,\upsilon)(-s)=-(\gamma,\upsilon)(s),
$$
$$
\boxed{A(-s)=-A(s),\qquad T(-s)=T(s).}
\tag{15}
$$
准确理由是：若 $a(-s)=a(s)$，用(13)反射一条解得到同一个(11)初值问题的解；普通 ODE 唯一性给(15)。例如(4)在反射后为
$-M(-A)-\mathcal C=MA-\mathcal C$，恰是 $T(-s)$ 的导数，号不能省略。

### 一个明确非恒 $k$ 的入口

从起点选择共同紧域，使
$$
hz>\sqrt{1+k^2}\quad\text{在全部实际及参考微包支撑上。}
\tag{16}
$$
它与 $e>0$ 可以同时满足。R521(27)(29)的完整积分给
$$
C_h=
\frac{|\mathcal G|}{3072h^6}
\sum_jw_j\sum_i\rho_i^4
\int\frac{(1+k^2-h^2z^2)F_{i,j}^4}{Q^2}<0.
\tag{17}
$$
原非零紧微包使每个有权积分的四次因子不恒零，全部权为正。故在(11)取
$$
a(0)=-\frac{\mathcal F(X_*)+C_k(S_*)}{C_h(S_*)}
\tag{18}
$$
便严格有 $k_{ss}(0)=1$。取一条在中心邻域等于(18)的固定偶光滑控制。

局部存在唯一性给一个充分小但正而有限的 $L$，使解在 $[-L,L]$ 保持同一合法紧域。并且
$$
k(s)=k_*+\frac{s^2}{2}+O(s^4),
\tag{19}
$$
所以 $k$ 真正非恒。这里不以“generic 非零”代替具体入口，也没有增加一个 profile 或几何数值实验。

由(15)，该实际段两端准确满足
$$
\boxed{h(-L)=h(L),\quad k(-L)=k(L),\quad
\omega(-L)=\omega(L).}
\tag{20}
$$
下面的重锚会保证：把 $[-L,L]$ 作为一个普通正长度物理段从左向右运行后，完整 $K=0$ 仍是同一规范下的真实结论。

## 4. 从中心累计到原左端累计的完整交叉项

置
$$
A_L=A(L),\qquad T_L=T(L).
$$
从真实左端 $s=-L$ 采用原 canonical 零历史，记其累计为
$\widehat A,\widehat T$。因(15)，原(3)直接给
$$
\boxed{\widehat A(s)=A(s)+A_L.}
\tag{21}
$$
第三层不能只平移一个常数。由原(4)，
$$
\begin{aligned}
\widehat T_s
&=-A_s\circ\widehat A+\mathcal C_s\\
&=T_s-A_s\circ A_L.
\end{aligned}
$$
从 $-L$ 的零值积分，并用 $T(-L)=T_L$，得到
$$
\boxed{
\widehat T(s)=T(s)-T_L-\widehat A(s)\circ A_L.
}
\tag{22}
$$
交叉项的次序是“当前累计在外、固定 $A_L$ 在内”。它不允许换成 $A_L\circ\widehat A$，也不能用两个矩阵乘积交换来删掉。

式(21)(22)均对原全部三槽输入成立，而非仅在 $D_\theta$ 上定义的简写。R73 的变化-profile chain 已在 $\mathcal C_s$ 中保留，因此重锚时没有另一个被遗漏的 $s$ 边界势。

## 5. 一次固定的真实第二、第三规范使整个场不变

在最终正长度段上，现在**只选择一次**
$$
\boxed{
w_\theta=-A_LD_\theta,\qquad
\chi_\theta=2T_L(\phi_\theta;D_\theta).
}
\tag{23}
$$
它们不随 $s$ 改变。先选定这条有限路径和 $L$，随后(23)固定；不在子段接头重选。

### 5.1 第二规范确实紧且满足第三 ruling

每个完整基本块的 $D_\theta$ 三矩为零。原 E8 的左二次尾表因此使
$A_LD_\theta$ 在该整块两 collar 为零，跨块仍为零。它是真紧 profile，不是仅其最高导数紧。

还需原三个交叉矩
$$
\boxed{I_j(\phi_\theta,A_LD_\theta)=0,\qquad j=0,1,2.}
\tag{24}
$$
准确来源与 R505(7)相同：对任意固定原 E8 算子，这三个完整 cubic 配对在整块共同平移后次数至多六；内侧的二次槽每块三矩零，使跨块 second tail 为零。单独出现的真二次尾与紧 outer 的原 $I_j$ 也正交，其中 $I_2$ 的 $2a'b'$ 项必须保留。R183 §5 的八个完整副本按三次权做第七差分，所以(24)逐完整块成立。后续常数正交换基、正幅及不交相加都保持它。

因此(23)中的 $w$ 满足原二阶齐次规范的全部第三 ruling 合法性，不需要新增三个未付观察。

### 5.2 第三规范的真紧性与种子

$T_L(\phi;D)$ 来自同一中心初值、同一实际几何和同一完整三阶恢复。在每个完整块外，二阶场已经双 collar 为零，第三 ruling 已在该块支付。具体地，块外 forcing 为零，左侧的 $P$ 正是该块完整第三 ruling 的尾值，也为零；$B$ 及局部导数同为零。R56(2)–(7)于是使其第三 characteristic 密度在块外为零。原中心入值为零，所以真正 scalar 历史
$T_L(\phi;D)$ 也在这些外部 collars 为零。故(23)的 $\chi$ 是真紧光滑 profile，不靠仅有 natural total 零来推紧性。

$\theta\mapsto w_\theta,\chi_\theta$ 是固定有限三角多项式，光滑且 $2\pi$ 周期。两个 seed 的 $D_0=D_\pi=0$，所以
$$
w_0=w_\pi=\chi_0=\chi_\pi=0.
$$
$\chi$ 是原允许的第三齐次场 $Y_{\chi_\theta}$，不能在以后另用作任意可变 $s$ 规范。

### 5.3 完整 second 与 third 字段逐字相同

R482 未消历史的原(15)(23)给最终字段使用的 scalar profiles
$$
\widehat q_\theta=\widehat A D_\theta+w_\theta,
$$
$$
\widehat b_\theta
=-2\widehat T(\phi_\theta;D_\theta)
+2\widehat A(\phi_\theta,w_\theta)-\chi_\theta.
\tag{25}
$$
由(21)(23)，
$$
\widehat q_\theta=A(s)D_\theta.
\tag{26}
$$
再把(22)完整代入(25)，两个有序复合项恰好消去：
$$
\begin{aligned}
\widehat b_\theta
={}&-2T(\phi;D)+2T_L(\phi;D)
+2\widehat A(\phi,A_LD)\\
&-2\widehat A(\phi,A_LD)-2T_L(\phi;D)\\
={}&\boxed{-2T(s)(\phi_\theta;D_\theta).}
\end{aligned}
\tag{27}
$$
所以从真实左端恢复的完整 $Z_\theta,W_\theta$，与中心构造中的完整字段完全相同。原局部 normal、$\eta$、chain、所有 $x$ 原函数与其两端值都没有改变；这不是只让某个 scalar period 相同。

由 R521 和(26)(27)，最后得到
$$
\boxed{\mathscr K(s,\theta)=0
\quad(-L\le s\le L,\ \theta\in\mathbb R)}
\tag{28}
$$
在一个真正从左向右、长度 $2L>0$ 的实际段上成立。证明中在中心向负 $s$ 解 ODE，不是插入一条“负成本路径”；最终历史(21)(22)均从真实左端以正常正方向积分，差异只由一次合法规范(23)准确实现。

## 6. 全算子的真实第二、第三端口

在右端，(15)(21)(22)给
$$
\boxed{
A_{\rm tot}=\widehat A(L)=2A_L,\qquad
T_{\rm tot}=\widehat T(L)=-2A_L^2.
}
\tag{29}
$$
因此
$$
\boxed{T_{\rm tot}+\frac12A_{\rm tot}^{\,2}=0}
\tag{30}
$$
是完整原三槽身份。没有取模 $W$，也没有只用某个有限 profile 测试。该等式保留实际 $M$ 不为零时必需的复合项。

若以后在这同一个真实半轨道上额外达到
$$
A_L=0,
\tag{31}
$$
则整段的 canonical 第二与第三算子都准确为零：
$A_{\rm tot}=T_{\rm tot}=0$，并且(23)的第二规范变为零。半段 $T_L$ 不必为零；它只通过同一个固定 $\chi=2T_L(\phi;D)$ 进入完整 ruling。

本文没有证明(31)可达。在当前足够短的构造，通常相反：
$$
A_L=L\,\Phi_{M_{\rm raw}(S_*,0,0)}+O(L^3).
\tag{32}
$$
原静态八矩从不整体为零：若 $k_*\ne0$，其 $p_2=-k_*h_*/2\ne0$；若 $k_*=0$，原 $t_1=-1/8$。所以对固定入口，充分短的非零 $L$ 有 $A_L\ne0$。不能以(30)冒充 $M=0$。

若后继要求原特定非零第三目标 $\tau\mathfrak H$，(31)所得的 $T_{\rm tot}=0$ 并不自动给该目标。它是一条完整第三返回的充分路径，而不是原非零 $\tau$ 规范机制的替代收据。

## 7. Frame、位置和全部 scalar germs 的准确反射

在中心固定 $F(0)=I$、$\alpha(0)=0$；一般中心 frame/位置只作同一个真实刚体变换。由 $k(-s)=k(s)$、(6)和 ODE 唯一性，
$$
\boxed{F(-s)=D_FF(s)D_F.}
\tag{33}
$$
特别 $T(-s)=-D_FT(s)$、$N(-s)=D_FN(s)$。再由 $h$ 偶和原 $\alpha_s=h^2T$，
$$
\boxed{\alpha(-s)=D_F\alpha(s).}
\tag{34}
$$

置 $G=F(L)$、$v=\alpha(L)$。两端真实数据为
$$
F(-L)=D_FGD_F,\quad F(L)=G,\qquad
\alpha(-L)=D_Fv,\quad\alpha(L)=v.
\tag{35}
$$
故 frame 的真实相对返回条件是
$$
D_FG^tD_FG=I,
\tag{36}
$$
位置返回条件是
$$
(I-D_F)v=0.
\tag{37}
$$
它们都没有由(28)(30)自动支付。比如(37)要求 $v$ 位于中心 $N$ 轴；它不是允许任意刚体平移把两个端点各自搬到同一点。

scalar 值虽满足(20)，全部端导数则为
$$
S^{(j)}(-L)=(-1)^jS^{(j)}(L).
\tag{38}
$$
因此端 germs 一般不相同；要作光滑周期识别，所有相应奇阶端导数仍须消去或由真实同规范连接支付。不能只比较 $h,k,\omega$ 的三个值。

## 8. 第四 period 没有随反射消失

本稿的原二、三阶字段具有分子奇偶
$$
V_Y(-s)=-D_FV_Y(s),\quad
V_Z(-s)=D_FV_Z(s),\quad
V_W(-s)=-D_FV_W(s).
\tag{39}
$$
第一式与 $V_Y$ 只有 $T/B$ 分量完全一致。相应协变导数为
$D_F\nabla Y,-D_F\nabla Z,D_F\nabla W$。

故完整 fourth forcing
$-(dZ)^2-\mathcal S(Y,W)$ 的 $J,T_x,T_s,P,B$ 关于中心为偶。
它们的真实 $s$ 导数为奇，而 $\lambda,\gamma$ 为奇。原 R56(5)遂给
$$
\mathcal R_{4,\theta}(-s,x)=\mathcal R_{4,\theta}(s,x).
\tag{40}
$$
整个第四 characteristic 积分因此准确是
$$
\boxed{
\int_{-L}^{L}\mathcal R_{4,\theta}(s,x)\,ds
=2\int_0^L\mathcal R_{4,\theta}(s,x)\,ds,
}
\tag{41}
$$
作为整个 $x,\theta$ 函数成立。

这条偶性是完整成本账，不是一个消去：反射段使第四剩余**加倍**，不使它为零。二阶尚未返回或 geometry germs 尚未闭合时，也不能把(41)先叫成一个已经定义的闭路正规成本；它是同一真实段的原 characteristic 累计。以后完成相应返回后，仍必须另付其整个函数零值。

所有 prototype、实际桥、倒行和 Klein 组装若使用，都要保(29)(35)(38)(41)的原值。尤其不能把来自不同 $L$ 或不同半路径的各自(23)混成一条共同规范。

## 9. 已获得的正向控制与后继真正目标

本稿给出一条明确、非恒 $k$、正长度的实际反射段。它在同一个 R521 第一圆上，用一次固定的紧 $w_\theta,\chi_\theta$ 支付完整第四 ruling；两端 scalar 值准确相同；其 canonical 第二、第三端口由(29)完全确定，纠正第三(30)作为全算子严格为零。

后继可直接研究同一实际半轨道的(31)(36)(37)、奇阶端 germs，以及(41)的全部第四累计，而不用再把半段第三 $T_L$ 独立要求为零。该缩减提供一个明确的实际边值问题，尚不证明它已有解。

固定完一条半路径后，(23)在整词中只可使用一次。若要获得保同一规范的路径族，必须在同一真实控制族中同时保持相应 $A_L$、$T_L(\phi;D)$ 及其它所需端数据，不能沿族逐条重选规范。本文没有用一个未付满秩来宣称这些端目标可以任意指定。

旧 R70 的无 ruling 桥、R517 另一库的 automatic $M=0$、以及 R459/R518 的不同母成本截面，都不能代替本稿尚欠的真实半轨道端点。主课题的完整周期、有限等距族、嵌入、厚度和宏观幅度均未由本稿解决。

### 原来源范围

- R56(2)–(8)：同锚分子、完整 ruling、characteristic 累计及两 collar；
- R73(12)(15)–(17)：全部八矩、变化-profile chain 和第三有序复合；
- R183 §5、R505(7)：完整八副本的第三四通道与 E8 第二规范三矩合法性；
- R482 未消历史的(23)(24)：真正 $q,b$ 与完整第四字段；
- R521：本稿同一有限正副本库、第三历史状态、$C_k>0$ 和实际加速度反馈。

全部反射、重锚和端口式均由上述原式直接证明。没有新增研究执行，也没有把局部实际段称为主问题的全闭词。
