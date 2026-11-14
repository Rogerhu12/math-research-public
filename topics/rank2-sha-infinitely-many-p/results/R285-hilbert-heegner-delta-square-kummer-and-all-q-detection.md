# R285：同一 Hilbert Heegner 点的 $\delta^2$ Kummer 层与全部 $q$ 检测

日期：2026-11-13。**状态：全部等价、局部比较及域交已证明；
这些原始 Kummer 类的跨 $p$ 非零尚未证明。**

本篇消去 R281 最大阶路线中的观察素数 $q$：
其作用准确是检测同一原 Hilbert Heegner 点的两层 Kummer
类。无需先知该点非扭、范数一部分秩一、负扭曲秩一或
负号 Sha 为零。所有类群 norm 和完整点格均保留。

## 1. 固定原来源和结论

固定
$$
       E:y^2+y=x^3+x^2-2x,\qquad N_E=389,
\tag{1}
$$
并取 R281 的合法 $(p,F)$。特别 $p\ge7$、普通非异常，
$p\nmid389\operatorname{disc}F$，
$\bar\rho_{E,p}(G_{\mathbb Q})=\operatorname{GL}_2(\mathbb F_p)$，
$389$ 分裂于 $F$，且 $\mathcal O_F^\times=\{\pm1\}$。
令
$$
     H=F[1],\qquad \mathcal C=\operatorname{Cl}(F),\qquad
     C=\mathcal C_{(p)},\qquad k=\mathbb F_p.
$$
仍以同一整数 $t_F$ 杀掉原完整基层扭迹，$p\nmid t_F$。
对每个非零满射
$$
                  \psi:C\longrightarrow\mathbb F_p
\tag{2}
$$
取对应的真实 Hilbert 子域 $L_\psi/F$，并定义
$$
 \begin{gathered}
 Q_\psi=[t_F]\operatorname{Tr}_{H/L_\psi}P[1],\qquad
 N_{L_\psi/F}Q_\psi=0,\\
 A_\psi=\ker\bigl(N:\operatorname{Res}_{L_\psi/F}E\longrightarrow E\bigr).
 \end{gathered}
\tag{3}
$$
(3) 包含 kernel 中的全部 $p$ 类群和阶与 $p$ 互素的类群
标签。绝不将 $Q_\psi$ 除以 $[H:L_\psi]$。

记 $\Gamma_\psi=\langle\tau\rangle\simeq C_p$，
$g=(p-1)/2$，并在 $A_\psi$ 上置
$$
       \delta=\tau^g(\tau-1),\qquad
       \delta^2=\tau+\tau^{-1}-2,\qquad
       \mathcal O=\mathbb Z_p[\zeta_p].
\tag{4}
$$
下文省略 $\psi$ 下标时，始终指这个实际商。
令
$$
       B=E(L)\otimes\mathbb Z_p,\quad
       B_0=E(F)\otimes\mathbb Z_p,\quad
       A_0=A(F)\otimes\mathbb Z_p=\ker(N:B\to B_0).
\tag{5}
$$
定义原二层 Kummer 类
$$
          \mathfrak k_\psi
                 =\kappa_{\delta^2,A_\psi}(Q_\psi)
                    \in H^1(F,A_\psi[\delta^2]).
\tag{6}
$$
对每个 R281 (4) 的真实 admissible $q$，令
$\Theta_{1,q}\in k[C]$ 是该文 (5) 的同一最大阶完整
theta 元素，$J=\ker(k[C]\to k)$。

**定理 1.1。** 准确有
$$
 \boxed{\quad
 \exists q:\Theta_{1,q}\notin J^3
 \quad\Longleftrightarrow\quad
 \exists\psi\ne0:\mathfrak k_\psi\ne0
 \quad\Longleftrightarrow\quad
 \exists\psi\ne0:Q_\psi\notin\delta^2A_{\psi,0}.
 \quad}
\tag{7}
$$
等价地，所有两类 admissible $q$ 的完整来源均在 $J^3$
中，当且仅当每个实际 Hilbert 商的同一个原点均在
$\delta^2A_{\psi,0}$ 中。

