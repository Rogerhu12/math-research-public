# 原 full54 几何端点与 type4 Newton 的未平方交叉恒等式

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。**状态：以下同一原 full54 的交叉恒等式及所列单位范围已证明；主目标未完成。**

本注沿用 R1049 的同一个 $Y_{j,0}$、$I_{j,p}$、$h_{j,p}=a_j^{-1}I_{j,p}$，
以及原 R806 的 $D_j=D_{j,1}$、$[z^4]D_j=1$。始终
$j\in\{4,10,16\}$，$p\equiv-1\bmod6$。三个 $B_j$ 是
[共同 Artin 基笔记](2026-11-27-original-weight-five-toric-artin-basis-and-common-phase.md)
及[未平方来源笔记](2026-11-27-original-unsquared-toric-theta-source-and-newton-pullback.md)
的实际 $B_j=(17\delta/9)T_{j,5}$，不重新选择平方根。

以下删去固定有限集合：原曲面、全有限角色、原周期和上述三条
固定代数截面的整模型坏素数及共同系数域的分歧素数。需要 R1049 整格结论时，还要求
$p$ 在该篇的充分大范围内。交叉恒等式本身不依赖新增 NS 的证明。

## 1. 结论及其精确范围

令 $K_{j,p}$ 为原负二 Newton 函数，采用
$$
d=p+1,\qquad c_\sigma=[z^d]\log(\sigma_0(z)/z),\qquad C=34c_\sigma,
$$
$$
J_{j,p}(v)=
\sum_{h\ge0}C^{-h}[z^{dh-2}]
 \bigl(D_j(z)e^{-Cz^d}\bigr)(v)_h,\qquad
K_{j,p}(v)=\frac{J_{j,p}(v)}{pv}.
\tag{1}
$$
这里 $(v)_h=v(v-1)\cdots(v-h+1)$。原 Newton 笔记已证明
$K_{j,p}\in\mathcal O\langle v\rangle$。

本注证明
$$
\boxed{
I_{j,p}B_lK_{l,p}(0)
 =I_{l,p}B_jK_{j,p}(0)
\qquad(j,l\in\{4,10,16\}).
}
\tag{2}
$$
这是整个 $p$-adic 值的恒等式，不只是模 $p$ 的平方或相位比较。

若至少一条 $K_{j,p}(0)$ 为单位，则在 R1049 的整格范围内存在
同一个实际单位 $F_p^{\rm geom}$，使
$$
\boxed{
I_{j,p}=F_p^{\rm geom}B_jK_{j,p}(0),\qquad
h_{j,p}=F_p^{\rm geom}\frac{B_j}{a_j}K_{j,p}(0),\qquad
\overline{F_p^{\rm geom}}=-[L:H].
}
\tag{3}
$$
这不把 $F_p^{\rm geom}$ 在全部精度上改成其剩余值，
不将几何循环认作椭圆单位全局类，也不把指定三个 $K$ 的非零
作为已证明的无穷素数结论。若三条 $K(0)$ 都为零，(2)本身
没有断言三个 $I$ 都为零。

## 2. 固定 weight3 向量和所有有限算子

令 $f=\theta(\psi_{27}^2)$，保持原 $\Gamma$、full9 的 $Ph$
和三处完整243项。先把原2、17有限邻点算子以及原有限投影
施到这个固定 weight3 来源，得三个实际向量 $V_j$。
它们可同时在一个固定的、素于 $p$ 的 full-level 覆盖上处理。
这是对有限 level 的真实拉回；没有改用满足另一个
cyclic Heegner 假设的模曲线。

若 $n\ge0$、$n\equiv4\bmod6$，记原经典 toric 和为
$\mathcal T_j(n)$，其形式是对 $\delta_3^n f$施相同的
weight-$3+2n$几何邻点算子，再作原全部有限求和。
R1006(22)的实际 Kodaira--Spencer 比较给
$$
\mathcal T_j(n)
 =34^n\,\operatorname{Tor}_{j,n}(\delta_3^nV_j).
