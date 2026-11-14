# R239 附录：原首头商的实际行图权、负Schur和同一未来带三费字典

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文对原 regular 严格降头矩阵，消去第零物理头，准确识别剩余左、完整右、裸右三种度量。左负 Schur 和完整右费使用同一个逐孔行图权；裸右费保留真实出生截断，因而仍看得见两种右费之间的高返回差。对于同一个真正顶部最小者，商前缀仍是这个加权问题的真正最小者，两个右测试也由同一个未来带支付。没有使用整个头矩阵的逆或 Jordan 条件数。最终的加权规范类比较仍未证明，普通 ISP 与无权 $N=M$ 仍为 OPEN。

依赖：[首源头共同右度量](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md)、[原负源流](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)、[任意严格降头的裸链补全](R239-appendix-natural-four-block-free-flag-and-bare-chain-transport.md) §§5–6、[同未来带双投影](R239-appendix-future-band-projection-angle-and-complete-common-cost-negative-graph.md)。下面直接重做所有消元及旗检查。

## 1. 原物理头的准确商与固定层逆

固定原头 $A=A_m$、$d=2^m$ 和尾 $D=D_m$，取原合法 $m,q$；特别可取 $m\ge8$、$4d\le q\le e^{d^3/4}$。把第零物理头分出：
$$
A=\begin{pmatrix}0&a\\0&\widehat A\end{pmatrix},
\qquad \mathbb C^d=\mathbb Ce_0\oplus\widehat H,
\qquad \widehat H=\operatorname{span}(e_1,\ldots,e_{d-1}).
\tag{1.1}
$$
$a$ 是原矩阵的整条首行；不只保留最近邻系数。$\widehat A$ 是维数 $d-1$ 的 regular 严格降头矩阵。所有头坐标仍是原正交物理坐标。

记
$$
E_{k,p}=\ker D^k\cap\mathcal H_p,\qquad E_{0,p}=\{0\},
\qquad P_{k,p}=P_{E_{k,p}},
$$
$$
R_p=(D:\mathcal H_{p+1}\to\mathcal H_p)^\dagger.
\tag{1.2}
$$
固定孔层删除满射，故 $DR_p=I$、$R_p\perp\ker D$；由直接相乘，
$$
R_pE_{k,p}\subseteq E_{k+1,p+1}.
\tag{1.3}
$$
这里只用真正单步 MP 逆，不将顺次逆认作幂的 MP 逆。

原源空间和商源空间分别是
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q},\qquad
\widehat{\mathscr R}_q=\bigoplus_{i=1}^{d-2}e_iE_{d-i-1,q}.
\tag{1.4}
$$
因此原源唯一写作 $r=(r_0,x)$，$r_0\in E_{d-1,q}$、$x\in\widehat{\mathscr R}_q$。记 $P$、$Q=I-P$ 为这个物理源分解。

定义商左空间及源映射
$$
\widehat V_q=\{\widehat v\in\widehat H\otimes\mathcal H_{\le q}:
\widehat A\widehat v_p+D\widehat v_{p+1}=0\ (0\le p<q)\},
\qquad \widehat E_q\widehat v=\widehat A\widehat v_q.
\tag{1.5}
$$
原、商矩阵均 regular，故它们的短核旗就是 (1.4) 对应的完整标准旗；商顶输入第 $i$ 头为 $E_{d-i,q}$。这一步不向退化头的任意物理商免费外推。

## 2. 原左费：首头每层可独立作真正 MP 消元

给定 $\widehat v\in\widehat V_q$，原左方程的第零头恰为
$$
Dv_{0,p+1}=-a\widehat v_p\quad(0\le p<q).
\tag{2.1}
$$
因为 $Ae_0=0$，这些首头分量不反馈到其余方程。它们的所有 primitive 部分以及 $v_{0,0}$ 都是独立零源方向，最小者中全为零。因此唯一最小首头补全是
$$
v_{0,0}=0,\qquad v_{0,p+1}=-R_pa\widehat v_p.
\tag{2.2}
$$
每个 $a\widehat v_p\in E_{d-1,p}$，(1.3) 保证 (2.2) 落在原第零头的 $E_{d,p+1}$，包括所有短核阶。原顶源首头为 $r_0=a\widehat v_q$。

故原真正左费准确为
$$
\boxed{
\mu_A(r_0,x)^2
=\min_{\substack{\widehat v\in\widehat V_q\\
\widehat E_q\widehat v=x,\ a\widehat v_q=r_0}}
\left[\|\widehat v\|^2+
\sum_{p=0}^{q-1}\|R_pa\widehat v_p\|^2\right].
}
\tag{2.3}
$$
各参数固定时所有映射有界、约束闭，并且目标至少是 $\|\widehat v\|^2$；最小值取得。由原源映射的满射性，对 (1.4) 的每个 $(r_0,x)$ 约束均可行。

