# R271 附录：原尾强位—玻色回缩、同源三最小费与新高 Schur 能量

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。

状态：**已证明。** 本稿在原 $(j+1)^{-2}$ 连续尾中构造一个有界的精确回缩及其右截面。它保留任意给定个数的真实强位，支付全部核旗、原有限头和同一首源的完整右费、裸右费、左费。裸费的证明使用完整可行链到高输入空间的距离，不假设非酉交织与正交投影交换。

特别，当强位数 $k\le s+1$ 时，模型没有高输入；原同源的新 $H_2^\circ$ 返回能量遂有显式上界。$k\ge s+2$ 时模型仍有高出生，回缩不再杀去这些核方向，可用于真正高返回的有限模型研究。**混合逆费用 $\lambda_{\rm flat}$、固定实际 $W$ 来源及同返回源规范不在免费运输范围中。**

## 1. 原物理位、模型及预算

固定原 $m\ge5$、$d=2^m$、合法 $q$ 和实际头 $A=A_m$，不改变 $A$ 的物理内积或 carry。选整数
$$
0\le s\le q,\qquad k\ge0,\qquad
n=q-s,\qquad J=m+k+2n,\qquad P=s+d.
\tag{1.1}
$$
把原尾依次分成：

- 强位 $m,\ldots,m+k-1$；
- $n$ 个相邻配对，覆盖 $m+k,\ldots,J-1$；
- 从 $J$ 开始的完整远尾。

记 $a_j=(j+1)^{-2}$，
$$
D=D_m,\qquad D_J=\sum_{j\ge J}a_jE_j,\qquad
S=S_J=\sum_{j\ge J}a_j^2,\qquad
\delta=\frac{a_J^2}{S}.
$$
积分比较给
$$
\delta\le\frac3{J+1}.
$$
本稿只要求
$$
\boxed{\epsilon:=\frac{4(s+d)^2}{J+1}<1.}
\tag{1.2}
$$

模型是 $k$ 个真实强位与一个标准玻色模式的张量积。玻色基 $e_r$ 为标准正交基，$\mathfrak b e_r=\sqrt r\,e_{r-1}$。模型删除为
$$
\boxed{\mathsf D=\sum_{i=m}^{m+k-1}a_iE_i+\sqrt S\,\mathfrak b.}
\tag{1.3}
$$
只使用总孔数 $0,\ldots,P$。模型第 $p$ 孔层 $\mathsf H_p$ 的标准基为
$$
|I\rangle\otimes e_{p-|I|},\qquad
I\subset\{m,\ldots,m+k-1\},\quad |I|\le p.
$$
特别每层有限维；$\mathsf D$ 在这些层间有界。模型头仍是同一个 $A_m$，不是另选的四维头或抽象 Jordan 头。

下面的常数统一取
$$
R=\exp\!\frac2{m+k+1},\qquad
\kappa=(1-\epsilon)^{-1/2},\qquad
\chi=R\kappa.
\tag{1.4}
$$

## 2. 原相邻暗对的双向删除恒等式

对一个相邻配对，设其两个原权为 $\alpha,\beta>0$，定义
$$
h=\frac{\beta|10\rangle-\alpha|01\rangle}
        {\sqrt{\alpha^2+\beta^2}},\qquad
g=\frac{\alpha|10\rangle-\beta|01\rangle}
        {\sqrt{\alpha^2+\beta^2}},
$$
$$
\rho=\langle g,h\rangle=\frac{2\alpha\beta}{\alpha^2+\beta^2},
\qquad \ell(x)=\rho^{-1}\langle g,x\rangle.
$$
于是
$$
\|h\|=1,\quad \ell(h)=1,\quad
D_{\rm pair}h=0,\quad \ell D_{\rm pair}=0,\quad
\|\ell\|=\frac{\alpha^2+\beta^2}{2\alpha\beta}.
\tag{2.1}
$$
最后一个删除恒等式也在双占据输入上成立，因为
$D_{\rm pair}|11\rangle=\beta|10\rangle+\alpha|01\rangle$。

