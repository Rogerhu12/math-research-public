# R271 附录：嵌套出生旗的商能量与两次 Schur 逆的完整降孔缺陷

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：完整证明；根代理与 kernel_resume_1cf 已全文独立核查。本文保持真实完整 $D_3$、实际联合旗及原 Hilbert 范数；不将 $D_3$ 换成保高度块后再套完整 Gram 的结论。

新增预算是：保高度降孔在真实中间 $Q_1^{-1}$ 度量中收缩；同时，跨出生项 $C_{21}$ 与两次 Schur 逆所产生的完整缺陷具有同源正能量界。后面的两桥源运输保留一个真实首段 primitive 项。它不等同于实际相邻残量源的运输，也尚未支付原返回源的全部 $Q$-修复费。

## 1. 同头实际链与三个正能量

固定
$$
m\ge5,\quad d=2^m,\quad4d\le q,\quad q+1\le e^{d^3/4}.
$$
全部相邻层使用同一个头 $m$。令
$$
C=D_{3,m}=\sum_{\ell\ge m}b_\ell^3E_\ell,\qquad
b_\ell=(\ell+1)^{-2},\qquad
s_3=\sum_{\ell\ge m}b_\ell^3\le\frac1{5m^5}.
$$
以下指标 $j$ 取 $q$ 或 $q+1$。

使用[完整链与真 Schur 稿 §3.2、§7](R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md)的实际空间
$$
\mathscr C_{j,t}=\bigoplus_{i=0}^{d-t}e_iE_{d-i,j+t},
\qquad
\mathscr Y_{j,t}=\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,j+t},
$$
$$
S_jc=(A_mc_t+D_mc_{t+1})_{t=1}^{d-1},
\qquad \mathcal G_j=S_jS_j^*.
$$
固定 $m,j$ 时 $\mathcal G_j$ 严格正。按相对出生层 $a=t-h+1$ 分成
$$
\mathscr Y_j=\mathscr Y_{0,j}\oplus\mathscr Y_{1,j}\oplus\mathscr Y_{2,j},
$$
其中三项分别是 $a\le0$、$a=1$、$a\ge2$。完整 Gram 为
$$
\mathcal G_j=
\begin{pmatrix}
B_{0,j}&V_{1,j}^*&0\\
V_{1,j}&B_{1,j}&V_{2,j}^*\\
0&V_{2,j}&B_{2,j}
\end{pmatrix}.
$$
定义准确 Schur 块
$$
Q_{1,j}=B_{1,j}-V_{1,j}B_{0,j}^{-1}V_{1,j}^*,
$$
$$
\mathcal H_{2,j}=B_{2,j}-V_{2,j}Q_{1,j}^{-1}V_{2,j}^*.
$$
另记
$$
T_{0,j}=V_{1,j}B_{0,j}^{-1},\qquad
T_{1,j}=V_{2,j}Q_{1,j}^{-1},\qquad
\Sigma_j=T_{1,j}T_{0,j}.
\tag{1.1}
$$
因此实际首段源 $g=(g_0,0,0)$ 的旧有效源正是
$$
\zeta_j=T_{0,j}g_0,\qquad \sigma_j=\Sigma_jg_0,
$$
其三个旧正能量为
$$
\mathcal E_{0,j}(g_0)=\langle B_{0,j}^{-1}g_0,g_0\rangle,\quad
\mathcal E_{1,j}(g_0)=\langle Q_{1,j}^{-1}\zeta_j,\zeta_j\rangle,\quad
\mathcal E_{2,j}(g_0)=\langle\mathcal H_{2,j}^{-1}\sigma_j,\sigma_j\rangle.
\tag{1.2}
$$

置
$$
\mathcal L_j=
\begin{pmatrix}
I&0&0\\
T_{0,j}&I&0\\
0&T_{1,j}&I
\end{pmatrix},
\qquad
\mathcal D_j=\operatorname{diag}(B_{0,j},Q_{1,j},\mathcal H_{2,j}).
$$
直接乘法给
$$
\boxed{\mathcal G_j=\mathcal L_j\mathcal D_j\mathcal L_j^*.}
\tag{1.3}
$$
它是有界可逆的三角坐标变换，不被称为等距变换。实际逆能量准确变为
$$
\|y\|_{\mathcal G_j^{-1}}^2
=\|\mathcal L_j^{-1}y\|_{\mathcal D_j^{-1}}^2,
\qquad
\mathcal L_j^{-1}=
\begin{pmatrix}
I&0&0\\
-T_{0,j}&I&0\\
\Sigma_j&-T_{1,j}&I
\end{pmatrix}.
\tag{1.4}
$$
这里 $\|x\|_P^2=\langle Px,x\rangle$，所有正算子都取于指定真实空间。

