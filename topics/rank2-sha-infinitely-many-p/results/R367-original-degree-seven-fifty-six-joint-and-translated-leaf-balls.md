# R367：原 degree 七与五十六联合、正交三坐标及叶域平移球

日期：2026-11-13。**状态：已证明。** 在同一原三输入中使用
$Y_{123},Q_{23},R$ 三个整坐标，行列式为 $-56$，Gram 矩阵为
$\operatorname{diag}(8,7,56)$。两个实际辅助分别作 $\mu_6$ 投影后，
完整联合准确为原三因子来源、degree 七参考与一条新的
degree 五十六来源的张量积。新来源给出固定原微分式、实际有界核、
完整普通 core 与三阶收缩尾。
R362 原叶六支平均中的四项平移小球因此合为一项。
部分输出 $Y_{123}$ 的指标仍保留；本篇不从辅助质量推出原中央非零。

## 1. 原对象及整正交坐标

同 R362，固定
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad\gamma=3+\omega,
$$
$$
\Theta=x\sigma^2,\quad C=y\sigma^3,\quad
S=-\frac1{84}\sigma(z)\sigma(2z)\sigma(\delta z)
                    \sigma(2\delta z)\sigma(\gamma z)\sigma(\bar\gamma z).
\tag{1}
$$
对每个普通 $p>7$，所有测度都用原 $E_{17}$ 周期 $\Omega$；
$\nu=\nu_\sigma$，$\int e^{zx/\Omega}d\nu(x)=\sigma(z)$。
采用 R358、R362 的
$$
\kappa=p/\bar\pi^2,\quad
\lambda_\sigma=\varepsilon^3/\bar\pi,\quad
t_p=\lambda_\sigma\kappa,\quad
\lambda_\Xi=\lambda_K\lambda_D
           =\varepsilon^2(2/p)/\bar\pi^2.
\tag{2}
$$

在原第 $1,2,3$ 个 sigma 输入中设
$$
V=2X_2+\delta X_3,\qquad
Y_A=X_1+V,\qquad
Q=\delta X_2+2X_3,\qquad
R=V-7X_1.
\tag{3}
$$
矩阵及逆为
$$
\begin{pmatrix}Y_A\\Q\\R\end{pmatrix}
=
\begin{pmatrix}
1&2&\delta\\
0&\delta&2\\
-7&2&\delta
\end{pmatrix}
\begin{pmatrix}X_1\\X_2\\X_3\end{pmatrix},
\qquad \det=-56,
\tag{4}
$$
$$
X_1=(Y_A-R)/8,\qquad V=(7Y_A+R)/8,
$$
$$
X_2=(2V-\delta Q)/7,\qquad X_3=(-\delta V+2Q)/7.
\tag{5}
$$
三行的 Hermitian Gram 矩阵准确为
$$
\boxed{\operatorname{diag}(8,7,56).}
\tag{6}
$$
所以原整格、所有深层和全部交叉 Gaussian 都已支付。
特别是三个原输入同时在 $p^n$，当且仅当这三个新坐标同时在 $p^n$。

定义已付的两条部分来源
$$
F_{23}(z)=\sigma(2z)\sigma(\delta z)
          =-2\delta\sigma^7xy=2\delta z^2+\cdots,
$$
$$
A(z)=\sigma(z)F_{23}(z)
     =-2\delta\sigma^8xy=2\delta z^3+\cdots,
\qquad D_7=-\Theta^2C.
\tag{7}
$$
$D_7(0)=1$。R362 已证明其完整 core 标量 $\lambda_7$ 是单位，且
$$
\nu_{D_7}|_p=\lambda_7[\kappa]_*\nu_{D_7},\qquad
\nu_{F_{23}}|_p=\lambda_{23}[\kappa]_*\nu_{F_{23}},
\quad \lambda_{23}\lambda_7=\lambda_\sigma^2.
\tag{8}
$$
第 2–4 节的联合证明不依赖 $\lambda_7$ 的进一步绝对角色识别；
已独立发表的 R368 则支付下列单位子族。

## 2. 原三变量全函数及两个真正可交换投影

