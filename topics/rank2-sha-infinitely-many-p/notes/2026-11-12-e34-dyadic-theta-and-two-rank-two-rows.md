# E34 的 dyadic theta 线与两条实际秩二 Weil 行

日期：2026-11-12。状态：以下曲线身份、局部向量与共同有限表示已证明。
未证明两条候选的中央导数在无穷多个素数上不同时消失。

## 1. 第二条候选的精确身份

此前正参数族 $y^2=x^3-17^kx$ 的三个非平凡 $17$ 角色中，只有
$k=1$ 的曲线有秩二。若改变 $2$ 处型，必须另核，不能沿用该结论。

Cremona 原表给
\[
 E^+:y^2=x^3+289x,\qquad\text{标签 }18496i1,\qquad
 \operatorname{rank}E^+(\mathbb Q)=2.
\]
原 allgens 行的两个生成点为
\[
                     (68,578),\qquad(144,1740).
\]
同一类中的 $18496i2$ 为
\[
                   E_{34}:y^2=x^3-1156x.
\]
它正是文献中的固定秩二曲线 $E_{+34}$，不是一个新的曲线例子。
两者由核 $(0,0)$ 的 $2$-同源联系：
\[
 (x,y)\longmapsto
 \left(x+\frac{289}{x},\,y\left(1-\frac{289}{x^2}\right)\right).
 \tag{1}
\]
同源与 $[i]:(x,y)\mapsto(-x,iy)$ 交换，所以相应 CM Hecke 特征相同。

以 $E_0:y^2=x^3-x$ 为参考，$E_{34}$ 是它的 $34$ 二次扭曲。
故
\[
                \psi_{34}=\psi_0(\chi_{136}\circ\mathrm N).
 \tag{2}
\]
这里 $\chi_{136}$ 是 $\mathbb Q(\sqrt{34})$ 的二次特征。
在 $2$ 处，其限制是 $\chi_8$，因为 $17$ 在 $\mathbb Q_2$ 中是平方；
在 $17$ 处，其单位限制是模 $17$ 的二次特征 $\lambda^2$。
$\lambda$ 仍采用原 $E_{17}$ 规范 $\lambda(3)=-i$。

以下明确计算 (2) 造成的 dyadic 改变，不把它当作原向量
$\mathbf1_{\mathbb Z_2}$。

## 2. 固定 $2$ 进空间及准确 Rao 矩阵

沿用[已证 dyadic 规范](2026-11-12-dyadic-vector-and-reference-theta.md)：
$\psi_2(x)=e^{-2\pi_{\mathbb C}i\{x\}_2}$，
$\operatorname{vol}(\mathbb Z_2)=1$，
\[
 i,\qquad g_*=\frac{-3+4i}{5}
\]
拓扑生成 $K_2^1$。令 $\omega_0$ 是原 $\psi_0$ splitting，
$\omega_+$ 是 (2) 的新 splitting。二者相差
\[
 \omega_+(g)=\eta(g)\omega_0(g),\qquad
 \eta(g)=\chi_8\!\left(\mathrm N(i(g-1))\right).
 \tag{3}
\]
这里 $\chi_8$ 表示局部域扩张
$\mathbb Q_2(\sqrt2)/\mathbb Q_2$ 的特征，即 Hilbert 符号 $(2,\cdot)_2$；
不能把 Dirichlet 特征在偶数处的零值代入 (3)。
准确地，
\[
 \eta(i)=(2,2)_2=1,\qquad
 \eta(g_*)=(2,16/5)_2=(2,5)_2=-1.
 \tag{4}
\]

考虑四维 Schwartz 空间
\[
 \mathcal V_2=\{f:\operatorname{supp}f\subset\tfrac12\mathbb Z_2,\
                         f(x+2)=f(x)\},
\]
基为 $e_a=\mathbf1_{a/2+2\mathbb Z_2}$，$a=0,1,2,3$。
它在所需算子下稳定；Fourier 交换互为对偶的格
$2\mathbb Z_2$ 与 $\frac12\mathbb Z_2$，而整 unipotent 与单位伸缩
也保持这个空间。

