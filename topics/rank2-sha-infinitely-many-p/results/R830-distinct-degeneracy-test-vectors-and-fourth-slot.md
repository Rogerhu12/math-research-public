# R830 — 不同二退化向量、原三重积的坏位测试及完整第四槽

日期：2026-11-15。

本篇保持 R826 的三个固定有序对、完整 Hecke 角色和原权四
$\lambda_\ell$，只把第三个输入改到另一份真实二退化副本。
同一退化副本的 Chow 零已由 R829 支付，本篇不再把它当非零来源。

**状态：已证明。** 以下几何恒等式、全部有限坏位测试和第四槽公式均已支付。
三、十七处使用同一原有限角色的公开精确有限群计算；运行与值见第6节。
局部测试非零不等于全局对角类或其指定 $p$-adic Abel–Jacobi 值非零。

## 1. 保持三个原动机，改变一个实际向量

沿 R826，取
$$
K=\mathbf Q(\omega),\qquad
f=\theta(\psi_{17}),\qquad
g_j=\theta(\eta_j^{-2}\psi_0),\qquad
\lambda_\ell=\eta_\ell^{-1}\psi_0^3,
$$
以及原有序对
$$
\begin{array}{c|c}
\ell&(j,k)\\ \hline
4&(10,16)\\
10&(16,4)\\
16&(4,10).
\end{array}
\tag{1}
$$
$f$ 的 primitive level 为 $10404$；
三个 $g_j$ 的 primitive level 为 $2601$，nebentypus 均为1。

R826(10)的全部八维分解继续保持：
$$
AI(\psi_{17})\otimes AI(\beta_j)\otimes AI(\beta_k)
=
AI(\lambda_\ell)\oplus
\mathrm N AI(\gamma_\ell)\oplus
\mathrm N AI(\psi_{17^3})\oplus
\mathrm N AI(\psi_{17^5}).
\tag{2}
$$
改选 old 向量不改任何一个表示、导子、全局角色或 primitive Euler。
尤其四因子在2、3、17处的 primitive Euler 都为1；
没有把单个 $g_j$ 在2处的好 Euler 附加给三重积。

三个原全局表示与下面所有向量、曲线和幂等元均先于研究素数 $p$ 固定。
不根据某个 $p$ 的值重新挑选 cycle。

## 2. 两个 degree12 退化映射与 cusp 对应

置
$$
M=2601,\qquad N=4M=10404,\qquad
X=X_1(N),\quad C=X_1(M).
$$
用 $Q=e^{2\pi i\tau}$ 作展开变量，以免与映射记号混淆。
取
$$
\begin{split}
q_0(E,P)&=(E,4P),\\
q_4(E,P)&=(E/\langle MP\rangle,\bar P).
\end{split}
\tag{3}
$$
在标准 cusp 坐标中它们分别是 $\tau\mapsto\tau$ 与
$\tau\mapsto4\tau$。两映射泛型次数均为12。
对 $q_0$，这是原 order-$M$ 点的十二个 primitive order4 分量；
对 $q_4$，六个 cyclic order4 核各有两个所需 primitive lifts。

取同一 cusp 支撑的 degree1 基点循环，必要时取固定域上的 Galois 平均。
由 Manin–Drinfeld，两个映射各自满足
$$
(q_a)_*o_X=o_C,\qquad q_a^*o_C=12o_X
\quad\text{于 }CH^1(X)_{\mathbf Q},\qquad a=0,4.
\tag{4}
$$
这使两份 Chow–Künneth 投影与 pull/push 相容。
(4)依赖实际 modular cusps；不对任意 pointed 曲线作同样断言。

若 $e_g^C,e_h^C$ 是下层实际自伴 Hecke 新形式投影，则选定 old 副本的幂等元为
$$
e_g^{(0)}=\frac1{12}q_0^*e_g^C(q_0)_*,
\qquad
e_h^{(4)}=\frac1{12}q_4^*e_h^C(q_4)_*.
\tag{5}
$$
由 $(q_a)_*q_a^*=12$，它们确为幂等元。
令 $\Delta_X$ 为使用(4)基点的 modified diagonal，定义
$$
\Delta^{(0,4)}_{j,k}
=(e_f\otimes e_g^{(0)}\otimes e_h^{(4)})_*\Delta_X.
\tag{6}
$$
再按(2)作原 $\lambda_\ell$ 的 CM 投影。
本篇将其与 R814 的 canonical cycle 区分，尚未付二者非零比例。

