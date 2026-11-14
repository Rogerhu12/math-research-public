# R363：原第一 Frobenius 商的闭合 Cartier 系统与二阶有理连接模型

日期：2026-11-13。**状态：以下原第一整商的准确有理 forcing、两个真实微分的有限 Cartier 闭合、原三块目标中完整模 \(p^2\) 的有理连接代表，以及该代表在全部真实测试点的精确零值和单位导数均已证明。它支付 R356 的 \(\mathcal A_\kappa\) 下一位，未将整个原 theta 或中央函数改为全局有理来源。所有整左核、首次提升像、charge40、十三行和公共 \(U_0\) 仍按 R351 保留。**

## 1. 同一原对象与可计算的首坏系数

保留 R356 的
\[
p=6s-1,\quad s>13,\quad b=17,\quad
E_b:y^2=x^3+b,\quad D=D_z,\quad Dx=2y,\quad Dy=3x^2.
\]
仍用
\[
n_0=(p-1)/2,\quad
\mathscr R_p(x)=\frac12\sum_{j=0}^{n_0}
\binom{n_0}{j}b^{n_0-j}\frac{x^{3j+1}}{3j+1},
\quad \widetilde Z=\mathscr R_p/y^p,\quad Z=\overline{\widetilde Z},
\]
\[
E_p=3x^2\mathscr R_p/y^{p+1},\qquad
D\widetilde Z=1-pE_p,\quad DZ=1,\quad D^p=0\ \text{于 }k(E_b).
\tag{1}
\]
所有分母仍为 \(p\) 单位。

令
\[
\xi_p=[z^{p-1}]x,\qquad
\kappa_\sigma=34[z^{p+1}]\log(\sigma/z),\quad
a_\sigma=p\kappa_\sigma,\quad
u_\sigma=\frac{(p+1)a_\sigma}{34}=-\xi_p .
\tag{2}
\]
这里的 \(\xi_p\) 不是未知原中央行；它是固定曲线 \(x(z)\) 的指定有限系数。
用 R342 的
\[
z=u h(t),\quad t=-bu^6,\quad
h(t)=\sum_{n\ge0}\frac{(1/2)_n}{n!(6n+1)}t^n,\quad u=x^{-1/2},
\]
Lagrange 公式准确给
\[
\boxed{
\xi_p=-\frac2{p-1}(-b)^s[t^s]h(t)^{-(p-1)}.
}
\tag{3}
\]
只需 \(h\) 的前 \(s\) 项，分母均整。
所以本篇全部有理 forcing 由固定的有限代数公式确定，不借目标素数扫描。

沿 R356 记
\[
c_p=\binom{3s-1}{2s-1}b^s\in k^\times,\qquad
\bar u_\sigma=-c_p,\qquad D^{p-1}(-x)=c_p\pmod p .
\]
令 \(f=-x\)，定义一个准确整多项式
\[
\boxed{
\widetilde T_p(x)=
\frac{\,D^{p-1}f/(p-1)!-u_\sigma\,}{p}
\in\mathcal O[x],\qquad \tau_p=\overline{\widetilde T_p}.
}
\tag{4}
\]
它的整性是系数逐项成立的：
\(D^{p-1}f\bmod p=c_p\) 是常数，
\((p-1)!\equiv-1\)，且 \(\bar u_\sigma=-c_p\)。
次数至多 \((p+1)/2=3s\)。
式 (3)、(4) 给出了这个整商的完整规范，没有把首坏系数改为可选参数。

## 2. 原第一整商的真实三角系统

用 R356 的特征零有限和
\[
\widetilde G_\sigma
=\sum_{i=0}^{p-2}\frac{(-1)^i\widetilde Z^{i+1}D^if}{(i+1)!},
\qquad
\widetilde H_f
=\sum_{i=0}^{p-2}\frac{(-1)^i\widetilde Z^iD^if}{i!}.
\]
在原已付局部窗口内定义
\[
z_1=\frac{z-\widetilde Z}{p},\qquad
j_1=\frac{\zeta_\sigma-\widetilde G_\sigma}{p}.
\tag{5}
\]
二者的整性分别由 R342、R356 保证；\(j_1\) 允许原点的一阶 Laurent 极。

