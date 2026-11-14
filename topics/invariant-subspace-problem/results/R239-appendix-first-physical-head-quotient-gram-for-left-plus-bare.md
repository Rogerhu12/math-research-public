# R239 附录：左加裸链的首物理头商坐标、原L+B Gram与负前缀正规方程

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文把原左向量和带负号的裸右链接在同一个物理孔轴上。未来高出生子空间确为头、尾两算子的共同不变子空间；在其原正交商中，全部接合核由第零物理头唯一参数化。相应 Gram 为 $I+S^*S$，上界独立于孔窗 $q$，且其真实源 Gram 的逆恰为原 $L+B$。完整前 $K$ 源头负图因此有准确的分孔正规方程。本文还得到一个固定原头、全 $q$ 的左费／裸费上界，但该头常数仍太大，未完成实际两费比较、无权 $N=M$ 或普通 ISP。

依赖：[原完整左空间和源](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)、[原两侧联合旗](R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)、[全尾低头及真幂锚](R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)、[归一链基](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)、[逐列头费用](R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md)。

## 1. 在原物理孔轴上取高出生商

固定原 $m\ge5,d=2^m$ 和合法 $q$，写 $A=A_m,D=D_m,\nu=\|D\|\le1/m$。令
$$
E_{h,p}=\ker D^h\cap\mathcal H_p,\qquad E_{0,p}=\{0\}.
$$
先在 $\mathcal H_{\le q+d}$ 上定义未来高出生空间
$$
\mathcal H_{\rm hi}=\bigoplus_{j=1}^{d}E_{j-1,q+j}.
$$
它在左侧孔层 $p\le q$ 为零。由于 $D E_{j-1,q+j}\subseteq E_{j-2,q+j-1}$，此空间在 $D$ 下不变；在所有头算子下也不变。第 $j=1$ 段为零，故不会向左侧漏出一个非零高出生项。

以 $P_{\rm lo}$ 表示其原物理正交补投影。对 $1\le h\le d$，置
$$
\mathcal F_h=
\left(\bigoplus_{p=0}^{q}E_{h,p}\right)
\oplus
\left(\bigoplus_{j=1}^{d}
 [E_{h,q+j}\cap E_{j-1,q+j}^{\perp}]\right).
\tag{1.1}
$$
当 $j>h$ 时后面的相交空间为零。定义同一个压缩删除
$$
\delta=P_{\rm lo}D|_{\mathcal F_d}.
$$
由核旗嵌套，
$$
\boxed{\delta\mathcal F_h\subseteq\mathcal F_{h-1},\qquad
\|\delta\|\le\nu,\qquad\delta^d=0.}
\tag{1.2}
$$
其中 $\mathcal F_0=0$。共同不变商保证
$$
\delta^j=P_{\rm lo}D^j|_{\mathcal F_d},
\qquad P_{\le q}\delta^j=P_{\le q}D^j|_{\mathcal F_d}.
\tag{1.3}
$$
这些是正交商的幂身份，不是把顺次 MP 逆认成真幂 MP 逆。

原接合物理空间准确为
$$
\mathcal Q=\bigoplus_{i=0}^{d-1}e_i\mathcal F_{d-i}.
\tag{1.4}
$$
在左侧它是原逐头短核旗；在未来第 $j$ 段，非零分量必须满足 $j\le d-i$，所以自动给出原头范围 $i\le d-j$ 和原低出生旗。这里没有扩大原右输入域。

$A$ 保持 (1.4)，且保持其中的低出生部分；$\delta$ 在尾作用。因共同高出生空间不变，两者在 (1.4) 上仍交换。上三角的 $V=V_m$ 和 $V^{-1}$ 都保持 (1.4)，因为降低头指标只会放宽尾核阶。

## 2. 整个接合核的唯一首头坐标

原归一给 $A=VJ_dV^{-1}$、$V=1\oplus V_+$。定义
$$
\boxed{\mathcal T f=
\sum_{j=0}^{d-1}(Ve_j)(-\delta)^jf,
\qquad f\in\mathcal F_d.}
\tag{2.1}
$$
每项的尾属于 $\mathcal F_{d-j}$；$Ve_j$ 只使用头 $i\le j$，故每项在 (1.4) 内。望远镜与 $\delta^d=0$ 给
$$
(A+\delta)\mathcal T f=0.
$$
反向令 $z\in\ker(A+\delta)|_{\mathcal Q}$，写 $u=V^{-1}z$。逐头方程为
$$
u_{i+1}=-\delta u_i\quad(0\le i<d-1),\qquad
\delta u_{d-1}=0.
$$
由 $e_0^*V^{-1}=e_0^*$，唯一参数就是 $f=e_0^*z$，最后一式由 $f\in\mathcal F_d$ 自动成立。因此
$$
\boxed{\mathcal T:\mathcal F_d\longrightarrow
\ker(A+\delta)|_{\mathcal Q}
\text{ 是有界双射，逆为 }e_0^*.}
\tag{2.2}
$$

