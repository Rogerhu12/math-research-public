# R679 — 原 π4 中性十二次扩展、三份完整 S 适配与两个真实外部返回

日期：2026-11-15。**状态：已证明。**

本文构造一个新测试 $q_N^\sharp$，明确区别于 R594 的原测试及 R674 的
$q_N^\dagger$。它只增加原完整 $\pi_4$ 推前为零的测试，因而保原 S/T
整个算术返回；同时将两个冻结共同来源及原未切第二 Y 的 cd 端点
准确指定为同一个原 S，且保 R665 实际二阶系数的规范值一。

新增权为六次与十二次之和。本文支付实际十九阶参数矩阵的整逆，
保 C 的第十二矩、新的 $L^8$ 条件项、至多十二次的观察深度项及
全部 T 浅域/外部。旧六次测试的局部零质量结论不移用于这个新测试。

## 1. 同一原来源和一个真正可乘的中性方向

沿用 R594、R664、R665、R669、R674、R675 的完整来源、固定 ray 和坏集：
$$
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad\Omega\in\mathcal O^\times,\quad
N\in4\mathbf Z_{>0},\quad u=\kappa^N.
\tag{1}
$$
仍有
$$
\mu_0=\nu_4\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),\quad
Q=c+2d,\quad L=2c-d,\quad
Y_0=A+Q,\quad Y_1=A+L,\quad \epsilon_i=(-1)^i.
$$
原整数旋转 $\mathsf J(c,d)=(d,-c)$ 的完整来源号为负。
第二支始终取第一支测试的实际转置 $q_1=q_0\circ\mathsf J^{-1}$。