特征零准确有
\[
Dz_1=E_p,
\]
\[
Dj_1=\widetilde Z^{p-1}\widetilde T_p+
u_\sigma\frac{\widetilde Z^{p-1}-z^{p-1}}p+
E_p\widetilde H_f.
\tag{6}
\]
第二式正是 R356 的完整 defect，不是一个删去了形式对数的方程。

以下在 \(k\) 上计算，条上横线只在可能混淆时写出。置
\[
e=\bar E_p=Z\,D\log y,\qquad
H_f=\overline{\widetilde H_f}.
\]
因 \(z=\widetilde Z+pz_1\)，准确有
\[
\overline{\frac{\widetilde Z^{p-1}-z^{p-1}}p}
=Z^{p-2}z_1.
\]
故原第一整商满足
\[
\boxed{
Dz_1=e,\qquad
Dj_1=Z^{p-1}\tau_p+eH_f-c_pZ^{p-2}z_1.
}
\tag{7}
\]

定义真实有限 Taylor 投影
\[
\Pi_Z(F)=\sum_{i=0}^{p-1}\frac{(-Z)^iD^iF}{i!}.
\tag{8}
\]
因为 \(DZ=1,D^p=0\)，逐项相消给 \(D\Pi_Z(F)=0\)，即
\(\Pi_Z(F)\in k(E_b)^p\)。
沿 \(1,Z,\ldots,Z^{p-1}\) 的 \(k(E_b)^p\)-基，
\(\Pi_Z\) 恰读取常数分量；它不是乘法同态。

对 \(f=-x\)，
\[
\Pi_Z(f)=H_f-c_pZ^{p-1}.
\]
所以取
\[
\boxed{
j_0=j_1-c_pZ^{p-1}z_1,\qquad
\mathfrak F_p=Z^{p-1}\tau_p+e\,\Pi_Z(-x),
}
\tag{9}
\]
就得到真正的有理 forcing
\[
\boxed{Dj_0=\mathfrak F_p\in k(E_b).}
\tag{10}
\]
这等式首先指原有限局部整商；未预设 \(j_0\) 是全局有理函数。

Gaussian 重标不会更换这个实际模 \(p\) 整商。
若 \(\kappa=\kappa_\sigma+\Delta\) 以及
\(\delta_\kappa=(p+1)\Delta/34\)，则
\[
j_{1,\kappa}-j_{1,\sigma}
=-\delta_\kappa\,\frac{z^p-\widetilde Z^p}{p}\in p\mathcal O[[z]]
\tag{11}
\]
于原窗口中，因为 \(z-\widetilde Z=pz_1\)。
故下文的 \(j_0,\mathfrak F_p\) 和实际下一位代表都不依赖这一整重标。

## 3. 第一微分的全部 Cartier 常数

置
\[
\omega_1=e\,dz,\qquad \omega_2=\mathfrak F_p\,dz .
\tag{12}
\]
首先有一个直接的原角向式
\[
\boxed{
e(t)=-3\,\frac{B_p(-t)}{(1-t)^{(p+1)/2}},
\qquad
B_p(\xi)=\sum_{j=0}^{n_0}\binom{n_0}{j}\frac{\xi^j}{6j+1}.
}
\tag{13}
\]
它由 (1) 的真实 \(\mathscr R_p\) 反序得出；
特别没有为求测试根值而另加覆盖。

令
\[
c_A=\frac34 b^{5s-1}\frac{(3s-1)!}{(4/3)_{3s-1}},
\qquad
\lambda_p=\frac{2c_A}{3b}
=\frac12 b^{5s-2}\frac{(3s-1)!}{(4/3)_{3s-1}} .
\tag{14}
\]
两者都是 \(k^\times\)，而且属于 \(\mathbf F_p\)。
分母中的每个因子都不是 \(p\) 的倍数。