这里第一类是 $a_q\equiv q+1$、第二类是
$a_q\equiv-(q+1)$，始终要求 $q^2\not\equiv1\pmod p$
且 $q$ 在 $F$ 惰性。甚至可预先固定任意
$v\in k^\times\setminus\{\pm1\}$，只用 $q\equiv v\pmod p$
的这两个符号族；命中某个非零类时，检测到它的 $q$
具有正 Dirichlet 密度。

结合 R281，(7) 任一非零条件给固定 E389 的
$\Sha(E/\mathbb Q)[p^\infty]=0$。跨 $p$ 的问题因此
可以只保留 (6) 的原始性，而不再把 $q$ 的存在当成
另一个未付非零条件。

## 2. 整个 Hilbert 类域与 $E[p]$ 的交、扭点及完备格

令 $M=E[p]$。先在 $F$ 上考虑 $F(M)$。由于
$F$ 在 $p$ 不分歧，满像限制仍给
$$
                   \operatorname{Gal}(F(M)/F)
                           =\operatorname{GL}_2(k).
$$
$H/F$ 阿贝尔，故 $H\cap F(M)$ 对应一个阿贝尔商。
$p\ge5$ 时 $\operatorname{GL}_2(k)$ 的交换子群为
$\operatorname{SL}_2(k)$；因此该交只能在
$F(\mu_p)$ 中。$F(\mu_p)/F$ 在每个 $p$ 位全分歧，
而 $H/F$ 处处不分歧，所以
$$
                         H\cap F(M)=F.
\tag{8}
$$
特别有
$$
                       E(H)[p]=0.
\tag{9}
$$
这里支付的是整个 $H$ 的交，不仅是某一个
$L_\psi$；类数是否含 $p$ 不影响 (8)。

在 $\mathbb Q$ 上也有
$$
                       H\cap\mathbb Q(M)=\mathbb Q.
\tag{10}
$$
理由是 $H/\mathbb Q$ 广义二面体，因而可解；满像的
任何可解商都因 $\operatorname{SL}_2(k)$ 完美而经由
determinant。于是该交包含在 $\mathbb Q(\mu_p)$。
$H/\mathbb Q$ 在 $p$ 不分歧，而 $\mathbb Q(\mu_p)/\mathbb Q$
在 $p$ 全分歧，交只能为 $\mathbb Q$。

由 (9)，$B,A_0,B_0$ 均无 $p$ 挠点，且 $A_0$ 是
有限自由 $\mathcal O$ 模。这里不规定其秩；它可以是零、
一或更大。因为 $\delta^{p-1}=p$ 乘一个 $\mathcal O$ 单位，
乘 $\delta$ 在 $A_0$ 上单射。

有限的与 $p$ 互素的挠点不影响这些结论：
$[\delta]$ 的次数为 $p^2$，所以它在该挠点部分为
自同构；张量 $\mathbb Z_p$ 后该部分消失。由通常
Kummer 正合列及有限生成性，
$$
 \begin{aligned}
 A(F)/\delta^jA(F)
       &\simeq A_0/\delta^jA_0,\\
 A_0/\delta^jA_0
       &\lhook\joinrel\longrightarrow H^1(F,A[\delta^j])
                              \qquad(j=1,2).
 \end{aligned}
\tag{11}
$$
因此 (6) 的零准确等价 $Q_\psi\in\delta^2A_0$。
若 $\kappa_{\delta,A}(Q_\psi)=0$，则存在**唯一**
$$
                         R_\psi\in A_0,\qquad
                         \delta R_\psi=Q_\psi.
\tag{12}
$$
没有在更大的 $E(L)\otimes\mathbb Q_p$ 中取除点，
更没有把某个局部除点默认下降为全局点。

更换杀扭整数 $t_F$ 只在这个 $p$ 完备格上乘一个
$\mathbb Z_p$ 单位；不影响 (6) 的非零性。
但 (3) 中可能含 $p$ 的 norm 次数不是这样一个单位，
全文完整保留它。

## 3. 同一个原点的正、负两层类

