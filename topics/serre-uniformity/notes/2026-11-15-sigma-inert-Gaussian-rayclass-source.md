# 惰性 harmonic-seven 源的四个固定 Gaussian CM 形式

日期：2026-11-15。状态：**以下固定字符分解、尺度、一次原函数、惰性 Hecke 关系与原 FG 接口已证明；尚未计算指定有限运输系数，亦未证明其原 CM 值或筛后非零。** 本文不新增素数窗口。

接 [原惰性 harmonic-seven 源](2026-11-15-sigma-inert-Gaussian-harmonic-seven-source.md)，简称 IH；所有 sigma、$U$、$\mathcal P$、$Q$ 以及 FG 规范仍取 [R812](../results/R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)。本篇只将 IH 的固定输入进一步分解，不更换原函数。

## 1. 原频率矩阵与一个独立的 q 变量

令
$$
\mathcal O=\mathbf Z[i],\qquad \pi_2=1+i,\qquad
\xi_8=(1+i)/\sqrt2,\qquad \xi_8^8=1,
$$
其中 $i,\sqrt2$ 是特征零指定根。设 $q_*=q^{1/12}$，只把它用作级数变量。对 $c=r+is\in\mathcal O/6\mathcal O$ 定义
$$
T_c(q_*)=\sum_{w\equiv c\ (6)}w^7q_*^{w\bar w}.
\tag{GC1}
$$
零频率项为零。原 IH 的 harmonic theta 矩阵准确为
$$
\mathcal T_{7,rs}(q)=
\frac{T_{r+is}(q_*)-T_{r-is}(q_*)}{2i}.
\tag{GC2}
$$
这里的分母是 $2i$；不是把某个不同归一的实部或虚部换进 IH。

对 $u\in\{1,i,-1,-i\}$，重新编号 $w=uv$ 给
$$
T_{uc}=u^7T_c=u^{-1}T_c.
\tag{GC3}
$$
若 $3\mid c$，则 $c=-c\bmod6$，故 (GC3) 迫 $T_c=0$。
余下 32 个特征在 Gaussian 单位作用下各有四元轨道，共八个轨道。这只是固定模六结构，与 $p$ 无关。

## 2. 四个准确的有限字符

在 $\mathcal O/3\simeq\mathbf F_9$ 中，$g=1+i$ 的阶为八：
$$
g^2=-i,\qquad g^4=-1,\qquad g^6=i.
\tag{GC4}
$$
对 $b\in\mathbf Z/8$ 令
$$
\epsilon_b(g)=\xi_8^b.
$$
在 $(\mathcal O/2)^\times=\{1,i\}$ 上令 $\delta(1)=1,\delta(i)=-1$。
因此 $\epsilon_b(i)=\xi_8^{6b}=i^{-b}$。
使
$$
\varepsilon(u)u^7=1\quad(u\in\mathcal O^\times)
\tag{GC5}
$$
成立的模六乘法字符恰为
$$
\epsilon_3,\ \epsilon_7,\ \delta\epsilon_1,\ \delta\epsilon_5.
\tag{GC6}
$$
例如不能在选定 $g=1+i$ 后又把 $i$ 误当成 $g^2$，这会交换两组角色。

Gaussian 整数环是 Euclidean 环，所以每个非零理想可取一个生成元。定义
$$
\psi_b((w))=\epsilon_b(w)w^7\quad(b=3,7),
$$
$$
\widetilde\psi_b((w))=\delta(w)\epsilon_b(w)w^7
\quad(b=1,5).
\tag{GC7}
$$
(GC5) 保证它们不依赖生成元的 Gaussian 单位。第一组的准确 conductor 为 $3\mathcal O$，第二组为 $6\mathcal O$：第一组的模三字符非平凡；第二组在模三因子及 $(\mathcal O/2)^\times$ 上均非平凡，而模 $(1+i)$ 的单位群平凡，故其二部 conductor 恰为 $(1+i)^2=(2)$。

定义标准整数指数 theta 级数
$$
F_b(t)=\sum_{(\mathfrak a,3)=1}\psi_b(\mathfrak a)t^{N\mathfrak a}
\quad(b=3,7),
$$
$$
G_b(t)=\sum_{(\mathfrak a,6)=1}
\widetilde\psi_b(\mathfrak a)t^{N\mathfrak a}
\quad(b=1,5).
\tag{GC8}
$$
四者首项均为 $t$，系数在 $\mathbf Z[\xi_8]$ 中。