原联合变换正是
$$
\mathcal G(z,t,w)=
\sigma(z-7w)\,
\sigma\bigl(2(z+w)+\delta t\bigr)\,
\sigma\bigl(\delta(z+w)+2t\bigr).
\tag{9}
$$
先只平均 $t$ 的 $\mu_6$。R362 的真实两输入身份给
$$
\mathsf P_t\mathcal G(z,t,w)
=\sigma(z-7w)F_{23}(z+w)D_7(t).
\tag{10}
$$
这一步固定 $X_1,V$，因此固定 $Y_A,R$，并没有改变所需的部分输出。

再令
$$
G(z,w)=\sigma(z-7w)F_{23}(z+w).
$$
由 (6)，其真实线丛为
$\mathcal O(8O)\boxtimes\mathcal O(56O)$；
也可直接从 degree 一与七算出交叉项 $-7+7=0$。
sigma 型一、$F_{23}$ 型二，所以
$$
G(\zeta z,\zeta w)=\zeta^3G(z,w).
\tag{11}
$$
只平均 $w$ 后，$z$ 属于 degree 八、型三的唯一线 $A$。
因此得到整个函数身份
$$
\boxed{
\mathsf P_w G(z,w)=A(z)\mathcal E(w),\qquad
\mathcal E(w)=\frac{[z^3]G(z,w)}{2\delta}.
}
\tag{12}
$$
$\mathcal E$ 是真实 degree 五十六、型零、原点质量一的全纯来源。

这两个投影在实际坐标 $(Y_A,Q,R)$ 上分别只作用 $Q,R$，
故准确可交换。合并为
$$
\boxed{
\mathsf P_Q\mathsf P_R
   (Y_A,Q,R)_*\nu^{\otimes3}
=\nu_A\otimes\nu_{D_7}\otimes\nu_{\mathcal E}.
}
\tag{13}
$$
它给出完整联合而非三个边际。只需要两个辅助各自 $\mu_6$ 不变；
没有先把原测度当作不变测度。

## 3. 新来源的原微分式和有界加权核

(12) 给完全明确的四项微分式
$$
\boxed{
\begin{aligned}
\mathcal E(w)=\frac1{12\delta}\{&
\sigma'''(-7w)F_{23}(w)
+3\sigma''(-7w)F_{23}'(w)\\
&+3\sigma'(-7w)F_{23}''(w)
+\sigma(-7w)F_{23}'''(w)\}.
\end{aligned}}
\tag{14}
$$
所有四项必须一起保留。它们共同是上述原线丛截面；
不能从其中一项的准周期或极部单独取结论。

原有界测度有两种同一归一的实际核表示：
$$
\boxed{
\nu_{\mathcal E}
=\frac1{12\delta\Omega^3}
 R_*\bigl(Y_A^3\,\nu^{\otimes3}\bigr),
}
\tag{15}
$$
以及把原第二、第三输入真正相加后的
$$
\boxed{
\nu_{\mathcal E}
=\frac1{12\delta\Omega^3}
 (v-7x)_*\bigl((x+v)^3\,\nu(dx)\nu_{F_{23}}(dv)\bigr).
}
\tag{16}
$$
这里的二输入来自加法卷积，不是 Mellin 乘积。
原矩
$\int x\,d\nu=\Omega$、
$\int v^2d\nu_{F_{23}}=4\delta\Omega^2$
使 (16) 的质量准确为一。
所有分母在普通 $p>7$ 都是单位，所以这些是原有界整测度。

新来源还可直接由 R357 完整四项式读出。若该篇函数为
$$
H(t,u)=K(t)D(u)+12bF(t)G_0(u)+4bB(t)T(u)-8b^2E(t)T(u),
$$
其中
$$
F=\sigma^4\Theta^2,\quad G_0=\sigma^2\Theta,\quad
B=\sigma^2\Theta^3,\quad T=\sigma^4,\quad E=\sigma^8,
$$
则
$$
\boxed{\mathcal E(w)=H(w,-2\delta w).}
\tag{17}
$$
为核对全部单位和因子二，R362 的
$P=\delta(L+M),Q_0=\delta(L-M)$ 满足
$$
\frac{Q_0-\delta P}{2}=-\omega Q,\qquad
P-2\delta Q_0=\omega R.
\tag{18}
$$
这两个等式是原坐标恒等式。
$D_7,\mathcal E$ 都型零，因此所列 $\mu_6$ 单位已准确支付；
未归一 tame 测试仍直接使用 (3) 的坐标。

