# R374：原七次有限角色的完整互反识别、两条固定六次扭曲与原周期

日期：2026-11-14。**状态：本篇的有限角色、两条固定 CM 曲线身份、
实际导子以及原形式周期比较均已证明。**
原 degree 七来源的相位不是任取一个七次扭曲符号；
在本课题的 primary 规范中，二处立方修正准确给出 $-28$。
本篇保留 R367 的 unit 平移小球，不从辅助参考的秩零或其非零质量
推原 $J'_S(0)\ne0$。

## 1. 同一规范与两个准确角色

沿用 R302、R316、R368：
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad \mathcal O=\mathbf Z[\omega].
$$
$E_0:y^2=x^3+1$ 的实际 CM 角色为 $\psi_0$。
对普通 $p>7$ 及原选定素理想 $\mathfrak p$，
$$
\pi_0=\psi_0(\mathfrak p),\qquad
\pi_0\bar\pi_0=p,\qquad
\pi_0\equiv1\pmod{2\delta},\qquad
v_{\mathfrak p}(\pi_0)=1.
\tag{1}
$$
R368 已给唯一
$$
u_7\in\mu_6,\qquad
u_7\equiv\pi_0/\bar\pi_0\pmod{7\mathcal O}.
\tag{2}
$$
固定 $b=17$ 时，仍有
$$
\pi=\psi_b(\mathfrak p),\quad
\varepsilon=\pi_0/\pi,\quad
\kappa=p/\bar\pi^2.
$$
原两个参考是
$$
D_7=-\sigma^7x^2y,\qquad
\mathcal E=\mathcal E_{56}
\quad\text{（R367 的原微分来源），}
$$
其质量均为一，且完整原 core 为
$$
\lambda_7=\frac{u_7}{\bar\pi_0},\qquad
\lambda_{\mathcal E}=\frac{(2/p)}{u_7\bar\pi_0}.
\tag{3}
$$

用通常的剩余类幂定义 $(a/\mathfrak p)_j$，$j=2,3,6$；
它是原 $K$ 中单位群 $\mu_j$ 的元素，不另取一个复嵌入的共轭。
本篇主结论是
$$
\boxed{u_7=\left(\frac{-28}{\mathfrak p}\right)_6.}
\tag{4}
$$
因此，若 $\psi_D$ 是同一解析 CM type 的
$E_D:y^2=x^3+D$ 角色，则
$$
\boxed{
\psi_{-1/28}=\psi_0u_7,\qquad
\psi_{-7/2}=\psi_0(2/N\,\cdot\,)\,u_7^{-1}.
}
\tag{5}
$$
这里第二式的二次角色在理想 $\mathfrak a$ 上是
$(2/N\mathfrak a)$；在普通素理想上就是 $(2/p)$。
两式是素于 $2\cdot3\cdot7$ 的理想群上的角色等式。
相应的整数模型代表为
$$
\boxed{
E_*:y^2=x^3-268912,\qquad
E_\dagger:y^2=x^3-224,
}
\tag{6}
$$
因为
$$
-268912=14^6(-1/28)=-2^4\,7^5,\qquad
-224=2^6(-7/2).
$$
特别原完整 core 恰为
$$
\boxed{
\lambda_7=\overline{\psi_{-1/28}(\mathfrak p)}^{-1},
\qquad
\lambda_{\mathcal E}=
\overline{\psi_{-7/2}(\mathfrak p)}^{-1}.
}
\tag{7}
$$
$\mathcal E_{56}$ 的下标仍指原来源的 degree；不把它误读为
曲线 $y^2=x^3+56$。

## 2. 二处 primary 修正的准确求值

$\pi_0\equiv1\bmod\delta$。
群
$$
\ker\bigl((\mathcal O/3)^\times
                  \longrightarrow(\mathcal O/\delta)^\times\bigr)
$$
有三个元素，正由 $\mu_3$ 给出。
所以存在唯一 $v\in\mu_3$ 使
$$
v\pi_0\equiv1\pmod3.
$$
置
$$
\alpha=-v\pi_0\equiv2\pmod3.
\tag{8}
$$
这是立方互反律的 primary 素元，和 (1) 的 $2\delta$-primary
素元不同，不能直接等同。

