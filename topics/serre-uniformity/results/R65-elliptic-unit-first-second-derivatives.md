# R65：用椭圆单位及至多二阶导数构造单素数 Selmer 类

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的生成公式；主目标仍未解决。** 对 R60 的固定
$A:y^2=x^3-x$、$p>37$、$p\equiv3\bmod4$，给出一个模 $p$ 非零的
Robert 椭圆单位基类。每个 $q\equiv-1\bmod4p$ 对应的唯一归一化
单素数类 $c_q$，在一阶导数不退化时由该导数构造；
若它退化，则加入一个可搜索的辅助素数，用同一原始族的二阶导数
构造。最后的 $p$ 处校正和下降到 $\mathbb Q$ 都明确写出。

这里的结果是有限代数生成公式。它没有计算具体 $p,q$ 的巨大根式展开，
也不把修改 Selmer 条件反推为实际非 CM 同余曲线。

## 1. 基域、系数与正确的单位分量

保留
$$
K=\mathbb Q(i),\quad \mathcal O=\mathbb Z_p[i],\quad
\mathbb F=\mathcal O/p\mathcal O=\mathbb F_{p^2},\quad
V=A[p],\quad T=\mathbb Q(A[p]).
$$
$V$ 在 $G_K$ 上是一维 $\mathbb F$ 表示；记其特征为
$\rho:G_K\to\mathbb F^\times$。R60 给
$$
C=\operatorname{Gal}(T/K)=\mathbb F^\times,\qquad
\operatorname{Gal}(T/\mathbb Q)=C\rtimes\langle\tau\rangle,
\quad \tau a\tau^{-1}=a^p.
\tag{65.1}
$$
在系数 $\mathbb F$ 上也以 $\overline a=a^p$ 记共轭；
$\tau(i)=-i$。

记
$$
\omega=\rho^{p+1},\qquad \chi_0=\rho^p,\qquad \chi=\widetilde{\chi_0},
\tag{65.2}
$$
其中 $\omega$ 是模 $p$ 圆分特征在 $C$ 上的限制，
$\widetilde{\rho^p}:C\to\mathcal O^\times$ 是 Teichmüller 提升。
$\chi$ 忠实，且 $\chi_0=\rho^p\ne\omega$。取幂等元
$$
e_\chi=\frac1{|C|}\sum_{\sigma\in C}\chi(\sigma)^{-1}\sigma.
$$

对任意 $\mathbb Z_p[C]$ 模 $D$，$\chi$ 分量均指
$e_\chi(D\otimes_{\mathbb Z_p}\mathcal O)$，或其模 $p$ 版本。
Kummer 数据对应 $V$ 的准确方式是
$$
H^1(T,V)\simeq
(T^\times/T^{\times p})\otimes_{\mathbb F_p}V(-1).
\tag{65.3}
$$
$V(-1)$ 的 $C$ 特征为 $\rho^{-p}=\chi_0^{-1}$，所以所需
根式正是 $\chi_0$ 分量，而不是无扭曲的不变单位。

选定 $V(-1)$ 的一个 $\mathbb F$ 基后，(65.3) 及
$p\nmid|C|$ 给规范线性识别
$$
\mathcal K:
\bigl((T^\times/T^{\times p})\otimes_{\mathbb F_p}\mathbb F
\bigr)^{\chi_0}
\xrightarrow{\ \sim\ }H^1(K,V).
\tag{65.4}
$$
式 (65.4) 中的右边用限制到 $T$ 后再取 $C$ 不变量理解；
$H^1(C,V)=H^2(C,V)=0$ 证明下降的存在和唯一性。
以下把 Kummer 乘法群模 $p$ 写成加法空间。

$\chi$ 这里只是有限 Cartan 作用的提升。本文没有把
$\mathcal O(\chi^{-1}\chi_{\rm cyc})$ 当作实际的 $T_pA$；
$A$ 在 $p$ 的通常 Kummer 条件始终由 $A$ 自己的形式群定义。

## 2. 零 Selmer 群、局部 $2,p$ 条件与 core rank

### 2.1 在 $K$ 上通常的 Selmer 群也为零

R50 证明 $\operatorname{Sel}_p(A/\mathbb Q)=0$。
因为 $[K:\mathbb Q]=2$ 与 $p$ 互素，限制和余限制将
$\operatorname{Sel}_p(A/K)$ 分解成正、负两个 $\tau$ 分量。
它们分别对应 $A/\mathbb Q$ 及其 $-1$ 二次扭曲的 Selmer 群。
该扭曲的短 Weierstrass 方程仍是
$y^2=x^3-x$，故两群都为零。因此
$$\boxed{\operatorname{Sel}_p(A/K)=0.} \tag{65.5}$$
这里用的是保持各处 Kummer 条件的标准二次下降，而非仅全局
上同调维数的比较。

### 2.2 二进局部上同调为零

$K_2/\mathbb Q_2$ 全分歧，剩余域仍为 $\mathbb F_2$。
$A$ 有潜在好约化。在 $K_2$，形式群为 pro-$2$ 群；
约化恒等分支要么是加法群，要么是至多五个 $\mathbb F_2$ 点的
椭圆曲线；潜在好约化的椭圆曲线分支群阶只含素因子 $2,3$。
故 $A(K_2)[p]=0$。

