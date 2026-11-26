# R1052：原完整 CM 轮廓与实际最低系数泛函

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route / o1_theta / root，
最低留数式另由 o2_high_coefficient 独立核对。

**已证明：R1044/R1046 原系数旗标中的全部三角系数，由同一个实际
CM 参数变换明确给出。** 本文保持原曲线、原中心点、全部 full-level
分支、两个 $p\bmod12$ 行的实际好因子，以及所有节点和参数单位。
证明直接约束实际微分在原 full node 的每一 normal 层，不假设更早
CM 层已经为零。完整 source 坐标比较也在含幂零元的 $R/(p)$ 上支付。

指定实际 Mordell–Weil 消去行的最低系数，遂成为下面的明确留数。
本文尚未证明该值恒非零，也未排除原深盘的全部非中心根；
Serre 主目标仍 OPEN。

## 1. 同一原对象和记号

设
$$
p=6N+5\ge41,\qquad m=(p-1)/2,\qquad
\ell=(p+1)/3=2N+2,
$$
$$
e_{\rm full}=p^2-1,\quad \varpi^{e_{\rm full}}=p,\quad
\pi_0=\varpi^2,\quad e_0=m(p+1),\quad
\varepsilon=\pi_0^m,\quad\varepsilon^{p+1}=p.
\tag{1052.1}
$$
原 $X_1,c_1$、最低型 $e_1$ 和 $S=\{A=0\}$ 沿 R1032–1040。
$p\equiv5\bmod12$ 时始终在实际 Raynaud 好部分 $B$ 中取微分，
再经原饱和注入使用；不声称整个 Jacobian 好约化。

令 $\Omega_L$ 为原整 $e_1$ Hodge 微分，底向量
$L=\sum_{s\in S}L_s\omega_s$。原中心首层为
$$
\varepsilon R_L(b)\,db,\qquad
R_L(b)=\frac2m\sum_{s\in S}\frac{L_s\theta_s}{(b-s)^2}.
$$
定义一个确切 primitive
$$
S_L(b)=-\frac2m\sum_{s\in S}\frac{L_s\theta_s}{b-s},
\qquad S_L'=R_L.
\tag{1052.2}
$$
R1032/R1039 的中心惯性计算，在任何 CM 归纳之前就给：
每个实际 Igusa 中心的最低可能层是 $m$，后继只能是
$m+j(p+1)$、$j\ge0$。因此其 generic valuation 满足
$$
v_I(\Omega_L)\ge m\quad(\pi_0\text{ 计}),
\qquad v_I(\Omega_L)\ge2m\quad(\varpi\text{ 计}).
\tag{1052.3}
$$
这里不要求 $\pi_0^{-m}\Omega_L$ 在整个节点局部环整。

保留 R1050 的实际 $B_{\rm CM}$：
$$
r=1-b^3,\quad
q(r)={}_2F_1(5/6,5/6;4/3;r),\quad
j(r)={}_2F_1(1/2,1/2;2/3;r),
$$
$$
Z=-\frac r3\left(\frac{q(r)}{j(r)}\right)^3,\qquad
b=B_{\rm CM}(Z),\qquad
B_{\rm CM}(Z)=1+Z+\frac5{16}Z^2+\cdots .
\tag{1052.4}
$$
只使用已付的次数 $\le\ell$，不会经过首个坏分母。
原 target 单位仍是 $\kappa_1=d^3c_Q^3$。
对 $1\le k\le\ell-1$ 置
$$
q_k(L)=[Z^k]\bigl(S_L(B_{\rm CM}(Z))-S_L(1)\bigr),
\qquad n_k=\ell-k.
\tag{1052.5}
$$

## 2. 同一个实际 full node

