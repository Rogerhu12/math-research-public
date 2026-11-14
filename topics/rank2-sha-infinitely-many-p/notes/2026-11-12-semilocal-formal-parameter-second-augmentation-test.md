# 全部好约化型的半局部形式参数与二次增广测试

日期：2026-11-12。**已证明；实际测试的无穷非零性仍开。**

固定本题的 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$，以及
R119/R125 中实际环类子扩张 $L/F$、$\Gamma=\langle\tau\rangle=C_p$。
设 $p\ge7$、$p\ne17$，$L/F$ 在 $p$ 上不分歧；实际非挠点
$Q\in A(F)$ 属于
$$
A=\ker\bigl(N:\operatorname{Res}_{L/F}E\longrightarrow E\bigr),
\qquad
A(F)\widehat\otimes\mathbb Z_p=\mathcal O w,\quad
\mathcal O=\mathbb Z_p[\zeta_p],\quad Q=\delta^a\varepsilon w,
\tag{1}
$$
其中 $\delta=\tau^{(p-1)/2}(\tau-1)$ 在 $A$ 上作用，
$\varepsilon\in\mathcal O^\times$。下述局部构造不要求 $p$ ordinary，
也不要求 $p$ 在 $F$ 或 $\mathbb Q(i)$ 分裂。

删去 R122/R125 的固定有限例外，特别是整除已经有限的
$\Sha(E^{(-15)}/\mathbb Q)$ 的素数后，R127 §5 的纯代数推论是
$$
                         a\le1\quad\Longrightarrow\quad
                  \Sha(E/\mathbb Q)[p^\infty]=0.             \tag{2}
$$
该推论只用真实有限 Sha 的符号公式和长度界，不用高度非退化。
本篇以实际点的形式参数模 $p^2$ 给出 (2) 的充分证书。

## 1. 完整半局部模与两种分解

记
$$
\mathcal B=\mathcal O_F\otimes\mathbb Z_p,
\qquad \mathcal P=\mathcal O_L\otimes\mathbb Z_p
                   =\prod_{w\mid p}\mathcal O_{L_w},
\qquad I=\ker(N_\Gamma:\mathcal P\to\mathcal P).
\tag{3}
$$
这里 $p\nmid\operatorname{disc}(F)$。群作用包括不同完成之间的
置换；尤其在完全分裂情形，不能把 $\mathcal P$ 换成一个完成并
让整个 $\Gamma$ 在其上平凡作用。

对 $F$ 的每个 $v\mid p$，分解群因 $\#\Gamma=p$ 只能是 $1$
或 $\Gamma$。前者给 $p$ 个相同的完成和正则置换模；后者给
不分歧次数 $p$ 扩张。后者也有整正规基：从剩余域的正规基取
Teichmüller 提升，其共轭经 Nakayama 给出整基。因此
$$
                 \mathcal P\simeq\mathcal B[\Gamma],
\qquad I=(\tau-1)\mathcal P.                                \tag{4}
$$
这不是选择一个未知的非整正规基。$\mathcal P/I\simeq\mathcal B$
为 $p$-无挠模，所以 $I/pI\hookrightarrow\mathcal P/p\mathcal P$。

两种 $F$-分解的具体规范如下。

- 若 $p$ 在 $F$ 分裂，两素位的 Artin 元为 $s,s^{-1}$；
  $s=1$ 时两边均完全分裂，$s\ne1$ 时两边均为不分歧次数 $p$
  扩张。式 (3) 同时保留这两个块。
- 若 $p$ 在 $F$ 惰性，唯一素理想是由有理整数 $p$ 生成的
  $(p)$。它在环类群中平凡，因此在 $L/F$ 中完全分裂。
  此时 $\mathcal B$ 为不分歧二次整数环，
  $\mathcal P\simeq\mathcal B^p$，$\Gamma$ 置换这 $p$ 个因子。

后一事实也可由反循环性看出：固定素位的 Artin 元在复共轭下
不变，又被共轭送到逆，故在奇数阶群中只能是 $1$。

## 2. 一个实际、整且保持指数的 formalizer

对 $v\mid p$ 令 $f_v=[k_v:\mathbb F_p]\in\{1,2\}$，
$s_v=\operatorname{Art}_{L/F}(v)\in\Gamma$。写
$a_{p^f}=p^f+1-\#E(\mathbb F_{p^f})$，并取
$$
D_p=\prod_{v\mid p}
       \bigl(s_v^2-a_{p^{f_v}}s_v+p^{f_v}\bigr)
           \in\mathbb Z[\Gamma],\qquad R=D_pQ.              \tag{5}