局部 Euler 特征公式及 Weil 自对偶，对剩余特征不为 $p$ 的地方给
$$
\dim_{\mathbb F_p}H^1(K_2,V)
=\dim H^0(K_2,V)+\dim H^0(K_2,V^*(1))=0.
\tag{65.6}
$$
所以后面构造的每个全局类在 $2$ 自动满足通常条件；没有遗留
“椭圆单位在 $2$ 或许有额外类”的问题。

### 2.3 只松弛 $p$ 处的群是一维 $\mathbb F$ 空间

$p$ 在 $K$ 惰性，$K_p/\mathbb Q_p$ 非分歧二次。
R60 所用的 CM 超奇异惯性满像给 $V^{G_{K_p}}=0$。
因而局部 Euler 特征公式给
$$
\dim_{\mathbb F_p}H^1(K_p,V)=4.
$$
通常的 $A$ Kummer 条件
$$L_p= \operatorname{im}(A(K_p)/p\to H^1(K_p,V))$$
维数为二：$A(K_p)$ 的形式群具有 $\mathbb Z_p$ 秩二，而没有
有理 $p$ 挠点。CM 作用使它是一维 $\mathbb F$ 直线。
因此 $H^1(K_p,V)/L_p$ 也是一维 $\mathbb F$ 空间。

令 $R_p(K)$ 在 $p$ 处全松弛、其余位置取通常条件。
由 (65.5) 及 Poitou–Tate，
$$
R_p(K)\xrightarrow{\sim}H^1(K_p,V)/L_p,\qquad
\dim_{\mathbb F}R_p(K)=1.
\tag{65.7}
$$
它的对偶严格群在通常 Selmer 群中，故为零。
所以这个有限系数 Selmer 结构的 core rank 为一，系数域是
$\mathbb F_{p^2}$，不是在 $\mathbb Q$ 上误计成二维。

更一般地，若 $J$ 是由 $p$ 和有限多个
$\mathfrak q=(q)$、$q\equiv-1\bmod4p$ 组成的集合，
在 $J$ 全松弛、其余位置通常的群记为 $R_J(K)$。因为
$\mathfrak q$ 在 $T/K$ 完全分裂，局部表示在 $K_{\mathfrak q}$
平凡，且 $N\mathfrak q=q^2\equiv1\bmod p$。该处
$H^1/L_{\mathfrak q}$ 也是一维 $\mathbb F$ 空间，故
$$
R_J(K)\xrightarrow{\sim}
\bigoplus_{v\in J}H^1(K_v,V)/L_v,\qquad
\dim_{\mathbb F}R_J(K)=|J|.
\tag{65.8}
$$
我们用 $\partial_{\mathfrak q}$ 表示该处的奇异商坐标。

## 3. 所需的类群分量严格为零

令 $\mathcal A_T$ 为 $T$ 的理想类群的 $p$ 部分。
有
$$
\boxed{\mathcal A_T^\chi=0.}
\tag{65.9}
$$
以下给出证明，避免把某个类群分量擅自设为零。

若 $\mathcal A_T/p\mathcal A_T$ 有一个 $C$ 等变的非零商
$V$，Hilbert 类域给一个非零同态
$$h:G_T\longrightarrow V$$
在 $T$ 的每个有限位置都不分歧。由于 $p\nmid|C|$，
它唯一下降为 $c\in H^1(K,V)$。

在 $p$ 处，$T/K$ 全分歧，局部惯性给整个 $C$。
$h$ 在 $T_p$ 的不分歧商上取值；$C$ 对这个商的共轭作用平凡，
所以其取值必须落在 $V^C=0$。因此 $h$ 在整个该局部分解群为零。
限制映射的核是某个阶与 $p$ 互素的群的 $H^1$，亦为零，
故 $\operatorname{loc}_p(c)=0$。

在 $2$，(65.6) 给局部类为零。在其余有限素数，
$T/K$ 与 $V$ 不分歧，而 $h$ 不分歧，故 $c$ 满足通常的好约化
Kummer 条件。复位置没有一次上同调。因此
$c\in\operatorname{Sel}_p(A/K)=0$，矛盾。

这排除了 $\mathcal A_T/p\mathcal A_T$ 的 $V$ 等型部分。
在 $\mathbb F$ 上，该 $\mathbb F_p$ 不可约型分解成
$\rho,\rho^p$ 两个 Frobenius 共轭特征；因
$\mathcal A_T$ 原来定义在 $\mathbb Z_p$ 上，两个分量同时消失。
Nakayama 引理于是给 (65.9)。

这个论证也适用于先商掉有限多个素理想所得的类群。
因此 R60 的 Kummer 算法在正确的 $V(-1)$ 分量上，确实没有未知的
$p$ 类群项；这是由 (65.5) 证明的加强，并非对整个类群无 $p$ 挠的断言。

## 4. 一个固定的模 $p$ 原始 Robert 椭圆单位

### 4.1 已发表的有限 Gras 指数定理