把 $\mathcal T f$ 的左侧写为 $v$、未来侧写为 $-a$。商核在低于 $q$ 的各行正好给 $v\in\mathscr V_q$；第 $q$ 行给
$$
Av_q=Da_1=:r;
$$
未来各行正好是原裸低链的所有内部方程。最右段在 (1.4) 中只能有第零头，故 $Aa_d=0$；两端封口均已包括。

反过来，任意同源的原左可行向量 $v$ 和原裸可行链 $a$，接为 $(v,-a)$ 后就在上述商核。因此 (2.2) 参数化全部同源左／裸可行对，不仅某一条完整补全链，也不需要额外假定裸最小者没有高返回。

## 3. q 一致的正 Gram 与准确源映射

写
$$
\mathcal T=e_0I+S,\qquad
\Psi_{d,m}=\sum_{j=1}^{d-1}\|Ve_j\|\nu^j.
$$
因为 $S$ 的像正交于第零物理头，
$$
\boxed{\Gamma=\mathcal T^*\mathcal T=I+S^*S,
\qquad I\preceq\Gamma\preceq(1+\Psi_{d,m}^2)I.}
\tag{3.1}
$$
上界对 $q$ 一致；各列费用与其真正删除次数一起保留。该式不把单列 $Ve_j\delta^jf$ 免费按 $\|\mathcal Tf\|$ 分别控制。

令 $\mathcal Bf=A(P_{\le q}\mathcal Tf)_q$。用 (1.3) 得到
$$
\boxed{\mathcal Bf=
\sum_{j=1}^{d-1}(-1)^jVe_{j-1}D^jf_{q+j}.}
\tag{3.2}
$$
不同 $j$ 在 $V^{-1}\mathcal Bf$ 中给不同源头。若 $s'=V^{-1}s$，则一个明确右逆在未来第 $j$ 层取
$$
f_{q+j}=(-1)^j(D^j:\mathcal H_{q+j}\to\mathcal H_q)^\dagger s'_{j-1}
\quad(1\le j<d),
\tag{3.3}
$$
其余层为零。因为 $s'_{j-1}\in E_{d-j,q}$，(3.3) 在 $E_{d,q+j}$，且正交于 $E_{j,q+j}$，所以在 (1.1) 中。固定孔层真幂的满射性保证这些逆有界。故 $\mathcal B$ 正好满射原完整源空间 $\mathscr R_q$。

由 §2 的全部可行对身份，
$$
\boxed{\min_{\mathcal Bf=r}\langle\Gamma f,f\rangle
=\mu(r)^2+\alpha(r)^2
=\langle(L+B)r,r\rangle.}
\tag{3.4}
$$
左右两边是同一个原源。左、裸两次最小化独立，所以最优像恰为
$$
\mathcal Tf_r=(E_q^\dagger r,-\mathcal A_b r),
\qquad f_r=e_0^*(E_q^\dagger r,-\mathcal A_b r).
$$
加权最小原像公式于是给
$$
\boxed{(L+B)^{-1}=\mathcal B\Gamma^{-1}\mathcal B^*,
\qquad \Gamma f_r=\mathcal B^*(L+B)r.}
\tag{3.5}
$$
这里不是用裸 Gram 代替完整 flat Gram；(3.5) 仅准确表示其所写的 $L+B$。

## 4. 完整核与负前 K 头的分孔正规方程

令 $W_{j,p}=E_{j,p}\ominus E_{j-1,p}$。由 (3.2) 和 $V^{-1}$ 的原前缀一致性，
$$
\ker\mathcal B=
\left(\bigoplus_{p=0}^{q}E_{d,p}\right)
\oplus\left(\bigoplus_{j=1}^{d}W_{j,q+j}\right).
\tag{4.1}
$$
未来第 $d$ 层也包括在内，因为那里整个 (1.1) 恰为 $W_{d,q+d}$，而 (3.2) 没有该层项。

