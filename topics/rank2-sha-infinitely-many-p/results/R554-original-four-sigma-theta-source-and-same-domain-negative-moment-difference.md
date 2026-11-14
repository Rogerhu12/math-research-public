# R554：原四条 $\sigma$ 与一条 $\Theta$ 的完整有界来源，以及同域负矩差

## 1. 固定原来源和结论

沿用 R540、R549 的曲线、微分、同一普通地点和普通周期。允许
$b=1$ 或返回原曲线后的 $b=17$，并排除已经删去的有限坏素数。
写

$$
x=\wp,\qquad y=\wp'/2,\qquad y^2=x^3+b,\qquad
D=\frac d{dz},\quad g=D\log\sigma ,
$$

所以 $Dx=2y,\ Dy=3x^2,\ Dg=-x$。令

$$
\Theta=x\sigma^2=\frac{\sigma(\delta z)}{\delta\sigma(z)},\qquad
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6.
\tag{1}
$$

$\Theta$ 是已经支付的质量一、degree $2$ 来源；以下没有在 Mellin
积分内部除掉它。取五条**独立**输入的完整测度

$$
\rho=\nu_\sigma^{\otimes4}\otimes\nu_\Theta,\qquad
(t_1,t_2,t_3,t_4,u),\qquad Y=t_1+t_2+t_3+t_4+u,
$$

$$
e_2(\mathbf t)=\sum_{1\le i<j\le4}t_it_j.
\tag{2}
$$

本条支付的是两个完整推前：

$$
\boxed{\nu_{f_4}=Y_*\rho,}
\tag{3}
$$

$$
\boxed{\nu_{f_1}
=\frac{\Omega_p^{-3}}{24}\,
Y_*\bigl[(Y^3-18u e_2(\mathbf t))\,\rho\bigr].}
\tag{4}
$$

这不是只比较原点质量或若干 Taylor 系数。两条负矩现在来自
**同一个**实际五输入表示和**同一个** $Y$ 单位域。

## 2. 整个函数恒等式

直接在原微分环中计算：

$$
Df_4=(2y+6gx)\sigma^6,
$$

$$
D^2f_4=(24gy+36g^2x)\sigma^6,
$$

$$
D^3f_4=24f_1+216g^2(y+gx)\sigma^6.
\tag{5}
$$

中间的 $gx^2$ 项确切相消。另一方面

$$
D\Theta=2(y+gx)\sigma^2,\qquad D\sigma=g\sigma.
$$

所以保留 (5) 的全部剩余项，得到

$$
\boxed{
Q:=D^3f_4-24f_1
=108\,\sigma^2(D\sigma)^2D\Theta .
}
\tag{6}
$$

右侧每一个因子都是固定整来源的正阶导数；式 (6) 没有把
$g^2$、$g^3$ 删去，也不需要把 $g$ 单独解释为有界测度。
它给的是四条原 $\sigma$ 输入和一条原 $\Theta$ 输入上的
正多项式权。

由 $f_4=\sigma^4\Theta$ 已得 (3)。现在使用原 Amice 规范

$$
\mathcal A_{\nu_F}(T)=F\bigl(\Omega_p\log(1+T)\bigr),\qquad
\nu_{D^jF}=\Omega_p^{-j}t^j\nu_F .
\tag{7}
$$

对 (6) 的一个输入标记，右侧测度为

$$
108\Omega_p^{-3}
Y_*\bigl[u\,t_3t_4\,\rho\bigr].
$$

四条 $\sigma$ 输入的真实置换对称性给

$$
Y_*(u\,t_3t_4\,\rho)
=\frac16Y_*(u e_2(\mathbf t)\rho).
$$

再用 $D^3f_4$ 的完整测度为
$\Omega_p^{-3}Y_*(Y^3\rho)$，即得 (4)。所有分母
$6,24$ 及 $\Omega_p$ 在当前射线上均为单位。

## 3. 完整测试范围与不能删除的条件

(3)–(4) 是有界测度的恒等式，因此对任意连续的 $Y$ 测试
$\varphi$ 有

$$
\int\varphi\,d\nu_{f_1}
=\frac{\Omega_p^{-3}}{24}
\int \varphi(Y)(Y^3-18u e_2)\,d\rho .
\tag{8}
$$

局部常值深度条件可以包含在 $\varphi(Y)$ 中。其支持不必是整个
$\mathbf Z_p$。

另一方面，若新测试另含 $t_i$ 或 $u$ 的独立隐藏条件，则 (8)
本身不授权把这些条件移到 $\nu_{f_1}$。完整五输入的右侧仍可
定义并研究，但必须保留它们；不能因同一个总推前恒等式而
认定两个隐藏事件相同。

本条也没有从 $\Theta(0)=1$ 直接在单位 Mellin 泛函内做反卷积。
(2) 中的 $u$ 始终是实际的独立输入。

## 4. 指定两个负矩的同域差

采用 R540 的两条原负矩