令 $\mathcal E_T=\mathcal O_T^\times$，令 $\mathcal C_T$ 为
Rubin 的椭圆单位群。Rubin (1991), Theorem 3.3，
印刷页 35 给每个不可约 $\mathbb Z_p[C]$ 分量
$$
\#(\mathcal E_T/\mathcal C_T)^\chi=\#\mathcal A_T^\chi.
\tag{65.10}
$$
其 §1 的假设是 $p$ 不除基域 Hilbert 类域的单位根数，
且在 Theorem 3.3 中 $p\nmid[T:K]$。
这里 $h_K=1$、该单位根数为四，而 $[T:K]=p^2-1$，全部满足。
定理没有要求 $p$ 在 $K$ 分裂或 $A$ ordinary。
原定理使用不可约 $\mathbb Z_p$ 特征；扩系数到 $\mathcal O$ 后，
相关型分成 $\chi$ 及其 Frobenius 共轭。两者的长度相同，
所以原定理也给出 (65.10) 的单个 $\mathcal O$ 特征版本。

Dirichlet 单位定理说明每个非平凡 $C$ 特征的单位分量秩一：
$C$ 在 $T$ 的复共轭嵌入对上自由传递作用，单位的有理表示为
正则表示减去平凡表示。$\chi$ 不等于 $p$ 次单位根的特征
$\omega$，所以其分量也没有单位根挠。
结合 (65.9)、(65.10)，得到
$$
(\mathcal E_T\otimes\mathcal O)^\chi
=(\mathcal C_T\otimes\mathcal O)^\chi
\simeq\mathcal O.
\tag{65.11}
$$

### 4.2 明确选择同一族单位

记 $\mathfrak m=\operatorname{cond}(T/K)$ 为此阿贝尔扩张的有限导子。
它只支撑于 $2,p$，且 $p\mid\mathfrak m$。
所以 $K$ 的四个单位模 $\mathfrak m$ 不同。
对任意理想 $\mathfrak n$，记 $K(\mathfrak n)$ 为对应射线类域。
用 Robert 的函数
$$
\Psi(1;\mathfrak n,\mathfrak b^{-1}\mathfrak n)
\in K(\mathfrak n)^\times
$$
表示由格子
$\mathfrak n\subset\mathfrak b^{-1}\mathfrak n$ 定义的椭圆单位值；
要求 $(\mathfrak b,6\mathfrak n)=1$。
其定义、范数关系和与 Stark 单位的关系在
Oukhaba–Viguié (2013), §4 明确重述，亦对应 Rubin (1991), §1 的构造。

固定
$$
\mathfrak m_0=(7)\mathfrak m,\qquad \mathfrak b=(11),\qquad
u_1=
N_{K(\mathfrak m_0)/T}
\Psi(1;\mathfrak m_0,\mathfrak b^{-1}\mathfrak m_0).
\tag{65.12}
$$
$\mathfrak m_0$ 至少含 $p$ 和 $(7)$ 两个不同素理想，因此
$u_1$ 是一个真正的全局单位。
下面证明其 $\chi$ 分量生成 (65.11)，特别是模 $p$ 非零。

因 $\chi$ 对 $C$ 忠实，它作为射线类特征的导子恰为
$\mathfrak m$。在椭圆单位生成元中，来自
$T\cap K(\mathfrak n)\ne T$ 的项在 $\chi$ 分量为零。
这里可使用 Oukhaba–Viguié, Remark 4.3 的范数生成元描述：
其单位群与 Rubin 的群之间的差异被 $[T:K]$ 杀掉，
故在当前 $p$ 进分量上相同。
其余项有 $\mathfrak m\mid\mathfrak n$，由 Robert 范数关系降到
$\mathfrak m$，差别仅为群环中的 Euler 因子。因此所需椭圆单位
分量由
$$
v_{\mathfrak a}=
N_{K(\mathfrak m)/T}
\Psi(1;\mathfrak m,\mathfrak a^{-1}\mathfrak m),
\qquad(\mathfrak a,6\mathfrak m)=1
\tag{65.13}
$$
的 $\chi$ 投影生成。Rubin 定义中的额外 $\sigma-1$ 因子对非平凡
$\chi$ 不改变此模：可取 $\chi(\sigma)-1$ 为 $\mathcal O$ 单位。
即使 $\mathfrak m$ 是单素数幂，(65.13) 的非平凡 $\chi$ 投影也在
单位分量中；唯一的 $p$ 上方素理想的赋值模为平凡 $C$ 模。

Stark–Robert 关系给交叉恒等式
$$
(N\mathfrak b-\chi(\sigma_{\mathfrak b}))\,
e_\chi v_{\mathfrak a}
=
(N\mathfrak a-\chi(\sigma_{\mathfrak a}))\,
e_\chi v_{\mathfrak b}
\tag{65.14}
$$
于加法记号的 $\chi$ 分量，$\sigma_{\mathfrak a}$ 为 Artin 元素。
可从
$\Psi_{\mathfrak m}(\mathfrak a)^{w_{\mathfrak m}}
=\varepsilon_{\mathfrak m}^{\,N\mathfrak a-\sigma_{\mathfrak a}}$
交叉相乘得到；可能的单位根在此分量为零，不需除以
$w_{\mathfrak m}$ 的 $p$ 部分。