## 2. 完整 $D_3$ 的实际下三角块

逐段降孔给
$$
C_{\mathscr Y,q}:\mathscr Y_{q+1}\longrightarrow\mathscr Y_q.
$$
因为 $CD_m=D_mC$，它把每个 $\ker D_m^h$ 送入相同核阶；因此不能降低相对出生层。准确写为
$$
\boxed{
C_{\mathscr Y,q}=
\begin{pmatrix}
C_{00}&0&0\\
C_{10}&C_{11}&0\\
C_{20}&C_{21}&C_{22}
\end{pmatrix}.
}
\tag{2.1}
$$
全部块均保留原 head 与孔层投影，省略的共同下标都是 $q$。

其中
$$
C_{22}=C_{2,q}
=C_{\mathscr Y,q}|_{\mathscr Y_{2,q+1}}
$$
是旧真高旗收缩所用的完整限制。
中间对角块
$$
C_{11}=P_{\mathscr Y_{1,q}}C_{\mathscr Y,q}|_{\mathscr Y_{1,q+1}}
$$
恰为[低旗换序稿 §1](R271-appendix-low-flag-full-head-commutators-and-weighted-source.md)保高度块 $C_0$ 的逐段限制：第 $t$ 段输入、输出均为真实 $U_t$。但跨项
$$
\boxed{
C_{21}=P_{\mathscr Y_{2,q}}C_{\mathscr Y,q}|_{\mathscr Y_{1,q+1}}
}
\tag{2.2}
$$
也必须保留。它逐头读取第 $t$ 段 $U_{t,q+t+1}$，输出其
$E_{t-1,q+t}$ 部分。第一段输出为零。这里没有声称 $C_{21}=0$，也没有声称只凭其普通范数即可控制 Schur 能量。

旧完整链交织
$$
S_q C_{\mathscr C,q}=C_{\mathscr Y,q}S_{q+1},
\qquad \|C_{\mathscr C,q}\|\le s_3
$$
已经支付
$$
\boxed{
C_{\mathscr Y,q}^*\mathcal G_q^{-1}C_{\mathscr Y,q}
\le s_3^2\mathcal G_{q+1}^{-1}.
}
\tag{2.3}
$$
以下只对这一完整不等式作准确坐标变换和限制。

## 3. 三个 Schur 坐标中的同一个收缩

定义完整缺陷块
$$
\Delta_{10}
=C_{10}+C_{11}T_{0,q+1}-T_{0,q}C_{00},
\tag{3.1}
$$
$$
\Delta_{21}
=C_{21}+C_{22}T_{1,q+1}-T_{1,q}C_{11},
\tag{3.2}
$$
$$
\Delta_{20}
=C_{20}+C_{21}T_{0,q+1}-T_{1,q}\Delta_{10}.
\tag{3.3}
$$
它们分别映射 $\mathscr Y_{0,q+1}\to\mathscr Y_{1,q}$、
$\mathscr Y_{1,q+1}\to\mathscr Y_{2,q}$、
$\mathscr Y_{0,q+1}\to\mathscr Y_{2,q}$。

令
$$
\widehat C_q
=\mathcal L_q^{-1}C_{\mathscr Y,q}\mathcal L_{q+1}.
$$
将 (1.4)、(2.1) 逐块相乘，准确得到
$$
\boxed{
\widehat C_q=
\begin{pmatrix}
C_{00}&0&0\\
\Delta_{10}&C_{11}&0\\
\Delta_{20}&\Delta_{21}&C_{22}
\end{pmatrix}.
}
\tag{3.4}
$$
尤其没有将任何 $B_0^{-1}$ 或 $Q_1^{-1}$ 移过 $C$。