原共同观察
$$
\pi_4=(Y,W,W',G),\qquad
D=F-C,\quad E=F+13C,\quad G=13H_1+(3-2\omega)F
\tag{2}
$$
中的 G 是一个真实物理输出。由原六输入的 Hermitian 配对直接有
$$
\langle G,C\rangle=\langle G,D\rangle=\langle G,E\rangle=0,
\qquad N(G)=936.
\tag{3}
$$
因此 G 不仅是一个形式多项式变量；它在原 D 深返回及 E 单位整逆中
保持。特别对任意原完整 $\pi_4$ 零差测试 h，
$$
(\pi_4)_*(h\mu_0)=0
\ \Longrightarrow\
(\pi_4)_*\!\left(\frac{G^6}{b\Omega^6}h\mu_0\right)=0.
\tag{4}
$$
(4) 是同一测度上乘一个 $\pi_4$ 可测有界整函数的投影公式。
它保任意完整 $\pi_4$ 测试，不只是三个边际或质量。

旋转支使用 $G_i=G\circ\mathsf J^{-i}$，并同时运输所有原门和观察。
不在旋转后擅自把 G 作为未变的另一条物理轴。
原六支 C 平均、C 单位条件及 D 深条件在 (4) 两边均保留。

## 2. 十九个明确的原中性列

令 $A_p$ 为 R594 的实际九乘二十约束矩阵，$R_p$ 为该篇固定整右逆：
$$
\Pi_p=I-R_pA_p.
$$
原二十列按原顺序是
$$
C^iF^jG^{6-i-j},\qquad 1\le i\le5,\quad0\le j\le6-i.
$$
取 R674 的固定索引
$$
\mathcal I=(0,1,2,3,4,13,15,16,17,18,19).
\tag{5}
$$
对 $0\le j\le10$，令 $\delta q_{j,N}$ 是
$\Pi_pe_{\mathcal I_j}$ 对应的完整原 carry 差测试，
包括该列的实际 E 次数整逆
$(1+\lambda\kappa^r)^{-1}$。这些是原十九/二十列中的确定有理函数，
不重新选择右逆。

定义十九个列
$$
\begin{aligned}
h_{j,N}&=\delta q_{j,N},&&0\le j\le10,\\
h_{11+j,N}&=\frac{G^6}{b\Omega^6}\delta q_{j,N},
&&0\le j\le7.
\end{aligned}
\tag{6}
$$
各列都是原有界整测试，且其完整 $\pi_4$ 推前为零。
后八列在生成多项式中等于将前八列的 G 指数增加六；
这一步和 E 单位整逆交换，理由是 (3)，不是只因为两个形式变量名称不同。

混合权按以下物理规范书写：
$$
\mathcal P(D,E,G)=\frac{\widehat P_6(D,E,G)}{b\Omega^6}
               +\frac{\widehat P_{12}(D,E,G)}{b^2\Omega^{12}},
\tag{7}
$$
两项分别齐次六次、十二次。第二项由 (6) 及实际整系数产生。
本文不声称它仍满足 R594 原六次测试的所有局部九个数值条件；
保留的是 (4) 的整个算术推前，以及下面明确重新指定的四组条件。

## 3. 完整来源矩阵的定义：所有参数和 C 补项

记
$$
\mathcal E=5A-29(Q+L),\qquad
e_0=-(170+117\omega)/9135,\quad e_1=-(170+291\omega)/9135,
$$
$$
h_0=-5-9\omega,\qquad h_1=-5-3\omega,\qquad g=3-2\omega.
$$
对 $t=\kappa^{n-N}$，定义真实第一权方向
$$
\begin{aligned}
H_0(t)&=D_*+e_0\mathcal E+
             \frac{h_0t}{315}(5A+39c-92d),\\
H_1(t)&=D_*+e_1\mathcal E+
             \frac{h_1t}{315}(5A-24c+97d),\\
K_i(t)&=H_i(t)-\frac{406}{143}D_*.
\end{aligned}
\tag{8}
$$
$t=0$ 给 R674 冻结方向；$t=1$ 给 R675 真 cd 端点。
保原
$$
E_\perp=14C^\perp,\qquad
G_{00}=G_\perp-\frac{-789+526\omega}{1596}E_\perp,\qquad \eta=\pm1.
$$

对混合多项式 (7)，完整归一来源算子是
$$
\begin{aligned}
\mathscr S_i(\mathcal P;t)(z)=\epsilon_i\int e^{Y_i z/\Omega}
\bigl\{&
\mathcal P(H_i(t),E_\perp+uK_i(t),G_\perp+guK_i(t))\\
&-\eta\lambda\,
\mathcal P(H_i(t),\kappa E_\perp+uK_i(t),
G_{00}+\kappa(G_\perp-G_{00})+guK_i(t))
\bigr\}\,d\mu_0.
\end{aligned}
\tag{9}
$$
这是 R674(6)/R675(5) 对实际有限多项式的线性扩张。
第二行是整个 $C^\perp$ 深补项；所有
$\lambda,\kappa,u$ 和原 $\widehat P$ 的整逆仍在式内。

置
$$
\mathscr U_i(\mathcal P)=\mathscr S_i(\mathcal P;0),\qquad
\mathscr B(\mathcal P)=\mathscr S_0(\mathcal P;1).
\tag{10}
$$
原完整整数旋转给
$\mathscr S_1(\mathcal P;1)=\mathscr B(\mathcal P)$；
这里已经在 (9) 保 $\epsilon_i$，故两个未归一来源相反。

下面的二阶系数也按同一个实际 (7) 定义。写
$$
\mathcal G_*=\{C\ {\rm unit},D_*\in p^N\},\quad
E_*=D_*+14C,\quad G_*=13H_1+g(D_*+C),\quad\ell_0=-3\omega/5.
$$
令
$$
J_2(\mathcal P)=\ell_0^2[z^2]\int_{\mathcal G_*}
 \mathcal P(D_*/u+z/u,E_*+z,G_*+gz)\,d\nu_4,
$$
$$
\boxed{\mathfrak j_2(\mathcal P)=
 \frac{2b\Omega^2}{\ell_0^2}\lambda^{-N}u^2J_2(\mathcal P).}
\tag{11}
$$
用 R665 的 $D_*,C^\perp$ 两个 whole 核计算 (11)，保完整单位减深项；
对十二次项使用真实十次矩，不能使用旧四次质量公式代替。

## 4. 为什么十二次权仍给同一个完整六维 S34 空间

(9) 中每个微分方向都和其实际 $Y_i$ 正交。
R669(6) 的交叉项
$$
29\cdot5a+(2b_1-29a)+2(-b_1-58a)=0
$$
与微分次数无关。因而提升到十二次伴随矩后，完整标准
even34 线丛、半特征和所有周期仍相同；没有新的 flat twist。
六次与十二次均为 $\mu_6$ 的零型权，因此
$$
\mathscr S_i(\mathcal P;t)\in
\mathcal S_{34}^{(0)}
=\operatorname{span}\{\Xi_0,\ldots,\Xi_5\},\qquad
\Xi_j=\sigma^{34}x^{17-3j}.
\tag{12}
$$
先有完整空间证明，才使用
$\Xi_j=z^{6j}(1+O(z^6))$ 的单位三角恢复。
只需 $z^0,z^6,\ldots,z^{30}$ 六个 jet，最高原总次数为 $30+12=42$。
它们可由同一原 sigma 整多项式流计算，固定新增阶乘分母至多 $42!$。

$t$ 只在 (8) 线性出现，故
$$
\deg_t\mathscr S_i(\mathcal P;t)\le12.
\tag{13}
$$
各实际矩阵条目是完整 $\lambda,\kappa,u,\eta$ 的固定有理函数。
本篇的测试系数依 N，所以不从 (13) 推另一个 N 方向递推。

计算必须保 C 的第十二矩。原分离
$$
\mu_0=\nu_{B_C}\otimes\nu_{\mathrm{flat},5},\qquad
B_C(s)=-y(s/\delta)\sigma(s/\delta)^3
$$
给准确截断
$$
\boxed{B_C(s)=1-\frac b{90}s^6
                 -\frac{19b^2}{3742200}s^{12}+O(s^{18}).}
\tag{14}
$$
其余五输入完整函数为
$$
\mathcal F_5(Z_f,Q_f,r,c,d)=
\frac{f_1(Z_f)\Sigma(Q_f)-f_3(Z_f)\Theta(Q_f)}{42}
 \sigma(r)\sigma(c)\sigma(d),
\tag{15}
$$
$f_1=-xy\sigma^6,f_3=-y\sigma^6,\Sigma=\sigma^2,\Theta=x\sigma^2$。
(14) 在伴随次数十二内是精确式，不是忽略高阶 C 的假设。

具体有限算法是将 (8) 及 (9) 的三个方向代 (15)，乘 (14)，
对每个 $D^aE^bG^c$ 取对应系数并乘 $a!b!c!$。
在原 $b$ 上，次数 $6d$ 的权已除 $b^d\Omega^{6d}$；
第 $z^{6j}$ 系数再乘 $b^{1-j}$，两个齐次块具有相同规范。
在 $b=1$ 计算这个表后按此规则恢复原 $b=17$，没有改变来源尺度。

## 5. 实际十九阶整逆与一个固定非零证书

原 S 是
$$
S=\frac{\sigma^{34}x^2}{7}
(x^3+b)(x^3-8b)(7x^6-4bx^3+16b^2).
\tag{16}
$$
其 $\Xi$ 坐标为
$$
(0,1,-53b/7,-12b^2/7,-80b^3/7,-128b^4/7).
$$
用 (12) 的六个归一 jet 记其向量为 $\mathbf s$。

定义实际十九乘十九矩阵 $\mathbb M^\sharp_{N,p}$：
第 j 列就是 $h_{j,N}$ 的
$$
\bigl(\operatorname{jet}_6\mathscr U_0,\
      \operatorname{jet}_6\mathscr U_1,\
      \operatorname{jet}_6\mathscr B,\
      \mathfrak j_2\bigr)^{\mathsf t}.
\tag{17}
$$
这里的 $\operatorname{jet}_6$ 按第4节归一。
以 $v_{\rm old}$ 记原 R594 旧测试的同一十九行向量，完整地定义
$$
\boxed{
a_{N,p}=(\mathbb M^\sharp_{N,p})^{-1}
       \bigl((\mathbf s,\mathbf s,\mathbf s,1)^{\mathsf t}-v_{\rm old}\bigr),
\qquad
q_N^\sharp=q_N+\sum_{j=0}^{18}(a_{N,p})_j h_{j,N}.
}
\tag{18}
$$
(18) 是全参数定义；它不是把一个模 p 解作为 p-adic 系数。
下面证明这个实际逆在所用子族整存在。

附脚本直接从原 sigma 递推、(14)–(15)、
R594 原二十列/整右逆及 (8) 生成全部矩阵。
在仅用于固定非零判定的辅助剩余域
$$
\mathbb F_{1009},\quad \omega=374,\quad
\tau=(1+\lambda)^{-1}=2,\quad \lambda=-1/2,\quad
\kappa=u=0,\quad b=\Omega=1,
$$
十九个列就是 (6) 的原顺序，不作依 p 选主元。完整得到
$$
\boxed{\det\overline{\mathbb M}^\sharp_+=770,\qquad
       \det\overline{\mathbb M}^\sharp_-=888\pmod{1009}.}
\tag{19}
$$
辅助目标 S jet 为 $(0,1,202,222,143,792)$。
两个完整十九维解分别为
$$
\begin{aligned}
\eta=+1:\ (&497,449,924,374,55,273,492,763,276,626,9,\\
          &297,511,462,321,222,124,82,716),\\
\eta=-1:\ (&137,910,330,579,327,32,750,348,389,148,463,\\
          &383,894,413,247,538,83,292,692).
\end{aligned}
\tag{20}
$$
JSON 保存全部 $19\times19$ 矩阵、旧仿射项、目标和右端。
脚本逐式检查三十八个新方程，并与已发表原完整矩阵的
286 个冻结/二阶条目及 310 个端点生成系数准确相合。
此处不是对普通素数作扫描；(19) 只证明两个固定特征零有理式
的分子都不恒等为零。

排除原固定分母以及 (14)、全部有限几何/阶乘分母，
对这两个固定非零分子应用已付的固定 CM 多项式单位密度引理。
仍在原 ray 的相对密度一子族上，有
$$
\boxed{\mathbb M^\sharp_{N,p}\in\mathrm{GL}_{19}(\mathcal O)
       \quad\text{对全部 }N\in4\mathbf Z_{>0}\text{ 同时成立}.}
\tag{21}
$$
因为 $\kappa,u\equiv0\pmod p$，余式与 N 无关；
实际 $\eta=\pm1$ 都已覆盖。原右逆的所有高参数修正由 (18) 保留。
(18) 的右端整，故新测试系数整，且固定 N 后不依 n。

由 (12)、(17)–(21)，得到三条**完整来源**身份及同一个实际系数：
$$
\boxed{
\mathscr U_0(q_N^\sharp)=S,\quad
\mathscr U_1(q_N^\sharp)=S,\quad
\mathscr B(q_N^\sharp)=S,\quad
\mathfrak j_2(q_N^\sharp)=1.}
\tag{22}
$$
特别
$$
\boxed{J_2^\sharp=
\frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N}.}
\tag{23}
$$
这是扩大中性测试族后的新结论，不修改 R677 对原二十列族的
端点障碍，也不改变旧 $q_N^\dagger$。