令 $h_{\rm mid}$ 为全部 $n$ 个 $h$ 的张量积，$\ell_{\rm mid}$ 为相应泛函的张量积；空乘积按 $1$ 理解。它们分别保留准确的 $n$ 孔前缀，且
$$
\|h_{\rm mid}\|=1,\quad
\ell_{\rm mid}(h_{\rm mid})=1,\quad
D_{\rm mid}h_{\rm mid}=0,\quad
\ell_{\rm mid}D_{\rm mid}=0.
\tag{2.2}
$$
若一对的起点为 $u$，则
$$
\log\|\ell_{\rm pair}\|
=\log\cosh\!\left(2\log\frac{u+2}{u+1}\right)
\le\frac2{(u+1)^2}.
$$
对起点 $m+k,m+k+2,\ldots$ 求和，使用
$\sum_{r\ge0}(a+2r)^{-2}\le a^{-1}$（$a\ge2$），得到
$$
\boxed{\|\ell_{\rm mid}\|\le R.}
\tag{2.3}
$$
这里是原相邻不等权配对，不以等权对替代它们。

## 3. 远尾真空列：精确玻色分析行与已付截面

在远尾第 $r$ 层定义标量分析行
$$
\tau_r f=
\frac{\langle(D_J^*)^r\Omega,f\rangle}{\sqrt{r!S^r}},
\qquad \tau_0=\langle\Omega,\cdot\rangle.
\tag{3.1}
$$
若 $e_r=e_r((a_j^2)_{j\ge J})$，则
$$
\|\tau_r\|^2=\frac{r!\,e_r}{S^r}\le1,
\qquad
\boxed{\tau_{r-1}D_J=\sqrt{rS}\,\tau_r.}
\tag{3.2}
$$
这是未逐层单位化的创建行；系数准确为 $\sqrt{rS}$，没有把原远尾的不同权视作等权。

用[完整双 Fock 塔](R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)的原 canonical 塔 $V_r=(W_r^*)^{-1}$，取其真空出生列
$$
v_r=
\sqrt{r!S^r}\,
D_{J,r}^{\dagger}\cdots D_{J,1}^{\dagger}\Omega,
\qquad v_0=\Omega.
\tag{3.3}
$$
这里明确是该塔的顺次单步 MP 列；不称为 $(D_J^r)^\dagger$。它满足
$$
D_Jv_r=\sqrt{rS}\,v_{r-1},\qquad
\tau_rv_r=1.
\tag{3.4}
$$
第二式可由第一式迭代到真空直接验证。

双 Fock 塔的全出生条件数以
$\epsilon_P=\frac43\delta P^2$ 控制。由 (1.2)，
$\epsilon_P\le\epsilon<1$，所以同一个已证界给
$$
\boxed{\|v_r\|\le\kappa\qquad(0\le r\le P).}
\tag{3.5}
$$
全部使用的远尾层均在这个已付窗口内。

## 4. 精确回缩与右截面保留全部核旗

对原第 $n+p$ 孔层，定义
$$
\mathsf T_p:\mathcal H_{n+p}^{\rm tail}\longrightarrow\mathsf H_p
$$
为：强位保留恒等，在中间配对施加 $\ell_{\rm mid}$，远尾的第 $r$ 层施加 $\tau_r$ 并写入玻色坐标 $e_r$。原层小于 $n$ 时将 $\mathsf T$ 定义为零。

反向定义
$$
\mathsf B_p:\mathsf H_p\longrightarrow\mathcal H_{n+p}^{\rm tail},
\qquad
\mathsf B_p(|I\rangle\otimes e_r)
=|I\rangle\otimes h_{\rm mid}\otimes v_r.
\tag{4.1}
$$
按孔层取直和。不同强位标签正交，不同总孔层也正交；因此 (2.3)、(3.2)、(3.5) 给
$$
\boxed{
\mathsf T\mathsf B=I,\qquad
\|\mathsf T\|\le R,\qquad
\|\mathsf B\|\le\kappa.
}
\tag{4.2}
$$
由 (2.2)、(3.2)、(3.4)，在每一个使用的层上都有
$$
\boxed{
\mathsf T D=\mathsf D\mathsf T,\qquad
D\mathsf B=\mathsf B\mathsf D.
}
\tag{4.3}
$$
将这些算子张量原头恒等，它们与 $A_m$ 交换。