(13) 也可写为 R362 同一原 $\Xi_\Delta$ 的第二个完整联合：
在 (18) 所给实际换坐标后，只再平均一个辅助，就得到
$\nu_{D_7}\otimes\nu_{\mathcal E}$。
原 $\Xi_\Delta$ 同时不变，使分别平均两个辅助与只再平均其中一个相同。

## 4. 完整 core 和两个不同 primitive 输入

R362 已付
$$
\nu_A|_p=\lambda_A[\kappa]_*\nu_A,\qquad
\lambda_A=\lambda_\sigma^3/\lambda_\Xi.
$$
把 (13) 限制到三个新坐标同时深一层，使用 (4) 和原 sigma core。
由于 $\nu_A$ 的三阶矩为单位、另两因子质量一，秩一张量标量准确确定：
$$
\boxed{
\nu_{\mathcal E}|_p=\lambda_{\mathcal E}[\kappa]_*\nu_{\mathcal E},
\qquad
\lambda_{\mathcal E}=\frac{\lambda_\Xi}{\lambda_7}
                    =\frac{\lambda_K\lambda_D}{\lambda_7}.
}
\tag{19}
$$
特别是
$$
\nu_{\mathcal E}(p^n\mathbf Z_p)=\lambda_{\mathcal E}^n,\qquad
\nu_{\mathcal E}(\mathbf Z_p^\times)=1-\lambda_{\mathcal E}.
\tag{20}
$$
$\lambda_{\mathcal E}$ 是单位。进一步由 R368 的独立完整相位，若
$\pi_0=\varepsilon\pi$、$u_p\in\mu_6$ 是
$\pi_0/\bar\pi_0\bmod7$ 的唯一 lift，则
$
\boxed{
\lambda_{\mathcal E}=\frac{(2/p)}{u_p\bar\pi_0},\qquad
1-\lambda_{\mathcal E}\in\mathcal O^\times
\quad\text{当 }p\equiv1\pmod3,\ (-14/p)=1 .
}
\tag{20a}
$
该固定族包含全部 $p\equiv1\pmod{168}$ 的素数。
这支付的是原碰撞观察的单位系数，不单独赋值原 $J'_S(0)$。
在未满足该充分条件的普通素数上，仍使用完整 (19)，不擅自删去质量。

(15) 的三个 sigma 输入全部深一层，给
$t_p^3[\kappa]_*\nu_{\mathcal E}$。
(16) 的两个输入 $x,v$ 全部深一层，则给
$(t_p^3/\lambda_7)[\kappa]_*\nu_{\mathcal E}$。
分别删去这些实际域，得到
$$
\boxed{
\nu_{\mathcal E}
=\nu_{\mathcal E,3}^{\rm prim}+t_p^3[\kappa]_*\nu_{\mathcal E}
=\nu_{\mathcal E,2}^{\rm prim}
       +(t_p^3/\lambda_7)[\kappa]_*\nu_{\mathcal E}.
}
\tag{21}
$$
两种原 primitive 不同。准确差为
$$
\boxed{
\nu_{\mathcal E,3}^{\rm prim}
-\nu_{\mathcal E,2}^{\rm prim}
=t_p^3(\lambda_7^{-1}-1)[\kappa]_*\nu_{\mathcal E}.
}
\tag{22}
$$
左边就是 $X_1,V$ 都深、但 $X_2,X_3$ 至少一个 unit 的真实 carry，
还保着原三次权。

两个几何级数都在有界测度范数下收敛；截到 $n=M$ 后的尾赋值
至少为 $3(M+1)$。例如
$$
\nu_{\mathcal E}
=\sum_{n\ge0}(t_p^3/\lambda_7)^n
                    [\kappa^n]_*\nu_{\mathcal E,2}^{\rm prim}.
\tag{23}
$$
这三阶收缩来自原输入权，不能拿它替换单位标量 (19) 的整个输出 core。
所有非单位输出均包含在 (21)–(23) 中。

对 $d=p-1$，全部 tame 环带归一式为
$$
\mathcal M_{\mathcal E,\ell}^{[n]}(u)
=\lambda_{\mathcal E}^n
 \omega_p(\bar\pi)^{-2n\ell}
 \langle\bar\pi\rangle^{-2ndu}
 \mathcal M_{\mathcal E,\ell}(u).
\tag{24}
$$
其导数完整保留
$-2nd\log_p(\bar\pi)\mathcal M_{\mathcal E,\ell}(0)$。
本篇没有删除新参考的未知相对斜率。