## 6. 原整个算术返回保持

由 (4)、(6)、(18)，
$$
\boxed{(\pi_4)_*(q_N^\sharp\mu_0)
       =(\pi_4)_*(q_N\mu_0)=\beta^N(\pi_4)_*\mu_0.}
\tag{24}
$$
因此所有原 Y/W/W' 完整单位及 Mellin 测试都保持原返回。
第二旋转支同样由完整 $\mathsf J$ 转置给出，而非重选测试。

深度 n 的两原 S 总行仍为
$\epsilon_i\lambda^{n+N}J_S(w)$。
原 T 总行和全部 W 失败支也仍为相应原行；
本篇不把 (22) 的纯 S 来源身份转移到不同的 T 单位 cut。

特别新测试已保原完整来源，但没有理由保旧八角域的严格零质量。
原六次质量/局部首项约束和 (24) 是不同命题；
本篇只对 (22)–(24) 明确指定的条件作结论。

## 7. 未附第二 Y 的 cd 域现在完整返回原 S

保持 R671/R675/R677 的实际域和观察：
$$
\mathsf E_i(n)=\{Y_i\in p^n\},\quad
\mathsf{CD}_N=\{c,d\in p^N\},\quad
\Gamma_n=\mathsf E_0(n)\cap\mathsf E_1(n),
$$
$$
\mathsf I_n=\Gamma_n\cap\mathsf{CD}_N
=\Gamma_n\cap\{\mathcal E\in p^N\},
$$
$$
\mathsf V_{i,n}=\mathsf E_i(n)\cap\mathsf{CD}_N,\quad
\mathsf O_{i,n}=\mathsf V_{i,n}\setminus\mathsf I_n,\quad
\mathsf X_{i,n}=\mathsf E_i(n)\setminus\mathsf{CD}_N.
\tag{25}
$$
每个行保自己的 $Y_i/(-\kappa)^n$ unit/Mellin 测试、
原 C/D 门和新同一个 $q_N^\sharp$；符号表示这些实际行，
不是无权集合的质量。

