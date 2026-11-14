# R271 附录：玻色双 Fock 塔与二次碰撞条件数

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_rebuild。
状态：已证明。新增的是全部不同出生列的准确玻色双塔表示及原 canonical Fock 同构的二次碰撞条件数。后文的平方根前缀应用只是旧已闭范围内的另一证明：[R239 联合核短塔](R239-appendix-short-flag-towers-and-near-linear-nonvacuum-prefix-removal.md) 已给更大的 $q^{1-o(1)}$ 前缀窗口，不把本稿应用重计为范围扩张。

## 1. 同一 canonical 塔和新的条件数

取有限正行或无限正 $\ell^2$ 行 $a$，保留原平方自由孔层、删除和 primitive 空间
$$
D=\sum_i a_iE_i,\quad S=\sum_i a_i^2,
\quad\delta=\frac{\max_i a_i^2}{S},
\quad K_b=\ker D\cap\mathcal H_b,
\quad K_0=\mathcal H_0.
$$
固定最高孔层 $P\ge1$，令
$$
\mathfrak F_p=\bigoplus_{b=0}^p K_b\quad(0\le p\le P)
$$
为外部正交直和。假设
$$
\boxed{\epsilon_P:=\frac43\delta P^2<1.}
\tag{1.1}
$$
此时 $2(p-1)\delta<1$ 对全部 $p\le P$ 成立。
准确交换子给
$$
D_pD_p^*\succeq S(1-2(p-1)\delta)I,
$$
所以每个 $D_p$ 满射，并有原单步最小右逆
$$
R_p=D_p^*(D_pD_p^*)^{-1}.
$$

与[R239 低孔 Fock 塔](R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)完全相同，定义
$$
V_p(k_0,\ldots,k_p)
=\sum_{b=0}^p\sqrt{(p-b)!S^{p-b}}\,
R_pR_{p-1}\cdots R_{b+1}k_b.
\tag{1.2}
$$
新生分量的空乘积为恒等。标准降阶为
$$
\mathfrak a_p(k_b)_{b\le p}
=(\sqrt{(p-b)S}\,k_b)_{b<p}.
$$

**定理 1.1。** (1.2) 是有界同构，准确满足
$$
D_pV_p=V_{p-1}\mathfrak a_p,
$$
并且在全部不同出生的整个外直和上有
$$
\boxed{
I\preceq V_p^*V_p\preceq(1-\epsilon_P)^{-1}I,
\quad
\|V_p\|\le(1-\epsilon_P)^{-1/2},
\quad \|V_p^{-1}\|\le1.
}
\tag{1.3}
$$
这些界对正交直和 $V_{\le P}$ 仍成立，且不再乘孔层数。
因此整个 canonical 塔的条件数至多
$$
\boxed{\kappa_P=(1-\epsilon_P)^{-1/2}.}
\tag{1.4}
$$
相较旧充分条件 $\delta[32(P+1)]^P\ll1$，新增的是实际跨出生 Gram 的 $P^2\delta$ 预算；不是仅控制每条单独的最小逆链。

## 2. 玻色空间中的正交创建列

使用[全出生最小逆稿](R271-appendix-all-birth-low-occupation-bosonic-minimal-gram-comparison.md) §3 的真正玻色空间：第 $p$ 层有正交基 $e_\alpha$，$\alpha_i\ge0$、$\sum_i\alpha_i=p$。令
$$
b_i^*e_\alpha=\sqrt{\alpha_i+1}\,e_{\alpha+\mathbf e_i},
\quad
b_ie_\alpha=\sqrt{\alpha_i}\,e_{\alpha-\mathbf e_i},
\quad
\mathcal B=\sum_i a_ib_i.
$$
各固定层有界且 $[\mathcal B,\mathcal B^*]=SI$。
原平方自由层按 $e_I\mapsto e_{1_I}$ 等距嵌入，投影记为 $Q_p$。
原删除是准确限制 $\mathcal B|_{\mathcal H_p}=D_p$，故每个 $K_b$ 都包含于真正的 $\ker\mathcal B$。

对 $r\ge0$ 和 $f\in K_b$ 定义
$$
\mathcal U_{b,r}f
=\frac{(\mathcal B^*)^r f}{\sqrt{r!S^r}}.
$$
CCR 给 $\|\mathcal U_{b,r}f\|=\|f\|$。
固定总层 $p=b+r$ 后，不同 $b$ 的这些像彼此正交：
若两个创建次数不同，在内积中移去共同次数后，剩余正次删除作用到一个 primitive 向量，内积为零。
因此
$$
\boxed{
\mathcal U_p:\mathfrak F_p\longrightarrow\mathcal F_p^{\rm bos},
\qquad
\mathcal U_p(f_b)=\sum_{b=0}^p\mathcal U_{b,p-b}f_b
\quad\text{是等距映射}.
}
\tag{2.1}
$$

