# 两步判据只使用正号 Selmer：可变化的辅助 Heegner 域

日期：2026-11-12。**已证明的充分条件。** 固定目标曲线为
$E=389\mathrm a1$；本篇不证明变化辅助域后实际点的非零或
两步原始性，也不从若干无穷集合的交集取得输入。

## 1. 准确条件

令 $F$ 为虚二次域，满足 $389$ 在 $F$ 分裂，
$\operatorname{disc}F$ 与 $389p$ 互素，且 $\mathcal O_F^\times=\{\pm1\}$。
取 $p\ge7$，要求 $p\nmid h_F$，$E$ 在 $p$ 好普通，
$a_p(E)\not\equiv\pm1\pmod p$，以及 $G_F$ 在 $T_pE$ 上满像。
这些条件逐个列出；没有把依 $F$ 而变的例外集说成统一有限集。

令 $\ell$ 是好约化素数，在 $F$ 惰性，且
$$
 \ell+1=pu,\qquad p\nmid u a_\ell(E).
\tag{1}
$$
设 $H=F[\ell]$，$L/F$ 为唯一的次数 $p$ 子扩张。
因为 $p\nmid h_F$，该扩张在 $\ell$ 全分歧，在其余有限位
不分歧；$L/\mathbb Q$ 为二面体扩张。

保留全部类群和，令
$$
 P_F=\operatorname{Tr}_{F[1]/F}P[1],\qquad
 Q_0=\operatorname{Tr}_{H/L}P[\ell].
\tag{2}
$$
本曲线的已证代数秩至少为二，Gross–Zagier–Kolyvagin 的
解析秩至多一结论遂迫使 $L(E,1)=L'(E,1)=0$。因此
$$
 L'(E/F,1)=\bigl(L(E,s)L(E^F,s)\bigr)'_{s=1}=0.
$$
Gross–Zagier 对**全部 Hilbert 类群迹**的公式给 $P_F$ 为
扭点。满 $G_F$ 像使 $E(F)[p]=0$，所以可取
$t_F\in\mathbb Z_{>0}$，$p\nmid t_F$，杀掉这个扭点。
定义原整数点
$$
                       Q=[t_F]Q_0.
\tag{3}
$$
则 Heegner 范数关系给 $N_{L/F}Q=t_Fa_\ell P_F=0$。
乘 $t_F$ 不改变任何 $\delta$ 整指数。条件是这个**指定的**
$Q$ 非扭；不能用另一个范数零点代替。

令
$$
 A=\ker(N:\operatorname{Res}_{L/F}E\to E),\quad
 \mathcal O=\mathbb Z_p[\zeta_p],\quad
 \delta=\tau^{(p-1)/2}(\tau-1).
$$
由非扭的完整类群和、每个非平凡 $C_p$ 角色投影非零和
Nekovář（2007）Theorem 3.2，完全按 R119、R139 §2 的
整论证，有
$$
 A(F)\otimes\mathbb Z_p=\mathcal O w,\quad
 S=\Sha(A/F)[p^\infty]\text{ 有限},\quad
 Q=\delta^a\varepsilon w.
\tag{4}
$$
非 CM 的 $E$ 自动满足该定理关于不在角色域获得 CM 的条件。

## 2. 通常 delta-Selmer 比较不使用负号 Selmer 群

在 $\lambda\mid\ell$，
$$
 \#E(\mathbb F_{\ell^2})=(\ell+1)^2-a_\ell^2
                          \not\equiv0\pmod p.
$$
不分歧和 tame 两部分的 Frobenius 均无不变量，所以
$H^i(F_\lambda,E[p])=0$，$i=0,1,2$；沿各层短正合列，
同样有 $H^i(F_\lambda,A[\delta^k])=0$。

在其余有限位，$L/F$ 不分歧或者分裂。好约化位的约化群
范数由 Lang 定理满射，形式群范数由不分歧迹和逐层提升
满射；这包括 $v\mid p$。唯一坏约化位在 $389$ 上方，
因 Heegner 条件 $F_v=\mathbb Q_{389}$。Tate 参数估值为一，
故在 $F_v^\times/q_E^{\mathbb Z}$ 中，不分歧范数的估值
障碍被 $q_E$ 消去，范数仍满射。无穷位对奇 $p$ 无贡献。
这些同一计算还给 $H^1(\Gamma_v,E(L_w))=0$：好约化位
分别用 Lang 与不分歧整 normal basis；$I_1$ 位用 Hilbert 90
及 $H^2(\Gamma_v,q_E^{\mathbb Z})\to
H^2(\Gamma_v,L_w^\times)$ 由 $v(q_E)=1$ 给出的同构。

在实际对角识别 $A[\delta]\simeq E[p]$ 下，R139 §4.2 的
Kummer 图原样适用。先由上述 $H^1$ 消失，将每个
$A(F_v)$ 点写成 $(\tau-1)Y$。给定 $Y\in B(F_v)$，取 $pV=NY$，
则 $Y-\operatorname{diag}V$ 给差分除点，Kummer 类为
$-\kappa_E(NY)$。范数满射使它遍历通常 Kummer 条件。
反向包含由 $H^1(F_v,A)\to H^1(F_v,B)$ 的注入得到，
该注入正由上述范数满射保证。于是
$$
                  \operatorname{Sel}_\delta(A/F)
                    \simeq\operatorname{Sel}_p(E/F)
\tag{5}
$$
是保留复共轭作用的实际局部条件比较。
这段证明没有使用 $E^F$ 的秩或 Sha。

## 3. 原完整类群族的上界

