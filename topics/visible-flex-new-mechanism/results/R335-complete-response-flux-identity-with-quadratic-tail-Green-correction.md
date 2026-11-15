# R335：完整响应总通量的二次左尾 Green 修正与准确 pure 归一化

日期：2026-11-15。**完整纸面证明；未执行新的 profile 求值、求积或符号程序、数值消元或 Actions 科学运行。**

本稿处理一个实际尚未支付的 period 读出。对紧 profile $u$，记
$$
\Omega_u(V)=\int_\ell^{r_*}u'''(x)V(u^2,0)(x)\,dx.
\tag{1}
$$
它不能仅由既有 universal self 的 $x^2$ 系数定义替代。本稿给出 $\Omega_u$ 在全部真实响应上的准确公式，特别保留二、三阶 history 的左尾。

结论有三点。

1. 原正式 pure 投影满足 $\mathcal B_E(\tau)(0,u)=16\,\pi\mathcal B_E(\tau)(u)$。因此此前未发表推导中的 $1/5$ 只可能对应 raw pure 输出，不能直接放在正式 $\pi$ 前。
2. 即使改成 $16/5$，对一般实紧 $u$，无尾公式仍然错误。准确差是第 5 节的显式 Green 项；第 7 节给出一个原算子反例。
3. 对全部第三对角核响应，$\Omega_u$ 确实为零。若一个允许为复数值的紧输入 $u$ **自身三条双线性矩全零**，Green 项也全消，此时且仅在本文所证范围内得到全部响应的无尾 $16/5$ 公式。非零实紧微包不满足这一附加假设。

本稿没有证明 $\Omega_u$ 在一般实输入的 $\mathcal R\cap\ker\pi$ 上恒零，也没有把它视为已知的 $U/\mathcal R$ 不变量。更没有从 whole universal self 已可控制推出该 period 读出已可控制。

来源是 [R73 的原八算子](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R247 的完整响应及正式 pure 投影](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md)、[R254 的完整第三空间分解](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md)、[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R261 的完整十八维第三核 Green 表示](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)。全部右锚均是原共同右 collar。

## 1. 完整响应与两个不同的 pure 规范

令
$$
J(F)(x)=\int_x^{r_*}F(t)\,dt.
$$
所有原 primitive 都保持这个方向及锚。先取任意 $u\in C_c^\infty((\ell,r_*))$；复输入时所有配对仍为双线性，不作复共轭。

对 $F=f\odot f$、$D=F-\phi\odot\phi$，原完整响应为
$$
\mathcal B_E(\tau)(F,\phi)
=2\tau(\Phi_E D;D)
-4\tau(\phi;\phi,\Phi_E D)
+4\Phi_E(\phi,\tau(\phi;D)).
\tag{2}
$$
内两槽对称，按对称平方线性延拓。设
$$
q_E=\Phi_E(u,u),\qquad T_\tau=\tau(u;u,u).
$$
在 $\phi=0,F=u^2$，
$$
\mathcal B_E(\tau)(u^2,0)=2\tau(q_E;u,u).
\tag{3}
$$
在 $F=0,\phi=u$，
$$
\mathcal B_E(\tau)(0,u)
=2\left\{D T_\tau(u)[q_E]-2\Phi_E(u,T_\tau)\right\}.
\tag{4}
$$
另一方面，R247(5)、R254(16) 的正式投影是
$$
\boxed{\pi\mathcal B_E(\tau)(u)
=\frac18\left\{D T_\tau(u)[q_E]-2\Phi_E(u,T_\tau)\right\}.}
\tag{5}
$$
故 raw 输出 (4) 正好是 (5) 的十六倍。后文一直使用正式 $\pi$；没有更改其定义。

令
$$
\mathcal L_u(V)=\int_\ell^{r_*}u'''\,\pi V(u).
\tag{6}
$$
目标是准确计算 $5\Omega_u(V)-16\mathcal L_u(V)$，而不是预先把它设为零。

## 2. 原八算子的完整三阶伴随

### 2.1. 含全部右尾的原式