由于创建一旦产生重复占据，就不可能在随后创建中回到平方自由层，准确有
$$
(D^*)^r=Q_{b+r}(\mathcal B^*)^r|_{\mathcal H_b}.
$$
所以创建塔
$$
W_p(f_b)=\sum_{b=0}^p
\frac{(D^*)^{p-b}f_b}{\sqrt{(p-b)!S^{p-b}}}
$$
满足
$$
\boxed{W_p=Q_p\mathcal U_p,\qquad W_p^*W_p\preceq I.}
\tag{2.2}
$$
这还没有给下界；下节支付全部混合出生的碰撞损失。

## 3. 两次同位删除只混合相邻出生

在第 $p$ 个玻色层定义碰撞计数算子
$$
\mathcal N_{\rm coll}
=\frac12\sum_i(b_i^*)^2b_i^2.
$$
它在 $e_\alpha$ 上的特征值为
$\frac12\sum_i\alpha_i(\alpha_i-1)$。
平方自由向量对应零值，其余基向量的值至少一，故
$$
\boxed{I-Q_p\preceq\mathcal N_{\rm coll}.}
\tag{3.1}
$$
无限行也合法：该正算子在固定层有界，其范数至多 $p(p-1)/2$，下面正项求和可按单调极限处理。

对 $f\in K_b$，平方自由性给 $b_i^2f=0$，并且
$$
b_if=E_if\in K_{b-1}.
$$
后者用 $D E_i=E_iD$。由 $[b_i,\mathcal B^*]=a_iI$，直接两次交换得到
$$
\boxed{
b_i^2\mathcal U_{b,r}f
=2\sqrt r\,\frac{a_i}{\sqrt S}
  \mathcal U_{b-1,r-1}E_if
 +\sqrt{r(r-1)}\frac{a_i^2}{S}
  \mathcal U_{b,r-2}f.
}
\tag{3.2}
$$
不存在的项按零处理。这是总层 $p-2$ 的两个出生分量；对完整输入 $(f_b)$，某个输出出生只收到相邻两个输入出生的贡献。

不同输出出生由 (2.1) 正交。
在每个输出出生内使用一次 $\|u+v\|^2\le2\|u\|^2+2\|v\|^2$，再将 (3.2) 对 $i$ 求和，得到
$$
\begin{aligned}
\frac12\sum_i\|b_i^2\mathcal U_p(f_b)\|^2
\le\sum_{b=0}^p\bigg[
&\frac{4r}{S}\sum_i a_i^2\|E_if_b\|^2\\
&+\frac{r(r-1)}{S^2}\sum_i a_i^4\|f_b\|^2
\bigg],\qquad r=p-b.
\end{aligned}
\tag{3.3}
$$
原 $b$ 孔层上准确有
$\sum_i\|E_if_b\|^2=b\|f_b\|^2$，且
$\sum_i a_i^4\le(\max_i a_i^2)S$。所以 (3.3) 至多为
$$
\delta\sum_{b=0}^p
\bigl[4r b+r(r-1)\bigr]\|f_b\|^2.
$$
保留 $b=p-r$ 后，系数满足
$$
4r(p-r)+r(r-1)=4pr-3r^2-r\le\frac43p^2.
$$
结合 (3.1)，得到整个混合出生空间上的准确损失界
$$
\boxed{
\|(I-Q_p)\mathcal U_p(f_b)\|^2
\le\frac43\delta p^2\sum_b\|f_b\|^2.
}
\tag{3.4}
$$
这里没有把单列误差直接相加后再付一次出生数；两带结构已经支付所有交叉项。

由正交投影的 Pythagoras 和 (2.1)--(2.2)，
$$
\boxed{
(1-\epsilon_P)I\preceq W_p^*W_p\preceq I
\qquad(p\le P).
}
\tag{3.5}
$$

## 4. 双塔准确识别原 canonical 顺次 MP 塔

