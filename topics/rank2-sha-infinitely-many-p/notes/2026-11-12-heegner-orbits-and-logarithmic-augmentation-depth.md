# 固定 Heegner 映射强迫的跨素数增广长度

日期：2026-11-12。状态：以下实际挠点、轨道和增广长度结论均已证明。
本篇沿用 R105 的固定辅助域和真实类群和；没有证明最底增广层非零，
没有完成无穷多个素数的 Sha 有限性。

固定
$$
F=\mathbb Q(\sqrt{-15}),\qquad E:y^2=x^3-17x,
$$
以及 R105 的非恒定有限映射
$$
\Phi:X_0(3N_E)\longrightarrow E,\qquad
\Phi(z_\ell)=X_\ell=(1+\tau_\ell)P[\ell].
\tag{1}
$$
记 $d_\Phi=\deg\Phi$。对每个充分大的输入素数 $p$，选 R105 的
辅助素数 $\ell$，因此 $v_p(\ell+1)=1$、$\ell\ll p^{C}$，并有
$$
0<\widehat h(X_\ell)\le C_X\log p
\tag{2}
$$
其中常数与 $p$ 无关。写 $H_\ell=F[\ell]$，令
$\sigma_p\in\operatorname{Gal}(H_\ell/F)$ 为任意阶 $p$ 元，
$\Delta_p=\sigma_p-1$。

## 1. 固定阿贝尔扩张中的挠点恰为全部二挠点

有准确等式
$$
E(F^{\rm ab})_{\rm tors}=E[2].
\tag{3}
$$
所需有限域数据如下。每一行可由
$\#E(\mathbb F_q)=q+1+\sum_{x\in\mathbb F_q}(\frac{x^3-17x}{q})$
直接核对，附带脚本只作这些整数有限求和。

| $q$ | $(\frac{-15}{q})$ | $\#E(\mathbb F_q)$ | $a_q$ | CM Frobenius $\alpha_q$ | $\alpha_q-\bar\alpha_q$ |
|---|---:|---:|---:|---|---|
| $53$ | $1$ | $68$ | $-14$ | $-7\pm2i$ | $\pm4i$ |
| $61$ | $1$ | $74$ | $-12$ | $-6\pm5i$ | $\pm10i$ |

解释 Frobenius 的归属时不需要选择上表的符号：两个素数均为好普通
素数，且在 $\mathbb Q(i)$ 中分裂。约化的 Frobenius 与 $[i]$ 交换，
故属于 $\mathbb Q(i)$；其整性和 $\mathbb Z[i]$ 的极大性使它属于
$\mathbb Z[i]$。迹为 $a_q$、范数为 $q$ 即给上表。
选与这个约化相容的算术 Frobenius $h_q\in G_{\mathbb Q}$，则在全部
prime-to-$q$ 挠点上，它准确作用为 $[\alpha_q]$。
因 $q$ 在 $F$ 分裂，可取 $h_q\in G_F$。

$F\ne\mathbb Q(i)$，所以存在 $g\in G_F$，其在
$\mathbb Q(i)$ 上为非平凡自同构。对任意
$T\in E(F^{\rm ab})_{\rm tors}$，$g,h_q$ 在 $T$ 及其共轭点上的
作用交换，因为 $F^{\rm ab}/F$ 是阿贝尔扩张。如果 $T$ 的阶与 $q$
互素，则
$$
0=(gh_q-h_qg)T
  =[\bar\alpha_q-\alpha_q]gT.
\tag{4}
$$
因此 prime-to-$53$ 挠点被 $4$ 杀，prime-to-$61$ 挠点被 $10$ 杀。
对 $53$-primary 部分使用第二式，得到它为零；对 $61$-primary 部分
使用第一式，同样为零。其余部分同时被 $4$ 和 $10$ 杀，故被 $2$ 杀。
这证明 (3) 的包含方向。

反向，全部二挠点为
$$
O,\quad(0,0),\quad(\sqrt{17},0),\quad(-\sqrt{17},0),
$$
它们均在二次阿贝尔扩张 $F(\sqrt{17})/F$ 中，故 (3) 成立。

## 2. 任意正次增广差分都非挠

若 $p>4d_\Phi$，则
$$
\Delta_p^kX_\ell\ \text{非挠}
\qquad\text{对每个整数 }k\ge1.
\tag{5}
$$
先证 $k=1$。若 $\Delta_pX_\ell$ 为挠点，由 (3) 得
$[2]\Delta_pX_\ell=0$，即 $[2]X_\ell$ 为 $\sigma_p$ 不变。