## 3. 负源图的 Schur 恰是逐孔行图权下的商左费

在同一原源空间上写
$$
L=J_{\rm left}^{-1}=\begin{pmatrix}L_{00}&L_{01}\\L_{10}&L_{11}\end{pmatrix},
\qquad K=(R_q|_{E_{d-1,q}})^*(R_q|_{E_{d-1,q}}).
$$
首源头共同右最小链引理给
$$
B=J_b^{-1}=K\oplus B_1,\qquad
G^{-1}=K\oplus G_1^{-1}.
\tag{3.1}
$$
这里 $B_1,G_1$ 仍是原源中 $Q$ 块，尚未换成无权商度量。

固定 $x$，极小化 $\mu_A(r_0,x)^2+\|R_qr_0\|^2$。源坐标中直接配方给
$$
r_0^*(x)=-(L_{00}+K)^{-1}L_{01}x,
\qquad
S^-=L_{11}-L_{10}(L_{00}+K)^{-1}L_{01},
\tag{3.2}
$$
极小值为 $\langle S^-x,x\rangle$。

另一方面，把 (2.3) 代入，并让 $r_0=a\widehat v_q$ 随 $\widehat v$ 变化，得到
$$
\boxed{
\langle S^-x,x\rangle
=\min_{\substack{\widehat v\in\widehat V_q\\\widehat E_q\widehat v=x}}
\sum_{p=0}^{q}\left[\|\widehat v_p\|^2+
\|R_pa\widehat v_p\|^2\right].
}
\tag{3.3}
$$
于是定义在整层 $\widehat H\otimes\mathcal H_p$ 上的实际正权为
$$
\boxed{W_p=I+a^*R_p^*R_pa\succeq I.}
\tag{3.4}
$$
式 (3.3) 是 $\widehat A+D$ 原方程在这些物理逐孔权下的真正左最小问题。它不只是抽象的源 Schur 表达式。

权可写成 $I+(a^*a)\otimes R_p^*R_p$，但 $R_p^*R_p$ 未被假定保所有短核旗；(3.3) 始终把二次型限制到原合法 $\widehat V_q$。同样不假定 $W_p$ 与 $\widehat A$ 或 $D$ 交换。

## 4. 完整右费的 Q 块：完全相同的行图权

商完整右链记为 $\widehat c=(\widehat c_1,\ldots,\widehat c_{d-1})$。第 $j$ 段位于 $q+j$ 孔，允许原头 $1\le i\le d-j$，第 $i$ 头尾旗为 $E_{d-i,q+j}$。它满足
$$
D\widehat c_1=x,\qquad
\widehat A\widehat c_j+D\widehat c_{j+1}=0\ (1\le j<d-1),
\qquad \widehat A\widehat c_{d-1}=0.
\tag{4.1}
$$

任何原完整右链源为 $(0,x)$ 时，删去第零头得到这样的商链。反向给定 (4.1)，第零头的准确最小补全为
$$
c_{1,0}=0,\qquad
c_{j+1,0}=-R_{q+j}a\widehat c_j\quad(1\le j\le d-1).
\tag{4.2}
$$
首方程 $Dc_{1,0}=0$ 的 primitive 自由量最小为零；每个后续方程也独立地由 MP 最小化。因为 $a\widehat c_j\in E_{d-1,q+j}$，新首头落在 $E_{d,q+j+1}$。最后一段仅有第零头，所以原末输出自动为零。所有头、段和尾核旗均合法。

用 $I_f\widehat c$ 表示 (4.2) 与原商分量拼成的链。其准确范数为
$$
\|I_f\widehat c\|^2
=\sum_{j=1}^{d-1}\langle W_{q+j}\widehat c_j,\widehat c_j\rangle.
\tag{4.3}
$$
故
$$
\boxed{
\lambda_A(0,x)^2=\langle G_1^{-1}x,x\rangle
=\min_{\substack{\widehat c\ {
m 满足}\ (4.1)}}
\sum_{j=1}^{d-1}\langle W_{q+j}\widehat c_j,\widehat c_j\rangle.
}
\tag{4.4}
$$
这个 $G_1$ 正是 (3.1) 的原完整右 Gram 块。左边的 (3.3) 与右边的 (4.4) 现在使用同一套 $W_p$，只在不同的实际孔层取值。

## 5. 裸右 Q 块：截断 MP 图与高返回项

