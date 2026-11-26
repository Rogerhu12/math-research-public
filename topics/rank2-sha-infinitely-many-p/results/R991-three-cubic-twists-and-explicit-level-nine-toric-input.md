# R991 — 保原三次角色的三个实际扭曲与 level9 的局部模输入

日期：2026-11-26。会话：`Astra-rank2-Sha-0b097461-20261127`。

**状态：已证明。** 本篇支付一个新的、具体的局部与几何输入：用
$E_{27}:y^2+y=x^3$ 代替 $E_0:y^2=x^3+1$，原三个
$\lambda_j=\psi_0^3\eta_j^{-1}$ 完全不变；2、3、17 的全部有限 toric
Hom 均非零，并给出实际向量。3 处向量固定一个明确的 level9 模群，
其通用椭圆曲面是下文的 $I_9+I_3$ 曲面，不能随意换成同一纯表示的 K3。
第三个扭曲 $E_{(4)}:y^2=x^3+4$ 虽解除2处阻碍，却在3处有全 Hom 消失。
最高三次 Chow 因子之间另有直接、严格的扭曲下降同构。

这些结论不包含新循环的最高分量 AJ 非零，不把局部 test vector 当成
Euler 系统的初项，也不把新输入认成 R854 的旧 canonical 循环。
第9节明确区分新的最高因子与混合因子。

## 1. 三条曲线、实际同构及全 Hecke 角色

沿 R806、R862、R990 固定
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,
\qquad \delta=1+2\omega=i\sqrt3,
\qquad t^3=2,
$$
并固定原 $H/K$、$[H:K]=18$、三个 $\eta_j$，$j=4,10,16$。
令 $\kappa(\sigma)=\sigma(t)/t$，采用使以下同构在 CM 正特征线上
给出所写角色的同一个 reciprocity 约定。

以下不是仅由 $j=0$ 得到的角色识别。实际同构为
$$
\begin{split}
I_{27}:E_0&\longrightarrow E_{27},&
(x,y)&\longmapsto\left(\frac{t x}{2},\frac{y-1}{2}\right),\\
I_4:E_0&\longrightarrow E_{(4)},&
(x,y)&\longmapsto(t^2x,2y).
\end{split}
\tag{1}
$$
直接代入方程即核定(1)。二者的 Galois 共轭分别为
$[\kappa]I_{27}$、$[\kappa^2]I_4$。在同一 CM 正特征线上的完整角色因而满足
$$
\psi_{27}=\kappa\psi_0,\qquad
\psi_4=\kappa^2\psi_0,\qquad
\boxed{\psi_{27}^3=\psi_4^3=\psi_0^3.}
\tag{2}
$$
所以三个原 $\eta_j$ 均不用改，原 $\lambda_j$ 也不用改。
这里 $E_{(4)}$ 的下标只表示方程常数4，不是 R733 的 $17^4$ 曲线。

$E_{27}$ 的最小判别式是 $-27$，在2处有好约化。为核其3处导子，
作 $x=X-1,y=Y+1$ 得
$$
Y^2+3Y=X^3-3X^2+3X-3.
$$
Tate 算法中 $v_3(a_6)=1$ 给 type II；$v_3(\Delta)=3$，
Ogg 导子公式给 $f_3=3+1-1=3$。故 $N(E_{27})=27$。
其 Hecke 角色导子为 $\delta^2=(3)$，也可不靠方程表唯一刻画：
$$
\psi_{27}((a))=\epsilon(a)^{-1}a,
\qquad a\equiv\epsilon(a)\pmod{3},\qquad \epsilon(a)\in\mu_6.
\tag{3}
$$
$\mathcal O_K/(3)$ 的单位群有六个元素，$\mu_6$ 向它双射；
$K$ 类数为1，故(3)给一个良定义的 type $(1,0)$ 角色且唯一。
单位 $\omega\equiv1\pmod\delta$ 的非平凡值说明导子确为 $\delta^2$。
这支付了 wild 3 部分。

设 $\nu_a$ 为 $\psi_a$ 的 unitary 角色，$a=0,27,4$；
即在理想规范中除以范数的平方根，在 idèle 规范中乘 $|\cdot|^{1/2}$。
由(3)及原 $\psi_0$ 的完整公式，$\kappa$ 的导子恰为
$$
\mathfrak f_\kappa=(2\delta^2).
\tag{4}
$$
2处的角色为 $\epsilon_2^{-1}$，其中 $\epsilon_2$ 是
$\mathbf F_4^\times\simeq\mu_3$ 的指定 Teichmüller 角色；
3处 $\kappa(\omega)=\omega,\kappa(-1)=1,\kappa(\delta)=1$。
最后一个值不是另选的规范：对全局主 idèle $\delta$ 应用乘积公式，
其2处剩余类为1，其余非3有限分量不贡献，便得到该值。