对惰性的有理素数 $\ell=7,11$，$A$ 的 Frobenius 迹为零，所以
在 $\mathfrak l=(\ell)$，
$$
\rho(\sigma_{\mathfrak l})=-\ell,\qquad
\chi_0(\sigma_{\mathfrak l})=-\ell.
$$
因此
$$
N(11)-\chi(\sigma_{(11)})\equiv121+11=132\not\equiv0\pmod p.
\tag{65.15}
$$
(65.14) 说明 $e_\chi v_{(11)}$ 本身生成 (65.11)。
再由新增素数 $(7)$ 的范数关系，
$$
e_\chi u_1=(1-\chi(\sigma_{(7)})^{-1})e_\chi v_{(11)},\qquad
1-\chi_0(\sigma_{(7)})^{-1}=1+\frac17=\frac87\ne0.
\tag{65.16}
$$
故
$$
\boxed{\overline{e_\chi u_1}\ne0,\qquad
\kappa_0:=\mathcal K(\overline{e_\chi u_1})
\text{ 生成 }R_p(K).}
\tag{65.17}
$$
最后一句由单位在 $p$ 外的 Kummer 类不分歧、(65.6)、(65.7) 及
Kummer 单射得到。这个原始性证明使用有限 Gras 等式和零 Selmer，
没有未经核对地把某个 $p$-进 $L$ 值专项化成单位。

## 5. 同一个原始 Euler system 的导数

### 5.1 明确的单位族和导数算子

令
$$\mathcal P_p=\{q:q\text{ 为素数},\ q\equiv-1\bmod4p\}.$$
每个 $\mathfrak q=(q)$ 在 $T/K$ 完全分裂，且
$N\mathfrak q=q^2\equiv1\bmod p$。
Rubin (1991), Lemma 1.1 给 $T(\mathfrak q)/T$：
它是 $T K(\mathfrak q)$ 中唯一的次数 $p$ 子扩张，
在全部 $\mathfrak q$ 上方素数全分歧，其余地方不分歧。

因为 $h_K=1$、$p\nmid4$，该扩张也是 $T$ 与
$K(\mathfrak q)/K$ 的唯一次数 $p$ 子扩张的合成。
对平方自由的
$\mathfrak n=\prod_{\mathfrak q\mid\mathfrak n}\mathfrak q$，
置
$$
T(\mathfrak n)=\prod_{\mathfrak q\mid\mathfrak n}T(\mathfrak q),
\qquad
\Gamma_{\mathfrak n}=\operatorname{Gal}(T(\mathfrak n)/T)
=\prod_{\mathfrak q\mid\mathfrak n}\Gamma_{\mathfrak q},
\quad \Gamma_{\mathfrak q}\simeq\mathbb Z/p\mathbb Z.
$$
这里的直积也可直接由射线类群的 $p$ 部分得到：基域类群和单位根
都没有 $p$ 部分，不同素理想的局部 $p$ 因子彼此独立。
$\operatorname{Gal}(T(\mathfrak n)/K)=C\times\Gamma_{\mathfrak n}$
为阿贝尔群。

固定每个 $\Gamma_{\mathfrak q}$ 的生成元 $\sigma_{\mathfrak q}$，并置
$$
D_{\mathfrak q}=\sum_{j=1}^{p-1}j\sigma_{\mathfrak q}^{\,j},\qquad
D_{\mathfrak n}=\prod_{\mathfrak q\mid\mathfrak n}D_{\mathfrak q}.
\tag{65.18}
$$
于是
$$
(\sigma_{\mathfrak q}-1)D_{\mathfrak q}
=p-\sum_{j=0}^{p-1}\sigma_{\mathfrak q}^{\,j}.
\tag{65.19}
$$
采用同一个固定的 $\mathfrak m_0,\mathfrak b$，定义
$$
u_{\mathfrak n}=
N_{K(\mathfrak m_0\mathfrak n)/T(\mathfrak n)}
\Psi(1;\mathfrak m_0\mathfrak n,
       \mathfrak b^{-1}\mathfrak m_0\mathfrak n).
\tag{65.20}
$$
所有候选 $q$ 都大于 $11$，所以 $\mathfrak n$ 与
$6\mathfrak m_0\mathfrak b$ 互素。
Robert 的范数及同余关系使 (65.20) 成为一个原始 Euler system。
在采用 $1-\operatorname{Frob}^{-1}$ 范数约定时，它们为
$$
N_{T(\mathfrak n\mathfrak q)/T(\mathfrak n)}
u_{\mathfrak n\mathfrak q}
=u_{\mathfrak n}^{\,1-\operatorname{Frob}_{\mathfrak q}^{-1}},
\tag{65.21}
$$
$$
u_{\mathfrak n\mathfrak q}
\equiv
u_{\mathfrak n}^{\,\operatorname{Frob}_{\mathfrak q}^{-1}
(N\mathfrak q-1)/p}
\pmod{\text{所有 }\mathfrak q\text{ 上方素理想}}.
\tag{65.22}
$$
这些关系及具体范数构造见 Oukhaba–Viguié, §4；
Rubin 的原函数约定可以使全部范数关系取逆，不影响下述非零性及
最终归一化，但有限—奇异映射的符号须跟随同一个约定。

### 5.2 有单位根时仍唯一的 $\chi$ 下降

