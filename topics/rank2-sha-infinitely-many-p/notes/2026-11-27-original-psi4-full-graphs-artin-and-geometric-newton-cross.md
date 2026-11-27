# 原 psi4 新十八图的完整 Artin 作用、fixed-base p² 权族与 canonical 斜率

2026-11-27 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

本篇只使用[新 sign 曲面和实际图](2026-11-27-original-psi4-sign-surface-fulllevel-graphs-and-fp.md)的同一个 $\mathcal T/C$、$A=A_4:y^2=x^3+4$、$\Omega_4$、完整 full2/full9 级结构、十八个 cyclic17 核及严格最高投影。原[来源笔记](2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)§§7、10–11给实际两个 theta 槽及全部 raw 幅度；[单参数 Newton 笔记](2026-11-27-original-psi4-double-slot-newton-and-canonical-slope.md)给原 $102/34$ 两个 completion。

以下证明新图的完整连续 cross，而非把旧54图的端点改名。canonical 的指定几何斜率结论仍明确保持参考端点非零的范围；不从一个正权锚推出共同因子在 augmentation 为单位。

## 1. 固定的源、图及系数

始终 $k=1,3,5$，并置
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad
\eta_k=\psi_k/\psi_4,\quad
\lambda_k=\psi_4^4/\psi_k,\quad
\xi_{k,n}=\eta_k^{-1}\nu_4^{-(3+2n)}.
\tag{1}
$$
$\psi_k$ 是原 $E_k:y^2=x^3+17^k$ 的完整 Hecke 角色；特别 $k=1$ 是原 rank2 canonical 来源。三个 $\eta_k$ 都为六阶，但其17分量分别有阶6、2、6。取同一个有限 Galois 扩域 $L/K$，包含原全部图、$A[306]$、系数和三条 $H_k=K^{\ker\eta_k}$。于是 $[H_k:K]=6$，$[L:H_k]$ 是同一个整数。外系数域在几何 Galois 作用下固定。

在 source $A$ 上保有序9级点列
$$
\beta_9=((1+\omega)u_9,(1-\omega)u_9)^t,\qquad
M_\omega=
\begin{pmatrix}-1/2&-1/2\\3/2&-1/2\end{pmatrix}
\equiv\begin{pmatrix}4&4\\6&4\end{pmatrix}\pmod9 .
\tag{2}
$$
这来自实际 $g=P$、$g'=\left(\begin{smallmatrix}1&1\\-1&1\end{smallmatrix}\right)$ 的点列，不是旧 $Ph$ 的列。源 Weil pairing 指数为 $+2$，degree17 后为 $+34\equiv1\bmod3$。

令 $\mathcal C$ 为 $A[17]$ 中十八个 cyclic 核，$\varphi_C:A\to E_C$ 为规范商；完整权 $c_k(C)$ 沿来源笔记。先在 full2 覆盖上取
$$
Q_\tau=(1+\omega^2\tau_0^*+\omega(\tau_0^*)^2)/3
$$
和 $e_A^-$，尚不施 sign。新模型笔记§6已逐核重编号证明：在完整十八项上，order3 的2级作用为恒等；然后 sign 恰为 $(1-s_2)/2$。在此顺序下，$\tau_0$ 的 cycle push 特征为 $\omega^2$，source $[\omega]_*$ 特征为 $\omega$，而实际 degree17 后的9级操作是 $\tau_0^{-1}$。以下记 $\mathscr Z_k$ 为完成这些真实投影和 sign 后、但尚未施 $e_{\eta_k}\operatorname{Cor}_{L/H_k}$ 的修正图和。每条图仍有
$$
\Delta_C=\Gamma_{\varphi_C}
 -17(E_C\times O_A)-(O_{b_C}\times A).
\tag{3}
$$
同一 transposition 的负取向也带全部两项修正。

## 2. 完整算术 Artin 作用，不省 full9 determinant

采用与原表一致的算术 reciprocity。因 $h_K=1$，每个有限 ray 类可取有限单位 idèle $u$ 代表。记 $\epsilon_2$ 是 $u_2\bmod2$ 的 $\mu_3$ lift，$\epsilon_3$ 是 $u_3\bmod3$ 的 $\mu_6$ lift。实际 $A_4$ 角色在有限单位上的补偿是
$$
\epsilon_4(u)=\epsilon_2^{-1}\epsilon_3^{-1},\qquad
\rho_4(\operatorname{Art}_{\rm ar}(u))
     =\epsilon_4(u)u^{-1}
