# R821 — 第四真实来源、四高轴必要系统与完整四块 carry

后继：[R824 完整物理四次核及真正中央 Schur 行](R824-original-quartic-first-correctors-and-native-central-schur.md)支付十三行边界单位障碍和同R分支值，保全部native项。

日期：2026-11-15。**状态：下列固定来源恒等式、四高轴整多项式系统、单位 Jacobian、完整四块评价及接触阶判据已证明。**

R816/R820 的 $E_{-11}$ 给第四条真实中央函数。本篇把它与原 $S_{34},T_{72},U_{136}$ 放在同一个 Gaussian 和同一个实际角参数中。四条中央同时零，确实约束四个确定的实际高系数模 $p^4$。这个结论是必要条件，不是四个独立算术变量，也不从低 Taylor 子式推出原矩阵已有一个可提升的四次幂首核。

本篇使用固定的 $(4,3,2,1)$ 子式，并删去其明确有限分子坏集。原十三行前缀完整保留：四块目标有三条十三行跨界带；在最后两个允许窗口还存在一个 $p^3$ 层的四次末端项。特别，$\epsilon^4=0$ 不能用来删掉这个已折回第三块的项。

## 1. 同一模型上的第四来源与全部固定角因子

使用共同 $E_1:y^2=x^3+1$，并置
$$
w=z^6,\quad t=-x^{-3},\quad\Theta=x\sigma^2,\quad
d=1+8t,\quad h_7=7+4t+16t^2,\quad\mathfrak a=t(t-1)h_7.
\tag{1}
$$
原三个来源为
$$
S=\Theta^{17}f_S,\quad T=\Theta^{36}f_T,\quad U=\Theta^{68}f_U,
$$
$$
f_S=\mathfrak a d/7,\quad
f_T=f_S(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3),\quad
f_U=\mathfrak a H_{18}/91.
\tag{2}
$$
$H_{18}$ 是 R468/R812 的完整十八次多项式。三个来源首项均为 $w$。

R816 的完整 $E_{-11}$ Schwartz 来源在共同模型上记为 $V$。它的准确角式是
$$
\boxed{
V=\Theta^{33}f_V,\qquad
f_V=\frac17\,\mathfrak a d^2(4t-1)
                   (-1+228t-48t^2+64t^3).
}
\tag{3}
$$
等价地，$V=\sigma^{66}\sum_{j=0}^{10}c_jx^{3j}$，其中升幂系数为
$$
(c_0,\ldots,c_{10})=
\left(0,\frac{262144}7,\frac{393216}7,159744,119808,
\frac{212736}7,53376,-\frac{7248}7,-\frac{18156}7,
\frac{1515}7,1\right).
\tag{4}
$$
由 $f_V=\sum c_j(-t)^{11-j}$ 直接得到 (3)。因此
$$
\operatorname{ord}_{t=0}f_V
=\operatorname{ord}_{t=1}f_V
=\operatorname{ord}_{h_7=0}f_V=1,\quad
\operatorname{ord}_{d=0}f_V=2,\quad \deg f_V=10.
\tag{5}
$$
$h_7$ 一栏在两个根上分别成立。所有固定角因子都在 (3) 中，没有把 $d^2$ 降成 $d$。

还有一个有用但不传播中央零的全函数式：
$$
\boxed{V=S\,H_{32},\qquad H_{32}=\Theta^{16}K_5,}
$$
$$
K_5=d(4t-1)(-1+228t-48t^2+64t^3)
=1-224t-896t^2+7424t^3-1792t^4+2048t^5.
\tag{6}
$$
$H_{32}$ 是完整全纯 degree32 截面，质量为一。在普通整 Amice 格中它为卷积单位；中央 Mellin 导数不是卷积乘法泛函，所以 (6) 不把 $J'_S=0$ 变成 $J'_V=0$。第四中央的授权来自 R816/R820 的完整曲线、Schwartz、周期及通常 Selmer 桥。

式 (3) 同时给 $V\in B_{33}$，其中 $B$ 是 R473 已付的三来源整归一化，因为
$$
B_{33}=\Theta^{33}\mathfrak a\,R[t]_{\le6},\qquad
\deg(f_V/\mathfrak a)=6.
\tag{7}
$$
故添入 $V$ 不扩大原有理函数域，也不改变该归一化的 Hilbert 主项。R473 的固定导子 $c$ 有权10980，仍有 $cV\in A_{11013}$；这是一条有成本的来源返回，不给 $cV$ 新的中央零，也不把它免费放进旧 $Y$ 单部分。

