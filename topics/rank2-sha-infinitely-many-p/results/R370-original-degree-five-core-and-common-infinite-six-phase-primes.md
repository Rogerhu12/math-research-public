# R370：原 degree 五的真实 core 与六碰撞相位的共同无限素数族

日期：2026-11-13。**状态：以下原两输入联合、degree 五 core 的准确
有限相位范围、未知符号下的统一单位界，以及全部六碰撞相位的同一
固定无限素数族均已证明。**
本篇没有猜定 degree 五的最后一个绝对符号；
所需单位结论对其两种可能值统一成立。
原叶域的部分输出条件及全部补域仍保留，主目标未完成。

## 1. 原对象和所付结论

保持 R316、R358、R362、R368 的同一曲线、sigma、周期及测度：
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad \delta=1+2\omega,
$$
$$
\Theta=x\sigma^2,\quad C=y\sigma^3,\quad
\nu=\nu_{\sigma,17},\qquad
\pi_0=\varepsilon\pi,\quad\bar\pi_0=\varepsilon^{-1}\bar\pi,\quad
\kappa=p/\bar\pi^2.
$$
这里 $p>7$ 普通、$\pi_0\equiv1\bmod2\delta$ 为 $E_0:y^2=x^3+1$
的实际 primary Frobenius，所有原微分及 $\Omega_{p,0}=\theta\Omega_p$
保持不变。

原两个相位 $-\omega,-\omega^2$ 的来源是
$$
\boxed{
D_5=-\Theta C=-\sigma^5xy,\qquad D_5(0)=1.
}
\tag{1}
$$
同一个原 pair 的部分输出来源为
$$
\boxed{
F_{12}=\sigma(z)\sigma(2z)=-2\sigma^5y=2z^2+\cdots.
}
\tag{2}
$$

定义唯一的实际单位
$$
\boxed{
u_{5,p}\in\mu_6,\qquad
u_{5,p}\equiv\pi_0/\bar\pi_0\pmod{5\mathcal O_K}.
}
\tag{3}
$$
五在 $K$ 中惰性，$\mathcal O_K/5=\mathbf F_{25}$ 的 norm-one 群
恰为原 $\mu_6$，所以 (3) 有意义。下文记 $u_5=u_{5,p}$。

**定理。** 存在由原完整 trace 唯一确定的
$\eta_{5,p}\in\{1,-1\}$，使
$$
\boxed{
\begin{aligned}
\nu_{D_5}|_p&=\lambda_5[\kappa]_*\nu_{D_5},
&\lambda_5&=\frac{\varepsilon\eta_{5,p}u_5}{\bar\pi}
           =\frac{\eta_{5,p}u_5}{\bar\pi_0},\\
\nu_{F_{12}}|_p&=\lambda_{12}[\kappa]_*\nu_{F_{12}},
&\lambda_{12}&=\frac{\varepsilon^5\eta_{5,p}u_5^{-1}}{\bar\pi}.
\end{aligned}}
\tag{4}
$$
这些是整个测度式，且
$$\lambda_{12}\lambda_5=\lambda_\sigma^2=\bar\pi^{-2}.\tag{5}$$
$\eta_{5,p}$ 是实际算子给出的符号，不是按需要任选的平方根。

令
$$
\lambda_\Xi=\lambda_K\lambda_D
=\frac{\chi_2(p)}{\bar\pi_0^2},\qquad \chi_2(p)=(2/p).
\tag{6}
$$
若 $u_5=\pm1$，则无论实际 $\eta_{5,p}$ 取哪个值，都有
$$
\boxed{
1-\lambda_5,\quad\lambda_5-\lambda_\Xi
\in\mathcal O_{\mathfrak p}^{\times}.
}
\tag{7}
$$

现在取下面**一个固定**的有限 Galois 扩张：
$$
\boxed{
\mathcal F=K(E_0[5],\zeta_{168})
          =\mathbf Q(E_0[5],\zeta_{168}).
}
\tag{8}
$$
对在 $\mathcal F/\mathbf Q$ 完全分裂的所有足够大素数，
R358、R368 及 (7) 同时适用：
R362 的全部六个相位碰撞管，在每个深度都有单位质量。
这给同一个原目标 $S$ 的共同无限素数族，不更换曲线。