\tag{4}
$$
因子 $34^n$对三个 $j$完全相同。等式中的 toric 方向为
$$
\xi_{j,n}=\eta_j^{-1}\nu_{27}^{-(3+2n)},\qquad
\nu_{27}=\psi_{27}N_K^{-1/2}.
\tag{5}
$$
原 $\eta_j$、算术 Artin 的逆、所有图的微分倍率和 Cor
都包含在 $\operatorname{Tor}_{j,n}$内。有限算子与 $p$-Hecke
及 $p$-depletion 交换；因此下面可在共同源 CM 曲线 $A=E_{27}$
上构造三个局部族，共用一个 $p^\infty$基和同一个 CM 周期。
不必为54个靶曲线分别猜周期。

## 3. 第二 theta 槽的一个固定共同整模型

采用未平方来源笔记§§10--11中**实际双 torus 投影后**的
positive rank-one Schwartz 向量，记为 $\phi_{\beta,j}$。
其 character 为 $\beta_j=\eta_j\psi_{27}$，Hermite 槽为 $n+2$。
这里不声称它在3处等于原 type4 的
$\mathbf1_{3^{-1}\mathbf Z_3}$；$\psi_{27}$的 wild3 类型仍在。

说明如何同时取一个固定整数，而不作随 $p$ 的选择。
三个 $\phi_{\beta,j}$在所有 $\ell\nmid102$处为原球；
在有限的 $\ell\mid102$处，都是同一个有理变极化后有限个
compact-open 特征函数的代数组合。取一个共同正整数 $D$，
使三个函数及其有限 Fourier 变换均满足
$$
\operatorname{supp}\phi\subset D^{-1}\widehat{\mathbf Z},
\qquad \phi(x+D\widehat{\mathbf Z})=\phi(x).
\tag{6}
$$
可取 $D$只含 $2,3,17$。具体选择规则是：逐个取三个实际
Schwartz 函数及其 Fourier 变换的支撑分母和局部常值半径的
最大值，再相乘；这定义了一个固定整数，不是存在某个别的向量。

Schrödinger 平移与调制由(6)给一个共同有限 Heisenberg 商。
在未平方来源笔记(13a)--(13c)的**同一**坐标中，
其复周期格与 R806 的 $\Lambda_S=\Omega_0^{-1}\Lambda_{E_0}$
可公度；所有换基系数属于 $\mathbf Z[1/102,\delta]$。
于是取共同整数 $M$，使 $M\Lambda_S$包含于三个实际 theta
函数的准周期格，并使该格上的有限 semicharacter 与
$\mathcal O(N O)$的标准对称 semicharacter 一致。
可按下列有限步骤选取：先清上述两个格基的全部分母，
再乘共同 Heisenberg 商的 exponent 和2。这个 $M$仍只需
含 $2,3,17$，并且对三个 $j$和全部研究素数 $p$固定。

这一步可直接从 theta 平移公式核定：位置平移及调制在
共同有限商为恒等时，只剩原二次 Gaussian 的 automorphy；
乘其 exponent 杀有限平坦 character，乘2固定对称号。
两条 rank-one 核具有相同的 quadratic coefficient，
故拉回到 $M\Lambda_S$后的次数准确为
$$
N=34M^2.
\tag{7}
$$
保留 $N$而不将其免费换回34。

这里的变量采用 R806(25)的准确规范。令
$\Theta_{\beta,j}(T)=\sum_r b_{\beta,j,r}T^r/r!$
为真实 positive Hermite coherent 生成函数，置
$$
h_\infty=\frac{\sqrt{51\sqrt3}}{204\pi i},\qquad
S_{\beta,j}(Z)=\Theta_{\beta,j}(Z/h_\infty).
\tag{7a}
$$
负槽同一规范正是
$\Theta_j(T)=s_jD_j(\Omega_0h_\infty T)$。
因而上面使用的 $\Lambda_S$是 $S_{\beta,j}$的 Fourier 变量格，
不是未经换元的 $T$格。

其真空非零由下节完整 finite 比较取得，不把新固定 source
的 $(4,6)$槽说成 $(4,0)$槽。定义
$$
E_{\beta,j}(z)
=\frac{\Theta_{\beta,j}(Mz/(\Omega_0h_\infty))}
       {\Theta_{\beta,j}(0)}
=\frac{S_{\beta,j}(Mz/\Omega_0)}{S_{\beta,j}(0)}.
\tag{8}
$$
这是同一个实际来源的拉回和刚性化；$h_\infty$、$M$均保留。