在此基下，原 $i$ 的作用是
\[
                I_{ab}=\frac12\,i^{-ab}.           \tag{5}
\]
原 $g_*$ 的 splitting 常数为
$\mu_0(g_*)=-\zeta_8^{-1}$。
Rao 核是
\[
 (r_S(g_*)f)(u)=2\int
   \psi_2\!\left(\frac{3u^2-10uv+3v^2}{8}\right)f(v)\,dv.
\]
取 $u=a/2$，在每个格中按 $v=j/2\bmod8\mathbb Z_2$ 分割，得
\[
 [\omega_0(g_*)]_{ab}
 =-\frac14\sum_{\substack{j\bmod16\\j\equiv b\ (4)}}
       \zeta_{32}^{-4-3a^2+10aj-3j^2}.
 \tag{6}
\]
写 $j=b+4k$，内和是一个四项几何级数。它非零恰当
$a+b\equiv2\pmod4$，因为其比为 $-i^{5a-3b}$。
在余下四个位置直接代入指数，准确得到
\[
 \boxed{\quad
 G_0=\begin{pmatrix}
 0&0&1&0\\
 0&-1&0&0\\
 1&0&0&0\\
 0&0&0&-1
 \end{pmatrix}.
 \quad}                                             \tag{7}
\]
这份计算包含 Haar 的 $1/8$、Rao 的 $2$ 及 splitting 相位，
不只是在复近似中认定矩阵。

由 (4)，新表示的两个矩阵为 $I,-G_0$。
直接解共同特征方程给
\[
 \boxed{\quad
 \phi_2^+=\frac1{\sqrt2}(e_0+e_1-e_2+e_3),\qquad
 \omega_+(i)\phi_2^+=\omega_+(g_*)\phi_2^+=\phi_2^+.
 \quad}                                             \tag{8}
\]
共同平凡空间一维。每个格的测度为 $1/2$，所以
$\|\phi_2^+\|^2=1$。拓扑生成性与连续性证明 (8) 对整个 $K_2^1$
成立。其值依 $2x\bmod4$ 为 $(1,1,-1,1)/\sqrt2$。

## 3. $17$ 处 Fourier 核与原有限标签

在自然极化中，原实际 $E_{34}$ 的平均向量为
\[
 v_{17}^+(y)=\frac{\sqrt{17}}{16}\,
      \lambda^{-2}(y)\mathbf1_{\mathbb Z_{17}^{\times}}(y).
 \tag{9}
\]
Yang **1997** Corollary 2.10 的自然 torus 作用，以及
[实结构证明](2026-11-12-theta-real-structure-and-mellin-square.md)
(13)–(15) 的 Fourier 核，均可原样用于非平凡二次特征 $\lambda^2$。
在 $x=t/17$ 时，它除共同非零代数常数外为
\[
             \lambda^2(t)\zeta_{289}^{19t^2}.
 \tag{10}
\]
这里仍固定 $i\equiv4\pmod{17}$、其模 $289$ lift 为 $38$；
全局加法特征的负指数方向使二次相位是 $+19t^2$。

全局支撑由 (8) 与 (10) 给出 $x=n/34$。
在 $2$ 处，$17^{-1}\equiv1\pmod4$，所以 dyadic 权只依 $n\bmod4$。
在 $17$ 处，$t=n/2$；$\lambda^2(2)=1$，且
$19/4\equiv77\pmod{289}$。
记
\[
 \varepsilon_n=
 \begin{cases}
 1,&n\equiv0,1,3\pmod4,\\
 -1,&n\equiv2\pmod4.
 \end{cases}
\]
于是完整 raw 权重与半权形式准确为
\[
 \boxed{\quad
 a_n^+=
 \begin{cases}
 \varepsilon_n\lambda(n)^2\zeta_{289}^{77n^2},&17\nmid n,\\
 0,&17\mid n,
 \end{cases}
 \qquad
 F_{34}(\tau)=\sum_n a_n^+q^{n^2/2312}.
 \quad}                                             \tag{11}
\]
省去的共同常数含 (8) 的 $1/\sqrt2$ 和 (9) 的 Gauss 常数，
与 $n$ 无关；它不影响本篇的行、角色及零点声明。
本文未借此省略常数建立任何新的 $p$-单位插值比较。

## 4. 同一个固定 Weil 向量上的两条秩二行