全部相关单位及 uniformizer 数据为
$$
\begin{array}{c|ccc|c}
 &\nu_0&\nu_{27}&\nu_4&\eta_j\\ \hline
\mathcal O_{K,2}^\times&\epsilon_2&1&\epsilon_2^{-1}&\epsilon_2^{-1}\\
2&-1&-1&-1&1\\
\mu_6\subset\mathcal O_{K,3}^\times&u^3&u&u^{-1}&1\\
\delta&i&i&i&-1\\
\mathcal O_{K,17}^\times&1&1&1&\vartheta_{l_j}\\
17&-1&-1&-1&1,
\end{array}
\tag{5}
$$
其中 $l_j=j-9=-5,1,7$，$\vartheta_l(u)=\operatorname{Teich}(u)^{16l}$。
所有未写的主单位值由导子决定，均为平凡；三个17处角色恰有阶18。
特别 $\eta_j$ 在 $\mathbf A_\mathbf Q^\times$ 上平凡。

表(5)的 uniformizer 值可逐个由全局主 idèle 核定。例如
$\nu_{27,\infty}(\delta)=-i$、$\nu_{27,2}(\delta)=1$，给
$\nu_{27,3}(\delta)=i$；主有理 idèle 2 的3处分量为 $-1$，
给 $\nu_{27,2}(2)=-1$。这些值不能被单位表代替。

因此
$$
\begin{array}{c|ccc}
 &\psi_0&\psi_{27}&\psi_4\\ \hline
\mathfrak f&(2\delta)&(\delta^2)&(2\delta^2)\\
N(E)&36&27&108\\
\mathfrak f_{\psi^2}&(2)&(\delta^2)&(2\delta^2)\\
N(\theta(\psi^2))&12&27&108.
\end{array}
\tag{6}
$$
每行导子由(5)的首个非平凡单位层直接读出。
模形式导子用 $|D_K|\mathrm N\mathfrak f$；$E_{(4)}$ 的实际导子108
也与 LMFDB `108.a2` 的方程相符，但这里不以数据库数值代替角色证明。

## 2. 固定 toric 角色及两个真正因子

对 $a=0,27,4$ 定义
$$
\pi_a=\mathrm{AI}_{K/\mathbf Q}(\nu_a^2),\qquad
\chi_{a,j}=\eta_j\nu_a^{-1},\qquad
\alpha_j=\nu_0^3\eta_j^{-1}.
\tag{7}
$$
$\pi_a$ 是 $\theta(\psi_a^2)$ 的 unitary 表示，中心角色为 $\chi_K$；
$\chi_{a,j}|_{\mathbf A_\mathbf Q^\times}=\chi_K$。
在 $K$ 上的 Rankin 参数严格分解为
$$
\left.\pi_a\right|_{W_K}\otimes\chi_{a,j}^{-1}
=\underbrace{\nu_a^3\eta_j^{-1}}_{\alpha_j}
\ \oplus\
\underbrace{\nu_a^{-1}\eta_j^{-1}}_{(\nu_a\eta_j)^{-1}}.
\tag{8}
$$
第一项由(2)就是原 $\lambda_j$ 的 unitary 角色。
另记
$$
\beta_{a,j}=\psi_a\eta_j.
\tag{9}
$$
它不是 R826 中的 $\eta_j^{-2}\psi_0$ 或 $\eta_j^{-7}\psi_0$。
其导子及 weight2 theta level 为
$$
\begin{array}{c|ccc}
a&0&27&4\\ \hline
\mathfrak f_{\beta_{a,j}}&(17\delta)&(34\delta^2)&(34\delta^2)\\
N(\theta(\beta_{a,j}))&2601&31212&31212.
\end{array}
\tag{10}
$$
在代数中心坐标下，(8)的 $L$ 函数分解是
$L(\lambda_j,s)L(\beta_{a,j},s-1)$；其中心分别是2与1。
第二项的 inverse/conjugate 在 $K/\mathbf Q$ 上给同一个诱导 $L$ 函数，
但在 CM 定向线和 AJ 目标上仍须保留(8)写明的方向。

## 3. 3处 Tunnell–Saito 判据的实际 Gauss 和

本节用 $F=\mathbf Q_3$、$L=K_3$，$\delta^2=-3$。
取 conductor0 的加性角色 $\Psi_F$，满足 $\Psi_F(1/3)=\omega$，
$\Psi_L=\Psi_F\circ\operatorname{Tr}_{L/F}$；different 指数为1。
对 conductor 指数 $c>0$ 的 unitary 角色 $\rho$，Tate 公式为
$$
\epsilon(\rho,\Psi_L)
=\rho(\delta^{c+1})3^{-c/2}
\sum_{u\in(\mathcal O_L/\delta^c)^\times}
\rho(u)^{-1}\Psi_L(u/\delta^{c+1}).
\tag{11}
$$
所有下述角色在 $-1$ 上为 $-1$。