所以对每个使用的 $h,p$，
$$
\mathsf T\bigl(\ker D^h\cap\mathcal H_{n+p}\bigr)
\subseteq\ker\mathsf D^h\cap\mathsf H_p,
$$
$$
\mathsf B\bigl(\ker\mathsf D^h\cap\mathsf H_p\bigr)
\subseteq\ker D^h\cap\mathcal H_{n+p}.
\tag{4.4}
$$
右截面恒等还给第一式在模型核上的满射。这里只运输核及像的准确关系；没有宣称它运输它们的正交补或正交投影。

模型 $\mathsf D:\mathsf H_p\to\mathsf H_{p-1}$ 满射。一个直接证明是先用玻色右逆，再按强位删除作有限 Neumann 展开：强位删除每次减少强位占据，至多 $k+1$ 次即为零。故与原尾一样，所有固定层的真正最小逆存在。各核阶的相容右逆和完整旗的有限递推也成立。

## 5. 同一个嵌入源的完整、裸、左最小费用

模型源空间取与原问题完全相同的逐头旗，只把源孔数 $q$ 换成 $s$：
$$
\mathsf R_s=
\bigoplus_{i=0}^{d-2}
e_i\otimes\bigl(\ker\mathsf D^{d-i-1}\cap\mathsf H_s\bigr).
$$
给定任意 $\widehat r\in\mathsf R_s$，本节始终用同一个原源
$$
\boxed{r=(I_{\rm head}\otimes\mathsf B_s)\widehat r.}
\tag{5.1}
$$
由 (4.4)，$r\in\mathscr R_q$，且 $\mathsf T r=\widehat r$。

原完整右链空间、方程及高输入为
$$
\mathscr C_j=
\bigoplus_{i=0}^{d-j}e_i\otimes E_{d-i,q+j},
\quad
Fc=Dc_1,\quad
(Sc)_j=Ac_j+Dc_{j+1},
$$
$$
\mathscr X_H=
\bigoplus_{j=1}^d
\bigoplus_{i=0}^{d-j}e_i\otimes E_{j-1,q+j}.
\tag{5.2}
$$
$E_{0,p}=0$。模型对应空间使用 $\mathsf D$、$\mathsf H_{s+j}$。由 (4.3)--(4.4)，$\mathsf T,\mathsf B$ 双向保留完整链方程、全部逐头旗及高输入空间。

令
$$
\mathcal A(r)=\{c\in\mathscr C:Fc=r,\ Sc=0\}.
$$
完整与裸最小费分别是
$$
\lambda(r)=\min_{c\in\mathcal A(r)}\|c\|,
\qquad
\boxed{
\alpha(r)=\inf_{c\in\mathcal A(r)}
                 \operatorname{dist}(c,\mathscr X_H).
}
\tag{5.3}
$$
第二个式子与原裸定义一致：完整可行链的低投影恰为同源低可行链；反向可由高方程的相容右逆补全。固定窗口的闭像及最小值均已存在。模型也可用其逐层满射作同一有限递推证明。

真正左费为
$$
\mu(r)=\min\{\|v\|:
\operatorname{supp}v\subset[0,q],\
P_{<q}(A+D)v=0,\ Av_q=r\}.
\tag{5.4}
$$
模型相应最小费写作 $\widehat\lambda,\widehat\alpha,\widehat\mu$。

**同源三费用定理。** 对 (5.1) 的同一个原源，
$$
\boxed{
R^{-1}\widehat\lambda(\widehat r)
\le\lambda(r)\le\kappa\widehat\lambda(\widehat r),
}
$$
$$
\boxed{
R^{-1}\widehat\alpha(\widehat r)
\le\alpha(r)\le\kappa\widehat\alpha(\widehat r),
}
$$
$$
\boxed{
R^{-1}\widehat\mu(\widehat r)
\le\mu(r)\le\kappa\widehat\mu(\widehat r).
}
\tag{5.5}
$$

