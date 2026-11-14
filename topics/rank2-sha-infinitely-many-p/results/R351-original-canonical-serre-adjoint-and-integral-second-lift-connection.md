# R351：原典范来源的整 Serre 伴随与第二提升连接

日期：2026-11-13。**状态：以下原次数二算子的完整带权 Serre 转置、真正二阶余像的整左核提升判据、两个原提升核之间的耦合连接余量，以及有理部分由原来源支付后的 \(\zeta\) 连接像约束均已证明。所有算子作用于 R335 的整个 canonical 原来源；保留 charge40、十三行运输、额外一次行移和首次 Bockstein 像。没有把单独的 \(Z_p^{-1}\) 极当作原余像，也没有给新来源附加中央零。**

## 1. 原来源、两个完整目标与实际整矩阵

沿 R338、R342、R352，取
\[
p=6s-1,\quad s>13,\quad1\le\ell<s-13,\quad
L=2s+\ell,\quad T=L+13,\quad b=17.
\]
系数环为原惰性位的整数环 \(\mathcal O\)，剩余域为 \(k\)；所有固定坏素数按所引原整格排除。令
\[
h_7=16t^2+4t+7,\quad a=t(t-1)h_7,\quad
\chi=(t-1)(1+8t)h_7,\quad t=-b/x^3,\quad w=z^6.
\]
为避免与实际常数 \(a_p\) 混淆，\(a\) 在本篇只表示这个角多项式。

用 \(\mathscr R\) 表示相对径向变量。整个已付来源为
\[
\mathcal V_{\le D}=\bigoplus_{n=0}^{D}\mathcal V_n,\qquad
\mathcal V_n=\mathscr R^n q_n(t)\mathcal O[t]_{\le e_{n+1}},
\]
\[
q_n=\frac{(t h_7)^{\lfloor(n+1)/4\rfloor}
(t-1)^{\lfloor(n+1)/3\rfloor}}{(1+8t)^{\lfloor n/2\rfloor}},
\quad
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2.
\tag{1}
\]
乘回原 \(G_0\) 后的 charge 是 \(n+40\)。这不是另加的全纯角格。

沿 R342 可取原 Gaussian 规范或同时重标后的规范；以下统一记为
\[
\rho=\Theta^{17}(1+8t),\quad
g=e^{-\kappa w^s}\rho,\quad a_p=p\kappa\in\mathcal O^\times,
\quad
\mathscr R_{\rm phys}=g e_2(a_p\epsilon),\quad w^s=p\epsilon.
\tag{2}
\]
R342 已证明两种同时重标给同一个原矩阵。令
\[
Y_-=\Gamma_T,\quad Y_+=\Gamma_{T+1},\qquad
M_-=m_{13}J_{D,L},\quad M_+=m_{13}J_{D+2,L+1}.
\tag{3}
\]
这里 \(J(\Phi)=\Phi(\mathscr R_{\rm phys},t(w))\)，\(m_{13}\) 是实际乘 \(w^{13}\)；
\(\Gamma_N\) 保留全部除幂关系及长度 \(N\) 的整基
\[
e_r=w^r/p^{\lfloor r/s\rfloor},\quad0\le r<N.
\]
\(M_+\) 的第三相对块长度是 \(\ell+1\)。即使其达到 \(s-13\)，
仍有 \(T+1\le3s\)，同一个三块整目标与完整边界均有定义。
没有将末行抹去以使两个目标相同。

置
\[
\mathcal E=\mathscr R\partial_{\mathscr R},\quad
\mathsf E=w\partial_w,\quad \mathsf E\epsilon=s\epsilon,
\quad L_0=(\mathsf Eg)/g,\quad
\Lambda=L_0+s a_p\epsilon,
\]
\[
\nu=\frac{(1-t)^{-1/2}}{h(t)},\qquad
h(t)=z\sqrt x,\qquad
W=\mathscr R^2a\chi,\qquad
B=W_{\rm phys}\nu .
\tag{4}
\]
\(B=-49b\,w+\cdots\) 是同一个完整目标中的 \(w\) 乘整单位。
因此它给真正的整映射 \(Y_-\to Y_+\)。
任何输入遗漏的第 \(T\) 行在乘 \(B\) 后落于截断外，故下式不需要未知输入尾。
R352 的原恒等式准确为
\[
\boxed{
M_+\mathcal Q
 =B\{(\mathsf E-13)M_- -\Lambda M_-\mathcal E\},
\qquad \mathcal Q=W\,t\partial_t .
}
\tag{5}
\]
\(\mathcal Q\) 保持 \(\mathscr R\) 不动，且
\(\mathcal Q\mathcal V_n\subset\mathcal V_{n+2}\) 已由真实零极逐点支付。
原来源的两条接触尾仍由同一个 \(\Phi,\mathcal E\Phi\) 给出。

