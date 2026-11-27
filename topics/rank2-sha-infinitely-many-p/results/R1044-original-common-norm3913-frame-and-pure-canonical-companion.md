# R1044 — 消去完整第二态的共同 norm3913 平面、两个 odd 全核与三条原中央行

日期：2026-11-27 UTC。**已证明。** 本篇在 R1040 的原六 sigma 张量内，将其真实两态的 $K,A$ 输出推至 $R=K+\omega A$。第二态 $\Xi _1$ 整个消失；第一态准确成为 $[\delta]^*(-xy\sigma^5)$。在这个真实输出内构造同时正交于原 $S34,T72,\Phi126$ 三观察的整行 $F$，范数为 $3913$。它与原 norm3 方向给出 degree5509 及 degree $3\cdot7\cdot13\cdot19\cdot43\cdot787$ 的两个 standard odd 全核，同一个固定 ray 上的绝对标量均为 $\beta=-\lambda$。

据此得到新的完整四输出 carry、一个固定六次测试、原五深网格上的真实 $T-S$ 差及只需 $H,J,N$ 三个角平均的完整 $\Phi126$ 行。原 $S/T$ 未平均的行和 $\Phi126$ 的平均行分别按其真实来源使用；所有不同单位域及补域保留。

## 1. 原两态中一个完整而非逐矩的消除

沿用 R1042(1) 的 $b=17,\lambda,\beta,\kappa,d,\rho,\Omega$，并用
R1040§10 的原整行：
$$
\begin{aligned}
Y&=(7,\pi,\bar\pi,3\delta,2\delta,2\delta),&
H&=(1,-1,-1,0,0,0),\\
K&=(-1,\omega,\omega^2,\delta,0,0),&
J&=(0,0,0,0,1,-1),\\
A&=(1,-\omega^2,-\omega,0,-\delta,-\delta),&
N&=(0,-2,2,2,-1,-1).
\end{aligned}
\tag{1}
$$
它们两两 Hermitian 正交，Gram 为 $(126,3,6,2,9,14)$，行列式
为 $756$。$Y=Y_A$，其余两条原观察 $Y_S,Y_T$ 仍是
R1042(2) 的完整整行。这里 $N$ 是一个行名，范数另写 $\mathrm N$。

R1040§12 已付：先作 $H,J,N$ 的实际主型投影及 $Y$ 的主型投影，
剩余 $Y,K,A$ 的整个来源是
$$
39\delta\,\Phi_{126,b}(Y)\Xi _0(k,a)+G_{126,b}(Y)\Xi _1(k,a),
\tag{2}
$$
另乘 $B_3(H)\Theta(J)\Theta_{14}(N)$。准确的两态为
$$
\begin{aligned}
\Xi _0(k,a)
={}&F_6^-(k)\Theta_9(a)
 +6b\,(y\sigma^6)(k)\bigl((X+4b)\sigma^9\bigr)(a),\\
\Xi _1(k,a)
={}&(xy\sigma^6)(k)(x^2\sigma^9)(a)
 -(x\sigma^6)(k)(x^2y\sigma^9)(a).
\end{aligned}
\tag{3}
$$
全部 theta frame、微分、$\Omega$ 与 R1040 相同。尤其不把
$G_{126,b}$ 的中央导数赋零。

令
$$
\boxed{
R=K+\omega A
=\delta(-\omega^2,-\omega^2,0,1,-\omega,-\omega),\qquad
\mathrm NR=15.}
\tag{4}
$$
末二个整系数为 $2+\omega$。$R/\delta$ 是原 standard odd 的
norm5 整行；这里的推前不需要任选一个新的 theta lift。

推前 $R$ 在 (3) 的 Amice 函数中准确是 $a=\omega k$。
由 $\sigma(\omega z)=\omega\sigma(z)$、
$x(\omega z)=\omega x(z)$、$y(\omega z)=y(z)$，两项
$\Xi _1$ 均取得相同的 $\omega^2$ 因子并相消，而
$$
\boxed{\begin{aligned}
\Xi _1(k,\omega k)&=0,\\
\Xi _0(k,\omega k)
&=-y\sigma^{15}(X+4b)(X-8b)
=[\delta]^*(-xy\sigma^5)=:\Theta_{15}.
\end{aligned}}
\tag{5}
$$
最后等式用原
$\sigma(\delta z)=\delta x\sigma^3$ 和完整 $[\delta]$ 加法公式；
其原点常数为一。没有额外的 $\omega$ 相位。