## 2. 原两输入的完整联合，含半特征和部分输出

在原第一个、第二个 sigma 输入上取
$$
Y_{12}=X_1+2X_2,\qquad Q_{12}=-2X_1+X_2.
\tag{9}
$$
坐标矩阵行列式是五。因此对当前每个 $p>7$，
$$
(X_1,X_2)\in(p^n\mathbf Z_p)^2
\Longleftrightarrow
(Y_{12},Q_{12})\in(p^n\mathbf Z_p)^2.
\tag{10}
$$

其同一原生成函数为
$$
F(z,t)=\sigma(z-2t)\sigma(2z+t).
\tag{11}
$$
两个变量的 degree 均为五，交叉 Gaussian 为
$1\cdot(-2)+2\cdot1=0$，恰好消掉。
原 sigma 半特征也逐变量吻合：
沿 $z$ 平移 $\lambda$，乘积特征是
$\chi(\lambda)\chi(2\lambda)=\chi(\lambda)$；
沿 $t$ 平移同样是 $\chi(-2\lambda)\chi(\lambda)=\chi(\lambda)$。
所以 (11) 真正在
$\mathcal S_5\boxtimes\mathcal S_5$，
$\mathcal S_5=\sigma^5L(5O)$，
没有隐含的平坦线丛更换。

标准五维基和型为
$$
\begin{array}{c|ccccc}
f&1&x&x^2&y&xy\\ \hline
G=\sigma^5f\text{ 的型 }k&5&3&1&2&0 .
\end{array}
\tag{12}
$$
又
$$F(\xi z,\xi t)=\xi^2F(z,t)\qquad(\xi\in\mu_6).$$
只将辅助 $t$ 作 $\mu_6$ 平均后，$z$ 型为二，故仅剩 (2) 的一条线。
相应辅助为 degree 五、型零、质量一，所以准确是 (1)。
因此
$$
\boxed{
\frac16\sum_{\xi\in\mu_6}F(z,\xi t)=F_{12}(z)D_5(t).
}
\tag{13}
$$

设 $\mathsf P_Q$ 表示只在辅助坐标作该平均。
由原 Amice 变换的唯一性，(13) 是完整原测度身份
$$
\boxed{
\mathsf P_Q(Y_{12},Q_{12})_*\nu^{\otimes2}
=\nu_{F_{12}}\otimes\nu_{D_5}.
}
\tag{14}
$$
它不是若干低矩的比较，也不是将加法 Mellin 写成乘法 Mellin。

特别可以与任何独立的 $X_3,X_4,X_5,X_6$ 条件一起使用。
但 (10) 的原两输入同深度条件仍有 $Y_{12}$ 条件；
不能只取辅助 $Q_{12}$ 的质量来代替整个原叶域。

## 3. 原共同 p 限制确定两个实际标量

原 sigma core 是
$$\nu|_p=\lambda_\sigma[\kappa]_*\nu,\qquad
\lambda_\sigma=\varepsilon^3/\bar\pi.$$
在 (14) 中限制 $Y_{12},Q_{12}$ 全部在 $p$。
由 (10)，这恰是两个原输入全部在 $p$，所以
$$
(\nu_{F_{12}}|_p)\otimes(\nu_{D_5}|_p)
=\lambda_\sigma^2[\kappa]_*\nu_{F_{12}}
                      \otimes[\kappa]_*\nu_{D_5}.
\tag{15}
$$
两右因子非零：$D_5$ 质量一，$F_{12}$ 的二阶矩为
$4\Omega_p^2\in\mathcal O^\times$。
纯张量唯一性于是给两个实际非零标量 $\lambda_{12},\lambda_5$，
分别满足 (4) 左列及 (5)。

还需核它们确为单位。由 $D_5$ 质量一，
$$\lambda_5=\nu_{D_5}(p\mathbf Z_p)\in\mathcal O.$$
对 $F_{12}$ 的第二矩，左侧 $\int_{p\mathbf Z_p}x^2d\nu_{F_{12}}$
属于 $p^2\mathcal O$，
右侧是 $\lambda_{12}\kappa^2\,4\Omega_p^2$。
因为 $\kappa^2\in p^2\mathcal O^\times$，故 $\lambda_{12}\in\mathcal O$。
(5) 的乘积是单位，遂使两个标量都是单位。
这里没有把具有非零质量的尾删掉，也没有除以未知中央值。

