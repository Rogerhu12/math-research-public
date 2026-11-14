# 慢符号普遍范围的泛函分解接口：有限秩判据与固定真空因子的实际障碍

日期：2026-11-12（UTC）。作者：literature。

状态：完整接口与实际反障碍，不另编号。
本稿没有否定一般的循环第一因子分解，
也没有证明具体慢符号已经具有普遍稠密像。

## 1. 真正需要的强主理想条件

记 $\mathfrak C=\{A\}'$。
R88 给 $\mathfrak C=\overline{\mathbb C[A]}^{\mathrm{SOT}}$，
且该交换子代数交换。
固定 $S\in\mathfrak C$。

下列条件等价：

1. $I\in\overline{S\mathbb C[A]}^{\mathrm{SOT}}$；
2. $I\in\overline{S\mathfrak C}^{\mathrm{SOT}}$；
3. 在任意有限放大 $A^{(d)}$ 的任意非零闭不变子商 $Q$ 上，
   $S_Q$ 单射且值域稠密；
4. 对每个有限秩泛函
   $$
   \varphi(T)=\sum_{j=1}^d\langle Tf_j,g_j\rangle,
   \tag{1.1}
   $$
   若 $\varphi(S\mathfrak C)=0$，则 $\varphi(I)=0$。

前两项由 R88 及有界左乘的强连续性等价。
若有强主理想单位，
它下降所有有限放大不变子商，
立即给核为零和稠密像。

反之，给定有限组 $f_1,\ldots,f_d$，令
$$
M=\overline{\{(p(A)f_1,\ldots,p(A)f_d):p\in\mathbb C[z]\}}.
$$
$S^{(d)}M$ 稠密于 $M$，
所以可同时将所有 $f_j$ 逼近为 $Sp(A)f_j$。
这给所需强闭包。

最后，线性子空间的强算子闭包与弱算子闭包相同：
两个局部凸拓扑的连续线性泛函都是有限个向量泛函之和。
对线性子空间使用 Hahn–Banach 分离，
便得到第4项。
这里仅需有限秩泛函，不需要先处理所有迹类泛函。

这给出当前慢符号问题的准确等价形式：
$$
\boxed{
S\text{ 的普遍分母性质}
\iff
\text{不存在 }\varphi(S\mathfrak C)=0,\ \varphi(I)\ne0
\text{ 的有限秩泛函}.
}
\tag{1.2}
$$

## 2. 循环第一因子分解是一个充分条件

假设一个有限秩泛函在 $\mathfrak C$ 上可以写成
$$
\varphi(T)=\langle Tf,g\rangle
\qquad(T\in\mathfrak C),
\tag{2.1}
$$
其中 $f$ 是 $A$ 的循环向量。

若 $S$ 在原 $H$ 上具有稠密像，
且 $\varphi(S\mathfrak C)=0$，
则 $g$ 正交于
$$
S\mathfrak C f.
$$
因为 $\mathfrak C f$ 稠密于 $H$，其像的闭包为
$\overline{SH}=H$，所以 $g=0$，$\varphi=0$。

因此：
$$
\boxed{
\begin{gathered}
S\text{ 在原 }H\text{ 上稠密像，且每个有限秩泛函}\\
\text{在 }\mathfrak C\text{ 上都能有某个循环第一因子的表示}\\
\Longrightarrow
I\in\overline{S\mathbb C[A]}^{\mathrm{SOT}}.
\end{gathered}}
\tag{2.2}
$$
对已知全空间 quasiaffine 的单个慢符号，
这会解决其全部限制和子商的范围问题。

(2.2) 是充分方向。
本稿不声称这种一般分解是普遍分母性质的必要条件，
也不把它与 (1.2) 的准确等价判据混淆。

若只关心原 $H$ 中的单个不变子商，
一个失败的子商本身已可由一个向量泛函检测：
若 $SM\subseteq N\subsetneq M$，
选 $x\in M\setminus N$ 和 $g\in N^\perp$，
使 $\langle x,g\rangle\ne0$，
则 $\langle STx,g\rangle=0$ 对所有 $T\in\mathfrak C$。
有限放大的普遍结论相应需要有限个向量泛函之和。

## 3. 不得混同 WOT/SOT 与 ultraweak 闭包

$\mathfrak C$ 是弱星闭的算子代数，
其正常泛函来自迹类算子的限制。
一般正常泛函可写成绝对可和的无限个向量泛函之和，
而不一定是 WOT 或 SOT 连续的有限和。

