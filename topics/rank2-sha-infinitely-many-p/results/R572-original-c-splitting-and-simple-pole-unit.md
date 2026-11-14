# R572 — 原完整 C 分离、简单极点单位行与原算术 carry 的精确比较

日期：2026-11-14。**状态：已证明。**

本篇把原 $\mathcal P_C\rho_0$ 的整个六输入分成两个明确的
$C$ 来源，连同其余四个伴随的全部 theta 因子一起保留。
一个固定五次伴随多项式对任意完整双输入测试准确抽出 R562
的原 $\sigma\otimes B$，不用反卷积或新增投影。

在该同一个四单位域上，进一步给出一个只有简单极点、且当前
射线上恒为单位的积分。它是一个实际 log 比值导数加正一权，
不是把原负二矩预设非零。最后写出这个固定测试与原完整
$S/T$ 中央测试在同一来源上的共同支、三个 carry 补支和
carry 外余域。所有原 $p,\lambda,\kappa$ 系数及两个 Mellin
单位条件保留；没有由辅助单位行推出原中央非零。

## 1. 一个完整的原六输入框架

沿用
[R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)、
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R562](R562-original-four-unit-domain-and-negative-two-unit-relation.md)、
[R569](R569-original-five-sigma-convolution-unit-and-four-unit-bridge.md)
的原普通射线、全部坏集和规范：
$$
b=17,\quad \omega^2+\omega+1=0,\quad\delta=1+2\omega,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad\Omega=\Omega_p\in\mathcal O^\times.
\tag{1}
$$
当前 $p\ge71$、$p\equiv7\bmod64$，原整数迹为偶数。
本篇不增加射线或固定坏素数。

原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$，
$\rho_0=-\nu_\sigma^{\otimes6}/84$、
$\mu_0=\mathcal P_C\rho_0$。取完整物理框架
$$
\boxed{
v=\xi_1-\xi_3+x=\delta C,\quad
Z=\xi_1-\xi_3-2x,\quad Q=\xi_1+\xi_3,\quad
r=\xi_2,\quad d_0=d_0,
}
\tag{2}
$$
并保原 $c$。按 $(c,v,Z,Q,r,d_0)$ 排序，完整矩阵行列式为 $6$，
Gram 为
$$
\operatorname{diag}(1,3,6,2,1,1).
\tag{3}
$$
这是原输入格在当前处的整同构，未遗忘任何隐藏坐标。
纯 $C$ 旋转准确只把 $v$ 变为 $\omega v$，
逐个固定 $c,Z,Q,r,d_0$。

原观察在这个框架中的完整式是
$$
A_0=\frac{-2+\omega}{2}Z+\frac{4+3\omega}{2}Q+2\delta r,
$$
$$
\boxed{Y=A_0+c+2d_0,\qquad
       W=A_0+3\delta c+4d_0.}
\tag{4}
$$
原 carry 的实际行同样准确是
$$
\boxed{
F=\frac{\delta}{6}Z+\frac{1-2\omega}{2}Q+\omega^2r
       +c+(2+3\omega)d_0,\qquad C=v/\delta,
}
$$
$$
H_1=\frac{\omega^2}{2}Z+\frac{\omega-1}{2}Q+2r,\qquad
G=13H_1+(3-2\omega)F.
\tag{5}
$$
所以 $Y,W,F,H_1,G$ 全不含 $v$。
这不表示原 $q_n$ 不含 $v$：其中全部 $C$、$D_j$、$E_j$
和 carry 指示必须继续用 (5)。

## 2. 完整三 sigma 恒等式与两个 C 来源

记原实际 theta 函数
$$
\Sigma=\sigma^2,\quad\Theta=x_\wp\sigma^2,\quad
P_3=\sigma^3,\quad B_1=x_\wp\sigma^3,\quad B=-y_\wp\sigma^3,
$$
$$
h_0=x_\wp^3\sigma^6,\quad h_6=\sigma^6,\quad
\mathcal H_6=h_0-2bh_6,
$$
$$
f_1=-x_\wp y_\wp\sigma^6,\quad f_2=x_\wp^2\sigma^6,\quad
f_3=-y_\wp\sigma^6,\quad f_4=x_\wp\sigma^6 .
\tag{6}
$$
这里 $B$ 质量一，$P_3$ 质量零；二者都是原 odd degree3 的
实际来源。全 $\mu_6$ 型分别为 $0,3$。