R73 的八坐标为
$$
E=(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1),\qquad
t_0=p_0/4+s_1/2.
$$
对任意光滑输入 $a,w$，原式为
$$
\begin{aligned}
\Phi_E(a,w)={}&A_0aw+\frac{A_1}{2}(aw'+a'w)+A_2a'w'\\
&+B_0J(a''w'')+B_1J(xa''w'')\\
&+B_2J(x^2a''w''+2a'w'),
\end{aligned}
\tag{7}
$$
其中
$$
\begin{aligned}
A_1&=p_0+p_1x+p_2x^2,& A_0&=-A_1'/2,\\
B_0&=r_0+r_1x-p_0x^2/4,&
B_1&=s_0+s_1x-p_1x^2/4,\\
B_2&=t_0+t_1x-p_2x^2/4.
\end{aligned}
$$
定义
$$
\mathcal C=B_0+xB_1+x^2B_2,\qquad W=B_1+2xB_2.
$$
则
$$
A_2=\mathcal C'-W
=r_1+(s_1-p_0/2)x+(t_1-p_1/2)x^2-p_2x^3/2.
\tag{8}
$$

对原 (7) 求三阶导，所有 primitive 都消失，准确得到
$$
\boxed{
D_x^3\Phi_E(a,w)=
D_x^2(g_E[a]D_x^2w)+D_x(h_E[a]D_xw)+c_E[a]w,
}
\tag{9}
$$
其中
$$
\begin{aligned}
g_E[a]&=\frac{A_1}{2}a+A_2a'-\mathcal C a'',\\
h_E[a]&=A_2a'''+2B_2a''-2B_2'a'+2B_2''a,\\
c_E[a]&=\frac{A_1}{2}a^{(4)}+A_1'a'''.
\end{aligned}
\tag{10}
$$

这里是全部八算子的统一公式，不是假定 $a$ 紧后只匹配某些项。一个直接核对方式是用
$$
D^3(BJ F)=-3B''F-3B'F'-BF'',\qquad \deg B\le2.
$$
把 (7) 的三个密度分别代入后，$w^{(4)},w''',w'',w',w$ 的系数依次为
$$
g_E[a],\quad2g_E[a]',\quad g_E[a]''+h_E[a],
\quad h_E[a]',\quad c_E[a].
$$
式 (8) 及 $t_0=p_0/4+s_1/2$ 正是上述重组所用的全部系数恒等。

例如，对
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
$$
(9) 分别成为
$$
\begin{aligned}
D^3P(a,w)&=-D^2(a''D^2w),\\
D^3R(a,w)&=D^2((a'-xa'')D^2w)+D(a'''Dw),\\
D^3S(a,w)&=-D^2(xa''D^2w).
\end{aligned}
\tag{11}
$$
这也核定了正右尾 $J$ 带来的负号。

### 2.2. 什么时候可以真正交换伴随

记 (9) 的算子为 $\mathscr A_{E,a}$。它形式自伴，且其准确 Green 项为
$$
\begin{aligned}
\mathfrak W_{E,a}(v,w)={}&
v(gw'')'-v'gw''-w(gv'')'+w'gv''\\
&+h(vw'-wv'),
\end{aligned}
$$
$$
D\mathfrak W_{E,a}(v,w)
=v\mathscr A_{E,a}w-w\mathscr A_{E,a}v.
\tag{12}
$$
本稿只在以下两种已支付的情形交换积分：

- $v$ 或 $w$ 是紧输入 $u$，因其全部端点 jets 为零，(12) 两端为零；
- 系数来自 $a=u$，此时 $g,h,c$ 都紧，即使两个被配对的函数各有二次左尾，(12) 两端仍为零。

随后若再把 $D^3$ 从一个有尾函数移到另一个有尾函数，必须另保下一节的三阶 Green 项。(12) 为零并不允许跳过这个第二步。

## 3. 二次尾的真实 Green 双线性型

