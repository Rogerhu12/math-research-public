# R244 后续附录：近似共同源的聚合转置预算与准确对偶代价

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d；根独立核验误差恒等式、酉框架极限和预对偶 Hahn–Banach 公式。
状态：完整的真实见证必要条件和有界预算降秩判据。系数算子不需要统一范数界；只要有限个聚合转置源有界，就足以把近似同源表示变成精确的低秩分离泛函。本文没有构造这种有界预算。

## 1. 设置及与旧算子球条件的区别

固定真正的最小秩正慢理想见证
$$
\rho=\sum_{i=1}^r f_i\otimes f_i,\qquad
\phi(F)=\sum_i\langle Ff_i,f_i\rangle,\qquad
\phi(SA')=0,\qquad \phi(I)>0.
$$
最小正秩等于最小一般分离秩，使用
[R228A §1](R228-appendix-minimal-witnesses-and-positive-quotient-orbits.md)。
记
$$
x_i=Cf_i,\qquad B(u,v)=\langle u,Cv\rangle.
$$
对每个有界 $T\in A'$，实际有 $T=CT^*C$；
$A'$ 交换，所以可在 B 配对中转移所有这些有界系数。

[R230 逐对共同域附录](R230-appendix-minimal-positive-rank-module-compression-and-pairwise-common-domains.md)
及其[完整源稿 §8](../notes/2026-11-13-minimal-positive-rank-module-compression-and-pairwise-common-vacuum-obstruction-normal-complex.md)
已经排除固定少数源、系数算子一致有界的近似压缩。
以下只要求具体聚合源向量有界，允许每个系数算子的范数任意增长。
该区别不以未经控制的算子 WOT 极限支付。

## 2. 精确误差恒等式与有界聚合预算降秩

取 $I\subseteq\{1,\ldots,r\}$、$|I|=s$，
以及固定 $g_1,\ldots,g_k\in H$，其中 $1\le k<s$。
允许任意
$$
T_{i\ell}^{(n)}\in A'\qquad(i\in I,\ 1\le\ell\le k).
$$
定义
$$
e_i^{(n)}=x_i-\sum_{\ell=1}^kT_{i\ell}^{(n)}g_\ell,\qquad
\varepsilon_n^2=\sum_{i\in I}\|e_i^{(n)}\|^2,
$$
$$
h_\ell^{(n)}=\sum_{i\in I}T_{i\ell}^{(n)}f_i,\qquad
\mathcal E_n=\left(\sum_{\ell=1}^k\|h_\ell^{(n)}\|^2\right)^{1/2}.
\tag{2.1}
$$
对每个 $F\in A'$，逐项有
$$
\begin{aligned}
\phi_I(F)
&:=\sum_{i\in I}\langle Ff_i,f_i\rangle\\
&=\sum_{\ell=1}^k B(Fh_\ell^{(n)},g_\ell)
 +\sum_{i\in I}B(Ff_i,e_i^{(n)}).
\end{aligned}
\tag{2.2}
$$
这里只转移有界 $T_{i\ell}^{(n)}$，并用它与 $F$ 交换；没有无界乘子域操作。

因此
$$
\boxed{
\left|\phi_I(F)-\sum_{\ell=1}^kB(Fh_\ell^{(n)},g_\ell)\right|
\le\varepsilon_n
\left(\sum_{i\in I}\|Ff_i\|^2\right)^{1/2}
\le\varepsilon_n\sqrt{\tau_I}\,\|F\|,
\quad \tau_I=\sum_{i\in I}\|f_i\|^2.
}
\tag{2.3}
$$
误差甚至在 $A'$ 的算子单位球上一致趋零。

**定理 2.1。** 若 $\varepsilon_n\to0$，则
$$
\boxed{\mathcal E_n\to\infty.}                            \tag{2.4}
$$

证明：若有有界子列，在有限个 H 坐标中取共同弱收敛子列
$h_\ell^{(n)}\rightharpoonup h_\ell$。
对每个固定 F，(2.3) 及弱收敛给
$$
\phi_I(F)=\sum_{\ell=1}^k B(Fh_\ell,g_\ell)
=\sum_{\ell=1}^k\langle Fh_\ell,Cg_\ell\rangle.
$$
以右侧替换整个 $\phi$ 中的 s 项，剩余不超过
$r-s+k<r$ 个一般向量配对项。
这个表达式在整个 $A'$ 上准确等于原 $\phi$，
所以仍湮灭 $SA'$，且在恒等算子 $I$ 上取原来的正迹。
与最小一般分离秩矛盾。
故 $\mathcal E_n$ 没有有界子列，即趋于无穷。证毕。

这个判据需要固定的 $g_\ell$。
它不要求每个 $T_{i\ell}^{(n)}f_i$ 分别有界，
只要求每列求和后的 $h_\ell^{(n)}$ 有界就能触发矛盾；
不同 i 的真实相消因此被保留。

## 3. 任意酉源框架仍有同一发散结论

允许每一步取 $V_n\in U(r)$ 并置
$$
x_i^{(n)}=\sum_j(V_n)_{ij}x_j,\qquad
f_i^{(n)}=Cx_i^{(n)}
=\sum_j\overline{(V_n)_{ij}}f_j.
$$
于是 $\sum_i f_i^{(n)}\otimes f_i^{(n)}=\rho$。
把 (2.1) 的目标换为 $x_i^{(n)}$，聚合源准确定义为
$$
h_\ell^{(n)}=\sum_{i\in I}T_{i\ell}^{(n)}f_i^{(n)}.
$$
若目标误差趋零，仍必有 $\mathcal E_n\to\infty$。

确实，假设聚合源有有界子列。
先利用有限维酉群紧性取 $V_n\to V$，从而
$f_i^{(n)}\to f_i^\infty$、$x_i^{(n)}\to x_i^\infty$ 于 H。
再对聚合向量取弱收敛子列。
误差式 (2.2) 对每个 n 都准确成立，
且
$$
\sum_{i\in I}\|Ff_i^{(n)}\|^2
\le\sum_{i=1}^r\|Ff_i^{(n)}\|^2
=\sum_{i=1}^r\|Ff_i\|^2.
$$
所以目标误差项一致趋零。
固定 F 有界，未合并的其余源配对也正常收敛。
极限把同一个原 $\phi$ 写成至多 $r-s+k$ 项，仍然矛盾。

这里从未将 $T_{i\ell}^{(n)}$ 作用于框架极限；
这些算子的范数可以无界。
所有弱极限都在已经聚合完的 H 向量上取得。

## 4. 固定源的准确误差—能量对偶式

令
$$
\mathcal E=(A')_*=\mathcal S_1(H)/(A')_\perp
$$
为 $A'$ 的正常泛函预对偶，范数为在 $A'$ 单位球上的泛函范数。
因 $A'$ 超弱闭，有 $\mathcal E^*=A'$。

对固定源组 $G=(g_1,\ldots,g_k)$ 定义有界线性映射
$$
L_G:H^{(k)}\to\mathcal E,\qquad
(L_Gh)(F)=\sum_{\ell=1}^k B(Fh_\ell,g_\ell).
$$
有界 C 对称性给
$$
\sup_{\|h\|\le1}|(L_Gh)(F)|
=\left(\sum_{\ell=1}^k\|Fg_\ell\|^2\right)^{1/2}
=:d_G(F).
\tag{4.1}
$$
对任意指定正常泛函 $\psi$ 和 $\delta\ge0$，置
$$
c_{G,\psi}(\delta)
=\inf\{\|h\|:\|\psi-L_Gh\|_{\mathcal E}\le\delta\},
\qquad\inf\varnothing=\infty.
$$
则有准确公式
$$
\boxed{
c_{G,\psi}(\delta)
=\sup_{F\in A'}
\frac{\bigl(|\psi(F)|-\delta\|F\|\bigr)_+}{d_G(F)}.
}
\tag{4.2}
$$
分母为零且分子为正时，该项按无穷取；
两者均为零时该项取零。

证明：对固定 $R\ge0$，集合
$L_G\{h:\|h\|\le R\}$ 在 $\mathcal E$ 中弱紧，
因为 Hilbert 球弱紧且 $L_G$ 为有界线性映射。
它加上 $\delta$ 倍闭单位球后仍范数闭：
若和中的序列范数收敛，取第一项的弱收敛子网，
第二项弱极限仍落在闭单位球中。
这个和集还是凸且平衡的。

Hahn–Banach 分离因此给
$$
\psi\in L_G(RB_{H^{(k)}})+\delta B_{\mathcal E}
\quad\Longleftrightarrow\quad
|\psi(F)|\le R\,d_G(F)+\delta\|F\|
\quad(F\in A').
$$
其支撑函数已由 (4.1) 准确计算。
对 R 取下确界，得到 (4.2)。证毕。

对第2节的 $\psi=\phi_I$，最小秩意味着
$\phi_I\notin\operatorname{Ran}L_G$。
同一有界球弱紧性于是给
$$
c_{G,\phi_I}(\delta)\longrightarrow\infty
\qquad(\delta\downarrow0).
\tag{4.3}
$$
由 (2.3)，每个实际近似系数表都必须支付
$$
\boxed{
\mathcal E_n\ge
c_{G,\phi_I}\bigl(\sqrt{\tau_I}\,\varepsilon_n\bigr).
}
\tag{4.4}
$$
这给一个按原正常泛函和固定源计算的准确成本，
不把它换成系数算子范数。
未证明 (4.3) 的统一速度，也不保证任意 G 的有限误差问题都有解。

## 5. 真空源的具体多项式版本

取 $k=1$、$g_1=1$。
由原 $1$ 循环，对任意选定源行都可以选多项式 $p_i^{(n)}$，使
$$
p_i^{(n)}(A)1\longrightarrow Cf_i.
$$
若至少选择最小秩见证中的两行，则定理2.1给
$$
\boxed{
\left\|\sum_{i\in I}p_i^{(n)}(A)f_i\right\|
\longrightarrow\infty.
}
\tag{5.1}
$$
只有误差向量在 $H$ 中收敛，不能把这解释为有界的共同源分解。
对于这里的 $G=(1)$，每个 $\delta>0$ 的 $c_{G,\phi_I}(\delta)$ 都有限：
上述有限多项式逼近及 (2.3) 已提供满足误差的有限范数聚合向量。
这不控制 $\delta\downarrow0$ 时的发散速度。

对于取**全部**源行的版本，甚至不需要最小秩。
只要原非零有限秩正见证湮灭 $SA'$，且实际 S 在 H 上单射，仍有
$$
\boxed{
p_i^{(n)}(A)1\to Cf_i\ \forall i
\quad\Longrightarrow\quad
\left\|\sum_{i=1}^r p_i^{(n)}(A)f_i\right\|\to\infty.
}
\tag{5.2}
$$
证明：若聚合向量有有界子列，弱极限 h 使 (2.3) 给
$\phi(F)=B(Fh,1)$。
在其中取 $F=SA^m$，得到
$B(Sh,A^m1)=0$ 对全部 $m\ge0$ 成立。
真空循环性迫 $Sh=0$，S 单射给 h=0，
随后 $\phi(I)=0$ 与正迹矛盾。
所以整个聚合范数趋于无穷。

(5.2) 保留了全部行之间的真实相消；
没有先分别要求每个 $X_{Cf_i}f_i$ 存在。
它既不是任意非湮灭态的反例，也不是从固定非湮灭 f 推测真正态的行为。

## 6. 与阻尼和共同核心的实际接口

若 R267 或另一构造能给第2节的固定少数源逼近，
并使这些具体 $h_\ell^{(n)}$ 有有界子列，就直接排除最小真见证。
系数算子范数是否有界已不是这个判据所需条件。

现有 R267 收缩强*单位只控制原有界乘子的作用，
没有自动给 (2.1) 的聚合源预算；
把一个无预算系数表左乘强单位也不能直接宣称 (4.4) 有界。
本文支付的是准确的误差、低秩极限和对偶成本，
尚未支付真实见证专属的成本上界。
普通复 Hilbert ISP 未由本稿完成。

## 7. 紧变化的源与相同的低秩极限

第2节的源无需在每一步准确固定。设 $G_n=(g_1^{(n)},\ldots,g_k^{(n)})$ 在 $H^{(k)}$ 中范数预紧，且
$$
e_i^{(n)}=x_i-\sum_{\ell=1}^kT_{i\ell}^{(n)}g_\ell^{(n)}
\longrightarrow0
\quad(i\in I),\qquad |I|=s>k,
$$
仍令
$$
h_\ell^{(n)}=\sum_{i\in I}T_{i\ell}^{(n)}f_i.
$$
则和第2节一样，
$$
\boxed{\left(\sum_\ell\|h_\ell^{(n)}\|^2\right)^{1/2}\longrightarrow\infty.}
\tag{7.1}
$$

证明：若有有界子列，利用源的范数预紧性和 Hilbert 球的弱紧性，进一步取
$$
g_\ell^{(n)}\to g_\ell,\qquad h_\ell^{(n)}\rightharpoonup h_\ell
\quad(1\le\ell\le k).
$$
第2节的准确误差恒等式逐个 n 仍成立。对每个固定有界 $F\in A'$，
$$
\begin{aligned}
B(Fh_\ell^{(n)},g_\ell^{(n)})-B(Fh_\ell,g_\ell)
={}&B(Fh_\ell^{(n)},g_\ell^{(n)}-g_\ell)\\
&+B(F(h_\ell^{(n)}-h_\ell),g_\ell).
\end{aligned}
$$
第一项的绝对值至多
$\|F\|\|h_\ell^{(n)}\|\|g_\ell^{(n)}-g_\ell\|\to0$；
第二项由弱收敛趋零。
于是得到第2节同一个至多 $r-s+k<r$ 项的准确整泛函表示，矛盾。
若还允许第3节的酉源框架，先同时取 $V_n\to V$，再使用其已付的误差估计即可。
没有将任何无界增长的系数算子移过框架极限。证毕。

本节需要源的范数预紧性；只有弱收敛时，两个变化向量的配对一般不能取极限。
它适用于 R267 中准确满足
$$
Q_n1\to1,\qquad PW_n1\to1
$$
的尾源或单位源，但不会自动产生相应的系数表或有界聚合预算。

## 8. 去掉不可见分量后的发散与归一弱零

先固定 $G$，沿用第4节的有界线性映射
$$
L_G:H^{(k)}\to\mathcal E,\qquad
(L_Gh)(F)=\sum_\ell B(Fh_\ell,g_\ell).
$$
记
$$
K_G=\ker L_G,\qquad
v_n=P_{K_G^\perp}h_n.
$$
这是 Hilbert 空间中对已经形成的聚合向量作正交投影；
不声称存在另一张系数表恰好生成 $v_n$。

因为 $L_Gv_n=L_Gh_n$，第2节的误差仍准确给
$$
\|\phi_I-L_Gv_n\|_{\mathcal E}
\le\sqrt{\tau_I}\,\varepsilon_n\longrightarrow0.
\tag{8.1}
$$
最小秩说明 $\phi_I\notin\operatorname{Ran}L_G$。如果 $v_n$ 有有界子列，
取其弱极限并在每个 F 上测试 (8.1)，就会得到
$\phi_I=L_Gv$，矛盾。因此
$$
\boxed{\|v_n\|\to\infty,\qquad
\frac{v_n}{\|v_n\|}\rightharpoonup0.}
\tag{8.2}
$$
第二项的证明也需保留：$\|L_Gv_n\|_{\mathcal E}$ 由 (8.1) 有界，
所以 $L_G(v_n/\|v_n\|)\to0$ 于 $\mathcal E$。
任一弱收敛子列的极限既在闭子空间 $K_G^\perp$ 中，
又被 $L_G$ 杀掉，因此必为零。
单位球弱紧且 $H^{(k)}$ 可分，故整个序列弱趋零。

在单源 $k=1$ 时，若 $g$ 对 $A'$ 循环，则
$$
L_gv=0
\Longrightarrow B(v,Fg)=0\quad(F\in A')
\Longrightarrow v=0.
$$
所以 $K_g=\{0\}$，(8.2) 直接用于原聚合向量 $h_n$。
这里包括 $g=1$，以及 R267 固定构造的 $g=P1$：
P 有稠密像且交换 $A'$，故 $P1$ 循环。
没有可正交删除的非零不可见向量来吸收原聚合向量的增长。

还有一个常用于变化源的准确版本。
若 $G_n\to G$ 于 $H^{(k)}$，$L_G$ 单射，
$\|h_n\|\to\infty$，且
$$
\|\psi_n-L_{G_n}h_n\|_{\mathcal E}\to0,\qquad
\sup_n\|\psi_n\|_{\mathcal E}<\infty,
$$
则同样有 $h_n/\|h_n\|\rightharpoonup0$。
事实上，
$$
\|L_G-L_{G_n}\|
\le\left(\sum_\ell\|g_\ell-g_\ell^{(n)}\|^2\right)^{1/2},
$$
故 $L_G(h_n/\|h_n\|)\to0$，任何弱聚点都属于 $\ker L_G=\{0\}$。
例如单源 $g_n\to1$ 或 $g_n\to P1$ 均满足此单射前提。
这一结论不把一般多源的 $L_G$ 免费视为单射。

## 9. 真正全行见证不能由固定强主理想因子阻尼成有界

本节使用第5节的全行情形，不需要最小秩。
固定非零有限秩正见证
$$
\phi(F)=\sum_{i=1}^r\langle Ff_i,f_i\rangle,\qquad
\phi(SA')=0,\qquad \phi(I)>0,
$$
并使用实际 S 在 H 上单射。
取一个固定循环源 $g$，允许单源系数 $T_i^{(n)}\in A'$，满足
$$
e_i^{(n)}=Cf_i-T_i^{(n)}g\to0,\qquad
h_n=\sum_iT_i^{(n)}f_i.
\tag{9.1}
$$

设固定 $R\in A'$ 满足**这个 R 自身的**强主理想条件
$$
I\in\overline{RA'}^{\mathrm{SOT}}.
\tag{9.2}
$$
则
$$
\boxed{\|Rh_n\|\to\infty,\qquad
\frac{Rh_n}{\|Rh_n\|}\rightharpoonup0.}
\tag{9.3}
$$

证明：在第2节误差式中以 RF 代 F，利用交换性得到
$$
\phi(RF)=B(FRh_n,g)
+\sum_i B(RFf_i,e_i^{(n)}).
\tag{9.4}
$$
最后一项的绝对值至多
$$
\varepsilon_n\left(\sum_i\|RFf_i\|^2\right)^{1/2}
\le\varepsilon_n\|R\|\sqrt{\phi(I)}\,\|F\|.
\tag{9.5}
$$
若 $Rh_n$ 有有界子列，取其弱极限 v，由 (9.4) 得
$$
\phi(RF)=B(Fv,g)\qquad(F\in A').
\tag{9.6}
$$
以 SF 代 F，左侧为零，所以
$$
B(FSv,g)=B(Sv,Fg)=0\qquad(F\in A').
$$
g 循环迫 $Sv=0$，S 单射迫 v=0。
(9.6) 遂给整个理想 $\phi(RA')=0$。
由于 $\phi$ 是有限个向量泛函之和，它对强算子收敛连续；
再用 (9.2) 得 $\phi(I)=0$，矛盾。
因此 $\|Rh_n\|\to\infty$。

由 (9.4)--(9.5)，$L_g(Rh_n)$ 在 $\mathcal E$ 中收敛于
正常泛函 $F\mapsto\phi(RF)$，因而有界。
第8节的 $\ker L_g=0$ 证明归一序列弱趋零。证毕。

如果 (9.1) 中的源变化为 $g_n\to g$，且极限 g 循环，结论仍然成立。
在假设 $Rh_n$ 有有界子列时，用第7节相同的“强源、弱聚合”极限即可得到 (9.6)；
得到发散后，再用第8节的变化源版本证明归一弱零。
全行酉框架也只改变误差表达，不改变同一个整泛函 $\phi$。

### 9.1 对 R267 固定 P 的准确适用范围

[R267 共同幂附录](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)
构造的特定非零 P 满足
$$
\|PW_n\|\le1,\qquad PW_n\to I\quad\text{强*}.
$$
因此这个固定 P 确实满足 (9.2)，可以在 (9.3) 中取 $R=P$。
这与仅知整个理想
$\mathfrak F_A=\bigcap_m A^mA'$
在强*拓扑稠密不同：
理想整体稠密不说明其中每个非零元的主理想都有强单位。

同样，对任意固定整数 $a\ge0,b\ge1$，构造中的 $R=A^aP^b$ 也满足 (9.2)。
准确地，R23 给最低 A 次数趋∞的收缩 $E_\ell=e_\ell(A)\to I$ 强*；
固定 a 后，充分大的 $\ell$ 有 $E_\ell=A^a B_\ell(A)$。
于是
$$
E_\ell(PW_n)^b
=(A^aP^b)\,B_\ell(A)W_n^b
$$
是 $A^aP^bA'$ 中的收缩，并在双指标极限强*趋 I。
所以 (9.3) 对这些固定因子全部成立。
不从这里推导任意变化 $a_n,b_n,P_n$ 的一致下界。

因此，R267 的固定强主理想因子不能把 (9.1) 中已经有效的真实全行逼近的聚合向量压成有界。
当前仍有意义的阻尼构造必须重新支付变化源、变化因子与目标误差的共同预算；
不能把强*单位趋 I 当作对这类归一弱零、原范数发散向量的统一控制。
上述结论仍未构造满足有界聚合预算的真实逼近，也未完成普通 ISP。


## 10. 只控制原有限源的变化阻尼

第9节的固定因子结论可以用于变化因子，而且不需要这些因子的算子范数一致有界。
本节明确保留真正需要的有限源收敛，以及极限泛函的非零锚。

仍使用全行真实见证，允许循环源变化为 $g_n\to g$，
其中极限 g 对 $A'$ 循环：
$$
e_i^{(n)}=Cf_i-T_i^{(n)}g_n\to0,\qquad
h_n=\sum_{i=1}^rT_i^{(n)}f_i.
\tag{10.1}
$$
取任意 $R_n\in A'$，只假设在原来的有限个源上有范数极限
$$
R_nf_i\longrightarrow u_i\in H
\qquad(1\le i\le r).
\tag{10.2}
$$
无需存在属于 $A'$ 的共同极限算子 $R$，
也不要求全空间强收敛或 $\sup_n\|R_n\|<\infty$。

定义正常泛函
$$
\psi_n(F)=\phi(R_nF),\qquad
\psi(F)=\sum_i\langle Fu_i,f_i\rangle.
$$
因 $R_nF=FR_n$，
$$
\|\psi_n-\psi\|_{\mathcal E}
\le\sum_i\|R_nf_i-u_i\|\,\|f_i\|\longrightarrow0.
\tag{10.3}
$$
而 $\psi_n(SF)=0$，所以
$$
\psi(SF)=0\qquad(F\in A').
\tag{10.4}
$$
假设这个极限泛函 $\psi$ 非零，则必有
$$
\boxed{\|R_nh_n\|\to\infty,\qquad
\frac{R_nh_n}{\|R_nh_n\|}\rightharpoonup0.}
\tag{10.5}
$$

证明：逐 n 将第2节的式子在 $R_nF$ 上测试，再用有界交换性，准确得到
$$
\psi_n(F)=B(FR_nh_n,g_n)
+\sum_i B(FR_nf_i,e_i^{(n)}).
\tag{10.6}
$$
关键的误差界是
$$
\left|\sum_i B(FR_nf_i,e_i^{(n)})\right|
\le\|F\|\varepsilon_n
\left(\sum_i\|R_nf_i\|^2\right)^{1/2}.
\tag{10.7}
$$
(10.2) 使最后的括号有界，故该误差在 $A'$ 单位球上一致趋零。
这里不出现 $\varepsilon_n\|R_n\|$；不能把不必要的整算子预算加回来。

若 $R_nh_n$ 有有界子列，利用 (10.3)、(10.6)--(10.7)
及强源—弱聚合的极限，得到
$$
\psi(F)=B(Fv,g)
$$
对某个弱极限 v 及全部 F 成立。
在此式中取 SF，由 (10.4) 得 $B(Sv,Fg)=0$。
g 循环及 S 单射迫 v=0，继而 $\psi=0$，与假设矛盾。
所以第一个结论成立。
再由 (10.3)、(10.6)--(10.7)，
$L_{g_n}(R_nh_n)$ 在 $\mathcal E$ 中收敛于 $\psi$。
第8节的变化源结论及 $\ker L_g=\{0\}$ 给归一弱零。证毕。

如果采用第3节的全行酉框架，结论也不变：
$\psi_n(F)=\phi(R_nF)$ 仍是同一个整泛函，且
$$
\sum_i\|R_nf_i^{(n)}\|^2=\sum_i\|R_nf_i\|^2.
$$
因此 (10.7) 的预算不变；无需将无界增长的 $R_n$ 作用于框架极限。

### 10.1 R267 的三个实际变化序列

特别，若 (10.2) 中 $u_i=Rf_i$，其中某个固定 $R\in A'$ 满足
$I\in\overline{RA'}^{\mathrm{SOT}}$，则极限
$\psi(F)=\phi(RF)$ 自动非零。
否则 $\phi(RA')=0$，由有限向量泛函的强连续性会得到
$\phi(I)=0$。
于是 (10.5) 对这类有限源收敛全部适用，即使
$\|R_n\|\to\infty$。

R267 的固定构造有以下三个具体实例：

| 变化因子 $R_n$ | 已证的有限源极限 | 非零极限泛函 |
|---|---|---|
| 收缩有限前缀 $P_n$ | $P_nf_i\to Pf_i$ | $F\mapsto\phi(PF)$；特定 P 的主理想有收缩强*单位 |
| 收缩尾积 $Q_n$ | $Q_nf_i\to f_i$ | $\phi$ |
| 收缩主理想单位 $PW_n$ | $PW_nf_i\to f_i$ | $\phi$ |

因此这些自然变化因子也不能把已经满足 (10.1) 的聚合向量变为有界。
这一证明没有估计 $(R_n-R)h_n$；
该差作用于增长向量通常没有可用控制。
合法极限完全取在固定有限源 $f_i$ 上，再经准确误差恒等式传回泛函。

相反，若某个变化阻尼使有限源极限存在，但得到 $\psi=0$，
本节没有矛盾：它可能已经丢失了整泛函的非零锚。
如果只有弱有限源极限，不能直接使用 (10.7) 之后的预对偶范数收敛。
新增 §11 用密集右测试代替这个极限步骤，已证明弱有限源极限及更一般的实际误差预算也足够。

### 10.2 与已经登记的静态配对禁阻的区别

R267 共同幂附录 §8 已经排除其固定 P 对真实见证的
固定真空向量表示。
第9--10节不把该静态不表示性重算为新结论；
增加的是任意实际近似系数表中的聚合范数必发散、
归一向量必弱零，以及只控制原有限源的变化阻尼版本。
这些结果仍是实际源预算的必要约束。
目前没有构造有界聚合预算，也没有闭合普通 ISP。

## 11. 只保实际误差与一个右锚的统一阻尼定理

本节去掉第10节中原有限源必须按范数收敛的前提。
保留的是实际泛函误差趋零和一个固定测试上的非零锚。
既不要求变化泛函有预对偶范数极限，也不要求阻尼算子有任何算子拓扑极限。

### 11.1 一个不取变化泛函极限的引理

仍在原实际 $A'$ 上工作。
设 $S\in A'$ 单射、稠密像，$g$ 对 $A'$ 循环，
$g_n\to g$ 于 $H$。
取 $x_n\in H$ 及正常泛函 $\psi_n$，满足
$$
\psi_n(SA')=0,\qquad
\left|\psi_n(F)-B(Fx_n,g_n)\right|
\le\epsilon_n\|F\|\quad(F\in A'),\qquad
\epsilon_n\to0.
\tag{11.1}
$$
不要求 $\|\psi_n\|$ 一致有界。
则：

1. 若 $x_n$ 有界，则每个固定 $F\in A'$ 都有 $\psi_n(F)\to0$。
2. 若存在固定 $F_0\in A'$、$c>0$，最终有
   $|\psi_n(F_0)|\ge c$，则
   $$
   \boxed{\|x_n\|\to\infty,\qquad x_n/\|x_n\|\rightharpoonup0.}
   \tag{11.2}
   $$
3. 更一般，只要 $x_n\ne0$ 且
   $\epsilon_n/\|x_n\|\to0$，就有第二个归一弱零结论，
   不需要非零锚。

证明始终使用同一个准确残差。令
$$
r_n(F)=\psi_n(F)-B(Fx_n,g_n).
$$
对任意固定 $F,G\in A'$，因 $\psi_n(SG)=0$，
以及原有界交换子的共同 $C$ 对称性，
$$
\boxed{
\psi_n(F)
=B(x_n,(F-SG)g_n)+r_n(F-SG).
}
\tag{11.3}
$$
因此
$$
|\psi_n(F)|
\le\|x_n\|\,\|(F-SG)g_n\|
+\epsilon_n\|F-SG\|.
\tag{11.4}
$$
集合 $\{SGg:G\in A'\}$ 稠密于 $H$：
先用 $g$ 的循环性逼近任意输入，再用 $S$ 的稠密像。
若 $\|x_n\|\le L$，对任意 $\eta>0$ 先选一个固定 $G$，
使 $\|(F-SG)g\|<\eta$。
随后 $g_n\to g$、$\epsilon_n\to0$ 给
$\limsup_n|\psi_n(F)|\le L\eta$。
令 $\eta\downarrow0$，证明第一项。
它也排除第二项中的任何有界子列，故范数趋于无穷。

为证明归一弱零，在 (11.1) 中直接测试 $SG$：
$$
\left|B\!\left(\frac{x_n}{\|x_n\|},SGg_n\right)\right|
\le\frac{\epsilon_n}{\|x_n\|}\|SG\|\to0.
$$
把 $g_n$ 换成 $g$ 的误差至多
$\|SG\|\,\|g_n-g\|\to0$。
再由 $SGg$ 的稠密性和归一向量的有界性，得到弱零。
这里不用变化 $\psi_n$ 在其他测试上的一致界。证毕。

### 11.2 原全行系数表与弱有限源极限

回到第10节准确的全行表：
$$
e_i^{(n)}=Cf_i-T_i^{(n)}g_n,\quad
\varepsilon_n^2=\sum_i\|e_i^{(n)}\|^2\to0,\quad
h_n=\sum_iT_i^{(n)}f_i,\quad g_n\to g,
$$
其中极限 $g$ 循环。
对任意 $R_n\in A'$，只需支付
$$
\boxed{
\varepsilon_n
\left(\sum_i\|R_nf_i\|^2\right)^{1/2}\longrightarrow0.
}
\tag{11.5}
$$
令 $\psi_n(F)=\phi(R_nF)$、$x_n=R_nh_n$，
第10节的真实误差式准确给 (11.1)。
所以，若一个固定右锚
$$
|\phi(R_nF_0)|\ge c>0
$$
最终保持，则
$$
\boxed{
\|R_nh_n\|\to\infty,\qquad
R_nh_n/\|R_nh_n\|\rightharpoonup0.
}
\tag{11.6}
$$
原 $R_nf_i$ 不必收敛，$\|R_n\|$ 也不必有界。
若只在某子列保锚，则结论准确应用于该子列。

特别，第10节的有限源范数收敛可以放宽为
$$
R_nf_i\rightharpoonup u_i\quad\text{于 }H\quad(1\le i\le r),
\tag{11.7}
$$
只要正常泛函
$$
\psi(F)=\sum_i\langle Fu_i,f_i\rangle
$$
非零。
弱收敛使有限个 $\|R_nf_i\|$ 一致有界，故 (11.5) 成立；
且每个固定 $F$ 有 $\phi(R_nF)\to\psi(F)$，
一个非零测试便给所需右锚。
本节没有把这种逐测试收敛提升为预对偶范数收敛。

### 11.3 固定源时的定量分离式

若 $g_n=g$ 固定，(11.4) 直接给
$$
\boxed{
\|x_n\|
\ge
\sup_{G\in A'}
\frac{\bigl(|\psi_n(F)|-\epsilon_n\|F-SG\|\bigr)_+}
{\|(F-SG)g\|}.
}
\tag{11.8}
$$
零分母按第4节相同约定解释。
这只是由准确残差给出的下界，不宣称新的等号对偶式。

给定 $F$、$c>0$、$L<\infty$，
先选固定 $G$ 使
$$
\|(F-SG)g\|<\frac{c}{2\max(L,1)}.
$$
置
$$
\eta_{F,c,L}
=\frac{c}{2(1+\|F-SG\|)}>0.
\tag{11.9}
$$
则任何满足 $|\psi_n(F)|\ge c$、$\|x_n\|\le L$
的实际表示都必须有
$$
\epsilon_n\ge\eta_{F,c,L}.
\tag{11.10}
$$
该常数依赖实际稠密像逼近的 $G$，
没有免费给它一个与 $F,c,L$ 无关的速度。

## 12. 同一正密度的精确截断源与被阻尼的真尾预算

本节把上面的统一分离应用于
[R230 正密度截断稿 §4.1](R230-appendix-positive-density-walsh-truncation-and-small-trace-tail-improvement.md)
的新精确源。
允许原 $\rho\ge0$ 为任意非零迹类，不要求有限秩。
仍假设 $\phi=\varphi_\rho$ 湮灭原单射、稠密像的慢理想 $SA'$。

令 $\Pi_p$ 为前 $p$ 位 Walsh 柱投影，
$$
\rho=\sum_i f_i\otimes f_i,\qquad
b_{i,p}=(I-\Pi_p)f_i,\qquad
\sigma_p=(I-\Pi_p)\rho(I-\Pi_p),\qquad
\delta_p=\operatorname{Tr}\sigma_p\to0.
$$
R230 给实际 $h_p\in H$，使
$$
\boxed{
\phi(F)=B(Fh_p,\Omega)+\varphi_{\sigma_p}(F)
\quad(F\in A'),\qquad
\|\phi-\Phi_{h_p}\|_{(A')_*}=\delta_p.
}
\tag{12.1}
$$
这是全部实际 $A'$ 上的等式。
$\sigma_p$ 保留真实纠缠，通常不湮灭 $S$。

### 12.1 一个比整算子范数更精确的误差

对任意有界 $R\in A'$，定义
$$
\epsilon_p(R)=
\left\|F\mapsto\varphi_{\sigma_p}(RF)\right\|_{(A')_*}.
\tag{12.2}
$$
由实际交换性、原正平方分解和 Cauchy--Schwarz，
$$
\begin{aligned}
|\varphi_{\sigma_p}(RF)|
&=\left|\sum_i\langle FRb_{i,p},b_{i,p}\rangle\right|\\
&\le\|F\|\sqrt{\delta_p}
 \left(\sum_i\|Rb_{i,p}\|^2\right)^{1/2}.
\end{aligned}
$$
所以
$$
\boxed{
\epsilon_p(R)
\le
\sqrt{\delta_p}
\left(\sum_i\|Rb_{i,p}\|^2\right)^{1/2}
\le\delta_p\|R\|.
}
\tag{12.3}
$$
中间项仅检查原正尾的实际像；
不把它替换为一个未付的全空间界。

对任意 $F,G\in A'$，一次使用 (12.1) 即有
$$
\boxed{
\phi(RF)
=B(Rh_p,(F-SG)\Omega)
+\varphi_{\sigma_p}(R(F-SG)).
}
\tag{12.4}
$$
因为 $\phi(RSG)=0$，(12.4) 没有额外的湮灭余项。
于是
$$
\boxed{
|\phi(RF)|
\le
\|Rh_p\|\,\|(F-SG)\Omega\|
+\epsilon_p(R)\|F-SG\|.
}
\tag{12.5}
$$

### 12.2 任意交换阻尼的统一结论

取任意 $R_p\in A'$。
若
$$
\epsilon_p(R_p)\to0,
$$
且在某个固定 $F_0$ 上最终有
$|\phi(R_pF_0)|\ge c>0$，则
$$
\boxed{
\|R_ph_p\|\to\infty,\qquad
R_ph_p/\|R_ph_p\|\rightharpoonup0.
}
\tag{12.6}
$$
若 $\|R_ph_p\|$ 有界，则所有固定右锚
$\phi(R_pF)\to0$。
这直接应用 §11，取 $g_p=\Omega$；
不要求 $R_pf_i$ 收敛，不要求 $\phi(R_p\,\cdot)$ 有极限。

它还是一个统一的预算分离。
对固定 $F,c,L$，按 (11.9) 取常数 $\eta_{F,c,L}>0$。
任意 $p,R$ 若满足
$$
|\phi(RF)|\ge c,\qquad \|Rh_p\|\le L,
$$
就必须支付
$$
\boxed{
\epsilon_p(R)\ge\eta_{F,c,L},\qquad
\delta_p\|R\|\ge\eta_{F,c,L}.
}
\tag{12.7}
$$
当 $\delta_p>0$ 时还必须有
$$
\boxed{
\|R\|\ge\frac{\eta_{F,c,L}}{\delta_p},
\qquad
\left(\sum_i\|Rb_{i,p}\|^2\right)^{1/2}
\ge\frac{\eta_{F,c,L}}{\sqrt{\delta_p}}.
}
\tag{12.8}
$$
若 $\delta_p=0$，上述非零锚和有界源的组合本来就不可能。
因此同时保锚并压住这一精确源的构造，
必须实际放大同一个原正尾；仅报告源范数下降不够。

### 12.3 标量重整化、非正行及范围边界

例如可以取
$$
R_p=c_p e^{-X_{a^{(p)}}},\qquad
a^{(p)}\ge0,\quad a^{(p)}\in\ell^2,\quad c_p\in\mathbb C.
$$
这里 $c_p$ 可以发散，正热有效行也可以任意改变。
只要这些完整算子满足
$$
\delta_p\,|c_p|\,\|e^{-X_{a^{(p)}}}\|\to0,
\tag{12.9}
$$
就属于 (12.6) 的范围。
特别，任意算子范数一致有界的标量重整化正热族均被覆盖。
更一般，(12.3) 的实际尾像预算趋零也已经足够，
即使 (12.9) 未知或失败。

同样的定理直接适用于任意其他有界 $A'$ 因子，
包括非正构造、有限预解积、R267 的变化因子；
每一步仍须支付 (12.2) 或其已证上界。
这里没有从算子的名称推出尾预算。

本节的 $h_p$ 是 (12.1) 的精确全代数截断源，
不是普通有限头矩 $v_p$，也不是任意未知重构表的输出。
若要替换为另一个源，必须另付被阻尼后的误差。
本节没有证明满足 (12.7) 的巨大尾放大不可能，
也未构造一般正常见证专属的有界源，普通 ISP 仍开。

