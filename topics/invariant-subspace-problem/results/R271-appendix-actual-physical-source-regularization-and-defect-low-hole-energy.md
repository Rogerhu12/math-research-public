# 同一实际最大图来源的临界物理正则化、原图核心与真实缺陷低孔能量

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下对原 N/Y 最大图来源的正则化、全部 carry 预算、固定正阻尼后的原图核心和实际 Green 缺陷能量界均已证明。没有得到阻尼趋零的图控制，没有证明物理孔平滑保持未知缺陷坐标空间，也没有证明 $Z=0$、$\Gamma<\infty$ 或 $N=M$。**

沿用原 $S=B^*$、$G=G_0^*$ 及
$$
\mathcal C=\overline{\{(Sg,T^*g):g\in\mathcal H\}},
\qquad
\mathcal E=\operatorname{Graph}G\ominus\mathcal C.
$$
本文固定同一个实际对
$$
y\in\mathcal D(G),\qquad f=Gy,\qquad T^*y=Sf,             \tag{0.1}
$$
及其唯一规范形式来源
$$
Sh=y,\qquad T^*h=f.                                     \tag{0.2}
$$
$h$ 不预设属于 $\mathcal H$。$\mathcal N$ 始终数全部物理孔，$P_q$ 始终指来源的首缺位 $q$ 块。记
$$
\kappa_0=2+2\log(3/2),\qquad s_0=\kappa_0/14.
$$

[临界小物理矩稿](../results/R271-appendix-critical-small-physical-exponential-maximal-graph-core.md)的结论以原 $y$ 的一个物理指数矩为条件。这里不加该条件：先从同一原 $(y,f)$ 取得阻尼后来源的加权 $\ell^1$ 费用，再支付共轭 carry；这同时给出原算子的真实图核心路径。最后利用 $\mathcal E$ 的第二条方程，取得无条件的低孔能量界。

## 1. 两种阻尼及准确同源换算

写 $\nu(n)$ 为整数 $n$ 的二进位占据位数，$q(n)$ 为其首零位。因此
$$
\nu(n+1)=\nu(n)-q(n)+1.
$$
令
$$
h_s=e^{-s\mathcal N}h,\qquad
S\widehat h_s=e^{-s\mathcal N}y.                         \tag{1.1}
$$
二者均在形式坐标层逐项定义。它们分别为
$$
(h_s)_n=e^{-s\nu(n)}h_n,\qquad
(\widehat h_s)_n=e^{-s(\nu(n)-q(n)+1)}h_n.
$$
所以在固定首缺位块上准确有
$$
P_qh_s=e^{-s(q-1)}P_q\widehat h_s.                       \tag{1.2}
$$
这里的 $q=0$ 因子为 $e^s$，不能随 $q\ge1$ 一起删去。

取
$$
b_0=\eta_0,\qquad b_q=q^{-2}\eta_{q-1}\quad(q\ge1),
\qquad \eta_j=\alpha_{j+1}/\alpha_j,
$$
并记加权来源空间
$$
\mathcal L_b=
\left\{u:\ \|u\|_{\mathcal L_b}
=\sum_{q\ge0}b_q\|P_qu\|<\infty\right\}.                 \tag{1.3}
$$
每个 $P_qu$ 是整个首缺位块上的 Hilbert 向量。$\mathcal L_b\subset C_2$，但不要求 $u\in\mathcal H$。

## 2. 从原图输入支付所有 $s\in[s_0,1]$ 的来源费用

令 $V_r$ 为低 $r$ 位全零的投影，$\mathsf P_p$ 为全部物理孔数 $p$ 层。原最大图域边界行和临界矩稿的有限压平下界给
$$
\|D_r^*V_ry\|
\le8\eta_{r-1}\|y\|+\alpha_r\|f\|,                      \tag{2.1}
$$
及
$$
\|V_r\mathsf P_{\le P}y\|
\le e^{16/3}(r+L_P)^2e^{\kappa_0P}
       \bigl(8\eta_{r-1}\|y\|+\alpha_r\|f\|\bigr),
\quad
L_P=\left\lceil\frac32(P+2)\right\rceil.                 \tag{2.2}
$$
其依据是各物理输入层经纯创建 $D_r^*$ 后正交；没有将物理截断后的 $y$ 另放进 $\mathcal D(G)$。