## 5. 原碰撞管成为真实独立矩形

在 R362 的同一 $(L,M)$ 中，相位 $\omega$ 的 tube 准确等于
$$
\boxed{
\{L,M\ {\rm unit},\ L-\omega M\in p^N\}
=\{Q\in p^N,\ R\ {\rm unit}\},\qquad N\ge1.
}
\tag{25}
$$
(18) 给碰撞差；其余从
$R=-7\delta L+(4+\omega)Q$
或直接从原坐标可核，$Q$ 深时 $R$ 与 $L$ 相差固定单位。
因此 (13) 支付
$$
q_{\omega,N}
=\lambda_7^N(1-\lambda_{\mathcal E})
=(\lambda_7-\lambda_K\lambda_D)\lambda_7^{N-1}.
\tag{26}
$$
同一个真实两辅助联合还给任意共同深度和环带的所有矩形质量，
例如
$$
\Xi_\Delta\{Q\in p^N,R\in p^M\}
=\lambda_7^N\lambda_{\mathcal E}^M.
\tag{27}
$$
此处的 (27) 使用分别 $\mu_6$ 不变的域，所以可用投影后的乘积；
它没有声称原未经投影的两个辅助独立。

乘上原第 $4,5,6$ 个不受限输入以后，(13) 给
$$
\boxed{
\mathsf P_Q\mathsf P_R
 (Y,Q,R)_*\eta_6
=\nu_S\otimes\nu_{D_7}\otimes\nu_{\mathcal E},
\qquad \eta_6=-\nu^{\otimes6}/84.
}
\tag{28}
$$
所以任意分别不变的辅助测试，确实对原同一完整中央函数作标量返回。
这包括 (25)，不包括下面尚未平均的单个叶域。

## 6. 单叶、六支并与真正的 translated ball

原三输入的相同深度叶域为
$$
\mathcal D_N=\{X_1\ {\rm unit},X_2,X_3\in p^N\}.
$$
由 (5)，精确地
$$
\boxed{
\mathcal D_N=
\{Y_A\ {\rm unit},Q\in p^N,\ R+7Y_A\in p^N\}.
}
\tag{29}
$$
第一步 $Q$ 的投影与 (29) 相容；第二步 $R$ 的投影不相容，
因为它固定 $Y_A$。因此原单支仍不能直接使用 (13)。

实际允许的六支为
$$
\mathcal D_{\xi,N}
=\{Y_A\ {\rm unit},Q\in p^N,\ R+7\xi^{-1}Y_A\in p^N\},
\qquad \xi\in\mu_6.
\tag{30}
$$
它们两两不交，只有 $\xi=1$ 是原叶支。
这正是 R362 同一六支；在原输入中的准确线管仍为
$$
(X_1,X_2,X_3)
\equiv Y_A\left(
 \frac{1+7\xi^{-1}}8,\
 \frac{1-\xi^{-1}}4,\
 -\frac{\delta(1-\xi^{-1})}8
\right)\pmod{p^N}.
\tag{31}
$$
因此 R362 的五个非原叶分支及 $p=19,43$ 的精确例外全部保留。

对 $y$ unit，(13) 现在把 R362 四项平移球式准确合成一项：
$$
\boxed{
w_N(y)=6\lambda_7^N
                \nu_{\mathcal E}(-7y+p^N\mathbf Z_p).
}
\tag{32}
$$
原因是 $Q$ 深球贡献 $\lambda_7^N$；
$\mathcal E$ 型零，使六个中心
$-7\xi^{-1}y$ 的小球质量相同。其原完整部分输出式为
$$
\boxed{
(Y_A)_*\left(1_{\bigcup_\xi\mathcal D_{\xi,N}}\nu^{\otimes3}\right)
=6\lambda_7^N
 \nu_{\mathcal E}(-7y+p^N)\,1_{\mathbf Z_p^\times}(y)\nu_A(dy).
}
\tag{33}
$$
平均六支则把右边除以六。
未平均的原单支不等于这个平均。

(32) 的小球中心是 unit。它不是原点深球质量
$\lambda_{\mathcal E}^N$，也不是原单位总质量
$1-\lambda_{\mathcal E}$。
普通 core (19) 没有把这些 unit 平移球全部指定成同一个数。
因此 (32) 是实际补域的压缩，而非免费消去补域。