$$
在任意 $w\mid v$ 的剩余域中，$s_v$ 对点的作用正是
$p^{f_v}$ 次 Frobenius。因此其特征多项式使相应因子杀掉
约化，故 $R$ 在所有 $w\mid p$ 都属于 formal group。
当 $s_v=1$ 时，该因子是实际整数
$\#E(\mathbb F_{p^{f_v}})$，同样杀掉约化。

本曲线有有理二挠点，所以 $a_p$ 为偶数。对 $p\ge7$，
$|a_p|\le2\sqrt p<p-1$，从而 $a_p\not\equiv\pm1\pmod p$。
又 $a_{p^2}=a_p^2-2p$，故
$$
D_p\equiv\prod_{v\mid p}(1-a_p^{f_v})\ne0
                         \pmod{(p,\tau-1)}.                \tag{6}
$$
于是 $D_p$ 在 $\mathbb Z_p[\Gamma]$ 及 $\mathcal O$ 中均为单位，
$R$ 在 (1) 的实际格中仍具有准确的指数 $a$。

若 $p$ 在 $F$ 分裂，(5) 就是
$$
(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p).
$$
若 $p$ 在 $F$ 惰性，(5) 是
$$
D_p=1-a_{p^2}+p^2=(p+1)^2-a_p^2.
$$
这也覆盖 $a_p=0$ 的超奇异情形。没有使用未构造的特征零
Frobenius 同源，只用了实际 Galois 作用在有限域点上的特征式。

## 3. 形式对数所需的准确精度

令 $t_E=-x/y$。在不分歧的 $p$ 进整数环中，好约化形式群给
$$
\log_E(t)=t+\sum_{n\ge2}\frac{c_n}{n}t^n,
\qquad c_n\in\mathbb Z_p.
$$
对 $t\in p\mathcal P$，$n-v_p(n)\ge2$，故
$$
\log_E(t)-t\in p^2\mathcal P,
\qquad \log_E:\widehat E(p\mathcal P)\xrightarrow\sim p\mathcal P.
\tag{7}
$$
最后的同构可由该整近恒等映射的 Hensel 逆得到；在此圆盘上
加法与对数级数均收敛。其 $\Gamma$-等变性来自模型和参数均在
$\mathbb Q$ 上定义。

由于 $N_\Gamma R=0$，
$$
z_R:=\frac{\log_E R}{p}\in I,
\qquad z_R\equiv\frac{t_E(R)}p\pmod{p\mathcal P}.           \tag{8}
$$
右边表示全部 $p$ 处参数的元组。它是逐个先除 $p$ 再取模，
没有把一次 norm/trace 的 $p$ 因子免费取消。

## 4. 精确二次增广核

定义整数群环元
$$
\mathcal D_2=\sum_{j=0}^{p-1}\binom j2\tau^j.
\tag{9}
$$
在 $\overline{\mathcal B}[\Gamma]
 =\overline{\mathcal B}[X]/(X^p)$ 中置 $X=\tau-1$。
对 $N(T)=1+T+\cdots+T^{p-1}$ 作两次形式求导，得到
$$
\mathcal D_2=\frac{\tau^2}2N''(\tau)
          =\tau^2(\tau-1)^{p-3}\pmod p.                    \tag{10}
$$
其中 $N(T)=(T-1)^{p-1}$ 于特征 $p$，且
$(p-1)(p-2)/2\equiv1$。所以在 $I/pI=X\overline{\mathcal B}[X]/X^p$
上，(10) 的核准确为 $X^3\overline{\mathcal B}[X]/X^p$。

这个剩余核有准确的整提升。分圆恒等式说明 $pI\subset(\tau-1)^2I$：
在 $I$ 上 $N_\Gamma=0$，而 $p$ 是 $(\tau-1)^{p-1}$ 的单位倍。
若 $z\in I$ 的约化属于 $X^3\overline{\mathcal P}$，可写
$z=(\tau-1)^3y+pw$；取 $N_\Gamma$ 得 $pN_\Gamma w=0$，
所以 $w\in I$。于是
$$
\boxed{\quad z\in I:\quad
 \mathcal D_2z\equiv0\pmod{p\mathcal P}
 \ \Longleftrightarrow\ z\in(\tau-1)^2I=\delta^2I.\quad}
\tag{11}
$$
特别地 $I/\delta^2I\simeq(\mathcal B/p\mathcal B)^2$，总
$\mathbb F_p$ 维数为 $4$。式 (11) 不丢掉 Artin 平凡的置换块。