对每个 $s\in[s_0,1]$ 置
$$
\theta_s=\frac{s}{\kappa_0+s},\qquad
\ell_j=-\log\eta_j,\qquad
P_r(s)=\left\lfloor\frac{\ell_{r-1}}{\kappa_0+s}\right\rfloor.
$$
低层只用 (2.2) 和阻尼的收缩性；高层直接用
$$
\|V_r\mathsf P_{>P}e^{-s\mathcal N}y\|
\le e^{-s(P+1)}\|y\|.
$$
由 $\alpha_r\le\eta_{r-1}$，准确得到
$$
\|V_re^{-s\mathcal N}y\|
\le \eta_{r-1}^{\theta_s}
\left[
8e^{16/3}(r+L_{P_r(s)})^2(\|y\|+\|f\|)+\|y\|
\right].                                               \tag{2.3}
$$
取整的高层使用 $P_r(s)+1>\ell_{r-1}/(\kappa_0+s)$；没有额外未定指数因子。

原权的归一化为
$$
\ell_j=1400\,16^j-630\,8^j+300\,2^j\le1700\,16^j.
$$
因为 $\kappa_0>2$，有 $P_r(s)<850\,16^{r-1}$，
$r+L_{P_r(s)}\le1280\,16^{r-1}$。置
$$
C_0=8e^{16/3}1280^2+1,\qquad A=\|y\|+\|f\|.
$$
于是
$$
\|V_re^{-s\mathcal N}y\|
\le C_0\,16^{2(r-1)}\eta_{r-1}^{\theta_s}A.              \tag{2.4}
$$

令 $P_q^+=V_q-V_{q+1}$ 为输出的正整数赋值 $q$ 块。由 (1.1)，对 $q\ge1$，
$$
b_q\|P_q\widehat h_s\|
=\frac{1}{q^2\alpha_{q-1}}\|P_q^+e^{-s\mathcal N}y\|.
$$
结合 (1.2)、(2.4)，两种来源均满足
$$
b_q\|P_qh_s\|,\ b_q\|P_q\widehat h_s\|
\le C_0\frac{16^{2(q-1)}}{q^2}e^{-d_{q-1}(s)}A,
\quad q\ge1,                                           \tag{2.5}
$$
其中
$$
A_j=-\log\alpha_j
=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\qquad d_j(s)=\theta_s\ell_j-A_j.
$$
在 $q=0$ 块直接按原坐标阻尼支付：
$$
b_0\|P_0h_s\|,\ b_0\|P_0\widehat h_s\|
\le\frac{b_0}{\alpha_0}\|y\|=e^{-1050}\|y\|.             \tag{2.6}
$$
这同时处理 (1.2) 的 $e^s$ 因子；没有漏掉任何首缺位块。最大图域本身已排除 $y$ 的真空坐标。

定义明确常数
$$
L(s)=e^{-1050}
+C_0\sum_{j\ge0}\frac{16^{2j}}{(j+1)^2}e^{-d_j(s)}.
                                                               \tag{2.7}
$$
则
$$
\boxed{
\|h_s\|_{\mathcal L_b},\ \|\widehat h_s\|_{\mathcal L_b}
\le L(s)(\|y\|+\|f\|),\qquad s\in[s_0,1].}              \tag{2.8}
$$
特别，这是对原最大图域全部来源的线性有界正则化，并非对原 $y$ 额外假设物理矩。

临界等号不能仅靠首指数判断。恰在 $s=s_0$，
$$
\theta_{s_0}=\frac1{15},\qquad
d_j(s_0)=48\,8^j-280\,2^j+\frac{850}{3};
$$
故
$$
d_0(s_0)=154/3,\quad d_1(s_0)=322/3,\quad
d_j(s_0)\ge30\,8^j\quad(j\ge2).
$$
因此 (2.7) 是真正可和的 $\ell^1$ 预算；$L(s)\le L(s_0)<\infty$ 对全部 $s\ge s_0$ 成立于本文区间。它比只写 $C_2$ 平方和更强，后面正是用它支付完整 Y 行和 carry。

## 3. 共轭后的全部真实 carry：统一列界

