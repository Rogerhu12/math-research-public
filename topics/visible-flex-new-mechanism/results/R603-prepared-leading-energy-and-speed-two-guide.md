# R603 Prepared 中心的真实最高能量层与 v=2 九参数输入

日期：2026-11-26。**原式纸证；没有科学执行。**
本稿接 R590、R598、R601。第一项结论具有明确的缩微族假设，
不声称固定 \(\varepsilon=1/12000\) 无根。
第二项给可直接执行的新有限 guide 参数化；其完整矩、历史、ruling 和宏观几何仍须实算。

## 1. 同一形状的实际母族及严格量词

固定 R598 的十八个真实中心、三旋转、正权与窗口 \([4,6]\)。
令 \(\varepsilon\downarrow0\)，只将每个完整块内原三十二微包的位置、
支撑宽度及 collar 按 \(\varepsilon\) 缩放：
微包中心偏移仍是 \((15j+3m-57)\varepsilon\)，
原 bump 的共同幅仍为 \(\varepsilon^{7/4}/256\)。
每个实际副本另乘 R598 固定 \((2w)^{1/4}\)。
所有下阶矩、原尾重置在完整块外为零、三旋转与十次正节点身份继续准确。
这是从起点指定的一族实际母；不同 \(\varepsilon\) 的历史或规范不拼接。

考虑一族**原完整 ruling 的真实解**，在共同的正物理时间区间
\([0,\ell]\)、\(\ell>0\) 上满足以下条件：

1. \((h_\varepsilon,k_\varepsilon)\) 在 \(C^2([0,\ell])\) 收敛到 \((h,k)\)；
   全部几何保持同一严格合法紧盒。特别高度有统一正下界，
   \(y\pm\eta_\varepsilon\)、\(e_\pm\) 和原两加速度行的分母保严格合法。
   可以把“有统一 \(C^3\) 界并取 \(C^2\) 收敛子列”作为足够来源，
   但只有物理盒或 \(C^2\) 有界本身不能代替本条件。
2. \(\eta_{\varepsilon,s}=k_{\varepsilon,s}/(2h_\varepsilon)\)、
   \(A_{\varepsilon,s}=M_\varepsilon\)，所有实际中心为 R601 prepared：
   \[
   (h,k,\eta,\gamma,\upsilon)_\varepsilon(0)
   =(H_\varepsilon,0,0,0,v_\varepsilon),
   \]
   \[
   A_{\varepsilon,\rm odd}(0)
   =\left(\frac{v_\varepsilon}{12H_\varepsilon},0,
          \frac{v_\varepsilon}{16H_\varepsilon^3},
          \frac{v_\varepsilon}{24H_\varepsilon}\right),
   \qquad A_{\varepsilon,\rm even}(0)=0.
   \]
   且 \(a_\varepsilon(0)=H_\varepsilon\)；
   两原 ruling 同时给 \(b_\varepsilon(0)=0\)。
   设 \(H_\varepsilon\to H>0,\ v_\varepsilon\to v\ne0\)。
3. 两侧都是 R590 的真实 C² 历史，且
   \(\rho_{\varepsilon,+}(0)=\rho_{\varepsilon,-}(0)=0\)。
   固定规范在每条路径上始终为一个常向量，
   并有有限极限
   \[
   \varepsilon^2\widehat\nu_\varepsilon\longrightarrow \nu_* .
   \tag{1}
   \]
   它可以随母族改变，不能随 \(s\) 改变。
   本文不证明任意有限解的规范自动满足这个增长界。

结论是
\[
\boxed{|v|=2.}
\tag{2}
\]
这是紧致缩微族的中心必要条件。
它不排除固定 \(\varepsilon\) 上 \(|v|\ne2\) 的真解，
也不排除规范更快增长、导数失去紧致性、中心未 prepared、
中心加速度不取 \(H\)，或不同形状母的路线。

## 2. C² 部分为什么在这个族中一致有界