$$
I_4=\int_{\mathbf Z_p^\times}v^{-2}\,d\nu_{f_4}(v),\qquad
I_1=\int_{\mathbf Z_p^\times}v^{-5}\,d\nu_{f_1}(v).
\tag{9}
$$

令

$$
J_\rho=
\int_{\{Y\in\mathbf Z_p^\times\}}
\frac{u e_2(\mathbf t)}{Y^5}\,d\rho.
\tag{10}
$$

这是有界连续被积函数与有界测度的原积分；分母只在明确的
$Y$ 单位域上取逆。(3)–(4) 给

$$
\boxed{24\Omega_p^3I_1=I_4-18J_\rho,}
\tag{11}
$$

或按 R549 的固定周期次幂，

$$
\boxed{
\Omega_p^2I_4-24\Omega_p^5I_1
=18\Omega_p^2J_\rho
=\Omega_p^5
\int_{\mathbf Z_p^\times}v^{-5}\,d\nu_Q(v).
}
\tag{12}
$$

因而同时假设 $I_4=I_1=0$，确实迫使 (10) 的**同一真实域**
加权积分为零。这里没有把它替成各输入独立单位、各输入独立
深度，或 $\{u\text{ unit},\sum t_i\text{ deep}\}$ 等其他域。

R540 已证明 $I_4$ 的平方属于同一个导子 $(6)$ 的真实
$\xi\psi_0^{-1}\bar\psi_0^2$ Katz 分支。本文没有改变有限角色、
普通地点、Euler 因子或该算术身份；$Q$ 也未被另认成某条
秩二曲线来源。

## 5. 固定全来源非零与十二阶原函数

原小展开为

$$
\sigma=z+\frac b{210}z^7+\cdots,\qquad
\Theta=1-\frac{2b}{15}z^6+\cdots,
$$

$$
f_4=z^4-\frac{4b}{35}z^{10}+\cdots,\qquad
f_1=z+\frac{6b}{35}z^7+\cdots.
$$

所以 (6) 给整个固定来源的首项

$$
\boxed{Q(z)=-\frac{432b}{5}z^7+\cdots.}
\tag{13}
$$

当前 $p>19$、$p\nmid b$ 时，这个首阶正矩是单位。它证明
$Q$ 本身非零，**并不**证明其指定负五矩非零。

令 $F_4''=f_4$、$F_1^{(5)}=f_1$，各自所有初始常数均取零。
则固定函数

$$
\mathcal H=F_4-24F_1,\qquad
D^5\mathcal H=Q,\qquad
\boxed{\mathcal H=-\frac b{1100}z^{12}+\cdots}
\tag{14}
$$

正是 paired-V 检查点中的同源十二阶剩余。式 (6) 支付了它的
五阶导数的完整有界正矩表示；它没有把 $\mathcal H$ 本身
认成有界测度或固定有限 theta 空间的元素。

## 6. 原普通核心下的完整二来源返回

本节的 $\beta_6,\kappa_0$ **专指 R540 的基曲线普通规范**：

$$
\beta_6=\xi(\mathfrak p)/\bar\pi_{0,p},\qquad
\kappa_0=\pi_{0,p}/\bar\pi_{0,p}.
$$

它们不与其他结果为原秩二来源选择的 $\beta,\kappa$ 混名。
R540 的两条完整来源核心为

$$
\nu_{f_j}|_{p\mathbf Z_p}
=\beta_6[\kappa_0]_*\nu_{f_j}\qquad(j=4,1).
$$

令 $F=D^3f_4$、$G=f_1$。把 (7) 的真实 $v^3$ 权一并运输：

$$
\nu_F|_{p\mathbf Z_p}
=\beta_6\kappa_0^3[\kappa_0]_*\nu_F,\qquad
\nu_G|_{p\mathbf Z_p}
=\beta_6[\kappa_0]_*\nu_G.
\tag{15}
$$

于是对同一 $Q=F-24G$，

$$
\boxed{
\nu_Q|_{p\mathbf Z_p}
=\beta_6[\kappa_0]_*
\bigl(\kappa_0^3\nu_Q+24(\kappa_0^3-1)\nu_G\bigr).
}
\tag{16}
$$

这是整个 $Y$ 测度的二来源闭合，保全部 $Y$ 测试。它不是
$Q$ 的单一标量核心，也不授权保留任意独立五输入隐藏条件。
按 R540 同时运输 $b=1$ 到 $b=17$ 的微分与周期后，(15)–(16)
仍成立：$F,G,Q$ 均乘相同的固定 $\theta^{-1}$，其中
$\theta=17^{1/6}$。

## 7. 证书和主缺口

配套脚本在
$\mathbf Q[b,x,y,g,\sigma]/(y^2-x^3-b)$ 中逐项检验 (5)–(6)，
独立核对固定首项、五输入对称权系数 $18$ 和二来源核心矩阵。
它不以有限素数样本代替函数恒等式。

本条已把两个指定负矩差完全接回同一个有界五输入来源。
还需证明相应完整单位域上的非消失，或找到与已知算术中央零
相容的全部补域消元。不得从 (13)、(14) 的局部非零直接删除
(10) 的真实互补条件。