对右 collar 为零、左 collar 为二次多项式的两个函数 $a,b$，记
$$
[a,b]_3=\int_\ell^{r_*}a'''b,
$$
并定义左尾双线性型
$$
\boxed{\mathcal G(a,b)=
\bigl(a''b-a'b'+ab''\bigr)(\ell).}
\tag{13}
$$
它对称，且只依赖两个真实左尾。若
$$
a_{\rm left}=a_2x^2+a_1x+a_0,\qquad
b_{\rm left}=b_2x^2+b_1x+b_0,
$$
则
$$
\mathcal G(a,b)=2a_2b_0-a_1b_1+2a_0b_2.
\tag{14}
$$
该值不依赖左 collar 中选取哪个 $\ell$。完整三次分部积分给
$$
\boxed{[a,b]_3+[b,a]_3=-\mathcal G(a,b).}
\tag{15}
$$
因此这个原积分配对在有尾函数上一般**不是**反对称的。若至少一个函数紧，$\mathcal G=0$，才可使用反对称式。

### 3.1. 所有尾值均由真实三个积分给出

对于一个紧输入 $u$ 及任意右零且光滑的 $v$，定义
$$
m(u,v)=
\left(
\int u''v'',\
\int xu''v'',\
\int(x^2u''v''+2u'v')
\right).
\tag{16}
$$
令 $p_E(m)$ 表示 $\Phi_E(u,v)$ 的左尾。由 (7)，准确为
$$
p_E(m)=B_0m_0+B_1m_1+B_2m_2.
\tag{17}
$$
八个单位方向的表是
$$
\begin{array}{c|c}
E&p_E(m)\\ \hline
p_0&(m_2-x^2m_0)/4\\
p_1&-x^2m_1/4\\
p_2&-x^2m_2/4\\
r_0&m_0\\
r_1&xm_0\\
s_0&m_1\\
s_1&xm_1+m_2/2\\
t_1&xm_2
\end{array}
\tag{18}
$$
这里 $m_2$ 始终包含 $2u'v'$，没有用仅 $\int x^2u''v''$ 的替代矩。

设
$$
\mu=m(u,u),\qquad \nu_E=m(u,q_E).
\tag{19}
$$
于是 $q_E$ 左尾是 $p_E(\mu)$，$\Phi_A(u,q_E)$ 左尾是 $p_A(\nu_E)$。这些量不是可独立指定的参数，而是原同一个 $u$ 的积分。

## 4. 一个完整交换子的收缩

取
$$
\tau=C(A,B),\qquad
C(A,B)(a;b,c)
=\Phi_A(a,\Phi_B(b,c))-\Phi_B(a,\Phi_A(b,c)).
$$
写
$$
q_A=\Phi_A(u,u),\quad q_B=\Phi_B(u,u),\quad
T=\Phi_A(u,q_B)-\Phi_B(u,q_A),
$$
$$
w=q_E,\qquad b_A=\Phi_A(u,w),\quad b_B=\Phi_B(u,w).
\tag{20}
$$
$q_A,q_B,w,T,b_A,b_B$ 都右零且有真实二次左尾，因为每个外层计算至少含一个紧输入 $u$。这句话不把一般 $\tau(w;u,u)$ 本身的左尾预设为二次。

令
$$
S=-\int wT'''.
\tag{21}
$$
由 (9)、(12)，
$$
\begin{aligned}
\int u'''\tau(w;u,u)
&=-\int u\{\mathscr A_{A,q_B}-\mathscr A_{B,q_A}\}w\\
&=-\int wT'''=S.
\end{aligned}
\tag{22}
$$
这里交换伴随时有紧参数 $u$，端项确实为零。结合 (3)，
$$
\Omega_u(\mathcal B_E\tau)=2S.
\tag{23}
$$

记
$$
D_{\rm tail}=\mathcal G(q_A,b_B)-\mathcal G(q_B,b_A).
\tag{24}
$$
对 $T$ 作 profile 变分，
$$
D T(u)[w]
=\tau(w;u,u)+2\Phi_A(u,b_B)-2\Phi_B(u,b_A).
\tag{25}
$$
再次使用紧系数的 (12)，先得到
$$
\int u'''DT(u)[w]
=S+2\left\{-\int b_Bq_A'''+\int b_Aq_B'''\right\}.
$$
另一方面，同一伴随交换给
$$
S=-\int q_Bb_A'''+\int q_Ab_B'''.
$$
这两个表达式之间必须用 (15)，而不能直接将三阶配对反号。准确关系是
$$
-\int b_Bq_A'''+\int b_Aq_B'''=S+D_{\rm tail}.
$$
所以
$$
\boxed{\int u'''DT(u)[w]=3S+2D_{\rm tail}.}
\tag{26}
$$

第三项的准确收缩是
$$
\int u'''\Phi_E(u,T)=-\int Tw'''=-[w,T]_3.
\tag{27}
$$
而 (15)、(21) 给
$$
[w,T]_3=S-\mathcal G(w,T).
\tag{28}
$$
原无尾推导遗漏的，正是 (26) 和 (28) 中的 Green 项。

## 5. 全部真实响应的准确公式

