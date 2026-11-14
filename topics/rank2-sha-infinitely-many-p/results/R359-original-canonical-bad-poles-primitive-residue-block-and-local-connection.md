# R359：原规范坏点后的原始留数块与完整局部连接

日期：2026-11-13。**状态：已证明。** 本篇在 R346 的同一实际留数格中保留原 canonical 的固定坏点，包括公共乘子的 $P_{134}$。相对来源的坏角至多三点；乘回整个 $G_0$ 后至多一百三十七点。相应原留数映射仍有一个明确单位子式；对 R342 的真实接触窗口，仅余至多三十二个高指标方向需要另行处理。并给 R356 规范连接在全部短极部上的整三角式及真正的扭留数余核。没有将扭留数替为原留数，也没有删除原十三行或首次提升 carry。

## 1. 同一个原极代数及规范坏角

固定
$$
p=6s-1>7,\quad p\nmid b,\quad b=17,\quad n_0=3s-1,
$$
系数环是原惰性位的完备离散赋值环 $\mathcal O$，剩余域为 $k$。
R346 的固定椭圆商、变量和真实极代数为
$$
E':Y^2=X^3+b^2,\quad \xi=X^3/b^2,\quad
r=(Y-b)/(Y+b),\quad T_p=Z_p^2,
$$
$$
B_p(\xi)=\sum_{j=0}^{n_0}\binom{n_0}{j}\frac{\xi^j}{6j+1},
\quad \deg B_p=n_0,\quad B_p(0)B_p(-1)\ne0.
\tag{1}
$$
$B_p$ 平方自由。R346 给出了同一特征零多项式
$\widetilde B_p$，首系数为单位且约化为 (1)，
因此
$$
\mathcal A=\mathcal O[\xi]/(\widetilde B_p)
\tag{2}
$$
是有限 étale 代数；需要时将多项式乘首系数的逆使其 monic。
加入 $X^3=b^2\xi$、$Y^2=b^2(1+\xi)$ 仍有限 étale，
而所有 $\xi,1+\xi,X,Y$ 均为单位。

原角变量为 $t=-\xi$。R335、R352 的相对来源
$$
\mathcal V_n=\mathscr R^n
 \frac{(t h_7(t))^{\lfloor(n+1)/4\rfloor}
        (t-1)^{\lfloor(n+1)/3\rfloor}}
      {(1+8t)^{\lfloor n/2\rfloor}}\,
 \mathcal O[t]_{\le e_{n+1}},
\qquad h_7(t)=16t^2+4t+7
\tag{3}
$$
以及 $W=\mathscr R^2t(t-1)^2(1+8t)h_7(t)^2$ 的额外坏角只有
$$
\boxed{F_{\rm rel}(\xi)=(1-8\xi)(16\xi^2-4\xi+7).}
\tag{4}
$$
$t=0,1$ 已由 (1) 排除，不能另扣其行数。

但整个原来源还必须乘回 $G_0=C_{1,0}$。
R335(8) 的固定原分子除 $t,t-1,1+8t,h_7$ 外，真实含有
primitive 多项式 $P_{134}(t)$，次数一百三十四。
所以全来源必须保留
$$
\boxed{F_{\rm full}(\xi)=F_{\rm rel}(\xi)P_{134}(-\xi),\qquad
\deg F_{\rm full}\le137.}
\tag{5}
$$
$P_{134}$ 在每个未倒置的素数处不恒为零，依据正是 R335 的
Gauss content 证明。不能把 (4) 的三点界直接用于整个 $G_0$。

## 2. 保持整性的好坏组件分解

对 (4) 或 (5) 选定 $F$，令
$$
B_{\rm bad}=\gcd(B_p,\bar F),\qquad
B_{\rm good}=B_p/B_{\rm bad},\qquad
d=\deg B_{\rm bad}.
\tag{6}
$$
所有多项式均先取 monic。因为 $B_p$ 平方自由，
$B_{\rm bad},B_{\rm good}$ 互素。
Hensel 分解唯一给
$$
\widetilde B_p=\widetilde B_{\rm bad}\widetilde B_{\rm good},
\qquad
\mathcal A=\mathcal A_{\rm bad}\times\mathcal A_{\rm good},
\quad
\mathcal A_{\rm good}=\mathcal O[\xi]/(\widetilde B_{\rm good}).
\tag{7}
$$
这里没有声称 $\widetilde B_{\rm bad}$ 在特征零必须整除 $F$；
它是由实际模 $p$ 坏纤维确定的 étale 组件。

