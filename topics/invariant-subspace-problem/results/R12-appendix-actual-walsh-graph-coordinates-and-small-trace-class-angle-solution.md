# 原 Walsh 块根的有界图坐标与同一 carry 的小迹类角度解

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

沿用 [原 Walsh 全块表示](R12-appendix-actual-walsh-block-trace-class-carry-and-closed-diagonal-roots.md) 的原 $C=A^{(m_0)}=D+K$、$Q_{-1},Q_m$、$a_m,\mu_m,\delta_m,\beta_m,p_m,r_m$。允许每个循环块平方根任意选分支，见 [全部分支的实际线性根门](R12-appendix-all-walsh-block-root-branches-same-carry-sylvester-divergence.md)。

本篇支付原 carry 在真正闭图坐标中的完整线性来源。结论与旧 $RX+XR=K$ 没有有界解相容：这里的未知量是改变闭根定义域的图角度，不能反向去掉两侧缺陷因子。

## 1. 全域有界 Julia 坐标

令 $R=\bigoplus R_m$ 为上述任意闭稳定块根，$R^2=D$ 于 $\mathcal D(R)$。定义

$$
G=(I+R^*R)^{-1/2},\qquad
H=(I+RR^*)^{-1/2},\qquad
V=RG.
$$

$G,H,V$ 都是全域有界压缩，$G H$ 的次序不交换。矩阵

$$
\mathcal U=\begin{pmatrix}V&H\\G&-V^*\end{pmatrix}
\tag{1.1}
$$

是酉算子，第一列是闭图 $\{(Rx,x):x\in\mathcal D(R)\}$ 的等距坐标。$G$ 的像在 $\mathcal D(R)$，而稳定域给真正全域身份

$$
H D G=V^2.
\tag{1.2}
$$

因此对原块对角 companion $\mathcal B_D=\begin{pmatrix}0&D\\I&0\end{pmatrix}$，

$$
\mathcal U^*\mathcal B_D\mathcal U
=\begin{pmatrix}A&F\\0&B\end{pmatrix},
\tag{1.3}
$$

其中所有式子都是有界算子的实际乘积：

$$
A=V^*DG+GV,\quad
F=GH-V^*DV^*,\quad
B=-HDV^*-VH.
\tag{1.4}
$$

原 carry 的完整扰动则为

$$
\mathcal U^*
\begin{pmatrix}0&K\\0&0\end{pmatrix}
\mathcal U
=
\begin{pmatrix}
V^*KG&-V^*KV^*\\
HKG&-HKV^*
\end{pmatrix}.
\tag{1.5}
$$

四块都迹类；没有只保下左块而丢掉其余原项。

在单个有限块上可合法写

$$
A_n=G_n^{-1}R_nG_n,\qquad
B_m=-H_mR_mH_m^{-1}.
\tag{1.6}
$$

这仅用于有限矩阵推导；本文不把 $G^{-1},H^{-1}$ 当作全域有界算子。

## 2. 同一真实右端的唯一小迹类线性解

存在唯一有界 $Y$ 满足

$$
\boxed{\quad BY-YA=-HKG.\quad}
\tag{2.1}
$$

这个解事实上是迹类，且对所有根分支共同满足

$$
\boxed{\quad
\|Y\|_1\le\sqrt{2a_0}+40e^{-1070}<10^{-4}.
\quad}
\tag{2.2}
$$

下面给全块来源证明，而非仅控制某一个矩阵元。

对 $m\ne n$，令 $X_{mn}$ 为唯一有限矩阵解

$$
R_mX_{mn}+X_{mn}R_n=K_{mn},
\qquad Y_{mn}=H_mX_{mn}G_n,
\tag{2.3}
$$

并置 $Y_{mm}=0$。有限唯一性对任意分支成立：不同非负块的 $r_m$ 严格递减；常数块与第 $0$ 块虽半径相同，但根分别为实数及纯虚数；同块的简单平方谱也不允许根谱含一对相反数。由 (1.6)，每个 $Y_{mn}$ 确满足 (2.1) 的相应块。

### 2.1 所有非负块，保完整源和有限高度

取 $m>n\ge0$，$N=2^n$、$M=2^m$、$d=M/N$，所以 $d$ 为偶数。写

$$
k=2^{-(m-n)/2}\delta_m,\qquad
\gamma_\ell=\prod_{j=1}^{\ell}a_{n+v_2(j)}.
$$

原低头分段满足 $\beta_m=\beta_n^d\gamma_{d-1}$。从
$D_mX-XD_n=R_mK_{mn}-K_{mn}R_n$ 望远镜至 $M$ 次，使用

$$
D_m^M=-p_mI,\qquad D_n^M=p_n^dI.
$$

在每一项左乘 $H_m$、右乘 $G_n$ 后，分别用
$H_mR_m=R_mG_m$ 的有界压缩延拓和 $R_nG_n$ 的压缩性。所有项仍是实际秩一项。因此完整迹范数有界于

$$
\|Y_{mn}\|_1
\le
\frac{2kN}{\mu_n^d+\mu_m\gamma_{d-1}}
\sum_{\ell=0}^{d-1}\mu_n^{d-1-\ell}\gamma_\ell.
\tag{2.4}
$$