还须证明 $W_p$ 满射，不能只由无限维中的下方有界推出。
$W_0=I$。若 $W_{p-1}$ 满射，则 $W_p$ 的新生列是 $K_p$ 上的恒等，旧列的像为
$$
D_p^*W_{p-1}\mathfrak M_p^{-1/2}\mathfrak F_{p-1}
=\operatorname{Ran}D_p^*,
$$
其中 $\mathfrak M_p$ 在出生 $b$ 上乘 $(p-b)S$，为有界正可逆算子。
而 $D_p$ 满射，所以
$$
\mathcal H_p=K_p\oplus^\perp\operatorname{Ran}D_p^*.
$$
归纳得 $W_p$ 满射；结合 (3.5)，$W_p$ 是有界同构。

从创建列的定义，准确有
$$
D_p^*W_{p-1}=W_p\mathfrak a_p^*.
$$
取伴随并乘真正的有界逆，令
$$
\widetilde V_p=(W_p^*)^{-1},
$$
则
$$
D_p\widetilde V_p=\widetilde V_{p-1}\mathfrak a_p.
\tag{4.1}
$$
此外，$W_p$ 的新生列等于恒等、旧列正交于 $K_p$。
所以 $\widetilde V_p$ 也在新生分量上等于恒等，旧列均正交于 $K_p$。
于是 (4.1) 在旧列上的唯一解恰为
$R_p\widetilde V_{p-1}\mathfrak a_p$。
逐层展开就得到原 (1.2)，即
$$
\boxed{V_p=(W_p^*)^{-1}.}
\tag{4.2}
$$
这是真正旧 canonical 右逆塔的识别，不只是另一个近似交织。

由 (3.5)，
$$
V_p^*V_p=(W_p^*W_p)^{-1}
$$
介于 $I$ 与 $(1-\epsilon_P)^{-1}I$，得到 (1.3)--(1.4)。
按孔层正交直和即可得到全部低层的同一界。

## 5. 原实际边界中的平方根非真空余窗

以下严格沿用[R239 低孔 Fock 塔](R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md) §§4–8 的实际对象和已付 lift。
固定两个实际边界之一，$M=\ker T$，原头
$$
L_m=A_m+D_m,\qquad d=2^m,\quad A_m^d=0,\quad\|A_m\|\le6,
$$
并有原真实近似 $\|L_m-T\|\le26\eta_{m-1}$、$\eta_{m-1}\le e^{-80d^4}$。
对合法 $q$，原低输出 $v=v_{m,q}(w)$ 满足
$$
\|v-P_{\le q}^{(m)}w\|\le e^{-74d^4}\|w\|,
\qquad P_{\le q-1}^{(m)}L_mv=0,\qquad D_m^dv=0.
$$
其原源为 $r_q=L_mv=A_mv_q$。

选整数 $0\le s\le q/2$，令
$$
n=q-s,\qquad J=m+2n,\qquad P=s+d-1.
\tag{5.1}
$$
旧前缀投影 $\mathcal P_n$ 固定前 $n$ 个原始配对块，满足
$\|\mathcal P_n\|=C_n\le e^{2/(m+1)}$，并同时杀掉前缀删除及其右作用。
去掉其单位原始前缀后，剩余是原 $D_J$，而
$$
\delta_J\le\frac3{J+1},\qquad
\boxed{\epsilon_P\le\frac{4(s+d-1)^2}{m+2(q-s)+1}.}
\tag{5.2}
$$
因此若右端至多某个固定 $\epsilon_0<1$，同一个旧 canonical 塔现在满足
$$
\|V_{\le P}\|\le K_0:=(1-\epsilon_0)^{-1/2},
\qquad\|V_{\le P}^{-1}\|\le1.
\tag{5.3}
$$

在其准确出生坐标中，完整核延伸仍是
$$
z_{b,t}=\frac{(-A_m)^t u_b}{\sqrt{t!S_J^t}}
\quad(0\le b\le s,\ 0\le t<d).
$$
推回原范数、补回前缀所得 $k$ 满足
$L_mk=0$、$P_{\le q}^{(m)}k=\mathcal P_nv$。
置 $c=\mathcal P_nv-k$，则完整原旗条件是
$$
\boxed{
L_mc=\mathcal P_n r_q,\quad
c\in\operatorname{Ran}\mathcal P_n\cap\mathcal H_{[q+1,q+d-1]}^{(m)},
\quad D_m^dc=0.
}
\tag{5.4}
$$
这些身份只依赖精确交织和 $A_m^d=0$，所以由 §4 的准确识别，正是旧稿同一构造。

## 6. 完整未来源、carry 和原范数费用