R675 已付 $n=N$ 同域端点及 R671 的完整 cd 运输。
结合 $\mathscr B=S$，对全部 $n\ge N$ 得到
$$
\boxed{
\mathcal V_{i,n}^{S,\sharp}(w)
=\epsilon_i\lambda^{n+3N}J_S(w),}
$$
$$
\boxed{
\mathcal X_{i,n}^{S,\sharp}(w)
=\epsilon_i\lambda^{n+N}(1-\lambda^{2N})J_S(w).}
\tag{26}
$$
这两条是未过滤的整个 Mellin 身份。
与旧 $q_N^\dagger$ 的未知非 S 端点不同，(26) 没有六维额外观察。
来源系数乘法也不产生变量缩放的 $\log$ 常数。

## 8. 同一个十二步算子控制实际 opposite-Y 外部

由 (13)、(22)，存在整个 S34 中的实际来源 $T_{i,a,N,p}$，使
$$
\mathscr S_i^\sharp(t)=S+\sum_{a=1}^{12}t^aT_{i,a,N,p}.
\tag{27}
$$
全部十二条高系数保留。定义真实序列移位 $\mathsf T:n\mapsto n+1$，
$$
\mathcal P_{12}(\mathsf T)=
 \prod_{a=1}^{12}(\mathsf T-\lambda^2\kappa^a),\quad