这里使用 Eisenstein 立方互反律：两个不同范数的 primary 素元
$\alpha,\beta\equiv2\bmod3$ 满足
$$
(\alpha/\beta)_3=(\beta/\alpha)_3.
\tag{9}
$$
一个给出完整证明的已发表主来源是
Friesen–Spearman–Williams，Rocky Mountain J. Math. 16 (1986)，
式 (1.1) 及 §2；见文末链接。

二在 $\mathcal O$ 中惰性，且 $2\equiv2\bmod3$，所以由 (9)
$$
\left(\frac2{\mathfrak p}\right)_3
=\left(\frac2\alpha\right)_3
=\left(\frac\alpha2\right)_3.
$$
$\mathcal O/(2)=\mathbf F_4$，这里的幂是 $(4-1)/3=1$。
又 $\pi_0\equiv1\bmod2$，负号在模二消失，因此最后一项是 $v$。
准确得到
$$
\boxed{v=(2/\mathfrak p)_3.}
\tag{10}
$$
这一步是后面 $-28$ 中 $2^2$ 的来源。

## 3. 两个七素位的立方符号

取
$$
\varrho=2+3\omega,\qquad
\bar\varrho=2+3\omega^2,\qquad
\varrho\bar\varrho=7.
$$
两者均为 primary，范数七，与 $\alpha$ 的范数 $p$ 不同。
把 (9) 分别用于这两个素位，再相乘，给
$$
\left(\frac7{\mathfrak p}\right)_3
=\left(\frac\alpha7\right)_3
=\left(\frac{v\pi_0}7\right)_3.
\tag{11}
$$
其中 $-1$ 是立方，故 (8) 的负号不留额外因子。
分母七的符号在此按两个素位相乘；没有将 split 七当成一个
剩余域为 $\mathbf F_{49}$ 的惰性素位。

在
$$
\mathcal O/7=\mathbf F_7\times\mathbf F_7,\qquad
\omega\longmapsto(2,4)
$$
中写 $\pi_0=(a,b)$。第一素位的立方符号在第一分量为 $a^2$。
第二素位的符号在第二分量为 $b^2$，因 $\mu_3$ 的两个嵌入互逆，
该全局单位在第一分量为 $b^{-2}$。所以两个**全局**符号之积在
第一分量为 $(a/b)^2$。由 (2) 和 $\mu_3$ 的单射，
$$
\left(\frac{\pi_0}7\right)_3=u_7^2.
\tag{12}
$$
同时对 $v\in\mu_3$，
$$
(v/7)_3=v^2v^2=v^4=v.
$$
因此 (11) 准确成为
$$
\boxed{(7/\mathfrak p)_3=u_7^2v.}
\tag{13}
$$
如果漏掉 (10) 的 $v$，便会把原角色错误地识别成一个裸的
$\pm7$ 六次扭曲。

## 4. 平方、立方共同确定绝对六次符号

置
$$w=(-28/\mathfrak p)_6.$$
由 (10)、(13)，
$$
w^2=(-28/\mathfrak p)_3
=(2/\mathfrak p)_3^2(7/\mathfrak p)_3
=v^2(u_7^2v)=u_7^2.
\tag{14}
$$
另一方面二次互反给
$$
w^3=(-28/p)=(-7/p)=(p/7).
$$
R368 的完整模七计算是 $u_7^3=(p/7)$；也可由
$ab=p$、$(a/b)^3=(ab)^3$ 直接重得。
故
$$w^3=u_7^3.$$
$\mu_6$ 中平方、立方的共同核为一，(14) 因而证明 (4)。
没有保留一个待拟合的正负号。

本证明用的是固定有限角色及已发表的互反律；
不从有限素数样本外推所有普通素数。

## 5. 六次扭曲方向及两个实际整数模型

对任意非零有理数 $D$，取 $\theta_D^6=D$。
从 $E_D$ 到 $E_0$ 的同构是
$$
(x,y)\longmapsto(x/\theta_D^2,y/\theta_D^3).
$$
在好普通素理想处比较该同构与 Frobenius，
并保持本课题的解析参数
$x(z)=z^{-2}+\cdots,y(z)=-z^{-3}+\cdots$：
坐标变换 $(x,y)\mapsto(\zeta^2x,\zeta^3y)$
对应解析 CM 元 $\zeta^{-1}$。
所以准确方向为
$$
\boxed{
\psi_D(\mathfrak p)
=(D/\mathfrak p)_6^{-1}\psi_0(\mathfrak p).
}
\tag{15}
$$
这和 R345 的原 $E_{1/4}$ 核定方向相同。