对原 $\alpha_j$，导子指数是1，单位型 $u^3$，$\alpha_j(\delta)=i$。
取代表 $1,-1$，和为 $\omega-\omega^2=\delta$，所以
$$
\epsilon(\alpha_j,\Psi_L)=-i.
\tag{12}
$$
对 $\gamma_{a,j}=(\nu_a\eta_j)^{-1}$，$\gamma_{a,j}(\delta)=i$。
$a=0$ 时仍是上述 conductor1 计算，得 $-i$。
$a=27,4$ 时 conductor2，分别有单位型 $u^{-1},u$。
用完整的六个代表 $\mu_6$，加性值为
$$
\begin{array}{c|rrrrrr}
u&1&-1&\omega&-\omega&\omega^2&-\omega^2\\ \hline
\Psi_L(u/\delta^3)&1&1&\omega^2&\omega&\omega&\omega^2.
\end{array}
\tag{13}
$$
这是 $1/\delta^3=\delta/9$ 和实际 trace 的直接计算。
于是
$$
\sum_{u\in\mu_6}u\Psi_L(u/\delta^3)=3,
\qquad
\sum_{u\in\mu_6}u^{-1}\Psi_L(u/\delta^3)=-3.
\tag{14}
$$
由 $\gamma(\delta^3)=i^3=-i$，得到
$$
\epsilon(\gamma_{0,j})=-i,\qquad
\epsilon(\gamma_{27,j})=-i,\qquad
\epsilon(\gamma_{4,j})=+i.
\tag{15}
$$
这些等式不依赖 $j$，因为 $\eta_j$ 的3处数据相同。

本篇采用的 Tunnell–Saito 判据是
$$
\dim\operatorname{Hom}_{L^\times}(\pi_{a,3},\chi_{a,j,3})=1
\quad\Longleftrightarrow\quad
\epsilon\bigl(\left.\pi_{a,3}\right|_{W_L}\otimes
\chi_{a,j,3}^{-1},\Psi_L\bigr)=\chi_{a,j,3}(-1).
\tag{16}
$$
其另一侧给除四元数代数上的 Jacquet–Langlands transfer。
参见 [CST, §3, pp.2554–2555]：其 $\Omega=\chi^{-1}$，
$\epsilon_F=\chi_{L/F}(-1)\epsilon_L$，代入即为(16)。
这里引用的是全局部表示定理，不把该文的 weight2 全局 Gross–Zagier
公式直接用到当前 weight3 循环。

$\chi_{a,j,3}(-1)=-1$。由(12)、(15)，左侧 epsilon 分别为
$-1,-1,+1$，故
$$
\dim\operatorname{Hom}_{K_3^\times}(\pi_{a,3},\chi_{a,j,3})
=\begin{cases}1,&a=0,27,\\0,&a=4.\end{cases}
\tag{17}
$$
这也说明 $\eta_j(\delta)=-1$ 不能省略：若只保留其单位型而把
该 uniformizer 值换成 $+1$，本计算的匹配会被翻转。

## 4. $E_{27}$ 在3处的实际紧诱导向量

下面构造(17)中 $a=27$ 的非零向量，同时核它确属 $\pi_{27,3}$。
令
$$
I^+=\left\{\begin{pmatrix}a&b\\3c&d\end{pmatrix}:
a,d\in1+3\mathbf Z_3,\ b,c\in\mathbf Z_3\right\},
\qquad
\theta\left(\begin{pmatrix}a&b\\3c&d\end{pmatrix}\right)=\omega^{b-c}.
\tag{18}
$$
在基 $(1,\delta/3)$ 下把 $L^\times$ 嵌入 $G=\mathrm{GL}_2(F)$，于是
$$
\delta=\begin{pmatrix}0&-1\\3&0\end{pmatrix},\qquad
J=F^\times I^+\ \sqcup\ \delta F^\times I^+.
\tag{19}
$$
定义 $\Lambda:J\to\mathbf C^\times$：在中心取 $\chi_K$，
在 $I^+$ 取 $\theta$，并令 $\Lambda(\delta)=i$。
因 $\delta^2=-3$ 且 $\chi_{K,3}(-3)=-1$，此定义兼容。
共轭 $\delta$ 保持(18)，所以确为角色。

$L^\times\subset J$。对 $b\in\mathbf Z_3$，
$$
1+b\delta=\begin{pmatrix}1&-b\\3b&1\end{pmatrix},
\quad \Lambda(1+b\delta)=\omega^b
=\chi_{27,j,3}(1+b\delta).
$$
最后一个等号用 $\nu_{27}(1+b\delta)=\omega^{-b}$；
再核 $\chi_{27,j,3}(\delta)=i$ 和中心，得到
$$
\Lambda|_{L^\times}=\chi_{27,j,3}.
\tag{20}
$$

