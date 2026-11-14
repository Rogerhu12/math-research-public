# 一次共同截平将真实混合交集逼近推进至四次孔窗口

日期：2026-11-13（UTC）。作者：boundary_next；AI-assisted，GPT-6 Astra Pro。状态：已证明的中间结论；同时适用于两个实际边界慢核。已接顶部精确修复及真实稳定像提升；修复范数的统一控制仍未证明，尚未证明 $N=M$。

本稿接续 R254 第三至第六附录和 R239 的混合低孔正则提升。新的步骤是：对整个计算需要的孔层只截平一次，在同一截平模型里完成纯核投影与低方程修复，最后一次变回原坐标。这样不会在每个删除右逆上重复支付指数对角代价。原 Hilbert 尾始终在原坐标中直接截掉，平方误差的尾项系数准确为 $1$。

结果把此前 $q=25d^3$ 的同时交集窗口推进到
$$
q=100d^4,\qquad d=2^m.
$$
这里的交集仍只是纯尾高阶核、低混合方程及低孔截断的交集，绝不等于完整混合核。R254 第六附录已证明其顶部输出存在高尾精确修复；本稿第 8 节把该接口推进同一四次窗口，并支付包含修复范数在内的真实提升总误差。

并行主线 [R254第九附录](../results/R254-appendix-common-plateau-pure-power-inverse-and-one-third-stable-range.md) 已以 $q=25d^4$ 给出四次窗口及 $p>1/3$ 正则核饱和。本稿保留独立的 $q=100d^4$ 完整混合交集/顶部修复预算，并供最小图能量与正凸平均使用；不重复计四次窗口思想或 $1/3$ 阈值为新的范围。

## 1. 实际模型与唯一复用的输入

删除原首位后，前 $m$ 个尾位是原物理位 $1,\ldots,m$，令 $m\ge2$、$d=2^m$、$r=2d$。令
$$
b_j=(j+2)^{-2},\qquad
D=\sum_{j\ge m}b_jE_j,\qquad
\eta=\eta_0=e^{-1070}.
$$
$P_\ell$ 是高尾恰有 $\ell$ 个孔的正交投影，张量有限头恒等；位置不作有限性限制。真实有限头记为 $C_m,A_m$，其中 $C_m^d=0$，$A_m$ 是 $C_m$ 的零常数多项式。

实际平方符号和混合符号分别是
$$
P=A^2-\eta C,\qquad P_m=(A_m+D)^2-\eta C_m
\quad(N),
$$
$$
P=A^2-\eta C(I+A)^2,\qquad
P_m=(A_m+D)^2-\eta C_m(I+A_m+D)^2
\quad(Y).
$$
$Y$ 型已经乘实际有界可逆单位；只使用同核关系 $K=\ker P$，不据此保持原形式伴随源。

R254 第三附录给出
$$
\|A_m\|+\|D\|<\frac23,\qquad
\|P-P_m\|\le36\eta_m,
$$
$$
-\log\eta_m=1400d^4-630d^3+300d.
\tag{1.1}
$$
两种模型均有
$$
P_m=D^2+Q_m,\qquad
Q_m=\sum_{\ell=1}^{d-1}C_m^\ell R_{\ell,m}(D),\quad
\deg R_{\ell,m}\le2,
\tag{1.2}
$$
$$
\|Q_m\|<\frac12,\quad \|P_m\|<1,\quad Q_m^d=0.
$$
所有真实混合项，包括 $2A_mD$ 和 $Y$ 型的混合项，保留在 $Q_m$ 中。

伴随多项式
$$
\mathcal A_m=\sum_{k=0}^{d-1}(-Q_m)^kD^{2(d-1-k)}
$$
满足
$$
\mathcal A_mP_m=D^{2d},\qquad
\|\mathcal A_m\|\le d\,2^{1-d}.
$$
因此对实际 $u\in K$，
$$
\boxed{\|D^r u\|\le36d\,2^{1-d}\eta_m\|u\|.}
\tag{1.3}
$$
该多项式在尾孔次数上最多下降 $r-2$。下文会在截平模型中使用同一准确带宽。