为核定与 R829 的差别，若把(5)第三项也改用 $q_0$，则
$$
(\mathrm{id}\times q_0\times q_0)_*\Delta_X^{\rm sm}
=(q_0\times\mathrm{id}\times\mathrm{id})^*\Delta_C^{\rm sm}.
\tag{7}
$$
$e_fq_0^*=0$，连同(4)，使该同映射的整个 Chow 投影为零。
这正是 R829 的已证明结论。不同映射时实际推前是
$x\mapsto(x,q_0(x),q_4(x))$，不能将其替成(7)右侧。
这一差异本身仍不是(6)非零的证明。

## 3. 二处的真正非零测试向量

所有局部表示先作权二的 unitary 归一；中心特征均为1。
在2处，$g,h$ 是 unramified principal series，$a_2(g)=a_2(h)=0$；
$f$ 是 conductor exponent2 的 supercuspidal。
原三重积的局部符号为 $+1$，故 split 三线性空间为一维。

设 $v_g,v_h$ 为 spherical newvectors，$v_f$ 为原 conductor2 newvector。
Dimitrov–Nyssen 已发表 Theorem3，取
$$
\gamma_2=\begin{pmatrix}2^{-1}&0\\0&1\end{pmatrix},\qquad n=2,
$$
给
$$
\boxed{\mathcal L_2(v_f,v_g,\gamma_2^2v_h)\ne0}
\tag{8}
$$
对该一维空间的任一非零三线性形式成立。
该定理覆盖 residue characteristic2；
本次只有一个 supercuspidal 输入，没有引入其全 supercuspidal 特例的额外条件。

几何 $q_4^*$ 恰给(8)这条局部向量线。
有限处的右平移 $\operatorname{diag}(1/4,1)$，经有理矩阵移到无穷处，
是权二 slash $\operatorname{diag}(4,1)$。
所以实际几何微分不是裸 $h(Q^4)dQ/Q$，而是
$$
\boxed{
\omega_g^{(0)}=g(Q)\frac{dQ}{Q},\qquad
\omega_h^{(4)}=4h(Q^4)\frac{dQ}{Q}.
}
\tag{9}
$$
标量4非零，故(8)仍适用。
在3、17处，$\operatorname{diag}(4,1)$ 是原 $K_0(\ell^2)$ 的单位矩阵，
对平凡 nebentypus 新向量作用为1；两个原 finite types 没有因此改变。

这里固定的是实际 trilinear 线和实际向量。
没有把(8)中的非零局部值无规范地写成1。

## 4. 三、十七处的 depth-zero 来源和新向量

### 4.1 真实原局部类型

在 $\ell=17$，原二次 CM 扩张不分歧。
R826 的单位角色均 tame regular，原导子指数为2；
因此三个输入均为 depth-zero supercuspidal。

在 $\ell=3$，原 CM 扩张分歧，但 R826 的 inducing character
在单位上为 residue sign、在 $\delta$ 上为 $+i$；
$\eta_j^{-2}$ 不改变该数据。它与共轭不同，故诱导不可约。
它对 wild inertia 平凡，所以是 tame 二维不可约参数。
中心特征为1，故 tame inertia 两特征值为 $\zeta,\zeta^3$，
满足 $\zeta^4=1$ 且 $\zeta^2\ne1$。
这就是唯一 regular order4 finite cuspidal type。
原 $f$ 的三处 inducing character 可取上述字符的共轭（其 $\delta$ 值为 $-i$）；诱导及有限类型相同。因此三处同样是 conductor2 depth-zero，
不是把“CM 扩张分歧”错误等同于正深度。

统一令 $q=\ell$，$G_q=PGL_2(\mathbf F_q)$，
$T_q=\{\operatorname{diag}(a,1):a\in\mathbf F_q^\times\}$。
有限类型 $\rho_m$ 来自 regular central-trivial
$\theta_m$；其维数为 $q-1$。

十七处固定 R818 §2、§5 的 norm-one 基
$$
g_{17}=2+11\omega,\qquad g_{17}^{6}=\omega,\quad g_{17}^{9}=-1,
$$
并按
$$
\boxed{\theta_m(z)=
 \zeta_{18}^{m\log_{g_{17}}(z^{16})}}
\tag{10}
$$
定义字符。$g_{17}$ 的阶是18，不能将它当成 $\mathbf F_{289}^\times$
的阶288生成元。枚举全乘法群时另选生成元，不改(10)的标签。