## 2. 二阶对偶恰是可提升的整左核

对任意有限自由整模映射 \(F:V\to Y\)，记
\[
K_1(F)=\ker\bar F,\quad
C_1(F)=\operatorname{coker}\bar F,\quad
C_2(F)=C_1(F)/\beta_1^F(K_1(F)).
\tag{6}
\]

**定理1。** 把 \(C_2(F)^\vee\) 看作 \((Y/pY)^\vee\) 的子空间，则
\[
\boxed{
C_2(F)^\vee
=\{\lambda_0:\ \text{存在 }\lambda_2\in(Y/p^2Y)^\vee,\ 
\lambda_2\bmod p=\lambda_0,\ \lambda_2F=0\bmod p^2\}.
}
\tag{7}
\]
所以本篇的二阶对偶总有实际整左核提升，不能用任意模 \(p\) Laurent 核替代。

**证明。** 先有 \(\lambda_0\bar F=0\)。取任意整提升 \(\lambda\)，则
\(\lambda F/p\bmod p\) 是 \(V/pV\) 上的线性函数。
它在 \(K_1(F)\) 上的值正是
\(\lambda_0\beta_1^F\)。若此值为零，该函数通过
\(\operatorname{im}\bar F\) 分解；把其负数延拓到整个 \(Y/pY\)，得到一个
\(\lambda_1\) 满足
\[
\lambda_1\bar F=-\overline{\lambda F/p}.
\]
于是 \(\lambda+p\lambda_1\) 是所需提升。反向将一个满足
\(\lambda_2F\equiv0\pmod{p^2}\) 的提升作用于 \(P\in K_1(F)\)，
除以 \(p\) 后得到 \(\lambda_0\beta_1^F(P)=0\)。\(\square\)

两个这种提升之差为 \(p\mu\)，其中
\(\bar\mu\bar F=0\)。这里不要求 \(\bar\mu\) 再杀掉 \(\beta_1\)；
后文的提升不变性会支付这个完整自由度。

本篇分别把 (7) 用于 \(M_-\) 与 \(M_+\)。一个右首核
\(\bar P\in\ker\beta_1^{M_-}\) 也恰有真正的模 \(p^2\) 核提升 \(P_2\)。
更换 \(P_2\) 的全部自由度是 \(pQ\)，其中
\(\bar Q\in K_1(M_-)\)。这正是 R338 的短正合列，未删掉首 Bockstein 像。

## 3. 真正带 \(p\) 权的 Serre 核

取 \(Y_+\) 上一个整行 \(\lambda\)，令 \(\lambda_r=\lambda(e_r)\)。
对应的物理 Laurent 微分必须是
\[
\boxed{
\mathcal L_\lambda(w)\,dw
=\sum_{r=0}^{T}\lambda_r\,p^{\lfloor r/s\rfloor}w^{-r-1}\,dw .
}
\tag{8}
\]
因为物理级数 \(F(w)=\sum f_rw^r\) 在 \(e_r\) 基中的坐标是
\(p^{\lfloor r/s\rfloor}f_r\)，故
\[
\langle\lambda,F\rangle
=\operatorname{Res}_{w=0}F(w)\mathcal L_\lambda(w)\,dw.
\tag{9}
\]
若删掉 (8) 的 \(p\) 权，得到的不是原整矩阵的对偶。