有限 Heisenberg 表示可在包含所需 roots of unity 的数域上
实现；(6)的实际向量和全部 projector 的系数均为代数数。
标准 theta structure 将其与
$H^0(E_0,\mathcal O(N O))$识别，解析比较只剩一个共同非零
标量；(8)在 $O$的归一将其消去。因此
$$
E_{\beta,j}(z)=\sigma_0(z)^N P_{\beta,j}(x_0(z),y_0(z)),
\qquad E_{\beta,j}(0)=1,
\tag{9}
$$
其中 $P_{\beta,j}$是固定代数多项式，
每项 $x^a y^b$取 $b=0,1$且 $2a+3b\le N$。
这里已杀平坦 twist，因而极只在 $O$。
同一 full unit character 使 (8)只含 $z^{6h}$；
它也排除额外的 $e^{bz}$或 $e^{az^2}$：前者不满足原偶性，
后者不满足原 $\omega$作用。故(9)是原 sigma 刚性化，
不是只到一个未计算的二次指数。

删去三个固定多项式系数的有限分母支撑后，(9)是共同整模型。
变量倍率 $M/\Omega_0$、次数 $N$和所有实尺度均独立于 $j$。



### 3.1 新旧两构造在每个有限处的实际接合

为证明上面所需的真空与§5的逐 $j$标量，比较旧 variable-weight
来源的 $m=4$与新 fixed-weight3 来源的 $n=4$：
$$
\chi_{\rm old}=\nu_{27}^{-4},\qquad
\chi_{\rm new}=\nu_{27}^{2},\qquad
\chi_{\rm new}/\chi_{\rm old}=\nu_{27}^{6}.
\tag{9a}
$$
新槽是 $(4,6)$；旧槽才是 $(4,0)$。下面比较的是这两个
槽之前的**同一个有限 Schwartz 函数**，不是将槽次数混同。

在3处，Chan 的实际 binary newvector 是
$\chi(z)\mathbf1_{\mathcal O_{K_3}^{\times}}(z)$再作用同一个
different 变换。原 $\nu_{27}$在单位上通过 $\mu_6$，
所以(9a)在每一个支撑点的比为1，连 different 变换后的
函数也逐点相同。余下 full3 compact 型及243项 projector
只用单位/主单位，故两者完全相同。

须另保非单位的 similitude。
$\nu_{27}(\delta)=i$，所以
$\nu_{27}^{6}(\delta)=-1$。
等价地，新旧三处 GL2 表示在此相差唯一的 unramified
quadratic twist：在 $GL_2(\mathbf Z_3)$上为1，在
$\operatorname{diag}(3,1)$上为$-1$。
原有限 word 的唯一奇3 valuation就是这个
$\operatorname{diag}(3,1)$；$Ph$的 determinant $-2$为3单位。
因此全 word 的变化准确是一个**独立于 $j$**的$-1$，
没有改 $\theta$、$\delta$延拓或 $Ph$的分量。
2、17处的有理 norm lifts 和单位上的(9a)均为1。

同时，两个 rank-one Hilbert90 characters 逐项给
$$
\begin{aligned}
\widetilde\alpha_{1,\rm old}
 &=\eta_j^{-1}\nu_0^{-8}
 =\eta_j^{-1}\nu_{27}^{-9}\nu_0
 =\widetilde\alpha_{1,\rm new},\\
\widetilde\alpha_{2,\rm old}
 &=\eta_j\nu_{27}\nu_0,\qquad
\frac{\widetilde\alpha_{2,\rm new}}
     {\widetilde\alpha_{2,\rm old}}=\nu_{27}^{12}.
\end{aligned}
\tag{9b}
$$
后一个比在2、17处的整个 inert norm-one torus及3处
单位和 $\delta$上均为1。
在其余 good split 处，真实向量是原球，
finite compact-unit projector 的 character 平凡、Haar体积1，
所以仍是原球，未产生一个与 $j$有关的 Euler 标量。

这里使用 compact-unit projector 足够有全局理由：
$h_K=1$使每一个有限 norm-one ideal divisor都由一个
范数为1的主元生成。因此在 $K^1\backslash\mathbf A_K^1$
上可先乘该主元把全部 finite valuations归零，
只剩无穷分量和有限单位，最后除原 $\mu_6$。
good split 的 unramified uniformizer值随这个主元转到
原无穷角色，正由 Hermite 槽次数记录；不能再附加一次
局部非紧积分或 Satake 归一化。
这也是本题同一 global theta kernel的理想重排，
没有删全 trace。