必须排除“构造了另一个 conductor3 表示”的可能。
[Kn, §5.2, Proposition5.3] 把全部 conductor3、tame 中心角色的
supercuspidal 表示写成 simple compact induction。其参数为
$r=\pm1$、$g_r=\left(\begin{smallmatrix}0&r\\3&0\end{smallmatrix}\right)$，
$\theta_r=\omega^{b+rc}$ 及 $\zeta^2=\chi_K(3r)$。
$\pi_{27,3}=\operatorname{AI}(\nu_{27,3}^2)$ 是 conductor3 的
supercuspidal，且有自扭曲 $\chi_{K,3}\circ\det$。
该扭曲在 $I^+$ 上平凡，在 $g_r$ 上为 $\chi_K(-3r)$。
$r=+1$ 时它把 $\zeta$ 变成 $-\zeta$，这两个紧诱导不等价；
$r=-1$ 时保持 $\zeta$。所以实际参数必须是 $r=-1$，只余
$\zeta=\pm i$。

余下正负用完整 Mackey 计算固定，不借用未统一的 epsilon 规范。
令 $J^{\rm full}$ 为标准无向边的稳定子，即由中心、Iwahori 及
$\delta$ 生成的群。$J$ 在其中指数2，另一陪集取
$h=\operatorname{diag}(-1,1)$。
在 Bruhat–Tits 树上 $L^\times/F^\times$ 固定该无向边并交换两端，
且在距该边 $n\ge1$ 的边上传递：稳定子是
$\mathbf Z_3^\times(1+3^n\mathcal O_L)$，其指数 $2\cdot3^n$
正好是该层边数。这也可从 $a+b\delta$ 对两个格子的作用直接核出。
因此 $L^\times\backslash G/J$ 的完整代表为
$$
g_n=\operatorname{diag}(3^n,1),\quad g_nh,\qquad n\ge0.
\tag{21}
$$
当 $n\ge1$，取 $u_n=1+3^n\delta$。它在 toric 角色上的值为1，而
$$
g_n^{-1}u_ng_n=
\begin{pmatrix}1&-1\\3^{2n+1}&1\end{pmatrix}
$$
在 $\theta$ 上为 $\omega^{-1}\ne1$；再共轭 $h$ 得 $\omega\ne1$。
故这些所有 Mackey 项都为零。$n=0$ 的 $h$ 项把单位型变成逆型，
也不匹配；单位陪集则恰在 $\zeta=i$ 时匹配(20)。
(17)已经给实际 $\pi_{27,3}$ 的 Hom 维数1，所以
$$
\boxed{\pi_{27,3}\simeq\mathrm{c\!-!Ind}_{J}^{G}\Lambda.}
\tag{22}
$$
取右平移模型，实际 test vector 为
$$
v_3(g)=\begin{cases}\Lambda(g),&g\in J,\\0,&g\notin J.\end{cases}
\tag{23}
$$
它是非零 $\chi_{27,j,3}$ 特征向量。由于 torus 模中心紧且 Hom
维数为1，非零 toric functional 在(23)上非零。
上述证明包括所有平移；特别不是只试一个 newvector 后猜 Hom。

## 5. 2、17处向量与第三扭曲的准确界限

先考虑 $a=27$。在 $q=2,17$，$\pi_{27,q}$ 是不可约的 unramified
principal series，$\chi_{27,j,q}$ 有 conductor1。令
$K(q)=\ker(\mathrm{GL}_2(\mathbf Z_q)\to\mathrm{GL}_2(\mathbf F_q))$。
该 principal series 的 $K(q)$-不变量是
$\mathbf P^1(\mathbf F_q)$ 上的函数空间。
非裂 torus
$$
C_{q+1}=\mathbf F_{q^2}^\times/\mathbf F_q^\times
$$
在这 $q+1$ 个点上单纯传递。若 $e_x$ 为点基，作用约定为
$t e_x=e_{tx}$，则
$$
v_{q,j}=\sum_{t\in C_{q+1}}\chi_{27,j,q}(t)^{-1}e_{t\infty}
\tag{24}
$$
是实际非零 $\chi_{27,j,q}$ 特征向量。uniformizer $q$ 是中心，
$\chi_{27,j,q}(q)=-1=\omega_{\pi_{27,q}}(q)$，故整个 torus 兼容。
紧 torus 的重数为1，再给 toric functional 在(24)上非零。