记 $\tau_q(u)$ 为去掉原首位后按全部孔次数定义的普通 Hilbert 尾。高尾孔数大于 $q$ 蕴含全部孔数大于 $q$，故
$$
\|P_{>q}u\|\le\tau_q(u).
\tag{1.4}
$$

## 2. 一次共同截平和全空间对角界

有限对角截平以及纯有限头/纯尾模型的一次相似预算，已见 R239 纯创建附录 §5.1—§5.2。本稿不把这个思想本身列为新增；新增在于用同一个对角处理保留混合项的右逆、两个约束的相容修复、原坐标正交距离及实际四次窗口提升。

先取任意整数 $q\ge r$。令
$$
L=q+2d,\qquad J=2L+1,\qquad
W=m+J+2=m+2q+4d+3,\qquad \beta=W^{-2}.
\tag{2.1}
$$
把前 $J$ 个纯高尾位置 $j=m,\ldots,m+J-1$ 的系数全部截平为 $\beta$，其余保留 $b_j$，得到
$$
\widetilde b_j=
\begin{cases}
\beta,&m\le j<m+J,\\
b_j,&j\ge m+J,
\end{cases}
\qquad
\widetilde D=\sum_{j\ge m}\widetilde b_jE_j.
$$
全部 $\widetilde b_j\le\beta$，并且
$$
\sum_j\widetilde b_j^2\ge J\beta^2,\qquad
\|\widetilde D\|\le\|D\|.
$$

置 $\rho_j=b_j/\widetilde b_j\ge1$。对有限孔集 $F$，令
$$
S e_F=\Bigl(\prod_{j\in F}\rho_j\Bigr)e_F.
$$
只有这 $J$ 个位置的 $\rho_j$ 不为 $1$，所以 $S$ 是整个 Hilbert 空间上的有界正可逆对角算子，且
$$
\|S^{-1}\|\le1,\qquad [S,P_\ell]=0.
$$
直接核算删除一个孔前后的乘子，得到正确方向
$$
\boxed{S D=\widetilde D S.}
\tag{2.2}
$$
它在有限头上是恒等，因而也与 $C_m,A_m$ 交换。

全空间最大对角乘子在占据全部这 $J$ 个位置时取得，故
$$
\|S\|=
\left[\frac{W^J}{\prod_{k=0}^{J-1}(m+k+2)}\right]^2
\le\left[\frac{W^J}{J!}\right]^2.
$$
使用 $J!\ge(J/e)^J$ 和 $\log(1+x)\le x$，有
$$
\log\|S\|
\le2J+2J\log\left(1+\frac{m+2}{J}\right)
\le2J+2m+4.
$$
因此可以统一记
$$
\boxed{\|S\|\le s_{m,q}:=
\exp(4q+8d+2m+6).}
\tag{2.3}
$$
这是全空间界，不依赖输入在位置上的有限性。下文只支付这一个 $s_{m,q}$。

## 3. 同一截平模型上的所有所需右逆

记 $\widetilde C=\widetilde D^*$。真实局部 CCR 给
$$
\widetilde C^*\widetilde C-\widetilde C\widetilde C^*
=\sum_j\widetilde b_j^2(I-2n_j).
$$
在完整的 $\ell$ 孔层上，$\sum_jn_j=\ell I$。对 $0\le\ell\le L$，
$$
\|\widetilde C f\|^2
\ge \beta^2(J-2\ell)\|f\|^2
\ge\beta^2\|f\|^2.
\tag{3.1}
$$
故存在实际有界层右逆
$$
\widetilde G_\ell:\mathcal H_\ell\longrightarrow\mathcal H_{\ell+1},
\qquad
\widetilde D\widetilde G_\ell=I,\qquad
\|\widetilde G_\ell\|\le\beta^{-1}=W^2=:k.
\tag{3.2}
$$
例如取创建算子的通常有界左逆后再取伴随。它定义在完整孔层，不要求保持有限位置支撑。