**定理1。** 实际第一微分满足
\[
\boxed{
\mathcal C\omega_1
=c_A\,\frac{x\,dx}{y^3}
=\lambda_p\{d(x^2/y)-x\,dz\},
}
\]
\[
\boxed{
\mathcal C^2\omega_1=-\lambda_pc_p\,dz\ne0,\qquad
\mathcal C^3\omega_1=0.
}
\tag{15}
\]

**证明。** 由 (1)
\[
\omega_1=\frac32
 \frac{x^2\mathscr R_p(x)(x^3+b)^{p-1}}{y^{3p}}\,dx.
\]
分子只含 \(x^{3j}\) 型幂；其次数小于 \(5p-1\)。
Cartier 所读的 \(kp-1\) 指数中，唯一可能的是 \(2p-1\)。
其系数为
\[
\frac34 b^{5s-1}
\sum_{j=0}^{n_0}\frac{(-1)^j\binom{n_0}{j}}{3j+1}
=\frac34 b^{5s-1}\frac{n_0!}{(4/3)_{n_0}}=c_A.
\]
最后的有限和由 beta 多项式积分或逐项有理积分直接证明。
这给第一式。又
\[
d(x^2/y)-x\,dz=3b\,x\,dz/y^2,
\]
配合 R356 的 \(\mathcal C(x\,dz)=c_pdz\)、\(\mathcal C(dz)=0\)，
得到其余各式。\(\square\)

这里的单位是指定原第一 Frobenius 商的 Cartier 常数，
不是原完整中央导数的单位。

## 4. 第二微分的完整有限 Cartier 闭合

**定理2。** 第二微分满足准确关系
\[
\boxed{
\mathcal C^2\omega_2=-c_p\,\mathcal C\omega_1,\qquad
\mathcal C^3\omega_2=\lambda_pc_p^2\,dz\ne0,\qquad
\mathcal C^4\omega_2=0.
}
\tag{16}
\]
并且
\[
\boxed{\mathcal C\omega_2+c_p\omega_1=dR_p^\dagger}
\tag{17}
\]
有一个明确的有理原函数。

**证明。** \(\Pi_Z(-x)\) 在 \(O\) 至多有二阶极，
但它是 \(p\) 次幂，故实际上在 \(O\) 正规；
其 \(\mu_6\) 型为 \(-2\)，所以在那里还有零。
结合 \(\deg\tau_p\le3s\)，得到 \(\omega_2\) 在 \(O\) 至多双极。
从 (9) 及 \(j_0=z^{-1}+\cdots\) 可读出其主部为
\(-z^{-2}dz\)。

除 \(O\) 外，\(\omega_2\) 只在三个非零二挠点有极，
极阶至多 \(p^2+1\)。它在 \([-1]\) 下为奇型微分，
因此这些固定点和 \(O\) 的残数全为零。
Cartier 后在 \(O\) 已正规；
两次 Cartier 后仅可能在三个二挠点有双极。

现在固定一个二挠点，取真实局部参数 \(v=y\)，写
\(Z=a v^{-p}+\cdots\)，其中 \(a\ne0\)。
因为
\(\Pi_Z(-x)=H_f-c_pZ^{p-1}\)，最高极部准确为
\[
\omega_1=a v^{-p-1}\,dv+\cdots,\qquad
\omega_2=-c_pa^p v^{-p^2-1}\,dv+\cdots.
\]
两次 Cartier 后，第二式的双极系数为
\(-c_pa^{1/p}\)，恰是第一式一次 Cartier 双极系数的 \(-c_p\) 倍。

两次 Cartier 保持 \(\omega_2\) 的 \(\mu_6\) 型 \(-1\)。
在 \(O\) 正规、仅在三个二挠点有至多双极且具有此型的微分空间
准确为一维，由 \(x\,dx/y^3\) 张成：
乘 \(y^2/dz\) 后，得到 \(L(6O)\) 中型为 \(-2\) 的函数，
只有 \(x\) 这一维。
因此上述主部比较给 (16) 第一式；
余式由 (15) 得出，末常数是明确单位。

