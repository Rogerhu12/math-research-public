# 真实二面体增广块与可指定的基域范数线

日期：2026-11-12。状态：下列符号、整数商及 Chebotarev 命题已证明。
它们没有证明实际 Heegner 迹点的增广像非零。

取 $E:y^2=x^3-17x$、$P=(-1,4)$、$Q=(9,24)$，
以及已经固定的 $F=\mathbb Q(\sqrt{-15})$。
令 $p\ge7$ 在 $F$ 和 $\mathbb Q(i)$ 均分裂，且 $p\ne17$。
只在第 3 节另外排除 $P,Q$ 所生成子格的有限饱和指数的素因子。
令辅助素数满足
$$
\ell\equiv7\pmod {1020},\qquad
\ell\equiv p-1\pmod {p^2}.
\tag{1}
$$
于是 $\ell$ 在两个虚二次域均惰性，$a_\ell(E)=0$，且
$v_p(\ell+1)=1$。沿用 R104 的实际循环域
$L_p/F$，其次数为 $p$，以及整数点
$$
Q_{\ell,p}=\operatorname{Tr}_{F[\ell]/L_p}P[\ell],
\qquad NQ_{\ell,p}=0.
$$
R105 已经处理类数二的和；这里仍保留其余
$u=(\ell+1)/p$ 次迹，不将它删掉。

## 1. 实际点可用整数 Galois 平移放进负特征

记 $\tau$ 为 $\operatorname{Gal}(L_p/F)$ 的生成元，$c$ 为复共轭，
所以 $c\tau c=\tau^{-1}$。CM 点的复共轭与 Atkin–Lehner 公式给
$$
cQ_{\ell,p}=-\tau^aQ_{\ell,p}+T
\tag{2}
$$
某个 $a\bmod p$ 和一个基域挠点 $T$。
这里的负号来自 $w(E/\mathbb Q)=+1$：
在模参数化上，$w_N$ 的线性部分为 $-1$。
公式也可直接在模问题上得到：复共轭将定向的 $\mathfrak N$-同源
反向，再用 $w_N$ 恢复方向；所差的理想类作用在取 prime-to-$p$
迹后成为 $\tau^a$。参数化原点的改动只给基域 cusp 挠点。

对 (2) 取 $N=1+\tau+\cdots+\tau^{p-1}$，由于 $NQ_{\ell,p}=0$，
有 $pT=0$。R104 已证明 $E(L_p)[p]=0$，故 $T=0$。
选整数 $b$ 满足 $2b\equiv a\pmod p$，并置
$Q'_{\ell,p}=\tau^bQ_{\ell,p}$。则
$$
cQ'_{\ell,p}=-Q'_{\ell,p}.
\tag{3}
$$
这只使用真实 Galois 平移，没有把点除以 $2$ 或 $p$。
在增广商中 $Q'$ 和 $Q$ 的像相同。