复合 $r$ 次，$\widetilde D^r:\mathcal H_p\to\mathcal H_{p-r}$ 对 $r\le p\le q$ 有范数至多 $k^r$ 的右逆。设 $\widetilde\Pi$ 为 $\ker\widetilde D^r$ 的正交投影。核按孔层分解，故
$$
\boxed{
\|P_{\le q}(I-\widetilde\Pi)z\|
\le k^r\|\widetilde D^r z\|,
\qquad z\in H.
}
\tag{3.3}
$$
证明是逐层从 $z_p$ 减去上述实际右逆作用于 $\widetilde D^r z_p$，再用最佳逼近和各层正交性。这里没有把斜投影的范数当成 $1$。

再定义
$$
\widetilde P_m=S P_m S^{-1}
=\widetilde D^2+\widetilde Q_m.
\tag{3.4}
$$
这不是只用 $\|S\|\|P_m\|\|S^{-1}\|$ 作粗估计。由精确多项式形式，
$$
\widetilde Q_m
=\sum_{\ell=1}^{d-1}C_m^\ell R_{\ell,m}(\widetilde D).
$$
因为 $\|A_m\|+\|\widetilde D\|<2/3$，原 $N/Y$ 的同一正范数预算直接给
$$
\|\widetilde Q_m\|<\tfrac12,\qquad
\|\widetilde P_m\|<1,\qquad
\widetilde Q_m^d=0.
\tag{3.5}
$$
所以这里没有第二个对角条件数。

令 $\widetilde H$ 为逐层二次右逆
$$
\widetilde H_\ell=\widetilde G_{\ell+1}\widetilde G_\ell,
\quad
\widetilde D^2\widetilde H=I,\quad
\|\widetilde H_\ell\|\le k^2.
$$
它只作用纯尾，故与 $C_m$ 交换。严格头过滤仍给
$$
(\widetilde Q_m\widetilde H)^d=0
$$
于本稿所需的有限孔域上成立，无须交换 $\widetilde H$ 与 $\widetilde Q_m$。

对输入孔数至多 $q-2$，定义
$$
\widetilde{\mathcal G}_m
=\widetilde H\sum_{j=0}^{d-1}(-\widetilde Q_m\widetilde H)^j.
\tag{3.6}
$$
每项最多升 $2d$ 孔，所有中间层不超过 $q+2d-2<L$，所以 (3.2) 覆盖了每一次实际运算。有限几何恒等式给
$$
\boxed{
\widetilde P_m\widetilde{\mathcal G}_m=I,\qquad
\widetilde{\mathcal G}_m\mathcal H_{\le q-2}
\subseteq\mathcal H_{\le q+2d-2}.
}
\tag{3.7}
$$
同时
$$
\boxed{
\|\widetilde{\mathcal G}_m|_{\mathcal H_{\le q-2}}\|
\le\sum_{j=0}^{d-1}2^{-j}k^{2j+2}
\le d\,k^{2d}=:B.
}
\tag{3.8}
$$
关键是 $k=W^2$ 只有多项式增长；所有层共享同一次截平。

## 4. 在截平模型中相容地修复两组约束

对实际 $u\in K$，置
$$
z=Su,\qquad x=\widetilde\Pi z.
$$
由 (1.3)、(2.2)、(2.3)、(3.3)，
$$
\|P_{\le q}(z-x)\|
\le\varepsilon\|u\|,
\qquad
\varepsilon=36d\,2^{1-d}\eta_m s_{m,q}k^{2d}.
\tag{4.1}
$$
没有在这里估计整个 $z-x$ 的高孔尾。

令
$$
r_0=P_{\le q-2}\widetilde P_mx,\qquad
c=\widetilde{\mathcal G}_m r_0.
\tag{4.2}
$$
第一项准确满足
$$
\widetilde P_m z=S P_m u=S(P_m-P)u,
$$
故其范数至多 $36\eta_m s_{m,q}\|u\|$。
另一方面 $\widetilde P_m$ 最多下降两孔，所以
$$
P_{\le q-2}\widetilde P_m(z-x)
=P_{\le q-2}\widetilde P_mP_{\le q}(z-x).
$$
结合 (3.5)，
$$
\|r_0\|
\le(36\eta_m s_{m,q}+\varepsilon)\|u\|
\le2\varepsilon\|u\|.
\tag{4.3}
$$
末步使用 $d2^{1-d}k^{2d}\ge1$，这由 $k\ge2$ 立即成立。注意未知高尾没有进入 (4.3)。

