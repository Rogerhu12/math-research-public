# 原 connected 字的逐元素返回与共同 Tate 坐标

日期：2026-11-27。本文是
[原 Y/K 有理等距笔记](2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md)
§12(35a)–(38) 的有限 Fourier 补充。只推广已经给出的逐元素原 theta 图；
不把一个新的 Mellin 导数赋零，不把无限对数展开送进有限点载体。

## 1. 沿原 connected 直线没有遗失二次相位

仍用原加性角色、同一个标准 Schrödinger 模型及
$$
T_{h,k}F(x)=\psi_p(k(x+h/2))F(x+h).
$$
该笔记(35a)逐项给
$$
\mathcal U_L M_s\mathcal U_L^{-1}
 =T_{s/c_L,-s},\qquad
M_sf(y)=\psi_p(sy)f(y).                                      \tag{1}
$$
两参数 $(s/c_L,-s)$、$(t/c_L,-t)$ 的辛配对为零。因此其**完整
Weyl lift**满足严格群律
$$
T_{s/c_L,-s}T_{t/c_L,-t}=T_{(s+t)/c_L,-s-t}.                  \tag{2}
$$
(1)中的 $-s^2/(2c_L)$ 正是标准 Weyl 半相位，不能再删一次，
也没有另一个剩余二次函数可自由选择。

按原 R300(8)–(12) 的 division/Miller 图，这条直线是同一个
connected Tate 群。固定相容的 $p^a$ 次根单位及原正式同构
$\beta:\widehat{\mathbf G}_m\to\widehat E$。两个相容的 connected
参数基只能相差一个 $u_L\in\mathbf Z_p^\times$。
同一基点上的两个群 lift 之比，若尚未由刚性化消去，
则只能是这条群上的连续线性 character，形如
$\psi_p(c_0s)$，$c_0\in\mathbf Z_p$。它不能是非线性相位。

这个最后的 character 也由已经付完的**全部**深限制排除。
若保留它，则对模 $p^a$ 的完整调制平均，实际 Amice 返回为
$$
 {\bf1}_{\,u_LY+c_0\in p^a\mathbf Z_p}\,\nu.                 \tag{3}
$$
另一方面，原笔记(36)–(37)给同一个来源的
$\mathbf1_{Y\in p^a\mathbf Z_p}\nu
=\beta_0^a[\kappa^a]_*\nu$；这里用 $\beta_0$ 表示该轴非零
whole-core 标量，避免与正式同构重名。
完整六 sigma 来源非零，故右边对每个 $a$ 都非零。
若 $c_0\ne0$，取 $a>v_p(c_0)$，(3)与原深限制的支撑不交，
不能成为同一个非零测度。因此
$$
c_0=0.                                                       \tag{4}
$$
这个论证使用原完整球返回和真实非零 core；仅由抽象 isotropic
群律本身不能排除 $c_0$。也不需要假设任何原中央值非零。

## 2. 任意有限字符及完整有限 Fourier 返回

令 $\varphi$ 在 $\mathbf Z_p$ 上模 $p^a$ 局部常值，并作准确有限展开
$$
\varphi(y)=\sum_{h\bmod p^a}\widehat\varphi(h)
                  \psi_p(hy/p^a).
$$
在原自然向量 $\varphi B_0$ 上应用(1)–(4)，逐元素的 Amice 公式为
$$
\mathcal A_{\varphi B_0}(T)
 =\sum_{h\bmod p^a}\widehat\varphi(h)\,
       \mathcal A_{B_0}
          \bigl(\zeta_{p^a}^{\,u_Lh}(1+T)-1\bigr).
$$
因而在同一个物理坐标上
$$
\boxed{\nu_{\varphi B_0}=\varphi(u_LY)\,\nu_{B_0}.}           \tag{5}
$$
其余所有轴、有限坏处、原 Gaussian 和 Miller 因子都共同保留。
这是有限个实际 theta 向量的恒等式；有限 Fourier 中的 $p^{-a}$
是原准确系数，未称其为单位。

特别，单位 multiplicative 字 $\vartheta$ 只多固定代数标量
$\vartheta(u_L)$，其准确导子不变；附在 $p^r$ 环带上的字符也
只按(5)缩放该环带，不产生平移。故原笔记(18)返回 Y-unit 时，
$r\ge1$ 的支确实消失，$r=0$ 支仍含原非平凡 Y 字。
另一 K 轴的负深度和相反字符必须全部保留，不能先忘掉它们。
将这些有限字另接 R745 的有限正矩或 R774/R749 的有限点载体时，
只准应用于已经写明的完整有限等式；(5)本身不把 $J'(0)$ 的
无限对数尾认作点对数的有限和。

