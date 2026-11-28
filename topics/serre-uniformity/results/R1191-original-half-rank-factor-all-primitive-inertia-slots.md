# R1191：同一个原半秩因子的全部 primitive 惯性槽与逐槽 Abel 横截

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 从 R1029/R1040 已选出的原非 CM、$\tau_1$、$D_0$ 非挠成分出发，R1011 的同一个有理简单半秩因子并不限于最低惯性型。其中心包含 $\mathbf Q(\zeta_{p+1}+\zeta_{p+1}^{-1})$，原素数 $p$ 在此域完全分裂；全部 primitive 共轭型因此给出实际不同的 $p$-进槽。每槽在任意既定模型的原 Tate 格上整分裂，具有准确的半秩对数维数。原 $\beta=q_C(D_0)$ 以及原有理 CM Abel 首向量在每槽都非零且横截。

本篇没有将这些非零量称为 $p$-单位，也没有从原 Jacobian 的特殊 Hodge 权直接指定任意同源模型的特殊 Hodge 格。已有 CM theta 的方向单位和 Fourier 标签仍须经过同一个原 non-CM jet 的实际比较。

## 1. 原点、原商与准确前提

保持原曲线、原点和同态
$$
X_1,\quad J=J_{X_1},\quad c_0:b=0,\quad c_1:b=1,
\quad N=1+\delta+\delta^2,
\quad D_0=(3-N)[c_1-c_0].
\tag{1191.1}
$$
设 $p>37$、$p\equiv5\pmod6$，并在 R1029 §6 或 R1040 §§6–7 已付原非 CM 非挠选择的范围内，取该同一个 canonical 成分 $\pi$，使它在一个固定的 $p$-进系数嵌入具有
$$
\tau_1=\widetilde\omega_2^{p-1}
       \oplus\widetilde\omega_2^{-(p-1)}.
\tag{1191.2}
$$
然后沿 R1011 的实际三次限制标量和简单商构造取
$$
q_C:J\twoheadrightarrow C,\qquad
q_CN=0,\qquad \beta=q_C(D_0)\ \text{非挠},
$$
$$
F_0=\operatorname{End}_{\mathbf Q}^0(C),\quad
f=[F_0:\mathbf Q],\quad
\dim C=2f,\quad
C(\mathbf Q)\otimes\mathbf Q=F_0\beta.
\tag{1191.3}
$$
$F_0$ 全实，$C/\mathbf Q$ 简单。以下结论适用于这个同源类中的任意已固定有理模型及任意满足 (1191.3) 的实际 $q_C$，不要求 optimal quotient，也不重新缩放 $\beta$。

统一的大素数范围可以取 $p>\max\{C_*,10^{18}\}$、$p\equiv5\pmod6$，其中 $C_*$ 是 R1026 的原绝对常数。这里采用这个充分范围只是同时消费既成选择与 R1011；下面的证明只需 (1191.1)–(1191.3)，不引入新的素数例外。

记原 GL2 型 canonical 因子为 $A_\pi$，系数域为
$$
F=\operatorname{End}_{\mathbf Q}^0(A_\pi),\qquad d=[F:\mathbf Q].
$$
R1011 的辅助 trace-zero 限制标量簇记为 $B_{\rm tr}$。该文已证明
$$
B_{\rm tr}\sim_{\mathbf Q} C^\nu,\qquad
F_0\subset F,\qquad d=\nu f,
\tag{1191.4}
$$
并且 $F$ 是 $M_\nu(F_0)$ 的极大交换子域。$\nu$ 是同源重数，不是 Abel 展开的首阶。

## 2. 真正的全局共轭类型

置
$$
n=p+1,\qquad
E=\mathbf Q(\zeta_n+\zeta_n^{-1}),\qquad
h=[E:\mathbf Q]=\varphi(n)/2,
$$
$$
\mathcal R_p=
\{r:1\le r\le(p-1)/2,\ (r,p+1)=1\}.
\tag{1191.5}
$$
每个 $r\in\mathcal R_p$ 都是奇数，且 $3\nmid r$；$\mathcal R_p$ 是 $(\mathbf Z/n)^\times/\{\pm1\}$ 的一组代表，大小为 $h$。