为核实兼容性，定义截平模型的伴随多项式
$$
\widetilde{\mathcal A}_m
=\sum_{j=0}^{d-1}(-\widetilde Q_m)^j
\widetilde D^{2(d-1-j)}.
$$
准确有
$$
\widetilde{\mathcal A}_m\widetilde P_m=\widetilde D^{2d},
$$
且尾次数带宽仍是只下降 $0,\ldots,2d-2$。
由 $x\in\ker\widetilde D^{2d}$，
$$
\widetilde{\mathcal A}_m r_0
=-\widetilde{\mathcal A}_mP_{>q-2}\widetilde P_mx.
$$
右边的源次数至少为 $q-1$，最多下降 $2d-2$，所以输出次数至少为 $q-2d+1$。又
$$
\widetilde D^{2d}c
=\widetilde{\mathcal A}_m\widetilde P_mc
=\widetilde{\mathcal A}_m r_0.
$$
按 $\widetilde D^{2d}$ 的严格分级性比较次数，得到
$$
\boxed{P_{\le q}c\in\ker\widetilde D^{2d}.}
\tag{4.4}
$$
这里没有交换核投影和右逆。

因此
$$
y=x-P_{\le q}c
$$
仍在 $\ker\widetilde D^{2d}$ 中。再由
$\widetilde P_mc=r_0$ 和
$P_{\le q-2}\widetilde P_mP_{>q}c=0$，得到
$$
P_{\le q-2}\widetilde P_my=0.
\tag{4.5}
$$
最后
$$
\|P_{\le q}(z-y)\|
\le(\varepsilon+2B\varepsilon)\|u\|
\le3B\varepsilon\|u\|.
\tag{4.6}
$$

## 5. 一次变回原坐标；真实低孔交集的正交距离

定义闭空间
$$
\boxed{
\mathcal W_{m,q}
=\ker D^{2d}\cap\mathcal H_{\le q}
\cap\ker(P_{\le q-2}P_m).
}
\tag{5.1}
$$
它不包含任何“投影后仍满足混合核”的假设。取实际候选
$$
v=S^{-1}P_{\le q}y.
\tag{5.2}
$$
$S$ 保持孔层，(2.2) 保持高阶核；截掉 $y$ 的 $>q$ 部分也不会改变低于等于 $q-2$ 的混合输出。因此 $v\in\mathcal W_{m,q}$。

低孔误差由 $S^{-1}$ 的收缩性控制：
$$
\|P_{\le q}(u-v)\|
\le3B\varepsilon\|u\|.
\tag{5.3}
$$
高孔部分准确就是 $P_{>q}u$，而不是它的共轭或斜投影。两个部分正交，故
$$
\boxed{
\operatorname{dist}(u,\mathcal W_{m,q})^2
\le\tau_q(u)^2+\rho_{m,q}^2\|u\|^2,
}
\tag{5.4}
$$
其中可以取完全显式的
$$
\boxed{
\rho_{m,q}
=108d^2\eta_m
\exp(4q+8d+2m+6)
(m+2q+4d+3)^{8d}.
}
\tag{5.5}
$$
这是把 $3B\varepsilon$ 中可用的因子 $2^{1-d}\le1$ 丢掉后的上界。

令 $v_{m,q}$ 为 $u$ 到 $\mathcal W_{m,q}$ 的实际正交投影，则同样满足 (5.4)，并有
$$
\|v_{m,q}\|\le\|u\|.
\tag{5.6}
$$
对这个向量，
$$
\boxed{
P_m v_{m,q}
\in\ker D^{2d}\cap
(\mathcal H_{q-1}\oplus\mathcal H_q).
}
\tag{5.7}
$$
纯核条件来自 $P_mD^{2d}=D^{2d}P_m$，两层支撑来自低方程和不升次数。这仍可能是非零向量。