特别2处必须取三个循环二阶子群的带权组合，17处取十八个循环
十七阶子群的带权组合。原 spherical 向量对这两个 ramified
toric 角色的周期为零；不能把它当成(24)。
在几何模问题上，可先加 full34 level，再用真实 degree34 商同源
$$
E\longrightarrow E/(C_2+C_{17})
\tag{25}
$$
和(24)的系数形成对应。由于 $34$ 素于9，完整9级结构可沿该同源
运输。先保留完整级结构再忘至第6节的 $\Gamma$，给实际代数对应，
不需要先假设一个高层 Chow 的抽象 $f$-isotypic projector。
两个局部权重及所有 conjugate 均必须保留。

对 $a=4$，表(5)给 $\chi_{4,j,2}|_{\mathcal O_{K,2}^\times}=1$，
但 $\pi_{4,2}$ 仍是 depth-zero supercuspidal：其残余 inducing
角色是非平凡 cubic，有限 $\mathrm{GL}_2(\mathbf F_2)=S_3$
型为 sign。sign 在 $\mathbf F_4^\times=C_3$ 上平凡，中心值又兼容，
所以支撑在 $\mathbf Q_2^\times\mathrm{GL}_2(\mathbf Z_2)$ 的
compact-type 向量确有非零 toric functional。
这正好解除 R990 的2处阻碍。

然而(17)已证明同一个 $a=4$ 在3处的全 Hom 为零。
因此它把阻碍移到3，不能单凭2处成功换成 level108 模曲面并宣布
新 CM 图有用。若走该输入，须使用3处除代数的另一种全球几何来源。
所有其他有限位的 Hom 均匹配：17处由(24)同样的有限域模型；
其余非分歧位用 unramified toric 向量，split 位用 Kirillov 模型。
合并 R990 与(17)、(24)，得到
$$
\begin{array}{c|ccc}
\dim\operatorname{Hom}_{K_v^\times}(\pi_{a,v},\chi_{a,j,v})
&a=0&a=27&a=4\\ \hline
v=2&0&1&1\\
v=3&1&1&0\\
v=17&1&1&1\\
\text{其余有限 }v&1&1&1.
\end{array}
\tag{26}
$$

## 6. 3处向量固定的真实模群与 $I_9+I_3$ 曲面

(18)在 $\Gamma_1(3)$ 上的核是
$$
\Gamma=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_1(3):
b-c/3\equiv0\pmod3\right\}.
\tag{27}
$$
映射 $\Gamma_1(3)\to\mathbf Z/3\mathbf Z$，$g\mapsto b-c/3$
是群同态；其在 $T$ 与 $ST^3S^{-1}$ 上均为1，所以满射。
$[\mathrm{SL}_2(\mathbf Z):\Gamma]=24$，$-I\notin\Gamma$，
PSL 指数12，且 $\Gamma(9)\subset\Gamma$。

它没有 elliptic stabilizer。order2 已被 $\Gamma_1(3)$ 排除；
若 trace$=-1$、$a=1+3A,d=1+3D,c=3C$，则
$A+D=-1$ 和 det$=1$ 给 $bC\equiv-1\pmod3$；
(27)又给 $b=C$，与 $b^2=-1$ 在 $\mathbf F_3$ 中无解矛盾。
两个 cusp 宽度分别为3、9；对应三个分歧点的度3 cover
在两个 cusp 与原 order3 elliptic 点均全分歧，基曲线 genus1。
所有抛物 lift 都是正的，因为 trace$=-2$ 不满足
$a=d=1\pmod3$。所以通用极小曲面的纤维是 $I_3,I_9$，而非
由错误负 lift 产生的 starred 纤维。

一个具体模型是
$$
B:\ v^3=t(1-27t),\qquad
\mathscr S:\ y^2+xy+t y=x^3\quad\text{over }B.
\tag{28}
$$
原 Tate3 曲面在 $t=0,1/27,\infty$ 的纤维分别为
$I_3,I_1,IV^*$；(28)在三点全分歧，极小化后分别为
$I_9,I_3,$ smooth。基曲线有明确的有理同构
$$
X=-12v,\qquad Y=4-216t,\qquad Y^2=X^3+16,
\tag{29}
$$
再由 $X=4x,Y=8y+4$ 识别为 $E_{27}$。

为固定 cover 的常数，而非只固定三个分支点，令
$$
h=\left(\frac{\eta(\tau)}{\eta(3\tau)}\right)^{12},\qquad
u=729/h,\qquad t=\frac1{u+27}.
$$
则
$$
j=\frac{(u+27)(u+3)^3}{u}
=\frac{(1-24t)^3}{t^3(1-27t)},\qquad
v^3=\frac{u}{(u+27)^2}=q+\cdots.
\tag{30}
$$
选择 $v=q^{1/3}+\cdots$ 的首项1，便固定(28)的三次 cover；
其三个局部 monodromy 均为 $\omega$，正是(27)的字符。
Tate3 在宽度1的 Q-cusp 为非裂 multiplicative；其 splitting field
是 $K$，与这里固定的 CM 域相同，不产生一个未记载的 $K$-twist。