## 2. 四个原中央及同一个 Gaussian

固定
$$
p=6s-1>211,\quad
\kappa=34[z^{p+1}]\log(\sigma/z)+\Delta,\quad
\Delta\in\mathcal O,\quad a_p=p\kappa\in\mathcal O^\times.
\tag{8}
$$
四个相对 charge 为
$$
\boxed{q_S=1,\quad q_T=36/17,\quad q_U=4,\quad q_V=33/17.}
\tag{9}
$$
令
$$
g=d\Theta^{17}e^{-\kappa w^s},\qquad
\widehat\nu=(g/d)^{q_\nu}f_\nu(t),\quad \nu=S,T,U,V.
\tag{10}
$$
这些都是同一个实际 $g$ 的四个测试。对 $V$，$q_V\kappa$ 与 R820 的 $66c_p$ 只差 $q_V\Delta\in\mathcal O$。R342 的全 Newton 重标及四个来源的零质量保证中央导数准确不变，未只比较首权。

若记
$$
c_{\nu,h}=[w^{hs}]\widehat\nu,\qquad
J_\nu(v)=\sum_{h\ge0}(q_\nu\kappa)^{-h}c_{\nu,h}(v)_h,
\tag{11}
$$
则 R303、R402、R469、R820 分别给这些实际来源的完整算术桥。无穷性反证允许同时假定
$$
J'_S(0)=J'_T(0)=J'_U(0)=J'_V(0)=0.
\tag{12}
$$
本篇不假定四个数在任何意义下线性独立，也不把其零传播到任意角乘子或乘积。

## 3. 八权全式与原 Hurwitz 代数中的准确四权化

R301 的圆盘 $R=p^{-1/(2p)}$ 上，四个完整 regularized 来源均满足
$\|\widehat\nu\|_R\le R^6$。对 $V$，这由 (4) 的最小物理阶六直接给出；其余三源由各自已付的完整多项式给出。因而
$$
v_p\big((q_\nu\kappa)^{-h}c_{\nu,h}\big)
\ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil.
\tag{13}
$$
完整归一中央为
$$
\boxed{
\frac{a_p}{p}J'_\nu(0)=
\sum_{h\ge1}\frac{(-1)^{h-1}(h-1)!\,p^{h-1}}
 {q_\nu^h a_p^{h-1}}\,c_{\nu,h}.
}
\tag{14}
$$
仅用 (13)，对 $h=1,\ldots,8$，除去一个 $p$ 后的统一下界依次为
$$
0,\ 1,\ 1,\ 2,\ 2,\ 2,\ 3,\ 3.
\tag{15}
$$
当 $h\ge9$，连同 $(h-1)!$ 的赋值，整个余尾在 $p^4\mathcal O$ 中。因此先完整保留
$$
\boxed{
F_\nu^{[8]}=\sum_{h=1}^{8}\frac{(-1)^{h-1}(h-1)!\,p^{h-1}}
 {q_\nu^h a_p^{h-1}}\,c_{\nu,h}
\equiv\frac{a_p}{p}J'_\nu(0)\pmod{p^4}.
}
\tag{16}
$$
(15) 只是一般圆盘的保守界，不是本篇实际来源的尖锐赋值。

现在支付可以整消高权的更强原来源事实。令
$\mathscr H_{\mathcal O}=\{f:n![w^n]f\in\mathcal O\}$、
$W=z^2x$、$F^\circ=\log(\sigma/z)-c_pw^s$。
R602 已证明 $W,F^\circ\in\mathscr H_{\mathcal O}$，
且该代数封闭于乘法、单位逆和零常数项的指数。除去实际首项 $w$ 后，
$S,T$ 的余项在该代数中。对新两源也逐项有
$$
\frac{Ue^{-136c_pw^s}}w
=\sum_{j=0}^{21}P_jw^{21-j}W^{2+3j}e^{136F^\circ},
$$
$$
\frac{Ve^{-66c_pw^s}}w
=\sum_{j=1}^{10}c_jw^{10-j}W^{3j}e^{66F^\circ}.
\tag{16a}
$$
其中 $P_j$ 是 R468 完整 $P_{21}$ 的升幂系数。所有 $w$ 幂非负，固定分母在当前 $p$ 为单位。
另有 $t=-wW^{-3}\in w\mathscr H_{\mathcal O}$。
所以以后第4–5节的全部整参数 $h_A$、$h_{A^*}$，
以及 Gaussian 重标因子 $e^{-q_\nu\Delta w^s}$，均由同一整 Hurwitz 运算处理。
对整个参数 family 都得到
$$
\boxed{
(hs-1)!\,C_{\nu,h}\in\mathcal O,\qquad
v_p((q_\nu\kappa)^{-h}C_{\nu,h})
\ge h-v_p((hs-1)!).
}
\tag{16b}
$$
这不是把全 Taylor 系数先当整数。