由 (65.19)、(65.21)，
$$
e_{\chi_0}[u_{\mathfrak n}^{D_{\mathfrak n}}]
\in
\left((T(\mathfrak n)^\times/
T(\mathfrak n)^{\times p})\otimes\mathbb F\right)
^{\Gamma_{\mathfrak n},\chi_0}.
$$
不变性可按 $\mathfrak n$ 的素因子归纳：
$(\sigma_{\mathfrak q}-1)D_{\mathfrak n}$ 在模 $p$ 后成为
负的范数算子；(65.21) 将它化为
$(1-\operatorname{Frob}_{\mathfrak q}^{-1})D_{\mathfrak n/\mathfrak q}
u_{\mathfrak n/\mathfrak q}$，而归纳不变性使其为零。

虽然 $\mu_p\subset T$，$\chi_0$ 分量的下降没有歧义。
因为 $C$ 与 $\Gamma_{\mathfrak n}$ 交换，
$$H^j(\Gamma_{\mathfrak n},\mu_p)\quad(j=1,2)$$
的 $C$ 作用只有圆分特征 $\omega$。而 $\chi_0\ne\omega$，
所以 inflation–restriction 在 $\chi_0$ 分量给同构
$$
\operatorname{res}:
\left((T^\times/T^{\times p})\otimes\mathbb F\right)^{\chi_0}
\xrightarrow{\sim}
\left((T(\mathfrak n)^\times/T(\mathfrak n)^{\times p})
\otimes\mathbb F\right)^{\Gamma_{\mathfrak n},\chi_0}.
\tag{65.23}
$$
定义原始导数数据及其全局类
$$
k_{\mathfrak n}
=\operatorname{res}^{-1}
 \bigl(e_{\chi_0}[u_{\mathfrak n}^{D_{\mathfrak n}}]\bigr),
\qquad
\kappa_{\mathfrak n}=\mathcal K(k_{\mathfrak n}).
\tag{65.24}
$$
$\mathfrak n=1$ 时就是已选的 $\kappa_0$。
(65.23) 也提供有限的下降算法；具体 Hilbert 90 构造见
Rubin, Proposition 2.2。无需假定 $T$ 不含 $\mu_p$，也没有任意选择
一个下降类后再忽略其差异。

以下所有 $\kappa_{\mathfrak n}$ 始终来自 (65.20)、(65.24) 的同一个
原始族。后面为满足 $p$ 条件所作的线性校正不改变这个定义。

### 5.3 局部条件与有限—奇异关系

对 $\mathfrak n$ 的任意素因子 $\mathfrak q$，已发表的导数局部关系给
$$
\kappa_{\mathfrak n}\in
R_{\{p\}\cup\{\mathfrak l:\mathfrak l\mid\mathfrak n\}}(K),
\qquad
\partial_{\mathfrak q}\kappa_{\mathfrak n}
=\Phi_{\mathfrak q}
  (\operatorname{loc}_{\mathfrak q}
          \kappa_{\mathfrak n/\mathfrak q}),
\tag{65.25}
$$
其中
$$
\Phi_{\mathfrak q}:
H^1_{\rm ur}(K_{\mathfrak q},V)
\xrightarrow{\sim}
H^1(K_{\mathfrak q},V)/
H^1_{\rm ur}(K_{\mathfrak q},V)
\tag{65.26}
$$
是一维 $\mathbb F$ 空间之间的同构，依赖已选生成元
$\sigma_{\mathfrak q}$。

这里可直接核查全部假设。$\mathfrak q$ 在 $T/K$ 全分裂，
$N\mathfrak q\equiv1\bmod p$，$p\nmid w_K=4$；原始单位族满足
(65.21)、(65.22)。Rubin (1991), Proposition 2.4 给单位根式的
赋值公式；Oukhaba–Viguié, §5、式 (5.2) 用上述 Robert 约定重述。
投影到 $\chi_0$ 并张量 $V(-1)$，正是 (65.25)。

为明确 (65.26) 确实可算，取 $\lambda\mid\mathfrak q$ 于 $T$，
在 $T(\mathfrak q)$ 上方取统一化元 $\pi$。则
$\overline{\pi^{\,1-\sigma_{\mathfrak q}}}$ 是
$k_\lambda^\times$ 中的本原 $p$ 次单位根。
取 $x_\lambda$ 满足
$$
x_\lambda^{(q^2-1)/p}
=\overline{\pi^{\,1-\sigma_{\mathfrak q}}}.
$$
$x_\lambda$ 在
$k_\lambda^\times/(k_\lambda^\times)^p$ 中的类唯一且非零。
把一个单位的剩余类写为 $x_\lambda^{d_\lambda}$，
局部映射取它到 $-d_\lambda\lambda\bmod p$，再合并全部
$\lambda$、投影 $\chi_0$、张量 $V(-1)$，得到 (65.26)。
该映射逐个剩余域都是同构，且与 $C$ 作用相容。
即使 $p^2\mid q+1$，此同构仍有效；这里没有额外要求
$v_p(q+1)=1$。

在 $p$ 外且不除 $\mathfrak n$ 的素数，下降域不分歧，单位类保持
不分歧；在 $2$ 另有 (65.6)。这些正是 (65.25) 第一式的通常局部条件。
它没有声称原始导数已经满足 $p$ 处的 $A$ Kummer 条件。

## 6. 明确消去 $p$ 处坐标