由 $e=12$、$g(B)=1$ 得 $\chi(\mathcal O_{\mathscr S})=1$、
$p_g=q=1$、$h^{1,1}=12$。零截面、纤维、$I_9$ 与 $I_3$ 的非恒等
分量已经给 $2+8+2=12$ 个独立 NS 类，所以
$$
\rho(\mathscr S)=12,\qquad \operatorname{rank}T(\mathscr S)=2,
\qquad\operatorname{rank}MW(\mathscr S)=0.
\tag{31}
$$
这就是 [GZ, Proposition4.9、Propositions11.1–11.2] 的极限曲面；
其 Remark5.6 还给实际 $MW_{\rm tors}=\mathbf Z/3\mathbf Z$、
NS 判别式绝对值3。

$S_3(\Gamma)$ 的维数等于 $p_g=1$。
(22)的局部向量与其余地方的 spherical 向量给
$\theta(\psi_{27}^2)$ 的一条非零 $\Gamma$-形式，故这唯一的 cusp
summand 的 étale 实现是
$$
T_\ell(\mathscr S)\simeq
\operatorname{Ind}_{G_K}^{G_\mathbf Q}\widehat{\psi_{27}^2}_\ell
\tag{32}
$$
（或限制到 $K$ 后两条共轭 CM 线）。这里使用模曲面
$H^1$-局部系数的标准 Betti–étale 实现；(30)固定了该模模型的下降。
此处(32)只声明纯实现，并不声明 $t_2(\mathscr S)$ 与 K3 的 Chow 同构。

在固定高 level cover 上，取 $E_{27}$ 的带级 CM 点、实际(25)，
以及从 $E_{27}$ 到相应纤维的实际同源 $\varphi$。
图 $Q\mapsto(\varphi(Q),Q)$ 在
$\mathscr S\times E_{27}$ 上给 codimension2 循环；应用实际
$\pi_2^{\rm tr}\otimes\pi_1$ 后同调为零，因为目标 Künneth 部分在
$H^3$，不在循环类的 $H^4$。再作原 finite-character trace/projector
就得到一个严格定义的新循环来源。具体级点域、所有 trace 及(24)
权重必须保留，不能把全部级结构先平均成 spherical 向量。
本构造目前没有声称其 AJ 非零。

## 7. 最高三次因子的严格 Chow 扭曲运输