所以新旧 positive 有限 Schwartz 确实是同一条实际函数，
两 tensor factors 的乘积仅差上述共同$-1$。
先把负槽按原 $d_{j,4}=1$刚性化，再把正槽按真空刚性化；
剩余乘积比例与旧来源的比因而仍独立于 $j$。
旧 $(4,0)$ seesaw 的
$T_{j,5}\ne0$现在严格证明同一 positive 函数的
$\Theta_{\beta,j}(0)\ne0$。
新 $(4,6)$取的是此函数的第6个 Hermite 系数，未将它
当成真空，也未提前赋其非零。

## 4. 真空为1的 beta Newton 因子

置
$$
C_\beta=Nc_\sigma,\qquad
b_{j,h}=C_\beta^{-h}[z^{dh}]
 \bigl(E_{\beta,j}(z)e^{-C_\beta z^d}\bigr),
$$
$$
J_{\beta,j,p}(v)=\sum_{h\ge0}b_{j,h}(v)_h.
\tag{10}
$$
它的指数明确为 $N$，不是原 $34$；在下文它仅作为三条
共同的 $C_\beta$出现。

给出完整收敛估计。使用 R301 的同一半径
$R=p^{-1/(2p)}$，有
$$
\left\|
\exp\!\left(N(\log(\sigma_0/z)-c_\sigma z^d)\right)
\right\|_R\le1.
$$
在(9)中，每个单项式的剩余首阶为 $N-2a-3b\ge0$；
原 $x,y$的整 Gauss 界遂给
$$
\|E_{\beta,j}e^{-C_\beta z^d}\|_R\le1.
$$
因 $v_p(C_\beta)=-1$，对 $h\ge1$得到
$$
v_p(b_{j,h})\ge
\left\lceil\frac{h(p-1)}{2p}\right\rceil\ge1.
\tag{11}
$$
右边随 $h$趋于无穷，而 $(v)_h$的 Gauss 范数至多1。
因此
$$
\boxed{
J_{\beta,j,p}\in1+p\mathcal O\langle v\rangle,\qquad
J_{\beta,j,p}(0)=1.
}
\tag{12}
$$
对每个正整数 $k$，有限三角卷积准确给
$$
J_{\beta,j,p}(k)=k!C_\beta^{-k}e_{\beta,j,dk},
\qquad e_{\beta,j,r}=[z^r]E_{\beta,j}.
\tag{13}
$$
这与(1)的
$$
J_{j,p}(k)=k!C^{-k}d_{j,dk-2}=pkK_{j,p}(k)
\tag{14}
$$
使用同一个 $k$；没有把两条不同的 weight 参数拼接。

## 5. 固定来源的正权未平方乘积

未平方来源笔记(34)--(39)给正常排序后的完整双核
及原固定 $\chi=\nu_{27}^2$。
对 $n\equiv4\bmod6$，两 Hermite 次数是 $n,n+2$，
两有限线始终为原 type4 和上述实际 beta。
所有单位及 $\delta$的 lift 已逐个保持。
特别 $\eta_j(\delta)=-1$对三条相同，
固定 source 的双槽相位为 $i^{(n+2)-n}=-1$。

R806 的第一因子以 $[z^4]=1$归一，第二因子以(8)的真空1
归一。全部有限局部比例只依赖这两个实际向量，和权 $n$无关；
它们的乘积由同一个 $T_{j,5}$准确记录在 $B_j$中。
所有随权的比例来自共同 Gaussian、两个 Hermite factorial、
同一变量倍率、(4)和原 $\delta$ lift，均独立于 $j$。
因此存在逐正权指定的非零共同数 $c_n$，使
$$
\boxed{
\mathcal T_j(n)=c_n B_j\,d_{j,n}\,e_{\beta,j,n+2}.
}
\tag{15}
$$
这里的 $c_n$不是根据平方事后选号：按双核直接取
$\bar Z^n W^{n+2}$系数，所得为共同的
$a^n n!(n+2)!$乘两个已固定 coherent 变量尺度，
再乘(4)和共同 $\delta$相位。
(8)的 $M^{-(n+2)}$也只进 $c_n$。
有限剩余标量与 $B_j$的比由第4槽/真空槽固定一次，
对所有 $n$保持。故(15)在某个 $d_{j,n}$为零时同样成立。