\quad\text{在所有 }A[306]\text{ 上}.
\tag{4}
$$
这是 $\nu_4$ 在2处 $\epsilon_2^{-1}$、3处 $u^{-1}$ 的原完整表。不是把 Hecke 理想值与 idèle 单位值取同向。

在2处，$\rho_4(u)$ 落 $\mathbf F_4^\times=C_3$，故其 sign 为1。在3处，唯一写成
$$
\rho_{4,3}(u)=\omega^r a,\qquad a\equiv1\pmod3,
\qquad \omega^r=\epsilon_2^{-1}\epsilon_3^{-2}.
\tag{5}
$$
把 $a=A+B\omega$ 写在 $\mathbf Z_3[\omega]$ 中，$a\equiv1\bmod3$ 给 $A\equiv1$、$B\equiv0\bmod3$。在原点列(2)上
$$
M(a)=A I+B M_\omega,\quad
b=-B/2,\quad c/3=B/2,\quad b-c/3=-B\equiv0\pmod3 .
\tag{6}
$$
所以 $a$ 落原完整 $G_\Gamma$；它的 determinant 是 $N(a)$，也正是有序 Weil pairing 的变化。式(6)没有先投到 $\mathrm{SL}_2$，也没有漏掉9级而只检查模3。

剩下 $\omega^r$ 在 degree17 靶的 $+34$ 分量上是 $\tau_0^{-r}$。由 cycle push 特征 $\omega^2$，其贡献为 $\omega^r$。在17处，用原 $C_t=\bar t C_0$ 标号；Galois 作用将 $t$ 变为 $[\rho_{4,17}(u)]^{-1}t$。完整十八项重编号因此给
$$
\chi_{k,17}(\rho_{4,17}(u))^{-1}
 =\chi_{k,17}(u_{17}).
\tag{7}
$$
等号使用 $\chi_{k,17}|_{\mu_6}=1$，包括 $\chi_{k,17}(\omega)=\chi_{k,17}(-1)=1$；没有在单一 order17 靶上虚构 $[\omega]$ 整自同态。

由(5)–(7)，真正的 Chow 等式是
$$
\boxed{
\gamma\mathscr Z_k
 =\epsilon_2^{-1}\epsilon_3^{-2}\chi_{k,17}(u_{17})
       \mathscr Z_k
 =\eta_k(\gamma)\mathscr Z_k .
}
\tag{8}
$$
$\epsilon_3^{-2}=\epsilon_3^4$ 正是新 $\eta_k$ 的3单位角色；三处 uniformizer 与 global principal 关系由(4)和单位 idèle 代表同时保留，不另挑 $\delta$ 相位。改变单位代表只差全局 $\mu_6$；上述三因子的乘积在它上为1，故(8)不依赖代表。

于是
$$
\boxed{
Y_k=e_{\eta_k}\operatorname{Cor}_{L/H_k}\mathscr Z_k
       =[L:H_k]\mathscr Z_k .
}
\tag{9}
$$
这里 $e_{\eta_k}=\frac16\sum\eta_k(\sigma)^{-1}\sigma$，已消去且只消去这一次六项平均；sign 的 $1/2$ 和十八核没有再约掉。$\operatorname{Cor}$ 的重数准确留下 $[L:K]/6$。

相同结论适用于下面所有 $n\equiv4\bmod6$ 的 algebraic CM raised 值。有限算子不随 $n$ 改变；source 单位作用只多出 $2n$ 次幂，与 $n=-2$ 相比为12的倍数，故全部 $\mu_6$ 相位保持(8)。

## 3. 实际三个正权锚及共同来源幅度

令
$$
S_1=S,\qquad S_3=H_{3,1},\qquad S_5=H_{5,1},
\qquad
D_k=D_{{\rm new},k},\quad [z^4]D_k=1 .
$$
$D_k$ 是来源笔记§§5–7、10–11的完整 degree102 两 Weyl 词，不是另选同谱线。正槽仍在同一个 $E_0:y^2=x^3+1$、同一个 $\sigma_0$ 规范中。写
$$
d_{k,m}=[z^m]D_k,\qquad s_{k,m}=[z^m]S_k.
$$

