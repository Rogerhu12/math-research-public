# R702 — 四十五条真实中性测试、完整四挠几何与 E 深门的三态算术返回

日期：2026-11-15。**状态：已证明。**

本文在 R693 的同一个原六支 carry 家族内加入十六条十二次中性测试。
所得新测试 $q_N^{(702)}$ 同时满足：两份冻结来源为 S、零，cd 端点
为 S，未缩放原 W 端点为 $6\delta T$，原二阶系数规范为一；
原 W-core 第二态的**整个第一 $2Y$ 来源**准确为
$\omega^2S(2z)/2+S_{\rm new}(z)$。

这使同一真实 E 深门的三个完整 Y 来源全部落在两条已识别秩二线内，
三个 W 来源仍是原 T 的倍数。三原中央零因此合法传到该门上所有
四轴核心词的完整归一 Y、W 观察，不再需要先在返回态上另作 CM 投影。
原 E 浅门的第二态外谱、不同词的物理逆像、全部 log 质量和 T 补项
仍保留；本文没有据一个深支非零宣布主目标完成。

公开计算给显示的四十五阶实际测试子式。缺少的八条方程由完整
半周期和四挠除子身份支付，不把辅助模数的左核提升为特征零恒等式。

## 1. 原参数、三态及同一共同隐藏权

保 R693 的原普通射线、周期、坏集与规范：
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad \Omega\in\mathcal O^\times,\quad
N\in4\mathbf Z_{>0},\quad u=\kappa^N.
\tag{1}
$$
本篇只删第7节的固定有限坏集及固定 CM 多项式稀疏坏集；
不改写此前任何射线模数。

原六 sigma 来源含 $-1/84$，原前四输入的总输出为 A：
$$
Y=A+c+2d,\qquad W=A+3\delta c+4d,\qquad
Y_*\mu_0=\nu_S,\quad W_*\mu_0=6\delta\nu_T.
\tag{2}
$$
本文为避免与旧 $L=2c-d$ 混同，记
$$
L_\Delta=\frac{W-Y}{2}=(1+3\omega)c+d,\qquad N(L_\Delta)=8.
\tag{3}
$$
所有本篇共同隐藏方向均与 Y、W 同时 Hermitian 正交，因此也与
$L_\Delta$ 正交。

沿 R638/R692 的真实 canonical W 平移，定义
$$
f_t=\mathsf T^{72}_{W,t}\mu_0,\qquad t\in E[4],
$$
$$
e_0=\mu_0,\quad
e_1=\frac14\sum_{t\in E[4]}f_t-\frac12\sum_{t\in E[2]}f_t,\quad
e_2=-\frac14\sum_{t\in E[4]}f_t,\quad
h_W=e_1+e_2=-\frac12\sum_{t\in E[2]}f_t.
\tag{4}
$$
这些是完整六输入来源，保原覆盖和全部伙伴。
原第一 $2Y$ 的标准空间是 $\mathcal S_{136}$。
R692 第2节的完整二挠投影为
$$
P_{2,Y}=\frac14\sum_{s\in E[2]}\mathsf T_s^{136},\qquad
P_{2,Y}e_0=e_0,\quad P_{2,Y}e_1=P_{2,Y}e_2=h_W/2.
\tag{5}
$$
投影和 (4) 都可与任意真正共同隐藏的有限多项式权交换。
这里仍须把原 C 单位补项作为完整的第二个来源分支保留。

