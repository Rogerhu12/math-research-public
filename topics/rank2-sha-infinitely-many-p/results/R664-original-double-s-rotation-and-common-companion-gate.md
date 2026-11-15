# R664 — 原双 S 观察的完整交域、共同伴随门及同一二阶系数

日期：2026-11-15。**状态：已证明。**

本篇只用原最后两个 sigma 的整数旋转，把 R653 的原 $Y=A+Q$
与另一条真正同曲线观察 $Y_1=A+L$ 放到同一个完整来源上。
两条观察的共同深域具有已定绝对号的正交 $126/10$ 核；
它们的第三共同伴随是 degree $9135$ 的真实 odd 核。
所有第一四输入和原 carry 多项式均保留。

两个 carry 门在该共同域上的差准确沿这个共同伴随。
其交集严格回到 R665 的同一个四输入门，而不是一个只在边际上
相似的新域。本文给完整七条条件来源，证明其中唯一非零总质量
恰读 R665 的 $J_N$；两个门的二阶差为该量的一个显示单位倍。
带 $Y/W$ 的测试必须保持全部七条来源和两个浅补域。
未由这一非零系数给原中央赋非零值。

## 1. 原整数旋转与四条真正的 S 行

保持 R645/R653 的所有原规范：
$$
b=17,\quad\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1 .
$$
当前 ray 已由 R655 定 $\chi_{65}=-1$。
另以 $\eta_A=\chi_{29,p}\in\{1,-1\}$ 表示 R488 的
**实际** whole odd29 标量；不把它与 $\chi_{65}$ 混同。

原物理输入是 $(\xi_1,\xi_2,\xi_3,x,c,d)$，且
$$
\nu_4=-\frac1{84}\mathcal P_{6,C}\nu_\sigma^{\otimes4},
\qquad
\mu_0=\nu_4\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
$$
$$
A=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\quad
Q=c+2d,\quad L=2c-d,\quad Y_0=A+Q .
\tag{1}
$$
$A,Q,L$ 相互正交，范数为 $29,5,5$。其余三个 A 伴随完整保持。

取实际整数矩阵
$$
\mathsf J(\xi_1,\xi_2,\xi_3,x,c,d)
       =(\xi_1,\xi_2,\xi_3,x,d,-c).
$$
原 sigma 为奇函数，故完整测度严格满足
$$
\boxed{\mathsf J_*\mu_0=-\mu_0,\qquad\mathsf J^4=I.}
\tag{2}
$$
$\mathsf J$ 与原 C 平均交换，没有换半特征或周期。
定义
$$
Y_j=Y_0\circ\mathsf J^{-j}
  =(A+Q,\ A+L,\ A-Q,\ A-L)_j,\qquad j=0,1,2,3 .
$$
于是整个边际而不只是中央值为
$$
\boxed{(Y_j)_*\mu_0=(-1)^j\nu_S.}
\tag{3}
$$

固定 R594 的同一个实际正分支 $q_N$，$N\ge1$，并令
$$
q_j=q_N\circ\mathsf J^{-j},\qquad
W_j=W\circ\mathsf J^{-j},\qquad W=A+b_QQ+b_LL,
$$
$$
b_Q=(11+6\omega)/5,\qquad b_L=(2+12\omega)/5.
$$
整个 $\pi_4$ 中性随 (2) 真实运输：
$$
\boxed{
\int q_j\,1_{\{Y_j\ {\rm unit}\}}\langle Y_j\rangle^{d_pu}\,d\mu_0
=(-1)^j\beta^N J_S(u),
}
$$
$$
\boxed{
\int q_j\,1_{\{W_j\ {\rm unit}\}}\langle W_j\rangle^{d_pu}\,d\mu_0
=(-1)^j\beta^N\,6\delta J_T(u).
}
\tag{4}
$$
这里 $q_j$ 与观察同时转置；不是把原 $q_N$ 不动而增加四个零条件。

## 2. 两相邻 S 轴的完整正交框架和绝对核心