在有限坐标上先定义
$$
N_i(s)=e^{-s\mathcal N}N_i^*e^{s\mathcal N},
\qquad
K(s)=e^{-s\mathcal N}(T^*-D^*)e^{s\mathcal N}.             \tag{3.1}
$$
本节证明它们需要的有界延拓，不以无界相似代替证明。

原 $N_i^*$ 在输入第 $i$ 位空缺时纯创建一孔；该列在 $N_i(s)$ 中的权为 $e^{-s}$。若从 $i$ 起有连续 $\ell\ge1$ 个占据位，直到 $i+\ell$ 首次空缺，则准确原权为
$$
\frac{\alpha_{i+\ell}}{\alpha_i},
$$
物理孔变化为 $1-\ell$。共轭列权于是为
$$
e^{s(\ell-1)}\frac{\alpha_{i+\ell}}{\alpha_i}\le\eta_i
\qquad(0\le s\le1).                                    \tag{3.2}
$$
这里逐个后续比值使用 $e\eta_j<1$。各输入仍前移同一个整数 $2^i$，所以列像互相正交，得到
$$
\|N_i(s)\|\le1,\qquad
\|N_i(s)-e^{-s}E_i^*\|\le\eta_i.
$$
原平方恒等式在每一有限行成立，故其有界延拓满足
$$
N_i(s)^2=\eta_iN_{i+1}(s),\qquad
\|(I+N_i(s))^{-1}\|
\le\frac2{1-\eta_i}<3.                                 \tag{3.3}
$$
这保留了完整 Cayley 逆。

### 3.1 N 型

记 $K_N(s)=\sum_i a_i(N_i(s)-e^{-s}E_i^*)$。固定来源首缺位 $q$。

当 $i<q$ 时，整块准确列范数为
$$
a_i\frac{\alpha_q}{\alpha_i}e^{s(q-i-1)}.
$$
对 $q\ge1$，除以 $b_q$ 后令 $j=q-1-i$，由
$$
\left(\frac q{i+1}\right)^2\le(j+1)^2,\qquad
e^s\eta_k\le e\eta_0<1/16
$$
得到低行总和小于
$$
b_q\sum_{j\ge0}(j+1)^2\,16^{-j}<2b_q.                   \tag{3.4}
$$
$i=q$ 时无 carry。$i>q$ 时 (3.2) 给
$$
\sum_{i>q}a_i\eta_i\le b_q/12\quad(q\ge1);
$$
对 $q=0$ 同一和至多 $b_0/3$。因此
$$
\boxed{\|K_N(s)P_q\|\le3b_q\qquad(0\le s\le1,\ q\ge0).} \tag{3.5}
$$

### 3.2 Y 型

全部真实 Cayley 项准确给
$$
K_Y(s)=K_N(s)
-\sum_{i\ge0}a_i\eta_i(I+N_i(s))^{-1}N_{i+1}(s).
                                                               \tag{3.6}
$$
先支付右侧 $N_{i+1}(s)P_q$，然后才用逆的范数 $3$，不能先让逆改变来源块再丢掉其成本。

对 $q\ge1$，按 $i\le q-2,\ i=q-1,\ i\ge q$ 分割。第一段由 (3.4) 少一个因子 $e^s$，总和不超过 $2b_q$；中项为 $e^{-s}b_q\le b_q$；最后一段由 $\|N_{i+1}(s)\|\le1$ 及 $\eta_q\le\eta_{q-1}/4$ 给
$$
\sum_{i\ge q}a_i\eta_i\le b_q/3.
$$
连逆后的总费用不超过 $10b_q$。对 $q=0$ 全部属于最后一段，其连逆费用至多 $4b_0$。结合 (3.5) 得
$$
\boxed{\|K_Y(s)P_q\|\le13b_q\qquad(0\le s\le1,\ q\ge0).} \tag{3.7}
$$
本节只是 $\mathcal L_b\to\mathcal H$ 的列求和；没有宣称整个 Y carry 在未经额外行权的 $C_2$ 上有界。

由 (3.5)、(3.7)，全部形式行与有界和一致，且
$$
\|K_N(s)u\|\le3\|u\|_{\mathcal L_b},\qquad
\|K_Y(s)u\|\le13\|u\|_{\mathcal L_b}.                    \tag{3.8}
$$

