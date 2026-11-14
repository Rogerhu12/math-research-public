# R396：非平凡四次 ray 上的原三 core、同输出域运输与完整尺度边界

日期：2026-11-14。**状态：已证明。** 本篇选择一个明确固定的无穷普通素数类。
在同一个原三输入联合中，输出 $Y$ 的 core 为 $-\lambda_0$，
两个正交辅助方向的 core 都为 $\lambda_0J$，其中 $J^2=-1$。
这些是保持其余坐标的完整测度恒等式。它们给相同原输出的真实域运输，
并给一个已知质量乘 $\log_p\bar\pi$ 的非齐次尺度边界。
奇数步返回实际质量一伴随，偶数步才返回原 $S$；二者不混同。

此外，R384 的原六条第二中心来源在偶深度恢复同一标量，
所以原来的六列插值与全部432球双返回可进入这个非平凡四次类，
无须扩成更大的参考空间。所有单位补域继续保留；本篇没有证明主目标。

## 1. 一个真实固定 ray 与全部原相位

沿用
$$
K=\mathbf Q(\omega),\quad\delta=1+2\omega,\quad
\omega^2+\omega+1=0,\quad b=17.
$$
设 $\psi_0$ 为 $y^2=x^3+1$ 的原 CM 角色，
$\pi_0=\psi_0(\mathfrak p)$ 取 $\pi_0\equiv1\pmod{2\delta}$ 的 primary 生成元。
考虑明确的固定类
$$
\boxed{
\pi_0\equiv a_*:=2143+2178\omega
                  \pmod{4896\mathcal O_K},\qquad4896=32\cdot9\cdot17.
}
\tag{1}
$$
它等价于
$$
\pi_0\equiv-1+2\omega\pmod{32},\qquad
\pi_0\equiv1\pmod9,\qquad
\pi_0\equiv\delta\pmod{17}.
\tag{2}
$$
$Na_*=4668679$ 与模数互素，并且 (1) 已兼容 primary 条件。
由固定 ray class 的素理想分布，(1) 有正密度的 degree-one 素理想；
有限删除后仍无穷。以下取其底下的有理普通 $p>17$，并在该 $\mathfrak p$
使用原普通嵌入，不把不同 $p$ 类的公式混用。

完整 ratio 为
$$
\boxed{
g=\pi_0/\bar\pi_0:
\quad g\equiv27+8\omega\pmod{32},\quad
g\equiv-1\pmod{68},\quad
g\equiv19=1+18\pmod{36}.
}
\tag{3}
$$
所以 R387 的四次特征准确是 $\rho(\mathfrak p)=\iota$。
目标的十七处原 idèle unit character 为 $z^{48}$。
由 (2)，
$$
\delta^{48}=(-3)^{24}\equiv-1\pmod{17};
$$
其余扭曲的坏点单位因子不变，故原 principal-ideal 关系给
$$
\boxed{\pi:=\psi_{17}(\mathfrak p)=-\pi_0,\qquad\varepsilon=-1.}
\tag{4}
$$
这也可由 R290 的已付六次剩余规范读取；不是从一个裸 ratio 猜测符号。

记
$$
\kappa=p/\bar\pi^2=p/\bar\pi_0^2,\qquad
\lambda_0=1/\bar\pi_0=-1/\bar\pi,\qquad
\lambda_Y=-\lambda_0.
\tag{5}
$$
所有缩放保持原 period，$v_p(\kappa)=1$，而 $\lambda_0$ 为单位。

## 2. 原中心 lift 的一个确切恒等式

对偶数 $N$，记 $\mathcal S_N=\sigma^NL(NO)$，
使用 R300 的实际对称 lift
$$
(\mathsf T_vG)(z)=e^{-N\eta_v(z+v/2)}G(z+v).
$$
原 quasi-periodicity 对 $\ell\in\Gamma$ 给
$$
\mathsf T_{v+\ell}=
\exp\!\left(\frac N2(\eta_\ell v-\eta_v\ell)\right)\mathsf T_v .
\tag{6}
$$
sigma 的 semicharacter 因 $N$ 偶而恰为一。
若 $\ell=Nv\in\Gamma$，则 $\eta_\ell=N\eta_v$，所以
$$
\boxed{\mathsf T_{(1+N)v}=\mathsf T_v.}
\tag{7}
$$
这是包含中心的原恒等式，而不是只把参数模 $N$ 截掉。

