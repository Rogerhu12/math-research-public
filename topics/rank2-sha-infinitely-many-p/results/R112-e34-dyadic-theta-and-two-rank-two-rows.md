# R112. E34 的实际 dyadic theta 线与两条秩二 Weil 行

日期：2026-11-12。**状态：已证明实际曲线、局部向量和有限表示接口；
未证明两条曲线的中央导数在无穷多个素数上不同时为零。**

## 1. 曲线身份

固定
\[
 E_{17}:y^2=x^3-17x,\qquad
 E_{34}:y^2=x^3-1156x.
\]
两者的 Mordell–Weil 秩均为二。第二条是已知曲线 $E_{+34}$，
不是新的秩二曲线发现。Cremona 原表的 $18496i1$ 为
$E^+:y^2=x^3+289x$，原 allgens 给生成点 $(68,578),(144,1740)$；
$18496i2$ 正是 $E_{34}$。
两者的 CM 等变 $2$-同源为
\[
 (x,y)\longmapsto
 \left(x+\frac{289}{x},y\left(1-\frac{289}{x^2}\right)\right).
 \tag{1}
\]

以 $E_0:y^2=x^3-x$ 为参考，
\[
                  \psi_{34}=\psi_0(\chi_{136}\circ\mathrm N),
 \tag{2}
\]
其中 $\chi_{136}$ 对应 $\mathbb Q(\sqrt{34})$。
二处的改变是局部二次特征 $\chi_8=(2,\cdot)_2$；
十七处的单位特征是 $\lambda^2$，仍取 $\lambda(3)=-i$。
因此 E34 不属于旧的固定 dyadic 型正参数四曲线比较。

## 2. 新 dyadic 线的完整有限计算

沿用原 self-dual Haar 测度及
$\psi_2(x)=e^{-2\pi_{\mathbb C}i\{x\}_2}$。
令
\[
 g_*=\frac{-3+4i}{5},\qquad
 e_a=\mathbf1_{a/2+2\mathbb Z_2}\quad(0\le a\le3).
\]
$i,g_*$ 拓扑生成 $K_2^1$。
旧 splitting 的两个矩阵为
\[
 I_{ab}=\tfrac12 i^{-ab},\qquad
 G_0=
 \begin{pmatrix}
 0&0&1&0\\0&-1&0&0\\1&0&0&0\\0&0&0&-1
 \end{pmatrix}.
 \tag{3}
\]
第二个矩阵来自保留 Haar 与 Rao 相位的准确和
\[
 (G_0)_{ab}=-\frac14
  \sum_{\substack{j\bmod16\\j\equiv b\ (4)}}
       \zeta_{32}^{-4-3a^2+10aj-3j^2}.
 \tag{4}
\]
写 $j=b+4k$，和的比为 $-i^{5a-3b}$，
故只有 $a+b\equiv2\pmod4$ 的四个位置非零，逐项给 (3)。

新 splitting 相差
$\eta(g)=\chi_8(\mathrm N(i(g-1)))$。
局部 Hilbert 符号给 $\eta(i)=1,\eta(g_*)=-1$，
所以新矩阵为 $I,-G_0$，共同平凡线准确由
\[
 \boxed{\quad
  \phi_2^+=\frac{e_0+e_1-e_2+e_3}{\sqrt2}
 \quad}                                                        \tag{5}
\]
生成。四格各测度 $1/2$，故其 $L^2$ 范数为一。
这里 $\chi_8(2)=1$ 是局部特征的值，
不是 Dirichlet 特征在偶数处的值。

## 3. 同一固定 Weil 向量的两条实际行

十七处自然极化向量为
\[
       v_{17}^+(y)=\frac{\sqrt{17}}{16}
                    \lambda^{-2}(y)\mathbf1_{\mathbb Z_{17}^{\times}}(y).
\]
Yang 1997 的准确 Fourier 核把它变成
$x=t/17$ 上的 $\lambda^2(t)\zeta_{289}^{19t^2}$，
乘一个与 $t$ 无关的非零代数常数。
结合 (5)，全局支撑是 $x=n/34$；因
$\lambda^2(2)=1$、$19/4\equiv77\pmod{289}$，
得到
\[
 a_n^+=
 \begin{cases}
 \varepsilon_n\lambda(n)^2\zeta_{289}^{77n^2},&17\nmid n,\\
 0,&17\mid n,
 \end{cases}
 \qquad
 (\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3)=(1,1,-1,1).
 \tag{6}
\]
共同常数包含 (5) 的 $1/\sqrt2$ 及十七处 Gauss 常数；
本结果不省略这些常数来声称新的单位插值。

