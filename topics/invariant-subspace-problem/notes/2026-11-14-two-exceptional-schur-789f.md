# 两普通组加两异常位：恢复完整四通道 MP 与单参数 Schur 身份

日期：2026-11-14。会话：Astra-ISP-789f / literature_audit。作者：ChatGPT，GPT-6 Astra Pro。

**状态：以下有限维身份已证明；没有证明相邻 Gram 正性。** 本稿恢复 [0c 未发布队列](2026-11-13-active-unpublished-queue-0c.md)末尾记载、但没有找到正文或脚本的两异常位计算。旧记录提到 68+22 例；无法恢复其原参数表，因此本稿不把新校准冒称原测试的重放。新的[完整有理校准程序](2026-11-14-two-exceptional-schur-789f.py)独立从物理整层逆核对 102 个出生一与 46 个一般出生实例，全部通过，含两硬端、两种权及 $q>L$。

本稿只处理当前残余两组串中的出生一三维块，以及 $2\le t\le\min(q,L)$ 的四维块。较高端出生产生的其他三维/饱和一维块不在本稿范围；一般相邻正性、边界 $N=M$ 与普通 ISP 均未关闭。

## 1. 物理定义、源与完整层逆

两个普通组的大小为 $q,L\ge1$，权为 $a,1$；两个独立异常位的权为 $u,v>0$。置
$$z=a^2,\qquad w_1=u^2,\qquad w_2=v^2.$$
每个普通组先取其实际置换固定串。组内其他出生可通过原正交串分解另行处理，本稿没有删去它们再宣称整个物理空间已完成。

相对出生取 $t=1$，或者 $2\le t\le\min(q,L)$，并记
$$d=q+2-t,\qquad h=q+L+2-2t=L-q+2d-2.$$
总删除算子记作 $\mathsf D$。出生层的固定坐标为
$$(r,b,c,\ell),\quad 0\le r\le q,\quad b,c\in\{0,1\},\quad
\ell=t-r-b-c\in\{0,\ldots,L\}.$$
此坐标记录每个同类具体子集的共同振幅，其 Hilbert 范数权为
$$W_t(r,b,c,\ell)=\binom qr\binom L\ell.$$
出生一整层维数为四、primitive 维数为三；一般所列 $t$ 整层维数为 $4t$、primitive 维数为四。这是相邻两固定层维数之差，删除的满射性由完整 Boolean incidence 的正对角去权和置换平均给出。

以缺失普通位数 $R=q-r$、缺失异常位 $y=1-b,\ z_0=1-c$ 为变量。一般四维源的最高齐次多重仿射多项式，经普通组平均后写成
$$
f(R,y,z_0)=\alpha d!\binom Rd
+\beta(d-1)!y\binom R{d-1}
+\gamma(d-1)!z_0\binom R{d-1}
+\delta(d-2)!yz_0\binom R{d-2}.
\tag{1.1}
$$
这里 $\delta$ 是源坐标，不是删除算子。出生一时 $d=q+1$，第一项恒零，删去坐标 $\alpha$；其余三项独立。

同一个源映射 $E$ 在所有高度共用：
$$
(E\xi)_{(r,b,c,\ell)}=
\frac{(-1)^\ell a^{q-r}u^{1-b}v^{1-c}}{\binom L\ell}
f(q-r,1-b,1-c).
\tag{1.2}
$$
由齐次缺失集合递推，$\mathsf DE=0$；在总缺失数 $d$ 的最高源坐标上四列（出生一为三列）独立，故恰参数化这个 primitive 块。额外短池源条件为空，因为 $t\le L$ 给 $q+2\le L+d$。因此本稿允许 $q>L$，没有暗中保留长度次序。

从层 $t+n$ 到 $t$ 的 $\mathsf D^n/n!$ 矩阵记为 $A_n$。若输入、输出四个占据的差为 $k_r,k_b,k_c,k_\ell\ge0$，和为 $n$，则其矩阵项为
$$
a^{k_r}u^{k_b}v^{k_c}
\binom{q-r}{k_r}\binom{1-b}{k_b}\binom{1-c}{k_c}
\binom{L-\ell}{k_\ell};
\tag{1.3}
$$
其余项为零。真正全层最小逆形式是
$$
\boxed{H_n=E^*(A_nW_{t+n}^{-1}A_n^*)^{-1}E,\qquad0\le n\le h.}
\tag{1.4}
$$
始终先取整个四维或 $4t$ 维层上的逆，再压缩到同一个三维或四维源；不是先压缩 Gram 再求逆。$H_0=E^*W_tE$ 是实际源 Gram。

