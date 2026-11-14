# 单中央非正势下的实际全周期内部解与普通源估计

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / root。

**状态：完整证明草稿，待未参与者全文独审。** geometric_closure 提供并与 root
讨论了实际 Sturm 变换、外区估计和中央势的用途；本稿的 Green、全端点/通量
闭合与有效常数由 root 写出。因此 geometric 不是本稿的未参与审者。

对象是同一个 fixed flat17 解析 Target 的旋转背景线性化及第一 outward 周期。
本稿给两个指定 Hadamard incoming 端口的真正全内部/普通 $L^2$ 源解，
不改变度量、周期、加速度零点、均值或源分量。不把此辅助边值逆说成
实际非径向候选、原尾 Robin 反馈或非线性闭面问题的逆。

## 1. 固定对象和已付输入

令 $c=a'$、$Q=aa''$、$\bar p=(1-c^2)^{-1/2}$、$\alpha=\bar p/a$。
实际 Gauss–Codazzi 线性变量为 $U=(\beta,\pi)^T$，普通源为 $f=(f_1,f_2)^T$。
按 [R75](../results/R75-flat17-sturm-frequency-propagator.md) 的精确变换，
$$
x=\frac\beta\alpha,\qquad y=\frac\pi{\bar p^3},\qquad
\frac{dr}{ds}=\frac1{a^2\bar p}>0,\qquad Z=(x,y)^T,
\tag{1}
$$
同一全周期 $0\le r\le R$ 的完整系统是
$$
x_r=-V(r)y_u+g_1,\qquad y_r=-x_u+g_2,
\qquad V=\frac{a^3a''}{(1-c^2)^2},
\tag{2}
$$
$$
g_1=a^3f_1,\qquad g_2=a^2\bar p^{-2}f_2.
\tag{3}
$$
这里 $u\in\mathbb R/(2\pi\mathbb Z)$。全部 Fourier 模 $j\in\mathbb Z$ 保留，
$k_j=\langle j\rangle=\sqrt{1+j^2}$。每模满足
$$
Z_j'=A_j(r)Z_j+g_j,\qquad
A_j=-ij\begin{pmatrix}0&V\\1&0\end{pmatrix}.
\tag{4}
$$

R75 及其完整独审已对原五个 exact-binary 参数和精确 Target 时长证明：
存在 $0<r_-<r_+<R$ 使
$$
V\ge0\quad\text{于 }[0,r_-]\cup[r_+,R],\qquad
V\le0\quad\text{于 }[r_-,r_+],
\tag{5}
$$
$$
R<\frac32,\qquad |V|<\frac{81}{80},\qquad
\frac5{12}<L:=r_+-r_-<\frac32.
\tag{6}
$$
中央两个负 ramp 在一个二次零点相接，势不变号；外区包含原开放平段，
没有改成简单根。这里的证明只需 $0<L<3/2$，不靠下界 $5/12$ 加强结论。

尤其，对同一个实际外区内的任意两点和两个方向，真正基本解满足
$$
\|T_j(r_2,r_1)\|\le6k_j^2.
\tag{7}
$$
这是 R75 的全模正变差能量估计，不是 WKB 主项或数值截断。
因此有源时仍有实际变常数式
$$
|Z_j(r_2)|\le6k_j^2
\left(|Z_j(r_1)|+\int_{\text{两点间区间}}|g_j(t)|\,dt\right).
\tag{8}
$$
反向时积分取正长度。R75 原稿 14295 B，SHA256
`68962bac35e0a6969ce159b17e0b7754698cffc816248ddfb596c35a7a93f5db`；
其[全文独审](2026-11-10-78718-audit-flat17-sturm-frequency-provider-v1.md)
17678 B，SHA256 `2342490bf048e45797d2ff278055228f1a081d6532bcda340f735fbe1b8279e2`。

## 2. 指定两端口、每模真实存在及准确通量

记
$$
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
P=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad z=PZ.
\tag{9}
$$
给定 incoming 和求出的 outgoing 分别为
$$
a_j=\binom{z_{+,j}(0)}{z_{-,j}(R)},\qquad
b_j=\binom{z_{-,j}(0)}{z_{+,j}(R)},\qquad I_j=|a_j|,\ O_j=|b_j|.
\tag{10}
$$
这是本稿选定的具体二点条件，不是把两端全部 $Z$ 都指定。