三个 $s_{k,6}$ 可直接手算。原
$x=z^{-2}-z^4/7+\cdots$、
$\sigma=z(1+z^6/210+\cdots)$ 给
$[z^6](\sigma^{34}x^{17})=-34/15$。
结合来源笔记§11的两个完整原多项式，得到
$$
\boxed{
(s_{1,6},s_{3,6},s_{5,6})
 =\left(1,-\frac{3154}{15},\frac{4046}{15}\right).
}
\tag{10}
$$
它们全部非零；没有用正槽质量1替代其第6槽。

定义 $\mathcal T_k(n)$ 为在实际 $A_4$ 代数微分上，对 $\delta_3^n f_{\Omega_4}$ 施同一完整 finite word、十八核几何 weight-$3+2n$ 商、$1/2$ sign、$e_{\eta_k}$ 和全部 Cor 所得的 algebraic CM 值。finite word 包括(2)的 $P$、243项3型及新2sign。Maass–Shimura 在 CM 的代数实现使用原 $K$ 两条 de Rham 线的 splitting，因此在固定 $L$ 与系数域内；不是依赖一个数值复周期的定义。

同一度17的 KS 自然性给
$$
\mathcal T_k(n)=17^n
 \operatorname{Tor}_{k,n}(\delta_3^n V_k),
\tag{11}
$$
其中 $V_k$ 是先把上述有限算子施到固定 weight3 $f_{\Omega_4}$ 所得的向量。若 $\varphi_C^*\omega_C=c_C\omega_A$，每次 raising 的费用为 $c_C^2/17$；所以先 raising 与后作 weight-$3+2n$ 商的比正是 $17^n$。所有靶的 degree 相同，两个 sign 取向亦相同。

来源笔记的实际双核、Hermite 正常排序和 §§10–11 的 raw 比例给
$$
\mathcal T_k(n)=A_n b_k\,
 \delta^{-n}d_{k,n}s_{k,n+2},
\qquad n\ge0,\quad n\equiv4\pmod6 .
\tag{12}
$$
$A_n\ne0$ 与 $k$ 无关；$b_k\ne0$ 是完整固定 finite/raw 幅度。具体地两个 coherent 槽是
$s_{{\rm new},k}D_k(\Omega_0h_\infty T/\delta)$ 与
$s_kS_k(\Omega_0h_\infty T)$，$h_\infty=\sqrt{51\sqrt3}/(204\pi i)$。
双槽读出的 $n!$、$(n+2)!$、同一个 chirped Gaussian 积分和同一 CM 微分换算全部在 $A_n$ 中；raw 乘积及实际 finite projector 的尺度在 $b_k$ 中。每个 finite support 和 partial Fourier 都已经在来源笔记明确固定。所有好 split 球的随权角色转入无穷槽；不能在这里添一个依赖 $k$ 的未计算局部积分。
因此(12)是未平方函数恒等式；没有从平方选择符号。

用(10)在实际同一族的 $n=4$ 取
$$
\boxed{
B_k=\frac{9\,\mathcal T_k(4)}{s_{k,6}}\ne0,\qquad
c_n=A_n/A_4,\quad c_4=1 .
}
\tag{13}
$$
$\delta^4=9$、$d_{k,4}=1$ 给 $B_k=A_4b_k$。所以
$$
\boxed{\mathcal T_k(n)
  =c_nB_k\delta^{-n}d_{k,n}s_{k,n+2}.}
\tag{14}
$$
这是实际图的非零正权值定义的 Artin 基；由(8)有
$\gamma B_k=\eta_k(\gamma)B_k$。不在大扩域中任意开平方，不把不同 $k$ 的基重新调号。

下文删去这些固定非零数和全部固定模型/系数的有限坏位。这个删除不包含依赖 $p$ 的 $K_{-,k,p}(0)$；后者的非零仍须保为显式条件。

## 4. 新 full2/full9 上的完整 p² 往返路径