如需 R254 第五附录的未截低孔空间
$$
\mathcal V_{m,q}=\ker D^{2d}\cap\ker(P_{\le q-2}P_m),
$$
则 $\mathcal W_{m,q}\subseteq\mathcal V_{m,q}$，所以 (5.4) 当然也给到 $\mathcal V_{m,q}$ 的距离界。其正交投影与粗 $P_{\le q}$ 交换，低块正是到 $\mathcal W_{m,q}$ 的投影；高块是原度量下的纯核投影。这些都是实际闭子空间的正交投影，不是 $S^{-1}\widetilde\Pi S$ 的范数声明。

## 6. 四次窗口的统一数值预算

取
$$
q=100d^4,\qquad m\ge2,\qquad d=2^m\ge4.
\tag{6.1}
$$
由 (5.5) 和 (1.1)，
$$
\begin{aligned}
\log\rho_{m,q}\le{}&
-1000d^4+630d^3-292d+2m+6\\
&+8d\log(m+200d^4+4d+3)+\log(108d^2).
\end{aligned}
\tag{6.2}
$$
使用
$$
m+200d^4+4d+3\le201d^4,\quad
\log201<6,\quad
\log d\le d/2,
$$
$$
2m\le d,\qquad \log(108d^2)\le4d,
$$
并丢掉负项 $-292d$，(6.2) 的正余量不超过
$$
630d^3+16d^2+53d+6<200d^4
\quad(d\ge4).
$$
于是
$$
\boxed{\rho_{m,100d^4}\le e^{-800d^4}.}
\tag{6.3}
$$
最终得到本稿主结论：
$$
\boxed{
\operatorname{dist}\!\left(
u,\,
\ker D^{2d}\cap\mathcal H_{\le100d^4}
\cap\ker(P_{\le100d^4-2}P_m)
\right)^2
\le
\tau_{100d^4}(u)^2+e^{-1600d^4}\|u\|^2.
}
\tag{6.4}
$$
全部 $m\ge2$ 适用；没有只写渐近 $o(1)$，也没有未知尾乘指数常数。

更一般地，本证明在任意 $q\ge2d$ 给出 (5.4)—(5.5)。若 $q=\lfloor\lambda d^4\rfloor$，固定 $0<\lambda<350$，则
$$
\log\rho_{m,q}
\le-\bigl(1400-4\lambda+o(1)\bigr)d^4.
\tag{6.5}
$$
不声明端点 $\lambda=350$。这里的常数 $4$ 来自方便的全空间截平对角界，并非最优阈值声明。

## 7. 同一个四次窗口仍可接已证明的正则提升

本节先检查完整混合核的提升预算，下一节再接已发布的顶部精确修复。修复向量范数的统一控制仍未证明。

R239 正则提升已经构造
$$
G_{7\to3}:X_7\to X_3,\qquad TG_{7\to3}=I,\qquad
\|G_{7\to3}\|\le C_G=\frac43e^{4Q_0},\quad Q_0=2^{22}.
$$
对真正的混合核低孔交集
$$
\mathcal U_{m,Q}=\ker P_m\cap\mathcal H_{\le Q},
$$
有
$$
\Lambda_{m,Q}=J_m-G_{7\to3}TJ_m:
\mathcal U_{m,Q}\longrightarrow M\cap X_3\subseteq N,
$$
$$
\|\Lambda_{m,Q}v-J_mv\|_{X_3}
\le\delta_{m,Q}\|v\|,
$$
$$
\delta_{m,Q}
=130C_G\sqrt{(2m+5)(Q+m+2)}
e^{7(Q+2m+3)}\eta_m.
\tag{7.1}
$$
这些是既有的所有 $Q$ 都成立的精确公式；旧稿的 $Q=50d^3$ 只是一次代入。