以下先取 $j=0,1$。置
$$
\boxed{
R=Y_0+Y_1=2A+Q+L,\qquad
D_{10}=Y_0-Y_1=Q-L,\qquad
\mathcal E=5A-29(Q+L).
}
\tag{5}
$$
其完整 Gram 和换元行列式为
$$
\boxed{
\operatorname{Gram}(R,D_{10},\mathcal E)
=\operatorname{diag}(126,10,9135),\qquad
\det\frac{(R,D_{10},\mathcal E)}{(A,Q,L)}=-126 .
}
\tag{6}
$$
逆换元准确为
$$
A=\frac{\mathcal E+29R}{63},\qquad
Q=\frac{5R-2\mathcal E+63D_{10}}{126},\qquad
L=\frac{5R-2\mathcal E-63D_{10}}{126}.
\tag{7}
$$
当前普通处 $2,3,5,7,29$ 都是单位，故 (6) 是原整物理格的
真实换元，保留其余三个 A 伴随。

三个轴与 C 正交，所以每个原 C 旋转都逐个固定它们。
沿各生成变量的原六 sigma 系数，模二非零数分别为 $2,2,5$。
因此它们分别在标准 even $\mathcal S_{126},\mathcal S_{10}$
与 standard odd $\mathcal S_{9135}$；不存在忽略的 flat twist。

当前完整中心满足
$$
g_\pi\equiv127=1+126\pmod{252},\qquad
g_\pi\equiv11=1+10\pmod{20},\qquad
g_\pi\equiv1\pmod{18270}.
\tag{8}
$$
这些只用原 $g_\pi\equiv3\bmod4$ 以及在 $9,5,7,29$ 上为一，
未增添 ray。

在两个 even 空间，实类 $1+N$ 给整个 Heisenberg 的恒等交织：
$((1+N)^2-1)/N=N+2$ 为偶数，完整中心亦为一。
故 whole 核为标量。令 $\gamma_7=3+\omega$；
真实 $\Theta(3\gamma_7z)\in\mathcal S_{126}$ 是 R316/R471 的
$\Theta$ 单位拉回，实际核心为 $\beta$。
它定标整个 $K_{126}=-I$。
另一个绝对号直接使用已发表 R568 §6 的非零联合锚：
$$
K_{10}=\chi_{65}I=-I.
\tag{9}
$$
不从一个不存在的 norm-five 一变量倍点猜 (9)。

whole odd9135 由 R370 的奇中心规范和 (8) 是某个标量。
这个标量用**同一个完整联合**定出：原 $(A,Q,L)$ 三轴同时深，
系数为
$$
(\eta_A\lambda)\beta^2=\eta_A\lambda^3 .
$$
由 (6)，这就是 $(R,D_{10},\mathcal E)$ 三轴同时深，
共同物理缩放也完全相同。前两个新轴已给 $\beta^2$；
整个 $\mu_0$ 非零，因此最后 whole 标量只能是 $\eta_A$。
得到
$$
\boxed{K_{126}=-I,\qquad K_{10}=-I,\qquad
       K_{9135}^{\rm odd}=\eta_A I.}
\tag{10}
$$

特别对全部 $r,s,e\ge0$ 和保全部六输入的任意连续测试，
$$
\boxed{
\mu_0|_{\{R\in p^r,D_{10}\in p^s,\mathcal E\in p^e\}}
=\beta^{r+s}(\eta_A\lambda)^e
(P_{R,\kappa^r}P_{D_{10},\kappa^s}
 P_{\mathcal E,\kappa^e})_*\mu_0 .
}
\tag{11}
$$
各 $P_{V,t}=I+(t-1)\bar V^tV/N(V)$ 都是完整物理映射；
它们正交而交换。原 C 平均及所有三个 A 伙伴均在此式中。