取 R108 的 $M=578$、$\mathcal D=\mathbb Z/1156$、
$Q(r)=r^2/2312$ 与
\[
 \Theta_M=\sum_{r\bmod1156}\sum_{n\equiv r(1156)}
                     q^{n^2/2312}\mathbf e_r.
\]
两条行准确为
\[
 \ell_{17}(\mathbf e_r)=
 \begin{cases}
  \lambda(r/2)\zeta_{289}^{19(r/2)^2},&2\mid r,\ 17\nmid r,\\
  0,&\text{其他},
 \end{cases}
 \qquad
 \ell_{34}(\mathbf e_r)=a_r^+.
 \tag{7}
\]
它们线性无关，而且
\[
                 F_{17}=\ell_{17}\Theta_M,\qquad
                 F_{34}=\ell_{34}\Theta_M.                     \tag{8}
\]
第二个 raw theta 形式的 Fourier 指数为 $n^2/2312$。
所有 $4\mid m$ 的中央权共用这些固定有限向量；
二次扭曲在奇次幂下不变。局部不变线均在 Hermitian 参数 $1$，
故 Yang 的实际全局平方公式适用。
两条曲线的中心 $L$ 值为零，因此
\[
                 F_{17}(i)=F_{34}(i)=0,\qquad
                 DF_{17}(i)=DF_{34}(i)=0.                      \tag{9}
\]
后一式也直接来自全局 $i$ 对称所强制的 Hermite 次数 $4\mid m$。

## 4. 低权比较与尚未完成的覆盖

Bruinier–Schwagenscheidt 2017 Lemma 2.1 的三个权 $1/2$ 基
\[
              \Theta_M,\quad\Theta_M^{\sigma_2},\quad
              \Theta_2\mid U_{17}
\]
在任一实际行 $\ell_j$ 下均给 $F_j,F_j,0$。
确实 $\sigma_2r=579r$ 固定偶 $r$；对奇 $r$ 只加 $578$，
不改变 (6)；$U_{17}$ 的支撑被两行杀掉。
所以 R108 的保留实际行的低权比较同时适用于这对候选。

若两条曲线的有限性素数集合之并无穷，则抽屉原理已足够完成
本题的存在性目标。但 (8) 及有限 Weil 空间本身没有给出这种覆盖。
现成 degree-five CM 伸缩差的已知非零对数导数在十七处平凡型；
在共同参考 splitting 下，两条新向量分别为
$\lambda^{-1}$、$\lambda^{-2}$ 型，与平凡型正交。
不能将该已知导数无证分解到本题两条秩二行。
使用非交换 Heisenberg 平移时，必须另算其真实中央导数。

## 5. 完整证明及来源

完整规范和独立核查见
[E34 dyadic 与两行笔记](../notes/2026-11-12-e34-dyadic-theta-and-two-rank-two-rows.md)。

- John Cremona，*ecdata*（2026 年读取）：
  [allcurves 原表](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.10000-19999)、
  [allgens 原表](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allgens/allgens.10000-19999)，
  $18496i1,i2$。
- Tonghai Yang，*Theta liftings and Hecke L-functions*，
  J. reine angew. Math. **485** (1997), 25–53：
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)，
  Corollary 2.10、式 (2.28)、Theorem 2.6。
- Yang **1999** 的 Appendix (A1)–(A3) 和 Haar 规范已在
  [dyadic 原证明](../notes/2026-11-12-dyadic-vector-and-reference-theta.md)
  逐项核定；本结果另算 (4) 的全部有限 Gauss 和。
- Bruinier–Schwagenscheidt **2017** 的原始基定理及整格已在
  [R108](R108-actual-weil-row-and-hasse-remainder.md) 核定。

没有把已知 E34 的存在、单个模素数计算或两行线性无关
当作无穷多个素数的非同时消失。