U_{12}=\prod_{a=1}^{12}(1-\kappa^a),\quad
V_{12}=\prod_{a=1}^{12}(1-\lambda\kappa^a).
\tag{28}
$$
$U_{12},V_{12}$ 均单位。由共同来源的原因子 $\lambda^{2n+2N}$，
$$
\boxed{
\mathcal P_{12}\mathcal I_{i,n}^{S,\sharp}
=\epsilon_i\lambda^{2n+2N+24}U_{12}J_S,}
$$
$$
\boxed{
\mathcal P_{12}\mathcal O_{i,n}^{S,\sharp}
=\epsilon_i\left[
 \lambda^{n+3N+12}V_{12}
-\lambda^{2n+2N+24}U_{12}\right]J_S,}
$$
$$
\boxed{
\mathcal P_{12}\mathcal X_{i,n}^{S,\sharp}
=\epsilon_i\lambda^{n+N+12}(1-\lambda^{2N})V_{12}J_S.}
\tag{29}
$$
每个移位项都使用自身的真实域、移动单位观察及同一个固定 N 测试。
(29) 不是把不同深度 cut 当成一个不动的条件。

原 $J_S(0)=0$ 给 (26)、(29) 的完整质量为零。
若再假设原 $J'_S(0)=0$，这些显示的完整中央导数都为零。
这是整个实际外部行的算术返回，不是将其某个非零子域赋零。