Hecke theta 定理准确给：$F_3,F_7$ 是权八、level $36$ 的 CM 新形式；
$G_1,G_5$ 是权八、level $144$ 的 CM 新形式。四者 nebentypus 都是
$$
\chi_{-4}\chi_{-3}=\chi_{12}.
\tag{GC9}
$$
这里没有套用“有理 Fourier 系数”的特殊情形；四个字符的值允许落在 $\mathbf Q(\xi_8)$。
所用一般定理是 Schütt, *CM newforms with rational coefficients*, arXiv:math/0511228v5，Theorem 1.4，PDF 第 3 页；其公式为 weight $l+1$、level $|D_K|N\mathfrak f$、nebentypus $\chi_K\varepsilon|_{\mathbf Z}$。

令
$$
\alpha_b=\psi_b((1+i))
=\epsilon_b(\pi_2)\pi_2^7.
$$
则
$$
\alpha_3=8i\sqrt2,\qquad \alpha_7=-8i\sqrt2,
\qquad \alpha_b^2=-2^7.
\tag{GC10}
$$
例如 $\pi_2^7=8(1-i)$，所以这些相位直接由 (GC4) 核定。

## 3. 全部 36 个特征的精确分解

以下公式逐类覆盖全部 $c\bmod6$；无须用有限 q 展开拟合。

### 3.1 c 是模六单位

在这一类中，$c$ 的两个整数坐标奇偶相反，且 $3\nmid c$。
对 $b=3,7$，从 $F_b$ 中删去被 $\pi_2$ 整除的理想给
$$
F_b^{(6)}(t)=F_b(t)-\alpha_bF_b(t^2).
\tag{GC11}
$$
因此乘法字符正交准确给
$$
\boxed{
T_c(t)=\frac14\left[
\sum_{b=3,7}\epsilon_b(c)^{-1}
 \bigl(F_b(t)-\alpha_bF_b(t^2)\bigr)
+\sum_{b=1,5}(\delta(c)\epsilon_b(c))^{-1}G_b(t)
\right].
}
\tag{GC12}
$$
证明其 $1/4$：$(\mathcal O/6)^\times$ 有 16 元；
$\sum_c\varepsilon(c)T_c=4F_\varepsilon^{(6)}$，
而 (GC3) 使其余十二个乘法字符的 Fourier 分量为零。
逆 Fourier 变换因此是 $4/16$。

### 3.2 c 被 pi_2 整除，但不被 2 整除

此时 $c$ 的两个坐标均为奇数，且 $3\nmid c$。
置 $d=c/\pi_2\bmod3$。选择 $c$ 的代表不影响这个 $d$。
写 $w=\pi_2v$，条件 $w\equiv c\bmod6$ 等价于
$v\equiv d\bmod3$ 且 $\pi_2\nmid v$。
模三版本的字符正交给
$$
\sum_{v\equiv d\ (3)}v^7t^{N v}
=\frac12\sum_{b=3,7}\epsilon_b(d)^{-1}F_b(t).
\tag{GC13}
$$
在其中删去 $v=\pi_2u$，得到
$$
\boxed{
T_c(t)=\frac{\pi_2^7}{2}
\sum_{b=3,7}\epsilon_b(d)^{-1}
\bigl(F_b(t^2)-\alpha_bF_b(t^4)\bigr).
}
\tag{GC14}
$$
范数二所造成的 $t^2,t^4$ 和两处 $\pi_2^7$ 均被保留。

### 3.3 c 被 2 整除，且 3 不整除 c

置 $d=c/2\bmod3$。写 $w=2v$ 并用 (GC13)，得到
$$
\boxed{
T_c(t)=2^6\sum_{b=3,7}\epsilon_b(d)^{-1}F_b(t^4).
}
\tag{GC15}
$$
其首常数来自 $2^7/2$，不能改成 $2^7$。

最后，$3\mid c$ 的四个特征按 (GC3) 恒为零。
(GC12)、(GC14)、(GC15) 的类别数分别为 16、8、8。

## 4. 八个固定矩阵是原 even-by-odd 空间的一组整基

将八个级数按次序写为
$$
\boldsymbol f(t)=
(F_3(t),F_3(t^2),F_3(t^4),
 F_7(t),F_7(t^2),F_7(t^4),G_1(t),G_5(t))^t.
\tag{GC16}
$$
令 $C_\nu(r,s)$ 是 (GC12)、(GC14)、(GC15) 中
$T_{r+is}$ 在第 $\nu$ 项前的准确常数；定义
$$
M_\nu(r,s)=
\frac{C_\nu(r,s)-C_\nu(r,-s)}{2i}.
\tag{GC17}
$$
于是
$$
\boxed{\mathcal T_7(q)=\sum_{\nu=1}^8 M_\nu f_\nu(q_*).}
\tag{GC18}
$$
每个 $M_\nu$ 对 $r\mapsto-r$ 为偶，对 $s\mapsto-s$ 为奇。
所以它属于维数 $4\cdot2=8$ 的原 even-by-odd 矩阵空间。