取好惰性 $p\equiv5\bmod6$、$p>211$，并排除上一节固定坏集。新 $\pi_4$ 有
$$
a_p=0,\qquad \epsilon(p)=\chi_K(p)=-1.
$$
令 $\mathcal H=R^1\pi_*\Omega^\bullet_{\mathcal E/C}$，取对应 $\Omega_4$ 的 $\mathcal H$-值 Coleman primitive $G$。使用 R997§4完整的 BDP 多项式规范：多项式杀 parabolic 类、在局部水平截面上可逆、在1不为零。新曲线是原模问题的有限覆盖，generic monodromy 仍含两个固定线不同的非平凡幺幂矩阵，故没有全局水平截面可任加。所有 Hecke 组合均保该刚性规范。

中心费用在新 level 也须实际算。$pI$ 在 full2 上为恒等；在9处
$pI=(-I)((-p)I)$，$-p\equiv1\bmod3$，第二因子在完整 $G_\Gamma$ 中且 $\theta=1$，第一因子在 weight3 类型上为 $-1$。故
$$
\langle p\rangle G=-G,\qquad \langle p^2\rangle G=G.
\tag{15}
$$
新 $P$、3型、$Q_\tau$、sign 与中心交换。这里保的是全 GL 模问题及 Weil pairing determinant，不将中间 degree-$p$ 商提前放回原连通分量。

对每个 order-$p$ 核 $D$，令 $\phi_D:E\to E/D$，定义
$$
\mathsf B_1G=\sum_{|D|=p}\frac{\phi_D^*}{p}G(E/D,\phi_D\ell).
$$
KS 自然性及 $T_pf_{\Omega_4}=0$ 给 $\nabla\mathsf B_1G=0$；上面的唯一性给 $\mathsf B_1G=0$。两步路径分成 cyclic order-$p^2$ 的非回返路径和 $p+1$ 条中央 $[p]$ 路径。每条中央路径在 $\mathcal H$ 的真实倍率是 $[p]^*/p^2=p^{-1}$，末端 level 为 $p\ell$。因此
$$
\mathsf B_2G=
 \sum_{D\in\mathscr C_2(E)}\frac{\lambda_D^*}{p^2}G(E/D,\lambda_D\ell),
\qquad
\mathsf B_1^2=\mathsf B_2+\frac{p+1}{p}\langle p\rangle ,
$$
$$
\boxed{\mathsf B_2G=\frac{p+1}{p}G,\qquad
|\mathscr C_2(E)|=p(p+1)=M_p.}
\tag{16}
$$
这些都是新向量上的同一 operator 等式。没有借旧54的循环身份。

## 5. 两个真实退化映射及完整图的负二返回

在新 fulllevel 模问题添加 cyclic $D\subset E[p^2]$，分别忘掉 $D$ 或取商。向外组合为
$$
\Omega_4^{[p]}=d_0^*\Omega_4-p^{-2}\lambda^*d_2^*\Omega_4,\qquad
G^{\rm out}(E,D)=G(E)-p^{-2}\lambda_D^*G(E/D).
\tag{17}
$$
若 $\lambda^*\omega'=c\omega$，则 actual KS 费用是 $c^3/p^2$。
在 Tate 向外分支 $c=p^2$，故(17)正是
$f_{\Omega_4}-p^2V_p^2f_{\Omega_4}$。其它 cyclic 分支由同一个 universal correspondence 定义，不假设 supersingular 曲线有 canonical 子群。

对(3)的一条新 degree17 图，推到商端准确为
$$
(\lambda_D\times1)_*\Delta_C
=\Gamma_{\lambda_D\varphi_C}
 -17p^2(E_{C,D}\times O_A)
 -(O_{b_{C,D}}\times A).
\tag{18}
$$
图、竖直修正和零截面修正的次数分别为1、$p^2$、1。
proper AJ 自然性遂给单条 outward 的两项读数。用(16)将全部 $D$ 求和，第二项的未归一总数为 $p^2\mathsf B_2G=M_pG$，于是
$$
\sum_D\operatorname{AJ}_p(\widetilde\Delta_{C,D})
           (\Omega_4^{[p]}\omega_A)
=M_p(1-p^{-2})
       \operatorname{AJ}_p(\Delta_C)(\Omega_4\omega_A).
\tag{19}
$$