在特征零形式原点令
\[
\Omega_{\lambda,n}
=w(t)^{13}\rho(t)^n\mathcal L_\lambda(w(t))\frac{dw}{dt}\,dt,
\qquad \omega_{\lambda,n}=\Omega_{\lambda,n}/dt.
\tag{10}
\]
此处 \(\rho\) 是整个原 theta frame；
\(w=(-t/b)h(t)^6\) 以及 \(w^{13}\) 均保留。
这些是有限极部决定的形式 Laurent 微分。
计算先在分式域进行；最终的残数由原整矩阵保证属于 \(\mathcal O\)，
再取模 \(p^r\)，不将可能含分母的中间 theta 系数分别约化。

对 \(\Phi=\mathscr R^n f(t)\in\mathcal V_n\)，准确有
\[
\boxed{
\langle\lambda,M_+\mathcal Q\Phi\rangle
=-\operatorname{Res}_{t=0}
 f(t)\,d\!\left(t\,a(t)\chi(t)\,\omega_{\lambda,n+2}(t)\right).
}
\tag{11}
\]
证明只用
\[
M_+\mathcal Q\Phi=w^{13}\rho^{n+2}a\chi\,t f'(t)
\]
及形式分部积分
\(\operatorname{Res}d(f\,t a\chi\,\omega)=0\)。
这给整个原 \(q_nt^j\) 基上的准确有限伴随，不用一个未付的全局 theta 商代替它。

特别当 \(\lambda_2\) 是 \(M_+\) 的模 \(p^2\) 整左核时，
(11) 对全部原 \(f=q_nt^j\) 的残数为零模 \(p^2\)。
这是这些实际测试函数上的残数矩条件，尚不是每个非原点极部逐个为零。

## 4. 不假设 Euler 保持核的完整连接余量

R338 的目标 Euler 计算先给一个对整个原首核都成立的事实：
\[
\boxed{\bar P\in K_1(M_-)
\quad\Longrightarrow\quad
\epsilon\,\bar M_-(\mathcal E\bar P)=0.}
\tag{12}
\]
确实，若 \(J(\bar P)\in\mathcal B_{13}=\ker\bar m_{13}\)，则
\[
\epsilon\bar J(\mathcal EP)
=a_p^{-1}(\epsilon\partial_\epsilon)\bar J(P).
\]
\(\epsilon\partial_\epsilon\) 保持两条十三行边界 \(\mathcal B_{13}\)；
乘 \(\bar m_{13}\) 后得到 (12)。
它没有断言 \(\bar M_-(\mathcal EP)=0\)。

现在取
\[
\bar P\in\ker\beta_1^{M_-},\qquad
\lambda_0\in C_2(M_+)^\vee,
\]
并取真正提升
\[
M_-P_2=0\bmod p^2,\qquad \lambda_2M_+=0\bmod p^2.
\tag{13}
\]
将 (5) 作用于它们，得到完整的有限恒等式
\[
\boxed{
\langle\lambda_2,B L_0 M_-(\mathcal EP_2)\rangle
+s a_p\langle\lambda_2,B\epsilon M_-(\mathcal EP_2)\rangle
\equiv0\pmod{p^2}.
}
\tag{14}
\]
右侧没有省去输入 Euler 行；
第一项中的 \(L_0\) 保留 \(g\) 的完整实际高轴。

由 (12)，(14) 第二项被 \(p\) 整除，故第一项也被 \(p\) 整除。
因此可定义实际连接余量
\[
\mathfrak r_{\mathcal Q}(\lambda_0,\bar P)
=\overline{\frac1p
 \langle\lambda_2,B L_0 M_-(\mathcal EP_2)\rangle}.
\tag{15}
\]

**定理2。** (15) 与两边的第一次提升无关，是
\[
C_2(M_+)^\vee\times\ker\beta_1^{M_-}\longrightarrow k
\]
上的双线性配对。若沿 R338 写同一 \(\bar P\) 的两条尾为
\[
D_1=a_p^{-1}[\mathscr S\bar W_0]_{<s},\qquad
D_2=[\mathscr S\bar W_1]_{<\ell},\qquad
\mathcal D(P)=(0,D_1,D_2),
\tag{16}
\]
则准确有
\[
\boxed{
\mathfrak r_{\mathcal Q}(\lambda_0,\bar P)
=s a_p\,\lambda_0\!\left(\bar B\,\bar m_{13}\mathcal D(P)\right).
}
\tag{17}
\]
其中 \(W_i=(\mathcal E^iP)(g_<,t)\) 可沿 R338 取原低轴；改用实际 \(g\)
给同样的两条尾。所有截断按 (16) 保留。