另一方面，$z_\ell$ 的定义域恰为 $H_\ell$：其 $j$ 值属于
CM 阶 $\mathcal O_\ell$，而 $F(j(z_\ell))=H_\ell$ 是环类域的
标准 CM 生成性质；R105 又已给出 $z_\ell\in X_0(3N_E)(H_\ell)$。
因此以下 $p$ 个源点彼此不同：
$$
z_\ell,\ \sigma_pz_\ell,\ \ldots,\ \sigma_p^{p-1}z_\ell.
$$
它们在固定有限映射 $[2]\circ\Phi$ 下却有同一个像 $[2]X_\ell$。
该映射的次数为 $4d_\Phi$，任一几何纤维中的不同点数至多为这个数，
与 $p>4d_\Phi$ 矛盾。故 $\Delta_pX_\ell$ 非挠。

令 $V=E(H_\ell)\otimes_{\mathbb Z}\mathbb Q$。$\sigma_p$ 在 $V$
上满足 $\sigma_p^p=1$，而 $T^p-1$ 在特征零没有重根。因此
$$
\ker(\sigma_p-1)^k=\ker(\sigma_p-1)
\quad(k\ge1).
$$
若某个 $\Delta_p^kX_\ell$ 为挠点，它在 $V$ 中为零，便会迫使
$\Delta_pX_\ell$ 也为挠点。由上一段即得 (5)。
这里使用的是真实 CM 点的完整轨道和固定映射的纤维次数，
不是从一个抽象循环表示中假定 $X_\ell$ 有非平凡分量。

## 3. 约对数多个实际增广层同时不可 p 除

存在固定常数 $C_0$，使对充分大的输入 $p$，若
$$
K_p=\left\lfloor
\log_2p-\frac12\log_2\log p-C_0
\right\rfloor,
\tag{6}
$$
则
$$
\boxed{\quad
\Delta_p^kX_\ell\notin pE(H_\ell)
\qquad(0\le k\le K_p).
\quad}
\tag{7}
$$
特别地，对任意固定 $\epsilon>0$，充分大的 $p$ 满足 (7) 对所有
$0\le k\le(1-\epsilon)\log_2p$ 成立。

证明：典范高度为 Galois 不变的二次型，由平行四边形恒等式得
$$
\widehat h(\Delta_pZ)
=\widehat h(\sigma_pZ-Z)
\le2\widehat h(\sigma_pZ)+2\widehat h(Z)
=4\widehat h(Z).
$$
迭代后配合 (2)，得到
$$
\widehat h(\Delta_p^kX_\ell)
\le4^kC_X\log p.
\tag{8}
$$
R102 已核的 Baker 定理给固定正常数 $c_{E,F}$，使
$E(F^{\rm ab})$ 中所有非挠点的典范高度至少为 $c_{E,F}$。
若 $\Delta_p^kX_\ell=pR$ 且 $R\in E(H_\ell)$，由 (5) 或 (2)
可知 $R$ 非挠，因而
$$
\widehat h(\Delta_p^kX_\ell)=p^2\widehat h(R)
\ge c_{E,F}p^2.
\tag{9}
$$
选固定 $C_0$ 使 $4^{-C_0}C_X<c_{E,F}$，则 (6)、(8) 与 (9)
对 $k\le K_p$ 矛盾，证明 (7)。

令 $\bar X_\ell$ 为 $X_\ell$ 在有限维 $\mathbb F_p$ 空间
$E(H_\ell)/pE(H_\ell)$ 中的像。其循环子模上的
$\Delta_p$ 满足 $\Delta_p^p=0$，而 (7) 给
$$
\Delta_p^{K_p}\bar X_\ell\ne0.
\tag{10}
$$
所以该真实点模 $p$ 的 Jordan 长度至少为 $K_p+1$。
这个长度随着输入素数趋于无穷；它是 (7) 的等价线性代数表述，
不是对整个 Mordell–Weil 模块另作自由性假设。

## 4. 与单素数导出点之间还差什么

本篇选择的 $\ell+1=pu$ 满足 $p\nmid u$。
记 $U\subset G_\ell$ 为阶 $u$ 的子群，则 R104 的实际降域点为
$$
Q_{\ell,p}=\operatorname{Tr}_{U}X_\ell.
\tag{11}
$$
这是因为 R105 已把阶二类群代表的和吸收到 $X_\ell$ 中。
R104 的导出判据仍要求
$$
[Q_{\ell,p}]\ne0
\quad\text{于}\quad
\ker N_p/(\sigma_p-1)\ker N_p.
\tag{12}
$$
(7) 没有证明 (11) 的迹保留这些非零增广层；即使已知它保留，
约 $\log_2p$ 的长度也尚未达到导数对应的深层。
本篇不把这个差距隐藏在「原始性」一词中，也不由 (10) 推出
单素数 Kolyvagin 类非零。

