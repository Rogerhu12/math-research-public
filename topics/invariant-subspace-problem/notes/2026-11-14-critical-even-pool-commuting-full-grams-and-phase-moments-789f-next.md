# 临界偶数池的完整层可交换 Gram 与真实相位矩表示

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：第 1—5 节的完整层交换、极分解和同一物理源压缩恒等式已证明。** 这些式子没有证明有限单弱位铅笔恒正，也没有证明其候选相位界。第 6 节明确保留该缺口。

## 1. 固定物理层；不用先压缩的假交换

旧池有 $2s$ 位，$s\ge1$，全部权 $b_i>0$。物理第 $k$ 层记为 $\mathcal H_k$，不同子集坐标正交归一。令

$$
d=\sum_i b_iE_i,\qquad
A_{\rm dual}=\sum_i b_i^{-1}E_i,\qquad
e=A_{\rm dual}^*,\qquad H=2s-2N.
$$

在全分级空间上有

$$
[d,A_{\rm dual}]=[d^*,e]=0,
\qquad [d,e]=[A_{\rm dual},d^*]=H.
\tag{1.1}
$$

以下相邻层算子全部保留其完整物理域：

$$
\mathcal Y=\mathcal H_{s-1},\quad
\mathcal M=\mathcal H_s,\quad
\mathcal Y_+=\mathcal H_{s+1},
$$
$$
R=d|_{\mathcal M}:\mathcal M\longrightarrow\mathcal Y,
\quad R_+=d|_{\mathcal Y_+}:\mathcal Y_+\longrightarrow\mathcal M,
$$
$$
e_-=e|_{\mathcal Y}:\mathcal Y\longrightarrow\mathcal M,
\quad e_0=e|_{\mathcal M}:\mathcal M\longrightarrow\mathcal Y_+.
$$

定义完整正定 Gram

$$
\boxed{\mathsf F=RR^*,\qquad \mathsf Q=e_-^*e_-\quad\hbox{on }\mathcal Y.}
\tag{1.2}
$$

$R$ 满射，$e_-$ 单射，故两者正定。可直接将这些秩声明经正对角相似变换化到无权 Boolean $\mathfrak{sl}_2$；下面第 3 节也给出所用相似变换。这里 $\mathsf Q$ 不表示有限弱位稿中的桥 $Q=F^*Z_2$。

## 2. 完整层上严格交换

**命题 2.1。** 有

$$
\boxed{\mathsf F\mathsf Q=\mathsf Q\mathsf F.}
\tag{2.1}
$$

证明在全分级记号中展开：

$$
\begin{aligned}
d d^*A_{\rm dual}e
&=d(A_{\rm dual}d^*-H)e\\
&=A_{\rm dual}d e d^*-dHe\\
&=A_{\rm dual}e d d^*+A_{\rm dual}Hd^*-dHe.
\end{aligned}
$$

输入在 $\mathcal Y$ 时，$d^*$ 和 $e$ 都先进入 $\mathcal M=\mathcal H_s$，而 $H|_{\mathcal M}=0$。最后两项因而严格为零，得到 (2.1)。这没有要求任意权之间相同。$\square$

这个交换发生在取逆和 primitive 压缩以前。一般不能推出下面的 $G$ 与 $L$ 交换。

## 3. 完整中间层的真实连接算子

临界层有

$$
\ker R=\ker e_0=:U=K_s(d).
\tag{3.1}
$$

一种直接核法是令 $D_k e_I=b_I e_I$，$b_I=\prod_{i\in I}b_i$，以 $d^{(0)},e^{(0)}$ 表示单位权的删除、创建。则

$$
d|_{\mathcal H_k}=D_{k-1}^{-1}d^{(0)}D_k,
\qquad
e|_{\mathcal H_k}=D_{k+1}^{-1}e^{(0)}D_k.
\tag{3.2}
$$

在无权中间层，$e^{(0)}=(d^{(0)})^*$ 且
$[d^{(0)},(d^{(0)})^*]=H=0$，所以两个核相同；(3.2) 给出 (3.1)。

令 $R^\dagger=R^*\mathsf F^{-1}$ 为完整层 Moore–Penrose 右逆。由共同核 (3.1)，存在唯一可逆映射

$$
\boxed{\mathsf S=e_0R^\dagger:\mathcal Y\longrightarrow\mathcal Y_+,
\qquad \mathsf S R=e_0.}
\tag{3.3}
$$

中间层的 $[d,e]=0$ 及全层的 $[d^*,e]=0$ 分别给出

$$
R_+\mathsf S=e_-,
\qquad
R_+^*R_+\mathsf S=\mathsf S\mathsf F.
\tag{3.4}
$$

第一式由 $R_+e_0=e_-R$ 右乘 $R^\dagger$ 得到；第二式由
$e_0R^*=R_+^*e_-$ 得到。于是