若每个正常泛函都能作 (2.1) 的循环因子表示，
可进一步得到 $S\mathfrak C$ 的 ultraweak 稠密性，
这是更强的充分条件。
但第1节的强主理想单位本身没有给统一有界范数的逼近网，
因此不能倒推出这一更强结论。

特别，有限柱配对的表示在前对偶范数下收敛，
并不保证对应的 $H$ 向量范数受控。
下面给出一个显式的秩一实例；
因此这个风险不只是无限迹类分解的记号问题。

## 4. 一列真实测试乘子：真空像有界而算子范数无界

取
$$
b_j=(j+1)^{-1},\qquad
B_N=\sum_{j=0}^N b_jV_j,
\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
\tag{4.1}
$$
每个 $B_N$ 都属于真正解析的 $\mathcal A$ 演算。

实际不同位恒等式给 $V_j1=\chi_j$，
所以
$$
\boxed{
\|B_N1\|^2=\sum_{j=0}^N b_j^2
\le g^2,\qquad g=\pi/\sqrt6.
}
\tag{4.2}
$$
另一方面，$\chi(V_j)=1$，
故
$$
\|B_N\|\ge|\chi(B_N)|
=\sum_{j=0}^Nb_j\to\infty.
\tag{4.3}
$$

令 $V_j^0=I-2E_j$，$B_N^0=\sum_{j\le N}b_jV_j^0$。
真实 carry 差具有一致界
$$
\boxed{
\|B_N-B_N^0\|
\le8g\|\eta\|_2=:K_*.
}
\tag{4.4}
$$
在 Walsh 次数表示中，
$$
V_j^0=C_j-A_j+2n_j,\qquad
\operatorname{Re}V_j^0=2n_j,
\tag{4.5}
$$
其中 $n_j$ 是第 $j$ 位被占据的正交投影。

## 5. 连续且处处非零的秩一泛函反障碍

选严格递增的整数 $M_n$，使
$$
\sum_{j=0}^{M_n}b_j\ge32^n.
\tag{5.1}
$$
令 $F_n=\{0,\ldots,M_n\}$，并定义
$$
\boxed{
f=1+\sum_{n\ge1}4^{-n}\chi_{F_n}.
}
\tag{5.2}
$$
各 Walsh 单项式连续，级数一致收敛。
因此 $f$ 连续且实值，并满足
$$
\frac23\le f(y)\le\frac43.
\tag{5.3}
$$
它是明确的非零 $L^2$ 向量。
本稿不据 (5.3) 宣称它的完整 $A$ 循环性。

令
$$
\varphi(T)=\langle Tf,f\rangle.
\tag{5.4}
$$
这是一个正的秩一正常泛函。
不同 $F_n$ 对应正交 Walsh 向量，且
$$
\|n_jf\|^2=\sum_{n:j\le M_n}16^{-n}.
$$
所以由 (4.5)，
$$
\operatorname{Re}\langle B_N^0f,f\rangle
=2\sum_{n\ge1}16^{-n}
\sum_{j=0}^{\min(N,M_n)}b_j.
\tag{5.5}
$$
所有项非负，随 $N$ 单调增加。
(5.1) 给其极限至少
$$
2\sum_{n\ge1}16^{-n}32^n
=2\sum_{n\ge1}2^n=+\infty.
$$
由 (4.4)，真实 carry 只能贡献有界误差，
故
$$
\boxed{\operatorname{Re}\varphi(B_N)\to+\infty.}
\tag{5.6}
$$

记原模型的双线性配对为
$$
\mathcal B(x,y)=\langle x,Cy\rangle.
$$
若存在 $h\in H$ 使
$$
\varphi(T)=\mathcal B(Th,1)\qquad(T\in\mathfrak C),
\tag{5.7}
$$
则由每个 $T\in\mathfrak C$ 的 $C$ 对称性，
$$
|\varphi(B_N)|
=|\mathcal B(h,B_N1)|
\le g\|h\|,
$$
与 (5.6) 矛盾。
因此
$$
\boxed{
\text{即使是这个秩一正常泛函，也不能把其中一个配对因子固定为 }1.
}
\tag{5.8}
$$

点态 $f$ 连续且有正下界，
并没有把这种算子代数分解自动变成点态函数分解。

## 6. 对一个完整正则类的两端因子障碍

定义
$$
\mathscr R
=\{v\in H:\sup_N\|B_Nv\|<\infty\}.
\tag{6.1}
$$
若
$$
\varphi(T)=\mathcal B(Tv,w)
$$
且 $v\in\mathscr R$，则
$|\varphi(B_N)|\le\|w\|\sup_N\|B_Nv\|<\infty$。
如果 $w\in\mathscr R$，
用 $C$ 对称性移到另一端，同样矛盾。
所以 (5.4) 不允许任一配对因子属于 $\mathscr R$。