## 4. 原 order-five 中心与真实 torus 作用

先在 $E_0$ 上计算。使用 R368 相同的奇 degree 原迹，只把幂改为五：
$$
\mathscr M_a(\sigma^5f)=\sigma^5
\operatorname{Tr}_{[a]}
\left[\left(\frac{r_{\bar a}}{r_a}\right)^5f\circ[\bar a]\right],
\qquad
T_{p,0}=\pi_0^{-1}\mathscr M_{\pi_0}.
\tag{16}
$$
奇半特征、完整正式群平均及交织方向与 R368 第2、4节相同；
原 division 函数和未归一 trace 均不改换。

order-five 的中心也可直接支付。
设 $\mathsf JG(z)=G(-z)$，任一 $T\in E[5]$ 的 lift 满足
$$A_T^5=a,\qquad \mathsf JA_T\mathsf J=bA_T^{-1},\qquad b^5=a^2.$$
乘以 $b^2/a$，准确得到 order five 且满足
$\mathsf JU_T\mathsf J=U_T^{-1}$ 的 lift。
若两个 lift 都满足这两条件，其比值同时满足 $\zeta^5=\zeta^2=1$，
所以相同。
故这里也不是只使用项目 Heisenberg 表示。

五维 Heisenberg 表示由 primitive 五次交换子给出不可约性。
原几何交织把参数送至 $(\pi_0/\bar\pi_0)T$。
(16) 与 $\mathsf J$ 交换；与 R368 一样，中心标量同时有五次幂一和平方一，
故准确为一。
因 $\mathcal O_K/5=\mathbf F_{25}$，共轭是五次幂，
norm-one 群阶六；原 $\mu_6$ 六个元素模五互异，所以它们给全群。
这证明 (3)。

$\mathsf I_vG(z)=G(vz)$ 的交织参数为 $v^{-1}T$。
(15) 已独立保证 (16) 非零。
Schur 引理给一个实际标量 $c_p\ne0$：
$$
\boxed{
T_{p,0}=c_p\,\mathsf I_{u_5^{-1}}
\quad\hbox{于整个 }\mathcal S_5.
}
\tag{17}
$$
此处没有同 degree 的 norm-five 一变量 sigma 锚，
故不从 (17) 擅自声称 $c_p=u_5$。

由 (12)，$D_5$ 型零、$F_{12}$ 型二。
所以在 $E_0$ 原规范下
$$
\lambda_{5,0}=c_p/\bar\pi_0,\qquad
\lambda_{12,0}=c_pu_5^{-2}/\bar\pi_0.
$$
将第3节已经独立支付的实际乘积
$\lambda_{12,0}\lambda_{5,0}=\bar\pi_0^{-2}$ 代入，得到
$$
\boxed{c_p^2=u_5^2,\qquad
c_p=\eta_{5,p}u_5,\quad\eta_{5,p}\in\{\pm1\}.}
\tag{18}
$$
若需要一个不依赖符号选择的定义，它正是
$$
\eta_{5,p}
=u_5^{-1}(T_{p,0}D_5)(0)
=(\pi_0u_5)^{-1}(\mathscr M_{\pi_0}D_5)(0).
\tag{19}
$$
因此 (18) 是对同一原标量的约束，没有在不同权或不同域上选择平方根。

## 5. 传回原 $E_{17}$ 的全周期与所有 tame

$D_{5,b}(z)=D_{5,0}(\theta z)$，
而 $F_{12,b}(z)=\theta^{-2}F_{12,0}(\theta z)$，
其中 $\theta=17^{1/6}$。
同 R316 的 $\Omega_{p,0}=\theta\Omega_p$ 使这些是同一
$\mathbf Z_p$ 变量上的测度比较，而非任意变量的代数缩放。

原 $p$ 层缩放从 $p/\bar\pi_0^2$ 变成 $\varepsilon^2\kappa$。
型零的 $D_5$ 对此无额外相位；型二的 $F_{12}$ 则有
$[\varepsilon^2]_*\nu_{F_{12}}=\varepsilon^4\nu_{F_{12}}$。
将 (18) 传回，正是 (4)，其乘积为 (5)。
这支付全部 tame 分支，不以 principal 质量代替整条来源。