$$
\mathsf Q=e_-^*e_-
 =\mathsf S^*R_+^*R_+\mathsf S
 =\mathsf S^*\mathsf S\mathsf F.
$$

因此

$$
\boxed{\mathsf S^*\mathsf S=\mathsf F^{-1}\mathsf Q,
\qquad[\mathsf S^*\mathsf S,\mathsf F]=0.}
\tag{3.5}
$$

这里 $\mathsf S$ 一般不是等距，不能省略其正因子。

## 4. 补集给出一个实际自伴共同相位

令 $\mathsf C_+:\mathcal Y_+\to\mathcal Y$ 为物理补集酉映射，并置

$$
\mathsf T=\mathsf C_+\mathsf S:\mathcal Y\longrightarrow\mathcal Y.
\tag{4.1}
$$

**命题 4.1。** $\mathsf T$ 自伴可逆，且

$$
\boxed{[\mathsf T,\mathsf F]=0,
\qquad \mathsf T^2=\mathsf F^{-1}\mathsf Q.}
\tag{4.2}
$$

完整证明如下。先在无权池定义 $R^{(0)}=d^{(0)}|_{\mathcal M}$、
$\mathsf F^{(0)}=R^{(0)}(R^{(0)})^*$，并令 $\mathsf C_0$ 为中间层补集。
中间层的 $H=0$ 给出

$$
[\mathsf C_0,(R^{(0)})^*R^{(0)}]=0.
$$

故

$$
\mathsf T^{(0)}=
R^{(0)}\mathsf C_0(R^{(0)})^*(\mathsf F^{(0)})^{-1}
$$

是自伴酉算子：分子与 $\mathsf F^{(0)}$ 交换，分子的平方是
$(\mathsf F^{(0)})^2$。又 $\mathsf C_+e^{(0)}|_{\mathcal M}=R^{(0)}\mathsf C_0$，所以
$\mathsf T^{(0)}=\mathsf C_+\mathsf S^{(0)}$。

设 $p=\prod_{i=1}^{2s}b_i$。由 (3.2) 和 $\mathsf S R=e_0$ 的唯一性，

$$
\mathsf S=D_{s+1}^{-1}\mathsf S^{(0)}D_{s-1}.
$$

补集满足 $\mathsf C_+D_{s+1}^{-1}=p^{-1}D_{s-1}\mathsf C_+$，于是

$$
\boxed{\mathsf T=p^{-1}D_{s-1}\mathsf T^{(0)}D_{s-1}.}
\tag{4.3}
$$

这是自伴可逆的正对角合同，并没有把合同误称为酉相似。
另一方面，补集将 $R_+^*R_+$ 共轭为 $RR^*=\mathsf F$。因此 (3.4) 给
$\mathsf F\mathsf T=\mathsf T\mathsf F$；最后 (3.5) 给出
$\mathsf T^2=\mathsf S^*\mathsf S=\mathsf F^{-1}\mathsf Q$。$\square$

特别，$\operatorname{sign}\mathsf T$ 是一个实际自伴酉算子，与
$\mathsf F$、$\mathsf Q$、$|\mathsf T|$ 同时交换。这还没有把有限弱位相位 $H_0$ 识别为该酉算子的压缩。

## 5. 真 MP 源的同一共同谱压缩

取实际物理源

$$
V=K_{s-1}(d)\subset\mathcal Y,\qquad
A_0=A_{\rm dual}|_U:U\longrightarrow V,
\qquad R_0=A_0A_0^*.
$$

令 $P=P_V$，并令

$$
G=\Gamma_{1,s-1},\qquad L=\Gamma_{2,s-1}.
$$

第一真实 MP 列是
$\mathcal J_1=R^*\mathsf F^{-1}|_V$。由完整层定义立即得

$$
G=P\mathsf F^{-1}|_V.
\tag{5.1}
$$

第二真实 MP 列满足

$$
\mathcal J_2=e_0\mathcal J_1=\mathsf S|_V.
\tag{5.2}
$$

为核这一点，$d^2/2:\mathcal H_{s+1}\to\mathcal H_{s-1}$ 在此临界高度是完整层可逆映射；由 (3.4) 及 $dV=0$，

$$
\frac12RR_+e_0\mathcal J_1
 =\frac12R e_-R\mathcal J_1
 =\frac12R e_-|_V=I_V.
$$

故 (5.2) 是唯一合法预像，确为真实 MP 列。结合 (3.5)、(4.2)，得到

$$
\boxed{L=P\mathsf F^{-1}\mathsf Q|_V=P\mathsf T^2|_V.}
\tag{5.3}
$$

此外，$R e_-|_V=2I_V$ 给出正交分解

$$
e_-|_V=2\mathcal J_1+A_0^*.
\tag{5.4}
$$

其中 $A_0^*=P_Ue_-|_V$，而 $\operatorname{Ran}\mathcal J_1\perp U$。所以