这里的 $N$ 不是省略的层数：若望远镜指标为 $bN+c$，$0\le c<N$，左右两个实际前缀范数乘积为
$\beta_m\mu_n^b/\gamma_b$，与 $c$ 无关；恰有 $N$ 项。再以低尾前缀反转
$\gamma_{d-1}/\gamma_b=\gamma_{d-1-b}$ 得 (2.4)。

令 $\vartheta_n=a_na_{n+1}/\mu_n^2$。原相邻权比不超过 $e^{-1070}$，所以

$$
\vartheta_n\le4e^{-1070}<\frac12.
$$

每对相邻前缀因子满足
$\gamma_{2j}\le(a_na_{n+1})^j$、
$\gamma_{2j+1}\le a_n(a_na_{n+1})^j$。于是

$$
\sum_{\ell\ge0}\frac{\gamma_\ell}{\mu_n^\ell}
\le\frac{1+a_n/\mu_n}{1-\vartheta_n}\le6.
$$

从 (2.4) 得到每一个完整块的共同预算

$$
\boxed{\quad
\|Y_{mn}\|_1
\le12\,2^n\,2^{-(m-n)/2}\frac{\delta_m}{\mu_n}
\qquad(m>n\ge0).
\quad}
\tag{2.5}
$$

这没有用主根分支的扇区性质。

原反线性共轭 $Jf(y)=\overline{f(-1-y)}$ 保持所有 $Q_m$，在 $m\ge0$ 块上是带负号的反序共轭。$JD^*J=D$、$JK^*J=K$，且任意平方根分支的有限多项式均给 $JR^*J=R$。故 $JH J=G$。有限唯一性推出

$$
Y_{nm}=J_nY_{mn}^*J_m,
\qquad \|Y_{nm}\|_1=\|Y_{mn}\|_1.
\tag{2.6}
$$

这支付全部反向块。

### 2.2 常数块及第一个临界块

常数根为 $\lambda=\pm\sqrt{\mu_0}$。对 $m\ge1$，用
$(R_m+\lambda)^{-1}=(R_m-\lambda)(D_m-\mu_0)^{-1}$，再把后一有限逆作完整几何和。$H_m(R_m-\lambda)$ 的范数不超过 $1+\sqrt{\mu_0}<\sqrt2$（$\mu_0\le a_0\le e^{-20}$）。$D_m^j u_m$ 的实际长度为原前缀积；按偶奇配对求和，与上段相同的前缀预算给

$$
\|Y_{m,-1}\|_1=\|Y_{-1,m}\|_1
\le6\sqrt2\,2^{-m/2}\frac{\delta_m}{\mu_0}.
\tag{2.7}
$$

第 $0$ 块根是 $\pm i\sqrt{\mu_0}$，必须单独计算；不能把它当作远尾。精确答案为

$$
\|Y_{0,-1}\|_1=\|Y_{-1,0}\|_1
=\frac{\delta_0}{(1+\mu_0)\sqrt{2\mu_0}}.
\tag{2.8}
$$

### 2.3 实际无限和与全域同一性

置 $\epsilon=e^{-1070}$、$t=2^{-1/2}$。原权的对数差满足

$$
-\log(\alpha_{j+1}/\alpha_j)
=1400\,16^j-630\,8^j+300\,2^j
\ge1070\,2^j.
$$

故 $\epsilon_n=a_{n+1}/a_n\le\epsilon^{2^n}$，
$\delta_m/\mu_n\le a_m/a_n$，且

$$
\sum_{m>n}t^{m-n}\frac{a_m}{a_n}
\le\frac{t\epsilon_n}{1-t\epsilon},
\qquad
\sum_{n\ge0}2^n\epsilon_n\le\frac{\epsilon}{1-2\epsilon}.
$$

将 (2.5)–(2.8) 全部相加：

$$
\|Y\|_1
\le
\frac{2\delta_0}{(1+\mu_0)\sqrt{2\mu_0}}
+
\frac{24t\epsilon}{(1-t\epsilon)(1-2\epsilon)}
+
\frac{12\epsilon}{1-t\epsilon}
\le\sqrt{2a_0}+40\epsilon.
\tag{2.9}
$$

因此有限块之和确在迹范数中收敛。$A,B$ 有界，故有限块身份可按此极限传到真正全域等式 (2.1)。若另一个有界解存在，差的每个有限块均解零右端；逐块唯一性迫全部矩阵元为零。这也证明了 (2.1) 的有界唯一性。

## 3. 线性已付与非线性原项

若想把该角度解扩展成原 $\mathcal B_C$ 的不变图，完整 Riccati 方程是

$$
(B-HKV^*)Z
-Z(A+V^*KG)
-Z(F-V^*KV^*)Z
+HKG=0.
\tag{3.1}
$$

本文只支付同一原右端的线性解 $Y$。没有给 (3.1) 各次新来源的同一逆费用，也没有证明相应来源类对乘积封闭。

尤其低两块不能因 (2.2) 绝对小而略去：其 Sylvester 根谱尺度是 $\sqrt{\mu_0}$，逆费用相应含 $\mu_0^{-1/2}$，而 (2.8) 正是约 $\sqrt{\mu_0/2}$。原比例 $\delta_0/\mu_0$ 接近 $1$，仍保留先前的临界反馈。故本文不从小迹范数直接声称非线性收缩，不去掉 $H_m,G_n$ 还原有界根修正，也没有构造原闭稳定根。
