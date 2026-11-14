# R362：原三输入双辅助、整个共同 core 与真实六分支叶域

日期：2026-11-13。**状态：已证明。** 在原六个 sigma 输入的第
$1,2,3$ 个中，构造两个真实辅助坐标；它们和部分输出
$Y_{123}$ 组成行列式为 $-8\omega^2/3$ 的整可逆变换。
原 degree 八、$\mu_6$ 型三空间只有一维，故这一次得到完整的
**部分输出与两个辅助**的联合身份。其辅助测度严格等于 R350–R358
原相交三元组的 $\Xi_\Delta$。因此 $\Xi_\Delta$ 的整个共同
$p^2$-core 得到准确标量，六个相位的双非单位边界全部返回同一原测度。
同时给出原叶域必须保留的部分输出条件、六个相位分支及它们的实际
平移小球公式。这些等式没有把单个叶域的中央零免费从总中央零传下来。

## 1. 原规范及结论

沿用 R350、R357、R358：
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
\gamma=3+\omega,
$$
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\sigma=z+\cdots,\quad \Theta=x\sigma^2,\quad C=y\sigma^3 .
\tag{1}
$$
原目标仍是
$$
\boldsymbol c=(1,2,\delta,2\delta,\gamma,\bar\gamma)^t,\qquad
S=-\frac1{84}\prod_{i=1}^6\sigma(c_i z).
\tag{2}
$$
对普通 $p>7$，用同一原 $E_{17}$ 周期 $\Omega$ 与原 sigma 测度
$\nu$，使
$$
\int e^{zx/\Omega}\,d\nu(x)=\sigma(z).
$$
记
$$
\pi=\psi_{17}(\mathfrak p),\quad \pi\bar\pi=p,\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p)\in\mu_6,
$$
$$
\kappa=p/\bar\pi^2,\qquad
\lambda_\sigma=\varepsilon^3/\bar\pi,\qquad
t_p=\lambda_\sigma\kappa .
\tag{3}
$$
因此 $v_p(\kappa)=v_p(t_p)=1$，且原完整 core 为
$\nu|_{p\mathbf Z_p}=\lambda_\sigma[\kappa]_*\nu$。

R358 已付
$$
D=\Theta^2,\qquad K=\Theta\Theta_\delta,\qquad
\lambda_D=\frac{\varepsilon(-1/p)}{\bar\pi},\qquad
\lambda_K=\frac{\varepsilon(-2/p)}{\bar\pi},
\tag{4}
$$
$$
\nu_D|_p=\lambda_D[\kappa]_*\nu_D,\qquad
\nu_K|_p=\lambda_K[\kappa]_*\nu_K,\qquad
1-\lambda_D,\ 1-\lambda_K\in\mathcal O^\times .
\tag{5}
$$
这里以及下文的限制都是实际测度限制；$\nu_D,\nu_K$ 的质量均为一。

令原第 $1,2,3$ 个输入为 $(X_1,X_2,X_3)$。本篇的新坐标为
$$
Y_A=X_1+2X_2+\delta X_3,
$$
$$
L=\frac{X_1+\omega X_2+X_3}{\delta},\qquad
M=\frac{\omega^2X_1+\omega X_2-\omega^2X_3}{\delta}.
\tag{6}
$$
设 $\mathsf P_\Delta$ 表示只把两个辅助同时作 $\mu_6$ 平均，
部分输出 $Y_A$ 保持不变。则完整原联合式为
$$
\boxed{
\mathsf P_\Delta(Y_A,L,M)_*\nu^{\otimes3}
   =\nu_A\otimes\Xi_\Delta,\qquad
A(z)=\sigma(z)\sigma(2z)\sigma(\delta z)
     =-2\delta\sigma^8xy .
}
\tag{7}
$$
这里的 $\Xi_\Delta$ **正是** R350 的原双辅助测度，而不是重新选取
一个具有相同少数矩的替代测度。并且
$$
\boxed{
\Xi_\Delta|_{(p\mathbf Z_p)^2}
   =\lambda_\Xi[\kappa,\kappa]_*\Xi_\Delta,\qquad
\lambda_\Xi=\lambda_K\lambda_D
   =\frac{\varepsilon^2(2/p)}{\bar\pi^2},
}
\tag{8}
$$
$$
\boxed{
\nu_A|_{p\mathbf Z_p}
   =\lambda_A[\kappa]_*\nu_A,\qquad
\lambda_A=\frac{\varepsilon(2/p)}{\bar\pi}.
}
\tag{9}
$$
下文证明全部身份及其真正可作用的域。