令
\[
h^\dagger=(\mathcal C\omega_2+c_p\omega_1)/dz.
\]
(16) 说明 \(\mathcal C(h^\dagger dz)=0\)，等价于
\(D^{p-1}h^\dagger=0\)。
所以可准确取
\[
\boxed{
R_p^\dagger=
\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^ih^\dagger}{(i+1)!}.
}
\tag{18}
\]
R356 的有限求导恒等式立即给 \(DR_p^\dagger=h^\dagger\)，
证明 (17)。\(\square\)

还有一个完全明确的第一次 Cartier 表达：
若
\[
L_p^p=\Pi_Z(-x),\qquad M_p^p=\Pi_Z(\tau_p),
\]
则两者的 \(p\) 次根均在原函数域中，且
\[
\boxed{
\mathcal C\omega_2=M_p\,dz+L_p\,\mathcal C\omega_1.
}
\tag{19}
\]
因此
\[
\langle\omega_1,\omega_2,\mathcal C\omega_2,
                    \mathcal C\omega_1,dz\rangle_k
\]
是一个至多五维、真正闭合的 Cartier 空间。
这里保留实际微分，不先商掉 exact 项；
(18) 也保留它的全部固定二挠极，不声称存在没有这些极的原函数。

## 5. 支付原 \(\mathcal A_\kappa\) 的全部模 \(p\) 系数

R356 修正后的准确首项常数为
\[
\lambda_{\rm lin}=(1-3p)^{-1},\quad
c_{\rm lin}=\sum_{j=1}^{p-1}\lambda_{\rm lin}^{\,j},\quad
\eta_{\rm lin}=(c_{\rm lin}+1)/p\in1+p\mathcal O .
\]
其实际下一位为
\[
\mathcal A_\kappa=
(x/y)j_{1,\kappa}+\eta_{\rm lin}\in w\mathcal O[[w]].
\tag{20}
\]
式 (11) 保证其模 \(p\) 不依赖 Gaussian 整重标。

在 (9) 中，\(z_1\) 至少有一阶零，
故 \((x/y)Z^{p-1}z_1\) 从 \(z^{p+1}=w^s\) 起。
在原目标模 \(p\) 中 \(w^s=0\)，所以
\[
\bar{\mathcal A}_\kappa
=1+(x/y)j_0\pmod{w^s}.
\tag{21}
\]

对实际有理 forcing \(\mathfrak F_p\)，再定义
\[
G^{(1)}_p=
\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^i\mathfrak F_p}{(i+1)!},
\qquad
\boxed{r^{(1)}_p=(x/y)G^{(1)}_p\in k(t).}
\tag{22}
\]
有
\[
DG^{(1)}_p=\mathfrak F_p+Z^{p-1}D^{p-1}\mathfrak F_p.
\]
\(\mathfrak F_p\) 在 \(O\) 只有双极，故
\(D^{p-1}\mathfrak F_p\) 在 \(O\) 正规：
它是一个 \(p\) 次幂，而双极的最高导数系数含 \(p!\)。
因此附加项至少从 \(z^{p-1}\) 起。
\(j_0\) 与 \(G^{(1)}_p\) 具有相同的 \(1/z\) 主部和型 \(-1\)；
其差在 \(z^p\) 之前没有可留下的导数零项。
于是
\[
j_0\equiv G^{(1)}_p\pmod{z^p},
\]
并得到原目标中的完整结论
\[
\boxed{\bar{\mathcal A}_\kappa=1+r^{(1)}_p(t(w))
\quad\text{于原 }\Gamma_{T+1}/p.}
\tag{23}
\]
所有普通 \(w^s\) 高项都由真正的 \(w^s=p\epsilon\) 支付；
在 R356 中它们还乘一个 \(p\)，故准确升到 \(p^2\)，不是任意截尾。

## 6. 实际测试点上的准确双零

