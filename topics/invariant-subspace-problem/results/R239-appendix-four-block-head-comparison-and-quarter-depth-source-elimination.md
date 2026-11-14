# R239 附录：原四块头比较、四分之一深度消元与全部自由头反馈

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：原完整四块头的范数比较、全部 primitive 延拓差、深度至少 $d/4+1$ 的实际右旗费用、同一平坦源/裸费 Schur 及扩大自由空间的准确反馈均已证明。最后两头列包含在该深度结论内。没有把环境模型当成原压缩，也没有把 $M$ 图残余或 Schur 最优深补全置零。普通 ISP 与 $N=M$ 均为 OPEN。

依赖：[直接 primitive 修正](R239-appendix-direct-primitive-correction-and-whole-dyadic-source-flags.md)，
[R271 原头四次幂界](R271-appendix-primitive-bandwidth-and-far-schur-localization.md)，
[R271 同一平坦源深 Schur](R271-appendix-deep-source-jet-schur-elimination-with-original-flat-cost.md)，
[R271 物理输出切分](R271-appendix-output-cut-schur-localization-and-larger-middle-band.md)。
本稿不依赖尚未完成的多高位导数锚消元。

## 1. 原四块空间及比较头

固定
$$
m\ge8,\qquad d=2^m,\qquad n=m-2,\qquad p=2^n=d/4,
\qquad4d\le q\le e^{d^3/4}.
\tag{1.1}
$$
把原头按 $e_{kp+\ell}$、$0\le k\le3$、$0\le\ell<p$ 识别为
$\mathbb C^4\otimes H_n$。这是物理正交重排，不改变原内积。

在 $\mathbb C^4$ 上，令两个 Boolean 删除算子为
$$
E_0e_1=e_0,\quad E_0e_3=e_2,\qquad
E_1e_2=e_0,\quad E_1e_3=e_1,
$$
其余基向量上为零。它们交换且平方为零。置
$$
b=b_n,\quad c=b_{n+1},\quad
D_{\rm hi}=bE_0+cE_1,\qquad b_j=(j+1)^{-2},
$$
$$
\boxed{A_\square=I_4\otimes A_n+D_{\rm hi}\otimes I_p.}
\tag{1.2}
$$
$A_n$ 是同一个原 $N$ 或 $Y$ 模型的真实低头；没有对它作等权或 Jordan 替换。

下面证明原 $A_m$ 与 (1.2) 的整个头算子范数差，而非只检查少数列。

## 2. 全部原权积及两高位的精确矩阵

### 2.1 低位跨块

对于 $i<n$，令 $\overline N_i=I_4\otimes N_i^{[n]}$。不跨每块底部的长度 $2^i$ 区间，其权积与低头完全相同。跨 $kp$、$k=1,2,3$ 的输入，准确把标准区间的一项 $\alpha_i$ 换成 $\alpha_{v_2(kp)}$，所以差的系数为
$$
\alpha_{v_2(kp)}/\alpha_i\le\alpha_n/\alpha_i\le\eta_{n-1}.
$$
不同输入的输出仍是不同标准基向量；故整体差是加权部分移位，并有
$$
\|N_i^{[m]}-\overline N_i\|
\le\alpha_n/\alpha_i\le\eta_{n-1}.
\tag{2.1}
$$
没有乘四个块或 $p$ 个列的数目。

对 $Y_i=N_i(I+N_i)^{-1}$，准确 resolvent 差公式及两侧逆范数小于 $3$ 给
$$
\|Y_i^{[m]}-I_4\otimes Y_i^{[n]}\|
\le9\alpha_n/\alpha_i.
\tag{2.2}
$$
因为 $\sum_{i<n}b_i<2$，两种模型的全部低位误差统一不超过
$18\eta_{n-1}$。

### 2.2 高位不是只有一条主耦合

记 $\eta=\eta_n$。原第 $n$ 位在四块上的准确矩阵是
$$
N_n^{[m]}=T\otimes I_p,\qquad
Te_1=e_0,\quad Te_2=\eta e_1,\quad Te_3=e_2.
\tag{2.3}
$$
相邻块底权积给中间系数 $\alpha_{n+1}/\alpha_n=\eta_n$；
也可由原 $N_n^2=\eta_nN_{n+1}$ 在第 $2p$ 列直接核对。

