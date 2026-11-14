# R157 — 准确平尾加标量矩阵的正支参考及严格 33/5 曲率界

**状态：已证明。** 对当前外设计参数不能改变的末 $0.02$ 区间，本文构造一个全角、全正 Bernstein 尾参数盒有效的第二基本形式参考。它准确满足 Gauss、准确接到给定 cut 的 II 迹，并且所有主曲率严格小于 $33/5=6.6$。其 Codazzi 缺陷写成明确公式并保留；它是可消费的较温和初猜，不是已实现度量的浸入或闭曲面。

## 1. 输入、方向及适用范围

采用 R155/R156 的当前 candidate
`notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json`，
SHA256 `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
切口半径准确为 $a_c=4/5$；末桥长 $L=.026$，初始深相位 $-p_d=-1.45$，准确终相位为 $-\pi/2$。在 $r=s_c-s$ 坐标中
$$
\epsilon(r)=D\left(3r^2/L^2-2r^3/L^3\right),\qquad
D=\pi/2-p_d,
$$
$$
a=a_c+\int_0^r\cos\epsilon(q)\,dq,\quad
a_s=-\cos\epsilon,\quad K=\frac{\sin\epsilon\,\epsilon_r}{a}.
\tag{1}
$$
这些是实际三次相位桥的准确积分定义，见 R156 第 1 节。外设计的七个 bump 在 $r\le1/50$ 上恒零，所以这里的 $a,K$ 与未知 $\delta$ 无关。全文只在这个保护条带上使用未改变的基准式，不把它借给其它被改动的前缀。

令
$$k(u)=\kappa(a_c\sin u)$$
为准确切口尾曲率。**本文把这个切口函数固定在材料角 $u$ 上延伸**，不是把半径改为 $a(s)$ 后重新评价 $\kappa(a(s)\sin u)$。R132 的控制盒 $0\le p_j\le6/5$ 给
$$0\le k(u)\le k_{\max}=\frac{4725}{736}.$$
上半尾的既定法向使准确 II 迹为
$$
S_T(u)=k(u)
\begin{pmatrix}\sin^2u&-\sin u\cos u\\-\sin u\cos u&\cos^2u\end{pmatrix}.
\tag{2}
$$
相位改变只重排 $u$，下列统一界因此对所有相位同样成立。

## 2. 当前 K 的简单严格有理上界

输入定义数无论以命名十进制解释，还是以保存二进制有理数解释，都满足
$$L>1/40,\qquad 14499/10000<p_d<3/2.$$
使用 $\pi<22/7$ 得
$$0<D<\frac{11}{7}-\frac{14499}{10000}
=\frac{8507}{70000}<\frac18.$$
而 $a\ge a_c=4/5$、$0\le\epsilon\le D$、
$$0<\epsilon_r\le\frac{3D}{2L}\quad(0<r<L).$$
于是整个未改基准末桥开片（因而当前保护条带）都有
$$
0<K=\frac{\sin\epsilon\,\epsilon_r}{a}
<\frac{3D^2}{2La}
<\frac{(3/2)(1/8)^2}{(1/40)(4/5)}
=\frac{75}{64}.
\tag{3}
$$
这是连续的有理预算，不使用有限采样的 $K$ 最大值。

## 3. 参考的准确定义、Gauss 和端值

定义
$$
h=\sqrt{k^2+4K},\qquad
b=\frac{h-k}{2}=\frac{2K}{h+k},\qquad
\widehat S=S_T+bI.
\tag{4}
$$
最后的商只在 $h+k>0$ 时使用；$K=k=0$ 时直接定义 $b=0$。它对应 R155 正支坐标
$$d=k\cos2u,\qquad m=-\frac k2\sin2u.$$
由于 $b^2+kb=K$，(2) 的特征值 $0,k$ 变成
$$\widehat\lambda_-=b,\qquad\widehat\lambda_+=k+b.$$
故内部 $K>0$ 时 $\widehat S$ 正定且
$$\det\widehat S=b(k+b)=K.$$
在 $K=0$ 切口上 $b=0$，完整 II 迹准确等于 $S_T$，包括全零尾弧、轴点以及任何零 $n$。这些结论没有角截断、投影或求解误差。

## 4. 全参数盒的严格曲率界

取 $C=33/5$。有
$$
C(C-k_{\max})=\frac{21879}{18400},\qquad
\frac{21879}{18400}-\frac{75}{64}=\frac{633}{36800}>0.
\tag{5}
$$
对全部 $0\le k\le k_{\max}$，(3)–(5) 给出
$$K<C(C-k),\qquad C>k.$$
若 $k+b\ge C$，则 $b\ge C-k$，从 $b(k+b)=K$ 推得
$K\ge C(C-k)$，矛盾。因此
$$
\boxed{0\le\widehat\lambda_-\le\widehat\lambda_+<33/5}
\tag{6}
$$
于整保护条带、完整角圆以及 R132 的整个非负尾控制盒成立。这个形式主曲率预算低于 $1/\rho=125/17$，其中 $\rho=17/125$；但在 Codazzi 和实际浸入尚未成立时，不能把 (6) 称为某个已存在曲面的曲率或 reach 证书。

## 5. 全角端值与一阶迹

始终有 $0\le b\le\sqrt K$，所以
$$\|\widehat S-S_T\|_{\mathrm{op}}=b\le\sqrt K.$$
R156 的真实三次退化
$$K=Cr^3+O(r^4),\qquad C>0$$
给出全角一致的 $O(r^{3/2})$ 端值误差。

在 $K>0$ 的内部，固定材料角求导得
$$b_s=K_s/h,\qquad b_u=-b k_u/h.$$
其中
$$|b_s|\le |K_s|/(2\sqrt K)=O(r^{1/2})$$
全角一致趋于零。对于角导数，$b/h\le1/2$，所以
$|b_u|\le|k_u|/2$。非负 $C^1$ 函数 $k$ 在每个零点有 $k_u=0$。
在紧角圆上，$\sup_{k\le\eta}|k_u|\to0$；否则取反例序列及收敛子列便与零点导数为零矛盾。
在补集 $k\ge\eta$ 上有
$$|b_u|\le K\|k_u\|_\infty/\eta^2\longrightarrow0.$$
先取小 $\eta$、再取小 $r$，证明 $b_u\to0$ 全角一致。故准确 cut 的值与材料角一阶迹都保留，参考在这一侧的径向一阶迹也连续且增量导数为零。

这没有声称参考的 II 在切口另一侧径向导数也匹配原尾，更没有把 II 径向 $C^2$ 加为曲面 $C^2$ 的必要条件。尤其 $k=0$ 处 $b=\sqrt K$ 通常有 $r^{3/2}$ 项，不是径向 $C^2$。按 R156，这种情况本身不构成原题的正则性障碍；仍须真正解相容方程和完成实际 $C^2$ 接合。

## 6. 真实 Codazzi 缺陷与积分消费

按数组顺序 $(n,m,l)$，参考为
$$
\widehat n=k\cos^2u+b,\quad
\widehat m=-k\sin u\cos u,\quad
\widehat l=k\sin^2u+b.
$$
令 $c=a_s/a$，以 R155 的符号定义
$$R_n=n_s-m_u/a-c(l-n),\qquad R_m=m_s-l_u/a+2cm.$$
逐项求导给出准确公式
$$
\boxed{R_n=b_s+\frac{k_u\sin u\cos u+(1+a_s)k\cos2u}{a},}
\tag{7}
$$
$$
\boxed{R_m=-\frac{b_u+k_u\sin^2u+(1+a_s)k\sin2u}{a}.}
\tag{8}
$$
因此在 $k$ 恒零的尾开弧，$R_n=b_s$ 一般不为零；这一点与 R156 的旋转参考在相同零弧准确满足 Codazzi 不同。两种参考提供不同初猜，不能把各自优点拼成一条未经验证的解。

固定材料角的真实格平均版本只需把 (7) 的 $b_s$ 换为
$(b_R-b_L)/\Delta s$，其余项用实际径向平均积分；(8) 原样积分。这避免额外求 $K_s$。若调用内部点态诊断，$K_s$ 必须来自真实 profile 导数，不能用有限场的 $nl-m^2$ 或其它候选替代。计算角依赖 $s$ 时仍须加入 R155 的完整 atlas 漂移和端点变化。

要把这块参考接进上游初猜，必须明确入口窗或其它连接；其产生的实际 Gauss/Codazzi 缺陷不能丢弃。本文只给末段参考及准确端口，没有证明和上游未知核自动接合。保持同一个目标 $a,K$ 时，这是改变近似 II 字段，不是改变物理度量，也不是把参考强加为所有解必须具有的形式。

## 7. 代码、准确常数消费和范围

`scripts/fd2d_gc_terminal_rank_one_reference.py` 给出：

- `terminal_rank_one_reference(K,kappa,u,kappa_u=...)`：实际值、材料角 jet、$h,b$ 和两个特征值；$K=0$ 时直接给准确尾迹。
- `terminal_rank_one_interior_jet(a,a_s,K,K_s,kappa,u,kappa_u=...)`：只在内部 $K>0$ 取商，返回真实径向 jet 及 (7)–(8)。

输入 `kappa` 的语义必须是固定的 $k_T(u)$。helper SHA256 为
`edae03a13f19347c33258a089bec27738d9aaae5fd76619b28ad698e6d9abd98`。

`scripts/fd2d-terminal-rank-one-reference-check.py` 从实际 candidate 二进制数准确转有理数，确认末桥身份、$D<1/8$、$L>1/40$，并用 `Fraction` 准确支付 (3)–(6) 的余量 $633/36800$。它另用一个独立标量度量的 561 个有限点检查实际值的差分 jet 和 (7)–(8)，不重复主代理的 actual14 比较或 BVP。

该次调用 chunk **4ad674**，直接自然 exit **0**，报告
`notes/2026-11-12-fd2d-terminal-rank-one-reference-check-01.json`。
径向 jet 差分误差最大 $5.574\times10^{-11}$、角 jet 为 $1.244\times10^{-10}$、Codazzi 公式为 $8.974\times10^{-11}$，Gauss 算术误差 $1.111\times10^{-16}$。有理曲率预算是严格代数结论；这些有限实现检查不被称为额外连续证书。

参考材料：R132（准确正 Bernstein 平尾及曲率盒），R155（正确正支、完整窗口与 Codazzi），R156（实际三次末桥及退化阶），R136（当前物理 profile 的准确积分定义）。