因此 ratio $1+N\bmod2N$ 在整个原 Heisenberg 表示上交织恒等。
其绝对标量仍须用同 degree 的真实锚确定。

在 $\mathcal S_{18}$，(3) 的 ratio 为 $19=1+18$；
使用原 $\Theta(3z)$ 锚，其已付 $T_{p,0}$ 标量为一。
由 primitive 十八次 Heisenberg 交换子与不可约性，
$$
\boxed{T_{p,0}|_{\mathcal S_{18}}=1.}
\tag{8}
$$
特别原 $C_{18}$ 有完整 scalar core。
这里没有要求三处 ratio 为不可能的 $-1$：真正使用的是 (3) 的 $19$。

原
$$
A=\sigma(z)\sigma(2z)\sigma(\delta z)
   =-2\delta\,\sigma^8xy
\tag{9}
$$
在 $\mathcal S_8$ 的 type3 块中恰占唯一一维。
其绝对符号也已固定，而不只知道平方为一：
对 $\gamma=3+\omega$，R387 的同一原 division 以及完整 $y$ 比给
$$
\mathscr M_\gamma A=(-1+2\omega)A=\varpi_7 A.
\tag{10}
$$
具体在目标横坐标二、三的完整七次纤维，计算
$(r_{\bar\gamma}/r_\gamma)^8\,
[y(\bar\gamma P)/y(\gamma P)]\,x(\bar\gamma P)$，
除以目标 $x$ 后两次都准确为 $\varpi_7$。
因为该 type3 块只有一维，(10) 是整个来源的恒等式。
同 degree 的 $\Theta(2z)$ 锚与 (2) 的 ratio 因而给本 ray 上
$T_{p,0}A=A$。

R316 的真实 homothety
$\Omega_{p,0}=17^{1/6}\Omega_p$ 保留所有 period。
$A$ 的 type3 和 $C_{18}$ 的 type0 都使
$[\varepsilon^2]_*$ 为一；由 (8)、(10)，
$$
\boxed{
\nu_A|_{p\mathbf Z_p}=\lambda_0[\kappa]_*\nu_A,\qquad
\nu_{C_{18}}|_{p\mathbf Z_p}=\lambda_0[\kappa]_*\nu_{C_{18}}.
}
\tag{11}
$$
这里没有将三因子 Mellin 拆成乘法。

## 3. 同一原三输入与正交 frame

保留 R379 的实际来源
$$
C=C_{18}
=\sigma^{18}(X-8b)
 \left(X^2-\frac{4bX}{7}+\frac{16b^2}{7}\right),\qquad X=x^3,
$$
$$
D=\sigma^{16}x^2(X+b),\quad
H=\sigma^{16}x^2(X^2+20bX-8b^2),\quad
S=DC=-A^2C/12 .
\tag{12}
$$
置 $H_C=HC$。它仍是这一篇原来源的实际乘积，质量为一；
没有把它认成另一条有理椭圆曲线。

对原三测度
$$
-\frac1{12}\nu_A(a)\nu_A(b_1)\nu_C(c)
$$
使用整数坐标
$$
Y=a+b_1+c,\qquad Q=a-b_1,\qquad
R=9(a+b_1)-8c.
\tag{13}
$$
矩阵行列式准确为三十四。原 degree 权为 $(8,8,18)$，故
$$
L\,\operatorname{diag}(8,8,18)L^t
 =\operatorname{diag}(34,16,2448).
\tag{14}
$$
等价地，完整 theta transform 是
$$
-\frac1{12}A(z+u+9v)A(z-u+9v)C(z-8v).
\tag{15}
$$
(14) 支付所有交叉 Gaussian：每个坐标系数都在它自己的原零特征
$\mathcal S_{34},\mathcal S_{16},\mathcal S_{2448}$，没有暗换平移截面或 period。

