# 惰性 ray 层的两素数 Robert 导数及 Norm 计算边界

本稿给 R201、R202 的一个自含结构接口，不声称已经计算未知 $L$。它只使用已发表的 Robert Norm 关系、Hilbert 90、局部 reciprocity、R168 的同一个 Selmer 坐标和 Chebotarev；不把未发表的一般 Euler-system–Kolyvagin-system 定理作为黑盒。

结论是：若 $q\equiv-1\pmod{4p}$、$\gamma_q=0$、$\lambda_q\ne0$，则在下面固定的正 tame 规范中，真实 $q$-ray Robert 单位的原始导数满足

$$
\boxed{\kappa'_q=2i\lambda_q d_0\quad\text{模 }p.} \tag{E.1}
$$

特别其系数是单位。对 $p=43,\lambda_q=16$，该系数为 $32i$，逆为 $4i$。这给出 Hilbert 90 构造 Norm 见证时的准确非零指数。它不提供 $776$ 位素数 $q$ 的全部 $q$-挠点，也不把该巨大层的直接枚举称作执行算法。

## 1. 字符、ray 扩张及确切 Euler 输入

采用 R163 的 $K=\mathbf Q(i)$、$A:y^2=x^3-x$、惰性 $p>37$，以及原始 Robert 生成元 $d_0$。令 $F=K(A[p])^{\mathbf F_p^\times}$，$\operatorname{Gal}(F/K)$ 的阶为 $p+1$，取系数环 $\mathcal O=\mathbf Z_{p^2}$。在其忠实单位字符 $\widetilde\chi(a)=\widetilde a^{p-1}$ 分量工作；经同一个 Kummer/系数识别，其模 $p$ 正下降是 $W(1)$。

对有理惰性素数 $l\equiv-1\pmod{4p}$，记 $K(l)/K$ 为 ray 模 $(l)$ 中的唯一次数 $p$ 子扩张。因为 $K$ 类数一、$p\nmid4$，这个子扩张存在；共轭对它作用为取逆。选生成元 $\sigma_l$，使 R168 同一 Weil 根所定义的 tame 角色取值为 $1$。

在 $F K(n)$、$n\mid qr$，选固定辅助理想 $(11)$ 的 Robert 单位，并取到这些子域的 Norm、同一 $\widetilde\chi$ 投影及整体单位倍数归一化，使底层类为 $d_0$。以下用加法记号写这些单位 $c_n$。其完整范数关系是

$$
N_l c_n=(1-\operatorname{Fr}_l^{-1})c_{n/l}. \tag{E.2}
$$

所有角色分量中的单位根项为零。辅助 $(11)$ 的因子 $121-\widetilde\chi(-11)=120$ 是 $p$ 单位，且有理标量在反循环 ray 层作用平凡，因此这一步不会引入一个待除的零 Euler 因子。整体归一化可以与 $d_0$ 的固定 $i$ 因子及复共轭下降同时相容。

式 (E.2) 是 R163 §5 已逐字核过的已发表 Oukhaba–Viguié §4、印刷页155的两分支 Norm 式在新增素数情形的直接应用。提高同一个 $p$ 素数的导子时则无新增 Euler 因子，因此也可同时选择相容的 cyclotomic $\mathbf Z_p$ 层。

## 2. 两个惰性素数的相互 Frobenius 恰为一

若 $q,r$ 都为上述惰性有理素数，则 $(q)$ 在 $K(r)/K$ 全分裂，$(r)$ 在 $K(q)/K$ 全分裂。理由是该素理想由复共轭固定，而扩张的 Galois 群为奇阶、共轭作用取逆；所以其 Frobenius 同时等于自身及自身的逆，只能为一。

此外在 $F/K$ 中，惰性有理素数的 CM Frobenius 为有理标量 $-l$，被 $\mathbf F_p^\times$ 商杀掉。因此 $q,r$ 在 $F$ 中也全分裂。式 (E.2) 在本稿涉及的有限层简化为

$$
N_q c_q=N_r c_r=N_q c_{qr}=N_r c_{qr}=0. \tag{E.3}
$$

这就是本特例比一般两素数导数更简单的原因：通常由两 ray 层相互 Frobenius 产生的 permutation correction 在这里为零。没有将一般情形的 correction 擅自删除。

## 3. 只用 Norm 关系证明局部 congruence

令 $m_l=(l^2-1)/p$。在 $l$ 处，(E.2) 蕴含

$$
\overline c_n=\overline c_{n/l}^{\,m_l}
\qquad(l\mid n,\ n\mid qr). \tag{E.4}
$$

这里给出可以除以 $p$ 的理由，避免从单个有限剩余域中的 $p$ 倍等式非法消去 $p$。将所有单位提升到同时相容的 cyclotomic $\mathbf Z_p$ 层。在 $l$ 上新增 ray 层全分歧，取剩余后 $N_l$ 是乘 $p$；算术 Frobenius 在剩余单位上是乘 $l^2$。所以 Norm 关系给

$$
p\,u_l(c_n)=(l^2-1)\operatorname{Fr}_l^{-1}u_l(c_{n/l})
$$

于剩余单位的相容逆极限。$l$ 不会在 cyclotomic $\mathbf Z_p$ 扩张中完全分裂；其 $p$ 主剩余单位的 Norm 逆极限是无 $p$ 挠的秩一 $\mathbf Z_p$ 模。故可在逆极限中除以 $p$，然后投到当前有限层。当前有限层 $\operatorname{Fr}_l$ 为一，得到 (E.4)。其他 ray 层在 $l$ 全分裂，因此每个分支都适用同一等式。

若只需要模 $p$ 的坐标，可先选整数群环投影代表再取剩余；改变投影代表的 $p$ 倍不会改变 (E.4) 的 $\mu_p$ 值。

## 4. 单素数导数就是一个真实 Norm

令 $D_l=\sum_{j=0}^{p-1}j\sigma_l^j$，则

$$
(\sigma_l-1)D_l=p-N_l.
$$

由 (E.3) 和 Hilbert 90，存在 $\beta_l$ 使 $(\sigma_l-1)\beta_l=c_l$。定义

$$
\kappa'_l=D_lc_l-p\beta_l=-N_l\beta_l\in F^\times\otimes\mathcal O. \tag{E.5}
$$

所以 $\kappa'_l$ 是 $-\beta_l$ 的 Norm。其模 $p$ 类与 Hilbert 90 解的选择无关。在 $l$ 处，它属于从 $K(l)$ 的局部 Norm 线；由于 $l$ 是有理数且反循环角色杀有理数，该 Norm 线模 $p$ 就是横截线，即 R168 的有限坐标为零。

在 $2,p,l$ 外，$c_l$ 是单位，新增扩张不分歧，(E.5) 给基域赋值被 $p$ 整除。因此其 Kummer 类不在外部产生新分歧。

## 5. 两素数导数的 local Norm 性也可直接证明

在 $F K(q)K(r)$ 中，指定

$$
(\sigma_q-1)\beta_{qr}=D_rc_{qr},\qquad
(\sigma_r-1)\beta_{qr}=D_qc_{qr}.
$$

两式确实构成一个 $\Gamma_q\times\Gamma_r$ 的 $1$-cocycle：各方向的 Norm 为零，交叉差都等于 $pc_{qr}$，由 (E.3) 可直接核对。一般 Hilbert 90 给相容的 $\beta_{qr}$。令

$$
\kappa'_{qr}=D_qD_rc_{qr}-p\beta_{qr}.
$$

它被两个群固定，故属于基域，而且

$$
\kappa'_{qr}=-N_q\beta_{qr}=-N_r\beta_{qr}. \tag{E.6}
$$

在 $q$ 处 $K(r)$ 完全分裂，因而 (E.6) 是一个真正的 $q$-局部 Norm；在 $r$ 处同理。故两个有限坐标都为零。此处没有使用一般 Kolyvagin 系统的半单性、自由性或核心顶点定理。

## 6. 有限–奇异因子准确为 $-2i$

取 R168 的同一局部标架 $F_l,K_l=JF_l$ 和 tame 根。对一个正下降的 $W(1)$ 类，其在 $\mathbf Q_l$ 的有限坐标为 $cK_l$、奇异坐标为 $dF_l$。限制到未分歧二次 $K_{(l)}$ 后，有限坐标为 $2ic$，奇异坐标为 $d$（在所选一维字符坐标中把 $F_l$ 识别为 $1$）。

对 (E.5) 或 (E.6) 中的 Hilbert 90 解，在 $l$ 处设赋值为 $t$。因为 $\sigma_l$ 对一致化参数的比值是固定的 $\zeta$，(E.4) 给

$$
\zeta^t=(\overline{\kappa'_{n/l}})^{m_l}.
$$

而 $\kappa'_n=-N_l\beta_n$ 的赋值是 $-t$。所以

$$
\operatorname{sing}_l(\kappa'_n)
=-\operatorname{finite}_{K_{(l)}}(\kappa'_{n/l}). \tag{E.7}
$$

对另一个 ray 方向出现的 $\beta_{n/l}$，可以在 $l$ 处乘一个基域元使其成为单位；这只改变 $\kappa'_{n/l}$ 的 $p$ 次幂，不改变 (E.7)。

复共轭把 $D_l$ 模 $p$ 变成 $-D_l$。将底层 Robert 家族选成与 $d_0$ 相同的正下降后，原始 $\kappa'_n$ 的共轭奇偶为 $(-1)^{\nu(n)}$。因此定义

$$
\kappa_n=(-2i)^{-\nu(n)}\kappa'_n. \tag{E.8}
$$

它们都下降到同一个 $\mathbf Q$ 上的 $W(1)$。式 (E.7) 恰变为

$$
\operatorname{sing}_l(\kappa_n)
=\operatorname{finite}_l(\kappa_{n/l}),\qquad
\operatorname{finite}_l(\kappa_n)=0\ (l\mid n). \tag{E.9}
$$

这解释了不能把原始 $q$ 导数直接当作与 $d_0$ 具有相同共轭奇偶的类；缺少的 $i$ 和二次限制因子在 (E.8) 中均保留。

## 7. 辅助素数存在与两行线性代数

令 $w_q$ 为 R168 的严格 $p$ primal 类，其 $q$ 奇异坐标为 $1$。选一个惰性 $r\equiv-1\pmod{4p}$，使

$$
\gamma_r=\operatorname{finite}_r(d_0)\ne0,
\qquad u=\operatorname{finite}_r(w_q)\ne0. \tag{E.10}
$$

这样的 $r$ 存在。限制到完整除法域 $T$ 后，$d_0,w_q$ 给两个非零不可约模 $W(1),W$ 的加法扩张。这两个模不同：标量 Cartan 在 $W$ 上平凡、在 $W(1)$ 上不平凡。因 $p\nmid|\operatorname{Gal}(T/\mathbf Q)|$，联合像是两者的直和。可以在真实复共轭 coset 中同时选择两个非零有限方向，再用 Chebotarev。若需要还可加 cyclotomic 模 $p^2$ 条件取得 $v_p(r+1)=1$；该额外平凡模与两非平凡模不混同。

记 $d_q^*,d_r^*$ 为奇异坐标分别为 $1$ 的 dual 类。全局 reciprocity 与 $w_q$ 严格 $p$ 给

$$
\operatorname{finite}_q(d_r^*)=u.
$$

因为 $\gamma_q=0$，(E.9) 使 $\kappa_q=e d_0$。在 $r$ 处横截和奇异条件给

$$
\kappa_r=\gamma_r d_r^*-\lambda_r d_0.
$$

再用 (E.9)，$\kappa_{qr}$ 的 $q,r$ 奇异坐标分别是 $\gamma_ru$、$e\gamma_r$。所以在基 $d_0,d_q^*,d_r^*$ 中

$$
\kappa_{qr}=\gamma_ru\,d_q^*+e\gamma_r d_r^*+t d_0.
$$

其 $q$ 有限坐标必须为零，得到

$$
0=\gamma_ru\lambda_q+e\gamma_ru
=\gamma_ru(\lambda_q+e).
$$

由 (E.10) 可消去非零因子，故 $e=-\lambda_q$。用 (E.8) 还原原始导数即得 (E.1)。

## 8. Hilbert 90 的显式和及它没有计算出的量

对普通单位坐标，若 $N u_q=1$，可取

$$
V=\sum_{j=0}^{p-1}\prod_{k=0}^{j-1}\sigma^k u_q.
$$

则 $V/\sigma V=u_q$。在当前 $\gamma_q=0$ 分量，可选整数投影代表使 $\overline u_q=1$；于是 $\overline V=p\ne0$，这个 Hilbert 90 和确实不为零。

原始导数为 $[NV]$。由 (E.1)，在正确的角色坐标中

$$
NV/U_0^{\,2i\lambda_q}=Z^p.
$$

这里的角色系数可用两个普通整数幂坐标表示；$2i\lambda_q$ 的可逆性允许将二者解回 R201 的目标 $U,V$。若已取得左侧的实际元素，只需在**基域**取 $p$ 次根并除掉 $Z$，不必再计算扩张域的全单位基。外支撑的除子亦在这一基域修正中清除；若不实际清除，则使用 R200 附属笔记的正号 Artin 修正。

但是 $\overline V=p$ 不能推出规范剩余量 $L$ 已知。未知恰藏在全局 $p$ 次根 $Z$ 的 $q$ 剩余值和外支撑 Artin 中。也不能把形式的 $q$ 层 Robert 单位当成已经可在给定的次数 $43$ 模型内算出的元素：从 $q$-挠点直接构造它会遇到 $776$ 位 $q$ 的不可接受枚举。本稿目前只把指数和有限–奇异规范闭合。

真正可执行的下一输入仍是：用 R191 已有的 cyclic $43$ 模型直接获得一个适合的 Norm/Hilbert 90 元素，或证明将该基域根/Artin 量与 R204 固定 $\{2,p\}$ 二阶 Frobenius 严格相连的互反式。没有这条连接，不能把 R204 的 $24$ 或 R189 的 $10$ 代入未知 $L$。

## 9. 来源及发表状态边界

- Oukhaba–Viguié, *On the Gras Conjecture for Imaginary Quadratic Fields*, Canadian Mathematical Bulletin **56** (2013), 148–160，§4 印刷页155：新增素数/已有素数的 Robert Norm 关系。
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf>
- Scholl, *An introduction to Kato's Euler systems* (1998), Theorem 1.2.1(iii)、Remark(iv),(v)，印刷页384–386：规范函数的同源分布。
  <https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf>
- Burns–Sakamoto–Sano, arXiv:1903.09509，Appendix A 给一般基域的导数构造；作者主页在本轮检索时仍标为 preprint。本稿仅将其作为检查方向的参考，所用惰性两素数特例已在 §§2–7 直接证明，不调用该预印本的定理。
  <https://arxiv.org/abs/1903.09509>
  <https://sites.google.com/site/takamichisanomath/home/research>
- R163、R168、R171、R191、R200、R201、R204：固定字符、局部规范、真实支撑及同一个数值实例。
