# 指数秩原始块的无权消去与固定前缀完整原始投影的指数障碍

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：以下扩块构造和完整投影下界已证明；未闭合全部实际残量的稳定分解。

本稿应用[相容真空 jets 与无权原始块消去](2026-11-13-compatible-vacuum-jets-and-unweighted-primitive-block-removal-boundary-resume.md)的通用投影结论：在前缀 $I=[m,m+2q-1]$ 上，只要
$$
\operatorname{Ran}P\subseteq H_q(I),\quad P=P P_q(I),
\quad D_IP=P D_I=0,
\tag{0.1}
$$
且 $\|P\|$ 一致受控，任意真实 $w\in M$ 的 $Pr_{m,q}(w)$ 都有合法小修复
$$
\lambda_q^P(w)\le
\sqrt{K_{m+2q,d}}\,\|P\|
\left[\|P_{[q+1,q+d]}^{(m)}w\|
+\sqrt d\,e^{-72d^4}\|w\|\right].
\tag{0.2}
$$
这里的 $P$ 可以有很大的秩。本稿先构造这样的指数秩投影，再证明同一固定前缀的完整原始投影不能具有这种统一范数。

## 1. 均权中间原始空间

在一个有 $2r$ 位的有限块上，令
$$
D_0=\sum_{j=1}^{2r}E_j.
$$
在 $r$ 孔层 $H_r$，
$[D_0,D_0^*]=2r-2\mathcal N=0$，所以
$$
\ker(D_0|_{H_r})=\ker(D_0^*|_{H_r}).
$$
令 $P_0^{(r)}$ 为这个公共核的正交投影，在其他孔层取零。则
$$
D_0P_0^{(r)}=P_0^{(r)}D_0=0.
\tag{1.1}
$$
在第 $r-1$ 层，$D_0D_0^*\ge2I$，故
$D_0:H_r\to H_{r-1}$ 满射。于是
$$
\boxed{
\operatorname{rank}P_0^{(r)}
=\binom{2r}{r}-\binom{2r}{r-1}
=\operatorname{Cat}(r):=\frac1{r+1}\binom{2r}{r}.
}
\tag{1.2}
$$
记 $\operatorname{Cat}(0)=1$。

## 2. 一个近均权块的原始投影范数只损失平方量

现在块为 $[n,n+2r-1]$，原权仍为 $a_j=(j+1)^{-2}$。
令 $a_0=a_n$，定义正对角矩阵
$$
S e_F=\left(\prod_{j\in F}\frac{a_0}{a_j}\right)e_F.
$$
直接按一个删除矩阵元核对，
$$
D_{\rm block}=S(a_0D_0)S^{-1}.
$$
因此
$$
P_{\rm block}=S P_0^{(r)}S^{-1}
\tag{2.1}
$$
是满足原权版本 (1.1) 的投影，其像严格在中间 $r$ 孔层。

对任意 $F$，
$$
0\le\log S_{FF}
\le4r\log\left(1+\frac{2r-1}{n+1}\right)
\le\frac{8r^2}{n+1}.
$$
乘 $S$ 以一个正标量不改变 (2.1)。取居中的标量后，可使
$$
\delta:=\|S-I\|\le\frac{8r^2}{n+1}\le\frac12
\qquad(n+1\ge16r^2).
$$
于是
$$
\|P_{\rm block}-P_0^{(r)}\|
\le\frac{2\delta}{1-\delta}\le4\delta.
\tag{2.2}
$$

这里不能直接把 (2.2) 的线性误差逐块相乘；投影范数有平方改善。
对任何非零有界幂等 $P$，相对于其像的正交分解有
$P=\begin{pmatrix}I&B\\0&0\end{pmatrix}$，故
$$
\boxed{\|P\|^2=1+\|P-P^*\|^2.}
\tag{2.3}
$$
由 (2.2)，$\|P_{\rm block}-P_{\rm block}^*\|\le8\delta$，所以
$$
\boxed{
\log\|P_{\rm block}\|
\le32\delta^2
\le\frac{2048r^4}{(n+1)^2}.
}
\tag{2.4}
$$
所有矩阵都在实际原权下；没有丢掉相似的条件数。

## 3. 前 2q 位上范数趋于1的指数秩投影

写 $q=ar+s$，$0\le s<r$。把前缀 $I=[m,m+2q-1]$ 分成
$a$ 个相邻 $2r$ 位块，最后若 $s>0$ 再加一个 $2s$ 位块。
在每块取 §2 的实际投影，并令
$$
P_q^{(r)}=\bigotimes_{\rm blocks}P_{\rm block}.
$$
它满足 (0.1)，且
$$
\boxed{
\operatorname{rank}P_q^{(r)}
=\operatorname{Cat}(r)^a\operatorname{Cat}(s).
}
\tag{3.1}
$$
因为各块恰有半数孔，全部像恰有 $q$ 孔；每个块的删除从左右都被杀掉，所以整个 $D_I$ 也从左右被杀掉。

若 $m+1\ge16r^2$，把最终小块也用 $r$ 的上界支付，
$$
\begin{aligned}
\log\|P_q^{(r)}\|
&\le2048r^4\sum_{k\ge0}(m+2rk+1)^{-2}\\
&\le2048r^4
 \left[\frac1{(m+1)^2}+\frac1{2r(m+1)}\right]\\
&\le\frac{2048r^3}{m+1}.
\end{aligned}
$$
因此
$$
\boxed{
\|P_q^{(r)}\|\le
\exp\!\left(\frac{2048r^3}{m+1}\right).
}
\tag{3.2}
$$