在 (2.3) 中以 $\mathcal L_{q+1}x$ 作输入，并用 (1.4)，得到本稿的统一正预算：
$$
\boxed{
\widehat C_q^*\mathcal D_q^{-1}\widehat C_q
\le s_3^2\mathcal D_{q+1}^{-1}.
}
\tag{3.5}
$$
这是同一个原 Hilbert 能量不等式；没有付环境右逆上界 $\Gamma_q$，也没有把一个普通高块压缩当作真 Schur 补。

## 4. 中间 $Q_1^{-1}$ 度量与完整 $C_{21}$ 缺陷

在 (3.5) 中取 $x=(0,h,0)$，得到
$$
\boxed{
C_{11}^*Q_{1,q}^{-1}C_{11}
+\Delta_{21}^*\mathcal H_{2,q}^{-1}\Delta_{21}
\le s_3^2Q_{1,q+1}^{-1}.
}
\tag{4.1}
$$
所以
$$
C_{11}^*Q_{1,q}^{-1}C_{11}
\le s_3^2Q_{1,q+1}^{-1}.
\tag{4.2}
$$
这正是保高度降孔通过实际中间逆的已付范围。它不表示 $Q_1^{-1}$ 与 $C_{11}$ 交换。

更具体，对每个 $h\in\mathscr Y_{1,q+1}$，
$$
\boxed{
\|T_{1,q}C_{11}h-C_{22}T_{1,q+1}h-C_{21}h\|_{\mathcal H_{2,q}^{-1}}^2
\le s_3^2\|h\|_{Q_{1,q+1}^{-1}}^2
-\|C_{11}h\|_{Q_{1,q}^{-1}}^2.
}
\tag{4.3}
$$
左边含有真实 $Q_1^{-1}$ 的整个运输缺陷。只有这个合成式得到预算；不能把 $C_{21}h$ 单独删掉后保留同一右端。

### 商空间解释

消去 $\mathscr Y_0$ 后的真正块为
$$
\mathcal H_{1,j}
=\begin{pmatrix}Q_{1,j}&V_{2,j}^*\\V_{2,j}&B_{2,j}\end{pmatrix}
$$
作用在 $\mathscr Y_{1,j}\oplus\mathscr Y_{2,j}$。其逆二次型准确为
$$
\|(h,k)\|_{\mathcal H_{1,j}^{-1}}^2
=\|h\|_{Q_{1,j}^{-1}}^2
+\|k-T_{1,j}h\|_{\mathcal H_{2,j}^{-1}}^2.
\tag{4.4}
$$
固定第一坐标的最小能量 lift 是 $(h,T_{1,j}h)$。
完整 $C$ 保持高旗，但会在该 lift 中产生 (2.2) 的 $C_{21}h$。
式 (4.1) 正是这个实际商范数的收缩与正交余量；不是先假定 $C_0$ 在完整逆度量里收缩。

## 5. 第一个逆与两个缺陷的同时预算

在 (3.5) 中取 $x=(h,0,0)$，得到
$$
\boxed{
C_{00}^*B_{0,q}^{-1}C_{00}
+\Delta_{10}^*Q_{1,q}^{-1}\Delta_{10}
+\Delta_{20}^*\mathcal H_{2,q}^{-1}\Delta_{20}
\le s_3^2B_{0,q+1}^{-1}.
}
\tag{5.1}
$$
第一中间逆的商收缩及两级误差因而同时有界。这里 $\Delta_{20}$ 必须按 (3.3) 使用；它不等于一个只含裸 $C_0$ 的二重交换子。

还可利用 (3.5) 中不同输入块之间的相互项，而非将两条独立估计的平方根相加。下面对实际首段源正要使用这一点。

## 6. 真首段源类型上的两桥运输

取 $x=g_0\in\mathscr Y_{0,q+1}$，只支撑第1段。真正最小修复的
$$
S_{q+1}b=(g_0,0,0),\qquad b=P_{\mathscr C_{q+1}}D_{\rm first}^*y
$$
确实属于这个类型：$b$ 只有第一段、高度至少2，故 $g_0=(A_mb_1,0,\ldots,0)$。

