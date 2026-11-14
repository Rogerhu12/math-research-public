# R271 附录：原 dyadic 源头的出生一修复与明确增长的真实余商

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本稿把既有向左头右逆应用到整个出生一零首源修正，并只对一个真实 dyadic 头块支付一次平衡 Jordan 相似。对所有原源
$r\in\mathscr R_q\cap F_H$，$H=2^n\le d/2$、$n\ge5$，得到
$\lambda(r)\le8e^{20H^4}\alpha(r)$；实际上完整费用由同源真幂底项的平方根控制。

因此在原 $d=2^m$、$Q=\lfloor e^{d^3/4}\rfloor$ 窗中，可明确取
$H=2^{\lfloor3m/4-2\rfloor}$，即 $d^{3/4}$ 量级的整个前缀源头。
其真正两费好顶部投影保同一实际源流、固定 $W$ 的左逼近及完整顶部右费差，费用均有严格指数余量。残源仍只满足真实 $M_2$ 正交条件。

依赖：[R249 真实平衡 Jordan 相似](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)、[全部孔数高旗向左右逆](R271-appendix-all-hole-high-birth-right-inverse-and-return-energy.md)、[同源真幂底项](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)、[任意固定原头旗](R271-appendix-every-fixed-original-head-flag-and-paid-backward-head-completion.md)、[真实两费好顶部投影](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md)。

向左头解法及全孔高旗右逆已经在所引旧稿证明；本稿新增的是包含首段 primitive 的完整出生一修正、整个原前缀源旗与原真幂底项的比较，以及 $H\asymp d^{3/4}$ 的实际窗口费用。没有重登旧全头高旗定理。普通 ISP 与原 $N=M$ 仍 OPEN。

## 1. 两个真实头尺度与原源尾旗

固定原 $m$、$d=2^m$、$A=A_m$、$D=D_m$，并取
$$
5\le n<m,\qquad H=2^n,\qquad
F_k=\operatorname{span}(e_0,\ldots,e_{k-1}).
$$
原嵌套给 $A_m|_{F_H}=A_n$，两者都指同一种 $N$ 或 $Y$ 模型。
定义原源旗
$$
\boxed{
\mathscr E_{H,q}
=\mathscr R_q\cap(F_H\otimes\mathcal H_q)
=\bigoplus_{i=0}^{H-1}e_iE_{d-i-1,q}.
}
\tag{1.1}
$$
尾核阶仍是原 $d-i-1$，没有改成小头问题的 $H-i-1$。
特别，本稿包括前缀最高头 $e_{H-1}$ 的全部合法原尾源。

写
$$
\nu_m=\|D_m\|\le m^{-1}<1,\qquad
V_t=(D^t:\mathcal H_{q+t}\to\mathcal H_q)^\dagger.
$$
这些是完整孔层上真正幂的 MP 逆。对 $r\in\mathscr E_{H,q}$ 置
$$
b_t=(-1)^{t-1}V_tA^{t-1}r\quad(1\le t\le H),\qquad
b_t=0\quad(t>H).
\tag{1.2}
$$
原真幂底项定理给
$$
\boxed{
\|b\|^2=\sum_{t=1}^{H}\|V_tA^{t-1}r\|^2\le\alpha(r)^2.
}
\tag{1.3}
$$
每个 $b_t$ 保原最大尾旗，且
$$
b_t\in F_{H-t+1}\otimes\mathcal H_{q+t},\qquad
b_t\perp\mathbb C^d\otimes E_{t,q+t}.
\tag{1.4}
$$

## 2. 真幂链的全部残量属于出生至少一