为实现校正，固定
$$
\ell_p:H^1(K_p,V)\longrightarrow\mathbb F,\qquad
\ker\ell_p=L_p,
\tag{65.27}
$$
为一个非零 $\mathbb F$ 线性函数。

它可以直接由实际的局部曲线构造。取 $A$ 的形式参数 $t=-x/y$，
选取 $t=p$ 的形式群点 $P$；它在
$A(K_p)/p$ 中非零，并生成这个一维 $\mathbb F$ 空间。
令 $a=\delta_A(P)\in L_p$。用局部 Tate 配对定义 $\ell_p$：
对所有 $b\in\mathbb F$，令
$$
\operatorname{Tr}_{\mathbb F/\mathbb F_p}
  (\overline b\,\ell_p(x))
=B_p(x,b a).
\tag{65.28}
$$
迹配对非退化给唯一的 $\ell_p(x)$。
CM 的 Rosati 对合为复共轭，故
$B_p(cx,ba)=B_p(x,\overline c\,ba)$；
这证明 (65.28) 对 $x$ 为 $\mathbb F$ 线性。
$L_p=L_p^\perp$ 又给其核恰为 $L_p$。
形式对数在 $p\mathcal O_{K_p}$ 上首项为 $t$，
所以所选 $P$ 的 Kummer 类确实非零。

这些配对可以在包含 $\mu_p,V$ 的局部域 $T_\lambda$ 中用
$p$ 次 Hilbert 符号计算，再按次数
$[T_\lambda:K_p]=p^2-1$ 下降；该次数模 $p$ 可逆。
这一构造使用超奇异曲线本身的形式群和 Weil 配对。

对任意 $c\in R_{\{p\}\cup J}(K)$，定义
$$
c^{[p]}=
c-\frac{\ell_p(\operatorname{loc}_p c)}
        {\ell_p(\operatorname{loc}_p\kappa_0)}\,\kappa_0.
\tag{65.29}
$$
分母由 (65.7)、(65.17) 非零。
于是 $c^{[p]}\in R_J(K)$，且它在 $J$ 的奇异坐标与 $c$ 相同。
改变 (65.27) 的基只同时缩放分子分母，不改变校正后的类。

## 7. 一阶导数的适用范围与准确退化密度

若
$$\operatorname{loc}_{\mathfrak q}\kappa_0\ne0,$$
则由 (65.25)
$$
d_{\mathfrak q}:=\kappa_{\mathfrak q}^{[p]}
\in R_{\{\mathfrak q\}}(K),\qquad d_{\mathfrak q}\ne0.
\tag{65.30}
$$
它将通过下一节的共轭投影给 $c_q$。

若 $\operatorname{loc}_{\mathfrak q}\kappa_0=0$，
则 $\partial_{\mathfrak q}\kappa_{\mathfrak q}=0$。
此时 $\kappa_{\mathfrak q}\in R_p(K)=\mathbb F\kappa_0$，
所以
$$\kappa_{\mathfrak q}^{[p]}=0. \tag{65.31}$$
可见模 $p$ 原始的基单位不保证每个一次导数都能生成所需类。

固定 $p$ 后，(65.31) 的候选有理素数在 $\mathcal P_p$ 中的相对
自然密度恰为 $1/p$。证明如下。
$R_p(K)$ 的 $\tau$ 固定部分是只在 $p$ 松弛的
$R_p(\mathbb Q)$；它是一维 $\mathbb F_p$，并在 $\mathbb F$ 上
张成 $R_p(K)$。取一个非零 $c_p^{\mathbb Q}$。
它限制到 $G_T$ 后不为零：$H^1(\operatorname{Gal}(T/\mathbb Q),V)=0$。
其像对整个非分裂正规化子稳定，所以由不可约性等于 $V$。
相应扩张 $N_p$ 满足
$$
\operatorname{Gal}(N_p/T)=V,\qquad
\operatorname{Gal}(N_p/\mathbb Q)=V\rtimes
\operatorname{Gal}(T/\mathbb Q).
\tag{65.32}
$$
它在 $2,p$ 外不分歧。

对 $q\in\mathcal P_p$，R60 的 Frobenius 公式把
$\operatorname{loc}_q(c_p^{\mathbb Q})=0$ 写为
$\pi_g^+(v)=0$。每个候选 Frobenius $g$ 的这个投影秩一，
其核占 $V$ 的 $1/p$。
$\kappa_0$ 是 $\operatorname{res}c_p^{\mathbb Q}$ 的非零
$\mathbb F$ 倍，且局部二次限制单射，所以这也正是
$\operatorname{loc}_{\mathfrak q}\kappa_0=0$。
Chebotarev 给所述密度。量词是先固定 $p,N_p$，再让 $q$ 变化。

## 8. 一个辅助素数与原始二阶导数补齐全部退化情形

现在固定一个退化素数 $q$，即
$\operatorname{loc}_{\mathfrak q}\kappa_0=0$。

### 8.1 可搜索的辅助素数总存在

选择 $r\in\mathcal P_p$、$r\ne q$，使
$$
\operatorname{loc}_{\mathfrak r}\kappa_0\ne0,\qquad
\operatorname{loc}_{\mathfrak q}d_{\mathfrak r}\ne0,
\quad d_{\mathfrak r}:=\kappa_{\mathfrak r}^{[p]}.
\tag{65.33}
$$
这些条件全部可以用已知的单位和一阶导数检查，不需要先知道
目标 $c_q$ 的生成元。