**定理1（完整联合恒等式）。** 令
$$
\Psi(z,s,t)=\sigma(z+s+t)\sigma(z-s+t)\sigma(t-2z).
$$
它在整个
$\mathcal S_6\otimes\mathcal S_2\otimes
\mathcal S_3^{\rm odd}$ 中满足
$$
\boxed{
\begin{aligned}
\Psi={}&
B(t)\{2\Sigma(s)f_1(z)-2\Theta(s)f_3(z)\}\\
&+P_3(t)\{\Theta(s)\mathcal H_6(z)-6b\Sigma(s)f_4(z)\}\\
&-B_1(t)\{3\Theta(s)f_2(z)+
                    \Sigma(s)(h_0(z)+4bh_6(z))\}.
\end{aligned}}
\tag{7}
$$

**证明。** 三个行的 Gram 为 $(6,2,3)$，交叉项全为零；
前两轴为标准偶半特征，第三轴为标准奇半特征。
原 sigma 加法式给
$$
\Psi=\Theta(s)\mathscr A(z,t)-\Sigma(s)\mathscr B(z,t),
$$
$$
\mathscr A=\Sigma(z+t)\sigma(t-2z),\qquad
\mathscr B=\Theta(z+t)\sigma(t-2z).
$$
两者均在整个 $\mathcal S_6\otimes\mathcal S_3^{\rm odd}$，
总型分别为 $3,1$。
用 odd3 的完整基 $B,B_1,P_3$ 及 even6 的全部型空间，
$\mathscr A$ 的三个系数分别只能在
$\langle f_3\rangle,\langle f_2\rangle,\langle h_0,h_6\rangle$；
$\mathscr B$ 的三个系数只能在
$\langle f_1\rangle,\langle h_0,h_6\rangle,\langle f_4\rangle$。

在 $t=0$，用 $\sigma(2z)=-2y_\wp\sigma(z)^4$ 得
$\mathscr A=-2f_3$、$\mathscr B=-2f_1$。
一次 $t$ 导数中所有 $\sigma'$ 项准确消去，分别给
$-3f_2$、$(x_\wp^3+4b)\sigma^6$。
再用 $z=0$ 定 $\mathscr A$ 的 $h_0$ 系数为一。
最后在 $t=z$，利用
$$
\mathscr A(z,z)=-4(x_\wp^3+b)\sigma^9,\qquad
\mathscr B(z,z)=-x_\wp(x_\wp^3-8b)\sigma^9
$$
分别定剩余系数为 $-2b$ 和 $6b$。
因此准确有
$$
\mathscr A=\mathcal H_6P_3-3f_2B_1-2f_3B,\qquad
\mathscr B=-2f_1B+(h_0+4bh_6)B_1+6bf_4P_3 .
$$
代回即 (7)。这个论证用完整有限 theta 空间确定全部系数；
不是从少量数值 jet 外推。证毕。

在原 (2) 的对偶变量中，三个 sigma 的实际参数为
$z+s+t,\,-z+s-t,\,t-2z$。
故原 $\sigma(\xi_1)\sigma(\xi_3)\sigma(x)$ 贡献的是
$-\Psi(z,s,t)$。连同 $\rho_0$ 的 $-1/84$，
完整常数变为 $+1/84$。
纯 $C$ 平均只杀 (7) 的 $B_1(t)$ 项，严格保 $B,P_3$ 两项。

于是完整六输入上有
$$
\boxed{
\mu_0=\nu_\sigma(c)\otimes
       \{\nu_B(v)\otimes\Lambda_B+
         \nu_{P_3}(v)\otimes\Lambda_P\},
}
\tag{8}
$$
其中四维伴随测度不是未知的形式符号，而是
$$
\boxed{
\Lambda_B=\frac1{42}
 \{\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
       -\nu_{f_3}(Z)\otimes\nu_\Theta(Q)\}
       \otimes\nu_\sigma(r)\otimes\nu_\sigma(d_0),
}
$$
$$
\boxed{
\Lambda_P=\frac1{84}
 \{\nu_{\mathcal H_6}(Z)\otimes\nu_\Theta(Q)
       -6b\nu_{f_4}(Z)\otimes\nu_\Sigma(Q)\}
       \otimes\nu_\sigma(r)\otimes\nu_\sigma(d_0).
}
\tag{9}
$$
每个因子均采用原同一个 $\Omega$，全部分母在当前处为单位。