将一个字符换成逆字符给同一 finite cuspidal。
在此等价范围内，三个原有序对的 finite indices 准确为
$$
\begin{array}{c|c|c}
q&\ell& (m_f,m_g,m_h)\\ \hline
3&4,10,16&(1,1,1)\pmod4\\
17&4&(3,16,4)\pmod{18}\\
17&10&(3,4,10)\pmod{18}\\
17&16&(3,10,16)\pmod{18}.
\end{array}
\tag{11}
$$
十七处 $m_{g_j}=-2(j-9)$；$f$ 可取3，因为其实际逆指数15给同一表示。
(11)来自 R826 的全有限角色，不从好素数特征猜测。
另一 R818 允许的系数域嵌入只置换三行。

### 4.2 从有限 split torus 线到原 Casselman 新向量

Kutzko 的 depth-zero compact-induction 描述给
$$
\pi_m\simeq
c\operatorname{-Ind}_{Z_\ell GL_2(\mathbf Z_\ell)}^{GL_2(\mathbf Q_\ell)}
\widetilde\rho_m .
\tag{12}
$$
$\widetilde\rho_m$ 是有限类型的 inflation，标量中心作用取原中心特征1。
这些 conductor2 supercuspidal 已为 minimal，故该描述无额外 conductor 条件。

由下面(14)的 character，$e_T=(q-1)^{-1}\sum_{t\in T_q}\rho_m(t)$ 的迹为1。
它是 Hermitian 正交投影，故 $\rho_m^{T_q}$ 是一维。
取其中 norm1 的 $v_m$，令 $F_{v_m}$ 为(12)中支撑在 $Z_\ell K_\ell$、
且 $F_{v_m}(1)=v_m$ 的向量。

用右平移约定 $\pi(a)F(x)=F(xa)$，置
$$
\gamma_\ell=\operatorname{diag}(\ell^{-1},1).
$$
对 $k\in K_0(\ell^2)$，
$\gamma_\ell^{-1}k\gamma_\ell$ 模 $\ell$ 为对角矩阵。
故 $\pi(\gamma_\ell)F_{v_m}$ 被 $K_0(\ell^2)$ 固定，
由 conductor2 新向量唯一性，它恰为原新向量线。

三个输入使用同一个 $\gamma_\ell$。
对角 $GL_2$ 不变性消去这个共同平移，
因此原三个新向量的测试非零准确等价于三个 $T_q$ 固定有限向量的测试非零。

如果 $L_\rho$ 是有限类型上的 invariant 三线性形式，其局部延拓可直接写为
$$
L(F_1,F_2,F_3)
=\sum_{x\in Z_\ell K_\ell\backslash GL_2(\mathbf Q_\ell)}
 L_\rho(F_1(x),F_2(x),F_3(x)).
\tag{13}
$$
每个向量 compact support modulo $Z_\ell K_\ell$，所以和有限；
中心特征乘积为1使其不依赖代表。
右平移只置换陪集，因此(13)为局部 invariant 形式。
对三个 $F_{v_i}$，它恰等于 $L_\rho(v_1,v_2,v_3)$。
Prasad multiplicity one 因而把有限测试准确送回原局部三线性线，
不只证明某个不相关的有限表示有 invariant。

## 5. 完全精确的有限 projector norm

给每个有限类型取 invariant Hermitian form，内积对第一因子线性。
$\theta_m$ 在 $\mathbf F_q^\times$ 上平凡，故 character 在 $G_q$ 上为
$$
\chi_m(x)=
\begin{cases}
q-1,&x=1,\\
-1,&x\text{ 为非平凡 unipotent},\\
0,&x\text{ 为 split regular},\\
-\theta_m(z)-\theta_m(z^q),&
 x\text{ 的 eigenvalues 为 }z,z^q\notin\mathbf F_q.
\end{cases}
\tag{14}
$$
这是实际有限 cuspidal character，亦可自含构造：
在 $G_q$ 上取 nontrivial additive $\psi$，则
$\operatorname{Ind}_{U_q}^{G_q}\psi-
 \operatorname{Ind}_{T_q^{\rm ns}}^{G_q}\theta_m$
的 character 为(14)。
按恒等、unipotent、split regular、nonsplit regular 四类求和，character norm 为1；identity值 $q-1>0$，
所以为真正不可约 character；其 unipotent invariants为0，故为cuspidal。
这一验证使用 regular 条件 $\theta_m^2\ne1$。