用 $\mathscr U_0,\mathscr U_1,\mathscr B,\mathscr W,\mathfrak j_2$
表示 R693 式(12)–(15) 的**全部实际参数**算子。
其精确定义继续使用
$$
D=F-C,\quad E_c=F+13C,\quad G=13H_1+(3-2\omega)F,
\quad \pi_4=(Y,W,W',G).
\tag{6}
$$
本文将 carry 变量写成 $E_c$，把共同 Y/W 伙伴写成
$$
E_{YW}=(5+6\omega)A-29c-(58+87\omega)d.
\tag{7}
$$
这两个 E 不混同。

端点的完整隐藏权由
$$
H=D_*-\frac{E_{YW}}{29},\quad K=H-\frac{406}{143}D_*,
\quad E_\perp=14C^\perp,\quad
G_{00}=G_\perp-\frac{-789+526\omega}{1596}E_\perp
\tag{8}
$$
和下面两项定义：
$$
\begin{aligned}
\Phi_P={}&P(H,E_\perp+uK,G_\perp+(3-2\omega)uK)\\
&-\eta\lambda
 P(H,\kappa E_\perp+uK,
 G_{00}+\kappa(G_\perp-G_{00})+(3-2\omega)uK),
\qquad \eta\in\{1,-1\}.
\end{aligned}
\tag{9}
$$
所有显示方向都与 Y/W 正交。定义完整第二态端点
$$
\mathscr Q(P)(z)=\int e^{2Yz/\Omega}\Phi_P\,de_1.
\tag{10}
$$
权中的原 $b,\Omega$ 次数归一按第2节，(9) 对各齐次块线性使用。
$\mathscr B,\mathscr W$ 是相同 $\Phi_P$ 在 $e_0$ 上的原 Y、W 来源。

## 2. 十六条新增中性测试与完整 E 单位逆

R590/R594 已付完整 C 平均的真实分离
$$
\mathcal P_6\mu_0=\nu_{B_C}(C)\otimes\nu^\flat,\qquad
m_{B_C}(0)=1,\quad m_{B_C}(i)=0\ (1\le i\le5).
\tag{11}
$$
F、G 和所有 $\pi_4$ 输出均不含这个独立 C。
因此对每个 $d\in6\mathbf Z_{>0}$，
$$
C^iF^jG^{d-i-j},\qquad
1\le i\le5,\quad 0\le j\le d-i,
\tag{12}
$$
完整忘 C 后为零。这是来源级中性，不是有限矩阵的核猜测。

先把 (12) 准确改写为
$$
P_{i,j,d}(D,E_c,G)=
\left(\frac{E_c-D}{14}\right)^i
\left(\frac{E_c+13D}{14}\right)^jG^{d-i-j}.
$$
对整个多项式施 R594 的实际 E 次数逆：
$$
\widehat P_{i,j,d}
=\sum_{a+e+g=d}
\frac{[D^aE_c^eG^g]P_{i,j,d}}{1+\lambda\kappa^e}
D^aE_c^eG^g.
\tag{13}
$$
不得只对其中一个六次因子施逆后再乘 F。

定义完整六支测试
$$
\mathfrak C_N(P_d)=
\frac1{6b^{d/6}\Omega^d}
\sum_{\zeta\in\mu_6}
1_{\{D_\zeta\in p^N,\ E_{c,\zeta}\ {\rm unit}\}}\,
\widehat P_d(D_\zeta/\kappa^N,E_{c,\zeta},G).
\tag{14}
$$
R590 的 entire42/1638 核及半特征不因多项式次数改变。
先用 D 核、再用 (13) 的完整 E 单位逆、最后用 (11)，得
$$
\boxed{(\pi_4)_*(\mathfrak C_N(P_{i,j,d})\mu_0)=0.}
\tag{15}
$$
(15) 保任意完整 $\pi_4$ 测试，所有六支、单位门、$\kappa^{-N}$
和完整 C 深补项都在内。

本文用 R693 已选的二十九条
$G^{6h}\delta q_{j,N}/(b^h\Omega^{6h})$，展平索引为
$$
\mathcal J_G=(0,1,\ldots,22,\ 25,26,\ 36,37,\ 47,48).
\tag{16}
$$
再加以下十六条 $d=12$ 的 (14)：
$$
\boxed{
\begin{array}{c|c|c}
i&j&d-i-j\\ \hline
1&5,6,\ldots,11&11-j\\
2&5,6,\ldots,10&10-j\\
3&5,6,7&9-j
\end{array}}
\tag{17}
$$
所有选列均是真实测试，没有把一个目标归一系数计作测试列。
公开程序虽另生成 B 方向，本文的四十五列完全不使用 B 列。

新测试将是
$$
q_N^{(702)}=q_N+\sum_{\ell=1}^{45}a_{\ell,N,p}h_{\ell,N},
\tag{18}
$$
$q_N$ 为 R594 的旧实际测试，$h_\ell$ 按 (16)、(17) 排列。
最高权次数仍为三十。新增十二次项没有被声称满足旧九条局部网格
质量条件；旧六次测试的 $\mathcal D_n$ 零质量不移给 (18)。
本篇重新支付的是完整来源、$\mathfrak j_2$ 及其真实后续行。

## 3. 全部准周期：半周期块只依原 Y 来源

以下引理适用于 (9) 的任意完整多项式权，主项和 C 深补项分别成立。

先在 $b=-1$ 的规范取 primitive 周期
$\Omega_0,\omega\Omega_0$，正实 $\Omega_0$，并保
$$
\eta_{\omega\Omega_0}=\omega^2\eta_{\Omega_0},\qquad
\delta\eta_{\Omega_0}\Omega_0=2\pi i,\qquad
\chi(m\Omega_0+n\omega\Omega_0)=(-1)^{m+n+mn}.
\tag{19}
$$
向原 $b=17$ 的真实 CM homothety 同时运输周期、准周期及 sigma；
以下的 $\eta_t t$、所有特征和绝对号保持。

写原六个 sigma 的参数为 $Yz+h$。共同隐藏性的完整条件是
$\langle h,Y\rangle=\langle h,W\rangle=0$。
因此
$$
\langle h,L_\Delta\rangle=0,\qquad
h_d=(2+3\omega)h_c.
\tag{20}
$$
这里 h 是全部隐藏变量，不是它的常数项。

对固定代表
$$
t\in\{0,\Omega_0/2,\omega\Omega_0/2,(1+\omega)\Omega_0/2\},
$$
准确有
$$
Wt=Yt+2L_\Delta t .
\tag{21}
$$
右边最后一项是原六 sigma 的整周期向量。
用原
$\sigma(z+\Lambda)=\chi(\Lambda)e^{\eta_\Lambda(z+\Lambda/2)}\sigma(z)$
逐因子相乘，并保 canonical W、Y prefactor，得到
$$
\boxed{
(\mathsf T^{72}_{W,t}\mathcal F)(Yz+h)
=\vartheta_t(\mathsf T^{34}_{Y,t}\mathcal F)(Yz+h),\qquad
\vartheta_t=
\prod_{\nu=1}^{6}\chi(2(L_\Delta)_\nu t)\,
 e^{-3\delta\eta_t t}.
}
\tag{22}
$$
式(22) 右侧的 $\mathsf T_{Y,t}$ 只在原 Y 方向平移。
推导所用数值为
$$
\langle Y,L_\Delta\rangle=-3\omega,\quad
N(L_\Delta)=8,\quad
N(Y)=34,\quad N(W)=72.
$$
z 的交叉指数准确消掉；隐藏指数为
$2\eta_t\langle h,L_\Delta\rangle=0$。
所以 (22) 对每个所需隐藏导数、全部 $u,\kappa$ 和第二个 C 分支都成立。

$t=0$ 时 $\vartheta_t=1$。对三个显示的非零代表，
两个非平凡 sigma 特征都为 $-1$，乘积为一，
$\eta_t t=\eta_{\Omega_0}\Omega_0/4$。
故
$$
\vartheta_t=e^{-3\pi i/2}=i\qquad(t\ne0).
\tag{23}
$$
没有任意选择平方根，也没有用仅模二的 projective 关系定标。

因此存在一个固定算子
$$
\mathcal H(B)=-\frac12\left(B+i\sum_{t\in E[2]\setminus0}
                                  \mathsf T_t^{34}B\right)
$$
使任意共同隐藏权 $\phi$ 满足
$$
Y_*(\phi h_W)=\mathcal H(Y_*(\phi e_0)).
\tag{24}
$$
原 R493 的完整 $h_W=\omega^2T_*\mu_0$、$YT=Y$ 给绝对校准
$\mathcal H(S)=\omega^2S$。
结合 (5)，若 $\mathscr B(P)=S$，便有整条身份
$$
\boxed{
P_{2,Y}\mathscr Q(P)=\frac{\omega^2}{2}S(2z).
}
\tag{25}
$$
这没有假设新权 $\phi$ 被几何 T 固定；(24) 对任意共同隐藏权成立。

## 4. 完整四挠除子来自同一个原 W 来源

对 $z,t\in E[4]$ 的固定 primitive 四分之一周期代表，准确有
$$
\boxed{2Yz+Wt=W(2z+t)-4L_\Delta z.}
\tag{26}
$$
最后一项仍是原六 sigma 的整周期向量。
原隐藏项在准周期指数中为
$-4\eta_z\langle h,L_\Delta\rangle=0$。
更明确地，令
$$
c_{YW}=\langle Y,W\rangle=34-6\omega,\qquad
c_{WL}=\langle W,L_\Delta\rangle=16-3\omega .
$$
带原 W canonical prefactor 的每一支，在该 z 的值等于
$$
\begin{aligned}
&\prod_{\nu=1}^{6}\chi(-4(L_\Delta)_\nu z)\\
&\quad{}\times
\exp\{-\eta_t(2c_{YW}z+36t)
       -4\eta_z(c_{WL}(2z+t)-16z)\}\,
B_W(2z+t).
\end{aligned}
\tag{27}
$$
其中 $B_W=W_*(\phi e_0)$。即使 $2z+t$ 超出所选基本代表，
也使用该实际点和原准周期；重取代表只改变已显示的非零因子。
(27) 保所有原 sigma 特征、$-1/84$ 和隐藏参数，
可先取隐藏导数再求值。

原 T 含 $\sigma(4z)$，所以在整个 $E[4]$ 为零。
若 $\mathscr W(P)=6\delta T$，(27) 的每个真实四挠支分别为零。
用 (4) 的准确十六项系数求和，得
$$
\boxed{\mathscr Q(P)|_{E[4]}=0.}
\tag{28}
$$
这不是把 T 的一个边际零免费提升到隐藏域：
是同一完整隐藏权下逐支的整周期等式。

## 5. 十五维余空间与全部八条依赖

原完整 principal 空间为
$$
\mathcal H_{136}^{(0)}
=\sigma^{136}x^2K[X]_{\le22},\qquad X=x^3,\qquad \dim=23.
$$
令
$$
\mathcal V=\{F\in\mathcal H_{136}^{(0)}:F|_{E[4]}=0\}.
$$
在原点为零使最高第22列消失。三个非零二挠点的 X 均为 $-b$；
十二个 primitive 四挠点的两个 X 值是
$X^2+20bX-8b^2$ 的根。因此
$$
\boxed{
\mathcal V=\sigma^{136}x^2
 (X+b)(X^2+20bX-8b^2)K[X]_{\le18},\qquad \dim\mathcal V=19.
}
\tag{29}
$$
这使用完整函数的零除子，不是某几个采样值的推断。

$E[2]$ 平移保持 $E[4]$，所以 $P_{2,Y}$ 保持 $\mathcal V$。
其不变空间是 $[2]^*\mathcal H_{34}^{(0)}$，原维数六。
在 E4 为零准确等价于原 S34 来源在 E2 为零，即原点质量及非零
二挠轨道值这两个独立条件。因此
$$
\dim P_{2,Y}\mathcal V=4,\qquad
\boxed{\mathcal V_+=\mathcal V\cap\ker P_{2,Y},\quad\dim\mathcal V_+=15.}
\tag{30}
$$
R466 式(8) 的完整 E2 迹和与 CM 算子的交换给
$P_{2,Y}S_{\rm new}=0$；该篇完整因式含 (29) 的三个因子，
故 $S_{\rm new}\in\mathcal V_+$。
原 $S(2z)$ 也在 $\mathcal V$。

由 (25)、(28)，一旦原端点 Y、W 分别为 S、$6\delta T$，
第二态只能且准确地有如下形式：
$$
\mathscr Q(P)=\frac{\omega^2}{2}S(2z)+V_P,\qquad V_P\in\mathcal V_+.
\tag{31}
$$

下面说明为何只需实际四十五阶逆。
R693 已付同一个权的 W 质量等于 Y 质量，
并有完整半周期行
$\ell_{72}(B_W)=3^9\delta\ell_{34}(B_Y)$。
所以两冻结来源、端点 Y/W 及 $\mathfrak j_2$ 合计最多三十维。
若这些旧三十行全为零，(22)、(27) 迫新增第二态在
$\ker P_{2,Y}\cap\mathcal V=\mathcal V_+$，最多十五维。
因此整个联合来源算子的像维数严格至多
$$
\boxed{30+15=45.}
\tag{32}
$$

该论证对全部实际 $\lambda,\kappa,u$ 成立。
目标
$$
\boxed{
\mathscr U_0=S,\quad\mathscr U_1=0,\quad
\mathscr B=S,\quad\mathscr W=6\delta T,\quad
\mathfrak j_2=1,\quad
\mathscr Q=\frac{\omega^2}{2}S(2z)+S_{\rm new}
}
\tag{33}
$$
满足以上所有线性兼容条件。
第6节四十五阶子式非零后，实际像等于这个四十五维兼容空间；
故选择四十五行求解会支付全部五十三行。
这里没有假定任何辅助剩余域的左核行在特征零仍相同。

## 6. 显示的四十五列、四十五行与公开精确子式

前三十行严格取 R693 式(27)：
两冻结 S 的六个 jet、端点 S 的六个 jet、
原 W 的第6至66阶十一个 jet、$\mathfrak j_2$。
Y/W 原质量和缺少的 W 第72阶由已付完整身份补齐。

新增来源先按固定齐次规范写成
$$
\mathscr Q(z)=\sigma_b(z)^{136}x_b(z)^2
 \sum_{j=0}^{22}b^{21-j}q_jX_b(z)^j .
\tag{34}
$$
其 $b=1$ 多项式为 $x^2\sum q_jx^{3j}$。
取以下十五个固定 x 值的完整多项式求值为后十五行：
$$
\boxed{1,\ 3,\ 5,\ 10,\ 11,\ 12,\ 13,\ 18,\ 19,\ 20,\
22,\ 23,\ 25,\ 28,\ 29.}
\tag{35}
$$
它们是完整 theta 系数的固定代数线性泛函，
不把实际椭圆曲线的十五个点值当成未付线丛成员资格。
公开脚本另保二十三个互异 X 点以恢复、核对全部二十三列。

用 (16)、(17) 四十五条真实测试在上述四十五行的矩阵记为
$\mathbb M_{702}(\lambda,\kappa,u,\eta)$。
目标行向量取 (33) 的相同四十五个读数，减去原 $q_N$ 的读数，记作 d。
定义
$$
\boxed{
(a_{\ell,N,p})_{\ell=1}^{45}=
\mathbb M_{702}(\lambda,\kappa,\kappa^N,\eta)^{-1}d .
}
\tag{36}
$$
没有 c0、a 或 bnew 的额外目标列；这些已固定为 $1,\omega^2/2,1$。

公开程序的原顺序为55条 G 列、44条未选 B/G 列，再50条完整 C12 列。
本篇所选列准确是
$$
\boxed{
\begin{gathered}
0,1,\ldots,22,\ 25,26,\ 36,37,\ 47,48,\\
104,105,106,107,108,109,110,\
116,117,118,119,120,121,\ 127,128,129 .
\end{gathered}}
\tag{37}
$$
所选行是原53行的 $0,\ldots,44$，正是前述三十行和 (35)。

在辅助域 $\mathbf F_{1009}$，$\omega=374$、$b=\Omega=1$、
$\kappa=u=0$、$\lambda=(1-\tau)/\tau$，公开准确得到
$$
\boxed{
\begin{array}{c|rr}
&\eta=1&\eta=-1\\ \hline
\tau=2&423&725\\
\tau=3&892&296
\end{array}}
\tag{38}
$$
为 (36) 同一四十五阶子式的行列式。
四种情形均是53行、149个实际测试候选、秩45且相容。
完整目标系数为 $(1,317,1)$，其中 $317=\omega^2/2$；
全部53行、另留出的原 W 第72阶和 W 质量都逐项通过。
这些输出用于证明固定子式不恒零，完整缺行证明是第3–5节。

程序从原 R594 算法重建全部九行/核投影，保完整 C 的
$0,6,12,18,24,30$ 阶项、整个 E 单位逆和两个 C 分支。
四挠部分用 R465 的实际十六支，逐个保 canonical 半周期常数、
两个 quarter 根及两点符号；每个点同时核原未平移端点的全部矩，
并核原无权 R465 的整条四挠恒等式。
所有归一都包括原 $-1/84$。
没有把可重算输出表写成脚本的数字输入。

## 7. 原参数曲线、整性、有限坏集与深度量词

(9)–(10)、(13) 和原 R665 的实际 $\mathfrak j_2$ 算子定义
固定的 $K(\lambda,\kappa,u)$ 矩阵，$K=\mathbf Q(\omega)$。
即使采用四挠点展开时先进入一个固定有限系数域，
完整 Galois 求和后的 (34) 仍在 K；
也可先在固定域取范数清分母，结论相同。

分母仅来自固定几何分母、原 $D_{594}$、有限阶乘、
$\tau-1$、有限组 $1+\lambda\kappa^e$、
$\det(A_p\mathsf B(\tau))$ 及新子式。
最高第一 $2Y$ 型读数到第132阶，加最高伴随次数30，
所需原总阶至多162。本篇可统一删 $p\le163$，
以及固定插值/准周期代数分母的素因子。
这不增加无界次数或未记录的半特征覆盖。

对每个 $\eta=\pm1$ 清完固定分母，令
$d_\eta(L,K,U)$ 为新子式分子。
(38) 在分母有定义处给
$$
d_\eta(L,0,0)\ne0 .
\tag{39}
$$
取固定幂清掉 $L=-1/T$ 的负次数，再对该固定有限组分子/分母
应用固定 CM 单位密度引理。
在旧射线的相对密度一子族上，全部边界值为单位；
新增坏素数计数为 $O(\sqrt X\log X)$ 加固定有限集。
旧 Chebotarev 正密度故仍留下无穷普通 p。

对其中每个 p 和**全部** $N\in4\mathbf Z_{>0}$，
$$
d_\eta(\lambda,\kappa,\kappa^N)
\equiv d_\eta(\lambda,0,0)\pmod p,
$$
其余分母同理。因此
$$
\boxed{
\mathbb M_{702}(\lambda,\kappa,\kappa^N,\eta)\in
\operatorname{GL}_{45}(\mathcal O),\qquad
a_{\ell,N,p}\in\mathcal O .
}
\tag{40}
$$
实际行列式赋值为零，没有新增深度损失。
(36) 使用完整 $\lambda,\kappa,u$，不把辅助 $\kappa=u=0$
的解代回原问题。
$\kappa^{-N}$ 只在实际 D 深门上使用，故新测试仍整有界。
系数可依 p、N，但固定 p、N 后不依后续观察深度 n。
不同 N 的测试族仍不得免费继承“固定多项式”的 N 递推。

由 (15)，新测试准确保持
$$
\boxed{(\pi_4)_*(q_N^{(702)}\mu_0)=\beta^N(\pi_4)_*\mu_0.}
\tag{41}
$$
同一全来源转移付到 R692 三态；原所有总 S/T 行、CM 投影行、
实际 word 逆域仍保持。
第5节、(36)、(40) 完整证明 (33)，不是只得到一个形式相容解。

## 8. 同一个 E 深门的全部三态 Y/W 来源

令
$$
\mathcal E_N=\{E_{YW}\in p^N\},\qquad
\widehat\nu_{\rm new}=[1/2]_*\nu_{S_{\rm new}},\qquad
a=\omega^2/2 .
$$
R690/R693 的完整 $D_*/E_{YW}$ 返回逐项与 W 四挠平移交换，
因为这些都是 W 的真实伙伴。
因此 (33) 给原物理 Y、W 下的来源恒等式
$$
\boxed{
\begin{aligned}
Y_*(1_{\mathcal E_N}q_N^{(702)}e_0)&=\lambda^{2N}\nu_S,\\
Y_*(1_{\mathcal E_N}q_N^{(702)}e_1)&=\lambda^{2N}
                     (a\nu_S+\widehat\nu_{\rm new}),\\
Y_*(1_{\mathcal E_N}q_N^{(702)}e_2)&=\lambda^{2N}
                     (a\nu_S-\widehat\nu_{\rm new}),\\
W_*(1_{\mathcal E_N}q_N^{(702)}(e_0,e_1,e_2))
 &=\lambda^{2N}6\delta(\nu_T,\nu_T,-\nu_T).
\end{aligned}}
\tag{42}
$$
第三条由 (24) 得 $Y_*h_W=\omega^2S$ 后相减；
最后三条保整个 W 核和原 $H_{2,W}T=0$。

(42) 是这些具体隐藏权和 E 门的**整个第一来源**。
它不授权在其右侧再任意附加另一个未付隐藏测试；
任何额外伙伴 cut 必须仍在完整来源上运输。

令
$$
f_w(x)=1_{x\in\mathcal O^\times}\langle x\rangle^{d_pw},
\qquad d_p=p-1 .
$$
物理新线的完整 Mellin 因子是
$\langle2\rangle^{-d_pw}J_{\rm new}(w)$，不能省略。
S、T、Snew 的实际 unit 质量均为零。
因此若三条原中央同时为零，
(42) 的六个完整中央导数确实全部为零，scale log 乘零质量后消失。

保 R692 的真实四轴
$$
Z=W-\frac{20+3\omega}{17}Y,\qquad
V=36Y-(17-3\omega)W,\qquad \gamma=\chi_{29}\chi_{7627}.
$$
它们和 E 门仍在同一完整三态上，来源矩阵为
$$
R=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},\qquad
K=\begin{pmatrix}0&1&-1\\1&0&-1\\0&0&-1\end{pmatrix}.
\tag{43}
$$
物理映射保原
$$
A_Y=R_YP_{Y,\kappa},\quad A_Z=R_YP_{Z,\kappa},\quad
A_W=P_{W,\kappa},\quad A_V=P_{V,\kappa}.
$$
Y/Z 来源用 R，W/V 来源用 K；Z、V 另乘 $\gamma$。
这些映射逐点固定 E 和本篇完整权。