## 3. 一个准确的五次伴随提取

取固定原多项式
$$
g_5=Z^3r d_0 .
$$
实际矩给
$$
m_\sigma(1)=\Omega,\quad m_{f_3}(3)=6\Omega^3,\quad
m_\Theta(0)=1,\quad m_\Sigma(0)=0.
$$
$\mathcal H_6$ 型零、$f_4$ 型四，故两者三次矩均为零。
由 (9) 得
$$
\boxed{\ \Lambda_B(g_5)=-\Omega^5/7,\qquad
          \Lambda_P(g_5)=0.\ }
\tag{10}
$$
从而对于**任意完整有界连续双输入测试** $f(c,v)$，
$$
\boxed{
\int g_5 f(c,v)\,d\mu_0
=-\frac{\Omega^5}{7}
 \int f(c,v)\,d\nu_\sigma(c)d\nu_B(v).
}
\tag{11}
$$
这比只比较一个边际的质量强：它允许 $c,v$ 的任意实际混合单位、
深度、负幂或 log 测试。式中没有反卷积。

(11) 的量词也明确了范围。若测试另外依赖 $Z,Q,r,d_0$，
须保完整 (8)–(9)，不能直接把 $\Lambda_B$ 换成 (10) 的常数。
尤其原 $Y/W$ 混合测试一般属于这种情形。

## 4. 原四单位域上的简单极点积分

采用 R562 同一个独立源
$$
\nu_\sigma(c)\otimes\nu_B(v),\qquad
H=\delta c-v,\quad K=\delta c+v .
$$
这里 $v=\delta C$；不重复再乘一个 $\delta$。
令
$$
\mathscr D=\{H,K\ {\rm unit}\},\qquad
\mathscr B=\{c,v,H,K\ {\rm unit}\}.
\tag{12}
$$
本篇的 $\mathscr B$ 是此四单位域，
**不是** R556 的 $\{u\in p,L\ {\rm unit}\}$。

定义有界简单极点测试
$$
\boxed{
\varphi(c,v)=
\frac{c(7\delta^2c^2+5v^2)}
     {8\delta^2(\delta^2c^2-v^2)}
=\frac{4(H+K)+3(H^{-1}K^2+K^{-1}H^2)}
       {16\delta^3}.
}
\tag{13}
$$
它只在 $\mathscr D$ 上使用，域外延为零。
同时有实际函数恒等式
$$
\boxed{
\varphi=\frac{7c}{8\delta^2}
-\frac{3v^2}{4\delta^3}
       \partial_v\log\!\left(\frac{\delta c-v}{\delta c+v}\right).
}
\tag{14}
$$
这里 $\partial_v\log(H/K)=-1/H-1/K$ 是显示的有理函数；
不需要在不同 residue 盘之间选择一个新 log 分支。
$\varphi$ 为总次数一，故 $g_5\varphi$ 的总物理次数为六。

### 4.1 整个 H/K 双单位积分

R562 的同一个完整联合为
$$
G_B(h,k)=\delta\{
\mathcal H_6(h)f_1(k)+f_1(h)\mathcal H_6(k)
-6b[f_3(h)f_4(k)+f_4(h)f_3(k)]\}.
\tag{15}
$$
整个 even6 空间没有型 $5$。
所以在 $\mathscr D$ 上，$H^{-1}K^2$ 与
$K^{-1}H^2$ 两项的积分都为零；这是完整双输入上的型消去。
又记
$$
m_1^\times=\Omega(1-\beta\kappa),\qquad
m_B^\times(0)=1-\beta.
$$
由 (13)、(15)，精确得到
$$
\boxed{
\int_{\mathscr D}\varphi\,d(\nu_\sigma\otimes\nu_B)
=\frac{\Omega(1-\beta\kappa)(1-\beta)}{2\delta^2}.
}
\tag{16}
$$
等价地，(13) 是 R562 的
$c^3(H^{-2}+K^{-2})/2$
减去
$(H^{-2}K^3+K^{-2}H^3)/(16\delta^3)$。
这一步在同一个全联合中准确消去了负二矩项，没有断言负二矩为零。