记内部残量
$$
y_t=Ab_t+Db_{t+1}\qquad(1\le t<d).
$$
由于 $A^Hr=0$，只有 $1\le t\le H-1$ 可能非零。
由 (1.2)，
$$
D^tAb_t=(-1)^{t-1}A^tr,\qquad
D^{t+1}b_{t+1}=(-1)^tA^tr.
$$
两项相消，所以准确有
$$
\boxed{
y_t\in F_{H-t}\otimes E_{t,q+t}\quad(1\le t\le H-1).
}
\tag{2.1}
$$
这里仅需真实幂原像身份；不把各层受限伴随桥独立放大。
在原尾两带结构中 $y_t$ 事实上位于出生一，但下面直接修复较大的 (2.1) 空间。

原物理内部算子是对角头作用与段移删除之和，故
$$
\boxed{\|y\|=\|Sb\|\le(\|A_m\|+\nu_m)\|b\|<7\|b\|.}
\tag{2.2}
$$
因此这个修复源的全部原范数已经由同一个真幂底项支付。

## 3. 含首段 primitive 的完整向左修正

把 R249 的小头相似记为
$$
A_n=\Sigma_n(\gamma_nJ_H)\Sigma_n^{-1},\qquad
J_He_i=e_{i-1},\quad J_He_0=0,
$$
$$
\gamma_n=e^{20-\mathcal L_n},\qquad
\mathcal L_n=\frac{25H^4}{2(H-2)},\qquad
\mathfrak k_n=\|\Sigma_n\|\,\|\Sigma_n^{-1}\|.
\tag{3.1}
$$
$\Sigma_n$ 与其逆都是原物理坐标中的上三角矩阵，所以保每个 $F_k$；
它们仅作用头，不改变原尾核阶。

先取只有第 $s$ 行非零的 $y^{[s]}$，$1\le s\le H-1$，
令 $\widetilde y_s=\Sigma_n^{-1}y_s$。
定义修正输入
$$
\boxed{
v_{s-k}^{[s]}
=(-1)^k\gamma_n^{-k-1}
\Sigma_n(J_H^*)^{k+1}D^k\widetilde y_s,
\qquad0\le k\le s-1.
}
\tag{3.2}
$$
其余段为零。与旧高出生右逆相比，这里包含了 $s-k=1$ 的首段。

令 $t=s-k$。由 (2.1)，原头与尾支撑分别给
$$
(J_H^*)^{k+1}F_{H-s}\subseteq F_{H-t+1},
\qquad
D^kE_{s,q+s}\subseteq E_{t,q+t}.
$$
因此
$$
\boxed{
v_t^{[s]}\in F_{H-t+1}\otimes E_{t,q+t}.
}
\tag{3.3}
$$
其最大物理头为 $H-t\le d-t$，满足原第 $t$ 段头旗；
对每个头 $i\le H-t$，有 $t\le d-i$，故最大尾核旗也满足。
这一步直接在原宽度 $d$ 中检查，没有套用小头源尾阶。

有限头没有溢出，故
$$
Av_s^{[s]}=y_s,\qquad
Av_t^{[s]}=-Dv_{t+1}^{[s]}\quad(1\le t<s).
\tag{3.4}
$$
首源尤其保持：
$$
\boxed{
Dv_1^{[s]}
=(-1)^{s-1}\gamma_n^{-s}
\Sigma_n(J_H^*)^sD^s\widetilde y_s=0,
}
\tag{3.5}
$$
因为 $y_s\in E_{s,q+s}$。
这准确支付了原最左端；不是删掉该方程。
末段 $H$ 及之后的修正均为零，所以末端也无剩余。

令
$$
\mathcal Q^{(1)}_{n,m,q}y=\sum_{s=1}^{H-1}v^{[s]}.
$$
由上述逐项等式，
$$
\boxed{
S\mathcal Q^{(1)}_{n,m,q}y=y,\qquad
F\mathcal Q^{(1)}_{n,m,q}y=0.
}
\tag{3.6}
$$
它是显示空间 (2.1) 上的完整零首源修正，不是纯高输入右逆。
其首段一般非零，但严格 primitive。

## 4. 只支付一次真实平衡相似的完整范数