## 5. 真实 prime-to-p 迹的一个额外因子可以由固定映射消去

这里可以将 (11) 的 $u$ 次迹再准确做完其中的一个因子 $2$，
并为所得点保留 (2)、(5)、(7) 的全部结论。

写 R105 的理想为 $\mathfrak r_{3,\ell}$、Artin 元为
$\tau_{3,\ell}$。另置
$$
\beta_\ell=\frac{5+\ell\sqrt{-15}}2,\qquad
\mathfrak r_{5,\ell}=(5,\beta_\ell),\qquad
k_\ell=\frac{5+3\ell^2}{4}.
\tag{13}
$$
$\mathcal O_\ell=\mathbb Z[\beta_\ell]$，且
$\beta_\ell^2=5\beta_\ell-5k_\ell$、$5\nmid k_\ell$。与 R105
完全相同的整数理想运算给
$$
\mathfrak r_{5,\ell}^2=(5),\qquad
N\mathfrak r_{5,\ell}=5.
\tag{14}
$$
故它可逆且 proper。其最大阶延拓为 $5$ 上方的分歧素理想
$\mathfrak r_5$。在 $\mathcal O_F$ 中
$$
\mathfrak r_3\mathfrak r_5=(\sqrt{-15}),
$$
所以 $[\mathfrak r_5]=[\mathfrak r_3]\ne1$。
Artin 元 $\tau_{5,\ell}$ 因而也恰有阶 $2$，并与
$\tau_{3,\ell}$ 在 $H_1$ 上有相同限制。

两者的乘积在 $G_\ell$ 中非平凡。事实上，
$\mathfrak r_{3,\ell}\mathfrak r_{5,\ell}$ 的范数为 $15$；若它主，
则 $\mathcal O_\ell$ 中存在范数 $15$ 的元素。
任意非实元素写成 $(a+b\ell\sqrt{-15})/2$，$b\ne0$，其范数至少为
$15\ell^2/4>15$；实元素是整数，其范数不等于 $15$。
所以
$$
\epsilon_\ell:=\tau_{3,\ell}\tau_{5,\ell}
\tag{15}
$$
是循环群 $G_\ell$ 的唯一阶二元。

因为 $p$ 为奇数，$\epsilon_\ell\in U$。定义实际迹点
$$
Z_\ell=(1+\epsilon_\ell)X_\ell
       =(1+\tau_{3,\ell})(1+\tau_{5,\ell})P[\ell].
\tag{16}
$$
最后一个等式使用 $\tau_{3,\ell}X_\ell=X_\ell$。
它不是把 $X_\ell$ 除以 $2$，而是 R104 所需的 prime-to-$p$ 迹
中真实发生的阶二子迹。

### 5.1 固定四分支模曲线映射

在 $X_0(15N_E)$ 上，对 $a\mid15$ 令 $d_a$ 为对阶 $a$ 子群取商、
同时运输 $N_E$ 层结构的退化映射。固定
$$
\Psi=\sum_{a\mid15}\pi\circ d_a:X_0(15N_E)\longrightarrow E.
\tag{17}
$$
对 $x_\ell$ 的 CM 曲线，同时选择
$\mathfrak r_{3,\ell}$、$\mathfrak r_{5,\ell}$ 决定的两个核。
它们与 $N_E$ 层结构两两互素，合成循环 $15N_E$ 子群，给出
$w_\ell\in X_0(15N_E)(H_\ell)$。
CM 互反律及 (14) 给精确等式
$$
\Psi(w_\ell)=Z_\ell.
\tag{18}
$$
两个理想类均等于自己的逆，因而相反的 Artin 规范不改变此式。
在无穷尖点，
$$
\Psi^*\omega_E
=c\bigl(f(q)+3f(q^3)+5f(q^5)+15f(q^{15})\bigr)\frac{dq}{q}.
\tag{19}
$$
$q$ 首系数为 $c\ne0$，故 $\Psi$ 是固定非恒定有限映射。
再次强调，这四个指定 CM 分支不等于对 $T_3T_5$ 的全部分支求和。