为证明搜索会结束，暂用 R60 已由对偶存在性定义的 $c_q$ 及其域
$N_q$。$N_p$ 与 $N_q$ 在 $T$ 上线性不交：
在对角 $G=\operatorname{Gal}(T/\mathbb Q)$ 作用下，若
$V^2$ 的像有关系，由半单性和
$\operatorname{End}_G(V)=\mathbb F_p$ 可写成
$ah_p+bh_q=0$。限制到 $q$ 惯性，$h_p$ 为零、$h_q$ 非零，
故 $b=0$；再用 $h_p\ne0$ 得 $a=0$。
于是
$$\operatorname{Gal}(N_pN_q/T)=V^2. \tag{65.34}$$

R60 的同一计数给：在固定的 $\mathcal P_p$ 中，
$$
\operatorname{loc}_r c_p^{\mathbb Q}\ne0,\qquad
\operatorname{loc}_r c_q\ne0
\tag{65.35}
$$
同时成立的相对密度为 $(1-1/p)^2>0$。
第一项等价于 (65.33) 第一项。
它成立时 $d_{\mathfrak r}$ 是
$R_{\{\mathfrak r\}}(K)$ 的基，因而是
$\operatorname{res}c_r$ 的非零 $\mathbb F$ 倍。
R60 的交替互反给
$$
\operatorname{loc}_r c_q\ne0
\ \Longleftrightarrow\
\operatorname{loc}_q c_r\ne0
\ \Longleftrightarrow\
\operatorname{loc}_{\mathfrak q}d_{\mathfrak r}\ne0.
$$
因此 (65.35) 正好证明 (65.33) 有无穷多个可选素数。
这里的 $c_q$ 只用于证明终止性；实际搜索测试的是 (65.33)。

### 8.2 必须用原始 $\kappa_{\mathfrak q\mathfrak r}$

由定义
$$
\kappa_{\mathfrak r}
=d_{\mathfrak r}+\alpha\kappa_0
\quad\text{对某个 }\alpha\in\mathbb F.
$$
因为 $\operatorname{loc}_{\mathfrak q}\kappa_0=0$，(65.33) 给
$$
\operatorname{loc}_{\mathfrak q}\kappa_{\mathfrak r}
=\operatorname{loc}_{\mathfrak q}d_{\mathfrak r}\ne0.
$$
应用原始 Euler system 的 (65.25)，得到
$$
\partial_{\mathfrak q}\kappa_{\mathfrak q\mathfrak r}
=\Phi_{\mathfrak q}
(\operatorname{loc}_{\mathfrak q}\kappa_{\mathfrak r})
\ne0.
\tag{65.36}
$$
这一步用的是 (65.24) 的原始二阶类；没有把归一化后的
$d_{\mathfrak r}$ 或 $c_r$ 重新冒充为兼容 Euler system 的成员。

因 $\partial_{\mathfrak r}d_{\mathfrak r}\ne0$，在一维
$\mathbb F$ 奇异商中可定义唯一标量
$$
\beta=
\frac{\partial_{\mathfrak r}\kappa_{\mathfrak q\mathfrak r}}
     {\partial_{\mathfrak r}d_{\mathfrak r}}.
$$
令
$$
\boxed{
d_{\mathfrak q}
=\left(\kappa_{\mathfrak q\mathfrak r}
       -\beta d_{\mathfrak r}\right)^{[p]}.}
\tag{65.37}
$$
减去 $\beta d_{\mathfrak r}$ 消去 $\mathfrak r$ 的奇异坐标，
再作 (65.29) 消去 $p$ 的坐标。
两项都不改变 $\mathfrak q$ 的奇异坐标：
$d_{\mathfrak r}$ 在 $\mathfrak q$ 不分歧，
$\kappa_0$ 在 $\mathfrak q$ 更为零。
故由 (65.36)
$$
d_{\mathfrak q}\in R_{\{\mathfrak q\}}(K),\qquad
d_{\mathfrak q}\ne0.
\tag{65.38}
$$

所以 (65.30)、(65.37) 联合覆盖每一个候选 $q$。
每个最终公式至多使用一阶与二阶导数，并至多需要一个辅助素数；
搜索辅助素数所需的大小和计算时间没有被统一控制。

## 9. 下降到 $\mathbb Q$ 并恢复 R60 的唯一归一化

对 (65.30) 或 (65.37) 得到的非零
$d_{\mathfrak q}\in R_{\{\mathfrak q\}}(K)$，
考虑
$$
P^+(d)=\frac{d+\tau d}{2}.
$$
$d_{\mathfrak q}$ 与 $i d_{\mathfrak q}$ 中至少一个满足
$P^+(b d_{\mathfrak q})\ne0$，$b\in\{1,i\}$。
若 $P^+(d_{\mathfrak q})=0$，则
$\tau d_{\mathfrak q}=-d_{\mathfrak q}$；
由 $\tau(i)=-i$ 得 $i d_{\mathfrak q}$ 本来就固定，证明此断言。