$$
\boxed{P\mathsf Q|_V=4G+R_0.}
\tag{5.5}
$$

有限弱位稿中的同一个 $H_0=G^{-1}L-2G-R_0$ 因而有严格完整层表示

$$
\boxed{H_0
 =G^{-1}P\mathsf F^{-1}\mathsf Q|_V
   +2G-P\mathsf Q|_V.}
\tag{5.6}
$$

等价地，将相互交换的自伴算子 $\mathsf F,\mathsf T$ 作联合谱分解

$$
\mathsf F=\sum_\alpha f_\alpha\Pi_\alpha,
\qquad\mathsf T=\sum_\alpha t_\alpha\Pi_\alpha,
\qquad f_\alpha>0,\quad t_\alpha\ne0,
$$

令同一个正算子值权 $W_\alpha=P\Pi_\alpha|_V$，则

$$
W_\alpha\succeq0,\quad\sum_\alpha W_\alpha=I_V,
$$
$$
\boxed{
G=\sum_\alpha f_\alpha^{-1}W_\alpha,\qquad
L=\sum_\alpha t_\alpha^2W_\alpha,\qquad
4G+R_0=\sum_\alpha f_\alpha t_\alpha^2W_\alpha.
}
\tag{5.7}
$$

三个矩确实使用同一个物理 primitive 压缩和同一组联合谱投影。不同 $W_\alpha$ 一般不交换，因此不能将 (5.7) 当成逐源标量化。

### 5.1 共同谱必须保留的真实源定号约束

令 $D=D_{s-1}$、$\Xi=D^2$，并令 $\sigma=(-1)^{s-1}$。还有完整物理恒等式

$$
\boxed{\mathsf T|_V=\sigma p^{-1}\Xi|_V,
\qquad P\mathsf T|_V=\sigma p^{-1}P\Xi|_V.}
\tag{5.8}
$$

特别，$P\mathsf T|_V$ 严格定号。证明如下：由 (3.2)，$DV$ 正是无权最高 primitive 空间 $V^{(0)}=\ker d^{(0)}|_{\mathcal H_{s-1}}$。在此空间上 $\mathsf T^{(0)}=\sigma I$。后一个式子可直接按子集系数验证：令 $k=s-1$，$v=\sum_{|I|=k}v_Ie_I$ 且 $d^{(0)}v=0$。对每个 $|J|=k$，

$$
(\mathsf C_+(e^{(0)})^2v/2)_J
=\sum_{I\cap J=\varnothing}v_I
=\sum_{S\subseteq J}(-1)^{|S|}\sum_{I\supseteq S}v_I
=(-1)^k v_J.
$$

其中 $|S|<k$ 时内和由 $(d^{(0)})^{k-|S|}v=0$ 为零；在 $V^{(0)}$ 上真实第一逆为 $e^{(0)}/2$，故该补集表达式正是 $\mathsf T^{(0)}v$。将这一身份代入 (4.3) 即得 (5.8)。

这里不声称 $\Xi V\subseteq V$，也不声称 $V$ 是 $\mathsf T$ 的整个最大定号子空间。高出生时仍有同符号的较低 birth 分量，后继 Schur 必须保留。第 6 节的抽象共同谱反模型没有保留 (5.8) 的 Boolean 源旗，因而不反驳真实相位候选。

## 6. 已付范围与仍未付的相位步骤

上文没有推出

$$
H_0^*L^{-1}H_0\preceq I,
\tag{6.1}
$$

也没有推出完整弱位铅笔的共同半线 SOS。实际候选 (6.1) 还必须利用
$V=\ker d|_{\mathcal H_{s-1}}$ 与 $U=\ker d|_{\mathcal H_s}$ 在同一 Boolean 系统内的关系，不能只保留一般正算子值矩的形式。

例如，若抽象地取一个共同谱的两点压缩，令 $n>1$，

$$
\mathsf F=\operatorname{diag}(1,n^{-1}),\quad
\mathsf Q=4\mathsf F^{-1},\quad
v=(\sqrt{1-n^{-1}},n^{-1/2}),\quad V=\mathbb C v,
$$

那么 $\mathsf F,\mathsf Q$ 交换，并且压缩后的 $R_0=P\mathsf Q|_V-4G=0$。但

$$
G=2-n^{-1},\qquad
L=4(n+1-n^{-1}),\qquad
H_0=L/G-2G,
$$

从而 $H_0^2/L\sim n$。这只是抽象矩表示不足的反模型，不是 Boolean 模型，也没有反驳真实 (6.1)。它说明若要从 (5.7) 继续，必须保留实际 primitive 源约束，不能仅使用完整层交换性和 $R_0\succeq0$。

本文与已完成的有限弱位铅笔配套；后者见
`2026-11-14-finite-weak-bit-common-defect-pencil-and-coefficient-obstruction-789f-next.md`。
