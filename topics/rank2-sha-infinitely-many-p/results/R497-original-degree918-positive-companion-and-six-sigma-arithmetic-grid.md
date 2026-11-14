# R497 — 原 degree918 正伴随测试、完整 S 抽取与六 sigma 非零网格

日期：2026-11-14。**状态：已证明。** R493 的实际五 sigma
degree27 来源与剩余一个 sigma，给真正的 $34\boxtimes918$
双输出。六个正伴随矩构成整个第一 principal 格的基；本篇给
一个无常数项的固定有理多项式，完整抽回原 $S$。同一个合法
算术测试在 R493 的原五深一单位网格上仍非零，赋值恰为 $5n$，
且能准确送到真实二挠态 $h$ 的 $W$ 深管。

全部第五阶法向碰撞、正 sigma 矩及 log 加权矩均保留。删去
一个显示固定整数的素因子即可给单位首项，不涉及随 $p$ 增长
的矩阵或数值猜测。完整算术中央中的 $Z$ 外域仍可抵消该小管，
故主目标未完成。

## 1. 真正的 27+1 两输入及全部四个隐藏输出

沿用 R493 的 $b=17$、$\delta,\gamma,\bar\gamma$、同一普通周期
$\Omega$ 和
$$
\lambda=-\bar\pi_0^{-1},\qquad\beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad d=p-1.
\tag{1}
$$
记 $x=\xi_4$，其原测度为 $\nu_\sigma$。其余五个独立 sigma 的
物理输入是
$$
(t_1,t_2,t_3,t_4,t_5)
=(\delta\xi_1,2\delta\xi_2,\gamma\xi_3,c,2d_0).
$$
取
$$
\begin{aligned}
Z&=t_1+t_2+t_3+t_4+t_5,\\
R_1&=4t_1-t_2,\\
R_2&=7(t_1+t_2)-15t_3,\\
R_3&=t_1+t_2+t_3-22t_4,\\
R_4&=4(t_1+t_2+t_3+t_4)-23t_5.
\end{aligned}
\tag{2}
$$
这是 R493(35) 的同一个整单位坐标，Gram 为
$\operatorname{diag}(27,60,2310,506,2484)$。
以下 $\mathbf R=(R_1,\ldots,R_4)$ 一直保留。

原 $Y_s$ 在本篇简记为 $Y$。新的真正正交输出是
$$
\boxed{Y=Z+\bar\gamma x,\qquad T_c=\gamma Z-27x.}
\tag{3}
$$
矩阵、Gram 及反解为
$$
\begin{pmatrix}1&\bar\gamma\\\gamma&-27\end{pmatrix},
\qquad\operatorname{diag}(34,918),\qquad\det=-34,
$$
$$
\boxed{Z=(27Y+\bar\gamma T_c)/34,\qquad
x=(\gamma Y-T_c)/34.}
\tag{4}
$$
它们与 $\mathbf R$ 全正交；两个奇半特征在每个新轴上成对
抵消，故新两轴是无 twist 的标准偶 theta 格。

将 $\mathbf R$ 忘却后，完整生成函数准确是
$$
\boxed{
F_b(y,t)=B_{27,b}(y+\gamma t)\,
          \sigma_b(\bar\gamma y-27t)
\in\mathcal S_{34}\boxtimes\mathcal S_{918},
}
\tag{5}
$$
其中
$$
B_{27,b}=S_b/\sigma_b(\bar\gamma z)
=-\frac1{84}\sigma_b(\delta z)\sigma_b(2\delta z)
 \sigma_b(\gamma z)\sigma_b(z)\sigma_b(2z).
\tag{6}
$$
第一来源 $F_b(y,0)$ 恰为 $S_b$，没有额外周期或尺度常数。
(5) 只用于计算纯 $T_c$ 测试；附 $\mathbf R$ 条件时使用下一节
同一个原六输入的完整核心。

## 2. 真实 Tc 核和四伴随共同核心