$\deg\varphi_C=17$ 素于 $p$，故每个 $D\subset E_C[p^2]$ 唯一来自 $D_A\subset A[p^2]$。同一有限平坦商给
$\lambda_D\varphi_C=\varphi_{C,D_A}\lambda_{D_A}$，保所有 full2/full9 标签和微分。这逐项证明 $p$ 对应与十八核、两个取向、$Q_\tau/e_A^-$、最高投影和全 $\eta/\operatorname{Cor}$ 交换。没有把 $1/2$ 或 $1/6$ 加第二次，也没有除以 $M_p$。

新模型笔记(32)已给
$\operatorname{AJ}_p(Y_k)(\Omega_4\omega_A)=p\mathcal I^{\rm new}_{k,p}/(p+1)$。
所以定义全部向外图和 $\mathcal A^{\rm out,new}_{k,p}$ 后，完整结果是
$$
\boxed{
\mathcal A^{\rm out,new}_{k,p}
=M_p(1-p^{-2})\operatorname{AJ}_p(Y_k)(\Omega_4\omega_A)
=(p^2-1)\mathcal I^{\rm new}_{k,p}.}
\tag{20}
$$
此式未使用旧新增 NS 格，也不从它声称 $\mathcal I^{\rm new}$ 整。

原函数与 proper fp 的归一同样实际相认：在同一总复形中，
$(1-F/p^2)G-\Xi_{4,p}$ 是闭类；其在任一纤维的差来自 $H^1(\mathcal T)=H^1(C)$，限制为零。纤维 $F=-p$，故
$$
[G|_{E_C}]=\frac{p}{p+1}\xi_{b_C,p}.
\tag{21}
$$
于是(20)也是整个 $\mathcal H$-值 primitive 的配对，非只拥有相同连接的任意局部积分。

## 6. 每个正权的非零 Euler 因子

设 $H=\delta_3^nV_k$、$w=3+2n$。因为
$\delta_3^nV_p^2=p^{2n}V_p^2\delta_3^n$，
$$
H^{[p]}=H-p^{2n+2}V_p^2H.
$$
完整 degree-$p$ 商在 weight $w$ 上是 $pT_p^{(w)}$，
且 $T_p^{(w)}H=p^na_pV_k=0$。两次商的回返 $[p]$ 具有真实值
$[p]^*H=-p^wH$，保的是(15)同一个 nebentype。因此完整 cyclic 和为
$$
C_2H=-(p+1)[p]^*H=(p+1)p^wH.
$$
在固定级结构上 $V_p^2=p^{-2w}\lambda_D^*$，所以
$$
\boxed{
\sum_DH^{[p]}(A,D)
=\left(M_p-p^{2n+2-2w}(p+1)p^w\right)H(A)
=M_p(1-p^{-2})H(A).
}
\tag{22}
$$
该因子对每个合法正整数 $n$都严格非零，独立于 $k$。它是正权逐项算出的式子；没有从(20)倒推整个权族，也没有把 $p^n$作为非整数参数函数。

与本篇不同，新底曲线 $A/D$ 的 canonical 上行、再经 $\lambda_D^*/p^2$ 的 imprimitive trace 仍为零；其两个旧项按(16)抵消。这里一直固定底曲线并加 level，故不使用那条零和。

## 7. 同一新图的 Kriz 局部连续族

只用 Kriz 已发表 monograph 的局部定理：Theorem6.21，Propositions7.7、7.15、7.20，Corollary7.21/Proposition7.22，以及§9.3(9.7)–(9.18)的原函数识别。不借其需要额外 cyclic Heegner 假设的全球应用。

### 7.1 CM 点、范围和稠密参数

本次源是实际 $A_4$。其 CM order 为 $\mathcal O_K$；十八个靶的 CM order 导子为17，均素于 $p$。$K_p/\mathbf Q_p$ 不分歧二次，$p>3$。固定共同的 $p^\infty$ 基 $\alpha$，按 Proposition7.7 取 inert CM 规范。其 $b=1$；将 $y=(A,t,\alpha)$ 改为 $y'=y\operatorname{diag}(p,1)$ 后，满足
$|\theta(y_{\rm dR})p/\hat z|<p^{1/(p-1)}$ 的严格界。为包含 Proposition7.15 的 $m\ge2$，在 $\Gamma(2,2)$ 上取该命题的 invariant affinoid，再沿原 tame full2/full9/17 对应自然拉回。三个 $V_k$、period、连接与 Frobenius 都用同一邻域。