原第 $n+1$ 位准确为
$$
N_{n+1}^{[m]}=E_1\otimes I_p,\qquad
(N_{n+1}^{[m]})^2=0.
\tag{2.4}
$$
置 $V=e_1e_2^*$、$R=e_0e_3^*$。直接乘 (2.3) 给
$$
T=E_0+\eta V,\qquad T^2=\eta E_1,\qquad T^3=\eta R,\qquad T^4=0.
$$
所以 $N$ 模型的高位误差至多 $b\eta$；$Y$ 模型则准确为
$$
Y_n^{[m]}=(E_0+\eta V-\eta E_1+\eta R)\otimes I_p,
\qquad Y_{n+1}^{[m]}=E_1\otimes I_p,
\tag{2.5}
$$
其高位误差至多 $3b\eta$。

因此
$$
\boxed{
\mathcal E_A:=A_m-A_\square,\qquad
\|\mathcal E_A\|\le18\eta_{n-1}+3b\eta_n
\le24\eta_{n-1}.
}
\tag{2.6}
$$
这一计算同时保留高 $3p$ 块上的两条主项 $bU_{2p}+cU_p$，也保留 $Y$ 模型的两个额外小回返项。

## 3. 比较头的准确幂零阶与加权幂和

两个张量项在 (1.2) 中交换。$A_n^p=0$，而 $D_{\rm hi}^3=0$，所以
$$
\boxed{A_\square^{p+2}=0.}
\tag{3.1}
$$
最大可能非零次数为 $(p-1)+2=p+1$。

取与直接 primitive 修正稿相同的
$$
\mathcal L=512\sqrt{q+2d-1}(m+q+2d-1)^{3/2}<2048q^2.
$$
记
$$
\mathcal F_m=\sum_{v=0}^{d-1}(2\mathcal L)^v\|A_m^v\|,
\qquad
\mathcal F_n=\sum_{j=0}^{p-1}(2\mathcal L)^j\|A_n^j\|.
$$
该稿 §§2–3 已完整证明
$$
\mathcal F_m\le d\,e^{3d^4/20},\qquad
\mathcal F_n\le p\,e^{d^4/8}.
\tag{3.2}
$$
其输入仅为原四次幂界、$m/d\le1/32$ 及
$\log(12\mathcal L)<d^3/2+11$，在本窗口完全相同。

定义
$$
\mathcal F_\square
=\sum_{u=0}^{p+1}(2\mathcal L)^u\|A_\square^u\|.
$$
二项式公式、$\|D_{\rm hi}\|\le2$、$\|D_{\rm hi}^2\|\le2$ 给
$$
\begin{aligned}
\mathcal F_\square
&\le
[1+4\mathcal Lp+4\mathcal L^2p(p+1)]\,\mathcal F_n\\
&\le
\boxed{9\mathcal L^2(p+1)^2\,\mathcal F_n.}
\end{aligned}
\tag{3.3}
$$
第一行逐项来自
$\binom{j+1}{1}\le p$、
$\binom{j+2}{2}\le p(p+1)/2$、$0\le j\le p-1$；
所以这里没有漏掉两高位的混合项。

## 4. 全部 primitive 延拓的统一小差

在原 $\ker D_m$ primitive 坐标上使用同一组 $Q_0,\ldots,Q_{d-1}$，定义完整未截断延拓
$$
\mathcal E_m^{\rm full}a
=\sum_{k=0}^{d-1}(-A_m)^kQ_ka,\qquad
\mathcal E_\square^{\rm full}a
=\sum_{k=0}^{p+1}(-A_\square)^kQ_ka.
\tag{4.1}
$$
输入可以是所有头、所有孔层 $\le q$ 的任意 primitive 向量。由原相容族，其全部中间孔层在 $q+d-1$ 以下，所有 $Q_k$ 都在正确域内。

两个延拓都保 primitive 身份：
$P_0\mathcal E_m^{\rm full}a=P_0\mathcal E_\square^{\rm full}a=a$。
一个属于原 $(A_m+D_m)$ 核，另一个属于明确比较头 $(A_\square+D_m)$ 核；不将两核认成相同。

准确幂差
$$
A_m^k-A_\square^k
=\sum_{u+v=k-1}A_m^v\mathcal E_AA_\square^u
$$
与 $\|Q_k\|\le2^{k-1}\mathcal L^k$ 给
$$
\|\mathcal E_m^{\rm full}-\mathcal E_\square^{\rm full}\|
\le\mathcal L\|\mathcal E_A\|\mathcal F_m\mathcal F_\square.
$$
由 (2.6)、(3.2)–(3.3)，
$$
\boxed{
\|\mathcal E_m^{\rm full}-\mathcal E_\square^{\rm full}\|
\le216\,\eta_{m-3}\mathcal L^3dp(p+1)^2
e^{11d^4/40}.
}
\tag{4.2}
$$