### 3.1 兼容所有 Hilbert 商的平衡

E389 的有理挠点为零，原 Heegner 共轭公式为
$cP[1]=-\sigma_{\mathfrak n}P[1]$。先只对
$\mathcal C_{(p')}$ 完整求迹，其余作用只剩 $C$。
由于 $C$ 阶为奇数，平方映射为自同构，可取唯一
$u\in C$，使 $u^2=\sigma_{\mathfrak n,(p)}$。
对这个共同来源作 $u$ 平移后，所有商同时满足
$$
                              cQ_\psi=-Q_\psi.
\tag{13}
$$
这只是原 CM 标签的一次 Galois 平移。群环中乘一个群元
不改变落入 $J^3$ 的性质；在各 $A_0$ 中乘 $\tau$ 幂
也不改变落入 $\delta^2A_0$ 的性质。因此 (7) 对未平衡的
原 (3) 完全等价。以下使用 (13) 来准确区分两个符号。

定义第一层
$$
                     \xi_{\psi,0}
                          =\kappa_{\delta,A}(Q_\psi)
                            \in H^1(F,M).
\tag{14}
$$
这里 $A[\delta]\simeq M$ 是范数一核中
**对角 $E[p]$** 的真实识别。因为 $c\delta=-\delta c$，
(13) 给
$$
                           c\xi_{\psi,0}=\xi_{\psi,0}.
\tag{15}
$$
若第一层为零，取 (12) 的唯一除点；由单射性及
$c\delta=-\delta c$ 有 $cR_\psi=R_\psi$。定义第二层
$$
                    \xi_{\psi,1}
                         =\kappa_{\delta,A}(R_\psi)
                            \in H^1(F,M)^-.
\tag{16}
$$
第二层只在 $\xi_{\psi,0}=0$ 后定义，不是任意选择的
全局 Bockstein 原函数。

### 3.2 它们准确组成 $\delta^2$ Kummer 层

在 $G_F$ 模范畴有
$$
       0\longrightarrow A[\delta]\longrightarrow A[\delta^2]
                       \xrightarrow{\delta} A[\delta]
                                      \longrightarrow0.
\tag{17}
$$
$A[\delta](F)=E(F)[p]=0$，故其上同调序列中的
$$
               H^1(F,M)\longrightarrow H^1(F,A[\delta^2])
\tag{18}
$$
是单射。$\delta_*\mathfrak k_\psi=\xi_{\psi,0}$。
若 $\xi_{\psi,0}=0$，(18) 中
$\mathfrak k_\psi$ 的唯一原像正是 (16)，因为
$\delta R_\psi=Q_\psi$。于是
$$
 \mathfrak k_\psi=0
   \iff
   \left\{
      \begin{array}{l}
       \xi_{\psi,0}=0,\\
       \xi_{\psi,1}=0\quad\text{对 (12) 的唯一除点}.
      \end{array}
   \right.
\tag{19}
$$
在涉及 $c$ 时，(17) 的 $\delta$ 箭头是反等变的；
不能因此把 (15)、(16) 误看成同一个符号。
这是两个真实 $H^1(F,E[p])$ 层，而不是只在已知
Mordell--Weil 二维子空间上的两个数。

### 3.3 与标准 Hilbert Kolyvagin 类的准确关系

置
$$
 D=\sum_{j=0}^{p-1}j\tau^j,\qquad
 D_\delta=\tau^{-g}D,\qquad
 N=\sum_{j=0}^{p-1}\tau^j.
$$
在完整群环中
$$
          (\tau-1)D=p-N,\qquad
          \delta D_\delta=D_\delta\delta=p-N.
\tag{20}
$$
在 $A$ 上 $N=0$。若 $\delta S=P$，则
$pS=D_\delta P$。限制到 $L$ 并取一个真实分量，得到
$$
       \operatorname{res}_{L/F}\kappa_{\delta,A}(P)
           =\kappa_{p,E}(D_\delta P)\in H^1(L,E[p]).
\tag{21}
$$
又因 $(\tau-1)DP=pP$，$D_\delta P$ 与 $DP$ 在
$E(L)/pE(L)$ 中相同。因此 (14) 正是原
$DQ_\psi$ 的通常 Hilbert Kolyvagin 类，经
$E(L)[p]=0$ 的 Hochschild--Serre 同构下降。
(16) 则是同一操作对唯一真实除点 $R_\psi$ 的结果。
这没有把标准导出类的原点换成一个任意已知有理点。

## 4. 局部通常 Selmer、全局 norm 和可能的 Sha 方向

本节说明两层类没有暗中丢掉 Sha 分量。
由于 $L/F$ 处处不分歧，对每个有限位 $v$ 有
$$
 \begin{gathered}
 H^1(\Gamma_v,E(L_w))=0,\\
 N:E(L_w)\longrightarrow E(F_v)\text{ 满射}
                         \quad\text{若 }[L_w:F_v]=p.
 \end{gathered}
\tag{22}
$$
分裂位用全部分量的和解释 norm。(22) 可沿用 R146 的
逐位证明：好约化位由约化上的 Lang 和不分歧形式群迹；
在 $p$ 用相同不分歧迹及原普通非异常条件；在 $389$
用 Tate 参数估值一，单位 norm 满射，参数的估值一
消去剩余的 valuation 商。无穷位因 $p$ 奇而无贡献。
这些是整个局部点群，不只是某个已知点生成的格。

由第一式，任何 $P\in A(F_v)$ 均可写为
$P=\delta X$，其中 $X$ 在局部 Weil restriction 的点群中。
若 $pZ=NX$，则 $S=X-Z_{\rm diag}$ 满足
$NS=0,\ \delta S=P$。因此
$$
            \kappa_{\delta,A}(P)
                    =-\kappa_{p,E}(NX)
                          \quad\text{于 }H^1(F_v,E[p]).
\tag{23}
$$
不同 $X$ 使 $NX$ 只改变一个 $pE(F_v)$ 元素；
第二式使 (23) 的像恰为通常有限 Kummer 条件。
所以 (14)、(16) 是整个通常 Selmer 群中的类。
经次数二的限制同构，(14) 属于
$\operatorname{Sel}_p(E/\mathbb Q)$，(16) 属于
$\operatorname{Sel}_p(E^F/\mathbb Q)$。

但它们不必是 Mordell--Weil 类。真实全局格有准确正合列
$$
       0\longrightarrow NB/pB_0
         \longrightarrow A_0/\delta A_0
         \longrightarrow H^1(\Gamma,B)
         \longrightarrow0.
\tag{24}
$$
第一箭头把 $NX$ 送到 $\delta X$，第三项为
$A_0/\delta B$；良定义和正合性直接来自
$N(X-Y)=0$ 及 $\ker\delta=B_0$。由 (22) 和
inflation--restriction，最后一项真实注入
$\Sha(E/F)[p]$。

还可准确核对这个序列与通常 Kummer 的关系：
如果 $P=\delta X$ 在全局成立，则 (20)--(21) 给
$$
                    \kappa_{\delta,A}(P)
                               =-\kappa_{p,E}(NX).
\tag{25}
$$
反之，如果 $\kappa_{\delta,A}(P)$ 是某个
$P_0\in B_0/pB_0$ 的通常 Kummer 类，则 (21) 给
$D_\delta P=pX+P_0$ 于 $B$。施加 $\delta$，
用无 $p$ 挠点性得到 $P=\delta X$。
因此 (24) 最后一项准确保留了通常 Sha 像。
本篇从未将它置零，也没有用
“$A_0=\delta B$”替代尚未证明的全局 norm 条件。

## 5. 一个实际完成上的第一矩与 Kummer 类

取 (1.1) 中任意 admissible $q$。因 $q$ 在 $F$ 惰性，
其在 $F$ 的素理想为主理想 $(q)$，故在整个 $H/F$
完全分裂。特别 $L/F$ 有全部 $p$ 个完成，剩余域
均为 $\mathbb F_{q^2}$。选一个完成并记
$$
             D_q=E(\mathbb F_{q^2}),\qquad W_q=D_q/pD_q.
$$
由 $a_q\equiv\epsilon(q+1)$、$q^2\ne1$，
$W_q$ 为一维，$q$ 次 Frobenius 在其上为 $\epsilon$。

对 $P\in A_0$，按原顺序取完整向量和群环
$$
 \begin{gathered}
       P_j=\operatorname{red}_{q_0}(\tau^{-j}P),\\
       \Phi_q(P)=\sum_{j=0}^{p-1}P_j\tau^j
                         \in W_q\otimes_k k[\Gamma],\qquad
       \sum_jP_j=0,\\
       m_1(P;q)=\sum_jjP_j,\qquad
       m_2(P;q)=\sum_j\binom j2P_j.
 \end{gathered}
\tag{26}
$$
先在实际有限点群 $D_q$ 中解释，再约化模 $p$；
对 $p$ 完备格用连续延拓即可。

**引理 5.1。** 在自然的有限 Kummer 同构下，
$$
           \operatorname{loc}_q\kappa_{\delta,A}(P)
                       =-\kappa_{p,E}(m_1(P;q)).
\tag{27}
$$
特别两侧同时为零或非零。

**证明。** 在代数闭剩余域的分裂 Weil restriction 中
取 $\delta S=P$，且 $NS=0$。令 $S_j$ 为其完整分量。
$\tau$ 对分量作 $j\mapsto j-1$ 的循环位移，故
$$
 \sum_{j=0}^{p-1}jP_j
    =\sum_jj(S_{j-g-1}-S_{j-g})
    =NS-pS_g=-pS_g.
\tag{28}
$$
这里 $p-1-g=g$，循环折回项的 $p$ 必须保留。
所以 $-S_g$ 是左边加权点的一个 $p$ 除点。
$\kappa_{\delta,A}$ 的值落在对角 $E[p]$，
读取第 $g$ 分量即给 (27) 的负号。
$q\ne p$ 好约化使形式群上的 $\delta$ 可逆，
故约化前后的有限 Kummer 条件相同。$\square$

若 $\xi_{\psi,0}=0$，用 (12)，群环等变性给
$$
             \Phi_q(Q_\psi)=\delta(T)\Phi_q(R_\psi),
       \qquad \delta(T)=(1+T)^gT,\quad T=\tau-1.
\tag{29}
$$
$\Phi_q(R_\psi)$ 的常数项为零，故准确有
$$
       m_1(Q_\psi;q)=0,\qquad
       m_2(Q_\psi;q)=m_1(R_\psi;q).
\tag{30}
$$
没有抹掉原 norm，也没有在一个非零常数项上免费移权。
综合 (27) 得第二层的实际比较
$$
          \operatorname{loc}_q\xi_{\psi,1}
                     =-\kappa_{p,E}(m_2(Q_\psi;q)).
\tag{31}
$$

## 6. 正、负 admissible $q$ 的完整 Chebotarev 检测

**引理 6.1。** 固定
$\epsilon\in\{+1,-1\}$、$v\in k^\times\setminus\{\pm1\}$。
任一非零
$$
                         \xi\in H^1(F,M)^\epsilon
$$
均被正密度的真实 $q$ 检测到；这些 $q$ 满足
$$
 \begin{gathered}
 q\text{ inert in }F,\qquad q\equiv v\pmod p,\\
 \rho_{E,p}(\operatorname{Frob}_q)
                \sim\operatorname{diag}(\epsilon,\epsilon v),\\
 \operatorname{loc}_q\xi\ne0,
 \end{gathered}
\tag{32}
$$
并可避开任意给定有限集合。还可指定其在整个
$H/\mathbb Q$ 上为同一个预先选定的反射 $c$ 的共轭类。

**证明。** 由 (10)，可先在
$K=H\mathbb Q(M)$ 上同时指定 Hilbert 反射 $c$ 和矩阵
$A=\operatorname{diag}(\epsilon,\epsilon v)$。
这不把一个非平凡 Hilbert 商的共轭作用漏掉。
在 $\operatorname{Gal}(K/F)$ 中，
$(-I,1)$ 是中心元并在 $M$ 上作用为 $-1$。
Sah 引理给
$H^1(\operatorname{Gal}(K/F),M)=0$，
因此非零 $\xi$ 向 $G_K$ 的限制仍非零。
该限制的像受满 $\operatorname{GL}_2(k)$ 稳定，
所以是全部 $M$。

将 $\xi$ 通过次数二下降写成
$H^1(\mathbb Q,M\otimes\chi_F^{(1-\epsilon)/2})$ 中
的 cocycle $z$。固定上述 Frobenius 的一个提升 $g_0$，
并用 $g=hg_0$、$h\in G_K$ 改变提升。
在扭表示中 $g$ 的线性作用为 $\epsilon A$，所以
$$
                         z(g^2)=(1+\epsilon A)z(g).
\tag{33}
$$
在 $F$ 的有限局部商
$$
                       M/(A^2-1)M
\tag{34}
$$
上只剩 $A$ 的 $\epsilon$ 特征线；(33) 的因子在这条线
准确为 $2$，并非零。$h$ 的变化使 (34) 中的值遍历一个
满射仿射线，零值比例为 $1/p$。故存在符合 (32) 的提升；
对这个有限 cocycle 域用 Chebotarev，得到正密度。
由于 $g$ 在 $H$ 上是反射，$g^2|_H=1$，这也保留了
全部 Hilbert 完成的原标号。$\square$

应用到 (15)，取 $\epsilon=+1$；
(27) 给检测原第一矩的正号 $q$。
第一层为零后，应用到 (16)，取 $\epsilon=-1$；
(31) 给检测原第二矩的负号 $q$。
这里没有预先选一个负号有理点代替 $\xi_{\psi,1}$。
即使该类有通常 Sha 分量，检测证明仍然适用。

## 7. 完整类群二阶忠实性与定理的两个方向

每个 $\psi$ 的群环 pushforward 保留全部 kernel 标签。
R234/R281 的同一个单位比较准确给
$$
              \psi_*(\Theta_{1,q})
                    =c_q\,\iota_q\bigl(\Phi_q(Q_\psi)\bigr),
                         \qquad c_q\in k^\times.
\tag{35}
$$
$c_q$ 对该来源的所有类群标签和所有 $\psi$ 相同；
不同 $q$ 之间无需指定一个共同单位。
特别 (35) 不是对每个点分别乘一个可变比例。

设 $r=\dim_k C/pC$。在 $k[C]/J^3$ 中使用各生成元的
截断对数坐标。因 $p>2$，其模型为总次数至多二的
多项式；常数项为零。写
$$
                       \theta=L(\mathbf x)+\tfrac12M(\mathbf x,\mathbf x).
$$
商 $\psi_{\mathbf b}$、$\mathbf b\in k^r\setminus\{0\}$，
把它送到
$$
                        L(\mathbf b)x+\tfrac12M(\mathbf b,\mathbf b)x^2,
                       \qquad x=T-T^2/2.
\tag{36}
$$
所有这些商联合核准确为 $J^3$：
先在 $e_i$ 上恢复 $L_i,M_{ii}$，再在 $e_i+e_j$ 上
用极化恢复 $M_{ij}$。把 $\mathbf b$ 乘非零标量只换
同一个子域的生成元，不改变两个低项同时为零的性质。
因此每个实际子域取一次即可。$C=0$ 时两边都平凡。

若某个 $\mathfrak k_\psi\ne0$：

1. 若 $\xi_{\psi,0}\ne0$，引理 6.1 的正号族和 (27)
   给一个原第一矩非零的 $q$；
2. 若 $\xi_{\psi,0}=0$，(19) 给
   $\xi_{\psi,1}\ne0$，负号族和 (31) 给一个原第二矩
   非零的 $q$。

由 (35)，该 $\psi$ 商不在 $(T^3)$，所以
$\Theta_{1,q}\notin J^3$。

反之，若所有 $\mathfrak k_\psi=0$，由 (11) 对每个
$\psi$ 写 $Q_\psi=\delta^2S_\psi$，其中
$S_\psi\in A_{\psi,0}$。任意 admissible $q$ 都有
$$
               \Phi_q(Q_\psi)
                  =\delta(T)^2\Phi_q(S_\psi)\in(T^3),
\tag{37}
$$
因为 norm 为零使最后一个因子常数项为零。
由 (35)--(36)，$\Theta_{1,q}\in J^3$。
这证明 (7) 的两个方向。

更换 $\psi$ 的非零标量会把 $\tau$ 换为 $\tau^a$；
相应 $\delta'$ 为 $\delta$ 乘一个
$\mathcal O$ 单位，因为
$(\tau^a-1)/(\tau-1)$ 在 $\delta=0$ 处的值为
$a\ne0\pmod p$。故
$\delta'^2A_0=\delta^2A_0$，(6) 的非零不依赖
这个生成元选择。所有论断都指同一真实子域和原完整点。

## 8. 原 Euler 首项与现在准确剩下的跨 $p$ 问题

(14)、(16) 是**观测原点**的普通 Kummer 类。
它们不等于 R271 弱 Heegner 系统的首项，也没有把那个
系统除以 $\delta$。

若 (6) 非零，本文先给同一最大阶来源的实际
$\Theta_{1,q}\notin J^3$。随后 R281 构造原
$\ell+1=pu$、$p\nmid u a_\ell$ 和真实分歧子域
$L'/F$，并对同一 conductor-$\ell$ 来源得到
$$
                   Q'=[t_F]\operatorname{Tr}_{F[\ell]/L'}P[\ell],
                  \qquad a(Q')\le1.
\tag{38}
$$
在这一最后的 Selmer 证明中，首项仍为
$(\tau'-1)Q'$，即 $\delta'Q'$ 乘单位，指数仍是
$a(Q')+1$。未把未分歧 Hilbert 点的某个形式除点
冒充该原首项。

所以这条路线真正未付的跨 $p$ 输入可以只写成：
$$
 \boxed{\quad
 \text{对无穷多个合法 }p,\text{ 存在实际 }F,\psi
 \text{ 使 }
 \kappa_{\delta^2,A_\psi}
       \!\left([t_F]\operatorname{Tr}_{F[1]/L_\psi}P[1]\right)
                                                        \ne0.
 \quad}
\tag{39}
$$
这个类不随 $q$ 改变。已知的两个独立有理点只给通常
Selmer 群中的非零类；没有证明它们就是 (14) 或 (16)，
不能据此宣布 (39) 非零。本文也没有从 Kolyvagin 系统在
某个更高辅助节点的本原性推回这两层原始性。

R281 的 $F=-2267,p=11$ 真来源由 (7) 保证确实命中
(6)，但它本身仍只给一个目标素数。固定 $F$ 只允许
有限多个 $p\mid h_F$，所以 (39) 的域必须真正变化。

## 来源与已付输入

- R271、R281：原完整类群 norm、同一个标量的真实 theta
  比较、最大阶 Hecke 提升和最终整个通常 Selmer 两步门。
- R146 的逐位不分歧 norm 计算；本篇 §4 同时保留
  $H^1(\Gamma,B)$ 的真实 Sha 像，没有使用 R230 的负号
  Sha 消失。
- R234 的 admissible 局部线及反射平方检测原理；
  本篇 §2、§6 重新支付未分歧 Hilbert 来源所需的整个
  域交和类群共轭，未沿用其 $\ell$ 分歧理由。
- L. Radičević, *Explicit realization of elements of the
  Tate--Shafarevich group constructed from Kolyvagin classes*,
  Research in Number Theory **8** (2022), Article 72，
  §2.3--2.4；
  [发表全文](https://doi.org/10.1007/s40993-022-00374-1)。
  其 Hilbert 类域上的 $DQ$ 类是 (20)--(21) 的标准
  一层来源。本篇没有使用其计算例子来证明跨 $p$ 非零，
  对任意真实 Hilbert 商所需的 norm、局部和二层比较
  已在正文完整证明。