因此 (2) 的**整个**五输出推前为
$$
\boxed{
39\delta\,\nu_{\Phi_{126,b}}\otimes
\nu_{B_3}\otimes\nu_\Theta\otimes\nu_{\Theta_{14}}
\otimes\nu_{\Theta_{15}}
}
\tag{6}
$$
（输出次序为 $Y,H,J,N,R$）。(6) 包含先前的 $Y,H,J,N$ 主型投影；
没有声称未投影的原五输出也已是这个张量。对原单位 Mellin 测试，
$Y$ 权本来 $\mu _6$-不变，故测试端只需 $H,J,N$ 的三个平均。

## 2. 同时保留三个原观察的新整平面

定义
$$
\boxed{
F=\frac{(40-48\delta)R+(-93-15\delta)J+(33-25\delta)N}{4\delta}.
}
\tag{7}
$$
它准确为整行
$$
\boxed{
F=(22-2\omega,\ 40+9\omega,\ -18-11\omega,\
             -20-35\omega,\ -11-\omega,\ -19-32\omega).
}
\tag{8}
$$
逐项内积给
$$
F\perp H,\quad
F,H\perp Y_S,Y_T,Y_A,\qquad
\mathrm NF=3913=7\cdot13\cdot43.
\tag{9}
$$
这些等式可直接用 (1)、R1042(2)、(8) 核对；不以两个好位的
本征值代替整行正交。

置
$$
c=23-\delta=22-2\omega,\quad C=cH,\quad
r=\frac{559}{228}=\frac{\mathrm NF}{\mathrm NC},\quad
h=1+r=\frac{787}{228},
$$
$$
\boxed{D=F-C,\qquad E=F+rC.}
\tag{10}
$$
于是
$$
\mathrm Nc=532=4\cdot7\cdot19,\quad
\mathrm NC=1596=4\cdot3\cdot7\cdot19,\quad
C\perp F,\quad D\perp E,
$$
$$
\boxed{
\mathrm ND=5509=7\cdot787,\qquad
\mathrm N(114E)=3\cdot7\cdot13\cdot19\cdot43\cdot787.
}
\tag{11}
$$
两个实际整行是
$$
\boxed{
D=(0,\ 62+7\omega,\ 4-13\omega,\
          -20-35\omega,\ -11-\omega,\ -19-32\omega),
\quad
114E=114F+559(11-\omega)H.
}
\tag{12}
$$
$D$ 模二有五个非零系数；$114E$ 模二有三个。
$\mathcal O_K/2=\mathbf F_4$ 的每个非零系数都保原 sigma 奇半特征，
故两行的完整半特征均为 standard odd。$E$ 始终使用 (12) 的整覆盖，
不将其有理范数当成整数 theta degree。

固定原四输出幂等为
$$
\boxed{
\Pi=I-\frac{\bar C^{\,t}C}{1596}
       -\frac{\bar F^{\,t}F}{3913}.
}
\tag{13}
$$
它满足 $Y_i\Pi=Y_i$，$i=S,T,A$。后续所有 whole carry 均保整个
$\Pi$，不是只保三个第一边际。

## 3. 实际 ray 相容性及两个绝对 odd 锚

原 R531§2(13) 已给
$$
g_\pi=\pi_0/\bar\pi_0\equiv1\pmod{27\cdot7\cdot13},\qquad
g_\pi\equiv27+8\omega\pmod{64}.
\tag{14}
$$
原 R410(1)、(4) 的十九处类是
$\pi_0\equiv1\bmod19$，所以 $g_\pi\equiv1\bmod19$。
保 R1042 的三处提升、三十一处条件，以及原五、十七等处全部条件，
仅新增
$$
\boxed{\pi_0\equiv1\pmod{43\cdot787}.}
\tag{15}
$$
四十三、七百八十七均与所有上述旧模数互素，故 (15) 由 CRT
与原类相容，而且所得类处处为单位。它保持原
$\pi_0\bmod64$，没有把旧 $g_\pi\bmod4=3$ 改为一。
同一个 ray-class 素理想定理仍给无穷普通有理素数。

