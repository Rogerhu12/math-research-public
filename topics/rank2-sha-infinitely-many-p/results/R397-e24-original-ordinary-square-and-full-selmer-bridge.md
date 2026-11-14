# R397 — E24 实际六项来源的普通中央平方与完整 Selmer 桥

日期：2026-11-14。**状态：下述同一个固定来源的普通整测度、全部周期和 Euler 因子、整条反圆平方、通常 Selmer 下界及有限证书已证明。主目标的跨素数非零仍未证明。**

## 1. 固定曲线、真实来源及结论

固定
$
 E_{24}:y^2=x^3+24,\qquad K=\mathbf Q(\delta),\quad
 \delta=\sqrt{-3},\quad\omega=(-1+\delta)/2.
$
R387 已证明 $E_{24}(\mathbf Q)_{\rm tors}=0$ 和
$r:=\operatorname{rank}E_{24}(\mathbf Q)\ge2$。本文不预设 $r=2$。
固定微分 $dz=dx/(2y)$，取
$x=z^{-2}+\cdots,\ y=-z^{-3}+\cdots,\ \sigma=z+\cdots$。

R389、R391、R393 已付本曲线的实际 Hecke 特征 $\psi$、导子
$\mathfrak f=(8\delta^4)$、原两处 Schwartz 向量、全权复平方及 degree72。
R395 将原十八项运输完整压缩成六个真实有限阶 Heisenberg 平移，
其中所有 Weyl 中心和相位均保留。本文使用 R395 的固定归一化
$
 \Phi(z)=G_{24}(z)=\frac{S_{24,\Lambda}(z/\Omega)}{\kappa_0 A}
        =\sigma(z)^{72}P_{11}(x(z)^3)=\sum_{m\ge0}s_mz^m.
 \tag{1}
$
这里 $\Omega=\Omega_{24}>0$ 满足
$\operatorname{Per}(E_{24},dz)=\Omega\Lambda$，
$\Lambda=\mathbf Z+s\mathbf Z=s\mathcal O_K$，
$s=(1-\omega)^{-1}$。常数 $\kappa_0\ne0$ 是 E−8 的实际 ground theta 质量，
$A=1+\zeta_9^4+\zeta_9^5$，且 $A^2=f_1$。
式 (1) 的六项定义独立于这些分析常数：对
$K_8(z)=\sigma(3z)/(3\sigma(z))$，将 $K_8(3z)$ 按 R395 的六个
$E[9]$ 点及原有限阶 lift 平移，系数为 $1,\omega,\omega^2$。
所以 $\Phi$ 在一个固定数域 $F$ 上定义，$\Phi\ne0$，
$P_{11}\in F[X]$，且 $s_m=0$ 除非 $6\mid m$。
其原质量为零，不在此预付 $s_6\ne0$。

R395 的原九阶有限 theta lift 保持每个好 $p>3$ 的整模型，
所以 $P_{11}$ 在这些素数的每个指定完成处整。
具体地，按极阶下降读取 $1,X,\ldots,X^{11}$ 的系数，
各最高 Laurent 系数都是一，故不会因选此基再引入分母。
以下固定
$
 p>7,\qquad p\equiv1\pmod3
 \tag{2}
$
及一个 $F\hookrightarrow\overline{\mathbf Q}_p$ 嵌入。
这是本曲线的一组固定好普通素数，不依赖权 $m$。
记 $R_p$ 为相容普通正式群周期与 $F$ 生成的完备整数环。
所有赋值都规范为 $v_p(p)=1$。

存在单位普通周期 $\Omega_p$，使
$
 \Phi(\Omega_p\log(1+Z))
 =\int_{\mathbf Z_p}(1+Z)^x\,d\nu_p(x)\in R_p[[Z]],
 \quad
 M_{p,m}:=\int x^m\,d\nu_p=\Omega_p^m m!s_m.
 \tag{3}
$
定义同一测度的单位 principal Mellin 变换
$
 G_p(T)=\int_{\mathbf Z_p^\times}
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu_p(x).
 \tag{4}
$
置固定非零代数数
$
 \kappa_{24}=\frac{L(E_{-8},1)}{6\Omega},\qquad
 E_{-8}:y^2=x^3-8 .
 \tag{5}
