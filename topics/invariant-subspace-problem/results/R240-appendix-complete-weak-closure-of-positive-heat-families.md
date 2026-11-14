# R240 附录：任意正热族的完整弱闭包与逃逸平方质量的准确标量

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。完整证明承接任意正热平方预算逃逸稿，不要求系数序列单调。

状态：完整弱闭包分类。任何非零弱极限都只是一个原实际正热因子乘以 $(0,1]$ 中的标量；有界平方预算球的闭包还具有尖锐的标量下界。本稿不宣称弱收敛等于强收敛，不使用非正系数或外加标量重标定。

## 1. 系数能量与真实头逼近

沿用
$$
R(b)=e^{-X_b},\qquad b\ge0,\quad b\in\ell^2,\qquad \|R(b)\|\le1.
$$
定义标量函数与总和
$$
f(x)=x-\log(1+x)\quad(x\ge0),\qquad
\mathcal E(b)=\sum_jf(b_j).
\tag{1.1}
$$
因为
$$
0\le f(x)\le x^2/2,
$$
对每个 $b\in\ell^2_+$，
$$
0\le\mathcal E(b)\le\|b\|_2^2/2<\infty.
\tag{1.2}
$$
$\mathcal E$ 是纯尾真空系数的准确对数，不是原实际热范数的替代。

引用[任意正热预算逃逸稿](R240-appendix-arbitrary-positive-heat-budget-escape-and-adaptive-source-obstruction.md)
已经逐项支付的实际有限头与纯尾逼近：
$$
Q_m(b)=e^{-H_m(b)}\otimes R^0(b_{\ge m}),
\qquad H_m(b)=\sum_{j<m}b_jV_j^{[m]},
$$
$$
\boxed{
\|R(b)-Q_m(b)\|
\le M\varepsilon_m
\quad(\|b\|_\infty\le M),
}
\tag{1.3}
$$
其中
$$
\varepsilon_m=
18m\eta_{m-1}+8\sum_{j\ge m}\eta_j\to0.
$$
每个头因子和尾因子都是收缩。
固定前 $m$ 位输入和输出时，纯尾因子贡献准确标量
$$
r_m(b)=
\prod_{j\ge m}e^{-b_j}(1+b_j)
=
\exp[-\mathcal E(b)+\mathcal E_m(b)],
$$
$$
\mathcal E_m(b)=\sum_{j<m}f(b_j).
\tag{1.4}
$$
(1.3) 始终保留实际 carry；(1.4) 仅用于其已付误差后的独立纯尾。

## 2. 有界平方预算序列的准确弱极限

**定理2.1。** 假设
$$
b^{(n)}\ge0,\qquad
\sup_n\|b^{(n)}\|_2\le R<\infty,\qquad
b^{(n)}\rightharpoonup b\quad\text{于 }\ell^2,
$$
并且
$$
\mathcal E(b^{(n)})\longrightarrow\ell.
\tag{2.1}
$$
则 $b\ge0$、$b\in\ell^2$，且
$$
\boxed{
R(b^{(n)})\longrightarrow
\lambda R(b)\quad\mathrm{WOT},
\qquad
\lambda=e^{\mathcal E(b)-\ell}.
}
\tag{2.2}
$$
这个标量满足
$$
\boxed{
e^{-(R^2-\|b\|_2^2)/2}\le\lambda\le1.
}
\tag{2.3}
$$

### 2.1 标量的准确范围

弱收敛给每个坐标收敛。
对每个固定 $m$，
$\mathcal E_m(b^{(n)})\to\mathcal E_m(b)$。
由 $\mathcal E(b^{(n)})\ge\mathcal E_m(b^{(n)})$，得到
$\ell\ge\mathcal E_m(b)$；
再令 $m\to\infty$，有 $\ell\ge\mathcal E(b)$。

另一方面，(1.2) 在尾上给
$$
\mathcal E(b^{(n)})-\mathcal E_m(b^{(n)})
\le
\frac12\left(R^2-\sum_{j<m}(b_j^{(n)})^2\right).
$$
先令 $n\to\infty$，再令 $m\to\infty$，得到
$$
0\le\ell-\mathcal E(b)
\le\frac12(R^2-\|b\|_2^2).
\tag{2.4}
$$
这就是 (2.3)。

### 2.2 实际算子的弱极限

取两个有限 Walsh 柱 $u,v$，并取包含其支撑的 $m$。
由于每个坐标收敛，有限维实际头满足
$$
H_m(b^{(n)})\longrightarrow H_m(b)
\quad\text{于算子范数},
$$
故其负指数也按范数收敛。
由 (1.4)、(2.1)，
$$
\begin{aligned}
\langle Q_m(b^{(n)})u,v\rangle
&=
e^{-\mathcal E(b^{(n)})+\mathcal E_m(b^{(n)})}
\langle e^{-H_m(b^{(n)})}u,v\rangle\\
&\longrightarrow
e^{-\ell+\mathcal E_m(b)}
\langle e^{-H_m(b)}u,v\rangle\\
&=
\lambda\langle Q_m(b)u,v\rangle.
\end{aligned}
\tag{2.5}
$$
所有 $\|b^{(n)}\|_\infty$ 及 $\|b\|_\infty$ 都不超过 $R$。
所以 (1.3) 使
$$
\limsup_n
|\langle[R(b^{(n)})-\lambda R(b)]u,v\rangle|
\le(1+\lambda)R\varepsilon_m\|u\|\|v\|.
$$
令 $m\to\infty$，右侧趋零。
再由收缩性和有限柱稠密性扩展到全部输入输出，证明 (2.2)。