令
$$
\Gamma_n=\{Y_0,Y_1\in p^n\},\quad t=\kappa^n,\quad
B_n=P_{R,t}P_{D_{10},t}.
$$
因为二是单位，
$$
\boxed{\Gamma_n=\{R,D_{10}\in p^n\},\qquad
\mu_0|_{\Gamma_n}=\lambda^{2n}(B_n)_*\mu_0.}
\tag{12}
$$
这不是把两个非正交 Y 核直接相乘。$B_n$ 同时把两条 Y 乘 $t$
并固定 $\mathcal E$；例如
$$
A B_n=A+(t-1)29R/63,\qquad
Q B_n=tQ+(t-1)\mathcal E/63,\qquad
L B_n=tL+(t-1)\mathcal E/63 .
\tag{13}
$$

## 3. 原同一个 q 在共同域上的完整两个门

仍用原 R594/R645 的
$$
C=(\xi_1-\xi_3+x)/\delta,\quad
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\quad
H_1=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x,
$$
$$
a=-(5+6\omega)/29,\quad b_F=(5+6\omega)/5,\quad
c_F=-3\omega/5,\quad g=3-2\omega .
$$
定义
$$
D_*=D_4-aA,\qquad H=C+D_* .
\tag{14}
$$
$C,D_*,H_1$ 全部与 $A,Q,L$ 正交；但
$\langle D_*,C\rangle=-1$，二者**不**正交。
R665 所支付的 C 移动/三倍覆盖在这里仍完整保留。

原两行是
$$
F=H+aA+b_FQ+c_FL,\qquad
F^{J}:=F\circ\mathsf J^{-1}=H+aA-c_FQ+b_FL.
\tag{15}
$$
$F\perp Y_0$、$F^J\perp Y_1$。
置
$$
h_0=-5-9\omega,\qquad h_1=-5-3\omega,
$$
$$
v_0=\frac{h_0}{315}(34Y_1-29Y_0),\qquad
v_1=\frac{h_1}{315}(34Y_0-29Y_1),
$$
$$
e_0=-\frac{170+117\omega}{9135},\qquad
e_1=-\frac{170+291\omega}{9135}.
\tag{16}
$$
准确正交分解为
$$
F=H+e_0\mathcal E+v_0,\qquad
F^J=H+e_1\mathcal E+v_1 .
$$
所以共同返回后的整权始终使用
$$
F_{i,n}=H+e_i\mathcal E+t v_i,\qquad
G_{i,n}=13H_1+gF_{i,n},
\tag{17}
$$
$$
\boxed{
q_i\circ B_n=
\frac{1_{\{C\ {\rm unit},\,F_{i,n}-C\in p^N\}}}{b\Omega^6}
\widehat P_p\bigl((F_{i,n}-C)/\kappa^N,\ F_{i,n}+13C,\ G_{i,n}\bigr).
}
\tag{18}
$$
这是原全部 $\lambda,\kappa,u_j$ 和九行右逆，不是其模 $p$ 近似。

现在取 $n\ge N$。$t v_i\in p^N$ 使门准确稳定为
$$
\mathcal G_i=\{C\ {\rm unit},\,D_*+e_i\mathcal E\in p^N\}.
\tag{19}
$$
由于
$$
\boxed{e_1-e_0=-2\omega/105\in\mathcal O^\times,}
$$
得到真正的逐点分区
$$
\boxed{
\mathcal G_0\cap\mathcal G_1
=\{C\ {\rm unit},D_*\in p^N,\mathcal E\in p^N\}
=\mathcal H_N\cap\{\mathcal E\in p^N\},
\quad
\mathcal H_N:=\{C\ {\rm unit},D_*\in p^N\},
}
\tag{20}
$$
$$
\boxed{
\mathcal G_i\setminus\mathcal G_{1-i}
=\mathcal G_i\cap\{\mathcal E\notin p^N\}.}
\tag{21}
$$
$\mathcal H_N$ 正是 R665 的原四输入门。
(21) 保留全部 $0\le v_p(\mathcal E)<N$，不是只保单位环带。
在 (20) 上两个原观察 $Y_0,Y_1$ 都仍可为单位；
这与 R645 的 A 门交集会排除其 A 单位观察不同。