原 canonical 水平含中心，故 $\pi$ 的中央角色平凡。取它的标准 newvector，得到平凡 nebentypus 的权二 newform，仍是同一个自守表示。Dieulefait–Pacetti–Tsaknias 的正式 Lemma 3.2、Theorem 3.3 适用：该 depth-zero 尖点型的惯性字符阶为 $p+1$，因而
$$
E\subset F,
\qquad
\{\text{全部系数共轭的 }p\text{-处惯性型}\}
=\{\tau_r:r\in\mathcal R_p\},
$$
$$
\tau_r=\widetilde\omega_2^{r(p-1)}
       \oplus\widetilde\omega_2^{-r(p-1)}.
\tag{1191.6}
$$
这里固定 (1191.2) 的最初 Teichmüller 标记来识别 $E$ 的各嵌入。该定理是单个给定素数处的全共轭结论；没有要求在不同坏素数处独立指定共轭。

这些共轭都实际位于 $A_\pi$ 的有理同源成分中。原 $H_6$、$N_{\rm ns}(p)$ 固定方向来自同一个有理 modular-curve cohomology，不能因改变系数嵌入而丢掉。由 (1191.6)，它们全是 primitive 尖点型，没有主系列型，也没有非 primitive 的 $\tau_3$。

## 3. 从 $F$ 到实际半秩中心 $F_0$ 的域论下降

需要证明的不是仅有 $E\subset F$，而是
$$
\boxed{E\subset F_0.}
\tag{1191.7}
$$
保持 R1011 的
$$
K=\mathbf Q(\zeta_3),\qquad
L=K(\sqrt[3]4),\qquad
\kappa:\operatorname{Gal}(L/K)\longrightarrow\mu_3.
$$
选一个辅助 Tate 素数 $\ell\ne p$，并把所有代数系数嵌入 $\overline{\mathbf Q}_\ell$。对 $\sigma:F\hookrightarrow\overline{\mathbf Q}_\ell$，R1011 (1011.14) 给实际绝对不可约四维表示
$$
W_\sigma=V_{\pi,\sigma}\otimes\operatorname{Std}_{L/\mathbf Q}.
\tag{1191.8}
$$
由 (1191.4)，若 $\sigma,\sigma'$ 在 $F_0$ 上相同，则 $W_\sigma\simeq W_{\sigma'}$。更明确地，每个 $F_0$ 嵌入的四维 $V_\ell C$ 因子，在 $B_{\rm tr}$ 中出现 $\nu=[F:F_0]$ 次；这 $\nu$ 次正对应它的全部 $F$ 嵌入延拓。