参数准确取
$$
n(u)=(p^2-1)u-2,\qquad v(u)=(p-1)u,\qquad u\in\mathbf Z_p.
\tag{23}
$$
正整数 $u$给 $n\ge0$、$n\equiv4\bmod6$，属于同一个 $n\equiv-2\bmod(p-1)$ 分支，并在 $\mathbf Z_p$ 稠密。辅助 cyclic 核生成元的改变在全部正权上不改变原 moduli 值，因此连续延拓也不改变；忘掉生成元不额外除以一个带 $p$ 的群阶。

### 7.2 全 p² 轨道确为 fixed-base 和

$\mathcal O_{K,p}^\times$ 在 cyclic order-$p^2$ 核上可递，稳定子为
$\mathbf Z_p^\times(1+p^2\mathcal O_{K,p})$，orbit 准确有 $M_p$ 项。用 CRT 为各代表取 $\alpha_D\in\mathcal O_K$，既代表指定模 $p^2$ 单位，又满足 $\alpha_D\equiv1\bmod306$。实际新角色给
$$
\psi_4((\alpha_D))=\alpha_D,\qquad
\eta_k((\alpha_D))=1.
$$
对
$\chi_{k,n}=\eta_k\psi_4^{n+3}\bar\psi_4^{-n}$
有
$$
(N_K^n\chi_{k,n})^{-1}((\alpha_D))
=\alpha_D^{-(3+2n)}.
\tag{24}
$$
主理想作用保源 $A_4$ 和全部 tame 标签；所运输微分是 $\alpha_D^{-1}\omega_A$，weight-$3+2n$ 值恰乘 $\alpha_D^{3+2n}$，与(24)抵消。这从真实角色证明原局部 orbit 是固定底曲线的完整 $D$ 和。它不是 conductor-$p^2$ 新底点的 canonical trace。

$\mathbf F_{p^2}^\times$ 的阶为 $p^2-1$，所以(23)保持这些单位幂连续。所有 $k$共用一个 CM period；原 $[L:H_k]$ 已由(9)证为同一个整数，正权 finite trace 没有额外的 $k$依赖常数。

### 7.3 真正 H 值的负二端点

先对固定 weight3 $V_k$ 作上述局部构造及(24)的完整求和，记所得函数为 $\mathcal L^{\rm raw}_{k,p}(u)$。此处 finite degree17 操作在 raising 之前，正权因此按(11)带 $17^{-n}$。本篇统一采用先 raising、后作 weight-$3+2n$ 几何商的规范，精确定义
$$
\mathcal L_{k,p}(u)=17^{n(u)}\mathcal L^{\rm raw}_{k,p}(u),
\qquad
17^{n(u)}=17^{-2}(17^{p^2-1})^u .
\tag{24a}
$$
由于 $p\ne17$ 且 $17^{p^2-1}\in1+p\mathbf Z_p$，这是实际解析单位，不是未定义的非整数 $p$ 幂。此一归一对全部 $k$相同。对正整数 $u$，
$$
\mathcal L_{k,p}(u)=q_{p,n(u)}\mathcal T_k(n(u)),
\qquad q_{p,n}\ne0,
\tag{25}
$$
$q_{p,n}$对三个 $k$相同。(11)的 $17^n$已由(24a)准确支付；余下因子保留(22)的 $M_p(1-p^{-2})$、同一 algebraic differential/CM period 及同一个 Kriz $p^\infty$ 基。这里只逐正权使用这些公共比较，不声称它们的各组成因子分别连续。

在端点，$k_{\rm modular}=3$、$r=1$，须用 Kriz (9.15)–(9.18)的 $j=1$ 配对取得 $H_{-2}$。不能把只在 $j\ge-k_{\rm modular}/2$ 的标量 $G_j$直接代到 $-2$。先识别 $G_{-1}$，再用整个 $\mathcal H$ 的两条 de Rham 线及杯积得到所需负二分量。

该配对的 Coleman 规范由§4的完整 BDP 多项式条件固定；在普通 locus 它与(17)的实际 $q$展开同一，沿上述邻域的刚性延拓仍同一。§5又把它与原 proper fp 的 $\Xi_{4,p}$ 逐 cochain 归一，所以没有一个可随 $k$调整的水平常数。