$\mathcal E$ 与 $C,D_*,H_1,Y_0,Y_1$ 都正交。
因此 (11) 对共同门的进一步返回完全合法，保住这五条输出。
它会移动 A、Q、L，不能单独宣称它保持原 W。

## 4. 两条原算术总行、交域和全部外部

原全 Y 核随 (2) 共轭给
$$
\mu_0|_{Y_i\in p^n}=\lambda^n(P_{Y_i,(-\kappa)^n})_*\mu_0,
\qquad i=0,1.
$$
令 $Z_i^S=Y_i,\ Z_i^T=W_i$，
$J_S^*=J_S,\ J_T^*=6\delta J_T$，并定义真正的完整总行
$$
\mathcal F_{i,n}^{Z}(u)=
\int_{Y_i\in p^n} q_i\,
1_{\{Z_i^Z P_{Y_i,(-\kappa)^n}^{-1}\ {\rm unit}\}}
\langle Z_i^Z P_{Y_i,(-\kappa)^n}^{-1}\rangle^{d_pu}\,d\mu_0 .
$$
所有逆像仅在其真实整像上使用。由 (4)，
$$
\boxed{\mathcal F_{i,n}^{Z}(u)
=(-1)^i\lambda^n\beta^N J_Z^*(u).}
\tag{22}
$$

以 $\mathcal I_{i,n}^{Z}$ 表示总行在 $\Gamma_n$ 上的部分，
$\mathcal O_{i,n}^{Z}$ 表示原 $\{Y_i\in p^n,Y_{1-i}\notin p^n\}$
上的完整剩余。由 (12)，
$$
\boxed{
\mathcal I_{i,n}^{Z}(u)=\lambda^{2n}
\int(q_i\circ B_n)\,1_{\{z_{i,n}^{Z}\ {\rm unit}\}}
       \langle z_{i,n}^{Z}\rangle^{d_pu}\,d\mu_0 .
}
\tag{23}
$$
原 S 观察是
$$
z_{i,n}^{S}=(-1)^nY_i .
\tag{24}
$$
根单位只可从 principal 权中去掉，不能因此改其它输出。

为保完整 T 观察，置
$$
b_Y=(20+3\omega)/17,\quad
w_0=(-8-18\omega)/315,\quad
w_1=(-4+6\omega)/315,\quad s=(-1)^n .
$$
$W_1=A-b_LQ+b_QL$，且 $w_i=\langle W_i,\mathcal E\rangle/9135$。
原正确的完整转置为
$$
\boxed{
z_{i,n}^{T}
=w_i\mathcal E+t(W_i-w_i\mathcal E)+(s-t)b_YY_i .
}
\tag{25}
$$
因而不能把两个 T 单位 cut 换成裸 Q/L 单位。
(23) 的两个 S 单位 cut 也分别是 $Y_0$、$Y_1$，不自动相同。

完整外部严格满足
$$
\boxed{
\mathcal O_{i,n}^{Z}(u)
=(-1)^i\lambda^n\beta^N J_Z^*(u)-\mathcal I_{i,n}^{Z}(u).
}
\tag{26}
$$
如果只假设原两个中央导数为零，才可于 $u=0$ 得
$(\mathcal O_{i,n}^{Z})'=-(\mathcal I_{i,n}^{Z})'$。
质量同理由原 $J_Z^*(0)=0$ 处理，但共同部分质量不能单独删去。
(20)、(21) 是 (23) 内部的另一真实分区，不能代替 (26) 的外部。

## 5. 同一四输入门的完整七条条件来源