在相对情形 $d\le3$；在全来源情形 $d\le137$。
好组件的秩准确为 $3s-1-d$。
所有固定 canonical 角因子在好组件上都是单位。
若还要返回 R346 的 genus-two 覆盖
$C:y^2=v^6+b$，加入 $v^2=b/X$ 是另一 étale 二次扩张。
因此这些单位性质在原曲线和所有实际分支上均成立，
没有选择或删除某个共轭分支。

## 3. 原留数在好组件上的明确单位子式

R346 给同一实际微分
$$
\omega_{\boldsymbol q}=
 \left(\sum_{n=1}^{K}q_nT_p^{-3n}\right)d\log r,
\qquad K\le s-1.
\tag{8}
$$
其全部真实特征零留数均整，约化后在 (1) 的极点上恰为
$$
\operatorname{Res}\omega_{\boldsymbol q}
=-6(Y/b)\xi^{-K}P_{\boldsymbol q}(\xi),
$$
$$
P_{\boldsymbol q}=
 \sum_{n=1}^{K}q_nb^n\xi^{K-n}A_n(\xi),\qquad
A_n(0)=1,\quad \deg A_n\le3n-1,
\quad \deg P_{\boldsymbol q}\le3K-1.
\tag{9}
$$
这里的 $A_n$ 是 R346 由原导子递推得到的多项式，不作更换。

**定理一。** 若
$$
\boxed{3K<3s-d,}
\tag{10}
$$
则 (8) 的原留数仅限制到好组件，仍是一个
$p$-饱和单射。更强地，它有一个由原系数坐标给出的单位 $K$ 阶子式，
其约化行列式为
$$
\boxed{b^{K(K+1)/2}.}
\tag{11}
$$

**证明。** (10) 正好是
$\deg P_{\boldsymbol q}<\deg B_{\rm good}$。
先在加入 $X,Y$ 的实际 étale 代数上，把留数乘单位
$-b\xi^K/(6Y)$，再取此六次扩张的迹除以六。
这给一个整线性映射到 $\mathcal A_{\rm good}$，其约化恰为
$P_{\boldsymbol q}$。这里六和所有显示因子都是单位。
若使用 genus-two 覆盖，可再以二次迹除以二返回；仍没有精度损失。

因为 $P_{\boldsymbol q}$ 的次数严格小于 $B_{\rm good}$，
在 $1,\xi,\ldots,\xi^{\deg B_{\rm good}-1}$ 的原整基中不需约化。
取系数行 $0,\ldots,K-1$，将列按 $q_K,q_{K-1},\ldots,q_1$ 排序，
由 (9) 的 $A_n(0)=1$ 得三角矩阵，反次序的对角准确为
$b^K,b^{K-1},\ldots,b$。其模 $p$ 行列式即 (11)。

实际特征零矩阵的这个子式因而为 $\mathcal O$ 单位。
整初等行列变换给一个 $K$ 阶单位块，证明单射与
$p$-饱和性。所有原特征零留数和好坏组件都已保留，
未用任意重选的剩余域模型替代它们。$\square$

相对坏角由 $d\le3$ 得统一范围
$$
\boxed{K\le s-2.}
\tag{12}
$$
完整 $G_0$ 坏角由 $d\le137$ 得统一范围
$$
\boxed{K\le s-46.}
\tag{13}
$$
这些是不依赖 $p$ 的准确固定损失，并非假定所有 $P_{134}$ 根都避开
原测试极。

## 4. 原 C2 接触格只剩至多三十二个高列

对任意原 $K\le s-1$ 令
$$
K_0=\max(0,\min(K,s-46)).
\tag{14}
$$
将 (8) 限制到原子格 $q_{K_0+1}=\cdots=q_K=0$，
按 $K_0$ 使用定理一。这时归一因子用 $\xi^{K_0}$；
由于 $\xi$ 为单位，与全格的定义完全兼容。
得到原好留数矩阵中的 $K_0$ 阶单位块。