R493 的 whole odd degree27 锚已经给
$$
\nu_{\mathrm{five}}|_{Z\in p\mathbf Z_p}
=\beta[\kappa,I_4]_*\nu_{\mathrm{five}},
\tag{7}
$$
保全部 $\mathbf R$。原独立 sigma 同样有 core $\beta$。
另一方面 whole $K_{34}=R_Y$ 已由 R443 的完整中心与实际锚定标。
因为 (3) 在当前普通处是整自同构，两原输入同时深和 $Y,T_c$
同时深是同一事件。两种完整限制比较，准确得
$$
\boxed{
\nu_{\Phi}|_{T_c\in p\mathbf Z_p}
=\lambda[I_Y,\kappa,I_4]_*\nu_{R_Y\Phi}.
}
\tag{8}
$$
这里 $\Phi$ 表示 (2)、(3) 的原完整六输入，$R_Y$ 只反射第一
输出，其余五个输出保留。具体地，$Z,x$ 的同时深标量是
$\beta^2=\lambda^2$；先用 $Y$ 的 $\lambda R_Y$ 核，再取消
$\lambda[\kappa,I]$ 的整推前，便是 (8)。没有猜新的符号。

原五个 sigma 同时深的标量是 $\beta^5$；(2) 将其准确变成
$Z,\mathbf R$ 同时深。与 (7) 比较并取消共同 $Z$ 核，得到
$$
\boxed{
\nu_\Phi|_{\mathbf R\in(p\mathbf Z_p)^4}
=\lambda^4[I_Y,I_{T_c},\kappa I_4]_*\nu_\Phi .
}
\tag{9}
$$
(8)、(9) 都保完整来源及其他输出，因而可附所有未改变坐标的
连续测试和实际紧开条件。

## 3. 全六维来源格的精确正伴随矩阵

对 $0\le k\le6$ 定义
$$
F_{k,b}(y)=(6k)![t^{6k}]F_b(y,t).
$$
它就是实际测试 $(T_c/\Omega)^{6k}$ 后的第一来源。原共同
$\mu_6$ 型为零，所以每个 $F_{k,b}$ 都在六维 principal 格中，
且准确写成
$$
\boxed{F_{k,b}(y)=\sigma_b(y)^{34}
 \sum_{a=0}^5 M_{ak}\,b^{k+4-a}x_b(y)^{2+3a}.}
\tag{10}
$$

以下给出矩阵的完整有限规则。先令 $b=1,w=z^6$，写
$x=z^{-2}B(w)$、$\sigma=zA(w)$。
原 Weierstrass 方程和 sigma 规范给
$$
q_0=1,\quad q_1=-1/7,\quad
q_n=\frac{\sum_{i=1}^{n-1}q_iq_{n-i}}{(6n+1)(n-1)},
$$
$$
B(w)=\sum q_nw^n,\qquad
\log A(w)=-\sum_{n\ge1}\frac{q_nw^n}{6n(6n-1)}.
\tag{11}
$$
置
$$
(p_0,\ldots,p_4)=(-128/7,-80/7,-12/7,-53/7,1),
$$
$$
\mathcal S(w)=A(w)^{34}\sum_{a=0}^4p_aw^{4-a}B(w)^{2+3a},
\qquad
\mathcal H(w)=\frac{\mathcal S(w)}{A(\bar\gamma^6w)}.
\tag{12}
$$
于是 $S=z^6\mathcal S(z^6)$、
$B_{27}=\bar\gamma^{-1}z^5\mathcal H(z^6)$。
写 $a_i=[w^i]A$、$h_j=[w^j]\mathcal H$。

第一格的完整 Taylor 基坐标为
$$
\mathsf J_{\ell a}
=[w^{\ell-5+a}]A^{34}B^{2+3a},\qquad0\le\ell,a\le5.
\tag{13}
$$
负下标系数为零，$\det\mathsf J=-1$。
(5) 的准确对应坐标是
$$
\boxed{
\mathsf V_{\ell k}
=(6k)!\gamma^{6k}
\sum_{i+j=k+\ell-1}a_i h_j\bar\gamma^{6i}
 \sum_r\binom{1+6i}{r}\binom{5+6j}{6k-r}
                 \frac{(-27)^r}{7^r},
\qquad M=\mathsf J^{-1}\mathsf V .
}
\tag{14}
$$
越界二项系数为零。(11)–(14) 只需 $0\le n\le11$ 的有理或
$K$ 系数。因整个来源已在六维格内，(13) 的六个精确坐标确实
决定整条函数，不是把未知函数的有限 jet 相合当作全局证明。