R602 的单调尾界遂原样适用于四个来源及整个参数 family：
$$
v_p\big(J'_\nu-L_{\nu,H}\big)\ge
\left\lceil\frac{(H+1)(5p-7)+6}{6(p-1)}\right\rceil+v_p(H!).
$$
取 $H=4$，右边为5。因此 (16) 的第五至第八权和全部后续权，在归一后严格属于 $p^4\mathcal O$，并有
$$
\boxed{
F_\nu^{[8]}\equiv F_\nu^{[4]}
=\frac{c_{\nu,1}}{q_\nu}
-\frac{p\,c_{\nu,2}}{q_\nu^2a_p}
+\frac{2p^2c_{\nu,3}}{q_\nu^3a_p^2}
-\frac{6p^3c_{\nu,4}}{q_\nu^4a_p^3}
\pmod{p^4}.
}
\tag{16c}
$$
下文仍用完整 $F_\nu=F_\nu^{[8]}$ 记账；改用 (16c) 给完全相同的四位系统。第七、第八权没有未经证明地丢弃，而是由 (16a)–(16b) 的真实整来源消去。

若 $B_{\nu,k}=[w^{ks}]\nu$ 表示未删 Gaussian 的原系数，
有限卷积又准确给同一个必要条件
$$
\boxed{
\frac4{q_\nu}B_{\nu,1}
-\frac{6p}{q_\nu^2a_p}B_{\nu,2}
+\frac{8p^2}{q_\nu^3a_p^2}B_{\nu,3}
-\frac{6p^3}{q_\nu^4a_p^3}B_{\nu,4}
\in p^4\mathcal O.
}
\tag{16d}
$$
这使用同一个完整 $J'_\nu=0$；四个裸系数的组合整体整，不能先分别赋零或把各项都当整数。

## 4. 四个确定的实际角系数

保 R434 的实际角展开
$$
\log\Theta^{17}=\sum_{n\ge1}\ell_nt^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}.
\tag{17}
$$
对 $r=4,3,2,1$ 定义
$$
\boxed{A_r^*=\ell_{s-r}
       +(-1)^{s-r+1}\frac{8^{s-r}}{s-r}.}
\tag{18}
$$
它们就是原 $\log g$ 的 $t^{s-r}$ 系数：Gaussian 项从 $t^s$ 才开始。显示分母在当前 $p$ 为单位，故 $A_r^*\in\mathcal O$。

从原 $\log g$ 精确删去这四项，定义唯一参考 $g_\circ$。对计算参数 $A=(A_4,A_3,A_2,A_1)$ 置
$$
h_A(t)=\sum_{r=1}^4 A_rt^{s-r},\qquad g_A=g_\circ e^{h_A}.
\tag{19}
$$
只有 $A=A^*$ 恢复原算术对象。$a_p$、所有其它原角系数和全部低轴均保持原值；计算参数不是新的椭圆曲线。

设 $T(w)=-t(w)/w=1+3w/7+75w^2/637+\cdots$。唯一写成
$$
h_A=w^{s-4}P_3(w)+w^sH_A(w),\qquad
P_3=u_0+u_1w+u_2w^2+u_3w^3.
\tag{20}
$$
完整三角坐标式为
$$
u_j=\sum_{\substack{1\le r\le4\\4-r\le j}}
 A_r(-1)^{s-r}[w^{\,j-4+r}]T(w)^{s-r},\qquad0\le j\le3.
\tag{21}
$$
对角依次为 $(-1)^{s-4},(-1)^{s-3},(-1)^{s-2},(-1)^{s-1}$，行列式为一。它在 $\mathcal O$ 上可逆；$H_A$ 是确定且线性依赖 $A$ 的完整高尾。

物理四块窗口低于 $w^p$，R324 的原形式对数及反演整性保证其中所需的 $H_A$ 系数整。读取第七、第八 Newton 权时使用第3节已经支付的真实 Hurwitz 整性；第5节另给整个参数多项式的解析整性证明。式 (18) 保留 $8^{s-r}$ 的全部原值，因而包含全部实际 $q_p(2)$ 和 Gaussian 进位；没有用剩余类替代其模 $p^4$ 值。