在当前 CM 尾的一个 ordinary 节点，取 R1021 的原 level 参数：
$a=T(v)$ 对应该支的 connected 直线，$y=T(Q)$ 对应另一条
étale 方向。这里 $a$ 是本节的 full-level 参数，
不是后文原 coarse source 函数；两者不混用。
其余 $p$ 条 $\mathbf F_p$ 直线的 $T(w)/y$ 都是单位。
Drinfeld 的完整乘积给
$$
p=U\,a^{p-1}y^{p(p-1)},\qquad U\text{ 为单位}.
$$
在原固定 Weil 分支取 $(p-1)$ 次单位根后，
$$
a y^p=u\,\varpi^{p+1}.
$$
置 $z_{\rm node}=\varpi/y$，于是
$a/y=u z_{\rm node}^{p+1}$。
在同一个 blowup chart 上，$a/y$ 为 transverse coordinate；
隐函数定理将它解成 $z_{\rm node}^{p+1}$ 乘单位。
原 $a,y$ 是正则参数，因此正规化后的实际节点环为
$$
R[[y,z_{\rm node}]]/(y z_{\rm node}-\varpi),
\qquad z_{\rm node}=1/\beta,\quad \beta=y/\varpi.
\tag{1052.6}
$$
这来自原 $T(v),T(Q)$，没有另选一个便利但未识别的 coarse 节点标架。
被开出的 $(p-1)$ 次单位根保留原 Weil 分支常数；
后文的 full-branch 运输不将各支单位独立改成一。

## 3. 中心赋值直接约束所有 CM normal 层

在 (1052.6) 写
$$
\Omega_L=f\,d\log y.
$$
$f$ 在实际节点环整。其规范 Laurent 分解为
$$
f=\sum_{a\ge0}c_a(\varpi)z_{\rm node}^a
  +\sum_{b\ge1}d_b(\varpi)y^b.
\tag{1052.7}
$$
在中心侧用 $z_{\rm node}=\varpi/y$；不同 $y$ 的 Laurent 指数
不能互相抵消。(1052.3) 因而逐系数给
$$
v_\varpi(c_a)+a\ge2m,\qquad v_\varpi(d_b)\ge2m.
\tag{1052.8}
$$
在尾侧用 $y=\varpi/z_{\rm node}$。若第 $i$ 个
$\varpi$-normal 层出现 $z_{\rm node}^{-q}dz_{\rm node}$，
则准确满足
$$
\boxed{\quad i-(q-1)\ge2m.\quad}
\tag{1052.9}
$$
特别地，第 $j=(3k+1)m$ 个 $\pi_0$-normal 层，在每个 full
ordinary 无穷点的极阶至多
$$
2j-2m+1=6km+1.
\tag{1052.10}
$$
原微分在 full affine tail 上正则，所以没有其它极点。

这个估计作用于实际全层：中心 smooth deformation、其它 CM 尾返回、
当前 CM 尾已经存在的主部以及 holomorphic 自由项都包括在内。
它不以先前 CM coefficient 为零为条件。

对节点单项 $\varpi^a y^b z_{\rm node}^c$，
尾极阶缺陷为
$$
(q-1)-i=-(a+c).
$$
达到 (1052.10) 的最高极阶，当且仅当该项来自中心赋值恰为
$2m$ 的首层。更高中心层严格降低极阶。
此前 CM 负主部和中心首层是同一个 overlap 的两个表达，
不能再作为一份独立的 self-return 加回去。

## 4. 真实整有限角消去所有同层低极部

令 $E=e_1$ 为 R1030/R1039 的实际整 finite corner。
R1021 在整个 $R/(p)$（包括 base nilpotents）上给 full affine
常数模型和原常线性 level 作用，所以 $E$ 与本篇各 normal 层相容。

在每个原分支
$$
C=X^pY-XY^p=c_0\ne0
$$
使用 R1044 的同一个
$$
\eta=dX/X^p=dY/Y^p,\qquad
\operatorname{div}_\infty(\eta)=(p-2)\sum_\infty[\infty].
$$
由 (1052.10)，第 $(3k+1)m$ 层 $\Omega_k/\eta$ 的各无穷极阶
至多
$$
D_k=6km+p-1=(3k+1)(p-1).
\tag{1052.11}
$$
R1044/R1046 的光滑平面 exact sequence 给总次数 $\le D_k$
的真实 polynomial representative。固定分支的 $\mu_{p+1}$
平均、用 $C/c_0$ 齐次化以及完整
$\mu_{p^2-1}$ 分支运输，将它变成同一个 degree $D_k$ source，
在全部实际分支上同时表示原微分。