令 $v_m$ 为第4节固定的 unit 向量。因为 $e_T$ rank1，
$$
M_m(x):=\langle\rho_m(x)v_m,v_m\rangle
=\operatorname{Tr}(\rho_m(x)e_T)
=\frac1{q-1}\sum_{t\in T_q}\chi_m(xt).
\tag{15}
$$
对 $v=v_{m_1}\otimes v_{m_2}\otimes v_{m_3}$，全群正交投影给
$$
\boxed{
\|e_{G_q}v\|^2
=\frac1{|G_q|}\sum_{x\in G_q}\prod_{i=1}^3M_{m_i}(x),
\qquad |G_q|=q(q^2-1).
}
\tag{16}
$$
(16)不是 $\sum|\prod M_i(x)|^2$，也不能只给其中一因子取共轭。
Hermitian 关系为 $M_m(x^{-1})=\overline{M_m(x)}$；
它已在同一精确 cyclotomic 环中核对。
非负性来自整个 $e_G=e_G^*=e_G^2$，不是对每个求和项假设正。

同时从(14)求全 character 内积得
$$
\dim(\rho_{m_1}\otimes\rho_{m_2}\otimes\rho_{m_3})^{G_q}
=
1-\frac12\#
 \{(\epsilon_1,\epsilon_2,\epsilon_3)\in\{\pm1\}^3:
   \epsilon_1m_1+\epsilon_2m_2+\epsilon_3m_3=0\bmod(q+1)\}.
\tag{17}
$$
在(11)中该个数为0：$q=3$ 时三个 odd 指数之和为odd，
$q=17$ 时一个odd加两个even仍为odd。因此维数恰为1。
于是(16)非零当且仅当原指定三个新向量在这一唯一 invariant 线上的值非零。

式(17)也可直接核定。记其中符号解数为 $A$。
identity 和 unipotent 的总贡献是 $(q-1)^3-(q^2-1)$。
nonsplit 项按 $\mathbf F_{q^2}^\times/\mathbf F_q^\times$ 配对求和，
贡献为 $-\frac{q(q-1)}2((q+1)A-8)$；
order2 类的较大中心化子恰由同一半和计入。
两者相加等于 $|G_q|(1-A/2)$，故得到(17)，没有遗漏 exceptional class。


## 6. 公开计算的固定参数、完整输出与范围

唯一 producer 为
`scripts/check-r830-fixed-bad-prime-test-vectors.py`，
版本 `R830-fixed-bad-prime-types-v2`，Python 标准库、无参数。
只处理两个固定有限域 $\mathbf F_3,\mathbf F_{17}$，不扫描研究素数 $p$。

有限域分别使用 $u^2=-1$ 和 $\omega^2+\omega+1=0$。
程序先固定原 norm-one 基，再在公开运行中独立搜索整个乘法群的生成元；
每个实际 character 始终按(10)而非新原根的指数定义。
完整 $PGL_2$ 枚举采用首个非零矩阵元归一为1的唯一代表，
因而准确包含 $q(q^2-1)$ 个元素。
每个 $\chi_m(xt)$、每个 $T$ 投影和(16)都在
$\mathbf Z[i]$ 或 $\mathbf Z[\zeta_{18}]$ 中精确运算，
不以数值误差识别零或 character。

公开运行成功且完整日志已由作者、根线程分别读取：

- run `43765677768`；job `132970102886`；
  source `5240a858e181a32c17403d7c393ce75d736c44bd`。
- 脚本 SHA256：
  `4f63322ef7fbfdf4110d72343d71f46bf52591d9f17d80a5ed8fa64c37353a6a`。
- stdout 2497 bytes，SHA256：
  `0cbcfcbec3f3ef637e4e0913ab0b8c98e6c0068ea92eb2a6cda0b914496156f8`。
- 三处完整表的规范 SHA256：
  `7e41892c527dd9574db6e2f7469af04997c10dd2979f46c841571e82aa0b57a2`。
- 十七处完整表的规范 SHA256：
  `3383dc41bc9cad5e2d65ef2381f756dd8ee9eeae6edb4bdddd5d78c767d67e2a`。