记原联合为 $\mathcal J$，并令
$$
\mu=\mathcal P_Q\mathcal P_R\mathcal J
$$
为两个辅助变量各自的 $\mu_6$ 平均。
这些平均与原点深域、单位域及全体共同 $\kappa$ 缩放交换。
整个 (15) 的总 $\mu_6$ 型为零；因此平均后每个 $Y$ 系数也恰为 type0。

沿用 R387 的准确矩阵
$$
JD=aH,\qquad JH=d_1D,\qquad
a=\frac{\delta}{72b},\quad d_1=24b\delta,\quad ad_1=-1.
\tag{16}
$$
记 $J_Q$ 为只作用于 $Q$ 原两列的这个算子。
R381/R387 已付的完整联合给
$$
\boxed{\mu=\eta_D\otimes\nu_H-\eta_H\otimes\nu_D,}
\tag{17}
$$
其中
$$
\eta_G=\mathcal P_R
  (u+c,\ 9u-8c)_*(\nu_G\otimes\nu_C),\qquad G=D,H.
$$
(17) 保任意 $(Y,R)$ 测试，且 $J_Q^2=-1$。
积分两个辅助变量后，$\mu$ 的原 $Y$ 边际仍是 $\nu_S$。

## 4. 三个保持其余坐标的完整 core

首先，(3) 的 $Y$ ratio 为 $-1\bmod68$。
在整个 $\mathcal S_{34}$ 上，原交织可用 $G(z)\mapsto G(-z)$ 实现；
其 type0 子块上这个算子为一。

绝对标量用 R300 已付的**原目标全测度**锚定：
$S$ 的实际 core 为 $1/\bar\pi=\lambda_Y$，
而以 $\pi_0$ 归一的值是 $\psi_{17}/\psi_0=-1$。
$S$ 是非零截面，首项为 $z^6$；此处只使用已经证明的完整 core，
不使用待证的 $M'_S(0)$。于是整个 type0 块的标量为负一，故
$$
\boxed{\mu|_{Y\in p\mathbf Z_p}
 =-\lambda_0[\kappa_Y]_*\mu.}
\tag{18}
$$
这保持任意 $(Q,R)$ 测试，不只是原 $Y$ 边际。

由 R387 的全部四次相位及本 ray 的 $\rho=\iota$，
$$
\boxed{\mu|_{Q\in p\mathbf Z_p}
 =\lambda_0[\kappa_Q]_*J_Q\mu.}
\tag{19}
$$
同样保持任意 $(Y,R)$ 测试。

原全三输入均在 $p\mathbf Z_p$ 时，(11) 给因子 $\lambda_0^3$。
因 (13) 是 $p$-整可逆坐标，故
$$
\mu|_{Y,Q,R\in p\mathbf Z_p}
 =\lambda_0^3[\kappa_Y,\kappa_Q,\kappa_R]_*\mu.
\tag{20}
$$
另一方面，先应用 (18)、(19)，得到
$$
-\lambda_0^2[\kappa_Y,\kappa_Q]_*
 J_Q(\mu|_{R\in p\mathbf Z_p}).
$$
缩放推前是单射，且 $J_Q^{-1}=-J_Q$，所以
$$
\boxed{\mu|_{R\in p\mathbf Z_p}
 =\lambda_0[\kappa_R]_*J_Q\mu.}
\tag{21}
$$
这是真正第三个完整 core，不需要认定整个
$\mathcal S_{2448}$ 都有某个猜测标量。

比较 (17) 中两个独立的 $Q$ 列，还得到
$$
\boxed{
\eta_D|_{R\in p}=-\lambda_0a[\kappa_R]_*\eta_H,\qquad
\eta_H|_{R\in p}=-\lambda_0d_1[\kappa_R]_*\eta_D.
}
\tag{22}
$$
两个负号以及 $ad_1=-1$ 都来自同一原联合。
特别
$$
\boxed{\eta_D|_{R\in p^2}
 =-\lambda_0^2[\kappa_R^2]_*\eta_D.}