现在仍取 $Q=q=100d^4$，并令 $m\ge4$、$d\ge16$。直接代入：
$$
\begin{aligned}
\log\delta_{m,q}={}&
-700d^4+630d^3-300d+2^{24}\\
&+14m+21+\log(520/3)
+\tfrac12\log((2m+5)(100d^4+m+2)).
\end{aligned}
\tag{7.2}
$$
其中
$$
630d^3\le40d^4,\qquad
2^{24}\le256d^4.
$$
余下的正对数项至多 $d^2\le d^4$：例如用
$2m+5\le2d$、$100d^4+m+2\le101d^4$、
$14m\le7d$，它们总和至多
$7d+30+\tfrac52\log d\le d^2$。
因此 (7.2) 至多 $-403d^4$，特别
$$
\boxed{\delta_{m,100d^4}\le e^{-400d^4},\qquad m\ge4.}
\tag{7.3}
$$
同时 $27\eta_m\le e^{-1360d^4}$。

对实际图向量 $w=Ju\in M$，既有投影不等式因而扩大为
$$
\boxed{
\operatorname{dist}(w,N)
\le\frac54\operatorname{dist}(u,\mathcal U_{m,100d^4})
+2e^{-400d^4}\|u\|.
}
\tag{7.4}
$$
若 $w\in D=M\ominus N$，则 $\|u\|\le\|w\|$，所以
$$
\boxed{
\operatorname{dist}(u,\mathcal U_{m,100d^4})
\ge\frac45(1-2e^{-400d^4})\|w\|.
}
\tag{7.5}
$$

(6.4) 的空间是 $\mathcal W_{m,q}$，而 (7.4) 需要 $\mathcal U_{m,q}$。二者的差别恰是 (5.7) 的两层输出。下一节通过高尾项修好这一差别并支付实际提升；仍不提供该高尾项的一致范数界。

## 8. 四次窗口内的精确高尾修复及真实缺陷必要条件

本节接续 R254 第六附录的精确修复方法，新的部分是共同截平预算在更大的 $q=100d^4$ 窗口仍足够。

### 8.1 同一截平右逆覆盖顶部输入

(3.6) 的同一有限几何和也可作用于输入孔数至多 $q$ 的向量：其最高输出为 $q+2d=L$，每次二次右逆所需的层指标不超过 $L-1$，仍在 (3.2) 的范围内。故
$$
\mathcal R_{m,q}
=S^{-1}\widetilde{\mathcal G}_m S
\tag{8.1}
$$
是真正的 $P_m$ 右逆，定义在整个 $\mathcal H_{\le q}$ 上，输出在 $\mathcal H_{\le q+2d}$。

由于 $\widetilde H$ 严格升两次孔，$\widetilde Q_m\widetilde H$ 不降孔，每个单层输入满足
$$
\boxed{
\mathcal R_{m,q}\mathcal H_p
\subseteq\bigoplus_{j=p+2}^{p+2d}\mathcal H_j
\quad(0\le p\le q).
}
\tag{8.2}
$$
$S,S^{-1}$ 保持孔次数，所以最低输出次数在变回原坐标后也准确保持。

此次输入只在 $\le q$ 孔，因而不必支付 (2.3) 的全空间对角界。因所有 $\rho_j\ge1$，各层最大乘子随层数递增；又 $J>q$，故
$$
\|S|_{\mathcal H_{\le q}}\|
=\|S|_{\mathcal H_q}\|
\le\left(\frac{W^q}{q!}\right)^2
\le\exp\left[2q\left(1+\log\frac Wq\right)\right].
\tag{8.3}
$$
当 $q=100d^4,m\ge2$ 时，
$$
W=2q+4d+m+3\le\frac{21}{10}q.
$$
由 $\log(21/10)<3/4$，得到
$$
\boxed{\|S|_{\mathcal H_{\le q}}\|\le e^{7q/2}.}
\tag{8.4}
$$
这个小于全空间 $e^{4q+O(d)}$ 的输入界，只在此处用于顶部残量；前面的同时交集逼近仍使用其已付的全空间界。

结合 (3.8) 及 $\|S^{-1}\|\le1$，可取
$$
\boxed{
\|\mathcal R_{m,q}\|
\le B^\sharp_{m,q}:=
d\,W^{4d}e^{7q/2}.
}
\tag{8.5}
$$
若 $m\ge4,d\ge16$，则
$$
\begin{aligned}
\log B^\sharp_{m,q}
&\le350d^4+\log d+4d\log(201d^4)\\
&\le350d^4+8d^2+\tfrac{49}{2}d
<351d^4.
\end{aligned}
$$
因此
$$
\boxed{B^\sharp_{m,100d^4}\le e^{351d^4},\qquad m\ge4.}
\tag{8.6}
$$
这保留了第六附录原 $q=25d^3$ 预算中的同一上界数字，但覆盖了 $100d^4$ 的孔窗口。