这八个常数矩阵在 $\mathbf Z[\xi_8,1/2]$ 上构成一组基。
可不计算行列式而证明这一点：

第一，在 16 个模六单位上，四个 (GC6) 字符的 Fourier 矩阵可逆，
其逆只除以四或十六；在后两类上，两个模三字符矩阵的逆只除以二或八。
将 (GC16) 改为
$$
F_b(t)-\alpha_bF_b(t^2),\quad
\pi_2^7\bigl(F_b(t^2)-\alpha_bF_b(t^4)\bigr),\quad
2^7F_b(t^4)
\tag{GC19}
$$
及两个 $G_b$，是上三角可逆变换；其对角只包含二的幂和 $\pi_2^7$，
均在该环中为单位。因此 $C_\nu$ 是满足 (GC3) 的八维函数空间的一组基。

第二，若 $T$ 满足 (GC3)，并令
$H(c)=(T(c)-T(\bar c))/(2i)$，则
$$
\boxed{T(c)=iH(c)-H(ic).}
\tag{GC20}
$$
这是使用 $T(ic)=-iT(c)$ 以及
$T(-i\bar c)=iT(\bar c)$ 的直接展开。
故 $T\mapsto H$ 单射，且其像恰为上述八维 even-by-odd 空间。
(GC20) 也不引入任何奇素数分母。
于是 (GC17) 在每个 $p>2$ 的剩余域中仍是一组基。
这没有证明原 CM 值向量非零。

## 5. 一次原函数的全部 oldform 尺度

对 (GC8) 中任一 $f(t)=\sum_{n\ge1}a_n(f)t^n$ 定义
$$
J_f(t)=\sum_{n\ge1}\frac{a_n(f)}n t^n.
$$
对于 (GC16) 中的 $f_\nu(t)=f(t^{d_\nu})$，其中
$d_\nu\in\{1,2,4\}$，置
$$
\mathscr J_\nu(t)=\frac1{d_\nu}J_f(t^{d_\nu}).
\tag{GC21}
$$
这保证 $\theta_t\mathscr J_\nu=f_\nu$，而不是漏掉一个 oldform 指数。

IH 的原函数因此恰为
$$
\boxed{\mathcal E(q)=\sum_{\nu=1}^8 M_\nu\mathscr J_\nu(q_*).}
\tag{GC22}
$$
因为每项原分母就是 $Nw$，且 $\theta_q=\theta_{q_*}/12$，
(GC22) 准确复现 IH 的 $\theta_q\mathcal E=\mathcal T_7/12$。
本文始终只取一次原函数；没有把它冒认成权八形式的七次标准 Eichler 积分。

## 6. 所有惰性 p 的 Hecke 多项式与整性

设 $p\ge41,\ p=11\bmod12$。则 $p$ 在 $\mathbf Q(i)$ 惰性，
且 $p\nmid6$。对四个 (GC8) 的形式，都没有范数为 $p$ 的 Gaussian 理想，故
$$
a_p(f)=0.
$$
唯一范数为 $p^2$ 的理想是 $(p)$；因为 $p\equiv-1\bmod6$，
四个有限字符在 $p$ 上都是 $-1$，于是
$$
\psi((p))=-p^7.
\tag{GC23}
$$
因此原 Hecke 多项式为
$$
\boxed{T^2+p^7.}
\tag{GC24}
$$
采用这个 Hecke 规范的二维 Frobenius 满足平方为 $-p^7I$；
没有指定一个未经比较的 integral crystalline 基。

直接按理想的 $(p)$-次数分解，也得到全部 Fourier 系数关系
$$
a_{p^{2j}m}(f)=(-p^7)^j a_m(f)\quad(p\nmid m),
\qquad
a_{p^{2j+1}m}(f)=0.
\tag{GC25}
$$
于是 $J_f$ 在这些 p 处逐系数整，且
$$
U_pJ_f=-p^5V_pJ_f,\qquad
J_f^{[p]}(t)=J_f(t)+p^5J_f(t^{p^2}).
\tag{GC26}
$$
这里 $U_p(\sum b_nt^n)=\sum b_{pn}t^n$，
$V_p(\sum b_nt^n)=\sum b_nt^{pn}$，
$[p]$ 表示删去指数被 p 整除的项。
特别，若 $n=p^{2j}m$，则 $a_n(f)/n$ 的 p 赋值至少为 $5j$；
这与 IH 对分母 $a^2+b^2$ 的直接整性核对完全一致。