因 $A_j^*J+JA_j=0$、$\operatorname{tr}A_j=0$，真实齐次基本解满足
$T_j^*JT_j=J$、$\det T_j=1$。令
$$
PT_j(R,0)P=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
$$
则 $D=\overline A$、$C=\overline B$、$|D|^2-|B|^2=1$，所以 $D\ne0$。
对任一固定整数 $j$ 和 $g_j\in L^2(0,R;\mathbb C^2)$，连续系数 ODE
的变常数积分实际存在。写
$$
w=P\int_0^R T_j(R,t)g_j(t)\,dt.
$$
给定 $a_j=(a_{1j},a_{2j})$，唯一初始值为
$$
z_{+,j}(0)=a_{1j},\qquad
z_{-,j}(0)=\frac{a_{2j}-Ca_{1j}-w_-}{D}.
\tag{11}
$$
故每模先已有唯一实际 $H^1_r$ 解，不是先假定全角解后只给先验估计。
逐模大频率传播虽可能很大，此处固定 $j$ 的有限积分没有存在问题。

设
$$
F_j=\|g_j\|_{L^2(0,R)},\qquad
E_j=|Z_j(0)|+|Z_j(R)|.
\tag{12}
$$
正交 $P$ 和端口分组给精确恒等式
$$
|Z_j(0)|^2+|Z_j(R)|^2=I_j^2+O_j^2.
$$
特别必须用
$$
E_j\le\sqrt2\sqrt{I_j^2+O_j^2}
\le\frac32(I_j+O_j),
\tag{13}
$$
不能把它无依据改成 $E_j\le I_j+O_j$。

对实际 $H^1$ 解，绝对连续通量满足
$$
\frac{d}{dr}(Z_j^*JZ_j)=2\operatorname{Re}(Z_j^*Jg_j).
$$
积分和 (10) 给
$$
O_j^2-I_j^2
=2\operatorname{Re}\int_0^R Z_j^*Jg_j\,dr,
\qquad
O_j^2-I_j^2\le2\|Z_j\|_{L^2}F_j.
\tag{14}
$$
均值 $j=0$ 同样成立；本证明不作零均值投影。

## 3. 非负 Dirichlet 势的 Green 核：完整所需界

暂在 $0\le t\le L$ 取任意连续 $q(t)\ge0$，记
$\mathcal L_q=-\partial_t^2+q$，两端为零 Dirichlet。
令 $u_L''=qu_L$、$u_L(0)=0,u_L'(0)=1$；
$u_R''=qu_R$、$u_R(L)=0,u_R'(L)=-1$。
积分方程或首次零点论证给内部
$$
u_L>0,\quad u_L'\ge1,\quad u_L''\ge0,
\qquad u_R>0,\quad u_R'\le-1,\quad u_R''\ge0.
\tag{15}
$$
例如 $u_L$ 在保持非负的区间有 $u_L'\ge1$，故不可能出现第一个正零点；
右端反向同理。Wronskian
$$
W=u_L'u_R-u_Lu_R'>0
$$
在内部为常数。真实 Green 核为
$$
G(s,t)=\frac{u_L(\min(s,t))u_R(\max(s,t))}{W}\ge0.
\tag{16}
$$
它在两端为零，连续，沿对角的 $s$ 导数跳跃为 $-1$，因此
$\mathcal L_qG(\cdot,t)=\delta_t$。