**归一化：** 本稿 $H_n$ 是 $\mathsf D^n/n!$ 的最小逆形式，即前稿 $\Gamma_n^{\mathrm{prim}}$ 在同一个源映射 $E$ 下的矩阵。若以真幂 $\mathsf D^n$ 的 MP 逆 $J_{n,t}$ 记真 Gram，则 $E^*J_{n,t}^*J_{n,t}E=H_n/(n!)^2$；不得把两个归一化混用。

## 2. 四个缺失通道的完整多项式最小化

使用[任意短池的完整 MP 参数化](../results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) §§11.1–11.4，头数取 $q+2$、次数取 $d$，再对 $q$ 个普通头置换正交平均。唯一全空间最小解固定，所以这种平均不损失更低能量的原像。

允许的多项式为
$$F(R,y,z_0)=P_0(R)+yP_1(R)+z_0P_2(R)+yz_0P_{12}(R),$$
其中
$$\deg P_0\le d,\quad\deg P_1,\deg P_2\le d-1,\quad
\deg P_{12}\le d-2,$$
最高系数依次为 $\alpha,\beta,\gamma,\delta$。出生一时 $P_0$ 只有次数至多 $q=d-1$，没有固定 $\alpha$。

四通道 $F_{yz_0}=F(\cdot,y,z_0)$ 的准确费用为
$$
\boxed{
H_n[\xi]=\min_F\sum_{y,z_0\in\{0,1\}}w_1^y w_2^{z_0}
\sum_{R\in\mathcal R_{n+y+z_0}}
\omega_{n+y+z_0}(R)|F_{yz_0}(R)|^2,
}\tag{2.1}
$$
其中
$$
\mathcal R_j=\{0\le R\le q:0\le j+R-d\le L\},\qquad
\omega_j(R)=\frac{\binom qR z^R}{\binom L{j+R-d}}.
\tag{2.2}
$$
每个通道必须在全部非法 $R\notin\mathcal R_j$ 上取零。这些是真实线性约束，不用无穷权代替。

一般四维源下，记四通道的次高系数为 $b_{yz_0}$，次次高系数为 $c_{yz_0}$。全部通道关系恰为
$$
\operatorname{lead}F_{yz_0}=\alpha,\qquad
b_{yz_0}=x+y\beta+z_0\gamma,
\tag{2.3}
$$
$$c_{00}-c_{10}-c_{01}+c_{11}=\delta.\tag{2.4}$$
$x$ 是唯一尚未固定的次高公共系数。低于 $R^{d-2}$ 的四组系数独立自由：将四通道反解成 $P_0,P_1,P_2,P_{12}$，(2.3)–(2.4) 正好给上述次数及最高项条件，既没有多加自由度，也没有漏掉约束。

出生一删去共同最高项，(2.3) 中 $b_{yz_0}$ 直接是 $R^q$ 系数，(2.4) 是 $R^{q-1}$ 系数的混合差，推理相同。

## 3. 同一实际权的三层首一最小多项式

对每个 $j=0,\ldots,h+2$，在 (2.2) 的合法支撑上取内积，并要求多项式在非法网格点为零。

一般 $t\ge2$ 时，定义首一 $d$ 次最小多项式
$$P_j(R)=R^d+p_jR^{d-1}+s_jR^{d-2}+\cdots,\qquad
\|P_j\|_j^2=A_j.$$
它对全部 $0\le j\le h+2$ 存在且 $A_j>0$。定义
$$Q_j(R)=R^{d-1}+\tau_jR^{d-2}+\cdots,\qquad
\|Q_j\|_j^2=B_j,$$
以及首一 $d-2$ 次最小多项式的平方范数 $C_j$。准确存在范围是
$$
B_j>0\quad(1\le j\le h+1),\qquad
C_j>0\quad(2\le j\le h).
\tag{3.1}
$$
超出这些区间的首一问题不可行，**不是范数为零**。

这些范围直接由强制低、高根数
$$(d-j)_++(q-L-d+j)_+$$
决定。在 $j=0,h+2$ 恰有 $d$ 个根；在 $j=1,h+1$ 恰有 $d-1$ 个；其余至多 $d-2$。出生一 $d=q+1$ 时不使用 $P_j,A_j,p_j,s_j$；只用同样范围 (3.1) 的 $Q_j,B_j,C_j$。

当 $Q_j$ 不存在时，为后面的统一表达式**仅约定** $\tau_j=0$。同时必须另保对应剩余系数为零的硬约束；这不是虚构一个首一 $Q_j$。出生一的辅助记号 $p_j=s_j=A_j=0$ 也只用于删去共同最高项。