degree17 的端点次序也可不凭形式负权而直接核定。设 $\varphi_C^*\omega_C=c_C\omega_A$；KS 给 $\varphi_C^*\Omega_C=c_C^3\Omega_A/17$。因此固定 weight3 几何商 $c_C^3f_C$ 的 primitive 恰为 $17\varphi_C^*G_C$，由同一刚性规范确定。杯积再乘 degree17，故 $\mathcal L^{\rm raw}$ 的负二分量为 $17^2c_C^{-1}$ 乘源规范的 weight-$-1$ 值；(24a)在0处准确乘 $17^{-2}$，将它变回 $c_C^{-1}$。这支付两次 inverse-KS，不能把 $17^2$藏进 period。

另一方面，实际图杯积是 $17c_C^{-1}$ 乘同一个 weight-$-1$ 值。这在两个 sign 取向上一样。因此将唯一余下的 Kriz 基与本篇代数源微分的负二比较倍率记为 $\kappa_p\ne0$，它只含同一源的实际 period/基而不含 degree17 次序，则
$$
\boxed{
\mathcal L_{k,p}(0)
 =\frac{\kappa_p}{17}\mathcal A^{\rm out,new}_{k,p}
 =\frac{\kappa_p(p^2-1)}{17}\mathcal I^{\rm new}_{k,p}.
}
\tag{26}
$$
$\kappa_p$ 是该一个源基的实际比较，不为每个 $k$选择；$p/(p+1)$已在(20)中支付。其整单位性没有在本篇预设。若把因子17吸入 $\mathcal L$ 的统一定义，(25)也须同乘17；所有下面的 cross 不受这种显示共同归一的影响。

## 8. 完整两 Gaussian 的 cross，不插值裸 factorial

令 $d=p+1$、
$C_+=34c_\sigma$、$C_-=102c_\sigma=3C_+$、
$q_\delta=\delta^d/3\in1+p\mathcal O$。在原 $E_0$ 坐标定义
$$
\begin{split}
J_{-,k}(v)&=\sum_{h\ge0}C_-^{-h}
 [z^{dh-2}](D_ke^{-C_-z^d})(v)_h=pvK_{-,k}(v),\\
J_{+,k}(v)&=\sum_{h\ge0}C_+^{-h}
 [z^{dh}](S_ke^{-C_+z^d})(v)_h .
\end{split}
\tag{27}
$$
原全尾证明逐项适用于三个 degree102 源；均为 $\sigma^{102}xP_{16}(x^3)$且首4为1。正槽 canonical 质量0，参考两条质量1；同一 R301 圆盘给
$$
K_{-,k}\in\mathcal O\langle v\rangle,\quad
J_{+,1}=J_S\in pv\mathcal O\langle v\rangle,\quad
J_{+,3},J_{+,5}\in1+p\mathcal O\langle v\rangle .
$$
所有坏分母只在已删除的固定集合；不作新的有限数学试算。

对整数 $r\ge1$，两个完成的有限回卷准确为
$$
\delta^{-(dr-2)}d_{k,dr-2}s_{k,dr}
=-3q_\delta^{-r}\frac{C_+^{2r}}{(r!)^2}
             J_{-,k}(r)J_{+,k}(r).
\tag{28}
$$
定义整个解析读者
$$
R_k(v)=-3q_\delta^{-v}K_{-,k}(v)J_{+,k}(v).
\tag{29}
$$
把(14)、(25)、(28)合并，正整数 $u$、$r=(p-1)u$时
$$
\mathcal L_{k,p}(u)
 =q_{p,n}c_n B_k\,
       \frac{pr\,C_+^{2r}}{(r!)^2} R_k(r).
\tag{30}
$$
所有随权 Gamma/factorial、CM period、$p$幂、degree17费用和同一 source 相位都在这个共同非零因子中。每个正整数 $r$ 非零，即使 $p\mid r$也可在特征零域中交叉相乘；不需某条 $d_{k,n}$或 $s_{k,n+2}$ 非零。

因此先在正整数处消去这个共同因子，再由(23)的稠密性与完整连续性，得到
$$
\boxed{
\mathcal L_{k,p}(u) B_l R_l((p-1)u)
=\mathcal L_{l,p}(u) B_k R_k((p-1)u)
\quad(u\in\mathbf Z_p).
}
\tag{31}
$$
这是同一新18×2图的全精度 identity。没有定义 $p^{n(u)}$、$C_+^{2v}/\Gamma(v+1)^2$，也没有先将正权复 $L$ 值当作 $p$-单位。负二取值用的是已构造的连续函数和(26)，不是裸整数权公式的形式极限。