原准确
$$
\log\eta_{m-3}
=-\frac{175}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d
$$
及 $\log\mathcal L\le d^3/2+\log2048$ 于是给
$$
\begin{aligned}
\log(\text{(4.2)右端})
\le{}&
-\frac{171}{2560}d^4+\frac{699}{256}d^3-\frac{75}{2}d\\
&+\log(216\cdot2048^3dp(p+1)^2).
\end{aligned}
\tag{4.3}
$$
当 $d\ge256$，
$$
\frac{171}{2560}-\frac{699}{256d}
\ge\frac{171}{2560}-\frac{699}{65536}
>\frac1{20}.
$$
最后对数至多为常数加 $4\log d$，小于 $(75/2)d$，故
$$
\boxed{
\|\mathcal E_m^{\rm full}-\mathcal E_\square^{\rm full}\|
\le\varepsilon_d:=e^{-d^4/20}.
}
\tag{4.4}
$$
这个界相对于原 primitive 输入的物理范数，适用于整个输入孔直和；没有孔层数 $q$ 的损失。

## 5. 深度 d/4+1 起的全部原右旗

记
$$
h=p+1=d/4+1,\qquad
\mathscr T_{\rm dp}
=\bigoplus_{h\le t\le d-2}
H_{\ge t+1}\otimes K_{q-t}.
\tag{5.1}
$$
任取 $a\in\mathscr T_{\rm dp}$。比较头延拓最多升 $p+1=h$ 个孔，而输入孔层至多为 $q-h$，故准确有
$$
P_{>q}\mathcal E_\square^{\rm full}a=0.
\tag{5.2}
$$
因此原完整右链
$$
\boxed{R_{\rm dp}a=-P_{>q}\mathcal E_m^{\rm full}a}
\tag{5.3}
$$
满足
$$
\|R_{\rm dp}a\|
\le\varepsilon_d\|a\|.
\tag{5.4}
$$

必须核对它属于原右旗，而不仅是环境右半向量。第 $k$ 项
$(-A_m)^kQ_ka$ 的尾核阶至多为 $k+1$，头指标至多为 $d-1-k$。若它出现在右段 $\ell\ge1$，则 $k\ge\ell$。因此
$$
d-i\ge k+1,\qquad i\le d-1-k\le d-\ell.
$$
所有逐头核阶和段号限制均成立。整核的内部零输出给
$R_{\rm dp}a\in\ker S_{\rm flag}$，最后一段至多为 $d-1$。由左右切分，
$$
\boxed{F_{\rm flag}R_{\rm dp}a=B_{\mathscr T}a=B_Ua.}
\tag{5.5}
$$
源是原实际源，且 $\Gamma_qB_Ua=a$。没有低锚，没有更改原 $q$，全部头方向——特别最后两列——都包括在 (5.1) 内。

## 6. 同一个原平坦源与裸费用的完整 Schur

沿 R271 原完整源 Schur 记
$$
\sigma=\Gamma_qr=(x,y),\qquad
x\in\mathscr T_{\rm sh}:=\bigoplus_{0\le t<h}H_{\ge t+1}\otimes K_{q-t},
\quad y\in\mathscr T_{\rm dp},
$$
$$
S=\mathcal G_q=
\begin{pmatrix}S_{00}&S_{01}\\S_{10}&S_{11}\end{pmatrix}\succeq I.
$$
令
$$
y_0=-S_{11}^{-1}S_{10}x,\quad z=y-y_0,\quad
\widehat S=S_{00}-S_{01}S_{11}^{-1}S_{10}.
\tag{6.1}
$$
这里 $\widehat S\succeq I$，且最优深补全 $y_0$ 一般非零。

对原同一个 $c^\flat=F_{\rm flag}^*J_q^{-1}r$，(5.5) 给
$$
\boxed{S_{11}z=R_{\rm dp}^*c^\flat.}
\tag{6.2}
$$
所以
$$
\boxed{
\mu(r)^2=\langle\widehat Sx,x\rangle+\langle S_{11}z,z\rangle,
\quad
\langle S_{11}z,z\rangle\le\varepsilon_d^2\lambda_{\rm flat}(r)^2.
}
\tag{6.3}
$$
两个合法源
$$
r_{\rm cut}=B_U(x,y_0),\qquad \delta r=B_U(0,z)
$$
有真正左正交分裂，且
$$
\boxed{
\mu(\delta r)\le\varepsilon_d\lambda_{\rm flat}(r),\qquad
\lambda(\delta r),\alpha(\delta r)
\le\varepsilon_d^2\lambda_{\rm flat}(r).
}
\tag{6.4}
$$