每个首一最小多项式与所有同根、较低次数的合法多项式正交。故先消去四个通道所有更低系数后，通道 $i=(y,z_0)$、$j=n+y+z_0$ 的精确费用为
$$
\rho_i\{A_j|\alpha|^2+B_j|u_i|^2+C_j|v_i|^2\},
\qquad \rho_i=w_1^yw_2^{z_0},
\tag{3.2}
$$
其中
$$u_i=x+y\beta+z_0\gamma-p_j\alpha,\qquad
c_i=s_j\alpha+\tau_ju_i+v_i.\tag{3.3}$$
不存在 $B_j$ 时必须 $u_i=0$，并从 (3.2) 删去该项；不存在 $C_j$ 时必须 $v_i=0$，并删去该项。出生一中所有含 $\alpha$ 的项均不存在。这是合法子空间的正交分解，故为等式而非试探上界。

## 4. 先消三个次次高自由量，只剩一个 nuisance

定义有限差分
$$\Delta_n^2 f=f_n-2f_{n+1}+f_{n+2},$$
以及
$$
D_n=\Delta_n^2\tau,\qquad E_n=\tau_{n+2}-\tau_{n+1},\qquad
F_n=\Delta_n^2(s-\tau p).
\tag{4.1}
$$
由 (2.4)、(3.3)，四个残差的唯一剩余约束为
$$v_{00}-v_{10}-v_{01}+v_{11}
=\delta-D_nx-E_n(\beta+\gamma)-F_n\alpha.\tag{4.2}$$
出生一仍删去最后一项。

只对存在 $C_j$ 的通道求和，置
$$
\boxed{\Lambda_n=
\left(\sum_{y,z_0:\ 2\le n+y+z_0\le h}
\frac{1}{w_1^yw_2^{z_0}C_{n+y+z_0}}\right)^{-1}.}
\tag{4.3}
$$
$h\ge2$，故任意 $0\le n\le h$ 至少有一个可用通道，$\Lambda_n$ 有限且严格正。

加权 Cauchy–Schwarz 不等式及其等号条件给 (4.2) 下的准确最小费用
$$\Lambda_n|\delta-D_nx-E_n(\beta+\gamma)-F_n\alpha|^2.$$
具体达到等号的残差为 $v_i=\epsilon_iK/(\rho_iC_j\sum_{\rm active}(\rho C)^{-1})$，其中 $\epsilon=(1,-1,-1,1)$、$K$ 为 (4.2) 右端；非活动通道为零。因此没有只证明下界而遗漏可达到性。

于是得到全部高度的完整身份：
$$
\boxed{\begin{aligned}
H_n[\alpha,\beta,\gamma,\delta]
=\min_x\bigg{&\mathcal A_n|\alpha|^2
+\sum_{y,z_0:\ B_j\ \mathrm{exists}}
w_1^yw_2^{z_0}B_j|x+y\beta+z_0\gamma-p_j\alpha|^2\\
&+\Lambda_n|\delta-D_nx-E_n(\beta+\gamma)-F_n\alpha|^2\bigg\},\qquad
j=n+y+z_0,
\end{aligned}}\tag{4.4}
$$
$$\mathcal A_n=A_n+(w_1+w_2)A_{n+1}+w_1w_2A_{n+2}.$$
出生一删去 $\alpha,\mathcal A_n,F_n$，得到真实三维源的相同单参数式。

**硬端约束必须保留：**
$$
\begin{array}{c|c|c}
&t\ge2&t=1\\\hline
n=0&x=p_0\alpha&x=0\\
n=h&x=p_{h+2}\alpha-\beta-\gamma&x=-\beta-\gamma
\end{array}\tag{4.5}
$$
在 $1\le n<h$，$x$ 是自由复参数；在两端按 (4.5) 代入，不再作自由最小化。$j=1,h+1$ 的缺失 $C_j$ 已由 (4.3) 的活动通道集合处理。因而 (4.4) 同时覆盖两端、首末内边及全部中间高度。

## 5. 明确的 $5\times5\to4\times4$ 和 $4\times4\to3\times3$ 矩阵

一般出生用坐标 $\zeta=(\alpha,\beta,\gamma,\delta,x)^T$。定义行向量
$$\ell_{yz_0}=(-p_j,y,z_0,0,1),\qquad
k_n=(-F_n,-E_n,-E_n,1,-D_n).$$
则 (4.4) 花括号中的原五维 Hermitian Gram 为
$$
\boxed{M_n=\mathcal A_ne_1e_1^*
+\sum_{y,z_0:\ B_j\ \mathrm{exists}}
\rho_iB_j\ell_i^*\ell_i+\Lambda_nk_n^*k_n.}\tag{5.1}
$$
内部写
$$M_n=\begin{pmatrix}G_n&b_n\\b_n^*&m_n\end{pmatrix},\qquad
m_n=\sum_i\rho_iB_j+\Lambda_nD_n^2>0.$$
同一四维源中的答案准确为
$$\boxed{H_n=G_n-b_nm_n^{-1}b_n^*.}\tag{5.2}$$
出生一从 (5.1) 删除第一行、第一列及第一项，得到四维 Gram；再对最后的 $x$ 作 (5.2)，即为真实三维 $H_n$。