这一步没有把变化的真实有限头强行当成与完整纯尾交换；
使用的是先前已经支付的全算子范数误差。

## 3. 每个允许标量都可由原正热因子实现

固定 $b\ge0$、$b\in\ell^2$ 与 $0<\lambda\le1$。
令
$$
c=-\log\lambda\ge0.
$$
取 $m_n\to\infty$、$N_n\to\infty$，
并在第 $m_n$ 位之后选任意 $N_n$ 个物理位 $I_n$。
定义
$$
b^{(n)}=
b\,\mathbf1_{j<m_n}
+\sqrt{2c/N_n}\,\mathbf1_{I_n}.
\tag{3.1}
$$
两部分支撑不交，且每行有限支撑、非负。
它们满足
$$
b^{(n)}\rightharpoonup b,\qquad
\|b^{(n)}\|_2^2
=\|b_{<m_n}\|_2^2+2c.
\tag{3.2}
$$
尾块弱趋零来自支撑逃向无穷且范数固定。

由 $f(x)=x^2/2+O(x^3)$ 于 $x\to0$，
$$
N_nf(\sqrt{2c/N_n})\longrightarrow c.
$$
因支撑不交，
$$
\mathcal E(b^{(n)})
=\mathcal E(b_{<m_n})
+N_nf(\sqrt{2c/N_n})
\longrightarrow\mathcal E(b)+c.
$$
定理2.1遂给
$$
\boxed{R(b^{(n)})\to\lambda R(b)\quad\mathrm{WOT}.}
\tag{3.3}
$$
若 $c=0$，直接取尾块为零。

如果另有
$$
\|b\|_2^2+2c\le R^2,
$$
那么 (3.2) 保证整个构造都在同一个平方预算球内。
因此 (2.3) 的下界不仅必要，而且准确可达；
等号通过把恰好 $R^2-\|b\|_2^2$ 的平方质量分散到高位小系数块来实现。

没有把这些弱极限写成强极限。
额外标量来自原算子族本身的弱极限，不是事先把热因子乘上一个重标定系数。

## 4. 一个平方预算球的完整弱闭包

记
$$
\mathscr R_R=
\{R(b):b\ge0,\ b\in\ell^2,\ \|b\|_2\le R\}.
$$
则
$$
\boxed{
\overline{\mathscr R_R}^{\,\mathrm{WOT}}
=
\left\{
\lambda R(b):
b\ge0,\ \|b\|_2\le R,\quad
e^{-(R^2-\|b\|_2^2)/2}\le\lambda\le1
\right\}.
}
\tag{4.1}
$$

充分性由 §3。
反向，原 $H$ 可分，算子范数球上的弱算子拓扑可度量，
所以可取一个 $\mathscr R_R$ 中的序列趋于给定弱闭包点。
正 $\ell^2$ 球弱序列紧，可取子列使系数弱收敛到某个 $b$。
由 (1.2)，再取子列使 $\mathcal E(b^{(n)})$ 收敛。
定理2.1便给 (4.1) 的形式和标量界。

特别，$0$ 不属于任何固定有限 $R$ 的这个弱闭包：
(2.3) 给 $\lambda>0$，而每个实际 $R(b)$ 都单射且非零。

这里按存在性的参数描述弱闭包，
不额外断言不同 $(b,\lambda)$ 表示某个算子时的唯一性。

## 5. 无预算限制的正热族没有其他非零弱极限

令
$$
\mathscr R_+=\{R(b):b\ge0,\ b\in\ell^2\}.
$$
则
$$
\boxed{
\overline{\mathscr R_+}^{\,\mathrm{WOT}}
=
\{0\}\ \cup\
\{\lambda R(b):b\ge0,\ b\in\ell^2,\ 0<\lambda\le1\}.
}
\tag{5.1}
$$

§3 给右侧全部非零算子。
$R(ne_0)$ 的范数由单个位的 $0.9^n$ 界趋零，
所以 $0$ 也在闭包内。

反向，设正热序列弱收敛到非零算子 $T$。
取一个在 $T$ 上非零的固定秩一正常泛函。
[预算逃逸定理](R240-appendix-arbitrary-positive-heat-budget-escape-and-adaptive-source-obstruction.md)
表明该序列的 $\ell^2$ 预算必一致有界。
于是它落在某个 $\mathscr R_R$ 中，(4.1) 给所需形式。
有界算子球的可度量性同样把此序列论证扩为完整弱闭包。

旧可数正因子累加的单调情形没有额外的逃逸平方质量，
因而其非零极限仍是旧稿中的一个实际 $R(b)$。
允许任意重新选择正行时，唯一新增的是本稿准确识别的 $(0,1]$ 标量。

## 6. 对配对正则器范围的准确含义

取正热族的任意非零弱极限 $P$。
(5.1) 使
$$
P=\lambda R(b),\qquad \lambda>0.
$$
非零标量不改变任意最小闭乘子的指定配对域条件：
$$
Pf_i\in\operatorname{Dom}X_{Cf_i}
\Longleftrightarrow
R(b)f_i\in\operatorname{Dom}X_{Cf_i}.
$$
它也只按 $\lambda$ 缩放对应聚合源与正常取值。
因此，通过任意非单调正热序列取非零弱极限，
不会在 R244 中产生超出某个原实际正热因子的配对正则能力。

这与上一稿“保非零状态锚且压住真源”的统一预算障碍一致。
结论仍不处理非正系数、不同类型的分母、额外发散标量重标定，
也不由弱闭包分类推出普通 Hilbert ISP 的结论。