将 $D=-1/28$ 代入 (15)，由 (4) 即得第一式 (5)。
第二式需保留二次角色：
$$
(2/p)=(8/\mathfrak p)_6,
$$
所以
$$
\frac{(2/p)}{u_7}
=\left(\frac{8/(-28)}{\mathfrak p}\right)_6
=\left(\frac{-2/7}{\mathfrak p}\right)_6.
\tag{16}
$$
这正是 $D=-7/2$ 在 (15) 中的倒数符号，证明第二式。

对于好惰性有理素数 $\ell\equiv2\bmod3$，
原 $\psi_0((\ell))=-\ell$ 是实数，故其模七比值为一。
另一方面有理 $D$ 的剩余值在 $\mathbf F_\ell^\times$ 中，
而 $(\ell^2-1)/6$ 是 $\ell-1$ 的倍数；
所以惰性素理想处的六次符号也为一。
二次角色 $(2/\ell^2)=1$。
这证明两式在全部好素理想上相同，再由乘法性得到 (5)
所说的整个理想群角色，而不只是一边普通素理想的比较。

对于第一条整数模型，原变量更换
$$
x_{\rm short}=4x,\qquad y_{\rm short}=8y+4
$$
给
$$
\boxed{E_*^{\min}:y^2+y=x^3-4202.}
\tag{17}
$$
其判别式为
$$
-27(1-4\cdot4202)^2=-3^3\,7^{10}.
$$
二处已好；三、七处判别式赋值分别为三、十，都小于十二，
因此这个整模型在所有素数处最小。
微分变换为
$$
\frac{dx_{\rm short}}{2y_{\rm short}}
=\frac12\frac{dx}{2y+1}.
\tag{18}
$$
若使用最小模型的周期，必须同时保留 (18) 的二因子。

## 6. 两个原导子由实际有限角色确定

本节直接给导子证明，故第一条曲线的 $441$ 不只是数据库猜测。

R302 的完整 primary 公式为
$$
\psi_0((a))=a\epsilon_0(a)^{-1},\qquad
\epsilon_0=\chi_{2,0}\chi_3,
\tag{19}
$$
其中 $\chi_{2,0}$ 是 $\mathcal O/(2)=\mathbf F_4$ 的
$\mu_3$ Teichmüller 角色，$\chi_3(a)=a\bmod\delta\in\{\pm1\}$。

对素于七的 $a\in\mathcal O$，定义
$$
U_7(a)\in\mu_6,\qquad
U_7(a)\equiv a/\bar a\pmod7.
$$
它是整个 $(\mathcal O/7)^\times$ 上的乘法角色，且
$$U_7(\zeta)=\zeta^2\quad(\zeta\in\mu_6).$$
(2) 在主理想 $(a)$ 上因此成为
$$
u_7((a))=U_7(a)\epsilon_0(a)^{-2}.
\tag{20}
$$
第一条固定角色为
$$
\psi_*((a))
=a\epsilon_0(a)^{-3}U_7(a)
=a\chi_3(a)U_7(a).
$$
所以它的有限角色准确是
$$
\boxed{\epsilon_*=\chi_3\,U_7^{-1}.}
\tag{21}
$$
二处三次角色已完全抵消。
在两个七素位分别固定另一分量时，$a/\bar a$ 遍历
$\mathbf F_7^\times$，故每个七素位都真正出现一阶导子；
三处的符号也非平凡。
由中国剩余定理，这些地方不能彼此抵消。
于是
$$
\boxed{\mathfrak f_*=(7\delta).}
\tag{22}
$$
其单位条件也准确：
$\epsilon_*(\zeta)=\zeta^3\zeta^{-2}=\zeta$，与 type 一相容。