下文只在每个正整数权使用(15)，从不声称 $c_n$、
其中的 factorial 或裸 $p^n$本身具有 $p$-adic 连续延拓。

## 6. fixed-base 的全部 $p^2$ 级结构：正权因子

设 $H=\delta_3^nV_j$，$w=3+2n$。
按原 $a_p=0$、$\epsilon(p)=-1$规范，
$$
H^{[p]}=H-p^{2n+2}V_p^2H.
\tag{16}
$$
其中 $p^{2n}$来自 $\delta_3^nV_p^2=p^{2n}V_p^2\delta_3^n$，
不可遗漏 Kodaira--Spencer 费用。

令 $M_p=p(p+1)$，对固定底曲线 $A$的全部 cyclic
$D\subset A[p^2]$，写 $\lambda_D:A\to A/D$并置
$C_2H=\sum_D\lambda_D^*H$，这里是真正的 $\omega^{\otimes w}$
拉回。一次完整 degree-$p$商算子为 $T_1=pT_p^{(w)}$，
且 $T_p^{(w)}H=p^na_pV_j=0$。
两次商分为 cyclic $p^2$商和 $(p+1)$条中央 $[p]$路径，
所以
$$
C_2H=-(p+1)[p]^*H=(p+1)p^wH.
\tag{17}
$$
最后一步使用完整 nebentypus：$[p]^*H=-p^wH$。

在每个固定级结构上，$V_p^2=p^{-2w}\lambda_D^*$；
这可在 Tate $u\mapsto u^{p^2}$、微分倍率 $p^2$处逐式核定。
故
$$
\boxed{
\sum_DH^{[p]}(A,D)
=\left(M_p-p^{2n+2-2w}(p+1)p^w\right)H(A)
=M_p(1-p^{-2})H(A).
}
\tag{18}
$$
该数在每个正整数 $n$都非零。这不是从负二的 fp 等式倒推，
也不是新底曲线 $A/D$上 canonical incoming trace；
后一操作在原完整 imprimitive 求和中为零，结论保持不变。

## 7. 局部连续族及其确切负二配对

这里只使用 Kriz 已发表 monograph 的局部 $q_{\rm dR}$
构造：Theorem6.21、Propositions7.7、7.15、7.20及
Corollary7.21/Proposition7.22，并使用§9.3(9.7)--(9.18)
对局部原函数的识别。**不使用**其全球 Theorem9.10 中
cyclic Heegner cycle 的应用。

### 7.1 准确参数域与 CM 点

在一个共同含系数的完备域中固定 $A=E_{27}$的
$p^\infty$基 $\alpha$，取 Proposition7.7 的 inert CM 规范。
本题 CM order 的导子为1、$p\nmid306$、$p>3$；
$K_p/\mathbf Q_p$为不分歧二次扩张。
其 Hodge--Tate 和 de Rham period 的估计给 $b=1$；
把 $y=(A,t,\alpha)$变为
$y'=y\operatorname{diag}(p,1)$后，满足 Theorem6.21 的严格界
$|\theta(y_{\rm dR})p/\hat z|<p^{1/(p-1)}$。
不是声称原 $A$存在 canonical subgroup。

为同时满足 Proposition7.15 写出的 $m\ge2$，可先在
$\Gamma(2,2)$上工作；其 invariant affinoid neighborhood
由该命题给出。三个 $V_j$都在同一个 neighborhood。
然后沿局部构造的 tame finite étale 拉回到原 full9 覆盖；
连接、period、Frobenius 和 $q_{\rm dR}$展开全部自然拉回。
原3处 wild conductor 不进入这些 $p$处估计。

选择一个 cyclic $D$的生成元只是用来升到该辅助级别。
正整数权的结果在更换生成元后相同，所以连续延拓也相同；
忘掉生成元不作一次带 $p$分母的新平均。

参数固定为
$$
n(u)=(p^2-1)u-2,\qquad v(u)=(p-1)u,\qquad u\in\mathbf Z_p.
\tag{19}
$$
正整数 $u$给 $n\ge0$、$n\equiv4\bmod6$，
并全部位于 Theorem6.21 的同一 $n\equiv-2\bmod(p-1)$支。
它们在 $\mathbf Z_p$稠密：任意模 $p^s$的类都有任意大的
正整数代表。乘以 $p-1$是 $\mathbf Z_p$的同胚。
这明确给出了所用稠密集及其实际定义域。