取原 $m=m(q)$，再令 $r=\lfloor m^{1/4}\rfloor$。
对充分大的 $q$，上述条件满足，$r\to\infty$，且
$r^3/m\to0$，故
$$
\|P_q^{(r)}\|\longrightarrow1.
\tag{3.3}
$$
由
$$
\frac{4^r}{(r+1)(2r+1)}
\le\operatorname{Cat}(r)\le4^r
$$
以及 (3.1)，得到
$$
\boxed{
\log\operatorname{rank}P_q^{(r)}
=(2\log2-o(1))q.
}
\tag{3.4}
$$
这只描述维数主指数，不表示该像等于完整中间原始空间。

对任意真实 $w\in M$，(0.2)、(3.3) 给
$$
\boxed{
\lambda_q^{P_q^{(r)}}(w)
\le(1+o(1))
 \left[\tau_q(w)+\sqrt d\,e^{-72d^4}\|w\|\right]
\longrightarrow0.
}
\tag{3.5}
$$
最小解线性性还给
$$
|\lambda_q(w)-\lambda_q^{I-P_q^{(r)}}(w)|
\le\lambda_q^{P_q^{(r)}}(w)\longrightarrow0.
\tag{3.6}
$$
因此已消去的块不仅是一条配对原始线；它可以具有 (3.4) 的指数秩，而且不要求原核向量的尾正则性。

## 4. 同一固定前缀的完整原始投影唯一

令 $I$ 恰有 $2q$ 位，原权为 $a_j$。
设
$$
K=\ker(D_I|_{H_q(I)}),\qquad
R=D_I H_{q+1}(I).
$$
在均权下，$K_0=R_0^\perp$；按同一个正对角 $S$ 相似后仍有
$$
H_q(I)=K\mathbin{\dot+}R.
\tag{4.1}
$$
因此，在第 $q$ 层上，任何像为全部 $K$ 且杀掉 $R$ 的投影只能是
$$
\boxed{P_{\rm full}=S P_0^{(q)}S^{-1}.}
\tag{4.2}
$$
其余层取零后，它也满足 $D_IP_{\rm full}=P_{\rm full}D_I=0$。
这个投影是唯一的，不能通过另选完整基来改变其算子范数。

## 5. 均权完整投影的互补子集矩阵元

固定一个 $q$ 元子集 $G$。均权 $P_0^{(q)}$ 与所有位排列交换，
因此其列
$$
f(F)=\langle P_0^{(q)}e_G,e_F\rangle
$$
只依赖 $k=|F\cap G|$，记为 $u_k$。
因 $D_0f=0$，对任意 $(q-1)$ 元集合 $H$、$k=|H\cap G|$，
$$
(q-k)u_{k+1}+(k+1)u_k=0.
$$
从 $k=0$ 递推到 $k=q-1$，得到 $u_q=(-1)^qu_0$。
另一方面，置换对称使所有对角元相等；由 (1.2) 的秩，
$$
u_q=\frac{\operatorname{Cat}(q)}{\binom{2q}{q}}
=\frac1{q+1}.
$$
所以对互补 $q$ 元子集 $F=I\setminus G$，
$$
\boxed{
\left|\langle P_0^{(q)}e_G,e_F\rangle\right|
=\frac1{q+1}.
}
\tag{5.1}
$$
这是一段有限维完整证明，没有借用未核的 Specht 张成结论。

## 6. 原固定前缀的完整投影范数指数大

取 $G$ 为前缀的最前 $q$ 位，$F$ 为最后 $q$ 位。
由于 $S_{FF}/S_{GG}=\prod_{j\in G}a_j/\prod_{j\in F}a_j$，
(4.2)、(5.1) 给
$$
\boxed{
\|P_{\rm full}\|
\ge
\frac1{q+1}
\left[
\frac{(m+2q)!\,m!}{((m+q)!)^2}
\right]^2.
}
\tag{6.1}
$$
对原 $m(q)=O(\log\log q)$，
中心二项系数与有限额外乘积的比较给
$$
\log\frac{(m+2q)!\,m!}{((m+q)!)^2}
=2q\log2+o(q).
$$
故
$$
\boxed{
\log\|P_{\rm full}\|
\ge(4\log2-o(1))q.
}
\tag{6.2}
$$
这是原 $(j+1)^{-2}$ 权的实际下界，不是任意不均匀权的抽象例。

特别，若某个分析算子 $\mathcal A$ 和重构算子 $\mathcal R$
在同一固定前缀内满足
$\mathcal R\mathcal A=P_{\rm full}$，则
$$
\|\mathcal R\|\,\|\mathcal A\|
\ge\|P_{\rm full}\|
\ge\exp[(4\log2-o(1))q].
\tag{6.3}
$$
把许多局部原始块相加，并要求在全部 $K$ 上为恒等、在 $R$ 上为零，
也必然合成为同一个 $P_{\rm full}$，因此同样受 (6.2) 限制。

## 7. 已推进的部分与剩余问题

(3.5)–(3.6) 对一个范数趋于1、维数具有几乎完整主指数的实际原始块，给出了真正的无权小修复。这使用真实全局核相容性；局部单位球中同样的方向仍能有很大的最小能量。

(6.2) 同时排除在这个固定前缀上，靠一个统一有界的完整原始投影或稳定分析/重构来直接覆盖全部剩余向量。其余原始方向、跨块删除链、移动前缀或利用真实范围的进一步分解仍需处理。不能从高秩或局部投影范数好直接宣布覆盖所有 $D^d$ 残量。