### 8.2 针对固定实际核向量的具体修复序列

固定 $u\in K$，令 $v_m$ 是到 $\mathcal W_{m,q}$ 的实际正交投影，$q=100d^4$。因为 $\mathcal W_{m,q}\subseteq\mathcal H_{\le q}$，其最佳逼近的低部误差由 (5.3) 的候选控制：
$$
\|v_m-P_{\le q}u\|
\le e^{-800d^4}\|u\|,\qquad
\|v_m\|\le\|u\|,\qquad
v_m\longrightarrow u.
\tag{8.7}
$$
这里低部结论使用了真实低孔子空间的最佳逼近性，并非从总距离中删去未知尾项。

置
$$
r_m=P_mv_m,\qquad
c_m=\mathcal R_{m,q}r_m,\qquad
k_m=v_m-c_m.
\tag{8.8}
$$
由 (5.7)、(8.1)、(8.2)，
$$
\boxed{
P_mk_m=0,\qquad
c_m\in\bigoplus_{j=q+1}^{q+2d}\mathcal H_j,\qquad
P_{\le q}k_m=v_m.
}
\tag{8.9}
$$
再用原模型的伴随多项式，
$$
D^{2d}c_m
=\mathcal A_mP_mc_m
=\mathcal A_mP_mv_m
=D^{2d}v_m=0.
$$
所以 $c_m,k_m$ 都在纯高阶核内，且
$$
k_m\in\ker P_m\cap\mathcal H_{\le q+2d}.
$$
低孔向量和高尾修复正交：
$$
\|k_m\|^2=\|v_m\|^2+\|c_m\|^2.
\tag{8.10}
$$

因为 $P_m$ 不升孔，
$$
r_m=P_{\{q-1,q\}}P_mP_{\{q-1,q\}}v_m.
$$
于是
$$
\boxed{
\|r_m\|
\le \|P_{\{q-1,q\}}u\|
+e^{-800d^4}\|u\|
\longrightarrow0.
}
\tag{8.11}
$$
上界 (8.5) 给
$$
\|c_m\|\le B^\sharp_{m,q}\|r_m\|,
\qquad
\|c_m\|\le e^{351d^4}\|u\|,
\qquad
\|k_m\|\le2e^{351d^4}\|u\|.
\tag{8.12}
$$

### 8.3 支付包含大修复范数的真实稳定像提升

取 $Q=q+2d$。把它代入精确公式 (7.1) 后，(7.2) 只增加 $14d$，并把对数中的 $q+m+2$ 换成 $q+2d+m+2$。
对 $d\ge16$，仍有
$$
q+2d+m+2\le101d^4.
$$
因此除了 $630d^3$ 和 $2^{24}$ 之外的正项至多 $d^2+14d\le2d^2\le d^4$。丢掉负项 $-300d$，得到
$$
\boxed{
\delta_{m,q+2d}\le e^{-403d^4},\qquad m\ge4.
}
\tag{8.13}
$$
定义真实稳定像向量
$$
n_m=\Lambda_{m,q+2d}k_m\in N.
\tag{8.14}
$$
由 (8.12)—(8.13)，
$$
\begin{aligned}
\|n_m-(J_mv_m-J_mc_m)\|
&\le\delta_{m,q+2d}\|k_m\|\\
&\le2e^{-52d^4}\|u\|
\le e^{-50d^4}\|u\|.
\end{aligned}
$$
所以
$$
\boxed{
\|n_m-(J_mv_m-J_mc_m)\|
\le e^{-50d^4}\|u\|,\qquad m\ge4.
}
\tag{8.15}
$$
这里已经乘入完整的高尾修复范数上界，不是只证明 $\delta_{m,q+2d}\to0$。