## 3. 原六输入共同规范使两轴的单位相同

若分别为两个抽象 theta 空间任选 connected Tate 基，
则只能得到两个单位 $u_Y,u_K$；此时原相反角色必须保留
$\vartheta(\epsilon u_Y/(2u_K))$。原问题没有作这种独立选择。

确切地，原六个 sigma 输入都使用同一个 $E$、同一个 $\psi_p$、
同一个正式同构 $\beta$ 和同一个 connected Tate 生成元。
对任一当前 $p$-整输出行 $L$，自然输出 $y=Lx$ 的调制是原六轴的
$$
 M_s^{\,L}=\prod_{j=1}^6M_{sL_j}^{(j)}.                      \tag{6}
$$
这里的 $L_j$ 取原固定 split 嵌入，与物理线性坐标
$Y_L=\sum_jL_j\xi_j$ 相同。逐输入的原图将(6)返回为
$\psi_p(u_\sigma sY_L)$，所以
$$
u_L=u_\sigma.                                                \tag{7}
$$
这也可在原标准极化中直接核：
若 $N_L=\langle L,L\rangle$，
$c_L=c_\sigma/N_L$，(1)的移位含 $N_L$；
从输出坐标还原到原输入的对偶行含 $N_L^{-1}$，二者准确相消。
因此逆 Gram 不产生一个另选的轴单位。全局有理 Weil lift
的共同标量在共轭(6)中消失，已付的固定坏处没有被修改。
原笔记当前两轴以及除以5后的同一个物理坐标都在此范围，
因为 $p\nmid5\cdot756$。于是
$$
\boxed{u_Y=u_K=u_\sigma.}                                   \tag{8}
$$
共同单位是否记为1只取决于最初生成元记号；下面只用其比为1。

因此将原自然条件
$k-\epsilon\kappa^{-n}y/2\in\mathbf Z_p$
按全部有限字符还原时，共同单位可从整格条件中约去，得到
**同一个**物理条件
$$
K-\epsilon\kappa^{-n}Y/2\in\mathbf Z_p.                       \tag{9}
$$
这不是仅凭球/环带的支撑猜出的相位身份。
相应原负号矩阵严格满足
$$
\operatorname{diag}(1,\kappa^{-n})\,
 \frac15\begin{pmatrix}2&-21\\1&2\end{pmatrix}\,
 \operatorname{diag}(1,\kappa^n)
 =\frac15\begin{pmatrix}2&-21\kappa^n\\\kappa^{-n}&2\end{pmatrix}
 =g_n^- .                                                   \tag{10}
$$
所有显示的非整 $\kappa$ 缩放仍须按原(37)–(39)连同支撑和
$\beta_0$ 标量返回；(10)不把这些缩放称为整自同构。

## 4. 全部原 $p$ 字的同一物理门及完整还原

现在固定原有理等距笔记(26)、(30)的同一 $n\ge1$，仍令
$\kappa=p\lambda^2$、$\beta_0=\bar\pi_0^{-1}$，
$d_n=(p-1)p^{n-1}$。$\mu_{-\epsilon}$ 是该笔记(32)–(33)的
整个固定坏处返回，$\Phi_n^\epsilon$ 保原六轴和全部有限向量。
记 $D_{K,t}$ 为只将物理 K 乘 $t$ 的推前矩阵。
对 $G_n=\mathbf Z_p^\times/(1+p^n\mathbf Z_p)$ 的**所有**字符，
包括平凡字符，准确有
$$
\boxed{
 \nu_{E_\vartheta\Phi_n^\epsilon}\big|_{Y\ {\rm unit}}
 =\frac{\beta_0^{-n}}{d_n}\,
   \vartheta(\epsilon/2)\,
   (D_{K,\kappa^{-n}})_*
   \left[
     {\bf1}_{Y,K\in\mathbf Z_p^\times}
     \vartheta(Y/K)\,\mu_{-\epsilon}
   \right].
}
\tag{11}
$$
原 $p^{1-n}$、负深度、相反 K 字、全部 Haar 和 Weyl 相位均在式内。