写 $\chi_8(n)=(2/n)$。第二条角色由 (19)、(20) 给
$$
\psi_\dagger((a))
=a\epsilon_0(a)\chi_8(Na)U_7(a)^{-1},
$$
故
$$
\boxed{
\epsilon_\dagger(a)
=\epsilon_0(a)^{-1}\chi_8(Na)U_7(a).
}
\tag{23}
$$
在二处，$\chi_8\circ N_{K_2/\mathbf Q_2}$ 平凡于 $1+8\mathcal O_2$，
但不平凡于 $1+4\mathcal O_2$：例如
$$N(1+4\omega)=13,\qquad \chi_8(13)=-1.$$
该元素的 tame $\chi_{2,0}$ 值为一，因此三次 tame 角色不能
抵消这个二次 wild 角色。
其余两处和 (22) 一样都确实分歧。
所以
$$
\boxed{\mathfrak f_\dagger=(56\delta).}
\tag{24}
$$
这里 $56=8\cdot7$。

CM 二维表示是这些 type-one 角色从 $K$ 到 $\mathbf Q$ 的诱导；
局部 Artin 导子的诱导公式给
$N(E)=|D_K|N_{K/\mathbf Q}\mathfrak f$。
代入 (22)、(24) 得
$$
\boxed{N(E_*)=441,\qquad N(E_\dagger)=28224.}
\tag{25}
$$
这一标准 CM 导子关系也正是 R302、R316 所用的关系；
本节已经支付其真正有限角色和所有分歧指数。