**证明。** R338 对真正原 \(p^2\) 核的计算准确给
\[
\overline{\epsilon M_-(\mathcal EP_2)/p}
=-\bar m_{13}\mathcal D(P).
\tag{18}
\]
第二块末十三行的未定部分被实际 \(\bar m_{13}\) 消去；
第三块完整保留。因此 (14) 除以 \(p\) 即为 (17)。

为核定提升自由度，也可不借助右端重新检查。
若 \(P_2\) 改为 \(P_2+pQ\)，则
\(\bar Q\in K_1(M_-)\)。由 (5) 的模 \(p\) 式及 (12)，有
\[
\lambda_0\bar B\,\bar L_0\,\bar M_-(\mathcal E\bar Q)=0.
\]
这正是 (15) 的变化。
若 \(\lambda_2\) 改为 \(\lambda_2+p\mu\)，则
\(\bar\mu\bar M_+=0\)；把同一个计算用于 \(\bar P\in K_1(M_-)\)
仍得到变化为零。改变整代表 \(p^2\) 倍也显然不影响 (15)。
这支付了第2节所列全部首次提升自由度。\(\square\)

式 (17) 是一个具体的原联系，不能把其左边任意置为零。
它读取真实 \(L_0\) 对尚未受控的 \(\mathcal EP\) 的第一整商，
因此不会从一个首核自动产生二阶零。

还能把右边写成原三块中的直接卷积。
令
\[
\beta(w)=[\,\bar g^2 a(\bar t)\chi(\bar t)\bar\nu\,]_{<s}
=-49b\,w+\cdots.
\]
普通整高系数在 \(w^s=p\epsilon\) 后模 \(p\) 消失，故
\[
\bar B=\beta(w)e_2(2a_p\epsilon),
\]
以及
\[
\boxed{
\bar B\,\bar m_{13}\mathcal D(P)
=\epsilon\,w^{13}\beta D_1
 +\epsilon^2w^{13}\beta(D_2+2a_pD_1)
}
\tag{19}
\]
于完整 \(Y_+/pY_+\) 中成立。式中乘积依该目标截断；
特别保留新增末行和原两条跨界带。
(19) 给 (17) 的实际有限矩阵，不把两条接触尾自由化。

## 5. 有理连接由真实原来源支付

下面将 (5) 的连接分成可由原来源支付的有理部分与实际 \(\zeta\) 部分。
原曲线规范为
\[
D_zx=2y,\quad D_zy=3x^2,\quad D_z\zeta=-x.
\]
从 \(t=-b/x^3\)、\(\rho=\Theta^{17}(1+8t)\)、\(\Theta=x\sigma^2\)
直接求导，得到完整恒等式
\[
\boxed{
\nu\mathsf E=-\frac{x}{6y}D_z,\qquad
\nu\Lambda=c(t)-\frac{17x\zeta}{3y},
\quad c(t)=\frac{8t}{1+8t}-\frac{17}{3}
=-\frac{17+112t}{3(1+8t)}.
}
\tag{20}
\]
第一式作用于整个物理级数。它不是只对一个截断项求导的近似式。

令
\[
A=Wc(t)
=-\frac{\mathscr R^2}{3}\,t(t-1)^2h_7^2(17+112t).
\tag{21}
\]
这是原归一化 \(\mathcal N_2\) 的真正元素：
相对于 R335 的次数二基本分式
\(\mathscr R^2t(t-1)h_7/(1+8t)\)，其商为
\[
-\frac13(t-1)(1+8t)h_7(17+112t),
\]
次数五，不超过原上界六。因此 \(A\mathcal V_n\subset\mathcal V_{n+2}\)，
同样 \(A\mathcal E\) 是原来源操作。