这里不能把“导数阶降到 C²”直接当作尺度结论。
写固定 bump 为 \(\beta\in C_c^\infty(-1,1)\)，
一微包的原空间 jets 是
\[
u_\varepsilon=\frac{\varepsilon^{7/4}}{256}\beta(\xi),\quad
p_\varepsilon=\frac{\varepsilon^{3/4}}{256}\beta'(\xi),\quad
r_\varepsilon=\frac{\varepsilon^{-1/4}}{256}\beta''(\xi),\quad
\mathsf t_\varepsilon=\frac{\varepsilon^{-5/4}}{256}\beta'''(\xi).
\tag{3}
\]
三十二微包的方向和有限幅系数全部固定。

R581 的完整局部 \(\mathscr R\) 及 R590(26) 的完整六个更新，
在原三旋转转置后是有限个齐次四次多项式读出，
只含 \(u,p,r\) 及原 \(J_0,J_1,J_2\)。
没有 profile 分母；几何分母在固定合法盒内一致有界。
几何系数对 \(A\) 多项式，对实际 \(a,b\) 至多仿射。

在一个完整块内，
\[
|J_j|\le C\varepsilon^{1/2},\qquad j=0,1,2.
\tag{4}
\]
因为主项是 \(r_\varepsilon^2\) 在 \(O(\varepsilon)\) 长度上的积分；
\(J_2\) 的 \(2p_\varepsilon^2\) 项更低。
整块外的这三个真尾都准确为零，不能把完整块之间的固定间隙算成
一个未清的长尾。

一个不含尾的四次 C² 单项式，
最坏是 \(r^4=O(\varepsilon^{-1})\)，
而完整块长度 \(O(\varepsilon)\)，故其积分 \(O(1)\)。
一个 \(J_j\) 占两个 profile 槽；
若再乘两个局部 jets，最坏是 \(J_jr^2=O(1)\)，积分 \(O(\varepsilon)\)。
两个尾则更低。固定有限块数不改变这些界。
这覆盖 R590 先取 \(r\) 原函数再用真实 \(D_0\) 后的全部低阶项；
四次齐次性和最多 C² 的性质由已登记 R586/R590 原式保证。

由条件1，\(S,v,a,b\) 一致有界。
由真 \(A_s=M\)、prepared 中心及共同有限时间，\(A\) 也一致有界。
故存在不依赖 \(\varepsilon\) 的 \(C\)，使
\[
|\mathscr R_\varepsilon|+
|\mathcal H^{(2)}_{\varepsilon,+}|+
|\mathcal H^{(2)}_{\varepsilon,-}|\le C.
\tag{5}
\]
这里 \(\mathscr R\) 包含实际 \(C_ha+C_kb\)。
用真实零入值与原负侧整体反号，
\[
|\rho_{\varepsilon,\pm}(s)|\le C\ell .
\tag{6}
\]
因此在完整 ruling 乘 \(\varepsilon^2\) 后，这些项一致趋零。
若另给 \(O(\varepsilon^{-2})\) 的第三 incoming，这一步不成立；
本文明确没有使用那种不同输入。

## 3. 正平方的首层确是六个正节点上的四次多项式范数

记 R598 的六参考中心为 \(c_1,\ldots,c_6\)，正权为 \(w_i>0\)。
真实十八块的三旋转总和在完整原式中准确等于六参考块乘6，
不是把母换成重叠的虚拟副本。

R601 在原八矩坐标中给
\[
V=H_A+2F_0=V_0(y)u+V_1(y)p+V_2(y)r,
\]
\[
V_2(y)=-2C_A(y)-\frac{Q(y)e_s(y)}{4h^3},
\]
\[
C_A=r_0+(r_1+s_0)y+\frac32s_1y^2+
(t_1-p_1/4)y^3-\frac14p_2y^4 .
\tag{7}
\]
因此 \(\deg V_2\le4\)，并且准确有
\[
[y^4]V_2=p_2/2.
\tag{8}
\]
\(Qe_s\) 只有三次，不能改掉这个最高系数。

令 \(D_i\) 为参考完整块中第 \(i\) 个微包的固定原差系数，
包括原宏包幅 \(a_j\)，不包括 (3)的共同 bump 幅。
定义正数
\[
c_*=\frac{6}{64\cdot256^4}
 \left(\sum_{i=1}^{32}D_i^2\right)
 \int_{-1}^{1}(\beta'''(\xi))^2(\beta''(\xi))^2\,d\xi>0 .