将同构限制到 $G_K$。两不可约 summands 为
$$
(V_{\pi,\sigma}|_{G_K})\otimes\kappa,\qquad
(V_{\pi,\sigma}|_{G_K})\otimes\kappa^{-1}.
$$
其行列式分别是
$$
\chi_{\rm cyc}\kappa^2,\qquad
\chi_{\rm cyc}\kappa^{-2}.
\tag{1191.9}
$$
二者不同，所以任何同构只能将相同 $\kappa$ 的 summands 配对。因此
$$
V_{\pi,\sigma}|_{G_K}
\simeq V_{\pi,\sigma'}|_{G_K}.
\tag{1191.10}
$$
$K/\mathbf Q$ 在 $p$ 未分歧，故 $I_p\subset G_K$。由原 local–global compatibility，(1191.10) 使这两个系数嵌入的 $p$-处惯性型相同。依 (1191.6)，它们在 $\zeta_n+\zeta_n^{-1}$ 上的值相同，也就是在整个 $E$ 上相同。

现在固定一个 $F_0$ 嵌入。$F/F_0$ 的全部延拓嵌入在 $E$ 上取相同值；任一 $x\in E$ 的 $F_0$-共轭因此只有一个。特征零可分性迫其在 $F_0$ 上的最小多项式为一次，即 $x\in F_0$。这证明 (1191.7)，没有假设 $F/F_0$ 为 Galois，也没有把 $F$ 与 $F_0$ 偷换。

同样的限制表示论还说明，相同 $F_0$ 嵌入上的两个权二表示至多相差 $\chi_{-3}$；该 twist 在 $p$ 未分歧。本文的域下降只使用 (1191.10)，不需要另外计算这个内扭曲是否实际出现。

## 4. 完全分裂、精确重数与每槽的半秩

$p\nmid n$，并且 $p\equiv-1\pmod n$。$p$ 在实 cyclotomic 域 $E$ 的 Frobenius 类因而为一，故
$$
E\otimes\mathbf Q_p\simeq
\prod_{r\in\mathcal R_p}\mathbf Q_p.
\tag{1191.11}
$$
记相应中心幂等元为 $e_r$，并置
$$
u=[F_0:E]=f/h,\qquad
F_{0,r}=e_r(F_0\otimes\mathbf Q_p).
$$
这里 $F_{0,r}$ 可以是若干 $p$-进域的乘积，不预设它是域，也不预设它在 $\mathbf Q_p$ 上未分歧。有限扩张的局部次数公式给
$$
\dim_{\mathbf Q_p}F_{0,r}=u.
\tag{1191.12}
$$
因为 $\operatorname{Lie}C$ 在 $F_0$ 上秩二，$V_pC$ 在 $F_0\otimes\mathbf Q_p$ 上秩四，有
$$
\boxed{
\dim_{\mathbf Q_p}e_r\operatorname{Lie}(C)=2u,
\qquad
\dim_{\mathbf Q_p}e_rV_pC=4u.
}
\tag{1191.13}
$$
在代数闭系数上，每个 $F_0$ 嵌入的四维因子在 $I_p$ 上有两份 $\tau_r$。因此整个 $r$ 槽准确有 $2u$ 份 $\tau_r$，两个字符各重数 $2u$。

$L/\mathbf Q$ 只在二、三处分歧，所以此处三次限制标量的标准表示在 $I_p$ 上平凡。正是这一点允许从二维 canonical 型得到上述两份，而不是另添一个 tame twist。

## 5. 原模型上的整分裂：不更换 optimal quotient

对任意已固定 $C$ 模型证明
$$
\boxed{
e_r\in\operatorname{End}_{\mathbf Q}(C)\otimes\mathbf Z_p,
\quad
T_pC=\bigoplus_{r\in\mathcal R_p}e_rT_pC.
}
\tag{1191.14}
$$
这一步不能仅说有理 Hecke 本征值生成 $F_0$：一个任意既定同源模型上的有理 Hecke 作用，尚未被证明全部整。以下直接使用原 Galois 稳定 Tate 格。

### 5.1 不同 primitive 型的剩余支持互斥

令 $q=p-1$。R1029 (1029.8)、Savitt 的 corrected 任意格半单化列表给每个二维 cusp 成分的剩余 $I_p$ pair：
$$
O_r=\{\omega^r,\omega^{1-r}\},\quad
A_r=\{\psi^{p+rq},\psi^{1-rq}\},\quad
B_r=\{\psi^{1+rq},\psi^{p-rq}\}.
\tag{1191.15}
$$
在 $1\le r,s\le(p-1)/2$ 内，$O/O$、$A/A$、$B/B$ 相等只可能 $r=s$；$A_r=B_s$ 的唯一可能是 $s=r+1$。ordinary 与 niveau-two 不混同。后一个参数奇偶相反，故不同奇 $r,s$ 的三组 pair 完全不相交。

而且它们不能只共享一个惯性字符。每个 pair 的 determinant 都是同一个 $\omega$；共享一个字符便迫另一个字符也相同。因此不同 $r$ 的全部剩余 $I_p$ Jordan–Hölder 字符支持互斥。

这也适用于限制标量后的四维因子及各系数域的任意稳定格：先取一个稳定系数整环的格，再按其 uniformizer 过滤模 $p$，只会改变各既有字符的重数。任意其它稳定格的剩余半单化相同。三次标准表示在 $I_p$ 上平凡，不增加字符。

### 5.2 原 Tate 格的 Goursat 论证

令 $\Lambda=T_pC$，固定 $r$，并写
$$
V_pC=V_r\oplus V',\qquad
\Lambda_r=\Lambda\cap V_r,\quad
\Lambda'=\Lambda\cap V'.
$$
两个 projection 格记为 $P_r,P'$。Goursat 的直接投影同构给
$$
\Lambda/(\Lambda_r\oplus\Lambda')
\simeq P_r/\Lambda_r\simeq P'/\Lambda'.
\tag{1191.16}
$$
这些都是有限 $p$-群和连续 $I_p$-模。若共同商非零，取其一个简单组成因子；它同时出现在 $P_r/pP_r$ 和 $P'/pP'$ 的半单化中，因为某个 $p^aP_r\subset\Lambda_r$、某个 $p^bP'\subset\Lambda'$。这与 §5.1 的支持互斥矛盾。因此共同商为零。对所有 $r$ 重复，得原格分解，特别每个 $e_r$ 保持 $\Lambda$。

### 5.3 从保 Tate 格到实际整端环

使用以下饱和等式：
$$
(\operatorname{End}_{\mathbf Q}^0(C)\otimes\mathbf Q_p)
\cap\operatorname{End}_{\mathbf Z_p}(T_pC)
=\operatorname{End}_{\mathbf Q}(C)\otimes\mathbf Z_p.
\tag{1191.17}
$$
在当前子代数上可直接证明，不必更换 $C$。若 $f\in\operatorname{End}_{\mathbf Q}(C)$ 且 $f/p^a$ 保持 Tate 格，则 $f$ 杀 $C[p^a]$。特征零下这个核为有限 étale 群概形，因而 $f$ 实际经商映射 $[p^a]:C\to C$ 因子化，给 $f=[p^a]g$、$g\in\operatorname{End}_{\mathbf Q}(C)$。再以 $\operatorname{End}_{\mathbf Q}(C)[1/p]$ 的 $p$-进逼近证明 (1191.17)。将 §5.2 的 $e_r$ 代入即得 (1191.14)。

在原 tame 扩张 $R$ 上，$C$ 半稳定且其全部 Weil 型是有限的尖点型，无 monodromy；故它实际良好。也可由原 Raynaud 环面只有二次惯性而 (1191.6) 不含该型直接排除环面。原整端环延伸至 Néron 模型，(1191.14) 在各 $p^a$ 核上兼容，得到
$$
\mathscr C[p^\infty]=\prod_{r\in\mathcal R_p}\mathscr G_r,
\quad
\operatorname{height}\mathscr G_r=4u,
\quad \dim\mathscr G_r=2u.
\tag{1191.18}
$$
这里没有声称 $J$ 的单个 $\tau_r$ 子集也在原整个 $J[p^\infty]$ 上整分裂。对于 $r>1$，原 $J$ 中主系列 $\mathrm{PS}_{r-1}$ 的 $O_r$ 和 $A_{r-1}=B_r$ 恰是必须保留的碰撞；$C$ 没有主系列谱才使本节成立。

## 6. 同一个 $\beta$ 的每槽非零及准确 MW 维数

R1011 §6 已证明：非挠有理点 $\beta$ 的循环子群在 $C$ 中几何 Zariski 稠密；并且在每个 $\tau:F_0\hookrightarrow\overline{\mathbf Q}$ 上，$\log_p\beta$ 的二维分量非零。后者使用包含原点的 $p$-进解析子群定理，适用于 $C$ 仅在 $\mathbf Q$ 上简单的情形，不偷换为几何简单。

因此每个 $r$ 满足
$$
\boxed{
\log_p\beta_r:=e_r\log_p\beta\ne0,
\qquad
\dim_{\mathbf Q_p}F_{0,r}\log_p\beta_r=u.
}
\tag{1191.19}
$$
第二个等式还需每个 $F_{0,r}$ 域因子中非零，已由上述逐 $F_0$ 嵌入的结论支付。因此每个真实槽的维数 $2u$ 与实际 MW 对数维数 $u$ 都准确已知。

可以用 R1189 的同一实际整数倍将 $\beta$ 送入原形式核，再以 (1191.14) 作用；由形式指数得到的各槽点非零且非挠。但这些 $p$-进槽点不被称为新的有理点，也不把 $e_r$ 称为 $\mathbf Q$ 上的独立简单商。

若把既定 $q_C$ 乘非零整数，或沿实际同源运输 $C,\beta$，非零性不变；证明始终应用于运输后的实际点及其实际 Tate 格。这里没有除掉同源分母来宣称赋值不变。

## 7. 原有理 Abel 首向量在每个槽都横截

保持原参数 $t=b-1$，写同一个实际形式对数
$$
\log_p q_C[x-c_1]=\sum_{j\ge j_*}U_jt^j,
\qquad
U_j\in\operatorname{Lie}(C)(\mathbf Q),\quad U_{j_*}\ne0.
\tag{1191.20}
$$
R1182 已控制这个原有理首阶；本文不重做该界。$\operatorname{Lie}(C)(\mathbf Q)$ 在 $F_0$ 上二维，所以一个非零 $U\in\operatorname{Lie}(C)(\mathbf Q)$ 在每个 $F_0$ 嵌入的二维分量 $U_\tau$ 都非零。

实际上对每个 $\tau$，都有
$$
\boxed{
\log_p\beta_\tau\ \text{与}\ U_\tau
\text{ 在 }\mathbf C_p\text{ 上线性无关}.
}
\tag{1191.21}
$$
若二者相关，$\log_p\beta$ 就落在代数线性子空间
$$
W_\tau=
\bigoplus_{\sigma\ne\tau}\operatorname{Lie}(C)_\sigma
\ \oplus\ \overline{\mathbf Q}U_\tau
\subsetneq\operatorname{Lie}(C)_{\overline{\mathbf Q}}.
\tag{1191.22}
$$
它由实际 $F_0$-作用和有理 $U$ 定义。包含点版本的解析子群定理给一个包含 $\beta$ 的非零整数倍、Lie 包含在 $W_\tau$ 的真代数子群，与原 $\beta$ 的几何 Zariski 稠密性矛盾。故 (1191.21) 成立。

保持 R1182 (1182.15) 的同一个 $F_0$-基和同一个整数 $D$，但明确区分其 $F_0$-值行列式与取迹后的有理交错型：
$$
\widetilde\Omega(v,w)=D\det_{F_0}(v,w),\qquad
\Omega(v,w)=\operatorname{Tr}_{F_0/\mathbf Q}\widetilde\Omega(v,w).
$$
将 $U=U_{j_*}$ 代入 (1191.21)，得到
$$
\widetilde a_{j_*}:=\widetilde\Omega(\log_p\beta,U_{j_*})
\in(F_0\otimes\mathbf Q_p)^\times.
\tag{1191.23}
$$
这里的上标 $\times$ **只表示反转 $p$ 后每个域分量非零**，不表示属于任何整环的单位群。

这不是将 R1182 的有理标量 $a_m$ 改成数域值；取迹仍恢复该文原有标量，只是此处先保留各域分量。对任意 $r$，由 $F_{0,r}$ 的 trace pairing 非退化，可选 $c_r\in F_{0,r}$，使
$$
\lambda_r(w)=\operatorname{Tr}_{F_{0,r}/\mathbf Q_p}
\bigl(c_r e_r\widetilde\Omega(\log_p\beta,w)\bigr)
$$
在首向量上非零。这个 $\mathbf Q_p$-线性泛函支撑在该槽、杀全部原 MW 对数，且
$$
\lambda_r(e_rU_{j_*})\ne0.
$$
因此同一个原 Abel 映射在每一个 primitive 槽上都给
$$
\operatorname{ord}_{t=0}
\lambda_r e_r\log_p q_C[x-c_1]=j_*.
\tag{1191.24}
$$
这是真正同 $\beta$、同首阶的逐槽横截，不是只比较一个抽象局部表示。它仍没有给 $v_p(\lambda_r(e_rU_{j_*}))$ 的单位上界。

## 8. 原正常层来源与已知单位的准确区分

本篇给出的回答是：**原半秩目标并非只能使用 $e_1$；同一个原 $C,\beta$ 的全部 primitive $r$ 槽都是真实可选来源。** 但目前不能把已有其它模型的单位直接分配给这些槽。

1. 原 $J$ 的特殊 Hodge 权由 R1018/R1038 完整给出。generic 尾为 $m(2j+1)$，CM 支持尾为 $3m(2j+1)$，Igusa 权为 $p+1$ 的倍数；$p\equiv5\bmod12$ 行的 Raynaud 环面权为 $e_0/2$，其角色阶为二，也不在 primitive 轨道中。primitive $r$ 必 $3\nmid r$，所以 $+rm$ 若出现只在原 generic 尾；$-rm$ 在该代表范围不出现于原 Hodge 空间。这是后续同源 normal 计算的实际起点。
2. 上一条关于原 $J$ 的特殊 Hodge 格，不能不经同源比较就变成任意既定 $C$ 模型的特殊 Hodge 格。$p$-同源可能改变 mod-$p$ Hodge 格；本篇 (1191.18) 只给真实 BT 分裂及维数。R1190 的一 $p$ Lie 格损失可用于实际子簇运输，但不把这个损失或指定 jet 自动设为单位。
3. R1028 的 $\nu_I=b\,db/u^2$ 是原中心的 weight-six、$\mathrm{PS}_2$ 来源；它不在 (1191.6) 的 primitive 尖点轨道中。$3\mid p+1$ 使 $\tau_3$ 也不在该轨道；不能由本篇推出原 $D_0$ 在这两个类型中非挠。
4. R918/R920 的 marked weight-four/ten 非零层属于其原 CM 目标。两文末节已明确保留它们到指定 coarse normal jet 的比较；它们不是本篇原 non-CM 两列的单位证明。
5. R1013/R1022 的原 theta 全方向非零及常平方是已付来源，不需重算。但方向值和指定 Fourier/primitive 标签不同；在未构造 (1191.20) 各 $r$ 首项到该同一个 theta 源的箭头前，不能用方向零界代替跨 $r$ 的 Abel–MW 行列式。

因此下一项实质问题可以在本篇真实多个槽中选择：计算同一 $q_C,\beta,U_{j_*}$ 的整 normal 读数，并证明至少一个槽相对于完整尾项有足够小的赋值。全局 Galois 共轭只给 (1191.6)、(1191.21)，并不运输一个未证明的 $p$-单位或 whole-disc 半径。

## 9. 来源与证明范围

- L. V. Dieulefait, A. Pacetti, P. Tsaknias, *On the number of Galois orbits of newforms*, **J. Eur. Math. Soc. 23** (2021), 2833–2860, [DOI 10.4171/JEMS/1073](https://doi.org/10.4171/JEMS/1073)，[正式 PDF](https://ems.press/content/serial-article-files/32574)。已亲读 printed pp.2846–2848：Lemma 3.2 和 Theorem 3.3；本篇只用给定 prime 的 primitive local-type Galois 轨道与 coefficient-field 包含，不用该文的大权存在定理。
- [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) §§2–6：同一三次点、实际 trace-zero 限制标量、$W_\pi$、$F_0\subset F$、全部同源重数、原 $\beta$ 及包含点的解析子群定理。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md) (1029.7)–(1029.11)、§6；[R1038](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md) §§2–3；[R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md) §§6–7：原完整类型、任意格剩余半单化及两行真实非 CM 来源。本篇的 Goursat 饱和证明直接保任意已固定 $C$ 格，不暗用任意商上的整 Hecke 作用。
- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md) §§5–6、[R1182](R1182-original-effective-Abel-jet-valuation-and-CM-disc-radius.md)：原半秩中心、平衡型及真实首阶；[R1184](R1184-original-uniform-cubic-CM-disc-and-Neron-integrality.md)、[R1189](R1189-original-CM-formal-multiple-and-ramified-norm-descent.md)、[R1190](R1190-original-one-p-Neron-Lie-lattice-bound.md)：原盘与格界仍按其完整范围使用。

全部新增步骤为实际域下降、有限格和解析子群定理的纸面证明；没有执行数学程序，也没有重跑有限窗口。Serre 主目标仍 OPEN。

root 亲读 DPT 正式 Lemma 3.2、Theorem 3.3，并逐式核定域下降、不同奇型的剩余支持互斥、原 Tate 格 Goursat 及实际端环饱和，完整证明直接登记。