完整右费和左费的证明直接把可行点经 $\mathsf T$ 或 $\mathsf B$ 运输。裸费还需要保留距离：若 $c$ 是模型完整可行链，则对任意模型高向量 $h$，
$$
\operatorname{dist}(\mathsf Bc,\mathscr X_H)
\le\|\mathsf B(c-h)\|
\le\kappa\|c-h\|.
$$
对 $h$ 再对 $c$ 取下确界，得到裸费上界；以 $\mathsf T$ 作反向同一论证得到下界。这一步不需要、也没有使用
$P_L\mathsf B=\mathsf BP_{\widehat L}$。

## 6. 完整高费用的准确加性运输

定义原同源新高能量及模型量
$$
\mathcal E_H(r)=\lambda(r)^2-\alpha(r)^2,\qquad
\widehat{\mathcal E}_H(\widehat r)
=\widehat\lambda(\widehat r)^2-\widehat\alpha(\widehat r)^2.
$$
两者非负。三费用定理直接给
$$
\boxed{
R^{-2}\widehat{\mathcal E}_H
-(\kappa^2-R^{-2})\widehat\alpha^2
\le\mathcal E_H
\le
\kappa^2\widehat{\mathcal E}_H
+(\kappa^2-R^{-2})\widehat\alpha^2.
}
\tag{6.1}
$$
下界还可与零取最大。不可把加性误差删掉，宣称高能量本身按相同常数乘法运输。

对非零源定义
$$
c(r)=\frac{\lambda(r)^2-\alpha(r)^2}
           {\alpha(r)^2+\mu(r)^2},
$$
模型定义同样。因为
$1+c=(\lambda^2+\mu^2)/(\alpha^2+\mu^2)$，有
$$
\boxed{
\chi^{-2}(1+\widehat c)\le1+c\le\chi^2(1+\widehat c).
}
\tag{6.2}
$$
所以模型中的大完整高费比若超过全部显示的 $\chi$ 费用，确实能给同一嵌入原源的大比值；它仍不自动满足固定 $W$ 的额外来源规范。

由[真幂底项与两过滤桥](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)及[新中间 Schur](R271-appendix-boundary-first-middle-schur-is-the-primitive-difference-gram.md)，原量精确为
$$
\boxed{
\mathcal E_H(r)=
\left\langle
(H_2^\circ)^{-1}\mathcal R\mathcal G^\dagger\zeta(r),
\mathcal R\mathcal G^\dagger\zeta(r)
\right\rangle.
}
\tag{6.3}
$$
这里 $\zeta(r)$、$\mathcal G^\dagger$、$\mathcal R$ 都是原完整滤波对象，且
$H_2^\circ=S_HS_H^*+\mathcal R(I-\Pi)\mathcal R^*$。本稿没有改写或交换其中两个受限 $D_3^*$。

## 7. 没有模型高输入时，支付原新末块能量

模型层维数是
$$
\dim\mathsf H_p=\sum_{j=0}^{\min(k,p)}\binom kj.
\tag{7.1}
$$
特别 $p\ge k$ 后恒为 $2^k$。若
$$
\boxed{k\le s+1,}
\tag{7.2}
$$
则对每个右段 $j\ge1$，
$$
\mathsf D^{j-1}:\mathsf H_{s+j}\longrightarrow\mathsf H_{s+1}
$$
是满射且两边同维，故为双射。因此
$$
\ker\mathsf D^{j-1}\cap\mathsf H_{s+j}=0,\qquad
\widehat{\mathscr X}_H=0.
$$
模型完整费与裸费准确相等，$\widehat\lambda=\widehat\alpha$。结合 (5.5)，得到本稿的原尾高能量上界：
$$
\boxed{
\begin{aligned}
&\left\langle
(H_2^\circ)^{-1}\mathcal R\mathcal G^\dagger\zeta(r),
\mathcal R\mathcal G^\dagger\zeta(r)
\right\rangle\\
&\hspace{15mm}\le
\left[
\frac{\exp(4/(m+k+1))}
 {1-4(s+d)^2/(m+k+2(q-s)+1)}
-1
\right]\alpha(r)^2 .
\end{aligned}
}
\tag{7.3}
$$
它对 (5.1) 的整个模型源空间成立，保持原 $A_m$、原尾、原全部旗和同一实际 $r$。