在任一 R346 测试点 \(P\)，有 \(Z(P)=0\)，且 \(x,y\) 都为单位。
由
\[
\mathfrak F_p=Z^{p-1}\tau_p+
 Z\,D\log y\,\Pi_Z(-x),\qquad \Pi_Z(-x)(P)=-x(P),
\]
准确得
\[
\mathfrak F_p(P)=0,\qquad
D\mathfrak F_p(P)=-3x(P)^3/y(P)\ne0.
\]
(22) 的每项含 \(Z\)，故
\[
G^{(1)}_p(P)=DG^{(1)}_p(P)=0,\qquad
D^2G^{(1)}_p(P)=-3x(P)^3/y(P).
\]
因此
\[
\boxed{
r^{(1)}_p=
-\frac{3x(P)^4}{2y(P)^2}Z^2+O(Z^3)
}
\tag{24}
\]
具有准确二阶零，显示系数为单位。

全局地，\(r^{(1)}_p\) 仅可能在 \(t=1\) 有极。
由 \(\mathfrak F_p\) 的上述极界、\(D\) 在二挠点为正规非零导子，
(22) 给二挠极阶至多 \(2p^2\)，所以可取
\[
\boxed{
N^{(1)}_p(t)=(1-t)^{p^2}r^{(1)}_p(t)\in k[t],
\quad \deg N^{(1)}_p\le p^2,\quad
B_p(-t)^2\mid N^{(1)}_p(t).
}
\tag{25}
\]
在 \(O\)，\(r^{(1)}_p(0)=-1\)，故相应商
\(Q_p=N^{(1)}_p/B_p(-t)^2\) 满足 \(Q_p(0)=-1\)。
(24) 还说明该商在每个 \(B_p(-t)\) 根处为单位。
这条双因子来自实际 first-lift forcing，不是对全来源自由作的加权乘法。

## 7. 保原点与全部真实测试点的模 \(p^2\) 有理代表

取 R346 的真实整反序多项式
\[
\mathscr B_p(\xi)=
\sum_{j=0}^{n_0}\binom{n_0}{j}
\frac{N}{N-3j}\xi^j,\qquad N=(3p-1)/2 .
\]
它约化为 \(B_p\)，且 \(\mathscr B_p(-t)=0\) 正是原
\(\mathscr R_p(x)=0\) 的非零测试分量。
其全部简单根形成 R346 已付的有限 étale 整代数。

选取 \(Q_p\) 的任一整系数提升 \(\widetilde Q_p\)，并准确指定
\(\widetilde Q_p(0)=-\eta_{\rm lin}\)；该值约化为 \(-1\)，所以兼容。
置
\[
\widetilde r^{(1)}_p(t)
=\frac{\mathscr B_p(-t)^2\widetilde Q_p(t)}{(1-t)^{p^2}},
\qquad
\boxed{
R_{\kappa,p}^{(2)}
=\widetilde r_\kappa+p\,\widetilde r^{(1)}_p,
}
\tag{26}
\]
其中
\(\widetilde r_\kappa=(x/y)\widetilde G_\kappa\)
是 R356 的完整特征零提升。

**定理3。** 在同一个原三块整目标中，
\[
\boxed{
R_{\kappa,p}^{(2)}
\equiv (x/y)\zeta_\kappa\pmod{p^2\Gamma_{T+1}}.
}
\tag{27}
\]
而且这个实际有理代表同时满足
\[
\boxed{R_{\kappa,p}^{(2)}(O)=-1}
\tag{28}
\]
以及在每个真实 lifted 测试点 \(\widetilde P\) 上
\[
\boxed{
R_{\kappa,p}^{(2)}(\widetilde P)=0,\qquad
D R_{\kappa,p}^{(2)}(\widetilde P)=-x(\widetilde P)^2/y(\widetilde P)
\in\mathcal O^\times .
}
\tag{29}
\]