这里
$$
D_k\le(p-1)^2<p^2-1.
$$
消费 R1044/R1046 已证明的完整 $C$-kernel filtration，
$$
\dim E\operatorname{Sym}^{D_k}=1,
$$
其真实非零生成元是 $dH_k/\eta$。$H_k$ 沿用原规范
$$
F=UV^{p-2},\quad
\Theta=X^p\partial_X+Y^p\partial_Y,\quad
a_k=\frac{(-1)^{3k-3}(3k-1)!}{2},
\quad H_k=a_k^{-1}\Theta^{3k-3}F.
\tag{1052.12}
$$
因此实际全层必为 $dH_k$ 的唯一标量倍数。
任何同层、同来源、$E$-固定且最高极部为零的差都为零。
这一步包含全部低极部和全纯自由项，没有预先假设原层有多项式
primitive。两行中所有分支、$p5$ 的两个无穷端和原交换符号
均继续使用 R1044/R1046 的实际运输。

## 5. 原 target 参数决定准确最高系数

原 full Cohen 模型上的 framing 作用给 $T$ 权一、
target $u'$ 权 $p-1$。
在取 Weil 分支之前，当前 ordinary DVR 上纯 $y$ 项只有相应
次数模 $e_{\rm full}$；有限 framing 可运输 Weil 分支，
不被误说成逐点稳定某一正规化节点。
Drinfeld 单位的纯 $y$ 部分仅含 $y^{j e_{\rm full}}$；
开单位根后保留原常数，首个非恒定修正仍是这个次数。
所以在同一个原中心重叠，
$$
u'=c_Q y^{p-1}+O(y^{p-1+e_{\rm full}}).
\tag{1052.13}
$$
R1050 已证明实际 Hodge graph 的 $\Xi=d u'$ 到所需短 PD 精度，
并将立方误差支付到 $(u')^{p+4}$。
由于
$$
e_{\rm full}=6m\ell,
$$
在本篇全部 $k\le\ell-1$ 的范围，原 coarse $b$ 准确为
$$
b=B_{\rm CM}(\kappa_1 y^{6m})
       \pmod{y^{6m(\ell+1)}}.
\tag{1052.14}
$$
没有未定 pure-center 单位的低项；$\kappa_1$ 仍是原单位。

由 (1052.2)、(1052.5)，中心 $\varepsilon dS_L$ 的
$y^{6mk-1}dy$ 系数是 $6mk\,\kappa_1^k q_k(L)\varepsilon$。
代 $y=\varpi/z_{\rm node}$，在第 $(3k+1)m$ 个
$\pi_0$-normal 层得到最高极部
$$
-6mk\,\kappa_1^k q_k(L)
 z_{\rm node}^{-6mk-1}dz_{\rm node}.
\tag{1052.15}
$$

比较原 $H_k$ 时也必须保实际 basis。
R1018 (1018.16) 的同一个 trace-zero basis 是
$$
A_0=\beta+s\alpha,\qquad B_0=\beta-s\alpha.
$$
当前节点为 connected $\alpha=0$、étale $\beta$，所以
$A_0/\beta,B_0/\beta\to1$，
$V/\beta^2\to1$、$U/\beta^{p+1}\to1$。
原 $F$ 的最高项遂准确为 $\beta^{3(p-1)}$，系数一。
沿曲线 $\eta=d\beta/\beta^p$，所以
$\Theta=\beta^p d/d\beta$。
第 $j$ 次作用的最高系数是 $(j+3)(p-1)=-(j+3)$，
正是 (1052.12) 的 $a_k$。故
$$
H_k=z_{\rm node}^{-6mk}+\text{较低极阶项}
\tag{1052.16}
$$
在这个指定原节点成立，没有吸收另一个未知方向常数。
$p5$ 的另一端仍保留原 $(\pm1)^k$ 运输，不另作归一。

由 §4 的一维实际图像，得到对所有 $L$ 的准确全层等式
$$
\boxed{\quad
(\Omega_L)_{(3k+1)m}
=\kappa_1^k q_k(L)\,dH_k,\qquad1\le k\le\ell-1 .
\quad}
\tag{1052.17}
$$
$6mk$ 是单位，故最高系数比较合法。
这不是只在 R1044 的消去旗标子空间上成立的等式。

## 6. 原 source 坐标在整个非约化底上的比较

原 coarse source 函数记作 $a_{\rm src}$，以避免与 §2 level
参数混同。它就是此前各结果的 $a$。
原整盘参数为
$$
z_{\rm src}=\frac{a_{\rm src}-1}{\varpi^{3p(p-1)}},
\qquad w=\frac{a_{\rm src}-1}{p^3},
\qquad z_{\rm src}=\varepsilon^3w.
\tag{1052.18}
$$
只知道特殊尾上的一次项不足以确定全部轮廓；
这里另支付高 $\pi_0$、低 $t$ 的坐标修正。

取 R1021 的同一 source framing-eigenparameter $u_s$。
它的权是 $1-p$，最小非负总次数为
$$
r_0=p(p-1),\qquad r_0\equiv1-p\pmod{p^2-1}.
$$
实际 Cohen 代表因而仅含总次数 $r_0+j e_{\rm full}$。
代原 level 参数 $T(P)=\varpi X,T(Q)=\varpi Y$ 后，
$$
u_s/\varpi^{r_0}=U_{r_0}(X,Y)+pR.
$$
R378 的同一 source leading Dickson 比较识别
$U_{r_0}=c_D\mathcal D$。两边在 R1021 的常数 affine 模型中
无 base-nilpotent 系数，故这个特殊纤维 polynomial 身份同样给整个
$R/(p)$ 上的身份。

实际 CM lift 的 $\mathcal O_K$ 作用在 $p$-divisible group 上连续扩成
$\mathcal O_K\otimes\mathbf Z_p=\mathbf Z_{p^2}$。
因此该 lift 被整 $\mu_{p^2-1}$ framing 固定；
$u_s$ 的非平凡角色迫
$$
u_s(c_1)=0
$$
准确成立。原 coarse 关系遂为
$$
a_{\rm src}-1=A_{\rm src}(u_s^3),\qquad
A_{\rm src}(0)=0,\quad A_{\rm src}'(0)\in R^\times.
$$
这里 $A_{\rm src}$ 的系数在 $W(k)$：$a_{\rm src}$ 属于原未分歧 fine 模问题，$u_s$ 也在该底上作 tame 平均。因此 (1052.19) 的单位没有未定的 base-nilpotent 系数。
它没有一个未付清的 $p$ 倍常数平移。
除去 $\varpi^{3r_0}$ 后，所有 $A_{\rm src}$ 的次数 $\ge2$ 项
都含 $\varpi^{3r_0}\in(p)$。因此在整个非约化 affine 底上
$$
z_{\rm src}\equiv\lambda_D\mathcal D^3\pmod p .
\tag{1052.19}
$$
source 尺度是 $\varepsilon^p$，target 尺度是 $\varepsilon$；
source 的这些非线性项落入 $p$，target 的 $B_{\rm CM}$ 项则须保留。

R378 的准确 Dickson 公式在原 $Q$ 点给
$$
\mathcal D=-c^{p-2}V\bigl(1+O(V^{p+1})\bigr),\qquad t=V^3 .
$$
所以
$$
z_{\rm src}=\lambda_0t\bigl(1+O(t^\ell)\bigr)+pR(t)
\tag{1052.20}
$$
为整个所需 $R/(p)$ 精度的比较；$\lambda_0$ 正是原单位。
它不是只在 reduced tail 上的公式。

不能将 (1052.20) 直接除 $\varepsilon^3$ 后当作 $w$ 的模 $p$
公式。正确误差控制如下。两源参数的一次导数都是单位，
形式逆函数定理使相应 $t$ 代换的差
$\delta(t)\in pR[[t]]$。
R1032/R1039 的实际最早 normal 层给
$\Omega_L\in\varepsilon^4R[[t]]dt$。
对任一 primitive 单项，用整恒等式
$$
\frac{(t+\delta)^n-t^n}{n}
=\sum_{k=1}^n\binom{n-1}{k-1}\frac{\delta^k}{k}t^{n-k}.
\tag{1052.21}
$$
因为 $k-v_p(k)\ge1$，每项都含 $p$。
即使 $\delta(0)\ne0$，它属于 $pR$，固定 $t$ 次数时的无穷和
仍 $p$-adic 收敛。故整个 primitive 的变化属于
$p\varepsilon^4R[[t]]$；减去实际 $c_1$ 常数仍保此界。
除 $p\varepsilon$ 后余在 $\varepsilon^3R$，
不改变实际未分歧系数的约化。
这个论证包含 $p$ 倍积分次数，没有把 $p/\varepsilon^3$ 偷换成 $p$。

## 7. 原完整 $w$ 多项式

R1044/R1046 的原参考多项式在 $Q$ 满足
$$
H_k(t)=c_k t^{n_k}+O(t^{n_k+\ell}),\qquad
c_k=\frac{(2\sqrt{A_{\rm tail}})^{3k-2}}{3k-1}.
\tag{1052.22}
$$
低于 $\ell$ 只有这一项：在原 $\Theta$ 展开中其它项的
$t$ 次数相差 $\ell$。全部 $c_k$ 都是单位。
(1052.20) 的非线性 $O(t^{\ell+1})$ 也不会混合这些次数。

使用原准确 $z_{\rm src}=\varepsilon^3w$ 和
$$
(3k+1)+3(\ell-k)=p+2,\qquad\varepsilon^{p+2}=p\varepsilon,
$$
(1052.17) 给
$$
\boxed{\quad
\overline{H_L}(w)=
\sum_{k=1}^{\ell-1}
 \kappa_1^k c_k\lambda_0^{-n_k}q_k(L)w^{n_k},
\qquad
H_L=\frac1{p\varepsilon}\int_{c_1}^{P(w)}\Omega_L .
\quad}
\tag{1052.23}
$$
所有其它次数、全部 $p$ 倍积分分母及原 formal-log 的非线性项，
继续消费 R1033/R1039 已付的完整尾界；
实际系数属于 $W(k)$，约化次数至多 $\ell-1$。
每个保留次数的惯性指定唯一的 normal 层，
更高同角色层相差 $e_0$，不改变 (1052.23)。

令
$$
C_{\rm vec}(b)=\sum_{s\in S}\frac{e_s}{b-s},\qquad
e_s=\theta_sf_s,\quad
\langle e_s,\Omega_L\rangle=-2L_s\theta_s.
$$
由 (1052.2)，原规范 Lie-valued Abel log 的全部列准确为
$$
\boxed{\quad
V_{\ell-k}=
 \frac{\kappa_1^k c_k\lambda_0^{-(\ell-k)}}m
 [Z^k]C_{\rm vec}(B_{\rm CM}(Z)).
\quad}
\tag{1052.24}
$$
展开 $B_{\rm CM}=1+Z+\cdots$，其对角项就是 R1044/R1046 的
$(-1)^kJ_{k-1}$；原旗标的全部先前列系数现在也已确定。

对任何原行 $c$，仍用 R1037/R1040 的 coefficient-fixed 插值多项式
$T_c$，$\deg T_c<\deg A$。原配对给
$$
B(c,C_{\rm vec}(b))=-\frac{T_c(b)}{2A(b)}.
$$
因此
$$
\boxed{\quad
\overline h_c(w)=
-\sum_{k=1}^{\ell-1}
 \frac{\kappa_1^k c_k\lambda_0^{-(\ell-k)}}{2m}
 [Z^k]\left(\frac{T_c}{A}\right)(B_{\rm CM}(Z))
 w^{\ell-k}.
\quad}
\tag{1052.25}
$$
本式特别适用于实际
$c=D\overline{\mathsf Q}(1-\overline{\mathsf Q})\lambda$，
不丢 $\overline{\mathsf Q}^{\,2}$，不替换成任意核行或参考 bare 系数。

## 8. 最低列的严格 Lagrange 留数

定义
$$
\mathcal C_{\rm CM}(T)
=[Z^{\ell-1}](T/A)(B_{\rm CM}(Z)).
$$
原 Hasse 多项式在安全截断范围满足
$$
A(b)=A(1)bq(r),\qquad b=(1-r)^{1/3}.
$$
两个原 period 的 Wronskian 给
$$
\left(r^{1/3}q/j\right)'
=\frac13 r^{-2/3}(1-r)^{-4/3}j^{-2}.
$$
从
$$
\mathcal C_{\rm CM}(T)
=\operatorname{Res}_{r=0}
 (T/A)\frac{Z'(r)}{Z(r)^\ell}\,dr
$$
直接代入 (1052.4)，利用 $3\ell=p+1$、$\ell$ 为偶数，
并在所需次数 $\ell-1<p$ 内使用
$(j/q)^p\equiv1\bmod r^p$，得到
$$
\boxed{\quad
\mathcal C_{\rm CM}(T)=
-\frac{3^{\ell-1}}{A(1)}
 [r^{\ell-1}]
 \frac{T((1-r)^{1/3})}{(1-r)^{5/3}j(r)^3}.
\quad}
\tag{1052.26}
$$
$j$ 的首次分母共振是次数 $\ell$；
上式仅读到 $\ell-1$，全部分母为单位。
它保留完整 $T$，不是只取它的最高项。

还可用同一个实际 principal-part source 表达。
设
$$
L_{\rm CM}(b)=
 \operatorname{PP}_{b=1}\left(Z_b'(b)/Z(b)^\ell\right).
\tag{1052.27}
$$
因为 $Z_b'/Z^\ell=(Z^{1-\ell})'/(1-\ell)$，
它没有简单极部；只含 $(b-1)^{-2},\ldots,(b-1)^{-\ell}$，
且在无穷远为 $O(b^{-2})$。
对 $T_c/A$ 使用完整留数定理，
$$
\boxed{\quad
\mathcal C_{\rm CM}(T_c)
=-\sum_{s\in S}\frac{T_c(s)L_{\rm CM}(s)}{A'(s)}
=2B(c,L_{\rm CM}).
\quad}
\tag{1052.28}
$$
最后一个 $L_{\rm CM}$ 指其在 $S$ 上的同一插值类；
没有在其它点省掉留数。

原实际 MW 消去行的准确最低读数遂为
$$
\boxed{\quad
\mathcal C_{\rm CM}
 (T_{D\overline{\mathsf Q}(1-\overline{\mathsf Q})\lambda})
=2B\bigl((1-\overline{\mathsf Q})\lambda,
               \overline{\mathsf Q}D L_{\rm CM}\bigr).
\quad}
\tag{1052.29}
$$
它在 (1052.25) 中只再乘一个已经明确且非零的原单位。
自伴性给这个等式；没有将 $D\overline{\mathsf Q}$ 与
$\overline{\mathsf Q}D$ 擅自交换，也没有删去真实返回项。

## 9. 已闭合的接口与仍须继续的原问题

本文将先前“模前列”的旗标提升为原实际完整多项式。
新的输入是实际 full node 的双分量赋值、
同一 target 参数的全所需截断、
以及整个非约化 source 坐标和积分误差控制。
它们合在一起处理全部节点反馈和坐标混合。

R1045–1047 已知实际完整消去轮廓非零并给公共零点数界；
本文进一步给其每一个系数和最低读数的明确公式。
仍须证明 (1052.29) 的指定值非零，或用完整多行关系排除原
正赋值深盘的非中心点。任意 inverse-period 系数、原 $f_N$、
核范数与这个实际读数尚不能自动等同。
O0 的完整全局覆盖仍须另行完成，不能由本局部接口代替。

## 来源

- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)，
  原 trace-zero basis (1018.16)、$\psi^3$ 的准确 ordinary 首系数。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)，
  同一 full-level Cohen 参数、framing 权、整个非约化 affine 模型及 target 参数。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)、
  [R1039](R1039-original-p5-complete-CM-normal-jet-and-rational-disc-scale.md)，
  原中心完整首层/最低角色、实际早于 $4m$ 消失，p5 双中心及全阶零环带留数。
- [R1044](R1044-original-CM-disc-complete-coefficient-flag.md)、
  [R1046](R1046-original-p5-complete-CM-flag-and-MW-nonzero-reduction.md)，
  同一全部分支、$\eta$、真实整角、完整齐次过滤、原 $H_k$ 与两端尺度。
- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md) §§2–4、
  [R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)，
  更正后保留的原 source 参数、Dickson 公式及全 $p$ 倍积分尾界；
  不恢复 R378 已撤回的秩零商身份。
- [R1050](R1050-actual-CM-parameter-short-PD-and-Picard-Fuchs.md)，
  同一实际 target Hodge graph、短 PD 自然性和全部所需 Picard–Fuchs 精度。
- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)、
  [R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md)，
  两行原实际 $\mathsf Q,B,D,T_c$。

global_route 给出完整全层推导；o1_theta 独核实际 node、source
framing 与非约化精度，root 逐项核对 full-node 阶数、准确 $\beta$
首系数、source/target 区别、全部 primitive 代换误差及配对。
最低留数由 o2_high_coefficient 独立核对。
全文为纸面证明，无数学程序执行。