## 6. 未定符号下仍一致成立的单位界

现在只假定 $u_5=\pm1$。令
$$e_p=\eta_{5,p}u_5\in\{\pm1\}.$$
则
$$\lambda_5=e_p/\bar\pi_0,\qquad
\lambda_5-\lambda_\Xi
=\frac{e_p\bar\pi_0-\chi_2(p)}{\bar\pi_0^2}.
\tag{20}
$$
设 $A_0=\pi_0+\bar\pi_0\in\mathbf Z$。
由于 $\pi_0\equiv1\bmod2$，
$$A_0\equiv0\bmod2,\qquad |A_0|\le2\sqrt p.$$
若 (20) 的差非单位，因为 $\pi_0$ 在所选普通位为零模 $p$，
就有
$$e_pA_0\equiv\chi_2(p)\pmod p.$$
对 $p>7$，整数界 $2\sqrt p<p-1$ 迫
$e_pA_0=\chi_2(p)=\pm1$，与偶性矛盾。

若 $1-\lambda_5$ 非单位，同样有 $A_0\equiv e_p\bmod p$，
继而 $A_0=e_p$，仍与偶性矛盾。这证明 (7)。
两个符号由同一个论证处理，未假设它们如何随 $p$ 分布。

## 7. 一个固定有限扩张同时支付所有素数条件

$E_0$ 定义在 $\mathbf Q$ 上，所以完整五分点域
$\mathbf Q(E_0[5])/\mathbf Q$ 有限 Galois。
$\mathbf Q(\zeta_{168})$ 也有限 Galois，且包含
$K=\mathbf Q(\zeta_3)$。
因此 (8) 是一个具体、固定、有限 Galois 扩张，未随 $p$ 变化。

令 $\mathcal P_*$ 为在 (8) 中完全分裂、并去掉有限个坏素数的素数集。
Chebotarev 密度定理应用于恒等共轭类，给
$$\operatorname{dens}(\mathcal P_*)=1/[\mathcal F:\mathbf Q]>0.\tag{21}$$
这里仅需其无穷性。逐一核对所需条件：

1. 完全分裂于 $\mathbf Q(\zeta_{168})$ 给
   $p\equiv1\bmod168$。因此 $p\equiv1\bmod3$，
   对原好约化 $j=0$ 曲线为普通；又 $\chi_2(p)=1$、$(p/7)=1$，
   所以 R368 的 $(-14/p)=1$ 条件成立。

2. 完全分裂于 $\mathbf Q(E_0[5])$ 使实际算术 Frobenius
   在整个 $E_0[5]$ 上为恒等。在分裂普通位，它是原
   $[\pi_0]$ 的作用。五在 $K$ 中惰性，
   $E_0[5]$ 是 $\mathcal O_K/5=\mathbf F_{25}$ 上的一维空间：
   $\omega$ 的二次最小多项式在模五不可约，而该群有二十五个元素。
   因而此作用忠实，严格得到
   $$\pi_0\equiv1\bmod5,\qquad\bar\pi_0\equiv1\bmod5,\qquad
   \boxed{u_5=1.}\tag{22}$$
   完全分裂在这里给的是一，不能只写成未指明的 $\pm1$。

(22) 使用实际 Frobenius 与好约化的 prime-to-$p$ 挠点比较；
没有在 CM 生成元上再乘一个自由单位。
因此第6节和 R368 同时适用于每个 $p\in\mathcal P_*$。
没有要求有限扩张之间额外不交；直接取其固定合成域的恒等类即可。

## 8. 同一个原 $S$ 的六条完整碰撞管全部无损

记 R362 的六条原管为
$$
\mathcal H_{\zeta,N}
=\{L,M\in\mathbf Z_p^\times,\ L-\zeta M\in p^N\},
\qquad \zeta\in\mu_6,\quad N\ge1.
$$
在 $\mathcal P_*$ 上，所有来源仍是同一个原辅助 $\Xi_\Delta$ 的真投影。
其完整质量为
$$
\boxed{
\begin{array}{c|c}
\zeta&q_{\zeta,N}\\ \hline
1&(1-\lambda_K)\lambda_D^N\\
-1&(1-\lambda_D)\lambda_K^N\\
\omega,\omega^2&
(\lambda_7-\lambda_\Xi)\lambda_7^{N-1}\\
-\omega,-\omega^2&
(\lambda_5-\lambda_\Xi)\lambda_5^{N-1}.
\end{array}}
\tag{23}
$$
第一、二行由 R358 对全部普通素数是单位；
第三行由 R368 和第7节是单位；
第四行由 (7)、(22) 是单位。
所有 $\lambda$ 本身都是单位，故结论对全部 $N\ge1$ 同时成立。