对辅助平方自由 $n$，先用实际点
$Y_n=\operatorname{Tr}_{F[\ell n]/LF[n]}P[\ell n]$，
再作 $Z_n=(\tau-1)Y_n$。在 Heegner 导出类下降中，保留
$\operatorname{Gal}(F[1]/F)$ 的全部 coset 和；$p\nmid h_F$
保证原 Cartesian／唯一下降输入不变，但不在整数点中除
$h_F$。因为 $L$ 在 $\ell$ 分歧而 $F[n]$ 不分歧，
$L\cap F[n]=F$；所有标签与 $\delta$ 都可按实际域交搬运。
特别在 $n=1$ 时，$Y_1$ 先定义在 $LF[1]$；对全部
$h_F$ 个 coset 求和后才得到 $Q_0$，没有额外的 $h_F$ 因子。
因此首项正是 $t_F(\tau-1)Q_0$，指数为 $a+1$。

R139 §§4–6 的每个局部输入在 §2 已核清。辅助 $q$ 在 $F$
惰性时自动在二面体 $L/F$ 分裂，且可令
$a_q\equiv q+1\equiv0\pmod {p^m}$ 达到任意精度。
对每个类群标签，有限／奇异算子仍是
$-q\varphi_q^{-1}$；求完整类群和、乘 $t_F$ 和
$B\to A$ 均与该比较相容。Howard 的弱 stub 论证因此给
$$
                      \operatorname{length}_{\mathcal O}S\le2(a+1).
\tag{6}
$$
本篇只需上界，不需对变化 $F$ 另用一个原始性定理。

## 4. 只看正号的 Cassels–Tate 下界

R122 的整平衡同构与有限配对适用于这个同一范数一格。
其对称完美配对 $B$ 满足
$$
 B(\delta x,y)=-B(x,\delta y),\qquad B(cx,cy)=-B(x,y).
$$
对准确长度 $n$ 的原始商
$$
 P_n=S[\delta^n]/\bigl(S[\delta^{n-1}]+
                           \delta S[\delta^{n+1}]\bigr)
$$
及 $\beta_n(x,y)=B(x,\delta^{n-1}y)$，R122 的直接核计算给
非退化性。奇 $n$ 的两个符号维数相等；偶 $n$ 的每个符号
部分有非退化交替配对。顶端和 socle 的符号相差
$(-1)^{n-1}$。

令 $m_n^\pm$ 是长度 $n$ 的循环块对 $S[\delta]^\pm$
的维数贡献。若 $n$ 奇，则 $m_n^+=m_n^-$，所以该层长度
$$
                    n(m_n^++m_n^-)=2n m_n^+\ge2m_n^+.
$$
若 $n$ 偶，则 $n\ge2$，直接有
$n(m_n^++m_n^-)\ge2m_n^+$，无须使用负号维数。
对所有 $n$ 相加，得到统一的精确适用下界
$$
                  \boxed{\ \operatorname{length}_{\mathcal O}S
                              \ge2\dim S[\delta]^+.\ }
\tag{7}
$$
这不是只从 $\#S$ 为平方推导；奇数长度层的正负配对是
不可省略的输入。

完整 Heegner 类群和的共轭公式及 $w(E)=+1$ 给
$cQ=-\tau^jQ$（平移扭点在 $p$ 格中为零）。因此点商
$A(F)/\delta A(F)$ 的符号是 $(-1)^{a+1}$。
由 $c\delta c=-\delta$，$\delta$-Kummer 再反号，故其
Selmer 像是一条符号 $(-1)^a$ 的直线。

写
$$
 r=\operatorname{rank}E(\mathbb Q),\qquad
 d_+=\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p].
$$
奇 $p$ 的二次基变分解与 (5) 给
$\dim\operatorname{Sel}_\delta(A/F)^+=r+d_+$。结合 Kummer
正合列，
$$
 \dim S[\delta]^+=r+d_+-\mathbf1_{\{a\ {\mathrm{even}}\}}.
\tag{8}
$$
式 (8) 不含负扭曲的秩、有限 Sha 或 Selmer 维数。

## 5. 变化辅助域时仍成立的两步判据

若 $a=0$，(6)–(8) 给 $2(r+d_+-1)\le2$；若 $a=1$，
则给 $2(r+d_+)\le4$。因 $r\ge2$，两种情形均迫
$r=2,d_+=0$。任意非零 $p$ 初级元素都有非零阶 $p$ 多重，
所以
$$
 \boxed{\quad Q\notin\delta^2(A(F)\otimes\mathbb Z_p)
       \ \Longrightarrow\quad
       \operatorname{rank}E(\mathbb Q)=2,\qquad
       \Sha(E/\mathbb Q)[p^\infty]=0.\quad}
\tag{9}
$$

因此为了固定的目标 $E389$，可以随 $p$ 选择符合 §1 的
辅助 Heegner 域。负扭曲解析秩一和其 $p$-Sha 消失不再是
(9) 的输入。尚须实际证明每个选定的 $F,p,\ell$ 满足
完整类群迹 $Q\ne0$ 以及所需的 $a\le1$；本篇没有从域可变
本身推出其中任何一个非零性。

## 来源

- R113、R122：实际范数一同源、对偶和有限原始层的完整证明。
- R139：非 CM 整弱 Heegner 族、全部局部条件和 $2(a+1)$
  上界；本篇 §§1–3 明列迁移到一般 $F$ 所需的实际输入。
- B. Howard, *The Heegner point Kolyvagin system*, Compositio Math.
  **140** (2004), §1.6–1.7；
  [正式全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)。
- J. Nekovář, *The Euler system method for CM points on Shimura
  curves*（2007），Theorem 3.2、§3.5.1；
  [作者全文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)。
- B. Gross–D. Zagier, *Heegner points and derivatives of L-series*
  （1986），以及 V. Kolyvagin 的解析秩至多一结论（1990）：
  此处只用来确认固定 $E$ 的解析秩至少二及基层完整迹为扭点。