## 4. 原算子的真实正阻尼图核心路径

从原同源形式身份 $T^*h=f$ 逐行作物理共轭：
$$
e^{-s\mathcal N}f
=e^{-s}D^*h_s+K(s)h_s.                                 \tag{4.1}
$$
每个原输出行有限，故这一步在形式层合法。由 (2.8)、(3.8)，右侧 carry 是实际 Hilbert 向量；左侧也属于 $\mathcal H$。因此
$$
D^*h_s=e^s\bigl(e^{-s\mathcal N}f-K(s)h_s\bigr)
\in\mathcal H.
$$
再使用 $K(0)h_s\in\mathcal H$，得到原、未改动算子的准确输出
$$
\boxed{
T^*h_s=e^s e^{-s\mathcal N}f+
       [K(0)-e^sK(s)]h_s\in\mathcal H.}                \tag{4.2}
$$
并且 $Sh_s\in\mathcal H$，范数不超过 $\|y\|$。注意这里阻尼的是规范 $h$ 的全部物理孔；$Sh_s$ 通常不等于 $e^{-s\mathcal N}y$。

由于 $h_s\in\mathcal L_b\subset C_2$，已发布的 N/Y 共同平方来源核心现在可以实际应用：
$$
\boxed{
(Sh_s,T^*h_s)\in\mathcal C\qquad(s_0\le s\le1).}          \tag{4.3}
$$
这里也有直接的共同核心证明。所有单独物理层仍是 Hilbert 向量，因为 $p$ 层只含 $q\le p$ 的有限首缺位块。置 $u_P=\mathsf P_{\le P}h_s\in\mathcal H$；则 $Su_P\to Sh_s$ 按坐标正交平方和收敛，$D^*u_P=\mathsf P_{\le P+1}D^*h_s\to D^*h_s$。同时 $u_P\to h_s$ 在 $\mathcal L_b$ 中由逐块强收敛及原可和支配得到，故 (3.8) 给 $K(0)u_P\to K(0)h_s$。于是 $(Su_P,T^*u_P)\to(Sh_s,T^*h_s)$；再在各 $u_P\in\mathcal H$ 中作有限坐标逼近即可。没有添加域假设，也没有替换原 Y 的主项或逆尾。

若 $c_N=3,c_Y=13$，还得到统一的实际输出预算
$$
\|T^*h_s\|
\le e^s\|f\|+(1+e^s)c_T L(s)(\|y\|+\|f\|).             \tag{4.4}
$$
(4.3) 包含临界 $s=s_0$。它没有涵盖 $s\downarrow0$，也没有证明仅对 $y$ 作物理阻尼后的 $\widehat h_s$ 具有 Hilbert 主项。

## 5. 真实 Green 缺陷的正能量式

现在额外取 $(y,f)\in\mathcal E$。它满足两条真实方程
$$
T^*y=Sf,\qquad By+Tf=0.
$$
由 (4.3)，$\mathcal E\perp\mathcal C$ 给
$$
0=\langle y,Sh_s\rangle+\langle f,T^*h_s\rangle.
$$
由于 $S$ 把不同来源物理层送到互相正交的坐标集合，
$$
A_s:=\langle y,Sh_s\rangle
=\sum_{p\ge0}e^{-sp}\|S\mathsf P_ph\|^2\ge0.
$$
另外
$$
F_s:=\langle f,e^{-s\mathcal N}f\rangle
=\|e^{-s\mathcal N/2}f\|^2\ge0.
$$
结合 (4.2) 得准确同源身份及预算
$$
\boxed{
A_s+e^sF_s
=-\operatorname{Re}\langle f,[K(0)-e^sK(s)]h_s\rangle
\le(1+e^s)c_TL(s)\|f\|(\|y\|+\|f\|).
}                                                       \tag{5.1}
$$
这个不等式使用真实第二方程所给的原图正交性，不是一般最大图来源的条件增长界。

### 5.1 用最低位准确支付坐标比较常数

为让 (5.1) 对同一 $f$ 产生实质费用，采用已发布的首位分解，记 $\alpha=\alpha_0=e^{-20}$：
$$
B=\alpha\begin{pmatrix}0&I\\R&0\end{pmatrix},\qquad
S=\alpha\begin{pmatrix}0&R^*\\I&0\end{pmatrix},
\quad
\|R\|\le\eta_0,\quad\|H\|<13/20,\quad\|T\|\le6.
$$
写 $y=(y^{(0)},y^{(1)})$、$f=(f^{(0)},f^{(1)})$。