## 2. 真实格、Gram 矩阵与部分输出

在三个输入中取
$$
r=(1,\omega^2,1)^t,\qquad s'=(\omega,\omega^2,-\omega)^t,\qquad
c_A=(1,2,\delta)^t .
$$
直接计算得
$$
c_A^tr=c_A^ts'=0,\qquad
r^*r=s'^*s'=3,\qquad r^*s'=1,\qquad c_A^*c_A=8 .
\tag{10}
$$
坐标矩阵的行是 $c_A^t,r^*/\delta,s'^*/\delta$，其行列式为
$$
\boxed{\det=-8\omega^2/3.}
\tag{11}
$$
因此对每个 $p>7$ 都是原 $\mathcal O_{\mathfrak p}$ 上的整可逆变换，
而且
$$
\boxed{
\begin{pmatrix}X_1\\X_2\\X_3\end{pmatrix}
=\frac{\bar c_A}{8}Y_A+
 \frac{\delta}{8}\bigl((3r-s')L+(3s'-r)M\bigr).
}
\tag{12}
$$
特别是
$$
(X_1,X_2,X_3)\in(p^n\mathbf Z_p)^3
\quad\Longleftrightarrow\quad
(Y_A,L,M)\in(p^n\mathbf Z_p)^3 .
\tag{13}
$$
这些是真正的三个坐标；没有把部分输出条件当成辅助条件。