\tag{23}
$$

## 5. 双深度、单位补域与奇偶输出

(19)、(21) 的所有迭代均合法；$R$ 限制与 $J_Q$ 交换，
而 $D,H$ 自己的完整 core 支付 $Q$ 方向的每次迭代。
因此对 $n,m\ge0$，
$$
\boxed{
\mu|_{Q\in p^n,R\in p^m}
=\lambda_0^{n+m}
 [\kappa_Q^n,\kappa_R^m]_*J_Q^{n+m}\mu .
}
\tag{24}
$$
它没有额外限制 $Y$，因而保原输出的全部 tame。

记 $L=n+m$。积分两个辅助变量，(17) 给
$$
\boxed{
Y_*(\mu|_{Q\in p^n,R\in p^m})
=\begin{cases}
(-1)^{L/2}\lambda_0^L\nu_S,&L\text{ 偶},\\
(-1)^{(L+1)/2}a\lambda_0^L\nu_{H_C},&L\text{ 奇}.
\end{cases}}
\tag{25}
$$
原 $H_C(0)=1$，且 (18) 同样作用于它，故
$$
\nu_{H_C}|_p=-\lambda_0[\kappa]_*\nu_{H_C},\qquad
\nu_{H_C}(\mathbf Z_p^\times)=1+\lambda_0.
\tag{26}
$$
$1+\lambda_0$ 为单位。事实上 $1\pm\lambda_0$ 均为单位：
非单位会由 Hasse 界迫 $E_0$ 的偶数 trace 等于 $\pm1$。
这同 R358 的原两挠单位证明一致，不使用 $H_C$ 的未知斜率。

全部单位补域由有限 inclusion-exclusion 读取，不能直接删去。
例如
$$
\boxed{
Y_*(\mu|_{Q,R\in\mathbf Z_p^\times})
=(1-\lambda_0^2)\nu_S+2a\lambda_0\nu_{H_C}.
}
\tag{27}
$$
对 $Y$ 再限单位，右边第二项的质量为
$2a\lambda_0(1+\lambda_0)$，是单位。
因此原 $M'_S(0)=0$ 并不把这个辅助双单位域赋成零。
(25) 的偶数行才是单独的原目标返回。

## 6. 真正相同输出的域运输及所有 tame 因子

从 (19)、(21) 可消去同一个 $\lambda_0J_Q$，得到全测度恒等式
$$
\boxed{
T_*(\mu|_{Q\in p\mathbf Z_p})
 =\mu|_{R\in p\mathbf Z_p},\qquad
T(Y,Q,R)=(Y,Q/\kappa,\kappa R).
}
\tag{28}
$$
原输出 $Y$ 完全不变。特别，对 $n\ge1,m\ge0$，
$$
\boxed{
T_*(\mu|_{v_p(Q)=n,\ v_p(R)=m})
 =\mu|_{v_p(Q)=n-1,\ v_p(R)=m+1}.
}
\tag{29}
$$
所以所有单位边界也在原域中被准确运送；没有先作源平均后猜测交域。

若两个辅助环带使用原归一变量
$$q=Q/p^n,\qquad r=R/p^m,$$
则运输后
$$
q'=\bar\pi^2q,\qquad r'=\bar\pi^{-2}r.
\tag{30}
$$
因此保 $Y$ 的任意测试时，辅助 tame $\ell_Q,\ell_R$ 与权
$u_Q,u_R$ 的完整因子为
$$
\boxed{
\omega_p(\bar\pi)^{2(\ell_Q-\ell_R)}
 \langle\bar\pi\rangle^{2d(u_Q-u_R)},\qquad d=p-1.
}
\tag{31}
$$
对原 $Y$ 中央变量求导没有新增项；
对辅助变量求导则分别出现
$+2d\log_p\bar\pi$、$-2d\log_p\bar\pi$ 乘原质量。
这些是不同的真实导数，不可把后者改称 $M'_S(0)$。