(14)、(15) 及原十九处条件，准确给两个 odd 全空间所需的
$$
g_\pi\equiv1\pmod{2\cdot5509},\qquad
g_\pi\equiv1\pmod{2\cdot3\cdot7\cdot13\cdot19\cdot43\cdot787}.
\tag{16}
$$
取
$$
\gamma_7=3+\omega,\quad \pi_{13}=4+\omega,\quad
\gamma_{19}=5+2\omega,\quad
\gamma_{43}=7+\omega,\quad\gamma_{787}=29+27\omega.
$$
由 $a^2-ab+b^2$ 逐项得其范数为下标。非零绝对锚是
$$
\boxed{
\sigma(\gamma_7\gamma_{787}z),\qquad
\sigma(\delta\gamma_7\pi_{13}\gamma_{19}
                 \gamma_{43}\gamma_{787}z).
}
\tag{17}
$$
它们的 degree 与 (11) 的两个实际整数 degree 完全相同，
且具有相同 standard odd 半特征。固定 CM pull 与普通深限制严格交换，
原 sigma 的核心为 $\beta=-\lambda$。完整 Heisenberg 模的 scalar
交织与 (17) 因而付清两条轴的**绝对**标量 $\beta$。

于是对 $L=D,E$、$n\ge0$，
$$
\boxed{
\rho|_{L\in p^n\mathcal O}
=\beta^n(P_{L,\kappa^n})_*\rho,\qquad
P_{L,t}=I+(t-1)\frac{\bar L^{\,t}L}{\mathrm NL}.
}
\tag{18}
$$
它保正交的全部其余五输出，特别保 (13)。
下文取原好位 $p>211$ 并排除固定 $787$；
需要第六节的统一单位首项时另排 $1153$。
其它新固定分母仅含 $2,3,7,13,19,43,103$。
事实上 $787,1153$ 都不在旧 $p\equiv7\bmod64$ 类中；
将其明确列出使结论也能逐项核对，不以这一观察隐藏分母。

## 4. 固定六次测试及完整共同 carry

原 norm3 偶纤维为
$$
B_3=-y\sigma^3=1+\frac{3b}{10}z^6+\cdots .
$$
因此在保其余五输出的意义下，$C=cH$ 的准确低矩为
$$
(\operatorname{forget}C)_*(C^6\rho)
=216c^6b\Omega^6(\operatorname{forget}C)_*\rho,\qquad
(\operatorname{forget}C)_*(C^2\rho)=0.
\tag{19}
$$
定义固定特征零数
$$
a=\frac1{216c^6},\qquad
b_Q=\frac{3a}{r^3(2-r)},\qquad
Q(C,F)=aC^6+b_QC^2F^4.
\tag{20}
$$
$b_Q$ 不含素数 $p$；这里以 $b_Q$ 区别曲线参数 $b=17$。
由 (19)，
$$
\boxed{\Pi_*\left(\frac{Q}{b\Omega^6}\rho\right)=\Pi_*\rho.}
\tag{21}
$$

用 $C=(E-D)/h,\ F=(E+rD)/h$ 写
$$
Q=h^{-6}\sum_{k=0}^6q_kD^kE^{6-k},
$$
$$
\boxed{
q_k=a(-1)^k\binom6k+
 b_Q\sum_{j=0}^2(-1)^j\binom2j\binom4{k-j}r^{k-j};
}
\tag{22}
$$
超出范围的二项式为零。此式完整指定全部七个系数。尤其
$$
\boxed{
q_5=0,\qquad
q_4=\frac{6a(2r-3)(1+r)}{r(r-2)}
=\frac{6a\cdot434\cdot787}{559\cdot103},\qquad
\frac{q_6}{q_4}=-\frac{559}{1302}.
}
\tag{23}
$$
第五项来自 $-6a+2r^3(2-r)b_Q=0$，是原特征零全式相消。

对 $n\ge1$ 取真实单位域
$$
\Gamma_n=\{D\in p^n\mathcal O,\ E\text{ 为单位}\}
=\{C,F\text{ 为单位},\ F-C\in p^n\mathcal O\}.
\tag{24}
$$
在其上定义
$$
\boxed{
q_{n,p}^{\,\mathrm{new}}
=\frac1{h^6b\Omega^6}
 \sum_{k=0}^6
 \frac{q_k(D/\kappa^n)^kE^{6-k}}
      {1+\lambda\kappa^{6-k}},
}
\tag{25}
$$
域外为零。所有分母由 R410 的原单位结论支付。先用 (18) 的
$D$ 深核，再逐次数用 $E$ 单位核，最后用 (21)，得到
$$
\boxed{
\Pi_*\bigl({\bf1}_{\Gamma_n}q_{n,p}^{\,\mathrm{new}}\rho\bigr)
=\beta^n\Pi_*\rho.
}
\tag{26}
$$
真实 $D$ 缩放在 $(C,F)$ 中为
$$
\binom{C'}{F'}=\frac1h
\begin{pmatrix}r+t&1-t\\r(1-t)&1+rt\end{pmatrix}
\binom CF,\qquad t=\kappa^n.
\tag{27}
$$
它固定 $E,Y_S,Y_T,Y_A$ 和整个 $\Pi$。因而 (26) 保任意真正
四输出 mixed 测试，其单位 cut 随显示矩阵一起处理。