$J_m$ 在高尾孔次数上最多下降一次，故 $J_mc_m$ 只支持高尾孔数 $[q,q+2d]$。而 (8.7) 和 $\|J_m-J\|\le27\eta_m$ 给
$$
J_mv_m\longrightarrow Ju.
\tag{8.16}
$$
这还不能单凭固定低孔坐标收敛推出 $n_m$ 弱收敛，因为 $\|c_m\|$ 尚可能发散。

### 8.4 实际缺陷迫高尾修复发散；有界子列仍足够

若 $0\ne w=Ju\in D=M\ominus N$，由 $n_m\in N$、(8.15)、(8.16)，
$$
\langle J_mc_m,w\rangle\longrightarrow\|w\|^2.
$$
用 $\|J_m\|\le5/4$ 和准确的高尾支撑，得到充分大 $m$ 时
$$
\boxed{
\|c_m\|\tau_{q-1}(w)
\ge\frac25\|w\|^2,\qquad q=100d^4.
}
\tag{8.17}
$$
这里 $\tau_{q-1}(w)$ 是原全部物理孔数超过 $q-1$ 的尾。结合 (8.5)、(8.11)，也有
$$
\boxed{
B^\sharp_{m,q}
\bigl(\|P_{\{q-1,q\}}u\|
+e^{-800d^4}\|u\|\bigr)
\tau_{q-1}(w)
\ge\frac25\|w\|^2.
}
\tag{8.18}
$$
特别，非零真缺陷迫这条具体的新修复序列满足 $\|c_m\|\to\infty$。

反过来，对任意实际 $u\in K$，如果这条具体序列 $c_m$ 沿子列有界，那么移动高孔支撑使 $J_mc_m$ 沿该子列弱趋零。由 (8.15)—(8.16)，对应 $n_m\in N$ 弱趋 $Ju$。闭线性子空间 $N$ 弱闭，故
$$
\boxed{
\sup_\ell\|c_{m_\ell}\|<\infty
\quad\Longrightarrow\quad Ju\in N.
}
\tag{8.19}
$$
没有声称这个充分条件已经对全部实际核向量成立，也没有声称 $Ju\in N$ 反过来迫这条指定修复序列有界。

## 9. 结论的精确范围

新结果同时支付了以下几点：整个交集逼近只出现一次截平对角；截平模型保留全部真实混合项；所有右逆在完整有限孔层上有真实定义域；伴随多项式带宽使两个核约束相容；原坐标正交距离的未知尾平方系数为 $1$；同一个四次窗口上的顶部精确高尾修复仍有 $\log B^\sharp\le351d^4$；把这个可能很大的修复范数乘入后，真实 $N$ 提升误差仍趋零。

顶部修复的存在现在已证明，不能再把“是否能消掉两层”列为未证。真正剩余项是：对固定实际核向量产生的这条特殊残量序列，能否选择或控制高尾修复，使其有有界子列。当前只有 $B^\sharp_{m,q}\|r_m\|$ 上界；$\|r_m\|\to0$ 的无速率事实不能吸收 $B^\sharp_{m,q}$ 的增长。尤其不能把低坐标保持、进位修正趋零或环境右逆界当成修复范数已经有界。

本稿没有构造非零实际缺陷，也没有证明 $N=M$。后续直接研究 (8.8) 的特殊修复范数或允许更佳选择的最小高尾修复；不再重复顶部修复存在性和已付的实际提升。

参考的已发布完整证明：
- [R239 纯创建与一次截平纯模型](../results/R239-appendix-pure-tail-creation-exponential-singular-bounds.md)，特别 §5.1—§5.2；
- [R254 纯高尾高阶约束](../results/R254-appendix-high-order-pure-tail-kernel-constraint-without-similarity.md)；
- [R254 保混合有限孔右逆](../results/R254-appendix-mixed-finite-hole-right-inverse-and-equation-repair.md)；
- [R254 同时交集逼近](../results/R254-appendix-simultaneous-pure-kernel-and-low-mixed-equation-approximation.md)；
- [R254 顶部精确修复与稳定像提升](../results/R254-appendix-exact-top-layer-repair-stable-lift-and-defect-norm-obstruction.md)；
- [R239 混合低孔正则提升](../results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)。