将 (26)–(28) 代入正式 (5)，得到
$$
8\mathcal L_u(\mathcal B_E\tau)
=5S+2D_{\rm tail}-2\mathcal G(w,T).
$$
因此
$$
\boxed{
5\Omega_u(\mathcal B_E C(A,B))
-16\mathcal L_u(\mathcal B_E C(A,B))
=4\,\mathfrak C_{E;A,B}(u),
}
\tag{29}
$$
其中
$$
\boxed{
\mathfrak C_{E;A,B}
=\mathcal G(q_E,T)
-\mathcal G(q_A,b_B)+\mathcal G(q_B,b_A).
}
\tag{30}
$$
这是完整原响应的恒等式；没有只取局部项、只取对角第三类或丢去 left primitive。

用 (18)–(20)，可完全从真实矩读出右端：
$$
\begin{aligned}
\mathfrak C_{E;A,B}={}&
\mathcal G\!\left(
p_E(\mu),\,p_A(\nu_B)-p_B(\nu_A)\right)\\
&-\mathcal G\!\left(p_A(\mu),p_B(\nu_E)\right)
+\mathcal G\!\left(p_B(\mu),p_A(\nu_E)\right).
\end{aligned}
\tag{31}
$$
$\mathcal G$ 在 (31) 作用于两个二次多项式，按 (14) 解释。$\mu$ 是二次量、各 $\nu$ 是三次量，故 (31) 是真实五次尾量。它不是新的自由形状常数。

### 5.1. 第三对角核方向

若 $\chi\in Z=\ker\Delta$，R258/R261 给
$$
D^3K_{\chi,u}=\mathscr A_{\chi,u},\qquad
\mathscr A_{\chi,u}^*=\mathscr A_{\chi,u},\qquad
K_{\chi,u}(u)=0,
$$
其中 $K_{\chi,u}(v)=\chi(v;u,u)$。于是
$$
\begin{aligned}
\Omega_u(\mathcal B_E\chi)
&=2\int u'''K_{\chi,u}(q_E)\\
&=-2\int u\mathscr A_{\chi,u}q_E
=-2\int q_E\mathscr A_{\chi,u}u=0.
\end{aligned}
\tag{32}
$$
端项由紧 $u$ 和原局部 Green 式支付。正式 $\pi\mathcal B_E\chi=0$ 也由 (5) 成立。因此 (32) 对全部十八维 $Z$ 成立，而不只八个新增 $\chi$。

R254 已付
$$
W=W_{71}\oplus
\operatorname{span}\{\chi_{30},\chi_{32},\chi_{34},\chi_{37},
\chi_{40},\chi_{100},\chi_{104},\chi_{109}\}.
$$
所以 (29) 加 (32) 覆盖原全部响应空间 $\mathcal R$。将 (30) 在一个完整响应呈示中线性相加，所得 $\mathfrak C_u(V)$ 不依赖呈示：若该呈示的原响应为零，(29) 的左端也为零，故尾和为零。这只是已证原恒等对关系的后果，不增添任何响应独立性假设。

最终可写为
$$
\boxed{
\Omega_u(V)=\frac{16}{5}\mathcal L_u(V)
+\frac45\mathfrak C_u(V),\qquad V\in\mathcal R.
}
\tag{33}
$$

## 6. 无尾结论的两个准确范围

第一，(32) 已证明
$$
\Omega_u\bigl(\mathcal B(E,Z)\bigr)=0.
\tag{34}
$$
不能将 $\mathcal B(E,Z)$ 直接替换成 $\mathcal R\cap\ker\pi$；R247/R254 已明确两者没有这种已付相等关系。

第二，若某个紧输入 $u$ 自身满足
$$
\mu=m(u,u)=0,
\tag{35}
$$
则全部 $p_E(\mu)=0$，所以 (31) 的三项全零。此时
$$
\boxed{
\Omega_u(V)=\frac{16}{5}\int u'''\pi V(u),\qquad V\in\mathcal R.
}
\tag{36}
$$
特别对该固定输入，
$$
\Omega_u(\mathcal R\cap\ker\pi)=0.
\tag{37}
$$

式 (35) 对非零实紧 $u$ 不可能，因为其首分量为 $\int(u'')^2>0$。对复紧 $u=f+ig$，三条双线性矩可以为零，且以上证明不使用正定性，故 (36)–(37) 同样有效。它给一个准确限定的复输入响应读出；本文没有进一步把该读出等同于原固定实圆的全部 mixed period 障碍。