与 R105 相同的 CM 阶高度及固定 ample 比较遂给
$$
c\log\ell-C\le\widehat h(Z_\ell)\le C'\log\ell+C''.
\tag{20}
$$
于是对已经选定的 Linnik 辅助素数，同样有
$0<\widehat h(Z_\ell)\ll\log p$。
$F(w_\ell)=H_\ell$ 也由其 $j$ 值得到，因此 §2 的纤维证明在
$p>4\deg\Psi$ 时适用，§3 的全部不可除层结论同样适用。
特别地，每个充分大的输入 $p$ 都可用同一个辅助 $\ell$ 使
$$
Z_\ell\notin pE(H_\ell),\qquad
\Delta_p^kZ_\ell\notin pE(H_\ell)
\quad(0\le k\le K'_p),
\tag{21}
$$
其中 $K'_p=\log_2p-\tfrac12\log_2\log p+O(1)$。
必要时统一增大此前的固定常数，便可使 (7)、(21) 同时成立。

剩余的实际点现在准确为
$$
Q_{\ell,p}=\operatorname{Tr}_{U/\langle\epsilon_\ell\rangle}Z_\ell.
\tag{22}
$$
这个剩余次数是 $u/2$，并未变成 $1$；由于 $4\mid\ell+1$ 且
$p$ 为奇数，它仍为偶数。

## 6. 固定有界次数 CM 分支所能处理的范围

以下给出 (16) 使用分歧理想的一个准确边界，不排除其他全局方法。
固定 $\mathcal O_F$ 的一个非零整理想 $\mathfrak a$ 和整数 $m\ge1$。
对不除其范数的惰性素数 $\ell$，记
$\mathfrak a_\ell=\mathfrak a\cap\mathcal O_\ell$ 为相应
prime-to-$\ell$ 可逆理想。若 $[\mathfrak a_\ell]^m=1$ 对无穷多个
$\ell$ 成立，则
$$
\mathfrak a=\bar{\mathfrak a},\qquad
[\mathfrak a_\ell]\in
\langle[\mathfrak r_{3,\ell}],[\mathfrak r_{5,\ell}]\rangle
\quad\text{对全部这样的 }\ell.
\tag{23}
$$

证明：延拓到最大阶，先得固定主理想
$\mathfrak a^m=(\alpha)$。在那些 $\ell$ 上，若
$\mathfrak a_\ell^m=(\alpha_\ell)$，则延拓给
$(\alpha_\ell)=(\alpha)$。$\mathcal O_F^\times=\{\pm1\}$，所以
$\alpha_\ell=\pm\alpha$，从而 $\alpha\in\mathcal O_\ell$ 对无穷多个
$\ell$ 成立。这迫使 $\alpha\in\mathbb Z$。
因此 $\mathfrak a^m=\bar{\mathfrak a}^{m}$；整数理想的唯一分解给
$\mathfrak a=\bar{\mathfrak a}$。
一个共轭不变理想的分裂素数因子配对成有理主理想，惰性素数因子本身
也是有理主理想；只有分歧的 $3,5$ 可留下奇数指数。
这就给出 (23)。

特别地，任何固定有限组有界次数的 CM 同源分支，不能在无穷多个
$\ell$ 上实现 $G_\ell$ 中的阶四元。更直接地，若一个
prime-to-$\ell$ 整理想 $\mathfrak b_\ell$ 的类属于 $G_\ell$ 且恰有
阶四，则其范数满足
$$
N\mathfrak b_\ell\ge\ell/2.
\tag{24}
$$
事实上，其最大阶延拓为 $(\beta)$，且
$N\mathfrak b_\ell=N_{F/\mathbb Q}\beta$。
环类核的标准描述
$(\mathcal O_F/\ell)^\times/\mathbb F_\ell^\times$
将阶四条件写为 $(\beta/\bar\beta)^2=-1\pmod\ell$。
故非零整数 $\operatorname{Tr}_{F/\mathbb Q}(\beta^2)$ 被 $\ell$ 整除。
它非零，因为若为零，则 $\beta/\bar\beta\in F$ 是一个四次本原
单位根，与 $F\ne\mathbb Q(i)$ 矛盾。再由
$$
\ell\le|\operatorname{Tr}(\beta^2)|
\le2N_{F/\mathbb Q}\beta
$$
即得 (24)。

(23)–(24) 只限制以这些真实 CM 同源为单独分支的构造。
它们没有排除非显然的迹恒等式，也没有将一个次数随 $\ell$ 增长的
模曲线上的高度常数当作统一常数。后续若要做完 (22)，仍需补充
对变化对应或实际 Heegner 迹点的全局控制。

## 依据与复算

- 实际点、固定有限映射及辅助素数选择：
  [R105](2026-11-12-minus15-classgroup-trace-primitivity.md)。
- 统一高度下界与 $O(\log p)$ 高度预算：
  [R102](2026-11-12-heegner-height-and-augmentation-primitivity.md)，
  该文列有 Baker 的一手定理及全部高度来源。
- 实际 prime-to-$p$ 迹和增广商：
  [R104](2026-11-12-cyclic-heegner-augmentation-and-complete-reduction.md)。
- §1 的两个点数及 Frobenius 整数：
  [整数证书](../scripts/check-minus15-abelian-torsion.py)。
  Frobenius 交换、纤维和高度推理均在本文完整给出。