准确有 $M_{[:,0]}=(p_0,\ldots,p_4,0)^t$。
令 $M_+=M_{[:,1:7]}$；其行列式模 $101$ 为
$$
\boxed{\det M_+\equiv17+17\delta\pmod{101}.}
\tag{15}
$$
范数模 $101$ 为 $45\ne0$，故这是一个严格的特征零满秩证书。
所有特征零系数均完整保存在附 JSON；不是对目标普通素数的扫描。

### 3.1 六个固定有理系数及完整 S 来源

出乎只看矩阵系数的表象，唯一解 $M_+\boldsymbol c=(p_0,\ldots,p_4,0)^t$
全部在 $\mathbf Q$。给出其完整整数规范。令
$$
L=43024169751465478338233979150199956512749200351148033743183443885006289024867517102817280,
\tag{16}
$$
$$
\begin{aligned}
N_1={}&-669434980352778043509581310714866556317857825822326580693089728706624639467520,\\
N_2={}&-119981363974691021171554991621708858631413799763774609514070383001600,\\
N_3={}&-55342492105213394108340720066257765863550432453355110400,\\
N_4={}&-42045915630443092877608745094656489256652800,\\
N_5={}&5620340233791194124683811078144,\\
N_6={}&1075621969600983023.
\end{aligned}
\tag{17}
$$
置 $c_k=N_k/L$。精确矩阵运算给
$$
\boxed{M_+(c_1,\ldots,c_6)^t=(p_0,\ldots,p_4,0)^t.}
\tag{18}
$$
因此无常数项的固定多项式
$$
\boxed{\mathfrak h_b(t)=\sum_{k=1}^6c_kb^{-k}t^{6k}}
\tag{19}
$$
完整抽回原来源：
$$
\boxed{
(Y)_*\{\mathfrak h_b(T_c/\Omega)\nu_\Phi\}=\nu_S.
}
\tag{20}
$$
这是真正的全部第一测度身份，包含非单位部分及全部第一测试。

## 4. 完整算术行、Tc 单位和四个原伴随深度

每条 (10) 的第一来源都为型零，所以 $R_YF_{k,b}=F_{k,b}$。
由 (8)，限制 $T_c$ 单位会乘因子
$1-\lambda\kappa^{6k}$。定义
$$
\boxed{
\mathfrak h_{b,p}^{\times}(t)
=\sum_{k=1}^6
\frac{c_kb^{-k}}{1-\lambda\kappa^{6k}}t^{6k}.
}
\tag{21}
$$
所有新增分母是单位，与 (19) 的系数差在 $p^6\mathcal O$。
准确有
$$
\boxed{
(Y)_*\{{\bf1}_{T_c\ {\rm unit}}\,
\mathfrak h_{b,p}^{\times}(T_c/\Omega)\nu_\Phi\}=\nu_S.
}
\tag{22}
$$
再用 (9)，对任意 $r\ge0$，同一实际来源给
$$
\boxed{
\int_{\mathbf R\in(p^r\mathbf Z_p)^4,\ T_c\ {\rm unit},\ Y\ {\rm unit}}
\langle Y\rangle^{du}\mathfrak h_{b,p}^{\times}(T_c/\Omega)
\,d\nu_\Phi
=\lambda^{4r}J_S(u).
}
\tag{23}
$$
所以 $J'_S(0)=0$ 确实消掉这些完整条件行；没有改变第一 Mellin
权，也没有把第二轴测试误当成独立算术输入。

## 5. 同一个合法测试在原五深一单位网格上的完整第五阶

保 R493 的实际独立域
$$
\mathcal D_n=\{x\ {\rm unit},\
 \xi_1,\xi_2,\xi_3,c,d_0\in p^n\mathbf Z_p\}
=\{Z,\mathbf R\in p^n,\ x\ {\rm unit}\},\qquad n\ge1.
\tag{24}
$$
在此域 $Y$、$T_c$ 均为单位。先对固定 (19) 定义
$$
\mathcal A(T)=d\int_{x\ {\rm unit}}\int
 \log\langle\bar\gamma x+TZ\rangle\,
 \mathfrak h_b\!\left(\frac{\gamma TZ-27x}{\Omega}\right)