## 5. 完整八权参数多项式的整性

令 $A_\nu=(g_\circ/d)^{q_\nu}f_\nu(t)$。对 $1\le h\le8$ 定义
$$
\boxed{
C_{\nu,h}(u)=[w^{hs}]A_\nu
 \sum_{m=0}^{h}\frac{q_\nu^m}{m!}h_A(w)^m.
}
\tag{22}
$$
其中 $A$ 按 (21) 由 $u$ 恢复，$h_A$ 包括 (20) 的整个 $H_A$。因为
$$
1+(h+1)(s-4)>hs\qquad(s>35,\ h\le8),
$$
高于 $m=h$ 的指数项不进入所读权。因此 (22) 是准确系数，关于 $u$ 的次数至多 $h$。

将 (22) 代入 (16)，仍记结果为 $F_\nu(u)$。下述整性不要求每个高权 $C_{\nu,h}$ 自身整：
$$
\boxed{
F_\nu\in\mathcal O[u_0,u_1,u_2,u_3],\qquad
F_\nu-\frac1{q_\nu}C_{\nu,1}
 \in p\mathcal O[u_0,u_1,u_2,u_3].
}
\tag{23}
$$

证明如下。R301 的严格圆盘满足 $\|x^{-1/2}/z\|_R=1$，故 $\|t\|_R=R^6$。对任何整参数，
$\|h_A-h_{A^*}\|_R\le R^{6(s-4)}$，其赋值 $(p-23)/(2p)$ 严格大于 $1/(p-1)$。于是 $e^{q_\nu(h_A-h_{A^*})}$ 及其逆真实收敛、范数一，整个参数来源仍有范数至多 $R^6$。所以 (13)–(15) 对全部整参数成立。

每个 (22) 的次数至多八。用每一变量的九个整点 $0,1,\ldots,8$ 作有限插值，Vandermonde 行列式的素因子均不超过七，在当前 $p$ 为单位。因此“在所有这些整点取整值”，以及高权和“取 $p$ 整除的值”，分别强迫整多项式系数及 $p$ 整除系数。这证明 (23)，也保留了所有高权实际分母。没有对参数网格作数学数值运行；这里是统一插值证明。

## 6. 固定四轴的精确 Jacobian 与有限坏集

四个参考的低四项与原来源相同，因被删高项的首阶大于四：
$$
\begin{array}{c|rrrr}
\nu &[w]\nu &[w^2]\nu &[w^3]\nu &[w^4]\nu\\ \hline
S&1&-988/105&16594771/1576575&-12606807124/725830875\\
T&1&-2938/35&-230804229/175175&2448768505164/152334875\\
U&1&135218/105&21083507491/1576575&1377083080404572/9435801375\\
V&1&7436/35&-53394351/15925&115502678148/13848625
\end{array}
\tag{24}
$$
这些有理数从原 $x''=6x^2$、$\sigma$ 的对数式和 (2)–(4) 求得。原首项全部为一。

$C_{\nu,1}/q_\nu$ 对 $u$ 的线性部分恰为
$$
u_0A_{\nu,4}+u_1A_{\nu,3}+u_2A_{\nu,2}+u_3A_{\nu,1}.
$$
因为 $A_\nu$ 质量零，$w^sH_A$ 不进入这个系数。由 (23)，整个 Jacobian 模 $p$ 在所有参数点恒为
$$
B_4=(A_{\nu,4},A_{\nu,3},A_{\nu,2},A_{\nu,1})_{\nu=S,T,U,V},
$$
$$
\boxed{\det B_4=-\frac{33226598045199130624}{173559375},
\qquad173559375=3^3\,5^5\,11^2\,17.}
\tag{25}
$$
以下固定删除
$$
\boxed{\mathcal B_4=\{p:p\le211\}\ \cup\
\{p:p\mid33226598045199130624\}.}
\tag{26}
$$
这是明确有限集合；没有用随 $p$ 改变的子式或未付的高度五、六轴。

**定理1。** 对 $p=6s-1\notin\mathcal B_4$，固定同一个 $g_\circ,t,a_p$ 后，四个 (16)、(22) 有唯一模 $p^4$ 的解 $u^\dagger$。四个原完整中央若同时零，实际 (18)、(21) 必满足
$$
\boxed{u^*\equiv u^\dagger\pmod{p^4}.}
\tag{27}
$$