定义
\[
\boxed{\mathcal D_\zeta=\mathcal Q+A\mathcal E,\qquad
Z=W_{\rm phys}\frac{x\zeta}{y}.}
\tag{22}
\]
\(Z\) 是同一目标中的整乘子：
由 (20)，
\[
Z=\frac3{17}(A_{\rm phys}-B\Lambda).
\]
这里 \(17\) 已属于固定排除集合，右边各项是已付整算子。
近原点 \(x\zeta/y=-1+\cdots\)，所以 \(Z\) 仍只有一次物理行移。

**定理3（真实 \(\zeta\) 连接的原像约束）。**
整个原来源上准确有
\[
\boxed{
M_+\mathcal D_\zeta
=B(\mathsf E-13)M_-+\frac{17}{3}Z M_-\mathcal E.
}
\tag{23}
\]
因此对任意 \(r\ge1\)、任意实际 \(P_r\in K_r(M_-)\)，
\[
\boxed{
Z M_-(\mathcal EP_r)\in
\operatorname{im}(M_+\bmod p^r)\subset Y_+/p^rY_+.
}
\tag{24}
\]
更明确地，其原来源代表可取
\((3/17)\mathcal D_\zeta P_r\)。
所以对任何满足 \(\lambda_rM_+\equiv0\pmod{p^r}\) 的整左核，
\[
\boxed{\langle\lambda_r,Z M_-(\mathcal EP_r)\rangle\equiv0\pmod{p^r}.}
\tag{25}
\]

**证明。** (21) 保证
\(A_{\rm phys}M_-(\mathcal EP)=M_+(A\mathcal EP)\)，
乘子的一次物理零保证从输入长度 \(T\) 到输出长度 \(T+1\)
不需额外未给行。
把 (20) 代入 (5)，再将这条真正来源移到左边，即为 (23)。
对核 \(P_r\)，
\(B(\mathsf E-13)M_-P_r\) 被 \(p^r\) 整除，因为这两个目标算子整。
于是得到 (24)、(25)。\(\square\)

(24) 是原像成员性，未把 \(Z\) 当来源，也未把
\(\mathcal EP_r\) 当核。它保留整个 \(\zeta\) 连接；不通过删去
\(-17x\zeta/(3y)\) 得到零。

若把已付公共目标单位 \(U_0\) 乘回，
\(M^{\rm orig}=U_0M\)，则 (23) 的完整原形式为
\[
M_+^{\rm orig}\mathcal D_\zeta
=B\left(\mathsf E-13-\frac{\mathsf E U_0}{U_0}\right)M_-^{\rm orig}
+\frac{17}{3}Z M_-^{\rm orig}\mathcal E .
\]
\(U_0\) 在多一行目标上仍取同一个实际单位的截断。
因此 charge40 的连接没有丢失；在原核上这一项同样被 \(p^r\) 整除，
所以 (24)、(25) 通过该原整目标同构保持成立。

相应的完整 Serre 式也完全明确。对 \(\Phi=\mathscr R^nf(t)\)，
\[
\boxed{
\langle\lambda,M_+\mathcal D_\zeta\Phi\rangle
=\operatorname{Res}_{t=0}f(t)\left[
-d(t a\chi\,\omega_{\lambda,n+2})
+n a\chi\,c(t)\,\Omega_{\lambda,n+2}\right].
}
\tag{26}
\]
它给整个次数 \(n\) 来源的实际伴随。
系数 \(n\) 是原径向 Euler 值；没有将它替换为常数或删除。

## 6. 与 R346 的原留数比较：已付约束和剩余对象

在 R342 的模 \(p\) 实际窗口内，
\[
z\equiv Z_p,\qquad \nu\equiv-\frac{x}{yZ_p}.
\]
但是 (20) 同时说明
\[
\nu\mathsf E=-xD_z/(6y),\qquad
\nu\Lambda=c(t)-17x\zeta/(3y).
\]
所以原算子中的 \(Z_p^{-1}\) 移动分母在完整导数中消去。
不能只从 \(\nu\) 单项在 \(Z_p=0\) 有极，推出某个原测试极部非零。