若 $R_{\rm sh}$ 是任一原完整右可行浅列，定义
$$
\widehat R=R_{\rm sh}-R_{\rm dp}S_{11}^{-1}S_{10}.
$$
那么保全部回馈的剩余方程是
$$
\boxed{\widehat Sx=\widehat R^*c^\flat(r).}
\tag{6.5}
$$
真正裸链也满足
$$
\|a_b(r)-a_b(r_{\rm cut})\|
\le\varepsilon_d^2\lambda_{\rm flat}(r).
\tag{6.6}
$$
没有声称新源 $r_{\rm cut}$ 的 $\lambda_{\rm flat}$ 被原值控制。可用的是 (6.5) 的同一个原 $c^\flat$。

## 7. 同一深度的 M 源旗也可一次支付

令 $\Delta=\Gamma_q(P\mathscr R_q)$ 为全部最小头对角，并将深列中与 $\Delta$ 重合部分删去后记为 $\mathscr Y$。对 $a\in\mathscr Y$，(5.3)–(5.5) 给纯坐标源、没有锚，且右链范数至多 $\varepsilon_d\|a\|$。

因此此前单高块源旗的准确论证直接给
$$
\boxed{
\mathscr X=\Gamma_q^{-1}(\Delta+\mathscr T_{\rm dp}),
\qquad
\mu(r)^2\le(2-\varepsilon_d^2)^{-1}\chi(r)^2
\quad(r\in\mathscr X).
}
\tag{7.1}
$$
可以一次作真正 $M=B+LGL$ 投影，保 $\chi^2$ 的 Pythagoras 和实际 $w$ 的强极限。余条件仍是
$$
P_{\Delta+\mathscr T_{\rm dp}}\Gamma_q^{-*}M\widehat r=0,
\tag{7.2}
$$
不能改成 primitive 支撑为零。§6 的左 Schur 与本节的 $M$ 投影是两种不同操作；不能无证明地同时保两套正交条件。

## 8. 消深后全部自由头的准确反馈

令 $\mathscr P_q$ 为原全部 primitive 坐标。原自由空间为 $\mathscr F=\ker\mathcal B$，其正交补是强制空间 $\mathscr T$。在 §6 固定浅 $x$ 而最小化所有深源时，原全部自由坐标仍一同最小化。因此总自由空间准确扩大为
$$
\boxed{\mathscr F_{\rm new}=\mathscr F\oplus\mathscr T_{\rm dp}
=\mathscr P_q\ominus\mathscr T_{\rm sh}.}
\tag{8.1}
$$
它包含所有孔层 $n\le q-h$ 的全部头，及顶部带内原本自由的头；并不只有“中段自由头”。

写原截断延拓
$$
\mathcal E=P_{\le q}\mathcal E_m^{\rm full}=I+\mathcal C_L,
$$
并按 $\mathscr F_{\rm new}\oplus\mathscr T_{\rm sh}$ 记
$C_F=\mathcal C_L|_{\mathscr F_{\rm new}}$、
$C_T=\mathcal C_L|_{\mathscr T_{\rm sh}}$。
因为 $P_0\mathcal C_L=0$，§6 的剩余最小前驱可以等价地准确写为
$$
\boxed{
p_{\rm cut}=x+f(x),\qquad
f(x)=-(I+C_F^*C_F)^{-1}C_F^*C_Tx,
\qquad
v_{\rm cut}=\mathcal E p_{\rm cut}.
}
\tag{8.2}
$$
这是完整自由空间最小化与深源 Schur 的结合律。验证只需在同一仿射空间 $x+\mathscr F_{\rm new}$ 中最小化
$\|p\|^2+\|\mathcal C_Lp\|^2$，其唯一正规方程就是 (8.2)。

R271 物理中段深度至少 $3d/8$，而 $h=d/4+1\le3d/8$。所以其**全部** primitive 头，包括此前强制及自由部分，都属于 $\mathscr F_{\rm new}$。其准确反馈为
$$
\boxed{
b_{\rm mid}(r_{\rm cut})=\mathcal K_{\rm mid}x,\qquad
\mathcal K_{\rm mid}
=-P_{\rm mid}(I+C_F^*C_F)^{-1}C_F^*C_T.
}
\tag{8.3}
$$
它不等于零。唯一不带新条件数的普遍界只是
$$
\|(I+C_F^*C_F)^{-1}C_F^*\|\le\tfrac12,
\qquad
\|\mathcal K_{\rm mid}x\|\le\tfrac12\|C_Tx\|.
\tag{8.4}
$$
目前 (8.4) 未支付 $C_T$ 在实际浅源上的温和费用。