特别，$a_S=a_T=\gamma,\ a_A=7$ 时，
$$
\boxed{\begin{aligned}
\int_{\Gamma_n,Y_S\ {\rm unit}}
 \langle Y_S/a_S\rangle^{dv}q_{n,p}^{\,\mathrm{new}}d\rho
 &=\beta^n\langle\gamma\rangle^{-dv}J_S(v),\\
\int_{\Gamma_n,Y_T\ {\rm unit}}
 \langle Y_T/a_T\rangle^{dv}q_{n,p}^{\,\mathrm{new}}d\rho
 &=6\delta\beta^n\langle\gamma\rangle^{-dv}J_T(v),\\
\int_{\Gamma_n,Y_A\ {\rm unit}}
 \langle Y_A/a_A\rangle^{dv}q_{n,p}^{\,\mathrm{new}}d\rho
 &=39\delta\beta^n\langle7\rangle^{-dv}J_{126,b}(v).
\end{aligned}}
\tag{28}
$$
原三来源质量均为零，所以这些固定尺度不增加首导数的质量项。
三条坏 canonical 假设因而给同一个**未平均**新测试上的三条完整零行。

## 5. 去掉 G 后的真实三角平均及全部单位域

记 (7) 的三个系数为 $a_R,a_J,a_N$。对任何连续有界
$h_0(C,F)$，定义原物理测试
$$
\boxed{
\mathcal B h_0
=\frac1{6^3}\sum_{\zeta_H,\zeta_J,\zeta_N\in\mu _6}
h_0\bigl(\zeta_H C,\
 a_RR+a_J\zeta_JJ+a_N\zeta_NN\bigr).
}
\tag{29}
$$
它是原 Hermitian 投影矩阵
$I+(\zeta-1)\bar L^{\,t}L/\mathrm NL$，
$L=H,J,N$，的真实转置。分母仅 $2,3,7$，没有舍弃隐藏输出。
(6) 准确给
$$
\boxed{
\int_{Y\ {\rm unit}}\langle Y\rangle^{dv}\mathcal Bh_0\,d\rho
=39\delta\,J_{126,b}(v)\,\Lambda_p(h_0),
}
\tag{30}
$$
其中整个伴随积分为
$$
\Lambda_p(h_0)=
\int h_0\bigl(cu_H,a_Ru_R+a_Ju_J+a_Nu_N\bigr)\,
d\nu_{B_3}(u_H)d\nu_{\Theta_{15}}(u_R)
d\nu_\Theta(u_J)d\nu_{\Theta_{14}}(u_N).
\tag{31}
$$
这是完整有界测度身份，不是只取消 $G$ 的某个矩。
若 $h_0$ 含单位域或 carry，(29)、(31) 均保原指示函数。
例如对 (25)，每支必须使用
$$
D_\zeta=a_RR+a_J\zeta_JJ+a_N\zeta_NN-\zeta_HC,\quad
E_\zeta=a_RR+a_J\zeta_JJ+a_N\zeta_NN+r\zeta_HC
\tag{32}
$$
以及 $\{D_\zeta\in p^n,E_\zeta\ {\rm unit}\}$。

在坏 $\Phi126$ 假设下，(30) 的首导数为零，
不再残留 $j_G/J_G(0)$。但是 (29) 不固定 $Y_S,Y_T$；
(28) 不能据此逐支改成 $S/T$ 的平均零行。
另一方面 (26) 本来保整个四输出，仍可用于任意已给出的
$Y_S/Y_T/Y_A$ mixed 条件。这两种实际许可分别保留。

## 6. 原五深网格中的新准确单位差

保持原输入网格
$$
\mathcal D_n=\{\xi_1=x\ {\rm unit},\
                   \xi_2,\ldots,\xi_6\in p^n\mathcal O\}.
\tag{33}
$$
由 (12)，$D$ 首坐标为零，$C,F\equiv cx$，
$E\equiv hcx$，所以它整个包含于 (24)，三条观察也都是单位。

记五深输入的 $D$ 系数为
$$
(d_2,\ldots,d_6)
=(62+7\omega,\ 4-13\omega,\ -20-35\omega,\
                  -11-\omega,\ -19-32\omega),\quad P=\prod_{j=2}^6d_j.