因此可作真正整 Schur 消元，保留全部好点及坏点行，使全原矩阵成为
$$
\boxed{
\begin{pmatrix}I_{K_0}&0\\0&\mathscr E\end{pmatrix},
\qquad \mathscr E\text{ 仅有 }K-K_0\text{ 列}.
}
\tag{15}
$$
其中高列在好行和坏行的全部贡献都进入 $\mathscr E$。
这不是把坏行删去后宣称余像为零。R346 对完整留数图的饱和性仍成立；这里没有把它换成原 canonical 矩阵 $M$ 的深 Smith 结论。

R342 真正由两条接触尾产生的上限为 $K=s-14$。
故对其全部允许的 $s>13$，
$$
\boxed{K-K_0\le32.}
\tag{16}
$$
当 $s>46$ 时等于三十二；当 $s\le46$ 时 $K\le32$ 本来就成立。
原中央单独测试若取 $K=s-1$，同理得到至多四十五列，不能把它
与 (16) 的两接触格混同。

若只在相对来源中工作，(12) 已覆盖全部 $K=s-14$，
没有这个固定列损失。返回整个 $G_0$ 时必须改用 (15)–(16)，
并仍保留 R328 的 charge40 与十三行目标运输。

## 5. 原规范连接的短极部整三角式

R356 在同一个原函数域给
$$
DZ_p=1,\qquad
G_\kappa(P)=0,\qquad
G_\kappa=
-\sum_{j=1}^{p-1}\frac{D^{j-1}x(P)}{j!}Z_p^j
\pmod{Z_p^p}
\tag{17}
$$
于全部原测试极 $P$。
Gaussian 重标只加 $-\bar\delta_\kappa Z_p^p$，不改变 (17)。
其特征零有限和提升 $\widetilde G_\kappa$ 在
$\widetilde Z_p=0$ 处仍精确为零，且
$D\widetilde Z_p$ 在这些点为单位。

在任一好组件的实际分支上取 $z_P=\widetilde Z_p$ 为参数，记
$$
a_\kappa(z_P)=\widetilde G_\kappa/(D\widetilde Z_p)
             \in z_P\mathcal O_P[[z_P]].
\tag{18}
$$
$\mathcal O_P$ 可理解为整个有限 étale 分支代数；以下运算均在其上整地进行，
不必选择单个代数闭包点。原 $t$ 导子也满足
$$
\boxed{t\partial_t=-\frac{x}{6y}D,}
\tag{19}
$$
而显示系数在这些点为单位。所有固定角向有理因子在好组件上都是单位，
故其对数导数可用真实整单位换框保留。

对原确定的 sigma 幂 $m\in\mathbf Z$，考察其规范连接部分
$$
\nabla_m f=(\partial_{z_P}f+m a_\kappa f)\,dz_P.
\tag{20}
$$
例如每个整个齐次原来源的 sigma 次数为 $34(n+40)$；
取相反伴随时可将 $m$ 换成其负数。
(20) 只记录这个准确连接部分，原 $U_0$、行移及理性因子仍须一起使用。

令
$$
\mathcal P_M=\bigoplus_{j=1}^{M}\mathcal O_Pz_P^{-j},
\qquad 1\le M<p.
$$
在模去正则项后，(20) 给
$\mathcal P_M\longrightarrow\mathcal P_{M+1}dz_P$。

**定理二。** 此映射整单射且 $p$-饱和，其余核是自由的一维
$\mathcal O_P$ 模。准确余核泛函为
$$
\boxed{\omega\longmapsto
 \operatorname{Res}_{z_P=0}(h_{m,P}\omega),\qquad
 h_{m,P}=\exp\left(m\int_0^{z_P}a_\kappa(u)\,du\right)
             \pmod{z_P^{M+1}}.}
\tag{21}
$$
所用全部低阶分母均为单位；$h_{m,P}(0)=1$，一次项为零。

**证明。** 在原极部基上，
$$
\nabla_m(z_P^{-j})
=-jz_P^{-j-1}dz_P+
           \text{极阶至多 }j-1\text{ 的项}.
\tag{22}
$$
按极阶排列，第 $2,\ldots,M+1$ 行给三角单位块，
对角为 $-1,\ldots,-M$。因为 $M<p$，全部是单位。
这直接证明整单射、饱和性及自由秩一余核。