若改用 raw pure 输出 $P_{\rm raw}(V)(u)=V(0,u)$，在 (35) 下可以等价写为
$$
\Omega_u(V)=\frac15\int u'''P_{\rm raw}(V)(u).
$$
这个 $1/5$ 既不能挪到正式 $\pi$ 前，也不能删去 (35) 后仍称普遍成立。

## 7. 一个原算子反例：二次左尾确实不能省

取
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad L=\Phi_{p_0},
\qquad \tau=C(P,R),\qquad E=L.
$$
令 $r=u''$，并写
$$
\mu_0=\int r^2,\qquad M_3=\int r^3.
$$
原算子给
$$
q_P=J(r^2),\qquad q_R=(u')^2+xJ(r^2),
$$
$$
T=\tau(u;u,u)=-\frac13J(r^3).
\tag{38}
$$
可由
$$
q_R'=2u'r+Jr^2-xr^2,\qquad
q_R''=2(u'-xr)r'
$$
直接代入交换子核定 (38)，同右端三常数为零。

因此左尾为
$$
(q_P)_{\rm left}=\mu_0,\quad
(q_R)_{\rm left}=x\mu_0,\quad
T_{\rm left}=-M_3/3,
$$
$$
(q_L)_{\rm left}=(\mu_2-x^2\mu_0)/4.
\tag{39}
$$
$b_P$ 的左尾是常数，$b_R$ 的左尾是 $x$ 乘同一个常数，所以
$$
\mathcal G(q_P,b_R)=\mathcal G(q_R,b_P)=0.
$$
但
$$
\mathcal G(q_L,T)
=\left(-\frac{\mu_0}{2}\right)
\left(-\frac{M_3}{3}\right)
=\frac{\mu_0M_3}{6}.
$$
式 (33) 准确成为
$$
\boxed{
\Omega_u(\mathcal B_L C(P,R))
-\frac{16}{5}\int u'''\pi\mathcal B_L C(P,R)(u)
=\frac{2}{15}\mu_0M_3.
}
\tag{40}
$$

这里确有实紧 $u$ 使右端非零。例如取一个非负、非零、偶的
$\varphi\in C_c^\infty((-1/8,1/8))$，令
$$
r(x)=\varphi(x+1)-2\varphi(x)+\varphi(x-1),\qquad
u=J^2r.
$$
三个支撑不交，且
$$
\int r=\int xr=0.
$$
所以 $u$ 真紧，$u''=r$。同时
$$
\mu_0=6\int\varphi^2>0,\qquad
M_3=-6\int\varphi^3\ne0.
$$
可将整个有限配置先共同平移进所需正区间；这两个积分不变。此处只给解析反例，没有评价任何具体 bump 的积分。

这个反例否定一般实紧输入上无尾的 $16/5$ 公式。它本身没有断言 $\pi\mathcal B_L C(P,R)=0$，所以**也没有**反向证明 $\Omega_u$ 在 $\mathcal R\cap\ker\pi$ 上必非零。该纯核问题须依据 (31) 与真实响应关系另解，不能由一个非 pure-zero 反例越界推出。

## 8. 对真实 range 和已有控制结论的影响

[R330 的两个内部退化通量](R330-two-actual-packet-degenerate-fluxes-and-twenty-observation-control.md) 依赖原 $L_f$ 的准确局部边界身份，其证明没有使用本文被否定的无尾收缩，因此不受影响。

对于一整个平端实际微包，$\int u'''G$ 仍可作为原 period range 的必要总通量读出；但是要判断响应能否改变它，必须使用 (33)，保留真实尾量。不能从 formal $D^3$ 自伴直接宣布所有 pure-zero 响应都杀掉它。

同样，whole universal pure 与 whole universal self 的联合实际控制，不提供本文未证的桥
$$
Q(V)=0\Longrightarrow\Omega_u(V)=0.
$$
这里的 $Q$ 是原 $x^2$ 左尾 self 坐标及其忠实完整呈示，不是整个函数 $V(u^2,0)$。完整 self 可达性与全部 period 可达性仍有区别。

下一项实际数学问题因而被准确分开：

- 在一般实输入上，决定 (31) 在 $\mathcal R\cap\ker\pi$、进一步在 $\mathcal R\cap\ker(\pi,Q)$ 上的真实像；
- 在已满足 (35) 的复输入上，检验 (37) 对真实 $U$ 成本的值，以及它是否对应当前同一实圆的未付 joint range 门；
- 若使用已有 self 控制器，逐原式计算其 Green 量，而不是把不同控制商的满射直接相加。

本稿只完成准确恒等与上述适用边界，没有预授这些后继问题的答案。