定义同一个原多项式的外部形式参数版本
$$
\boxed{
p_N(z)=\frac1{b\Omega^6}
\widehat P_p(D_*/\kappa^N+z/\kappa^N,\
             H+13C+z,\ 13H_1+gH+gz)
=\sum_{k=0}^{6}z^k p_{k,N}.
}
\tag{27}
$$
$p_{k,N}$ 只依 $C,D_*,H_1$，并且
$p_{k,N}\in p^{-kN}\mathcal O$ 在真实 $\mathcal H_N$ 上。
齐次次数为 $6-k$，全部原 $\lambda,\kappa$ 系数保留。

在原四输入上定义**条件 A 测度**
$$
\boxed{
\Lambda_{k,N}:=
 A_*\bigl(1_{\mathcal H_N}p_{k,N}\,d\nu_4\bigr),\qquad0\le k\le6.
}
\tag{28}
$$
它们不是独立添加的 sigma 输入。对任何完整 $(A,Q,L)$ 测试，
(28) 与原 pair 的张量使用只是原 Fubini 推前，保同一来源。

每条 $\kappa^{kN}\Lambda_{k,N}$ 都是整有界测度。
其沿 A 的完整核心是
$$
\boxed{
\Lambda_{k,N}|_{A\in p^r}
=(\eta_A\lambda)^r[\kappa^r]_*\Lambda_{k,N}.
}
\tag{29}
$$
因为 $\mathcal H_N,p_{k,N}$ 与 A 的正交缩放逐点不变。
所有限制算子都只作用 A 的三个伴随；沿 A 仍是完整
standard odd $\mathcal S_{29}$ 的真实截面，未改 degree 或 flat 特征。
也可用 R665 的完整四轴整数框架与单位减深域逐项看出这一点。

原 $\nu_4$ 在同时 $\mu_6$ 下型为四，而 $p_{k,N}$ 齐次度数为
$6-k$，门 $\mathcal H_N$ 在同一旋转下不变。
因此 $\Lambda_{k,N}$ 的型为 $k-2\bmod6$。
完整总质量只可能在 $k=2$ 非零。
R665 的原 $\ell_0=c_F$ 和其 $J_N$ 恰给
$$
\boxed{
\Lambda_{k,N}(\mathbf Z_p)=
\begin{cases}J_N/c_F^2,&k=2,\\0,&k\ne2.\end{cases}
}
\tag{30}
$$
这是同一四输入的准确恒等，故对独立形式参数 z 有
$$
\boxed{\int_{\mathcal H_N}p_N(z)\,d\nu_4=(J_N/c_F^2)z^2.}
\tag{31}
$$
若 z 之后取 $\mathcal E$，它含 A；带 Y/W 的积分必须用 (28)，
不能把 (31) 的总质量当作条件 A 测度。

(20) 的共同门现在可完全写出。令
$\mathcal C_{i,n}^{Z}$ 为 (23) 在两 carry 门共同部分的积分。
利用 (11) 再把 $\mathcal E$ 深 N 返回，得到
$$
\boxed{
\begin{aligned}
\mathcal C_{i,n}^{Z}(u)
={}&\lambda^{2n}(\eta_A\lambda)^N
\sum_{k=0}^{6}
\int (e_i\kappa^N\mathcal E+t v_i)^k\\
&\quad\cdot1_{\{\zeta_{i,n}^{Z}\ {\rm unit}\}}
\langle\zeta_{i,n}^{Z}\rangle^{d_pu}\,
d(\Lambda_{k,N}(A)\otimes\nu_{\rm pair}(Q,L)).
\end{aligned}
}
\tag{32}
$$
其中
$$
\zeta_{i,n}^{S}=sY_i,\qquad
\zeta_{i,n}^{T}
=w_i\kappa^N\mathcal E+t(W_i-w_i\mathcal E)+(s-t)b_YY_i.
\tag{33}
$$
原 $t v_i$、$\kappa^N\mathcal E$、所有单位 cut 与 log 质量完整保留。
(32) 只有七条真实条件来源；$\nu_{\rm pair}$ 可按 R653 全五项再展开，
但没有先杀不被观察保持的角型。