\,d\nu_{B_{27}}(Z)d\nu_\sigma(x).
\tag{25}
$$
五个原 sigma 的同时深 core，或 (7)、(9) 的完整比较，给该
小管中央准确为
$$
\boxed{\mathcal C_n=\beta^{5n}\mathcal A(\kappa^n).}
\tag{26}
$$

R493(34) 给 $\mu_5(B_{27})=120\Omega^5/\bar\gamma$、
$\mu_j=0$ 对 $0\le j<5$。对 $m=6k$ 定义
$$
A_k=\gamma^5\sum_{a=1}^5
 \frac{(-1)^{a-1}}{a7^a}\binom{6k}{5-a}(-27)^{6k-5+a},
$$
$$
B_k=\gamma^5\binom{6k}{5}(-27)^{6k-5}.
\tag{27}
$$
这里字母 $B_k$ 是显示常数，不是来源 $B_{27}$。
写
$$
I_m=\int_{x\ {\rm unit}}x^m\,d\nu_\sigma,\qquad
I_{m,\log}=\int_{x\ {\rm unit}}x^m\log\langle x\rangle\,d\nu_\sigma.
$$
完整第五阶为
$$
\boxed{
[T^5]\mathcal A=
\frac{120d}{\bar\gamma}
\sum_{k=1}^6 c_kb^{-k}\Omega^{5-6k}
\{A_k I_{6k-5}+B_k[I_{6k-5,\log}
                 +\log\langle\bar\gamma\rangle I_{6k-5}]\}.
}
\tag{28}
$$
这保了 log 与测试的全部法向碰撞，尤其没有漏掉
$\log\langle\bar\gamma\rangle$。所有矩指数
$1,7,13,19,25,31$ 都为正。

原 sigma 核心给
$$
I_{6k-5}=(1-\beta\kappa^{6k-5})(6k-5)!
             b^{k-1}a_{k-1}\Omega^{6k-5}.
\tag{29}
$$
两个 log 因子均在 $p\mathcal O$ 中。因此在显示系数都整的素数处，
$$
\boxed{[T^5]\mathcal A\equiv(d/b)\alpha\pmod p,}
\tag{30}
$$
其中固定代数数为
$$
\alpha=\frac{120}{\bar\gamma}
\sum_{k=1}^6 c_k A_k(6k-5)!a_{k-1}
=\frac{A+B\delta}{D},
\tag{31}
$$
$$
\begin{aligned}
A={}&1440935741522357826619235140107022805303896592950241958401828702957725824129,\\
B={}&-1813765269049121739800435840694154580102806900217087779806497668058675862540,\\
D={}&178000081118033421953983855808692884462466015608355923166875641368652904792064.
\end{aligned}
\tag{32}
$$
特别 $\alpha\ne0$，这是完整特征零计算。

固定排除
$$
\boxed{\mathcal E=\{p:p\mid17LD(A^2+3B^2)\}.}
\tag{33}
$$
所有整数已显示，不需要其素因子分解。删除有限集合后，当前固定
无限 ray 仍有无穷多个普通素数；(19) 系数整且 $\alpha$ 为单位。

低于第五阶的项全部由 $B_{27}$ 的矩消失。对总 $Z$ 次数 $r$
的高项，测试次数只有三十六，可能的 log 分母是
$r-j$，$0\le j\le36,r-j\ge1$；log 常数项没有该分母。
所有单位上的正负矩仍整，故
$$
v_p([T^r]\mathcal A)\ge-\lfloor\log_pr\rfloor.
\tag{34}
$$
对 $p\ge71,n\ge1,r>5$，$rn-\lfloor\log_pr\rfloor>5n$。
结合 (30) 得
$$
\boxed{v_p(\mathcal C_n)=5n,\qquad\mathcal C_n\ne0.}
\tag{35}
$$
(21) 与 (19) 相差 $p^6$，按同一完整展开，单位第五阶不变，
全尾界也不变。因此 (35) 对实际合法单位测试 (21) 同样成立，
记其值为 $\mathcal C_n^\times$。

## 6. 原算术中央的一条准确补域