当 $m\to\infty$ 且 $(s+d)^2/(J+1)\to0$ 时，方括号趋于零。若 $\epsilon\le1/4$，由 $4/(m+k+1)\le2/3$ 还可用简洁界
$$
\chi^2-1
\le\frac{11}{m+k+1}+\frac{6(s+d)^2}{J+1}.
\tag{7.4}
$$
例如 $s=0,k=1$ 时，模型源为任意合法头向量乘真空，原源是同一头向量乘
$$
\Omega_{\{m\}}\otimes h_{\rm mid}\otimes\Omega_{\{j\ge m+1+2q\}},
$$
即一个未占据真实强位、$q$ 个原相邻暗对及远尾真空。原高返回不被假定为零，而由 (7.3) 支付。

这里控制的是允许原零首源低自由度参与的**新** $H_2^\circ$ 最小能量。没有据此单独界住纯高修复
$\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|$。

## 8. 两道 primitive 桥确能保留下来

若 $k\ge s+2$，则
$$
\dim\ker\mathsf D|_{\mathsf H_{s+2}}=\binom{k}{s+2}>0.
$$
由 $\mathsf T\mathsf B=I$，这个原高输入子空间的像并不被分析行杀掉。因此本稿的回缩不限于此前“真幂测试杀整个核”的方形情形。

最小例为 $s=0,k=2$。令两个强位权为 $a,b>0$，模型第2层的向量
$$
u=|12\rangle\otimes e_0
-\frac b{\sqrt S}|1\rangle\otimes e_1
-\frac a{\sqrt S}|2\rangle\otimes e_1
+\frac{\sqrt2ab}{S}|\varnothing\rangle\otimes e_2
$$
满足 $\mathsf Du=0$。模型交换子中的三次尾为
$$
\mathsf C=a^3E_1+b^3E_2,\qquad
[\mathsf D,[\mathsf D,\mathsf D^*]]=-2\mathsf C.
$$
直接计算
$$
\mathsf C^2u=2a^3b^3\Omega\ne0.
\tag{8.1}
$$
所以相邻两道真实受限 primitive 伴随的复合非零。回缩将这些高核方向准确嵌入原核旗；估计仍须使用 §§5–6 的实际范数费用。本文没有把 $\mathsf C$ 与原 $D_3$ 直接交织，也没有把 (8.1) 当作原高费下界。

## 9. 未运输的混合逆及实际来源

原 $\lambda_{\rm flat}$ 不是 §§5–6 的某个同源最小范数。若 $J_{\rm left}=EE^*$，并令 $\mathsf F_{\rm right}=F|_{\ker S}$、$G_{\rm right}=\mathsf F_{\rm right}\mathsf F_{\rm right}^*$，则
$$
\lambda_{\rm flat}(r)^2
=\left\langle
J_{\rm left}^{-1}G_{\rm right}J_{\rm left}^{-1}r,r
\right\rangle.
\tag{9.1}
$$
两边各自最小费的比较，不能把这个完整交叉量免费运输到同一个
$\widehat r$。非酉回缩也不保持同返回源的加权正交规范。

同样，(4.3) 交织纯边界 $A_m+D_m$；它没有与固定实际 $T_N/T_Y$ 交换，故不由此声称 $\mathsf B\widehat w\in W$ 或从有限模型自动获得原缺陷向量。若使用模型的坏源，仍须验证原同源的 flat 费用、真实 $M/W$ 来源或已付规范归约。

本稿新增的是原连续尾中的全部核旗回缩、三项同源真正最小费以及 (7.3) 的实际新末块能量。原全源、实际窄源的剩余高费用、无权 $N=M$ 和普通 Hilbert ISP 继续开放。