\tag{34}
$$
其范数依次为
$$
3\cdot1153,\quad3\cdot79,\quad25\cdot37,\quad
3\cdot37,\quad3\cdot7\cdot37.
\tag{35}
$$
设 $T$ 为五深输入的共同真实缩放，$e_0=hc$。
将 $Y_i=a_ix+TZ_i$、$E=e_0x+TE_f$ 和 (25) 整体代入，
定义完整 $\mathcal A_i(T)$，定义方法与 R1042(28) 完全相同，
但使用本篇 (22)、(34) 及本篇实际 $E$。
五个 sigma 深核准确给
$$
\int_{\mathcal D_n}d\log\langle Y_i/a_i\rangle\,
 q_{n,p}^{\,\mathrm{new}}d\rho
=\beta^{5n}\mathcal A_i(\kappa^n).
\tag{36}
$$
$q_5=0$ 和五输入角型给 $\mathcal A_i(0)=0$，
包括整个质量与常数 logarithm。

这里只需两个具有相同自由系数 $\gamma$ 的实际 $S/T$ 行。
由于它们仅末两输入不同，
$$
\begin{aligned}
\sum_{j=2}^6\frac{(Z_T-Z_S)_j}{\gamma d_j}
&=\frac1\gamma\left(\frac{3\delta-1}{d_5}+\frac2{d_6}\right)
=-\frac{12}{\gamma d_6},\\
[\xi_2\cdots\xi_6]D_f^4(Z_T/\gamma-Z_S/\gamma)
&=-\frac{288P}{\gamma d_6}.
\end{aligned}
\tag{37}
$$
第一式可由
$(3\delta-1)d_6+2d_5=-12d_5$ 直接逐系数核验。
原 $-1/84$、$q_4$、全部阶乘和自由第一单位矩均给
$$
\boxed{
[T](\mathcal A_T-\mathcal A_S)=
\frac db\frac{1+\lambda\kappa}{1+\lambda\kappa^2}
\cdot
\frac{24q_4e_0^2P}{7h^6\gamma d_6}.
}
\tag{38}
$$
两行的整条 $\log\langle x\rangle$ 质量项严格相消；
这里没有忽略它们。

由 (23)、(35)，(38) 在所列好位是单位。
整个 logarithm 尾仍满足
$v_p([T^j](\mathcal A_T-\mathcal A_S))
\ge-\lfloor\log_pj\rfloor$。
所以对每个 $n\ge1$，
$$
\boxed{
v_p\left(
\int_{\mathcal D_n}d\log\langle Y_T/Y_S\rangle\,
q_{n,p}^{\,\mathrm{new}}d\rho\right)=n.
}
\tag{39}
$$
(39) 是新平面内、同一实际网格和同一有限逆测试的结论；
没有重算旧 F81 的数值，也没有把它等同完整中央。

## 7. 当前可继续消费的两个全式

令 $L_i={\bf1}_{Y_i\ {\rm unit}}d\log\langle Y_i/a_i\rangle$，
$h_n={\bf1}_{\Gamma_n}q_{n,p}^{\,\mathrm{new}}$。
若三条原 canonical 首导数同时为零，本篇支付
$$
\boxed{\begin{aligned}
\int L_i h_n\,d\rho&=0\qquad(i=S,T,A),\\
\int L_A\,\mathcal B h_n\,d\rho&=0.
\end{aligned}}
\tag{40}
$$
第二式的来源现在是 (6) 的纯 $\Phi126$，没有未知第二态；
第一组三式仍使用 (26) 的原完整共同平面。

任意进一步分域必须保
$$
\boxed{
0=\int_{\mathcal D_n}(L_T-L_S)h_n\,d\rho+
   \int_{\Gamma_n\setminus\mathcal D_n}
             (L_T-L_S)q_{n,p}^{\,\mathrm{new}}d\rho,
}
\tag{41}
$$
以及 (32) 全部旋转域。R1042§9 已证明旧 F81 的一个真实两单位补管
有非零常数项，因此没有依据把这类补域统称为更深误差。
本篇给的是可在完整补域继续联立的原来源、绝对核和测试；
未证明 (41) 的第二项与 (40) 不相容，故不将其写成无穷素数结论。

### 依赖与执行

- R1040§§10、12：原整框架、实际两态及全部相位。
- R1042§§1–4：同一三个原算术来源、ordinary homothety、完整测试规范。
- R531§2、R410§§1–3：实际旧 ray 的 $7/13/19$ 条件、绝对全核和单位。
- R1038：固定 E3969 的 rank、全有限来源、平方和通常全 Sha 桥。

全文是显示的固定代数、原 theta／测度身份和完整尾估计。
没有新增数学执行、有限素数扫描或新的有限谱缓存。