采用 R108 的 $M=578$、$\mathcal D=\mathbb Z/1156$ 及
$Q(r)=r^2/2312$。原 $E_{17}$ 的行是
\[
 \ell_{17}(\mathbf e_r)=
 \begin{cases}
 \lambda(r/2)\zeta_{289}^{19(r/2)^2},&2\mid r,\ 17\nmid r,\\
 0,&\text{其他}.
 \end{cases}
\]
第二条行则为
\[
                         \ell_{34}(\mathbf e_r)=a_r^+.
 \tag{12}
\]
(11) 的周期为 $1156$，因此 (12) 良定，并有
\[
             \ell_{17}\Theta_M=F_{17},\qquad
             \ell_{34}\Theta_M=F_{34}.              \tag{13}
\]
两行线性无关：$\ell_{17}$ 在所有奇 $r$ 为零，
而 $\ell_{34}$ 在 $r=1$ 非零。
这是真正共同的有限表示，不是仅由两个 theta 空间维数相同所作的识别。

固定有限向量在全部 $4\mid m$ 的 Hecke 中央权中不变：
原 $\psi_0$ 的有限角色在这些权已不变，(2) 的二次扭曲在奇次幂下
也不变。Dyadic 线 (8)、split 线 (9) 与未分歧参考向量给
Hermitian 参数 $1$ 的非零局部不变向量，故 Yang 的全局平方公式
适用于这个实际有限向量。

两条曲线的代数秩均为二。由解析秩零的定理，
其中心 $L$ 值均为零；原平方公式因而给
\[
                       F_{17}(i)=F_{34}(i)=0.
 \tag{14}
\]
固定全局有限向量对有理 $i$ 不变，Hermite 第 $m$ 阶有特征 $i^m$。
因此相应 Hermite 生成函数只含 $4\mid m$ 的项，也有
$DF_{17}(i)=DF_{34}(i)=0$。
本篇不声称这已证明 $F_{34}$ 的二阶 CM 导数是某个 $p$-单位。

## 5. 有限族覆盖尚需要哪一条实际关系

R108 的三个权 $1/2$ 基在 $\ell_{34}$ 下仍为
\[
             F_{34},\qquad F_{34},\qquad0.
 \tag{15}
\]
确实 $\sigma_2$ 固定偶 $r$；对奇 $r$，它把 $r$ 送到 $r+578$，
而 (11) 的符号在两个奇类中相同，其他两个因子不变。
$U_{17}$ 的支撑仍被 $\ell_{34}$ 杀掉。
同样结论适用于两行的任意固定线性组合。

这给一个实际有限族接口：若能证明
$\{E_{17},E_{34}\}$ 的有限性素数集合之并无穷，就可用抽屉原理
得到本课题要求的某一条固定曲线。但 (13) 本身不提供这样的覆盖。

现成的 degree-five CM 伸缩差的已知非零导数仍在 $17$ 处平凡型。
在共同自然极化及参考 splitting 下，两条新 primitive 向量的
单位型分别是 $\lambda^{-1}$、$\lambda^{-2}$；
与平凡型的投影正交。因此该已知导数不落在 (13) 的两行张成中。
若使用非交换的 Heisenberg 平移来混合这些型，必须重新计算真实
中央导数；不能把原已知的固定对数公式不变地搬进来。

## 6. 一手来源与独立核查

- John Cremona，*ecdata* 原始曲线与生成点表（2026 年读取）：
  [allcurves.10000-19999](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.10000-19999)；
  [allgens.10000-19999](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allgens/allgens.10000-19999)。
  已逐行读 $18496i1,i2$；前者实际行为
  \[18496\ i\ 1\ [0,0,0,289,0]\ 2\ 2.\]
  allgens 的实际生成点是 $(68,578),(144,1740)$。
- Tonghai Yang，*Theta liftings and Hecke L-functions*，
  J. reine angew. Math. **485** (1997), 25–53：
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)，
  Corollary 2.10、式 (2.28)、Theorem 2.6。
- Tonghai Yang，*Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves*，Compositio Math. **117** (1999), 337–359，
  Appendix (A1)–(A3)。本篇 (3)–(8) 使用
  [既有 dyadic 笔记](2026-11-12-dyadic-vector-and-reference-theta.md)
  已逐项核过的完整 splitting 与 Haar 规范；
  有限 Gauss 和 (6)–(7) 在本篇另行精确计算。

局部二次特征取值、两个有限矩阵的共同特征线及 $L^2$ 范数
已由另一子代理独立复算。没有把单个有限域计算或高精度样例
当作无穷非消失定理。