故任意实际核心词 $\mathfrak w$，令 $M_{\mathfrak w}$ 为按顺序
相乘的物理映射，$r$ 为词长，$s$ 为 Z/V 出现数，则
$$
\boxed{
(1_{\mathcal E_N}q_N^{(702)}e_0)|_{M_{\mathfrak w}\mathcal O^6}
=\lambda^r\gamma^s(M_{\mathfrak w})_*
(1_{\mathcal E_N}q_N^{(702)}S_{\mathfrak w}e_0).
}
\tag{44}
$$
来源轨道是 $e_0,e_1,e_2,-e_0-e_1-e_2$。
对观察 $f_w(Y\circ M_{\mathfrak w}^{-1})$ 或
$f_w(W\circ M_{\mathfrak w}^{-1})$，右侧正好是 (42) 的
对应算术行乘 $\lambda^r\gamma^s$。
三原中央零因此合法传到全部这些**完整归一词行**，
无需再作返回后的 CM 投影。

这没有把 $Y\circ M_{\mathfrak w}^{-1}$ 改成原 Y；
不同词的 unit cut、移动 W 观察和附加原输入条件仍必须全转置。
四-unit 分区的混合行也不由 (44) 自动分别归零。

## 9. E 浅来源、旧 A34 词及新高项全部保留