限制映射给
$$
R_{\{q\}}(\mathbb Q)
\xrightarrow{\sim}
R_{\{\mathfrak q\}}(K)^{\tau=1},
\tag{65.39}
$$
因为二次扩张次数与 $p$ 互素，且通常 Kummer 条件的限制与范数
相容。令 $d_q^{\mathbb Q}$ 为
$P^+(b d_{\mathfrak q})$ 的唯一下降。它非零，
所以由 R60 §3，存在唯一 $\lambda_q\in\mathbb F_p^\times$ 使
$$\operatorname{loc}_q d_q^{\mathbb Q}=\lambda_q e_q.$$
最终
$$
\boxed{c_q=\lambda_q^{-1}d_q^{\mathbb Q}.}
\tag{65.40}
$$
这与 R60 由 Poitou–Tate 定义的 $c_q$ 完全相同，理由是那里的
唯一性。

没有对原始椭圆单位族预设复共轭的符号，也没有在每个导数阶数
任意改符号后再引用兼容关系。原始族始终在 $K$ 上计算，
所有局部校正完成之后才作 (65.39)。

## 10. 算法输出、可复验范围与没有得到的结论

给定 $p$ 和目标 $q$，公式提供以下有限过程：

1. 在固定除法域 $T$ 及其有限射线扩张中计算
   (65.12)、(65.20) 的 Robert 函数值。
   (65.15)、(65.16) 及有限 Gras 等式保证基值的正确分量模 $p$ 非零。
2. 由 (65.18)、(65.23) 计算原始导数的 Kummer 数据。
3. 若基类在 $q$ 不为零，用 (65.30)；
   否则枚举并检测 (65.33)，然后使用原始二阶类和 (65.37)。
4. 用真实局部曲线的 (65.28)、(65.29) 作 $p$ 处校正，
   再用 (65.39)、(65.40) 下降并归一化。
5. 在 $\mathbb F_p$ 基下展开最终的 Kummer 数据，得到 R60
   的两个根式类 $a_{q,1},a_{q,2}\in T^\times/T^{\times p}$。
   对其他候选素数应用 R60 的赋值归零及剩余符号公式，
   即可恢复矩阵条目。

这消除了 R60 §9 中“尚未证明有正确、非零椭圆单位生成元及导数下降”
的存在性缺口。它不要求计算整个 $T$ 的基本单位或类群；
(65.9) 仅排除了所需等型分量，而 Robert 函数及局部符号仍然可能
具有很高的代数计算成本。本轮没有展开具体数值的 Robert 单位、
辅助素数或任何 $m_{ji}$，不能把生成公式说成完成了那些数值运算。

$T(\mathfrak n)/K$ 是用于制造单位的阿贝尔射线扩张。
R60 的控制域 $N_q/K$ 却具有
$$\operatorname{Gal}(N_q/K)=V\rtimes C,$$
其中 $C$ 对 $V$ 非平凡作用，因而不是阿贝尔扩张。
它来自下降后 Kummer 数据的 $p$ 次根；本文没有声称
$N_q$ 本身包含于 $K$ 的普通射线类域。

最后，这一构造没有给 R19 的整数解，没有给 R53 的原始高指数元，
也没有把实际 $E$ 的 $p$-Selmer 群传到 R46 的辅助三同源问题。
它精确生成 R60 的全局算术矩阵，尚未从这些条目推出变化 $p$
上的统一排除。

## 11. 核验过的已发表输入

- K. Rubin, **The “main conjectures” of Iwasawa theory for imaginary quadratic fields**,
  Inventiones Mathematicae **103** (1991), 25–68，
  [DOI](https://doi.org/10.1007/BF01239508)，
  [作者论文目录](https://webapps.math.uci.edu/~krubin/preprints/)，
  [Göttingen 原期刊档案](https://resolver.sub.uni-goettingen.de/purl?PPN356556735_0103)。
  已核原文 §1（印刷页 27–29）的基域、单位根假设及 Lemma 1.1、
  Proposition 1.2；§2 的导数算子、Proposition 2.2；
  Theorem 3.3（印刷页 35）的逐特征精确指数等式。
  有限—奇异理想公式为 Proposition 2.4。
- H. Oukhaba and S. Viguié, **On the Gras Conjecture for Imaginary Quadratic Fields**,
  Canadian Mathematical Bulletin **56** (2013), 148–160，
  [期刊全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf)，
  [DOI](https://doi.org/10.4153/CMB-2011-173-1)。
  本文只用其 §4 对 Robert 函数、范数关系、Euler unit 族的明确重述、
  Remark 4.3 的单位群比较，以及 §5 的公式 (5.2)；
  未将其专门处理 $p\mid w_K$ 的 Theorem 1.1 误套在当前情形。
- R. Pollack and K. Rubin, **The main conjecture for CM elliptic curves at supersingular primes**,
  Annals of Mathematics **159** (2004), 447–464，
  [全文](https://arxiv.org/pdf/math/0509604)，§1 的 CM 超奇异惯性满像。
  $A$ 的零 Selmer 结论及其 $L$ 值归一化已完整核验在
  [R50](R50-actual-selmer-alternating-matrix.md)。
- [R60](R60-selmer-matrix-kummer-residue-symbols.md)：
  唯一归一化、局部基、交替互反、Kummer 符号和联合控制域。
  本文的辅助素数存在性使用其中已证明的确定性有限群结构和
  Chebotarev 计数。