为明确新条件数没有省掉旧源预算，令
$y=V_{\le P}^{-1}P_{\le P}^{(J)}\mathcal P_nw$。
真实方程的坐标残量满足
$$
A_my_{b,t}+\sqrt{(t+1)S_J}\,y_{b,t+1}=e_{b,t},
\qquad
\|e\|\le26C_n\eta_{m-1}\|w\|,
$$
因为 (5.3) 给 $\|V^{-1}\|\le1$。
初始坐标误差也至多 $C_ne^{-74d^4}\|w\|$。
逐出生的同一三角递推误差由
$$
\Gamma_d=d6^dS_J^{-d/2}
\le d54^dq^{3d/2},\qquad\log\Gamma_d\le d^4
$$
支付；各出生是外部正交直和，没有额外 $\sqrt s$。
推回原空间只再乘一次固定 $K_0$。
在随 $q$ 增大的合法原头上，$K_0$ 被固定剩余指数余量吸收，故对充分大 $q$，
$$
\boxed{
\|c\|\le K_0C_n\,
\|P_{[q+1,q+d-1]}^{(m)}w\|
 +e^{-71d^4}\|w\|.
}
\tag{6.1}
$$
这是同一实际源、原宽 $d$、原 Hilbert 范数的费用。
没有将某个投影后的源冒认为整个原源，也没有越过已付 lift 窗口。

## 7. 旧已闭范围的平方根子窗：完整塔的另一证明

取旧全整数头选择
$$
m(q)=\max\left\{5,\left\lceil
\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right\},
\qquad d(q)=2^{m(q)}=O((\log q)^{1/3}).
$$
任选固定
$$
0<c_0<1/\sqrt2,\qquad s(q)=\lfloor c_0\sqrt q\rfloor.
$$
此时 $d=o(\sqrt q)$、$J\sim2q$，所以 (5.2) 的右端趋于 $2c_0^2<1$。
选择任意 $2c_0^2<\epsilon_0<1$，(5.3)--(6.1) 对全部充分大的整数 $q$ 成立。
原全孔尾 $\tau_q(w)\to0$，因此
$$
\boxed{
\|c_q\|\le K_0C_{q-s(q)}\tau_q(w)
 +e^{-71d(q)^4}\|w\|\longrightarrow0.
}
\tag{7.1}
$$
如果 $s=o(\sqrt q)$，则整个条件数还趋于一；但消去结论只需有界条件数，因此可保留上述固定正倍数的平方根窗口。

旧完整配对分解的望远镜等式为
$$
\mathcal P_{q-s}=T_\infty+\sum_{i=q-s+1}^{q}T_i.
$$
同一个完整分析界 $A_q=1+O(m(q)^{-1/2})$ 作用于 (5.4)，得到
$$
\boxed{
\mu_\infty^{[\ell]}(r_q)^2+
\sum_{i=q-s(q)+1}^{q}\mu_i^{[\ell]}(r_q)^2
\le A_q^2\|c_q\|^2\longrightarrow0
\qquad(\ell\ge d(q)).
}
\tag{7.2}
$$
这里 $\ell$ 是修复宽度，区别于本稿前部的孔层 $p$。
因此本稿完整塔也独立支付这个平方根子窗的整体消去。这一应用范围已被[R239 联合核短塔 §§7–8](R239-appendix-short-flag-towers-and-near-linear-nonvacuum-prefix-removal.md) 的 $s(q)=q/[128(d+1)]^{d+4}=q^{1-o(1)}$ 窗口覆盖；新增的是本稿 §§1–4 的完整多出生 canonical 塔条件数，不是更大的当前消去范围。
对原宽 $d$ 或已定义双宽 $2d$ 的完整最小修复，仍由同一实际原像给
$$
\left|\|F_\ell^\dagger r_q\|
-\|F_\ell^\dagger(I-\mathcal P_{q-s(q)})r_q\|\right|
\le\|c_q\|\longrightarrow0.
$$

## 8. 尚未覆盖的部分

本稿支付的是旧完整 canonical Fock 塔的全部跨出生 Gram。既有联合核短塔只建 $d$ 个新增层，并已消去更大的 $q^{1-o(1)}$ 末段；该更强范围完整保留。
本稿平方根子窗构造不覆盖其余早期分支，也未得到它们的总最小能量或原实际窄源的三 Gram 比较。
不能由 (7.2) 推出 $T_iw\in W$、$K_q(N)\subset N$ 或无权 $N=M$。
原正常见证和普通 Hilbert ISP 继续开放。