## 9. 新八阶条件系数必须保留；原负一主项未被删掉

对同一实际混合权 (7)，定义 $J_a^\sharp$ 为
$$
J_a^\sharp=\ell_0^a[z^a]\int_{\mathcal G_*}
 \mathcal P^\sharp(D_*/u+z/u,E_*+z,G_*+gz)\,d\nu_4 .
\tag{30}
$$
原四输入来源及六次/十二次权的完整角型迫
$$
\boxed{
\int_{\mathcal G_*}
 \mathcal P^\sharp(D_*/u+z/u,E_*+z,G_*+gz)\,d\nu_4
=\frac{J_2^\sharp}{\ell_0^2}z^2+
 \frac{J_8^\sharp}{\ell_0^8}z^8 .}
\tag{31}
$$
这是所有系数的准确消去；$J_8^\sharp$ 没有被指定为零。
整系数和原深门直接给
$$
v_p(J_8^\sharp)\ge-8N.
\tag{32}
$$

令 $\Delta_{N,n}^\sharp$ 是 R665 的两个实际
$b_LL\pm b_YQ$ log 行在同一 $L\in p^n$ 门上的差，
仅把权换为 $q_N^\sharp$。保原全部 C/D 门、Q-unit 和 L 总输入。
对 $a=2,8$ 定义
$$
\begin{aligned}
\mathscr H_a(t)={}&
6b\sum_{k\equiv1(6)}
 \frac{h^kt^k}{k}I_{\Sigma_5,-k}M_{X_5,k+a}\\
&+6b\sum_{k\equiv3(6)}
 \frac{h^kt^k}{k}I_{X_5,-k}M_{\Sigma_5,k+a}
+3\sum_{k\equiv5(6)}
 \frac{h^kt^k}{k}I_{Z_5,-k}M_{Z_5,k+a},\qquad k\ge1,
\end{aligned}
\tag{33}
$$
$h=b_L/b_Y$，负矩保 Q 单位，正矩是整个 L 总矩。
R665 的全 log 展开及 (31) 给
$$
\boxed{
\Delta_{N,n}^\sharp=
2\beta^n\left[
 \kappa^{2n}J_2^\sharp\mathscr H_2(\kappa^n)+
 \kappa^{8n}J_8^\sharp\mathscr H_8(\kappa^n)\right].}
\tag{34}
$$
没有将第二项或任一其余负矩删除。

原 $X_5=x\sigma^5$ 满足
$$
X_5(z)=z^3-\frac{5b}{42}z^9+\cdots,\quad
M_{X_5,3}=6\Omega^3,\quad M_{X_5,9}=-43200b\Omega^9.
$$
所以
$$
\mathscr H_2(\kappa^n)=36b\Omega^3hI_{\Sigma,-1}\kappa^n+p^{3n}\mathcal O,
$$
$$
\mathscr H_8(\kappa^n)=-259200b^2\Omega^9hI_{\Sigma,-1}\kappa^n
                      +p^{3n}\mathcal O.