作为对照，$\mathcal D_1=\sum j\tau^j$ 满足
$\mathcal D_1\equiv-\tau(\tau-1)^{p-2}\pmod p$，其在 $I$
上的核模 $p$ 提升为 $\delta I$。二次测试保留了可能的一次
可除层，正好匹配 (2) 的加强，而不是仍只检测 $a=0$。

## 5. 实际有限证书及其范围

定义实际半局部有限值
$$
\boxed{\quad
\mathcal T_{2,p}(Q)=
 \sum_{j=0}^{p-1}\binom j2
       \frac{t_E(\tau^j D_pQ)}p
           \pmod{p\mathcal P}.
\quad}                                                       \tag{12}
$$
它只需实际点的所有 $p$ 处参数模 $p^2$，其所在环为
$\mathcal P/p\mathcal P$。由 (8)–(11)，
$$
\mathcal T_{2,p}(Q)=0
\quad\Longleftrightarrow\quad z_R\in\delta^2 I.
\tag{13}
$$
右边也等价于 $R$ 在半局部 **formal 范数零群** 中可被
$\delta^2$ 除；用 (7) 的逆对 $pI$ 即得。这是准确局部等价，
没有将局部可除性当成全局可除性。

若 $a\ge2$，则 $Q\in\delta^2A(F)$。这一完整整数断言可由
R128 的有限商证明得到，也可直接注意 $pA(F)\subset\delta^2A(F)$，
故 $A(F)/\delta^2A(F)$ 是有限 $p$ 群，其 $p$ 进完成忠实。
取实际 $S\in A(F)$ 使 $Q=\delta^2S$。同一个 $D_p$ 使
$D_pS$ 在所有 $p$ 处 formal，且它仍范数零。于是
$z_R=\delta^2\log_E(D_pS)/p\in\delta^2 I$，(12) 必为零。
因此准确有
$$
\boxed{\quad \mathcal T_{2,p}(Q)\ne0
 \quad\Longrightarrow\quad a\le1
 \quad\Longrightarrow\quad\Sha(E/\mathbb Q)[p^\infty]=0.
 \quad}                                                       \tag{14}
$$
最后一箭头仍只排除开头所述固定有限集。它同时适用于 R123 的
普通输入和 R126 不限制约化型的无穷输入；没有假设后者与
ordinary 素数的交集无穷。

若需要沿用 R127 的 $R=12D_pQ$，(7) 使 (12) 整体只乘
$12\bmod p$，非零条件不变。本测试本身不涉及坏位高度，
所以不需要这个额外因子。

## 6. 哪一种“不自动为零”已经证明

整个局部范数零群并不使 (12) 自动为零。在 (4) 的任一整
正规基中取一个基生成元 $e$，则
$z=(\tau-1)e\in I$ 满足
$\mathcal D_2z\equiv\tau^2(\tau-1)^{p-2}e\ne0$。
另取 $z=(\tau-1)^2e$，则 $\mathcal D_1z=0$、
$\mathcal D_2z\ne0$ 于特征 $p$。用 (7) 取
$\exp_E(pz)$，这些确实对应实际半局部 formal 范数零点。

这只是 **ambient 局部群的非零性证书**，不是实际全局
Heegner 点 $Q$ 的非零性证书。全局 (1) 的秩一格在 $I$ 中
可能有额外局部可除指数，故 $a\le1$ 并不反向保证 (12)
非零；更不能由 $Q$ 非挠或 R120 的完整 norm 族就宣布它非零。
R120 的规范 Euler 因子在普通非异常子族为单位，与本篇
局部模相容，但未支付这条特定剩余行的非零性。

接下来仍须对实际 (12) 证明无穷非零，或从实际全局约束给出
另一种排除 $a\ge2$ 的方法。本篇没有将有限可计算条件当成
已经解决的素数变化问题。

## 依赖

- R119：实际范数核的完整 Mordell--Weil 秩及有限 Sha。
- R122、R125、R127 §5：任意充分大好素数上的纯代数充分条件
  $a\le1\Rightarrow\Sha(E/\mathbb Q)[p^\infty]=0$。
- R123、R126：两套已经证明的实际输入选择。
- R128：完整整数增广像与 $p$ 进格的比较；本篇只用其中
  $A(F)/\delta^2A(F)$ 为有限 $p$ 群的部分，不要求固定
  $61$ 的 Artin 元已经被选成生成元。

有限域正规基、Frobenius 特征式及形式对数所需精度已在
§§1–4 展开；本篇没有另借 ordinary 高度或未付的主猜想。