### 7.2 全 $p^2$ orbit 的共同周期

$\mathcal O_{K,p}^\times$在 cyclic $p^2$子群上可递，
稳定子模 $p^2$为 $(\mathbf Z/p^2)^\times$，
所以 orbit 准确有 $M_p=p(p+1)$项。
每个代表可用 CRT 选一个 $\alpha_D\in\mathcal O_K$，
满足指定的模 $p^2$单位值及 $\alpha_D\equiv1\bmod306$。
在原理想规范下
$$
\psi_{27}((\alpha_D))=\alpha_D,\qquad
\eta_j((\alpha_D))=1.
$$
记正权 algebraic character 为
$$
\chi_{j,n}=\eta_j\psi_{27}^{n+3}\bar\psi_{27}^{-n}.
$$
则局部 toric 求和中真正出现的系数是
$$
(N_K^n\chi_{j,n})^{-1}((\alpha_D))
=\alpha_D^{-(3+2n)}.
\tag{20}
$$
主理想作用后仍是同一个 $A$和同一个 tame level；
运输的微分为 $\alpha_D^{-1}\omega_A$，其 weight-$3+2n$
值正好乘 $\alpha_D^{3+2n}$，与(20)抵消。
所以原全 orbit 是固定底曲线的全 $D$和，不能换成新的
conductor-$p^2$底曲线。

$K_p$剩余域为 $\mathbf F_{p^2}$，故(19)也使(20)的单位幂
在这一个支上连续。所有 $j$使用同一基 $\alpha$和同一 period；
不会有三个不相干的 $p$-adic CM 周期。
原54的有限算子已在§2移到 $V_j$上，故这同时保留原54、
$e_{\eta_j}$和全部 Cor。

### 7.3 负二必须用整个 $\mathcal H$-值原函数

按上述局部构造及(20)作完整求和，得到连续函数
$\mathcal L_{j,p}(u)$。正整数 $u$处，(4)、(18)及
CM period 比较给
$$
\mathcal L_{j,p}(u)=q_{p,n(u)}\,\mathcal T_j(n(u)),
\tag{21}
$$
其中 $q_{p,n}$对三个 $j$完全相同且非零。
它保留原 $M_p(1-p^{-2})$、实际 level 微分比较 period、
同一 $p^\infty$基的 CM period 和(4)的 $34^n$。
(21)只在正整数权使用；从未要求这些因子分别连续。

端点必须按 Kriz (9.15)--(9.18)取得：
$k=3,r=k-2=1$，取其中的 $j=1$，得到 $H_{-2}$
与整个 $\mathcal H$-值 Coleman 原函数对 $\omega_A$的配对。
不能把只在 $j\ge-k/2$先下降的标量 $G_j$直接代入 $j=-2$。
先由 $G_{-1}$识别原函数，再用 (9.15)--(9.16)的配对，
才得到所需的最高线。

该原函数的水平规范也固定。采用 R997§4 的完整 BDP
多项式条件：多项式杀 parabolic $H^1$中的给定类、在局部
解析水平截面上可逆，且在1不为零。其存在由权重2和1分离。
原函数满足该多项式作用后的 rigid 条件；再以原全 level
monodromy 的两个不同固定线幺幂矩阵排掉剩余全局 rigid
水平截面。故不是任取一个局部积分常数。
在普通 locus 与 $p$-depleted $q$展开的原函数相同，
沿上述 admissible neighborhood 的刚性延拓保持相同。
在本题它准确是
$$
\mathcal G^{\rm out}(A,D)
=\mathcal G(A)-p^{-2}\lambda_D^*\mathcal G(A/D).
\tag{22}
$$

[固定底曲线 $p^2$ 笔记](2026-11-27-original-inert-fixed-base-p-square-depletion-and-fp-parameter.md)
已用实际 degree34 图的完整 Chow 推前支付
$$
\mathcal A^{\rm out}_{j,p}
 =M_p(1-p^{-2})\operatorname{AJ}_p(Y_{j,0})(\Omega\omega_A)
 =(p^2-1)I_{j,p}.