\tag{35}
$$
每个 log 分母 k 均保留；$kn-v_p(k)\ge3n$ 对奇 $k\ge3$ 给统一尾界。
于是
$$
\begin{aligned}
\Delta_{N,n}^\sharp={}&
72b\Omega^3h\,\beta^n\kappa^{3n}I_{\Sigma,-1}
 \left[J_2^\sharp-7200b\Omega^6\kappa^{6n}J_8^\sharp\right]\\
&+J_2^\sharp p^{5n}\mathcal O+J_8^\sharp p^{11n}\mathcal O.
\end{aligned}
\tag{36}
$$
由 (23)、(32)，当 $n>N$ 时方括号除以 $J_2^\sharp$ 是单位。
R655 已付同一个原 $\Sigma_5=\sigma_{17}^5$ 的 $I_{\Sigma,-1}\ne0$；
不宣称它是统一单位。凡
$$
n>N,\qquad 2n>v_p(I_{\Sigma,-1}),
$$
都有准确值层
$$
\boxed{v_p(\Delta_{N,n}^\sharp)=3n-2N+v_p(I_{\Sigma,-1}).}
\tag{37}
$$

## 10. 完整 T 补域、角域质量及剩余算术问题

R662/R665 的实际全域分解对这个合法新测试仍成立。
若原 $J'_T(0)=0$，记其两个原 T 外部为 $\mathcal E_\pm^\sharp$，
原整个 L 浅补域为 $\mathcal R_{N,n}^\sharp$，则
$$
\boxed{
\mathcal E_+^\sharp-\mathcal E_-^\sharp+
\mathcal R_{N,n}^\sharp=-\Delta_{N,n}^\sharp.}
\tag{38}
$$
(38) 保两条不同移动 W 单位 cut、所有 log 质量和全部外部。
(29) 是纯 S 观察；本篇没有证明 (38) 左边等于这些 S 外部的组合。
因此 (37) 与 (29) 不能单独推出中央矛盾。

十二次权还允许原 pair 的正总次数八。
旧 R678/R682 六次测试在八角域的严格零质量不可直接沿用。
若把新测试用于那些同域词，必须保完整相对 Mellin
$T-\langle b_Y\rangle^{d_pw}S$，
包括质量乘 $\log\langle b_Y\rangle$ 的项。
已付的条件化三阶稳定说明可以另行应用，但不替代这些量。
本文不更改旧 q、旧角域证书或旧零质量结论。

新增完整结论是：通过真正 $\pi_4$ 中性、可整计算的十二次扩展，
同一测试的两份冻结来源和原 cd 端点已同时准确回到 S；
原两种完整外部的算术返回 (26)、(29) 已支付，
而原已知负一深支以 (34)–(37) 全部保留。
固定曲线的无穷不同 p 主目标仍未完成，剩余为同一测试下
T 的真实失败支与这些完整 S 返回的准确关系。

## 复现文件与依赖

- [脚本](../scripts/check-r679-neutral-degree-twelve-three-s-adaptation.js)
- [完整十九阶证书](../scripts/check-r679-neutral-degree-twelve-three-s-adaptation.json)

默认 Node 脚本读取已发表 R594、R674、R675 JSON；
从原 sigma 递推重建全部四个六/十二次生成表、两个十九阶矩阵及仿射解。
辅助域中的所有运算是准确整数/有限域运算。
实际测试严格由 (9)、(11)、(17)、(18) 定义，不使用辅助解作 p-adic 系数。

主要依赖：
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)；
[R664](R664-original-double-s-rotation-and-common-companion-gate.md)；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)；
[R669](R669-original-double-s-six-dimensional-source-return.md)；
[R674](R674-original-double-s-arithmetic-adaptation-and-negative-one.md)；
[R675](R675-original-cd-endpoint-and-complete-six-source-return.md)；
[R677](R677-adapted-cd-endpoint-and-complete-exterior-filters.md)。