令
$$
F_A(z;v,w)=
\prod_{j=1}^3
 \sigma\left(c_{A,j}z+\frac{\bar r_jv+\bar s'_jw}{\delta}\right).
\tag{14}
$$
(10) 使 $z$ 和辅助的交叉 Gaussian 准确消失，所以作为 $z$ 的函数，
它是同一原 $\mathcal O(8O)$ 的截面。sigma 的原 $\mu_6$ 协变给
$$
F_A(\zeta z;\zeta v,\zeta w)=\zeta^3F_A(z;v,w).
\tag{15}
$$
对辅助同时平均以后，$z$ 的型准确为三。
$\sigma^8L(8O)$ 中此型只有
$\sigma^8xy$ 一条线：在标准单项式 $x^j,x^jy$ 中分别检验极阶
及 $\mu_6$ 型即可；唯一允许的奇项是 $xy$。
又 $A=-2\delta\sigma^8xy=2\delta z^3+\cdots$，故
$$
\mathsf P_\Delta F_A(z;v,w)=A(z)\psi_A(v,w),\qquad
\psi_A(v,w)=\frac{[z^3]F_A(z;v,w)}{2\delta}.
\tag{16}
$$
$\psi_A(0,0)=1$，且 (15) 已使该系数本身同时 $\mu_6$ 不变。
它是实际有界测度
$$
\boxed{
\Xi_A=\frac1{12\delta\Omega^3}(L,M)_*
                          (Y_A^3\,\nu^{\otimes3})
}
\tag{17}
$$
的变换。因而 (16) 是全测度身份；不用从形式截面猜其测度存在性。

## 3. 两条完整 CM 截线唯一识别原辅助

本节证明 $\Xi_A=\Xi_\Delta$。需要识别的是整个函数，而不只是有限矩。

令
$$
H_A(t,u)=\psi_A\bigl(\delta(t+u),\delta(t-u)\bigr).
\tag{18}
$$
辅助系数向量 $\bar r+\bar s'$、$\bar r-\bar s'$ 分别有范数八、四，
彼此正交。所以 $H_A$ 是原
$\mathcal O(8O)\boxtimes\mathcal O(4O)$ 的截面，并同时 $\mu_6$ 不变。
其实际六维空间的基为
$$
\begin{gathered}
\Theta^4(t)\Theta^2(u),\quad
[\sigma^6\Theta](t)\Theta^2(u),\quad
[\sigma^8y](t)[\sigma^4y](u),\\
[\sigma^4\Theta^2](t)[\sigma^2\Theta](u),\quad
[\sigma^2\Theta^3](t)\sigma^4(u),\quad
\sigma^8(t)\sigma^4(u).
\end{gathered}
\tag{19}
$$

对 $\zeta\in\mu_6$ 考虑 $\psi_A(\delta t,-\zeta\delta t)$。
它的实际 degree 为 $6-\zeta-\bar\zeta$，型为零，原点质量一。
degree 四、五、七的型零空间各只有一维。因此
$$
\begin{array}{c|c}
\zeta&\psi_A(\delta t,-\zeta\delta t)\\ \hline
1&\Theta^2(t)\\
-\omega,-\omega^2&-\Theta(t)C(t)\\
\omega,\omega^2&-\Theta(t)^2C(t).
\end{array}
\tag{20}
$$
degree 八的 $\zeta=-1$ 此时尚未预先指定。

由 $1+\delta=-2\omega^2$ 及上述实际相位，得到
$$
H_A(t,\delta t)=H_A(t,-\delta t)=-\Theta(2t)C(2t),
$$
$$
H_A(\delta t,t)=H_A(\delta t,-t)=-\Theta(2t)^2C(2t).
\tag{21}
$$
(19) 中只有第三列对 $u$ 为奇；(21) 准确杀掉该列。
其余写成
$$
\begin{aligned}
H_A={}&(\Theta^4+\alpha b\sigma^6\Theta)(t)\Theta^2(u)\\
&+ab[\sigma^4\Theta^2](t)[\sigma^2\Theta](u)
 +db[\sigma^2\Theta^3](t)\sigma^4(u)
 +eb^2\sigma^8(t)\sigma^4(u).
\end{aligned}
\tag{22}
$$
第一系数一来自原质量。设 $X=x(t)^3$。
只用原除法身份
$$
\sigma_\delta=\delta x\sigma^3,\quad
\Theta_\delta=\sigma^6(X+4b),\quad
\Theta_2=\sigma^8x(X-8b),\quad
C_2=-\sigma^{12}(X^2+20bX-8b^2).
\tag{23}
$$
把第一条 (21) 代入 (22) 并除去共同亚纯因子，给
$$
\begin{aligned}
&(X+\alpha b)(X+4b)^2-3abX(X+4b)+9dbX^2+9eb^2X\\
&\hspace{15mm}=(X-8b)(X^2+20bX-8b^2).
\end{aligned}
\tag{24}
$$
常数项给 $\alpha=4$，其余给 $a=3d,e=4d-24$。
第二条 (21) 再给
$$
\begin{aligned}
&(X+4b)^4-108bX^2(X+4b)+9abX(X+4b)^2\\
&\qquad-3db(X+4b)^3+81eb^2X^2\\
&\hspace{15mm}=(X-8b)^2(X^2+20bX-8b^2).
\end{aligned}
\tag{25}
$$
比较 $bX^3$ 得 $-92+24d=4$。
所以 $\alpha=4,a=12,d=4,e=-8$，全函数恰为 R357 的
$$
\boxed{
\begin{aligned}
H_A(t,u)={}&K(t)D(u)
 +12bF(t)G(u)+4bB(t)T(u)-8b^2E(t)T(u),\\
F={}&\sigma^4\Theta^2,\quad G=\sigma^2\Theta,\quad
B=\sigma^2\Theta^3,\quad T=\sigma^4,\quad E=\sigma^8 .
\end{aligned}}
\tag{26}
$$
故 $\psi_A=\psi_\Delta$、$\Xi_A=\Xi_\Delta$。也同时支付了
先前未指定的 degree 八截线 $K$。这证明 (7)。

## 4. 整个二维 core；三输入与五输入 primitive 的准确差

将 (7) 限制到 $Y_A,L,M$ 全部在 $p\mathbf Z_p$。
由 (13)，这正是原三个输入全部深一层。
原 sigma core、坐标线性以及同时平均全部交换，故
$$
(\nu_A|_p)\otimes(\Xi_\Delta|_{p^2})
=\lambda_\sigma^3[\kappa]_*\nu_A
                    \otimes[\kappa,\kappa]_*\Xi_\Delta.
\tag{27}
$$
右端非零。秩一张量唯一性给两个非零标量
$\lambda_A\lambda_\Xi=\lambda_\sigma^3$，分别是两因子的 core 标量。
此处可直接对第二因子取总质量以固定标量；没有项目不确定性。

令
$$
P=\delta(L+M),\qquad Q=\delta(L-M).
\tag{28}
$$
该变换的行列式为六，故 $(L,M)\in p^2$ 当且仅当 $(P,Q)\in p^2$。
(26) 的后三项各在至少一个变量中有非平凡 $\mu_6$ 型，
在原点深球上的质量准确为零。于是
$$
\Xi_\Delta((p\mathbf Z_p)^2)
=\nu_K(p\mathbf Z_p)\nu_D(p\mathbf Z_p)
=\lambda_K\lambda_D.
\tag{29}
$$
结合质量 $\Xi_\Delta(1)=1$，便得 (8)、(9)，包括全部绝对相位。
一般深度为
$$
\boxed{
\Xi_\Delta|_{(p^a\mathbf Z_p)^2}
 =\lambda_\Xi^a[\kappa^a,\kappa^a]_*\Xi_\Delta,\qquad
\nu_A|_{p^a\mathbf Z_p}
 =\lambda_A^a[\kappa^a]_*\nu_A .
}
\tag{30}
$$
两标量均为单位。$\nu_A$ 虽质量为零，三阶原矩为
$12\delta\Omega^3$，是单位；(27)–(29) 没有除去一个未知或可能零的质量。

由 (17)，去掉原三输入全部在 $p$ 的部分后，定义实际
$\Xi_3^{\rm prim}$。原三个输入和三次权同时缩放，给
$$
\Xi_\Delta=\Xi_3^{\rm prim}
               +t_p^3[\kappa,\kappa]_*\Xi_\Delta.
\tag{31}
$$
R350 原五输入五次权同样给
$$
\Xi_\Delta=\Xi_5^{\rm prim}
               +t_p^5[\kappa,\kappa]_*\Xi_\Delta.
\tag{32}
$$
因此是真正两种原核之间的全输出身份
$$
\boxed{
\Xi_3^{\rm prim}-\Xi_5^{\rm prim}
=(t_p^5-t_p^3)[\kappa,\kappa]_*\Xi_\Delta.
}
\tag{33}
$$
各自的几何级数在有界测度范数下收敛：
$$
\Xi_\Delta=\sum_{n\ge0}t_p^{jn}
 [\kappa^n,\kappa^n]_*\Xi_j^{\rm prim},\qquad j=3,5.
\tag{34}
$$
截去 $n>M$ 的尾赋值至少 $j(M+1)$，在原整归一后成立。
所有输出域均保留，特别是 primitive 输入可以输出两个非单位。
准确的这部分为
$$
\boxed{
\Xi_j^{\rm prim}|_{p^2}
 =(\lambda_\Xi-t_p^j)[\kappa,\kappa]_*\Xi_\Delta,\qquad j=3,5.
}
\tag{35}
$$
系数均为单位。这不与 (34) 的收缩相矛盾：
(34) 收缩的是原全部输入深一层的加权项，
(30) 则是实际输出两个坐标同时深一层。

## 5. 六个碰撞相位的完整补项及全部权

沿用 R350 的六条实际一维来源
$$
D_\zeta=
\begin{cases}
\Theta^2,&\zeta=1,\\
\Theta\Theta_\delta,&\zeta=-1,\\
-\Theta^2C,&\zeta=\omega,\omega^2,\\
-\Theta C,&\zeta=-\omega,-\omega^2.
\end{cases}
\tag{36}
$$
它们是 $\delta(L-\zeta M)$ 的原推前，质量一。
记 $d_{\zeta,N}=\nu_{D_\zeta}(p^N\mathbf Z_p)$，$d_{\zeta,0}=1$。
对 $N\ge a$，有
$$
\boxed{
e_{\zeta;a,N}:=
\Xi_\Delta\{L,M\in p^a,\ L-\zeta M\in p^N\}
=\lambda_\Xi^a d_{\zeta,N-a}.
}
\tag{37}
$$
证明就是 (30)，并使用 $\kappa^a/p^a=\bar\pi^{-2a}$ 是单位；
这里仅取深球质量，所以 $\delta$ 和该单位不改变条件。
尤其对于真正双方 unit 的碰撞管
$$
\mathcal H_{\zeta,N}
=\{L,M\in\mathbf Z_p^\times,\ L-\zeta M\in p^N\},\quad N\ge1,
$$
$$
\boxed{
q_{\zeta,N}=\Xi_\Delta(\mathcal H_{\zeta,N})
=d_{\zeta,N}-\lambda_\Xi d_{\zeta,N-1}.
}
\tag{38}
$$
其三个输入或五个输入 primitive 补项也全部明确：
$$
e^{\rm prim,j}_{\zeta;a,N}
=(\lambda_\Xi-t_p^j)\lambda_\Xi^{a-1}
                                    d_{\zeta,N-a},\qquad a\ge1 .
\tag{39}
$$
没有剩下未知的二维双非单位项。对于 $\zeta=1,-1$，
(38) 回到已付的单位
$$
q_{1,N}=(1-\lambda_K)\lambda_D^N,\qquad
q_{-1,N}=(1-\lambda_D)\lambda_K^N .
\tag{40}
$$
(37)–(39) 对另四相位仍保其实际一维来源；
本篇不未经计算把它们的质量换成别的参考。

以上质量式来自更强的测度等式 (30)、(35)。例如任意有界
$f(L,M)$ 的共同深层积分准确为
$$
\int_{(p^a)^2}f(L,M)\,d\Xi_\Delta
=\lambda_\Xi^a\int f(\kappa^aL,\kappa^aM)\,d\Xi_\Delta.
\tag{41}
$$
所以全部 tame、主单位权与其导数都保留。
若把部分输出的第 $a$ 个环带除以 $p^a$ 归一，令 $d=p-1$，则
$$
\mathcal M_{A,\ell}^{[a]}(u)
=\lambda_A^a\omega_p(\bar\pi)^{-2a\ell}
 \langle\bar\pi\rangle^{-2adu}\mathcal M_{A,\ell}(u).
\tag{42}
$$
其中央导数含原
$-2ad\log_p(\bar\pi)\mathcal M_{A,\ell}(0)$。
若改用未乘 $\delta$ 的差坐标，另保
$\omega_p(\delta)^{-\ell}\langle\delta\rangle^{-du}$；
不能只保 (37) 的赋值后删除这些单位和质量项。

## 6. 与原相交三元组的同一共同限制运输

R350 的原辅助是
$$
L_r=\frac{X_1+\omega X_2+X_3}{\delta},\qquad
L_s=\frac{X_1-\omega X_4-\omega^2X_5}{\delta}.
$$
设 $Y_5=\sum_{i=1}^5c_iX_i$，
$S_5=-\prod_{i=1}^5\sigma(c_i z)/84$。
R350 全函数身份中的第六因子始终为 $\sigma(\bar\gamma z)$，
可在整个函数整环中准确消去，得到
$$
\mathsf P_\Delta(Y_5,L_r,L_s)_*
                   \left(-\nu^{\otimes5}/84\right)
=\nu_{S_5}\otimes\Xi_\Delta .
\tag{43}
$$
两边的剩余测度已由原五个输入具体定义；这不是把 Mellin 变换相除。

另一方面，(7) 乘上不受限制的第四、第五输入，给
$$
\mathsf P_\Delta(Y_5,L,M)_*
                   \left(-\nu^{\otimes5}/84\right)
=\nu_{S_5}\otimes\Xi_\Delta .
\tag{44}
$$
故可以在 (43)、(44) 上同时施加任意共同的
$(Y_5,X_6)$ 条件，并保任意辅助同时 $\mu_6$ 不变测试。
更具体，设 $g(Y_5,X_6)$ 有界、$h(L,M)$ 同时不变，则
$$
\boxed{
\begin{aligned}
Y_*\bigl(g(Y_5,X_6)h(L_r,L_s)\,\eta_6\bigr)
&=Y_*\bigl(g(Y_5,X_6)h(L,M)\,\eta_6\bigr)\\
&=\Xi_\Delta(h)\,
 (Y_5+\bar\gamma X_6)_*
                \bigl(g\,\nu_{S_5}\otimes\nu\bigr),
\end{aligned}}
\tag{45}
$$
其中 $\eta_6=-\nu^{\otimes6}/84$，$Y=\boldsymbol c^t\boldsymbol X$。
更一般允许 $h$ 随 $(Y_5,X_6)$ 变化，只须对每个固定共同坐标仍同时不变。
这些等式可直接加原输出 unit 条件和完整中央核。

(7) 自身还容许在第四、第五、第六输入上施加各自条件；
但此时部分输出卷积变为对应的受限卷积。
(45) 没有声称原混合辅助也容许独立限制第四、第五输入，
因为 $L_s$ 实际使用它们。这里明确保留两种身份的共同域。

## 7. 原叶域准确落在第二相位，但仍含部分输出条件

对 $N\ge1$，原三输入叶域
$$
\mathcal D_N=\{X_1\in\mathbf Z_p^\times,\ X_2,X_3\in p^N\}
$$
满足精确等价
$$
\boxed{
\mathcal D_N
=\{L,M\in\mathbf Z_p^\times,\ 
        L-\omega M\in p^N,\ Y_A-\delta L\in p^N\}.
}
\tag{46}
$$
事实上
$$
\delta(L-\omega M)=\delta X_2+2X_3,\qquad
Y_A-\delta L=(2-\omega)X_2+2\omega X_3;
\tag{47}
$$
这两行对 $(X_2,X_3)$ 的行列式是 $-8$。
所以 (46) 付到了原坐标；这里的碰撞相位确为 $\omega$，
与原混合三元组中同一叶域的相位一不同。

(46) 的最后一条条件，在固定 $Y_A$ 时对
$(L,M)\mapsto(\xi L,\xi M)$ 不变性不成立。
因此 (7) **不能**单独用于这一个叶域。
真实可用的是六个分支
$$
\mathcal D_{\xi,N}=
\{L,M\in\mathbf Z_p^\times,\ L-\omega M\in p^N,\
                         Y_A-\xi\delta L\in p^N\},
\quad \xi\in\mu_6.
\tag{48}
$$
它们在这里两两不交，且其并在辅助同时平均下不变。
只有 $\xi=1$ 是原 $\mathcal D_N$。

固定 $Y_A=y\in\mathbf Z_p^\times$，
(12) 将每个分支准确写成原三个输入中的一个模 $p^N$ 线管：
$$
\boxed{
\boldsymbol X\equiv yv_\xi\pmod{p^N},\qquad
v_\xi=\xi^{-1}e_1+(1-\xi^{-1})\bar c_A/8.
}
\tag{49}
$$
即
$$
v_\xi=
\left(\frac{1+7\xi^{-1}}8,\
      \frac{1-\xi^{-1}}4,\
      -\frac{\delta(1-\xi^{-1})}8\right)^t .
\tag{50}
$$
$\xi=1$ 给原单 unit 轴；其余五支的第二、第三输入都是 unit。
第一坐标除下述明确例外也为 unit：
$$
N(1+7\xi^{-1})=
\begin{cases}
36,&\xi=-1,\\
43,&\xi=\omega,\omega^2,\\
57,&\xi=-\omega,-\omega^2.
\end{cases}
\tag{51}
$$
故 $p>7$ 时可能例外只有 $19,43$，准确分支条件为
$\xi\equiv-7\pmod{\mathfrak p}$，该系数的赋值为一。
这些分支没有被删掉，也没有被算作原单 unit 叶域。

## 8. 六分支平均的真实平移小球式

给 $y$ unit，定义
$$
\begin{aligned}
w_N(y)=\Xi_\Delta\{&
L,M\ {\rm unit},\ L-\omega M\in p^N,\\
& y-\xi\delta L\in p^N\text{ 对某个 }\xi\in\mu_6\}.
\end{aligned}
\tag{52}
$$
于是完整的部分输出等式为
$$
\boxed{
(Y_A)_*\left(1_{\bigcup_\xi\mathcal D_{\xi,N}}
                         \nu^{\otimes3}\right)
=w_N(y)\,\nu_A(dy).
}
\tag{53}
$$
平均单支则在右边除以六；未作平均的原单支不等于 (53) 的右边除以六。

此处 $w_N$ 有准确的原测度表达。记
$$
a_y=-\omega y,\qquad b_y=(2+\omega)y,\qquad
J_N(v)=v+p^N\mathbf Z_p .
$$
在 $\xi=1$ 分支，(28) 的两个坐标分别落在
$J_N(a_y),J_N(b_y)$；这用的是原整可逆变换，所以两个小球没有额外相关条件。
其余 $\xi$ 同时把两个中心乘 $\xi^{-1}$。
$\Xi_\Delta$ 的同时不变性使六个辅助分支质量相等。
由 (26)，因此
$$
\boxed{
\begin{aligned}
w_N(y)=6\bigl\{&
\nu_K(J_N(a_y))\nu_D(J_N(b_y))\\
&+12b\,\nu_F(J_N(a_y))\nu_G(J_N(b_y))\\
&+4b\,\nu_B(J_N(a_y))\nu_T(J_N(b_y))\\
&-8b^2\,\nu_E(J_N(a_y))\nu_T(J_N(b_y))
\bigr\}.
\end{aligned}}
\tag{54}
$$
所有相位、因子二及 $\delta$ 均已在原坐标里支付。
这里的后三项是在 **unit 中心的平移小球** 上取值，不能以其原点
深球质量为零为由删除。$w_N(y)$ 是真实随部分输出变化的函数；
没有把它预设成常数或 $q_{\omega,N}$。

还可保全它的共同深度边界。把 (52) 去掉 unit 限制后的并集质量记为
$W_N(y)$。若 $v_p(y)\ge N$，该并集正是 $L,M\in p^N$，故
$$
W_N(y)=\lambda_\Xi^N.
\tag{55}
$$
若 $a=v_p(y)<N$，该并集中 $v_p(L)=v_p(M)=a$，
由 (30) 得
$$
\boxed{
W_N(y)=\lambda_\Xi^a
       w_{N-a}(\kappa^{-a}y).
}
\tag{56}
$$
因此共同深度已完全支付，而剩余 unit 小球观察准确是 (54)。

## 9. 另一个同域的两输入部分联合

(47) 中的第一行还给一个可保留任意其余输入条件的真实身份。
令
$$
Y_{23}=2X_2+\delta X_3,\qquad Q_{23}=\delta X_2+2X_3.
$$
其行列式为七。原函数
$$
\sigma(2z+\delta t)\sigma(\delta z+2t)
$$
在 $z,t$ 的交叉 Gaussian 为零，分别是 degree 七。
只平均 $t$ 的 $\mu_6$ 后，$z$ 型为二；
该空间只有 $\sigma^7xy$ 一条线。
原部分来源是
$$
F_{23}=\sigma(2z)\sigma(\delta z)
      =-2\delta\sigma^7xy=2\delta z^2+\cdots.
$$
辅助质量为一、degree 七型零，故准确为
$D_7=-\Theta^2C$。因此全测度身份是
$$
\boxed{
\mathsf P_{\mu_6,Q}(Y_{23},Q_{23})_*\nu^{\otimes2}
=\nu_{F_{23}}\otimes\nu_{D_7}.
}
\tag{57}
$$
同原点深层限制和秩一论证给
$$
\nu_{F_{23}}|_p=\lambda_{23}[\kappa]_*\nu_{F_{23}},\qquad
\nu_{D_7}|_p=\lambda_7[\kappa]_*\nu_{D_7},\qquad
\lambda_{23}\lambda_7=\lambda_\sigma^2.
\tag{58}
$$
两个标量都是单位：$D_7$ 的质量一、$F_{23}$ 的二阶矩
$4\delta\Omega^2$ 是单位，给其整性，乘积是单位。
本篇未重新指定这条 $\lambda_7$ 的绝对有限角色。

(57) 可以与任意独立的 $X_1,X_4,X_5,X_6$ 条件一起使用。
但
$$
X_2,X_3\in p^N
\quad\Longleftrightarrow\quad
Y_{23},Q_{23}\in p^N
\tag{59}
$$
仍有 **部分输出** $Y_{23}$ 的条件。
不能只使用辅助质量 $\lambda_7^N$ 而忘掉该条件。
这也只直接支付相同深度的两输入；不同独立深度须保其原斜域。

## 10. 对原完整中央观察的准确意义

(7)、(43)–(45) 是全测度身份。因此当额外域仅依赖被允许的辅助时，
可以直接乘原输出 unit 条件、任一 tame 测试以及
$\langle Y\rangle^{(p-1)u}$，再对 $u$ 求导。
例如六输入无额外叶限制时，
$$
\mathcal J_{\mathcal H_{\zeta,N}}(u)
=q_{\zeta,N}J_S(u),\qquad
\mathcal J'_{\mathcal H_{\zeta,N}}(0)
=q_{\zeta,N}J'_S(0).
\tag{60}
$$
两个已付单位相位 (40) 因而给原观察的无损返回。
第二相位 $\omega$ 的整个双非单位边界由 (37) 支付，
但原叶域还须使用 (48)–(54) 的六分支和随部分输出变化的权。

R339 的叶族还包含原 norm3 展开后各叶的独立深度。
(45)、(53)、(57) 均明确给出可共同保留的坐标；
本篇没有把这些独立限制全部改成辅助条件。
要把 R339 已证的非零子域送回原 $J'_S(0)$，
尚须对 (54) 的实际平移小球项或 (48) 中五个非原叶分支取得相应控制。
这里取得的是同一实际 $\Xi_\Delta$ 的新完整 core、
全部共同补域及一个真实跨相位叶域接口。

## 引用

- [R350：六相位碰撞及叶补域](R350-original-diagonal-pair-six-phase-collision-and-leaf-complement.md)，原 $\Xi_\Delta$、五输入核及六条差来源。
- [R357：完整和差四项联合式](R357-original-pair-sum-difference-joint-and-collision-boundary.md)，原六维辅助空间与全 CM 截线。
- [R358：碰撞参考的绝对 core](R358-original-collision-reference-absolute-cores-and-unit-tubes.md)，$D,K$ 的全普通相位及单位质量。
- [R339：原 norm3 叶深度族](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)，独立深度子域的非零输入。