另一方面，实际对偶 Laurent 核 (8) 在代入
\(w=Z_p^6\) 后仍可能产生这些移动极。
(11)、(26) 显示其正确读法：同时保留
\(p^{\lfloor r/s\rfloor}\)、\(w^{13}\rho^n\)、原角基与完整连接，
先作有限整残数再取所需提升层。
因此来源条件实际给的是这些指定微分的有限矩约束，以及
(17)、(24) 的实际整像条件。

R346 对一个已经给定的向量
\(q=(q_1,\ldots,q_K)\)、\(K=s-14\)，证明了原非原点残数映射单射。
用于原二阶问题时，这个向量必须仍准确是 R342 的
\[
q_n(\lambda,P)=\frac1{6n(6n+1)}
\left\{
\sum_{j=n}^{s-14}\lambda_{1,j+13}[w^{j-n}]D_1
+\sum_{j=n}^{\ell-1}\lambda_{2,j+13}[w^{j-n}]D_2
\right\}.
\tag{27}
\]
这里还需准确支付两个目标之间的对偶比较。
令 \(\pi:Y_+\to Y_-\) 删除新增末行，并置
\[
M^\flat=\pi M_+:\mathcal V_{\le D+2}\longrightarrow Y_-.
\]
一个 \(\mu_0\in C_2(M^\flat)^\vee\) 的真正整左核提升
\(\mu_2\) 同时给出：
\(\lambda_2=\pi^\vee\mu_2\) 是 \(M_+\) 的整左核；
\(\mu_2\) 限制来源次数到 \(D\) 后是 \(M_-\) 的整左核。
因此这些明确的共同对偶可同时用于 (17)、(24)、(27)，
两条 \(D_i\) 继续来自同一 \(P\)。

不能把任意 \(\lambda_2\in\ker(M_+^\vee\bmod p^2)\)
直接截去末坐标后称为 \(M_-\) 的左核。
若写
\(\lambda_2=\pi^\vee\mu_2+c\,e_T^\vee\)，则准确有
\[
\mu_2 M^\flat=-c\,e_T^\vee M_+\pmod{p^2}.
\]
这条真实末行必须保留。共同对偶的构造付出了它，
但本篇未预支该共同对偶的维数或声称它涵盖所有 R342 测试。

准确的下一比较因而是把 (17)、(24)、(26) 产生的整像条件，
作用于 (27) 在 R346 有限 étale 极部中的
\[
P_q(\xi)=\sum_{n=1}^{K}q_n b^n\xi^{K-n}A_n(\xi),
\qquad B_p(\xi)=0,\qquad \xi=-t.
\tag{28}
\]
不能从“\(\lambda\) 杀原像”单独令 \(P_q\) 为零：
在 (17) 中仍有确定的连接余量，
在 (26) 中仍有整个 \(\zeta\) 与 theta frame，
且 (27) 的两条尾未变成任意独立变量。

本篇不把这些剩余项视作无法再比较的抽象障碍。
(19)、(21)、(23) 给出了其全部有限来源和目标算子；
要将 R346 的非原点单射转为原 \(C_2\) 的约束，
现在可以直接检验这个具体原像，而不需假设 Euler 保持核或删除移动极。

原完整中央失败的输入仍只是 R338/R342 已付的聚合
\[
a_p c_1-pc_2\equiv0\pmod{p^2}.
\tag{29}
\]
(24) 来自真正来源恒等式，未给新的完整中央零；
特别未将 (29) 拆成逐中央权消失。

## 7. 所有固定成本和可核查依据

本篇使用原 charge \(n+40\)，算子增加 relative charge 二。
\(m_{13}\) 的两条十三行跨界带完整保留；
\(B\) 或 \(Z\) 的一次物理行移另有
\(r=s-1,2s-1\) 两条真实 \(p\) 边界。
没有把目标单位、矩阵转置或 (24) 的像成员性当作新增中央观察。

证明依赖原整格和整性窗口 R335、R338、R342，以及
R352 的完整来源闭合与多一行恒等式；
第2、3、4、5节分别给出所需的有限线性代数、形式残数、
提升相容性和实际椭圆微分计算。
这些是全体参数的证明，不以目标素数扫描代替。

本文件通过已授权的仓库连接器直接保存；同步方式是 GitHub API，
没有将其记为本地 git pull。核心索引与 HANDOFF 由根代理维护。