这个类包含全部有限 Walsh 次数的 $\ell^2$ 完成空间，
不是只包含有限柱。
为核对，固定 $p$。
在次数不超过 $p$ 的空间上，有限系数行的创建、消灭、占据部分满足
$$
\begin{aligned}
\|C_bv\|&\le g\sqrt{p+1}\|v\|,\\
\|A_bv\|&\le g\sqrt p\|v\|,\\
\|D_bv\|&\le g\sqrt p\|v\|.
\end{aligned}
$$
按 (4.5) 及三角不等式，
再加 (4.4)，得到与 $N$ 无关的安全界
$$
\boxed{
\|B_Nv\|
\le\bigl(4g\sqrt{p+1}+K_*\bigr)\|v\|,
\qquad v\in H_{\le p}.
}
\tag{6.2}
$$
这些估计先在有限支持 Walsh 系数上成立，
再由 Hilbert 范数完成延到全部 $H_{\le p}$。
其中占据项的对角值由
$|\sum_{j\in F}b_j|\le g\sqrt{|F|}$ 控制。

此外，$\mathscr R$ 在所有有界交换子下不变：
$$
B_NTv=T B_Nv,\qquad T\in\mathfrak C.
$$
因此它还包含所有有限次数向量的有界交换子像及有限线性组合。

这个障碍仍然没有否定存在一个别的循环因子。
例如高次数的某些已知循环类不必属于 $\mathscr R$。
不能把 (6.1) 当作所有循环向量的刻画。

## 7. 有限柱因子的 Hilbert 范数确实发散

令
$$
f_r=1+\sum_{n=1}^r4^{-n}\chi_{F_n},
\qquad
\varphi_r(T)=\langle Tf_r,f_r\rangle.
$$
$f_r$ 是有限柱，且 $f_r\to f$ 在 $H$ 中和一致范数中均成立。
所以在正常泛函范数中
$$
\|\varphi_r-\varphi\|
\le(\|f_r\|+\|f\|)\|f_r-f\|\to0.
\tag{7.1}
$$

对每个有限柱 $v$，
实际有限 Walsh 乘子
$$
X_v=\sum_F\widehat v_F\prod_{j\in F}V_j
$$
属于真正解析的 $A$ 演算，并满足 $X_v1=v$。
因此有限柱配对可准确改写为
$$
\varphi_r(T)
=\mathcal B(T h_r,1),
\qquad
h_r=X_{f_r}X_{Cf_r}1.
\tag{7.2}
$$
所有因子有界、交换且 $C$ 对称。
$h_r$ 是一个真正解析乘子作用于 $1$ 的向量。
因 $\varphi_r(I)=\|f_r\|^2>0$，该解析乘子非零；
故 $h_r$ 是已知的循环向量。

但是，在 $N=M_r$ 处，
(5.1)、(5.5)、(4.4) 给
$$
\operatorname{Re}\varphi_r(B_{M_r})
\ge
2\sum_{n=1}^r2^n-K_*\|f_r\|^2.
$$
结合 (4.2)、(7.2)，得到
$$
\boxed{
\|h_r\|
\ge
g^{-1}\left(2\sum_{n=1}^r2^n-K_*\|f_r\|^2\right)
\longrightarrow\infty.
}
\tag{7.3}
$$
事实上该下界按 $2^r$ 增长，
而 (7.1) 的误差按 $4^{-r}$ 下降。

因此有限柱正常泛函的快速前对偶收敛，
不能直接传成真空因子向量的有界性或 Hilbert 空间极限。
这给出了该步骤的真实反障碍。

## 8. 对具体慢符号还保留什么

对
$$
S_N=\sum_{j\ge0}(j+1)^{-2}N_j
\quad\text{或}\quad
S_Y=\sum_{j\ge0}(j+1)^{-2}N_j(I+N_j)^{-1},
$$
已知全空间核和范围结论，并不自动给第1节的强主理想单位。

本稿精确建立：

1. 真正等价的目标是有限秩泛函的湮灭判据 (1.2)；
2. 每个有限秩泛函具有某个循环第一因子，是一个充分但未证的一般路线；
3. 固定因子为 $1$，以及只在 (6.1) 的正则类内选择因子，都不足以实现所有有限秩泛函；
4. 具体的有限柱前对偶极限可以伴随分解向量的巨大范数发散。

没有证明一般循环因子分解不存在，
没有把 $f$ 的点态正性当作 $A$ 循环性，
也没有把这些功能分析障碍当成原 Haar 不变子商的反例。