对 $0\le K\le d-1$，记原完整前缀源旗为 $X_{K,q}$，$K=0$ 时取零空间。其完整原像为
$$
\boxed{\mathcal C_K:=\mathcal B^{-1}X_{K,q}
=\left(\bigoplus_{p=0}^{q}E_{d,p}\right)
\oplus\left(\bigoplus_{j=1}^{K}[E_{d,q+j}\cap E_{j-1,q+j}^{\perp}]\right)
\oplus\left(\bigoplus_{j=K+1}^{d}W_{j,q+j}\right).}
\tag{4.2}
$$
证明只需注意 $\mathcal Bf\in X_{K,q}$ 当且仅当 $D^jf_{q+j}=0$ 对 $K+1\le j<d$ 成立。这里保留所有原尾核阶，不缩成较小头的天然短尾旗。

对原最优 $f_r$，由 (3.5) 得到准确等价
$$
\boxed{r\in\ker[\iota_{X_{K,q}}^*(L+B)]
\quad\Longleftrightarrow\quad
\Gamma f_r\perp\mathcal C_K.}
\tag{4.3}
$$
具体说，$\Gamma f_r$ 在全部左孔层及未来前 $K$ 层为零；在以后第 $j$ 层，它对真实 $W_j$ 的投影为零。这是 $\Gamma f_r$ 的条件，不能换成 $f_r$ 自身的这些坐标为零。

其余强制坐标空间准确为
$$
\mathcal U_K=\mathcal C_K^\perp
=\bigoplus_{j=K+1}^{d-1}
[E_{d,q+j}\cap E_{j,q+j}^{\perp}].
\tag{4.4}
$$
若 $f_r=c+a$ 按 $\mathcal C_K\oplus\mathcal U_K$ 分解，正规方程给
$$
c=-\Gamma_{CC}^{-1}\Gamma_{CU}a,
\qquad
\langle(L+B)r,r\rangle
=\langle(\Gamma_{UU}-\Gamma_{UC}\Gamma_{CC}^{-1}\Gamma_{CU})a,a\rangle.
\tag{4.5}
$$
$\Gamma_{CC}\succeq I$，而 Schur 补也不小于单位。这里的自由坐标包括全部左孔层，反馈没有被删除。

## 5. 固定原头、所有 q 的真实左费／裸费上界

按输入孔轴把 $\mathcal F_d=\mathcal F_L\oplus\mathcal F_R$ 分成 $\le q$ 与 $>q$。因为 $\delta$ 只降孔，
$$
\mathcal T=
\begin{pmatrix}T_{LL}&S_{LR}\\0&T_{RR}\end{pmatrix},
\qquad T_{LL}^*T_{LL}\succeq I,
\qquad\|S_{LR}\|\le\Psi_{d,m}.
\tag{5.1}
$$
跨越切口的块没有零次项，故只支付正次删除列。记 $P_{LL}$ 为 $\operatorname{Ran}T_{LL}$ 的真正正交投影；该像由下界闭合。

固定原裸最小链 $a(r)$ 的首头数据 $f_R=-e_0^*a(r)$。由 §2 的全部可行对身份，固定这条裸链后，所有左可行向量恰为
$$
T_{LL}f_L+S_{LR}f_R\quad(f_L\in\mathcal F_L).
$$
因此
$$
\boxed{E_q^\dagger r=(I-P_{LL})S_{LR}f_R.}
\tag{5.2}
$$
特别
$$
\boxed{\mu(r)\le\|S_{LR}\|\,\|f_R\|
\le\Psi_{d,m}\alpha(r)
\quad(r\in\mathscr R_q).}
\tag{5.3}
$$
此处 $P_{LL}$ 是完整低孔零源核的投影，不是物理头截断。式 (5.2) 也表明 $(I-P_{LL})S_{LR}$ 杀掉全部零裸源首头自由数据；这是全部同源可行对的结论，未假设其余输出为零。

这一固定头常数确不依赖 $q$，但 $\Psi_{d,m}$ 仍含高列的巨大费用。原已付头界只给 $\log\Psi_{d,m}=O(d^4)$ 的粗尺度，故 (5.3) 尚不足以用原 $\log q\le d^3/4$ 的窗口计数收尾。

### 5.1 保同一裸最小者的右侧 Schur

令 $\mathcal B_R=\mathcal B|_{\mathcal F_R}$，并写
$$
\Gamma_R=T_{RR}^*T_{RR},\qquad
C=(I-P_{LL})S_{LR}.
$$
则 $T_{RR}$ 恰参数化所有原裸低可行链（取负号只改变源方向），逆仍是其第零物理头。因而
$$
\boxed{B^{-1}=\mathcal B_R\Gamma_R^{-1}\mathcal B_R^*,
\qquad C=E_q^\dagger\mathcal B_R.}
\tag{5.4}
$$
先在 $\Gamma$ 中消去左坐标，余下的真实右侧 Schur 为
$$
\boxed{\Gamma_{R,\mathrm{eff}}
=\Gamma_R+C^*C
=\Gamma_R+\mathcal B_R^*L\mathcal B_R.}
\tag{5.5}
$$
这说明给定 $r$ 时，左项的值与裸首头数据的零源自由量无关；同时最小化左加裸费用，确实选回原裸最小者，而非另一条重选的右链。