$
以下证明其代数性，不把分析周期商未经证明地视为代数数。
实际 Katz 分支在 §3–4 的相容规范下满足
$
 \boxed{\mathcal K_{24,p}(T)=
 \frac{\kappa_{24}}s\Omega_p
 (1+T)^{-a_{72,p}}G_p(T)^2,\quad
 a_{72,p}=\frac{\log_p\langle72\rangle}{\log_p(1+p)}.}
 \tag{6}
$
记 $r_p=\operatorname{corank}_{\mathbf Z_p}
\Sha(E_{24}/\mathbf Q)[p^\infty]$。则
$
 \boxed{G_p\ne0,\quad G_p(0)=0,\quad
 r+r_p\le\operatorname{ord}_0\mathcal K_{24,p}
       =2\operatorname{ord}_0G_p.}
 \tag{7}
$
因此
$
 \boxed{G_p'(0)\ne0\ \Longrightarrow\
 r=2\ \text{且}\ \Sha(E_{24}/\mathbf Q)[p^\infty]\text{有限}.}
 \tag{8}
$
对这个同一固定代数级数，还有完整有限证书
$
 \boxed{G_p'(0)\ne0\ \Longleftrightarrow\
 \exists n\ge0:\ 
 v_p\!\left(((p-1)p^n)!\,s_{(p-1)p^n}\right)<2n+2.}
 \tag{9}
$
本篇不声称 (8) 的逆命题，也不声称 (9) 已对无穷个素数命中。

## 2. 普通 sigma、整性与阶乘

令 $t=-x/y$、$D_E=d/dz$。Mazur–Tate 普通 sigma 的唯一性，
以 Mazur–Stein–Tate Theorem 1.3 的表述，给唯一奇整级数
$\Sigma_p=t+\cdots$ 和 $c_p\in\mathbf Z_p$，满足
$
 D_E^2\log\Sigma_p=-x-c_p. \tag{10}
$
因 $p\equiv1\pmod3$，$\omega\in\mathbf Z_p$。真实 CM 自同构有
$t([\omega]P)=\omega t(P)$、$x([\omega]P)=\omega x(P)$。
将 $\Sigma_p(t)$ 换成 $\omega^{-1}\Sigma_p(\omega t)$，
链式法则将 (10) 的常数变为 $\omega^2c_p$；
奇性、整性和首项不变，所以唯一性给 $c_p=\omega^2c_p=0$。
同一特征零微分方程及奇首项规范于是给
$
 \Sigma_p(t)=\sigma(\log_Et)\in t\mathbf Z_p[[t]]. \tag{11}
$

式 (1) 每项 $\Sigma_p^{72}x^{3j}$ 的 $t$-阶为
$72-6j\ge6$（$0\le j\le11$）。由 (2)，它们的系数均整，
故 $\Phi(\log_Et)\in t^6R_p[[t]]$。
在完备最大不分歧整环上取相容高度一正式群同构
$\beta:\widehat{\mathbf G}_m\to\widehat E_{24}$，以
$\beta^*dz=\Omega_p\,dZ/(1+Z)$ 定义单位 $\Omega_p$。
则 $\log_E\beta(Z)=\Omega_p\log(1+Z)$，
Amice 对应给 (3) 的同一有界整测度。
展开指数生成函数给准确矩 $\Omega_p^m m!s_m$；
没有删去任何阶乘，也没有另加 $p$-依赖 Gaussian。

## 3. 原 Hermite 变量、实际周期与固定常数

R393 的原尺度为
$
 c=\frac{\sqrt{3\sqrt3}}{72\pi i},\qquad
 \mathcal B_{\rm raw}(U)=S_{24,\Lambda}(cU).
$
由 (1)，归一化后
$
 \mathcal B(U):=\frac{\mathcal B_{\rm raw}(U)}{\kappa_0A}
   =\Phi(\Omega cU)=\sum_{m\ge0}\frac{b_m}{m!}U^m,
 \quad b_m=(\Omega c)^m m!s_m. \tag{12}
$
特别这里是 $\Omega c$，不是 $c/\Omega$。

R393 的全部有限范数为 $54f_1$，无穷范数为
$m!/(4\pi)^m/\sqrt{6\sqrt3}$，原 Yang 常数为
$\pi\sqrt{6\sqrt3}/(324\sqrt3 f_1)$。
R395 由真实 E−8 ground 源证明
$C_{24}\kappa_0^2=L(E_{-8},1)/(6f_1)$ 和 $A^2=f_1$。
于是对每个 $6\mid m$，完整平方恰为
$
 L(\psi^{2m+1},m+1)
 =\frac{L(E_{-8},1)}6\,\frac{(4\pi)^m}{m!}\,b_m^2.
 \tag{13}
$
这一步消去的是已经算出的 $f_1=A^2$，不把未知逐权重单位吸入平方根。
R395 的 ground theta 非零同时给 $L(E_{-8},1)\ne0$。

由 $4\pi c^2=-\sqrt3/(432\pi)$ 及 $6\mid m$，(12)–(13) 给
$
 \frac{(2\pi/\sqrt3)^mL(\psi^{2m+1},m+1)}
      {m!\Omega^{2m+1}}
 =\kappa_{24}\,216^{-m}s_m^2. \tag{14}
$
Katz 的晶格生成周期为 $\Omega_\infty=s\Omega$，
$\operatorname{Per}(E_{24},dz)=\Omega_\infty\mathcal O_K$。
因 $s^2=-\omega^2/3$，在 $6\mid m$ 时 $s^{2m}=3^{-m}$。
所以准确换算是
$
 \boxed{\mathcal E_m:=
 \frac{(2\pi/\sqrt3)^mL(\psi^{2m+1},m+1)}
      {m!\Omega_\infty^{2m+1}}
 =\frac{\kappa_{24}}s\,72^{-m}s_m^2.}
 \tag{15}
$
实尺度给 $216^{-m}$，CM 晶格尺度给 $72^{-m}$；
同时必须保留固定 $s^{-1}=1-\omega$。

由 $\Phi\ne0$ 且 $\Phi(0)=0$，存在某个 $m_*>0$、$6\mid m_*$，
使 $s_{m_*}\in F^\times$。CM 临界值的代数性给
$\mathcal E_{m_*}\in\overline{\mathbf Q}$；(13) 使其非零。
于是
$
 \kappa_{24}=s\,72^{m_*}\mathcal E_{m_*}/s_{m_*}^2
 \in\overline{\mathbf Q}^{\times}. \tag{16}
$
可扩大固定数域 $F$ 包含它。
这不要求预先识别首个非零系数，也不要求 $\kappa_{24}$ 在每个 $p$ 为单位；
中心零阶只需要它非零。

周期规范使用 de Shalit 的晶格周期。
若另用 $\Omega_K=(2\pi i)^{-1}\int dz$，必须先换算
$\Omega_\infty=2\pi i\Omega_K$；Castella–Wan Remark 2.2
明确给出此区别。不能把 $2\pi i$ 当成代数单位处理。

## 4. 实际插值、两个 Euler 因子及整条平方

固定 $\pi=\psi(\mathfrak p)$、$\bar\pi=\psi(\bar{\mathfrak p})$，
$v_p(\pi)=1,\ v_p(\bar\pi)=0,\ \pi\bar\pi=p$。令
$
 \epsilon_m=\psi^{m+1}\bar\psi^{-m}
            =\psi^{2m+1}\mathrm N^{-m}. \tag{17}
$
其 infinity type 为 $(m+1,-m)$。
R389 已支付 $\psi$ 在二、三处的完整角色，包括
$\chi_3(\delta)=i$ 的 uniformizer 值；对 $6\mid m$，
$\epsilon_m$ 的导子仍准确为 $\mathfrak f=(8\delta^4)$。
局部扭转的根单位不可只在单位群上消去而漏掉 uniformizer。
又 $\psi\bar\psi=\mathrm N$，所以在同一全部 Euler 乘积中
$
 L(\epsilon_m^{-1},0)=L(\bar\epsilon_m,1)
                    =L(\psi^{2m+1},m+1). \tag{18}
$

用 $\Omega_\infty=s\Omega$ 及相容 $\Omega_p$ 的 Katz/de Shalit 规范，
沿固定分支先扭转实际 $\psi_p$，再沿
$\langle\psi_p/\bar\psi_p\rangle$ 推前。取非零切向权参数 $T$，
使 $t_m=(1+p)^m-1$。对正的 $p-1\mid m$，
Katz 插值给
$
 \mathcal K_{24,p}(t_m)=
 \Omega_p^{2m+1}m!\,
 \frac{(2\pi/\sqrt3)^m}{\Omega_\infty^{2m+1}}
 \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2
 L(\psi^{2m+1},m+1). \tag{19}
$
有限导子版本见 Agboola–Howard Theorem 2.1.1；
晶格周期及 $(k,j)=(m+1,-m)$ 的明确归一见
Castella–Wan Remark 2.2、Theorem 2.4。
本篇只用后者的 Katz 插值，不使用该文非 CM supersingular 主定理。

两个 Euler 因子分别为
$
 1-\epsilon_m(\mathfrak p)/p
 =1-\epsilon_m^{-1}(\bar{\mathfrak p})
 =1-\pi^m/\bar\pi^{m+1}. \tag{20}
$
代数字符在 $p$ 上未分歧，故相应 Gauss 因子为一；
导子恰等于 $\mathfrak f$，没有额外坏位删除因子。
对偶或 Artin 反演约定须同时作
$T\mapsto(1+T)^{-1}-1$，不逐权重改选单位。
与通常单 CM Selmer 对偶相容的分支，正是 (19) 的共轭相容版本；
复共轭交换 CM 分量，(18) 保持全部 L 值和中心零阶。

代入 (3)、(15)，恰得
$
 \mathcal K_{24,p}(t_m)
 =\frac{\kappa_{24}}s\Omega_p\,72^{-m}
   \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2M_{p,m}^2.
 \tag{21}
$
一个阶乘来自 Katz，另一个来自复平方，合成 $(m!s_m)^2$。

整测度给
$
 v_p\!\left(M_{p,m}-\int_{\mathbf Z_p^\times}x^m\,d\nu_p\right)\ge m .
 \tag{22}
$
Euler 因子与一的差也有至少 $m$ 的赋值。
固定 $p-1\mid m_0\ge0$，取
$m_j=m_0+(p-1)p^j$。
它实趋于无穷而 $p$-adic 趋于 $m_0$，故 (21) 的非单位和
Euler 误差都趋于零，单位矩趋于 $G_p(t_{m_0})$，
$72^{-m_j}\to\langle72\rangle^{-m_0}$。
因此 (6) 在这些全部权点成立。取互异权点趋于零，
解析恒等定理证明整条 (6)。

总质量 $\Phi(0)=0$ 尚不单独给单位质量 $G_p(0)=0$；
下一节由通常 Selmer 真正证明它。

## 5. 完整通常 Selmer 与原 Sha

### 5.1 具体主猜想假设

$K$ 的类数一由 Minkowski 界
$(2/\pi)\sqrt3<2$ 得到。
$E_{24}/K$ 具有全部最大整环 CM；本篇 $p>7$ 是好普通素数。
R389 在二、三处给 $\epsilon_2=1,\epsilon_3=-i$，
其余有限处为一；同一原无限型的 $\epsilon_\infty=i$。
改变全局加性角色为其二分之一不改变总根数，
故完整乘积为 $W(E_{24})=1$。
其 ray class 次数准确为
$
 [K(\mathfrak f):K]
 =\frac{5184}{6}\left(1-\frac14\right)
                  \left(1-\frac13\right)=432. \tag{23}
$
根单位中只有一同余于一模 $\mathfrak f$，所以分母六准确。
所有 $p>3$ 均不整除 432。

Agboola–Howard Theorem 2.4.17(1)(b),(c) 因此适用：
反圆 $\mathbf Z_p$-扩张 $D_\infty/K$ 上的通常单 CM 初级
Selmer 对偶 $X(D_\infty)$ 是 torsion Iwasawa 模，
其特征理想由该 Katz 分支生成。
所用对象是通常 $X$，不是严格局部条件的 $X_{\rm str}$。
原文 Remark 1.1.8 的对偶作用若与权参数反向，须同时反演；
该坐标变换导数非零，不改变中心零阶。

若使用带辅助理想的 Coleman 定义，可取 $(5)$。
$5$ 在 $K$ 惰性，$E_{24}/\mathbf F_5$ 的迹为零，
所以 $\psi((5))=-5$、$\mathrm N(5)=25$；
辅助因子的中心值为 $-30$，在本篇范围是单位。
Theorem 2.1.1 与 Proposition 2.3.4 的整条测度比较因此不会在中心
加零；不以逐个插值点的任意单位代替这个比较。
于是 $\mathcal K_{24,p}\ne0$，且
$
 \operatorname{ord}_0\operatorname{char}X(D_\infty)
 =\operatorname{ord}_0\mathcal K_{24,p}. \tag{24}
$
这里没有高度非退化或全 Sha 有限的前提。

### 5.2 基层通常 Selmer 的限制单射

记 $S_K^\pi=\operatorname{Sel}_{\pi^\infty}(E_{24}/K)$，
$S_{D_\infty}^\pi$ 同理，全部地方使用通常 Kummer 局部条件。
限制给
$
 S_K^\pi\longrightarrow
 (S_{D_\infty}^\pi)^{\operatorname{Gal}(D_\infty/K)}. \tag{25}
$
这是单射：在 $\mathfrak p$ 处，CM 的 $\pi$ 分量为高度一连通正式群；
非零一阶挠点的 tame inertia 角色像的阶为 $p-1$。
pro-$p$ 扩张不能使它平凡，故
$E_{24}(D_\infty)[\pi]=0$，进而全部 $\pi$-初级挠子为零。
全局 inflation–restriction 的限制核遂为零，
而每个局部 Kummer 像在限制下保留。共轭分量完全相同。

取 Pontryagin 对偶并有理化，得
$
 \operatorname{corank}_{\mathbf Z_p} S_K^\pi
 \le\dim_{\mathbf Q_p}
    (X(D_\infty)/TX(D_\infty))\otimes\mathbf Q_p
 \le\operatorname{ord}_0\mathcal K_{24,p}. \tag{26}
$
第二步只用初等 torsion Iwasawa 模论：在高度一素理想 $(T)$
局部化后，块 $A/(T^{e_i})$ 的中心维数为一，特征阶为 $e_i$；
求和得到不等式，有限模及别的支撑不贡献。
非零切向重参数不改变零阶。

### 5.3 两个 CM 分量与整个有理 p-初级

有理三次同源
$
 E_{24}\longrightarrow E':Y^2=X^3-648
$
的目标正是 $E_{24}^{(-3)}$；其与对偶复合为 $[3]$。
因 $p>7$，它们在全 $p^\infty$ Galois 模、全部局部 Kummer 像
和通常 Selmer 群上给同构。
又 $K/\mathbf Q$ 次数二，限制与核心限制给
$
 \operatorname{Sel}_{p^\infty}(E_{24}/K)
 \simeq \operatorname{Sel}_{p^\infty}(E_{24}/\mathbf Q)
       \oplus
       \operatorname{Sel}_{p^\infty}(E_{24}^{(-3)}/\mathbf Q).
 \tag{27}
$
两项余秩均为 $r+r_p$。
另一方面 $\mathcal O_K\otimes\mathbf Z_p=\mathbf Z_p\oplus\mathbf Z_p$
把左边分成两个 CM 初级部分，复共轭交换它们，故两部分余秩相同。
所以准确地
$
 \boxed{\operatorname{corank}_{\mathbf Z_p}S_K^\pi=r+r_p.} \tag{28}
$
这里未把 $E(K)$ 的秩 $2r$ 误放进单 CM 分量，
也未删任何潜在 Sha 自由方向。

(6)、(24)、(26)、(28) 联立给 (7)。
因 $r\ge2$，$\mathcal K_{24,p}$ 的中央阶至少二，
所以同一 $G_p(0)=0$；$\mathcal K_{24,p}\ne0$ 给 $G_p\ne0$。
若 $G_p'(0)\ne0$，右边阶恰二，故 $r=2,r_p=0$。
通常 Selmer 有限余生成，其 Sha 商也有限余生成，
余秩零等价于该 $p$-初级有限。这证明 (8)。

## 6. 原固定系数的有限证书与准确边界

令 $m_n=(p-1)p^n$、$t_n=(1+p)^{m_n}-1$、
$h_m=m!s_m\in F$。由 (22)，
$
 \Omega_p^{m_n}h_{m_n}=G_p(t_n)+e_n,\qquad
 v_p(e_n)\ge m_n,\qquad v_p(t_n)=n+1. \tag{29}
$
最后一个等式由提升指数公式。
若 $G_p'(0)=0$，(7) 和整性给 $G_p\in T^2R_p[[T]]$，
所以 $v_p(G_p(t_n))\ge2n+2$。
因 $m_n\ge2n+2$ 且 $\Omega_p$ 为单位，
所有 $n$ 都有 $v_p(h_{m_n})\ge2n+2$。

反之若 $G_p'(0)\ne0$，取 $n+1>v_p(G_p'(0))$，
其线性项赋值为 $n+1+v_p(G_p'(0))<2n+2$，
高项赋值至少 $2n+2$。再增大 $n$ 后，(29) 的误差不能取消首项。
这证明 (9)，并给实际极限
$
 G_p'(0)=\lim_{n\to\infty}
 \frac{\Omega_p^{m_n}h_{m_n}}{(1+p)^{m_n}-1}. \tag{30}
$
周期只作为单位进入，所以有限证书无需知道其数值。

R395 进一步给
$
 \Phi(z)=\sigma^{72}XQ_4(X)R_6(X),\quad X=x^3,\quad\deg R_6\le6,
$
其中
$Q_4=(X+96)(X^3-2304X^2+27648X+884736)$。
这些是同一个实际来源的固定因子，可直接用于研究 (9)。
整个来源在模 $p$ 的 primitive 性、六个不同有限 theta 特征、
固定三挠除子以及分支非恒零，均不单独计算 $G_p'(0)$。

当前所余正是：对无穷不同的普通素数，证明这个同一固定来源的 (9)
命中；或把它与已有固定 rank-two 曲线的完整中央行建立足够的真实关系，
使同一无穷素数集合上至少一条非零。
有限个素数证书、不同 theta 子域非零或另一个辅助来源的非零，
均不能替代此项。

## 已出版输入与仓库依赖

- A. Agboola、B. Howard，
  *Anticyclotomic Iwasawa theory of CM elliptic curves*，
  Ann. Inst. Fourier **56** (2006)，1001–1048；
  Theorem 2.1.1、Proposition 2.3.4、
  Theorem 2.4.17(1)(b),(c)、Remark 1.1.8：
  [出版全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- F. Castella、X. Wan，
  *Perrin-Riou's main conjecture for elliptic curves at supersingular primes*，
  Math. Ann. **389** (2024)，2595–2636；
  Remark 2.2、Theorem 2.4 的周期与 Katz 插值：
  [出版全文](https://web.math.ucsb.edu/~castella/Perrin-Riou-print.pdf)。
- B. Mazur、W. Stein、J. Tate，
  *Computation of p-Adic Heights and Log Convergence*，
  Documenta Mathematica Extra Volume Coates (2006)，Theorem 1.3：
  [作者出版稿](https://www.wstein.org/papers/pheight/pheight.pdf)。
- E. de Shalit，*Iwasawa Theory of Elliptic Curves with Complex Multiplication*，
  Academic Press (1987)，II.4.14；有限导子 Katz 规范同上述已出版表述。
- R387：固定 E24 的秩至少二与无挠证书。
  R389：本曲线的原局部角色、导子、根数和 Hermitian 类。
  R391、R393：两处原 Schwartz 向量、真正 degree72 与全权复平方。
  [R395](R395-e24-six-actual-translates-fixed-divisor-and-square-normalization.md)：
  同一六项代数/整来源、固定因子及准确平方归一。
  [R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)：
  旧 E17 来源的对应桥梁；本文重新支付新曲线的 72、432、r≥2 和原常数。