按 (3.2) 的同一 $k$ 分组，原输出段 $s$ 被送至输入段 $s-k$；
这个段号映射单射，因此每组保正交平方和。
再对不同 $k$ 作三角不等式，得到
$$
\boxed{
\|\mathcal Q^{(1)}_{n,m,q}\|
\le\Gamma^{(1)}_{n,m}
:=\mathfrak k_n
\sum_{k=0}^{H-2}\gamma_n^{-k-1}\nu_m^k
\le H\mathfrak k_n\gamma_n^{-(H-1)}.
}
\tag{4.1}
$$
全部相似只产生一个 $\mathfrak k_n$，没有每递归一次再乘它。

R249 的准确预算为
$$
\log\mathfrak k_n\le
\mathcal L_n(H-1)-\omega_{H-1}
+H\log12+2\log H,
$$
$$
\omega_{H-1}
=\frac{20}{3}H^4-15H^3+(150n-275)H+\frac{850}{3}.
\tag{4.2}
$$
将 (3.1)、(4.2) 代入 (4.1)，保全部低阶项得到
$$
\begin{aligned}
\log\Gamma^{(1)}_{n,m}
\le{}&
\left(\frac{55}{3}+\frac{25}{H-2}\right)H^4+15H^3\\
&-(150n-255-\log12)H-\frac{790}{3}+3\log H.
\end{aligned}
\tag{4.3}
$$
当 $H\ge32$、$n\ge5$，第二行严格为负，而
$$
\frac{55}{3}+\frac{25}{H-2}+\frac{15}{H}
\le\frac{55}{3}+\frac{25}{30}+\frac{15}{32}
=\frac{1885}{96}<20.
$$
因此
$$
\boxed{\Gamma^{(1)}_{n,m}\le e^{20H^4}.}
\tag{4.4}
$$
本节用的是原真实 $N/Y$ 头相似，不是任意头维数的统一 Jordan 条件数假设。

## 5. 完整费用由同源真幂底项控制

对 (2.1) 的实际 $y=Sb$ 取
$v=\mathcal Q^{(1)}_{n,m,q}y$。则
$$
\boxed{c=b-v}
\tag{5.1}
$$
是一条原完整合法同源链。

由 (1.4)、(3.3)，每段 $b_t$ 与 $v_t$ 正交。因此
$$
\lambda(r)^2\le\|c\|^2
=\|b\|^2+\|v\|^2
\le[1+49(\Gamma^{(1)}_{n,m})^2]\|b\|^2.
$$
结合 (1.3)、(4.4)，得到主结论
$$
\boxed{
\lambda(r)^2
\le[1+49e^{40H^4}]
\sum_{t=1}^{H}\|V_tA^{t-1}r\|^2
\le64e^{40H^4}\alpha(r)^2.
}
\tag{5.2}
$$
特别可取
$$
\boxed{C_H=8e^{20H^4},\qquad
\lambda(r)\le C_H\alpha(r)
\quad(r\in\mathscr E_{H,q}).}
\tag{5.3}
$$
整个原前缀旗中的任意源尾核阶及线性组合均包括在内。

(5.1) 允许改变低域，故其高能量界属于真正完整最小费用，
不推出固定裸最小候选的
$\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|$
有同一估计。出生一修正中的首 primitive 正是不能免费去掉的一部分。

## 6. 合法窗中明确可付的 $d^{3/4}$ 头宽

现在令 $m\ge10$、$d=2^m$，取
$$
Q_m=\lfloor e^{d^3/4}\rfloor,\qquad
n_m=\left\lfloor\frac{3m}{4}-2\right\rfloor,\qquad
H_m=2^{n_m}.
\tag{6.1}
$$
则 $5\le n_m<m$，并有
$$
\boxed{\frac{d^{3/4}}8<H_m\le\frac{d^{3/4}}4.}
\tag{6.2}
$$
记 $K_m$ 为真实好顶部定理中终端半窗的不交未来带个数，
可取
$$
K_m\ge\frac{Q_m}{4d}\ge\frac{e^{d^3/4}}{8d}.
\tag{6.3}
$$
这些切口仍在原合法窗中，没有扩大有限核 lift 的范围。