令 $\mathcal T_{\rm out}$ 是 R271 物理输出切分的同一个低部重建算子。对合法 $r_{\rm cut}$，
$$
u(r_{\rm cut})
=\mathcal T_{\rm out}\mathcal K_{\rm mid}x+\epsilon_{\rm out},
\qquad
\|\epsilon_{\rm out}\|\le\varepsilon_d\|\nu(r_{\rm cut})\|.
\tag{8.5}
$$
对差源 $\delta r$ 再用同一个式子及 (6.4)，得到
$$
\boxed{
\|\mathcal T_{\rm out}[b_{\rm mid}(r)-\mathcal K_{\rm mid}x]\|
\le(1+\varepsilon_d)\varepsilon_d\lambda_{\rm flat}(r).
}
\tag{8.6}
$$
这里没有乘 $\|\mathcal T_{\rm out}\|$，也没有换平坦源。

因此剩余的实际中段问题可准确集中到
$\mathcal T_{\rm out}\mathcal K_{\rm mid}x$，
同时保留 (6.5) 的同源对偶方程和 (6.6) 的真实裸项。
一个足够的后继估计是对这些同源三元组证明
$$
\langle\widehat Sx,x\rangle
\le C_m\bigl(\|a_b(r_{\rm cut})\|^2+\|c^\flat(r)\|^2\bigr)
$$
达到已有窗口求和门槛；或相应控制 (8.5) 的实际重建量。
本稿未证明该估计。

## 9. 比较头可用于自由反馈，但不能省去自由最小化

(4.4) 还给同一个全部 primitive 空间上的
$$
\|\mathcal E-\mathcal E_\square\|\le\varepsilon_d,
\qquad \mathcal E_\square=P_{\le q}\mathcal E_\square^{\rm full}.
$$
两者的 primitive 投影都是恒等，故都以下界一有界。固定浅 $x$，在相同仿射空间
$x+\mathscr F_{\rm new}$ 内分别最小化 $\|\mathcal E p\|$ 和
$\|\mathcal E_\square p\|$，记最小值 $\mu,\mu_\square$，最小者 $p,p_\square$。则
$$
\boxed{(1+\varepsilon_d)^{-1}\mu
\le\mu_\square\le(1+\varepsilon_d)\mu.}
\tag{9.1}
$$
证明：同一 $p$ 代入另一延拓的费用至多增加
$\varepsilon_d\|p\|\le\varepsilon_d$ 乘原费用；双向取 inf 即得。

令 $v=\mathcal E p$、$v_\square=\mathcal E_\square p_\square$。
根代理进一步给出不损失平方根的直接正规方程证明，核验如下。
置
$$
D_E=\mathcal E_\square-\mathcal E,\qquad
q_0=p_\square,\qquad \delta p=q_0-p\in\mathscr F_{\rm new}.
$$
原最小性给
$$
\|\mathcal E\delta p\|^2
=\langle\mathcal E q_0,\mathcal E\delta p\rangle.
$$
模型最小性则给
$\langle\mathcal E_\square q_0,\mathcal E_\square\delta p\rangle=0$。
两式相减，准确得到
$$
\|\mathcal E\delta p\|^2
=-\langle\mathcal E_\square q_0,D_E\delta p\rangle
-\langle D_Eq_0,\mathcal E\delta p\rangle.
$$
两种延拓都以下界一有界，所以
$\|\delta p\|\le\|\mathcal E\delta p\|$、
$\|q_0\|\le\|\mathcal E_\square q_0\|=\mu_\square$。于是
$$
\|\mathcal E\delta p\|^2
\le2\varepsilon_d\mu_\square\|\mathcal E\delta p\|,
\qquad
\|\mathcal E\delta p\|\le2\varepsilon_d\mu_\square.
$$
再加上 $\|D_Eq_0\|\le\varepsilon_d\mu_\square$，得到
$$
\boxed{
\|v-v_\square\|
\le3\varepsilon_d\mu_\square
\le3\varepsilon_d(1+\varepsilon_d)\mu,
\qquad
\|p-p_\square\|\le2\varepsilon_d(1+\varepsilon_d)\mu.
}
\tag{9.2}
$$
这把实际扩大自由最小化以 $O(\varepsilon_d)$ 的物理及坐标误差稳定运输到明确的四块模型，费用不包含整个延拓的大条件数。

但模型的仿射约束仍是同一个
$x+\mathscr F_{\rm new}$，由原头物理浅旗决定。
不能将它擅自换成比较头自身的一套天然源旗，也不能仅因 $A_\square^{p+2}=0$ 就断言 (8.3) 的自由反馈消失。低部重建、原裸项及同一 $c^\flat$ 之间的剩余估计继续保留。