令 $G_0$ 为 $q=0$ 的核。差 $v=G_0(\cdot,t)-G(\cdot,t)$ 无导数跳跃，
满足零边界及 $\mathcal L_qv=qG_0\ge0$。若 $v_-=\max(-v,0)$ 非零，
弱式乘 $v_-$ 给
$$
0\le\int qG_0v_-=-\int\left(|v_-'|^2+qv_-^2\right)\le0,
$$
故 $v_-=0$。因此
$$
0\le G(s,t)\le G_0(s,t)
=\frac{\min(s,t)(L-\max(s,t))}{L}\le\frac L4.
\tag{17}
$$

还需要比点值更关键、对任意大的 $q$ 都一致的导数界。若 $t<s$，
$$
G_t(s,t)=\frac{u_L'(t)u_R(s)}W
\le\frac{u_L'(s)u_R(s)}W\le1.
$$
若 $t>s$，由于 $-u_R'$ 不增加，
$$
-G_t(s,t)=\frac{u_L(s)(-u_R'(t))}W
\le\frac{u_L(s)(-u_R'(s))}W\le1.
$$
两侧符号分别为非负/非正；故几乎处处
$$
|G_t(s,t)|\le1,\qquad
\|G(s,\cdot)\|_{L^2_t}\le\frac{L^{3/2}}4,\qquad
\|G_t(s,\cdot)\|_{L^2_t}\le\sqrt L.
\tag{18}
$$
这里没有借 $q$ 严格正或排除中央零点。

## 4. 中央普通源的无额外径向导数估计

在中央区间把起点平移到0，置 $q=-j^2V\ge0$。从原一阶系统消元，
仅在弱意义下
$$
\mathcal L_q y_j=ijg_{1,j}-\partial_r g_{2,j}.
\tag{19}
$$
不假设 $g_2$ 有径向导数或端点值。令 $y_h$ 解同一齐次 Dirichlet 问题，
边界值取实际 $y_j(r_-),y_j(r_+)$。其实际存在唯一性可由 (15) 的两基解
和 $W>0$ 得到。对复值 $y_h$，
$$
(|y_h|^2)''=2|y_h'|^2+2q|y_h|^2\ge0,
$$
所以
$$
\sup|y_h|\le B_j:=\max(|y_j(r_-)|,|y_j(r_+)|).
\tag{20}
$$
零边界的真实弱式 Green 表达为
$$
y_j(s)-y_h(s)
=ij\int_0^L G(s,t)g_{1,j}(t)\,dt
 +\int_0^L G_t(s,t)g_{2,j}(t)\,dt.
\tag{21}
$$
对光滑源这就是积分分部，边界项因 $G=0$ 消失。对普通 $L^2$ 源，
先以光滑源在 $L^2$ 逼近；两个零边界解之差 $v$ 的能量给
$$
\int(|v'|^2+q|v|^2)
\le (|j|L\|\Delta g_1\|_2+\|\Delta g_2\|_2)\|v'\|_2,
\tag{22}
$$
其中 $\|v\|_2\le L\|v'\|_2$ 来自基本积分和 Cauchy–Schwarz。
故解在 $H^1_0$ 收敛，进而一致收敛；(18) 也使右边一致收敛。
弱 Dirichlet 解由同一零源能量唯一，于是 (21) 对实际一阶解成立。
这明确支付普通源的解释，不把 $g_2'$ 当作已有 $L^2$ 数据。

由 (18)–(21)，
$$
\sup_{[r_-,r_+]}|y_j|
\le B_j+\left(\frac{|j|L^{3/2}}4+\sqrt L\right)F_j.
\tag{23}
$$
再对一阶 $x_j'=-ijVy_j+g_{1,j}$ 真实积分，
$$
\sup_{[r_-,r_+]}|x_j|
\le |x_j(r_-)|+|j|\frac{81}{80}L\sup|y_j|+\sqrt L F_j.
\tag{24}
$$
此步不除 $j$，所以 $j=0$ 已包含。

## 5. 从真实两端点到内部的有效多项式界

以下固定一个模，简写 $k=k_j,E=E_j,F=F_j$。
因 $R<3/2$，有 $\sqrt R<5/4$；同样 $\sqrt L<5/4$、
$L^{3/2}/4<1/2$。先从两个实际外端分别用 (8) 得全外区
$$
|Z_j(r)|\le6k^2 E+\frac{15}{2}k^2F.
\tag{25}
$$
该式同时控制中央的两个边界值，故 (23)、$|j|\le k\le k^2$ 给
$$
Y:=\sup_{[r_-,r_+]}|y_j|
\le6k^2E+\frac{37}{4}k^2F.
\tag{26}
$$
用 $L(81/80)<243/160$、$k\ge1$，(24) 给
$$
X:=\sup_{[r_-,r_+]}|x_j|
\le\frac{1209}{80}k^3E+\frac{14591}{640}k^3F.
\tag{27}
$$
所有常数来自有理加乘：$1209/80=6+(243/160)6$，
$14591/640=15/2+(243/160)(37/4)+5/4$。
中央的 Euclidean 范数至多 $X+Y$，因此全周期
$$
\sup_r|Z_j(r)|
\le33k^3(E+F),\qquad
\|Z_j\|_{L^2_r}\le50k^3(E+F).
\tag{28}
$$
因为 $1209/80+6=1689/80<33$，
$14591/640+37/4=20511/640<33$，外区常数更小，且 $(5/4)33<50$。
若需要统一宽松点值常数，可把第一式右端33改40；下节采用此宽松界。

## 6. 通量闭合真实未知 outgoing，而非把端点都假定有界

将 (13) 代入 (28)，得到
$$
\|Z_j\|_{L^2_r}\le75k^3(I_j+O_j+F_j).
\tag{29}
$$
于是通量 (14) 给
$$
O_j^2-I_j^2\le150k^3(I_j+O_j+F_j)F_j.
\tag{30}
$$
分完整三种情形：若 $O_j\le I_j$，已无问题；若 $O_j>I_j$ 且
$I_j+O_j\ge F_j$，除以正数 $I_j+O_j$ 得
$O_j-I_j\le300k^3F_j$；最后若 $I_j+O_j<F_j$，直接有 $O_j<F_j$。
因此统一保守取
$$
\boxed{\quad O_j\le I_j+400k_j^3F_j.\quad}
\tag{31}
$$
这里可以缩常数，但本稿不依赖优化；$F=0$ 时通量其实给 $O_j=I_j$。

把 (31) 回代 (29) 得
$$
\|Z_j\|_{L^2_r}\le150k^3I_j+30075k^6F_j.
\tag{32}
$$
同样，(28) 的宽松点值40配 (13) 给
$$
\sup_r|Z_j(r)|\le60k^3(I_j+O_j+F_j)
\le120k^3I_j+24060k^6F_j.
$$
所以可统一记为
$$
\boxed{\quad
\max\left(\sup_r|Z_j(r)|,\|Z_j\|_{L^2_r}\right)
\le200k_j^3 I_j+40100k_j^6F_j.
\quad}
\tag{33}
$$
没有指数 $e^{c|j|}$、没有解析带宽损耗；代价是明确的3次/6次角导数。
它来自两个 prescribed incoming 的二点问题，不能冒充一般初值 Cauchy 问题
的无指数前向传播。后者会把一个远端 incoming 随解一起放大，两命题不冲突。

均值可再直接核：$j=0$ 时 $z_r=Pg$，
$$
z_+(r)=a_{10}+\int_0^r(Pg)_+\,dt,\qquad
z_-(r)=a_{20}-\int_r^R(Pg)_-\,dt.
\tag{34}
$$
两个实际端口及两个均值均保留，$O_0\le I_0+\sqrt R F_0$，
且 $\sup|Z_0|\le I_0+\sqrt R F_0$，均被上式覆盖。

## 7. 真正全角解、任意共同权与逐项极限

对任意正数权列 $w_j>0$ 和实阶数 $\nu$，定义 Fourier Hilbert 完备化
$$
\|h\|_{w,\nu}^2
=\sum_{j\in\mathbb Z}w_j^2 k_j^{2\nu}|h_j|^2.
\tag{35}
$$
两个端口/两个内部变量共用同一个权。它包括 Sobolev、log 和指数解析权。
对于任意极端增长/衰减权，只声称此 Hilbert 完备化中的系数解，
不把所有这种抽象元素都称作分布；普通 Sobolev/log 类自然给真实分布。

定理：给定 $a\in X_w^{\nu+3}(\mathbb C^2)$ 和
$g\in L^2_rX_w^{\nu+6}(\mathbb C^2)$，(2)、(10) 有唯一逐模解，且
$$
Z\in C([0,R];X_w^\nu)\cap H^1([0,R];X_w^{\nu-1}),
\tag{36}
$$
$$
\max\left(\sup_r\|Z(r)\|_{w,\nu},
                 \|Z\|_{L^2_rX_w^\nu}\right)
\le200\|a\|_{w,\nu+3}
  +40100\|g\|_{L^2_rX_w^{\nu+6}}.
\tag{37}
$$
边界另外满足对任意阶数 $\lambda$ 的准确有限损失估计
$$
\|b\|_{w,\lambda}\le\|a\|_{w,\lambda}
   +400\|g\|_{L^2_rX_w^{\lambda+3}},
\tag{38}
$$
只要右边有限。对 (36) 的输入可特别取 $\lambda=\nu+3$，
所以输出端口保留与输入相同的较高角阶。

证明不是形式求和：先对 $|j|\le N$ 使用真实解 (11)，用 (33) 对各模乘权，
再取 $\ell^2$ 范数和 Minkowski，(37) 即对每个有限部分和一致成立。
$\sum w_j^2k_j^{2(\nu+6)}F_j^2$ 由 Tonelli 恰为源的声明 $L^2$ 范数。
对两部分和之差使用同一估计，右端只是数据尾，趋零；故部分和在
$C_rX_w^\nu$ 和 $L^2_rX_w^\nu$ 真正收敛。

由 $\|\begin{psmallmatrix}0&V\\1&0\end{psmallmatrix}\|\le81/80$ 和 $|j|\le k_j$，
$$
\|\partial_r Z\|_{L^2_rX_w^{\nu-1}}
\le\frac{81}{80}\|Z\|_{L^2_rX_w^\nu}
    +\|g\|_{L^2_rX_w^{\nu-1}}.
\tag{39}
$$
同一尾差估计使导数也收敛，给 (36) 及真实逐模/分布方程和端点值。
(38) 由 (31) 逐模求和，输出同样为极限。每模唯一性保证全类唯一性，
不需选择模数截断后的新逆。

实系数及 $j\leftrightarrow-j$ 共轭对称使实数据的解为实。
若数据有所有 Sobolev 阶、源对 $r$ 在这些角范数连续，角级数及所有角导数
一致收敛，(2) 再给经典 $C^1_r$、角 $C^\infty$ 解。
固定正解析权 $w_j=e^{\sigma|j|}$ 时 (37) 保同一 $\sigma$，
但须如实支付有限角阶；不能只由一个没有多项式余量的边界范数声称无损。

## 8. 物理源和原变量的明确单位

原周期两端 $a=1,c=0,\bar p=1$，所以 $Z=U$，端口没有隐藏缩放。
R75 已证明
$$
\|g_j\|_{L^2_r}<\frac54\|f_j\|_{L^2_s},\qquad
\|U_j\|_{L^2_s}<\frac65\|Z_j\|_{L^2_r}.
\tag{40}
$$
还因 $U=\operatorname{diag}(\bar p/a,\bar p^3)Z$、$\bar p<51/50$、$a\ge1$，
$\sup|U_j|<(6/5)\sup|Z_j|$。故同一物理普通源有保守全周期界
$$
\boxed{\quad
\max\left(\sup_s|U_j(s)|,\|U_j\|_{L^2_s}\right)
\le250k_j^3I_j+61000k_j^6\|f_j\|_{L^2_s},
\quad}
\tag{41}
$$
$$
O_j\le I_j+500k_j^3\|f_j\|_{L^2_s}.
\tag{42}
$$
数值只用 $(6/5)200=240<250$ 和
$(6/5)(5/4)40100=60150<61000$。径向坐标变换和矩阵均与角无关，
所以同样的 (37)–(38) 物理版也对全部共同 Fourier 权成立。
这里的 $f$ 必须确为完整线性 GC 方程的两分量源；未转换的 metric column
不能直接代入。实际 Darboux/位置变量的变换、边界源与接合还需分别支付。

## 9. 实际推进范围与不能省略的边界问题

本稿在固定全宽周期上支付了此前只有逐模酉边界算子但尚缺的内部存在、
普通 $L^2$ 源和有限角损失；均值、开放平段、二次零点都在同一证明内。
没有运行 PDE、调候选参数、改变任何物理常数或借用旧候选数组。

真正曲面问题仍有独立要求：实际 core/bridge/tail 选择的反射或 Robin
关系一般是 incoming 与 outgoing 的反馈，不是本稿两个自由 incoming。
即使齐次散射酉且每模 cross transmission 非零，反馈差矩阵仍可能奇异
或逆随频率增长，不能从 (31) 得到其统一逆。当前非径向候选还引入角依赖
系数，失去这里的精确逐模分解；非线性扰动也不由有限导数损失自动闭合。

因此本稿没有支付原选定 range 的 $K_0$、原尾 DN/Schur 逆、全非线性曲面、
闭合帽、固定 $H$、有效幅度、全时reach或README/G5。它是实际同一背景的
完整辅助内部源 provider，后续可以用，但必须核真实端口和全部转换。