## 6. 完整右链与裸高返回的同一首头表示

另在完整未来尾空间置
$$
\mathcal F_R^{\rm full}=\bigoplus_{j=1}^{d}E_{d,q+j}.
$$
给 $f\in\mathcal F_R^{\rm full}$ 在未来之外补零，定义
$$
T_R^{\rm full}f
=P_{>q}\sum_{j=0}^{d-1}(Ve_j)(-D)^jf.
\tag{6.1}
$$
其第 $k$ 段由输入 $f_{q+s}$、$k\le s\le d$ 贡献，删除次数为 $s-k$，所以输出头 $i\le s-k\le d-k$，尾核阶至多 $d-(s-k)\le d-i$。原完整右旗的所有头、尾旗均保持。

同一个望远镜证明给内部零输出和末段封口。反向对任意完整零内部输出链用原观察行逐次代入，得 (6.1)，参数唯一等于该链的第零物理头。因此 (6.1) 有界双射到原完整右核，且仍有 $\|(T_R^{\rm full})^{-1}\|\le1$。

记 $\mathcal B_R^{\rm full}$ 为 (3.2) 的同一未来公式，域扩为 $\mathcal F_R^{\rm full}$。完整右链 (6.1) 的源是 $-\mathcal B_R^{\rm full}f$；负号不改变源 Gram。故
$$
\boxed{G=\mathcal B_R^{\rm full}
\bigl[(T_R^{\rm full})^*T_R^{\rm full}\bigr]^{-1}
(\mathcal B_R^{\rm full})^*.}
\tag{6.2}
$$
该式与 (3.5)、(5.4) 给出原 $L+B$、裸 $B$ 和完整右 $G$ 的同一物理首头坐标表示；原平坦费仍严格是 $\langle GLr,Lr\rangle$，不交换任何因子。

未来高出生首头子空间为 $\bigoplus_jE_{j-1,q+j}$。它在 $D$ 下不变，且被 $\mathcal B_R^{\rm full}$ 杀掉；其整条 (6.1) 像在高出生右空间内。因此
$$
P_{\rm lo}T_R^{\rm full}f=T_{RR}P_{\rm lo}f.
\tag{6.3}
$$
取原裸最小者的同一个 $f_R=-e_0^*a(r)\in\mathcal F_R$，把它作为完整未来输入，不加高出生首头自由量。则 $-T_R^{\rm full}f_R$ 是同源的完整合法候选，其低部分恰为 $a(r)$。高部分的零次项为零，所以
$$
\|(I-P_{\rm lo})T_R^{\rm full}f_R\|
\le\Psi_{d,m}\|f_R\|\le\Psi_{d,m}\alpha(r).
$$
由原物理低／高正交性，
$$
\boxed{\lambda(r)^2\le(1+\Psi_{d,m}^2)\alpha(r)^2,
\qquad \lambda(r)^2-\alpha(r)^2\le\Psi_{d,m}^2\alpha(r)^2.}
\tag{6.4}
$$
这是全源、全原尾阶、固定原头的 $q$ 一致界。它没有宣称真正最小完整链使用零高首头参数，也没有将最小高返回费用误作某个未经 Schur 消元的纯 $S_H^\dagger$ 费用。

## 7. 准确的局部化输入及其未付范围

每个 $\delta^j$ 恰降 $j$ 孔，故 $\Gamma=\mathcal T^*\mathcal T$ 在孔轴上的带宽至多 $d-1$。$\mathcal C_K$ 按孔层正交分解，因而 $\Gamma_{CC}$ 仍有同一带宽。式 (4.4) 的强制层从 $q+K+1$ 才开始，所以 $\Gamma_{CU}a$ 的自由孔层支撑从 $q-d+K+2$ 才可能开始。

这些事实与 (3.1)、(4.5) 一起，是原 $L+B$ 负前缀的一个明确正 Gram 局部化问题。普通总条件数界仍可能付 $e^{O(d^4)}$；本文没有证明可以把各列增长除以其删除次数来缩小该费用，也没有由列次数反推列间正交。

若尝试接天然四块模型，仍须分别保留其不同短核旗和同一个原源的裸／flat 运输；不能只把 $d$ 换成一个较小链长后宣称原 (4.3) 自动保留。原反馈比较及其窗口阶上界继续开放。