## 7. 不同原深度的准确斜域与平均量词

令 $n_2,n_3\ge1$，原叶条件
$X_1$ unit、$X_2\in p^{n_2}$、$X_3\in p^{n_3}$
在三个新坐标中准确为 $Y_A$ unit 及
$$
\boxed{
\begin{aligned}
2(7Y_A+R)-8\delta Q&\in p^{n_2},\\
-\delta(7Y_A+R)+16Q&\in p^{n_3}.
\end{aligned}}
\tag{34}
$$
因 $56$ 是单位，没有改动深度。
当 $n_2=n_3=N$ 才化为 (29)。

设 $I_{n_2,n_3}(y,q,r)$ 是 (34) 与 $y$ unit 的指示函数，
并定义保留重数的实际平均
$$
\overline I(y,q,r)
=\frac1{36}\sum_{\alpha,\beta\in\mu_6}
                    I_{n_2,n_3}(y,\alpha q,\beta r).
\tag{35}
$$
由 (13) 的全联合，严格得到
$$
\boxed{
(Y_A)_*(\overline I\,\nu^{\otimes3})
=\nu_A(dy)\iint I_{n_2,n_3}(y,q,r)
                    \,d\nu_{D_7}(q)d\nu_{\mathcal E}(r).
}
\tag{36}
$$
这是三十六项平均；其域可能交叠，不能按不交的并集计算。
相同深度时第一组平均是重复的，(36) 正好等于 (33) 除以六。
不同深度的两条斜条件完整保留。

## 8. 全输出、全部中央核以及剩余的具体观察

上述身份都可与任意独立的第 $4,5,6$ 输入条件共同使用；
这些条件若存在，输出来源必须保为对应的受限卷积。
设
$$
Y_B=2\delta X_4+\gamma X_5+\bar\gamma X_6,
$$
$g(X_4,X_5,X_6)$ 有界，$\Phi(Y)$ 是任意有界输出测试。
(33) 的完整六输入版本是
$$
\begin{aligned}
&\int_{\bigcup_\xi\mathcal D_{\xi,N}}
 g\,\Phi(Y_A+Y_B)\,d\eta_6\\
&\quad=-\frac{\lambda_7^N}{14}
 \int_{y\ {\rm unit}}\int
 g\,\Phi(y+Y_B)\,
 \nu_{\mathcal E}(-7y+p^N)\,
               d\nu_A(y)\,d\nu^{\otimes3}(X_4,X_5,X_6).
\end{aligned}
\tag{37}
$$
因子 $-1/84$、六分支及原 $Y_B$ 尺度全部保留。

可以在 (28)、(37) 中直接取
$$
\Phi(Y)=1_{\mathbf Z_p^\times}(Y)
        \omega_p(Y)^\ell\langle Y\rangle^{(p-1)u}
$$
及其中央导数。对于仅由两个辅助决定的矩形或碰撞管，(28) 给
已付标量乘原 $J_S(u)$。对于单叶或六支并，(37) 还含真实
$\nu_{\mathcal E}(-7y+p^N)$，以及可能存在的其他叶输入条件。
这些不能换成原 $J_S'(0)$ 的标量倍数。

本篇由同一原三输入取得两个完全独立的辅助观察，并把原相位
$\omega$ 碰撞管和叶六支补域压到固定一条新来源。
要从 R339 的非零独立叶 grid 返回总中央，余下的具体对象已是
(32)、(34)、(37) 的 unit 平移球与原部分输出耦合，
而非未指定的二维测度或被遗漏的 Gaussian。

## 引用

- [R362：原三输入与整个双辅助 core](R362-original-triple-pair-core-and-six-branch-leaf-domain.md)，原 $\Xi_\Delta$、$F_{23},D_7$ 及完整六支域。
- [R357：和差完整四项联合](R357-original-pair-sum-difference-joint-and-collision-boundary.md)，(17) 所用全部原来源。
- [R358：两碰撞参考绝对 core](R358-original-collision-reference-absolute-cores-and-unit-tubes.md)，$\lambda_K,\lambda_D$。
- [R368：degree 七绝对 core 与固定普通单位族](R368-original-degree-seven-absolute-core-and-fixed-prime-unit-tubes.md)，(20a) 的绝对相位和充分单位判据。
- [R339：原 norm3 独立叶深度族](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)，需保留其全部独立叶条件。