特别令 $u=0$，消去共同非零 $\kappa_p(p^2-1)/17$，得到
$$
\boxed{
\mathcal I^{\rm new}_{k,p} B_l R_l(0)
=\mathcal I^{\rm new}_{l,p} B_k R_k(0).
}
\tag{32}
$$
新 Artin 基与源幅均来自(8)、(13)，未借旧十八阶 $B_j$。

## 9. 原 canonical 坏条件落到哪个实际几何斜率

$R_1(0)=0$，而
$$
R_1'(0)=-3K_{-,1}(0)J_S'(0).
\tag{33}
$$
若存在 $r=3$ 或5使 $R_r(0)\ne0$，则在某个 $u=0$ 邻域可定义同一个实际连续因子
$$
F_{\rm new,p}(u)=
 \frac{\mathcal L_{r,p}(u)}
      {B_r R_r((p-1)u)} .
\tag{34}
$$
如 $R_r(0)$为整单位，可在相应整单位邻域使用；如仅在系数域非零，本式只是该域上的连续商，不自动整。

由(31)，$\mathcal L_{1,p}(u)=B_1F_{\rm new,p}(u)R_1((p-1)u)$。尽管没有假定 $F_{\rm new,p}$可微，$R_1(0)=0$使差商存在并给
$$
\boxed{
\mathcal L_{1,p}(0)=0,\qquad
\mathcal L_{1,p}'(0)
=-3(p-1)B_1F_{\rm new,p}(0)
       K_{-,1}(0)J_S'(0).
}
\tag{35}
$$
证明只用 $F_{\rm new,p}(u)\to F_{\rm new,p}(0)$及 $R_1$的解析性，未对未知公共 period 求导。

所以，在这个显示的参考范围内，原 canonical 坏条件 $J_S'(0)=0$ 确实迫**同一新图权族的指定一阶**为零。若参考两条 $R_r(0)$皆零，(31)仍成立，但本篇不由它断言(34)的连续延拓或(35)的无条件版本。

反向迫原 canonical 非零仍须实际控制(35)左端和共同因子/负槽端点。三个 $n=4$锚、参考质量1、一个纯表示同型或另一个点的日志，都不证明这些量在无穷多个不同 $p$非零。本篇没有将 $\lambda_k$ 的新局部最高类直接认作原通常全 $\Sha$ 的椭圆 canonical；它只给出原坏条件到这个精确同源几何读者的合法必要零。

## 原始依据

- 新 sign/fulllevel/fp 笔记：全部实际模型、图、两取向、Chow 投影、full9 点列及 $p/(p+1)$。本篇§§2、4–7分别重新支付其 Galois 与 $p$-correspondence。
- 新 psi4 来源笔记§§7、10–11：未平方 binary kernel、两个完整 Weyl 词、三个来源幅度、$\delta^{-n}$和 chirped Gaussian。
- 新双槽 Newton 笔记§§2–6：全部高尾、两个实际 completion、$q_\delta$、canonical 的原 $J_S'(0)$。
- D. J. Kriz, *Supersingular p-adic L-functions, Maass–Shimura Operators and Waldspurger Formulas*, Annals of Mathematics Studies212, Princeton, 2021，Theorem6.21、§7.3、§9.3，特别(9.15)–(9.18)。[原书全文](https://dokumen.pub/supersingular-p-adic-l-functions-maass-shimura-operators-and-waldspurger-formulas-ams-212-9780691225739.html)。
- Hsieh, Documenta Math.19 (2014)，§§4.1、4.4、5.1 的实际级结构、KS 和几何模形式规范。[原文](https://content.ems.press/assets/public/full-texts/serials/dm/19/8965392/online/10.4171-dm-462.pdf)。
- BDP 的 Coleman 原函数多项式规范和 Besser proper fp 的 functoriality，按新模型笔记§8所引用的准确版本与本篇(17)–(21)使用。

本篇没有执行新的数学程序；全部和保留完整十八核、两取向、六阶 Artin 与 Cor，未以小例子代替这些恒等式。