两端用 (4.5) 的固定嵌入 $J_n:\xi\mapsto(\xi,x(\xi))$，直接取
$$H_n=J_n^*M_nJ_n.\tag{5.3}$$
这里没有无穷系数，也没有从内点极限推硬端严格性。$H_n$ 的正定性来自原完整 MP 和源单射；它不蕴含相邻差的正定性。

## 6. 标量输入均可由同一个实际有限测度精确生成

定义
$$\nu_k(i)=\binom qi\binom L{k-i}z^i,\qquad
\Delta_s(k)=\det\left[\sum_i i^{a+b}\nu_k(i)\right]_{a,b=0}^{s-1},
\quad\Delta_0=1,$$
并置 $C_q=(q!)^2z^q$、$k=j+t-2$。同原[互补 Hankel 证明](../results/R239-appendix-general-birth-dual-hankel-and-birth-two-full-source.md) §4 的 Lagrange 最高系数最小化，准确给
$$
A_j=C_q\frac{\Delta_{t-2}(k)}{\Delta_{t-1}(k)}\quad(t\ge2),\qquad
B_j=C_q\frac{\Delta_{t-1}(k)}{\Delta_t(k)},\qquad
C_j=C_q\frac{\Delta_t(k)}{\Delta_{t+1}(k)}.
\tag{6.1}
$$
每个式子只在其上述可行区间使用。出生一不出现负下标行列式。

次高、次次高系数也无需猜测。以下给可直接生成的有限矩公式。对任一可行次数 $e\le q$，设
$$\lambda_R=\frac{(-1)^{q-R}}{R!(q-R)!},\qquad
\widehat\omega_j(R)=\lambda_R^2/\omega_j(R),\qquad s=q-e.$$
令 $\pi_s$ 为该合法支撑权的首一 $s$ 次正交多项式，平方范数为 $h_s$；定义
$$J_1=h_s^{-1}\langle R^{s+1},\pi_s\rangle_{\widehat\omega_j},\qquad
J_2=h_s^{-1}\langle R^{s+2},\pi_s\rangle_{\widehat\omega_j}.$$
记完整网格的初等对称和 $e_1=\sum_{R=0}^qR$、$e_2=\sum_{R<S}RS$。对应原首一 $e$ 次最小多项式的两个最高以下系数准确是
$$\boxed{J_1-e_1,\qquad J_2-e_1J_1+e_2}\tag{6.2}$$
（第二式仅在 $e\ge2$ 使用）。用 $e=d$ 得 $p_j,s_j$，用 $e=d-1$ 得 $\tau_j$。

证明 (6.2)：原最小多项式的值为
$\lambda_R\pi_s(R)/(\omega_j(R)h_s)$。Lagrange 的最高系数恒等式对 $R^{s+1}P$ 给 $J_1=p+e_1$；对 $R^{s+2}P$ 给 $J_2=s_2+e_1p+e_1^2-e_2$。解出 $p,s_2$ 即得。所有非法值为零，已包含全部强制根。

因此 (5.1)–(5.3) 的每个输入都由原 $q,L,z,w_1,w_2,t,n$ 唯一决定；没有以任意正数族替代实际可实现域。

## 7. 持久化校准、范围与接续

[程序](2026-11-14-two-exceptional-schur-789f.py)分别实现两套计算：一套用 (1.2)–(1.4) 构造完整物理层矩阵并求逆；另一套先构造所有非法网格根，直接解首一正交最小化，再按 (5.1)–(5.3) 消去唯一参数。两套程序不共享 reduced Gram 或预先压缩的原层逆。

实际运行输出：

```text
PASS exact complete-layer Gram identities: birth-one=102, general=46
Includes all endpoint heights, unequal exceptional weights, and q > pool.
No adjacent-positivity claim is tested or made.
```

完整套件使用两个严格正有理权组，覆盖 $t=1,2,3$、全部高度、两个硬端和池较短的合法范围。它验证的是恢复身份的独立实现；全参数身份的证明在 §§2–5，而不是有限例子。源码不存大矩阵数据，可重新生成。

目前真正剩余有限问题仍是将同一个物理源下的 (5.2) 用于三个相邻高度，证明或否定
$$H_nH_{n+1}^{-1}H_n\prec H_{n-1}.$$
不能分别改变三个高度的源坐标，也不能将 Schur 补前的若干标量 log 凸性直接当作这一矩阵序。恢复了完整身份，并未关闭此不等式，更未关闭原无限尾或普通 ISP。