记原无权第二态第一 $2Y$ 来源为 R465 的 $\Xi$。
完整 (41) 在三态上传递，所以 E 浅门准确为
$$
\boxed{
\begin{aligned}
Y_*(1_{\mathcal E_N^c}q_N^{(702)}e_0)
 &=(\lambda^N-\lambda^{2N})\nu_S,\\
Y_*(1_{\mathcal E_N^c}q_N^{(702)}e_1)
 &=\lambda^N[1/2]_*\nu_\Xi
   -\lambda^{2N}(a\nu_S+\widehat\nu_{\rm new}),\\
Y_*(1_{\mathcal E_N^c}q_N^{(702)}e_2)
 &=\lambda^N(\omega^2\nu_S-[1/2]_*\nu_\Xi)
   -\lambda^{2N}(a\nu_S-\widehat\nu_{\rm new}),\\
W_*(1_{\mathcal E_N^c}q_N^{(702)}(e_0,e_1,e_2))
 &=(\lambda^N-\lambda^{2N})6\delta(\nu_T,\nu_T,-\nu_T).
\end{aligned}}
\tag{45}
$$
$\Xi$ 的原 rank0 参考和所有外谱仍在第二、三行。
不能由 (42) 或原三中央零删去它们。

R698 的 adjusted-CM A34 词仍移动 E：
$$
E_{YW}\circ P_{A,\kappa^{34}}
=E_{YW}+(5+6\omega)(\kappa^{34}-1)A .
\tag{46}
$$
逆门必须保 $\kappa^{-34}$ 的完整式；
只有另附已付 $A\in p^{N+34}$ 时才与原 E 深门等价。
本篇没有把 first-Y 投影、A34 或 E 门互相免费交换。