这一部分完全不需要第6节曲面的 Chow 比较。
对 $E=E_0,E_{27},E_{(4)}$ 取原点 $O$ 并定义实际
$\pi_1=\Delta-E\times O-O\times E$。
令 $R=[\omega]\times[\omega]\times[\omega]$，定义
$$
\Pi_E=\pi_1^{\otimes3}\frac{1+R+R^2}{3}.
\tag{33}
$$
它在 Chow 层是幂等元，realization 恰为最高 $(3,0)$ 与共轭 $(0,3)$
两条线；需要单独正线时再用原 $e_+^{\otimes3}$。
因为 $R\Pi_E=\Pi_E$，在 $K'=K(t)$ 上
$$
G_a=\Pi_{E_a}\,\Gamma_{I_a^{\times3}}\,\Pi_{E_0}
\tag{34}
$$
被 $\operatorname{Gal}(K'/K)$ 在 Chow 群中逐项固定：
Galois 共轭(1)所多出的对角 $\mu_3$ 作用被(33)严格消去。
于是
$$
C_a=\frac13\operatorname{Cor}_{K'/K}G_a
\tag{35}
$$
定义于 $K$。用逆同构的图同样定义 $D_a$。
限制到 $K'$ 后，$D_aC_a$ 与 $C_aD_a$ 就是对应的 $\Pi$。
有理 Chow 群上 $\operatorname{Cor}\operatorname{Res}=3$，故
restriction 单射，得到严格等式
$$
D_aC_a=1_{(E_0^3,\Pi_{E_0})},\qquad
C_aD_a=1_{(E_a^3,\Pi_{E_a})}.
\tag{36}
$$
这是真正的双向 Chow 同构，不使用一般 realization 的保真性或
nilpotence 来猜逆。

微分规范也可直接核定。用
$\varpi_0=dx/(2y)$、$\varpi_{27}=dx/(2y+1)$、
$\varpi_4=dx/(2y)$，(1)给
$$
I_{27}^*\varpi_{27}=t\varpi_0,\qquad
I_4^*\varpi_4=t^{-1}\varpi_0.
$$
所以在最高三次微分上
$$
C_{27}^*(\varpi_{27}^{\otimes3})=2\varpi_0^{\otimes3},\qquad
C_4^*(\varpi_4^{\otimes3})=\tfrac12\varpi_0^{\otimes3}.
\tag{37}
$$
与 $[\omega]$ 交换保证原 CM 正线保持。对应定义于 $K$，故与原
$H/K$ 的 restriction、corestriction、$e_{\eta_j}$ 以及所有
étale AJ 映射交换。codimension2 的 AJ 目标使用 **$H^3(2)$**；
不能遗漏 Tate twist，或把用于 Hodge 比较的 $H^3(1)$ 写成 AJ 目标。

对每个 $p\ne2,3$，(1)及(33)–(36)还在一个有限不分歧于 good-$p$
的模型上给互逆的整格比较；清除 projector 的固定分母即可。
因而在全部但有限多个 $p$ 上，它是保持原 finite/ordinary local
conditions 的整比较。若要同时保留 $e_{\eta_j}$，另外清除18的
分母；仍只排除2、3。没有新增依赖 $p$ 的任意标量或不同 $\eta$。

## 8. 新 Euler 系统所需的运输比旧循环识别更弱

若新的构造直接给
$$
c_{a,m,p}\in H^1(F_m,T_{a,p})
$$
且 $T_{a,p}$ 的完整 $G_K$ 作用就是原
$\widehat\lambda_j(2)$ 的固定整格，则可经(2)、(36)的比较运输。
group cohomology 的自然性给 restriction/corestriction 与 Euler
多项式的全部交换关系；local conditions 的自然性给未分歧、
Bloch–Kato $f$ 以及固定 CM 方向的 ordinary 条件交换。
非零及初始类的任何已证局部非零也在同构下保持。

因此为了给原表示一个**新的** Euler 系统，逻辑上不必先证明
$t_2(\mathscr S)$ 的 Chow 逆，更不必把新循环等同于旧 canonical。
但“完整 $G_K$ 模同构”在这里必须是带全部有限角色、整格与 local
conditions 的同构，不能只凭无穷型相同。并且一个一般新几何族
没有自动附带 Euler norm relations、初项非零或所需 reciprocity。
本篇尚未提供这些缺少的输入；(23)、(24)的非零仅是局部表示中的非零。

## 9. 无穷处、完整 root 与最高/混合分量

在无穷处 $\pi_a$ 是 weight3 discrete series。
$\mathbf C^\times/\mathbf R^\times$ 上 $\chi_{a,j}$ 的角权绝对值为1，
而该 discrete series 的紧型权重为 $\pm3,\pm5,\ldots$。
所以
$$
\operatorname{Hom}_{\mathbf C^\times}(\pi_{a,\infty},\chi_{a,j,\infty})=0.
\tag{38}
$$
除代数 $\mathbf H^\times$ 上的 transfer 才包含角权 $\pm1$。
这一项对三个扭曲都相同，不能因有限处(26)全为1而声称全 toric
period 非零。

为避免把不同局部加性规范拼在一起，本段用一个明确的全局标准：
$\Psi_{\mathbf Q,\infty}(x)=e^{2\pi i x}$，有限处取
$e^{-2\pi i\{x\}_q}$，再复合 $K/\mathbf Q$ 的 trace。
这在3处是第3节角色的逆，因此(12)、(15)每个单角色 epsilon
都乘其 $(-1)$ 值 $-1$；两因子的乘积及(16)不变。

在2处，非平凡 cubic 的实际 $\mathbf F_4$ Gauss 和为2：
trace0的非零元素为1，其余两个加性值为 $-1$，故
$1-\omega-\omega^2=2$。乘 uniformizer 值 $-1$ 后 epsilon 为 $-1$；
未分歧的 $\beta_{0,j,2}$ 则为1。
在17处，对任一原 odd 指数 $\vartheta_{l_j}$，沿 trace 纤维求和给
$17\vartheta_{l_j}(\delta)=-17$，乘 uniformizer $-1$ 后为 $+1$。
在3处应用(11)–(14)及上述加性反转；无穷处取 $i^{|m|}$。
因此完整表为
$$
\begin{array}{c|rrrr|r}
 &2&3&17&\infty&W\\ \hline
\lambda_j&-1&+i&+1&-i&-1\\
\beta_{0,j}&+1&+i&+1&+i&-1\\
\beta_{27,j}&-1&+i&+1&+i&+1\\
\beta_{4,j}&-1&-i&+1&+i&-1.
\end{array}
\tag{39}
$$
局部表的分配依赖加性角色；全局 root 和(26)不依赖。
这里第一行与 R806/R826 的原全局 $W(\lambda_j)=-1$ 一致。
相应的 Rankin 全局 root 依次为
$$
W(\pi_{0,K}\otimes\chi_{0,j}^{-1})=+1,
\quad W(\pi_{27,K}\otimes\chi_{27,j}^{-1})=-1,
\quad W(\pi_{4,K}\otimes\chi_{4,j}^{-1})=+1.
\tag{40}
$$
这与有限处不匹配集合分别为 $\{2\},\varnothing,\{3\}$，再加
共同的无穷处不匹配完全一致。

对 $a=27$，原 $L'(\lambda_j,2)\ne0$ 已由 R818 支付；
但新 $L(\beta_{27,j},1)\ne0$ **尚未支付**。root 为 $+1$ 不能代替
该结论。如果以后支付其非零，(8)才给该 Rankin 复解析秩为1。
而一个全 Rankin AJ 类仍必须应用实际最高 projector，或先证明
混合因子的相应 Selmer 为零，才能得到原 $\lambda_j$ 分量非零。
不能从一条总类非零反推它在每个 summand 非零。

若采用 Schütt 的具体 K3
$$
X:\ y^2+s^2xy=x^3+2sx^2+s^2x,
\tag{41}
$$
[Sch, §2, Proposition3.1] 给其 $T$ 对应同一 weight3 level27 CM
新形式；原始方程来自 rational Tate4 曲面经 $z=s^3$ 的 base change。
然而(41)的纤维模结构并非(27)的通用模曲面。
单凭两个 $T_\ell$ 相同，不能把(23)、(24)的新 CM 图/AJ 放到(41)
上；须实际对应或另一个已证 Euler 系统输入。
本篇仅把这两个可选择的新方向定位到准确的角色与局部型，
没有把纯比较当成混合循环比较。

同一曲面的进一步实际几何已记入
[I9/I3 对应范围注](../notes/2026-11-27-congruence-i9-i3-surface-and-correspondence-scope.md)：
所有有限自同构群商均不是 K3；真实三同源对应满足 $F^2=[-3]$，
不是可直接取商的对合。这些结论排除特定比较方法，不排除一般代数对应
或第8节所述直接运输新 Euler 系统的路径。

## 10. 已付范围与后继输入

本篇已付：(1)–(6)的三个全角色；(11)–(26)的全部有限 toric 型与
实际向量；(27)–(32)的真实模群、方程、纯实现；(33)–(37)的最高
三次 Chow 双向运输；(38)–(40)的无穷处与完整 factor/root。

仍需实际提供的是新类的原 $\lambda_j$ 最高投影及其跨 $p$ 非零，
或能直接给相同完整表示的另一套 Euler 系统和 reciprocity。
若走第6节曲面与第9节 K3 的几何比较，其具体 Chow 对应也尚未给出。
这些未付事项不会被“相同 CM motive”、局部 Hom 维数1、root 为正，
或固定7993处旧 canonical 类的非零替代。

## 文献与原结论

- [CST] Li Cai, Jie Shu, Ye Tian, *Explicit Gross–Zagier and Waldspurger formulae*,
  Algebra & Number Theory **8** (2014), 2523–2572，§3 pp.2554–2555：
  [原刊 PDF](https://msp.org/ant/2014/8-10/ant-v8-n10-p.pdf)。本篇只用其
  局部 Tunnell–Saito 判据及 test-vector 术语，不套用其 weight2 全局结论。
- [Kn] Andrew Knightly, *Counting locally supercuspidal newforms*,
  Essential Number Theory **4** (2025), 349–438，§5.1–5.2，特别
  Proposition5.3：[原刊](https://msp.org/ent/2025/4-2/p03.xhtml)，
  DOI `10.2140/ent.2025.4.349`。§5.1 包括 residue characteristic2；
  §5.2 的参数和紧诱导用于(22)，没有混用该文的 root-number 加性规范。
- [GZ] François Greer, Yilong Zhang, *Elliptic-elliptic surfaces and the Hesse pencil*,
  2024，Proposition4.9、Remark5.6、Propositions11.1–11.2：
  [arXiv:2409.18927](https://arxiv.org/abs/2409.18927)。
- [Sch] Matthias Schütt, *Arithmetic of a singular K3 surface*,
  Michigan Mathematical Journal **56** (2008), 513–527，§2、Proposition3.1：
  [arXiv:math/0605560](https://arxiv.org/abs/math/0605560)。
- J. Tate, *Fourier analysis in number fields and Hecke's zeta-functions*,
  in Cassels–Fröhlich, *Algebraic Number Theory* (1967)，§3：局部 epsilon
  的有限 Gauss 和公式；J. Silverman, *Advanced Topics in the Arithmetic of
  Elliptic Curves* (1994)，ChapterII 的 CM 角色及 ChapterIV 的 Tate 算法。
- R806、R817–R818、R826、R854、R862、R988、R990：只调用已登记的完整
  原角色、旧 canonical 检测、原复导数及实际 Chow 结论，不重跑旧计算。