证明先解模 $p$ 的仿射系统。若 $u_r$ 已解到 $p^r$，则
$$
u_{r+1}=u_r-p^rB_4^{-1}
 \big(F_S(u_r),F_T(u_r),F_U(u_r),F_V(u_r)\big)^t/p^r
 \pmod{p^{r+1}},\qquad r=1,2,3.
\tag{28}
$$
(23)、(25) 使每一步整且唯一。所有 $F_\nu$ 始终使用完整八权和整个 $H_A$。实际同时失败提供一个解，唯一性给 (27)。这不把一个形式 Hensel 解变成新算术对象，也不把模 $p^4$ 必要条件变成完整中央零的充分条件。

## 7. 重复倍点来源为什么不能重复计中央

本节明确排除一种错误的独立性推断。R812 的 $A(z)=S(2z)/64$ 也是 degree136 来源，并有不同低 Taylor 行，但其完整中央严格满足
$$
J_A'(0)=J_S'(0)/64.
\tag{29}
$$
一般地，对固定整数 $m$、$p\nmid m$，令 $A_m=m^{-6}S(mz)$，使用它的 theta Gaussian $m^2\kappa$。完整整数权卷积及 R342 重标给
$$
\boxed{
J_{A_m}(v)=m^{-6}\big(m^{p-1}\big)^vJ_S(v),\qquad
J_{A_m}'(0)=m^{-6}J_S'(0).
}
\tag{30}
$$
这里 $m^{p-1}\in1+p\mathcal O$，且原质量为零。

为什么它仍可能给一个非零的形式低 jet 子式？围绕实际原来源作共同角变形 $\delta h$ 时，正确倍点变形是
$$
m^{-6}S(mz)e^{\delta h(mz)}.
$$
若把它当作独立 charge $m^2$ 的角行，则使用的是
$$
m^{-6}S(mz)e^{m^2\delta h(z)}.
$$
两者差一个完整且通常非平凡的因子
$$
\boxed{\exp\{m^2\delta h(z)-\delta h(mz)\}.}
\tag{31}
$$
因此正确 pullback family 的中央行严格成比例；共同角坐标 family 离开原倍点轨道后才可能有较高 Jacobian 秩。不能丢掉 (31) 再把形式秩计成新的算术条件。

第四来源 $V$ 的完整十一处 ramified Hecke 角色由 R816 单独支付，旧三条来源在十一处没有该角色。它也不是原 $S$ 的一个 CM 标量 pullback：所需范数比 $66/34=33/17$ 在惰性素数17处赋值为 $-1$，不是 $K=\mathbf Q(\sqrt{-3})$ 元素的范数。相对 $T,U$ 的范数比同样有惰性素数11的奇赋值。

这些事实排除了这里显示的重复倍点机制，但本篇仍不由 (25) 证明四个中央值的算术独立性。**定理1支付的是四条已授权真实等式的必要坐标系统；从该系统到原深核或预算收益，仍须同一实际来源的额外论证。** 任意多 $S(mz)$ 不能使后面的目标深度成为免费结论。

## 8. 同一原来源的完整四块评价与三条十三行带

保留原 canonical 来源和完整 $P_{134}/U_0$，不把新 $V$ 免费加入旧单部分。四块评价本身是一个无条件定义的实际映射；它的存在不由中央条件的条数推出。

令
$$
L_4=3s+\ell,\qquad1\le\ell<s-13,
$$
$$
\Gamma_{L_4}^{(4)}
=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^4,w^\ell\epsilon^3),
$$
$$
\Gamma_{L_4+13}^{(4)}
=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^4,
                         w^{\ell+13}\epsilon^3).
\tag{32}
$$
原 R324 的有限整性覆盖全部当前物理窗口，因 $L_4+13<4s<p$。只需将原 Gaussian 的整指数截断到三次，全部 $0!,1!,2!,3!$ 为单位。

对实际相对来源 $P$，令 $P_i(w)=(\mathcal E_{\rm rel}^iP)(t(w),\vartheta(w))$，
$\vartheta=(g/d)^{1/17}$，并令 $\mathscr S$ 为准确的 $s$ 阶系数移位。整个评价是
$$
\boxed{
J_4(P)=
\begin{pmatrix}
[P_0]_{<s}\\
[a_pP_1+p\mathscr SP_0]_{<s}\\
[\frac{a_p^2}{2}P_2+pa_p\mathscr SP_1+p^2\mathscr S^2P_0]_{<s}\\
[\frac{a_p^3}{6}P_3+\frac{pa_p^2}{2}\mathscr SP_2+
p^2a_p\mathscr S^2P_1+p^3\mathscr S^3P_0]_{<\ell}
\end{pmatrix}.
}
\tag{33}
$$
没有把末块的真实三次 Euler 行换成另一个自由参数。