(18) 从一次项开始，故 (21) 所需积分、指数在该有限范围内只有
$1,\ldots,M$ 作为可能分母。它满足
$h_{m,P}'=m a_\kappa h_{m,P}$ 到所需阶数，
所以
$$
h_{m,P}\nabla_m f=d(h_{m,P}f)
$$
在所有可能影响留数的阶数成立。
于是 (21) 杀掉全部像，而在 $z_P^{-1}dz_P$ 上取一。
和 (22) 的单位块比较，它就是整个自由余核，不遗漏额外极部。$\square$

R346 的原微分极阶至多 $6K<p$。
可取 $M=6K-1$，所以本结论覆盖全部真实接触极部。
各 Gaussian 规范之间的 $Z_p^p$ 差不改变这里使用的短阶
$h_{m,P}$；同一规范的全部低阶系数由 (17) 支付。

## 6. 原留数与扭留数不可混同

定理一使用的是 (8) 的原实际留数。
定理二给的是原连接对应的扭留数 (21)。
两者准确相差
$$
\operatorname{Res}(h_{m,P}\omega)-\operatorname{Res}\omega
=\sum_{j=2}^{M}[z_P^j]h_{m,P}\,
                   [z_P^{-j-1}dz_P]\omega.
\tag{23}
$$
例如由 (17)，
$$
[z_P^2]h_{m,P}\equiv-\frac m2x(P)\pmod p.
\tag{24}
$$
这项通常不为零；“连接在该点的值为零”只消掉一次项，
并不使所有余核泛函等于原留数。
因此不能将定理一的单位 minor 无证套到 (21) 的整个新矩阵。

还有两个原接口必须保持。

第一，R351 的整 Serre 核准确含
$w^{13}\rho^n\Lambda_\lambda(w)\,dw$，其中 $\Lambda_\lambda$ 保
$p^{\lfloor r/s\rfloor}$ 权。$w=Z_p^6$ 时，$w^{13}$ 在每个
非原点测试极同样具有七十八阶零。在原点被记为单位的
$G_0/w^{13}$，不能因此在这些点也当作单位。
R342 的 $K=s-14$ 已在其实际接触公式中付过十三行；
本篇对该接触格使用 (16)，没有再次删除行移或其可能共振。

第二，R356 的原特征零比较还含真正的首次提升余项
$A_\kappa^\circ$。其精确首项修正使用
$\lambda_{\rm lin}=1/(1-3p)$、
$c_{\rm lin}=\sum_{j=1}^{p-1}\lambda_{\rm lin}^j$、
$\eta_{\rm lin}=(c_{\rm lin}+1)/p$；
并非在特征零把 $\lambda_{\rm lin}$ 设成一。
这个同一余项及原 Gaussian $\epsilon$ 项在 R356(29)–(30) 中完整保留。
定理二是已付规范连接在短极部上的整线性事实，不把这些模 $p^2$
项置零。

当前得到的实际推进是：规范坏角及全部分支有明确整分解；
原留数比较可保留一个单位低块和至多三十二个真实高列；
局部伴随的正确余核由 (21) 逐项给出。
下一步须将此扭留数矩阵、原 $A_\kappa^\circ$ 和 R351 的同一可提升左核
作完整比较。尚未由这些局部事实推出原 $C_2$ 消失或中央导数非零。

## 依据

- [R335：整个原导子的整数典范基](R335-full-integral-canonical-conductor-and-exact-relative-source.md)，尤其真实 $P_{134}$ 分子与所有固定角点。
- [R342：原接触格及指定残数](R342-original-gaussian-recalibration-and-miller-adjoint-residue.md)。
- [R346：全部原测试极与原始留数映射](R346-original-off-origin-residue-injection-and-full-cartier-polar-part.md)。
- [R351：整 Serre 伴随及可提升左核](R351-original-canonical-serre-adjoint-and-integral-second-lift-connection.md)。
- [R352：同一次数二微分与真实物理连接](R352-whole-canonical-degree-two-derivation-and-original-moving-poles.md)。
- [R356：准确 Gaussian 规范原函数及保留的首次提升](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)，包括精确线性系数勘误。

本篇为符号证明，无目标素数扫描。执行环境仍不可用时，仅以允许的小文本接口发表；
不把远端同步记作一次本地 git pull。