由 $H_m^4\le d^3/256$ 与 (5.3)，
$$
\boxed{
\frac{C_{H_m}^2}{K_m}
\le512d\exp\!\left(-\frac{3d^3}{32}\right).
}
\tag{6.4}
$$
因此不只是 $C_{H_m}^2\le K_m$，还保留明确的严格指数余量。
同样
$$
\boxed{
\frac{C_{H_m}}{K_m}
\le64d\exp\!\left(-\frac{11d^3}{64}\right).
}
\tag{6.5}
$$

## 7. 真正两费投影保全部实际来源费用

令原实际族的终端尾预算为 $\varepsilon_m\to0$。
真实好顶部定理选出一个
$b\in[Q_m/2,Q_m-d]$，使
$$
\Xi_b(r_b)^2\le\frac{2\varepsilon_m^2}{K_m},
\qquad
\Xi_b(r)^2=\alpha_b(r)^2+\lambda_{{\rm flat},b}(r)^2.
$$
所有费用仍属于同一个原源，且
$$
M_{2,b}=B_b+L_bG_bL_b
$$
使用原裸、左、完整右三个真实 Gram。

在原真实负图 $\mathscr N_b$ 中取
$$
Z_b=\mathscr E_{H_m,b}\cap\mathscr N_b,\qquad
p_b=P_{Z_b}^{M_{2,b}}r_b,\qquad r_b'=r_b-p_b.
\tag{7.1}
$$
由 (5.3) 和同源
$\mu_b(p)^2\le\lambda_b(p)\lambda_{{\rm flat},b}(p)$，
$$
\Xi_b(r_b')^2+\Xi_b(p_b)^2=\Xi_b(r_b)^2,
$$
$$
\mu_b(p_b)^2\le
\frac{C_{H_m}\varepsilon_m^2}{K_m},\qquad
\lambda_b(p_b)\le
\frac{\sqrt2 C_{H_m}\varepsilon_m}{\sqrt{K_m}}.
\tag{7.2}
$$
将 (6.4)–(6.5) 代入，得到完整物理费用
$$
\boxed{
\mu_b(p_b)\le
8\sqrt d\,e^{-11d^3/128}\varepsilon_m,\qquad
\lambda_b(p_b)\le
32\sqrt d\,e^{-3d^3/64}\varepsilon_m.
}
\tag{7.3}
$$
第一项控制原顶部左最小像的改变量，第二项控制完整顶部右最小链的改变量。
它们都不要求未知实际尾有额外衰减率。

按已证好顶部定理，从
$E_b^\dagger r_b'=E_b^\dagger r_b-E_b^\dagger p_b$
重建全部截断，仍为同一相容残源流，保固定 $w$ 的左逼近，
全部 primitive 增量、MP 反馈和累计未来两费均被原预算加 (7.3) 支付。
没有逐窗另选来源。

精确余条件为
$$
\boxed{
r_b'\in\mathscr N_b,\qquad
\langle M_{2,b}r_b',z\rangle=0
\quad(z\in\mathscr E_{H_m,b}\cap\mathscr N_b).
}
\tag{7.4}
$$
本稿没有把 (7.4) 换成前 $H_m$ 个源坐标全零，也不把较低各窗分别投影。

## 8. 所得宽度与未完成部分

(6.2) 把既有慢增固定头删除落实为 $d^{3/4}$ 量级的整个原前缀。
它仍小于全源所需的 $d-1=2^m-1$ 个物理头。

原 $M_{2,b}$、真实负图、左最小逆均随 $m,b$ 改变。
因此 (7.4) 不能仅凭普通坐标稠密性推出固定非零 $w$ 不存在。
真正余流的测试源及其原度量控制仍须继续支付。
原纯 $S_H^\dagger$ 窄源界也未由这个允许首 primitive 变化的构造得到。