同一个完整物理评价仍为
$$
M_\circ^{\rm orig}=c_*U_{0,\circ}m_{13}J_{4,\circ}.
\tag{34}
$$
每列的总 charge 是原相对 charge 加四十，记为 $\mathcal E_{\rm tot}$。对已经付成本的混合列，保其全部真实 charge；若另外通过 R473 的导子运输 $V$，须使用那条真实运输后的整个列，不能只把 $33/17$ 填进旧列格。

乘 $w^{13}$ 在三个满块各有一条十三行跨界带，准确落在源下标
$$
s-13,\ldots,s-1;\quad
2s-13,\ldots,2s-1;\quad
3s-13,\ldots,3s-1.
\tag{35}
$$
每个跨界坐标乘一个 $p$。最后部分块因 $\ell<s-13$ 不再跨界。所以该运输的固定 Smith 成本为39，而非旧三块的26；最前十三个自由目标方向仍保留。对同一实际源格，任意精度核长度差在0与39之间。

## 9. 原 $M$ 的完整参数式，包括末端四次项

令 $P_3,H_A$ 如 (20)。在 (32) 的整个目标中，
$$
\boxed{
\begin{aligned}
M_A^{\rm orig}=c_*U_{0,\circ}\bigg\{
&\sum_{j=0}^{3}\frac{p^j\epsilon^j}{j!}
 w^{13-4j}(P_3+w^4H_A)^j
 J_{4,\circ}\mathcal E_{\rm tot}^{\,j}\\
&+\frac{p^3\epsilon^3}{24}w^{s-3}P_3^4
 J_{4,\circ}\mathcal E_{\rm tot}^{\,4}
\bigg\}\pmod{p^4}.
\end{aligned}
}
\tag{36}
$$
每个 $J_{4,\circ}$ 使用完整所需前缀；公共单位 $U_{0,\circ}$ 未取常数。第一行的物理前缀准确是 $13,9,5,1$，所以三次项完全整。

证明逐列乘 $e^{Qh_A}$。对 $j\le3$，准确使用 $w^{j(s-4)}=p^j\epsilon^jw^{-4j}$，与原 $w^{13}$ 合并后没有负幂。第四次项的首阶却是
$$
w^{13+4(s-4)}=w^{4s-3}
=p^3\epsilon^3w^{s-3},
\tag{37}
$$
而不是一个可合法书写为 $p^4\epsilon^4w^{-3}$ 的整项。第四次项中一旦出现 $w^4H_A$，阶至少为 $4s+1$，已超出目标；所以只剩 (36) 的 $P_3^4$。第五次及更高项首阶至少 $5s-7>4s$，真正消失。这证明 (36)。

式 (36) 第二行自动给全部末端情形：

- $\ell\le s-16$ 时，$\epsilon^3w^{s-3}=0$，该行完全消失。
- $\ell=s-15$ 时，保 $U_{0,\circ}P_3^4J_{4,\circ}\mathcal E_{\rm tot}^4$ 的常数项。
- $\ell=s-14$ 时，保同一完整乘积的常数和一次项。

两个末端情形都保原公共单位，不能只取 $J$ 的裸常数而遗漏 $U_0$ 的一次项。它们是真正的 $p^3$ carry。

立即有
$$
\boxed{\bar M_A^{\rm orig}=\bar M_\circ^{\rm orig}.}
\tag{38}
$$
并且 $M_A\bmod p^4$ 至多读取 $u\bmod p^3$：一次项已有 $p$，二次项已有 $p^2$，三、四次项已有 $p^3$。定理1给出的第四位实际高轴信息不能仅因没有出现在这个矩阵中就被算作已实现的第四深核。

## 10. 真首核上的十二条首提升末行