- [公开完整日志](https://github.com/Rogerhu12/math-research-public/actions/runs/43765677768/job/132970102886)。

本次确认十七处全乘法群原根为 $(1,3)$，阶288；
原 $(2,11)$ 保持为范数一群的阶18生成元。
初版 run `43765417609` 因混淆这两个阶数，在建全群表时 assertion 失败，
没有产生十七处数学范数结论；本篇只使用已修正的上述 v2 完整运行。

令 $\zeta=\zeta_{18}$。输出给三处
$
\|e_{G_3}(v_1\otimes v_1\otimes v_1)\|^2=\frac14.
\tag{18a}
$
十七处三个平方范数准确为
$
\begin{array}{c|l}
\ell&2304\,\|e_{G_{17}}(v_f\otimes v_g\otimes v_h)\|^2\\ \hline
4&13-8\zeta-8\zeta^2+10\zeta^4-2\zeta^5\\
10&13-2\zeta-2\zeta^2-8\zeta^4+10\zeta^5\\
16&13+10\zeta+10\zeta^2-2\zeta^4-8\zeta^5.
\end{array}
\tag{18b}
$
$1,\zeta,\ldots,\zeta^5$ 是 $\mathbf Q(\zeta_{18})$ 的基；
各常数项为13，所以三项均非零。
它们是(16)的 Hermitian 平方范数，故在对应复嵌入下严格为正，
不需要浮点正性判断。全部 $T$ 投影 rank1、
完整 invariant dimension1 和 $M(x^{-1})=\overline{M(x)}$ 检查均通过。

选有限 invariant 张量的 unit 基 $u$ 后，
$L_\rho(w)=\langle w,u\rangle$，所以(18a)–(18b)就是
$|L_\rho(v)|^2$；基的单位复相位不影响非零。
这里未将这个有限计数规范的数值冒认任意 Haar/Ichino 规范的局部积分。
第4节的显式 compact-induction 延拓足以把非零无损送回原局部线。
原代数微分和对角类的绝对规范仍由(3)、(5)、(9)固定。

结合(8)，三份固定新向量在2、3、17全部是有效 test vectors。
其余有限位是原 spherical 向量，其非零性由标准 unramified
三线性测试（Dimitrov–Nyssen Theorem2(i)，原 Prasad Theorem1.3）给出。
这是所有有限位的结论；无穷处仍为原符号 $-1$，
不能将它偷换成一个非零的全局中心三重积积分。

仓库仅保留 producer、参数及 run/hash；
全部可重算表和输出不另存仓库或 Release。

## 7. 新微分、原函数、第四槽和周期倍率

在原 ordinary ray 上取 $p>17$，$p=\pi\bar\pi$，
$v_p(\pi)=1$。继续用 R826 的 arithmetic/CM 嵌入。
两个退化映射在 $p$ 处与 canonical Frobenius 相容，所以
$$
\varphi\omega_f=-\pi\omega_f,\quad
\varphi\omega_g^{(0)}=\pi\omega_g^{(0)},\quad
\varphi\omega_h^{(4)}=\pi\omega_h^{(4)}.
\tag{18}
$$
下层的真实零常数 CM 原函数为
$$
\theta G_g=g-\bar\pi Vg,\qquad
\theta G_h=h-\bar\pi Vh,\qquad \theta=Q\,d/dQ.
$$
它们的完整 ideal coefficients 是 R826 附录A的原系数；
不删除任何 $17\delta$ 条件。拉回后为
$$
\boxed{G_g^{(0)}=G_g(Q),\qquad G_h^{(4)}=G_h(Q^4).}
\tag{19}
$$
(19)第三项没有额外4；微分使 $\theta G_h(Q^4)=4(\theta G_h)(Q^4)$，
恰产生(9)中的4。

因此 Besser 的完整 finite-polynomial 代表是
$$
\begin{split}
\Xi_{g,h}^{(0,4)}
&=G_g^{(0)}\omega_h^{(4)}
   -\pi^{-1}G_h^{(4)}\Phi^*\omega_g^{(0)}\\
&=\boxed{\left(4G_g(Q)h(Q^4)
 -\bar\pi G_h(Q^4)g(Q^p)\right)\frac{dQ}{Q}.}
\end{split}
\tag{20}
$$
两项的 Fourier 条件分别为
$\mathrm N\mathfrak a+4\mathrm N\mathfrak b=n$ 和
$4\mathrm N\mathfrak a+p\mathrm N\mathfrak b=n$；
各原函数因子仍要求 $\bar{\mathfrak p}\nmid\mathfrak a$，
并除以它的实际范数。
这与同映射 R826 的两项卷积不同。

取 Besser 的 Frobenius 相容 proper-cohomology 配对，则
$$
\boxed{
AJ_p(\Delta^{(0,4)}_{j,k})
(\omega_f\otimes\omega_g^{(0)}\otimes\omega_h^{(4)})
=
\frac{\langle\omega_f,[\Xi_{g,h}^{(0,4)}]\rangle_X}
 {1+\bar\pi/\pi^2}.
}
\tag{21}
$$
左侧的全纯三槽正读取(2)的原 $\lambda_\ell$ 分量。
证明与 R826 §5 完全相同，但输入换成(9)、(19)的实际拉回：
卷积多项式为 $1-\varphi/\pi^2$，
且 $\langle\omega_f,\varphi v\rangle=-\bar\pi\langle\omega_f,v\rangle$。
分母的赋值为 $-2$、其逆为2，非零且不能倒置。

所有微分使用 $dQ/Q$，没有附未说明的 $2\pi i$ 或 CM 周期。
若下层单位根基满足
$\langle\eta_g,\omega_g\rangle=\langle\eta_h,\omega_h\rangle=1$，
则所选副本的准确规范是
$$
\eta_g^{(0)}=\frac1{12}q_0^*\eta_g,\qquad
\eta_h^{(4)}=\frac1{12}q_4^*\eta_h.
\tag{22}
$$
映射的 degree12 不可被(9)的4替代，也不可再给(21)除以12。
(5)已定义投影，而(21)测试的是该投影子空间内的实际拉回微分。
改变原函数常数只给全纯类，和 $\omega_f$ 的杯积为零；
cusp 基点变动同样不改变本全纯槽。

交换第二、第三个实际输入及其退化位置，有
$$
\Xi^{(0,4)}_{g,h}+\Xi^{(4,0)}_{h,g}
=d\bigl(G_g(Q)G_h(Q^4)\bigr).
\tag{23}
$$
故全纯槽按应有 Koszul 规则反号。
(23)不把固定 $(0,4)$ 中两种不同有序角色的值相认。

## 8. 已证明的改进与剩余全局门

本篇已经替换了 R829 的必零局部向量，并逐处保留原有限表示。
即使所有固定局部测试均非零，仍不能从(16)推(21)非零：
前者是同一个局部 trilinear functional 的 test-vector 判据，
后者是固定 global diagonal cycle 的指定 $p$-adic regulator。

R826 的复三重积一阶非零仍由原 $\lambda_\ell$ 与三个参考因子给出。
R817 的三个原 fixed canonical cycles 非零、R818 的三条复 rank1、
以及 R811 的 canonical 严格核结论各保持原范围。
本篇没有将这些事实强行转换为(6)与 R814 的比例恒等式；
该全局比较、比例非零以及跨 $p$ AJ 非零仍需实际证明。

尤其(21)的两项完整杯积不能经 ordinary-forms projector删掉第二项。
R826(A5)的 critical cohomology 行在这里仍适用。
它也没有给原 $J_S',J_T',J_U'$ 额外增加一个假定的中央零。

## 9. 原文与固定复现依据

- M. Dimitrov–L. Nyssen, *Test vectors for trilinear forms when at least one
  representation is not supercuspidal*, Manuscripta Math. **133** (2010),
  479–504，Theorem3，§3.4 的完整证明：
  <https://doi.org/10.1007/s00229-010-0382-0>；
  <https://arxiv.org/pdf/1005.0724>。
- D. Prasad, *Trilinear forms for representations of GL(2) and local
  epsilon-factors*, Compositio Math. **75** (1990), 1–46：
  Theorem1.1 的 multiplicity one；Theorem6.1 的 compact-induction；
  §6 equal-conductor case、Proposition6.7。
  <https://www.numdam.org/article/CM_1990__75_1_1_0.pdf>。
- J. A. Green, *The characters of the finite general linear groups*,
  Trans. Amer. Math. Soc. **80** (1955), 402–447。
  本篇(14)–(17)另给 $GL_2$ 所需有限计算的自含形式。
  <https://doi.org/10.1090/S0002-9947-1955-0072878-2>。
- A. Besser, *On the regulator formulas of Bertolini, Darmon and Rotger*,
  Res. Math. Sci. **3** (2016), article26，
  Proposition2.1/2.2、(2.7)、(2.11)–(2.13)、(4.2)–(4.3)：
  <https://link.springer.com/article/10.1186/s40687-016-0073-x>。
- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)、
  [R829](R829-same-degeneracy-diagonal-chow-vanishing.md)：
  原全角色、四槽、完整两项公式与同映射 Chow 零。
- [R818](R818-original-three-weight-four-complex-analytic-rank-one.md)：
  norm-one 生成元、固定系数域嵌入和三原角色标签。