商裸低链第 $j$ 段另满足
$$
\widehat c_j\perp E_{j-1,q+j}
\tag{5.1}
$$
（逐头理解），且 (4.1) 的内部方程只在低出生输出中成立，即其残差属于 $E_{j-1,q+j}$。这是宽度 $d-1$ 的真正商裸旗，和原删去首头后的低旗一致。

对一个给定裸商链，令 $y=a\widehat c_j$。于是
$y\in E_{d-1,q+j}\cap E_{j-1,q+j}^\perp$。原第 $j+1$ 段首头必须在
$E_{d,q+j+1}\cap E_{j,q+j+1}^\perp$，并满足
$$
(I-P_{j-1,q+j})(y+Dz)=0.
\tag{5.2}
$$
其唯一解准确为
$$
\boxed{z=-(I-P_{j,q+j+1})R_{q+j}y.}
\tag{5.3}
$$
存在性：$DRy=y$，而 $DP_{j,q+j+1}Ry\in E_{j-1,q+j}$，故 (5.2) 成立；投影与嵌套核旗还保证 $z\in E_d\cap E_j^\perp$。唯一性：若两个解之差 $z'$ 正交于 $E_j$，同时 $Dz'\in E_{j-1}$，则 $D^jz'=0$，因此 $z'\in E_j$，只能为零。没有把 $R$ 与 $P_j$ 交换。

记相应裸补全映射为 $I_b$，并定义实际二次型权
$$
\boxed{
W_{q+j}^{[j]}
=I+a^*R_{q+j}^*(I-P_{j,q+j+1})R_{q+j}a.
}
\tag{5.4}
$$
首段首头仍是独立 primitive，最小为零。因此
$$
\boxed{
\alpha_A(0,x)^2=\langle B_1x,x\rangle
=\min_{\substack{\widehat c\ {
m 商裸低链}\\D\widehat c_1=x}}
\sum_{j=1}^{d-1}\langle W_{q+j}^{[j]}\widehat c_j,\widehat c_j\rangle.
}
\tag{5.5}
$$
各最小值存在，也可由原闭值域裸最小者删去首头直接看出。

在同一个给定段向量上，完整与裸的行图权差恰为
$$
\boxed{
\langle (W_{q+j}-W_{q+j}^{[j]})z,z\rangle
=\|P_{j,q+j+1}R_{q+j}az\|^2.
}
\tag{5.6}
$$
这是实际高出生返回，不能删除。两个变分域及最优链也不相同，所以 (5.6) 不声称两个最小费用之差等于右端的最小值。

## 6. 原负源图上的完整三费字典

令 $r=(r_0,x)$ 满足原真实负源条件
$$
P(L+B)r=0.
\tag{6.1}
$$
由 (3.1)–(3.2)，$r_0=r_0^*(x)$。设
$\kappa=\|R_qr_0\|^2=\langle Kr_0,r_0\rangle$。直接相乘得到向量身份
$$
\boxed{Lr=(-Kr_0,S^-x).}
\tag{6.2}
$$
因此所有费用均来自同一个原 $r$：
$$
\boxed{
\begin{aligned}
\mu_A(r)^2&=\langle S^-x,x\rangle-\kappa,\\
\alpha_A(r)^2&=\kappa+\langle B_1x,x\rangle,\\
\lambda_A(r)^2&=\kappa+\langle G_1^{-1}x,x\rangle,\\
\lambda_{{\rm flat},A}(r)^2
&=\kappa+\langle G_1S^-x,S^-x\rangle,\\
\chi_A(r)^2
&=2\kappa+\langle B_1x,x\rangle+
\langle G_1S^-x,S^-x\rangle.
\end{aligned}}
\tag{6.3}
$$
特别，商问题需要估计的左量是 (3.3) 的真正加权最小能量，而其右侧必须用 (5.5) 与 (4.4) 的真实度量。不能把 $S^-$ 换成无权小头 Gram，或把 $G_1^{-1}$ 换成 (5.5)。

## 7. 同一个实际顶部诱导加权商前缀最小者

令 $v^{\rm top}=E_{A,Q}^{\dagger}r_Q$ 为一个真正原顶部最小者。对每个 $p\le Q$，任意 $e_0$ 头的纯 primitive 向量都是支持 $\le Q$ 的原零源核。因此其首头 primitive 分量全部为零；整个第零头准确满足
$$
v^{\rm top}_{0,0}=0,\qquad
v^{\rm top}_{0,p+1}=-R_pa\widehat v^{\rm top}_p\quad(0\le p<Q).
\tag{7.1}
$$