把参考完整列写成 $w^{13}A_\Phi(w)e_3(Q_\Phi a_p\epsilon)$，
$A_\Phi$ 包括全部公共普通单位和固定 $P_{134}$。对同一真实首核向量 $P$ 令
$$
W_i(P)=\sum_\Phi P_\Phi Q_\Phi^iA_\Phi(w).
\tag{39}
$$
由原整个 $M$ 的四块，而非相对 $J$，准确有
$$
W_0,W_1,W_2\in w^{s-13}k[[w]],\qquad W_3\in w^\ell k[[w]].
\tag{40}
$$
定义
$$
d_{j,i}=[w^{s-13+i}]W_j\quad(j=1,2),\qquad
d_{3,i}=[w^{\ell+i}]W_3,\qquad0\le i\le3,
$$
并令负下标为零。则固定真实首余核中的 Bockstein 变化为
$$
\boxed{
\begin{aligned}
(\beta_1^A-\beta_1^\circ)(P)=\Big[&
\sum_{i=0}^3\sum_{j=0}^3u_jd_{1,i-j}\epsilon w^{s-4+i}\\
&+a_p\sum_{i=0}^3\sum_{j=0}^3u_jd_{2,i-j}\epsilon^2w^{s-4+i}\\
&+\frac{a_p^2}{2}\sum_{i=0}^3\sum_{j=0}^3
u_jd_{3,i-j}\epsilon^3w^{\ell+9+i}\Big].
\end{aligned}
}
\tag{41}
$$
方括号始终商去同一完整 $\operatorname{im}\bar M$。除 (36) 以 $p$ 再模 $p$，只剩一次项。$H_A$ 部分分别由 $w^{13}W_1,w^{13}W_2,w^{13}W_3$ 到达块端点而消失；这是在 (40) 后发生的真实消去，不是预先删高尾。

十二个目标位置为
$$
\boxed{2s-4,\ldots,2s-1;\quad3s-4,\ldots,3s-1;
\quad L_4+9,\ldots,L_4+12.}
\tag{42}
$$
这些是同一个原 $P$ 的十二个尾响应，未变成十二个自由源或十二个已知非零余核类。后续第二、第三提升须继续使用整个 (36)，尤其其末端四次项。

## 11. 四块真正要求什么幂次接触

这一节给可直接用于后续原强窗的必要且充分首核判据，不宣称已构造相应深类。取同一真实格中的一个约化来源
$$
\bar P=t^rF^4Q,\quad
F(0,1)=0,\quad(\mathcal E_{\rm rel}F)(0,1)Q(0,1)\ne0,
$$
$$
h=\operatorname{ord}_wF(t(w),\bar\vartheta(w))>0.
\tag{43}
$$
各 Euler 阶的准确接触依次为
$$
\operatorname{ord}P_i=r+(4-i)h,\qquad0\le i\le3.
$$
因此 (33) 给
$$
\boxed{\bar P\in\ker\bar J_4
\quad\Longleftrightarrow\quad
r+2h\ge s,\qquad r+h\ge\ell.}
\tag{44}
$$
非零首项系数中的 $4,12,24$ 在当前 $p$ 都是单位；含 $\mathcal E Q$ 的其它项有更高 $F$ 次数，不改变这些阶。

这不是旧 cube 的额外一条免费条件。若用 $t^rF^3Q$，第三个满块已读到阶 $r+h$，故必须 $r+h\ge s$。特别在旧贴边 $r+2h=s$、$h>13$ 时，
$$
r+h+13=s-h+13<s,
\tag{45}
$$
连原 $w^{13}$ 后的第三满块都不能通过。因此若要在这一路径使用四块强窗，真正目标是同源的四次幂候选及其完整首次修正，不是把旧三次候选原样提升。

反之，(44) 只判一个已存在的首核形状。它既不证明全首核都被 $F^4$ 整除，也不证明该候选在相同格内有 $p^2,p^3,p^4$ 提升；原 $M$ 的全部 carry 和修正像仍须支付。旧 R738/R741 的非立方首核范围不会因此消失。

## 12. 真实预算结论与下一项有限对象

后继[全纯幂重数优化](../notes/2026-11-15-general-central-blocks-and-pure-power-multiplicity-budget.md)保留任意m≥N−1的真实长行：固定F^N的量纲不是全部重数最小值。

由 (7)，四源仍在同一个二元函数域及已付归一化中。固定导子、degree66 的型常数和有限坏集只改变固定成本；它们没有自动改善 R418/R473 的复主项、普通饱和主项或惰性全次数范数主项。若仍使用原真正二变量格，严格门仍是
$$
a_I+2b_I<3.
\tag{46}
$$