两冻结来源现在准确是 $c_0=1,c_1=0$。
故 R693 式(39)–(40) 的全部原 cd 外部身份仍成立，
将其中 $c_0$ 换成一即可；其固定 N 的过滤仍为
$$
P_{30}=\prod_{a=1}^{30}(\mathsf T-\lambda^2\kappa^a).
$$
每一移位仍用自己的真实门和归一观察。
原 T 的 cd 返回观察是 $b_YY+\kappa^NZ$，不是 (42) 的未缩放 W；
其所有近相消支和质量项继续保留。

最后，同一个四 sigma 门的系数满足
$$
J_2^{(702)}
=\frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N},
\qquad \ell_0=-3\omega/5,
$$
$$
J_a^{(702)}=0\quad
(a\notin\{2,8,14,20,26\}),\qquad
v_p(J_a^{(702)})\ge-aN .
\tag{47}
$$
R693 的完整负一深支因此原样成为
$$
\Delta_{N,n}^{(702)}
=2\beta^n\sum_{a\in\{2,8,14,20,26\}}
   \kappa^{an}J_a^{(702)}\mathscr H_a(\kappa^n),
\tag{48}
$$
其中 $\mathscr H_a$ 是该篇式(43) 的原 Q-unit 全负矩级数。
R655 的同一个已证非零 $I_{\Sigma_5,-1}$ 给
$$
v_p(\Delta_{N,n}^{(702)})
=3n-2N+v_p(I_{\Sigma_5,-1})
\quad(n>N,\ 2n>v_p(I_{\Sigma_5,-1})).
\tag{49}
$$
这里没有将负一矩说成单位；所有新高项都保在 (48)。
它仍只是一条实际深支，必须与 (45)、(46) 及全部 T 失败支同域比较。
本篇新增的算术传播是 (42)–(44)，并未把 (49) 单独当作总中央矛盾。