(GC24) 的两条 Newton 斜率都是 $7/2$；一次原函数的 (GC26) 含 $p^5$。
因此这些关系不是一个可任意设成一的 ordinary unit-root 归一。
它们也没有评价原 supersingular 点的指定 FG 条目。

## 7. 在原 CM 点保留共同尺度的八项接口

继续 IH 的
$$
\mathcal P=A^5\lambda^{p+4}\eta^{-2},\qquad
Q-Q_{\rm poly}=\frac{\mathcal P}{32}U_e\overline{\mathcal E}U_o^t,
$$
且 $Q_{\rm poly}(P_0)=0$。
由 (GC22) 得准确函数域恒等式
$$
Q-Q_{\rm poly}=
\frac1{32}\sum_{\nu=1}^8
 U_e M_\nu U_o^t\,
 \overline{\mathcal P\mathscr J_\nu(q_*)}.
\tag{GC27}
$$

这里各个被加项的 CM 评价可以作为代数对象严格定义，
而不先把 $q_*,\lambda,\eta$ 单独代入 $P_0$。
确实，R812 的 $U$ 与逆在原 CM 点的 tame 盖上正则，
原 $Q-Q_{\rm poly}$ 正则；其在 even-by-odd 子空间上的逆运输说明
$\mathcal P\overline{\mathcal E}$ 的全部八个坐标正则。
再由 (GC17) 的整基及其在 $p>2$ 的单位逆，
每个 $\overline{\mathcal P\mathscr J_\nu}$ 都具有同一个函数域中的正则延拓。
定义
$$
e_{\nu,p}=
\left.\overline{\mathcal P\mathscr J_\nu(q_*)}\right|_{P_0}
\tag{GC28}
$$
指这个正则延拓值。它不是未经证明的特征零 Eichler CM 值的直接约化。

R812 已固定 $U(P_0)=c\widehat U$，其中
$c^6=-d_0^{-16}/\det\widehat U$，且其实际公开计算证明
$c,\widehat U,\widehat U^{-1}$ 在所有本篇 p 都是单位数据。
在固定复合域
$$
K_*=\mathbf Q(\sqrt[3]4,\sqrt3,i,\sqrt2)
$$
中定义
$$
\kappa_\nu=[\widehat U M_\nu\widehat U^t]_{FG}.
\tag{GC29}
$$
于是原未筛目标准确等于
$$
\boxed{
(6B)^5\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j
=\frac{c^2}{32}\sum_{\nu=1}^8\kappa_\nu e_{\nu,p}.
}
\tag{GC30}
$$
共同尺度此处是 $c^2$，因为 (GC27) 没有 split 分支的逐条目 Frobenius；
不得从 R812 的另一公式搬来 $c^{2-2p}$。

(GC29) 是一个固定 36 特征、八项的有限代数运输任务。
只需原 R812 的 Miller/Heisenberg 基和 (GC12)--(GC17)，不需要计算任何 p 窗口。
即使算得全部非零 $\kappa_\nu$ 都为单位，也仍必须证明
(GC30) 的实际 $e_{\nu,p}$ 不在该 FG 超平面上；可逆矩阵不能代替这一点。

另外，在 $P_0$ 原 CM 特征迫 $Q$ 的八个 even-by-odd 条目中
只有 FG 和 HJ 可以非零。
因此八个 $e_{\nu,p}$ 满足由
$\widehat U M_\nu\widehat U^t$ 给出的六条精确线性关系。
这些关系将原值向量限制在二维子空间，但不证明指定 FG 值非零，
也不把它与 HJ 值随意相认。

## 8. 范围

本篇新增的是原 harmonic-seven 源的四个固定 CM 形式、全部模六特征的
准确分解及 oldform 尺度、原惰性 Hecke 多项式、一次原函数的 p 整性关系，
以及可按固定代数算子核对的原 FG 八项接口。

没有证明 $e_{\nu,p}$ 的指定组合为单位。
即使 (GC30) 将来成为非零定理，它仍只是未筛交替卷积。
原 R770 同一本原标签的 Legendre 与两条 Cartier 因子共同非零仍是独立缺口。
本篇也不以“固定 CM motive”或 positive Newton slopes 代替实际 period 比较。

外部一般输入仅为：
Matthias Schütt, *CM newforms with rational coefficients*,
[arXiv:math/0511228v5](https://arxiv.org/pdf/math/0511228),
Theorem 1.4，PDF 第 3 页。其余有限字符、常数和系数恒等式均已在正文证明。