### 4.2 两个真实深补集及全部尾项

$\mathscr D$ 的不交分解仍是
$$
\mathscr D=\mathscr B
 \ \sqcup\ \{c\in p\mathcal O,\ v\ {\rm unit}\}
 \ \sqcup\ \{c\ {\rm unit},\ v\in p\mathcal O\}.
\tag{17}
$$
后两域自动有 $H,K$ 单位。

在第一补集，把 $X=\delta^2c^2/v^2$ 代入 (13)：
$$
\varphi=-\frac{5c}{8\delta^2}
-\frac{3c}{2\delta^2}\sum_{j\ge1}X^j.
$$
原 sigma 非零矩只有 $1\bmod6$；用完整 $\beta$ 核，得到
$$
\boxed{
C_\varphi=
-\frac{5\beta\kappa\Omega(1-\beta)}{8\delta^2}
-\frac{3\beta}{2\delta^2}
 \sum_{r\ge1}\delta^{6r}\kappa^{6r+1}
 m_\sigma(6r+1)m_B^\times(-6r).
}
\tag{18}
$$

在第二补集，把 $T=v^2/(\delta^2c^2)$ 代入：
$$
\varphi=\frac{7c}{8\delta^2}
+\frac{3c}{2\delta^2}\sum_{j\ge1}T^j.
$$
原 $B$ 非零矩只有 $0\bmod6$，所以
$$
\boxed{
V_\varphi=
\frac{7\beta\Omega(1-\beta\kappa)}{8\delta^2}
+\frac{3\beta}{2\delta^2}
 \sum_{r\ge1}\delta^{-6r}\kappa^{6r}
 m_B(6r)m_\sigma^\times(1-6r).
}
\tag{19}
$$
所有负幂均在实际单位域，原测度整有界。
这两个级数一致收敛，尾阶分别为 $\kappa^7$ 和 $\kappa^6$。
没有把任何负矩换成正矩。

定义
$$
\mathcal R_{\rm simp}=
\int_{\mathscr B}\varphi\,d(\nu_\sigma\otimes\nu_B).
$$
由 (16)–(19) 精确有
$$
\boxed{
\begin{aligned}
\mathcal R_{\rm simp}
={}&\frac{\Omega}{8\delta^2}
 \{4-11\beta+\beta\kappa(1+6\beta)\}\\
&+\frac{3\beta}{2\delta^2}
 \sum_{r\ge1}\delta^{6r}\kappa^{6r+1}
 m_\sigma(6r+1)m_B^\times(-6r)\\
&-\frac{3\beta}{2\delta^2}
 \sum_{r\ge1}\delta^{-6r}\kappa^{6r}
 m_B(6r)m_\sigma^\times(1-6r).
\end{aligned}}
\tag{20}
$$
例如第二个尾的首项为
$-324b\beta\delta^{-8}\kappa^6\Omega^6
 m_\sigma^\times(-5)$；
第一个尾的首项为
$36b\beta\delta^4\kappa^7\Omega^7m_B^\times(-6)$。
原常数、一阶修正及两个补集的相位全在 (20) 内。

### 4.3 当前固定射线上的真实单位

**定理2。** 在全部当前普通素数上，
$$
\boxed{\quad 4-11\beta\in\mathcal O^\times,\qquad
                   \mathcal R_{\rm simp}\in\mathcal O^\times.\quad}
\tag{21}
$$

**证明。** 若 $4-11\beta$ 模原普通素位为零，
则 $\bar\pi_0\equiv11/4$。整数迹
$t_p=\pi_0+\bar\pi_0$ 满足
$4t_p-11=kp$，其中 $k\in\mathbf Z$。
Hasse 界给
$$
|4t_p-11|\le8\sqrt p+11<2p\qquad(p\ge71),
$$
所以 $k=-1,0,1$。但 $t_p$ 为偶数，
$4t_p-11\equiv5\bmod8$，
而 $p\equiv7\bmod8$ 使上述三个 $kp$ 的余数分别为 $1,0,7$，
均矛盾。
式 (20) 的其余显示一阶项在 $p\mathcal O$，
两尾分别在 $p^7\mathcal O,p^6\mathcal O$，
其外部 $\Omega/(8\delta^2)$ 为单位。证毕。