令 $\mathcal L_{i,n}^{Z}$ 为 (23) 在 (21) 上的部分，则
$$
\boxed{
\mathcal I_{i,n}^{Z}=\mathcal C_{i,n}^{Z}+\mathcal L_{i,n}^{Z},\qquad
\mathcal O_{i,n}^{Z}+\mathcal C_{i,n}^{Z}+\mathcal L_{i,n}^{Z}
=(-1)^i\lambda^n\beta^N J_Z^* .
}
\tag{34}
$$
这是原两个 S/T 全行与共同伴随深域的完整接合，所有浅环带和
原 Y 外部都显示在同一个等式中。

## 6. 原非零 J_N 对两个门的准确二阶返回

R665 已付，在同一原 ray 的相对密度一子族中，
$$
v_p(J_N)=-2N\qquad(N\in4\mathbf Z_{\ge1}),
$$
并由原 $I_{\Sigma_5,-1}\ne0$ 读出同一 T 混合行的真实 L 深支。
本篇没有重复其四次矩计算；(27)–(30) 已逐项识别为同一个系数。

两个新门的实际第二法向差为
$$
\begin{aligned}
[z^2]\int_{\mathcal H_N}
   \{p_N(e_1z)-p_N(e_0z)\}\,d\nu_4
&=\frac{e_1^2-e_0^2}{c_F^2}J_N\\
&=\boxed{\frac{136(1-5\omega)}{345303}\,J_N.}
\end{aligned}
\tag{35}
$$
该固定比例的范数准确为
$$
\frac{2^6\,17^2\,31}{3^{10}\,7^4\,29^2}.
$$
所以它在当前所有好普通素数上为单位，不需新增 ray。
由 (31)，上面整个形式参数差就是 (35) 乘 z²，
不是还漏了其它无权次数。

特别两个真实冻结门不能在这个原四输入平均下逐点或整条抹成同一个门。
但带 Y/W 观察时，(32) 中全部 $\Lambda_{k,N}$ 仍在。
(35) 只付显示的二阶行；它既不是原 $J'_S,J'_T$，也不取消
(34) 的 $\mathcal L$ 或 $\mathcal O$。

R661 的三个实际 Katz 点继续用于 R653 的独立 Q 测试：
$\ell_D,\ell_{Z,1},I_{\Sigma_5,-1}$。
整数旋转 (2) 对它们只搬整个 gate 和同一测试，没有产生第二条
独立的 Katz 非零假设。现在新增的严格接口是 (32) 的完整共同域，
以及 (35) 与 R665 已知负一行使用**相同** $J_N$。
下一步必须在 (34) 与 R665 的原 T 外部/L 浅补偿之间建立真正关系；
不能仅凭这些质量或一个低阶系数收尾。

## 精确文件与来源

- [check-r664-double-s-rotation-and-common-gate.js](../scripts/check-r664-double-s-rotation-and-common-gate.js)
- [check-r664-double-s-rotation-and-common-gate.json](../scripts/check-r664-double-s-rotation-and-common-gate.json)

固定有理 CM 证书核完整整数旋转、所有 Gram/中心/半特征、
全部投影和门差、T 观察转置、同一二阶比例及其范数。
深度全量词、原测度、有限七来源和全部补域由正文证明。

主要依赖：
[R645](R645-original-ya-intersection-and-carry-transpose.md) 的原 Y/A 核和 q；
[R653](R653-original-five-degree-kernel-and-native-rows.md) 的全 S5 pair；
[R568 §6](R568-original-positive-strip-full-cores-and-native-transport.md) 的 whole S10 绝对锚；
[R488](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md) 的原 odd29；
[R655](R655-original-sigma-five-schwartz-and-rank-one-negative-moment.md) 的原负一非零；
[R661](R661-original-odd-five-characters-and-two-logarithmic-rows.md) 的两个 log 行；
[R662](R662-original-annulus-exterior-and-exact-w-compensation.md) 的实际外部补偿；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md) 的同一个完整 $J_N$。