令
$$
\Gamma_n=\{\mathbf R\in(p^n\mathbf Z_p)^4,\ T_c\ {\rm unit},\
 Y\ {\rm unit}\}.
$$
由 (4)，若 $Z\in p^n$ 则 $Y$ 单位恰使 $x$ 单位，且 $T_c$
自动为单位。故有真实不交分拆
$$
\boxed{\Gamma_n=\mathcal D_n\sqcup\mathcal B_n,\qquad
\mathcal B_n=\{\mathbf R\in(p^n)^4,\ T_c,Y\ {\rm unit},\
 Z\notin p^n\},\quad Z=(27Y+\bar\gamma T_c)/34.}
\tag{36}
$$
(23) 给
$$
\boxed{
\lambda^{4n}J'_S(0)=\mathcal C_n^\times+
 \int_{\mathcal B_n}d\log\langle Y\rangle\,
       \mathfrak h_{b,p}^{\times}(T_c/\Omega)\,d\nu_\Phi .
}
\tag{37}
$$
小管项已严格非零，但外域仍保全部 $Z,x,Y$ 单位或相消分支。
$J'_S(0)=0$ 只使外域等于其负值，没有被 (35) 排除。

## 7. 保 Y 的 T 把同一个算术测试送到原 h 的 W 深管

R493 的 $\mathcal T$ 满足
$Y\mathcal T=Y$、$h=\omega^2\mathcal T_*\rho_0$。
因此整条 (20)–(23)、(36)–(37) 都有准确的 $h$ 版本。
其实际测试和条件是
$$
T_c^{\mathcal T}=T_c\circ\mathcal T^{-1}
=\gamma Y-34\ell_4,\qquad
\mathbf R^{\mathcal T}=\mathbf R\circ\mathcal T^{-1}.
\tag{38}
$$
这些全部为真正 $Y$ 伴随，故原第一 Mellin 权原样保持。
特别
$$
\int_{\mathcal T\Gamma_n}
d\log\langle Y\rangle\,
 \mathfrak h_{b,p}^{\times}(T_c^{\mathcal T}/\Omega)\,dh
=\omega^2\lambda^{4n}J'_S(0),
\tag{39}
$$
而其中的真实小管 $\mathcal E_n=\mathcal T\mathcal D_n$ 满足
$W\in p^n$，同一合法测试的中央为
$\omega^2\mathcal C_n^\times$，赋值恰为 $5n$。
这里不再把 R493 的 $\ell_4^6$ 直接当成已知算术条件零；
测试已完整换成 (38) 的正次数纯伴随多项式。

仍须明确，$\mathbf R^{\mathcal T},T_c^{\mathcal T}$ 是 $Y$
伴随，通常不是 $W$ 伴随。原 $W$ core 的物理参数 $s$ 将它们
准确改为
$$
\begin{aligned}
Y&\longmapsto Y+\frac{s-1}{72}(37-3\delta)W,\\
T_c^{\mathcal T}&\longmapsto
 T_c^{\mathcal T}+\frac{s-1}{72}\gamma(37-3\delta)W,\\
\mathbf R^{\mathcal T}&\longmapsto
 \mathbf R^{\mathcal T}+\frac{s-1}{72}
 (12+8\delta,\ 6+74\delta,\ -40+20\delta,\ -68-12\delta)^tW.
\end{aligned}
\tag{40}
$$
其中 $s=\kappa^r$ 用于深度 $r$。脚本按原五输入 Gram 逐项验证
所有四个非零系数。R493 的 $W$ 伴随深度框架在小管上与
(24) 等价，但在外域 (36) 中不能直接互换。(40) 的全部移动
条件与 (37) 的补域正是余下需要控制的内容。

## 证书与依赖

- [完整六维矩阵、六个有理测试、全部第五阶项和域转置脚本](../scripts/check-r497-degree918-positive-companion-test.py)；
  [特征零精确数据](../scripts/check-r497-degree918-positive-companion-test.json)。
- [R493：真实六 sigma 因式、T 与 degree27 完整原核](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R443：whole degree34 的真实 Y 反射核心](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R455：六维 theta 格与正伴随测试的原规范](R455-original-pure-companion-test-and-slope-core-arithmetic-return.md)。