例如 $Y$ 为单位、$v_p(Q)=1,v_p(R)=0$ 的总质量为
$$
\boxed{-a\lambda_0(1-\lambda_0^2)(1+\lambda_0)\in\mathcal O^\times.}
\tag{32}
$$
它由
$\lambda_0J_Q(1-\lambda_0J_Q)^2$
以及 (17) 直接展开。
(29) 把它送到 $v_p(Q)=0,v_p(R)=1$ 的相同质量。
(31) 因而在这两个实际环带上给明确非零的辅助尺度边界，
而没有遗漏哪一边的单位域。

## 7. 原输出尺度上的非齐次行及其准确归属

还可在原 $Y$ 变量中写一个完整的非齐次行。
令 $B_0(u)$ 为限制
$Q\in p\mathbf Z_p,\ Y\in\mathbf Z_p^\times$、积分全部 $R$
后的 principal $Y$-Mellin。
令 $B_1(u)$ 取相同 $Q$ 域、$Y\in p\mathbf Z_p^\times$，
但用 $Y/p$ 作为原环带变量。
由 (18)、(25)，
$$
B_0(u)=-a\lambda_0 M_{H_C,0}(u),\qquad
B_0(0)=-a\lambda_0(1+\lambda_0),
$$
$$
B_1(u)=-\lambda_0
 \langle\bar\pi\rangle^{-2du}B_0(u).
\tag{33}
$$
因此
$$
\boxed{
(-\lambda_0)^{-1}B_1'(0)-B_0'(0)
=2d\,a\lambda_0(1+\lambda_0)\log_p\bar\pi\ne0.
}
\tag{34}
$$
$\bar\pi$ 是本地单位；若其对数为零，它在该有限局部域中必须为根单位，
与其代数范数 $p$ 矛盾。其他因子均已证单位。
没有把未知 $M'_{H_C}(0)$ 当已知值；它在这个确切的两尺度差中相消。

这个已知项有清楚的全辅助归属。
令 $\tau=(Q,R)_*\mu$ 为积分全部 $Y$ 后的原辅助测度。
将第一归一 $Y$ 环带导数除以 $-\lambda_0$，再减单位 $Y$ 导数，
所得辅助值测度准确为
$$
\boxed{-2d(1+\lambda_0)\log_p\bar\pi\ \tau.}
\tag{35}
$$
再积分 $R$，因为由 (17)
$$Q_*\tau=-\nu_D,$$
(35) 准确变成
$$
\boxed{2d(1+\lambda_0)\log_p\bar\pi\ \nu_D.}
\tag{36}
$$
它的总质量是零，故未加辅助限制的原目标行没有这个非齐次项。
读 $Q\in p$ 才得到 (34)；读 $Q\in p^2$ 又准确为零，
因为 $\nu_D(p^2)=-\lambda_0^2D(0)=0$。
这说明已知对数项位于真实奇数状态，不能在回到原 $S$ 的偶数状态时保留一个本应消失的常数。

## 8. 原六列第二中心在偶深度的直接恢复

本节只使用 R384 已有的六个来源，不增添新的参考列。
在原 $Y$ type0 基
$$F_i=\sigma^{34}x^{2+3i},\quad0\le i\le5,$$
R384 已付
$$
\eta_D=\sum_{i=0}^5\nu_{F_i}\otimes\nu_{\Gamma_i}.
\tag{37}
$$
每个 $\Gamma_i$ 都是它自己的原 degree2448 来源；
$\Gamma_i(0)$ 是原 $S$ 的目标向量。
由 (23) 与 $F_i$ 的独立性，
$$
\boxed{
\nu_{\Gamma_i}|_{p^2}
 =-\lambda_0^2[\kappa^2]_*\nu_{\Gamma_i},
\qquad
\nu_{\Gamma_i}|_{p^{2n}}
 =(-1)^n\lambda_0^{2n}[\kappa^{2n}]_*\nu_{\Gamma_i}.
}
\tag{38}
$$
这不是声称一次 $p$-core 为标量，也不是把整个
$\mathcal S_{2448}$ 当成一条来源。