取 $q+1\le Q$，令 $\widehat v=P_{\le q}\widehat v^{\rm top}$、
$x=\widehat A\widehat v^{\rm top}_q$。则
$$
\boxed{\widehat v\ \text{是 (3.3) 的真正加权最小者}.}
\tag{7.2}
$$
可由原负源流与 (3.3) 直接推出，也可作如下完整变分验证。任取
$\widehat z\in\widehat V_q$、$\widehat E_q\widehat z=0$。按 (2.2) 补第零头，再额外在孔 $q+1$ 加入
$-e_0R_qa\widehat z_q$；这个向量支持 $\le q+1$，且是原完整零源核。其最后源为零使用 $Ae_0=0$。与 $v^{\rm top}$ 正交，逐孔使用 (7.1)，恰给
$$
\sum_{p=0}^{q}\langle W_p\widehat v^{\rm top}_p,\widehat z_p\rangle=0.
\tag{7.3}
$$
这就是 (3.3) 的正规方程，证明 (7.2)。所以没有逐窗重新选来源或把原最小性偷换成无权商最小性。

## 8. 商的两种右测试仍由同一实际未来带支付

进一步取 $q+d\le Q$，令
$y=P_{[q+1,q+d]}v^{\rm top}$。其商头分量记为
$\widehat y_j=\widehat v^{\rm top}_{q+j}$，$1\le j\le d-1$。
这些实际向量不必落在第 $j$ 段右测试的缩短头旗；以下只与已经合法的测试链配对，不作此支撑假设。

对任意商完整链 $\widehat c$，其原补全 $I_f\widehat c$ 合法，并由 (7.1) 得
$$
\boxed{
\langle y,I_f\widehat c\rangle
=\sum_{j=1}^{d-1}
\langle W_{q+j}\widehat y_j,\widehat c_j\rangle.
}
\tag{8.1}
$$
第 $q+1$ 孔的第零头不贡献，因为补全链的 $c_{1,0}=0$；最后孔其余头也不贡献，因为原最后测试仅含第零头。对于合法商裸链，同理有
$$
\boxed{
\langle y,I_b\widehat c\rangle
=\sum_{j=1}^{d-1}
\langle W_{q+j}^{[j]}\widehat y_j,\widehat c_j\rangle.
}
\tag{8.2}
$$
这里利用 (5.3) 的正交投影，仍保所有 $a$ 的长跳项。

若 $\widehat c_f(z)$、$\widehat c_b(z)$ 分别为 (4.4)、(5.5) 对源 $z$ 的真正最小者，则原同未来带双投影和 (6.2) 给
$$
\boxed{
\sum_j\langle W_{q+j}\widehat y_j,\widehat c_f(z)_j\rangle
=\langle S^-x,z\rangle,
}
\tag{8.3}
$$
$$
\boxed{
\sum_j\langle W_{q+j}^{[j]}\widehat y_j,\widehat c_b(z)_j\rangle
=-\langle B_1x,z\rangle.
}
\tag{8.4}
$$
裸测试的负号和完整平坦测试的正号均保持。两式使用同一个 $\widehat y$，以及同一个原 $r$ 的 $S^-x$；没有独立更换平坦源。

此外，把 (7.1) 中落在未来带的首头分量与其商头一一配对，得到
$$
\sum_{j=1}^{d-1}\langle W_{q+j}\widehat y_j,\widehat y_j\rangle
\le\|y\|^2.
\tag{8.5}
$$
遗漏项仅是未来第一段首头和未来末段其余头的非负物理范数。故此加权未来量完全由原同一未来带支付，未引入额外的 $\|W_p\|$ 损失。

## 9. 准确剩余问题

本文把一次真实首头消元变成了一个保原源的具体加权问题：左负 Schur 与完整右费具有同一行图权，裸右费则恰少去 (5.6) 的高出生行图部分。对实际族，(7.2)、(8.3)–(8.5) 也保留了来源和累计未来能量。

仍未证明的是：这些真实 $W_p$、$W_{q+j}^{[j]}$ 及 $\widehat A$ 的组合，是否在实际规范类上满足原合法窗可承受的左／两右费比较。对 $R_p$ 直接取全层范数，或者递归时把每个 $W_p$ 当作标量，都可能产生过大的孔数损失；本文没有这样做。第二次消去头坐标时还必须保 $W_p$ 的真实头交叉块，不能当作又一个无权首头问题。

对天然四块退化头，§§2、4、5 的物理补全公式在合法天然源上仍可逐项使用，但 (1.4) 的商源满射及任意 $x$ 的变分域需要重新确认。本文的完整商定理仅声明于原 regular 头，未免费断言该退化商具有标准源旗。