\tag{23}
$$
因此局部(9.17)--(9.18)的同一非零 period 倍率给
$$
\mathcal L_{j,p}(0)=q_{p,-2}^{\rm fp}I_{j,p},
\qquad q_{p,-2}^{\rm fp}\ne0,
\tag{24}
$$
且该倍率对三个 $j$相同。这里保留 $p^2-1$、$p/(p+1)$及
负一权的 CM period；没有将它们当成1。
所用三图/54图/Cor 的系数均为原模型给定值，不随 $j$
另行修正相位。

## 8. 在正权先消去所有共同因子，再取端点

把(13)--(15)代入(21)，对每个正整数 $u$，令
$k=v(u)=(p-1)u$。由于 $n=dk-2$，有
$$
\mathcal L_{j,p}(u)
=q_{p,n}c_n B_j\,
 \frac{pk(CC_\beta)^k}{(k!)^2}\,
 K_{j,p}(k)J_{\beta,j,p}(k).
\tag{25}
$$
全部随权 factorial、$p$幂、period 和同源尺度都出现在
这个**共同**因子中。无需除以某个可能为零的 $d_{j,n}$。
逐项交叉相乘便得
$$
\begin{aligned}
\mathcal L_{j,p}(u)B_l
 K_{l,p}(v(u))J_{\beta,l,p}(v(u))
={}&
\mathcal L_{l,p}(u)B_j
 K_{j,p}(v(u))J_{\beta,j,p}(v(u)).
\end{aligned}
\tag{26}
$$
两边已由前节构造为 $\mathbf Z_p$上的连续函数。
正整数稠密，故(26)在整个参数域成立。取 $u=0$，
用(12)、(24)并消去共同非零 $q_{p,-2}^{\rm fp}$，
恰得(2)。

这一论证没有构造 $n!/k!$的 Gamma 插值，也没有把
$p^n$按整数权公式延拓到负整数。共同因子只在真实正权处
逐项消掉，最后被取极限的是已经构造的连续 cross identity。

最后设 $K_{j_0,p}(0)$为单位。按(2)定义
$$
F_p^{\rm geom}
=\frac{I_{j_0,p}}{B_{j_0}K_{j_0,p}(0)}.
$$
R1049 的整格及未平方来源笔记的已付首层式为
$$
\overline{I_{j,p}}
=-[L:H]\,\overline{B_j}\,\overline{K_{j,p}(0)}.
\tag{27}
$$
$B_j$及 $[L:H]=432$在删去的固定坏集外均为单位。
因此 $F_p^{\rm geom}$是单位且剩余值为 $-[L:H]$，
而(2)给全部三个等式(3)。

从而任何**实际同一来源**的线性组合都满足
$$
\sum_j b_j h_{j,p}
=F_p^{\rm geom}
 \sum_j b_j\frac{B_j}{a_j}K_{j,p}(0).
\tag{28}
$$
(28)不授权把原 Sha-bad 只给的一条带外项关系，
升级成三条 $K_{j,p}(0)=0$；也不提供无穷 $p$的非零输入。

## 原始来源和已付依赖

- D. J. Kriz, *Supersingular p-adic L-functions, Maass--Shimura
  Operators and Waldspurger Formulas*, Annals of Mathematics Studies212,
  Princeton University Press, 2021。
  [出版社](https://press.princeton.edu/books/paperback/9780691216461/supersingular-p-adic-l-functions-maass-shimura-operators-and)
  及[原书全文转录](https://dokumen.pub/supersingular-p-adic-l-functions-maass-shimura-operators-and-waldspurger-formulas-ams-212-9780691225739.html)：
  Theorem6.21 pp186--190，§7.3 pp208--215，
  §9.3 pp243--248，特别(9.15)--(9.18)。
- R997§4：原曲面的完整 Frobenius/水平规范；R1006(22)：
  原有限邻点与 raised operator 的真实 KS 比例。
- 未平方来源笔记§§2--8、10--11：实际 finite Schwartz、
  完整双核、原 $B_j$及两条 Hermite 槽。
- R301、原负二 Newton 笔记：唯一 $c_\sigma$的高尾界及(1)。
- 固定底曲线 $p^2$笔记：所有 cyclic $D$的完整 Chow 图及
  (23)；R1049§§11--14：整格、$\alpha_p$和原模 $p$定标。