R376 的原 prime-power theta-group 证明可直接取
$a=\pi^{2n},b=\bar\pi^{2n}$；它只需该层的实际 scalar trace。
所以在偶深度 $N=2n$，同一球矩阵的每列都有共同因子
$(-1)^n\lambda_0^N$ 与原 integral frame 因子，标签、Gaussian 和来源均不变。
R384 的六来源行列式因此原样适用。

准确地，保留该篇原中心
$$1,\ 2,\ 3,\ 4,\ 5,\ 9,$$
排除其固定 leading determinant 和 Vandermonde 的素因子，并取 $p>31$。
这只删除固定有限集合。(1) 的无穷族仍无穷。
degree332928 的原 determinant section 给每个
$$\boxed{N\ge332930,\qquad N\text{ 偶}}\tag{39}$$
上的同层球矩阵整可逆。

第一中心权由 R387 已对全部普通 $p>17$ 支付。
故 R384 的原六列逆权 $V_N$ 与十二球权 $W_N$ 满足同一个完整式
$$
\boxed{
Y_*\left(
1_{Y\in\mathbf Z_p^\times}
W_N(Q;Y)V_N(R;Y)\,\mathcal J
\right)=\nu_S^\times.
}
\tag{40}
$$
其支撑仍是
$$
Q\simeq\xi cY,\quad c=1,2,\quad\xi\in\mu_6;
\qquad
R\simeq\zeta a_jY,\quad a_j=1,2,3,4,5,9,\quad\zeta\in\mu_6.
$$
全部432球、可能为零的 cofactor 以及随 $Y\bmod p^N$ 变化的真实权都保留。
本节只把同一已付六列返回送进一个新的非平凡四次 ray，
没有把它等同单叶，也没有由 (34) 的奇数边界给 (40) 预赋非零。

## 9. 验证和后继的准确剩余条件

[check-jzero-nontrivial-quartic-ray-three-cores.js](../scripts/check-jzero-nontrivial-quartic-ray-three-cores.js)
给全部固定整数同余、原 A8 的两个完整七纤维、真正 Gram/行列式、
$J^2=-1$ 和第三 core 的符号，共十四项精确通过。
其中没有目标素数扫描。

本篇支付的是新的完整原域关系：
两个辅助深度可按 (28)–(31) 真运输；
奇数状态的已知质量在原输出归一尺度中给 (34)；
偶数状态以及偶深度双返回则准确回到原 $S$。
仍须控制 (40) 的全部单位补域，或者给一个把原中央零合法传到
(34) 那个奇数状态的同源恒等式。不能只因两个状态在有限矩阵中相连，
就把两者的中央导数同时置零。

终端不可用，本次依授权以 GitHub 集成提交小文本，不称为 git pull。
2026-11-14 02:12:19 UTC 读取 API main fdb7471bfe35579c35f1b29e8048157712ea9961；从上次 c7b31b2743b57ce65b8eb242e59dd50bca04eb74 比较，根 README 与本课题 README 均无变化，读号交根代理记入 HANDOFF。

### 引用

- [R290：原十七处角色与完整 local splitting](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)。
- [R300：全 theta Heisenberg 与原正式 trace](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)。
- [R316：原低次测度和真实周期](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R358：绝对 dyadic 锚与单位证明](R358-original-collision-reference-absolute-cores-and-unit-tubes.md)。
- [R376：原 prime-power 加法球及完整 frame](R376-original-additive-ball-theta-group-formula-and-integral-torsion-values.md)。
- [R379：原三输入与正交坐标](R379-original-third-joint-core-unit-collisions-and-three-input-return.md)。
- [R381：原反对称完整联合](R381-original-antisymmetric-joint-twelve-balls-and-complete-reference-elimination.md)。
- [R384：同一六列第二中心与全部双返回](R384-original-second-moving-center-integral-interpolation-and-double-return.md)。
- [R387：原四次双谱、完整 core 与十二球单位返回](R387-original-degree-sixteen-quartic-core-and-all-ordinary-moving-balls.md)。