N 型两条精确关系为
$$
y^{(0)}+H^*y^{(1)}=\alpha f^{(0)},\qquad
f^{(1)}+Hf^{(0)}=-\alpha y^{(1)}.
$$
Y 型则为
$$
y^{(0)}+H^*y^{(1)}=\alpha(I-R^*)f^{(0)},\qquad
f^{(1)}+Hf^{(0)}=-\alpha(I-R)y^{(1)}.
$$
Y 第一式由原 $T_Y^*$ 第二块行乘 $I-R^*$ 得到，使用 $H^*R^*=R^*H^*$；第二式由 $By+T_Yf=0$ 乘原 $I-R$ 得到。

同时
$$
\alpha\|y^{(1)}\|\le\|By\|\le6\|f\|,\qquad
\alpha\|f^{(0)}\|\le\|Sf\|\le6\|y\|.
$$
故两型统一有
$$
\boxed{
\|y\|\le\frac{10}{\alpha_0}\|f\|,\qquad
\|f\|\le\frac{10}{\alpha_0}\|y\|.}                        \tag{5.2}
$$
例如第一项的系数不超过
$6(1+13/20)/\alpha+\alpha(1+\eta_0)<10/\alpha$；
另一项完全对称。这里不需要把 $H^2$ 的小范数误当成 $H$ 自身同阶小范数。

### 5.2 一个明确的无条件低物理孔结论

在 $s=1$，$\kappa_0<3$ 给 $\theta_1>1/4$，因而
$$
d_j(1)>
\frac{770}{3}16^j-\frac{135}{2}8^j-225\,2^j+\frac{850}{3}.
$$
右边在 $j=0,1$ 分别为 $247.5$、$3400$，在 $j\ge2$ 至少为 $200\,16^j$。于是
$$
\sum_{j\ge0}\frac{16^{2j}}{(j+1)^2}e^{-d_j(1)}
<2e^{-247.5}.
$$
粗界 $C_0<e^{22}$ 已足够，连同 $q=0$ 项，得到
$$
L(1)<e^{-1050}+2e^{-225.5}<e^{-224}.                      \tag{5.3}
$$
由 (5.1)、(5.2)，对原两型都可用 $c_T\le13$，从而
$$
F_1
\le(1+e^{-1})13L(1)(1+10e^{20})\|f\|^2
<286e^{-204}\|f\|^2
<e^{-198}\|f\|^2.
$$
因此，实际 Green 缺陷输出无条件满足
$$
\boxed{
\|e^{-\mathcal N/2}f\|^2\le e^{-198}\|f\|^2,\qquad
\|\mathsf P_{\le190}f\|^2\le e^{-8}\|f\|^2.
}                                                       \tag{5.4}
$$
第二式只用 $e^{-\mathcal N}\ge e^{-190}$ 在相应物理层上成立。这是同一实际缺陷的来源约束，没有将一般近核源当成 $W$ 向量。

## 6. 实际范围与继续欠费

(2.8) 对全部原最大图来源自动成立；(4.3) 给固定正物理阻尼后的真实核心，并支付了原主项的 Hilbert 输出；(5.1)--(5.4) 进一步使用实际缺陷两方程。

这些结论不提供 $s\downarrow0$ 的图范数上界。即使 $Sh_s\to y$ 在 $\mathcal H$ 中成立，也不能据此断言 $T^*h_s\to f$ 或沿子列有界。(5.4) 仅把固定低孔部分压小，不是任意高孔指数矩，也不能从中推断 $\mathcal E=0$。

在原闭坐标 $R:F\to Y$、$X=\{v+Zv:v\in F\}$ 中，(5.4) 适用于同一 $f=v+Zv$。它没有将 $P_F\operatorname{Ran}T^*=F$ 提升成 $F\subset\operatorname{Ran}T^*$，也没有消去同 $u$ 的实际 $\Gamma$ 费用。原 $Z=0$、$\overline{Z(F)}=W$ 和最终 $N=M$ 仍分别保持为尚未支付的端点。