可以准确说明一个条件性量纲。若已经另行支付同一曲面类 $C$ 上的真实来源格、$F^n$ 候选及全部修正，记 $\kappa_C=C^2$，则
在原已付上同调消失下准确有
$h^0(nC)=(n^2\kappa_C+n\chi_C)/2+1$；
对变动的 $C$，余项须保为 $O(n\chi_C+1)$。
以下只在 $n$ 固定、$\chi_C=o(\kappa_C)$，
且真实 $q$／来源返回的额外成本为 $O_n(b)=o(\kappa_C)$ 时读取主阶；
这些真实来源条件并不由中央条数自动提供。
$n$ 块首核条件的一般形式仍是
$r+2h\ge s$、$r+h\ge\ell$。在贴边 $s\sim2h$、固定低阶成本后，目标主长度是 $2(n-1)h$，对应比率
$$
\frac{n^2}{4(n-1)}\,\kappa_C.
\tag{47}
$$
$n=3,4$ 分别给 $9\kappa_C/8,4\kappa_C/3$。这是已指定 $F^n$ 族的维数量纲，不是“$n$ 条中央零推出该族”的定理；(30)–(31) 已说明为什么仅累加低 jet 独立的倍点来源不能实现这个推论。

本篇新增的确定输入是：原第四中央、完整八权及其实际 Hurwitz 四权化、四个实际高系数的唯一必要解，以及它们对同一个 $M$ 的全部三带和末端四次作用。下一步可直接把 (27) 的真实固定值代入 (36)、(41)，在原来源格检验指定修正像或完整左核。尚未付的是“第四中央使原四块矩阵出现一个可见的坏 Smith 条件／排除全部相容修正”的连接；不以形式 Hensel 可解、任意多曲线或四个函数的条数替代它。

## 13. 公开精确运行与重现

固定多项式和 (24)–(25) 由已公开的
[check-r820-original-four-source-angle-and-jacobian.py](../scripts/check-r820-original-four-source-angle-and-jacobian.py)
从原 differential equation 和四个完整角多项式重建。无参数，Python3、
python-flint0.9.0；不读取保存的输出作为输入，不生成输出文件。

- Source commit：78292df097d9417ffa2aa3fae11cf18013d34025。
- GitHub Actions run：43756861065；job：132942734482。
- Script SHA256：4802d2d36cbd860f6d94421ece1a71993aac5c871c550836fd5ee7f4cabc78aa。
- Stdout：1913 bytes；SHA256：c9eca31eeb4de59d6983db587c0c10be004bb8eefbfc70281195d84ed0d4e3ab。

所有原数学断言及 Fraction 系数类型检查通过。该运行还输出高度五、六的两个非零小式及分子 gcd155648；本篇没有用它们修改 (26)，也没有声称原十三行成本已覆盖改用那些高轴的展开。理论部分的 (13)–(47) 是上文的统一证明，不是有限素数抽样外推。

## 依赖与准确范围

- [R816](R816-original-minus-eleven-rank-two-schwartz-and-degree66-source.md)：$E_{-11}$ 的实际秩至少二、完整局部 Schwartz 与 degree66 来源。
- [R820](R820-original-minus-eleven-full-central-and-selmer-bridges.md)：同一来源普通／惰性的完整中央、原 usual Selmer 和全部 Sha 初级商。
- [R468](R468-third-original-central-row-three-axis-hensel-and-six-carry-interface.md)：共同三来源、原角坐标、完整公共单位及前三块接口。
- [R812](R812-original-same-charge-cancellation-and-complete-source-budget.md)：原倍点与中央重复的全规范；其函数身份在第7节重新显式给出。
- [R602](R602-original-gaussian-hurwitz-integrality-and-next-central-bockstein.md)：全 Hurwitz 代数、严格单调尾界及有限 Gaussian 卷积；本篇以 (16a) 付新来源的适用范围。
- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、[R324](R324-original-u-connection-first-forced-row-and-five-block-smith.md)、[R342](R342-original-gaussian-recalibration-and-miller-adjoint-residue.md)：真实解析半径、有限整性与 Gaussian 重标。
- [R335](R335-full-integral-canonical-conductor-and-exact-relative-source.md)、[R425](R425-complete-two-central-hensel-parameters-and-four-row-schur-interface.md)、[R459](R459-actual-angular-content-and-padded-cubic-first-lift.md)：原 canonical 格、真实 Bockstein 商和不删角含量的接触。
- [R473](R473-three-source-function-field-normalization-and-integral-conductor.md)、[R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)：同一归一化、固定导子及真实全次数预算。