在共同族上 $\chi_2(p)=1$、$u_5=1$，
(18) 又给 $\lambda_5^2=\bar\pi_0^{-2}=\lambda_\Xi$。
所以最后一行还可准确简化为
$$\boxed{q_{-\omega,N}=q_{-\omega^2,N}
=(1-\lambda_5)\lambda_5^N.}\tag{24}$$
这条简化不要求知道 $\eta_{5,p}$。

D5 两相位的双深度及原三／五输入 primitive carry 完整为
$$
\boxed{
e_{\zeta;a,N}=\lambda_\Xi^a\lambda_5^{N-a},\qquad
e_{\zeta;a,N}^{\rm prim,j}
=(\lambda_\Xi-t_p^j)\lambda_\Xi^{a-1}\lambda_5^{N-a},
\quad j=3,5.
}
\tag{25}
$$
其中 $N\ge a\ge1$、$t_p=\varepsilon^3p/\bar\pi^3$。
$v_p(t_p)=1$ 使最后的差为单位；原非单位输出边界没有删除。

由 R362 的完整联合，对同一原输出、任一 tame $\ell$、任一权参数 $v$，
$$
\boxed{
J_{\mathcal H_{\zeta,N};\ell}(v)
=q_{\zeta,N}J_{S,\ell}(v),\qquad
J'_{\mathcal H_{\zeta,N};\ell}(0)
=q_{\zeta,N}J'_{S,\ell}(0).
}
\tag{26}
$$
所有 $q_{\zeta,N}$ 在同一个 $\mathcal P_*$ 上都是单位。
没有改变原 $Y$ 的尺度，故此处不引入额外参考斜率。

如要归一 $D_5$ 自身的第 $n$ 个环带，仍须保留
$$
M_{5,\ell}^{[n]}(v)
=\lambda_5^n\omega_p(\bar\pi)^{-2n\ell}
 \langle\bar\pi\rangle^{-2n(p-1)v}M_{5,\ell}(v)
$$
以及导数中的
$-2n(p-1)\log_p(\bar\pi)M_{5,\ell}(0)$。
原 principal 质量 $1-\lambda_5$ 在本族是单位，并非零；
有限层重构的剩余项
$\lambda_5^M[\kappa^M]_*\nu_{D_5}$ 也仍有单位质量。

(26) 的辅助条件不是原独立叶深度的全部条件。
R362 的六分支还带实际 $Y_A-\xi\delta L\in p^N$，
且 unit 平移小球的四个真实来源全部存在。
本结果只把六个管的返回系数在一个固定无限族上同时变成无损；
它没有把这些部分输出条件、五个非原叶分支或其补域相消掉。

## 9. 依赖与记录

- [R316：原 sigma 整测度与完整 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R358：两原相位的绝对 core 与单位管](R358-original-collision-reference-absolute-cores-and-unit-tubes.md)。
- [R362：实际 $\Xi_\Delta$、原管及叶域补项](R362-original-triple-pair-core-and-six-branch-leaf-domain.md)。
- [R368：order-seven 真锚、degree 七绝对 core 及固定族单位](R368-original-degree-seven-absolute-core-and-fixed-prime-unit-tubes.md)。
  本文第4节独立写出 order-five 的归一与中心消去，
  第2节重新支付所用的原 two-input joint。

证明使用固定有限 Heisenberg 群、真实 theta 联合及整数范数界，
没有新增目标素数扫描。本文经 GitHub Contents API 保存小文本，
没有声称执行本地 git pull。提交前两 README 的内容 blob 仍为
f787a306d90892d8dec765dc59747d60ba39f055、
f8dd8071ac0c2b31f344a40c15ac2a42796bf9af，
与已读基准 35e391cd9a73d5a514d252312d3ff61962ddbc70 相同。