## 10. 公开执行与可重现记录

脚本：
[check-r702-complete-quarter-source-adaptation.js](../scripts/check-r702-complete-quarter-source-adaptation.js)。

命令：

```sh
node check-r702-complete-quarter-source-adaptation.js --max-block=4 --taus=2,3 --with-b --b-g-blocks=3 --neutral-degree=12
```

- 实际公开 Actions run：`43689632357`；job：`132737328611`。
- source commit：`c231609e8efd0dce8394cd16b9755d6807965fdb`。
- script SHA256：`1adb03a5a36ffa6c540716a5e3e68de5bba6b61a48b50e2b553ce3b77c240b07`。
- stdout：18314 bytes；SHA256
  `735bd265f35a07cf8cf22d8649f1cb88edd4fa3b864798d51d6d79670ee269e7`。
- 固定 R594 原输入算法由脚本当场重建；不读旧输出 JSON。

依根规则15，仓库只留证明、脚本、参数、真实 run 与 hash。
本篇没有保存可重算矩阵/证书输出，也不以 V8 执行标签冒充公开 run。

### 依赖

- [R493：原半挠六 sigma 与保 Y 几何](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R594：原完整九行右逆与六支中性家族](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)。
- [R466：真实新秩二谱线](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。
- [R692：同一四轴三态及实际词域](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)。
- [R693：完整半周期及原三十行返回](R693-neutral-thirty-degree-carry-and-complete-st-companion-return.md)。
- [固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)。