此定理不声称 $I_4=m_{f_4}^\times(-2)$ 非零。
它给的是同一个原四单位域上明确的另一条有界积分。

## 5. 单位行准确回到原六输入

由 (11)，定义原完整测试
$$
\mathfrak U(\xi)=g_5\,
1_{\{c,v,\delta c-v,\delta c+v\ {\rm unit}\}}\varphi(c,v).
$$
则
$$
\boxed{
\mu_0(\mathfrak U)
=-\frac{\Omega^5}{7}\mathcal R_{\rm simp}
=\frac{\Omega^6}{168}
 \{4-11\beta+\beta\kappa(1+6\beta)\}
 +p^6\mathcal O
 \in\mathcal O^\times.
}
\tag{22}
$$
精确尾由 (20) 乘 $-\Omega^5/7$ 给出，
不是只保一个形式模 $p$ 值。
整个权是原物理次数六，且没有引入 $\kappa^{-1}$；
唯一负幂都位于显示的原 $H,K$ 单位域。

原完整算术行同样可以用 (8) 精确表达。
令
$$
\ell=(p-1)\{
1_{\{Y\ {\rm unit}\}}\log\langle Y\rangle
-1_{\{W\ {\rm unit}\}}\log\langle W\rangle\}.
$$
由 (4)，$\ell$ 不含 $v$；只有在这个**未附加 carry 切集**的
完整测试中，$P_3(v)$ 的质量零才严格消去。
因此
$$
\boxed{
\begin{aligned}
J'_S-6\delta J'_T
=\mu_0(\ell)
=\frac1{42}\int \ell\,
 d\Bigl[
 &\nu_\sigma(c)\otimes\nu_\sigma(r)\otimes\nu_\sigma(d_0)\\
 &\otimes\{
 \nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
 -\nu_{f_3}(Z)\otimes\nu_\Theta(Q)\}
 \Bigr].
\end{aligned}}
\tag{23}
$$
两个实际单位条件和 (4) 的全部混合观察原样保留。
这是真实原 $S/T$ 来源的完整恒等式，不是把 (22) 的单位测试
改名为中央权。原归一也可检查为
$Y_*\mu_0=S$ 的首项 $z^6$、
$W_*\mu_0=6\delta T$ 的首项 $6\delta z^6$；
完整身份本身来自整个框架与原来源，而非该低阶检查。

## 6. 与原 q 的共同支和全部补域

保 R536 的准确三支测试，置 $\zeta_j=\omega^{2j}$：
$$
D_j=F-\zeta_j C,\quad E_j=F+13\zeta_j C,\quad
\Gamma_{n,j}=\{C,F\ {\rm unit},D_j\in p^n\},
$$
$$
\Gamma_n^{(3)}=\coprod_{j=0}^2\Gamma_{n,j},\qquad
q_n=\frac1{3b\Omega^6}\sum_{j=0}^2
1_{\Gamma_{n,j}}\,
\widehat P_p(D_j/\kappa^n,E_j,G).
\tag{24}
$$
所有 $\lambda,\kappa$ 系数、七行右逆及单位逆都在原
$\widehat P_p$ 内，不把它换成近似多项式。
R536 的全 $\pi_4$ 返回给
$$
\boxed{\mu_0(q_n\ell)=
             \beta^n(J'_S-6\delta J'_T).}
\tag{25}
$$
(25) 是完整算术行，不只是一条 native strip。

在每个实际 carry 上，有全深度等式
$$
v=\delta\zeta_j^{-1}(F-D_j),
$$
$$
H=\delta(c-\zeta_j^{-1}F)+\delta\zeta_j^{-1}D_j,\qquad
K=\delta(c+\zeta_j^{-1}F)-\delta\zeta_j^{-1}D_j .
\tag{26}
$$
由于 $n\ge1$，所以共同域准确为
$$
\boxed{
\mathscr K_{n,j}:=\Gamma_{n,j}\cap\mathscr B
=\Gamma_{n,j}\cap
 \{c,\ c-\zeta_j^{-1}F,\ c+\zeta_j^{-1}F\ {\rm unit}\}.
}
\tag{27}
$$
它不是只检查 $c,v$ 单位。