令
$$
\mathsf M=\ker(N:E(L_p)\to E(F))\otimes\mathbb Z_p,
\qquad
\delta=\tau^{(p-1)/2}(\tau-1).
\tag{4}
$$
$\delta$ 与 $\tau-1$ 只差一个单位，且准确有
$$
c\delta c=-\delta.
\tag{5}
$$
因为 $2$ 在 $\mathbb Z_p$ 中可逆，$\mathsf M=\mathsf M^+\oplus\mathsf M^-$。
所以实际目标所在的块准确为
$$
\left(\mathsf M/\delta\mathsf M\right)^-
=\mathsf M^-/\delta\mathsf M^+.
\tag{6}
$$
它是被 $p$ 杀掉的有限群。实际单素数成功条件仍然是
$[Q'_{\ell,p}]\ne0$ 于 (6)，而不是仅有 $Q'_{\ell,p}\ne0$ 或
$Q'_{\ell,p}\notin p\mathsf M$。

## 2. 范数正特征与增广负特征的准确对应

R104 的整数正合列在 $p$ 部上为
$$
0\longrightarrow
NE(L_p)/pE(F)\longrightarrow
\mathsf M/(\tau-1)\mathsf M
\longrightarrow H^1(C_p,E(L_p))\longrightarrow0.
\tag{7}
$$
必须保留复共轭的扭转。左箭头将 $NZ$ 送到 $[(\tau-1)Z]$，
而在中间商里
$$
c[(\tau-1)Z]=-[(\tau-1)cZ].
$$
同样，循环 cocycle 由其在 $\tau$ 上的值识别时，
自然的复共轭作用将 $[R]$ 送到 $[-cR]$。
因此 (7) 的所需特征部分准确是
$$
0\longrightarrow
\bigl(NE(L_p)/pE(F)\bigr)^+
\longrightarrow\mathsf M^-/\delta\mathsf M^+
\longrightarrow H^1(C_p,E(L_p))^+
\longrightarrow0.
\tag{8}
$$
例如，若真正构造出 $Z\in E(L_p)$ 满足
$(\tau-1)Z=Q_{\ell,p}$，R104 的下降类就是
$-\delta_p(NZ)$。其正特征可与 $P,Q$ 比较。
对于实际 Heegner 点，该类满足通常 Selmer 条件，故 (8) 的实际
右侧像落在 $\Sha(E/F)[p]^+$。没有声称整个右项都属于 Sha。

令 $\lambda$ 为 $F$ 中 $\ell$ 上方的唯一素位。
$L_p/F$ 在 $\lambda$ 全分歧，次数为 $p$，剩余域不变。
由于 $E$ 在 $\ell$ 好约化且 $\ell\ne p$，准确有
$$
N_{(L_p)_\lambda/F_\lambda}E((L_p)_\lambda)
=pE(F_\lambda).
\tag{9}
$$
证明：约化的范数为乘 $p$；乘 $p$ 在形式群上是同构。
故范数像包含于 $pE(F_\lambda)$；反向将基域点视作扩域点，
其范数就是 $p$ 倍，得到等号。

在正特征上，$E(F)\otimes\mathbb Z_p$ 与 $E(\mathbb Q)\otimes\mathbb Z_p$
的识别无额外 $p$ 分母。因此令
$$
\rho_\ell:E(\mathbb Q)/pE(\mathbb Q)
\longrightarrow E(\mathbb F_\ell)/pE(\mathbb F_\ell)
$$
为约化映射，则
$$
\boxed{\quad
\bigl(NE(L_p)/pE(F)\bigr)^+\subseteq\ker\rho_\ell.
\quad}
\tag{10}
$$
这里可以用 $\mathbb F_\ell$ 而非 $\mathbb F_{\ell^2}$：次数为二的
剩余域扩张在模 $p$ 乘法商上为单射，直接用范数和 $2$ 的逆即可证明。

因 $a_\ell=0$ 且 $v_p(\ell+1)=1$，
$\#E(\mathbb F_\ell)=\ell+1$ 的 $p$ 部恰为 $p$，故
$E(\mathbb F_\ell)/pE(\mathbb F_\ell)\simeq\mathbb F_p$。
只要 $\rho_\ell$ 非零，(10) 就把实际基域范数像压到一维以下。

## 3. 可以指定这条实际约化核线

假设 $P,Q$ 在 $E(\mathbb Q)/pE(\mathbb Q)$ 中独立。
这只排除固定的有限素数集。
对每一条线
$$
\mathcal L\subset E(\mathbb Q)/pE(\mathbb Q)\simeq\mathbb F_p^2,
$$
存在正密度的辅助素数 $\ell$ 同时满足 (1) 与
$$
\rho_\ell\ne0,\qquad\ker\rho_\ell=\mathcal L.
\tag{11}
$$
因而 (10) 中的上界线可以任意预先指定。

### 3.1 两点的完整 Kummer 平移像

置 $T=E[p]$、$K=\mathbb Q(T)$。
R104 的 CM 惯性证明在 $\mathbb Q$ 上给
$$
G=\operatorname{Gal}(K/\mathbb Q)=N(C),
\qquad |G|=2(p-1)^2.
$$
$T$ 是绝对不可约 $\mathbb F_p[G]$-模，且
$\operatorname{End}_G(T)=\mathbb F_p$。
这也可直接由全部对角矩阵及交换两条线的矩阵验证。
中心 $-I$ 的 Sah 计算给 $H^1(G,T)=0$。

选 $p\widetilde P=P$、$p\widetilde Q=Q$，令
$B=K(\widetilde P,\widetilde Q)$。其平移群
$$
W=\operatorname{Gal}(B/K)\subset T\oplus T
$$
是 $G$ 子模。由于 $p\nmid|G|$，Maschke 分解适用。
若 $W\ne T\oplus T$，就有一条非零 $G$-映射
$(v_1,v_2)\mapsto av_1+bv_2$ 在 $W$ 上为零。
这意味着 $aP+bQ$ 的 Kummer 类在 $K$ 上为零；
Sah 和 inflation–restriction 使它在 $\mathbb Q$ 上也为零，
与 $P,Q$ 模 $p$ 独立矛盾。因此
$$
W=T\oplus T.
\tag{12}
$$

### 3.2 与要求 $M=1$ 的同余域相容

令 $C_0=\mathbb Q(\zeta_{1020p^2})$。
$[KC_0:K]$ 的 $p$ 部至多为 $p$。
另一方面，$B\cap KC_0$ 在 $\mathbb Q$ 上正规，
所以其在 $K$ 上的 Galois 群是 (12) 的一个 $G$ 商。
任何非零这样的商至少有阶 $p^2$。
两者矛盾，故
$$
B\cap KC_0=K.
\tag{13}
$$
因此加入 (1) 的完整模 $p^2$ 条件仍保留全部两点 Kummer 平移。

取 $\operatorname{Gal}(KC_0/\mathbb Q)$ 中一个元素 $h$，
其在 $C_0$ 上按 (1) 的剩余类作用。这样的 $h$ 存在，因为对 $C_0$
的限制满射。其在 $T$ 上的作用 $g$ 交换 CM 两条线，且
$\det g=-1$，所以
$$
g^2=1,\qquad \dim_{\mathbb F_p}T/(g-1)T=1.
$$
由 (12)–(13)，$h$ 在 $BC_0$ 中的所有提升可以任意改变两点的
Kummer 平移 $t_P,t_Q\in T$。
有限域的 Kummer 同构将 $P,Q$ 的约化像识别为
$$
t_P\bmod(g-1)T,\qquad t_Q\bmod(g-1)T.
$$
故能使这个非零线性函数恰有预定核 $\mathcal L$。
同时共轭只改变目标一维空间的基，不改变该核。
于是符合条件的 Frobenius 元素构成非空共轭稳定集合，
Chebotarev 给 (11) 的正密度结论。

## 4. 量词与尚未得到的结论

第 3 节固定 $p$ 后给正密度的 $\ell$，但没有给
$\log\ell=O(\log p)$ 的统一界。
因此不能把这些 $\ell$ 自动认作 R105 用 CRT 与 Linnik 选出的同一批
小辅助素数。R105 的 $X_\ell\notin pE(F[\ell])$ 与本文的指定核线
目前不能未经补充论证同时使用。

即使 $\ker\rho_\ell$ 是已知的一条线，(10) 只是实际全球范数像的
上界。没有由此证明该像非零，更没有证明
$Q_{\ell,p}$ 在 (6) 中的指定类非零。
若实际类位于 R104 的 Mordell–Weil 部分，(10) 决定它只能落在哪条
$P,Q$ 组合线上；是否存在该类及其系数是否非零，仍是当前条件。

## 输入与出处

- Howard（2004），*The Heegner point Kolyvagin system*；BCGS（2026），
  *Non-vanishing of Kolyvagin systems and Iwasawa theory*：实际点的范数、
  复共轭及通常 Selmer 条件使用 R100 已列明的原文接口。
- [R104](../results/R104-cyclic-heegner-augmentation-and-complete-reduction.md)：
  真实循环域、无 $p$ 挠点、完整 Cartan 正规化子及整数正合列。
- [R103](../results/R103-explicit-minus15-heegner-field.md)、
  [R105](../results/R105-minus15-classgroup-trace-primitivity.md)：固定 $F$、
  类数二求和与小辅助素数的原始性。
- 第 1–3 节其余比较、Kummer 像及同余域相容性均在本文证明。