官方 LMFDB 的
[441.e1 / 441a1](https://www.lmfdb.org/EllipticCurve/Q/441a1/)
记录模型 (17)、导子 $441$、Mordell–Weil 秩与解析秩均为零。
这只是独立的外部数据核对：本篇的 (4)–(25) 不依赖该数据，
也没有在本篇另行完成该曲线的下降或原中央特殊值证明。
后续若使用其完整 Katz/Yang 参考，仍须支付那一条具体的
特殊值、周期和有限 Schwartz 身份。

## 7. 同一来源的全部原周期比较

对每个非零 $b$ 和一组一致的 $\theta_b^6=b$，
保持复周期格与普通形式群周期
$$
\Gamma_b=\theta_b^{-1}\Gamma_0,\qquad
\Omega_{p,b}=\theta_b^{-1}\Omega_{p,0}.
\tag{26}
$$
这是 CM 格及形式群的实际同构；
不把 $\theta_b$ 当成 $\mathbf Z_p$ 测度变量的任意缩放。
三次 CM 使原 reduced sigma 的二次 Gaussian 修正为零，准确有
$$
x_b(z)=\theta_b^2x_0(\theta_bz),\qquad
y_b(z)=\theta_b^3y_0(\theta_bz),\qquad
\sigma_b(z)=\theta_b^{-1}\sigma_0(\theta_bz).
\tag{27}
$$
因此原七次来源的所有常数恰好相消：
$$
\boxed{D_{7,b}(z)=D_{7,0}(\theta_bz).}
\tag{28}
$$

对 degree 五十六不能只从其质量一猜 (28)。
用 R367 的原全函数
$$
G_b(z,w)=\sigma_b(z-7w)
        \sigma_b(2(z+w))\sigma_b(\delta(z+w)),
$$
以及准确归一
$$\mathcal E_b(w)=[z^3]G_b(z,w)/(2\delta),$$
(27) 给
$$
G_b(z,w)=\theta_b^{-3}G_0(\theta_bz,\theta_bw).
$$
取 $z^3$ 系数时 $\theta_b^3$ 精确消掉前面的因子，得到
$$
\boxed{\mathcal E_b(w)=\mathcal E_0(\theta_bw).}
\tag{29}
$$
所以对两条原来源 $G=D_7,\mathcal E$，完整 Amice 级数准确是
$$
\boxed{
G_b\bigl(\Omega_{p,b}\log(1+Z)\bigr)
=G_0\bigl(\Omega_{p,0}\log(1+Z)\bigr).
}
\tag{30}
$$
这首先是正式级数身份；由原有界测度的唯一性，它是整个测度
身份，保留全部 tame 分支与全部深度，不只比较一个质量或导数。

(30) 可分别用于 $b=17,-1/28,-7/2$。
原 $E_{17}$ 来源因而可以在上述固定曲线的形式群坐标中写出，
而不用重新选择 Mellin 变量。
复周期同样只能按 (26) 传送；负 $b$ 时这里说的是指定 CM
生成周期，不自动宣称它是正实 primitive 周期。
换到 (17) 的最小模型，另按 (18) 传送微分与周期。

特别若两条固定曲线自己的普通参数为
$$
\pi_* =u_7\pi_0,\qquad
\pi_\dagger=(2/p)u_7^{-1}\pi_0,
$$
则
$$
\kappa_*=u_7^2(p/\bar\pi_0^2),\qquad
\kappa_\dagger=u_7^{-2}(p/\bar\pi_0^2).
\tag{31}
$$
两条原来源都为 $\mu_6$ 型零，故 (31) 的六次单位作用在整个
测度上恒等。这说明 (7)、(30) 与原 $\kappa$ core 完全相容；
没有将不同曲线的 Frobenius 缩放未经支付就视为同一数。

## 8. 固定角色识别后仍保留的真实小球

对 $G=D_7$ 或 $\mathcal E$，记其完整 Amice 级数为
$\widehat\nu_G(Z)$。对任意 $a\bmod p^n$，实际小球质量是
$$
\boxed{
\nu_G(a+p^n\mathbf Z_p)
=\frac1{p^n}\sum_{\zeta^{p^n}=1}
             \zeta^{-a}\widehat\nu_G(\zeta-1).
}
\tag{32}
$$
这由有限加法角色正交直接得到，包含完整的 $p^{-n}$ 及
所有根单位支。级数在 $\zeta-1$ 处按原有界 Amice 级数取值。
不能先把形式表达中的 $\log\zeta$ 替为零，再把 (32) 错算成
原点质量；原外层 sigma 的复合不能作那样的点值换序。

R367 的同一六支叶平均现在仍准确是
$$
\boxed{
w_N(y)=6\lambda_7^N\,
             \nu_{\mathcal E}(-7y+p^N\mathbf Z_p),
\qquad y\in\mathbf Z_p^\times.
}
\tag{33}
$$
(4)–(31) 把 (33) 的 core 与实际固定 CM 曲线完全识别。
但 (32) 的非平凡加法角色和 $y$ 依赖没有因此消失；
尤其它不等于 $\lambda_\mathcal E^N$，
也不等于原单位总质量 $1-\lambda_\mathcal E$。
原单叶、另外五支以及部分输出 $Y_A$ 在 R367 的量词继续保持。

当前可直接使用的新增事实是：两条原辅助的有限相位已经是
(6) 的固定、绝对、全地方 CM 角色，所有曲线与原 $E_{17}$ 的
周期传送由 (26)–(31) 给出。
后继对 (32) 的带加法角色 theta 运输，必须使用这个真正的
有限来源和全部根单位支，不能仅由固定曲线秩零或
$1-\lambda_\mathcal E$ 为单位推 (33) 是一个可删除常数。

## 9. 来源与提交说明

1. C. Friesen, B. K. Spearman, K. S. Williams,
   *Another proof of Eisenstein's law of cubic reciprocity and its supplement*,
   Rocky Mountain J. Math. **16** (1986), 395–402，式 (1.1)、§2：
   [作者公开全文](https://people.math.carleton.ca/~williams/papers/pdf/141.pdf)。
   本篇只以其 primary 素元的互反律为外部代数输入；
   二处修正、两七素位比较和六次绝对相位均在 §§2–4 逐项证明。
2. [R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)：
   原 $E_0$ 的 $2\delta$-primary 角色及全部周期规范。
3. [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)、
   [R345](R345-original-degree-three-absolute-core-phase-and-middle-cartier-row.md)：
   原 sigma 正式整性、实际六次扭曲方向与 CM 形式周期。
4. [R367](R367-original-degree-seven-fifty-six-joint-and-translated-leaf-balls.md)：
   $\mathcal E$ 的完整全函数、三阶归一、原小球及叶域。
5. [R368](R368-original-degree-seven-absolute-core-and-fixed-prime-unit-tubes.md)、
   [R370](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)：
   原 degree 七绝对 trace 及共同固定无穷素数族。
6. [LMFDB 441a1](https://www.lmfdb.org/EllipticCurve/Q/441a1/)：
   仅用于第6节所注明的外部曲线数据核对，未替代本篇证明。

本条通过 GitHub Contents API 提交小文本；没有声称执行本地 git pull。
提交前两 README 的原文与已读基准
35e391cd9a73d5a514d252312d3ff61962ddbc70 相同，内容 blob 仍为
f787a306d90892d8dec765dc59747d60ba39f055、
f8dd8071ac0c2b31f344a40c15ac2a42796bf9af。