因为 $C$ 不改变链段，而 $\mathscr Y_2$ 的第一段为零，
$$
\boxed{C_{20}x=0.}
\tag{6.1}
$$
置
$$
\zeta_{q+1}=T_{0,q+1}x,\qquad
\sigma_{q+1}=\Sigma_{q+1}x.
$$
将输入 $(x,-\zeta_{q+1},0)$ 代入 (3.5)。
其输出的第三块准确为
$$
\begin{aligned}
\Delta_{20}x-\Delta_{21}\zeta_{q+1}
={}&\Sigma_q C_{00}x-C_{22}\Sigma_{q+1}x\\
&-T_{1,q}C_{10}x+C_{20}x.
\end{aligned}
\tag{6.2}
$$
在 (6.1) 下，得到
$$
\boxed{
\begin{aligned}
&\|\Sigma_q C_{00}x
-C_{22}\sigma_{q+1}
-T_{1,q}C_{10}x\|_{\mathcal H_{2,q}^{-1}}^2\\
&\quad+\|C_{00}x\|_{B_{0,q}^{-1}}^2
+\|C_{10}x-T_{0,q}C_{00}x\|_{Q_{1,q}^{-1}}^2\\
&\le s_3^2
\bigl[\mathcal E_{0,q+1}(x)+\mathcal E_{1,q+1}(x)\bigr].
\end{aligned}
}
\tag{6.3}
$$
尤其
$$
\|\Sigma_q C_{00}x
-C_{22}\sigma_{q+1}
-T_{1,q}C_{10}x\|_{\mathcal H_{2,q}^{-1}}
\le s_3\sqrt{\mathcal E_{0,q+1}(x)+\mathcal E_{1,q+1}(x)}.
\tag{6.4}
$$
右端不含 $\mathcal E_{2,q+1}$，也不含一般 $\Gamma$。
这保留两次实际逆及全部中间跨旗项。

### 6.1 剩余首段 primitive 项有一个明确的原像

$e=C_{10}x$ 只在第1段，尾高度为1。若 $S_{q+1}b=(x,0,0)$ 如上，令 $\mathscr X_{1,q}$ 为整个 $\mathscr C_q$ 中相对出生层恰为1的部分，并置
$$
u=P_{\mathscr X_{1,q}}C_{\mathscr C,q}b.
$$
由于 $b$ 只在第1段，$u$ 也只在第1段，而且 $D_mu_1=0$。由完整 $C$ 与 $S$ 的交织以及第一段只有头作用，
$$
\boxed{S_qu=(0,e,0),\qquad D_{\rm first}u=0,\qquad
\|u\|\le s_3\|b\|.}
\tag{6.5}
$$
其中 $(0,e,0)$ 是出生层三块记号，不是链段记号。

实际最小内部右逆及 (1.4) 因而给
$$
\boxed{
\|e\|_{Q_{1,q}^{-1}}^2+
\|T_{1,q}e\|_{\mathcal H_{2,q}^{-1}}^2
\le\|u\|^2\le s_3^2\|b\|^2.
}
\tag{6.6}
$$
这是准确的原像预算，但最后的 $\|b\|$ 尚未被原最小修复范数 $\lambda$ 控制。不能用 (6.6) 宣称已付所需缺陷专属增长界。

## 7. 源类与尚未完成的接口

式 (4.1) 是真实 $Q_1^{-1}$ 商度量上的收缩，(4.3)、(5.1)、(6.3) 则支付完整运输余项。它们不能被改写成 $C_{11}$ 与任一中间逆交换，也不能把 $C_{21}$ 或 $C_{10}$ 扔掉。

特别，即使 $x$ 是第 $q+1$ 层真正 $w\in M\ominus N$ 产生的 $g_0$，本文也没有证明 $C_{00}x$ 是第 $q$ 层来自 $D_3w$ 或原实际尾理想作用的最优首段源。旧完整修复算子确有已付 $W$ 投影交换缺陷，但它不能未经进一步核对就拆成这里的 $B_0^{-1}$、$Q_1^{-1}$。

同样，(6.3) 的右端是同源的前两块能量，不是 $\lambda^2$；(6.6) 保留 $\|b\|$。尚须把这些已付运输关系接到[真实返回源笔记](../notes/2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md)中的
$$
F Kc_L,\qquad Q=I+K,\qquad
\mathcal E_2\le\lambda\,\lambda_q(FKc_L),
$$
或另行证明真正窄源上的能量预算。本文没有由一般全 primitive 比较猜想代替这一接口，也没有据此推出无权 $N=M$。