对非平凡 $\vartheta$，原(18)中只有 $r=0$ 支通过 Y-unit。
若 $(D_a f)(k)=f(ak)$，则逐点有
$$
 A_{-n}(k)\vartheta(p^nk)^{-1}
 =\vartheta(\lambda^{2n})
       D_{\kappa^n}(A_0\vartheta^{-1})(k),\qquad
 q_n^\circ=\epsilon\lambda^{-2n}/2 .
\tag{12}
$$
所以原 $\vartheta(q_n^\circ)$ 与(12)的系数相乘，
恰给 $\vartheta(\epsilon/2)$。第3节的共同单位使
$\vartheta(u_Y/u_K)=1$，没有遗失的独立轴因子。

这里将负深度球推广到带字球，不需要称新字为原 Hecke 本征向量。
实际恒等式 $D_aM_s=M_{as}D_a$ 与(5)逐元素相容。
由已经付出的
$\nu_{D_{\kappa^n}B_0}=\beta_0^{-n}(D_{K,\kappa^{-n}})_*\nu_{B_0}$，
同一个有限 Fourier 展开准确给
$$
 \nu_{D_{\kappa^n}(\varphi B_0)}
 =\beta_0^{-n}(D_{K,\kappa^{-n}})_*
                   \nu_{\varphi B_0}.
\tag{13}
$$
因此(12)保留原 whole-core 标量，而非重选一个逐字符标量。
对于平凡字符，直接由原(39)及
$\mu|_{K\ {\rm unit}}=\mu-\beta_0(D_{K,\kappa})_*\mu$
得到(11)，原两个 K 球都在场。

对 $G_n$ 的全部字符求和，正交关系把(11)变成单个完整门：
$$
\boxed{
 \nu_{\Phi_n^\epsilon}\big|_{Y\ {\rm unit}}
 =\beta_0^{-n}(D_{K,\kappa^{-n}})_*
 \left[
 {\bf1}_{Y,K\in\mathbf Z_p^\times}
 {\bf1}_{\,K-\epsilon Y/2\in p^n\mathbf Z_p}
 \,\mu_{-\epsilon}
 \right].
}
\tag{14}
$$
这同时支付该笔记(59)中所有 $p$-new 分量的几何读法，
不是只给一条最高导子存在性。五处所有 old/new 仍原样留在
$\mu_{-\epsilon}$ 内。

写 $\nu$ 为原六输出来源，则已付的固定反变关系是
$\mu_{-\epsilon}=(g_0^{-\epsilon})_*\nu$。在原坐标中，
$$
 Y'=(2Y-21\epsilon K)/5,\quad
 K'=(\epsilon Y+2K)/5,\quad
 K'-\epsilon Y'/2=5K/2.
\tag{15}
$$
故(14)的门准确是原 $K\in p^n\mathbf Z_p$；
在此门内，$Y'$ 为单位当且仅当原 Y 为单位，而 $K'$ 自动为单位。
原 K 的完整深限制是
$\nu|_{K\in p^n\mathbf Z_p}
 =\beta_0^n(D_{K,\kappa^n})_*\nu$，
与 Y-unit 交换。两个 $\beta_0$ 因子精确相消，得到
$$
\boxed{
 \nu_{\Phi_n^\epsilon}\big|_{Y\ {\rm unit}}
 =(g_n^{-\epsilon})_*\bigl(\nu|_{Y\ {\rm unit}}\bigr).
}
\tag{16}
$$
这里第一侧的 Y 是原反变输出；第二侧的单位条件取原输入 Y。
由 $v_p(\kappa^n)>0$ 及 $p\nmid10$，
$g_n^{-\epsilon}$ 的第一坐标在原整支撑上确实保这项单位条件。
原 $\mathscr P_3=\Pi_{H,0}\Pi_{J,0}\Pi_{N,0}$ 只动另三轴，
故(11)–(16)可以在其前后共同施加；它不是一个三次多项式。

例如对同一个 K/Y 读者，(16)给
$$
 \int_{Y\ {\rm unit}}\frac K Y\,d\nu_{\Phi_n^\epsilon}
 =
 \int_{Y\ {\rm unit}}
 \frac{\epsilon\kappa^{-n}Y+2K}
      {2Y-21\epsilon\kappa^nK}\,d\nu.
\tag{17}
$$
分母在所写域是单位，没有把这个有理函数截成首项。
(11)的每一个有限字可以再接其自己的完整算术点公式；
(17)本身没有给原中央 $J'(0)$ 新零，也没有把此分式的
无限展开交换过 point-only 投影。

以上全为同一来源上的手证，无新数学执行。