\tag{9}
\]
固定非零紧 bump 的这个积分严格正：
否则在每个 \(\beta''\ne0\) 的开连通分支上 \(\beta'''=0\)，
使 \(\beta''\) 为非零常数，不能连续连接到支撑外的零值。
并且 R521 方向给
\(\sum_iD_i^2=20\sum_{j=0}^7\binom7j^{4/3}>0\)。

于是 R590 的完整正平方有一致展开
\[
\varepsilon^2\,w(S)\cdot\mathcal E_\varepsilon(S,v,A)
=\mathcal F(S,v,A)+O(\varepsilon),
\]
\[
\boxed{\mathcal F(S,v,A)=
 \frac{c_*}{h}\sum_{i=1}^6w_i Q(c_i)V_2(c_i)^2\ge0.}
\tag{10}
\]
证明：把 (3)代入 R590(32)。
\(\mathsf t^2r^2\) 的积分恰为 \(\varepsilon^{-2}\)；
与 \(p\) 的交叉多一 \(\varepsilon\)，
与 \(u\) 的交叉多两 \(\varepsilon\)，其余更低。
各微包位置 \(c_i+\varepsilon t_j+\varepsilon\xi\) 到 \(c_i\) 的差为
\(O(\varepsilon)\)。在条件1的紧状态集上，多项式系数及其 \(y\) 导数一致有界，
故误差一致为 \(O(\varepsilon)\)。
式(10)只需要 \(C^0\) 的参数一致性，不声称误差的时间二阶导数也一致小。

## 4. 先取完整方程的极限，再在极限轨道求中心 jet

R590 的正侧原式是
\[
0=\mathscr R_\varepsilon
 -4w_\varepsilon\cdot\rho_{\varepsilon,+}
 -4w_\varepsilon\cdot\mathcal E_\varepsilon
 -2w_\varepsilon\cdot\widehat\nu_\varepsilon .
\tag{11}
\]
由(1)(5)(6)(10)，先在整个固定时间区间取 \(C^0\) 极限，得准确恒等式
\[
\boxed{\mathcal F(s)=w(S(s))\cdot P,\qquad P=-\nu_*/2.}
\tag{12}
\]
\(P\) 是一条固定向量。没有把规范沿时间配权。
负侧原式仍同时成立；下述必要条件只需其正侧，中心的 \(b=0\) 已由两原式付清。

现在完全在极限轨道上计算。
条件1与真 \(\eta_s=k_s/(2h)\)、\(A_s=M\)
给极限的 \(\eta\in C^2,A\in C^1\)，并保留所有原方程与 prepared 初值。
特别 \(V_2(s,y)\) 至少为 \(C^1\) 的时间函数。
R601 原中心身份在该极限轨道直接给
\[
V_2(0,y)=0,\qquad
(V_2)_s(0,y)=\frac{H-a}{4H^3}y(1+H^2y^2)=0.
\tag{13}
\]
所以对每个固定参考节点，
\(V_2(s,c_i)=o(s)\)，从而
\[
\mathcal F(0)=0,\qquad \mathcal F(s)=o(s^2).
\tag{14}
\]

**此处没有交换 \(\varepsilon\) 极限与时间二阶导数。**
先用一致 \(C^0\) 展开取得(12)，再用独立保证的极限 \(C^2\) 几何和真 \(M\)
得到(13)(14)。既没有把 \(O(\varepsilon)\) 除以 \(s^2\)，
也没有假设有限 \(\varepsilon\) 的巨大能量具有统一二阶导数界。

记 \(d=h\eta-k\)。原运动学在中心给
\[
d(0)=0,\quad d_s(0)=-v/2,\quad h_s(0)=0,\quad h_{ss}(0)=H.
\]
因此
\[
w(0)=\left(\frac1{4H},0,\frac H4\right),\qquad
w_s(0)=(0,-v/4,0).
\]
由(12)(14)及 \(v\ne0\)，
\[
P_0=-H^2P_2,\qquad P_1=0,
\]
故
\[
\mathcal F(s)=\frac{P_2}{4h(s)}
 \{h(s)^2-H^2(1+d(s)^2)\}.
\tag{15}
\]

## 5. \(P_2\ne0\) 的真实局部矛盾，以及中心速度结论

若 \(P_2=0\)，则 \(P=0\)，(12)使 \(\mathcal F(s)=0\)
在整个共同正时间区间成立。
式(10)的每个权、\(Q(c_i)\)、\(h^{-1}\) 都严格正，
故 \(V_2(s,c_i)=0\)，对六个不同节点、每个 \(s\) 同时成立。
四次以下的多项式因而恒为零；由(8)，\(p_2(s)=0\)。
原 \(p_{2,s}=-kh/2\) 与 \(h>0\) 随即给 \(k(s)=0\)，
这与中心 \(k_s(0)=v\ne0\) 矛盾。
这只用任意共同小正时间区间，不借未知末端八矩返回。

因此 \(P_2\ne0\)。令
\(m=h^2-H^2(1+d^2)\)。由(15)与(14)，\(m(s)=o(s^2)\)。
而真实 \(C^2\) 中心运动学给
\[
m(0)=m_s(0)=0,\qquad
m_{ss}(0)=2H^2-\frac{H^2v^2}{2}.
\tag{16}
\]
于是 \(m_{ss}(0)=0\)，得到 \(v^2=4\)，即(2)。

条件(1)和几何的 \(C^2\) 紧致性是结论的一部分。
本稿没有为一个固定有限母排除其它 \(v\)，
没有证明任意实际根都产生这种缩微族，
也没有在原 R573 已知长尺度路线外另宣任何 reach 不可能性。
它指出的是：若准备用 prepared 与 \(a=H\) 消掉最高能量的中心一阶生成，
则 \(v=\pm2\) 是与固定规范最高层相容的更强有限初猜选择。

## 6. 同时精确给 \(h_{ss}(0)=H,\ k_s(0)=v_*\) 与 \(\int hk=0\)

固定 \(v_*=2\)（也可独立选择 \(-2\)），令 \(s=Lx\)、\(\theta=\pi x/2\)。
高度仍采用 R601 的精确消元：
\[
h(x)=1.9+\tanh\!\left(\sum_{j=0}^4\alpha_j\cos j\pi x\right),
\]
\[
B_*=-\frac{HL^2}{\pi^2[1-(H-1.9)^2]},\quad
\alpha_4=\frac{B_*-\alpha_1-4\alpha_2-9\alpha_3}{16},
\]
\[
\alpha_0=\operatorname{atanh}(H-1.9)-\sum_{j=1}^4\alpha_j.
\tag{17}
\]
因此 \(.9<H<2.9\) 给 \(h(0)=H,\ h_{ss}(0)=H\)，且全域 \(.9<h<2.9\)。

定义
\[
T_*=\frac{2Lv_*}{1.95\pi},\qquad
b_5(c)=\frac{T_*-c-3b_1-5b_2-7b_3-9b_4}{11},
\tag{18}
\]
\[
K_c(x)=c\sin\theta+\sum_{j=1}^5 b_j(c)\sin((2j+1)\theta),
\qquad k(x)=1.95\tanh K_c(x),
\tag{19}
\]
其中 \(b_1,\ldots,b_4\) 自由，只有 \(b_5\) 随 \(c\) 由(18)确定。
原点 \(K_c=0\)，且加权正弦斜率和准确为 \(T_*\)，所以
\[
k(0)=0,\qquad k_s(0)=v_*,\qquad k_{ss}(0)=0.
\tag{20}
\]
所有奇半波在 \(x=1\) 的一阶导数都为零，
故原末 \(k_s(1)=0\) 仍保留，原末 \(h_s(1)=0\) 亦不变。

### 6.1 这里的 \(c\) 仍有准确唯一单调定义

由(18)(19)，
\[
\partial_c K_c(x)=\psi(\theta)
=\sin\theta-\frac1{11}\sin11\theta>0
\quad(0<x\le1).
\tag{21}
\]
严格性可以直接证明：
\(\sin(11\theta)/\sin\theta\) 是十一个单位复数的几何和；
在 \(0<\theta\le\pi/2\) 时它们不全同向，
故其绝对值严格小于11，且 \(\sin\theta>0\)。

于是
\[
\Phi(c)=\int_0^1h(x)k(x;c)\,dx,\qquad
\Phi'(c)=1.95\int_0^1h(x)\operatorname{sech}^2K_c(x)\psi(\theta)\,dx>0.
\]
又由有界收敛，
\[
\lim_{c\to\pm\infty}\Phi(c)
=\pm1.95\int_0^1h(x)\,dx.
\]
因此存在唯一有限的 \(c\) 使
\[
\boxed{\int_0^1hk\,dx=0.}
\tag{22}
\]
这同时支付 prepared 中心 \(p_2(0)=0\) 下的连续末 \(p_2=0\)。
固定正 Gauss 规则也有同样的离散单调性，
但其数值根不被冒称连续精确根；实际末 \(p_2\) 误差仍需报告。

## 7. 真正新的九参数与仍然未付的账

新自由向量为
\[
(H,\alpha_1,\alpha_2,\alpha_3,b_1,b_2,b_3,b_4,L)
\in\mathbb R^9.
\tag{23}
\]
它同时按(17)–(22)给三个准确连续条件。
从已经付费的十一参数 guide 只取其实际
\(H,\alpha_{1,2,3},b_{1,\ldots,4},L\)，
重新定义 \(b_5,c\)，不是再跑旧十一个自由量的优化。
完整 \(\eta\)、prepared \(A\)、七个剩余末矩、两侧 rho、固定规范、
原 frame/位置和几何预算都必须按这条新路径共同重算。

原两条 ruling 与全部正平方不改变。
\(\zeta_0\) 仍按 R601 在同一母的真实中心支付 \(a=H,b=0\)。
进入完整质量 BVP 后，可以像前包一样释放原十个真实中心参数；
本节只是有完整原式理由的更强初猜，不强制最终根满足整个缩微族假设。

这九参数计数不授七矩 rank 或根。
\(|k|<1.95\) 与高度范围准确，但 \(\eta\) 和整个速度盒仍须另核；
单调 \(c\) 的存在不保证其速度峰值或宏观直径预算自动合格。
特别本稿没有闭合 pose、第四 period、同十三规范或主 reach / holding 条件。

### 原依据

R581/R584：完整局部 \(\mathscr R\) 的 C² 表达和真正十九态；
R586：原尾齐次四次与同点槽；
R590(22)–(33)：完整 C² 更新、同中心的规范与真实非负势；
R598：同一十八块正库及六参考节点的准确表示；
R601：prepared 中心的真实 \(V_s\)、固定 \(\zeta_0\) 支付及高度消元。