$\Gamma_{n,j}$ 中剩余的三个不交补支是
$$
\begin{aligned}
\mathscr C_{n,j,0}
 &=\Gamma_{n,j}\cap\{c\in p\mathcal O\},\\
\mathscr C_{n,j,-}
 &=\Gamma_{n,j}\cap
   \{c\ {\rm unit},\,c-\zeta_j^{-1}F\in p\mathcal O\},\\
\mathscr C_{n,j,+}
 &=\Gamma_{n,j}\cap
   \{c\ {\rm unit},\,c+\zeta_j^{-1}F\in p\mathcal O\}.
\end{aligned}
\tag{28}
$$
$F$ 为单位且 $p\ne2$，故这三支互不相交；
它们与 (27) 合起来正是整个 $\Gamma_{n,j}$。
原 $v$ 深支不在 carry 内，因为 (24) 强制 $C=v/\delta$ 为单位。
在 $\mathscr C_{0}$ 上 $H,K$ 都为单位；
在 $\mathscr C_{-}$ 或 $\mathscr C_{+}$ 上分别只有 $H$ 或 $K$ 深。
这些都是实际旧变量中的线性条件。

为把**两个测试**的差也写完整，记 $\ell/p$ 为原有界连续函数。
由 (22)、(25)，同源精确有
$$
\boxed{
\begin{aligned}
\mu_0(\mathfrak U)
-\frac{\beta^n}{p}(J'_S-6\delta J'_T)
={}&
 \sum_j\int_{\mathscr K_{n,j}}
      \{g_5\varphi-q_n\ell/p\}\,d\mu_0\\
&+\int_{\mathscr B\setminus\Gamma_n^{(3)}}
      g_5\varphi\,d\mu_0\\
&-\sum_{j=0}^2\sum_{\epsilon\in\{0,-,+\}}
      \int_{\mathscr C_{n,j,\epsilon}}
          q_n\ell/p\,d\mu_0 .
\end{aligned}}
\tag{29}
$$
$\ell/p$ 的整性来自原 $\log\langle\text{unit}\rangle\in p\mathcal O$；
所有其他测试在显示域上整有界。
在 (29) 中，$q_n$ 仍是 (24)，包括各自 $D_j/\kappa^n$；
不能因 (26) 在模 $p$ 保单位条件，就同时把该归一变量取零。

若原两个中央都为零，(29) 的整个右边必须是一个单位。
因此不能同时把共同域上的测试差、四单位域的 carry 外余域和
(28) 的三个实际补支都当成 $p$ 倍小项。
这给真实原算术测试与固定单位行之间的准确剩余条件，
没有把其中某个局部行单独置零。

对 (29) 的各项，也可逐项应用 R568/R569 已付的完整实际词
$\mathsf A=P_{u,\kappa}P_{P,\kappa}$。
必须同时把域取为 $\mathsf A$ 的像，把
$q_n,g_5,H,K,Y,W$ 全部按 $\mathsf A^{-1}$ 转置；
来源统一乘 $-\chi_{65}\lambda^2$。
不会由这个共同词自动使 (29) 的三个部分相等或消失。

## 7. 范围与证书

新增的实质输入是 (8)–(11) 的完整原双来源、
(20)–(22) 的四单位简单极点单位行、(23) 的原全算术五变量式，
以及 (26)–(29) 的真实同域比较。
它们不需要新增曲线身份、不使用反卷积，也不把两个原负矩赋非零。
原全中央之间的关系仍须利用 (29) 所保留的实际混合域支付；
课题完成标准尚未达到。

- [check-r572-original-c-splitting-and-simple-pole-unit.js](../scripts/check-r572-original-c-splitting-and-simple-pole-unit.js)
- [check-r572-original-c-splitting-and-simple-pole-unit.json](../scripts/check-r572-original-c-splitting-and-simple-pole-unit.json)

精确证书用 BigInt 的 $\mathbf Q(\omega)$ 算术核定全部六行矩阵、
所有原观察与 carry 行、全 sigma 相位、有限 theta 系数、
(13)–(14) 的完整有理函数身份、两个补集的常数及 (21) 的固定
模八排除。它不以有限素数试验或数值估计代替全域证明。