**证明。** R356 的准确分解是
\[
(x/y)\zeta_\kappa
=\widetilde r_\kappa-p\eta_{\rm lin}
+p\mathcal A_\kappa.
\]
由 (23)、\(\eta_{\rm lin}\equiv1\pmod p\)，减去 (26) 后属于
\(p^2\mathcal O[[w]]+p w^s\mathcal O[[w]]\)。
原关系 \(w^s=p\epsilon\) 将第二项也送入 \(p^2\Gamma\)，
证明整个目标的 (27)，包括其全部高块。

在 \(O\)，
\(\widetilde r_\kappa(0)=c_{\rm lin}\)、
\(\widetilde r^{(1)}_p(0)=-\eta_{\rm lin}\)，
所以总值是 \(c_{\rm lin}-p\eta_{\rm lin}=-1\)，得到 (28)。

在真实测试点，\(\widetilde Z=0\)，故
\(\widetilde G_\kappa=0\)。
(26) 的第二项有真实 \(\mathscr B_p(-t)^2\) 因子，
其值和一阶导数都为零。
又 \(D\widetilde Z=1\) 在这些点准确成立，
R356 的特征零 defect 公式给
\(D\widetilde G_\kappa=-x\)。
因此得到 (29)。\(\square\)

不同允许的 \(\widetilde Q_p\) 使代表只改变 \(p^2\) 的原整目标项，
所以 (27) 及下一配对不依赖此提升选择。
这构造的是原有限目标所需的有理系数代表；
没有声称原 theta 在所有点等于它。

## 8. 真正第二提升的完整有理配对

沿 R351 取
\[
\bar P\in\ker\beta_1^{M_-},\qquad
\lambda_0\in C_2(M_+)^\vee,
\]
及其真正的模 \(p^2\) 左、右核提升 \(P_2,\lambda_2\)。
令 \(\mathcal D(P)\) 仍是 R338 的两条耦合尾。
把 (27) 代入 R356 的完整原 Gaussian 连接式，得到
\[
\mathcal Z\equiv
W_{\rm phys}R_{\kappa,p}^{(2)}
-\frac{(p+1)a_\kappa}{34}B\epsilon
\pmod{p^2}.
\tag{30}
\]
所以原 \(\mathcal A_\kappa\) 项现在已全部纳入一个指定有理代表，
不能在这一步重新删去 Gaussian 的 \(\epsilon\) 项。

R351 的 \(\lambda_2\mathcal ZM_-(\mathcal EP_2)=0\pmod{p^2}\)
以及 R338 的完整边界计算，准确给
\[
\boxed{
\overline{\frac1p
\langle\lambda_2,
 W_{\rm phys}R_{\kappa,p}^{(2)}M_-(\mathcal EP_2)\rangle}
=-\frac{(p+1)\bar a_\kappa}{34}\,
\lambda_0\!\left(\bar B\,\bar m_{13}\mathcal D(P)\right).
}
\tag{31}
\]
其整除性和两侧首次提升相容性来自同一个真实原矩阵，
未要求 \(\mathcal EP_2\) 保持核。
所有除幂对偶 \(p^{\lfloor r/s\rfloor}\)、目标末行和原首 Bockstein 像
仍按 R351 保留。

(29)、(31) 给出了可直接在 R346 有限 étale 测试代数中比较的
原二阶系数及其精确一阶 jet。
恢复公共 \(G_0,U_0\) 时，R351 的完整
\(-\mathsf E\log U_0\) 连接、\(P_{134}\) 和固定 \(Z^{-78}\) 行移仍在；
本篇没有把 \(U_0\) 在这些非原点处称为单位。
局部单位因子及坏分量需按 R359 分开支付。

原完整中央失败的实际输入仍只给
\(a_\kappa c_1-pc_2\equiv0\pmod{p^2}\) 聚合。
(15)、(16) 中的 Cartier 单位以及 (29) 的局部单位导数
均未被单独称为中央非零。
现在已完成的是原第一整商到真实二阶有理连接模型的完整运输。

本篇为全参数证明，无目标素数扫描。
依赖 R338、R342、R346、R351、R352、R356 的实际来源和窗口；
原整环境之外没有另加曲线或来源。
文件通过已授权 GitHub API 保存；核心同步记录由根代理维护。
